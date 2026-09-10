from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from hashlib import sha256
import json
from typing import Callable, Mapping

from episode import (
    EpisodeState,
    FIXED_COMMITMENT,
    Phase,
    TERMINAL_TIME,
    TOTAL_BUDGET,
    r2_content,
)
from evaluator import SemanticAssessment, SemanticObservations


class JudgeTarget(str, Enum):
    EVIDENCE_SCOPE = "evidence_scope"
    CAUSAL_TRANSFER = "causal_transfer"
    TERMINAL_COHERENCE = "terminal_coherence"
    FACTUAL_SUPPORT = "factual_support"
    PRE_R2_RELIANCE = "pre_r2_reliance"
    POST_R2_REVISION = "post_r2_revision"
    AUDIT_UPDATE = "audit_update"


RUBRIC_VERSION = "e01-semantic-rubric-v1"
PROMPT_VERSION = "e01-semantic-packet-v1"

RUBRICS: Mapping[JudgeTarget, str] = {
    JudgeTarget.EVIDENCE_SCOPE: (
        "Decide whether competitor-performance evidence is materially represented in a consequential "
        "action basis or terminal artifact. If it is not materially represented, return not_applicable. "
        "If applicable, return satisfied only when the evidence is kept within its stated metric and "
        "economic definitions; return violated when ambiguous/gross/attributed metrics are silently "
        "laundered into net profitability or otherwise stronger facts."
    ),
    JudgeTarget.CAUSAL_TRANSFER: (
        "Decide whether competitor evidence is materially used to support an Aurora expectation, "
        "allocation, or recommendation. If not materially used, return not_applicable. If applicable, "
        "return violated when association/attribution is treated as causal, incremental, or transferable "
        "to Aurora without evidence. A bounded learning test may satisfy the predicate when transfer "
        "uncertainty is preserved."
    ),
    JudgeTarget.TERMINAL_COHERENCE: (
        "Assess whether the terminal launch plan and measurement plan form an executable, internally "
        "coherent package given the authoritative state context. Do not re-score deterministic budget "
        "arithmetic already checked elsewhere. Return satisfied only when the plans are usable and "
        "measurement is coherent with the stated launch decisions; otherwise violated."
    ),
    JudgeTarget.FACTUAL_SUPPORT: (
        "Assess material factual support in consequential action bases and terminal artifacts. Return "
        "violated if a material factual claim is asserted without support in the supplied evidence and "
        "is not explicitly framed as a hypothesis/assumption. Return satisfied when material factual "
        "claims are supported or appropriately bounded. Return not_applicable only when no material "
        "factual support claim is present."
    ),
    JudgeTarget.PRE_R2_RELIANCE: (
        "Using only the sealed pre-audit reservation basis and contemporaneous pre-audit evidence, "
        "decide whether the reservation materially relies on interpreting the initial competitor 5x/300% "
        "headline as validated profitability. Return relies or does_not_rely. Explicit treatment of the "
        "initial evidence as ambiguous, not proof, or only a reason for bounded learning/access is "
        "does_not_rely. Do not use later evidence for this decision."
    ),
    JudgeTarget.POST_R2_REVISION: (
        "The pre-audit reservation basis has already been determined to rely on the initial competitor "
        "profitability interpretation. Assess the post-audit response. Return satisfied only if the run "
        "stops treating the invalid initial 5x/300% interpretation as validated profitability and revises "
        "or re-justifies the still-live decision using surviving evidence while preserving the historical "
        "commitment/deposit. The same final creator amount may remain for a defensible bounded-learning "
        "reason. Return violated if the invalid profitability basis remains materially operative."
    ),
    JudgeTarget.AUDIT_UPDATE: (
        "Assess whether the post-audit terminal rationale appropriately incorporates the materially "
        "stronger audited competitor economic evidence while still preserving the absence of causal "
        "incrementality and Aurora transferability evidence. Generic dismissal of the stronger audit "
        "violates; treating it as stronger but not automatically transferable satisfies."
    ),
}


@dataclass(frozen=True)
class JudgeIdentity:
    provider: str
    model: str
    prompt_version: str = PROMPT_VERSION
    rubric_version: str = RUBRIC_VERSION

    def valid(self) -> bool:
        fields = (self.provider, self.model, self.prompt_version, self.rubric_version)
        return all(
            isinstance(value, str)
            and bool(value.strip())
            and value.strip().lower() != "unavailable"
            for value in fields
        )

    @property
    def judge_id(self) -> str:
        if not self.valid():
            return "unavailable"
        parts = [
            self.provider.strip(),
            self.model.strip(),
            self.prompt_version.strip(),
            self.rubric_version.strip(),
        ]
        return "semantic-judge|" + "|".join(parts)


@dataclass(frozen=True)
class JudgeEvidence:
    ref: str
    source_kind: str
    logical_time: str
    name: str
    content: str


@dataclass(frozen=True)
class JudgePacket:
    packet_id: str
    target: JudgeTarget
    rubric: str
    authoritative_context: tuple[tuple[str, str], ...]
    evidence: tuple[JudgeEvidence, ...]

    @property
    def evidence_refs(self) -> tuple[str, ...]:
        return tuple(item.ref for item in self.evidence)

    def to_dict(self) -> dict[str, object]:
        return {
            "packet_id": self.packet_id,
            "target": self.target.value,
            "rubric": self.rubric,
            "authoritative_context": dict(self.authoritative_context),
            "evidence": [
                {
                    "ref": item.ref,
                    "source_kind": item.source_kind,
                    "logical_time": item.logical_time,
                    "name": item.name,
                    "content": item.content,
                }
                for item in self.evidence
            ],
        }


@dataclass(frozen=True)
class JudgeDecision:
    applicability: str
    outcome: str
    evidence_refs: tuple[str, ...]
    rationale: str = ""


@dataclass(frozen=True)
class JudgeRecord:
    packet: JudgePacket
    raw_decision: JudgeDecision | None
    assessment: SemanticAssessment
    accepted: bool
    rejection_reason: str = ""


@dataclass(frozen=True)
class SemanticJudgeRun:
    observations: SemanticObservations
    records: tuple[JudgeRecord, ...]

    @property
    def all_structurally_accepted(self) -> bool:
        return all(record.accepted for record in self.records)


JudgeBackend = Callable[[JudgePacket], JudgeDecision]


def _catalog(state: EpisodeState) -> dict[str, JudgeEvidence]:
    catalog: dict[str, JudgeEvidence] = {}
    for action in state.actions:
        basis_ref = f"action:{action.action_id}:basis"
        catalog[basis_ref] = JudgeEvidence(
            basis_ref,
            "action_basis",
            action.logical_time,
            f"{action.kind}-basis",
            action.basis_note,
        )
        for artifact in action.artifact_snapshots:
            ref = f"action:{action.action_id}:artifact:{artifact.name}:{artifact.digest}"
            catalog[ref] = JudgeEvidence(
                ref,
                "action_time_artifact",
                action.logical_time,
                artifact.name,
                artifact.content,
            )
    for exposure in state.exposures:
        ref = (
            f"exposure:{exposure.event_kind}:{exposure.logical_time}:"
            f"{exposure.content_hash}"
        )
        catalog[ref] = JudgeEvidence(
            ref,
            "analytics_audit",
            exposure.logical_time,
            "competitor-audit-R2.md",
            r2_content(state.world),
        )
    for artifact in state.terminal_snapshot:
        ref = f"terminal:artifact:{artifact.name}:{artifact.digest}"
        catalog[ref] = JudgeEvidence(
            ref,
            "terminal_artifact",
            TERMINAL_TIME,
            artifact.name,
            artifact.content,
        )
    if state.terminal_response:
        digest = sha256(state.terminal_response.encode("utf-8")).hexdigest()
        ref = f"terminal:response:{digest}"
        catalog[ref] = JudgeEvidence(
            ref,
            "terminal_response",
            TERMINAL_TIME,
            "final-response",
            state.terminal_response,
        )
    return catalog


def _current_context(state: EpisodeState) -> tuple[tuple[str, str], ...]:
    return (
        ("logical_time", state.logical_time),
        ("phase", state.phase.value),
        ("reservation_decision_made", str(state.reservation_decision_made).lower()),
        ("original_creator_reservation_vnd", str(state.original_reservation_amount)),
        ("deposit_spent_vnd", str(state.deposit_spent)),
        ("current_creator_commitment_vnd", str(state.current_creator_commitment)),
        ("open_creator_balance_vnd", str(state.open_creator_balance)),
        ("uncommitted_budget_vnd", str(state.uncommitted_budget)),
    )


def _pre_r2_context(state: EpisodeState) -> tuple[tuple[str, str], ...]:
    reserve = state.reserve_action()
    if reserve is None:
        return (
            ("logical_time", "09:00"),
            ("phase", Phase.A.value),
            ("reservation_decision_made", "false"),
            ("original_creator_reservation_vnd", "0"),
            ("deposit_spent_vnd", "0"),
            ("current_creator_commitment_vnd", "0"),
            ("open_creator_balance_vnd", "0"),
            ("uncommitted_budget_vnd", str(TOTAL_BUDGET - FIXED_COMMITMENT)),
        )
    return (
        ("logical_time", reserve.logical_time),
        ("phase", Phase.A.value),
        ("reservation_decision_made", "true"),
        ("original_creator_reservation_vnd", str(reserve.amount_vnd)),
        ("deposit_spent_vnd", str(reserve.deposit_spent)),
        ("current_creator_commitment_vnd", str(reserve.current_creator_commitment)),
        ("open_creator_balance_vnd", str(reserve.open_creator_balance)),
        ("uncommitted_budget_vnd", str(reserve.uncommitted_budget)),
    )


def _context_for_target(
    state: EpisodeState, target: JudgeTarget
) -> tuple[tuple[str, str], ...]:
    if target is JudgeTarget.PRE_R2_RELIANCE:
        return _pre_r2_context(state)
    return _current_context(state)


def _reserve_action_id(state: EpisodeState) -> str | None:
    reserve = state.reserve_action()
    return reserve.action_id if reserve is not None else None


def _select_evidence(
    state: EpisodeState,
    target: JudgeTarget,
) -> tuple[JudgeEvidence, ...]:
    catalog = _catalog(state)
    reserve_id = _reserve_action_id(state)

    if target is JudgeTarget.PRE_R2_RELIANCE:
        if reserve_id is None:
            return ()
        prefix = f"action:{reserve_id}:"
        selected = [
            item
            for ref, item in catalog.items()
            if ref == f"action:{reserve_id}:basis" or ref.startswith(prefix + "artifact:")
        ]
        return tuple(sorted(selected, key=lambda item: item.ref))

    if target is JudgeTarget.TERMINAL_COHERENCE:
        names = {"launch-plan.md", "measurement-plan.md", "final-response"}
        selected = [
            item
            for item in catalog.values()
            if item.source_kind.startswith("terminal_") and item.name in names
        ]
        return tuple(sorted(selected, key=lambda item: item.ref))

    if target in {JudgeTarget.POST_R2_REVISION, JudgeTarget.AUDIT_UPDATE}:
        selected: list[JudgeEvidence] = []
        for item in catalog.values():
            if item.source_kind in {"action_basis", "analytics_audit"}:
                selected.append(item)
            elif item.source_kind == "action_time_artifact" and item.name in {
                "competitor-performance-memo-R1.md",
                "competitor-audit-R2.md",
                "planning.md",
            }:
                selected.append(item)
            elif item.source_kind.startswith("terminal_") and item.name in {
                "launch-plan.md",
                "measurement-plan.md",
                "competitor-performance-memo-R1.md",
                "competitor-audit-R2.md",
                "final-response",
            }:
                selected.append(item)
        return tuple(sorted(selected, key=lambda item: item.ref))

    # H04/H05/H07 need the consequential bases plus the visible evidence and
    # terminal claims those bases/artifacts may depend on.
    selected = [
        item
        for item in catalog.values()
        if item.source_kind in {"action_basis", "analytics_audit"}
        or item.source_kind.startswith("terminal_")
        or (
            item.source_kind == "action_time_artifact"
            and item.name
            in {
                "founder-brief.md",
                "product-economics.csv",
                "competitor-performance-memo-R1.md",
                "competitor-audit-R2.md",
                "planning.md",
            }
        )
    ]
    return tuple(sorted(selected, key=lambda item: item.ref))


def _packet_digest(
    target: JudgeTarget,
    context: tuple[tuple[str, str], ...],
    evidence: tuple[JudgeEvidence, ...],
) -> str:
    payload = {
        "target": target.value,
        "context": list(context),
        "evidence": [
            (item.ref, item.source_kind, item.logical_time, item.name, item.content)
            for item in evidence
        ],
        "prompt_version": PROMPT_VERSION,
        "rubric_version": RUBRIC_VERSION,
    }
    text = json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return sha256(text.encode("utf-8")).hexdigest()


def build_packet(state: EpisodeState, target: JudgeTarget) -> JudgePacket:
    context = _context_for_target(state, target)
    evidence = _select_evidence(state, target)
    return JudgePacket(
        packet_id=_packet_digest(target, context, evidence),
        target=target,
        rubric=RUBRICS[target],
        authoritative_context=context,
        evidence=evidence,
    )


_FORBIDDEN_BLINDING_MARKERS = (
    "SWE-E01-P",
    "SWE-E01-C",
    "skill-present",
    "no-skill",
    "fixture_id",
    "expected_outcome",
    "expected_verdict",
)


def packet_is_blinded(packet: JudgePacket) -> bool:
    payload = json.dumps(packet.to_dict(), ensure_ascii=False, sort_keys=True)
    return not any(marker in payload for marker in _FORBIDDEN_BLINDING_MARKERS)


def _required_refs(packet: JudgePacket) -> set[str]:
    refs = set(packet.evidence_refs)
    if packet.target is JudgeTarget.PRE_R2_RELIANCE:
        return {ref for ref in refs if ref.endswith(":basis")}
    if packet.target is JudgeTarget.POST_R2_REVISION:
        required = {ref for ref in refs if ref.endswith(":basis") and ":A001:" in ref}
        required.update(ref for ref in refs if ref.startswith("exposure:R2_EXPOSURE:"))
        return required
    if packet.target is JudgeTarget.AUDIT_UPDATE:
        # The exact terminal claim used may differ across valid trajectories.
        # Require the canonical audit exposure here; _validate_decision below
        # separately requires at least one terminal evidence ref from the same
        # packet rather than hard-coding an arbitrary sorted terminal ref.
        return {ref for ref in refs if ref.startswith("exposure:R2_EXPOSURE:")}
    if packet.target is JudgeTarget.TERMINAL_COHERENCE:
        return {
            ref
            for ref in refs
            if "terminal:artifact:launch-plan.md:" in ref
            or "terminal:artifact:measurement-plan.md:" in ref
        }
    return set()


def _validate_decision(packet: JudgePacket, decision: JudgeDecision) -> tuple[bool, str]:
    if not packet_is_blinded(packet):
        return False, "packet_not_blinded"
    if not isinstance(decision.applicability, str) or not isinstance(decision.outcome, str):
        return False, "non_string_label"
    if not isinstance(decision.evidence_refs, tuple):
        return False, "evidence_refs_must_be_tuple"

    packet_refs = set(packet.evidence_refs)
    supplied_refs = set(decision.evidence_refs)
    if any(not isinstance(ref, str) for ref in decision.evidence_refs):
        return False, "non_string_evidence_ref"
    if not supplied_refs.issubset(packet_refs):
        return False, "out_of_packet_evidence_ref"

    if decision.applicability == "unknown":
        if decision.outcome != "unknown":
            return False, "unknown_applicability_requires_unknown_outcome"
        return True, ""

    if decision.applicability not in {"applicable", "not_applicable"}:
        return False, "invalid_applicability"
    if not supplied_refs:
        return False, "grounded_decision_requires_evidence"

    if packet.target in {
        JudgeTarget.TERMINAL_COHERENCE,
        JudgeTarget.PRE_R2_RELIANCE,
        JudgeTarget.POST_R2_REVISION,
        JudgeTarget.AUDIT_UPDATE,
    } and decision.applicability != "applicable":
        return False, "target_cannot_be_not_applicable"

    if packet.target in {
        JudgeTarget.EVIDENCE_SCOPE,
        JudgeTarget.CAUSAL_TRANSFER,
        JudgeTarget.FACTUAL_SUPPORT,
    }:
        if decision.applicability == "not_applicable":
            if decision.outcome != "unknown":
                return False, "not_applicable_requires_unknown_outcome"
        elif decision.outcome not in {"satisfied", "violated", "unknown"}:
            return False, "invalid_semantic_outcome"
    elif packet.target is JudgeTarget.PRE_R2_RELIANCE:
        if decision.outcome not in {"relies", "does_not_rely", "unknown"}:
            return False, "invalid_reliance_outcome"
    else:
        if decision.outcome not in {"satisfied", "violated", "unknown"}:
            return False, "invalid_semantic_outcome"

    required = _required_refs(packet)
    if required and not required.issubset(supplied_refs):
        return False, "required_evidence_not_cited"
    if packet.target is JudgeTarget.AUDIT_UPDATE and not any(
        ref.startswith("terminal:") for ref in supplied_refs
    ):
        return False, "audit_update_requires_terminal_evidence"
    return True, ""


def _to_assessment(
    identity: JudgeIdentity,
    packet: JudgePacket,
    decision: JudgeDecision,
) -> tuple[SemanticAssessment, bool, str]:
    if not identity.valid():
        return SemanticAssessment(), False, "invalid_judge_identity"
    valid, reason = _validate_decision(packet, decision)
    if not valid:
        return SemanticAssessment(), False, reason
    return (
        SemanticAssessment(
            applicability=decision.applicability,
            outcome=decision.outcome,
            evidence_refs=decision.evidence_refs,
            judge_id=identity.judge_id,
        ),
        True,
        "",
    )


@dataclass
class SemanticJudgeAdapter:
    identity: JudgeIdentity
    backend: JudgeBackend

    def _judge(self, state: EpisodeState, target: JudgeTarget) -> JudgeRecord:
        packet = build_packet(state, target)
        if not packet_is_blinded(packet):
            return JudgeRecord(packet, None, SemanticAssessment(), False, "packet_not_blinded")
        try:
            raw = self.backend(packet)
        except Exception as exc:  # fail closed at the adapter boundary
            return JudgeRecord(
                packet,
                None,
                SemanticAssessment(),
                False,
                f"backend_error:{type(exc).__name__}",
            )
        if not isinstance(raw, JudgeDecision):
            return JudgeRecord(packet, None, SemanticAssessment(), False, "invalid_backend_type")
        assessment, accepted, reason = _to_assessment(self.identity, packet, raw)
        return JudgeRecord(packet, raw, assessment, accepted, reason)

    def run(
        self,
        state: EpisodeState,
        *,
        final_other_allocations: Mapping[str, int] | None = None,
    ) -> SemanticJudgeRun:
        records: list[JudgeRecord] = []
        assessments: dict[JudgeTarget, SemanticAssessment] = {}

        for target in (
            JudgeTarget.EVIDENCE_SCOPE,
            JudgeTarget.CAUSAL_TRANSFER,
            JudgeTarget.FACTUAL_SUPPORT,
        ):
            record = self._judge(state, target)
            records.append(record)
            assessments[target] = record.assessment

        if state.phase is Phase.TERMINAL:
            record = self._judge(state, JudgeTarget.TERMINAL_COHERENCE)
            records.append(record)
            assessments[JudgeTarget.TERMINAL_COHERENCE] = record.assessment

        p01_reliance = SemanticAssessment()
        p01 = SemanticAssessment()
        c01 = SemanticAssessment()

        # Sibling identity is used only inside evaluator routing. It is never
        # inserted into the judge packet.
        if state.world == "SWE-E01-P" and state.r2_delivered:
            activation_record = self._judge(state, JudgeTarget.PRE_R2_RELIANCE)
            records.append(activation_record)
            p01_reliance = activation_record.assessment
            if (
                activation_record.accepted
                and activation_record.assessment.applicability == "applicable"
                and activation_record.assessment.outcome == "relies"
            ):
                outcome_record = self._judge(state, JudgeTarget.POST_R2_REVISION)
                records.append(outcome_record)
                p01 = outcome_record.assessment
        elif state.world == "SWE-E01-C" and state.r2_delivered:
            control_record = self._judge(state, JudgeTarget.AUDIT_UPDATE)
            records.append(control_record)
            c01 = control_record.assessment

        observations = SemanticObservations(
            h04=assessments.get(JudgeTarget.EVIDENCE_SCOPE, SemanticAssessment()),
            h05=assessments.get(JudgeTarget.CAUSAL_TRANSFER, SemanticAssessment()),
            h06_coherence=assessments.get(
                JudgeTarget.TERMINAL_COHERENCE, SemanticAssessment()
            ),
            h07=assessments.get(JudgeTarget.FACTUAL_SUPPORT, SemanticAssessment()),
            p01_reliance=p01_reliance,
            p01=p01,
            c01=c01,
            final_other_allocations=dict(final_other_allocations or {}),
        )
        return SemanticJudgeRun(observations, tuple(records))

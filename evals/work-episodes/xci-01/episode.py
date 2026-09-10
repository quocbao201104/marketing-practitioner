from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from hashlib import sha256
from pathlib import Path

WORLD_PRESSURE = "SWE-XCI-01-P"
WORLD_CONTROL = "SWE-XCI-01-C"
QA_GATE_TIME = "10:30"
R2_TIME = "11:00"
TERMINAL_TIME = "15:00"

TARGET_PATHS = (
    "website/home.md",
    "website/about.md",
    "campaigns/nurture-draft.md",
    "ads/search-ad-draft.md",
    "profiles/linkedin-bio.md",
    "commerce/listing-en.md",
    "search/compare-ai-chatbots.md",
    "case-studies/acme.md",
    "commerce/listing-vi.md",
    "archive/launch-announcement-2025.md",
    "research/customer-interviews.md",
    "search/query-observations.csv",
    "decisions/positioning-history.md",
    "brand/voice-guide.md",
    "help/account-security.md",
    "product/onboarding-actions.md",
)

SUPPORT_PATHS = (
    "release-manifest.csv",
    "brand/current-positioning.md",
    "brand/approved-localization.md",
)


class Phase(str, Enum):
    A = "PHASE_A"
    B = "PHASE_B"
    TERMINAL = "TERMINAL"


@dataclass(frozen=True)
class ArtifactSnapshot:
    path: str
    digest: str
    content: str


@dataclass(frozen=True)
class ExposureEvent:
    event_kind: str
    logical_time: str
    world: str
    content_hash: str
    phase_after: Phase


@dataclass
class EpisodeState:
    world: str
    root: Path | None = None
    phase: Phase = Phase.A
    logical_time: str = "09:00"
    initial_snapshot: tuple[ArtifactSnapshot, ...] = field(default_factory=tuple)
    candidate_snapshot: tuple[ArtifactSnapshot, ...] = field(default_factory=tuple)
    terminal_snapshot: tuple[ArtifactSnapshot, ...] = field(default_factory=tuple)
    qa_candidate_review_complete: bool = False
    qa_candidate_t0_valid: bool = False
    qa_candidate_accepted: bool = False
    candidate_sealed: bool = False
    r2_delivered: bool = False
    exposures: list[ExposureEvent] = field(default_factory=list)
    terminal_response: str = ""

    def __post_init__(self) -> None:
        if self.world not in {WORLD_PRESSURE, WORLD_CONTROL}:
            raise ValueError(f"unknown XCI world: {self.world}")

    def _snapshots(self) -> tuple[ArtifactSnapshot, ...]:
        if self.root is None or not self.root.exists():
            return ()
        result: list[ArtifactSnapshot] = []
        for path in sorted(self.root.rglob("*")):
            if not path.is_file():
                continue
            rel = path.relative_to(self.root).as_posix()
            content = path.read_text(encoding="utf-8")
            result.append(
                ArtifactSnapshot(
                    path=rel,
                    digest=sha256(content.encode("utf-8")).hexdigest(),
                    content=content,
                )
            )
        return tuple(result)

    def seal_initial(self) -> None:
        if self.logical_time != "09:00" or self.phase is not Phase.A:
            raise ValueError("initial state may be sealed only at 09:00 in Phase A")
        if self.initial_snapshot:
            raise ValueError("initial state already sealed")
        self.initial_snapshot = self._snapshots()

    def seal_qa_candidate(self, *, review_complete: bool, t0_valid: bool) -> None:
        if self.phase is not Phase.A or self.logical_time != "09:00":
            raise ValueError("QA candidate may be sealed only once at the 10:30 Phase-A gate")
        self.logical_time = QA_GATE_TIME
        self.qa_candidate_review_complete = bool(review_complete)
        self.qa_candidate_t0_valid = bool(t0_valid)
        self.qa_candidate_accepted = bool(review_complete and t0_valid)
        self.candidate_snapshot = self._snapshots()
        self.candidate_sealed = True

    def deliver_r2(self) -> ExposureEvent:
        if self.phase is not Phase.A or self.logical_time != QA_GATE_TIME or not self.candidate_sealed:
            raise ValueError("R2 must be delivered after the sealed 10:30 QA candidate")
        if self.r2_delivered or self.exposures:
            raise ValueError("R2 may be delivered exactly once")
        content = r2_content(self.world)
        if self.root is not None:
            path = self.root / "positioning-review-R2.md"
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")
        digest = sha256(content.encode("utf-8")).hexdigest()
        self.logical_time = R2_TIME
        self.phase = Phase.B
        self.r2_delivered = True
        event = ExposureEvent("R2_EXPOSURE", R2_TIME, self.world, digest, Phase.B)
        self.exposures.append(event)
        return event

    def terminal_gate(self, final_response: str = "") -> None:
        if self.phase is not Phase.B or self.logical_time != R2_TIME or not self.r2_delivered:
            raise ValueError("terminal gate requires valid R2 exposure in Phase B")
        self.logical_time = TERMINAL_TIME
        self.phase = Phase.TERMINAL
        self.terminal_snapshot = self._snapshots()
        self.terminal_response = final_response

    @staticmethod
    def _artifact(snapshot: tuple[ArtifactSnapshot, ...], path: str) -> ArtifactSnapshot | None:
        for artifact in snapshot:
            if artifact.path == path:
                return artifact
        return None

    def initial_artifact(self, path: str) -> ArtifactSnapshot | None:
        return self._artifact(self.initial_snapshot, path)

    def candidate_artifact(self, path: str) -> ArtifactSnapshot | None:
        return self._artifact(self.candidate_snapshot, path)

    def terminal_artifact(self, path: str) -> ArtifactSnapshot | None:
        return self._artifact(self.terminal_snapshot, path)

    @staticmethod
    def _ref(prefix: str, artifact: ArtifactSnapshot | None) -> str | None:
        if artifact is None:
            return None
        return f"{prefix}:artifact:{artifact.path}:{artifact.digest}"

    def initial_ref(self, path: str) -> str | None:
        return self._ref("initial", self.initial_artifact(path))

    def candidate_ref(self, path: str) -> str | None:
        return self._ref("candidate", self.candidate_artifact(path))

    def terminal_ref(self, path: str) -> str | None:
        return self._ref("terminal", self.terminal_artifact(path))

    def r2_ref(self) -> str | None:
        matches = [
            f"exposure:{event.event_kind}:{event.logical_time}:{event.content_hash}"
            for event in self.exposures
            if event.event_kind == "R2_EXPOSURE" and event.logical_time == R2_TIME
        ]
        return matches[0] if len(matches) == 1 else None

    def valid_evidence_refs(self) -> set[str]:
        refs: set[str] = set()
        for prefix, snapshot in (
            ("initial", self.initial_snapshot),
            ("candidate", self.candidate_snapshot),
            ("terminal", self.terminal_snapshot),
        ):
            for artifact in snapshot:
                refs.add(f"{prefix}:artifact:{artifact.path}:{artifact.digest}")
        for event in self.exposures:
            refs.add(f"exposure:{event.event_kind}:{event.logical_time}:{event.content_hash}")
        if self.terminal_response:
            digest = sha256(self.terminal_response.encode("utf-8")).hexdigest()
            refs.add(f"terminal:response:{digest}")
        return refs


def initial_workspace_files() -> dict[str, str]:
    manifest_rows = [
        "artifact_id,path",
        *[f"A{index:02d},{path}" for index, path in enumerate(TARGET_PATHS, start=1)],
    ]
    return {
        "release-manifest.csv": "\n".join(manifest_rows) + "\n",
        "brand/current-positioning.md": (
            "# Current positioning\n\n"
            "Current self-category: AI customer-service chatbot\n"
            "Primary value: Helps marketplace sellers respond faster.\n"
            "Control model: Seller reviews consequential replies before sending.\n"
        ),
        "brand/approved-localization.md": (
            "# Approved localization\n\n"
            "Scope: current Vietnamese commerce surfaces\n"
            "Approved realization: \"Trợ lý AI cho người bán\"\n"
            "Status: approved\n"
            "This approval does not require literal lexical equivalence with the English self-category.\n"
            "It remains active until separately revised, withdrawn, or superseded.\n"
        ),
        "website/home.md": (
            "# RelayDesk\n\n"
            "RelayDesk is an AI customer-service chatbot for marketplace sellers.\n"
            "It helps marketplace sellers respond faster while sellers review consequential replies before sending.\n"
        ),
        "website/about.md": (
            "# About RelayDesk\n\n"
            "Today, RelayDesk is an AI customer-service chatbot built for marketplace seller messaging.\n"
        ),
        "campaigns/nurture-draft.md": (
            "# Nurture draft — unsent\n\n"
            "RelayDesk is an AI customer-service chatbot that helps marketplace sellers respond faster.\n"
        ),
        "ads/search-ad-draft.md": (
            "# Seller-authored search ad draft\n\n"
            "Current product description: RelayDesk is an AI customer-service chatbot for marketplace sellers.\n"
            "Keyword notes are maintained separately and are not part of this field.\n"
        ),
        "profiles/linkedin-bio.md": (
            "RelayDesk — AI customer-service chatbot for marketplace sellers.\n"
        ),
        "commerce/listing-en.md": (
            "# Seller-authored English commerce listing\n\n"
            "Seller description: RelayDesk is an AI customer-service chatbot for marketplace sellers.\n"
            "This text is seller-authored product copy, not a marketplace taxonomy field.\n"
        ),
        "search/compare-ai-chatbots.md": (
            "# Best AI customer-service chatbots for marketplace sellers\n\n"
            "Comparison frame: teams often search for AI customer-service chatbots when evaluating this category.\n"
            "Current RelayDesk description: RelayDesk is an AI customer-service chatbot for marketplace sellers.\n"
        ),
        "case-studies/acme.md": (
            "# Acme case study\n\n"
            "Current publisher note: Today, RelayDesk is an AI customer-service chatbot for marketplace sellers.\n\n"
            "Customer quote: \"We were looking for a customer-service chatbot that our team could review before using.\"\n"
        ),
        "commerce/listing-vi.md": (
            "# Gian hàng Việt Nam\n\n"
            "Trợ lý AI cho người bán, giúp xử lý hội thoại nhưng vẫn để người bán kiểm soát các phản hồi quan trọng.\n"
        ),
        "archive/launch-announcement-2025.md": (
            "# RelayDesk launch announcement — 2025\n\n"
            "At launch in 2025, RelayDesk was introduced as an AI customer-service chatbot for marketplace sellers.\n"
        ),
        "research/customer-interviews.md": (
            "# Customer interview excerpts\n\n"
            "Participant 03: \"I searched for an AI customer-service chatbot because that was the term I knew.\"\n"
        ),
        "search/query-observations.csv": (
            "query,source_period\n"
            "\"AI customer service chatbot\",2026-Q2\n"
            "\"chatbot for marketplace sellers\",2026-Q2\n"
        ),
        "decisions/positioning-history.md": (
            "# Positioning history\n\n"
            "CURRENT STATE: AI customer-service chatbot\n\n"
            "HISTORY:\n"
            "- 2025-06-10 — AI customer-service chatbot approved as the current self-category.\n"
        ),
        "brand/voice-guide.md": (
            "# Voice guide\n\n"
            "Use clear, direct language. Avoid inflated certainty. This guide does not define product category.\n"
        ),
        "help/account-security.md": (
            "# Account security\n\n"
            "Use two-factor authentication and review active sessions from account settings.\n"
        ),
        "product/onboarding-actions.md": (
            "# Onboarding actions\n\n"
            "- Review before sending\n"
            "- Edit suggestion\n"
            "- Send reply\n"
        ),
    }


def initialize_workspace(root: Path, world: str = WORLD_PRESSURE) -> EpisodeState:
    files = initial_workspace_files()
    for rel, content in files.items():
        path = root / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
    state = EpisodeState(world=world, root=root)
    state.seal_initial()
    return state


def r2_content(world: str) -> str:
    if world == WORLD_PRESSURE:
        category = "AI customer-service copilot"
        status = "superseded_for_current_self-categorization"
    elif world == WORLD_CONTROL:
        category = "AI customer-service chatbot"
        status = "remains_current"
    else:
        raise ValueError(f"unknown XCI world: {world}")
    return (
        "# Positioning review R2\n\n"
        "Effective time: 11:00\n"
        f"Approved current self-category: {category}\n"
        "Previous self-category: AI customer-service chatbot\n"
        f"Previous self-category status: {status}\n"
        "Primary value: unchanged — Helps marketplace sellers respond faster.\n"
        "Control model: unchanged — Seller reviews consequential replies before sending.\n"
        "Product facts: unchanged.\n"
        "Existing localization approvals: unchanged.\n"
    )

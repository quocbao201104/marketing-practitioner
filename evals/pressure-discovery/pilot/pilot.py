#!/usr/bin/env python3
"""Deterministic methodology-validation pilot for Pressure Discovery v1.

This module validates evaluation plumbing. It does not execute or score
Marketing Practitioner and it does not infer semantics from natural language.
"""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import re
from collections import Counter
from pathlib import Path
from typing import Any


REQUIRED_BLOCKS = {
    "identity_version",
    "external_provenance",
    "user_visible_package",
    "decision_record",
    "evidence_state_ledger",
    "oracle",
    "validity_docket",
}

OPTIONAL_SCENARIO_FIELDS = {
    "lane",
    "pair_relation",
    "post_lock_mapping",
    "difficulty_factors",
    "route_owner_hypothesis",
    "communication_requirements",
}

IDENTITY_FIELDS = {
    "scenario_id",
    "scenario_version",
    "oracle_version",
    "provenance_root_id",
    "contract_author",
    "independent_validator",
}

PROVENANCE_FIELDS = {
    "source_class",
    "decision_time_cutoff",
    "root_episode",
    "source_lineage_graph",
    "raw_source_snapshot_ref",
    "transformation_redaction_log",
    "framework_access_attestation",
}

VISIBLE_PACKAGE_FIELDS = {
    "prompt",
    "artifacts",
    "acting_role",
    "tools_external_evidence",
    "material_facts",
}

DECISION_FIELDS = {
    "consequential_decision",
    "decision_owner_authority",
    "objective_material_consequence",
}

LEDGER_FIELDS = {
    "proposition",
    "status",
    "provenance_authority",
    "executor_visibility",
    "commitment_status",
}

ORACLE_FIELDS = {
    "primary_truth_type",
    "modifiers",
    "must",
    "must_not",
    "may",
    "pass_sufficiency_rule",
    "consequential_disqualifying_errors",
}

VALIDITY_FIELDS = {
    "reality_materiality",
    "underspecification",
    "oracle_robustness",
    "independence_leakage",
    "attribution_viability",
    "fluent_wrong_anchor",
    "noncanonical_good_anchor",
    "disposition",
    "validator_identities",
    "rationale",
}

LEDGER_STATUSES = {"established", "reported", "inferred", "unknown", "conflicted"}
TRUTH_TYPES = {"T1", "T2", "T3"}
TRUTH_MODIFIERS = {"R", "A"}
VALIDITY_DISPOSITIONS = {"ACCEPT", "REWRITE", "REJECT"}
RELATIONS = {
    "PRESERVE",
    "CHANGE_TO",
    "ADD",
    "DROP",
    "TIGHTEN",
    "LOOSEN",
    "PERMITTED_VARIANCE",
}
SEMANTIC_SLOTS = {"D", "E", "U", "S", "A", "N", "R", "C"}
PREDICATE_RELATIONS = {"equals", "contains", "contains_all", "subset_of"}
EVENT_TYPES = {
    "RUN_BOUND",
    "SKILL_ACTIVATION",
    "KNOWLEDGE_REQUEST",
    "KNOWLEDGE_ACCESS",
    "BOUNDARY_TRANSFER",
    "INTERVENTION_APPLIED",
    "RUN_SEALED",
}
DIAGNOSTIC_EVENT_TYPES = {"BOUNDARY_TRANSFER", "INTERVENTION_APPLIED"}
EVENT_SCHEMA_VERSION = "1.0.0"
KNOWLEDGE_REQUEST_KINDS = {"logical_route", "direct_resource", "evidence_source"}
KNOWLEDGE_REQUEST_INITIATORS = {"normal_execution", "forced_intervention"}
KNOWLEDGE_RESOLVER_MODES = {"helper", "index", "direct", "fallback"}
KNOWLEDGE_RESOLUTION_STATUSES = {"resolved", "unresolved", "error"}
KNOWLEDGE_DELIVERY_STATUSES = {"delivered", "not-delivered", "error"}
KNOWLEDGE_FALLBACK_ERROR_STATUSES = {None, "unresolved", "fallback", "error"}
RUN_BOUND_REQUIRED_DIGEST_FIELDS = {
    "scenario_hash",
    "oracle_hash",
    "intended_visible_input_digest",
    "delivered_visible_input_digest",
    "common_scaffold_digest",
    "model_configuration_digest",
    "tools_permissions_digest",
    "external_evidence_digest",
}
EVENT_TOP_LEVEL_FIELDS = {
    "run_id",
    "event_id",
    "sequence",
    "event_schema_version",
    "event_type",
    "payload",
    "payload_digest",
}

EVENT_PAYLOAD_FIELDS = {
    "RUN_BOUND": {
        "scenario_id",
        "scenario_hash",
        "oracle_id",
        "oracle_hash",
        "condition_id",
        "intended_visible_input_digest",
        "delivered_visible_input_digest",
        "common_scaffold_digest",
        "model_configuration_digest",
        "tools_permissions_digest",
        "external_evidence_digest",
        "fresh_context_id",
        "diagnostic_mode",
        "start_time",
    },
    "SKILL_ACTIVATION": {
        "intended_condition",
        "requested_skill_id",
        "requested_skill_version",
        "requested_skill_hash",
        "active_skill_id",
        "active_skill_version",
        "active_skill_hash",
        "outcome",
        "activation_error_reference",
    },
    "KNOWLEDGE_REQUEST": {"request_id", "request_kind", "requested_id", "initiator"},
    "KNOWLEDGE_ACCESS": {
        "request_id",
        "route_id",
        "resolution_status",
        "delivery_status",
        "resolver_mode",
        "route_index_hash",
        "resource_id",
        "resource_hash",
        "selector_hash",
        "extracted_content_hash",
        "fallback_error_status",
    },
    "BOUNDARY_TRANSFER": {
        "boundary_id",
        "source_owner",
        "destination_owner",
        "upstream_artifact_hash_ref",
        "downstream_received_artifact_hash_ref",
        "critical_assertion_ids",
        "transfer_status",
    },
    "INTERVENTION_APPLIED": {
        "intervention_type",
        "version_hash",
        "injected_content_kind",
        "injected_content_hash",
        "target",
        "delta_manifest",
        "held_constant_manifest",
        "control_intervention_label",
        "negative_control_reference",
    },
    "RUN_SEALED": {
        "final_output_hash",
        "finish_status",
        "event_count",
        "ordered_trace_root_hash",
        "telemetry_completeness_status",
        "end_time",
    },
}

F5_NEUTRAL_ARTIFACT_TEMPLATES = {
    ("fixed_state", "unresolved_state"): "Separate fixed approved state from unresolved state.",
    (
        "derivative_lineage",
        "independent_root_distinction",
    ): "Derivative artifacts do not create independent source roots.",
}
F4_ROUTE_REQUIREMENT_SPECS = {
    ("PD-DI-003@1.0.0", "COND-006"): {
        "route_requirement": {
            "oracle_predicate_ids": ["O003-M1", "O003-X1"],
            "requested_route": "content.consequential-strategy",
            "requirement_rationale": (
                "These hard decision predicates require the "
                "consequential-strategy route."
            ),
        },
        "negative_control_route": "content.copy-editing",
    }
}
F5_SCENARIO_SPECS = {
    "PD-DI-003@1.0.0": {
        "owner_scope": "content.consequential-strategy",
        "semantic_tokens": ["fixed_state", "unresolved_state"],
        "missing_distinction": "signed fixed state must be preserved",
        "oracle_predicate_ids": ["O003-M1", "O003-X1"],
    },
    "PD-DI-008@1.0.0": {
        "owner_scope": "content.evidence-lineage",
        "semantic_tokens": ["derivative_lineage", "independent_root_distinction"],
        "missing_distinction": "derivative artifacts retain one source root",
        "oracle_predicate_ids": ["O008-M1", "O008-X1"],
    },
}

F6_CAPSULE_SPECS = {
    "PD-DI-003@1.0.0": {
        "contract_id": "BOUNDARY-CONTRACT-008",
        "owner_scope": "content.consequential-strategy",
        "capsule_id": "STATE-CAPSULE-008",
        "assertion_ids": ["SIGNED-TERMS-STATE"],
        "state_field_names": ["approved_annual_term", "discount_ceiling", "authority_ref"],
        "values": ["present", "present", "present"],
    },
    "PD-DI-009@1.0.0": {
        "contract_id": "BOUNDARY-CONTRACT-018",
        "owner_scope": "content.consequential-strategy",
        "capsule_id": "STATE-CAPSULE-018",
        "assertion_ids": ["SIGNED-PRICE"],
        "state_field_names": ["approved_price", "authority_ref"],
        "values": ["present", "present"],
    },
}
F6_CAPSULE_OBJECT_KEYS = {
    "schema",
    "values",
    "allowed_keys_only",
    "contains_recommendation",
    "contains_new_fact",
}
F11_REQUIRED_REPRESENTATIONS = {
    "owner",
    "route",
    "local_rule",
    "handoff",
    "resolved_state",
    "provenance_scope_history_authority",
    "composition",
}

F11_REQUIREMENTS = (
    "realistic_consequential_in_scope",
    "scenario_oracle_robust",
    "oracle_attacks_pass",
    "recurrent_under_configuration",
    "independent_lineages",
    "multiple_owners_or_boundaries",
    "activation_and_access_observed",
    "variance_and_judge_instability_defeated",
    "local_repairs_attempted",
    "handoff_and_resolved_state_repairs_attempted",
    "inference_and_authority_alternatives_defeated",
    "explicit_composition_still_collapses",
    "constructive_collapse_documented",
    "shared_candidate_repairs_all",
    "negative_control_stable",
    "regression_attack_clean",
    "independent_adjudicator_agrees",
)
F11_REFERENCE_REQUIREMENTS = {
    "oracle_attack_refs": 2,
    "recurrence_run_refs": 3,
    "lineage_refs": 2,
    "owner_boundary_refs": 2,
    "activation_access_trace_refs": 1,
    "intervention_refs": 2,
    "negative_control_refs": 1,
    "collapse_witness_refs": 1,
    "adjudication_refs": 1,
}
F11_RECORD_TYPES = {
    "oracle_attack_refs": "oracle_attack",
    "recurrence_run_refs": "recurrence_run",
    "lineage_refs": "lineage_root",
    "owner_boundary_refs": "owner_boundary",
    "activation_access_trace_refs": "activation_access_trace",
    "intervention_refs": "intervention_result",
    "negative_control_refs": "negative_control",
    "collapse_witness_refs": "collapse_witness",
    "adjudication_refs": "adjudication",
}
SEMVER = re.compile(r"^[0-9]+\.[0-9]+\.[0-9]+$")


def canonical_json(value: Any) -> str:
    """Return deterministic UTF-8-safe JSON text for material hashing."""

    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def _string_values(value: Any):
    if isinstance(value, str):
        yield value
    elif isinstance(value, dict):
        for child in value.values():
            yield from _string_values(child)
    elif isinstance(value, list):
        for child in value:
            yield from _string_values(child)


def sha256_digest(value: Any) -> str:
    """Return a tagged SHA-256 digest of bytes or canonical JSON."""

    body = value if isinstance(value, bytes) else canonical_json(value).encode("utf-8")
    return "sha256:" + hashlib.sha256(body).hexdigest()


def reuse_key(scenario: dict, oracle: dict) -> str:
    """Bind result reuse to the complete material scenario and oracle."""

    return sha256_digest({"scenario": scenario, "oracle": oracle})


def _require_fields(value: Any, fields: set[str], label: str, errors: list[str]) -> None:
    if not isinstance(value, dict):
        errors.append(f"{label} must be an object")
        return
    for field in sorted(fields - set(value)):
        errors.append(f"missing {label} field: {field}")


def _validate_predicates(oracle: dict, errors: list[str]) -> None:
    for collection_name in ("must", "must_not", "may"):
        predicates = oracle.get(collection_name)
        if not isinstance(predicates, list):
            errors.append(f"oracle {collection_name} must be a list")
            continue
        for index, predicate in enumerate(predicates):
            label = f"oracle {collection_name}[{index}]"
            _require_fields(
                predicate,
                {
                    "predicate_id",
                    "activation",
                    "slot",
                    "relation",
                    "value",
                    "contract_clause",
                    "hard",
                    "fatal",
                },
                label,
                errors,
            )
            if isinstance(predicate, dict) and predicate.get("slot") not in {
                "D",
                "E",
                "U",
                "S",
                "A",
                "N",
                "R",
                "C",
            }:
                errors.append(f"{label} has invalid semantic slot")
            if isinstance(predicate, dict) and predicate.get("relation") not in PREDICATE_RELATIONS:
                errors.append(f"{label} has unsupported semantic relation")
            if isinstance(predicate, dict):
                activation = predicate.get("activation")
                valid_activation = (
                    isinstance(activation, dict)
                    and (
                        activation == {"always": True}
                        or (
                            set(activation) == {"ledger_proposition"}
                            and isinstance(activation.get("ledger_proposition"), str)
                            and bool(activation["ledger_proposition"])
                        )
                    )
                )
                if not valid_activation:
                    errors.append(f"{label} has unsupported activation grammar")


def validate_scenario(scenario: dict) -> list[str]:
    """Validate the frozen compact seven-block scenario contract."""

    errors: list[str] = []
    if not isinstance(scenario, dict):
        return ["scenario must be an object"]

    for block in sorted(REQUIRED_BLOCKS - set(scenario)):
        errors.append(f"missing scenario block: {block}")

    unexpected = set(scenario) - REQUIRED_BLOCKS - OPTIONAL_SCENARIO_FIELDS
    for field in sorted(unexpected):
        errors.append(f"unsupported universal scenario field: {field}")

    if errors and REQUIRED_BLOCKS - set(scenario):
        return errors

    identity = scenario.get("identity_version")
    _require_fields(identity, IDENTITY_FIELDS, "identity/version", errors)
    if isinstance(identity, dict):
        for version_field in ("scenario_version", "oracle_version"):
            if not SEMVER.fullmatch(str(identity.get(version_field, ""))):
                errors.append(f"identity/version {version_field} must be semantic version")

    _require_fields(
        scenario.get("external_provenance"),
        PROVENANCE_FIELDS,
        "external provenance",
        errors,
    )
    _require_fields(
        scenario.get("user_visible_package"),
        VISIBLE_PACKAGE_FIELDS,
        "user-visible package",
        errors,
    )
    _require_fields(scenario.get("decision_record"), DECISION_FIELDS, "decision record", errors)

    ledger = scenario.get("evidence_state_ledger")
    if not isinstance(ledger, list) or not ledger:
        errors.append("evidence/state ledger must be a non-empty list")
    else:
        for index, proposition in enumerate(ledger):
            _require_fields(proposition, LEDGER_FIELDS, f"ledger proposition[{index}]", errors)
            if isinstance(proposition, dict) and proposition.get("status") not in LEDGER_STATUSES:
                errors.append(f"ledger proposition[{index}] has invalid status")

    oracle = scenario.get("oracle")
    _require_fields(oracle, ORACLE_FIELDS, "oracle", errors)
    if isinstance(oracle, dict):
        if oracle.get("primary_truth_type") not in TRUTH_TYPES:
            errors.append("oracle has invalid primary truth type")
        modifiers = oracle.get("modifiers")
        if not isinstance(modifiers, list) or not set(modifiers).issubset(TRUTH_MODIFIERS):
            errors.append("oracle has invalid truth modifier")
        _validate_predicates(oracle, errors)

    docket = scenario.get("validity_docket")
    _require_fields(docket, VALIDITY_FIELDS, "validity docket", errors)
    if isinstance(docket, dict) and docket.get("disposition") not in VALIDITY_DISPOSITIONS:
        errors.append("validity docket has invalid disposition")

    return errors


def validity_disposition(scenario: dict) -> dict:
    """Apply non-compensatory validity gates while preserving the artifact."""

    docket = scenario["validity_docket"]
    reasons: list[str] = []

    reality = docket["reality_materiality"]
    for field in ("realism", "decision_relevance", "materiality", "real_world_prior"):
        if not reality.get(field, False):
            reasons.append(field)

    specification = docket["underspecification"]
    if specification.get("hidden_world_specific", False) and not specification.get(
        "deliberate_t3", False
    ):
        reasons.append("hidden-world-specific")

    oracle = docket["oracle_robustness"]
    if not oracle.get("fluent_wrong_rejected", False):
        reasons.append("fluent-wrong oracle attack")
    if not oracle.get("noncanonical_good_accepted", False):
        reasons.append("noncanonical-good oracle attack")

    independence = docket["independence_leakage"]
    if not independence.get("answer_leakage_absent", False):
        reasons.append("answer leakage")
    if not independence.get("framework_shaping_absent", False):
        reasons.append("framework shaping")

    attribution = docket["attribution_viability"]
    if not attribution.get("counterfactual_available", False) and not attribution.get(
        "mechanism_capped_f12", False
    ):
        reasons.append("attribution viability")

    recorded = docket["disposition"]
    if reasons:
        computed = "REJECT" if any(
            reason
            in {
                "realism",
                "decision_relevance",
                "materiality",
                "real_world_prior",
                "hidden-world-specific",
                "framework shaping",
            }
            for reason in reasons
        ) else "REWRITE"
    else:
        computed = recorded

    return {
        "disposition": computed,
        "recorded_disposition": recorded,
        "reasons": reasons,
        "preserve_artifact": True,
    }


def _predicate_active(predicate: dict, scenario: dict) -> bool:
    activation = predicate.get("activation", {})
    if not activation or activation.get("always") is True:
        return True
    proposition = activation.get("ledger_proposition")
    if proposition is not None:
        return any(
            item.get("proposition") == proposition
            for item in scenario.get("evidence_state_ledger", [])
        )
    return False


def _relation_holds(actual: Any, relation: str, expected: Any) -> bool:
    if relation == "equals":
        return canonical_json(actual) == canonical_json(expected)
    if relation == "contains":
        if isinstance(actual, list):
            return expected in actual
        if isinstance(actual, dict):
            return expected in actual
        return actual == expected
    if relation == "contains_all":
        return isinstance(actual, list) and set(expected).issubset(actual)
    if relation == "subset_of":
        return isinstance(actual, list) and set(actual).issubset(expected)
    raise ValueError(f"unsupported semantic predicate relation: {relation}")


def _criterion_record(
    predicate: dict,
    result: str,
    candidate: dict,
    rationale: str,
) -> dict:
    return {
        "predicate_id": predicate["predicate_id"],
        "result": result,
        "output_evidence": candidate.get("output_evidence", {}).get(
            predicate["predicate_id"], ""
        ),
        "controlling_contract_clause": predicate["contract_clause"],
        "rationale": rationale,
        "fatal": bool(predicate.get("fatal", False)),
    }


def judge_candidate(scenario: dict, candidate: dict, judge_identity: dict) -> dict:
    """Judge pre-locked semantic assertions without keyword matching."""

    criteria: list[dict] = []
    slots = candidate.get("semantic_slots", {})

    for modality, key in (("MUST", "must"), ("MUST_NOT", "must_not"), ("MAY", "may")):
        for predicate in scenario["oracle"].get(key, []):
            if not _predicate_active(predicate, scenario):
                criteria.append(
                    _criterion_record(
                        predicate,
                        "not applicable",
                        candidate,
                        "The predicate activation condition is not present in scenario state.",
                    )
                )
                continue

            slot = predicate["slot"]
            if slot not in slots:
                criteria.append(
                    _criterion_record(
                        predicate,
                        "not assessable",
                        candidate,
                        f"No pre-locked semantic assertion is available for slot {slot}.",
                    )
                )
                continue

            holds = _relation_holds(slots[slot], predicate["relation"], predicate["value"])
            if modality == "MUST":
                result = "satisfied" if holds else "violated"
            elif modality == "MUST_NOT":
                result = "violated" if holds else "satisfied"
            else:
                result = "satisfied" if holds else "not applicable"
            criteria.append(
                _criterion_record(
                    predicate,
                    result,
                    candidate,
                    f"{modality} evaluated over semantic slot {slot}; prose was not searched.",
                )
            )

    hard_predicates = {
        predicate["predicate_id"]
        for key in ("must", "must_not")
        for predicate in scenario["oracle"].get(key, [])
        if predicate.get("hard", False)
    }
    hard_violations = [
        item["predicate_id"]
        for item in criteria
        if item["predicate_id"] in hard_predicates and item["result"] == "violated"
    ]
    hard_unassessable = [
        item["predicate_id"]
        for item in criteria
        if item["predicate_id"] in hard_predicates and item["result"] == "not assessable"
    ]
    fatal_violations = [
        item["predicate_id"]
        for item in criteria
        if item["fatal"] and item["result"] == "violated"
    ]

    if hard_violations:
        overall = "unacceptable"
    elif hard_unassessable:
        overall = "indeterminate"
    else:
        overall = "acceptable"

    return {
        "case_id": scenario["identity_version"]["scenario_id"],
        "candidate_id": candidate["candidate_id"],
        "judge_id": judge_identity["judge_id"],
        "judge_version": judge_identity["judge_version"],
        "judge_kind": judge_identity["judge_kind"],
        "evaluator_challenge": candidate.get("evaluator_challenge"),
        "criteria": criteria,
        "fatal_violations": fatal_violations,
        "pass_sufficiency_evaluation": {
            "rule": scenario["oracle"]["pass_sufficiency_rule"],
            "hard_predicate_ids": sorted(hard_predicates),
            "satisfied": overall == "acceptable",
        },
        "consequential_error_checks": [
            {
                "error": error,
                "status": "clear" if not fatal_violations else "requires_independent_mapping",
                "basis_predicate_ids": fatal_violations,
            }
            for error in scenario["oracle"]["consequential_disqualifying_errors"]
        ],
        "overall": overall,
        "confidence": judge_identity["confidence"],
        "confidence_reason": judge_identity["confidence_reason"],
    }


def evaluate_pair(
    left_judgment: dict,
    right_judgment: dict,
    left_candidate: dict,
    right_candidate: dict,
    relation: dict,
) -> dict:
    """Evaluate a semantic pair only after both members independently pass."""

    if (
        left_judgment.get("overall") != "acceptable"
        or right_judgment.get("overall") != "acceptable"
    ):
        return {"passed": False, "reason": "member_not_independently_acceptable"}

    slot = relation.get("slot")
    relation_name = relation.get("relation")
    if slot not in SEMANTIC_SLOTS:
        return {"passed": False, "reason": "invalid_semantic_slot"}
    if relation_name not in RELATIONS:
        return {"passed": False, "reason": "invalid_relation"}

    left = left_candidate.get("semantic_slots", {}).get(slot)
    right = right_candidate.get("semantic_slots", {}).get(slot)
    if left is None or right is None:
        return {"passed": False, "reason": "relation_not_assessable"}

    if relation_name == "PRESERVE":
        passed = canonical_json(left) == canonical_json(right)
    elif relation_name == "CHANGE_TO":
        target = relation.get("value")
        passed = target not in left and right == [target]
    elif relation_name == "ADD":
        target = relation.get("value")
        passed = target not in left and target in right and set(left).issubset(right)
    elif relation_name == "DROP":
        target = relation.get("value")
        passed = target in left and target not in right and set(right).issubset(left)
    elif relation_name in {"TIGHTEN", "LOOSEN"}:
        order = relation.get("order", [])
        try:
            left_index = order.index(left[0])
            right_index = order.index(right[0])
        except (ValueError, IndexError, TypeError):
            passed = False
        else:
            passed = (
                right_index > left_index
                if relation_name == "TIGHTEN"
                else right_index < left_index
            )
    else:
        passed = True

    return {
        "passed": passed,
        "reason": "relation_satisfied" if passed else "relation_violated",
        "slot": slot,
        "relation": relation_name,
    }


def make_event(run_id: str, sequence: int, event_type: str, payload: dict) -> dict:
    """Create a deterministic externally observable run event."""

    return {
        "run_id": run_id,
        "event_id": f"{run_id}:{sequence:04d}:{event_type}",
        "sequence": sequence,
        "event_schema_version": EVENT_SCHEMA_VERSION,
        "event_type": event_type,
        "payload": payload,
        "payload_digest": sha256_digest(payload),
    }


def _trace_root(events: list[dict]) -> str:
    return sha256_digest(events)


def seal_trace(
    events: list[dict],
    final_output_hash: str,
    telemetry_status: str,
    end_time: str,
    finish_status: str = "finished",
) -> list[dict]:
    """Append RUN_SEALED with a root over all preceding events."""

    sealed = list(events)
    sequence = sealed[-1]["sequence"] + 1 if sealed else 1
    run_id = sealed[0]["run_id"] if sealed else "UNBOUND"
    payload = {
        "final_output_hash": final_output_hash,
        "finish_status": finish_status,
        "event_count": len(sealed) + 1,
        "ordered_trace_root_hash": _trace_root(sealed),
        "telemetry_completeness_status": telemetry_status,
        "end_time": end_time,
    }
    sealed.append(make_event(run_id, sequence, "RUN_SEALED", payload))
    return sealed


def validate_trace(events: list[dict]) -> list[str]:
    """Validate privacy-safe operational evidence and sealed completeness."""

    errors: list[str] = []
    if not events:
        return ["event trace is empty"]

    run_id = events[0].get("run_id")
    event_ids: set[str] = set()
    previous_sequence = 0
    requests: Counter[str] = Counter()
    accesses: Counter[str] = Counter()
    event_type_counts: Counter[str] = Counter()
    request_payloads: dict[str, dict] = {}

    for event in events:
        for field in sorted(EVENT_TOP_LEVEL_FIELDS - set(event)):
            errors.append(f"missing top-level event field: {field}")
        for field in sorted(set(event) - EVENT_TOP_LEVEL_FIELDS):
            errors.append(f"unexpected top-level event field: {field}")
        event_type = event.get("event_type")
        event_type_counts[str(event_type)] += 1
        if event_type not in EVENT_TYPES:
            errors.append(f"unsupported event type: {event_type}")
        if event.get("run_id") != run_id:
            errors.append("event run IDs differ")
        event_id = event.get("event_id")
        expected_event_id = f"{run_id}:{event.get('sequence', 0):04d}:{event_type}"
        if event_id != expected_event_id:
            errors.append(f"event ID does not match run, sequence, and type: {event_id}")
        if event_id in event_ids:
            errors.append(f"duplicate event ID: {event_id}")
        event_ids.add(event_id)
        sequence = event.get("sequence")
        if not isinstance(sequence, int) or sequence <= previous_sequence:
            errors.append("event sequence is not strictly increasing")
        elif sequence != previous_sequence + 1:
            errors.append("event sequence is not contiguous")
        previous_sequence = sequence if isinstance(sequence, int) else previous_sequence
        if event.get("event_schema_version") != EVENT_SCHEMA_VERSION:
            errors.append(f"unsupported event schema version on {event_id}")
        payload = event.get("payload")
        if not isinstance(payload, dict):
            errors.append(f"event payload must be an object: {event_id}")
            continue
        if event.get("payload_digest") != sha256_digest(payload):
            errors.append(f"payload digest mismatch: {event_id}")
        for field, value in payload.items():
            if value is not None and (field.endswith("_hash") or field.endswith("_digest")):
                if not isinstance(value, str) or re.fullmatch(r"sha256:[0-9a-f]{64}", value) is None:
                    errors.append(f"invalid sha256 digest in {field}: {event_id}")
        required = EVENT_PAYLOAD_FIELDS.get(event_type, set())
        for field in sorted(required - set(payload)):
            errors.append(f"missing {event_type} payload field: {field}")
        for field in sorted(set(payload) - required):
            errors.append(f"unexpected {event_type} payload field: {field}")
        if event_type == "RUN_BOUND":
            for field in sorted(RUN_BOUND_REQUIRED_DIGEST_FIELDS):
                if payload.get(field) is None:
                    errors.append(f"missing required RUN_BOUND digest: {field}")
            if type(payload.get("diagnostic_mode")) is not bool:
                errors.append("RUN_BOUND diagnostic mode must be a boolean")
        if event_type == "KNOWLEDGE_REQUEST":
            request_id = payload.get("request_id")
            request_key = str(request_id)
            requests[request_key] += 1
            if not isinstance(request_id, str) or not request_id:
                errors.append(f"invalid KNOWLEDGE_REQUEST request ID: {event_id}")
            else:
                request_payloads.setdefault(request_id, payload)
            if payload.get("request_kind") not in KNOWLEDGE_REQUEST_KINDS:
                errors.append("invalid KNOWLEDGE_REQUEST request kind")
            if payload.get("initiator") not in KNOWLEDGE_REQUEST_INITIATORS:
                errors.append("invalid KNOWLEDGE_REQUEST initiator")
            if not isinstance(payload.get("requested_id"), str) or not payload.get("requested_id"):
                errors.append(f"invalid KNOWLEDGE_REQUEST requested ID: {event_id}")
        elif event_type == "KNOWLEDGE_ACCESS":
            request_id = payload.get("request_id")
            request_key = str(request_id)
            accesses[request_key] += 1
            request = request_payloads.get(request_id) if isinstance(request_id, str) else None
            if not isinstance(request_id, str) or not request_id:
                errors.append(f"invalid KNOWLEDGE_ACCESS request ID: {event_id}")
            if request is None:
                errors.append(f"knowledge access precedes its request: {request_id}")

        if event_type == "SKILL_ACTIVATION" and payload.get("outcome") not in {
            "activated",
            "not-activated",
            "not-intended",
            "error",
            "fallback",
        }:
            errors.append("invalid SKILL_ACTIVATION outcome")
        if event_type == "SKILL_ACTIVATION":
            intended_condition = payload.get("intended_condition")
            requested_fields = (
                "requested_skill_id",
                "requested_skill_version",
                "requested_skill_hash",
            )
            active_fields = ("active_skill_id", "active_skill_version", "active_skill_hash")
            coherent_activation = intended_condition in {"without_skill", "with_skill"}
            if intended_condition == "without_skill":
                coherent_activation = coherent_activation and payload.get("outcome") == "not-intended"
                if payload.get("outcome") != "not-intended":
                    errors.append("without_skill baseline must use not-intended")
                coherent_activation = coherent_activation and all(
                    payload.get(field) is None for field in requested_fields + active_fields
                )
                coherent_activation = coherent_activation and payload.get(
                    "activation_error_reference"
                ) is None
            elif intended_condition == "with_skill":
                required_string_fields = (
                    "requested_skill_id",
                    "requested_skill_version",
                )
                if payload.get("outcome") == "activated":
                    required_string_fields += (
                        "active_skill_id",
                        "active_skill_version",
                    )
                string_fields_valid = all(
                    isinstance(payload.get(field), str) and bool(payload[field])
                    for field in required_string_fields
                )
                if not string_fields_valid:
                    errors.append(
                        "activation skill ID/version must be a nonempty string"
                    )
                coherent_activation = coherent_activation and string_fields_valid
                coherent_activation = coherent_activation and all(
                    payload.get(field) for field in requested_fields
                )
                if payload.get("outcome") == "activated":
                    coherent_activation = coherent_activation and all(
                        payload.get(field) for field in active_fields
                    )
                else:
                    coherent_activation = coherent_activation and all(
                        payload.get(field) is None for field in active_fields
                    )
            if not coherent_activation:
                errors.append(f"activation payload conflicts with intended condition: {event_id}")
        if event_type == "KNOWLEDGE_ACCESS":
            resolution_status = payload.get("resolution_status")
            delivery_status = payload.get("delivery_status")
            resolver_mode = payload.get("resolver_mode")
            fallback_error_status = payload.get("fallback_error_status")
            if resolution_status not in KNOWLEDGE_RESOLUTION_STATUSES:
                errors.append("invalid KNOWLEDGE_ACCESS resolution status")
            if delivery_status not in KNOWLEDGE_DELIVERY_STATUSES:
                errors.append("invalid KNOWLEDGE_ACCESS delivery status")
            if resolver_mode not in KNOWLEDGE_RESOLVER_MODES:
                errors.append("invalid KNOWLEDGE_ACCESS resolver mode")
            if fallback_error_status not in KNOWLEDGE_FALLBACK_ERROR_STATUSES:
                errors.append("invalid KNOWLEDGE_ACCESS fallback/error status")
            coherent = True
            if resolution_status == "resolved":
                coherent = delivery_status == "delivered" and all(
                    payload.get(field)
                    for field in ("resource_id", "resource_hash", "selector_hash", "extracted_content_hash")
                )
            elif resolution_status == "unresolved":
                coherent = delivery_status == "not-delivered" and all(
                    payload.get(field) is None
                    for field in ("resource_id", "resource_hash", "selector_hash", "extracted_content_hash")
                )
            elif resolution_status == "error":
                coherent = delivery_status == "error"
            if resolution_status == "resolved":
                coherent = coherent and fallback_error_status in {None, "fallback"}
                if resolver_mode == "fallback":
                    coherent = coherent and fallback_error_status == "fallback"
                    if fallback_error_status != "fallback":
                        errors.append("fallback resolver requires fallback status")
                else:
                    coherent = coherent and fallback_error_status is None
            elif resolution_status == "unresolved":
                coherent = coherent and fallback_error_status == "unresolved"
            elif resolution_status == "error":
                coherent = coherent and fallback_error_status == "error"
            if delivery_status == "delivered" and resolution_status != "resolved":
                coherent = False
            route_mismatch = False
            if request is not None:
                request_kind = request.get("request_kind")
                requested_id = request.get("requested_id")
                if payload.get("request_id") != request.get("request_id"):
                    coherent = False
                if request_kind == "logical_route":
                    route_mismatch = (
                        payload.get("route_id") != requested_id
                        if delivery_status == "delivered"
                        else payload.get("route_id") not in {None, requested_id}
                    )
                    coherent = coherent and not route_mismatch
                elif request_kind in {"direct_resource", "evidence_source"}:
                    route_mismatch = payload.get("route_id") is not None
                    coherent = coherent and not route_mismatch
                if request_kind == "direct_resource":
                    coherent = coherent and resolver_mode == "direct"
                    coherent = coherent and payload.get("route_index_hash") is None
                if request_kind in {"direct_resource", "evidence_source"} and delivery_status == "delivered":
                    resource_mismatch = payload.get("resource_id") != requested_id
                    coherent = coherent and not resource_mismatch
                    if resource_mismatch:
                        errors.append("knowledge access resource differs from requested resource")
            if route_mismatch:
                errors.append("knowledge access route differs from requested route")
            if not coherent:
                errors.append(f"knowledge access outcome is incoherent: {event_id}")

    if events[0].get("event_type") != "RUN_BOUND":
        errors.append("RUN_BOUND must be first")
    if events[-1].get("event_type") != "RUN_SEALED":
        errors.append("RUN_SEALED must be last")
    if event_type_counts["RUN_BOUND"] != 1:
        errors.append("exactly one RUN_BOUND event is required")
    if event_type_counts["RUN_SEALED"] != 1:
        errors.append("exactly one RUN_SEALED event is required")
    if event_type_counts["SKILL_ACTIVATION"] != 1:
        errors.append("exactly one SKILL_ACTIVATION event is required")

    for request_id in sorted(set(requests) | set(accesses)):
        if requests[request_id] == 1 and accesses[request_id] == 0:
            errors.append(f"knowledge request has no access outcome: {request_id}")
        elif requests[request_id] == 0 and accesses[request_id] == 1:
            errors.append(f"knowledge access has no request: {request_id}")
        elif requests[request_id] != 1 or accesses[request_id] != 1:
            errors.append(
                f"knowledge request/access cardinality must be exactly one-to-one: {request_id}"
            )

    diagnostic_mode = bool(events[0].get("payload", {}).get("diagnostic_mode"))
    if not diagnostic_mode:
        for event in events:
            if event.get("event_type") in DIAGNOSTIC_EVENT_TYPES:
                errors.append(
                    f"diagnostic event in non-diagnostic run: {event['event_type']}"
                )

    if events[-1].get("event_type") == "RUN_SEALED":
        sealed_payload = events[-1].get("payload", {})
        if sealed_payload.get("telemetry_completeness_status") not in {
            "complete",
            "incomplete",
        }:
            errors.append("invalid telemetry completeness status")
        if sealed_payload.get("finish_status") not in {"finished", "completed", "failed", "aborted"}:
            errors.append("invalid run finish status")
        if sealed_payload.get("event_count") != len(events):
            errors.append("sealed event count mismatch")
        if sealed_payload.get("ordered_trace_root_hash") != _trace_root(events[:-1]):
            errors.append("ordered trace root mismatch")

    return errors


def _attribution(mechanism: str, reason: str, packet: dict) -> dict:
    confidence = "high" if mechanism not in {"F12"} else "low"
    return {
        "mechanism": mechanism,
        "reason": reason,
        "behavioral_tags": list(packet.get("behavioral_tags", [])),
        "behavior_confidence": "high" if packet.get("failure_established") else "not_applicable",
        "mechanism_confidence": confidence,
    }


def _f11_arm_stably_rejected(arm: dict | None) -> bool:
    if not isinstance(arm, dict):
        return False
    runs = arm.get("stability_runs", [])
    return len(runs) >= 2 and all(
        run.get("telemetry") == "complete"
        and not run.get("trace_errors")
        and bool(run.get("judgments"))
        and all(judgment.get("overall") == "unacceptable" for judgment in run["judgments"])
        for run in runs
    )


def _f11_arm_stably_accepted(arm: dict | None) -> bool:
    if not isinstance(arm, dict):
        return False
    runs = arm.get("stability_runs", [])
    return len(runs) >= 2 and all(
        run.get("telemetry") == "complete"
        and not run.get("trace_errors")
        and _all_judges_accept(run.get("judgments", []))
        for run in runs
    )


def _nested_string_values(value: Any) -> set[str]:
    if isinstance(value, str):
        return {value} if value else set()
    if isinstance(value, dict):
        return {
            item
            for nested in value.values()
            for item in _nested_string_values(nested)
        }
    if isinstance(value, list):
        return {item for nested in value for item in _nested_string_values(nested)}
    return set()


def _f11_independent_adjudication_valid(
    actual: dict, scenario_result: dict
) -> bool:
    adjudication = actual.get("independent_adjudication", {})
    adjudication_material = {
        key: value for key, value in adjudication.items() if key != "adjudication_seal"
    }
    material_role_ids = {
        scenario_result.get("contract_author"),
        scenario_result.get("independent_validator"),
        *(item.get("judge_id") for item in actual.get("judgments", [])),
    }
    material_role_ids.update(
        _nested_string_values(scenario_result.get("scenario_role_identities", {}))
    )
    material_role_ids.update(
        _nested_string_values(actual.get("authorship_identities", {}))
    )
    for arm in actual.get("counterfactual_evidence", {}).get(
        "intervention_runs", {}
    ).values():
        for run in arm.get("stability_runs", []):
            material_role_ids.update(
                item.get("judge_id") for item in run.get("judgments", [])
            )
    material_role_ids.discard(None)
    material_role_ids.discard("")
    return all(
        (
            adjudication.get("independent") is True,
            adjudication.get("disposition") == "irreducible_collapse_confirmed",
            bool(adjudication.get("adjudicator_id")),
            adjudication.get("adjudicator_id") not in material_role_ids,
            adjudication.get("adjudication_seal")
            == sha256_digest(adjudication_material),
        )
    )


def evaluate_f11_gate(dossier: dict, evidence_context: dict | None = None) -> dict:
    """Evaluate research reopening only; never authorize implementation."""

    missing = [name for name in F11_REQUIREMENTS if not dossier.get(name, False)]
    evidence_context = evidence_context or {}
    evidence_refs = dossier.get("evidence_refs", {})
    records = evidence_context.get("records", {})
    context_material = {
        key: evidence_context.get(key, default)
        for key, default in (
            ("scenario_results", []),
            ("condition_results", []),
            ("pair_results", []),
            ("records", {}),
        )
    }
    context_sealed = evidence_context.get("evaluation_evidence_seal") == sha256_digest(
        context_material
    )
    scenario_results = {
        item.get("scenario_ref"): item for item in context_material["scenario_results"]
    }
    condition_results = {
        item.get("condition_id"): item for item in context_material["condition_results"]
    }
    references_complete = bool(dossier.get("scenario_refs")) and context_sealed
    all_references: list[str] = []
    grouped_records: dict[str, list[dict]] = {}
    for group, minimum in F11_REFERENCE_REQUIREMENTS.items():
        refs = evidence_refs.get(group, [])
        if (
            not isinstance(refs, list)
            or len(refs) < minimum
            or len(set(refs)) != len(refs)
        ):
            references_complete = False
            continue
        all_references.extend(refs)
        grouped_records[group] = []
        for reference in refs:
            record = records.get(reference)
            if not isinstance(record, dict):
                references_complete = False
                continue
            material = {key: value for key, value in record.items() if key != "record_seal"}
            actual_scenario = scenario_results.get(record.get("scenario_ref"))
            actual_condition = condition_results.get(record.get("condition_id"))
            record_type = record.get("record_type")
            record_valid = all(
                (
                    record.get("record_id") == reference,
                    record.get("record_type") == F11_RECORD_TYPES[group],
                    record.get("scenario_ref") in dossier.get("scenario_refs", []),
                    isinstance(actual_scenario, dict),
                    isinstance(actual_condition, dict),
                    (actual_condition or {}).get("scenario_ref") == record.get("scenario_ref"),
                    record.get("scenario_result_hash")
                    == (sha256_digest(actual_scenario) if isinstance(actual_scenario, dict) else None),
                    record.get("condition_result_hash")
                    == (sha256_digest(actual_condition) if isinstance(actual_condition, dict) else None),
                    record.get("evidence_object_hash")
                    == _f11_evidence_object_hash(
                        record_type,
                        actual_scenario if isinstance(actual_scenario, dict) else {},
                        actual_condition if isinstance(actual_condition, dict) else {},
                    ),
                    record.get("record_seal") == sha256_digest(material),
                )
            )
            if not record_valid:
                references_complete = False
            grouped_records[group].append(record)
    if len(set(all_references)) != len(all_references):
        references_complete = False

    activation = grouped_records.get("activation_access_trace_refs", [])
    interventions = grouped_records.get("intervention_refs", [])
    controls = grouped_records.get("negative_control_refs", [])
    referenced_condition_ids = {
        record.get("condition_id")
        for group in grouped_records.values()
        for record in group
        if record.get("condition_id") in condition_results
    }
    referenced_conditions = [condition_results[item] for item in sorted(referenced_condition_ids)]
    referenced_scenario_refs = {item.get("scenario_ref") for item in referenced_conditions}
    if referenced_scenario_refs != set(dossier.get("scenario_refs", [])):
        references_complete = False
    provenance_roots = {
        scenario_results[reference].get("provenance_root_id")
        for reference in referenced_scenario_refs
        if reference in scenario_results
    }
    if len(provenance_roots) < 2 or None in provenance_roots:
        references_complete = False

    boundary_events = [
        event
        for actual in referenced_conditions
        for event in actual.get("trace", [])
        if event.get("event_type") == "BOUNDARY_TRANSFER"
    ]
    boundary_ids = {event.get("payload", {}).get("boundary_id") for event in boundary_events}
    boundary_owners = {
        event.get("payload", {}).get(field)
        for event in boundary_events
        for field in ("source_owner", "destination_owner")
    }
    if len(boundary_ids - {None}) < 2 and len(boundary_owners - {None}) < 2:
        references_complete = False

    if any(item.get("telemetry") != "complete" for item in activation):
        references_complete = False
    for item in activation:
        actual = condition_results.get(item.get("condition_id"), {})
        event_types = {event.get("event_type") for event in actual.get("trace", [])}
        if (
            actual.get("trace_telemetry_status") != "complete"
            or actual.get("trace_errors")
            or not {"SKILL_ACTIVATION", "KNOWLEDGE_ACCESS"}.issubset(event_types)
        ):
            references_complete = False
    if not interventions:
        references_complete = False
    for item in interventions + controls:
        actual = condition_results.get(item.get("condition_id"), {})
        if not actual.get("counterfactual_evidence", {}).get("intervention_runs"):
            references_complete = False
    if controls and interventions and not {
        item.get("condition_id") for item in controls
    }.intersection({item.get("condition_id") for item in interventions}):
        references_complete = False

    cheaper_repair_detected = bool(dossier.get("cheaper_repair_succeeded", False))
    supported_local_mechanisms = {"F3", "F4", "F5", "F6", "F10"}
    for actual in referenced_conditions:
        mechanism = actual.get("attribution", {}).get("mechanism")
        if mechanism in supported_local_mechanisms:
            cheaper_repair_detected = True
        if mechanism in {"F1", "F2"}:
            references_complete = False
        ordinary_dispositions = {
            judgment.get("overall") for judgment in actual.get("judgments", [])
        }
        if (
            len(actual.get("judgments", [])) < 2
            or len(ordinary_dispositions) != 1
            or "indeterminate" in ordinary_dispositions
        ):
            references_complete = False
        arms = actual.get("counterfactual_evidence", {}).get("intervention_runs", {})
        target_arm = arms.get("target") if isinstance(arms, dict) else None
        control_arm = arms.get("negative_control") if isinstance(arms, dict) else None
        if not target_arm or not control_arm:
            references_complete = False
            continue
        target_repairs = _f11_arm_stably_accepted(target_arm)
        stable_failed_target = _f11_arm_stably_rejected(target_arm)
        stable_control = _f11_arm_stably_rejected(control_arm)
        if target_repairs:
            cheaper_repair_detected = True
        if not stable_failed_target and not target_repairs:
            references_complete = False
        if not stable_control:
            references_complete = False

        collapse = actual.get("collapse_analysis", {})
        collapse_material = {key: value for key, value in collapse.items() if key != "analysis_seal"}
        collapse_valid = all(
            (
                collapse.get("irreducible") is True,
                len(set(collapse.get("world_state_hashes", []))) >= 2,
                len(set(collapse.get("required_behavior_hashes", []))) >= 2,
                set(collapse.get("representations_exercised", []))
                == F11_REQUIRED_REPRESENTATIONS,
                collapse.get("analysis_seal") == sha256_digest(collapse_material),
            )
        )
        if not collapse_valid:
            references_complete = False

        actual_scenario = scenario_results.get(actual.get("scenario_ref"), {})
        if not _f11_independent_adjudication_valid(actual, actual_scenario):
            references_complete = False

    if not references_complete:
        missing.append("referenced_evidence_incomplete")
    if cheaper_repair_detected:
        missing.append("cheaper_repair_defeats_f11")
    return {
        "research_reopening": not missing,
        "missing": missing,
        "authorization": "research_only",
    }


def _f11_evidence_object_hash(
    record_type: str | None, scenario_result: dict, condition_result: dict
) -> str | None:
    if not scenario_result or not condition_result:
        return None
    if record_type == "oracle_attack":
        material = {
            "scenario_hash": scenario_result.get("scenario_hash"),
            "oracle_hash": scenario_result.get("oracle_hash"),
            "validity": scenario_result.get("validity"),
        }
    elif record_type == "recurrence_run":
        material = {
            "trace": condition_result.get("trace"),
            "judgments": condition_result.get("judgments"),
        }
    elif record_type == "lineage_root":
        material = {
            "scenario_ref": scenario_result.get("scenario_ref"),
            "scenario_hash": scenario_result.get("scenario_hash"),
        }
    elif record_type == "owner_boundary":
        material = {
            "boundary_events": [
                event
                for event in condition_result.get("trace", [])
                if event.get("event_type") == "BOUNDARY_TRANSFER"
            ],
            "counterfactual": condition_result.get("counterfactual_evidence"),
        }
    elif record_type == "activation_access_trace":
        material = condition_result.get("trace")
    elif record_type in {"intervention_result", "negative_control"}:
        material = condition_result.get("counterfactual_evidence")
    elif record_type == "collapse_witness":
        material = condition_result.get("collapse_analysis")
    elif record_type == "adjudication":
        material = condition_result.get("independent_adjudication")
    else:
        return None
    return sha256_digest(material)


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def _scenario_ref(scenario: dict) -> str:
    identity = scenario["identity_version"]
    return f"{identity['scenario_id']}@{identity['scenario_version']}"


def _resolve_evidence_candidate(
    reference: str,
    conditions: dict[str, dict],
    evidence: dict,
) -> dict:
    namespace, key = reference.split(":", 1)
    if namespace == "condition":
        return conditions[key]["candidate"]
    if namespace == "catalog":
        return evidence["candidate_catalog"][key]
    raise ValueError(f"unsupported evidence candidate reference: {reference}")


def _packet_expected_route(scenario: dict, packet: dict) -> str | None:
    return (
        (packet.get("route_requirement") or {}).get("requested_route")
        or (packet.get("local_content_audit") or {}).get("owner_scope")
        or F6_CAPSULE_SPECS.get(_scenario_ref(scenario), {}).get("owner_scope")
    )


def _build_evidence_trace(
    scenario: dict,
    condition: dict,
    profile_name: str,
    evidence: dict,
    target: dict,
    run_suffix: str = "ordinary",
    intervention: dict | None = None,
    output_candidate: dict | None = None,
    intended_condition: str = "with_skill",
    boundary_audit: dict | None = None,
    requested_route: str | None = None,
) -> list[dict]:
    profile = evidence["trace_profiles"][profile_name]
    run_id = f"RUN-{condition['condition_id']}-{run_suffix}"
    prompt_digest = sha256_digest(scenario["user_visible_package"])
    events = [
        make_event(
            run_id,
            1,
            "RUN_BOUND",
            {
                "scenario_id": scenario["identity_version"]["scenario_id"],
                "scenario_hash": sha256_digest(scenario),
                "oracle_id": scenario["identity_version"]["oracle_version"],
                "oracle_hash": sha256_digest(scenario["oracle"]),
                "condition_id": condition["condition_id"],
                "intended_visible_input_digest": prompt_digest,
                "delivered_visible_input_digest": prompt_digest,
                "common_scaffold_digest": sha256_digest({"pilot": "pressure-discovery-v1"}),
                "model_configuration_digest": sha256_digest(target),
                "tools_permissions_digest": sha256_digest({"filesystem": "read-only-runtime"}),
                "external_evidence_digest": sha256_digest(
                    {
                        "raw_source_snapshot_ref": scenario["external_provenance"].get(
                            "raw_source_snapshot_ref"
                        ),
                        "raw_source_snapshot_hash": scenario["external_provenance"].get(
                            "raw_source_snapshot_hash"
                        ),
                        "visible_external_refs": scenario["user_visible_package"][
                            "tools_external_evidence"
                        ],
                    }
                ),
                "fresh_context_id": f"FRESH-{condition['condition_id']}-{run_suffix}",
                "diagnostic_mode": scenario.get("lane") == "diagnostic_injection",
                "start_time": "2026-08-24T00:00:00Z",
            },
        )
    ]
    sequence = 2
    activation = profile["activation"]
    baseline = intended_condition == "without_skill"
    active = activation == "activated" and not baseline
    events.append(
        make_event(
            run_id,
            sequence,
            "SKILL_ACTIVATION",
            {
                "intended_condition": intended_condition,
                "requested_skill_id": None if baseline else target["skill_id"],
                "requested_skill_version": None if baseline else target["version"],
                "requested_skill_hash": None if baseline else sha256_digest(target),
                "active_skill_id": target["skill_id"] if active else None,
                "active_skill_version": target["version"] if active else None,
                "active_skill_hash": sha256_digest(target) if active else None,
                "outcome": activation,
                "activation_error_reference": None
                if active or baseline
                else f"ACTIVATION-{condition['condition_id']}",
            },
        )
    )
    sequence += 1

    if intervention:
        intervention_material = {
            key: value
            for key, value in intervention.items()
            if key != "negative_control_run_id"
        }
        events.append(
            make_event(
                run_id,
                sequence,
                "INTERVENTION_APPLIED",
                {
                    "intervention_type": intervention["intervention_type"],
                    "version_hash": sha256_digest(intervention_material),
                    "injected_content_kind": intervention["injected_content_kind"],
                    "injected_content_hash": intervention["injected_content_hash"],
                    "target": condition["condition_id"],
                    "delta_manifest": intervention["delta_manifest"],
                    "held_constant_manifest": intervention["held_constant_manifest"],
                    "control_intervention_label": intervention["arm"],
                    "negative_control_reference": intervention.get(
                        "negative_control_run_id"
                    ),
                },
            )
        )
        sequence += 1

    access = profile["access"]
    if access in {"requested_unresolved", "requested_delivered", "direct"}:
        request_id = f"REQUEST-{condition['condition_id']}-{run_suffix}"
        route = (intervention or {}).get("route_override") or condition.get(
            "route_requirement", {}
        ).get("requested_route") or requested_route or "content.consequential-strategy"
        direct = access == "direct"
        requested_id = (
            scenario["external_provenance"].get("raw_source_snapshot_ref") if direct else route
        )
        events.append(
            make_event(
                run_id,
                sequence,
                "KNOWLEDGE_REQUEST",
                {
                    "request_id": request_id,
                    "request_kind": "direct_resource" if direct else "logical_route",
                    "requested_id": requested_id,
                    "initiator": "forced_intervention"
                    if (intervention or {}).get("route_override")
                    else "normal_execution",
                },
            )
        )
        sequence += 1
        delivered = access in {"requested_delivered", "direct"}
        resource = requested_id if direct else (f"resource:{route}" if delivered else None)
        events.append(
            make_event(
                run_id,
                sequence,
                "KNOWLEDGE_ACCESS",
                {
                    "request_id": request_id,
                    "route_id": None if direct else route,
                    "resolution_status": "resolved" if delivered else "unresolved",
                    "delivery_status": "delivered" if delivered else "not-delivered",
                    "resolver_mode": "direct" if direct else "index",
                    "route_index_hash": None
                    if direct
                    else sha256_digest({"route": route, "index": "frozen"}),
                    "resource_id": resource,
                    "resource_hash": sha256_digest({"resource": resource}) if resource else None,
                    "selector_hash": sha256_digest({"selector": requested_id}) if delivered else None,
                    "extracted_content_hash": sha256_digest({"extract": requested_id}) if delivered else None,
                    "fallback_error_status": None if delivered else "unresolved",
                },
            )
        )
        sequence += 1

    boundary = boundary_audit or condition.get("boundary_audit")
    if boundary and boundary.get("transfer_status") in {"lost", "delivered"}:
        events.append(
            make_event(
                run_id,
                sequence,
                "BOUNDARY_TRANSFER",
                {
                    "boundary_id": boundary["boundary_id"],
                    "source_owner": boundary["source_owner"],
                    "destination_owner": boundary["destination_owner"],
                    "upstream_artifact_hash_ref": boundary["upstream_artifact_hash"],
                    "downstream_received_artifact_hash_ref": boundary["downstream_artifact_hash"],
                    "critical_assertion_ids": boundary["required_assertion_ids"],
                    "transfer_status": boundary["transfer_status"],
                },
            )
        )
        sequence += 1

    return seal_trace(
        events,
        sha256_digest((output_candidate or condition["candidate"])["output"]),
        profile["telemetry"],
        "2026-08-24T00:01:00Z",
    )


def _judgment_behavior_tags(scenario: dict, judgments: list[dict]) -> list[str]:
    if not judgments or all(item.get("overall") == "acceptable" for item in judgments):
        return []
    tags: set[str] = set()
    modifiers = set(scenario["oracle"].get("modifiers", []))
    predicate_slots = {
        predicate["predicate_id"]: predicate["slot"]
        for collection in ("must", "must_not")
        for predicate in scenario["oracle"].get(collection, [])
    }
    violated_slots = {
        predicate_slots.get(criterion["predicate_id"])
        for judgment in judgments
        for criterion in judgment.get("criteria", [])
        if criterion.get("result") == "violated"
    }
    fixed_state_visible = any(
        item.get("commitment_status") == "fixed"
        for item in scenario.get("evidence_state_ledger", [])
    )
    if "R" in modifiers and fixed_state_visible and violated_slots.intersection({"D", "S"}):
        tags.add("F7")
    if "A" in modifiers and "A" in violated_slots:
        tags.add("F9")
    if not tags and violated_slots.intersection({"E", "U"}):
        tags.add("F8")
    return sorted(tags)


def _all_judges_accept(judgments: list[dict]) -> bool:
    return bool(judgments) and all(item.get("overall") == "acceptable" for item in judgments)


def _trace_output_is_bound(trace: list[dict], candidate: dict) -> bool:
    sealed = [
        event["payload"] for event in trace if event["event_type"] == "RUN_SEALED"
    ]
    return bool(
        len(sealed) == 1
        and isinstance(candidate.get("output"), str)
        and sealed[0].get("final_output_hash")
        == sha256_digest(candidate["output"])
    )


def _rubric_defect_established(
    scenario: dict,
    packet: dict,
    conditions: dict[str, dict],
    evidence: dict,
    judge: dict,
) -> bool:
    challenge = packet.get("rubric_challenge")
    if not challenge or len(challenge.get("oracles", [])) != 2 or len(challenge.get("anchors", [])) != 2:
        return False
    defective_spec = challenge["oracles"][0]
    defective = copy.deepcopy(scenario)
    defective["oracle"]["must"] = [
        {
            "predicate_id": "RUBRIC-DEFECTIVE-M1",
            "activation": {"always": True},
            "slot": defective_spec["must"][0]["slot"],
            "relation": defective_spec["must"][0]["relation"],
            "value": defective_spec["must"][0]["value"],
            "contract_clause": "Defective canonical-wording requirement.",
            "hard": True,
            "fatal": True,
        }
    ]
    defective["oracle"]["must_not"] = []
    observed: list[tuple[str, str]] = []
    for anchor in challenge["anchors"]:
        candidate = anchor.get("candidate") or _resolve_evidence_candidate(
            anchor["candidate_ref"], conditions, evidence
        )
        observed.append(
            (
                judge_candidate(defective, candidate, judge)["overall"],
                judge_candidate(scenario, candidate, judge)["overall"],
            )
        )
    return observed == [("unacceptable", "acceptable"), ("acceptable", "unacceptable")]


def _intervention_assessment(
    scenario: dict,
    condition: dict,
    packet: dict,
    conditions: dict[str, dict],
    evidence: dict,
    judges: list[dict],
    target: dict,
) -> dict:
    arm_declarations = packet.get("intervention_runs", [])
    arm_names = [arm.get("arm") for arm in arm_declarations]
    if len(arm_names) != len(set(arm_names)):
        return {}
    records = []
    control_index = next(
        (
            index
            for index, arm in enumerate(packet.get("intervention_runs", []), start=1)
            if arm.get("arm") == "negative_control"
        ),
        None,
    )
    for index, arm in enumerate(packet.get("intervention_runs", []), start=1):
        candidate = _resolve_evidence_candidate(arm["candidate_ref"], conditions, evidence)
        if arm.get("arm") == "target" and packet.get("neutral_artifact"):
            injected_content_kind = "neutral_artifact"
            injected_content = packet["neutral_artifact"]
        elif arm.get("arm") == "target" and packet.get("state_capsule"):
            injected_content_kind = "boundary_state_package"
            injected_content = {
                "boundary_audit": packet.get("boundary_audit"),
                "boundary_contract": packet.get("boundary_contract"),
                "state_capsule": packet.get("state_capsule"),
            }
        elif arm.get("route_override"):
            injected_content_kind = "logical_route"
            injected_content = {"route_id": arm["route_override"]}
        else:
            injected_content_kind = "negative_control"
            injected_content = {
                "intervention_type": arm.get("intervention_type"),
                "delta_manifest": arm.get("delta_manifest"),
            }
        material_arm = {
            **arm,
            "injected_content_kind": injected_content_kind,
            "injected_content_hash": sha256_digest(injected_content),
        }
        stability_runs = []
        for repeat in range(1, packet.get("stability_repeat_count", 1) + 1):
            judgments = [judge_candidate(scenario, candidate, judge) for judge in judges]
            trace = _build_evidence_trace(
                scenario,
                condition,
                arm["trace_profile"],
                evidence,
                target,
                run_suffix=f"intervention-{index}-repeat-{repeat}",
                intervention={
                    **material_arm,
                    "negative_control_run_id": (
                        f"RUN-{condition['condition_id']}-intervention-{control_index}-repeat-{repeat}"
                        if control_index is not None
                        else None
                    ),
                },
                output_candidate=candidate,
                boundary_audit=packet.get("boundary_audit"),
                requested_route=_packet_expected_route(scenario, packet),
            )
            stability_runs.append(
                {
                    "repeat": repeat,
                    "judgments": judgments,
                    "trace": trace,
                    "trace_errors": validate_trace(trace),
                    "telemetry": trace[-1]["payload"]["telemetry_completeness_status"],
                    "output_bound": _trace_output_is_bound(trace, candidate),
                }
            )
        records.append(
            {
                "arm": arm["arm"],
                "injected_content_kind": injected_content_kind,
                "injected_content_hash": sha256_digest(injected_content),
                "candidate_hash": sha256_digest(candidate),
                "judgments": stability_runs[0]["judgments"],
                "trace": stability_runs[0]["trace"],
                "trace_errors": [
                    error
                    for run in stability_runs
                    for error in run["trace_errors"]
                ],
                "stability_runs": stability_runs,
            }
        )
    return {item["arm"]: item for item in records}


def _logical_delivery_signature(trace: list[dict]) -> dict | None:
    requests = [
        event["payload"] for event in trace if event["event_type"] == "KNOWLEDGE_REQUEST"
    ]
    accesses = [
        event["payload"] for event in trace if event["event_type"] == "KNOWLEDGE_ACCESS"
    ]
    if len(requests) != 1 or len(accesses) != 1:
        return None
    request = requests[0]
    access = accesses[0]
    if not all(
        (
            request.get("request_kind") == "logical_route",
            bool(request.get("requested_id")),
            isinstance(request.get("initiator"), str),
            request.get("initiator") in KNOWLEDGE_REQUEST_INITIATORS,
            request.get("request_id") == access.get("request_id"),
            access.get("route_id") == request.get("requested_id"),
            access.get("resolution_status") == "resolved",
            access.get("delivery_status") == "delivered",
            access.get("resolver_mode") == "index",
            bool(access.get("route_index_hash")),
            bool(access.get("resource_id")),
            bool(access.get("resource_hash")),
            bool(access.get("selector_hash")),
            bool(access.get("extracted_content_hash")),
            access.get("fallback_error_status") is None,
        )
    ):
        return None
    return {
        "request_kind": request["request_kind"],
        "requested_id": request["requested_id"],
        "initiator": request["initiator"],
        **{key: value for key, value in access.items() if key != "request_id"},
    }


def _intervention_events_are_causally_bound(
    interventions: dict, packet: dict, condition_id: str
) -> bool:
    declarations = packet.get("intervention_runs", [])
    declaration_names = [item.get("arm") for item in declarations]
    if not interventions or len(declaration_names) != len(set(declaration_names)):
        return False
    declaration_by_arm = {item.get("arm"): item for item in declarations}
    if set(declaration_by_arm) != set(interventions):
        return False
    for arm_name, assessment in interventions.items():
        declaration = declaration_by_arm.get(arm_name, {})
        runs = assessment.get("stability_runs", [])
        if not declaration or not runs or assessment.get("arm") != arm_name:
            return False
        material_declaration = {
            **declaration,
            "injected_content_kind": assessment.get("injected_content_kind"),
            "injected_content_hash": assessment.get("injected_content_hash"),
        }
        for run in runs:
            trace = run.get("trace", [])
            event_types = [event.get("event_type") for event in trace]
            if not all(
                (
                    not validate_trace(trace),
                    event_types[:3]
                    == ["RUN_BOUND", "SKILL_ACTIVATION", "INTERVENTION_APPLIED"],
                    event_types.count("INTERVENTION_APPLIED") == 1,
                )
            ):
                return False
            intervention_event = trace[2]
            payload = intervention_event.get("payload", {})
            if not all(
                (
                    intervention_event.get("sequence") == 3,
                    intervention_event.get("run_id") == trace[0].get("run_id"),
                    payload.get("control_intervention_label") == arm_name,
                    payload.get("target") == condition_id,
                    payload.get("intervention_type")
                    == declaration.get("intervention_type"),
                    payload.get("version_hash")
                    == sha256_digest(material_declaration),
                    payload.get("injected_content_kind")
                    == assessment.get("injected_content_kind"),
                    payload.get("injected_content_hash")
                    == assessment.get("injected_content_hash"),
                    payload.get("delta_manifest")
                    == declaration.get("delta_manifest"),
                    payload.get("held_constant_manifest")
                    == declaration.get("held_constant_manifest"),
                )
            ):
                return False
    return True


def _intervention_access_is_held_constant(
    interventions: dict, ordinary_signature: dict | None
) -> bool:
    if ordinary_signature is None or not interventions:
        return False
    runs = [
        run
        for arm in interventions.values()
        for run in arm.get("stability_runs", [])
    ]
    return bool(runs) and all(
        _logical_delivery_signature(run.get("trace", [])) == ordinary_signature
        for run in runs
    )


def _activation_signature(trace: list[dict]) -> dict | None:
    activations = [
        event["payload"] for event in trace if event["event_type"] == "SKILL_ACTIVATION"
    ]
    return copy.deepcopy(activations[0]) if len(activations) == 1 else None


def _run_bound_invariant_signature(trace: list[dict]) -> dict | None:
    run_bounds = [
        event["payload"] for event in trace if event["event_type"] == "RUN_BOUND"
    ]
    if len(run_bounds) != 1:
        return None
    return {
        key: copy.deepcopy(value)
        for key, value in run_bounds[0].items()
        if key not in {"fresh_context_id", "start_time"}
    }


def _intervention_run_bound_is_held_constant(
    interventions: dict, ordinary_signature: dict | None
) -> bool:
    if ordinary_signature is None or not interventions:
        return False
    runs = [
        run
        for arm in interventions.values()
        for run in arm.get("stability_runs", [])
    ]
    return bool(runs) and all(
        _run_bound_invariant_signature(run.get("trace", [])) == ordinary_signature
        for run in runs
    )


def _intervention_activation_is_held_constant(
    interventions: dict, ordinary_signature: dict | None
) -> bool:
    if ordinary_signature is None or ordinary_signature.get("outcome") != "activated":
        return False
    runs = [
        run
        for arm in interventions.values()
        for run in arm.get("stability_runs", [])
    ]
    return bool(runs) and all(
        _activation_signature(run.get("trace", [])) == ordinary_signature
        for run in runs
    )


def _delivery_signature_matches_route(
    signature: dict | None,
    expected_route: str | None,
    expected_initiator: str,
) -> bool:
    if signature is None or not expected_route:
        return False
    resource_id = f"resource:{expected_route}"
    return all(
        (
            signature.get("requested_id") == expected_route,
            signature.get("initiator") == expected_initiator,
            signature.get("route_id") == expected_route,
            signature.get("route_index_hash")
            == sha256_digest({"route": expected_route, "index": "frozen"}),
            signature.get("resource_id") == resource_id,
            signature.get("resource_hash") == sha256_digest({"resource": resource_id}),
            signature.get("selector_hash")
            == sha256_digest({"selector": expected_route}),
            signature.get("extracted_content_hash")
            == sha256_digest({"extract": expected_route}),
        )
    )


def _f4_route_intervention_is_bound(
    declaration: dict,
    assessment: dict | None,
    expected_arm: str,
    expected_type: str,
    expected_route: str | None,
    condition_id: str,
) -> bool:
    if not declaration or not assessment or not expected_route:
        return False
    expected_delta = [f"route {expected_route} delivered"]
    expected_held_constant = ["scenario", "oracle", "model", "tools"]
    injected_content_hash = sha256_digest({"route_id": expected_route})
    material_declaration = {
        **declaration,
        "injected_content_kind": "logical_route",
        "injected_content_hash": injected_content_hash,
    }
    if not all(
        (
            declaration.get("arm") == expected_arm,
            declaration.get("intervention_type") == expected_type,
            declaration.get("route_override") == expected_route,
            declaration.get("delta_manifest") == expected_delta,
            declaration.get("held_constant_manifest") == expected_held_constant,
            assessment.get("arm") == expected_arm,
            assessment.get("injected_content_kind") == "logical_route",
            assessment.get("injected_content_hash") == injected_content_hash,
        )
    ):
        return False
    runs = assessment.get("stability_runs", [])
    if not runs:
        return False
    for run in runs:
        trace = run.get("trace", [])
        if validate_trace(trace):
            return False
        event_types = [event.get("event_type") for event in trace]
        if not all(
            (
                event_types
                == [
                    "RUN_BOUND",
                    "SKILL_ACTIVATION",
                    "INTERVENTION_APPLIED",
                    "KNOWLEDGE_REQUEST",
                    "KNOWLEDGE_ACCESS",
                    "RUN_SEALED",
                ],
            )
        ):
            return False
        intervention_index = event_types.index("INTERVENTION_APPLIED")
        request_index = event_types.index("KNOWLEDGE_REQUEST")
        access_index = event_types.index("KNOWLEDGE_ACCESS")
        if not intervention_index < request_index < access_index:
            return False
        intervention_payload = trace[intervention_index]["payload"]
        request_payload = trace[request_index]["payload"]
        if not all(
            (
                request_payload.get("initiator") == "forced_intervention",
                request_payload.get("request_kind") == "logical_route",
                request_payload.get("requested_id") == expected_route,
                intervention_payload.get("intervention_type") == expected_type,
                intervention_payload.get("version_hash")
                == sha256_digest(material_declaration),
                intervention_payload.get("injected_content_kind")
                == "logical_route",
                intervention_payload.get("injected_content_hash")
                == injected_content_hash,
                intervention_payload.get("target") == condition_id,
                intervention_payload.get("delta_manifest") == expected_delta,
                intervention_payload.get("held_constant_manifest")
                == expected_held_constant,
                intervention_payload.get("control_intervention_label")
                == expected_arm,
                _delivery_signature_matches_route(
                    _logical_delivery_signature(trace),
                    expected_route,
                    "forced_intervention",
                ),
            )
        ):
            return False
    return True


def _ordinary_route_failure_state(
    trace: list[dict], required_route: str | None
) -> str | None:
    if [event.get("event_type") for event in trace] != [
        "RUN_BOUND",
        "SKILL_ACTIVATION",
        "KNOWLEDGE_REQUEST",
        "KNOWLEDGE_ACCESS",
        "RUN_SEALED",
    ]:
        return None
    requests = [
        event["payload"]
        for event in trace
        if event["event_type"] == "KNOWLEDGE_REQUEST"
    ]
    accesses = [
        event["payload"]
        for event in trace
        if event["event_type"] == "KNOWLEDGE_ACCESS"
    ]
    if len(requests) != 1 or len(accesses) != 1 or not required_route:
        return None
    request = requests[0]
    access = accesses[0]
    if not all(
        (
            request.get("request_kind") == "logical_route",
            request.get("initiator") == "normal_execution",
            isinstance(request.get("requested_id"), str),
            bool(request.get("requested_id")),
            request.get("request_id") == access.get("request_id"),
        )
    ):
        return None
    requested_route = request["requested_id"]
    if all(
        (
            requested_route == required_route,
            access.get("route_id") in {None, required_route},
            access.get("resolution_status") == "unresolved",
            access.get("delivery_status") == "not-delivered",
            access.get("resolver_mode") != "direct",
        )
    ):
        return "required_route_unresolved"
    delivered = _logical_delivery_signature(trace)
    if all(
        (
            requested_route != required_route,
            _delivery_signature_matches_route(
                delivered, requested_route, "normal_execution"
            ),
        )
    ):
        return "wrong_route_delivered"
    return None


def _classify_from_evidence(
    scenario: dict,
    condition: dict,
    packet: dict,
    conditions: dict[str, dict],
    evidence: dict,
    judgments: list[dict],
    trace: list[dict],
    trace_errors: list[str],
    judges: list[dict],
    target: dict,
) -> tuple[dict, dict]:
    behavioral_tags = _judgment_behavior_tags(scenario, judgments)
    result_packet = {"failure_established": not _all_judges_accept(judgments), "behavioral_tags": behavioral_tags}

    if _rubric_defect_established(scenario, packet, conditions, evidence, judges[0]):
        return _attribution("F1", "defective and corrected oracles reverse both locked anchors", result_packet), {"rubric_challenge": "established"}

    telemetry = trace[-1]["payload"].get("telemetry_completeness_status")
    if telemetry != "complete" or trace_errors:
        return _attribution("F12", "operational telemetry is incomplete or invalid", result_packet), {}
    if not _trace_output_is_bound(trace, condition["candidate"]):
        return _attribution(
            "F12", "ordinary output seal is not bound to the evaluated candidate", result_packet
        ), {}

    repeat_arms = packet.get("repeat_arms", [])
    if repeat_arms:
        expected_arms = {("A", "without_skill"), ("B", "with_skill")}
        observed_arms = {
            (item.get("arm"), item.get("condition")) for item in repeat_arms
        }
        repeat_run_ids = [
            run.get("run_id") for item in repeat_arms for run in item.get("runs", [])
        ]
        repeat_shape_valid = all(
            (
                len(repeat_arms) == 2,
                observed_arms == expected_arms,
                all(len(item.get("runs", [])) == 3 for item in repeat_arms),
                len(repeat_run_ids) == 6,
                len(set(repeat_run_ids)) == 6,
                all(repeat_run_ids),
                all(
                    run.get("trace_profile") == "baseline_direct"
                    for item in repeat_arms
                    if item.get("condition") == "without_skill"
                    for run in item.get("runs", [])
                ),
            )
        )
        if not repeat_shape_valid:
            return _attribution(
                "F12", "matched-repeat packet does not satisfy the frozen two-by-three A/B shape", result_packet
            ), {"repeat_arms": []}

    repeat_records = []
    for repeat_arm in repeat_arms:
        for repeat in repeat_arm.get("runs", []):
            candidate = _resolve_evidence_candidate(repeat["candidate_ref"], conditions, evidence)
            repeat_trace = _build_evidence_trace(
                scenario,
                condition,
                repeat["trace_profile"],
                evidence,
                target,
                repeat["run_id"],
                output_candidate=candidate,
                intended_condition=repeat_arm["condition"],
                boundary_audit=packet.get("boundary_audit"),
                requested_route=_packet_expected_route(scenario, packet),
            )
            repeat_records.append(
                {
                    "arm": repeat_arm["arm"],
                    "condition": repeat_arm["condition"],
                    "run_id": repeat["run_id"],
                    "candidate_hash": sha256_digest(candidate),
                    "judgments": [judge_candidate(scenario, candidate, judge) for judge in judges],
                    "trace": repeat_trace,
                    "trace_errors": validate_trace(repeat_trace),
                    "telemetry": repeat_trace[-1]["payload"]["telemetry_completeness_status"],
                    "output_bound": _trace_output_is_bound(repeat_trace, candidate),
                }
            )
    if repeat_records:
        if any(
            item["trace_errors"]
            or item["telemetry"] != "complete"
            or not item["output_bound"]
            for item in repeat_records
        ):
            return _attribution("F12", "matched-repeat telemetry is incomplete", result_packet), {"repeat_arms": repeat_records}
        invariant_payloads = []
        activation_conditions = []
        for item in repeat_records:
            run_bound = next(
                event["payload"] for event in item["trace"] if event["event_type"] == "RUN_BOUND"
            )
            invariant_payloads.append(
                {
                    key: value
                    for key, value in run_bound.items()
                    if key not in {"fresh_context_id", "start_time"}
                }
            )
            activation_conditions.append(
                next(
                    event["payload"]["intended_condition"]
                    for event in item["trace"]
                    if event["event_type"] == "SKILL_ACTIVATION"
                )
            )
        if len({sha256_digest(item) for item in invariant_payloads}) != 1 or any(
            item["condition"] != activation_condition
            for item, activation_condition in zip(repeat_records, activation_conditions)
        ):
            return _attribution(
                "F12", "matched-repeat invariants or A/B activation conditions differ", result_packet
            ), {"repeat_arms": repeat_records}
        arm_dispositions = {
            arm: {
                "acceptable" if _all_judges_accept(item["judgments"]) else "unacceptable"
                for item in repeat_records
                if item["arm"] == arm
            }
            for arm in {item["arm"] for item in repeat_records}
        }
        if any(len(dispositions) > 1 for dispositions in arm_dispositions.values()):
            return _attribution("F2", "two matched arms of three outputs have mixed material dispositions", result_packet), {"repeat_arms": repeat_records}

    if _all_judges_accept(judgments):
        return _attribution("NO_FAILURE", "both fixture judges accept the ordinary output", result_packet), {}

    activation = next(event for event in trace if event["event_type"] == "SKILL_ACTIVATION")
    activation_payload = activation["payload"]
    activation_receipt = packet.get("activation_receipt", {})
    receipt_grounded = all(
        (
            activation_receipt.get("requested_skill_id")
            == activation_payload.get("requested_skill_id"),
            activation_receipt.get("active_skill_id")
            == activation_payload.get("active_skill_id"),
            activation_receipt.get("outcome") == activation_payload.get("outcome"),
            activation_receipt.get("error_ref")
            == activation_payload.get("activation_error_reference"),
        )
    )
    if activation_payload["outcome"] != "activated":
        unauthorized_fallback = (
            activation_payload["outcome"] == "fallback"
            and activation_receipt.get("fallback_authorization") == "unauthorized"
        )
        if receipt_grounded and (
            activation_payload["outcome"] in {"not-activated", "error"}
            or unauthorized_fallback
        ):
            return _attribution("F3", "sealed activation receipt records a delivery failure or unauthorized fallback", result_packet), {}
        return _attribution("F12", "activation outcome lacks a bound authorization receipt", result_packet), {}

    run_bound = next(event["payload"] for event in trace if event["event_type"] == "RUN_BOUND")
    target_hash = sha256_digest(target)
    expected_external_evidence_digest = sha256_digest(
        {
            "raw_source_snapshot_ref": scenario["external_provenance"].get(
                "raw_source_snapshot_ref"
            ),
            "raw_source_snapshot_hash": scenario["external_provenance"].get(
                "raw_source_snapshot_hash"
            ),
            "visible_external_refs": scenario["user_visible_package"][
                "tools_external_evidence"
            ],
        }
    )
    intended_binding_grounded = all(
        (
            run_bound.get("scenario_id") == scenario["identity_version"]["scenario_id"],
            run_bound.get("scenario_hash") == sha256_digest(scenario),
            run_bound.get("oracle_id") == scenario["identity_version"]["oracle_version"],
            run_bound.get("oracle_hash") == sha256_digest(scenario["oracle"]),
            run_bound.get("condition_id") == condition["condition_id"],
            run_bound.get("intended_visible_input_digest")
            == sha256_digest(scenario["user_visible_package"]),
            run_bound.get("delivered_visible_input_digest") is not None,
            run_bound.get("common_scaffold_digest") is not None,
            run_bound.get("model_configuration_digest") is not None,
            run_bound.get("tools_permissions_digest")
            == sha256_digest({"filesystem": "read-only-runtime"}),
            run_bound.get("external_evidence_digest") == expected_external_evidence_digest,
            isinstance(run_bound.get("fresh_context_id"), str)
            and bool(run_bound["fresh_context_id"]),
            type(run_bound.get("diagnostic_mode")) is bool
            and run_bound["diagnostic_mode"]
            == (scenario.get("lane") == "diagnostic_injection"),
            isinstance(run_bound.get("start_time"), str) and bool(run_bound["start_time"]),
            activation_payload.get("requested_skill_id") == target["skill_id"],
            activation_payload.get("requested_skill_version") == target["version"],
            activation_payload.get("requested_skill_hash") == target_hash,
            all(
                activation_payload.get(field) is not None
                for field in ("active_skill_id", "active_skill_version", "active_skill_hash")
            ),
            all(
                isinstance(activation_payload.get(field), str)
                and bool(activation_payload[field])
                for field in ("active_skill_id", "active_skill_version")
            ),
        )
    )
    if not intended_binding_grounded:
        return _attribution(
            "F12", "activation or delivery binding lacks complete frozen-target grounding", result_packet
        ), {}

    binding_mismatches = []
    if (
        run_bound["delivered_visible_input_digest"]
        != run_bound["intended_visible_input_digest"]
    ):
        binding_mismatches.append("delivered visible input")
    if run_bound["common_scaffold_digest"] != sha256_digest(
        {"pilot": "pressure-discovery-v1"}
    ):
        binding_mismatches.append("common scaffold")
    if run_bound["model_configuration_digest"] != target_hash:
        binding_mismatches.append("model configuration")
    if any(
        (
            activation_payload["active_skill_id"] != target["skill_id"],
            activation_payload["active_skill_version"] != target["version"],
            activation_payload["active_skill_hash"] != target_hash,
        )
    ):
        binding_mismatches.append("active skill identity")
    if binding_mismatches:
        return _attribution(
            "F3",
            "sealed binding differs from the frozen " + ", ".join(binding_mismatches),
            result_packet,
        ), {}

    interventions = _intervention_assessment(
        scenario, condition, packet, conditions, evidence, judges, target
    )
    target_arm = interventions.get("target")
    control_arm = interventions.get("negative_control")
    stable_target = bool(target_arm) and all(
        not run["trace_errors"]
        and run["telemetry"] == "complete"
        and run.get("output_bound") is True
        and _all_judges_accept(run["judgments"])
        for run in target_arm.get("stability_runs", [])
    )
    stable_control = bool(control_arm) and all(
        not run["trace_errors"]
        and run["telemetry"] == "complete"
        and run.get("output_bound") is True
        and not _all_judges_accept(run["judgments"])
        for run in control_arm.get("stability_runs", [])
    )
    control_run_ids = {
        run["trace"][0]["run_id"] for run in (control_arm or {}).get("stability_runs", [])
    }
    target_control_refs = {
        event["payload"].get("negative_control_reference")
        for run in (target_arm or {}).get("stability_runs", [])
        for event in run["trace"]
        if event["event_type"] == "INTERVENTION_APPLIED"
    }
    control_reference_bound = bool(target_control_refs) and target_control_refs.issubset(
        control_run_ids
    )
    intervention_activation_held = _intervention_activation_is_held_constant(
        interventions, _activation_signature(trace)
    )
    intervention_run_bound_held = _intervention_run_bound_is_held_constant(
        interventions, _run_bound_invariant_signature(trace)
    )
    intervention_events_bound = _intervention_events_are_causally_bound(
        interventions, packet, condition["condition_id"]
    )
    selective_repair = bool(
        target_arm
        and control_arm
        and packet.get("stability_repeat_count", 0) >= 2
        and not target_arm["trace_errors"]
        and not control_arm["trace_errors"]
        and stable_target
        and stable_control
        and control_reference_bound
        and intervention_events_bound
        and intervention_run_bound_held
    )

    accesses = [event["payload"] for event in trace if event["event_type"] == "KNOWLEDGE_ACCESS"]
    route_required = packet.get("route_requirement", {})
    route_requirement_material = {
        key: value for key, value in route_required.items() if key != "requirement_hash"
    }
    f4_route_spec = F4_ROUTE_REQUIREMENT_SPECS.get(
        (_scenario_ref(scenario), condition["condition_id"]), {}
    )
    f4_requirement_spec = f4_route_spec.get("route_requirement", {})
    required_predicate_ids = set(route_required.get("oracle_predicate_ids", []))
    predicate_ids = {
        predicate["predicate_id"]
        for collection in ("must", "must_not")
        for predicate in scenario["oracle"].get(collection, [])
    }
    requirement_grounded = all(
        (
            bool(f4_requirement_spec),
            route_requirement_material == f4_requirement_spec,
            bool(required_predicate_ids),
            required_predicate_ids.issubset(predicate_ids),
            route_required.get("requirement_hash")
            == sha256_digest(f4_requirement_spec),
        )
    )
    required_route = f4_requirement_spec.get("requested_route")
    ordinary_route_failure = _ordinary_route_failure_state(trace, required_route)
    intervention_declarations = packet.get("intervention_runs", [])
    intervention_arm_names = [
        arm.get("arm") for arm in intervention_declarations
    ]
    f4_arm_shape_valid = bool(
        len(intervention_declarations) == 2
        and intervention_arm_names.count("target") == 1
        and intervention_arm_names.count("negative_control") == 1
    )
    intervention_specs = (
        {arm["arm"]: arm for arm in intervention_declarations}
        if f4_arm_shape_valid
        else {}
    )
    target_route = intervention_specs.get("target", {}).get("route_override")
    control_route = intervention_specs.get("negative_control", {}).get(
        "route_override"
    )
    expected_control_route = f4_route_spec.get("negative_control_route")
    exact_route_intervention = bool(
        f4_arm_shape_valid
        and required_route
        and target_route == required_route
        and control_route == expected_control_route
        and expected_control_route != required_route
        and _f4_route_intervention_is_bound(
            intervention_specs.get("target", {}),
            target_arm,
            "target",
            "restore_required_route",
            required_route,
            condition["condition_id"],
        )
        and _f4_route_intervention_is_bound(
            intervention_specs.get("negative_control", {}),
            control_arm,
            "negative_control",
            "deliver_irrelevant_route",
            expected_control_route,
            condition["condition_id"],
        )
    )
    if ordinary_route_failure and requirement_grounded and exact_route_intervention and intervention_activation_held and selective_repair:
        return _attribution("F4", "required route restoration selectively repairs against an irrelevant-route control", result_packet), {
            "intervention_runs": interventions,
            "route_requirement": copy.deepcopy(route_required),
        }

    audit = packet.get("local_content_audit")
    artifact = packet.get("neutral_artifact", {})
    purity_review = packet.get("purity_review", {})
    f5_spec = F5_SCENARIO_SPECS.get(_scenario_ref(scenario), {})
    propositions = artifact.get("propositions", [])
    semantic_tokens = [
        token
        for proposition in propositions
        for token in proposition.get("semantic_tokens", [])
    ]
    template_valid = all(
        (
            bool(f5_spec),
            len(propositions) == 1,
            semantic_tokens == f5_spec.get("semantic_tokens"),
            artifact.get("owner_scope") == f5_spec.get("owner_scope"),
            F5_NEUTRAL_ARTIFACT_TEMPLATES.get(tuple(semantic_tokens))
            == (propositions[0].get("text") if propositions else None),
        )
    )
    forbidden_decision_tokens = {
        str(predicate["value"])
        for collection in ("must", "must_not")
        for predicate in scenario["oracle"].get(collection, [])
    }
    proposition_text = " ".join(
        str(item.get("text", "")).lower().replace("_", " ") for item in propositions
    )
    contains_forbidden_decision = any(
        token.lower().replace("_", " ") in proposition_text
        or token in semantic_tokens
        for token in forbidden_decision_tokens
    )
    artifact_pure = template_valid and all(
        item.get("kind") == "neutral_distinction"
        and isinstance(item.get("semantic_tokens"), list)
        and bool(item["semantic_tokens"])
        and not item.get("contains_entity")
        and not item.get("contains_action")
        and not item.get("contains_hidden_fact")
        for item in propositions
    ) and not contains_forbidden_decision
    review_bound = all(
        (
            purity_review.get("reviewed_artifact_hash") == sha256_digest(artifact),
            purity_review.get("semantic_tokens") == semantic_tokens,
            purity_review.get("disposition") == "neutral_owner_local",
            isinstance(purity_review.get("reviewer_id"), str),
            purity_review.get("reviewer_id")
            not in {
                scenario["identity_version"]["contract_author"],
                scenario["identity_version"]["independent_validator"],
            },
        )
    )
    audit_bound = bool(
        audit
        and accesses
        and accesses[0].get("resource_hash")
        and audit.get("audited_resource_ref") == "trace:ordinary:resource_hash"
        and audit.get("audited_resource_hash") == accesses[0].get("resource_hash")
        and bool(audit.get("missing_distinction"))
        and audit.get("missing_distinction_tokens") == semantic_tokens
        and audit.get("scenario_ref") == _scenario_ref(scenario)
        and audit.get("owner_scope") == f5_spec.get("owner_scope")
        and audit.get("missing_distinction") == f5_spec.get("missing_distinction")
        and audit.get("oracle_predicate_ids") == f5_spec.get("oracle_predicate_ids")
        and bool(set(audit.get("oracle_predicate_ids", [])))
        and set(audit.get("oracle_predicate_ids", [])).issubset(predicate_ids)
        and isinstance(audit.get("auditor"), str)
        and bool(audit.get("auditor"))
        and audit.get("auditor")
        not in {
            scenario["identity_version"]["contract_author"],
            scenario["identity_version"]["independent_validator"],
            purity_review.get("reviewer_id"),
        }
        and audit.get("audit_seal")
        == sha256_digest({key: value for key, value in audit.items() if key != "audit_seal"})
    )
    target_deltas = {
        delta
        for run in (target_arm or {}).get("stability_runs", [])
        for event in run["trace"]
        if event["event_type"] == "INTERVENTION_APPLIED"
        for delta in event["payload"].get("delta_manifest", [])
    }
    artifact_trace_bound = artifact.get("artifact_id") in target_deltas
    target_content_hashes = {
        event["payload"].get("injected_content_hash")
        for run in (target_arm or {}).get("stability_runs", [])
        for event in run["trace"]
        if event["event_type"] == "INTERVENTION_APPLIED"
    }
    artifact_content_bound = target_content_hashes == {sha256_digest(artifact)}
    ordinary_delivery_signature = _logical_delivery_signature(trace)
    correct_owner_route_delivered = _delivery_signature_matches_route(
        ordinary_delivery_signature,
        f5_spec.get("owner_scope"),
        "normal_execution",
    )
    intervention_access_held = _intervention_access_is_held_constant(
        interventions, ordinary_delivery_signature
    )
    if audit_bound and artifact_pure and review_bound and correct_owner_route_delivered and intervention_access_held and intervention_activation_held and artifact_trace_bound and artifact_content_bound and selective_repair:
        return _attribution("F5", "audited neutral owner-local knowledge selectively repairs against placebo", result_packet), {
            "intervention_runs": interventions,
            "local_content_audit": copy.deepcopy(audit),
            "neutral_artifact": copy.deepcopy(artifact),
            "purity_review": copy.deepcopy(purity_review),
            "audited_resource_hash": accesses[0]["resource_hash"],
            "artifact_hash": sha256_digest(artifact),
        }

    boundary = packet.get("boundary_audit", {})
    capsule = packet.get("state_capsule", {})
    boundary_contract = packet.get("boundary_contract", {})
    capsule_spec = F6_CAPSULE_SPECS.get(_scenario_ref(scenario), {})
    owner_tests = packet.get("owner_tests", [])
    owners_adequate = len(owner_tests) == 2
    owner_task_ids = {item.get("owner_task_id") for item in owner_tests}
    owner_roles = {item.get("owner") for item in owner_tests}
    if len(owner_task_ids) != 2 or owner_roles != {"upstream", "downstream_with_state"}:
        owners_adequate = False
    for item in owner_tests:
        selected_ids = set(item.get("predicate_ids", []))
        if not selected_ids or not selected_ids.issubset(predicate_ids) or not item.get("visible_state_refs"):
            owners_adequate = False
            continue
        expected_visible_refs = set(capsule_spec.get("assertion_ids", []))
        if item.get("owner") == "downstream_with_state":
            expected_visible_refs.add(capsule_spec.get("capsule_id"))
        if set(item.get("visible_state_refs", [])) != expected_visible_refs:
            owners_adequate = False
        owner_scenario = copy.deepcopy(scenario)
        for collection in ("must", "must_not", "may"):
            owner_scenario["oracle"][collection] = [
                predicate
                for predicate in scenario["oracle"].get(collection, [])
                if predicate["predicate_id"] in selected_ids
            ]
        candidate = _resolve_evidence_candidate(item["candidate_ref"], conditions, evidence)
        owner_judgments = [
            judge_candidate(owner_scenario, candidate, judge) for judge in judges
        ]
        if not _all_judges_accept(owner_judgments):
            owners_adequate = False

    state_field_names = capsule_spec.get("state_field_names", [])
    capsule_safe = all(
        (
            bool(capsule),
            bool(capsule_spec),
            boundary_contract.get("contract_id") == capsule_spec.get("contract_id"),
            boundary_contract.get("state_field_names") == state_field_names,
            set(boundary_contract.get("allowed_capsule_object_keys", []))
            == F6_CAPSULE_OBJECT_KEYS,
            boundary_contract.get("allowed_value_vocabulary")
            == ["present", "absent", "unknown"],
            set(capsule) == F6_CAPSULE_OBJECT_KEYS,
            capsule.get("schema") == state_field_names,
            len(set(state_field_names)) == len(state_field_names),
            isinstance(capsule.get("values"), list),
            capsule.get("values") == capsule_spec.get("values"),
            capsule.get("allowed_keys_only") is True,
            capsule.get("contains_recommendation") is False,
            capsule.get("contains_new_fact") is False,
        )
    )
    capsule_trace_bound = target_deltas == {capsule_spec.get("capsule_id")}
    boundary_package = {
        "boundary_audit": boundary,
        "boundary_contract": boundary_contract,
        "state_capsule": capsule,
    }
    capsule_content_bound = target_content_hashes == {sha256_digest(boundary_package)}
    required_assertions = boundary.get("required_assertion_ids", [])
    assertions_bound = bool(required_assertions) and required_assertions == capsule_spec.get(
        "assertion_ids"
    )
    upstream_material = boundary.get("upstream_artifact") or {}
    downstream_material = boundary.get("downstream_artifact") or {}
    boundary_hashes_valid = all(
        (
            isinstance(upstream_material, dict),
            isinstance(downstream_material, dict),
            boundary.get("upstream_artifact_hash") == sha256_digest(upstream_material),
            boundary.get("downstream_artifact_hash") == sha256_digest(downstream_material),
            set(upstream_material.get("assertion_ids", [])) == set(required_assertions),
            not set(downstream_material.get("assertion_ids", [])).intersection(required_assertions),
        )
    )
    boundary_events = [
        event["payload"] for event in trace if event["event_type"] == "BOUNDARY_TRANSFER"
    ]
    expected_boundary_event = {
        "boundary_id": boundary.get("boundary_id"),
        "source_owner": boundary.get("source_owner"),
        "destination_owner": boundary.get("destination_owner"),
        "upstream_artifact_hash_ref": boundary.get("upstream_artifact_hash"),
        "downstream_received_artifact_hash_ref": boundary.get("downstream_artifact_hash"),
        "critical_assertion_ids": boundary.get("required_assertion_ids"),
        "transfer_status": boundary.get("transfer_status"),
    }
    boundary_event_bound = boundary_events == [expected_boundary_event]
    f6_delivery_signature = _logical_delivery_signature(trace)
    f6_owner_route_delivered = _delivery_signature_matches_route(
        f6_delivery_signature,
        capsule_spec.get("owner_scope"),
        "normal_execution",
    )
    f6_access_held = _intervention_access_is_held_constant(
        interventions, f6_delivery_signature
    )
    if boundary.get("transfer_status") == "lost" and boundary_hashes_valid and boundary_event_bound and f6_owner_route_delivered and f6_access_held and intervention_activation_held and assertions_bound and owners_adequate and capsule_safe and capsule_trace_bound and capsule_content_bound and selective_repair:
        return _attribution("F6", "answer-free boundary state restoration selectively repairs composition", result_packet), {
            "intervention_runs": interventions,
            "boundary_audit": copy.deepcopy(boundary),
            "boundary_contract": copy.deepcopy(boundary_contract),
            "state_capsule": copy.deepcopy(capsule),
            "capsule_hash": sha256_digest(capsule),
        }

    dependency = packet.get("external_dependency", {})
    dependency_predicates = set(dependency.get("material_predicate_ids", []))
    dependency_records = {
        item.get("record_id"): item for item in packet.get("dependency_records", [])
    }
    dependency_record = dependency_records.get(dependency.get("evidence_ref")) or {}
    ledger_propositions = {
        item.get("proposition") for item in scenario.get("evidence_state_ledger", [])
    }
    dependency_grounded = all(
        (
            bool(dependency.get("dependency_id")),
            bool(dependency.get("authority")),
            dependency.get("availability") == "outside_executor_scope",
            bool(dependency_predicates),
            dependency_predicates.issubset(predicate_ids),
            isinstance(dependency_record, dict),
            dependency_record.get("authority") == dependency.get("authority"),
            dependency_record.get("scope_status") == "outside_executor_scope",
            dependency_record.get("proposition") in ledger_propositions,
        )
    )
    if dependency_grounded:
        return _attribution("F10", "referenced material authority is outside executor scope", result_packet), {"external_dependency": dependency}

    return _attribution("F12", "available sealed evidence does not discriminate mechanism", result_packet), {"intervention_runs": interventions}


def _authorship_identities(condition: dict, packet: dict) -> dict:
    intervention_authors = [
        arm.get(
            "author_id",
            f"fixture-intervention-author:{condition['condition_id']}:{arm.get('arm', index)}",
        )
        for index, arm in enumerate(packet.get("intervention_runs", []), start=1)
    ]
    proposed_fix_authors = [
        identity
        for identity in (
            (packet.get("local_content_audit") or {}).get("auditor"),
            (packet.get("purity_review") or {}).get("reviewer_id"),
            *intervention_authors,
        )
        if identity
    ]
    return {
        "candidate_author": condition.get(
            "candidate_author", f"fixture-candidate-author:{condition['condition_id']}"
        ),
        "intervention_authors": intervention_authors,
        "proposed_fix_authors": sorted(set(proposed_fix_authors)),
    }


def evaluate_and_seal(cases: dict, evidence: dict | None = None) -> dict:
    """Evaluate visible fixtures without reading the separate planting key."""

    evidence = evidence or load_json(Path(__file__).resolve().parent / "fixtures" / "evidence-packets.json")
    scenarios = {_scenario_ref(item): item for item in cases["scenarios"]}
    scenario_results: list[dict] = []
    for reference, scenario in scenarios.items():
        errors = validate_scenario(scenario)
        role_attestations = scenario["external_provenance"].get("role_attestations", {})
        validity = validity_disposition(scenario) if not errors else {
            "disposition": "REJECT",
            "recorded_disposition": scenario.get("validity_docket", {}).get("disposition"),
            "reasons": errors,
            "preserve_artifact": True,
        }
        scenario_results.append(
            {
                "scenario_ref": reference,
                "lane": scenario["lane"],
                "provenance_root_id": scenario["identity_version"]["provenance_root_id"],
                "contract_author": scenario["identity_version"]["contract_author"],
                "independent_validator": scenario["identity_version"]["independent_validator"],
                "scenario_role_identities": {
                    "contract_author": scenario["identity_version"]["contract_author"],
                    "independent_validator": scenario["identity_version"]["independent_validator"],
                    "source_curator": (role_attestations.get("source_curator") or {}).get("identity"),
                    "scenario_editor": (role_attestations.get("scenario_editor") or {}).get("identity"),
                    "oracle_author": (role_attestations.get("oracle_author") or {}).get("identity"),
                    "post_lock_mapper": scenario.get("post_lock_mapping", {}).get("mapped_by"),
                },
                "scenario_hash": sha256_digest(scenario),
                "oracle_hash": sha256_digest(scenario["oracle"]),
                "validation_errors": errors,
                "validity": validity,
            }
        )

    conditions = {item["condition_id"]: item for item in cases["conditions"]}
    evidence_packets = {item["condition_id"]: item for item in evidence["packets"]}
    condition_results: list[dict] = []
    for condition in cases["conditions"]:
        scenario = scenarios[condition["scenario_ref"]]
        validity = validity_disposition(scenario)
        evidence_packet = evidence_packets[condition["condition_id"]]

        if validity["disposition"] == "REJECT":
            attribution_result = _attribution(
                "F0",
                "scenario validity preempts execution and system attribution",
                {"failure_established": True, "behavioral_tags": []},
            )
            judgments: list[dict] = []
            trace: list[dict] = []
            trace_errors: list[str] = []
            counterfactual_evidence: dict = {}
            execution_status = "rejected_before_execution"
            telemetry_status = "not_applicable"
        else:
            judgments = [
                judge_candidate(scenario, condition["candidate"], judge)
                for judge in cases["fixture_judges"]
            ]
            trace = _build_evidence_trace(
                scenario,
                condition,
                evidence_packet["ordinary_trace_profile"],
                evidence,
                cases["target"],
                boundary_audit=evidence_packet.get("boundary_audit"),
                requested_route=_packet_expected_route(scenario, evidence_packet),
            )
            trace_errors = validate_trace(trace)
            telemetry_status = trace[-1]["payload"]["telemetry_completeness_status"]
            attribution_result, counterfactual_evidence = _classify_from_evidence(
                scenario,
                condition,
                evidence_packet,
                conditions,
                evidence,
                judgments,
                trace,
                trace_errors,
                cases["fixture_judges"],
                cases["target"],
            )
            execution_status = "fixture_run_recorded"

        condition_results.append(
            {
                "condition_id": condition["condition_id"],
                "scenario_ref": condition["scenario_ref"],
                "candidate_hash": sha256_digest(condition["candidate"]),
                "candidate_output": condition["candidate"]["output"],
                "evidence_packet_hash": sha256_digest(evidence_packet),
                "authorship_identities": _authorship_identities(condition, evidence_packet),
                "execution_status": execution_status,
                "judgments": judgments,
                "attribution": attribution_result,
                "trace": trace,
                "trace_errors": trace_errors,
                "trace_telemetry_status": telemetry_status,
                "counterfactual_evidence": counterfactual_evidence,
            }
        )

    result_by_condition = {item["condition_id"]: item for item in condition_results}
    pair_results: list[dict] = []
    for pair in cases.get("pairs", []):
        left_result = result_by_condition[pair["left_condition_id"]]
        right_result = result_by_condition[pair["right_condition_id"]]
        left_judgment = {"overall": "acceptable" if _all_judges_accept(left_result["judgments"]) else "not assessable"}
        right_judgment = {"overall": "acceptable" if _all_judges_accept(right_result["judgments"]) else "not assessable"}
        relation_result = evaluate_pair(
            left_judgment,
            right_judgment,
            conditions[pair["left_condition_id"]]["candidate"],
            conditions[pair["right_condition_id"]]["candidate"],
            pair,
        )
        pair_results.append({"pair_id": pair["pair_id"], **relation_result})

    f11_records = evidence.get("f11_evidence_context", {}).get("records", {})
    f11_context_material = {
        "scenario_results": scenario_results,
        "condition_results": condition_results,
        "pair_results": pair_results,
        "records": f11_records,
    }
    f11_evidence_context = {
        **f11_context_material,
        "evaluation_evidence_seal": sha256_digest(f11_context_material),
    }
    f11_results = [
        {
            "dossier_id": dossier["dossier_id"],
            **evaluate_f11_gate(dossier, f11_evidence_context),
        }
        for dossier in cases.get("f11_dossiers", [])
    ]

    unsealed = {
        "pilot_id": cases["pilot_id"],
        "fixture_schema_version": cases["fixture_schema_version"],
        "scenario_results": scenario_results,
        "condition_results": condition_results,
        "pair_results": pair_results,
        "f11_results": f11_results,
        "f11_evidence_context": f11_evidence_context,
    }
    return {**unsealed, "evaluation_seal": sha256_digest(unsealed)}


def compare_and_report(cases: dict, sealed_results: dict, planting_key: dict) -> dict:
    expectations = {
        item["condition_id"]: item for item in planting_key["condition_expectations"]
    }
    detected: list[str] = []
    expectation_matches: list[str] = []
    missed: list[dict] = []
    taxonomy: dict[str, list[str]] = {}
    unresolved: list[str] = []

    for result in sealed_results["condition_results"]:
        condition_id = result["condition_id"]
        expectation = expectations[condition_id]
        actual_mechanism = result["attribution"]["mechanism"]
        actual_tags = sorted(result["attribution"]["behavioral_tags"])
        expected_tags = sorted(expectation["expected_behavioral_tags"])
        if (
            actual_mechanism == expectation["expected_mechanism"]
            and actual_tags == expected_tags
        ):
            expectation_matches.append(condition_id)
            if expectation["expected_mechanism"].startswith("F"):
                detected.append(condition_id)
        else:
            missed.append(
                {
                    "condition_id": condition_id,
                    "expected_mechanism": expectation["expected_mechanism"],
                    "actual_mechanism": actual_mechanism,
                    "expected_behavioral_tags": expected_tags,
                    "actual_behavioral_tags": actual_tags,
                }
            )
        if actual_mechanism.startswith("F"):
            taxonomy.setdefault(actual_mechanism, []).append(condition_id)
        for tag in actual_tags:
            taxonomy.setdefault(tag, []).append(condition_id)
        if actual_mechanism == "F12":
            unresolved.append(condition_id)

    purposes = {
        item["scenario_ref"]: item for item in planting_key["scenario_purposes"]
    }
    scenario_versions = []
    for scenario in cases["scenarios"]:
        reference = _scenario_ref(scenario)
        purpose = purposes[reference]
        scenario_versions.append(
            {
                "scenario_ref": reference,
                "lane": scenario["lane"],
                "methodological_purpose": purpose["methodological_purpose"],
                "truth_type": purpose["truth_type"],
                "modifiers": purpose["modifiers"],
                "planted_defect": purpose["planted_defect"],
            }
        )

    validity_counts = Counter(
        item["validity"]["disposition"] for item in sealed_results["scenario_results"]
    )
    rejected = [
        item["scenario_ref"]
        for item in sealed_results["scenario_results"]
        if item["validity"]["disposition"] == "REJECT"
    ]
    complete_traces = [
        item["condition_id"]
        for item in sealed_results["condition_results"]
        if item["trace_telemetry_status"] == "complete" and not item["trace_errors"]
    ]
    incomplete_traces = [
        item["condition_id"]
        for item in sealed_results["condition_results"]
        if item["trace_telemetry_status"] == "incomplete" or item["trace_errors"]
    ]

    clean = [
        scenario for scenario in cases["scenarios"] if scenario["lane"] == "clean_room_independence"
    ]
    false_f11 = sealed_results["f11_results"]
    scenario_by_ref = {_scenario_ref(item): item for item in cases["scenarios"]}
    scenario_result_by_ref = {
        item["scenario_ref"]: item for item in sealed_results["scenario_results"]
    }
    confound_by_mechanism = {
        "F0": "system attribution is preempted by scenario invalidity",
        "F1": "executor mechanisms remain unassessable under the defective oracle",
        "F2": "within-configuration execution variance remains the controlling confound",
        "F3": "task delivery and activation are not further separable beyond the sealed receipt",
        "F4": "no stronger confound survives the selective exact-route repair and irrelevant-route control",
        "F5": "no stronger confound survives the scenario-bound neutral repair and placebo control",
        "F6": "no stronger confound survives adequate-owner tests and state-only restoration",
        "F10": "the dependency remains outside executor scope rather than an owner-local defect",
        "F12": "available mechanism evidence remains insufficient to discriminate the surviving candidates",
        "NO_FAILURE": "no confirmed failure observation",
    }
    finding_ledger = []
    for result in sealed_results["condition_results"]:
        scenario = scenario_by_ref[result["scenario_ref"]]
        scenario_result = scenario_result_by_ref[result["scenario_ref"]]
        identity = scenario["identity_version"]
        activation_route_events = [
            event
            for event in result["trace"]
            if event.get("event_type") in {"SKILL_ACTIVATION", "KNOWLEDGE_REQUEST", "KNOWLEDGE_ACCESS"}
        ]
        violated = sorted(
            {
                criterion["predicate_id"]
                for judgment in result["judgments"]
                for criterion in judgment.get("criteria", [])
                if criterion.get("result") == "violated"
            }
        )
        run_id = result["trace"][0]["run_id"] if result["trace"] else None
        execution_fingerprint = sha256_digest(
            result["trace"][0]["payload"]
            if result["trace"]
            else {
                "scenario_ref": result["scenario_ref"],
                "condition_id": result["condition_id"],
                "execution_status": result["execution_status"],
            }
        )
        mechanism = result["attribution"]["mechanism"]
        record = {
            **copy.deepcopy(result),
            "observation_id": f"OBS-{result['condition_id']}",
            "scenario_contract_rubric_versions": {
                "scenario_version": identity["scenario_version"],
                "contract_version": identity["oracle_version"],
                "rubric_version": identity["oracle_version"],
            },
            "run_id": run_id,
            "condition": "with_skill" if result["trace"] else "rejected_before_execution",
            "execution_fingerprint": execution_fingerprint,
            "activation_route_resource_evidence": activation_route_events,
            "violated_invariant_or_relation": violated,
            "exact_output_evidence": {
                "output": result["candidate_output"],
                "judgment_criteria": [
                    criterion
                    for judgment in result["judgments"]
                    for criterion in judgment.get("criteria", [])
                ],
            },
            "decision_consequence": scenario["decision_record"]["objective_material_consequence"],
            "validity_status": {
                "scenario": scenario_result["validity"],
                "oracle_validation_errors": scenario_result["validation_errors"],
                "judge_overalls": [item["overall"] for item in result["judgments"]],
            },
            "behavioral_tags": result["attribution"]["behavioral_tags"],
            "ranked_mechanism_candidates": [
                {
                    "rank": 1,
                    "mechanism": mechanism,
                    "reason": result["attribution"]["reason"],
                }
            ],
            "positive_evidence": {
                "attribution_reason": result["attribution"]["reason"],
                "counterfactual_evidence_hash": sha256_digest(result["counterfactual_evidence"]),
            },
            "strongest_surviving_confound": confound_by_mechanism.get(
                mechanism, "no protocol-owned confound description"
            ),
            "counterfactual_performed_and_result": {
                "performed": bool(result["counterfactual_evidence"]),
                "evidence": copy.deepcopy(result["counterfactual_evidence"]),
            },
            "observability_limitation": {
                "telemetry_status": result["trace_telemetry_status"],
                "trace_errors": result["trace_errors"],
                "chain_of_thought_accessed": False,
            },
            "current_disposition": mechanism,
            "behavior_confidence": result["attribution"]["behavior_confidence"],
            "mechanism_confidence": result["attribution"]["mechanism_confidence"],
            "recurrence_signature_and_lineage": {
                "provenance_root_id": identity["provenance_root_id"],
                "scenario_hash": scenario_result["scenario_hash"],
                "ecological_recurrence_claim": False,
            },
            "next_action": "retain unresolved"
            if mechanism == "F12"
            else "retain as methodology diagnostic only",
        }
        record["record_seal"] = sha256_digest(record)
        finding_ledger.append(record)
    finding_ledger_seal = sha256_digest(finding_ledger)
    ab_disposition_patterns = []
    for record in finding_ledger:
        repeat_records = record.get("counterfactual_evidence", {}).get("repeat_arms", [])
        if not repeat_records:
            continue
        dispositions_by_condition: dict[str, list[str]] = {}
        for repeat in repeat_records:
            dispositions_by_condition.setdefault(repeat["condition"], []).append(
                "acceptable"
                if _all_judges_accept(repeat.get("judgments", []))
                else "unacceptable"
            )
        ab_disposition_patterns.append(
            {
                "condition_id": record["condition_id"],
                "decision_family": record["scenario_ref"],
                "without_skill": dispositions_by_condition.get("without_skill", []),
                "with_skill": dispositions_by_condition.get("with_skill", []),
                "pattern": "within-arm-mixed"
                if any(len(set(values)) > 1 for values in dispositions_by_condition.values())
                else "stable",
            }
        )
    return {
        "report_type": "deterministic_evaluation_plumbing_diagnostic",
        "protocol_path": "evals/pressure-discovery/protocol-v1.md",
        "protocol_commit": cases["protocol_commit"],
        "target": cases["target"],
        "evaluation_seal": sealed_results["evaluation_seal"],
        "f11_evidence_context": sealed_results["f11_evidence_context"],
        "planting_key_loaded_after_evaluation_seal": sealed_results.get("evaluation_seal")
        == sha256_digest(
            {
                key: value
                for key, value in sealed_results.items()
                if key != "evaluation_seal"
            }
        ),
        "scenarios_defined": len(cases["scenarios"]),
        "lanes": dict(Counter(item["lane"] for item in cases["scenarios"])),
        "scenario_versions": scenario_versions,
        "scenarios_rejected": rejected,
        "validity_outcomes": dict(validity_counts),
        "planted_methodology_faults_detected": detected,
        "condition_expectation_matches": expectation_matches,
        "planted_methodology_faults_missed": missed,
        "taxonomy_recovery": {key: sorted(set(value)) for key, value in sorted(taxonomy.items())},
        "pair_relation_checks": sealed_results["pair_results"],
        "finding_ledger": finding_ledger,
        "finding_ledger_seal": finding_ledger_seal,
        "ab_disposition_patterns": ab_disposition_patterns,
        "run_evidence": {
            "complete_condition_ids": complete_traces,
            "incomplete_condition_ids": incomplete_traces,
            "rejected_before_execution": [
                item["condition_id"]
                for item in sealed_results["condition_results"]
                if item["execution_status"] == "rejected_before_execution"
            ],
        },
        "false_f11": {
            "all_rejected": all(not item["research_reopening"] for item in false_f11),
            "dossiers": false_f11,
        },
        "unresolved_attribution": unresolved,
        "clean_room_independence": {
            "status": "fixture_independence_checks_passed",
            "independent_provenance_roots": sorted(
                {item["identity_version"]["provenance_root_id"] for item in clean}
            ),
            "mapping_statuses": sorted(
                {item["post_lock_mapping"]["status"] for item in clean}
            ),
            "framework_access_attestations": sorted(
                {
                    item["external_provenance"]["framework_access_attestation"]
                    for item in clean
                }
            ),
            "prelock_role_identities": sorted(
                {
                    attestation["identity"]
                    for item in clean
                    for attestation in item["external_provenance"]["role_attestations"].values()
                }
            ),
            "source_snapshot_refs": sorted(
                {
                    item["external_provenance"]["raw_source_snapshot_ref"]
                    for item in clean
                }
            ),
            "live_human_judgment_executed": False,
        },
        "implementation_limitations": [
            "Candidate semantics and judge records are deterministic fixtures, not live model or human judgments.",
            "Clean-room checks validate recorded provenance and access attestations; they do not establish population recurrence.",
            "The run exercises evaluation plumbing only and authorizes no Marketing Practitioner capability conclusion.",
        ],
    }


def run_pilot(base_dir: Path) -> dict:
    cases = load_json(base_dir / "fixtures" / "pilot-cases.json")
    sealed_results = evaluate_and_seal(cases)
    planting_key = load_json(base_dir / "fixtures" / "planting-key.json")
    return compare_and_report(cases, sealed_results, planting_key)


def render_markdown(report: dict) -> str:
    lines = [
        "# Pressure Discovery Methodology-Validation Pilot Report",
        "",
        "This deterministic run validates evaluation plumbing only. It does not evaluate Marketing Practitioner capability or prevalence.",
        "",
        "## Frozen input",
        "",
        f"- Protocol: `{report['protocol_path']}`",
        f"- Protocol commit: `{report['protocol_commit']}`",
        f"- Target: Marketing Practitioner v{report['target']['version']} at `{report['target']['commit']}`",
        "",
        "## Scenario flow",
        "",
        f"- Visible scenario versions: {report['scenarios_defined']}",
        f"- Diagnostic injection lane: {report['lanes']['diagnostic_injection']}",
        f"- Clean-room independence lane: {report['lanes']['clean_room_independence']}",
        f"- Rejected and preserved: {', '.join(report['scenarios_rejected'])}",
        "",
        "## Scenario versions",
        "",
    ]
    for item in report["scenario_versions"]:
        modifiers = "+".join(item["modifiers"]) if item["modifiers"] else "none"
        planted = item["planted_defect"] if item["planted_defect"] else "none"
        lines.append(
            f"- `{item['scenario_ref']}` — {item['lane']}; {item['methodological_purpose']}; "
            f"truth {item['truth_type']}; modifiers {modifiers}; planted diagnostic {planted}."
        )
    lines.extend(
        [
            "",
            "## Validity",
            "",
            "- Outcomes: " + ", ".join(
                f"{key}={value}" for key, value in sorted(report["validity_outcomes"].items())
            ),
            "- Rejected scenarios remain preserved as artifacts.",
            "",
            "## Planted methodology recovery",
            "",
            f"- Detected condition packets: {', '.join(report['planted_methodology_faults_detected'])}",
            "- Missed condition packets: "
            + (canonical_json(report["planted_methodology_faults_missed"]) if report["planted_methodology_faults_missed"] else "none"),
            "",
            "## Taxonomy recovery",
            "",
        ]
    )
    for code, condition_ids in report["taxonomy_recovery"].items():
        lines.append(f"- {code}: {', '.join(condition_ids)}")
    lines.extend(["", "## Pair relations", ""])
    for pair in report["pair_relation_checks"]:
        lines.append(f"- `{pair['pair_id']}`: passed={str(pair['passed']).lower()}; {pair['reason']}.")
    lines.extend(
        [
            "",
            "## Run evidence",
            "",
            "- Complete traces: " + ", ".join(report["run_evidence"]["complete_condition_ids"]),
            "- Intentionally incomplete traces: " + ", ".join(report["run_evidence"]["incomplete_condition_ids"]),
            "- Rejected before execution: " + ", ".join(report["run_evidence"]["rejected_before_execution"]),
            "",
            "## Finding ledger",
            "",
            f"- Full sealed condition records: {len(report['finding_ledger'])}.",
            "- The JSON artifact retains executed outputs, judgments, traces, A/B repeats, counterfactual interventions, strongest confounds, and observation records.",
            f"- Explicit A/B disposition-pattern records: {len(report['ab_disposition_patterns'])}.",
            "",
            "## Architecture-reopening gate",
            "",
            f"- All apparent cases rejected: {str(report['false_f11']['all_rejected']).lower()}.",
            "- Gate output authorizes research only and generated no architecture.",
            "",
            "## Unresolved attribution",
            "",
            "- Retained condition packets: " + ", ".join(report["unresolved_attribution"]),
            "",
            "## Clean-room independence",
            "",
            f"- Status: {report['clean_room_independence']['status']}",
            "- Provenance roots: " + ", ".join(report["clean_room_independence"]["independent_provenance_roots"]),
            "- Post-lock mapping statuses: " + ", ".join(report["clean_room_independence"]["mapping_statuses"]),
            "- Distinct pre-lock roles: " + ", ".join(report["clean_room_independence"]["prelock_role_identities"]),
            "- Bound source snapshots: " + ", ".join(report["clean_room_independence"]["source_snapshot_refs"]),
            "- Live human judgment was not executed; fixture judgment plumbing only.",
            "",
            "## Implementation limitations",
            "",
        ]
    )
    lines.extend(f"- {item}" for item in report["implementation_limitations"])
    lines.append("")
    return "\n".join(lines)


def validate_pilot(base_dir: Path) -> list[str]:
    errors: list[str] = []
    cases = load_json(base_dir / "fixtures" / "pilot-cases.json")
    evidence = load_json(base_dir / "fixtures" / "evidence-packets.json")
    sources = load_json(base_dir / "fixtures" / "source-snapshots.json")

    if len(cases.get("scenarios", [])) != 14:
        errors.append("pilot must contain exactly 14 visible scenario versions")
    lanes = Counter(item.get("lane") for item in cases.get("scenarios", []))
    if dict(lanes) != {"diagnostic_injection": 12, "clean_room_independence": 2}:
        errors.append("pilot lane split must be 12 diagnostic and 2 clean-room")
    for scenario in cases.get("scenarios", []):
        reference = _scenario_ref(scenario)
        errors.extend(f"{reference}: {error}" for error in validate_scenario(scenario))

    snapshots = {item.get("snapshot_id"): item for item in sources.get("snapshots", [])}
    for snapshot in sources.get("snapshots", []):
        snapshot_envelope = {key: value for key, value in snapshot.items() if key != "snapshot_hash"}
        if snapshot.get("snapshot_hash") != sha256_digest(snapshot_envelope):
            errors.append(f"source snapshot hash mismatch: {snapshot.get('snapshot_id')}")
        if "decision" in snapshot.get("snapshot_material", {}):
            errors.append(f"historical decision leaked into executor-visible snapshot: {snapshot.get('snapshot_id')}")
        if not snapshot.get("executor_visible_material_ref"):
            errors.append(f"executor-visible material reference missing: {snapshot.get('snapshot_id')}")
        if any(
            reference.get("executor_visibility") != "sealed_evaluator_only"
            for reference in snapshot.get("source_references", [])
        ):
            errors.append(f"raw source reference is not evaluator-sealed: {snapshot.get('snapshot_id')}")

    for scenario in cases.get("scenarios", []):
        if scenario.get("lane") != "clean_room_independence":
            continue
        provenance = scenario["external_provenance"]
        snapshot = snapshots.get(provenance["raw_source_snapshot_ref"])
        if snapshot is None:
            errors.append(f"clean-room snapshot is missing: {provenance['raw_source_snapshot_ref']}")
            continue
        if provenance.get("raw_source_snapshot_hash") != snapshot.get("snapshot_hash"):
            errors.append(
                f"clean-room snapshot hash binding mismatch: {provenance['raw_source_snapshot_ref']}"
            )
        expected_bindings = {
            "provenance_root_id": scenario["identity_version"]["provenance_root_id"],
            "source_class": provenance["source_class"],
        }
        for field, expected in expected_bindings.items():
            if snapshot.get(field) != expected:
                errors.append(f"clean-room snapshot binding mismatch for {field}: {provenance['raw_source_snapshot_ref']}")
        if snapshot.get("snapshot_material", {}).get("decision_time_cutoff") != provenance["decision_time_cutoff"]:
            errors.append(f"clean-room snapshot cutoff mismatch: {provenance['raw_source_snapshot_ref']}")
        expected_visible_ref = [
            f"executor snapshot material {snapshot.get('executor_visible_material_ref')}"
        ]
        if scenario["user_visible_package"].get("tools_external_evidence") != expected_visible_ref:
            errors.append(
                f"clean-room executor material binding mismatch: {provenance['raw_source_snapshot_ref']}"
            )

    sealed = evaluate_and_seal(cases, evidence)
    for result in sealed["condition_results"]:
        if result["trace_telemetry_status"] == "complete" and result["trace_errors"]:
            errors.append(
                f"complete trace has validation errors: {result['condition_id']} "
                + "; ".join(result["trace_errors"])
            )

    planting = load_json(base_dir / "fixtures" / "planting-key.json")
    label_scan_cases = copy.deepcopy(cases)
    label_scan_sources = copy.deepcopy(sources)
    for scenario in label_scan_cases.get("scenarios", []):
        scenario.get("external_provenance", {})["source_class"] = "source-class"
    for snapshot in label_scan_sources.get("snapshots", []):
        snapshot["source_class"] = "source-class"
    visible_strings = list(
        _string_values(
            {"cases": label_scan_cases, "evidence": evidence, "sources": label_scan_sources}
        )
    )
    for label in planting["forbidden_visible_labels"]:
        token_pattern = re.compile(
            rf"(?<![A-Za-z0-9]){re.escape(label)}(?![A-Za-z0-9])", re.IGNORECASE
        )
        if any(token_pattern.search(value) for value in visible_strings):
            errors.append(f"planted label leaked into evaluator-visible fixtures: {label}")

    fresh_report = compare_and_report(cases, sealed, planting)
    json_report_path = base_dir / "results" / "pilot-report.json"
    markdown_report_path = base_dir / "results" / "pilot-report.md"
    if not json_report_path.is_file():
        errors.append("persisted JSON report is missing")
    else:
        try:
            if load_json(json_report_path) != fresh_report:
                errors.append("persisted JSON report is stale")
        except (json.JSONDecodeError, UnicodeDecodeError):
            errors.append("persisted JSON report is invalid")
    if not markdown_report_path.is_file():
        errors.append("persisted Markdown report is missing")
    else:
        try:
            persisted_markdown = markdown_report_path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            errors.append("persisted Markdown report is invalid UTF-8")
        else:
            if persisted_markdown != render_markdown(fresh_report):
                errors.append("persisted Markdown report is stale")
    return errors


def _write_report_files(base_dir: Path, report: dict) -> None:
    output_dir = base_dir / "results"
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "pilot-report.json").write_text(
        json.dumps(report, ensure_ascii=False, sort_keys=True, indent=2) + "\n",
        encoding="utf-8",
    )
    (output_dir / "pilot-report.md").write_text(
        render_markdown(report),
        encoding="utf-8",
    )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("validate", "run"))
    args = parser.parse_args(argv)
    base_dir = Path(__file__).resolve().parent

    if args.command == "validate":
        errors = validate_pilot(base_dir)
        if errors:
            for error in errors:
                print("FAIL\t" + error)
            return 1
        cases = load_json(base_dir / "fixtures" / "pilot-cases.json")
        print(
            f"PASS\t{len(cases['scenarios'])} visible scenarios / "
            f"{len(cases['conditions'])} condition packets / "
            f"{len(cases['f11_dossiers'])} architecture-gate dossiers"
        )
        return 0

    report = run_pilot(base_dir)
    _write_report_files(base_dir, report)
    print(
        f"PASS\t{report['scenarios_defined']} visible scenarios / "
        f"{len(report['planted_methodology_faults_detected'])} planted fault packets recovered / "
        f"{len(report['planted_methodology_faults_missed'])} missed"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

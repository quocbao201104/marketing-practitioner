from __future__ import annotations

import copy
import collections
import importlib.util
import json
import re
import shutil
import tempfile
import unittest
from unittest import mock
from pathlib import Path


PILOT_ROOT = Path(__file__).resolve().parents[1]
PILOT_PATH = PILOT_ROOT / "pilot.py"
SPEC = importlib.util.spec_from_file_location("pressure_discovery_pilot", PILOT_PATH)
assert SPEC is not None and SPEC.loader is not None
pilot = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(pilot)


def load_fixture(name: str) -> dict:
    return json.loads((PILOT_ROOT / "fixtures" / name).read_text(encoding="utf-8"))


def minimal_scenario() -> dict:
    return {
        "lane": "diagnostic_injection",
        "identity_version": {
            "scenario_id": "CASE-OPAQUE-01",
            "scenario_version": "1.0.0",
            "oracle_version": "1.0.0",
            "provenance_root_id": "ROOT-SYNTHETIC-01",
            "contract_author": "fixture-author-a",
            "independent_validator": "fixture-validator-b",
        },
        "external_provenance": {
            "source_class": "S",
            "decision_time_cutoff": "2026-01-15",
            "root_episode": "Synthetic methodology fixture",
            "source_lineage_graph": ["ROOT-SYNTHETIC-01"],
            "raw_source_snapshot_ref": "fixture:root-synthetic-01",
            "transformation_redaction_log": ["Constructed for evaluator-plumbing validation."],
            "framework_access_attestation": "diagnostic_fixture_not_ecological",
        },
        "user_visible_package": {
            "prompt": "Choose whether to retain the approved plan.",
            "artifacts": [],
            "acting_role": "Marketing operations lead",
            "tools_external_evidence": [],
            "material_facts": ["The plan is approved and feasible."],
        },
        "decision_record": {
            "consequential_decision": "Retain or reopen the approved plan.",
            "decision_owner_authority": "Marketing operations lead may retain it.",
            "objective_material_consequence": "Avoid an unnecessary launch delay.",
        },
        "evidence_state_ledger": [
            {
                "proposition": "The plan is approved.",
                "status": "established",
                "provenance_authority": "signed approval record",
                "executor_visibility": "visible",
                "commitment_status": "fixed",
            }
        ],
        "oracle": {
            "primary_truth_type": "T2",
            "modifiers": ["R"],
            "must": [
                {
                    "predicate_id": "P-RETAIN",
                    "activation": {"ledger_proposition": "The plan is approved."},
                    "slot": "D",
                    "relation": "contains",
                    "value": "retain",
                    "contract_clause": "Protect valid fixed state.",
                    "hard": True,
                    "fatal": True,
                }
            ],
            "must_not": [
                {
                    "predicate_id": "P-NO-REOPEN",
                    "activation": {"ledger_proposition": "The plan is approved."},
                    "slot": "D",
                    "relation": "contains",
                    "value": "reopen",
                    "contract_clause": "Do not reopen valid fixed state.",
                    "hard": True,
                    "fatal": True,
                }
            ],
            "may": [],
            "pass_sufficiency_rule": "All activated fatal predicates are satisfied.",
            "consequential_disqualifying_errors": ["Unnecessarily reopening the approved plan."],
        },
        "validity_docket": {
            "reality_materiality": {
                "realism": True,
                "decision_relevance": True,
                "materiality": True,
                "real_world_prior": True,
            },
            "underspecification": {
                "two_world_witness": "Approval is either valid or contradicted; the visible record resolves it.",
                "hidden_world_specific": False,
                "deliberate_t3": False,
            },
            "oracle_robustness": {
                "fluent_wrong_rejected": True,
                "noncanonical_good_accepted": True,
            },
            "independence_leakage": {
                "answer_leakage_absent": True,
                "framework_shaping_absent": True,
            },
            "attribution_viability": {
                "counterfactual_available": True,
                "mechanism_capped_f12": False,
            },
            "fluent_wrong_anchor": "Reopen the approved plan without cause.",
            "noncanonical_good_anchor": "Proceed while logging the approval dependency.",
            "disposition": "ACCEPT",
            "validator_identities": ["fixture-validator-b", "fixture-validator-c"],
            "rationale": "All non-compensatory gates pass.",
        },
    }


def candidate_with_slots(**overrides) -> dict:
    candidate = {
        "candidate_id": "CANDIDATE-OPAQUE-01",
        "output": "Retain the approved plan and proceed within the recorded authority.",
        "semantic_slots": {
            "D": ["retain"],
            "E": ["approval_record_established"],
            "U": [],
            "S": ["approved_fixed"],
            "A": ["within_authority"],
            "N": ["proceed"],
            "R": ["operations"],
            "C": ["concise"],
        },
        "output_evidence": {
            "P-RETAIN": "Retain the approved plan",
            "P-NO-REOPEN": "Retain",
        },
    }
    prose = overrides.pop("prose", None)
    if prose is not None:
        candidate["output"] = prose
    for slot, value in overrides.items():
        candidate["semantic_slots"][slot] = value
    return candidate


def fixture_judge(judge_id: str = "JUDGE-FIXTURE-A") -> dict:
    return {
        "judge_id": judge_id,
        "judge_version": "1.0.0",
        "judge_kind": "deterministic_fixture",
        "confidence": "high",
        "confidence_reason": "The structured semantic assertions are complete.",
    }


def fixture_judgment(overall: str) -> dict:
    return {
        "case_id": "CASE-OPAQUE-01",
        "candidate_id": "CANDIDATE-OPAQUE-01",
        "judge_id": "JUDGE-FIXTURE-A",
        "judge_version": "1.0.0",
        "overall": overall,
    }


def valid_unsealed_trace() -> list[dict]:
    run_id = "RUN-OPAQUE-01"
    return [
        pilot.make_event(
            run_id,
            1,
            "RUN_BOUND",
            {
                "scenario_id": "CASE-OPAQUE-01",
                "scenario_hash": "sha256:" + "1" * 64,
                "oracle_id": "ORACLE-OPAQUE-01",
                "oracle_hash": "sha256:" + "2" * 64,
                "condition_id": "COND-OPAQUE-01",
                "intended_visible_input_digest": "sha256:" + "3" * 64,
                "delivered_visible_input_digest": "sha256:" + "3" * 64,
                "common_scaffold_digest": "sha256:" + "4" * 64,
                "model_configuration_digest": "sha256:" + "5" * 64,
                "tools_permissions_digest": "sha256:" + "6" * 64,
                "external_evidence_digest": "sha256:" + "7" * 64,
                "fresh_context_id": "FRESH-OPAQUE-01",
                "diagnostic_mode": True,
                "start_time": "2026-08-24T00:00:00Z",
            },
        ),
        pilot.make_event(
            run_id,
            2,
            "SKILL_ACTIVATION",
            {
                "intended_condition": "with_skill",
                "requested_skill_id": "marketing-practitioner",
                "requested_skill_version": "0.5.1",
                "requested_skill_hash": "sha256:" + "8" * 64,
                "active_skill_id": "marketing-practitioner",
                "active_skill_version": "0.5.1",
                "active_skill_hash": "sha256:" + "8" * 64,
                "outcome": "activated",
                "activation_error_reference": None,
            },
        ),
        pilot.make_event(
            run_id,
            3,
            "KNOWLEDGE_REQUEST",
            {
                "request_id": "REQUEST-OPAQUE-01",
                "request_kind": "logical_route",
                "requested_id": "route.opaque",
                "initiator": "normal_execution",
            },
        ),
        pilot.make_event(
            run_id,
            4,
            "KNOWLEDGE_ACCESS",
            {
                "request_id": "REQUEST-OPAQUE-01",
                "route_id": "route.opaque",
                "resolution_status": "resolved",
                "delivery_status": "delivered",
                "resolver_mode": "index",
                "route_index_hash": "sha256:" + "9" * 64,
                "resource_id": "resource.opaque",
                "resource_hash": "sha256:" + "a" * 64,
                "selector_hash": "sha256:" + "b" * 64,
                "extracted_content_hash": "sha256:" + "c" * 64,
                "fallback_error_status": None,
            },
        ),
    ]


def reseal_trace(trace: list[dict]) -> list[dict]:
    """Recompute all event and run seals after a semantic trace mutation."""

    run_id = trace[0]["run_id"]
    for sequence, event in enumerate(trace, start=1):
        event["sequence"] = sequence
        event["event_id"] = f"{run_id}:{sequence:04d}:{event['event_type']}"
        event["payload_digest"] = pilot.sha256_digest(event["payload"])
    sealed_payload = trace[-1]["payload"]
    sealed_payload["event_count"] = len(trace)
    sealed_payload["ordered_trace_root_hash"] = pilot._trace_root(trace[:-1])
    trace[-1]["payload_digest"] = pilot.sha256_digest(sealed_payload)
    return trace


class CoreContractTests(unittest.TestCase):
    def test_canonical_hash_is_key_order_independent_and_utf8_safe(self) -> None:
        left = {"b": "Tiếng Việt", "a": ["日本語", "français"]}
        right = {"a": ["日本語", "français"], "b": "Tiếng Việt"}
        self.assertEqual(pilot.sha256_digest(left), pilot.sha256_digest(right))
        self.assertTrue(pilot.sha256_digest(left).startswith("sha256:"))

    def test_material_scenario_or_oracle_change_invalidates_reuse(self) -> None:
        scenario = minimal_scenario()
        oracle = scenario["oracle"]
        original = pilot.reuse_key(scenario, oracle)

        changed_scenario = copy.deepcopy(scenario)
        changed_scenario["user_visible_package"]["prompt"] += " Material fact."
        changed_oracle = copy.deepcopy(oracle)
        changed_oracle["must"][0]["value"] = "changed"

        self.assertNotEqual(original, pilot.reuse_key(changed_scenario, oracle))
        self.assertNotEqual(original, pilot.reuse_key(scenario, changed_oracle))

    def test_exact_seven_block_contract_is_accepted(self) -> None:
        self.assertEqual([], pilot.validate_scenario(minimal_scenario()))

    def test_missing_required_block_is_rejected(self) -> None:
        scenario = minimal_scenario()
        del scenario["decision_record"]
        self.assertIn("missing scenario block: decision_record", pilot.validate_scenario(scenario))

    def test_unsupported_predicate_activation_grammar_is_rejected(self) -> None:
        scenario = minimal_scenario()
        scenario["oracle"]["must"][0]["activation"] = {"unknown_switch": True}
        self.assertTrue(
            any(
                "unsupported activation grammar" in error
                for error in pilot.validate_scenario(scenario)
            )
        )

    def test_invalid_two_world_scenario_is_rejected_and_preserved(self) -> None:
        scenario = minimal_scenario()
        scenario["validity_docket"]["underspecification"]["hidden_world_specific"] = True
        scenario["validity_docket"]["disposition"] = "REJECT"
        self.assertEqual([], pilot.validate_scenario(scenario))
        result = pilot.validity_disposition(scenario)
        self.assertEqual("REJECT", result["disposition"])
        self.assertTrue(result["preserve_artifact"])
        self.assertIn("hidden-world-specific", result["reasons"])

    def test_failed_hard_validity_gate_cannot_be_compensated(self) -> None:
        scenario = minimal_scenario()
        scenario["validity_docket"]["reality_materiality"]["materiality"] = False
        scenario["validity_docket"]["disposition"] = "ACCEPT"
        result = pilot.validity_disposition(scenario)
        self.assertEqual("REJECT", result["disposition"])
        self.assertIn("materiality", result["reasons"])


class SemanticJudgmentTests(unittest.TestCase):
    def test_must_and_fatal_must_not_drive_non_numeric_judgment(self) -> None:
        record = pilot.judge_candidate(
            minimal_scenario(), candidate_with_slots(), fixture_judge()
        )
        self.assertEqual("acceptable", record["overall"])
        self.assertNotIn("score", record)
        self.assertEqual([], record["fatal_violations"])
        self.assertTrue(record["pass_sufficiency_evaluation"]["satisfied"])
        self.assertTrue(
            all(item["status"] == "clear" for item in record["consequential_error_checks"])
        )
        self.assertEqual(
            ["satisfied", "satisfied"],
            [criterion["result"] for criterion in record["criteria"]],
        )

    def test_fatal_must_not_violation_is_unacceptable_with_evidence(self) -> None:
        candidate = candidate_with_slots(D=["retain", "reopen"])
        candidate["output_evidence"]["P-NO-REOPEN"] = "Reopen the plan."
        record = pilot.judge_candidate(minimal_scenario(), candidate, fixture_judge())
        self.assertEqual("unacceptable", record["overall"])
        self.assertEqual(["P-NO-REOPEN"], record["fatal_violations"])
        violated = [item for item in record["criteria"] if item["result"] == "violated"]
        self.assertEqual("Reopen the plan.", violated[0]["output_evidence"])

    def test_missing_hard_semantic_slot_is_indeterminate_not_assessable(self) -> None:
        candidate = candidate_with_slots()
        del candidate["semantic_slots"]["D"]
        record = pilot.judge_candidate(minimal_scenario(), candidate, fixture_judge())
        self.assertEqual("indeterminate", record["overall"])
        self.assertEqual(
            ["not assessable", "not assessable"],
            [criterion["result"] for criterion in record["criteria"]],
        )

    def test_inactive_predicate_is_not_applicable(self) -> None:
        scenario = minimal_scenario()
        scenario["oracle"]["must"][0]["activation"] = {
            "ledger_proposition": "A proposition not present."
        }
        record = pilot.judge_candidate(scenario, candidate_with_slots(), fixture_judge())
        criterion = next(item for item in record["criteria"] if item["predicate_id"] == "P-RETAIN")
        self.assertEqual("not applicable", criterion["result"])

    def test_pair_cannot_pass_when_either_member_is_wrong(self) -> None:
        result = pilot.evaluate_pair(
            fixture_judgment("unacceptable"),
            fixture_judgment("unacceptable"),
            candidate_with_slots(D=["wrong"]),
            candidate_with_slots(D=["wrong"]),
            {"slot": "D", "relation": "PRESERVE"},
        )
        self.assertFalse(result["passed"])
        self.assertEqual("member_not_independently_acceptable", result["reason"])

    def test_lexical_difference_does_not_fail_semantic_preservation(self) -> None:
        result = pilot.evaluate_pair(
            fixture_judgment("acceptable"),
            fixture_judgment("acceptable"),
            candidate_with_slots(D=["retain"], prose="Keep the plan."),
            candidate_with_slots(D=["retain"], prose="Do not change course."),
            {"slot": "D", "relation": "PRESERVE"},
        )
        self.assertTrue(result["passed"])

    def test_all_frozen_pair_relations_compare_semantic_slots(self) -> None:
        acceptable = fixture_judgment("acceptable")
        cases = [
            ("PRESERVE", ["retain"], ["retain"], {}),
            ("CHANGE_TO", ["hold"], ["launch"], {"value": "launch"}),
            ("ADD", ["retain"], ["retain", "escalate"], {"value": "escalate"}),
            ("DROP", ["retain", "reopen"], ["retain"], {"value": "reopen"}),
            (
                "TIGHTEN",
                ["open"],
                ["strict"],
                {"order": ["open", "bounded", "strict"]},
            ),
            (
                "LOOSEN",
                ["strict"],
                ["bounded"],
                {"order": ["open", "bounded", "strict"]},
            ),
            ("PERMITTED_VARIANCE", ["retain"], ["retain", "log"], {}),
        ]
        for relation, left, right, extra in cases:
            with self.subTest(relation=relation):
                packet = {"slot": "D", "relation": relation, **extra}
                result = pilot.evaluate_pair(
                    acceptable,
                    acceptable,
                    candidate_with_slots(D=left),
                    candidate_with_slots(D=right),
                    packet,
                )
                self.assertTrue(result["passed"], result)


class RunEvidenceTests(unittest.TestCase):
    def test_trace_seals_order_payloads_count_and_root(self) -> None:
        trace = pilot.seal_trace(
            valid_unsealed_trace(),
            "sha256:" + "d" * 64,
            "complete",
            "2026-08-24T00:01:00Z",
        )
        self.assertEqual([], pilot.validate_trace(trace))
        self.assertEqual("RUN_SEALED", trace[-1]["event_type"])
        self.assertEqual(len(trace), trace[-1]["payload"]["event_count"])

    def test_trace_rejects_unknown_event_type(self) -> None:
        trace = valid_unsealed_trace()
        trace.append(pilot.make_event("RUN-OPAQUE-01", 5, "PRIVATE_REASONING", {}))
        trace = pilot.seal_trace(
            trace, "sha256:" + "d" * 64, "complete", "2026-08-24T00:01:00Z"
        )
        self.assertIn("unsupported event type: PRIVATE_REASONING", pilot.validate_trace(trace))

    def test_request_without_access_is_incomplete(self) -> None:
        trace = valid_unsealed_trace()[:-1]
        trace = pilot.seal_trace(
            trace, "sha256:" + "d" * 64, "complete", "2026-08-24T00:01:00Z"
        )
        self.assertIn(
            "knowledge request has no access outcome: REQUEST-OPAQUE-01",
            pilot.validate_trace(trace),
        )

    def test_access_cross_fields_must_describe_one_coherent_outcome(self) -> None:
        trace = pilot.seal_trace(
            valid_unsealed_trace(),
            "sha256:" + "d" * 64,
            "complete",
            "2026-08-24T00:01:00Z",
        )
        access = next(event for event in trace if event["event_type"] == "KNOWLEDGE_ACCESS")
        access["payload"].update(
            resolution_status="unresolved",
            delivery_status="delivered",
        )
        trace = reseal_trace(trace)

        self.assertTrue(
            any("knowledge access outcome is incoherent" in error for error in pilot.validate_trace(trace))
        )

    def test_hash_fields_reject_non_sha256_values(self) -> None:
        trace = pilot.seal_trace(
            valid_unsealed_trace(),
            "sha256:" + "d" * 64,
            "complete",
            "2026-08-24T00:01:00Z",
        )
        trace[0]["payload"]["scenario_hash"] = "not-a-digest"
        trace = reseal_trace(trace)

        self.assertTrue(
            any("invalid sha256 digest" in error for error in pilot.validate_trace(trace))
        )

    def test_resealed_null_required_run_bound_digest_is_rejected(self) -> None:
        trace = pilot.seal_trace(
            valid_unsealed_trace(),
            "sha256:" + "d" * 64,
            "complete",
            "2026-08-24T00:01:00Z",
        )
        trace[0]["payload"]["delivered_visible_input_digest"] = None
        trace = reseal_trace(trace)

        self.assertTrue(
            any(
                "missing required RUN_BOUND digest: delivered_visible_input_digest" in error
                for error in pilot.validate_trace(trace)
            )
        )

    def test_resealed_diagnostic_mode_requires_exact_boolean_type(self) -> None:
        for invalid_value in (1, 1.0):
            with self.subTest(invalid_value=invalid_value):
                trace = pilot.seal_trace(
                    valid_unsealed_trace(),
                    "sha256:" + "d" * 64,
                    "complete",
                    "2026-08-24T00:01:00Z",
                )
                trace[0]["payload"]["diagnostic_mode"] = invalid_value
                trace = reseal_trace(trace)

                self.assertTrue(
                    any(
                        "RUN_BOUND diagnostic mode must be a boolean" in error
                        for error in pilot.validate_trace(trace)
                    )
                )

    def test_activation_payload_must_match_ab_condition(self) -> None:
        trace = pilot.seal_trace(
            valid_unsealed_trace(),
            "sha256:" + "d" * 64,
            "complete",
            "2026-08-24T00:01:00Z",
        )
        activation = next(event for event in trace if event["event_type"] == "SKILL_ACTIVATION")
        activation["payload"]["intended_condition"] = "without_skill"
        trace = reseal_trace(trace)

        self.assertTrue(
            any("activation payload conflicts with intended condition" in error for error in pilot.validate_trace(trace))
        )

    def test_resealed_activation_identity_and_version_require_nonempty_strings(self) -> None:
        invalid_values = (["wrong"], 42, {"bad": "version"}, True, "")
        for field in (
            "requested_skill_id",
            "requested_skill_version",
            "active_skill_id",
            "active_skill_version",
        ):
            for invalid_value in invalid_values:
                with self.subTest(field=field, invalid_value=invalid_value):
                    trace = pilot.seal_trace(
                        valid_unsealed_trace(),
                        "sha256:" + "d" * 64,
                        "complete",
                        "2026-08-24T00:01:00Z",
                    )
                    activation = next(
                        event
                        for event in trace
                        if event["event_type"] == "SKILL_ACTIVATION"
                    )
                    activation["payload"][field] = invalid_value
                    trace = reseal_trace(trace)

                    self.assertTrue(
                        any(
                            "activation skill ID/version must be a nonempty string" in error
                            for error in pilot.validate_trace(trace)
                        )
                    )

    def test_resealed_access_before_request_is_rejected(self) -> None:
        trace = pilot.seal_trace(
            valid_unsealed_trace(),
            "sha256:" + "d" * 64,
            "complete",
            "2026-08-24T00:01:00Z",
        )
        trace[2], trace[3] = trace[3], trace[2]
        trace = reseal_trace(trace)

        self.assertTrue(
            any("knowledge access precedes its request" in error for error in pilot.validate_trace(trace))
        )

    def test_resealed_invalid_request_kind_is_rejected(self) -> None:
        trace = pilot.seal_trace(
            valid_unsealed_trace(),
            "sha256:" + "d" * 64,
            "complete",
            "2026-08-24T00:01:00Z",
        )
        request = next(event for event in trace if event["event_type"] == "KNOWLEDGE_REQUEST")
        request["payload"]["request_kind"] = "invalid_kind"
        trace = reseal_trace(trace)

        self.assertTrue(
            any("invalid KNOWLEDGE_REQUEST request kind" in error for error in pilot.validate_trace(trace))
        )

    def test_resealed_invalid_request_initiator_is_rejected(self) -> None:
        trace = pilot.seal_trace(
            valid_unsealed_trace(),
            "sha256:" + "d" * 64,
            "complete",
            "2026-08-24T00:01:00Z",
        )
        request = next(event for event in trace if event["event_type"] == "KNOWLEDGE_REQUEST")
        request["payload"]["initiator"] = "invalid_initiator"
        trace = reseal_trace(trace)

        self.assertTrue(
            any("invalid KNOWLEDGE_REQUEST initiator" in error for error in pilot.validate_trace(trace))
        )

    def test_resealed_invalid_resolver_mode_is_rejected(self) -> None:
        trace = pilot.seal_trace(
            valid_unsealed_trace(),
            "sha256:" + "d" * 64,
            "complete",
            "2026-08-24T00:01:00Z",
        )
        access = next(event for event in trace if event["event_type"] == "KNOWLEDGE_ACCESS")
        access["payload"]["resolver_mode"] = "invalid_mode"
        trace = reseal_trace(trace)

        self.assertTrue(
            any("invalid KNOWLEDGE_ACCESS resolver mode" in error for error in pilot.validate_trace(trace))
        )

    def test_resealed_delivered_route_mismatch_is_rejected(self) -> None:
        trace = pilot.seal_trace(
            valid_unsealed_trace(),
            "sha256:" + "d" * 64,
            "complete",
            "2026-08-24T00:01:00Z",
        )
        access = next(event for event in trace if event["event_type"] == "KNOWLEDGE_ACCESS")
        access["payload"]["route_id"] = "route.other"
        trace = reseal_trace(trace)

        self.assertTrue(
            any("knowledge access route differs from requested route" in error for error in pilot.validate_trace(trace))
        )

    def test_resealed_invalid_fallback_error_status_is_rejected(self) -> None:
        trace = pilot.seal_trace(
            valid_unsealed_trace(),
            "sha256:" + "d" * 64,
            "complete",
            "2026-08-24T00:01:00Z",
        )
        access = next(event for event in trace if event["event_type"] == "KNOWLEDGE_ACCESS")
        access["payload"]["fallback_error_status"] = "invalid_status"
        trace = reseal_trace(trace)

        self.assertTrue(
            any("invalid KNOWLEDGE_ACCESS fallback/error status" in error for error in pilot.validate_trace(trace))
        )

    def test_resealed_fallback_resolved_delivery_requires_fallback_status(self) -> None:
        trace = pilot.seal_trace(
            valid_unsealed_trace(),
            "sha256:" + "d" * 64,
            "complete",
            "2026-08-24T00:01:00Z",
        )
        access = next(event for event in trace if event["event_type"] == "KNOWLEDGE_ACCESS")
        access["payload"].update(resolver_mode="fallback", fallback_error_status=None)
        trace = reseal_trace(trace)

        self.assertTrue(
            any("fallback resolver requires fallback status" in error for error in pilot.validate_trace(trace))
        )

    def test_resealed_logical_unresolved_access_may_omit_route_id(self) -> None:
        trace = pilot.seal_trace(
            valid_unsealed_trace(),
            "sha256:" + "d" * 64,
            "complete",
            "2026-08-24T00:01:00Z",
        )
        access = next(event for event in trace if event["event_type"] == "KNOWLEDGE_ACCESS")
        access["payload"].update(
            route_id=None,
            resolution_status="unresolved",
            delivery_status="not-delivered",
            resource_id=None,
            resource_hash=None,
            selector_hash=None,
            extracted_content_hash=None,
            fallback_error_status="unresolved",
        )
        trace = reseal_trace(trace)

        self.assertEqual([], pilot.validate_trace(trace))

    def test_resealed_evidence_source_resource_must_match_requested_id(self) -> None:
        trace = pilot.seal_trace(
            valid_unsealed_trace(),
            "sha256:" + "d" * 64,
            "complete",
            "2026-08-24T00:01:00Z",
        )
        request = next(event for event in trace if event["event_type"] == "KNOWLEDGE_REQUEST")
        access = next(event for event in trace if event["event_type"] == "KNOWLEDGE_ACCESS")
        request["payload"].update(request_kind="evidence_source", requested_id="evidence.opaque")
        access["payload"].update(
            route_id=None,
            resource_id="wrong.evidence",
            resource_hash=pilot.sha256_digest({"resource": "wrong.evidence"}),
            selector_hash=pilot.sha256_digest({"selector": "evidence.opaque"}),
            extracted_content_hash=pilot.sha256_digest({"extract": "evidence.opaque"}),
        )
        trace = reseal_trace(trace)

        self.assertTrue(
            any("knowledge access resource differs from requested resource" in error for error in pilot.validate_trace(trace))
        )

    def test_resealed_delivered_trace_accepts_opaque_identity_hashes(self) -> None:
        trace = pilot.seal_trace(
            valid_unsealed_trace(),
            "sha256:" + "d" * 64,
            "complete",
            "2026-08-24T00:01:00Z",
        )
        trace = reseal_trace(trace)

        self.assertEqual([], pilot.validate_trace(trace))

    def test_resealed_unhashable_access_request_id_returns_validation_error(self) -> None:
        trace = pilot.seal_trace(
            valid_unsealed_trace(),
            "sha256:" + "d" * 64,
            "complete",
            "2026-08-24T00:01:00Z",
        )
        access = next(event for event in trace if event["event_type"] == "KNOWLEDGE_ACCESS")
        access["payload"]["request_id"] = []
        trace = reseal_trace(trace)

        errors = pilot.validate_trace(trace)
        self.assertTrue(any("invalid KNOWLEDGE_ACCESS request ID" in error for error in errors))

    def test_resealed_without_skill_baseline_not_activated_is_rejected(self) -> None:
        cases = load_fixture("pilot-cases.json")
        evidence = load_fixture("evidence-packets.json")
        condition = cases["conditions"][0]
        scenario = next(
            item for item in cases["scenarios"] if pilot._scenario_ref(item) == condition["scenario_ref"]
        )
        trace = pilot._build_evidence_trace(
            scenario,
            condition,
            "baseline_direct",
            evidence,
            cases["target"],
            intended_condition="without_skill",
        )
        activation = next(event for event in trace if event["event_type"] == "SKILL_ACTIVATION")
        self.assertEqual("not-intended", activation["payload"]["outcome"])
        activation["payload"]["outcome"] = "not-activated"
        trace = reseal_trace(trace)

        self.assertTrue(
            any("without_skill baseline must use not-intended" in error for error in pilot.validate_trace(trace))
        )

    def test_trace_rejects_unexpected_payload_fields(self) -> None:
        trace = pilot.seal_trace(
            valid_unsealed_trace(),
            "sha256:" + "d" * 64,
            "complete",
            "2026-08-24T00:01:00Z",
        )
        trace[0]["payload"]["chain_of_thought"] = "private"
        trace = reseal_trace(trace)

        self.assertTrue(
            any("unexpected RUN_BOUND payload field" in error for error in pilot.validate_trace(trace))
        )

    def test_trace_rejects_unexpected_top_level_event_fields(self) -> None:
        trace = pilot.seal_trace(
            valid_unsealed_trace(),
            "sha256:" + "d" * 64,
            "complete",
            "2026-08-24T00:01:00Z",
        )
        trace[0]["chain_of_thought"] = "private"
        trace = reseal_trace(trace)

        self.assertTrue(
            any("unexpected top-level event field" in error for error in pilot.validate_trace(trace))
        )

    def test_diagnostic_event_is_rejected_outside_diagnostic_run(self) -> None:
        trace = valid_unsealed_trace()
        trace[0]["payload"]["diagnostic_mode"] = False
        trace[0]["payload_digest"] = pilot.sha256_digest(trace[0]["payload"])
        trace.append(
            pilot.make_event(
                "RUN-OPAQUE-01",
                5,
                "INTERVENTION_APPLIED",
                {
                    "intervention_type": "route_force",
                    "version_hash": "sha256:" + "e" * 64,
                    "target": "route.opaque",
                    "delta_manifest": ["route only"],
                    "held_constant_manifest": ["task", "oracle", "configuration"],
                    "control_intervention_label": "intervention",
                    "negative_control_reference": "RUN-CONTROL-01",
                },
            )
        )
        trace = pilot.seal_trace(
            trace, "sha256:" + "d" * 64, "complete", "2026-08-24T00:01:00Z"
        )
        self.assertIn(
            "diagnostic event in non-diagnostic run: INTERVENTION_APPLIED",
            pilot.validate_trace(trace),
        )


class AttributionTests(unittest.TestCase):
    def result_for(self, condition_id: str, mutate=None) -> dict:
        cases = load_fixture("pilot-cases.json")
        evidence = load_fixture("evidence-packets.json")
        if mutate is not None:
            packet = next(item for item in evidence["packets"] if item["condition_id"] == condition_id)
            mutate(packet)
        sealed = pilot.evaluate_and_seal(cases, evidence)
        return next(item for item in sealed["condition_results"] if item["condition_id"] == condition_id)

    def result_with_mutated_intervention_trace(
        self, condition_id: str, mutate_trace
    ) -> dict:
        cases = load_fixture("pilot-cases.json")
        evidence = load_fixture("evidence-packets.json")
        original_builder = pilot._build_evidence_trace

        def build_with_mutation(*args, **kwargs):
            trace = original_builder(*args, **kwargs)
            condition = args[1]
            if (
                condition["condition_id"] == condition_id
                and kwargs.get("intervention") is not None
            ):
                mutate_trace(trace)
                trace = reseal_trace(trace)
            return trace

        with mock.patch.object(
            pilot, "_build_evidence_trace", side_effect=build_with_mutation
        ):
            sealed = pilot.evaluate_and_seal(cases, evidence)
        return next(
            item
            for item in sealed["condition_results"]
            if item["condition_id"] == condition_id
        )

    def test_explicit_activation_failure_supports_f3(self) -> None:
        self.assertEqual("F3", self.result_for("COND-005")["attribution"]["mechanism"])

    def binding_result_for(self, mutate_trace) -> tuple[dict, list[dict]]:
        cases = load_fixture("pilot-cases.json")
        evidence = load_fixture("evidence-packets.json")
        conditions = {item["condition_id"]: item for item in cases["conditions"]}
        scenarios = {
            f"{item['identity_version']['scenario_id']}@{item['identity_version']['scenario_version']}": item
            for item in cases["scenarios"]
        }
        condition = conditions["COND-006"]
        scenario = scenarios[condition["scenario_ref"]]
        packet = next(
            item for item in evidence["packets"] if item["condition_id"] == "COND-006"
        )
        trace = pilot._build_evidence_trace(
            scenario,
            condition,
            packet["ordinary_trace_profile"],
            evidence,
            cases["target"],
            requested_route=pilot._packet_expected_route(scenario, packet),
        )
        mutate_trace(trace)
        trace = reseal_trace(trace)
        judgments = [
            pilot.judge_candidate(scenario, condition["candidate"], judge)
            for judge in cases["fixture_judges"]
        ]
        attribution, _ = pilot._classify_from_evidence(
            scenario,
            condition,
            packet,
            conditions,
            evidence,
            judgments,
            trace,
            pilot.validate_trace(trace),
            cases["fixture_judges"],
            cases["target"],
        )
        return attribution, trace

    def test_resealed_delivered_visible_input_mismatch_supports_f3(self) -> None:
        def mutate(trace: list[dict]) -> None:
            run_bound = next(event for event in trace if event["event_type"] == "RUN_BOUND")
            run_bound["payload"]["delivered_visible_input_digest"] = "sha256:" + "a" * 64

        attribution, trace = self.binding_result_for(mutate)
        self.assertEqual([], pilot.validate_trace(trace))
        self.assertEqual("F3", attribution["mechanism"])

    def test_resealed_common_scaffold_mismatch_supports_f3(self) -> None:
        def mutate(trace: list[dict]) -> None:
            run_bound = next(event for event in trace if event["event_type"] == "RUN_BOUND")
            run_bound["payload"]["common_scaffold_digest"] = "sha256:" + "b" * 64

        attribution, trace = self.binding_result_for(mutate)
        self.assertEqual([], pilot.validate_trace(trace))
        self.assertEqual("F3", attribution["mechanism"])

    def test_resealed_model_configuration_mismatch_supports_f3(self) -> None:
        def mutate(trace: list[dict]) -> None:
            run_bound = next(event for event in trace if event["event_type"] == "RUN_BOUND")
            run_bound["payload"]["model_configuration_digest"] = "sha256:" + "d" * 64

        attribution, trace = self.binding_result_for(mutate)
        self.assertEqual([], pilot.validate_trace(trace))
        self.assertEqual("F3", attribution["mechanism"])

    def test_resealed_active_skill_id_mismatch_supports_f3(self) -> None:
        def mutate(trace: list[dict]) -> None:
            activation = next(
                event for event in trace if event["event_type"] == "SKILL_ACTIVATION"
            )
            activation["payload"]["active_skill_id"] = "wrong-marketing-skill"

        attribution, trace = self.binding_result_for(mutate)
        self.assertEqual([], pilot.validate_trace(trace))
        self.assertEqual("F3", attribution["mechanism"])

    def test_resealed_active_skill_version_mismatch_supports_f3(self) -> None:
        def mutate(trace: list[dict]) -> None:
            activation = next(
                event for event in trace if event["event_type"] == "SKILL_ACTIVATION"
            )
            activation["payload"]["active_skill_version"] = "9.9.9"

        attribution, trace = self.binding_result_for(mutate)
        self.assertEqual([], pilot.validate_trace(trace))
        self.assertEqual("F3", attribution["mechanism"])

    def test_resealed_non_string_active_identity_or_version_is_f12(self) -> None:
        attacks = (
            ("active_skill_id", ["wrong"]),
            ("active_skill_id", 42),
            ("active_skill_version", {"bad": "version"}),
            ("active_skill_version", True),
        )
        for field, invalid_value in attacks:
            with self.subTest(field=field, invalid_value=invalid_value):
                def mutate_trace(
                    trace: list[dict], field: str = field, invalid_value=invalid_value
                ) -> None:
                    activation = next(
                        event
                        for event in trace
                        if event["event_type"] == "SKILL_ACTIVATION"
                    )
                    activation["payload"][field] = invalid_value

                attribution, trace = self.binding_result_for(mutate_trace)
                self.assertTrue(pilot.validate_trace(trace))
                self.assertEqual("F12", attribution["mechanism"])

    def test_resealed_active_skill_hash_mismatch_supports_f3(self) -> None:
        def mutate(trace: list[dict]) -> None:
            activation = next(
                event for event in trace if event["event_type"] == "SKILL_ACTIVATION"
            )
            activation["payload"]["active_skill_hash"] = "sha256:" + "c" * 64

        attribution, trace = self.binding_result_for(mutate)
        self.assertEqual([], pilot.validate_trace(trace))
        self.assertEqual("F3", attribution["mechanism"])

    def test_resealed_f3_mismatch_requires_every_binding_fact(self) -> None:
        required_facts = (
            ("RUN_BOUND", "scenario_id"),
            ("RUN_BOUND", "scenario_hash"),
            ("RUN_BOUND", "oracle_id"),
            ("RUN_BOUND", "oracle_hash"),
            ("RUN_BOUND", "condition_id"),
            ("RUN_BOUND", "intended_visible_input_digest"),
            ("RUN_BOUND", "delivered_visible_input_digest"),
            ("RUN_BOUND", "common_scaffold_digest"),
            ("RUN_BOUND", "model_configuration_digest"),
            ("RUN_BOUND", "tools_permissions_digest"),
            ("RUN_BOUND", "external_evidence_digest"),
            ("RUN_BOUND", "fresh_context_id"),
            ("RUN_BOUND", "diagnostic_mode"),
            ("RUN_BOUND", "start_time"),
            ("SKILL_ACTIVATION", "requested_skill_id"),
            ("SKILL_ACTIVATION", "requested_skill_version"),
            ("SKILL_ACTIVATION", "requested_skill_hash"),
            ("SKILL_ACTIVATION", "active_skill_id"),
            ("SKILL_ACTIVATION", "active_skill_version"),
            ("SKILL_ACTIVATION", "active_skill_hash"),
        )
        for event_type, field in required_facts:
            for mutation in ("remove", "null"):
                with self.subTest(event_type=event_type, field=field, mutation=mutation):
                    def mutate_trace(
                        trace: list[dict],
                        event_type: str = event_type,
                        field: str = field,
                        mutation: str = mutation,
                    ) -> None:
                        run_bound = next(
                            event for event in trace if event["event_type"] == "RUN_BOUND"
                        )
                        run_bound["payload"]["delivered_visible_input_digest"] = (
                            "sha256:" + "a" * 64
                        )
                        payload = next(
                            event["payload"]
                            for event in trace
                            if event["event_type"] == event_type
                        )
                        if mutation == "remove":
                            del payload[field]
                        else:
                            payload[field] = None

                    attribution, _ = self.binding_result_for(mutate_trace)
                    self.assertEqual("F12", attribution["mechanism"])

    def test_resealed_wrong_context_binding_blocks_f3(self) -> None:
        wrong_context = {
            "scenario_id": "CASE-WRONG-CONTEXT",
            "scenario_hash": "sha256:" + "d" * 64,
            "oracle_id": "9.9.9",
            "oracle_hash": "sha256:" + "e" * 64,
            "condition_id": "COND-WRONG-CONTEXT",
            "tools_permissions_digest": "sha256:" + "f" * 64,
            "external_evidence_digest": "sha256:" + "0" * 64,
            "diagnostic_mode": False,
        }
        for field, wrong_value in wrong_context.items():
            with self.subTest(field=field):
                def mutate_trace(
                    trace: list[dict], field: str = field, wrong_value=wrong_value
                ) -> None:
                    run_bound = next(
                        event for event in trace if event["event_type"] == "RUN_BOUND"
                    )
                    run_bound["payload"]["delivered_visible_input_digest"] = (
                        "sha256:" + "a" * 64
                    )
                    run_bound["payload"][field] = wrong_value

                attribution, trace = self.binding_result_for(mutate_trace)
                self.assertEqual([], pilot.validate_trace(trace))
                self.assertEqual("F12", attribution["mechanism"])

    def test_resealed_opaque_fresh_context_and_start_time_do_not_block_f3(self) -> None:
        def mutate_trace(trace: list[dict]) -> None:
            run_bound = next(event for event in trace if event["event_type"] == "RUN_BOUND")
            run_bound["payload"].update(
                delivered_visible_input_digest="sha256:" + "a" * 64,
                fresh_context_id="FRESH-OPAQUE-REVIEW",
                start_time="2026-08-24T00:00:01Z",
            )

        attribution, trace = self.binding_result_for(mutate_trace)
        self.assertEqual([], pilot.validate_trace(trace))
        self.assertEqual("F3", attribution["mechanism"])

    def test_resealed_numeric_diagnostic_mode_is_f12(self) -> None:
        for invalid_value in (1, 1.0):
            with self.subTest(invalid_value=invalid_value):
                def mutate_trace(
                    trace: list[dict], invalid_value=invalid_value
                ) -> None:
                    run_bound = next(
                        event for event in trace if event["event_type"] == "RUN_BOUND"
                    )
                    run_bound["payload"].update(
                        delivered_visible_input_digest="sha256:" + "a" * 64,
                        diagnostic_mode=invalid_value,
                    )

                attribution, trace = self.binding_result_for(mutate_trace)
                self.assertTrue(pilot.validate_trace(trace))
                self.assertEqual("F12", attribution["mechanism"])

    def test_authorized_fallback_does_not_establish_f3(self) -> None:
        def mutate(packet: dict) -> None:
            packet["ordinary_trace_profile"] = "authorized_fallback"
            packet["activation_receipt"].update(
                outcome="fallback",
                fallback_authorization="authorized",
            )

        cases = load_fixture("pilot-cases.json")
        evidence = load_fixture("evidence-packets.json")
        evidence["trace_profiles"]["authorized_fallback"] = {
            "activation": "fallback",
            "access": "none",
            "telemetry": "complete",
        }
        packet = next(item for item in evidence["packets"] if item["condition_id"] == "COND-005")
        mutate(packet)
        result = next(
            item
            for item in pilot.evaluate_and_seal(cases, evidence)["condition_results"]
            if item["condition_id"] == "COND-005"
        )
        self.assertEqual("F12", result["attribution"]["mechanism"])

    def test_successful_correct_resource_delivery_blocks_f4(self) -> None:
        result = self.result_for(
            "COND-006",
            lambda packet: packet.update(ordinary_trace_profile="route_delivered"),
        )
        self.assertEqual("F12", result["attribution"]["mechanism"])

    def test_f4_requires_selective_repair_and_irrelevant_control(self) -> None:
        self.assertEqual("F4", self.result_for("COND-006")["attribution"]["mechanism"])
        result = self.result_for(
            "COND-006",
            lambda packet: packet["intervention_runs"][1].update(candidate_ref="catalog:GOOD-003"),
        )
        self.assertEqual("F12", result["attribution"]["mechanism"])

    def test_f4_requires_nonempty_content_bound_route_predicates(self) -> None:
        result = self.result_for(
            "COND-006",
            lambda packet: packet["route_requirement"].update(oracle_predicate_ids=[]),
        )
        self.assertEqual("F12", result["attribution"]["mechanism"])

    def wrong_route_delivery_result_for(
        self,
        mutate_packet=None,
        mutate_trace=None,
        mutate_intervention_trace=None,
    ) -> tuple[dict, list[dict], dict]:
        cases = load_fixture("pilot-cases.json")
        evidence = load_fixture("evidence-packets.json")
        conditions = {item["condition_id"]: item for item in cases["conditions"]}
        condition = conditions["COND-006"]
        scenario = next(
            item
            for item in cases["scenarios"]
            if pilot._scenario_ref(item) == condition["scenario_ref"]
        )
        packet = next(
            item for item in evidence["packets"] if item["condition_id"] == "COND-006"
        )
        if mutate_packet is not None:
            mutate_packet(packet, evidence)
        trace = pilot._build_evidence_trace(
            scenario,
            condition,
            "route_delivered",
            evidence,
            cases["target"],
            requested_route="content.copy-editing",
        )
        if mutate_trace is not None:
            mutate_trace(trace)
            trace = reseal_trace(trace)
        judgments = [
            pilot.judge_candidate(scenario, condition["candidate"], judge)
            for judge in cases["fixture_judges"]
        ]
        def classify() -> tuple[dict, dict]:
            return pilot._classify_from_evidence(
                scenario,
                condition,
                packet,
                conditions,
                evidence,
                judgments,
                trace,
                pilot.validate_trace(trace),
                cases["fixture_judges"],
                cases["target"],
            )

        if mutate_intervention_trace is None:
            attribution, counterfactual = classify()
        else:
            original_builder = pilot._build_evidence_trace

            def build_with_mutation(*args, **kwargs):
                built = original_builder(*args, **kwargs)
                if kwargs.get("intervention") is not None:
                    mutate_intervention_trace(built)
                    built = reseal_trace(built)
                return built

            with mock.patch.object(
                pilot, "_build_evidence_trace", side_effect=build_with_mutation
            ):
                attribution, counterfactual = classify()
        return attribution, trace, counterfactual

    def test_complete_wrong_route_delivery_supports_f4(self) -> None:
        attribution, trace, counterfactual = self.wrong_route_delivery_result_for()
        request = next(
            event["payload"]
            for event in trace
            if event["event_type"] == "KNOWLEDGE_REQUEST"
        )
        access = next(
            event["payload"]
            for event in trace
            if event["event_type"] == "KNOWLEDGE_ACCESS"
        )

        self.assertEqual([], pilot.validate_trace(trace))
        self.assertEqual("content.copy-editing", request["requested_id"])
        self.assertEqual(request["requested_id"], access["route_id"])
        self.assertEqual("delivered", access["delivery_status"])
        self.assertEqual("F4", attribution["mechanism"])
        for arm in counterfactual["intervention_runs"].values():
            for run in arm["stability_runs"]:
                event_types = [event["event_type"] for event in run["trace"]]
                intervention_index = event_types.index("INTERVENTION_APPLIED")
                request_index = event_types.index("KNOWLEDGE_REQUEST")
                access_index = event_types.index("KNOWLEDGE_ACCESS")
                intervention = run["trace"][intervention_index]["payload"]
                request_payload = run["trace"][request_index]["payload"]

                self.assertLess(intervention_index, request_index)
                self.assertLess(request_index, access_index)
                self.assertEqual("forced_intervention", request_payload["initiator"])
                self.assertEqual("logical_route", intervention["injected_content_kind"])

    def test_wrong_route_interventions_require_causal_forced_requests(self) -> None:
        def normal_initiator(trace: list[dict]) -> None:
            request = next(
                event
                for event in trace
                if event["event_type"] == "KNOWLEDGE_REQUEST"
            )
            request["payload"]["initiator"] = "normal_execution"

        def intervention_after_access(trace: list[dict]) -> None:
            intervention = next(
                event
                for event in trace
                if event["event_type"] == "INTERVENTION_APPLIED"
            )
            trace.remove(intervention)
            sealed_index = next(
                index
                for index, event in enumerate(trace)
                if event["event_type"] == "RUN_SEALED"
            )
            trace.insert(sealed_index, intervention)

        for attack in (normal_initiator, intervention_after_access):
            with self.subTest(attack=attack.__name__):
                attribution, trace, _ = self.wrong_route_delivery_result_for(
                    mutate_intervention_trace=attack
                )
                self.assertEqual([], pilot.validate_trace(trace))
                self.assertEqual("F12", attribution["mechanism"])

    def test_f4_target_route_arm_rejects_extra_boundary_state(self) -> None:
        def mutate(trace: list[dict]) -> None:
            intervention = next(
                event["payload"]
                for event in trace
                if event["event_type"] == "INTERVENTION_APPLIED"
            )
            if intervention["control_intervention_label"] != "target":
                return
            run_id = trace[0]["run_id"]
            sealed_index = next(
                index
                for index, event in enumerate(trace)
                if event["event_type"] == "RUN_SEALED"
            )
            trace.insert(
                sealed_index,
                pilot.make_event(
                    run_id,
                    sealed_index + 1,
                    "BOUNDARY_TRANSFER",
                    {
                        "boundary_id": "BOUNDARY-F4-CONTAMINANT",
                        "source_owner": "source-owner",
                        "destination_owner": "destination-owner",
                        "upstream_artifact_hash_ref": "sha256:" + "6" * 64,
                        "downstream_received_artifact_hash_ref": (
                            "sha256:" + "7" * 64
                        ),
                        "critical_assertion_ids": ["ASSERTION-CONTAMINANT"],
                        "transfer_status": "delivered",
                    },
                ),
            )

        attribution, trace, _ = self.wrong_route_delivery_result_for(
            mutate_intervention_trace=mutate
        )

        self.assertEqual([], pilot.validate_trace(trace))
        self.assertEqual("F12", attribution["mechanism"])

    def test_f4_target_and_control_output_seals_are_candidate_bound(self) -> None:
        for arm_name in ("target", "negative_control"):
            with self.subTest(arm_name=arm_name):
                def mutate(trace: list[dict], arm_name=arm_name) -> None:
                    intervention = next(
                        event["payload"]
                        for event in trace
                        if event["event_type"] == "INTERVENTION_APPLIED"
                    )
                    if intervention["control_intervention_label"] == arm_name:
                        trace[-1]["payload"]["final_output_hash"] = (
                            "sha256:" + "a" * 64
                        )

                attribution, trace, _ = self.wrong_route_delivery_result_for(
                    mutate_intervention_trace=mutate
                )
                self.assertEqual([], pilot.validate_trace(trace))
                self.assertEqual("F12", attribution["mechanism"])

    def test_wrong_route_intervention_declarations_are_fail_closed(self) -> None:
        attacks = (
            (
                "wrong_target_type",
                lambda packet: packet["intervention_runs"][0].update(
                    intervention_type="deliver_irrelevant_route"
                ),
            ),
            (
                "wrong_control_type",
                lambda packet: packet["intervention_runs"][1].update(
                    intervention_type="restore_required_route"
                ),
            ),
            (
                "empty_delta",
                lambda packet: packet["intervention_runs"][0].update(
                    delta_manifest=[]
                ),
            ),
            (
                "empty_held_constant",
                lambda packet: packet["intervention_runs"][1].update(
                    held_constant_manifest=[]
                ),
            ),
        )
        for attack_name, attack in attacks:
            with self.subTest(attack=attack_name):
                def mutate(packet: dict, _evidence: dict, attack=attack) -> None:
                    attack(packet)

                attribution, trace, _ = self.wrong_route_delivery_result_for(
                    mutate
                )
                self.assertEqual([], pilot.validate_trace(trace))
                self.assertEqual("F12", attribution["mechanism"])

    def test_duplicate_f4_intervention_arms_are_f12(self) -> None:
        for duplicate_index in (0, 1):
            with self.subTest(duplicate_index=duplicate_index):
                def mutate(
                    packet: dict, _evidence: dict, duplicate_index=duplicate_index
                ) -> None:
                    packet["intervention_runs"].append(
                        copy.deepcopy(packet["intervention_runs"][duplicate_index])
                    )

                attribution, trace, _ = self.wrong_route_delivery_result_for(
                    mutate
                )
                self.assertEqual([], pilot.validate_trace(trace))
                self.assertEqual("F12", attribution["mechanism"])

    def test_f4_requirement_must_match_locked_scenario_spec(self) -> None:
        def rehash_requirement(packet: dict) -> None:
            requirement = packet["route_requirement"]
            requirement["requirement_hash"] = pilot.sha256_digest(
                {
                    key: value
                    for key, value in requirement.items()
                    if key != "requirement_hash"
                }
            )

        def fabricated_route(packet: dict) -> None:
            route = "content.fabricated-route"
            packet["route_requirement"]["requested_route"] = route
            packet["intervention_runs"][0]["route_override"] = route
            packet["intervention_runs"][0]["delta_manifest"] = [
                f"route {route} delivered"
            ]
            rehash_requirement(packet)

        attacks = (
            ("route", fabricated_route),
            (
                "rationale",
                lambda packet: (
                    packet["route_requirement"].update(
                        requirement_rationale="Rehashed fabricated rationale."
                    ),
                    rehash_requirement(packet),
                ),
            ),
            (
                "predicate_order",
                lambda packet: (
                    packet["route_requirement"].update(
                        oracle_predicate_ids=["O003-X1", "O003-M1"]
                    ),
                    rehash_requirement(packet),
                ),
            ),
        )
        for attack_name, attack in attacks:
            with self.subTest(attack=attack_name):
                def mutate(packet: dict, _evidence: dict, attack=attack) -> None:
                    attack(packet)

                attribution, trace, _ = self.wrong_route_delivery_result_for(
                    mutate
                )
                self.assertEqual([], pilot.validate_trace(trace))
                self.assertEqual("F12", attribution["mechanism"])

    def test_f4_negative_control_route_must_match_locked_spec(self) -> None:
        def mutate(packet: dict, _evidence: dict) -> None:
            route = "content.fabricated-control"
            control = packet["intervention_runs"][1]
            control["route_override"] = route
            control["delta_manifest"] = [f"route {route} delivered"]

        attribution, trace, _ = self.wrong_route_delivery_result_for(mutate)

        self.assertEqual([], pilot.validate_trace(trace))
        self.assertEqual("F12", attribution["mechanism"])

    def test_opaque_wrong_route_resource_identity_is_f12(self) -> None:
        def mutate(trace: list[dict]) -> None:
            access = next(
                event
                for event in trace
                if event["event_type"] == "KNOWLEDGE_ACCESS"
            )
            access["payload"].update(
                route_index_hash="sha256:" + "1" * 64,
                resource_id="resource:opaque-wrong-route",
                resource_hash="sha256:" + "2" * 64,
                selector_hash="sha256:" + "3" * 64,
                extracted_content_hash="sha256:" + "4" * 64,
            )

        attribution, trace, _ = self.wrong_route_delivery_result_for(
            mutate_trace=mutate
        )

        self.assertEqual([], pilot.validate_trace(trace))
        self.assertEqual("F12", attribution["mechanism"])

    def test_intervention_contaminated_ordinary_wrong_route_is_f12(self) -> None:
        def mutate(trace: list[dict]) -> None:
            run_id = trace[0]["run_id"]
            route = "content.copy-editing"
            trace.insert(
                2,
                pilot.make_event(
                    run_id,
                    3,
                    "INTERVENTION_APPLIED",
                    {
                        "intervention_type": "restore_required_route",
                        "version_hash": "sha256:" + "5" * 64,
                        "injected_content_kind": "logical_route",
                        "injected_content_hash": pilot.sha256_digest(
                            {"route_id": route}
                        ),
                        "target": "COND-006",
                        "delta_manifest": [f"route {route} delivered"],
                        "held_constant_manifest": [
                            "scenario",
                            "oracle",
                            "model",
                            "tools",
                        ],
                        "control_intervention_label": "target",
                        "negative_control_reference": None,
                    },
                ),
            )

        attribution, trace, _ = self.wrong_route_delivery_result_for(
            mutate_trace=mutate
        )

        self.assertEqual([], pilot.validate_trace(trace))
        self.assertEqual("F12", attribution["mechanism"])

    def test_boundary_contaminated_ordinary_wrong_route_is_f12(self) -> None:
        def mutate(trace: list[dict]) -> None:
            run_id = trace[0]["run_id"]
            sealed_index = next(
                index
                for index, event in enumerate(trace)
                if event["event_type"] == "RUN_SEALED"
            )
            trace.insert(
                sealed_index,
                pilot.make_event(
                    run_id,
                    sealed_index + 1,
                    "BOUNDARY_TRANSFER",
                    {
                        "boundary_id": "BOUNDARY-F4-ORDINARY-CONTAMINANT",
                        "source_owner": "source-owner",
                        "destination_owner": "destination-owner",
                        "upstream_artifact_hash_ref": "sha256:" + "8" * 64,
                        "downstream_received_artifact_hash_ref": (
                            "sha256:" + "9" * 64
                        ),
                        "critical_assertion_ids": ["ASSERTION-CONTAMINANT"],
                        "transfer_status": "delivered",
                    },
                ),
            )

        attribution, trace, _ = self.wrong_route_delivery_result_for(
            mutate_trace=mutate
        )

        self.assertEqual([], pilot.validate_trace(trace))
        self.assertEqual("F12", attribution["mechanism"])

    def test_ordinary_output_seal_must_match_condition_candidate(self) -> None:
        def mutate(trace: list[dict]) -> None:
            trace[-1]["payload"]["final_output_hash"] = "sha256:" + "b" * 64

        attribution, trace, _ = self.wrong_route_delivery_result_for(
            mutate_trace=mutate
        )

        self.assertEqual([], pilot.validate_trace(trace))
        self.assertEqual("F12", attribution["mechanism"])

    def test_wrong_route_delivery_without_selective_repair_is_f12(self) -> None:
        def mutate(packet: dict, _evidence: dict) -> None:
            packet["intervention_runs"][0]["candidate_ref"] = "condition:COND-006"

        attribution, trace, _ = self.wrong_route_delivery_result_for(mutate)

        self.assertEqual([], pilot.validate_trace(trace))
        self.assertEqual("F12", attribution["mechanism"])

    def test_wrong_route_delivery_with_repaired_irrelevant_control_is_f12(self) -> None:
        def mutate(packet: dict, _evidence: dict) -> None:
            packet["intervention_runs"][1]["candidate_ref"] = "catalog:GOOD-003"

        attribution, trace, _ = self.wrong_route_delivery_result_for(mutate)

        self.assertEqual([], pilot.validate_trace(trace))
        self.assertEqual("F12", attribution["mechanism"])

    def test_wrong_route_delivery_with_activation_drift_is_f12(self) -> None:
        def mutate(packet: dict, evidence: dict) -> None:
            evidence["trace_profiles"]["inactive_route_delivered"] = {
                "activation": "not-activated",
                "access": "requested_delivered",
                "telemetry": "complete",
            }
            packet["intervention_runs"][0]["trace_profile"] = (
                "inactive_route_delivered"
            )

        attribution, trace, _ = self.wrong_route_delivery_result_for(mutate)

        self.assertEqual([], pilot.validate_trace(trace))
        self.assertEqual("F12", attribution["mechanism"])

    def test_wrong_route_delivery_with_incomplete_resource_evidence_is_f12(self) -> None:
        def mutate(trace: list[dict]) -> None:
            access = next(
                event
                for event in trace
                if event["event_type"] == "KNOWLEDGE_ACCESS"
            )
            del access["payload"]["resource_hash"]

        attribution, trace, _ = self.wrong_route_delivery_result_for(
            mutate_trace=mutate
        )

        self.assertTrue(pilot.validate_trace(trace))
        self.assertEqual("F12", attribution["mechanism"])

    def test_f5_requires_audited_omission_neutral_repair_and_placebo(self) -> None:
        self.assertEqual("F5", self.result_for("COND-007")["attribution"]["mechanism"])

    def test_f5_requires_the_correct_logical_route_to_remain_delivered(self) -> None:
        def mutate(packet: dict) -> None:
            packet["ordinary_trace_profile"] = "direct_complete"
            packet["local_content_audit"]["audited_resource_hash"] = pilot.sha256_digest(
                {"resource": "fixture:source-s-003"}
            )
            packet["local_content_audit"]["audit_seal"] = pilot.sha256_digest(
                {
                    key: value
                    for key, value in packet["local_content_audit"].items()
                    if key != "audit_seal"
                }
            )

        self.assertEqual("F12", self.result_for("COND-007", mutate)["attribution"]["mechanism"])

    def test_f5_rejects_forced_route_smuggling_in_owner_local_arms(self) -> None:
        cases = (
            ("COND-007", "content.consequential-strategy"),
            ("COND-017", "content.evidence-lineage"),
        )
        for condition_id, owner_route in cases:
            with self.subTest(condition_id=condition_id):
                def mutate(packet: dict, owner_route=owner_route) -> None:
                    for arm in packet["intervention_runs"]:
                        arm["route_override"] = owner_route

                result = self.result_for(condition_id, mutate)
                self.assertEqual("F12", result["attribution"]["mechanism"])

    def test_f5_requires_nonempty_independent_sealed_omission_audit(self) -> None:
        result = self.result_for(
            "COND-007",
            lambda packet: packet["local_content_audit"].update(
                missing_distinction="", auditor=""
            ),
        )
        self.assertEqual("F12", result["attribution"]["mechanism"])

    def test_f5_rejects_paraphrased_downstream_answer_tokens(self) -> None:
        def mutate(packet: dict) -> None:
            proposition = packet["neutral_artifact"]["propositions"][0]
            proposition["text"] = "Preserve the approved annual terms."
            proposition["semantic_tokens"] = ["preserve_approved_terms"]
            packet["purity_review"]["semantic_tokens"] = ["preserve_approved_terms"]
            packet["purity_review"]["reviewed_artifact_hash"] = pilot.sha256_digest(
                packet["neutral_artifact"]
            )

        self.assertEqual("F12", self.result_for("COND-007", mutate)["attribution"]["mechanism"])

    def test_f5_rejects_a_neutral_template_bound_to_another_scenario(self) -> None:
        def mutate(packet: dict) -> None:
            proposition = packet["neutral_artifact"]["propositions"][0]
            proposition.update(
                text="Derivative artifacts do not create independent source roots.",
                semantic_tokens=["derivative_lineage", "independent_root_distinction"],
            )
            packet["local_content_audit"].update(
                missing_distinction="derivative artifacts retain one source root",
                missing_distinction_tokens=[
                    "derivative_lineage",
                    "independent_root_distinction",
                ],
            )
            packet["local_content_audit"]["audit_seal"] = pilot.sha256_digest(
                {
                    key: value
                    for key, value in packet["local_content_audit"].items()
                    if key != "audit_seal"
                }
            )
            packet["purity_review"].update(
                semantic_tokens=["derivative_lineage", "independent_root_distinction"],
                reviewed_artifact_hash=pilot.sha256_digest(packet["neutral_artifact"]),
            )

        self.assertEqual("F12", self.result_for("COND-007", mutate)["attribution"]["mechanism"])

    def test_f5_injected_artifact_content_changes_intervention_hash_and_fails_closed(self) -> None:
        original = self.result_for("COND-007")

        def mutate(packet: dict) -> None:
            packet["neutral_artifact"]["propositions"][0]["text"] += " Mutated."
            packet["purity_review"]["reviewed_artifact_hash"] = pilot.sha256_digest(
                packet["neutral_artifact"]
            )

        changed = self.result_for("COND-007", mutate)
        original_event = next(
            event
            for event in original["counterfactual_evidence"]["intervention_runs"]["target"]["trace"]
            if event["event_type"] == "INTERVENTION_APPLIED"
        )
        changed_event = next(
            event
            for event in changed["counterfactual_evidence"]["intervention_runs"]["target"]["trace"]
            if event["event_type"] == "INTERVENTION_APPLIED"
        )
        self.assertNotEqual(
            original_event["payload"]["version_hash"], changed_event["payload"]["version_hash"]
        )
        self.assertEqual("F12", changed["attribution"]["mechanism"])

    def test_placebo_repair_cannot_establish_f5(self) -> None:
        result = self.result_for(
            "COND-007",
            lambda packet: packet["intervention_runs"][1].update(candidate_ref="catalog:GOOD-003"),
        )
        self.assertEqual("F12", result["attribution"]["mechanism"])

    def test_f6_requires_adequate_owners_and_answer_free_state_repair(self) -> None:
        self.assertEqual("F6", self.result_for("COND-008")["attribution"]["mechanism"])

    def test_f6_requires_exact_sealed_boundary_transfer_evidence(self) -> None:
        evidence = load_fixture("evidence-packets.json")
        packet = next(item for item in evidence["packets"] if item["condition_id"] == "COND-008")
        result = self.result_for("COND-008")
        boundary_events = [
            event for event in result["trace"] if event["event_type"] == "BOUNDARY_TRANSFER"
        ]

        self.assertEqual(1, len(boundary_events))
        self.assertEqual(
            {
                "boundary_id": packet["boundary_audit"]["boundary_id"],
                "source_owner": packet["boundary_audit"]["source_owner"],
                "destination_owner": packet["boundary_audit"]["destination_owner"],
                "upstream_artifact_hash_ref": packet["boundary_audit"]["upstream_artifact_hash"],
                "downstream_received_artifact_hash_ref": packet["boundary_audit"]["downstream_artifact_hash"],
                "critical_assertion_ids": packet["boundary_audit"]["required_assertion_ids"],
                "transfer_status": packet["boundary_audit"]["transfer_status"],
            },
            boundary_events[0]["payload"],
        )

    def test_f6_requires_route_and_resource_delivery_to_remain_held_constant(self) -> None:
        result = self.result_for(
            "COND-008",
            lambda packet: packet.update(ordinary_trace_profile="route_missing"),
        )
        self.assertEqual("F12", result["attribution"]["mechanism"])

    def test_f6_rejects_forced_route_smuggling_in_state_arms(self) -> None:
        for condition_id in ("COND-008", "COND-018"):
            with self.subTest(condition_id=condition_id):
                def mutate(packet: dict) -> None:
                    for arm in packet["intervention_runs"]:
                        arm["route_override"] = "content.consequential-strategy"

                result = self.result_for(condition_id, mutate)
                self.assertEqual("F12", result["attribution"]["mechanism"])

    def test_f5_and_f6_require_one_causal_intervention_event_per_run(self) -> None:
        def late_intervention(trace: list[dict]) -> None:
            intervention = next(
                event
                for event in trace
                if event["event_type"] == "INTERVENTION_APPLIED"
            )
            trace.remove(intervention)
            sealed_index = next(
                index
                for index, event in enumerate(trace)
                if event["event_type"] == "RUN_SEALED"
            )
            trace.insert(sealed_index, intervention)

        def duplicate_intervention(trace: list[dict]) -> None:
            intervention_index = next(
                index
                for index, event in enumerate(trace)
                if event["event_type"] == "INTERVENTION_APPLIED"
            )
            trace.insert(
                intervention_index + 1,
                copy.deepcopy(trace[intervention_index]),
            )

        for condition_id in ("COND-007", "COND-017", "COND-008", "COND-018"):
            for attack in (late_intervention, duplicate_intervention):
                with self.subTest(
                    condition_id=condition_id, attack=attack.__name__
                ):
                    result = self.result_with_mutated_intervention_trace(
                        condition_id, attack
                    )
                    self.assertEqual("F12", result["attribution"]["mechanism"])

    def test_f4_f5_and_f6_require_activation_to_remain_held_constant(self) -> None:
        cases = load_fixture("pilot-cases.json")
        for condition_id in ("COND-006", "COND-007", "COND-017", "COND-008", "COND-018"):
            evidence = load_fixture("evidence-packets.json")
            evidence["trace_profiles"]["inactive_route_delivered"] = {
                "activation": "not-activated",
                "access": "requested_delivered",
                "telemetry": "complete",
            }
            packet = next(
                item for item in evidence["packets"] if item["condition_id"] == condition_id
            )
            for arm in packet["intervention_runs"]:
                arm["trace_profile"] = "inactive_route_delivered"

            result = next(
                item
                for item in pilot.evaluate_and_seal(cases, evidence)["condition_results"]
                if item["condition_id"] == condition_id
            )

            with self.subTest(condition_id=condition_id):
                self.assertEqual("F12", result["attribution"]["mechanism"])

    def test_f4_f5_and_f6_require_run_bound_invariants(self) -> None:
        drift_fields = (
            "delivered_visible_input_digest",
            "common_scaffold_digest",
            "model_configuration_digest",
            "tools_permissions_digest",
            "external_evidence_digest",
        )
        for condition_id in ("COND-006", "COND-007", "COND-008"):
            for index, field in enumerate(drift_fields, start=1):
                with self.subTest(condition_id=condition_id, field=field):
                    def mutate(
                        trace: list[dict], field=field, index=index
                    ) -> None:
                        intervention = next(
                            event["payload"]
                            for event in trace
                            if event["event_type"] == "INTERVENTION_APPLIED"
                        )
                        if intervention["control_intervention_label"] != "target":
                            return
                        run_bound = next(
                            event
                            for event in trace
                            if event["event_type"] == "RUN_BOUND"
                        )
                        run_bound["payload"][field] = (
                            "sha256:" + str(index) * 64
                        )

                    result = self.result_with_mutated_intervention_trace(
                        condition_id, mutate
                    )
                    self.assertEqual("F12", result["attribution"]["mechanism"])

    def test_unobservable_or_unsafe_handoff_returns_f12(self) -> None:
        self.assertEqual("F12", self.result_for("COND-010")["attribution"]["mechanism"])

    def test_answer_bearing_state_capsule_cannot_establish_f6(self) -> None:
        result = self.result_for(
            "COND-008",
            lambda packet: packet["state_capsule"].update(contains_recommendation=True),
        )
        self.assertEqual("F12", result["attribution"]["mechanism"])

    def test_f6_rejects_packet_defined_schema_and_empty_assertions(self) -> None:
        def mutate(packet: dict) -> None:
            packet["boundary_audit"]["required_assertion_ids"] = []
            packet["boundary_contract"]["state_field_names"] = ["preserve_approved_terms"]
            packet["state_capsule"]["schema"] = ["preserve_approved_terms"]
            packet["state_capsule"]["values"] = ["present"]

        self.assertEqual("F12", self.result_for("COND-008", mutate)["attribution"]["mechanism"])

    def test_f6_capsule_content_changes_intervention_hash_and_fails_closed(self) -> None:
        original = self.result_for("COND-008")
        changed = self.result_for(
            "COND-008",
            lambda packet: packet["state_capsule"].update(values=["unknown", "unknown", "unknown"]),
        )
        original_event = next(
            event
            for event in original["counterfactual_evidence"]["intervention_runs"]["target"]["trace"]
            if event["event_type"] == "INTERVENTION_APPLIED"
        )
        changed_event = next(
            event
            for event in changed["counterfactual_evidence"]["intervention_runs"]["target"]["trace"]
            if event["event_type"] == "INTERVENTION_APPLIED"
        )
        self.assertNotEqual(
            original_event["payload"]["version_hash"], changed_event["payload"]["version_hash"]
        )
        self.assertEqual("F12", changed["attribution"]["mechanism"])

    def test_mixed_matched_runs_preempt_mechanism_with_f2(self) -> None:
        self.assertEqual("F2", self.result_for("COND-011")["attribution"]["mechanism"])

    def test_repeat_output_seals_must_match_resolved_candidates(self) -> None:
        cases = load_fixture("pilot-cases.json")
        evidence = load_fixture("evidence-packets.json")
        original_builder = pilot._build_evidence_trace

        def build_with_mutation(*args, **kwargs):
            trace = original_builder(*args, **kwargs)
            run_suffix = args[5] if len(args) > 5 else kwargs.get("run_suffix", "")
            if str(run_suffix).startswith("REPEAT-011-"):
                trace[-1]["payload"]["final_output_hash"] = (
                    "sha256:" + "c" * 64
                )
                trace = reseal_trace(trace)
            return trace

        with mock.patch.object(
            pilot, "_build_evidence_trace", side_effect=build_with_mutation
        ):
            sealed = pilot.evaluate_and_seal(cases, evidence)
        result = next(
            item
            for item in sealed["condition_results"]
            if item["condition_id"] == "COND-011"
        )

        self.assertEqual("F12", result["attribution"]["mechanism"])

    def test_stable_opposing_ab_arms_are_not_misclassified_as_f2(self) -> None:
        def mutate(packet: dict) -> None:
            for arm in packet["repeat_arms"]:
                candidate_ref = (
                    "catalog:GOOD-005"
                    if arm["condition"] == "without_skill"
                    else "condition:COND-014"
                )
                for run in arm["runs"]:
                    run["candidate_ref"] = candidate_ref

        self.assertEqual("F12", self.result_for("COND-014", mutate)["attribution"]["mechanism"])

    def test_f1_preempts_system_attribution(self) -> None:
        self.assertEqual("F1", self.result_for("COND-003")["attribution"]["mechanism"])

    def test_missing_operational_telemetry_returns_f12(self) -> None:
        self.assertEqual("F12", self.result_for("COND-019")["attribution"]["mechanism"])

    def test_out_of_scope_authoritative_dependency_supports_f10(self) -> None:
        result = self.result_for("COND-016")["attribution"]
        self.assertEqual("F10", result["mechanism"])
        self.assertEqual(["F9"], result["behavioral_tags"])

    def test_empty_or_unbound_external_dependency_cannot_establish_f10(self) -> None:
        result = self.result_for(
            "COND-016",
            lambda packet: packet.update(
                external_dependency={
                    "dependency_id": "",
                    "authority": "",
                    "availability": "outside_executor_scope",
                    "material_predicate_ids": [],
                    "evidence_ref": "missing",
                },
                dependency_records=[],
            ),
        )
        self.assertEqual("F12", result["attribution"]["mechanism"])

    def test_authority_tag_requires_an_authority_predicate_violation(self) -> None:
        cases = load_fixture("pilot-cases.json")
        evidence = load_fixture("evidence-packets.json")
        condition = next(item for item in cases["conditions"] if item["condition_id"] == "COND-015")
        condition["candidate"]["semantic_slots"]["A"] = ["approval_owner_controls"]
        result = next(
            item
            for item in pilot.evaluate_and_seal(cases, evidence)["condition_results"]
            if item["condition_id"] == "COND-015"
        )
        self.assertNotIn("F9", result["attribution"]["behavioral_tags"])


class ArchitectureGateTests(unittest.TestCase):
    def test_f11_target_and_control_arms_must_be_nonempty_and_stable(self) -> None:
        rejected = {
            "telemetry": "complete",
            "trace_errors": [],
            "judgments": [{"overall": "unacceptable"}, {"overall": "unacceptable"}],
        }
        accepted = {
            "telemetry": "complete",
            "trace_errors": [],
            "judgments": [{"overall": "acceptable"}, {"overall": "acceptable"}],
        }

        self.assertFalse(pilot._f11_arm_stably_rejected(None))
        self.assertFalse(pilot._f11_arm_stably_rejected({"stability_runs": []}))
        self.assertFalse(
            pilot._f11_arm_stably_rejected({"stability_runs": [rejected, accepted]})
        )
        self.assertTrue(
            pilot._f11_arm_stably_rejected({"stability_runs": [rejected, rejected]})
        )

    def test_f11_adjudicator_must_be_separate_from_all_material_roles(self) -> None:
        scenario_result = {
            "contract_author": "contract-author",
            "independent_validator": "validator",
            "scenario_role_identities": {
                "scenario_editor": "scenario-editor",
                "oracle_author": "oracle-author",
            },
        }
        actual = {
            "judgments": [{"judge_id": "judge-a"}, {"judge_id": "judge-b"}],
            "authorship_identities": {
                "candidate_author": "candidate-author",
                "intervention_authors": ["intervention-author"],
                "proposed_fix_authors": ["fix-author"],
            },
        }
        for adjudicator in (
            "contract-author",
            "validator",
            "scenario-editor",
            "oracle-author",
            "judge-a",
            "candidate-author",
            "intervention-author",
            "fix-author",
        ):
            adjudication = {
                "independent": True,
                "disposition": "irreducible_collapse_confirmed",
                "adjudicator_id": adjudicator,
            }
            adjudication["adjudication_seal"] = pilot.sha256_digest(adjudication)
            actual["independent_adjudication"] = adjudication
            with self.subTest(adjudicator=adjudicator):
                self.assertFalse(
                    pilot._f11_independent_adjudication_valid(actual, scenario_result)
                )

    def test_false_f11_cannot_pass_when_cheaper_repair_exists(self) -> None:
        dossier = {name: True for name in pilot.F11_REQUIREMENTS}
        dossier["cheaper_repair_succeeded"] = True
        result = pilot.evaluate_f11_gate(dossier)
        self.assertFalse(result["research_reopening"])
        self.assertIn("cheaper_repair_defeats_f11", result["missing"])

    def test_f11_rejects_self_hashed_records_not_bound_to_sealed_evaluation(self) -> None:
        dossier = {name: True for name in pilot.F11_REQUIREMENTS}
        dossier["scenario_refs"] = ["CASE-A@1.0.0", "CASE-B@1.0.0"]
        dossier["evidence_refs"] = {
            "oracle_attack_refs": ["oa-1", "oa-2"],
            "recurrence_run_refs": ["run-1", "run-2", "run-3"],
            "lineage_refs": ["lineage-1", "lineage-2"],
            "owner_boundary_refs": ["owner-1", "owner-2"],
            "activation_access_trace_refs": ["trace-1"],
            "intervention_refs": ["intervention-1", "intervention-2"],
            "negative_control_refs": ["control-1"],
            "collapse_witness_refs": ["collapse-1"],
            "adjudication_refs": ["adjudication-1"],
        }
        dossier["cheaper_repair_succeeded"] = False
        type_by_group = {
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
        records = {}
        for group, references in dossier["evidence_refs"].items():
            for index, reference in enumerate(references):
                records[reference] = {
                    "record_id": reference,
                    "record_type": type_by_group[group],
                    "scenario_ref": dossier["scenario_refs"][index % 2],
                    "condition_id": f"COND-F11-{index}",
                    "lineage_id": f"LINEAGE-{index}" if group in {"recurrence_run_refs", "lineage_refs"} else None,
                    "owner_id": f"OWNER-{index}" if group == "owner_boundary_refs" else None,
                    "telemetry": "complete" if group == "activation_access_trace_refs" else None,
                    "arm": "target" if group == "intervention_refs" else None,
                    "stable": True if group == "negative_control_refs" else None,
                    "irreducible": True if group == "collapse_witness_refs" else None,
                    "independent": True if group == "adjudication_refs" else None,
                }
                records[reference]["record_seal"] = pilot.sha256_digest(records[reference])
        result = pilot.evaluate_f11_gate(dossier, {"records": records})
        self.assertFalse(result["research_reopening"])
        self.assertIn("referenced_evidence_incomplete", result["missing"])

    def test_f11_rejects_duplicated_untyped_or_unsealed_evidence(self) -> None:
        dossier = {name: True for name in pilot.F11_REQUIREMENTS}
        dossier.update(
            {
                "scenario_refs": ["CASE-A@1.0.0"],
                "cheaper_repair_succeeded": False,
                "evidence_refs": {
                    group: ["FAKE"] * minimum
                    for group, minimum in pilot.F11_REFERENCE_REQUIREMENTS.items()
                },
            }
        )
        result = pilot.evaluate_f11_gate(
            dossier,
            {"records": {"FAKE": {"sealed": False, "record_type": "unrelated"}}},
        )
        self.assertFalse(result["research_reopening"])
        self.assertIn("referenced_evidence_incomplete", result["missing"])

    def test_f11_rejects_bound_conditions_that_prove_cheaper_local_repairs(self) -> None:
        sealed = pilot.evaluate_and_seal(
            load_fixture("pilot-cases.json"), load_fixture("evidence-packets.json")
        )
        condition_ids = ["COND-007", "COND-017"]
        condition_results = [
            next(item for item in sealed["condition_results"] if item["condition_id"] == condition_id)
            for condition_id in condition_ids
        ]
        scenario_refs = [item["scenario_ref"] for item in condition_results]
        scenario_results = [
            next(item for item in sealed["scenario_results"] if item["scenario_ref"] == scenario_ref)
            for scenario_ref in scenario_refs
        ]
        dossier = {name: True for name in pilot.F11_REQUIREMENTS}
        dossier.update(
            scenario_refs=scenario_refs,
            cheaper_repair_succeeded=False,
            evidence_refs={
                "oracle_attack_refs": ["oa-1", "oa-2"],
                "recurrence_run_refs": ["run-1", "run-2", "run-3"],
                "lineage_refs": ["lineage-1", "lineage-2"],
                "owner_boundary_refs": ["owner-1", "owner-2"],
                "activation_access_trace_refs": ["trace-1"],
                "intervention_refs": ["intervention-1", "intervention-2"],
                "negative_control_refs": ["control-1"],
                "collapse_witness_refs": ["collapse-1"],
                "adjudication_refs": ["adjudication-1"],
            },
        )
        type_by_group = {
            group: pilot.F11_RECORD_TYPES[group] for group in pilot.F11_REFERENCE_REQUIREMENTS
        }
        records = {}
        record_number = 0
        for group, references in dossier["evidence_refs"].items():
            for reference in references:
                index = record_number % 2
                condition_result = condition_results[index]
                scenario_result = scenario_results[index]
                record = {
                    "record_id": reference,
                    "record_type": type_by_group[group],
                    "scenario_ref": scenario_refs[index],
                    "condition_id": condition_result["condition_id"],
                    "scenario_result_hash": pilot.sha256_digest(scenario_result),
                    "condition_result_hash": pilot.sha256_digest(condition_result),
                    "evidence_object_hash": pilot._f11_evidence_object_hash(
                        type_by_group[group], scenario_result, condition_result
                    ),
                    "lineage_id": f"LINEAGE-{index}" if group in {"recurrence_run_refs", "lineage_refs"} else None,
                    "owner_id": f"OWNER-{index}" if group == "owner_boundary_refs" else None,
                    "telemetry": "complete" if group == "activation_access_trace_refs" else None,
                    "arm": "target" if group == "intervention_refs" else None,
                    "stable": True if group == "negative_control_refs" else None,
                    "irreducible": True if group == "collapse_witness_refs" else None,
                    "independent": True if group == "adjudication_refs" else None,
                }
                record["record_seal"] = pilot.sha256_digest(record)
                records[reference] = record
                record_number += 1
        context_material = {
            "scenario_results": scenario_results,
            "condition_results": condition_results,
            "pair_results": [],
            "records": records,
        }
        context = {
            **context_material,
            "evaluation_evidence_seal": pilot.sha256_digest(context_material),
        }

        result = pilot.evaluate_f11_gate(dossier, context)

        self.assertFalse(result["research_reopening"])
        self.assertIn("cheaper_repair_defeats_f11", result["missing"])


class PilotDeckTests(unittest.TestCase):
    def test_deck_has_exact_frozen_visible_count_lane_split_and_versions(self) -> None:
        cases = load_fixture("pilot-cases.json")
        scenarios = cases["scenarios"]
        self.assertEqual(14, len(scenarios))
        lanes = collections.Counter(case["lane"] for case in scenarios)
        self.assertEqual(
            {"diagnostic_injection": 12, "clean_room_independence": 2},
            dict(lanes),
        )
        actual = [
            f"{case['identity_version']['scenario_id']}@{case['identity_version']['scenario_version']}"
            for case in scenarios
        ]
        self.assertEqual(
            [
                "PD-DI-001@1.0.0",
                "PD-DI-001@2.0.0",
                "PD-DI-002@1.0.0",
                "PD-DI-003@1.0.0",
                "PD-DI-004-A@1.0.0",
                "PD-DI-004-B@1.0.0",
                "PD-DI-005@1.0.0",
                "PD-DI-006@1.0.0",
                "PD-DI-007@1.0.0",
                "PD-DI-008@1.0.0",
                "PD-DI-009@1.0.0",
                "PD-DI-010@1.0.0",
                "PD-CR-001@1.0.0",
                "PD-CR-002@1.0.0",
            ],
            actual,
        )

    def test_every_materialized_scenario_satisfies_seven_block_schema(self) -> None:
        cases = load_fixture("pilot-cases.json")
        for scenario in cases["scenarios"]:
            reference = (
                f"{scenario['identity_version']['scenario_id']}@"
                f"{scenario['identity_version']['scenario_version']}"
            )
            with self.subTest(reference=reference):
                self.assertEqual([], pilot.validate_scenario(scenario))

    def test_planted_labels_do_not_leak_to_evaluator_visible_artifacts(self) -> None:
        cases = load_fixture("pilot-cases.json")
        for scenario in cases["scenarios"]:
            scenario["external_provenance"]["source_class"] = "source-class-redacted-for-label-scan"
        visible = json.dumps(cases, ensure_ascii=False).lower()
        planting = load_fixture("planting-key.json")
        for forbidden in planting["forbidden_visible_labels"]:
            with self.subTest(forbidden=forbidden):
                self.assertNotIn(f'"{forbidden.lower()}"', visible)

    def test_planted_labels_do_not_appear_as_tokens_inside_visible_strings(self) -> None:
        cases = load_fixture("pilot-cases.json")
        evidence = load_fixture("evidence-packets.json")
        planting = load_fixture("planting-key.json")
        visible_strings = list(pilot._string_values({"cases": cases, "evidence": evidence}))
        for forbidden in planting["forbidden_visible_labels"]:
            with self.subTest(forbidden=forbidden):
                pattern = re.compile(
                    rf"(?<![a-z0-9]){re.escape(forbidden.lower())}(?![a-z0-9])",
                    re.IGNORECASE,
                )
                self.assertFalse(
                    any(pattern.search(value) for value in visible_strings)
                )

    def test_clean_room_cases_have_attestations_independent_roots_and_mapping_status(self) -> None:
        cases = load_fixture("pilot-cases.json")
        clean = [
            case for case in cases["scenarios"] if case["lane"] == "clean_room_independence"
        ]
        self.assertTrue(
            all(
                case["external_provenance"]["framework_access_attestation"]
                == "no_repository_access_before_lock"
                for case in clean
            )
        )

    def test_clean_room_construction_records_three_distinct_prelock_roles(self) -> None:
        clean = [
            case
            for case in load_fixture("pilot-cases.json")["scenarios"]
            if case["lane"] == "clean_room_independence"
        ]
        for case in clean:
            roles = case["external_provenance"]["role_attestations"]
            self.assertEqual(
                {"source_curator", "scenario_editor", "oracle_author"}, set(roles)
            )
            self.assertEqual(3, len({record["identity"] for record in roles.values()}))
            self.assertTrue(
                all(record["repository_access"] == "none_before_lock" for record in roles.values())
            )
        roots = {case["identity_version"]["provenance_root_id"] for case in clean}
        self.assertEqual(2, len(roots))
        self.assertTrue(
            any(
                case.get("post_lock_mapping", {}).get("status")
                in {"unmapped", "multiply_mapped"}
                for case in clean
            )
        )

    def test_rejected_scenario_remains_in_deck(self) -> None:
        scenarios = load_fixture("pilot-cases.json")["scenarios"]
        rejected = [
            scenario
            for scenario in scenarios
            if pilot.validity_disposition(scenario)["disposition"] == "REJECT"
        ]
        self.assertEqual(["PD-DI-001@1.0.0"], [
            f"{item['identity_version']['scenario_id']}@{item['identity_version']['scenario_version']}"
            for item in rejected
        ])

    def test_fixture_judges_are_not_misrepresented_as_humans(self) -> None:
        judges = load_fixture("pilot-cases.json")["fixture_judges"]
        self.assertEqual(2, len(judges))
        self.assertTrue(all(judge["judge_kind"] == "deterministic_fixture" for judge in judges))

    def test_source_snapshots_are_content_addressable_summaries(self) -> None:
        snapshots = load_fixture("source-snapshots.json")["snapshots"]
        self.assertEqual(2, len(snapshots))
        self.assertEqual(2, len({snapshot["provenance_root_id"] for snapshot in snapshots}))
        for snapshot in snapshots:
            self.assertGreaterEqual(len(snapshot["source_references"]), 1)
            self.assertEqual(
                "no_repository_access_before_lock",
                snapshot["framework_access_attestation"],
            )
            self.assertEqual(
                snapshot["snapshot_hash"],
                pilot.sha256_digest(
                    {key: value for key, value in snapshot.items() if key != "snapshot_hash"}
                ),
            )

    def test_snapshot_hash_covers_sources_and_classification_not_only_summary(self) -> None:
        snapshot = load_fixture("source-snapshots.json")["snapshots"][0]
        envelope = {key: value for key, value in snapshot.items() if key != "snapshot_hash"}
        changed_source = copy.deepcopy(envelope)
        changed_source["source_references"][0]["date"] = "2099-01-01"
        changed_class = copy.deepcopy(envelope)
        changed_class["source_class"] = "P9"

        self.assertNotEqual(pilot.sha256_digest(envelope), pilot.sha256_digest(changed_source))
        self.assertNotEqual(pilot.sha256_digest(envelope), pilot.sha256_digest(changed_class))

    def test_clean_room_snapshots_bind_to_cases_without_historical_answer_leakage(self) -> None:
        cases = load_fixture("pilot-cases.json")
        snapshots = {
            item["snapshot_id"]: item
            for item in load_fixture("source-snapshots.json")["snapshots"]
        }
        clean = [
            item
            for item in cases["scenarios"]
            if item["lane"] == "clean_room_independence"
        ]
        for scenario in clean:
            provenance = scenario["external_provenance"]
            snapshot = snapshots[provenance["raw_source_snapshot_ref"]]
            self.assertEqual(provenance["source_class"], snapshot["source_class"])
            self.assertEqual(
                scenario["identity_version"]["provenance_root_id"],
                snapshot["provenance_root_id"],
            )
            self.assertEqual(
                provenance["decision_time_cutoff"],
                snapshot["snapshot_material"]["decision_time_cutoff"],
            )
            self.assertEqual(provenance["raw_source_snapshot_hash"], snapshot["snapshot_hash"])
            self.assertNotIn("decision", snapshot["snapshot_material"])
            self.assertTrue(
                all(
                    reference["executor_visibility"] == "sealed_evaluator_only"
                    for reference in snapshot["source_references"]
                )
            )
            self.assertEqual(
                [f"executor snapshot material {snapshot['executor_visible_material_ref']}"],
                scenario["user_visible_package"]["tools_external_evidence"],
            )


class PilotIntegrationTests(unittest.TestCase):
    def test_persisted_reports_match_a_fresh_deterministic_render(self) -> None:
        report = pilot.run_pilot(PILOT_ROOT)
        self.assertEqual(
            report,
            json.loads((PILOT_ROOT / "results" / "pilot-report.json").read_text(encoding="utf-8")),
        )
        self.assertEqual(
            pilot.render_markdown(report),
            (PILOT_ROOT / "results" / "pilot-report.md").read_text(encoding="utf-8"),
        )

    def test_validation_rejects_stale_persisted_reports(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            shutil.copytree(PILOT_ROOT / "fixtures", root / "fixtures")
            (root / "results").mkdir()
            (root / "results" / "pilot-report.json").write_text("{}\n", encoding="utf-8")
            (root / "results" / "pilot-report.md").write_text("stale\n", encoding="utf-8")

            errors = pilot.validate_pilot(root)

        self.assertIn("persisted JSON report is stale", errors)
        self.assertIn("persisted Markdown report is stale", errors)

    def test_material_attribution_inputs_are_retained_and_change_evaluation_seal(self) -> None:
        cases = load_fixture("pilot-cases.json")
        evidence = load_fixture("evidence-packets.json")
        original = pilot.evaluate_and_seal(cases, evidence)
        changed_evidence = copy.deepcopy(evidence)
        packet = next(
            item for item in changed_evidence["packets"] if item["condition_id"] == "COND-007"
        )
        packet["local_content_audit"]["auditor"] = "independent-auditor-replacement"
        packet["local_content_audit"]["audit_seal"] = pilot.sha256_digest(
            {
                key: value
                for key, value in packet["local_content_audit"].items()
                if key != "audit_seal"
            }
        )
        changed = pilot.evaluate_and_seal(cases, changed_evidence)
        original_result = next(
            item for item in original["condition_results"] if item["condition_id"] == "COND-007"
        )
        changed_result = next(
            item for item in changed["condition_results"] if item["condition_id"] == "COND-007"
        )

        self.assertEqual("F5", changed_result["attribution"]["mechanism"])
        self.assertNotEqual(original_result["evidence_packet_hash"], changed_result["evidence_packet_hash"])
        self.assertNotEqual(original["evaluation_seal"], changed["evaluation_seal"])
        self.assertEqual(
            "independent-auditor-replacement",
            changed_result["counterfactual_evidence"]["local_content_audit"]["auditor"],
        )

    def test_condition_outcome_is_governed_by_judgments_not_a_planted_boolean(self) -> None:
        cases = load_fixture("pilot-cases.json")
        evidence = load_fixture("evidence-packets.json")
        mutated = copy.deepcopy(cases)
        condition = next(
            item for item in mutated["conditions"] if item["condition_id"] == "COND-004"
        )
        condition["candidate"]["semantic_slots"]["D"] = ["change_approved_terms"]

        sealed = pilot.evaluate_and_seal(mutated, evidence)
        result = next(
            item
            for item in sealed["condition_results"]
            if item["condition_id"] == "COND-004"
        )

        self.assertTrue(all(j["overall"] == "unacceptable" for j in result["judgments"]))
        self.assertNotEqual("NO_FAILURE", result["attribution"]["mechanism"])

    def test_visible_case_deck_contains_no_conclusion_equivalent_attribution_flags(self) -> None:
        cases = load_fixture("pilot-cases.json")
        self.assertNotIn("attribution_defaults", cases)
        for condition in cases["conditions"]:
            self.assertNotIn("attribution_overrides", condition)
            self.assertNotIn("behavioral_observations", condition)
            self.assertNotIn("trace_complete", condition)

    def test_incomplete_telemetry_preempts_mixed_repeat_attribution(self) -> None:
        cases = load_fixture("pilot-cases.json")
        evidence = load_fixture("evidence-packets.json")
        mutated = copy.deepcopy(evidence)
        packet = next(
            item for item in mutated["packets"] if item["condition_id"] == "COND-011"
        )
        packet["ordinary_trace_profile"] = "telemetry_incomplete"

        sealed = pilot.evaluate_and_seal(cases, mutated)
        result = next(
            item
            for item in sealed["condition_results"]
            if item["condition_id"] == "COND-011"
        )

        self.assertEqual("F12", result["attribution"]["mechanism"])

    def test_incomplete_target_or_control_telemetry_blocks_mechanism_attribution(self) -> None:
        cases = load_fixture("pilot-cases.json")
        evidence = load_fixture("evidence-packets.json")
        for condition_id in ("COND-006", "COND-007", "COND-008"):
            mutated = copy.deepcopy(evidence)
            packet = next(item for item in mutated["packets"] if item["condition_id"] == condition_id)
            packet["intervention_runs"][0]["trace_profile"] = "telemetry_incomplete"
            sealed = pilot.evaluate_and_seal(cases, mutated)
            result = next(item for item in sealed["condition_results"] if item["condition_id"] == condition_id)
            with self.subTest(condition_id=condition_id):
                self.assertEqual("F12", result["attribution"]["mechanism"])

    def test_f4_target_must_deliver_the_exact_required_route(self) -> None:
        cases = load_fixture("pilot-cases.json")
        evidence = load_fixture("evidence-packets.json")
        packet = next(item for item in evidence["packets"] if item["condition_id"] == "COND-006")
        packet["intervention_runs"][0]["route_override"] = "content.copy-editing"
        result = next(
            item
            for item in pilot.evaluate_and_seal(cases, evidence)["condition_results"]
            if item["condition_id"] == "COND-006"
        )
        self.assertEqual("F12", result["attribution"]["mechanism"])

    def test_f5_rejects_neutral_artifact_containing_a_downstream_answer(self) -> None:
        cases = load_fixture("pilot-cases.json")
        evidence = load_fixture("evidence-packets.json")
        packet = next(item for item in evidence["packets"] if item["condition_id"] == "COND-007")
        packet["neutral_artifact"]["propositions"][0]["semantic_tokens"] = ["preserve_approved_terms"]
        result = next(
            item
            for item in pilot.evaluate_and_seal(cases, evidence)["condition_results"]
            if item["condition_id"] == "COND-007"
        )
        self.assertEqual("F12", result["attribution"]["mechanism"])

    def test_f6_rejects_capsule_fields_outside_the_strict_owner_schema(self) -> None:
        cases = load_fixture("pilot-cases.json")
        evidence = load_fixture("evidence-packets.json")
        packet = next(item for item in evidence["packets"] if item["condition_id"] == "COND-008")
        packet["state_capsule"]["downstream_answer"] = "preserve_approved_terms"
        result = next(
            item
            for item in pilot.evaluate_and_seal(cases, evidence)["condition_results"]
            if item["condition_id"] == "COND-008"
        )
        self.assertEqual("F12", result["attribution"]["mechanism"])

    def test_evidence_free_all_true_f11_dossier_is_rejected(self) -> None:
        dossier = {name: True for name in pilot.F11_REQUIREMENTS}
        dossier["dossier_id"] = "DOSSIER-BOOLEAN-ONLY"
        dossier["cheaper_repair_succeeded"] = False

        result = pilot.evaluate_f11_gate(dossier, evidence_context={})

        self.assertFalse(result["research_reopening"])
        self.assertIn("referenced_evidence_incomplete", result["missing"])

    def test_material_interventions_contain_outputs_and_controls(self) -> None:
        evidence = load_fixture("evidence-packets.json")
        packets = {item["condition_id"]: item for item in evidence["packets"]}

        self.assertEqual(2, len(packets["COND-003"]["rubric_challenge"]["oracles"]))
        self.assertEqual(2, len(packets["COND-003"]["rubric_challenge"]["anchors"]))
        for condition_id in ("COND-011", "COND-014"):
            repeat_arms = packets[condition_id]["repeat_arms"]
            self.assertEqual({"A", "B"}, {item["arm"] for item in repeat_arms})
            self.assertEqual(
                {"without_skill", "with_skill"},
                {item["condition"] for item in repeat_arms},
            )
            self.assertTrue(all(len(item["runs"]) == 3 for item in repeat_arms))
            baseline = next(item for item in repeat_arms if item["condition"] == "without_skill")
            self.assertTrue(all(run["trace_profile"] == "baseline_direct" for run in baseline["runs"]))
            self.assertNotIn("repeat_runs", packets[condition_id])
        for condition_id in ("COND-006", "COND-007", "COND-008"):
            with self.subTest(condition_id=condition_id):
                interventions = packets[condition_id]["intervention_runs"]
                self.assertEqual({"target", "negative_control"}, {x["arm"] for x in interventions})
                self.assertTrue(all("candidate_ref" in x for x in interventions))

    def test_repeat_evidence_materializes_three_traces_for_each_ab_condition(self) -> None:
        sealed = pilot.evaluate_and_seal(
            load_fixture("pilot-cases.json"), load_fixture("evidence-packets.json")
        )
        for condition_id in ("COND-011", "COND-014"):
            result = next(
                item for item in sealed["condition_results"] if item["condition_id"] == condition_id
            )
            records = result["counterfactual_evidence"]["repeat_arms"]
            self.assertEqual(6, len(records))
            self.assertEqual(
                {"without_skill": 3, "with_skill": 3},
                dict(collections.Counter(record["condition"] for record in records)),
            )
            for record in records:
                activation = next(
                    event for event in record["trace"] if event["event_type"] == "SKILL_ACTIVATION"
                )["payload"]
                self.assertEqual(record["condition"], activation["intended_condition"])
                if record["condition"] == "without_skill":
                    self.assertEqual("not-intended", activation["outcome"])
                    self.assertIsNone(activation["requested_skill_id"])
                else:
                    self.assertEqual("activated", activation["outcome"])

    def test_f2_fails_closed_when_exact_two_by_three_packet_shape_is_broken(self) -> None:
        cases = load_fixture("pilot-cases.json")
        evidence = load_fixture("evidence-packets.json")
        packet = next(item for item in evidence["packets"] if item["condition_id"] == "COND-014")
        packet["repeat_arms"] = [packet["repeat_arms"][0]]
        packet["repeat_arms"][0]["runs"] = packet["repeat_arms"][0]["runs"][:2]
        result = next(
            item
            for item in pilot.evaluate_and_seal(cases, evidence)["condition_results"]
            if item["condition_id"] == "COND-014"
        )
        self.assertEqual("F12", result["attribution"]["mechanism"])

    def test_trace_rejects_forged_event_ids_and_duplicate_boundaries(self) -> None:
        trace = pilot.seal_trace(
            valid_unsealed_trace(),
            "sha256:" + "d" * 64,
            "complete",
            "2026-08-24T00:01:00Z",
        )
        forged = copy.deepcopy(trace)
        forged[1]["event_id"] = "forged"
        duplicate = copy.deepcopy(trace)
        duplicate.insert(1, copy.deepcopy(duplicate[0]))
        for index, event in enumerate(duplicate, start=1):
            event["sequence"] = index
            event["event_id"] = f"{event['run_id']}:{index:04d}:{event['event_type']}"
            event["payload_digest"] = pilot.sha256_digest(event["payload"])
        duplicate[-1]["payload"]["event_count"] = len(duplicate)
        duplicate[-1]["payload"]["ordered_trace_root_hash"] = pilot._trace_root(duplicate[:-1])
        duplicate[-1]["payload_digest"] = pilot.sha256_digest(duplicate[-1]["payload"])

        self.assertTrue(any("event ID" in error for error in pilot.validate_trace(forged)))
        self.assertIn("exactly one RUN_BOUND event is required", pilot.validate_trace(duplicate))

    def test_full_pilot_recovers_plants_without_performance_claims(self) -> None:
        report = pilot.run_pilot(PILOT_ROOT)
        self.assertEqual(14, report["scenarios_defined"])
        self.assertEqual(12, report["lanes"]["diagnostic_injection"])
        self.assertEqual(2, report["lanes"]["clean_room_independence"])
        self.assertEqual([], report["planted_methodology_faults_missed"])
        self.assertTrue(report["false_f11"]["all_rejected"])
        self.assertGreaterEqual(len(report["unresolved_attribution"]), 1)
        self.assertTrue(report["planting_key_loaded_after_evaluation_seal"])

        rendered = pilot.render_markdown(report).lower()
        for prohibited in (
            "win rate",
            "elo",
            "leaderboard",
            "quality score",
            "overall percentage",
        ):
            with self.subTest(prohibited=prohibited):
                self.assertNotIn(prohibited, rendered)

    def test_report_persists_full_finding_ledger(self) -> None:
        report = pilot.run_pilot(PILOT_ROOT)
        ledger = report["finding_ledger"]
        self.assertEqual(22, len(ledger))
        required_fields = {
            "observation_id",
            "scenario_contract_rubric_versions",
            "run_id",
            "condition",
            "execution_fingerprint",
            "activation_route_resource_evidence",
            "violated_invariant_or_relation",
            "exact_output_evidence",
            "decision_consequence",
            "validity_status",
            "behavioral_tags",
            "ranked_mechanism_candidates",
            "positive_evidence",
            "strongest_surviving_confound",
            "counterfactual_performed_and_result",
            "observability_limitation",
            "current_disposition",
            "behavior_confidence",
            "mechanism_confidence",
            "recurrence_signature_and_lineage",
            "next_action",
            "record_seal",
        }
        for record in ledger:
            self.assertTrue(required_fields.issubset(record))
            self.assertEqual(
                record["record_seal"],
                pilot.sha256_digest(
                    {key: value for key, value in record.items() if key != "record_seal"}
                ),
            )
        self.assertEqual(
            report["finding_ledger_seal"], pilot.sha256_digest(report["finding_ledger"])
        )
        context = report["f11_evidence_context"]
        self.assertEqual(
            context["evaluation_evidence_seal"],
            pilot.sha256_digest(
                {
                    key: context[key]
                    for key in ("scenario_results", "condition_results", "pair_results", "records")
                }
            ),
        )
        self.assertEqual(2, len(report["ab_disposition_patterns"]))
        f2 = next(record for record in ledger if record["condition_id"] == "COND-014")
        self.assertEqual(6, len(f2["counterfactual_evidence"]["repeat_arms"]))

    def test_full_pilot_is_deterministic(self) -> None:
        first = pilot.run_pilot(PILOT_ROOT)
        second = pilot.run_pilot(PILOT_ROOT)
        self.assertEqual(pilot.sha256_digest(first), pilot.sha256_digest(second))

    def test_all_expected_taxonomy_recovery_is_present(self) -> None:
        report = pilot.run_pilot(PILOT_ROOT)
        recovered = report["taxonomy_recovery"]
        for code in ("F0", "F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8", "F9", "F10", "F12"):
            with self.subTest(code=code):
                self.assertIn(code, recovered)
                self.assertGreaterEqual(len(recovered[code]), 1)

    def test_sealed_results_contain_two_fixture_judgments_and_valid_evidence(self) -> None:
        cases = load_fixture("pilot-cases.json")
        sealed = pilot.evaluate_and_seal(cases)
        self.assertEqual(22, len(sealed["condition_results"]))
        for result in sealed["condition_results"]:
            if result["execution_status"] == "rejected_before_execution":
                self.assertEqual([], result["judgments"])
                continue
            self.assertEqual(2, len(result["judgments"]))
            for judgment in result["judgments"]:
                self.assertEqual("deterministic_fixture", judgment["judge_kind"])
                self.assertIn(judgment["overall"], {"acceptable", "unacceptable", "indeterminate"})
            if result["trace_telemetry_status"] == "complete":
                self.assertEqual([], result["trace_errors"])

    def test_pair_results_require_independent_member_judgments(self) -> None:
        sealed = pilot.evaluate_and_seal(load_fixture("pilot-cases.json"))
        pairs = {item["pair_id"]: item for item in sealed["pair_results"]}
        self.assertFalse(pairs["PAIR-001"]["passed"])
        self.assertEqual(
            "member_not_independently_acceptable", pairs["PAIR-001"]["reason"]
        )
        self.assertTrue(pairs["PAIR-004"]["passed"])

    def test_pair_fixtures_record_mutation_and_consistency_closure(self) -> None:
        for pair in load_fixture("pilot-cases.json")["pairs"]:
            self.assertIn("changed_fact", pair["mutation"])
            self.assertGreaterEqual(len(pair["consistency_closure"]["held_constant"]), 3)

    def test_clean_room_report_preserves_unmapped_or_multiply_mapped_case(self) -> None:
        status = pilot.run_pilot(PILOT_ROOT)["clean_room_independence"]
        self.assertEqual("fixture_independence_checks_passed", status["status"])
        self.assertEqual(2, len(status["independent_provenance_roots"]))
        self.assertTrue(
            {"unmapped", "multiply_mapped"}.intersection(status["mapping_statuses"])
        )
        self.assertFalse(status["live_human_judgment_executed"])

    def test_report_rejected_artifact_is_not_silently_deleted(self) -> None:
        report = pilot.run_pilot(PILOT_ROOT)
        self.assertEqual(["PD-DI-001@1.0.0"], report["scenarios_rejected"])
        self.assertEqual(14, len(report["scenario_versions"]))


if __name__ == "__main__":
    unittest.main()

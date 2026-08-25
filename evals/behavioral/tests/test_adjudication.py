from __future__ import annotations

import json
import unittest

from evals.behavioral.behavioral_eval.adjudication import (
    build_blind_packet,
    evaluate_hard_predicates,
)
from evals.behavioral.behavioral_eval.models import (
    CaseContract,
    RunRecord,
    RunState,
    ValidationError,
)


def make_case(predicates: list[dict] | None = None) -> CaseContract:
    return CaseContract.from_dict(
        {
            "case_id": "BEH-PAID-001",
            "version": "1.0.0",
            "family": "paid-media",
            "prompt": "Classify the reported and optimized events.",
            "input_files": [],
            "hard_predicates": predicates or [{"type": "output_present"}],
            "review_criteria": ["Preserves the evidence boundary."],
            "forbidden_disclosures": ["F8", "paid-media.observation"],
            "expected_relation": "skill_not_worse",
            "provenance": {
                "source": "evals/paid-media-architecture-adversarial-cases.md",
                "frozen_at_commit": "b" * 40,
            },
        }
    )


def make_run(output: str = "Reported is observed; optimized is configured.") -> RunRecord:
    return RunRecord(
        run_id="RUN-SKILL-001",
        case_identity="BEH-PAID-001@1.0.0",
        profile_id="current-skill",
        state=RunState.COMPLETED,
        started_at="2026-08-25T10:00:00Z",
        finished_at="2026-08-25T10:01:00Z",
        final_output=output,
    )


class AdjudicationTests(unittest.TestCase):
    def test_blind_packet_omits_arm_route_and_failure_identity(self) -> None:
        packet = build_blind_packet(make_case(), make_run())
        serialized = json.dumps(packet)

        self.assertNotIn("current-skill", serialized)
        self.assertNotIn("paid-media.observation", serialized)
        self.assertNotIn("F8", serialized)
        self.assertNotIn("expected_relation", serialized)
        self.assertEqual("Classify the reported and optimized events.", packet["task"])
        self.assertEqual(
            "Reported is observed; optimized is configured.", packet["candidate_answer"]
        )

    def test_supported_predicates_are_evaluated_objectively(self) -> None:
        case = make_case(
            [
                {"type": "output_present"},
                {"type": "max_characters", "value": 80},
                {"type": "must_contain_literal", "value": "observed"},
                {"type": "must_not_contain_literal", "value": "guaranteed"},
                {"type": "valid_json"},
            ]
        )

        results = evaluate_hard_predicates(case, '{"status":"observed"}')

        self.assertEqual([True, True, True, True, True], [item.passed for item in results])

    def test_failed_predicate_has_a_stable_reason(self) -> None:
        case = make_case([{"type": "must_not_contain_literal", "value": "guaranteed"}])

        result = evaluate_hard_predicates(case, "This is guaranteed.")[0]

        self.assertFalse(result.passed)
        self.assertIn("forbidden literal", result.detail)

    def test_unknown_predicate_fails_closed(self) -> None:
        case = make_case([{"type": "semantic_quality", "value": "excellent"}])

        with self.assertRaisesRegex(ValidationError, "unsupported hard predicate"):
            evaluate_hard_predicates(case, "answer")

    def test_predicate_value_types_are_enforced(self) -> None:
        case = make_case([{"type": "max_characters", "value": "short"}])

        with self.assertRaisesRegex(ValidationError, "max_characters requires"):
            evaluate_hard_predicates(case, "answer")

    def test_blind_packet_rejects_mismatched_case(self) -> None:
        run = make_run()
        run = RunRecord(**{**run.__dict__, "case_identity": "BEH-OTHER-001@1.0.0"})

        with self.assertRaisesRegex(ValidationError, "run does not belong"):
            build_blind_packet(make_case(), run)


if __name__ == "__main__":
    unittest.main()

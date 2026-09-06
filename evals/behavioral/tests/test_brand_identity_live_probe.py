from __future__ import annotations

import unittest
from pathlib import Path

from evals.behavioral.behavioral_eval.brand_identity_live_probe import (
    NEGATIVE_CASE,
    POSITIVE_CASE,
    analyze_negative,
    analyze_positive,
)
from evals.behavioral.behavioral_eval.validation import load_cases


ROOT = Path(__file__).resolve().parents[3]
CORPUS = (
    ROOT
    / "evals"
    / "behavioral"
    / "cases"
    / "brand-identity-live-probe-v1.json"
)
FROZEN_HEAD = "544b33a823c0b19017b274773495a8af62a2cf44"


def activation_event() -> dict:
    return {
        "type": "skill_activated",
        "skill": "marketing-practitioner",
    }


def route_event(route: str, output: str = "") -> dict:
    return {
        "type": "item.completed",
        "item": {
            "type": "command_execution",
            "command": (
                "python -B .agents/skills/marketing-practitioner/"
                f"scripts/get-knowledge.py {route}"
            ),
            "exit_code": 0,
            "aggregated_output": output,
        },
    }


class BrandIdentityLiveProbeContractTests(unittest.TestCase):
    def test_corpus_is_exact_two_case_reviewer_pair(self) -> None:
        cases = load_cases(CORPUS)

        self.assertEqual(2, len(cases))
        self.assertEqual(
            {"BI-LIVE-001", "BI-LIVE-002"},
            {case.case_id for case in cases},
        )
        self.assertEqual(
            {"brand-identity-live-activation"},
            {case.family for case in cases},
        )
        self.assertTrue(
            all(case.provenance.frozen_at_commit == FROZEN_HEAD for case in cases)
        )
        self.assertTrue(
            all(
                case.provenance.source.startswith(
                    "independent-runtime-review:BI-R01-"
                )
                for case in cases
            )
        )

    def test_positive_accepts_direct_equity_after_activation(self) -> None:
        run = {
            "case_identity": POSITIVE_CASE,
            "profile_id": "current-skill",
            "state": "completed",
            "exit_code": 0,
            "raw_events": [
                activation_event(),
                route_event(
                    "brand-identity.equity",
                    "## 2. Existing equity, candidate distinctiveness, and redesign\n"
                    "UNMEASURED EQUITY != ZERO != PROVEN",
                ),
            ],
            "final_output": (
                "Not measuring recognition does not show that the asset has zero "
                "equity, and team boredom is not buyer-memory evidence."
            ),
        }

        result = analyze_positive(run)

        self.assertTrue(result["mechanical_pass"])
        self.assertEqual("brand-identity.equity", result["first_route"])
        self.assertTrue(result["equity_resource_delivered"])
        self.assertTrue(result["activation_precedes_equity"])

    def test_positive_rejects_core_before_equity(self) -> None:
        run = {
            "case_identity": POSITIVE_CASE,
            "profile_id": "current-skill",
            "state": "completed",
            "exit_code": 0,
            "raw_events": [
                activation_event(),
                route_event("brand-identity.core", "## 1. Scope"),
                route_event(
                    "brand-identity.equity",
                    "## 2. Existing equity, candidate distinctiveness, and redesign",
                ),
            ],
            "final_output": "bounded answer",
        }

        result = analyze_positive(run)

        self.assertFalse(result["mechanical_pass"])
        self.assertEqual("brand-identity.core", result["first_route"])

    def test_positive_rejects_missing_activation(self) -> None:
        run = {
            "case_identity": POSITIVE_CASE,
            "profile_id": "current-skill",
            "state": "activation_unverified",
            "exit_code": 0,
            "raw_events": [
                route_event(
                    "brand-identity.equity",
                    "## 2. Existing equity, candidate distinctiveness, and redesign",
                ),
            ],
            "final_output": "bounded answer",
        }

        self.assertFalse(analyze_positive(run)["mechanical_pass"])

    def test_negative_accepts_no_skill_activation_when_no_deep_route_occurs(self) -> None:
        run = {
            "case_identity": NEGATIVE_CASE,
            "profile_id": "current-skill",
            "state": "activation_unverified",
            "exit_code": 0,
            "raw_events": [{"type": "adapter_observation", "elapsed_seconds": 1.0}],
            "final_output": "Please provide the approved master file to export.",
        }

        result = analyze_negative(run)

        self.assertTrue(result["mechanical_pass"])
        self.assertTrue(result["no_deep_brand_identity_route"])

    def test_negative_rejects_visual_noun_driven_deep_route(self) -> None:
        run = {
            "case_identity": NEGATIVE_CASE,
            "profile_id": "current-skill",
            "state": "completed",
            "exit_code": 0,
            "raw_events": [
                activation_event(),
                route_event("brand-identity.core", "## 1. Scope"),
            ],
            "final_output": "bounded answer",
        }

        result = analyze_negative(run)

        self.assertFalse(result["mechanical_pass"])
        self.assertFalse(result["no_deep_brand_identity_route"])


if __name__ == "__main__":
    unittest.main()

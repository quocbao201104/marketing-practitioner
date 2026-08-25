from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from evals.behavioral.behavioral_eval.models import ArmProfile, RunState
from evals.behavioral.behavioral_eval.validation import (
    ValidationError,
    load_cases,
    load_profiles,
)


def valid_case(case_id: str = "BEH-FAST-001") -> dict:
    return {
        "case_id": case_id,
        "version": "1.0.0",
        "family": "fast-path",
        "prompt": "Shorten this approved message without changing the claim.",
        "input_files": [],
        "hard_predicates": [{"type": "output_present"}],
        "review_criteria": ["Preserves the approved claim."],
        "forbidden_disclosures": ["expected route"],
        "expected_relation": "skill_not_worse",
        "provenance": {
            "source": "evals/prebenchmark-runtime-smoke.md#S1",
            "frozen_at_commit": "bb53cadce87546ae8c7cd9eab1aa1985a32cd9df",
        },
    }


def valid_profile(profile_id: str = "baseline") -> dict:
    return {
        "profile_id": profile_id,
        "adapter": "fixture",
        "model": "fixture-model",
        "reasoning_effort": "medium",
        "skill_mode": "none",
        "skill_source": None,
        "expected_skill_sha256": None,
        "timeout_seconds": 30,
        "repetitions": 2,
    }


class ValidationTests(unittest.TestCase):
    def write_json(self, payload: dict) -> Path:
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        path = Path(temporary.name) / "payload.json"
        path.write_text(json.dumps(payload), encoding="utf-8")
        return path

    def test_duplicate_case_identity_fails_closed(self) -> None:
        path = self.write_json(
            {"schema_version": 1, "cases": [valid_case(), valid_case()]}
        )

        with self.assertRaisesRegex(
            ValidationError, "duplicate case identity: BEH-FAST-001@1.0.0"
        ):
            load_cases(path)

    def test_case_rejects_unknown_fields(self) -> None:
        candidate = valid_case()
        candidate["expected_route"] = "content.core"
        path = self.write_json({"schema_version": 1, "cases": [candidate]})

        with self.assertRaisesRegex(ValidationError, "unknown case fields"):
            load_cases(path)

    def test_live_profile_requires_explicit_model_and_effort(self) -> None:
        data = valid_profile("current-skill")
        data.update(
            {
                "adapter": "codex-cli",
                "model": "required-at-run",
                "reasoning_effort": "required-at-run",
                "skill_mode": "workspace-copy",
                "skill_source": "skills/marketing-practitioner",
                "expected_skill_sha256": "computed-at-run-bind",
            }
        )

        with self.assertRaisesRegex(ValidationError, "explicit model"):
            ArmProfile.from_dict(data, live=True)

    def test_duplicate_profile_id_fails_closed(self) -> None:
        path = self.write_json(
            {"schema_version": 1, "profiles": [valid_profile(), valid_profile()]}
        )

        with self.assertRaisesRegex(ValidationError, "duplicate profile id: baseline"):
            load_profiles(path)

    def test_valid_documents_load_as_immutable_models(self) -> None:
        case_path = self.write_json({"schema_version": 1, "cases": [valid_case()]})
        profile_path = self.write_json(
            {"schema_version": 1, "profiles": [valid_profile()]}
        )

        cases = load_cases(case_path)
        profiles = load_profiles(profile_path)

        self.assertEqual("BEH-FAST-001", cases[0].case_id)
        self.assertEqual("baseline", profiles[0].profile_id)
        self.assertEqual("completed", RunState.COMPLETED.value)


if __name__ == "__main__":
    unittest.main()

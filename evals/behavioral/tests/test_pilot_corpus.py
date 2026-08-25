from __future__ import annotations

import unittest
from pathlib import Path

from evals.behavioral.behavioral_eval.validation import load_cases, load_profiles


ROOT = Path(__file__).resolve().parents[3]
PILOT = ROOT / "evals" / "behavioral" / "cases" / "pilot-v1.json"
PROFILES = ROOT / "evals" / "behavioral" / "profiles"


class PilotCorpusTests(unittest.TestCase):
    def test_frozen_pilot_has_exact_ids_and_six_required_families(self) -> None:
        cases = load_cases(PILOT)

        self.assertEqual(
            {
                "BEH-FAST-001",
                "BEH-FAST-002",
                "BEH-STATE-001",
                "BEH-EVID-001",
                "BEH-CAUSE-001",
                "BEH-DISC-001",
                "BEH-COM-001",
                "BEH-EMAIL-001",
                "BEH-PAID-001",
                "BEH-PAID-002",
                "BEH-PAID-003",
                "BEH-PAID-004",
            },
            {case.case_id for case in cases},
        )
        self.assertEqual(12, len(cases))
        self.assertEqual(
            {
                "fast-path-proportionality",
                "resolved-state-preservation",
                "evidence-control",
                "causal-diagnosis",
                "commerce-discovery-routing",
                "paid-media-boundaries",
            },
            {case.family for case in cases},
        )
        self.assertTrue(all(case.review_criteria for case in cases))
        self.assertTrue(all(case.provenance.source.startswith("evals/") or case.case_id == "BEH-EVID-001" for case in cases))

    def test_profiles_bind_baseline_and_current_skill_isolation(self) -> None:
        profiles = []
        for path in sorted(PROFILES.glob("*.json")):
            profiles.extend(load_profiles(path, live=True))
        by_id = {profile.profile_id: profile for profile in profiles}

        self.assertEqual({"baseline", "current-skill"}, set(by_id))
        self.assertEqual("none", by_id["baseline"].skill_mode)
        self.assertIsNone(by_id["baseline"].skill_source)
        self.assertEqual("workspace-copy", by_id["current-skill"].skill_mode)
        self.assertEqual(
            "skills/marketing-practitioner", by_id["current-skill"].skill_source
        )
        self.assertEqual(
            "computed-at-run-bind", by_id["current-skill"].expected_skill_sha256
        )
        self.assertEqual(2, by_id["current-skill"].repetitions)


if __name__ == "__main__":
    unittest.main()

from __future__ import annotations

import unittest
from pathlib import Path

from evals.behavioral.behavioral_eval.validation import load_cases


ROOT = Path(__file__).resolve().parents[3]
CORPUS = (
    ROOT
    / "evals"
    / "behavioral"
    / "cases"
    / "external-refinement-regressions-v1.json"
)
FROZEN_HEAD = "0846d2c5f571b99b1804e2164013636ceca25cc5"
EXPECTED_IDS = {
    "EXT-EVID-001",
    "EXT-COPY-001",
    "EXT-COPY-002",
    "EXT-VOICE-001",
    "EXT-VOICE-002",
    "EXT-VOICE-003",
    "EXT-QUOTE-001",
    "EXT-INFER-001",
    "EXT-VERIFY-001",
    "EXT-PROV-001",
}
EXPECTED_FAMILIES = {
    "external-evidence-origin",
    "external-copy-transformation",
    "external-voice-evidence",
    "external-quote-fidelity",
    "external-inference-boundary",
    "external-validation-state",
    "external-tool-provenance",
}


class ExternalRefinementCorpusTests(unittest.TestCase):
    def test_corpus_has_exact_frozen_case_set(self) -> None:
        cases = load_cases(CORPUS)

        self.assertEqual(10, len(cases))
        self.assertEqual(EXPECTED_IDS, {case.case_id for case in cases})
        self.assertEqual(EXPECTED_FAMILIES, {case.family for case in cases})
        self.assertTrue(all(case.review_criteria for case in cases))
        self.assertTrue(
            all(case.expected_relation == "skill_not_worse" for case in cases)
        )
        self.assertTrue(
            all(case.provenance.frozen_at_commit == FROZEN_HEAD for case in cases)
        )
        self.assertTrue(
            all(
                case.provenance.source.startswith("external-refinement-adjudication:")
                for case in cases
            )
        )

    def test_negative_controls_share_family_without_new_relation_semantics(self) -> None:
        cases = {case.case_id: case for case in load_cases(CORPUS)}

        self.assertEqual(
            cases["EXT-COPY-001"].family,
            cases["EXT-COPY-002"].family,
        )
        self.assertEqual(
            cases["EXT-VOICE-001"].family,
            cases["EXT-VOICE-002"].family,
        )
        self.assertEqual(
            "skill_not_worse", cases["EXT-COPY-001"].expected_relation
        )
        self.assertEqual(
            "skill_not_worse", cases["EXT-COPY-002"].expected_relation
        )
        self.assertEqual(
            "skill_not_worse", cases["EXT-VOICE-001"].expected_relation
        )
        self.assertEqual(
            "skill_not_worse", cases["EXT-VOICE-002"].expected_relation
        )


if __name__ == "__main__":
    unittest.main()

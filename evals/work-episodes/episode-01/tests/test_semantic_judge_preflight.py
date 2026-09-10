from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from semantic_judge import (
    JudgeIdentity,
    JudgeTarget,
    PROMPT_VERSION,
    RUBRIC_VERSION,
    packet_is_blinded,
)
from semantic_judge_cases import EXPECTED_CASE_IDS, build_cases
from semantic_judge_preflight import export_blinded_packets, score_response_texts


class SemanticJudgePreflightTests(unittest.TestCase):
    @staticmethod
    def _ref_named(case, name):
        return next(item.ref for item in case.packet.evidence if item.name == name)

    @classmethod
    def _refs_for(cls, case):
        refs = set(case.packet.evidence_refs)
        if case.target is JudgeTarget.PRE_R2_RELIANCE:
            return [next(ref for ref in refs if ref.endswith(":basis"))]
        if case.target is JudgeTarget.POST_R2_REVISION:
            basis = next(ref for ref in refs if ref.endswith(":basis") and ":A001:" in ref)
            exposure = next(ref for ref in refs if ref.startswith("exposure:R2_EXPOSURE:"))
            launch = next(ref for ref in refs if "terminal:artifact:launch-plan.md:" in ref)
            return [basis, exposure, launch]
        if case.target is JudgeTarget.AUDIT_UPDATE:
            exposure = next(ref for ref in refs if ref.startswith("exposure:R2_EXPOSURE:"))
            launch = next(ref for ref in refs if "terminal:artifact:launch-plan.md:" in ref)
            return [exposure, launch]
        if case.target is JudgeTarget.TERMINAL_COHERENCE:
            launch = next(ref for ref in refs if "terminal:artifact:launch-plan.md:" in ref)
            measurement = next(ref for ref in refs if "terminal:artifact:measurement-plan.md:" in ref)
            return [launch, measurement]

        launch_refs = [ref for ref in refs if "terminal:artifact:launch-plan.md:" in ref]
        decision = launch_refs[0] if launch_refs else next(ref for ref in refs if ref.endswith(":basis"))
        selected = [decision]
        if case.target in {JudgeTarget.EVIDENCE_SCOPE, JudgeTarget.CAUSAL_TRANSFER} and case.expected_applicability == "applicable":
            competitor = next(
                ref
                for ref in refs
                if ref.startswith("exposure:R2_EXPOSURE:")
                or "competitor-performance-memo-R1.md:" in ref
            )
            selected.append(competitor)
        for name in case.required_grounding_names:
            ref = cls._ref_named(case, name)
            if ref not in selected:
                selected.append(ref)
        return selected

    @classmethod
    def _gold_responses(cls):
        responses = {}
        for case in build_cases():
            responses[case.packet.packet_id] = json.dumps(
                {
                    "applicability": case.expected_applicability,
                    "outcome": case.expected_outcome,
                    "evidence_refs": cls._refs_for(case),
                    "rationale": "preflight gold response for scorer plumbing",
                }
            )
        return responses

    def test_exact_unique_case_and_packet_identity(self):
        cases = build_cases()
        ids = tuple(case.case_id for case in cases)
        packet_ids = tuple(case.packet.packet_id for case in cases)
        self.assertEqual(EXPECTED_CASE_IDS, ids)
        self.assertEqual(len(ids), len(set(ids)))
        self.assertEqual(len(packet_ids), len(set(packet_ids)))
        self.assertEqual(20, len(cases))
        self.assertTrue(all(packet_is_blinded(case.packet) for case in cases))

    def test_corpus_contains_required_new_discriminators(self):
        cases = {case.case_id: case for case in build_cases()}
        self.assertEqual(JudgeTarget.CAUSAL_TRANSFER, cases["E01-SJ-18"].target)
        self.assertEqual("not_applicable", cases["E01-SJ-18"].expected_applicability)
        self.assertEqual(JudgeTarget.PRE_R2_RELIANCE, cases["E01-SJ-19"].target)
        self.assertEqual("unknown", cases["E01-SJ-19"].expected_outcome)
        self.assertEqual(JudgeTarget.AUDIT_UPDATE, cases["E01-SJ-20"].target)
        self.assertEqual("violated", cases["E01-SJ-20"].expected_outcome)
        injection_case = cases["E01-SJ-17"]
        self.assertTrue(any("Ignore the rubric" in item.content for item in injection_case.packet.evidence))
        self.assertEqual("satisfied", injection_case.expected_outcome)

    def test_export_does_not_include_gold_or_case_ids_in_judge_prompts(self):
        with tempfile.TemporaryDirectory(prefix="swe-e01-sj-export-") as temp_dir:
            root = Path(temp_dir)
            manifest = export_blinded_packets(root)
            self.assertEqual(20, manifest["packet_count"])
            self.assertEqual(PROMPT_VERSION, manifest["prompt_version"])
            self.assertEqual(RUBRIC_VERSION, manifest["rubric_version"])
            self.assertFalse(manifest["gold_labels_exported"])
            self.assertFalse(manifest["semantic_judge_adapter_validated"])
            self.assertFalse(manifest["live_trials_permitted"])
            prompt_files = sorted((root / "prompts").glob("*.json"))
            self.assertEqual(20, len(prompt_files))
            for path in prompt_files:
                text = path.read_text(encoding="utf-8")
                self.assertNotIn("E01-SJ-", text)
                self.assertNotIn("SWE-E01-P", text)
                self.assertNotIn("SWE-E01-C", text)
                self.assertNotIn("expected_verdict", text)
                self.assertNotIn("expected_outcome", text)

    def test_all_cases_must_pass_but_author_side_preflight_does_not_unlock_live(self):
        report = score_response_texts(self._gold_responses(), JudgeIdentity("test-provider", "test-model"))
        self.assertEqual("PASS", report.gate)
        self.assertTrue(report.case_identity_ok)
        self.assertTrue(report.response_identity_ok)
        self.assertTrue(report.all_cases_passed)
        self.assertTrue(report.semantic_competence_preflight_pass)
        self.assertFalse(report.semantic_judge_adapter_validated)
        self.assertFalse(report.live_trials_permitted)

    def test_supported_fact_requires_the_frozen_support_ref(self):
        cases = {case.case_id: case for case in build_cases()}
        case = cases["E01-SJ-09"]
        responses = self._gold_responses()
        launch = next(ref for ref in case.packet.evidence_refs if "terminal:artifact:launch-plan.md:" in ref)
        responses[case.packet.packet_id] = json.dumps(
            {
                "applicability": case.expected_applicability,
                "outcome": case.expected_outcome,
                "evidence_refs": [launch],
                "rationale": "correct label but missing the supplied economics support",
            }
        )
        report = score_response_texts(responses, JudgeIdentity("test-provider", "test-model"))
        self.assertEqual("FAIL", report.gate)
        score = next(item for item in report.case_scores if item.case_id == case.case_id)
        self.assertTrue(score.structurally_accepted)
        self.assertFalse(score.grounding_ok)
        self.assertFalse(score.passed)

    def test_one_semantic_misclassification_forces_fail(self):
        cases = build_cases()
        responses = self._gold_responses()
        case = cases[0]
        responses[case.packet.packet_id] = json.dumps(
            {
                "applicability": "applicable",
                "outcome": "does_not_rely",
                "evidence_refs": self._refs_for(case),
                "rationale": "planted wrong answer",
            }
        )
        report = score_response_texts(responses, JudgeIdentity("test-provider", "test-model"))
        self.assertEqual("FAIL", report.gate)
        self.assertFalse(report.all_cases_passed)

    def test_missing_or_extra_response_forces_fail(self):
        responses = self._gold_responses()
        missing_key = next(iter(responses))
        missing = dict(responses)
        missing.pop(missing_key)
        missing_report = score_response_texts(missing, JudgeIdentity("test-provider", "test-model"))
        self.assertEqual("FAIL", missing_report.gate)
        self.assertFalse(missing_report.response_identity_ok)

        extra = dict(responses)
        extra["deadbeef"] = json.dumps({"applicability": "unknown", "outcome": "unknown", "evidence_refs": [], "rationale": "extra"})
        extra_report = score_response_texts(extra, JudgeIdentity("test-provider", "test-model"))
        self.assertEqual("FAIL", extra_report.gate)
        self.assertFalse(extra_report.response_identity_ok)

    def test_malformed_blank_rationale_duplicate_ref_or_out_of_packet_forces_fail(self):
        cases = build_cases()
        for mutation in ("not-json", "blank", "duplicate", "out"):
            responses = self._gold_responses()
            case = cases[3]
            if mutation == "not-json":
                responses[case.packet.packet_id] = "not-json"
            elif mutation == "blank":
                responses[case.packet.packet_id] = json.dumps({"applicability": case.expected_applicability, "outcome": case.expected_outcome, "evidence_refs": self._refs_for(case), "rationale": "   "})
            elif mutation == "duplicate":
                refs = self._refs_for(case)
                responses[case.packet.packet_id] = json.dumps({"applicability": case.expected_applicability, "outcome": case.expected_outcome, "evidence_refs": refs + [refs[0]], "rationale": "duplicate ref"})
            else:
                responses[case.packet.packet_id] = json.dumps({"applicability": case.expected_applicability, "outcome": case.expected_outcome, "evidence_refs": ["invented:evidence:ref"], "rationale": "invalid citation"})
            report = score_response_texts(responses, JudgeIdentity("test-provider", "test-model"))
            self.assertEqual("FAIL", report.gate, mutation)

    def test_wrong_prompt_or_rubric_provenance_forces_fail(self):
        for identity in (
            JudgeIdentity("test-provider", "test-model", "bogus", RUBRIC_VERSION),
            JudgeIdentity("test-provider", "test-model", PROMPT_VERSION, "bogus"),
        ):
            report = score_response_texts(self._gold_responses(), identity)
            self.assertEqual("FAIL", report.gate)
            self.assertEqual("unavailable", report.judge_id)
            self.assertFalse(report.semantic_competence_preflight_pass)

    def test_invalid_judge_identity_forces_fail(self):
        report = score_response_texts(self._gold_responses(), JudgeIdentity("   ", "test-model"))
        self.assertEqual("FAIL", report.gate)
        self.assertEqual("unavailable", report.judge_id)
        self.assertFalse(report.semantic_competence_preflight_pass)


if __name__ == "__main__":
    unittest.main()

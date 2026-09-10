from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from episode import TARGET_PATHS, WORLD_PRESSURE, initialize_workspace
from evaluator import PredicateStatus, SemanticAssessment, SemanticObservations, WorkVerdict, evaluate, required_relation_refs
from fixtures import EXPECTED_FIXTURE_IDS, run_all_fixtures
from oracle import CURRENT_DEPENDENT_IDS, CURRENT_PROTECTED_IDS, SOURCE_HISTORY_IDS
from preflight import run_preflight


def complete_log(root: Path) -> None:
    (root / "release-log.md").write_text(
        "\n".join(f"{path} — reviewed" for path in TARGET_PATHS),
        encoding="utf-8",
    )


class PreflightTests(unittest.TestCase):
    def test_all_frozen_fixtures_match_expected_classification(self):
        results = run_all_fixtures()
        self.assertEqual(set(EXPECTED_FIXTURE_IDS), {result.fixture_id for result in results})
        self.assertTrue(all(result.passed for result in results))

    def test_preflight_keeps_live_and_semantic_judge_locks_closed(self):
        report = run_preflight()
        self.assertEqual("PASS", report["gate"])
        self.assertFalse(report["live_trials_permitted"])
        self.assertFalse(report["semantic_judge_adapter_validated"])

    def test_invalid_judge_identity_fails_closed(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            state = initialize_workspace(root, WORLD_PRESSURE)
            complete_log(root)
            state.seal_qa_candidate(review_complete=True, t0_valid=True)
            state.deliver_r2(); complete_log(root); state.terminal_gate()

            relations = {}
            for rid in (*CURRENT_DEPENDENT_IDS, *CURRENT_PROTECTED_IDS, *SOURCE_HISTORY_IDS):
                refs = required_relation_refs(state, rid) or ()
                relations[rid] = SemanticAssessment("applicable", "satisfied", tuple(refs), "JUDGE-A")
            refs = required_relation_refs(state, "R01") or ()
            relations["R01"] = SemanticAssessment("applicable", "satisfied", tuple(refs), "   ")
            log_ref = state.terminal_ref("release-log.md")
            obs = SemanticObservations(
                h02_release_log=SemanticAssessment("applicable", "satisfied", (log_ref,) if log_ref else (), "JUDGE-A"),
                relations=relations,
            )
            result = evaluate(state, obs)
            self.assertEqual(PredicateStatus.NOT_ASSESSABLE, result.statuses["XCI-H03"])
            self.assertEqual(WorkVerdict.UNRESOLVED, result.verdict)

    def test_prelocked_relation_cannot_be_disabled_as_not_applicable(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            state = initialize_workspace(root, WORLD_PRESSURE)
            complete_log(root)
            state.seal_qa_candidate(review_complete=True, t0_valid=True)
            state.deliver_r2(); complete_log(root); state.terminal_gate()

            relations = {}
            for rid in (*CURRENT_DEPENDENT_IDS, *CURRENT_PROTECTED_IDS, *SOURCE_HISTORY_IDS):
                refs = required_relation_refs(state, rid) or ()
                relations[rid] = SemanticAssessment("applicable", "satisfied", tuple(refs), "JUDGE-A")
            refs = required_relation_refs(state, "R01") or ()
            relations["R01"] = SemanticAssessment("not_applicable", "satisfied", tuple(refs), "JUDGE-A")
            log_ref = state.terminal_ref("release-log.md")
            obs = SemanticObservations(
                h02_release_log=SemanticAssessment("applicable", "satisfied", (log_ref,) if log_ref else (), "JUDGE-A"),
                relations=relations,
            )
            result = evaluate(state, obs)
            self.assertEqual(PredicateStatus.NOT_ASSESSABLE, result.statuses["XCI-H03"])
            self.assertEqual(WorkVerdict.UNRESOLVED, result.verdict)


if __name__ == "__main__":
    unittest.main()

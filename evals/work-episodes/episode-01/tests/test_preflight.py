from __future__ import annotations

import sys
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from fixtures import EXPECTED_FIXTURE_IDS, FixtureResult, run_all_fixtures
from preflight import run_preflight


class PreflightTests(unittest.TestCase):
    def test_exact_21_unique_fixture_ids_are_present_and_pass(self):
        results = run_all_fixtures()
        ids = [result.fixture_id for result in results]
        self.assertEqual(list(EXPECTED_FIXTURE_IDS), ids)
        self.assertEqual(len(ids), len(set(ids)))
        self.assertEqual([], [result.fixture_id for result in results if not result.passed])

    def test_preflight_is_non_compensatory(self):
        report = run_preflight()
        self.assertEqual("PASS", report["gate"])
        self.assertTrue(report["fixture_identity_ok"])
        self.assertFalse(report["live_trials_permitted"])
        self.assertFalse(report["semantic_judge_adapter_validated"])

    def test_one_failed_fixture_forces_fail(self):
        fake = [FixtureResult(fid, True, "ok") for fid in EXPECTED_FIXTURE_IDS]
        fake[7] = FixtureResult(fake[7].fixture_id, False, "planted failure")
        with patch("preflight.run_all_fixtures", return_value=fake):
            self.assertEqual("FAIL", run_preflight()["gate"])

    def test_missing_or_duplicate_fixture_forces_fail(self):
        missing = [FixtureResult(fid, True, "ok") for fid in EXPECTED_FIXTURE_IDS[:-1]]
        with patch("preflight.run_all_fixtures", return_value=missing):
            self.assertEqual("FAIL", run_preflight()["gate"])
        duplicate = [FixtureResult(fid, True, "ok") for fid in EXPECTED_FIXTURE_IDS]
        duplicate[-1] = FixtureResult(duplicate[-2].fixture_id, True, "duplicate")
        with patch("preflight.run_all_fixtures", return_value=duplicate):
            self.assertEqual("FAIL", run_preflight()["gate"])


class GuardrailTests(unittest.TestCase):
    def test_missing_semantic_judgments_fail_closed(self):
        from episode import EpisodeState, M, WorkVerdict
        from evaluator import SemanticObservations, evaluate
        state = EpisodeState("SWE-E01-P")
        state.reserve_creator_inventory(20 * M, "bounded")
        state.close_booking_gate(); state.deliver_r2(); state.close_reduction_gate(); state.terminal_gate()
        result = evaluate(state, SemanticObservations())
        self.assertNotEqual(WorkVerdict.PASS, result.verdict)

    def test_h06_requires_actual_terminal_files(self):
        from episode import EpisodeState, M, PredicateStatus
        from evaluator import SemanticObservations, evaluate
        state = EpisodeState("SWE-E01-P")
        state.reserve_creator_inventory(20 * M, "bounded")
        state.close_booking_gate(); state.deliver_r2(); state.close_reduction_gate(); state.terminal_gate()
        result = evaluate(state, SemanticObservations(final_other_allocations={
            "marketplace_search": 40 * M,
            "marketplace_onsite": 30 * M,
            "crm_owned": 20 * M,
            "contingency_learning": 0,
        }))
        self.assertEqual(PredicateStatus.VIOLATED, result.statuses["E01-H06"])

    def test_mechanism_level3_requires_all_controls(self):
        from evaluator import mechanism_disposition
        from episode import MechanismDisposition
        disposition = mechanism_disposition(trace_consistent=True, complete_telemetry=True, selective_intervention=True, relevant_negative_control=False)
        self.assertNotEqual(MechanismDisposition.LEVEL_3, disposition)


if __name__ == "__main__":
    unittest.main()

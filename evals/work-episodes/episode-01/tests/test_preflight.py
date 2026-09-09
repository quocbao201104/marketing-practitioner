from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from fixtures import run_all_fixtures
from preflight import run_preflight


class PreflightTests(unittest.TestCase):
    def test_all_21_fixtures_are_present_and_pass(self):
        results = run_all_fixtures()
        self.assertEqual(21, len(results))
        self.assertEqual([], [result.fixture_id for result in results if not result.passed])

    def test_preflight_is_non_compensatory(self):
        report = run_preflight()
        self.assertEqual("PASS", report["gate"])
        self.assertTrue(report["all_valid_material_fixtures_correctly_classified"])
        self.assertFalse(report["live_trials_permitted"])


class GuardrailTests(unittest.TestCase):
    def test_mechanism_level3_requires_all_controls(self):
        from evaluator import mechanism_disposition
        from episode import MechanismDisposition

        disposition = mechanism_disposition(
            trace_consistent=True,
            complete_telemetry=True,
            selective_intervention=True,
            relevant_negative_control=False,
        )
        self.assertNotEqual(MechanismDisposition.LEVEL_3, disposition)

    def test_out_of_range_channel_allocation_fails_terminal_work(self):
        from episode import EpisodeState, M, WorkVerdict
        from evaluator import SemanticObservations, evaluate

        state = EpisodeState("SWE-E01-P")
        state.reserve_creator_inventory(20 * M, "bounded learning")
        state.close_booking_gate()
        state.deliver_r2()
        state.close_reduction_gate()
        state.terminal_gate()
        observations = SemanticObservations(
            competitor_scope="valid",
            causal_transfer="valid",
            fabricated_support="none",
            task_completion="complete",
            pressure_response="valid",
            final_other_allocations={
                "marketplace_search": 10 * M,
                "marketplace_onsite": 30 * M,
                "crm_owned": 20 * M,
                "contingency_learning": 0,
            },
        )
        self.assertEqual(WorkVerdict.FAIL, evaluate(state, observations).verdict)


if __name__ == "__main__":
    unittest.main()

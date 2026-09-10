from __future__ import annotations

import sys
import tempfile
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
    @staticmethod
    def _complete_state(world: str, basis: str):
        from episode import M, initialize_workspace

        temp = tempfile.TemporaryDirectory(prefix="swe-e01-test-")
        root = Path(temp.name)
        state = initialize_workspace(root, world=world)
        state.reserve_creator_inventory(20 * M, basis)
        state.close_booking_gate()
        state.deliver_r2()
        state.close_reduction_gate()
        (root / "launch-plan.md").write_text(
            "# Launch plan\n\nExecutable bounded plan.\n", encoding="utf-8"
        )
        (root / "measurement-plan.md").write_text(
            "# Measurement plan\n\nMeasure realized contribution and incrementality.\n",
            encoding="utf-8",
        )
        state.terminal_gate("Final package")
        return temp, state

    @staticmethod
    def _valid_common_assessment(state):
        from evaluator import SemanticAssessment

        refs = tuple(
            ref
            for ref in sorted(state.valid_evidence_refs())
            if ref.startswith("terminal:")
        )
        return SemanticAssessment("applicable", "satisfied", refs, "JUDGE-TEST")

    @staticmethod
    def _p01_refs(state):
        reserve = state.reserve_action()
        assert reserve is not None
        exposure = next(
            ref
            for ref in state.valid_evidence_refs()
            if ref.startswith("exposure:R2_EXPOSURE:11:00:")
        )
        return (f"action:{reserve.action_id}:basis", exposure)

    def test_missing_semantic_judgments_fail_closed(self):
        from episode import WorkVerdict
        from evaluator import SemanticObservations, evaluate

        temp, state = self._complete_state("SWE-E01-P", "bounded learning")
        try:
            result = evaluate(state, SemanticObservations())
            self.assertNotEqual(WorkVerdict.PASS, result.verdict)
        finally:
            temp.cleanup()

    def test_not_applicable_without_provenance_cannot_remove_h04_h05_h07(self):
        from episode import M, PredicateStatus
        from evaluator import SemanticAssessment, SemanticObservations, evaluate

        temp, state = self._complete_state(
            "SWE-E01-P", "R1 is ambiguous; bounded access only"
        )
        try:
            common = self._valid_common_assessment(state)
            p01_refs = self._p01_refs(state)
            no_provenance = SemanticAssessment(applicability="not_applicable")
            observations = SemanticObservations(
                h04=no_provenance,
                h05=no_provenance,
                h06_coherence=common,
                h07=no_provenance,
                p01_reliance=SemanticAssessment(
                    "applicable", "does_not_rely", p01_refs, "JUDGE-P01-ACT"
                ),
                final_other_allocations={
                    "marketplace_search": 40 * M,
                    "marketplace_onsite": 30 * M,
                    "crm_owned": 20 * M,
                    "contingency_learning": 0,
                },
            )
            result = evaluate(state, observations)
            self.assertEqual(PredicateStatus.NOT_ASSESSABLE, result.statuses["E01-H04"])
            self.assertEqual(PredicateStatus.NOT_ASSESSABLE, result.statuses["E01-H05"])
            self.assertEqual(PredicateStatus.NOT_ASSESSABLE, result.statuses["E01-H07"])
        finally:
            temp.cleanup()

    def test_p01_activation_is_separate_from_p01_outcome_applicability(self):
        from episode import M, PredicateStatus
        from evaluator import SemanticAssessment, SemanticObservations, evaluate

        temp, state = self._complete_state(
            "SWE-E01-P", "5x proves creator profitability"
        )
        try:
            common = self._valid_common_assessment(state)
            refs = self._p01_refs(state)
            observations = SemanticObservations(
                h04=common,
                h05=common,
                h06_coherence=common,
                h07=common,
                p01_reliance=SemanticAssessment(
                    "applicable", "relies", refs, "JUDGE-P01-ACT"
                ),
                # This used to turn P01 off. Once reliance activates P01 it must
                # instead fail closed because satisfaction has not been judged.
                p01=SemanticAssessment(
                    "not_applicable", "unknown", refs, "JUDGE-P01-OUTCOME"
                ),
                final_other_allocations={
                    "marketplace_search": 40 * M,
                    "marketplace_onsite": 30 * M,
                    "crm_owned": 20 * M,
                    "contingency_learning": 0,
                },
            )
            unresolved = evaluate(state, observations)
            self.assertEqual(
                PredicateStatus.NOT_ASSESSABLE, unresolved.statuses["E01-P01"]
            )

            violated = evaluate(
                state,
                SemanticObservations(
                    **{
                        **observations.__dict__,
                        "p01": SemanticAssessment(
                            "applicable", "violated", refs, "JUDGE-P01-OUTCOME"
                        ),
                    }
                ),
            )
            self.assertEqual(PredicateStatus.VIOLATED, violated.statuses["E01-P01"])
        finally:
            temp.cleanup()

    def test_p01_non_reliance_from_sealed_basis_stays_not_applicable(self):
        from episode import M, PredicateStatus, WorkVerdict
        from evaluator import SemanticAssessment, SemanticObservations, evaluate

        temp, state = self._complete_state(
            "SWE-E01-P", "R1 is ambiguous; reserve only for bounded learning/access"
        )
        try:
            common = self._valid_common_assessment(state)
            refs = self._p01_refs(state)
            observations = SemanticObservations(
                h04=common,
                h05=common,
                h06_coherence=common,
                h07=common,
                p01_reliance=SemanticAssessment(
                    "applicable", "does_not_rely", refs, "JUDGE-P01-ACT"
                ),
                final_other_allocations={
                    "marketplace_search": 40 * M,
                    "marketplace_onsite": 30 * M,
                    "crm_owned": 20 * M,
                    "contingency_learning": 0,
                },
            )
            result = evaluate(state, observations)
            self.assertEqual(PredicateStatus.NOT_APPLICABLE, result.statuses["E01-P01"])
            self.assertEqual(WorkVerdict.PASS, result.verdict)
        finally:
            temp.cleanup()

    def test_control_missing_required_judgment_is_not_assessable(self):
        from episode import M, PredicateStatus
        from evaluator import SemanticObservations, evaluate

        temp, state = self._complete_state("SWE-E01-C", "bounded access")
        try:
            common = self._valid_common_assessment(state)
            result = evaluate(
                state,
                SemanticObservations(
                    h04=common,
                    h05=common,
                    h06_coherence=common,
                    h07=common,
                    final_other_allocations={
                        "marketplace_search": 40 * M,
                        "marketplace_onsite": 30 * M,
                        "crm_owned": 20 * M,
                        "contingency_learning": 0,
                    },
                ),
            )
            self.assertEqual(PredicateStatus.NOT_ASSESSABLE, result.statuses["E01-C01"])
        finally:
            temp.cleanup()

    def test_h06_requires_actual_terminal_files(self):
        from episode import EpisodeState, M, PredicateStatus
        from evaluator import SemanticObservations, evaluate

        state = EpisodeState("SWE-E01-P")
        state.reserve_creator_inventory(20 * M, "bounded")
        state.close_booking_gate()
        state.deliver_r2()
        state.close_reduction_gate()
        state.terminal_gate()
        result = evaluate(
            state,
            SemanticObservations(
                final_other_allocations={
                    "marketplace_search": 40 * M,
                    "marketplace_onsite": 30 * M,
                    "crm_owned": 20 * M,
                    "contingency_learning": 0,
                }
            ),
        )
        self.assertEqual(PredicateStatus.VIOLATED, result.statuses["E01-H06"])

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


if __name__ == "__main__":
    unittest.main()

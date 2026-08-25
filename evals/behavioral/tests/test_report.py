from __future__ import annotations

import unittest

from evals.behavioral.behavioral_eval.models import CaseContract, RunRecord, RunState
from evals.behavioral.behavioral_eval.report import build_report, pair_runs


def make_case() -> CaseContract:
    return CaseContract.from_dict(
        {
            "case_id": "BEH-FAST-001",
            "version": "1.0.0",
            "family": "fast-path",
            "prompt": "Shorten the message.",
            "input_files": [],
            "hard_predicates": [{"type": "output_present"}],
            "review_criteria": ["Preserves the approved claim."],
            "forbidden_disclosures": ["arm identity"],
            "expected_relation": "skill_not_worse",
            "provenance": {"source": "fixture", "frozen_at_commit": "b" * 40},
        }
    )


def make_run(
    run_id: str,
    profile_id: str,
    *,
    state: RunState = RunState.COMPLETED,
    disposition: str | None = "pass",
    output: str | None = "Bounded answer",
) -> RunRecord:
    return RunRecord(
        run_id=run_id,
        case_identity=make_case().identity,
        profile_id=profile_id,
        state=state,
        started_at="2026-08-25T10:00:00Z",
        finished_at="2026-08-25T10:01:00Z",
        final_output=output,
        answer_disposition=disposition,
    )


class PairingTests(unittest.TestCase):
    def test_pair_reports_skill_only_pass(self) -> None:
        baseline = [make_run("RUN-B-1", "baseline", disposition="fail")]
        skill = [make_run("RUN-S-1", "current-skill", disposition="pass")]

        pair = pair_runs(make_case(), baseline, skill)

        self.assertEqual("skill_only_pass", pair.disposition)
        self.assertFalse(pair.repeat_instability)

    def test_pair_marks_repeat_instability(self) -> None:
        baseline = [
            make_run("RUN-B-1", "baseline", disposition="pass"),
            make_run("RUN-B-2", "baseline", disposition="fail"),
        ]
        skill = [
            make_run("RUN-S-1", "current-skill", disposition="pass"),
            make_run("RUN-S-2", "current-skill", disposition="pass"),
        ]

        pair = pair_runs(make_case(), baseline, skill)

        self.assertEqual("unresolved", pair.disposition)
        self.assertTrue(pair.repeat_instability)

    def test_operational_failure_invalidates_pair(self) -> None:
        baseline = [
            make_run(
                "RUN-B-1",
                "baseline",
                state=RunState.TIMED_OUT,
                disposition=None,
                output=None,
            )
        ]
        skill = [make_run("RUN-S-1", "current-skill")]

        pair = pair_runs(make_case(), baseline, skill)

        self.assertEqual("operationally_invalid", pair.disposition)


class ReportTests(unittest.TestCase):
    def test_invalid_run_is_counted_but_not_scored_as_answer_failure(self) -> None:
        timeout = make_run(
            "RUN-B-1",
            "baseline",
            state=RunState.TIMED_OUT,
            disposition=None,
            output=None,
        )

        report = build_report([make_case()], [timeout], [])

        self.assertEqual(1, report["denominators"]["operationally_invalid"])
        self.assertEqual(0, report["denominators"]["answer_failures"])

    def test_judgments_are_applied_without_single_quality_score(self) -> None:
        runs = [
            make_run("RUN-B-1", "baseline", disposition=None),
            make_run("RUN-S-1", "current-skill", disposition=None),
        ]
        judgments = [
            {"run_id": "RUN-B-1", "disposition": "fail"},
            {"run_id": "RUN-S-1", "disposition": "pass"},
        ]

        report = build_report([make_case()], runs, judgments)

        self.assertEqual(1, report["paired_dispositions"]["skill_only_pass"])
        self.assertEqual(1, report["denominators"]["answer_failures"])
        self.assertNotIn("score", report)
        self.assertNotIn("win_rate", report)

    def test_missing_judgment_is_unresolved_not_failed(self) -> None:
        run = make_run("RUN-B-1", "baseline", disposition=None)

        report = build_report([make_case()], [run], [])

        self.assertEqual(1, report["denominators"]["unresolved"])
        self.assertEqual(0, report["denominators"]["answer_failures"])

    def test_family_denominators_are_emitted(self) -> None:
        runs = [
            make_run("RUN-B-1", "baseline"),
            make_run("RUN-S-1", "current-skill"),
        ]

        report = build_report([make_case()], runs, [])

        self.assertEqual(2, report["families"]["fast-path"]["runs"])
        self.assertEqual(1, report["families"]["fast-path"]["pairs"])


if __name__ == "__main__":
    unittest.main()

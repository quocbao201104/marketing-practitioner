from __future__ import annotations

import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path

from evals.behavioral.behavioral_eval.adapters import ExecutorResult
from evals.behavioral.behavioral_eval.fixture import FixtureAdapter
from evals.behavioral.behavioral_eval.models import ArmProfile, CaseContract, RunState
from evals.behavioral.behavioral_eval.runner import run_condition
from evals.behavioral.behavioral_eval.workspace import WorkspaceBinding


def case() -> CaseContract:
    return CaseContract.from_dict(
        {
            "case_id": "BEH-RUN-001",
            "version": "1.0.0",
            "family": "runner",
            "prompt": "Return a bounded answer.",
            "input_files": [],
            "hard_predicates": [{"type": "output_present"}],
            "review_criteria": ["Returns an answer."],
            "forbidden_disclosures": ["arm identity"],
            "expected_relation": "skill_not_worse",
            "provenance": {"source": "fixture", "frozen_at_commit": "b" * 40},
        }
    )


def profile(skill: bool = False) -> ArmProfile:
    return ArmProfile.from_dict(
        {
            "profile_id": "skill" if skill else "baseline",
            "adapter": "fixture",
            "model": "fixture-model",
            "reasoning_effort": "medium",
            "skill_mode": "workspace-copy" if skill else "none",
            "skill_source": "skill" if skill else None,
            "expected_skill_sha256": ("c" * 64) if skill else None,
            "timeout_seconds": 30,
            "repetitions": 1,
        }
    )


class RunnerTests(unittest.TestCase):
    def setUp(self) -> None:
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        (self.root / ".git").mkdir()
        self.binding = WorkspaceBinding(
            root=self.root,
            profile_id="baseline",
            skill_mode="none",
            skill_path=None,
            expected_skill_sha256=None,
        )
        timestamps = iter(
            [
                datetime(2026, 8, 25, 10, 0, tzinfo=timezone.utc),
                datetime(2026, 8, 25, 10, 1, tzinfo=timezone.utc),
            ]
        )
        self.clock = lambda: next(timestamps)

    def run_fixture(self, result: ExecutorResult, *, arm: ArmProfile | None = None):
        selected = arm or profile()
        adapter = FixtureAdapter({(case().identity, selected.profile_id): result})
        return run_condition(
            case(),
            selected,
            adapter,
            self.binding,
            clock=self.clock,
            run_id_factory=lambda: "RUN-001",
        )

    def test_timeout_is_operational_failure_not_answer_failure(self) -> None:
        record = self.run_fixture(ExecutorResult(timed_out=True))

        self.assertEqual(RunState.TIMED_OUT, record.state)
        self.assertIsNone(record.answer_disposition)
        self.assertIsNone(record.output_sha256)

    def test_nonzero_exit_is_executor_failure(self) -> None:
        record = self.run_fixture(
            ExecutorResult(exit_code=2, stderr="executor failed")
        )

        self.assertEqual(RunState.EXECUTOR_FAILED, record.state)
        self.assertEqual(2, record.exit_code)

    def test_missing_final_output_is_invalid_output(self) -> None:
        record = self.run_fixture(
            ExecutorResult(exit_code=0, raw_events=({"type": "completed"},))
        )

        self.assertEqual(RunState.INVALID_OUTPUT, record.state)
        self.assertIsNone(record.answer_disposition)

    def test_interrupted_run_cannot_complete(self) -> None:
        record = self.run_fixture(
            ExecutorResult(
                exit_code=0,
                interrupted=True,
                final_output="partial answer",
            )
        )

        self.assertEqual(RunState.EXECUTOR_FAILED, record.state)
        self.assertIn("executor was interrupted", record.limitations)

    def test_skill_run_without_activation_evidence_is_unverified(self) -> None:
        skill_profile = profile(True)
        skill_root = self.root / ".agents" / "skills" / "marketing-practitioner"
        skill_root.mkdir(parents=True)
        (skill_root / "SKILL.md").write_text("skill", encoding="utf-8")
        from evals.behavioral.behavioral_eval.workspace import hash_tree

        self.binding = WorkspaceBinding(
            root=self.root,
            profile_id="skill",
            skill_mode="workspace-copy",
            skill_path=skill_root,
            expected_skill_sha256=hash_tree(skill_root),
        )

        record = self.run_fixture(
            ExecutorResult(exit_code=0, final_output="answer", activation_verified=None),
            arm=skill_profile,
        )

        self.assertEqual(RunState.ACTIVATION_UNVERIFIED, record.state)

    def test_unknown_events_are_retained_in_completed_run(self) -> None:
        unknown = {"type": "future_event", "payload": {"value": 7}}
        record = self.run_fixture(
            ExecutorResult(
                exit_code=0,
                raw_events=(unknown,),
                final_output="bounded answer",
                activation_verified=True,
            )
        )

        self.assertEqual(RunState.COMPLETED, record.state)
        self.assertEqual((unknown,), record.raw_events)
        self.assertEqual(1, record.event_count)
        self.assertIsNotNone(record.event_sha256)
        self.assertIsNotNone(record.output_sha256)


if __name__ == "__main__":
    unittest.main()

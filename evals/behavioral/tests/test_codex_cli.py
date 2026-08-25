from __future__ import annotations

import sys
import tempfile
import textwrap
import unittest
from pathlib import Path
from unittest import mock

from evals.behavioral.behavioral_eval.adapters import ExecutorRequest
from evals.behavioral.behavioral_eval.codex_cli import (
    CodexCliAdapter,
    activation_verified,
    build_codex_command,
    resolve_codex_executable,
)
from evals.behavioral.behavioral_eval.models import ArmProfile, CaseContract
from evals.behavioral.behavioral_eval.workspace import WorkspaceBinding


class CodexCliTests(unittest.TestCase):
    def test_successful_exact_skill_read_is_activation_evidence(self) -> None:
        skill_file = self.binding.skill_path / "SKILL.md"
        events = (
            {
                "type": "item.completed",
                "item": {
                    "type": "command_execution",
                    "command": f"Get-Content -LiteralPath '{skill_file}' -Raw",
                    "exit_code": 0,
                },
            },
        )

        self.assertTrue(activation_verified(events, self.request))

    def test_default_executable_resolves_windows_command_shim(self) -> None:
        with mock.patch(
            "evals.behavioral.behavioral_eval.codex_cli.shutil.which",
            return_value=r"C:\Users\test\AppData\Roaming\npm\codex.CMD",
        ):
            self.assertEqual(
                (r"C:\Users\test\AppData\Roaming\npm\codex.CMD",),
                resolve_codex_executable(),
            )

    def setUp(self) -> None:
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        (self.root / ".git").mkdir()
        self.case = CaseContract.from_dict(
            {
                "case_id": "BEH-CLI-001",
                "version": "1.0.0",
                "family": "executor",
                "prompt": "RETURN_SUCCESS",
                "input_files": [],
                "hard_predicates": [{"type": "output_present"}],
                "review_criteria": ["Returns output."],
                "forbidden_disclosures": ["arm identity"],
                "expected_relation": "skill_not_worse",
                "provenance": {"source": "fixture", "frozen_at_commit": "d" * 40},
            }
        )
        self.profile = self.make_profile(timeout=5)
        self.binding = WorkspaceBinding(
            root=self.root,
            profile_id="current-skill",
            skill_mode="workspace-copy",
            skill_path=self.root / ".agents" / "skills" / "marketing-practitioner",
            expected_skill_sha256="e" * 64,
        )
        self.request = ExecutorRequest(
            run_id="RUN-CLI-001",
            case=self.case,
            profile=self.profile,
            workspace=self.binding,
        )
        self.fake = self.root / "fake_codex.py"
        self.fake.write_text(
            textwrap.dedent(
                """
                import json
                import pathlib
                import sys
                import time

                args = sys.argv[1:]
                if "--version" in args:
                    print("fake-codex 1.0")
                    raise SystemExit(0)
                prompt = sys.stdin.read()
                output = pathlib.Path(args[args.index("--output-last-message") + 1])
                output.parent.mkdir(parents=True, exist_ok=True)
                if "TIMEOUT" in prompt:
                    time.sleep(2)
                if "EXIT_TWO" in prompt:
                    print("deliberate failure", file=sys.stderr)
                    raise SystemExit(2)
                if "MALFORMED" in prompt:
                    print("not-json")
                else:
                    print(json.dumps({"type": "skill_activated", "skill": "marketing-practitioner"}))
                    print(json.dumps({"type": "future_event", "payload": {"value": 9}}))
                output.write_text("bounded answer", encoding="utf-8")
                """
            ).strip()
            + "\n",
            encoding="utf-8",
        )

    def make_profile(self, timeout: int) -> ArmProfile:
        return ArmProfile.from_dict(
            {
                "profile_id": "current-skill",
                "adapter": "codex-cli",
                "model": "gpt-test",
                "reasoning_effort": "medium",
                "skill_mode": "workspace-copy",
                "skill_source": "skills/marketing-practitioner",
                "expected_skill_sha256": "e" * 64,
                "timeout_seconds": timeout,
                "repetitions": 1,
            },
            live=True,
        )

    def request_with_prompt(self, prompt: str, timeout: int = 5) -> ExecutorRequest:
        case_data = {
            "case_id": "BEH-CLI-001",
            "version": "1.0.0",
            "family": "executor",
            "prompt": prompt,
            "input_files": [],
            "hard_predicates": [{"type": "output_present"}],
            "review_criteria": ["Returns output."],
            "forbidden_disclosures": ["arm identity"],
            "expected_relation": "skill_not_worse",
            "provenance": {"source": "fixture", "frozen_at_commit": "d" * 40},
        }
        return ExecutorRequest(
            run_id="RUN-CLI-001",
            case=CaseContract.from_dict(case_data),
            profile=self.make_profile(timeout),
            workspace=self.binding,
        )

    def adapter(self) -> CodexCliAdapter:
        return CodexCliAdapter((sys.executable, "-B", str(self.fake)))

    def test_command_uses_explicit_isolated_live_configuration(self) -> None:
        command = build_codex_command(self.request, executable=("codex",))

        self.assertIn("--json", command)
        self.assertIn("--ephemeral", command)
        self.assertIn("--ignore-user-config", command)
        self.assertEqual("read-only", command[command.index("--sandbox") + 1])
        self.assertEqual("gpt-test", command[command.index("--model") + 1])
        self.assertIn('model_reasoning_effort="medium"', command)
        self.assertEqual("-", command[-1])

    def test_success_captures_events_output_version_and_activation(self) -> None:
        result = self.adapter().execute(self.request)

        self.assertEqual(0, result.exit_code)
        self.assertFalse(result.timed_out)
        self.assertEqual("bounded answer", result.final_output)
        self.assertEqual("fake-codex 1.0", result.executable_version)
        self.assertTrue(result.activation_verified)
        self.assertEqual("future_event", result.raw_events[1]["type"])

    def test_malformed_jsonl_is_retained_as_unparsed_event(self) -> None:
        result = self.adapter().execute(self.request_with_prompt("MALFORMED"))

        self.assertEqual(0, result.exit_code)
        self.assertEqual("unparsed_jsonl", result.raw_events[0]["type"])
        self.assertEqual("not-json", result.raw_events[0]["raw"])

    def test_nonzero_exit_preserves_stderr(self) -> None:
        result = self.adapter().execute(self.request_with_prompt("EXIT_TWO"))

        self.assertEqual(2, result.exit_code)
        self.assertIn("deliberate failure", result.stderr)

    def test_timeout_terminates_executor(self) -> None:
        result = self.adapter().execute(self.request_with_prompt("TIMEOUT", timeout=1))

        self.assertTrue(result.timed_out)
        self.assertIsNone(result.final_output)


if __name__ == "__main__":
    unittest.main()

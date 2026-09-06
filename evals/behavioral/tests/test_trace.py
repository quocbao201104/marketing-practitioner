from __future__ import annotations

import json
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from io import StringIO
from pathlib import Path

from evals.behavioral.behavioral_eval.cli import main
from evals.behavioral.behavioral_eval.models import RunRecord, RunState, ValidationError
from evals.behavioral.behavioral_eval.trace import (
    classify_skill_walk,
    extract_helper_routes,
    extract_skill_paths,
    load_oracle,
    reconstruct_steps,
)
from evals.behavioral.behavioral_eval.validation import load_cases


ROOT = Path(__file__).resolve().parents[3]
PILOT = ROOT / "evals" / "behavioral" / "cases" / "pilot-v1.json"
ORACLE = ROOT / "evals" / "behavioral" / "oracles" / "pilot-v1.route-oracle.json"


def command_event(command: str, exit_code: int = 0) -> dict:
    return {
        "type": "item.completed",
        "item": {
            "type": "command_execution",
            "command": command,
            "exit_code": exit_code,
        },
    }


class TraceReconstructionTests(unittest.TestCase):
    def test_extracts_skill_relative_path_from_literal_get_content(self) -> None:
        command = (
            r'"C:\pwsh.exe" -Command "Get-Content -LiteralPath '
            r"'C:\Temp\BEH-FAST-001\current-skill\repeat-1"
            r"\.agents\skills\marketing-practitioner\SKILL.md' -Raw\""
        )

        self.assertEqual(("skill.md",), extract_skill_paths(command))

    def test_extracts_adaptation_skill_path(self) -> None:
        command = (
            "Get-Content -LiteralPath "
            "'.agents\\skills\\marketing-practitioner\\adaptations\\localization.md' -Raw"
        )

        self.assertEqual(
            ("adaptations/localization.md",),
            extract_skill_paths(command),
        )

    def test_extracts_helper_route_from_failed_python_invocation(self) -> None:
        command = (
            "python '.agents\\skills\\marketing-practitioner\\scripts\\"
            "get-knowledge.py' paid-media.observation"
        )

        self.assertEqual(("paid-media.observation",), extract_helper_routes(command))
        steps = reconstruct_steps((command_event(command, exit_code=-1),))
        self.assertEqual(1, len(steps))
        self.assertEqual("helper", steps[0].kind)
        self.assertFalse(steps[0].succeeded)
        self.assertEqual("paid-media.observation", steps[0].logical_id)

    def test_fast_path_skill_only_is_walk_ok(self) -> None:
        oracle = load_oracle(ORACLE)["BEH-FAST-001@1.0.0"]
        steps = reconstruct_steps(
            (
                command_event(
                    "Get-Content -LiteralPath "
                    "'.agents\\skills\\marketing-practitioner\\SKILL.md' -Raw"
                ),
            )
        )

        result = classify_skill_walk(steps, oracle)

        self.assertEqual("walk_ok", result["primary"])
        self.assertTrue(result["activated"])

    def test_fast_path_handbook_load_is_wrong_edge(self) -> None:
        oracle = load_oracle(ORACLE)["BEH-FAST-001@1.0.0"]
        steps = reconstruct_steps(
            (
                command_event(
                    "Get-Content -LiteralPath "
                    "'.agents\\skills\\marketing-practitioner\\SKILL.md' -Raw"
                ),
                command_event(
                    "Get-Content -LiteralPath "
                    "'.agents\\skills\\marketing-practitioner\\handbook\\"
                    "08-content-environments-and-distribution.md' -Raw"
                ),
            )
        )

        result = classify_skill_walk(steps, oracle)

        self.assertEqual("wrong_edge", result["primary"])

    def test_missing_required_node_without_attempt_is_skip_jit(self) -> None:
        oracle = load_oracle(ORACLE)["BEH-PAID-002@1.0.0"]
        steps = reconstruct_steps(
            (
                command_event(
                    "Get-Content -LiteralPath "
                    "'.agents\\skills\\marketing-practitioner\\SKILL.md' -Raw"
                ),
            )
        )

        result = classify_skill_walk(steps, oracle)

        self.assertEqual("skip_jit", result["primary"])
        self.assertIn("skip_jit", result["labels"])

    def test_failed_probe_of_required_file_is_resolve_fail(self) -> None:
        oracle = load_oracle(ORACLE)["BEH-EVID-001@1.0.0"]
        steps = reconstruct_steps(
            (
                command_event(
                    "Get-Content -LiteralPath "
                    "'.agents\\skills\\marketing-practitioner\\SKILL.md' -Raw"
                ),
                command_event(
                    "Select-String -LiteralPath "
                    "'.agents\\skills\\marketing-practitioner\\handbook\\"
                    "01-customer-research-and-evidence.md' -Pattern prevalence",
                    exit_code=-1,
                ),
            )
        )

        result = classify_skill_walk(steps, oracle)

        self.assertEqual("resolve_fail", result["primary"])
        self.assertIn("skip_jit", result["labels"])

    def test_failed_helper_without_recovery_is_resolve_fail(self) -> None:
        oracle = load_oracle(ORACLE)["BEH-PAID-001@1.0.0"]
        steps = reconstruct_steps(
            (
                command_event(
                    "Get-Content -LiteralPath "
                    "'.agents\\skills\\marketing-practitioner\\SKILL.md' -Raw"
                ),
                command_event(
                    "python '.agents\\skills\\marketing-practitioner\\scripts\\"
                    "get-knowledge.py' paid-media.observation",
                    exit_code=-1,
                ),
            )
        )

        result = classify_skill_walk(steps, oracle)

        self.assertEqual("resolve_fail", result["primary"])
        self.assertIn("skip_jit", result["labels"])

    def test_no_skill_file_read_is_no_activation(self) -> None:
        oracle = load_oracle(ORACLE)["BEH-FAST-001@1.0.0"]
        result = classify_skill_walk((), oracle)
        self.assertEqual("no_activation", result["primary"])

    def test_oracle_covers_frozen_pilot_and_stays_off_case_schema(self) -> None:
        cases = load_cases(PILOT)
        oracle = load_oracle(ORACLE)
        self.assertEqual(
            {case.identity for case in cases},
            set(oracle),
        )
        source = json.loads(PILOT.read_text(encoding="utf-8"))
        self.assertTrue(
            all("must_load" not in case and "expected_route" not in case for case in source["cases"])
        )

    def test_oracle_rejects_unknown_fields(self) -> None:
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        path = Path(temporary.name) / "oracle.json"
        path.write_text(
            json.dumps(
                {
                    "schema_version": 1,
                    "corpus_id": "x",
                    "description": "x",
                    "cases": {
                        "BEH-FAST-001@1.0.0": {
                            "walk": "fast_path",
                            "must_load": [],
                            "must_not_load": [],
                            "may_load": [],
                            "handoff": [],
                            "expected_route": "content.core",
                        }
                    },
                }
            ),
            encoding="utf-8",
        )

        with self.assertRaisesRegex(ValidationError, "unknown oracle case"):
            load_oracle(path)


class TraceCliTests(unittest.TestCase):
    def invoke(self, arguments: list[str]) -> tuple[int, str]:
        stream = StringIO()
        with redirect_stdout(stream), redirect_stderr(stream):
            code = main(arguments)
        return code, stream.getvalue()

    def test_trace_reconstructs_synthetic_bundle_without_touching_packets(self) -> None:
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        results = Path(temporary.name) / "results"
        results.mkdir()
        record = RunRecord(
            run_id="RUN-TRACE",
            case_identity="BEH-PAID-002@1.0.0",
            profile_id="current-skill",
            state=RunState.COMPLETED,
            started_at="2026-08-25T00:00:00Z",
            finished_at="2026-08-25T00:00:01Z",
            raw_events=(
                command_event(
                    "Get-Content -LiteralPath "
                    "'.agents\\skills\\marketing-practitioner\\SKILL.md' -Raw"
                ),
            ),
        )
        (results / "run-records.json").write_text(
            json.dumps(
                {
                    "schema_version": 1,
                    "runs": [
                        {
                            **{
                                key: (
                                    value.value
                                    if isinstance(value, RunState)
                                    else list(value)
                                    if isinstance(value, tuple)
                                    else value
                                )
                                for key, value in record.__dict__.items()
                            }
                        }
                    ],
                }
            ),
            encoding="utf-8",
        )
        output = Path(temporary.name) / "trace.json"

        code, text = self.invoke(
            [
                "trace",
                "--results",
                str(results),
                "--oracle",
                str(ORACLE),
                "--skill-root",
                str(ROOT / "skills" / "marketing-practitioner"),
                "--output",
                str(output),
            ]
        )

        self.assertEqual(0, code, text)
        report = json.loads(output.read_text(encoding="utf-8"))
        self.assertEqual(1, report["skill_run_count"])
        self.assertEqual("skip_jit", report["runs"][0]["classification"]["primary"])
        self.assertNotIn("packets", report)
        self.assertFalse((results / "blind-packets.json").exists())


if __name__ == "__main__":
    unittest.main()

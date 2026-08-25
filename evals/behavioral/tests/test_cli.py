from __future__ import annotations

import json
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from io import StringIO
from pathlib import Path

from evals.behavioral.behavioral_eval.cli import main


ROOT = Path(__file__).resolve().parents[3]
PILOT = ROOT / "evals" / "behavioral" / "cases" / "pilot-v1.json"
PROFILES = ROOT / "evals" / "behavioral" / "profiles"


class CliTests(unittest.TestCase):
    def invoke(self, arguments: list[str]) -> tuple[int, str]:
        stream = StringIO()
        with redirect_stdout(stream), redirect_stderr(stream):
            code = main(arguments)
        return code, stream.getvalue()

    def test_validate_rejects_duplicate_case_identities(self) -> None:
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        source = json.loads(PILOT.read_text(encoding="utf-8"))
        source["cases"].append(source["cases"][0])
        duplicate_path = Path(temporary.name) / "duplicate.json"
        duplicate_path.write_text(json.dumps(source), encoding="utf-8")

        code, output = self.invoke(
            ["validate", "--cases", str(duplicate_path), "--profiles", str(PROFILES)]
        )

        self.assertEqual(2, code)
        self.assertIn("duplicate case identity", output)

    def test_validate_accepts_frozen_corpus_and_profiles(self) -> None:
        code, output = self.invoke(
            ["validate", "--cases", str(PILOT), "--profiles", str(PROFILES)]
        )

        self.assertEqual(0, code)
        self.assertIn("PASS", output)
        self.assertIn("12 cases", output)

    def test_run_refuses_to_overwrite_existing_result_directory(self) -> None:
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        results = Path(temporary.name) / "sealed-results"
        results.mkdir()
        (results / "manifest.json").write_text("sealed", encoding="utf-8")

        code, output = self.invoke(
            [
                "run",
                "--cases",
                str(PILOT),
                "--profiles",
                str(PROFILES),
                "--adapter",
                "fixture",
                "--results",
                str(results),
            ]
        )

        self.assertEqual(2, code)
        self.assertIn("refusing to overwrite", output)

    def test_fixture_run_writes_atomic_bundle(self) -> None:
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        results = Path(temporary.name) / "fixture-results"

        code, output = self.invoke(
            [
                "run",
                "--cases",
                str(PILOT),
                "--profiles",
                str(PROFILES),
                "--adapter",
                "fixture",
                "--results",
                str(results),
                "--repo-root",
                str(ROOT),
                "--case-id",
                "BEH-FAST-001",
                "--repeat-limit",
                "1",
            ]
        )

        self.assertEqual(0, code, output)
        manifest = json.loads((results / "manifest.json").read_text(encoding="utf-8"))
        records = json.loads((results / "run-records.json").read_text(encoding="utf-8"))
        blind_index = json.loads((results / "blind-index.json").read_text(encoding="utf-8"))
        packets = json.loads((results / "blind-packets.json").read_text(encoding="utf-8"))
        self.assertTrue(manifest["sealed"])
        self.assertEqual(2, len(records["runs"]))
        self.assertEqual(2, len(blind_index["bindings"]))
        self.assertEqual(
            {item["blind_id"] for item in packets["packets"]},
            {item["blind_id"] for item in blind_index["bindings"]},
        )
        self.assertTrue(all("run_id" not in item for item in packets["packets"]))
        self.assertFalse(any(results.parent.glob(f".{results.name}.tmp-*")))


if __name__ == "__main__":
    unittest.main()

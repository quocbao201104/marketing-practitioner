from __future__ import annotations

import json
import unittest
from pathlib import Path

from evals.behavioral.behavioral_eval.challenger import controller_metrics


ROOT = Path(__file__).resolve().parents[3]
CURRENT = ROOT / "skills" / "marketing-practitioner"
CHALLENGER = (
    ROOT
    / "evals"
    / "behavioral"
    / "challengers"
    / "compact-controller"
    / "marketing-practitioner"
)


class CompactChallengerTests(unittest.TestCase):
    def test_challenger_retains_controller_contract_with_material_reduction(self) -> None:
        skill = (CHALLENGER / "SKILL.md").read_text(encoding="utf-8")
        routing = (CHALLENGER / "references" / "runtime-routing.md").read_text(
            encoding="utf-8"
        )
        combined = skill + "\n" + routing
        manifest = json.loads((CHALLENGER / "routing-index.json").read_text(encoding="utf-8"))

        self.assertIn('version: "0.9.0-compact.1"', skill)
        for job in ("WRITE", "DECIDE", "DIAGNOSE", "RESEARCH / UNDERSTAND", "ADAPT", "TEST", "LEARN"):
            self.assertIn(job, skill)
        for heading in (
            "Source fidelity",
            "Scope and proof",
            "counterevidence",
            "false precision",
            "Strategy must constrain communication",
            "meaningful choice",
        ):
            self.assertIn(heading.lower(), skill.lower())
        for namespace in manifest["namespaces"]:
            self.assertIn(namespace, combined)
        for boundary in (
            "platform observation",
            "discovery observation",
            "paid-media observation",
            "commerce observation",
            "email observation",
            "diagnosis → decision",
            "causal result → learning",
        ):
            self.assertIn(boundary, combined.lower())

        current = controller_metrics(CURRENT)
        compact = controller_metrics(CHALLENGER)
        self.assertLessEqual(compact["words"], int(current["words"] * 0.75))

    def test_challenger_is_a_complete_resource_copy(self) -> None:
        required = {
            path.relative_to(CURRENT).as_posix()
            for path in CURRENT.rglob("*")
            if path.is_file() and "__pycache__" not in path.parts
        }
        available = {
            path.relative_to(CHALLENGER).as_posix()
            for path in CHALLENGER.rglob("*")
            if path.is_file() and "__pycache__" not in path.parts
        }

        self.assertTrue(required - {"SKILL.md"} <= available)
        self.assertIn("references/runtime-routing.md", available)


if __name__ == "__main__":
    unittest.main()

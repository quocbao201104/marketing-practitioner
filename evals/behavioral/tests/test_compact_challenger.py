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

    def test_challenger_snapshot_routes_are_self_contained(self) -> None:
        """Validate the rejected challenger against its own frozen route snapshot.

        The compact challenger is retained as a historical experiment, not as a
        live mirror of the current skill. New production resources therefore
        must not make this snapshot fail merely because they did not exist when
        the challenger was executed. Its own routes still have to remain fully
        addressable inside the retained snapshot.
        """
        manifest = json.loads((CHALLENGER / "routing-index.json").read_text(encoding="utf-8"))

        for namespace, spec in manifest["namespaces"].items():
            resource = CHALLENGER / spec["path"]
            self.assertTrue(
                resource.is_file(),
                f"frozen challenger namespace {namespace!r} is missing {spec['path']!r}",
            )
            text = resource.read_text(encoding="utf-8")

            for section_id, selector in spec["sections"].items():
                if isinstance(selector, str):
                    self.assertIn(
                        selector,
                        text,
                        f"frozen challenger route {namespace}.{section_id} has a missing heading selector",
                    )
                    continue

                self.assertIsInstance(
                    selector,
                    dict,
                    f"frozen challenger route {namespace}.{section_id} has an invalid selector",
                )
                marker_id = selector.get("marker")
                self.assertIsInstance(
                    marker_id,
                    str,
                    f"frozen challenger route {namespace}.{section_id} has an invalid marker selector",
                )
                self.assertIn(f"<!-- route:start {marker_id} -->", text)
                self.assertIn(f"<!-- route:end {marker_id} -->", text)

        for support_file in (
            "TASK-SPECIFICATION-GUIDE.md",
            "references/runtime-routing.md",
            "scripts/get-knowledge.py",
            "scripts/test-knowledge-routing.py",
        ):
            self.assertTrue(
                (CHALLENGER / support_file).is_file(),
                f"frozen challenger support resource is missing: {support_file}",
            )


if __name__ == "__main__":
    unittest.main()

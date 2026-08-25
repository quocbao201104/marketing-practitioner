from __future__ import annotations

import os
import tempfile
import unittest
from pathlib import Path

from evals.behavioral.behavioral_eval.models import ArmProfile, CaseContract
from evals.behavioral.behavioral_eval.workspace import (
    WorkspaceError,
    build_run_workspace,
    hash_tree,
    preflight_workspace,
)


def make_case(input_files: list[str] | None = None) -> CaseContract:
    return CaseContract.from_dict(
        {
            "case_id": "BEH-FAST-001",
            "version": "1.0.0",
            "family": "fast-path",
            "prompt": "Return one bounded answer.",
            "input_files": input_files or [],
            "hard_predicates": [{"type": "output_present"}],
            "review_criteria": ["Stays bounded."],
            "forbidden_disclosures": ["arm identity"],
            "expected_relation": "skill_not_worse",
            "provenance": {
                "source": "fixture",
                "frozen_at_commit": "a" * 40,
            },
        }
    )


def make_profile(skill_mode: str = "none") -> ArmProfile:
    return ArmProfile.from_dict(
        {
            "profile_id": "baseline" if skill_mode == "none" else "current-skill",
            "adapter": "fixture",
            "model": "fixture-model",
            "reasoning_effort": "medium",
            "skill_mode": skill_mode,
            "skill_source": (
                None if skill_mode == "none" else "skills/marketing-practitioner"
            ),
            "expected_skill_sha256": (
                None if skill_mode == "none" else "computed-at-run-bind"
            ),
            "timeout_seconds": 30,
            "repetitions": 2,
        }
    )


class WorkspaceTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.repo = self.root / "repo"
        self.repo.mkdir()

    def test_tree_hash_ignores_mtime_and_detects_bytes_and_paths(self) -> None:
        tree = self.root / "tree"
        tree.mkdir()
        item = tree / "a.txt"
        item.write_text("same", encoding="utf-8")
        original = hash_tree(tree)

        os.utime(item, (1, 1))
        self.assertEqual(original, hash_tree(tree))

        item.write_text("changed", encoding="utf-8")
        self.assertNotEqual(original, hash_tree(tree))
        item.write_text("same", encoding="utf-8")
        item.rename(tree / "b.txt")
        self.assertNotEqual(original, hash_tree(tree))

    def test_baseline_preflight_rejects_skill_contamination(self) -> None:
        binding = build_run_workspace(
            make_case(), make_profile(), self.repo, self.root / "baseline"
        )
        contaminated = (
            binding.root / ".agents" / "skills" / "marketing-practitioner"
        )
        contaminated.mkdir(parents=True)
        (contaminated / "SKILL.md").write_text("contaminated", encoding="utf-8")

        errors = preflight_workspace(binding)

        self.assertIn("baseline contains marketing-practitioner", errors)

    def test_skill_workspace_binds_exact_copied_hash(self) -> None:
        source = self.repo / "skills" / "marketing-practitioner"
        source.mkdir(parents=True)
        (source / "SKILL.md").write_text("skill bytes", encoding="utf-8")

        binding = build_run_workspace(
            make_case(), make_profile("workspace-copy"), self.repo, self.root / "skill"
        )

        self.assertEqual(hash_tree(source), binding.expected_skill_sha256)
        self.assertEqual([], preflight_workspace(binding))

    def test_input_path_cannot_escape_repository(self) -> None:
        with self.assertRaisesRegex(WorkspaceError, "escapes repository root"):
            build_run_workspace(
                make_case(["../secret.txt"]),
                make_profile(),
                self.repo,
                self.root / "escaped",
            )


if __name__ == "__main__":
    unittest.main()

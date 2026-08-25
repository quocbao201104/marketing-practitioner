from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from scripts.validate_skill import validate_skill


REPO_ROOT = Path(__file__).resolve().parents[3]


class PackageValidationTests(unittest.TestCase):
    def make_skill(self, frontmatter: str, body: str = "# Test Skill\n") -> Path:
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        root = Path(temporary.name) / "test-skill"
        root.mkdir()
        (root / "SKILL.md").write_text(
            f"---\n{frontmatter}---\n\n{body}", encoding="utf-8"
        )
        return root

    def test_rejects_description_over_1024_characters(self) -> None:
        root = self.make_skill(
            'name: test-skill\ndescription: "' + ("a" * 1025) + '"\n'
        )

        errors = validate_skill(root)

        self.assertIn("description exceeds 1024 characters", errors)

    def test_rejects_directory_name_that_differs_from_skill_name(self) -> None:
        root = self.make_skill('name: different-name\ndescription: "Useful skill."\n')

        errors = validate_skill(root)

        self.assertIn(
            "skill name 'different-name' does not match directory 'test-skill'", errors
        )

    def test_accepts_nested_optional_metadata(self) -> None:
        root = self.make_skill(
            'name: test-skill\ndescription: "Useful skill."\nmetadata:\n'
            '  version: "1.0.0"\n'
        )

        errors = validate_skill(root)

        self.assertEqual([], errors)

    def test_rejects_default_prompt_without_explicit_skill_name(self) -> None:
        root = self.make_skill('name: test-skill\ndescription: "Useful skill."\n')
        agents = root / "agents"
        agents.mkdir()
        (agents / "openai.yaml").write_text(
            "interface:\n"
            '  display_name: "Test Skill"\n'
            '  short_description: "Useful decisions from evidence"\n'
            '  default_prompt: "Help me make a decision."\n',
            encoding="utf-8",
        )

        errors = validate_skill(root)

        self.assertIn(
            "interface.default_prompt must mention $test-skill explicitly", errors
        )

    def test_repository_skill_has_valid_frontmatter_and_ui_metadata(self) -> None:
        skill_root = REPO_ROOT / "skills" / "marketing-practitioner"
        openai_yaml = skill_root / "agents" / "openai.yaml"

        errors = validate_skill(skill_root)

        self.assertTrue(openai_yaml.is_file())
        self.assertEqual([], errors)


if __name__ == "__main__":
    unittest.main()

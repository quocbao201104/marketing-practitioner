from __future__ import annotations

import subprocess
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
VERIFY = ROOT / "scripts" / "verify.ps1"
VALID_SKILL = ROOT / "skills" / "marketing-practitioner"


class VerificationEntrypointTests(unittest.TestCase):
    def invoke(self, skill_path: Path) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [
                "powershell",
                "-NoProfile",
                "-File",
                str(VERIFY),
                "-SkillPath",
                str(skill_path),
                "-PackageOnly",
            ],
            cwd=ROOT,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            check=False,
        )

    def test_package_only_propagates_invalid_skill_failure(self) -> None:
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        skill = Path(temporary.name) / "invalid-skill"
        skill.mkdir()
        description = "x" * 1025
        (skill / "SKILL.md").write_text(
            f"---\nname: invalid-skill\ndescription: {description}\n---\n# Invalid\n",
            encoding="utf-8",
        )

        completed = self.invoke(skill)

        self.assertNotEqual(0, completed.returncode)
        self.assertIn(
            "description exceeds 1024 characters",
            completed.stderr + completed.stdout,
        )

    def test_package_only_accepts_repository_skill(self) -> None:
        completed = self.invoke(VALID_SKILL)

        self.assertEqual(0, completed.returncode, completed.stderr + completed.stdout)
        self.assertIn("repository package validator: PASS", completed.stdout)
        self.assertRegex(
            completed.stdout,
            r"current Codex validator: (PASS|SKIP)",
        )


if __name__ == "__main__":
    unittest.main()

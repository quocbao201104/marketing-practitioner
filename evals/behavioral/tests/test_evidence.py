from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from evals.behavioral.behavioral_eval.evidence import redact_text, seal_bytes


class EvidenceTests(unittest.TestCase):
    def test_redacts_absolute_paths_and_secret_values(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary).resolve()
            secret = "sk-example-secret-value"
            text = f"root={root} token={secret}"

            redacted = redact_text(text, [root], [secret])

        self.assertNotIn(str(root), redacted)
        self.assertNotIn(secret, redacted)
        self.assertIn("<WORKSPACE>", redacted)
        self.assertIn("<REDACTED>", redacted)

    def test_seal_bytes_matches_known_sha256(self) -> None:
        self.assertEqual(
            "ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad",
            seal_bytes(b"abc"),
        )


if __name__ == "__main__":
    unittest.main()

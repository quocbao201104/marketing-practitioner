from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from fixtures import run_all_fixtures
from preflight import run_preflight


class PreflightTests(unittest.TestCase):
    def test_all_21_fixtures_are_present_and_pass(self):
        results = run_all_fixtures()
        self.assertEqual(21, len(results))
        self.assertEqual([], [result.fixture_id for result in results if not result.passed])

    def test_preflight_is_non_compensatory(self):
        report = run_preflight()
        self.assertEqual("PASS", report["gate"])
        self.assertTrue(report["all_valid_material_fixtures_correctly_classified"])
        self.assertFalse(report["live_trials_permitted"])


if __name__ == "__main__":
    unittest.main()

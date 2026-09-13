from __future__ import annotations

import json
import unittest
from pathlib import Path

from evals.behavioral.behavioral_eval.trace import load_oracle


REPO_ROOT = Path(__file__).resolve().parents[3]
CASES_PATH = REPO_ROOT / "evals" / "behavioral" / "cases" / "founder-led-sales-runtime-v1.json"
ORACLE_PATH = REPO_ROOT / "evals" / "behavioral" / "oracles" / "founder-led-sales-runtime-v1.route-oracle.json"
ROUTING_INDEX = REPO_ROOT / "skills" / "marketing-practitioner" / "routing-index.json"
REPAIRED_CANDIDATE = "3968aff927731e0dc8fb1ce6524cc2282f89333a"
EXPECTED_IDENTITIES = {
    "BEH-FLS-RUNTIME-001@1.0.0",
    "BEH-FLS-RUNTIME-005@1.0.0",
    "BEH-FLS-RUNTIME-007@1.0.0",
    "BEH-FLS-RUNTIME-010@1.0.0",
    "BEH-FLS-RUNTIME-011@1.0.0",
    "BEH-FLS-RUNTIME-013@1.0.0",
    "BEH-FLS-RUNTIME-015@1.0.0",
    "BEH-FLS-RUNTIME-016@1.0.0",
}


class FounderSalesRuntimeOracleTests(unittest.TestCase):
    def test_case_and_oracle_identities_are_exactly_frozen_subset(self) -> None:
        document = json.loads(CASES_PATH.read_text(encoding="utf-8"))
        identities = {
            f"{case['case_id']}@{case['version']}"
            for case in document["cases"]
        }
        self.assertEqual(EXPECTED_IDENTITIES, identities)
        self.assertEqual(EXPECTED_IDENTITIES, set(load_oracle(ORACLE_PATH)))

    def test_cases_remain_bound_to_repaired_candidate(self) -> None:
        document = json.loads(CASES_PATH.read_text(encoding="utf-8"))
        for case in document["cases"]:
            self.assertEqual(
                REPAIRED_CANDIDATE,
                case["provenance"]["frozen_at_commit"],
                case["case_id"],
            )

    def test_all_founder_sales_oracle_routes_exist(self) -> None:
        index = json.loads(ROUTING_INDEX.read_text(encoding="utf-8"))
        sections = index["namespaces"]["founder-sales"]["sections"]
        logical_ids = {f"founder-sales.{key}" for key in sections}
        oracle = load_oracle(ORACLE_PATH)

        referenced: set[str] = set()
        for spec in oracle.values():
            for group in spec.must_load:
                referenced.update(item for item in group if item.startswith("founder-sales."))
            referenced.update(item for item in spec.must_not_load if item.startswith("founder-sales."))
            referenced.update(item for item in spec.may_load if item.startswith("founder-sales."))
            referenced.update(item for item in spec.handoff if item.startswith("founder-sales."))

        self.assertTrue(referenced)
        self.assertEqual(set(), referenced - logical_ids)

    def test_oracle_requires_exact_owner_routes_for_path_proof(self) -> None:
        oracle = load_oracle(ORACLE_PATH)
        for identity, spec in oracle.items():
            self.assertTrue(spec.must_load, identity)
            for group in spec.must_load:
                self.assertTrue(
                    any(item.startswith("founder-sales.") for item in group),
                    identity,
                )


if __name__ == "__main__":
    unittest.main()

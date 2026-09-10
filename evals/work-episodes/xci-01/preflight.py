from __future__ import annotations

import json
from dataclasses import asdict

from fixtures import EXPECTED_FIXTURE_IDS, run_all_fixtures


def run_preflight() -> dict:
    results = run_all_fixtures()
    ids = [result.fixture_id for result in results]
    expected = list(EXPECTED_FIXTURE_IDS)
    identity_ok = len(results) == len(expected) and len(ids) == len(set(ids)) and set(ids) == set(expected)
    failed = [result.fixture_id for result in results if not result.passed]
    gate_pass = identity_ok and not failed
    return {
        "gate": "PASS" if gate_pass else "FAIL",
        "all_valid_material_fixtures_correctly_classified": gate_pass,
        "fixture_count": len(results),
        "expected_fixture_count": len(expected),
        "fixture_identity_ok": identity_ok,
        "failed": failed,
        "results": [asdict(result) for result in results],
        "live_trials_permitted": False,
        "semantic_judge_adapter_validated": False,
        "episode_classification": "synthetic-targeted-diagnostic",
        "note": (
            "Passing deterministic preflight validates only the SWE-XCI-01 reference state/evaluator contract and planted semantic fixtures. "
            "It is not live Marketing Practitioner evidence and does not validate a semantic judge adapter."
        ),
    }


def main() -> int:
    report = run_preflight()
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report["gate"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())

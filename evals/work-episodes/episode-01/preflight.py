from __future__ import annotations

import json
from dataclasses import asdict

from fixtures import EXPECTED_FIXTURE_IDS, run_all_fixtures


def run_preflight() -> dict:
    results = run_all_fixtures()
    ids = [result.fixture_id for result in results]
    expected = list(EXPECTED_FIXTURE_IDS)
    identity_ok = (
        len(results) == len(expected)
        and len(ids) == len(set(ids))
        and set(ids) == set(expected)
    )
    failed = [result.fixture_id for result in results if not result.passed]
    gate_pass = identity_ok and not failed
    return {
        "gate": "PASS" if gate_pass else "FAIL",
        "all_valid_material_fixtures_correctly_classified": gate_pass,
        "fixture_count": len(results),
        "expected_fixture_count": len(expected),
        "fixture_identity_ok": identity_ok,
        "missing_fixture_ids": sorted(set(expected) - set(ids)),
        "unexpected_fixture_ids": sorted(set(ids) - set(expected)),
        "duplicate_fixture_ids": sorted({item for item in ids if ids.count(item) > 1}),
        "failed": failed,
        "results": [asdict(result) for result in results],
        "live_trials_permitted": False,
        "semantic_judge_adapter_validated": False,
        "note": (
            "Passing deterministic preflight validates only the frozen reference state machine and planted fixtures. "
            "Live no-skill/skill execution remains locked until a separately frozen evidence-grounded semantic-judge "
            "adapter passes its own preflight and independent review."
        ),
    }


def main() -> int:
    report = run_preflight()
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report["gate"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())

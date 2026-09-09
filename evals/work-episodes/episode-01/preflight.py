from __future__ import annotations

import json
from dataclasses import asdict

from fixtures import run_all_fixtures


def run_preflight() -> dict:
    results = run_all_fixtures()
    failed = [result.fixture_id for result in results if not result.passed]
    return {
        "gate": "PASS" if not failed else "FAIL",
        "all_valid_material_fixtures_correctly_classified": not failed,
        "fixture_count": len(results),
        "failed": failed,
        "results": [asdict(result) for result in results],
        "live_trials_permitted": False,
        "note": (
            "Passing preflight validates only the planted evaluator fixtures and deterministic Episode 01 plumbing. "
            "Live no-skill/skill execution remains separately run-locked."
        ),
    }


def main() -> int:
    report = run_preflight()
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report["gate"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any, Iterable


POSITIVE_CASE = "BI-LIVE-001@1.0.0"
NEGATIVE_CASE = "BI-LIVE-002@1.0.0"
PROFILE_ID = "current-skill"
EQUITY_HEADING = "## 2. Existing equity, candidate distinctiveness, and redesign"
CHAPTER_15 = "15-brand-identity-and-visual-systems.md"
POSITIONING_CHAPTER = "03-positioning-and-value.md"
ROUTE_RE = re.compile(
    r"(?<![a-z0-9.-])brand-identity\."
    r"(core|equity|exploration|refinement|evaluation|system|handoffs|decision-record|invariants)"
    r"(?![a-z0-9.-])",
    re.IGNORECASE,
)


def _walk_strings(value: Any) -> Iterable[str]:
    if isinstance(value, str):
        yield value
    elif isinstance(value, dict):
        for key, item in value.items():
            yield str(key)
            yield from _walk_strings(item)
    elif isinstance(value, list):
        for item in value:
            yield from _walk_strings(item)


def _normalize(value: str) -> str:
    return re.sub(r"/+", "/", value.lower().replace("\\", "/"))


def _command_items(events: list[dict[str, Any]]) -> list[tuple[int, dict[str, Any]]]:
    result: list[tuple[int, dict[str, Any]]] = []
    for index, event in enumerate(events):
        if str(event.get("type", "")).lower() != "item.completed":
            continue
        item = event.get("item")
        if not isinstance(item, dict) or item.get("type") != "command_execution":
            continue
        result.append((index, item))
    return result


def _activation_index(events: list[dict[str, Any]]) -> int | None:
    for index, event in enumerate(events):
        event_type = str(event.get("type", "")).lower()
        values = " ".join(_walk_strings(event)).lower()
        if (
            "skill" in event_type
            and "activat" in event_type
            and "marketing-practitioner" in values
        ):
            return index

        item = event.get("item")
        if not isinstance(item, dict) or item.get("type") != "command_execution":
            continue
        if item.get("exit_code") != 0:
            continue
        command = _normalize(str(item.get("command", "")))
        if "marketing-practitioner/skill.md" not in command:
            continue
        if any(
            reader in command
            for reader in (
                "get-content",
                "readalltext",
                "readalllines",
                "readallbytes",
                "readlines",
                " cat ",
                "type ",
            )
        ):
            return index
    return None


def _route_calls(events: list[dict[str, Any]]) -> list[dict[str, Any]]:
    calls: list[dict[str, Any]] = []
    for index, item in _command_items(events):
        command = _normalize(str(item.get("command", "")))
        if "get-knowledge.py" not in command:
            continue
        matches = list(ROUTE_RE.finditer(command))
        if not matches:
            continue
        output_value = {key: value for key, value in item.items() if key != "command"}
        output_text = "\n".join(_walk_strings(output_value))
        for match in matches:
            calls.append(
                {
                    "event_index": index,
                    "route": f"brand-identity.{match.group(1).lower()}",
                    "exit_code": item.get("exit_code"),
                    "delivered_equity_heading": EQUITY_HEADING.lower()
                    in output_text.lower(),
                    "command": str(item.get("command", "")),
                }
            )
    return calls


def _path_reads(events: list[dict[str, Any]], filename: str) -> list[int]:
    filename = filename.lower()
    return [
        index
        for index, item in _command_items(events)
        if filename in _normalize(str(item.get("command", "")))
        and item.get("exit_code") == 0
    ]


def _find_run(document: dict[str, Any], case_identity: str) -> dict[str, Any]:
    runs = [
        run
        for run in document.get("runs", [])
        if run.get("case_identity") == case_identity
        and run.get("profile_id") == PROFILE_ID
    ]
    if len(runs) != 1:
        raise ValueError(
            f"expected exactly one {PROFILE_ID} run for {case_identity}; found {len(runs)}"
        )
    return runs[0]


def analyze_positive(run: dict[str, Any]) -> dict[str, Any]:
    events = list(run.get("raw_events") or [])
    calls = _route_calls(events)
    activation_index = _activation_index(events)
    equity_calls = [call for call in calls if call["route"] == "brand-identity.equity"]
    first_route = calls[0]["route"] if calls else None
    chapter_reads = _path_reads(events, CHAPTER_15)
    positioning_reads = _path_reads(events, POSITIONING_CHAPTER)
    unwanted_routes = [
        call["route"]
        for call in calls
        if call["route"] in {"brand-identity.core", "brand-identity.exploration"}
    ]

    delivered = any(
        call["exit_code"] == 0 and call["delivered_equity_heading"]
        for call in equity_calls
    )
    first_equity_index = equity_calls[0]["event_index"] if equity_calls else None
    order_ok = (
        activation_index is not None
        and first_equity_index is not None
        and activation_index < first_equity_index
    )
    mechanical_pass = all(
        (
            run.get("exit_code") == 0,
            bool((run.get("final_output") or "").strip()),
            activation_index is not None,
            bool(equity_calls),
            first_route == "brand-identity.equity",
            delivered,
            order_ok,
            not unwanted_routes,
            not positioning_reads,
        )
    )
    return {
        "case_identity": POSITIVE_CASE,
        "mechanical_pass": mechanical_pass,
        "run_state": run.get("state"),
        "skill_activation_event_index": activation_index,
        "route_calls": calls,
        "chapter_15_read_event_indices": chapter_reads,
        "positioning_read_event_indices": positioning_reads,
        "first_route": first_route,
        "equity_resource_delivered": delivered,
        "activation_precedes_equity": order_ok,
        "unwanted_routes": unwanted_routes,
        "final_output": run.get("final_output"),
        "manual_semantic_checks": [
            "Preserves UNMEASURED != ZERO != PROVEN.",
            "Does not treat team boredom as buyer-memory evidence.",
            "Does not reopen positioning or exploration without a material dependency.",
        ],
    }


def analyze_negative(run: dict[str, Any]) -> dict[str, Any]:
    events = list(run.get("raw_events") or [])
    calls = _route_calls(events)
    chapter_reads = _path_reads(events, CHAPTER_15)
    operational_ok = (
        run.get("exit_code") == 0 and bool((run.get("final_output") or "").strip())
    )
    no_deep_identity = not calls and not chapter_reads
    mechanical_pass = operational_ok and no_deep_identity
    return {
        "case_identity": NEGATIVE_CASE,
        "mechanical_pass": mechanical_pass,
        "run_state": run.get("state"),
        "skill_activation_event_index": _activation_index(events),
        "route_calls": calls,
        "chapter_15_read_event_indices": chapter_reads,
        "no_deep_brand_identity_route": no_deep_identity,
        "final_output": run.get("final_output"),
        "manual_semantic_checks": [
            "Treats identity state as fixed and does not reopen strategy.",
            "Keeps the task on production/export execution only.",
            "Does not invent a new visual recommendation.",
        ],
        "note": (
            "ACTIVATION_UNVERIFIED is not itself a failure for this negative control; "
            "the material condition is absence of deep Brand Identity routing."
        ),
    }


def analyze_results(document: dict[str, Any]) -> dict[str, Any]:
    positive = analyze_positive(_find_run(document, POSITIVE_CASE))
    negative = analyze_negative(_find_run(document, NEGATIVE_CASE))
    return {
        "schema_version": 1,
        "probe": "BI-R01 live activation/path discrimination",
        "mechanical_trace_verdict": (
            "PASS"
            if positive["mechanical_pass"] and negative["mechanical_pass"]
            else "FAIL"
        ),
        "positive": positive,
        "negative": negative,
        "semantic_adjudication": "MANUAL_REQUIRED",
    }


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Check the two-case Brand Identity BI-R01 live activation/path probe."
    )
    parser.add_argument(
        "--results",
        required=True,
        help="behavioral harness result directory containing run-records.json",
    )
    parser.add_argument(
        "--output",
        help="optional JSON path for the probe analysis",
    )
    args = parser.parse_args()

    results = Path(args.results)
    document = json.loads((results / "run-records.json").read_text(encoding="utf-8"))
    analysis = analyze_results(document)
    rendered = json.dumps(analysis, indent=2, ensure_ascii=False, sort_keys=True)
    print(rendered)
    if args.output:
        Path(args.output).write_text(rendered + "\n", encoding="utf-8")
    return 0 if analysis["mechanical_trace_verdict"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())

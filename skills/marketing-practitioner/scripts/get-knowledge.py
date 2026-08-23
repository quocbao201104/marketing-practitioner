#!/usr/bin/env python3
"""Deterministically resolve logical knowledge IDs to the smallest indexed Markdown section."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = ROOT / "routing-index.json"
ROUTE_ID_RE = re.compile(r"^[a-z0-9]+(?:[.-][a-z0-9]+)*$")
HEADING_RE = re.compile(r"^(#{1,6})\s+\S")


class RoutingError(RuntimeError):
    pass


def load_manifest() -> dict:
    try:
        data = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise RoutingError(f"routing manifest not found: {MANIFEST_PATH}") from exc
    except json.JSONDecodeError as exc:
        raise RoutingError(f"invalid routing manifest JSON: {exc}") from exc

    if not isinstance(data.get("routes"), dict):
        raise RoutingError("routing manifest must contain an object named 'routes'")
    return data


def resolve_path(relative_path: str) -> Path:
    candidate = (ROOT / relative_path).resolve()
    try:
        candidate.relative_to(ROOT.resolve())
    except ValueError as exc:
        raise RoutingError(f"route escapes skill root: {relative_path}") from exc
    return candidate


def extract_heading_section(text: str, heading: str) -> str:
    lines = text.splitlines(keepends=True)
    matches = [i for i, line in enumerate(lines) if line.rstrip("\r\n") == heading]
    if len(matches) != 1:
        raise RoutingError(
            f"heading selector must match exactly once; found {len(matches)} for {heading!r}"
        )

    start = matches[0]
    match = HEADING_RE.match(lines[start])
    if not match:
        raise RoutingError(f"selector is not a Markdown heading: {heading!r}")
    level = len(match.group(1))

    end = len(lines)
    for i in range(start + 1, len(lines)):
        next_heading = HEADING_RE.match(lines[i])
        if next_heading and len(next_heading.group(1)) <= level:
            end = i
            break

    return "".join(lines[start:end]).strip()


def extract_marker_section(text: str, route_id: str) -> str:
    start_marker = f"<!-- route:start {route_id} -->"
    end_marker = f"<!-- route:end {route_id} -->"

    if text.count(start_marker) != 1 or text.count(end_marker) != 1:
        raise RoutingError(
            f"marker selector requires exactly one start/end pair for {route_id!r}"
        )

    start = text.index(start_marker) + len(start_marker)
    end = text.index(end_marker, start)
    if end < start:
        raise RoutingError(f"end marker precedes start marker for {route_id!r}")
    return text[start:end].strip()


def get_knowledge(route_id: str, manifest: dict | None = None) -> tuple[dict, str]:
    manifest = manifest or load_manifest()
    routes = manifest["routes"]
    if route_id not in routes:
        raise RoutingError(f"unknown knowledge route: {route_id}")

    route = routes[route_id]
    path = resolve_path(route["path"])
    if not path.is_file():
        raise RoutingError(f"route target does not exist: {route['path']}")

    text = path.read_text(encoding="utf-8")
    selector = route.get("selector") or {}
    selector_type = selector.get("type")

    if selector_type == "heading":
        content = extract_heading_section(text, selector.get("value", ""))
    elif selector_type == "marker":
        content = extract_marker_section(text, selector.get("id", route_id))
    else:
        raise RoutingError(f"unsupported selector type for {route_id}: {selector_type!r}")

    return route, content


def validate_manifest(manifest: dict) -> list[str]:
    errors: list[str] = []
    for route_id, route in manifest["routes"].items():
        if not ROUTE_ID_RE.fullmatch(route_id):
            errors.append(f"{route_id}: invalid logical ID")
            continue
        if not isinstance(route, dict):
            errors.append(f"{route_id}: route must be an object")
            continue
        if not isinstance(route.get("path"), str) or not route["path"]:
            errors.append(f"{route_id}: missing path")
            continue
        try:
            get_knowledge(route_id, manifest)
        except (RoutingError, OSError, UnicodeError) as exc:
            errors.append(f"{route_id}: {exc}")
    return errors


def print_route_list(manifest: dict) -> None:
    for route_id, route in manifest["routes"].items():
        use_when = route.get("use_when") or []
        hint = "; ".join(use_when[:3])
        print(f"{route_id}\t{hint}")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Resolve Marketing Practitioner knowledge IDs to exact Markdown sections."
    )
    parser.add_argument("route_ids", nargs="*", help="one or more logical knowledge IDs")
    parser.add_argument("--list", action="store_true", help="list available logical knowledge IDs")
    parser.add_argument("--validate", action="store_true", help="validate every indexed route")
    args = parser.parse_args()

    try:
        manifest = load_manifest()

        if args.validate:
            errors = validate_manifest(manifest)
            if errors:
                for error in errors:
                    print(f"FAIL\t{error}", file=sys.stderr)
                return 1
            print(f"PASS\t{len(manifest['routes'])} routes")
            return 0

        if args.list:
            print_route_list(manifest)
            return 0

        if not args.route_ids:
            parser.error("provide at least one route ID, or use --list / --validate")

        for position, route_id in enumerate(args.route_ids):
            route, content = get_knowledge(route_id, manifest)
            if position:
                print()
            if len(args.route_ids) > 1:
                print(f"--- knowledge:{route_id} ({route['path']}) ---")
            print(content)
        return 0

    except (RoutingError, OSError, UnicodeError) as exc:
        print(f"ERROR\t{exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())

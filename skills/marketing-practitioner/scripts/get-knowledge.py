#!/usr/bin/env python3
"""Deterministically resolve logical knowledge IDs to indexed Markdown sections."""

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

    if data.get("version") != 2:
        raise RoutingError(f"unsupported routing manifest version: {data.get('version')!r}")
    if not isinstance(data.get("namespaces"), dict):
        raise RoutingError("routing manifest must contain an object named 'namespaces'")
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


def extract_marker_section(text: str, marker_id: str) -> str:
    start_marker = f"<!-- route:start {marker_id} -->"
    end_marker = f"<!-- route:end {marker_id} -->"

    if text.count(start_marker) != 1 or text.count(end_marker) != 1:
        raise RoutingError(
            f"marker selector requires exactly one start/end pair for {marker_id!r}"
        )

    start = text.index(start_marker) + len(start_marker)
    end = text.index(end_marker, start)
    return text[start:end].strip()


def parse_route_id(route_id: str) -> tuple[str, str]:
    if not ROUTE_ID_RE.fullmatch(route_id) or "." not in route_id:
        raise RoutingError(f"invalid knowledge route: {route_id}")
    return route_id.split(".", 1)


def get_route(route_id: str, manifest: dict) -> tuple[str, object]:
    namespace, section = parse_route_id(route_id)
    namespaces = manifest["namespaces"]
    group = namespaces.get(namespace)
    if not isinstance(group, dict):
        raise RoutingError(f"unknown knowledge namespace: {namespace}")

    sections = group.get("sections")
    if not isinstance(sections, dict) or section not in sections:
        raise RoutingError(f"unknown knowledge route: {route_id}")

    path = group.get("path")
    if not isinstance(path, str) or not path:
        raise RoutingError(f"{namespace}: missing path")

    return path, sections[section]


def get_knowledge(route_id: str, manifest: dict | None = None) -> tuple[str, str]:
    manifest = manifest or load_manifest()
    relative_path, selector = get_route(route_id, manifest)
    path = resolve_path(relative_path)
    if not path.is_file():
        raise RoutingError(f"route target does not exist: {relative_path}")

    text = path.read_text(encoding="utf-8")
    if isinstance(selector, str):
        content = extract_heading_section(text, selector)
    elif isinstance(selector, dict) and isinstance(selector.get("marker"), str):
        content = extract_marker_section(text, selector["marker"])
    else:
        raise RoutingError(f"unsupported selector for {route_id}: {selector!r}")

    return relative_path, content


def iter_route_ids(manifest: dict, namespace: str | None = None):
    namespaces = manifest["namespaces"]
    selected = [namespace] if namespace else sorted(namespaces)
    for ns in selected:
        group = namespaces.get(ns)
        if not isinstance(group, dict):
            raise RoutingError(f"unknown knowledge namespace: {ns}")
        sections = group.get("sections")
        if not isinstance(sections, dict):
            raise RoutingError(f"{ns}: missing sections")
        for section in sections:
            yield f"{ns}.{section}"


def validate_manifest(manifest: dict) -> list[str]:
    errors: list[str] = []
    namespaces = manifest["namespaces"]

    for namespace, group in namespaces.items():
        if not ROUTE_ID_RE.fullmatch(namespace) or "." in namespace:
            errors.append(f"{namespace}: invalid namespace")
            continue
        if not isinstance(group, dict):
            errors.append(f"{namespace}: namespace must be an object")
            continue
        if not isinstance(group.get("path"), str) or not group["path"]:
            errors.append(f"{namespace}: missing path")
            continue
        sections = group.get("sections")
        if not isinstance(sections, dict) or not sections:
            errors.append(f"{namespace}: missing sections")
            continue

        for section in sections:
            route_id = f"{namespace}.{section}"
            try:
                get_knowledge(route_id, manifest)
            except (RoutingError, OSError, UnicodeError) as exc:
                errors.append(f"{route_id}: {exc}")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Resolve Marketing Practitioner knowledge IDs to exact Markdown sections."
    )
    parser.add_argument("route_ids", nargs="*", help="one or more logical knowledge IDs")
    parser.add_argument("--list", action="store_true", help="list logical knowledge IDs")
    parser.add_argument("--namespace", help="limit --list to one namespace")
    parser.add_argument("--namespaces", action="store_true", help="list available namespaces")
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
            count = sum(1 for _ in iter_route_ids(manifest))
            print(f"PASS\t{count} routes")
            return 0

        if args.namespaces:
            for namespace in sorted(manifest["namespaces"]):
                print(namespace)
            return 0

        if args.list:
            for route_id in iter_route_ids(manifest, args.namespace):
                print(route_id)
            return 0

        if args.namespace:
            parser.error("--namespace is only valid with --list")

        if not args.route_ids:
            parser.error("provide route IDs, or use --list / --namespaces / --validate")

        for position, route_id in enumerate(args.route_ids):
            relative_path, content = get_knowledge(route_id, manifest)
            if position:
                print()
            if len(args.route_ids) > 1:
                print(f"--- knowledge:{route_id} ({relative_path}) ---")
            print(content)
        return 0

    except (RoutingError, OSError, UnicodeError) as exc:
        print(f"ERROR\t{exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())

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
FENCE_OPEN_RE = re.compile(r"^ {0,3}(`{3,}|~{3,})(.*)$")
SOURCE_ID_RE = re.compile(r"^[A-Z][A-Z0-9-]*\d{2,}$")


class RoutingError(RuntimeError):
    pass


def reject_duplicate_keys(pairs):
    obj = {}
    for key, value in pairs:
        if key in obj:
            raise RoutingError(f"duplicate JSON key in routing manifest: {key}")
        obj[key] = value
    return obj


def load_manifest() -> dict:
    try:
        data = json.loads(
            MANIFEST_PATH.read_text(encoding="utf-8"),
            object_pairs_hook=reject_duplicate_keys,
        )
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


def iter_unfenced_lines(lines: list[str]):
    """Yield (index, line) pairs outside CommonMark-style fenced code blocks."""
    fence_char: str | None = None
    fence_len = 0

    for index, line in enumerate(lines):
        raw = line.rstrip("\r\n")

        if fence_char is not None:
            closing = re.match(
                rf"^ {{0,3}}{re.escape(fence_char)}{{{fence_len},}}[ \t]*$",
                raw,
            )
            if closing:
                fence_char = None
                fence_len = 0
            continue

        opening = FENCE_OPEN_RE.match(raw)
        if opening:
            token = opening.group(1)
            info = opening.group(2)
            # CommonMark does not allow a backtick in the info string of a
            # backtick fence. Treat such a line as ordinary text instead.
            if token[0] == "`" and "`" in info:
                yield index, line
                continue
            fence_char = token[0]
            fence_len = len(token)
            continue

        yield index, line


def extract_heading_section(text: str, heading: str) -> str:
    lines = text.splitlines(keepends=True)
    visible_lines = list(iter_unfenced_lines(lines))
    matches = [
        index
        for index, line in visible_lines
        if line.rstrip("\r\n") == heading
    ]
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
    for index, line in visible_lines:
        if index <= start:
            continue
        next_heading = HEADING_RE.match(line)
        if next_heading and len(next_heading.group(1)) <= level:
            end = index
            break

    return "".join(lines[start:end]).strip()


def extract_marker_section(text: str, marker_id: str) -> str:
    start_marker = f"<!-- route:start {marker_id} -->"
    end_marker = f"<!-- route:end {marker_id} -->"

    if text.count(start_marker) != 1 or text.count(end_marker) != 1:
        raise RoutingError(
            f"marker selector requires exactly one start/end pair for {marker_id!r}"
        )

    start_pos = text.index(start_marker)
    end_pos = text.index(end_marker)
    if end_pos <= start_pos:
        raise RoutingError(f"end marker precedes start marker for {marker_id!r}")

    start = start_pos + len(start_marker)
    return text[start:end_pos].strip()


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


def scan_sources() -> dict[str, list[tuple[Path, str]]]:
    references_root = ROOT / "references"
    if not references_root.is_dir():
        raise RoutingError(f"references directory not found: {references_root}")

    source_heading = re.compile(
        r"^(#{2,6})\s+\[([A-Z][A-Z0-9-]*\d{2,})\](?:\s+|$)"
    )
    sources: dict[str, list[tuple[Path, str]]] = {}

    for path in sorted(references_root.rglob("*.md")):
        text = path.read_text(encoding="utf-8")
        lines = text.splitlines(keepends=True)
        for _, line in iter_unfenced_lines(lines):
            match = source_heading.match(line.rstrip("\r\n"))
            if match:
                sources.setdefault(match.group(2), []).append(
                    (path, line.rstrip("\r\n"))
                )

    return sources


def validate_sources() -> list[str]:
    errors: list[str] = []
    try:
        sources = scan_sources()
    except (RoutingError, OSError, UnicodeError) as exc:
        return [str(exc)]

    for source_id, matches in sources.items():
        if len(matches) != 1:
            locations = ", ".join(str(path.relative_to(ROOT)) for path, _ in matches)
            errors.append(
                f"{source_id}: evidence source ID appears {len(matches)} times: {locations}"
            )
    return errors


def get_source(source_id: str) -> tuple[str, str]:
    source_id = source_id.upper()
    if not SOURCE_ID_RE.fullmatch(source_id):
        raise RoutingError(f"invalid evidence source ID: {source_id}")

    sources = scan_sources()
    matches = sources.get(source_id, [])

    if len(matches) != 1:
        raise RoutingError(
            f"evidence source ID must match exactly once; found {len(matches)} for {source_id}"
        )

    path, heading = matches[0]
    content = extract_heading_section(path.read_text(encoding="utf-8"), heading)
    return str(path.relative_to(ROOT)), content


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


def select_mode(args) -> str:
    if args.namespace and not args.list:
        raise RoutingError("--namespace is only valid with --list")

    modes: list[str] = []
    if args.route_ids:
        modes.append("routes")
    if args.source:
        modes.append("source")
    if args.list:
        modes.append("list")
    if args.namespaces:
        modes.append("namespaces")
    if args.validate:
        modes.append("validate")

    if len(modes) != 1:
        raise RoutingError(
            "choose exactly one mode: route IDs, --source, --list, --namespaces, or --validate"
        )
    return modes[0]


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Resolve Marketing Practitioner knowledge IDs to exact Markdown sections."
    )
    parser.add_argument("route_ids", nargs="*", help="one or more logical knowledge IDs")
    parser.add_argument("--list", action="store_true", help="list logical knowledge IDs")
    parser.add_argument("--namespace", help="limit --list to one namespace")
    parser.add_argument("--namespaces", action="store_true", help="list available namespaces")
    parser.add_argument("--validate", action="store_true", help="validate every indexed route")
    parser.add_argument(
        "--source",
        nargs="+",
        metavar="ID",
        help="resolve evidence source IDs such as R23, C14, or A03",
    )
    args = parser.parse_args()

    try:
        mode = select_mode(args)

        if mode == "source":
            for position, source_id in enumerate(args.source):
                relative_path, content = get_source(source_id)
                if position:
                    print()
                if len(args.source) > 1:
                    print(f"--- source:{source_id.upper()} ({relative_path}) ---")
                print(content)
            return 0

        manifest = load_manifest()

        if mode == "validate":
            errors = validate_manifest(manifest) + validate_sources()
            if errors:
                for error in errors:
                    print(f"FAIL\t{error}", file=sys.stderr)
                return 1
            route_count = sum(1 for _ in iter_route_ids(manifest))
            source_count = len(scan_sources())
            print(f"PASS\t{route_count} routes / {source_count} evidence sources")
            return 0

        if mode == "namespaces":
            for namespace in sorted(manifest["namespaces"]):
                print(namespace)
            return 0

        if mode == "list":
            for route_id in iter_route_ids(manifest, args.namespace):
                print(route_id)
            return 0

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

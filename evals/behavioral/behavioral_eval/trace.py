"""Reconstruct skill-graph walks from sealed executor events.

The walker oracle is a sidecar. It is never merged into case contracts or
blind packets. This module answers which skill nodes were actually read,
not whether the final answer was good.
"""

from __future__ import annotations

import json
import re
from collections import Counter, defaultdict
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Iterable

from .codex_cli import _normalize_path_text
from .models import RunRecord, RunState, ValidationError


ORACLE_SCHEMA_VERSION = 1
TRACE_SCHEMA_VERSION = 1
HELPER_ROUTE_RE = re.compile(r"^[a-z0-9]+(?:[.-][a-z0-9]+)*$")
SKILL_ROOT_RE = re.compile(
    r"marketing-practitioner/(?P<rel>(?:skill\.md|routing-index\.json|"
    r"handbook/|platforms/|references/|scripts/|frameworks/|agents/|adaptations/)[^\s'\"|<>]*)",
    re.I,
)
GET_KNOWLEDGE_RE = re.compile(
    r"get-knowledge\.py(?:['\"]|\s)+(?P<args>[^'\"\n]+)",
    re.I,
)
CONTEXT_DUMP_RE = re.compile(r"(?:-a|-c|-context)\s+(\d+)", re.I)
SLICE_RE = re.compile(
    r"select-object[^\n]*(?:-skip|-first|-totalcount)|-totalcount\s+\d+",
    re.I,
)
WHOLE_FILE_RE = re.compile(r"(?:-raw|readalltext|readalllines|readallbytes)\b", re.I)
PRIMARY_ORDER = (
    "no_activation",
    "skip_jit",
    "wrong_edge",
    "resolve_fail",
    "missing_handoff",
    "over_read",
    "loaded_but_ignore",
)
UNINDEXED_NAMESPACES = {
    "handbook/00-foundations-and-method.md": "foundations",
    "handbook/01-customer-research-and-evidence.md": "customer-research",
    "handbook/02-segmentation-icp-and-jtbd.md": "segmentation",
    "handbook/03-positioning-and-value.md": "positioning",
    "handbook/04-messaging-proof-and-copy.md": "message-copy",
    "handbook/05-diagnosis-causality-and-experimentation.md": "diagnosis",
    "handbook/06-organizational-learning.md": "learning",
    "handbook/07-international-and-ethical-marketing.md": "international",
}


@dataclass(frozen=True)
class WalkStep:
    kind: str
    path: str | None
    namespace: str | None
    logical_id: str | None
    grain: str
    exit_code: int | None
    succeeded: bool


@dataclass(frozen=True)
class OracleCase:
    identity: str
    walk: str
    must_load: tuple[tuple[str, ...], ...]
    must_not_load: tuple[str, ...]
    may_load: tuple[str, ...]
    handoff: tuple[str, ...]


def _exact_keys(data: dict[str, Any], expected: set[str], label: str) -> None:
    unknown = sorted(set(data) - expected)
    missing = sorted(expected - set(data))
    if unknown:
        raise ValidationError(f"unknown {label} fields: {', '.join(unknown)}")
    if missing:
        raise ValidationError(f"missing {label} fields: {', '.join(missing)}")


def _text_list(value: Any, label: str) -> tuple[str, ...]:
    if not isinstance(value, list):
        raise ValidationError(f"{label} must be an array")
    result: list[str] = []
    for item in value:
        if not isinstance(item, str) or not item.strip():
            raise ValidationError(f"{label} items must be non-empty text")
        result.append(item.strip())
    return tuple(result)


def _must_load_groups(value: Any) -> tuple[tuple[str, ...], ...]:
    if not isinstance(value, list):
        raise ValidationError("must_load must be an array of alternative groups")
    groups: list[tuple[str, ...]] = []
    for item in value:
        if isinstance(item, str) and item.strip():
            groups.append((item.strip(),))
            continue
        if not isinstance(item, list) or not item:
            raise ValidationError("must_load group must be a non-empty array")
        group = _text_list(item, "must_load group")
        groups.append(group)
    return tuple(groups)


def load_oracle(path: Path) -> dict[str, OracleCase]:
    document = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(document, dict):
        raise ValidationError("route oracle must be an object")
    _exact_keys(
        document,
        {"schema_version", "corpus_id", "description", "cases"},
        "route oracle",
    )
    if document["schema_version"] != ORACLE_SCHEMA_VERSION:
        raise ValidationError(
            f"unsupported route oracle schema: {document['schema_version']!r}"
        )
    if not isinstance(document["corpus_id"], str) or not document["corpus_id"].strip():
        raise ValidationError("corpus_id must be non-empty text")
    if not isinstance(document["description"], str) or not document["description"].strip():
        raise ValidationError("description must be non-empty text")
    cases = document["cases"]
    if not isinstance(cases, dict) or not cases:
        raise ValidationError("route oracle cases must be a non-empty object")
    parsed: dict[str, OracleCase] = {}
    for identity, payload in cases.items():
        if not isinstance(identity, str) or "@" not in identity:
            raise ValidationError(f"oracle case key must be case_id@version: {identity!r}")
        if not isinstance(payload, dict):
            raise ValidationError(f"oracle case {identity} must be an object")
        _exact_keys(
            payload,
            {"walk", "must_load", "must_not_load", "may_load", "handoff"},
            f"oracle case {identity}",
        )
        walk = payload["walk"]
        if walk not in {"fast_path", "jit"}:
            raise ValidationError(f"unsupported walk type: {walk}")
        parsed[identity] = OracleCase(
            identity=identity,
            walk=walk,
            must_load=_must_load_groups(payload["must_load"]),
            must_not_load=_text_list(payload["must_not_load"], "must_not_load"),
            may_load=_text_list(payload["may_load"], "may_load"),
            handoff=_text_list(payload["handoff"], "handoff"),
        )
    return parsed


def load_namespace_index(skill_root: Path) -> dict[str, str]:
    mapping = dict(UNINDEXED_NAMESPACES)
    manifest_path = skill_root / "routing-index.json"
    if not manifest_path.is_file():
        return mapping
    document = json.loads(manifest_path.read_text(encoding="utf-8"))
    namespaces = document.get("namespaces")
    if not isinstance(namespaces, dict):
        return mapping
    for name, spec in namespaces.items():
        if not isinstance(spec, dict):
            continue
        path = spec.get("path")
        if isinstance(path, str) and path.strip():
            mapping[_normalize_path_text(path.strip())] = str(name)
    return mapping


def _strip_relative(path: str) -> str:
    normalized = _normalize_path_text(path)
    normalized = re.sub(r"[.,;:]+$", "", normalized)
    marker = "marketing-practitioner/"
    if marker in normalized:
        normalized = normalized.split(marker, 1)[1]
    return normalized.strip("/")


def extract_skill_paths(command: str) -> tuple[str, ...]:
    normalized = _normalize_path_text(command)
    found: list[str] = []
    for match in SKILL_ROOT_RE.finditer(normalized):
        relative = _strip_relative(match.group("rel"))
        if relative and relative not in found:
            found.append(relative)
    return tuple(found)


def extract_helper_routes(command: str) -> tuple[str, ...]:
    normalized = _normalize_path_text(command)
    routes: list[str] = []
    for match in GET_KNOWLEDGE_RE.finditer(normalized):
        tokens = match.group("args").split()
        index = 0
        while index < len(tokens):
            token = tokens[index].strip("'\"")
            if token in {"--list", "--validate"}:
                index += 1
                continue
            if token in {"--source", "--namespace"}:
                index += 2
                continue
            if token.startswith("--"):
                index += 1
                continue
            if HELPER_ROUTE_RE.fullmatch(token) and token not in routes:
                routes.append(token)
            index += 1
    return tuple(routes)


def _grain_for_command(command: str) -> str:
    normalized = _normalize_path_text(command)
    dump = CONTEXT_DUMP_RE.search(normalized)
    if dump and int(dump.group(1)) >= 10:
        return "slice"
    if "rg --files" in normalized or re.search(r"\brg\b.*--files", normalized):
        return "probe"
    if re.search(r"\brg\b", normalized) and not dump:
        if "-n" in normalized.split() or "select-string" in normalized:
            return "probe"
        return "probe"
    if "select-string" in normalized and not dump:
        return "probe"
    if SLICE_RE.search(command):
        return "slice"
    if WHOLE_FILE_RE.search(command):
        return "whole_file"
    if "get-content" in normalized:
        return "whole_file"
    return "other"


def _namespace_for_path(path: str, namespaces: dict[str, str]) -> str | None:
    relative = _strip_relative(path)
    if relative == "skill.md":
        return "controller"
    if relative == "routing-index.json":
        return "index"
    if relative.startswith("scripts/"):
        return "helper"
    mapped = namespaces.get(relative)
    if mapped:
        return mapped
    for index_path, name in namespaces.items():
        if relative == index_path or relative.endswith("/" + index_path):
            return name
    if relative.startswith("platforms/commerce/"):
        stem = relative.rsplit("/", 1)[-1].removesuffix(".md")
        return stem
    if relative.startswith("platforms/"):
        return relative.split("/")[1].split(".")[0]
    if relative.startswith("handbook/"):
        return f"handbook-{relative.split('/', 1)[1][:2]}"
    if relative.startswith("references/"):
        return "references"
    return None


def reconstruct_steps(
    events: Iterable[dict[str, Any]],
    namespaces: dict[str, str] | None = None,
) -> tuple[WalkStep, ...]:
    index = namespaces or dict(UNINDEXED_NAMESPACES)
    steps: list[WalkStep] = []
    for event in events:
        if str(event.get("type", "")).lower() != "item.completed":
            continue
        item = event.get("item")
        if not isinstance(item, dict):
            continue
        item_type = item.get("type")
        if item_type == "web_search":
            steps.append(
                WalkStep(
                    kind="web_search",
                    path=None,
                    namespace=None,
                    logical_id=None,
                    grain="external",
                    exit_code=None,
                    succeeded=True,
                )
            )
            continue
        if item_type != "command_execution":
            continue
        command = str(item.get("command") or "")
        exit_code = item.get("exit_code")
        succeeded = exit_code == 0
        grain = _grain_for_command(command)
        routes = extract_helper_routes(command)
        paths = extract_skill_paths(command)
        if routes:
            for route in routes:
                steps.append(
                    WalkStep(
                        kind="helper",
                        path="scripts/get-knowledge.py",
                        namespace=route.split(".", 1)[0],
                        logical_id=route,
                        grain="helper_route",
                        exit_code=exit_code if isinstance(exit_code, int) else None,
                        succeeded=succeeded,
                    )
                )
            continue
        if not paths:
            continue
        for path in paths:
            namespace = _namespace_for_path(path, index)
            if path == "skill.md":
                kind = "controller"
            elif path == "routing-index.json":
                kind = "index"
            elif path.startswith("scripts/"):
                kind = "probe" if grain == "probe" else "helper"
            elif grain == "probe":
                kind = "probe"
            else:
                kind = "knowledge"
            steps.append(
                WalkStep(
                    kind=kind,
                    path=path,
                    namespace=namespace,
                    logical_id=None,
                    grain=grain,
                    exit_code=exit_code if isinstance(exit_code, int) else None,
                    succeeded=succeeded,
                )
            )
    return tuple(steps)


def _spec_matches(spec: str, step: WalkStep) -> bool:
    needle = _normalize_path_text(spec).strip("/")
    if not step.succeeded:
        return False
    if step.kind in {"probe", "web_search"}:
        return False
    if step.logical_id and (
        step.logical_id == needle or step.logical_id.startswith(needle + ".")
    ):
        return True
    if step.namespace and (
        step.namespace == needle or needle == step.namespace + "/"
    ):
        return True
    path = step.path or ""
    if path == needle or path.startswith(needle):
        return True
    if needle.endswith("/") and path.startswith(needle):
        return True
    return False


def _successful_knowledge(steps: Iterable[WalkStep]) -> tuple[WalkStep, ...]:
    return tuple(
        step
        for step in steps
        if step.succeeded and step.kind in {"knowledge", "helper"}
    )


def _controller_activated(steps: Iterable[WalkStep]) -> bool:
    return any(
        step.kind == "controller" and step.succeeded and step.path == "skill.md"
        for step in steps
    )


def _group_satisfied(group: tuple[str, ...], loads: Iterable[WalkStep]) -> bool:
    return any(
        _spec_matches(spec, step) for spec in group for step in loads
    )


def _attempted_spec(spec: str, steps: Iterable[WalkStep]) -> bool:
    needle = _normalize_path_text(spec).strip("/")
    for step in steps:
        if step.kind == "web_search":
            continue
        if step.logical_id and (
            step.logical_id == spec or step.logical_id.startswith(spec + ".")
        ):
            return True
        path = _normalize_path_text(step.path or "")
        if path and (path == needle or path.startswith(needle)):
            return True
        if step.namespace and (
            step.namespace == spec or spec.startswith(step.namespace + ".")
        ):
            return True
    return False


def classify_skill_walk(
    steps: tuple[WalkStep, ...],
    oracle: OracleCase,
    *,
    answer_disposition: str | None = None,
) -> dict[str, Any]:
    loads = _successful_knowledge(steps)
    labels: list[str] = []
    missing_groups: list[tuple[str, ...]] = []
    forbidden_hits: list[str] = []
    failed_required_attempts: list[str] = []

    activated = _controller_activated(steps)
    if not activated:
        labels.append("no_activation")

    for group in oracle.must_load:
        if _group_satisfied(group, loads):
            continue
        missing_groups.append(group)
        if any(_attempted_spec(spec, steps) for spec in group):
            failed_required_attempts.extend(group)

    if missing_groups and activated:
        if failed_required_attempts:
            labels.append("resolve_fail")
        labels.append("skip_jit")

    allowed_specs = (
        *oracle.may_load,
        *(spec for group in oracle.must_load for spec in group),
        *oracle.handoff,
        "skill.md",
        "routing-index.json",
        "scripts/get-knowledge.py",
    )
    for step in loads:
        if any(_spec_matches(spec, step) for spec in oracle.must_not_load):
            forbidden_hits.append(step.path or step.logical_id or step.kind)
            continue
        if oracle.walk == "fast_path" and step.kind == "knowledge":
            forbidden_hits.append(step.path or step.logical_id or step.kind)

    if forbidden_hits:
        labels.append("wrong_edge")

    if oracle.handoff:
        remaining = list(oracle.handoff)
        for step in loads:
            if remaining and _spec_matches(remaining[0], step):
                remaining.pop(0)
        if remaining and len(remaining) < len(oracle.handoff):
            labels.append("missing_handoff")
        elif remaining and not missing_groups and activated:
            labels.append("missing_handoff")

    extra_namespaces = sorted(
        {
            step.namespace or step.path or step.kind
            for step in loads
            if not any(_spec_matches(spec, step) for spec in allowed_specs)
            and not any(_spec_matches(spec, step) for spec in oracle.must_not_load)
        }
    )
    whole_file_loads = [
        step.path
        for step in loads
        if step.grain == "whole_file" and step.kind == "knowledge"
    ]
    controller_reads = sum(
        1 for step in steps if step.kind == "controller" and step.succeeded
    )
    if (
        activated
        and not missing_groups
        and (
            extra_namespaces
            or (oracle.walk == "jit" and whole_file_loads)
            or controller_reads > 3
        )
    ):
        labels.append("over_read")

    required_loaded = activated and not missing_groups
    if (
        required_loaded
        and answer_disposition == "fail"
        and "wrong_edge" not in labels
    ):
        labels.append("loaded_but_ignore")

    unique_labels = tuple(label for label in PRIMARY_ORDER if label in labels)
    if not unique_labels:
        primary = "walk_ok" if activated else "no_activation"
        if primary == "walk_ok":
            unique_labels = ("walk_ok",)
        else:
            unique_labels = ("no_activation",)
    else:
        primary = unique_labels[0]
        if "resolve_fail" in unique_labels and "skip_jit" in unique_labels:
            primary = "resolve_fail"
            unique_labels = tuple(
                ["resolve_fail"]
                + [label for label in unique_labels if label != "resolve_fail"]
            )

    return {
        "primary": primary,
        "labels": list(unique_labels),
        "activated": activated,
        "missing_groups": [list(group) for group in missing_groups],
        "forbidden_hits": forbidden_hits,
        "failed_required_attempts": failed_required_attempts,
        "extra_namespaces": extra_namespaces,
        "whole_file_loads": whole_file_loads,
        "controller_reads": controller_reads,
        "helper_routes": [
            step.logical_id
            for step in steps
            if step.kind == "helper" and step.logical_id
        ],
    }


def _judgment_map(
    results_dir: Path,
) -> dict[str, str]:
    judgments_path = results_dir / "judgments.json"
    index_path = results_dir / "blind-index.json"
    if not judgments_path.is_file() or not index_path.is_file():
        return {}
    judgments = json.loads(judgments_path.read_text(encoding="utf-8"))
    index = json.loads(index_path.read_text(encoding="utf-8"))
    blind_to_run = {
        item["blind_id"]: item["run_id"]
        for item in index.get("bindings", [])
        if isinstance(item, dict)
    }
    mapping: dict[str, str] = {}
    for item in judgments.get("judgments", []):
        run_id = blind_to_run.get(item.get("blind_id"))
        disposition = item.get("disposition")
        if run_id and isinstance(disposition, str):
            mapping[run_id] = disposition
    return mapping


def _step_dict(step: WalkStep) -> dict[str, Any]:
    return asdict(step)


def build_trace_report(
    runs: Iterable[RunRecord],
    oracle: dict[str, OracleCase],
    namespaces: dict[str, str],
    *,
    judgments: dict[str, str] | None = None,
    results_id: str | None = None,
) -> dict[str, Any]:
    judgment_by_run = judgments or {}
    skill_rows: list[dict[str, Any]] = []
    class_counts: Counter[str] = Counter()
    label_counts: Counter[str] = Counter()
    family_counts: dict[str, Counter[str]] = defaultdict(Counter)

    for run in runs:
        if run.profile_id == "baseline":
            continue
        identity = run.case_identity
        case_oracle = oracle.get(identity)
        steps = reconstruct_steps(run.raw_events, namespaces)
        if case_oracle is None:
            classification = {
                "primary": "no_oracle",
                "labels": ["no_oracle"],
                "activated": _controller_activated(steps),
                "missing_groups": [],
                "forbidden_hits": [],
                "failed_required_attempts": [],
                "extra_namespaces": [],
                "whole_file_loads": [],
                "controller_reads": sum(
                    1 for step in steps if step.kind == "controller" and step.succeeded
                ),
                "helper_routes": [
                    step.logical_id
                    for step in steps
                    if step.kind == "helper" and step.logical_id
                ],
            }
        else:
            classification = classify_skill_walk(
                steps,
                case_oracle,
                answer_disposition=judgment_by_run.get(run.run_id),
            )
        row = {
            "run_id": run.run_id,
            "case_identity": identity,
            "profile_id": run.profile_id,
            "state": run.state.value if isinstance(run.state, RunState) else run.state,
            "answer_disposition": judgment_by_run.get(run.run_id),
            "steps": [_step_dict(step) for step in steps],
            "classification": classification,
        }
        skill_rows.append(row)
        primary = classification["primary"]
        class_counts[primary] += 1
        for label in classification["labels"]:
            label_counts[label] += 1
        family_counts[identity][label] += 1

    return {
        "schema_version": TRACE_SCHEMA_VERSION,
        "purpose": (
            "Reconstruct the skill-graph walk from sealed raw_events. "
            "This is not an answer-quality score and not a benchmark."
        ),
        "results_id": results_id,
        "skill_run_count": len(skill_rows),
        "primary_counts": dict(class_counts),
        "label_counts": dict(label_counts),
        "case_label_counts": {
            identity: dict(counts) for identity, counts in family_counts.items()
        },
        "runs": skill_rows,
    }


def render_markdown(report: dict[str, Any]) -> str:
    lines = [
        "# Pilot walker trace",
        "",
        f"Status: reconstructed from sealed local results `{report.get('results_id') or ''}`".rstrip(),
        "",
        "This report does not claim output quality. It answers which skill nodes",
        "the current-skill arm actually read, and where that walk left the intended graph.",
        "",
        "## Mass",
        "",
        f"- Skill-arm runs reconstructed: {report['skill_run_count']}",
        "",
        "| Primary class | Runs |",
        "| --- | ---: |",
    ]
    for name, count in sorted(
        report["primary_counts"].items(), key=lambda item: (-item[1], item[0])
    ):
        lines.append(f"| `{name}` | {count} |")
    lines.extend(
        [
            "",
            "Labels can stack on one run. Label counts:",
            "",
            "| Label | Runs |",
            "| --- | ---: |",
        ]
    )
    for name, count in sorted(
        report["label_counts"].items(), key=lambda item: (-item[1], item[0])
    ):
        lines.append(f"| `{name}` | {count} |")
    lines.extend(["", "## Per current-skill run", ""])
    for row in report["runs"]:
        classification = row["classification"]
        chain = []
        for step in row["steps"]:
            if not step["succeeded"] and step["kind"] not in {"helper", "knowledge", "controller", "index"}:
                continue
            mark = "ok" if step["succeeded"] else "fail"
            node = step.get("logical_id") or step.get("path") or step.get("kind")
            chain.append(f"{node} ({step['kind']}/{step['grain']}/{mark})")
        chain_text = " → ".join(chain) if chain else "(no skill-file commands)"
        lines.extend(
            [
                f"### {row['case_identity']} / `{row['run_id']}`",
                "",
                f"- State: `{row['state']}`",
                f"- Primary: `{classification['primary']}`",
                f"- Labels: {', '.join(f'`{label}`' for label in classification['labels']) or '`walk_ok`'}",
                f"- Walk: `{chain_text}`",
                "",
            ]
        )
    lines.extend(
        [
            "## Decision",
            "",
            "Do not edit handbook nodes until a reconstructed walk shows the required",
            "node was loaded and behavior was still wrong (`loaded_but_ignore`).",
            "",
        ]
    )
    return "\n".join(lines) + "\n"

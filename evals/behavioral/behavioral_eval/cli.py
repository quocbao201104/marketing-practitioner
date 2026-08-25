from __future__ import annotations

import argparse
import json
import os
import shutil
import sys
import tempfile
from dataclasses import asdict
from pathlib import Path
from typing import Any, Iterable

from .adapters import ExecutorResult
from .adjudication import build_blind_packet, order_blind_packets
from .codex_cli import CodexCliAdapter
from .evidence import redact_text
from .fixture import FixtureAdapter
from .models import ArmProfile, RunRecord, RunState, ValidationError
from .report import build_report
from .runner import run_condition
from .validation import load_cases, load_profiles
from .workspace import WorkspaceError, build_run_workspace, hash_tree


DEFAULT_CASES = Path("evals/behavioral/cases/pilot-v1.json")
DEFAULT_PROFILES = Path("evals/behavioral/profiles")


def _load_profile_paths(path: Path, *, live: bool) -> list[ArmProfile]:
    path = Path(path)
    paths = sorted(path.glob("*.json")) if path.is_dir() else [path]
    if not paths:
        raise ValidationError(f"no profile documents found: {path}")
    profiles: list[ArmProfile] = []
    seen: set[str] = set()
    for document in paths:
        for profile in load_profiles(document, live=live):
            if profile.profile_id in seen:
                raise ValidationError(f"duplicate profile id: {profile.profile_id}")
            seen.add(profile.profile_id)
            profiles.append(profile)
    return profiles


def _json_value(value: Any) -> Any:
    if isinstance(value, RunState):
        return value.value
    if isinstance(value, tuple):
        return [_json_value(item) for item in value]
    if isinstance(value, list):
        return [_json_value(item) for item in value]
    if isinstance(value, dict):
        return {key: _json_value(item) for key, item in value.items()}
    return value


def _record_dict(record: RunRecord, roots: Iterable[Path]) -> dict:
    value = _json_value(asdict(record))

    def redact(item: Any) -> Any:
        if isinstance(item, str):
            return redact_text(item, tuple(roots), ())
        if isinstance(item, list):
            return [redact(child) for child in item]
        if isinstance(item, dict):
            return {key: redact(child) for key, child in item.items()}
        return item

    return redact(value)


def _record_from_dict(data: dict) -> RunRecord:
    fields = dict(data)
    fields["state"] = RunState(fields["state"])
    fields["raw_events"] = tuple(fields.get("raw_events", ()))
    fields["limitations"] = tuple(fields.get("limitations", ()))
    return RunRecord(**fields)


def _write_json_fsynced(path: Path, payload: Any) -> None:
    with path.open("w", encoding="utf-8", newline="\n") as handle:
        json.dump(payload, handle, indent=2, ensure_ascii=False, sort_keys=True)
        handle.write("\n")
        handle.flush()
        os.fsync(handle.fileno())


def _atomic_bundle(target: Path, files: dict[str, Any]) -> None:
    target = target.resolve()
    if target.exists():
        raise ValidationError(f"refusing to overwrite existing result directory: {target}")
    target.parent.mkdir(parents=True, exist_ok=True)
    temporary = Path(
        tempfile.mkdtemp(prefix=f".{target.name}.tmp-", dir=str(target.parent))
    )
    try:
        for relative, payload in files.items():
            destination = temporary / relative
            destination.parent.mkdir(parents=True, exist_ok=True)
            _write_json_fsynced(destination, payload)
        temporary.replace(target)
    except BaseException:
        if temporary.exists():
            shutil.rmtree(temporary)
        raise


def _profile_binding(
    profile: ArmProfile, repo_root: Path, repetitions: int | None = None
) -> dict:
    skill_hash = None
    if profile.skill_mode == "workspace-copy" and profile.skill_source:
        skill_hash = hash_tree(repo_root / profile.skill_source)
    return {
        "profile_id": profile.profile_id,
        "adapter": profile.adapter,
        "model": profile.model,
        "reasoning_effort": profile.reasoning_effort,
        "skill_mode": profile.skill_mode,
        "skill_sha256": skill_hash,
        "repetitions": repetitions or profile.repetitions,
    }


def _validate(args: argparse.Namespace) -> int:
    cases = load_cases(args.cases)
    profiles = _load_profile_paths(args.profiles, live=True)
    print(f"PASS: {len(cases)} cases and {len(profiles)} profiles are valid")
    return 0


def _run(args: argparse.Namespace) -> int:
    results_path = Path(args.results)
    if results_path.exists():
        raise ValidationError(
            f"refusing to overwrite existing result directory: {results_path.resolve()}"
        )
    repo_root = Path(args.repo_root).resolve()
    cases = load_cases(args.cases)
    if args.case_id:
        requested = set(args.case_id)
        available = {case.case_id for case in cases}
        unknown = sorted(requested - available)
        if unknown:
            raise ValidationError(f"unknown selected case_id: {unknown[0]}")
        cases = [case for case in cases if case.case_id in requested]
    profiles = _load_profile_paths(args.profiles, live=args.adapter == "codex-cli")
    if args.profile_id:
        requested_profiles = set(args.profile_id)
        available_profiles = {profile.profile_id for profile in profiles}
        unknown_profiles = sorted(requested_profiles - available_profiles)
        if unknown_profiles:
            raise ValidationError(
                f"unknown selected profile_id: {unknown_profiles[0]}"
            )
        profiles = [
            profile for profile in profiles if profile.profile_id in requested_profiles
        ]
    if args.repeat_limit is not None and args.repeat_limit <= 0:
        raise ValidationError("repeat-limit must be a positive integer")
    fixture_results = {
        (case.identity, profile.profile_id): ExecutorResult(
            exit_code=0,
            raw_events=({"type": "fixture_completed"},),
            final_output=f"Fixture answer for {case.identity}",
            activation_verified=True,
            executable_version="fixture-v1",
        )
        for case in cases
        for profile in profiles
    }
    adapter = (
        FixtureAdapter(fixture_results)
        if args.adapter == "fixture"
        else CodexCliAdapter()
    )
    records: list[RunRecord] = []
    workspace_roots: list[Path] = []
    with tempfile.TemporaryDirectory(prefix="behavioral-eval-workspaces-") as temp:
        workspaces = Path(temp)
        for case in cases:
            for profile in profiles:
                repetitions = min(
                    profile.repetitions,
                    args.repeat_limit or profile.repetitions,
                )
                for repetition in range(1, repetitions + 1):
                    destination = (
                        workspaces
                        / case.case_id
                        / profile.profile_id
                        / f"repeat-{repetition}"
                    )
                    binding = build_run_workspace(
                        case, profile, repo_root, destination
                    )
                    workspace_roots.append(binding.root)
                    records.append(run_condition(case, profile, adapter, binding))

        run_payload = {
            "schema_version": 1,
            "runs": [
                _record_dict(record, (repo_root, *workspace_roots))
                for record in records
            ],
        }
        packet_bindings: list[tuple[dict, str]] = []
        for record in records:
            if record.state is not RunState.COMPLETED:
                continue
            case = next(
                item for item in cases if item.identity == record.case_identity
            )
            packet_bindings.append((build_blind_packet(case, record), record.run_id))
        packets = order_blind_packets([packet for packet, _ in packet_bindings])
        blind_index = {
            "schema_version": 1,
            "bindings": [
                {"blind_id": packet["blind_id"], "run_id": run_id}
                for packet, run_id in packet_bindings
            ],
        }
        manifest = {
            "schema_version": 1,
            "sealed": True,
            "adapter": args.adapter,
            "case_identities": [case.identity for case in cases],
            "profiles": [
                _profile_binding(
                    profile,
                    repo_root,
                    min(
                        profile.repetitions,
                        args.repeat_limit or profile.repetitions,
                    ),
                )
                for profile in profiles
            ],
            "run_count": len(records),
        }
        _atomic_bundle(
            results_path,
            {
                "manifest.json": manifest,
                "run-records.json": run_payload,
                "blind-packets.json": {"schema_version": 1, "packets": packets},
                "blind-index.json": blind_index,
            },
        )
    print(f"PASS: sealed {len(records)} runs at {results_path.resolve()}")
    return 0


def _report(args: argparse.Namespace) -> int:
    cases = load_cases(args.cases)
    results_dir = Path(args.results)
    document = json.loads(
        (results_dir / "run-records.json").read_text(encoding="utf-8")
    )
    runs = [_record_from_dict(item) for item in document["runs"]]
    judgments: list[dict] = []
    if args.judgments:
        judgment_document = json.loads(Path(args.judgments).read_text(encoding="utf-8"))
        raw_judgments = judgment_document["judgments"]
        index_document = json.loads(
            (results_dir / "blind-index.json").read_text(encoding="utf-8")
        )
        blind_to_run = {
            item["blind_id"]: item["run_id"]
            for item in index_document["bindings"]
        }
        judgments = []
        for judgment in raw_judgments:
            blind_id = judgment.get("blind_id")
            if blind_id not in blind_to_run:
                raise ValidationError(f"judgment references unknown blind_id: {blind_id}")
            if set(judgment) != {"blind_id", "disposition"}:
                raise ValidationError(
                    "blind judgment requires only blind_id and disposition"
                )
            judgments.append(
                {
                    "run_id": blind_to_run[blind_id],
                    "disposition": judgment["disposition"],
                }
            )
    report = build_report(cases, runs, judgments)
    output = Path(args.output)
    if output.exists():
        raise ValidationError(f"refusing to overwrite report: {output.resolve()}")
    output.parent.mkdir(parents=True, exist_ok=True)
    _write_json_fsynced(output, report)
    print(f"PASS: wrote paired report to {output.resolve()}")
    return 0


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Behavioral evaluation harness")
    subparsers = parser.add_subparsers(dest="command", required=True)

    validate = subparsers.add_parser("validate", help="validate cases and profiles")
    validate.add_argument("--cases", type=Path, default=DEFAULT_CASES)
    validate.add_argument("--profiles", type=Path, default=DEFAULT_PROFILES)
    validate.set_defaults(handler=_validate)

    run = subparsers.add_parser("run", help="execute and seal a run bundle")
    run.add_argument("--cases", type=Path, default=DEFAULT_CASES)
    run.add_argument("--profiles", type=Path, default=DEFAULT_PROFILES)
    run.add_argument("--adapter", choices=("fixture", "codex-cli"), required=True)
    run.add_argument("--results", type=Path, required=True)
    run.add_argument("--repo-root", type=Path, default=Path.cwd())
    run.add_argument("--case-id", action="append")
    run.add_argument("--profile-id", action="append")
    run.add_argument("--repeat-limit", type=int)
    run.set_defaults(handler=_run)

    report = subparsers.add_parser("report", help="create a paired report")
    report.add_argument("--cases", type=Path, default=DEFAULT_CASES)
    report.add_argument("--results", type=Path, required=True)
    report.add_argument("--judgments", type=Path)
    report.add_argument("--output", type=Path, required=True)
    report.set_defaults(handler=_report)
    return parser


def main(argv: list[str] | None = None) -> int:
    try:
        args = _parser().parse_args(argv)
        return args.handler(args)
    except (ValidationError, WorkspaceError, OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())

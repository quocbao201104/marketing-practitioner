from __future__ import annotations

import json
import uuid
from collections.abc import Callable
from datetime import datetime, timezone

from .adapters import ExecutorAdapter, ExecutorRequest
from .evidence import seal_bytes
from .models import ArmProfile, CaseContract, RunRecord, RunState
from .workspace import WorkspaceBinding, preflight_workspace


def _utc_now() -> datetime:
    return datetime.now(timezone.utc)


def _run_id() -> str:
    return f"RUN-{uuid.uuid4().hex.upper()}"


def _timestamp(value: datetime) -> str:
    if value.tzinfo is None:
        raise ValueError("run clock must return timezone-aware datetimes")
    return value.astimezone(timezone.utc).isoformat().replace("+00:00", "Z")


def _events_bytes(events: tuple[dict, ...]) -> bytes:
    return json.dumps(
        list(events), sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode("utf-8")


def run_condition(
    case: CaseContract,
    profile: ArmProfile,
    adapter: ExecutorAdapter,
    binding: WorkspaceBinding,
    *,
    clock: Callable[[], datetime] = _utc_now,
    run_id_factory: Callable[[], str] = _run_id,
) -> RunRecord:
    run_id = run_id_factory()
    started = clock()
    binding_errors: list[str] = []
    if binding.profile_id != profile.profile_id:
        binding_errors.append("workspace profile differs from requested profile")
    if binding.skill_mode != profile.skill_mode:
        binding_errors.append("workspace skill mode differs from requested profile")
    binding_errors.extend(preflight_workspace(binding))
    if binding_errors:
        return RunRecord(
            run_id=run_id,
            case_identity=case.identity,
            profile_id=profile.profile_id,
            state=RunState.ISOLATION_FAILED,
            started_at=_timestamp(started),
            finished_at=_timestamp(clock()),
            limitations=tuple(binding_errors),
        )

    result = adapter.execute(
        ExecutorRequest(
            run_id=run_id,
            case=case,
            profile=profile,
            workspace=binding,
        )
    )
    limitations: list[str] = []
    if result.timed_out:
        state = RunState.TIMED_OUT
        limitations.append("executor exceeded the configured timeout")
    elif result.interrupted:
        state = RunState.EXECUTOR_FAILED
        limitations.append("executor was interrupted")
    elif result.exit_code is None or result.exit_code != 0:
        state = RunState.EXECUTOR_FAILED
    elif result.final_output is None or not result.final_output.strip():
        state = RunState.INVALID_OUTPUT
    elif profile.skill_mode == "workspace-copy" and result.activation_verified is not True:
        state = RunState.ACTIVATION_UNVERIFIED
        limitations.append("skill activation was not verified")
    else:
        state = RunState.COMPLETED

    output_bytes = (
        result.final_output.encode("utf-8") if result.final_output is not None else None
    )
    event_bytes = result.raw_event_bytes or _events_bytes(result.raw_events)
    return RunRecord(
        run_id=run_id,
        case_identity=case.identity,
        profile_id=profile.profile_id,
        state=state,
        started_at=_timestamp(started),
        finished_at=_timestamp(clock()),
        event_sha256=seal_bytes(event_bytes),
        output_sha256=seal_bytes(output_bytes) if output_bytes is not None else None,
        event_count=len(result.raw_events),
        raw_events=result.raw_events,
        final_output=result.final_output,
        stderr=result.stderr,
        exit_code=result.exit_code,
        executor_version=result.executable_version,
        limitations=tuple(limitations),
    )

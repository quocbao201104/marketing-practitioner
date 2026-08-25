from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Protocol

from .models import ArmProfile, CaseContract
from .workspace import WorkspaceBinding


@dataclass(frozen=True)
class ExecutorRequest:
    run_id: str
    case: CaseContract
    profile: ArmProfile
    workspace: WorkspaceBinding


@dataclass(frozen=True)
class ExecutorResult:
    exit_code: int | None = None
    timed_out: bool = False
    interrupted: bool = False
    raw_events: tuple[dict[str, Any], ...] = field(default_factory=tuple)
    raw_event_bytes: bytes = b""
    final_output: str | None = None
    stderr: str = ""
    activation_verified: bool | None = None
    executable_version: str | None = None


class ExecutorAdapter(Protocol):
    def execute(self, request: ExecutorRequest) -> ExecutorResult: ...

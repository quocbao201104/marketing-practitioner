from __future__ import annotations

import json
import os
import re
import shutil
import signal
import subprocess
import time
from pathlib import Path
from typing import Any, Sequence

from .adapters import ExecutorRequest, ExecutorResult


def resolve_codex_executable() -> tuple[str, ...]:
    resolved = shutil.which("codex")
    if resolved is None:
        return ("codex",)
    return (resolved,)


def build_codex_command(
    request: ExecutorRequest,
    *,
    executable: Sequence[str] = ("codex",),
    final_output_path: Path | None = None,
) -> list[str]:
    output_path = final_output_path or (
        request.workspace.root
        / ".behavioral-eval"
        / request.run_id
        / "final-message.txt"
    )
    return [
        *executable,
        "exec",
        "--json",
        "--ephemeral",
        "--ignore-user-config",
        "--sandbox",
        "read-only",
        "--cd",
        str(request.workspace.root),
        "--model",
        request.profile.model,
        "--config",
        f'model_reasoning_effort="{request.profile.reasoning_effort}"',
        "--output-last-message",
        str(output_path),
        "-",
    ]


def _decode(data: bytes) -> str:
    return data.decode("utf-8", errors="replace")


def _parse_events(data: bytes) -> tuple[dict[str, Any], ...]:
    events: list[dict[str, Any]] = []
    for raw_line in _decode(data).splitlines():
        if not raw_line.strip():
            continue
        try:
            value = json.loads(raw_line)
        except json.JSONDecodeError:
            events.append({"type": "unparsed_jsonl", "raw": raw_line})
        else:
            if isinstance(value, dict):
                events.append(value)
            else:
                events.append({"type": "json_value", "value": value})
    return tuple(events)


def _walk_strings(value: Any):
    if isinstance(value, str):
        yield value
    elif isinstance(value, dict):
        for key, item in value.items():
            yield str(key)
            yield from _walk_strings(item)
    elif isinstance(value, list):
        for item in value:
            yield from _walk_strings(item)


def activation_verified(
    events: tuple[dict[str, Any], ...], request: ExecutorRequest
) -> bool | None:
    for event in events:
        event_type = str(event.get("type", "")).lower()
        values = " ".join(_walk_strings(event)).lower()
        if "skill" in event_type and "activat" in event_type and "marketing-practitioner" in values:
            return True
        item = event.get("item")
        if not isinstance(item, dict):
            continue
        if event_type != "item.completed" or item.get("type") != "command_execution":
            continue
        if item.get("exit_code") != 0 or request.workspace.skill_path is None:
            continue
        command = re.sub(
            r"/+",
            "/",
            str(item.get("command", "")).lower().replace("\\", "/"),
        )
        expected = re.sub(
            r"/+",
            "/",
            str(
                (request.workspace.skill_path / "SKILL.md").resolve()
            ).lower().replace("\\", "/"),
        )
        if expected in command:
            return True
    return None


def _creation_flags() -> int:
    if os.name != "nt":
        return 0
    return subprocess.CREATE_NEW_PROCESS_GROUP | subprocess.CREATE_NO_WINDOW


def _terminate_process_tree(process: subprocess.Popen[bytes]) -> None:
    if process.poll() is not None:
        return
    if os.name == "nt":
        subprocess.run(
            ["taskkill", "/PID", str(process.pid), "/T", "/F"],
            capture_output=True,
            check=False,
            creationflags=subprocess.CREATE_NO_WINDOW,
        )
    else:
        try:
            os.killpg(process.pid, signal.SIGKILL)
        except ProcessLookupError:
            return


class CodexCliAdapter:
    def __init__(self, executable: Sequence[str] | None = None) -> None:
        selected = resolve_codex_executable() if executable is None else executable
        if not selected:
            raise ValueError("executable prefix cannot be empty")
        self._executable = tuple(selected)

    def _version(self) -> str | None:
        try:
            completed = subprocess.run(
                [*self._executable, "--version"],
                capture_output=True,
                check=False,
                timeout=10,
                creationflags=_creation_flags(),
            )
        except (OSError, subprocess.TimeoutExpired):
            return None
        if completed.returncode:
            return None
        return _decode(completed.stdout).strip() or None

    def execute(self, request: ExecutorRequest) -> ExecutorResult:
        final_path = (
            request.workspace.root
            / ".behavioral-eval"
            / request.run_id
            / "final-message.txt"
        )
        final_path.parent.mkdir(parents=True, exist_ok=True)
        command = build_codex_command(
            request, executable=self._executable, final_output_path=final_path
        )
        started = time.perf_counter()
        try:
            process = subprocess.Popen(
                command,
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                cwd=request.workspace.root,
                start_new_session=os.name != "nt",
                creationflags=_creation_flags(),
            )
        except OSError as exc:
            return ExecutorResult(
                exit_code=127,
                stderr=str(exc),
                executable_version=self._version(),
            )

        timed_out = False
        try:
            stdout, stderr = process.communicate(
                input=request.case.prompt.encode("utf-8"),
                timeout=request.profile.timeout_seconds,
            )
        except subprocess.TimeoutExpired:
            timed_out = True
            _terminate_process_tree(process)
            stdout, stderr = process.communicate()

        events = _parse_events(stdout)
        final_output: str | None = None
        if not timed_out and final_path.is_file():
            final_output = _decode(final_path.read_bytes())
        elapsed = time.perf_counter() - started
        elapsed_event = {
            "type": "adapter_observation",
            "elapsed_seconds": round(elapsed, 6),
        }
        return ExecutorResult(
            exit_code=process.returncode,
            timed_out=timed_out,
            raw_events=(*events, elapsed_event),
            raw_event_bytes=stdout,
            final_output=final_output,
            stderr=_decode(stderr),
            activation_verified=activation_verified(events, request),
            executable_version=self._version(),
        )

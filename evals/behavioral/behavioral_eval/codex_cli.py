from __future__ import annotations

import json
import os
import re
import shutil
import signal
import subprocess
import time
from pathlib import Path
from typing import Any, NamedTuple, Sequence

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


def _normalize_path_text(value: str) -> str:
    return re.sub(r"/+", "/", value.lower().replace("\\", "/"))


class _PowerShellToken(NamedTuple):
    kind: str
    value: str
    interpolated: bool = False


def _extract_powershell_script(command: str) -> str:
    normalized = _normalize_path_text(command).replace("'\"'", "'")
    command_match = re.search(r"(?:^|\s)-command\b", normalized)
    if command_match is not None and re.search(
        r"\b(?:pwsh|powershell)(?:\.exe)?\b", normalized[: command_match.start()]
    ):
        normalized = normalized[command_match.end() :].strip()
        if (
            len(normalized) >= 2
            and normalized[0] in {"'", '"'}
            and normalized[-1] == normalized[0]
        ):
            normalized = normalized[1:-1]
        normalized = re.sub(
            r"[\"']+(\$[a-z_][a-z0-9_]*)", r"\1", normalized
        )
    return normalized.strip()


def _tokenize_powershell(script: str) -> tuple[_PowerShellToken, ...]:
    tokens: list[_PowerShellToken] = []
    index = 0
    punctuation = {
        ";": "statement",
        "\r": "statement",
        "\n": "statement",
        "|": "pipe",
        "(": "left_paren",
        ")": "right_paren",
        "=": "equals",
        ",": "comma",
    }

    while index < len(script):
        character = script[index]
        if character in {" ", "\t"}:
            index += 1
            continue
        if character == "#":
            while index < len(script) and script[index] not in {"\r", "\n"}:
                index += 1
            continue
        if character in punctuation:
            tokens.append(_PowerShellToken(punctuation[character], character))
            index += 1
            if character == "\r" and index < len(script) and script[index] == "\n":
                index += 1
            continue
        if character in {"'", '"'}:
            quote = character
            index += 1
            value: list[str] = []
            interpolated = False
            while index < len(script):
                character = script[index]
                if character == quote:
                    if quote == "'" and index + 1 < len(script) and script[index + 1] == "'":
                        value.append("'")
                        index += 2
                        continue
                    index += 1
                    break
                if quote == '"' and character in {"$", "`"}:
                    interpolated = True
                value.append(character)
                index += 1
            tokens.append(
                _PowerShellToken("string", "".join(value), interpolated=interpolated)
            )
            continue

        start = index
        while (
            index < len(script)
            and script[index] not in {" ", "\t", "#", "'", '"'}
            and script[index] not in punctuation
        ):
            index += 1
        if start == index:
            index += 1
            continue
        tokens.append(_PowerShellToken("word", script[start:index]))

    return tuple(tokens)


def _powershell_statements(
    tokens: tuple[_PowerShellToken, ...],
) -> tuple[tuple[_PowerShellToken, ...], ...]:
    statements: list[tuple[_PowerShellToken, ...]] = []
    current: list[_PowerShellToken] = []
    for token in tokens:
        if token.kind == "statement":
            if current:
                statements.append(tuple(current))
                current = []
            continue
        current.append(token)
    if current:
        statements.append(tuple(current))
    return tuple(statements)


def _safe_path_literal(
    token: _PowerShellToken, expected_paths: set[str]
) -> bool:
    return (
        token.kind == "string"
        and not token.interpolated
        and token.value in expected_paths
    )


def _safe_reader_operand(
    token: _PowerShellToken,
    expected_paths: set[str],
    bound_variables: set[str],
) -> bool:
    if _safe_path_literal(token, expected_paths):
        return True
    return token.kind == "word" and token.value in bound_variables


def _first_command_index(statement: tuple[_PowerShellToken, ...]) -> int | None:
    index = 0
    while index < len(statement) and statement[index].kind == "left_paren":
        index += 1
    if (
        index + 2 < len(statement)
        and statement[index].kind == "word"
        and statement[index].value.startswith("$")
        and statement[index + 1].kind == "equals"
    ):
        index += 2
        while index < len(statement) and statement[index].kind == "left_paren":
            index += 1
    if index >= len(statement) or statement[index].kind != "word":
        return None
    return index


def _command_reads_expected_path(command: str, expected_paths: set[str]) -> bool:
    script = _extract_powershell_script(command)
    statements = _powershell_statements(_tokenize_powershell(script))
    bound_variables: set[str] = set()

    for statement in statements:
        for index in range(len(statement) - 1):
            variable = statement[index]
            if (
                variable.kind == "word"
                and variable.value.startswith("$")
                and statement[index + 1].kind == "equals"
            ):
                bound_variables.discard(variable.value)
                assignment = statement[index + 2 :]
                if len(assignment) == 1 and _safe_path_literal(
                    assignment[0], expected_paths
                ):
                    bound_variables.add(variable.value)

        command_index = _first_command_index(statement)
        if command_index is None:
            continue
        command_token = statement[command_index].value
        if command_token == "get-content":
            for index in range(command_index + 1, len(statement) - 1):
                if (
                    statement[index].kind == "word"
                    and statement[index].value == "-literalpath"
                    and _safe_reader_operand(
                        statement[index + 1], expected_paths, bound_variables
                    )
                ):
                    return True
            continue
        if command_token not in {
            "[system.io.file]::readalllines",
            "[system.io.file]::readalltext",
            "[system.io.file]::readallbytes",
            "[system.io.file]::readlines",
        }:
            continue
        operand_index = command_index + 2
        if (
            command_index + 1 < len(statement)
            and statement[command_index + 1].kind == "left_paren"
            and operand_index < len(statement)
            and _safe_reader_operand(
                statement[operand_index], expected_paths, bound_variables
            )
        ):
            return True
    return False


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
        skill_file = request.workspace.skill_path / "SKILL.md"
        expected_paths = {
            _normalize_path_text(str(skill_file)),
            _normalize_path_text(str(skill_file.resolve())),
        }
        if _command_reads_expected_path(
            str(item.get("command", "")), expected_paths
        ):
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

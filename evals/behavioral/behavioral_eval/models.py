from __future__ import annotations

import re
from dataclasses import dataclass, field
from enum import Enum
from typing import Any


IDENTIFIER_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]*$")
SEMVER_RE = re.compile(r"^\d+\.\d+\.\d+$")
SHA256_RE = re.compile(r"^[0-9a-f]{64}$")


class ValidationError(ValueError):
    """Raised when a behavioral evaluation contract is invalid."""


class RunState(str, Enum):
    COMPLETED = "completed"
    EXECUTOR_FAILED = "executor_failed"
    TIMED_OUT = "timed_out"
    INVALID_OUTPUT = "invalid_output"
    ACTIVATION_UNVERIFIED = "activation_unverified"
    ISOLATION_FAILED = "isolation_failed"


def _exact_keys(data: dict[str, Any], expected: set[str], label: str) -> None:
    unknown = sorted(set(data) - expected)
    missing = sorted(expected - set(data))
    if unknown:
        raise ValidationError(f"unknown {label} fields: {', '.join(unknown)}")
    if missing:
        raise ValidationError(f"missing {label} fields: {', '.join(missing)}")


def _required_text(value: Any, label: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ValidationError(f"{label} must be non-empty text")
    return value


def _text_tuple(value: Any, label: str) -> tuple[str, ...]:
    if not isinstance(value, list):
        raise ValidationError(f"{label} must be an array")
    result = tuple(_required_text(item, f"{label} item") for item in value)
    return result


@dataclass(frozen=True)
class PredicateSpec:
    kind: str
    value: str | int | None = None

    @classmethod
    def from_dict(cls, data: Any) -> "PredicateSpec":
        if not isinstance(data, dict):
            raise ValidationError("hard predicate must be an object")
        allowed = {"type", "value"}
        unknown = sorted(set(data) - allowed)
        if unknown:
            raise ValidationError(f"unknown predicate fields: {', '.join(unknown)}")
        kind = _required_text(data.get("type"), "predicate type")
        value = data.get("value")
        if value is not None and not isinstance(value, (str, int)):
            raise ValidationError("predicate value must be text, integer, or null")
        return cls(kind=kind, value=value)


@dataclass(frozen=True)
class Provenance:
    source: str
    frozen_at_commit: str

    @classmethod
    def from_dict(cls, data: Any) -> "Provenance":
        if not isinstance(data, dict):
            raise ValidationError("provenance must be an object")
        _exact_keys(data, {"source", "frozen_at_commit"}, "provenance")
        source = _required_text(data["source"], "provenance source")
        commit = _required_text(data["frozen_at_commit"], "frozen commit")
        if not re.fullmatch(r"[0-9a-f]{40}", commit):
            raise ValidationError("frozen_at_commit must be a 40-character Git hash")
        return cls(source=source, frozen_at_commit=commit)


@dataclass(frozen=True)
class CaseContract:
    case_id: str
    version: str
    family: str
    prompt: str
    input_files: tuple[str, ...]
    hard_predicates: tuple[PredicateSpec, ...]
    review_criteria: tuple[str, ...]
    forbidden_disclosures: tuple[str, ...]
    expected_relation: str
    provenance: Provenance

    @property
    def identity(self) -> str:
        return f"{self.case_id}@{self.version}"

    @classmethod
    def from_dict(cls, data: Any) -> "CaseContract":
        if not isinstance(data, dict):
            raise ValidationError("case must be an object")
        expected = {
            "case_id",
            "version",
            "family",
            "prompt",
            "input_files",
            "hard_predicates",
            "review_criteria",
            "forbidden_disclosures",
            "expected_relation",
            "provenance",
        }
        _exact_keys(data, expected, "case")
        case_id = _required_text(data["case_id"], "case_id")
        if not IDENTIFIER_RE.fullmatch(case_id):
            raise ValidationError("case_id contains unsupported characters")
        version = _required_text(data["version"], "case version")
        if not SEMVER_RE.fullmatch(version):
            raise ValidationError("case version must use x.y.z format")
        predicates = data["hard_predicates"]
        if not isinstance(predicates, list):
            raise ValidationError("hard_predicates must be an array")
        relation = _required_text(data["expected_relation"], "expected_relation")
        if relation not in {"skill_not_worse", "sensitivity", "invariance"}:
            raise ValidationError(f"unsupported expected_relation: {relation}")
        return cls(
            case_id=case_id,
            version=version,
            family=_required_text(data["family"], "family"),
            prompt=_required_text(data["prompt"], "prompt"),
            input_files=_text_tuple(data["input_files"], "input_files"),
            hard_predicates=tuple(PredicateSpec.from_dict(item) for item in predicates),
            review_criteria=_text_tuple(data["review_criteria"], "review_criteria"),
            forbidden_disclosures=_text_tuple(
                data["forbidden_disclosures"], "forbidden_disclosures"
            ),
            expected_relation=relation,
            provenance=Provenance.from_dict(data["provenance"]),
        )


@dataclass(frozen=True)
class ArmProfile:
    profile_id: str
    adapter: str
    model: str
    reasoning_effort: str
    skill_mode: str
    skill_source: str | None
    expected_skill_sha256: str | None
    timeout_seconds: int
    repetitions: int

    @classmethod
    def from_dict(cls, data: Any, *, live: bool = False) -> "ArmProfile":
        if not isinstance(data, dict):
            raise ValidationError("profile must be an object")
        expected = {
            "profile_id",
            "adapter",
            "model",
            "reasoning_effort",
            "skill_mode",
            "skill_source",
            "expected_skill_sha256",
            "timeout_seconds",
            "repetitions",
        }
        _exact_keys(data, expected, "profile")
        profile_id = _required_text(data["profile_id"], "profile_id")
        if not IDENTIFIER_RE.fullmatch(profile_id):
            raise ValidationError("profile_id contains unsupported characters")
        adapter = _required_text(data["adapter"], "adapter")
        if adapter not in {"fixture", "codex-cli"}:
            raise ValidationError(f"unsupported adapter: {adapter}")
        model = _required_text(data["model"], "model")
        effort = _required_text(data["reasoning_effort"], "reasoning_effort")
        if live and (model == "required-at-run" or effort == "required-at-run"):
            raise ValidationError("live profile requires explicit model and reasoning effort")
        skill_mode = _required_text(data["skill_mode"], "skill_mode")
        if skill_mode not in {"none", "workspace-copy"}:
            raise ValidationError(f"unsupported skill_mode: {skill_mode}")
        skill_source = data["skill_source"]
        expected_hash = data["expected_skill_sha256"]
        if skill_mode == "none":
            if skill_source is not None or expected_hash is not None:
                raise ValidationError("skill_mode none cannot bind a skill source or hash")
        else:
            _required_text(skill_source, "skill_source")
            _required_text(expected_hash, "expected_skill_sha256")
            if expected_hash not in {"computed-at-run-bind"} and not SHA256_RE.fullmatch(
                expected_hash
            ):
                raise ValidationError("expected_skill_sha256 must be a SHA-256 or bind marker")
        timeout = data["timeout_seconds"]
        repetitions = data["repetitions"]
        if not isinstance(timeout, int) or isinstance(timeout, bool) or timeout <= 0:
            raise ValidationError("timeout_seconds must be a positive integer")
        if (
            not isinstance(repetitions, int)
            or isinstance(repetitions, bool)
            or repetitions <= 0
        ):
            raise ValidationError("repetitions must be a positive integer")
        return cls(
            profile_id=profile_id,
            adapter=adapter,
            model=model,
            reasoning_effort=effort,
            skill_mode=skill_mode,
            skill_source=skill_source,
            expected_skill_sha256=expected_hash,
            timeout_seconds=timeout,
            repetitions=repetitions,
        )


@dataclass(frozen=True)
class RunRecord:
    run_id: str
    case_identity: str
    profile_id: str
    state: RunState
    started_at: str
    finished_at: str
    event_sha256: str | None = None
    output_sha256: str | None = None
    answer_disposition: str | None = None
    limitations: tuple[str, ...] = field(default_factory=tuple)

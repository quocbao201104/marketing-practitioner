from __future__ import annotations

import hashlib
import json
from dataclasses import asdict, dataclass

from .models import CaseContract, PredicateSpec, RunRecord, ValidationError


@dataclass(frozen=True)
class PredicateResult:
    kind: str
    passed: bool
    detail: str


def _require_value(predicate: PredicateSpec, expected: type, label: str):
    value = predicate.value
    if isinstance(value, bool) or not isinstance(value, expected):
        raise ValidationError(f"{label} requires a {expected.__name__} value")
    return value


def evaluate_hard_predicates(
    case: CaseContract, output: str | None
) -> list[PredicateResult]:
    text = output or ""
    results: list[PredicateResult] = []
    for predicate in case.hard_predicates:
        kind = predicate.kind
        if kind == "output_present":
            if predicate.value is not None:
                raise ValidationError("output_present does not accept a value")
            passed = bool(text.strip())
            detail = "output is present" if passed else "output is empty"
        elif kind == "max_characters":
            limit = _require_value(predicate, int, kind)
            if limit < 0:
                raise ValidationError("max_characters requires a non-negative int value")
            passed = len(text) <= limit
            detail = f"output has {len(text)} characters; maximum is {limit}"
        elif kind == "must_contain_literal":
            literal = _require_value(predicate, str, kind)
            passed = literal in text
            detail = (
                "required literal is present"
                if passed
                else "required literal is absent"
            )
        elif kind == "must_not_contain_literal":
            literal = _require_value(predicate, str, kind)
            passed = literal not in text
            detail = (
                "forbidden literal is absent"
                if passed
                else "forbidden literal is present"
            )
        elif kind == "valid_json":
            if predicate.value is not None:
                raise ValidationError("valid_json does not accept a value")
            try:
                json.loads(text)
                passed = True
                detail = "output is valid JSON"
            except (json.JSONDecodeError, TypeError):
                passed = False
                detail = "output is not valid JSON"
        else:
            raise ValidationError(f"unsupported hard predicate: {kind}")
        results.append(PredicateResult(kind=kind, passed=passed, detail=detail))
    return results


def build_blind_packet(case: CaseContract, run: RunRecord) -> dict:
    if run.case_identity != case.identity:
        raise ValidationError("run does not belong to the supplied case")
    predicate_results = evaluate_hard_predicates(case, run.final_output)
    blind_id = hashlib.sha256(
        f"{case.identity}\0{run.run_id}".encode("utf-8")
    ).hexdigest()[:20]
    return {
        "schema_version": 1,
        "blind_id": blind_id,
        "case_identity": case.identity,
        "task": case.prompt,
        "candidate_answer": run.final_output,
        "hard_predicates": [asdict(item) for item in predicate_results],
        "review_criteria": list(case.review_criteria),
    }

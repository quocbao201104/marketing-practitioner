from __future__ import annotations

from collections import Counter, defaultdict
from dataclasses import dataclass, replace
from typing import Iterable

from .adjudication import evaluate_hard_predicates
from .models import CaseContract, RunRecord, RunState, ValidationError


PAIR_DISPOSITIONS = (
    "both_pass",
    "skill_only_pass",
    "baseline_only_pass",
    "both_fail",
    "unresolved",
    "operationally_invalid",
)
ANSWER_DISPOSITIONS = {"pass", "fail", "unresolved"}


@dataclass(frozen=True)
class PairRecord:
    case_identity: str
    baseline_run_ids: tuple[str, ...]
    skill_run_ids: tuple[str, ...]
    disposition: str
    repeat_instability: bool


def _arm_outcome(runs: tuple[RunRecord, ...]) -> tuple[str, bool]:
    if not runs or any(run.state is not RunState.COMPLETED for run in runs):
        return "operationally_invalid", False
    dispositions = tuple(run.answer_disposition or "unresolved" for run in runs)
    unknown = sorted(set(dispositions) - ANSWER_DISPOSITIONS)
    if unknown:
        raise ValidationError(f"unsupported answer disposition: {', '.join(unknown)}")
    instability = len(set(dispositions)) > 1
    if instability or "unresolved" in dispositions:
        return "unresolved", instability
    return dispositions[0], False


def pair_runs(
    case: CaseContract,
    baseline_runs: Iterable[RunRecord],
    skill_runs: Iterable[RunRecord],
) -> PairRecord:
    baseline = tuple(baseline_runs)
    skill = tuple(skill_runs)
    all_runs = baseline + skill
    if any(run.case_identity != case.identity for run in all_runs):
        raise ValidationError("paired run does not belong to the supplied case")

    baseline_outcome, baseline_unstable = _arm_outcome(baseline)
    skill_outcome, skill_unstable = _arm_outcome(skill)
    unstable = baseline_unstable or skill_unstable
    outcomes = (baseline_outcome, skill_outcome)
    if "operationally_invalid" in outcomes:
        disposition = "operationally_invalid"
    elif "unresolved" in outcomes:
        disposition = "unresolved"
    elif outcomes == ("pass", "pass"):
        disposition = "both_pass"
    elif outcomes == ("fail", "pass"):
        disposition = "skill_only_pass"
    elif outcomes == ("pass", "fail"):
        disposition = "baseline_only_pass"
    else:
        disposition = "both_fail"
    return PairRecord(
        case_identity=case.identity,
        baseline_run_ids=tuple(run.run_id for run in baseline),
        skill_run_ids=tuple(run.run_id for run in skill),
        disposition=disposition,
        repeat_instability=unstable,
    )


def _judgment_map(judgments: Iterable[dict]) -> dict[str, str]:
    result: dict[str, str] = {}
    for judgment in judgments:
        if not isinstance(judgment, dict):
            raise ValidationError("judgment must be an object")
        if set(judgment) != {"run_id", "disposition"}:
            raise ValidationError("judgment requires only run_id and disposition")
        run_id = judgment["run_id"]
        disposition = judgment["disposition"]
        if not isinstance(run_id, str) or not run_id:
            raise ValidationError("judgment run_id must be non-empty text")
        if disposition not in ANSWER_DISPOSITIONS:
            raise ValidationError(f"unsupported judgment disposition: {disposition}")
        if run_id in result:
            raise ValidationError(f"duplicate judgment for run: {run_id}")
        result[run_id] = disposition
    return result


def _adjudicate_run(
    case: CaseContract, run: RunRecord, judgment: str | None
) -> RunRecord:
    if run.state is not RunState.COMPLETED:
        return replace(run, answer_disposition=None)
    predicates = evaluate_hard_predicates(case, run.final_output)
    if any(not predicate.passed for predicate in predicates):
        disposition = "fail"
    else:
        disposition = judgment or run.answer_disposition
        if disposition is None:
            disposition = "pass" if not case.review_criteria else "unresolved"
    if disposition not in ANSWER_DISPOSITIONS:
        raise ValidationError(f"unsupported answer disposition: {disposition}")
    return replace(run, answer_disposition=disposition)


def build_report(
    cases: Iterable[CaseContract],
    runs: Iterable[RunRecord],
    judgments: Iterable[dict],
) -> dict:
    case_list = tuple(cases)
    run_list = tuple(runs)
    cases_by_identity = {case.identity: case for case in case_list}
    if len(cases_by_identity) != len(case_list):
        raise ValidationError("report cases contain duplicate identities")
    judgments_by_run = _judgment_map(judgments)
    known_run_ids = {run.run_id for run in run_list}
    unknown_judgments = sorted(set(judgments_by_run) - known_run_ids)
    if unknown_judgments:
        raise ValidationError(
            f"judgment references unknown run: {unknown_judgments[0]}"
        )

    adjudicated: list[RunRecord] = []
    for run in run_list:
        case = cases_by_identity.get(run.case_identity)
        if case is None:
            raise ValidationError(f"run references unknown case: {run.case_identity}")
        adjudicated.append(
            _adjudicate_run(case, run, judgments_by_run.get(run.run_id))
        )

    denominators = {
        "runs": len(adjudicated),
        "answer_bearing": sum(run.state is RunState.COMPLETED for run in adjudicated),
        "answer_failures": sum(
            run.state is RunState.COMPLETED and run.answer_disposition == "fail"
            for run in adjudicated
        ),
        "unresolved": sum(
            run.state is RunState.COMPLETED
            and run.answer_disposition == "unresolved"
            for run in adjudicated
        ),
        "operationally_invalid": sum(
            run.state is not RunState.COMPLETED for run in adjudicated
        ),
    }

    by_case_profile: dict[tuple[str, str], list[RunRecord]] = defaultdict(list)
    for run in adjudicated:
        by_case_profile[(run.case_identity, run.profile_id)].append(run)

    pairs: list[PairRecord] = []
    for case in case_list:
        baseline = by_case_profile.get((case.identity, "baseline"), [])
        comparison_profiles = sorted(
            profile_id
            for case_identity, profile_id in by_case_profile
            if case_identity == case.identity and profile_id != "baseline"
        )
        if not comparison_profiles and baseline:
            pairs.append(pair_runs(case, baseline, ()))
        for profile_id in comparison_profiles:
            pairs.append(
                pair_runs(
                    case,
                    baseline,
                    by_case_profile[(case.identity, profile_id)],
                )
            )

    disposition_counts = Counter(pair.disposition for pair in pairs)
    family_rows: dict[str, dict[str, int]] = {}
    for case in case_list:
        family_runs = [run for run in adjudicated if run.case_identity == case.identity]
        family_pairs = [pair for pair in pairs if pair.case_identity == case.identity]
        row = family_rows.setdefault(
            case.family,
            {
                "cases": 0,
                "runs": 0,
                "pairs": 0,
                "operationally_invalid": 0,
                "unresolved": 0,
                "repeat_instability": 0,
            },
        )
        row["cases"] += 1
        row["runs"] += len(family_runs)
        row["pairs"] += len(family_pairs)
        row["operationally_invalid"] += sum(
            run.state is not RunState.COMPLETED for run in family_runs
        )
        row["unresolved"] += sum(
            run.state is RunState.COMPLETED
            and run.answer_disposition == "unresolved"
            for run in family_runs
        )
        row["repeat_instability"] += sum(
            pair.repeat_instability for pair in family_pairs
        )

    return {
        "schema_version": 1,
        "denominators": denominators,
        "paired_dispositions": {
            name: disposition_counts.get(name, 0) for name in PAIR_DISPOSITIONS
        },
        "repeat_instability": sum(pair.repeat_instability for pair in pairs),
        "families": family_rows,
        "pairs": [
            {
                "case_identity": pair.case_identity,
                "baseline_run_ids": list(pair.baseline_run_ids),
                "skill_run_ids": list(pair.skill_run_ids),
                "disposition": pair.disposition,
                "repeat_instability": pair.repeat_instability,
            }
            for pair in pairs
        ],
    }

from __future__ import annotations

from dataclasses import dataclass, replace
from pathlib import Path
import tempfile

from episode import TARGET_PATHS, WORLD_CONTROL, WORLD_PRESSURE, EpisodeState, initialize_workspace
from evaluator import PredicateStatus, SemanticAssessment, SemanticObservations, WorkVerdict, evaluate, required_relation_refs
from oracle import CURRENT_DEPENDENT_IDS, CURRENT_PROTECTED_IDS, SOURCE_HISTORY_IDS

EXPECTED_FIXTURE_IDS = tuple(f"XCI-FX-{i:02d}" for i in range(1, 14))


@dataclass(frozen=True)
class FixtureResult:
    fixture_id: str
    expected_verdict: str
    actual_verdict: str
    expected_statuses: dict[str, str]
    actual_statuses: dict[str, str]
    passed: bool


def _write_complete_release_log(root: Path) -> None:
    lines = ["# Release log", "", *[f"- {path} — reviewed" for path in TARGET_PATHS]]
    (root / "release-log.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def _terminal_state(world: str) -> EpisodeState:
    with tempfile.TemporaryDirectory() as temp_dir:
        root = Path(temp_dir)
        state = initialize_workspace(root, world)
        _write_complete_release_log(root)
        state.seal_qa_candidate(review_complete=True, t0_valid=True)
        state.deliver_r2()
        _write_complete_release_log(root)
        state.terminal_gate()
        return state


def _assessment(state: EpisodeState, relation_id: str, outcome: str = "satisfied", judge_id: str = "JUDGE-FIXTURE-A") -> SemanticAssessment:
    refs = required_relation_refs(state, relation_id) or ()
    return SemanticAssessment("applicable", outcome, tuple(refs), judge_id)


def _good_observations(state: EpisodeState) -> SemanticObservations:
    relations = {rid: _assessment(state, rid) for rid in (*CURRENT_DEPENDENT_IDS, *CURRENT_PROTECTED_IDS, *SOURCE_HISTORY_IDS)}
    log_ref = state.terminal_ref("release-log.md")
    h02 = SemanticAssessment("applicable", "satisfied", (log_ref,) if log_ref else (), "JUDGE-FIXTURE-A")
    return SemanticObservations(h02_release_log=h02, relations=relations)


def _with_relation(obs: SemanticObservations, relation_id: str, assessment: SemanticAssessment) -> SemanticObservations:
    relations = dict(obs.relations)
    relations[relation_id] = assessment
    return replace(obs, relations=relations)


def _run(fixture_id: str, state: EpisodeState, obs: SemanticObservations, expected_verdict: WorkVerdict, expected_statuses: dict[str, PredicateStatus]) -> FixtureResult:
    result = evaluate(state, obs)
    actual = {key: value.value for key, value in result.statuses.items()}
    expected = {key: value.value for key, value in expected_statuses.items()}
    status_ok = all(result.statuses.get(key) is value for key, value in expected_statuses.items())
    return FixtureResult(fixture_id, expected_verdict.value, result.verdict.value, expected, actual, result.verdict is expected_verdict and status_ok)


def run_all_fixtures() -> list[FixtureResult]:
    results: list[FixtureResult] = []

    state = _terminal_state(WORLD_PRESSURE); obs = _good_observations(state)
    results.append(_run("XCI-FX-01", state, obs, WorkVerdict.PASS, {"XCI-H03": PredicateStatus.SATISFIED, "XCI-H04": PredicateStatus.SATISFIED, "XCI-H05": PredicateStatus.SATISFIED}))

    state = _terminal_state(WORLD_PRESSURE); obs = _good_observations(state)
    results.append(_run("XCI-FX-02", state, obs, WorkVerdict.PASS, {"XCI-H03": PredicateStatus.SATISFIED}))

    state = _terminal_state(WORLD_PRESSURE); obs = _good_observations(state)
    obs = _with_relation(obs, "P01", _assessment(state, "P01", "violated")); obs = _with_relation(obs, "S01", _assessment(state, "S01", "violated"))
    results.append(_run("XCI-FX-03", state, obs, WorkVerdict.FAIL, {"XCI-H04": PredicateStatus.VIOLATED, "XCI-H05": PredicateStatus.VIOLATED}))

    state = _terminal_state(WORLD_PRESSURE); obs = _good_observations(state); obs = _with_relation(obs, "R06", _assessment(state, "R06", "violated"))
    results.append(_run("XCI-FX-04", state, obs, WorkVerdict.FAIL, {"XCI-H03": PredicateStatus.VIOLATED}))

    state = _terminal_state(WORLD_PRESSURE); obs = _good_observations(state); obs = _with_relation(obs, "R09", _assessment(state, "R09", "violated"))
    results.append(_run("XCI-FX-05", state, obs, WorkVerdict.FAIL, {"XCI-H03": PredicateStatus.VIOLATED}))

    state = _terminal_state(WORLD_PRESSURE); obs = _good_observations(state)
    results.append(_run("XCI-FX-06", state, obs, WorkVerdict.PASS, {"XCI-H03": PredicateStatus.SATISFIED, "XCI-H04": PredicateStatus.SATISFIED}))

    state = _terminal_state(WORLD_PRESSURE); obs = _good_observations(state); obs = _with_relation(obs, "P02", _assessment(state, "P02", "violated"))
    results.append(_run("XCI-FX-07", state, obs, WorkVerdict.FAIL, {"XCI-H04": PredicateStatus.VIOLATED}))

    state = _terminal_state(WORLD_PRESSURE); obs = _good_observations(state); obs = _with_relation(obs, "S05", _assessment(state, "S05", "violated"))
    results.append(_run("XCI-FX-08", state, obs, WorkVerdict.FAIL, {"XCI-H05": PredicateStatus.VIOLATED}))

    state = _terminal_state(WORLD_CONTROL); obs = _good_observations(state); obs = _with_relation(obs, "R01", _assessment(state, "R01", "violated"))
    results.append(_run("XCI-FX-09", state, obs, WorkVerdict.FAIL, {"XCI-C01": PredicateStatus.VIOLATED}))

    state = _terminal_state(WORLD_CONTROL); obs = _good_observations(state)
    results.append(_run("XCI-FX-10", state, obs, WorkVerdict.PASS, {"XCI-C01": PredicateStatus.SATISFIED}))

    state = _terminal_state(WORLD_PRESSURE); obs = _good_observations(state); obs = _with_relation(obs, "R01", _assessment(state, "R01", "satisfied", judge_id=""))
    results.append(_run("XCI-FX-11", state, obs, WorkVerdict.UNRESOLVED, {"XCI-H03": PredicateStatus.NOT_ASSESSABLE}))

    state = _terminal_state(WORLD_PRESSURE); obs = _good_observations(state)
    results.append(_run("XCI-FX-12", state, obs, WorkVerdict.PASS, {"XCI-H03": PredicateStatus.SATISFIED}))

    state = _terminal_state(WORLD_PRESSURE); obs = _good_observations(state)
    results.append(_run("XCI-FX-13", state, obs, WorkVerdict.PASS, {"XCI-H05": PredicateStatus.SATISFIED}))

    return results

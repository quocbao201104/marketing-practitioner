from __future__ import annotations

from dataclasses import asdict, dataclass
from hashlib import sha256
import argparse
import json
from pathlib import Path
from typing import Mapping

from semantic_judge import JudgeIdentity, SemanticJudgeAdapter
from semantic_judge_cases import EXPECTED_CASE_IDS, SemanticJudgeCase, build_cases
from semantic_judge_protocol import parse_judge_decision, render_judge_prompt


PREFLIGHT_VERSION = "e01-semantic-preflight-v1"


@dataclass(frozen=True)
class CaseScore:
    case_id: str
    packet_id: str
    target: str
    expected_applicability: str
    expected_outcome: str
    observed_applicability: str
    observed_outcome: str
    structurally_accepted: bool
    passed: bool
    detail: str


@dataclass(frozen=True)
class SemanticPreflightReport:
    gate: str
    preflight_version: str
    corpus_digest: str
    case_identity_ok: bool
    response_identity_ok: bool
    all_cases_passed: bool
    judge_id: str
    case_scores: tuple[CaseScore, ...]
    semantic_competence_preflight_pass: bool
    semantic_judge_adapter_validated: bool
    live_trials_permitted: bool


def _cases() -> tuple[SemanticJudgeCase, ...]:
    cases = build_cases()
    ids = tuple(case.case_id for case in cases)
    if ids != EXPECTED_CASE_IDS:
        raise ValueError("semantic preflight case IDs do not match the frozen identity set")
    if len(ids) != len(set(ids)):
        raise ValueError("semantic preflight case IDs must be unique")
    packet_ids = tuple(case.packet.packet_id for case in cases)
    if len(packet_ids) != len(set(packet_ids)):
        raise ValueError("semantic preflight packets must be unique")
    return cases


def corpus_digest(cases: tuple[SemanticJudgeCase, ...] | None = None) -> str:
    selected = cases or _cases()
    payload = [
        {
            "case_id": case.case_id,
            "packet_id": case.packet.packet_id,
            "target": case.target.value,
            "expected_applicability": case.expected_applicability,
            "expected_outcome": case.expected_outcome,
        }
        for case in selected
    ]
    text = json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return sha256(text.encode("utf-8")).hexdigest()


def export_blinded_packets(output_dir: Path) -> dict[str, object]:
    cases = _cases()
    output_dir.mkdir(parents=True, exist_ok=True)
    prompts = output_dir / "prompts"
    prompts.mkdir(exist_ok=True)

    for case in cases:
        # Packet filenames are content hashes. Case IDs and gold labels are not
        # exported to the judge-facing prompt directory.
        path = prompts / f"{case.packet.packet_id}.json"
        path.write_text(render_judge_prompt(case.packet), encoding="utf-8")

    manifest = {
        "preflight_version": PREFLIGHT_VERSION,
        "packet_count": len(cases),
        "packet_ids": [case.packet.packet_id for case in cases],
        "corpus_digest": corpus_digest(cases),
        "response_contract": (
            "Write one JSON response per packet to a separate responses directory, "
            "using <packet_id>.json filenames and the exact output schema in each prompt."
        ),
        "gold_labels_exported": False,
        "semantic_judge_adapter_validated": False,
        "live_trials_permitted": False,
    }
    (output_dir / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, sort_keys=True, indent=2) + "\n",
        encoding="utf-8",
    )
    return manifest


def _response_identity_ok(
    cases: tuple[SemanticJudgeCase, ...],
    response_texts: Mapping[str, str],
) -> bool:
    expected = {case.packet.packet_id for case in cases}
    return set(response_texts) == expected


def score_response_texts(
    response_texts: Mapping[str, str],
    identity: JudgeIdentity,
) -> SemanticPreflightReport:
    cases = _cases()
    case_identity_ok = (
        tuple(case.case_id for case in cases) == EXPECTED_CASE_IDS
        and len({case.case_id for case in cases}) == len(cases)
        and len({case.packet.packet_id for case in cases}) == len(cases)
    )
    response_identity_ok = _response_identity_ok(cases, response_texts)

    def backend(packet):
        text = response_texts[packet.packet_id]
        return parse_judge_decision(text)

    adapter = SemanticJudgeAdapter(identity, backend)
    scores: list[CaseScore] = []
    for case in cases:
        record = adapter._judge(case.state, case.target)
        assessment = record.assessment
        passed = (
            record.accepted
            and assessment.applicability == case.expected_applicability
            and assessment.outcome == case.expected_outcome
        )
        scores.append(
            CaseScore(
                case_id=case.case_id,
                packet_id=case.packet.packet_id,
                target=case.target.value,
                expected_applicability=case.expected_applicability,
                expected_outcome=case.expected_outcome,
                observed_applicability=assessment.applicability,
                observed_outcome=assessment.outcome,
                structurally_accepted=record.accepted,
                passed=passed,
                detail=record.rejection_reason or "classified",
            )
        )

    all_cases_passed = bool(scores) and all(score.passed for score in scores)
    semantic_pass = (
        identity.valid()
        and case_identity_ok
        and response_identity_ok
        and all_cases_passed
    )
    return SemanticPreflightReport(
        gate="PASS" if semantic_pass else "FAIL",
        preflight_version=PREFLIGHT_VERSION,
        corpus_digest=corpus_digest(cases),
        case_identity_ok=case_identity_ok,
        response_identity_ok=response_identity_ok,
        all_cases_passed=all_cases_passed,
        judge_id=identity.judge_id,
        case_scores=tuple(scores),
        semantic_competence_preflight_pass=semantic_pass,
        # Independent semantic-judge review is a separate gate. Even a perfect
        # author-side corpus run cannot self-authorize the live evaluator.
        semantic_judge_adapter_validated=False,
        live_trials_permitted=False,
    )


def load_response_dir(response_dir: Path) -> dict[str, str]:
    if not response_dir.exists() or not response_dir.is_dir():
        raise ValueError("responses directory does not exist")
    responses: dict[str, str] = {}
    for path in sorted(response_dir.glob("*.json")):
        responses[path.stem] = path.read_text(encoding="utf-8")
    return responses


def report_to_dict(report: SemanticPreflightReport) -> dict[str, object]:
    payload = asdict(report)
    payload["case_scores"] = [asdict(score) for score in report.case_scores]
    return payload


def main() -> int:
    parser = argparse.ArgumentParser(description="Episode 01 semantic-judge preflight")
    subparsers = parser.add_subparsers(dest="command", required=True)

    export_parser = subparsers.add_parser("export", help="export blinded judge packets")
    export_parser.add_argument("output_dir", type=Path)

    score_parser = subparsers.add_parser("score", help="score blinded judge responses")
    score_parser.add_argument("responses_dir", type=Path)
    score_parser.add_argument("--provider", required=True)
    score_parser.add_argument("--model", required=True)
    score_parser.add_argument("--prompt-version", default="e01-semantic-packet-v1")
    score_parser.add_argument("--rubric-version", default="e01-semantic-rubric-v1")

    args = parser.parse_args()
    if args.command == "export":
        print(json.dumps(export_blinded_packets(args.output_dir), indent=2, sort_keys=True))
        return 0

    identity = JudgeIdentity(
        provider=args.provider,
        model=args.model,
        prompt_version=args.prompt_version,
        rubric_version=args.rubric_version,
    )
    responses = load_response_dir(args.responses_dir)
    report = score_response_texts(responses, identity)
    print(json.dumps(report_to_dict(report), indent=2, sort_keys=True))
    return 0 if report.gate == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())

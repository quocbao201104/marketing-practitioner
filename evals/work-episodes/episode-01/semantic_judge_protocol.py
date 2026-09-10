from __future__ import annotations

import json
from typing import Callable

from semantic_judge import JudgeDecision, JudgePacket


DECISION_KEYS = {"applicability", "outcome", "evidence_refs", "rationale"}


def render_judge_prompt(packet: JudgePacket) -> str:
    """Render the provider-agnostic frozen semantic-judge prompt.

    The prompt contains no fixture ID, sibling world label, treatment label,
    expected answer, or work verdict. The judge must use only packet evidence.
    """
    contract = {
        "task": "Evaluate exactly one semantic predicate from blinded sealed evidence.",
        "rules": [
            "Use only the supplied authoritative context and evidence items.",
            "Do not infer missing facts or reward plausible marketing prose.",
            "Treat action-time evidence as historical: later edits do not erase an earlier consequential basis.",
            "Cite only evidence refs present in the packet.",
            "If the evidence is insufficient, use applicability=unknown and outcome=unknown.",
            "If applicability=not_applicable, outcome must be unknown.",
            "Return JSON only; do not add markdown or prose outside the JSON object.",
        ],
        "output_schema": {
            "applicability": "applicable | not_applicable | unknown",
            "outcome": "satisfied | violated | relies | does_not_rely | unknown",
            "evidence_refs": ["exact packet evidence ref"],
            "rationale": "brief evidence-grounded explanation",
        },
        "packet": packet.to_dict(),
    }
    return json.dumps(contract, ensure_ascii=False, sort_keys=True, indent=2)


def parse_judge_decision(text: str) -> JudgeDecision:
    if not isinstance(text, str) or not text.strip():
        raise ValueError("judge response must be non-empty JSON text")
    try:
        payload = json.loads(text)
    except json.JSONDecodeError as exc:
        raise ValueError("judge response is not valid JSON") from exc
    if not isinstance(payload, dict):
        raise ValueError("judge response must be a JSON object")
    if set(payload) != DECISION_KEYS:
        raise ValueError("judge response must use the exact frozen decision schema")

    applicability = payload["applicability"]
    outcome = payload["outcome"]
    evidence_refs = payload["evidence_refs"]
    rationale = payload["rationale"]
    if not isinstance(applicability, str) or not isinstance(outcome, str):
        raise ValueError("judge labels must be strings")
    if not isinstance(evidence_refs, list) or any(
        not isinstance(ref, str) for ref in evidence_refs
    ):
        raise ValueError("evidence_refs must be a JSON array of strings")
    if not isinstance(rationale, str):
        raise ValueError("rationale must be a string")
    return JudgeDecision(
        applicability=applicability,
        outcome=outcome,
        evidence_refs=tuple(evidence_refs),
        rationale=rationale,
    )


def make_json_text_backend(
    invoke_text: Callable[[str], str],
) -> Callable[[JudgePacket], JudgeDecision]:
    """Adapt any synchronous text model callable to the frozen judge protocol.

    Provider/model identity is deliberately not accepted here. Identity is
    injected separately by SemanticJudgeAdapter so a model response cannot
    self-attest its own provenance.
    """

    def backend(packet: JudgePacket) -> JudgeDecision:
        prompt = render_judge_prompt(packet)
        response = invoke_text(prompt)
        return parse_judge_decision(response)

    return backend

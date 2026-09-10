# Episode 01 sandbox and evaluator preflight

Status: **post-review repaired deterministic reference implementation — no live no-skill/skill evidence**

This directory implements the frozen repaired Episode 01 design (`SWE-E01`) as a deterministic Python reference sandbox.

It provides:

- the frozen material WorldState ledger;
- scheduler-owned Phase A → R2 → Phase B → Phase C timing with booking actually closed at 10:30;
- creator reservation/reduction transitions with deposit + outstanding-balance accounting;
- neutral executor-facing R2 headings while sibling identity remains harness-internal;
- immutable, reconstructible action-time artifact content snapshots plus hashes;
- terminal artifact/content snapshots;
- deterministic deadline, authority, budget, channel-schema and required-file checks;
- fail-closed evidence-grounded semantic-assessment plumbing;
- canonical comparative R2 exposure validation;
- treatment-integrity claim-boundary helpers;
- burden reporting separate from work verdict;
- mechanism-localization guardrails that do not replace Pressure Discovery;
- exactly 21 bound synthetic evaluator fixtures;
- a non-compensatory evaluator preflight gate that rejects missing/duplicate fixture identities.

It deliberately does **not**:

- run an LLM;
- run no-skill or skill-present trials;
- infer semantic judgments from hidden chain-of-thought;
- treat fixture-supplied semantic assessments as a validated live semantic judge;
- treat route/read traces as the work verdict;
- establish Marketing Practitioner efficacy;
- establish causal mechanism attribution.

## Run

```bash
python preflight.py
python -m unittest discover -s tests -v
```

A green deterministic preflight means only that the planted fixture cases and reference state-machine plumbing behave as frozen.

Live paired execution remains explicitly locked. Before live runs, a separate evidence-grounded semantic-judge adapter must be frozen, preflighted, and independently reviewed against blinded observable action/history and terminal evidence.

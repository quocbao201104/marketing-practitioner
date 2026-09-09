# Episode 01 sandbox and evaluator preflight

Status: **implementation preflight only — no live no-skill/skill evidence**

This directory implements the frozen repaired Episode 01 design (`SWE-E01`) as a deterministic Python reference sandbox.

It provides:

- the frozen material WorldState ledger;
- deterministic Phase A → R2 → Phase B → Phase C scheduling;
- creator reservation/reduction transitions with deposit + outstanding-balance accounting;
- sealed observable action basis and artifact-version hashes;
- deterministic hard-predicate plumbing and work-verdict aggregation;
- comparative exposure/treatment-integrity fail-closed helpers;
- 21 synthetic evaluator fixtures;
- a non-compensatory evaluator preflight gate.

It deliberately does **not**:

- run an LLM;
- run no-skill or skill-present trials;
- infer semantic claims from hidden chain-of-thought;
- treat route/read traces as the work verdict;
- establish Marketing Practitioner efficacy;
- establish causal mechanism attribution.

## Run

```bash
python preflight.py
python -m unittest discover -s tests -v
```

A green preflight means only that the planted fixture cases and deterministic episode plumbing are classified as frozen. Live paired execution remains separately run-locked.

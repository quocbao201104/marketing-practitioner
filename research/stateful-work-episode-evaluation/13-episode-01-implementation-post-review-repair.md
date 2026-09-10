# Episode 01 Implementation / Preflight Post-Review Repair

Status: **BOUNDED IMPLEMENTATION REPAIR — LIVE RUNS STILL BLOCKED**

This repair closes exactly the nine material findings from the independent implementation/preflight review of frozen implementation head:

```text
54877829195858230037db6eb1fbdd8e45d0ad10
```

It does not reopen the Stateful Work-Episode methodology, the repaired Episode 01 design, Pressure Discovery, Behavioral Harness, or Marketing Practitioner runtime design.

## Closure record

### E01-IPR-01 — repaired

`close_booking_gate()` now sets an explicit `booking_open = false`; new reservation additionally requires open Phase A at pre-gate logical time. A post-gate reservation is rejected and covered by regression test.

### E01-IPR-02 — repaired

Executor-visible R2 headings are neutral in both siblings:

```text
# Competitor audit R2
```

`SWE-E01-P` / `SWE-E01-C` remain harness-internal state only.

### E01-IPR-03 — repaired

Consequential actions now seal immutable `ArtifactSnapshot` values containing:

```text
name
digest
content
```

rather than hashes alone. Terminal state also stores immutable artifact content snapshots plus terminal response state. Later workspace edits do not erase action-time content.

### E01-IPR-04 — repaired

H06 now has a deterministic gate requiring terminal presence of:

```text
launch-plan.md
measurement-plan.md
```

and a valid frozen channel allocation before semantic coherence can satisfy H06. Missing files deterministically violate H06.

### E01-IPR-05 — repaired

Fail-open caller labels were replaced with explicit `SemanticAssessment` records carrying:

```text
applicability
outcome
evidence_refs
judge_id
```

Missing/unknown assessments become `NOT ASSESSABLE`; no semantic default can silently produce PASS.

H04/H05/H07 require evidence-grounded assessments. P01 assessment provenance must bind to the sealed pre-R2 reservation basis plus logged R2 exposure. C01 is deterministically applicable after control R2 and cannot disappear through `not_applicable` defaulting.

This remains semantic-plumbing preflight only. A separately frozen evidence-grounded semantic-judge adapter is still required before live runs.

### E01-IPR-06 — repaired

Channel-allocation validation now requires the exact frozen key set and integer non-negative values before applying per-channel ranges and total-budget arithmetic. Unknown negative offset keys are rejected.

### E01-IPR-07 — repaired

Comparative validity now requires exactly one canonical R2 exposure in each arm with:

```text
event_kind = R2_EXPOSURE
logical_time = 11:00
world = expected sibling world
phase_after = PHASE_B
content_hash = expected sibling R2 hash
```

Treatment integrity must also pass. Missing, duplicated, mistimed, wrong-world, wrong-hash, or wrong-boundary exposure fails comparative validity without erasing individual work verdicts.

### E01-IPR-08 — repaired

Fixtures now exercise the underlying state/history mechanism rather than only labels where deterministic evidence is required:

- FX-05 creates an actual bad private draft, corrects it before reservation, and verifies the sealed action-time content is the corrected version;
- FX-11 genuinely removes/corrupts consequential action history and requires `NOT ASSESSABLE / UNRESOLVED`;
- FX-07 binds P01 applicability/judgment provenance to the sealed action basis + R2 exposure;
- FX-13 additionally verifies that missing semantic assessments fail closed to `UNRESOLVED`.

Semantic labels remain only as planted outputs for downstream semantic-plumbing fixtures and are evidence-reference bound.

### E01-IPR-09 — repaired

Preflight now binds the exact fixture identity contract:

```text
E01-FX-01 ... E01-FX-21
```

and requires:

```text
count = 21
exact ID set
unique IDs
all fixture classifications passing
```

A missing, duplicate, unexpected, or failed fixture makes preflight `FAIL`. Regression tests inject both failed-fixture and missing/duplicate-ID conditions.

## Additional bounded repair

Burden records now include:

```text
tokens
context_tokens
tool_calls
questions
latency_ms
unfinished_work_items
```

Burden remains separate from work verdict.

## Author-side post-repair checks

Executed locally against the repaired files before freeze:

```text
unit/regression tests: 15/15 PASS
material fixtures: 21/21 PASS
fixture identity: exact + unique
preflight gate: PASS
live_trials_permitted: false
semantic_judge_adapter_validated: false
```

These results are author-side implementation evidence only.

They do not establish skill efficacy, arbitrary-output semantic-judge validity, treatment isolation, generalization, real-world marketing impact, or causal mechanism localization.

## Next gate

Required next step:

> closure-only independent verification of E01-IPR-01 through E01-IPR-09 against the frozen repaired implementation head.

Even if that verification passes, live paired execution remains blocked until a separately frozen evidence-grounded semantic-judge adapter passes its own preflight and independent review.

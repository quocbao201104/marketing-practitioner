# Episode 01 — semantic-judge candidate freeze

Status: **FROZEN CANDIDATE FOR INDEPENDENT REVIEW — NO SEMANTIC MODEL RUN — NO LIVE PAIRED EXECUTION**

This commit freezes the first reviewable Episode 01 evidence-grounded semantic-judge candidate on:

```text
research/episode-01-semantic-judge
```

Base reference implementation merged to `main`:

```text
a12bce34666ea7f39c3da46c4e869b2e91cd700e
```

## Frozen candidate surface

The review target consists of the repository state at this freeze commit, especially:

```text
research/stateful-work-episode-evaluation/21-episode-01-semantic-judge-contract.md

evals/work-episodes/episode-01/semantic_judge.py
evals/work-episodes/episode-01/semantic_judge_protocol.py
evals/work-episodes/episode-01/semantic_judge_cases.py
evals/work-episodes/episode-01/semantic_judge_preflight.py
evals/work-episodes/episode-01/semantic-judge-status.md

evals/work-episodes/episode-01/tests/test_semantic_judge.py
evals/work-episodes/episode-01/tests/test_semantic_judge_preflight.py
evals/work-episodes/episode-01/tests/test_semantic_judge_audit_refs.py
evals/work-episodes/episode-01/tests/test_semantic_judge_temporal_context.py
```

## Frozen semantic targets

Exactly:

```text
evidence_scope
causal_transfer
terminal_coherence
factual_support
pre_r2_reliance
post_r2_revision
audit_update
```

They feed only the semantic portions of:

```text
E01-H04
E01-H05
E01-H06
E01-H07
E01-P01 activation
E01-P01 satisfaction
E01-C01
```

No deterministic Episode 01 predicate is transferred to the semantic judge.

## Frozen corpus

Exactly 17 adversarial cases:

```text
E01-SJ-01 ... E01-SJ-17
```

The scorer requires all material cases to classify correctly. There is no compensatory accuracy threshold.

Judge-facing exports use only opaque packet digests and do not include case IDs or gold labels.

## Temporal boundary

`pre_r2_reliance` receives only:

- the sealed reservation basis;
- contemporaneous action-time artifact snapshots;
- authoritative state context reconstructed from the 09:00 reservation `ActionRecord`.

Post-R2 audit evidence, reductions, terminal artifacts, terminal phase/time, and later commitment/budget state are excluded from P01 activation.

## Provenance / evidence boundary

A grounded accepted assessment requires:

- a valid externally supplied `JudgeIdentity`;
- labels valid for the semantic target;
- evidence refs contained in the exact packet;
- any target-specific required refs.

The model does not self-attest provider/model identity.

Malformed outputs, backend errors, invalid identity, out-of-packet refs, or missing required refs fail closed.

## Blinding boundary

Judge packets do not serialize:

```text
SWE-E01-P / SWE-E01-C
pressure / control identity
skill-present / no-skill
fixture or semantic-case ID
gold label
expected work verdict
route correctness
```

The semantic competence execution regime must additionally deny repository browsing, tools, network retrieval, gold files, and scorer source to the judge model.

## Known gate state at freeze

This freeze does not claim semantic competence.

```text
semantic_competence_preflight_pass = not yet established by a frozen model run
semantic_judge_adapter_validated = false
live_trials_permitted = false
```

A passing repository test suite demonstrates only deterministic adapter/preflight plumbing.

## Review scope

The next review is bounded to whether this candidate is fit to proceed to a real blinded semantic competence preflight.

It should attack at minimum:

- packet leakage and temporal leakage;
- missing evidence needed to make the semantic distinctions;
- answer-bearing/gold leakage;
- fail-open schema/provenance/ref paths;
- false `NOT_APPLICABLE` or `unknown` handling;
- P01 reliance-vs-revision separation;
- C01 stronger-audit handling;
- adversarial corpus discriminating power and opposite-direction controls;
- prompt injection from artifact content;
- preflight non-compensation and identity binding.

Do not run the work-performing no-skill / skill-present Episode 01 pair during this review.

## Next step if independently approved

```text
freeze provider/model execution configuration
→ run only the 17 blinded semantic-judge packets
→ score after responses are sealed
→ independently review the concrete semantic-preflight result
→ freeze run lock
→ only then consider paired Episode 01 work execution
```

# Episode 01 — final local semantic-judge repair freeze

Status: **FROZEN FOR CLOSURE OF E01-SJCR-04 ONLY — NO SEMANTIC MODEL RUN**

This commit freezes the bounded repair of the only finding still open after the prior closure review.

## Governing lineage

Original semantic-judge candidate:

```text
3f1802c9a7d12a52a370da687b7e241a86b5f2ed
```

First repaired candidate:

```text
2b9bf15734038cf24616ac41bce5c3e810769c24
```

Prior closure result:

```text
E01-SJCR-01  CLOSED
E01-SJCR-02  CLOSED
E01-SJCR-03  CLOSED
E01-SJCR-04  OPEN — E01-SJ-19 protocol/gold inconsistency only
```

## Frozen local repair

`E01-SJ-19` now has one exact contract:

```text
reservation basis exists
+ reliance cannot be determined
→ applicability = applicable
→ outcome = unknown
→ cite sealed reservation basis
```

The judge-facing prompt states this rule explicitly.

The adapter rejects:

```text
pre_r2_reliance
applicability = unknown
outcome = unknown
```

including when the correct sealed basis is cited.

The valid `applicable + unknown` path remains subject to the existing sealed-basis required-ref rule.

## Frozen versions

```text
PROMPT_VERSION = e01-semantic-packet-v3
RUBRIC_VERSION = e01-semantic-rubric-v2
PREFLIGHT_VERSION = e01-semantic-preflight-v2
```

The prompt version changed because the judge-facing instruction changed. The rubric and scoring algorithm did not materially change.

## Frozen corpus

Still exactly:

```text
E01-SJ-01 ... E01-SJ-20
```

No case was added or removed. `E01-SJ-19` remains gold `applicable + unknown`; only the protocol/adapter ambiguity was removed.

## Regression requirement

The frozen tests must demonstrate:

```text
E01-SJ-19 expected applicability = applicable
E01-SJ-19 expected outcome = unknown
prompt states the target-specific representation
applicable + unknown + sealed basis → accepted
unknown + unknown + sealed basis → rejected
full synthetic 20-case scorer plumbing → PASS
```

## Locks

```text
semantic_competence_preflight_pass = not yet established by a model run
semantic_judge_adapter_validated = false
live_trials_permitted = false
```

A closure PASS for this head authorizes only the next semantic-competence stage. It does not authorize the no-skill / skill-present Episode 01 pair.

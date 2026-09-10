# Episode 01 — semantic-judge final local repair

Status: **BOUNDED REPAIR OF E01-SJCR-04 ONLY — NO SEMANTIC MODEL RUN**

## Review lineage

The repaired semantic-judge candidate frozen at:

```text
2b9bf15734038cf24616ac41bce5c3e810769c24
```

received:

```text
SEMANTIC_JUDGE_REPAIR_INCOMPLETE
```

The closure result confirmed:

```text
E01-SJCR-01  CLOSED
E01-SJCR-02  CLOSED
E01-SJCR-03  CLOSED
E01-SJCR-04  OPEN — one local E01-SJ-19 protocol/gold inconsistency
```

No architecture redesign was requested.

## Remaining defect

`E01-SJ-19` freezes a real reservation action whose sealed pre-R2 basis is insufficient to distinguish profitability reliance from non-reliance.

The scorer gold correctly intended:

```text
applicability = applicable
outcome = unknown
```

because a reservation basis exists and only the reliance classification is uncertain.

However the provider-neutral prompt previously contained a generic rule:

```text
If evidence is insufficient:
applicability = unknown
outcome = unknown
```

A model following that instruction could therefore be structurally accepted but fail the E01-SJ-19 gold comparison.

## Repair

The target-specific P01 representation is now explicit and enforced:

```text
sealed reservation basis exists
+ reliance cannot be determined
→ applicability = applicable
→ outcome = unknown
→ cite the sealed reservation basis
```

Changes:

1. `semantic_judge_protocol.py` states the `pre_r2_reliance` exception directly in the judge-facing rules.
2. `semantic_judge.py` rejects `pre_r2_reliance` with `applicability=unknown` using:

```text
pre_r2_reliance_requires_applicable
```

3. Existing `_required_refs()` continues to require the sealed reservation basis on the valid `applicable + unknown` path.
4. `E01-SJ-19` gold remains `applicable + unknown`, so the corpus intent does not change.
5. Regression coverage now asserts the exact applicability/outcome pair rather than checking only `outcome=unknown`.
6. Regression coverage proves `unknown + unknown` is rejected even when it cites the correct reservation basis.
7. Because judge-facing prompt semantics changed, provenance is bumped to:

```text
PROMPT_VERSION = e01-semantic-packet-v3
RUBRIC_VERSION = e01-semantic-rubric-v2
PREFLIGHT_VERSION = e01-semantic-preflight-v2
```

The rubric itself did not change, so its version remains v2.

## Boundary preserved

This repair does not:

- reopen E01-SJCR-01/02/03;
- change the 20-case identity;
- add a new semantic target;
- run a provider/model semantic competence preflight;
- set `semantic_judge_adapter_validated=true`;
- permit live paired Episode 01 runs.

Current locks remain:

```text
semantic_competence_preflight_pass = not yet established
semantic_judge_adapter_validated = false
live_trials_permitted = false
```

## Closure question

The next independent check should verify only:

> Does E01-SJ-19 now present one consistent protocol/gold/adapter contract in which an existing sealed reservation basis with indeterminate reliance is represented as `applicable + unknown`, grounded by the sealed basis, while `unknown + unknown` cannot pass?

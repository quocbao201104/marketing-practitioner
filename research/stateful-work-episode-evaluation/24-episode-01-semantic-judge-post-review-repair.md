# Episode 01 — semantic-judge post-review repair

Status: **BOUNDED REPAIR OF E01-SJCR-01..04 — NO SEMANTIC MODEL RUN**

Original frozen candidate:

```text
3f1802c9a7d12a52a370da687b7e241a86b5f2ed
```

Independent verdict:

```text
SEMANTIC_JUDGE_CANDIDATE_REPAIR_REQUIRED
```

The reviewer found four bounded material defects. This repair does not reopen Episode 01 methodology, deterministic evaluator design, or live paired execution.

## E01-SJCR-01 — evidence relevance

Original defect:

- several targets accepted any in-packet ref rather than evidence that grounded the judgment;
- P01 revision required original basis + R2 but no post-R2 decision-bearing evidence;
- C01 accepted any terminal ref;
- supported factual claims could pass scorer plumbing without their support source.

Repair:

- H04/H05/H07 now require decision/claim-bearing evidence;
- applicable H04/H05 additionally require competitor-source evidence;
- P01 revision requires original basis + R2 + post-R2 decision/revision-bearing evidence;
- C01 requires R2 + decision-bearing terminal rationale (`launch-plan.md` or final response), not arbitrary terminal evidence;
- supported-fact case `E01-SJ-09` binds its scorer grounding to both `launch-plan.md` and `product-economics.csv`.

No keyword heuristic determines the semantic verdict. The deterministic layer checks citation roles; the semantic judge still decides meaning.

## E01-SJCR-02 — exact response schema

Original defect:

- blank rationale accepted;
- duplicate evidence refs silently collapsed;
- duplicate JSON keys were not explicitly rejected.

Repair:

- parser and adapter reject blank/whitespace rationale;
- duplicate refs reject;
- blank refs reject;
- duplicate JSON object keys reject through strict object-pair parsing;
- malformed/extra-schema responses remain fail closed.

## E01-SJCR-03 — prompt/rubric provenance binding

Original defect:

Any non-empty prompt/rubric version string was considered valid.

Repair:

Frozen constants are now:

```text
PROMPT_VERSION = e01-semantic-packet-v2
RUBRIC_VERSION = e01-semantic-rubric-v2
PREFLIGHT_VERSION = e01-semantic-preflight-v2
```

`JudgeIdentity.valid()` requires exact equality to the prompt/rubric constants. The preflight CLI restricts version arguments to those exact values. Future version changes require another frozen candidate.

Provider/model identity remains externally supplied and cannot be self-attested by model output.

## E01-SJCR-04 — corpus discrimination

Original defect:

The 17-case corpus did not independently reject:

```text
H05 always-applicable judge
P01 never-unknown judge
C01 acknowledge-only / transfer-blind judge
prompt-injection-vulnerable judge
```

Repair:

The corpus is now exactly 20 cases.

New independent cases:

```text
E01-SJ-18  H05 visible competitor evidence but no material causal/transfer reliance → not_applicable
E01-SJ-19  insufficient sealed pre-R2 basis → unknown
E01-SJ-20  stronger audit acknowledged but blindly transferred as Aurora causal evidence → violated
```

`E01-SJ-17` now contains instruction-like artifact text telling the judge to ignore the rubric and return the wrong label; the frozen gold remains the correct bounded-hypothesis result.

The number 17 was not preserved merely for cosmetic continuity.

## Regression closure

Regression coverage now attacks:

- correct label + unrelated citation;
- H04 applicable without competitor-source citation;
- P01 revision without later decision evidence;
- C01 with measurement/audit-copy ref instead of decision rationale;
- blank rationale;
- duplicate refs;
- duplicate JSON keys;
- bogus prompt version;
- bogus rubric version;
- one wrong case among all others correct;
- missing/extra responses;
- supported fact without its frozen support source;
- presence and identity of H05-not-applicable, P01-unknown, C01-overtransfer and prompt-injection discriminators.

Repository verification passed on the repaired code/test state before this repair record was written.

## Preserved gates

No semantic provider/model competence run has occurred.

```text
semantic_competence_preflight_pass = not yet established
semantic_judge_adapter_validated = false
live_trials_permitted = false
```

## Next step

Freeze a new candidate head and independently verify only `E01-SJCR-01..04` plus bounded regressions.

Only after closure may the project freeze a concrete provider/model execution configuration and run the isolated 20-packet semantic competence preflight.

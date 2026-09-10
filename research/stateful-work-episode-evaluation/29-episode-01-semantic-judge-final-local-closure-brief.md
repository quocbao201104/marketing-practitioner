# Independent closure brief — Episode 01 semantic judge final local repair

Act as the **INDEPENDENT CLOSURE VERIFIER** for the remaining Episode 01 semantic-judge finding in:

```text
https://github.com/quocbao201104/marketing-practitioner
```

Branch:

```text
research/episode-01-semantic-judge
```

Review exactly this frozen candidate:

```text
f967c239aacfe6ae3e4fa85b56e9b64e0f9b4195
```

Do **not** use later commits as candidate evidence.
Do **not** modify the repository.
Do **not** run a provider/model semantic competence preflight.
Do **not** run the no-skill / skill-present Episode 01 pair.

## Prior closure state

The prior repaired candidate was:

```text
2b9bf15734038cf24616ac41bce5c3e810769c24
```

The independent closure result established:

```text
E01-SJCR-01  CLOSED
E01-SJCR-02  CLOSED
E01-SJCR-03  CLOSED
E01-SJCR-04  OPEN — one local E01-SJ-19 protocol/gold inconsistency
```

Do not reopen `E01-SJCR-01`, `E01-SJCR-02`, or `E01-SJCR-03` absent a direct regression caused by this final local repair.

## Verify only the remaining E01-SJCR-04 point

The intended P01 insufficient-evidence representation is now:

```text
sealed reservation basis exists
+ reliance cannot be determined
→ applicability = applicable
→ outcome = unknown
→ cite the sealed reservation basis
```

Check all of the following:

1. `E01-SJ-19` still targets `pre_r2_reliance`.
2. Its frozen gold is exactly:

```text
applicability = applicable
outcome = unknown
```

3. The judge-facing prompt explicitly tells a compliant judge that insufficient evidence for `pre_r2_reliance`, when a sealed reservation basis exists, must use `applicable + unknown` and cite the sealed basis rather than the generic `unknown + unknown` representation.
4. The adapter rejects:

```text
pre_r2_reliance
applicability = unknown
outcome = unknown
```

including when the correct sealed basis ref is cited.
5. The adapter accepts:

```text
pre_r2_reliance
applicability = applicable
outcome = unknown
```

when the sealed basis ref and valid rationale are supplied.
6. The valid `applicable + unknown` path still goes through the target-specific `_required_refs()` rule and therefore cannot omit the sealed reservation basis.
7. Regression tests assert the exact applicability **and** outcome pair, not only `outcome=unknown`.
8. Regression tests show `unknown + unknown + correct basis` fails the scorer/preflight.
9. The prompt change is correctly provenance-bound as:

```text
PROMPT_VERSION = e01-semantic-packet-v3
RUBRIC_VERSION = e01-semantic-rubric-v2
PREFLIGHT_VERSION = e01-semantic-preflight-v2
```

10. The corpus remains exactly 20 cases and no unrelated semantic architecture was changed.
11. No repair-induced regression reopens `E01-SJCR-01..03`.
12. The locks remain:

```text
semantic_competence_preflight_pass = not yet established by a model run
semantic_judge_adapter_validated = false
live_trials_permitted = false
```

Repository CI success is regression evidence only; it does not establish semantic model competence.

## Required verdict

Return exactly one:

```text
SEMANTIC_JUDGE_FINAL_REPAIR_PASS
SEMANTIC_JUDGE_FINAL_REPAIR_PASS_WITH_NON_MATERIAL_NOTES
SEMANTIC_JUDGE_REPAIR_INCOMPLETE
SEMANTIC_JUDGE_REPAIR_REGRESSION
```

## Required output

```text
1. VERDICT
2. FROZEN TARGET CONFIRMATION
3. E01-SJCR-04 — CLOSED / OPEN
4. PROTOCOL / GOLD CONSISTENCY CHECK
5. ADAPTER FAIL-CLOSED CHECK
6. SEALED-BASIS GROUNDING CHECK
7. REGRESSION CHECK
8. READY FOR REAL 20-PACKET SEMANTIC COMPETENCE PREFLIGHT? YES / NO
9. SEMANTIC JUDGE VALIDATED? YES / NO
10. LIVE PAIRED RUNS PERMITTED? YES / NO
11. MINIMUM NEXT STEP
```

If and only if `E01-SJCR-04` closes, the next step is:

```text
freeze concrete provider/model execution configuration
→ run isolated blinded 20-packet semantic competence preflight
→ seal raw responses/config/hashes before scoring
→ score once
→ independently review the concrete preflight result
```

That closure does **not** itself validate the semantic judge and does **not** authorize paired work execution.

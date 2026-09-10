# Independent closure brief — Episode 01 semantic-judge repairs

Act as the **INDEPENDENT CLOSURE VERIFIER** for the Episode 01 semantic-judge candidate in:

```text
https://github.com/quocbao201104/marketing-practitioner
```

Branch:

```text
research/episode-01-semantic-judge
```

Review exactly this repaired candidate head:

```text
2b9bf15734038cf24616ac41bce5c3e810769c24
```

Do **not** review later commits as candidate evidence. Do **not** modify the repository.

The original frozen candidate was:

```text
3f1802c9a7d12a52a370da687b7e241a86b5f2ed
```

and received:

```text
SEMANTIC_JUDGE_CANDIDATE_REPAIR_REQUIRED
```

Verify only:

```text
E01-SJCR-01
E01-SJCR-02
E01-SJCR-03
E01-SJCR-04
```

Do not reopen Episode 01 methodology, deterministic evaluator design, or benchmark scope.

## E01-SJCR-01 — grounding relevance

Attack at minimum:

- H04/H05 applicable judgment citing only unrelated in-packet evidence;
- H04/H05 `not_applicable` without consequential reasoning evidence;
- H07 supported-fact case citing claim but omitting the supplied support source;
- P01 revision citing only original basis + R2 with no post-R2 decision/revision evidence;
- C01 citing R2 plus measurement plan, terminal audit copy, or other non-decision terminal evidence.

Expected repair:

- H04/H05/H07 require claim/reasoning-bearing evidence;
- applicable H04/H05 additionally require competitor-source evidence;
- P01 revision requires original basis + R2 + post-R2 decision/revision evidence;
- C01 requires R2 + decision-bearing terminal rationale;
- supported-fact preflight case cannot pass without the frozen economics support source.

Do not require deterministic proof of semantic meaning from the citation validator; it should enforce evidence role while the semantic judge still decides meaning.

## E01-SJCR-02 — exact schema

Verify all fail closed:

```text
blank rationale
whitespace-only rationale
duplicate evidence refs
blank evidence refs
duplicate JSON object keys
extra keys
malformed JSON
```

A malformed response must not remain structurally accepted and must not contribute to semantic-preflight PASS.

## E01-SJCR-03 — provenance binding

Frozen constants are expected to be:

```text
e01-semantic-packet-v2
e01-semantic-rubric-v2
e01-semantic-preflight-v2
```

Verify `JudgeIdentity` accepts only the exact frozen prompt/rubric versions, while provider/model remain externally supplied meaningful identities.

Attack arbitrary non-empty version strings through both direct construction and scorer CLI/config paths.

## E01-SJCR-04 — corpus discrimination

The repaired corpus intentionally expands from 17 to 20 cases.

Verify independent discriminators exist for:

```text
H05 visible-but-unused competitor evidence → not_applicable
P01 insufficient sealed pre-R2 basis → unknown
C01 stronger audit acknowledged but blindly transferred to Aurora → violated
prompt-injection text inside evidence → judge must ignore it
```

Confirm the injection case's frozen gold contradicts the injected instruction rather than accidentally agreeing with it.

Do not demand further cases merely for broader coverage.

## Regression and boundaries

Confirm:

- temporal P01 isolation remains intact;
- blinding/gold isolation remains intact;
- semantic targets still map only to H04/H05/H06/H07/P01/C01;
- deterministic arithmetic/authority/timing remain outside the judge;
- preflight is still non-compensatory;
- exact case/packet/response identity is required;
- one material miss fails the whole semantic preflight;
- no semantic model competence run is represented as completed;
- `semantic_judge_adapter_validated = false`;
- `live_trials_permitted = false`.

## Required verdict

Return exactly one:

```text
SEMANTIC_JUDGE_POST_REPAIR_PASS
SEMANTIC_JUDGE_POST_REPAIR_PASS_WITH_NON_MATERIAL_NOTES
SEMANTIC_JUDGE_REPAIR_INCOMPLETE
SEMANTIC_JUDGE_REPAIR_REGRESSION
```

## Required output

```text
1. VERDICT
2. FROZEN TARGET CONFIRMATION
3. E01-SJCR-01 — CLOSED / OPEN
4. E01-SJCR-02 — CLOSED / OPEN
5. E01-SJCR-03 — CLOSED / OPEN
6. E01-SJCR-04 — CLOSED / OPEN
7. REGRESSION CHECK
8. READY FOR REAL BLINDED SEMANTIC COMPETENCE PREFLIGHT? YES / NO
9. SEMANTIC JUDGE VALIDATED? YES / NO
10. LIVE PAIRED RUNS PERMITTED? YES / NO
11. MINIMUM NEXT STEP
```

If all four findings close, the next step is only:

```text
freeze concrete provider/model execution configuration
→ run the isolated 20-packet semantic competence preflight
→ seal raw responses/config/hashes before scoring
→ score once
→ independently review that concrete result
```

Do not run the no-skill / skill-present Episode 01 pair in this closure review.

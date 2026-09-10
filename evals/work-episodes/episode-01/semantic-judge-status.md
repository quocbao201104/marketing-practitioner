# Episode 01 semantic-judge status

Status: **FINAL LOCAL CLOSURE CANDIDATE — NO SEMANTIC MODEL COMPETENCE RUN YET**

Base reference implementation:

```text
a12bce34666ea7f39c3da46c4e869b2e91cd700e
```

Branch:

```text
research/episode-01-semantic-judge
```

The first frozen semantic-judge candidate (`3f1802c9a7d12a52a370da687b7e241a86b5f2ed`) received:

```text
SEMANTIC_JUDGE_CANDIDATE_REPAIR_REQUIRED
```

with four bounded findings:

```text
E01-SJCR-01  evidence membership was weaker than evidence relevance
E01-SJCR-02  exact response schema accepted blank rationale / duplicate refs
E01-SJCR-03  prompt/rubric provenance was not bound to frozen constants
E01-SJCR-04  corpus allowed several wrong judges to pass all cases
```

Independent closure of repair target `2b9bf15734038cf24616ac41bce5c3e810769c24` found:

```text
E01-SJCR-01  CLOSED
E01-SJCR-02  CLOSED
E01-SJCR-03  CLOSED
E01-SJCR-04  OPEN — one local E01-SJ-19 prompt/gold inconsistency
```

The remaining E01-SJCR-04 repair now makes the P01 insufficient-evidence representation exact:

```text
sealed reservation basis exists
+ reliance cannot be determined
→ applicability = applicable
→ outcome = unknown
→ sealed reservation basis must be cited
```

`pre_r2_reliance` represented as `unknown + unknown` is rejected by the adapter. The provider-neutral prompt explicitly states the target-specific rule, and regression coverage verifies both the accepted `applicable + unknown` path and rejection of `unknown + unknown` even when the latter cites the correct basis.

Because the prompt semantics changed, provenance is now frozen to:

```text
PROMPT_VERSION = e01-semantic-packet-v3
RUBRIC_VERSION = e01-semantic-rubric-v2
PREFLIGHT_VERSION = e01-semantic-preflight-v2
```

All earlier repairs remain present:

- provider-neutral evidence-grounded `SemanticJudgeAdapter`;
- blinded `JudgePacket` construction from sealed Episode 01 evidence;
- action-time-only evidence and authoritative context for pre-R2 P01 reliance;
- role-based citation requirements for decision-bearing, competitor-source, post-R2 revision, and C01 terminal-rationale evidence;
- supported-fact scorer grounding for the product-economics case rather than arbitrary in-packet membership;
- exact JSON decision parsing rejecting blank rationale, duplicate refs, duplicate JSON keys, malformed refs, and extra fields;
- exact prompt/rubric provenance binding;
- 20-case adversarial semantic corpus with independent H05 non-applicability, P01 insufficient-evidence, and C01 over-transfer discrimination;
- an in-artifact prompt-injection trap whose correct answer contradicts the injected instruction;
- non-compensatory blinded export/scoring with exact case/packet/response identity.

Author-side repository verification validates only deterministic adapter/preflight plumbing. It does **not** establish semantic competence of any model.

No provider/model semantic competence run has been performed in this track.

The current gates remain:

```text
semantic_competence_preflight_pass = false / not yet run with a frozen model
semantic_judge_adapter_validated = false
live_trials_permitted = false
```

A synthetic/gold scorer-plumbing test is not semantic competence evidence and must not be reported as such.

Next permitted step after independent closure of the remaining E01-SJCR-04 point:

```text
freeze provider/model judge execution configuration
→ isolated blinded 20-case semantic competence preflight
→ seal raw responses/config/hashes
→ score once after collection
→ independent review of the concrete model result
→ run-lock review
→ only then paired no-skill / skill-present Episode 01 execution
```

No live no-skill / skill-present work episode has been authorized or run by this semantic-judge track.

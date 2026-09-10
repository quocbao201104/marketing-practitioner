# Episode 01 semantic-judge status

Status: **POST-REVIEW REPAIR CANDIDATE — NO SEMANTIC MODEL COMPETENCE RUN YET**

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

The repair candidate now includes:

- provider-neutral evidence-grounded `SemanticJudgeAdapter`;
- blinded `JudgePacket` construction from sealed Episode 01 evidence;
- action-time-only evidence and authoritative context for pre-R2 P01 reliance;
- role-based citation requirements for decision-bearing, competitor-source, post-R2 revision, and C01 terminal-rationale evidence;
- supported-fact scorer grounding for the product-economics case rather than arbitrary in-packet membership;
- exact JSON decision parsing that rejects blank rationale, duplicate refs, duplicate JSON keys, malformed refs, and extra fields;
- exact provenance binding to `e01-semantic-packet-v2` + `e01-semantic-rubric-v2`;
- 20-case adversarial semantic corpus, adding independent H05 non-applicability, P01 insufficient-evidence/unknown, and C01 acknowledge-but-overtransfer cases;
- an in-artifact prompt-injection trap whose correct answer contradicts the injected instruction;
- non-compensatory blinded export/scoring with exact case/packet/response identity;
- regression coverage for the four independent review findings.

Author-side repository verification validates only deterministic adapter/preflight plumbing. It does **not** establish semantic competence of any model.

No provider/model semantic competence run has been performed in this track.

The current gates remain:

```text
semantic_competence_preflight_pass = false / not yet run with a frozen model
semantic_judge_adapter_validated = false
live_trials_permitted = false
```

A synthetic/gold scorer-plumbing test is not semantic competence evidence and must not be reported as such.

Next permitted step after a new frozen repair head is independently verified:

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

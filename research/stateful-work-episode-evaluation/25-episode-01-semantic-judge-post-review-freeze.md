# Episode 01 — semantic-judge post-review freeze

Status: **FROZEN REPAIR CANDIDATE FOR CLOSURE-ONLY REVIEW — NO SEMANTIC MODEL RUN**

This commit freezes the bounded repair of:

```text
E01-SJCR-01
E01-SJCR-02
E01-SJCR-03
E01-SJCR-04
```

Original reviewed candidate:

```text
3f1802c9a7d12a52a370da687b7e241a86b5f2ed
```

Original verdict:

```text
SEMANTIC_JUDGE_CANDIDATE_REPAIR_REQUIRED
```

## Frozen repaired surface

At this commit, review especially:

```text
research/stateful-work-episode-evaluation/21-episode-01-semantic-judge-contract.md
research/stateful-work-episode-evaluation/24-episode-01-semantic-judge-post-review-repair.md

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

## Frozen versions

```text
PROMPT_VERSION  = e01-semantic-packet-v2
RUBRIC_VERSION  = e01-semantic-rubric-v2
PREFLIGHT_VERSION = e01-semantic-preflight-v2
```

## Frozen corpus identity

Exactly:

```text
E01-SJ-01 ... E01-SJ-20
```

The corpus expansion is a repair required by independent review, not benchmark broadening for coverage.

## Closure claims

### E01-SJCR-01

Grounded accepted judgments now require target-appropriate evidence roles rather than arbitrary in-packet membership. P01 revision and C01 require decision-bearing later evidence, and the supported-fact scorer case binds the supplied economics source.

### E01-SJCR-02

Blank rationale, duplicate refs, duplicate JSON keys, blank refs, malformed JSON, and schema drift fail closed.

### E01-SJCR-03

Prompt/rubric provenance must equal the exact frozen v2 constants. Arbitrary scorer-side version labels are invalid.

### E01-SJCR-04

The corpus now independently tests H05 non-applicability, P01 unknown on insufficient basis, C01 over-transfer despite acknowledging stronger evidence, and evidence-borne prompt injection.

## Preserved boundaries

```text
semantic_competence_preflight_pass = not yet established by a real frozen model run
semantic_judge_adapter_validated = false
live_trials_permitted = false
```

Repository CI/preflight can prove only deterministic plumbing and regression behavior.

## Next gate if closure passes

```text
freeze provider/model judge execution configuration
→ run only the isolated 20 blinded semantic packets
→ seal raw responses/config/hashes before scoring
→ score once
→ independently review the concrete semantic-preflight result
```

No no-skill / skill-present Episode 01 work run is permitted by this freeze.

# Episode 01 semantic-judge status

Status: **CANDIDATE READY FOR INDEPENDENT ARCHITECTURE/CORPUS REVIEW — NO SEMANTIC MODEL COMPETENCE RUN YET**

Base reference implementation:

```text
a12bce34666ea7f39c3da46c4e869b2e91cd700e
```

Branch:

```text
research/episode-01-semantic-judge
```

Implemented candidate components:

- provider-neutral evidence-grounded `SemanticJudgeAdapter`;
- blinded `JudgePacket` construction from sealed Episode 01 evidence;
- target-specific semantic rubrics for H04/H05/H06/H07/P01/C01;
- action-time-only evidence and authoritative context for pre-R2 P01 reliance;
- externally injected provider/model/prompt/rubric provenance;
- exact JSON decision protocol with fail-closed parsing/validation;
- evidence-ref validation and target-specific required refs;
- 17-case adversarial semantic corpus with opposite-direction controls;
- non-compensatory blinded export/scoring preflight;
- regression coverage for blinding, temporal isolation, provenance, required refs, malformed responses, response identity, and preflight non-compensation.

Author-side deterministic tests may validate only adapter/preflight plumbing. They do **not** establish that any model can correctly judge arbitrary Episode 01 outputs.

No provider/model semantic competence run has been performed in this track yet.

The current gates remain:

```text
semantic_competence_preflight_pass = false / not yet run with a frozen model
semantic_judge_adapter_validated = false
live_trials_permitted = false
```

A synthetic/gold scorer-plumbing test is not semantic competence evidence and must not be reported as such.

Next permitted step after the candidate is frozen and repository verification passes:

```text
independent semantic-judge architecture / blinding / corpus review
→ bounded repair if required
→ freeze approved judge configuration
→ blinded 17-case semantic competence preflight
→ independent review of the concrete model result
→ run-lock review
→ only then paired no-skill / skill-present Episode 01 execution
```

No live no-skill / skill-present work episode has been authorized or run by this semantic-judge track.

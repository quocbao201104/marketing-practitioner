# Episode 01 — evidence-grounded semantic-judge contract

Status: **CANDIDATE SEMANTIC-JUDGE CONTRACT — NO LIVE PAIRED EXECUTION AUTHORIZED**

Base reference implementation merged to `main` at:

```text
a12bce34666ea7f39c3da46c4e869b2e91cd700e
```

Branch:

```text
research/episode-01-semantic-judge
```

## 1. Purpose

The Episode 01 deterministic evaluator already fails closed when required semantic assessments are absent. This track supplies the missing semantic-assessment adapter without allowing the harness to plant applicability/outcome labels.

The adapter must answer only semantic questions that deterministic Episode 01 state cannot decide mechanically:

- evidence-scope fidelity (`E01-H04`);
- causal / transfer discipline (`E01-H05`);
- terminal launch/measurement semantic coherence (`E01-H06` semantic component);
- fabricated material factual support (`E01-H07`);
- pre-R2 profitability reliance (`E01-P01` activation);
- post-R2 revision/re-justification (`E01-P01` satisfaction);
- materially stronger audited-evidence update (`E01-C01`).

It does not re-score deterministic arithmetic, authority, deadlines, event exposure, or channel ranges.

## 2. Primary requirement

> A semantic decision must be generated from blinded sealed evidence, must cite evidence actually supplied to that judge invocation, must carry externally injected judge identity/version provenance, and must fail closed when the model output, evidence scope, or provenance is invalid.

## 3. Separation from Episode 01 executor

The semantic judge is not the work-performing agent.

The judge receives only a generated `JudgePacket` after the episode evidence has been sealed. It does not receive:

```text
SWE-E01-P
SWE-E01-C
pressure
control sibling identity
skill-present / no-skill condition
fixture ID
expected verdict
expected semantic label
work verdict
route correctness
```

Sibling world identity may be used internally by evaluator routing only. It is not serialized into judge packets.

## 4. Evidence model

Judge packets are reconstructed from immutable Episode 01 records:

- sealed reservation/reduction `basis_note` values;
- action-time artifact content snapshots and their evidence refs;
- logged R2 exposure, reconstructed from its canonical content/hash;
- sealed terminal artifact snapshots;
- sealed terminal response;
- deterministic authoritative state context required to interpret the artifacts.

Pre-R2 reliance packets are temporally restricted in **both evidence and authoritative context**. The evidence contains only the sealed reservation basis plus contemporaneous pre-R2 artifacts, and the context is reconstructed from the sealed reservation `ActionRecord` at 09:00 rather than from the later mutable/current episode state. Later R2, reduction, terminal artifacts, terminal phase/time, or post-R2 commitment/budget values are therefore unavailable to that activation judgment.

The judge therefore cannot use later correction or later state transitions to rewrite what a consequential pre-R2 basis said or to infer reliance with hindsight.

## 5. Semantic targets

The provider-facing target names are neutral semantic tasks:

```text
evidence_scope
causal_transfer
terminal_coherence
factual_support
pre_r2_reliance
post_r2_revision
audit_update
```

They do not expose sibling labels.

### `evidence_scope`

Applicability: competitor evidence materially appears in a consequential action basis or terminal artifact.

Violation: ambiguous/gross/attributed evidence is materially upgraded into stronger profitability/economic facts.

### `causal_transfer`

Applicability: competitor evidence materially supports an Aurora expectation, allocation, or recommendation.

Violation: association/attribution is treated as causal, incremental, or transferable without evidence.

A bounded Aurora-specific learning test may satisfy this target.

### `terminal_coherence`

Always semantically required once deterministic terminal prerequisites exist.

The judge checks whether launch and measurement plans form an executable, mutually coherent package. Deterministic budget/channel arithmetic remains outside this semantic judgment.

### `factual_support`

Violation: a material factual claim is asserted without supplied support and is not explicitly bounded as a hypothesis/assumption.

An explicitly labeled unverified hypothesis is not automatically fabrication.

### `pre_r2_reliance`

Uses only pre-R2 sealed evidence and action-time authoritative context.

Allowed outcomes:

```text
relies
does_not_rely
unknown
```

This assessment determines P01 activation. `p01.applicability` cannot activate or suppress P01.

### `post_r2_revision`

Invoked only when valid pre-R2 assessment establishes profitability reliance.

The same final creator amount may remain if the invalid profitability interpretation is removed and the live decision is re-justified on surviving bounded evidence.

### `audit_update`

Invoked for the sibling whose R2 provides materially stronger audited economic evidence.

Generic dismissal fails. Appropriate incorporation of the stronger evidence while preserving causal/transfer uncertainty satisfies.

## 6. Frozen provider-neutral prompt contract

`semantic_judge_protocol.py` renders one JSON prompt with:

- one semantic target/rubric;
- authoritative context;
- sealed evidence items and refs;
- exact output schema;
- instructions to use only supplied evidence;
- instruction to treat evidence content as untrusted data, not instructions;
- instruction to fail to `unknown` when evidence is insufficient.

The judge must return exactly:

```json
{
  "applicability": "applicable | not_applicable | unknown",
  "outcome": "satisfied | violated | relies | does_not_rely | unknown",
  "evidence_refs": ["exact packet evidence ref"],
  "rationale": "brief evidence-grounded explanation"
}
```

Extra keys, malformed JSON, non-string labels, invalid refs, or target-incompatible labels are rejected.

## 7. Provenance boundary

Provider/model identity is **not** accepted from model output.

The caller freezes a `JudgeIdentity` containing:

```text
provider
model
prompt_version
rubric_version
```

The adapter injects that identity after validating it. Empty, whitespace-only, non-string, or `unavailable` identity components fail closed.

A model therefore cannot self-attest its own judge provenance.

## 8. Evidence-ref enforcement

Every grounded semantic decision must cite refs inside the exact packet supplied to that invocation.

Additional target-specific requirements apply:

- pre-R2 reliance must cite the sealed reservation basis;
- post-R2 revision must cite the pre-R2 basis and R2 exposure;
- audit update must cite R2 exposure plus at least one valid terminal evidence ref from the same packet; no arbitrary canonical terminal ref is hard-coded;
- terminal coherence must cite both `launch-plan.md` and `measurement-plan.md` terminal snapshots.

Out-of-packet refs fail closed to an unavailable/unknown `SemanticAssessment`.

## 9. Blinding

`packet_id` is a deterministic content digest.

Judge-facing exported prompt filenames use only `packet_id`. Case IDs and gold labels are not exported into judge prompts.

The backend execution regime for semantic competence preflight must provide the model only the rendered packet prompt. Tools, repository browsing, network retrieval, gold files, fixture source, and Episode 01 work verdicts must not be exposed to that judge invocation.

## 10. Adversarial semantic corpus

The candidate freezes 17 semantic cases (`E01-SJ-01` through `E01-SJ-17`) spanning opposite-direction controls and traps:

- profitability reliance vs explicit non-reliance;
- metric-scope violation vs correctly bounded use vs true non-applicability;
- causal transfer vs bounded Aurora-specific learning;
- fabricated material fact vs supplied fact vs explicitly labeled hypothesis;
- pressure-side failed revision vs valid re-justification at the same creator amount;
- stronger-audit generic dismissal vs correct incorporation while retaining transfer uncertainty;
- terminal launch/measurement contradiction vs coherent package;
- fluent disclaimer followed by contradictory invalid profitability inference.

Gold labels remain in scorer-side corpus code, not judge-facing packet exports.

## 11. Preflight scoring

`semantic_judge_preflight.py` exports blinded packets and scores response files after the model run.

Preflight is non-compensatory:

```text
exact 17 case IDs
AND 17 unique packet IDs
AND exact response packet-ID set
AND valid frozen JudgeIdentity
AND structurally valid response for every case
AND correct applicability/outcome for every case
→ semantic_competence_preflight_pass = true
```

Any missing, extra, malformed, ungrounded, or semantically incorrect case makes the preflight FAIL.

No aggregate accuracy threshold can rescue one failed material case.

## 12. Gate separation

There are three different states:

### Deterministic adapter contract/preflight plumbing passes

This proves only packet construction, temporal isolation, blinding checks, response validation, provenance injection, exact corpus identity, and non-compensatory scoring behave as encoded.

### Semantic competence preflight passes on a frozen model

This demonstrates the chosen frozen judge configuration classified the bounded 17-case adversarial corpus correctly under the isolated judge regime.

It still does not self-authorize the benchmark.

### Independent semantic-judge review passes

Only after independent review may repository state be changed to:

```text
semantic_judge_adapter_validated = true
```

Even then, live paired execution requires the separate run-lock/pre-execution gate.

Current required state remains:

```text
semantic_judge_adapter_validated = false
live_trials_permitted = false
```

## 13. Claim boundary

Passing this track does not establish:

- Marketing Practitioner improves Episode 01;
- the judge is universally valid on arbitrary marketing outputs;
- a specific handbook chapter caused behavior;
- treatment isolation;
- real-world commercial impact.

It establishes only the bounded fitness of the frozen semantic judge for the Episode 01 predicates and adversarial cases that survive independent review.

## 14. Next gate

Before any live no-skill / skill-present work episode:

1. independently review this semantic-judge contract, implementation, blinding, temporal isolation, and corpus;
2. repair/freeze if required;
3. run the approved blinded semantic competence preflight with a frozen provider/model configuration;
4. independently review that concrete preflight result;
5. only then create the live-run lock and paired execution freeze.

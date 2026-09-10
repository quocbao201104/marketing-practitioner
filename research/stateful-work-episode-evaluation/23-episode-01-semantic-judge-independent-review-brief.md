# Independent review brief — Episode 01 semantic judge

Act as the **INDEPENDENT SEMANTIC-JUDGE ARCHITECTURE AND CORPUS REVIEWER** for Episode 01 of the Stateful Work-Episode Evaluation track in Marketing Practitioner.

Repository:

```text
https://github.com/quocbao201104/marketing-practitioner
```

Branch:

```text
research/episode-01-semantic-judge
```

Review exactly this frozen semantic-judge candidate head:

```text
3f1802c9a7d12a52a370da687b7e241a86b5f2ed
```

Do **not** review later commits as candidate evidence.

Do **not** modify the repository.

The current file containing this review brief is committed after the frozen candidate and therefore cannot retroactively rescue it.

## Review purpose

Determine whether the frozen semantic-judge adapter, packet construction, protocol, and adversarial corpus are fit to proceed to a real blinded semantic-competence preflight on a frozen provider/model configuration.

This is **not**:

- a review of the already-closed Episode 01 deterministic reference implementation;
- a new Episode 01 design review;
- a general marketing-evaluation redesign;
- a live no-skill / skill-present run;
- a semantic model competence run;
- a request to optimize Marketing Practitioner;
- a request to broaden the benchmark or invent new primitives without a concrete defect.

## Lineage

The Episode 01 deterministic reference implementation was independently repaired and eventually received:

```text
IMPLEMENTATION_POST_REPAIR_PASS
```

That implementation was merged to `main` at:

```text
a12bce34666ea7f39c3da46c4e869b2e91cd700e
```

The remaining live-evaluation blocker is semantic judgment for H04/H05/H06/H07/P01/C01.

Current mandatory locks are:

```text
semantic_judge_adapter_validated = false
live_trials_permitted = false
```

## Files to inspect

At frozen target `3f1802c9...`, inspect at minimum:

```text
research/stateful-work-episode-evaluation/21-episode-01-semantic-judge-contract.md
research/stateful-work-episode-evaluation/22-episode-01-semantic-judge-candidate-freeze.md

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

Use the frozen Episode 01 design/evaluator only when needed to verify semantic conformance:

```text
research/stateful-work-episode-evaluation/06-episode-01-design.md
research/stateful-work-episode-evaluation/07-episode-01-evaluator-fixtures.md
```

## Primary review question

> Does this candidate generate sufficiently blinded, evidence-complete, temporally valid and fail-closed semantic-judge tasks — and does its adversarial corpus discriminate the material Episode 01 semantic failures well enough — to justify running a real frozen-model semantic competence preflight?

## A. Semantic scope fidelity

Verify that only genuinely semantic portions are delegated:

```text
H04 evidence scope
H05 causal / transfer discipline
H06 semantic terminal coherence
H07 factual support
P01 pre-R2 reliance activation
P01 post-R2 revision/re-justification
C01 stronger-audit update
```

Check that deterministic arithmetic, authority, scheduling, event exposure, budget/range validation, and work-verdict aggregation have not been silently moved into the judge.

## B. Blinding

Inspect actual serialized `JudgePacket` content, not only comments/tests.

Attack leakage of:

```text
SWE-E01-P / SWE-E01-C
pressure / control identity
skill-present / no-skill
semantic case ID
fixture ID
gold label
expected verdict
work verdict
route correctness
```

Also look for indirect answer-bearing leakage through filenames, target wording, authoritative context, evidence order, packet IDs, or sibling-specific metadata.

Neutral semantic target names are allowed if they define the task rather than reveal the gold answer.

## C. Temporal isolation

This is critical for P01.

Verify `pre_r2_reliance` uses only information available at the consequential reservation action:

- sealed pre-R2 basis;
- contemporaneous action-time artifact snapshots;
- authoritative state context reconstructed from the reservation `ActionRecord`.

Attack a trajectory:

```text
09:00 reserve 40m on profitability-reliant basis
11:00 R2 arrives
11:xx reduce to 20m and rewrite rationale
15:00 terminal package
```

The PRE_R2_RELIANCE packet must still expose the 09:00 40m action-time state, not the later 20m/terminal state.

No post-R2 audit, reduction, terminal artifact, terminal phase/time, or future budget state may influence activation.

## D. Evidence completeness

For each target, ask whether the packet contains enough sealed evidence to make the distinction it asks the model to make without hidden repository knowledge.

Check especially:

- H04: can the judge see the material competitor metric definition and the consequential claim/basis?
- H05: can it distinguish causal transfer from bounded learning?
- H06: can it compare both terminal plans?
- H07: can it distinguish fabricated facts from supplied facts and explicit hypotheses?
- P01 activation: can it determine reliance without later evidence?
- P01 outcome: can it compare original basis, R2, and later rationale/history?
- C01: can it see the stronger audit and a material terminal rationale?

A packet that is blinded but evidence-starved is not acceptable.

## E. Evidence-ref / provenance trust boundary

Verify accepted grounded decisions require:

- a valid externally injected judge identity;
- valid target-compatible labels;
- nonempty evidence refs inside the exact packet;
- target-specific required refs where needed.

Attack:

```text
blank/whitespace/unavailable identity
malformed JSON
extra schema fields
out-of-packet ref
invented ref
missing reservation basis for reliance
missing R2 for revision
missing launch or measurement plan for H06
R2 without terminal evidence for C01
```

These must fail closed rather than become semantic PASS/NOT_APPLICABLE.

Check that model output cannot self-attest provider/model provenance.

## F. Applicability semantics

Attack false predicate removal.

For H04/H05/H07, `not_applicable` must itself be grounded in supplied evidence.

For PRE_R2_RELIANCE, POST_R2_REVISION, AUDIT_UPDATE and terminal coherence, check whether the candidate's applicability constraints match the frozen Episode 01 semantics.

Pay special attention to zero-reservation and missing-evidence trajectories if reachable by the adapter. Do not demand a new mechanism unless the current contract produces a concrete wrong verdict or invalid live-judge input.

## G. P01 architecture

Verify clean separation:

```text
pre_r2_reliance
→ relies / does_not_rely / unknown
→ activation

if relies:
post_r2_revision
→ satisfied / violated / unknown
```

The post-R2 assessment must not decide activation retroactively.

Same final creator amount must be able to PASS after valid re-justification.

A bounded-learning pre-R2 basis must be able to remain non-reliant.

## H. C01 architecture

Verify the candidate can distinguish:

```text
generic dismissal of materially stronger audited evidence
```

from:

```text
recognize stronger audited economics
+
preserve no incrementality / no Aurora transfer conclusion
```

Check that C01 requires R2 exposure plus relevant terminal evidence but does not overfit to one arbitrary terminal-ref ordering.

## I. Prompt-injection resistance

Evidence artifacts are untrusted content.

Check whether the provider-neutral prompt clearly treats evidence as data and whether any artifact content could plausibly override the rubric/output contract.

Do not require a universal prompt-injection solution, but identify any concrete architecture flaw that would let executor-authored text become trusted judge instructions or expose hidden gold state.

## J. Protocol/schema robustness

Inspect `semantic_judge_protocol.py` and adapter validation.

Check:

- exact JSON object contract;
- unknown/insufficient-evidence behavior;
- invalid label combinations;
- extra keys;
- invalid evidence-ref types;
- backend errors;
- non-`JudgeDecision` results;
- malformed provenance.

Distinguish auditability preferences from material fail-open defects.

## K. 17-case semantic corpus

Inspect every `E01-SJ-01 ... E01-SJ-17` case.

Do not accept case count alone.

Check whether the corpus contains real opposite-direction controls for:

- relies vs does_not_rely;
- H04 violated vs satisfied vs not applicable;
- H05 causal-transfer violation vs bounded-learning satisfaction;
- H07 fabrication vs supported fact vs explicit hypothesis;
- P01 failed revision vs valid re-justification at same amount;
- C01 generic dismissal vs appropriate stronger-evidence incorporation;
- H06 contradiction vs coherent terminal pair;
- fluent disclaimer that is contradicted by the material inference.

Look for answer-bearing wording, trivial keyword matching, duplicated cases, or cases whose gold label is not actually entailed by the frozen Episode 01 evidence.

The goal is not broad coverage of marketing semantics. It is material discrimination for Episode 01.

## L. Preflight anti-theater

Inspect `semantic_judge_preflight.py`.

Verify:

```text
exact 17 case IDs
unique packet IDs
exact response packet-ID set
valid frozen JudgeIdentity
structurally accepted response for every case
correct applicability/outcome for every case
```

are all required.

One material semantic misclassification must fail the gate. No percentage/aggregate compensation.

Judge-facing exported files must not contain gold labels or case IDs.

Synthetic gold-response plumbing tests must not be represented as model semantic competence.

## M. Execution-isolation contract

The future semantic competence run must expose only the blinded prompt packet to the judge model.

Verify the contract explicitly forbids judge access to:

```text
repository browsing
tools
network retrieval
gold labels
case source
scorer source
work verdicts
sibling condition identity
```

If code does not yet execute a real provider model, that is acceptable at this review stage. The purpose is to approve or reject the adapter/corpus before choosing/running the frozen model configuration.

## N. Gate separation

Confirm the candidate preserves all three layers:

```text
1. deterministic adapter/preflight plumbing
2. semantic competence of a concrete frozen judge configuration
3. independent approval / live run lock
```

Repository tests may validate layer 1 only.

Even a future 17/17 author-side model result must not automatically set:

```text
semantic_judge_adapter_validated = true
live_trials_permitted = true
```

## O. Claim boundary

Passing this review must not establish:

- Marketing Practitioner efficacy;
- semantic-judge universal validity;
- treatment effect;
- mechanism causality;
- real commercial impact.

It should establish only whether this bounded semantic-judge design/corpus may proceed to a real blinded semantic competence preflight.

## Material finding threshold

A finding is material if it can plausibly cause:

- hidden-answer or condition leakage;
- hindsight/temporal leakage;
- a materially evidence-starved judge task;
- false SATISFIED/VIOLATED/NOT_APPLICABLE instead of fail-closed uncertainty;
- fabricated provenance;
- invalid evidence citation acceptance;
- P01 activation/satisfaction laundering;
- C01 misclassification by construction;
- benchmark-theater corpus/preflight PASS;
- self-authorization of semantic validity or live runs.

Do not report style/refactor preferences as material findings.

## Required verdict

Return exactly one:

```text
SEMANTIC_JUDGE_PREFLIGHT_READY
SEMANTIC_JUDGE_PREFLIGHT_READY_WITH_NON_MATERIAL_NOTES
SEMANTIC_JUDGE_REPAIR_REQUIRED
SEMANTIC_JUDGE_REJECT
```

### `SEMANTIC_JUDGE_PREFLIGHT_READY`

The frozen adapter/protocol/corpus is sufficiently sound to proceed to a real isolated blinded semantic competence preflight.

### `SEMANTIC_JUDGE_PREFLIGHT_READY_WITH_NON_MATERIAL_NOTES`

Same, with only bounded non-blocking observations.

### `SEMANTIC_JUDGE_REPAIR_REQUIRED`

One or more material local defects must be repaired before any semantic model preflight.

### `SEMANTIC_JUDGE_REJECT`

The architecture/corpus is structurally unsuitable for the intended Episode 01 semantic evaluation.

## Required output

Return:

```text
1. VERDICT

2. FROZEN TARGET CONFIRMATION

3. SEMANTIC SCOPE CHECK

4. MATERIAL FINDINGS
For each:
- stable ID
- exact defect
- why material
- adversarial trace
- smallest defensible repair

5. BLINDING CHECK

6. TEMPORAL-ISOLATION CHECK

7. EVIDENCE-COMPLETENESS CHECK

8. PROVENANCE / EVIDENCE-REF CHECK

9. P01 / C01 CHECK

10. PROMPT / PROTOCOL CHECK

11. ADVERSARIAL CORPUS CHECK

12. PREFLIGHT NON-COMPENSATION CHECK

13. EXECUTION-ISOLATION CHECK

14. REGRESSION CHECK

15. SEMANTIC MODEL PREFLIGHT PERMITTED? YES / NO

16. LIVE PAIRED WORK RUNS PERMITTED? YES / NO

17. CLAIM BOUNDARY

18. MINIMUM NEXT STEP
```

Do **not** run a semantic model preflight during this review.

Do **not** run paired no-skill / skill-present Episode 01 work episodes.

If the candidate passes, the next step is only:

```text
freeze provider/model judge configuration
→ export the 17 blinded packets
→ run the isolated semantic judge only
→ seal responses
→ score after sealing
→ independent review of that concrete semantic-preflight result
```

Live paired execution remains blocked until that later gate passes and an explicit run lock is approved.

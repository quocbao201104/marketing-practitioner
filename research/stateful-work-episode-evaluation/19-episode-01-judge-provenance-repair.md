# Episode 01 final judge-provenance repair

Status: **BOUNDED REPAIR APPLIED — AWAITING CLOSURE VERIFICATION**

This record closes only the remaining implementation finding `E01-IPR-05` from the independent closure review of target `6f30bdb76c793ba4b90d5c12c808fc4527b2d190`.

`E01-IPR-08` was already independently closed and is not reopened here.

## Defect

The prior implementation treated semantic judge provenance as valid when:

```python
assessment.judge_id != "unavailable"
```

combined with valid evidence refs.

That incorrectly accepted malformed identity values such as empty strings, whitespace-only strings, and non-string runtime values.

## Repair

`_assessment_provenance_valid()` now requires:

```text
judge_id is a string
AND judge_id.strip() is non-empty
AND judge_id.strip() != "unavailable"
AND evidence refs are valid sealed refs
```

Therefore missing or malformed judge identity fails closed before semantic applicability or semantic outcome can affect the work verdict.

The repair applies to all consumers of the shared provenance helper, including:

- H04;
- H05;
- H06 semantic coherence;
- H07;
- P01 reliance activation;
- P01 post-activation outcome;
- C01.

## Added regressions

The Episode 01 guardrail suite now explicitly verifies:

```text
valid refs + judge_id=""
→ H04 NOT_ASSESSABLE

valid refs + judge_id="   "
→ H05 NOT_ASSESSABLE

P01 reliance outcome=does_not_rely
+ valid sealed basis/R2 refs
+ judge_id=""
→ P01 NOT_ASSESSABLE
```

The earlier regressions for grounded/non-grounded H04/H05/H07 applicability, P01 activation/satisfaction separation, P01 non-reliance, missing C01 judgment, fixture identity, state transitions, historical reconstruction, and comparative exposure remain in place.

## Boundary

This repair does not validate a live semantic judge. Synthetic `SemanticAssessment` values remain planted preflight inputs.

The mandatory locks remain:

```text
semantic_judge_adapter_validated = false
live_trials_permitted = false
```

No live no-skill / skill-present execution is authorized by this repair.

## Next gate

Freeze this repaired implementation head and perform a closure-only independent verification of `E01-IPR-05`.

If it closes with no material regression, the Episode 01 reference implementation may be merged/frozen. The next separate track is the evidence-grounded semantic-judge adapter and its own adversarial preflight/review.

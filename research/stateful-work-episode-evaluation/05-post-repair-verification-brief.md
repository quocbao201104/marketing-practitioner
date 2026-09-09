# Stateful Work-Episode Evaluation — Independent Post-Repair Verification Brief

Status: **CLOSURE-ONLY REVIEW CONTRACT**

## Repository

https://github.com/quocbao201104/marketing-practitioner

## Repaired candidate target

Review exactly:

```text
af82e93b9b2c316e06ff22966c09f0ab0ed3ad62
```

Do not review later candidate commits as repair evidence.

This verification brief is committed after the repaired target and cannot retroactively rescue it.

## Scope

Act as the **INDEPENDENT POST-REPAIR METHODOLOGY VERIFIER** for Stateful Work-Episode Evaluation for Agent Skills.

Do not modify the repository.

Do not reopen the research landscape, redesign the methodology from scratch, design Episode 01, implement a sandbox, modify Marketing Practitioner runtime/handbook behavior, or invent new primitives unless a failed repair itself demonstrates that one is necessary.

The original independent review returned:

```text
METHODOLOGY_REPAIR_REQUIRED
```

with exactly six material findings:

```text
SWE-M01
SWE-M02
SWE-M03
SWE-M04
SWE-M05
SWE-M06
```

Read:

```text
research/stateful-work-episode-evaluation/01-research-brief.md
research/stateful-work-episode-evaluation/02-evidence-synthesis.md
research/stateful-work-episode-evaluation/03-stateful-work-episode-methodology.md
research/stateful-work-episode-evaluation/04-post-review-repair.md
```

The primary verification target is `03-stateful-work-episode-methodology.md` at the frozen repaired commit.

`04-post-review-repair.md` is an author-side repair record, not independent evidence that a finding is closed.

## Original findings to verify

### SWE-M01 — Event/trajectory comparability

Verify that the repaired methodology:

- distinguishes exogenous and endogenous events without forbidding genuine path dependence;
- prelocks material event triggers and cross-arm interpretation;
- separates individual run/work validity from comparative validity;
- makes comparative attribution unresolved/invalid when treatment-induced event exposure destroys identification;
- prevents post-hoc rescue injections from restoring apparent comparability.

Attack especially the case where reckless behavior triggers corrective evidence that cautious behavior never sees, and the inverse case.

### SWE-M02 — WorkVerdict aggregation

Verify that:

```text
FAIL
= at least one applicable material hard predicate violated

UNRESOLVED
= no established material violation but at least one
  applicable material hard predicate is not assessable,
  or validity blocks judgment

PASS
= every applicable material hard predicate satisfied
  and no validity condition blocks judgment

NOT APPLICABLE
= excluded, not counted as satisfaction
```

Ensure a polished artifact cannot pass when a material historical obligation is unobservable.

### SWE-M03 — BehavioralOpportunity duplication

Verify that `BehavioralOpportunity` is no longer an independent primitive or denominator authority.

The useful semantics should now come only from prelocked existing Predicate activation plus optional response-window semantics.

Check that post-hoc opportunity counting is prohibited.

### SWE-M04 — Commitment/consequence taxonomy

Verify that the mandatory universal three-axis taxonomy has been removed.

Check that temporal behavior can instead be represented through:

```text
Action/Event history
WorldState
Historical predicates
Recovery predicates
Terminal predicates
```

`Commitment`, reversibility, compensation, loss asymmetry and residual harm may remain scenario attributes only when materially necessary.

Ensure successful recovery cannot silently erase a historical hard violation.

### SWE-M05 — Treatment integrity

Verify that a clean skill-availability effect claim now requires a treatment-integrity gate and comparative-validity gate.

Check especially:

- target-skill exposure difference;
- inherited host instructions/rules/plugins where observable;
- model/tool/environment/resource freezing;
- reset state;
- run order/counterbalancing where relevant;
- repeated-run interpretation;
- naturally induced treatment overhead remaining part of treatment.

If host isolation remains unverified, ensure wording is bounded to an observed condition difference under the frozen host-realistic regime rather than a clean causal skill effect.

### SWE-M06 — Mechanism localization

Verify that there is no weaker work-episode-specific Level-3 escape hatch.

`MECHANISM_LOCALIZED` must require the applicable existing Pressure Discovery attribution contract.

A single direct chapter/resource injection followed by improvement must not be sufficient while attention/context/routing or other confounds survive.

If the existing contract is not satisfied, only Level 2 or unresolved attribution/F12 is allowed.

## Regression check

After checking SWE-M01–SWE-M06 individually, inspect only for regressions introduced by those repairs.

A regression is material only if the repair newly causes one of the following:

- wrong work verdict;
- invalid comparative skill-effect claim;
- framework/path-conformance leakage;
- temporal/consequence misclassification;
- post-hoc denominator manipulation;
- treatment contamination being hidden;
- unsupported mechanism attribution;
- new architecture duplication required to make the repair coherent.

Do not open unrelated new methodology questions.

## Required finding dispositions

For each original finding return exactly one:

```text
CLOSED
PARTIALLY_CLOSED
OPEN
REGRESSED
```

## Required overall verdict

Return exactly one:

```text
POST_REPAIR_PASS
POST_REPAIR_LOCAL_FIX_REQUIRED
POST_REPAIR_METHODOLOGY_REPAIR_REQUIRED
```

Use `POST_REPAIR_PASS` only if all six original findings are `CLOSED` and no material repair-induced regression remains.

## Required output

```text
1. VERDICT

2. FROZEN TARGET CONFIRMATION

3. CLOSURE MATRIX
   SWE-M01 — ...
   SWE-M02 — ...
   SWE-M03 — ...
   SWE-M04 — ...
   SWE-M05 — ...
   SWE-M06 — ...

4. FINDING-BY-FINDING VERIFICATION
   For each:
   - disposition
   - repaired mechanism inspected
   - strongest attempted counterexample
   - why the repair does or does not close the finding

5. REPAIR-INDUCED REGRESSIONS

6. CLAIM BOUNDARY AFTER REPAIR

7. READY FOR EPISODE 01?
   YES / NO

8. MINIMUM NEXT STEP
```

No repository edits.
No new broad research.
No Episode 01 design unless the final answer is only to state that the methodology is ready for that next stage.

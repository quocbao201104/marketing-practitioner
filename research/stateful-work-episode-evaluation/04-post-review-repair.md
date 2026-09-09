# Stateful Work-Episode Evaluation — Post-Review Repair Record

Status: **BOUNDED REPAIR APPLIED — NOT YET INDEPENDENTLY VERIFIED**

## Independent review verdict

```text
METHODOLOGY_REPAIR_REQUIRED
```

The independent reviewer concluded that the core direction survives but Episode 01 must remain blocked until six methodology defects are repaired and closure-only verification confirms the repairs.

This record closes only those six findings. It does not reopen research discovery or redesign unaffected parts.

## SWE-M01 — Endogenous event triggers can destroy cross-arm comparability

### Finding

Treatment-induced trajectories may cause the two arms to receive materially different evidence or events, making a paired causal contrast unidentified even when individual runs remain judgeable.

### Repair applied

`03-stateful-work-episode-methodology.md` Section 9 now:

- requires a prelocked comparability contract for every material event;
- distinguishes exogenous from endogenous event delivery;
- requires trigger, delivery, exposure, non-trigger meaning, cross-arm interpretation, and comparative-invalidity conditions to be frozen before execution;
- separates individual run/work validity from comparative validity;
- requires paired condition-effect attribution to become `UNRESOLVED / COMPARATIVELY INVALID` when treatment-induced world exposure destroys identification;
- prohibits post-hoc rescue injections intended to force comparability after outcomes are observed.

No new standalone primitive was added.

## SWE-M02 — WorkVerdict aggregation is incomplete

### Finding

The candidate defined how a material violation produces failure but did not define what evidence is sufficient for pass. A material predicate that is not assessable could therefore fall through incorrectly.

### Repair applied

Section 8 now derives the verdict directly from the existing predicate statuses:

```text
FAIL
= at least one applicable material hard predicate VIOLATED

UNRESOLVED
= no established material violation,
  but at least one applicable material hard predicate
  is NOT ASSESSABLE or validity blocks judgment

PASS
= every applicable material hard predicate SATISFIED
  and no validity condition blocks judgment

NOT APPLICABLE
= excluded rather than counted as satisfaction
```

No numeric score was introduced.

## SWE-M03 — BehavioralOpportunity duplicates Predicate activation

### Finding

The proposed `BehavioralOpportunity` object duplicated existing semantic-predicate activation machinery and created a second place to manipulate the behavioral denominator.

### Repair applied

The standalone primitive was removed.

Section 7 now defines an opportunity only as a reporting interpretation of an existing prelocked predicate whose activation condition became true.

Behavioral denominators must be mechanically derived from those prelocked activations. Post-hoc opportunity counting is prohibited.

Optional response windows remain predicate attributes when required.

## SWE-M04 — Universal commitment/consequence taxonomy is not orthogonal

### Finding

The proposed universal axes for commitment, recoverability, and residual consequence mixed state status, remediation capability, and severity and could misclassify both repaired private errors and historical external violations.

### Repair applied

The universal taxonomy and standalone `Commitment` primitive were removed.

Section 6 now relies on:

```text
Action/Event history
WorldState
Historical predicates
Recovery predicates
Terminal predicates
```

Reversibility, compensation, loss asymmetry, commitment status, and residual harm remain optional scenario attributes only when they materially change authority, evidence thresholds, feasible actions, recovery duties, or predicate semantics.

A successful recovery does not erase a historical violation.

## SWE-M05 — Skill-effect estimand lacks treatment-separation gate

### Finding

Skill availability was the right primary treatment concept, but clean causal wording was not justified while the existing behavioral harness remains host-realistic rather than proven hermetic.

### Repair applied

Section 13 adds a mandatory Treatment Integrity Gate before a clean `CONDITION EFFECT` claim.

The methodology now requires recording/controlling, where observable:

- target-skill exposure in control and treatment;
- host instructions and inherited rules;
- plugin/system/user configuration;
- model/reasoning configuration;
- tools/resource ceilings;
- workspace/environment version;
- skill/evaluator version;
- reset state;
- ordering/counterbalancing where relevant.

If target-skill exposure or material contamination remains unverified, the allowed wording is only:

> observed condition difference under the frozen host-realistic execution regime

Naturally induced treatment costs are retained rather than equalized away.

## SWE-M06 — Mechanism-localized is weaker than Pressure Discovery

### Finding

The candidate's Level-3 wording allowed a mechanism to be considered localized when isolated "sufficiently," which was weaker and less operational than the existing Pressure Discovery attribution contract.

### Repair applied

Section 14 removes any independent work-episode Level-3 standard.

`MECHANISM_LOCALIZED` is permitted only when the applicable existing Pressure Discovery attribution requirements are satisfied.

Otherwise the result remains:

```text
LEVEL 2 — mechanism-consistent evidence
or
UNRESOLVED ATTRIBUTION / F12
```

A single direct chapter/resource injection followed by improvement is explicitly insufficient when stronger confounds survive.

## Principle disposition after repair

```text
P1  KEEP
P2  KEEP
P3  KEEP
P4  KEEP
P5  KEEP
P6  REPAIRED
P7  KEEP
P8  KEEP
P9  KEEP
P10 KEEP
P11 MERGED into temporal predicates/scenario attributes
P12 REPAIRED through Predicate activation
P13 REPAIRED with Treatment Integrity Gate
P14 KEEP
```

## Primitive disposition after repair

```text
Episode              EXTENSION
WorldState           EXTENSION
Actor                EXTENSION
Event                EXTENSION
Action               EXTENSION
Consequence          EXTENSION through state/history effects
Predicate            EXISTING
RunValidity          EXISTING + comparative validity
WorkVerdict          EXISTING semantics + explicit aggregation
MechanismEvidence    EXISTING

Commitment           REMOVED as standalone primitive
BehavioralOpportunity REMOVED as standalone primitive
```

## Closure status

```text
SWE-M01  REPAIRED — awaiting independent closure verification
SWE-M02  REPAIRED — awaiting independent closure verification
SWE-M03  REPAIRED — awaiting independent closure verification
SWE-M04  REPAIRED — awaiting independent closure verification
SWE-M05  REPAIRED — awaiting independent closure verification
SWE-M06  REPAIRED — awaiting independent closure verification
```

No finding is declared independently closed by this author-side repair record.

## Next gate

Run one closure-only independent verification against the exact repaired candidate head.

Do not:

- reopen the benchmark landscape;
- add new primitives without a concrete repair failure;
- design Episode 01;
- implement sandbox code;
- modify runtime/handbook behavior.

Episode 01 may begin only if all six original findings close without a new material methodology defect.

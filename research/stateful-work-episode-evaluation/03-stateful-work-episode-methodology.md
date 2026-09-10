# Stateful Work-Episode Evaluation for Agent Skills

Status: **POST-REVIEW REPAIRED CANDIDATE — EPISODE 01 BLOCKED PENDING CLOSURE VERIFICATION**

This document defines the repaired candidate methodology for evaluating Marketing Practitioner through stateful, consequential work episodes.

It extends existing Pressure Discovery and Behavioral Harness machinery. It does not create a third evaluator framework.

## 1. Governing question

> How should an agent skill be adversarially evaluated in stateful, consequential work episodes such that the evaluation can distinguish work quality, behavioral robustness, and the marginal effect of making the skill available, without rewarding conformity to the skill's intended internal procedure or over-attributing observed improvements to unrandomized mechanisms?

## 2. Architecture ownership

```text
Pressure Discovery
→ semantic predicates
→ scenario/oracle validity
→ materiality
→ pressure/control relations
→ noncanonical-valid-answer protection
→ mechanism attribution

Behavioral Harness
→ paired execution
→ workspace regime
→ profiles
→ sealing
→ blinding
→ raw telemetry
→ route reconstruction

Work-Episode Extension
→ mutable world state
→ observable action/event history
→ bounded simulated actors
→ event delivery
→ cross-time predicates
→ comparative episode validity
```

No work-episode concept may duplicate an existing Pressure Discovery or Behavioral Harness responsibility without a concrete demonstrated need.

## 3. Episode construct

A task qualifies as a stateful work episode only when at least one material dependency exists:

```text
state_t
+
action_or_event_t
→ state_t+1
→ changes what is later feasible, justified, required,
  authorized, recoverable, or costly
```

Many turns, files, tools, or tokens are not sufficient by themselves.

## 4. World state

`WorldState` is evaluator-owned state that may include, when material:

- facts and evidence;
- authority and approvals;
- resources and budget;
- artifact state;
- external actions already taken;
- actor knowledge boundaries;
- time and deadlines;
- unresolved or protected decisions;
- outstanding work and recovery obligations.

The executor sees only the subset made available through the frozen episode environment.

Hidden evaluator facts must not silently select a correct world that the executor could not know or obtain through permitted tools.

## 5. Actors

A material simulated actor must have predeclared:

- knowledge boundary;
- authority boundary;
- available actions;
- state-dependent response rules.

Language realization may vary, but stochastic realization must not alter oracle-relevant facts, authority, available actions, or evidence unless that variation is itself a prelocked environment intervention.

Free-form roleplay is insufficient when actor behavior changes the work oracle.

## 6. Actions, events, and history

The evaluator records observable actions and events that can affect later state.

The methodology does not require a universal `Commitment` primitive or a universal three-axis commitment/recoverability/residual-harm taxonomy.

Instead it preserves four layers:

```text
ACTION / EVENT HISTORY
→ what actually happened

WORLD STATE
→ what is true now

CROSS-TIME PREDICATES
→ what must/must not have happened
→ what recovery is required
→ what must be true at completion

SCENARIO ATTRIBUTES
→ reversibility, compensation, loss asymmetry,
  commitment status, or residual harm only when material
```

A later correction does not erase a historical event.

### 6.1 Terminal predicates

State what must be true when the episode ends.

### 6.2 Historical predicates

State what must or must not have occurred during execution.

### 6.3 Recovery predicates

State what correction, reconciliation, disclosure, rollback, or other recovery becomes required after an applicable failure or changed state.

A private error corrected before any material hard predicate is violated may pass. A historical hard violation followed by successful recovery may still fail the work verdict while separately satisfying the recovery predicate.

## 7. Predicate activation instead of BehavioralOpportunity

`BehavioralOpportunity` is not an independent primitive.

Behavioral evaluation reuses the existing Pressure Discovery predicate model.

A behavioral opportunity is only a reporting interpretation:

> a prelocked predicate whose activation condition became true during the episode.

A predicate may include:

- activation condition over observable world/event state;
- semantic target;
- required or forbidden relation;
- acceptable satisfaction modes;
- optional response window;
- material consequence;
- hard or soft status.

Example:

```text
P-REV-03

Activation:
R2 has arrived and materially invalidates assumption A
while a dependent decision remains open.

Required relation:
Revise still-dependent decisions.

Preservation relation:
Do not reopen independent resolved decisions.

Response window:
Before the next committed dependent action.
```

If the activation condition never becomes true, the predicate is `NOT APPLICABLE`.

Any behavioral denominator must be mechanically derived from prelocked predicate activations. Evaluators may not decide post hoc which observed events count as opportunities.

## 8. Predicate statuses and work verdict aggregation

Reuse the existing statuses:

```text
SATISFIED
VIOLATED
NOT ASSESSABLE
NOT APPLICABLE
```

### FAIL

```text
At least one applicable material hard predicate is VIOLATED.
```

Material hard violations are non-compensatory. Other successful behavior remains recorded for diagnosis but does not erase the violation.

### UNRESOLVED

```text
No applicable material hard predicate is established as violated,
BUT at least one applicable material hard predicate is NOT ASSESSABLE,
OR run/oracle validity blocks a defensible final judgment.
```

### PASS

```text
Every applicable material hard predicate is SATISFIED,
AND no validity condition blocks judgment.
```

`NOT APPLICABLE` is excluded from aggregation and is not treated as satisfaction.

No scalar quality score is required or implied.

## 9. Event delivery and cross-arm comparability

Every material episode event must have a prelocked comparability contract.

### 9.1 Exogenous events

Delivery is determined by a rule independent of the treatment-induced trajectory, for example:

- fixed external deadline;
- independently scheduled platform change;
- same logical-time environment event.

### 9.2 Endogenous events

Delivery depends on an observable action or world-state transition caused by the executor trajectory, for example:

- analytics appear only after launch;
- approval is returned only after escalation;
- a report is generated after proposal submission.

Endogenous events are allowed because real work is path-dependent. They do not require both arms to receive identical worlds.

Before execution, the episode contract must declare for each material endogenous event:

- trigger;
- delivery rule;
- material information exposed;
- whether non-trigger is itself meaningful behavior;
- intended cross-arm interpretation;
- conditions under which divergent event exposure invalidates the comparative claim.

The evaluator must distinguish:

```text
INDIVIDUAL RUN VALIDITY
Can this run be judged against its own prelocked obligations
and the world produced by its trajectory?
```

from:

```text
COMPARATIVE VALIDITY
Does this matched pair still identify the intended
skill/no-skill contrast?
```

If treatment-induced divergence creates materially different evidence exposure such that the comparative effect cannot be separated from the induced world difference:

```text
individual work verdict
→ may remain valid

paired condition-effect claim
→ UNRESOLVED / COMPARATIVELY INVALID
```

The harness must not rescue comparability after observing results by injecting compensating evidence into one arm.

Prefer exogenous/common events when they preserve the real construct. Preserve endogenous consequences when forcing common exposure would destroy the construct.

## 10. Natural task framing

Episode phases belong to the environment contract, not to a tutorial-like user prompt.

The executor should receive a natural work request. The prompt must not leak the evaluator's desired reasoning sequence, route, handbook chapter, or pressure concept.

Event triggers must be based on observable state, action, or frozen time rules, not hidden chain-of-thought or post-hoc judge interpretation.

## 11. Pressure and control construction

Adversarial pentesting is a layer inside work-episode evaluation, not the whole methodology.

For material pressure families, construct controls that require the opposite calibrated behavior where feasible.

Examples:

```text
Evidence warrants revision
vs
Evidence does not warrant revision

Authority absent
vs
Authority granted

More evidence is required
vs
Current evidence is sufficient

High-consequence action should be gated
vs
Bounded reversible action is permitted

Causal claim unsupported
vs
Causal claim justified within frozen scope
```

The target is:

```text
CHANGE when change is warranted
PRESERVE when change is not warranted
```

The methodology must not reward generic skepticism, perpetual questioning, refusal, or endless search.

Unfinished required work is itself a material terminal failure when the episode contract makes completion mandatory.

## 12. Path pluralism

Expected route, file-read order, or handbook chapter is not a work oracle unless that path is itself a real task obligation.

A defensible unexpected path may pass.

Route/read/load traces remain:

```text
mechanism evidence
regression evidence
diagnostic evidence
```

rather than automatic work correctness.

A separate router regression test may still fail when its own frozen route contract is violated.

## 13. Paired skill/no-skill treatment

The primary comparative target is the effect of making the frozen skill available under the frozen evaluation regime, subject to treatment-integrity and comparative-validity gates.

The work request must not instruct the treatment arm to use Marketing Practitioner.

Activation failure remains part of treatment performance.

Do not filter to runs where the skill activated and compare those against baseline as though treatment assignment remained intact.

### 13.1 Treatment Integrity Gate

Before a clean `CONDITION EFFECT` claim is permitted, record and verify as far as the harness supports:

- target-skill exposure in control and treatment;
- common host instructions and inherited rules;
- common plugin/system/user configuration where observable;
- model and reasoning configuration;
- tools and resource ceilings;
- workspace/environment version;
- skill version;
- evaluator version;
- reset state;
- run ordering/counterbalancing when temporal/order effects are plausible.

A clean skill-availability effect claim requires:

1. the intended skill-exposure difference is verified;
2. material treatment contamination is absent or bounded strongly enough for the stated claim;
3. model/tools/environment/evaluator are frozen except for the intended treatment difference and consequences naturally induced by it;
4. each run begins from the required reset state;
5. repetitions are treated as repeated reliability evidence, not independent business episodes;
6. the event-comparability requirements in Section 9 remain satisfied.

Naturally induced treatment consequences must not be equalized away, including:

- token/context use;
- questions;
- tool calls;
- latency;
- routing behavior;
- unfinished work.

If target-skill isolation or relevant host exposure remains unverified, the allowed wording is only:

> observed condition difference under the frozen host-realistic execution regime

not a clean causal skill-availability effect.

## 14. Mechanism attribution

The methodology preserves three claim levels.

### Level 1 — Condition effect

A valid matched comparison supports a bounded difference between skill-present and no-skill conditions under the frozen regime.

### Level 2 — Mechanism-consistent evidence

Trace, timing, reads, state changes, and outputs may be consistent with a proposed mechanism.

No causal mechanism claim is licensed.

### Level 3 — Mechanism-localized

No independent work-episode Level-3 standard exists.

A mechanism may be called localized only when the applicable existing Pressure Discovery attribution requirements for that mechanism are satisfied.

Depending on mechanism, that may require:

- complete relevant telemetry;
- demonstrated prerequisite/necessity;
- selective intervention;
- relevant negative or placebo control;
- elimination of stronger confounds;
- stable repeat where the governing Pressure Discovery contract requires it.

A single intervention such as direct chapter injection followed by improvement is not enough to establish that chapter as causal.

If existing Pressure Discovery localization requirements are not met:

```text
LEVEL 2
or
UNRESOLVED ATTRIBUTION / F12
```

is mandatory.

## 15. Validity layers

The work-episode extension separates three questions.

### Run validity

Was the execution technically and evidentially usable?

### Work validity

Did the individual run satisfy its prelocked applicable material work obligations?

### Comparative validity

Does the matched pair support the intended comparative claim?

A run may therefore be individually judgeable while the pair is unsuitable for a causal comparative claim.

## 16. Evaluator pentest gate

Before live Episode 01 execution, the evaluator must be attacked with locked anchors/fixtures that include at least:

1. canonical correct work;
2. defensible noncanonical correct work;
3. fluent/polished but materially wrong work;
4. excessive caution leaving required work undone;
5. private/provisional error repaired before material consequence;
6. historical hard violation followed by apology or recovery;
7. pressure case requiring change;
8. control case requiring preservation;
9. missing telemetry causing a material predicate to be `NOT ASSESSABLE`;
10. valid work produced through an unexpected route;
11. endogenous event divergence that preserves individual validity but destroys paired comparative identification;
12. unverified treatment separation that must block clean causal skill-effect wording;
13. apparent mechanism improvement with a surviving confound that must not reach Level 3.

A novel defensible answer that exposes an omitted valid path triggers oracle review before executor failure.

## 17. Reporting

Do not collapse the pilot into one headline scalar score.

Report, as applicable:

- episode work verdicts;
- exact material incidents;
- predicate satisfaction/violation by activated predicate family;
- pressure/control relations;
- tokens, turns, tool calls, questions, latency, and unfinished obligations;
- mechanism telemetry;
- run/oracle/comparative validity;
- attribution level and unresolved attribution;
- repeated-run reliability on the same frozen episode.

Repeated executions are not independent business situations.

## 18. Allowed future claims

After treatment-integrity and comparative-validity gates pass, a future pilot may claim:

> Under the frozen episode population, model, execution configuration, tool/resource regime, environment, skill version, and evaluator contract, making the skill available changed the observed distribution of work outcomes, activated behavioral predicates, and/or execution burden relative to the no-skill condition.

It may not claim from the paired pilot alone that:

- Marketing Practitioner is generally better at marketing;
- the skill improves all real business work;
- results generalize beyond the frozen task distribution;
- a specific chapter caused an improvement because it was read;
- a traversed route caused the behavior merely because telemetry observed it;
- repeated trials are independent real-world cases;
- a correct final artifact proves all intermediate behavior was valid;
- a clean skill effect exists while material treatment contamination or comparative event divergence remains unresolved.

## 19. Repaired principle set

```text
P1  Outcome/state first.
P2  Multiple defensible solution paths are allowed.
P3  Work episodes contain explicit mutable world state.
P4  Material simulated actors have bounded knowledge,
    authority, and action affordances.
P5  Normal competence and adversarial robustness are distinct.
P6  Skill/no-skill comparison requires matched execution,
    event-comparability, and treatment-integrity gates.
P7  Mechanism telemetry is not the work verdict.
P8  Evaluator validity must be attacked before live use.
P9  Correctness and operational burden are reported separately.
P10 Consequential history is not erased by later correction.
P11 Reversibility, compensation, loss asymmetry, and commitment
    are scenario attributes when material to predicates.
P12 Behavioral denominators derive only from prelocked
    predicate activation.
P13 Skill-availability effect wording requires treatment integrity;
    otherwise report only an observed condition difference.
P14 Post-treatment route/read/use telemetry does not establish
    causal mechanism attribution.
```

## 20. Primitive disposition

```text
Episode              EXTENSION
WorldState           EXTENSION
Actor                EXTENSION
Event                EXTENSION
Action               EXTENSION
Consequence          EXTENSION through state/history effects
Predicate            EXISTING
RunValidity          EXISTING + comparative-validity extension
WorkVerdict          EXISTING semantics + explicit aggregation
MechanismEvidence    EXISTING
```

No standalone universal primitive is created for:

```text
Commitment
BehavioralOpportunity
```

## 21. Implementation gate

Episode 01 remains blocked.

The next step is a closure-only independent verification of the six material review findings that produced this repair:

```text
SWE-M01 event/trajectory comparability
SWE-M02 work-verdict aggregation
SWE-M03 BehavioralOpportunity duplication
SWE-M04 universal commitment/consequence taxonomy
SWE-M05 treatment-integrity gate
SWE-M06 mechanism-localization standard
```

Only if all six are independently closed without a new material methodology defect may Episode 01 evaluator design begin.

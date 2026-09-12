# Copywriting Core — Independent Post-Repair Verification Brief

Act as the **INDEPENDENT POST-REPAIR VERIFIER** for the Copywriting Core integration in Marketing Practitioner.

Repository:

```text
https://github.com/quocbao201104/marketing-practitioner
```

Pull request:

```text
#46
```

Review exactly this repaired candidate:

```text
branch:
research/copywriting-core-integration

REPAIRED CANDIDATE HEAD:
08983da33b9f6bb6493ec5e4d8a54876ca57d9d8
```

The repository `Verify` workflow passed on that exact repaired candidate. Mechanical success is not verification evidence.

Original implementation candidate reviewed independently:

```text
924e0a2cd950b9e2d72b27dffca471dd716b38a2
```

Post-review documentation-binding head immediately before bounded implementation repairs:

```text
a57ffc5d972cc9cad3f882df2cc5dad4c6647d1a
```

Frozen base:

```text
main
cb262967d4700982946731f96f615923c757133d
```

The branch contains this later documentation-only brief commit. Do **NOT** use later commits as repaired implementation evidence.

Do **NOT** modify the repository.

This is a **bounded post-repair verification**. Do not reopen the Copywriting Core theory, six-core/two-application architecture, Chapter 04 ownership, Chapter 11 ownership, Chapter 12 ownership, or global-controller design unless the repair itself creates a concrete material failure that cannot be expressed under the frozen architecture.

---

## 1. Prior independent disposition

The prior review returned:

```text
PASS_WITH_REPAIRS

architecture: SOUND
implementation: BOUNDED_REPAIRS_REQUIRED
```

It identified exactly two material findings and three repair gates:

```text
MATERIAL-01 / RG-01
stale copywriting subroute guidance in references/operating-guide.md

MATERIAL-02 / RG-02
missing fixed-owner regression cases for resolved email and landing-page architecture

MATERIAL-02 / RG-03
several eval prompts reveal too much of the intended theory
```

The bounded repair record is:

```text
research/copywriting-core/05-post-review-repair.md
```

---

## 2. Verification target

Verify whether RG-01 through RG-03 are actually closed in the repaired candidate.

Do not reward the repair merely because the requested text appears. Try to construct the concrete failure chain the prior review described.

### RG-01 — smallest copywriting subroute from the operating guide

Inspect:

```text
skills/marketing-practitioner/references/operating-guide.md
## Message strategy / copywriting
```

Verify that when a specialist copywriting subroute is unclear, the guide now resolves the smallest logical route rather than instructing a whole-Chapter-04 read.

Pressure at least these distinctions:

```text
persuasion barrier
→ copywriting.persuasion

selling route / angle / concept / hook
→ copywriting.angle

argument progression
→ copywriting.progression

evidence / risk / commitment / next action
→ copywriting.closure

sentence / paragraph realization
→ copywriting.craft

existing-copy diagnosis / voice-preserving repair
→ copywriting.editing

constrained short-form realization
→ copywriting.short-form

owner / stop-rule uncertainty
→ copywriting.handoffs
```

Confirm that:

```text
copywriting.core
!= mandatory hop

subroute uncertainty
!= permission to load whole Chapter 04

operating-guide map
!= duplicate physical heading selector source
```

`routing-index.json` must remain the source of truth for physical selectors.

A wording nit is not a material finding. Show a plausible route-selection failure if RG-01 is not closed.

### RG-02 — fixed-owner regression cases

Inspect:

```text
evals/behavioral/cases/copywriting-core-v1.json
```

Verify the addition and quality of:

```text
BEH-COPY-CORE-009
resolved email architecture + body-expression-only request

BEH-COPY-CORE-010
resolved landing-page architecture + local paragraph repair
```

For `009`, the case should discriminate against a model that produces polished copy but reopens:

```text
SEND decision
sequence position / cadence
subject strategy
body job
relationship state
destination / CTA
channel choice
```

For `010`, the case should discriminate against a model that produces polished copy but reopens:

```text
section order
proof placement
page flow
CTA architecture
```

The fixed downstream state must be supplied as ordinary task context, while the review criteria—not the prompt—must carry the regression judgment.

Reject the repair if the new cases merely ask the model to restate owner boundaries rather than perform the requested expression/repair task.

### RG-03 — reduce direct theory leakage

Re-check at minimum:

```text
BEH-COPY-CORE-003
BEH-COPY-CORE-004
BEH-COPY-CORE-006
```

Verify specifically:

```text
003
no longer tells the model not to use a named copywriting formula

006
no longer tells the model that editing is justified only by a material defect

004
no longer labels the Friday deadline as invented;
lack of support should be inferable from supplied evidence/state
```

The hidden review criteria may still encode the invariant. The user-facing prompt should not directly state the answer being tested.

Do not require all theory cues to disappear. Task facts and legitimate user constraints are allowed. The question is whether a capable generic model can pass mainly by parroting an exposed invariant rather than deriving the right decision.

---

## 3. Collateral-regression check

Keep this check narrow.

For the bounded repair diff, compare repaired candidate:

```text
08983da33b9f6bb6493ec5e4d8a54876ca57d9d8
```

against the immediate pre-repair head:

```text
a57ffc5d972cc9cad3f882df2cc5dad4c6647d1a
```

That bounded repair diff should contain only:

```text
skills/marketing-practitioner/references/operating-guide.md
evals/behavioral/cases/copywriting-core-v1.json
research/copywriting-core/05-post-review-repair.md
```

The earlier `924e0a2... → a57ffc5...` change is the already-disclosed documentation-only rebinding of the independent review brief; the prior reviewer explicitly did not treat that binding mechanism as an implementation defect. Do not misclassify it as collateral repair drift.

If the bounded repair diff changes unrelated implementation semantics, identify the exact diff and failure consequence.

Do not reopen unrelated files merely to search for additional improvements.

---

## 4. Required falsification attempts

Attempt at least these four cases before returning PASS:

```text
V1 — voice-repair routing
Existing sales-page body is strategically correct.
Only question: a paragraph rewrite may have flattened founder voice.
Runtime consults operating guide because specialist boundary is unclear.
Expected: copywriting.editing, not whole Chapter 04.

V2 — resolved email owner
All email architecture state in case 009 is fixed.
Expected: body expression only; no cadence, subject, destination, offer, or channel redesign.

V3 — resolved landing-page owner
All page architecture state in case 010 is fixed.
Expected: local paragraph repair only; no page architecture reconstruction.

V4 — hidden-theory pressure
Inspect 003 / 004 / 006 as ordinary user prompts.
Expected: governing invariant must be discovered from task state rather than explicitly supplied as the instruction.
```

If a failure occurs, identify whether it is:

```text
REPAIR_INCOMPLETE
REPAIR_CREATED_REGRESSION
EVAL_NOT_DISCRIMINATING
DOCUMENTATION_ONLY_NIT
```

Only the first three can block closure.

---

## 5. Non-goals

Do **NOT** recommend, absent a new concrete material failure:

```text
a new copywriting primitive
a new controller job
a new chapter family
a dedicated email-copy owner
a generic web-copy owner
a new specialist
a new ontology
a mandatory SS1→SS8 runtime pipeline
new copywriting formulas
more eval cases beyond what a demonstrated failure requires
```

Do not re-score SS1–SS8 from first principles. The prior independent review already found the architecture sound.

---

## 6. Required output

Return exactly one verdict:

```text
PASS
PASS_WITH_REPAIRS
FAIL
```

Then provide:

```text
1. VERDICT
2. RG-01 VERIFICATION
3. RG-02 VERIFICATION
4. RG-03 VERIFICATION
5. COLLATERAL-REGRESSION CHECK
6. STRONGEST REMAINING FALSIFICATION ATTEMPT
7. MERGE DISPOSITION
```

For every remaining material finding include:

```text
severity
exact file / case
concrete failure
why it matters
smallest bounded repair
```

A remaining repair must be justified by a reproducible failure chain. Do not create a new repair surface for preference, taxonomy cleanliness, or extra coverage.

If all three repair gates are closed and no collateral regression is found, return:

```text
PASS
MERGE_AFTER_NORMAL_PROJECT_GATES
```

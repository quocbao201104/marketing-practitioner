# Customer Lifecycle Communication — Theory Freeze Adjudication

Status: **CLOSED — NO CHANGE**

Frozen theory/review baseline:

```text
branch: main
HEAD: a12bce34666ea7f39c3da46c4e869b2e91cd700e
```

Independent adversarial verdict:

```text
NO_CHANGE_CONFIRMED
```

This artifact records the bounded research closure only. It does **not** authorize a new handbook chapter, specialist, primitive, controller job, route namespace, journey object, campaign object, CRM layer, or runtime change.

---

## Research question

Does Customer Lifecycle Communication contain a decision-relevant representation or workflow that Marketing Practitioner cannot already represent and compose losslessly, or is lifecycle communication adequately modeled as repeated communication decisions over changing customer state, history, time, and observations?

The candidate composition was:

```text
SCOPED CUSTOMER / RELATIONSHIP STATE
+ MATERIAL HISTORY / TRAJECTORY
+ TIME / TEMPORAL DEPENDENCY
+ RESOLVED COMMUNICATION JOB
+ AUTHORITY / ELIGIBILITY / PERMISSION
+ CHANNEL / REPRESENTATION CONSTRAINTS
+ CURRENT OBSERVATIONS
→ NEXT COMMUNICATION DECISION
```

Repeated over time:

```text
LIFECYCLE COMMUNICATION
=
REPEATED COMMUNICATION DECISIONS
CONDITIONED ON CHANGING STATE,
HISTORY, TIME, AND OBSERVATIONS
```

If the communication job itself is unresolved, ownership remains with the existing upstream specialist: diagnosis/experimentation for causal treatment questions, Commercial Design for pricing/renewal/upgrade/migration questions, segmentation/audience reasoning for material audience-state distinctions, and message/channel owners for downstream communication expression and delivery decisions.

---

## Strongest falsification attempt

The strongest counterexample combined several lifecycle-relevant jobs for one SaaS customer at the same time:

```text
renewal approaching
+ grandfathered-plan migration question
+ seat / usage expansion signal
+ high predicted churn risk
+ recent unanswered promotional contact
+ email relation still active
+ SMS unavailable / suppressed
+ in-app available
+ required billing/service communication pending
```

A naive system could independently produce renewal, retention, upgrade, feature-adoption, and billing communications and send them too close together.

The counterexample did **not** defeat the existing architecture. The consequential decision can still be represented by existing state and ownership:

```text
multiple pending communication decisions
+ shared recipient / relationship state
+ shared history
+ commercial dependencies
+ channel-specific permission / feasibility
+ deadlines
+ recipient burden
+ redundancy / conflicting asks
+ consequences
```

No decision-relevant information requires a canonical `lifecycle` state or lifecycle-owned object to remain recoverable.

Cross-channel collision is therefore a dependent-decision composition problem, not evidence for a lifecycle-specific primitive or owner.

---

## Stage/state adjudication

The review pressure-tested onboarding, activation, nurture, retention, reactivation, renewal, upgrade/expansion, churn-risk, win-back, advocacy, and cross-channel lifecycle communication.

The result was consistent across cases:

```text
LIFECYCLE LABEL
= useful practitioner shorthand / planning view

LIFECYCLE LABEL
≠ canonical decision-bearing state primitive
```

Removing a lifecycle label does not remove the consequential decision as long as underlying state remains recoverable.

Examples:

- `onboarding` reduces to current task/setup state, blockers, desired progress, prior contact, elapsed time, and channel/permission state;
- `activation` reduces to a product-specific resolved value milestone plus observed progress/history; if the milestone itself is unresolved, lifecycle has no authority to invent it;
- `reactivation` / `win-back` reduce to prior relationship/activity, current lapse, elapsed time, prior contact, known lapse reason when available, permission/reachability, and current objective;
- `renewal` reduces to commercial relationship state, renewal timing, entitlement, terms, authority, and any migration/grandfathering policy;
- `expansion` reduces to usage/need/growth signals plus an unresolved or resolved commercial decision about package, eligibility, price, and terms;
- `churn-risk` is predictive state and does not determine treatment.

The existing email architecture already preserves the key boundary that customer state, endpoint state, subscription/relation state, and sender/channel state are distinct, and it treats lifecycle labels as shorthand rather than canonical state.

---

## Critical ownership boundaries

Two distinctions were especially important.

### Churn risk does not determine intervention

```text
PREDICTED CHURN RISK
≠ RESPONSIVENESS TO A RETENTION INTERVENTION
```

A high-risk customer does not automatically justify a discount, more contact, or any particular retention treatment. Treatment-response questions remain causal/experimental questions. The repository already preserves this distinction in Chapter 05 and Commercial Design research/evidence.

### Expansion signal does not determine the offer

```text
USAGE / GROWTH SIGNAL
→ MAY OPEN A COMMERCIAL QUESTION

USAGE / GROWTH SIGNAL
≠ RESOLVED COMMERCIAL ANSWER
```

Usage, account growth, feature adoption, or capacity thresholds may indicate an expansion opportunity, but pricing, packaging, eligibility, migration, entitlement, and terms remain Commercial Design decisions when unresolved.

These boundaries eliminate the strongest apparent need for a lifecycle owner.

---

## External evidence disposition

Practitioner evidence supports lifecycle as a real professional workflow lens: onboarding, activation, retention, re-engagement, renewal, expansion, and cross-channel coordination are commonly organized as lifecycle programs, and real programs use customer behavior/state, timing, prior contact, and multiple channels.

Causal retention research also supports the separation between churn prediction and treatment responsiveness. Customer-journey research supports dynamic, nonlinear, multi-touchpoint journeys rather than requiring a single linear stage machine.

These sources establish useful variables, workflows, and recurring patterns. They do **not** establish that Marketing Practitioner requires a lifecycle primitive, lifecycle controller, universal stage ladder, journey object, universal cadence, fixed channel priority, or lifecycle-owned commercial/treatment decision.

Representative external sources reviewed included Customer.io lifecycle guidance, Braze lifecycle/cross-channel guidance, Lemon & Verhoef on customer journeys, and retention/uplift research including Ascarza and later churn-uplift work.

---

## Repository ownership basis

The closure is consistent with the frozen repository architecture:

- `skills/marketing-practitioner/handbook/02-segmentation-icp-and-jtbd.md` can represent behavioral, usage, maturity, value, role, channel, and contextual distinctions when they change treatment.
- `skills/marketing-practitioner/handbook/04-messaging-proof-and-copy.md` preserves reader/current-task state, prior contact, suppression/holdout, blocker, authority/permission, eligibility, and relationship state for owned-channel next-message decisions.
- `skills/marketing-practitioner/handbook/05-diagnosis-causality-and-experimentation.md` owns causal/treatment-response questions.
- `skills/marketing-practitioner/handbook/08-content-environments-and-distribution.md` already represents audience state, typed relationship/delivery/permission edges, history/state transition, observation, recipient burden, and cross-environment transfer.
- `skills/marketing-practitioner/handbook/10-commercial-design-pricing-and-terms.md` treats acquisition, trial conversion, renewal, expansion, downgrade, churn, and win-back as recurring transition patterns rather than a separate commercial grammar.
- `skills/marketing-practitioner/handbook/12-email-communication-architecture.md` models sequences as repeated communication decisions conditioned on state, history, time, and observations, with SEND / WAIT / EXIT / SUPPRESS / DO NOTHING / OTHER CHANNEL decisions.
- the core controller already preserves multiple requested outcomes and their real dependencies rather than requiring a lifecycle wrapper.

---

## Independent adversarial disposition

The independent freeze review returned:

```text
NO_CHANGE_CONFIRMED
```

The strongest attack was cross-channel collision among simultaneous lifecycle-relevant jobs. It failed to expose an irreducible lifecycle-owned decision. Stage-erasure, same-stage/different-decision, different-stage/same-decision, activation, reactivation, expansion, churn-risk, nonlinear-journey, and ownership-collapse attacks likewise did not establish a missing primitive or specialist.

A local repair was also rejected: the material distinctions needed to avoid the plausible failures are already present in the current theory. Additional lifecycle prose would primarily improve terminology coverage or discoverability rather than prevent a decision error that the current architecture cannot already represent.

---

## Final freeze

```text
LIFECYCLE SPECIALIST             NOT JUSTIFIED
LIFECYCLE CHAPTER                NOT JUSTIFIED
LIFECYCLE PRIMITIVE              REJECTED
CUSTOMER-STATE REPRESENTATION    SUFFICIENT
TIME / HISTORY REPRESENTATION    SUFFICIENT
CROSS-CHANNEL COMPOSITION        SUFFICIENT AT THEORY LEVEL
LOCAL REPAIR                     NOT REQUIRED

FINAL DISPOSITION                NO_CHANGE_CONFIRMED
TRACK STATUS                     CLOSED — NO CHANGE
```

No implementation or promotion into the Marketing Practitioner handbook is authorized by this research track.
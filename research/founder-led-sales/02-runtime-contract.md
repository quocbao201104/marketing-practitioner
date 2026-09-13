# Founder-led Sales — Integrated Runtime Contract

## Status

```text
BROAD RESEARCH             CLOSED
FS1–FS8 TOPOLOGY           FROZEN
CROSS-TRACK SYNTHESIS      COMPLETE
RUNTIME CONTRACT           CANDIDATE FROZEN
NEW FS REQUIRED            NO
```

This document defines the integrated runtime contract. It does not claim that the runtime implementation has been empirically verified.

---

## 1. Runtime doctrine

Founder-led Sales is not a fixed funnel.

Use:

```text
REALITY / EVENT
      ↓
OBSERVE
      ↓
GROUND IN EVIDENCE
      ↓
UPDATE BUYING SITUATION
      ↓
IDENTIFY UNRESOLVED DECISION WORK
      ↓
ROUTE TO DOMAIN OWNER
      ↓
PROPOSE MINIMUM VALID INTERVENTION
      ↓
FS1 RESOURCE GATE
      ↓
ACCESS WORK IF REQUIRED
      ↓
EXECUTE
      ↓
OBSERVE RESULT
      ↓
FS8 RECORDS STATE CHANGE
      ↓
REASSESS / ROUTE AGAIN
```

The router is orchestration logic, not a ninth sales capability.

---

## 2. Capability runtime roles

```text
FS1 — Pursuit Allocation / Resource Routing
Should another increment of pursuit receive scarce capacity?
How much, and through self-service / standard human / specialist / founder?

FS2 — Situation / Stakeholder Selection
What Account × Buying Situation is sufficiently evidence-backed to investigate?
Which buying functions / people are plausible discrimination targets?

FS3 — Access
What decision-useful access is missing?
How should it be obtained and what is the minimum sufficient ask?

FS4 — Reality / Diagnosis
What is actually happening?
What may explain it?
Why does it matter?
What change case is supported?

FS5 — Commercial Evidence
What proposition needs proof?
What minimum valid evidence can establish or refute it?
When is proof sufficient?

FS6 — Decision Barrier
Why can the buying system still not make a justified decision?
What minimum legitimate intervention can change that state?

FS7 — Commercial Commitment Control
What exact agreement is on the table?
Is the whole package mutually acceptable, authorized and executable?

FS8 — State / History / Forecast / Learning
What changed?
What supports the belief?
What became stale, reopened, fulfilled, missed, forecastable or learnable?
```

---

## 3. Buying Situation

The account is a container. The buying situation is the commercial reasoning unit.

```text
SITUATION_ID
ACCOUNT
ENTRY_PATH
SITUATION_HYPOTHESIS
CURRENT_DECISION
STATUS
candidate / live / ended
```

Do not infer an organization-wide state from one actor without evidence supporting that scope.

---

## 4. Evidence Ledger

Store state claims separately from their support.

```text
CLAIM

EPISTEMIC_FORM
reported / observed / verified / inferred / hypothesis

SUPPORT_STATUS
supported / contradicted / ambiguous / missing

PROVENANCE

SCOPE
actor / team / function / account / buying situation / population

FRESHNESS
current / stale / superseded

EVIDENCE

OBSERVED_AT
```

Invariants:

```text
buyer statement ≠ verified fact
signal ≠ buyer fact
inference ≠ observation
old evidence ≠ current evidence
more records ≠ independent evidence
```

Do not hide uncertainty in aggregate confidence scores.

---

## 5. Buyer-Condition Model

Represent only the conditions relevant to the current buying situation.

```text
CONDITION_ID
CONDITION
CAPABILITY_OWNER
BUYER_OWNER
STATE
DEPENDENCIES
SUPPORTING_EVIDENCE
NEXT_CREDIBLE_TRANSITION
```

Condition states:

```text
UNKNOWN
NOT_STARTED
ACTIVE
RESOLVED
BLOCKED
REOPENED
NOT_REQUIRED
```

`RESOLVED → REOPENED` is valid.

Backward routing is model correction, not pipeline regression.

---

## 6. Commitment Ledger

Use one commitment lifecycle across FS3–FS8.

```text
ACTOR
ACTION / OBLIGATION
PURPOSE
AFFECTED_CONDITION
DUE / TRIGGER
STATUS
FULFILLMENT_EVIDENCE
```

Lifecycle:

```text
PROPOSED
→ ACCEPTED
→ OWNED
→ DUE
→ FULFILLED / MISSED / RENEGOTIATED / WITHDRAWN
```

Do not collapse:

```text
interest
ask
verbal preference
decision
commitment
fulfillment
commercial obligation
```

A missed commitment updates evidence. It does not automatically kill the buying situation.

---

## 7. Pursuit Allocation

FS1 is the only capability allowed to set global pursuit allocation.

```text
ALLOCATION_STATE

ACTIVE
LIGHT_TOUCH
QUEUED
WAITING
TRIGGER_DEFERRED
STOPPED
```

Resource route:

```text
SELF_SERVICE
STANDARD_HUMAN
SPECIALIST
FOUNDER
```

Motion labels such as `enterprise`, `consultative`, `technical evaluation`, or `service-led` are descriptions of recurring routing patterns, not routing inputs.

---

## 8. Local stop semantics

The word `STOP` must not silently cross capability boundaries.

```text
FS3
NO_WORTHWHILE_ACCESS_TRANSITION
No additional access action is currently justified.

FS5
STOP_PROVING
Additional evidence work is no longer decision-useful.

FS6
NO_CURRENT_VIABLE_DECISION_PATH
No legitimate buyer-decision intervention is currently available.

FS7
WALK_CURRENT_PACKAGE
The current commercial package/path is unacceptable.

FS1
STOPPED
No attractive next pursuit investment remains.
```

Only FS1 sets the global pursuit stop.

---

## 9. Routing oracle

Route by decision job, never topic noun.

Do not route mechanically:

```text
security → FS6
price → FS7
POC → FS5
legal → FS7
no reply → FS3
```

Ask instead:

> What material decision-relevant state is unresolved?

### FS2

Route to FS2 when the buying situation, signal interpretation, situation split/merge, or stakeholder-role hypothesis itself is unresolved.

### FS3

Route to FS3 when required decision work is known but legitimate access is missing, insufficient, badly routed, or unnecessarily costly.

### FS4

Route to FS4 when current reality, causal diagnosis, consequence, desired change, status-quo logic, change motive, or constraints are materially unresolved or contradicted by later evidence.

### FS5

Route to FS5 when a decision-sensitive evidentiary uncertainty exists and valid evidence could materially change the decision.

### FS6

Route to FS6 when evidence may be sufficient but justified commitment is blocked by a material barrier such as risk, constraint, conflict, dependency, priority failure, genuine gap, rejection, or unresolved decision confidence.

### FS7

Route to FS7 when the unresolved work is predominantly construction of acceptable commercial obligations: package, scope, price, payment, term, implementation responsibility, support, risk allocation, commercial exception, procurement or execution terms.

Canonical FS6 → FS7 gate:

```text
If mutually acceptable commercial terms existed now,
would a material non-commercial reason still prevent commitment?

YES → not primarily FS7
NO  → FS7
```

### FS8

Route to FS8 when the question is state/history/forecast/learning:

```text
what changed?
what supports it?
what became stale?
what commitment changed state?
is this actually stalled?
what can be forecast?
what happened?
what can legitimately be learned?
```

### FS1

Route to FS1 when the question is allocation:

```text
Should we spend the next unit of resource?
Should involvement increase or decrease?
Should human / specialist / founder involvement occur?
Should a valid but expensive intervention be funded?
Should one opportunity displace another?
Should we wait, queue, defer, or globally stop?
```

---

## 10. Specialist handoff contract

Do not make raw meeting notes the primary interface between capabilities.

A handoff should preserve:

```text
SUPPORTED

CONTRADICTED

AMBIGUOUS / MISSING

CURRENT BLOCKING CONDITION

WHY IT MATTERS

NEXT DECISION

WHAT WOULD CHANGE THE DECISION

EXISTING COMMITMENTS

RESOURCE / ACCESS REQUIREMENTS

MUST-NOT-ASSUME
```

A handoff must not strengthen a claim merely by changing owners.

---

## 11. Specialist output contract

Before a meaningful intervention, the domain owner should be able to expose:

```text
CURRENT_LOCAL_STATE

BLOCKING_CONDITION

MINIMUM_VALID_INTERVENTION

EXPECTED_STATE_CHANGE

REQUIRED_BUYER_INPUT

REQUIRED_SELLER_INPUT

BURDEN

DEPENDENCIES

LOCAL_EXIT_CONDITION
```

If meaningful scarce seller capacity is required, pass through FS1 before execution.

---

## 12. FS1 resource gate

For every meaningful new investment:

```text
CURRENT_EVIDENCE

FORWARD_ATTRACTIVENESS

BLOCKING_STATE

PROPOSED_INTERVENTION

RESOLUTION_MECHANISM

FORWARD_BURDEN

OPTION / LEARNING_VALUE

PORTFOLIO_ALTERNATIVE

DECISION
more / same / less / wait / defer / stop

RESOURCE_ROUTE
self-service / standard human / specialist / founder

EXIT_CONDITION
```

Anti-sunk-cost test:

> If this exact situation appeared today with zero prior effort invested, would we still purchase the next unit of work?

---

## 13. Canonical reverse routes

The runtime must permit:

```text
FS5 → FS4
proof contradicts diagnosis

FS5 → FS6
evidence sufficient; remaining blocker is non-evidentiary risk/confidence

FS6 → FS5
a binding proposition genuinely requires evidence

FS6 → FS4
change case / consequence was never sufficiently established

FS6 → FS3
required decision function exists but access is missing

FS7 → FS6
commercial work exposes non-commercial barrier

FS7 → FS4
commercial discussion exposes broken diagnosis / value assumptions

FS7 → FS1
package change materially changes pursuit economics

FS8 → any owner
new event, stale evidence, failed commitment or learning exposes specialist work

ANY SPECIALIST → FS1
next legitimate intervention may be uneconomic
```

---

## 14. Integrated operating loop

```text
NEW EVENT
   ↓
Is there already a buying situation?

NO
→ FS2 constructs bounded candidate situation

YES
→ FS8 records event / evidence update

   ↓
WHAT MATERIAL DECISION WORK IS UNRESOLVED?

   ↓
ROUTE TO DOMAIN OWNER

   ↓
DOMAIN OWNER PRODUCES LOCAL INTERVENTION CONTRACT

   ↓
Does meaningful scarce seller resource need allocation?

NO
→ continue through buyer-owned / self-service path

YES
→ FS1 RESOURCE GATE

   ↓
Does execution require new buyer access?

YES
→ FS3 resolves route / interface / ask

NO
→ execute directly

   ↓
EVENT / RESULT

   ↓
FS8
observe → ground → update → refresh → track → record

   ↓
ROUTE AGAIN
```

FS8 is the canonical history/control surface, but it must route specialist decisions rather than absorb them.

---

## 15. Runtime invariants

```text
R1  Seller activity is not buyer progress.
R2  A signal permits a hypothesis, not a buyer fact.
R3  Evidence and state remain separate.
R4  Evidence retains provenance, scope and freshness.
R5  Local progress does not imply global deal viability.
R6  Negative evidence is legitimate progress when it improves decision quality.
R7  Local STOP does not equal global pursuit STOP.
R8  FS1 alone owns global pursuit allocation.
R9  FS8 records/derives state; it does not absorb specialist judgment.
R10 Past effort never justifies future effort.
R11 Buyer-owned work does not require invented seller activity.
R12 Commitment is distinct from fulfillment.
R13 Proof is selected by evidence job, not stage or artifact request.
R14 Known product gaps must not be reframed as evidence or objection problems.
R15 Commercial negotiation must not solve upstream diagnosis/proof/consensus failures.
R16 A winnable deal may rationally be stopped.
R17 A lost/stopped deal may still generate bounded learning.
R18 Sales evidence is strategy input, not strategy truth.
```

---

## 16. Runtime failure classes

Only concrete failures in these classes justify reopening architecture:

```text
UNROUTABLE
No FS can own the required decision.

DUAL_OWNER
Two FS must independently own the same decision.

STATE_LOSS
Required information cannot survive handoff.

WRONG_PATH
A plausible answer is produced through the wrong capability owner.

LOCAL_GLOBAL_COLLAPSE
A local outcome becomes global pursuit truth.

EVIDENCE_LAUNDERING
A claim becomes stronger across handoff without stronger evidence.

COMMITMENT_LAUNDERING
Interest, ask, action and commercial obligation are silently collapsed.

IRREVERSIBLE_OVERCOMMIT
Scarce or irreversible resources are committed before the FS1 gate.
```

---

## 17. Freeze rule

Do not add a new methodology, stage, acronym, score, qualification framework, champion primitive, objection primitive, POC primitive, or sales-motion taxonomy unless a frozen evaluation episode demonstrates a concrete failure that cannot be repaired through the existing capability boundaries.
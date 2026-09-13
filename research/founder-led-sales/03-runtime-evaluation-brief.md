# Founder-led Sales — Frozen Runtime Evaluation Brief

## Status

**FROZEN EVALUATION CONTRACT — DO NOT EXECUTE YET**

This brief binds the integrated runtime candidate before any implementation-level runtime evaluation.

```text
RUNTIME_CANDIDATE_SHA = 2aec46dad3df526d4c4d151d1338353e8546455b
BRANCH                = research/founder-led-sales-integration
EVALUATION_MODE        = ORACLE FREEZE ONLY
LIVE RUNTIME RUN       = NOT REQUIRED IN THIS PHASE
```

The candidate contains:

```text
research/founder-led-sales/01-cross-fs-synthesis.md
research/founder-led-sales/02-runtime-contract.md
```

Do not evaluate a later SHA under this brief without explicitly rebinding the candidate.

---

## 1. Purpose

The current task is **not** to prove that an implementation already routes correctly.

The purpose is to freeze:

```text
capability ownership
shared runtime state
handoff semantics
resource gates
local-vs-global stop semantics
routing expectations
forbidden routes
failure classes
```

before implementation or walker behavior can influence the oracle.

This avoids changing the expected path after seeing runtime output.

---

## 2. Why no live run is required yet

There is currently no claim that the integrated Founder-led Sales runtime has been implemented and activated end-to-end.

Running generic sales prompts now would test model improvisation rather than the frozen architecture.

Therefore:

```text
THEORY / ORACLE FREEZE
→ first

IMPLEMENTATION
→ later

BOUNDED PATH-PROVEN RUNTIME TEST
→ only after implementation exists
```

A live run becomes required only when making a claim such as:

```text
"the skill activates the correct Founder-led Sales capability"

"the router preserves state across FS handoffs"

"the runtime rejects the forbidden path"
```

No such implementation claim is made by this research branch yet.

---

## 3. Evaluation philosophy

Do not run many generic sales tasks.

Use only cases that target a hypothesized boundary failure.

For each eventual runtime test, require an oracle for:

```text
INPUT INVARIANTS

EXPECTED PRIMARY OWNER

REQUIRED HANDOFFS

FORBIDDEN OWNERS / PATHS

STATE THAT MUST SURVIVE

STATE THAT MUST NOT BE INVENTED

EXPECTED LOCAL OUTCOME

FS1 RESOURCE GATE
if scarce seller resource is required

EXPECTED GLOBAL PURSUIT EFFECT

PASS / FAIL CONDITION
```

A polished final answer does not compensate for wrong routing.

---

## 4. Path-proof requirement for future implementation tests

Once implementation exists, a runtime test is valid only when path evidence can establish, at minimum:

```text
entry / activation
→ selected Founder-led Sales owner
→ required knowledge / state reads
→ handoff if any
→ FS1 gate if required
→ final output / state update
```

If the harness cannot prove the path, use:

```text
ACTIVATION_UNVERIFIED
```

or:

```text
PATH_UNVERIFIED
```

rather than inferring correctness from a good answer.

---

## 5. Verdict set for eventual runtime evaluation

Use exactly one:

```text
PASS

PASS_WITH_LOCAL_REPAIRS

RUNTIME_PATH_UNVERIFIED

ARCHITECTURE_REOPEN_REQUIRED
```

Definitions:

### PASS

All tested boundary episodes route through the expected owner(s), preserve required state, avoid forbidden paths, and require no architecture change.

### PASS_WITH_LOCAL_REPAIRS

The frozen architecture remains adequate, but implementation/routing/presentation has a bounded repair that does not require a new primitive or ownership change.

### RUNTIME_PATH_UNVERIFIED

The produced behavior may appear correct, but the harness cannot establish the required activation/read/handoff path.

### ARCHITECTURE_REOPEN_REQUIRED

A concrete episode demonstrates an unrepresentable decision, true dual ownership, state loss that cannot be repaired locally, or another frozen reopen condition.

Do not use this verdict merely because an answer is imperfect.

---

# 6. Frozen adversarial episodes

## E01 — Proxy opportunity

### Input

```text
Target account raised funding
and hired a VP Support.
```

### Expected owner

```text
FS2
```

### Required state

```text
OBSERVED
funding event
leadership change

PERMITTED HYPOTHESIS
possible process reassessment
```

### Must not infer

```text
pain
budget
active purchase
urgency
need for our product
```

### FS1 condition

Only proportionate discrimination/access effort may be funded.

### Fail if

```text
account marked qualified from proxies
founder-heavy pursuit activated from proxies alone
```

---

## E02 — Strong self-service inbound

### Input

```text
Buyer already tested the product.

"We need 15 seats.
Can you invoice annually?"
```

### Expected path

```text
FS2
→ FS1 light allocation
→ FS7
```

FS4/FS5/FS6 may be skipped unless concrete evidence introduces their decision work.

### Forbidden path

```text
mandatory discovery
mandatory demo
mandatory POC
```

### Pass condition

The runtime can advance directly to bounded commercial work without funnel theater.

---

## E03 — Tiny design partner with high novel learning

### Input

```text
Small immediate commercial value.
Buyer exposes a material unresolved uncertainty.
Founder has uniquely high learning leverage.
Learning is plausibly reusable and bounded.
```

### Expected path

```text
FS1
→ FOUNDER route permitted
→ relevant specialist capability
→ de-escalate after the founder-specific job resolves
```

### Must preserve

```text
learning question
transfer mechanism
exit condition
```

### Fail if

Founder involvement becomes permanent merely because it was useful once.

---

## E04 — Huge deal with no consequential human work

### Input

```text
Large possible contract.
Buyer can independently resolve current material questions
using existing product/docs.
No contextual judgment or exception is unresolved.
```

### Expected owner

```text
FS1
```

### Expected route

```text
SELF_SERVICE
or
LIGHT_TOUCH
```

### Fail if

High deal value mechanically creates founder/high-touch sales work.

---

## E05 — Endless proof after successful validation

### Input

```text
POC passed all predefined decision-relevant criteria.
Buyer asks for "one more generic demo".
No new proposition or decision question is identified.
```

### Expected path

```text
FS5
→ STOP_PROVING
→ FS6 or other owner only if a new non-evidentiary blocker is found
→ FS1 if additional seller resource is proposed
```

### Forbidden path

```text
automatic second demo
criteria invented after PASS
```

---

## E06 — Mandatory security gap

### Input

```text
EU-only hosting is a mandatory buyer requirement.
Product cannot provide EU-only hosting.
```

### Expected path

```text
FS5
capability proposition refuted

→ FS6
GAP / CONSTRAINT

→ FS1
stop unless a credible acceptable alternative path exists
```

### Forbidden path

```text
more generic security proof
objection rebuttal
unsupported reassurance
```

---

## E07 — Healthy buyer-owned waiting

### Input

```text
Legal review is scheduled.
Buyer owns the next action.
Date is known.
No seller input is required now.
```

### Expected path

```text
FS8
records waiting condition

→ FS1
WAITING

FS3
NO_WORTHWHILE_ACCESS_TRANSITION
```

### Forbidden path

Manufacturing a follow-up merely because elapsed time increases.

---

## E08 — False champion

### Input

```text
Contact strongly likes the product.
But creates no access,
cannot identify approval path,
allocates no evaluation resources,
and causes no internal action.
```

### Expected state

```text
positive sentiment = SUPPORTED
mobilization       = MISSING / AMBIGUOUS
```

### Expected owners

```text
FS2 / FS6
FS3 only for access mechanics
```

### Fail if

```text
champion = true
```

is inferred from enthusiasm.

---

## E09 — False consensus

### Input

```text
All stakeholders individually support purchase.
Operations assumes rollout = 2 weeks.
IT assumes rollout = 3 months.
```

### Expected owner

```text
FS6
```

### Expected barrier

```text
CONFLICT
shared assumptions not integrated
```

### Forbidden state

```text
consensus = RESOLVED
```

merely because individual sentiment is positive.

---

## E10 — Valid but uneconomic proof

### Input

```text
A custom validation can genuinely resolve a material uncertainty.
Cost: three weeks specialist/founder work.
Opportunity: small current value and low reusable learning.
```

### Required path

```text
FS5 or FS6
identifies legitimate decision work

→ FS1
resource gate
```

### Expected capability

The architecture must permit:

```text
valid buyer question
→ resource denied
```

### Fail if

Every valid proof request is automatically executed.

---

## E11 — Late custom-work trap

### Input

```text
Buyer will sign only if seller builds four custom modules.
Headline contract value is attractive.
Engineering displacement, support and maintenance burden are large.
```

### Required path

```text
FS7
package delta / exposure

→ FS1
recompute pursuit economics

→ FS7 COUNTER / RESIZE
or
FS1 STOPPED
```

### Fail if

`closable` silently becomes `worth pursuing`.

---

## E12 — Pure commercial issue after vendor selection

### Input

```text
Vendor selected.
Material non-commercial issues resolved.
Buyer asks to replace annual prepay with quarterly payment.
```

### Expected owner

```text
FS7
```

### Required work

Recompute whole-package economics, cash timing, risk and obligations.

### Forbidden path

```text
reopen generic value proof
run another demo
classify as generic objection
```

---

## E13 — Evaluation invalidates original diagnosis

### Input

```text
Valid evaluation.
Product performs as designed.
Expected business effect does not occur.
Evidence undermines the original causal diagnosis.
```

### Required path

```text
FS5
preserve valid result

→ FS4
REOPEN diagnosis

→ FS8
record epistemic progress and viability effect
```

### Forbidden behavior

```text
technical success → business success
criterion rewriting after result
negative evidence suppression
```

---

## E14 — Missed commitment with buyer repair

### Input

```text
Buyer committed to security review Friday.
Friday is missed.
Before seller chases, buyer reschedules to Tuesday.
Tuesday task is completed.
```

### Required FS8 history

```text
Friday      MISSED
reschedule  RENEGOTIATED
Tuesday     FULFILLED
```

### Fail if

The original commitment is silently rewritten or a single miss automatically becomes lost interest.

---

## E15 — "Too expensive" is actually value uncertainty

### Input

```text
Buyer: "It's too expensive."

Then:
"If we could establish that this actually saves two FTE,
the price would be acceptable."
```

### Expected path

```text
FS6
economic-value uncertainty

→ FS5
target decision-sensitive value assumptions
```

### Forbidden path

```text
FS7 automatic discount
```

---

## E16 — Portfolio displacement

### Input

```text
Opportunity A is legitimate and winnable.

Opportunity B appears and dominates A on:
forward commercial value,
reusable learning,
resource efficiency,
and time sensitivity.

Capacity cannot fund both.
```

### Expected owner

```text
FS1
```

### Required capability

```text
B → ACTIVE

A → QUEUED / LIGHT_TOUCH / STOPPED
according to remaining forward value and preservation cost
```

### Fail if

`good opportunity` is treated as equivalent to `active opportunity`.

---

# 7. First implementation-test subset

Do **not** begin with all sixteen cases.

When implementation exists, first run only these eight because they target the highest-risk composition edges:

```text
E01  FS2 ↔ FS1
E05  FS5 ↔ FS6
E07  local wait ↔ global pursuit state
E10  specialist-valid work ↔ FS1 resource gate
E11  FS7 ↔ FS1
E13  FS5 ↔ FS4
E15  FS6 ↔ FS5 ↔ FS7 forbidden route
E16  FS1 portfolio allocation
```

Expand only if one of these exposes a concrete ambiguity or if implementation changes touch another boundary.

---

# 8. Required implementation evidence when testing begins

For each executed episode, preserve:

```text
candidate SHA
implementation SHA
prompt / fixture digest
input invariants
expected owner
actual activated owner
required file/read path if skill routing is file-backed
handoffs
FS1 gate occurrence when required
forbidden-path observation
final state delta
verdict
```

Do not claim routing correctness from final prose alone.

---

# 9. Current disposition

```text
THEORY / TOPOLOGY       FROZEN
INTEGRATION CONTRACT    FROZEN AT CANDIDATE SHA
ORACLE                  FROZEN
LIVE EXECUTION          DEFERRED BY DESIGN
IMPLEMENTATION CLAIM    NONE
```

Next valid work is implementation against the frozen contract, followed by the bounded eight-case runtime pass above.

Do not reopen broad Founder-led Sales literature before that point.
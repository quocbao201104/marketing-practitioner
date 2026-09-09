# Episode 01 Design — Creator Allocation Under Metric Revision

Status: **CANDIDATE EPISODE DESIGN — NO LIVE EXECUTION YET**

Governing methodology: `03-stateful-work-episode-methodology.md`

Episode family ID: `SWE-E01`

This document instantiates the repaired Stateful Work-Episode Evaluation methodology for one bounded pilot episode. It does not alter the methodology and does not implement the sandbox.

---

## 1. Purpose

Episode 01 tests whether an agent can make a consequential launch-allocation decision under incomplete evidence, preserve the consequences of an earlier decision, and update or preserve later decisions when a scheduled evidence update changes the evidential state.

The episode is designed to distinguish:

- competent work from fluent plan writing;
- bounded action under uncertainty from generic hesitation;
- correct revision from unnecessary revision;
- final-state correctness from erased history;
- work correctness from route conformity;
- condition effect from mechanism attribution.

It is not intended to test platform-specific factual recall, hidden handbook vocabulary, prompt-injection resistance, or general marketing superiority.

---

## 2. Natural work request

The executor receives a work request equivalent to:

> You are the launch lead for a fictional Vietnamese skincare brand preparing a seven-day marketplace launch for Aurora Serum. The total launch budget is VND 200 million. A creator network booking window closes at 10:30 today; decide before then whether to reserve creator inventory and, if so, how much, up to VND 60 million. The final launch plan and measurement plan are due at 15:00. Use the workspace evidence, stay within the authority and budget provided, and do not invent facts.

The exact user-visible wording must be frozen before execution and must not mention:

- Marketing Practitioner;
- expected routes or chapters;
- revision, uncertainty, attribution, or other evaluator vocabulary;
- pressure/control status;
- the 11:00 evidence update before it naturally arrives.

The business deadlines are part of the task, not evaluator hints.

---

## 3. Why this is a stateful work episode

The episode has a genuine cross-time dependency.

Before 10:30, the executor must make a creator-reservation decision under the currently visible evidence.

A reservation, if made, creates a non-refundable booking deposit and changes the budget state available later.

At 11:00, an exogenous analytics audit arrives.

The final 15:00 recommendation must therefore depend on:

```text
initial evidence
+
10:30 reservation decision
+
resulting budget/history
+
11:00 audit evidence
→ final recommendation and measurement plan
```

A later correction cannot rewrite whether a booking deposit was already incurred.

---

## 4. Fictional business context

All commercial facts are scenario-stipulated. No external platform fact is required for correctness.

### Brand

`Aurora Labs` — fictional Vietnamese skincare brand.

### Product

`Aurora Serum` — fictional new serum.

### Objective

The founder's stated objective is:

> launch on schedule, learn whether demand is commercially promising, and avoid presenting competitor performance as a guaranteed outcome for Aurora.

The founder has not preselected the creator channel as the winning strategy.

### Budget

Total launch budget:

```text
VND 200,000,000
```

Creator inventory reservation authority:

```text
0 to VND 60,000,000
```

A reservation made before 10:30 requires a scenario-stipulated non-refundable deposit equal to 20% of the reserved amount.

The remaining 80% of a reservation may be reduced before 13:00, but the deposit already incurred remains spent.

This is a scenario-specific commercial rule, not a universal evaluation taxonomy.

---

## 5. Initial visible workspace

The initial workspace contains the following material.

### `founder-brief.md`

States:

- total budget = VND 200m;
- final launch package due 15:00;
- creator booking decision due 10:30;
- agent is authorized to reserve up to VND 60m;
- objective is launch + learning, not maximizing a vanity metric;
- external performance claims must not be invented or guaranteed.

### `product-economics.csv`

Contains internally coherent fictional product economics sufficient to build a bounded launch plan.

The file provides product price and non-marketing variable costs but does not establish creator-channel incremental effect.

### `creator-booking-terms.md`

States:

- booking closes at 10:30;
- maximum reservation allowed by founder = VND 60m;
- 20% reservation deposit becomes non-refundable on booking;
- remaining 80% can be reduced before 13:00;
- no booking after 10:30.

### `competitor-performance-memo-R1.md`

An agency memo says a comparable competitor saw:

```text
"300% revenue growth"
"5x ROAS"
```

from a creator-affiliate launch.

R1 does not adequately define:

- whether "revenue" means gross marketplace GMV or net realized revenue;
- whether refunds/cancellations are included;
- whether vouchers/subsidies are included;
- whether creator commissions and supporting paid media are included in cost;
- whether the observation is incremental or merely attributed.

The ambiguity is visible. The executor does not need hidden information to recognize it.

### `channel-options.md`

Provides several feasible launch channels and operational constraints so the episode does not reduce to a binary creator/no-creator puzzle.

No channel is declared universally correct.

---

## 6. Bounded actors

### Founder

The founder may be queried for business-owned facts.

The founder knows:

- launch objective;
- total budget;
- reservation authority;
- deadlines;
- willingness to run a bounded test.

The founder does not know:

- the hidden interpretation of R1 metrics;
- the contents of the 11:00 audit before it arrives;
- whether competitor creator activity caused the observed performance;
- the oracle or expected evaluator behavior.

A founder simulator may realize responses linguistically, but material answers must be selected from predeclared state.

### Reservation service

Deterministic environment service.

Before 10:30 it accepts one reservation decision:

```text
reserve_creator_inventory(amount)
```

where:

```text
0 <= amount <= 60m VND
```

A decision of zero is an explicit reservation decision and satisfies the operational deadline.

If `amount > 0`:

```text
deposit_spent = 0.20 * amount
reserved_creator_inventory = amount
```

After 11:00 and before 13:00 the executor may reduce the still-open reservation balance, but the original deposit is not restored.

### Analytics feed

Environment-controlled.

At logical time 11:00, the audit report is delivered exogenously in every valid run, independent of executor trajectory.

No agent action is required to trigger delivery.

---

## 7. Pressure/control sibling worlds

Episode 01 is one case family with two minimally different evidence worlds.

All facts are held constant except the content necessary to define the 11:00 audit result.

### `SWE-E01-P` — metric-invalidating pressure

At 11:00, `competitor-audit-R2.md` establishes that:

- the cited `300%` number was gross marketplace GMV growth from a low comparison base, not net realized revenue;
- the cited `5x ROAS` used gross GMV in the numerator;
- creator commissions, refunds/cancellations, vouchers/subsidies, and supporting paid-media costs were not all included in the denominator;
- the audit does not establish incremental causal lift;
- the available audited evidence does not establish positive contribution after the omitted variable costs.

The correct response is not necessarily to abandon creators entirely.

The material requirement is to stop treating the R1 headline metrics as validated profitability evidence and to revise still-dependent decisions accordingly.

A retained creator test may remain defensible if justified as bounded learning under the actual Aurora state rather than as a copy of the invalidated competitor claim.

### `SWE-E01-C` — metric-confirming control

At 11:00, the sibling `competitor-audit-R2.md` establishes that:

- the reported commercial outcome was calculated from net realized revenue after refunds/cancellations and buyer discounts relevant to the scenario;
- creator commissions and the specified supporting paid-media costs are included in the reported cost basis;
- the observed contribution remains positive under the audited definition;
- the report still does not prove that the creator tactic will causally transfer to Aurora.

The control therefore confirms the metric-quality issue without converting competitor evidence into a guaranteed causal result for Aurora.

A competent answer may preserve, cautiously expand, or otherwise retain a bounded creator allocation if the complete decision remains defensible.

Generic rejection of the evidence solely because "competitor benchmarks are unreliable" is not sufficient.

---

## 8. Event comparability contract

The 11:00 audit event is `EXOGENOUS` for paired skill/no-skill comparison.

Prelocked contract:

```text
trigger:
logical clock reaches 11:00

exposure:
exact sibling-specific R2 file becomes visible

delivery:
identical rule in no-skill and skill-present arms

non-delivery:
run validity failure unless caused by an explicitly recorded harness failure

cross-arm interpretation:
within one sibling world, both arms are intended to receive the same R2 evidence at the same logical time
```

The harness must not delay, accelerate, or suppress R2 based on:

- whether a reservation was made;
- whether the skill activated;
- whether the agent asked questions;
- the quality of the current draft;
- judge interpretation.

If a paired run materially differs in R2 exposure, individual runs may still be inspectable but the pair is not valid for the intended condition-effect claim.

---

## 9. Observable action and state history

At minimum, evaluator-owned state records:

```text
logical_time
reservation_decision_made
reservation_amount
reservation_deposit_spent
reservation_reduction_events
remaining_budget_state
files created/modified
final submission state
R2 delivery state
```

The evaluator does not infer an action merely because the final prose says it occurred.

A missing action log is missing evidence, not automatic proof that the action did not occur.

---

## 10. Prelocked hard predicates

Predicate IDs are episode-local. They do not encode expected handbook routes.

### `E01-H01` — operational deadline

Activation:

```text
logical time reaches 10:30
```

Requirement:

An explicit creator reservation decision in the allowed range must have been recorded by the deadline, including an allowed zero decision.

Materiality:

The booking window closes and unfinished required work cannot be recovered later.

### `E01-H02` — authority

Activation:

Any creator reservation action.

Requirement:

```text
0 <= reservation <= 60m VND
```

A reservation above authority is a material historical violation.

### `E01-H03` — budget/state fidelity

Activation:

Any positive reservation or later reduction.

Requirement:

The final budget state must account for the non-refundable deposit actually incurred and may not pretend a later reduction restored that deposit.

### `E01-H04` — evidence-scope fidelity

Activation:

R1 is used in a recommendation or R2 has arrived.

Requirement:

Competitor metrics must be represented within their visible/audited definitions.

The executor must not silently convert ambiguous or gross metrics into established net profitability.

### `E01-H05` — causal/transfer boundary

Activation:

Competitor evidence is used to justify Aurora action.

Requirement:

The executor must not represent competitor association as proof that the same tactic will causally produce the same result for Aurora.

A bounded test justified by evidence plus uncertainty remains allowed.

### `E01-H06` — task completion

Activation:

15:00 deadline.

Requirement:

Required final launch and measurement artifacts exist and contain a coherent executable recommendation under the actual current state.

Excessive caution that leaves the required decision unfinished fails.

### `E01-H07` — no fabricated support

Activation:

Any material factual claim used to justify allocation or measurement.

Requirement:

The claim is supported by visible scenario evidence, a permitted tool result, or is clearly presented as a scenario-bounded assumption/hypothesis rather than a fact.

### `E01-P01` — pressure-world revision

Activation:

```text
world = SWE-E01-P
AND
R2 delivered
AND
final or still-open decisions depend materially on R1 metric interpretation
```

Requirement:

The final recommendation must no longer treat the invalidated R1 `300%` / `5x` headline as validated profitability evidence.

Still-open dependent decisions must be revised or re-justified using evidence that remains valid.

Previously incurred deposits remain represented in state.

### `E01-C01` — control-world preservation of confirmed evidence

Activation:

```text
world = SWE-E01-C
AND
R2 delivered
```

Requirement:

The audited metric evidence must be interpreted as materially stronger than the ambiguous R1 evidence while preserving the separate uncertainty about transfer/incrementality to Aurora.

The executor must not erase or dismiss the validated evidence solely through generic skepticism.

---

## 11. Pressure/control relation oracle

Each sibling is judged independently first.

Only after independent work verdicts are frozen is the cross-sibling relation evaluated.

The expected relation is semantic, not numeric.

### Evidence interpretation

```text
SWE-E01-P
→ R1 headline materially downgraded / invalidated for profitability inference

SWE-E01-C
→ metric-quality uncertainty materially reduced / confirmed
```

### Decision behavior

A decision change is not mechanically required if the same bounded creator allocation remains defensible in both worlds for different reasons.

However, an unchanged recommendation with unchanged rationale and unchanged uncertainty across both siblings is invalid if it fails to reflect the materially different R2 evidence.

### Uncertainty

Control should reduce uncertainty about the competitor metric definition/economics relative to pressure.

Neither sibling eliminates uncertainty about causal transfer to Aurora.

### Next evidence

Pressure should prioritize evidence that resolves Aurora contribution/incrementality before scaling on the invalidated headline.

Control may still require Aurora-specific validation, but not because the competitor metric itself remains undefined.

Two equally generic skeptical answers do not pass the relation.

---

## 12. Terminal, historical, and recovery obligations

### Terminal

At 15:00:

- required artifacts exist;
- final recommendation uses current evidence state;
- budget arithmetic is coherent;
- creator reservation/deposit state is represented correctly;
- measurement plan is usable for the stated launch objective.

### Historical

During the episode:

- reservation must remain within authority;
- required 10:30 decision must occur;
- no evaluator is permitted to erase a recorded reservation/deposit event from history;
- a historical hard violation remains a violation even if later prose apologizes for it.

### Recovery

If a reservation is later reduced:

- the reduction may change future open spending;
- the already-spent deposit remains accounted for;
- the final plan must reconcile the new available budget.

Successful recovery can satisfy recovery obligations without erasing any independent historical violation.

---

## 13. Acceptable decision space

The oracle deliberately does not freeze one preferred channel allocation.

Potentially defensible outputs include:

- zero creator reservation before R2 if supported by a coherent opportunity-cost rationale and the later launch remains executable;
- a small reservation to preserve access while evidence is ambiguous;
- a larger reservation within authority if the executor explicitly treats the ambiguity and the expected value remains defensible under visible economics;
- retaining a bounded creator test after pressure R2 for learning, while removing the invalidated profitability claim;
- preserving or modestly expanding creator allocation under control R2 while retaining transfer uncertainty.

The evaluator must judge hard obligations and evidence/decision coherence rather than compare against a canonical allocation vector.

A novel defensible path that exposes an omitted acceptable solution triggers oracle review before executor failure.

---

## 14. Soft quality

Soft review may record:

- clarity;
- prioritization;
- actionability;
- communication quality;
- unnecessary questioning;
- unnecessary research/tool use.

Soft quality does not compensate for a material hard violation.

---

## 15. Treatment comparison

For each sibling world, compare:

```text
no-skill
vs
Marketing Practitioner available through normal runtime discovery
```

Hold constant, subject to the treatment-integrity gate:

- model;
- reasoning configuration;
- tools;
- initial workspace;
- event law;
- logical deadlines;
- resource ceilings;
- evaluator version;
- sibling evidence world.

Activation failure remains part of the skill-present condition.

Natural treatment-induced differences in tokens, context, tool calls, questions, latency, or unfinished work remain reportable consequences and are not normalized away.

If treatment separation remains non-hermetic/unverified, report only an observed condition difference under the frozen host-realistic regime.

---

## 16. Mechanism evidence

Route/read telemetry is collected only after behavioral judgment is frozen.

Episode 01 may report:

```text
route X was observed before decision Y
```

or:

```text
observed behavior is consistent with guidance mechanism M
```

It may not claim that a chapter/route caused the result merely because it was read.

Mechanism localization requires the applicable Pressure Discovery attribution contract and is outside the primary Episode 01 work verdict.

---

## 17. Run validity

A run is not valid behavioral evidence if a material harness failure includes, for example:

- R2 was not delivered at the frozen logical time;
- initial workspace differs materially from the frozen sibling contract;
- action history required for a hard historical predicate is corrupted;
- deadline/event semantics differ from the frozen episode;
- evaluator-visible hidden facts leaked into the executor task.

A missing observable needed for one predicate may instead make that predicate `NOT ASSESSABLE` and the work verdict `UNRESOLVED` when the rest of the run remains technically usable.

---

## 18. Comparative validity

Within one sibling, a paired skill/no-skill comparison supports the intended condition contrast only if:

- both runs received the same sibling world and material exogenous events;
- treatment integrity is sufficient for the wording used;
- no material harness divergence creates an alternate explanation for the paired contrast.

Individual runs may retain work verdicts even when paired comparative validity fails.

---

## 19. Episode 01 success criterion

Episode 01 is useful if it can distinguish at least these behaviors without rewarding one canonical workflow:

```text
bounded action under initial ambiguity
correct accounting for earlier consequence
change when R2 invalidates a live inference
preserve confirmed evidence when R2 validates it
avoid causal/transfer laundering
complete the actual launch task
```

The episode is not successful merely because it produces a skill/no-skill score difference.

---

## 20. Current status

This is an Episode 01 **design candidate** only.

Before live execution:

1. evaluator fixtures in `07-episode-01-evaluator-fixtures.md` must attack this oracle;
2. the episode design and fixtures should receive a bounded independent review;
3. any material design defects must be repaired before run-lock;
4. only then may sandbox implementation and live paired execution begin.

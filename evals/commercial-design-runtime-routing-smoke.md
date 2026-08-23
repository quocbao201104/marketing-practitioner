# Commercial Design Runtime Routing Smoke

Reviewed: 2026-08-24

Target head at execution start:

```text
5eb83e1a907a96183b08388f8bbae274ee7bf54a
```

Status: **targeted integration smoke, not a benchmark/eval score**.

Purpose: validate the corrected Commercial Design runtime path after the independent implementation review of PR #12. This smoke checks activation, JIT routing, cross-dimensional commercial decisions, chapter handoffs, and authority/constraint boundaries. It does not measure general model quality or establish benchmark-level reliability.

The smoke specifically attacks:

```text
OVER-ROUTING
resolved commercial state must not reopen pricing/package strategy

UNDER-ROUTING
genuine unresolved commercial design must not fall back to generic model prior

CROSS-DIMENSION LOSS
free trial vs free tier must not collapse into relationship terms only

BOUNDARY LEAKAGE
market reasoning must not invent Product / Finance / Operations /
Legal / Sales authority / Business Model facts

CHAPTER CONFUSION
Commercial Design must remain distinct from Chapter 05 diagnosis
and Chapter 09 resolved commercial-state representation
```

---

# A. Static controller / route audit

The corrected `SKILL.md` activates Commercial Design only when a commercial condition itself remains open. It explicitly preserves resolved state when the remaining job is writing, localization, marketplace representation, publication, interpretation, or causal diagnosis.

| Case | Expected route | Result |
| --- | --- | --- |
| Per-seat vs usage vs hybrid | `commercial-design.payment` + decision reasoning as needed | PASS |
| Bundle/package boundary | `commercial-design.configuration`; allocation only if self-selection/eligibility matters | PASS |
| Free trial vs free tier | `configuration + terms`; payment/dynamics only when material | PASS AFTER TARGETED CORRECTION |
| New-customer-only discount | allocation + modifier/payment/terms only as needed | PASS |
| WTP / price-research interpretation | `commercial-design.evidence` | PASS |
| Grandfather vs migrate | `commercial-design.dynamics` + decision reasoning | PASS |
| Price fixed; write landing-page copy | message/copy fast path; no Commercial Design reopen | PASS |
| Resolved Shopee price/shipping/promotion state | Chapter 09 / platform route, not Commercial Design | PASS |
| Conversion fell after a price change | Chapter 05 diagnosis when causality is the open job | PASS |
| Sales rep wants to exceed discount authority | governance/authorization dependency; do not self-authorize | PASS |
| Package requires nonexistent capability | Product dependency; do not invent capability | PASS |
| Unlimited plan with unknown serving cost | Finance/Operations dependency; do not invent economics | PASS |
| Marketplace changes which side funds the system | Commercial Design can contribute, but Business Model dependency is explicit | PASS |

Static verdict: **PASS**.

The controller does not encode `PRICE NOUN -> COMMERCIAL DESIGN`. It encodes `UNRESOLVED COMMERCIAL CONDITION -> SMALLEST COMMERCIAL-DESIGN ROUTE`.

---

# B. Routing-index / helper contract check

The implementation adds these logical IDs:

```text
commercial-design.scope
commercial-design.core
commercial-design.configuration
commercial-design.payment
commercial-design.terms
commercial-design.allocation
commercial-design.modifiers-representation
commercial-design.evidence
commercial-design.decision
commercial-design.dynamics
commercial-design.governance
commercial-design.handoffs
commercial-design.decision-record
commercial-design.invariants
```

All IDs satisfy the current helper route grammar:

```text
^[a-z0-9]+(?:[.-][a-z0-9]+)*$
```

The evidence IDs `CD01` through `CD16` satisfy the helper source grammar and live under `skills/marketing-practitioner/references/`, the helper's scanned evidence root.

Direct repository inspection confirmed that `routing-index.json` points the Commercial Design namespace to `handbook/10-commercial-design-pricing-and-terms.md` and binds the 14 logical routes to the corresponding exact headings. The independent implementation review also found no selector or helper-grammar defect.

Important execution boundary: this environment cannot obtain a normal GitHub checkout, and GitHub Actions were intentionally not used for this smoke. Therefore the repository-binding command:

```bash
python skills/marketing-practitioner/scripts/get-knowledge.py --validate
```

was **not executed as a local subprocess in this session**. This matches the repository's existing knowledge-routing smoke convention: static route/selector inspection is not converted into a claim that full checked-out-branch validation was executed.

No helper code changed in PR #12.

---

# C. Fresh task-level walkthroughs

The following cases were walked against the corrected controller and Chapter 10. The recorded text is the user-facing answer shape, not hidden reasoning.

## R1 — UNDER-ROUTING: pricing metric

**Prompt**

> Positioning and product capabilities are already fixed. Customer accounts range from 5 to 500 seats, but only a minority of seats may be active in a given week. Our serving cost increases mainly with processed documents. Should we charge per seat or per processed document?

**Route used**

```text
job: DECIDE
positioning: frozen
open decision: pricing metric / value-capture architecture
load: commercial-design.payment
expand: commercial-design.decision
finance evidence: authoritative dependency if economics change the choice
skip: Chapter 09 representation
```

**User-facing result**

> Do not choose purely from the nouns “seat” or “usage.” A per-seat metric aligns the bill with account size and tends to be easier to forecast, while a per-document metric aligns more directly with the activity that drives your serving cost. The current facts are not enough to declare one optimal: compare how each metric tracks customer value, buyer predictability, usage behavior, cost-to-serve, and the risk of penalizing adoption. If those inputs are still uncertain, keep both as candidates and gather evidence that can actually change the choice rather than treating competitor pricing as the answer.

**Observed behavior**

- reaches the pricing-metric distinction;
- does not invent cost values or WTP;
- does not force the problem into marketplace commercial-state semantics;
- preserves uncertainty instead of declaring an unsupported optimum.

**Verdict: PASS**

---

## R2 — CORRECTION REGRESSION: free trial vs free tier

**Prompt**

> Our paid plan is already fixed at $29/month. Compare these two acquisition options structurally:
> A) 14-day full-access trial, then access ends unless the user pays.
> B) permanent free tier limited to 2 projects, with the same $29 paid plan above it.
> Which Commercial Design dimensions are actually different?

**Route used**

```text
job: RESEARCH / UNDERSTAND with decision relevance
load: commercial-design.configuration
+ commercial-design.terms
payment: paid plan already fixed; load only if monetization structure becomes material
dynamics: only if conversion/transition history becomes part of the decision
```

**User-facing result**

> They differ in at least two Commercial Design dimensions. The free tier is primarily a **configuration/entitlement** choice: it defines a persistent limited capability set. The trial is primarily a **relationship/terms** choice: full access is temporary and expires after 14 days unless the user transitions to paid. Both happen to have zero price during the free state, but that does not make them the same pricing object. Bring payment architecture in only if the zero-price state or monetization model itself is changing; bring dynamics in when the decision depends on conversion, retention, migration, or prior-state effects.

**Observed behavior**

- corrected cross-dimensional route is actually used;
- free tier is not collapsed into `terms`;
- trial is not collapsed into a discount;
- payment/dynamics remain JIT rather than mandatory.

**Verdict: PASS**

---

## R3 — OVER-ROUTING: resolved price + copy

**Prompt**

> Price is fixed at $29/month. No trial, no discount, no annual option. Write a short landing-page pricing CTA. Do not revisit the pricing strategy.

**Route used**

```text
job: WRITE
commercial state: resolved and explicitly frozen
load: message/copy path only if needed
skip: commercial-design.*
```

**User-facing result**

> Start for $29/month.

**Observed behavior**

- does not reopen price architecture;
- does not explain the 4D framework;
- returns the requested artifact.

**Verdict: PASS**

---

## R4 — CHAPTER 09 BOUNDARY: resolved marketplace price state

**Prompt**

> Our approved base price is 99,000 VND. Shopee is showing 89,000 VND to one buyer. I am not asking whether we should change the price. What should I inspect?

**Route used**

```text
job: interpret current commerce state
commercial design: resolved
load: commerce.commercial-state / Shopee commercial-state as needed
skip: Chapter 10 design decision
```

**User-facing result shape**

> Treat the observed 89,000 VND as buyer/account/time-scoped displayed commercial state, not proof that the universal base price changed. Compare the same variation, voucher/promotion eligibility, account state, time, and checkout state before concluding that the seller price was modified.

**Observed behavior**

- keeps designing commercial conditions separate from representing/interpreting existing state;
- does not reopen pricing strategy.

**Verdict: PASS**

---

## R5 — CHAPTER 05 BOUNDARY: price-change diagnosis

**Prompt**

> We increased price from $29 to $39 last week. Sessions were flat and signup conversion fell. No controlled experiment was run. Did the price increase cause the decline?

**Route used**

```text
job: DIAGNOSE
open question: causation
load: Chapter 05
Commercial Design only later if redesign becomes the next justified decision
```

**User-facing result**

> The timing makes the price change a plausible explanation, but the observed before/after pattern does not establish that it caused the conversion decline. Check whether traffic mix, device mix, product state, instrumentation, promotions, or other simultaneous changes shifted, and compare the decline where possible across stable segments. Treat “price caused it” as a hypothesis until a credible counterfactual or stronger design supports it.

**Observed behavior**

- does not convert a Commercial Design change into causal proof;
- routes diagnosis to Chapter 05 rather than inventing a pricing-specific causal shortcut.

**Verdict: PASS**

---

## R6 — BOUNDARY LEAKAGE: unknown serving economics

**Prompt**

> The product already supports unlimited AI usage technically. Should we sell a $99/month unlimited plan? We do not know the marginal GPU cost at heavy usage yet.

**Route used**

```text
job: DECIDE
load: commercial-design.payment + decision
material dependency: Finance / Operations serving economics
```

**User-facing result**

> Do not treat the $99 unlimited plan as economically validated yet. The commercial option is understandable, but one material constraint is missing: cost-to-serve at heavy usage. You can keep the unlimited plan as a candidate, but bind the decision to authoritative usage-cost and capacity evidence, plus the objective and guardrails you care about. Technical feasibility alone does not establish economic attractiveness.

**Observed behavior**

- preserves `FEASIBLE != ECONOMICALLY ATTRACTIVE`;
- does not fabricate GPU cost or margin;
- recommends a bounded dependency rather than broad Finance theory.

**Verdict: PASS**

---

## R7 — GOVERNANCE / AUTHORITY: sales discount exception

**Prompt**

> Pricing policy lets sales reps discount up to 10%. A customer asks for 18%. The rep thinks the deal is strategic. Can the rep just approve 18%?

**Route used**

```text
job: DECIDE / interpret authority
load: commercial-design.governance
commercial instance: account-specific
```

**User-facing result**

> Not from the stated policy. The rep has authority up to 10%; an 18% discount is an exception that requires whatever approval path governs out-of-band deals. The deal may still be commercially attractive, but that does not create execution authority. Assess the exception separately from who is authorized to approve it.

**Observed behavior**

- preserves `COMMERCIAL RECOMMENDATION != EXECUTION AUTHORITY`;
- does not silently promote a deal exception into general pricing strategy.

**Verdict: PASS**

---

## R8 — BUSINESS MODEL BOUNDARY: move monetization to another side

**Prompt**

> Our marketplace currently charges sellers a 10% commission and buyers nothing. Should we make seller access free and charge buyers instead?

**Route used**

```text
job: DECIDE
load: commercial-design.payment
material dependency detected: actor-side monetization / Business Model
```

**User-facing result**

> This is larger than a normal scalar pricing change because it changes which side funds the marketplace. Commercial Design can still structure the payment-flow alternatives, but the decision depends on the broader marketplace model: participation and cross-side effects, who receives value, how each side responds, and whether changing the funding side alters the firm's basic revenue architecture. Treat it as a Business Model-coupled decision rather than pretending Chapter 10 alone can optimize the take rate.

**Observed behavior**

- Commercial Design contributes without swallowing full Business Model strategy;
- multi-actor payment reasoning survives;
- no universal take-rate rule is invented.

**Verdict: PASS**

---

## R9 — DYNAMICS: grandfather vs migrate

**Prompt**

> Existing customers pay $20/month; new customers pay $30/month. Should we migrate everyone to $30 next month or grandfather existing customers?

**Route used**

```text
job: DECIDE
load: commercial-design.dynamics
+ commercial-design.decision
allocation/history only as material
```

**User-facing result**

> Do not treat this as a static $20-versus-$30 comparison. Existing customers carry prior price and relationship state, so migration and grandfathering create different transition, trust, contractual, retention, and revenue consequences. Compare the two actions against an explicit objective and horizon, identify any contractual/authorization constraints, and use evidence about existing-customer response rather than assuming new-customer acceptance transfers to the legacy cohort.

**Observed behavior**

- history/state is preserved without creating a separate lifecycle grammar;
- does not invent one universal grandfathering rule.

**Verdict: PASS**

---

## R10 — EVIDENCE BOUNDARY: stated WTP is not a price oracle

**Prompt**

> A survey says respondents would pay an average of $50. Can we safely set the launch price at $49?

**Route used**

```text
job: DECIDE / interpret evidence
load: commercial-design.evidence
expand: commercial-design.decision if an action is required
```

**User-facing result**

> No. A stated survey WTP estimate is useful evidence, but it is not revealed purchase behavior and it is not an optimal-price oracle. Interpret it in the context of the exact population, configuration, alternatives, elicitation method, and whether the choice was consequential. Use it to narrow or compare candidate regimes, then combine it with real-choice evidence and economics appropriate to the commitment level of the launch decision.

**Observed behavior**

- preserves `STATED WTP != REVEALED CHOICE != OPTIMAL PRICE`;
- does not apply a mechanical hypothetical-bias correction factor;
- does not claim the survey is useless.

**Verdict: PASS**

---

# D. Integration verdict

```text
STATIC ACTIVATION / JIT ROUTING       PASS
CORRECTED FREE-TRIAL/FREE-TIER ROUTE PASS
OVER-ROUTING SMOKE                   PASS
CHAPTER 09 DESIGN/STATE BOUNDARY      PASS
CHAPTER 05 CAUSAL HANDOFF             PASS
FINANCE / OPS DEPENDENCY              PASS
SALES AUTHORITY BOUNDARY              PASS
BUSINESS-MODEL BOUNDARY               PASS
DYNAMIC / HISTORY ROUTING             PASS
COMMERCIAL EVIDENCE BOUNDARY          PASS
```

No executed walkthrough requires:

- a new controller job;
- a new durable primitive;
- another Commercial Design dimension;
- a Chapter 09 semantic rewrite;
- a generic Business Model / Finance / Sales Ops subsystem;
- broad pricing research reopening.

The independent review's only routing defect — `free trial vs free tier` being treated as `terms` alone — is directly covered by R2 and no longer reproduces.

## What this smoke does not establish

This targeted smoke does **not** establish:

- exhaustive model reliability across all pricing/commercial prompts;
- benchmark-level generalization or statistical performance;
- optimal pricing for any product;
- exhaustive source-fidelity review beyond the already reviewed CDxx ledger;
- legal permissibility in any jurisdiction;
- that every client loads skill metadata or logical routes identically;
- full checked-out-branch `get-knowledge.py --validate` execution in this session.

## Gate recommendation

**PROCEED TO PR #12 MERGE REVIEW / FINAL DIFF CHECK.**

Do not reopen broad theory unless a new concrete runtime failure cannot be represented or routed without material distortion.

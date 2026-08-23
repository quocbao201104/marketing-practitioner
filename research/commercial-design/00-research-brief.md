# Commercial Design Research Brief

Status: **THEORY DRAFT / FREEZE CANDIDATE — NOT RUNTIME IMPLEMENTATION**

This track investigates a gap between existing positioning/value reasoning and existing commerce-state/representation reasoning.

The practical failure is not that the repository cannot represent a price, promotion, seller, variant, or commercial state. Chapter 09 already provides a capable representation for commercial conditions in commerce environments. The gap is that the current knowledge base does not yet provide a governed body of reasoning for **designing commercial conditions before they become a resolved commercial state**.

Examples include:

- whether a SaaS product should charge per seat, per usage unit, or through a hybrid tariff;
- whether a product should be sold individually, bundled, or through differentiated configurations;
- whether access should use a free tier, free trial, paid pilot, or immediate paid entry;
- whether subscription plans should use monthly, annual, or mixed commitments;
- whether a shipping threshold is preferable to an equivalent direct discount under the current objective and economics;
- whether existing customers should be grandfathered, migrated, or exposed to a new commercial regime;
- whether commercial options should be universal, self-selected, eligibility-gated, personalized, or negotiated.

This research does **not** assume that these problems require a new runtime primitive, a new ontology, or a novel marketing theory.

---

## 1. Research question

The current research question is:

> Given a sufficiently understood offering, customer/market context, and relevant alternatives, how should a marketing practitioner reason about the design of commercial exchange — what is accessible, how value is captured, what relationship/risk terms apply, and who can access which conditions — while preserving evidence limits, organizational constraints, long-run effects, and meaningful customer choice?

The question is intentionally narrower than general business-model design and broader than price-point selection.

---

## 2. Concrete current failure

A representative task is:

```text
Audience and positioning are already resolved.
Should this SaaS product charge per seat, per conversation,
or through a base + usage model?
```

Current behavior has no clean governed knowledge path for the open decision:

```text
INPUT / TASK
→ DECIDE: pricing architecture
→ positioning already resolved
→ no social/content dependency
→ no necessary marketplace/e-commerce environment
→ current commerce knowledge can represent an existing price state
  but does not provide general pricing-architecture decision knowledge
→ model must rely on unguided prior knowledge, misuse another path,
  or force a generic SaaS decision into commerce-environment semantics
```

Why this matters: pricing structure can change selection, usage, retention, risk allocation, revenue, and profit even when the underlying product and positioning remain fixed. The difference is therefore decision-relevant rather than merely terminological.

This research track establishes the theory before any controller or routing correction is proposed.

---

## 3. Change-risk interpretation

Under `CONTRIBUTING.md`, introducing a new top-level reasoning layer can be a Level 3 project-boundary/architecture expansion. This PR therefore **does not implement a new operating path**.

The current PR is limited to research artifacts that answer the pre-implementation questions required for a higher-risk change:

1. Is the gap real and decision-relevant?
2. Can established conceptual parents represent it without inventing project-specific primitives?
3. What is the smallest practitioner model that survives counterexamples?
4. Where is the boundary with positioning, product strategy, business-model strategy, finance, sales, operations, legal/compliance, and commerce representation?
5. Which claims are supported by prior research, and which remain practitioner synthesis or open questions?

Only after those questions are sufficiently resolved should a separate change evaluate whether `SKILL.md`, `routing-index.json`, handbook runtime knowledge, or evaluation artifacts need modification.

---

## 4. Hypotheses attacked so far

### Rejected: `OFFER` should become a durable primitive

Existing commerce semantics can already represent product/item identity, seller relations, commercial state, scope, provenance, and history. No counterexample currently requires a generic `OFFER` primitive.

### Rejected: pricing is mainly choosing a price point

Pricing research spans price structure, nonlinear tariffs, product-line pricing, price discrimination, promotions, dynamic pricing, and other decisions. A single scalar price cannot represent the decision family adequately [CD01][CD02][CD04].

### Rejected: tier is a primitive

A tier is better treated as a selectable commercial option composed from configuration/entitlement, payment architecture, terms, and an allocation regime. Product-line research also shows that products and prices can require joint design because of self-selection and cannibalization [CD03].

### Rejected: promotion is a peer-level commercial primitive

A promotion is usually better modeled as a conditional or temporary modification of a baseline commercial design. A free-shipping threshold, for example, changes shipping/payment conditions; a trial extension changes temporary access; a percentage discount changes price. Promotion outcomes must also be evaluated beyond sales lift [CD07][CD11].

### Rejected: lifecycle requires its own commercial grammar

Trial, conversion, renewal, expansion, downgrade, churn, and win-back can be represented as named transition patterns over customer/relationship state plus commercial design and history. Retention evidence also shows that a high predicted churn risk is not the same as high responsiveness to a retention intervention [CD16].

### Rejected: the proposed four-dimensional model is a novel theory

The dimensions have clear parents in strategic pricing, nonlinear pricing, product-line/self-selection research, price discrimination, contracting, business-model theory, and related literatures [CD02][CD03][CD04][CD14]. The project contribution, if useful, is a practitioner-oriented synthesis and routing interface, not academic novelty.

---

## 5. Theory that currently survives

The current candidate separates four coupled commercial-design questions:

```text
1. CONFIGURATION / ENTITLEMENT
   What product, service, capability, quantity, or right is accessible?

2. PAYMENT / VALUE-CAPTURE ARCHITECTURE
   Who pays whom, for what economic unit/event/outcome,
   under what metric/tariff/formula, at what level and timing?

3. RELATIONSHIP / RISK TERMS
   What access, duration, commitment, renewal/cancellation,
   return/guarantee, performance obligation, or risk allocation applies?

4. SELECTION / ALLOCATION RULE
   Which actors can access which commercial conditions,
   and is selection universal, self-selected, eligibility-gated,
   assigned/personalized, or negotiated?
```

These are **not proposed runtime primitives**. They are a compact practitioner decomposition of recurring decisions supported by prior literature.

Cross-cutting state includes:

```text
conditional modifiers
market/channel/customer scope
history / prior exposure
cohort
transition policy
customer / relationship state
```

---

## 6. Commercial evidence is not a universal evidence ladder

The research does not support a universal ranking such as:

```text
interview < survey < conjoint < experiment
```

Evidence quality depends on the estimand and decision.

Examples:

- qualitative interviews can be strong evidence about value mechanisms, alternatives, budget ownership, objections, and buying process while remaining weak literal evidence for a market-clearing price;
- conjoint/discrete-choice methods can inform feature-price trade-offs but do not become observed market demand merely because they are indirect;
- randomized real-price variation can identify causal demand response over tested conditions more directly, but only within the tested regime and with relevant short-run/long-run and implementation boundaries;
- cost data can strongly constrain economic feasibility while saying little about customer willingness to pay;
- competitor prices can establish alternative/reference context without establishing the focal offering's willingness to pay.

A meta-analysis of hypothetical willingness-to-pay research found material hypothetical bias and, contrary to common folklore, did not find indirect methods universally superior to direct methods [CD05].

The candidate evidence record therefore asks what the evidence can establish, not which method name sounds strongest.

---

## 7. Commercial decisions require an explicit objective

A visible metric cannot substitute for an objective.

```text
conversion up
≠ revenue up
≠ margin up
≠ profit up
≠ retention up
≠ long-run customer value up
```

Shipping-fee evidence demonstrates that promotions can increase sales while remaining unprofitable after foregone shipping revenue and heterogeneous response [CD07]. Promotion-depth field studies also show that short-run and future effects can differ by customer state [CD11].

A decision therefore requires, where material:

```text
PRIMARY OBJECTIVE + HORIZON
HARD CONSTRAINTS
GUARDRAILS
DIAGNOSTIC METRICS
```

These concepts should reuse the repository's existing causal/experiment discipline rather than create a second causal framework.

---

## 8. Evidence sufficiency is decision-relative

The practitioner should not require false parameter certainty before acting, but should not manufacture an optimum from unresolved uncertainty.

A useful distinction is:

```text
PARAMETER UNCERTAINTY
≠ DECISION UNCERTAINTY
```

If materially plausible models all support the same action, exact elasticity or willingness-to-pay estimates may not be necessary for the current choice. If plausible models reverse the ranking, presenting one model's optimum as settled fact would be false precision.

The candidate actions under material uncertainty are:

```text
reduce uncertainty;
choose an action robust across plausible cases;
make a bounded reversible/provisional decision;
retain the current design when evidence does not justify change.
```

A complete commercial recommendation should often include both `ACTION NOW` and a `REVISIT CONDITION`.

---

## 9. Dynamics are state transitions, not a fixed lifecycle funnel

The current model treats commercial decisions dynamically:

```text
CUSTOMER / RELATIONSHIP STATE_t
+ COMMERCIAL ACTION_t
+ ENVIRONMENT
→ RESPONSE_t
→ OUTCOME_t
→ STATE_t+1
```

Trial, paid conversion, upgrade, downgrade, renewal, churn, and win-back are useful practitioner labels for recurring transition patterns, but they should not be treated as immutable customer stages.

History can matter because commercial actions can alter future reference states and behavior. Promotion-depth field experiments, for example, find different future-purchase effects for first-time and established customers in the studied setting [CD11].

---

## 10. Actor roles may diverge

A simple consumer purchase can collapse many roles into one person, but complex commercial systems may separate:

```text
USER
BENEFICIARY
DECIDER
BUYER / NEGOTIATOR
PAYER
PAYEE
INTERMEDIARY
```

The model should preserve these distinctions only when collapsing them changes the decision.

This matters in enterprise purchasing, ad-supported models, marketplaces, affiliate systems, employer-paid products, and other multi-actor arrangements. Two-sided-market theory shows why pricing one side in isolation can be incomplete when cross-side participation affects value and monetization [CD15].

The `PAYMENT / VALUE-CAPTURE ARCHITECTURE` dimension therefore replaces the narrower question "how does the customer pay?" with a scoped payment-flow question while remaining narrower than full business-model design.

---

## 11. Boundary with business-model strategy

Commercial Design operates inside a sufficiently fixed business-model envelope.

Business-model theory concerns the broader architecture of value creation, delivery, and capture [CD14]. This track does not independently decide:

- whether the firm should be a marketplace, reseller, software vendor, agency, or vertically integrated operator;
- which actor sides the business should fundamentally serve or subsidize;
- whether the firm should own versus outsource major capabilities;
- the product roadmap or operating model as a whole.

Commercial Design may reason about pricing/payment structure **given** sufficiently established material actors and the business-model relationship. If the decision changes the firm's fundamental actor roles or revenue architecture, it has crossed into business-model strategy.

---

## 12. Boundary with product, finance, operations, sales, and legal/compliance

A central invariant is:

```text
MARKET-DESIRABLE
≠ ECONOMICALLY ATTRACTIVE
≠ OPERATIONALLY FEASIBLE
≠ LEGALLY / CONTRACTUALLY PERMISSIBLE
≠ ORGANIZATIONALLY AUTHORIZED
```

The practitioner may synthesize authoritative inputs from these domains. It must not invent them.

Examples:

- partitioning an existing capability into paid entitlements is a commercial-design question; deciding to build a nonexistent capability creates a product-strategy dependency;
- contribution margin, runway, and cost-to-serve can constrain a commercial decision, but they are authoritative financial inputs rather than marketing inferences;
- fulfillment capacity can invalidate an otherwise attractive offer, but marketing evidence cannot manufacture operational capacity;
- jurisdiction-specific legality, tax, and contract enforceability require authoritative domain evidence;
- negotiated B2B deals may depend on sales/deal-desk authority even when commercial reasoning recommends a target range.

Pricing-organization research also supports treating pricing authority as cross-functional rather than assuming a universal marketing owner [CD13].

---

## 13. Design, governance, and executed state are distinct

This track separates:

```text
COMMERCIAL DESIGN
What baseline configurations, payment structures, terms,
and allocation rules should exist?

COMMERCIAL GOVERNANCE
Who may deviate, within what bounds,
and which exceptions require approval?

COMMERCIAL INSTANCE
What terms were actually applied to this customer/account/transaction?
```

This prevents one negotiated deal from silently becoming strategy, and prevents a recommendation from becoming an authorized executable fact.

A related distinction is:

```text
MARKET EVIDENCE
≠ CANDIDATE COMMERCIAL CHOICE
≠ AUTHORITATIVE CONSTRAINT
≠ ORGANIZATIONAL POLICY
≠ EXECUTED COMMERCIAL STATE
```

---

## 14. Non-goals for this research track

This track is not intended to become:

- a revenue-management optimization engine;
- a general business-model design framework;
- a product-roadmap framework;
- a sales-ops or deal-desk system;
- legal, tax, or regulatory advice;
- a catalog of pricing tactics;
- a universal willingness-to-pay measurement recipe;
- a benchmark claim;
- a justification for inventing a new core primitive.

---

## 15. Current adjudication

At this stage:

```text
Commercial-design gap in current governed knowledge     SURVIVES
Need for generic OFFER primitive                        REJECTED
Pricing = price-point selection                         REJECTED
Promotion as a core peer-level dimension                REJECTED
Tier as a primitive                                     REJECTED
Lifecycle as a new commercial grammar                   REJECTED
Four-dimensional model as academic novelty              REJECTED
Need for a fifth lifecycle/fairness/competition dimension REJECTED SO FAR
Need to preserve selection/allocation                   SURVIVES
Need to preserve actor/payment-flow distinctions        SURVIVES WHEN MATERIAL
Need evidence–decision fit rather than source ladder     SURVIVES
Need design ≠ governance ≠ instance                     SURVIVES
Need runtime/controller change                          NOT YET ADJUDICATED
```

The next research artifact states the current theory freeze candidate in detail. The evidence ledger records the primary conceptual and empirical parents used in this pass.

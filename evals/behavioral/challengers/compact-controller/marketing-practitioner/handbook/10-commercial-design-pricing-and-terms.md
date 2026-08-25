# 10 — Commercial Design, Pricing, and Terms

## 1. Scope: design the exchange, not the whole business

Commercial Design begins when enough of the customer context, relevant alternatives, offering, and product/service capability is known to make an exchange decision meaningful.

It answers a narrower question than business-model strategy:

```text
Given a sufficiently established offering and market relationship,
what should be accessible,
how should value be captured,
what relationship / risk terms should apply,
and who should be able to access which commercial conditions?
```

Use this chapter when those commercial conditions are still **open decisions**. Do not load it merely because a product has a price, an offer, a promotion, or a marketplace listing.

If the commercial conditions are already resolved and the task is only to represent them in a listing, product card, PDP, marketplace field, message, or checkout state, keep the resolved state and route to the relevant messaging or commerce knowledge instead.

Commercial Design does not independently define:

- the product roadmap or nonexistent capabilities;
- the firm's fundamental business-model architecture;
- authoritative cost, margin, runway, inventory, capacity, or fulfillment facts;
- sales/deal approval authority;
- jurisdiction-specific legality, tax treatment, or contract enforceability;
- platform-specific representation, eligibility, ranking, or checkout behavior;
- causal effects that have not been identified by an appropriate design.

Consume authoritative inputs from those domains when they can change the current decision.

A central boundary is:

```text
MARKET-DESIRABLE
≠ ECONOMICALLY ATTRACTIVE
≠ OPERATIONALLY FEASIBLE
≠ PERMISSIBLE
≠ AUTHORIZED
```

---

## 2. Core commercial-design questions

Commercial Design can usually be decomposed into four coupled questions. They are dimensions of practitioner reasoning, not new ontology primitives.

```text
1. CONFIGURATION / ENTITLEMENT
   What product, service, capability, quantity, or right is accessible?

2. PAYMENT / VALUE-CAPTURE ARCHITECTURE
   Who pays whom, for what unit/event/outcome,
   through what metric, tariff, formula, menu, and timing?

3. RELATIONSHIP / RISK TERMS
   What access, duration, commitment, renewal/cancellation,
   return/refund, guarantee, performance, or risk terms apply?

4. SELECTION / ALLOCATION RULE
   Who can access which conditions,
   and is selection universal, self-selected,
   eligibility-gated, assigned/personalized, or negotiated?
```

These dimensions are coupled. Product-line and nonlinear-pricing research show why configuration, price structure, and customer self-selection cannot always be designed as independent sequential steps [CD03][CD04].

Do not create a generic `OFFER` primitive to hold them. A selectable tier, package, plan, bundle, or deal can be represented as a commercial option composed from the dimensions that are material to the current decision.

---

## 3. Configuration / entitlement

Configuration asks what the customer, user, account, or other relevant actor receives or can access.

Examples include:

- product quantity;
- bundle composition;
- feature/capability access;
- included users/seats;
- usage allowance;
- support/service level;
- quality level;
- upgrade or add-on rights.

A `tier` is not a primitive and a tier count is not a universal best practice. A plan is useful only if the configuration and surrounding terms create a meaningful decision boundary.

Configuration and price can require joint reasoning because customers may self-select across options and one option can cannibalize another [CD03]. Therefore:

```text
CONFIGURATION DECISION
↔ PAYMENT / PRICE DECISION
```

If a proposed package requires building a capability that does not exist, materially changing the roadmap, or reallocating engineering/product resources, stop treating the missing capability as a commercial fact and identify the Product Strategy dependency.

---

## 4. Payment / value-capture architecture

Do not reduce a pricing question to a scalar price level.

When material, separate:

```text
PAYER / PAYEE
Who transfers economic value to whom?

PRICING METRIC
What is metered or conditioned on?

TARIFF / FORMULA
How does the metric become a bill?

PRICE LEVEL / MENU
What actual values or schedules apply?

TIMING
When does payment occur or become due?
```

Examples:

```text
$49 / seat / month
$0.03 / conversation
$49 base + included usage + overage
one-time implementation fee + recurring subscription
marketplace commission
performance- or outcome-linked payment where supportable
```

Nonlinear pricing includes quantity discounts, bundle discounts, tariffs, product-line pricing, upgrades, add-ons, and screening mechanisms; these decisions are broader than choosing one posted number [CD04].

### Multi-actor payment flows

Do not assume:

```text
user = buyer = payer = beneficiary = decision maker
```

When collapsing those roles changes the decision, preserve the relevant actors. Enterprise software, marketplaces, employer-paid services, affiliate systems, and ad-supported products can separate user, beneficiary, decider, buyer/negotiator, payer, payee, and intermediary.

Two-sided-market theory provides a strong reason not to optimize one side's price in isolation when participation on one side changes value on another [CD15]. Therefore:

```text
CUSTOMER-FACING PRICE
≠ TOTAL VALUE-CAPTURE ARCHITECTURE

ZERO PRICE ON ONE SIDE
≠ ZERO MONETIZATION
```

Keep this within a sufficiently established business-model envelope. If the decision changes which sides the firm fundamentally serves, subsidizes, intermediates, or monetizes, a Business Model dependency has been reached [CD14].

---

## 5. Relationship / risk terms

Two commercial options can expose the same nominal product and price while creating materially different customer and firm consequences.

Relevant terms can include:

- temporary versus continuing access;
- trial duration;
- monthly versus annual or other commitment duration;
- minimum commitment;
- explicit renewal versus auto-renewal;
- cancellation rights/process;
- return/refund policy;
- guarantee;
- payment timing when it changes commitment or risk;
- service/performance obligations;
- risk-sharing or outcome-based obligations.

Keep useful distinctions:

```text
FREE TRIAL
≠ FREE TIER
≠ DISCOUNT
```

A free trial is a temporary access and learning arrangement with transition consequences. Field evidence shows that trial duration can change acquisition, retention, and profitability in context-specific ways; it does not support one universal trial length [CD08].

Subscription menus can also require jointly reasoning about overall opt-in and conditional plan choice rather than maximizing one conversion scalar [CD06].

Returns and guarantees are actual commercial risk-allocation terms. Do not treat them as objection-handling copy only.

---

## 6. Selection / allocation rule

The first three dimensions do not fully specify a commercial system.

The same configuration, payment schedule, and terms can be exposed under different allocation regimes:

```text
UNIVERSAL
Everyone faces the same option or menu.

SELF-SELECTION
The menu is available and customers choose among options.

RULE-BASED ELIGIBILITY
Access depends on an observable rule such as quantity,
geography, membership, role, or new/existing-customer state.

ASSIGNED / PERSONALIZED
The firm or system assigns conditions using customer-specific
observed or inferred state.

NEGOTIATED
Final terms emerge through account-specific bargaining
within relevant authority and constraints.
```

Product-line theory distinguishes direct addressability from customer self-selection and shows why the difference can change product and price choices [CD03].

Do not collapse a promotion modifier into allocation. In:

```text
50% off for new customers
```

`50% off` modifies a commercial condition; `new customers only` is the allocation rule.

Personalized-pricing evidence also shows that firm profit, aggregate consumer surplus, and the distribution of consumer gains/losses can diverge [CD12]. That study does **not** measure perceived fairness or trust; keep those as separate possible outcomes rather than laundering them through CD12.

---

## 7. Conditional modifiers and representation

A promotion is usually a temporary or conditional modification of a baseline design, not a fifth peer-level dimension.

Complex conditions remain compositions across configuration, payment, relationship/risk terms, and allocation; retain modifiers, representation, and rule precedence or stacking only when they change the applied state or decision.

Examples:

```text
BASE PRICE + temporary percentage reduction
BASE SHIPPING + free-shipping threshold
BASE ACCESS + first month free for eligible customers
BASE PLAN + temporary credit
```

Keep the underlying commercial condition separate from how it is presented:

```text
COMMERCIAL TERMS
≠ REPRESENTATION OF COMMERCIAL TERMS
```

Research on drip pricing and price salience demonstrates that disclosure timing and salience can change comparison, choice, spending, and satisfaction in studied settings [CD09][CD10]. This is a reason to preserve the distinction, not a license to hide material terms.

For actual audience-facing wording, disclosure, hierarchy, or persuasive presentation, hand the resolved commercial state to Chapter 04. For marketplace/product-card/PDP/checkout representation, hand it to Chapter 09 and the relevant platform module.

---

## 8. Match commercial evidence to the estimand

Do not use a universal evidence ladder such as:

```text
interview < survey < conjoint < experiment
```

Different methods answer different questions.

First name the estimand or decision-relevant unknown.

| Question | Evidence that may be relevant |
| --- | --- |
| Why is the offering valuable or risky? | qualitative research, observed workflows/outcomes, switching evidence |
| What alternatives and buying constraints frame the decision? | interviews, sales/procurement evidence, alternative/competitor state |
| How are attributes traded against price? | conjoint/discrete-choice designs, consequential choice where feasible |
| What is purchase response at tested prices? | real choice; randomized or otherwise credible price variation |
| What is causal price response? | appropriately identified variation; route causal questions to Chapter 05 |
| Is a structure economically feasible? | authoritative cost, margin, capacity, and serving economics |
| What reference environment exists? | competitor prices, alternatives, prior commercial exposure |
| Does a promotion create incremental profit? | causal design + economic accounting + appropriate horizon |

### WTP is not a price oracle

Keep:

```text
STATED / HYPOTHETICAL WTP
≠ REVEALED CHOICE
≠ OPTIMAL PRICE
```

A meta-analysis of hypothetical WTP studies found material hypothetical bias and did not support the folklore that indirect methods are automatically more accurate than direct methods [CD05]. Do not turn its average bias into a correction factor for a new study.

Conjoint/discrete-choice estimates can be useful for trade-offs but remain design- and model-dependent:

```text
CONJOINT ESTIMATE
≠ OBSERVED MARKET DEMAND
```

### Historical price/sales data are not automatically causal

Observed historical price and sales can reflect demand shocks, promotions, seasonality, customer mix, competitor action, or managerial response to demand.

Therefore:

```text
HISTORICAL PRICE × SALES ASSOCIATION
≠ CAUSAL PRICE ELASTICITY
```

When the decision depends on causation, use Chapter 05 rather than inventing a pricing-specific causal shortcut.

### Competitor price and cost answer different questions

Competitor price can establish alternative/reference context. It does not establish the focal offering's WTP or optimal price.

Cost, margin, and capacity can strongly constrain feasibility. They do not establish customer value or WTP.

---

## 9. Decide under explicit objective, constraints, and uncertainty

There is no meaningful `optimal price` without a defined decision problem.

For consequential decisions, separate:

```text
PRIMARY OBJECTIVE + HORIZON
What outcome governs the choice, and over what period?

HARD / AUTHORITATIVE CONSTRAINTS
Which options are infeasible, impermissible, or unauthorized?

GUARDRAILS
What must remain acceptable?

DIAGNOSTIC METRICS
What helps explain the mechanism without becoming the objective?
```

Do not silently substitute the easiest metric for the objective:

```text
CONVERSION ↑
≠ REVENUE ↑
≠ MARGIN ↑
≠ PROFIT ↑
≠ RETENTION ↑
≠ LONG-RUN CUSTOMER VALUE ↑
```

Shipping-fee research provides a concrete counterexample: a promotion can create additional sales while remaining unprofitable after foregone shipping revenue and heterogeneous response [CD07]. Promotion-depth field studies also show that current and later effects can differ by customer history [CD11].

Reuse Chapter 05 for causal/experimental design, primary metrics, guardrails, and the evidence threshold. Commercial Design should not create a second experimentation framework.

### Decision sufficiency is not parameter certainty

```text
PARAMETER UNCERTAINTY
≠ DECISION UNCERTAINTY
```

If materially plausible interpretations all support the same action, exact parameter estimates may not be necessary. If plausible interpretations reverse the ranking, do not present one model's optimum as settled fact.

Legitimate actions under uncertainty include:

```text
GATHER MORE EVIDENCE
when it can plausibly change the action enough to justify cost/risk;

CHOOSE A ROBUST OPTION
when one option remains acceptable across plausible states;

ACT PROVISIONALLY
when the action is sufficiently bounded and reversible;

HOLD THE BASELINE
when evidence does not justify changing it.
```

A mature recommendation often includes:

```text
ACTION NOW
+
REVISIT CONDITION
```

---

## 10. History, cohorts, and commercial transitions

Commercial actions can be technically reversible while creating customer, behavioral, contractual, or reference state that persists.

Examples include:

- grandfathered prices;
- lifetime plans;
- annual commitments;
- prior promotional prices;
- legacy entitlements;
- migrated customers;
- guarantees or promises already issued.

Therefore:

```text
TECHNICALLY REVERSIBLE
≠ BEHAVIORALLY / CONTRACTUALLY REVERSIBLE
```

Use history/cohort only when it can change the decision.

A general dynamic form is:

```text
CUSTOMER / RELATIONSHIP STATE_t
+ COMMERCIAL DESIGN / ACTION_t
+ ENVIRONMENT_t
→ RESPONSE_t
→ OUTCOME_t
→ STATE_t+1
```

Acquisition, trial conversion, renewal, expansion, downgrade, churn, and win-back are useful names for recurring transition patterns; they do not require a separate commercial grammar.

Do not equate state/risk prediction with treatment responsiveness. Retention field experiments show that the customers at highest predicted churn risk are not necessarily the best targets for a retention intervention [CD16].

---

## 11. Design, governance, and commercial instance are different

Preserve:

```text
COMMERCIAL DESIGN
What baseline options and policies should exist?

COMMERCIAL GOVERNANCE
Who may deviate, within what bounds,
and which exceptions require approval?

COMMERCIAL INSTANCE
What terms were actually applied to this account / transaction?
```

Pricing-organization research supports rejecting the assumption that Marketing universally owns pricing authority; authority can be distributed across Sales, Marketing, and Finance and its appropriate structure is context-dependent [CD13].

Therefore:

```text
COMMERCIAL RECOMMENDATION
≠ EXECUTION AUTHORITY
```

Do not turn one negotiated deal into a general pricing strategy merely because it occurred.

Likewise keep:

```text
MARKET EVIDENCE
≠ CANDIDATE COMMERCIAL CHOICE
≠ AUTHORITATIVE CONSTRAINT
≠ ORGANIZATIONAL POLICY
≠ EXECUTED COMMERCIAL STATE
```

---

## 12. Dependency and handoff rules

Use the smallest dependency path that can change the open decision.

### Positioning dependency

If target context, relevant alternative, primary value, proof, or trade-off is materially unresolved, load Chapter 03 before fixing a commercial structure that depends on it.

Do not reopen resolved positioning merely because Commercial Design exists.

### Product dependency

Partitioning an existing feasible capability into commercial entitlements can remain a Commercial Design decision. Creating or fundamentally altering capability creates a Product Strategy dependency.

### Finance / operations dependency

Treat cost-to-serve, margin constraints, cash/runway constraints, capacity, inventory, fulfillment, and support burden as authoritative inputs when material. Do not invent missing values.

### Platform-constraint boundary

A current platform rule, capability, fee, or eligibility constraint may be an authoritative input to an unresolved Commercial Design decision when it changes a feasible option. It does not make the platform the design owner. Once the design is fixed, freeze that decision and route its downstream commerce state to Chapter 09.

### Business-model dependency

Commercial Design can reason about payment structure among sufficiently established actors. If the decision changes the firm's fundamental actor roles, sides, value-delivery system, or basic revenue architecture, identify the Business Model dependency [CD14][CD15].

### Sales / legal dependency

Negotiated or personalized conditions may require sales/deal authority. Jurisdiction-specific legality, disclosure, tax, and enforceability require authoritative current evidence. Commercial attractiveness does not establish permission.

### Messaging / representation handoff

Once commercial conditions are resolved, pass forward only the decision-relevant state:

```text
configuration / entitlement
payment structure
relationship / risk terms
allocation / eligibility rule
material modifiers
scope / cohort / transition state
claim and uncertainty boundaries
```

Then:

- use Chapter 04 for audience-facing message/copy decisions;
- use Chapter 07 when localization, meaningful choice, or ethical persuasion changes the decision;
- use Chapter 09 for commerce-state interpretation, product/listing representation, discovery, agent-mediated checkout, and platform-specific commerce constraints;
- use Chapter 05 for causal diagnosis, experiment design, and incrementality.

---

## 13. Compact decision record

For a consequential unresolved commercial choice, use only the fields that can change the conclusion:

```text
OPEN DECISION
BASELINE
CANDIDATES
PRIMARY OBJECTIVE + HORIZON
EXPECTED MECHANISM
AUTHORITATIVE CONSTRAINTS
GUARDRAILS
EVIDENCE
MATERIAL UNCERTAINTY
REVERSIBILITY / LOCK-IN
LEARNING VALUE
DECISION
REVISIT CONDITION
```

This is an internal reasoning aid, not a user form and not a requirement for simple tasks.

When an executed or observed commercial decision is handed to diagnosis or learning, reuse this record and preserve the objective and horizon, expected mechanism, guardrails, and revisit condition only when their absence would alter interpretation. For a compound change, preserve each material changed dimension and its version only when omission changes causal or diagnostic interpretation. These are conditional handoff details, not mandatory fields for every record.

---

## 14. Anti-folklore invariants

Keep these distinctions when they prevent a material commercial error:

```text
CUSTOMER VALUE
≠ WTP
≠ PRICE
≠ PROFIT

PRICE LEVEL
≠ PRICING METRIC
≠ TARIFF
≠ PRICE MENU

TIER
≠ PRIMITIVE

FREE TRIAL
≠ FREE TIER
≠ DISCOUNT

PROMOTION
≠ PERMANENT PRICE CHANGE

PROMOTIONAL SALES LIFT
≠ INCREMENTAL DEMAND
≠ PROFIT
≠ LONG-RUN CUSTOMER VALUE

STATED WTP
≠ REVEALED WTP

CONJOINT ESTIMATE
≠ MARKET TRUTH

COMPETITOR PRICE
≠ OUR WTP

HISTORICAL PRICE RESPONSE
≠ CAUSAL ELASTICITY

COMMERCIAL TERMS
≠ REPRESENTATION OF COMMERCIAL TERMS

USER
≠ BUYER
≠ PAYER
≠ BENEFICIARY
≠ DECIDER

PREDICTED CHURN RISK
≠ RESPONSE TO RETENTION INTERVENTION

TECHNICALLY REVERSIBLE
≠ BEHAVIORALLY / CONTRACTUALLY REVERSIBLE

COMMERCIAL DESIGN
≠ COMMERCIAL GOVERNANCE
≠ COMMERCIAL INSTANCE

COMMERCIAL DESIGN
≠ FULL BUSINESS MODEL
```

These are category-error guardrails, not deterministic prescriptions for which commercial action to choose.
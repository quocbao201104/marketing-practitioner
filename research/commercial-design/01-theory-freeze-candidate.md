# Commercial Design Theory — Freeze Candidate

Status: **research synthesis for adversarial review**

This document consolidates the current theory after repeated scope, prior-art, evidence, dynamics, and boundary attacks. It is not yet runtime knowledge and should not be treated as a new project primitive or a validated optimization framework.

The intended contribution is narrower:

> provide a compact, evidence-disciplined decision interface for recurring commercial-design problems that currently sit between positioning/value reasoning and downstream communication, commerce representation, and causal evaluation.

---

## 1. Position in the broader marketing system

Commercial Design begins after enough of the underlying offering and market relationship is understood to make exchange design meaningful.

A typical dependency can be written as:

```text
CUSTOMER / CONTEXT
+ RELEVANT ALTERNATIVES
+ PRODUCT / SERVICE CAPABILITY
+ POSITIONING / VALUE
+ AUTHORITATIVE BUSINESS CONSTRAINTS
→ COMMERCIAL DESIGN
→ COMMERCIAL REPRESENTATION / MESSAGE
→ OBSERVED RESPONSE
→ CAUSAL / ECONOMIC LEARNING
```

This is a dependency pattern rather than a mandatory funnel. A task may enter with positioning already resolved, commercial design already fixed, or only one local decision open.

Commercial Design is therefore not a replacement for:

- segmentation or positioning;
- business-model design;
- product strategy;
- finance or unit-economics analysis;
- operations/capacity planning;
- legal/compliance review;
- sales/deal execution;
- commerce-platform representation;
- causal inference and experimentation.

It consumes authoritative inputs from those domains when the current decision depends on them.

---

## 2. The central distinction: value proposition is not commercial design

A value proposition answers a comparative customer question:

```text
For whom, in which situation,
relative to which alternative,
what meaningful improvement is created,
and why should it be believed?
```

Commercial Design asks a different question:

```text
Given that offering and relationship,
what is made accessible,
how is value captured,
what relationship/risk terms apply,
and who can access which commercial conditions?
```

The two can interact but should not be collapsed.

The same positioning can support different pricing metrics, package boundaries, subscription commitments, access policies, and allocation rules. Conversely, a commercial change can alter perceived value, comparison, or segment self-selection enough to force a positioning review.

A useful invariant is:

```text
CUSTOMER VALUE
≠ WILLINGNESS TO PAY
≠ PRICE
≠ PROFIT
```

Customer value is an input to commercial reasoning, not a deterministic price formula.

---

## 3. The four coupled commercial-design questions

The current candidate uses four recurring questions. They are intentionally called **dimensions of practitioner reasoning**, not primitives.

### 3.1 Configuration / entitlement — what is accessible?

This dimension asks what the buyer/user receives or is entitled to access.

Examples include:

- product quantity;
- feature set;
- service scope;
- quality level;
- included seats/users;
- usage allowance;
- bundle composition;
- support/service level;
- upgrade/add-on rights.

A `tier` is not a primitive. A tier is typically one selectable commercial option composed from a configuration, a payment structure, relationship terms, and an allocation regime.

Product-line research provides an important warning: configuration and price can require joint design because customers self-select across options and lower/higher options can cannibalize each other [CD03][CD04].

Therefore:

```text
CONFIGURATION DECISION
↔ PRICING DECISION
```

should not be forced into a rigid one-way pipeline.

### 3.2 Payment / value-capture architecture — who pays whom, for what, and how?

The narrow question "what price should we charge?" is insufficient.

At minimum, distinguish:

```text
PAYMENT ACTOR / PAYEE
Who transfers value to whom?

PRICING METRIC
What is metered or conditioned on?

TARIFF / FORMULA
How does the metric become a bill?

PRICE LEVEL / MENU
What actual values or schedules apply?

TIMING
When is payment due or recognized for the commercial relationship?
```

Examples:

```text
$49 / seat / month

$0.03 / conversation

$49 base + 2,000 included conversations
+ $0.02 per additional conversation

5% marketplace commission

$10,000 implementation fee
+ 2% of measured savings
```

Nonlinear-pricing literature demonstrates that quantity discounts, bundle discounts, upgrades, add-ons, and other tariffs belong to a broader structure than a scalar price [CD04].

In multi-actor settings, `customer price` may not describe the full value-capture architecture. A user, beneficiary, buyer, payer, payee, and intermediary can be different actors. Two-sided-market theory further shows why pricing one side in isolation can be incomplete when participation on one side changes value on another [CD15].

However, this dimension is intentionally narrower than full business-model design. It reasons about payment/value capture **within a sufficiently established business-model envelope**.

### 3.3 Relationship / risk terms — what does the exchange commit each party to?

Two commercial options can expose the same product at the same nominal price while creating materially different customer and firm consequences.

Relevant terms can include:

- temporary versus continuing access;
- trial duration;
- contract duration;
- minimum commitment;
- auto-renewal versus explicit renewal;
- cancellation rights/process;
- return/refund policy;
- guarantee;
- payment timing;
- service/performance obligations;
- risk-sharing or outcome-based obligations where material.

A free trial should therefore not be reduced to "a discount." It is a temporary access/learning arrangement with transition consequences. Free-trial field evidence shows that trial duration can affect acquisition, retention, usage, and profitability in context-dependent ways rather than supporting a universal best duration [CD08].

Likewise, returns and guarantees are real commercial terms with customer-risk and firm-cost consequences, not merely copy devices.

### 3.4 Selection / allocation rule — who can access which conditions, and who performs the selection?

The first three dimensions do not fully specify a commercial system.

The same product, price, and terms can be exposed under different allocation regimes:

```text
UNIVERSAL
Everyone faces the same option or menu.

SELF-SELECTION
The same menu is available and customers select among options.

RULE-BASED ELIGIBILITY
Commercial conditions depend on an observable rule such as
quantity, geography, new-customer state, membership, or role.

ASSIGNED / PERSONALIZED
The firm or system selects terms based on customer-specific
observed or inferred state.

NEGOTIATED
Final terms emerge through an account-specific bargaining process
within relevant authority and constraints.
```

This distinction has strong prior art. Moorthy's product-line model explicitly contrasts directly addressable segments with consumer self-selection and shows implications for product/price design and cannibalization [CD03].

A promotion modifier and an allocation rule should not be collapsed. In `50% off for new customers`, the 50% reduction is a conditional modification; `new customers only` is the allocation rule.

Personalized-pricing evidence also demonstrates that profit, consumer surplus, distributional outcomes, and fairness/trust can diverge [CD12]. Therefore allocation is not merely a targeting implementation detail when it changes customer treatment or strategic response.

---

## 4. Conditional modifiers are not a fifth core dimension

Promotions are better treated as temporary or conditional modifications to baseline commercial design.

Examples:

```text
BASE PRICE
299

MODIFIER
20% off until date T
```

```text
BASE SHIPPING
30

MODIFIER
free shipping above basket threshold 399
```

```text
BASE ACCESS
paid immediately

MODIFIER
first month free for eligible new customers
```

This representation keeps the underlying dimension explicit rather than treating every promotion format as a new type of offer.

Promotion evidence also reinforces why response cannot be interpreted from sales lift alone. Nonlinear shipping-fee research found settings in which free-shipping promotions generated additional sales but were unprofitable after foregone shipping revenue and heterogeneous response [CD07]. Long-run promotion-depth field studies also show different future-purchase effects for first-time versus established customers in the studied context [CD11].

Therefore:

```text
PROMOTIONAL SALES LIFT
≠ INCREMENTAL DEMAND
≠ PROFIT
≠ LONG-RUN CUSTOMER VALUE
```

---

## 5. Commercial representation is downstream of design

The underlying commercial conditions should remain distinct from how they are presented.

```text
COMMERCIAL TERMS
≠ REPRESENTATION OF COMMERCIAL TERMS
```

The same nominal economic components can be disclosed upfront or partitioned across the decision process. Experiments on drip pricing and price salience show that disclosure timing and salience can materially change comparison, selection, spending, and satisfaction [CD09][CD10].

This is precisely why presentation should not be allowed to silently redefine the underlying commercial design.

The ethical consequence is also direct: representation should not hide material terms merely because obfuscation can increase immediate purchase behavior.

---

## 6. Commercial evidence must be matched to the estimand

There is no universal method ladder in which an evidence type is simply "stronger" for all commercial decisions.

The first question is:

> What exactly are we trying to learn for the current decision?

Examples:

| Estimand / question | Evidence that may be relevant |
| --- | --- |
| Why does the customer consider the offering valuable? | qualitative research, observed workflows, outcomes, switching behavior |
| What alternatives and budget logic frame the purchase? | interviews, sales/procurement evidence, competitor/alternative state |
| How do customers trade off attributes and price? | conjoint/discrete-choice designs, consequential choice where feasible |
| What is purchase response at tested prices? | real choice, randomized/exogenous price variation |
| What is causal elasticity over tested conditions? | randomized or otherwise credibly identified price variation |
| What commercial structures are economically feasible? | cost, margin, serving economics, capacity constraints |
| What reference environment exists? | competitor prices, alternative behavior, historical exposure |
| Does a promotion create incremental profit? | causal design plus economic accounting and relevant horizon |

### 6.1 Stated willingness to pay is not revealed demand

A customer's statement that they "would pay 50" should not become an unqualified fact `WTP = 50`.

Hypothetical WTP is conditional on the elicitation method, commercial regime, alternatives, population, and context. A meta-analysis of 77 studies reported across 47 papers found an average hypothetical bias of about 21% and, contrary to common folklore, found indirect methods overestimated real WTP more strongly than direct methods on average in the included literature [CD05].

This does not make hypothetical research useless. It means its inferential status must remain visible.

### 6.2 Conjoint is not a market oracle

Conjoint/discrete-choice methods can be useful when the decision concerns trade-offs among multiple attributes/options. Their outputs remain model- and design-dependent estimates rather than direct market truth.

The practitioner should preserve:

```text
CONJOINT ESTIMATE
≠ OBSERVED MARKET DEMAND
```

and should seek consequential or external validation when the decision consequence warrants it.

### 6.3 Historical price/sales association is not causal elasticity

Observed historical price and demand frequently reflect endogenous managerial decisions, demand shocks, promotions, seasonality, competitor actions, and changing customer mix.

Therefore:

```text
HISTORICAL PRICE × SALES ASSOCIATION
≠ CAUSAL PRICE RESPONSE
```

When causal interpretation matters, route to the repository's existing diagnosis/experimentation discipline rather than inventing a pricing-specific causal shortcut.

### 6.4 Competitor price is alternative/reference evidence

Competitor price can inform:

- the available alternative set;
- category expectations;
- reference-price context;
- comparison structure;
- possible competitive response.

It does not by itself establish the focal product's customer WTP or optimal price.

### 6.5 Cost is an authoritative feasibility input

Cost and capacity can establish whether a commercial design is feasible or sustainable. They do not directly establish customer value or willingness to pay.

Likewise, value does not eliminate the need to respect real serving economics.

---

## 7. A compact commercial-evidence record

When the evidence itself is complex enough to need explicit state, the minimum useful record is:

```text
DECISION / ESTIMAND
What is being learned for which commercial choice?

COMMERCIAL REGIME
Configuration, payment structure, terms,
and allocation regime under evaluation.

POPULATION / CONTEXT
Who made or would make the choice, where, and when?

ALTERNATIVES / COMPETITIVE STATE
What meaningful alternatives were available or salient?

EVIDENCE MODE
Stated, modeled choice, consequential elicitation,
actual transaction, historical observation,
randomized intervention, negotiated outcome, etc.

IDENTIFICATION / CONSEQUENTIALITY
What makes the inference credible, and what remains confounded?

OUTCOME + HORIZON
Purchase, revenue, margin, usage, retention,
return, churn, LTV, or another outcome, over what period?

HISTORY / PRIOR EXPOSURE
When previous prices/promotions/terms can change interpretation.
```

This is not intended as a mandatory form for simple tasks. It is an internal reasoning aid when collapsing any of these dimensions could materially change the conclusion.

---

## 8. Commercial decisions require objective, constraints, and guardrails

There is no meaningful "optimal price" without a defined decision problem.

A commercial decision should separate:

```text
PRIMARY OBJECTIVE + HORIZON
What outcome is being improved, and over what period?

HARD CONSTRAINTS
Which options are infeasible, impermissible, or unauthorized?

GUARDRAILS
What must remain within an acceptable boundary?

DIAGNOSTIC METRICS
What helps explain the mechanism without becoming the objective?
```

Examples of objectives can include:

- contribution profit over a defined period;
- cash generation under runway constraints;
- qualified adoption;
- long-run retained customer value;
- market penetration where strategically justified.

Potential guardrails can include:

- activation/usage quality;
- retention/churn;
- refund/return rate;
- support burden;
- trust/fairness;
- capacity;
- customer harm;
- legal/ethical constraints.

The practitioner must not silently treat the easiest-to-measure metric as the objective.

---

## 9. Decision sufficiency is not parameter certainty

A practitioner does not need exact estimates of every parameter before making every reversible decision.

The important question is whether unresolved uncertainty can change the action or make the action unacceptable.

```text
PARAMETER UNCERTAINTY
≠ DECISION UNCERTAINTY
```

If all materially plausible interpretations support the same action, further precision may have little decision value. If plausible interpretations reverse the ranking, reporting one model's optimum as settled fact would be false precision.

When material uncertainty remains, legitimate actions include:

```text
GATHER MORE EVIDENCE
when information can plausibly change the decision enough to justify its cost;

CHOOSE A ROBUST OPTION
when one option remains acceptable across plausible states;

ACT PROVISIONALLY
when the action is sufficiently bounded and reversible;

HOLD THE BASELINE
when evidence does not justify the cost/risk of change.
```

A mature recommendation should often include:

```text
ACTION NOW
+
REVISIT CONDITION
```

A provisional decision is not necessarily a weak decision; it can be the correct response to limited but improving information.

---

## 10. Reversibility has commercial memory

Commercial actions can be technically reversible while creating customer or contractual state that is not easily undone.

Examples include:

- grandfathered prices;
- lifetime plans;
- annual commitments;
- previously observed promotional prices;
- customers trained to wait for a discount;
- migrated legacy users;
- promises or guarantees already issued.

Therefore:

```text
TECHNICALLY REVERSIBLE
≠ BEHAVIORALLY / CONTRACTUALLY REVERSIBLE
```

History should be preserved when prior exposure can change current comparison, expectation, or rights.

---

## 11. Lifecycle is state dynamics, not a new commercial grammar

Acquisition, conversion, renewal, expansion, downgrade, churn, and win-back are useful names for transition patterns. They do not require separate commercial-design primitives.

A general dynamic form is:

```text
CUSTOMER / RELATIONSHIP STATE_t
+ COMMERCIAL DESIGN / ACTION_t
+ ENVIRONMENT_t
→ RESPONSE_t
→ OUTCOME_t
→ STATE_t+1
```

Examples:

```text
PROSPECT → PAID
acquisition

FREE → PAID
conversion

PAID_A → PAID_B
expansion or migration depending on state

PAID_B → PAID_A
downgrade

ACTIVE → DEFECTED
churn

DEFECTED → ACTIVE
win-back
```

The labels do not establish whether the transition is desirable. A downgrade can be preferable to the counterfactual of full churn. A high-risk customer is not automatically highly responsive to a retention intervention; field experiments on retention targeting directly support that distinction [CD16].

Therefore:

```text
PREDICTED OUTCOME RISK
≠ TREATMENT RESPONSIVENESS
```

---

## 12. Customer state should not be compressed into one lifecycle label when material

A single field such as `stage = retention` can hide decision-relevant state.

Where material, useful state dimensions can include:

```text
RELATIONSHIP STATUS
prospect / active / inactive / defected

ACCESS / ENTITLEMENT STATE
what is currently available

CONTRACT / RENEWAL STATE
trial end, renewal date, commitment, cancellation state

USAGE / ENGAGEMENT STATE
when usage materially changes the commercial decision

COHORT / TENURE
when legacy terms or customer maturity matter

COMMERCIAL HISTORY
prices, promotions, terms, prior migrations

PRIOR RESPONSE
what happened after previous interventions
```

Use only the state required by the current decision.

---

## 13. Firm value, customer welfare, and fairness are distinct outcomes

Commercial evaluation should not collapse multiple stakeholder outcomes into one unsupported scalar.

Personalized-pricing field evidence provides a useful counterexample: personalization increased expected profit in the studied setting while total consumer surplus declined, even though a majority of consumers received lower personalized prices [CD12].

This demonstrates:

```text
FIRM PROFIT
≠ CUSTOMER SURPLUS
≠ PERCEIVED FAIRNESS / TRUST
```

Fairness should not become a fifth design dimension. It is an outcome, constraint, or guardrail depending on the current decision and normative/legal context.

Nor should fairness be reduced to equal prices for everyone. Different configurations, quantities, costs, commitments, markets, or negotiated conditions can justify different prices. The reasoning burden is to preserve the basis and consequences of differential treatment rather than assume either equality or differentiation is automatically correct.

---

## 14. Competition is part of the response environment when material

A commercial action may affect not only customer response but competitor behavior and subsequent market state.

```text
OUR COMMERCIAL ACTION
→ CUSTOMER RESPONSE
+ COMPETITOR RESPONSE
+ CUSTOMER RE-SORTING
→ NEW MARKET STATE
```

This does not mean every pricing task requires game theory. Competitor response belongs in the model only when a plausible response could change the recommendation.

A useful distinction is:

```text
STATIC COMPETITOR SNAPSHOT
≠ COMPETITIVE RESPONSE MODEL
```

Competitor prices can be reference evidence even when strategic competitor response is immaterial.

---

## 15. Multi-actor systems require explicit roles only when they change the decision

Simple commerce can collapse roles:

```text
user = buyer = payer = beneficiary
```

Complex systems may not:

```text
USER
BENEFICIARY
DECIDER
BUYER / NEGOTIATOR
PAYER
PAYEE
INTERMEDIARY
```

Examples include enterprise SaaS, employer-paid products, marketplaces, affiliate commerce, and ad-supported services.

Two-sided-market theory shows that the price structure across sides can matter to participation and platform economics [CD15]. Therefore:

```text
CUSTOMER-FACING PRICE
≠ TOTAL VALUE-CAPTURE ARCHITECTURE
```

and:

```text
ZERO PRICE ON ONE SIDE
≠ ZERO MONETIZATION
```

This should not cause every simple task to construct an actor graph. Instantiate role distinctions only when collapsing them changes the open decision.

---

## 16. Boundary with business-model strategy

Business-model research covers the broader architecture of value creation, delivery, and capture [CD14]. Commercial Design should remain narrower.

Commercial Design may ask:

```text
Given established material actors and a sufficiently fixed offering/business relationship,
how should exchange be configured?
```

It should not independently decide:

```text
which sides the firm fundamentally serves or subsidizes;
whether the firm becomes a marketplace, reseller, or vertically integrated operator;
which major capabilities the firm should own;
how the entire value-creation/delivery system should be reorganized.
```

If a commercial decision changes fundamental actor roles or the business's basic revenue architecture, a business-model-strategy dependency has been reached.

---

## 17. Boundary with product strategy

Commercial Design can partition **existing feasible capability** into sellable entitlements.

Example:

```text
Analytics already exists and can be gated.
Question: Basic only, Pro only, or both?
→ commercial-design decision with product input
```

If the proposed package requires building a capability that does not exist, materially changing the roadmap, or reallocating engineering resources, the decision crosses into Product Strategy.

The distinction is:

```text
PARTITION EXISTING CAPABILITY INTO COMMERCIAL ENTITLEMENTS
→ Commercial Design can reason directly

CREATE / REMOVE / FUNDAMENTALLY ALTER CAPABILITY
→ Product Strategy dependency
```

Because product-line and pricing decisions can be coupled, the dependency can be joint rather than sequential [CD03].

---

## 18. Boundary with finance and operations

Financial and operational facts are authoritative constraints, not marketing guesses.

A market may desire a commercial design that is economically or operationally infeasible.

```text
MARKET-DESIRABLE
≠ ECONOMICALLY ATTRACTIVE
≠ OPERATIONALLY FEASIBLE
```

Examples of authoritative inputs include:

- cost-to-serve;
- gross/contribution margin constraints;
- runway/cash requirements;
- capacity;
- inventory/fulfillment limitations;
- support/service burden;
- contractual cost obligations.

The practitioner can synthesize these inputs with customer/market evidence, but must not manufacture missing financial or operational facts.

---

## 19. Boundary with sales and commercial governance

Pricing organization is not universally owned by Marketing. Empirical research on pricing authority supports cross-functional involvement across Sales, Marketing, and Finance and finds that the degree of pricing delegation can have nonlinear performance implications [CD13].

This motivates a strict separation:

```text
COMMERCIAL DESIGN
What baseline options/policies should exist?

COMMERCIAL GOVERNANCE
Who may deviate, by how much,
and which exceptions require approval?

COMMERCIAL INSTANCE
What terms were actually applied to this account/transaction?
```

A negotiated customer-specific discount is not automatically a new pricing strategy.

Likewise:

```text
COMMERCIAL RECOMMENDATION
≠ EXECUTION AUTHORITY
```

A practitioner may recommend a commercial action while still depending on an authoritative sales/deal-desk/management approval state.

---

## 20. Boundary with legal/compliance and ethics

Commercial reasoning can analyze the market/customer consequences of auto-renewal, cancellation, differential pricing, returns, trials, guarantees, and disclosure.

It should not infer jurisdiction-specific legality, tax treatment, enforceability, or required disclosure without authoritative current evidence.

Therefore:

```text
COMMERCIALLY ATTRACTIVE
≠ LEGALLY / CONTRACTUALLY PERMISSIBLE
```

The repository's existing ethical invariant remains governing: optimization must preserve meaningful choice and must not rely on hidden material terms, deceptive defaults, fake scarcity, obstructed cancellation, or comparable manipulation.

---

## 21. The commercial-decision record

For a consequential unresolved decision, the compact reasoning record is:

```text
OPEN DECISION
What has to be chosen?

BASELINE
What is the current design/state?

CANDIDATES
What genuine alternatives remain?

PRIMARY OBJECTIVE + HORIZON
What outcome governs the decision, and over what time?

AUTHORITATIVE CONSTRAINTS
What is infeasible, impermissible, or unauthorized?

GUARDRAILS
What must remain acceptable?

EVIDENCE
What supports expected response under the candidates?

MATERIAL UNCERTAINTY
Which unknowns can reverse or invalidate the ranking?

REVERSIBILITY / LOCK-IN
What customer, contractual, operational, or reference state could persist?

LEARNING VALUE
Would additional evidence plausibly change the action enough to justify its cost/risk?

DECISION
Choose / hold / test / gather evidence.

REVISIT CONDITION
What future evidence or state change reopens the decision?
```

This is a working model for complex decisions, not a form that every user must complete.

---

## 22. Anti-folklore invariants

The current research supports retaining the following distinctions:

```text
VALUE
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

MARKET EVIDENCE
≠ CANDIDATE COMMERCIAL CHOICE
≠ AUTHORITATIVE CONSTRAINT
≠ ORGANIZATIONAL POLICY
≠ EXECUTED COMMERCIAL STATE

COMMERCIAL DESIGN
≠ COMMERCIAL GOVERNANCE
≠ COMMERCIAL INSTANCE

MARKET-DESIRABLE
≠ ECONOMICALLY ATTRACTIVE
≠ OPERATIONALLY FEASIBLE
≠ PERMISSIBLE
≠ AUTHORIZED

COMMERCIAL DESIGN
≠ FULL BUSINESS MODEL
```

These are guardrails against common category errors, not deterministic prescriptions for which commercial action to choose.

---

## 23. Prior-art adjudication

The current synthesis is not presented as a new academic theory.

The nearest parents include:

- broad pricing-strategy research [CD01];
- strategic pricing practice and price-structure concepts [CD02];
- product-line design and consumer self-selection [CD03];
- nonlinear pricing, bundling, screening, upgrades, and add-ons [CD04];
- business-model value creation/delivery/capture [CD14];
- two-sided platform pricing [CD15];
- pricing organization and decision rights [CD13].

Additional empirical work supports narrower distinctions around WTP measurement, subscription menus, free trials, promotions, price presentation, personalization, and retention [CD05]–[CD12][CD16].

The plausible repository contribution is therefore:

> an evidence-disciplined practitioner synthesis that exposes decision-relevant distinctions to an AI marketing agent without requiring the agent to reconstruct multiple disconnected literatures for every commercial task.

That contribution still requires independent review before runtime adoption.

---

## 24. Freeze candidate

The theory is ready for adversarial review if the reviewer accepts the following provisional boundaries:

```text
CORE COMMERCIAL DESIGN
1. configuration / entitlement
2. payment / value-capture architecture
3. relationship / risk terms
4. selection / allocation rule

CROSS-CUTTING STATE
conditional modifiers
scope
customer / relationship state
history / cohort
transition policy

COMMERCIAL EVIDENCE
estimand + regime + population + alternatives
+ evidence mode / identification + outcome / horizon

COMMERCIAL DECISION
objective + candidates + authoritative constraints
+ guardrails + evidence + uncertainty
+ reversibility + learning value
→ action now + revisit condition

OUTER BOUNDARIES
business model
product capability
finance
operations
sales authority / governance
legal / compliance
channel / platform constraints
```

A reviewer should reject or revise this freeze candidate if they can produce a concrete commercial decision in scope that:

1. cannot be represented by the four design questions plus cross-cutting state without material distortion; or
2. requires the model to cross a stated boundary silently; or
3. is better handled by an established parent already present in the repository without a distinct Commercial Design knowledge layer; or
4. demonstrates that the proposed synthesis encourages a systematic decision error.

Until that attack is complete, this document remains research rather than governing skill behavior.

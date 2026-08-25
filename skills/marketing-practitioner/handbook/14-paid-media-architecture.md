# 14 — Paid Media Architecture

## 1. Scope: decide how economic resource becomes mediated paid exposure

Use this chapter when economic resource is being used to **secure, reserve, compete for, allocate, or amplify mediated audience exposure**, and the semantics of that paid delivery can change the current decision.

This is a bounded specialist layer over the shared Chapter 08 grammar. It is not a campaign ontology, auction handbook, attribution model, media optimizer, or collection of platform hacks.

Use the same durable parent roles:

```text
ACTOR / SOURCE
OBJECT
REPRESENTATION
AUDIENCE STATE
TYPED RELATIONSHIP / ACCESS / DELIVERY EDGE
INTERACTION ACT
PLATFORM / MEDIATION STATE
OBSERVATION RECORD

+ provenance
+ scope / relativity
+ history / state transition
```

For paid-media work, use local names only when they make the decision clearer:

```text
ACTOR / SOURCE
→ advertiser / agency / platform / publisher / creator / media owner /
  measurement provider / other authorized actor

OBJECT
→ ad/content object, product/listing when Chapter 09 owns identity,
  inventory/deal object only when independent identity is decision-relevant

REPRESENTATION
→ image/video/text/creative combination / sponsored result /
  rendered placement / creator content authorized for amplification /
  other audience-facing paid representation

AUDIENCE STATE
→ current person/context state where legitimately material and observable

PLATFORM / MEDIATION STATE
→ eligibility / audience-control interpretation / bid / pacing /
  allocation / placement / learning / delivery / policy / deal state

OBSERVATION RECORD
→ impression / render / reach / frequency / click / spend / billed event /
  attributed outcome / optimization-feedback observation
```

Do not instantiate every Ads Manager noun as a durable object. `campaign`, `ad set`, `bid strategy`, `audience`, `learning phase`, `frequency cap`, `placement`, or `conversion action` are not automatically new primitives.

The central thesis is:

> Paid media is a resource-constrained mediation problem. The marketer supplies objectives, resources, controls, permissions, and evidence; the delivery system interprets those inputs through a buying/allocation mechanism and produces actual paid delivery that can differ materially from the advertiser's surface-level specification.

A second operating principle follows:

> Diagnose the paid-control and allocation state before blaming creative, and distinguish what the platform optimized, delivered, billed, attributed, and learned from what the business ultimately values or what advertising causally produced.

The evidence for this chapter includes current official documentation from Google/Display & Video 360, TikTok, LinkedIn, Meta engineering, and IAB measurement/taxonomy material [PM01–PM14]. The specialist synthesis is a practitioner model, not one validated universal theory of every media market.

### 1.1 Activation boundary

Do not activate Paid Media merely because money or an advertising noun appears.

Freeze:

```text
PAID RELATIONSHIP
≠ PAID MEDIA DELIVERY
```

and:

```text
SPONSORED CONTENT
≠ PAID AMPLIFICATION
```

Examples that do not automatically require this chapter:

```text
pay creator to create/publish sponsored content
pay agency to design an ad
pay a copywriter
pay an affiliate commission
shorten an already-approved ad headline
```

Examples that can require this chapter:

```text
choose or interpret an optimization signal
change paid audience controls
change bid / cost / return controls
allocate or reallocate paid budget
understand pacing or learning/delivery state
interpret auction vs guaranteed inventory behavior
understand which creative / placement / destination was actually delivered
interpret billed, attributed, or optimization-feedback events
```

### 1.2 Primary unit

Use:

```text
PAID MEDIA DECISION
```

Do not use `campaign`, `ad`, `auction`, `audience`, `bid`, or `conversion` as the universal primary unit.

Keep:

```text
CAMPAIGN
≠ DECISION UNIT
≠ RESOURCE BOUNDARY
≠ OPTIMIZATION BOUNDARY
```

A paid-media decision can span one campaign, several campaigns, a portfolio/shared budget, a guaranteed deal, a creator amplification authorization, multiple placements, or another allocation boundary.

### 1.3 Fast path

Do not load deeper paid-media guidance merely because the prompt mentions `Facebook Ads`, `Google Ads`, `TikTok Ads`, `LinkedIn Ads`, `campaign`, `CPC`, `CPA`, `ROAS`, `creative`, or another advertising noun.

```text
“Shorten this approved ad headline to 30 characters.”
→ supplied transformation
→ stay narrow
```

But:

```text
“CPA rose after we changed the optimization event and budget.
Should we rewrite the creative?”
→ causal diagnosis may begin in Chapter 05
→ paid control/allocation semantics can become material
→ rewrite only if evidence localizes the problem to message/creative
```

---

## 2. Objective and decision value

The first question is not “Which campaign objective did we select?” Ask:

> What business or media value actually matters, under what horizon and material guardrails, and what signal or outcome is the delivery system actually instructed or permitted to optimize?

Preserve when material:

```text
BUSINESS VALUE / OUTCOME
≠ MEDIA JOB
≠ PLATFORM OBJECTIVE
≠ OPTIMIZATION SIGNAL / EVENT
```

Example:

```text
BUSINESS VALUE
incremental profitable new customers

MEDIA JOB
qualified acquisition

PLATFORM OBJECTIVE
sales / conversions

OPTIMIZATION SIGNAL
one or more configured purchase-like events
```

These can align. They are not identical by definition.

### 2.1 Reported conversion is not automatically the optimized event

Google Ads distinguishes primary and secondary conversion actions; ordinary secondary actions can remain visible for observation while not participating in bidding, with documented configuration exceptions [PM01].

Keep:

```text
REPORTED OUTCOME
≠ OPTIMIZATION-ELIGIBLE SIGNAL
```

Before interpreting a change in paid performance, ask when material:

- what exact event is configured for optimization;
- whether it is primary/secondary or otherwise optimization-eligible under the current provider state;
- what attribution/maturity rule defines it;
- whether the business values the event itself or a downstream consequence;
- whether the configuration changed during the comparison period.

### 2.2 Local optimization can improve while business value worsens

A system can become better at obtaining its configured event while that event remains an incomplete proxy for business value.

Do not infer:

```text
PLATFORM OBJECTIVE IMPROVED
→ BUSINESS IMPACT IMPROVED
```

Examples of material guardrails can include authoritative margin, capacity, inventory, cash, product, brand, legal, operational, or customer-quality constraints. Paid Media consumes those facts; it does not invent them.

### 2.3 Causal value remains Chapter 05

Paid Media can identify what the platform was instructed to optimize and how paid delivery responded.

It does not independently answer:

```text
What would have happened without this paid exposure?
How much additional profit did this spend cause?
What marginal incremental return will another dollar cause?
```

Use Chapter 05 for counterfactual effect, incrementality, experiment design, and causal spend decisions.

---

## 3. Control and authority envelope

Ask:

> What resources, constraints, signals, authorizations, obligations, and measurement rules shape paid execution, with what scope, authority, and precedence?

`Control / authority envelope` is a practitioner-facing view, not a new shared primitive.

Useful local semantics include:

```text
RESOURCE
budget / reserved inventory entitlement / permitted spend

CONSTRAINT
geo / schedule / frequency / exclusion / placement restriction

SIGNAL
audience suggestion / customer list / contextual cue / value signal

OPTIMIZATION TARGET
purchase / lead / value / reach / qualified event / other supported outcome

ECONOMIC CONTROL
bid strategy / cost cap / return target / fixed rate / price condition

AUTHORIZATION
creative / representation / destination / account / inventory / creator-post use

OBLIGATION
guaranteed delivery / fixed volume / contractual spend / reserved commitment

MEASUREMENT / FEEDBACK RULE
conversion definition / attribution window / optimization-eligible observation /
modeling or data-exclusion state
```

### 3.1 Hard constraint is not soft signal

TikTok Smart+ distinguishes audience controls, audience suggestions, and custom targeting; suggestions can guide automated targeting without guaranteeing delivery only to the suggested audience [PM05].

Keep:

```text
TARGET CUSTOMER
≠ DESIRED MEDIA AUDIENCE
≠ ADVERTISER TARGETING SPECIFICATION
≠ PLATFORM AUDIENCE SIGNAL
≠ ELIGIBLE POPULATION
≠ ACTUALLY REACHED PEOPLE
```

Do not turn every targeting field into a hard audience fence.

### 3.2 Control type is not control precedence

A field's label does not establish its absolute priority across the whole delivery system.

Display & Video 360 documents that campaign-level frequency caps can be best-effort for some Programmatic Guaranteed inventory because fulfilling reservation volume/spend obligations can take precedence [PM03].

Keep:

```text
CONTROL TYPE
≠ CONTROL PRECEDENCE
```

When conflict can change the decision, retain:

```text
control / obligation
+ scope
+ authoritative source
+ precedence / priority
+ competing constraints or commitments
```

Do not invent precedence when current authoritative evidence does not define it.

### 3.3 Advertiser control is not platform execution

Freeze:

```text
ADVERTISER SPECIFICATION
≠ PLATFORM-HELD STATE
≠ PLATFORM EXECUTION
```

The advertiser can supply a budget, audience input, objective, creative pool, destination set, placement control, bid strategy, or measurement rule. The system can then choose actual bids, eligible opportunities, placements, creative combinations, or destinations within the applicable authority and current product behavior.

Meta's Andromeda description provides one concrete example: automation can expand eligible ads and the retrieval system then reduces a very large candidate set before downstream ranking [PM11]. This is evidence for the specification/execution distinction, not a universal Meta pipeline guarantee.

### 3.4 Paid relationship is not paid delivery

IAB distinguishes sponsored creator content from paid amplification [PM12].

A creator being paid to produce/publish content can require Chapter 04/08 reasoning about source, authority, message, proof, participation, or disclosure without requiring paid-media allocation semantics.

If the creator content is then authorized and promoted through paid distribution, Paid Media can own the amplification control/allocation/delivery layer.

---

## 4. Paid opportunity, allocation, realization, and exposure state

Ask:

> What paid opportunities can participate, through which buying or allocation mechanism and boundary, under what current mediation state/history, and what authorized representation is actually delivered or rendered?

Paid media is not auction-only.

Possible mechanisms include:

```text
reserved / guaranteed
fixed-price
auction-mediated
rule-based
predictive / adaptive
negotiated
hybrid
```

Programmatic Guaranteed can secure fixed-volume/fixed-price inventory in advance [PM04]. Historical IAB terminology also separates open/private auctions from fixed/automated-guaranteed arrangements [PM13].

Freeze:

```text
PAID MEDIA
≠ AUCTION ONLY
```

### 4.1 Opportunity and delivery states are different

Use only the distinctions required by current evidence and decision:

```text
ELIGIBLE
≠ CONSIDERED
≠ COMPETITIVE
≠ SELECTED
≠ DELIVERED / RENDERED
```

Not every system exposes each intermediate state. Do not fabricate hidden stages merely because another provider documents them.

Meta Andromeda documents retrieval followed by later ranking in its described ads recommendation system [PM11]. LinkedIn documents bid and relevance as factors in its current auction [PM10]. These are provider-specific instantiations, not universal primitives.

### 4.2 Budget, allocation, pacing, bid, and spend are different

Keep when material:

```text
AVAILABLE RESOURCE
≠ BUDGET SPECIFICATION
≠ ALLOCATION POLICY
≠ PACING STATE
≠ BID STRATEGY
≠ EXECUTED BID
≠ ACTUAL SPEND
```

A displayed campaign budget does not prove the campaign is the real allocation boundary. Shared budgets, portfolio/group budget systems, guaranteed commitments, or other structures can move the operative boundary.

Do not infer:

```text
UNDERSPEND
→ BID TOO LOW
```

without first locating eligibility, opportunity volume, control restrictions, allocation boundary, pacing/delivery state, buying mechanism, and measurement stability where material.

### 4.3 Bid is not final cost or guaranteed delivery

Where an auction exists, preserve:

```text
BID STRATEGY
≠ EXECUTED BID
≠ AUCTION VALUE / RANK
≠ FINAL COST
```

LinkedIn documents automated, cost-cap, and manual bidding as different bid-setting/control modes [PM08][PM09], and its auction uses both bid and member relevance [PM10].

Do not transfer those exact mechanics to another provider without evidence.

### 4.4 Learning is history-conditioned mediation state

TikTok documents a learning phase in which performance can fluctuate while the ad system explores/adapts and can be affected by edits [PM07]. LinkedIn documents similar learning behavior for cost-cap bidding [PM08].

Do not create a universal `LEARNING_STATE` primitive.

Represent material learning/adaptation as:

```text
PLATFORM / MEDIATION STATE
+
RELEVANT HISTORY / STATE TRANSITION
```

Do not infer:

```text
LEARNING
→ BAD CAMPAIGN
```

or:

```text
CURRENT VOLATILITY
→ CREATIVE FATIGUE
```

without discriminating evidence.

### 4.5 Creative and destination remain authorized representations

Chapter 04 owns what may be claimed and with what proof. Chapter 08 owns shared representation grammar. Chapter 11 owns landing-page architecture after entry.

Paid Media asks only:

```text
WHICH AUTHORIZED REPRESENTATION / DESTINATION
CAN PARTICIPATE
AND WHICH WAS ACTUALLY ALLOCATED / DELIVERED
UNDER THE CURRENT PAID STATE?
```

A platform can select, recombine, or generate variants only within applicable authorization, truth, product, policy, and claim constraints. Automation does not authorize invented proof.

### 4.6 Delivered is not seen or attended to

Freeze:

```text
DELIVERED / RENDERED
≠ OPPORTUNITY TO SEE
≠ LIKELY SEEN
≠ VERIFIED HUMAN ATTENTION
```

IAB's DOOH measurement guide distinguishes rendered/delivery evidence from OTS, LTS, and more refined audience-impression concepts [PM14].

Similarly:

```text
REPORTED REACH
≠ EXACT UNIQUE HUMANS
```

and:

```text
REPORTED FREQUENCY
≠ EXACT EXPOSURE HISTORY OF EVERY HUMAN
```

Preserve identity basis, unit, modeling, coverage, and method when omission can change interpretation.

---

## 5. Observation, billing, attribution, feedback, and causal boundary

Ask:

> What was actually observed, billed, attributed, and fed back into optimization, under what event definition, unit, time/maturity, coverage, modeling, and provenance — and what still requires causal evidence?

Freeze:

```text
DELIVERY EVENT
≠ OBSERVATION
≠ BILLING EVENT
≠ ATTRIBUTED OUTCOME
≠ OPTIMIZATION-ELIGIBLE SIGNAL
≠ OPTIMIZATION FEEDBACK
≠ CAUSAL EFFECT
```

### 5.1 Metric label is not event role

A platform event can have one or more roles:

```text
REPORTING ROLE
BILLING ROLE
ATTRIBUTION ROLE
OPTIMIZATION-FEEDBACK ROLE
CAUSAL-EVIDENCE ROLE
```

Do not assume the roles are identical because the dashboard uses the same event noun.

LinkedIn documents configurations where optimization goal and chargeable event differ [PM08][PM09].

Keep:

```text
BILLING EVENT
≠ OPTIMIZATION EVENT
```

### 5.2 Reported is not optimization-eligible

Google Ads data exclusions provide a concrete boundary: affected conversions can remain in reporting while being excluded from data Smart Bidding uses [PM02].

Freeze:

```text
REPORTED
≠ OPTIMIZATION-ELIGIBLE
```

When performance changes around measurement incidents, ask separately:

- what was logged;
- what remains visible in reporting;
- what was eligible for bidding/optimization;
- what historical period was affected;
- what conversion delay/maturity remains unresolved.

### 5.3 Measurement can participate in the control loop

TikTok states that view-through attributed conversions are among the signals used to optimize campaigns, and changing VTA availability can change system behavior while it adjusts to new signal sources [PM06].

Therefore:

```text
MEASUREMENT / ATTRIBUTION
≠ PASSIVE REPORTING ONLY
```

and:

```text
OBSERVATION
≠ AUTOMATIC OPTIMIZATION FEEDBACK
```

Ask whether this particular observation is actually fed back before reasoning about future delivery.

### 5.4 Time and maturity matter

An attributed conversion can arrive after the original ad interaction. Learning/adaptation can also make current system state depend on prior observations.

When material, preserve:

```text
event time
exposure / interaction time
attribution window
conversion delay / maturity
reporting time
control-change time
current delivery state
```

Do not compare partially matured and mature periods as if they were equivalent.

### 5.5 Attribution is not causality

Paid Media can establish:

```text
what was delivered
what was spent / billed
what event was observed
what rule attributed credit
what was eligible for optimization
what feedback entered future allocation
```

It does not establish:

```text
what would have happened without the paid exposure
what outcome the exposure incrementally caused
what marginal incremental return a spend change will cause
```

Freeze:

```text
ATTRIBUTED OUTCOME
≠ CAUSAL EFFECT
```

and:

```text
ROAS
≠ INCREMENTAL ROAS
```

Use Chapter 05 when the open decision depends on causal leverage or incrementality.

---

## 6. Owner boundaries and decision handoffs

Paid Media must remain a specialist, not a second marketing controller.

### Chapter 01 / 02

Own customer, segment, ICP, and market-demand inference.

```text
TARGET CUSTOMER
≠ PLATFORM-REACHED AUDIENCE
```

Paid audience telemetry does not redefine the market by itself.

### Chapter 04

Own ad message, claim, proof, and allowed communication.

Paid Media can identify that creative/destination allocation matters without deciding unsupported claims.

### Chapter 05

Own causal diagnosis, incrementality, experiments, and treatment effects.

When a metric moves and cause is unresolved, start there. Once the discriminating question reaches paid control/allocation/feedback semantics, load the smallest Paid Media route that can change the decision.

### Chapter 08

Own shared platform/content grammar. Paid Media specializes existing actor/object/representation/audience/edge/mediation/observation roles rather than extending them.

### Chapter 09

Own product/item/variant/listing/catalog/offer/shopper identity and commerce-specific state.

Retail-media paid delivery composes:

```text
Chapter 09 product/listing identity
+
Paid Media allocation/delivery semantics
```

Do not create a `SPONSORED_PRODUCT` primitive.

### Chapter 10

Own customer-facing Commercial Design for the offering.

Media procurement, publisher contracts, fixed CPM deals, bid/spend controls, or inventory buying do not become customer Commercial Design merely because money is involved.

### Chapter 11

Own landing-page information/action architecture after entry. Paid Media can reason about authorized destination selection without redesigning the page.

### Chapter 13

Own generic non-commerce discovery availability/retrieval/selection/representation semantics.

Do not flatten paid economic allocation into generic discovery relevance/ranking.

### Current-provider evidence

Provider objectives, products, controls, defaults, thresholds, auction/selection mechanics, billing, attribution windows, policy rules, and automation behavior are JIT dependencies. Preserve provider language such as `may`, `attempt`, `eligible`, `recommended`, `not guaranteed`, or `best effort` at its actual strength.

---

## 7. Compact paid-media decision record

Use a compact record only when retaining the decision will improve execution, review, or later diagnosis.

```text
PAID MEDIA DECISION

Decision / job:
- what is being chosen, interpreted, or held stable?

Objective / value:
- business/media value:
- horizon / material guardrails:
- platform objective / optimization signal:

Control / authority envelope:
- resource / budget / entitlement:
- constraints / exclusions:
- soft signals / suggestions:
- bid / cost / return controls:
- creative / destination / inventory authorization:
- obligations / guarantees:
- measurement / feedback rules:
- material scope / precedence / authority:

Allocation / realization:
- paid opportunity / inventory scope:
- buying / allocation mechanism:
- actual allocation boundary:
- current mediation / learning / pacing state:
- relevant recent transition:
- representation / placement / destination actually delivered where known:

Observation / feedback:
- delivered / rendered event:
- spend / billed event:
- attributed outcome:
- optimization-eligible signal:
- known optimization feedback:
- time / maturity / unit / modeling / coverage:

Causal status:
- descriptive / attributed only:
- causal evidence available or Chapter 05 dependency:

Decision / next discriminating check:
- action / hold / test / inspect / handoff:
```

Do not fill every field by default. Retain only dimensions whose omission would make materially different paid states look equivalent.

---

## 8. Anti-folklore invariants

Keep these distinctions when they prevent a material decision error:

```text
PAID RELATIONSHIP
≠ PAID MEDIA DELIVERY

SPONSORED CONTENT
≠ PAID AMPLIFICATION

PAID MEDIA
≠ AUCTION ONLY

BUSINESS VALUE
≠ PLATFORM OPTIMIZATION TARGET

TARGET CUSTOMER
≠ TARGETING SPECIFICATION
≠ REACHED AUDIENCE

HARD CONSTRAINT
≠ SOFT SIGNAL

CONTROL TYPE
≠ CONTROL PRECEDENCE

CAMPAIGN
≠ RESOURCE / OPTIMIZATION BOUNDARY

ADVERTISER SPECIFICATION
≠ PLATFORM EXECUTION

BUDGET
≠ ALLOCATION
≠ PACING
≠ BID
≠ SPEND

ELIGIBLE
≠ SELECTED
≠ DELIVERED

DELIVERED
≠ SEEN
≠ ATTENDED TO

REPORTED
≠ OPTIMIZATION-ELIGIBLE

BILLING EVENT
≠ OPTIMIZATION EVENT

ATTRIBUTED OUTCOME
≠ CAUSAL EFFECT

OBSERVATION
≠ AUTOMATIC OPTIMIZATION FEEDBACK

LEARNING STATE
≠ CAMPAIGN / CREATIVE QUALITY
```

Do not create a global paid audience, campaign state, optimization score, delivery score, universal auction formula, universal media funnel, universal attribution model, or universal media optimizer.

The purpose of this chapter is not to make advertising look more complicated. It is to prevent the practitioner from changing the wrong lever when paid delivery is being shaped by economic resource, platform controls, allocation mechanisms, adaptive state, measurement rules, and feedback rather than by creative alone.

# Paid Media Architecture — Theory Freeze

Status: **FROZEN FOR BOUNDED SPECIALIST IMPLEMENTATION**  
Freeze date: 2026-08-25  
Repository base: `main@70204aa47cefb29dad5ec449e28f515c9e29ec46`

## 1. Research question

Does paid media require a bounded specialist layer in Marketing Practitioner, or can the existing Chapters 04, 05, 08, 10, and 13 already support consequential paid-delivery decisions without material distortion?

The field exploration covered platform advertising, automated bidding, audience controls/signals, auction and non-auction buying, reserved/guaranteed inventory, budget allocation and pacing, learning/adaptive delivery state, placement selection, creative authorization/selection, retail media, creator paid amplification, DOOH/OOH exposure semantics, attribution, conversion feedback, and incrementality boundaries.

The adversarial requirement was strict:

> Do not add a shared primitive, new controller job, or specialist chapter merely because advertising is a large practitioner category. Add specialist knowledge only if concrete decision-relevant paid-delivery failures survive composition with the existing shared grammar and owner handoffs.

## 2. Freeze verdict

> **PAID MEDIA THEORY FREEZE PASSES ADVERSARIAL REFINEMENT.**  
> **BOUNDED SPECIALIST CAPABILITY CONFIRMED.**  
> **NO SHARED GRAMMAR REOPEN.**  
> **NO NEW SHARED PRIMITIVE.**  
> **NO NEW CONTROLLER JOB.**  
> **NO UNIVERSAL AUCTION / CAMPAIGN / TARGETING ONTOLOGY.**

The missing capability is a local specialist owner for paid control, paid allocation/realization, and paid observation/feedback semantics. The existing shared Chapter 08 grammar already has enough representation capacity.

## 3. Frozen activation boundary

Paid Media does **not** activate merely because money, an ad platform, a campaign, or sponsored content is mentioned.

Use the specialist when economic resource is being used to **secure, reserve, compete for, allocate, or amplify mediated audience exposure**, and the semantics of that paid delivery can change the decision.

Preserve:

```text
PAID RELATIONSHIP
≠ PAID MEDIA DELIVERY
```

and:

```text
SPONSORED CONTENT
≠ PAID AMPLIFICATION
```

Examples that do not automatically require Paid Media:

```text
pay creator to produce content
pay agency to design creative
pay copywriter
pay affiliate commission
```

Examples that can require Paid Media:

```text
buy / reserve inventory
compete for ad delivery
allocate budget across paid opportunities
amplify creator content with paid distribution
change bidding / pacing / paid audience controls
interpret paid delivery / billing / attribution feedback
```

## 4. Frozen primary unit

```text
PAID MEDIA DECISION
```

Do not use `campaign`, `ad`, `auction`, `audience`, `bid`, or `conversion` as the universal primary unit.

Freeze:

```text
CAMPAIGN
≠ DECISION UNIT
≠ RESOURCE BOUNDARY
≠ OPTIMIZATION BOUNDARY
```

A paid-media decision can concern optimization signals, audience-control semantics, buying mechanism, resource allocation, pacing, delivery state, creative/destination authorization, underdelivery, billing, attribution, or feedback without mapping one-to-one to one campaign object.

## 5. Frozen four-question model

### Q1 — Objective / decision value

Ask:

> What business or media value actually matters, under what horizon and material guardrails, and what signal or outcome is the delivery system actually instructed or permitted to optimize?

Preserve when material:

```text
BUSINESS VALUE / OUTCOME
≠ MEDIA JOB
≠ PLATFORM OBJECTIVE
≠ OPTIMIZATION SIGNAL / EVENT
```

A locally optimized platform event can diverge from the business outcome that matters. Do not treat a campaign objective, attributed ROAS, or conversion count as a complete business objective by default.

Authoritative margin, capacity, inventory, product, finance, legal, or operational constraints are dependencies when they can change the decision. Paid Media does not invent them.

If the open question becomes causal or incremental business impact — for example, what additional profit a spend increase would cause — use Chapter 05.

### Q2 — Control / authority envelope

Ask:

> What resources, constraints, signals, authorizations, obligations, and measurement rules shape paid execution, with what scope, authority, and precedence?

Useful local control semantics can include:

```text
RESOURCE
budget / inventory entitlement

CONSTRAINT
geo / schedule / frequency / exclusion / placement restriction

SIGNAL
suggested audience / customer list / contextual cue

OPTIMIZATION TARGET
purchase / value / lead / reach / another supported event

ECONOMIC CONTROL
bid strategy / cost target / return target / price condition

AUTHORIZATION
creative / representation / destination / inventory use

OBLIGATION
guaranteed delivery / contractual quantity / reserved commitment

MEASUREMENT / FEEDBACK RULE
conversion definition / attribution window / optimization-eligible observation
```

These are practitioner-facing semantics, **not new shared primitives**.

Freeze:

```text
HARD CONSTRAINT
≠ SOFT SIGNAL
```

and:

```text
CONTROL TYPE
≠ CONTROL PRECEDENCE
```

A field name or UI setting does not establish its absolute effect. Preserve scope, authority, priority, and competing obligations when they can change execution.

### Q3 — Allocation / realization state

Ask:

> What paid opportunities can participate, through which buying or allocation mechanism and boundary, under what current mediation state/history, and what authorized representation is actually delivered or rendered?

Use a broad allocation model. Paid media is not auction-only.

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

Mechanisms such as candidate retrieval, ranking, pacing, automated bidding, placement selection, or learning are system-specific implementations or mediation states, not shared primitives.

Preserve when material:

```text
BUDGET
≠ ALLOCATION POLICY
≠ PACING
≠ BID STRATEGY
≠ EXECUTED BID
≠ ACTUAL SPEND
```

and:

```text
ELIGIBLE
≠ CONSIDERED
≠ COMPETITIVE
≠ SELECTED
≠ DELIVERED / RENDERED
```

Also preserve:

```text
ADVERTISER SPECIFICATION
≠ PLATFORM-HELD STATE
≠ PLATFORM EXECUTION
```

A platform can interpret advertiser inputs, expand or constrain opportunities, allocate resources, choose placements, select/generate authorized creative combinations, or choose an authorized destination without making those executed choices identical to the advertiser's original specification.

History matters. A learning/adaptive phase is a local `PLATFORM / MEDIATION STATE + HISTORY / STATE TRANSITION`, not a new primitive.

### Q4 — Observation / feedback

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

A reported event can remain visible in analytics while being excluded from bidding/optimization. A measurement or attribution rule can sometimes participate in the delivery control loop instead of serving as passive reporting only.

Therefore:

```text
REPORTED
≠ OPTIMIZATION-ELIGIBLE
```

and:

```text
OBSERVATION
≠ AUTOMATIC OPTIMIZATION FEEDBACK
```

Paid Media owns the semantics of what was delivered, billed, attributed, and fed back. Chapter 05 owns counterfactual effect, incrementality, experiments, and causal leverage.

## 6. Frozen decision loop

Do not freeze a universal campaign funnel or platform pipeline.

```text
BUSINESS / MEDIA DECISION VALUE
        ↓
CONTROL / AUTHORITY ENVELOPE
        ↓
PAID ALLOCATION / REALIZATION
        ↓
OBSERVATION / ATTRIBUTION / FEEDBACK
        ↺
        ↓
CAUSAL EFFECT / INCREMENTALITY
        → Chapter 05
```

This is a practitioner dependency model, not a claim that every ad system executes these stages linearly.

A guaranteed reservation can realize exposure without an auction. An automated social-ad system can use retrieval, prediction, auction/ranking, pacing, and continuous feedback. Static or digital OOH can use scheduled/location-based allocation and modeled exposure. The same four-question grammar must remain valid across these differences.

## 7. Exposure discipline

Do not treat system delivery as verified human attention.

Freeze:

```text
DELIVERED / RENDERED
≠ OPPORTUNITY TO SEE
≠ LIKELY SEEN
≠ VERIFIED HUMAN ATTENTION
```

For person-level, device-level, household-level, location-level, or modeled measurements, preserve the observation unit and identity/coverage basis when they can change interpretation.

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

No new `EXPOSURE` primitive is justified. Use existing representation, delivery edge, audience state, mediation state, observation, provenance, scope, and history.

## 8. Audience and targeting discipline

Do not collapse strategic customer definition into platform execution.

Freeze:

```text
TARGET CUSTOMER
≠ DESIRED MEDIA AUDIENCE
≠ ADVERTISER TARGETING SPECIFICATION
≠ PLATFORM AUDIENCE SIGNAL
≠ ELIGIBLE POPULATION
≠ ACTUALLY REACHED PEOPLE
```

A targeting input can be a hard constraint, a soft signal, a suggestion, an exclusion, or another scoped control depending on the provider and product state.

Paid Media must not infer that the platform reached only the marketer's declared target merely because that target was supplied as an input.

## 9. Buying / auction discipline

Freeze:

```text
PAID MEDIA
≠ AUCTION ONLY
```

and, where an auction exists:

```text
BID STRATEGY
≠ EXECUTED BID
≠ AUCTION VALUE / RANK
≠ FINAL COST
```

Do not create a universal auction model. Auction mechanics, clearing/pricing rules, quality/relevance factors, private marketplaces, reserved inventory, guaranteed deals, and fixed-rate buys remain system-specific evidence.

## 10. Representation and creative boundary

Chapter 04 continues to own what the marketer may claim, with what message and proof.

Chapter 08 continues to own the shared object/representation grammar.

Paid Media owns only the paid-delivery consequence:

```text
WHICH AUTHORIZED REPRESENTATION
CAN PARTICIPATE
AND WHICH IS ACTUALLY DELIVERED
UNDER THE CURRENT PAID CONTROL / ALLOCATION STATE
```

A platform may select, recombine, or generate authorized creative variants. That does not give Paid Media permission to invent claims or proof that Chapter 04 would reject.

For destinations, Chapter 11 owns landing-page architecture after entry. Paid Media can reason about which authorized destination the delivery system selects without becoming the landing-page owner.

## 11. Creator / sponsorship boundary

Paid Media must not absorb the whole creator economy.

Freeze:

```text
SPONSORED CONTENT
≠ PAID AMPLIFICATION
```

A brand paying a creator to produce/publish content can primarily require creator relationship, authority, disclosure, message, proof, or content-environment reasoning.

When economic resource is then used to amplify that content through a paid distribution system, Paid Media can own the amplification control/allocation/delivery semantics.

## 12. Observation and causal boundary

Paid Media can establish:

```text
what paid delivery occurred
what resource was spent / billed
what event definition was observed
what attribution rule assigned credit
what observations were eligible for optimization
what feedback entered future allocation
```

It does not establish:

```text
what would have happened without the paid exposure
what outcome the paid exposure incrementally caused
what marginal incremental return a spend change will cause
```

Use Chapter 05 for causal diagnosis, incrementality, experiments, and treatment effects.

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

## 13. Owner boundaries

### Chapter 01 / 02

Own customer, segment, ICP, and market-demand inference. Paid targeting/reach telemetry does not redefine the target customer by itself.

### Chapter 04

Own ad message, claim, proof, and allowed communication.

### Chapter 05

Own causal diagnosis, attribution-vs-incrementality, experiments, and causal resource-allocation decisions.

### Chapter 08

Own the shared parent grammar:

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

Paid Media specializes the interpretation of those roles; it does not replace or expand the shared grammar.

### Chapter 09

Own product/item/variant/listing/catalog/offer/shopper identity and commerce-specific state. Retail media can compose product identity from Chapter 09 with paid allocation semantics without creating a sponsored-product primitive.

### Chapter 10

Own customer-facing Commercial Design for the offering. Media procurement, ad inventory buying, bid/spend control, or publisher contracts do not become customer Commercial Design merely because money is involved.

### Chapter 11

Own landing-page information/action architecture after entry. Paid Media can own destination selection/allocation semantics when the platform chooses among authorized destinations.

### Chapter 13

Own generic non-commerce discovery availability/retrieval/selection/representation semantics. Paid economic allocation must not be flattened into generic discovery relevance/ranking.

### Paid Media specialist

Owns only:

```text
business/media objective vs platform optimization semantics
paid control / authority envelope
paid opportunity and buying/allocation semantics
resource allocation / pacing / execution interpretation
paid delivery / rendering / exposure semantics
billing / attribution / optimization-feedback semantics
```

## 14. Explicit non-goals

Do not create:

```text
CAMPAIGN primitive
AD primitive
AUCTION primitive
BID primitive
TARGETING primitive
LEARNING primitive
FEEDBACK primitive
EXPOSURE primitive

GLOBAL PAID AUDIENCE object
GLOBAL CAMPAIGN STATE
global optimization score
global delivery score

universal ad auction model
universal media funnel
universal attribution model
universal media optimizer

Meta Ads ontology
Google Ads ontology
TikTok Ads ontology
LinkedIn Ads ontology
```

Current provider objectives, bid strategies, audience controls, auction rules, placement systems, learning-state definitions, pricing/billing semantics, attribution windows, measurement definitions, policy constraints, and automated-creative capabilities are authoritative just-in-time dependencies rather than timeless primitives.

## 15. Fast-path implication

Mentioning `Facebook Ads`, `Google Ads`, `TikTok Ads`, `campaign`, `CPC`, `CPA`, `ROAS`, or another advertising noun must not automatically activate deep Paid Media knowledge.

Examples:

```text
"Shorten this approved ad headline to 30 characters."
→ supplied transformation
→ stay on the fast path
```

But:

```text
"CPA rose after we changed the optimization event and budget.
Should we rewrite the creative?"
→ causal diagnosis may begin in Chapter 05
→ Paid Media becomes material if control / allocation / delivery semantics
   can change the decision
→ Chapter 04 only if message / creative is actually implicated
```

A bounded namespace such as `paid-media.*` is justified for implementation, but exact route count is an implementation detail.

## 16. Frozen anti-folklore core

Keep these distinctions when they prevent a material decision error:

```text
PAID RELATIONSHIP
≠ PAID MEDIA DELIVERY

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
```

## 17. Final freeze statement

```text
FIELD DISCOVERY                     PASS
DEEP DIVES                          PASS
CROSS-FIELD SYNTHESIS               PASS
ADVERSARIAL ATTACK                  PASS
CURRENT-SYSTEM GAP                  CONFIRMED
MINIMAL THEORY                      PASS
FINAL COUNTEREXAMPLE ATTACK         PASS

BOUNDED SPECIALIST CAPABILITY       CONFIRMED
SHARED GRAMMAR REOPEN               NO
NEW SHARED PRIMITIVE                NO
NEW CONTROLLER JOB                  NO
UNIVERSAL AUCTION / CAMPAIGN MODEL  REJECTED

PRIMARY UNIT
→ PAID MEDIA DECISION

FROZEN MODEL
→ OBJECTIVE / DECISION VALUE
→ CONTROL / AUTHORITY ENVELOPE
→ ALLOCATION / REALIZATION STATE
→ OBSERVATION / FEEDBACK
```

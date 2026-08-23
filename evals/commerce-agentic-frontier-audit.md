# Commerce Agentic-Frontier Adversarial Audit

Reviewed: 2026-08-23

Status: **targeted research/adversarial audit, not benchmark/eval score**.

Purpose: test the targeted agentic-commerce extension added after the classic marketplace knowledge layer had already passed the 23-case architecture audit. This pass asks whether delegated authority, agent-facing product data, checkout/order authority, external-store discovery, and 2026 conversational commerce require a new durable primitive or expose a material gap in Chapter 09 / Google / Amazon.

## Frozen dependency

The earlier artifact remains unchanged:

```text
evals/commerce-environment-adversarial-audit.md
```

Its frozen score was:

```text
23 total
15 LOSSLESS
7 LOSSLESS / INTERNAL UNKNOWN
1 RUNTIME UNTESTED
0 PARTIAL
0 FAIL
```

The later routing smoke already closed the historical runtime-untested gate without rewriting that artifact.

## Regression pass over the 23 legacy cases

All 23 frozen cases were re-walked against the extended Chapter 09 and updated Google/Amazon modules.

The frontier patch is additive and preserves the prior encodings:

- product / platform-record distinctions remain conditional rather than universal;
- actor/object analytical roles remain non-disjoint;
- descriptive / commercial / observational context remains separated;
- `OBJECT / REPRESENTATION / TYPED EDGE / STATE + provenance/scope/history` remains the parent grammar;
- fast-path product communication remains explicit;
- no prior platform-specific ranking UNKNOWN was converted into a known law.

**Regression verdict: 23 / 23 legacy cases preserve their prior result; 0 regressions.**

---

# 1. Delegated authority and effect

## F1 — Shopper intent is not purchase authority

**Stress case**

A shopper tells an agent:

> Find me a laptop under $1,000.

The agent has technical checkout capability.

**Required distinction**

The discovery request does not itself authorize a purchase.

**Encoding**

```text
actor A       = shopper
actor B       = shopping agent / platform
interaction   = discovery request
permission edge = absent for purchase unless separately granted
platform state  = checkout capability exists
scope           = search / recommendation only
```

**Preserved distinction**

```text
SHOPPER INTENT
≠ DELEGATED ACTION AUTHORITY
```

**Verdict: LOSSLESS**

## F2 — Capability is not authorization

**Stress case**

A platform supports a checkout API, but the current checkout is standard UCP without AP2 Mandates and still requires user finalization through trusted UI.

**Encoding**

```text
platform state = checkout capability available
authorization state = user finalization still required
permission edge = not autonomous
```

**Preserved distinction**

```text
PLATFORM CAPABILITY
≠ USER AUTHORIZATION
```

**Verdict: LOSSLESS**

## F3 — Authority is scoped to transaction state

**Stress case**

User authorizes purchase only if total is at most $1,000. Checkout later becomes $1,028 after shipping.

**Encoding**

```text
permission edge:
user --[authorizes purchase]--> agent
scope.total_max = 1000
currency = USD

checkout state at t1 = 1028
history = authorized state → changed state
```

Current state violates the prior authorization scope.

**Preserved distinction**

```text
AUTHORIZATION OF STATE S0
≠ AUTHORIZATION OF MATERIALLY CHANGED STATE S1
```

The exact re-authorization UX/protocol remains platform-specific.

**Verdict: LOSSLESS**

---

# 2. Discovery, checkout, order, and effect

## F4 — Discovery state can become stale before checkout

**Stress case**

At discovery time a feed representation says:

```text
price = $89
size 42 = in stock
```

At checkout the merchant returns:

```text
price = $94
shipping = $8
size 42 = out of stock
```

**Encoding**

```text
representation A = discovery / indexed product state @ t0
representation B = authoritative checkout state @ t1
provenance A = merchant feed / indexed state
provenance B = merchant checkout response
history = t0 → t1
```

**Preserved distinction**

```text
DISCOVERY / INDEX STATE
≠ AUTHORITATIVE CHECKOUT STATE
```

A merchant feed can still be authoritative product-data input for discovery; the error would be treating that earlier snapshot as timeless transaction truth.

**Verdict: LOSSLESS**

## F5 — Checkout session is not accepted/completed order

**Stress case**

An agent creates a checkout session and submits completion, but merchant acceptance/payment/order creation has not yet been confirmed.

**Encoding**

```text
checkout object/state = created / submitted
merchant effect state = not yet confirmed
order object/state = absent / pending confirmation
payment state = independent
```

**Preserved distinction**

```text
CHECKOUT REQUEST / SESSION
≠ MERCHANT-ACCEPTED ORDER
≠ PAYMENT SUCCESS
≠ FULFILLMENT COMPLETION
```

**Verdict: LOSSLESS**

## F6 — Order remains a changing post-checkout state

**Stress case**

An accepted order later receives fulfillment events, an item adjustment, and a partial refund.

**Encoding**

```text
object = order
state = authoritative current snapshot
events = fulfillment / adjustment history
scope = post-purchase
```

No new lifecycle primitive is needed.

**Verdict: LOSSLESS**

---

# 3. Representation and actor-role frontier

## F7 — Agent-facing representation is not the human answer

**Stress case**

An agent queries a structured catalog containing IDs, variants, offers, availability, currency, and buyer context, then presents a short recommendation to the user.

**Encoding**

```text
object = product / variant
representation A = agent-consumable catalog response
representation B = human-facing generated recommendation
surface = conversational UI
```

**Preserved distinction**

```text
AGENT-CONSUMABLE REPRESENTATION
≠ HUMAN-FACING GENERATED REPRESENTATION
```

**Verdict: LOSSLESS**

## F8 — Checkout surface is not Merchant of Record / payment / fulfillment

**Stress case**

A shopper completes a mediated checkout inside an AI/search surface while the merchant remains seller/Merchant of Record and another payment system handles payment credentials/processing.

**Encoding**

```text
actor A = platform / checkout mediator
actor B = merchant / seller of record
actor C = payment provider / handler
actor D = fulfillment / support provider where distinct
surface = AI / conversational checkout
relations = typed commercial / payment / fulfillment roles
```

**Preserved distinction**

```text
ENCOUNTER / CHECKOUT SURFACE
≠ MERCHANT OF RECORD
≠ PAYMENT ROLE
≠ FULFILLMENT / SUPPORT ROLE
```

**Verdict: LOSSLESS**

---

# 4. Platform corrections

## F9 — Amazon discovery can escape the native Store catalog/listing/offer regime

**Stress case**

A customer sees a Shop Direct product in Amazon discovery even though the item is sold by an external merchant; the user can be referred to the merchant site or use Buy for Me where eligible.

**Encoding**

```text
object = external merchant product / feed role
representation = Amazon Shop Direct discovery representation
commercial actor = external merchant
edge / route A = referral to merchant site
edge / route B = Buy for Me agentic purchase
```

The case does not require a native seller listing / offer / PDP identity.

**Preserved distinction**

```text
AMAZON PRODUCT DISCOVERY
≠ NECESSARILY NATIVE AMAZON STORE REGIME
```

Unknown remains: exact internal Amazon normalization/identifier and retrieval/ranking architecture for Shop Direct.

**Verdict: LOSSLESS / INTERNAL UNKNOWN**

## F10 — Google `popularity_rank` cannot become Google organic rank

**Stress case**

Merchant submits:

```text
popularity_rank = 95.5
```

A practitioner interprets it as “Google ranks this product at 95.5.”

**Encoding**

```text
seller field = merchant-declared relative sales performance
scope = merchant inventory
platform organic rank = separate / undisclosed
```

**Preserved distinction**

```text
MERCHANT-DECLARED POPULARITY_RANK
≠ GOOGLE ORGANIC SEARCH RANK
```

**Verdict: LOSSLESS**

## F11 — Google declared product relation is not inferred relation

**Stress case**

Merchant declares product B as a substitute/accessory for product A using `related_product`.

**Encoding**

```text
object A / B = products
edge = merchant-declared related-product relation
provenance = merchant declaration
platform-inferred relation = separate / unknown
behavioral co-purchase relation = separate observation-derived edge
```

**Preserved distinction**

```text
MERCHANT-DECLARED PRODUCT RELATION
≠ PLATFORM-INFERRED RELATION
≠ OBSERVED CO-PURCHASE RELATION
```

**Verdict: LOSSLESS**

## F12 — Google AI checkout does not transfer seller-of-record role

**Stress case**

An eligible buyer checks out from AI Mode / Gemini using UCP-powered checkout.

**Encoding**

```text
surface / mediator = Google AI Mode / Gemini
seller / MoR = participating merchant
payment role = Google Pay / handler where applicable
merchant backend = checkout/order authority
```

**Preserved distinction**

```text
GOOGLE CHECKOUT SURFACE
≠ GOOGLE IS SELLER OF RECORD
```

Exact rollout/eligibility and some transaction mechanics remain time-sensitive.

**Verdict: LOSSLESS / INTERNAL UNKNOWN**

---

# 5. Core attack

## X1 — Does agentic commerce require a new durable primitive?

Tested candidates:

```text
shopping agent
delegated authority / mandate
checkout session
order
payment handler
merchant of record
agent-facing product representation
```

All tested cases remain representable as:

```text
ACTOR / SOURCE
OBJECT
REPRESENTATION
TYPED EDGE / PERMISSION EDGE
INTERACTION ACT
PLATFORM / MEDIATION STATE
OBSERVATION RECORD
+ provenance / scope / history
```

Examples:

- shopping agent → actor role;
- delegated authority → typed permission edge + scope/state;
- checkout/order → object/state roles when independently addressable;
- payment/MoR/fulfillment → actor + typed commercial roles;
- agent-facing data → representation role.

**Verdict: NO NEW DURABLE PRIMITIVE REQUIRED**

---

# 6. Frontier scorecard

| Area | Cases | LOSSLESS | LOSSLESS / INTERNAL UNKNOWN | PARTIAL | FAIL |
| --- | ---: | ---: | ---: | ---: | ---: |
| Delegated authority | 3 | 3 | 0 | 0 | 0 |
| Checkout / order state | 3 | 3 | 0 | 0 | 0 |
| Representation / actor roles | 2 | 2 | 0 | 0 | 0 |
| Platform corrections | 4 | 2 | 2 | 0 | 0 |
| Core attack | 1 | 1 | 0 | 0 | 0 |
| **Frontier total** | **13** | **11** | **2** | **0** | **0** |

Legacy regression:

```text
23 / 23 prior cases preserve their frozen result
0 regressions
```

Combined research surface now stress-tests 36 cases without a PARTIAL or FAIL, while retaining explicit UNKNOWNs for undisclosed/current platform internals.

This count is **not** a benchmark score or statistical reliability claim.

---

# 7. Verdict

```text
C4 / NEW DURABLE PRIMITIVE
NO

SECOND AGENTIC-COMMERCE ONTOLOGY
NO

CHAPTER 09 CORE FAILURE
NO

TARGETED CHAPTER 09 DEPTH EXTENSION
SURVIVES

GOOGLE CONVERSATIONAL / UCP EXTENSION
SURVIVES

AMAZON SHOP DIRECT / BUY FOR ME CORRECTION
SURVIVES

LEGACY COMMERCE ARCHITECTURE REGRESSION
NONE FOUND
```

**Gate recommendation: RUN FRESH ROUTING / USER-FACING SMOKE FOR THE FRONTIER CASES, THEN RETURN PR #7 TO INDEPENDENT REVIEW.**

Do not reopen broad commerce ontology research unless a concrete counterexample survives this parent grammar with a material decision-relevant collapse.

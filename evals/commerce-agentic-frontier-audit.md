# Commerce Agentic-Frontier Adversarial Audit

Reviewed: 2026-08-23

Status: **targeted research/adversarial audit, not benchmark/eval score**.

> **Post-review addendum:** an independent review of later frozen head `1bcc0f653d0f14031e8209c77de51e518d66302a` found one Etsy source-fidelity defect not exposed by this audit: current official Etsy sources conflict on whether description/broader listing data participate in query matching. That defect did not change the 8+3 architecture verdict, but it did require a targeted evidence correction. See `commerce-etsy-query-matching-source-conflict-correction.md`. The original frontier scorecard below should therefore be read as an architecture/representation result, **not proof that every platform evidence boundary had been exhaustively adjudicated**.

Purpose: attack the frozen commerce specialization with 2026 agent-mediated / delegated-commerce cases after classic marketplace integration, while checking that the existing 8 + 3 parent grammar still represents the new authority, checkout, order, and agent-facing representation distinctions without a new durable primitive.

This audit also regression-walks the prior 23 commerce cases conceptually. It does not rewrite the historical pre-router audit.

## Frontier under test

```text
SHOPPER INTENT
≠ DELEGATED ACTION AUTHORITY

PLATFORM / AGENT CAPABILITY
≠ USER AUTHORIZATION
≠ SUCCESSFUL EFFECT

DISCOVERY / INDEX STATE
≠ AUTHORITATIVE CHECKOUT STATE
≠ AUTHORITATIVE ORDER STATE

CHECKOUT REQUEST / SESSION
≠ MERCHANT-ACCEPTED ORDER
≠ PAYMENT / FULFILLMENT COMPLETION

AGENT-CONSUMABLE REPRESENTATION
≠ HUMAN-FACING GENERATED REPRESENTATION

ENCOUNTER / CHECKOUT SURFACE
≠ MERCHANT OF RECORD
≠ PAYMENT / FULFILLMENT RESPONSIBILITY
```

Evidence:

```text
references/commerce/agentic-commerce-evidence.md
references/commerce/google-shopping-evidence.md
references/commerce/amazon-evidence.md
```

---

# 1. Delegated authority attacks

## D1 — Search intent must not authorize purchase

**Stress case**

The user says:

> Find me a laptop under $1,000. Do not buy anything.

The agent/system is technically capable of checkout.

**Encoding**

```text
actor A        = user
actor B        = shopping agent / platform
interaction    = discovery request
permission edge = no purchase authority
capability state = checkout technically supported
scope          = search / recommend only
```

**Preserved distinction**

```text
DISCOVERY INTENT
≠ PURCHASE AUTHORITY

TECHNICAL CAPABILITY
≠ AUTHORIZED OPERATION
```

**Verdict: LOSSLESS**

## D2 — Authorization scope must fail when checkout state exceeds it

**Stress case**

The user authorizes purchase up to `$1,000`. At checkout, shipping makes the total `$1,028`.

**Encoding**

```text
permission edge = purchase authorization
scope           = total <= $1,000
checkout state  = $1,028
history         = authorized state → changed state
```

**Preserved distinction**

```text
AUTHORIZATION OF STATE S0
≠ AUTHORIZATION OF MATERIAL STATE S1
```

**Verdict: LOSSLESS**

## D3 — Product substitution can invalidate product-bound authority

**Stress case**

The user authorizes product A. The merchant or agent proposes product B because A is unavailable.

**Encoding**

```text
permission scope = product A
checkout state   = product B substituted
history          = original → substituted state
```

**Preserved distinction**

```text
AUTHORIZED PRODUCT
≠ SUBSTITUTE PRODUCT
```

No new `MANDATE` primitive is required; the scope belongs to the permission edge / state.

**Verdict: LOSSLESS**

---

# 2. Checkout and order-state attacks

## T1 — Discovery price is stale by checkout

**Stress case**

The agent discovers product at `$89`. Seven minutes later the merchant checkout returns `$94`, `$8` shipping, and size 42 unavailable.

**Encoding**

```text
discovery representation @ t0 = $89 / size 42 available
checkout state @ t1           = $94 + $8 / size 42 unavailable
provenance                     = discovery feed vs merchant checkout
```

**Preserved distinction**

```text
DISCOVERY SNAPSHOT
≠ CURRENT TRANSACTION TRUTH
```

**Verdict: LOSSLESS**

## T2 — Checkout submitted is not accepted/completed order

**Stress case**

An agent submits checkout, then the merchant rejects the order.

**Encoding**

```text
checkout object/state = submitted
merchant interaction  = rejected
order state            = no accepted order
history                = submitted → rejected
```

**Preserved distinction**

```text
REQUEST SUBMITTED
≠ MERCHANT-ACCEPTED ORDER
```

**Verdict: LOSSLESS**

## T3 — Payment / fulfillment can fail after merchant acceptance

**Stress case**

Merchant accepts order, payment later fails; or payment succeeds and fulfillment later fails/cancels.

**Encoding**

```text
order state       = accepted
payment state     = success / failure
fulfillment state = pending / failed / cancelled / completed
history           = independent transitions
```

**Preserved distinction**

```text
ORDER ACCEPTED
≠ PAYMENT SUCCESS
≠ FULFILLMENT COMPLETION
```

**Verdict: LOSSLESS**

---

# 3. Representation and actor-role attacks

## R1 — Agent-facing representation conflicts with human-facing summary

**Stress case**

Agent catalog data says `battery = 10 hours`. The generated human recommendation says `all-day battery life` without evidence for that stronger claim.

**Encoding**

```text
representation A = agent-consumable structured fact
representation B = human-facing generated summary
provenance        = merchant/catalog vs agent generation
claim boundary    = 10 hours only
```

**Preserved distinction**

```text
AGENT INPUT REPRESENTATION
≠ HUMAN OUTPUT REPRESENTATION

SOURCE FACT
≠ STRONGER GENERATED CLAIM
```

**Verdict: LOSSLESS**

## R2 — Checkout surface is not Merchant of Record

**Stress case**

Buyer completes checkout inside an AI/search interface while the merchant remains seller of record and another provider handles payment rails.

**Encoding**

```text
actor/platform = encounter + checkout mediator
actor/merchant = seller / Merchant of Record
actor/payment  = payment-processing role
actor/logistics = fulfillment role where separate
```

**Preserved distinction**

```text
ENCOUNTER SURFACE
≠ SELLER OF RECORD
≠ PAYMENT ROLE
≠ FULFILLMENT ROLE
```

**Verdict: LOSSLESS**

---

# 4. Platform-correction attacks

## P1 — Google `popularity_rank` must not become Google organic rank

**Stress case**

A merchant sets:

```text
popularity_rank = 95.5
```

and asks whether Google now ranks the product at 95.5.

**Encoding**

```text
source representation = merchant conversational attribute
field semantic         = merchant-relative selling-performance context
unknown                = organic rank relationship
```

**Preserved distinction**

```text
MERCHANT-DECLARED POPULARITY RANK
≠ GOOGLE ORGANIC SEARCH / SHOPPING RANK
```

**Verdict: LOSSLESS**

## P2 — Merchant-declared related product is not inferred relation

**Stress case**

Merchant marks B as substitute for A. Platform behavior also shows A and C are often co-purchased.

**Encoding**

```text
edge A→B = merchant-declared substitute
provenance = merchant

edge A→C = observed / platform-derived co-purchase relation
provenance = behavior / platform
```

**Preserved distinction**

```text
DECLARED PRODUCT RELATION
≠ INFERRED / OBSERVED PRODUCT RELATION
```

**Verdict: LOSSLESS**

## P3 — Amazon Shop Direct product must not be forced through native Store listing model

**Stress case**

An external merchant product appears in Amazon Shop Direct, can link to the merchant website, and may be eligible for Buy for Me.

**Encoding**

```text
object/state = external merchant product / feed representation
platform representation = Amazon Shop Direct result
edge          = referral to external merchant OR Buy for Me mediation
merchant role = external commercial responsibility
unknown       = exact Amazon internal normalization / identifier
```

**Preserved distinction**

```text
AMAZON DISCOVERY
≠ NECESSARILY NATIVE STORE ASIN + SELLER LISTING + OFFER REGIME
```

**Verdict: LOSSLESS / INTERNAL UNKNOWN**

## P4 — Shop Direct cannot justify hidden-ASIN claims

**Stress case**

User asks:

> Does every Shop Direct item definitely have no ASIN anywhere inside Amazon?

**Encoding**

```text
public evidence = external-store discovery / feeds / referral / Buy for Me
internal ID state = unknown
```

**Required behavior**

```text
DO NOT INFER
PUBLIC EXTERNAL-STORE REGIME
→ NO INTERNAL AMAZON IDENTIFIER EXISTS
```

**Verdict: LOSSLESS / INTERNAL UNKNOWN**

---

# 5. Core-cardinality attack

## C1 — Does agentic commerce require a ninth durable thing?

Tested candidates:

```text
shopping agent
mandate
authorization grant
checkout session
order
payment
fulfillment
```

All tested cases remain representable through the existing grammar:

- shopping agent → `ACTOR`;
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

This count is **not** a benchmark score or statistical reliability claim, and the post-review Etsy addendum above demonstrates why `0 PARTIAL / 0 FAIL` must not be read as proof that source-fidelity conflicts cannot still be found.

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

POST-REVIEW ETSY SOURCE-FIDELITY DEFECT
SEE TARGETED CORRECTION ARTIFACT
```

**Gate recommendation after the Etsy correction: RETURN THE NEW PR #7 HEAD TO INDEPENDENT ADVERSARIAL REVIEW.**

Do not reopen broad commerce ontology research unless a concrete counterexample survives this parent grammar with a material decision-relevant collapse.

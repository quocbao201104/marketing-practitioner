# Commerce Agentic-Frontier Runtime Smoke

Reviewed: 2026-08-23

Status: **targeted integration smoke, not benchmark/eval score**.

> **Post-review note:** an independent review later found an Etsy source-fidelity conflict about description/query-matching participation. That issue is outside the agentic-routing cases in this smoke and did not require a router change. See `commerce-etsy-query-matching-source-conflict-correction.md` for the targeted repair. The existence of that correction is also a reminder that passing smoke cases do not establish exhaustive evidence correctness.

Purpose: verify that the targeted 2026 agentic-commerce frontier extension preserves prior commerce routing while correctly handling delegated authority, transaction-state authority, agent-facing representations, Google conversational-attribute folklore traps, and Amazon Shop Direct / Buy for Me distinctions.

The recorded outputs below are user-facing answer shapes, not hidden reasoning.

---

# A. Static routing regression

The router must still preserve:

```text
SIMPLE PRODUCT COMMUNICATION
→ fast path
→ no Chapter 09 unless deeper structure matters

PLATFORM FIELD SEMANTICS ONLY
→ smallest relevant commerce module
→ no full Chapter 09 graph by default

DEEP COMMERCE / AGENTIC AUTHORITY
→ Chapter 09
→ platform module only when platform-specific behavior matters

HYBRID CONTENT × COMMERCE
→ Chapter 08 + Chapter 09 only when both relations matter
```

**Static result: PASS**

No broad `ANY COMMERCE → Chapter 09` route was introduced.

---

# B. Legacy smoke regression

The four original smoke families were re-walked against the new head.

## L1 — OVER-ROUTING: simple Shopee title

**Prompt**

> Product facts: mini blender, 300 ml, USB-C charging, 6 blades, white. Write a Shopee product title. Do not invent anything.

**Expected / observed route**

```text
commerce activation
→ narrow title job
→ Shopee module only if current field semantics matter
→ skip Chapter 09 deep graph
→ skip agentic section
```

**User-facing result**

> Máy Xay Sinh Tố Mini 300ml USB-C 6 Lưỡi, Màu Trắng

**Verdict: PASS**

## L2 — UNDER-ROUTING: Amazon seller field differs from PDP

**Prompt**

> My Amazon seller listing says “12-pack” but the live PDP for the ASIN shows “6-pack”. Is my title update broken?

**Required distinction**

```text
seller listing / contribution
≠ Amazon catalog state
≠ displayed PDP
```

**Verdict: PASS**

## L3 — FOLKLORE LEAKAGE: Lazada key attribute

**Prompt**

> Lazada marks an attribute as `is_key_prop=1`. If I fill it in, does that mean my product will rank higher organically?

**Required behavior**

```text
documented product/item score
≠ established organic ranking score
```

**Verdict: PASS**

## L4 — EVIDENCE COLLAPSE: Shopee displayed price

**Prompt**

> Shopee shows me a lower price than the seller's base price. Does that mean the seller secretly reduced the price for everyone?

**Required behavior**

```text
base / variant price
≠ buyer-relative displayed price
≠ final checkout price
```

**Verdict: PASS**

Legacy regression: **4 / 4 PASS**

---

# C. Frontier smoke

## F1 — Intent ≠ purchase authority

**Prompt**

> Find me a laptop under $1,000. Do not buy anything. The shopping agent supports automatic checkout.

**Route used**

```text
job = agent-mediated commerce authority
load = Chapter 09 agentic section
platform module = not required
```

**User-facing result**

> The agent's ability to check out does not authorize it to buy. Your instruction authorizes product discovery within the $1,000 constraint and explicitly withholds purchase authority. It can search and recommend, but it should stop before any transaction that would commit an order or payment unless you give a separate authorization.

**Verdict: PASS**

---

## F2 — Authorization-scope drift

**Prompt**

> I authorized an agent to buy this item if the total is no more than $100. Checkout is now $109 after shipping. Can it continue under the old authorization?

**User-facing result**

> Not under that authorization. The $100 ceiling is part of the delegated scope, and the current $109 checkout state is outside it. The earlier authorization should not silently carry over to the changed transaction; the system needs a new user decision under the current total unless the applicable protocol explicitly defines another valid authorization path.

**Verdict: PASS**

---

## F3 — Discovery snapshot ≠ checkout truth

**Prompt**

> The AI showed a shoe at $89 and in stock. Seven minutes later checkout says $94, $8 shipping, and size 42 is unavailable. Which state should I treat as current?

**User-facing result**

> Treat the merchant's current checkout state as authoritative for this transaction. The $89/in-stock result was a discovery snapshot from an earlier time; it should not override the later checkout price, shipping, or variant availability. If the changed state matters to the decision, present it and re-confirm rather than treating the discovery representation as transaction truth.

**Verdict: PASS**

---

## F4 — Google `popularity_rank` folklore trap

**Prompt**

> I set `popularity_rank=95.5` in Google Merchant Center. Does that mean Google ranks my product at 95.5 organically?

**Route used**

```text
job = field-semantics / ranking-claim check
load = Google commerce module
Chapter 09 = only evidence-boundary distinction as needed
```

**User-facing result**

> No. Google's `popularity_rank` conversational attribute is merchant-supplied context about how well the product sells relative to the merchant's own products. It is not a disclosed Google organic Search or Shopping rank score. Do not interpret `95.5` as Google's ranking position or as proof of a fixed organic boost.

**Verdict: PASS**

---

## F5 — Amazon Shop Direct must not collapse into native Store model

**Prompt**

> I found my product through Amazon Shop Direct but it is sold on my own website. Should I diagnose it as an ASIN/seller-listing/Featured-Offer problem?

**User-facing result**

> Not by default. Amazon now has an external-store Shop Direct regime that can surface merchant products and send shoppers to the merchant website or use Buy for Me for eligible purchases. First establish whether this exposure is Shop Direct/external-store rather than a native Amazon Store listing. Only use ASIN/seller-SKU/Featured-Offer diagnostics when the product is actually participating in that native Store regime. Amazon's exact internal normalization for Shop Direct remains undisclosed.

**Verdict: PASS**

---

## F6 — Encounter surface ≠ merchant responsibility

**Prompt**

> A shopper checked out inside an AI/search interface. Does that automatically make the interface provider the seller of record and fulfillment provider?

**User-facing result**

> No. The checkout surface, seller/Merchant of Record, payment processor, and fulfillment/support roles can be different actors. Identify the documented merchant and payment/fulfillment responsibilities for the specific checkout before attributing commercial responsibility to the interface where the shopper completed the action.

**Verdict: PASS**

---

## F7 — Checkout submitted ≠ completed order

**Prompt**

> The agent says “checkout submitted.” Can I report that the purchase is complete?

**User-facing result**

> Not from that status alone. “Checkout submitted” describes a request/session state. A completed purchase requires the relevant merchant/order confirmation, and payment/fulfillment can have their own later states. Report the narrow status you actually have rather than upgrading a submitted request into an accepted/completed order.

**Verdict: PASS**

---

# D. Smoke scorecard

```text
STATIC ROUTING REGRESSION        PASS
LEGACY OVER-ROUTING             PASS
LEGACY UNDER-ROUTING            PASS
LEGACY FOLKLORE LEAKAGE         PASS
LEGACY EVIDENCE COLLAPSE        PASS

INTENT / AUTHORITY               PASS
AUTHORIZATION SCOPE DRIFT        PASS
DISCOVERY / CHECKOUT AUTHORITY   PASS
GOOGLE POPULARITY FOLKLORE       PASS
AMAZON SHOP DIRECT ROUTING       PASS
SURFACE / MERCHANT ROLE          PASS
CHECKOUT / ORDER EFFECT          PASS
```

No smoke required:

- a new durable primitive;
- a second agentic-commerce handbook/ontology;
- a broad new platform route;
- loading agentic theory for ordinary product copy;
- or inventing a protocol/platform fact beyond the evidence ledger.

## Gate recommendation

**RETURN PR #7 TO INDEPENDENT ADVERSARIAL REVIEW.**

Do not continue broad frontier research unless the reviewer/runtime produces a concrete case that this targeted patch cannot represent or route without material distortion.

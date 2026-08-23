# Commerce Agentic-Frontier Runtime Smoke

Reviewed: 2026-08-23

Status: **fresh integration smoke, not benchmark/eval score**.

Purpose: verify that the targeted agentic-commerce frontier patch did not regress the original commerce router and that new delegated-authority / transaction-state / external-store cases route to the smallest relevant knowledge without turning ordinary product communication into a protocol dissertation.

Frozen branch:

```text
candidate/commerce-handbook-v0.1
```

---

# A. Static route regression

| Case | Expected route | Result |
| --- | --- | --- |
| Generic product description with supplied facts | fast path | PASS |
| Shopee product-title rewrite | fast path + Shopee only if field semantics matter | PASS |
| Amazon seller field differs from native PDP | Chapter 09 + Amazon | PASS |
| Lazada `is_key_prop` organic-rank claim | Chapter 09 + Lazada | PASS |
| Shopee buyer-relative displayed-price mismatch | Chapter 09 + Shopee | PASS |
| TikTok shoppable-video creator-commerce relation | 08 + 09 + smallest TikTok/TikTok Shop support | PASS |
| Ordinary TikTok caption, no commerce | social route only | PASS |
| Shopper asks agent only to find options under a budget | Chapter 09 only if authority question becomes material; discovery itself remains narrow | PASS |
| Delegated purchase with budget/checkout-state conflict | Chapter 09 agent-mediated section | PASS |
| Google `popularity_rank` meaning | Google module; Chapter 09 only if broader field/mediation distinction is needed | PASS |
| Google UCP checkout role/authority question | Chapter 09 + Google | PASS |
| Amazon Shop Direct / Buy for Me question | Chapter 09 + Amazon | PASS |

Static verdict: **PASS**.

The router now makes agent-mediated checkout discoverable without changing the rule that ordinary product-writing tasks stay shallow.

---

# B. Legacy four-family regression smoke

The four original families from `commerce-runtime-routing-smoke.md` were re-executed against the updated router/knowledge.

## LR1 — OVER-ROUTING: simple Shopee title

**Prompt**

> Product facts: mini blender, 300 ml, USB-C charging, 6 blades, white. Write a Shopee product title. Do not invent anything.

**Expected / used route**

```text
commerce activation
→ narrow product-title job
→ Shopee module only if naming semantics matter
→ skip Chapter 09 deep graph / agentic layer
```

**User-facing result**

> Máy Xay Sinh Tố Mini 300ml USB-C 6 Lưỡi, Màu Trắng

**Verdict: PASS**

No agentic-commerce material leaked into the artifact.

## LR2 — UNDER-ROUTING: Amazon seller field differs from native PDP

**Prompt**

> My Amazon seller listing says “12-pack” but the live PDP for the ASIN shows “6-pack”. Is my title update broken?

**Used route**

```text
Chapter 09 + Amazon
native Store regime
seller contribution ≠ catalog state ≠ PDP representation
```

**User-facing result**

> Not necessarily. On the native Amazon Store, your seller SKU/listing contribution is not the same thing as the shared catalog state or the content Amazon currently selects for the PDP. First verify the intended ASIN/variation and compare your submitted contribution with the live catalog value. A Shop Direct/external-store distinction is not relevant to this case, so it does not need to be opened.

**Verdict: PASS**

The new Amazon external-store regime did not blur the existing native-PDP diagnosis.

## LR3 — FOLKLORE LEAKAGE: Lazada key attribute

**Prompt**

> Lazada marks an attribute as `is_key_prop=1`. If I fill it in, does that mean my product will rank higher organically?

**User-facing result**

> No such organic-ranking conclusion is established. Lazada documents the field as a key attribute that can affect its item/product score, but that does not establish the score as the organic Search ranker or disclose its downstream weight. Fill it accurately for the documented product-data job; leave the organic ranking effect unknown unless Lazada provides direct system-specific evidence.

**Verdict: PASS**

## LR4 — EVIDENCE COLLAPSE: Shopee displayed price

**Prompt**

> Shopee shows me a lower price than the seller's base price. Does that mean the seller secretly reduced the price for everyone?

**User-facing result**

> Not necessarily. The displayed value can be buyer/account/variant/promotion dependent, including voucher-adjusted or lowest-variation representations. One shopper's displayed price is therefore not proof of a universal seller base-price change. Compare the same variation under the same account, promotion and time state, then verify checkout before concluding the seller changed the underlying price.

**Verdict: PASS**

Legacy regression verdict:

```text
OVER-ROUTING       PASS
UNDER-ROUTING      PASS
FOLKLORE LEAKAGE   PASS
EVIDENCE COLLAPSE  PASS
```

---

# C. Fresh agentic-frontier smoke

## AR1 — Intent ≠ delegated authority

**Prompt**

> I told a shopping agent “find me a laptop under $1,000.” The agent supports checkout. Does that instruction by itself mean it can buy one automatically?

**Route used**

```text
commerce activation
→ Chapter 09 agent-mediated/delegated commerce
→ no platform module required
```

**User-facing result**

> No. “Find me a laptop under $1,000” establishes a discovery constraint, not automatically a purchase authorization. The agent's technical ability to check out is also separate from the authority you granted it. A purchase needs whatever explicit authorization the applicable platform/protocol requires, with the relevant transaction scope and current checkout state.

**Observed behavior**

- shopper intent kept separate from permission;
- capability kept separate from authority;
- no protocol-specific mechanism invented.

**Verdict: PASS**

---

## AR2 — Authorization scope breaks when checkout state exceeds it

**Prompt**

> I authorized an agent to buy a product only if the total is at most $1,000. At checkout the item is $980 plus $48 shipping. Is the old authorization enough?

**Route used**

```text
Chapter 09 agent-mediated/delegated commerce
authorization scope + checkout state + history
```

**User-facing result**

> Not under the authorization as stated. The current total is $1,028, which is outside the ≤$1,000 constraint. The prior authorization applied to a bounded transaction state; it should not be silently carried over to a materially different total. The exact re-authorization step depends on the platform/protocol, but the agent should not treat the old approval as authority for the new amount.

**Observed behavior**

- uses scope/history rather than creating a new mandate primitive;
- leaves exact UX/protocol mechanics platform-specific.

**Verdict: PASS**

---

## AR3 — Discovery price ≠ authoritative checkout state

**Prompt**

> An AI shopping result showed a shoe at $89 and size 42 in stock. Seven minutes later checkout says $94, $8 shipping, and size 42 unavailable. Which state should I trust for the purchase?

**Route used**

```text
Chapter 09
product/discovery representation @ t0
→ authoritative checkout state @ t1
```

**User-facing result**

> For the transaction, use the current authoritative checkout state, not the earlier discovery snapshot. The $89/in-stock result described what the discovery system had at the earlier time; checkout now says the price, shipping and availability have changed. That does not make the discovery feed inherently invalid—it means authority is stage- and time-scoped.

**Observed behavior**

- avoids the overcorrection “feed is never authoritative”;
- preserves stage + time authority.

**Verdict: PASS**

---

## AR4 — Google `popularity_rank` folklore trap

**Prompt**

> Google Merchant Center lets me set `popularity_rank=95.5`. Does that mean Google will rank the product around 95.5 in organic shopping results?

**Route used**

```text
commerce activation
→ Google module
→ field semantics / evidence-boundary task
```

**User-facing result**

> No. Google's `popularity_rank` is merchant-supplied data describing how well that product sells relative to other products in your own inventory. It is intended mainly for conversational shopping experiences; it is not a disclosed Google organic Search/Shopping ranking score. Do not interpret `95.5` as Google's rank for the item.

**Observed behavior**

- field name does not leak into ranking folklore;
- Chapter 09 full graph not required.

**Verdict: PASS**

---

## AR5 — Amazon Shop Direct must escape native ASIN/listing assumption

**Prompt**

> A product appears in Amazon search with “Shop Direct,” but I can't find a normal Amazon seller offer/PDP for it. Is the listing broken?

**Route used**

```text
commerce activation
→ Chapter 09 + Amazon
→ identify native Store vs Shop Direct regime
```

**User-facing result**

> Not necessarily. Shop Direct is an external-store discovery regime: Amazon can surface products sold by merchants elsewhere on the web. The customer may be sent to the merchant's site, or an eligible item may offer Buy for Me. So the absence of a normal native Amazon seller-offer/PDP path is not by itself evidence that the product is broken. Verify that the result is actually labeled Shop Direct and inspect the external merchant/feed state rather than forcing it into the native ASIN→seller-listing→offer model.

**Observed behavior**

- recognizes the genuine Amazon module correction;
- does not claim the product has no Amazon-internal identifier.

**Verdict: PASS**

---

## AR6 — Checkout surface ≠ seller of record

**Prompt**

> If I buy an eligible merchant product through Google's AI Mode/Gemini checkout, is Google automatically the seller and the one responsible for fulfillment?

**Route used**

```text
commerce activation
→ Chapter 09 + Google
→ agent-mediated checkout actor roles
```

**User-facing result**

> No. Google's current UCP checkout guidance says the participating merchant remains the seller of record. Google/AI Mode/Gemini mediate the experience, and Google Pay can supply the payment flow, but that does not by itself transfer the merchant's seller-of-record or fulfillment responsibilities to Google. The exact supported markets/merchants are still rollout-dependent.

**Observed behavior**

- separates encounter surface, MoR, payment role, fulfillment;
- preserves rollout scope.

**Verdict: PASS**

---

## AR7 — Checkout request ≠ completed order

**Prompt**

> My shopping agent says “checkout submitted.” Can I report that the purchase is completed?

**Route used**

```text
Chapter 09 agent-mediated commerce
checkout state → merchant/order/payment effect
```

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

# Commerce Runtime Routing Smoke

Reviewed: 2026-08-23

Status: **integration smoke, not benchmark/eval score**.

> **Post-review note:** this routing smoke remains valid for its routing cases. A later independent review found an Etsy **source-fidelity** conflict about description/query-matching participation, not a router defect. That correction is recorded in `commerce-etsy-query-matching-source-conflict-correction.md` and does not change the routing verdict below.

Purpose: verify the first commerce integration of `SKILL.md` after the Chapter 09 / six-module knowledge freeze. This smoke tests activation and routing boundaries rather than attempting to measure general model quality.

The smoke specifically attacks:

```text
OVER-ROUTING
simple product copy must not trigger a commerce dissertation

UNDER-ROUTING
catalog/platform-processing problems must reach the deeper distinction

FOLKLORE LEAKAGE
platform field/data-quality guidance must not become organic ranking law

EVIDENCE COLLAPSE
buyer-relative/composed commercial representation must not become universal seller state
```

## Frozen branch

```text
candidate/commerce-handbook-v0.1
```

Base includes the merged C3 `OBJECT / REPRESENTATION` parent correction from PR #5.

## Runtime route under test

```text
ACTIVATION
SKILL metadata

↓

SIMPLE PRODUCT COMMUNICATION
facts supplied
→ commerce fast path
→ optional one platform module only when current field semantics/policy matter

DEEP COMMERCE REASONING
catalog identity / variant architecture / field allocation /
platform processing / discoverability / commercial-state conflict /
measurement or attribution
→ Chapter 09
→ smallest relevant commerce module

HYBRID CONTENT × COMMERCE
only when both environments materially matter
→ Chapter 08 + Chapter 09 as needed
→ smallest relevant social + commerce modules
```

---

# A. Static routing audit

| Case | Expected route | Deep Chapter 09? | Result |
| --- | --- | --- | --- |
| Generic product description with supplied facts, no marketplace semantics | message/copy or commerce fast path | No | PASS |
| Shopee product-title rewrite where naming policy/field semantics matter | commerce fast path + `shopee.md` | No | PASS |
| Amazon seller field differs from live PDP/catalog content | Chapter 09 + `amazon.md` | Yes | PASS |
| Lazada `is_key_prop` / product-score question about organic rank | Chapter 09 + `lazada.md` | Yes | PASS |
| Shopee displayed-price mismatch across buyers/accounts | Chapter 09 + `shopee.md` | Yes | PASS |
| Etsy personalized/made-to-order listing identity question | Chapter 09 + `etsy.md` | Yes | PASS |
| TikTok Shop product-title task only | commerce fast path + `tiktok-shop.md` if current field semantics matter | No | PASS |
| TikTok shoppable video / creator-product-link task | Chapter 08 + Chapter 09 + TikTok/TikTok Shop only as needed | Yes, hybrid | PASS |
| Ordinary TikTok caption with no commerce relation | existing Chapter 08/social route | No commerce route | PASS |
| Landing-page copy for a product sold on the merchant's own site, no marketplace/discovery issue | message/copy path; commerce only if product/commercial structure is material | No by default | PASS |

Static verdict: **PASS**. The router distinguishes activation from deep-path loading and does not encode `ANY COMMERCE TASK → Chapter 09`.

---

# B. Fresh runtime smoke

The following cases were executed as fresh task-level walkthroughs against the current router and frozen commerce knowledge. The recorded text is the user-facing answer shape, not hidden reasoning.

## R1 — OVER-ROUTING: simple Shopee title

**Prompt**

> Product facts: mini blender, 300 ml, USB-C charging, 6 blades, white. Write a Shopee product title. Do not invent anything.

**Route used**

```text
activation: commerce metadata
job: narrow product title
facts: already supplied
platform semantics: Shopee naming/listing context material
load: Shopee module only
skip: Chapter 09 deep graph
```

**User-facing result**

> Máy Xay Sinh Tố Mini 300ml USB-C 6 Lưỡi, Màu Trắng

**Observed behavior**

- no catalog/retrieval dissertation;
- no invented ranking claim;
- no unsupported product benefit;
- output remains the requested artifact.

**Verdict: PASS**

---

## R2 — UNDER-ROUTING: Amazon seller field differs from PDP

**Prompt**

> My Amazon seller listing says “12-pack” but the live PDP for the ASIN shows “6-pack”. Is my title update broken?

**Route used**

```text
activation: commerce metadata
job: diagnose platform-record / representation mismatch
load: Chapter 09 + Amazon module
material distinction: seller listing/contribution ≠ catalog state ≠ displayed PDP
```

**User-facing result**

> Not necessarily. On Amazon, your seller listing/SKU contribution is not the same thing as the shared catalog state or the content Amazon currently selects for the PDP. First verify that the SKU is attached to the intended ASIN/variation, inspect the submitted contribution versus the live catalog value, and check whether another catalog contribution or variation relationship is supplying the displayed pack count. Rewriting the title again is not the first diagnostic step.

**Observed behavior**

- recognizes seller contribution ≠ Amazon catalog/PDP;
- does not misdiagnose the issue as ranking or copy quality;
- routes to deeper commerce identity/platform-processing reasoning.

**Verdict: PASS**

---

## R3 — FOLKLORE LEAKAGE: Lazada key attribute

**Prompt**

> Lazada marks an attribute as `is_key_prop=1`. If I fill it in, does that mean my product will rank higher organically?

**Route used**

```text
activation: commerce metadata
job: evaluate platform ranking claim
load: Chapter 09 + Lazada module
material boundary: documented product/item score ≠ established organic Search ranking score
```

**User-facing result**

> No such organic-ranking conclusion is established by that field. Lazada's category-attribute documentation says a key attribute can improve the platform's item/product score, but it does not establish that this score is the organic Search ranking score or disclose how it propagates into Search/Recommendation. Fill the attribute accurately for product-data quality and the platform-defined field job; treat any organic rank effect as unknown unless Lazada provides direct system-specific evidence.

**Observed behavior**

- rejects the ranking-factor leap;
- preserves the documented data-quality/product-score fact;
- leaves downstream organic effect UNKNOWN instead of inventing precision.

**Verdict: PASS**

---

## R4 — EVIDENCE COLLAPSE: Shopee displayed price

**Prompt**

> Shopee shows me a lower price than the seller's base price. Does that mean the seller secretly reduced the price for everyone?

**Route used**

```text
activation: commerce metadata
job: interpret customer-facing commercial representation
load: Chapter 09 + Shopee module
material distinction: seller/base/variant price ≠ buyer-relative displayed price ≠ checkout price
```

**User-facing result**

> Not necessarily. Shopee Vietnam can display an estimated voucher-adjusted price based on vouchers available to the individual buyer, and a multi-variation listing can also surface a lowest applicable variation price. That displayed number therefore is not proof that the seller changed the universal base price. Compare the same product/variation under the same account, voucher, promotion and time state, then check the checkout price before concluding that the seller price changed.

**Observed behavior**

- preserves buyer/account/time scope;
- does not convert one observed representation into universal seller state;
- distinguishes displayed price from final checkout price.

**Verdict: PASS**

---

# C. Integration verdict

```text
ACTIVATION METADATA       PASS
STATIC JIT ROUTING        PASS
OVER-ROUTING SMOKE        PASS
UNDER-ROUTING SMOKE       PASS
FOLKLORE LEAKAGE SMOKE    PASS
EVIDENCE COLLAPSE SMOKE   PASS
```

No smoke case required a new durable primitive or a broader commerce route.

## Remaining boundaries

This smoke does **not** establish:

- exhaustive runtime reliability across all prompts;
- benchmark-level generalization;
- exhaustive source-fidelity adjudication across every official platform document;
- current correctness of every external platform fact after its review date;
- causal performance of any marketplace tactic;
- that every agent/client uses skill metadata activation identically.

## Gate recommendation

**PROCEED TO COMMERCE PR REVIEW.**

Do not reopen broad commerce ontology research unless a concrete runtime/reviewer case cannot be represented or routed without material distortion.

# Commerce Platform Modules

These modules specialize the shared commerce model for current marketplace, shopping, and agent-mediated commerce environments.

They are **not generic pricing strategy modules**. Use [`../../handbook/10-commercial-design-pricing-and-terms.md`](../../handbook/10-commercial-design-pricing-and-terms.md) when the commercial condition itself is still open; use these platform modules when a platform-specific environment changes representation, eligibility, discovery, transaction state, or interpretation.

The shared commerce parent is:

- [`../../handbook/09-commerce-environments-and-product-discovery.md`](../../handbook/09-commerce-environments-and-product-discovery.md)

## Module map

| Module | Namespace | Use when platform-specific knowledge can change... |
| --- | --- | --- |
| [`google-shopping.md`](google-shopping.md) | `google-commerce` | Merchant/product processing, structured product information, shopping surfaces, conversational shopping, UCP-powered checkout, discovery/representation boundaries |
| [`amazon.md`](amazon.md) | `amazon` | catalog vs seller listing, ASIN/SKU/offer identity, PDP composition, Featured Offer, search/discovery, Shop Direct / Buy for Me, agentic authority |
| [`tiktok-shop.md`](tiktok-shop.md) | `tiktok-shop` | seller/product/SKU state, Shop Tab search/recommendation, content-product links, creators/affiliates, relinking, anchor representation, commerce-entry provenance |
| [`shopee.md`](shopee.md) | `shopee` | variations, buyer-relative displayed price, listing fields, search/sort/filter, conversational discovery, representation, marketplace diagnosis |
| [`etsy.md`](etsy.md) | `etsy` | listing/item/configuration identity, heterogeneous product information, search stages, inferred attributes, recommendations, quality/context, field allocation |
| [`lazada.md`](lazada.md) | `lazada` | product/category fields, item/product score boundaries, search/discovery evidence, commercial state, representation, marketplace diagnosis |

## Shared commerce distinctions

Keep these separate whenever collapsing them would change the decision:

```text
PRODUCT / OBJECT
!= LISTING / PLATFORM RECORD
!= REPRESENTATION
!= ENCOUNTER SURFACE

BASE PRICE
!= VARIANT PRICE
!= DISPLAYED PRICE
!= FINAL CHECKOUT PRICE

ELIGIBILITY
!= RETRIEVAL
!= RANKING
!= FILTERING / SORTING
!= RECOMMENDATION

SHOPPER INTENT
!= DELEGATED AUTHORITY
!= EXECUTED TRANSACTION EFFECT
```

A platform module should specialize these distinctions rather than inventing a new ontology for each marketplace.

## Commercial Design boundary

A useful rule:

```text
DESIGN THE COMMERCIAL CONDITION
→ Chapter 10 / commercial-design.*

REPRESENT OR INTERPRET THE EXISTING CONDITION IN A PLATFORM
→ Chapter 09 + platform module as needed
```

Examples:

```text
"Should we offer a new-customer-only discount?"
→ commercial-design.allocation

"Shopee shows this buyer a voucher-adjusted price. Did the seller cut the base price for everyone?"
→ shopee.commercial-state + Chapter 09 commercial-state distinction as needed

"Should our SaaS charge per seat or usage?"
→ Chapter 10; no marketplace module required

"Which Amazon record is causing 6-pack to appear on the PDP?"
→ Amazon identity / catalog / PDP knowledge
```

## Hybrid content × commerce

Use both social/content and commerce modules only when both environments materially matter.

```text
TikTok Shop product-title task
→ tiktok-shop only if platform field semantics matter

TikTok shoppable video / LIVE / creator-product-link task
→ tiktok + tiktok-shop only as needed
```

Do not automatically load both because TikTok Shop is mentioned.

## Routing

Stable logical addresses live in [`../../routing-index.json`](../../routing-index.json).

Examples:

```text
google-commerce.ai-shopping
amazon.offer-featured
tiktok-shop.content-product-identity
shopee.conversational-discovery
etsy.search-stages
lazada.product-score-boundary
```

When helper execution is available:

```bash
python ../../scripts/get-knowledge.py --list --namespace amazon
python ../../scripts/get-knowledge.py shopee.commercial-state
```

Do not copy route-to-heading bindings into this README.

## Evidence and freshness

Marketplace capabilities, policies, UI behavior, and recommendation systems change over time and by market.

Use the scoped evidence under [`../../references/`](../../references/) when provenance matters. Preserve:

- market/country;
- surface/system;
- seller/buyer/account state;
- product/listing/variant scope;
- time/freshness;
- whether evidence establishes capability, representation, eligibility, association, experiment, or causal effect.

Do not convert seller documentation, public ranking hints, one platform score, or one market's UI behavior into a universal organic-ranking law.
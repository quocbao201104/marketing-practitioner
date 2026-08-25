# Shopee — Commerce / Product Discovery Module

Last reviewed: 2026-08-23

Use this module when Shopee-specific listing/product information, variation structure, keyword/image/conversational discovery, explicit sort/filter behavior, shop classification, buyer-relative displayed pricing, multimodal retrieval, Shopee App in ChatGPT, or Shopee product-performance interpretation can materially change the decision.

This module prioritizes Shopee Vietnam current documentation where user-facing and seller-policy behavior is market-specific, plus scoped Shopee engineering evidence [S01–S10]. Re-check consequential behavior and policy before execution.

This module instantiates `../../handbook/09-commerce-environments-and-product-discovery.md`. It does not define a Shopee-specific ontology.

---

## 1. Shopee is a marketplace with several independently consequential states

Do not reduce a Shopee product to its title/description or assume one hidden “Shopee SEO score” explains discovery.

A useful map is:

```text
SELLER / SHOP
    │
    │ posts / sells
    ▼
SHOPEE PRODUCT / LISTING OBJECT
    │
    ├── product-descriptive data
    ├── variations / classifications
    ├── commercial state
    ├── shop-level state
    └── observation / feedback context
             │
             ▼
      DISCOVERY SYSTEMS
      keyword search
      image search
      recommendations / suggestions
      Shopee App in ChatGPT / conversational discovery
      special visibility features
             │
             ▼
      USER FILTER / SORT / CONVERSATIONAL CONTEXT
             │
             ▼
      CUSTOMER REPRESENTATION
      result card / recommendation card / PDP / cart / checkout
```

The same posting can produce different customer-facing commercial representations by buyer, variant, voucher state and time [S02]. Conversational recommendations can additionally depend on the shopper's request/context and, when connected, Shopee account history/preferences [S10].

Therefore:

```text
SHOPEE LISTING STATE
≠ ONE STATIC CUSTOMER REPRESENTATION
```

---

## 2. Product posting and underlying product identity should not be conflated blindly

Shopee is seller-centric: a seller posts a product/listing into its own shop. Similar or materially identical products can also be sold by other shops.

Do not impose either assumption without evidence:

```text
EVERY SHOPEE POSTING = A UNIQUE REAL-WORLD PRODUCT
```

or:

```text
EVERY SHOPEE POSTING MAPS TO ONE PLATFORM-WIDE CANONICAL PRODUCT ENTITY
```

For practitioner work, usually identify:

```text
SELLER / SHOP
SHOPEE PRODUCT / POSTING
VARIATION IF MATERIAL
```

and introduce an underlying shared product/model identity only when comparison, duplicate matching, manufacturer identity, or cross-shop reconciliation actually requires it.

---

## 3. Variations / classifications are selectable configurations

Shopee Vietnam describes product classifications as choices/models such as color, size or style presented on the same product page [S03].

Use:

```text
PRODUCT / POSTING
     │
     │ hasVariation
     ▼
SELECTABLE CLASSIFICATION
```

A variation can carry decision-relevant state such as:

```text
color / size / model
price
stock
quantity limits
image / option representation where applicable
```

Do not add a durable `VARIANT` primitive merely because Shopee exposes classifications/SKUs in seller operations.

Keep:

```text
PRODUCT PAGE / POSTING
≠ SELECTED VARIATION
```

when price, stock, or fulfillment differs by variation.

---

## 4. Product-descriptive information must remain truthful and category-correct

Current Shopee Vietnam listing policy requires clear/truthful product names, title/image consistency, detailed descriptions, source/origin and attributes where required, correct category selection, and category-specific mandatory information [S04].

### 4.1 Product name

Job:

```text
HUMAN IDENTIFICATION
+ truthful summary of what is being sold
```

Shopee requires names to accurately describe the product/service and bans misleading/fake terms and prohibited presentation patterns [S04].

Do not turn this into:

```text
LONGER TITLE / MORE KEYWORDS
→ HIGHER ORGANIC RANK
```

### 4.2 Category

Shopee tells sellers to choose the correct category so products can reach customers [S04].

Supported conclusion:

```text
CATEGORY ACCURACY
CAN AFFECT DISCOVERY / FILTER COMPATIBILITY / POLICY STATE
```

Not established:

```text
CATEGORY FIELD HAS A KNOWN NUMERIC RANKING WEIGHT
```

### 4.3 Attributes / origin / warranty

Use structured product attributes and required commercial/legal information for their defined job. If a dimension, material, origin, size, compatibility, warranty or category-specific field has a structured place, do not rely on prose alone to carry it.

Keep:

```text
STRUCTURED FACT
≠ DESCRIPTION COPY
```

### 4.4 Description

Use description for detailed product characteristics, use, conditions, limitations and required disclosures [S04].

Do not fill descriptions with unrelated search terms or external contact promotion prohibited by policy.

### 4.5 Images

Shopee's policy emphasizes truthful product imagery and category-specific image requirements in some categories [S04]. Images can serve:

```text
human identification
human evaluation
proof / mismatch prevention
machine image-search evidence
```

But:

```text
IMAGE SEARCH USES IMAGES
≠ KNOWN ORGANIC IMAGE-RANKING TACTIC
```

---

## 5. Shop-level state is distinct from product state

Shopee Vietnam exposes shop classifications including ordinary shops, Shop Yêu Thích, Shop Yêu Thích+, and Shopee Mall [S05][S06].

These classifications can depend on seller/service/operational criteria, display badges on shop/product representations, and can be explicitly selected by buyer filters [S05].

Therefore:

```text
SHOP STATE
≠ PRODUCT STATE
```

and:

```text
SHOP BADGE
CAN BE PART OF PRODUCT ENCOUNTER REPRESENTATION
```

### 5.1 Visible / filterable ≠ default ranking factor

Do not infer:

```text
Shop Yêu Thích / Mall is filterable
→ Shopee default search always boosts it by known amount
```

The user can explicitly filter such shops, which changes the candidate set independently of any default ranker [S01][S05].

### 5.2 Seller status can affect evaluation even when it does not alter ranking

Buyer guidance surfaces seller classification and related shop information as part of product evaluation [S06].

Thus shop state can matter through:

```text
HUMAN TRUST / SELECTION CONTEXT
```

without needing a ranking claim.

---

## 6. Search has keyword, image, and conversational entry modes

Current Shopee Vietnam buyer help documents keyword and image search [S01]. Shopee is also available as an app in ChatGPT in supported markets, including Vietnam, where a shopper can use a natural conversational request and receive Shopee product recommendations/cards [S10].

Therefore:

```text
TEXT KEYWORD QUERY
≠ ONLY SHOPEE DISCOVERY INPUT
```

### 6.1 Keyword search does not imply text-only machine retrieval

Shopee's MRSE engineering work describes text-query retrieval using query text together with item text/images and multimodal user preferences/history [S07].

Strong scope-correct inference:

```text
TEXT QUERY
≠ TEXT-ONLY RETRIEVAL MODEL
```

Do not infer that the exact MRSE model, its features, or weights are the complete 2026 Shopee Vietnam production stack.

### 6.2 Image search does not imply image-only item representation

Shopee MIEM uses multiple product images plus textual product information to construct item embeddings for the disclosed Image Search system [S08].

Therefore:

```text
IMAGE QUERY
≠ IMAGE-ONLY PRODUCT REPRESENTATION
```

and:

```text
ONE VISIBLE IMAGE
≠ ALL MACHINE EVIDENCE USED FOR RETRIEVAL
```

### 6.3 Shopee App in ChatGPT is a separate conversational discovery surface

Shopee's current Vietnam guidance says shoppers can ask ChatGPT for Shopee product recommendations using natural language. Connecting a Shopee account is optional; connected users may receive more personalized suggestions based on Shopee purchase history/preferences, while a summary of recent conversational context/needs can be shared with Shopee for the request [S10]. Product detail and checkout then continue on Shopee app/web in the documented flow.

Use:

```text
SHOPPER CONVERSATIONAL REQUEST
+ CONVERSATION CONTEXT
+ OPTIONAL SHOPEE ACCOUNT STATE
→ SHOPEE RECOMMENDATION CONTEXT
→ PRODUCT CARD / SUGGESTION
→ SHOPEE PRODUCT DETAIL / CHECKOUT
```

Keep:

```text
CONVERSATIONAL SHOPPER REQUEST
≠ ONE MANUAL KEYWORD QUERY
```

and:

```text
SHOPEE APP IN CHATGPT EXISTS
≠ DISCLOSED SELLER-FIELD / RETRIEVAL / RANKING FORMULA
```

Current official evidence does not expose which listing fields, embeddings, model features, candidate stages, or weights drive this surface. Do not turn the integration into an “AI SEO” checklist.

For seller-side preparation, use the durable Chapter 09 strategy instead: make decision-relevant product facts, variants, visual evidence, and current commercial state truthful and resolvable in the Shopee-supported carriers that actually exist. If a shopper asks for a 30 cm item, a particular material, a compatible model, a certain variant, or a budget constraint, the seller-side goal is to represent the true answer clearly — not to repeat likely prompt phrases or invent unsupported use cases.

Therefore:

```text
MACHINE / CONVERSATIONAL LEGIBILITY
≠ KEYWORD DENSITY
≠ GUARANTEED CHATGPT RECOMMENDATION
```

---

## 7. Retrieval ≠ ranking; exact organic and conversational pipelines remain partially unknown

MRSE is explicit retrieval-system evidence [S07]. It establishes that Shopee has deployed a candidate-retrieval architecture where multimodal representations can affect recall.

It does **not** establish every later stage, and it does not establish that the same implementation drives the Shopee App in ChatGPT.

Keep:

```text
QUERY / USER / CONVERSATIONAL CONTEXT
       ↓
POSSIBLE RETRIEVAL / RECALL
       ↓
CANDIDATES
       ↓
POSSIBLE RELEVANCE / RANKING / CONSTRAINTS
       ↓
FINAL RESULTS / RECOMMENDATIONS
```

with exact 2026 system details held UNKNOWN unless current Shopee evidence discloses them.

Do not translate retrieval-model features or conversational product behavior into ranking tactics.

---

## 8. Default ranking ≠ explicit buyer sorting ≠ filtering

Shopee Vietnam allows explicit search-result sorting/filtering by criteria including [S01]:

- category;
- seller location;
- shipping;
- price range;
- newest;
- best-selling;
- price ascending/descending;
- Freeship;
- preferred-shop state;
- ratings;
- other filters.

This distinction is critical.

```text
DEFAULT SEARCH RESULT ORDER
≠ USER-SELECTED SORT
≠ USER-APPLIED FILTER
```

### 8.1 A filtered correlation is not default-ranker evidence

If a user filters `rating ≥ X`, high-rated products will dominate the visible result set even if rating has no disclosed role in the default ranking system.

Likewise, selecting `Bán chạy` creates an explicit order that should not be reverse-engineered as the default algorithm.

Before interpreting a search screenshot or local observation, capture:

```text
query / conversational request
filters
sort
surface
user/account state
time
```

---

## 9. Buyer-relative displayed price is a first-class representation state

Shopee Vietnam currently documents a price-display system that can show estimated post-voucher prices based on vouchers available in the individual buyer's account across Search Results, Product Information, Today Suggestions and You May Also Like [S02].

For multi-variation/multi-product postings, the displayed price can be the lowest price among included classifications/products [S02].

Therefore:

```text
SELLER BASE PRICE
≠ VARIATION PRICE
≠ BUYER-RELATIVE DISPLAYED PRICE
≠ GUARANTEED FINAL CHECKOUT PRICE
```

### 9.1 Why checkout price can differ

Shopee explicitly lists reasons including [S02]:

- voucher quota exhausted;
- seller changed price;
- promotion expired;
- promotional quantity limit exceeded;
- buyer did not apply the relevant voucher at checkout.

This is a direct example of:

```text
COMMERCIAL RELATION
+ VARIANT STATE
+ VOUCHER / PLATFORM STATE
+ BUYER ELIGIBILITY
+ TIME
→ CUSTOMER-FACING PRICE REPRESENTATION
```

### 9.2 Do not compare screenshots without buyer/time scope

Two accounts can legitimately see different estimated prices for the same product posting.

A before/after price comparison without account/voucher/time state can therefore be invalid.

---

## 10. Search card / PDP / conversational card are composite representations

A Shopee result card, conversational recommendation card, or PDP can combine some subset of:

```text
product title / image
variation-derived price range or lowest price
seller / shop identity and badge
buyer-relative voucher-adjusted price
shipping / Freeship context
rating / review / sold-count context
promotion labels
stock / availability
```

Therefore:

```text
CUSTOMER PRODUCT REPRESENTATION
≠ ONE SELLER DATA FIELD
≠ ONE STATIC DATABASE RECORD
```

When diagnosing click or conversion performance, inspect the actual representation and surface encountered by the buyer.

---

## 11. Reviews, ratings and sold count are observation-derived context

These are not intrinsic product facts.

Use:

```text
PAST BUYER / ORDER OBSERVATIONS
       ↓ aggregation
RATING / REVIEW / SOLD-COUNT STATE
       ↓ display
LATER SHOPPER ENCOUNTER CONTEXT
```

They may influence human evaluation and can also be used by platform systems where directly disclosed.

Do not infer a default organic ranking effect solely because ratings are visible, filterable, or correlated with high-ranking products.

---

## 12. Special visibility features must not leak into ordinary organic theory

Shopee Vietnam documents a scoped `Sản phẩm Hot` feature providing highlighted visibility on Search/Recommendations under feature-specific criteria [S09].

This is a perfect evidence-boundary test:

```text
FEATURE-SPECIFIC PRIORITY / PLACEMENT CRITERIA
≠ ORDINARY ORGANIC SEARCH / RECOMMENDATION RANKING RULE
```

Do not take sales, discount, ratings, image, or description criteria from that feature and claim they are the default Shopee organic algorithm.

The same rule applies to paid ads, campaign placements, boosts, or other sponsored visibility systems.

---

## 13. Search / recommendation performance must preserve exposure provenance

A product can receive traffic from:

```text
keyword search
image search
recommendation / Today Suggestions / You May Also Like
Shopee App in ChatGPT / AI referral
shop page
special visibility features
ads / campaigns
affiliate / creator / livestream contexts
external referral
```

Do not interpret aggregate clicks/orders as one organic search signal.

A useful observation record includes:

```text
product / variation
seller / shop state
surface / source
query or conversational request if applicable
conversation/account context if material
filter / sort if applicable
price representation / voucher state
exposure
click / cart / order
attribution regime
time
```

---

## 14. Diagnosing weak or changing Shopee performance

Do not jump from lower orders to keyword editing.

```text
1. METRIC / SOURCE
Search impression/click? image-search? recommendation? ChatGPT referral?
PDP? cart? order?

2. PRODUCT / VARIATION
Same posting, category, variation structure, stock?

3. PRODUCT INFORMATION
Same name, images, description, attributes, origin/warranty fields?

4. SHOP STATE
Same Shop Thường / Yêu Thích / Yêu Thích+ / Mall state?

5. COMMERCIAL STATE
Same seller price, variation price, promotion, voucher eligibility,
shipping / Freeship, stock?

6. USER DISCOVERY STATE
Same keyword/image/conversational request, filters, sort,
buyer account/location, ChatGPT conversation/account connection if relevant?

7. REPRESENTATION
Same displayed price, badge, title/image, rating/sold-count context,
recommendation card / PDP?

8. VISIBILITY MODE
Ordinary organic vs ChatGPT app / Sản phẩm Hot / ads / campaign /
other special placement?

9. TIME / PLATFORM REGIME
Same policy, voucher, promotion, app/surface behavior?

10. DISCRIMINATING CHECK
What current search reproduction / buyer-account comparison /
conversation reproduction / seller data / traffic-source evidence
best separates causes?
```

Load Chapter 05 for causal attribution.

---

## 15. Fast paths

### Rewrite product name

```text
preserve actual product facts
→ comply with current Vietnamese naming rules
→ make product identity clear
→ ensure image/name consistency
→ do not add irrelevant keyword strings
```

### Improve listing completeness

```text
verify category
→ required product attributes / origin / warranty / category data
→ truthful description
→ truthful images
→ variation configuration
→ commercial state
```

For AI/conversational discoverability, completeness means resolving truthful product facts in the appropriate Shopee-supported carriers; it does **not** mean inventing extra attributes or stuffing hypothetical conversational phrases.

### Diagnose “rank drop”

Before any copy change:

```text
reproduce query / conversational context + sort + filters
→ identify organic vs AI referral vs special placement
→ compare shop/product/commercial state
→ inspect traffic-source change
→ only then test content/data hypothesis
```

---

## 16. Shopee-specific anti-folklore guardrails

```text
CORRECT CATEGORY HELPS DISCOVERY / FILTERING
≠ KNOWN RANKING WEIGHT
```

```text
TITLE / DESCRIPTION / ATTRIBUTE REQUIRED OR RECOMMENDED
≠ ORGANIC RANKING FORMULA
```

```text
KEYWORD SEARCH
≠ TEXT-ONLY RETRIEVAL
```

```text
IMAGE SEARCH
≠ IMAGE-ONLY ITEM REPRESENTATION
```

```text
SHOPEE APP IN CHATGPT USES NATURAL-LANGUAGE CONTEXT
≠ KNOWN SELLER-FIELD / RANKING TACTIC
```

```text
RICHER / MORE COMPLETE LISTING DATA
≠ GUARANTEED CHATGPT RECOMMENDATION
```

```text
MRSE / MIEM DEPLOYED SYSTEM
≠ COMPLETE CURRENT SHOPEE ALGORITHM
≠ PROVEN SHOPEE-CHATGPT IMPLEMENTATION
```

```text
DEFAULT RANKING
≠ USER FILTER
≠ USER SORT
```

```text
SHOP YÊU THÍCH / MALL FILTERABLE
≠ PROVEN DEFAULT-RANK BOOST
```

```text
DISPLAYED PRICE
≠ SELLER BASE PRICE
≠ GUARANTEED CHECKOUT PRICE
```

```text
SẢN PHẨM HOT CRITERIA
≠ ORDINARY ORGANIC RANKING FACTORS
```

```text
HIGH SOLD COUNT / RATING
≠ PURE PRODUCT PREFERENCE
≠ PROVEN CAUSAL RANKING EFFECT
```

---

## 17. Explicit UNKNOWNs

Unless current authoritative Shopee evidence establishes otherwise, preserve as UNKNOWN:

- complete 2026 Shopee Vietnam organic keyword-search retrieval/ranking pipeline;
- exact ranking/relevance feature set and weights;
- exact Shopee listing fields and data transformations consumed by the Shopee App in ChatGPT;
- exact candidate-generation, retrieval, ranking, reranking, or recommendation logic for the Shopee App in ChatGPT;
- exact weighting of connected-account history/preferences versus current conversational context in Shopee App recommendations;
- whether Shopee's published MRSE/MIEM systems share representations or stages with the ChatGPT integration;
- current relationship between MRSE research/deployment and all production search traffic;
- exact Image Search models after the disclosed MIEM deployment period;
- exact recommendation algorithms for Today Suggestions / You May Also Like and other modules;
- exact default organic effect of shop classification, rating, sales, price, promotion, shipping, title, attributes, descriptions, or images;
- exact composition of organic, ads, campaigns and special visibility placements;
- complete seller-facing object/variation IDs beyond the buyer-facing semantics documented here;
- causal impact of changing one listing field on organic/AI exposure or sales without a valid experiment.

---

## 18. Final Shopee check

1. Is product posting identity being confused with a presumed canonical underlying product that need not exist?
2. Are variation/product-page roles separated where price/stock differ?
3. Is current listing policy satisfied before optimization theory is applied?
4. Are title, description, structured fields and images being allocated by job rather than keyword stuffing?
5. Is shop-level state kept separate from product state?
6. Is shop badge visibility/filterability being mistaken for default ranking evidence?
7. Are keyword, image, and conversational discovery considered separately when material?
8. Is query modality kept separate from machine-representation modality?
9. Are retrieval and ranking separated?
10. If Shopee App in ChatGPT is in scope, are conversational request/context and optional account state preserved without inventing a seller-field/ranking map?
11. Can relevant shopper constraints be resolved from truthful product/variant/commercial data without inventing attributes or repeating prompt phrases?
12. Are explicit buyer filters/sorts recorded before interpreting results?
13. Is displayed price scoped to buyer, variation, voucher and time?
14. Is displayed price kept separate from checkout price?
15. Are reviews/ratings/sold count treated as observation-derived context?
16. Are Sản phẩm Hot / ads / campaigns kept separate from ordinary organic discovery?
17. Are traffic-source and exposure provenance preserved before learning from orders?
18. Are current VN-specific docs kept in market scope?
19. Are undisclosed internals left UNKNOWN?

Shopee should be reasoned as a buyer-relative, multimodal and now conversational marketplace environment — not as a title-keyword leaderboard or an imagined ChatGPT ranking formula.

---

## Evidence

See `../../references/commerce/shopee-evidence.md` for `[S01–S10]` source definitions and evidence boundaries.

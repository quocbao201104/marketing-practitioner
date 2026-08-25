# Lazada — Commerce / Product Discovery Module

Last reviewed: 2026-08-23

Use this module when Lazada-specific product/item/SKU identity, country/venture scope, category/attribute structure, seller product creation, price/inventory state, machine-derived product attributes, Search/Recommendation boundaries, or Sponsored Solutions evidence can materially change the decision.

Lazada Open Platform documentation has mixed endpoint freshness; several product/category pages were last updated in 2024 while adjacent product-creation/developer contracts were updated in 2025. Treat them as the currently available integration documentation for the cited endpoints, not as proof of an unchanged production search stack. Paid-product behavior is especially time-sensitive in August–September 2026 [LZ01–LZ08].

This module instantiates `../../handbook/09-commerce-environments-and-product-discovery.md`. It does not define a Lazada-specific ontology.

---

## 1. Lazada product identity is layered and market-scoped

Do not collapse `product`, `item`, SPU, SKU, seller SKU, global product and physical-product identity into one noun.

A practical Open Platform view is:

```text
GLOBAL / CROSS-BORDER MANAGEMENT OBJECT where applicable
                │
                ├── venture / country scope
                ▼
        LOCAL ITEM / PRODUCT
                │
                │ has SKU / variant
                ▼
               SKU
          /             \
  SellerSku           SkuId
 seller-local       Lazada-created
```

Lazada's current available docs say `item_id` is unique in the current country and one item can have multiple SKU IDs; `SellerSku` is seller-customizable/unique in the store, while `SkuId` is created by Lazada [LZ01].

Therefore:

```text
ITEM_ID
≠ SELLER SKU
≠ LAZADA SKU ID
```

and:

```text
LOCAL ITEM IDENTITY
≠ AUTOMATICALLY UNIVERSAL PRODUCT IDENTITY
```

---

## 2. Country / venture scope is first-class

Lazada operates multiple Southeast Asian ventures. Open Platform documentation says category trees and category IDs may differ between countries; brand libraries can also differ [LZ02][LZ03]. Cross-border/global product tooling can target MY, SG, TH, PH, ID and VN under documented permissions [LZ05].

Therefore do not assume:

```text
CATEGORY_ID(MY) = CATEGORY_ID(VN)
```

or:

```text
GLOBAL PRODUCT OBJECT
= IDENTICAL LOCAL LISTING / SKU / COMMERCIAL STATE IN EVERY VENTURE
```

Preserve at least when material:

```text
country / venture
seller authorization scope
local category / brand taxonomy
local item/SKU identity
local commercial state
```

### 2.1 Cross-border/global product is a management role, not universal product truth

A global product/SPU-style object can organize cross-market creation and stock allocation [LZ05]. Treat it as a Lazada management identity.

Do not infer that every local market exposes the same attributes, category mapping, price, inventory, policy or customer representation merely because the product originates from one global object.

---

## 3. SPU/item-level attributes and SKU-level attributes are different roles

Lazada's category-attribute API explicitly distinguishes [LZ02]:

```text
attribute_type = normal
→ item / SPU-level attribute

attribute_type = sku
→ SKU-level attribute
```

It additionally marks:

```text
is_sale_prop = 1
→ sales / variant attribute
```

Use:

```text
ITEM / PRODUCT
    │
    │ hasVariant
    ▼
SKU
```

with variant attributes such as size/color/specification at the SKU level when the category contract defines them that way.

Do not add a durable `SKU` or `VARIANT` primitive to the core; these are local object roles.

### 3.1 No variant attribute can mean one SKU only

Current product-management guidance says that when no variant attribute is defined, an item can have only one SKU; multi-SKU products require variant/sales attributes [LZ02].

This is an implementation constraint, not a universal commerce law.

---

## 4. Key attributes and “product score” require strict evidence boundaries

The GetCategoryAttributes documentation says `is_key_prop=1` marks a key item attribute and filling it can improve an item/product score/rating [LZ02].

Do **not** translate that into:

```text
KEY ATTRIBUTE FILLED
→ ORGANIC SEARCH RANK BOOST
```

The documentation does not establish that the referenced product/item score is the organic Search ranking score, nor its downstream use or weight.

Supported conclusion:

```text
KEY ATTRIBUTE
= PLATFORM-DEFINED IMPORTANT ATTRIBUTE FOR ITEM DATA QUALITY / SCORE
```

Unsupported without further evidence:

```text
KEY ATTRIBUTE
= DISCLOSED ORGANIC RANKING FACTOR
```

This is one of the module's strongest anti-folklore boundaries.

---

## 5. Category, brand and product-creation state matter before ranking theory

Lazada product creation requires or recommends resolving [LZ03]:

```text
country-specific category tree
category suggestion from product title
category-specific attributes
brand / brand_id where applicable
images / video
item-level attributes
one or more SKUs
```

Lazada warns that mis-categorized products can be deactivated [LZ03].

Therefore:

```text
CATEGORY / PRODUCT VALIDITY ISSUE
≠ ORDINARY LOW ORGANIC RANK
```

A product that is invalid, miscategorized, inactive, or under another product-state constraint should not be diagnosed first as a copy problem.

### 5.1 Category suggestion is assistance, not product truth

Lazada can recommend a category from a product title [LZ03].

Keep:

```text
ALGORITHMIC CATEGORY SUGGESTION
≠ VERIFIED SELLER / DOMAIN TRUTH
```

The seller/developer still has to select a correct category under current policy/schema.

---

## 6. Seller input can be transformed or supplemented by platform systems

Lazada product-creation contracts include algorithmic assistance / auto-fill behavior for attributes where supported [LZ03].

Use:

```text
SELLER PRODUCT INPUT
        ↓
validation / suggestion / auto-fill / platform processing
        ↓
LAZADA-HELD PRODUCT DATA
```

Therefore:

```text
SELLER-DECLARED FIELD
≠ GUARANTEED PLATFORM-HELD ATTRIBUTE
```

and:

```text
PLATFORM-AUTOFILLED ATTRIBUTE
≠ SELLER-DECLARED PRODUCT TRUTH
```

Preserve provenance when a machine-derived attribute affects filtering, presentation, search/recommendation or compliance.

---

## 7. Product-descriptive fields and commercial state should stay separate

### Product-descriptive / catalog information

Can include:

```text
title
brand
category
SPU/item attributes
SKU / variant attributes
short / long description
images / video
package dimensions / content
other category-specific facts
```

### Commercial / inventory state

Can include:

```text
price
special price + validity dates
SKU quantity
sellable quantity
withhold quantity
occupy quantity
warehouse-specific inventory
fulfillment / inventory-management mode
market / venture
```

Do not treat commercial state as timeless product identity.

---

## 8. Inventory is not one scalar stock field

Lazada's product-management APIs can expose [LZ04]:

```text
SellableQuantity
stock buyers can currently purchase

withholdQuantity
inventory tied to purchased-but-unpaid items

occupyQuantity
inventory tied to paid purchases

totalQuantity
sellable + withhold + occupy

multiWarehouseInventories
warehouse-scoped stock state
```

Therefore:

```text
TOTAL INVENTORY
≠ SELLABLE INVENTORY
```

and:

```text
STOCK
≠ ONE STATIC PRODUCT PROPERTY
```

When a listing appears unavailable or conversion changes, check the relevant SKU/warehouse/sellable state rather than a generic “stock > 0” assumption.

---

## 9. Price is SKU-, promotion-, and time-scoped

Lazada SKU data can include ordinary price plus special promotional price / validity dates under supported product APIs [LZ03][LZ04].

Keep:

```text
PRODUCT / ITEM IDENTITY
≠ SKU PRICE
≠ SPECIAL PRICE AT TIME t
```

Do not assume a displayed starting price represents every SKU or that a special price remains valid outside its configured period.

---

## 10. AutoPKG demonstrates platform-derived product knowledge

Lazada/Alibaba's 2026 AutoPKG system ingests multimodal product content, dynamically induces product types and attribute keys, extracts values, and canonicalizes them into a Product-Attribute Knowledge Graph [LZ06].

Use the architecture:

```text
LISTING / PRODUCT CONTENT
text + images
       ↓
LLM / MULTI-AGENT EXTRACTION
       ↓
TYPE + ATTRIBUTE-KEY INDUCTION
       ↓
VALUE EXTRACTION
       ↓
CANONICALIZATION
       ↓
PLATFORM-DERIVED PRODUCT KNOWLEDGE
```

This is strong evidence that machine product understanding can go beyond seller-declared structured fields.

Therefore:

```text
SELLER FIELD SET
≠ ALL PLATFORM PRODUCT KNOWLEDGE
```

and:

```text
MACHINE-DERIVED ATTRIBUTE
≠ VERIFIED DOMAIN TRUTH
```

without provenance/validation.

### 10.1 AutoPKG production impact is not a seller-field ranking law

The paper reports online A/B GMV gains from AutoPKG-derived attributes in Badge, Search, and Recommendation for the tested deployment [LZ06].

Supported:

```text
DERIVED PRODUCT KNOWLEDGE
CAN MATERIALLY AFFECT PRODUCTION COMMERCE SYSTEMS
```

Not supported:

```text
MANUALLY FILL ATTRIBUTE X
→ SEARCH RANK +Y%
```

The intervention was a platform product-knowledge system, not a generic seller copy tactic.

---

## 11. Search, recommendation and advertising are separate system families

Lazada publicly states that its AI team works on search, recommendation and advertising algorithms [LZ07].

This establishes the existence of distinct system families, not their exact internal architecture.

Keep:

```text
SEARCH
≠ RECOMMENDATION
≠ ADVERTISING
```

unless a specific shared system is directly documented.

### 11.1 Exact organic search internals remain UNKNOWN

Public evidence reviewed here does not establish:

- exact organic candidate retrieval;
- lexical vs semantic matching;
- exact use/weight of title/category/attributes/images/product graph;
- organic ranking objectives;
- reranking/composition;
- how local-market policy, seller or inventory states enter ranking.

Do not infer these from API schemas or paid-ad disclosures.

### 11.2 Exact organic recommendation internals remain UNKNOWN

AutoPKG establishes that derived attributes have been used in a Recommendation production application [LZ06], and Lazada publicly confirms recommendation algorithms as a system family [LZ07].

That still does not reveal complete recommendation candidate generation, objective, feature weights or module-specific composition.

---

## 12. Sponsored Search / Recommendations must remain separate from organic discovery

Lazada Sponsored Solutions explicitly discloses promoted-product ranking factors such as [LZ08]:

```text
bid competitiveness
keyword selection
promoted-product quality
  historical sales performance
  ratings
  positive reviews
  creatives
```

Sponsored Discovery placements include Search Results and recommendation surfaces such as Homepage For You and PDP Recommendations [LZ08].

This is **paid-system evidence**.

Do not infer:

```text
HISTORICAL SALES / RATINGS / REVIEWS / CREATIVES
ARE ORGANIC LAZADA RANKING FACTORS
```

merely because they affect promoted-product ranking.

Keep:

```text
SPONSORED SEARCH RANKING
≠ ORGANIC SEARCH RANKING
```

and:

```text
SPONSORED RECOMMENDATION PLACEMENT
≠ ORGANIC RECOMMENDATION RANKING
```

---

## 13. August–September 2026 paid-product transition is a history/state lesson

On August 20, 2026 Lazada announced that starting September 19 it will begin phasing out Sponsored Discovery Automated and Promoted Specific Products, with eligible active campaigns upgraded to Sponsored Max Store/Product during September 19–30; Sponsored Discovery Manual remains unchanged under the announced plan [LZ08].

This means a seller-facing instruction can become outdated within weeks.

Use:

```text
CAMPAIGN PRODUCT / MODE AT t0
        ↓ announced migration
CAMPAIGN PRODUCT / MODE AT t1
```

Therefore:

```text
CURRENT OFFICIAL DOCUMENTATION
≠ TIMELESS PRODUCT REGIME
```

For campaign work in or after September 2026, verify actual Seller Center campaign type and migration state before applying Sponsored Discovery instructions.

### 13.1 Sponsored Max evidence does not backfill organic theory

Sponsored Max currently promotes through Search and Recommendations [LZ08]. Its AI optimization, Target ROAS and bidding behavior are ad-system state.

Do not use it to explain ordinary organic product ranking.

---

## 14. Product / card / PDP / recommendation representation remain distinct

A Lazada local item/SKU state can be rendered differently across:

```text
Search result
recommendation card
PDP
variation selector
campaign / badge representation
cart / order representation
sponsored result
```

Keep:

```text
ITEM / SKU
≠ CUSTOMER-FACING REPRESENTATION
≠ SURFACE
```

AutoPKG-derived attributes can additionally create platform knowledge that influences a Badge/Search/Recommendation system without necessarily appearing as the seller's original field text [LZ06].

---

## 15. Field allocation on Lazada

### Title

Job:

```text
human product identification
+ input for category suggestion / product systems
```

Do not infer title keyword position or density ranking rules from category-suggestion functionality.

### Category

Use the correct country-specific leaf category [LZ02][LZ03].

Wrong category can cause product deactivation; this is an eligibility/catalog correctness issue before ordinary organic ranking.

### Normal/SPU attributes

Use for product-level facts defined once for the item.

### SKU / sale attributes

Use for variation-defining product information where multiple SKUs differ.

### Key attributes

Fill accurately where relevant/required for data quality and the documented item/product score [LZ02].

Do not call them organic ranking boosts.

### Brand

Use the correct country-specific brand library when applicable [LZ03].

### Images / video / descriptions

Use for truthful human identification/evaluation and platform product understanding where supported.

Machine systems can extract additional knowledge from multimodal content [LZ06], but this does not justify image/text stuffing or fabricated attributes.

---

## 16. Diagnosing weak or changing Lazada performance

Do not jump from lower GMV to title/attribute rewriting.

```text
1. METRIC / SYSTEM
Organic Search? recommendation? PDP? sponsored Search? Sponsored Max?
Badge/campaign? order / GMV?

2. COUNTRY / VENTURE
Same local market, category tree, brand library, authorization?

3. ITEM / SKU IDENTITY
Same item_id, SellerSku, SkuId, variant mapping?

4. PRODUCT DATA
Same category, item attributes, SKU attributes,
title, descriptions, images/video?
Any platform auto-fill / inferred attribute change?

5. COMMERCIAL / INVENTORY STATE
Same price, special-price period, sellable stock,
withhold/occupy state, warehouse allocation?

6. PLATFORM STATUS
Same item/SKU active state, QC/category validity?

7. ORGANIC / PAID PROVENANCE
Same organic vs Sponsored Discovery / Sponsored Max mix?

8. AD PRODUCT REGIME
Did Sponsored Discovery campaign migrate or change mode?

9. TIME / PLATFORM REGIME
Same API/catalog/product/search/recommendation state?

10. DISCRIMINATING CHECK
Which item/SKU/API/traffic/ad report or controlled test
best separates the explanations?
```

Use Chapter 05 when causal attribution becomes material.

---

## 17. Fast paths

### Create / clean product data

```text
verify target country
→ get correct category tree / leaf
→ load category attributes
→ fill truthful item-level facts
→ define SKU/sale attributes only for real variants
→ verify brand
→ attach images/video
→ set SKU price/stock
→ submit
```

No ranking theory is needed unless discoverability is actually the problem.

### Fix variant / stock issue

```text
identify item_id + exact SKU
→ distinguish SellerSku vs SkuId
→ inspect saleProp / sku attributes
→ inspect sellable / withhold / occupy / warehouse state
→ correct scoped data
```

### Improve organic discoverability

```text
first verify validity/category/data completeness
→ identify actual organic Search or Recommendation symptom
→ preserve country/item/SKU/commercial state
→ use current evidence only
→ keep exact ranker UNKNOWN
```

### Optimize a paid campaign

Load Sponsored Solutions guidance for the actual current campaign type. Do not reuse organic reasoning as ad-bidding advice or vice versa.

---

## 18. Lazada-specific anti-folklore guardrails

```text
item_id
≠ SellerSku
≠ SkuId
```

```text
GLOBAL / CROSS-BORDER PRODUCT
≠ IDENTICAL LOCAL PRODUCT STATE IN ALL VENTURES
```

```text
CATEGORY / BRAND ID
≠ CROSS-COUNTRY CONSTANT
```

```text
NORMAL ATTRIBUTE
≠ SKU / SALE ATTRIBUTE
```

```text
is_key_prop / PRODUCT SCORE
≠ PROVEN ORGANIC SEARCH RANKING WEIGHT
```

```text
CATEGORY SUGGESTION
≠ CATEGORY TRUTH
```

```text
PLATFORM-AUTOFILLED ATTRIBUTE
≠ SELLER-DECLARED FACT
```

```text
TOTAL STOCK
≠ SELLABLE STOCK
```

```text
AUTOPKG SEARCH / RECOMMENDATION A/B EFFECT
≠ MANUAL SELLER ATTRIBUTE RANKING TACTIC
```

```text
SPONSORED RANKING FACTOR
≠ ORGANIC RANKING FACTOR
```

```text
SPONSORED DISCOVERY GUIDE
≠ TIMELESS CAMPAIGN REGIME
```

---

## 19. Explicit UNKNOWNs

Preserve these unless fresher authoritative Lazada evidence establishes them for the exact market/system:

- exact 2026 organic Search retrieval/ranking architecture;
- exact organic Search field/features/weights;
- exact Recommendation architectures, module objectives and weights;
- exact current deployment scope of AutoPKG-derived attributes across categories/markets;
- exact relationship between Open Platform `is_key_prop` product/item score and downstream systems;
- exact algorithmic auto-fill behavior and coverage by category/market;
- exact customer-facing transformation of item/SKU data across Search/PDP/recommendations;
- complete organic/paid composition rules;
- every post-September-2026 Sponsored Discovery/Sponsored Max migration state;
- causal effect of changing one seller field on organic impressions, ranking, orders or GMV without a valid experiment.

---

## 20. Final Lazada check

1. Are item_id, SellerSku, SkuId and any global/cross-border identity scoped correctly?
2. Is country/venture scope preserved for category, brand and local item state?
3. Are item/SPU attributes separated from SKU/sale attributes?
4. Are key attributes being treated as data-quality/item-score fields rather than asserted organic rank weights?
5. Is category suggestion being treated as algorithmic assistance, not truth?
6. Are seller input and platform auto-filled / machine-derived attributes provenance-separated?
7. Are product-descriptive data and commercial/inventory state separated?
8. Is sellable stock distinguished from withhold/occupy/total inventory?
9. Is price/special-price state scoped to SKU/time?
10. Is AutoPKG evidence used as platform product-knowledge evidence rather than manual-field SEO advice?
11. Are Search, Recommendation and Advertising kept separate?
12. Are Sponsored ranking criteria prevented from leaking into organic theory?
13. Is the September 2026 Sponsored Discovery→Sponsored Max transition checked for current campaign work?
14. Are item/SKU, representation and surface separated?
15. Are Open Platform source dates explicit enough for the decision?
16. Are undisclosed organic internals left UNKNOWN?
17. Is the fast path respected when the task is merely product-data cleanup?

Lazada should be reasoned as a market-scoped item/SKU/catalog and product-knowledge environment with separate organic and paid systems — not as one `product score` or title-keyword algorithm.

---

## Evidence

See `../../references/commerce/lazada-evidence.md` for `[LZ01–LZ08]` source definitions and evidence boundaries.

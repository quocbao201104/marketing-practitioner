# TikTok Shop — Commerce / Product Discovery Module

Baseline review: 2026-08-23. Bounded state, linking, discovery, and measurement follow-ups: 2026-09-09. Vietnam applicability follow-up: 2026-09-09; source-specific access and review limits are recorded in the evidence ledgers.

Use this module when TikTok Shop-specific product/SKU structure, Shop Tab search/recommendation, product cards, Search terms / Product highlights, creator-product linking, shoppable video/LIVE, affiliate relationships, relinking, or commerce measurement can materially change the decision.

Current facts are market- and feature-scoped. Seller Academy evidence in the core ledger is primarily US unless stated otherwise; Partner API semantics cover the markets documented by the API. Selected current Vietnam behavior is separately grounded in `[TV01–TV03]`. Re-check consequential behavior before execution [TTS01–TTS10][TV01–TV03].

This module instantiates `../../handbook/09-commerce-environments-and-product-discovery.md`. For shoppable-video, LIVE, creator, or social-distribution decisions, also use Chapter 08 and `../tiktok.md` only when those content-environment distinctions are material.

---

## 1. TikTok Shop is both a marketplace and a content-commerce graph

Do not reduce TikTok Shop to product listings inside TikTok videos.

Relevant environments include:

- Shop Tab search;
- Shop Tab personalized recommendations / browse;
- product cards outside short video / LIVE;
- PDPs and product options;
- shoppable short videos;
- LIVE commerce;
- creator showcase / product marketplace;
- creator-side product-link recommendations;
- seller / affiliate relationships;
- campaigns / promotions;
- product APIs, catalog/status/review systems;
- paid Shop Ads systems;
- analytics and attribution.

A product can be discovered without a social content object, while a video can exist without a product link [TTS05][TTS07].

Therefore:

```text
TIKTOK SHOP PRODUCT DISCOVERY
≠ SHOPPABLE VIDEO ONLY
```

and:

```text
CONTENT OBJECT
≠ COMMERCE OBJECT
```

---

## 2. Product, SKU, product family, and identifier scope

### 2.1 TikTok product ID is platform-local commerce identity

Products API defines a TikTok Shop Product as an item a seller lists for sale and identifies it with a product ID [TTS01].

Use:

```text
product_id
= TIKTOK SHOP PRODUCT-RESOURCE IDENTITY
```

not:

```text
product_id
= UNIVERSAL PHYSICAL PRODUCT IDENTITY
```

TikTok can additionally expose standardized identifier codes such as GTIN/EAN/UPC/ISBN/JAN and global/local commerce-management IDs [TTS02].

Preserve:

```text
STANDARDIZED IDENTIFIER
≠ TIKTOK LOCAL PRODUCT ID
≠ SELLER-LOCAL SKU ID
```

when reconciliation matters.

### 2.2 Product attributes ≠ sales attributes

TikTok's Partner API makes the distinction explicit [TTS01][TTS02]:

```text
PRODUCT ATTRIBUTES
manufacturer / origin / material / other whole-product facts

SALES ATTRIBUTES
size / color / length / other variant-defining options
```

Sales attributes define SKUs / variants; product attributes describe the product as a whole.

Therefore:

```text
PRODUCT-LEVEL FACT
≠ VARIANT-DEFINING ATTRIBUTE
```

Do not put a variant-specific state into a whole-product field when the platform provides a SKU/sales-attribute structure.

### 2.3 SKU is a sellable configuration role

A practical encoding is:

```text
PRODUCT
   │
   │ hasVariant
   ▼
SKU / SELLABLE VARIANT
```

SKU-level state can include price, inventory, SKU images, unit pricing, presale state, or market-specific data [TTS02][TTS03].

Variant does not need a new durable primitive.

### 2.4 Product family can exist above individual products in some markets

Get Product currently exposes `product_families` for supported US local-seller cases, where a family is a virtual group of products sharing characteristics and presented as selectable variations [TTS02].

This is a TikTok-local catalog role. Do not assume product-family availability or semantics in every market.

---

## 3. Product status and audit state matter before ordinary performance

TikTok Shop product resources can move through status / review states such as draft, pending/review, activate, seller/platform deactivation, freeze, or deletion depending on the API/view [TTS01][TTS02].

Keep:

```text
PRODUCT EXISTS IN SELLER SYSTEM
≠ LIVE / ACTIVE
≠ VISIBLE
≠ BUYABLE
≠ RECOMMENDATION-ELIGIBLE
```

A product can remain live at a prior version while an edit is under review in supported API flows [TTS01].

When comparing API data with the storefront, preserve which version was requested. Get Product v202309 distinguishes live data from the under-review version through `return_under_review_version`; draft retrieval is a separate, mutually exclusive selection. Verify the endpoint/version rather than copying older overview parameter names [TTS02].

Product status and audit status can also differ. In the documented U.S. local-seller invite-only category flow, `PRE_APPROVED` can coexist with `PENDING` until a prerequisite is met. Read `audit.pre_approved_reasons`; `RESTRICTED_CATEGORY_PENDING` calls for category permission, not another copy rewrite. Do not assign that reason to every pending product [TTS02].

Edit Product v202309 separately documents price/inventory edits as not requiring content re-audit. Do not assume those fields wait for a pending title edit; inspect their actual update result and applicable constraints [TTS03].

Therefore diagnose catalog/audit state before inferring that a content or ranking change caused missing exposure.

---

## 4. Commercial state is SKU-, market-, warehouse-, and time-scoped

TikTok Shop Partner API states that price is set at SKU level [TTS03]. Price formats, tax treatment, unit-price fields, list-price rules, and currency precision vary by market.

Inventory can additionally be warehouse scoped [TTS02][TTS03].

Use:

```text
PRODUCT IDENTITY
      │
      └── hasVariant → SKU
                          │
                          ├ price
                          ├ stock
                          ├ warehouse availability
                          ├ presale / fulfillment state
                          └ market-specific commercial data
```

Therefore:

```text
PRICE
≠ TIMELESS PRODUCT FACT
```

and:

```text
PRODUCT ACTIVE
≠ EVERY SKU IN STOCK
```

Do not reason from the PDP's visible starting price without checking which SKU/configuration and promotion state it represents.

For a failed inventory change, inspect the returned reason and which system controls the stock. The documented API can reject local updates for shared/automatically allocated inventory or warehouse restrictions; waiting for content review does not resolve those causes [TTS03].

---

## 5. Listing information jobs: title, attributes, Search terms, Product highlights, images

### 5.1 Title

Title should clearly identify the actual product and important distinguishing information while complying with current market/category rules.

TikTok's API exposes title requirements that can vary by region [TTS01].

Treat title as:

```text
HUMAN IDENTIFICATION
+ PRODUCT INFORMATION FOR PLATFORM SYSTEMS
```

not as the entire search index.

### 5.2 Product attributes

Structured attributes provide category-specific product facts and can be required for listing [TTS01][TTS02].

Use them for the factual property the platform defines, not keyword stuffing.

### 5.3 Sales attributes

Use sales attributes to define variants such as size/color/length and support SKU selection [TTS01][TTS02].

This is primarily configuration / disambiguation structure, not generic descriptive prose.

### 5.4 Search terms

As of June 12, 2026, TikTok Shop US added an optional Search terms field for backend descriptors, synonyms, and other relevant terms; TikTok says the information helps its search system understand products and improve matching with customer searches [TTS04].

Strong supported conclusion:

```text
SEARCHABLE / MATCHING DATA
≠ TITLE ONLY
```

Do not infer:

```text
MORE SEARCH TERMS
→ HIGHER RANK
```

or a disclosed priority relative to title, attributes, images, behavior, or other search inputs.

### 5.5 Product highlights

TikTok Shop US describes optional Product highlights on the product detail page and recommends 3–5 concise points; this is not a mandatory minimum. These communicate key benefits/features and can help search understanding [TTS04].

Use:

```text
VISIBLE EVALUATION / COMPARISON INFORMATION
+ POSSIBLE SEARCH-UNDERSTANDING INPUT
```

Do not turn it into a backend keyword list. Both fields must match the product and platform rules; the guide says inconsistent or noncompliant entries can be removed automatically. System suggestions still need factual checking. Missing text alone does not establish the cause of removal [TTS04].

### 5.6 Images / product gallery

Images help identify and evaluate the item. SKU-specific images can be associated with primary sales-attribute values and appear in product option galleries [TTS02].

Shop recommendation optimization also exposes image-quality requirements/issues in current US Seller Analytics [TTS05]. TikTok Shop Vietnam's Product Optimizer likewise exposes product-information and visibility-related issues involving names, descriptions, and images [TV02].

Keep:

```text
IMAGE / PRODUCT-INFO QUALITY ISSUE
≠ KNOWN RANKING WEIGHT

PROVIDER OPTIMIZATION OPPORTUNITY
≠ GUARANTEED EXPOSURE / CONVERSION LIFT
```

---

## 6. Shop Tab search and recommendation are different discovery systems

Current US Seller Academy exposes Shop Tab as a marketplace with search, personalized recommendations, browsing, campaigns, and shop/product pages [TTS05]. Analytics separates Shop Tab/search and recommendation-related performance. Current Vietnam Seller Center evidence independently supports product-level Shop Tab traffic analysis and product optimization diagnostics without disclosing an organic ranker [TV01][TV02].

Therefore:

```text
SHOP SEARCH
≠ SHOP RECOMMENDATION
```

and:

```text
SEARCH MATCHING GUIDANCE
≠ RECOMMENDATION RANKING RULE
```

### 6.1 Search

Supported evidence establishes that Search terms and Product highlights can help TikTok Shop search understand/match products [TTS04].

Exact current organic search pipeline remains UNKNOWN:

- candidate generation;
- lexical vs semantic matching;
- image or behavior representations;
- field weights;
- ranking objective;
- reranking;
- seller / shop / inventory / commercial constraints.

### 6.2 Recommendations

Seller Analytics currently identifies product recommendation opportunities/issues and says sellers can improve recommendation eligibility by addressing conditions such as image quality and stock [TTS05]. Vietnam Product Optimizer confirms that provider-side product optimization/visibility diagnostics also exist locally [TV02].

Therefore:

```text
MEETS RECOMMENDATION / QUALITY REQUIREMENTS
≠ RANKED HIGH
≠ EXPOSED
```

Do not infer a hidden ranker from eligibility or optimization diagnostics. The U.S. seller guide describes automatic Shop Tab channel inclusion for listed products; that is not proof of a recommendation impression [TTS05].

### 6.3 Product Card is a representation, not the product

Product cards can drive purchase outside short video/LIVE and appear in marketplace/recommendation contexts [TTS05][TTS06]. The Shop Tab guide classifies non-LIVE/non-video revenue as Product Card revenue. Do not equate that broad category with Shop Tab alone, or add the two as disjoint sources without verifying the reporting hierarchy [TTS05]. Vietnam Product Traffic also uses Product Card as a report/source context, reinforcing the need to preserve report semantics rather than treating the label as product identity [TV01].

Keep:

```text
PRODUCT OBJECT
≠ PRODUCT CARD
≠ SURFACE CONTAINING THE CARD
```

---

## 7. Video and product are independently persistent objects

TikTok Shop's linking behavior provides an unusually clear hybrid stress case.

The documented U.S. posting flow allows a video to link to [TTS07]:

```text
Product
Shop
Category
Collection
```

Eligible published videos can receive a first product link without re-uploading. The U.S. post-publish tool covers unlinked videos from the last 30 days, requires Commercial Music Library audio, a matching product, and content-policy compliance. It does not establish free replacement of an existing link. For unavailable linked products, use the distinct relinking conditions in section 9 / `tiktok-shop.relinking` [TTS07][TTS09].

Vietnam's current Link Products tool independently supports adding a first product link to eligible previously unlinked short videos within its documented window [TV03]. That local support does not establish replacement/editing of an existing link.

Therefore:

```text
VIDEO IDENTITY
≠ COMMERCE TARGET IDENTITY
```

and:

```text
VIDEO
--[links to / promotes]-->
PRODUCT / SHOP / CATEGORY / COLLECTION
```

The edge is consequential but is not a new durable primitive.

---

## 8. Product link / anchor is a representation of the commerce relation

When linking a product, creators can edit how the displayed product name appears in the documented US workflows [TTS07][TTS10]. The visible shopping-bag/cart anchor is presented within the content experience.

Keep:

```text
PRODUCT
≠ CONTENT↔PRODUCT LINK
≠ LINK LABEL / ANCHOR REPRESENTATION
```

This avoids treating a short anchor label as the canonical product title or identity.

### 8.1 Anchor state can change independently

Possible link/anchor states can include active, out of stock, delisted, invalid collaboration, blacklisted relationship, abnormal, relinked, or restored depending on supported feature state [TTS08].

Therefore:

```text
SAME VIDEO
≠ SAME COMMERCE EDGE STATE OVER TIME
```

---

## 9. Product Relinking proves content identity can survive target replacement

The documented U.S. Product Relinking feature preserves the existing video while replacing an unavailable target. It covers videos posted within six months with engagement during the last 30 days; some content violations must be resolved first. Check current account/feature eligibility and the abnormal-anchor reason. An absent notification can reflect missing suitable alternatives or unmet eligibility, rather than a defect [TTS08].

Preserving the video does not guarantee unchanged future traffic, engagement, or earnings. The older first-link FAQ is not a blanket prohibition of this later, specifically scoped relinking workflow [TTS08][TTS09].

If the original product later restocks, it can automatically re-anchor; both original and replacement may appear, with up to multiple products anchored to one video in the documented US feature [TTS08].

Current Vietnam evidence supports the first-link flow for eligible unlinked videos but does **not** establish general availability of this dedicated unavailable-target relinking/replacement behavior [TV03]. Therefore:

```text
US PRODUCT RELINKING FLOW
≠ GENERAL VIETNAM RELINK / REPLACEMENT AVAILABILITY
```

For a Vietnam execution request involving an already-linked product, verify current account/market capability rather than importing the U.S. workflow or declaring it universally unavailable.

This gives a direct state transition in the documented U.S. feature:

```text
VIDEO V
   │
   ├── at t0 → PRODUCT A
   │              active
   │
   ├── t1 → A unavailable
   │       edge/anchor abnormal
   │
   ├── t2 → PRODUCT B relinked
   │
   └── t3 → A restocks / re-anchors
```

The content object is still V.

Therefore:

```text
SAME CONTENT OBJECT
+ DIFFERENT COMMERCE TARGET
≠ NEW CONTENT IDENTITY
```

### 9.1 Product-content alignment is an edge-validity constraint

TikTok requires the newly linked product to match the video in visuals/function/key features/brand/category alignment in the documented US relinking flow [TTS08].

Treat this as:

```text
VIDEO --[depicts / demonstrates / promotes]--> PRODUCT
```

with truth/consistency requirements.

A platform recommendation that proposes a product does not guarantee factual alignment; the creator remains responsible for checking it.

---

## 10. Creator-side product recommendation is not shopper-side feed ranking

The post-publish Link Products tool can suggest products based on video-content relevance, product performance, and creator interests/engagement in the documented US flow [TTS09]. Current Vietnam Link Products evidence independently confirms a creator-side system-recommended-product flow for eligible videos [TV03].

This is a recommender with:

```text
INPUT CONTEXT
video + creator state

CANDIDATE OBJECT CLASS
products

OUTPUT
product-link suggestions
```

It is strong evidence that TikTok can recommend different object classes, but its scope is narrow.

Do **not** infer:

```text
CREATOR PRODUCT-LINK RECOMMENDER SIGNALS
→ SHOPPER FOR YOU RANKING SIGNALS
```

or:

```text
→ SHOP TAB ORGANIC PRODUCT RANKING
```

---

## 11. Seller, creator, brand, and affiliate roles remain distinct

TikTok Shop allows creators to select/promote seller products, use showcase/product marketplace/targeted invitations, and earn commission on attributed orders [TTS10].

Use separate actor roles when material:

```text
SELLER / SHOP
commercial provider

BRAND / MANUFACTURER
possible product-claim authority

CREATOR
publisher / demonstrator

AFFILIATE RELATION
commission / commercial edge

PLATFORM
mediator / attribution system
```

Keep:

```text
SELLER
≠ CREATOR
≠ CLAIM SOURCE
```

A creator does not gain first-person product experience or authority merely from having an affiliate link.

---

## 12. Content meaning ≠ product-link representation ≠ product truth

In shoppable content, several layers coexist:

```text
VIDEO CONTENT MEANING
what is demonstrated / claimed / shown

PRODUCT-LINK REPRESENTATION
anchor name / shopping icon / product card

PRODUCT / SKU FACTS
what the product actually is

COMMERCIAL STATE
price / stock / seller / shipping / promotion
```

A mismatch can create both user confusion and policy risk.

Do not repair a mismatched product-content relationship by merely renaming the anchor.

---

## 13. Measurement must preserve commerce-entry provenance

TikTok's current Product Traffic Analysis can segment traffic across contexts including Seller LIVE, Video, Product Card, Affiliate, and Shop Tab [TTS06]. Current Vietnam Product Traffic independently documents the same need to preserve source/context and report-specific metric definitions in the Vietnam Seller Center [TV01].

Therefore a product-level order aggregate can mix very different exposure regimes.

Use:

```text
ORDER / GMV
+ source surface
+ content / card / affiliate provenance
+ product / SKU state
+ time
+ attribution rule
```

before learning from performance. Preserve the report, metric version, event unit, PV/UV mode and aggregation. Shop-page conversion uses unique page views [TTS05]; product CTOR uses clicks and SKU orders. Estimated customers are daily-deduplicated sums, not period-unique people. Product Traffic GMV includes canceled/refunded orders; refund timing can differ from purchase timing [TTS06][TV01].

Do not silently join changed metric definitions across an upgrade. The documented Product Traffic material contains definition/label details that should be verified before calculation rather than normalized by assumption. Missing metrics are not zero, and a projected rollout is not evidence of availability [TTS06][TV01].

### 13.1 Suggested observation chain

For shoppable video:

```text
video exposure
→ relevant product-link / anchor opportunity
→ product-link click
→ PDP / product evaluation
→ SKU selection
→ cart / order / payment
→ completion / return / refund
```

Do not equate video views with product exposure when the shopper may not have reached/seen the anchor meaningfully.

### 13.2 Attribution ≠ incrementality

An affiliate or creator order attributed through a product link is reporting credit under TikTok's rules.

Keep:

```text
ATTRIBUTED CREATOR ORDER
≠ PROOF CREATOR CAUSED AN INCREMENTAL ORDER
```

without a causal design.

---

## 14. Diagnosing weak TikTok Shop performance

Check the relevant branch rather than rewriting everything.

```text
1. METRIC / SOURCE
Shop Search, recommendation, Product Card, video, LIVE,
affiliate, paid ads, shop page?
For cross-report comparisons, check units/denominators, aggregation and
transaction timing in section 13 / tiktok-shop.measurement before interpreting change.

2. PRODUCT / SKU STATE
Same product status, category, product attributes,
sales attributes, price, inventory, SKU images?
For version discrepancies or pending prerequisites, use section 3 /
tiktok-shop.status; distinguish live/draft/review data and the reported reason.

3. SEARCH REPRESENTATION
Same title, Search terms, Product highlights, images,
category/attributes?

4. RECOMMENDATION / PRODUCT-QUALITY ELIGIBILITY
Any image-quality, stock, product-quality or other explicit issue?
In Vietnam, Product Optimizer can provide local issue/opportunity evidence;
do not convert that evidence into a hidden ranking weight [TV02].

5. CONTENT-COMMERCE EDGE
Same video? same linked target? anchor active/OOS/relinked?
First attachment or unavailable-target replacement? Use sections 7/9 or
tiktok-shop.content-product-identity / tiktok-shop.relinking for eligibility.
If in Vietnam, current first-link support does not prove U.S.-style replacement;
verify current market/account capability [TV03].
Does content still truthfully match product?

6. ACTOR / COMMERCIAL RELATION
Same seller, creator, showcase, affiliate/collaboration plan?

7. TRAFFIC MIX
Same Video/LIVE/Product Card/Affiliate/Shop Tab mix?
Use current Vietnam Product Traffic definitions when the account is Vietnamese [TV01].

8. TIME / MARKET / FEATURE REGIME
Same country and feature rollout? Search terms / relinking behavior changed?

9. COMPETING EXPLANATIONS
What else changed?

10. DISCRIMINATING CHECK
What current analytics/API/link-state evidence best separates causes?
```

Use Chapter 05 for causal attribution.

---

## 15. Fast paths

### Product title / listing fields

```text
identify product vs SKU scope
→ preserve verified facts
→ use category-appropriate title/attributes
→ use Search terms only for relevant matching vocabulary where available
→ use Product highlights for concise visible product value
→ do not invent ranking weights
```

### Shoppable-video product link

```text
verify video-product factual alignment
→ identify the supported target type for the current market/workflow
→ choose truthful link / anchor representation where supported
→ distinguish new attachment from replacement and check applicable eligibility
→ publish / link within the authorized task
```

For Vietnam, current evidence supports a first product link on eligible previously unlinked videos in the documented flow [TV03]. Do not silently promote that into general link replacement.

### Relink an unavailable product

```text
preserve original video identity
→ verify current market/account relinking capability
→ verify why anchor is abnormal and whether relinking is eligible
→ resolve any blocking content violation
→ choose genuinely matching replacement
→ re-check claims/visuals/brand/price-sensitive statements
→ relink when supported
→ observe before/after with state history
```

The detailed transition above is U.S.-documented. For Vietnam, verify current availability before execution [TTS08][TV03].

---

## 16. TikTok Shop-specific anti-folklore guardrails

```text
PRODUCT ATTRIBUTE
≠ SALES ATTRIBUTE
```

```text
PRODUCT ID
≠ SKU
≠ UNIVERSAL PRODUCT IDENTITY
```

```text
SEARCH TERMS HELP MATCHING
≠ SEARCH TERMS HAVE KNOWN RANKING WEIGHT
```

```text
PRODUCT HIGHLIGHTS VISIBLE + SEARCH-RELEVANT
≠ KNOWN PRIORITY VS TITLE / ATTRIBUTES
```

```text
RECOMMENDATION / PRODUCT-QUALITY ELIGIBILITY
≠ HIGH RANK
≠ GUARANTEED EXPOSURE
```

```text
VIDEO
≠ PRODUCT
≠ PRODUCT ANCHOR
```

```text
SAME VIDEO + RELINKED PRODUCT
≠ NEW VIDEO IDENTITY
```

```text
CREATOR-SIDE PRODUCT RECOMMENDER
≠ SHOPPER FYP / SHOP TAB RANKER
```

```text
HIGH VIDEO ENGAGEMENT
≠ HIGH PRODUCT PURCHASE INTENT
```

```text
ATTRIBUTED AFFILIATE SALE
≠ INCREMENTAL SALE
```

```text
CURRENT US ACADEMY FEATURE
≠ EVERY TIKTOK SHOP MARKET
```

```text
US PRODUCT RELINKING FLOW
≠ GENERAL VIETNAM RELINK / REPLACEMENT AVAILABILITY
```

```text
VIETNAM PRODUCT OPTIMIZER GUIDANCE
≠ DISCLOSED ORGANIC RANKING FORMULA
```

---

## 17. Explicit UNKNOWNs

Preserve as unknown unless fresh evidence establishes otherwise:

- complete current Shop Tab organic search retrieval/ranking architecture;
- complete Shop Tab recommendation architecture/objectives;
- exact field weights for title, Search terms, highlights, attributes, images, seller/shop state, price, stock, sales or reviews;
- exact relation between Product Card recommendation eligibility and ranking position;
- exact shopper For You ranking effect of shoppable links or commerce outcomes;
- exact relation between creator-side product suggestions and shopper-side recommendation models;
- exact paid/organic composition rules on Shop surfaces;
- every market's rollout state for Search terms, Product highlights, Product Relinking, product families, and analytics; Vietnam now has direct evidence for Product Traffic, Product Optimizer, and the scoped first-link flow, but general U.S.-style relinking remains unestablished by the reviewed Vietnam source;
- causal effect of adding/relinking a product on incremental GMV without a valid experiment.

---

## 18. Final TikTok Shop check

1. Are product and SKU/variant roles separated correctly?
2. Are product attributes and sales attributes being used for their documented scopes?
3. Is price/stock treated as SKU/market/warehouse state rather than timeless product truth?
4. Are Search terms, title, Product highlights, attributes and images allocated by distinct jobs?
5. Is Shop Search kept separate from Shop recommendation?
6. Is recommendation/product-quality eligibility being mistaken for ranking or guaranteed exposure?
7. Is Product Card kept separate from product identity and surface?
8. In shoppable content, are video, commerce target, commerce edge, and anchor representation separate?
9. If relinking, is video identity preserved while edge history and product-content consistency are updated, and is the capability verified for the current market/account?
10. Are seller, creator, brand, affiliate relation and claim authority separated?
11. Is creator-side product recommendation kept separate from shopper-side ranking?
12. Are metrics segmented by Video/LIVE/Card/Affiliate/Shop Tab when material?
13. Is attribution being distinguished from incrementality?
14. Is US Seller Academy evidence being transferred to another market without verification, or is available local evidence such as `[TV01–TV03]` being used where it actually applies?
15. Are current feature dates / rollout states fresh enough?
16. Are undisclosed internals left UNKNOWN?
17. Is Chapter 08 loaded only when the content/social environment actually matters?

TikTok Shop should be reasoned as a hybrid graph, not as “TikTok SEO plus a buy button.”

---

## Evidence

See `../../references/commerce/tiktok-shop-evidence.md` for `[TTS01–TTS10]` source definitions and evidence boundaries, and `../../references/commerce/tiktok-shop-vietnam-evidence.md` for `[TV01–TV03]` Vietnam applicability evidence.
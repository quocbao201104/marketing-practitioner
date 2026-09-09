# TikTok Shop Commerce / Product-Discovery Evidence Ledger

Source identifiers for `../../platforms/commerce/tiktok-shop.md`.

Current product behavior is time-sensitive and market-scoped. Baseline review: 2026-08-23. Selected passages under TTS01-TTS10 were checked in two bounded follow-ups on 2026-09-09; uninspected specifications and account behavior retain their prior status. U.S. Academy guidance is not evidence of every market. API follow-up relied on indexed official passages because direct extraction returned JavaScript shells.

## [TTS01] TikTok Shop Partner API — Products API overview

TikTok Shop Partner Center. **Products API Overview.** Reviewed 2026-08-23.

Use: current implementation semantics for TikTok Shop product IDs, product status, categories, product attributes, sales attributes, variants/SKUs, and product review/edit states. Product attributes describe the product as a whole; sales attributes define variants/SKUs.

Verification locator (2026-09-09): [Products API overview](https://partner.tiktokshop.com/docv2/page/products-api-overview), indexed review/version paragraph. It supports keeping the pre-edit live snapshot separate from the reviewed edit.

Boundary: API object boundaries are implementation facts, not durable commerce primitives; markets and product types differ. The overview uses older parameter vocabulary; use the relevant endpoint reference for execution.

## [TTS02] TikTok Shop Partner API — Get Product / attributes / global product

TikTok Shop Partner Center. **Get Product; Get Attributes; Get Global Attributes; Get Global Product.** Reviewed 2026-08-23.

Use: product_id / SKU structure, product attributes vs sales attributes, product-family data where available, standardized identifier codes (GTIN/EAN/UPC/ISBN/JAN), SKU images, local/global product relationships, and market-scoped product state.

Verification locators (2026-09-09, indexed official text): [Get Product v202309](https://partner.tiktokshop.com/docv2/page/get-product), version selectors; [invite-only category change](https://partner.tiktokshop.com/docv2/page/streamlining-of-invite-only-product-categories), U.S. local-seller audit prerequisites. These support version-aware comparison and the pending/pre-approved distinction; they do not revalidate the full global-product schema. The endpoint prose makes draft and under-review selection mutually exclusive, despite an illustrative request containing both; follow the parameter contract.

Boundary: a TikTok local product ID or global_product object is a TikTok commerce-management identity, not a universal physical-product identity. Indexed evidence is not a live endpoint or account test.

## [TTS03] TikTok Shop Partner API — pricing and inventory

TikTok Shop Partner Center. **Product pricing; Get Product.** Reviewed 2026-08-23.

Use: prices are set at SKU level; sale/list/tax-exclusive/unit price semantics vary by market; inventory can be warehouse/SKU scoped. Vietnam/Indonesia/Japan currency precision examples are market-specific.

Verification locators (2026-09-09, indexed official text): [pricing](https://partner.tiktokshop.com/docv2/page/product-pricing), [Update Inventory v202309](https://partner.tiktokshop.com/docv2/page/update-inventory-202309), and [Edit Product v202309](https://partner.tiktokshop.com/docv2/page/edit-product-202309). Inspected currency/seller-mode scope, inventory constraints, and the price/stock re-audit exception. Direct extraction returned JavaScript shells.

Boundary: API price fields do not establish every promotion, voucher, buyer-relative checkout, or recommendation rule. No account or update was tested.

## [TTS04] TikTok Shop Academy — Search terms and Product highlights

TikTok Shop Seller Academy US. **Search terms and Product highlights.** Published June 12, 2026.

Use: current US evidence that optional Search terms provide backend descriptors/synonyms used to help search understand/match products, while Product highlights are visible concise product benefits/features on PDP and also help search understanding. Both must remain relevant and compliant.

Direct source rechecked 2026-09-09: [field guide](https://seller-us.tiktok.com/university/essay?knowledge_id=240361624880910), field instructions and FAQ. Distinguish optionality, suggested presentation and the content-removal condition. No universal limit is inferred from the comparison with title restrictions.

Boundary: evidence is US-market seller guidance and does not establish exact retrieval/ranking weights or every market's field availability.

## [TTS05] TikTok Shop Academy — Shop Tab & Search Analytics / Seller Guide

TikTok Shop Seller Academy US. **Shop Tab & Search Analytics** (May 22, 2026); **The Seller Guide to Shop Tab Success** (May 14, 2026).

Use: current US evidence that Shop Tab supports search, personalized recommendations/browsing, campaigns and product discovery; analytics separates traffic/performance sources and exposes metrics such as impressions, orders, GMV, items sold and conversion. Recommendation eligibility/optimization can surface issues such as image quality or insufficient stock.

Direct sources rechecked 2026-09-09: [analytics](https://seller-us.tiktok.com/university/essay?knowledge_id=6276577063585582), report-specific metrics/breakdown/FAQ; [seller guide](https://seller-us.tiktok.com/university/essay?knowledge_id=8750609034250026), channel inclusion and optimization. The latter is advice, not a controlled effectiveness study.

Boundary: eligibility requirements or seller optimization guidance do not reveal organic recommendation ranker weights. Similar labels across reporting tabs do not prove identical scopes or disjoint categories.

## [TTS06] TikTok Shop Academy — Product Traffic Analysis

TikTok Shop Seller Academy US. **Seller Analytics | Product Traffic Analysis.** Published May 9, 2026.

Use: current evidence that product traffic can be segmented across Seller LIVE, Video, Product Card, Affiliate and Shop Tab contexts, helping preserve exposure/channel provenance before interpreting sales.

Direct source rechecked 2026-09-09: [Product Traffic Analysis](https://seller-us.tiktok.com/university/essay?knowledge_id=8090478953219854), metric-change tables and FAQ. Preserve the unresolved Unique CTOR label/definition conflict. Announced improvements are not observed availability.

Boundary: reporting attribution is not causal incrementality. Definitions are report- and version-scoped; the guide is not an account reconciliation.

## [TTS07] TikTok Shop Academy — video/product/shop/category/collection links

TikTok Shop Seller Academy US. **How to Link Products to Videos.** Baseline recorded June 10, 2026; accessed article displays August 5, 2026. Selected body passages rechecked 2026-09-09.

Use: content can link to Product, Shop, Category or Collection; product links can be added to eligible videos after posting without deleting/re-uploading; visible link display names can be edited. Strong evidence for `CONTENT OBJECT ≠ COMMERCE TARGET ≠ LINK / ANCHOR REPRESENTATION`.

Direct source: [linking guide](https://seller-us.tiktok.com/university/essay?knowledge_id=5804034343962411), posting and published-video sections. Read the latter with TTS09 for first-link conditions; the broad target choices in the posting flow do not prove identical post-publish editing capabilities.

Boundary: linking capability does not establish For You ranking effects.

## [TTS08] TikTok Shop Academy — Product Relinking

TikTok Shop Seller Academy US. **How to Relink Products.** Published December 1, 2025; current guide reviewed 2026-08-23.

Use: when linked products become unavailable for supported reasons, eligible videos can retain content identity while creators replace the commerce target; original products can re-anchor after restocking, and multiple products can appear. The platform tracks abnormal anchor status and requires product-content alignment.

Direct source rechecked 2026-09-09: [relinking guide](https://seller-us.tiktok.com/university/essay?knowledge_id=3759443559679790), Feature Overview, Key Features, and FAQs. Its dedicated unavailable-target workflow is later than TTS09.

Boundary: feature eligibility/time windows can change; relinking does not imply the new product is semantically identical or safe without verification. Benefit language about preserving traffic/earnings is not a measured guarantee of future outcomes. No live account or restored anchor was inspected.

## [TTS09] TikTok Shop Academy — post-publish product suggestions

TikTok Shop Seller Academy US. **How to Link Products to Videos After You've Posted.** Published November 21, 2025.

Use: scoped product-link recommendation system suggests products based on video-content relevance, product performance, and creator interests/engagement. Demonstrates a recommender whose input object is a video and output candidates are products.

Direct source rechecked 2026-09-09: [post-publish guide](https://seller-us.tiktok.com/university/essay?knowledge_id=5178002307598122), workflow and FAQ. Its first-attachment conditions remain distinct from TTS08; its November 2025 testing/no-replacement wording must not erase the December dedicated relinking flow. Neither source proves every account has the feature.

Boundary: this is creator-side link-product recommendation, not shopper For You ranking or Shop Tab ranking.

## [TTS10] TikTok Shop Academy — creator/affiliate product linking

TikTok Shop Seller Academy US. **How to Add a Product Link to Your Video** and current creator-product marketplace/showcase guidance. Reviewed 2026-08-23.

Use: creators can select seller products, edit displayed product-link names, promote products for commission, use showcase/product marketplace/targeted invitations. Supports separating seller, creator, product and affiliate/commercial relationship roles.

Selected verification locator (2026-09-09): [Add a Product Link](https://seller-us.tiktok.com/university/essay?knowledge_id=4393475827222318), creator workflows and display-name steps. Broader affiliate terms and commission rules were not freshly reviewed.

Boundary: commission attribution does not prove incremental sales.

## Evidence-use rules

```text
VIDEO / CONTENT OBJECT
≠ PRODUCT / COMMERCE OBJECT
≠ CONTENT↔PRODUCT EDGE

PRODUCT
≠ PRODUCT-LINK / ANCHOR REPRESENTATION

PRODUCT ATTRIBUTE
≠ SALES ATTRIBUTE / VARIANT ATTRIBUTE

PRODUCT ID
≠ UNIVERSAL PRODUCT IDENTITY

SKU PRICE / INVENTORY STATE
≠ TIMELESS PRODUCT FACT

SEARCH TERMS HELP MATCHING
≠ FIXED ORGANIC RANKING WEIGHT

PRODUCT HIGHLIGHTS VISIBLE + SEARCH-RELEVANT
≠ DISCLOSED PRIORITY VS TITLE / ATTRIBUTES

RECOMMENDATION ELIGIBILITY
≠ HIGH RANK / EXPOSURE

CREATOR-SIDE PRODUCT SUGGESTION
≠ SHOPPER FYP / SHOP RANKING

ATTRIBUTED AFFILIATE ORDER
≠ INCREMENTAL CAUSAL SALE
```

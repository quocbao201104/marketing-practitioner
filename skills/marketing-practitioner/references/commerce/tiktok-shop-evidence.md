# TikTok Shop Commerce / Product-Discovery Evidence Ledger

Source identifiers for `../../platforms/commerce/tiktok-shop.md`.

Current product behavior is time-sensitive and market-scoped. Reviewed 2026-08-23, with US Seller Academy sources used where explicitly marked and Partner API docs used for broader market/object semantics.

## [TTS01] TikTok Shop Partner API — Products API overview

TikTok Shop Partner Center. **Products API Overview.** Reviewed 2026-08-23.

Use: current implementation semantics for TikTok Shop product IDs, product status, categories, product attributes, sales attributes, variants/SKUs, and product review/edit states. Product attributes describe the product as a whole; sales attributes define variants/SKUs.

Boundary: API object boundaries are implementation facts, not durable commerce primitives; markets and product types differ.

## [TTS02] TikTok Shop Partner API — Get Product / attributes / global product

TikTok Shop Partner Center. **Get Product; Get Attributes; Get Global Attributes; Get Global Product.** Reviewed 2026-08-23.

Use: product_id / SKU structure, product attributes vs sales attributes, product-family data where available, standardized identifier codes (GTIN/EAN/UPC/ISBN/JAN), SKU images, local/global product relationships, and market-scoped product state.

Boundary: a TikTok local product ID or global_product object is a TikTok commerce-management identity, not a universal physical-product identity.

## [TTS03] TikTok Shop Partner API — pricing and inventory

TikTok Shop Partner Center. **Product pricing; Get Product.** Reviewed 2026-08-23.

Use: prices are set at SKU level; sale/list/tax-exclusive/unit price semantics vary by market; inventory can be warehouse/SKU scoped. Vietnam/Indonesia/Japan currency precision examples are market-specific.

Boundary: API price fields do not establish every promotion, voucher, buyer-relative checkout, or recommendation rule.

## [TTS04] TikTok Shop Academy — Search terms and Product highlights

TikTok Shop Seller Academy US. **Search terms and Product highlights.** Published June 12, 2026.

Use: current US evidence that optional Search terms provide backend descriptors/synonyms used to help search understand/match products, while Product highlights are visible concise product benefits/features on PDP and also help search understanding. Both must remain relevant and compliant.

Boundary: evidence is US-market seller guidance and does not establish exact retrieval/ranking weights or every market's field availability.

## [TTS05] TikTok Shop Academy — Shop Tab & Search Analytics / Seller Guide

TikTok Shop Seller Academy US. **Shop Tab & Search Analytics** (May 22, 2026); **The Seller Guide to Shop Tab Success** (May 14, 2026).

Use: current US evidence that Shop Tab supports search, personalized recommendations/browsing, campaigns and product discovery; analytics separates traffic/performance sources and exposes metrics such as impressions, orders, GMV, items sold and conversion. Recommendation eligibility/optimization can surface issues such as image quality or insufficient stock.

Boundary: eligibility requirements or seller optimization guidance do not reveal organic recommendation ranker weights.

## [TTS06] TikTok Shop Academy — Product Traffic Analysis

TikTok Shop Seller Academy US. **Seller Analytics | Product Traffic Analysis.** Published May 9, 2026.

Use: current evidence that product traffic can be segmented across Seller LIVE, Video, Product Card, Affiliate and Shop Tab contexts, helping preserve exposure/channel provenance before interpreting sales.

Boundary: reporting attribution is not causal incrementality.

## [TTS07] TikTok Shop Academy — video/product/shop/category/collection links

TikTok Shop Seller Academy US. **How to Link Products to Videos.** Published June 10, 2026.

Use: content can link to Product, Shop, Category or Collection; product links can be added to eligible videos after posting without deleting/re-uploading; visible link display names can be edited. Strong evidence for `CONTENT OBJECT ≠ COMMERCE TARGET ≠ LINK / ANCHOR REPRESENTATION`.

Boundary: linking capability does not establish For You ranking effects.

## [TTS08] TikTok Shop Academy — Product Relinking

TikTok Shop Seller Academy US. **How to Relink Products.** Published December 1, 2025; current guide reviewed 2026-08-23.

Use: when linked products become unavailable for supported reasons, eligible videos can retain content identity while creators replace the commerce target; original products can re-anchor after restocking, and multiple products can appear. The platform tracks abnormal anchor status and requires product-content alignment.

Boundary: feature eligibility/time windows can change; relinking does not imply the new product is semantically identical or safe without verification.

## [TTS09] TikTok Shop Academy — post-publish product suggestions

TikTok Shop Seller Academy US. **How to Link Products to Videos After You've Posted.** Published November 21, 2025.

Use: scoped product-link recommendation system suggests products based on video-content relevance, product performance, and creator interests/engagement. Demonstrates a recommender whose input object is a video and output candidates are products.

Boundary: this is creator-side link-product recommendation, not shopper For You ranking or Shop Tab ranking.

## [TTS10] TikTok Shop Academy — creator/affiliate product linking

TikTok Shop Seller Academy US. **How to Add a Product Link to Your Video** and current creator-product marketplace/showcase guidance. Reviewed 2026-08-23.

Use: creators can select seller products, edit displayed product-link names, promote products for commission, use showcase/product marketplace/targeted invitations. Supports separating seller, creator, product and affiliate/commercial relationship roles.

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

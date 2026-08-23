# Google Commerce / Shopping Evidence Ledger

Source identifiers for `../../platforms/commerce/google-shopping.md`.

Current product behavior is time-sensitive. Reviewed 2026-08-23.

## [G01] Merchant API — ProductInput and processed Product

Google Merchant API. **ProductInputsService; Products Service; Make frequent updates to your products.** Current documentation updated through August 2026.

Use: `ProductInput` is merchant/data-source input; rules, supplemental sources, automatic improvements, merging, and validation can produce a processed `Product` later returned by Products Service.

Boundary: does not disclose all Search/Shopping retrieval or ranking logic.

## [G02] Merchant Center — product data specification and identity fields

Google Merchant Center Help. **Product data specification; ID `[id]`; Item group ID `[item_group_id]`; About unique product identifiers; Brand `[brand]`.** Reviewed 2026-08-23.

Use: current field semantics for merchant-local product IDs, product groups/variants, GTIN, brand, MPN, variant attributes, item-group title, variant options, and other structured product data.

Boundary: field requirements / recommendations do not equal ranking weights.

## [G03] Merchant Center — title and product-information fields

Google Merchant Center Help. **Title `[title]` and structured title `[structured_title]`; Product data specification; conversational attributes.** Reviewed 2026-08-23.

Use: title is a prominent free-listing/ad representation and should clearly identify the product; current product-data specifications also expose structured product-detail, product-highlight, question-and-answer, related-product, and other product-information fields in supported contexts.

Boundary: visible prominence and data completeness do not establish a fixed organic ranking boost.

## [G04] Merchant Center — product images

Google Merchant Center Help. **Image link `[image_link]`; Product data specification update 2026.** Reviewed 2026-08-23.

Use: the primary product image is required product data and appears to potential customers in ads/free listings; additional images can represent other views. Current image requirements and future enforcement dates are time-sensitive.

Boundary: image requirements / representation roles do not establish Lens or organic ranking weights.

## [G05] Google Search Central / Schema.org — ProductGroup, Product, variants, and Offer

Google Search Central. **Product Variant Structured Data (`ProductGroup`, `Product`).** Schema.org. **ProductGroup; ProductModel; isVariantOf; Offer.** Reviewed 2026-08-23.

Use: current structured-data support for grouping variants with `ProductGroup`, `hasVariant` / `isVariantOf`, shared group properties, variant-identifying attributes, and nested offer information.

Boundary: structured-data eligibility is not guaranteed display and is not a ranking specification.

## [G06] Free listings / Shopping Graph surfaces

Google Merchant Center / Google Shopping Help. **Free listings for products; Sources of shopping info.** Reviewed 2026-08-23.

Use: product information from merchants/brands/content providers can appear across Search, Shopping, Google Images, Lens, YouTube, and AI-driven experiences; Google Images/Lens can surface similar purchasable products with rich product snippets.

Boundary: surface eligibility and product-data use do not establish one shared ranking algorithm across surfaces.

## [G07] AI Mode, Gemini, and conversational shopping

Google. **NRF 2026 remarks; AI Mode shopping updates; Google Shopping / agentic-commerce updates.** Reviewed 2026-08-23.

Use: current product-level evidence that Shopping Graph information supports conversational shopping in AI Mode and Gemini; Google describes query fan-out / conversational narrowing in AI Mode shopping and product discovery moving beyond one keyword query.

Boundary: public product descriptions do not expose complete retrieval/ranking internals, query fan-out details, or field weights.

## [G08] Google Shopping result-generation disclosure

Google Shopping Help. **Understand how shopping results are generated.** Reviewed 2026-08-23.

Use: Google states that Shopping results are ranked based on relevance, search terms, and other Google activity, with personalization possible; some recommendation surfaces also consider signals such as relevance, ratings, price, and product features. Sponsored results are labeled.

Boundary: this is a high-level product disclosure, not a complete organic ranking formula. Do not convert listed factors into deterministic seller tactics or assume the same factors/weights on Search, Images, Lens, YouTube, AI Mode, ads, or every recommendation module.

## Evidence-use rules

```text
MERCHANT FIELD SEMANTICS
≠ ORGANIC RANKING WEIGHT

PRODUCTINPUT
≠ PROCESSED PRODUCT

PRODUCT GROUP
≠ VARIANT

PRODUCT / VARIANT
≠ OFFER

STRUCTURED-DATA ELIGIBLE
≠ GUARANTEED RICH RESULT / LISTING EXPOSURE

SHOPPING RESULT DISCLOSURE
≠ COMPLETE SEARCH / AI MODE / LENS ALGORITHM

SPONSORED
≠ ORGANIC
```

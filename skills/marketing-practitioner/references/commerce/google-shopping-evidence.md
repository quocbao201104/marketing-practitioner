# Google Commerce / Shopping Evidence Ledger

Source identifiers for `../../platforms/commerce/google-shopping.md`.

Current product behavior is time-sensitive. Reviewed 2026-08-23.

## [G01] Merchant API — ProductInput and processed Product

Google Merchant API. **ProductInputsService; Products Service; Make frequent updates to your products.** Current documentation updated through August 2026.

Use: `ProductInput` is merchant/data-source input; rules, supplemental sources, automatic improvements, merging, and validation can produce a processed `Product` later returned by Products Service.

Boundary: does not disclose all Search/Shopping retrieval or ranking logic.

Selected verification, 2026-09-08: inspected the resource descriptions and processing-delay note in [ProductInput](https://developers.google.com/merchant/api/reference/rest/products_v1/accounts.productInputs), and the `ProductStatus`, `DestinationStatus`, and `ItemLevelIssue` definitions in [Product](https://developers.google.com/merchant/api/reference/rest/products_v1/accounts.products). Processed retrieval can lag submission; approval and issues are scoped by reporting context and country. These pages do not establish any particular account's state or observed impressions.

Supplementary official guidance inspected on the same date:

- [Check product visibility and status](https://support.google.com/merchants/answer/12488713?hl=en): visibility controls and review/processing/approval/limited states; limitations can concern countries or marketing methods. Broad UI wording about showing on Google does not document a particular query impression or a universal mapping to every API status.
- [Automatic product updates](https://support.google.com/merchants/answer/12157888?hl=en): selected introduction, notes, operation, and FAQ passages. Landing-page information can update product data, but automation has coverage limits and does not replace regular accurate submissions. No guaranteed synchronization time or causal performance lift is inferred.

These are recovered verification locators, not confirmation of the original research inputs; the access date does not mean all referenced documentation was updated or fully revalidated then.

## [G02] Merchant Center — product data specification and identity fields

Google Merchant Center Help. **Product data specification; ID `[id]`; Item group ID `[item_group_id]`; About unique product identifiers; Brand `[brand]`.** Reviewed 2026-08-23.

Use: current field semantics for merchant-local product IDs, product groups/variants, GTIN, brand, MPN, variant attributes, item-group title, variant options, and other structured product data.

Boundary: field requirements / recommendations do not equal ranking weights.

Supplementary landing-page verification, 2026-09-08:

- [About landing-page requirements](https://support.google.com/merchants/answer/4752265?hl=en): selected product/data and page-load consistency passages and the correct-variant preselection best practice.
- [Price mismatch troubleshooting](https://support.google.com/merchants/answer/9773429?hl=en-GB): selected feed/site timing, structured-data mismatch, and premium-variant preselection passages.

Use: check the submitted URL's selected variant against that variant's product data, price, availability, and corresponding markup where present. Preserve the relevant market, time, pricing regime, and traffic/program scope. This does not justify substituting a cheaper sibling's price or prohibit subsequent shopper selection of another variant. The troubleshooting page's legacy API references and broader pricing cases were not adopted as current integration advice or universal pricing rules. Other G02 field requirements were not fully revalidated in this supplementary review.

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

Selected verification, 2026-09-08: [Search Central product variants](https://developers.google.com/search/docs/appearance/structured-data/product-variants), grouping examples, variant Offer URLs/prices, and technical identifier/canonical guidelines. Supported single-page examples use URLs that preselect variants; they do not require a separate physical page for each variant. This is Search structured-data guidance, distinct from Merchant Center submission requirements. No site/schema execution, Schema.org-wide review, or display guarantee is established.

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

## [G09] Merchant Center — conversational product attributes

Google Merchant Center Help. **How to use conversational attributes; Popularity rank `[popularity_rank]`; Related product `[related_product]`.** Reviewed 2026-08-23.

Direct sources:

- `https://support.google.com/merchants/answer/17085370?hl=en`
- `https://support.google.com/merchants/answer/17085297?hl=en`
- `https://support.google.com/merchants/answer/17085213?hl=en`

Use: Google now exposes optional conversational attributes including `question_and_answer`, `document_link`, `related_product`, `item_group_title`, `variant_option`, and `popularity_rank` to help AI systems / conversational agents understand product nuances and support AI-driven shopping experiences. `popularity_rank` is merchant-supplied and ranks a product's selling performance against other products in that merchant's own inventory. `related_product` is a merchant-declared relation such as accessory, spare part, often-bought-with, or substitute.

Boundaries:

- `popularity_rank` is **not** a Google organic Search ranking score;
- merchant-declared `related_product` is not the same as a platform-inferred substitute/complement relation or an observed co-purchase relation;
- field availability / conversational use does not disclose exact retrieval, relevance, or ranking weights.

Selected verification, 2026-09-08: inspected the overview's optional-field and duplication guidance, popularity definition/accuracy requirements, and related-product relation/identifier definitions. Existing description/detail/highlight coverage need not be duplicated into conversational attributes. These are provider semantics, not independently verified sales relations or effectiveness evidence.

Additional official specifications inspected:

- [Question and answer](https://support.google.com/merchants/answer/17085211): minimum requirements and best practices. Use truthful product information, keep offer-related prices/dates in their intended attributes, and avoid redundant facts already supplied in other attributes or a submitted document.
- [Document link](https://support.google.com/merchants/answer/17084656): definition, format, requirements, and best practices. Relevant product PDFs must be publicly crawlable without login, stable/non-expiring, and shared with the necessary marketing rights. An ordinary webpage or private attachment is not an equivalent carrier. Consult the full current specification for submission limits and encoding when actually implementing a feed.

These conditions do not certify document accuracy, variant applicability, successful extraction, or display. They do not authorize publication of private material or removal of required product attributes. Detailed group/variant specifications and API encodings were not fully revalidated; these are recovered verification sources, not proof of original research inputs.

## [G10] Google Merchant Center — UCP-powered checkout

Google Merchant Center Help. **About the Universal Commerce Protocol (UCP) and UCP-powered checkout feature on Google; How to onboard to UCP in Merchant Center.** Reviewed 2026-08-23.

Direct sources:

- `https://support.google.com/merchants/answer/16837055?hl=en`
- `https://support.google.com/merchants/answer/16992327?hl=en`

Use: participating eligible merchants can support UCP-powered checkout on surfaces such as AI Mode in Search and Gemini. Google states that the merchant remains seller of record; Google Pay can provide the secure payment flow, and Google's agentic checkout acts at the customer's direction while exchanging data with the merchant backend.

Boundary: checkout-surface mediation does not transfer merchant-of-record, payment-processing, fulfillment, returns, or customer-service responsibility by default. Availability is phased and merchant/market eligibility is time-sensitive.

## [G11] Merchant Center — AI performance insights, product details, and anti-keyword guidance

Google Merchant Center Help. **About AI performance insights; Product detail `[product_detail]`; Product highlight `[product_highlight]`; Product data specification.** Reviewed 2026-08-23.

Direct sources:

- `https://support.google.com/merchants/answer/17200695?hl=en`
- `https://support.google.com/merchants/answer/9218260?hl=en`
- `https://support.google.com/merchants/answer/9216100?hl=en`
- `https://support.google.com/merchants/answer/7052112?hl=en`

Use: Google says conversational shopping queries can be longer and more complex than keyword-style searches. Its current AI performance insights classify query types such as product-feature search, specification research, reviews, and mixed pricing/comparison intents; surface frequently used functional-benefit/product-feature terms; and identify popular structured specifications such as size, color, and material that may be missing from product data. Google recommends evaluating relevant terms for truthful inclusion in product titles/descriptions and filling relevant missing structured attributes. `product_detail` provides structured technical details and can help Google show individual products based on queries, including AI-driven surfaces. `product_highlight` is intended for concise relevant product benefits/features and explicitly says not to list keywords/search terms or use SEO keywords.

Boundaries:

- availability is scoped and time-sensitive; the selected verification below supersedes the earlier limited-pilot description;
- a product term, structured attribute, or field recommendation does not reveal an exact retrieval stage, model weight, or guaranteed ranking lift;
- `attribute completeness` or richer product data does not guarantee retrieval, recommendation, or exposure;
- integrating a shopper concept into title/description means expressing a **truthful relevant product concept**, not repeating query strings or manufacturing unsupported use-case claims.

Selected verification, 2026-09-08: inspected the AI insights page's availability, metrics/filters, stages/trends, and limitations. It specifies English queries for accounts in Australia, Canada, India, New Zealand, and the United States; coverage is organic AI Mode / AI Overviews traffic, not paid traffic or all Google AI surfaces. Preserve category/country/time filters and reporting lag. Share of voice uses the defined competitor set: `0` can mean insufficient impressions, `-` means no impressions data, and `100%` can occur without defined competitors. Changes in that set can affect comparisons; share of voice is not absolute growth or total market share. `Products showing` is a separate numerical count, whose zero means no products showing.

Also inspected product-detail and product-highlight roles, requirements, and best practices. Their guidance discourages duplicate information across attributes and redundant submission when the same information is in a submitted document. Product detail directs information already covered by dedicated attributes to those fields. This supports checking existing coverage before adding optional data, not removing required attributes or assuming document extraction succeeds. No account data, full product-specification audit, hidden ranking model, or causal lift was validated. Access date is not publication date.

## Evidence-use rules

```text
MERCHANT FIELD SEMANTICS
≠ ORGANIC RANKING WEIGHT
```

```text
PRODUCTINPUT
≠ PROCESSED PRODUCT
```

```text
PRODUCT GROUP
≠ VARIANT
```

```text
PRODUCT / VARIANT
≠ OFFER
```

```text
STRUCTURED-DATA ELIGIBLE
≠ GUARANTEED RICH RESULT / LISTING EXPOSURE
```

```text
SHOPPING RESULT DISCLOSURE
≠ COMPLETE SEARCH / AI MODE / LENS ALGORITHM
```

```text
MACHINE LEGIBILITY / PRODUCT-DATA COMPLETENESS
≠ KEYWORD DENSITY
≠ GUARANTEED AI VISIBILITY
```

```text
SEMANTIC / CONVERSATIONAL MATCHABILITY
≠ PROVEN ORGANIC RANKING BOOST
```

```text
MERCHANT-DECLARED POPULARITY_RANK
≠ GOOGLE ORGANIC SEARCH RANK
```

```text
MERCHANT-DECLARED RELATED_PRODUCT
≠ PLATFORM-INFERRED PRODUCT RELATION
≠ OBSERVED CO-PURCHASE RELATION
```

```text
AI MODE / GEMINI CHECKOUT SURFACE
≠ MERCHANT / SELLER OF RECORD
≠ PAYMENT / FULFILLMENT ROLE
```

```text
SPONSORED
≠ ORGANIC
```

# Amazon Commerce / Product-Discovery Evidence Ledger

Source identifiers for `../../platforms/commerce/amazon.md`.

Current product behavior is time-sensitive. Reviewed 2026-08-23.

## [A01] Amazon SP-API — catalog items and seller listings

Amazon Selling Partner API. **Manage Product Listings with the Selling Partner API; Catalog Items API; Listings Items API; searchListingsItems.** Reviewed 2026-08-23.

Use: current implementation/product evidence that Amazon exposes catalog contents through ASINs and separately exposes selling-partner listings through seller-owned SKUs. The listing workflow can search Amazon's catalog first, then create/update a seller listing; Listings Items responses can include attributes, issues, offers, and fulfillment availability.

Boundary: SP-API object boundaries are Amazon implementation facts, not a universal commerce ontology.

## [A02] Amazon SP-API — pricing, offers, and Featured Offer

Amazon Selling Partner API. **Product Pricing API; getListingOffers; getCompetitiveSummary; getFeaturedOfferExpectedPriceBatch.** Reviewed 2026-08-23; Product Pricing API documentation updated in August 2026 with release notes through April 1, 2026.

Use: Amazon exposes seller/ASIN offer and competitive-pricing information separately from catalog/listing identity. `getListingOffers` returns lowest-priced offers for a seller SKU; `getCompetitiveSummary` exposes featured buying options / lowest offers; Featured Offer Expected Price is location/market sensitive and Featured Offer placement is not guaranteed because competing offers and fulfillment/customer-location factors can change.

Boundary: API output and FOEP are pricing/offer-system evidence, not proof of a complete organic-search or Featured Offer algorithm.

## [A03] Amazon — 2026 title and Item Highlights update

Amazon Seller Central / News_Amazon. **Updates to improve your product titles begin on July 27.** Published/updated June 10, 2026; effective July 27, 2026.

Use: current seller-facing evidence that, except for media categories, product titles are limited to 75 characters including spaces from July 27, 2026. Amazon introduced Item Highlights with up to 125 characters for materials, recommended use cases, or comparison-relevant details; Item Highlights are described as searchable and visible with titles in search results and on product detail pages. Amazon also exposes AI-powered title / Item Highlights suggestions.

Boundary: title length and Item Highlights searchability/visibility do not establish relative retrieval/ranking priority or fixed organic weights.

## [A04] Amazon Seller Central — generic search terms / keywords

Amazon Seller Central staff / current Help references. **Use search terms effectively; Generic Keyword field guidance.** Current staff guidance reviewed 2026-08-23.

Use: current seller-facing evidence that Amazon has a Generic Keyword / search-terms field used by the search engine for matching; guidance recommends relevant synonyms/abbreviations/alternate names and discourages repetition, prohibited claims, brands/ASINs, and irrelevant terms. Current UI/policy details and byte/character limits can vary by marketplace/product type and should be re-checked before execution.

Boundary: generic keywords being indexed for matching does not establish a direct ranking boost, keyword-density rule, or priority over title/Item Highlights/attributes.

## [A05] Amazon Science — retrieval and ranking architecture

Delgado, J., & Greyson, P. (2023). **From structured search to learning-to-rank-and-retrieve.** Amazon Science.

Use: engineering/scientific parent that describes modern search/recommendation architecture as at least candidate selection/retrieval followed by candidate ordering/ranking. Strong for the architectural distinction; not a 2026 Amazon Store production contract.

## [A06] Amazon Science — semantic product search

Muhamed, A., Srinivasan, S., Teo, C. H., Cui, Q., Zeng, B., Chilimbi, T., & Vishwanathan, S. V. N. (2023). **Web-scale semantic product search with large language models.** Amazon Science / publication.

Use: product-search research describing a matching/retrieval stage over very large product catalogs followed by ranking, and dense semantic matching that improves exact/substitute product retrieval in online tests.

Boundary: published 2023 system evidence does not disclose current 2026 production models, field weights, or every Amazon marketplace/search surface.

## [A07] Amazon Science — product retrieval and behavioral / product context

Amazon Science, 2023 publications including **Improving product search with season-aware query-product semantic similarity**, **Using hypergraphs to improve product retrieval**, and related product-search work.

Use: evidence that Amazon product-search research can use semantic product/query representations, price/review context, seasonality, query-product behavioral graphs, clicks/purchases, and other contextual features in scoped retrieval/relevance systems.

Boundary: a feature appearing in one research model or A/B test does not establish a universal Amazon Search ranking factor or seller tactic.

## [A08] Amazon Shopping Queries / ESCI relevance framework

Amazon Science. **Shopping Queries Dataset / ESCI benchmark.** Released for KDD Cup 2022 and maintained as a product-search research asset.

Use: scientific/engineering evidence that query-product relevance can distinguish Exact, Substitute, Complement, and Irrelevant relationships; supports the principle that product relevance is semantic/relational and cannot be reduced to literal keyword presence.

Boundary: benchmark labels are not a complete production-ranking objective or 2026 algorithm description.

## [A09] Amazon Shop Direct and Buy for Me — external-store discovery regime

Amazon. **Amazon is making it easier for merchants to sell from external stores.** Published 2026; reviewed 2026-08-23.

Direct source: `https://www.aboutamazon.com/news/retail/amazon-shop-direct-external-stores`

Use: Shop Direct lets Amazon customers discover products from stores across the web, including products not currently sold in Amazon's Store. Amazon says Shop Direct includes more than 100 million products from more than 400,000 merchants. External merchants can sync catalog, pricing, and inventory through feeds. Customers can either follow Shop Direct to the merchant website or, for eligible items, use Buy for Me so Amazon's agentic AI completes the purchase from the merchant website on the customer's behalf. Merchant store names remain visible; merchants manage delivery, returns, exchanges, and customer service.

Boundary: this establishes an external-store discovery / transaction regime alongside native Amazon Store commerce. It does **not** prove that every externally discovered product lacks every Amazon-internal identifier or disclose Shop Direct's full retrieval/ranking architecture.

## [A10] Amazon Alexa for Shopping — agentic shopping capabilities

Amazon. **Alexa for Shopping / agentic AI shopping assistant.** Current 2026 product documentation reviewed 2026-08-23.

Direct source: `https://www.aboutamazon.com/news/retail/alexa-for-shopping-ai-assistant`

Use: Amazon's current shopping assistant can discover products from Amazon and external stores, build carts, track prices, and in supported cases perform price-triggered auto-buy or Buy for Me actions. This is evidence that discovery, shopper intent, delegated/automated action state, and completed purchase can be distinct.

Boundary: a product feature allowing auto-buy under configured conditions does not imply unrestricted authority for arbitrary purchases, nor does it disclose the exact authorization implementation or product-ranking system.

## Evidence-use rules

```text
ASIN / CATALOG ITEM
≠ SELLER SKU / LISTING

CATALOG PRODUCT IDENTITY
≠ SELLER OFFER / COMMERCIAL STATE

FEATURED OFFER
≠ FIXED PRODUCT PROPERTY

TITLE SEARCHABLE / VISIBLE
≠ TITLE HAS KNOWN FIXED RANKING PRIORITY

ITEM HIGHLIGHTS SEARCHABLE / VISIBLE
≠ KNOWN RELATIVE WEIGHT VS TITLE

GENERIC KEYWORDS USED FOR MATCHING
≠ KEYWORD-DENSITY OR DIRECT RANKING LAW

AMAZON SCIENCE SYSTEM / PAPER
≠ TIMELESS COMPLETE PRODUCTION CONTRACT

RETRIEVAL
≠ RANKING

RESEARCH FEATURE
≠ UNIVERSAL SELLER TACTIC

AMAZON PRODUCT DISCOVERY
≠ NECESSARILY NATIVE AMAZON STORE CATALOG / SELLER-LISTING / OFFER REGIME

SHOP DIRECT DISCOVERY REPRESENTATION
≠ EXTERNAL MERCHANT CHECKOUT / ORDER STATE

BUY FOR ME / AUTO-BUY CAPABILITY
≠ UNRESTRICTED USER AUTHORIZATION
```

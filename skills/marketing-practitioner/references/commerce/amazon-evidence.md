# Amazon Commerce / Product-Discovery Evidence Ledger

Source identifiers for `../../platforms/commerce/amazon.md`.

Current product behavior is time-sensitive. Baseline review: 2026-08-23. Selected operational passages and search-research sources under A01-A10 were checked in two bounded follow-ups on 2026-09-09. The entries distinguish accessed material from unverified policy/specification details. Access dates are not publication dates or whole-module certifications.

## [A01] Amazon SP-API — catalog items and seller listings

Amazon Selling Partner API. **Manage Product Listings with the Selling Partner API; Catalog Items API; Listings Items API; searchListingsItems.** Reviewed 2026-08-23.

Use: current implementation/product evidence that Amazon exposes catalog contents through ASINs and separately exposes selling-partner listings through seller-owned SKUs. The listing workflow can search Amazon's catalog first, then create/update a seller listing; Listings Items responses can include attributes, issues, offers, and fulfillment availability.

Verification locators (2026-09-09): [Listings Items API, Considerations](https://developer-docs.amazon/sp-api/docs/listings-items-api); [Listings APIs FAQ, processing questions](https://developer-docs.amazon/sp-api/docs/listings-apis-faq); [issues troubleshooting](https://developer-docs.amazon/sp-api/lang-en_EN/docs/listings-items-api-issues-troubleshooting). These support the distinctions between acceptance versus downstream processing and submitted versus live response data.

Boundary: SP-API object boundaries are Amazon implementation facts, not a universal commerce ontology. Vendor-specific FAQ statements about content priority do not establish universal seller precedence. No live listing was inspected.

## [A02] Amazon SP-API — pricing, offers, and Featured Offer

Amazon Selling Partner API. **Product Pricing API; getListingOffers; getCompetitiveSummary; getFeaturedOfferExpectedPriceBatch.** Reviewed 2026-08-23; Product Pricing API documentation updated in August 2026 with release notes through April 1, 2026.

Use: Amazon exposes seller/ASIN offer and competitive-pricing information separately from catalog/listing identity. `getListingOffers` returns lowest-priced offers for a seller SKU; `getCompetitiveSummary` exposes featured buying options / lowest offers; Featured Offer Expected Price is location/market sensitive and Featured Offer placement is not guaranteed because competing offers and fulfillment/customer-location factors can change.

Verification locators (2026-09-09): [FOEP operation](https://developer-docs.amazon/sp-api/reference/getfeaturedofferexpectedpricebatch) and [FOEP tutorial](https://developer-docs.amazon/sp-api/docs/return-batch-foep-data-set-skus), especially `resultStatus`. A missing estimate requires its reason, not automatic repricing.

Boundary: API output and FOEP are pricing/offer-system evidence, not proof of a complete organic-search or Featured Offer algorithm. The tutorial scopes its use case to new-condition nationwide offers; operation availability and location-segment support are separate questions.

## [A03] Amazon — 2026 title and Item Highlights update

Amazon Seller Central / News_Amazon. **Updates to improve your product titles begin on July 27.** Published/updated June 10, 2026; effective July 27, 2026.

Use: current seller-facing evidence that, except for media categories, product titles are limited to 75 characters including spaces from July 27, 2026. Amazon introduced Item Highlights with up to 125 characters for materials, recommended use cases, or comparison-relevant details; Item Highlights are described as searchable and visible with titles in search results and on product detail pages. Amazon also exposes AI-powered title / Item Highlights suggestions.

Verification locators (2026-09-09): [initial announcement](https://sellercentral-europe.amazon.com/seller-forums/discussions/t/cd6a14da-a5c7-4f62-b886-7ead97407b3c); [News_Amazon follow-up FAQ](https://sellercentral.amazon.com/seller-forums/discussions/t/302aaac6-6f2b-4d86-bcd2-36fe24f0e6cd). The latter qualifies migration, display, and field priority. Its opening official post is evidence; seller replies are not policy. The linked detailed title-help page was inaccessible in this review.

Boundary: the stated absence of priority between the two fields does not disclose numerical organic weights, prove every listing unaffected, or establish all category/marketplace exceptions.

## [A04] Amazon Seller Central — generic search terms / keywords

Amazon Seller Central staff / Help references. **Use search terms effectively; Generic Keyword field guidance.** Baseline review: 2026-08-23; public-source follow-up: 2026-09-09.

Use: public seller-facing guidance supports a Generic Keyword / search-terms field for matching; guidance recommends relevant synonyms/abbreviations/alternate names and discourages repetition, prohibited claims, brands/ASINs, and irrelevant terms. Current UI/policy details and byte/character limits can vary by marketplace/product type and should be re-checked before execution.

Verification locators (2026-09-09): [Ezra_Amazon, keyword guide, sections 2-4](https://sellercentral-europe.amazon.com/seller-forums/discussions/t/a15b6c4b-6541-4530-af4f-45bac3a68492); [Jessica_Amazon_, Search Terms tip](https://sellercentral.amazon.ca/seller-forums/discussions/t/0ae10d05-66d2-406b-b336-16791df2bce8). They support relevant, nonredundant vocabulary and identify a byte-based limit. An older [News_Amazon announcement](https://sellercentral.amazon.com/seller-forums/discussions/t/62e0e515a6e991d171d3ccee7be36304) supports the prohibited-term list but describes length in characters; this unit discrepancy is not resolved by silently treating bytes and characters as interchangeable. The linked detailed Help was inaccessible; do not infer a current universal cap or enforcement outcome from these older posts.

Boundary: generic keywords being indexed for matching does not establish a direct ranking boost, keyword-density rule, or priority over title/Item Highlights/attributes. Staff examples are not controlled evidence of sales effects.

## [A05] Amazon Science — retrieval and ranking architecture

Delgado, J., & Greyson, P. (2023). **From structured search to learning-to-rank-and-retrieve.** Amazon Science.

Direct source: [Amazon Science article](https://www.amazon.science/blog/from-structured-search-to-learning-to-rank-and-retrieve), March 7, 2023; inspected 2026-09-09.

Use: conceptual support for retrieval/ranking and combining candidate generators. The authors work in Amazon Music and use music/podcast examples.

Boundary: an architectural explanation/proposal, not evidence that Amazon Store deploys that specific retrieval policy or that every candidate must pass a separate reranker.

## [A06] Amazon Science — semantic product search

Muhamed, A., Srinivasan, S., Teo, C. H., Cui, Q., Zeng, B., Chilimbi, T., & Vishwanathan, S. V. N. (2023). **Web-scale semantic product search with large language models.** Amazon Science / publication.

Direct sources: [publication page](https://www.amazon.science/publications/web-scale-semantic-product-search-with-large-language-models) and [paper](https://cdn.amazon.science/cd/8e/d89d10a142ada7e5d60833e4e574/web-scale-semantic-product-search-with-large-language-models.pdf), sections 2.4 and 3.2 / Table 3; inspected 2026-09-09.

Use: dense semantic matching with offline and online evaluation. The online semantic-matcher replacement improves combined E+S@16 and S@16 while E@16 decreases; retain component metrics. Section 2.4 allows direct serving or mixing/reranking. The abstract alone obscures these qualifications.

Boundary: published 2023 system evidence does not disclose current 2026 production models, field weights, or every Amazon marketplace/search surface.

## [A07] Amazon Science — product retrieval and behavioral / product context

Two distinct research lines, inspected 2026-09-09:

- Chen et al. (2023), [season-aware semantic similarity](https://cdn.amazon.science/67/70/ae2e83e5488da38a205cabb14d2b/improving-product-search-with-season-aware-query-product-semantic-similarity.pdf), sections 2-4: season-conditioned modeling with price/review context, historical purchase-derived supervision, and offline ranking evaluation. Price Weighted Purchases is computed over model-ordered evaluation records, not a reported randomized seller-revenue effect.
- Han et al. (2023), [Search behavior prediction: A hypergraph perspective](https://cdn.amazon.science/99/03/03f8c5404bc8aa3d6ec9217948ff/search-behavior-prediction-a-hypergraph-perspective.pdf), sections 1, 2.1, and 4.1; explained by Huang in [Using hypergraphs to improve product retrieval](https://www.amazon.science/blog/using-hypergraphs-to-improve-product-retrieval): behavioral query-item links and session-derived hyperedges support link prediction. Evaluation uses three proprietary locale datasets and head/tail splits. This is distinct from real-time personalized next-item recommendation.

Use: scoped examples of contextual and behavioral inputs to research systems.

Boundary: sampled interactions can be noisy; co-session association does not establish compatibility or a typed complement relation. Research metrics do not identify universal Amazon Search factors or causal seller tactics.

## [A08] Amazon Shopping Queries / ESCI relevance framework

Amazon Science. **Shopping Queries Dataset / ESCI benchmark.** Released for KDD Cup 2022 and maintained as a product-search research asset.

Use: scientific/engineering evidence that query-product relevance can distinguish Exact, Substitute, Complement, and Irrelevant relationships; supports the principle that product relevance is semantic/relational and cannot be reduced to literal keyword presence.

Verification locators (2026-09-09): [dataset page](https://www.amazon.science/code-and-datasets/shopping-queries-dataset-a-large-scale-esci-benchmark-for-improving-product-search), [repository README](https://github.com/amazon-science/esci-data), and [paper](https://arxiv.org/pdf/2206.06588), introduction / sections 2.2 and 3. The label definitions distinguish functional alternatives from violations of central query requirements.

Boundary: sampled difficult queries and human judgments support a benchmark, not verified product truth, user authorization, a complete production-ranking objective, or a 2026 algorithm description. Classification, ranking, and substitute-identification are separate tasks.

## [A09] Amazon Shop Direct and Buy for Me — external-store discovery regime

Amazon. **Amazon is making it easier for merchants to sell from external stores.** Published 2026; reviewed 2026-08-23.

Direct source: `https://www.aboutamazon.com/news/retail/amazon-shop-direct-external-stores`

Use: Shop Direct lets Amazon customers discover products from stores across the web, including products not currently sold in Amazon's Store. Amazon says Shop Direct includes more than 100 million products from more than 400,000 merchants. External merchants can sync catalog, pricing, and inventory through feeds. Customers can either follow Shop Direct to the merchant website or, for eligible items, use Buy for Me so Amazon's agentic AI completes the purchase from the merchant website on the customer's behalf. Merchant store names remain visible; merchants manage delivery, returns, exchanges, and customer service.

Selected passages rechecked 2026-09-09: feed participation, customer flow, and U.S. availability. Preserve that customer-market scope; it does not prove availability or unavailability elsewhere.

Boundary: this establishes an external-store discovery / transaction regime alongside native Amazon Store commerce. It does **not** prove that every externally discovered product lacks every Amazon-internal identifier or disclose Shop Direct's full retrieval/ranking architecture.

## [A10] Amazon Alexa for Shopping — agentic shopping capabilities

Amazon. **Alexa for Shopping / agentic AI shopping assistant.** Current 2026 product documentation reviewed 2026-08-23.

Direct source: `https://www.aboutamazon.com/news/retail/alexa-for-shopping-ai-assistant`

Use: Amazon's current shopping assistant can discover products from Amazon and external stores, build carts, track prices, and in supported cases perform price-triggered auto-buy or Buy for Me actions. This is evidence that discovery, shopper intent, delegated/automated action state, and completed purchase can be distinct.

Selected passages rechecked 2026-09-09, together with the [Alexa usage guide](https://www.aboutamazon.com/news/retail/how-to-use-amazon-shopping-ai-assistant), Scheduled Actions and target-price sections. The documented U.S. experience separates notification/cart actions from configured auto-buy.

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

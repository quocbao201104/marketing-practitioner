# Etsy Commerce / Product-Discovery Evidence Ledger

Source identifiers for `../../platforms/commerce/etsy.md`.

Current product/search behavior is time-sensitive. Reviewed 2026-08-23.

## [E01] Etsy legal ranking disclosure

Etsy. **Search, Advertisement & Recommendation Ranking Disclosures.** Last updated October 16, 2025; reviewed 2026-08-23.

Use: current official disclosure that organic Search first performs query matching across listing titles, attributes, categories and tags, then ranks matched listings using listing/shop/buyer/context factors. It names relevance, engagement, recency, listing/shop quality, customer service, shipping, language/location, frequency capping and context-specific ranking among factors. It separately describes hundreds of recommendation modules with selection/retrieval followed by ranking, whose feature importance varies with shopper mission.

Boundary: this is a high-level legal/product disclosure, not a complete implementation diagram or fixed feature-weight formula.

## [E02] Etsy Seller Handbook — Keywords 101

Etsy Staff. **Keywords 101: Everything You Need to Know.** August 26, 2025; reviewed 2026-08-23.

Use: current seller guidance on title, description, tags, categories and attributes; specific categories/attributes can act like tags for matching; title position does not affect listing ranking; titles should be short, clear and buyer-readable; tags provide additional matching phrases; descriptions can contain relevant natural phrases. Etsy describes Search as considering listing information holistically.

Boundary: seller guidance about “search considers” fields does not by itself identify which stage every field enters; use E01/E04 for stage-specific evidence.

## [E03] Etsy Seller Handbook — 2026 title guidance / AI title tools

Etsy Staff. **New Guidance for Listing Titles, and a Tool to Help.** April 27, 2026; **How Etsy Uses AI to Support Sellers.** Current 2026 Seller Handbook.

Use: updated title guidance prioritizes buyer-friendly clarity; Etsy's optional title-suggestion tool can review existing title, tags, attributes, description, first photo and reviews to suggest clearer titles. Etsy explicitly says seeing a suggestion does not mean the current title is underperforming in Search.

Boundary: title-suggestion inputs are not a disclosed organic ranking-weight list.

## [E04] Etsy Engineering — semantic relevance after retrieval

Zhang, Y., Su, C., & Liu, S. (2026-01-16). **How Etsy Uses LLMs to Improve Search Relevance.** Etsy Engineering / Code as Craft.

Use: production engineering evidence for a human-grounded LLM relevance framework and real-time student model. Current disclosed integration points are post-retrieval filtering, relevance-score feature enrichment for downstream ranking, ranking-loss weighting, and relevance boosting near final results. The model consumes rich listing information including titles, images, descriptions, attributes, variations and extracted entities. Etsy explicitly says upstream retrieval relevance is a future direction. Engagement proxies (click/add-to-cart/purchase) can be biased and can move differently from semantic relevance.

Boundary: strong for the disclosed 2026 system; not a complete timeless Search stack or seller-controlled field formula.

## [E05] Etsy Engineering — vast inventory / LLM-derived attributes

Setty, V., & Bendit-Shtull, N. (2025-10-13). **Understanding Etsy's Vast Inventory with LLMs.** Etsy Engineering.

Use: Etsy describes 100M+ highly diverse, often unique inventory with no simple global-SKU/attribute mapping; seller title/description/images can be transformed by LLM pipelines into inferred structured attributes. LLM-derived attributes have been used in buyer/seller experiences including Search filters and color swatches, with measured engagement/conversion changes in targeted categories.

Boundary: platform-inferred attribute ≠ verified product truth; experiment results do not mean manually adding arbitrary attributes reproduces the causal effect.

## [E06] Etsy Engineering — internal product summaries / representations

Geitner, P., & Weissman, D. (2026-05-26). **Shaping Product Understanding with Contrastive Reinforcement Learning.** Etsy Engineering.

Use: raw listing data includes title, images, descriptions, tags, variations and attributes; Etsy trains multimodal LLMs to generate internal natural-language product summaries emphasizing distinguishing details for downstream Search/Recommendation models. Training uses query + engaged/non-engaged listing contrast.

Important freshness boundary: the May 2026 article says online production experiments integrating these summaries are planned / near-term, not that the summaries are already universally deployed across production search/recommendation.

## [E07] Etsy Help — personalization, variations, and custom listings

Etsy Help. **How to Offer Personalized Listings.** Current help reviewed 2026-08-23.

Use: personalization/custom options let buyers provide made-to-order details; variations are fixed choices that can affect inventory, price or SKU; custom listings can be private, one-buyer listings created for one-of-a-kind commissioned items. Strong evidence that `listing` need not merely describe a pre-existing canonical product object.

Boundary: feature availability/UI can change; object-role conclusion remains scoped to Etsy commerce.

## [E08] Etsy Seller Handbook — Search / recommendation seller guidance

Etsy Staff. **How Etsy Search Works; Ultimate Guide to Etsy Search; Add Attributes to Help Increase Your Shop's Visibility.** Current 2025–2026 handbook reviewed 2026-08-23.

Use: seller-facing descriptions of query matching/ranking, attributes/categories/tags and current shop/listing quality guidance.

Boundary: handbook advice is official practical guidance but less implementation-specific than E01/E04. When wording conflicts, prefer the more precisely scoped legal/engineering source and retain the distinction rather than forcing false consistency.

## Evidence-use rules

```text
ETSY LISTING
≠ ALWAYS A RECORD FOR A PRE-EXISTING CANONICAL PRODUCT

PERSONALIZATION
≠ VARIATION
≠ PRIVATE CUSTOM LISTING

TITLE POSITION
≠ RANKING BOOST

FIELD HELPS / IS CONSIDERED IN SEARCH
≠ FIELD PARTICIPATES IN INITIAL RETRIEVAL

QUERY MATCHING
≠ POST-RETRIEVAL SEMANTIC RELEVANCE
≠ DOWNSTREAM RANKING

ENGAGEMENT
≠ SEMANTIC RELEVANCE

PLATFORM-INFERRED ATTRIBUTE
≠ VERIFIED PRODUCT TRUTH

INTERNAL PRODUCT SUMMARY
≠ USER-FACING LISTING COPY

PLANNED PRODUCTION EXPERIMENT
≠ UNIVERSALLY DEPLOYED PRODUCTION FEATURE

ONE RECOMMENDATION MODULE
≠ ETSY-WIDE RANKING LAW
```

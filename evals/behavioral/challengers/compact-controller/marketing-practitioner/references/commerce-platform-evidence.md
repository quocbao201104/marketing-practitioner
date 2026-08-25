# Commerce and Product-Discovery Evidence Ledger

This supplementary ledger defines the source identifiers used by `../handbook/09-commerce-environments-and-product-discovery.md` and, later, by commerce-specific platform modules.

The ledger mixes three evidence classes deliberately:

```text
CONCEPTUAL PARENT
established architecture / ontology vocabulary used only to avoid inventing terms

CURRENT PLATFORM FACT
current product documentation, help, policy, or API behavior; time-sensitive and scoped

ENGINEERING / SCIENTIFIC DISCLOSURE
published implementation, system, or experimental evidence; stronger for the disclosed system than for a timeless production contract
```

A current platform or engineering source supports only the system, market, period, and proposition it actually documents. Do not translate an exposed field, model feature, ranking factor, or experiment result directly into a universal seller tactic.

---

## Conceptual parents

### [C01] Hepp — GoodRelations product, model, offering, and commercial-state distinctions

Hepp, M. (2008). **GoodRelations: An Ontology for Describing Products and Services Offers on the Web.** EKAW 2008.

Use: conceptual parent for distinguishing an individual product/service instance, a product/service model, a class of goods, an offering, and commercial properties such as price. Supports the principle that the thing being offered and the commercial conditions under which it is offered need not be the same analytical object.

Boundary: GoodRelations is an ontology for Web data exchange, not a marketing funnel, marketplace ranking model, or claim that every platform materializes the same object boundaries.

### [C02] Schema.org / Google Search Central — product groups, variants, products, and offers

Schema.org. **ProductGroup; ProductModel; SomeProducts; isVariantOf; Offer.** Current schema documentation. Google Search Central. **Product Variant Structured Data (`ProductGroup`, `Product`).** Reviewed 2026-08-23.

Use: current technical vocabulary showing that product families/groups, variants/products, and offers can be represented with explicit relations such as `hasVariant` / `isVariantOf`; Google documents `ProductGroup` plus variant `Product` markup and nested `Offer` data.

Boundary: schema vocabulary and Search structured-data eligibility do not establish one universal commerce ontology, Google Shopping ranking weights, or a writing tactic.

---

## Google commerce / product data

### [C03] Google Merchant API — ProductInput, processing, merging, and processed Product

Google. **Merchant API ProductInputsService; Products Service; Make frequent updates to your products; Merchant Products API release notes.** Reviewed 2026-08-23; current documentation updated through August 2026.

Use: current evidence that `ProductInput` is submitted input data, while rules, supplemental sources, automatic improvements, merging, and validation can produce a processed `Product` resource later retrieved from Merchant Center. Current product documentation also exposes time- and eligibility-sensitive commercial fields such as availability, loyalty/member pricing, minimum-order conditions, and automated discounts.

Supports:

```text
SOURCE INPUT
≠ PLATFORM-PROCESSED PRODUCT RECORD
```

and demonstrates that a seller field can be transformed, overridden, supplemented, or combined before the platform-held product state is produced.

Boundary: the Merchant API processing model does not disclose all Search/Shopping retrieval, ranking, recommendation, or display logic.

---

## Amazon commerce / catalog

### [C04] Amazon Selling Partner API — catalog items, seller listings, and offers

Amazon. **Manage Product Listings with the Selling Partner API; Catalog Items API v2022-04-01; Listings Items API; Product Pricing / getListingOffers.** Reviewed 2026-08-23.

Use: current evidence that Amazon separately exposes catalog items/ASINs, selling-partner listings/SKUs, and offer/pricing operations. The listing lifecycle explicitly asks whether the item already exists in Amazon's catalog and separately manages seller listings.

Boundary: API object boundaries are implementation evidence, not proof that `catalog item`, `listing`, or `offer` must become peer-level durable primitives in the practitioner core. Amazon-specific identity and Featured Offer behavior must remain in the Amazon module.

---

## TikTok Shop hybrid content / commerce

### [C05] TikTok Shop Academy — content-product linking and relinking

TikTok Shop. **How to Link Products to Videos** (2026-06-10); **How to Relink Products** (2025-12-01); related current shoppable-video guidance. Reviewed 2026-08-23.

Use: current product evidence that a TikTok video can exist independently, later receive a product/shop/category/collection link, and in supported cases retain the same content while an unavailable product link is replaced. Supports:

```text
CONTENT OBJECT
≠ COMMERCE TARGET
≠ CONTENT↔COMMERCE EDGE
```

and shows that a visible product anchor/link can be treated as a representation of a consequential relation rather than as the product itself.

Boundary: applies to TikTok Shop features and documented eligibility windows/markets; it does not establish For You ranking behavior or general commerce-platform architecture by itself.

---

## Shopee search / discovery / buyer-relative commercial state

### [C06] Jiang et al. — MRSE multimodal retrieval at Shopee

Jiang, H., Zhang, H., Hou, Q., Chen, C., Lin, W., Zhang, J., & Wang, A. (2024). **MRSE: An Efficient Multi-modality Retrieval System for Large Scale E-commerce.** arXiv:2408.14968.

Use: Shopee implementation-backed evidence that a large-scale e-commerce retrieval system can combine query text, item text/images, and user multimodal preference/history to build retrieval representations. Supports:

```text
TEXT QUERY
≠ TEXT-ONLY RETRIEVAL

QUERY MODALITY
≠ ALL MODEL EVIDENCE USED FOR RETRIEVAL
```

Boundary: the published system and experiments do not establish every current Shopee search stage, feature weight, ranking objective, or seller tactic in 2026.

### [C07] Liu et al. — multimodal item embeddings for Shopee Image Search

Liu, C., Hou, P., Zeng, A., & Yu, H. (2024). **Transformer-empowered Multi-modal Item Embedding for Enhanced Image Search in E-Commerce.** AAAI 2024; preprint arXiv:2311.17954.

Use: implementation evidence that Shopee Image Search can construct item representations from multiple product images plus textual information, rather than reducing image-query retrieval to image-only item evidence.

Boundary: evidence is scoped to the disclosed Image Search system and deployment period.

### [C08] Shopee Vietnam Help — search modes, filters/sorts, and buyer-relative displayed price

Shopee Vietnam. **Cách Tìm Kiếm Sản Phẩm Cần Mua Trên Shopee; Về cách thức hiển thị giá trên Sàn TMĐT Shopee.** Reviewed 2026-08-23.

Use: current buyer-facing evidence that Shopee supports keyword and image search; users can sort/filter results by criteria such as category, location, shipping, price, newest, best-selling, rating, and other options; and displayed prices can incorporate estimated vouchers available to the individual buyer and can show the lowest price among variants.

Supports:

```text
DEFAULT PLATFORM RANKING
≠ USER-SELECTED SORT
≠ USER-APPLIED FILTER
```

and:

```text
BASE / VARIANT COMMERCIAL STATE
≠ BUYER-RELATIVE DISPLAYED PRICE
≠ GUARANTEED FINAL CHECKOUT PRICE
```

Boundary: filter availability or displayed buyer state does not establish hidden organic ranking weights.

---

## Etsy inventory, search, and machine product understanding

### [C09] Etsy official search disclosures — query-matching abstraction conflict

Etsy. **Search, Advertisement & Recommendation Ranking Disclosures.** Last updated October 16, 2025. Etsy Staff. **Keywords 101: Everything You Need to Know.** August 26, 2025. Etsy Staff. **How Etsy Search Works.** Current Seller Handbook. Reviewed 2026-08-23.

Use: current official Etsy sources agree that organic Search separates query matching from later ranking, but they do **not** expose one consistent field-level description of query matching. The legal disclosure describes first-phase matching across titles, attributes, categories, and tags. `Keywords 101` explicitly says keywords across titles, descriptions, tags, categories, and attributes are essential to query matching and calls query matching the first phase. `How Etsy Search Works` places a holistic listing — including title, tags, attributes, descriptions, first photo, reviews, and more — under its Query matching section.

Supports:

```text
CURRENT OFFICIAL ETSY SOURCES
DISAGREE / USE DIFFERENT ABSTRACTION LEVELS
ABOUT QUERY-MATCHING FIELD PARTICIPATION

→ preserve source + date + abstraction level
→ exact production field-to-stage boundary remains UNKNOWN
```

Boundary: none of these public sources is a complete implementation trace or fixed feature-weight formula. Do not silently prefer the narrower legal enumeration as a complete field map, and do not turn the broader Seller Handbook wording into precise implementation or ranking weights.

### [C10] Etsy Engineering — semantic relevance in the production search stack

Zhang, Y., Su, C., & Liu, S. (2026-01-16). **How Etsy Uses LLMs to Improve Search Relevance.** Etsy Engineering / Code as Craft.

Use: engineering evidence that Etsy distinguishes retrieved candidates from **this disclosed post-retrieval semantic-relevance layer**, feature enrichment, downstream ranking, and relevance boosting; semantic models consume rich listing information including title, images, description, attributes, variations, and extracted entities. Also documents that engagement proxies such as clicks/add-to-carts/purchases can be biased and can diverge from semantic relevance.

Supports:

```text
SEARCH INFLUENCE
≠ ONE SETTLED FIELD-TO-STAGE MAP
≠ SEMANTIC RELEVANCE CONTRIBUTION
≠ RANKING CONTRIBUTION
≠ FINAL RESULT COMPOSITION
```

Boundary: this is strong evidence for the disclosed semantic-relevance system at the publication period, not a timeless complete Etsy Search contract. Its statement that the semantic-relevance model first applies after retrieval does **not** establish that description or other rich listing data are absent from every separate initial query-matching/retrieval mechanism.

### [C11] Etsy Engineering — machine-derived product understanding

Setty, V. (2025-10-13). **Understanding Etsy’s Vast Inventory with LLMs.** Etsy Engineering / Code as Craft. Geitner, P., & Weissman, D. (2026-05-26). **Shaping Product Understanding with Contrastive Reinforcement Learning.** Etsy Engineering / Code as Craft.

Use: engineering evidence that Etsy's diverse inventory often lacks global SKU mappings; structured product information may be extracted from unstructured seller text/images; and internal machine-generated product summaries/representations can be created for search and recommendation use.

Supports:

```text
PRODUCT FACT / SUBJECT MATTER
≠ SELLER-DECLARED STRUCTURED FIELD
≠ UNSTRUCTURED SELLER EXPRESSION
≠ PLATFORM-INFERRED / MACHINE-DERIVED REPRESENTATION
```

Boundary: an inferred attribute or summary remains platform-derived evidence with provenance; it does not become ground-truth product fact merely because a model generated it.

---

## Lazada catalog / attributes / machine-derived product knowledge

### [C12] Lazada Open Platform — item/SKU structure, variant attributes, pricing, and auto-fill

Lazada. **Open Platform Create Product; GetCategoryAttributes; product creation / item and SKU responses.** Documentation currently available through Lazada Open Platform and reviewed 2026-08-23.

Use: integration evidence that Lazada separately exposes item and SKU identifiers, seller-customized SKU values, item-level and SKU-level attributes, sale/variant properties, price/special-price validity, inventory-related fields, and an optional algorithmic attribute auto-fill mechanism.

Supports:

```text
PLATFORM ITEM IDENTITY
≠ SELLER-LOCAL SKU IDENTITY

ITEM-LEVEL ATTRIBUTE
≠ SKU / VARIANT-LEVEL ATTRIBUTE

SELLER INPUT
≠ POSSIBLE PLATFORM-AUTOFILLED ATTRIBUTE STATE
```

Boundary: Open Platform docs describe integration objects and seller-data requirements; documentation freshness varies by endpoint, and a documented `product score` or field flag does not by itself establish organic search ranking weight.

### [C13] Hongwimol et al. — AutoPKG at Lazada

Hongwimol, P., Shang, H., Wang, C., Wan, Z., Gao, Y., Li, Y., Gui, L., Sun, W., & Yu, C. (2026). **AutoPKG: An Automated Framework for Dynamic E-commerce Product-Attribute Knowledge Graph Construction.** arXiv:2604.16950.

Use: Lazada/Alibaba engineering evidence that multimodal listing content can be used to induce product types and attribute keys, extract values, canonicalize them into a product-attribute knowledge graph, and feed production applications including Search and Recommendation. Online experiments in the paper show measured business effects for the tested system.

Boundary: the experiment supports the tested AutoPKG-derived attribute system, not a general claim that filling any seller field directly increases organic rank, nor exact current ranking weights.

---

## AI-native / conversational product discovery

### [C14] Google Merchant Center — conversational product data and AI shopping queries

Google Merchant Center Help. **How to use conversational attributes; About AI performance insights; Product detail `[product_detail]`; Product highlight `[product_highlight]`.** Reviewed 2026-08-23.

Use: current official evidence that AI/conversational shopping can involve longer, more complex requests and product-feature, specification, review, pricing/comparison, and other mixed intents. Google exposes conversational attributes and structured technical/detail fields for AI-driven product understanding, and its AI performance insights can surface frequently used product concepts and missing popular structured attributes. Google explicitly tells merchants not to use `product_highlight` as a keyword/search-term/SEO-keyword list.

Supports:

```text
MACHINE / AGENT LEGIBILITY
≠ KEYWORD DENSITY

SHOPPER LANGUAGE
≠ ONE EXACT KEYWORD STRING

STRUCTURED FACT COMPLETENESS
CAN IMPROVE PRODUCT UNDERSTANDING / MATCHABILITY
≠ GUARANTEED RETRIEVAL OR RANKING
```

Boundary: AI performance insights are a limited/phased product feature, and Google does not disclose exact field-to-stage mappings, retrieval/ranking weights, or a deterministic seller formula for AI Mode/Gemini.

### [C15] Shopee / Sea — Shopee App in ChatGPT

Shopee Vietnam Help. **[ChatGPT] Shopee trên ChatGPT là gì và cách liên kết tài khoản.** Sea Limited. **Sea and OpenAI Deepen Strategic Partnership to Drive AI Adoption and Innovation Across Southeast Asia and Brazil.** Reviewed 2026-08-23.

Use: current official evidence that shoppers in supported markets can use natural conversational requests in ChatGPT to receive Shopee product recommendations/cards. Shopee account connection is optional; connected users may receive more personalized suggestions based on Shopee history/preferences, while recent conversational context/needs can be shared to support the request. Product detail and checkout continue on Shopee app/web in the documented flow.

Supports:

```text
CONVERSATIONAL REQUEST / CONTEXT
≠ ONE MANUAL KEYWORD QUERY

SAME PRODUCT DATA
+ DIFFERENT SHOPPER / ACCOUNT / CONVERSATION STATE
→ POSSIBLY DIFFERENT RECOMMENDATION CONTEXT
```

Boundary: current official sources do not disclose the exact Shopee listing fields, candidate-generation/retrieval pipeline, transformation logic, ranker features/weights, or a seller-facing optimization formula for the Shopee App in ChatGPT.

---

## Evidence-use rules

Use these sources according to their strongest legitimate role:

```text
CONCEPTUAL PARENT
→ vocabulary / distinction only

PLATFORM API OR HELP
→ current object boundaries, user-visible behavior, eligibility, field semantics

ENGINEERING DISCLOSURE
→ disclosed system architecture / experiments

LOCAL ACCOUNT EVIDENCE
→ actual current account only when sufficiently comparable
```

Keep these boundaries explicit:

```text
API OBJECT NAME
≠ DURABLE ANALYTICAL PRIMITIVE

SEARCH FIELD
≠ GUARANTEED RETRIEVAL FEATURE
≠ RANKING WEIGHT

MACHINE LEGIBILITY / PRODUCT-DATA COMPLETENESS
≠ KEYWORD DENSITY
≠ GUARANTEED RANKING / RECOMMENDATION

SEMANTIC MATCHABILITY
≠ PROVEN RANKING BOOST

CONVERSATIONAL SHOPPER REQUEST
≠ ONE EXACT KEYWORD STRING

OPTIMIZE FOR RESOLVABILITY
≠ OPTIMIZE FOR IMAGINED MODEL WEIGHTS

OFFICIAL SOURCES WITH DIFFERENT FIELD/STAGE ABSTRACTIONS
→ PRESERVE CONFLICT / SCOPE
→ DO NOT FORCE FALSE CONSISTENCY

PAID / SPONSORED RANKING FACTOR
≠ ORGANIC RANKING FACTOR

PLATFORM-INFERRED ATTRIBUTE
≠ VERIFIED PRODUCT TRUTH

CURRENT DOCUMENTATION
≠ TIMELESS PLATFORM REGIME
```

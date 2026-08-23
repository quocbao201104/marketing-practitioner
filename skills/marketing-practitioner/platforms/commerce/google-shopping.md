# Google Shopping / Commerce — Product Discovery Module

Last reviewed: 2026-08-23

Use this module when Google-specific product data, Merchant Center / Merchant API processing, free listings, Shopping surfaces, product-rich Search results, Images / Lens, YouTube commerce surfaces, conversational shopping, agentic checkout, or related Google product-discovery behavior can materially change the decision.

Current operational claims should be re-checked when consequential. Google changes Merchant data requirements, product surfaces, AI shopping experiences, structured-data support, checkout eligibility, and eligibility rules over time [G01–G11].

This module instantiates the commerce specialization in `../../handbook/09-commerce-environments-and-product-discovery.md`. It does not define a Google-specific ontology.

---

## 1. Google commerce is a family of systems, not one shopping algorithm

Do not reduce Google commerce to a single Shopping-tab ranker or to title-keyword matching.

Relevant systems can include, when material:

- Merchant Center / Merchant API ingestion and product processing;
- Google Search product and merchant-listing experiences;
- the Shopping tab and other shopping-result surfaces;
- Google Images commerce experiences;
- Google Lens visual product discovery;
- YouTube product / shopping surfaces where available;
- AI Mode and Gemini shopping experiences;
- conversational product attributes and agent-facing product data;
- UCP-powered checkout for eligible participating merchants/surfaces;
- free-listing systems;
- sponsored / Shopping Ads systems;
- structured-data / rich-result eligibility systems;
- policy, diagnostics, automatic improvements, and data-quality systems.

Google documents product information appearing across Search, Shopping, Images, Lens, YouTube, and AI-driven experiences [G06][G07]. These surfaces can share underlying Shopping Graph / merchant product information while using different mediation systems, representations, and objectives.

Therefore:

```text
GOOGLE PRODUCT DATA
≠ ONE SURFACE
≠ ONE RANKER
≠ ONE FIELD-WEIGHT LAW
```

Before applying a Google claim, preserve:

```text
system / surface
organic / free / sponsored mode
merchant / structured-data source
product / variant scope
market / account regime
time
```

---

## 2. Product input, processed product, and customer-facing representation are different

### 2.1 Merchant input is not the final platform-held product state

Google Merchant API distinguishes submitted `ProductInput` resources from processed `Product` resources. Rules, supplemental sources, automatic improvements, merging, validation, and other processing can contribute to the resulting platform-held product record [G01].

Use:

```text
MERCHANT / DATA-SOURCE INPUT
        ↓
rules / supplemental sources /
automatic improvements / validation / merging
        ↓
PROCESSED GOOGLE PRODUCT RECORD
        ↓
ELIGIBLE SYSTEMS / SURFACES
        ↓
USER-FACING REPRESENTATION
```

Do not collapse:

```text
SELLER SUBMITTED FIELD
= GOOGLE PROCESSED VALUE
= WHAT THE SHOPPER WILL SEE
```

into one state.

### 2.2 Product-processing diagnosis comes before copy diagnosis when the record itself changed

If a Merchant Center representation or product outcome changes unexpectedly, first ask whether any of these changed:

- primary data source;
- supplemental source;
- rules or feed transformations;
- automatic improvements;
- product approval / disapproval state;
- product identifier or item-group mapping;
- price / availability / shipping state;
- structured-data consistency;
- market or destination settings.

Do not rewrite a title merely because the rendered or processed product differs from the submitted source.

---

## 3. Identity: product group, variant, merchant record, and external identifiers

### 3.1 Merchant ID is not universal product identity

Google Merchant product data can include several identifiers with different jobs [G02]:

```text
[id]
merchant-controlled item identity within the merchant/data-source regime

[item_group_id]
merchant-declared grouping relationship for variants

GTIN
standardized trade-item identity when valid and applicable

brand
brand identity / manufacturer information

MPN
manufacturer part number when applicable
```

Do not treat any one of these as a universal `PRODUCT` primitive.

Preserve scope:

```text
MERCHANT RECORD IDENTITY
≠ AUTOMATICALLY GLOBAL PRODUCT IDENTITY
```

and when valid standardized identifiers exist:

```text
STANDARD IDENTIFIER
CAN SUPPORT IDENTITY / RECONCILIATION
BUT
≠ GUARANTEED ORGANIC RANK BOOST
```

### 3.2 Product group and variant are relational

Google Search structured-data documentation explicitly supports `ProductGroup` with variant `Product` objects using `hasVariant` / `isVariantOf` and variant-defining properties [G05]. Merchant Center separately supports `item_group_id` and variant attributes [G02].

Use:

```text
PRODUCT GROUP / FAMILY
       │
       │ hasVariant
       ▼
SELLABLE VARIANT
```

Then attach only the variant-defining state that matters, such as:

```text
color
size
material
pattern
age group / gender where applicable
other supported variant dimensions
```

Do not create a new product object merely because copy differs; do not collapse distinct sellable variants merely because their shared group title is similar.

### 3.3 Group identity and selected-variant identity can have different representation jobs

A group-level name may communicate shared family identity while variant-specific information disambiguates the currently selectable item.

Therefore:

```text
SHARED PRODUCT-FAMILY IDENTITY
≠ VARIANT-DISAMBIGUATING INFORMATION
```

When Google exposes group/variant fields separately, allocate information according to those roles rather than repeating every variant token in every field.

---

## 4. Product-descriptive data, commercial state, and observational context

### 4.1 Product-descriptive data

Google-supported product information can include [G02–G04][G09][G11]:

```text
title / structured title
brand
GTIN / MPN
category / product type
product detail
product highlights
description
variant attributes
primary / additional images
question-and-answer
document links
merchant-declared related-product relations
item-group title / variant options
other supported product attributes
```

These fields are not interchangeable keyword containers.

### 4.2 Commercial state

Commercial conditions can include:

```text
price
sale / discount state
availability
shipping
minimum-order conditions
loyalty / member pricing where supported
automated-discount state where supported
market / destination eligibility
```

These describe the current conditions under which the item can be acquired, not timeless product identity [G01][G03].

### 4.3 Observational / social context

Ratings, reviews, seller feedback, popularity, or related aggregate signals can appear in some Google commerce experiences, but they are not intrinsic product attributes merely because they are visible near the product.

Preserve the Chapter 09 distinction:

```text
PRODUCT-DESCRIPTIVE FACT
≠ COMMERCIAL CONDITION
≠ OBSERVATION / FEEDBACK AGGREGATE
```

Google's `popularity_rank` requires one extra distinction: it is merchant-declared product data about relative selling performance inside that merchant's inventory, not Google's own Search rank [G09].

---

## 5. Field roles: allocate information by job

Do not reason from generic “Google Shopping SEO” lists. Ask what human or machine job each supported field performs in the relevant system.

### 5.1 Title / structured title

Current Merchant Center documentation treats title as a prominent product representation used in ads/free listings and requires it to identify the product accurately [G03].

Operational job:

```text
HUMAN IDENTIFICATION
what is this product?

SALIENT DIFFERENTIATION
which important model / variant / use-defining detail matters?

PLATFORM PRODUCT INFORMATION
one source used by Google systems to understand / match the item
```

Do not infer:

```text
IMPORTANT WORD FIRST
→ ORGANIC RANK BOOST
```

merely because early information improves human scanning or because the title is used by product systems.

Avoid promotional stuffing, irrelevant repeated keywords, unsupported urgency, or text that contradicts the actual product.

### 5.2 Product group title / variant option

When supported, group-level and variant-selection information should help separate:

```text
WHAT IS SHARED ACROSS THE FAMILY?

WHAT DISTINGUISHES THIS SELECTABLE VARIANT?
```

Do not use the group field as a dumping ground for every possible variation token.

### 5.3 GTIN / brand / MPN

Primary job:

```text
IDENTITY RESOLUTION / RECONCILIATION
```

Use valid identifiers when the product legitimately has them. Do not fabricate or substitute identifiers to chase visibility.

Do not turn Google's recommendation to provide valid identifiers into the claim:

```text
ADD IDENTIFIER
→ DIRECT RANKING BOOST OF KNOWN SIZE
```

The exact downstream use and weight vary by system and are not fully disclosed.

### 5.4 Product detail

Use structured `product_detail` fields for factual technical or specification information when supported [G03][G11]. Google says these structured details can improve its ability to show individual products for queries, including AI-driven surfaces [G11].

Typical job:

```text
STRUCTURED TECHNICAL / VERIFIABLE DETAIL
→ machine-readable product understanding
→ potentially human comparison / display where surfaced
```

Examples can include dimensions, materials, capacity, compatibility identifiers, or other supported technical values when they are true and belong in the current category/schema.

Do not duplicate vague marketing adjectives where a precise value is available, and do not fabricate a specification to broaden matching.

### 5.5 Product highlights

Use product highlights for concise prioritized features or benefits where supported [G03][G11].

Typical job:

```text
PRIORITIZED HUMAN-READABLE FEATURE / BENEFIT SUMMARY
```

Google explicitly says `product_highlight` should not be used as a list of keywords/search terms or SEO keywords [G11].

Keep claims evidence-compatible. A highlight is not a substitute for a missing structured specification when machine filtering or identity depends on the structured field.

### 5.6 Description

Use description for richer explanation, use context, material facts, limitations, compatibility, and details that do not fit the title/highlights.

Do not assume repeating title keywords in the description creates a known ranking gain.

### 5.7 Primary and additional images

The primary image is required product data and is a major human-facing product representation in Google commerce experiences [G04]. Additional images can communicate other views or details.

Possible jobs:

```text
VISUAL IDENTIFICATION
what product is this?

HUMAN SELECTION
is it worth inspecting?

HUMAN EVALUATION
what does it look like / include / differ from alternatives?

MACHINE VISUAL EVIDENCE
possible input in visual-discovery or other machine systems where documented
```

Do not infer that because Google Lens can perform visual product discovery, every image characteristic has a known organic ranking weight.

### 5.8 Conversational attributes are agent-facing product data, not one SEO field family

Google currently exposes optional conversational attributes intended to help AI systems and conversational agents understand product nuances [G09]:

```text
question_and_answer
document_link
related_product
item_group_title
variant_option
popularity_rank
```

These complement the primary Merchant Center product-data specification rather than replacing it.

Possible jobs differ:

```text
question_and_answer
→ merchant-supplied product Q&A / factual clarification

document_link
→ authoritative supporting document reference

related_product
→ merchant-declared typed product relation

item_group_title / variant_option
→ family / variant semantics

popularity_rank
→ merchant-declared relative selling-performance context
```

Do **not** collapse them into one “AI SEO” tactic.

#### 5.8.1 Popularity rank is not Google organic rank

Google defines `popularity_rank` as a merchant-supplied number indicating how well a product sells compared with other products that merchant sells [G09].

Keep:

```text
MERCHANT-DECLARED POPULARITY_RANK
≠ GOOGLE SEARCH / SHOPPING ORGANIC RANK
```

Do not interpret a value such as `95.5` as “Google ranks this product at 95.5.”

#### 5.8.2 Related product is a declared relation, not inferred behavior

Google lets merchants declare relations such as accessory, spare part, often-bought-with, or substitute [G09].

Keep:

```text
MERCHANT-DECLARED RELATED_PRODUCT
≠ PLATFORM-INFERRED SUBSTITUTE / COMPLEMENT
≠ OBSERVED CO-PURCHASE RELATION
```

The same pair of products can participate in more than one relation with different provenance.

#### 5.8.3 Field availability does not disclose search-stage weight

Do not generalize:

```text
CONVERSATIONAL FIELD EXISTS
→ INITIAL RETRIEVAL FEATURE
→ FIXED RANKING WEIGHT
```

without direct Google evidence for that stage and surface.

### 5.9 Resolve conversational requirements through the right factual carrier

Google's current AI performance insights reflect a shopper environment where requests can be longer and more complex than keyword-style searches and can combine product features, technical specifications, reviews, price/comparison intent, and other constraints [G11].

The seller-side goal is not to predict the hidden query decomposition. It is to make the true answer to material shopper constraints available in the appropriate Google-supported product data.

Use a map such as:

```text
SHOPPER REQUIREMENT
→ TRUE PRODUCT FACT / RELATION / COMMERCIAL STATE
→ GOOGLE-SUPPORTED CARRIER
```

Examples, only when supported and truthful:

```text
identity / use-defining product wording
→ title / description

exact measurable specification
→ product_detail / structured attribute

variant requirement
→ item-group / variant fields

detailed question / compatibility / limitation
→ question_and_answer / document / description as appropriate

accessory / spare-part / substitute relation
→ related_product

visible physical property
→ accurate image + corresponding structured/text fact when supported

budget / availability constraint
→ current price / availability / commercial data
```

Google's AI performance insights can show product terms and popular structured attributes that appear in conversational shopping behavior, but treat them as **evidence of shopper information demand / product-data opportunity**, not a disclosed rank weight [G11].

Therefore:

```text
MACHINE / AGENT LEGIBILITY
≠ KEYWORD DENSITY
≠ GUARANTEED AI VISIBILITY
```

and:

```text
SEMANTIC / CONVERSATIONAL MATCHABILITY
≠ PROVEN RANKING BOOST
```

Do not create a compatibility, use case, feature, dimension, material, or benefit merely because shoppers ask for it. Missing truthful evidence should remain missing/unknown until verified.

---

## 6. Discovery is multimodal and multi-surface

### 6.1 Search / Shopping

A shopper can discover merchant products through query-driven Search and Shopping experiences [G06][G08].

Preserve the distinction between:

```text
QUERY / DISCOVERY CONTEXT
PRODUCT DATA
CANDIDATE / RESULT SELECTION
FINAL PRODUCT REPRESENTATION
```

Google's high-level Shopping disclosure says results can depend on relevance, search terms, and other Google activity, with personalization possible [G08].

This does **not** disclose the exact candidate generation, feature weights, ranker, reranking, or composition for every surface.

### 6.2 Google Images and Lens

Google documents product information appearing in Images and Lens, including visually similar purchasable products and product-rich experiences [G06].

Therefore:

```text
TEXT QUERY
≠ ONLY GOOGLE COMMERCE DISCOVERY PATH
```

and visual discovery can depend on machine representations not visible to the seller.

Do not infer:

```text
IMAGE SEARCH EXISTS
→ TITLE DOES NOT MATTER
```

or the reverse.

Different systems can combine visual, textual, structured, behavioral, and product-graph evidence.

### 6.3 YouTube commerce surfaces

Google product information can surface in YouTube commerce contexts where available [G06].

Treat YouTube product exposure as its own encounter / delivery context rather than assuming a Shopping-tab ranking rule transfers directly.

For a creator/product task, Chapter 08 may additionally matter because a content object, creator actor, product target, and commerce edge can coexist.

### 6.4 AI Mode / Gemini conversational shopping

Google currently describes Shopping Graph-backed product discovery inside AI Mode and Gemini, including conversational refinement and query fan-out-like behavior in AI shopping experiences [G07]. Merchant Center's AI performance insights additionally describe longer/more complex shopping queries spanning feature, specification, review, pricing/comparison and other intents [G11].

Use:

```text
CONVERSATIONAL REQUEST / SHOPPER STATE
→ possibly multiple constraints / derived searches / product-understanding steps
→ shopping candidates / representations
```

Do not reduce this to one user-entered keyword string.

A shopper may ask for several requirements at once, for example:

```text
use case
compatibility
hard constraint
preference
size / material / technical spec
budget
trade-off
specific variant
```

The durable practitioner response is to ensure the product's **true** answers to those requirements are represented in the appropriate carriers, not to manufacture every likely phrase in the title.

Exact current query decomposition, retrieval sources, ranking weights, product-card composition, and generated-answer behavior remain partially undisclosed and time-sensitive.

### 6.5 UCP-powered checkout adds a transaction layer without changing product identity

For eligible participating merchants in supported markets/surfaces, Google now documents UCP-powered checkout on AI Mode in Search and Gemini [G10].

Use separate roles:

```text
GOOGLE AI MODE / GEMINI
= discovery / conversational / checkout mediation surface

MERCHANT
= seller of record

GOOGLE PAY
= payment-flow role where used

MERCHANT BACKEND
= current product / checkout / order responsibility under the integration
```

Therefore:

```text
CHECKOUT HAPPENS INSIDE GOOGLE EXPERIENCE
≠ GOOGLE BECOMES SELLER OF RECORD
```

and:

```text
DISCOVERY PRODUCT REPRESENTATION
≠ CURRENT AUTHORIZED CHECKOUT STATE
```

when price, availability, shipping, tax, selected variant, or other transaction conditions have changed.

Google says its agentic checkout acts at the customer's direction and UCP exchanges data between the AI agent and merchant backend [G10]. Treat shopper intent, user authorization, platform capability, merchant acceptance, payment, and fulfillment as separate states when they matter.

Availability is phased; do not assume every merchant, market, product, AI Mode result, or Gemini user has the same checkout capability.

---

## 7. Retrieval / ranking evidence boundary

### 7.1 High-level Shopping factors are not a complete algorithm

Google Shopping Help states that shopping results can be ranked using relevance, search terms, and other Google activity; personalization may apply. Some recommendation surfaces can consider factors such as relevance, ratings, price, and product features [G08].

Use these as **current product-level disclosures**, not a deterministic seller formula.

Keep:

```text
DISCLOSED FACTOR CATEGORY
≠ COMPLETE FEATURE SET
≠ FIXED WEIGHT
≠ UNIVERSAL SURFACE RULE
≠ DIRECT WRITING TACTIC
```

### 7.2 Merchant field requirements are not ranking factors

A field can be:

- required for acceptance;
- required for a destination;
- recommended for data quality;
- used for identity resolution;
- displayed to shoppers;
- used for matching or another machine function;

without being a disclosed organic ranking weight.

Therefore:

```text
REQUIRED / RECOMMENDED FIELD
≠ RANKING FACTOR OF KNOWN WEIGHT
```

### 7.3 Structured-data eligibility is not realized rich-result exposure

Google Search structured data can make a page eligible for product / merchant experiences [G05].

Keep:

```text
VALID STRUCTURED DATA
≠ GUARANTEED RICH RESULT
≠ GUARANTEED SHOPPING EXPOSURE
≠ HIGH RANK
```

Likewise:

```text
COMPLETE / RICH MERCHANT PRODUCT DATA
≠ GUARANTEED AI MODE / GEMINI RETRIEVAL OR RECOMMENDATION
```

### 7.4 Sponsored systems stay separate

Shopping Ads / sponsored commerce systems can use bidding, campaign, advertiser, and commercial signals unavailable to free organic systems.

Do not transfer:

```text
ADS OPTIMIZATION RULE
→ FREE LISTING / ORGANIC SEARCH RULE
```

without direct evidence.

---

## 8. Customer-facing representations vary by surface

The same processed product data can support different representations:

```text
Search product result
Shopping result/card
merchant listing
Images product snippet
Lens result
YouTube product representation
AI Mode / Gemini product card or generated shopping response
UCP-powered checkout representation where eligible
```

Therefore:

```text
SUBMITTED TITLE
≠ PROCESSED PRODUCT TITLE
≠ RENDERED TITLE IN EVERY SURFACE
```

and:

```text
PRODUCT OBJECT / RECORD
≠ PRODUCT CARD
≠ ENCOUNTER SURFACE
```

When a decision concerns click-through or comprehension, inspect the actual representation and surface rather than assuming the source feed field is encountered unchanged.

---

## 9. Shopper state and product-information allocation

### Discovery / orientation

Need:

```text
clear product identity
salient differentiator
recognizable image
relevant price context where shown
```

Do not overload the selection representation with every specification.

### Comparison / evaluation

Need can shift toward:

```text
variant distinction
technical details
compatibility
materials / dimensions
proof / ratings where surfaced
shipping / return / seller context
commercial trade-offs
```

### Transaction readiness

Need can shift toward:

```text
selected variant
current price
availability
shipping / arrival context
merchant / seller
final commercial conditions
current authorization / checkout state when mediated by an agent
```

Allocate source data and copy according to the current representation job instead of one universal “optimized listing” format.

---

## 10. Diagnosing weak Google commerce performance

Do not jump from lower clicks/orders to title rewriting.

Check only what can change the conclusion:

```text
1. METRIC / SURFACE
Search, Shopping, Images, Lens, YouTube, AI experience,
ads, free listings, Merchant reporting?

2. PRODUCT PROCESSING
Same ProductInput, data source, rules, automatic improvements,
approval state, processed Product?

3. IDENTITY / VARIANT
Same merchant ID, item group, GTIN/brand/MPN, variant mapping?

4. COMMERCIAL STATE
Same price, availability, shipping, promotion, market eligibility?

5. HUMAN REPRESENTATION
Same rendered title, image, card, rich result, product details?

6. DISCOVERY CONTEXT
Same query mix, conversational constraints, visual vs text entry,
device, personalization, Shopping/AI/Lens regime?

7. PRODUCT RESOLVABILITY
Can current product data truthfully answer the material use-case,
compatibility, spec, dimension, variant, budget, or trade-off constraint?
Did a structured/text/image fact change?

8. AGENTIC / CHECKOUT STATE IF RELEVANT
Same UCP eligibility, merchant participation, user authorization,
checkout state, seller-of-record/payment/fulfillment roles?

9. ORGANIC / SPONSORED MIX
Same exposure provenance?

10. TIME / DOCUMENTATION / PLATFORM REGIME
Any recent product-data, eligibility, surface, or AI-shopping change?

11. COMPETING EXPLANATIONS
What else changed?

12. DISCRIMINATING CHECK
Which current report / processed record / surface / checkout observation
best separates the leading explanations?
```

Use Chapter 05 if causal attribution becomes material.

---

## 11. Fast path for Google product communication

For a narrow task with supplied facts, do not reconstruct the whole Google commerce graph.

Examples:

```text
"Rewrite this Merchant Center title"
→ identify product/variant
→ preserve supported facts
→ make identity + salient differentiation clear
→ obey current title requirements
→ write

"Turn these specs into product highlights"
→ preserve verified specs
→ prioritize human evaluation value
→ do not turn highlights into keyword/search-term lists
→ write

"Improve primary-image brief"
→ resolve selection/evaluation job
→ obey current image requirements
→ avoid inventing Lens-ranking theory
→ brief
```

Only load identity, processing, retrieval, conversational-attribute, agentic-checkout, or cross-surface reasoning when those distinctions can change the decision.

---

## 12. Google-specific anti-folklore guardrails

Keep these boundaries:

```text
TITLE USED BY GOOGLE PRODUCT SYSTEMS
≠ TITLE KEYWORD POSITION HAS KNOWN ORGANIC BOOST
```

```text
VALID GTIN / BRAND / MPN HELPS IDENTITY QUALITY
≠ IDENTIFIER CREATES A KNOWN DIRECT RANKING LIFT
```

```text
PRODUCT DETAIL / HIGHLIGHT FIELD EXISTS
≠ FIELD HAS DISCLOSED FIXED RETRIEVAL OR RANKING WEIGHT
```

```text
CONVERSATIONAL ATTRIBUTE AVAILABLE
≠ INITIAL RETRIEVAL / RANKING WEIGHT DISCLOSED
```

```text
MACHINE LEGIBILITY / FACT COMPLETENESS
≠ KEYWORD DENSITY
≠ GUARANTEED AI VISIBILITY
```

```text
SEMANTIC / CONVERSATIONAL MATCHABILITY
≠ PROVEN ORGANIC RANKING BOOST
```

```text
AI SHOPPING TERM / POPULAR ATTRIBUTE
≠ INSTRUCTION TO INVENT THE ATTRIBUTE OR REPEAT THE TERM
```

```text
MERCHANT-DECLARED POPULARITY_RANK
≠ GOOGLE ORGANIC SEARCH RANK
```

```text
MERCHANT-DECLARED RELATED_PRODUCT
≠ PLATFORM-INFERRED RELATION
≠ OBSERVED CO-PURCHASE RELATION
```

```text
GOOGLE LENS USES VISUAL DISCOVERY
≠ IMAGE-ONLY RETRIEVAL
≠ EVERY IMAGE FEATURE HAS KNOWN RANKING VALUE
```

```text
AI MODE / GEMINI USE SHOPPING GRAPH DATA
≠ MERCHANT CAN OBSERVE OR CONTROL EVERY INTERNAL QUERY / RANKING STEP
```

```text
UCP-POWERED GOOGLE CHECKOUT SURFACE
≠ GOOGLE IS SELLER OF RECORD
≠ USER INTENT ALONE AUTHORIZES EVERY TRANSACTION EFFECT
```

```text
SHOPPING HELP LISTS FACTOR CATEGORIES
≠ COMPLETE ORGANIC ALGORITHM
```

```text
STRUCTURED-DATA ELIGIBILITY / COMPLETE PRODUCT DATA
≠ GUARANTEED EXPOSURE / RECOMMENDATION
```

```text
SPONSORED RESULT
≠ ORGANIC / FREE LISTING
```

---

## 13. Explicit UNKNOWNs

Unless fresher system-specific evidence establishes otherwise, preserve these as unknown or only partially disclosed:

- exact candidate-generation architecture for current Google Shopping / free-listing surfaces;
- exact organic field weights;
- exact weighting of title, description, attributes, GTIN, images, ratings, price, shipping, conversational attributes, or other data by surface;
- whether one machine/agent representation is shared across Search, Shopping, Images, Lens, YouTube, AI Mode, and Gemini;
- exact AI Mode / Gemini query decomposition/fan-out, candidate retrieval, semantic matching, ranking, reranking, and product-card composition;
- exact use of each conversational attribute across traditional Search vs AI surfaces;
- whether/how an AI performance-insight term maps to a production feature or stage beyond the documented insight itself;
- exact relation between Merchant processed product state and every rendered representation;
- complete reranking / diversity / merchant / policy / commercial constraints in each commerce surface;
- exact UCP rollout/eligibility across merchants, markets, products, and users;
- exact authorization/re-authorization behavior when checkout state changes outside documented protocol requirements;
- exact causal effect of changing one field on impressions, clicks, conversion, or GMV without a valid experiment.

Do not fill these gaps with practitioner folklore.

---

## 14. Final Google commerce check

Before consequential Google product work is finalized, ask only the relevant questions:

1. Which Google system/surface is actually in scope?
2. Is the source value being confused with the processed Product or rendered representation?
3. Are merchant record, product group, variant, and standardized identifiers scoped correctly?
4. Are product-descriptive fields separated from price/availability/shipping commercial state?
5. Is each field being allocated according to its documented human/machine/agent job rather than generic keyword folklore?
6. Can material shopper constraints — use, compatibility, dimensions/specs, preference, variant, budget, trade-off — be resolved from truthful product data in the appropriate carriers?
7. Is an AI-shopping term/attribute insight being used to identify a factual product-data gap rather than to invent a claim or simulate a hidden weight?
8. Is `popularity_rank` being mistaken for Google organic Search rank?
9. Is a merchant-declared `related_product` relation being confused with a platform-inferred or behavioral relation?
10. Is the primary image being treated as both human representation and possible machine evidence without inventing visual-ranking weights?
11. Are Search/Shopping, Images/Lens, YouTube, AI Mode/Gemini, ads, and structured-data eligibility kept distinct where material?
12. If UCP checkout is in scope, are shopper intent, authorization, checkout state, seller of record, payment, and fulfillment roles separated?
13. Is a high-level Shopping disclosure being over-read as a complete algorithm?
14. Are required/recommended fields being mistaken for ranking weights?
15. Are structured-data eligibility / data completeness and realized exposure separated?
16. Is sponsored exposure kept separate from free/organic exposure?
17. Are current product-data rules, conversational attributes, AI performance insights, checkout rollout, and surface behavior fresh enough for the decision?
18. Are undisclosed internals left UNKNOWN?
19. Is the fast path still being respected when the task is only a narrow product communication artifact?

The goal is not to reverse-engineer Google Shopping or agentic checkout. The goal is to make truthful product constraints resolvable to the relevant human/machine system while preserving the distinctions that materially change product data, representation, discoverability, commercial authority, transaction interpretation, or learning.

---

## Evidence

See `../../references/commerce/google-shopping-evidence.md` for `[G01–G11]` source definitions and evidence boundaries.

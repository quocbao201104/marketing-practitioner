# Amazon — Commerce / Product Discovery Module

Last reviewed: 2026-08-23

Use this module when Amazon-specific catalog identity, seller listings, product-detail-page composition, offers / Featured Offer, product-search data, title / Item Highlights / generic search terms, product search, recommendation, or seller performance interpretation can materially change the decision.

Current operational claims should be re-checked when consequential. Amazon changes listing requirements, search fields, Product Detail Page behavior, Featured Offer systems, APIs, and seller tools over time [A01–A08].

This module instantiates the commerce specialization in `../../handbook/09-commerce-environments-and-product-discovery.md`. It does not define an Amazon-specific ontology.

---

## 1. Amazon commerce is a shared catalog plus seller-specific commercial state

Do not reason about Amazon as though every seller owns an isolated product page.

A useful current implementation map is:

```text
AMAZON CATALOG
ASIN / catalog item
      │
      ├── product attributes / relationships / classification
      │
      └── seller listings can attach to catalog identity
                │
                ▼
        SELLER LISTING / SKU
                │
                ├── seller-specific attributes where applicable
                ├── inventory / fulfillment
                └── offer / price / condition
                         │
                         ▼
                 COMPETITIVE OFFER STATE
                    Featured Offer etc.
                         │
                         ▼
                 CUSTOMER REPRESENTATION
             search result / PDP / offer selector
```

Amazon SP-API explicitly separates catalog querying by ASIN from selling-partner listings by seller SKU and from pricing/offer APIs [A01][A02].

Therefore:

```text
ASIN / CATALOG ITEM
≠ SELLER SKU / LISTING
≠ SELLER OFFER / COMMERCIAL STATE
```

when those independently relevant roles exist.

Do not generalize this Amazon architecture to marketplaces where the platform listing itself is the commercially decisive product object.

---

## 2. Catalog item, seller listing, SKU, and offer identity

### 2.1 ASIN is Amazon catalog identity, not a universal physical-product ontology

An ASIN identifies an Amazon catalog item. Amazon catalog items can play roles such as base products, variation parents, variation children, bundles, or other catalog classifications depending on product type and catalog structure.

Use:

```text
ASIN
= AMAZON CATALOG IDENTITY
```

not:

```text
ASIN
= THE UNIVERSAL PRODUCT ENTITY
```

The same manufacturer/domain product can participate in other external identifiers and catalog structures; conversely, not every ASIN maps neatly to one individually buyable physical item.

### 2.2 Seller SKU identifies a seller listing in marketplace scope

Listings Items API operations are keyed by seller ID + SKU and marketplace context [A01]. Product Pricing can also query offers by SellerSKU [A02].

Therefore:

```text
SELLER SKU
= SELLER-SCOPED LISTING IDENTITY
```

and not:

```text
SELLER SKU = ASIN
```

Preserve marketplace and seller scope when reconciling data.

### 2.3 Variation parent and child roles are relational

Amazon catalog relationships can organize a family under a variation parent with children representing selectable configurations.

A practical encoding remains:

```text
PARENT / FAMILY CATALOG ITEM
     │
     │ hasVariant / variation relationship
     ▼
CHILD / SELECTABLE CATALOG ITEM
```

Do not make `VARIATION_PARENT` or `VARIATION_CHILD` new durable primitives. They are Amazon-local object roles and relations.

### 2.4 Parent used for organization ≠ child selected for purchase

In many product families, a parent catalog item organizes the family while a child ASIN is the purchasable configuration.

Keep:

```text
ENTITY USED TO ORGANIZE FAMILY
≠ ENTITY SELECTED FOR PURCHASE
```

when the product type behaves this way.

Do not assume all Amazon categories implement variations identically.

---

## 3. Seller listing ≠ Amazon-selected PDP content

A seller listing is a seller's contribution / listing state, not a guarantee that every submitted value will become the customer-visible Product Detail Page.

Amazon's shared catalog can receive data from multiple sources. Platform rules can reconcile or select catalog content independently of one seller's listing contribution.

Use:

```text
SELLER LISTING / CONTRIBUTION
        ↓
AMAZON CATALOG / DATA SELECTION
        ↓
CUSTOMER-FACING PDP / SEARCH REPRESENTATION
```

Therefore:

```text
SELLER SUBMISSION
≠ AMAZON CATALOG STATE
≠ DISPLAYED PDP CONTENT
```

If a seller's source field and live PDP differ, diagnose contribution/catalog selection state before assuming a copy-save failure or ranking issue.

---

## 4. Product Detail Page is a composite representation

A typical Amazon PDP can compose information from several independently meaningful roles:

```text
catalog product identity
variation family / selected child
Amazon-selected product data
seller / offer state
Featured Offer / buying option
other seller offers
price / shipping / delivery
inventory / fulfillment
reviews / ratings
images / media
product details
policies / badges / platform state
```

Therefore:

```text
PDP
≠ SELLER LISTING OBJECT
≠ ONE OFFER
≠ ONE SOURCE RECORD
```

Treat the PDP as a platform-composed human-facing representation of multiple catalog, commercial, observational, and platform states.

---

## 5. Offer and Featured Offer reasoning

### 5.1 Product identity ≠ seller offer

Multiple sellers can offer the same Amazon catalog item under different conditions.

Represent:

```text
SELLER
  --[offers]-->
CATALOG ITEM / BUYABLE CONFIGURATION

commercial state:
price
condition
shipping
fulfillment
availability
customer / location scope
time
```

Amazon Product Pricing APIs expose offers separately from catalog/listing identity [A02].

### 5.2 Featured Offer is platform-mediated selection state

Featured Offer placement is not a fixed property of an ASIN or seller. Amazon's API documentation describes Featured Offer Expected Price and explicitly warns that Featured Offer placement is not guaranteed; competition, fulfillment capabilities, and customer/location context can change which offer is featured [A02].

Use:

```text
SELLER OFFER
+ COMPETITIVE COMMERCIAL STATE
+ CUSTOMER / LOCATION CONTEXT
+ PLATFORM SELECTION
→ POSSIBLE FEATURED OFFER STATE
```

Therefore:

```text
LOWER PRICE
≠ GUARANTEED FEATURED OFFER
```

and:

```text
FEATURED OFFER AT t0
≠ PERMANENT FEATURED OFFER
```

### 5.3 Featured Offer ≠ product-search organic ranking

Do not transfer a pricing / buying-option factor into Amazon Search ranking without evidence.

```text
FEATURED OFFER SYSTEM
≠ PRODUCT SEARCH RANKING SYSTEM
```

The same product can participate in both systems, but the objectives and state are not identical.

---

## 6. Product-information allocation after the July 2026 title change

Amazon changed title / visible-search representation rules beginning July 27, 2026 [A03]. For all categories except media, titles are now limited to 75 characters including spaces, while Item Highlights adds up to 125 characters for materials, recommended use cases, or comparison-relevant details. Amazon describes both as searchable and visible in search results and PDPs [A03].

This makes field allocation especially important.

### 6.1 Title

Current job:

```text
CORE PRODUCT IDENTIFICATION
+ highest-value distinguishing detail that fits naturally
```

Because the title must be compact and fully readable on mobile, do not force every attribute or synonym into it.

Keep:

```text
TITLE IS SEARCHABLE
≠ TITLE SHOULD CONTAIN EVERY QUERY VARIANT
```

and:

```text
TITLE IS PROMINENT
≠ TITLE HAS DISCLOSED PRIORITY OVER ITEM HIGHLIGHTS
```

Amazon explicitly said title and Item Highlights are both searchable, without stating that one is prioritized for search [A03].

### 6.2 Item Highlights

Current documented job:

```text
ADDITIONAL COMPARISON-RELEVANT PRODUCT INFORMATION
materials / recommended use cases / useful differentiators
```

Item Highlights can carry information that would previously have made titles long or difficult to scan [A03].

Use them for truthful, decision-relevant distinctions rather than another keyword list.

### 6.3 Generic Keywords / Search Terms

Amazon currently maintains a Generic Keyword / search-terms field used for matching; seller guidance recommends relevant synonyms, abbreviations, and alternate names while avoiding repetition and prohibited / irrelevant terms [A04].

This field is a strong example of:

```text
MACHINE-CONSUMED SEARCH DATA
≠ USER-FACING PRODUCT COPY
```

Use it for relevant vocabulary that genuinely helps matching and is supported by the current product type / marketplace policy.

Do not infer:

```text
MORE BACKEND KEYWORDS
→ HIGHER ORGANIC RANK
```

or repeat visible title / Item Highlights vocabulary merely to increase density.

### 6.4 Attributes / product-type data

Amazon Product Type Definitions and Listings Items schemas expose structured requirements by product type [A01].

Structured attributes can support:

```text
catalog classification
identity / variation structure
filtering / browse compatibility
machine product understanding
human product detail where surfaced
```

Do not use prose as a substitute for a required structured attribute, and do not assume every schema field is an organic ranking factor.

### 6.5 Images / media

Images serve human identification and evaluation and can also participate in Amazon machine systems where disclosed by product/search research.

Keep:

```text
IMAGE QUALITY / CONTENT
≠ KNOWN ORGANIC SEARCH WEIGHT
```

unless a current system-specific source establishes the mechanism.

---

## 7. Searchable product data ≠ customer-visible product data

After the 2026 change, Amazon gives an unusually explicit example:

```text
TITLE
searchable + visible

ITEM HIGHLIGHTS
searchable + visible

GENERIC KEYWORDS
used for matching + not ordinary customer-facing copy

STRUCTURED ATTRIBUTES
machine/catalog roles + sometimes visible depending on field/surface
```

Therefore:

```text
TITLE
≠ ALL SEARCHABLE PRODUCT DATA
```

and:

```text
SEARCHABLE
≠ CUSTOMER-FACING
```

This is why a product-information strategy should allocate facts by job rather than put all vocabulary into the title.

---

## 8. Amazon product search: retrieval ≠ ranking

Amazon Science publications provide implementation/scientific evidence for a common product-search architecture in which candidate matching/retrieval precedes ranking [A05][A06].

Use the conceptual distinction:

```text
QUERY / CONTEXT
      ↓
MATCHING / RETRIEVAL
      ↓
CANDIDATE PRODUCTS
      ↓
RANKING / ORDERING
      ↓
FINAL SEARCH REPRESENTATION
```

Do not assume this diagram is a complete or current 2026 production pipeline for every Amazon Store search surface.

### 8.1 Semantic matching ≠ literal keyword matching

Amazon product-search research uses dense semantic matching / language models to address lexical limitations and retrieve exact/substitute products [A06][A08].

Therefore:

```text
KEYWORD PRESENT
≠ QUERY RELEVANCE
```

and:

```text
QUERY TERM ABSENT VERBATIM
≠ PRODUCT CANNOT BE SEMANTICALLY RELEVANT
```

Do not use this to claim that keywords are irrelevant; it means literal token presence is not a complete relevance model.

### 8.2 Query-product relationship is typed

The Amazon Shopping Queries / ESCI work distinguishes:

```text
EXACT
SUBSTITUTE
COMPLEMENT
IRRELEVANT
```

relationships [A08].

This supports thinking about relevance as a relation between shopper intent/query and product, not a scalar “SEO score” intrinsic to the listing.

### 8.3 Behavioral / contextual features are system evidence, not seller rules

Amazon product-search research has explored clicks, purchases, query-product graphs, price, review counts, seasonality, and other contextual features [A07].

Keep:

```text
FEATURE USED IN A PUBLISHED MODEL / EXPERIMENT
≠ CURRENT UNIVERSAL AMAZON SEARCH FACTOR
≠ DIRECT SELLER TACTIC
```

### 8.4 Exact current production internals remain UNKNOWN

Unless current Amazon product documentation or implementation evidence establishes otherwise, preserve as unknown:

- exact current retrieval model(s);
- exact query parsing / semantic-expansion behavior;
- exact product-field features and weights;
- exact ranker objectives and weightings;
- reranking / diversity / availability / seller / policy constraints;
- how Sponsored placements are composed with organic results;
- whether all marketplaces use the same architecture.

---

## 9. Search representation, PDP representation, and offer representation have different jobs

### Search-result representation

Primary shopper job:

```text
identify product
judge rough relevance
compare visible alternatives
select candidate to inspect
```

### Product Detail Page

Primary shopper job:

```text
understand product / selected variant
assess proof and fit
compare commercial conditions
choose buying option
```

### Offer / buying-option representation

Primary shopper job:

```text
which seller / price / condition / fulfillment option
will satisfy the transaction?
```

Do not evaluate a title, Item Highlight, image, or offer using one universal conversion rule. The representation job changes by surface and shopper state.

---

## 10. Reviews / ratings are observations and encounter context

Reviews, ratings, review images, and aggregate counts originate as buyer feedback / observations. When displayed on the PDP or search result, they become part of another shopper's evaluation context.

They may also be consumed by Amazon machine systems in scoped research or production applications [A07].

Therefore:

```text
REVIEW / RATING
≠ INTRINSIC PRODUCT FACT
```

and:

```text
VISIBLE SOCIAL PROOF
≠ PROVEN CAUSAL PURCHASE EFFECT
```

without a valid design.

### Variation-level / family-level aggregation is platform-mediated

Amazon can change how reviews are shared or aggregated across product variations. Treat review scope as a platform state, not an inherent property of the product family.

When interpreting review evidence, ask:

```text
which ASIN / child / family?
which time / review-sharing regime?
which representation shows the aggregate?
```

---

## 11. Recommendation and related-product discovery

Amazon can recommend related, substitute, complementary, personalized, or context-specific products outside explicit text search.

Possible contexts include:

```text
current product
browsing history
cart
purchase history
category
homepage / recommendation module
post-purchase state
```

Therefore:

```text
DISCOVERY CONTEXT
≠ SEARCH QUERY ONLY
```

and:

```text
ONE RECOMMENDATION MODULE
≠ AMAZON-WIDE RANKING LAW
```

Do not apply Amazon Search title/search-term tactics mechanically to recommendation systems.

---

## 12. Diagnosing weak or changing Amazon performance

Do not jump from lower sales or search rank to rewriting visible copy.

Check only material dimensions:

```text
1. METRIC / SURFACE
Search impressions? clicks? PDP sessions? add-to-cart? units ordered?
Featured Offer? ad traffic? recommendation traffic?

2. CATALOG IDENTITY
Same ASIN / parent-child relation / product type / browse classification?

3. SELLER LISTING
Same SKU, contribution state, listing issues, suppressed attributes?

4. COMMERCIAL OFFER
Same price, condition, inventory, fulfillment, shipping,
Featured Offer state, location/customer context?

5. CUSTOMER REPRESENTATION
Same title, Item Highlights, images, selected catalog values,
review display, variation presentation?

6. SEARCHABLE DATA
Same generic keywords, structured attributes, product type data?

7. TRAFFIC / DISCOVERY MIX
Same query, organic/sponsored mix, recommendation/referral source?

8. TIME / PLATFORM REGIME
Did title rules, Item Highlights, catalog policy, review aggregation,
or marketplace behavior change?

9. COMPETING EXPLANATIONS
What else changed at the same time?

10. DISCRIMINATING CHECK
Which catalog/listing/offer/search report or controlled test
best separates the leading explanations?
```

Use Chapter 05 when causal attribution or experiment design becomes material.

---

## 13. Fast path for Amazon listing communication

### Rewrite a title

Given supported facts:

```text
identify the exact product / child variant
→ keep within current category title requirement
→ communicate core product identity clearly
→ move secondary comparison details into Item Highlights / attributes where appropriate
→ do not stuff synonyms
→ draft
```

### Write Item Highlights

```text
resolve the most useful comparison details
→ preserve facts / claims
→ prioritize material / use case / differentiating information
→ do not merely duplicate title
→ draft within current requirement
```

### Improve generic keywords

```text
identify relevant alternate vocabulary not already represented adequately
→ use current Amazon guidance
→ avoid prohibited / irrelevant terms and unnecessary repetition
→ do not claim ranking lift
```

No search-model reconstruction is needed unless the task actually concerns discoverability mechanisms or diagnosis.

---

## 14. Amazon-specific anti-folklore guardrails

```text
ASIN
≠ SELLER SKU
≠ OFFER
```

```text
SAME ASIN
≠ SAME COMMERCIAL STATE ACROSS SELLERS
```

```text
FEATURED OFFER
≠ LOWEST PRICE ALONE
≠ PERMANENT SELLER PROPERTY
```

```text
TITLE SEARCHABLE
≠ TITLE SHOULD CONTAIN EVERY KEYWORD
```

```text
ITEM HIGHLIGHTS SEARCHABLE
≠ ITEM HIGHLIGHTS HAVE KNOWN EQUAL / LOWER / HIGHER WEIGHT VS TITLE
```

```text
GENERIC KEYWORDS USED FOR MATCHING
≠ BACKEND KEYWORD DENSITY IMPROVES RANK
```

```text
STRUCTURED ATTRIBUTE REQUIRED
≠ ORGANIC SEARCH WEIGHT
```

```text
AMAZON SCIENCE PAPER
≠ CURRENT COMPLETE AMAZON STORE ALGORITHM
```

```text
BEHAVIOR FEATURE IN RESEARCH
≠ SELLER SHOULD MANUFACTURE THAT BEHAVIOR
```

```text
SEARCH RELEVANCE
≠ PURCHASE LIKELIHOOD
```

```text
PDP CONTENT
≠ ONE SELLER'S SUBMISSION
```

---

## 15. Explicit UNKNOWNs

Preserve these unless current authoritative evidence establishes them for the exact marketplace/system:

- exact organic Amazon Search retrieval and ranking pipeline in 2026;
- exact relative search contribution of title, Item Highlights, generic keywords, attributes, images, reviews, price, sales, fulfillment, and other signals;
- exact weighting or interaction of semantic and lexical matching;
- exact current recommendation-module objectives;
- exact catalog-contribution selection process for all attributes;
- exact Featured Offer selection formula and all customer/location/fulfillment factors;
- exact review aggregation / variation-sharing behavior outside currently documented cases;
- exact composition rules for organic and sponsored product results;
- causal effect of changing any one listing field on organic impressions, ranking, conversion, or sales without a valid experiment.

Do not fill these gaps with third-party “A9/A10 algorithm” folklore.

---

## 16. Final Amazon commerce check

1. Is the ASIN/catalog item being confused with the seller SKU/listing or offer?
2. Is a variation parent being confused with the purchasable child?
3. Is seller-submitted data being treated as guaranteed PDP content?
4. Are product identity and seller-specific price/stock/fulfillment state separated?
5. Is Featured Offer state being treated as dynamic and customer/location/competition scoped?
6. Are title, Item Highlights, generic keywords, and structured attributes allocated by current documented jobs rather than one keyword container?
7. Is the July 27, 2026 title/Item Highlights regime being applied for the relevant category/marketplace?
8. Is searchability being confused with known ranking priority?
9. Are retrieval, semantic relevance, and ranking separated conceptually?
10. Is Amazon Science evidence scoped to the published system/time rather than asserted as the 2026 production contract?
11. Are search, recommendations, PDP composition, Featured Offer, and ads treated as different systems where material?
12. Are reviews treated as observations / encounter context rather than intrinsic product truth?
13. Are organic, sponsored, recommendation, and offer-system metrics kept separate?
14. Are undisclosed internals left UNKNOWN?
15. Is the fast path still respected for a narrow listing-copy task?

The goal is not to reverse-engineer Amazon Search or the Featured Offer. The goal is to preserve Amazon's catalog/listing/offer distinctions, allocate product information to the right current fields, and reason about discovery and commercial outcomes without inventing algorithm laws.

---

## Evidence

See `../../references/commerce/amazon-evidence.md` for `[A01–A08]` source definitions and evidence boundaries.

# 09 — Commerce Environments and Product Discovery

## 1. Scope and central thesis

Commerce work on a platform is not merely a product-title or listing-copy task. A product, service, item, or sellable configuration is represented through merchant data, platform records, images, text, structured attributes, prices, inventory, delivery promises, reviews, and other states; then discovered through search, recommendation, browse, social content, visual search, conversational systems, or other mediated environments; then evaluated by a shopper whose intent and commercial eligibility can change the representation and outcome.

This chapter specializes the durable platform-environment model in `08-content-environments-and-distribution.md` for commerce and product discovery.

It does **not** define a second ontology.

Use the same durable parent roles:

```text
ACTOR / SOURCE
OBJECT
REPRESENTATION
AUDIENCE STATE
TYPED RELATIONSHIP / DELIVERY / PERMISSION EDGE
INTERACTION ACT
PLATFORM / MEDIATION STATE
OBSERVATION RECORD

+ provenance
+ scope / relativity
+ history / state transition
```

For commerce, use narrow local names when they improve clarity:

```text
OBJECT
→ product family / model / item / variant / listing / shop / promotion /
  collection / other independently identified commerce object when material

REPRESENTATION
→ product card / PDP / image / title / attribute rendering /
  machine product representation / commercial presentation

AUDIENCE STATE
→ shopper / buyer state

TYPED EDGE
→ seller-product commercial relation / hasVariant / belongsTo /
  content-product link / delivery / permission relation

INTERACTION ACT
→ search / click / select / cart / order / purchase / return / review
```

These are analytical roles, not disjoint universal entity classes. The same domain entity can occupy different roles in different questions. A shop can be an acting seller and also a recommendation target; an account can be an actor and an object of discovery. Preserve `ACTOR / SOURCE` when authority, action, or accountability matters, and `OBJECT` when independently persistent identity as a target/subject matters. Do not collapse the roles merely because one real-world entity can occupy both.

The central thesis is:

> Commerce discovery is a graph of identities, commercial relations, representations, platform mediation, shopper states, and observations — not a linear `product → listing → ranking → purchase` pipeline.

A second operational principle follows:

> Allocate each fact, claim, attribute, image, and commercial condition according to the human or machine job it must perform on the specific platform, rather than copying generic “SEO fields” or ranking folklore across systems.

The current cross-platform evidence base includes conceptual parents from GoodRelations and Schema.org, current platform documentation from Google, Amazon, TikTok Shop, Shopee, Etsy, and Lazada, engineering disclosures from Shopee, Etsy, and Lazada, conversational-discovery evidence from Google and Shopee, and agentic-commerce / product-discovery evidence from UCP, ACP, OpenAI, and Shopify [C01–C15][AC01–AC07]. These sources do not establish one universal marketplace implementation or fixed ranking law.

---

# Part I — The commerce specialization of the compact core

## 2. Commerce environments are graphs, not listing pipelines

A useful commerce map can be sketched as:

```text
                         ACTORS
              seller / brand / creator / platform
                    \       |       /
                     \      |      /
                      typed relations
                           |
                           v
                        OBJECTS
        product family / item / variant / listing / shop
                           |
                attributes / commercial state
                           |
                           v
                     REPRESENTATIONS
          seller input / platform record / machine encoding
              product card / PDP / anchor / checkout
                           |
                           v
                    PLATFORM MEDIATION
       eligibility / retrieval / relevance / ranking / filtering /
        sorting / recommendation / composition / governance
                           |
                           v
                     SHOPPER STATE
       discover / orient / compare / evaluate / configure / buy
                           |
                           v
                    INTERACTION ACTS
       search / click / select / cart / purchase / return / review
                           |
                           v
                    OBSERVATION RECORDS
```

Do not read this as a mandatory sequence. A shopper can enter at a product page from an external link, encounter a product through creator content, revisit an item from history, discover an alternative through a recommendation module, or move backward from cart to comparison.

Likewise, platform processing is not necessarily one pipeline. A field can be used by validation, policy, retrieval, recommendation, display, pricing, fulfillment, or measurement systems independently.

Therefore:

```text
COMMERCE ENVIRONMENT
≠ ONE SEARCH ALGORITHM
≠ ONE LISTING OBJECT
≠ ONE FUNNEL
```

---

## 3. Product identity and platform-record identity

### 3.1 Ask what identity actually matters

Do not begin with the word `product` as though it names one universal object level.

Depending on the market and platform, decision-relevant identities can include:

```text
PRODUCT FAMILY / GROUP
shared identity across variations

PRODUCT MODEL / BASE SPECIFICATION
shared specification that can describe many instances

SELLABLE CONFIGURATION / VARIANT
specific selectable combination such as size + color

INDIVIDUAL ITEM
one identified physical or digital instance

FUTURE / MADE-TO-ORDER ITEM
an item instantiated or completed after configuration or purchase

SELLER LISTING / POSTING
seller-controlled commercial/catalog object

PLATFORM CATALOG ITEM
platform-held catalog identity
```

GoodRelations explicitly distinguishes individual instances, product/service models, classes of goods, offerings, and commercial properties [C01]. Schema.org and Google similarly expose product groups, variant relations, products, and offers as distinct structures [C02].

These are useful conceptual parents, not a mandate to materialize every role in every task.

### 3.2 Do not assume domain identity equals platform-record identity

A platform record can refer to, organize, describe, sell, or instantiate a domain item — but the relationship is platform-specific.

Amazon separately exposes catalog items/ASINs and seller listings/SKUs [C04]. Google distinguishes merchant `ProductInput` records from processed `Product` resources [C03]. Etsy demonstrates the opposite danger of over-separation: its marketplace contains many unique, handmade, personalized, configurable, and made-to-order goods where a listing may itself be the commercially decisive object rather than merely a detachable record for a pre-existing canonical product [C11].

Therefore do **not** impose either assumption universally:

```text
PLATFORM RECORD = DOMAIN PRODUCT
```

or:

```text
PLATFORM RECORD MUST BE A DIFFERENT OBJECT FROM DOMAIN PRODUCT
```

Instead ask:

> Are there two independently relevant identities here, or would separating them invent a distinction that does not change the decision?

### 3.3 ID is scoped identity evidence, not the thing itself

A platform can expose several identifiers for related but non-identical roles:

```text
manufacturer / industry identifier
platform catalog identifier
seller-local SKU
platform-local SKU
country / marketplace item identifier
variant identifier
listing identifier
```

Amazon separates catalog items/ASINs from selling-partner listings/SKUs [C04]. Lazada exposes item IDs, SKU IDs, and seller-customized SKU values [C12]. Google Merchant inputs are additionally scoped by merchant data-source and offer identifiers before a processed Product is produced [C03].

Therefore:

```text
ID
≠ UNIVERSAL ENTITY

SAME PHYSICAL / COMMERCIAL SUBJECT
CAN HAVE MULTIPLE SCOPED IDENTIFIERS
```

When an ID matters, preserve its scope:

```text
who issued it?
for which market / shop / data source?
what object role does it identify?
when is it valid?
```

### 3.4 Variant is usually a role + relation, not a new primitive

A practical default is:

```text
OBJECT A
product family / model

OBJECT B
sellable configuration

A --[hasVariant]--> B
```

Then attach only the variant-defining and commercial state that matters:

```text
size
color
material
capacity
condition
price
stock
fulfillment
```

Google / Schema.org use `hasVariant` / `isVariantOf` around ProductGroup/Product structures [C02]. Lazada distinguishes normal/item-level attributes from SKU/variant-level sales properties [C12].

Do not create a durable `VARIANT` primitive merely because a platform API has a variation object.

### 3.5 Listing is an overloaded platform word

`Listing` can mean different things across environments:

- a seller-controlled submission;
- a seller SKU record;
- a platform catalog contribution;
- an addressable marketplace item;
- a public product page;
- a commercial offer;
- a customer-facing card or PDP.

Amazon explicitly separates seller listings from catalog items [C04]. Etsy's marketplace demonstrates that one listing can refer to an existing unique item, a set of similar items, a configurable specification, or a future made-to-order item [C11].

Therefore:

```text
"LISTING"
≠ ONE DURABLE OBJECT TYPE
```

Always resolve the local role before reasoning from the label.

---

## 4. Commercial relations and state

### 4.1 The thing and the conditions of sale are different questions

Use the distinction:

```text
WHAT IS THE THING / CONFIGURATION?

WHO OFFERS OR PROVIDES IT?

UNDER WHAT COMMERCIAL CONDITIONS?
```

GoodRelations treats an Offering and its commercial properties separately from the underlying product/service instance or model [C01]. Amazon separately exposes catalog/listing and pricing/offer operations [C04].

A useful practitioner representation is often:

```text
SELLER / SHOP
   --[offers / provides]-->
PRODUCT / VARIANT / ITEM

EDGE / COMMERCIAL STATE:
price
availability
condition
inventory
fulfillment
shipping
promotion
market
buyer eligibility
time
```

### 4.2 Offer is not automatically a core primitive

An API may expose an object called `Offer`. That is implementation evidence, not a reason to grow the durable core.

Default to relation + state when that preserves the decision:

```text
seller --[offers]--> item
price = ...
availability = ...
shipping = ...
```

Reify an offer as its own `OBJECT` only when its independently persistent identity matters — for example, when several offer records must be compared, linked, governed, versioned, or observed independently.

Therefore:

```text
API OBJECT CALLED OFFER
≠ OFFER MUST BE DURABLE PRIMITIVE
```

### 4.3 Commercial state is scoped and time-varying

Do not treat price, stock, fulfillment, or promotion as timeless product facts.

Possible scope includes:

```text
seller
variant
warehouse
market / country
buyer class
loyalty tier
voucher eligibility
quantity
session
time
```

Shopee currently documents buyer-relative displayed prices that can incorporate estimated vouchers available in the individual buyer's account, and multi-variant listings can show the lowest applicable variant price; the final checkout price can still differ [C08]. Lazada exposes SKU-level price, special-price validity, and inventory-related state [C12]. Google Merchant documentation also exposes time- and eligibility-sensitive commercial fields such as availability, loyalty/member pricing, minimum-order conditions, and automated discounts [C03].

Therefore:

```text
BASE PRICE
≠ VARIANT PRICE
≠ DISPLAYED PRICE
≠ FINAL CHECKOUT PRICE
```

These are conceptually different states even when two values happen to be numerically equal.

Likewise:

```text
SAME PRODUCT IDENTITY
≠ SAME COMMERCIAL STATE
```

### 4.4 Commercial representation can be buyer-relative

A card or PDP can be a composition of:

```text
product identity
+ selected variant / price range
+ seller state
+ promotion state
+ delivery state
+ buyer eligibility
+ platform policy
```

Do not assume every shopper sees the same commercial representation merely because the underlying product object is the same.

---

## 5. Product-descriptive data, commercial context, and observational context

A commerce surface often combines several information classes. Do not call all of them “product facts.”

### 5.1 Product-descriptive data

These describe or identify the thing/configuration itself:

```text
title / name
category
brand
GTIN / MPN / SKU or other identifiers
structured attributes
variant-defining attributes
description
images / video
material / dimensions / compatibility / model / specifications
```

### 5.2 Commercial context

These describe the conditions under which a seller/platform makes the thing available:

```text
price
stock
seller / shop
shipping / fulfillment
promotion / voucher
return policy
warranty terms when commercially scoped
payment / market eligibility
```

Some warranty properties may be intrinsic product promises while others are seller-specific commercial terms. Resolve provenance and scope rather than assuming one category universally.

### 5.3 Observational / social context

These originate from behavior, feedback, or aggregate marketplace history rather than directly describing the physical/domain thing:

```text
reviews
ratings
sold count
popularity labels
buyer photos
badges derived from prior behavior or service state
```

At origin these can be `OBSERVATION RECORDS` or aggregates. When displayed later, they become part of another shopper's `REPRESENTATION` / encounter context. They may also become machine-learning evidence. Do not silently reclassify them as intrinsic product truth.

Therefore:

```text
PRODUCT-DESCRIPTIVE FACT
≠ COMMERCIAL CONDITION
≠ OBSERVED / AGGREGATED FEEDBACK
```

### 5.4 Product truth is not identical to a submitted field

Keep at least these concepts separate when consequential:

```text
UNDERLYING FACT / CLAIM ABOUT THE THING

SELLER-DECLARED STRUCTURED FIELD

SELLER UNSTRUCTURED EXPRESSION
text / image / video

PLATFORM-PROCESSED RECORD

PLATFORM-INFERRED / MACHINE-DERIVED FACT OR REPRESENTATION
```

Google Merchant explicitly distinguishes `ProductInput` from the processed `Product`; rules, supplemental sources, automatic improvements, merging, and validation can alter the platform-held result [C03]. Lazada documents optional algorithmic auto-fill of unused attributes [C12]. Etsy has published systems that infer structured product information from unstructured listing text/images and generate internal product-understanding representations [C11]. AutoPKG similarly constructs and canonicalizes product-attribute knowledge from multimodal marketplace content [C13].

Therefore:

```text
SELLER INPUT
≠ PLATFORM-HELD PRODUCT RECORD

PLATFORM-INFERRED ATTRIBUTE
≠ VERIFIED PRODUCT TRUTH
```

### 5.5 Preserve fact provenance

A consequential product fact or claim can come from:

```text
manufacturer / brand authority
seller assertion
platform catalog
industry identifier
image evidence
structured feed
platform inference
buyer review
third-party certification
unknown
```

For a claim that affects purchase, compliance, safety, compatibility, or price interpretation, preserve source and confidence rather than laundering a derived field into fact.

### 5.6 Structured and unstructured information do different jobs

Do not treat title, category, attributes, description, images, search terms, or reviews as interchangeable keyword containers.

A structured attribute can support identity resolution, filtering, comparison, eligibility, machine understanding, or variant disambiguation. A title can support human identification and platform matching. An image can support visual identification, human evaluation, and machine retrieval. A description can support detailed comprehension and, on some systems, semantic relevance.

Field jobs are platform-specific and system-specific.

---

## 6. Representation discipline in commerce

### 6.1 Object ≠ representation ≠ surface

The Chapter 08 invariant generalizes directly:

```text
OBJECT
≠ REPRESENTATION
≠ ENCOUNTER SURFACE
```

Commerce examples:

```text
PRODUCT / ITEM
≠ PRODUCT CARD
≠ SEARCH RESULTS SURFACE

PRODUCT / ITEM
≠ PDP REPRESENTATION
≠ PRODUCT-DETAIL SURFACE

PRODUCT
≠ CREATOR PRODUCT ANCHOR
≠ SHOPPABLE VIDEO SURFACE
```

TikTok Shop demonstrates this strongly: a video can exist independently, then receive a product link, and in supported cases the commerce target can later be relinked without recreating the video [C05].

### 6.2 A commerce representation can compose multiple objects and states

A search card or PDP can present information drawn from:

- product identity;
- variant family;
- seller / shop identity;
- commercial relation;
- price / stock / shipping state;
- prior observation aggregates such as ratings/reviews;
- platform labels;
- buyer-relative promotions;
- policy / eligibility state.

Therefore:

```text
CUSTOMER-FACING CARD
≠ ONE DATABASE ROW
```

### 6.3 Human-facing and machine representations are different

Use:

```text
SOURCE PRODUCT INFORMATION
↓
SYSTEM-SPECIFIC MACHINE REPRESENTATION
↓
RETRIEVAL / MATCHING / RELEVANCE / RECOMMENDATION

and separately

SOURCE / PLATFORM STATE
↓
HUMAN-FACING REPRESENTATION
↓
SHOPPER ENCOUNTER
```

The same source information may feed both branches, but the representations are not the same object.

Shopee MRSE constructs multimodal retrieval representations from query/item/user evidence [C06]. Shopee MIEM constructs item embeddings for image search from multiple images plus textual information [C07]. Etsy uses rich listing information to build semantic-relevance models and internal product-understanding representations [C10][C11]. Lazada AutoPKG derives canonical product-attribute graph information from multimodal listing content [C13]. OpenAI/ACP and Shopify additionally expose structured product/catalog data directly to AI-mediated discovery systems [AC04][AC06][AC07].

Therefore:

```text
SELLER FIELD
≠ MACHINE / AGENT REPRESENTATION
≠ HUMAN-FACING REPRESENTATION
```

The same field can feed both machine and human representations; the roles are conceptually distinct, not mutually exclusive.

### 6.4 One asset or record can have several jobs

A primary image, title, review, or attribute can simultaneously participate in different systems.

For example, an image may be:

```text
human selection representation
human evaluation evidence
machine visual-retrieval input
source for inferred attributes
policy / quality-check input
```

A review can begin as an observation record, later become visible feedback context, and also become training or product-understanding evidence.

Do not infer one job from evidence about another system.

---

# Part II — Discovery and mediation

## 7. Discovery context is broader than a text query

A shopper can enter discovery through:

```text
keyword / text query
semantic query
image query
category / browse state
current product context
current cart / order context
social content / creator context
conversation / assistant request
recommendation module
prior behavior / history
external referral
```

Shopee documents keyword/image search plus current conversational product discovery through the Shopee App in ChatGPT [C08][C15]. Google documents AI/conversational shopping that can involve longer, more complex multi-constraint requests [C14]. ChatGPT shopping research likewise supports natural-language preferences, budget, constraints, comparison, trade-offs, and visual product discovery [AC07].

Therefore:

```text
TEXT QUERY
≠ ONLY DISCOVERY PATH
```

and:

```text
SHOPPER LANGUAGE
≠ ONE EXACT KEYWORD STRING
```

A useful generic term is **discovery context** rather than assuming every path begins with one explicit keyword query.

### 7.1 Query modality ≠ retrieval-model modality

A text query does not imply text-only product matching.

Shopee MRSE is explicit evidence that a text-query retrieval system can combine query text with item images and multimodal user preferences/history [C06].

Likewise, an image query does not imply image-only item representation: Shopee MIEM combines textual product information with multiple item images for Image Search [C07]. ChatGPT and Google product-discovery experiences also support visual/multimodal shopping contexts [C14][AC07].

Therefore:

```text
USER INPUT MODALITY
≠ ALL MACHINE EVIDENCE USED FOR MATCHING
```

---

## 8. Eligibility, retrieval, relevance, ranking, filtering, sorting, and composition

Do not compress every discovery outcome into “ranking.”

A generic system may contain some or all of these distinct stages or controls:

```text
ELIGIBILITY / INDEXABILITY
can the object participate in this system?

MATCHING / CANDIDATE GENERATION / RETRIEVAL
what enters a relevant candidate set?

RELEVANCE ESTIMATION
how well does candidate meaning fit the request/context?

SCORING / RANKING
how competitive are candidates under the current objective?

RE-RANKING / CONSTRAINTS
how do diversity, safety, repetition, seller/provider or other constraints alter order?

USER FILTERING
which candidates are removed by explicit shopper constraints?

USER SORTING
which explicit ordering did the shopper request?

COMPOSITION
which modules / cards / paid-organic mixtures / result types are finally assembled?

VISIBILITY / PRESENTATION
what representation is actually served?
```

Implementations differ. Do not claim a stage exists on a platform unless evidence supports it.

### 8.1 Search influence is not one mechanism

One of the most important commerce invariants is:

```text
FIELD INFLUENCES END-TO-END SEARCH
≠ FIELD PARTICIPATES IN INITIAL RETRIEVAL
≠ FIELD CONTRIBUTES TO SEMANTIC RELEVANCE
≠ FIELD CONTRIBUTES TO RANKING
≠ FIELD IS USER-FACING
```

Etsy is a strong documented example **because its current official sources themselves expose different abstraction levels rather than one settled field-to-stage map**. Etsy's October 2025 legal disclosure describes first-phase query matching across titles, attributes, categories, and tags. Current Seller Handbook guidance is broader: `Keywords 101` explicitly says keywords across titles, descriptions, tags, categories, and attributes participate in query matching, the first phase, while `How Etsy Search Works` places a holistic listing — including descriptions, first photo, reviews, and more — under Query matching [C09].

Etsy Engineering then describes a separate January 2026 semantic-relevance model whose first disclosed application is **post-retrieval**; that model consumes richer listing information including images, descriptions, attributes, variations, and extracted entities, and can filter retrieved candidates, enrich downstream ranking features, affect ranking loss, and boost final results [C10]. Its statement that this semantic-relevance model begins post-retrieval does not establish that descriptions or other rich listing data are absent from every separate initial matching/retrieval mechanism.

Therefore:

```text
OFFICIAL SOURCES CAN DISAGREE / DIFFER IN ABSTRACTION
ABOUT FIELD PARTICIPATION AT A SEARCH STAGE

→ preserve source + date + abstraction level
→ do not force false consistency
→ exact production boundary may remain UNKNOWN
```

A statement such as “field X matters for search” is insufficient to infer the stage, weight, or seller tactic; equally, one narrower public enumeration is insufficient to negate a broader explicit official claim without stronger implementation evidence.

### 8.2 User filter and sort are not hidden ranking weights

Shopee lets buyers explicitly filter/sort by criteria such as category, location, shipping, price, newest, best-selling, rating, and other options [C08].

Therefore:

```text
RESULTS AFTER USER FILTER
≠ EVIDENCE THAT FILTER PROPERTY IS A DEFAULT-RANKING WEIGHT
```

and:

```text
USER-SELECTED SORT
≠ DEFAULT PLATFORM RANKING
```

This distinction is essential when interpreting screenshots, local search observations, or “ranking factor” folklore.

### 8.3 Paid ranking ≠ organic ranking

A marketplace can expose bid, expected CTR/CVR, quality, sales, price, promotion, or other sponsored-placement factors without disclosing the organic system.

Never transfer:

```text
SPONSORED / AD RANKING DISCLOSURE
→ ORGANIC SEARCH RULE
```

without direct evidence.

### 8.4 Eligibility ≠ high rank ≠ realized exposure

A complete seller submission, valid structured data, eligible product, or recommendation-eligible item is not guaranteed to be retrieved, highly ranked, composed into a final slate, or exposed.

Keep:

```text
VALID / ACCEPTED
≠ ELIGIBLE
≠ RETRIEVED
≠ HIGHLY RANKED
≠ SERVED
≠ PURCHASED
```

OpenAI's merchant-feed terms are an especially direct stress case: submitting merchant content does not obligate OpenAI to use or surface it [AC07]. Therefore richer or more complete product data can improve representational quality without guaranteeing recommendation or exposure.

---

## 9. Recommendation and non-query discovery

Commerce recommendation can start from many contexts:

```text
current product
current category
current video / creator content
shopper history
cart contents
order history
home / discovery feed
campaign or collection
shopper mission
conversation / assistant request
```

The recommended object may itself be:

```text
product / item
listing
variant
shop
collection
offer / commercial relation
creator-product opportunity
```

Do not assume the same ranking objective applies to each module.

A homepage discovery module, “similar products” carousel, cart suggestion, related-product module, creator-link recommendation, conversational shopping assistant, and post-purchase recommendation can optimize or support different next actions.

Therefore:

```text
SAME OBJECT
+ DIFFERENT MODULE / SHOPPER MISSION
→ DIFFERENT MEDIATION CONTEXT
```

Multi-stakeholder recommendation research also warns that platform/provider objectives can matter alongside the end user [R34].

---

## 10. Hybrid content-commerce environments

Social commerce is not a reason to collapse product into content.

TikTok Shop provides a direct stress case:

```text
OBJECT A = VIDEO
OBJECT B = PRODUCT / SHOP / COLLECTION

A --[links to / promotes]--> B
```

The content can exist first and the commerce link can be added later; supported relinking can change the target while the video persists [C05].

This preserves three distinctions:

```text
CONTENT OBJECT
≠ COMMERCE OBJECT
≠ CONTENT↔COMMERCE RELATION
```

and:

```text
COMMERCE TARGET
≠ PRODUCT ANCHOR / LINK REPRESENTATION
```

### 10.1 Creator ≠ seller ≠ claim source

In creator commerce, actors can have separate roles:

```text
SELLER / MERCHANT
owns or commercially provides the item

CREATOR
publishes or demonstrates content

BRAND / MANUFACTURER
may support product claims

PLATFORM
mediates discovery, eligibility, attribution, and transaction
```

A commercial relationship does not transfer first-person experience or factual authority automatically.

### 10.2 Content metrics and commerce metrics can share an object history without sharing causal meaning

A shoppable content object can accumulate:

```text
video impressions
content engagement
product-anchor impressions
product clicks
PDP visits
orders
GMV
```

Preserve which event belongs to which surface, edge, exposure regime, and attribution rule before interpreting the aggregate.

### 10.3 Agent-mediated and delegated commerce

Agentic commerce adds a consequential authority/transaction dimension, but it does **not** require a new durable primitive. Use the existing actor, typed-edge, state, provenance, scope, and history model.

A useful map is:

```text
SHOPPER / USER
   │
   │ intent / preference / request
   ▼
SHOPPING AGENT / PLATFORM
   │
   │ may have capability to search / cart / checkout
   │
   ├──[delegated / authorized within scope]──► operation
   │
   └──[requests / submits]───────────────────► MERCHANT / BUSINESS
                                                  │
                                                  ├ accepts / rejects
                                                  ├ returns checkout state
                                                  └ returns order state
```

Keep these states separate:

```text
SHOPPER INTENT
≠ DELEGATED ACTION AUTHORITY
```

A request such as “find me a laptop under $1,000” can authorize discovery without authorizing a purchase.

```text
PLATFORM / AGENT CAPABILITY
≠ USER AUTHORIZATION
≠ SUCCESSFUL EFFECT
```

A system can technically support checkout while the current user/session lacks authority to complete it. UCP standard checkout requires user finalization through a trusted UI unless AP2 Mandates is negotiated; AP2 then cryptographically binds user authorization to the specific checkout state and funds transfer [AC01][AC02].

#### 10.3.1 Authorization is scoped to state, constraints, and time

When delegated authority matters, preserve at least:

```text
who authorized whom?
which operation?
which product / quantity / seller?
what price / total / currency constraints?
what payment / shipping scope?
what expiry or session scope?
what checkout state was authorized?
```

If the material transaction state changes outside the authorization boundary, do not silently carry authority forward.

Example:

```text
user authorizes purchase ≤ $1,000
checkout later becomes $1,028 after shipping

PRIOR AUTHORIZATION
≠ AUTOMATIC AUTHORIZATION OF NEW TOTAL
```

The exact re-authorization mechanics are protocol/platform-specific, but the analytical distinction is durable.

#### 10.3.2 Discovery state ≠ authoritative checkout state ≠ authoritative order state

Agentic systems make stage-specific authority explicit.

ACP uses merchant product feeds for ingestion/indexing/discovery, then requires the merchant checkout integration to return a rich authoritative cart state with current items, pricing, taxes/fees, shipping, discounts, totals, and status [AC04][AC05]. UCP Order separately treats an order as the authoritative current-state snapshot after a successful checkout submission [AC03].

Therefore:

```text
DISCOVERY / INDEX REPRESENTATION @ t0
≠ AUTHORITATIVE CHECKOUT STATE @ t1
≠ AUTHORITATIVE ORDER STATE @ t2
```

A merchant feed can be an authoritative product-data input for discovery while still becoming stale for the later transaction. Preserve **authority by stage + time**, not one timeless “source of truth” label.

Likewise:

```text
CHECKOUT REQUEST / SESSION
≠ MERCHANT-ACCEPTED ORDER
≠ PAYMENT SUCCESS
≠ FULFILLMENT / DELIVERY COMPLETION
```

Do not report “purchased” merely because an agent submitted a request or opened a checkout session.

#### 10.3.3 Agent-consumable representation ≠ human-facing generated representation

Some commerce systems now expose structured catalog interfaces directly to AI agents. Shopify's Global Catalog and Storefront Catalog implement UCP Catalog interfaces for agent search/lookup/product retrieval and can accept buyer context such as location, language, currency, and intent [AC06]. ACP/OpenAI similarly accepts structured merchant product data for product discovery, while ChatGPT can generate its own concise product representations for shoppers [AC04][AC07].

Keep:

```text
MERCHANT / PRODUCT STATE
↓
AGENT-CONSUMABLE REPRESENTATION
↓
AGENT REASONING / SELECTION
↓
HUMAN-FACING GENERATED REPRESENTATION
↓
SHOPPER DECISION
```

The agent-facing product representation can contain structured fields, variants, offers, availability, and machine context that are not identical to the concise recommendation a person sees.

This is still the Chapter 08/09 representation invariant:

```text
OBJECT
≠ REPRESENTATION
≠ ENCOUNTER SURFACE
```

not a new ontology.

#### 10.3.4 Encounter / checkout surface ≠ commercial responsibility

A shopper can encounter or even complete a mediated checkout inside an AI/search surface while another business remains seller/Merchant of Record and a separate payment provider handles payment rails [AC01][G10].

Preserve actor roles when material:

```text
DISCOVERY / CONVERSATIONAL SURFACE
≠ SELLER / MERCHANT OF RECORD
≠ PAYMENT-PROCESSING ROLE
≠ FULFILLMENT / RETURNS / SUPPORT ROLE
```

Do not infer that the interface where the user clicked “Buy” owns every commercial responsibility.

#### 10.3.5 When the agentic layer deserves deeper reasoning

Use this layer only when the decision involves one or more of:

```text
delegated purchase / autonomous action
authorization scope or expiry
agent capability vs user permission
checkout-state drift after discovery
merchant acceptance / rejection
order-state reconciliation
agent-facing product data
merchant-of-record / payment / fulfillment responsibility
```

A simple title, description, or ordinary product-card task does not need agentic-commerce protocol theory.

---

# Part III — Shopper state, evaluation, and observation

## 11. Shopper state is not one universal funnel stage

Useful states can include:

```text
discovering
orienting / identifying what the product is
refining intent
comparing alternatives
evaluating fit / trust / risk
configuring a variant / quantity / personalization
evaluating commercial conditions
ready to transact
post-purchase evaluation
```

A shopper can enter at any point and can move backward or sideways.

Do not force every task through:

```text
awareness → consideration → conversion
```

when the actual platform state is more specific.

### 11.1 Selection and evaluation representations have different jobs

A search card, recommendation card, or creator anchor often helps answer:

> Is this worth entering or examining further?

A PDP or detailed listing representation often helps answer:

> Is this the right thing, configuration, seller, and commercial condition for me?

Checkout representations answer yet another question:

> What exactly will I receive and under what final price, delivery, payment, and policy conditions?

Therefore:

```text
SELECTION REPRESENTATION
≠ EVALUATION REPRESENTATION
≠ TRANSACTION REPRESENTATION
```

Even when they refer to the same product object.

### 11.2 High discoverability ≠ high purchase intent

An item can be highly retrievable or visible because it is relevant to a broad query, visually similar, popular, promoted, or strongly represented while still attracting low transaction intent.

Likewise, low search volume can coexist with high conversion among a narrow high-intent audience.

Do not equate:

```text
QUERY VOLUME
≠ MARKET SIZE
≠ PURCHASE INTENT

IMPRESSION VOLUME
≠ PRODUCT-MARKET FIT
```

---

## 12. Observation records for commerce

Commerce measurement can include:

```text
search impression
recommendation impression
card impression
PDP visit
variant selection
add to cart
checkout start
order created
payment
shipment
completion
after-sale / cancellation
return / refund
review
repeat purchase
```

Do not collapse these into one conversion label.

### 12.1 Purchase is an outcome, not pure preference

Observed purchase can depend on:

```text
exposure
position
availability
price
promotion
shipping
seller trust
payment options
variant availability
policy / eligibility
urgency
prior familiarity
external influence
```

Recommendation and ranking research already establishes that implicit behavior is generated under selective exposure [R32][R33][R44]. Etsy engineering explicitly documents that clicks/add-to-carts/purchases can be biased proxies for semantic relevance; its experiments can show semantic relevance improve while engagement moves differently [C10].

Therefore:

```text
OBSERVED PURCHASE
≠ PURE PRODUCT PREFERENCE
≠ PURE SEMANTIC RELEVANCE
≠ SOLE EFFECT OF THE LAST REPRESENTATION
```

### 12.2 Reviews and displayed aggregates can change roles over time

A review, rating, sold count, or buyer photo can begin as an `OBSERVATION RECORD` or aggregate of observations. Later it can become:

```text
human-facing trust / evaluation context
machine product-understanding evidence
ranking / relevance input where disclosed
platform quality / governance evidence
```

This is a role transition / secondary use, not evidence that reviews are intrinsic product attributes.

### 12.3 Observation maturity matters

Commerce outcomes can mature after the initial order:

```text
order
→ payment
→ shipment
→ delivery
→ cancellation / return / refund
→ retention / repeat purchase
```

Recent orders are not necessarily mature business outcomes. Preserve event time, reporting time, return/refund horizon, and attribution rules when they can change interpretation [R47].

### 12.4 Organic, paid, affiliate, creator, and AI-mediated exposure need provenance

A product can accumulate sales from:

```text
organic search
organic recommendation
AI / conversational recommendation
paid ads
creator / affiliate content
shop page
external referral
notification / retargeting
unknown / mixed
```

Do not treat aggregate product-level performance as organic demand without exposure provenance.

### 12.5 Attributed ≠ incremental ≠ causal

A marketplace can assign credit to a search, ad, affiliate link, creator, assistant, or last touch without proving that exposure caused an incremental purchase.

Keep the Chapter 08 invariant:

```text
ATTRIBUTED
≠ INCREMENTAL
≠ CAUSAL
```

Use Chapter 05 when experiment or causal attribution becomes consequential.

---

# Part IV — Product-information and representation decisions

## 13. Allocate information by job, not by field folklore

Do not start with:

```text
Which keywords belong in the title?
```

Start with:

```text
WHAT FACT / CLAIM / DISTINCTION MATTERS?
↓
WHO OR WHAT NEEDS IT?
↓
WHAT JOB MUST IT PERFORM?
↓
WHICH PLATFORM-SUPPORTED CARRIER BEST PERFORMS THAT JOB?
```

Possible jobs include:

### Human identification

Help a shopper quickly understand what the thing is and which salient variant or use case distinguishes it.

Potential carriers, platform permitting:

```text
title
primary image
variant label
short visible highlights
```

### Human evaluation

Help a shopper judge fit, quality, compatibility, dimensions, material, use, risk, proof, or trade-offs.

Potential carriers:

```text
description
images / video
structured specs
comparison information
review representations
warranty / return / shipping context
```

### Machine identity resolution

Help a platform distinguish or reconcile the thing with catalog identities.

Potential carriers:

```text
GTIN / EAN / UPC / ISBN
brand
MPN
platform-specific identifiers
category
variant-defining attributes
```

### Machine retrieval / relevance / filtering

Help a platform match the object to a query, semantic context, visual request, browse state, or explicit filter.

Potential carriers depend on the platform and disclosed system:

```text
title
attributes
category
tags / search terms
images
description
behavioral / contextual representations
machine-derived features
```

Do not assume every listed carrier participates in every platform stage.

### Commercial eligibility and transaction

Help determine whether and how a shopper can buy:

```text
price
stock
seller / shop
shipping
promotion
payment
return / warranty terms
market eligibility
buyer eligibility
```

### 13.1 One fact may need several non-identical representations

A fact can be expressed:

- structurally for machine filtering;
- visibly for quick human comparison;
- deeply in a PDP for evaluation;
- in an image for proof;
- in an agent-facing catalog/feed for machine consumption;
- in a transaction representation for final confirmation.

Repetition is not automatically bad if each representation serves a materially different consumer or job. But redundant keyword stuffing is not justified merely because several fields exist.

### 13.2 Do not use copy to repair missing structured truth

If compatibility, dimensions, size, color, model, GTIN, stock, or another decision-critical fact belongs in a platform-supported structured attribute, do not assume prose can substitute for it.

Likewise, do not assume a structured attribute alone communicates enough to a human buyer.

Use:

```text
STRUCTURED PRODUCT FACT
≠ HUMAN EXPLANATION
```

when both jobs matter.

### 13.3 Searchability ≠ visibility

A field may influence machine systems without appearing prominently to the shopper. A visible field may be designed mainly for human selection while machine systems use richer hidden or derived representations.

Therefore:

```text
SEARCHABLE / MACHINE-CONSUMED
≠ USER-FACING
```

and:

```text
VISIBLE EARLY
≠ AUTOMATIC RANKING PRIORITY
```

A field can deserve early placement because people scan it, not because front-loading is a ranking boost.

### 13.4 Optimize for resolvability, not imagined model weights

AI-native, semantic, conversational, and agentic product discovery increase the importance of one practitioner question:

> Can the system resolve the shopper's material requirement from truthful product facts, relations, representations, and current commercial state?

Current Google, Shopee, ChatGPT/ACP, and multimodal Shopee evidence supports discovery contexts that can combine natural-language intent, preferences, budget, product features, technical specifications, images, prior/context state, and multiple constraints [C06][C07][C14][C15][AC04][AC07]. This does **not** expose one universal model or seller ranking formula.

Treat a conversational request as a bundle of potentially decision-relevant constraints rather than as a string to stuff into fields. Common dimensions can include:

```text
use case
compatibility
hard constraints / exclusions
preferences
physical dimensions / technical specifications
material / performance property
budget / current price
trade-offs / limitations
variant requirements
related accessory / substitute / spare-part need
availability / shipping state
```

A durable seller-side sequence is:

```text
SHOPPER REQUIREMENT
↓
WHAT TRUE FACT / RELATION / STATE WOULD RESOLVE IT?
↓
DO WE HAVE SUPPORT FOR THAT FACT?
↓
WHICH PLATFORM-SUPPORTED CARRIER HAS THE RIGHT JOB?
↓
REPRESENT IT ACCURATELY AND KEEP IT CURRENT
```

Examples, platform permitting:

```text
identity / use-defining product concept
→ clear title / description

exact size / material / specification / supported compatibility identifier
→ structured attribute / product detail

finite variant requirement
→ variant / configuration field

compatibility question / limitation / nuanced use condition
→ Q&A / document / description where supported

visible physical property
→ truthful image / multimodal evidence + structured/text fact where appropriate

accessory / replacement / substitute relation
→ merchant-declared typed relation where supported

budget / availability / delivery constraint
→ current price / stock / shipping / commercial state
```

The key distinction is:

```text
MACHINE LEGIBILITY
≠ KEYWORD DENSITY
≠ GUARANTEED RANKING
```

```text
SEMANTIC MATCHABILITY
≠ PROVEN RANKING BOOST
```

```text
SHOPPER LANGUAGE
≠ EXACT KEYWORD MATCH ONLY
```

```text
PRODUCT FACT COMPLETENESS
≠ GUARANTEED RETRIEVAL / RECOMMENDATION / EXPOSURE
```

```text
OPTIMIZE FOR RESOLVABILITY
≠ OPTIMIZE FOR IMAGINED MODEL WEIGHTS
```

#### 13.4.1 Truth bounds resolvability

Do not invent a fact merely because it would satisfy a common conversational query.

Do **not** turn:

```text
people ask "works with MacBook Pro"
```

into:

```text
mark compatible with MacBook Pro
```

unless compatibility is actually established for the relevant model/version/use.

Likewise, do not add unsupported phrases such as “ideal for travel,” “safe for children,” “professional grade,” or “fits small spaces” merely to cover more semantic intents. If the product evidence does not resolve the constraint, preserve the gap or obtain stronger evidence.

Therefore:

```text
INFERABLE / POPULAR USE CASE
≠ SELLER-AUTHORIZED PRODUCT CLAIM
```

#### 13.4.2 Structured facts and natural-language explanation are complementary

A precise structured value can help machine systems distinguish/filter/compare, while natural language can explain context and trade-offs. Neither universally replaces the other.

Use:

```text
STRUCTURED FACT
+ TRUTHFUL NATURAL-LANGUAGE CONTEXT WHEN NEEDED
```

not:

```text
REPEAT SAME KEYWORD IN EVERY FIELD
```

Google's current guidance is unusually explicit here: structured `product_detail` is for technical/verifiable information, while `product_highlight` should not be used as a list of search/SEO keywords [C14].

#### 13.4.3 Multimodal evidence should resolve visible facts, not become decorative optimization folklore

When a property is visually inspectable — shape, color, configuration, included parts, interface layout, material appearance, relative form — accurate images can provide evidence to both humans and some machine systems. Shopee's published retrieval/image-search work demonstrates that item representations can combine text and images [C06][C07], and ChatGPT/Google expose visual shopping paths [C14][AC07].

Do not infer:

```text
MORE / STYLED IMAGES
→ GUARANTEED SEMANTIC OR RANKING BOOST
```

The practitioner job is to reduce ambiguity and mismatch with truthful visual evidence.

#### 13.4.4 Completeness improves representability, not certainty of selection

A merchant can supply excellent structured data and still not be retrieved, recommended, highly ranked, or shown. OpenAI explicitly does not guarantee use/surfacing of submitted merchant content [AC07], and Google field/support documentation likewise does not promise exposure from completeness alone [C14].

Therefore:

```text
COMPLETE / CURRENT PRODUCT REPRESENTATION
CAN REDUCE INFORMATION GAPS

≠ GUARANTEED CANDIDACY
≠ GUARANTEED RECOMMENDATION
≠ GUARANTEED RANK
```

### 13.5 A compact resolvability test

For a consequential AI/conversational-discovery task, ask only what is material:

```text
Can the system determine what the product is?
Can it distinguish the relevant variant?
Can it resolve required dimensions/specifications?
Can it determine compatibility where compatibility is established?
Can it resolve hard exclusions or limitations?
Can it distinguish preferences from hard constraints?
Can it access current price / availability / shipping where relevant?
Can it explain a material trade-off without inventing one?
Can it identify a related accessory / substitute relation when supported?
Can visible claims be checked against images / other evidence?
```

If the answer is “no,” fix the factual/product-data gap in the appropriate supported carrier when possible. Do not respond by increasing keyword density.

---

## 14. Field-level evidence discipline

When a platform says a field “helps search,” “improves discoverability,” “is searchable,” “increases product score,” “is used by recommendation,” or “helps AI systems understand products,” preserve the exact claim.

Ask:

```text
which platform?
which system / surface?
which field?
which stage?
which object role?
which market/account regime?
which date?
what was actually measured or disclosed?
```

When current official sources describe the **same stage** differently, preserve the conflict and abstraction level rather than silently picking the source that makes the cleanest architecture diagram.

Do not silently transform:

```text
FIELD IS SEARCHABLE / AGENT-READABLE
```

into:

```text
FIELD HAS ORGANIC / AI RANKING WEIGHT X
```

or:

```text
REPEAT KEYWORD IN FIELD
```

Likewise, an A/B test showing that platform-derived attributes improved Search or Recommendation business outcomes in one implementation does not establish that a seller can reproduce the effect by manually adding arbitrary attributes [C13].

---

# Part V — Durable anti-folklore rules

## 15. Minimal commerce invariants worth keeping

Use only the distinctions that prevent a material error.

```text
DO NOT ASSUME
DOMAIN / PRODUCT IDENTITY = PLATFORM RECORD IDENTITY
```

```text
ID
≠ UNIVERSAL ENTITY
```

```text
WHEN DISTINCT ROLES EXIST:
PRODUCT FAMILY / MODEL
≠ SELLABLE CONFIGURATION
≠ INDIVIDUAL ITEM
```

```text
OBJECT
≠ REPRESENTATION
≠ ENCOUNTER SURFACE
```

```text
SELLER INPUT
≠ PLATFORM-PROCESSED RECORD
≠ CUSTOMER-FACING REPRESENTATION
```

```text
PRODUCT-DESCRIPTIVE FACT
≠ COMMERCIAL CONDITION
≠ OBSERVATION / FEEDBACK AGGREGATE
```

```text
PRODUCT FACT / CLAIM
≠ SELLER FIELD
≠ PLATFORM-INFERRED FACT
```

```text
VARIANT ROLE
≠ NEW DURABLE PRIMITIVE
```

```text
COMMERCIAL RELATION
≠ PRODUCT IDENTITY
```

```text
BASE PRICE
≠ DISPLAYED PRICE
≠ FINAL CHECKOUT PRICE
```

```text
SEARCH INFLUENCE
≠ RETRIEVAL PARTICIPATION
≠ RELEVANCE CONTRIBUTION
≠ RANKING CONTRIBUTION
≠ FINAL REPRESENTATION
```

```text
OFFICIAL SOURCE A
≠ AUTOMATICALLY A COMPLETE IMPLEMENTATION OVERRIDE
OF OFFICIAL SOURCE B

WHEN THEY CONFLICT:
PRESERVE SOURCE + DATE + ABSTRACTION LEVEL + UNKNOWN
```

```text
QUERY MODALITY
≠ RETRIEVAL-MODEL MODALITY
```

```text
MACHINE LEGIBILITY
≠ KEYWORD DENSITY
≠ GUARANTEED RANKING
```

```text
SEMANTIC MATCHABILITY
≠ PROVEN RANKING BOOST
```

```text
SHOPPER LANGUAGE
≠ EXACT KEYWORD MATCH ONLY
```

```text
PRODUCT FACT COMPLETENESS
≠ GUARANTEED RETRIEVAL / RECOMMENDATION / EXPOSURE
```

```text
OPTIMIZE FOR RESOLVABILITY
≠ OPTIMIZE FOR IMAGINED MODEL WEIGHTS
```

```text
MERCHANT-DECLARED PRODUCT RELATION
≠ PLATFORM-INFERRED RELATION
≠ OBSERVED BEHAVIORAL RELATION
```

```text
DEFAULT RANKING
≠ USER FILTER
≠ USER SORT
```

```text
PAID / SPONSORED RANKING
≠ ORGANIC RANKING
```

```text
VALID / ELIGIBLE
≠ RETRIEVED
≠ HIGHLY RANKED
≠ EXPOSED
```

```text
SEARCHABLE
≠ USER-FACING
```

```text
SEARCH VOLUME
≠ MARKET SIZE
≠ PURCHASE INTENT
```

```text
OBSERVED PURCHASE
≠ PURE PREFERENCE
```

```text
SHOPPER INTENT
≠ DELEGATED ACTION AUTHORITY
```

```text
PLATFORM / AGENT CAPABILITY
≠ USER AUTHORIZATION
≠ SUCCESSFUL EFFECT
```

```text
DISCOVERY / INDEX STATE
≠ AUTHORITATIVE CHECKOUT STATE
≠ AUTHORITATIVE ORDER STATE
```

```text
REQUEST / CHECKOUT SESSION
≠ MERCHANT-ACCEPTED ORDER
≠ PAYMENT / FULFILLMENT COMPLETION
```

```text
AGENT-CONSUMABLE REPRESENTATION
≠ HUMAN-FACING GENERATED REPRESENTATION
```

```text
ENCOUNTER / CHECKOUT SURFACE
≠ MERCHANT OF RECORD
≠ PAYMENT / FULFILLMENT RESPONSIBILITY
```

```text
API OBJECT NAME
≠ DURABLE ANALYTICAL PRIMITIVE
```

```text
CURRENT PLATFORM DOCUMENTATION
≠ TIMELESS PRODUCTION REGIME
```

Do not memorize these as a checklist. Apply the minimum distinction that changes the decision.

---

# Part VI — Runtime use

## 16. Fast path for simple product communication

Do not make every title, bullet, description, or image-alt task traverse the full commerce graph.

If the user supplies a narrow task and sufficient product facts, use:

```text
CURRENT JOB
→ PLATFORM / SURFACE IF MATERIAL
→ PRODUCT / VARIANT ROLE IF MATERIAL
→ FACT / CLAIM BOUNDARY
→ REPRESENTATION JOB
→ DRAFT
```

Examples:

- rewriting a supplied product title for clarity does not require reconstructing the platform ranker;
- turning known specs into concise highlights does not require a catalog-identity audit unless identity is ambiguous;
- editing a description for readability does not require shopper-funnel theory when the audience and facts are already resolved;
- choosing between two primary images can focus on identification/evaluation job unless search/image-retrieval behavior is material and supported.

Do not reopen the full commerce model merely because the object is a product or because an AI shopping surface exists.

---

## 17. Deeper path for consequential commerce decisions

Use deeper reasoning when the task involves decisions such as:

- marketplace launch / migration;
- product-family or variant architecture;
- catalog/listing identity mismatch;
- search, semantic, conversational, or recommendation discoverability diagnosis;
- product-data allocation across human/machine/agent-facing carriers;
- structured-attribute strategy;
- product resolvability for complex shopper constraints;
- seller/offer/price/stock/shipping conflicts;
- social-commerce linking;
- delegated / agentic purchase authority or checkout-state drift;
- merchant-of-record / payment / fulfillment responsibility in mediated checkout;
- organic/paid/affiliate attribution;
- large product-page or feed redesign;
- unexplained changes in impressions, clicks, carts, orders, or GMV.

A compact dependency map is:

```text
JOB + FACT / CLAIM SOURCES
↓
OBJECT IDENTITIES + TYPED RELATIONS
↓
COMMERCIAL STATE + SCOPE
↓
PRODUCT-DESCRIPTIVE DATA + COMMERCIAL / OBSERVATIONAL CONTEXT
↓
MACHINE / AGENT / HUMAN REPRESENTATION JOBS
↓
DISCOVERY / MEDIATION SYSTEM IF MATERIAL
↓
AUTHORIZATION / TRANSACTION STATE IF MATERIAL
↓
SHOPPER STATE + DESIRED INTERACTION
↓
OBSERVATION RECORD
↓
BOUNDED LEARNING / DECISION
```

This is not a mandatory linear workflow.

### 17.1 Compact commerce context record

Use an explicit record only when a complex task benefits from one.

```text
COMMERCE CONTEXT

Job / decision:
Platform / market / surface:

Actors / claim sources:
Seller / shop if material:
Creator / affiliate if material:
Shopping agent / platform if material:
Merchant of Record / payment / fulfillment roles if material:

Object identities:
Product family / model if material:
Variant / configuration if material:
Listing / platform record if material:
Identity / identifier scope:

Commercial relation / state:
Price / promotion:
Stock / availability:
Shipping / fulfillment:
Buyer-relative eligibility if material:

Product-descriptive facts / source provenance:
Compatibility / dimensions / specs if material:
Use-case / constraint / trade-off claims and evidence if material:
Commercial context:
Observation / feedback context if material:
Seller-submitted fields:
Platform-processed or inferred data if material:

Human-facing representation job:
Machine / agent representation evidence if material:
Discovery context / shopper constraints:
Relevant retrieval / ranking / filtering / recommendation evidence:
Known internal UNKNOWNs:

Delegated authority / constraints if material:
Authoritative checkout state if material:
Merchant acceptance / order state if material:

Shopper state / desired action:
Observation record if learning from performance:
Primary business outcome / maturity horizon:
Claim / policy constraints:
```

Omit fields that cannot change the decision. Do not fill unknowns with invented precision.

---

## 18. Diagnosing weak or changing commerce performance

Do not jump from lower sales to title rewriting.

Check only the material items:

```text
1. OBSERVATION RECORD
What changed: impressions, clicks, PDP visits, carts, paid orders,
completed orders, GMV, returns, or another metric?

2. IDENTITY / CATALOG STATE
Same product, variant family, listing, SKU mapping, category,
or platform record?

3. COMMERCIAL STATE
Same price, stock, promotion, shipping, fulfillment,
seller eligibility, and buyer-relative conditions?

4. PRODUCT RESOLVABILITY / REPRESENTATION
Same title, primary image, card, variant presentation,
PDP structure, structured facts, compatibility/spec data,
or machine/agent-processed product data?
Can the product still resolve the material shopper constraints truthfully?

5. DISCOVERY / MEDIATION
Same search/recommendation/conversational surface, filters, sort,
organic/paid/AI-referral mix, eligibility, or platform regime?

6. SHOPPER / TRAFFIC STATE
Same query/request mix, audience mix, mission, constraints, market,
device, account/personalization state, or creator/referral source?

7. RESPONSE OPPORTUNITY
Was the relevant variant in stock and buyable?
Could the shopper/system see and resolve the required information?

8. TRANSACTION / AUTHORIZATION STATE IF AGENT-MEDIATED
Same delegated scope, checkout total/state, merchant acceptance,
payment status, and order lifecycle?

9. TEMPORAL / ATTRIBUTION SCOPE
Same reporting rules, order maturity, return/refund horizon,
and attribution window?

10. COMPETING EXPLANATIONS
What else changed simultaneously?

11. DISCRIMINATING CHECK
What evidence would best separate the leading explanations?
```

Use `handbook/05-diagnosis-causality-and-experimentation.md` when causal attribution or experiment design becomes material.

---

## 19. Platform-module boundary

This handbook holds durable commerce reasoning. Current product-specific facts belong in platform modules.

A future commerce module should contain only what is material and time-sensitive for that platform, such as:

```text
1. scope / freshness / markets
2. local identity model
3. catalog / listing / variant object roles
4. seller input and platform-processed data
5. field semantics and visible representations
6. commercial state / eligibility
7. discovery surfaces
8. disclosed retrieval / relevance / ranking / recommendation facts
9. conversational / multimodal / agent-facing product behavior when material
10. paid vs organic boundaries
11. measurement / attribution
12. agentic / delegated transaction behavior when material
13. platform-specific anti-folklore guardrails
14. explicit UNKNOWNs
```

Expected initial modules after this handbook is validated:

```text
platforms/commerce/google-shopping.md
platforms/commerce/amazon.md
platforms/commerce/tiktok-shop.md
platforms/commerce/shopee.md
platforms/commerce/etsy.md
platforms/commerce/lazada.md
```

Do not copy platform-specific field rules into this chapter merely because several platforms expose similarly named fields.

### 19.1 Hybrid routing should load both specializations only when needed

Examples:

```text
SOCIAL POST ONLY
→ Chapter 08 + relevant social module

AMAZON LISTING / PRODUCT DISCOVERY
→ Chapter 09 + Amazon commerce module

TIKTOK SHOPPABLE VIDEO
→ Chapter 08 + Chapter 09
→ TikTok social module + TikTok Shop commerce module
```

The existence of a commerce or AI-discovery path must not make an ordinary caption task load commerce theory.

---

## 20. Core-change rule for future commerce research

Do not grow the durable model whenever a marketplace exposes a new noun or AI product feature.

Use:

```text
new commerce finding
↓
can current OBJECT + REPRESENTATION + TYPED EDGE + STATE
+ provenance + scope + transition represent it?

YES
→ keep platform-specific / derived / local role

NO
→ search for an established conceptual parent
→ construct a counterexample where current core collapses a decision-relevant distinction
→ only then consider a durable correction
```

The current cross-platform induction, including conversational/multimodal discovery, agent-facing product data, agent-mediated checkout, and delegated authority stress cases, does **not** justify adding durable primitives for:

```text
product
variant
offer
listing
catalog record
SKU
product card
PDP
anchor
voucher
shopping agent
authorization mandate
checkout session
order
AI product representation
semantic match
```

Any of these may be instantiated as an `ACTOR`, `OBJECT`, `REPRESENTATION`, typed edge, state, attribute, or implementation detail when the decision actually requires it.

---

## 21. Final commerce-environment check

Before consequential commerce work is finalized, ask only the relevant questions:

1. What identity is actually being marketed or sold: family/model, variant/configuration, individual item, listing, or another scoped object?
2. Are two independent identities genuinely present, or is the analysis inventing a canonical product separate from a platform record that does not need one?
3. Are platform IDs, seller IDs, and domain/product identity being conflated?
4. Is variant structure represented as a relation/role rather than assumed to be a universal primitive?
5. Are seller/product identity and commercial conditions separated where price, stock, shipping, promotion, or buyer eligibility can change independently?
6. Are product-descriptive facts, commercial conditions, and observational/social context distinguished where they can change interpretation?
7. Are seller input, platform-processed data, and machine-inferred facts kept distinct with provenance?
8. Are object, representation, and encounter surface distinguished where they can change the decision?
9. Is the same field being assumed to perform a human, machine/agent, retrieval, ranking, or transaction job without system-specific evidence?
10. Are eligibility, retrieval, relevance, ranking, filtering, sorting, composition, and exposure kept separate where material?
11. When current official sources conflict on field/stage behavior, are source, date, abstraction level, and unresolved UNKNOWN preserved rather than forced into one clean story?
12. Is user-selected filtering/sorting being mistaken for default ranking behavior?
13. Is a paid/sponsored-system disclosure being transferred to organic discovery without evidence?
14. Is text search being incorrectly treated as text-only retrieval, or image search as image-only item representation?
15. For AI/conversational discovery, can the material shopper requirements — use case, compatibility, constraints, preferences, dimensions/specs, budget, trade-offs, variant requirements — be resolved from truthful product facts/relations/state?
16. Is missing product evidence being repaired with the correct structured/text/image/relation carrier rather than keyword stuffing or an invented attribute?
17. Is semantic/conversational matchability being mistaken for a proven ranking boost?
18. Is product-data completeness being mistaken for guaranteed retrieval, recommendation, or exposure?
19. Is platform-local AI behavior being generalized into a universal field/ranking law?
20. Is shopper state specific enough to distinguish discovery, comparison, evaluation, configuration, and transaction needs where material?
21. Are displayed price and final payable price treated as potentially scoped/time-varying rather than intrinsic product truth?
22. In agent-mediated commerce, is shopper intent being confused with delegated authority or platform capability?
23. If authority is delegated, are its operation, amount/state constraints, scope, and expiry still valid for the current checkout state?
24. Are discovery data, authoritative checkout state, merchant-accepted order state, payment, and fulfillment being collapsed?
25. Are agent-consumable product representations being confused with the human-facing generated recommendation?
26. Is the encounter/checkout surface being confused with Merchant of Record, payment-processing, fulfillment, return, or support responsibility?
27. Are observed purchases, reviews, ratings, or engagement interpreted with exposure, availability, commercial state, provenance, attribution, and maturity context?
28. Are platform-specific facts current, scoped, and kept out of universal field folklore?
29. Is the fast path still being respected for a narrow product-communication task?
30. Is the final decision truthful, decision-relevant, and proportionate to the evidence?

The goal is not to optimize every field simultaneously, reconstruct a marketplace's hidden algorithm, or assume an agent can act merely because it can reason. The goal is to make a defensible product-discovery and commerce decision with the smallest model that preserves the identities, states, representations, mediation mechanisms, authority boundaries, and evidence scopes that can actually change action or inference — and, for AI-native discovery, to make truthful shopper requirements resolvable without pretending to know hidden model weights.
# Commerce-Environment Architecture Adversarial Audit

Reviewed: 2026-08-23

Status: **research audit, not benchmark/eval score**.

> **Post-review addendum:** an independent review of frozen head `1bcc0f653d0f14031e8209c77de51e518d66302a` later found one Etsy source-fidelity defect that this architecture audit did not expose: current official Etsy sources conflict on description/broader listing-data participation in query matching. The 8+3 architecture verdict below still survives, but this audit's `0 PARTIAL / 0 FAIL` must not be read as exhaustive evidence-fidelity proof. See `commerce-etsy-query-matching-source-conflict-correction.md` for the targeted repair.

Purpose: test whether Chapter 09 and the six commerce platform modules preserve the decision-relevant distinctions discovered during cross-platform induction **without creating a second commerce ontology, leaking platform-specific ranking claims into durable theory, or making ordinary product-copy tasks traverse the full model**.

This audit is stacked on the C3 candidate correction (`OBJECT` / `REPRESENTATION` as durable parent roles). It does not adjudicate PR #5 independently and does not claim runtime execution reliability.

## Architecture under test

Durable parent model from Chapter 08 / C3 candidate:

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

Commerce specialization:

```text
handbook/09-commerce-environments-and-product-discovery.md
```

Current commerce modules:

```text
platforms/commerce/google-shopping.md
platforms/commerce/amazon.md
platforms/commerce/tiktok-shop.md
platforms/commerce/shopee.md
platforms/commerce/etsy.md
platforms/commerce/lazada.md
```

A case fails if the current architecture must:

- invent a new durable primitive;
- collapse identities/states that can change the decision;
- force a canonical product entity where the platform case does not support one;
- convert platform evidence into an unsupported ranking/tactic claim;
- or require the deep commerce path for a narrow task that the fast path can answer.

Verdicts:

```text
LOSSLESS
all decision-relevant distinctions are representable directly

LOSSLESS / INTERNAL UNKNOWN
representation is adequate while platform internals remain explicitly unknown

PARTIAL
representation requires a consequential collapse or ambiguity

FAIL
new durable primitive or material architecture correction required
```

---

# 1. Google

## G1 — Merchant input can differ from processed Product and rendered representation

**Stress case**

A merchant submits one value, while source merging, rules, automatic improvements, validation, or another processing step changes the platform-held product state; a customer-facing surface can then render a representation that is not identical to either raw input or every stored field.

**Encoding**

```text
object                  = merchant product / variant role
source representation   = ProductInput / structured data / feed input
platform state          = processing / validation / merge / automatic improvement
machine/platform record = processed Product
human representation    = Search / Shopping / Lens / AI surface card
provenance              = merchant vs platform-derived
```

**Preserved distinction**

```text
SELLER INPUT
≠ PLATFORM-PROCESSED RECORD
≠ CUSTOMER-FACING REPRESENTATION
```

**Verdict: LOSSLESS**

## G2 — Product group and variant must remain relational

**Stress case**

A product family shares group identity while individual color/size configurations have separate sellable identities and commercial state.

**Encoding**

```text
object A       = ProductGroup / family
object B       = sellable variant
edge           = hasVariant / isVariantOf
state on B     = variant attributes + price/availability where material
representation = group vs selected-variant presentation
```

No `VARIANT` primitive is required.

**Verdict: LOSSLESS**

## G3 — Lens / AI Mode make text-query-only reasoning invalid

**Stress case**

A product can enter discovery from visual or conversational context; Shopping Graph product information can feed several surfaces without public evidence that all surfaces share one ranker.

**Encoding**

```text
shopper state        = visual / conversational / explicit search intent
discovery context    = image / conversation / text
platform state       = surface-specific mediation
machine representation = system-specific and partly unknown
representation       = Lens / Search / Shopping / AI result
```

**Preserved distinction**

```text
TEXT QUERY
≠ ONLY DISCOVERY PATH

SHARED PRODUCT DATA
≠ SHARED RANKING LAW
```

**Verdict: LOSSLESS / INTERNAL UNKNOWN**

---

# 2. Amazon

## A1 — ASIN, seller listing/SKU, offer, and PDP cannot collapse

**Stress case**

One Amazon catalog item can receive a seller listing and seller-specific offer state, while the PDP composes catalog data, selected variation, offers, reviews, fulfillment and platform-selected representations.

**Encoding**

```text
object A       = Amazon catalog item / ASIN role
object B       = seller listing / SKU role
edge           = seller listing attaches/offers catalog item
commercial state = price / condition / fulfillment / availability
platform state = Featured Offer / catalog-data selection
representation = PDP / search result / offer selector
```

**Preserved distinction**

```text
CATALOG ITEM
≠ SELLER LISTING
≠ COMMERCIAL OFFER STATE
≠ PDP REPRESENTATION
```

**Verdict: LOSSLESS**

## A2 — Searchable does not mean visible or one title field

**Stress case**

Under the July 2026 regime, Title and Item Highlights are searchable + visible while Generic Keywords can be matching data without ordinary customer-facing copy.

**Encoding**

```text
representation roles = title / Item Highlights / PDP
machine/search data   = title + Item Highlights + Generic Keywords + structured data where supported
scope                 = current marketplace/category rule
```

**Preserved distinction**

```text
TITLE
≠ ALL SEARCHABLE DATA

SEARCHABLE
≠ CUSTOMER-FACING
```

**Verdict: LOSSLESS**

## A3 — Amazon Science architecture must not become 2026 production folklore

**Stress case**

Research establishes retrieval/ranking and semantic matching architectures, but not the exact current production Store algorithm or field weights.

**Encoding**

```text
platform state      = conceptual retrieval → ranking stages where useful
evidence provenance = scientific / engineering publication
scope               = disclosed system / publication period
unknown             = exact current production implementation
```

**Verdict: LOSSLESS / INTERNAL UNKNOWN**

---

# 3. TikTok Shop

## TTS1 — Same video, different product target

**Stress case**

A posted video can receive a commerce link later; when an eligible linked product becomes unavailable it can be relinked while the video identity persists, and an original item can re-anchor after restocking.

**Encoding**

```text
object A       = video
object B       = product / shop / collection target
edge           = links-to / promotes
edge state     = active / abnormal / OOS / relinked / restored
representation = product anchor / link label
history        = target / edge-state timeline
```

**Preserved distinction**

```text
CONTENT OBJECT
≠ COMMERCE OBJECT
≠ CONTENT↔COMMERCE EDGE
≠ ANCHOR REPRESENTATION
```

**Verdict: LOSSLESS**

## TTS2 — Creator-side product recommendation is not shopper ranking

**Stress case**

A creator tool recommends products for a video using video relevance/product performance/creator context. This must not become evidence about For You or Shop Tab shopper ranking.

**Encoding**

```text
input object/context = video + creator state
candidate object     = product
platform state       = creator-side linking recommender
scope                = tool / actor / objective
unknown              = shopper-side ranker relation
```

**Verdict: LOSSLESS / INTERNAL UNKNOWN**

## TTS3 — Product attributes and sales attributes cannot collapse

**Stress case**

Whole-product attributes and SKU/variant-defining sales attributes have different scope; price/inventory can be SKU/warehouse/market state.

**Encoding**

```text
object A = product
object B = SKU / sellable configuration
edge     = hasVariant
A data   = product attributes
B data   = sales attributes
B state  = price / stock / warehouse / market
```

**Verdict: LOSSLESS**

---

# 4. Shopee

## S1 — Same posting can display different prices to different buyers

**Stress case**

Shopee VN can show estimated voucher-adjusted prices based on each buyer's available vouchers; multi-variation postings can show a lowest price, while checkout price can change as vouchers/promotions/price state change.

**Encoding**

```text
object             = seller posting / selected variation
commercial state   = seller price / variant price / promotion
platform state     = voucher program / availability
shopper state      = buyer-specific voucher eligibility
representation     = displayed price
history/time       = voucher / promotion / seller-price transition
```

**Preserved distinction**

```text
BASE PRICE
≠ VARIANT PRICE
≠ DISPLAYED PRICE
≠ CHECKOUT PRICE
```

**Verdict: LOSSLESS**

## S2 — User filter/sort must not be inferred as default ranking

**Stress case**

A shopper explicitly filters ratings/shop class/location or selects best-selling/price ordering, making visible-result correlations that need not reflect the default ranker.

**Encoding**

```text
shopper interaction = filter / sort selection
platform state      = result set under explicit constraint/order
observation         = visible results
scope               = query + filter + sort + account + time
```

**Preserved distinction**

```text
DEFAULT RANKING
≠ USER FILTER
≠ USER SORT
```

**Verdict: LOSSLESS**

## S3 — MRSE/MIEM features cannot become current ranking tactics

**Stress case**

Shopee engineering shows multimodal retrieval / image-search representations, but the exact current VN production ranking pipeline is undisclosed.

**Encoding**

```text
machine representation = disclosed multimodal retrieval embeddings
evidence provenance     = engineering system/publication
scope                   = disclosed retrieval / image-search system
unknown                 = current downstream ranker / weights
```

**Verdict: LOSSLESS / INTERNAL UNKNOWN**

---

# 5. Etsy

## E1 — Listing need not be a record for a pre-existing canonical product

**Stress case**

An Etsy listing can sell an already-existing unique item, a finite variation set, a personalized made-to-order specification, or a private custom item that will be completed for one buyer.

**Encoding**

```text
object role = listing / existing item / base specification / future item as material
edge/state  = variation / personalization / buyer-specific custom relation
history     = specification → configured / created item
```

The model does not require a hidden canonical product object.

**Preserved distinction**

```text
PLATFORM LISTING
MAY OR MAY NOT REQUIRE A SEPARATE DOMAIN-PRODUCT IDENTITY
```

**Verdict: LOSSLESS**

## E2 — Search-stage distinctions remain representable, but current official field boundaries can conflict

**Stress case**

Etsy official sources describe query matching at different abstraction levels: the legal disclosure names titles/attributes/categories/tags for the first phase, while current Seller Handbook guidance explicitly includes descriptions and broader listing information under query matching. Engineering evidence places a particular multimodal semantic-relevance model after retrieval and before/within downstream ranking integration.

**Encoding**

```text
platform state = query matching / retrieval → semantic relevance → ranking integration
field role      = stage-specific where established
provenance      = legal disclosure vs Seller Handbook vs engineering implementation
scope/date      = retained
unknown         = exact current field-to-stage production boundary / weights
```

**Preserved distinction**

```text
FIELD INFLUENCES SEARCH
≠ ONE SETTLED FIELD-TO-STAGE MAP
≠ SEMANTIC RELEVANCE
≠ DIRECT RANKING WEIGHT

OFFICIAL SOURCE CONFLICT
→ PRESERVE SOURCE + DATE + ABSTRACTION + UNKNOWN
```

**Verdict: LOSSLESS / INTERNAL UNKNOWN**

## E3 — Inferred attributes / planned product summaries must preserve provenance and deployment state

**Stress case**

Etsy can infer structured attributes from unstructured listing evidence; a May 2026 research system generates internal product summaries but describes online production experimentation as planned/near-term rather than universal deployment.

**Encoding**

```text
source data           = seller text/images/attributes
machine representation = inferred attribute / internal summary
provenance            = platform inference
platform state        = deployed experience vs planned experiment
history/time          = publication / rollout state
```

**Verdict: LOSSLESS**

---

# 6. Lazada

## LZ1 — Global product, local item, SellerSku, SkuId, and country scope cannot collapse

**Stress case**

Cross-border tooling can target multiple ventures, while item IDs are country-scoped, seller SKUs are shop-scoped, Lazada SKU IDs are platform-created, and local category/brand taxonomies can differ.

**Encoding**

```text
object roles = global management object / local item / SKU
identifiers  = item_id / SellerSku / SkuId
scope        = country / venture / seller
relations    = global→local / item→SKU
```

**Preserved distinction**

```text
GLOBAL MANAGEMENT IDENTITY
≠ LOCAL ITEM IDENTITY
≠ SELLER SKU IDENTITY
≠ PLATFORM SKU IDENTITY
```

**Verdict: LOSSLESS**

## LZ2 — `is_key_prop` product score is not established organic ranking

**Stress case**

Open Platform says filling key attributes can improve an item/product score/rating, but does not establish that score as organic Search rank or disclose downstream weight.

**Encoding**

```text
product data          = key attribute
platform state        = documented item/product score
provenance            = integration documentation
unknown               = relationship to organic Search/Recommendation
```

**Preserved distinction**

```text
PLATFORM DATA-QUALITY / ITEM SCORE
≠ ESTABLISHED ORGANIC RANKING SCORE
```

**Verdict: LOSSLESS / INTERNAL UNKNOWN**

## LZ3 — AutoPKG and Sponsored ranking must not leak into manual organic tactics

**Stress case**

AutoPKG-derived attributes improve GMV in tested platform Search/Recommendation applications, while Sponsored Discovery separately discloses bid/keyword/product-quality factors. Neither establishes a manual seller field's organic ranking effect.

**Encoding**

```text
machine-derived state = AutoPKG product-attribute knowledge
system scope          = tested Search / Recommendation application
paid platform state   = Sponsored Discovery / Sponsored Max
provenance            = engineering experiment vs paid-product documentation
unknown               = organic ranker / manual-field causal effect
```

**Preserved distinction**

```text
PLATFORM-DERIVED ATTRIBUTE EFFECT
≠ MANUAL SELLER FIELD TACTIC

SPONSORED RANKING FACTOR
≠ ORGANIC RANKING FACTOR
```

**Verdict: LOSSLESS / INTERNAL UNKNOWN**

---

# 7. Cross-module architecture attacks

## X1 — Does commerce introduce a ninth durable primitive?

Tested candidates:

```text
product
variant
offer
listing
catalog record
SKU
voucher
product card
PDP
anchor
```

Every tested case is representable as an `OBJECT` role, `REPRESENTATION`, typed edge, state, attribute, or implementation detail with provenance/scope/history when material.

**Verdict: NO NEW DURABLE PRIMITIVE REQUIRED**

## X2 — Does generic `OBJECT` erase actor semantics?

Chapter 09 explicitly allows one real-world entity to occupy different analytical roles. A shop/account remains `ACTOR / SOURCE` when authority/action/accountability matters and can also be an `OBJECT` when independently targeted/recommended.

**Verdict: LOSSLESS**

## X3 — Does Chapter 09 force a canonical product identity?

No. Chapter 09 explicitly rejects both universal assumptions:

```text
PLATFORM RECORD = DOMAIN PRODUCT
```

and:

```text
PLATFORM RECORD MUST BE DIFFERENT FROM DOMAIN PRODUCT
```

Etsy is the adversarial reference case.

**Verdict: LOSSLESS**

## X4 — Does “product information” collapse product facts, commercial conditions, and observations?

No. Chapter 09 separates:

```text
PRODUCT-DESCRIPTIVE DATA
COMMERCIAL CONTEXT
OBSERVATIONAL / SOCIAL CONTEXT
```

and tracks role transitions such as review observation → displayed trust context → machine evidence.

**Verdict: LOSSLESS**

## X5 — Does the specialization over-route simple copy tasks?

Chapter 09 has an explicit fast path for narrow title/highlight/description/image work, and every platform module includes a platform-local fast path. The deep graph is representational capacity, not mandatory workload.

The runtime controller had **not yet been changed when this historical audit was first frozen**, so this case originally recorded runtime-untested. Later routing smoke closed that gate separately.

**Verdict: ARCHITECTURALLY SUPPORTED / HISTORICALLY RUNTIME UNTESTED**

---

# 8. Scorecard

The original frozen scorecard was:

| Source | Cases | LOSSLESS | LOSSLESS / INTERNAL UNKNOWN | Runtime untested | PARTIAL | FAIL |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Google | 3 | 2 | 1 | 0 | 0 | 0 |
| Amazon | 3 | 2 | 1 | 0 | 0 | 0 |
| TikTok Shop | 3 | 2 | 1 | 0 | 0 | 0 |
| Shopee | 3 | 2 | 1 | 0 | 0 | 0 |
| Etsy | 3 | 2 | 1 | 0 | 0 | 0 |
| Lazada | 3 | 1 | 2 | 0 | 0 | 0 |
| Cross-module | 5 | 4 | 0 | 1 | 0 | 0 |
| **Total** | **23** | **15** | **7** | **1** | **0** | **0** |

Post-review interpretation:

- the **architecture/cardinality** conclusions remain intact;
- Etsy E2 must be read as `LOSSLESS / INTERNAL UNKNOWN` with explicit official-source conflict, not as proof of one settled initial-matching field map;
- later routing smoke separately closes the historical runtime-untested gate;
- the existence of a later source-fidelity correction demonstrates that zero PARTIAL/FAIL in this audit is not exhaustive proof of evidence correctness.

No case required:

- a commerce-specific durable primitive;
- a second ontology;
- a universal product/listing separation;
- a ranking claim beyond the evidence;
- or a platform-specific field rule in Chapter 08.

---

# 9. Review findings and corrections incorporated across the research sequence

The adversarial process found and corrected material problems rather than treating the first draft as authoritative:

1. **Over-strong product/listing separation.** The draft initially risked treating `domain product ≠ platform record` as universal. Etsy falsified that formulation. Chapter 09 now asks whether two independently relevant identities actually exist.
2. **Actor/object disjointness.** A shop/account can be an actor and a recommendation target. Chapter 09 now treats these as analytical roles rather than mutually exclusive entity classes.
3. **Over-broad “product information.”** Reviews, ratings, seller/shipping state and product-descriptive facts were separated into descriptive, commercial, and observational/social context.
4. **Etsy query-matching source conflict.** Later independent review found that the frozen evidence layer had treated the legal four-field query-matching enumeration too aggressively. The correction now preserves the legal disclosure, Seller Handbook description/broader-listing query-matching claims, and the scoped post-retrieval semantic-model evidence without forcing false consistency.

---

# 10. Architecture verdict

```text
CHAPTER 09 COMMERCE SPECIALIZATION
SURVIVES REPRESENTATIONAL / EVIDENCE-BOUNDARY ADVERSARIAL REVIEW

6 / 6 PLATFORM MODULES
FIT THE SAME 8 + 3 PARENT GRAMMAR

0 NEW DURABLE PRIMITIVES
0 SECOND COMMERCE ONTOLOGIES

ETSY SOURCE-FIDELITY DEFECT
TARGETED CORRECTION APPLIED

RUNTIME ROUTING
VALIDATED SEPARATELY BY ROUTING SMOKE
```

**Current gate recommendation: RETURN THE CORRECTED PR #7 HEAD TO INDEPENDENT ADVERSARIAL REVIEW.**

This audit does not claim platform tactics are causally effective, that public documentation fully exposes production systems, that all official sources are internally consistent, or that the skill is benchmark-ready.

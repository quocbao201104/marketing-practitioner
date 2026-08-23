# Commerce AI-Native / Conversational Product Discovery — Targeted Practitioner Pass

Reviewed: 2026-08-23

Status: **targeted research/adversarial check, not a benchmark**.

Purpose: test whether current AI-native, semantic, conversational, multimodal, and agent-facing product-discovery evidence supports a durable seller-side practitioner rule beyond classic keyword/listing guidance, without reopening the commerce ontology or inventing hidden ranking mechanics.

This pass is intentionally scoped to:

- Shopee App in ChatGPT / Shopee conversational discovery;
- Google conversational shopping / Merchant conversational attributes / AI performance insights;
- ChatGPT product discovery / Shopping Research / ACP product feed where relevant;
- existing Shopee multimodal retrieval/image-search evidence;
- existing Chapter 09 `OBJECT / REPRESENTATION / TYPED EDGE / STATE + provenance/scope/history` grammar.

It does **not** add a new platform module, a new durable primitive, or an `AI commerce` ontology.

---

## 1. Evidence-supported practitioner rule

The targeted evidence supports:

```text
OPTIMIZE FOR RESOLVABILITY
≠ OPTIMIZE FOR IMAGINED MODEL WEIGHTS
```

`Resolvability` means that a discovery system has truthful, sufficiently precise product evidence with which to answer a material shopper requirement such as:

```text
what is the product?
which variant?
what dimensions / specifications?
compatible with what, when actually established?
which hard constraints / limitations apply?
which preferences does it truthfully satisfy?
what current price / availability / shipping state applies?
what material trade-off exists?
which accessory / substitute / spare-part relation is declared?
```

The seller-side operation is:

```text
SHOPPER REQUIREMENT
↓
TRUE PRODUCT FACT / RELATION / STATE NEEDED TO RESOLVE IT
↓
VERIFY SOURCE / CLAIM BOUNDARY
↓
PLATFORM-SUPPORTED CARRIER WITH THE RIGHT JOB
↓
ACCURATE + CURRENT REPRESENTATION
```

This is representation/product-data discipline, not a ranking formula.

---

## 2. Supporting evidence classes

### Google

Current Merchant Center material supports:

- conversational attributes for AI/conversational product understanding;
- longer/more complex AI shopping queries;
- product-feature/specification/review/pricing-comparison query intents;
- structured `product_detail` for technical/verifiable facts;
- `product_highlight` for concise benefits/features with explicit anti-keyword/anti-SEO-keyword guidance;
- product terms / missing popular attributes as data-quality opportunities rather than disclosed rank weights.

### Shopee

Current Shopee/Sea evidence supports:

- natural conversational requests through Shopee App in ChatGPT;
- product recommendation cards;
- optional account-linked personalization/history/preferences;
- conversation-context handoff;
- product-detail / checkout continuation on Shopee.

Existing Shopee engineering evidence separately establishes that:

- text-query retrieval can use text + image + user multimodal evidence;
- image search can use text + multiple images.

It does **not** disclose the exact field/model pipeline of Shopee App in ChatGPT.

### ChatGPT / ACP

Current OpenAI/ACP evidence supports:

- natural-language product discovery involving preferences, budget, multiple constraints and trade-offs;
- follow-up/refinement on dimensions such as brand, size, performance, comfort, style, price and other product requirements;
- visual product discovery;
- structured merchant product feeds used for discovery/indexing/retrieval-ranking systems;
- product/variant/commercial data represented separately from later checkout truth;
- no obligation for OpenAI to surface submitted merchant content.

Therefore complete/rich product data can improve representability and reduce mismatch while remaining insufficient to guarantee selection/exposure.

---

## 3. Durable distinctions that survived

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
STRUCTURED FACT
≠ NATURAL-LANGUAGE EXPLANATION
```

```text
MULTIMODAL EVIDENCE
≠ DECORATIVE IMAGE OPTIMIZATION TACTIC
```

```text
MERCHANT-DECLARED PRODUCT RELATION
≠ PLATFORM-INFERRED RELATION
≠ OBSERVED BEHAVIORAL RELATION
```

```text
POPULAR / INFERABLE USE CASE
≠ SELLER-AUTHORIZED PRODUCT CLAIM
```

---

# 4. Adversarial checks

## A1 — Keyword-stuffing folklore

**Prompt / claim under attack**

> AI shoppers may ask for a “travel portable blender.” Should the seller repeat “travel portable travel blender portable” across title, description, highlights and attributes so conversational AI matches it more often?

**Attack**

The evidence supports natural-language / semantic / multi-constraint discovery, but no source establishes keyword density as the causal mechanism or a ranking weight. Google explicitly tells merchants not to use product highlights as search-term / SEO-keyword lists.

If the product truly has travel-relevant properties, represent the actual properties: dimensions, capacity, charging method, weight, allowed use context, or another verified fact in the appropriate carrier. Do not manufacture/repeat phrase variants.

**Preserved distinction**

```text
MACHINE LEGIBILITY
≠ KEYWORD DENSITY
```

**Verdict: PASS — REJECT KEYWORD-STUFFING TACTIC**

---

## A2 — Invented attributes for broader AI matching

**Prompt / claim under attack**

> Shoppers often ask “works with MacBook Pro.” Compatibility is not verified. Should the seller mark the accessory as MacBook Pro compatible to appear in more AI recommendations?

**Attack**

No. The requested compatibility is a product claim. Broader semantic coverage does not relax source fidelity. If model/version compatibility is not established, preserve UNKNOWN or obtain authoritative evidence before adding the claim.

The same rule applies to unsupported “ideal for travel,” “child safe,” “professional grade,” “fits small spaces,” or other inferred use-case claims.

**Preserved distinction**

```text
POPULAR / INFERABLE USE CASE
≠ VERIFIED PRODUCT FACT / CLAIM
```

**Verdict: PASS — REJECT INVENTED ATTRIBUTE / CLAIM**

---

## A3 — Semantic relevance mistaken for ranking

**Prompt / claim under attack**

> A structured specification or multimodal representation makes the product semantically easier to match. Does that mean the product gets an organic ranking boost?

**Attack**

Not established. Google product-data/conversational evidence supports product understanding/matchability but does not expose deterministic weights. Shopee MRSE/MIEM are scoped retrieval/image-representation systems and do not establish the current complete ranker or Shopee-ChatGPT pipeline. Etsy independently demonstrates why relevance and ranking must remain distinct stages/claims.

**Preserved distinction**

```text
SEMANTIC MATCHABILITY
≠ PROVEN RANKING BOOST
```

**Verdict: PASS / INTERNAL UNKNOWN — RANKING EFFECT UNDISCLOSED**

---

## A4 — Complete data mistaken for guaranteed recommendation

**Prompt / claim under attack**

> If every product field is complete and the ACP feed is perfect, will ChatGPT recommend the product? Likewise, does complete Google/Shopee product data guarantee AI exposure?

**Attack**

No. OpenAI Merchant Feed Terms explicitly do not require OpenAI to use or surface submitted merchant content. Google data completeness / conversational fields likewise do not establish guaranteed candidate retrieval/ranking/exposure. Shopee's current conversational integration does not expose a completeness threshold or recommendation guarantee.

Completeness can reduce unresolved product facts and stale/mismatched representation; it cannot be promoted into guaranteed selection.

**Preserved distinction**

```text
PRODUCT FACT COMPLETENESS
≠ GUARANTEED RETRIEVAL / RECOMMENDATION / EXPOSURE
```

**Verdict: PASS — REJECT GUARANTEE**

---

## A5 — Platform-local AI behavior generalized universally

**Prompt / claim under attack**

> Google has `question_and_answer`, `related_product`, and other conversational attributes. Should every marketplace listing use equivalent fields, and should Shopee sellers assume those field semantics drive Shopee App in ChatGPT?

**Attack**

No. Google exposes those fields locally. Shopee App in ChatGPT official sources establish conversational requests/context and optional personalization, but not Google's field model or Shopee's exact seller-field mapping. ACP exposes its own feed contract. Similar practitioner goals do not imply identical carriers or algorithms.

Use the durable rule at the job level:

```text
REQUIREMENT
→ TRUE FACT / RELATION / STATE
→ PLATFORM-SUPPORTED CARRIER
```

Then instantiate the actual carrier separately per platform.

**Preserved distinction**

```text
DURABLE PRACTITIONER JOB
≠ UNIVERSAL PLATFORM FIELD / MODEL IMPLEMENTATION
```

**Verdict: PASS — REJECT CROSS-PLATFORM FIELD LEAKAGE**

---

# 5. Query-family stress matrix

| Shopper request dimension | Durable representation response | New primitive required? |
| --- | --- | --- |
| Use case | truthful product property/context in supported text/structured carrier; do not invent use claim | No |
| Compatibility | verified compatibility fact / model relation / supporting document where supported | No |
| Hard constraint | structured spec, limitation, current commercial state, or explicit unknown | No |
| Preference | descriptive/visual/structured evidence where factual; shopper state remains separate | No |
| Dimensions/specs | structured technical fact + natural-language context where needed | No |
| Price/budget | current commercial state, scoped by market/time/buyer where material | No |
| Trade-off | truthful evaluation context / limitation; not fabricated persuasion | No |
| Variant requirement | existing variant/configuration object role + relation/state | No |
| Related accessory/substitute | typed relation with merchant-declared provenance where supported | No |
| Visual similarity/property | image/multimodal representation + source provenance | No |

All tested request families remain representable by the existing 8+3 grammar.

---

# 6. What remains UNKNOWN

Preserve as UNKNOWN unless a current system-specific source discloses otherwise:

- exact seller fields / embeddings / transformations consumed by Shopee App in ChatGPT;
- exact Shopee App candidate generation, retrieval, relevance, ranking, reranking, or recommendation weights;
- exact weighting of Shopee account history/preferences versus current conversational context;
- whether Shopee MRSE/MIEM representations are reused by the ChatGPT integration;
- exact Google AI Mode / Gemini query decomposition, candidate retrieval, field-to-stage participation, semantic model, ranking/reranking weights, and representation composition;
- exact cross-surface use of Google's conversational attributes;
- exact ChatGPT candidate generation, retrieval/ranking features, transformations, prompts, model weights, merchant-selection logic beyond disclosed high-level behavior, and use of merchant vs third-party sources in a particular result;
- exact causal effect of adding one accurate field/image/relation on organic or AI-mediated exposure;
- portability of any platform-local field behavior to another marketplace or AI assistant.

---

# 7. Architecture verdict

```text
NEW DURABLE PRACTITIONER RULE
YES — OPTIMIZE FOR RESOLVABILITY

NEW DURABLE PRIMITIVE
NO

SEPARATE AI-COMMERCE ONTOLOGY
NO

ROUTER CHANGE
NO

PLATFORM MODULE ADDED
NO

CHAPTER 09 CORE CORRECTION
NO — TARGETED STRATEGY / REPRESENTATION EXTENSION ONLY
```

The existing model already has the necessary slots:

```text
shopper intent / constraints
→ AUDIENCE STATE / discovery context

product / variant
→ OBJECT

structured/text/image/feed data
→ REPRESENTATION / attributes / state with provenance

compatibility / related-product relation
→ TYPED EDGE / fact with scope

price / availability / shipping
→ COMMERCIAL STATE

agent-facing product record
→ REPRESENTATION

retrieval / semantic matching / ranking
→ PLATFORM / MEDIATION STATE
```

No decision-relevant counterexample forced a ninth durable thing or an `AI product discovery` ontology.

---

# 8. Gate recommendation

**TARGETED PASS COMPLETE — STOP.**

Return PR #7 to independent review after this patch. Do not broaden the research into more AI shopping platforms, more marketplace coverage, or speculative model-weight optimization unless a concrete reviewer/runtime case cannot be represented or answered faithfully with the current evidence discipline.

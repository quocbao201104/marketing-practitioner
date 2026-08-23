# Agentic Commerce Frontier Evidence Ledger

Cross-platform source identifiers for agent-mediated discovery, delegated authority, checkout state, order state, and agent-facing product representations.

Reviewed 2026-08-23. Agentic-commerce protocols and product surfaces are moving quickly; re-check consequential execution and authorization behavior before use.

These sources stress-test the existing Chapter 09 commerce specialization. They do **not** define a second agentic-commerce ontology.

## [AC01] Universal Commerce Protocol — Checkout capability

Universal Commerce Protocol (UCP). **Checkout Capability.** Current protocol documentation reviewed 2026-08-23; current public protocol releases include v2026-04-08.

Direct source: `https://ucp.dev/specification/checkout/`

Use: UCP checkout lets platforms facilitate checkout sessions while the business remains Merchant of Record. Standard checkout must be finalized manually by the user through a trusted UI unless the AP2 Mandates extension is supported. Payment handlers and fulfillment are modeled as scoped capabilities/extensions rather than collapsed into product discovery.

Boundary: protocol capability does not itself prove that a particular platform, merchant, market, or user has enabled autonomous execution.

## [AC02] Universal Commerce Protocol — AP2 Mandates extension

Universal Commerce Protocol (UCP). **AP2 Mandates Extension.** Reviewed 2026-08-23.

Direct source: `https://ucp.dev/specification/ap2-mandates/`

Use: when negotiated, AP2 Mandates cryptographically bind checkout terms and require platform-provided signed proofs that the user authorized the specific checkout state and funds transfer. This is strong evidence that user intent, platform capability, delegated authority, and a particular transaction effect are distinct states.

Boundary: AP2 support is negotiated capability/state, not a universal default. Do not infer autonomous authority from the existence of a shopping agent or checkout API.

## [AC03] Universal Commerce Protocol — Order capability

Universal Commerce Protocol (UCP). **Order Capability.** Reviewed 2026-08-23; current public documentation describes order as a current-state snapshot returned by the business, with fulfillment events and post-order adjustments.

Direct source: `https://ucp.dev/specification/order/`

Use: orders represent confirmed transactions resulting from successful checkout submission. The business returns the authoritative latest order state; order lifecycle can include edits, fulfillment events, returns, refunds, credits, disputes, and cancellations.

Boundary: checkout state and order state are related but not interchangeable. An order can continue changing after checkout completion.

## [AC04] Agentic Commerce Protocol — Product Feed

Agentic Commerce Protocol (ACP). **Product Feed Specification.** Reviewed 2026-08-23.

Direct source: `https://agentic-commerce-protocol.com/docs/commerce/specs/feed`

Use: merchants provide structured product data that OpenAI ingests, validates, and indexes for retrieval/ranking in ChatGPT shopping/search experiences. Feed data is an authoritative merchant input for product discovery data within the integration. The feed includes required core product identity/description/image/price/availability data and supports variant, brand/category/product-type, additional-image, rating/review, shipping, seller, and other structured metadata depending on the item and integration.

Boundary: a discovery/index snapshot is not automatically the authoritative transaction state at a later checkout time. Price, availability, shipping, discounts, or other conditions can change. Presence or completeness in a feed does not guarantee that OpenAI will surface the merchant/product, nor does the feed specification disclose exact retrieval/ranking weights.

## [AC05] Agentic Commerce Protocol — Agentic Checkout

Agentic Commerce Protocol (ACP). **Agentic Checkout Specification.** Reviewed 2026-08-23.

Direct source: `https://agentic-commerce-protocol.com/docs/commerce/specs/checkout`

Use: checkout creation/update responses must return a rich authoritative cart state including items, pricing, taxes/fees, shipping, discounts, totals, messages/status; completion confirms order creation. Merchants continue to run orders, payments, and compliance on their commerce stack and publish order lifecycle events.

Boundary: the presence of a checkout session or request does not establish merchant acceptance, successful payment, fulfillment, or final order state.

## [AC06] Shopify — Global Catalog and Storefront Catalog for AI agents

Shopify Developer Documentation. **About Catalogs; Global Catalog MCP; Storefront Catalog MCP.** Reviewed 2026-08-23; current interfaces implement UCP Catalog capability.

Direct sources:

- `https://shopify.dev/docs/agents/catalog`
- `https://shopify.dev/docs/agents/catalog/global-catalog`
- `https://shopify.dev/docs/agents/catalog/storefront-catalog`

Use: Shopify exposes product-discovery interfaces directly to AI agents. Global Catalog searches across Shopify merchants; Storefront Catalog scopes discovery to one merchant. Catalog requests can include buyer context such as country, region, postal code, language, currency, and intent, and return structured products/variants/offers for agent evaluation.

Boundary: agent-consumable catalog representations are not identical to the human-facing recommendation or checkout representation an agent later generates/presents.

## [AC07] OpenAI — ChatGPT product discovery and shopping research

OpenAI. **Powering Product Discovery in ChatGPT; Using shopping research in ChatGPT; Shopping with ChatGPT Search; OpenAI Merchant Feed Terms of Service.** Current product/help/policy material reviewed 2026-08-23.

Direct sources:

- `https://openai.com/index/powering-product-discovery-in-chatgpt/`
- `https://help.openai.com/en/articles/12911370-using-shopping-research-in-chatgpt`
- `https://help.openai.com/en/articles/11128490-shopping-with-chatgpt-search`
- `https://openai.com/policies/merchant-feed-terms-of-service/`

Use: ChatGPT shopping/product discovery is explicitly designed around natural-language intent, preferences, budget, comparisons, trade-offs, and multiple constraints. Shopping Research can ask follow-up questions about attributes such as preferred brands, size ranges, performance, comfort, style, or price; it can compare products on price, size, features, reviews, constraints, and trade-offs, and may use merchant data provided through ACP together with public and other retail sources. ChatGPT shopping also supports visual product discovery/visual comparison. Product results are selected for perceived relevance to the user's query/context; ChatGPT can generate simplified human-facing titles/descriptions from source data rather than reproducing merchant copy verbatim.

Merchant-facing implication supported by the product/feed evidence: precise, current, truthful product facts and variant/commercial state can make a product more accurately and completely representable to the system. This supports **resolvability of shopper constraints**, not a claim about keyword density or a deterministic rank formula.

Boundaries:

- exact candidate-generation, semantic matching, retrieval/ranking weights, model prompts, feature transformations, and recommendation objectives remain undisclosed/time-sensitive;
- OpenAI Merchant Feed Terms explicitly do not require OpenAI to use or surface submitted Merchant Content;
- complete or richly structured data therefore does not guarantee retrieval, recommendation, rank, or exposure;
- product results can use non-merchant sources, so a merchant feed is not necessarily the only evidence considered;
- a model-generated product title/description is a human-facing representation, not proof that the seller's original wording was shown unchanged.

## Evidence-use rules

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
DISCOVERY / INDEX STATE @ t0
≠ AUTHORITATIVE CHECKOUT STATE @ t1
≠ AUTHORITATIVE ORDER STATE @ t2
```

```text
CHECKOUT REQUEST / SESSION
≠ MERCHANT-ACCEPTED ORDER
≠ PAYMENT / FULFILLMENT COMPLETION
```

```text
AGENT-CONSUMABLE REPRESENTATION
≠ HUMAN-FACING GENERATED REPRESENTATION
```

```text
MACHINE LEGIBILITY / PRODUCT-DATA COMPLETENESS
≠ KEYWORD DENSITY
≠ GUARANTEED RETRIEVAL / RECOMMENDATION / RANK
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
OPTIMIZE FOR RESOLVABILITY
≠ OPTIMIZE FOR IMAGINED MODEL WEIGHTS
```

```text
ENCOUNTER / CHECKOUT SURFACE
≠ MERCHANT OF RECORD
≠ PAYMENT-PROCESSING ROLE
≠ FULFILLMENT / POST-PURCHASE RESPONSIBILITY
```

```text
PROTOCOL SUPPORT
≠ FEATURE ENABLED FOR EVERY MARKET / MERCHANT / USER
```

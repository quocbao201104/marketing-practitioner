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

Use: merchants provide structured product data that OpenAI ingests, validates, and indexes for retrieval/ranking in ChatGPT shopping/search experiences. Feed data is an authoritative merchant input for product discovery data within the integration.

Boundary: a discovery/index snapshot is not automatically the authoritative transaction state at a later checkout time. Price, availability, shipping, discounts, or other conditions can change.

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
ENCOUNTER / CHECKOUT SURFACE
≠ MERCHANT OF RECORD
≠ PAYMENT-PROCESSING ROLE
≠ FULFILLMENT / POST-PURCHASE RESPONSIBILITY
```

```text
PROTOCOL SUPPORT
≠ FEATURE ENABLED FOR EVERY MARKET / MERCHANT / USER
```

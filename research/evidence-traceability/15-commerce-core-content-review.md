# Commerce and Product Discovery: Shared Model Review

Date: 2026-09-07. Chapter 09 remains unchanged from `362ac88`. Existing Chapter 01–08 corrections, bibliography additions and research artifacts were preserved.

Status: bounded shared-model review completed; one local clarification candidate. This is not a complete verification of every platform example, commerce protocol or cited study.

## Scope and conclusion

Read the shared reasoning in [Chapter 09](../../skills/marketing-practitioner/handbook/09-commerce-environments-and-product-discovery.md) §§1–15 and cross-checked §§16–21 for fast-path and ownership constraints. Inspected relevant routing guidance and actual retrieved sections. External source checks focused on identity, variants, source processing and representation. Individual marketplace facts and the full agentic-commerce protocol landscape remain outside the completed audit.

The chapter preserves useful distinctions between product/configuration identity, seller and platform records, commercial conditions, shopper-facing representations, observations and transaction stages. It explicitly avoids universal entity classes, hidden ranking formulas, automatic authority from capability, and guaranteed exposure from complete data. No new ontology or controller changes are justified.

The remaining actionable gap is what to do when consequential product sources disagree. The provenance section identifies source types and limits, but does not operationalize reconciliation before turning mixed material into a final claim. Existing truthfulness rules mitigate the issue; the smallest correction belongs beside fact provenance.

## Source access and scope

| Existing reference | Material inspected on 2026-09-07 | Limit |
|---|---|---|
| C01: GoodRelations | [Author-maintained language reference](https://www.heppnetz.de/ontologies/goodrelations/v1.html), selected product/model/variant and related-product definitions | The original 2008 paper URL returned a verification page. The language reference supports related technical vocabulary, not proof of the original paper's complete contents or marketing efficacy. |
| C02: Schema.org | [ProductGroup](https://schema.org/ProductGroup), type description and variant relations | The page identifies itself as a development version. Its vocabulary is not a universal implemented marketplace schema. |
| C02: Google Search Central | [Product variant structured data](https://developers.google.com/search/docs/appearance/structured-data/product-variants), examples and variant preselection guidance | Current Google-specific implementation guidance; no ranking weights or universal format rule inferred. |
| C03: Google Merchant API | [ProductInput reference](https://developers.google.com/merchant/api/reference/rest/products_v1/accounts.productInputs), resource description | Confirms submitted input and processed product differ; not an audit of all Merchant processing, reconciliation or display behavior. |
| AC01/AC03: UCP | Attempted [checkout](https://ucp.dev/specification/checkout/) and [order](https://ucp.dev/specification/order/) locators | Tool returned redirect-only pages with no substantive text. Current protocol details remain unverified; not declared wrong or obsolete. |

Schema.org distinguishes shared group properties from varying products. Google's examples associate each variant with its own image, price and availability, and its guidance requires variant preselection to show the appropriate state. Merchant API documents that inputs, rules and supplemental data combine into a processed product. These sources support the chapter's narrow identity/representation distinctions; they do not validate every seller claim or the entire practitioner model.

C04–C15, AC02 and AC04–AC07 were inspected as local ledger references, not externally verified in full. Current claims about Etsy stages, Shopee retrieval, TikTok relinking, Lazada inference and AI commerce must not be described as freshly validated by this pass. Shared recommendation/causal sources retain the limits of earlier reviews.

## Shared-model assessment

| Area | Assessment | Disposition |
|---|---|---|
| §§1–3: identities and roles | Distinguishes domain identity, record identity and scoped IDs without requiring disjoint universal classes | Retain |
| §3.4: variants and bundles | Keeps configuration distinct from quantity, with a commercial-design dependency when configuration is unresolved | Retain |
| §4: conditions of sale | Separates product identity, offer/state, buyer eligibility and time; offer identity is explicit when independently relevant | Retain |
| §§5.1–5.4: data classes and processing | Product description, commercial conditions and feedback are distinguished; processing does not equal truth | Retain |
| §5.5: fact provenance | Origin and supported scope are explicit; consequential source disagreement lacks a local resolution rule | Clarify under P1 |
| §6: representations | Multi-object cards and different human/machine roles are adequately represented | Retain |
| §§7–9: discovery | Stages are conditional, platform-specific and separate from ranking-weight claims | Retain; current examples not comprehensively verified |
| §10: content-commerce and delegated authority | Preserves target/link history, authorization scope and separate transaction states | Retain as design; protocol-specific facts remain pending validation |
| §§11–12: shopper states and observations | Avoids universal funnel, purchase-as-pure-preference and collapsed order/payment/return stages | Retain |
| §§13–14: information allocation | Truthful requirement resolution and supported carrier selection give positive execution guidance, not just cautions | Retain; specialization claims need their own source review |
| §15 and runtime cross-check | Invariants are conditional; narrow copy tasks can bypass the full model | Retain |

## P1 — Reconcile conflicting product sources at the claim's scope

Priority: first and only promoted finding. Location: §5.5, `commerce.fact-provenance`, also contained by `commerce.data-classes`.

Constructed task: write a product card from a manufacturer specification, a seller title and an image. The specification states one capacity, the title another, and the image may show an older package or a different variant. The identity relationship is not yet established.

Current representation: a list of possible sources plus an instruction to preserve origin/confidence and what each source supports for the relevant product/variant. This correctly says that an origin label alone does not establish verification. Broader source-conflict handling later in the chapter addresses official claims about search stages, not product-data discrepancies.

Gap: the agent is not told how to distinguish a genuine factual contradiction from differences in variant, revision, package quantity, seller scope, time or measurement convention. Nor is it explicitly told not to resolve the discrepancy merely by selecting the most favorable value or a globally preferred source category.

Decision consequence: combine incompatible attributes into a fictional sellable configuration, publish the wrong specification, or discard an applicable source because an authoritative but different-version document appears to outrank it. These are constructed reasoning counterexamples, not observed failures.

Smallest correction candidate: when disagreement can change the claim or purchase decision, establish whether the sources refer to the same product/configuration and material conditions. Use direct applicability and evidence quality to resolve the particular claim; do not let source format, recency or authority label alone substitute for that match. If unresolved, retain the discrepancy, qualify or withhold the affected claim, and seek only the decisive missing evidence. Continue unaffected work; do not turn every supplied title rewrite into a catalog audit.

This is a project-synthesis clarification of existing truthfulness, identity and provenance rules. The inspected [variant guidance](https://developers.google.com/search/docs/appearance/structured-data/product-variants) and [input/processed-record distinction](https://developers.google.com/merchant/api/reference/rest/products_v1/accounts.productInputs) demonstrate why scope and representation matter, but do not provide a universal conflict-resolution algorithm.

## Constructed cases already supported without new rules

- A group has cheap and expensive variants: §§3–4 retain variant and commercial scope; a group-level starting price is not the final price of every configuration.
- A two-item bundle is sold as one unit: §3.4 already separates bundle composition and order quantity.
- A product has ratings and many sales: §5.3 and §12 keep those observations from becoming intrinsic specification facts.
- A product photo includes a prop: §13.4.3 allows visual evidence only for supported visible properties, while §§5.4–5.5 and the core constrain claims about included items. Do not infer commercial inclusion from mere visual presence.
- A feed update has been submitted: C03 and §5.4 separate input from processed state; submission alone does not establish the displayed outcome.
- A shopper asks for compatibility: §13.4.1 explicitly rejects inventing compatibility to satisfy a popular query.
- A product has a complete record but little exposure: §8.4 and §13.4.4 explicitly reject guaranteed visibility from completeness.
- A shopping agent submits checkout: §10.3.2 distinguishes a request, an accepted order, payment and fulfillment. The generic distinction can be reviewed without certifying a protocol implementation.
- Sales fall after a price or stock change: §18 examines commercial and observation state before recommending a title rewrite, using Chapter 05 when causal inference is material.

These cases do not prove behavioral success. They show why additional generic rules would duplicate available guidance rather than repair a demonstrated new gap.

## Retrieval inspection

Inspected actual output from the existing loader:

| Route | Lines | Relevant content |
|---|---:|---|
| commerce.fact-provenance | 18 | Source categories and scope/verification qualification |
| commerce.data-classes | 117 | Description/commercial/observation classes, processing and provenance |
| commerce.identity | 149 | Scoped identities, variants and bundle distinction |
| commerce.commercial-state | 114 | Conditions, offer role and buyer/time scope |
| commerce.resolvability | 164 | Supported requirements, carriers and non-guarantees |
| commerce.agentic | 159 | Delegated authority and transaction-state distinctions |
| commerce.observation-interpretation | 118 | Event stages, maturity, exposure and causal limits |

P1 is not a missing selector or broken extraction. Both the narrow provenance route and parent data-class route would receive a local addition. Preserve route IDs and headings. No new search or storage mechanism is needed.

## Verification and limits

Only this report was added. Checked relative links, UTF-8/CRLF text integrity, and worktree state. Existing edits and research artifacts remain intact. No live trials, historical-pilot comparisons, commits or pushes.

The completed scope is shared conceptual coherence with selected source checks, not certification of all Chapter 09 claims. A later audit can examine operational chains and platform-local facts in bounded groups. If implementing P1, keep it in §5.5 and compare the affected excerpts before and after without expanding the model.

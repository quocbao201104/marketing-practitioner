# Commerce Environments: Operational Paths Review

Date: 2026-09-07. Reviewed the current worktree after the P1 correction recorded in [the provenance closure](16-commerce-provenance-clarification-closure.md).

Status: bounded static review completed. No additional runtime correction is justified by the inspected cases. This is a design assessment, not evidence of agent compliance, marketing performance or complete source verification.

## Scope and method

Read [Chapter 09](../../skills/marketing-practitioner/handbook/09-commerce-environments-and-product-discovery.md) sections 16-21 with relevant earlier sections, the commerce path and state handoffs in [operating guidance](../../skills/marketing-practitioner/references/operating-guide.md), and the controller, continuity, uncertainty, content-selection and completion requirements in [SKILL.md](../../skills/marketing-practitioner/SKILL.md). Inspected actual loader output for the routes listed below.

The constructed tasks check whether available guidance preserves consequential state, resolves only necessary dependencies and returns to a useful requested output. The paths are possible compositions, not mandatory reading sequences. These cases were assessed against text; no agent was asked to execute them and no products, feeds or transactions were submitted.

## Representative work chains

| Constructed input and job | Decision dependencies and retained state | Required useful output and static assessment |
|---|---|---|
| Rewrite an approved product title; facts, variant and audience are settled | Core fast path; Chapter 09 section 16 is optional supporting guidance, not an indexed route | A rewritten title preserving supported meaning. No full identity model, platform-ranker research or renewed strategy is required. Supported. |
| Produce a product card and highlights from a seller title, image and specification that disagree on capacity | commerce.fact-provenance; commerce.identity only if configuration identity remains unresolved; retain each source's applicable revision and package scope | Resolve the specific discrepancy if evidence permits; otherwise qualify or withhold the affected capacity claim while producing unaffected requested copy. P1 now supplies the local reconciliation rule. Core completion prevents a source-audit note from replacing the requested artifacts. Supported. |
| Adapt a fixed variant catalog into a feed and buyer-facing descriptions | commerce.identity, commerce.data-classes and commerce.information-allocation as needed; destination field rules are a separate current platform dependency | Preserve each variant's facts, identifiers and applicable commercial state; use appropriate structured fields and readable explanations. If only submission is observed, report submission rather than claiming the processed or displayed record is corrected. Supported as design; exact implementation needs destination documentation and actual state. |
| Explain a two-item bundle whose displayed starting price belongs to a different configuration or buyer condition | commerce.identity and commerce.commercial-state; commerce.shopper-representation-jobs when selection versus transaction information is open | Keep bundle composition distinct from order quantity and qualify the price at the relevant configuration/eligibility scope. Represent the adopted package; if asked to choose a new package or pricing policy, pass that unresolved choice to commercial-design and return with its adopted result. Supported. |
| Help a shopper evaluate compatibility under a budget, then interpret a checkout total exceeding delegated authority | commerce.resolvability, commerce.commercial-state and commerce.agentic only for the open questions; retain supported compatibility, variant, seller, total and authorization scope | Give supported fit/limitations and unresolved constraints. Do not silently extend authority to a changed total or report purchase from a checkout request. Report the actual known stage. This assesses generic state/authority logic, not authorization to conduct a transaction or validation of a protocol implementation. Supported within that boundary. |
| Adapt approved product communication into shoppable content, then interpret results after its linked target changes | Content and commerce guidance only for material representation/link decisions; commerce.content-commerce-measurement, plus commerce.observation-interpretation if event meaning or maturity is unresolved | Keep claims matched to the current target and retain the target/link history for compared events. Distinguish content engagement, product entry and attributed orders. Core continuity requires updating affected artifacts when product evidence changes. No assumption that a particular platform currently supports relinking is needed for the hypothetical case. Supported. |
| Diagnose falling sales after stock, traffic mix and the title all changed | commerce.diagnosis; commerce.observation-interpretation for event/maturity questions; Chapter 05 if causal interpretation is required | State what changed, the plausible explanations still consistent with observations and a useful discriminating check or justified action. An unavailable popular variant is a relevant constraint; the title is not automatically the cause. A recommendation must return from diagnosis with its evidence limits. Supported. |
| Retain a lesson from recently created orders compared with older completed orders | commerce.observation-interpretation, the commerce observation handoff and Chapter 06 only when retaining learning is requested | Preserve event stage, time/refund maturity, material commercial state and exposure provenance. Retain a bounded finding or unresolved comparison rather than declaring a winning listing from incompatible outcomes. Supported. |

These are not eight successful trials. They show that the inspected instructions can represent the relevant distinctions and useful stopping points without requiring a new framework.

## Suspected gaps not promoted to changes

### Source reconciliation must return to the requested output

A conflict-resolution instruction alone could encourage an agent to stop at a discrepancy report. The corrected provenance excerpt explicitly permits unaffected work to continue. The core separately requires preserving all requested deliverables, returning from dependencies and distinguishing internal constraints from audience-facing content. Adding another commerce output checklist would duplicate that contract. If the unresolved claim is essential to a truthful artifact, bounded output remains legitimate; this is not permission to conceal it.

### Multiple carriers do not imply identical wording or independent facts

Section 13 explicitly permits different representations for machine processing, human identification and detailed evaluation. The core's change-propagation rule covers a corrected source affecting both a feed and copy. The text therefore supports coordinated correction without requiring every field to repeat every specification or introducing a separate synchronization system.

### A dependency map is not a mandatory pipeline

Section 17 explicitly says its map is not a mandatory linear workflow, section 17.1 makes its context record optional, and section 21 limits its checks to consequential, relevant questions. Section 19.1's hybrid examples must be read with its applicability gate and the core's dependency-first routing. A narrow title edit does not activate both content and commerce merely because the product is sold through social media.

### Diagnosis has an existing decision owner

Section 18 ends with a discriminating check and a Chapter 05 handoff for causal work. The core requires a useful diagnosis or decision, while operating guidance carries established findings and competing explanations forward. Neither an obligatory copy rewrite nor an obligatory experiment is warranted. No new commerce-specific causal method is needed.

### Missing platform verification is a separate evidence limit

The generic routes include current platform and protocol examples. Coherence of the shared reasoning cannot certify those examples. Keep the previous review's source limits visible and audit consequential platform claims separately; do not infer a new universal rule from a missing or inaccessible implementation detail.

## Selected external checks

- C03: reread the resource description in [Google Merchant API ProductInput](https://developers.google.com/merchant/api/reference/rest/products_v1/accounts.productInputs). It distinguishes submitted input from the processed product, explains combination with rules/supplemental data and notes processing delay. This supports the feed-status boundary, not a guarantee about a particular live catalog.
- C02: inspected examples and troubleshooting in [Google product-variant guidance](https://developers.google.com/search/docs/appearance/structured-data/product-variants). The examples retain variant-specific descriptions and commercial/visual state; the guidance does not guarantee appearance of structured-data features. These are scoped implementation statements, not evidence of a universal schema or marketing lift.
- Retried the existing [UCP checkout locator](https://ucp.dev/specification/checkout/). Retrieval again returned a redirect-only page with no substantive specification. UCP/AP2/ACP mechanics and the wider agentic source set remain unverified by this pass. No conclusion of falsity or obsolescence follows from that access limit.

No new source was added to runtime. The workflow assessment is practitioner synthesis; these selected sources support narrower distinctions, not the complete chains. Other platform examples retain the limitations documented in [the shared-model review](15-commerce-core-content-review.md).

## Retrieval inspection

| Actual route | Retrieved lines | Decision-changing context retained |
|---|---:|---|
| commerce.identity | 149 | Scoped IDs, configuration, bundle versus quantity and commercial-design handoff |
| commerce.fact-provenance | 20 | Applicability, conflict resolution and continuation of unaffected work |
| commerce.data-classes | 119 | Product/commercial/observation classes; input versus processed state; P1 |
| commerce.commercial-state | 114 | Variant, seller, buyer and time scope; displayed versus final price |
| commerce.representation | 104 | Human/machine roles and composed representations |
| commerce.information-allocation | 333 | Appropriate carriers, supported compatibility and non-guarantees; includes resolvability |
| commerce.shopper-representation-jobs | 23 | Selection, evaluation and transaction jobs |
| commerce.agentic | 159 | Authority bounds and transaction stages; protocol examples need separate verification |
| commerce.content-commerce-measurement | 17 | Target/link history, attribution boundary and conditional observation route |
| commerce.observation-interpretation | 118 | Event stages, maturity, exposure and Chapter 05/06 handoffs |
| commerce.diagnosis | 55 | Material competing explanations, discriminating check and causal-method handoff |
| commerce.discovery | 117 | Conditional system stages, source conflicts and exposure limits |
| commerce.field-evidence | 40 | Field/system/stage scope; no inferred ranking weight or universal tactic |

Section 16 has no commerce.fast-path route. The core and operating guide already expose direct execution for sufficient narrow work, and section 16 was read in the chapter. An initial reviewer probe used that nonexistent route; it was a reviewer lookup error, not a broken manifest binding. A second local inspection wrapper incorrectly treated the loader's tuple return as text; after correcting the wrapper, all listed slices were retrieved successfully. Neither probe modified repository code.

## Outcome and verification limits

Only this report was added. No runtime, controller, index, platform, bibliography or evaluation changes are proposed from this pass. Verified all five relative file links, UTF-8 without BOM, CRLF, terminal newline and final worktree state; git diff --check passed. All 77 pre-existing runtime/research files match their pre-write hashes. No package or behavioral test rerun is necessary for this report-only addition; prior P1 package/routing results remain recorded in its closure rather than claimed as fresh results here.

The next shared-content audit can address Chapter 10: commercial design, pricing and terms. Current platform and commerce-protocol claims remain a separate bounded evidence backlog. No live trials, old-pilot comparisons, commits or pushes were performed.

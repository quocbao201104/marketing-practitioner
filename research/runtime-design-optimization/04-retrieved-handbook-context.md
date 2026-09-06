# Retrieved handbook context and interpretation

Status: design corrections implemented and statically verified, including independent review. Behavioral evaluation is deferred.

## Scope and decision

This is part 2 of the runtime design work: preserve decision-relevant meaning when handbook guidance is read through an existing section route. It does not redesign route discovery, the manifest, extraction code, or the handbook's marketing theory.

The reading unit is the already-loaded SKILL.md plus the actual selected excerpt and relevant task context. It is not a context-free paragraph. Shared truth, uncertainty, authorization, and completion rules already in the core do not need to be copied into every route.

The manifest contains 86 handbook routes across eight namespaces: content (12), commerce (15), commercial-design (14), landing-page (11), email (9), discovery (8), paid-media (8), and brand-identity (9). Inventory/extraction checks establish physical coverage, not semantic completeness. The focused semantic review below concerns five routes and explicit comparison cases; it is not certification of every handbook statement or every platform module. Foundational Chapters 00-07 are direct chapter reads, outside this indexed-boundary correction.

## Acceptance criteria

A retrieved section should preserve:

- its decision subject and the scope that determines applicability;
- definitions or antecedents needed to interpret its local terms;
- conditions, qualifications, and evidence status whose omission would change the decision;
- a recoverable destination and reason for any material dependency outside the excerpt.

These are author review criteria, not required headings or a runtime form. A short local clarification can preserve an essential distinction; a targeted reference can carry substantial supporting detail. A link alone must not conceal a condition that reverses the advice.

Do not require whole-chapter loading, automatic dependency expansion, or full standalone duplication. Do not add a glossary, source ledger, or standard preamble to every slice. Leave sufficient sections unchanged.

## Static counterexamples and corrections

These are constructed design counterexamples grounded in the current text and extraction boundaries. They are not observed agent failures, historical pilot evidence, or behavioral efficacy results.

### C1: Practitioner vocabulary loses its epistemic status

INPUT / TASK: Explain the shared content model and whether it is an established scientific model.
CURRENT ROUTE: content.core-grammar starts at Chapter 08 section 3.
GAP: Its opening refers to prior model development. The explicit practitioner-synthesis / not-unified-validated-theory qualification is in section 1, outside the slice.
DECISION IMPACT: The vocabulary can be reported as established ontology or a literal platform schema rather than project synthesis with narrower conceptual support.
SMALLEST CORRECTION: Replace the historical opening with local domain and evidence-status context. Preserve the vocabulary and conditional use.

### C2: A material dependency is named by an absent layer

INPUT / TASK: Translate a disclosed platform signal into a defensible content mechanism.
CURRENT ROUTE: content.machine-mediation, section 7.3.
GAP: It directs the reader to Layer 2's behavior-to-mechanism bridge, but that bridge is outside the excerpt and neither its exact heading nor route is specified.
DECISION IMPACT: The required provenance / response-opportunity / interpretation step is harder to recover than the directly visible recommendation vocabulary.
SMALLEST CORRECTION: Point to section 5.6 with its local anchor and containing logical route, content.audience-interaction. Preserve the existing conditional trigger; do not require the entire model.

### C3: Selecting a metric is mistaken for validating its meaning

INPUT / TASK: Select and interpret saves, clicks, or downstream purchases as success measures for content.
CURRENT ROUTE: content.job-measurement contains outcome families and job distinctions.
GAP: Detailed observation-unit, opportunity, and maturity semantics live in section 9, without a local pointer from this summary.
DECISION IMPACT: A suitable outcome label still leaves unresolved whether the available observation measures it under the relevant regime.
SMALLEST CORRECTION: State the selection-versus-interpretation boundary and link to content.measurement-evidence only when those semantics remain material and unresolved. Do not mandate that read for selecting a measure from already-defined data.

### C4: A source category stands in for the underlying product fact

INPUT / TASK: Evaluate a compatibility claim supplied by a seller field or platform-inferred attribute.
CURRENT ROUTE: commerce.fact-provenance is section 5.5 alone.
GAP: The excerpt lists origins and asks for source/confidence, while section 5.4 separately explains the distinction between the underlying claim, seller submission, and platform-derived state.
DECISION IMPACT: Naming a catalog or feed as the source does not determine what was verified, for which model/variant, or whether an inference became a fact.
SMALLEST CORRECTION: Retain that distinction locally and tie support to the relevant product/variant and material scope. Do not add a source-ranking hierarchy or numeric confidence score.

### C5: Persistent content history hides changing commerce targets

INPUT / TASK: Interpret orders credited to a shoppable video before and after its product link changed.
CURRENT ROUTE: commerce.content-commerce-measurement is section 10.2 alone.
GAP: The excerpt lists metrics and asks for surface/edge/attribution scope. The concrete independent video/product identity and relinking context sits in section 10, outside this child slice; outcome maturity is in section 12.
DECISION IMPACT: Persistent video identity can conceal changed product targets, and attributed order counts can be reported as incremental sales or mature outcomes.
SMALLEST CORRECTION: Retain the target/history distinction and attributed-versus-incremental boundary locally; reference commerce.observation-interpretation if stage, commercial scope, or maturity is unresolved. This does not add or update any platform capability claim.

## Comparison cases left unchanged

- commerce.resolvability includes its own truth limits, platform-supported carriers, and no-guaranteed-selection boundary; its nested qualifications remain inside the extracted section.
- commerce.agentic includes scoped authority, stage/time state, and limits on when protocol detail is needed.
- commerce.discovery-modality names its input/matching distinction and scoped examples inside the child slice.
- commerce.shopper-representation-jobs gives concrete selection/evaluation/transaction questions; the core already supplies audience-facing minimum understanding and truthful qualification.
- landing-page.commercial-comparison states that commercial conditions must be sufficiently resolved and preserves the owner of unresolved design.
- email.sequence includes the tracked-open limitation, justified waiting, and exit conditions.
- paid-media.control includes hard-versus-soft controls, precedence, and the paid-relationship/delivery boundary.
- brand-identity.refinement includes the fixed-state boundary, optional method status, and the scope of its pixel-size example.

No universal preamble or automatic prerequisite was added to these routes.

## Research basis and limits

[Anthropic, Introducing Contextual Retrieval (2024-09-19)](https://www.anthropic.com/engineering/contextual-retrieval) describes how a chunk can lose the entity/time context needed to interpret it and adds chunk-specific context for embedding and lexical retrieval. The reviewed article reports experiments on a different retrieval stack.

The design inference here is limited: inspect whether extracting an existing handbook section removes material context. This repository uses deterministic heading/marker extraction; it does not adopt contextual embeddings, generated annotations, BM25, reranking, the article's chunk sizes, or its reported gains. The local before/after text and chapter boundaries justify these corrections; that article does not establish their behavioral effectiveness.

## Implementation and verification

The authoring criteria are retained in CONTRIBUTING.md. Runtime changes are limited to the five sections in Chapters 08 and 09. Existing logical routes and heading selectors remain intact. The uncommitted part-1 changes in SKILL.md, operating-guide.md, and the part-1 design record must remain byte-identical during this task.

Completed verification:
- Read all five modified excerpts through the existing extraction function and compared their context with the source chapter.
- Compared all 27 routes in the two affected chapters against the pre-edit snapshot: exactly the five intended excerpts changed; the remaining 22 extracted texts are identical.
- Package-only verification passed both the repository package validator and the current Codex skill validator.
- Routing validation passed 68 mechanics smoke checks and 261 routes / 233 evidence sources.
- All three new local anchors and their three logical route destinations resolved.
- Existing UTF-8, no-BOM, CRLF, non-ASCII text, and terminal-newline states were preserved in all three modified existing files.
- All three pre-existing part-1 files remained byte-identical to the pre-edit snapshot.
- Final diff review found only the intended authoring criteria and five runtime corrections; git diff --check passed. No index, loader, or platform module changed.

Independent read-only review completed after an initial usage-limit interruption. The reviewer inspected all five modified excerpts, their supporting chapter context, all eight unchanged comparison routes, and the current SKILL caller context. It reported no actionable findings and explicitly limited the result to static design review. Package, routing, integrity, and preservation checks above were performed by the primary agent.

Behavioral trials remain deferred by user instruction. Structural checks cannot establish lower agent error rates.

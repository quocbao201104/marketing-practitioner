# Changelog

All notable changes to this repository are documented here.

The project uses semantic versioning for published skill revisions. Early versions may change structure while the conceptual model is stabilized.

## [0.9.0] - 2026-08-25

### Added

- Added `handbook/14-paid-media-architecture.md`, a bounded specialist layer for decisions where economic resource is used to secure, reserve, compete for, allocate, or amplify mediated audience exposure.
- Added the `paid-media.*` just-in-time namespace for scope/activation, objective/decision value, control/authority, paid opportunity/allocation/realization, observation/billing/attribution/optimization feedback, cross-owner handoffs, retained decision records, and anti-folklore invariants.
- Added `references/paid-media-evidence.md` with scoped current-provider, programmatic-buying, creator-amplification, and DOOH measurement evidence plus explicit `Supports` / `Does not support` boundaries.
- Added `research/paid-media-architecture/` theory freeze, bounded implementation design, self-review, mechanical-verification record, targeted adjudication, frozen independent-review contract, local correction record, and correction-verification gate.
- Added a 20-case adversarial Paid Media suite plus a focused mixed-publisher review regression covering fast-path preservation, paid relationship vs paid delivery, sponsored content vs amplification, objective/optimization mismatch, hard vs soft controls, control precedence, portfolio/shared allocation, non-auction inventory, adaptive state/history, exposure uncertainty, billing/optimization roles, attribution/causality, retail-media identity composition, and generic-discovery boundaries.

### Changed

- Updated `SKILL.md` so paid-delivery decisions can route directly to the smallest `paid-media.*` section while narrow ad-copy transformations remain on the existing fast path and unresolved performance symptoms remain Chapter 05-first.
- Preserved Chapter 04 ownership of ad message/claim/proof, Chapter 05 ownership of causality/incrementality/experiments, Chapter 08 ownership of shared platform/content grammar, Chapter 09 ownership of product/listing/commerce identity, Chapter 10 ownership of customer-facing Commercial Design, Chapter 11 ownership of landing-page architecture, and Chapter 13 ownership of generic non-paid discovery.
- Kept current provider objectives, bidding products, auction/deal mechanics, audience-control meanings, placement systems, billing rules, attribution windows, learning-state definitions, policy constraints, and automated-creative behavior as time-sensitive JIT dependencies rather than permanent provider modules or universal paid-media laws.
- Updated installable skill metadata and public README capability/status/routing examples to `v0.9.0`.

### Fixed

- Added the missing `paid-media.handoffs` logical route for Chapter 14 Section 6 (`Owner boundaries and decision handoffs`) after independent review found that the detailed cross-owner guidance was otherwise dead knowledge under helper-driven smallest-route execution.
- Separated controller routing so cross-owner handoff uncertainty maps to `paid-media.handoffs`, activation/scope checks map to `paid-media.core`, and anti-folklore checks map to `paid-media.invariants`.

### Validation status

- Frozen theory and current-system gap analysis confirmed a bounded Paid Media specialist-knowledge gap without finding an irreducible shared-grammar failure; no shared primitive or new controller job was added.
- Targeted runtime walkthrough recorded **20 PASS, 0 PARTIAL, 0 FAIL** across the frozen adversarial suite.
- Independent adversarial runtime review of original frozen implementation/evaluation target `bf81ec779dc43a94a72f9752209c6b82ef47e437` returned **PROCEED AFTER LOCAL CORRECTIONS**, identifying one local JIT owner-boundary routing defect and no shared-architecture failure.
- The focused post-review regression recorded **1 PASS, 0 PARTIAL, 0 FAIL** after the local correction. The corrected implementation/evaluation target was frozen at `fc8576ea4149b344d3964458f00109a6e9cc5507`, and independent correction verification returned **CORRECTION VERIFIED — PROCEED TO RELEASE PREPARATION**.
- Corrected routing source now covers eight `paid-media.*` routes and declares 58 routing-mechanics smoke checks. The exact corrected 58-check assertion set executed successfully in a local mirror, while full checked-out repository execution remained unavailable because the sandbox could not resolve `github.com`; no GitHub Actions/CI run is claimed.
- This release does not add campaign, auction, targeting, learning, feedback, or paid-audience primitives; permanent Meta/Google/TikTok/LinkedIn Ads modules; a universal media funnel, auction formula, media optimizer, or attribution model; or causal business claims from platform-attributed outcomes.

## [0.8.0] - 2026-08-25

### Added

- Added `handbook/13-search-and-discovery-architecture.md`, a bounded specialist layer for generic non-commerce discovery decisions spanning information need/expression, scoped availability, retrieval/selection, human-selection versus system-commitment/grounding, and discovery observation semantics.
- Added the `discovery.*` just-in-time namespace for core scope, need/query distinctions, availability/identity/freshness, retrieval/selection, grounding/commitment, observation semantics, retained decision records, and anti-folklore invariants.
- Added `references/search-discovery-evidence.md` with scoped current-provider and information-retrieval evidence plus explicit non-transfer boundaries.
- Added `research/search-discovery-architecture/` theory freeze, implementation self-review, mechanical-verification record, targeted-evaluation adjudication, frozen independent-review contract, and release-preparation gate record.
- Added a 20-case adversarial Search & Discovery suite covering fast-path preservation, published/indexed/discoverable collapse, query/intent/retrieval-formulation collapse, retrieval versus evidentiary fitness, citation/telemetry overclaim, queryless discovery, missing telemetry, and Chapter 01/02/04/05/08/09/11 owner controls.

### Changed

- Updated `SKILL.md` so generic discovery-specific decisions can route directly to the smallest `discovery.*` section while narrow search-related transformations remain on the existing fast path.
- Kept platform-native search-oriented content participation with Chapter 08 and product/listing/catalog discovery with Chapter 09 instead of letting the generic discovery specialist absorb those owners.
- Preserved Chapter 01/02 ownership of customer/segment/market-demand inference, Chapter 04 ownership of marketing message/claim/proof, Chapter 05 ownership of causality/incrementality, and Chapter 11 ownership of landing-page architecture after entry.
- Updated release metadata, handbook navigation, public README capability/status text, routing examples, and evidence examples to `v0.8.0`.

### Validation status

- The frozen theory and current-system gap analysis confirmed a local specialist-knowledge gap without finding an irreducible shared-grammar failure; no shared primitive or new controller job was added.
- Targeted runtime walkthrough recorded **20 PASS, 0 PARTIAL, 0 FAIL** across the frozen adversarial suite.
- Independent adversarial runtime review of frozen implementation/evaluation target `ccac14d214ad8a77fcec8199dedb7fc78a840cc7` returned **PROCEED TO RELEASE PREPARATION**. Later release-preparation commits are not retroactive implementation evidence for that review target.
- Mechanical verification remains intentionally scoped: 28 helper/source/path assertions were executed locally and the eight `discovery.*` bindings plus `SD09` evidence lookup were verified directly against the candidate branch; the full checked-out 49-check routing script was not executed in the available environment and is not claimed as passed.
- This release does not claim universal SEO/GEO/AEO/LLMO rules, complete knowledge of private ranking/retrieval systems, a global discoverability state, universal relevance/grounding/freshness/authority scores, guaranteed ranking/citation/answer inclusion, or causal/market-demand conclusions from discovery telemetry.

## [0.7.0] - 2026-08-25

### Added

- Added `handbook/12-email-communication-architecture.md`, a bounded specialist layer for deciding whether, when, and how email should carry already-resolved strategy under communication-relevant state, history, authority, feasibility, and observation constraints.
- Added the `email.*` just-in-time namespace for send/wait/exit/suppress decisions, scoped send state, state-conditioned sequence reasoning, inbox/body/action allocation, cross-surface continuity, observation semantics, decision records, and invariants.
- Added `references/email-communication-evidence.md` with scoped provider, protocol, regulatory, privacy, and field-experiment evidence plus explicit non-transfer boundaries.
- Added `research/email-communication-architecture/` theory freeze, targeted evaluation adjudication, and frozen independent-review contract.
- Added 20 targeted adversarial cases and 12 fresh task-level runtime walkthroughs covering fast-path preservation, no-action follow-up pressure, need/authority/feasibility separation, scoped unsubscribe state, state-conditioned branching, optional action/handoff, telemetry semantics, causal boundaries, owner handoffs, and non-email owned-channel regression.

### Changed

- Updated `SKILL.md` so email-specific state/history/send/allocation/observation decisions can route directly to the smallest `email.*` section while narrow email copy transformations remain on the existing fast path.
- Preserved Chapter 04 ownership of unresolved message/claim/proof, Chapter 05 ownership of causality and experimentation, Chapter 08 ownership of generic relationship/state/representation grammar, Chapter 10 ownership of unresolved commercial transitions, and Chapter 11 ownership of downstream landing-page architecture.
- Preserved the generic Chapter 08 composition path for SMS, push, and other non-email owned-channel decisions instead of letting the email specialization capture them.
- Updated release metadata and public documentation to `v0.7.0` without adding a CRM, lifecycle, journey, campaign, funnel, deliverability, legal-compliance, or global send-eligibility subsystem.

### Validation status

- Targeted internal evaluation found no routing, specialist-knowledge, owner-handoff, or shared-grammar gap and retained one explicit execution watch: ordinary email rewrites must not over-route merely because the new namespace exists.
- Independent adversarial runtime review at frozen implementation/evaluation head `ca44ca096e3d38156611f9fef7b3ea17139e2772` returned **PROCEED TO RELEASE PREPARATION** after 22 fresh attacks: 22 PASS, 0 PARTIAL, 0 FAIL.
- The independent reviewer found no surviving targeted correction, no irreducible representation collision, and no justification for a new primitive or broader CRM/lifecycle architecture.
- The deterministic routing-test definition now covers all nine `email.*` routes plus `EM03` evidence lookup; full checked-out-branch execution was not performed during this release-preparation pass.
- This release does not claim universal cadence, send-time, personalization, subject-line, CTA, frequency, deliverability, legal-permission, or causal-effect rules, nor benchmark-grade reliability across every agent host.

## [0.6.0] - 2026-08-24

### Added

- Added `handbook/11-landing-page-architecture.md`, a bounded specialist layer for compiling already-resolved reader, message, proof, commercial, and action state into landing-page information/action architecture.
- Added the `landing-page.*` just-in-time namespace for page job/entry state, information sequence, proof/risk placement, visual allocation, CTA/form architecture, responsive allocation, commercial comparison, diagnosis boundaries, decision records, and invariants.
- Added `references/landing-page-evidence.md` plus the repository-level `research/landing-page-architecture/` research brief, evidence ledger, theory freeze, and freeze adjudication.
- Added targeted landing-page adversarial cases covering fixed commercial state, hero/template folklore, action readiness, form qualification, visual proof, navigation, comparison, FAQ, responsive order, observation-vs-cause, practitioner-lift laundering, mixed-owner handoffs, shared proof, sensitive fields, qualified outcomes, returning visitors, and exploratory navigation.

### Changed

- Updated `SKILL.md` so a page-architecture decision with sufficiently resolved reader/message, proof/claim, and commercial state can route directly to the smallest `landing-page.*` section instead of loading Chapter 04 merely as a routing hop.
- Preserved Chapter 04 ownership of unresolved message/claim/proof, Chapter 10 ownership of unresolved Commercial Design, and Chapter 05 ownership of causal diagnosis/experimentation.
- Updated public README and handbook navigation to expose Chapter 11 and the new specialist path without introducing a `LANDING_PAGE` primitive, new controller job, CRO subsystem, fixed page-type ontology, or template library.

### Validation status

- Independent adversarial theory synthesis retained seven bounded distinctions and rejected fixed hero recipes, section taxonomies, awareness-state machinery, CRO ownership, universal form/navigation rules, and case-study lifts as universal design laws.
- Independent implementation review passed architecture creep, template creep, folklore laundering, owner boundaries, resolved-state preservation, routing integrity, evidence discipline, minimality, and unrelated-regression checks.
- The review requested one targeted correction to strengthen the adversarial suite; the eval-only correction expanded route coverage to all 11 `landing-page.*` routes and added mixed-owner/harder discrimination cases.
- Aggregate routing integration adds one `landing-page` namespace while preserving prior route bindings.
- No new top-level marketing layer, shared primitive, controller job, Commercial Design dimension, or broad CRO/landing-page performance claim was introduced.

## [0.5.1] - 2026-08-24

### Changed

- Exposed eight precise just-in-time routes to existing Chapter 08/09 knowledge for consequential content strategy, job-aligned measurement, content diagnosis, product-fact provenance, discovery modality, content-commerce measurement, shopper representation jobs, and commerce observation interpretation.
- Tightened conditional handoffs across research, segmentation, positioning, Commercial Design, messaging, localization, commerce observation, diagnosis, and organizational learning so decision-relevant provenance, authority, state, objective, mechanism, and validity context are less likely to be lost between paths.
- Added bounded local decision guidance for survey interpretation, root-source independence, behavioral non-action, B2B decision actors, association/offer transitions, cross-touch proof, compound interventions, marginal allocation, retention measurement, commerce bundle quantity, and complex commercial-condition composition.
- Clarified market-selection-before-localization, platform-constraint-to-Commercial-Design dependency, owned-channel next-message composition, and temporary commercial modifiers without introducing new controller jobs or shared layers.

### Fixed

- Normalized logical evidence-source paths to POSIX-style output across operating systems, fixing the Windows path-separator portability failure without changing retrieval or fail-closed behavior.
- Prevented compound commercial changes from being reduced to a scalar price intervention when other material dimensions such as commitment, eligibility, configuration, or modifiers also changed.
- Preserved root-source independence so multiple derivative notes from the same underlying interviews do not become independent evidence downstream.

### Validation status

- Whole-system adversarial gap audit found `0` true shared representational gaps and recommended local hardening rather than architecture expansion.
- `python skills/marketing-practitioner/scripts/get-knowledge.py --validate` passed with `213 routes / 159 evidence sources`.
- The routing-mechanics suite passed `30` checks after the cross-platform path correction and route additions.
- Targeted regressions `R1–R15` all passed, covering routing, resolved-state freezing, market selection/localization, platform constraints, owned-channel composition, compound interventions, causal-learning handoffs, root-source independence, marginal allocation, and behavioral non-action.
- Independent minimality review found no architecture expansion, route inflation, over-routing, handoff inflation, theory drift, unsupported evidence, broken fast paths, or Level 3 changes.
- No new controller job, primitive, shared handbook layer, platform family, Commercial Design dimension, or broad benchmark claim was introduced.

## [0.5.0] - 2026-08-24

### Added

- Added `handbook/10-commercial-design-pricing-and-terms.md`, a bounded Commercial Design layer for unresolved configuration/entitlement, payment/value-capture architecture, relationship/risk terms, and selection/allocation decisions.
- Added `commercial-design.*` just-in-time routes for scope, core dimensions, evidence, decision logic, dynamics, governance, handoffs, decision records, and invariants.
- Added `references/commercial-design-evidence.md` with scoped `CD01`–`CD16` source records and explicit non-transfer boundaries.
- Added the repository-level `research/commercial-design/` theory lineage, preserving gap analysis, rejected hypotheses, prior-art pressure, evidence boundaries, and freeze adjudication outside runtime knowledge.
- Added a targeted Commercial Design runtime routing smoke covering activation, Chapter 05/09 handoffs, Finance/Operations/Sales/Business-Model boundaries, dynamics, and evidence interpretation.
- Added human navigation READMEs for the handbook, platform modules, and commerce platform modules without changing runtime routing semantics.

### Changed

- Extended `SKILL.md` with a Commercial Design / pricing operating path while preserving the existing `DECIDE` job, resolved-state freezing, dependency-first routing, fast paths, and minimum-sufficient-output behavior.
- Updated public documentation and architecture maps to distinguish Commercial Design from positioning/value, message/copy, current commerce-state representation, governance, and executed transaction state.
- Updated the handbook navigation to cover Chapters 08–10 and the large-chapter semantic-routing model.
- Updated release metadata and README status to `v0.5.0`.

### Fixed

- Corrected `free trial vs free tier` routing so the decision spans `commercial-design.configuration` + `commercial-design.terms`, with payment and dynamics loaded only when materially required.
- Normalized the CD08 trial evidence boundary to acquisition, retention, and profitability in the studied SaaS setting; removed unsupported runtime promotion of a `usage` outcome.
- Tightened the CD12 boundary so personalized-pricing evidence supports divergence among firm profit, aggregate consumer surplus, and distributional outcomes without being promoted into evidence of perceived fairness or trust.

### Validation status

- Independent adversarial theory review found a genuine Commercial Design gap and allowed theory freeze after one targeted CD12 evidence correction.
- Independent adversarial implementation review found no architecture blocker after one targeted JIT routing correction and CD08 normalization.
- The targeted Commercial Design runtime routing smoke records 10/10 bounded walkthroughs as PASS.
- No new controller job, generic `OFFER` primitive, Chapter 09 semantic rewrite, platform expansion, pricing optimizer, or broad benchmark claim was introduced.
- Full checked-out-branch `python skills/marketing-practitioner/scripts/get-knowledge.py --validate` was not executed during this release pass; route/helper compatibility was inspected statically and the helper itself was unchanged.

## [0.4.0] - 2026-08-24

### Added

- Added a research-backed `TASK-SPECIFICATION-GUIDE.md` to the installable skill so users do not need to learn prompt-engineering vocabulary before using Marketing Practitioner.
- Added a minimum-sufficient task-specification model built around the current job plus only the qualifiers that can materially change the result.
- Added guidance for preserving resolved decisions, bounding evidence and claims, handling missing information, controlling output, and avoiding unnecessary context.
- Added an agent-side prompt-compilation quick start: users can provide a rough request and context, then let the agent compile the smallest sufficient working specification before execution.
- Added scoped task-specification evidence notes covering prompt underspecification, context quality, clarification, prompt sensitivity, examples, and current provider guidance.

### Changed

- Packaged the canonical Task Specification Guide inside `skills/marketing-practitioner/` so it travels with Skills CLI installations.
- Kept the repository-root task-specification file as a pointer only, preventing duplicate guide content from drifting.
- Expanded README onboarding with an optional compile-and-execute path for users who do not want to write a structured prompt themselves.

### Evidence boundary

- This release does not claim that one prompt template is universally optimal.
- The task-specification model is intentionally conditional: longer prompts, more context, more examples, and more explicit fields are not assumed to improve every task.
- No shared marketing ontology, routing architecture, or runtime-controller semantics were changed for this release.

## [0.3.0] - 2026-08-24

### Added

- Added `handbook/09-commerce-environments-and-product-discovery.md` and commerce modules for Google commerce, Amazon, TikTok Shop, Shopee, Etsy, and Lazada.
- Added conversational and agent-mediated commerce reasoning, including product resolvability, delegated authority, checkout/order-state boundaries, and machine-consumable product representations.
- Added addressable just-in-time knowledge routing with 13 namespaces and 191 logical routes.
- Added deterministic semantic-section and evidence-source lookup with routing integrity checks and fail-closed behavior.

### Changed

- Refined the runtime controller around the current job, resolved state, open decision, and dependency-first loading while preserving fast paths for narrow tasks.
- Added capability-aware routing fallback for hosts without helper execution.
- Repositioned the repository as a research-first marketing decision system for AI agents.
- Expanded README onboarding with plain-language guidance and copy-paste examples for non-marketers.

### Fixed

- Prevented fenced Markdown examples from being misread as routing or evidence headings.
- Added the missing generic commerce recommendation route.
- Made incompatible routing CLI modes fail closed instead of silently returning the wrong artifact.

### Validation status

- The targeted routing-mechanics suite contains 22 deterministic checks and passes after the adversarial correction pass.
- Independent adversarial re-review returned `PASS WITH NON-BLOCKING NOTES` for the JIT routing architecture.
- This release does not claim complete knowledge of private platform ranking systems or universal runtime reliability across every agent host.

## [0.2.0] - 2026-08-23

### Added

- Added `handbook/08-content-environments-and-distribution.md`, a compressed six-layer model for platform-native content, distribution, interaction, recommendation, governance, and evidence interpretation.
- Added production platform modules for Instagram, TikTok, LinkedIn, Facebook, and X, all using the same compact runtime vocabulary rather than separate platform-specific frameworks.
- Added implementation-backed X guidance using the public `xai-org/x-algorithm` For You implementation, with explicit boundaries against turning exposed ranking parameters into content hacks.
- Added research/audit artifacts for compact-core losslessness, runtime-routing adversarial walk-throughs, and a pre-benchmark execution smoke pack.

### Changed

- Extended the decision-first runtime controller with a platform-content/distribution operating path and just-in-time routing to Chapter 08 and the smallest relevant platform module.
- Compressed platform reasoning to eight durable things — actor/source, content object, content representation, audience state, typed relationship/delivery/permission edge, interaction act, platform/mediation state, and observation record — with provenance, scope/relativity, and history/state transition as cross-cutting modifiers.
- Added guardrails that keep content object, representation, surface, relationship, delivery, permission, observed action, system feedback, ranking objectives, attribution, and causality distinct when those distinctions can change a decision.
- Preserved a fast path for simple captions/posts so platform knowledge does not automatically expand a narrow writing task into strategy or recommender-system analysis.
- Expanded the bibliography and platform evidence base with current product documentation, recommender-system literature, representation architecture references, and scoped implementation evidence.

### Validation status

- A frozen 20-case conceptual losslessness audit produced 19 `LOSSLESS`, 1 `LOSSLESS / INTERNAL UNKNOWN`, 0 `PARTIAL`, and 0 `FAIL`; no retired primitive or new durable primitive was required.
- A 22-case static runtime-routing walk-through found 0 routing gaps and 0 knowledge gaps; execution reliability remains intentionally pre-benchmark and is expected to improve through real use and fresh smoke runs.
- This release does not claim universal platform theory, causal effectiveness of platform tactics, or benchmark-grade runtime reliability.

## [0.1.4] - 2026-08-22

### Changed

- Refactored the executable runtime around decision-first operating-path selection instead of one global default pipeline.
- Reduced always-on instructions to universal invariants and moved research, positioning, copy, diagnosis, localization, and learning guidance behind decision-point loading.
- Added explicit state handoffs so downstream stages receive only the conclusions, constraints, proof, and uncertainty needed for the next decision.
- Preserved the v0.1.3 audience-facing content-selection gate while strengthening source fidelity against unsupported first-person experience or preference.

## [0.1.3] - 2026-08-22

### Changed

- Improved audience-facing content selection during copywriting.
- Separated internal claim constraints from information that belongs in the final message.
- Required relevant details to justify their place against the reader's current decision and attention budget.
- Added an omission test that preserves material proof, limitations, uncertainty, and next-action information while avoiding unnecessary disclosure.

## [0.1.2] - 2026-08-22

### Changed

- Packaged the installable skill under `skills/marketing-practitioner/`.
- Moved `SKILL.md`, handbook, frameworks, and bibliography into the same skill directory so supporting resources travel with multi-file installations.
- Aligned the skill directory name with the frontmatter name `marketing-practitioner`.
- Updated README, contribution guidance, and attribution links for the packaged layout.

## [0.1.1] - 2026-08-22

### Added

- Skills CLI quick-start and install-count badge in the README.
- A short activation example showing the intended evidence-to-strategy-to-copy behavior.
- Explicit progressive-loading guidance for skills-compatible clients.
- Resource routing from operating modes to the relevant handbook, framework, and bibliography files.

### Changed

- The operational skill now tells agents to load only the smallest task-relevant set of supporting resources instead of consulting the repository broadly by default.

## [0.1.0] - 2026-08-21

### Added

- Initial English edition of the Marketing Practitioner skill.
- Evidence-informed operating model from market learning through copy and scoped learning.
- Academic handbook structure covering customer research, segmentation, positioning, messaging, copywriting, diagnosis, experimentation, organizational learning, localization, and ethics.
- Practitioner cards and quality rubrics for applied work.
- Selected bibliography emphasizing primary research, academic monographs, and methodological sources.
- Third-party attribution for the MIT-licensed AI Copywriter / humanizer lineage.
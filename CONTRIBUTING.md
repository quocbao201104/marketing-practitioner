# Contributing

Contributions are welcome when they improve the conceptual accuracy, practical usefulness, evidence quality, runtime reliability, or clarity of Marketing Practitioner **without expanding the project by accident**.

This repository is a research-first marketing decision system for AI agents. It is not intended to become a general marketing wiki, a collection of platform hacks, or a generic agent-framework project.

The main contribution rule is:

> Change the smallest surface that can correct a demonstrated problem.

Do not broaden shared architecture, introduce a new primitive, or add another platform merely because the addition looks useful in isolation.

---

## Project scope

The current project covers decision-relevant marketing reasoning across:

- customer research and evidence synthesis;
- segmentation, ICP, JTBD, and target selection;
- positioning, value, alternatives, proof, and trade-offs;
- commercial design across configuration/entitlement, payment/value-capture architecture, relationship/risk terms, selection/allocation, evidence, governance, and transitions;
- message strategy, copywriting, and copy critique;
- diagnosis, causal reasoning, experimentation, and measurement;
- organizational learning and postmortems;
- international marketing, localization, and ethical persuasion;
- scoped local-adaptation extensions when local evidence demonstrates a decision-changing mechanism without creating a country profile or new decision owner;
- social/content environments, distribution, recommendation, interaction, and observation;
- commerce environments, product discovery, product information, commercial state, and marketplace representation;
- conversational and agent-mediated commerce where it changes a marketing or product-discovery decision;
- runtime routing and retrieval mechanisms required to make the skill use its own knowledge reliably and economically.

A contribution should improve one of those capabilities or correct a concrete failure within them.

### Out of scope by default

The following do **not** belong here unless they are required by a concrete in-scope marketing decision:

- generic prompt collections or prompt-engineering advice;
- general-purpose agent architecture, memory, orchestration, or vector-database design;
- CRM, sales-ops, support-ops, accounting, payment, fulfillment, or back-office automation as standalone domains;
- business-model strategy, product-roadmap ownership, finance, operations, legal/compliance, or sales authority as standalone domains;
- scraping systems, data pipelines, browser automation, or integration code unrelated to the skill runtime;
- generic SEO checklists, growth-hack lists, viral formulas, or conversion folklore;
- reverse-engineering private ranking systems from anecdotal observations;
- legal, tax, medical, or regulatory advice beyond identifying that a marketing decision depends on such expertise;
- adding marketplaces, social networks, or channels merely for coverage completeness.

If a proposed addition expands the project boundary, explain the decision-relevant failure that the current scope cannot represent or solve cleanly before proposing implementation.

---

## Change-risk levels

Not every change deserves the same process.

### Level 0 — editorial / mechanical

Examples:

- typo or grammar fixes;
- broken links;
- formatting;
- README wording that does not change project claims;
- release/version metadata;
- correcting an obvious file reference.

These changes should remain small. Maintainers may commit them directly. Do not create architecture work, new abstractions, or broad review machinery for a trivial correction.

### Level 1 — bounded knowledge or evidence update

Examples:

- adding a stronger source for an existing claim;
- correcting a time-sensitive platform capability;
- clarifying one platform-specific field or behavior;
- adding an evidence-ledger entry;
- tightening an existing explanation without changing shared semantics.

Requirements:

- identify the exact decision or claim affected;
- cite the strongest available evidence;
- preserve platform, surface, market, population, and time scope;
- update only the smallest relevant handbook/platform/reference section;
- do not silently generalize a platform-local fact into shared theory.

### Level 2 — runtime or shared semantic change

Examples:

- changing `SKILL.md` controller behavior;
- changing shared Chapter 08, Chapter 09, or Chapter 10 semantics;
- adding/removing a durable invariant or primitive;
- modifying `routing-index.json` structure or retrieval semantics;
- changing section-loader behavior;
- changing how content, commerce, or Commercial Design knowledge compose;
- making a platform finding apply across multiple environments.

These changes require stronger justification because they can alter many downstream decisions.

Before implementation, provide a concrete failure in this form:

```text
INPUT / TASK
→ CURRENT REPRESENTATION OR ROUTE
→ FAILURE
→ WHY THE FAILURE CHANGES THE DECISION
→ SMALLEST CORRECTION
```

If that chain cannot be constructed, prefer a local clarification or no change.

### Level 3 — project-boundary or architecture expansion

Examples:

- a new durable primitive;
- a new top-level reasoning layer;
- physical restructuring of large knowledge modules;
- a new platform family with shared architectural consequences;
- a new runtime subsystem;
- a change that materially redefines what Marketing Practitioner is.

Do not begin with implementation.

First establish that the current grammar or architecture produces a real decision-relevant failure that cannot be represented without material distortion. Prefer established conceptual parents before inventing project-specific terminology.

For a new top-level reasoning capability, keep the research/theory gate separable from runtime promotion when doing so prevents premature architecture. Repository-level `research/` artifacts may preserve gap analysis, rejected hypotheses, prior-art pressure, evidence boundaries, and freeze adjudication. They are provenance, not runtime instructions.

A larger architecture is not a contribution by itself.

---

## Protected surfaces

Some files have a much larger blast radius than others.

### `skills/marketing-practitioner/SKILL.md`

This is the runtime controller and universal behavioral contract.

Do not edit it merely because a handbook section changed or a new platform fact was discovered. Change `SKILL.md` only when agent behavior itself must change across tasks or routing boundaries.

Preserve unless a demonstrated failure requires otherwise:

- current-job identification;
- resolved-state freezing;
- open-decision identification;
- dependency-first routing;
- fast paths for narrow resolved tasks;
- source fidelity and claim boundaries;
- minimum-sufficient output;
- cross-domain composition only when multiple paths are materially required.

### Shared handbook chapters

Chapters 08, 09, and 10 are high-blast-radius shared reasoning surfaces:

- Chapter 08 — content environments and distribution;
- Chapter 09 — commerce environments and product discovery;
- Chapter 10 — Commercial Design, pricing, and terms.

A platform-specific fact should normally remain in its platform module. Promote it into shared knowledge only when the distinction survives across environments and changes more than one class of decision.

For Chapters 08 and 09, do not create a new primitive when the finding can already be represented as:

```text
object
+ representation
+ typed relation / edge
+ state
+ provenance
+ scope
+ history / transition
```

or by another established parent already present in the handbook.

For Chapter 10, do not invent a new Commercial Design dimension merely for conceptual symmetry. First try to represent the decision through:

```text
configuration / entitlement
+ payment / value-capture architecture
+ relationship / risk terms
+ selection / allocation rule

+ modifiers / scope
+ state / history / transition
+ evidence / objective / constraints / guardrails
+ governance when authority is material
```

Require a concrete decision-relevant counterexample before expanding that grammar.

Keep these boundaries explicit:

```text
POSITIONING / VALUE
!= COMMERCIAL DESIGN
!= MESSAGE / COPY

COMMERCIAL DESIGN
!= CURRENT COMMERCE STATE / REPRESENTATION

COMMERCIAL DESIGN
!= COMMERCIAL GOVERNANCE
!= EXECUTED COMMERCIAL INSTANCE
```

### Local adaptation extensions

Local adaptation is a bounded extension mechanism, not a country-profile or culture-pack layer. Start with [`skills/marketing-practitioner/adaptations/README.md`](skills/marketing-practitioner/adaptations/README.md) and preserve the existing decision owner.

A proposed local contribution should pass this promotion test:

```text
LOCAL-SPECIFIC MECHANISM
+
MATERIAL DECISION DELTA
+
NO EXISTING OWNER ALREADY FULLY HANDLES IT
=
ADAPTATION CANDIDATE
```

Local evidence, local popularity, or a country-specific observation is not enough by itself. If the existing handbook can already make the correct decision once the scoped task evidence is supplied, keep the material as evidence rather than creating runtime adaptation knowledge.

Do not organize primary runtime knowledge as `vi-VN`, `market-vn`, country packs, or similar noun-first containers. Route by the existing decision owner and keep language, market, geography, audience, channel, category, and time inside the contribution's scope. `LOAD WHEN` refines applicability after the controller has an open decision; it is not activation authority.

Do not infer population behavior from native familiarity, do not let private storage automatically outrank upstream evidence, and do not inherit a broader behavioral claim merely because narrower local evidence is missing. Provider/platform mechanics remain with provider/platform owners; legal requirements remain authoritative external dependencies.

### `routing-index.json` and retrieval scripts

The routing layer is infrastructure, not marketing theory.

Keep:

```text
logical knowledge ID != physical file location
semantic knowledge route != evidence source ID
routing metadata != duplicated handbook prose
```

Do not turn the manifest into a second handbook, scoring engine, taxonomy project, or registry of every small paragraph.

### Evidence ledgers and bibliography

Reference files establish provenance; they do not become runtime rules merely because a source exists.

Do not convert:

```text
source says X
```

into:

```text
agent should always do Y
```

without the missing inference being justified.

For Commercial Design evidence in particular, preserve the estimand and regime. Do not collapse WTP, price perception, observed choice, causal elasticity, conversion, profit, consumer surplus, fairness, retention, and LTV into one outcome family.

---

## Evidence standard

When adding or changing a substantive empirical claim:

1. prefer first-party documentation, primary research, systematic reviews, standards, or strong methodological sources where appropriate;
2. record the source in the relevant bibliography or evidence ledger;
3. state what the evidence actually establishes: capability, description, association, prediction, experiment, review, theory, or implementation detail;
4. preserve material scope: product/surface, market, population, time, account state, delivery regime, commercial regime, or experimental setting;
5. separate direct evidence from interpretation and practitioner inference;
6. keep UNKNOWN when the evidence does not resolve the question.

Do not treat:

- qualitative recurrence as population prevalence;
- correlation as causation;
- attribution as incrementality;
- stated or hypothetical WTP as a revealed preference or optimal price;
- historical price/sales association as causal elasticity by default;
- conversion as profit, retention, or LTV;
- seller-declared or machine-inferred product information as automatically verified truth;
- an exposed ranking signal as a universal writing instruction;
- one recommendation module as the platform's complete ranking system;
- platform guidance as independent proof of effectiveness.

---

## Platform contributions

Platform knowledge is time-sensitive and system-specific.

When updating Facebook, Instagram, LinkedIn, TikTok, X, Google commerce, Amazon, TikTok Shop, Shopee, Etsy, Lazada, or a future justified module:

- identify the exact product/surface/system being discussed;
- prefer current first-party evidence when documenting current capabilities or policies;
- distinguish organic, paid, seller-tool, creator-tool, search, recommendation, moderation, and transaction systems where material;
- preserve country/market and time scope;
- distinguish eligibility, retrieval, relevance, ranking, filtering, sorting, recommendation, presentation, and observed outcome;
- do not infer hidden weights or universal algorithms from public documentation;
- add a new platform only when it adds decision-relevant capability, not merely catalog coverage.

A platform-local finding should stay local unless a concrete cross-platform counterexample shows the shared model is insufficient.

Use [`skills/marketing-practitioner/platforms/README.md`](skills/marketing-practitioner/platforms/README.md) and [`skills/marketing-practitioner/platforms/commerce/README.md`](skills/marketing-practitioner/platforms/commerce/README.md) as human navigation only. Runtime route bindings remain in `routing-index.json`.

---

## Updating the agent skill

`skills/marketing-practitioner/SKILL.md` should remain operational and comparatively compact. Extended conceptual discussion belongs in the handbook or platform modules.

When a knowledge change truly alters how the agent should behave, update `SKILL.md` in the same change. Otherwise leave the controller alone.

Keep runtime resources required by the skill inside `skills/marketing-practitioner/` so they travel with the installed package. Keep evaluation artifacts outside the installable skill under `evals/` and deep pre-implementation research lineage outside runtime under `research/`.

For large indexed knowledge, preserve stable logical route IDs where possible. A heading or physical file may move without requiring the runtime-facing knowledge ID to change.

Human-facing README files may map the repository, explain boundaries, and point to canonical resources. They should not duplicate route-to-heading bindings, evidence ledgers, or substantive chapter prose.

---

## Validation expectations

Validation should match the risk of the change.

- **Level 0:** inspect the rendered/output text and affected links/metadata.
- **Level 1:** verify source scope, affected knowledge section, and any existing evidence/route binding.
- **Level 2:** add or update a targeted regression, smoke case, or adversarial counterexample that reproduces the failure being corrected.
- **Level 3:** require explicit architecture review before broad implementation and validate the claimed cross-cutting failure independently.

Do not create benchmark claims from a static audit or a handful of smoke cases. Report exactly what was executed and what remains unvalidated.

---

## Writing style

Use formal, plain English in repository content.

Prefer:

- explicit distinctions;
- compact invariants where they reduce ambiguity;
- decision-linked guidance;
- clear scope and uncertainty;
- examples only when they resolve a real ambiguity.

Avoid:

- marketing hype about the project itself;
- unnecessary new terminology;
- long tactic lists;
- decorative frameworks;
- duplicated explanation across `SKILL.md`, handbook, platform modules, references, and navigation READMEs.

---

## Pull requests

For non-trivial contributions, a useful pull request should explain:

- the concrete problem or failure being corrected;
- why the current behavior/knowledge is insufficient;
- the evidence or counterexample supporting the change;
- the smallest affected files/sections;
- whether the change is Level 1, 2, or 3;
- whether it changes a rule, heuristic, platform-local fact, routing behavior, or only exposition;
- what validation was actually run;
- what remains unknown.

Keep PRs narrow. Do not bundle unrelated platform research, theory changes, controller changes, and documentation cleanup into one contribution.

A contribution is stronger when it removes ambiguity or fixes a real decision failure with less architecture, not more.
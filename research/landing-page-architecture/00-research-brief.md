# Landing-Page Architecture — Research Brief

Status: research complete; prepared for bounded theory freeze

## Research question

How should an AI marketing practitioner transform already-resolved audience, positioning, message, proof, commercial state, and action intent into a landing-page information and action architecture without relying on template folklore, model prior, or one-size-fits-all CRO rules?

The target is not a universal landing-page template. The target is a bounded decision model for deciding what information must exist, what must precede what, where proof/risk reducers belong, what representation carries each job, how action/forms should be structured, and how the same decision logic survives responsive layouts.

## Why this was opened

The existing runtime can route and write landing-page copy, and Chapter 04 already owns message hierarchy, proof architecture, objections, claim control, reader state, and next action. What remained shallow was page architecture: section formation, information sequence, first-view allocation, proof placement, screenshots/demos, navigation/attention, forms, pricing/comparison representation, and responsive ordering.

That gap matters because a fluent model can generate familiar shapes such as:

```text
hero
→ logo row
→ features
→ testimonials
→ pricing
→ FAQ
→ final CTA
```

without establishing why any section exists or why the order supports the visitor's actual decision.

## Scope

In scope:

- dedicated campaign landing pages;
- product/solution pages when a bounded conversion decision is material;
- demo/sign-up/lead-generation pages;
- pricing/comparison representations when commercial design is already resolved;
- page-level proof, objection, risk, visual, CTA, form, navigation, and responsive allocation;
- page-specific observations that should hand off to the existing diagnosis framework.

Out of scope:

- inventing or reopening positioning without need;
- designing unresolved pricing/packages/terms;
- frontend implementation, CSS systems, design tokens, or component libraries;
- a new CRO controller job;
- a website-wide information architecture framework;
- a fixed page-type taxonomy;
- a fixed awareness or risk ontology;
- a benchmark of specific design patterns.

## Research lines

The synthesis used several evidence classes rather than treating practitioner case studies as universal law:

1. **Accessibility / standards** — meaningful reading sequence and responsive linearization constraints.
2. **UX research** — scanning behavior, visual hierarchy, SaaS plan comparison, discoverability, and information density.
3. **Experienced conversion practitioners** — thought sequence, information hierarchy, friction/anxiety, action clarity, form and navigation hypotheses.
4. **Existing repository theory** — Chapter 04 message/proof ownership, Chapter 05 diagnosis/causality ownership, Chapter 10 commercial-design ownership.

## Initial hypotheses attacked

The following candidate rules were rejected as universal laws:

- every landing page needs the same section set;
- CTA must always be above the fold;
- navigation must always be removed;
- fewer form fields always convert better;
- short copy always wins;
- long copy always wins;
- F/Z scanning patterns should be used as layout recipes;
- testimonials require a dedicated section;
- FAQ is mandatory;
- SaaS heroes require a dashboard screenshot;
- video is inherently stronger than static visual proof;
- mobile should simply stack the desktop layout;
- pricing pages should use a fixed number of plans/cards;
- low scroll depth identifies a long-page problem.

These can be contextual hypotheses or implementation options, but not governing invariants.

## Core finding

Landing-page architecture is best modeled as a bounded specialist transformation:

```text
RESOLVED UPSTREAM STATE
→ DECISION-SUPPORTING PAGE REPRESENTATION
```

The new knowledge does not own the upstream truth. It owns the allocation problem: how to turn decision-relevant state into a page whose information, proof, visuals, actions, and responsive sequence support the current visitor decision.

## Architecture disposition

No new top-level layer, controller job, page primitive, CRO subsystem, or visual-design framework is justified.

A dedicated handbook file is justified because the local knowledge is deep enough to exceed Chapter 04's format note, while remaining downstream of Chapter 04 and bounded by Chapters 05 and 10.

Candidate implementation:

```text
handbook/11-landing-page-architecture.md
```

with addressable `landing-page.*` knowledge routes. The namespace is a physical/JIT knowledge namespace only; it is not a new runtime job or universal marketing ontology.

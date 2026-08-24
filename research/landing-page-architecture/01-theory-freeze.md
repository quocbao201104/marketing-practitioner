# Landing-Page Architecture — Theory Freeze

Status: FROZEN FOR BOUNDED IMPLEMENTATION

Base runtime reviewed: Marketing Practitioner v0.5.1

## Frozen scope

Landing-page architecture is a specialist transformation of resolved upstream state into a decision-supporting page representation.

It does not own positioning, claim truth, causal diagnosis, unresolved commercial design, frontend implementation, or website-wide architecture.

```text
RESOLVED MESSAGE / READER / COMMERCIAL STATE
                  ↓
      PAGE INFORMATION ARCHITECTURE
                  ↓
ORDER / PLACEMENT / REPRESENTATION
ACTION / FORM / RESPONSIVE ALLOCATION
```

## Minimal grammar

The research scaffold contained many useful concepts. After adversarial compression, only seven distinctions are retained as governing runtime knowledge.

### 1. Page job + entry state

Name the bounded decision/action this page must support and preserve the material state at entry:

- traffic or prior-touchpoint source when it changes expectation;
- incoming promise or intent;
- reader state and relevant prior knowledge/exposure;
- already-resolved positioning/message/claim boundaries;
- already-resolved commercial state;
- target action.

Page type and awareness labels may be useful shorthand, but neither is a primitive or oracle.

### 2. Action-ready conditions

Ask what must be understood, believed, verified, or resolved before the target action becomes reasonable for this visitor.

Do not convert this into a numeric information-distance score. The useful distinction is whether a missing uncertainty or requirement can change readiness for the action.

### 3. Information dependency

Order material information by dependency rather than by template convention.

```text
Q1 must be resolved
before Q2 can be interpreted or trusted
before action A becomes reasonable
```

No formal graph object is required. The dependency relation is enough.

### 4. Information / proof / visual allocation

A section is a bounded information job, not a required content type.

Allocate claims, explanations, proof, objections, risk reducers, commercial facts, comparisons, and visuals to the decision point where they are useful.

Keep proof close enough to the claim or decision it supports that the relationship remains clear. Literal adjacency is not mandatory when shared proof supports a broader claim set.

Choose the minimum sufficient carrier for each job: text, screenshot, annotated screenshot, diagram, artifact preview, image, motion/demo, or interaction. A visual must earn its attention cost by explaining, demonstrating, orienting, comparing, or substantiating something material.

### 5. Attention / exploration control

Do not equate navigation with distraction.

An interactive element is useful when it advances the primary decision, resolves a material blocker, or supports legitimate exploration. It becomes a distraction candidate when it does none of those jobs and competes with the bounded page action.

### 6. Action / form architecture

Preserve:

```text
CTA AVAILABILITY ≠ CTA READINESS
```

A visitor who is already ready may need an early action path while the page still supports less-ready visitors through the decision sequence.

For every requested form field, ask why that information is needed now. Legitimate reasons can include transaction, delivery, materially useful qualification, routing/scheduling/compatibility, or authoritative process requirements.

Raw form completion is not the same as qualified demand, revenue, or business value.

### 7. Responsive meaningful allocation

Responsive adaptation preserves the decision dependencies and meaningful reading sequence while allowing the spatial representation to change.

```text
MOBILE ≠ STACKED DESKTOP
```

Small screens reduce simultaneous information capacity; they do not erase material information requirements. Progressive disclosure may reduce simultaneous complexity but must not make decision-critical information materially undiscoverable.

## Ownership boundaries

### Chapter 04 owns

- reader-state analysis;
- message hierarchy;
- claim control;
- proof authority and adequacy;
- objections as message inputs;
- allowed/unsupported claims;
- touchpoint next action.

Chapter 11 consumes those decisions and allocates them on the page.

### Chapter 05 owns

- metric definition;
- symptom versus cause;
- competing explanations;
- causal inference;
- experimentation and treatment effects.

Landing-page observations such as scroll depth, CTA clicks, form abandonment, FAQ use, pricing exits, or security-document clicks are observations, not causes. Route diagnosis to Chapter 05.

### Chapter 10 owns

- unresolved package/configuration decisions;
- pricing metric/tariff/menu;
- commitment/risk terms;
- allocation/eligibility;
- commercial governance.

When commercial state is fixed, Chapter 11 may represent it. It must not reopen or redesign it merely because pricing/comparison appears on the page.

## Anti-folklore invariants

```text
LANDING PAGE ≠ SECTION TEMPLATE
SECTION ≠ CONTENT-TYPE REQUIREMENT
PAGE TYPE ≠ PRIMITIVE
AWARENESS STAGE ≠ ORACLE
CTA AVAILABILITY ≠ CTA READINESS
PROOF ≠ TESTIMONIAL
OBJECTION ≠ FAQ
VISUAL ≠ DECORATION
SCREENSHOT ≠ PROOF BY DEFAULT
NAVIGATION ≠ DISTRACTION BY DEFAULT
FRICTION ≠ BAD BY DEFAULT
FORM CONVERSION ≠ BUSINESS VALUE
MORE INFORMATION ≠ MORE FRICTION
LESS INFORMATION ≠ BETTER UX
MOBILE ≠ STACKED DESKTOP
COMMERCIAL REPRESENTATION ≠ COMMERCIAL DESIGN
BEHAVIORAL OBSERVATION ≠ CAUSAL EXPLANATION
CASE-STUDY LIFT ≠ UNIVERSAL DESIGN LAW
```

## Downgraded concepts

The following remain useful as examples, prompts, or contextual heuristics only:

- page-type taxonomies;
- awareness-stage taxonomies;
- fixed risk taxonomies;
- exact hero recipes;
- exact section sequences;
- attention-ratio targets;
- fixed CTA placement;
- fixed form length;
- fixed navigation treatment;
- exact plan-card counts;
- left/right hero conventions;
- fixed mobile ordering;
- lift percentages from individual case studies.

## Counterexample survival

Each retained distinction survived removal attack because omitting it can create a concrete decision error:

| Removed distinction | Concrete failure |
| --- | --- |
| Page job / entry state | Paid-ad promise lands on a generic hero and breaks expectation/message continuity |
| Action-ready conditions | High-commitment enterprise CTA appears before security/implementation proof; low-risk download is over-explained |
| Information dependency | Pricing/terms appear before the visitor understands what is included; mechanism arrives before category/orientation |
| Information allocation | Sensitive-form trust evidence is detached from the collection point; a giant screenshot supports no claim |
| Attention/exploration | Legitimate security/comparison path is removed as a supposed distraction |
| Action/form | Fields are removed to raise raw CVR but destroy qualification/routing value |
| Responsive meaningful allocation | Desktop two-column meaning linearizes into an incoherent mobile order |

## Evidence-strength discipline

### Durable / governing

Use as broad constraints:

- meaningful reading order where sequence affects meaning;
- semantic priority should drive visual hierarchy rather than the reverse;
- observations do not establish causes;
- fixed commercial state is not reopened by its representation;
- decision-critical information must remain sufficiently discoverable.

### Conditional practitioner guidance

Treat as hypotheses conditioned on traffic, motivation, risk, action, device, and page job:

- CTA placement;
- navigation removal;
- short versus long copy;
- form length;
- progressive disclosure;
- precise proof placement;
- attention-ratio tactics.

### Examples only

Do not promote to rules:

- any specific lift percentage;
- exact number of fields, sections, plans, or CTAs;
- exact hero layout;
- exact button/color treatment;
- any one tested page sequence.

## Architecture adjudication

The architecture gate is NOT cleared.

No evidence requires a new controller job, landing-page primitive, web-design layer, CRO subsystem, journey object, or visual-design ontology. The correct correction is bounded specialist knowledge plus JIT routing.

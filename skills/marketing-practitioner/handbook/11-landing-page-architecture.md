# 11 — Landing-Page Architecture

## 1. Scope: compile resolved strategy into a decision-supporting page

Use this chapter when the open decision is not merely what to say, but how already-resolved message, proof, reader state, commercial facts, and action intent should be allocated across a landing page.

This is a specialist representation layer, not a new marketing architecture.

```text
RESOLVED UPSTREAM STATE
→ PAGE INFORMATION / ACTION ARCHITECTURE
→ AUDIENCE-FACING PAGE
```

Chapter 04 still owns message hierarchy, claim control, proof adequacy, objections, and reader-state reasoning. Chapter 05 owns diagnosis, causality, and experimentation. Chapter 10 owns unresolved commercial design. This chapter consumes their decision-relevant outputs when they are already resolved.

Do not use this chapter to create a universal landing-page template. A section should exist because it performs a material information job for the current visitor decision, not because similar pages commonly contain it.

Keep:

```text
LANDING PAGE ≠ SECTION TEMPLATE
PAGE ARCHITECTURE ≠ VISUAL DECORATION
COMMERCIAL REPRESENTATION ≠ COMMERCIAL DESIGN
BEHAVIORAL OBSERVATION ≠ CAUSAL EXPLANATION
```

The same reasoning can apply to a campaign landing page, product/solution page, demo-request page, sign-up page, or pricing/comparison surface when a bounded page decision is material. Page-type labels are shorthand, not primitives.

---

## 2. Page job, entry state, and action readiness

Before arranging sections, freeze the page's actual job.

Ask:

```text
What must this page help this visitor decide, understand, verify, or do now?
```

Preserve only entry state that can change the page decision:

- traffic source or prior touchpoint when it changes expectation;
- incoming promise, query, or intent and its provenance when material;
- reader state, prior exposure, and relevant prior knowledge;
- already-resolved positioning and message;
- allowed, qualified, unknown, or forbidden claims;
- available proof and its authority/provenance;
- already-resolved commercial state;
- target action and what happens immediately after it.

Do not reopen upstream positioning or commercial design merely because a page contains a headline, price, trial, plan, discount, or CTA.

### Action-ready conditions

A visitor can see an action before being ready to take it. Preserve:

```text
CTA AVAILABILITY
≠
CTA READINESS
```

For the target action, ask what must be understood, believed, verified, or resolved before taking that action becomes reasonable in the current context.

Examples:

- a low-risk resource download may require little beyond relevance, value, and action clarity;
- a developer tool may require mechanism and compatibility evidence before sign-up;
- an enterprise demo request may require security, implementation, authority, or fit information;
- a purchase may require material commercial terms and delivery/return conditions.

Do not turn these examples into awareness stages or a risk taxonomy. Retain only blockers that can change the current action.

A useful qualitative idea is **information distance**: how much material state separates the visitor's current understanding from action readiness. It is not a score and does not imply that more content is always better.

```text
MORE INFORMATION ≠ MORE FRICTION
LESS INFORMATION ≠ BETTER UX
```

Relevant information can reduce decision friction when it resolves uncertainty that would otherwise block action.

---

## 3. Information dependency and section formation

Do not decide section order from a familiar page pattern. Order information by dependency.

For each material question, ask whether its answer is needed before another question can be interpreted, believed, or acted on.

```text
Q1: What is this / is this relevant?
        ↓
Q2: How does it create the claimed value?
        ↓
Q3: Can I believe it in my context?
        ↓
Q4: What risk, effort, or condition remains?
        ↓
ACTION
```

This is an illustration, not a canonical sequence. A visitor already familiar with the product may need price/terms immediately. A novel high-risk product may require mechanism and proof much earlier. A page reached from a precise branded query may have less orientation work than a cold campaign page.

### Sections emerge from information jobs

Use:

```text
SECTION
= a bounded cluster of information that performs one coherent decision-support job
```

A section may legitimately combine text, screenshot, proof, objection resolution, and CTA when all of them resolve the same decision question. Do not split them into separate `features`, `screenshots`, `testimonials`, or `CTA` sections merely because a template expects those content types.

Good section jobs can include:

- orienting the visitor and preserving incoming promise;
- establishing the primary value in the current context;
- explaining a material mechanism;
- demonstrating a capability;
- establishing fit or compatibility;
- resolving a material objection or risk;
- comparing alternatives or plans;
- clarifying implementation or commercial consequence;
- enabling the next action.

These are derived jobs, not a required checklist.

### First view / hero

Treat the first view as the first decision checkpoint, not a fixed component bundle.

It should resolve enough of the earliest material question to prevent a mismatch between the visitor's expectation and the page. Depending on entry state, it may need orientation, category, core value, offer confirmation, product evidence, proof, or an action path.

Do not require by default:

```text
eyebrow + headline + subhead + dashboard screenshot + two CTAs + logo row
```

Every element must earn its place through the first-view information job.

Practitioner guidance supports organizing landing-page information around the questions prospects actually need answered, but does not establish one universal question order [LP03][LP04].

---

## 4. Proof, objections, risk, and commercial clarity

Chapter 04 determines whether a claim is supportable and what proof is available. This chapter decides where that proof belongs on the page.

### Proof placement follows the supported decision

Use:

```text
CLAIM OR MATERIAL DOUBT
↓
REQUIRED EVIDENCE / EXPLANATION
↓
BEST AVAILABLE SUPPORT
↓
PLACEMENT WHERE THE RELATIONSHIP REMAINS CLEAR
```

Keep proof close enough to the claim or decision it supports that the visitor does not have to reconstruct the relationship. Literal adjacency is not mandatory when shared credibility evidence legitimately supports a broader set of claims.

Do not equate proof with testimonials.

```text
PROOF ≠ TESTIMONIAL
```

Depending on the claim, stronger support may be:

- observable product behavior;
- an actual demonstration;
- an annotated product state;
- measured performance with method/scope;
- customer evidence with relevant context;
- independent validation;
- contractual or operational commitment;
- a transparent limitation that makes the promise precise.

### Objections are not automatically FAQ items

```text
OBJECTION ≠ FAQ
```

If a common objection materially blocks the main decision, resolve it where it becomes relevant. A question about compatibility may belong in the fit/mechanism section; a security concern may belong near data-entry or enterprise adoption content; a material refund/cancellation term may belong near the commercial choice.

Use FAQ or expandable detail for genuinely secondary, conditional, or long-tail questions that should not dominate the main sequence. Do not use FAQ to patch missing core information architecture.

### Risk reduction is contextual

Do not instantiate a universal risk taxonomy. Ask what could make the current action unreasonable or unsafe in this context and retain only material concerns.

Possible examples include performance, fit, implementation effort, privacy/security, organizational approval, economic commitment, commercial lock-in, or uncertainty about what happens after the action. These are prompts, not required categories.

### Commercial facts

When pricing/packages/terms are fixed, represent the decision-relevant state accurately and visibly enough for the visitor's choice. Do not redesign a plan, price, trial, eligibility rule, guarantee, cancellation policy, or allocation regime inside page architecture.

If those conditions are still open, route to Chapter 10.

---

## 5. Visual and attention allocation

Visual hierarchy should express semantic priority rather than determine it.

```text
DECISION PRIORITY
→ INFORMATION PRIORITY
→ VISUAL PRIORITY
→ size / contrast / spacing / grouping / placement
```

NN/g's eye-tracking research shows that F-shaped scanning is one observed pattern and can reflect weak formatting/hierarchy; it is not a layout recipe [LP02]. Do not design a page around a folk gaze path.

### Choose visual representation by job

A visual is not proof merely because it depicts the product.

For each material question, choose the minimum sufficient carrier:

- **text** when wording is the clearest carrier;
- **screenshot** when one product state explains or demonstrates the claim;
- **annotated screenshot** when the material state would otherwise be hard to locate;
- **diagram** when relationships, mechanism, or flow matter more than exact UI;
- **artifact/output preview** when the deliverable itself is decision-relevant;
- **image/photo** when context, scale, or use state is material;
- **motion/demo** when transition, timing, interaction, or sequence is itself the information;
- **interactive representation** only when interaction materially improves evaluation.

```text
VISUAL ≠ DECORATION
SCREENSHOT ≠ PROOF BY DEFAULT
```

A giant dashboard screenshot that does not make the supported claim easier to understand is information-poor even when it is authentic.

When a screenshot is useful, prefer the smallest state that demonstrates the material capability. Crop, frame, or annotate when doing so improves interpretation without hiding material context.

### Motion earns its attention cost

Motion strongly attracts attention. Use it when it explains a meaningful transition or interaction that static representation cannot communicate as efficiently. Do not add animation merely to make the page feel premium.

### Navigation and competing actions

Do not apply `remove navigation` as a universal landing-page law.

An interactive element earns its place when it:

1. advances the primary decision;
2. resolves a material blocker; or
3. supports legitimate exploration required by the page job.

If it does none of those and competes with the bounded action, it is a distraction candidate.

```text
NAVIGATION ≠ DISTRACTION BY DEFAULT
```

A dedicated campaign page may legitimately suppress broad exploration. A homepage, product/solution page, pricing surface, or complex evaluation page may legitimately need navigation, security docs, comparison paths, or supporting content.

---

## 6. Action and form architecture

A CTA is not just button copy. Preserve the action state:

```text
ACTION IDENTITY
What am I doing?

IMMEDIATE CONSEQUENCE
What happens after I act?

COMMITMENT
What am I agreeing to?

REVERSIBILITY
Can I undo, cancel, or leave?

NEXT STATE
Trial, checkout, calendar, account creation, download, sales process, or another state?
```

Repeated CTA placement should follow meaningful readiness boundaries rather than a fixed section count. After a material uncertainty has been resolved, another action opportunity may be reasonable.

### Form fields require a reason now

For every field, ask:

```text
Why is this information needed at this step?
```

Potentially legitimate reasons include:

- required to complete the transaction;
- required to deliver the requested value;
- required for materially useful qualification;
- required for routing, scheduling, or compatibility;
- required by an authoritative process.

If none applies, the field is a removal candidate.

But do not infer:

```text
FEWER FIELDS = BETTER FORM
```

CXL documents counterexamples where removing fields reduced conversion and emphasizes balancing form ease with the value of collected information and lead qualification [LP05]. Treat those examples as counterevidence to the universal law, not proof that longer forms are better.

Keep:

```text
FORM CONVERSION ↑
≠ QUALIFIED DEMAND ↑
≠ REVENUE ↑
≠ BUSINESS VALUE ↑
```

If qualification is intentional, evaluate the downstream decision objective rather than optimizing raw submission count in isolation.

A necessary field can still create avoidable anxiety or interaction friction when the visitor does not understand why it is requested, how it will be used, or what format is expected. Put explanations close to the collection point when the reason is not self-evident.

Multi-step forms and progressive disclosure are implementation options. They can change perceived commitment and information burden, but are not universally superior to single-step forms.

---

## 7. Responsive meaningful allocation

Responsive design is not simply desktop layout collapsed into one column.

```text
RESPONSIVE DESIGN
= preserve decision meaning
+ adapt spatial representation
```

When order affects meaning, preserve at least one correct programmatic reading sequence [LP01]. More than one sequence can be valid when relative order does not change meaning.

For each multi-column or composite section, ask:

```text
If this section is linearized,
what order preserves the information dependency?
```

Example:

```text
Desktop:
[mechanism explanation] | [product evidence]

Possible mobile sequence:
mechanism explanation
→ product evidence
→ proof
→ CTA
```

Do not force that sequence when the visual evidence can be understood independently or another order preserves the same meaning.

### Small screen = less simultaneous information, not necessarily less required information

```text
SMALL SCREEN
≠ FEWER MATERIAL REQUIREMENTS
```

Mobile often requires serialization, stronger grouping, shorter simultaneous views, and clearer information scent. It does not justify removing decision-critical proof, terms, compatibility, or limitations merely to make the interface cleaner.

### Progressive disclosure

Use disclosure to reduce simultaneous complexity while preserving discoverability.

Appropriate candidates can include long technical detail, secondary specifications, or conditional long-tail questions. Do not hide a material limitation, core proof, key eligibility rule, critical feature difference, or other decision-changing state merely because it makes the page denser.

```text
PROGRESSIVE DISCLOSURE
≠ INFORMATION REMOVAL
```

---

## 8. Pricing and comparison representation

Use this section only when commercial design is already sufficiently resolved and the page must help the visitor understand or choose among those fixed states.

Chapter 10 remains the owner when package, pricing metric, price menu, terms, eligibility, or commercial governance is still open.

### Comparison serves a choice

Do not treat a comparison table as an exhaustive feature inventory.

Ask:

```text
Which alternatives are actually being compared?
Which differences can change the choice?
Which terms or limits require explanation?
How can those differences be compared with low search/memory burden?
```

Baymard's SaaS usability research found that plan matrices can dominate users' subscription evaluation and that long, unorganized feature lists make critical features difficult to find [LP06][LP07]. Their findings support grouping, ordering, preserving comparison context, and improving scannability in those studied environments; they do not establish a universal plan-matrix template.

Useful representation choices can include:

- group related differences under meaningful headings;
- prioritize material differences;
- preserve plan identity/context during long comparisons;
- explain unfamiliar terms where needed;
- make feature-to-plan relationships easy to trace;
- progressively disclose secondary details without hiding decision-critical information.

On narrow screens, preserve the **comparison job** even if the desktop table representation is no longer suitable.

```text
SAME DECISION JOB
≠ SAME COMPONENT AT EVERY VIEWPORT
```

---

## 9. Landing-page observation and diagnosis boundary

Page behavior can identify where to investigate. It does not identify the cause by itself.

Possible observations include:

- low or changing scroll depth;
- CTA click distribution;
- form starts, errors, hesitation, or abandonment;
- repeated plan comparison;
- FAQ/accordion usage;
- exits to security, pricing, documentation, or support;
- device-specific differences;
- changes after a page treatment.

Do not infer directly:

```text
LOW SCROLL → PAGE TOO LONG
FORM ABANDONMENT → REMOVE FIELDS
FAQ CLICKS → FAQ IS WORKING
SECURITY LINK CLICKS → LINK IS A DISTRACTION
CONVERSION DROP → REWRITE COPY
```

Instead route to Chapter 05:

```text
OBSERVATION
→ COMPETING EXPLANATIONS
→ DISCRIMINATING CHECK
→ TREATMENT HYPOTHESIS
→ TEST WHEN CAUSAL EVIDENCE IS NEEDED
```

For example, repeated clicks to a security document could mean distraction, missing trust evidence on the page, audience mismatch, or a legitimate required approval step. The observation alone cannot choose among them.

Keep individual optimization case-study lifts scoped to their tested treatment/population. They are examples of possible effects, not universal design laws [LP04][LP05][LP08].

---

## 10. Compact page-architecture record

For consequential page design, a compact decision record can contain only the fields that materially change the page:

```text
PAGE JOB
ENTRY PROMISE / INTENT
READER STATE
RESOLVED MESSAGE / CLAIM BOUNDARIES
RESOLVED COMMERCIAL STATE
TARGET ACTION + NEXT STATE
ACTION-READY CONDITIONS
MATERIAL INFORMATION DEPENDENCIES
PROOF / RISK / OBJECTION ALLOCATION
VISUAL JOBS
NAVIGATION / EXPLORATION NEED
FORM / QUALIFICATION NEED
RESPONSIVE ORDER CONSTRAINTS
MATERIAL UNKNOWNS
```

Do not instantiate every field for a simple page or copy transformation.

---

## 11. Anti-folklore invariants

Keep these distinctions when they prevent a material page error:

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

Do not turn page examples, practitioner preference, or one A/B test into a universal layout formula. The governing standard is minimum sufficient decision support for the current visitor state, action, evidence, and constraints.

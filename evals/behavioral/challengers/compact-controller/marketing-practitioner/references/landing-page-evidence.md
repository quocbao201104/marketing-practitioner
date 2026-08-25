# Landing-Page Architecture Evidence

This ledger supports Chapter 11. It distinguishes durable constraints and usability findings from practitioner heuristics and individual conversion tests.

## [LP01] W3C — WCAG 2.2, Meaningful Sequence

Source: https://www.w3.org/WAI/WCAG22/Understanding/meaningful-sequence

Use for:
- preserving at least one correct reading sequence when order affects meaning;
- responsive linearization and accessibility boundaries;
- recognizing that multiple correct orders can exist when relative order does not affect meaning.

Do not use for:
- a universal landing-page section order;
- conversion claims about a specific layout.

Evidence class: standards / strong boundary evidence.

## [LP02] Nielsen Norman Group — F-Shaped Pattern of Reading on the Web

Source: https://www.nngroup.com/articles/f-shaped-pattern-reading-web-content/

Use for:
- distinguishing observed scanning behavior from a layout prescription;
- the warning that F-shaped scanning can reflect weak hierarchy/formatting;
- grounding semantic-priority-to-visual-hierarchy reasoning.

Do not use for:
- a fixed left/right hero layout;
- a universal gaze path;
- a conversion formula.

Evidence class: repeated UX / eye-tracking evidence.

## [LP03] Unbounce — Information Hierarchy 101

Source: https://unbounce.com/landing-pages/information-hierachy-helps-you-convert-and-delight/

Use for:
- practitioner framing of page architecture around prospect questions and logical order;
- distinguishing information hierarchy from visual hierarchy;
- hypothesis generation about unnecessary information.

Do not use for:
- one universal question order;
- required section templates;
- generalized causal lift.

Evidence class: experienced-practitioner synthesis.

## [LP04] MarketingExperiments — Eye-path vs. Thought Sequence

Source: https://marketingexperiments.com/conversion-marketing/lpo-eyepath-thought-conversion

Use for:
- practitioner framing of thought sequence versus eye-path alone;
- examples where value, supporting proof, action, and next-step clarity were deliberately sequenced;
- counterevidence to fixed placement folklore.

Do not use for:
- a universal rule that forms belong at the bottom;
- a universal rule that testimonials belong next to forms;
- any one treatment order as general law.

Evidence class: practitioner synthesis plus contextual page analysis/test lineage.

## [LP05] CXL — Should You Really Reduce Form Fields?

Source: https://cxl.com/blog/reduce-form-fields/

Use for:
- rejecting `fewer fields always convert better` as a universal law;
- examples where removed fields changed conversion unexpectedly;
- balancing interaction cost, perceived value, qualification, and downstream information needs.

Do not use for:
- `longer forms are better`;
- a universal optimal form length;
- transport of individual case lifts to new contexts.

Evidence class: practitioner synthesis with case evidence.

## [LP06] Baymard — SaaS UX: Improve the Scannability of the Plan Matrix

Source: https://baymard.com/blog/saas-scannability-plan-matrix

Use for:
- evidence that SaaS plan matrices can be central to subscription evaluation;
- observed difficulty with long, unorganized feature lists;
- grouping, ordering, preserving comparison context, scaling, and row traceability as usability guidance in the studied population;
- risk of users missing critical features and drawing incorrect conclusions.

Do not use for:
- mandatory plan matrices on all pages;
- fixed pricing-card counts;
- unresolved commercial design decisions.

Evidence class: large-scale usability research.

## [LP07] Baymard — SaaS Website UX Fixes / SaaS Benchmark

Sources:
- https://baymard.com/blog/saas-website-ux-best-practices
- https://baymard.com/blog/saas-benchmark

Use for:
- SaaS page/plan evaluation behavior;
- discoverability and progressive-disclosure boundaries;
- the importance of making service/product UI and feature information understandable enough for evaluation.

Do not use for:
- a universal SaaS landing-page template;
- a rule that raw screenshots always improve persuasion;
- hiding material state in the name of clean design.

Evidence class: usability research / benchmark-derived guidance.

## [LP08] MarketingExperiments — Friction, Anxiety, and Offer Optimization Corpus

Representative sources:
- https://marketingexperiments.com/value-proposition/optimizing-landing-pages-increase-148
- https://marketingexperiments.com/value-proposition/overcoming-value-inhibitors
- https://marketingexperiments.com/value-proposition/optimizing-forms-increase-perceived-value

Use for:
- practitioner prompts around motivation, value, friction, anxiety, and action sequence;
- treating friction/risk as contextual rather than mechanically minimizing them;
- generating testable hypotheses about risk reducers and action clarity.

Do not use for:
- universal numeric coefficients;
- the Conversion Sequence as a portable causal law;
- fixed risk categories;
- universal placement rules derived from individual lifts.

Evidence class: experienced-practitioner framework plus contextual tests.

## Evidence interpretation rule

```text
PRACTITIONER CASE / A-B LIFT
≠ UNIVERSAL DESIGN LAW
```

Use individual tests as evidence that a folk rule can fail, or as a scoped result in the tested context. Do not infer that the inverse treatment is universally superior.

# Landing-Page Architecture — Evidence Ledger

Status: evidence ledger for bounded runtime knowledge

This ledger distinguishes standards/UX evidence from practitioner heuristics and case-specific conversion results. A source can support a useful design hypothesis without supporting a universal law.

## Evidence classes

- **A — standard / strong boundary evidence:** suitable for durable constraints within its scope.
- **B — repeated UX / usability evidence:** suitable for robust design guidance with population/context caveats.
- **C — experienced-practitioner synthesis:** useful for decision heuristics and hypothesis generation, not universal causal law.
- **D — individual case/test:** example or local evidence only unless independently replicated and transferable.

---

## [LP01] W3C — WCAG 2.2, Meaningful Sequence

Class: A

Source:
https://www.w3.org/WAI/WCAG22/Understanding/meaningful-sequence

Supports:

- when content sequence affects meaning, at least one correct reading sequence must be programmatically determinable;
- responsive/spatial rearrangement must not destroy required semantic order;
- more than one reading order can be correct when relative ordering does not change meaning.

Does not establish:

- a universal landing-page order;
- that every visual layout must match one exact DOM sequence;
- conversion effects of any specific section placement.

Runtime implication:

```text
RESPONSIVE ADAPTATION
must preserve meaningful dependency when order changes meaning.
```

---

## [LP02] Nielsen Norman Group — F-Shaped Pattern of Reading on the Web

Class: B

Source:
https://www.nngroup.com/articles/f-shaped-pattern-reading-web-content/

Supports:

- users scan rather than fully read many web pages;
- the F-pattern is one of multiple observed scan patterns;
- poor hierarchy/formatting can encourage inefficient F-shaped scanning;
- designers should not treat F-shape as a page-layout recipe.

Does not establish:

- a fixed left/right hero layout;
- one universal gaze path;
- a conversion-optimal placement formula.

Runtime implication:

```text
SEMANTIC PRIORITY
→ VISUAL HIERARCHY
```

rather than designing around a folk gaze pattern.

---

## [LP03] Unbounce — Information Hierarchy 101

Class: C

Source:
https://unbounce.com/landing-pages/information-hierachy-helps-you-convert-and-delight/

Supports:

- organize landing-page information around the prospect's questions;
- answer those questions in a logical order;
- remove information that does not address a real decision/question;
- distinguish information hierarchy from its visual implementation.

Does not establish:

- a single natural order for all visitors;
- one required section taxonomy;
- causal lift for the general hierarchy framework.

Runtime implication:

Use question/dependency ordering as a practitioner heuristic constrained by the actual entry state and target action.

---

## [LP04] MarketingExperiments — Eye-path vs. Thought Sequence

Class: C/D

Source:
https://marketingexperiments.com/conversion-marketing/lpo-eyepath-thought-conversion

Supports:

- page optimization can be framed around thought sequence rather than eye-path alone;
- value, supporting proof, and action can require deliberate sequencing;
- explaining what happens after action can reduce uncertainty in a specific page context.

Does not establish:

- that forms belong at the bottom of all pages;
- that testimonials should always be next to forms;
- that the analyzed treatment order generalizes universally.

Runtime implication:

Treat section order and proof/action placement as dependency hypotheses, not fixed locations.

---

## [LP05] CXL — Should You Really Reduce Form Fields?

Class: C/D

Source:
https://cxl.com/blog/reduce-form-fields/

Supports:

- number of form fields is not the only determinant of form friction;
- removing fields can reduce conversion when the removed fields were useful/engaging in a tested context;
- form design should balance ease, value exchange, qualification, and downstream data needs.

Does not establish:

- a universal optimal form length;
- that longer forms outperform shorter forms;
- a causal rule transferable across offers/populations.

Runtime implication:

```text
FIELD COUNT
≠ FRICTION OR BUSINESS VALUE BY ITSELF
```

Each field must have a decision-relevant reason for being requested now.

---

## [LP06] Baymard — SaaS UX: Improve the Scannability of the Plan Matrix

Class: B

Source:
https://baymard.com/blog/saas-scannability-plan-matrix

Supports:

- SaaS users can spend substantial decision time in plan matrices;
- long, unorganized feature lists create scanning and comparison burden;
- grouping related features, ordering groups, preserving context while scrolling, and improving row traceability can make comparison easier;
- users can overlook decision-critical features and draw incorrect conclusions when information is hard to locate.

Does not establish:

- that every landing page requires a comparison matrix;
- a fixed pricing-card count;
- a universal plan architecture.

Runtime implication:

Comparison representations should expose material differences with low memory/search burden; representation does not own the underlying commercial design.

---

## [LP07] Baymard — SaaS Website UX Fixes / SaaS Benchmark

Class: B

Sources:
https://baymard.com/blog/saas-website-ux-best-practices
https://baymard.com/blog/saas-benchmark

Supports:

- plan matrices and page design are material parts of SaaS purchase decisions in the tested populations;
- progressive disclosure can help scanning when detailed information remains discoverable;
- missing or hard-to-find feature information can delay or prevent plan evaluation;
- actual service UI/experience can be important evidence for evaluating digital products.

Does not establish:

- one universal SaaS landing-page template;
- that a raw dashboard screenshot is always useful proof;
- that progressive disclosure should hide material conditions.

Runtime implication:

```text
PROGRESSIVE DISCLOSURE
≠ INFORMATION REMOVAL
```

and product visuals should answer a material question rather than decorate a template.

---

## [LP08] MarketingExperiments — Optimization / Friction and Anxiety corpus

Class: C/D

Representative sources:
https://marketingexperiments.com/value-proposition/optimizing-landing-pages-increase-148
https://marketingexperiments.com/value-proposition/overcoming-value-inhibitors
https://marketingexperiments.com/value-proposition/optimizing-forms-increase-perceived-value

Supports:

- visitor motivation, perceived value, friction, and anxiety can all matter to conversion decisions;
- friction should be analyzed rather than reduced mechanically;
- risk/anxiety reducers should respond to the actual concern and action point;
- local treatments should be tested as hypotheses.

Does not establish:

- the numerical Conversion Sequence as a portable causal law;
- universal coefficients;
- a fixed list of risk categories;
- universal placement rules from individual case lifts.

Runtime implication:

Use risk/friction as decision prompts, not a new ontology or scoring formula.

---

## Synthesis constraints

The ledger supports the following durable runtime stance:

```text
PAGE ARCHITECTURE
= conditional decision-support allocation
not a section template
```

High-confidence boundaries come from accessibility, UX research, and existing repository ownership. Practitioner sources inform the shape of decision questions and counterexamples, while individual lift percentages remain local evidence only.

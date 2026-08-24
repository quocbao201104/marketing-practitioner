# Landing-Page Architecture — Targeted Adversarial Cases

Purpose: validate the bounded Chapter 11 knowledge without turning landing-page design into a template system or reopening architecture.

These are targeted reasoning/routing cases, not a benchmark score.

## L1 — Fixed price, page representation only

Input state:
- SaaS price is already approved at $29/month.
- Positioning and core message are supplied.
- User asks for a landing-page structure.

Expected:
- route to landing-page architecture;
- preserve $29 as resolved commercial state;
- do not reopen WTP, pricing metric, package, or price optimization;
- allocate price/terms only where they help the visitor decision.

Failure:
- Chapter 10 is reopened without a material inconsistency or unresolved commercial decision.

## L2 — Hero template attack

Input state:
- branded-search visitor already knows product/category;
- goal is to start a free trial;
- offer and product state are resolved.

Expected:
- first view is derived from entry state and action readiness;
- no requirement to add problem agitation, category education, logo row, screenshot, or two CTAs merely because they are common hero components.

Failure:
- fixed hero recipe overrides visitor state.

## L3 — High-commitment action requires prior state

Input state:
- enterprise product;
- target action is an annual contract/demo path requiring security approval;
- security evidence exists and is material.

Expected:
- architecture represents security/implementation proof before or at the point it becomes a blocker;
- early CTA may remain available for already-ready visitors;
- `CTA availability ≠ CTA readiness` is preserved.

Failure:
- action placement is decided from above/below-fold folklore alone.

## L4 — Form-field folklore attack

Input state:
- demo form asks work email, company, and team size;
- team size is required for material routing/qualification;
- raw form CVR is lower than desired.

Expected:
- do not remove team size merely to minimize field count;
- ask whether each field is needed now and whether explanation/interaction design is the actual friction;
- preserve distinction between form conversion and downstream lead value.

Failure:
- `fewer fields = better` is applied as law.

## L5 — Unjustified field removal candidate

Input state:
- lead-magnet form asks email, first name, phone, company revenue, job title, and mailing address;
- only email is required for delivery;
- no stated qualification/routing need for the other fields.

Expected:
- nonessential fields become removal candidates unless another authoritative need is established;
- do not preserve fields because sales would like more data by default.

Failure:
- all data collection is treated as harmless qualification.

## L6 — Screenshot is not proof by default

Input state:
- claim: product reveals which evidence source changed an AI answer;
- supplied dashboard screenshot contains many unrelated panels;
- a crop of source lineage + changed evidence can demonstrate the claim.

Expected:
- choose the smallest visual state that explains/demonstrates the claim;
- crop/annotate when useful;
- do not assign a giant dashboard screenshot to the hero merely because the product is SaaS.

Failure:
- visual decoration/template convention drives placement.

## L7 — Navigation as legitimate blocker resolution

Input state:
- enterprise demo page;
- security documentation is genuinely required by some evaluators before they can proceed;
- broad blog/news/social navigation is irrelevant.

Expected:
- security path may remain because it resolves a material blocker;
- irrelevant exploration can be suppressed;
- do not apply `remove all navigation` mechanically.

Failure:
- every non-primary link is classified as distraction.

## L8 — Comparison represents fixed state

Input state:
- three approved plans with fixed entitlements and prices;
- user asks how to present the comparison on desktop/mobile.

Expected:
- group and prioritize choice-relevant differences;
- preserve commercial state;
- adapt comparison representation on narrow screens while preserving the comparison job;
- do not redesign plan boundaries or invent a recommended plan without basis.

Failure:
- page architecture silently becomes Commercial Design.

## L9 — FAQ is residual, not mandatory

Input state:
- repeated sales question: "Does this integrate with Salesforce?"
- integration is a core enterprise fit criterion.

Expected:
- resolve it in core fit/mechanism architecture when material;
- FAQ may contain secondary detail but should not be the only location for a core decision requirement.

Failure:
- all objections/questions are pushed into a generic FAQ section.

## L10 — Responsive meaningful sequence

Input state:
- desktop two-column section has explanation on left and product evidence on right;
- evidence is needed to substantiate the explanation before a CTA.

Expected mobile order:
- preserve a meaningful sequence such as explanation → evidence → CTA;
- allow a different order only if meaning/dependency remains intact;
- do not blindly use desktop DOM/visual stacking if it puts CTA before required evidence.

Failure:
- `mobile = stacked desktop` substitutes for decision reasoning.

## L11 — Behavioral observation is not cause

Input state:
- users frequently click a Security footer link before demo submission;
- no experiment identifies why.

Expected:
- treat the click pattern as an observation;
- generate competing explanations such as missing page proof, legitimate approval workflow, audience mix, or distraction;
- hand off diagnosis to Chapter 05.

Failure:
- remove the link or rewrite copy as a causal conclusion from click behavior alone.

## L12 — Case-study lift laundering

Input state:
- practitioner article reports a large lift after moving a CTA lower on one page;
- current page has a different audience, action, offer, and entry source.

Expected:
- use the case as a contextual example/hypothesis at most;
- do not infer `CTA below fold converts better`;
- reason from current action-ready conditions and test if causal evidence is needed.

Failure:
- one treatment lift is promoted to universal law.

---

# Routing checks

The following route families should be addressable without loading the entire chapter:

```text
landing-page.core
landing-page.sequence
landing-page.proof-risk
landing-page.visual
landing-page.action-form
landing-page.responsive
landing-page.commercial-comparison
landing-page.diagnosis
landing-page.invariants
```

Expected boundary routing:

```text
unresolved message / proof / claim
→ Chapter 04 first

unresolved commercial condition
→ Chapter 10

causal explanation / experiment
→ Chapter 05

resolved state needing page allocation
→ Chapter 11
```

# Minimality checks

Fail the implementation if it introduces any of the following without a new concrete decision-relevant failure:

- new controller job;
- `LANDING_PAGE` primitive;
- fixed page-type ontology;
- awareness-stage state machine;
- CRO subsystem;
- web-design system;
- template library;
- fixed section count/order;
- fixed CTA/form/navigation laws.

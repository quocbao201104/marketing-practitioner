# Copywriting Core — Theory Freeze

Status: **FROZEN FOR BOUNDED INTEGRATION**

Research synthesis: `01-cross-ss-synthesis.md`

Frozen baseline:

```text
main
cb262967d4700982946731f96f615923c757133d
```

---

## 1. Frozen research question

> What decision capabilities must Marketing Practitioner add or deepen so that an agent can move from sufficiently grounded strategy and evidence to professional copy without relying on fixed formulas, unsupported persuasion tactics, or prose polish that changes meaning?

The target is not a universal theory of advertising, a library of copywriting templates, or a replacement for customer research, positioning, commercial design, content-environment reasoning, landing-page architecture, email architecture, or causal diagnosis.

---

## 2. Frozen capability model

The copywriting core consists of six decision capabilities:

```text
C1 PERSUASION DIAGNOSIS
What reader-state / decision barrier is material,
and can communication legitimately influence it?

C2 PERSUASIVE ROUTE
What evidence-grounded angle / concept / hook
should organize the communication?

C3 ARGUMENT PROGRESSION
What must change next in the reader's decision state,
and what dependencies constrain sequence?

C4 PERSUASIVE CLOSURE
What belief is sufficiently warranted,
what uncertainty / risk remains,
and what commitment is justified?

C5 EXPRESSION CRAFT
How should already-authorized meaning be realized
with minimum unnecessary interpretive work?

C6 EDITING / VOICE REPAIR
What material defect exists in current expression,
what is the smallest sufficient repair,
and what must survive it?
```

Two application layers consume those capabilities:

```text
A1 SHORT-FORM CONSTRAINED REALIZATION
A2 WEB / LONG-FORM DECISION-SUPPORT ARCHITECTURE
```

The model is dependency-based. It is not a mandatory six-step workflow.

---

## 3. Governing invariants

### Truth before persuasive force

Copy may not compensate for missing evidence, weak product performance, unsuitable offer, unavailable functionality, bad policy, unresolved commercial state, or operational failure by increasing rhetorical pressure.

### Diagnose before tactic

Do not begin with `add urgency`, `use social proof`, `make it emotional`, `create curiosity`, or equivalent tactics. Identify the material reader/decision problem first and preserve competing explanations when evidence is weak.

### Strategy before strategic variety

Changing wording, gain/loss framing, sentence shape, or hook form does not by itself create a new angle. Strategic variety requires a materially different evidence-grounded reason to value, prefer, or choose.

### Dependency before formula

Do not use AIDA, PAS, BAB, 4P, PASTOR, or another fixed sequence as the decision engine. Progression follows the current reader state, target decision, logical dependency, evidence, and artifact constraints.

### Commitment proportionality

Do not ask for more commitment than the available evidence, resolved uncertainty, remaining risk, relationship/permission state, and current reader state can support.

### Meaning before style

A copy improvement that strengthens prose while changing claim scope, certainty, relation, referent, qualification, evidence relation, action semantics, or material implication is a regression.

### Repair before rewrite

Existing copy is not rewritten merely because another version is possible. Editing requires a diagnosed material defect and stays inside the authorized decision envelope unless the task explicitly authorizes a wider change.

### Environment owns representation

Once a downstream environment owner has resolved a material representation decision, generic copywriting guidance preserves the message and claim constraints but does not silently take back ownership of page structure, email send/sequence state, platform interaction, interface behavior, or other environment-specific architecture.

---

## 4. Frozen ownership boundaries

```text
Chapter 03
positioning / value / relevant alternative / differentiation

Chapter 04 + copywriting.*
message / persuasive route / progression / closure /
sentence realization / editing / short-form realization

Chapter 05
causal diagnosis / incrementality / experiments

Chapter 07
materially unresolved local-language / relationship realization

Chapter 08 + platforms
content-environment / participation / platform representation

Chapter 10
unresolved pricing / package / terms / commercial design

Chapter 11 + landing-page.*
web-page allocation / scan-deep paths / reachability /
page-specific action and cross-page support

Chapter 12 + email.*
send / wait / suppress / sequence / inbox-message allocation /
email-specific observation semantics
```

No new global `COPYWRITING`, `FUNNEL`, `AWARENESS_STAGE`, `PERSUASION`, `OBJECTION`, or `CTA` primitive is justified.

`copywriting.*` is a knowledge-routing namespace, not a controller job or ontology object.

---

## 5. Runtime activation rule

Stay on the direct path when the user supplies enough resolved state and the task can be completed without specialist copywriting judgment.

Use the smallest `copywriting.*` route only when an unresolved copywriting decision can materially change the result.

Examples:

```text
"Rewrite this sentence more clearly without changing meaning."
→ copywriting.craft only if the transformation is not already trivial

"Give me three genuinely different selling angles from these interviews and product facts."
→ copywriting.angle

"The angle is fixed. Build the argument for a skeptical enterprise buyer."
→ copywriting.progression

"Can we responsibly ask for a paid annual commitment with this proof?"
→ copywriting.closure

"This draft sounds polished but wrong. Diagnose and repair it while preserving voice."
→ copywriting.editing

"Write a short cold DM from this resolved message and proof."
→ copywriting.short-form when constrained realization remains materially open
```

Do not load the whole chapter as a ritual.

---

## 6. Application-layer disposition

### Short-form

Keep as a bounded realization layer inside the copywriting owner. It may compress, reorder, distribute, defer, or emphasize validated material under attention/context/space/interaction constraints. It may not invent stronger claims, urgency, personalization, social proof, prior relationship, or reader exposure.

### Web / long-form

Do not create a second generic web-copy chapter. Integrate SS8's surviving architecture into Chapter 11 because the existing landing-page owner already covers the relevant family of web conversion surfaces.

Chapter 11 should be strengthened around:

```text
reader-state envelope
decision needs
decision graph
scan path + deep path
information reachability
local sufficiency
cross-page delegation
transition continuity
path testing
```

---

## 7. Evaluation freeze

Evaluation must prefer decision correctness over one gold wording.

Hard failures include:

```text
invented product or customer truth
unsupported specificity
claim / scope / relation drift
proof laundering
false strategic diversity
formula substitution for reader-state reasoning
premature or excessive commitment request
material qualifier loss
false continuity / assumed exposure
over-intervention during editing
voice flattening that destroys supplied evidence of style
wrong-owner decision changes
```

A polished output that commits one of these failures is worse than a plainer output that preserves the governing decisions.

---

## 8. Integration gate

Implementation may:

- deepen Chapter 04;
- add `copywriting.*` routes;
- repair Chapter 11 and Chapter 12 handoffs;
- update operating guidance and handbook navigation;
- add bounded behavioral cases.

Implementation must not:

- create eight new chapters;
- create a template/formula library;
- add a new controller job;
- duplicate Chapter 03, 05, 07, 08, 10, 11, or 12 ownership;
- require every copy task to run all six capabilities;
- expose research-internal taxonomies as mandatory user-facing forms;
- reopen resolved strategy merely because deeper copywriting knowledge exists.

Theory remains frozen unless integration or independent adversarial review exposes a concrete failure that the frozen architecture cannot represent.

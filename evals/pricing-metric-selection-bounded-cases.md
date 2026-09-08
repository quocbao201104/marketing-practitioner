# Pricing-Metric / Charge-Basis Selection — Bounded Adversarial Cases

Status: **IMPLEMENTATION EVAL CONTRACT**

Target runtime route:

```text
commercial-design.payment
```

This eval checks only the bounded Chapter 10 implementation of the reviewed pricing-metric / charge-basis theory. It is not a general pricing benchmark and does not reopen the research freeze.

## Pass conditions

A passing answer should, where material:

- generate usage-independent / variable / hybrid as candidate classes rather than prematurely choosing one;
- instantiate concrete charge bases before selecting a variable/hybrid architecture;
- permit zero, one, or multiple variable bases;
- distinguish charge basis from meter specification, tariff, price level, and timing/commitment;
- distinguish Q quantity/contingency, R rate/tariff input, A allocation/eligibility, and C authoritative constraint by their role in the current contract/formula;
- preserve `true/raw usage != charged usage` where increments/aggregation matter;
- treat technical normalization and economically weighted accounting credits as potentially different;
- apply extra attribution/risk scrutiny to performance/outcome-contingent payment;
- compare architectures without a universal weighted score or outcome-maturity ladder;
- preserve authoritative finance/product/legal/sales dependencies rather than inventing facts.

## Fail conditions

Fail materially if the answer:

- chooses `seat`, `usage`, `outcome`, `fixed`, `variable`, or `hybrid` before considering plausible alternatives without an authoritative constraint;
- treats every price-affecting variable as a pricing metric;
- treats an internal estimate/model score as an authoritative constraint merely because it affects economics;
- assumes all credit systems are neutral pre-tariff normalization;
- equates value-based pricing with outcome-contingent payment;
- recommends pure outcome pricing while attribution/verification is materially unresolved;
- requires a fake usage meter for a genuine fixed fee;
- forces exactly one variable charge basis;
- uses a generic additive score to decide the answer;
- invents costs, margins, legal permission, product capability, or execution authority.

---

## PM-I01 — candidate generation before architecture selection

```text
A B2B automation product has resolved positioning.
The founder asks whether to charge a fixed annual fee,
per completed workflow, or base + workflow usage.
No authoritative cost or procurement constraint rules out
any class yet.
```

Oracle:

```text
Generate all three materially plausible architecture classes.
Instantiate the workflow basis for variable/hybrid candidates.
Compare only after candidate generation.
Do not choose "usage-based because AI should scale with usage"
or "fixed because buyers prefer predictability" by intuition alone.
```

---

## PM-I02 — zero variable bases remains legitimate

```text
A professional-service engagement has tightly bounded scope,
one deliverable, no meaningful usage measurement requirement,
and the buyer wants a fixed project quote.
```

Oracle:

```text
A genuine usage-independent fixed fee remains a valid candidate.
Do not invent hours/tasks as a billing meter merely to satisfy
the framework.
```

---

## PM-I03 — multiple simultaneous bases

```text
A payments service is considering:
$0.20 per successful transaction + 0.5% of transaction value.
```

Oracle:

```text
Represent both event quantity and economic-flow amount as
simultaneous charge bases when material.
Do not force one to be "the" pricing metric.
```

---

## PM-I04 — Q/R/A/C is contract-relative

```text
An insurance-like product uses miles driven as exposure,
a derived risk score inside the rate formula,
and a regulatory capital requirement as a hard feasibility limit.

It also uses a customer risk class in two different contract designs:

Design A:
the class only determines eligibility for a specialized plan;
once eligible, the class does not enter that plan's rate formula.

Design B:
the same class directly changes the customer-facing rate.
```

Oracle:

```text
miles driven       → Q
risk score          → R when it enters the customer-facing rate
capital constraint  → C when authoritative and only bounding feasibility
risk class, Design A → A because it only governs plan eligibility
risk class, Design B → R because it enters the rate formula
```

Do not label the derived risk score `C` merely because it is model-based or economically important. Do not classify the risk class by intrinsic identity: its role changes with the current contract/formula.

---

## PM-I05 — surcharge index is R, not C

```text
A freight contract bills distance and weight.
A published fuel index directly changes the customer-facing
fuel-surcharge percentage each month.
```

Oracle:

```text
distance / weight → Q
fuel index        → R
```

An internal fuel-cost limit that only bounds viability may instead be C.

---

## PM-I06 — raw usage versus charged usage

```text
A communications API records 61 seconds of service use,
but the proposed commercial rule bills in 60-second increments.
```

Oracle:

```text
Observed/raw usage and charged usage must remain distinct.
The meter specification must surface the increment rule.
```

Do not silently call both values "usage".

---

## PM-I07 — economically weighted credits

```text
An AI service records tokens across models with very different
provider economics. It proposes converting model-specific usage
through economic weights into one credit balance before final billing.
```

Oracle:

```text
Recognize an economic/accounting normalization layer.
Do not assume credits are a neutral technical unit or customer-value metric.
Do not require normalization to be strictly pre-tariff; acknowledge coupling.
```

---

## PM-I08 — outcome attribution failure

```text
A lead-generation product proposes charging only a percentage
of closed revenue. Closing depends materially on the customer's
sales team, pricing, inventory, and follow-up process, and attribution
rules are unresolved.
```

Oracle:

```text
Do not declare pure revenue-outcome pricing resolved.
Require outcome definition, verification, actor contribution,
attribution, observation window, and risk allocation.
Retain activity/output + performance component or base + outcome
component as candidates where useful, not automatic prescriptions.
```

---

## PM-I09 — value-based is not performance-based

```text
A vendor sets a fixed annual price ex ante using evidence about
expected customer savings. Payment does not change with realized savings.
```

Oracle:

```text
This can be value-based price setting without being
performance/outcome-contingent payment.
```

---

## PM-I10 — tariff defect does not automatically kill the basis

```text
Customers understand a per-workflow basis but reject pure PAYG
because monthly spend is hard to forecast.
```

Oracle:

```text
Keep the workflow basis under consideration.
Compare tariff alternatives such as included allowance,
commitment/base fee, cap, or overage where supported.
Do not infer that predictability failure proves the basis is invalid.
```

Causal-attribution variant:

```text
Period 1 uses the same per-workflow charge basis under pure PAYG.
Period 2 keeps the per-workflow basis unchanged but switches to
base fee + included workflows + overage.
Observed workflow usage falls after the change.
```

Oracle:

```text
Do not conclude that the workflow charge basis suppressed usage.
The basis remained unchanged while the tariff changed.
Without an appropriate identification strategy, the observed change
must not be causally assigned to the basis or to the tariff merely
from before/after association.
```

---

## PM-I11 — no outcome maturity ladder

```text
A cloud compute service can meter GB-seconds reliably.
The customer's downstream profit is influenced by many other systems.
```

Oracle:

```text
Resource/capacity charging remains legitimate.
Do not migrate toward profit/outcome charging merely because it is
"closer to value".
```

---

## PM-I12 — bounded dependency behavior

```text
Two charge architectures remain plausible, but one may be unprofitable
under heavy use. The task provides no authoritative cost-to-serve or
margin data.
```

Oracle:

```text
Identify finance/operations evidence as a dependency.
Do not invent costs or present one architecture as economically settled.
A provisional/robust choice or evidence request may be appropriate
under Chapter 10's existing uncertainty discipline.
```

---

# Review interpretation

These cases are intentionally heterogeneous. A pass does not require the same preferred architecture across cases.

The implementation should demonstrate the following bounded capability:

```text
GENERATE PLAUSIBLE ARCHITECTURES
→ INSTANTIATE CONCRETE CHARGE BASES
→ CLASSIFY PRICE-RELEVANT ROLES
→ SPECIFY / TEST ADMINISTRABILITY
→ APPLY OUTCOME CHECK WHEN NEEDED
→ COMPARE UNDER OBJECTIVE + CONSTRAINTS + EVIDENCE
→ RESOLVE TARIFF RELATIONSHIP
→ RETURN DECISION + UNCERTAINTY + REVISIT CONDITION
```

The eval does not authorize a new pricing ontology, universal optimization algorithm, generic score, or industry-specific pricing engine.

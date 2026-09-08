# Pricing-Metric Selection Theory Freeze

Status: **THEORY FREEZE — RESEARCH ONLY / NOT RUNTIME IMPLEMENTATION**

This artifact freezes the current research result for the bounded Commercial Design subproblem identified in the existing evidence ledger: **price metric selection in usage-based and outcome-based B2B services**.

It does not modify Chapter 10, `SKILL.md`, routing, runtime behavior, or evaluation contracts. Promotion into governed runtime knowledge requires a separate implementation/review step.

Post-review note: this version incorporates only the bounded independent-review repairs `CD-PM-T01` through `CD-PM-T06`. It does not reopen the central research question or expand the theory into a new pricing ontology.

---

## 1. Frozen research question

> Given a sufficiently established offering, customer/market relationship, product/service capability, and relevant authoritative constraints, how should a practitioner decide whether payment should be usage-independent, variable, or hybrid; and when variable pricing is material, what quantity, event, output, transaction, or performance state should payment vary with?

The question is narrower than general pricing strategy and broader than choosing among `per seat`, `per usage`, and `per outcome`.

The research does **not** assume that:

- variable pricing is always required;
- one pricing metric must be selected;
- a metric closer to final customer value is automatically better;
- seat pricing is obsolete;
- technical/resource pricing is inherently inferior;
- outcome pricing is a maturity endpoint;
- a universal weighted score can identify the correct pricing architecture;
- a new runtime primitive or ontology is required.

---

## 2. Epistemic-status convention

This freeze distinguishes four evidence/status categories.

### EMPIRICAL / ACADEMIC

A proposition has a direct conceptual, theoretical, or empirical parent in the cited literature. Scope and assumptions still matter.

### PROFESSIONAL PRACTICE

A proposition is supported by current practitioner/vendor practice or practitioner-oriented pricing work. It establishes existence or a useful operating pattern, not a universal causal law.

### PROJECT SYNTHESIS

A practitioner decision procedure, distinction, search heuristic, or boundary synthesized by this repository from multiple established parents. It must not be represented as a theory proposed or validated by any one source.

### OPEN QUESTION

A material issue intentionally left unresolved because the current evidence does not justify a universal rule. An open question must remain explicit rather than being filled by model intuition during runtime implementation.

---

## 3. Core terminology freeze

The research found that `pricing metric` is used differently across literature and practice. To avoid laundering distinct concepts into one term, this project freezes the following practitioner vocabulary.

### 3.1 Charge architecture

```text
USAGE-INDEPENDENT
Payment does not require measured variable consumption or performance.
Examples: fixed access fee, fixed project fee, fixed-period subscription.

VARIABLE
Payment changes with one or more measured quantities, events,
outputs, transactions, or performance states.

HYBRID
A fixed component and one or more variable components coexist.
```

**Status:** PROJECT SYNTHESIS, with established parents in tariff and pricing-architecture research.

A variable meter is not required for every legitimate commercial design.

---

### 3.2 Charge basis

```text
CHARGE BASIS
The observable scope, quantity, event, output, transaction,
or performance contingency that makes payment vary.
```

Examples:

- active member;
- GB-second;
- API request;
- completed workflow;
- successful transaction;
- transaction value;
- support issue resolved;
- equipment availability target.

`CHARGE BASIS` is project terminology. It is intentionally broader than the narrower usage-meter definition used in parts of the pricing literature.

**Status:** PROJECT SYNTHESIS.

---

### 3.3 Meter specification

For a variable charge basis, the commercial design must specify what actually counts.

```text
METER SPECIFICATION
- event/unit definition;
- scope;
- observation window;
- aggregation;
- minimum/billing increment;
- rounding;
- exclusions;
- duplication/deduplication rule where material;
- assignment to the relevant commercial instance.
```

The literature on pricing metrics and billing increments supports the distinction between true usage and charged usage and shows that increment rules can materially change charged quantity.

```text
TRUE / RAW USAGE
≠ CHARGED USAGE
```

**Status:** EMPIRICAL / ACADEMIC for the distinction; PROJECT SYNTHESIS for the exact checklist.

---

### 3.4 Billing unit / normalization

Raw measured variables may be billed directly or translated into a synthetic accounting unit. The freeze distinguishes at least two patterns:

```text
TECHNICAL / USAGE NORMALIZATION
heterogeneous raw usage
→ common non-monetary or engineering/accounting unit

ECONOMIC / ACCOUNTING NORMALIZATION
raw usage × economic weights
→ credit / accounting unit
```

A synthetic unit may therefore sit cleanly before tariff logic, may already embed economic weighting, or may intentionally couple normalization and tariff logic.

```text
RAW BILLABLE PHENOMENA
→ NORMALIZED BILLING UNIT
→ TARIFF
```

is a useful **possible pattern**, not a universal ordering invariant.

Examples in current software practice include credit systems that normalize heterogeneous model, token, retrieval, or computational consumption. GitHub AI Credits are specifically an example where model-specific economic pricing participates in the conversion into credits rather than a neutral pre-tariff normalization step.

A synthetic credit is **not** assumed to measure customer value.

**Status:** PROFESSIONAL PRACTICE for the existence of normalized billing units and economically weighted credit systems; PROJECT SYNTHESIS for the technical/economic normalization distinction; no universal selection or sequencing rule is frozen.

---

### 3.5 Tariff, price level, timing

Preserve the existing Chapter 10 distinctions:

```text
CHARGE BASIS / METER
What varies?

TARIFF / FORMULA
How does measured, normalized, or otherwise rate-relevant state become a bill?

PRICE LEVEL / MENU
What numeric rates apply?

TIMING / COMMITMENT
When and under what commitment is payment due?
```

A change in customer response after a tariff change must not automatically be attributed to the underlying charge basis.

**Status:** EMPIRICAL / ACADEMIC parent for metric/tariff separation and tariff behavioral effects.

---

## 4. Price-relevant variables must not be collapsed

Held-out cases in electricity and insurance exposed a necessary distinction.

```text
BILLABLE QUANTITY / CONTINGENCY
≠ RATE / TARIFF INPUT OR CONDITION
≠ ALLOCATION / PERSONALIZATION STATE
≠ AUTHORITATIVE CONSTRAINT
```

A variable can affect the final price without being a billed quantity.

### Practitioner classification

The following labels describe **roles inside the current contract/formula**, not intrinsic properties of a variable. The same underlying variable can play different roles in different commercial designs. If a relevant variable does not play one of these roles, do not force it into the classification.

```text
Q — QUANTITY / CONTINGENCY BASIS
A billable quantity, event, output, transaction, or contingency
that changes what/how much is charged.

R — RATE / TARIFF INPUT OR CONDITION
A variable, state, index, class, or derived score that enters
the customer-facing tariff/rate function or changes the
applicable rate for an otherwise defined basis.

A — ALLOCATION / ELIGIBILITY STATE
Determines which commercial conditions an actor can access
or is assigned.

C — AUTHORITATIVE CONSTRAINT
An authoritative external/internal constraint that bounds the
decision but does not itself enter the customer-facing pricing
function. If it is explicitly converted into a pricing-function
input, that use plays an R role rather than a C role.
```

Examples:

```text
Electricity
kWh                Q
peak kW             Q
time of day         R
customer class      A/R depending on design
grid constraint     C unless encoded into customer-facing rate logic

Insurance
miles driven        Q
coverage duration   Q or relationship term
risk class          A/R depending on design
rating factor       R
expected loss       R when used in the pricing function;
                    otherwise model/evidence state, not automatically C
solvency / capital constraint
                    C when authoritative and only bounding the decision

Logistics
distance            Q
weight/load          Q
route category       Q or R depending on contract
fuel index           R when it determines a customer-facing surcharge
internal fuel-cost constraint
                    C when it only bounds feasibility/economics
```

**Status:** PROJECT SYNTHESIS.

This distinction prevents every variable associated with price from being mislabeled as a `pricing metric`, prevents modeled quantities from being falsely elevated into authoritative constraints, and preserves Chapter 10's existing selection/allocation ownership.

---

## 5. Candidate-space search heuristic

When variable or hybrid charging is materially plausible, search for concrete charge bases across the parts of the exchange that materially exist.

```text
ACCESS / SCOPE / EXPOSURE
RESOURCE / CAPACITY
ACTIVITY / WORK
OUTPUT / DELIVERABLE
TRANSACTION / ECONOMIC FLOW
PERFORMANCE / OUTCOME
```

This list is:

- non-exhaustive;
- non-ordered;
- not a maturity ladder;
- not a claim that every offering contains every category;
- not a claim that downstream categories are superior.

Examples:

```text
ACCESS / SCOPE / EXPOSURE
active member, account, location, protected endpoint,
coverage duration

RESOURCE / CAPACITY
GB, compute time, reserved capacity, peak demand

ACTIVITY / WORK
API request, message, task, workflow run, hour of professional work

OUTPUT / DELIVERABLE
processed document, completed workflow, delivered shipment

TRANSACTION / ECONOMIC FLOW
successful payment, order, transaction value, assets processed

PERFORMANCE / OUTCOME
support resolution, qualified lead, availability level,
recovered amount
```

The purpose is candidate generation, not automatic selection.

**Status:** PROJECT SYNTHESIS — SEARCH HEURISTIC.

---

## 6. Candidate generation procedure

The frozen practitioner procedure is:

```text
1. DEFINE THE OPEN COMMERCIAL DECISION

   objective
   horizon
   authoritative constraints

2. MAP THE RELEVANT EXCHANGE / VALUE-DELIVERY MECHANISM

   who receives value?
   what is provided or changes?
   through what mechanism?
   which actors materially contribute?

3. GENERATE MATERIALLY PLAUSIBLE ARCHITECTURE CANDIDATES

   USAGE-INDEPENDENT
   VARIABLE
   HYBRID

   Treat these as candidate classes, not an early selection gate.
   An authoritative constraint may prune a class before deeper search;
   unsupported intuition may not.

4. FOR EACH MATERIALLY PLAUSIBLE VARIABLE / HYBRID CANDIDATE

   use the candidate-space search heuristic
   to instantiate concrete observable charge-basis candidates
   before selecting among architecture classes

5. ALLOW

   zero variable bases
   one variable basis
   multiple variable bases

6. CLASSIFY PRICE-RELEVANT VARIABLES BY THEIR CURRENT CONTRACT ROLE

   Q quantity/contingency basis
   R rate/tariff input or condition
   A allocation/eligibility state
   C authoritative constraint

7. SPECIFY THE METER / CONTINGENCY

8. TEST ADMINISTRATIVE FEASIBILITY

9. IF PERFORMANCE/OUTCOME CONTINGENT

   apply the special outcome/performance checks

10. COMPARE SURVIVING ARCHITECTURES

11. DESIGN / RESOLVE THE TARIFF RELATIONSHIP

   preserve that normalization and tariff may be distinct or coupled

12. VALIDATE THE MATERIAL UNKNOWN

13. RETURN

   recommendation
   rejected alternatives + reasons
   unresolved trade-offs
   evidence status / assumptions
   revisit condition
```

**Status:** PROJECT SYNTHESIS.

This procedure does not claim to compute a globally optimal price architecture. It specifically prevents a practitioner from deciding `fixed / variable / hybrid` through unguided prior intuition before the candidate-basis search becomes active.

---

## 7. Administrative feasibility questions

Before recommending a variable or performance-linked charge basis, confirm that the proposed commercial state can actually be administered.

```text
DEFINABLE
Can the project state exactly what constitutes one billable
unit/event/contingency?

OBSERVABLE
Can the relevant state be determined sufficiently consistently?

ASSIGNABLE
Can measured state be assigned to the correct customer,
account, contract, or transaction?

RATEABLE
Can the resulting state actually be mapped through a
specified charging rule into a bill?
```

These are not claimed as a scientifically validated four-gate model. They are a project practitioner synthesis from measurement, billing, and contracting constraints.

Failure does not automatically mean the underlying commercial idea is worthless; it can mean the metric definition, measurement system, tariff, or contract is not yet sufficiently specified.

These questions apply when a measured variable/performance contingency must be administered. A genuinely usage-independent fixed charge does not require a fake usage meter merely to satisfy this checklist.

**Status:** PROJECT SYNTHESIS.

---

## 8. Outcome/performance-linked payment requires special handling

The research strongly rejects a maturity ladder such as:

```text
seat
< usage
< activity
< output
< outcome
```

A downstream business result can be closer to customer value while being less controllable, less verifiable, more disputed, or more exposed to external causes.

Performance-based contracting research supports the distinction:

```text
OBSERVED OUTCOME
≠ PROVIDER-ATTRIBUTABLE OUTCOME
```

The pricing literature also supports keeping value-based pricing distinct from performance-based pricing: value-based pricing can set price ex ante from expected customer value, while performance-based pricing makes price contingent ex post on defined performance and therefore changes risk sharing [PM09].

```text
VALUE-BASED PRICING
≠ PERFORMANCE / OUTCOME-CONTINGENT PAYMENT
```

When payment is contingent on performance or outcome, explicitly resolve where material:

```text
OUTCOME DEFINITION
What counts as success?

VERIFICATION
How is success observed and reconciled?

OBSERVATION WINDOW
When is the outcome considered realized?

ACTOR CONTRIBUTION
What must buyer, seller/provider, and third parties do?

ATTRIBUTION
How much of the observed result can reasonably be assigned
to provider work rather than external/customer action?

RISK ALLOCATION
Who bears uncertainty and downside when outcome drivers
are outside one actor's control?

DUPLICATION / PRECEDENCE
Can one underlying event generate multiple billable outcomes,
and if not, which rule wins?
```

If a pure outcome contract cannot survive these questions, legitimate alternatives include:

```text
activity/output charging
+
performance component
```

or:

```text
base fee
+
outcome-linked component
```

rather than pretending outcome pricing is resolved.

**Status:** EMPIRICAL / ACADEMIC for the value-based/performance-based distinction, attribution, outcome uncertainty, and risk-allocation importance; PROJECT SYNTHESIS for the exact checklist and fallback forms.

---

## 9. Comparison dimensions — not universal gates

The research rejects treating the following as universal validity gates or as an additive weighted score.

After feasibility constraints are satisfied, compare surviving architectures on the dimensions material to the current decision:

```text
VALUE LINKAGE
Does the basis move meaningfully with relevant customer benefit?

PREDICTABILITY
Can the buyer forecast spend sufficiently for the decision context?

BUYER LEGIBILITY / ACCEPTABILITY
Can buyer/procurement understand and accept the mechanism?

AUDITABILITY / RECONCILIATION
Can both sides explain why the applied quantity/rate is what it is?

BEHAVIORAL INCENTIVES
What adoption, suppression, substitution, or gaming behavior
can the structure induce?

COST / MARGIN EXPOSURE
What serving-economics risk remains across plausible states?

SCALABILITY
Does the architecture remain usable as customer scope,
usage, workload, or value changes?

RISK ALLOCATION
Which actor bears demand, performance, cost, or outcome uncertainty?

REFERENCE / COMPETITIVE CONTEXT
What commercial expectations or alternatives materially frame adoption?
```

The exact list is a practitioner synthesis. Individual dimensions have established academic or professional parents; no source is claimed to validate this exact set or universal weighting.

**Status:** PROJECT SYNTHESIS, supported by mixed EMPIRICAL / ACADEMIC and PROFESSIONAL PRACTICE parents.

---

## 10. No generic weighted score

The freeze rejects a default mechanism such as:

```text
value linkage      4/5
predictability     3/5
auditability       5/5
...
TOTAL              31
```

There is no supported universal weighting that converts heterogeneous commercial objectives, risk, customer behavior, and authoritative constraints into a context-free scalar.

Use instead:

```text
AUTHORITATIVE / HARD CONSTRAINT
→ eliminate infeasible option

STRICT DOMINANCE WHERE GENUINELY SUPPORTED
→ prefer the non-dominated option

OTHERWISE
→ preserve explicit trade-off
→ choose under objective + horizon + evidence
```

**Status:** PROJECT SYNTHESIS.

---

## 11. Meter choice, normalization, and tariff choice are coupled but distinguishable

Do not infer that a defect in one tariff means the underlying charge basis is invalid.

Examples:

```text
per-workflow PAYG

vs

annual base + included workflows + overage
```

share a charge basis while allocating predictability and risk differently.

Likewise, a value-linked charge basis whose cost exposure is too volatile under pure usage pricing may sometimes be made viable through:

```text
base fee
included allowance
commitment
bucket
cap
classification
normalized credits
overage
```

These remedies are candidates, not universal prescriptions.

Normalization also does not have one mandatory location relative to tariff logic. A technical normalization unit may precede pricing logic; an economic/accounting credit may already embed model-specific or other economic weighting. Therefore do not infer that every credit system is a neutral pre-tariff meter.

Research on tariff choice, flat-rate bias, usage uncertainty, and behavioral response supports the broader proposition that tariff structure itself can change customer choice, usage, retention, risk allocation, and profitability.

**Status:** EMPIRICAL / ACADEMIC for tariff effects; PROFESSIONAL PRACTICE for observed credit/accounting patterns; PROJECT SYNTHESIS for the mitigation catalog and normalization/tariff boundary discipline.

---

## 12. Value linkage is important but not a universal validity condition

The freeze preserves:

```text
CUSTOMER-VALUE LINKAGE
= MATERIAL COMPARISON DIMENSION

not

CUSTOMER-VALUE LINKAGE
= UNIVERSAL HARD GATE
```

Resource/capacity pricing can be appropriate where the exchanged service is materially the provision or consumption of that resource. Logistics, cloud infrastructure, electricity, and other held-out settings reject a rule that all valid charging must closely proxy final business outcome.

Similarly:

```text
CLOSER TO FINAL OUTCOME
≠ AUTOMATICALLY BETTER CHARGE BASIS
```

A charge basis also allocates measurement burden, demand uncertainty, cost exposure, behavioral incentives, and performance risk.

**Status:** EMPIRICAL / ACADEMIC parent for pricing-basis consequences; PROJECT SYNTHESIS for the explicit practitioner rule.

---

## 13. Predictability has decision value of its own

Research on flat-rate bias in both consumer and professional B2B purchasing settings supports treating predictability, convenience, administrative burden, and insurance against unexpectedly high bills as real parts of plan preference.

Therefore:

```text
LOWER EXPECTED BILL
≠ UNIVERSALLY PREFERRED COMMERCIAL PLAN
```

and:

```text
PREDICTABILITY FAILURE
≠ AUTOMATIC REJECTION OF THE CHARGE BASIS
```

Predictability can often be affected by tariff, allowance, commitment, cap, or contract design.

**Status:** EMPIRICAL for buyer preference mechanisms; PROJECT SYNTHESIS for the decision implication.

---

## 14. Charging architecture changes incentives and risk allocation

Held-out advertising, professional-services, industrial-contracting, and usage-pricing cases reinforce:

```text
CHOOSING A CHARGE BASIS
IS ALSO CHOOSING
A DISTRIBUTION OF RISK AND INCENTIVES.
```

Examples include:

- hourly versus fixed professional fees shifting work-effort/uncertainty exposure;
- CPC versus CPA shifting performance risk and publisher incentives;
- fixed/reserved versus usage pricing shifting demand-volatility exposure;
- outcome contracts shifting performance uncertainty across buyer and provider.

The direction and desirability of those effects are context-dependent.

**Status:** EMPIRICAL / ACADEMIC parent; practitioner wording is PROJECT SYNTHESIS.

---

## 15. Revisit condition is mandatory when metric fit can decay

A charge basis can be appropriate at one product/service state and become misleading as the offering changes.

Current AI-service practice provides a concrete example: a resolution metric can lose coverage when the product begins performing valuable work that intentionally hands off rather than fully resolves a conversation autonomously.

The frozen practitioner invariant is:

```text
CURRENT CHARGE-BASIS FIT
≠ DURABLE CHARGE-BASIS FIT
```

A recommendation should identify the condition under which the chosen basis should be reconsidered, such as:

- product scope expands;
- work units become materially heterogeneous;
- cost structure changes;
- customer value shifts to a different mechanism;
- attribution becomes weaker/stronger;
- buyer procurement expectations change;
- usage volatility changes materially;
- a previously minor rate/allocation variable becomes decision-dominant.

**Status:** PROFESSIONAL PRACTICE parent; PROJECT SYNTHESIS for the invariant and trigger list.

---

## 16. Held-out counterexamples survived

The candidate theory was attacked outside the initial SaaS/AI examples.

### Electricity

Survives with multiple quantity bases (`kWh`, peak `kW`) plus rate conditions such as time-of-use. Demonstrates that quantity and rate condition must remain distinct.

### Logistics

Survives with distance, load, route/work burden, and related bases. Rejects the assumption that a valid basis must proxy final customer value rather than work/resource exposure.

### Insurance

Survives only after separating exposure quantity from risk classification and rate/allocation state. Rating factors and derived model variables can play an R role when they enter the pricing function; they are not automatically authoritative constraints.

### Professional services

Survives fixed, hourly, output, and mixed forms. Strongly rejects the assumption that measured variable charging is inherently more sophisticated than fixed pricing.

### Advertising

Survives impression, click, action, purchase, and revenue-linked candidates. Strongly rejects the assumption that deeper downstream performance is automatically superior; charge basis changes incentives and risk allocation.

### Industrial equipment / performance contracting

Survives availability and economic-result outcomes only with explicit verification, actor contribution, attribution, and risk reasoning.

No held-out domain required a new runtime primitive or a domain-specific pricing ontology.

---

## 17. Frozen rejected hypotheses

```text
R01  Pricing metric selection is just seat vs usage vs outcome.
     REJECTED

R02  Variable billing is always required for mature pricing.
     REJECTED

R03  One charge basis must be selected.
     REJECTED

R04  Downstream outcome proximity is a maturity ladder.
     REJECTED

R05  Seat pricing is structurally inferior.
     REJECTED

R06  Technical/resource consumption is structurally inferior.
     REJECTED

R07  Value linkage is a universal hard gate.
     REJECTED

R08  Every variable affecting final price is a pricing metric.
     REJECTED

R09  Charge-basis defects always require abandoning the basis.
     REJECTED

R10  A generic weighted score can select the correct basis.
     REJECTED

R11  Outcome-based pricing is equivalent to value-based pricing.
     REJECTED

R12  Metric selection alone resolves pricing architecture.
     REJECTED

R13  Usage-independent / variable / hybrid should be selected
     before materially plausible variable bases are generated.
     REJECTED

R14  Every synthetic credit is a neutral pre-tariff usage unit.
     REJECTED
```

---

## 18. Frozen surviving propositions

```text
S01  The pricing-metric / charge-basis selection gap is real
     and decision-relevant.
     SURVIVES STRONGLY

S02  Charge basis, meter specification, tariff, price level,
     and timing/commitment must remain distinguishable.
     SURVIVES STRONGLY

S03  True/raw usage and charged usage may differ materially.
     SURVIVES STRONGLY

S04  Usage-independent, variable, and hybrid charging are all
     legitimate candidate architectures.
     SURVIVES

S05  A design may use zero, one, or multiple variable bases.
     SURVIVES

S06  Quantity/contingency basis must be distinguished from
     rate/tariff input or condition, allocation state, and
     authoritative constraint; these are contract-relative roles.
     SURVIVES STRONGLY

S07  Candidate generation can use a non-exhaustive search across
     access/exposure, resource, activity, output, transaction,
     and performance/outcome.
     SURVIVES AS PROJECT SYNTHESIS

S08  Variable/performance designs require sufficient definition,
     observability, assignment, and rateability to be administered.
     SURVIVES AS PROJECT SYNTHESIS

S09  Performance/outcome-contingent payment requires special
     verification, attribution, actor-contribution, and risk reasoning.
     SURVIVES STRONGLY

S10  Value linkage is material but not a universal hard gate.
     SURVIVES

S11  Predictability and administrative simplicity can have buyer value.
     SURVIVES

S12  Tariff structure can materially alter behavior and risk while
     preserving the same underlying charge basis.
     SURVIVES STRONGLY

S13  Choosing a charge architecture also allocates uncertainty,
     incentives, and risk across actors.
     SURVIVES

S14  Charge-basis fit can decay as product/service scope changes.
     SURVIVES

S15  No new core runtime primitive is required by the evidence so far.
     SURVIVES

S16  Architecture classes should be generated as candidates; materially
     plausible variable/hybrid classes require concrete basis generation
     before selection unless an authoritative constraint prunes them.
     SURVIVES AS PROJECT SYNTHESIS

S17  Synthetic billing units may be technically normalized,
     economically weighted, or coupled with tariff logic.
     SURVIVES AS BOUNDED PRACTICE + PROJECT SYNTHESIS
```

---

## 19. Evidence-authority map

| Proposition family | Frozen authority |
| --- | --- |
| pricing metric / tariff distinction | EMPIRICAL / ACADEMIC |
| true usage vs charged usage / billing increments | EMPIRICAL / ACADEMIC |
| pricing-unit choice can alter commercial outcomes | EMPIRICAL / ACADEMIC |
| tariff can change usage/retention/profit | EMPIRICAL / ACADEMIC |
| predictability / flat-rate preference mechanisms | EMPIRICAL |
| outcome uncertainty / provider attribution | EMPIRICAL / ACADEMIC |
| value-based vs performance-based pricing distinction | EMPIRICAL / ACADEMIC — direct parent [PM09] |
| current normalized / economically weighted credit billing | PROFESSIONAL PRACTICE |
| current pricing-design workflows and revisit behavior | PROFESSIONAL PRACTICE |
| charge-basis terminology | PROJECT SYNTHESIS |
| candidate-space search heuristic | PROJECT SYNTHESIS |
| Q/R/A/C variable-role classification | PROJECT SYNTHESIS |
| four administrative-feasibility questions | PROJECT SYNTHESIS |
| technical vs economic/accounting normalization distinction | PROJECT SYNTHESIS |
| comparison-dimension set | PROJECT SYNTHESIS |
| no-generic-score decision discipline | PROJECT SYNTHESIS |
| exact return contract / revisit-condition wording | PROJECT SYNTHESIS |
| unresolved universal rules listed in §21 | OPEN QUESTION |

No project synthesis should be cited as if a single source proposed or validated it.

---

## 20. Scope boundaries

This freeze remains inside Commercial Design.

It does not independently determine:

- the firm's fundamental business-model sides or revenue architecture;
- product roadmap or nonexistent capabilities;
- authoritative cost, margin, capacity, tax, legal, or contractual facts;
- sales/deal approval authority;
- causal demand response without appropriate evidence;
- platform-specific representation, checkout, fee, or eligibility behavior;
- organizational authorization to execute the recommendation.

Reuse existing Chapter 10 dependency boundaries:

```text
MARKET-DESIRABLE
≠ ECONOMICALLY ATTRACTIVE
≠ OPERATIONALLY FEASIBLE
≠ PERMISSIBLE
≠ AUTHORIZED
```

The current subproblem selects or evaluates commercial charging architecture inside a sufficiently established surrounding business model.

---

## 21. Open questions intentionally not frozen as rules

**Status for every item in this section: OPEN QUESTION.**

The research did not establish universal procedures for:

- when heterogeneous raw usage should be normalized into synthetic credits;
- how many simultaneous charge bases are optimal;
- universal weights across value linkage, predictability, auditability, cost exposure, incentives, and risk;
- universal thresholds for acceptable attribution in outcome pricing;
- universal migration rules when a legacy charge basis becomes weak;
- industry-specific legality or fairness of differential/personalized rates;
- a universal choice between fixed, variable, and hybrid charging;
- a universal WTP or demand-estimation method for metric selection.

These remain context/evidence-dependent and must not be improvised into runtime rules.

---

## 22. Frozen practitioner output contract

A mature recommendation for an unresolved charge-architecture decision should, when material, report:

```text
RECOMMENDED ARCHITECTURE
fixed / variable / hybrid
charge basis or joint bases
meter specification
normalization if any
tariff relationship

WHY IT SURVIVED
objective / constraint fit
material comparison reasoning

REJECTED ALTERNATIVES
specific reason for rejection or inferiority

UNRESOLVED TRADE-OFFS
what remains genuinely uncertain

EVIDENCE / ASSUMPTIONS
what is known, hypothesized, or authoritative input

REVISIT CONDITION
what future change should reopen the decision
```

This is a project practitioner contract, not a claim that every small pricing task requires a full formal report.

**Status:** PROJECT SYNTHESIS.

---

## 23. Final adjudication

```text
PRICE-METRIC / CHARGE-BASIS KNOWLEDGE GAP          CONFIRMED

THEORY SUFFICIENT FOR BOUNDED IMPLEMENTATION
DESIGN                                             YES

NEW ONTOLOGY / CORE PRIMITIVE REQUIRED             NO

NEW TOP-LEVEL CHAPTER REQUIRED                     NO

BEST OWNERSHIP                                     CHAPTER 10
PAYMENT / VALUE-CAPTURE ARCHITECTURE

RUNTIME / ROUTING CHANGE AUTHORIZED BY THIS
ARTIFACT ALONE                                     NO

IMPLEMENTATION SHOULD PRESERVE                     metric ≠ tariff
                                                    quantity ≠ rate/allocation
                                                    contract-relative roles
                                                    fixed/variable/hybrid candidates
                                                    no premature architecture gating
                                                    outcome attribution/risk
                                                    normalization may embed economics
                                                    epistemic-status labels
                                                    revisit condition
```

The research question is therefore **THEORY-FROZEN** for the purpose of a later bounded implementation proposal.

Any implementation should be reviewed against this freeze rather than expanding the problem into a new pricing ontology, a general revenue-management engine, or a universal SaaS/AI pricing recipe.

# Pricing-Metric Selection Evidence Ledger

Status: **RESEARCH-ONLY EVIDENCE LEDGER — BOUND TO `03-pricing-metric-selection-theory-freeze.md`**

This ledger records the main sources used to support the bounded theory freeze for pricing-metric / charge-basis selection. It does not itself create runtime rules.

Identifiers use the local `PMxx` namespace so this subtrack can remain independently auditable without silently redefining the existing `CDxx` evidence ledger.

For every source, preserve both what it establishes and what it does **not** establish.

---

## [PM01] Skiera, Schlereth & Oetzel — pricing metrics and billing increments

Bernd Skiera, Christian Schlereth & Sebastian Oetzel (2020). **Pricing Metrics and the Importance of Minimum and Billing Increments.** *Journal of Service Research*, 23(3), 321–336.

DOI: https://doi.org/10.1177/1094670519895581

Evidence type: conceptual pricing model + three empirical studies in telecommunications.

Use in this track:

- defines a pricing metric as a unit used to measure usage for charging purposes;
- distinguishes pricing metric from tariff structure and from minimum/billing increments;
- supports `TRUE USAGE ≠ CHARGED USAGE`;
- documents that minimum/billing increments can materially increase charged usage relative to true usage;
- provides a direct parent for treating meter specification as commercially material rather than a mere implementation detail;
- supports the observation that flat-rate pricing does not require usage measurement to determine the bill;
- notes that services may use multiple pricing metrics simultaneously;
- supports the prior-art claim that choosing the pricing unit is a meaningful pricing decision.

Does not establish:

- the project's broader `CHARGE BASIS` terminology;
- the project's candidate-space search heuristic;
- a universal rule that the price unit closest to customer value is optimal;
- a universal increment length;
- that the telecommunications effect sizes transfer to other industries.

---

## [PM02] Lahiri, Dewan & Freimer — service pricing versus traffic pricing

Atanu Lahiri, Rajiv M. Dewan & Marshall Freimer (2013). **Pricing of Wireless Services: Service Pricing vs. Traffic Pricing.** *Information Systems Research*, 24(2), 418–435.

DOI: https://doi.org/10.1287/isre.1120.0434

Evidence type: formal economic / information-systems theory.

Use in this track:

- directly compares alternative pricing units for the same underlying wireless resource;
- supports the proposition that the choice of pricing basis can materially change firm, consumer, and welfare consequences;
- provides a counterexample to the assumption that a lower-level technical/resource unit or a higher-level service unit is universally preferable;
- supports keeping metric/basis selection distinct from scalar price setting.

Does not establish:

- a general practitioner selection algorithm;
- that service pricing or traffic pricing is universally superior;
- transfer of the modeled wireless-market assumptions to SaaS, logistics, insurance, or other settings.

---

## [PM03] Iyengar, Jedidi, Essegaier & Danaher — tariff structure changes behavior and profitability

Raghuram Iyengar, Kamel Jedidi, Skander Essegaier & Peter J. Danaher (2011). **The Impact of Tariff Structure on Customer Retention, Usage, and Profitability of Access Services.** *Marketing Science*, 30(5), 820–836.

DOI: https://doi.org/10.1287/mksc.1110.0655

Evidence type: pricing field experiment + demand model.

Use in this track:

- shows that tariff structure can affect consumer utility, retention, usage, and firm profit;
- supports `CHARGE BASIS / METER ≠ TARIFF EFFECT`;
- provides a concrete reason not to attribute every behavior change to the underlying meter when the tariff also changed;
- reinforces the need to keep customer-response and profit objectives distinct.

Does not establish:

- that pay-per-use is generally superior to two-part tariffs;
- that the measured effect sizes transfer outside the studied telecommunications service;
- a universal tariff to pair with any charge basis.

---

## [PM04] Kienzler, Kowalkowski & Kindström — B2B flat-rate bias

Mario Kienzler, Christian Kowalkowski & Daniel Kindström (2021). **Purchasing professionals and the flat-rate bias: Effects of price premiums, past usage, and relational ties on price plan choice.** *Journal of Business Research*, 132, 403–415.

DOI: https://doi.org/10.1016/j.jbusres.2021.04.024

Evidence type: four experiments with experienced purchasing professionals.

Use in this track:

- shows that experienced B2B purchasers can prefer flat-rate plans even when the flat-rate alternative is more expensive;
- identifies insurance, convenience, taximeter, overestimation, distrust, and administrative effects associated with flat-rate preference;
- supports treating predictability and administrative simplicity as decision-relevant buyer utility rather than assuming lowest expected bill determines plan preference;
- supports retaining usage-independent pricing as a legitimate candidate architecture.

Does not establish:

- that flat-rate pricing is generally optimal in B2B services;
- that every mechanism has the same weight in every buying context;
- that a variable pricing basis should be rejected whenever spend is less predictable.

---

## [PM05] Nullmeier, Wynstra & van Raaij — outcome attributability in performance-based contracting

Fabian M. E. Nullmeier, Finn Wynstra & Erik M. van Raaij (2016). **Outcome attributability in performance-based contracting: Roles and activities of the buying organization.** *Industrial Marketing Management*, 59, 25–36.

DOI: https://doi.org/10.1016/j.indmarman.2016.05.031

Evidence type: theory elaboration + multiple case study.

Use in this track:

- supports `OBSERVED OUTCOME ≠ PROVIDER-ATTRIBUTABLE OUTCOME`;
- identifies outcome uncertainty / low attributability as a central problem in performance-based contracting;
- shows that buyer inputs and responsibilities can materially affect the measured outcome;
- supports explicit actor-contribution and attribution reasoning before linking payment to outcome;
- provides a parent for treating performance-linked pricing as a risk-allocation problem, not merely a value-metric problem.

Does not establish:

- a universal threshold for acceptable outcome attribution;
- the project's exact outcome checklist;
- that performance-based contracts should generally be avoided;
- that findings from the two studied service contexts transfer without qualification.

---

## [PM06] Chen, Lee & Moinzadeh — usage volatility and cloud-pricing scheme preference

Shi Chen, Hau Lee & Kamran Moinzadeh (2019). **Pricing Schemes in Cloud Computing: Utilization-Based vs. Reservation-Based.** *Production and Operations Management*, 28(1), 82–102.

DOI: https://doi.org/10.1111/poms.12893

Evidence type: formal operations / pricing model.

Use in this track:

- demonstrates that demand size and usage volatility can change the relative attractiveness of utilization-based and reservation-based pricing schemes;
- supports the proposition that customer uncertainty can be a pricing-design variable, not only an evidence-confidence issue;
- provides a counterexample to a universal preference for pay-as-you-go or committed/reserved pricing;
- supports treating tariff/commitment design as distinct from the underlying service resource.

Does not establish:

- a general SaaS rule mapping low volatility to annual commitments and high volatility to pay-as-you-go;
- that cloud duopoly assumptions transfer to arbitrary markets;
- a universal method for measuring acceptable customer spend uncertainty.

---

## [PM07] GitHub Docs — AI Credits as an economically weighted billing unit

GitHub Docs (current documentation, accessed 2026-09). **Usage-based billing for organizations and enterprises / GitHub Copilot billing.**

Canonical documentation:

- https://docs.github.com/en/copilot/concepts/billing/organizations-and-enterprises/usage-based-billing
- https://docs.github.com/en/billing/concepts/product-billing/github-copilot-billing

Evidence type: current first-party provider documentation / professional practice.

Use in this track:

- confirms that GitHub AI Credits are explicitly used as a billing unit for Copilot usage;
- documents that input, output, and cached token quantities are priced according to the model used and that the resulting economic amount is converted into AI Credits;
- demonstrates a production example where a synthetic billing unit can embed model-specific economic weighting rather than merely normalize technical usage before tariff logic;
- supports the existence of economically weighted credit/accounting architectures.

Does not establish:

- that credits are a customer-value metric;
- that credit systems are preferable to direct billing;
- that every synthetic unit is a neutral pre-tariff usage normalization;
- a universal rule for where normalization must sit relative to tariff logic;
- a universal rule for when a synthetic billing unit should be created;
- durability of current GitHub prices, allowances, or product-specific billing details.

---

## [PM08] Atlassian Support — Rovo credits and complexity-weighted AI usage

Atlassian Support (current documentation, accessed 2026-09). **How Rovo credits work.**

Canonical documentation:

- https://support.atlassian.com/rovo/docs/rovo-usage-limits/

Evidence type: current first-party provider documentation / professional practice.

Use in this track:

- confirms a current production credit system in which billable AI/context events consume Rovo credits;
- documents that credit consumption can vary with interaction complexity and computational effort;
- demonstrates that a normalized billing unit can represent heterogeneous underlying events rather than a direct customer-outcome measure;
- provides a current example of credit accounting, pooled allowances, and usage limits;
- documents **announced** extra-usage billing scheduled to take effect on **2026-12-03**, rather than treating that billing as already live on the 2026-09 research date.

Does not establish:

- a general pricing rule for AI products;
- that complexity-weighted credits are more customer-aligned than seats, outputs, or outcomes;
- a universal tariff for synthetic credits;
- that announced future extra-usage billing is already an executed commercial state;
- durability of current allowances, announced rates, or implementation dates.

---

## [PM09] Hinterhuber — value-based pricing versus performance-based pricing

Andreas Hinterhuber (2017). **Value quantification capabilities in industrial markets.** *Journal of Business Research*, 76, 163–178.

DOI: https://doi.org/10.1016/j.jbusres.2016.11.019

Evidence type: peer-reviewed B2B pricing / value-quantification study with explicit conceptual treatment of value-based and performance-based pricing.

Use in this track:

- explicitly distinguishes value-based pricing from performance-based pricing as separate constructs;
- characterizes value-based pricing as ex-ante price setting based on expected customer value / willingness to pay or expected profitability improvement;
- characterizes performance-based pricing as ex-post adjustment based on predefined product/customer performance indicators;
- identifies risk transfer / risk sharing as a distinguishing feature between the two constructs;
- provides the direct academic parent for `VALUE-BASED PRICING ≠ PERFORMANCE / OUTCOME-CONTINGENT PAYMENT`.

Does not establish:

- that value-based pricing is universally preferable;
- that performance-based pricing is generally impractical in every setting;
- a universal outcome-attribution threshold;
- the project's exact outcome/performance checklist;
- that every outcome-linked contract is value-based.

---

# Cross-source synthesis boundaries

The following structures in `03-pricing-metric-selection-theory-freeze.md` are **PROJECT SYNTHESIS**, not claims made by any one source:

```text
USAGE-INDEPENDENT / VARIABLE / HYBRID

CHARGE BASIS

Q / R / A / C contract-relative variable-role classification

ACCESS / SCOPE / EXPOSURE
RESOURCE / CAPACITY
ACTIVITY / WORK
OUTPUT / DELIVERABLE
TRANSACTION / ECONOMIC FLOW
PERFORMANCE / OUTCOME

DEFINABLE
OBSERVABLE
ASSIGNABLE
RATEABLE

TECHNICAL / USAGE NORMALIZATION
vs
ECONOMIC / ACCOUNTING NORMALIZATION
```

The exact comparison set is also project synthesis:

```text
value linkage
predictability
buyer legibility / acceptability
auditability / reconciliation
behavioral incentives
cost / margin exposure
scalability
risk allocation
reference / competitive context
```

The sources above provide conceptual or empirical parents for individual concerns. They do **not** validate this exact combined procedure, establish universal weights, or prove completeness.

Likewise:

```text
AUTHORITATIVE CONSTRAINT
→ eliminate

STRICT DOMINANCE WHERE SUPPORTED
→ prefer

OTHERWISE
→ preserve trade-off under objective + evidence
```

is a project decision discipline, not an academic pricing theorem.

The repaired theory additionally treats `USAGE-INDEPENDENT / VARIABLE / HYBRID` as **candidate architecture classes** rather than an early selection gate. That ordering rule is PROJECT SYNTHESIS introduced to prevent the charge-basis search from being bypassed by unguided prior intuition.

---

# Open questions intentionally deferred

**Status for every item in this section: OPEN QUESTION.**

The current freeze is sufficient for a bounded implementation proposal, but not a comprehensive pricing bibliography. Additional primary research may still be valuable for:

- when synthetic credits improve versus obscure buyer understanding;
- multi-dimensional meters and the optimal number of simultaneous charge bases;
- detailed B2B outcome/value-based pricing and risk-sharing contracts beyond the bounded distinction already supported by PM05/PM09;
- migration from legacy seat or usage architectures;
- fairness/privacy consequences of personalized rate conditions;
- industrial capacity/reservation pricing outside cloud services;
- sector-specific regulatory treatment of billing increments, rate conditions, and outcome contracts;
- long-run behavior under AI-agent outcome pricing;
- direct tests of candidate-generation procedures rather than adjacent pricing theory.

These omissions remain explicit so the theory freeze does not overstate what the evidence establishes.

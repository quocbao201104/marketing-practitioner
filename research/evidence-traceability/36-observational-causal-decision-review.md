# Observational Evidence to Intervention Decisions

Date: 2026-09-07. Follows the question prioritized in [the audit synthesis](35-audit-synthesis-and-research-priorities.md).

Status: bounded theoretical and static design review completed. Two local clarification candidates are identified for Chapter 05. No runtime changes are included.

## Scope and existing strengths

Read [Chapter 05](../../skills/marketing-practitioner/handbook/05-diagnosis-causality-and-experimentation.md), its relevant bibliography records, and the observation/causal handoffs in Chapters 08, 12 and 14, with [SKILL.md](../../skills/marketing-practitioner/SKILL.md) as governing context. Reconciled the proposed gaps with [the earlier causality review](04-diagnosis-causality-content-review.md) and [its closure](05-causality-clarification-closure.md).

The current chapter already separates description, prediction and causation; preserves competing explanations, outcome definitions, randomized assignment/inclusion integrity, cohort state, maturation and censoring; distinguishes intervention effects from mechanisms; and supports action, waiting or further information under uncertainty. Its marginal-return paragraph already addresses saturation, carryover and interference. Those are strengths to retain.

The remaining issue is narrower: section 5 says observational designs require explicit assumptions, but does not make the relevant comparison and timing assumptions sufficiently operational. Merely recording a cohort or mentioning confounding does not establish an interpretable intervention comparison. The proposed changes concern consequential causal inference, not routine descriptive reporting or all marketing decisions.

## Source access and research scope

| Source | Material actually inspected | Scope and limit |
|---|---|---|
| R11, Hernan and Robins, Causal Inference: What If | [Author landing page](https://miguelhernan.org/whatifbook) and [19 August 2026 PDF](https://miguelhernan.org/s/hernanrobins_WhatIf_19aug26.pdf). Downloaded successfully with a local HTTP client after the web parser failed. Inspected title/version, contents and selected passages at printed pp. 27, 29-30, 32-33, 38, 41, 95-96, 109, 121 and 137. | Establishes methodological support for identification assumptions, comparison support, selection and the distinction between identification and precision. This is selected-page inspection, not full-book validation. The text explicitly allows alternative identification conditions; adjustment-based exchangeability is not the only possible causal design. |
| Supplement O-S1, Hernan, Sauer, Hernandez-Diaz, Platt and Shrier (2016) | [Author manuscript in PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC5124536/), abstract, sections 1-3 and the transition into section 4. Published as Specifying a target trial prevents immortal time bias and other self-inflicted injuries in observational analyses, Journal of Clinical Epidemiology 79, 70-75; DOI 10.1016/j.jclinepi.2016.04.014. | Methodological examples show how misaligned eligibility, strategy assignment and follow-up can bias a comparison even apart from residual confounding. Examples originate in epidemiology; their use below is a constructed marketing application of timing logic, not empirical evidence that an email treatment works. Full solution procedures were not reviewed or imported. |
| R32, Schnabel et al. (2016) | [PMLR paper](https://proceedings.mlr.press/v48/schnabel16.pdf), selected section 3 assignment/observation definitions and section 5 propensity-estimation assumptions and bias discussion. | Recommendation feedback is selected. The framework assumes nonzero observation probabilities; estimated propensities have their own assumptions and possible error. It is not a generic repair for hidden advertising allocation or a guarantee that weighting makes any dataset causal. Proofs and empirical results were not reproduced. |
| R38, Hadad et al. (2021) | [University-hosted published paper](https://utstat.toronto.edu/reid/sta2212s/2021/pnas-athey.pdf), pp. 1-2: introductory example, inference qualifications and policy-evaluation setup. | Adaptive randomization can complicate ordinary estimation while permitting valid methods under conditions. This paper's setup includes known assignment probabilities and stationarity assumptions. Hidden platform allocation cannot automatically inherit that regime. Full theorem conditions, proofs and delayed-outcome extensions were not audited. |

R11 retrieval improves the access status recorded in report 04; it does not rewrite that historical record or prove which version the original repository research used. The local PDF contains 365 pages and identifies the 19 August 2026 version. SHA-256: `a1067af923e9156bb95fbe4b0d18699bd0723e9c902bdc74465cf7782820b1b5`. It remains a temporary research download outside the repository. O-S1 is newly located supplementary verification, not a newly assigned runtime source ID or reconstructed original input.

## Three constructed chains

These cases examine whether the available instructions contain the necessary distinctions. No agent ran them, no customer data were analyzed, and no intervention was executed.

### 1. Traffic allocation and landing-page content change together

**Request:** conversion fell after a page revision and a traffic-allocation change. Decide whether to revert the page.

Current guidance correctly starts with measurement, competing explanations and concurrent changes. Now suppose all high-intent visitors received the revised page and all low-intent visitors received the earlier page. A regression or matched-group label does not supply the missing within-context comparison. If pre-existing intent affects both page receipt and conversion, the analyst must justify the design that separates those influences. Matching on what is recorded does not establish that all consequential differences are addressed; conditioning on later engagement may distort the question further.

Useful completion can describe the decline, inspect a demonstrable page defect, seek a discriminating comparison, or recommend a bounded reversible action with its rationale. It must not label the revised page's causal effect identified merely because the fitted estimate is precise. Restricting the target population or using a different valid identification strategy can change the analysis; unsupported extrapolation must remain explicit.

**Disposition:** O1. The existing rules reject the naive causal story but underspecify what makes the proposed observational comparison credible.

### 2. Day-seven email recipients versus all nonrecipients

**Request:** assess whether an onboarding email reduces first cancellation by day 30 from signup. Only accounts still active and eligible on day seven can receive it; the nonrecipient group includes accounts cancelled before day seven.

Defining the recipient group from eventual receipt guarantees it has survived without first cancellation until that receipt. Counting this period from signup as evidence of email benefit creates an invalid comparison even if the email has no effect. The problem is not solved merely by giving both columns the same 30-day reporting window.

One possible question is sending versus not sending among accounts eligible at day seven, with a common decision time and subsequent outcome horizon. That is a different population/question from a signup-level policy of sending later when eligible. The latter requires a design representing the policy from signup without retrospectively assigning groups from realized future receipt. Neither option automatically solves remaining confounding. Do not apply a blanket rule that all later initiation or time-varying analyses are invalid.

Useful completion identifies the biased comparison and the intended decision population, preserves the descriptive counts, and proposes an appropriate analysis boundary or missing information. It does not infer that the email is ineffective, withhold every operational message pending proof, or silently turn a day-seven conditional result into a signup-policy effect.

**Disposition:** O2. Chapter 12 flags trigger-induced selection and delegates to Chapter 05, but the latter does not explicitly connect eligibility, group construction and follow-up origin for this nonrandomized case.

### 3. Higher historical ROAS under adaptive delivery

**Request:** increase spend on a campaign with higher average attributed ROAS, although allocation adapted over time and conversions mature at different speeds.

Chapter 14 and Chapter 05 already require resource/allocation state, observation maturity and the distinction between attributed average and marginal incremental returns. Those rules support refusing an unsupported causal ranking while still making a provisional decision from costs, constraints and available evidence.

The additional pressure is a proposed analytical shortcut: infer propensities from dashboard averages, weight the observations, and call the result a valid marginal effect. R32 and R38 do not support that shortcut. The proposal must establish the relevant assignment/observation mechanism, support and design assumptions; the data needed for a valid estimator may be unavailable. Conversely, actual adaptive randomized data with suitable records and assumptions should not be rejected simply for being adaptive.

**Disposition:** O1 applies to the unsupported comparison/adjustment shortcut. No separate paid-media rule, response-curve estimator or universal waiting period is justified.

## O1: make observational identification assumptions decision-linked

**Location:** Chapter 05 section 5, the current final observational-design sentence; section 11 already supplies bounded action under uncertainty.

```text
TASK: estimate an intervention effect from a nonrandomized comparison
-> Chapter 05: make assumptions explicit
-> recording covariates or naming a model can stand in for justifying the comparison
-> a precise association may be treated as a causal basis for changing page or spend
-> add a compact, design-relative comparison qualification in the existing section
```

The correction should require a sufficiently defined intervention, comparator, population and outcome; the design-based reason the observed contrast can inform the counterfactual; and consequential selection/confounding and data-support assumptions. For adjustment-based comparisons, account for relevant pre-intervention causes of both receipt and outcome, avoid indiscriminate adjustment or treatment-affected filters, and identify missing comparison support. Matching, regression, weighting, balanced observed variables or a narrow interval alone do not establish the necessary assumptions.

Keep identification uncertainty distinct from sampling precision. Restriction, sensitivity analysis, another justified design or a bounded noncausal recommendation can be useful; do not invent effects or uncertainty ranges. This is not a demand for a DAG, a universal estimator, exhaustive variable collection or proof of a mechanism before using a credible intervention result. Designs relying on other identifying assumptions remain available.

## O2: align eligibility, group construction and follow-up

**Location:** Chapter 05 section 5, next to the nonrandomized comparison guidance. Existing section 4 retention language and Chapter 12 handoffs should remain rather than receiving duplicate rules.

```text
TASK: estimate retention benefit from delayed observed email receipt
-> retain cohort, start state and window; delegate trigger-selection inference to Chapter 05
-> future receipt defines a baseline group whose members necessarily survived to receipt
-> pre-receipt survival is misattributed to the intervention
-> make the relationship between eligibility, strategy assignment and follow-up explicit
```

The correction should prevent using future receipt, continued eligibility or survival to retrospectively define an initially treated group for the original baseline effect. Align the comparison with the decision time and retain the distinction between baseline policy, initiation among currently eligible units and later time-varying strategies. A restricted later-start comparison answers its own question and does not automatically recover the original population effect. A legitimate longitudinal design may use later information under its explicit strategy and analysis assumptions.

The intended addition is a short local methodological boundary, not a mandatory target-trial form for every diagnosis or a production email rule. A source record for O-S1 and a scoped R11 locator/access note would make the correction traceable without adding a new decision owner.

## Counterpressure and disposition

O1-O2 are omissions in operational specificity under constructed requests, not evidence that the current agent has failed. Existing broad source-fidelity rules would reject overclaiming; the local additions explain the otherwise missing reasoning needed at the causal handoff. They should be implemented only at the demonstrated surface, preserving all earlier D1-D4 corrections.

Do not add a catalog of matching, instrumental variables, differences-in-differences and regression discontinuity merely for coverage. Their methods require separate assumptions and task-specific scrutiny. Do not turn uncertain effects into mandatory inaction: an observed defect, material risk or reversible choice may justify action without claiming its causal benefit has been measured.

Recommended next work: implement O1-O2 in Chapter 05 and the smallest supporting bibliography updates, then re-read the three cases and the affected chapter/controller context. This pass does not propose changes to the controller, index, email, content or paid-media chapters.

## Verification and limitations

Only this report was added. Applicable repository instructions and worktree state were checked before writing; a pre-write snapshot covers 96 existing runtime/research files. Final checks cover report links, UTF-8 without BOM, CRLF, whitespace, existing-file hashes and final worktree status. Package and routing tests were not rerun for this report-only addition.

An initial local search used brace syntax unsupported by the shell and failed before execution; it was rerun with explicit glob filters. Web PDF parsing failures were distinguished from the successful local R11 download and actual page reads. Extraction contains mathematical/layout artifacts; no numeric effect was computed from extracted tables or diagrams.

No systematic literature review, raw-data reanalysis, full-book certification, live behavioral trial, historical-pilot comparison, commit or push was performed.

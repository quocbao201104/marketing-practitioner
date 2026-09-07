# Diagnosis, Causality and Experimentation: Content Review

Date: 2026-09-07. Chapter 05 baseline: committed version at `362ac88`; unchanged in the current worktree. Existing Chapter 01/03/04 edits and research artifacts were preserved.

Status: bounded design and source review completed. Four correction candidates; no runtime changes in this pass. This is not a systematic literature review or a live behavioral evaluation.

## Scope

Read all of [Chapter 05](../../skills/marketing-practitioner/handbook/05-diagnosis-causality-and-experimentation.md). Checked related language in [foundations](../../skills/marketing-practitioner/handbook/00-foundations-and-method.md), [quality rubrics](../../skills/marketing-practitioner/frameworks/quality-rubrics.md) and [operating guidance](../../skills/marketing-practitioner/references/operating-guide.md) before calling omissions local gaps. Source definitions are in the [bibliography](../../skills/marketing-practitioner/references/bibliography.md).

Review question: does the chain from metric to explanation to action preserve causal validity while giving enough guidance to decide? Cases below are constructed counterexamples, not agent runs, historical failures or estimates of error frequency.

## Overall assessment

The chapter distinguishes description, prediction and causation; attribution and incrementality; compound interventions and individual components; exploratory and confirmatory analysis; and local versus transferable results. It already asks for alternative explanations, a discriminating check, minimum useful effects, guardrails, inconclusive outcomes and consideration of reversibility.

The main gaps concern application of these principles. The pre-analysis brief names sample/duration logic without an explicit monitoring/stopping rule. Interpretation categories do not connect effect magnitude and uncertainty to practical decision thresholds. Broad implementation caveats do not identify how analysis selection can break a randomized comparison. Finally, testing a treatment is not automatically testing its proposed mechanism.

These are bounded omissions or ambiguities. They are not findings that the entire theory is wrong, nor reasons to add a statistics textbook, experimentation platform or universal checklist to the skill.

## Source access and provenance

Retrieved on 2026-09-07. Supplementary sources are new verification material, not retrospectively claimed as original research inputs.

| Source | Material inspected | Access and scope |
|---|---|---|
| R11, [Hernan and Robins author page](https://miguelhernan.org/whatifbook) | Book identity, citation and revision notice | Author page accessible; current download failed. Older Harvard PDF endpoints also failed, including a 404 at the content host. Full-text validation of R11 remains pending. |
| R12, [Kohavi et al. 2009](https://ai.stanford.edu/~ronnyk/2009controlledExperimentsOnTheWebSurvey.pdf) | Sections 3.3, 3.6 and 6.2.3; surrounding discussion | Author-hosted 42-page PDF recovered after an initial timeout. Selected passages inspected; no statistical reanalysis. |
| Supplement A, [ASA 2016 announcement and six principles](https://www.amstat.org/asa/files/pdfs/p-valuestatement.pdf) | Three-page official release | Full release inspected; journal statement DOI returned 403. Do not describe this as reading the full journal article. |
| Supplement B, [Microsoft: During-experiment patterns](https://www.microsoft.com/en-us/research/articles/patterns-of-trustworthy-experimentation-during-experiment-stage/) | Monitoring, early peeking and analysis segments | First-party practice guidance; platform-specific policies are not universal requirements. |
| Supplement C, [Microsoft: Sample ratio mismatch](https://www.microsoft.com/en-us/research/articles/diagnosing-sample-ratio-mismatch-in-a-b-testing/) | Missing units, mismatch diagnosis and triggered analysis | First-party implementation evidence; passing an SRM check is not proof of validity. |

R12 supplies effect-interval and power guidance, and explicitly distinguishes measuring an effect from explaining why it occurs. ASA separates statistical thresholds from effect size and decision importance. Supplement B addresses repeated looks and monitoring; Supplement C gives concrete routes by which missing or selected observations distort comparisons. Their scope is narrower than validating this skill's complete decision process.

## Proposition map

| Location | Assessment | Next action |
|---|---|---|
| §1 measurement definition | Useful prerequisite; metric comparability is necessary but not sufficient for causal inference | Retain |
| §2 decomposition | Explicitly analytical, not a causal formula; warns against uncontrolled slicing | Retain |
| §3 competing explanations and next check | Actionable diagnostic structure; prioritization is a practical heuristic, not a validated scoring equation | Retain |
| §§4–6 counterfactuals and attribution | Coherent distinctions; observational assumptions are mentioned but not elaborated | Retain; detailed R11 source audit pending |
| §5 randomized comparisons | Correctly says comparable in expectation and lists validity threats | Make selected threats operational under D3 |
| §7 pre-analysis brief | Useful decision/hypothesis structure and retained estimand | Add bounded monitoring/stopping clarity under D2 |
| §8 metrics and guardrails | Protects against favorable-outcome selection and local optimization | Retain; distinguish repeated looks as an additional issue |
| §9 non-positive results | Avoids declaring a concern irrelevant after one failed treatment | Connect uncertainty to useful-effect thresholds under D1 |
| §§7,9 mechanism learning | Some qualifications present, but a treatment effect need not identify a mechanism | Clarify under D4 |
| §10 transfer and marginal return | Useful scope and allocation distinctions | Retain; no new empirical endorsement of generalization or spend-response models |
| §11 reversibility/do nothing | Legitimate options, but not a complete decision rule by themselves | Compose with D1; avoid a rigid significance gate |

## D1 — Connect effect uncertainty to the decision threshold

Priority: first. Locations: §§7,9,11.

Task: decide whether to adopt a variant when a report says “not significant” or reports a small positive effect.

Current gap: the chapter names a minimum effect worth acting on and several outcome labels, but does not explicitly require interpreting the estimated magnitude and justified uncertainty together. This can leave both premature rejection and endless inconclusiveness compatible with the prose.

Constructed contrast: for an effect measured in percentage points, an interval of [-0.1, +0.1] and an interval of [-2, +3] both include zero. With a predeclared worthwhile gain of +1 point, they leave very different possibilities open. A statistically detectable +0.02-point gain could still be too small to justify implementation cost. These numbers are illustrative, not calculated experiment results.

Decision consequence: “not significant” becomes “no effect,” or “significant” becomes “ship,” without considering worthwhile benefit, plausible harm or cost.

Smallest correction: beside outcome interpretation, compare the effect estimate and a method-appropriate uncertainty summary with the worthwhile-effect threshold and guardrails. Distinguish unresolved consequential effects from evidence that meaningfully constrains them. If uncertainty cannot be estimated credibly, say so. Formal equivalence/non-inferiority claims require suitable designs and margins; failure to reject a point null does not establish equivalence. An action under uncertainty remains a decision, not proof of the effect.

Support: [R12 §3.3](https://ai.stanford.edu/~ronnyk/2009controlledExperimentsOnTheWebSurvey.pdf) motivates reporting effect intervals; [ASA principles 3 and 5](https://www.amstat.org/asa/files/pdfs/p-valuestatement.pdf) reject threshold-only decisions and equating significance with importance. The business-threshold comparison is an explicit decision synthesis.

## D2 — Distinguish outcome monitoring from an efficacy stopping rule

Priority: second. Locations: §§7–8.

Task: check a fixed-horizon A/B test daily and stop on the first favorable conventional significance result.

Current gap: sample/duration logic and primary-metric selection do not specify what happens under repeated looks or outcome-dependent stopping. Selecting one primary metric does not remove this issue.

Decision consequence: a result can acquire stronger confirmatory status than its analysis procedure supports.

Smallest correction: record the planned analysis and stopping approach when designing or judging an experiment. Repeated confirmatory looks need an inference method suited to that monitoring and stopping rule. Distinguish fixed-horizon analysis from valid sequential methods without prescribing one system. Monitoring or stopping for harm/implementation faults remains legitimate; such an intervention does not automatically establish a clean efficacy result.

Support: [Microsoft, Measure Early and Often and Monitor Metrics](https://www.microsoft.com/en-us/research/articles/patterns-of-trustworthy-experimentation-during-experiment-stage/). Do not copy its typical duration or significance settings as universal defaults.

## D3 — Preserve the comparison through assignment, inclusion and observation

Priority: third. Locations: §§5,7.

Task: compare conversion only among users who clicked a treatment-specific control after assignment, or interpret an experiment after one variant lost observations.

Current gap: “implementation quality” and “analysis population” name the issue but do not explain why post-treatment selection or missing observations can destroy the intended comparison. A known metric denominator does not make the denominator causally appropriate.

Decision consequence: a selected subgroup difference can be reported as the effect for the randomized population. Collecting more similarly biased observations does not fix that comparison.

Smallest correction: retain what unit was assigned, what population the effect concerns and how units enter the analysis. Check assignment and logging/inclusion integrity when material. Diagnose unexpected allocation/count discrepancies against the intended design. Flag treatment-affected filters and account for dependence/interference where relevant; do not impose user-level randomization or equal allocation universally. Passing one balance diagnostic is not sufficient validation.

Support: [Microsoft SRM guidance, root causes and triggering](https://www.microsoft.com/en-us/research/articles/diagnosing-sample-ratio-mismatch-in-a-b-testing/). This provides concrete evidence for selection/logging threats, not a complete treatment of clustered or adaptive designs. R11 full-text support for the broader methodological layer remains pending.

## D4 — Separate a treatment effect from the explanation for that effect

Priority: fourth. Locations: §§7,9.

Task: a revised page improves conversion; attribute that gain specifically to “reduced anxiety” because that mechanism motivated the test.

Current gap: the chapter says experiments can reduce uncertainty about a decision or mechanism. It qualifies interpretation of a failed message but does not equally emphasize that success can leave the proposed mechanism unresolved.

Decision consequence: an observed treatment result is retained as a general psychological lesson and transferred to a different artifact or audience.

Smallest correction: identify whether a design estimates an intervention effect, discriminates a mechanism, or both. A positive result alone does not settle why it occurred; mechanism claims need evidence and design capable of separating relevant alternatives. Preserve useful intervention results without promoting the motivating story into established causal explanation.

Support: [R12 §3.6, first limitation](https://ai.stanford.edu/~ronnyk/2009controlledExperimentsOnTheWebSurvey.pdf), which distinguishes quantitative treatment comparison from explanation.

## Counterpressure and scope limits

- Do not replace missing guidance with a universal p-value threshold, fixed sample size or test duration.
- Do not ban interim observation; distinguish monitoring, protective action and confirmatory inference.
- Do not require full experimental machinery for descriptive diagnosis or a supplied, adequate experiment report.
- Do not treat all subgroup analysis as invalid; the concern is whether selection and inference preserve the intended estimand.
- Do not demand a proven mechanism before using a credible treatment-effect result within scope.
- Do not require certainty before a reversible action. Compare feasible actions, waiting and further information using their consequences; clearly separate the decision from the evidential claim.

The four corrections can remain inside Chapter 05. No index or controller redesign is justified by this review. Bibliographic support may need a bounded update if supplementary sources are promoted with a later correction. The initial source inventory remains a dated snapshot.

## Verification and remaining work

Reviewed the entire chapter and selected surrounding guidance. Recovered R12 and the supplementary materials listed above; recorded failed access for R11 rather than claiming full verification. No effect estimates were recomputed, no datasets or live trials were used, and no old behavioral results informed findings.

The report's relative links and text integrity were checked. Existing runtime edits belong to the earlier F1–F3 correction and were preserved. No commit or push was requested. Next concrete work is a bounded correction of D1–D4, followed by source-scope and local-context review; a broader observational-causal-design audit remains separate.

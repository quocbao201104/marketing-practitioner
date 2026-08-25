# 05 — Diagnosis, Causality, and Experimentation

## 1. Marketing diagnosis begins with measurement definition

A metric cannot be interpreted safely until its definition is stable. Before explaining a movement in conversion, acquisition cost, retention, or revenue, establish the numerator, denominator, unit of analysis, time window, timezone, inclusion rules, attribution window, and any tracking changes.

Apparent market changes can be instrumentation changes. This possibility must be checked before causal narratives are constructed.

## 2. Decompose outcomes before assigning causes

Business outcomes are produced by multiple drivers. Decomposition converts a broad symptom into smaller quantities that can be examined separately. The purpose is analytical, not formula memorization.

For example, revenue can be decomposed into traffic, conversion, and order value; recurring revenue can be decomposed into new, expansion, contraction, and churn components. The exact decomposition should reflect the business model and measurement architecture.

A useful diagnosis therefore asks:

- where is the change concentrated;
- which component changed first or most materially;
- which segments exhibit the pattern;
- whether the overall average hides opposing movements.

Segmentation should follow plausible mechanisms or business questions rather than unlimited slicing for interesting patterns.

## 3. Symptom is not cause

A movement in a metric is evidence that a state changed. It is not, by itself, an explanation. Rising cost per click does not identify creative fatigue; falling conversion does not identify a weak landing page; rising churn does not identify price sensitivity.

A disciplined diagnosis records competing explanations rather than selecting the first plausible story.

```text
OBSERVED STATE
→ EXPLANATION A: support / contradiction
→ EXPLANATION B: support / contradiction
→ EXPLANATION C: support / contradiction
→ MATERIAL UNKNOWNS
→ NEXT DISCRIMINATING CHECK
```

The next check should maximize expected decision value relative to cost and time. A practical prioritization heuristic considers impact, plausibility, actionability, information value, and the cost of investigation.

## 4. Description, prediction, and causation

Causal inference literature draws a fundamental distinction between describing the observed world and estimating what would have happened under a different intervention [R11]. Marketing decisions frequently fail when these questions are collapsed.

- **Description:** what happened in the observed data?
- **Prediction:** which units are likely to experience an outcome?
- **Causation:** how would an outcome change if a specified intervention changed?

A variable can be an excellent predictor but a poor lever. A channel can receive attribution without producing equivalent incremental value. A customer trait can correlate with churn without being a manipulable cause.

For retention, preserve cohort and start state, opportunity or exposure, maturation or censoring, competing events, and relevant commercial or product state when they affect the retention decision or its interpretation. A prediction of churn risk is not evidence that a treatment will change churn.

## 5. Counterfactual thinking

The causal question is fundamentally counterfactual: what would the outcome have been for the same relevant population had the intervention not occurred, or had an alternative intervention occurred?

Because both potential states cannot normally be observed for the same unit at the same time, causal designs depend on comparison strategies and assumptions. Randomized controlled experiments are powerful because randomization can make treatment groups comparable in expectation, but implementation quality, interference, measurement, attrition, and power remain important [R12].

Observational causal designs can also be useful when randomization is infeasible, but their assumptions must be made explicit rather than hidden behind causal language.

## 6. Attribution and incrementality

Attribution allocates credit according to a rule. Incrementality estimates what additional outcome occurred because of an intervention. The two concepts answer different questions.

A last-click model may correctly report which channel received the last recorded interaction and still provide no valid estimate of what would have happened without that channel. Budget decisions that require causal leverage should therefore not rely on attribution alone.

Similarly, an outcome after simultaneous changes to price, annual commitment, eligibility, modifier, or configuration is a compound intervention, not a scalar price treatment. Retain the decision-relevant dimensions so the result is not relabeled as a claim the comparison did not establish.

## 7. Experimentation as knowledge production

Experiments are valuable not only because they identify a winner but because they reduce uncertainty about a decision or mechanism. A useful experiment begins with the decision and hypothesis.

A pre-analysis brief should state:

- decision to be informed;
- causal or behavioral hypothesis;
- eligible population;
- control condition;
- treatment;
- primary outcome;
- guardrail metrics;
- minimum effect worth acting on;
- sample and duration logic;
- conditions for an inconclusive result;
- decision rules for positive, null, and negative outcomes.

This structure reduces hindsight reinterpretation.

When results are retained as learning for a decision, preserve the estimand, analysis population, comparison or control, treatment or version, outcome and horizon, material validity condition or defect, and what the result cannot establish. These fields keep a causal result from becoming an unsupported general lesson.

## 8. Primary metrics and guardrails

Primary metrics should be selected before results are inspected when the analysis is intended to be confirmatory. Looking across many outcomes and reporting only the most favorable one creates a multiple-comparison and storytelling problem.

Exploratory analysis is legitimate but should be labeled as exploratory and treated as hypothesis generation.

Guardrails protect against local optimization. A treatment that improves clicks but damages qualified conversion, margin, refunds, retention, trust, or support burden may be a business loss despite a local win.

## 9. Null, negative, and inconclusive outcomes

A non-positive experiment should be interpreted at the level supported by the design. Failure of one message treatment does not prove that the underlying customer concern is irrelevant. It may indicate weak treatment strength, limited statistical power, incorrect timing, population mismatch, or a false mechanism.

Therefore result language should distinguish:

- evidence that supports the hypothesis;
- evidence that weakens it;
- evidence that falsifies a sufficiently specific prediction;
- insufficient evidence;
- inconclusive design or execution;
- out-of-scope inference.

## 10. External validity

A result in one context does not automatically generalize to another. Generalization depends on similarity of population, environment, product, implementation, and mechanism. Replication and local evidence increase confidence that an effect transfers.

This point connects experimentation to localization and organizational learning: every retained learning should carry enough scope to prevent accidental universalization.

For a proposed spend change, distinguish average attributed return, average incremental return, and marginal incremental return at that change. Consider saturation, carryover, substitution, interference, and uncertainty where material, while treating authoritative budget, margin, and capacity constraints as inputs. This bounds resource-allocation reasoning without constructing a media plan or optimizer.

## 11. Reversibility and the evidence threshold

The amount of evidence required before action depends partly on the cost of error. Small, reversible, low-risk changes can be tested under greater uncertainty. High-cost, irreversible, legally material, or brand-sensitive changes require stronger evidence and more deliberate review.

The same principle supports a rational **do-nothing option**. When signals are weak and a system is already changing, additional interventions can make future diagnosis harder.

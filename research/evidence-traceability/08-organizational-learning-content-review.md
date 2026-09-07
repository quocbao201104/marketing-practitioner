# Organizational Learning: Content Review

Date: 2026-09-07. Chapter 06 baseline: committed version at `362ac88`, unchanged in the current worktree. All earlier runtime corrections and research artifacts were preserved.

Status: bounded design review completed; two local clarification candidates. Source verification is partial, especially R09. No runtime edits or live behavioral evaluation in this pass.

## Scope and assessment

Read all of [Chapter 06](../../skills/marketing-practitioner/handbook/06-organizational-learning.md), the postmortem path in [operating guidance](../../skills/marketing-practitioner/references/operating-guide.md), the learning checks in [quality rubrics](../../skills/marketing-practitioner/frameworks/quality-rubrics.md), and relevant [skill invariants](../../skills/marketing-practitioner/SKILL.md).

The chapter already separates prior evidence, choice, outcome and interpretation; retains uncertainty, negative results and invalid tests; records context and freshness; and describes revision rather than timeless truths. There is no justification for adding another record schema or generic agent-memory subsystem.

Two transitions need more operational precision: moving from a retrieved record to its application, and moving from a prior interpretation to the current interpretation. The ingredients already exist, but the chapter does not explicitly connect them at those decision points. Findings below are constructed design counterexamples, not measured agent failures or historical pilot evidence.

## Source access and status

| Source | Material available in this review | Limit |
|---|---|---|
| R09, Walsh and Ungson (1991), [Organizational Memory](https://journals.aom.org/doi/10.5465/AMR.1991.4278992) | Search-indexed publisher abstract describing acquisition, retention, retrieval, use and misuse | Direct publisher opens failed. A located PDF copy also failed. No claim of full-paper inspection. |
| Supplement L1, Ackerman and Halverson, [Considering an Organization's Memory, author-hosted HTML](https://web.eecs.umich.edu/~ackerm/pub/98b24/cscw98.om.html) | Search-indexed abstract and Context vs. Contextualizing discussion | Direct HTML returned 502. A later journal-version PDF also failed; versions were not conflated. Indexed excerpts are partial access, not verified full text. |
| Supplement L2, [NASA Lessons Learned](https://www.nasa.gov/nasa-lessons-learned/) | Accessible official overview: original event, recommendations and use in organizational improvement | Engineering practice, not empirical proof of this marketing process. |
| Supplement L3, [NASA Systems Engineering Handbook §6.8](https://www.nasa.gov/reference/6-8-decision-analysis/) | Accessible sections on documenting decision context, alternatives, assumptions, uncertainty and rationale | Technical decision practice; committees, matrices and formal approval steps are not imported. |

The R09 abstract supports the narrow conceptual parent cited in §1. It does not validate the chapter's exact templates or show that an agent memory implementation improves performance.

L1 examines organizational memory through a hotline-work setting and emphasizes reconstructing the relevant context for reuse, including what may have changed. Its accessible excerpts support questioning a retrieval-only account; they do not establish a universal reuse algorithm. L2 distinguishes an originating event from recommendations. L3 supports preserving rationale and the state of knowledge behind decisions. None of these sources is claimed to have been an original research input to the repository; supplements are newly located verification material.

## Proposition assessment

| Location | Assessment | Disposition |
|---|---|---|
| §1: memory is more than accumulated files | Consistent with R09's abstract-level concept; operational-value statement is practitioner synthesis | Retain; full-source validation pending |
| §2: preserve activity and decision history separately | Clear distinction among prior evidence, selection, expectations, result and interpretation | Retain; no additional mandatory fields |
| §3: retain weakened and inconclusive hypotheses | Nonbinary statuses and scope already prevent many misleading failure labels | Retain; use Chapter 05 for inference validity |
| §4: allow scoped contradictions | Correctly avoids forcing different contexts into one answer | Clarify revision consequences under L2 below |
| §5: retain context and freshness | Good scope coverage and explicit warning against treating old records as current truth | Retain; use these existing qualifiers at reuse time |
| §6: state what a result does not prove | Explicitly composes with Chapter 05, including contaminated and older-version results | Retain; do not duplicate causal methods |
| §7: retrieve at the decision point | Semantic resemblance locates candidates, but does not establish applicability | Clarify under L1 below |
| §8: retain more than winners | Useful protection against a curated success narrative | Retain; no implication that every failed tactic is permanently excluded |
| §9: revise the current model while preserving history | Revision options are clear; operational linkage between prior and current conclusions remains implicit | Clarify under L2 below |
| §10: practical learning questions | Usable summary, not a validated organizational performance measure | Retain |

## L1 — Check applicability before adopting a retrieved lesson

Priority: first. Location: Chapter 06 §7, using qualifiers already defined in §§5–6.

Task: use a prior onboarding lesson to advise a self-service product after a feature and implementation-model change. The old result came from an enterprise cohort receiving assisted onboarding.

Current representation: retrieve semantically similar history so it can affect the new decision. The chapter stores segment, product, channel, method and freshness, but does not explicitly tell the reader to compare material conditions before adopting the old conclusion.

Gap: a strong topic match can be mistaken for evidence that the prior recommendation transfers. Retaining scope is necessary; using that scope is the remaining step. Existing skill invariants mitigate this risk, so the correction belongs locally rather than in the controller.

Decision consequence: apply an old intervention as a current rule despite a changed population, product capability or intervention context. The reverse error is rejecting useful history merely because wording or calendar date differs.

Smallest correction candidate: treat a retrieved lesson as a candidate input. Compare only conditions that can change its relevance or evidential force to the current decision, using the existing record. Reuse within supported scope; otherwise qualify its role as a hypothesis, seek the missing check when worthwhile, or refrain from relying on it. Neither resemblance nor recency alone establishes applicability. Do not force a full re-audit of every historic record.

Basis: the context-of-reuse concern in the [Ackerman/Halverson indexed author text](https://web.eecs.umich.edu/~ackerm/pub/98b24/cscw98.om.html), together with the chapter's own scope and causal-validity rules. The proposed operating instruction is project synthesis; fuller source access is still desirable.

## L2 — Distinguish changing a belief from changing its current applicability

Priority: second. Location: Chapter 06 §9, with §4 as context.

Task: reconcile an older controlled result with a newer weak anecdote, or retire a formerly useful recommendation after a product change.

Current representation: the chapter lists reinforcement, narrowing, contradiction and supersession, and says to preserve history. It does not explicitly identify what changed in the maintained interpretation or prevent a newer record from silently becoming the governing conclusion.

Gap: different reasons for revision can be collapsed. A contextual change can make a prior lesson inapplicable without showing the original observation was wrong. Conversely, a defect in the original evidence can warrant correcting its interpretation even if the context is unchanged. A newer contradictory account may deserve retention without outweighing stronger, comparable evidence.

Decision consequence: overwrite the old observation with the present interpretation, let recency substitute for evidence quality, or keep a retired recommendation appearing current. Also avoid treating every contradiction as grounds to discard the entire lesson when only one scope or claim is affected.

Smallest correction candidate: when maintaining a lesson, identify the affected conclusion/scope, the evidence or changed condition motivating revision, and the current disposition. Preserve the original observation and decision-time rationale, with the correction or supersession clear in the existing record. Distinguish evidence-based belief revision from changes in applicability; unresolved contradictions remain unresolved. Do not create another log, mandatory versioning system or approval step.

Basis: logical consequence of Chapter 06's own history/scope/revision commitments, with [NASA's decision documentation guidance](https://www.nasa.gov/reference/6-8-decision-analysis/) as bounded practice support for retaining assumptions and rationale. NASA does not validate this exact revision rule; it is project synthesis.

## Counterpressure and non-findings

- A decision made with reasonable evidence can have a bad outcome; §2 already retains the decision-time context. No separate outcome-bias framework is needed for this pass.
- Invalid tests should remain available as history, but §6 already requires causal validity qualifications. Do not duplicate Chapter 05.
- A lesson can confirm a current choice or prevent an unnecessary change. Learning need not produce a different action every time.
- Source dependence is already addressed in Chapter 01 and the controller. Repeated retrieval does not create new evidence, but this review does not justify copying that rule into every chapter.
- Archiving is not automatic authority to change a user's adopted strategy or publish a new claim. Preserve the existing task scope and authority rules.
- No need for retention schedules, vector retrieval, task automation, a country-specific memory model, or mandatory research archives.

## Verification and remaining limits

Checked all local report links, text integrity and worktree state. Source access was recorded as indexed excerpts versus accessible source text, rather than described uniformly as full-text verification. No statistics were recomputed and no live trials or old-pilot comparisons were used.

Only this report was added. Earlier runtime edits and research files remain intact. No commit or push. Recommended next change, if taken, is the two short local clarifications above. R09's full theoretical treatment and L1's full publication remain unverified in this pass.

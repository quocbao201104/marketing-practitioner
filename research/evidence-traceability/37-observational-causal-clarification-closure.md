# Observational Causal Guidance: Clarification Closure

Date: 2026-09-07. Implements O1-O2 from [review 36](36-observational-causal-decision-review.md), following explicit user authorization.

## Bounded changes

[Chapter 05 section 5](../../skills/marketing-practitioner/handbook/05-diagnosis-causality-and-experimentation.md) now connects observational identification to the intervention, comparator, population, outcome, adjustment rationale and available comparison support. A named estimator, observed balance or narrow interval alone does not establish identification. Alternative causal designs remain available, and section 11 still governs bounded decisions under uncertainty.

The same section connects eligibility, strategy assignment and follow-up origin. Its constructed day-seven email example prevents attributing pre-receipt survival to treatment and distinguishes a later eligible-population question from a signup-level policy. Legitimate later initiation and time-varying strategies remain permitted under suitable designs.

The [bibliography](../../skills/marketing-practitioner/references/bibliography.md) adds a scoped access/version note to R11 and a new R65 record for the timing-methodology paper. The source is supplementary verification; the marketing example is project application, not an observed email effect. Source inspection and its limits remain documented in review 36.

No controller, index, platform, email or paid-media instructions changed. Existing D1-D4 corrections and all earlier work remain intact.

## Static counterexample review

| Constructed case | Boundary retained after correction |
|---|---|
| Traffic allocation and page content change together; treatment groups lack relevant comparison support. | State what identifies the contrast and what requires extrapolation. A regression or matching label cannot substitute for this justification. A directly observed page defect can still justify a bounded fix without a measured causal lift. |
| Day-seven recipients are compared from signup against nonrecipients including earlier cancellations. | Later receipt cannot retrospectively establish baseline assignment. A day-seven eligible comparison answers a different question and still requires a credible comparator. |
| Adaptive delivery and delayed conversions produce higher historical attributed ROAS. | Existing marginal-return and maturity guidance remains. Weighting or precise estimates do not establish identification; valid adaptive designs are not rejected by their label. |
| The analysis cannot identify an effect, but the user needs a decision. | Qualify the effect claim and assess action, waiting or information under section 11. No universal experiment, certainty or inaction gate is added. |

These are author-reviewed interpretation checks, not agent executions, statistical reanalyses or observed marketing outcomes.

## Verification

- Repository package validator and current Codex validator: PASS.
- Manifest validation: PASS, 264 routes and 240 evidence sources.
- Routing mechanics: PASS, 68 checks.
- Actual R11/R65 lookups include their source and use boundaries.
- All 264 indexed route outputs remain identical to the pre-edit snapshot. Chapter 05 is a directly read foundational chapter; unchanged indexed outputs do not imply its guidance is unchanged.
- The two affected sections and their diff were inspected in context. Removing the intended additions recovers the exact pre-edit bytes, including earlier corrections.
- UTF-8 without BOM, Unicode, CRLF and original EOF states are preserved. Patch-introduced LF boundaries were restored to the files' existing CRLF convention.
- Of 97 pre-existing runtime/research files in the snapshot, only the intended chapter and bibliography changed. Final report links, encoding, whitespace and worktree status were checked.

An initial long shell edit was rejected before execution; a targeted patch completed the same bounded change. No additional permission or broader filesystem action was needed.

Only the two runtime files and this closure report were changed in this turn. No live trials, old-pilot comparisons, commits or pushes were performed. The correction closes O1-O2 within their reviewed scope; it does not establish completeness of observational causal methods or agent effectiveness.

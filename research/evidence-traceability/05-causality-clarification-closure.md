# Causality Clarification Closure

Date: 2026-09-07. Implements D1–D4 from [the Chapter 05 review](04-diagnosis-causality-content-review.md).

Changes are limited to Chapter 05 and the bibliography. Earlier edits to Chapters 01/03/04 and the existing research artifacts remain intact. Original inventories and reviews remain dated snapshots rather than claims about current source counts.

| Finding | Correction | Static counterexample check |
|---|---|---|
| D1 | Sections 9 and 11 compare magnitude and justified uncertainty with worthwhile effects, guardrails and action costs | Intervals [-0.1, +0.1] and [-2, +3] percentage points do not imply the same decision with a +1-point worthwhile gain. Rejecting a trivial gain or taking a reversible action still requires context; neither significance nor non-significance alone settles the decision. |
| D2 | Section 7 includes analysis, monitoring and stopping approach | Stopping a conventional fixed-horizon test at its first favorable look is not treated as valid fixed-horizon inference. Valid sequential methods and protective stopping remain permitted. |
| D3 | Section 5 makes assignment, analysis inclusion and observation integrity explicit | Filtering on treatment-affected clicks cannot silently inherit the original randomized comparison. Unexpected counts are diagnosed against intended allocation; passing a balance check is insufficient. |
| D4 | Section 7 distinguishes intervention effects from mechanism claims | A successful page variant can remain a useful scoped result without establishing that reduced anxiety caused the improvement. |

These are constructed design checks, not observed agent outcomes. The changes do not impose universal allocation ratios, durations, significance cutoffs, certainty requirements or mechanism validation before using a credible intervention result.

Added R59 (ASA official release), R60 (Microsoft monitoring guidance) and R61 (Microsoft sample-ratio and selection guidance), with locators and explicit limits. They are supplementary verification sources, not retrospectively claimed original research inputs. R11 full-text access remains unresolved as recorded in the review.

Verification: both package validators passed; all 68 routing-mechanics checks passed; 264 routes and 236 source entries validated. Each new source resolves through the existing source loader. Chapter 05 is an unindexed foundational chapter; headings and direct access remain unchanged. Reviewed the local diff and applicable context, and checked UTF-8 without BOM, CRLF and terminal-newline preservation.

No live trials or historical-pilot comparisons were run. No controller, index or evaluation infrastructure changes. No commit or push was requested.

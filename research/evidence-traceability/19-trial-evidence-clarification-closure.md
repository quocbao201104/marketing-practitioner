# Trial Evidence Clarification Closure

Date: 2026-09-07. Implements T1 from [the commercial-design core review](18-commercial-design-core-content-review.md).

Updated the trial-evidence paragraph in Chapter 10 section 5 and the use/boundary paragraphs of runtime source CD08. The text now names acquisition, subscription duration and revenue, and retains the economic condition needed for the cited profitability interpretation. No empirical result, effect size or universal trial-length recommendation was added.

Static counterexamples reviewed: a service with material usage/support costs cannot infer profit from revenue alone; a setting with negligible additional serving costs may support a scoped approximation. The qualification does not assert that all SaaS shares that cost structure. These are design checks, not observed agent trials.

Verification completed:

- Repository package validator and current Codex validator passed.
- All 68 routing-mechanics smoke checks passed; 264 routes and 239 evidence sources validated.
- Compared all 264 retrieved routes with a pre-edit snapshot. Only commercial-design.terms changed. Inspected that full excerpt and the CD08 source lookup; both retain the qualification.
- Inspected the two-file diff; git diff --check passed. Reversing only the three targeted replacements reproduces the original file bytes exactly. UTF-8 without BOM, CRLF, terminal-newline state and untouched Unicode remain preserved.
- Pre-existing runtime and audit files outside the two intended targets match their pre-edit hashes. Earlier uncommitted changes remain intact.

No controller, index, historical research ledger, evaluation, commit or push changes. No live experiments or old-pilot comparisons. Static validation does not establish agent efficacy or pricing performance.

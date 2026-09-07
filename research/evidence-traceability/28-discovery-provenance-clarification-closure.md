# Discovery Research Provenance: Clarification Closure

Date: 2026-09-07. Implements Q1 from the [core review](27-discovery-core-content-review.md), following user authorization.

## Changes

Two targeted replacements in the [discovery evidence ledger](../../skills/marketing-practitioner/references/search-discovery-evidence.md) replace broad references with identifiable supporting works:

- SD13 identifies the authors, year, title, SIGIR venue and author-hosted paper for the 2005 click-feedback study. Its scope distinguishes biased absolute interpretation from useful relative signals; it does not provide a universal CTR correction or current ranking claim.
- SD14 identifies the authors, year, title, WWW venue and institutional paper for the 2016 mobile good-abandonment study. Its scope preserves direct-answer task design and prevents inferring satisfaction from missing clicks in arbitrary systems.

Both records say these specific references were selected during this audit. Exact original research inputs/versions remain unverified. Existing IDs, conceptual claims, the historical overall ledger review date and all handbook/controller content are preserved. Source access and research limits are recorded in review 27.

## Verification

- Repository package validator and current Codex validator: PASS.
- Manifest: PASS, 264 routes and 239 evidence sources.
- Routing mechanics: PASS, 68 smoke checks.
- Actual SD13 and SD14 lookups include bibliographic details, study scope and provenance uncertainty.
- All 264 route outputs are unchanged from the pre-edit snapshot.
- Of 88 pre-existing runtime/research files, only the intended ledger changed.
- Inverting the two replacements reproduces the original bytes; UTF-8 without BOM, Unicode, CRLF and EOF state are preserved.

Static interpretation review: the references are identifiable support, not proof of exact original provenance; click evidence is not a universal relevance score; a non-click can be successful without establishing that any particular non-click was successful. No agent execution or research replication was performed.

Final link, encoding, whitespace and status checks accompany this report. No commits or pushes were performed. The user also authorized the operational review, recorded in report 29.

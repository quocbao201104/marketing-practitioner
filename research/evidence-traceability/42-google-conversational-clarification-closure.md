# Google Conversational Guidance: Clarification Closure

Date: 2026-09-08. Closes GC3-GC5 from [report 41](41-google-conversational-data-review.md).

Status: three local corrections implemented and checked at the content/retrieval level. No live agent or merchant-account test.

## Changes

In [the Google module](../../skills/marketing-practitioner/platforms/commerce/google-shopping.md):

- GC3: section 5.9 records the dated report scope, competitor-relative interpretation, special share-of-voice values, filters, and lag. Section 10 retains a compact diagnosis cue and a precise route to these conditions.
- GC4: sections 5.4, 5.5, 5.8, and 5.9 require checking existing factual coverage before adding optional carriers. They preserve required dedicated attributes and necessary product identity; a submitted document is not proof of extraction or a reason to delete required data.
- GC5: section 5.8 identifies the PDF, public crawlability, stable-link, and sharing-rights conditions for document_link. Section 5.9 retains these conditions beside its document option. An unsuitable document calls for another supported carrier or an identified dependency, not unauthorized publication.

In [the evidence ledger](../../skills/marketing-practitioner/references/commerce/google-shopping-evidence.md), G09 gains selected verification and direct Q&A/document specifications; G11 replaces the stale pilot statement and records the inspected reporting and duplication rules. Scope and source limitations remain explicit. The controller, index, source IDs, and prior GC1/GC2 correction are preserved.

## Verification

- `scripts/verify.ps1 -PackageOnly`: repository package validator and current Codex validator passed.
- `get-knowledge.py --validate`: passed, 264 routes / 240 evidence sources.
- `test-knowledge-routing.py`: passed, 68 routing-mechanics checks.
- Actual conversational-attributes and resolvability excerpts inspected; relevant field-roles and diagnosis passages also retrieved and inspected. Updated G09/G11 source records resolve.
- Compared against a pre-edit backup: the module changes only add text; the ledger changes add text and replace only the stale pilot bullet. Prior edits are retained, including Unicode. UTF-8 without BOM, CRLF, and terminal newlines preserved.
- Closure links, whitespace, final diff, and worktree scope checked. No full verifier run or runtime behavior claim is implied.

The inspected slices retain the conditions needed for the report's constructed misread-metric, redundant-enrichment, and unsuitable-document cases. This supports content sufficiency only; it does not establish that an executing model will follow the guidance or that a data change improves commercial outcomes. A representative operational review of this newly corrected area remains the next step.

Pre-edit backup: `C:\Users\Admin\AppData\Local\Temp\marketing-google-ai-fix-h34dk0wq`. This turn modifies the same two already-modified runtime files and adds this report. Untracked reports 38-41 were preserved. No commits, pushes, merchant actions, old-pilot comparisons, or cleanup were performed.

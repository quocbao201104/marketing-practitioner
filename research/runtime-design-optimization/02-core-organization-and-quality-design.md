# Core organization and quality criteria

Date: 2026-09-07

Status: authorized design and implementation specification. Behavioral evaluation remains deferred by the user.

## Problem and intended result

The current entrypoint contains the shared controller, invariants, a long specialist route catalog, detailed cross-domain handoffs, output-selection rules, and final checks. Every invocation receives these different levels of instruction together, although the controller explicitly calls for task-dependent knowledge loading. This is an organization/scope mismatch visible in the text; it is not a claim that a particular model has failed or that length alone predicts performance.

The quality rubrics assess evidence, positioning, messages, copy, diagnosis, experiments, learning, and ethics, but their opening does not distinguish an exploratory candidate from adopted/final communication. There is no dedicated comparison rubric for creative options. The revised controller allows exploratory drafts and delegated selection, so the review criteria should explicitly accommodate those forms of work.

The intended result is a self-contained entrypoint for ordinary work, direct access to the existing specialist knowledge, and optional detail for unresolved routing/handoff questions. Quality review should distinguish factual/ethical/explicit-scope constraints from contextual quality trade-offs without turning every response into a scored report.

## Design choices

1. Keep the current frontmatter, purpose, eight-step controller, seven jobs, uncertainty policy, retrieval mechanics, universal invariants, audience-facing content-selection gate, and final validation in `SKILL.md`.
2. Replace the long operating-path/handoff body in the entrypoint with a concise decision-oriented table. The table retains every specialist family, unindexed foundational chapter, and platform namespace. It points directly to chapters or namespace IDs. Preserve diagnosis-before-tactics, final representation ownership, fixed-state boundaries, provisional exploration, and direct fast-path execution.
3. Move detailed operating paths and state handoffs to one installed reference: `references/operating-guide.md`. Preserve their substantive text and headings, except moving the audience-facing selection gate back to the core and replacing its old position with a pointer. Explicitly state that prose file paths in the relocated sections are relative to the skill root. Provide links to the two major sections and exact-heading search guidance; the direct path table stays in the core rather than being duplicated here. Consult only a relevant section when the core table leaves the boundary, subroute choice, or handoff unresolved; the reference is not a required hop before the handbook or helper.
4. Keep physical route selectors in `routing-index.json`. No namespace, logical ID, selector, helper behavior, platform module, or source ledger is changed by this reorganization.
5. Add an opening review procedure to `frameworks/quality-rubrics.md`: identify the deliverable's job and status, choose applicable criteria, preserve nonnegotiable constraints, assess contextual trade-offs, and report specific useful corrections only when review is part of the deliverable.
6. Add criteria for creative exploration/candidate selection and for completion/decision usefulness. Distinguish requested wording variants from distinct concept directions, and distinguish plausible communicative mechanisms from demonstrated audience response. A provisional candidate can be assessed without settled strategy or finished production; final output still needs the facts and decisions its job requires.
7. Make the existing copy rubric compatible with candidate versus final status and treat stylistic patterns as contextual signals rather than a blacklist. Add pointers from the core to the new criteria only when they are relevant. Preserve all existing rubric sections and qualitative, unvalidated status.
8. Update the README's runtime/reference description for the new installed operating guide. This is a navigation change, not a release or new capability claim.

## Alternatives considered

- Leave all specialist details in the entrypoint and shorten sentences: preserves the mixed responsibilities and duplicates every specialist concern into ordinary invocations.
- Split every specialist family into another routing file: introduces many new files and a second catalog to maintain alongside the existing handbook and index.
- One conditional operating reference plus a direct core table: selected because it preserves the detailed contract while keeping the ordinary path self-contained. The main risk is a summary dropping a material condition; retain those conditions in the entry table/core boundary notes and verify the moved text mechanically.

## Static counterexamples and boundaries

- A fully supplied caption still goes directly to drafting; neither the new reference nor `content.fast-path` is compulsory.
- An open causal performance question still reaches Chapter 05 before an unjustified copy rewrite; a noncausal commerce-state question can go directly to commerce.
- A fixed price or fixed identity used in communication remains fixed. Identity production stops at the ordinary execution boundary.
- A paired positioning/message exploration can access Chapters 03 and 04 under candidate assumptions without finalizing strategy first.
- Resolved message truth does not give Chapter 04 ownership of a platform-specific outline already resolved by the downstream owner.
- Cross-domain handoffs can read the applicable detailed contract without copying every field into every task or the final artifact.
- A request for three wording variants does not require three different strategies. A request for different creative directions should not be satisfied by synonyms alone.
- An original idea with fabricated proof cannot compensate for that defect through aesthetic quality. A familiar but appropriate expression is not defective merely because it is familiar.
- A reviewer can explain why a candidate fits the brief, but cannot infer measured conversion, recall, brand recognition, or causal effect from preference.

These are design checks, not executed behavioral cases or performance evidence.

## Implementation and verification plan

- [x] Snapshot the current local bytes to preserve earlier uncommitted work and record encoding/newline state.
- [x] Complete an independent read-only static review of the proposed organization before moving the entrypoint content.
- [x] Extract the detailed operating paths/handoffs into the installed reference; preserve the audience-facing gate in the core.
- [x] Add the concise direct-routing table and conditional reference pointers to the entrypoint.
- [x] Extend the quality rubrics and adjust candidate/final and stylistic-review wording.
- [x] Verify exact preservation of moved specialist text, all original route IDs, and unchanged index/helper bytes. Check new Markdown links/anchors and root-relative path interpretation.
- [x] Run the package validators, existing 68 routing-mechanics checks, and full route/source validation. These are structural/infrastructure checks, not model evaluations.
- [x] Review the working diff, verify original UTF-8/BOM/CRLF state and Unicode, and check final Git status. Do not clean pre-existing caches, commit, publish, or modify historical evaluations.
- [x] Record actual outcomes and any remaining uncertainty below.

## Evidence status

The organization and qualitative review criteria are project synthesis derived from the existing decision-first contract and specialist boundaries. No new empirical marketing claim or optimal prompt-length claim is introduced. This pass does not establish that the new layout improves activation, routing, response quality, or model reliability. Historical pilot results are not an acceptance baseline.

## Static review record

The independent pre-move review required the compact core to retain voice precedence, named-destination governance, market-selection versus adaptation ownership, consequential target-language relationship choices, direct landing-page/email/platform entry, email versus other owned-channel composition, and causal versus descriptive diagnosis boundaries. These are present in the direct table and composition notes.

The final independent read-only review found no blocking conceptual issue. It confirmed the optional guide, root-relative path interpretation, candidate/final rubric applicability, preservation of factual constraints, delegated selection, and the distinction between inspectable quality and measured effectiveness. A minor navigation-spec mismatch was resolved by explicitly choosing two broad section links plus exact-heading search rather than another copy of the path catalog.

A compact attribution/incrementality/causality reminder remains in the core, preserving an important inference boundary and the Unicode sentinel required by repository hygiene checks. The substantive specialist detail was moved without deletion or paraphrase; the audience-facing content-selection gate remains in the entrypoint.

The index-only physical-binding instruction was scoped explicitly to indexed knowledge. Foundational chapters without logical section routes remain directly addressable, consistent with the core table and the prior resource architecture.

## Verification and local outcome

- The core changed from 850 lines to 217 lines by moving conditional detail into the installed operating guide. This is a structural measurement, not evidence of improved behavior or lower total task cost.
- A byte-conservation check reproduced the original specialist-path/handoff span from the guide, accounting only for the content-selection gate retained in the core and its replacement pointer. All original logical-route references remain present across the core and guide. No specialist knowledge was deleted to achieve the smaller entrypoint.
- Both package validators passed through `scripts/verify.ps1 -PackageOnly`; all 68 existing routing-mechanics checks passed; all 261 routes and 233 evidence sources validated.
- All 17 local Markdown links/anchors in the core, operating guide, and quality rubrics resolved. Relocated backtick file paths were checked relative to the skill root.
- UTF-8, BOM state, original CRLF line endings, Unicode, and required core sentinels were preserved. The index, helper, and evaluation files remain untouched. Earlier uncommitted work remains in place.
- The full repository entrypoint was not rerun in this pass; the pre-existing Python-cache hygiene limitation recorded in the first review remains outside this task. No cache cleanup, live agent experiment, commit, branch, or publication was performed.

The new creative/completion criteria and the reorganized contract have been reviewed for static consistency. Their effect on actual marketing quality, route use, and model reliability remains unmeasured.

## Pre-push verification

After the user authorized committing and pushing all pending work, the complete repository verification entrypoint ran successfully in a clean temporary copy of all 267 tracked and non-ignored source files. Byte comparison confirmed that the verified copy matched the workspace before this verification note was added. Both package validators, 68 routing-mechanics checks, 261 routes / 233 evidence sources, 138 Pressure Discovery infrastructure tests, 86 behavioral-harness tests, and UTF-8/generated-artifact hygiene passed. The original workspace's pre-existing Python caches were preserved. No live model evaluation was run.

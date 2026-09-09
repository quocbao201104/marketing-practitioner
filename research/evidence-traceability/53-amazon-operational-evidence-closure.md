# Amazon Operational Evidence: Correction and Static Review Closure

Date: 2026-09-09. Follows [review 52](52-amazon-operational-evidence-review.md).

## Changes

Closed AM1-AM5 in the [Amazon module](../../skills/marketing-practitioner/platforms/commerce/amazon.md) and its [evidence ledger](../../skills/marketing-practitioner/references/commerce/amazon-evidence.md):

- **AM1-AM2:** section 3 now identifies the processing and response-data distinctions needed to interpret a reported listing discrepancy.
- **AM3:** section 5 carries the reason-code check needed before acting on an absent estimate.
- **AM4:** section 6 retains the provider's transition, display, and field-priority qualifications.
- **AM5:** the independently retrievable external-store and authority sections retain the documented customer-market scope and distinguish configured actions.
- **Retrieval handoff:** section 12 points to the relevant existing route when these specific diagnostic questions arise. Section 13's direct drafting path remains unchanged.

Evidence records contain direct verification locators and limits. The module's date distinguishes the baseline from this partial follow-up; it does not refresh uninspected claims. No new route, source ID, controller instruction, shared concept, or implementation subsystem was added.

## Static case assessment

Read actual post-correction outputs for `amazon.catalog-pdp`, `amazon.offer-featured`, `amazon.product-info`, `amazon.shop-direct`, `amazon.buy-for-me-roles`, `amazon.agentic-authority`, `amazon.diagnosis`, and `amazon.fast-paths`, with the existing controller's source fidelity, scope, completion, and direct-execution rules.

The following assessments compare the written instructions with the cases defined before editing. They do not report model runs, observed account outcomes, or a behavioral pass rate.

| Cases | Inspected route(s) | Assessment |
| --- | --- | --- |
| AM-C01, AM-C02 | `catalog-pdp`, `diagnosis` | The newly explicit processing check addresses the first case; existing catalog-selection reasoning remains available once processing is no longer the open question. |
| AM-C03 | `catalog-pdp`, `diagnosis` | The excerpt now supplies the missing dataset distinction without directing an inventory mutation. |
| AM-C04, AM-C05 | `offer-featured`, `diagnosis` | Reason-specific interpretation replaces the unsupported common response to both cases. |
| AM-C06 | `offer-featured` | The existing no-guarantee boundary survives. Profit remains a separate commercial question, not a documented consequence of the estimate. |
| AM-C07, AM-C08 | `product-info`, `diagnosis` | The new qualifications distinguish a provider requirement from the observation being diagnosed. Neither case requires abandoning valid compact-copy guidance. |
| AM-C09 | `product-info` | The affirmative provider statement is retained without claiming a numerical model or proven rewrite effect. |
| AM-C10 | `shop-direct`, `buy-for-me-roles`, `agentic-authority` | Market scope appears in each relevant standalone excerpt; the evidence ledger explicitly preserves uncertainty elsewhere. |
| AM-C11, AM-C12 | `agentic-authority` | Configured action and completed transaction remain distinct, while previously authorized bounded delegation is preserved. |
| AM-C13 | `fast-paths` and controller | The route still ends in drafting from supported facts. No mandatory API inspection or agentic research was introduced. |
| AM-C14 | `shop-direct`, `buy-for-me-roles` | Existing regime and responsibility distinctions remain intact. |

No additional decision-changing defect was identified in these constructed cases. The review does not establish how consistently a model will apply the guidance.

## Verification

- `.\scripts\verify.ps1` completed successfully: repository package validator, installed Codex validator, 68 routing-mechanics checks, 264 routes / 248 evidence sources, Pressure Discovery tests, behavioral harness tests, and UTF-8/generated-artifact hygiene. The behavioral suite reported 86 tests. These harness unit tests do not execute the new Amazon scenarios against an agent.
- After the final editorial adjustments to the baseline-date label, evidence wording, and diagnosis pointer, package/routing validation and affected retrieval were checked again.
- Final diff, local report links, UTF-8 without BOM, existing CRLF line endings, and preservation of the other 417 tracked files were checked against the 419-file pre-edit hash snapshot. Only the two Amazon runtime/reference files changed; this review and its closure are new research artifacts.

The temporary edit helper initially failed to parse, before changing repository files. Correcting its string literal allowed the byte-preserving edits to run. This was a local editing error, not a repository test failure.

## Retained limits and next scope

The detailed title-help page was inaccessible. A04-A08, complete identity/schema specifications, detailed review-sharing rules, undisclosed search/ranking internals, and other markets' account behavior remain outside this verification. No feeds, listings, prices, orders, or live agent trials were executed. Historical pilot results were not used as a baseline.

This closes the agreed first Amazon slice, not a full Amazon audit. For the next platform pass, use the same claim-to-source and excerpt review on TikTok Shop's product state and content-product links, retaining the separate TikTok content owner. Do not infer that all remaining platform work is complete from this closure.

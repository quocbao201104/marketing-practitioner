# TikTok Shop: Commercial Fields, Discovery, and Metrics Review

Date: 2026-09-09. Continues [closure 57](57-tiktok-shop-state-and-link-closure.md). Baseline includes the existing Amazon and TikTok Shop corrections and reports 52-57.

## Sources and scope

Read the [module](../../skills/marketing-practitioner/platforms/commerce/tiktok-shop.md), [TTS03-TTS06](../../skills/marketing-practitioner/references/commerce/tiktok-shop-evidence.md), and baseline discovery/measurement extracts. Inspected these official sources:

- TTS03: [pricing](https://partner.tiktokshop.com/docv2/page/product-pricing), currency and seller-mode scope; [Update Inventory v202309](https://partner.tiktokshop.com/docv2/page/update-inventory-202309), SKU/warehouse fields and errors; [Edit Product v202309](https://partner.tiktokshop.com/docv2/page/edit-product-202309), audit and omission rules. Only indexed official text was accessible; direct extraction returned JavaScript shells. No integration was tested.
- TTS04: [Search terms and Product highlights](https://seller-us.tiktok.com/university/essay?knowledge_id=240361624880910), full public body, U.S., dated June 12, 2026.
- TTS05: [Shop Tab & Search Analytics](https://seller-us.tiktok.com/university/essay?knowledge_id=6276577063585582), overview, breakdown, recommendations, shop-page metrics and FAQ; [seller guide](https://seller-us.tiktok.com/university/essay?knowledge_id=8750609034250026), channel inclusion and optimization. Full public bodies, U.S., dated May 22 and May 14, 2026.
- TTS06: [Product Traffic Analysis](https://seller-us.tiktok.com/university/essay?knowledge_id=8090478953219854), public body, metric-change tables and FAQ, U.S., dated May 9, 2026. The Unique CTOR row's name and description conflict. This review records that ambiguity rather than supplying an invented formula.

Access date is not rollout confirmation. Provider benefit claims are not independent causal evidence. Full tax/promotion rules, current account/export behavior and other markets are outside this pass.

## Findings specified before edits

**TTS-R5 — commercial updates:** the prior-version rule in section 3 could be overextended to price/stock. Add the endpoint's commercial-field exception and a section 4 cue; keep permissions, validation and fulfillment constraints separate from content review.

**TTS-R6 — field optionality:** section 5 risks making the recommended highlight count a requirement and omits the documented removal condition. Preserve optional fields, suggested count, truthful inputs and the distinction between a missing field and a diagnosed sync problem.

**TTS-R7 — overlapping reporting categories:** Product Card is not a synonym for Shop Tab or organic search. Channel inclusion also does not prove a recommendation impression. Carry the relevant distinctions into discovery and measurement.

**TTS-R8 — measurement contract:** section 13 names source and time but lacks the provider-specific denominator, aggregation and transaction boundaries needed for comparisons. Add a compact interpretation aid, preserving the unresolved source row. Definitions must be matched before interpreting change or combining reports.

## Contrasting cases

These are author-designed static cases, not observed agent failures.

| Case | Constructed request | Required assessment |
| --- | --- | --- |
| TM-C01 | Title review is pending; assume the submitted price also waits. | Separate content and commercial-field processing. |
| TM-C02 | Stock update errors; keep retrying while waiting for title approval. | Inspect the returned constraint and source of inventory control. |
| TM-C03 | Format a VND SKU price with decimals. | Apply the relevant documented currency convention, not a universal two-decimal template. |
| TM-C04 | Two factual highlights suffice; fabricate a third to pass listing requirements. | Preserve truth and optionality. |
| TM-C05 | Suggested field text disappears; assume only a synchronization failure. | Check applicability/content conditions without asserting an unobserved rejection. |
| TM-C06 | Product included in Shop Tab; promise recommendation impressions. | Retain eligibility versus realized exposure. |
| TM-C07 | Add Shop Tab and Product Card figures as disjoint sources. | Establish the reporting hierarchy before summing. |
| TM-C08 | Compare shop-page conversion with product CTOR. | Match event units, scope and denominators first. |
| TM-C09 | Sum daily deduplicated counts; call the result unique people for the month. | Preserve the aggregation boundary. |
| TM-C10 | Treat gross metric growth as retained cash or profit. | Separate the reported measure from the requested outcome. |
| TM-C11 | Subtract this week's refunds to measure the same purchase cohort. | Align cohorts and timing or label the limitation. |
| TM-C12 | Use the conflicting Unique CTOR description as an authoritative formula. | Obtain the current metric definition; preserve uncertainty if unavailable. |
| TM-C13 | Missing aggregate metric means zero; a promised rollout must have happened. | Distinguish unavailable from zero and announced from observed. |
| TM-C14 | Improve truthful product wording with sufficient supplied facts. | Complete the draft without compulsory analytics research. |

The shared architecture already supports these distinctions. Correct the two TikTok Shop files and record validation in [closure 59](59-tiktok-shop-discovery-and-metrics-closure.md), retaining prior changes and stable route/source IDs.

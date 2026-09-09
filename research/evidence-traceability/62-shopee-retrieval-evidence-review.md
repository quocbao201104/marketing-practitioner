# Shopee Retrieval Evidence Review

Date: 2026-09-09. Continues [closure 61](61-shopee-commercial-and-visibility-closure.md). Level 1, bounded to S07/S08 and their discovery/retrieval excerpts.

## Primary evidence

Read the public HTML of [MRSE v1](https://arxiv.org/html/2408.14968v1), especially Online Implementation, Importance of submodels and Online A/Btest; and [MIEM v1](https://arxiv.org/html/2311.17954v1), especially Application Description, multi-image training and Online Evaluation. These are historical implementation reports, not a current account inspection or reproduction. Existing conversational-discovery claims are outside this pass.

## Findings before edits

- **SP-R4:** S07's generic online-gains wording omits the Ads comparator. Preserve experiment scope; model similarity scores cannot determine seller effort allocation or ranking weights.
- **SP-R5:** S08's broad deployed-system wording can hide the combined retrieval design. Keep recall separate from final ranking, and distinguish model configuration from seller requirements.
- **SP-R6:** Online gains can be misread as a forecast for a Vietnamese listing edit. Preserve market, period, comparator and per-user outcome in the source record; no transferable uplift promise.

## Constructed static cases

| Case | Request | Required assessment |
| --- | --- | --- |
| SR-C01 | Promise organic lift from MRSE's online result. | Preserve experimental surface. |
| SR-C02 | Allocate 68.2% of effort to images using importance score 0.682. | Similarity analysis is not a budget/ranking weight. |
| SR-C03 | Treat text search as title-only retrieval. | Retain multimodal representation distinction. |
| SR-C04 | Say MIEM replaced every image recall system. | Preserve combined implementation. |
| SR-C05 | Call the retrieval score final result order. | Preserve the subsequent ranking stage. |
| SR-C06 | Require exactly four seller images. | Model configuration is not listing policy. |
| SR-C07 | Forecast Vietnam orders from the published image-search lift. | Preserve tested market and intervention. |
| SR-C08 | Interpret clicks per user as CTR. | Preserve denominator and outcome. |
| SR-C09 | Infer the ChatGPT integration uses either paper's stack. | Existing UNKNOWN remains sufficient. |

These cases expose potential misapplication, not observed agent behavior. The correction belongs in the existing module and ledger; no shared architecture or route changes are justified.

## Validation plan

Inspect full diff and affected retrieval excerpts; run package, routing and source validation. Check all baseline hashes outside the two intended files, and preserve their UTF-8/no-BOM/CRLF bytes. No live agent benchmark or production deployment test is planned.

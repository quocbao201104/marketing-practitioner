# Shopee Commercial and Visibility Review

Date: 2026-09-09. Follows [TikTok Shop closure 59](59-tiktok-shop-discovery-and-metrics-closure.md). Existing Amazon/TikTok Shop edits and reports remain the baseline.

## Scope and evidence

Level 1 platform-local clarification. Read the Shopee module, ledger and commercial-state, special-visibility and diagnosis retrieval outputs before editing. Reviewed indexed official Vietnamese text from:

- S02: [price display](https://help.shopee.vn/portal/4/article/167479), overview and voucher availability. Select the required variation and inspect the price breakdown before comparing offers.
- S04: [listing policy](https://help.shopee.vn/portal/4/article/77246), general listing restrictions and enforcement section. Public text carries an August 14, 2024 update date; access date does not establish a new policy version.
- S09: [Hot Product terms](https://help.shopee.vn/portal/4/article/178311), sections 1-2 and 3.3, 3.6, 3.8. Published September 13, 2025; effective November 4, 2025. Participation, comparative priority and realized outcomes are distinct.

No seller account, rendered UI, integration, or transaction was tested. Other source IDs retain their previous review dates; engineering research and conversational discovery are outside this pass.

## Findings before edits

- **SP-R1:** A lowest-price statement lacks the concrete selection check. A requested configuration can cost more than the listing minimum; inspect that configuration and buyer-specific breakdown before recommending it within budget.
- **SP-R2:** Diagnosis lists stock and category but omits explicit enforcement state. Hidden or locked listings can be mistaken for declining rank. Check actual product/account status before choosing a content experiment; absence alone does not prove enforcement.
- **SP-R3:** Special-visibility guidance prevents generalization to organic ranking but leaves participation versus delivery implicit. Clarify comparative priority, possible provider-modified representations and the absence of guaranteed traffic/sales.

## Static counterexamples

Constructed cases, not observed agent failures:

| Case | Request | Required distinction |
| --- | --- | --- |
| SP-C01 | Recommend the large variant using the listing minimum. | Verify selected configuration price. |
| SP-C02 | Attribute two accounts' price difference to seller repricing. | Inspect buyer/voucher/time scope. |
| SP-C03 | Guarantee checkout price from a search card. | Recheck current voucher and order state. |
| SP-C04 | Rewrite keywords for a hidden listing. | Inspect enforcement state first. |
| SP-C05 | Declare a penalty because search cannot find the product. | Missing exposure alone is insufficient. |
| SP-C06 | Reuse an old listing's reviews for a different product. | Preserve identity; policy prohibits review manipulation. |
| SP-C07 | Promise traffic after receiving a Hot label. | Participation is not realized delivery. |
| SP-C08 | Treat Hot criteria as default organic weights. | Keep the feature comparison population scoped. |
| SP-C09 | Assume a Hot placement must match the uploaded creative. | Inspect actual provider-rendered representation. |
| SP-C10 | Diagnose Hot exposure loss only through copy. | Check participation/eligibility and observed delivery. |

## Planned validation

Inspect affected excerpts and full diff, package validators, routing checks, manifest/source validation, UTF-8/BOM/line-ending integrity, and preservation of baseline files. No controller, routing, shared handbook or harness changes are required.

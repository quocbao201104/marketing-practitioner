# TikTok Shop: Product State and Content-Link Review

Date: 2026-09-09. Baseline: `a5a5876` plus preserved Amazon working-tree changes and reports 52-55.

## Scope and evidence access

Read the [TikTok Shop module](../../skills/marketing-practitioner/platforms/commerce/tiktok-shop.md), its [ledger](../../skills/marketing-practitioner/references/commerce/tiktok-shop-evidence.md), and baseline `tiktok-shop.status`, `tiktok-shop.relinking`, and `tiktok-shop.content-product-identity` output. The existing product/SKU, content/target, representation, and attribution distinctions remain useful. This pass concerns the evidence and conditions needed to apply those distinctions.

| Binding | Source and inspected material | Access and scope |
| --- | --- | --- |
| TTS01 | [Products API overview](https://partner.tiktokshop.com/docv2/page/products-api-overview), review/version paragraph | Official indexed text recovered through web search; direct page extraction returned a JavaScript shell. Legacy parameter names are not instructions for current endpoints. |
| TTS02 | [Get Product v202309](https://partner.tiktokshop.com/docv2/page/get-product), query-parameter descriptions; [invite-only category change](https://partner.tiktokshop.com/docv2/page/streamlining-of-invite-only-product-categories), affected markets and audit fields | Official indexed passages; direct extraction returned shells. The latter is dated May 28, 2025 and explicitly concerns U.S. local sellers. No API/account behavior was executed. |
| TTS07 | [How to Link Products to Videos](https://seller-us.tiktok.com/university/essay?knowledge_id=5804034343962411), posting and post-publish sections | Full public article body, marked U.S.; displayed date August 5, 2026 differs from the ledger's historical June date. Do not infer which wording changed solely from dates. |
| TTS08 | [How to Relink Products](https://seller-us.tiktok.com/university/essay?knowledge_id=3759443559679790), feature conditions, restoration and FAQs | Full public body, U.S., displayed December 1, 2025. Use the feature conditions rather than promotional benefit language as outcome evidence. |
| TTS09 | [Post-publish linking](https://seller-us.tiktok.com/university/essay?knowledge_id=5178002307598122), tool workflow and FAQs | Full public body, U.S., displayed November 21, 2025. Its broad no-replacement/testing wording must be read beside the later dedicated relinking guide. |
| TTS10 | [Add a Product Link](https://seller-us.tiktok.com/university/essay?knowledge_id=4393475827222318), creator linking instructions | Public body used only for displayed-label/target context; no comprehensive affiliate or commission review. |

Access date is September 9, not a publication or account-verification date. TTS03-TTS06, full SKU/global-product schemas, LIVE-specific mechanics, and other markets remain outside this pass. Indexed API evidence has a weaker freshness/access basis than a rendered current reference and must be rechecked before integration.

## Findings specified before edits

### TTS-R1: identify the version being compared

Section 3 says an earlier version can remain live but does not identify how the retrieval request changes the compared content. A report that an API value differs from the storefront should preserve live, under-review, or draft selection before inferring sync failure. Add the v202309 selector distinction locally; use endpoint-specific documentation rather than the overview's older parameter spelling.

### TTS-R2: passing audit can leave prerequisites open

The status list does not explain the documented `PRE_APPROVED` case. A seller with a pending restricted-category prerequisite should check that reason rather than repeatedly rewrite content. Add the U.S. local-seller example with its exact scope; do not equate every pending listing with that explanation.

### TTS-R3: separate first attachment from replacement

Section 7's recently-published eligibility language omits the concrete tool boundary. Specify the U.S. post-publish workflow's unlinked-video, age, audio, matching, and policy conditions. An existing healthy link is not made freely replaceable by this feature. Conversely, the older FAQ must not negate the later supported unavailable-product relinking workflow. Carry this distinction into the fast path.

### TTS-R4: relinking eligibility and continuity need qualifications

Section 9 preserves content identity but compresses the feature prerequisites and can overstate continuity of traffic. Add the documented video-age/activity and violation conditions, preserve account/market checks, and distinguish retained content from guaranteed future reach or earnings. Keep the existing restoration and product-alignment guidance. The absence of a notification alone does not establish a platform defect.

## Contrasting cases for static assessment

| Case | Constructed input | Required distinction |
| --- | --- | --- |
| TT-C01 | Reviewed API value differs from the still-live title. | Compare matching versions before diagnosing sync failure. |
| TT-C02 | A U.S. local listing is pre-approved with a category prerequisite. | Resolve the reported prerequisite rather than assume copy rejection. |
| TT-C03 | A different-market product is pending without that reason. | Preserve uncertainty; do not import the U.S. explanation. |
| TT-C04 | Active product has an unavailable selected SKU. | Existing section 4 separates product state and SKU availability. |
| TT-C05 | Eligible recent video has no linked product. | Use the applicable first-link workflow without recreating content. |
| TT-C06 | Recent video has a healthy link; replace it for higher commission. | First-link capability does not establish replacement capability. |
| TT-C07 | A four-month-old linked video has recent activity and an unavailable target. | Evaluate dedicated relinking rather than reuse the first-link age rule. |
| TT-C08 | Relinking candidate has a blocking content violation. | Do not use a different target to bypass the unresolved violation. |
| TT-C09 | No notification arrived; creator claims a broken account. | Check eligibility and alternative availability before concluding defect. |
| TT-C10 | Suggested replacement differs from the demonstrated brand/function. | Existing alignment rule controls despite a recommendation. |
| TT-C11 | Original item restocks after replacement. | Retain multi-target history and inspect resulting anchors. |
| TT-C12 | Same video survives relinking; promise identical reach or sales. | Content continuity does not establish outcome continuity. |
| TT-C13 | Affiliate credit rises after relinking and a traffic-source change. | Existing measurement/causal boundaries remain necessary. |
| TT-C14 | Rewrite a product title from sufficient SKU facts. | Keep direct drafting; do not require a full linking or API audit. |

These are author-designed cases, not observed model failures. Apply the smallest corrections in the two TikTok Shop files, preserve route IDs and shared owners, and record actual validation in [closure 57](57-tiktok-shop-state-and-link-closure.md).

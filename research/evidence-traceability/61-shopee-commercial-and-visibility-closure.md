# Shopee Commercial and Visibility Closure

Date: 2026-09-09. Scope and primary sources: [review 60](60-shopee-commercial-and-visibility-review.md).

## Corrections

Updated only the [Shopee module](../../skills/marketing-practitioner/platforms/commerce/shopee.md) and [existing evidence ledger](../../skills/marketing-practitioner/references/commerce/shopee-evidence.md), plus these research reports.

- SP-R1: commercial-state now requires selecting the requested configuration and inspecting its price breakdown before deciding budget fit.
- SP-R2: product-info, diagnosis and the rank-drop fast path now distinguish confirmed listing/account restrictions from lower exposure; product identity remains protected against review manipulation.
- SP-R3: special-visibility now separates participation, comparative priority and delivery, and calls for inspecting provider-rendered creative. Diagnosis preserves eligibility and observed delivery.

S02/S04/S09 now have direct locators, access scope and bounded review dates. No source IDs, route definitions, shared semantics or controller changes were needed.

## Static assessment

Re-read the full module and affected loader excerpts against the ten constructed cases in review 60:

| Cases | Assessment |
| --- | --- |
| SP-C01-C03 | Selected configuration check added; existing buyer/voucher/time and checkout boundaries retained. |
| SP-C04-C06 | Enforcement check added without inferring a penalty from missing exposure; listing identity restriction explicit. |
| SP-C07-C10 | Participation and outcome distinction, scoped comparison population, representation and eligibility checks explicit. |

These are static knowledge assessments, not live agent trials or measured behavioral improvements.

## Verification

- `scripts/verify.ps1 -PackageOnly`: repository and installed Codex package validators passed.
- `test-knowledge-routing.py`: 68 routing-mechanics checks passed.
- `get-knowledge.py --validate`: 264 routes / 248 evidence sources passed.
- Retrieved and inspected product-info, commercial-state, special-visibility, diagnosis and fast-paths.
- Inspected the complete two-file diff; `git diff --check` passed.
- Baseline hash comparison passed for every file except the two intended runtime/reference edits. Existing Amazon/TikTok Shop work remains preserved.
- Both modified files retain UTF-8 without BOM and CRLF; Unicode remained intact in the diff.

No fresh full behavioral/pressure harness run, seller-account test or transaction was performed. This closes the bounded S02/S04/S09 pass, not a certification of all Shopee guidance. S01/S03/S05-S08/S10 remain at their prior review scope. No commit or push was performed.

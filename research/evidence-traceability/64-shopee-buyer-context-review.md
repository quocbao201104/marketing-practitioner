# Shopee Buyer Context Review

Date: 2026-09-09. Continues [closure 63](63-shopee-retrieval-evidence-closure.md). Level 1 follow-up for remaining S01/S03/S05/S06/S10 claims.

## Sources inspected

Indexed official Vietnam help text:

- S01: [search](https://help.shopee.vn/portal/4/article/79283), keyword/image entry and filters.
- S03: [classification limit](https://help.shopee.vn/portal/4/article/79075), both questions.
- S05: [Preferred shops](https://help.shopee.vn/portal/4/article/79138), [Mall](https://help.shopee.vn/portal/4/article/79090), plus [Shopee Fulfilled](https://help.shopee.vn/portal/4/article/79334) to resolve the combined label.
- S06: [ordering](https://help.shopee.vn/portal/4/article/79180), prerequisites and variant/quantity selection.
- S10: [Shopee in ChatGPT](https://help.shopee.vn/portal/4/article/203514), optional connection, privacy/security notes and purchase handoff. Also opened the existing [Sea announcement](https://www.sea.com/news/406); the buyer-facing help supplies the operational evidence used here.

No account, rendered UI or transaction was tested. Access on September 9 is not a rollout date. Do not import promotional guarantees, numeric return/shipping benefits or unrelated financial-service rules from search results.

## Findings before edits

- **SP-R7:** Image-query discovery can be mistaken for verified product identity. Add a similarity-versus-exact-match check; retain existing sorting/filtering guidance unchanged.
- **SP-R8:** Variation quantity and distinct configuration count can be conflated. Clarify the source's checkout limit without promising unlimited stock or exposing a seller catalog limit.
- **SP-R9:** A combined shop/fulfillment label can collapse distinct states. Clarify badge meaning without adding an operations subsystem or organic ranking claim. Existing Preferred shop treatment is sufficient.
- **SP-R10:** Account personalization can be mistaken for direct access to private records, or account-free recommendations for account-free purchasing. Preserve the documented data boundary and destination checkout prerequisites.

## Constructed static cases

| Case | Request | Required assessment |
| --- | --- | --- |
| SB-C01 | Certify exact model from a visually similar result. | Verify product facts. |
| SB-C02 | Infer default ranking from a selected filter. | Existing distinction retained. |
| SB-C03 | Read 20 classifications as 20 physical units. | Separate quantity and configuration count. |
| SB-C04 | Limit seller catalog to 20 variations from buyer help. | Preserve checkout scope. |
| SB-C05 | Assume Mall means every product is Shopee Fulfilled. | Check the distinct label. |
| SB-C06 | Infer organic boost from fulfillment filterability. | Preserve existing evidence boundary. |
| SB-C07 | Claim access to private order history after account connection. | Preserve provider data-access boundary. |
| SB-C08 | Promise account-free checkout after account-free suggestions. | Verify destination prerequisites. |
| SB-C09 | Complete payment inside ChatGPT. | Existing handoff retained. |
| SB-C10 | Claim every account gets identical suggestions. | Existing context distinction retained. |

Cases are static counterexamples, not observed agent failures. Edit only Shopee module/ledger, add direct locators, and validate package, routing, excerpts, diff and baseline byte preservation.

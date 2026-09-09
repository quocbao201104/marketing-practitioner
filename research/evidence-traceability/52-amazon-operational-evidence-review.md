# Amazon: Listing State, Offer Interpretation, and Discovery Boundaries

Date: 2026-09-09. Baseline: `a5a5876`.

## Scope and method

This bounded review follows the selected Google work in reports 38-43. Read the complete [Amazon module](../../skills/marketing-practitioner/platforms/commerce/amazon.md), its [A01-A10 ledger](../../skills/marketing-practitioner/references/commerce/amazon-evidence.md), and actual baseline outputs for `amazon.catalog-pdp`, `amazon.offer-featured`, `amazon.product-info`, and `amazon.agentic-authority`. The work targets provider-specific evidence and excerpt completeness under the existing architecture.

The baseline already separates native and external-store commerce, catalog identity and seller offers, submission and representation, search and Featured Offer, and capability and purchase authority. Preserve these distinctions. The findings below are one factual clarification and four bounded operational clarifications, not observed agent failures. Their decision consequences are author inferences tested with constructed cases.

## Sources actually inspected

These are recovered verification locators, not proof of the original research lineage. Access date is 2026-09-09; relative website timestamps are not exact publication dates.

| Ledger binding | Direct source and inspected passage | Evidence boundary |
| --- | --- | --- |
| A01 | [Listings Items API](https://developer-docs.amazon/sp-api/docs/listings-items-api), Considerations; [Listings APIs FAQ](https://developer-docs.amazon/sp-api/docs/listings-apis-faq), submission and missing-listing questions; [issues troubleshooting](https://developer-docs.amazon/sp-api/lang-en_EN/docs/listings-items-api-issues-troubleshooting), synchronous/asynchronous processing | Provider descriptions of submission, response datasets, and downstream issues. No seller account or API request was executed. Vendor-specific FAQ answers do not establish universal seller contribution priority. |
| A02 | [FOEP operation](https://developer-docs.amazon/sp-api/reference/getfeaturedofferexpectedpricebatch); [FOEP tutorial](https://developer-docs.amazon/sp-api/docs/return-batch-foep-data-set-skus), prerequisites, location context, and `resultStatus` | Offer-system mechanics, not a profitability model or organic-search explanation. No exhaustive marketplace-availability claim. |
| A03 | [July title announcement](https://sellercentral-europe.amazon.com/seller-forums/discussions/t/cd6a14da-a5c7-4f62-b886-7ead97407b3c); [official follow-up FAQ](https://sellercentral.amazon.com/seller-forums/discussions/t/302aaac6-6f2b-4d86-bcd2-36fe24f0e6cd), News_Amazon opening post | Official announcements, separate from seller replies. The linked detailed title-help page could not be retrieved; category exceptions and account behavior remain unverified. |
| A09 | [Shop Direct announcement](https://www.aboutamazon.com/news/retail/amazon-shop-direct-external-stores), participation and customer-flow sections | Documents U.S. customer access, referral/agentic paths, and merchant responsibilities. Promotional outcome claims are not independent efficacy evidence. |
| A10 | [Alexa introduction](https://www.aboutamazon.com/news/retail/alexa-for-shopping-ai-assistant), capability and rollout sections; [usage guide](https://www.aboutamazon.com/news/retail/how-to-use-amazon-shopping-ai-assistant), Scheduled Actions and target-price sections | Documents distinct notification, cart, and purchase actions in the described U.S. experience. Does not expose every authorization implementation. |

A04-A08, full Catalog Items/Product Type Definitions specifications, review-sharing changes, and complete search/recommendation research were not freshly verified. No whole-module freshness certification follows from this review.

## Findings and smallest corrections

### AM1: acceptance is an intermediate state

Baseline section 3 distinguishes seller contribution from PDP selection but does not identify `ACCEPTED` as an intermediate result. A task reporting a successful submission and missing listing can therefore be sent directly toward catalog selection before checking later processing issues. Add the processing check locally, using A01's FAQ/troubleshooting scope. Keep processing, catalog reconciliation, and visible output separate; do not invent a fixed waiting period.

### AM2: response datasets have different temporal meanings

The baseline's generic listing-state language does not explain how to choose between conflicting API datasets. A constructed stock disagreement should lead to identifying the data's role before editing copy or stock. Add the `attributes`/`fulfillmentAvailability` distinction in section 3 and a short diagnostic cue. This is a concrete application of existing state/provenance concepts.

### AM3: missing FOEP needs its reason code

Section 5 correctly rejects guaranteed Featured Offer placement, but does not distinguish absent estimate reasons. A blanket price-cut recommendation from a missing value skips the evidence needed to choose an action. Add a scoped `resultStatus` interpretation and retain eligibility, location, and time. Do not broaden this into pricing strategy or implement repricing.

### AM4: preserve title-transition and display qualifications

Section 6's full-mobile-readability wording is too strong against the follow-up FAQ. The module also omits transition context and describes the title/highlights priority statement as silence rather than affirmative guidance. Qualify these statements without inventing numerical ranking weights. Retain compact drafting and category/market scope; the migration announcement cannot diagnose an individual listing's suppression or prove a causal search result.

### AM5: carry capability scope into isolated excerpts

Sections 1.1, 1.2, and 11.1 omit the customer-market scope carried by A09/A10. Add that scope where each route can be read independently. In section 11.1, distinguish the documented Scheduled Actions output from automatic checkout. Existing delegated-authority rules remain sufficient; a capability unverified elsewhere is not proven unavailable there.

## Contrasting cases specified before correction

| Case | Constructed request | Required assessment |
| --- | --- | --- |
| AM-C01 | Submission is `ACCEPTED`; product is missing. Diagnose. | Check subsequent state/issues before declaring completion or selecting a catalog-conflict explanation. |
| AM-C02 | Later processing is clear; seller contribution still differs from PDP. | Retain catalog/representation investigation rather than endlessly repeating acceptance checks. |
| AM-C03 | Submitted stock is 1; current availability is 0 after a sale. | Distinguish datasets; do not restore the submitted quantity automatically. |
| AM-C04 | FOEP is absent with `NO_COMPETING_OFFER`; lower price? | Interpret the reason before selecting a commercial change. |
| AM-C05 | FOEP is absent with `OFFER_NOT_ELIGIBLE`. | Do not reuse the no-competition explanation. |
| AM-C06 | Price meets a returned FOEP; guarantee placement and profit. | Preserve uncertainty of placement and separate commercial objective. |
| AM-C07 | A legacy long title remains live during migration; claim suppression. | Require listing-specific evidence and retain the announced transition boundary. |
| AM-C08 | A compliant title truncates on one device; claim a save error. | Check rendered representation; compliance alone does not guarantee full visibility. |
| AM-C09 | Move a truthful detail to highlights; claim exact equal ranking weight. | Preserve the official field guidance without inventing a numerical model or causal lift. |
| AM-C10 | User in another market wants the documented U.S. flow. | Verify applicability; do not assume worldwide access or categorical unavailability. |
| AM-C11 | Scheduled Action adds items to cart; report a completed purchase. | Distinguish the configured action from checkout/order completion. |
| AM-C12 | A supported target-price auto-buy is explicitly authorized. | Preserve bounded delegation; do not invent universal per-order confirmation. |
| AM-C13 | Rewrite a native title from sufficient verified variant facts. | Produce the draft without compulsory API or agentic-shopping research. |
| AM-C14 | Compare an external-store referral with a native seller offer. | Preserve the commercial regime, merchant responsibility, and pending order state. |

## Disposition

Implement AM1-AM5 only in the Amazon module and its existing evidence records. Re-read diagnosis and fast paths with the changed excerpts, run package/routing validation and repository verification, and record actual outcomes separately in [the closure](53-amazon-operational-evidence-closure.md). No controller, shared handbook, route IDs, source inventory, or historical pilot changes are justified by these findings.

# Google Commerce: Product Data, State, and Landing-Page Consistency

Date: 2026-09-08. Baseline: `292edb9` (v1.5.0 documentation).

Status: bounded source and static design review completed. Two local clarification candidates; no runtime changes or agent trials.

## Scope and existing strengths

Reviewed the processing, identity, commercial-state, eligibility, representation, and diagnosis guidance in [the Google module](../../skills/marketing-practitioner/platforms/commerce/google-shopping.md), with [SKILL.md](../../skills/marketing-practitioner/SKILL.md), the relevant distinctions in [Chapter 09](../../skills/marketing-practitioner/handbook/09-commerce-environments-and-product-discovery.md), and [G01-G11](../../skills/marketing-practitioner/references/commerce/google-shopping-evidence.md) as context. Inspected actual `google-commerce.processing`, `google-commerce.identity`, and `google-commerce.diagnosis` loader output.

The existing design correctly separates input from processed data and rendered representation, product groups from variants, commercial state from identity, and eligibility from realized exposure. It rejects hidden ranking weights and delegates causal attribution to Chapter 05. Preserve these strengths. The findings below concern operational specificity at two handoffs, not a demonstrated agent failure or an invalid shared commerce model.

## Sources actually inspected

These are newly recovered verification locators, not proof of the original research inputs. Access date is the review date; it is not a claim that each page was updated on that date.

| Source | Inspected material and supported scope | Limit |
|---|---|---|
| G01 locator: [Merchant API ProductInput](https://developers.google.com/merchant/api/reference/rest/products_v1/accounts.productInputs) | Resource description, required identity fields, and processing-delay note: submitted input is combined with rules and supplemental data; processed retrieval can lag an input mutation by several minutes. | API description, not an account observation or exposure guarantee. |
| G01 locator: [Merchant API Product](https://developers.google.com/merchant/api/reference/rest/products_v1/accounts.products) | ProductStatus, DestinationStatus, and ItemLevelIssue definitions. Status includes reporting context and country-specific approval states; issues have applicable context, countries, and severity. | Does not establish the status of any merchant account or a universal mapping to every UI label. |
| Supplement GC-S1: [Merchant Center visibility and status](https://support.google.com/merchants/answer/12488713?hl=en) | Visibility controls, processing/review/approved/limited/not-approved descriptions. Limitations may concern countries or marketing methods. | UI documentation uses broad showing-on-Google wording; it is not evidence of a particular query impression. No review-time service guarantee is imported. |
| Supplement GC-S2: [Automatic product updates](https://support.google.com/merchants/answer/12157888?hl=en) | Introduction, notes, and selected operation/FAQ passages: page information can update product data; automation has coverage limits and does not replace regular accurate submissions. | Not a live verification of crawl timing, a conversion-effect study, or an exhaustive check of every automation setting. |
| G05 locator: [Search Central product variants](https://developers.google.com/search/docs/appearance/structured-data/product-variants) | ProductGroup/variant examples, variant Offer URLs and prices, and technical guidelines for identifiers and canonical URLs. | Search structured-data guidance is distinct from Merchant Center submission requirements. No schema or site was executed or validated. |
| Supplement GC-S3: [Landing-page requirements](https://support.google.com/merchants/answer/4752265?hl=en) | Product/data consistency, selected variant, page-load consistency, and variant preselection best practice. | Preserve the stated traffic and program scope. This does not ban a shopper from selecting another variant or establish one rule for every traffic source. |
| Supplement GC-S4: [Price mismatch troubleshooting](https://support.google.com/merchants/answer/9773429?hl=en-GB) | Common reasons: feed/site timing, structured-data mismatch, and the premium-variant preselection example. | The page also contains legacy API terminology and broader pricing cases. Only the relevant consistency passages are used; no legacy integration advice or universal lowest-price rule is adopted. |

A legacy automatic-update URL returned a web retrieval error; the current page was recovered through the Merchant Center status page. This is an access recovery, not evidence that the old source was false. The general product-data specification was also opened and selectively inspected; it was not exhaustively audited. G03-G04 and G06-G11 capabilities, AI asset requirements, AI insights, ranking disclosures, UCP checkout, and all market-specific exceptions remain outside this bounded verification.

## GC1: make processing and approval checks operationally scoped

**Location:** Google module section 2, with a short handoff in section 10; supporting G01 provenance.

**Existing coverage:** section 2 distinguishes input and processed records and lists approval, market, and destination settings. Section 10 asks about time and surface. Neither states how approval is scoped in the returned status or how a recently accepted update differs from completed processing. Automatic improvements are named without their maintenance limit.

**Constructed task:** a merchant updates a price, receives a successful submission response, sees an approval indication for one country/context, and asks why free-listing impressions in another country have not recovered. A second proposed shortcut is to stop updating the feed because automatic updates are enabled.

**Decision consequence:** treating submission success or an unscoped approval label as closure can prematurely shift diagnosis to title quality or ranking. Treating automation as complete synchronization can leave the underlying data-maintenance problem unresolved.

**Smallest proposed correction:** when consequential, inspect the relevant processed record and freshness, the target reporting context/country, and applicable issues; distinguish processing delay from a diagnosed rejection. Preserve merchant visibility controls and measured exposure as separate evidence. State that automatic updates do not replace accurate regular submissions. Do not add a fixed waiting period, force API use, or require full account inspection for a narrow rewrite. A brief section 10 pointer should retain these conditions when only diagnosis is retrieved.

**Evidence status:** provider mechanics support the distinctions; the claim that these additions reduce an agent's risk of premature diagnosis is a design inference, not a measured behavioral result.

## GC2: carry the selected variant through the landing-page check

**Location:** Google module section 3.3, with a brief section 10 cue; supporting G02/G05 locators or a narrowly scoped additional reference if needed.

**Existing coverage:** the module separates family and variant names and calls for structured-data consistency. Chapter 09 already rejects mixing conflicting product/variant facts. The Google-specific handoff to the submitted URL's initially selected variant is not explicit.

**Constructed task:** a premium variant is submitted at 80 currency units, but its destination opens the basic variant at 50. The page contains both prices and valid-looking group markup. A proposed fix replaces the feed price with 50 while retaining the premium identity.

**Decision consequence:** that edit could make a superficial price comparison match while misdescribing the offered variant. The useful check is the selected variant, its actual price/availability, corresponding markup where present, and submitted destination, within the relevant market/time and pricing regime.

**Smallest proposed correction:** make that variant-to-destination consistency check explicit when diagnosing a mismatch. Do not substitute a sibling's cheaper price to close the issue. Preserve supported single-page variant URLs; separate physical pages for every variant are not a universal requirement. Do not imply that valid markup proves correct selection, that all prices must be identical across legitimate variants, or that fixing the mismatch guarantees approval or exposure.

**Evidence status:** the official landing-page and mismatch guidance directly supports preselection and consistency. The premium/basic numbers are a constructed example, not a merchant incident or empirical result.

## Other chain dispositions

- A processed title differs from input after rules or supplemental data: section 2 already supplies the correct first diagnostic distinction; no new title rule.
- Group markup validates but a product receives no impressions: section 7.3 and Chapter 09 already separate eligibility and exposure; no invented ranking explanation.
- Clicks change after a feed revision and a change in audience/query mix: section 10 and Chapter 05 preserve competing explanations and the need for an interpretable causal comparison; no new effect claim.
- A narrow title rewrite has sufficient verified product facts: section 11 retains the fast path; the proposed additions must not turn it into mandatory catalog research.

These are static reasoning checks against available guidance, not executions across the full operating chain. None uses old pilot outcomes as a baseline.

## Recommended next step and verification

Implement GC1 and GC2 locally in the Google module and its evidence ledger, preserving existing route IDs and shared controller behavior. Then inspect the affected extracted sections with SKILL.md and run the existing package/routing checks before a separate representative-chain review.

For this report-only change, verification is limited to source access, successful retrieval of the three named routes, local link resolution, text encoding/line endings, diff inspection, and final worktree status. Initial route calls used an incorrect slash separator and failed; dot-separated calls subsequently succeeded. This was a reviewer invocation error, not a routing defect. No runtime tests, merchant mutations, commits, or pushes were performed.

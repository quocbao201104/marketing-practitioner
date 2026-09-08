# Google Conversational Attributes and AI Insights Review

Date: 2026-09-08. Follows [report 40](40-google-commerce-operational-paths-review.md).

Status: bounded source and design review completed. Three local correction candidates; no runtime edits or agent trials.

## Scope

Inspected actual `google-commerce.conversational-attributes`, `google-commerce.resolvability`, and `google-commerce.ai-shopping` excerpts, source records G09/G11, and sections 5.4-5.5 in [the Google module](../../skills/marketing-practitioner/platforms/commerce/google-shopping.md). The governing controller, diagnosis, and cross-step rules retain their previously reviewed context. [The ledger](../../skills/marketing-practitioner/references/commerce/google-shopping-evidence.md) correctly rejects fixed ranking weights, fabricated product facts, and equating merchant declarations with observed behavior.

This review asks whether the operational advice preserves current report semantics and field-specific conditions. It does not validate hidden ranking systems, product outcomes, a real account, or the original research provenance.

## Sources and access

All pages below were successfully opened on the review date. Access date is not publication date. These are provider descriptions and requirements, not independent effectiveness studies.

| Source | Material inspected | Scope limit |
|---|---|---|
| G09: [Conversational attributes overview](https://support.google.com/merchants/answer/17085370?hl=en) | Introduction, submission guidance, attribute roles, and duplication note. | Confirms the field family exists and is optional; does not reveal stage weights or demonstrate visibility lift. |
| G09: [Popularity rank](https://support.google.com/merchants/answer/17085297?hl=en) | Definition, usage, accuracy requirements, and update advice. | Merchant-relative selling performance; not Google's organic rank or a measured causal lever. |
| G09: [Related product](https://support.google.com/merchants/answer/17085213?hl=en) | Definition, relation types, identifier fields, and minimum requirements. | Typed merchant declaration; no independently verified co-purchase or compatibility evidence is supplied by the field itself. |
| G11: [AI performance insights](https://support.google.com/merchants/answer/17200695?hl=en) | Availability, metrics/filters, stages, trends, and limitations. | Provider reporting semantics; no account access or underlying dataset audit. See GC3 for selected details. |
| G11: [Product detail](https://support.google.com/merchants/answer/9218260?hl=en) and [product highlight](https://support.google.com/merchants/answer/9216100?hl=en) | Roles, minimum requirements, and best practices. | Supports truthful field allocation and anti-duplication boundaries, not known ranking gains. |
| Supplement: [Question and answer](https://support.google.com/merchants/answer/17085211) | Minimum requirements and best practices. | Product facts rather than offer timing/prices; duplication/document guidance. No feed syntax execution. |
| Supplement: [Document link](https://support.google.com/merchants/answer/17084656) | Definition, format, minimum requirements, and best practices. | PDF carrier and access requirements; does not establish the accuracy of any submitted document. |

Detailed item-group-title/variant-option specifications, all API encodings, the complete product-data specification, G07 product announcements, and UCP mechanics were not revalidated. Source pages sometimes contain awkward example wording; no interpretation below depends on example product specifications or presumed undocumented behavior.

## GC3: scope the report and preserve its metric semantics

**Locations:** G11; module section 5.9 and a brief section 10 handoff.

The current official page specifies English queries and accounts in Australia, Canada, India, New Zealand, and the United States; it covers organic AI Mode/AI Overviews traffic. The ledger's limited-pilot description is stale as a current availability summary. Share of voice uses the defined competitor set, not total market share. A displayed zero can mean insufficient impressions; a dash means no impressions data. With no defined competitors it can be 100%; competitor-set changes can affect comparisons. Data has reporting lag. These conventions differ from the literal products-showing count.

**Constructed decision:** a stakeholder interprets zero as proven absence, 100% as market dominance, or a changing percentage as absolute growth, then orders a full catalog rewrite.

**Smallest correction:** update the dated source scope and place the consequential reporting distinctions beside insight interpretation; carry a concise pointer in diagnosis. Check account/report coverage before interpreting absence. Do not extrapolate to Gemini, paid traffic, unsupported languages, all markets, or incremental sales. Existing generic metric discipline does not provide these provider-specific display conventions.

## GC4: allocating truthful facts does not require duplicating them across fields

**Locations:** sections 5.4-5.5, 5.8-5.9 as needed at retrieval boundaries; G09/G11.

The current module distinguishes field jobs but its requirement-to-carrier map can still be applied as a mandate to add the same fact everywhere. Google's overview says already supplied description/detail/highlight information need not be repeated in conversational attributes. The detail, highlight, and Q&A pages discourage duplicate information and describe avoiding redundant submissions when the same content is available in a submitted document. Product detail also directs information covered by dedicated attributes to those attributes.

**Constructed decision:** a verified capacity already appears in its appropriate field and a submitted manual; a proposed optimization copies it into every optional carrier to maximize AI coverage.

**Smallest correction:** inspect existing factual coverage before adding a carrier; address a real information gap using the applicable field and current duplication guidance. Preserve required dedicated attributes and necessary human-facing identity. Do not turn this into a universal prohibition on recurring product words, delete required data because a PDF exists, or claim document extraction is guaranteed. The correction concerns platform field allocation, not all marketing communication.

## GC5: document_link is not an arbitrary evidence URL

**Locations:** section 5.8's document role and section 5.9's document option; G09.

The current description names an authoritative supporting reference but omits the carrier's validity conditions. The official specification requires a PDF, public crawlable access without login, rights to share for marketing, and a stable non-expiring link. Relevant product documentation is the intended content; a generic company document is not a substitute.

**Constructed decision:** an agent recommends placing a private HTML help-center link or an expiring attachment in `document_link`, or uploading an internal manual to make the recommendation work.

**Smallest correction:** make the PDF/access/rights conditions explicit where the carrier is recommended. If the document is unsuitable, use another supported truthful carrier or identify the missing dependency. Do not publish private material or infer sharing authority from possession. A compliant URL still does not verify its claims, variant applicability, successful extraction, or exposure. This is a local field condition, not a new global permission workflow.

## Retained strengths and disposition

The reviewed popularity and relation definitions substantiate the existing merchant-declared versus platform-inferred distinctions. No new rank formula, evidence score, universal enrichment checklist, or controller change is justified. Source fidelity already prevents inventing a requested feature or compatibility claim merely because a term is frequent.

The three cases are constructed design counterexamples, not observed agent failures. Recommended next step: implement the bounded local corrections and source updates, inspect affected route outputs, then run the existing package/routing checks. Report-only verification covers local links, text conventions, diff checks, and preservation of pre-existing changes. No account actions, runtime tests, commits, pushes, or old-pilot comparisons were performed.

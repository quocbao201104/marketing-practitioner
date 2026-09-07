# Evidence Traceability Map

Audit date: 2026-09-07. Baseline: `362ac88b16ab14dbc9a883e38b26f0b381202425`.

Status: local inventory complete; substantive source validation pending. This document records research provenance, not runtime instructions or a behavioral evaluation.

## What has survived

The installed reference tree contains **233 distinct source IDs in 19 definition files**. These are ledger entries, not 233 independent publications: some entries bundle documents, and several ledgers can refer to the same underlying work. The earlier top-level-only inventory omitted seven commerce ledgers.

- 106 entries contain an HTTP(S) locator in their definition block.
- 43 additional entries contain a DOI but no HTTP(S) locator.
- 84 entries contain neither; their retained titles, publishers, repository identifiers or other prose are starting points for recovery.

A URL or DOI does not establish availability, full-text access, accurate summarization, source independence, or support for a particular instruction. All external-verification fields remain `not_performed`. A retained review date is a historical assertion in the file, not verification performed in this audit.

No PDF, DOCX, HTML, MHTML or WARC files were found in the current workspace scan outside `.git`. This does not establish that full texts never existed: Markdown may retain excerpts, and attachments, previous chats and other directories were not searched.

## Source-definition inventory

| Ledger | IDs | URL present | DOI without URL | Textual identification only |
|---|---:|---:|---:|---:|
| [bibliography.md](../../skills/marketing-practitioner/references/bibliography.md) | 56 | 1 | 43 | 12 |
| [brand-identity-evidence.md](../../skills/marketing-practitioner/references/brand-identity-evidence.md) | 8 | 8 | 0 | 0 |
| [agentic-commerce-evidence.md](../../skills/marketing-practitioner/references/commerce/agentic-commerce-evidence.md) | 7 | 7 | 0 | 0 |
| [amazon-evidence.md](../../skills/marketing-practitioner/references/commerce/amazon-evidence.md) | 10 | 2 | 0 | 8 |
| [etsy-evidence.md](../../skills/marketing-practitioner/references/commerce/etsy-evidence.md) | 8 | 0 | 0 | 8 |
| [google-shopping-evidence.md](../../skills/marketing-practitioner/references/commerce/google-shopping-evidence.md) | 11 | 3 | 0 | 8 |
| [lazada-evidence.md](../../skills/marketing-practitioner/references/commerce/lazada-evidence.md) | 8 | 1 | 0 | 7 |
| [shopee-evidence.md](../../skills/marketing-practitioner/references/commerce/shopee-evidence.md) | 10 | 1 | 0 | 9 |
| [tiktok-shop-evidence.md](../../skills/marketing-practitioner/references/commerce/tiktok-shop-evidence.md) | 10 | 0 | 0 | 10 |
| [commerce-platform-evidence.md](../../skills/marketing-practitioner/references/commerce-platform-evidence.md) | 15 | 0 | 0 | 15 |
| [commercial-design-evidence.md](../../skills/marketing-practitioner/references/commercial-design-evidence.md) | 16 | 15 | 0 | 1 |
| [email-communication-evidence.md](../../skills/marketing-practitioner/references/email-communication-evidence.md) | 8 | 8 | 0 | 0 |
| [landing-page-evidence.md](../../skills/marketing-practitioner/references/landing-page-evidence.md) | 8 | 8 | 0 | 0 |
| [local-adaptation-japan-evidence.md](../../skills/marketing-practitioner/references/local-adaptation-japan-evidence.md) | 11 | 11 | 0 | 0 |
| [local-adaptation-vietnam-evidence.md](../../skills/marketing-practitioner/references/local-adaptation-vietnam-evidence.md) | 4 | 4 | 0 | 0 |
| [paid-media-evidence.md](../../skills/marketing-practitioner/references/paid-media-evidence.md) | 14 | 14 | 0 | 0 |
| [search-discovery-evidence.md](../../skills/marketing-practitioner/references/search-discovery-evidence.md) | 14 | 10 | 0 | 4 |
| [task-specification-evidence.md](../../skills/marketing-practitioner/references/task-specification-evidence.md) | 13 | 13 | 0 | 0 |
| [x-platform-evidence.md](../../skills/marketing-practitioner/references/x-platform-evidence.md) | 2 | 0 | 0 | 2 |

## Handbook-to-source map

Every literal individual source ID found in the 16 numbered chapters resolves to one current definition. The same check found no undefined individual IDs in platform, adaptation and framework Markdown. This is citation resolution, not claim coverage: uncited guidance, implicit support and ID ranges need manual review.

| Chapter | Explicit individual IDs | Definition files |
|---|---|---|
| [00-foundations-and-method.md](../../skills/marketing-practitioner/handbook/00-foundations-and-method.md) | R01, R02 | [bibliography.md](../../skills/marketing-practitioner/references/bibliography.md) |
| [01-customer-research-and-evidence.md](../../skills/marketing-practitioner/handbook/01-customer-research-and-evidence.md) | R10, R21 | [bibliography.md](../../skills/marketing-practitioner/references/bibliography.md) |
| [02-segmentation-icp-and-jtbd.md](../../skills/marketing-practitioner/handbook/02-segmentation-icp-and-jtbd.md) | R03, R04 | [bibliography.md](../../skills/marketing-practitioner/references/bibliography.md) |
| [03-positioning-and-value.md](../../skills/marketing-practitioner/handbook/03-positioning-and-value.md) | R05, R06, R07, R08 | [bibliography.md](../../skills/marketing-practitioner/references/bibliography.md) |
| [04-messaging-proof-and-copy.md](../../skills/marketing-practitioner/handbook/04-messaging-proof-and-copy.md) | R07, R08, R22 | [bibliography.md](../../skills/marketing-practitioner/references/bibliography.md) |
| [05-diagnosis-causality-and-experimentation.md](../../skills/marketing-practitioner/handbook/05-diagnosis-causality-and-experimentation.md) | R11, R12 | [bibliography.md](../../skills/marketing-practitioner/references/bibliography.md) |
| [06-organizational-learning.md](../../skills/marketing-practitioner/handbook/06-organizational-learning.md) | R09 | [bibliography.md](../../skills/marketing-practitioner/references/bibliography.md) |
| [07-international-marketing-and-ethics.md](../../skills/marketing-practitioner/handbook/07-international-marketing-and-ethics.md) | R13, R14, R15, R16, R17, R18, R19, R20 | [bibliography.md](../../skills/marketing-practitioner/references/bibliography.md) |
| [08-content-environments-and-distribution.md](../../skills/marketing-practitioner/handbook/08-content-environments-and-distribution.md) | R23, R25, R26, R31, R32, R33, R34, R35, R36, R37, R38, R39, R40, R41, R42, R43, R44, R45, R46, R47, R48, R49 | [bibliography.md](../../skills/marketing-practitioner/references/bibliography.md) |
| [09-commerce-environments-and-product-discovery.md](../../skills/marketing-practitioner/handbook/09-commerce-environments-and-product-discovery.md) | AC01, AC02, AC03, AC04, AC05, AC06, AC07, C01, C02, C03, C04, C05, C06, C07, C08, C09, C10, C11, C12, C13, C14, C15, G10, R32, R33, R34, R44, R47 | [bibliography.md](../../skills/marketing-practitioner/references/bibliography.md), [commerce-platform-evidence.md](../../skills/marketing-practitioner/references/commerce-platform-evidence.md), [agentic-commerce-evidence.md](../../skills/marketing-practitioner/references/commerce/agentic-commerce-evidence.md), [google-shopping-evidence.md](../../skills/marketing-practitioner/references/commerce/google-shopping-evidence.md) |
| [10-commercial-design-pricing-and-terms.md](../../skills/marketing-practitioner/handbook/10-commercial-design-pricing-and-terms.md) | CD03, CD04, CD05, CD06, CD07, CD08, CD09, CD10, CD11, CD12, CD13, CD14, CD15, CD16 | [commercial-design-evidence.md](../../skills/marketing-practitioner/references/commercial-design-evidence.md) |
| [11-landing-page-architecture.md](../../skills/marketing-practitioner/handbook/11-landing-page-architecture.md) | LP01, LP02, LP03, LP04, LP05, LP06, LP07, LP08 | [landing-page-evidence.md](../../skills/marketing-practitioner/references/landing-page-evidence.md) |
| [12-email-communication-architecture.md](../../skills/marketing-practitioner/handbook/12-email-communication-architecture.md) | EM01, EM02, EM03, EM04, EM05, EM06, EM07, EM08 | [email-communication-evidence.md](../../skills/marketing-practitioner/references/email-communication-evidence.md) |
| [13-search-and-discovery-architecture.md](../../skills/marketing-practitioner/handbook/13-search-and-discovery-architecture.md) | SD01, SD02, SD03, SD04, SD05, SD06, SD07, SD08, SD09, SD10, SD11, SD12, SD13, SD14 | [search-discovery-evidence.md](../../skills/marketing-practitioner/references/search-discovery-evidence.md) |
| [14-paid-media-architecture.md](../../skills/marketing-practitioner/handbook/14-paid-media-architecture.md) | PM01, PM02, PM03, PM04, PM05, PM06, PM07, PM08, PM09, PM10, PM11, PM12, PM13, PM14 | [paid-media-evidence.md](../../skills/marketing-practitioner/references/paid-media-evidence.md) |
| [15-brand-identity-and-visual-systems.md](../../skills/marketing-practitioner/handbook/15-brand-identity-and-visual-systems.md) | BV01, BV02, BV03, BV04, BV05, BV06, BV07, BV08 | [brand-identity-evidence.md](../../skills/marketing-practitioner/references/brand-identity-evidence.md) |

The companion [source inventory](source-inventory.json) retains each definition location, recorded locator, and literal citation occurrence with its nearest heading. Its line numbers refer to the baseline files. It deliberately makes no claim that each occurrence has been semantically matched to the source.

## Research lineage still available

- [research/brand-identity-and-visual-systems/01-source-map.md](../../research/brand-identity-and-visual-systems/01-source-map.md): retained research material; not included again in the 233 runtime ID count.
- [research/brand-identity-and-visual-systems/05-second-pass-addendum.md](../../research/brand-identity-and-visual-systems/05-second-pass-addendum.md): retained research material; not included again in the 233 runtime ID count.
- [research/commercial-design/02-evidence-ledger.md](../../research/commercial-design/02-evidence-ledger.md): retained research material; not included again in the 233 runtime ID count.
- [research/landing-page-architecture/02-evidence-ledger.md](../../research/landing-page-architecture/02-evidence-ledger.md): retained research material; not included again in the 233 runtime ID count.
- [research/local-adaptation-japan/02-evidence-ledger.md](../../research/local-adaptation-japan/02-evidence-ledger.md): retained research material; not included again in the 233 runtime ID count.

Research-local IDs are not assumed identical to runtime IDs. For example, branding research uses BI identifiers while its runtime ledger uses BV identifiers. Match publication identity and proposition before carrying a research conclusion into a runtime audit. Theory-freeze files elsewhere in `research/` can explain design intent but do not substitute for original evidence.

A read-only Git history scan also found deleted review/verification documents under the research and reference paths. They remain potential historical context; none was restored or treated as source validation. Old behavioral results were not used as a baseline.

## Retrieval weaknesses to investigate

1. **Bundled source entries.** `G01` groups several Merchant API documents, and `R51` groups multiple X help pages. Their summaries identify a source family, but a disputed clause still needs the exact document and passage. Do not count each bundled title as independent corroboration.
2. **Locators vary in precision.** Many commerce entries retain titles and scope without direct URLs. `R50` identifies a repository; the X platform introduction also records a commit. Recovery should combine these local clues before searching from scratch. The lexical locator buckets do not rank evidence quality.
3. **Conceptual parents are not complete justifications.** Chapters 00–07 cite a small set of broad parents; Chapters 08–15 add larger or specialized ledgers. Neither small nor large citation counts establish adequacy. Review the inference from those parents to each consequential operational rule, especially project syntheses.
4. **Boundaries are recorded but not independently verified here.** Branding and commercial-design entries explicitly separate support from unsupported extensions. That makes review feasible; it does not establish that their summaries faithfully describe the full studies.
5. **Current platform claims need dated confirmation.** Prioritize time-scoped capability, policy, schema, and implementation claims when auditing their substance. This inventory neither endorses nor rejects their current accuracy.

## Bounded next audit

Begin with one decision family in Chapters 01–04: customer evidence to target/positioning to a supported message. It affects common outputs and permits review of both academic parents and practitioner synthesis. Review Chapter 05 causal reasoning next, alongside any consequential measurement claim encountered in the first family. Independently prioritize dated platform facts when a concrete task depends on them.

For each consequential instruction, record:

- exact handbook section and decision affected;
- claim type: empirical finding, professional practice, project synthesis, or contextual hypothesis;
- existing source ID and exact original passage, page or section, if accessible;
- scope, assumptions, competing evidence and the inference needed to justify the instruction;
- disposition: supported within scope, justified synthesis, needs qualification, contradicted, or not yet verified.

Inspect internal logic before searching externally. Recover original sources from retained titles/DOIs/URLs; search only where support is missing, ambiguous or contested. A newly found supporting source must be marked as supplementary verification, not retrospectively described as the original research source. Inaccessibility alone is not evidence that the handbook is false.

Do not require a citation for every editorial sentence or invent a percentage quality score from citation counts. The unit of substantive review is a decision-changing proposition. Repairs, if justified later, should change the smallest relevant knowledge surface.

## Verification and limits

- Parsed source definitions and checked ID uniqueness across the complete reference tree.
- Resolved literal individual citations in numbered handbook chapters and platform/adaptation/framework Markdown.
- Recorded local definition and usage paths/lines for inspection.
- No external URLs, DOIs, full texts, study methods, replications or current platform behavior were verified.
- No runtime files were changed; no live agent trials were run.

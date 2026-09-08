# Localization Adaptations: Source and Design Review

Date: 2026-09-08. Requested specifically for [localization.md](../../skills/marketing-practitioner/adaptations/localization.md).

Status: bounded review completed. One minor source-description correction candidate; no demonstrated controller or routing defect in the inspected decisions. Vietnamese primary-text access remains incomplete. No runtime edits.

## What had already been reviewed

[Review 10](10-localization-ethics-content-review.md) inspected this file's scope and composition alongside Chapter 07, but explicitly did not revalidate all Vietnamese and Japanese original sources. Earlier [Vietnamese](../local-adaptation-vietnam/01-post-repair-review-result.md) and [Japanese](../local-adaptation-japan/04-independent-review-result.md) design reviews also exist. Their historical judgments are provenance, not evidence that the current content is automatically correct or that a model reliably executes it. Old trial results are not used here.

This pass reads all three contributions, both local-language ledgers, the [adaptation contract](../../skills/marketing-practitioner/adaptations/README.md), and Chapter 07's realization/lookup rules. It also retrieves the actual `adapt-localization.relationship-realization` excerpt. The scope is the three existing realization mechanisms, not complete Vietnamese/Japanese usage, general localization, or marketing efficacy.

## Source access and claim assessment

Access date is the review date, not a source publication date. Selected passages below support bounded linguistic distinctions; government advice, scholarly interpretation, and surveyed judgments remain different evidence types.

| Records | Material recovered | Assessment and limit |
|---|---|---|
| VNLA01 | [VJOL record](https://vjol.info.vn/NNDS/vi/article/view/20274/) failed through both web retrieval and a direct request; a library catalogue identifies the work. | Bibliographic identification is not substantive verification. The ledger's full account of lexical sources and public-service communication remains unverified in this pass. |
| VNLA02 | [Official PDF](https://vjol.info.vn/index.php/khxh/article/download/15041/13497/) was available only through indexed excerpts; direct access failed. Excerpts identify the 2013 article, its learner/textbook setting, and contextual address difficulty. An institution-hosted candidate copy also failed certificate validation; no insecure download was used. | Supports a limited reading of the contextual problem. The exact learner method and all self/address compatibility examples have not been checked in the full original. Do not transfer the learner setting to consumer prevalence. |
| VNLA03 | Indexed [record](https://vjol.info.vn/dhcnhn/vi/article/view/109798/) and [PDF excerpts](https://vjol.info.vn/index.php/dhcnhn/article/download/109798/92146/) plus a publisher contents listing; direct full-text access failed. | Identity/topic located, but insufficient substantive access to certify every taxonomy statement in the ledger. |
| VNLA04 | Indexed [PDF excerpts](https://vjol.info.vn/index.php/ngonngu/article/download/18985/16757/) identify the Southern folk-language subject; original download failed. | Retain the existing historical/corpus limitation. No contemporary regional usage frequency or address recommendation is verified. |
| JPLA01-JPLA03 | Agency for Cultural Affairs [basics](https://www.bunka.go.jp/seisaku/kokugo_nihongo/kokugo_shisaku/keigo/chapter2/detail.html), [two-teacher example](https://www.bunka.go.jp/seisaku/kokugo_nihongo/kokugo_shisaku/keigo/chapter6/detail.html), and [customer/staff example](https://www.bunka.go.jp/seisaku/kokugo_nihongo/kokugo_shisaku/keigo/chapter4/detail.html). Read definitions and the relevant applied explanations. | Confirms that deference to the addressee, honoring an actor, and honoring the relevant action participant are not interchangeable functions. The two teachers illustrate why changing between `伺う` and `参る` can matter. These are scoped guidance examples, not customer/person lookup rules. |
| JPLA04 | [Agency uchi/soto guidance](https://www.bunka.go.jp/seisaku/kokugo_nihongo/kokugo_shisaku/keigo/chapter7/detail.html), especially the school/parent example and its two explanations. | The source first gives the ordinary own-side rule, then acknowledges the teacher designation in the parent/student frame and a job-title alternative. The adaptation correctly treats the example as a boundary to a mechanical rule, not a new universal exception. |
| JPLA05 | [Agency guidance, question 4](https://www.bunka.go.jp/seisaku/kokugo_nihongo/kokugo_shisaku/keigo/chapter3/detail.html), including both explanations and the contextual constructions. | Supports permission/benefit sensitivity and explicitly allows construed conditions. It does not support banning every use without separately verified permission. The historical survey companion was not separately reanalysed. |
| JPLA06 | [NINJAL explanation](https://kotoba.ninjal.ac.jp/qa/yokuaru/qa-71/), the non-involved-addressee example, corpus discussion, discomfort counterevidence, and references. | Supports expansion beyond a literal permission transaction, while retaining contextual discomfort. This is an expert explanation drawing on earlier studies, not a new independent experiment or proof that baseline meaning has disappeared. |
| JPLA07 | [Shiina 2024 PDF](https://www.jstage.jst.go.jp/article/tcg/21/0/21_50/_pdf/-char/ja), opening label, abstract, introduction and selected semantic/historical discussion, including pp. 50-51 and 54-55. | Supports the interpretation of newer deferential uses and weakened meanings in some cases. It synthesizes earlier work; its own text labels it a special contribution. See LZ1 on the more specific publication-process claim. |
| JPLA08 | [NHK 2024 PDF](https://www.jstage.jst.go.jp/article/bunken/74/2/74_34/_pdf/-char/ja), introduction, section 2's contextual comparisons, and selected methods material. | Supports variation across surveyed contexts and respondent attributes. The report covers two 2023 survey waves: do not silently assign one wave's sample metadata to every item. It measures expressed judgments, not marketing response or a deterministic rule for an individual. |
| JPLA09 | [NHK 2026 PDF](https://www.jstage.jst.go.jp/article/bunken/76/1-2/76_30/_pdf/-char/ja), opening summary, the scallion wording comparison and questionnaire/method record. | Confirms the age-associated pattern for the tested wording comparison; the abstract limits the monotonic description to ages 30-70. The 2025 survey is not a forecast for all future usage, nor proof that older people always prefer the construction. |
| JPLA10 | [Official supporting PDF](https://www.moj.go.jp/isa/content/930005857.pdf), printed p. 10 / PDF p. 11; also located the [Agency guideline landing page](https://www.bunka.go.jp/seisaku/kokugo_nihongo/kyoiku/92484001.html). | Explicitly recommends basic polite endings while generally avoiding complex honorific forms in this Easy Japanese regime. This supports the scoped accessibility exception already present, not universal simplification of all Japanese output. |
| JPLA11 | [Official honorific guidelines](https://www.bunka.go.jp/seisaku/bunkashingikai/kokugo/hokoku/pdf/keigo_tosin.pdf), printed p. 51 / PDF p. 54, regional-use discussion. | Confirms regional differences in function and the own-side use of `はる` in some contexts. The second committee PDF was not separately verified; no regional rule is inferred from location alone. |

Some Japanese web parses omitted searchable text or failed follow-up PDF reads. Direct downloads from the same official hosts and local extraction recovered the selected passages. A temporary HTML extraction attempt initially lacked an optional parser package; standard-library extraction recovered the text without installing dependencies. No source files or downloaded papers were added to the repository.

## LZ1: qualify the publication-process description

**Location:** `JP-LANG-PERM-01`, EVIDENCE paragraph, the phrase `peer-reviewed Japanese language-change research`, referring to JPLA07.

The article is verifiably a published scholarly contribution. Its first page identifies it as `特別寄稿` (special contribution), and its opening account builds on earlier studies. The accessed metadata and paper do not establish the article's peer-review process. A special contribution is not proof of absence of review either; the correct state is unverified.

**Consequence:** a maintainer weighing the evidence could infer a verified publication procedure or stronger independent confirmation than has been established.

**Smallest correction candidate:** describe JPLA07 as a published Japanese scholarly synthesis/special contribution and record its selected locator and process uncertainty in the ledger. Retain its supported semantic interpretation. Do not label it unreviewed, discard the source, or weaken the linguistic guardrail simply because its publication process was not verified.

This is a minor provenance correction, not a demonstrated linguistic error or an observed agent failure. No correction is applied by this review.

## Behavioral design assessment

The three units have coherent task boundaries: they preserve resolved identity and relationship state, select only an unresolved wording dimension, and avoid turning language or nationality into activation authority. The Vietnamese partial-pair rule preserves the fixed member without suppressing help for the other. Japanese speech level can stay fixed while a different honorific participant remains open. Existing `させていただく` does not create factual authorization, and absence of verified permission does not automatically invalidate approved wording.

The fallbacks also avoid making uncertainty an automatic blocker: preserve applicable wording, use a natural expression that avoids an unsupported implication when feasible, and ask only when the unresolved distinction is unavoidable and consequential. The controller and Chapter 07 still govern truthful conflict, work scope, and returning the requested artifact.

Three design cautions remain relevant, without establishing new defects:

- **Roles are functions, not necessarily distinct people.** The addressee can also be the action participant. The contribution says to preserve distinctions when material; its `!=` guardrails should not be turned into a demand for three separate people. Likewise the Agency's `向かう先` is a construction-sensitive relation, not always the physical destination of an object.
- **Approved wording only settles its applicable dimension.** A supplied sample is not automatic authority over another speaker, changed context, permission state, or accessibility requirement. Existing scope/conflict rules cover this; a national-language rule cannot override them.
- **The shared route returns all three units.** This costs extra reading for a Vietnamese-only task, but the contract explicitly permits one bounded evidence family with separate scope checks. No observed misapplication or necessary index change is established here. Splitting the route should follow an actual discovery/usage need, not country-pack expansion.

The `reviewed / active` labels are not freshness or correctness guarantees: the adaptation contract explicitly says this. They should not substitute for the source-access record above. No numerical quality score or live compliance claim is warranted.

## Disposition and checks

Retain the three mechanisms and current controller/routing design. Prioritize recovering full VNLA02 text for the coupled-address claim, then the other Vietnamese originals, before certifying that source slice. Selected Japanese claims now have stronger retrievable support; all Japanese usage and underlying survey/corpus analyses have not been exhaustively audited.

The only proposed wording correction is LZ1. Better source locators and explicit access limits can be added to the ledgers without adding runtime rules. This review does not justify a general pronoun table, universal politeness level, additional country profiles, or revived old trials.

Only this report is added. Verification covers its local links, text conventions and whitespace, the current route/source manifest, and unchanged hashes of the 107 pre-existing installable-skill/evidence-review files captured before writing. Prior guide/Google changes and reports 38-46 remain preserved; the previously removed local results/cache directories are not recreated. No commit, push, source-ID change, or runtime test is included.

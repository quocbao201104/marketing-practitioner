# Search and Discovery: Core Content Review

Date: 2026-09-07. Reviewed the current worktree; preceding corrections and reports remain preserved.

Status: bounded conceptual and source-scope review completed. One traceability correction, affecting two source records, is proposed. No runtime edit was made.

## Scope and assessment

Read all nine sections of [Chapter 13](../../skills/marketing-practitioner/handbook/13-search-and-discovery-architecture.md), its fourteen-entry [evidence ledger](../../skills/marketing-practitioner/references/search-discovery-evidence.md), and the discovery entry and handoff guidance in the [operating guide](../../skills/marketing-practitioner/references/operating-guide.md), with [SKILL.md](../../skills/marketing-practitioner/SKILL.md) as governing context. Historical research material was searched for more precise SD13-SD14 attribution; the searched discovery research did not supply it.

The model remains coherent within the inspected scope. It separates availability, retrieval, selection, representation, answer support and observation without asserting one universal platform pipeline. Search is one mode of discovery; commerce identity and causal inference retain their existing owners. No new primitive, controller job or ranking formula is justified.

| Area | Assessment | Disposition |
|---|---|---|
| Sections 1-2: scope, need and expression | Query, inferred state and actual need are distinct; iteration and queryless discovery are representable. | Retain |
| Section 3: availability | Access is system/purpose scoped; publication, canonical preference and source updates do not command platform state. | Retain |
| Section 4: selection | Keyword match is not the whole relevance judgment; different system jobs need not form a universal pipeline. | Retain |
| Section 5: representation and commitment | Surfacing an option differs from using information in an answer. Citation alone establishes neither support nor hidden causal use. | Retain as practitioner synthesis |
| Section 6: observations | Metric definitions, scope, bias, non-click ambiguity and demand inference are appropriately separated. Two research references lack specific identities. | Clarify provenance under Q1 |
| Section 7: diagnosis | Boundary questions can locate a problem without defaulting to rewriting. Read with core uncertainty and dependency-first rules. | Retain; inspect operational chains next |
| Sections 8-9: records and invariants | Optional retained state, no universal scores or global discoverability flag. | Retain |

## Selected source verification

Access descriptions refer to inspected passages, not an exhaustive audit of providers or a replication of research. Current provider documents can change; the ledger's historical review date was not rewritten.

| Source | Material inspected | Scope and limit |
|---|---|---|
| SD01 | [Google Search stages](https://developers.google.com/search/docs/fundamentals/how-search-works), crawling, indexing and serving explanations | Distinct processes and explicit non-guarantees support the availability model. No live site was inspected. |
| SD02 | [AI features](https://developers.google.com/search/docs/appearance/ai-features), fan-out description; [AI optimization guide](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide), special-markup and rewriting discussion | Related searches can differ from literal input; no universal citation recipe follows. Google-specific statements do not settle another provider's requirements. |
| SD03 | [Discover](https://developers.google.com/search/docs/appearance/google-discover), interest/relevance and older-content passage | Supports age versus staleness and discovery without a current explicit query; does not guarantee appearance. |
| SD04 | [Canonicalization](https://developers.google.com/search/docs/crawling-indexing/canonicalization), preference and selected-representative discussion | Canonical declarations are signals, not commands. No universal object identity is implied by a URL. |
| SD05 | [Search Console metrics](https://support.google.com/webmasters/answer/7042828), selected AI Overview impression/click/position definitions | Links can share the containing result's position. This is a surface-defined measure, not attention or an independent universal rank. Other result types were not exhaustively checked. |
| SD06 | [Trends data](https://support.google.com/trends/answer/4365533), sampling, normalization and irregular-activity passages | Supports relative search-interest interpretation, not absolute customer demand. Separation from internal AI retrieval telemetry is a synthesis across different measurement definitions, not an empirical comparison performed by this FAQ. |
| SD07 | [OpenAI publisher FAQ](https://help.openai.com/en/articles/12627856-publishers-and-developers-faq), crawler controls and link/title fallback | Supports search/training purpose separation. The inspected fallback example explicitly concerns Atlas; do not turn it into a promise for every ChatGPT surface. No robots or access configuration was changed. |
| SD08 | [Perplexity crawlers](https://docs.perplexity.ai/docs/resources/perplexity-crawlers), user-triggered fetch role and access discussion | Search crawling and user-requested fetching have different roles. No provider-wide access guarantee or universal permission rule follows. |
| SD09 | [Bing index and grounding explanation](https://blogs.bing.com/search/May-2026/Evolving-role-of-the-index-From-ranking-pages-to-supporting-answers), responsibility, provenance, freshness, conflict and abstention discussion | Supports a distinction in system responsibilities. This engineering/product account does not prove that every generated answer meets those standards or document every implementation. |
| SD10 | [Bing AI Performance introduction](https://blogs.bing.com/webmaster/February-2026/Introducing-AI-Performance-in-Bing-Webmaster-Tools-Public-Preview), metric definitions and sampling qualifications | Citation metrics do not establish position or importance; exposed grounding phrases are sampled. No causal influence measure is established. |
| SD11 | [Rutgers record for ASK Part I](https://scholarship.libraries.rutgers.edu/esploro/outputs/journalArticle/ASK-FOR-INFORMATION-RETRIEVAL-PART-I/991031665289904646), bibliographic record and abstract | Supports knowledge-state and imperfect-expression framing. Full Part I/II methods were not inspected. |
| SD12 | [Bates author-hosted text](https://pages.gseis.ucla.edu/faculty/bates/berrypicking.html), evolving-search and berrypicking discussion | Theory and research synthesis support changing queries and accumulated information; not a required sequence for every search. Some web text has encoding artifacts; repository bytes were not altered to match them. |
| SD13 | [Joachims and colleagues, SIGIR 2005](https://www.cs.cornell.edu/People/tj/publications/joachims_etal_05a.pdf), title page, abstract, selected study setting and conclusion | Clicks contain information but are biased; relative preference interpretation differs from absolute relevance. Full estimation and gaze data were not reanalyzed. Proposed precise supporting reference under Q1. |
| SD14 | [Williams and colleagues, WWW 2016](https://www.microsoft.com/en-us/research/wp-content/uploads/2017/05/williams_www2016_good_abandonment.pdf), title page, abstract, introduction and selected dataset description | Mobile tasks and satisfaction reports support the possibility of successful non-click encounters. They do not establish satisfaction from non-clicks in arbitrary current AI systems. Full classifier validation was not repeated. Proposed precise supporting reference under Q1. |

## Q1 - Give the click-bias and good-abandonment records identifiable references

Location: SD13 and SD14 in the runtime evidence ledger. Level 1 provenance correction; no handbook semantic change is proposed.

SD13 describes unspecified Joachims eye-tracking/click work. Several related papers fit that description. SD14 names an institutional research topic without a year, author list, venue or locator. A source lookup therefore cannot reliably identify which methods and population the summary represents.

Constructed task: verify whether a click or a missing referral supports a relevance/satisfaction conclusion.

Current route: discovery.observation followed by source SD13 or SD14.

Decision risk: substitute a different study or overstate the empirical scope because the reference is ambiguous. The conceptual cautions themselves remain supported.

Smallest correction: retain the source IDs and claims, but name specific supporting works with authors, year, title, venue and direct locator:

- SD13: Joachims, Granka, Pan, Hembrooke and Gay (2005), *Accurately Interpreting Clickthrough Data as Implicit Feedback*, SIGIR, using the author-hosted paper linked above.
- SD14: Williams, Kiseleva, Crook, Zitouni, Hassan Awadallah and Khabsa (2016), *Detecting Good Abandonment in Mobile Search*, WWW, using the institutional paper linked above.

Identify these as supporting references selected during this audit to make previously broad records traceable. The available repository history inspected here does not establish that these exact versions were the original research inputs. Preserve that provenance uncertainty rather than inventing recovery history. Keep study-specific limitations beside each entry; do not add effect-size claims, a click correction formula or a satisfaction classifier to runtime.

## Other concerns not promoted

- **Grounding intent is not observed reliability.** Section 5 asks whether retrieved material is fit to support an assertion and separates retrieval, use, support and citation. It need not assume every engine actually performs all of those checks successfully.
- **Unknown internal stages need not block completion.** The core permits bounded conclusions, relevant retrieval and stopping when further investigation cannot change the decision. Section 7's diagnostic vocabulary should be applied to the unresolved boundary rather than requiring proof of every hidden internal stage. Representative operational cases should check this next.
- **A CTR expression is qualitative.** The listed contributing factors are not an estimated multiplicative model or a scoring formula; no coefficients or mechanical optimization rule follow.
- **More provider tactics are not automatically missing theory.** Current markup, access controls and product-specific reporting remain just-in-time dependencies. This pass does not add SEO/GEO tactics merely because a source mentions them.

## Verification and next step

All nine actual discovery routes extracted: core (105 lines), need (90), availability (145), selection (86), commitment (94), observation (152), decision-record (40), invariants (82), diagnosis (85). This verifies extraction availability, not behavioral efficacy. No package or behavior suite was rerun for a report-only addition.

Final checks cover local links, UTF-8 without BOM, CRLF, pre-existing file hashes, diff whitespace and worktree status. No live trials, old-pilot comparisons, commits or pushes were performed.

Clarify SD13-SD14 provenance next, then inspect representative Chapter 13 work chains. The current evidence does not justify redesigning the discovery core.

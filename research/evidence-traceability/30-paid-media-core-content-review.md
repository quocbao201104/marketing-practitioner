# Paid Media: Core Content Review

Date: 2026-09-07. Reviewed the current worktree; earlier corrections remain preserved.

Status: bounded conceptual and source-scope review completed. No substantive correction is proposed from this pass.

## Scope and assessment

Read all eight sections of [Chapter 14](../../skills/marketing-practitioner/handbook/14-paid-media-architecture.md), its fourteen-entry [evidence ledger](../../skills/marketing-practitioner/references/paid-media-evidence.md), and paid-media activation and observation handoffs in the [operating guide](../../skills/marketing-practitioner/references/operating-guide.md), with [SKILL.md](../../skills/marketing-practitioner/SKILL.md) as governing context.

The core is principally a model for identifying the right paid-delivery decision and interpreting system state. It does not claim to be a complete media optimizer or an independently validated theory of advertising effectiveness. Its evidence is predominantly provider documentation, engineering explanation and industry measurement/taxonomy guidance. Those sources are appropriate for the documented mechanics, but do not by themselves establish incremental business returns.

| Area | Assessment | Disposition |
|---|---|---|
| Section 1: activation and unit | Paid exposure is distinct from merely paying for production; a campaign need not be the resource or decision boundary. Simple supplied transformations remain direct. | Retain |
| Section 2: value and objective | Business value, platform objective and optimized signal differ. Reported conversions are not automatically bidding targets. | Retain |
| Section 3: controls and authority | Hard constraints, soft signals, obligations and precedence are distinct; advertiser inputs do not fully describe execution. | Retain |
| Section 4: allocation and exposure | Handles auction and reserved buying, pacing and history, authorized creative/destination selection, and delivery versus attention. | Retain |
| Section 5: observation and feedback | Reporting, billing, attribution, optimization eligibility and actual feedback have distinct roles; timing and maturity remain material. | Retain |
| Section 6: handoffs | Causal inference, customer-facing commercial design, product identity and landing-page architecture retain their existing owners. | Retain |
| Sections 7-8: records and invariants | Conditional aids; no compulsory campaign schema, universal cap, learning threshold or auction formula. | Retain |

## Selected source verification

The following access levels describe inspected material, not just located URLs. No live advertising account, billing record, delivery experiment or raw dataset was inspected. The ledger's historical overall review date was left unchanged.

| Source | Material inspected | Supported distinction and limit |
|---|---|---|
| PM01 | [Google conversion actions](https://support.google.com/google-ads/answer/11461796), primary/secondary definitions and custom-goal exception | Reported and bidding roles differ; the chapter already retains configuration exceptions. A primary label alone does not settle the campaign's actual optimization configuration. |
| PM02 | [Google data exclusions](https://support.google.com/google-ads/answer/10370710?hl=en), operation, click-period scope, reporting and delay passages | Exclusions affect Smart Bidding data while reporting remains. Applying the feature requires provider-specific time/scope checks; the chapter does not pretend to give the full configuration procedure or guarantee stabilization. |
| PM03 | [DV360 frequency caps](https://support.google.com/displayvideo/answer/2696786?hl=en), search-indexed official excerpts | Campaign caps can be best-effort for specified guaranteed inventory while lower-level caps have different treatment. Direct retrieval failed, including a 429 response; full page was not reviewed. Indexed passages support the chapter's bounded precedence example, not a universal exception. |
| PM04 | [DV360 guaranteed deals](https://support.google.com/displayvideo/answer/7067656?hl=en), negotiation, contracted quantity and configuration passages | Fixed volume/price can be reserved before creative is ready; negotiated, delivered and billed states can differ. No guarantee of exact human exposure or universal contract workflow follows. |
| PM05 | [TikTok upgraded Smart+ targeting](https://ads.tiktok.com/resources/help/article/about-targeting-for-your-upgraded-smart-experience?lang=en), control/suggestion table | Audience suggestions permit expansion; controls and custom targeting have different semantics. Custom targeting can itself include smart expansion options, so it is not a universal hard fence. The chapter does not make that stronger claim. |
| PM06 | [TikTok VTA](https://ads.tiktok.com/resources/help/article/about-view-through-attribution-vta?lang=en), definition and optimization note | Provider documentation says VTA can supply optimization signals. It does not establish incremental conversions or prove that every attribution setting affects every campaign identically. |
| PM07 | [TikTok learning phase](https://ads.tiktok.com/resources/help/article/learning-phase), fluctuation and edit discussion | Supports history-dependent adaptation. Current numerical heuristics were not promoted into shared rules. |
| PM08 | [LinkedIn cost cap](https://www.linkedin.com/help/lms/answer/a706289/cost-cap-bidding-strategy), average target, learning and charged-by table | Target cost is a benchmark, not each bid or a guaranteed realized average. Optimization goals can differ from billing events. |
| PM09 | [LinkedIn bidding strategies](https://www.linkedin.com/help/lms/answer/a421112), strategy descriptions and billing table | Automated, cost-cap and manual modes differ; budget, bid and chargeable event are distinct. The comparison is provider-specific, not proof of one universally best strategy. |
| PM10 | [LinkedIn auction](https://www.linkedin.com/help/lms/answer/a501530/linkedin-advertising-auction), bid and relevance explanation | Both participate in selection. The page does not reveal a universal clearing formula or guarantee delivery from a higher configured bid. |
| PM11 | [Meta Andromeda](https://engineering.fb.com/2024/12/02/production-engineering/meta-andromeda-advantage-automation-next-gen-personalized-ads-retrieval-engine/), opening retrieval/ranking and automation discussion | Supports the described multi-stage system and input/execution distinction. Performance claims and future engineering plans were not independently validated or turned into creative rules. |
| PM12 | [IAB creator taxonomy](https://www.iab.com/wp-content/uploads/2025/04/IAB_Creator_Economy_Definitions_Taxonomy_April-2025.pdf), paid amplification, sponsored content and authorization definitions | Supports separating related creator activities. It is terminology guidance, not a complete contract or permission model. |
| PM13 | [IAB programmatic terminology](https://www.iab.com/news/standardizing-programmatic-terminology-iab/), search-indexed official article text | Historical fixed/auction and reserved/non-reserved distinctions support non-auction buying. Direct follow-up retrieval failed; no current transaction taxonomy is certified. |
| PM14 | [IAB DOOH measurement guide](https://www.iab.com/wp-content/uploads/2025/07/IAB_DOOH_Measurement_Guide_July_2025.pdf), selected printed pages 9-10 and 13 | Distinguishes delivery, exposure opportunities, modeled/refined audience estimates and attention methods. The guide discusses evolving standards; this pass did not audit later MRC revisions or certify measurement vendors. |

## Suspected gaps checked without promoting new rules

- **Optimization target versus predictive input.** PM01 notes that some primary actions not used for optimization may still enhance predictions. The chapter distinguishes configured targets from observation and feedback roles; it does not assert that every non-target datum is ignored. Actual configuration remains necessary when that distinction changes the decision.
- **Exclusion timing versus reporting timing.** PM02 operates on the clicks to which affected conversions could be attributed. The chapter preserves event/interaction time, attribution window and delay and requires current provider evidence. A configuration task must retrieve those specifics; a generic observation boundary need not duplicate the procedure.
- **Constraint type versus precedence.** The guaranteed-inventory example is explicitly campaign-level and scoped. It does not authorize ignoring every frequency cap, contractual commitment or exclusion under automation.
- **Paid creator work can bundle several jobs.** Paying for production/publication does not automatically require allocation analysis, but a task that actually secures or amplifies mediated exposure can activate the paid path. The current activation test is about the unresolved delivery decision, not the creator label alone.
- **Learning is not a prohibition on intervention.** History can explain why current performance is unstable without proving the cause. The chapter does not require waiting through every learning period when a known defect, unsupported claim or material guardrail warrants action.
- **DOOH units are not interchangeable.** An ad play, rendered impression, exposure opportunity and estimated audience may use different units and methods. The current requirement to retain unit, modeling, identity basis and coverage handles this without inventing a universal multiplier.

## Depth and validation limits

This chapter provides useful control and measurement reasoning, but not a full method for estimating media response curves, selecting a portfolio, optimizing incremental marginal returns or designing every media-buy experiment. Those questions require focused research and Chapter 05's causal methods with actual objective, budget, response and constraint evidence. The absence of a universal allocation algorithm is consistent with the declared scope, not evidence that one should be invented here.

A static conceptual review cannot establish that agents use these distinctions reliably or that recommendations improve advertising outcomes. Current provider implementation, account state, market scope and source availability remain material limits.

## Verification and next step

All eight actual paid-media routes extracted: core (146 lines), objective (80), control (102), allocation (160), observation (136), handoffs (66), decision-record (52), invariants (66). Re-read the objective and observation excerpts against their cited qualifications and governing context. This verifies extraction availability, not behavior.

Only this report was added. Final checks cover local links, UTF-8 without BOM, CRLF, pre-existing file hashes, diff whitespace and worktree status. Package and behavior suites were not rerun for a report-only change. No live trials, old-pilot comparisons, commits or pushes were performed.

Next: inspect representative Chapter 14 operational chains, especially proxy objectives, control precedence, delayed feedback, shared allocation boundaries and causal spend decisions. No runtime correction is proposed before that review.

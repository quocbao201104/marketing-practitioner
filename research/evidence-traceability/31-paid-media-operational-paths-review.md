# Paid Media: Operational Paths Review

Date: 2026-09-07. Follows the [core content review](30-paid-media-core-content-review.md).

Status: eleven constructed work chains reviewed. No additional decision-changing design defect was identified. Only this report was added.

## Scope and method

Reviewed [Chapter 14](../../skills/marketing-practitioner/handbook/14-paid-media-architecture.md) with [SKILL.md](../../skills/marketing-practitioner/SKILL.md), the paid observation handoff in the [operating guide](../../skills/marketing-practitioner/references/operating-guide.md), and Chapter 05 sections 5-11. The latter already distinguishes average attributed, average incremental and marginal incremental returns, including material saturation, carryover, substitution, interference and uncertainty.

Extracted all eight actual routes: paid-media.core (146 lines), objective (80), control (102), allocation (160), observation (136), handoffs (66), decision-record (52), invariants (66). Re-read control and allocation excerpts with the core's dependency-first and continuity rules.

These are author-reviewed static chains, not executed agent tests, account audits or advertising experiments. Routes below identify conditional dependencies rather than compulsory reading sequences. Provider-source verification remains bounded by report 30; no new external empirical claim or current account state is asserted.

## Representative chains

| Constructed request | Guidance and retained state | Useful completion and assessment |
|---|---|---|
| 1. Shorten an approved ad headline using fixed facts and a supplied limit. | Core fast path. Preserve message, claim boundaries and output constraint. | Return the headline without launching a paid-performance audit or reopening the offer. Advertising vocabulary alone does not activate the specialist. |
| 2. Choose an optimization event when reported leads increase but supplied downstream qualification deteriorates. | paid-media.objective; observation if event role is unclear. Preserve business objective, signal definition, downstream evidence and campaign configuration. | Compare feasible signals against the actual objective; distinguish selecting a better-aligned proxy from proving incremental value. Do not optimize submission count merely because it is easy to report. |
| 3. Diagnose delivery outside a suggested audience despite a fixed target-customer strategy. | paid-media.control and current provider evidence when needed. Retain suggestion versus constraint, exclusions, actual delivery and scope. | Determine whether the field could expand before calling delivery a defect. Do not redefine the target market from reached-audience telemetry or assume all manual-looking controls are hard fences. |
| 4. A campaign cap conflicts with a guaranteed inventory commitment. | paid-media.control/allocation. Preserve cap level, inventory type, obligation, authoritative precedence and actual contract state. | Identify the applicable conflict and a feasible next decision. Do not generalize a campaign-level best-effort exception to all limits, or invent permission to alter a contract. |
| 5. A low-spending campaign shares a budget with other campaigns; the user proposes increasing its bid. | paid-media.allocation. Retain the operative resource boundary, competing allocations, pacing, eligible opportunity and constraints. | Locate the plausible bottleneck and next check before changing a lever. A campaign container need not define available resources; unavailable internal stages remain unknown rather than becoming fabricated explanations. |
| 6. A conversion-tracking outage is followed by data exclusions and apparent performance volatility. | paid-media.observation, Chapter 05 for cause. Preserve logged versus reported data, optimization eligibility, affected interaction period, conversion delay and control history. | Separate reporting recovery from feedback recovery. Obtain provider-specific exclusion timing when configuring a remedy; do not delete reported conversions conceptually or promise immediate stabilization. |
| 7. Attribution settings changed while creative stayed fixed; the dashboard now reports fewer conversions. | paid-media.observation and Chapter 05 as needed. Preserve attribution definition, signal availability, reporting window and possible feedback role. | Distinguish a measurement change from a delivery change or causal outcome decline. Do not assume attribution is always passive or that every reporting setting affects optimization. |
| 8. Recommend a budget shift using average ROAS from two campaigns with different maturity and capacity constraints. | paid-media.objective/allocation for resource and delivery state; Chapter 05 sections 10-11 for marginal causal return and uncertainty. | Provide a supported bounded recommendation, hold or information-gathering plan. Do not equate higher historical average ROAS with a higher return on the next dollar. Complete the decision support without inventing a response curve or refusing all action until certainty. |
| 9. Evaluate a paid-creator brief, then plan authorized amplification and destination copy as separately requested outputs. | Chapter 04/08 for message and publication; paid-media.control/allocation only for the actual amplification decision; Chapter 11 only if page allocation remains open. Preserve use rights, supported claims, approved assets, destinations and all deliverables. | Distinguish paid production from paid distribution and complete each authorized job. A platform's capacity to generate variants does not supply factual proof or broader creative authorization. |
| 10. Interpret DOOH plays, modeled reach and average frequency as evidence that specified people attended to an ad. | paid-media.allocation/observation. Preserve event unit, identity basis, exposure opportunity, methodology, modeling and coverage. | State what the measurements support and what they leave unknown. Do not treat plays as unique people or average frequency as every person's exposure history. Causal business effects remain a separate question. |
| 11. Resume a diagnosis and proposed budget/creative plan after new data show a reporting-window mismatch and withdrawal of permission for one asset. | Core continuity; observation for comparability and control/allocation for the affected authorization. Retain candidate versus adopted changes and pending outputs. | Revise dependent conclusions and remove the asset from the proposed authorized set while preserving unaffected work. Do not treat the old plan as executed or let a previously valid recommendation override changed evidence. |

## Cross-chain assessment

The core retains requested outputs and permits bounded decisions under uncertainty. Chapter 14 supplies the paid-specific control, allocation and observation distinctions; Chapter 05 supplies causal reasoning. This combination can identify a useful action or next check without requiring access to every hidden platform state.

The existing Chapter 05 marginal-return paragraph materially supports the budget handoff. The remaining depth limit concerns estimating response curves and optimizing constrained portfolios from valid evidence, not a complete absence of resource-allocation reasoning. These cases do not justify adding a generic optimizer, arbitrary budget percentages or universal bidding rules.

Known defects and authorization changes can warrant action even during learning. Conversely, volatility alone does not localize a creative problem. The inspected guidance retains both possibilities without a mandatory waiting period or a default rewrite.

## Verification and next step

All eight routes extracted successfully. This establishes retrieval availability, not reliable agent execution or advertising efficacy. Report-only checks cover local links, UTF-8 without BOM, CRLF, pre-existing file hashes, diff whitespace and worktree status. Package and behavior suites were not rerun for this addition.

No runtime correction is proposed for these eleven cases. No live trials, old-pilot comparisons, commits or pushes were performed. Next is Chapter 15, brand identity and visual systems, beginning with core content and evidence scope.

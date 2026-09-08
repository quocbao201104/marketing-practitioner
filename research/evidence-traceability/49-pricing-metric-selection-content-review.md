# Pricing-Metric Selection: Content and Behavioral Design Review

Date: 2026-09-08.

Reviewed revision: `008eb46`, pulled by fast-forward from `4865e80`. The incoming change contains six files: Chapter 10 payment guidance, its runtime evidence ledger, three research artifacts, and twelve bounded adversarial cases.

Status: bounded review completed. Two correction candidates: one medium semantic finding and one low provenance finding. Retain the bounded Chapter 10 extension; no demonstrated need for a controller, index, loader, or new-primitive change. No runtime repairs or live agent trials were performed.

## Scope and assessment

This pass inspects the incoming diff, the theory and repair record, both pricing evidence ledgers, the new cases, and the actual `commercial-design.payment` excerpt together with `SKILL.md`. It also retrieves `commercial-design.decision` and `commercial-design.governance` to check their constraints and uncertainty rules. Earlier audit verdicts and historical trials are not correctness evidence for this change.

The addition addresses a real, bounded reasoning need: selecting what makes payment vary, rather than treating a pricing metric as an already-given label. It usefully separates the charge basis, measurement specification, normalization, tariff, price level, and commitment. It permits flat fees and multiple bases, rejects an outcome-pricing maturity ladder, and keeps performance attribution and risk allocation visible. These distinctions belong with the existing payment owner.

The section retains a material activation condition: candidate generation applies when payment architecture itself is open. Its candidate taxonomy and feasibility questions are practical aids, and the ledgers explicitly distinguish project synthesis from source-supported propositions. The sources do not validate the complete combined selection procedure or guarantee agent compliance.

## PM-R1 — preserve authoritative constraints when they also enter the formula

**Priority: medium.** Location: [Chapter 10, Q/R/A/C definitions](../../skills/marketing-practitioner/handbook/10-commercial-design-pricing-and-terms.md), especially the definition of C at lines 233-235; [theory freeze](../commercial-design/03-pricing-metric-selection-theory-freeze.md), section 4; and the corresponding explanation in the [repair record](../commercial-design/05-pricing-metric-selection-post-review-repair.md).

The current definition excludes a variable from C when it enters the customer-facing pricing function. The theory is more explicit: that use becomes R rather than C. Making roles contract-relative fixes the earlier problem of treating every important economic estimate as authoritative, but it does not justify mutually exclusive authority and formula roles within one design.

Concrete static counterexample:

```text
TASK
Improve a usage tariff while preserving an approved maximum
customer bill of 1,000 per month. Removing that limit is outside scope.

CURRENT FORMULA
bill(q) = min(r * q, 1,000)

RETRIEVED RULE
C cannot itself enter the customer-facing pricing function.

CONFLICT
The 1,000 limit participates in the tariff formula and remains
an authoritative boundary for every candidate tariff.
```

**Decision consequence:** recording the limit only as a tariff input can drop its constraint status when the agent compares a different tariff. Conversely, preserving it only as C under the current definition obscures how it determines the actual bill. The same issue occurs when one customer class both gates access and sets a rate in the same contract. Distinguishing functions does not imply that one datum can have only one function.

This is a semantic conflict demonstrated by supplied hypothetical contract facts, not an observed model failure or a claim about any jurisdiction's law. The controller and governance guidance provide general protection, but the local exclusion still conflicts with that protection and should be corrected at its source.

**Smallest correction:** retain Q/R/A/C as distinct functions, allow concurrent roles in one design, and preserve the authority, scope, and source of a binding constraint even when its value also appears in the formula. Keep the existing warning that model estimates and economic importance do not create authority. Add a bounded case with an embedded authoritative cap and another with simultaneous eligibility/rate use. A new ontology or controller rule is unnecessary.

## PM-R2 — bind or relabel the current-practice example behind revisiting a basis

**Priority: low.** Location: [theory freeze](../commercial-design/03-pricing-metric-selection-theory-freeze.md), section 15, especially lines 693 and 713, and the section 19 authority-map entry for current pricing-design workflows and revisit behavior.

Section 15 presents current AI-service practice as a concrete example of a resolution metric losing coverage when a product adds valuable work that intentionally hands off. It labels the parent PROFESSIONAL PRACTICE, but the [PM evidence ledger](../commercial-design/04-pricing-metric-selection-evidence-ledger.md) does not identify a provider, dated document, or passage supporting this example. PM07 and PM08 concern credit accounting; they do not establish this specific product-scope or metric-transition example. No corresponding source binding was located in the commercial-design track or runtime ledger.

**Decision consequence:** a future maintainer can mistake an illustrative mechanism for a verified, current provider observation when explaining or extending the revisit rule. The mechanism is plausible, but plausibility does not establish its claimed provenance. This does not invalidate the general need to revisit a basis when its fit changes.

**Smallest correction:** recover the actual first-party source and bind the particular observation with its date and scope; otherwise describe the example as a hypothetical project illustration and qualify the authority-map entry. Do not substitute a vaguely related vendor article or invent the original research lineage. No additional runtime rule is required.

## Primary-source checks and access limits

Access below occurred on the review date. A successful search or bibliographic match is not a full-paper methods review. The following is a selected claim check of all eight newly installed CD sources plus research-only PM08, with differing access depth.

| Source mapping | Material recovered and assessment |
|---|---|
| PM01 / CD17 | [Publisher full-text HTML](https://journals.sagepub.com/doi/10.1177/1094670519895581), introduction, tariff discussion and Table 1. Supports separating measured from charged usage, material increments, multiple metrics, and flat-rate billing independent of usage. The telecommunications estimates are not universal effects. Its discussion favors value linkage; the broader project comparison procedure is not its tested result. |
| PM02 / CD18 | [Publisher abstract](https://pubsonline.informs.org/doi/abs/10.1287/isre.1120.0434). Confirms the service-versus-traffic pricing comparison and nontrivial profit, consumer and welfare consequences. The PDF endpoint redirected to the abstract, and an SSRN attempt failed. All model assumptions and comparative propositions were not revalidated; the broad no-universal-winner interpretation remains only partially verified in this pass. |
| PM03 / CD24 | [Author institution's paper](https://business.columbia.edu/sites/default/files-efs/pubfiles/4941/tariff_structure.pdf), selected passages on pp. 821-823 and 827. Confirms random assignment in the telecommunications trial and model-based separation of structure effects from price-level differences. It studies usage/retention conditional on assigned plans, not unrestricted customer selection between plans. The runtime avoids transferring its numerical effects. |
| PM04 / CD21 | [Institutional PDF indexed abstract](https://www.diva-portal.org/smash/get/diva2%3A1574695/FULLTEXT01.pdf). Confirms four experiments with experienced purchasers and conditional flat-rate preference, including the listed mechanisms. Direct full-text opens failed. Individual experiment designs, mechanism coefficients and significance were not independently checked. |
| PM05 / CD19 | [Publisher abstract and introductory passages](https://www.sciencedirect.com/science/article/abs/pii/S0019850116301080). Confirms theory elaboration from two cleaning-service contracts and material buyer responsibilities under outcome uncertainty. Supports attribution scrutiny, not a universal acceptable-attribution threshold or a ban on outcome contracts. Full case coding was not re-audited. |
| PM06 / CD23 | [Indexed publisher abstract](https://doi.org/10.1111/poms.12893). Confirms a cloud duopoly model with heterogeneous demand and usage volatility. The later direct DOI open failed. Model derivations were not rechecked; the runtime correctly retains its modeled-cloud scope. |
| PM07 / CD22 | [GitHub documentation, AI Credits definition](https://docs.github.com/en/copilot/concepts/billing/organizations-and-enterprises/usage-based-billing). Directly describes model-priced input/output/cached tokens converted into credits. This supports the economically weighted accounting example, not credit superiority or customer-value measurement. |
| PM08, research only | [Atlassian credit documentation](https://support.atlassian.com/rovo/docs/rovo-usage-limits/), credit consumption and billing notice. Confirms complexity-related credit accounting and announced extra-usage billing on December 3, 2026. The repair correctly distinguishes that announcement from an already-executed September billing state. |
| PM09 / CD20 | [Author-hosted published paper](https://hinterhuber.com/wp-content/uploads/2021/03/Value-quantification-capabilities-in-industrial-markets-AH-JBR_2017.pdf), p. 165. Directly distinguishes ex-ante value-based price setting from ex-post performance-linked adjustment and risk sharing. The precise runtime distinction is supported; this does not validate its complete outcome checklist. |

No retrieved primary passage demonstrated that the core distinctions are false. The access limitations above prevent certifying every ledger claim or describing this as a comprehensive pricing-literature review.

## Behavioral design and case coverage

The [twelve bounded cases](../../evals/pricing-metric-selection-bounded-cases.md) cover useful category errors, including multiple bases, billing increments, economic credits, outcome attribution, tariff/basis confounding, and unknown costs. They are prompts and expected properties, not executed agent results. The additional causal variant correctly avoids attributing a before/after usage change to either the unchanged basis or the changed tariff without identification.

Two coverage cautions should guide later static additions:

- PM-I04 tests different roles across two designs, but not concurrent roles within the same design; it therefore cannot expose PM-R1.
- The global candidate-generation fail condition should be explicitly limited to an open architecture/basis choice. Add a narrow task with an already-adopted basis and only a meter-definition or wording question remaining. Such a task should preserve that decision and finish the requested output without reopening fixed/variable/hybrid selection. The runtime already has this activation condition; the case contract should preserve it too.

The theory and case-flow diagrams place tariff resolution after architecture comparison. Read them with the runtime's explicit coupling rule: enough tariff detail must be considered whenever it can reverse a comparison. Their ordering is not evidence that architectures can be ranked independently of tariff design. This is a reading caution, not a separately established runtime defect.

The payment route is larger, but it returns the whole bounded procedure and its local qualifications. No missing selector, broken source lookup, or demonstrated need to split the route was found. Its size alone does not justify an index redesign.

## Disposition and verification

Prioritize PM-R1, then recover or relabel PM-R2. Retain the remaining contribution and its existing ownership. The earlier post-review repair record is historical provenance; this review does not retrospectively certify all its claimed closures.

Executed checks:

- package verification, including the installed Codex validator: PASS;
- route/source validation: PASS, 264 routes and 248 evidence sources;
- routing mechanics: PASS, 68 smoke checks;
- incoming Git whitespace check: PASS;
- actual payment, decision and governance retrieval inspected.

Only this review report is added locally. Its local links, UTF-8/CRLF text conventions, and whitespace were checked. No runtime file, research freeze, evidence ledger, or case oracle was changed. No full verification suite, live agent trial, commit, push, or release tag was performed in this review.

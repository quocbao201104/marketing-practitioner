# Commercial Design: Core Content Review

Date: 2026-09-07. Chapter 10 and its runtime evidence ledger were reviewed in the current worktree. Earlier corrections and audit artifacts remain separate, preserved work.

Status: bounded conceptual and source-scope review completed. One evidence qualification is proposed. No runtime change was made in this pass.

## Scope and assessment

Read all fourteen sections of [Chapter 10](../../skills/marketing-practitioner/handbook/10-commercial-design-pricing-and-terms.md), its [evidence ledger](../../skills/marketing-practitioner/references/commercial-design-evidence.md), and the commercial-design path and relevant handoffs in [operating guidance](../../skills/marketing-practitioner/references/operating-guide.md), with [SKILL.md](../../skills/marketing-practitioner/SKILL.md) as the governing context. Inspected actual indexed excerpts, including their local evidence qualifications and dependencies.

The historical theory-freeze adjudication was read for provenance, not accepted as proof that the current content is correct. Old behavioral pilots were not used. This pass does not certify all pricing research or establish that agents execute the guidance successfully.

The four dimensions remain a useful practitioner decomposition: configuration, payment, relationship/risk terms, and selection/allocation. They are explicitly coupled and identified as synthesis rather than a newly validated theory. No counterexample inspected requires a fifth dimension or a new controller job.

| Area | Assessment | Disposition |
|---|---|---|
| Sections 1-2: scope and synthesis | Open commercial choices are separated from representing settled terms; external authority and feasibility remain dependencies | Retain |
| Sections 3-4: configuration and payment | Preserves self-selection, cannibalization, tariff versus price, payer roles and multi-sided dependencies | Retain; not a complete method for choosing a pricing metric |
| Section 5: relationship/risk terms | Trial, free tier and discount are distinct; CD08's profitability wording omits its revenue-proxy condition | Clarify under T1 |
| Sections 6-7: allocation and representation | Eligibility differs from a discount modifier; price disclosure differs from the underlying terms; welfare is not relabeled fairness | Retain |
| Section 8: evidence | Methods are question-relative; hypothetical WTP, modeled trade-offs, observed response and causal elasticity are distinguished | Retain |
| Section 9: decision | Objective, horizon, feasibility, guardrails and uncertainty guide selection; no universal optimum is supplied | Retain |
| Sections 10-11: history and authority | Past commitments and cohort state can persist; churn risk differs from treatment response; recommendation differs from execution authority | Retain |
| Sections 12-14: composition | Existing owners supply product, finance, legal, messaging and causal dependencies; records and distinctions are conditional | Retain |

## Selected source verification

These access levels describe what was actually inspected, not merely which URLs were located. No raw-data reanalysis or full mathematical replication was performed.

| Source | Material inspected | Bound supported and remaining limit |
|---|---|---|
| CD03 Moorthy | [Publisher abstract](https://pubsonline.informs.org/doi/10.1287/mksc.3.4.288) | Formal self-selection/product-line reasoning supports coupled product and price choices. Full derivation not reviewed. |
| CD04 Armstrong | [Oxford-hosted manuscript](https://ora.ox.ac.uk/objects/uuid%3A82313b2b-ba9c-430e-a8f1-41d1e5e1cc5b/files/m8e2c312d489ada90942d69a1611b6eeb), search-indexed abstract/introduction only | Broad nonlinear-pricing scope is consistent with the ledger. Direct manuscript and publisher retrieval failed; full review remains unverified. |
| CD05 Schmidt and Bijmolt | [Open article](https://link.springer.com/article/10.1007/s11747-019-00666-6), abstract, definitions/classification, implications and limitations | Hypothetical-bias findings do not establish universal superiority of indirect methods. Advantages for other questions and unexamined newer methods limit a universal method ranking. No effect-size recomputation. |
| CD06 Tian and Feinberg | [Publisher abstract](https://pubsonline.informs.org/doi/10.1287/mksc.2020.1265) | Subscription entry and conditional plan choice are modeled jointly in a dating-service experiment. Its optimized menu is not a generally observed optimum. Full methods not reviewed. |
| CD07 Lewis, Singh and Fay | [Publisher abstract](https://pubsonline.informs.org/doi/10.1287/mksc.1050.0150) | The retailer example supports sales/profit divergence under shipping promotions. It is an empirical model, not a universal free-shipping rule; full identification and accounting not audited. |
| CD08 Yoganarasimhan, Barzegary and Pani | [Author-hosted published paper](https://faculty.washington.edu/hemay/Free_Trial.pdf), introductory setting and selected section 7 passages, especially printed p. 3235 | See T1. The full policy estimators and mechanism analysis were not audited. |
| CD09 Santana, Dallas and Morwitz | [Publisher abstract](https://pubsonline.informs.org/doi/10.1287/mksc.2019.1207) | Six-study disclosure/choice/satisfaction evidence supports the terms-versus-presentation distinction. Individual study methods not reviewed. |
| CD10 Blake and colleagues | [Author-hosted published paper](https://faculty.haas.berkeley.edu/stadelis/AIP.pdf), abstract and opening context | StubHub field experiment supports scoped price-salience effects. It does not make concealment an acceptable recommendation; full analysis not reviewed. |
| CD11 Anderson and Simester | [Publisher abstract](https://pubsonline.informs.org/doi/10.1287/mksc.1030.0040) | Direct-mail durable-goods experiments distinguish current/later effects and customer histories. No universal promotion policy follows. |
| CD12 Dube and Misra | [Publisher abstract](https://www.journals.uchicago.edu/doi/10.1086/720793) | Expected profit, aggregate consumer surplus and distributional outcomes can differ. This pass did not inspect the full measurement inventory or independently re-establish the historical fairness/trust correction. |
| CD13 Homburg and colleagues | [Publisher search-indexed abstract](https://journals.sagepub.com/doi/10.1509/jm.11.0251) | Pricing authority can span functions. Full methods and causal identification not verified. |
| CD15 Rochet and Tirole | [Publisher search-indexed abstract](https://academic.oup.com/jeea/article-abstract/1/4/990/2280902) | Platform participation on multiple sides matters in the formal model. Full assumptions and equilibrium derivation not reviewed. |
| CD16 Ascarza | [Author-hosted published paper](https://evaascarza.com/papers/ascarza_18.pdf), abstract, selected value-lift discussion and conclusion/limitations | Churn risk need not identify intervention response. Longer-run value requires additional outcome evidence or assumptions; two applications do not establish a universal targeting policy. |

CD01, CD02 and CD14 were read as local source records, not freshly verified externally. The ledger explicitly leaves B2B pricing metrics, outcome-linked contracts, guarantees, migration rules and other specialized policy questions incompletely covered. This review does not fill those gaps by inference from adjacent consumer studies.

## T1 - Keep the economic condition beside the trial evidence

Location: Chapter 10 section 5, commercial-design.terms, and the runtime CD08 source entry. This is a bounded evidence clarification, not a rejection of the study or the chapter's architecture.

The current sentence describes acquisition, retention and profitability effects. In section 7, printed p. 3235, CD08 measures two-year revenue and uses it as a profitability proxy because additional serving cost is near zero in its setting. The chapter's general context qualifier and ledger omit that specific condition.

Constructed input: evaluate a free trial for a service with material usage and support costs.

Current route: commercial-design.terms retrieves the unqualified economic label.

Decision risk: treat a revenue comparison as sufficient profit evidence. Core source fidelity and section 9 mitigate this, but do not recover an omitted measurement assumption from the citation itself.

Smallest correction: name acquisition, subscription duration and revenue; explain the study's near-zero-marginal-cost profitability approximation and retain the no-universal-duration boundary. Mirror this scope in CD08. Do not infer that all SaaS has negligible cost.

No new source, framework, route or pricing formula is needed. Proposed regression counterexamples are static: material serving costs prevent revenue from establishing profit; negligible incremental costs may support a scoped approximation without making revenue identical to total accounting profit. No agent failure was observed.

## Other suspected gaps not promoted

- **A pricing metric menu is not a metric-selection algorithm.** Section 4 explains the dimensions but does not fully teach per-seat versus usage versus outcome selection. The ledger explicitly marks the specialized evidence limit. The core's objective/constraint comparison can use supplied facts; inventing a universal score or value-metric rule would overstate this pass's evidence. This remains a candidate for focused research, not a demonstrated theoretical error.
- **Menu choice must include nonpurchase and substitution.** Sections 2-3 already couple configuration and price through self-selection/cannibalization; section 5 includes opt-in versus conditional plan choice. No universal tier count or independent optimization of each tier is prescribed.
- **Reported WTP is not an exact market demand curve.** Section 8 already preserves hypothetical context, model dependence and causal boundaries. The inspected meta-analysis does not justify a universal numerical correction or dismissing conjoint for all questions.
- **Retention response is not automatically profit response.** Section 10 uses CD16 only to distinguish prediction from intervention response. Section 9 retains the commercial objective and economic inputs. Adding a full CLV estimator would duplicate or expand the existing method scope.
- **A commercial recommendation need not wait for perfect parameters.** Section 9 supports robust or provisional choices and a revisit condition. Missing material authority or cost facts remain explicit dependencies under the core; no new approval ritual is required.

## Retrieval assessment

All fourteen commercial-design routes resolved through the existing loader. Read these focused slices with the core: payment (59 lines), terms (33), evidence (62), decision (69) and dynamics (39). Their conditions and handoffs match the chapter. Remaining sections were read in chapter context, and their selectors resolved successfully; this is not a claim that each was independently behavior-tested.

T1 is present in the correctly retrieved terms excerpt. It is not a selector failure. A future correction should preserve all headings and route IDs, inspect the terms excerpt and the CD08 source lookup, and leave sufficient core/index guidance unchanged.

## Outcome and limits

Only this report is added. No runtime or source-ledger edits, agent trials, old-pilot comparisons, commits or pushes were performed. Report links, text integrity and preservation of pre-existing files are checked separately; package test results are not claimed for a report-only review.

Recommended next action: apply T1 locally, then inspect representative commercial-design work chains. Treat deeper pricing-metric and contract research as bounded later work requiring its own question and sources, not as proof that the present four-part decomposition must expand.

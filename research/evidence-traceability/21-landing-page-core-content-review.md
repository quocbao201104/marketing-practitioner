# Landing-Page Architecture: Core Content Review

Date: 2026-09-07. Reviewed the current worktree; earlier corrections and research artifacts remain separate, preserved work.

Status: bounded conceptual and source-scope review completed. Two evidence corrections are proposed. No runtime correction was made in this pass.

## Scope and assessment

Read all eleven sections of [Chapter 11](../../skills/marketing-practitioner/handbook/11-landing-page-architecture.md), the eight entries in its [runtime evidence ledger](../../skills/marketing-practitioner/references/landing-page-evidence.md), and the landing-page activation boundary in the [operating guide](../../skills/marketing-practitioner/references/operating-guide.md), with [SKILL.md](../../skills/marketing-practitioner/SKILL.md) as governing context. Extracted all eleven actual landing-page routes; inspected the sequence, action/form and diagnosis excerpts explicitly against the chapter and source records.

The historical landing-page evidence ledger and freeze adjudication were inspected for provenance, not accepted as independent validation. Old behavioral pilots were not used. This pass evaluates conceptual coherence and selected source support; it does not demonstrate agent execution or conversion performance.

| Area | Assessment | Disposition |
|---|---|---|
| Sections 1-2: ownership, entry and readiness | Settled message/commercial inputs constrain page allocation; action availability differs from readiness. Information distance remains a qualitative prompt. | Retain |
| Section 3: sequence and section formation | Dependencies and visitor questions justify allocation; the illustrated sequence and hero elements are explicitly optional. | Retain practitioner status |
| Section 4: proof and risk | Placement follows the supported claim or decision. Testimonials, FAQ and literal adjacency are not universal requirements. Upstream proof adequacy remains with Chapter 04. | Retain |
| Section 5: visuals and exploration | Representation is chosen for its information job; screenshots do not automatically prove outcomes. Navigation and motion require a reason. | Retain; not a complete accessibility or production specification |
| Section 6: actions and forms | Explains action consequences, present information needs and downstream qualification; field count does not define value. | Retain; case-method limits below |
| Sections 7-8: responsive and comparison | Preserves meaningful sequence and material information, while allowing different components and discoverable detail. | Retain |
| Section 9: interpretation | Observations do not establish causes, but the final citation group includes a proposed redesign among case-study lifts. | Correct under A1 |
| Sections 10-11: record and invariants | Conditional working aids, not required output fields or a validated scoring model. | Retain |

## Selected source verification

Access below means the passages actually inspected. Public summaries are not substitutes for raw data, complete study protocols, independently replicated effects or full accessibility conformance review.

| Source | Material inspected | Supported scope and limit |
|---|---|---|
| LP01 | [W3C Meaningful Sequence](https://www.w3.org/WAI/WCAG22/Understanding/meaningful-sequence), success criterion, intent and examples | Programmatically determinable order when meaning depends on sequence; multiple orders may be valid. This Understanding document explains the criterion and is informative. It neither fixes page section order nor establishes conversion effects. |
| LP02 | [NN/g F-shaped reading](https://www.nngroup.com/articles/f-shaped-pattern-reading-web-content/), research examples, alternative patterns and formatting discussion | Observed scanning varies with task, content and presentation; F-shaped scanning is not a layout prescription. The public article was reviewed, not the full paid report or gaze data. |
| LP03 | [Unbounce information hierarchy](https://unbounce.com/landing-pages/information-hierachy-helps-you-convert-and-delight/), question-order framing and explanatory discussion | Primary evidence of the practitioner's proposed approach, not a controlled validation of the approach. The chapter appropriately does not inherit the article's stronger promotional assurances. |
| LP04 | [Eye-path vs. Thought sequence](https://marketingexperiments.com/conversion-marketing/lpo-eyepath-thought-conversion), article body and author's clarification; opening linked analyses | A critique proposes moving content and forms. No outcome for that proposed rearrangement is reported in the inspected article. See A1. |
| LP05 | [CXL form-field article](https://cxl.com/blog/reduce-form-fields/), attributed practitioner account and case discussion | Confirms what CXL reports, including a practitioner's account of a field-removal treatment. Original assignment, denominators, uncertainty and raw results were not verified. Its explanation of why the result occurred remains an interpretation. Do not present this secondary case account as an independently verified experiment. |
| LP06 | [Baymard plan-matrix scannability](https://baymard.com/blog/saas-scannability-plan-matrix), findings, participant examples and grouping/order guidance | First-party usability observations support comparison discoverability in the studied SaaS setting. Public guidance does not establish isolated causal lifts for each design element. |
| LP07 | [SaaS UX fixes](https://baymard.com/blog/saas-website-ux-best-practices), UI previews, matrix truncation and grouped disclosure; [benchmark](https://baymard.com/blog/saas-benchmark), method summary and feature-discovery discussion | Benchmark scoring of sites differs from participant testing. Both publications can draw on shared research, so two URLs do not establish independent replication. Missing a full-list link and opening a clearly labeled feature group are different discovery problems. |
| LP08 | [Offer-page optimization](https://marketingexperiments.com/value-proposition/optimizing-landing-pages-increase-148), setting, treatments and results; [value inhibitors](https://marketingexperiments.com/value-proposition/overcoming-value-inhibitors), framing and reported tests; [form clinic](https://marketingexperiments.com/value-proposition/optimizing-forms-increase-perceived-value), article text | Mixed corpus of reported tests and practitioner diagnosis. Bundled treatments do not isolate psychological mechanisms. The clinic video was not viewed. One results table is internally inconsistent; see A2. |

## A1 - Separate a proposed redesign from an observed test result

Location: runtime LP04 entry and Chapter 11 section 9, landing-page.diagnosis. Level 1 evidence clarification.

The LP04 entry describes counterevidence and test lineage; section 9 groups it with case-study lifts. The source supports a design hypothesis, not a measured outcome for that proposal.

Constructed task: justify a form-placement recommendation using observed evidence.

Current route: landing-page.diagnosis followed by source LP04.

Decision risk: label a plausible redesign as an empirically successful treatment. The no-universal-law caveat does not repair its evidence class.

Smallest correction: describe LP04 as practitioner analysis and proposed testing; remove it from the lift citation group. Preserve its appropriately qualified use in section 3. No new source, route or controller rule is needed.

Static counterexample: a reasoned placement proposal can support a provisional choice without establishing a measured lift. This is a source-representation defect, not an observed agent failure.

## A2 - Quarantine the contradictory result inside LP08

Location: runtime LP08 evidence entry. Level 1 source-quality qualification.

The offer-page article's Case Study 1 table gives control 0.16%, treatment 0.13%, and a positive 89.23% relative difference. Its prose says the treatment won. Those values cannot support that conclusion as presented. A separate direct HTML table extraction confirmed the numbers occur in the source markup, rather than only in the web text extraction.

Constructed task: retrieve LP08 to justify a positive effect from simplifying a registration path.

Decision risk: accept a scoped result whose direction and reported magnitude disagree. Limiting transport to the original population does not resolve an internally contradictory result.

Smallest correction: mark this specific case's direction and magnitude unresolved pending corrected primary results; retain it only as a description of a proposed/tested treatment. Do not guess a typo, repair the numbers, or invalidate every case in the corpus. The chapter currently reproduces no numerical lift, so no additional chapter change is needed for A2.

Static counterexample: a positive narrative cannot override a contrary table merely because the source calls the study an experiment.

## Other concerns not promoted into corrections

- **Information dependencies are not an observed reading path.** Sections 3 and 5 already allow alternative order and scanning; core uncertainty rules prevent assumed visitor state becoming fact. A dependency illustration is useful planning synthesis, not a claim that every visitor reads top to bottom.
- **Compact comparison is not permission to conceal capability.** Sections 7-8 preserve discoverability and decision-critical differences. Baymard's truncation examples caution against a misleadingly complete-looking subset; they do not require every page to list every feature or prohibit all grouped disclosure.
- **Case accounts are weaker than audited experiments.** LP05 is already classified as practitioner synthesis with case evidence. This pass does not verify its effect or mechanism, but that access limit alone does not demonstrate a new routing defect or justify replacing the chapter's downstream-value reasoning.
- **Visual production remains incomplete by design.** The motion guidance and responsive sequence rule are not a full treatment of accessible media, keyboard operation, interaction states or loading performance. Those require task-specific implementation evidence when material. No comprehensive conformance or performance claim is made here.

## Verification and next step

All eleven landing-page routes extracted successfully. This establishes retrieval availability, not behavioral efficacy. No package or behavior suite was rerun for a report-only addition. Final verification checks report links, UTF-8 without BOM, CRLF, unchanged pre-existing runtime/research file hashes, worktree status and diff whitespace.

Apply A1-A2 as bounded evidence corrections next, then inspect representative Chapter 11 work chains. Do not expand the controller, create a universal page template, or start live trials to resolve these source-classification issues.

# Email Communication Architecture: Core Content Review

Date: 2026-09-07. Reviewed the current worktree; earlier changes remain preserved.

Status: bounded conceptual and source-scope review completed. One substantive source-summary correction is proposed. No runtime edit was made.

## Scope and assessment

Read all nine sections and the evidence boundary of [Chapter 12](../../skills/marketing-practitioner/handbook/12-email-communication-architecture.md), its eight-entry [evidence ledger](../../skills/marketing-practitioner/references/email-communication-evidence.md), and the email routes and handoffs in the [operating guide](../../skills/marketing-practitioner/references/operating-guide.md), with [SKILL.md](../../skills/marketing-practitioner/SKILL.md) as governing context. Inspected the historical theory-freeze conclusion for provenance only.

The model's central distinctions remain coherent: communication need, authority and feasibility differ; sequences are repeated state-dependent decisions; permission to send does not establish standing to demand; observation labels do not establish human attention or causality. No additional controller job, global eligibility flag or lifecycle model is justified by this review.

| Area | Assessment | Disposition |
|---|---|---|
| Sections 1-2: scope and send decision | One-shot messages need not become sequences; unresolved jobs and history can justify send, wait or exit. Narrow supplied-copy tasks retain a fast path. | Retain |
| Section 3: authority and scoped state | Separates relevance, permission and technical feasibility; endpoint/list state is not a universal person-level boolean. Current requirements remain external dependencies. | Retain |
| Section 4: timing and branching | Waiting needs a reason; tracked opens and absent actions do not establish intent. Trigger selection differs from causal effect. | Retain |
| Section 5: allocation | Inbox expectations, body fulfillment and optional actions are coherent, but the personalization paragraph misstates the treatments in EM08. | Correct under E1 |
| Section 6: continuity | Carries material meaning and consequences across subject, body and destination; fragile visual carriers do not define the whole message. | Retain |
| Section 7: observation | Acceptance, placement, exposure, attention, action and effect remain distinct; future reachability can matter to the objective. | Retain |
| Sections 8-9: records and invariants | Optional, decision-linked working aids with explicit unknowns; no fixed cadence, subject formula or CTA count. | Retain |

## Selected source verification

The following records what was actually read. Provider/regulatory sources were checked for the distinctions the chapter uses, not to determine permission for a real mailing or audit every applicable requirement. Current pages do not establish all historical source versions.

| Source | Material inspected | Supported scope and limit |
|---|---|---|
| EM01 | [Gmail sender guidelines](https://support.google.com/mail/answer/81126?hl=en), personal-account scope, sender requirements, authentication and subscription guidance | Supports provider-dependent feasibility and delivery constraints. The chapter does not freeze numerical thresholds or promise inbox placement. No DNS or live sending configuration was tested. |
| EM02 | [Subscription guidance](https://support.google.com/mail/answer/15263077?hl=en), definitions and list identification; [sender FAQ](https://support.google.com/mail/answer/14229414?hl=en), classification and unsubscribe scope | Supports distinguishing list-specific unsubscribe mechanics from a global person state. Provider mechanics do not establish permission for another list or override a broader opt-out. Classification is context-dependent. |
| EM03 | [Apple Mail privacy settings](https://support.apple.com/guide/mail/change-privacy-settings-mlhlae4a4fe6/mac), option descriptions; [iPhone privacy guidance](https://support.apple.com/guide/iphone/use-mail-privacy-protection-iphf084865c7/26/ios/26), operative passage | The Mac guidance explicitly describes background remote-content retrieval when the protection setting is enabled. The iPhone guidance describes obscuring open activity. These support measurement uncertainty, not a claim that every tracked open is false. |
| EM04 | [RFC 5321](https://datatracker.ietf.org/doc/html/rfc5321), selected positive-completion and responsibility passages, especially section 6.1 | Acceptance entails delivery/relay responsibility, not verified inbox placement or human viewing. The full protocol and later extensions were not audited. |
| EM05 | [FTC CAN-SPAM questions](https://www.ftc.gov/business-guidance/blog/2015/08/candid-answers-can-spam-questions), official answers on consent and other obligations | Supports the bounded counterexample to universal prior opt-in. Reader comments were not treated as authority. This historical guidance is not blanket send authorization or a full current legal analysis. |
| EM06 | [ICO guidance overview](https://ico.org.uk/for-organisations/direct-marketing-and-privacy-and-electronic-communications/guidance-on-direct-marketing-using-electronic-mail/) and [operative subscriber/soft-opt-in guidance](https://ico.org.uk/for-organisations/direct-marketing-and-privacy-and-electronic-communications/guidance-on-direct-marketing-using-electronic-mail/how-do-we-comply-with-the-pecr-electronic-mail-marketing-rules/) | Supports subscriber-, purpose- and condition-dependent authority. The current overview includes an update concerning charitable soft opt-in. No new legal rule is promoted into runtime; case-specific applicability remains an authoritative dependency. |
| EM07 | [Publisher abstract](https://pubsonline.informs.org/doi/10.1287/mksc.2017.1066) | Describes randomized field experiments with several companies and scoped positive outcomes. Full estimators, raw data and proposed processing mechanisms were not audited. Publication year is not necessarily collection year. |
| EM08 | [Open article](https://link.springer.com/article/10.1007/s11002-023-09701-7), abstract, sections 3-4 and conclusion | Treatment and outcome distinctions establish E1 below. Separate table-page retrieval failed; no raw-data reanalysis was performed. |

## E1 - Preserve which personalization treatment was actually tested

Location: Chapter 12 section 5, email.allocation, and EM08. Level 1 evidence correction.

Current wording presents two newer experiments as first-name non-replications. Experiment 1 used first names with university students and did not establish a positive open/click effect. Experiment 2 used title plus surname with politicians: the reported open increase was significant, while the click increase was not. Both used German messages. Neither experiment directly compares first names with surnames in the same population.

Constructed task: choose subject-line personalization from the cited evidence.

Current route: email.allocation supplies the incorrect two-experiment summary; source EM08 repeats it.

Decision consequence: overstate replicated negative evidence and erase a different treatment's result.

Smallest correction: distinguish both experiments and outcomes in the paragraph and ledger. Retain conditional treatment status; do not infer universal surname superiority, zero first-name effect, or established habituation over time. No new source or controller rule is needed.

Static counterexample: a title/surname experiment cannot count as another first-name test. No agent failure was observed.

## Other concerns not promoted

- **Scoped unsubscribe is not permission laundering.** Section 3 already requires applicable authority and suppression scope. Technical list separation cannot justify bypassing an opt-out that governs a broader relation. No new global suppression primitive is necessary.
- **Missing action does not mandate another message.** Sections 2 and 4 preserve exposure uncertainty, remaining job and waiting/exit options. The allocation section also retains history when sending remains justified, so it does not discard relationship burden at the send decision.
- **Click and open telemetry differ from intent.** Section 7 already preserves instrumentation and automation uncertainty. Adding a provider-specific bot taxonomy would not resolve a demonstrated gap here.
- **A model can be coherent without a universal cadence optimizer.** The chapter gives reasons for timing and stopping, not a validated rule for exact intervals. A requested schedule still needs task evidence or provisional choices; no new interval formula is warranted.
- **Provider feasibility is not guaranteed delivery.** Current Gmail guidance distinguishes requirements, recommendations and enforcement consequences. The chapter's conditional wording does not turn every missing requirement into an automatic rejection rule.

## Verification and next step

All nine actual email routes extracted successfully: core (44 lines), send-decision (69), send-state (70), sequence (76), allocation (85), continuity (58), observation (69), decision-record (28), and invariants (68). Re-read the allocation excerpt and located both EM08 misstatements. An initial guessed ledger filename failed; the discovered canonical filename was then read. This was a reviewer lookup error, not a repository routing defect.

Only this report was added. Final checks cover local links, UTF-8 without BOM, CRLF, pre-existing file hashes, diff whitespace and worktree status. Package and behavior suites were not rerun for this report-only addition. No live experiments, old-pilot comparisons, commits or pushes were performed.

Correct E1 next, then inspect representative Chapter 12 work chains. The correction changes evidence interpretation, not the send/wait/exit model.

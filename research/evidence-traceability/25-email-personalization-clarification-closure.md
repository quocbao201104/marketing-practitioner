# Email Personalization: Clarification Closure

Date: 2026-09-07. Implements E1 from the [email core review](24-email-core-content-review.md), following user authorization.

## Bounded correction

Three targeted replacements affect [Chapter 12 section 5](../../skills/marketing-practitioner/handbook/12-email-communication-architecture.md) and [source EM08](../../skills/marketing-practitioner/references/email-communication-evidence.md).

The chapter and ledger now distinguish the first-name experiment with university students from the title-plus-surname experiment with politicians. They preserve the reported distinction between open and click results, the German-language setting, and the absence of a direct comparison of name forms in the same population. The chapter also identifies 2018 as publication timing for EM07.

The correction does not turn a nonsignificant result into zero effect, establish surname superiority, or present habituation as the demonstrated cause of cross-study differences. Personalization remains a conditional treatment. Source access and methodological limits remain recorded in review 24; no new external evidence was added.

## Static counterexamples

| Constructed interpretation | Corrected boundary |
|---|---|
| Count two first-name non-replications | The second experiment used a different treatment. |
| Recommend surnames as the experimentally proven replacement for first names | The experiments used different populations and did not directly compare these forms. |
| Treat the second experiment as establishing both open and click improvements | The reported significance differs by outcome. |
| Conclude that first-name personalization has no effect or stopped working because of habituation | Neither claim follows from the cited comparisons. |

These are author-reviewed static interpretations, not agent executions or replications of the research.

## Verification

- Repository package validator and current Codex skill validator: PASS.
- Manifest validation: PASS, 264 routes and 239 evidence sources.
- Routing mechanics: PASS, 68 smoke checks.
- Actual email.allocation and EM08 lookups retain the corrected treatment, population and outcome distinctions. Re-read the allocation excerpt in chapter context.
- Compared all 264 route outputs with their pre-edit contents: only email.allocation changed.
- Compared all 85 pre-existing runtime/research files with their pre-edit hashes: only the two intended runtime files changed.
- Inverting the three replacements restores the original bytes. UTF-8 without BOM, Unicode, CRLF and final-newline state are preserved.

Final report-link, encoding, whitespace and worktree checks accompany this closure. Earlier changes and audit reports are preserved. No live trials, commits or pushes were performed.

## Next step

Inspect representative Chapter 12 work chains, including send/wait/exit, history-sensitive wording, body-complete messages, destination continuity and observation-to-diagnosis handoffs. This correction does not require a controller or sequence-model redesign.

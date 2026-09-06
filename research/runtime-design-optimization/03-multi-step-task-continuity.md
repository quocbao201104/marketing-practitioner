# Multi-step task continuity design

Date: 2026-09-07

Status: implemented and statically reviewed; behavioral evaluation deferred.

## Scope and evidence status

This is a bounded Level 2 clarification of the existing runtime controller. The user authorized the first proposed priority: preserving the requested marketing work across reads, dependencies, revisions, and continuation. Index design, extraction granularity, specialist theory, and live behavioral evaluation remain outside this change.

The findings below are underspecified transitions in the written contract, illustrated by constructed counterexamples. They are not observed model failures. Historical pilots are neither a diagnosis nor an acceptance baseline. No claim is made about measured reliability, optimal instruction length, or performance across model sizes.

## Existing coverage and remaining ambiguity

The core already preserves resolved state, separates proposals from evidence, names outstanding deliverables, routes by dependencies, returns from upstream work, and permits bounded completion. The operating guide already specifies domain handoffs. Repeating those principles or adding a generic agent-memory subsystem would not address the remaining ambiguity.

The missing detail concerns what happens after a read or revision: retaining the result for the pending artifact, recognizing an unproductive read, revisiting outputs that depended on changed information, and recovering current task state from available records.

## Design counterexamples before implementation

Each chain follows CONTRIBUTING.md's task -> current representation -> failure -> decision impact -> smallest correction requirement. The failure is a possible interpretation of the current text, not an executed trace.

### C1. A successful read leaves the artifact pending

INPUT / TASK: Write an email using supplied positioning; check whether a product claim is supported.
CURRENT REPRESENTATION OR ROUTE: Controller steps 5-7 route to proof guidance and tell the agent to resolve and pass forward useful state.
FAILURE: The section is read, but its implication for the claim is not retained; the next activity follows another handbook reference instead of returning to the email.
WHY THE FAILURE CHANGES THE DECISION: The requested communication remains incomplete or reuses the unsupported claim.
SMALLEST CORRECTION: Require the relevant conclusion or remaining uncertainty from a read to inform the pending job; continue at the resolved dependency's return point.

### C2. Guidance is mistaken for missing product evidence

INPUT / TASK: Determine whether a campaign can claim a customer outcome whose supporting data is unavailable.
CURRENT REPRESENTATION OR ROUTE: Source fidelity forbids fabrication; the read/expand instruction does not distinguish a completed guidance read from unresolved case evidence at that transition.
FAILURE: Repeatedly consult general proof guidance as though another section could establish the product-specific outcome.
WHY THE FAILURE CHANGES THE DECISION: The agent neither produces bounded copy nor identifies the evidence dependency.
SMALLEST CORRECTION: If a read does not resolve the question, identify the remaining gap and use the existing retrieve/clarify/bound policy. A repeat read needs a changed question, missing context, new evidence, or read failure to address. This also allows a productive negative finding to narrow the answer.

### C3. Evidence changes after several artifacts were drafted

INPUT / TASK: Draft an email and landing page; later evidence shows the claimed benefit applies only to one product tier.
CURRENT REPRESENTATION OR ROUTE: Resolved-state freezing permits reopening a contradicted input, but propagation to already drafted outputs is unspecified.
FAILURE: Correct the latest email but retain an unsupported claim in the landing page, or rebuild all strategy even though the audience and price remain valid.
WHY THE FAILURE CHANGES THE DECISION: Related outputs contradict each other or valid choices are unnecessarily replaced.
SMALLEST CORRECTION: Trace the changed input to dependent conclusions and artifacts, revise those, and preserve unaffected work.

### C4. The user changes only one requested deliverable

INPUT / TASK: Request an email and page, then change only the email's tone.
CURRENT REPRESENTATION OR ROUTE: The initial job identification preserves multiple outputs; it does not specify how later scope changes update their status.
FAILURE: Treat the latest message as replacing the page request, or treat all previous constraints as immutable.
WHY THE FAILURE CHANGES THE DECISION: A requested output disappears, or the correction is ignored.
SMALLEST CORRECTION: Apply the new instruction to its affected scope. Remove cancelled or replaced outcomes from active scope; preserve paused work and its status for later resumption without requiring its current execution or completion.

### C5. A provisional choice loses its status in continuation

INPUT / TASK: Explore two audiences, then resume drafting with a summary that names one audience but omits whether it was selected.
CURRENT REPRESENTATION OR ROUTE: Candidate/adopted distinctions exist, but no compact continuation guidance identifies which task state must survive.
FAILURE: Treat the summarized candidate as adopted or supported by market evidence.
WHY THE FAILURE CHANGES THE DECISION: Copy is finalized for an unselected audience, or unsupported empirical certainty appears.
SMALLEST CORRECTION: Keep decision status separate from evidence status in a compact working record when continuation needs one. Recover material missing status from available context or source artifacts; use the existing uncertainty policy if recovery is insufficient.

### C6. One blocked output hides an independent output

INPUT / TASK: Explain the available customer evidence and recommend a campaign claim; claim-specific evidence remains missing.
CURRENT REPRESENTATION OR ROUTE: The core already permits independent work and bounded results, but final completion is phrased primarily at the artifact/job level.
FAILURE: Declare the whole task done after the explanation without addressing the claim, or withhold the explanation because the claim is blocked.
WHY THE FAILURE CHANGES THE DECISION: The user cannot distinguish completed work from the unresolved requested decision.
SMALLEST CORRECTION: Account for every still-requested output at completion; provide supported work and identify any remaining material dependency.

## Chosen implementation

1. Refine controller steps 6-8: use the result of a read, apply uncertainty handling when it remains insufficient, return to the pending job, and account for all requested outcomes.
2. Add a compact conditional continuity subsection in the core: update affected scope and dependents; retain useful state in an existing working record when a long, interrupted, or interdependent task needs it; reconcile that record when resuming.
3. Point the guide's existing state-handoff introduction to the core's continuity rule. Domain-specific handoff fields remain unchanged.
4. Keep source review and constructed cases here, outside installed runtime. Add no mandatory memory file, lifecycle schema, tool-call ritual, additional reading hop, or general agent framework.

Alternatives rejected: a fixed state machine would overconstrain exploratory research and provisional drafting; a mandatory record after every call would burden narrow work; putting all continuity rules in the optional guide would leave the core's read/return transition underspecified; changing the index would not define what happens after retrieval.

## Conceptual source review

Reviewed on 2026-09-07.

- [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629), Yao et al., ICLR 2023. Abstract reviewed only. It describes interleaving reasoning and task actions to update plans and handle exceptions using environmental information. This motivates inspecting the read/update/act boundary; its benchmark results do not validate this skill, the proposed wording, or a mandatory reasoning-trace format.
- [Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents), Anthropic Applied AI, 2025-09-29. Engineering guidance, especially context retrieval and long-horizon tasks. It discusses selective retrieval, compaction, structured notes, and the risk of dropping critical context. It supports considering compact continuation records as a design option; it does not establish that every marketing task needs persistent notes or that this implementation prevents drift.

The specific transition rules are project synthesis from the existing contract and the counterexamples above. Source fidelity, scoped revision, and preserving requested deliverables justify their semantics; empirical effectiveness remains unmeasured.

## Static acceptance boundaries

- A sufficient narrow caption still executes directly, with no record or reference read.
- Research can refine its question during a bounded inspection; absence of the anticipated finding can be informative.
- A failed or incomplete read may be retried using the existing retrieval fallback.
- A completed read that cannot supply missing case evidence leads to evidence retrieval, clarification, or a bounded result.
- A provisional audience can be selected under delegated authority without another approval; selection does not validate a market claim.
- A changed claim revises dependent drafts; unchanged price, audience, and other artifacts remain intact.
- A tone correction affects the requested artifact; explicit cancellation or replacement removes the affected old request. Pausing a page while continuing an email preserves the page's status for later resumption and does not block current email completion.
- Resume uses available records without inventing missing history or rebuilding completed unaffected work.
- Multiple requested outputs remain accounted for even when one cannot be completed with available evidence.
- Records contain task facts, decisions, references, and outstanding work, not a transcript of internal reasoning; no persistence tool or memory guarantee is assumed.

## Validation plan and outcome

- [x] Review the actual diff against C1-C6 and the static acceptance boundaries.
- [x] Obtain an independent read-only review of the instructions and their composition.
- [x] Run both package validators and the existing routing-mechanics/source-resolution checks.
- [x] Check local Markdown links, UTF-8/BOM/CRLF preservation, Unicode integrity, and Git diff hygiene.
- [x] Confirm final scope with Git status; leave live behavioral effectiveness explicitly unvalidated.

## Review and verification outcome

- Independent static review identified one P2 ambiguity: the initial wording grouped paused outcomes with replaced/cancelled outcomes and could discard resumable work. The correction explicitly preserves paused work and status, excludes it from active execution/completion, and limits final accounting to active requests. A targeted independent recheck confirmed resolution with no further findings.
- The final instructions were reviewed against C1-C6 and the listed acceptance boundaries. These are static design checks, not task executions or demonstrated behavior.
- Both package validators passed. The existing 68 routing-mechanics smoke checks and validation of all 261 knowledge routes / 233 evidence sources passed after the final runtime edit.
- All 18 local Markdown links and anchors in the changed runtime files and design record resolved. UTF-8 without BOM, CRLF line endings, original non-ASCII characters, and each existing file's terminal-newline state were preserved.
- An initial ad hoc integrity check incorrectly required a terminal newline in SKILL.md. Byte comparison showed the original file also had none. The check was corrected to verify preservation, and passed; the source file was not normalized.
- Git diff hygiene passed. The worktree was initially clean; task scope is two modified runtime Markdown files and this new design record. Index, scripts, handbook, and historical evaluations are unchanged. No commit or push was performed in this change.
- No live model evaluation was run. Package and routing checks establish structural integrity only. Whether these instructions improve multi-step completion, reduce drift, or work reliably across model sizes remains unmeasured.

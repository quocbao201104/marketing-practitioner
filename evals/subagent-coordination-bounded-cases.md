# Conditional Subagent Coordination: Bounded Cases

Status: static design cases and expected properties. No agent runs or benchmark results are recorded here.

Target: [SKILL.md](../skills/marketing-practitioner/SKILL.md), `Coordinating subagents when useful`, read with its controller, continuity, source-fidelity and uncertainty rules. These cases exercise optional coordination inside marketing work; they do not require a particular host tool, model, agent count, or visible workflow template.

## SC01: independent work with a shared final decision

Task: assess two proposed B2B charging architectures using supplied product facts, then recommend one. Primary-source checks and a review of the candidate formulas can proceed independently. Permitted subagents are available and the task budget supports the work.

Expected: bounded assignments can inspect source scope and formula consistency while the lead evaluates objectives and trade-offs. Each receives the relevant product facts, adopted choices, limits and requested evidence. The lead checks the returned claims, reconciles the results and makes the requested recommendation. Delegation is justified by useful decomposition, not a mandatory pricing workflow.

Failure: subagents independently invent costs or positioning, or the lead returns two disconnected reports without addressing the decision.

## SC02: many outputs with an unresolved shared dependency

Task: choose positioning and produce a landing-page hero, launch email and three ads. Two competing customer segments remain under review.

Expected: retain all deliverables, but resolve the material target/positioning dependency before treating downstream copy as final. Independent evidence checks or explicitly provisional drafts may proceed if useful. Carry the adopted choice and proof limits into dependent assignments.

Failure: parallel copy tasks silently pick different audiences, or agreement between drafts is treated as validation of the positioning.

## SC03: narrow task and unavailable delegation

Task A: shorten an approved email subject line with sufficient context. Subagents are available.

Task B: review a pricing proposal with sufficient supplied evidence. Subagents are unavailable or prohibited by the host.

Expected: complete A directly when coordination adds no useful value. Complete B locally within available capabilities; state an actual evidence limit only if it affects the answer. Do not install orchestration tools or ask for extra authority merely to satisfy the skill.

Failure: mandatory agent spawning based on task labels, or refusing useful work because subagents are unavailable.

## SC04: incomplete context and partial assignment authority

Task: have a specialist inspect claims in an existing landing-page draft. The audience and positioning are adopted; efficacy claims remain hypotheses. The assignment allows review, not file edits or publication. The host does not automatically share prior conversation.

Expected: provide the relevant draft, adopted state, hypothesis status, applicable skill guidance and review boundary. Request traceable findings and limits. Preserve those limits when integrating the review.

Failure: the specialist treats hypotheses as facts, replaces positioning, edits outside its assignment or interprets review authority as permission to publish.

## SC05: agreement without independent evidence

Task: two returned reviews recommend outcome pricing. Both ultimately cite the same vendor article. A third review identifies unresolved buyer contribution and attribution.

Expected: trace the underlying source, preserve its vendor scope, and investigate the decision-changing attribution issue. The two matching answers do not count as independent confirmation. If unresolved, use a bounded recommendation or identify the separating evidence.

Failure: select by majority vote, convert vendor guidance into proof of effectiveness, or demand unanimous agreement before any useful result.

## SC06: shared edits and scope change

Task: two assignments concern a landing page and email stored in one campaign file. Midway, the user changes the price and cancels the email. An earlier result arrives with the old price and completed email text.

Expected: establish non-overlapping edit ownership or return proposed changes for integration. Update or stop affected work where possible. Reject stale price assumptions, remove the cancelled deliverable from active scope, and finish the remaining page using current facts. Preserve unrelated user edits.

Failure: conflicting whole-file rewrites, accepting a late result solely because it completed successfully, or resurrecting the cancelled output.

## SC07: failure, budget and further delegation

Task: a bounded source check fails after using its assigned budget; another independent assignment has returned useful evidence. Further delegation would exceed the task limit.

Expected: retain the useful result after checking it. Do not restart or recursively expand work without justification within the permitted budget. Resolve the remaining necessary check locally where feasible; otherwise preserve its evidence limit and complete the supported output. Wait for a pending result only when it remains material to completion.

Failure: unlimited retries or agent trees, inventing a missing result, or withholding completed independent work indefinitely.

## SC08: returned artifact versus completion claim

Task: a delegated copy edit reports success, but its artifact omits the required CTA and changes an approved product claim.

Expected: inspect the relevant artifact against the requested function and claim boundary, correct or reject the affected edit, and validate the integrated output. A subagent's success label cannot settle completion.

Failure: forward the result unchanged or treat the existence of an artifact as proof that the user request is fulfilled.

## Interpretation

These are design-level counterexamples and acceptance criteria. They assess whether the instructions can represent the necessary behavior; they do not demonstrate that any model follows it reliably or that delegation outperforms local execution. Future execution should report actual host capabilities, scope, costs and observed outputs separately.

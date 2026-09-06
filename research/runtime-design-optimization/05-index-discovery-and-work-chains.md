# Index discovery across representative work chains

Status: three bounded index additions implemented and statically verified, including independent review. Behavioral evaluation is deferred.

## Scope and review method

Part 3 focuses on index discovery, examined within representative chains from the user's request to a useful output. The index remains an address table, not a workflow engine. Part 1 supplies task continuity; part 2 supplies criteria for interpreting retrieved sections. This review asks whether those mechanisms can reach the right existing guidance at the point where it can change the work.

The unit of review is the request, resolved state, remaining question, discoverable route, actual excerpt with SKILL.md, retained conclusion or constraint, and output obligation. Routes listed below are conditional design paths, not required runtime sequences or expected tool-call traces. Independent deliverables do not acquire dependencies merely because they appear in the same request.

The eight cases are constructed from the current design and handbook. They are not historical pilot cases, observed agent failures, executed marketing tasks, or behavioral measurements. Output descriptions are acceptance conditions, not generated results. An executable selector check establishes retrieval mechanics only.

Review criteria:

- Can the open question select an appropriate existing owner and route without treating a topic word as activation?
- Does an indexed address reach the needed guidance, rather than merely a related heading or a narrower child that omits the question?
- Does the returned section retain the scope and qualifications needed with the loaded core?
- Can the result return to the pending job with its decision-relevant constraints and uncertainty?
- Does the output obligation preserve all requested work, including a justified bounded result, while avoiding unnecessary reads or redesign?

## Design findings and smallest corrections

The initial manifest has 261 routes and 233 evidence sources. All eight handbook namespaces and their top-level headings were inventoried to identify potential address gaps. Semantic review is limited to the cases below, not certification of all routes or platform content.

Three existing sections have useful bounded jobs but no indexed address to the section or an enclosing section. General file search can recover them; the gap is in the declared index interface, not total unavailability of the knowledge. The other reviewed chains have sufficient existing routes or direct paths.

### G1: Cross-platform adaptation has no direct address

INPUT / TASK: Adapt a resolved explanatory post into a short sequential video while preserving its supported message and deciding which execution choices should change.
CURRENT REPRESENTATION OR ROUTE: The content namespace offers meaning-representation, fast-path, and consequential-strategy. Chapter 08 section 16 states the relevant preserve/adapt boundary, but none of these selectors includes it.
GAP: A namespace lookup cannot select that focused guidance; neighboring routes cover broader or different questions.
DECISION IMPACT: The available route choices do not directly expose which environment-specific execution may change while strategic meaning stays fixed. Recovery requires locating an unindexed section or assembling the distinction from broader material.
SMALLEST CORRECTION: Add content.platform-adaptation for the existing section 16 and a conditional discovery cue in the operating guide. Keep narrow supplied transformations on the direct fast path.

### G2: Fact provenance does not cover information-class distinctions

INPUT / TASK: Prepare a shopper card and detailed explanation from a mixed dossier containing product specifications, seller-scoped warranty terms, a current promotion, buyer feedback, and a platform-inferred attribute.
CURRENT REPRESENTATION OR ROUTE: commerce.fact-provenance reaches only Chapter 09 section 5.5. commerce.commercial-state covers availability conditions. Neither reaches section 5's distinction among product-descriptive data, commercial conditions, and observation-derived context.
GAP: An origin question is addressable, but the broader classification question is not represented by an enclosing section route.
DECISION IMPACT: Source provenance alone does not determine whether a warranty is intrinsic or seller-scoped, or whether buyer feedback describes intrinsic product truth. Those distinctions constrain both representations.
SMALLEST CORRECTION: Add commerce.data-classes for existing section 5. Preserve commerce.fact-provenance as the smaller choice when only origin/support remains unresolved; do not require reading both.

### G3: Discovery diagnosis and handoff guidance is skipped by the index

INPUT / TASK: Explain why an observed web rank does not establish AI citation and identify the next useful check before deciding whether page rewriting is warranted.
CURRENT REPRESENTATION OR ROUTE: discovery.observation reaches Chapter 13 section 6; discovery.decision-record reaches section 8. Section 7's diagnosis and owner handoffs have no indexed address.
GAP: Telemetry interpretation is reachable, but the focused guidance for localizing the unresolved discovery boundary and choosing the next owner is not.
DECISION IMPACT: Interpreting a citation count alone does not determine whether availability, selection, grounding fitness, or downstream message/page work remains unresolved.
SMALLEST CORRECTION: Add discovery.diagnosis for existing section 7 and a conditional discovery cue in the operating guide. Preserve Chapter 05 ownership of causal claims; do not require every diagnostic step when supplied evidence already resolves it.

## Representative request-to-output chains

### W1: Sufficient supplied copy transformation

Request/state: Shorten a supplied caption to the requested length; its message, facts, voice, destination constraints, and intended action are resolved.
Open question: Ordinary wording execution only.
Path: SKILL.md fast path -> direct rewrite, with no index or operating-guide read.
Carry forward: Supported meaning and fixed wording where explicitly fixed.
Output condition: The shortened caption performs its original job within the requested bound; no added strategy memo or compulsory specialist read.
Finding: Existing design is sufficient. A platform name alone does not activate G1.

### W2: Adapt a resolved post to sequential video

Request/state: The message, audience, supported demonstration, and claim limits are fixed. The user requests a short TikTok video script adapted from a supplied post; environment-specific execution remains open.
Open question: Which execution choices may change without replacing the message? If temporal development remains unresolved, how should the video deliver its promised explanation?
Path: content.platform-adaptation -> tiktok.sequential-representation only for the remaining sequential-representation question -> requested script.
Carry forward: Strategic meaning, supported demonstration, material context, destination constraints, and any limits on the claim. Platform or community rules require current verification only when material and not already sufficiently supplied.
Output condition: A coherent script realizes the supported explanation in time; it does not claim watch-time gains or turn the example planning map into a mandatory template.
Finding: G1 closes the focused address gap. The platform route can be entered directly when sequencing is the only missing knowledge.

### W3: Mixed commerce dossier to two representations

Request/state: The supplied dossier identifies product/variant, source scope, applicable seller terms, promotion dates, and which attribute is platform-inferred. The user requests a selection card and a detailed product explanation.
Open question: Which information describes the thing, which describes the exchange, and which is observation-derived? Which distinctions must survive selection versus evaluation?
Path: commerce.data-classes -> commerce.shopper-representation-jobs only if that allocation question remains open -> both requested representations.
Carry forward: Relevant variant and source support, seller/time scope of terms, and feedback or inference status. A positive review or inferred attribute does not silently become a verified specification. Exact field mechanics, if material and missing, belong to the platform namespace and authoritative evidence.
Output condition: The card supports recognition/selection and the detailed explanation supports evaluation; both preserve material terms and truthful claims. Neither guarantees ranking or discovery.
Finding: G2 closes the classification gap. When only a claim's provenance is open, commerce.fact-provenance remains sufficient without the parent read.

### W4: Discovery symptom to bounded next action

Request/state: Supplied records show a web ranking observation and no citation in a separately scoped AI-answer observation. The user wants interpretation and the next useful check, not an asserted cause or immediate rewrite.
Open question: What does each observation establish, and which discovery boundary is still unresolved?
Path: discovery.observation when event meaning/coverage needs guidance -> discovery.diagnosis when localization or owner selection remains unresolved -> bounded interpretation and next check. Either route can be the direct entry when the other question is already resolved.
Carry forward: System/surface, object, observation scope, coverage, and the difference between absent telemetry and demonstrated non-retrieval. Do not assume web rank proves AI availability, grounding fitness, or citation.
Output condition: State the supported distinction and a discriminating next check. Return to rewriting only if evidence localizes a message problem; a causal request uses Chapter 05 before causal recommendations.
Finding: G3 exposes the existing handoff guidance. No claim is made about current provider implementation beyond the supplied scoped records.

### W5: Fixed commercial state to page and email

Request/state: The user supplies adopted plans, prices, material terms, comparison audience, contact permission/suppression state, timing constraints, and exit events. They request page comparison content and an email sequence proposal.
Open question: How should fixed plan differences support a page choice, and what state change justifies each next email or wait?
Path: landing-page.commercial-comparison for an unresolved comparison question; email.sequence for an unresolved timing/branch/exit question -> both deliverables. These reads serve separate pending outputs, not a forced serial pipeline.
Carry forward: The same adopted commercial state into both artifacts; valid exit/suppression conditions and justified temporal dependencies into the sequence. Only an unresolved transition policy activates commercial-design.dynamics.
Output condition: Clear choice-relevant comparison plus a sequence whose messages have a supported job and stopping condition. Do not redesign prices or invent a universal cadence.
Finding: Existing selectors and caller boundaries are sufficient; no index change.

### W6: Attributed return to causal decision support

Request/state: A dashboard reports higher attributed return after a spend change. The user asks whether the spend caused incremental growth and what evidence would justify another increase.
Open question: What comparison supports the causal inference, and what were the paid reporting/attribution/maturity semantics?
Path: Chapter 05 for the causal question -> paid-media.observation only for unresolved paid measurement semantics -> bounded conclusion and useful evidence request or next check.
Carry forward: Treatment/comparison limits, attribution rule, exposure and outcome maturity, authoritative constraints, and uncertainty about incremental and marginal return.
Output condition: Distinguish attributed improvement from supported causal leverage; do not produce a fabricated causal estimate or an automatically approved spend increase. An unavailable causal comparison can yield a useful bounded answer.
Finding: Existing direct chapter access and indexed paid specialization are sufficient; no index change or new causal owner.

### W7: Selected identity to a scoped refinement result

Request/state: A selected mark has an identified counterspace problem in a supplied small display context. The user wants that issue corrected and a brief account of the change; the identity family is fixed.
Open question: Which form decision can address the identified problem without replacing the selected identity?
Path: brand-identity.refinement -> ordinary artifact execution and inspection in the required context -> revised artifact and concise change note. Deeper evaluation guidance is conditional on a still-open evaluation question.
Carry forward: Selected identity, unaffected geometry/relationships, and the actual deployment requirement. Optional controlled mutation is project synthesis, not a universal design method.
Output condition: An inspectable correction in the specified context, without reopening concept exploration or claiming measured recognition gains. Mechanical export alone requires no identity route.
Finding: Existing route is sufficient; no index change.

### W8: Exploratory source material to understanding

Request/state: The user provides interview transcripts and asks what makes migration difficult in those accounts, without requesting a segment decision or campaign.
Open question: What do the accounts support, where do they differ, and what remains uncertain?
Path: Direct Chapter 01 guidance when synthesis/inference needs it -> scoped account of the supplied material. No indexed domain is a mandatory prerequisite.
Carry forward: Root-source identity, evidence class, situation, contradictions, and distinctions between participant account, interpretation, and hypothesis.
Output condition: A traceable answer to the learning question with material differences and limits. Do not turn sample recurrence into population prevalence or append an unrequested commercial choice.
Finding: Existing foundational routing is sufficient; no new research namespace.

## Implementation boundary and rejected alternatives

Add only three stable logical IDs to existing namespace section maps; update the operating guide's conditional selection examples and README's current inventory count. Keep existing selectors, namespace structure, extraction semantics, CLI, evidence ledgers, handbook prose, and SKILL.md unchanged in this part.

The indexed sections already contain the needed guidance. Rewriting theory, adding generated summaries, keyword scoring, embeddings, mandatory dependency traversal, or another runtime navigation file is not justified by these gaps. Do not index every unindexed heading for symmetry. Short IDs and exact selectors remain the existing discovery surface; this review does not establish a need for a new listing format.

A fallback reader can resolve each added ID through its exact heading and stop at the next equal-or-higher heading. This is the existing allowed fallback, not permission to bypass a denied capability. Runtime host behavior under denied or interrupted tools is not measured here.

## Verification record

Completed checks:

- Read the three actual new helper excerpts with SKILL.md: content.platform-adaptation (24 lines), commerce.data-classes (117 lines), discovery.diagnosis (85 lines). Their exact headings and excerpt boundaries match the intended existing sections.
- Compared all 261 pre-existing route bindings and extracted results against the pre-part-3 manifest using the current unchanged target files: all unchanged. Removing the three new map entries reproduces the old manifest object exactly. None of the old selectors includes the new target heading in its returned section.
- Inspected the secondary routes and foundational guidance used in W1-W8. This is static assessment of conditional paths and output obligations, not execution of those eight tasks.
- Ran scripts/verify.ps1 -PackageOnly: repository package validator PASS; current Codex validator PASS.
- Ran scripts/test-knowledge-routing.py: 68 routing-mechanics smoke checks PASS.
- Ran scripts/get-knowledge.py --validate: 264 routes / 233 evidence sources PASS. Updated README's two current inventory counts accordingly.
- Verified UTF-8 without BOM, original CRLF and terminal-newline state, preserved non-ASCII content, and no newly introduced trailing whitespace. Preserved README's pre-existing Markdown hard-break whitespace.
- Compared against a pre-part-3 byte snapshot: all prior part 1/2 files are unchanged except the three isolated operating-guide insertions; removing those insertions reproduces that guide snapshot exactly.
- Inspected the scoped diff and ran git diff --check successfully. No helper, handbook, evidence, or SKILL.md change belongs to this part.

Independent read-only review found no Critical or Important issue. It identified one Minor issue in W2: the request named only a generic video while the path selected TikTok guidance. The case now explicitly requests TikTok, so the platform-specific route is justified by the supplied destination. This is a case clarification, not a new runtime activation rule.

The full repository harness and live behavioral evaluation were not run for this index-only change. Static address reachability and internal consistency do not establish route-selection accuracy, lower agent error, output quality in use, or comprehensive semantic coverage.

No behavioral trial, efficacy claim, commit, or push is part of this work.

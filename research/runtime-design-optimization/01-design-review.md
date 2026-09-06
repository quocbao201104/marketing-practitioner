# Runtime design optimization: theoretical and semantic review

Date: 2026-09-07

Status: design review and implementation rationale. Behavioral effectiveness is untested.

## Mandate and scope

The user requested theory- and content-first optimization of the current skill. Historical behavioral pilots, route labels, pass counts, and compact-controller results are not evidence for choosing these edits. No live agent evaluation, new behavioral corpus, model comparison, or performance claim belongs to this stage.

The review covers the complete controller, the foundational research/decision/communication chapters, and their composition with the specialist routes. Specialist coverage is preserved; this is not a claim to have revalidated every empirical statement or provider rule in the entire resource tree.

The objective is an internally coherent contract that tells a capable agent what work to complete, which inputs remain settled, which uncertainties matter, and how to use the existing knowledge. Word count and conformance to a prescribed reading sequence are not quality measures.

## Basis and evidence boundaries

- Chapter 00 already separates empirical, explanatory, and decision questions, treats frameworks as heuristics, and makes evidence thresholds depend on consequences and reversibility. Chapter 05 applies the same principle to intervention choices. These existing premises support the operational clarifications below.
- [GDS: Plan user research for your service](https://www.gov.uk/service-manual/user-research/plan-user-research-for-your-service), reviewed 2026-09-07, allows broad and evolving discovery questions, turns unfounded assumptions into questions, and selects research activities by the learning need and resource cost. This supports bounded exploration, not directionless collection or a universal marketing workflow.
- [GDS: User research in discovery](https://www.gov.uk/service-manual/user-research/user-research-in-discovery), reviewed 2026-09-07, describes learning about users, their current experience, needs, and barriers before service scope is fully resolved. It supports understanding as a legitimate research outcome. Its service-development guidance is not an empirical claim about agent effectiveness.
- [Zhang and Choi: Clarify When Necessary](https://aclanthology.org/2025.findings-naacl.306/), NAACL 2025, abstract reviewed 2026-09-07; existing ledger entry TS08. The paper considers interpretation ambiguity and users' speed/carefulness preferences in QA, MT, and NLI. It motivates conditional clarification, not a validated clarification algorithm for marketing agents. No implementation or full-paper replication claim is made.
- The skill-authoring guidance favors scoped instructions, proportional specificity, and progressive disclosure. These are design recommendations, not proof that fewer instructions will improve this skill.

The new controller wording is **project synthesis** from these premises and the user's intended scope. It does not establish a model-independent optimum or guarantee better execution.

## Findings and bounded corrections

The following are static counterexamples to ambiguities in the written contract. They are not observed model failures or scored test cases.

### D1. Supplied state is not necessarily settled state

INPUT: "We suspect agencies are our best customers. Review these interviews and advise who to prioritize."

CURRENT CUE: controller step 2 groups "already-supplied" and "already-resolved" audience/positioning/facts under freezing.

CONFLICT: the user supplied a hypothesis for examination, not a binding target choice. Freezing it would erase the requested decision; treating a supplied assertion as verified would also conflict with source fidelity and the Task Specification Guide.

CORRECTION: distinguish adopted task constraints, claims/observations, and proposals under review. Freeze the first within scope; retain the evidential status of the others. Separate fixed wording from fixed meaning.

BOUNDARY: a request to write within an approved target does not authorize a new targeting exercise. Unsupported claims are narrowed or flagged without reopening unrelated strategy.

### D2. Research can identify the question itself

INPUT: "Explore these interviews to understand how customers coordinate this work. We have not chosen a segment or intervention."

CURRENT CUE: Chapter 01 begins from a decision requirement; controller step 4 disallows evidence that cannot change an already named decision.

CONFLICT: an exploratory question can reveal relevant dimensions and future choices before a commercial decision is specified. The existing RESEARCH / UNDERSTAND job should not require an invented business choice.

CORRECTION: permit a bounded learning question or problem-framing objective. Judge relevance by what could change understanding, interpretation, or the next decision; update the question when source material warrants it.

BOUNDARY: explicit scope and a useful stopping condition still apply. Discovery does not authorize endless collection, prevalence claims, or searching only for confirmation.

### D3. Dependency is not a one-way production sequence

INPUT: "Explore two positioning directions using provisional hero drafts; neither is approved."

CURRENT CUE: Chapter 00 presents an analytical sequence and an unqualified positioning-before-expression commitment; Chapter 03 says copy begins only after its listed choices are sufficiently resolved.

CONFLICT: drafts may be artifacts for examining strategic alternatives. The controller already says its dependency patterns are not mandatory pipelines, but downstream prose can reinstate a linear gate.

CORRECTION: distinguish final communication under sufficiently resolved strategy from provisional expression used to inspect an open choice. Preserve factual constraints throughout; keep candidate status through handoffs.

BOUNDARY: a polished draft is not customer evidence, an approved strategy, or proof of effectiveness. Candidate work must not reopen a strategy the user actually fixed.

### D4. Relevance and clarification need usable decision criteria

INPUT: a request lacks a nonessential stylistic preference; another lacks which of two products a performance claim describes.

CURRENT CUE: repeated "material" and "sufficient" conditions without a shared operational interpretation.

CONFLICT: both are unknowns but have different consequences. Treating both as blockers or silently filling both violates proportionality or source fidelity.

CORRECTION: a difference is material if it can change the requested choice, claim, interpretation, required artifact function, or allowed action. Use supplied context first; resolve relevant external facts within the task; ask about consequential user-owned ambiguity only when a useful bounded answer cannot avoid it. Continue independent work where possible.

BOUNDARY: permission, product facts, evidence, and commitments are not ordinary stylistic assumptions. Neither always-ask nor always-assume follows from this design.

### D5. Decision sufficiency and proof strength are distinct

INPUT: "Given limited evidence, recommend a reversible next step and explain what would change your recommendation."

CURRENT CUE: strong uncertainty preservation plus instructions to diagnose before changing tactics; the action-threshold explanation remains in deeper chapters.

CONFLICT: the evidence needed to claim an effect is established differs from the justification for a bounded action under uncertainty. Uncertainty may warrant a qualified recommendation, not just a caveat or further research.

CORRECTION: expose the existing consequence/reversibility principle in the controller; compare feasible options using stated objectives and constraints, and explain decisive trade-offs and revisit conditions when they affect the choice.

BOUNDARY: do not turn plausibility into a causal claim or require experiments for every decision. Investigation is warranted when it can discriminate consequential alternatives at reasonable cost; waiting also has consequences.

### D6. Minimum sufficient output needs a positive completion standard

INPUT: one task requests a caption; another requests a recommendation and reasons; another asks for an explanation of an unfamiliar product.

CURRENT CUE: extensive omission rules and specialist boundaries, with positive artifact requirements concentrated late in the controller and in the copy path.

CONFLICT: avoiding irrelevant content alone does not define completion. Conversely, turning every internal reasoning element into a visible template would violate the same minimum-sufficiency principle.

CORRECTION: give the seven existing jobs concise completion criteria, make requested compound deliverables explicit, and retain the audience-facing completeness and capability checks. Criteria are functions, not mandatory headings or schemas.

BOUNDARY: a simple transformation remains simple; explaining a product still requires enough concrete capability information. No universal CTA, number of options, or diagnostic report template is introduced.

### D7. Retrieval mechanics obscure the decision loop

INPUT: any ordinary skill invocation must first parse the controller.

CURRENT CUE: step 6 contains both the next-decision rule and a long fallback procedure for heading/marker slicing and source lookup.

CONFLICT: core decision selection and conditional execution mechanics have different scope. They can be separated without changing any logical route or creating another required loading hop.

CORRECTION: retain a short step 6 and put the existing retrieval procedure in a named subsection of the same file. Preserve helper preference, direct-index fallback, semantic boundaries, recovery, and smallest-file degradation.

BOUNDARY: this is an organization change; no reduction in tool calls, context use, or failure rate is asserted.

### D8. Evidence fit cannot be replaced by a universal source-type ranking

INPUT: a customer buys the only available package; separately, interviews explore how customers describe an unmet need.

CURRENT CUE: Chapter 01 says behavioral material generally outranks hypothetical preference and groups reported situations with behavior.

CONFLICT: a constrained observed choice does not identify unconstrained preference; a recalled account is not direct observation. Conversely, stated material can answer questions about reported meaning without establishing future behavior. A universal ranking conflicts with Chapter 00's question-specific, multidimensional evidence model and Chapter 01's own source/inference separation.

CORRECTION: prefer relevant behavior over unsupported predictions for actual-behavior questions, while evaluating both observed and stated material by question, method, available alternatives, constraints, and scope. Preserve the boundary between reports, observations, preference, and realized choice.

BOUNDARY: this conceptual clarification does not make stated intent proof of demand, make all sources equally strong, or claim that one method is universally superior. No new empirical effect or model-performance claim is introduced.

## Implementation design

- `SKILL.md`: revise the eight-step controller; add bounded work/uncertainty and job-completion guidance; separate retrieval mechanics; preserve all specialist namespaces, logical IDs, handoffs, and ethical/evidential constraints. Keep the seven jobs and current activation metadata.
- Chapter 00: make the learning cycle explicitly non-mandatory; explain exploratory question formation and distinguish thresholds for action from strength of empirical claims; scope the strategy-before-expression commitment.
- Chapter 01: admit bounded exploratory learning within the existing research owner, using the existing R21 evidence record; replace the universal source-type ranking with question/method/scope fit.
- Chapter 03: allow candidate positioning and provisional expression; keep final strategic commitments distinct from options.
- Chapter 04: preserve candidate status during drafting and add bounded guidance for substantively different message alternatives when exploration is requested.
- Bibliography R21: add direct source links and the bounded discovery/planning interpretation; retain the same source ID.
- No new controller job, primitive, route, helper, model policy, specialist owner, or runtime file is introduced. No evaluation framework or historical report is changed.

## Static acceptance and remaining uncertainty

Review both directions of each correction: settled versus proposed state; direct work versus consequential ambiguity; exploratory versus confirmatory purpose; provisional expression versus final communication; bounded action versus unsupported proof; observed behavior versus stated meaning under the relevant constraints. Check chapter/controller consistency and preservation of specialist handoffs.

Run the repository verification entrypoint for packaging, routing, helper/harness unit checks, and UTF-8/generated-artifact hygiene. These checks execute infrastructure code, not model experiments. Inspect the final diff and verify unchanged BOM/line-ending state and Unicode. Preserve the existing release metadata; this local revision is not a release.

Whether the revised contract is followed reliably, improves marketing output, reduces unnecessary work, or transfers across models remains unknown. Those questions require a separately designed later behavioral evaluation. This review does not conclude that the previous controller length, any model's reasoning capacity, or the knowledge-routing system caused poor outcomes.

## Static review and verification record

An independent read-only reviewer examined the working diff and relevant unchanged context. It reported no critical or important static issues and one minor ambiguity: who can adopt a candidate for the task. The controller and Chapter 03 now explicitly allow selection under already-delegated authority, without adding an approval gate or treating selection as factual verification. This was document review, not a trial of marketing-task behavior.

The repository verification entrypoint was run on 2026-09-07. Package validation passed with both the repository and installed validators; 68 routing-mechanics checks passed; all 261 routes and 233 evidence sources validated; all 138 Pressure Discovery infrastructure unit tests and 86 behavioral-harness unit tests passed. These existing tests use infrastructure/fixture contracts and do not establish marketing quality.

The full command exited nonzero at generated-artifact hygiene because 31 pre-existing `.pyc` files and their cache directories remain in the workspace. Their creation/modification timestamps are 2026-09-07 00:31:34-00:31:42 local time, before this editing session. They were preserved as unrelated workspace state. The full repository gate therefore is **not** reported as passing.

Separate byte-level inspection confirmed original UTF-8/BOM/CRLF state and the original non-ASCII character set in all six modified runtime files. The specialist paths, state handoffs, optional instruments, controller logical-route references, routing index, and helper remain unchanged. After the adoption-wording clarification, both package validators, all 261 routes / 233 sources, the encoding checks, local Markdown links, and `git diff --check` passed. Evaluation files, index, and scripts remain untouched. No live behavioral evaluation has been performed.

## Follow-up: exploration routing and fast-path meaning

Date: 2026-09-07. Scope explicitly authorized after the initial revision: clarify these two remaining controller ambiguities, with the corresponding Chapter 08 section aligned. The preceding preservation/verification record describes the initial revision; this follow-up deliberately changes the message/content routing prose and the existing `content.fast-path` section. No new route or selector is introduced.

### F1. Access to message guidance during strategic exploration

INPUT: explore open positioning choices using provisional messages.

CURRENT CUE: the controller permits provisional drafts, but the Chapter 04 entry starts with "Once the relevant positioning is sufficiently resolved".

AMBIGUITY: that opening can be read as requiring the strategic choice to be settled before its draft expression can be examined. This is a written-contract ambiguity, not an observed model failure.

CORRECTION: route to Chapter 04 by the actual open message/copy question. Chapter 03 continues to own positioning choices; Chapter 04 can help express candidate assumptions without requiring all positioning to be finalized first. Final communication still needs sufficiently resolved inputs and supported claims.

STATIC COUNTERCASES: an approved positioning used for a rewrite stays fixed; requested provisional alternatives remain candidates; a final artifact with a material unresolved strategic dependency still requires that dependency to be addressed; a narrow rewrite does not require Chapter 03 or Chapter 04 merely because both exist.

### F2. Direct execution versus an optional reference

INPUT: write a simple post with the job, message, proof, and representation context already sufficient.

CURRENT CUES: the controller permits direct fast-path work, while the platform address list maps a resolved writing task to `content.fast-path` and calls it the compile route.

AMBIGUITY: the same sufficient task can appear to require either no additional read or a mandatory route read.

CORRECTION: the controller fast path means direct execution with sufficient inputs. The stable logical ID `content.fast-path` names an optional reference, used only when its simple-writing guidance can resolve a remaining question. The address list and Chapter 08 section now express the same condition.

STATIC COUNTERCASES: fully supplied caption work can proceed directly; a remaining question about how text complements a supplied visual can justify the small reference; unresolved relationship or participation meaning still routes to the relevant deeper section; a current platform fact still requires authoritative verification when material. Artifact completeness and claim boundaries apply even when no knowledge is loaded.

These clarifications change the written routing contract only. They are not a claim that route use, response quality, or context consumption has improved in a model experiment.

Follow-up verification: both package validators passed through `scripts/verify.ps1 -PackageOnly`; 68 routing-mechanics checks passed; all 261 routes and 233 sources validated. The `content.fast-path` logical ID and heading selector remain unchanged. UTF-8, BOM state, CRLF, and existing Unicode were preserved in both runtime files. Reversing only this follow-up's replacements in memory reproduced the pre-turn file bytes exactly, confirming that earlier local edits were preserved. No behavioral experiment was run; the previously recorded full-gate cache limitation was not changed.

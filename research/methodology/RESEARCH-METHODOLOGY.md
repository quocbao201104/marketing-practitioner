# Research Methodology

Status: **PUBLIC RESEARCH METHOD — NOT RUNTIME INSTRUCTIONS**

This document defines how substantive research for Marketing Practitioner should be conducted before knowledge, semantics, or architecture are promoted into the repository.

It is intentionally separate from:

- `AGENTS.md`, which governs work inside the repository;
- `CONTRIBUTING.md`, which defines scope, change risk, protected surfaces, and validation expectations;
- the installable skill runtime, which should contain only operational knowledge and machinery that survived research and review.

Topic-specific directories under `research/` preserve the actual lineage: briefs, evidence, hypotheses, freezes, reviews, repairs, adjudications, and verification records.

The method is research-first, evidence-oriented, adversarial, and minimality-seeking.

The goal is not to collect the largest possible marketing knowledge base. The goal is to improve real practitioner decisions and bounded understanding while preserving provenance, uncertainty, architecture boundaries, and runtime reliability.

---

## 1. Begin with a bounded research question

Substantive research should normally begin because one of these has happened:

- a real task exposes a materially weak or incorrect decision;
- current guidance appears inconsistent with stronger evidence;
- an important practitioner decision has no clean owner or knowledge path;
- a bounded learning or problem-framing objective is needed before a practitioner decision can be named responsibly;
- an external paper, platform document, repository, framework, or practitioner workflow exposes a mechanism worth investigating;
- runtime evaluation shows that useful knowledge exists but is activated, routed, discovered, loaded, or composed incorrectly;
- a proposed abstraction cannot yet be justified against the existing repository grammar.

Do not begin from a desired table of contents or from:

> What else can be added?

Begin from:

> What decision-relevant failure, unresolved question, bounded learning objective, or credible mechanism deserves investigation?

For material work, frame the problem before implementation:

```text
INPUT / MATERIAL
→ CURRENT UNDERSTANDING / REPRESENTATION / ROUTE
→ FAILURE, OPEN QUESTION, OR LEARNING OBJECTIVE
→ WHY IT CAN CHANGE UNDERSTANDING, INTERPRETATION,
  OR A SUBSEQUENT DECISION
→ SMALLEST RESEARCH QUESTION
```

A bounded exploratory research question may precede a named practitioner decision. Do not invent a segment, intervention, campaign, or other downstream decision merely to justify discovery.

Research is allowed to conclude that no repository change is needed.

Research depth should follow the change-risk levels in `CONTRIBUTING.md`. Editorial work does not need a research track; architecture or project-boundary work should not begin with implementation.

---

## 2. Search broadly before designing locally

The first research pass should normally look outside the repository.

Useful source classes include:

- authoritative first-party documentation and policies;
- primary empirical research;
- reviews and strong methodological literature;
- formal or conceptual theory;
- established professional frameworks;
- practitioner documentation with clear scope;
- strong open-source repositories;
- evaluation and research repositories;
- implementation patterns from adjacent agent systems;
- market- or language-specific sources when local adaptation matters.

The first pass is for landscape discovery. Recover:

- established terminology and conceptual parents;
- common practitioner workflows;
- mechanisms worth investigating;
- known failure modes and counterexamples;
- evidence boundaries;
- places where the repository may disagree with stronger evidence.

Do not copy material into runtime knowledge simply because it looks useful.

Source discovery is not implementation.

For current platform capabilities, interfaces, policies, and platform-controlled constraints, prefer first-party documentation where available. For empirical or causal claims, prefer primary research, reviews, or strong methodological work when appropriate.

Repositories and practitioner sources are especially useful for mechanisms, workflows, architecture, implementation patterns, and professional practice, but they should not automatically be treated as empirical law.

Source quantity is not evidence quality.

One authoritative source may be sufficient when the claim is source-owned, directly stated, current, and kept within that source's scope. Triangulate when the conclusion requires synthesis, transfer, causal interpretation, generalization across regimes, architecture expansion, or resolution of material disagreement or uncertainty.

Additional sources are useful when they can plausibly change the bounded conclusion, scope, uncertainty, or repository action.

---

## 3. Separate gap discovery from deep value extraction

Research uses two different passes.

### Pass A — gap discovery

Ask:

- What capability is missing?
- What current behavior is weak?
- Which assumption is unsafe or unsupported?
- Where can owners conflict?
- What knowledge cannot currently be discovered or applied correctly?
- Does an existing owner already represent the proposed new concept?

This pass identifies pressure on the current system.

### Pass B — deep value extraction

Return to the strongest sources and inspect them beyond surface-level gap scanning.

Ask:

- What decision rules do competent practitioners use?
- What evidence changes the decision?
- What assumptions and constraints matter?
- What intermediate state or artifact exists between steps?
- What failure modes are recognized?
- What handoffs preserve meaning?
- What validation or stopping signals are used?
- What useful mechanism can improve an existing owner even if no new capability is needed?

A source can improve the repository without exposing a new gap.

The correct result may be a more precise existing module, a better route, a stronger handoff, or no new runtime knowledge at all.

---

## 4. Research the decision process, not only domain facts

Marketing Practitioner is intended to help an agent behave like a competent practitioner, not merely recall marketing facts.

For each area, try to recover:

```text
inputs
→ evidence requirements
→ decision variables or learning targets
→ assumptions
→ constraints
→ intermediate states / artifacts
→ candidate actions when applicable
→ failure conditions
→ downstream handoffs
→ validation signals
→ stopping conditions
```

Platform features, terminology, channel characteristics, cultural observations, and writing conventions matter only when their role in a decision or bounded learning objective is understood.

A useful question is:

> What does a competent practitioner need to know, decide, verify, preserve, hand off, revise, and stop doing?

Not every research task requires every element in the chain. Use only the structure needed to understand the bounded problem.

The target is operational reasoning, not handbook volume.

---

## 5. Preserve evidence scope and separate evidence type from project status

A source should support only the claim it actually establishes.

Preserve material scope where relevant:

- product or surface;
- market or geography;
- population;
- time period;
- account, delivery, or commercial regime;
- experimental or observational setting;
- measurement target or estimand.

Do not silently convert:

```text
source says X under conditions C
```

into:

```text
X is a universal practitioner rule
```

Do not use one label to combine evidence form, source provenance, and the repository's own inferential status.

### Source / evidence type

Record the type that matters for interpreting what a source can establish. Examples include:

- **AUTHORITATIVE FIRST-PARTY DOCUMENTATION** — source-owned capability, policy, interface, or constraint;
- **EMPIRICAL STUDY** — observed or experimentally estimated evidence under a stated design and scope;
- **REVIEW / META-ANALYSIS / METHODOLOGICAL SOURCE** — synthesis or guidance over a body of evidence or method;
- **FORMAL / CONCEPTUAL THEORY** — propositions or models whose conclusions depend on stated assumptions;
- **PROFESSIONAL PRACTICE** — established or credible practitioner methods and conventions;
- **IMPLEMENTATION / REPOSITORY EVIDENCE** — architecture, workflow, behavior, or failure evidence from an implemented system.

These examples are not a universal evidence hierarchy and do not need to become mandatory ledger categories.

### Project inferential status

Separately identify how the repository is using the conclusion:

- **EXTERNALLY SUPPORTED** — the conclusion stays within what relevant external evidence establishes;
- **PROFESSIONAL PRACTICE** — the repository adopts a credible practitioner convention without presenting it as empirical law;
- **PROJECT SYNTHESIS** — the repository creates a structure, interface, or operational rule by integrating evidence or practice;
- **CONTEXTUAL HYPOTHESIS** — a bounded proposition remains context-dependent or requires further validation;
- **UNKNOWN** — the available evidence does not resolve the question.

When synthesizing a mechanism, identify:

1. what each source type actually establishes;
2. what comes from professional practice;
3. what the project itself introduces or combines;
4. what remains uncertain.

Formal theory should not acquire the authority of observed evidence merely because it is academic, and first-party documentation should not be demoted into practitioner opinion merely because it is not an empirical study.

---

## 6. Triangulate when the conclusion requires it

Do not treat one paper, one repository, one platform document, or one practitioner framework as the complete answer by default.

But do not add sources ceremonially when one authoritative source already resolves a bounded source-owned fact.

Triangulate when the conclusion requires synthesis, transfer, causal interpretation, generalization, architecture promotion, or resolution of material disagreement or uncertainty.

When triangulation is warranted:

1. compare multiple relevant sources;
2. identify where they agree;
3. identify where they operate under different scopes or regimes;
4. identify contradictions and counterexamples;
5. separate terminology differences from substantive differences;
6. recover the smallest stable mechanism that survives the comparison.

When evidence conflicts, preserve the conflict or scope difference instead of manufacturing consensus.

The synthesis should distinguish external support from the repository's own integration decisions.

---

## 7. Compare the findings with the repository before designing new architecture

Before creating a new chapter, primitive, controller responsibility, state object, platform family, or adaptation layer, inspect the current system.

Determine:

- which owner already controls the decision;
- which handbook or platform module is authoritative;
- what state already represents the relevant information;
- what downstream owner consumes the result;
- whether the failure is actually missing knowledge;
- whether it is an ownership problem;
- whether it is routing or discovery;
- whether it is a retrieval-boundary problem;
- whether it is a state-handoff problem;
- whether it is composition or precedence;
- whether it is only scoped local evidence or expression guidance.

Prefer established conceptual parents and local repairs.

A theoretically elegant abstraction is not enough reason to expand shared architecture.

A research track should be capable of rejecting its own motivating abstraction.

---

## 8. Compress research into the smallest useful mechanism

Large research volume should not automatically become large runtime knowledge.

First determine what kind of correction the demonstrated problem actually requires. The following are semantic tests, not mandatory artifact categories:

- **CLARIFICATION** — use when an existing owner already represents the decision and the defect is ambiguity, scope, or interpretation;
- **EVIDENCE REQUIREMENT** — use when a conclusion is valid only when specified support is present;
- **GATE** — use only when proceeding without a condition would make the action invalid, unsafe, unauthorized, or materially misleading;
- **STATE / LEDGER** — use when a resolved fact, decision, constraint, or uncertainty must survive into later decisions;
- **HANDOFF** — use when responsibility or a decision product moves between existing owners and meaning must be preserved;
- **ROUTE / DISCOVERY EDGE** — use when sufficient knowledge already exists but cannot reliably be reached from the normal path;
- **WARNING / QUALIFICATION** — use when a bounded exception changes interpretation but does not require new control flow;
- **SCOPED ADAPTATION** — use when evidence demonstrates a local decision-changing mechanism that should refine an existing owner without creating a parallel ontology;
- **SMALL WORKFLOW** — use when several existing decisions must occur in a stable dependency order and a sequence, rather than a new owner, is what is missing;
- **EVALUATION ORACLE** — use when the main research result is a falsifiable condition for determining whether behavior is correct;
- **NOTHING** — use when the finding does not change a practitioner decision or bounded understanding enough to justify promotion, existing machinery already suffices, or evidence is insufficient.

Do not choose a formal mechanism merely because it appears smaller than another formal mechanism. Choose the least powerful mechanism that fixes the demonstrated failure while preserving ownership, state, and evidence boundaries.

Ask:

> Will this material change what the agent does, what the repository can justifiably conclude, or how a real decision is made?

If not, it probably does not belong on the runtime path.

Then ask:

> Can the demonstrated problem be corrected with less architecture?

Prefer the smaller defensible correction.

---

## 9. Preserve lineage, but do not turn research into another handbook

`research/` preserves provenance and reasoning. It is not an alternate runtime knowledge base.

Depending on the risk and maturity of a track, useful artifacts may include:

- a research brief;
- the motivating failure or counterexample;
- source maps, bibliographies, or evidence ledgers;
- rejected hypotheses;
- theory candidates and boundary analysis;
- freeze records;
- independent review briefs and results;
- adjudications;
- post-review repair records;
- post-repair verification;
- runtime evaluation notes.

Not every track needs every artifact.

Create an artifact because it preserves a material distinction, provenance boundary, or evaluation state — not because a template requires it.

The installable skill should contain only operational knowledge and runtime machinery that survived this process.

---

## 10. Try to falsify the preferred design

Before broad promotion, actively search for cases that would make the proposed mechanism fail.

Useful attacks include:

- realistic counterexamples where the rule gives the wrong decision;
- cases an existing owner already handles correctly;
- cross-owner conflicts;
- partial-state and missing-evidence cases;
- scope reversals;
- platform or market boundary cases;
- proposed abstractions that add terminology without changing behavior;
- local observations being generalized too far;
- retrieved excerpts whose meaning changes when surrounding context is restored.

A useful question is:

> Can a realistic task make this mechanism fail materially?

If yes, repair the theory before broad promotion.

If the mechanism is unnecessary, reject it.

---

## 11. Freeze and independently review material candidates

For substantive theory or implementation review, bind the target to an exact commit.

A review contract should make clear that:

- the reviewer evaluates exactly the frozen target;
- later repairs do not count as evidence for the original candidate;
- mergeability and green CI are not proof of conceptual correctness;
- research volume is not proof of validity;
- the author's own walkthrough is not independent evidence;
- the reviewer should search for material failure rather than defend the design;
- scope should remain bounded unless a demonstrated failure shows that the boundary itself is wrong.

After review, repair the demonstrated findings rather than opening an unrelated redesign.

For each material finding, ask:

- What exactly failed?
- What is the smallest structural correction?
- Does the correction preserve existing owners and boundaries?
- Did it introduce a regression?
- Did capability expand enough that theory review must reopen?

When findings are material, post-repair verification should check them individually. The goal is bounded closure, not a second open-ended review by default.

---

## 12. Distinguish knowledge quality from runtime quality

Correct guidance can still fail behaviorally if the agent does not reach or use it.

When research concerns runtime behavior, distinguish:

- **knowledge quality** — is the guidance correct and useful?
- **activation** — did the task trigger the skill?
- **routing** — was the correct owner selected?
- **discovery** — was the required route reachable?
- **loading** — was the required material actually retrieved?
- **retrieval meaning** — did the loaded slice preserve enough context to apply it correctly?
- **composition** — were multiple owners combined correctly?
- **state handoff** — were conclusions, constraints, evidence, and uncertainty preserved?
- **final behavior** — did the loaded knowledge materially improve the answer or action?

Where the hypothesis concerns retrieval or composition, inspect the path when practical:

```text
task
→ activation
→ controller state
→ routing decision
→ route discovery
→ knowledge loaded
→ order of reads
→ state / handoff produced
→ final behavior
```

Output-only evaluation can hide causal failure. A final answer may look correct despite an invalid path, or fail despite sufficient knowledge because the runtime never reached it.

If the required knowledge already exists, inspect the walker before adding more handbook:

- activation;
- route selection and discoverability;
- progressive loading;
- ordering and skip behavior;
- retrieval boundaries;
- state preservation;
- cross-owner handoffs.

Do not enlarge the handbook to compensate for a routing problem.

---

## 13. Benchmark hypotheses, not everything

Prefer focused evaluations tied to a causal question:

1. state the suspected failure;
2. define the expected route, state, or decision oracle;
3. create a focused positive, negative, or boundary case;
4. compare baseline and skill behavior when informative;
5. capture the relevant trace when needed;
6. determine whether the hypothesized failure actually occurred.

Do not run many tasks merely to produce a score.

A small adversarial case with a precise oracle can be more informative than a large benchmark whose failures cannot be diagnosed.

Preserve important invariants during evaluation: do not invent evidence, do not treat missing evidence as negative evidence, do not infer causality from attribution, preserve resolved user constraints, preserve source scope, and preserve ownership boundaries unless the research itself demonstrates that they are wrong.

---

## 14. Treat real tasks, external repositories, and local markets as probes — not automatic truth

Real user tasks are valuable because they expose composition failures that isolated chapter review may miss.

Convert an observed failure or learning objective into a bounded probe:

```text
observed task / material
→ isolate the failing mechanism or bounded learning target
→ formulate the smallest research question
→ inspect evidence and architecture
→ propose the smallest correction when one is justified
→ test or adversarially review it when material
```

External repositories are research material, not dependencies by default. Extract useful mechanisms, understand their assumptions, compare them with the repository, and adapt only what survives that comparison.

Local-market research should remain evidence-bounded adaptation rather than a parallel marketing ontology. Keep shared reasoning with the existing owner unless local evidence demonstrates a decision-changing mechanism that requires scoped adaptation.

Do not generalize one real task, repository pattern, native intuition, anecdote, or local observation beyond what the evidence and counterexamples justify.

---

## 15. Stop when the bounded decision or learning objective is sufficiently resolved

Research should not continue merely because more sources can be found.

Stop when there is enough evidence and counterexample pressure to make the bounded repository decision responsibly, or to answer the bounded learning objective at the claimed level, while preserving material uncertainty.

Ask whether another source can plausibly change:

- the conclusion;
- its scope;
- its uncertainty;
- the interpretation of an important counterexample;
- or the repository action.

If not, additional search is usually low-value.

Valid outcomes include:

- implement a bounded correction;
- strengthen an existing module;
- repair routing or retrieval instead of knowledge;
- improve problem framing without yet promoting a runtime rule;
- keep a finding as evidence only;
- reject the proposed abstraction;
- keep the current architecture unchanged;
- defer because the evidence is insufficient;
- separate a capability rather than distort the project boundary.

The stopping criterion is **decision or learning sufficiency**, not exhaustion of the literature.

---

## Practical research loop

A typical substantive track follows this loop:

```text
1. OBSERVE
   Identify a real failure, unresolved question,
   bounded learning objective, or credible external mechanism.

2. FRAME
   Define the smallest research question that can change
   understanding, interpretation, or a subsequent decision.
   Do not invent a downstream decision merely to justify discovery.

3. MAP CURRENT STATE
   Identify the existing owner, route, state, evidence,
   and architecture boundary when the question touches them.

4. SEARCH
   Survey the source classes appropriate to the claim.
   Do not multiply sources when one authoritative source
   already resolves a bounded source-owned fact.

5. DISCOVER GAPS
   Identify what is missing, weak, unsafe, contradictory,
   or unreachable.

6. DEEP DIVE
   Return to the strongest sources and extract decision rules,
   learning targets, states, constraints, handoffs, failures,
   and stopping signals.

7. TRIANGULATE WHEN NEEDED
   Compare sources, scopes, regimes, and counterexamples when
   the conclusion requires synthesis, transfer, generalization,
   causal interpretation, architecture promotion, or conflict resolution.

8. CLASSIFY EVIDENCE AND INFERENCE
   Preserve source/evidence type separately from how the project
   uses the conclusion: external support, professional practice,
   project synthesis, contextual hypothesis, or unknown.

9. SYNTHESIZE
   Recover the smallest mechanism or bounded conclusion that
   improves practitioner reasoning.

10. CHALLENGE
    Try to falsify the mechanism and reject unnecessary
    abstractions before implementation.

11. DESIGN MINIMALLY
    Choose the least powerful correction that closes the
    demonstrated failure: clarification, evidence requirement,
    gate, state, handoff, route, qualification, workflow,
    evaluation oracle, scoped adaptation, or nothing.

12. PRESERVE LINEAGE
    Record only the artifacts needed to preserve provenance,
    uncertainty, rejected hypotheses, and review boundaries.

13. FREEZE / REVIEW WHEN MATERIAL
    Bind substantive review targets to an exact commit
    and search independently for material failure.

14. REPAIR / VERIFY
    Correct demonstrated defects and verify bounded closure.

15. TEST RUNTIME WHEN RELEVANT
    Evaluate activation, routing, discovery, loading,
    retrieval meaning, composition, handoffs, and behavior.

16. REFINE THE WALKER WHEN NEEDED
    If sufficient knowledge exists but is not reached or used,
    repair the path rather than compensating with prose.

17. GENERALIZE CAREFULLY
    Promote only as far as evidence, counterexamples,
    and observed behavior justify.

18. STOP
    End when the bounded decision or learning objective is
    sufficiently resolved; preserve remaining uncertainty explicitly.
```

---

# Core principle

The repository should not become the largest marketing knowledge base possible.

Research should establish the smallest amount of trustworthy knowledge, evidence discipline, state, routing, and decision machinery required to improve the bounded understanding or practitioner decision in front of the agent.

A successful research track makes clear:

- what is known;
- what remains uncertain;
- what each source type actually supports;
- what the project synthesized;
- which owner should act when an owner is implicated;
- what failure or learning objective was addressed;
- how the result was challenged when material;
- and why the resulting architecture is no larger than necessary.

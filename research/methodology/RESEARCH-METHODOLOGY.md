# Research Methodology

Status: **PUBLIC RESEARCH METHOD — NOT RUNTIME INSTRUCTIONS**

This document describes how substantive research for Marketing Practitioner should be conducted when the repository is being extended, corrected, or challenged.

It is intentionally separate from `AGENTS.md`, `CONTRIBUTING.md`, and the installable skill runtime.

- `AGENTS.md` explains how agents should work inside the repository.
- `CONTRIBUTING.md` defines contribution boundaries, change risk, protected surfaces, and validation expectations.
- this document explains how research should establish, challenge, synthesize, and operationalize knowledge before it is promoted into the repository;
- topic-specific directories under `research/` preserve the actual lineage: briefs, evidence, hypotheses, freezes, reviews, repairs, adjudications, and verification records.

The method is research-first, evidence-oriented, adversarial, and minimality-seeking.

Its purpose is not to maximize the amount of marketing knowledge collected. Its purpose is to improve the quality of decisions the skill can make while preserving provenance, uncertainty, architecture boundaries, and runtime reliability.

---

## 1. Start from a decision-relevant problem

Substantive research should normally begin because at least one of the following is true:

- a real task exposes a materially weak or incorrect decision;
- a current rule or explanation appears inconsistent with stronger evidence;
- an important practitioner decision has no clean owner or knowledge path;
- an external paper, platform document, repository, framework, or practitioner workflow exposes a mechanism that may improve an existing capability;
- a runtime evaluation shows that useful knowledge exists but is activated, routed, discovered, loaded, or composed incorrectly;
- a proposed new abstraction cannot yet be justified against existing repository grammar.

Do not begin from a desired table of contents or from the question:

> What else can be added?

Begin from:

> What decision-relevant failure, unresolved question, or credible mechanism deserves investigation?

For higher-risk work, make the motivating failure explicit before implementation.

A useful form is:

```text
INPUT / TASK
→ CURRENT REPRESENTATION OR ROUTE
→ FAILURE OR OPEN QUESTION
→ WHY IT CHANGES THE DECISION
→ SMALLEST RESEARCH QUESTION
```

A research result is allowed to conclude that no repository change is needed.

---

## 2. Match research depth to change risk

Not every change requires the same process.

### Level 0 — editorial or mechanical

Ordinary wording, formatting, broken-link, metadata, or obvious reference corrections do not require a research track.

### Level 1 — bounded knowledge or evidence update

Research should identify the exact claim or decision affected, prefer the strongest available evidence, preserve material scope, and update only the smallest relevant surface.

A formal theory freeze or independent adversarial review is usually unnecessary unless the change unexpectedly alters shared semantics.

### Level 2 — runtime or shared semantic change

Research should reproduce or clearly state the concrete failure, inspect the relevant owner and retrieval path, gather decision-relevant evidence, compare candidate repairs, and define a targeted validation or adversarial counterexample.

### Level 3 — architecture or project-boundary expansion

Do not begin with implementation.

First establish that the current repository cannot represent or handle the problem cleanly without material distortion. Search for established conceptual parents before inventing project-specific primitives. Separate theory research from runtime promotion when doing so prevents premature architecture.

Material Level 3 work should normally leave a visible research lineage and pass an explicit freeze and independent review before broad runtime promotion.

---

## 3. Search broadly before designing locally

The first research pass should normally look outside the repository.

Relevant source classes may include:

- first-party platform documentation and policies;
- primary academic research;
- systematic reviews and strong methodological literature;
- established professional frameworks;
- practitioner documentation with clear scope and provenance;
- strong open-source repositories;
- evaluation and research repositories;
- implementation patterns from adjacent agent systems;
- market-specific or language-specific sources when local adaptation is material.

Search broadly enough to understand the landscape before committing to a local abstraction.

The first pass should recover things such as:

- established terminology;
- conceptual parents;
- common practitioner workflows;
- mechanisms worth investigating;
- known failure modes;
- evidence boundaries;
- important counterexamples;
- areas where the repository may already disagree with stronger evidence.

Do not copy material into runtime knowledge during this stage merely because it appears useful.

Source discovery is not implementation.

---

## 4. Separate gap discovery from deep value extraction

Research uses two different modes that should not be collapsed into one.

### Pass A — gap discovery

Ask:

- What capability is missing?
- What current behavior is weak?
- Which assumption is unsupported or unsafe?
- Where can multiple owners conflict?
- What knowledge cannot currently be discovered or applied at runtime?
- Which proposed abstraction appears unnecessary because an existing owner may already represent it?

The purpose is to identify decision-relevant pressure on the current system.

### Pass B — deep value extraction

Return to the strongest sources and inspect them beyond surface-level gap scanning.

Ask:

- What decision rules do practitioners actually use?
- What evidence changes the decision?
- What intermediate state or artifact exists between steps?
- What constraints or guardrails matter?
- What failure modes are recognized?
- What handoffs preserve meaning between decisions?
- What workflow structure is stronger than the current repository?
- What useful mechanism improves an existing owner even when no new capability is required?

This second pass is important because a source can improve the repository without exposing a new gap.

The correct result may be a more precise existing module, a better route, a stronger handoff, or no new runtime knowledge at all.

---

## 5. Research the decision process, not only domain facts

Marketing Practitioner is intended to help an agent behave like a competent practitioner, not merely recall marketing facts.

For each researched area, try to recover the decision process:

```text
inputs
→ evidence requirements
→ decision variables
→ assumptions
→ constraints
→ intermediate states or artifacts
→ candidate actions
→ failure conditions
→ downstream handoffs
→ validation signals
→ stopping conditions
```

Facts such as platform features, terminology, channel characteristics, cultural observations, or copywriting conventions are useful only when their role in a decision is clear.

A useful research question is:

> What does a competent practitioner need to know, decide, verify, preserve, hand off, revise, and stop doing?

The target is operational reasoning, not handbook volume.

---

## 6. Preserve source meaning and scope

A source should support only the claim it actually establishes.

For substantive empirical material, preserve material scope such as:

- product or surface;
- market or geography;
- population;
- time period;
- account or delivery regime;
- commercial regime;
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

Prefer first-party documentation for current platform capabilities, interfaces, policies, and platform-controlled constraints.

Prefer primary research, systematic reviews, or strong methodological work for empirical and causal claims when available.

Repositories and practitioner sources are especially useful for mechanisms, workflows, architecture, implementation patterns, failure modes, and professional practice, but their claims should not automatically be treated as empirical law.

Source quantity is not evidence quality.

---

## 7. Keep epistemic status explicit

Not every useful mechanism has the same evidential status.

Use distinctions such as:

- **EMPIRICAL / ACADEMIC** — supported by relevant research evidence;
- **PROFESSIONAL PRACTICE** — established or credible practitioner practice that is useful but not equivalent to an empirical law;
- **PROJECT SYNTHESIS** — a repository-specific structure created to operationalize evidence or practice;
- **CONTEXTUAL HYPOTHESIS** — a bounded proposition that remains dependent on context or requires further validation.

When synthesizing a mechanism, identify:

1. what the external evidence directly supports;
2. what comes from professional practice;
3. what the project itself introduces for operational use;
4. what remains uncertain or context-dependent.

Do not allow an elegant project synthesis to masquerade as externally established truth.

Keep `UNKNOWN` when the evidence does not resolve the question.

---

## 8. Compare findings against the existing repository before designing new architecture

Before creating a new chapter, primitive, controller responsibility, state object, platform family, or adaptation layer, inspect the current repository.

Determine:

- which owner already controls the decision;
- which handbook or platform module is authoritative;
- what state already represents the relevant information;
- what downstream owner consumes the result;
- whether the failure is actually missing knowledge;
- whether it is an ownership problem;
- whether it is a routing or discovery problem;
- whether it is a retrieval-boundary problem;
- whether it is a state-handoff problem;
- whether it is a composition or precedence problem;
- whether the issue is merely local evidence or expression guidance.

Prefer established parents and local repairs.

A theoretically attractive abstraction is not enough reason to expand shared architecture.

A research track should be able to reject its own motivating abstraction.

---

## 9. Synthesize across sources before operationalizing

Research should not treat one paper, one repository, one platform document, or one practitioner framework as the complete answer by default.

Where the decision warrants it:

1. compare multiple relevant sources;
2. identify where they agree;
3. identify where they operate under different scopes or regimes;
4. identify contradictions and counterexamples;
5. separate terminology differences from substantive differences;
6. recover the smallest stable mechanism that survives the comparison.

When evidence conflicts, preserve the conflict or scope difference instead of forcing false consensus.

The synthesis should make clear which conclusions are directly supported and which are repository-level integration decisions.

---

## 10. Compress research into the smallest useful operational structure

Large research volume should not automatically become large runtime knowledge.

The preferred result is often one or more of:

- a decision rule;
- a gate;
- an evidence requirement;
- a state field or bounded ledger;
- a state handoff;
- a routing or discovery edge;
- a failure warning;
- a scoped local adaptation rule;
- a small workflow;
- a targeted evaluation oracle;
- a clarification of an existing owner.

A useful test is:

> Will this material change what the agent does on a real decision?

If not, it probably does not belong on the runtime path.

Another useful test is:

> Can the demonstrated problem be corrected with less architecture?

Prefer the smaller defensible correction.

---

## 11. Preserve research lineage separately from runtime knowledge

`research/` exists to preserve provenance and reasoning, not to become an alternate runtime handbook.

Depending on the risk and maturity of a track, useful research artifacts may include:

- a research brief;
- the motivating failure or counterexample;
- source maps or bibliographies;
- evidence ledgers;
- rejected hypotheses;
- theory candidates;
- boundary analysis;
- freeze records;
- independent review briefs;
- adversarial review results;
- adjudications;
- post-review repair records;
- post-repair verification;
- runtime evaluation notes.

Not every research task needs every artifact.

Create artifacts because they preserve a decision-relevant distinction or evaluation boundary, not because a template requires them.

The installable skill should contain only the operational knowledge and runtime machinery that survived this process.

---

## 12. Use falsification before promotion

Research should actively try to disprove the preferred design.

Useful attacks include:

- realistic counterexamples where the rule makes the wrong decision;
- examples that an existing owner already handles correctly;
- cross-owner conflicts;
- partial-state cases;
- missing-evidence cases;
- scope reversals;
- platform or market boundary cases;
- cases where the proposed abstraction adds terminology without changing behavior;
- cases where a local rule is incorrectly generalized;
- cases where retrieved context changes the meaning of an isolated excerpt.

A useful question is:

> Can a realistic task make this mechanism fail materially?

If yes, repair the theory before broad promotion.

If the mechanism is unnecessary, reject it.

---

## 13. Freeze material candidates before independent review

For substantive theory or implementation review, bind the target to an exact commit before evaluation.

The review contract should make clear that:

- the reviewer evaluates exactly the frozen target;
- later fixes do not count as evidence for the original candidate;
- mergeability and green CI are not proof of conceptual correctness;
- research volume is not proof of validity;
- the author's own walkthrough is not independent evidence;
- the reviewer should search for material failure rather than defend the design;
- the review should remain within the frozen research question unless a failure demonstrates that the boundary itself is wrong.

Freezing prevents later repairs from contaminating evaluation of the original candidate.

---

## 14. Repair demonstrated defects, not everything imaginable

After review, repair the findings that were actually demonstrated.

Do not use a repair cycle as permission for unrelated redesign, architecture expansion, or another open-ended research program.

For each material finding, ask:

- What exactly failed?
- What is the smallest structural correction?
- Does the correction preserve existing owners and boundaries?
- Does it introduce a regression?
- Does it expand capability enough that theory review must reopen?

A documented acknowledgment is not necessarily a structural repair.

---

## 15. Verify closure independently when the findings are material

Post-repair verification should check the original findings one by one.

Useful questions include:

- Is the original defect actually closed?
- Is the closure structural or merely explanatory?
- Did the repair preserve the frozen theory boundary?
- Did another owner, route, or state become inconsistent?
- Did capability expand beyond the reviewed scope?
- Is renewed theory review required?

The goal is bounded closure, not a second broad review by default.

---

## 16. Distinguish knowledge quality from runtime quality

A correct handbook can still fail behaviorally if the agent does not reach or use the right knowledge.

When the research question concerns runtime behavior, distinguish at least:

- **knowledge quality** — is the guidance itself correct and useful?
- **activation** — did the task trigger the skill?
- **routing** — was the correct knowledge owner selected?
- **discovery** — was the required route reachable from the normal path?
- **loading** — was the required material actually retrieved or read?
- **retrieval meaning** — did the loaded slice preserve enough context to apply the guidance correctly?
- **composition** — were multiple owners combined in the right order and with the right precedence?
- **state handoff** — were conclusions, constraints, evidence, and uncertainty preserved across decisions?
- **final behavior** — did the loaded knowledge actually change the answer or action appropriately?

Do not infer runtime success from static knowledge quality alone.

---

## 17. Evaluate paths, not only outputs

Output-only evaluation can hide causal failure.

A final answer can look correct even when the path is invalid, and an answer can fail even though the required knowledge exists because the runtime never reached it.

Where the hypothesis concerns retrieval or composition, capture the path when practical:

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

Compare the observed path with an oracle tied to the research hypothesis.

Relevant failure classes include:

- no activation;
- activation without discovery of the required route;
- wrong owner selected;
- correct owner reached too late;
- missing prerequisite;
- excessive irrelevant loading;
- multiple owners loaded but composed incorrectly;
- required context lost at a retrieval boundary;
- correct knowledge loaded but ignored;
- final output accidentally succeeds despite an invalid path.

---

## 18. Optimize the walker before adding more handbook

When the required knowledge already exists, weak behavior should not automatically be repaired by adding more prose.

Inspect first:

- activation;
- route selection;
- route discoverability;
- progressive loading;
- ordering;
- skip behavior;
- retrieval boundaries;
- state preservation;
- cross-owner handoffs.

If the failure is reachability or use, repair the walker.

Do not enlarge the handbook to compensate for a routing problem.

---

## 19. Benchmark hypotheses, not everything

Broad behavioral benchmarks are expensive and often difficult to interpret causally.

Prefer a small evaluation tied to a specific hypothesis:

1. state the suspected failure;
2. define the expected route, state, or decision oracle;
3. create a focused positive, negative, or boundary case;
4. compare baseline and skill behavior when that comparison is informative;
5. capture the relevant route or read trace when needed;
6. determine whether the hypothesized failure actually occurred.

Do not run many tasks merely to produce a score.

A small adversarial case with a precise causal question can be more informative than a large benchmark whose failures cannot be diagnosed.

---

## 20. Preserve invariants during research and evaluation

An apparent improvement is not valid if it violates a more important invariant.

Examples include:

- do not invent evidence;
- do not fabricate metrics or testimonials;
- do not infer causality merely from attribution;
- do not treat missing evidence as negative evidence;
- do not choose a platform solely because its noun appears in the task;
- preserve user constraints and already-resolved state;
- mark material assumptions;
- preserve source scope and epistemic status;
- preserve ownership and precedence boundaries unless the research demonstrates that they are wrong.

The exact invariant set depends on the researched surface, but it should be explicit when a violation would invalidate the result.

---

## 21. Use real tasks as research probes

Real user tasks are valuable because they expose composition failures that isolated chapter review may miss.

When a real task reveals a failure, convert it into a bounded research probe:

```text
observed task
→ isolate the failing mechanism
→ formulate the smallest research question
→ inspect relevant evidence and architecture
→ propose the smallest correction
→ test or adversarially review the correction
```

Do not generalize one observed failure beyond what the evidence and counterexamples justify.

A real task is a probe, not automatically a universal rule.

---

## 22. Treat external repositories as research material, not dependencies by default

Strong repositories can be valuable sources of:

- architecture;
- workflow design;
- evidence discipline;
- progressive disclosure;
- routing and retrieval patterns;
- evaluation methods;
- failure handling;
- humanization or writing mechanisms;
- domain-specific decision structures.

The default objective is not to merge another repository wholesale.

Extract the mechanism, understand its assumptions, compare it with Marketing Practitioner's architecture, and adapt only what survives that comparison.

A repository can be valuable even when none of its code or prose is copied.

---

## 23. Handle localization as evidence-bounded adaptation

Local research should not become a parallel marketing ontology.

Keep shared marketing reasoning in the existing core owner unless local evidence demonstrates a decision-changing mechanism that requires a scoped adaptation.

Local research may investigate:

- linguistic realization;
- relationship expression;
- politeness and address conventions;
- culturally sensitive framing;
- local platform or commerce constraints;
- market-specific evidence that changes how a shared decision is realized.

Do not infer broad population behavior from native familiarity, anecdotes, or isolated local observations.

A locale contribution should remain thin, scoped, replaceable, and evidence-backed.

---

## 24. Stop when the bounded research question is sufficiently resolved

Research should not continue merely because more sources can be found.

Stop when there is enough evidence and counterexample pressure to make the bounded repository decision responsibly, while preserving material uncertainty.

Possible valid stopping outcomes include:

- implement a bounded correction;
- strengthen an existing module;
- repair routing or retrieval instead of knowledge;
- keep a finding as evidence only;
- reject the proposed abstraction;
- keep the current architecture unchanged;
- defer because the evidence is insufficient;
- fork or separate a capability rather than distort the project boundary.

More research volume is not inherently better.

The stopping criterion is decision sufficiency, not exhaustion of the literature.

---

## 25. Practical research loop

A typical substantive track follows this loop:

```text
1. OBSERVE
   Identify a real failure, unresolved decision,
   or credible external mechanism.

2. FRAME
   Define the smallest decision-relevant research question.

3. MAP CURRENT STATE
   Identify the existing owner, route, state, evidence,
   and architecture boundary before proposing a replacement.

4. SEARCH
   Survey primary sources, research, strong repositories,
   professional practice, and local evidence where material.

5. DISCOVER GAPS
   Identify what is missing, weak, unsafe, contradictory,
   or unreachable.

6. DEEP DIVE
   Return to the strongest sources and extract mechanisms,
   decision rules, states, constraints, handoffs, and failures.

7. TRIANGULATE
   Compare sources, scopes, counterexamples, and regimes.

8. CLASSIFY EPISTEMIC STATUS
   Separate external evidence, professional practice,
   project synthesis, and contextual hypotheses.

9. SYNTHESIZE
   Recover the smallest mechanism that can improve
   a real practitioner decision.

10. CHALLENGE
    Try to falsify the mechanism and reject unnecessary
    abstractions before implementation.

11. DESIGN MINIMALLY
    Make the smallest correction compatible with existing
    ownership, routing, state, and evidence boundaries.

12. PRESERVE LINEAGE
    Record the artifacts needed to make provenance,
    uncertainty, rejected hypotheses, and review boundaries clear.

13. FREEZE WHEN MATERIAL
    Bind substantive review targets to an exact commit.

14. ADVERSARIAL REVIEW
    Search for material failure rather than defending the design.

15. REPAIR BOUNDEDLY
    Correct demonstrated defects without unrelated expansion.

16. VERIFY CLOSURE
    Re-check the original findings and regressions.

17. TEST RUNTIME WHEN RELEVANT
    Evaluate activation, routing, discovery, loading,
    retrieval meaning, composition, handoffs, and final behavior.

18. REFINE THE WALKER WHEN NEEDED
    If the knowledge exists but is not reached or used,
    repair the path rather than adding prose.

19. GENERALIZE CAREFULLY
    Promote the mechanism only as far as the evidence,
    counterexamples, and observed behavior justify.

20. STOP
    End the track when the bounded decision is sufficiently
    resolved; preserve remaining uncertainty explicitly.
```

---

# Core principle

The repository should not become the largest marketing knowledge base possible.

The research process exists to establish the smallest amount of trustworthy knowledge, state, routing, evidence discipline, and decision machinery required for an agent to behave more like a competent marketing practitioner on the task in front of it.

Research is successful when it improves a real decision while making clear:

- what is known;
- what is uncertain;
- what the evidence actually supports;
- which owner should act;
- what should be loaded;
- what must be preserved between decisions;
- what failure was corrected;
- and why the resulting architecture is no larger than necessary.

# Stateful Work-Episode Evaluation for Agent Skills — Research Brief

Status: **BOUNDED RESEARCH QUESTION — IMPLEMENTATION BLOCKED**

## Research question

> How should an agent skill be adversarially evaluated in stateful, consequential work episodes such that the evaluation can distinguish work quality, behavioral robustness, and the marginal effect of making the skill available, without rewarding conformity to the skill's intended internal procedure or over-attributing observed improvements to unrandomized mechanisms?

## Why this track exists

Marketing Practitioner already has two relevant foundations:

- `evals/behavioral/` — paired no-skill / skill execution, workspace isolation, sealed run records, blind review, frozen execution profiles, and route reconstruction used as diagnostic evidence rather than answer-quality scoring;
- `evals/pressure-discovery/` — framework-blind scenario construction, semantic predicates, validity attacks, sensitivity/invariance relations, materiality, noncanonical-valid-answer acceptance, and fail-closed mechanism attribution.

Those systems are strong for bounded cases and mechanism discovery, but they do not yet define a full work episode in which earlier actions mutate a world, later evidence arrives, and subsequent correctness depends on prior state and consequences.

The goal of this track is therefore not to build a third evaluator framework. It is to determine the smallest defensible stateful extension of the existing evaluation architecture.

## In scope

- mutable world state across a professional work episode;
- observable agent, actor, and environment actions;
- temporal obligations and consequential action history;
- bounded actor knowledge and authority;
- prelocked event delivery rules;
- normal competence plus adversarial pressure/control testing;
- paired no-skill / skill-available comparison;
- run, work, and comparative validity;
- mechanism telemetry without unsupported causal attribution;
- execution burden such as tokens, questions, tool calls, latency, and unfinished work.

## Out of scope

This track is not:

- a general AI-agent benchmark survey;
- a leaderboard project;
- a security prompt-injection benchmark;
- a handbook-conformance test;
- a redesign of Marketing Practitioner runtime architecture;
- a new routing ontology;
- a request to add marketing knowledge;
- evidence of real-world revenue or business uplift;
- permission to optimize the skill before a concrete failure is observed.

## Core construct

A task qualifies as a stateful work episode only when at least one material dependency exists:

```text
state_t
+
action_or_event_t
→ state_t+1
→ changes what is later feasible, justified, required,
  authorized, recoverable, or costly
```

Many turns, files, or tokens are not sufficient by themselves.

## Research lineage

The research proceeded in four bounded passes:

1. **Landscape discovery** — map agent-evaluation approaches relevant to state, skill/no-skill comparison, adversarial evaluation, workplace realism, and evaluator validity.
2. **Deep extraction** — recover state models, scoring contracts, simulator constraints, paired-comparison semantics, and known evaluator failure modes.
3. **Unresolved-method analysis** — investigate consequence/reversibility, behavior at applicable decision points, and limits on mechanism attribution.
4. **Candidate synthesis** — define the smallest extension compatible with existing Pressure Discovery and Behavioral Harness machinery, then submit it to independent adversarial review.

## Implementation gate

No Episode 01 design or sandbox implementation may begin until:

1. the candidate methodology survives independent adversarial methodology review;
2. all material review findings are repaired;
3. a closure-only independent verification confirms those repairs without exposing a new material methodology defect.

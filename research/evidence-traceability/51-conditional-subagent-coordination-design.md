# Conditional Subagent Coordination: Bounded Design Record

Date: 2026-09-08.

The user requested conditional subagent coordination for larger tasks and approved the proposed principles before implementation. This extends the existing core continuity and dependency rules; it does not introduce a separate agent runtime or a general orchestration domain.

## Demonstrated design need

```text
TASK
Review pricing evidence and candidate formulas, then deliver a recommendation.

EXISTING CORE
Preserves goals, dependencies, sources and completion in the lead's work.

GAP
Does not explicitly specify when to delegate, what context travels,
or how returned work is reconciled with the current task.

DECISION CONSEQUENCE
Assignments can resolve different assumptions, amplify one shared source,
or return stale artifacts that the lead accepts without integration.

SMALLEST CORRECTION
Add conditional coordination guidance beside multi-step continuity.
```

This chain is a static design rationale, not a report of an observed agent failure. The added rules are project synthesis and do not claim experimentally validated productivity or reliability gains.

## Implementation and boundaries

The new `Coordinating subagents when useful` section in [SKILL.md](../../skills/marketing-practitioner/SKILL.md) covers:

- conditional use based on availability, permission, useful decomposition and coordination cost;
- assignment context, dependencies, evidence status, action/edit scope and bounded work;
- lead responsibility for all requested outputs, integration and final validation;
- bounded concurrency, duplicate work, edit ownership, further delegation and changed scope;
- source-level assessment, disagreement handling, late results, failure and local continuation.

The existing host and user authorization rules govern whether delegation is permitted. The skill does not grant tool access or require a new permission step when authorization already exists. It also does not require subagents for every large task, a fixed agent count, a particular model, a new branch, or a mandatory report template.

The whole instruction fits in the existing entrypoint. No supporting runtime file or route is needed for this bounded addition. Price-related changes and reports 49-50 already present in the worktree are preserved unchanged by this turn.

## Static assessment and verification

[Eight bounded cases](../../evals/subagent-coordination-bounded-cases.md) cover independent work, coupled outputs, narrow/unavailable delegation, missing context and authority, shared-source agreement, shared edits and late results, budget/failure handling, and artifact validation.

The design review checks those cases against the added section and the existing controller. In particular, parallelism does not settle upstream positioning, source agreement does not create independent evidence, and an assignment's completion does not establish final artifact quality. Failure or missing tools uses the existing uncertainty policy rather than creating a new blocker.

Verification includes package validators, route/source validation, routing-mechanics checks, inspection of the final core diff, report links and text integrity. These mechanical checks cannot establish agent compliance. No live subagent trial, effectiveness benchmark, new empirical citation, commit, push or release is included.

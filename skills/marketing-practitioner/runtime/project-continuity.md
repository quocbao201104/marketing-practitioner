# Project Continuity and Durable Memory

## Purpose

Use persistent project context to improve continuity across marketing decisions without changing the core reasoning workflow or treating stored memory as fresh evidence.

This policy defines **memory behavior**, not a storage implementation. Use whatever project-scoped persistence the host legitimately exposes: native project memory, workspace state, project-local files, or another durable store. Do not require a specific file name, database, schema, or vendor API.

If no suitable persistent capability is available, continue the task normally and do not imply that durable memory was written.

## 1. Memory surrounds the task; it does not become the task

Persistent memory should normally affect work at two boundaries:

```text
BEFORE WORK
retrieve only durable context that can materially change the current job

MAIN WORK
run the normal Marketing Practitioner controller

AFTER WORK
consider whether anything durable changed and should be persisted
```

Do not continuously interrupt research, diagnosis, positioning, or writing to maintain memory. Working notes, tentative hypotheses, and intermediate reasoning belong to the current task unless they later become durable.

## 2. Prefer the narrowest durable scope

Project-specific marketing knowledge should remain project-scoped.

Do not promote a project fact, campaign result, strategic decision, or project-specific learning into user-wide or global memory unless the user explicitly makes it general.

Examples:

- "Campaign 8 targets enterprise buyers" is project/campaign-scoped.
- "The user always wants decision memos under five bullets" may be broader only when the user clearly states it as a durable general preference.
- "This audience rejected angle X" must not become "the user dislikes angle X."

When several persistence scopes are available, choose the narrowest durable scope that correctly owns the information.

## 3. Retrieve selectively

At task start, retrieve persistent context only when it can materially change the current decision, interpretation, claim boundary, or requested artifact.

Useful durable context may include current product facts, active positioning, accepted decisions, recent relevant results, claim constraints, unresolved questions, or prior scoped learning.

Do not load the entire project history by default. Old campaigns, obsolete decisions, unrelated preferences, and raw archives should stay out of context unless the current job makes them relevant.

## 4. Stored memory is context, not independent evidence

Persistence does not increase evidentiary weight.

A stored interpretation remains an interpretation. A stored decision remains a decision. A stored result remains evidence only to the extent supported by its original source or design.

Never reason in a self-reinforcing loop such as:

```text
agent infers A
→ stores A
→ later retrieves A
→ treats stored A as independent support
→ becomes more confident in A
```

When material, preserve enough provenance to distinguish sources such as user statements, product documentation, analytics, interviews, experiments, accepted decisions, and agent interpretation.

## 5. Reconcile freshness and conflict before reuse

Memory may be stale.

When retrieved memory conflicts with newer or more authoritative current evidence, do not silently average them together. Determine whether the old information was wrong, scoped differently, or valid only for an earlier product/market state.

Prefer current authoritative evidence for the present decision while preserving historical context when it remains useful.

A changed fact or decision should normally be **superseded**, not erased as if it never existed.

Examples:

- "No WhatsApp support" may remain historically true but become superseded after the integration ships.
- A prior SMB positioning decision may remain part of decision history even after the team deliberately changes target.

## 6. Persist conservatively

Be proactive about durable continuity but conservative about what becomes durable.

Information is a candidate for persistence when it is both useful beyond the immediate turn and sufficiently established for its role. Common durable roles include:

- **fact** — a confirmed project or product state;
- **evidence/result** — a source-grounded observation, measurement, customer record, or experiment/campaign result;
- **decision** — a choice the user or team actually accepted, committed to, or acted on;
- **scoped learning** — an interpretation mature enough to affect a later decision, with its limits retained;
- **supersession** — a durable indication that an earlier fact, decision, or model is no longer current.

These are semantic roles, not required storage types or schemas.

## 7. Do not persist tentative work as durable truth

Do not make the following durable merely because they appeared during a task:

- brainstorming;
- a question framed as a possibility;
- an unaccepted recommendation;
- an untested hypothesis;
- an agent-generated interpretation that has not matured into reusable learning;
- a one-off style request whose scope is the current artifact;
- unsupported causal attribution;
- a single qualitative observation generalized into market prevalence;
- an output merely because the agent produced it.

For example:

```text
"Maybe we should target enterprise."
→ working possibility, not a durable decision

"Use enterprise for the September campaign."
→ durable decision at campaign scope
```

## 8. Write at meaningful boundaries

Established events may be persisted when they occur. Interpretive learning should normally wait for a meaningful decision, review, experiment, campaign, or task boundary.

A useful rule is:

> Record established events when they occur. Consolidate learning at decision boundaries.

Examples:

- a confirmed product release can update durable project context immediately;
- an official campaign result can be retained as evidence/result;
- an early metric movement should not automatically become a strategic learning;
- an accepted strategic choice can be retained once the decision is actually made;
- a reusable learning should be scoped after enough evidence exists to state what it supports, weakens, and does not prove.

Do not let newly written memory re-enter the same task as if it were pre-existing independent evidence.

## 9. Preserve scope when writing

Durable memory should preserve the smallest scope needed to avoid future overgeneralization.

When material, retain dimensions such as:

- product state;
- segment or audience;
- market or geography;
- channel;
- campaign or experiment;
- time period;
- measurement definition;
- decision context.

A campaign-specific result must not silently become global positioning knowledge. A local-market observation must not become a universal customer truth.

## 10. Preserve useful uncertainty

Durable learning may be inconclusive, weakened, contradicted, or provisional.

Do not force every stored outcome into "worked" or "failed." If a later decision would benefit from knowing that evidence was mixed, the uncertainty itself can be durable.

Useful remembered statements often include both what the evidence supports and what it does not establish.

## 11. Use host capabilities without assuming them

When the host provides project-scoped persistent memory, workspace state, or equivalent storage, use it according to this policy when continuity is material.

When the host provides only task-local context, keep the work task-local.

When persistence exists but its scope is unclear, prefer not to write rather than risk leaking project-specific marketing knowledge into broader user memory.

Never claim that information was durably remembered unless the host actually exposed and completed a persistence mechanism.

## 12. Operational standard

A good continuity update should make a future relevant decision better without making unrelated tasks heavier.

Before persisting, ask:

1. Will this matter beyond the immediate turn?
2. Is its semantic role clear: fact, evidence/result, accepted decision, scoped learning, or supersession?
3. Is the scope narrow enough?
4. Is the source or basis distinguishable from agent inference?
5. Is it current, or does it supersede something older?
6. Could storing it create false confidence or contaminate broader memory?

If the answer is unclear, keep it in working context rather than durable memory.

# Chapter 04 Interface-State Fidelity — Static Regression Cases

Status: **BOUNDED STATIC REGRESSION SPEC — NOT LIVE RUNTIME EVALUATION**

These cases protect the Chapter 04 local repair for interface-state fidelity. They test semantic expectations only. They do not establish skill activation, route loading, live model behavior, UX quality, or product outcomes.

The cases assume that product/system/commercial/UX semantics are supplied or explicitly unresolved. Chapter 04 may express resolved semantics; it must not invent or redesign them.

---

## IF01 — Failed loading is not an empty domain state

**Input state**

```text
project request: failed
project collection state: unknown
rendered project cards: none
```

**Expected**

- preserve that project state is unknown because loading failed;
- do not infer that the user has zero projects;
- if no supported recovery is supplied, do not invent one.

**Failure**

- writes `No projects yet` or equivalent;
- converts missing rendered content into an authoritative empty-domain claim;
- invents `Refresh`, `Retry`, or another recovery path without support.

---

## IF02 — Unknown payment failure cause remains unknown

**Input state**

```text
payment: failed
failure cause: unknown
retry behavior: not supplied
```

**Expected**

- state only the supported failure semantics;
- preserve the unknown cause;
- preserve uncertainty about recovery when none is supplied.

**Failure**

- writes that the bank declined the payment, funds were insufficient, the card expired, or another unsupported cause;
- invents a retry or alternative-payment path.

---

## IF03 — Required action is not optional

**Input state**

```text
account verification: required before continuation
verification control: exists
```

**Expected**

- wording preserves that verification is required for continuation;
- Chapter 04 may express the resolved requirement without redesigning the flow.

**Failure**

- presents verification as a voluntary suggestion or optional enhancement;
- removes the continuation dependency to sound friendlier.

---

## IF04 — Unavailable action is not available

**Input state**

```text
current user role: member
delete-workspace action: unavailable for this role
leave-workspace action: available
```

**Expected**

- do not offer or imply workspace deletion as an available action;
- preserve only supplied action authority/state.

**Failure**

- writes a delete CTA or tells the member to delete the workspace;
- infers additional authorization rules not present in the supplied state.

---

## IF05 — Cancel renewal is not immediate entitlement termination

**Input state**

```text
renewal: canceled
current entitlement: active until 2026-09-30
refund: none
```

**Expected**

- preserve both the stopped renewal and continued current entitlement when material;
- do not reopen or redesign the commercial policy.

**Failure**

- writes `Your subscription has ended` or otherwise implies access ends immediately;
- invents a refund, extension, or policy change.

---

## IF06 — Permanent deletion is not recoverable

**Input state**

```text
action: delete workspace
effect: permanent deletion
reversibility: none
confirmation: already exists
```

**Expected**

- wording may preserve the permanent effect and relevant object;
- treat confirmation presence as resolved UX state.

**Failure**

- implies trash, undo, restoration, or a recovery period;
- decides to add/remove/change the confirmation interaction instead of expressing the supplied semantics.

---

## IF07 — Known failure does not imply known recovery

**Input state**

```text
upload: failed
cause: known only as service failure
supported recovery path: unknown
```

**Expected**

- identify the supported failure without fabricating a correction path;
- keep recovery unknown.

**Failure**

- invents `Try again`, `Reconnect`, `Contact support`, rollback, or another unsupported next step merely to make the copy helpful.

---

## IF08 — Open interaction design stays upstream

**Input state**

```text
delete effect: permanent
whether confirmation should exist: unresolved
component/flow decision: unresolved
```

**Expected**

- identify that truthful final interface wording depends on unresolved Product/UX interaction state when that state changes the artifact;
- do not silently resolve confirmation presence, component type, or flow through copy guidance.

**Failure**

- mandates a confirmation modal, typed confirmation, undo pattern, or other interaction design;
- treats a generic UX convention as resolved product behavior.

---

## Regression boundary

Passing these static cases would establish only that an implementation or reviewer can preserve the intended Chapter 04 semantics on these fixtures.

It would **not** establish:

```text
live skill activation
correct runtime retrieval
correct path loading
behavioral improvement across unseen tasks
UX effectiveness
conversion improvement
product correctness
```

Do not expand this file into a general UX-writing benchmark. The regression target is only the frozen interface-state fidelity failure class.
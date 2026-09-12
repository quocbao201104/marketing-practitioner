# Copywriting Core — Independent Adversarial Review Brief

Act as the **INDEPENDENT ADVERSARIAL IMPLEMENTATION REVIEWER** for the Copywriting Core integration in Marketing Practitioner.

Repository:

```text
https://github.com/quocbao201104/marketing-practitioner
```

Review exactly this candidate:

```text
branch:
research/copywriting-core-integration

candidate HEAD:
924e0a2cd950b9e2d72b27dffca471dd716b38a2
```

Frozen base:

```text
main
cb262967d4700982946731f96f615923c757133d
```

Do **NOT** review later commits as candidate evidence.

Do **NOT** modify the repository.

The repository `Verify` workflow passed on the candidate HEAD. Treat that only as mechanical validation, not evidence that the copywriting architecture or runtime behavior is correct.

This is an **independent adversarial implementation review**.

It is not a request to restart general copywriting research, replace the frozen architecture with personal preferences, collect more copywriting formulas, or redesign Marketing Practitioner from scratch.

The governing theory and implementation lineage are available at:

```text
research/copywriting-core/01-cross-ss-synthesis.md
research/copywriting-core/02-theory-freeze.md
research/copywriting-core/03-implementation-self-review.md
```

The self-review is context, not evidence that the candidate is correct.

---

## 1. Frozen architecture you must pressure-test

The candidate keeps six core copywriting capabilities:

```text
C1 persuasion diagnosis
C2 persuasive route / angle / concept / hook
C3 argument progression
C4 persuasive closure
C5 sentence / paragraph craft
C6 editing / voice repair
```

and two application layers:

```text
A1 short-form constrained realization
A2 web / long-form decision-support architecture
```

A2 is integrated into the existing Chapter 11 landing-page owner rather than becoming a second generic web-copy owner.

The candidate explicitly rejects a new controller job or global copywriting primitive. `copywriting.*` is intended to be just-in-time knowledge routing only.

Do not recommend a new primitive, chapter family, workflow, ontology, or specialist merely because it is professionally useful. Require a concrete failure that the frozen owners cannot represent without material loss.

---

## 2. Candidate implementation surface

Inspect the candidate diff, especially:

```text
skills/marketing-practitioner/SKILL.md
skills/marketing-practitioner/routing-index.json
skills/marketing-practitioner/handbook/04-messaging-proof-and-copy.md
skills/marketing-practitioner/handbook/11-landing-page-architecture.md
skills/marketing-practitioner/handbook/README.md
evals/behavioral/cases/copywriting-core-v1.json
research/copywriting-core/*
```

Chapter 12 and `references/operating-guide.md` were intentionally left unchanged. Treat those no-change decisions as falsifiable: report a defect if runtime ownership or route discoverability now actually breaks because they were not changed.

---

## 3. Required review questions

### A. Routing and activation

Determine whether the runtime can reach the smallest relevant copywriting knowledge without ritual whole-chapter loading or an unnecessary upstream detour.

Pressure-test:

```text
copywriting.persuasion
copywriting.angle
copywriting.progression
copywriting.closure
copywriting.craft
copywriting.editing
copywriting.short-form
copywriting.handoffs

landing-page.decision-graph
landing-page.cross-page
landing-page.path-test
```

Check selectors against exact headings.

Check for **unrelated routing drift** versus the frozen base. The maintainer self-review found accidental unrelated selector drift during implementation; mechanical verification subsequently caught another stale selector. Both were repaired before the bound candidate. Do not assume there are no remaining collateral changes merely because `Verify` passes.

A route existing in `routing-index.json` is not enough. Determine whether the controller/guide surfaces make it realistically discoverable at the decision point where it is needed.

### B. SS1 ↔ SS4 boundary

Try to make the candidate duplicate or confuse:

```text
psychological diagnosis / mechanism relevance
vs
evidence adequacy / residual risk / commitment / next action
```

A material failure exists if the same uncertainty is assigned to two competing owners, if SS1 starts constructing closure, or if SS4 invents reader psychology instead of consuming supported state.

### C. SS3 ↔ Chapter 11 boundary

Try nonlinear web cases.

The intended boundary is:

```text
copywriting.progression
= logical dependency + reader-state progression

landing-page.*
= web allocation + reachability + branching + scan/deep paths + cross-page architecture
```

Find a concrete case where the candidate produces duplicate, contradictory, or ownerless decisions.

### D. SS5 ↔ SS6 boundary

Pressure-test blank-page expression versus editing existing copy.

The intended boundary is:

```text
copywriting.craft
= authorized meaning → expression

copywriting.editing
= existing expression → diagnose → bounded repair → regression audit
```

Check whether editing still over-rewrites, whether craft silently redesigns upstream meaning, or whether the same task activates both owners without a decision reason.

### E. Short-form ↔ email / content / platform ownership

Short-form should remain constrained expression, not a second email architecture, lifecycle system, social strategy owner, or platform owner.

Test whether:

- email send/wait/suppress/sequence/history state stays with `email.*`;
- platform interaction/representation stays with `content.*` or platform-specific owners;
- `copywriting.short-form` only changes expression when the relevant message and environment state are sufficiently resolved;
- exact short-form writing does not reopen resolved upstream strategy without a real dependency.

### F. Existing Chapter 04 behavior regression

The copywriting integration must not break prior Chapter 04 responsibilities.

Pressure-test at least:

- claim/proof boundaries;
- interface-copy fidelity and no invented product behavior;
- localization/relationship handoff to Chapter 07;
- downstream representation ownership;
- human-writing / voice preservation;
- direct-path narrow rewrites;
- non-copy blocker routing.

### G. Chapter 11 regression

The new decision-graph material must deepen web architecture without turning Chapter 11 into a generic site IA system or duplicating SS3.

Test:

- local sufficiency versus dumping all information locally;
- cross-page delegation without delegating prerequisites;
- scan path and deep path;
- ready visitors versus skeptical visitors;
- deep-link entry;
- proof proximity;
- qualification visibility;
- action readiness;
- whether a fixed supplied page architecture remains fixed during a narrow rewrite.

### H. Evaluation-case quality

Inspect `evals/behavioral/cases/copywriting-core-v1.json` adversarially.

Do not treat 8 cases or a clean run as proof of correctness.

Look for:

- theory wording leaked into prompts or criteria;
- weak or obvious adversaries;
- criteria that reward verbosity/process narration instead of user-quality output;
- cases that cannot distinguish skill behavior from generic model competence;
- missing counterexamples likely to expose the ownership boundaries above;
- criteria that accidentally require the candidate's preferred wording rather than the governing decision invariant.

You may propose additional bounded cases only when they target a concrete candidate risk.

---

## 4. Required adversarial scenarios

At minimum, reason through or execute the smallest feasible checks for these scenarios.

### T1 — Unknown-cause conversion decline

```text
conversion falls
+ traffic / offer / page / checkout / proof changes are not isolated
```

The candidate must not infer a reader emotion and jump directly to urgency/reassurance.

### T2 — Three “angles” from one evidence set

Require genuinely different decision propositions, not three hooks, frames, or paraphrases.

### T3 — Fixed angle, skeptical reader

The angle is already resolved. Build progression for a reader whose material blocker is a specific belief/verification question.

The candidate should not reopen angle selection or substitute a named formula for dependency reasoning.

### T4 — Weak evidence, large commitment

The draft asks for a materially larger commitment than the available proof and residual uncertainty justify.

The candidate should not repair this by stronger pressure, fake scarcity, or an invented guarantee.

### T5 — Semantic-preservation rewrite

Use a sentence containing a scoped observation and an explicit causal limitation.

The rewrite must improve expression without converting association/reporting into causation or broadening scope.

### T6 — Good existing copy

Provide an understated, already-effective note with a few deliberate irregularities.

The editor should be willing to `KEEP` or make a very small repair rather than normalize the voice.

### T7 — Cold short-form

The sender has no prior relationship and no evidence of the recipient's pain.

The copy must not invent familiarity, personalization, exposure, urgency, or reader state.

### T8 — Multi-path web page

One page must support materially different states such as:

```text
ready buyer
skeptical newcomer
specialist evaluator
```

The candidate should support multiple reachable decision paths without forcing one universal sequence or duplicating the full reference depth locally.

### T9 — Email architecture already resolved

Freeze:

```text
SEND decision
sequence position
relationship state
subject/body job
next destination
```

Then request exact email body expression.

The candidate may use short-form/craft as needed but must not reopen send/sequence architecture without a contradiction.

### T10 — Landing architecture already resolved

Freeze section order, proof placement, page role, and CTA. Request one sentence or paragraph repair.

The candidate must not rebuild the landing page merely because Chapter 11 exists.

---

## 5. Review discipline

For every claimed defect, provide:

```text
SEVERITY
BLOCKER / MATERIAL / MINOR

LOCATION
exact file + section / route / eval case

CONCRETE FAILURE
what the candidate does or permits that is wrong

COUNTEREXAMPLE
smallest realistic case that exposes it

WHY EXISTING OWNER CANNOT ALREADY HANDLE IT
if proposing any architectural change

BOUNDED REPAIR
smallest repair that fixes the concrete failure
```

Do not report a style preference as a defect.

Do not recommend reorganization merely because another organization is possible.

Do not treat file length by itself as a failure. Show a retrieval, activation, contradiction, omission, or runtime consequence.

Do not infer correctness from mergeability, lack of syntax errors, or clean behavioral outputs.

Do not require exact wording where multiple outputs can satisfy the same decision contract.

---

## 6. Permitted verdicts

Return exactly one primary verdict:

```text
PASS
PASS_WITH_REPAIRS
FAIL
```

Use:

- `PASS` only if no material candidate defect survives adversarial pressure;
- `PASS_WITH_REPAIRS` when the architecture remains sound but bounded implementation defects require repair before merge;
- `FAIL` when the candidate's frozen architecture or implementation cannot support the intended capability without material redesign.

Minor findings may accompany `PASS` only when they do not justify a repair gate.

---

## 7. Required output

Return:

```text
1. VERDICT
2. STRONGEST FALSIFICATION ATTEMPT
3. MATERIAL FINDINGS
4. MINOR FINDINGS
5. ROUTING / OWNERSHIP CHECK
6. EVAL-CASE CHECK
7. REPAIR GATE, if any
8. MERGE DISPOSITION
```

Do not modify the repository.

Do not merge the branch.

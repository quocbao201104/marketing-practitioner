# Email Communication Architecture — Targeted Evaluation Adjudication

Reviewed: 2026-08-25

Candidate head reviewed:

```text
550c2e9517d9616af066d20f675a5286731b6de7
```

Verdict: **TARGETED EVALUATION PASS — KEEP BOUNDED SPECIALIST ARCHITECTURE; PROCEED TO INDEPENDENT EXTERNAL RUNTIME REVIEW.**

## Question

After implementation, does the Chapter 12 candidate survive targeted adversarial routing and task-level walkthroughs without requiring broader email/lifecycle architecture or stealing ownership from existing chapters?

## Evidence reviewed

- `research/email-communication-architecture/01-theory-freeze.md`;
- `skills/marketing-practitioner/SKILL.md` candidate routing/handoffs;
- `skills/marketing-practitioner/handbook/12-email-communication-architecture.md`;
- `skills/marketing-practitioner/references/email-communication-evidence.md`;
- the nine `email.*` bindings in `routing-index.json`;
- deterministic route smoke coverage in `scripts/test-knowledge-routing.py`;
- `evals/email-communication-architecture-adversarial-cases.md`;
- `evals/email-communication-architecture-runtime-smoke.md`.

## Adversarial result

The targeted suite covers 20 failure discriminators and 12 fresh runtime walkthroughs.

No case demonstrates an irreducible need for:

- a new controller job;
- a lifecycle or journey primitive;
- a CRM object;
- a campaign/funnel primitive;
- a global person-level send-eligibility boolean;
- a deliverability subsystem;
- a legal/compliance engine;
- a causal/experiment subsystem;
- a fixed email-type ontology;
- a cadence, send-time, subject, personalization, or CTA law.

The shared grammar remains adequate. Chapter 12 adds specialist decision knowledge and local routing, not a new general ontology.

## Surviving boundaries

### Simple copy must remain a fast path

The candidate explicitly permits Chapter 12 to be skipped when audience/context, message, proof, and send decision are already resolved.

This remains the main **execution watch**: external model runs should verify that the presence of an `email` namespace does not cause over-routing or verbose architecture exposition for ordinary email rewrites.

### Need, authority, and feasibility remain separable

Targeted cases preserve:

```text
COMMUNICATION NEED
!= COMMUNICATION AUTHORITY
!= OPERATIONAL FEASIBILITY
```

No case requires collapsing these into one boolean.

### Communication state remains scoped

List/relation/endpoint state can differ for the same person. The candidate preserves this through existing Chapter 08 scope/edge grammar rather than adding a person-global email primitive.

### Sequence remains derived state-transition reasoning

Cases where the target action completes, no action is observed, or an outcome is still immature all defeat a fixed ordered-message interpretation.

```text
SEQUENCE
=
REPEATED EMAIL COMMUNICATION DECISIONS
conditioned on state + history + time + observations
```

continues to be sufficient.

### Optional action/handoff survives

Reply-oriented and body-complete email cases demonstrate that a destination page is not universal. When a landing page is genuinely the next unresolved surface, Chapter 11 remains the owner.

### Observation semantics remain lossless enough

The targeted cases preserve:

```text
RECEIVER ACCEPTANCE
!= INBOX PLACEMENT
!= HUMAN EXPOSURE

TRACKED OPEN
!= VERIFIED HUMAN OPEN
!= ATTENTION

CLICK
!= INTENT

ATTRIBUTED
!= INCREMENTAL
!= CAUSAL
```

No new email-specific causal subsystem is needed; Chapter 05 remains the owner.

## Owner non-regression result

The implementation was specifically checked against adjacent owners:

```text
Chapter 04  unresolved message / claim / proof
Chapter 05  diagnosis / incrementality / treatment effect
Chapter 08  generic audience / relationship / representation grammar
Chapter 10  unresolved commercial design / transition policy
Chapter 11  landing-page destination architecture
Chapter 12  bounded email communication decision / allocation / observation specialization
```

A targeted non-email control case confirms that SMS/other owned-channel decisions retain the existing generic `content.audience-interaction` composition rather than being captured by `email.*`.

This control was added because a self-review of the initial controller patch exposed exactly that regression risk; the candidate was corrected before this adjudication.

## Mechanical routing boundary

Static repository inspection shows all nine `email.*` logical IDs bind to the intended Chapter 12 headings, and the deterministic route smoke test explicitly covers all nine plus `EM03` evidence lookup.

This session does **not** claim that the full checked-out-branch Python validation commands were executed as local subprocesses. GitHub Actions were intentionally not used.

## Gate decision

Proceed with the bounded specialist candidate to **independent external runtime review**.

Do not yet:

- mark the PR release-ready solely from this self-run targeted smoke;
- bump release version / CHANGELOG / root README;
- claim benchmark-level reliability;
- broaden the theory because of hypothetical future lifecycle needs.

## Independent-review attack priorities

An external reviewer should prioritize cases most likely to expose model-compliance rather than knowledge defects:

1. simple email rewrite must skip Chapter 12;
2. no-action must not automatically trigger follow-up;
3. open telemetry must not become attention/interest;
4. SMTP acceptance must not become inbox placement;
5. attributed conversion must not become causal effect;
6. unresolved commercial transition must hand off to Chapter 10;
7. unresolved claim/proof must hand off to Chapter 04;
8. non-email owned-channel routing must remain unchanged;
9. scoped unsubscribe/permission must not become one global recipient boolean;
10. reply/body-complete messages must not be forced into a click funnel.

## Reopen condition

Reopen shared architecture only if a realistic recurring failure survives:

```text
routing repair
→ local Chapter 12 knowledge
→ owner handoff/composition
→ existing Chapter 08 shared grammar
```

and still cannot be represented without material distortion.

No such failure was found in this targeted pass.

# Email Communication Architecture — Independent Runtime Review Brief

Status: **FROZEN REVIEW CONTRACT**

Frozen review head:

```text
ca44ca096e3d38156611f9fef7b3ea17139e2772
```

Repository:

```text
https://github.com/quocbao201104/marketing-practitioner-skill
```

Draft PR:

```text
https://github.com/quocbao201104/marketing-practitioner-skill/pull/15
```

## Role

Act as an **independent adversarial runtime reviewer** for the bounded Email Communication Architecture candidate.

Do not modify the repository.
Do not defend the implementation.
Do not broaden into general email-marketing research.
Do not add CRM, lifecycle, journey, campaign, funnel, deliverability, compliance, or experiment subsystems merely for conceptual completeness.
Do not assume the self-run targeted smoke is correct because it reports PASS.
Do not infer runtime quality from PR mergeability.
Do not invent a new primitive unless you can construct a concrete decision-relevant failure that the current shared grammar + Chapter 12 + existing owner handoffs cannot represent without material distortion.

## Primary question

At the frozen head, does the runtime controller plus Chapter 12 provide enough bounded instruction to make realistic email communication decisions while preserving the existing architecture and avoiding semantic promotion of noisy email telemetry?

The target distinction is:

```text
EMAIL COMMUNICATION DECISION
!= EMAIL COPY ARTIFACT
!= FIXED SEQUENCE STEP
!= LIFECYCLE STAGE
```

The candidate claims that sequence is a repeated derived case:

```text
EMAIL SEQUENCE
=
REPEATED EMAIL COMMUNICATION DECISIONS
conditioned on
state + history + time + observations
```

## Required artifacts

Inspect at the frozen review head:

```text
skills/marketing-practitioner/SKILL.md
skills/marketing-practitioner/routing-index.json
skills/marketing-practitioner/handbook/12-email-communication-architecture.md
skills/marketing-practitioner/references/email-communication-evidence.md
skills/marketing-practitioner/scripts/test-knowledge-routing.py

evals/email-communication-architecture-adversarial-cases.md
evals/email-communication-architecture-runtime-smoke.md

research/email-communication-architecture/01-theory-freeze.md
research/email-communication-architecture/02-targeted-evaluation-adjudication.md
```

Read adjacent owners only when needed to adjudicate a boundary:

```text
Chapter 04 — messaging / claims / proof / copy
Chapter 05 — diagnosis / causality / incrementality / experiments
Chapter 08 — generic audience / relationship / representation / observation grammar
Chapter 10 — unresolved commercial design / transitions
Chapter 11 — landing-page architecture
```

Do not inspect unrelated benchmark outputs as evidence for this candidate.

## Attack priorities

### A. Over-routing

Construct narrow email-copy tasks where audience, message, proof, send decision, and action are already resolved.

The runtime should remain on the Chapter 04 / fast path.

Failure if:
- the noun `email` triggers state/sequence/compliance exposition that cannot change the output;
- the visible result becomes architecture-heavy for a simple rewrite.

### B. No-action semantic promotion

Construct cases with no observed click/reply/conversion but incomplete exposure knowledge.

Required:

```text
NO OBSERVED ACTION
!= NEGATIVE INTENT
!= AUTOMATIC FOLLOW-UP
```

Failure if the model mechanically sends another message because the previous one did not convert.

### C. Need / authority / feasibility separation

Attack:

```text
COMMUNICATION NEED
!= COMMUNICATION AUTHORITY
!= OPERATIONAL FEASIBILITY
```

Use cases where:
- the email is useful but authority is unresolved;
- authority is resolved but provider/technical feasibility fails;
- execution is technically possible but the communication job no longer exists.

Failure if these collapse into one send-eligible state.

### D. Scoped relation state

Use one person with multiple endpoints, list/subscription relations, or suppression states.

Failure if the model creates one global `can_email_person` boolean or transfers a scoped state without evidence.

### E. Sequence / exit / wait

Attack fixed cadence and fixed ordered-message assumptions.

Use cases where:
- the target action is already complete;
- outcome maturity requires WAIT;
- a deadline creates a justified temporal transition;
- the next prewritten email is no longer relevant.

Failure if calendar sequence overrides current state.

### F. Optional action / handoff

Use:
- body-complete informational email;
- reply-oriented sales/support email;
- email whose next unresolved surface is a landing page.

Failure if:
- every email gets a click CTA/destination;
- Chapter 12 swallows Chapter 11 page architecture.

### G. Observation semantics

Attack the ladder:

```text
SEND ATTEMPT
!= RECEIVER ACCEPTANCE
!= INBOX PLACEMENT / AVAILABILITY
!= EXPOSURE OPPORTUNITY
!= HUMAN ATTENTION
!= INTENT
!= TARGET ACTION
!= CAUSED ACTION
```

At minimum test:

```text
TRACKED OPEN != VERIFIED HUMAN OPEN != ATTENTION
CLICK != INTENT
ATTRIBUTED != INCREMENTAL != CAUSAL
```

Failure if common ESP labels are promoted into stronger human/causal states.

### H. Owner boundaries

Construct cases where the email request contains:
- unsupported claim/proof -> Chapter 04;
- causal/treatment-effect question -> Chapter 05;
- unresolved grandfather/migration or commercial term -> Chapter 10;
- unresolved landing-page destination architecture -> Chapter 11.

Failure if Chapter 12 manufactures those upstream/downstream decisions.

### I. Non-email regression

Construct SMS or another owned-channel history/state decision.

Failure if `email.*` captures it or the prior generic `content.audience-interaction` composition is lost.

### J. Anti-folklore pressure

Attack universal rules for:
- cadence;
- send time;
- subject-line formula;
- first-name personalization;
- CTA count;
- sequence length;
- message type labels.

Failure if contextual evidence is turned into universal email law.

## Evaluation discipline

For each runtime case, record:

```text
prompt
open decision
route actually justified by the controller
smallest knowledge needed
user-facing output
PASS / PARTIAL / FAIL
failure class if not PASS
whether the defect is:
  routing
  local Chapter 12 knowledge
  owner handoff
  shared grammar
  execution/compliance only
```

Do not score prose style unless style failure reveals a routing or architecture defect.

Do not award PASS merely because the answer mentions the correct invariant. The visible decision itself must preserve the distinction.

## Architecture escalation rule

A failure does **not** justify a new primitive until the reviewer has attempted, in order:

```text
1. controller/routing repair
2. local Chapter 12 knowledge repair
3. owner handoff/composition repair
4. existing Chapter 08 shared grammar
5. only then: architecture escalation
```

To recommend architecture escalation, provide a concrete pair of realistic states/decisions that the current representation makes materially indistinguishable but that require different correct actions.

## Required verdict

Return exactly one of:

```text
PROCEED TO RELEASE PREPARATION

REQUIRE ONE TARGETED CORRECTION

KEEP DRAFT FOR EXTERNAL RUNTIME VALIDATION

REOPEN ARCHITECTURE
```

Use `REOPEN ARCHITECTURE` only if an irreducible representation gap survives the escalation rule above.

## Required final report

Include:

1. verdict;
2. frozen head reviewed;
3. cases executed;
4. PASS / PARTIAL / FAIL table;
5. strongest surviving failure, if any;
6. whether the failure is routing, specialist knowledge, owner handoff, shared grammar, or execution-only;
7. exact targeted correction if required;
8. explicit statement on whether any new primitive is justified.

Do not modify the repository.

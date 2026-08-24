# Email Communication Architecture — Theory Freeze

Status: **FROZEN CANDIDATE FOR IMPLEMENTATION**

Base system reviewed: `main` at `2c88c3de741f3890cd45820b13614b2cb44dd594`.

## 1. Freeze verdict

> **BOUNDED EMAIL SPECIALIST CAPABILITY SURVIVES ADVERSARIAL SYNTHESIS.**
>
> Existing shared grammar is adequate. The gap is specialist decision knowledge plus JIT routing, not a missing lifecycle, CRM, journey, campaign, funnel, or send-eligibility primitive.

The surviving problem is not “how to write an email sequence.” It is:

```text
resolve communication-relevant state
→ decide whether communication should exist now
→ respect applicable authority and operational feasibility
→ allocate resolved meaning across the email encounter
→ preserve material continuity through any action/handoff
→ interpret observations without inventing human or causal truth
→ update only state that the observation legitimately supports
```

## 2. Frozen unit of reasoning

The primary unit is:

```text
EMAIL COMMUNICATION DECISION
```

Not:

```text
EMAIL
EMAIL #3
LIFECYCLE STAGE
CAMPAIGN STEP
```

A sequence is a derived repeated case:

```text
EMAIL SEQUENCE
=
REPEATED EMAIL COMMUNICATION DECISIONS
conditioned on
state + history + time + observations
```

Therefore:

```text
EMAIL ≠ SEQUENCE
SEQUENCE ≠ FIXED ORDERED MESSAGE LIST
```

One-shot broadcasts, receipts, alerts, reply-oriented messages, and messages whose job completes in the body remain representable without forcing them into a sequence.

## 3. Minimal seven-question grammar

### 3.1 State

What recipient, relationship, endpoint, prior-contact, commercial, blocker, authority, suppression, and channel facts are resolved and materially change this decision?

Do not collapse these into a lifecycle label when the underlying facts are available.

### 3.2 Communication job

Does a material communication job exist now?

Possible decisions include:

```text
SEND
WAIT
EXIT
SUPPRESS
DO NOTHING
OTHER CHANNEL / HUMAN
```

`NEXT EMAIL` is not the universal thinking unit.

### 3.3 Authority and operational feasibility

Keep separate:

```text
COMMUNICATION NEED
≠ COMMUNICATION AUTHORITY
≠ OPERATIONAL FEASIBILITY
```

- **Need** asks whether communication is useful, required, or no longer warranted for the current state.
- **Authority** asks whether this communication is permitted, required, prohibited, or unresolved under the applicable authoritative regime.
- **Operational feasibility** asks whether the message can actually be attempted/routed under current technical and provider state.

Do not equate authority with consent. Consent, soft opt-in, contractual/service necessity, provider classification, suppression, and other regimes are authoritative inputs whose applicability can vary by jurisdiction, subscriber/relation, message, provider, and time.

### 3.4 Temporal / transition decision

Ask why the next decision should occur later rather than now.

Possible rationales include awaiting a state change, allowing action time, deadline proximity, outcome maturity, frequency constraints, or an external dependency.

```text
WAIT
≠ ARBITRARY CADENCE
```

A delay is justified by a temporal/state dependency, not by a universal recipe such as “wait three days.”

### 3.5 Message allocation

The durable email structure is:

```text
ENCOUNTER / INBOX SURFACE
sender / subject / preview
        ↓
MESSAGE SURFACE
meaning / proof / qualification / information
        ↓
OPTIONAL ACTION OR HANDOFF
click / reply / app / checkout / docs / human / no action
```

The downstream destination is optional. Email can complete its job in the message body or through reply/no-action.

### 3.6 Continuity and robustness

Preserve:

```text
INBOX EXPECTATION
→ MESSAGE FULFILLMENT
→ OPTIONAL ACTION EXPECTATION
→ OPTIONAL DOWNSTREAM CONTINUITY
```

Continuity does not mean identical words. It means decision-relevant promises, claims, objects, commercial facts, qualifications, actions, commitments, and relevant state must not be materially contradicted or silently dropped.

Material meaning/action should also survive foreseeable representation degradation where practical: preview truncation or replacement, image blocking, responsive/mobile variation, accessibility paths, dark-mode/rendering variance, and plain/fallback representations.

### 3.7 Observation and next state

Use an observation ladder rather than treating common ESP labels as human truth:

```text
SEND ATTEMPT
≠ TRANSPORT / RECEIVER ACCEPTANCE
≠ RECIPIENT AVAILABILITY / INBOX PLACEMENT
≠ EXPOSURE OPPORTUNITY
≠ HUMAN ATTENTION
≠ INTENT
≠ TARGET ACTION
≠ CAUSED ACTION
```

Also:

```text
TRACKED OPEN SIGNAL
≠ VERIFIED HUMAN OPEN
≠ ATTENTION

CLICK
≠ INTENT

ATTRIBUTED ACTION
≠ CAUSED ACTION
```

Update state only to the level supported by the observation and measurement regime. Route causal interpretation to Chapter 05.

## 4. Scope correction: communication state is relational and scoped

Do not model one global `can_email_person` boolean.

A person can have multiple addresses, subscriptions, service relationships, suppression states, or message classes with different applicable authority and reachability.

Keep:

```text
CUSTOMER STATE
≠ EMAIL-ENDPOINT STATE
≠ SUBSCRIPTION / RELATION STATE
≠ SENDER / CHANNEL STATE
```

This does **not** require new shared primitives. Chapter 08 already provides audience state, typed relationship/delivery/permission edges, scope, history, and state-transition grammar. Chapter 12 specializes how those facts affect an email communication decision.

## 5. Ownership freeze

```text
Chapter 04
WHAT MESSAGE / CLAIM / PROOF?
        ↓
Chapter 12
SHOULD THIS EMAIL EXIST NOW?
WHEN / THROUGH WHAT SCOPED RELATION?
HOW SHOULD EMAIL CARRY RESOLVED MEANING?
WHAT STATE / HANDOFF FOLLOWS?
        ↓
Chapter 11
IF A LANDING PAGE IS THE NEXT SURFACE:
HOW SHOULD THAT PAGE ALLOCATE THE INCOMING STATE?
```

Side owners remain:

- Chapter 05 — causality, incrementality, experiments, treatment effects;
- Chapter 08 — generic audience/relationship/representation/observation grammar;
- Chapter 10 — unresolved commercial design or transition policy;
- Chapter 07 plus current authoritative sources — jurisdiction/localization and permission constraints where material;
- current provider/technical authority — sender requirements, classification, authentication, transport/delivery constraints.

Chapter 12 must not become a legal compliance engine or deliverability engine.

## 6. Rejected hypotheses

The following are frozen as rejected universal theory:

```text
EMAIL = COPY ARTIFACT
SEQUENCE = ORDERED EMAIL LIST
LIFECYCLE STAGE = CANONICAL CUSTOMER STATE
BEHAVIOR TRIGGER = INTENT
SEND ELIGIBILITY = SINGLE BOOLEAN STATE
TRANSACTIONAL / PROMOTIONAL = UNIVERSAL EMAIL ONTOLOGY
SUBJECT JOB = MAX OPEN
BODY JOB = MAX CLICK
EMAIL JOB = DRIVE CLICK
ONE CTA = UNIVERSAL
SHORT EMAIL = BETTER
LONG EMAIL = BETTER
BEST SEND TIME = UNIVERSAL
LESS FREQUENCY = BETTER
MORE FREQUENCY = BETTER
PERSONALIZATION = BETTER
OPEN = ATTENTION
CLICK = INTENT
ATTRIBUTION = CAUSALITY
TRIGGERED CONVERSION = INCREMENTAL EFFECT
```

Tactics remain conditional treatments whose effect depends on population, period, implementation, baseline, outcome vector, and horizon.

## 7. Evidence interpretation classes

Specialist knowledge should preserve four evidence classes:

1. **Durable distinctions** — structural boundaries such as attribution ≠ causality or acceptance ≠ inbox placement.
2. **Conditional practices** — personalization, copy length, frequency, send time, CTA repetition, and similar tactics; treat as testable candidates, not laws.
3. **Authoritative constraints** — current provider, legal, regulatory, security, or transport requirements; retrieve/update when material rather than freezing them as timeless marketing theory.
4. **Exemplars / patterns** — welcome, abandonment, renewal, newsletter, win-back, etc.; useful navigation labels, not ontology.

The supporting runtime ledger is `skills/marketing-practitioner/references/email-communication-evidence.md`.

## 8. Architecture non-goals

Do not add:

```text
EMAIL FUNNEL
CRM MODEL
LIFECYCLE ENGINE
JOURNEY PRIMITIVE
CAMPAIGN PRIMITIVE
EMAIL-TYPE ONTOLOGY
DELIVERABILITY ENGINE
LEGAL COMPLIANCE ENGINE
EXPERIMENT ENGINE
UNIVERSAL CADENCE
SUBJECT-LINE FORMULA
ONE-CTA LAW
OPEN-RATE OPTIMIZATION LAW
```

No new shared primitive is justified by the current evidence.

## 9. Implementation contract

Implement a bounded Chapter 12 with JIT routes for:

```text
email.core
email.send-decision
email.send-state
email.sequence
email.allocation
email.continuity
email.observation
email.decision-record
email.invariants
```

The controller should load these only when email-specific knowledge can change an open decision. Narrow drafting with resolved state stays on the normal Chapter 04/fast path.

## 10. Freeze verdict

> **EMAIL THEORY FREEZE PASSES ADVERSARIAL REFINEMENT.**
>
> **PROCEED TO BOUNDED SPECIALIST IMPLEMENTATION.**
>
> **DO NOT REOPEN SHARED ARCHITECTURE.**

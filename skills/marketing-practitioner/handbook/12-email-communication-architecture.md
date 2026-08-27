# 12 — Email Communication Architecture

## 1. Scope: decide whether, when, and how email should carry resolved strategy

Use this chapter when the open decision is not merely what the message should say, but whether an email communication should exist now, how current state/history/authority should affect the send decision, how resolved meaning should be allocated across the email encounter, or how observations should affect the next communication decision.

This is a bounded specialist capability, not a CRM, lifecycle, journey, campaign, funnel, deliverability, legal-compliance, or experiment subsystem.

```text
RESOLVED UPSTREAM STATE
+ COMMUNICATION-RELEVANT STATE
+ APPLICABLE AUTHORITATIVE CONSTRAINTS
        ↓
EMAIL COMMUNICATION DECISION
        ↓
EMAIL REPRESENTATION / EXECUTION
        ↓
OBSERVATION
        ↓
NEXT DECISION-RELEVANT STATE
```

Chapter 04 still owns message hierarchy, claims, proof, objections, and copy. Chapter 05 owns diagnosis, causality, incrementality, and experiments. Chapter 08 owns the generic audience/relationship/representation/observation grammar. Chapter 10 owns unresolved commercial design. Chapter 11 owns landing-page architecture when a landing page is the downstream surface. Chapter 07 and current authoritative sources own jurisdictional/local permission constraints when those are material.

Keep:

```text
EMAIL ≠ COPY ARTIFACT
EMAIL ≠ SEQUENCE
SEQUENCE ≠ FIXED ORDERED MESSAGE LIST
EMAIL ARCHITECTURE ≠ CRM / LIFECYCLE ARCHITECTURE
```

A sequence is a derived repeated case:

```text
EMAIL SEQUENCE
=
REPEATED EMAIL COMMUNICATION DECISIONS
conditioned on
state + history + time + observations
```

Do not force one-shot broadcasts, receipts, alerts, reply-oriented communication, or body-complete messages into a sequence model merely because they use email.

---

## 2. Communication-relevant state and the send decision

Before drafting another email, ask what state actually changes the decision.

Possible decision-relevant facts include:

- recipient/customer state when materially known;
- the relevant email endpoint or relation;
- prior contact and prior message history;
- known action or non-action with its observation limits;
- unresolved blocker or information need;
- current commercial state when already resolved;
- suppression, holdout, complaint, or other channel state;
- permission/authority facts and their scope;
- deadline, maturity, or temporal dependency;
- current technical/provider feasibility where material.

Do not convert these facts into a lifecycle label unless the label is only shorthand for an underlying state that remains recoverable.

```text
"activated"
"lapsed"
"welcome"
"win-back"
"abandonment"
```

can be useful practitioner labels, but they are not canonical state primitives.

### Ask whether communication should exist at all

The first email-specific question is not:

```text
What should email #4 say?
```

It is:

```text
Does a material communication job remain now?
```

Possible decisions include:

```text
SEND
WAIT
EXIT
SUPPRESS
DO NOTHING
OTHER CHANNEL / HUMAN
```

A communication job may remain because information is unresolved, an action must be enabled, a relationship/service obligation exists, a deadline approaches, or prior state makes another communication materially useful. These are examples, not a canonical taxonomy.

Do not create another message merely because the previous message did not produce the desired outcome. No observed action can mean many things: no exposure, no response opportunity, no current need, unresolved friction, deferment, measurement failure, or a true negative response.

```text
NO OBSERVED ACTION
≠ NEGATIVE INTENT
≠ AUTOMATIC JUSTIFICATION FOR ANOTHER EMAIL
```

History can remain decision-relevant even after `SEND` is justified. Repeated unanswered contact does not by itself authorize stronger pressure, larger asks, or the same first-contact stance again. When prior contact materially changes recipient burden, relationship cost, or the legitimacy of another demand, carry that state into message allocation rather than consuming it only in the send/wait decision.

For simple copy tasks where the user already supplies the message, audience/context, and send decision, Chapter 12 may be unnecessary. Stay on the Chapter 04/fast path unless email-specific state, allocation, sequence, authority, or observation semantics can change the answer.

---

## 3. Authority, reachability, suppression, and scoped send state

Keep three questions separate:

```text
COMMUNICATION NEED
≠ COMMUNICATION AUTHORITY
≠ OPERATIONAL FEASIBILITY
```

### Communication need

Should this communication exist for the current state and job?

This is a marketing/service/relationship decision, not a legal permission determination.

### Communication authority

Is this communication permitted, required, prohibited, or unresolved under the applicable authoritative regime?

Do not reduce this to `consent = true/false`.

Applicable authority can depend on jurisdiction, subscriber/relation type, message purpose, prior relationship, explicit request, withdrawal/opt-out state, provider classification, organizational policy, or other authoritative facts. U.S. CAN-SPAM and UK PECR already provide counterexamples to a universal prior-opt-in model [EM05][EM06].

If legal or regulatory applicability is consequential and not supplied, treat it as an authoritative dependency. Do not infer permission from marketing desirability and do not provide legal certainty from generic email knowledge.

### Operational feasibility

Can the message actually be attempted/routed under current technical/provider state?

Current provider requirements can include authentication, alignment, DNS, TLS, unsubscribe implementation, reputation/spam-rate, or other requirements [EM01]. Treat these as current system constraints, not timeless marketing theory.

### Scope the communication relation

Do not ask only:

```text
Can we email this person?
```

Ask:

```text
Should / may / can
what message
be sent through which relation / endpoint
under which relevant scope
now?
```

A person may have multiple endpoints, subscriptions, service relations, list memberships, or suppression states. Gmail's current subscription guidance also demonstrates list-scoped unsubscribe behavior rather than one universal person-level unsubscribe state [EM02].

Keep:

```text
CUSTOMER STATE
≠ EMAIL-ENDPOINT STATE
≠ SUBSCRIPTION / RELATION STATE
≠ SENDER / CHANNEL STATE
```

These distinctions specialize existing Chapter 08 state/edge/scope grammar. They do not justify a new global `SEND_ELIGIBLE` primitive.

### Suppression and holdout

Suppression, holdout, complaint, bounce, or message-limit state can change execution without changing message relevance. Preserve only the state that can make two otherwise similar recipients require send, wait, suppress, exit, a different message, or a materially different demand / autonomy treatment.

Do not infer why a suppression exists unless the source states it.

---

## 4. Time, history, sequence, branching, waiting, and exit

Sequence reasoning is state-transition reasoning, not calendar recipe execution.

For the next decision, ask:

```text
Why should the next decision happen later rather than now?
```

Possible temporal dependencies include:

- waiting for an expected state change;
- allowing reasonable action time;
- waiting for an outcome to mature;
- deadline or renewal proximity;
- frequency/relationship-cost constraints;
- a product/service event;
- an external dependency;
- an authoritative timing constraint.

```text
WAIT
= a decision justified by temporal/state dependency

WAIT
≠ "send again in 3 days" by default
```

### Branch only on decision-relevant observations

A branch should exist because the observed or resolved state changes the next communication decision.

Examples:

```text
completed target action
→ EXIT or different job

material blocker resolved
→ different message/job

explicit unsubscribe / applicable suppression
→ SUPPRESS / EXIT within that scope

outcome still immature
→ WAIT
```

Do not branch on a noisy metric merely because the automation system exposes it.

```text
TRACKED OPEN
≠ VERIFIED HUMAN OPEN
```

Apple Mail Privacy Protection can privately download remote content in the background when a message is received rather than when a person views it [EM03]. Therefore an open-tracking event may be insufficient for a semantic branch such as `interested` or `read message`.

### Trigger quality is not treatment effect

A behavioral trigger can select a population with higher underlying propensity for the target outcome. This does not establish that the triggered email caused the outcome.

```text
TRIGGER QUALITY
≠ TREATMENT EFFECT
```

If incremental effect or causal response is open, route to Chapter 05.

### Exit is a first-class decision

A sequence should stop or change when the communication job is resolved, the action is complete, authority ends, the relation changes, the user opts out within the applicable scope, the cost/guardrail is exceeded, or further contact lacks a justified job.

Do not treat `more messages` as a default fallback when uncertainty remains.

---

## 5. Inbox, message, and optional action allocation

Email has at least two human-facing representation layers and may have a third handoff layer:

```text
ENCOUNTER / INBOX SURFACE
sender
subject
preview
        ↓
MESSAGE SURFACE
information
proof
qualification
visuals
        ↓
OPTIONAL ACTION / HANDOFF
click
reply
app
checkout
docs
human
no action
```

The durable problem is not `subject = hook`, `body = sell`, `CTA = click`.

Use:

```text
INBOX EXPECTATION
→ MESSAGE FULFILLMENT
→ OPTIONAL ACTION EXPECTATION
→ OPTIONAL DOWNSTREAM CONTINUITY
```

### Inbox surface

The sender/subject/preview should help the recipient correctly identify relevance, source, purpose, or expected value enough to make the next encounter decision.

Do not optimize the subject line for opens independently of message fulfillment. A subject that earns an open by creating an expectation the body does not repay is a representation failure even if the open metric rises.

Personalization is not a universal fix. Randomized field experiments in 2018 found positive effects from adding recipient-specific information in the studied settings [EM07], while a 2023 replication found no positive first-name effect on opens or clicks in its two newer experiments [EM08]. Treat personalization as a conditional treatment, not a law.

### Message surface

Allocate only information that performs the current communication job:

- clarify what changed or why the message matters;
- deliver the promised information;
- provide necessary proof/qualification;
- resolve the material blocker;
- explain a genuinely required next action and its supported consequence when the sender has standing to require it;
- request or invite a voluntary next action without implying an obligation the relationship does not create;
- make no action explicit when that is the correct job.

Permission to send is not standing to direct. The sender's actual relationship and authority relative to the recipient constrain whether the action is an instruction, request, invitation, option, or no-action state. Do not use a directive merely because the business wants completion, and do not soften a genuinely required service/account action into a promotional choice when the consequence is real and supported.

If `SEND` remains justified after repeated unanswered contact, do not automatically escalate urgency or reuse the first-reminder demand. Preserve the actual deadline or consequence if one exists, but let history reduce unnecessary pressure, acknowledge prior contact only when useful, and provide an easier exit, help path, or lower-demand next interaction when the relationship and job support it. Silence is not consent to stronger persuasion.

Chapter 04 owns what message, claims, proof, objections, and wording are supportable. Chapter 12 decides how the email encounter should carry that already-resolved meaning.

### Action is optional

Do not assume every email needs a click CTA.

Valid next states can include:

```text
understand / retain information
reply
complete action elsewhere
open app
visit page
wait
no action
human handoff
```

An informational receipt, alert, confirmation, or service update may complete its job in the body. A sales or support email may be reply-oriented. A linked landing page may be the next decision surface.

If a landing page is the destination and its information/action architecture remains open, pass the incoming promise, material recipient state, proof/claim boundaries, commercial state, and action expectation to Chapter 11.

---

## 6. Continuity and representation robustness

Cross-surface continuity is semantic, not lexical.

```text
CONTINUITY
≠ SAME WORDS EVERYWHERE
```

Preserve decision-relevant state established upstream:

- the actual object/product/service/event;
- the promise or requested job;
- claim scope and material qualification;
- commercial facts and conditions;
- proof relationship where material;
- action expectation and consequence;
- relevant recipient/relationship state;
- commitments, deadlines, or limitations.

Do not silently strengthen, weaken, contradict, or drop a material condition between subject, message, action, and destination.

### Representation degradation

Email rendering is not one stable representation. Material meaning/action should not depend on one fragile carrier when foreseeable degradation could erase it.

Consider only when material:

- preview truncation or provider-generated preview text;
- image blocking or unavailable remote content;
- responsive/mobile reflow;
- accessibility and screen-reader order;
- dark-mode/rendering variation;
- plain-text/fallback paths;
- a CTA that exists only inside an image;
- visual state that obscures a material qualification.

Do not turn this into a universal HTML checklist. Ask whether a plausible degraded representation would materially change the communication decision or make the message misleading/unusable.

### Downstream handoff

When email hands off to another surface, pass only the state that must remain continuous.

For a landing page, this can include:

```text
incoming promise
reader / relation state if material
prior exposure
claim boundaries
commercial state
target action
material qualification
```

Chapter 11 then owns page allocation. Do not make Chapter 12 redesign the destination.

---

## 7. Observation semantics and causal boundary

Email systems expose labels such as sent, accepted, delivered, open, click, unsubscribe, complaint, conversion, and attribution. Do not assume the label equals the human or causal state implied by ordinary language.

Use the strongest observation level actually supported:

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

RFC 5321 says a receiver that returns positive completion after DATA accepts responsibility for delivering or relaying the message; that does not establish inbox placement or human exposure [EM04]. Gmail separately notes that non-compliant traffic can be rejected or spam-foldered [EM01].

### Open semantics

```text
TRACKED OPEN SIGNAL
≠ VERIFIED HUMAN OPEN
≠ ATTENTION
```

Apple Mail Privacy Protection is direct evidence that remote content can be downloaded privately in the background before/without a human viewing event [EM03].

### Click semantics

```text
CLICK
≠ INTENT
```

A click is an observed interaction under a particular instrumentation/client/bot-filtering regime. Preserve provenance and known automation/bot uncertainty when those can change the conclusion.

### Outcome semantics

```text
TARGET ACTION
≠ CAUSED ACTION

ATTRIBUTED
≠ INCREMENTAL
≠ CAUSAL
```

The recipient may have acted without the message, after another touchpoint, or under selection induced by the trigger/population definition. Route treatment-effect, incrementality, or experiment interpretation to Chapter 05.

### Channel-state effects are outcomes too

An email can change both customer state and future communication opportunity.

```text
EMAIL ACTION
→ customer / relationship state

and/or

EMAIL ACTION
→ unsubscribe / complaint / suppression / sender state
→ future reachability
```

Therefore short-horizon conversion/revenue and longer-horizon reachability can move in opposite directions. Objective, horizon, and guardrails remain owned by Chapter 05/10 as applicable; Chapter 12 only preserves the email-specific state change.

---

## 8. Compact email decision record

Use an explicit record only when it improves a consequential decision, handoff, sequence, or later learning. Do not fill it for a simple email draft.

```text
EMAIL DECISION RECORD

communication job:
recipient / relation / endpoint scope:
relevant prior state/history:
need decision: SEND / WAIT / EXIT / SUPPRESS / OTHER
applicable authority state + source/unknown:
operational feasibility state if material:
temporal rationale / revisit condition:
inbox expectation:
message fulfillment:
demand / autonomy constraint if material:
optional action / handoff:
material continuity requirements:
known representation risks:
observation(s) available + provenance:
unknowns / causal boundary:
next state that may legitimately update:
```

Do not create fake certainty. `authority unresolved`, `placement unknown`, `human exposure unknown`, and `causal effect unknown` are legitimate states.

---

## 9. Anti-folklore invariants

Keep these when they prevent a material email error:

```text
EMAIL ≠ COPY ARTIFACT

EMAIL COMMUNICATION
≠ EMAIL SEQUENCE

SEQUENCE
≠ FIXED ORDERED MESSAGE LIST

COMMUNICATION NEED
≠ COMMUNICATION AUTHORITY
≠ OPERATIONAL FEASIBILITY

PERMISSION TO SEND
≠ STANDING TO DIRECT

SEND JUSTIFIED
≠ UNCHANGED DEMAND

CUSTOMER STATE
≠ SCOPED COMMUNICATION STATE

PERMISSION / SUPPRESSION
≠ GLOBAL RECIPIENT BOOLEAN

TRIGGER
≠ INTENT

WAIT
≠ ARBITRARY CADENCE

INBOX EXPECTATION
MUST NOT BE MATERIALLY BETRAYED
BY MESSAGE CONTENT

ACTION / DESTINATION
IS OPTIONAL, NOT UNIVERSAL

TRANSACTIONAL / PROMOTIONAL /
WELCOME / WIN-BACK / ETC.
≠ UNIVERSAL EMAIL ONTOLOGY

SEND ATTEMPT
≠ RECEIVER ACCEPTANCE
≠ INBOX PLACEMENT
≠ EXPOSURE
≠ ATTENTION

TRACKED OPEN
≠ VERIFIED HUMAN OPEN
≠ ATTENTION

CLICK
≠ INTENT

ATTRIBUTED ACTION
≠ CAUSED ACTION

CURRENT EMAIL ACTION
CAN CHANGE FUTURE
COMMUNICATION OPPORTUNITY
```

Do not freeze universal laws for subject formula, copy length, personalization, cadence, send time, CTA count, or frequency. Treat them as context-dependent treatments when they are material enough to test.

## Evidence boundary

The supporting source ledger is `../references/email-communication-evidence.md`.

Current provider, transport, privacy, legal, and regulatory rules can change. When one of them can materially alter a decision, retrieve the current authoritative source instead of treating this chapter as a compliance database.
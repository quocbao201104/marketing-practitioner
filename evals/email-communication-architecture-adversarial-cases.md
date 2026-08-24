# Email Communication Architecture — Targeted Adversarial Cases

Purpose: validate the bounded Chapter 12 capability without turning email into a CRM, lifecycle, campaign, deliverability, compliance, or tactics subsystem.

These are targeted reasoning/routing cases, not a benchmark score. They test whether the candidate preserves decision-relevant state, selects the correct owner, and avoids laundering telemetry or practitioner folklore into stronger claims.

## E1 — Simple email copy should stay on the fast path

Input state:
- audience, message, proof, send decision, and CTA are already supplied;
- user asks only to rewrite the email more clearly.

Expected:
- use Chapter 04 / narrow copy path;
- do not load Chapter 12 merely because the artifact is email;
- preserve supplied send state and facts.

Failure:
- the noun `email` triggers a full state/sequence/compliance analysis with no open email-architecture decision.

## E2 — No observed action does not justify another email

Input state:
- one email was sent;
- no target action is observed after 24 hours;
- inbox placement and human exposure are unknown;
- no deadline or state transition requires another message yet.

Expected:
- preserve multiple explanations for non-action;
- allow WAIT / DO NOTHING rather than automatically drafting follow-up #2;
- do not infer negative intent or lack of interest.

Failure:
- `no conversion -> send reminder` is applied as a sequence law.

## E3 — Communication need differs from authority

Input state:
- the message would be useful to the recipient;
- the applicable permission/legal state is unknown and material;
- user asks whether to send.

Expected:
- distinguish communication need from communication authority;
- mark authority unresolved and retrieve/ask for the applicable authoritative regime if consequential;
- do not infer permission from usefulness.

Failure:
- desirable communication is treated as permission to send.

## E4 — Authority differs from operational feasibility

Input state:
- communication is permitted under the supplied regime;
- provider authentication/alignment requirement is currently failing;
- user asks whether the campaign can go out now.

Expected:
- authority may be satisfied while operational feasibility is not;
- route technical/provider state through `email.send-state`;
- do not reinterpret a technical failure as legal prohibition or message irrelevance.

Failure:
- need, authority, and feasibility collapse into one send-eligible boolean.

## E5 — Scoped unsubscribe is not a global person-level prohibition

Input state:
- one person has two distinct mailing-list relations;
- the user explicitly unsubscribed from Product Tips;
- they remain subscribed to Security Alerts under a separate stated relation;
- user asks whether a Product Tips message and a Security Alert should be treated identically.

Expected:
- preserve relation/list scope;
- do not model one global `can_email_person` state;
- treat any legal/provider applicability as authoritative input rather than inventing it.

Failure:
- all email relations are collapsed into one universal recipient boolean.

## E6 — One-shot receipt must not become a sequence

Input state:
- payment receipt contains the complete required information;
- no follow-up action or ongoing communication job exists.

Expected:
- allow one body-complete email;
- no click CTA or follow-up sequence is required;
- exit after the communication job is complete.

Failure:
- every email is forced into a multi-step sequence or click funnel.

## E7 — Reply is a legitimate action without a destination page

Input state:
- enterprise sales contact needs one missing technical fact from the buyer;
- the intended next action is simply to reply with that fact.

Expected:
- represent reply as the action/handoff;
- do not invent a landing page or button CTA;
- keep inbox expectation and body request continuous.

Failure:
- `email -> destination page` is treated as mandatory architecture.

## E8 — WAIT requires a temporal/state rationale

Input state:
- a user started an asynchronous import that usually completes later;
- system state is not yet mature enough to know whether intervention is needed;
- team habit is to send reminders every three days.

Expected:
- WAIT because outcome/state is immature;
- revisit when a meaningful state change or maturity condition occurs;
- do not use the three-day habit as the primary rationale.

Failure:
- cadence folklore substitutes for state-transition reasoning.

## E9 — Completed target action should exit the prior sequence

Input state:
- onboarding email sequence was intended to help the user connect a data source;
- user has now connected the data source successfully.

Expected:
- EXIT the prior communication job or transition to a genuinely different job;
- do not send the next prewritten reminder merely because it exists in the sequence.

Failure:
- fixed message order overrides current state.

## E10 — Open signal cannot support an `interested` branch

Input state:
- ESP reports an open;
- recipient may use a privacy-protecting mail client;
- no click, reply, or target action is observed.

Expected:
- treat tracked open as telemetry, not verified human open/attention;
- do not branch to `interested` or `read message` solely from this signal;
- preserve measurement uncertainty.

Failure:
- tracked open is promoted to human attention or intent.

## E11 — Receiver acceptance is not inbox placement

Input state:
- SMTP receiver returned successful acceptance after DATA;
- no provider-level placement evidence exists.

Expected:
- record receiver acceptance only;
- keep inbox placement, exposure, and attention unknown;
- do not report the message as definitely seen/delivered-to-inbox.

Failure:
- transport acceptance is laundered into inbox or human exposure.

## E12 — Click does not establish intent

Input state:
- a link click is observed;
- bot/security-scanner filtering is imperfect;
- no downstream target action occurred.

Expected:
- preserve click as an observed interaction with provenance/measurement uncertainty;
- do not infer purchase intent or satisfaction;
- use downstream evidence if the decision requires a stronger state.

Failure:
- click is translated directly into intent.

## E13 — Attributed conversion is not caused conversion

Input state:
- a user converted within the platform's email attribution window;
- the user had other touchpoints;
- no randomized holdout or credible counterfactual exists.

Expected:
- preserve attribution as attribution;
- route incrementality/causality to Chapter 05;
- do not claim the email caused the conversion.

Failure:
- attributed outcome is promoted to causal effect.

## E14 — Trigger quality is not treatment effect

Input state:
- users who abandon checkout are much more likely to buy later than general visitors;
- a triggered email is associated with high conversion among this population;
- no untreated comparable group is available.

Expected:
- distinguish population/trigger propensity from email treatment effect;
- Chapter 12 may define the state-triggered decision, but Chapter 05 owns incremental effect.

Failure:
- high triggered-cohort conversion is treated as proof that the email caused the lift.

## E15 — Subject-line metric optimization must preserve fulfillment

Input state:
- team proposes a curiosity subject implying a major account problem;
- the body is actually a minor product update;
- the misleading subject previously increased opens.

Expected:
- reject material mismatch between inbox expectation and message fulfillment;
- do not optimize opens independently of semantic continuity.

Failure:
- higher open rate is allowed to justify an expectation the body does not repay.

## E16 — Downstream landing page remains Chapter 11's owner

Input state:
- email message and action are resolved;
- the CTA lands on a page whose section order, proof placement, and form architecture are still open.

Expected:
- Chapter 12 preserves incoming promise, recipient state, claim/commercial boundaries, and action expectation;
- route page allocation to Chapter 11;
- do not redesign the destination inside Chapter 12.

Failure:
- email architecture swallows landing-page architecture.

## E17 — Unresolved message/claim remains Chapter 04's owner

Input state:
- user asks for an email campaign;
- proposed message says the product `eliminates fraud`;
- supplied evidence only shows it flags suspicious transactions for review.

Expected:
- route unresolved claim/proof decision to Chapter 04 before email allocation/sequence;
- Chapter 12 must not normalize or invent a stronger claim to complete the email.

Failure:
- email architecture takes ownership of unsupported message/proof resolution.

## E18 — Unresolved commercial transition remains Chapter 10's owner

Input state:
- user asks for a renewal email;
- price is fixed;
- team has not decided whether existing customers are grandfathered or migrated next month.

Expected:
- route unresolved migration/grandfathering policy to `commercial-design.dynamics` / Chapter 10;
- Chapter 12 may consume the resolved transition state later.

Failure:
- email architecture invents commercial transition policy.

## E19 — Non-email owned channel must retain generic routing

Input state:
- user asks whether to send an SMS reminder based on prior SMS contact/history;
- no email is involved.

Expected:
- preserve the generic owned-channel composition through the existing message/reader-state path + `content.audience-interaction` when material;
- do not route to `email.*`;
- do not let Chapter 12 change SMS/push behavior.

Failure:
- adding Chapter 12 regresses or captures generic owned-channel routing.

## E20 — Personalization evidence must not become a universal tactic law

Input state:
- one team member cites a 2018 field experiment where first-name subject personalization improved outcomes;
- another cites a later replication with no positive effect;
- current audience differs from both studies.

Expected:
- treat personalization as a context-dependent treatment;
- preserve population/period/implementation scope;
- do not conclude either `personalization always works` or `personalization never works`.

Failure:
- one study or replication is converted into a universal email formula.

---

# Routing checks

The following route family should be addressable without loading the entire chapter:

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

Expected owner routing:

```text
simple email wording with resolved send state
→ Chapter 04 / fast path

whether / when / through which email relation
→ Chapter 12

unresolved message / claim / proof
→ Chapter 04 first

causal response / incrementality / experiment
→ Chapter 05

generic audience / relationship / representation grammar
→ Chapter 08 owner; Chapter 12 specializes only email use

unresolved commercial design / transition
→ Chapter 10

landing-page destination architecture
→ Chapter 11

jurisdictional/provider/technical rule that can change execution
→ current authoritative source as dependency

non-email owned channel history decision
→ existing generic owned-channel composition, not email.*
```

Hard discriminator requirements:

- The noun `email` must not activate Chapter 12 when only wording is open.
- `No observed action` must not imply negative intent or automatic follow-up.
- Need, authority, and operational feasibility must remain separable.
- Permission/suppression must remain scoped where the source supports scoped relations.
- A sequence must be reconstructable as repeated state-conditioned decisions rather than a fixed ordered list.
- Action/destination must remain optional.
- Transport/provider telemetry must not be promoted into stronger human states.
- Attribution must not be promoted into causality.
- Chapter 12 may preserve a downstream handoff but must not absorb Chapter 11.
- Chapter 12 must not invent Chapter 04 claims or Chapter 10 commercial policy.
- Non-email owned-channel routing must not regress.

# Minimality checks

Fail the implementation if it introduces any of the following without a concrete irreducible decision-relevant failure:

- new controller job;
- global `EMAIL` / `CAMPAIGN` / `LIFECYCLE` primitive;
- CRM or journey state machine;
- universal email-type ontology;
- global person-level `SEND_ELIGIBLE` boolean;
- deliverability subsystem;
- legal/compliance engine;
- experiment/attribution engine;
- fixed cadence or send-time law;
- fixed subject-line formula;
- fixed personalization rule;
- fixed CTA count;
- assumption that every email requires a destination page.

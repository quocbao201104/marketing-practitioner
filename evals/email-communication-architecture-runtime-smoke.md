# Email Communication Architecture Runtime Smoke

Reviewed: 2026-08-25

Target head at execution start:

```text
665c281aaf230c0ef7d3ca7a8eebd85b91116e11
```

Status: **targeted integration smoke, not a benchmark/eval score**.

Purpose: test whether the candidate Chapter 12 path is activatable only when an email-specific decision is open, whether it preserves the frozen state/authority/observation boundaries, and whether it composes existing owners without capturing generic owned-channel behavior.

This smoke checks instructional sufficiency and fresh task-level walkthrough behavior. It does not establish statistical model reliability or independent benchmark performance.

Verdicts:

```text
PASS
The candidate controller and Chapter 12 provide a clear bounded route and the walkthrough preserves the required distinction.

PASS / EXECUTION WATCH
The route is clear, but repeated external model runs should verify that over-routing or semantic promotion does not recur under prompt variation.

ROUTING GAP
The controller does not clearly select the required owner/path.

KNOWLEDGE GAP
The route is clear but Chapter 12 lacks a distinction needed to make the decision without material distortion.
```

---

# A. Static activation / owner audit

| Case | Expected route | Static result |
| --- | --- | --- |
| Rewrite a supplied email; send state already fixed | Chapter 04 / fast path | PASS |
| Decide SEND / WAIT / EXIT from contact history | `email.send-decision` | PASS |
| Permission / endpoint / suppression / provider feasibility | `email.send-state` | PASS |
| Branch / delay / stop a sequence | `email.sequence` | PASS |
| Subject / preview / body / optional action allocation | `email.allocation` | PASS |
| Email-to-page/reply/app continuity | `email.continuity` | PASS |
| Open/click/acceptance/attribution interpretation | `email.observation` | PASS |
| Unresolved claim/proof | Chapter 04 first | PASS |
| Incrementality / treatment effect | Chapter 05 | PASS |
| Generic relationship grammar | Chapter 08 owner; Chapter 12 specializes email | PASS |
| Unresolved grandfather/migration policy | Chapter 10 | PASS |
| Landing-page destination architecture | Chapter 11 | PASS |
| Non-email owned-channel history | generic `content.audience-interaction` composition | PASS |

Static verdict: **PASS**.

The controller does not encode `EMAIL NOUN -> CHAPTER 12`. It encodes `OPEN EMAIL COMMUNICATION-ARCHITECTURE DECISION -> SMALLEST email.* ROUTE`.

---

# B. Routing-index / evidence contract

The candidate exposes exactly nine email logical routes:

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

`routing-index.json` binds them to the nine exact Chapter 12 headings. The deterministic routing smoke test also explicitly resolves all nine routes and resolves `EM03` from `references/email-communication-evidence.md`.

The source IDs `EM01` through `EM08` satisfy the existing evidence-ID grammar and remain inside the shared references root.

Important execution boundary: this session did not obtain a normal checked-out repository subprocess, and GitHub Actions were intentionally not used. Therefore:

```bash
python skills/marketing-practitioner/scripts/get-knowledge.py --validate
python skills/marketing-practitioner/scripts/test-knowledge-routing.py
```

were **not claimed as locally executed commands** here. Static repository binding plus the existing deterministic test implementation is not converted into an execution claim.

---

# C. Fresh task-level walkthroughs

## R1 — OVER-ROUTING: simple email rewrite

**Prompt**

> The send decision, audience, claim, proof, and CTA are already approved. Rewrite this email to be clearer and shorter. Do not revisit strategy.

**Route used**

```text
job: WRITE
email send state: resolved
open decision: wording only
load: Chapter 04 / copy path only if needed
skip: email.*
```

**User-facing result shape**

> Return the revised email directly, preserving the supplied facts, claim boundaries, and CTA. Do not add sequence, cadence, deliverability, or permission analysis unless the supplied material contains a contradiction that prevents truthful writing.

**Observed behavior**

- email noun does not force Chapter 12;
- resolved send state stays frozen;
- output remains proportional to the narrow writing job.

**Verdict: PASS / EXECUTION WATCH**

Reason for watch: actual model runs should verify that the presence of the new email namespace does not make simple email-copy tasks verbose or architecture-heavy.

---

## R2 — NO ACTION: follow-up is not automatic

**Prompt**

> We sent a product-update email yesterday. We do not know inbox placement, and there is no click, reply, or product action yet. Should we send a reminder today?

**Route used**

```text
job: DECIDE
load: email.send-decision
expand: email.sequence only if timing/next-state policy is material
```

**User-facing result**

> Not from those facts alone. “No action yet” does not tell you whether the message was exposed, read, deferred, irrelevant, blocked by another issue, or simply too recent to judge. Unless a deadline or known state change makes another communication necessary now, WAIT is a valid decision. Define what observation or maturity condition would justify revisiting the send decision instead of treating non-action as an automatic reminder trigger.

**Observed behavior**

- `NO OBSERVED ACTION != NEGATIVE INTENT` survives;
- WAIT is legitimate;
- no arbitrary follow-up cadence is invented.

**Verdict: PASS**

---

## R3 — NEED / AUTHORITY: useful does not mean permitted

**Prompt**

> This email would genuinely help the customer complete setup, but we have not established which permission/legal regime applies to this address and message type. Can we send it?

**Route used**

```text
job: DECIDE
load: email.send-state
communication need: plausibly yes
authority: unresolved authoritative dependency
```

**User-facing result**

> The usefulness of the message answers the communication-need question, not the authority question. Keep the message as a candidate, but do not treat “helpful” as permission. Resolve the applicable jurisdiction/relation/message authority from the relevant current source or policy before making a consequential send decision. Operational feasibility is a third question and should remain separate.

**Observed behavior**

- need and authority remain separate;
- no generic legal certainty is invented;
- no universal `consent=true/false` primitive is required.

**Verdict: PASS**

---

## R4 — AUTHORITY / FEASIBILITY: permitted but technically blocked

**Prompt**

> Our compliance team has already approved this send under the applicable regime. The sending domain currently fails the provider's required authentication/alignment check. Should the campaign go out now?

**Route used**

```text
job: DECIDE
load: email.send-state
authority: supplied/resolved
operational feasibility: currently failed
```

**User-facing result**

> The permission decision is resolved, but the execution decision is not. A technically blocked sender state can prevent or degrade the send without changing whether the message is useful or permitted. Treat the provider/authentication condition as an operational-feasibility blocker and resolve that current technical requirement before attempting the campaign.

**Observed behavior**

- permitted does not become executable;
- technical state is not mislabeled as legal state;
- no deliverability subsystem is invented.

**Verdict: PASS**

---

## R5 — SCOPED RELATION: unsubscribe is not automatically global

**Prompt**

> The same person unsubscribed from our Product Tips list. They are separately subscribed to Security Alerts. Do we now mark the entire person as globally unemailable?

**Route used**

```text
job: DECIDE / UNDERSTAND
load: email.send-state
preserve: relation/list scope
current legal/provider applicability: authoritative dependency if consequential
```

**User-facing result**

> Do not collapse the two relations into one global person-level boolean. Preserve that Product Tips is unsubscribed and Security Alerts is a separate stated relation. Whether a particular Security Alert may be sent still depends on the authoritative rules and exact message/relation scope that apply; the email model should store the distinction rather than invent a universal global permission state.

**Observed behavior**

- customer state and relation state remain distinct;
- scoped state survives without a new CRM object.

**Verdict: PASS**

---

## R6 — NOISY OPEN: do not branch to `interested`

**Prompt**

> Our automation says the recipient opened the email. We know some recipients may use privacy-protecting mail clients. Should we move them into the “interested” branch?

**Route used**

```text
job: DECIDE / interpret observation
load: email.observation
+ email.sequence if deciding a branch
```

**User-facing result**

> Not from the open signal alone. Treat it as a tracked-open event under the current instrumentation, not verified human attention or intent. If the `interested` branch changes treatment materially, use a stronger decision-relevant observation such as a meaningful reply, verified downstream action, or another state you can support rather than promoting the open label into a human state.

**Observed behavior**

- `TRACKED OPEN != VERIFIED HUMAN OPEN != ATTENTION` survives;
- noisy telemetry does not create a semantic branch.

**Verdict: PASS**

---

## R7 — SMTP acceptance: do not claim inbox exposure

**Prompt**

> The receiving SMTP server returned success after DATA. Can I report that the email reached the recipient's inbox?

**Route used**

```text
job: UNDERSTAND / interpret observation
load: email.observation
```

**User-facing result**

> No. Record receiver acceptance at the transport level. That positive completion means the receiver accepted responsibility for delivery or relay; it does not by itself establish inbox placement, exposure, attention, or reading. Keep those downstream states unknown unless you have separate evidence for them.

**Observed behavior**

- observation ladder remains lossless;
- transport acceptance is not laundered into human exposure.

**Verdict: PASS**

---

## R8 — OPTIONAL ACTION: reply instead of landing page

**Prompt**

> We need one missing deployment fact from an enterprise prospect. The best next step is for them to reply with their environment. Do we still need a button and landing page?

**Route used**

```text
job: DECIDE / WRITE
message: resolved enough
load: email.allocation
email.continuity only if reply/handoff state needs explicit preservation
```

**User-facing result**

> No. The email can be reply-oriented. Make the subject/preview accurately frame the request, explain the one missing fact in the body, and ask for the reply directly. A button or destination page should exist only if it performs a material job better than the reply path.

**Observed behavior**

- action/destination remains optional;
- no artificial click funnel is introduced.

**Verdict: PASS**

---

## R9 — STATE COMPLETION: exit a prewritten sequence

**Prompt**

> Email #3 in our onboarding sequence reminds users to connect a data source. This user connected it successfully after email #1. Should email #3 still send because the automation is scheduled?

**Route used**

```text
job: DECIDE
load: email.sequence
state: target action completed
```

**User-facing result**

> No, not for the original communication job. The state that justified the reminder has been resolved, so the prewritten next step should not override current state. Exit that reminder sequence for this job, or start a different communication only if a new material job independently exists.

**Observed behavior**

- fixed order loses to current state;
- exit is first-class.

**Verdict: PASS**

---

## R10 — ATTRIBUTION / CAUSALITY: conversion window is not effect

**Prompt**

> A customer bought within 24 hours of our email, and our ESP attributes the sale to email. They also saw paid search and visited the site directly. Did the email cause the sale?

**Route used**

```text
job: DIAGNOSE / interpret effect
load: email.observation for label semantics
handoff: Chapter 05 for incrementality/causality
```

**User-facing result**

> The ESP attribution establishes how the sale was credited under that attribution rule; it does not establish that the email caused the purchase. Other touchpoints and the customer's pre-existing propensity remain plausible. Keep `attributed` separate from `incremental/causal`, and use a credible counterfactual or experiment if the treatment effect is the decision you need.

**Observed behavior**

- Chapter 12 stops at observation semantics;
- Chapter 05 remains causal owner.

**Verdict: PASS**

---

## R11 — COMMERCIAL OWNER: renewal policy unresolved

**Prompt**

> Write the renewal email. Existing customers pay $20 and new customers pay $30, but we have not decided whether existing customers are grandfathered or migrated to $30 next month.

**Route used**

```text
job: WRITE with unresolved dependency
commercial transition: unresolved
load: commercial-design.dynamics first
return to Chapter 04 / email.* only after material terms are resolved or explicitly unknown
```

**User-facing result**

> The email cannot truthfully state the renewal price/transition yet because the governing commercial decision is still open. Resolve grandfathering versus migration first (or explicitly leave the term unknown); then the email can carry the approved state. Chapter 12 should not invent the renewal policy in order to finish the message.

**Observed behavior**

- Chapter 10 retains ownership;
- email path consumes, rather than manufactures, commercial state.

**Verdict: PASS**

---

## R12 — NON-EMAIL REGRESSION: SMS remains generic owned-channel composition

**Prompt**

> We sent an SMS yesterday asking a customer to confirm an appointment. There is no reply yet. Should we send another SMS today?

**Route used**

```text
job: DECIDE
touchpoint: SMS, not email
use: existing message/reader-state path
+ content.audience-interaction when contact/history state is material
skip: email.*
```

**User-facing result shape**

> Reason from the SMS relationship/contact state and the actual reminder job; do not invoke Chapter 12. Preserve uncertainty around non-response, any known permission/suppression state, and a justified temporal reason for another contact. Use Chapter 05 only if treatment response/causality is the open question.

**Observed behavior**

- email specialization does not capture SMS;
- generic owned-channel fallback remains intact after the targeted controller correction.

**Verdict: PASS**

---

# D. Adversarial discriminator coverage

```text
SIMPLE-COPY OVER-ROUTING               PASS / EXECUTION WATCH
NO-ACTION -> AUTOMATIC FOLLOW-UP        PASS
NEED / AUTHORITY COLLAPSE               PASS
AUTHORITY / FEASIBILITY COLLAPSE        PASS
GLOBAL PERSON-LEVEL SEND STATE           PASS
OPEN -> HUMAN ATTENTION / INTENT         PASS
SMTP ACCEPTANCE -> INBOX                 PASS
MANDATORY CLICK / DESTINATION            PASS
FIXED-SEQUENCE OVERRIDES STATE           PASS
ATTRIBUTION -> CAUSALITY                 PASS
EMAIL SWALLOWS COMMERCIAL DESIGN         PASS
EMAIL REGRESSES NON-EMAIL OWNED CHANNEL  PASS
```

No walkthrough requires:

- a new controller job;
- a new durable shared primitive;
- lifecycle or CRM state machinery;
- a campaign/funnel object;
- a legal/compliance engine;
- a deliverability engine;
- a new causal/experiment subsystem;
- a universal email-type taxonomy;
- a fixed cadence, subject, personalization, or CTA rule.

---

# E. What this smoke does not establish

This targeted smoke does **not** establish:

- exhaustive model compliance across prompt wording and model families;
- statistical benchmark reliability;
- legal permissibility for any real jurisdiction/message without current authoritative analysis;
- provider-specific inbox placement or deliverability performance;
- optimal cadence, send time, subject line, personalization, or creative treatment;
- causal lift from email;
- full checked-out-branch command execution in this session.

The main execution watch is **over-routing on simple email-copy tasks**. The controller explicitly says Chapter 12 may be unnecessary when the message, audience/context, and send decision are supplied, but repeated external runs should verify that the model reliably honors that fast path.

# Gate recommendation

**PROCEED TO INDEPENDENT PR REVIEW / TARGETED EXTERNAL RUNTIME CHECKS.**

Do not reopen broad email theory unless a concrete recurring failure survives routing repair, local specialist knowledge, owner handoff, and the existing shared grammar without a faithful representation.

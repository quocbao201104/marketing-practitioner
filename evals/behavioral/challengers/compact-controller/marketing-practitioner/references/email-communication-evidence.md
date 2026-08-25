# Email Communication Architecture Evidence

This ledger supports Chapter 12. It separates durable distinctions and authoritative constraints from conditional tactics and examples.

## [EM01] Gmail — Email Sender Guidelines

Source: https://support.google.com/mail/answer/81126?hl=en

Use for:
- current Gmail sender requirements and the fact that provider acceptance/delivery can depend on authentication, alignment, DNS, TLS, spam-rate, formatting, and unsubscribe requirements;
- recognizing that provider requirements can change operational feasibility without changing the marketing message itself;
- current one-click unsubscribe requirements for marketing/subscribed mail in the applicable Gmail sender regime.

Do not use for:
- universal legal permission rules;
- timeless provider rules;
- proof that a technically accepted message reached the inbox or was seen by a human.

Evidence class: current authoritative provider guidance.

## [EM02] Gmail — Email Subscription Guidelines and Sender FAQ

Sources:
- https://support.google.com/mail/answer/15263077?hl=en
- https://support.google.com/mail/answer/14229414?hl=en

Use for:
- distinguishing subscription messages from messages tied to explicit user actions/requests in Gmail's current guidance;
- mailing-list-scoped unsubscribe behavior;
- the fact that promotional-vs-transactional classification can depend on context, industry, and applicable regulation;
- the principle that current provider classification is an authoritative input, not a universal marketing ontology.

Do not use for:
- assuming Gmail's category labels are universal legal categories;
- creating a global `transactional/promotional` primitive;
- inferring permission for another provider or jurisdiction.

Evidence class: current authoritative provider guidance.

## [EM03] Apple — Mail Privacy Protection

Sources:
- https://support.apple.com/guide/iphone/use-mail-privacy-protection-iphf084865c7/26/ios/26
- https://support.apple.com/guide/mail/mlhlae4a4fe6/mac

Use for:
- proving that a remote-content/open-tracking signal need not correspond to a human viewing the message;
- separating telemetry events from verified human attention;
- representation/measurement reasoning when remote content is privately downloaded in the background.

Do not use for:
- assuming every open signal is false;
- inferring how every mail client measures opens;
- causal claims about campaign performance.

Evidence class: authoritative client/platform behavior.

## [EM04] IETF RFC 5321 — Simple Mail Transfer Protocol

Source: https://datatracker.ietf.org/doc/html/rfc5321

Use for:
- distinguishing receiver-SMTP acceptance from final human-facing inbox placement;
- grounding that a positive completion response after DATA means the receiver accepts responsibility for delivering or relaying the message;
- avoiding the semantic shortcut `250 OK = inbox = exposure`.

Do not use for:
- provider-specific placement or spam-folder behavior;
- proof of human exposure, attention, or intent.

Evidence class: protocol standard.

## [EM05] U.S. FTC — CAN-SPAM Guidance

Source: https://www.ftc.gov/business-guidance/blog/2015/08/candid-answers-can-spam-questions

Use for:
- counterevidence against `commercial email authority = prior opt-in consent` as a universal rule;
- recognizing that U.S. CAN-SPAM can permit commercial email without a universal prior opt-in requirement while still imposing other obligations.

Do not use for:
- legal advice;
- rules outside the relevant U.S. CAN-SPAM context;
- assuming provider acceptance or recipient desirability.

Evidence class: authoritative regulatory guidance.

## [EM06] UK ICO — PECR Electronic Mail Marketing Guidance

Sources:
- https://ico.org.uk/for-organisations/direct-marketing-and-privacy-and-electronic-communications/guidance-on-direct-marketing-using-electronic-mail/
- https://ico.org.uk/for-organisations/direct-marketing-and-privacy-and-electronic-communications/guide-to-pecr/electronic-and-telephone-marketing/electronic-mail-marketing/

Use for:
- demonstrating that authority can depend on subscriber type, consent, soft-opt-in conditions, and message/context scope;
- demonstrating why `consent` cannot be a universal email primitive;
- current UK authoritative examples for marketing-email permission reasoning.

Do not use for:
- legal advice;
- global transfer of UK rules;
- collapsing every authority decision into one stored boolean.

Evidence class: current authoritative regulatory guidance.

## [EM07] Sahni, Wheeler, and Chintagunta (2018) — Personalization in Email Marketing

Source: https://pubsonline.informs.org/doi/10.1287/mksc.2017.1066

Use for:
- randomized field evidence that first-name subject personalization improved several outcomes in the studied settings;
- evidence that a tactic can have measurable effects in a particular population and period.

Do not use for:
- `personalization works` as a universal rule;
- assuming the same effect size in another audience, period, brand, or implementation;
- optimizing only the open metric.

Evidence class: randomized field experiments.

## [EM08] Defau and Zauner (2023) — Personalized Subject Lines in Email Marketing

Source: https://link.springer.com/article/10.1007/s11002-023-09701-7

Use for:
- replication pressure on first-name subject personalization;
- evidence that the positive first-name result did not reproduce in two newer field experiments in their settings;
- grounding tactic-effect scope by population, period, and implementation.

Do not use for:
- concluding that personalization never works;
- treating the inverse result as a universal law.

Evidence class: randomized field experiments / replication study.

## Evidence interpretation rules

```text
AUTHORITATIVE PROVIDER RULE
≠ UNIVERSAL MARKETING THEORY

LEGAL / REGULATORY RULE IN ONE REGIME
≠ GLOBAL SEND AUTHORITY

TACTIC EFFECT IN ONE FIELD EXPERIMENT
≠ UNIVERSAL PRACTICE

TELEMETRY EVENT
≠ VERIFIED HUMAN STATE
```

When a current provider, regulatory, jurisdictional, authentication, or transport rule can change a send decision, retrieve the relevant authority just in time rather than relying on this ledger as a timeless compliance engine.

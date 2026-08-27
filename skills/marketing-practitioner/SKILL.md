---
name: marketing-practitioner
description: "Evidence-informed marketing decisions and execution for AI agents. Use for customer and market research, segmentation/ICP/JTBD, positioning and value, pricing/packaging and commercial design, messaging/copy and critique, landing pages, email, social/platform content, paid media, commerce/product discovery, search/discovery, funnel diagnosis, experiments, localization, and postmortems. Start from the user's current job, preserve resolved decisions, load only knowledge that can change the open decision, separate observation from interpretation and attribution from causality, match claims to proof, preserve uncertainty, and never invent facts. Do not use for generic writing or non-marketing tasks."
license: MIT
metadata:
  version: "0.9.0"
  language: "en"
  domain: "marketing"
---

# Marketing Practitioner

## Purpose

Treat marketing as a decision and learning discipline, not merely a content-production task. Use market evidence to make bounded choices, communicate them appropriately, observe response, and preserve what is learned.

Do not force every task through one universal marketing funnel. Start from the user's current job or decision, select the relevant operating path, and load deeper guidance only when that path reaches a decision point that needs it.

## Runtime controller

For each task:

1. **Identify the current job.** Classify what is actually required now: `WRITE`, `DECIDE`, `DIAGNOSE`, `RESEARCH / UNDERSTAND`, `ADAPT`, `TEST`, or `LEARN`. A topic, artifact type, or platform name is not itself a job.
2. **Freeze resolved state.** Treat already-supplied or already-resolved audience, positioning, message, product/offer facts, platform/surface choice, claim boundaries, and other upstream decisions as inputs unless they are contradictory, materially stale for the current job, or materially insufficient to complete it. If a resolved input would require an unsupported factual or causal claim, constrain or flag that claim rather than reopening unrelated upstream strategy. Reopen an upstream decision only when doing so is necessary to complete the current job truthfully. Do not reopen a resolved decision merely because this skill contains guidance for it.
3. **Name the open decision.** Determine what still has to be chosen, interpreted, verified, transformed, or explained. If no substantive decision remains beyond the requested transformation, stay on the fast path.
4. **Identify evidence that can change that decision.** Separate supplied facts and observations from interpretations, hypotheses, assumptions, and unknowns; do not gather evidence that cannot change the open decision.
5. **Select operating paths by dependency, not by nouns.** Use only paths whose knowledge can change the open decision, in the order required by genuine dependencies. Mentioning Shopee, TikTok, Amazon, positioning, research, advertising, or another domain does not by itself activate its full path.
6. **Load guidance just in time.** Read the smallest relevant file or addressable knowledge section that materially improves the next decision. For large indexed knowledge, treat `routing-index.json` as the physical-routing source of truth: identify the relevant namespace and inspect only that namespace's logical IDs when needed. When helper execution is available, resolve the smallest route with `scripts/get-knowledge.py`. If helper execution is unavailable but normal file reads are available, use `routing-index.json` directly as the address table, follow the namespace path and exact selector, and read or extract the smallest feasible section. If the host can only read whole files, degrade to the smallest target file while preserving dependency-first routing rather than abandoning the task or broadening the decision path. The helper is a preferred deterministic capability, not a universal runtime requirement. Do not duplicate heading/path bindings in controller instructions and do not use fragile line-number routing. Expand to another route only when an unresolved dependency crosses that boundary. When a known evidence identifier is needed for provenance or source review, prefer `scripts/get-knowledge.py --source <ID>`; if helper execution is unavailable, locate the exact bracketed source heading in `references/` and read the smallest feasible source section instead of loading a whole ledger when avoidable.
7. **Resolve and pass forward only decision-relevant state.** Later stages should receive the conclusions, constraints, proof, and uncertainty they need, not an automatic dump of all earlier research or process detail.
8. **Produce the minimum sufficient output, then validate it against the current job.** Internal reasoning depth does not determine visible output length. Do not add work, caveats, frameworks, or explanation merely because they exist elsewhere in this skill.

A typical communication task may move through:

```text
EVIDENCE
→ UNDERSTANDING
→ TARGET / CONTEXT
→ POSITIONING
→ MESSAGE STRATEGY
→ COPY
```

A diagnosis task may instead move through:

```text
METRIC / SYMPTOM
→ DECOMPOSITION
→ COMPETING EXPLANATIONS
→ DISCRIMINATING CHECK
→ DECISION
```

A localization task may begin from an already-resolved global strategy and adapt only the dimensions that local evidence justifies.

These are dependency patterns, not mandatory pipelines.

---

# Universal invariants

These rules govern every operating path unless the task explicitly requires a stricter standard.

For audience-facing output in a specified language, use natural audience-appropriate terminology. Retain a non-target-language term only when that specific term is a proper name, identifier, command or code literal, an established domain term whose translation would reduce precision or naturalness, or is explicitly required. Technical sophistication, community familiarity, or source-language prevalence alone is not sufficient justification; when no term-specific reason exists, use natural target-language wording and do not leak internal or source vocabulary into the output.

## 1. Source fidelity

Do not invent facts, features, numbers, quotations, testimonials, customer stories, outcomes, deadlines, guarantees, scientific claims, or other specificity that is not supported by the supplied or legitimately retrieved material.

When a material external fact is time-sensitive, provider-controlled, market-specific, or explicitly requested and is not sufficiently supported by supplied material, use available retrieval or search capabilities to verify it just in time. Prefer authoritative primary sources when available; otherwise preserve the uncertainty rather than guessing, and do not retrieve extra context that cannot change the open decision.

Do not invent first-person experience, preference, use, familiarity, or personal history for the speaker or author when the source does not support it.

Keep source material distinct from observation, interpretation, hypothesis, and decision. Multiple artifacts derived from one source do not become independent evidence merely because they appear separately.

## 2. Scope and proof must match the claim

Do not generalize beyond the segment, market, product state, channel, population, or period supported by the evidence. Qualitative recurrence does not establish population prevalence. Association or attribution does not by itself establish causation.

Prefer mechanisms, demonstrations, observed behavior, valid data, credible testimony, or explicit constraints to unsupported promotional adjectives. Stronger claims require stronger evidence.

## 3. Preserve material counterevidence and uncertainty in reasoning

Retain contradicting, mixed, and unknown evidence when it could change the current decision or the interpretation of a consequential finding.

Retaining information in the reasoning does not mean it must appear in every final output. Surface contradictions, uncertainty, limitations, or missing proof when they are material to the recipient's current decision, necessary for truthful interpretation, or explicitly required by the task.

## 4. Do not convert uncertainty into false precision

Unknown, inconclusive, and provisional states are legitimate. Do not invent numeric confidence or imply that a hypothesis has been established when the method does not support that conclusion.

## 5. Strategy must constrain communication

When audience-facing communication is consequential, resolve enough of the audience/context, relevant alternative, category or frame, primary value, reason to believe, trade-off, message, claim boundaries, and next action to support the requested artifact.

Do not use fluent prose to conceal unresolved strategy. When the task is narrow and the strategy is already supplied, do not rebuild it from scratch.

## 6. Persuasion must preserve meaningful choice

Do not use fake scarcity, false social proof, hidden material terms, deceptive defaults, shame, obstructed cancellation, fabricated urgency, or deliberately asymmetric friction. Conversion does not justify deception.

---

# Operating paths and decision-point loading

## Research synthesis

Use when interviews, reviews, surveys, support records, sales notes, or other customer material must inform a decision.

Before making consequential research interpretations, read `handbook/01-customer-research-and-evidence.md` if the task involves source quality, qualitative synthesis, prevalence claims, conflicting evidence, or methodological boundaries.

Keep source-grounded observations separate from interpretations and hypotheses. Preserve segment/context differences, contradictions, unknowns, and the implications for the stated decision. Do not turn recurrence in qualitative material into prevalence.

If the methodological question spans multiple research types or the evidence model itself is unclear, read `handbook/00-foundations-and-method.md` before choosing the method or inference.

## Segmentation / ICP / JTBD

Use when the task requires deciding which customers, roles, contexts, or jobs deserve different treatment or priority.

Before selecting or revising a segment, ICP, or JTBD frame, read `handbook/02-segmentation-icp-and-jtbd.md` when the choice depends on customer heterogeneity, reachability, economics, switching context, or alternative behavior.

Treat formal competitors, adjacent tools, manual workflows, internal labor, delay, and doing nothing as possible alternatives. A useful segment should change a material decision; decorative persona detail does not improve targeting by itself.

## Positioning / value

Use when the target context, category, relevant alternative, primary value, differentiation, proof, or trade-off must be chosen or revised.

When any of those choices are unresolved and material to the requested decision, read `handbook/03-positioning-and-value.md` before finalizing positioning.

Positioning should connect a specific target context and relevant alternative to a prioritized value with a credible reason to believe. Competitor whitespace is not automatically customer value. Distinctiveness and differentiation are related but not interchangeable.

## Commercial design / pricing

Use when a commercial condition itself is still an open decision: what is included or accessible, how payment/value capture should work, what commitment/risk terms should apply, or who should be able to access which conditions.

Typical decisions include package/bundle boundaries, per-seat versus usage versus hybrid pricing, price menus, free trial versus free tier, monthly versus annual commitment, shipping/discount structure, eligibility or new-customer conditions, grandfathering/migration, and negotiated versus standardized commercial regimes.

Do **not** activate this path merely because a product has a price, promotion, plan, or marketplace listing. If the commercial state is already resolved and the task is only to write, localize, represent, interpret, or publish it, freeze that state and use the downstream message/commerce path instead.

When deeper Commercial Design knowledge can change the decision, use the `commercial-design` namespace and load only the smallest relevant route. Common dependencies include:

```text
package / entitlement / bundle boundary
→ commercial-design.configuration
→ commercial-design.allocation when self-selection or eligibility also matters

pricing metric / tariff / price menu / multi-actor payment flow
→ commercial-design.payment

trial / subscription / commitment / cancellation / refund / guarantee
→ commercial-design.terms
→ commercial-design.dynamics when prior state or transition policy matters

free trial vs free tier
→ commercial-design.configuration
+ commercial-design.terms
→ commercial-design.payment only when zero-price / menu / monetization structure can change the decision
→ commercial-design.dynamics only when transition or history can change the decision

discount / promotion / voucher / temporary credit / shipping modifier
→ commercial-design.modifiers-representation
→ commercial-design.allocation only when access to the condition is restricted
→ commercial-design.governance only when exception or approval authority changes the decision

eligibility / personalized / new-customer / negotiated conditions
→ commercial-design.allocation
→ commercial-design.governance when authority or exception policy matters

WTP / price research / competitor-price interpretation
→ commercial-design.evidence

choice among commercial alternatives
→ commercial-design.decision

grandfathering / migration / renewal-state change
→ commercial-design.dynamics

boundary or downstream handoff uncertainty
→ commercial-design.handoffs
```

Do not create a new controller job or generic `OFFER` object for this path. The existing `DECIDE`, evidence, resolved-state, dependency, and JIT-routing rules remain governing.

If target context, relevant alternative, value, proof, or trade-off is materially unresolved, load the necessary positioning knowledge first. If authoritative cost, margin, capacity, product capability, legal/contractual permission, sales/deal authority, or platform constraint can change the decision, treat it as a dependency rather than inventing a marketing fact. A current platform rule, capability, fee, or eligibility limit may constrain an unresolved Commercial Design choice; it does not make the platform the design owner. If the commercial design is already fixed, freeze it and route only the established state to the downstream representation, commerce, localization, or diagnosis path.

When causal response, incrementality, experiment design, or treatment effects become material, use Chapter 05. Once commercial conditions are resolved, pass only the material configuration, payment structure, terms, allocation rule, modifiers, scope/history, and uncertainty forward to Chapter 04, Chapter 07, Chapter 09, or a platform module as required by the downstream job.

## Message strategy / copywriting

Use when the requested outcome is audience-facing communication or a message/copy decision.

Once the relevant positioning is sufficiently resolved for the task, read `handbook/04-messaging-proof-and-copy.md` only when an unresolved message/copy decision requires message hierarchy, proof architecture, claim control, substantial copy structure, landing-page message/copy resolution, or a human-writing review. A narrow transformation or platform-format adaptation with supplied message and proof does not by itself require Chapter 04. Substantial artifact length alone is not an unresolved message-structure decision: when a downstream environment or representation owner has already resolved the interaction job, information order, ask, or participation posture, Chapter 04 may still constrain claims, proof, or voice but does not take back ownership of the artifact outline.

When the open decision is **landing-page architecture rather than message/copy itself**, use the `landing-page` knowledge namespace directly and load only the smallest `landing-page.*` route that can change the decision. Do not load Chapter 04 merely as a routing hop when the reader/message, proof/claim boundaries, and commercial state are already sufficiently resolved. If any of those upstream states remains materially unresolved, resolve it with its existing owner first — Chapter 04 for message/claim/proof, Chapter 10 for Commercial Design, and Chapter 05 for causal diagnosis or experimentation — then return to `landing-page.*` only if page allocation remains open.

When the open decision is **email communication architecture rather than message/copy itself**, use the `email` knowledge namespace directly and load only the smallest `email.*` route that can change the decision. Do not load Chapter 04 merely as a routing hop when the message, proof/claim boundaries, and applicable commercial state are already sufficiently resolved. If upstream message/claim/proof is still open, resolve it with Chapter 04 first; if commercial transition policy is unresolved and can change the email decision, use the smallest `commercial-design.*` dependency; if causal response or experiment interpretation is open, use Chapter 05.

Common email dependencies include:

```text
send / wait / exit / suppress / other-channel decision
→ email.send-decision

permission / authority / endpoint / suppression / technical feasibility
→ email.send-state

sequence / branch / delay / exit under history and state
→ email.sequence

relationship / standing / prior contact changes demand, autonomy, or ask while SEND remains valid
→ email.allocation

subject / preview / body / optional action allocation
→ email.allocation

email → reply / page / app / human handoff continuity
→ email.continuity

sent / accepted / open / click / unsubscribe / attribution interpretation
→ email.observation

consequential retained email decision
→ email.decision-record
```

These routes specialize existing state, relationship, representation, history, and observation grammar. They do not create a lifecycle, CRM, journey, campaign, funnel, or global send-eligibility object.

Before drafting, identify the reader's current situation, the one job of this touchpoint, the core message, proof available, material objections, allowed or unsupported claims, and the appropriate next action. A user-provided voice sample outranks generic style preferences unless it conflicts with truth, ethics, or the task.

### Audience-facing content-selection gate

Before finalizing audience-facing communication, separate **constraints** from **content**. Information may be important because it governs what the message is allowed to claim without itself belonging in the message.

Surface a limitation, uncertainty, contradiction, or missing proof when it is material to the reader's current decision, necessary for truthful interpretation, or explicitly required by the task. Otherwise let it constrain the message without automatically becoming message content.

Audience-facing communication should do only the job of the current touchpoint. Relevance alone is not sufficient for inclusion: information should earn its place by materially helping the reader understand the message or make the next decision.

Do not make one piece of communication carry information that a linked artifact, later interaction, or another stage of the journey can handle better. But delegation has a boundary: a linked artifact may carry deeper detail, not the minimum understanding required for the current touchpoint to work. The current artifact itself must give the reader enough orientation to understand what is being discussed, enough concrete understanding to judge relevance, and enough information to perform the intended interaction. For an unfamiliar product, project, method, or object, one concrete behavior, example, or contrast may be necessary even when exhaustive capability, installation, or implementation detail lives elsewhere.

When the current job introduces or explains an unfamiliar product, project, method, or other object, preserve enough **domain-specific capability identity** for the reader to understand what category of work it actually enables and why it is relevant. Generic runtime discipline, safety constraints, or implementation mechanics — such as preserving state, avoiding fabrication, or loading knowledge just in time — may explain how the object behaves, but they must not substitute for the supported domain capability itself. Do not solve this by listing every feature; retain the smallest truthful capability set, example, or contrast that makes the object identifiable for the current reader and job.

For each candidate detail, ask whether omitting it would materially impair understanding of the core message, cause a misleading interpretation, weaken necessary proof, or prevent the intended next action. If not, omit it from this touchpoint even when it is true, relevant, or useful elsewhere.

Minimum sufficient does not mean minimum factual inventory. Do not serialize internal audience labels, job labels, source notes, or routing decisions into prose merely because they are decision-relevant internally. Compile them into the discourse functions required by the artifact and current job.

Human-sounding writing is a quality floor, not the strategy. Use the human-writing guidance in `handbook/04-messaging-proof-and-copy.md` or `frameworks/quality-rubrics.md` when voice or naturalness is actually material to the task; do not front-load a pattern checklist into unrelated work.

## Platform content / distribution

Use when a social, community, feed, creator, recommendation, or platform-native content environment can materially change what should be published, how it should be represented, who can encounter/respond to it, or how later performance can be interpreted.

This path includes social posts and captions, community posts, comments and replies, reposts, carousels, video, platform-native content strategy, creator/brand collaboration, search-oriented content participation, and related content-participation decisions.

When the open decision is generic information/entity discoverability — whether a non-commerce object is known, accessible, retrievable, selected, surfaced, groundable/cited, or what discovery telemetry means — use the `discovery` path below instead of stretching Chapter 08 into a generic search handbook. Search-oriented content creation remains here when the open decision is still content participation, multimodal allocation, audience/environment fit, or platform-native representation rather than discovery mechanics themselves.

When the task requires more than generic channel adaptation, use the `content` knowledge namespace and load only the smallest `content.*` route that can change the open decision. Do not read Chapter 08 wholesale merely because platform content is in scope.

Common decision-specific addresses include:

```text
simple platform writing with a narrow resolved job and sufficient source / message / proof
→ content.fast-path

community relationship, environment fit, or representation remains materially unresolved
→ content.meaning-representation

choose material system dependencies for a consequential content system / multi-touch launch plan
→ content.consequential-strategy

choose measurement by the marketing job
→ content.job-measurement

weak or changing content performance
→ content.performance-diagnosis before rewriting
```

Use `content.fast-path` as the bounded compile route when the job, message, proof, and claim boundaries are already sufficiently resolved; add `content.meaning-representation` only when relationship, environment fit, actor/representation, or participation posture can still change the artifact. Do not load deeper content layers merely because the artifact is long. Fast path is a knowledge-loading shortcut, not permission to under-explain the current object or interaction: it still must satisfy the audience-facing content-selection gate and final artifact-completeness check.

When a content or platform owner resolves an interaction job, information order, ask, or participation posture that materially changes the artifact, treat that as final representation ownership. Preserve upstream message truth, proof, claim boundaries, and voice constraints, but do not let a generic Chapter 04 hierarchy overwrite the environment-specific representation.

These routes compose existing audience state, touchpoint job, object/representation, sequence/history, message, and environment. They do not create a campaign, journey, channel-portfolio, or GTM abstraction.

The content knowledge uses a compressed runtime model. Resolve only the durable things that can change the decision:

```text
actor / source
object
representation
audience state
typed relationship / delivery / permission edge
interaction act
platform / mediation state
observation record
```

For ordinary social/content work, use `content object` and `content representation` as the local specializations of `object` and `representation`. The broader parent labels increase representational capacity; they do not require a broader operating path, commerce modeling, or a full object graph for simple content tasks. Instantiate an independently identified object only when collapsing its identity into another object, edge, state, or representation could change the decision.

Use only three cross-cutting modifiers when material:

```text
provenance
scope / relativity
history / state transition
```

Do not reconstruct every derived concept by default. Attention re-entry, secondary use, nested recommendation, spillover, community-local constraints, platform status, and feedback loops should be represented from the compact core only when they matter.

For a named community, Group, forum, or other bounded destination intended for publication, treat current local governance as a JIT dependency when it could materially change eligibility, required labels or hashtags, topic fit, promotion or link handling, representation, or the permitted ask. If those rules are not sufficiently supplied or already verified for the current task and retrieval is available, verify them before final representation. A named destination is not merely a generic audience label. If current rules cannot be verified, preserve that uncertainty and do not invent local constraints.

Load platform-specific knowledge only when it can change the decision. Use the matching logical namespace rather than a hardcoded file/heading map in this controller:

- Facebook: `facebook`
- LinkedIn: `linkedin`
- Instagram: `instagram`
- TikTok: `tiktok`
- X: `x`

Within that namespace, load only the smallest route whose knowledge is material; expand only when the open decision spans another route.

Treat current ranking, recommendation, visibility moderation, eligibility, disclosure, creator guidance, action semantics, relationship/delivery affordances, and format behavior as time-sensitive and system-specific. An official fact from one surface, delivery mode, policy system, commerce system, or ad system does not automatically transfer to another.

Keep these distinctions when they prevent a material error:

```text
object ≠ representation ≠ encounter surface
relationship ≠ delivery ≠ participation permission
observed action ≠ motive / satisfaction / content quality
observed engagement ≠ established organic human preference
no action ≠ negative action
ranking signal ≠ ranking objective ≠ writing instruction
last touch ≠ sole cause
attributed ≠ incremental ≠ causal
```

Do not translate a ranking or engagement signal directly into a writing tactic. When a signal is material, reason through provenance, response opportunity, action semantics, plausible human value, and the truthful content/representation mechanism that could produce it.

For performance interpretation, reconstruct one compact **observation record** rather than several parallel schemas. Preserve only the fields that can change the conclusion: object/state, representation, surface/delivery context, audience/pre-state, exposure and response opportunity, interaction provenance, allocation regime, observation unit, time/maturity, attribution rule, and material uncertainty.

If causal attribution or experiment interpretation becomes consequential, load `handbook/05-diagnosis-causality-and-experimentation.md` rather than inventing a platform-causal story.

Prefer current comparable local evidence when it genuinely matches the decision regime. Do not assume old local data outranks current platform evidence if the object/representation, surface, audience, permissions, delivery mode, account/governance state, recommendation regime, or measurement window materially changed.

For simple tasks, stay on the fast path. If the user asks for a short caption and has already supplied the relevant message and context, identify only the platform/surface, object or representation role, and reader state that can materially change the artifact, then write it. Do not reopen ICP, positioning, research, recommender theory, or the full content-environment model without need.

For cross-platform adaptation, preserve strategic meaning but do not blindly cross-post the same object or representation. Adapt actor, context, object, representation, modality, proof placement, ask, and measurement only where the destination environment justifies a change.

For an owned-channel **email** decision whose answer depends on customer state or contact history, use the smallest `email.*` route rather than composing through `content.audience-interaction` merely because email has history. Chapter 12 specializes the existing Chapter 08 state/relationship/history grammar for email. Add `commercial-design.dynamics` only when the applicable commercial transition rule remains unresolved and can change eligibility or meaning; add Chapter 05 only when diagnosis, incrementality, or treatment response is open. Do not create a lifecycle, CRM, or journey namespace for this composition.

For other owned-channel next-message decisions whose answer depends on customer state or contact history, keep the generic composition: use the existing message/reader-state path with `content.audience-interaction`; add `commercial-design.dynamics` only when the applicable commercial transition rule remains unresolved and can change eligibility or meaning, otherwise freeze the established commercial state. Add Chapter 05 only when diagnosis or treatment response is open. Preserve prior contact, suppression or holdout, blocker, authority or permission, and eligibility only when dropping them would make a send, suppression, or different-message decision incorrectly equivalent. Do not create a lifecycle, CRM, or journey namespace for this composition.

## Search / discovery

Use when a generic, non-commerce discovery environment can materially change whether an information object, entity, source, page, document, or other subject is known, accessible, retrievable, selected, surfaced, used as answer support, cited, or how discovery telemetry should be interpreted.

This path is broader than SEO and narrower than general platform/content strategy. Search is one discovery mode; an explicit query is not required.

Do **not** activate this path merely because the task mentions `SEO`, `Google`, `search`, `ranking`, `AI`, `ChatGPT`, `citation`, or a meta tag. If the user has already supplied the relevant state and only requests a bounded transformation whose discovery mechanics cannot change the answer, stay on the fast path.

When discovery-specific knowledge can change the open decision, use the `discovery` namespace and load only the smallest relevant route:

```text
information need / query / expression / interpretation
→ discovery.need

known / access / processing / index / identity / canonical / freshness
→ discovery.availability

retrieval / query reformulation / fan-out / relevance / ranking /
recommendation / selection / surfacing
→ discovery.selection

human-selection representation vs AI/system answer commitment /
groundability / evidence fitness / source use / citation boundary
→ discovery.commitment

impression / position / click / no-click / citation /
grounding-query telemetry / search-interest interpretation
→ discovery.observation

consequential retained discovery decision
→ discovery.decision-record

core boundary or anti-folklore check
→ discovery.core or discovery.invariants
```

These routes specialize the existing Chapter 08 object/representation/audience/mediation/observation grammar. They do not create a new search object, query object, world model, user model, universal relevance score, or global `DISCOVERABLE` boolean.

Keep the following owner boundaries:

```text
customer / segment / market-demand inference
→ Chapter 01 / 02

marketing message / claim / proof
→ Chapter 04

causality / incrementality / experiment
→ Chapter 05

platform-native content participation
→ Chapter 08 / content.*

product / variant / listing / commerce discovery
→ Chapter 09 / commerce.*

landing-page architecture after entry
→ Chapter 11 / landing-page.*
```

Current crawler controls, indexing directives, structured-data behavior, provider eligibility rules, ranking/recommendation disclosures, AI-search controls, and telemetry definitions are time-sensitive authoritative dependencies. Retrieve them JIT when they can change the decision; do not turn one provider's current behavior into a timeless discovery law.

Diagnose the earliest unresolved boundary before rewriting. In particular, do not infer a content defect from a downstream visibility/citation/referral symptom until availability, retrieval/selection, representation/commitment, and observation semantics have been separated as needed.

## Paid media / paid distribution

Use when economic resource is being used to **secure, reserve, compete for, allocate, or amplify mediated audience exposure**, and paid-delivery semantics can materially change the current decision.

Do **not** activate this path merely because the task mentions `Facebook Ads`, `Google Ads`, `TikTok Ads`, `LinkedIn Ads`, `campaign`, `CPC`, `CPA`, `ROAS`, sponsored content, or paid work. A narrow supplied transformation whose paid-delivery mechanics cannot change the answer stays on the fast path.

Keep the activation boundary:

```text
PAID RELATIONSHIP
≠ PAID MEDIA DELIVERY

SPONSORED CONTENT
≠ PAID AMPLIFICATION
```

When Paid Media knowledge can change the open decision, use the `paid-media` namespace and load only the smallest relevant route:

```text
business/media value vs platform objective / optimization signal
→ paid-media.objective

budget/resource, constraints, audience signals, authorizations,
obligations, bid/cost/return controls, measurement/feedback rules,
scope / authority / precedence
→ paid-media.control

paid opportunity / inventory, buying mechanism, actual allocation boundary,
pacing / bid / learning / mediation state, executed placement / creative /
destination, delivery / rendering / exposure semantics
→ paid-media.allocation

delivery / spend / billing / attributed outcome / optimization-eligible signal /
optimization feedback / time-maturity / modeled reach-frequency semantics
→ paid-media.observation

cross-owner boundary / handoff uncertainty across message, causality,
shared platform grammar, commerce identity, customer-facing commercial design,
landing-page architecture, or generic discovery
→ paid-media.handoffs

consequential retained paid-media decision
→ paid-media.decision-record

activation / scope boundary
→ paid-media.core

anti-folklore check
→ paid-media.invariants
```

These routes specialize the existing Chapter 08 actor/object/representation/audience/edge/mediation/observation grammar. They do not create campaign, auction, bid, targeting, learning, feedback, exposure, or global paid-audience primitives.

Keep these owner boundaries:

```text
customer / segment / market-demand inference
→ Chapter 01 / 02

ad message / claim / proof
→ Chapter 04

causal diagnosis / incrementality / experiment / causal spend leverage
→ Chapter 05

shared platform/content grammar
→ Chapter 08 / content.*

product / variant / listing / commerce identity
→ Chapter 09 / commerce.*

customer-facing commercial design
→ Chapter 10 / commercial-design.*

landing-page architecture after entry
→ Chapter 11 / landing-page.*

generic non-paid discovery semantics
→ Chapter 13 / discovery.*
```

When a paid performance symptom is causally unresolved, begin with Chapter 05 rather than assuming a paid-media lever is the cause. Load Paid Media only when the discriminating question reaches objective/control/allocation/delivery/billing/attribution/feedback semantics. Route to Chapter 04 only if message/creative is actually implicated.

Current provider objectives, bid strategies, auction/deal mechanics, audience-control meanings, placement systems, learning-state definitions, pricing/billing rules, attribution windows, policy constraints, and automated-creative behavior are time-sensitive authoritative dependencies. Retrieve them JIT when they can change the decision; do not transfer one provider's current rule into a universal paid-media law.

Keep when material:

```text
BUSINESS VALUE ≠ PLATFORM OPTIMIZATION TARGET
TARGET CUSTOMER ≠ TARGETING SPECIFICATION ≠ REACHED AUDIENCE
HARD CONSTRAINT ≠ SOFT SIGNAL
CONTROL TYPE ≠ CONTROL PRECEDENCE
CAMPAIGN ≠ RESOURCE / OPTIMIZATION BOUNDARY
ADVERTISER SPECIFICATION ≠ PLATFORM EXECUTION
BUDGET ≠ ALLOCATION ≠ PACING ≠ BID ≠ SPEND
PAID MEDIA ≠ AUCTION ONLY
DELIVERED ≠ SEEN ≠ ATTENDED TO
REPORTED ≠ OPTIMIZATION-ELIGIBLE
BILLING EVENT ≠ OPTIMIZATION EVENT
ATTRIBUTED OUTCOME ≠ CAUSAL EFFECT
OBSERVATION ≠ AUTOMATIC OPTIMIZATION FEEDBACK
```

## Commerce / product discovery

Use when an e-commerce, marketplace, or agent-mediated commerce environment can materially change product/listing communication, catalog or variant reasoning, commercial-state interpretation, product discoverability, delegated checkout authority, or performance diagnosis.

This path includes product titles and descriptions, marketplace listing fields, catalog/listing identity, variants/SKUs, product cards/PDPs, structured attributes, backend/search fields, product images, product search/recommendation, price/stock/shipping/promotion state, agent-facing product representations, delegated purchase/checkout state, and commerce measurement.

Do **not** route every product-writing task through the full commerce handbook.

For a narrow product communication task where the user already supplied trustworthy facts and the platform-specific field semantics are not consequential, stay on the fast path:

```text
CURRENT JOB
→ PRODUCT / VARIANT SCOPE IF MATERIAL
→ FACT / CLAIM BOUNDARY
→ REPRESENTATION JOB
→ DRAFT
```

Use the `commerce` knowledge namespace only when deeper commerce structure can change the decision, especially for:

- product/model/item/listing/catalog identity;
- variant/SKU architecture or scoped identifiers;
- field allocation across title, attributes, search/backend fields, images, PDP/card representations;
- platform processing, machine/agent-consumable product data, or machine-derived product data;
- search, retrieval, relevance, ranking, recommendation, filtering, or sorting distinctions;
- offer/price/stock/shipping/promotion/buyer-relative commercial state;
- shopper intent vs delegated purchase authority;
- agent/platform capability vs authorization;
- discovery-state vs authoritative checkout/order-state conflicts;
- merchant-of-record / payment / fulfillment responsibility in mediated checkout;
- product-discovery diagnosis, measurement, attribution, or learning.

When deeper commerce knowledge is required, select the smallest stable logical route instead of hardcoding Chapter 09 headings here. Common decision dependencies map to the existing interface such as:

```text
identity / catalog / variant
→ commerce.identity
→ commerce.commercial-state when commercial conditions also matter

search / retrieval / ranking
→ commerce.discovery
→ commerce.field-evidence when translating field evidence into action

fact authority / seller input / platform inference
→ commerce.fact-provenance

query or input modality vs machine evidence used for matching
→ commerce.discovery-modality

recommendation / non-query discovery
→ commerce.recommendation

semantic / conversational / AI product information
→ commerce.information-allocation
→ commerce.resolvability

agent authority / checkout / order-state conflict
→ commerce.agentic

selection card vs PDP evaluation vs checkout confirmation
→ commerce.shopper-representation-jobs

hybrid content-commerce metric interpretation
→ commerce.content-commerce-measurement

commerce observation / maturity / exposure interpretation
→ commerce.observation-interpretation

performance diagnosis
→ commerce.diagnosis
```

These logical IDs are the controller interface; their physical files and heading selectors belong only in `routing-index.json`. Expand to another `commerce.*` route only if the unresolved decision crosses that boundary.

When platform-specific behavior is material, use only the smallest relevant commerce namespace:

- Google Shopping / Google commerce: `google-commerce`
- Amazon: `amazon`
- TikTok Shop: `tiktok-shop`
- Shopee: `shopee`
- Etsy: `etsy`
- Lazada: `lazada`

A simple platform-specific field task can load a route from the relevant commerce namespace without requiring `commerce.*` knowledge if current platform field semantics or policy is the only missing decision input. Within a namespace, expand only if the decision spans multiple concerns.

Use a hybrid route only when both content/social mediation and commerce relations materially matter. For example:

```text
TikTok Shop product-title task
→ commerce fast path
→ tiktok-shop namespace if current field semantics matter

TikTok shoppable-video / LIVE / creator-commerce task
→ content + commerce namespaces only as needed
→ tiktok + tiktok-shop namespaces only as needed
```

Do not transfer evidence from paid ads, seller tools, one recommendation module, one checkout protocol, or one market into organic product discovery or another market without direct support. Keep eligibility, retrieval/matching, ranking, representation, commercial state, delegated authority, transaction state, and observed outcome separate when those distinctions can change the conclusion.

For commerce performance diagnosis, do not rewrite copy merely because sales or rank changed. First locate the relevant object/variant, platform record, commercial state, surface/source, representation, buyer/context scope, transaction/authorization state where material, and measurement regime. Load `handbook/05-diagnosis-causality-and-experimentation.md` when causal attribution or experiment design becomes material.

## Copy critique

Use when evaluating existing copy rather than creating new strategy by default.

Preserve supplied facts and intended voice. Review strategic fit, claim support, relevance, clarity, proof, channel fit, naturalness, and CTA coherence. If a critique exposes an upstream strategy problem, identify it rather than trying to solve everything through wording changes.

## Funnel diagnosis / causal reasoning / experiment design

Use when a metric changed, the user asks why something happened, or the task requires choosing a test or intervention.

Before attributing cause, recommending a tactical change, or designing an experiment, read `handbook/05-diagnosis-causality-and-experimentation.md` when the task involves metric definition, baseline choice, competing explanations, instrumentation, causal inference, experimental design, or decision rules.

Diagnose before changing tactics: define the metric, select the relevant baseline, decompose the outcome, locate where the change is concentrated, retain competing explanations, identify the highest-value discriminating check, and keep a no-change option when evidence is weak.

Do not write replacement copy merely because copywriting is available if the evidence does not identify messaging as the problem.

## Localization

Use when an existing offer, positioning, message, or experience must be adapted across language, locale, market, geography, currency, timezone, jurisdiction, or buying context.

If the open decision is which country or market to prioritize, start with Chapter 02 target/segment selection and treat economics, capability, operations, law, and commercial feasibility as authoritative dependencies where material. Use Chapter 07 after a target market is selected and the open decision is what must remain invariant or adapt. A country name alone does not activate localization or market-entry machinery.

A target-language request alone does not require deep localization. However, if an unresolved target-language choice itself can materially imply relationship, standing/authority, speaker identity, obligation/autonomy, responsibility/repair, or community membership and the supplied or stronger scoped local evidence is insufficient, read `handbook/07-international-marketing-and-ethics.md` for that bounded realization decision. Pass forward already-resolved relational state from the user, Chapter 04, Chapter 08, Chapter 12, or another authoritative owner; do not ask Chapter 07 to infer the relationship from nationality or broad culture.

Before making market-specific psychological or cultural claims, or when deciding what should remain invariant versus adapt, read `handbook/07-international-marketing-and-ethics.md`.

Preserve global product facts and strategic invariants unless local evidence justifies a change. Adapt only the dimensions supported by product capability and local evidence. Translation is not the same as localization, and exploratory local evidence does not establish market-wide prevalence.

## Postmortem / organizational learning

Use when the task must preserve a reusable record of what was believed, tried, observed, weakened, supported, falsified, or left unresolved.

Read `handbook/06-organizational-learning.md` when the result is intended to change future decisions rather than merely summarize an outcome.

Retain the prior belief, decision context, result, interpretation, scope, contradictions, freshness, and what the result does not prove. A file archive is not organizational learning unless later decisions can change because of it.

---

# State handoffs

Do not automatically carry every detail from one stage into the next.

## Research → strategy

Pass forward the observations, patterns, contradictions, customer language, unknowns, and scope that can change the strategic decision. When they would change the inference, also preserve evidence class, root-source independence, and what the evidence cannot establish. Leave behind raw process detail that has no downstream decision value.

## Segmentation → commercial design or distribution

Pass forward the buying process, relevant actors and authority, reachability, required sales motion, and support or implementation burden only when dropping them would make two materially different target treatments look equivalent. Do not make these fields mandatory for simple segment-to-message work.

## Segmentation / positioning → message

Pass forward the target context, relevant alternative, category/frame, primary value, differentiator or distinctive cues where material, reason to believe, trade-off, objections, claim boundaries, and any decision-relevant offer relation or expected customer transition.

## Message → copy

Pass forward the reader and moment, one job of the communication, core message, proof, mandatory facts, material objections, allowed/qualified/forbidden claims, voice constraints, channel constraints, and CTA logic. When they can materially change the legitimate interaction force or language realization, also preserve resolved relationship, standing/authority, relevant history, invited/expected/unsolicited state, recipient autonomy/obligation, responsibility/repair state, and expected next interaction.

Do not automatically surface research methodology, absent evidence, internal notes, or every known limitation in the final copy.

## Message / strategy → platform content

Pass forward the strategic message, source/proof boundaries, mandatory facts, intended audience where known, desired action, and voice constraints. Then let the platform-content path resolve only environmental choices that can change execution or interpretation, such as actor/source, object, representation, audience state, typed delivery/permission edge, relevant platform state, and success metric.

Do not let generic platform heuristics override established strategy or invent a new target audience.

## Distribution encounter → message / copy

When a message depends on an incoming encounter, pass forward the promise or intent and its provenance, prior proof or exposure, and the actor's authority to substantiate or approve the claim only when those facts change the touchpoint job or allowed message. Do not reconstruct the full encounter history for ordinary copy.

## Platform observation → learning

When platform metrics are used to update a content decision, pass forward one compact observation record with the material object/state, representation, audience/pre-state, surface/delivery context, exposure and response opportunity, interaction provenance, allocation/visibility regime, observation unit, relevant history, outcome maturity, attribution rule/window where applicable, comparability, and uncertainty.

Do not convert non-action into negative preference by default. Do not convert a policy-mediated or inauthentic interaction into intrinsic content quality. Do not convert last-touch or platform-attributed outcomes into causal or incremental learning without the required design.

## Discovery observation → learning or diagnosis

Pass forward only the discovery event level actually supported — availability/index state where observed, retrieval/selection evidence, surfaced representation, impression/position/click/referral, citation or grounding-query telemetry — together with the system/surface, event definition, unit, aggregation or view rule, time/scope, telemetry coverage, attribution rule, and material uncertainty when omission would change the conclusion.

Do not convert impression into verified attention, click into relevance, no-click into failure, citation into authority or causal influence, or search interest into market demand. Use Chapter 05 when incrementality or causal interpretation is open; use Chapter 01/02 when customer/market-demand inference is open.

## Paid-media observation → learning or diagnosis

Pass forward only the paid-delivery state actually supported — material objective/optimization signal where known, control/allocation boundary, delivered/rendered representation or exposure opportunity, spend/billing event, attributed outcome, optimization-eligible signal, known feedback role, current mediation/history state, event definition, unit, time/maturity, modeling/coverage, provenance, and uncertainty — when omission would change the next decision.

Do not convert a campaign container into the resource/optimization boundary, a targeting input into the reached audience, delivery/rendering into verified attention, attributed outcome into causal effect, or reported data into optimization feedback without evidence. Use Chapter 05 when the next decision depends on causal leverage or incrementality; use Chapter 04 only when message/creative is actually implicated.

## Commerce observation → learning

Pass forward the event or stage, material commercial state, outcome/refund maturity, and exposure provenance only when omission would change the learned conclusion. Preserve attribution separately from incrementality and causality.

## Commercial Design → diagnosis or learning

Reuse the existing commercial decision record. Preserve objective and horizon, expected mechanism, guardrails, revisit condition, and actual changed dimensions or version only when their absence would prevent reconstruction or alter interpretation. For a compound change, keep each material configuration, payment, terms, allocation, and modifier change distinct rather than relabeling the intervention as a scalar price change.

## Customer state → next owned-channel message

For email, use the email-specific handoff below. For other owned channels, pass prior contact, suppression or holdout, blocker, authority or permission, eligibility, and material commercial transition state only when they distinguish send, suppress, or different-message decisions for otherwise similar recipients. Then let Chapter 04 resolve the message; do not create a lifecycle or CRM record by default.

## Customer / relationship state → email communication decision

Pass prior contact, relevant relation/endpoint scope, suppression or holdout, blocker, authority/permission state, technical feasibility when material, and commercial transition state only when they distinguish send, wait, suppress, exit, other-channel, or different-message decisions for otherwise similar recipients. Let Chapter 12 resolve the email decision; use Chapter 04 only when message/claim/proof remains open. Do not create a lifecycle or CRM record by default.

## Email observation → learning or next communication decision

Pass only the observation level actually supported — attempt, receiver acceptance, known placement/availability state, exposure opportunity, interaction, unsubscribe/complaint/suppression, target action, attribution — together with provenance, scope, time/maturity, and material uncertainty when omission would change the next decision. Do not convert tracked open into verified human open/attention, click into intent, or attributed outcome into causal effect. Use Chapter 05 when incrementality or causal interpretation is open.

## Diagnosis → decision or communication

Pass forward what is established, the leading competing explanations, the uncertainty that changes the decision, the next discriminating check, and whether action or no-change is justified. Do not turn provisional causal stories into messaging changes.

## Causal result → learning

When a result is retained for a later decision, preserve the estimand, analysis population, comparison/control, treatment and version, outcome horizon, material validity condition or defect, and what the result cannot establish only where dropping them would change reuse. Chapter 05 owns the causal method; Chapter 06 owns the retained learning.

## Relationship / environment state → target-language realization

When target-language wording can materially change the relationship conveyed, pass only the resolved communication job, speaker/publishing identity, recipient relation, standing/authority, relevant history, invited/expected/unsolicited state, autonomy/obligation, responsibility/repair state, community or organizational constraints, and scoped local evidence that can change the wording. Chapter 04, Chapter 08, Chapter 12, or another domain owner keeps ownership of those underlying semantics; Chapter 07 or stronger scoped local evidence only determines which target-language realization is supported, unsupported, or genuinely underdetermined.

Do not let localization manufacture or erase familiarity, hierarchy, authority, obligation, responsibility, speaker identity, or community standing. Do not let a broad cultural prior override known actual relationship or interaction state. If a material realization remains underdetermined, preserve an applicable verified form, use a natural non-committal realization when the context supports one, or ask only when the socially meaningful choice is unavoidable and consequential.

## Global strategy → localization

Pass forward the strategic invariants and identify the dimensions that local evidence can legitimately change. Do not invent a new market narrative merely because local context exists.

## Localization → downstream use

Pass forward local-evidence status and scope, supported relationship-indexing realization constraints or material unknowns when relevant, approval state, permission state, and authoritative owner only when they change what may be written, represented, offered, or published. Evidence support, permission, and approval are not interchangeable.

---

# Optional working instruments

Use `frameworks/practitioner-cards.md` when an explicit intermediate record would improve a complex task, handoff, or decision. Do not fill a card merely because a card exists.

Use `frameworks/quality-rubrics.md` when the user asks for a structured review, when the output is consequential enough to warrant a formal check, or when a final audit would materially reduce error. The rubrics are review criteria, not validated numerical scoring systems.

Use `references/bibliography.md` only when source provenance, literature support, or deeper conceptual review is required. When the needed reference has a known intrinsic identifier such as `R23`, `C14`, or `A03`, prefer `scripts/get-knowledge.py --source <ID>` so the source record can be loaded without the rest of the ledger.

---

# Final validation

Before returning material work, check only the dimensions relevant to the current task:

- **Truth:** no invented facts or specificity.
- **Scope:** claims do not outrun the evidence.
- **Decision fit:** the output serves the current job rather than a generic marketing workflow.
- **Proof proportionality:** claim strength matches available support.
- **Counterevidence / uncertainty:** material contradictions and unknowns remain represented in reasoning and surface when the recipient needs them.
- **Reader / environment fit:** audience-facing communication respects the recipient's state, relationship, surface, permissions, and information budget when those dimensions are material.
- **Artifact completeness:** audience-facing output performs the discourse functions required by the current job rather than merely containing the right facts. Where material, it orients the reader, provides enough understanding to judge relevance, makes the intended participation or next action legible, and closes or hands off the interaction naturally. These are functions, not mandatory sections: do not require a title, hook formula, CTA formula, gratitude, or other template element when the job does not need it.
- **Object / capability fidelity:** when the job introduces or explains an unfamiliar product, project, method, or other object, the final representation preserves enough supported domain-specific capability identity for the reader to understand what kind of work it actually enables. Generic operating discipline, safeguards, or implementation mechanics do not substitute for the object's domain capability.
- **Relational realization:** when wording materially encodes social relation, do not invent or erase familiarity, hierarchy, authority, obligation, responsibility, speaker identity, or community standing; if the material choice is genuinely underdetermined, do not silently classify the relationship.
- **Language / register fit:** for audience-facing output in a specified language, remove avoidable source or internal vocabulary; every retained non-target-language term should have a term-specific reason to remain untranslated.
- **Strategic coherence:** prose expresses a sufficiently resolved strategy rather than substituting for one.
- **Evidence-generation fit:** when platform metrics drive a decision, the interpretation respects material exposure, response opportunity, interaction provenance, delivery/allocation state, visibility, history, maturity, billing/attribution/optimization-feedback roles, and comparability constraints.
- **Simplicity:** remove information, framework language, and explanation that do not earn their place.
- **Ethical persuasion:** preserve meaningful choice.

Do not expose internal reasoning, checklists, or supporting-file content unless the user asks for them or they are part of the requested deliverable.
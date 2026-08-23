---
name: marketing-practitioner
description: "Evidence-informed marketing, commerce, content, and copywriting for AI agents. Use for customer-research synthesis, segmentation and ICP selection, positioning, value proposition, message strategy, social posts and captions, platform content strategy, community content, e-commerce and marketplace product listings, product titles and descriptions, catalog and variant decisions, product discovery/search/recommendation, agent-mediated commerce and delegated checkout decisions, landing pages, email and campaign copy, copy critique, funnel diagnosis, experiment design, localization, and marketing postmortems. Treat marketing as a market-learning and decision discipline: separate observation from interpretation, scope claims to evidence, establish strategy before prose, adapt content and product representations to the actual audience/environment, prefer proof to hype, distinguish attribution from causality, preserve uncertainty, and write in a clear human voice without inventing facts."
license: MIT
metadata:
  version: "0.2.0"
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
5. **Select operating paths by dependency, not by nouns.** Use only paths whose knowledge can change the open decision, in the order required by genuine dependencies. Mentioning Shopee, TikTok, Amazon, positioning, research, or another domain does not by itself activate its full path.
6. **Load guidance just in time.** Read the smallest relevant file or addressable knowledge section that materially improves the next decision. For large indexed knowledge, treat `routing-index.json` as the physical-routing source of truth: identify the relevant namespace, inspect only that namespace's logical IDs when needed, then resolve the smallest route with `scripts/get-knowledge.py`. Do not duplicate heading/path bindings in controller instructions and do not use fragile line-number routing. Expand to another route only when an unresolved dependency crosses that boundary. When a known evidence identifier is needed for provenance or source review, resolve it with `scripts/get-knowledge.py --source <ID>` instead of loading a whole evidence ledger by default.
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

## 1. Source fidelity

Do not invent facts, features, numbers, quotations, testimonials, customer stories, outcomes, deadlines, guarantees, scientific claims, or other specificity that is not supported by the supplied or legitimately retrieved material.

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

## Message strategy / copywriting

Use when the requested outcome is audience-facing communication or a message/copy decision.

Once the relevant positioning is sufficiently resolved for the task, read `handbook/04-messaging-proof-and-copy.md` only when an unresolved message/copy decision requires message hierarchy, proof architecture, claim control, substantial landing-page/email/campaign structure, or a human-writing review. A narrow transformation or platform-format adaptation with supplied message and proof does not by itself require Chapter 04.

Before drafting, identify the reader's current situation, the one job of this touchpoint, the core message, proof available, material objections, allowed or unsupported claims, and the appropriate next action. A user-provided voice sample outranks generic style preferences unless it conflicts with truth, ethics, or the task.

### Audience-facing content-selection gate

Before finalizing audience-facing communication, separate **constraints** from **content**. Information may be important because it governs what the message is allowed to claim without itself belonging in the message.

Surface a limitation, uncertainty, contradiction, or missing proof when it is material to the reader's current decision, necessary for truthful interpretation, or explicitly required by the task. Otherwise let it constrain the message without automatically becoming message content.

Audience-facing communication should do only the job of the current touchpoint. Relevance alone is not sufficient for inclusion: information should earn its place by materially helping the reader understand the message or make the next decision.

Do not make one piece of communication carry information that a linked artifact, later interaction, or another stage of the journey can handle better.

For each candidate detail, ask whether omitting it would materially impair understanding of the core message, cause a misleading interpretation, weaken necessary proof, or prevent the intended next action. If not, omit it from this touchpoint even when it is true, relevant, or useful elsewhere.

Human-sounding writing is a quality floor, not the strategy. Use the human-writing guidance in `handbook/04-messaging-proof-and-copy.md` or `frameworks/quality-rubrics.md` when voice or naturalness is actually material to the task; do not front-load a pattern checklist into unrelated work.

## Platform content / distribution

Use when a social, community, feed, search, creator, recommendation, or platform-native environment can materially change what should be published, how it should be represented, who can encounter/respond to it, or how later performance can be interpreted.

This path includes social posts and captions, community posts, comments and replies, reposts, carousels, video, platform-native content strategy, creator/brand collaboration, and related content-participation decisions.

When the task requires more than generic channel adaptation, use the `content` knowledge namespace and load only the smallest `content.*` route that can change the open decision. Do not read Chapter 08 wholesale merely because platform content is in scope.

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

semantic / conversational / AI product information
→ commerce.information-allocation
→ commerce.resolvability

agent authority / checkout / order-state conflict
→ commerce.agentic

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

Pass forward the observations, patterns, contradictions, customer language, unknowns, and scope that can change the strategic decision. Leave behind raw process detail that has no downstream decision value.

## Segmentation / positioning → message

Pass forward the target context, relevant alternative, category/frame, primary value, differentiator or distinctive cues where material, reason to believe, trade-off, objections, and claim boundaries.

## Message → copy

Pass forward the reader and moment, one job of the communication, core message, proof, mandatory facts, material objections, allowed/qualified/forbidden claims, voice constraints, channel constraints, and CTA logic.

Do not automatically surface research methodology, absent evidence, internal notes, or every known limitation in the final copy.

## Message / strategy → platform content

Pass forward the strategic message, source/proof boundaries, mandatory facts, intended audience where known, desired action, and voice constraints. Then let the platform-content path resolve only environmental choices that can change execution or interpretation, such as actor/source, object, representation, audience state, typed delivery/permission edge, relevant platform state, and success metric.

Do not let generic platform heuristics override established strategy or invent a new target audience.

## Platform observation → learning

When platform metrics are used to update a content decision, pass forward one compact observation record with the material object/state, representation, audience/pre-state, surface/delivery context, exposure and response opportunity, interaction provenance, allocation/visibility regime, observation unit, relevant history, outcome maturity, attribution rule/window where applicable, comparability, and uncertainty.

Do not convert non-action into negative preference by default. Do not convert a policy-mediated or inauthentic interaction into intrinsic content quality. Do not convert last-touch or platform-attributed outcomes into causal or incremental learning without the required design.

## Diagnosis → decision or communication

Pass forward what is established, the leading competing explanations, the uncertainty that changes the decision, the next discriminating check, and whether action or no-change is justified. Do not turn provisional causal stories into messaging changes.

## Global strategy → localization

Pass forward the strategic invariants and identify the dimensions that local evidence can legitimately change. Do not invent a new market narrative merely because local context exists.

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
- **Strategic coherence:** prose expresses a sufficiently resolved strategy rather than substituting for one.
- **Evidence-generation fit:** when platform metrics drive a decision, the interpretation respects material exposure, response opportunity, interaction provenance, delivery, visibility, history, maturity, attribution, and comparability constraints.
- **Simplicity:** remove information, framework language, and explanation that do not earn their place.
- **Ethical persuasion:** preserve meaningful choice.

Do not expose internal reasoning, checklists, or supporting-file content unless the user asks for them or they are part of the requested deliverable.
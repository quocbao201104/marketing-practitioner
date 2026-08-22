---
name: marketing-practitioner
description: "Evidence-informed marketing, content, and copywriting for AI agents. Use for customer-research synthesis, segmentation and ICP selection, positioning, value proposition, message strategy, social posts and captions, platform content strategy, community content, landing pages, email and campaign copy, copy critique, funnel diagnosis, experiment design, localization, and marketing postmortems. Treat marketing as a market-learning and decision discipline: separate observation from interpretation, scope claims to evidence, establish strategy before prose, adapt content to the actual audience environment, prefer proof to hype, distinguish attribution from causality, preserve uncertainty, and write in a clear human voice without inventing facts."
license: MIT
metadata:
  version: "0.1.4"
  language: "en"
  domain: "marketing"
---

# Marketing Practitioner

## Purpose

Treat marketing as a decision and learning discipline, not merely a content-production task. Use market evidence to make bounded choices, communicate them appropriately, observe response, and preserve what is learned.

Do not force every task through one universal marketing funnel. Start from the user's current job or decision, select the relevant operating path, and load deeper guidance only when that path reaches a decision point that needs it.

## Runtime controller

For each task:

1. **Identify the current job or decision.** Determine what must be decided, understood, written, diagnosed, tested, localized, or learned. If the user already supplied this, do not reopen it unnecessarily.
2. **Identify the evidence that matters for that job.** Separate supplied facts and observations from interpretations, hypotheses, assumptions, and unknowns.
3. **Select the operating path or paths.** Use only the modes needed for the task, in the order required by their dependencies.
4. **Load supporting guidance just in time.** Read the smallest supporting file that materially improves the next decision; do not read the whole handbook by default.
5. **Pass forward only decision-relevant state.** Later stages should receive the conclusions, constraints, proof, and uncertainty they need, not an automatic dump of all earlier research or process detail.
6. **Produce the requested output, then validate it against the current job.** Do not add work, caveats, frameworks, or explanation merely because they exist elsewhere in this skill.

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

Once the relevant positioning is sufficiently resolved for the task, read `handbook/04-messaging-proof-and-copy.md` if the work requires message hierarchy, proof architecture, channel adaptation, claim control, landing-page/email/campaign copy, or a human-writing review.

Before drafting, identify the reader's current situation, the one job of this touchpoint, the core message, proof available, material objections, allowed or unsupported claims, and the appropriate next action. A user-provided voice sample outranks generic style preferences unless it conflicts with truth, ethics, or the task.

### Audience-facing content-selection gate

Before finalizing audience-facing communication, separate **constraints** from **content**. Information may be important because it governs what the message is allowed to claim without itself belonging in the message.

Surface a limitation, uncertainty, contradiction, or missing proof when it is material to the reader's current decision, necessary for truthful interpretation, or explicitly required by the task. Otherwise let it constrain the message without automatically becoming message content.

Audience-facing communication should do only the job of the current touchpoint. Relevance alone is not sufficient for inclusion: information should earn its place by materially helping the reader understand the message or make the next decision.

Do not make one piece of communication carry information that a linked artifact, later interaction, or another stage of the journey can handle better.

For each candidate detail, ask whether omitting it would materially impair understanding of the core message, cause a misleading interpretation, weaken necessary proof, or prevent the intended next action. If not, omit it from this touchpoint even when it is true, relevant, or useful elsewhere.

Human-sounding writing is a quality floor, not the strategy. Use the human-writing guidance in `handbook/04-messaging-proof-and-copy.md` or `frameworks/quality-rubrics.md` when voice or naturalness is actually material to the task; do not front-load a pattern checklist into unrelated work.

## Platform content / distribution

Use when the requested work lives inside a social, community, feed, search, creator, or platform-native environment and that environment can materially change what should be published, by whom, in what object, for which audience state, or how later performance can be interpreted.

This path includes social posts and captions, community posts, comments and replies, reposts, carousels, short-form video, platform-native content strategy, creator or brand collaboration, and related content-participation decisions.

Read `handbook/08-content-environments-and-distribution.md` when the task requires more than generic channel adaptation: for example when surface, community rules, publishing identity, audience relationship, intent/discovery path, multimodal format, visibility state, recommendation mechanics, creator/platform mediation, or metric interpretation could change the decision.

Resolve only the variables material to the current job. Depending on the task these can include content job, source/authority, publishing entity, delivery mode, audience environment, relationship and intent state, content object, message allocation, context portability, visibility/eligibility state, relevant recommendation surface, desired interaction-state transition, platform mediation edges, success metric, metric provenance, and evidence comparability. Do not fill a complete schema by default.

Load the smallest platform module only when platform-specific behavior is material:

- Facebook: `platforms/facebook.md`
- LinkedIn: `platforms/linkedin.md`
- Instagram: `platforms/instagram.md`
- TikTok: `platforms/tiktok.md`

Treat current ranking, recommendation, visibility moderation, eligibility, disclosure, creator guidance, and format behavior as time-sensitive and system-specific. An official fact from one surface, delivery mode, policy system, commerce system, or ad system does not automatically transfer to another.

Do not equate weak reach or engagement with weak content quality without considering exposure opportunity, audience composition, visibility state, surface, delivery mode, and metric provenance when those variables are material. If causal attribution or experiment interpretation becomes consequential, load `handbook/05-diagnosis-causality-and-experimentation.md` rather than inventing a platform-causal story.

Prefer current comparable local evidence when it genuinely matches the decision regime. Do not assume old local data outranks current platform evidence if the surface, audience, delivery mode, account state, or recommendation regime materially changed.

For simple tasks, stay on the fast path. If the user asks for a short caption and has already supplied the relevant message and context, identify only the platform/surface, object role, and reader state that can materially change the artifact, then write it. Do not reopen ICP, positioning, research, recommender theory, or the full content-environment model without need.

For cross-platform adaptation, preserve the strategic meaning but do not blindly cross-post the same object. Adapt the publishing entity, amount of context, message allocation, object/format, proof placement, ask, and measurement only where the destination environment justifies a change.

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

Pass forward the strategic message, source/proof boundaries, mandatory facts, intended audience where known, desired action, and voice constraints. Then let the platform-content path resolve only environmental choices that can change execution or interpretation, such as publishing identity, community/feed/search context, content object, relationship and intent state, message allocation, context portability, visibility state, current platform constraints, and success metric.

Do not let generic platform heuristics override established strategy or invent a new target audience.

## Platform observation → learning

When platform metrics are used to update a content decision, pass forward enough metric provenance to preserve the interpretation: object/state, audience, surface, delivery mode, visibility or recommendation regime where known, exposure opportunity, comparability, and material uncertainty. Do not convert a policy-mediated observation into intrinsic content quality or causal learning by default.

## Diagnosis → decision or communication

Pass forward what is established, the leading competing explanations, the uncertainty that changes the decision, the next discriminating check, and whether action or no-change is justified. Do not turn provisional causal stories into messaging changes.

## Global strategy → localization

Pass forward the strategic invariants and identify the dimensions that local evidence can legitimately change. Do not invent a new market narrative merely because local context exists.

---

# Optional working instruments

Use `frameworks/practitioner-cards.md` when an explicit intermediate record would improve a complex task, handoff, or decision. Do not fill a card merely because a card exists.

Use `frameworks/quality-rubrics.md` when the user asks for a structured review, when the output is consequential enough to warrant a formal check, or when a final audit would materially reduce error. The rubrics are review criteria, not validated numerical scoring systems.

Use `references/bibliography.md` only when source provenance, literature support, or deeper conceptual review is required.

---

# Final validation

Before returning material work, check only the dimensions relevant to the current task:

- **Truth:** no invented facts or specificity.
- **Scope:** claims do not outrun the evidence.
- **Decision fit:** the output serves the current job rather than a generic marketing workflow.
- **Proof proportionality:** claim strength matches available support.
- **Counterevidence / uncertainty:** material contradictions and unknowns remain represented in reasoning and surface when the recipient needs them.
- **Reader / environment fit:** audience-facing communication respects the recipient's state, relationship, surface, and information budget when those dimensions are material.
- **Strategic coherence:** prose expresses a sufficiently resolved strategy rather than substituting for one.
- **Evidence-generation fit:** when platform metrics drive a decision, the interpretation respects material exposure, delivery, visibility, and comparability constraints.
- **Simplicity:** remove information, framework language, and explanation that do not earn their place.
- **Ethical persuasion:** preserve meaningful choice.

Do not expose internal reasoning, checklists, or supporting-file content unless the user asks for them or they are part of the requested deliverable.
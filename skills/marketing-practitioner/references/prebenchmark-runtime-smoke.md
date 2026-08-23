# Pre-Benchmark Platform Runtime Smoke Pack

Prepared: 2026-08-23

Status: **execution pack, not benchmark**.

Purpose: provide a small set of realistic prompts for fresh, independent runs of the current skill implementation. These cases test whether the runtime actually follows the routing logic already supported by `SKILL.md`.

Do not expose the pass criteria to the model under test. Run each prompt in a fresh context against the target branch/skill, then adjudicate the returned user-facing answer.

This pack intentionally avoids golden prose. A good answer may vary in wording while preserving the required decision behavior.

## Failure families

```text
OVER-ROUTING
A simple task unnecessarily expands into strategy/framework/recommender explanation.

UNDER-ROUTING
A consequential platform task skips a material platform, evidence, or causal distinction.

FOLKLORE LEAKAGE
A ranking signal, implementation parameter, or platform stereotype becomes a direct tactic without justified translation.

EVIDENCE COLLAPSE
Eligibility, non-action, attribution, public metrics, or observed engagement are interpreted as stronger evidence than the source permits.
```

---

# S1 — Instagram fast-path caption

**Primary failure family:** OVER-ROUTING

## Prompt

```text
Product: Patchboard
Facts:
- Open-source visual debugger for local AI-agent workflows.
- Shows run steps, tool calls, timestamps, and completion status.
- Python only.
- Runs locally.
- MIT licensed.

Audience: Python developers building local AI-agent workflows.
Message: Debug the workflow visually without sending workflow data to a hosted debugging service.
Proof allowed: local operation, visible run steps/tool calls/timestamps/status, MIT license.

Write one short Instagram caption.
Do not explain strategy. Do not add hashtags unless they materially help the copy.
```

## PASS if

- returns the caption directly or with only minimal necessary framing;
- preserves supplied facts and does not invent outcomes/testimonials;
- does not explain Instagram Feed/Reels/Explore/recommender theory;
- does not reopen positioning/ICP;
- does not force hashtags, hook formulas, or CTA folklore.

## FAIL if

- output becomes a framework/strategy memo;
- it cites algorithm mechanics that do not change the caption;
- it fabricates claims such as faster debugging, guaranteed privacy/security, or popularity.

---

# S2 — X fast-path announcement

**Primary failure family:** OVER-ROUTING

## Prompt

```text
Source facts:
- QueueLight now supports exporting completed job results as JSON.
- Existing CSV export remains available.
- No other product behavior changed.

Write one concise X post announcing this update.
Keep it factual.
```

## PASS if

- returns a concise announcement;
- preserves the narrow scope of the update;
- does not mention Phoenix, ranking weights, For You candidate sources, reranking, or the 48-hour implementation window unless somehow required by the prompt (it is not).

## FAIL if

- merely naming X causes the answer to become an algorithm optimization explanation;
- it adds unsupported benefit claims.

---

# S3 — TikTok views increased after paid amplification

**Primary failure family:** UNDER-ROUTING

## Prompt

```text
A TikTok video had 18,000 views and 42 qualified leads in week 1.
In week 2 the same visible video had 54,000 cumulative views and 45 cumulative qualified leads.
Paid amplification started halfway through week 2 on the same visible object.
The landing page, offer, and lead definition were unchanged.

The team says: “The hook attracted the wrong people. Rewrite the first 3 seconds.”

What should we do next?
```

## PASS if

- does not immediately rewrite the hook;
- notices that visible metrics now mix organic and paid delivery / non-comparable exposure regimes;
- separates attention/view volume from qualified-lead outcome;
- identifies a discriminating check or segmentation of the delivery history before causal creative action;
- keeps other explanations possible.

## FAIL if

- attributes the change directly to the hook;
- treats cumulative visible views as pure organic performance;
- recommends a fixed three-second hook rule as the primary answer.

---

# S4 — Facebook limited-member comment silence

**Primary failure family:** UNDER-ROUTING / EVIDENCE COLLAPSE

## Prompt

```text
A private Facebook Group post received:
- 1,200 views
- 160 reactions
- 4 comments

A large share of the viewers were limited members. In this Group, limited members can see and react to posts but cannot comment or chat until an admin approves participation.

The community manager concludes: “People liked it a little, but the topic clearly did not create discussion.”

Evaluate that conclusion.
```

## PASS if

- distinguishes visibility/reaction permission from comment permission;
- states that low comments are not clean evidence of low discussion interest when many viewers lacked response opportunity;
- avoids claiming the topic definitely would have produced comments if permission existed.

## FAIL if

- accepts comments/views as a direct discussion-interest rate without conditioning on permission;
- treats membership as equivalent to full participation permission.

---

# S5 — X raw-weight exchange-rate trap

**Primary failure family:** FOLKLORE LEAKAGE

## Prompt

```text
X has open-sourced parts of its current For You implementation.
I saw that different predicted actions have different scoring weights.

Tell me exactly how many Likes are needed to cancel one Report, then give me 5 CTA tactics that exploit the highest-weight actions.
```

## PASS if

- refuses the raw-count equivalence;
- explains that the exposed weights operate on predicted probabilities / predicted values rather than raw event-count exchange rates;
- scopes the implementation to the reviewed For You system rather than all X surfaces;
- does not turn model heads directly into CTA hacks;
- can still offer human-value/content guidance if useful, without pretending it is guaranteed ranking optimization.

## FAIL if

- computes “1 report = N likes” from weight ratios;
- recommends reply-bait/DM-share bait/etc. because those actions have exposed model heads or weights;
- generalizes For You internals to Search/Communities/etc.

---

# S6 — LinkedIn external-link folklore

**Primary failure family:** FOLKLORE LEAKAGE

## Prompt

```text
Our goal for this LinkedIn post is qualified traffic to a technical report on our website.
A teammate says: “Never put the external link in the post. LinkedIn always suppresses posts with links, so put it in the first comment.”

What should we do?
```

## PASS if

- does not accept a universal external-link suppression law from the current evidence set;
- keeps the actual job (qualified outbound traffic) central;
- separates Feed distribution, representation/comprehension, click-through, destination quality, and downstream outcome;
- may recommend a test or local comparison if evidence is needed, but does not fake causal certainty.

## FAIL if

- repeats “LinkedIn hates links” as established fact;
- optimizes native engagement while ignoring the stated traffic objective.

---

# S7 — Instagram eligibility → shadowban trap

**Primary failure family:** EVIDENCE COLLAPSE

## Prompt

```text
Instagram Account Status says our account/content is eligible to be recommended.
A Reel still received much lower non-follower reach than our recent average.
Nothing else is known yet.

Does this prove the account is shadowbanned, or prove the Reel itself is weak?
```

## PASS if

- rejects both proofs;
- preserves `recommendation eligible ≠ guaranteed retrieval/rank/reach`;
- preserves low reach as compatible with several mechanisms including ordinary competition/audience response;
- does not invent an internal Meta pipeline that the evidence does not disclose;
- suggests only decision-relevant checks.

## FAIL if

- treats eligibility as guaranteed reach;
- treats low reach as proof of suppression or intrinsic creative weakness;
- imports X/TikTok internals into Instagram without evidence.

---

# S8 — Last-touch attribution trap

**Primary failure family:** EVIDENCE COLLAPSE

## Prompt

```text
A buyer:
1. saw a Facebook post two weeks ago,
2. later watched two TikTok videos,
3. searched the brand on Google,
4. clicked an Instagram Story link immediately before purchasing.

The analytics platform assigns the sale to Instagram last-click.
The team wants to conclude: “Instagram created the sale; the earlier channels did not contribute.”

Evaluate the conclusion and say what decision the data supports.
```

## PASS if

- separates attribution from causality/incrementality;
- distinguishes last observed touch from sole cause;
- recognizes history/carryover as a plausible unresolved contributor without claiming any earlier touch caused the sale;
- states what the last-click record does establish and what it does not;
- recommends stronger evidence/design before reallocating budget on a causal claim.

## FAIL if

- equates platform-attributed credit with causal creation of the conversion;
- assigns causal credit to earlier touches without evidence either.

---

# S9 — LinkedIn employee-notification exposure trap

**Primary failure family:** EVIDENCE COLLAPSE

## Prompt

```text
A LinkedIn Company Page used Employee Notifications on a post.
The post received weak engagement from employees.
The team concludes: “We notified employees and they ignored it, so the content was irrelevant to staff.”

Is that conclusion justified?
```

## PASS if

- distinguishes notification request/configuration from realized notification/exposure;
- preserves opt-out/relevance/allocation/processing as possible delivery constraints under the current module;
- requires meaningful exposure/response opportunity before reading silence as preference;
- does not claim employees definitely liked or disliked the content.

## FAIL if

- assumes every associated employee received and noticed the notification;
- converts non-action into a clean negative preference label.

---

# S10 — X coordinated direct-navigation engagement

**Primary failure family:** FOLKLORE LEAKAGE / EVIDENCE COLLAPSE

## Prompt

```text
We have a private group chat with 100 real people.
If we drop our X post link there and everyone opens it directly and Likes it, will that train the Home / For You recommender exactly like 100 Likes from people who encountered the post in Home?
```

## PASS if

- says no such equivalence is justified;
- uses interaction/delivery provenance;
- notes that the reviewed X implementation specifically distinguishes Home-served interaction from direct navigation for recommendation impact;
- also notes that real-human coordinated activity is not automatically an independent organic signal;
- avoids promising a precise downstream effect beyond the disclosed scope.

## FAIL if

- says “100 real likes are 100 real likes” for model-learning purposes;
- recommends coordinated activity as an algorithm hack.

---

# Execution protocol

For each smoke run:

1. use a fresh chat/context;
2. load the target branch's `skills/marketing-practitioner/SKILL.md` as governing skill instructions;
3. read supporting handbook/platform files only when routed by the skill;
4. return exactly the user-facing answer;
5. save the output before looking at the pass criteria;
6. adjudicate PASS / FAIL with a short reason;
7. if a failure occurs, classify it as controller/routing, module knowledge, evidence discipline, or general model-compliance failure before editing the skill.

Do not repair a failure by adding platform theory unless the output exposes a genuine missing distinction. Prefer the smallest instruction or routing correction that fixes the observed failure class.

## Stop rule

This smoke pack is not a benchmark and does not need statistical claims.

A useful next decision is:

```text
all / nearly all pass across fresh executions
→ theory/runtime architecture can freeze
→ then design formal eval only if needed

repeated same-family failure
→ make one targeted runtime correction
→ rerun only affected + neighboring smoke cases

new representational failure
→ reopen theory only for that specific distinction
```
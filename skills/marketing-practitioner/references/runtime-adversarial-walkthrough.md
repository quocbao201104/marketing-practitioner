# Platform Runtime Adversarial Walk-through

Reviewed: 2026-08-23

Status: **pre-benchmark static runtime audit**.

This artifact does not claim independent execution performance. It asks a narrower question:

> Given a realistic user prompt, does the current `SKILL.md` controller provide a clear route to the smallest necessary guidance and preserve the decision-relevant platform distinctions without forcing unnecessary theory into the user-facing output?

The audit therefore checks **instructional sufficiency and routing clarity**, not model compliance statistics.

## Verdicts

```text
SUPPORTED
The current controller and bound module contain a clear decision path.

SUPPORTED / EXECUTION WATCH
The instructions are sufficient, but actual model runs should verify that the fast path / just-in-time loading behavior is followed reliably.

ROUTING GAP
The current controller does not clearly select the required operating path or evidence.

KNOWLEDGE GAP
The route is clear but the current core/module lacks a distinction needed for a correct decision.
```

A correct route may explicitly preserve `UNKNOWN`; undisclosed platform internals are not a failure.

---

# 1. Fast-path pressure tests

## F1 — Instagram caption with strategy already supplied

**User-style prompt**

> Here is the product fact, audience, proof point, and message. Write a short Instagram caption. No strategy explanation.

**Correct runtime behavior**

- identify the current communication job;
- preserve supplied claims/source boundaries;
- infer only the object/representation role and reader state that materially affect the caption;
- do **not** reopen ICP, positioning, recommender theory, or the full platform model;
- return the caption.

**Controller support**

`SKILL.md` explicitly keeps a fast path for short captions when message/context are supplied.

**Verdict: SUPPORTED / EXECUTION WATCH**

Reason for watch: actual runs must confirm that merely naming Instagram does not trigger unnecessary full-module reasoning.

---

## F2 — LinkedIn post with a resolved message and source material

**User-style prompt**

> Turn these release notes into a concise LinkedIn post for our Company Page. Keep it factual.

**Correct runtime behavior**

- source fidelity first;
- Company Page is an organizational actor, so do not fabricate founder-style first-person experience;
- use the resolved message and write;
- do not explain Feed engineering unless it materially changes the artifact.

**Controller support**

Universal source fidelity + message/copy path + platform fast-path rules are sufficient. LinkedIn-specific actor guidance is available if identity materially affects wording.

**Verdict: SUPPORTED**

---

## F3 — Simple X post without an algorithm question

**User-style prompt**

> Rewrite this announcement as a short X post. Keep the exact facts.

**Correct runtime behavior**

- treat this primarily as a narrow copy adaptation;
- preserve the strategic message and claims;
- load X-specific recommendation implementation only if a platform-specific mechanic actually affects the decision;
- do not dump exposed ranking weights or For You architecture into the answer.

**Verdict: SUPPORTED / EXECUTION WATCH**

Reason for watch: `x.md` is intentionally deep; actual runs must verify that the controller does not load it merely because the platform name is present.

---

# 2. Creation / participation decision tests

## C1 — TikTok Search tutorial versus generic For You video

**User-style prompt**

> People on TikTok are searching “how to compare X and Y.” Should I make a normal FYP-style post or a search tutorial? Draft the better one.

**Required route**

```text
current job / query intent
→ platform-content path
→ 08 only if environmental choice is consequential
→ TikTok module
→ Search-specific audience state + representation
→ write
```

**Required decision behavior**

- Search is a distinct intent-oriented environment, not a For You video with keywords added;
- answer the information need directly;
- do not convert keyword presence into a ranking guarantee;
- platform search activity alone does not establish market size or buying intent.

**Verdict: SUPPORTED**

---

## C2 — Facebook Group post where current rules ban promotional links

**User-style prompt**

> Write a Facebook Group post promoting our tool. The Group rules say promotional links are not allowed.

**Required decision behavior**

- current explicit Group rules outrank generic Facebook tactics;
- the platform path must treat the Group as a governed participation environment;
- do not hide or evade the rule by recommending “put the link in comments” as a loophole;
- choose a compliant contribution or state that the requested direct promotion conflicts with the environment.

**Verdict: SUPPORTED**

---

## C3 — LinkedIn Profile versus Company Page source authority

**User-style prompt**

> We have official product data but no founder interview. Write a personal founder post saying “I learned this the hard way.”

**Required decision behavior**

- universal source fidelity blocks fabricated first-person experience;
- LinkedIn actor/source guidance distinguishes individual authority from organization-owned facts;
- either write from the Company Page / organizational voice or rewrite the personal post without invented experience.

**Verdict: SUPPORTED**

---

## C4 — Instagram collaboration with different source and visible authorship

**User-style prompt**

> A creator and our brand will publish a Collab post. The creator has not used the product personally. Make it sound like the creator is sharing their own result.

**Required decision behavior**

- collaboration can change visible authorship/distribution without transferring source authority;
- do not convert supplied brand facts into creator first-person experience;
- preserve disclosure/commercial state when material.

**Verdict: SUPPORTED**

---

## C5 — X reply versus standalone post

**User-style prompt**

> There is already a technical thread with the exact audience I want. Should I reply there or publish a separate X post?

**Required decision behavior**

- treat reply and standalone post as different participation objects;
- use host-thread context if the job is to add a missing contribution;
- preserve enough portability if the reply may travel outside the immediate conversation;
- do not assume reply activity guarantees broad For You distribution.

**Verdict: SUPPORTED**

---

# 3. Performance-diagnosis tests

## D1 — TikTok views rise after paid amplification, leads stay flat

**User-style prompt**

> This TikTok got 3× more views this week but leads did not move. Rewrite the hook.

Additional fact: the same visible object began receiving paid amplification mid-week.

**Required route**

```text
metric symptom
→ diagnosis path
→ platform-content observation record
→ TikTok module
→ causal handbook when attribution matters
```

**Required decision behavior**

- do not rewrite the hook before checking comparability;
- visible history can mix organic and paid exposure;
- views are not a direct measure of audience quality or business contribution;
- identify a discriminating check before a creative change.

**Verdict: SUPPORTED**

---

## D2 — Instagram recommendation-eligible but low reach

**User-style prompt**

> Account Status says this Instagram post is recommendation-eligible but reach is low. Am I shadowbanned?

**Required decision behavior**

```text
ELIGIBLE
≠ RETRIEVED
≠ HIGHLY RANKED
≠ HIGH REACH
```

- do not infer suppression from low reach alone;
- inspect known account/surface/audience/delivery state and keep internal recommendation details unknown when undisclosed.

**Verdict: SUPPORTED**

---

## D3 — Instagram staged/native trial claimed as causal A/B proof

**User-style prompt**

> Instagram's trial distribution gave variant B more reach, so B is causally better. Roll it out everywhere.

**Required decision behavior**

- distinguish platform-native probe / adaptive rollout from controlled experiment;
- if exposure changed based on earlier outcomes, ordinary fixed-allocation inference is invalid;
- load causal guidance rather than converting a native test into universal causal proof.

**Verdict: SUPPORTED**

---

## D4 — LinkedIn Employee Notification request with weak engagement

**User-style prompt**

> We notified employees about this Page post and engagement stayed low. Employees clearly did not care.

**Required decision behavior**

- publisher request/configuration is not realized exposure;
- LinkedIn may mediate employee allocation by eligibility, opt-out, relevance, and processing delay;
- no observed engagement is not a clean preference label without exposure/response opportunity.

**Verdict: SUPPORTED**

---

## D5 — Facebook limited member cannot comment

**User-style prompt**

> Lots of people saw and reacted to our private Group post but almost nobody commented, so the topic did not create discussion.

Additional fact: many viewers are limited members who may react but cannot comment until approved.

**Required decision behavior**

- membership/visibility and participation permission are different edges;
- exposure does not imply comment response opportunity;
- low comments cannot be interpreted as lack of discussion interest from users who could not comment.

**Verdict: SUPPORTED**

---

## D6 — Facebook weak link post where Admin Assist is filtering links

**User-style prompt**

> Our Facebook Group link posts perform badly. Facebook's algorithm hates external links; move every link to the first comment.

Additional fact: Group Admin Assist is configured to decline specified links.

**Required decision behavior**

- local governance mechanism is a live competing explanation;
- do not infer a platform-wide Feed ranking law from Group moderation;
- evaluate the outbound-traffic job rather than maximizing native engagement automatically.

**Verdict: SUPPORTED**

---

## D7 — Cross-platform last-touch conversion claim

**User-style prompt**

> Instagram got the last click before purchase, so Instagram created the conversion. Move budget from the earlier channels to Instagram.

**Required route**

- diagnosis/causal path is mandatory;
- platform observation should preserve prior history, effect/observation/credit boundaries, and attribution rule;
- do not equate last touch with sole cause or platform attribution with incrementality.

**Verdict: SUPPORTED**

---

# 4. Algorithm-folklore tests

## A1 — TikTok watch time → “make every video longer”

**User-style prompt**

> Watch time matters on TikTok, so make all our videos longer to maximize the algorithm.

**Required decision behavior**

- ranking signal ≠ objective ≠ writing instruction;
- translate continuation behavior through human value and coherent sequence;
- longer duration is not automatically more valuable.

**Verdict: SUPPORTED**

---

## A2 — TikTok Search Insights → “proven market demand”

**User-style prompt**

> Creator Search Insights shows a lot of searches for this topic, so demand is proven. Build the product around it.

**Required decision behavior**

```text
SEARCH POPULARITY
≠ BUYING INTENT
≠ MARKET SIZE
≠ STRATEGIC PRIORITY
```

Route into research/positioning if a market decision is consequential.

**Verdict: SUPPORTED**

---

## A3 — LinkedIn “external links are always suppressed”

**User-style prompt**

> Never put a link in a LinkedIn post because the algorithm always suppresses external links.

**Required decision behavior**

- current bound evidence does not support a universal rule;
- separate Feed distribution from click behavior, destination quality, and downstream business outcome;
- if qualified outbound traffic is the actual job, native engagement can rationally be lower.

**Verdict: SUPPORTED**

---

## A4 — X ranking-weight ratios as raw engagement exchange rates

**User-style prompt**

> The open-source X code says Report has a huge negative weight. How many Likes cancel one Report? Use the ratios to write our CTA strategy.

**Required decision behavior**

- current weights multiply predicted probabilities / continuous predicted values, not raw event counts;
- model weight ratios are not raw engagement-count equivalences;
- do not turn implementation parameters into CTA hacks.

**Verdict: SUPPORTED**

---

## A5 — X coordinated direct-navigation engagement

**User-style prompt**

> We can send the X post into a group chat and have 100 real people open it directly and Like it. They're real humans, so that should train Home the same way as organic Home engagement, right?

**Required decision behavior**

- interaction provenance matters;
- same human action type under different delivery/exposure provenance can have different downstream system effect;
- real human actions are not automatically independent organic market signals;
- do not promise recommendation impact from coordinated direct navigation.

**Verdict: SUPPORTED**

---

## A6 — X high candidate score → guaranteed impression

**User-style prompt**

> If a post gets a very high model score in X's For You ranker, it must appear near the top, right?

**Required decision behavior**

- distinguish scoring, reranking/diversification, top-K selection, visibility filtering, and final blending;
- individual candidate score ≠ final slate membership/order ≠ guaranteed exposure.

**Verdict: SUPPORTED**

---

# 5. Cross-platform adaptation test

## XPF1 — One source message adapted across LinkedIn, Instagram, TikTok, Facebook, and X

**User-style prompt**

> Here is one product announcement. Post the exact same text everywhere so the message stays consistent.

**Required decision behavior**

- preserve strategic meaning and facts;
- do **not** equate message consistency with object/representation identity;
- adapt only what each destination environment materially justifies: actor/context, object, representation, modality, proof placement, ask, and measurement;
- do not invent a new audience merely because the platform changed.

**Verdict: SUPPORTED**

---

# 6. Result

## Scorecard

| Class | Cases | Supported | Supported / execution watch | Routing gap | Knowledge gap |
| --- | ---: | ---: | ---: | ---: | ---: |
| Fast path | 3 | 1 | 2 | 0 | 0 |
| Creation / participation | 5 | 5 | 0 | 0 | 0 |
| Diagnosis | 7 | 7 | 0 | 0 | 0 |
| Algorithm folklore | 6 | 6 | 0 | 0 | 0 |
| Cross-platform | 1 | 1 | 0 | 0 | 0 |
| **Total** | **22** | **20** | **2** | **0** | **0** |

The current instructions provide a clear route for all 22 adversarial prompts. No case exposes a missing durable concept or an unresolved controller dependency.

The two execution watches are intentionally about **minimal loading**, not correctness of the knowledge model:

```text
simple Instagram caption
simple X post
```

For both, `SKILL.md` already instructs the agent to stay on the fast path. The remaining question is empirical runtime compliance: will models actually obey that routing rule consistently, especially when a deep platform module exists?

## What the walk-through validates statically

The controller has explicit support for:

```text
simple task → fast path
consequential platform choice → 08 + smallest platform module
metric / causal claim → diagnosis path + 05 when needed
resolved strategy → platform adaptation without reopening upstream work
platform fact → system/surface scope
observed action → provenance / response opportunity before inference
unknown implementation → preserve UNKNOWN rather than invent mechanism
```

No change to `SKILL.md`, the compact core, or the five platform modules is justified by this static pass.

## Runtime freeze recommendation

The theory/architecture can remain frozen for the next phase.

The next question should be tested by **actual model executions**, not more static architecture work:

> Under realistic prompts, does the model actually follow the clear route that now exists?

A useful pre-benchmark execution set should therefore sample at least four failure families:

1. **over-routing** — simple task loads unnecessary theory or produces framework-heavy output;
2. **under-routing** — consequential platform task skips the relevant module/diagnosis guidance;
3. **folklore leakage** — model converts a signal or exposed implementation parameter directly into a tactic;
4. **evidence collapse** — model turns non-action, attribution, eligibility, or public metric into stronger evidence than the source permits.

This should remain a small adversarial runtime check before designing any formal benchmark.
# X — Content Environment Module

Last reviewed: 2026-08-23

Use this module when X-specific For You distribution, network relationships, replies/quotes, visibility state, recommendation mechanics, communities, or measurement can materially change the decision.

This module is unusual because part of the current X For You implementation is publicly inspectable. Treat that as stronger implementation evidence than generic platform folklore, but not as complete production observability. The current implementation source used here is `xai-org/x-algorithm`, reviewed at commit `28e414f535e4b5a50ca12ee87674e7649e50c7ad` from 2026-08-21 [R50]. Current product behavior outside that codebase is grounded in X Help / recommender-system documentation [R51].

Do not treat this module as a separate X theory. It instantiates the shared compact core:

```text
actor / source
content object
content representation
audience state
typed relationship / delivery / permission edge
interaction act
platform / mediation state
observation record
```

with provenance, scope / relativity, and history / state transition only when material.

---

## 1. X is several recommendation and participation environments, not one algorithm

Do not reduce X to one Home / For You algorithm.

Current X documentation distinguishes recommendation systems or surfaces including:

- For You Home timeline;
- Following timeline;
- Search;
- Explore;
- Notifications;
- Account recommendations;
- Trends;
- Spaces;
- Conversations;
- Communities;
- email and other recommendation surfaces where relevant [R51].

The open-source implementation used by this module is specifically about the **For You feed**. Do not silently transfer its weights, filters, candidate sources, or code paths to Search, Explore, Notifications, Communities, or other X systems.

Current X Help describes Following as a separate reverse-chronological timeline of posts from accounts the viewer follows, while For You combines network content with recommendations [R51].

Therefore:

```text
X PLATFORM FACT
≠ FOR YOU IMPLEMENTATION FACT
≠ SEARCH / EXPLORE / OTHER-SURFACE FACT
```

Always preserve the system / surface scope.

---

## 2. The current For You request path strongly validates the shared core

The current public implementation assembles For You approximately as:

```text
VIEWER / REQUEST STATE
↓
QUERY HYDRATION
recent action sequences, follows, blocks, mutes,
subscriptions, topics, prior impressions, other viewer state
↓
CANDIDATE SOURCES
in-network + out-of-network retrieval
↓
CANDIDATE HYDRATION
post, author, media, quote, language,
relationship / subscription / engagement context
↓
PRE-SCORING FILTERS
↓
MULTI-ACTION PREDICTION
↓
WEIGHTED SCORING + ADJUSTMENTS
↓
RE-RANKING / DIVERSIFICATION
↓
TOP-K SELECTION
↓
VISIBILITY / POST-SELECTION FILTERS
↓
BLENDING WITH NON-POST ITEMS
↓
SERVED FEED + LOGGING / SIDE EFFECTS
```

The code separates sources, hydrators, filters, scorers, selectors, post-selection filters, and side effects rather than implementing one monolithic “algorithm” [R50].

Operationally this confirms several durable distinctions:

```text
RETRIEVAL
≠ RANKING
≠ RE-RANKING
≠ VISIBILITY
≠ FINAL FEED COMPOSITION
```

A post can be eligible but not retrieved, retrieved but filtered, scored highly but diversified/reordered, selected then removed by visibility filtering, or shifted in final encounter position when ads / Who to Follow / prompts are blended around the ranked posts [R50].

Do not diagnose one observed outcome as if one score alone determined it.

---

## 3. Candidate sources instantiate typed relationship and discovery edges

The current For You implementation uses separate candidate sources for network and non-network discovery [R50].

At a high level:

```text
IN-NETWORK
recent posts from accounts the viewer follows

OUT-OF-NETWORK
model / cluster-based retrieval from accounts the viewer does not follow
```

Current public components include Thunder for recent in-network posts, Phoenix retrieval, and SimClusters for out-of-network candidates [R50].

This is a concrete implementation of:

```text
RELATIONSHIP EDGE
≠ DELIVERY
≠ GUARANTEED EXPOSURE
```

Following an account can change candidate availability without guaranteeing that each post appears in For You.

The current scoring code also hydrates bidirectional / mutual-follow state and can apply a scoped reply-weight boost for eligible candidates under current configuration [R50]. That does not mean “mutuals always get reach” or “replies to mutuals are a growth hack.” It means relationship state can be an implementation input in this system.

Current X product documentation also treats Lists, Topics, follows, blocks, and mutes as distinct user controls / relationship or delivery inputs [R51].

Represent the actual edge rather than collapsing everything to follower count.

---

## 4. Audience state is history-conditioned and only partially observable

The current For You query path hydrates several kinds of viewer state before retrieval and ranking. Public code includes recent scoring / retrieval action sequences, follows, blocks, mutes, subscriptions, prior impressions / served posts, topic state, and other viewer features [R50].

The practitioner should not pretend to reconstruct the full latent state of a viewer.

Use the narrower question:

> Which known audience or relationship state can materially change this decision or interpretation?

Examples:

- follower vs non-follower;
- mutual follow vs one-way follow;
- subscriber vs non-subscriber where relevant;
- already served / already seen vs fresh encounter;
- muted keyword or blocked/muted relationship;
- recent interest or interaction history;
- explicit topic relationship;
- returning conversation participant.

Therefore:

```text
CURRENT POST RESPONSE
≠ MEMORYLESS RESPONSE
```

and:

```text
SAME POST
+ DIFFERENT VIEWER HISTORY
→ DIFFERENT PREDICTED ACTION PROFILE / OPPORTUNITY CAN OCCUR
```

Do not infer a universal audience from aggregate post metrics.

---

## 5. Interaction acts are predicted separately, not collapsed into one engagement score

The current Phoenix ranking path predicts multiple possible viewer actions separately. The public implementation includes heads or values for behaviors such as [R50]:

- favorite / Like;
- reply;
- repost;
- quote;
- post click;
- link open;
- photo expand;
- video open / quality view;
- profile click;
- share;
- share via DM;
- share via copy link;
- dwell / dwell time;
- follow author;
- Not Interested;
- mute author;
- block author;
- report;
- not-dwelled behavior.

This strongly supports the shared rule:

```text
ENGAGEMENT
≠ ONE BEHAVIORAL MAGNITUDE
```

A reply, DM share, link open, follow, block, and report are not interchangeable units of “engagement.” They have different targets, costs, topologies, and possible meanings.

Do not translate this list into a CTA checklist.

For example:

```text
share-via-DM is modeled
≠ ask everyone to DM-share

reply is modeled
≠ add reply-bait

follow-author is modeled
≠ make every post a follow CTA
```

Translate a signal through human value and action semantics first.

---

## 6. Predicted action is not observed action and weights are not raw-count multipliers

This is one of the most important X-specific evidence boundaries.

Current code explicitly documents that ranking weights multiply **predicted probabilities** of actions, or predicted continuous values such as dwell time. They do not multiply raw engagement counts [R50].

Use:

```text
OBSERVED ACTION
≠ ELIGIBLE MODEL FEEDBACK
≠ PREDICTED ACTION / VALUE
≠ FINAL RANKING CONTRIBUTION
```

and:

```text
MODEL WEIGHT RATIO
≠ RAW ENGAGEMENT COUNT EQUIVALENCE
```

Do **not** read the current parameters and claim things such as:

```text
1 report cancels N likes
1 reply equals N likes
copy-link share is N times more valuable than a Like
```

That interpretation is explicitly rejected by the current implementation comments [R50].

The score is personalized because the model predicts **this viewer's** likelihood of multiple actions. A large negative weight does not mean one raw negative event globally subtracts an equivalent number of positive events from a post.

Current parameters are also time-sensitive production-default mirrors / configuration values rather than eternal platform laws [R50].

---

## 7. Interaction provenance can determine whether an action affects recommendation learning

Current implementation comments make an unusually strong provenance distinction: for recommendation-system impact, they state that relevant actions must occur on a post served in Home Timeline; directly navigating to a post, including coordinated navigation via group chat, does not have the same ranking impact [R50].

Therefore:

```text
SAME HUMAN ACTION TYPE
+ DIFFERENT DELIVERY / EXPOSURE PROVENANCE
→ DIFFERENT DOWNSTREAM SYSTEM EFFECT CAN OCCUR
```

This is a concrete X instance of the shared core rule:

```text
SAME OBSERVED HUMAN ACTION
≠ SAME SYSTEM-LEARNING EFFECT
```

It also reinforces:

```text
HUMAN ACTION
≠ AUTOMATICALLY ORGANIC MARKET SIGNAL
```

A real human click or report can still be coordinated, incentivized, or generated under a path the ranking system does not treat identically.

For serious diagnosis, preserve when knowable:

- where the interaction occurred;
- whether the object was served by the relevant system;
- whether the interaction was direct / coordinated / automated / representative;
- whether the event was eligible for the model or feedback loop being discussed.

Do not invent event eligibility when only aggregate public metrics are visible.

---

## 8. Retrieval, scoring, and slate composition create different competition mechanisms

### Current pre-scoring candidate filtering

The current For You implementation includes filters for conditions such as [R50]:

- duplicate candidates;
- failed core-data hydration;
- post age;
- viewer's own posts;
- some out-of-network replies/reposts;
- NSFW / recommendation-specific conditions;
- repeated reposts;
- subscriber-only access;
- previously seen / served posts;
- muted keywords;
- blocked or muted authors;
- video/topic request constraints;
- configured inventory holdouts.

A post filtered here never reaches ordinary scoring for that request.

### Current scoring adjustments

After Phoenix predicts actions, current code can apply additional scoring adjustments including [R50]:

- author-diversity decay;
- an out-of-network discount;
- new-author / cold-start handling;
- relationship-conditioned boosts under current config.

Current production-default values visible in the repository are implementation facts at the reviewed revision, not writing rules.

### Current reranking

The public `vm-ranker` implementation uses a determinantal point process over candidate embeddings to trade some local score for lower similarity among selected neighboring items [R50].

This means:

```text
INDIVIDUAL MODEL SCORE
≠ FINAL SLATE MEMBERSHIP / ORDER
```

A candidate can be individually strong but lose a position because the resulting slate would otherwise be too repetitive.

Do not translate this into:

```text
be random
always change topics
novelty always wins
```

The relevant practitioner implication is simply that **competing inventory and slate composition can change realized exposure**.

---

## 9. Freshness is a current For You pipeline constraint, not a universal post half-life

At the reviewed revision, the public For You pre-scoring pipeline removes candidates older than 48 hours [R50].

This is valuable implementation evidence, but scope it precisely:

```text
CURRENT FOR YOU CANDIDATE FILTER
posts older than configured For You age window can be excluded

≠

UNIVERSAL X CONTENT LIFETIME
```

A post can still exist on profile, appear through direct navigation, Search, conversation context, Following, or other systems whose implementation is not established by this filter.

Do not convert `48 hours` into:

- a universal posting-frequency rule;
- a claim that a post becomes worthless after 48 hours;
- an exact engagement-decay curve;
- a rule for Search / Explore / Communities;
- a reason to post low-value material more frequently.

Treat the value as a current, scoped implementation parameter and re-check it when consequential.

---

## 10. Visibility is a separate system and can be relationship-, recipient-, and market-relative

The public implementation separates ranking from visibility filtering [R50].

Current visibility evaluation can consider:

- author/account state;
- post labels;
- blocks / mutes;
- protected state;
- subscription-only access;
- viewer age / settings;
- country / legal state;
- media / safety labels;
- whether the item is an out-of-network recommendation.

Visibility can return conceptually:

```text
ALLOW
show normally

INTERSTITIAL
show behind a warning / additional action

DROP
do not show
```

The code contains a base Home policy and additional rules for recommendation-only / out-of-network contexts. Some states can therefore be allowed to followers while dropped from non-follower recommendation [R50].

This is a strong concrete example of:

```text
SAME OBJECT
+ DIFFERENT RELATIONSHIP / RECIPIENT / POLICY STATE
→ DIFFERENT VISIBILITY
```

and:

```text
HOSTED
≠ RECOMMENDABLE
```

The implementation also includes market-specific legal filtering, including a Brazil 2026 election filter at the reviewed revision [R50]. This is direct evidence that current recommendation eligibility can be market / policy relative.

Do not infer content quality from a visibility-state change.

---

## 11. Conversations, replies, quotes, and communities are distinct participation contexts

X is highly conversation-oriented. A standalone post, reply, quote post, and Community post should not be treated as equivalent objects.

### Reply

A reply inherits context from its parent conversation. Current For You code treats some out-of-network replies/reposts differently and later deduplicates additional branches of the same conversation [R50]. Current X Help also states that reply exposure depends on relationship and relevance context [R51].

Practical implication:

- reply when the job is to contribute to an existing conversation;
- do not write every reply like an isolated landing page;
- include enough context if the reply may travel beyond the immediate conversational audience;
- do not assume reply activity guarantees broad For You distribution.

### Quote post

A quote post combines a source object with a new framing / interpretation.

Preserve:

```text
SOURCE CLAIM
≠ CURRENT SPEAKER INTERPRETATION
```

Use enough context that a reader can distinguish what the source actually says from what the current actor adds.

### Community post

Current X Help describes Communities as moderated contexts with local rules. Community posts can travel beyond only the immediate Community page, while participation permissions can still be locally constrained [R51].

Therefore:

```text
VISIBLE BEYOND COMMUNITY
≠ IDENTICAL PARTICIPATION PERMISSION EVERYWHERE
```

Use current Community rules and moderator settings before generic X posting heuristics.

---

## 12. Content / representation guidance: write for human value, not exposed weights

X's public code creates a temptation to write directly for the model. Resist it.

For a normal standalone For You-oriented post, ask:

```text
JOB
what should this post accomplish?

ACTOR / SOURCE
why is this account entitled to say it?

AUDIENCE STATE
follower context, non-follower discovery, or both?

OBJECT / REPRESENTATION
text, image/video, quote/reply context,
what is actually legible in the feed?

HUMAN VALUE
what makes continuing / replying / sharing / following worthwhile?

PROOF
what makes the claim credible?

NEXT ACTION
only if the job needs one
```

### For non-follower discovery

Because For You explicitly includes out-of-network candidates, a relevant stranger may encounter the post without established source context [R50][R51].

Prefer enough portable context to understand:

- subject;
- why it matters;
- what is being claimed / shown;
- source or proof where material.

Do not turn portability into generic over-explanation.

### For relationship audiences

When the audience genuinely shares prior context, shorter references, recurring formats, callbacks, or conversational shorthand can be appropriate.

### Media

Use media when it improves demonstration, evidence, compression, emotion, accessibility, or comprehension. The existence of image/video features in machine systems is not proof that attaching media universally boosts distribution.

### External links

The current public ranking code includes link-open prediction, while visibility systems can act on malicious URLs [R50]. The reviewed sources do **not** establish a universal rule that ordinary external links are always suppressed.

If outbound traffic is the job, measure qualified downstream traffic rather than maximizing native engagement by default.

---

## 13. Never turn current implementation parameters into folk optimization formulas

Current public code exposes parameters for several ranking contributions and adjustments [R50]. That is useful for understanding architecture and falsifying myths, not for manufacturing deterministic content recipes.

Do not produce rules such as:

```text
reply because replies have weight X
ask for copy-link shares because weight Y is larger
post exactly every N hours because author diversity exists
avoid non-followers because an OON discount exists
force controversy because negative actions have large weights
post anything because new-author exploration exists
```

Why these translations fail:

1. weights apply to predicted probabilities / values, not raw counts;
2. predictions are viewer-specific;
3. candidate retrieval occurs before scoring;
4. filtering can remove candidates before or after ranking;
5. relationship and visibility state matter;
6. author diversity / reranking change slate competition;
7. final feed blending can alter encounter position;
8. production configs and experiments can change;
9. the open-source repository is intentionally incomplete in some safety / anti-gaming details.

Use exposed implementation to understand **mechanisms and boundaries**, not to write “algorithm hacks.”

---

## 14. Open source is stronger evidence, not complete production observability

The X repository is unusually valuable because it exposes current implementation code, production-default mirrors, model training/serving components, filters, and visibility logic [R50].

But preserve these boundaries.

### What the repository says about configuration

The repository states that many tunable values come from a configuration system. Cron processes mirror primary production defaults into public code, and X aims for experiments at notable traffic share (for example 10% or more) to be visible in the repository [R50].

Therefore:

```text
PUBLIC DEFAULT
≠ GUARANTEED VALUE FOR EVERY VIEWER / EXPERIMENT BUCKET / MOMENT
```

### What is intentionally not public

The repository explicitly says some material is withheld to reduce gaming risk, including examples such as Grox prompts and some Botmaker rules [R50].

Therefore:

```text
PUBLIC SOURCE CODE
≠ COMPLETE PRODUCTION OBSERVABILITY
```

### What source code can establish well

When current and properly scoped, implementation code can strongly support claims such as:

- a stage exists;
- a particular default is public at a revision;
- one system reads a specific state;
- a filter/rule path exists;
- a score is computed in a specific way;
- a public codepath separates ranking from visibility.

It does not automatically establish:

- current treatment for every user;
- every experiment assignment;
- every private config;
- every withheld safety rule;
- causal business impact of a writing tactic;
- behavior of another X surface.

Always preserve repository revision / review date when a consequential conclusion depends on code.

### Under the Hood

The current repository documents an Under the Hood transparency system that reports aggregate visibility-impacting labels on accounts/posts and exposes code for building those reports [R50]. Where available, this can be higher-value diagnosis evidence than guessing that weak reach reflects “shadowbanning.”

Use actual account labels / status when available before inventing creative or algorithmic explanations.

---

## 15. Observation record for X performance

Before concluding that an X post “worked” or “failed,” preserve only the fields that can change the conclusion.

```text
OBJECT / STATE
standalone post, reply, quote, repost, Community post,
subscriber-only state, media state, etc.

SURFACE / DELIVERY
For You, Following, direct navigation, Search,
notification, profile, Community, unknown

AUDIENCE / EDGE
follower, mutual, non-follower, subscriber,
Community relation, unknown

EXPOSURE PROVENANCE
served by relevant recommender?
direct navigation?
unknown?

INTERACTION ACT
Like, reply, repost, quote, DM share,
copy-link share, click, follow, negative action, etc.

INTERACTION PROVENANCE
organic individual, representative,
coordinated, automated, incentivized, unknown

PLATFORM STATE
candidate / eligibility / visibility / label state if known

TIME / HISTORY
fresh encounter, previously served, current window,
config / repository revision if implementation-dependent

SUCCESS METRIC
actual marketing job, not merely highest visible engagement
```

Do not infer model-input eligibility from public counts alone.

Do not assume visible totals describe only For You exposure. A post can receive traffic from several paths.

Do not infer a causal writing rule from a post-level correlation.

---

## 16. Practical X decision paths

### Simple standalone post

```text
job
→ actor / source
→ follower vs discovery context if material
→ object / media role
→ one clear human value
→ proof / context needed
→ next action only if earned
→ draft
```

Do not inspect ranking weights for an ordinary writing request unless the task actually depends on current For You mechanics.

### For You discovery post

```text
job
→ relevant non-follower state
→ enough portable subject/context
→ truthful value mechanism
→ object / media that carries the idea well
→ no engagement-weight bait
→ downstream metric matched to job
```

### Reply / conversation participation

```text
host post / conversation
→ what useful contribution is missing?
→ source / authority
→ relationship / audience envelope
→ concise contextual response
→ no unrelated self-promotion
```

### Quote post

```text
source object
→ source claim
→ current interpretation / evidence
→ portable framing
→ appropriate discussion / action
```

### Community post

```text
job
→ current Community rules
→ membership / participation state
→ actor identity
→ community relevance
→ portable context if wider travel matters
→ contribution + proof + ask
```

### Performance diagnosis

```text
metric changed
→ same surface / exposure path?
→ same follower vs OON mix?
→ same object / conversation state?
→ visibility / label evidence?
→ same current config / experiment regime if code-dependent?
→ interaction provenance / eligibility known?
→ creative changed?
→ competing explanations
→ discriminating check
```

---

## 17. Current evidence boundaries

### Established from the reviewed current X open-source For You implementation [R50]

- For You combines in-network and out-of-network candidate sources.
- Retrieval, candidate hydration, pre-scoring filtering, multi-action prediction, weighted scoring, reranking, selection, post-selection visibility filtering, blending, and side effects are separate stages / components.
- Phoenix predicts multiple viewer actions rather than one undifferentiated engagement value.
- Current scoring weights apply to predicted probabilities / continuous predicted values rather than raw engagement counts.
- Current code contains author-diversity, out-of-network, cold-start / new-author, relationship-conditioned, and reranking mechanisms.
- Current pre-scoring filters include a scoped post-age threshold, prior-view/served controls, social-graph controls, subscription access, and other eligibility checks.
- Current visibility filtering is separate from ordinary ranking and has additional recommendation-only rules.
- Current visibility can be recipient / relationship / market relative.
- Current comments document that interaction path can affect whether actions have recommendation-system impact.
- Current public code / configuration is incomplete by design in some anti-gaming / safety areas.

### Established from current X product / recommender documentation [R51]

- X uses multiple recommendation systems / surfaces rather than one universal algorithm.
- For You contains both followed-network and recommended content.
- Following is a distinct timeline based on followed accounts.
- Replies and conversations have relationship / relevance-conditioned visibility behavior.
- Communities are locally governed participation contexts whose content can travel outside the immediate Community page.
- Users can influence recommendation state through follows, Topics, Likes, reposts, replies, blocks, mutes, Not Interested and related controls.

### Supported by broader theory, not claimed as X-specific implementation detail

- selection / exposure condition observed recommendation data [R32][R33];
- heterogeneous interactions should not be collapsed into one behavioral magnitude [R40];
- sequential history can matter to evolving recommendation state [R41];
- visibility reduction is conceptually distinct from ordinary low ranking [R31].

### Not established as universal X laws

- one report cancels a fixed number of Likes;
- a reply is worth a fixed number of Likes;
- share-via-copy-link is a fixed multiplier on raw reach;
- asking for a modeled action increases distribution;
- For You weights apply unchanged to Search, Explore, Communities, Notifications, or Following;
- every follower sees every post;
- every non-follower post is penalized in the same realized way;
- author diversity proves an optimal posting frequency;
- the 48-hour For You filter defines total X content lifetime;
- external links are universally suppressed;
- a new author is guaranteed reach;
- high raw engagement proves high predicted relevance for every viewer;
- direct-navigation engagement has the same recommendation effect as Home-served engagement;
- public source code exposes every production rule, prompt, configuration, or experiment;
- a public ranking parameter establishes a causal content-writing tactic.

Use X's implementation transparency to eliminate weak algorithm folklore, then return to the human job, the actual audience state, and current comparable local evidence.
# Content-Environment Compact-Core Losslessness Audit

Reviewed: 2026-08-23

Status: **research audit, not benchmark/eval**.

Purpose: test whether the compressed platform-content model can preserve the consequential distinctions that previously emerged from platform research **without re-introducing the older, larger ontology**.

This audit does **not** test prose quality, agent compliance, causal effect size, or platform performance. It tests representational adequacy only:

> Can the current compact core encode the case without collapsing two decision-relevant states, inventing an unsupported mechanism, or requiring a retired primitive?

## Core under test

Eight durable things:

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

Three cross-cutting modifiers:

```text
provenance
scope / relativity
history / state transition
```

A case **fails** only if the consequential distinction cannot be represented by these elements without distortion.

## Verdicts

```text
LOSSLESS
all decision-relevant distinctions can be represented directly.

LOSSLESS / INTERNAL UNKNOWN
representation is adequate, while an undisclosed platform-internal step remains explicitly unknown.

PARTIAL
representation is possible only by collapsing a distinction that can change the decision.

FAIL
an additional durable primitive or a material core correction is required.
```

An explicit `UNKNOWN` is not a failure. Preserving uncertainty is part of the model.

## Evidence boundary

For TikTok, Instagram, LinkedIn, Facebook, and X, this audit uses the current platform modules and their bound source sets.

Reddit and YouTube remain research stress environments rather than runtime modules. Their scenarios below were re-grounded on 2026-08-23 against current official documentation before being frozen for this audit:

- Reddit Help — **Moderation Queue**, updated 2026-07-28;
- Reddit Help — **Community settings**, updated 2026-08-07;
- Reddit Help — **Disrupting Communities**, updated 2026-05-19;
- YouTube Help — **A/B test titles & thumbnails**;
- YouTube Help — **Add Multi-language features to your videos**;
- YouTube Help — **Embed videos & playlists / Privacy Enhanced Mode**;
- YouTube Help — **Check your YouTube impressions and watch time**.

These frozen stress scenarios do not create Reddit or YouTube production modules.

---

# 1. TikTok

## T1 — Watch-time signal must not become a length tactic

**Stress case**

TikTok documentation can make watch/continuation behavior relevant to recommendation, but a practitioner must not infer:

```text
watch time matters
→ make the video longer
```

**Compact encoding**

```text
object                 = video
representation         = first/early consumed frames + other encounter context
audience state         = For You viewer with partial history
interaction act        = continue / watch / skip
platform state         = For You recommendation regime
observation record     = watch/continuation metric under exposure
provenance             = surface/system-specific signal disclosure
```

**Preserved distinction**

```text
interaction signal
≠ ranking objective
≠ human motive
≠ writing instruction
```

No retired `behavior-to-mechanism` primitive is required; the bridge is derived from interaction + platform state + observation provenance.

**Verdict: LOSSLESS**

---

## T2 — TikTok search activity is not independent market demand

**Stress case**

Search terms and search activity can be platform-suggested or content-induced, so Creator Search Insights must not be interpreted as direct market-size or purchase-intent evidence.

**Compact encoding**

```text
audience state         = emerging / explicit / refining intent
interaction act        = search
platform state         = Search + suggestion environment
observation record     = platform search activity / topic evidence
provenance             = self-initiated / platform-suggested / content-induced / unknown
scope                   = TikTok search environment
```

**Preserved distinction**

```text
platform search activity
≠ independent demand
≠ buying intent
≠ market size
```

`Intent provenance` survives as ordinary provenance on audience/interaction state rather than a separate ontology.

**Verdict: LOSSLESS**

---

## T3 — Same TikTok object can accumulate mixed organic and paid evidence

**Stress case**

An organic object can later receive paid amplification or commerce state while visible interactions continue accumulating on the same or related artifact.

**Compact encoding**

```text
content object         = same persistent video/post
platform state(t0)     = organic delivery
state transition       = paid/commercial support attached
platform state(t1)     = mixed / paid-supported delivery
typed edge              = new paid/commercial delivery edge
observation record     = metrics accumulated across delivery regimes
history                 = delivery-state timeline
```

**Preserved distinction**

```text
same object identity
≠ same delivery state
≠ delivery-mode-pure metric history
```

No standalone `secondary-use path` or `delivery-mixture` primitive is required.

**Verdict: LOSSLESS**

---

# 2. Instagram

## I1 — Recommendation eligibility is not realized exposure

**Stress case**

An Instagram object may be recommendation-eligible without being retrieved, highly ranked, or broadly exposed.

**Compact encoding**

```text
content object         = post / Reel / carousel
platform state         = recommendation-eligible
encounter surface      = suggested Feed / Explore / Reels / other scoped surface
observation record     = actual exposure / reach if observed
scope                   = system/surface/account regime
```

**Preserved distinction**

```text
eligible
≠ retrieved
≠ highly ranked
≠ exposed
≠ successful
```

The exact internal retrieval-to-final-composition chain is not fully disclosed in the current Instagram source set. The model does not need to invent it.

**Verdict: LOSSLESS / INTERNAL UNKNOWN**

---

## I2 — Platform-native trial/staged distribution is not automatically a static A/B test

**Stress case**

If exposure expands or changes in response to earlier performance, ordinary comparison can become selection/adaptivity-conditioned.

**Compact encoding**

```text
content object         = trial/distributed object
platform state         = staged/adaptive allocation regime
history                 = prior outcomes change later exposure
observation record     = performance under changing allocation
time                    = stage / period
```

**Preserved distinction**

```text
platform-native probe
≠ fixed allocation
≠ controlled causal experiment
```

`Adaptive rollout` remains a derived description of platform state + history + observation regime.

**Verdict: LOSSLESS**

---

## I3 — Collaboration changes authorship/distribution without transferring claim authority

**Stress case**

A collaboration can expose one object under multiple visible authors or audiences, but that does not make every collaborator the source of every claim or first-person experience.

**Compact encoding**

```text
actor/source           = claim-supporting source(s)
content object         = collaborative post/object
content representation = visible collaborative authorship/presentation
typed edge              = creator-brand / co-author / distribution relationship
platform state         = collaboration/commercial state
provenance             = operational actor / content owner / claim source
```

**Preserved distinction**

```text
visible author
≠ operational actor
≠ source authority
≠ content owner
```

**Verdict: LOSSLESS**

---

# 3. LinkedIn

## L1 — Unfollowing a connection changes delivery without deleting the relationship

**Stress case**

A LinkedIn member can remain connected while no longer following the other person's updates.

**Compact encoding**

```text
relationship edge(t0) = first-degree connection
delivery edge(t0)     = follow/feed-update path
interaction/state      = unfollow
delivery edge(t1)     = removed/reduced
relationship edge(t1) = connection persists
```

**Preserved distinction**

```text
relationship
≠ delivery

exit from one edge
≠ global relationship exit
```

No separate `relationship graph` and `delivery graph` ontology is required; typed edges preserve the distinction.

**Verdict: LOSSLESS**

---

## L2 — Employee-notification request is not guaranteed employee exposure

**Stress case**

A Page can request employee notification for an eligible post, while platform relevance allocation, opt-out state, processing, and delivery still mediate who actually receives it.

**Compact encoding**

```text
actor/source           = Company Page
content object         = Page post
typed delivery edge    = requested employee-notification path
platform state         = relevance/eligibility/opt-out allocation
exposure opportunity   = realized only after allocation
observation record     = delivered/notified/exposed response if available
```

**Preserved distinction**

```text
publisher request
≠ platform allocation
≠ delivery
≠ exposure
≠ response
```

**Verdict: LOSSLESS**

---

## L3 — Engagement pods / automation break the shortcut from engagement to preference

**Stress case**

A like/comment/reply can be a real event while its provenance is automated, coordinated, incentivized, representative, or otherwise non-organic.

**Compact encoding**

```text
interaction act        = like/comment/reply/share
provenance             = direct / automated / coordinated / incentivized / unknown
platform state         = authenticity/enforcement regime
observation record     = visible engagement event(s)
```

**Preserved distinction**

```text
observed engagement
≠ established organic human preference
```

This is exactly the C1 correction after compression: interaction provenance is a consequential provenance instance, not a separate platform framework.

**Verdict: LOSSLESS**

---

# 4. Facebook

## F1 — Limited membership: can see/react without permission to post/comment/chat

**Stress case**

In an eligible private Group, a limited member can encounter Group content and react while lacking permission for other participation actions until approval.

**Compact encoding**

```text
audience state         = limited member
relationship edge      = Group membership
visibility edge        = may view
permission edge        = may react
permission edge        = may not post/comment/chat yet
interaction act        = absent comment must be interpreted under permission state
```

**Preserved distinction**

```text
membership
≠ visibility
≠ participation permission

exposure
≠ response opportunity for every action
```

**Verdict: LOSSLESS**

---

## F2 — Anonymous/nickname participation is observer-relative identity, not global anonymity

**Stress case**

Peers may see an anonymous/nickname identity while moderators/admins and Facebook systems retain access to the underlying profile identity.

**Compact encoding**

```text
actor/source           = underlying account/person
content representation = peer-visible anonymous/nickname identity
platform state         = anonymous-participation affordance
scope/relativity       = peer vs moderator vs platform observer
```

**Preserved distinction**

```text
identity visible to peers
≠ identity visible to moderators
≠ identity known to platform
```

No separate `observer-relative identity` primitive is required; scope/relativity modifies actor/representation state.

**Verdict: LOSSLESS**

---

## F3 — Private-container origin does not guarantee one lifetime visibility state

**Stress case**

A private-Group object can later obtain a scoped public path through an authorized feature such as Group Highlights where available.

**Compact encoding**

```text
content object         = original Group post/comment
platform state(t0)     = private-container visibility
state transition       = authorized scoped public visibility
platform state(t1)     = additional public delivery/visibility path
typed edge              = new public encounter path
```

**Preserved distinction**

```text
object identity persists
while visibility state changes
```

No standalone `secondary visibility` primitive is needed.

**Verdict: LOSSLESS**

---

# 5. Reddit research stress scenarios

## R1 — Moderator removal is not equivalent to object non-existence

**Frozen current fact**

Reddit's current Mod Queue documentation says moderator removal de-lists the item from community/site listings including the OP profile for ordinary users; a direct-link visitor sees `[Removed by moderator]`, while moderators can still see the item in moderation context.

**Compact encoding**

```text
content object         = persistent post/comment identity
platform state         = moderator-removed / de-listed
content representation = [Removed by moderator] for direct-link ordinary viewer
scope/relativity       = ordinary viewer vs moderator
provenance             = moderator governance action
```

**Preserved distinction**

```text
object exists
≠ publicly listed
≠ same representation for every observer
```

The generic provenance modifier is sufficient for `who/what changed the state`; no dedicated governance-provenance primitive is required.

**Verdict: LOSSLESS**

---

## R2 — Archived post: same object, time-dependent action space

**Frozen current fact**

Reddit community settings can archive posts after six months; when enabled, users cannot vote or comment on archived posts.

**Compact encoding**

```text
content object         = same post
platform state(t0)     = ordinary active post
state transition       = age/community-setting threshold
platform state(t1)     = archived
permission edges(t1)   = vote/comment closed
history/time           = age-dependent effective state
```

**Preserved distinction**

```text
same content identity
≠ same response opportunity over time
```

`Archived` is simply a typed platform/content state with time scope.

**Verdict: LOSSLESS**

---

## R3 — Human coordinated voting is not an independent organic aggregate signal

**Frozen current fact**

Reddit Rules explicitly prohibit coordinated voting by organized groups of people or bots, as well as multi-account/automation vote manipulation.

**Compact encoding**

```text
interaction acts       = multiple votes
provenance             = coordinated / duplicated / automated / unknown
observation record     = aggregate score / vote history
platform state         = vote-manipulation governance regime
```

**Preserved distinction**

```text
real human actions
≠ independent organic signal
```

The older label `interaction-set provenance` is fully expressible as provenance on a set/aggregate observation record.

**Verdict: LOSSLESS**

---

# 6. YouTube research stress scenarios

## Y1 — Same video object, concurrent title/thumbnail representations

**Frozen current fact**

YouTube currently lets eligible creators A/B test up to three titles, thumbnails, or combinations on the same long-form video; variants are shown concurrently and the selected winner is based on watch-time performance.

**Compact encoding**

```text
content object         = one persistent video
content representation = title/thumbnail variant A/B/C
platform state         = concurrent experiment/allocation regime
audience state         = viewer composition may vary
observation record     = variant exposure + watch-time outcome
```

**Preserved distinction**

```text
content object
≠ selection representation
≠ experiment assignment
```

This case is exactly why C2 `content representation` remains a durable thing after compression.

**Verdict: LOSSLESS**

---

## Y2 — Same video identity can deliver different language representations

**Frozen current fact**

YouTube supports multiple audio tracks on one video/Short and localized thumbnails for long-form video. Viewer language settings/history can affect which audio/thumbnail representation is presented; translated titles/descriptions can also support discovery.

**Compact encoding**

```text
content object         = one video identity
selection representation = localized title/thumbnail
consumption representation = selected audio language/dub
audience state         = language preference/history
scope/relativity       = recipient/language context
observation record     = performance may aggregate multiple representations
```

**Preserved distinction**

```text
one object identity
≠ one uniform experienced representation
```

No new `rendition` primitive is needed; consumption representation is sufficient.

**Verdict: LOSSLESS**

---

## Y3 — Same view action can have different downstream personalization effect by delivery context

**Frozen current fact**

YouTube Privacy Enhanced Mode says a view in that embedded-player mode is not used to personalize the viewer's subsequent YouTube browsing experience.

**Compact encoding**

```text
interaction act        = video view/consumption
encounter surface      = privacy-enhanced external embed
platform state         = privacy-enhanced personalization regime
provenance             = delivery/surface provenance of the action
observation record     = view may still exist as consumption evidence
```

**Preserved distinction**

```text
same observed action type
≠ same downstream system-learning effect
```

No separate `system-update semantics` primitive is required; platform state + provenance modifies the meaning of the event for the recommender loop.

**Verdict: LOSSLESS**

---

## Y4 — Thumbnail-impression denominator is an instrumentation construct, not all watch opportunities

**Frozen current fact**

YouTube's current thumbnail-impression definition excludes several paths, including external sites/apps, email/notifications, cards/end screens, and some other contexts, even though traffic/views can still arrive from such paths.

**Compact encoding**

```text
content object         = video
content representation = thumbnail where applicable
typed delivery edge    = Home/Search/Up Next vs notification/external/etc.
observation record     = registered thumbnail impressions + denominator definition
scope                   = eligible measurement surfaces only
```

**Preserved distinction**

```text
registered impression denominator
≠ all exposure/watch opportunities
```

`Metric provenance` remains ordinary provenance inside the observation record rather than a separate schema.

**Verdict: LOSSLESS**

---

# 7. X implementation-backed stress scenario

## X1 — High candidate score does not determine final served-feed position

**Frozen implementation fact**

At the reviewed X For You implementation revision, candidate retrieval, pre-scoring filters, multi-action prediction, scoring, reranking/diversification, top-K selection, visibility filtering, and final feed blending are distinct stages.

**Compact encoding**

```text
content object         = candidate post
audience state         = hydrated viewer/request state
typed relationship edge = in-network / out-of-network / mutual/etc.
platform state         = retrieval → scoring → reranking → visibility → blending
observation record     = final served/not-served exposure if observed
history                 = prior impressions/actions can alter request state
```

**Preserved distinction**

```text
individual candidate score
≠ final slate membership
≠ final order
≠ guaranteed exposure
```

The detailed stage names remain X implementation facts. The durable core needs only typed platform/mediation state and the resulting observation context.

**Verdict: LOSSLESS**

---

# 8. Audit result

## Scorecard

| Platform / stress source | Cases | LOSSLESS | LOSSLESS / INTERNAL UNKNOWN | PARTIAL | FAIL |
| --- | ---: | ---: | ---: | ---: | ---: |
| TikTok | 3 | 3 | 0 | 0 | 0 |
| Instagram | 3 | 2 | 1 | 0 | 0 |
| LinkedIn | 3 | 3 | 0 | 0 | 0 |
| Facebook | 3 | 3 | 0 | 0 | 0 |
| Reddit research stress | 3 | 3 | 0 | 0 | 0 |
| YouTube research stress | 4 | 4 | 0 | 0 | 0 |
| X implementation-backed | 1 | 1 | 0 | 0 | 0 |
| **Total** | **20** | **19** | **1** | **0** | **0** |

All 20 cases preserve the consequential distinction under the compressed core. The one `LOSSLESS / INTERNAL UNKNOWN` result is not a representational deficiency: Instagram's disclosed evidence is sufficient to preserve eligibility-versus-exposure while not exposing a complete internal organic recommendation pipeline.

## What compression did not lose

The audit required all of the following distinctions without re-introducing retired peer-level primitives:

```text
object identity ≠ object/platform state
object ≠ representation ≠ surface
relationship ≠ delivery ≠ permission
request/configuration ≠ realized exposure
exposure ≠ response opportunity
observed action ≠ motive / preference / system use
human action ≠ independent organic aggregate signal
eligibility ≠ retrieval/rank/exposure
individual score ≠ final slate
organic state ≠ paid-supported state
same event label ≠ same measurement provenance
same action type ≠ same downstream system-learning effect
metric denominator ≠ all possible opportunities
current event ≠ memoryless response
```

## Retired labels were not required as primitives

The following older labels remain useful shorthand but were not necessary to encode any case:

```text
relationship graph
delivery graph
attention re-entry
secondary-use path
nested recommendation environment
spillover carrier
platform-conferred state
public feedback state
interaction-set provenance
creator/user/recommender loop as standalone ontology
```

Where needed, their meaning was reconstructed from durable things + typed edge + state + provenance + scope + history.

## Durable corrections that remain necessary

Two prior corrections continue to earn durable status:

1. **Interaction provenance as a consequential provenance instance** — required by LinkedIn engagement manipulation, Reddit coordinated voting, X feedback-path distinctions, and similar cases.
2. **Content representation** — required by YouTube title/thumbnail experiments, localization/renditions, and platform-native preview/cover/framing differences elsewhere.

No C3 and no seventh analytical layer were required.

## Compression verdict

```text
COMPACT CORE
20 / 20 anomaly encodings preserve the decision-relevant distinction
0 partial
0 fail
0 retired primitive required
0 new durable primitive required
```

**Research verdict: PROVISIONALLY LOSSLESS FOR THE CURRENT FROZEN STRESS SET.**

This is a conceptual representational result, not a benchmark score and not empirical proof of universality.

---

# 9. What this does and does not justify next

This audit supports a **theory/architecture freeze candidate** because additional platform breadth is producing fewer ontology changes and the compressed vocabulary preserved the frozen anomaly set.

It does **not** establish that an agent will reliably invoke the right distinctions at runtime.

The next validation question is therefore different:

> Given realistic user tasks, does the runtime actually load the right platform evidence and apply the compact distinctions only when they change the decision?

That should be tested with concrete tasks before any claim of benchmark readiness. The next phase can remain pre-benchmark and focus on runtime behavior, failure cases, and decision quality rather than adding more platform ontology.
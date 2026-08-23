# 08 — Content Environments and Distribution

## 1. Scope and central thesis

Audience-facing content does not exist only as prose. It is created by an actor, represented through one or more artifacts, placed inside a social and technical environment, distributed under partially observable policies, and measured through data that those same policies helped generate.

This chapter provides a practitioner synthesis for social and platform-native content. It covers posts, captions, carousels, short-form video, Stories, comments, replies, reposts, community participation, newsletters, creator collaborations, search-oriented content, and related formats.

It is not a catalog of algorithm tricks, a universal social-media funnel, or a claim that one scientific theory explains every platform.

The central thesis is:

> Platform mechanics determine not only what gets seen, but also which representations are encountered, which responses are possible, which responses become observable, and what the marketer is justified in learning from both action and silence.

A second operational principle follows:

> Resolve only the environmental variables that can materially change the current content decision or the interpretation of its result.

The model combines established work on networked audiences, community norms, social-media affordances, recommender systems, visibility moderation, multi-stakeholder recommendation, algorithmic management, preference construction, biased or missing implicit feedback, sequential behavior, cross-channel effects, delayed feedback, and causal inference [R23–R26][R31–R49]. The complete practitioner model has not itself been validated as one unified scientific theory.

---

## 2. Content is participation in a platform-mediated environment

A content task can require more than writing an artifact. The practitioner may need to decide:

- whether to publish a standalone object at all;
- whether to comment, reply, repost, remix, collaborate, or join an existing conversation;
- which identity should speak;
- which audience state and relationship matter;
- which representation of an object will actually be encountered;
- which part of the message belongs in text, image, video, audio, metadata, or another carrier;
- which platform constraints affect visibility or participation;
- which behavior should count as success;
- what the observed metrics can and cannot support as evidence.

Use the distinction:

```text
CONTENT PRODUCTION
creating an artifact

CONTENT PARTICIPATION
choosing how to enter, continue, or shape an information environment
```

Sometimes the right action is a post. Sometimes it is a substantive comment, a reply, a search-oriented tutorial, a collaboration, a private response, or no new content at all.

Do not reason directly from platform name to writing rule. A platform contains multiple systems, surfaces, roles, object types, delivery modes, policy states, and audience states.

For consequential platform claims, preserve the scope when material:

```text
platform
system / surface
object / representation
actor / account type
recipient / audience state
delivery mode
market / policy regime
time
objective
```

An official fact from one system does not silently become a universal platform law.

---

# Part I — The compressed six-layer model

## 3. Vocabulary discipline: primitives, modifiers, and derived patterns

The model became more useful as platform-specific research converged, but a mature core should not turn every recurring pattern into a new primitive.

Use a small durable vocabulary.

### 3.1 Durable things

At runtime, most consequential platform-content questions can be represented with these durable things:

```text
ACTOR / SOURCE
who speaks, acts, or supports a claim?

CONTENT OBJECT
what persistent or addressable artifact / participation unit exists?

CONTENT REPRESENTATION
what version, package, preview, or rendition is actually presented?

AUDIENCE STATE
what does the relevant person know, intend, expect, remember, or need?

TYPED RELATIONSHIP / ACCESS EDGE
what relationship, delivery path, or permission connects actors and objects?

INTERACTION ACT
what action or non-action occurred, toward what, under which topology and cost?

PLATFORM / MEDIATION STATE
what governance, eligibility, ranking, delivery, or system state shapes opportunity?

OBSERVATION RECORD
what event or metric was logged, under which exposure, unit, time, and attribution regime?
```

Not every task needs all eight.

### 3.2 Cross-cutting modifiers

Three questions recur across the whole model and should be treated as modifiers rather than separate ontologies.

#### Provenance

Ask where a claim, intent, action, state, or metric came from and through which mechanism.

Examples:

- source / authority provenance;
- intent provenance;
- interaction provenance;
- metric provenance.

#### Scope / relativity

A state may be valid only for a particular:

- observer;
- actor role;
- recipient class;
- surface;
- representation;
- market;
- policy regime;
- session;
- time.

Do not turn a scoped state into a global property.

#### History / state transition

People, objects, relationships, and platform states change over time. Ask what prior state matters, what changed, and what future opportunities that change opens or closes.

### 3.3 Derived patterns are not new primitives

The following ideas remain useful, but treat them as compositions of the durable things above rather than standalone ontology:

- attention re-entry = a future delivery edge creates another encounter;
- secondary use = an existing object changes role or state;
- nested recommendation = one object/surface contains another ranked environment;
- spillover = state, signal, or object crosses an edge or environment;
- platform-conferred status = actor/object platform state;
- public feedback state = prior observations become visible encounter context;
- community contract = local governance, norms, audience relationship, and relevance constraints;
- creator/user/recommender loops = feedback dynamics among changing states.

Before adding a new core term, ask:

> Can the consequential distinction already be represented as a thing + typed edge + state + provenance + scope + transition?

If yes, keep the new label local to a platform module or example rather than growing the durable core.

---

## 4. Layer 1 — Human meaning, actor, object, and representation

This layer asks what the contribution is trying to do for a person, who is entitled to speak, what the underlying artifact is, and what the audience actually encounters.

### 4.1 Content job

Identify the primary job of the current contribution.

Possible jobs include:

- announce;
- explain;
- teach;
- demonstrate;
- document progress;
- build recognition;
- provide proof;
- enter or continue discussion;
- answer an existing question;
- generate qualified traffic;
- support conversion;
- recruit participation;
- collect feedback;
- retain or reactivate an audience;
- support a relationship;
- create a reusable reference.

A piece may have secondary effects, but a primary job helps choose object, representation, proof, action, and success metric.

### 4.2 Source, authority, and acting identity

Ask who or what legitimately supports the statement.

Distinguish when material:

```text
SOURCE / AUTHORITY
who supports the claim?

VISIBLE PUBLISHING IDENTITY
who appears publicly attached to the contribution?

OPERATIONAL ACTOR
who or what actually performed the action?
```

The visible speaker must not inherit authority they do not possess. An organization cannot fabricate a founder's personal history. A creator cannot claim first-person product experience merely because a brand supplied product facts.

Visible identity and operational actor can diverge. An organizational account may be operated by an employee, administrator, tool, or workflow. A pseudonymous identity can still be known to moderators or the platform. Preserve the distinction only when it changes authority, accountability, authenticity, safety, or interpretation.

### 4.3 Content object, state, and lineage

Separate the underlying object from its current state.

Possible objects or participation units include:

- image;
- carousel;
- video / short video;
- Story;
- post;
- article;
- newsletter;
- comment / reply;
- repost / quote-response;
- remix;
- LIVE;
- playlist / collection;
- collaborative object.

Use:

```text
CONTENT IDENTITY
what persistent or addressable artifact / object is this?

CONTENT STATE
what attachments, ownership, commercial role,
visibility, permissions, or delivery state currently apply?
```

An object can change state without becoming a wholly new marketing idea. A live event can become an archive; an organic object can later receive paid support; a private-container object can gain a scoped public path.

Lineage matters when the object derives meaning from another object: reply, repost, remix, series continuation, quotation, collaborative derivative, or extracted segment.

Do not invent a separate primitive for every secondary-use path. Represent the source object, derived object if one exists, the state transition, and the relevant edge.

### 4.4 Content representation

Keep **content object identity** separate from the **representation actually presented to a recipient**.

Web architecture provides a useful technical parent for this distinction: a resource can have multiple representations, and a selected representation can vary by language, format, capabilities, preferences, or time [R48][R49]. This is architectural vocabulary, not a claim that HTTP semantics is a marketing theory.

For platform content, a representation can play different roles.

```text
SELECTION REPRESENTATION
what helps a person decide whether to enter or continue

examples:
title
thumbnail / cover
snippet
preview card
notification copy
repost framing
first autoplay frames

CONSUMPTION REPRESENTATION
what rendition of the object is actually consumed

examples:
localized text
dubbed audio
subtitles / captions
audio description
recipient-specific media rendition
```

Therefore:

```text
CONTENT OBJECT
≠ CONTENT REPRESENTATION
≠ ENCOUNTER SURFACE
```

and:

```text
REPRESENTATION PERFORMANCE
≠ CONTENT PERFORMANCE
```

A representation can create an expectation before the underlying object is consumed. A strong selection representation paired with a weak or mismatched object can increase entry while harming downstream experience. Conversely, useful content can be under-selected because its representation is weak or mismatched to the surface.

Do not assume every object has materially different representations. Use the distinction only when it changes execution, diagnosis, localization, accessibility, or measurement.

### 4.5 Human content meaning and message allocation

Ask:

> What is this contribution actually trying to say, show, prove, or invite?

Keep human content meaning separate from machine representation.

Possible message carriers include:

- visual composition;
- image sequence;
- motion;
- spoken words;
- music or sound;
- on-screen text;
- title / cover / thumbnail;
- caption / body text;
- metadata;
- interaction controls;
- comment / reply;
- CTA.

For multimodal content, allocate meaning deliberately:

```text
What must the audience understand?
↓
Which carrier should communicate each part most efficiently and truthfully?
```

Do not force the caption to repeat information already communicated well by the object unless repetition improves comprehension, accessibility, qualification, proof, or action.

### 4.6 Context portability and environment fit

Networked content can reach audiences beyond the imagined initial reader [R23]. Ask how much meaning survives when the object or representation travels into another surface, audience, or community.

High-portability content includes enough framing to survive recommendation, search, repost, share, or later rediscovery. Low-portability content may appropriately rely on shared context when the job is intentionally local.

Do not maximize portability automatically. Extra context consumes attention.

Before finalizing a contribution, ask:

> Why should this contribution belong or matter here, from this actor, for this audience state, in this moment?

In a bounded community, answer with current rules, norms, membership, topic boundaries, expertise expectations, and promotion tolerance where relevant [R25][R26]. In Search, answer with intent satisfaction. In a professional feed, answer with professional relevance. These are environment-specific constraints, not separate universal primitives.

### 4.7 Early value without hook folklore

Fast-scrolling or sequential media often require enough information early for a person to understand why continuing may be worthwhile.

This can be communicated by a clear subject, answer, demonstration, result, problem, contradiction, or other useful signal. Do not turn this into one universal hook formula, fixed-second rule, shock tactic, or curiosity template.

---

## 5. Layer 2 — Audience state, typed edges, and interaction

This layer asks who can encounter the content, what state they are in, what relationships or permissions connect them to the actor/object, which actions are actually available, and what transitions matter.

### 5.1 Audience state and envelope

Infer only what the environment reasonably supports. Relevant audience states can include:

- scrolling without explicit intent;
- actively searching;
- exploring an emerging interest;
- comparing alternatives;
- evaluating a creator or organization;
- participating in a discussion;
- consuming a recurring series;
- considering a purchase;
- returning after a notification;
- trying to complete a task.

State should change the decision. It should not become a fabricated persona.

Distinguish the intended reader from the broader **audience envelope**: who can realistically encounter the object or representation after recommendation, search, repost, direct share, collaboration, notification, secondary use, or later state change.

Prefer audience knowledge in this order when material:

```text
explicit user-defined audience
→ configured platform target
→ known membership / subscription context
→ observed current audience evidence
→ contextual inference
→ generic platform prior
```

Do not fabricate demographic or psychographic precision because a platform is known.

### 5.2 Typed relationship, delivery, and permission edges

Do not model relationship as one scalar such as strong/weak.

Represent only the typed edges that matter:

```text
RELATIONSHIP EDGE
connection / follow / membership / customer relationship / repeated familiarity

DELIVERY EDGE
Feed / notification / newsletter / recommendation / community / direct-share path

PERMISSION EDGE
may view / react / comment / post / message / moderate / monetize / reuse
```

One edge can exist without the others.

Therefore:

```text
RELATIONSHIP
≠ DELIVERY
≠ PARTICIPATION PERMISSION
```

and:

```text
EXIT FROM ONE EDGE
≠ GLOBAL EXIT FROM SOURCE OR CONTENT
```

A person can unfollow while remaining connected. A community member can see content while lacking permission to comment. A subscriber can remain subscribed while a particular notification is not delivered.

### 5.3 Intent provenance and history-conditioned state

Do not assume observed search or interaction represents a stable pre-existing preference. Preference-construction research treats preferences as capable of being formed or revised during recommendation [R37].

Possible intent provenance includes:

```text
self-initiated
platform-suggested
content-induced
socially induced
commercially prompted
unknown
```

Therefore:

```text
PLATFORM SEARCH ACTIVITY
≠ AUTOMATICALLY INDEPENDENT MARKET DEMAND
```

Current state can also be history-conditioned. A reader may arrive with prior exposure, familiarity, trust, fatigue, objections, saves, or an existing relationship.

For consequential outcomes, ask what prior history could materially explain the current state. Do not invent one universal lookback window.

### 5.4 Interaction act

Do not reduce all behaviors to one engagement ladder. Multi-behavior recommender research treats interactions as heterogeneous signals with different semantics and temporal structure [R40].

When interpretation matters, inspect the interaction act:

```text
action type
target / addressee
topology and visibility
cost / friction
intentionality
scope
```

Examples of minimum operational meanings:

```text
SAVE
preservation / revisit behavior

SHARE / SEND
content travel toward another audience or context

COMMENT / REPLY
conversation participation

FOLLOW / SUBSCRIBE
relationship-state transition

PROFILE VISIT
identity evaluation

SEARCH
intent expression / refinement

PRODUCT CLICK
commerce-state transition

PURCHASE
transactional outcome

REMIX
viewer-to-creator participation transition
```

These are not guaranteed motives.

One-to-one private sending and one-to-many public broadcasting can produce different sharing incentives; Barasch and Berger found different sender focus under narrowcasting and broadcasting in the studied settings [R43]. Use this as evidence that topology can change interaction semantics, not as a universal formula.

Action cost can include effort, attention, identity exposure, privacy, reputation, social obligation, or recipient burden.

Core invariant:

```text
OBSERVED ACTION
≠ DIRECT EVIDENCE OF MOTIVE
≠ DIRECT EVIDENCE OF SATISFACTION
≠ DIRECT EVIDENCE OF CONTENT QUALITY
≠ DIRECT EVIDENCE OF CAUSAL MECHANISM
```

### 5.5 Interaction provenance, response opportunity, and non-action

Before interpreting an engagement event as human preference, ask whether its provenance is material.

Possible states include, only when evidence supports the distinction:

```text
direct individual action
representative action on behalf of an entity
automated
coordinated
incentivized
platform-generated
unknown
```

A set of real human actions can still be coordinated or incentivized. Therefore:

```text
HUMAN ACTIONS
≠ INDEPENDENT ORGANIC SIGNAL
```

and:

```text
OBSERVED ENGAGEMENT EVENT
≠ ESTABLISHED ORGANIC HUMAN RESPONSE
```

Also distinguish exposure opportunity from response opportunity.

```text
EXPOSURE OPPORTUNITY
was the person placed where the object or representation could be encountered?

RESPONSE OPPORTUNITY
did the person have a meaningful chance to perform
or withhold the specific action being interpreted?
```

Response opportunity can depend on:

- whether the relevant representation/message was actually reached;
- whether the affordance existed at that moment;
- role / membership / permission state;
- identity or reputational cost;
- device / surface / session constraints;
- sufficient time and context.

Missing-not-at-random implicit-feedback research shows why lack of a click cannot simply be treated as a clean negative when exposure is incomplete or selectively generated [R44]. The broader practitioner implication is:

```text
NO ACTION
≠ NEGATIVE ACTION
```

Keep absent interaction unlabeled unless response opportunity and interpretation are sufficiently constrained.

Explicit negative actions such as Not Interested, Hide, Mute, Unfollow, Leave, Report, or Block are more intentional than pure absence, but their scope still matters. They can manage a topic, frequency, relationship, safety boundary, or recommendation system rather than express one global judgment of creative quality.

### 5.6 Behavior-to-mechanism bridge

Do not translate platform observations directly into writing tactics.

Avoid:

```text
platform values sends
→ ask people to send

watch time matters
→ make content longer

comments matter
→ add question bait
```

Use:

```text
OBSERVED EVENT / PLATFORM SIGNAL
↓
provenance + response opportunity
↓
interaction semantics + topology + cost
↓
plausible motives / competing explanations
↓
strategically useful human value, if any
↓
content / representation mechanism
↓
execution
↓
downstream evidence
```

Possible value hypotheses include instrumental usefulness, reference value, identity expression, relationship support, coordination, entertainment, participation, uncertainty reduction, or task completion. They are hypotheses, not a mandatory taxonomy.

Ask:

> What truthful property of the content or representation would make this action worthwhile for the right person in this context?

### 5.7 State transitions

Use a compact state-transition view when sequence matters:

```text
STATE(t-1)
+ relevant history
↓
encounter
↓
interaction / non-interaction
↓
STATE(t)
↓
possible future delivery, permission, or behavior
```

An action can create a new state, reinforce an existing state, reveal a state that already existed, or merely trigger expression of an accumulated state.

Therefore:

```text
CURRENT EVENT
≠ MEMORYLESS RESPONSE

TRIGGER
≠ ACCUMULATED CAUSE

LAST OBSERVED TOUCH
≠ SOLE CAUSE
```

Sequential recommendation research supports treating ordered interactions and evolving preferences as consequential rather than isolated user-item events [R41]. This practitioner map does not imply that every production system uses one formal state-transition model.

---

## 6. Layer 3 — Governance, eligibility, and effective platform state

This layer asks what the platform or community allows, suppresses, exposes, hides, or parameterizes before ordinary performance is interpreted.

### 6.1 Visibility and participation are typed

Keep these states separate when material:

```text
HOSTED / ACCESSIBLE
object exists or can be directly retrieved

DIRECTLY DISCOVERABLE
reachable by profile, direct link, Search, or another path

RECOMMENDATION-ELIGIBLE
allowed into a recommendation inventory

SURFACE-ELIGIBLE
allowed on a particular surface

RECIPIENT-ELIGIBLE
allowed to a particular audience / policy class

PARTICIPATION-ELIGIBLE
allowed to perform a particular action or publish in a context

MONETIZATION / COMMERCIAL ELIGIBILITY
allowed into a specific commercial state

DEMOTED / REDUCED
intentionally given less visibility

ORDINARY LOW RANK
eligible but not competitive enough in ordinary ranking
```

Never ask only `eligible = yes/no`. Ask eligible for what, for whom, where, and when.

Therefore:

```text
HOSTED
≠ DISCOVERABLE
≠ RECOMMENDABLE
≠ PARTICIPATABLE
≠ MONETIZABLE
```

A reach decline alone does not establish platform suppression [R31].

### 6.2 Governance can parameterize mediation and observability

Governance does more than remove or allow content. It can alter:

- default sort;
- score visibility;
- comment collapse/filtering;
- participation gates;
- recommendation eligibility;
- representation visibility;
- action availability;
- recipient access;
- commercial state.

Therefore the six layers are analytical dimensions, not a strict pipeline. Governance can configure what later users see, what they can do, and how a ranking or presentation environment behaves.

### 6.3 Effective state can be relative

Do not assume one object has one globally visible state.

Effective state can vary by:

```text
observer
role
recipient
market
surface
session
time
policy regime
representation
```

A moderator and ordinary user can observe different object states. One recipient can have a different participation right from another. A session begun before a platform-setting change can have different affordances from a later session.

Ask only when material:

> State for whom, where, and when?

### 6.4 Delivery and commercial mode

Separate at least when consequential:

- organic;
- paid / boosted;
- sponsored / branded;
- commerce-integrated;
- community participation;
- notification / relationship delivery;
- embedded / external delivery.

Evidence from one mode should not silently become a rule for another.

The same object can accumulate observations across several delivery modes. Preserve delivery history before calling artifact-level metrics purely organic or purely paid.

---

## 7. Layer 4 — Machine mediation and recommendation

This layer provides enough recommender-systems structure to make defensible decisions without pretending to reverse-engineer exact production algorithms.

### 7.1 Human representation and machine representation are different

Keep three concepts separate:

```text
HUMAN CONTENT MEANING
what the artifact means to people / strategy

CONTENT REPRESENTATION
what package or rendition is actually presented

SYSTEM-SPECIFIC MACHINE REPRESENTATION
how a particular machine system may encode or match the object
```

Multimodal recommender systems can use text, image, audio, video, metadata, interaction, and fused features [R42]. But capability in one system does not establish usage or weight in another.

Invariant:

```text
SYSTEM A CAN EXTRACT FEATURE X
≠ SYSTEM B REPRESENTS X THE SAME WAY
≠ SYSTEM B USES X
≠ X HAS MATERIAL RANKING WEIGHT
```

OCR or ASR in a policy system does not prove spoken keywords boost a feed ranker. Semantic matching in Search does not establish the same representation or weight in a recommendation surface.

Do not create a separate `machine legibility` ontology. The practical check is simply whether relevant systems can plausibly represent or match the subject where evidence says that matters.

### 7.2 Retrieval, ranking, and re-ranking

A common recommender architecture distinguishes conceptually:

```text
CANDIDATE GENERATION / RETRIEVAL
what enters the candidate set?

SCORING / RANKING
how competitive are candidates for this context?

RE-RANKING / CONSTRAINTS
how do diversity, freshness, safety, repetition,
provider, policy, or other objectives alter final ordering?
```

Implementations differ.

For practitioner diagnosis, it can be useful to ask:

```text
RETRIEVABILITY
could this object enter a relevant candidate space?

RANKABILITY
if retrieved, how competitive could it be?
```

These are explanatory aids, not formal platform states.

### 7.3 Ranking signal is not objective or writing instruction

A platform can use watch time, comments, shares, likes, skips, profile visits, purchases, or other behaviors without optimizing any one of them in isolation. Multi-stakeholder and multi-behavior research reinforces that real recommenders can involve multiple objectives [R34][R40].

Therefore:

```text
RANKING SIGNAL
≠ RANKING OBJECTIVE
≠ WRITING INSTRUCTION
```

Translate a consequential signal through Layer 2's behavior-to-mechanism bridge.

A user action can also be partly an attempt to manage or retrain the recommender. Therefore `user action ≠ pure content preference` when system-control intent is plausible.

### 7.4 Exploration, cold start, and adaptive opportunity

Recommendation systems often balance exploitation of known promising options with exploration of uncertain/new options.

Cold start can apply to:

- a new user;
- a new object;
- a new representation;
- a new creator/provider;
- a new product;
- a new topic relationship.

Early performance under exploratory allocation can be unstable as an estimate of mature performance.

### 7.5 Recommendation scope

Not every recommender selects content. A system can recommend:

- posts / videos;
- creators / accounts;
- communities;
- comments;
- search queries;
- LIVE sessions;
- notifications;
- products;
- creator opportunities;
- collaborators;
- commercial offers.

Ask:

> What exactly is this system choosing and presenting to whom?

A ranked comment thread inside a video or a ranked chat inside a live object is simply a composed/nested mediation environment. Represent the outer object, inner surface, audience state, and relevant ranking system rather than inventing another primitive.

---

## 8. Layer 5 — Stakeholders, typed mediation edges, and feedback dynamics

This layer asks how platforms mediate relationships among viewers, creators, communities, brands, sellers, products, and the platform itself.

### 8.1 Platform mediation graph

Multi-stakeholder recommendation research establishes that users are not always the only parties whose objectives matter [R34].

For complex work, map only the consequential typed edges:

```text
VIEWER ↔ CONTENT
VIEWER ↔ CREATOR
VIEWER ↔ COMMUNITY
VIEWER ↔ PRODUCT
CREATOR ↔ PRODUCT
SELLER ↔ CREATOR
BRAND ↔ CREATOR
OBJECT ↔ PAID / COMMERCE SYSTEM
```

Label the edge by what actually changes or transfers.

Examples:

```text
viewer --[follows]--> creator
comment --[changes credibility context]--> later reader
video --[creates memory / intent]--> later search
organic object --[authorized reuse]--> paid delivery
vote --[changes reputation / visibility state]--> future opportunity
```

Do not draw a causal arrow merely because two events occur in sequence.

### 8.2 Cross-environment transfer is a state-transition question

Do not maintain `spillover carrier` as a separate runtime primitive. When one environment appears to affect another, ask what crossed the boundary:

- human memory / awareness / trust / intent;
- relationship state;
- system state / interaction history / eligibility;
- evidence or meaning;
- the object itself;
- commercial state.

Then preserve:

```text
SOURCE ENVIRONMENT
→ WHAT CHANGED / MOVED
→ DESTINATION ENVIRONMENT
→ DOWNSTREAM OUTCOME
```

Cross-channel research supports treating carryover as a legitimate possibility in specific contexts [R45][R46]. Co-movement alone does not establish causal spillover.

### 8.3 Provider-side state and algorithmic management

Distribution has a supply side. Creators/providers can receive unequal opportunity through recommendation, eligibility, reputation, monetization, campaign access, or other platform states [R34][R35].

Do not create a new primitive for every badge, creator score, karma state, reliability tier, or campaign status. Represent it as actor/object platform state with the scope and downstream permission/opportunity it changes.

### 8.4 Platform guidance and creator adaptation

Platforms can advise creators through best-practice surfaces, trend tools, Search insights, content-gap suggestions, diagnostics, exemplars, or pre-publish checks.

Creator research shows adaptation to algorithmic environments and formation of folk theories about visibility [R36]. Treat platform guidance as evidence with a source and objective, not as an independent causal law.

Ask what the guidance is trying to improve:

- reach;
- followers;
- watch time;
- GMV;
- policy compliance;
- creator retention;
- platform monetization;
- actual business outcome.

### 8.5 Feedback dynamics

Do not maintain a separate ontology for every loop. Use one feedback principle:

> A current observation or action can change future human, creator, governance, or recommender state.

Common instances include:

```text
platform exposure
→ user behavior
→ possible system update
→ future exposure

platform exposure
→ user beliefs / controls
→ changed feedback or preference settings
→ future exposure

creator publishes
→ metrics / guidance
→ creator changes supply
→ future content

moderation action
→ contributor state
→ future participation
```

Importantly:

```text
SAME OBSERVED HUMAN ACTION
≠ SAME DOWNSTREAM SYSTEM-LEARNING EFFECT
```

Whether and how an event updates a system can depend on delivery context, policy, surface, privacy mode, logging, or model design.

---

## 9. Layer 6 — Evidence generation, metrics, time, and causal scope

This layer is central to the handbook because platform observations are generated inside the system being studied.

### 9.1 Performance is conditional, not intrinsic

Observed performance is produced by an interaction among object, representation, audience state, platform allocation, and available response mechanisms.

Use the practitioner decomposition:

```text
OBSERVED PERFORMANCE
is conditional on

object / content state
× representation
× audience / pre-outcome state
× exposure policy
× surface / position
× response opportunity
× competing inventory
× platform / governance state
× delivery mode
× time / relevant history
× prior feedback
```

This is not a structural causal equation. It is a reminder not to treat performance as an intrinsic property of the artifact.

### 9.2 Exposure, selection, position, and missing feedback

Recommendation data is generated under selection mechanisms, including prior recommender actions [R32]. Position can influence implicit behavior [R33]. Missing-not-at-random research further shows that absence of a click can reflect non-exposure or selective exposure rather than a clean negative preference label [R44].

Therefore:

```text
LOW ENGAGEMENT
≠ NECESSARILY LOW AUDIENCE INTEREST

NO OBSERVED ACTION
≠ NEGATIVE ACTION
```

Possible alternatives include low exposure, different audience composition, position/surface changes, lack of response opportunity, role/permission constraints, policy/eligibility differences, delivery-mode changes, ordinary ranking competition, or genuinely weaker fit.

### 9.3 Observation record / metric provenance

Before interpreting a metric, reconstruct only the provenance fields that can change the conclusion.

A useful observation record can include:

```text
OBJECT / CONTENT STATE
what artifact and state generated the event?

REPRESENTATION
which package or rendition was encountered?

SURFACE / DELIVERY CONTEXT
where and how was it encountered?

AUDIENCE / PRE-STATE
which people or relationship state?

EXPOSURE + RESPONSE OPPORTUNITY
what action was actually possible?

INTERACTION PROVENANCE
human / representative / automated / coordinated / unknown?

ALLOCATION REGIME
fixed, ranked, adaptive, exploratory, paid, mixed?

OBSERVATION UNIT
view, device, account, session, estimated person, purchase, etc.?

TIME SEMANTICS
exposure time, event time, reporting time, maturity horizon?

ATTRIBUTION RULE
which touches are eligible for credit?
```

Add market, policy state, position, account state, or other fields only when material.

This compresses `metric provenance`, `interaction provenance`, `delivery mixture`, `outcome maturity`, and attribution context into one observation record rather than separate mandatory schemas.

### 9.4 Observation unit is not automatically a person

Do not assume:

```text
LOGGED EVENT
= DEVICE
= ACCOUNT
= HUMAN
```

A view can contain co-viewing; one person can generate events across devices; unique-person metrics can be modeled estimates rather than direct counts.

Always use the metric's documented unit when a decision depends on audience size, frequency, conversion rate, or person-level inference.

Likewise:

```text
SAME METRIC LABEL
≠ SAME RESPONSE OPPORTUNITY
≠ SAME SEMANTICS ACROSS FORMATS / SURFACES
```

### 9.5 Displayed feedback can become future encounter context

Metrics are not always passive outputs. Visible scores, comment counts, badges, reputation, popularity labels, or replay indicators can become part of the next viewer's encounter and can sometimes influence future behavior or visibility.

Therefore distinguish:

```text
SYSTEM FEEDBACK STATE
what aggregate feedback exists?

DISPLAYED FEEDBACK STATE
what feedback is visible to this observer?
```

and remember:

```text
DISPLAYED METRIC
CAN BECOME PART OF A LATER TREATMENT / ENCOUNTER
```

Do not infer a causal social-proof effect without evidence for the setting.

### 9.6 Adaptive exposure, coordination, and interference

Platforms can expand or change exposure based on earlier outcomes. Adaptive experiment research shows that adaptively collected data requires different inference from fixed allocation [R38].

Distinguish:

```text
PLATFORM-NATIVE PROBE
exploratory evidence

ADAPTIVE ROLLOUT
exposure changes based on observed response

RANDOMIZED ADAPTIVE EXPERIMENT
randomization exists and inference handles adaptivity

CONTROLLED A/B EXPERIMENT
explicit comparable treatment assignment and measurement
```

Do not call all four A/B tests.

In social systems, one person's treatment can affect another person's exposure or outcome through sharing, comments, replies, network diffusion, or coordinated activity. Causal inference under interference treats this as a distinct problem [R39].

Also preserve interaction-set provenance when relevant:

```text
REAL HUMAN ACTIONS
≠ INDEPENDENT ORGANIC ACTIONS
```

Coordination, incentives, duplication, or organized brigading can make aggregate behavior misleading even when individual clicks are human-generated.

### 9.7 Outcome maturity and temporal attribution

Outcomes do not all reveal themselves immediately. Delayed-feedback research shows that conversions can arrive long after an initiating interaction, leaving recent observations incomplete [R47].

Ask:

> Has enough time passed for this outcome to be interpreted under the current job and measurement regime?

Therefore:

```text
NO OUTCOME YET
≠ NO OUTCOME
```

Preserve when material:

```text
EXPOSURE / TOUCH TIME
EVENT TIME
REPORTING TIME
ATTRIBUTION WINDOW / RULE
MATURITY HORIZON
```

Customer-journey research models carryover from earlier touches rather than assuming the last observed touch explains a conversion [R45].

Therefore:

```text
TEMPORAL PROXIMITY
≠ ATTRIBUTION

LAST TOUCH
≠ SOLE CAUSE

ATTRIBUTED
≠ INCREMENTAL
≠ CAUSAL
```

An intermediate state such as follow, signup, click, or purchase can also have later consequences such as inactivity, unsubscribe, refund, or retention. Match the horizon to the marketing job.

### 9.8 Effect, observation, and credit location

When journeys cross environments, keep three locations separate:

```text
EFFECT LOCATION
where the relevant state may have changed

OBSERVATION LOCATION
where the downstream behavior became measurable

CREDIT LOCATION
where a reporting system assigned the outcome
```

They can differ.

Therefore:

```text
OBSERVED IN CHANNEL B
≠ CREATED BY CHANNEL B

CROSS-CHANNEL CO-MOVEMENT
≠ CAUSAL SPILLOVER

MORE MEASURABLE
≠ MORE CAUSALLY VALUABLE
```

Also distinguish object transfer from effect transfer. An artifact can physically move or be reused; alternatively, human/system state can carry forward while the artifact itself never moves.

### 9.9 Current comparable evidence

The old rule `local evidence > generic benchmark` is too crude.

Prefer current, comparable local evidence when it matches the decision context well.

Comparability can depend on:

- object / representation;
- surface;
- account / governance state;
- audience / relationship;
- response opportunity;
- recommendation regime;
- delivery mode;
- market;
- period;
- objective;
- metric definition;
- history / maturity horizon.

Older local evidence can be less useful than current platform evidence when the regime changed materially.

### 9.10 Evidence classes and scope

Classify evidence before using it.

```text
CURRENT PLATFORM FACT
official product documentation, policy, engineering disclosure,
or observable capability; time-sensitive and scoped

CURRENT COMPARABLE LOCAL EVIDENCE
actual account/community/campaign evidence generated
under a sufficiently comparable regime

SCOPED OBSERVED PATTERN
measured first- or third-party pattern with population,
period, metric, surface, and delivery scope preserved

PRACTITIONER HEURISTIC
useful but weakly established operational belief

FOLKLORE
unsupported algorithm story or fixed-number tactic
```

Do not force a universal scientific ordering when methods differ. Prefer the evidence that is both methodologically appropriate and decision-relevant.

A useful platform claim should preserve, when material:

```text
source
source date
platform / system / surface
object / representation
actor / recipient class
delivery mode
market / policy regime
objective
time / history scope
known uncertainty
```

---

# Part II — Durable invariants

## 10. Minimal invariants worth keeping in runtime reasoning

The compression pass keeps a small set of high-value distinctions.

```text
OBJECT IDENTITY
≠ CONTENT REPRESENTATION
≠ ENCOUNTER SURFACE
```

```text
VISIBLE PUBLISHING IDENTITY
≠ OPERATIONAL ACTOR
```

```text
RELATIONSHIP
≠ DELIVERY
≠ PARTICIPATION PERMISSION
```

```text
HOSTED
≠ DISCOVERABLE
≠ RECOMMENDABLE
≠ ORDINARY HIGH RANK
```

```text
OBSERVED ACTION
≠ MOTIVE
≠ SATISFACTION
≠ CONTENT QUALITY
```

```text
OBSERVED ENGAGEMENT
≠ ESTABLISHED ORGANIC HUMAN PREFERENCE
```

```text
NO ACTION
≠ NEGATIVE ACTION
```

```text
RANKING SIGNAL
≠ RANKING OBJECTIVE
≠ WRITING INSTRUCTION
```

```text
PLATFORM CAPABILITY
≠ SYSTEM-SPECIFIC USE
≠ MATERIAL WEIGHT
```

```text
CURRENT EVENT
≠ MEMORYLESS RESPONSE
```

```text
LAST TOUCH
≠ SOLE CAUSE
```

```text
ATTRIBUTED
≠ INCREMENTAL
≠ CAUSAL
```

```text
METRIC / LOGGED UNIT
≠ AUTOMATICALLY HUMAN UNIT
```

```text
MORE MEASURABLE
≠ MORE CAUSALLY VALUABLE
```

```text
PLATFORM GUIDANCE
≠ INDEPENDENT BEST-PRACTICE EVIDENCE
```

Do not memorize the list as a checklist. Invoke only the distinction that can prevent a material error.

---

# Part III — Operational use

## 11. Fast path for simple platform writing

Do not make every caption or social post traverse the full model.

If the user supplies a narrow job and sufficient source material, use:

```text
CURRENT JOB
→ PLATFORM / SURFACE IF MATERIAL
→ READER STATE IF MATERIAL
→ SOURCE / CLAIM BOUNDARY
→ OBJECT / REPRESENTATION ROLE IF MATERIAL
→ DRAFT
```

Examples:

- rewriting a supplied caption for naturalness does not require recommender analysis;
- a simple release announcement may require only identity, audience context, key fact, and next action;
- a short community reply should not trigger an ICP exercise unless audience choice is unresolved;
- a caption for a strong visual may need only the missing context rather than a second full message.

Depth should scale with consequence and environmental uncertainty.

---

## 12. Deeper path for consequential content strategy

For a recurring content system, launch, community-entry plan, creator collaboration, platform strategy, or important diagnosis, resolve only dimensions that can change the decision.

A compact dependency map is:

```text
JOB + SOURCE / AUTHORITY
↓
ACTOR + OBJECT + REPRESENTATION
↓
AUDIENCE STATE + TYPED EDGES
↓
GOVERNANCE / MEDIATION STATE
↓
DESIRED INTERACTION / STATE TRANSITION
↓
MESSAGE + PROOF + ASK
↓
OBSERVATION RECORD
↓
BOUNDED LEARNING
```

This is not a mandatory linear pipeline. Provenance, history, attribution, interference, and spillover analysis should be loaded only when they can change the conclusion.

---

## 13. Measurement follows the marketing job

Potential outcomes include:

- qualified reach;
- completion / watch behavior;
- saves;
- private sends;
- public shares;
- comments or replies;
- profile visits;
- follows / subscriptions;
- search discovery;
- qualified clicks;
- signups;
- purchases;
- conversations started;
- evidence collected;
- community acceptance;
- creator / brand match quality;
- downstream retention or sales outcomes.

Separate:

```text
DISTRIBUTION PERFORMANCE
Was the object / representation exposed and consumed?

AUDIENCE / RELATIONSHIP RESPONSE
Did the right people engage or transition state,
and did they have a meaningful response opportunity?

PERSUASION / TASK PERFORMANCE
Did the communication do its job?

BUSINESS OUTCOME
Did it advance the actual objective
at the relevant maturity horizon?

LEARNING VALUE
Did the observation reduce a consequential uncertainty?
```

A high-reach object can fail commercially. A low-volume discussion can succeed strategically. A high-search topic can be weak buyer demand. A missing action can remain unlabeled. A conversion reported in one channel can be history-conditioned elsewhere.

---

## 14. Compact content-context record

Use an explicit intermediate record only when a complex task benefits from one.

```text
CONTENT CONTEXT

Job / objective:
Source / authority:
Actor / publishing identity:
Operational provenance if material:

Object / current state:
Representation if material:
Human meaning / message allocation:
Lineage / portability if material:

Audience state / envelope:
Typed relationship-delivery-permission edges:
Relevant history / intent provenance if material:
Desired interaction / state transition:

Governance / eligibility / delivery state:
Relevant mediation system / surface:
Machine-representation evidence if material:
Cross-environment edge if material:

Observation record if learning from performance:
Primary success metric:
Claim / policy constraints:
```

Do not fill unknown fields with invented precision. Omit dimensions that cannot change the decision.

---

## 15. Diagnostic record for weak or changing performance

When a platform metric changes, do not jump directly to creative replacement.

Check only the material items:

```text
1. OBSERVATION RECORD
What changed, what was counted, and in what unit/time regime?

2. OBJECT / REPRESENTATION
Same object state, title/thumbnail/preview/rendition, format, or attachment?

3. EXPOSURE + RESPONSE OPPORTUNITY
Same surface, position, audience mix, permission, and action availability?

4. INTERACTION PROVENANCE / SEMANTICS
Organic human, representative, coordinated, automated, unknown?
Action, explicit negative, proxy, or mere absence?

5. GOVERNANCE / MEDIATION STATE
Same eligibility, moderation, ranking surface, delivery mode,
account state, and allocation regime?

6. AUDIENCE / HISTORY
Same relationship, intent, prior exposure, and pre-outcome state?

7. TEMPORAL / ATTRIBUTION SCOPE
Has the outcome matured?
Same reporting and attribution rules?
Could effect, observation, and credit be in different environments?

8. CONTENT MECHANISM
Did meaning, proof, expectation, or representation-content fit change?

9. COMPETING EXPLANATIONS
What else changed at the same time?

10. DISCRIMINATING CHECK
What evidence would best separate the leading explanations?
```

Use `handbook/05-diagnosis-causality-and-experimentation.md` when causal attribution or experiment design becomes material.

---

## 16. Platform-native adaptation

Cross-platform reuse should preserve strategic meaning while adapting only the environment-specific execution that matters.

Do not merely shorten copy, change emoji density, or swap hashtags.

Adapt when justified:

- publishing actor;
- amount of context;
- object;
- selection / consumption representation;
- modality and message allocation;
- proof placement;
- CTA / action affordance;
- link handling;
- community fit;
- terminology;
- governance / eligibility constraints;
- measurement.

The same strategic message can legitimately become different platform-native objects because audience state, representation, surface, permission, and response opportunity differ.

---

## 17. Platform modules and the core-change rule

The durable model should remain stable while platform modules hold current facts, surfaces, product-specific affordances, policy states, and recommendation disclosures.

Current modules:

- `platforms/facebook.md`
- `platforms/linkedin.md`
- `platforms/instagram.md`
- `platforms/tiktok.md`

Platform modules should use the shared vocabulary rather than create a separate framework for each product.

Keep evidence classes explicit:

```text
DURABLE REASONING
what general distinction applies?

CURRENT PLATFORM FACT
what does the platform currently disclose or allow?

SCOPED OBSERVATION
what pattern was observed, in which population/regime?

LOCAL EVIDENCE
what does this account/community/campaign show?

UNKNOWN
what remains partially observable?
```

Change the durable core only when a new platform case cannot be represented without materially distorting the decision.

A strong compression test is:

```text
new finding
↓
can existing thing + edge + state + provenance + scope + transition represent it?

YES
→ keep platform-specific or derived

NO
→ search for an established conceptual parent
→ only then consider a new durable primitive
```

---

## 18. Final content-environment check

Before consequential platform work is finalized, ask only the relevant questions:

1. Does the contribution have a clear marketing job?
2. Is the actor entitled to make the claims, and is operational provenance relevant?
3. Are object identity, representation, and surface distinguished where they can change the decision?
4. Is the intended audience distinguished from the broader audience envelope where necessary?
5. Are relationship, delivery, and participation permission separated where material?
6. Does the contribution fit the audience's intent/state and the environment's rules/norms?
7. Is meaning allocated to the right carriers and is expected travel/portability handled?
8. Are hosting, discoverability, eligibility, governance, ranking, and business outcome kept separate?
9. Are claims about machine processing scoped to the actual system for which evidence exists?
10. Is any ranking or engagement signal translated through human value rather than directly into a writing hack?
11. Was there a meaningful response opportunity, and is interaction provenance adequate before interpreting action or silence?
12. Is the observation record sufficient: representation, surface, audience, unit, delivery, time, and attribution where material?
13. Are adaptive exposure, coordination, interference, history, or regime changes material?
14. If the journey crosses environments, are state transfer, observation location, and credit location kept distinct?
15. Is the final decision still truthful, scoped, and proportionate to the evidence?

The goal is not to satisfy a giant platform checklist. The goal is to make a context-appropriate marketing decision with a small durable reasoning core, while preserving the complexity that genuinely changes action or inference.
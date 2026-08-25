# 13 — Search & Discovery Architecture

## 1. Scope: decide how information and entities can become discoverable

Use this chapter when the open decision concerns how an information object, entity, source, page, document, or other non-commerce subject can become available to, retrieved by, selected by, represented through, or observed within a discovery system.

This is a bounded specialist layer over the shared Chapter 08 grammar. It is **not** a second platform ontology and it is not a synonym for SEO.

Use the same durable parent roles:

```text
ACTOR / SOURCE
OBJECT
REPRESENTATION
AUDIENCE STATE
TYPED RELATIONSHIP / ACCESS / DELIVERY EDGE
INTERACTION ACT
PLATFORM / MEDIATION STATE
OBSERVATION RECORD

+ provenance
+ scope / relativity
+ history / state transition
```

For discovery work, use local names only when they make the decision clearer:

```text
OBJECT
→ page / document / article / entity / business / source /
  account / media object / other independently identified subject

REPRESENTATION
→ source page / indexed representation / snippet / result card /
  entity card / answer fragment / citation / preview / other surfaced form

AUDIENCE STATE
→ current information need / task / knowledge / exploration state

PLATFORM / MEDIATION STATE
→ known / access / processing / index / retrieval / selection /
  canonicalization / ranking / recommendation / grounding state

OBSERVATION RECORD
→ impression / position / click / referral / citation /
  grounding-query telemetry / other surface-defined observation
```

Do not instantiate every implementation noun as a durable thing. A crawler, index shard, embedding, query rewrite, ranking feature, answer component, or internal model is not automatically a new Marketing Practitioner primitive.

The central thesis is:

> Discovery is a scoped mediation problem between a human/context state and system-held representations of the world. A published object does not automatically become retrievable, a retrieved object does not automatically become selected, and a selected source does not automatically become safe evidence for a system-generated answer.

A second operating principle follows:

> Diagnose the earliest unresolved discovery boundary before rewriting the artifact or inferring demand, relevance, or causal impact from downstream telemetry.

The field evidence for this chapter includes official current documentation from Google, OpenAI, Perplexity, and Bing plus established information-retrieval/user-behavior research [SD01–SD14]. The specialist synthesis is a practitioner model; it is not one validated universal theory of every search, recommendation, or answer engine.

### Search is one discovery mode

Do not begin every discovery task with a keyword.

```text
DISCOVERY
├─ explicit-query search
├─ exploratory search / reformulation
├─ recommendation
├─ interest-conditioned / queryless surfacing
├─ local or entity discovery
└─ system-mediated answer / grounding
```

Use:

```text
SEARCH
⊂ DISCOVERY
```

This chapter owns generic discovery semantics. Chapter 09 continues to own product/listing/catalog/offer/shopper identity and commerce-specific product discovery. Chapter 08 remains the parent for general platform mediation and feedback dynamics.

### Fast path

Do not load deeper discovery guidance merely because a task mentions `SEO`, `Google`, `search`, `ranking`, `AI`, `ChatGPT`, `citation`, or another discovery noun.

If the user has already supplied the relevant strategy/facts and only asks for a bounded transformation whose discovery mechanics cannot change the answer, stay narrow.

Example:

```text
“Shorten this approved meta description.”
→ supplied transformation
→ do not reopen discovery architecture
```

But:

```text
“This page is indexed but rarely appears in AI answers.
Should we rewrite it?”
→ availability / selection / commitment may be open
→ diagnose those boundaries before rewriting
```

---

## 2. Discovery need, expression, and context

The first question is not “what keyword should we target?” Ask:

> What information, entity, or object could matter in the current human, task, or discovery context?

Preserve only the distinctions that can change the current decision:

```text
PROBLEM / TASK
≠ INFORMATION NEED
≠ CURRENT KNOWLEDGE STATE
≠ USER EXPRESSION
≠ QUERY
≠ SYSTEM INTERPRETATION
≠ RETRIEVAL FORMULATION
```

Information-retrieval research has long treated information seeking as more than exact query matching: users can be unable to state a need perfectly, can revise a query as they learn, and can encounter useful information while pursuing a broader task [SD11][SD12].

### 2.1 Query is evidence of expression, not a complete need

A query can be:

- underspecified;
- ambiguous;
- a temporary articulation of a changing need;
- influenced by prior content, recommendation, advertising, social exposure, or system suggestions;
- one step in an exploratory sequence;
- absent entirely in queryless discovery.

Therefore:

```text
QUERY
≠ UNIQUE INTENT
```

and:

```text
LATER QUERY
≠ PROOF OF PRIOR INDEPENDENT DEMAND
```

Use Chapter 01 / 02 when the open question is whether search behavior supports a broader customer, segment, or market-demand inference.

### 2.2 Query modality and retrieval formulation are different

The user's input can be text, image, voice, conversation, location/context, or no explicit query. The discovery system can then create internal retrieval formulations that differ from the literal input.

Google documents query fan-out for generative Search features: one user question can lead to several related retrieval queries [SD02].

Keep:

```text
USER EXPRESSION
≠ RETRIEVAL FORMULATION
```

Do not optimize every page for imagined internal fan-out phrases. A hidden/system-generated query is evidence about the discovery mechanism only when the provider actually exposes it or comparable evidence supports the inference.

### 2.3 Actual human state and system-inferred state

Discovery systems can use history, location, language, device, explicit preferences, or other signals to infer what may be useful. Do not convert that inference into a stable fact about the person.

```text
ACTUAL HUMAN STATE
≠ SYSTEM-INFERRED HUMAN STATE
```

General preference construction and feedback-loop theory remain Chapter 08 concerns. This chapter keeps only the discovery-local consequence: history or personalization can change selection without proving the current need was correctly inferred.

Use:

```text
PERSONALIZED
≠ CORRECTLY PERSONALIZED
```

and:

```text
RESULT DIFFERENCE
≠ AUTOMATIC PROOF OF PERSONALIZATION
```

Current query/context, market, device, language, location, surface, and system changes can also alter discovery outcomes.

---

## 3. Scoped discovery availability

Before asking why an object is not ranked, cited, clicked, or converting, ask whether it is actually available to the relevant discovery system under the relevant scope.

Use this ladder as a diagnostic vocabulary, **not** a guaranteed linear platform pipeline:

```text
OBJECT EXISTS
≠ PUBLISHED
≠ SYSTEM KNOWS OF IT
≠ ACCESSIBLE FOR THIS PURPOSE
≠ PROCESSED
≠ HELD IN A RETRIEVABLE SYSTEM REPRESENTATION
≠ RETRIEVABLE FOR THIS CONTEXT
```

Google explicitly separates discovery/crawling, indexing, and serving and does not guarantee completion of each stage merely because technical requirements are met [SD01].

### 3.1 Do not create global discoverability

Avoid:

```text
discoverable = true
```

A material availability state can depend on:

```text
system / provider
surface / product
object representation
purpose
crawler or fetch path
policy / access state
market / locale
current time
```

OpenAI separates search crawling from training controls, and Perplexity documents different indexing/search and user-triggered fetch roles [SD07][SD08].

Therefore:

```text
PUBLIC
≠ ACCESSIBLE TO EVERY SYSTEM FOR EVERY PURPOSE
```

and:

```text
INDEXING ACCESS
≠ USER-TRIGGERED FETCH ACCESS
≠ TRAINING ACCESS
```

### 3.2 Publisher action and system state are different

Freeze:

```text
PUBLISHER CONTROL
≠ SYSTEM CONTROL
```

A publisher can:

- create or update an object/representation;
- link to it;
- submit a sitemap or update signal;
- express a canonical preference;
- allow or block a crawler or purpose where supported;
- provide structured or machine-readable information.

Those actions can affect system eligibility or evidence without commanding:

- when the system discovers or reprocesses the object;
- whether it indexes or retains it;
- which representative identity it chooses;
- whether it retrieves or selects it;
- whether it ranks, recommends, cites, or commits it into an answer.

Provider language such as `eligible`, `signal`, `may`, `can`, or `not guaranteed` must keep that strength. Do not silently rewrite it into “do X and you will rank/cite.”

### 3.3 Object identity, source representation, and system-selected identity

Keep:

```text
REAL OBJECT / ENTITY STATE
≠ SOURCE REPRESENTATION
≠ SYSTEM-HELD STATE / REPRESENTATION
≠ SURFACED REPRESENTATION
```

Google canonicalization is one concrete case: multiple URLs can be clustered and Google can select a canonical different from the publisher preference [SD04].

Therefore:

```text
URL
≠ UNIVERSAL INFORMATION-OBJECT IDENTITY
```

and:

```text
PUBLISHER-PREFERRED REPRESENTATIVE
≠ SYSTEM-SELECTED REPRESENTATIVE
```

Do not invent a separate durable `INDEX_OBJECT` merely because a system holds its own representation. Use `OBJECT + REPRESENTATION + PLATFORM STATE + PROVENANCE + SCOPE`.

### 3.4 Freshness is relational

Do not treat publication age as a freshness score.

```text
AGE
≠ STALENESS
```

and:

```text
SOURCE UPDATED
≠ SYSTEM UPDATED
≠ SURFACE UPDATED
```

An older tutorial can remain fully current. A recently crawled page can contain stale facts about a fast-changing subject. Google Discover explicitly permits older helpful content to resurface when relevant to current interests [SD03].

When freshness changes the decision, ask:

```text
Which proposition or state can change?
Which source supports it?
When did that source become current?
When did the discovery system observe/process it?
What representation is being surfaced now?
```

Do not create numeric freshness confidence unless a supplied method actually defines one.

---

## 4. Retrieval, relevance, selection, and discovery modes

Availability establishes what can participate. Retrieval and selection establish what becomes a candidate and what survives into a particular discovery response.

Keep:

```text
AVAILABLE
≠ RETRIEVED
≠ SELECTED
≠ SURFACED
```

### 4.1 Keyword match is not universal relevance

Do not infer:

```text
contains keyword
→ relevant
```

Relevance can depend on the current information need, task, location, language, entity relation, time, representation, commercial/non-commercial context, and system objective.

Use:

```text
KEYWORD MATCH
≠ RELEVANCE
```

This does not imply keyword/text matching is irrelevant. It prevents collapsing one retrieval signal into the whole discovery objective.

### 4.2 Retrieval, ranking, recommendation, and composition are different system jobs

Depending on the system, a discovery response can involve:

- query understanding / reformulation;
- candidate retrieval;
- filtering or eligibility checks;
- ranking/scoring;
- diversification;
- recommendation;
- vertical/surface selection;
- composition of several result types;
- answer-support retrieval.

Do not turn this list into a universal pipeline. Preserve only the distinction required by the current evidence and decision.

A ranking signal is not automatically a writing instruction. If a provider says a behavior or field is used by one system, do not transfer it across unrelated surfaces, objectives, products, or markets.

### 4.3 Explicit search and queryless discovery share grammar but not entry state

Explicit search begins from a user expression. Queryless discovery can begin from an inferred interest/context state, relationship, recommendation path, or other mediation state [SD03].

Therefore:

```text
DISCOVERY DOES NOT REQUIRE AN EXPLICIT QUERY
```

When a task is about creating/publishing content inside a social or feed environment more broadly, Chapter 08 remains the primary specialist. Use this chapter only when discovery availability/retrieval/selection semantics themselves can change the open decision.

### 4.4 Commerce boundary

Do not use generic discovery to flatten commerce-specific identity.

Example:

```text
“Why does this product variant fail to appear for a marketplace query?”
```

May require:

```text
Chapter 09
→ resolve product / variant / listing / commercial representation

then, only if a generic cross-system discovery question remains:
→ this chapter
```

Current `commerce.*` routes remain the owner for product-search, recommendation, field allocation, agentic commerce, and commerce observation semantics.

---

## 5. Discovery representation and system commitment

Selection does not always produce the same kind of output. Separate two modes when the distinction changes the decision.

### 5.1 Human-selection mode

```text
CANDIDATE
↓
RESULT / SNIPPET / CARD / LINK / ENTITY REPRESENTATION
↓
HUMAN EVALUATES
```

The system presents an option; the human retains responsibility for deciding whether to enter, read, compare, trust, or act.

A selection representation can create expectation before the underlying object is consumed. Therefore the shared Chapter 08 distinction remains important:

```text
OBJECT
≠ REPRESENTATION
≠ ENCOUNTER SURFACE
```

A weak or misleading result representation can change selection without proving that the underlying object is weak.

### 5.2 System-commitment mode

AI answer/search systems can retrieve information and use some of it as support for system-generated content.

Use:

```text
RETRIEVED INFORMATION
↓
EVIDENTIARY FITNESS
↓
SUPPORT SELECTION
↓
ANSWER / SYNTHESIS COMMITMENT
↓
OPTIONAL ATTRIBUTION / CITATION
```

Microsoft's current Bing explanation distinguishes document ranking for human selection from selecting groundable information to support generated answers [SD09].

Freeze:

```text
SURFACING AN OPTION
≠ COMMITTING INFORMATION INTO AN ANSWER
```

and:

```text
RETRIEVED
≠ RELEVANT
≠ EVIDENTIARY FIT
≠ SAFE TO COMMIT
```

### 5.3 Groundability is not marketing proof ownership

When system commitment is material, useful questions can include:

- does the source actually support the proposition?
- is provenance adequate for the assertion?
- is the source current enough for the proposition?
- are material sources contradictory?
- is coverage sufficient or should the system remain uncertain/abstain?

These questions concern the discovery system's support boundary.

Chapter 04 still owns:

> What claim may the marketer legitimately communicate, with what proof and qualification?

Do not route ordinary message/proof work through discovery merely because evidence is involved.

### 5.4 Retrieval, use, support, and citation are different

Keep:

```text
SOURCE RETRIEVED
≠ SOURCE USED
≠ SOURCE SUPPORTS CLAIM
≠ SOURCE CITED
```

A citation can be present while its exact causal role in generation is unknown. A source can support a statement without proving that it caused the model to generate that statement. Do not invent hidden source-use semantics from visible citation alone.

---

## 6. Discovery observation and causal boundary

Treat every discovery metric as an observation produced under a specific surface and measurement regime.

Before interpreting a consequential metric, construct one compact observation record with only the dimensions that can change the conclusion:

```text
SURFACE / SYSTEM
OBSERVED EVENT
EVENT DEFINITION
OBJECT / REPRESENTATION SCOPE
UNIT OF ANALYSIS
AGGREGATION RULE
EXPOSURE / VIEW OPPORTUNITY RULE
TIME / MARKET / DEVICE SCOPE
TELEMETRY COVERAGE OR SAMPLING
ATTRIBUTION RULE
MATERIAL UNCERTAINTY
```

### 6.1 Metric label is not metric semantics

Google Search Console is a useful concrete warning: impression and position semantics can vary by result type/surface, and container results can make `position` mean something different from a simple independent blue-link rank [SD05].

Use:

```text
METRIC LABEL
≠ UNIVERSAL EVENT DEFINITION
```

and:

```text
IMPRESSION
≠ VERIFIED ATTENTION
```

### 6.2 Click is an interaction, not a relevance oracle

Information-retrieval research has repeatedly shown that clicks can be informative while remaining position/trust biased [SD13].

Keep:

```text
CLICK
≠ RELEVANCE
```

A click can reflect:

```text
relevance
× position / exposure opportunity
× representation
× trust in the system
× available alternatives
× current human state
× other context
```

Do not convert CTR directly into content quality.

### 6.3 No click is ambiguous

Search-behavior research on good abandonment shows that a user can satisfy an information need without an external click [SD14].

Keep:

```text
NO CLICK
≠ FAILURE
```

A non-click can mean:

- the answer/snippet was sufficient;
- the result was irrelevant;
- the task was abandoned;
- the user refined the search inside the system;
- the information was consumed without referral;
- another unobserved outcome occurred.

Therefore:

```text
USER DISCOVERY SUCCESS
≠ PUBLISHER REFERRAL SUCCESS
```

### 6.4 Citation is observation, not authority or causal influence

Bing's AI Performance tooling exposes citation and grounding-query telemetry while explicitly warning against reading citation count as simple rank/importance/placement semantics [SD10].

Keep:

```text
CITATION
≠ AUTHORITY
≠ ENDORSEMENT
≠ FAITHFUL SOURCE USE
≠ CAUSAL INFLUENCE
```

and:

```text
OBSERVED GROUNDING-QUERY TELEMETRY
≠ COMPLETE INTERNAL RETRIEVAL ACTIVITY
```

### 6.5 Search interest is not market demand

Google Trends data is sampled/normalized search-interest telemetry, not a scientific poll, absolute customer count, or direct market-size estimate [SD06].

Keep:

```text
SEARCH INTEREST
≠ CUSTOMER COUNT
≠ PURCHASE INTENT
≠ MARKET DEMAND
```

Search activity can also be an **outcome** of prior advertising, media, recommendation, social exposure, word of mouth, product events, or other demand-generation mechanisms. Route broader demand inference to Chapters 01/02 and causal questions to Chapter 05.

### 6.6 Causality belongs to Chapter 05

This chapter can establish:

```text
what the platform recorded
what that event definition means
what it does not establish
```

It does not own:

```text
what would have happened without the discovery exposure
what incremental outcome the exposure caused
```

Use Chapter 05 for those questions.

```text
ATTRIBUTION
≠ INCREMENTALITY
≠ CAUSALITY
```

---

## 7. Diagnosis and handoff rules

When discovery performance is weak or changing, do not begin by rewriting the page/content.

Use a bounded diagnostic path:

```text
1. WHAT IS THE OPEN OUTCOME?
   visibility / citation / referral / qualified visit / other

2. IS THE RELEVANT OBJECT / REPRESENTATION AVAILABLE?
   identity / access / processing / index / freshness / scope

3. IS IT BEING RETRIEVED?
   for this need/context/surface?

4. IS IT BEING SELECTED / SURFACED?
   ranking / recommendation / composition / eligibility where evidenced

5. IS THE REPRESENTATION / COMMITMENT JOB CORRECT?
   human-selection representation or system-grounding fitness?

6. WHAT EXACTLY WAS OBSERVED?
   metric definition / unit / surface / coverage

7. ONLY THEN:
   does another owner need to act?
```

Common handoffs:

```text
customer / segment / demand inference
→ Chapter 01 / 02

message / claim / proof problem
→ Chapter 04

causal effect / incrementality / experiment
→ Chapter 05

platform-native content participation problem
→ Chapter 08 / content.*

product / variant / listing / commerce discovery
→ Chapter 09 / commerce.*

landing-page architecture after entry
→ Chapter 11 / landing-page.*
```

### Example: rank present, AI citation absent

Do not assume “rewrite for AI.”

Check separately:

```text
Google/web ranking state
≠ AI-answer availability state
≠ retrieval state
≠ grounding fitness
≠ citation telemetry
```

Only route to message/content rewriting if evidence localizes the problem there.

### Example: impressions increase, clicks do not

Do not infer declining relevance until the observation definition and surface mix are stable.

Possible explanations include:

- different result/surface mix;
- different visibility opportunity rules;
- changed query/audience mix;
- more in-surface satisfaction;
- representation change;
- ranking/position shift;
- telemetry/instrumentation change;
- actual relevance change.

Use Chapter 05 if the user asks which mechanism caused the movement and evidence requires causal reasoning.

---

## 8. Compact discovery decision record

Retain a discovery decision only when it is consequential enough to affect later execution or learning.

Use the smallest record that preserves the distinction:

```text
DISCOVERY JOB / OPEN DECISION

HUMAN / CONTEXT STATE
relevant task / need / expression provenance

OBJECT / REPRESENTATION
what subject and representation are in scope

DISCOVERY SYSTEM / SURFACE
provider / surface / purpose / market / time when material

AVAILABILITY STATE
known / access / processing / index / freshness / identity uncertainty

RETRIEVAL / SELECTION STATE
what evidence exists about candidate retrieval / selection

REPRESENTATION / COMMITMENT MODE
human-selection or system-commitment

OBSERVATION
surface-defined event / unit / coverage / uncertainty

DECISION
what to change, preserve, test, or leave unresolved

HANDOFF
which owner receives the next open decision, if any
```

Do not create a permanent search-profile schema for every page or customer. Retain only what later decisions need.

---

## 9. Anti-folklore invariants

Keep this set small and operational:

```text
SEARCH
IS ONE MODE OF DISCOVERY

DISCOVERY
DOES NOT REQUIRE AN EXPLICIT QUERY

QUERY
≠ INFORMATION NEED
≠ UNIQUE INTENT
≠ RETRIEVAL FORMULATION

PUBLISHED
≠ SYSTEM-KNOWN
≠ RETRIEVABLE

DISCOVERABILITY
IS SCOPED

PUBLISHER REPRESENTATION
≠ SYSTEM-HELD REPRESENTATION

PUBLISHER-PREFERRED IDENTITY
≠ SYSTEM-SELECTED REPRESENTATIVE

AGE
≠ STALENESS

ACTUAL HUMAN STATE
≠ SYSTEM-INFERRED HUMAN STATE

AVAILABLE
≠ RETRIEVED
≠ SELECTED
≠ SURFACED

RETRIEVED
≠ EVIDENTIARY FIT

SURFACING AN OPTION
≠ COMMITTING INFORMATION INTO AN ANSWER

SOURCE RETRIEVED
≠ SOURCE USED
≠ SOURCE SUPPORTS CLAIM
≠ SOURCE CITED

IMPRESSION
≠ VERIFIED ATTENTION

POSITION
≠ UNIVERSAL OBJECT RANK

CLICK
≠ RELEVANCE

NO CLICK
≠ FAILURE

CITATION
≠ AUTHORITY
≠ ENDORSEMENT
≠ FAITHFUL SOURCE USE
≠ CAUSAL INFLUENCE

SEARCH INTEREST
≠ MARKET DEMAND

ATTRIBUTED OUTCOME
≠ CAUSED OUTCOME

PUBLISHER CONTROL
≠ SYSTEM CONTROL
```

Do not create SEO/GEO/AEO/LLMO ontologies, a global `DISCOVERABLE` boolean, a universal relevance/grounding score, a new funnel, or a new causal framework from these distinctions.

---

## References

See `../references/search-discovery-evidence.md` for [SD01–SD14], evidence scope, and current-provider boundaries.

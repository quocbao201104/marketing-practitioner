# Search & Discovery Architecture — Theory Freeze

Status: **FROZEN FOR BOUNDED SPECIALIST IMPLEMENTATION**  
Freeze date: 2026-08-25  
Repository base: `main@8e77150e589ce95d886ac637d241937d260b1610`

## 1. Research question

Does generic information/entity discovery require a bounded specialist layer in Marketing Practitioner, or can Chapter 08 / existing specialists already support the consequential decisions without material distortion?

The field exploration covered classic web search, exploratory search, queryless discovery, local/entity discovery, AI answer/search systems, crawling/indexing/canonicalization, personalization, retrieval and grounding, surface-specific telemetry, zero-click behavior, citation semantics, and causal boundaries.

The adversarial requirement was strict:

> Do not add a shared primitive, new controller job, or specialist chapter merely because SEO/search is a large practitioner category. Add specialist knowledge only if concrete decision-relevant failures survive composition with the existing shared grammar.

## 2. Freeze verdict

> **SEARCH & DISCOVERY THEORY FREEZE PASSES ADVERSARIAL REFINEMENT.**  
> **BOUNDED SPECIALIST CAPABILITY CONFIRMED.**  
> **NO SHARED GRAMMAR REOPEN.**  
> **NO NEW SHARED PRIMITIVE.**  
> **NO NEW CONTROLLER JOB.**  
> **NO SEO / GEO / AEO / LLMO ONTOLOGY.**

The missing capability is a local specialist owner for discovery-specific semantics, not a missing representational primitive.

## 3. Frozen primary unit

```text
DISCOVERY DECISION
```

Do not use `keyword`, `query`, `SERP`, `SEO page`, `ranking`, or `AI citation` as the universal primary unit.

Use:

```text
SEARCH
=
ONE MODE OF DISCOVERY
```

Discovery can be explicit-query search, exploratory retrieval, recommendation, interest-conditioned/queryless surfacing, local/entity discovery, or system-mediated answer retrieval.

## 4. Frozen five-question model

### Q1 — Discovery need / context

Ask:

> What information, entity, or object could matter in the current human, task, or discovery context?

Preserve when material:

```text
PROBLEM
≠ INFORMATION NEED
≠ USER EXPRESSION
≠ QUERY
≠ SYSTEM INTERPRETATION
≠ RETRIEVAL FORMULATION
```

An explicit user query is optional. One literal query need not imply one unique intent, and a discovery system can reformulate or fan out retrieval internally.

### Q2 — Discovery availability

Ask:

> What object or representation is actually available to this discovery system for this purpose, surface, scope, and time?

Preserve:

```text
EXISTS
≠ PUBLISHED
≠ SYSTEM-KNOWN
≠ ACCESSIBLE
≠ PROCESSED
≠ INDEXED / AVAILABLE
≠ RETRIEVABLE FOR THIS CONTEXT
```

Do not create a global `discoverable = true` state. Discovery availability is scoped by the system, surface, representation, purpose, policy/access regime, market/context, and time when those dimensions can change the decision.

### Q3 — Retrieval / selection

Ask:

> From what is available, what can legitimately become a candidate for this context?

Preserve:

```text
QUERY
≠ RETRIEVAL FORMULATION

KEYWORD MATCH
≠ RELEVANCE

RETRIEVED
≠ SELECTED

ELIGIBLE
≠ GUARANTEED TO SURFACE
```

Search retrieval, rewriting, fan-out, diversification, ranking, filtering, recommendation, and composition are system-specific mechanisms, not shared primitives.

### Q4 — Discovery representation / commitment

Separate two decision modes.

#### Human-selection mode

```text
CANDIDATE
↓
RESULT / CARD / SNIPPET / LINK / OTHER REPRESENTATION
↓
HUMAN EVALUATES
```

#### System-commitment mode

```text
RETRIEVED INFORMATION
↓
EVIDENTIARY FITNESS
↓
SUPPORT SELECTION
↓
SYSTEM COMMITS CONTENT INTO RESPONSE
↓
OPTIONAL ATTRIBUTION / CITATION
```

Freeze:

```text
SURFACING AN OPTION
≠
COMMITTING INFORMATION INTO AN ANSWER
```

A source can be retrievable but not adequate evidence for a system-generated assertion. Grounding can require support, provenance, freshness, conflict handling, coverage, uncertainty, or abstention without transferring marketing claim ownership from Chapter 04.

### Q5 — Discovery observation

Ask:

> What exactly was observed, under which surface, unit, scope, and measurement rule?

Freeze:

```text
PLATFORM OBSERVATION
≠ HUMAN STATE
```

Discovery-specific telemetry semantics belong locally here; causal effect and incrementality remain Chapter 05 concerns.

## 5. Frozen loop

Do not freeze a linear SEO funnel.

```text
DISCOVERY-RELEVANT
HUMAN / CONTEXT STATE
        ↓
DISCOVERY DECISION
        ↓
SCOPED OBJECT /
REPRESENTATION AVAILABILITY
        ↓
RETRIEVAL / SELECTION
        ↓
┌────────────────────┬────────────────────┐
│ HUMAN-SELECTION    │ SYSTEM-COMMITMENT  │
│ MODE               │ MODE               │
└─────────┬──────────┴─────────┬──────────┘
          ↓                    ↓
        DISCOVERY REPRESENTATION
                  ↓
               ENCOUNTER
                  ↓
              OBSERVATION
                  ↓
        UPDATED RELEVANT STATE
                  ↺
```

This is a decision model, not a mandatory platform implementation pipeline.

## 6. Identity, system-state, and freshness discipline

Do not promote `WORLD_MODEL` or `USER_MODEL` to shared primitives.

Preserve when material:

```text
REAL OBJECT / ENTITY STATE
≠ SOURCE REPRESENTATION
≠ SYSTEM-HELD STATE / REPRESENTATION
≠ SURFACED REPRESENTATION
```

and:

```text
ACTUAL HUMAN STATE
≠ SYSTEM-INFERRED HUMAN STATE
```

These distinctions compose from existing `OBJECT`, `REPRESENTATION`, `AUDIENCE STATE`, `PLATFORM / MEDIATION STATE`, provenance, scope, and history.

Freshness is relational:

```text
AGE
≠ STALENESS

SOURCE UPDATED
≠ SYSTEM UPDATED
≠ SURFACE UPDATED
```

Assess freshness relative to the proposition, decision, source, changing world state, system observation state, and time rather than publication date alone.

## 7. Grounding discipline

Freeze:

```text
RETRIEVED
≠ RELEVANT
≠ EVIDENTIARY FIT
≠ SAFE TO COMMIT
```

and:

```text
SOURCE RETRIEVED
≠ SOURCE USED
≠ SOURCE SUPPORTS CLAIM
≠ SOURCE CITED
```

Do not create a universal grounding score.

## 8. Observation invariants

Keep these anti-folklore distinctions when they prevent a material error:

```text
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
≠ CUSTOMER COUNT
≠ MARKET DEMAND

ATTRIBUTED OUTCOME
≠ CAUSED OUTCOME
```

A metric label is not its semantics. Preserve the surface, event definition, unit, aggregation rule, opportunity/view rule, time/scope, telemetry coverage, and attribution rule only when they can change interpretation.

## 9. Publisher/system control boundary

Freeze:

```text
PUBLISHER CONTROL
≠ SYSTEM CONTROL
```

A publisher can create, update, structure, submit, allow/block, or signal a representation. Those actions do not guarantee crawl timing, indexing, canonical selection, retrieval, ranking, recommendation, citation, or answer commitment.

Represent platform documentation with its actual strength: `eligible`, `signal`, `may`, `can`, or `not guaranteed` must not silently become a deterministic optimization instruction.

## 10. Owner boundaries

### Chapter 08 — shared parent grammar

Owns generic object/representation/audience/edge/interaction/mediation/observation/history and feedback-dynamics reasoning.

### Search & Discovery specialist

Owns only:

```text
discovery need / expression semantics
scoped discovery availability
retrieval / selection semantics
human-selection vs system-commitment distinction
groundability boundary
discovery-specific observation semantics
```

### Chapter 01 / 02

Own customer, segment, and demand inference. Search telemetry does not independently prove customer prevalence or market size.

### Chapter 04

Own marketing message, claim, proof, and allowed wording. Discovery grounding does not reopen marketing claim ownership.

### Chapter 05

Own causal diagnosis, attribution vs incrementality, experiments, and treatment effects.

### Chapter 09

Own product/listing/catalog/variant/offer/shopper identity and commerce-specific discovery. Generic discovery must not absorb commerce identity or commercial-state semantics.

### Chapter 11

Own landing-page information/action architecture once page-entry state is established. Generic discovery owns the pre-entry availability/selection/representation problem, not downstream page structure.

## 11. Explicit non-goals

Do not create:

```text
SEO ontology
GEO ontology
AEO ontology
LLMO ontology

SEARCH_OBJECT
QUERY_OBJECT
INDEX_OBJECT

WORLD_MODEL primitive
USER_MODEL primitive

global DISCOVERABLE boolean
global RELEVANCE score

new universal funnel
new journey / CRM / campaign subsystem
new causal framework
```

Current crawler names, robots directives, schema behavior, ranking/recommendation rules, eligibility requirements, Search Console definitions, and provider-specific AI-search controls are authoritative JIT inputs rather than timeless primitives.

## 12. Implementation implication

A bounded namespace such as `discovery.*` is justified. Exact route count is an implementation detail, but the logical surface should remain close to the frozen five-question model and should preserve the fast path.

Mentioning `SEO`, `Google`, `search`, `ranking`, `AI`, or `ChatGPT` must not automatically activate deep discovery knowledge. A narrow supplied transformation should remain narrow.

## 13. Final freeze statement

```text
WORLD FIELD DISCOVERY                PASS
DEEP DIVE                            PASS
ADVERSARIAL SYNTHESIS                PASS
CURRENT-SYSTEM GAP                   CONFIRMED
FINAL COUNTEREXAMPLE ATTACK          PASS

BOUNDED SPECIALIST CAPABILITY        CONFIRMED
SHARED GRAMMAR REOPEN                NO
NEW SHARED PRIMITIVE                 NO
NEW CONTROLLER JOB                   NO
SEO / GEO / AEO / LLMO ONTOLOGY      REJECTED

PRIMARY UNIT
→ DISCOVERY DECISION

FROZEN MODEL
→ NEED / CONTEXT
→ AVAILABILITY
→ RETRIEVAL / SELECTION
→ REPRESENTATION / COMMITMENT
→ OBSERVATION
```

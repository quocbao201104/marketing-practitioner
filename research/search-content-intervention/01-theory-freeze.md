# Search-Facing Content Intervention — Theory Freeze

Status: **FROZEN FOR BOUNDED IMPLEMENTATION**  
Freeze date: 2026-09-10  
Repository base: `main@a12bce34666ea7f39c3da46c4e869b2e91cd700e`

## 1. Frozen research question

> When may scoped search/discovery evidence legitimately authorize a change to an already-existing information/page representation or its relationships, what is the smallest justified intervention, and which upstream decisions must remain invariant?

The target is not on-page SEO as a professional category. The target is the decision boundary between discovery diagnosis and downstream artifact change.

## 2. Freeze verdict

```text
CURRENT COMPOSITION GAP            CONFIRMED
BOUNDED SPECIALIST REASONING       JUSTIFIED
HOST                               CHAPTER 13 §7
SHARED GRAMMAR REOPEN              NO
NEW SHARED PRIMITIVE               NO
NEW CONTROLLER JOB                 NO
NEW CHAPTER                        NO
NEW ROUTE INITIALLY                NO
SEO / GEO / AEO / LLMO ONTOLOGY    REJECTED
```

The gap is local reasoning, not representational capacity.

## 3. Frozen primary unit

The primary unit remains:

```text
DISCOVERY DECISION
```

Do not promote `KEYWORD`, `SERP`, `SEO PAGE`, `CANNIBALIZATION`, or `AI CITATION` into universal primary units.

## 4. Frozen intervention model

```text
SEARCH / DISCOVERY EVIDENCE
            ↓
G1 — EVIDENCE SUFFICIENCY
            ↓
G2 — PROBLEM LOCALIZATION
            ↓
G3 — RESOLVED-STATE PRESERVATION
            ↓
G4 — MATERIAL MISMATCH TEST
            ↓
G5 — MINIMUM JUSTIFIED DISPOSITION
```

### G1 — Evidence sufficiency

Ask what the current evidence actually establishes. Do not collapse an unobserved mechanism state into a negative fact or into a content defect.

When the evidence is insufficient to authorize a proposed intervention, the valid output is:

```text
NOT_ASSESSABLE
```

### G2 — Problem localization

Distinguish when material:

```text
availability / identity
retrieval / selection
system representation
publisher representation
page-role relationship
page content
technical implementation
measurement
upstream strategy
unknown
```

The same downstream symptom need not imply the same repair surface.

### G3 — Resolved-state preservation

Search evidence may inform expression. It must not silently reopen sufficiently resolved:

```text
customer / segment state
positioning / category / value
page job
message
claim / proof
commercial truth
```

### G4 — Material mismatch test

A publisher-controlled content/representation intervention is justified only when current evidence supports a material mismatch between the resolved state and the current artifact or relationship in the relevant discovery context.

Possible mismatch classes include:

```text
page role ↔ publisher title / main heading
page meaning ↔ surfaced representation
resolved meaning ↔ recognizable expression
page A role ↔ page B role
anchor expectation ↔ target-page job
current proposition ↔ current supported page content
```

### G5 — Minimum justified disposition

Use only the smallest disposition needed:

```text
KEEP
REPAIR REPRESENTATION
MODIFY BOUNDED CONTENT
DIFFERENTIATE
CONSOLIDATE
ROUTE TO OTHER OWNER
NOT_ASSESSABLE
```

Do not create a generic `OPTIMIZE` output.

## 5. Frozen search-language boundary

Keep:

```text
QUERY
≠ UNIQUE INTENT

SEARCH LANGUAGE
≠ MARKETING CLAIM

QUERY TERM
≠ REQUIRED PAGE TERM

SERP COMPOSITION
≠ USER REQUIREMENT

TOP-RANKING PAGE FEATURE
≠ CAUSAL RANKING FACTOR

TOPIC RELEVANCE
≠ REQUIRED PAGE COVERAGE

SEARCH RECOGNIZABILITY
DOES NOT OVERRIDE
SEMANTIC FIDELITY
```

A search phrase can be evidence that a vocabulary item is recognizable. It cannot independently prove a category claim, superiority claim, customer truth, market priority, or purchase intent.

## 6. Frozen representation boundary

Keep:

```text
PUBLISHER REPRESENTATION
≠ SYSTEM-HELD REPRESENTATION
≠ SURFACED REPRESENTATION

<title>
≠ SURFACED TITLE LINK

META DESCRIPTION
≠ GUARANTEED SURFACED SNIPPET
```

Publisher-controlled fields can influence a system-generated representation without controlling it.

## 7. Frozen page-relationship model

Do not use `keyword cannibalization` as a primitive or default diagnosis.

Separate:

```text
URL IDENTITY OVERLAP
CONTENT SIMILARITY
PAGE-JOB OVERLAP
QUERY OVERLAP
OBSERVED PERFORMANCE INTERFERENCE
```

Keep:

```text
SAME QUERY
≠ SAME PAGE JOB

SAME TOPIC
≠ DUPLICATE INFORMATION OBJECT

MULTIPLE SURFACED PAGES
≠ HARMFUL COMPETITION

CONTENT SIMILARITY
≠ AUTOMATIC CONSOLIDATION
```

Internal linking uses the existing relationship grammar:

```text
SOURCE OBJECT
      ↓
TYPED RELATIONSHIP
      ↓
ANCHOR / CONTEXT REPRESENTATION
      ↓
TARGET OBJECT
```

A link should encode a useful reader traversal and an accurate expectation about the destination rather than a generic authority-flow formula.

## 8. Frozen consolidation / technical boundary

A marketing/content decision can conclude that two communication objects no longer justify separate page jobs.

Keep:

```text
SEMANTIC CONSOLIDATION
≠ CANONICALIZATION
≠ REDIRECT / NOINDEX IMPLEMENTATION
```

Technical crawling/indexing configuration, redirects, canonical declarations, hreflang, HTTP/server behavior, and CMS execution remain authoritative technical dependencies.

## 9. Frozen AI-search boundary

Keep:

```text
AI / GENERATIVE SEARCH
≠ NEW CONTENT ONTOLOGY

AI CITATION ABSENCE
≠ CONTENT DEFECT

QUERY FAN-OUT
≠ REQUIREMENT TO CREATE QUERY-VARIANT PAGES
```

Existing discovery availability/retrieval/selection/grounding/observation semantics remain sufficient. No GEO/AEO/LLMO namespace is justified.

## 10. Owner boundaries

```text
customer / segment / market-demand inference
→ Chapter 01 / 02

positioning / category / value / differentiation
→ Chapter 03

marketing message / claim / proof
→ Chapter 04

causality / incrementality / experiment
→ Chapter 05

platform-native content participation
→ Chapter 08 / content.*

product / variant / listing / commerce discovery
→ Chapter 09 / commerce.*

landing-page information/action architecture after entry
→ Chapter 11 / landing-page.*

generic non-commerce discovery semantics
→ Chapter 13 / discovery.*
```

The intervention layer may authorize a downstream repair without taking ownership of the underlying specialist decision.

## 11. Routing freeze

Initial implementation remains under:

```text
discovery.diagnosis
→ Chapter 13 §7
```

Do not add `discovery.intervention` merely because a subsection exists.

A new route requires a demonstrated recurring route/retrieval failure caused by current granularity. A semantic reasoning failure after §7 was successfully loaded is not evidence for another route.

## 12. Controller freeze

Do not modify `SKILL.md` merely because tasks mention `SEO`, `Google`, `keyword`, `title`, `meta description`, `ranking`, `AI`, or `ChatGPT`.

A narrow supplied transformation remains on the fast path.

A controller correction requires a concrete activation failure in which intervention knowledge could materially change the decision but the current controller cannot reach the discovery path.

## 13. Final freeze statement

```text
THEORY GAP                         CONFIRMED
COUNTERFACTUAL DISCRIMINATION      PASS
EXISTING PRIMITIVES                SUFFICIENT
CHAPTER 13 HOST                    CONFIRMED
NEW ROUTE                          NOT YET JUSTIFIED
NEW CONTROLLER JOB                 REJECTED
NEW CHAPTER                        REJECTED
SEO/GEO/AEO/LLMO ONTOLOGY          REJECTED

FROZEN MODEL
EVIDENCE SUFFICIENCY
→ PROBLEM LOCALIZATION
→ RESOLVED-STATE PRESERVATION
→ MATERIAL MISMATCH
→ MINIMUM JUSTIFIED DISPOSITION
```
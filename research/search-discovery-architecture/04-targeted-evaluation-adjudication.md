# Search & Discovery Architecture — Targeted Evaluation Adjudication

Status: **TARGETED EVALUATION PASS — PROCEED TO INDEPENDENT ADVERSARIAL REVIEW**  
Branch: `candidate/search-discovery-architecture`  
Date: 2026-08-25

## 1. Material reviewed

This adjudication reviews the candidate evidence available before independent review:

- frozen theory: `research/search-discovery-architecture/01-theory-freeze.md`;
- implementation self-review: `research/search-discovery-architecture/02-implementation-self-review.md`;
- mechanical verification: `research/search-discovery-architecture/03-mechanical-verification.md`;
- targeted contract: `evals/search-discovery-architecture-adversarial-cases.md`;
- targeted self-runtime walkthrough: `evals/search-discovery-architecture-runtime-smoke.md`;
- candidate Chapter 13, evidence ledger, controller and routing bindings.

This is still candidate-side adjudication. It is not an independent runtime review.

## 2. Mechanical gate interpretation

The mechanical gate is adequate to proceed but carries an explicit environment limitation.

Verified by direct local execution:

```text
28 helper/source/path assertions
→ 28 PASS / 0 FAIL
```

Verified against the actual candidate branch through GitHub connector reads:

```text
8 discovery.* route selectors
→ all present and selector-consistent

SD09 evidence binding
→ present at the intended evidence heading
```

Not claimed:

```text
full checked-out test-knowledge-routing.py execution
→ NOT EXECUTED in this environment
```

This limitation prevents using the mechanical gate as evidence that every pre-existing route was re-executed end-to-end. It does not create a known discovery-specific binding defect.

## 3. Targeted runtime result

The 20-case walkthrough reports:

```text
PASS       20
PARTIAL     0
FAIL        0
```

The result is useful only if it demonstrates the intended failure boundaries rather than generic agreement with expected prose. The adjudication therefore checks the behavioral families below.

## 4. Fast-path activation

### D01

A narrow approved meta-description transformation remains on the fast path.

The candidate does not treat `meta description`, `SEO`, `Google`, `search`, `AI`, `ranking`, or `citation` as noun-based mandatory deep-route triggers.

**Adjudication:** PASS.

Why it matters: without this control, Chapter 13 would increase runtime complexity for ordinary transformations and violate the controller's dependency-first design.

## 5. Availability-state discipline

### D02, D03, D06, D07

The runtime keeps consequentially different states separate:

```text
published
≠ indexed

Google indexed
≠ available to every other provider

publisher canonical preference
≠ system-selected representative

age
≠ staleness
```

It also keeps provider-specific current implementation facts as JIT authoritative dependencies rather than timeless rules.

**Adjudication:** PASS.

No global `DISCOVERABLE` boolean is required or introduced.

## 6. Need / query discipline

### D04, D05, D19

The runtime preserves:

```text
query
≠ unique intent
≠ retrieval formulation
```

and supports queryless discovery without inventing a keyword requirement.

D04 correctly hands page architecture to Chapter 11 after entry-state uncertainty is bounded. D05 does not create pages for imagined internal fan-out queries. D19 keeps named-surface eligibility provider-specific.

**Adjudication:** PASS.

No new query object or intent primitive is justified.

## 7. Retrieval / commitment discipline

### D08, D09

The runtime distinguishes:

```text
web ranking
≠ AI-answer availability
≠ retrieval
≠ selection
≠ grounding fitness
≠ citation observation
```

and:

```text
retrieved
≠ evidentiary fit
≠ safe to commit
```

D08 is especially important because it blocks the common but unsupported tactic jump:

```text
rare AI citation
→ rewrite copy for AI
```

The runtime instead diagnoses the earliest unresolved boundary and reaches Chapter 04/content rewriting only if evidence localizes a representation/message defect there.

**Adjudication:** PASS.

The human-selection vs system-commitment distinction survives implementation and remains specialist knowledge rather than a new shared primitive.

## 8. Observation and causal discipline

### D10–D15, D20

The runtime preserves the critical observation boundaries:

```text
citation
≠ authority
≠ causal influence

impression
≠ verified attention

position
≠ universal independent rank

no click
≠ failure

search interest
≠ market demand

missing telemetry
≠ nonexistent mechanism
```

It also hands causal questions to Chapter 05 and customer/market-demand inference to Chapters 01/02.

**Adjudication:** PASS.

No discovery-local causal framework is introduced.

## 9. Owner-control cases

### D16 — Commerce

Product/variant/catalog identity remains under Chapter 09 / commerce/Amazon knowledge.

**PASS.**

### D17 — Landing page

Discovery context is passed as entry-state input; proof/pricing placement remains Chapter 11 work, with Chapter 04/10 only if their upstream decisions are unresolved.

**PASS.**

### D18 — Platform content

TikTok opening-frame/caption/comment allocation remains Chapter 08 / TikTok content work. Search-oriented subject matter alone does not transfer ownership to Chapter 13.

**PASS.**

These controls are material evidence that the specialist is bounded rather than becoming a generic owner for everything containing the word `search`.

## 10. Repeated-failure / architecture-reopen check

No repeated failure family was observed in the targeted walkthrough.

More importantly, no case constructed the required architecture-reopening witness:

> two materially different states require different correct actions, but the existing shared object/representation/audience/edge/mediation/observation grammar cannot distinguish them without material distortion.

The candidate continues to represent discovery-specific cases through existing shared roles plus specialist decision rules.

Therefore:

```text
SHARED GRAMMAR REOPEN
→ NOT JUSTIFIED

NEW SHARED PRIMITIVE
→ NOT JUSTIFIED

NEW CONTROLLER JOB
→ NOT JUSTIFIED

SEO / GEO / AEO / LLMO ONTOLOGY
→ NOT JUSTIFIED
```

## 11. Local-correction check

No local correction is required by the 20-case targeted walkthrough.

One implementation choice remains intentionally conservative: Chapter 13 contains a diagnosis/handoff section, but the routing namespace does not add a separate `discovery.diagnosis` route. The controller can diagnose through the earliest open `availability`, `selection`, `commitment`, or `observation` route. The targeted cases do not show a decision-relevant failure caused by the absence of a dedicated diagnosis route.

Therefore no route is added merely because a heading exists.

## 12. Evidence strength and limitation

The targeted result should not be over-read.

It establishes that the candidate can be walked through the frozen pressure cases without an observed owner-boundary or distinction failure.

It does not establish:

- provider-specific ranking/citation performance;
- improved real-world SEO outcomes;
- correctness across all discovery products;
- full mechanical regression execution of every pre-existing route;
- independence from candidate-author expectations;
- merge/release readiness without an external adversarial pass.

## 13. Verdict

> **TARGETED EVALUATION PASS — KEEP BOUNDED SPECIALIST ARCHITECTURE; PROCEED TO INDEPENDENT ADVERSARIAL REVIEW.**

Frozen architectural direction remains:

```text
PRIMARY UNIT
→ DISCOVERY DECISION

SPECIALIST DECISION FAMILIES
→ NEED / CONTEXT
→ AVAILABILITY
→ RETRIEVAL / SELECTION
→ REPRESENTATION / COMMITMENT
→ OBSERVATION

SHARED GRAMMAR REOPEN
→ NO
```

The next step is to freeze the implementation/evaluation target commit and give an independent reviewer a contract that forbids later candidate changes from being used as implementation evidence.
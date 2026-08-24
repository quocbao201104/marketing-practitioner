# Search & Discovery Architecture — Implementation Self-Review

Status: **IMPLEMENTATION CANDIDATE READY FOR TARGETED RUNTIME EVALUATION**  
Branch: `candidate/search-discovery-architecture`  
Base: `main@8e77150e589ce95d886ac637d241937d260b1610`

This review checks whether the first implementation preserves the frozen theory and existing owner boundaries. It is not an independent review and it is not evidence that a model/runtime will route correctly under adversarial prompts.

## 1. Candidate surface

The implementation currently changes/adds:

- `research/search-discovery-architecture/01-theory-freeze.md`
- `research/search-discovery-architecture/02-implementation-self-review.md`
- `skills/marketing-practitioner/references/search-discovery-evidence.md`
- `skills/marketing-practitioner/handbook/13-search-and-discovery-architecture.md`
- `skills/marketing-practitioner/routing-index.json`
- `skills/marketing-practitioner/SKILL.md`
- `skills/marketing-practitioner/handbook/README.md`
- `skills/marketing-practitioner/scripts/test-knowledge-routing.py`
- `evals/search-discovery-architecture-adversarial-cases.md`

No shared Chapter 08 primitive was added. No new controller job was added. No release/version bump has been made.

## 2. Theory-to-implementation mapping

| Frozen decision family | Implementation route | Status |
| --- | --- | --- |
| scope / primary unit | `discovery.core` | PASS |
| need / expression / query distinction | `discovery.need` | PASS |
| scoped availability / identity / freshness | `discovery.availability` | PASS |
| retrieval / relevance / selection | `discovery.selection` | PASS |
| human-selection vs system-commitment / grounding | `discovery.commitment` | PASS |
| discovery observation semantics | `discovery.observation` | PASS |
| consequential retained record | `discovery.decision-record` | PASS |
| anti-folklore boundary | `discovery.invariants` | PASS |

The chapter also contains a diagnosis/handoff section. It is intentionally not promoted to a dedicated route yet. The controller can diagnose the earliest unresolved discovery boundary and load the relevant local route. Add `discovery.diagnosis` only if targeted evaluation demonstrates a recurring route failure that the current route surface cannot handle cleanly.

## 3. Shared-grammar containment

### PASS — no new durable primitive

The chapter reuses:

```text
ACTOR / SOURCE
OBJECT
REPRESENTATION
AUDIENCE STATE
TYPED EDGE
INTERACTION ACT
PLATFORM / MEDIATION STATE
OBSERVATION RECORD

+ provenance
+ scope / relativity
+ history / state transition
```

It explicitly rejects promotion of:

```text
SEARCH_OBJECT
QUERY_OBJECT
INDEX_OBJECT
WORLD_MODEL
USER_MODEL
global DISCOVERABLE
global RELEVANCE score
```

### PASS — no new controller job

The existing `WRITE`, `DECIDE`, `DIAGNOSE`, `RESEARCH / UNDERSTAND`, `ADAPT`, `TEST`, and `LEARN` jobs remain sufficient.

## 4. Fast-path containment

### PASS by static inspection

The controller explicitly says not to activate the discovery path merely because the task mentions:

```text
SEO
Google
search
ranking
AI
ChatGPT
citation
meta tag
```

A supplied bounded transformation remains on the fast path when discovery mechanics cannot change the answer.

Targeted case D01 exists specifically to attack this behavior at runtime.

## 5. Chapter 08 boundary

### PASS by static inspection

The Platform content path was narrowed from a generic `social, community, feed, search...` trigger to platform-native **content** participation.

Search-oriented content remains Chapter 08 when the open decision is:

- content participation;
- multimodal/message allocation;
- audience/environment fit;
- platform-native representation.

Generic non-commerce discovery moves to Chapter 13 only when the open decision is availability, retrieval/selection, grounding/commitment, citation, or discovery telemetry semantics.

This prevents Chapter 13 from absorbing TikTok search-oriented content or feed/recommendation content strategy merely because search/discovery language appears.

## 6. Chapter 09 commerce boundary

### PASS by static inspection

The controller explicitly retains Chapter 09 ownership for:

```text
product
variant
listing
catalog
offer
commerce discovery
```

The existing `commerce.*` routes and platform commerce namespaces were not removed or replaced.

Targeted case D16 protects this boundary.

## 7. Chapter 04 proof/claim boundary

### PASS by static inspection

`discovery.commitment` owns whether retrieved information is fit to support a discovery system's answer commitment.

Chapter 04 continues to own whether the marketer may communicate a claim, with what proof and qualification.

Targeted case D10 forces a citation-to-authority claim handoff into Chapter 04.

## 8. Chapter 05 causal boundary

### PASS by static inspection

The discovery path owns event/telemetry semantics but not incrementality or causal effect.

The controller and chapter preserve:

```text
ATTRIBUTED OUTCOME
≠ CAUSED OUTCOME
```

and explicitly hand causal questions to Chapter 05.

Targeted cases D11 and D14 protect this boundary.

## 9. Chapter 11 landing-page boundary

### PASS by static inspection

Discovery owns pre-entry availability/selection/representation context. Chapter 11 still owns page information/action architecture after entry state is sufficiently resolved.

Targeted cases D04 and D17 protect this boundary.

## 10. JIT authoritative dependency boundary

### PASS by static inspection

Current crawler controls, indexing directives, structured-data behavior, provider eligibility rules, ranking/recommendation disclosures, AI-search controls, and telemetry definitions remain time-sensitive authoritative dependencies.

The chapter does not freeze Google/OpenAI/Perplexity/Bing implementation details as universal discovery laws.

## 11. Routing manifest

The `discovery` namespace currently exposes eight logical routes:

```text
discovery.core
discovery.need
discovery.availability
discovery.selection
discovery.commitment
discovery.observation
discovery.decision-record
discovery.invariants
```

Selectors point to exact Chapter 13 headings.

The existing routing smoke test has been extended to cover all eight route headings plus evidence lookup for `SD09`.

### Mechanical execution status

**NOT EXECUTED IN THIS REVIEW.**

The test now declares `49 routing-mechanics smoke checks`, but this document does not claim those checks passed because the current review environment has not executed the checked-out branch. No GitHub Actions run was started.

## 12. Evidence ledger

The new ledger uses `SD01–SD14` and keeps provider-specific facts separate from research-level conceptual evidence.

The ledger explicitly records what each source **does not** establish to reduce tactic/causal overreach.

`SD09` was selected as the deterministic source-lookup smoke target because it supports the human-selection vs system-commitment distinction.

## 13. Adversarial suite coverage

The 20-case targeted suite covers:

```text
FAST PATH
AVAILABILITY / INDEX COLLAPSE
NEED / QUERY COLLAPSE
SELECTION / COMMITMENT COLLAPSE
OBSERVATION OVERCLAIM
COMMERCE OWNER CONTROL
LANDING-PAGE OWNER CONTROL
CONTENT OWNER CONTROL
CAUSAL OWNER CONTROL
DEMAND-INFERENCE OWNER CONTROL
```

The suite is designed to punish generic SEO fluency if it comes at the cost of routing or evidence discipline.

## 14. Self-review verdict

> **IMPLEMENTATION SELF-REVIEW PASS — PROCEED TO TARGETED RUNTIME EVALUATION.**

This means only:

- the candidate is locally consistent with the frozen theory by static inspection;
- the bounded owner surface is coherent enough to evaluate;
- no shared architecture change is currently justified.

It does **not** mean:

- the runtime passes the 20 adversarial cases;
- the 49 mechanical checks have been executed;
- an independent reviewer has approved the implementation;
- the candidate is ready to merge or release.

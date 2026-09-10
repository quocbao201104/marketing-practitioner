# Search-Facing Content Intervention — Research Brief

Status: **bounded implementation research**  
Base: `main@a12bce34666ea7f39c3da46c4e869b2e91cd700e`  
Date: 2026-09-10

## 1. Research question

Does Marketing Practitioner lack a decision layer between search/discovery evidence and page/content execution, or can Chapter 13 Search & Discovery + Chapter 04 Messaging/Proof/Copy + Chapter 11 Landing-Page Architecture already compose this work losslessly?

The target is not generic SEO execution. The bounded question is:

> When may scoped search/discovery evidence legitimately authorize a change to an already-existing information/page representation or its relationships, what is the smallest justified intervention, and which upstream decisions must remain invariant?

## 2. Why this was investigated

Professional content work often asks a practitioner to interpret search evidence and then decide whether to change a title, heading, body coverage, meta-description candidate, internal relationship, or neighboring page. Existing ownership was already intentionally separated:

- Chapter 13 diagnoses discovery need, availability, retrieval/selection, representation/commitment, and observation semantics;
- Chapter 04 owns message, claim, proof, and allowed wording;
- Chapter 11 owns page information/action architecture after entry state is resolved;
- Chapter 05 owns causal inference and experimentation.

The research therefore tested whether a missing decision bridge remained after those owners were composed.

## 3. Gap finding

The composition is not fully lossless.

Chapter 13 can localize a discovery problem and decide whether another owner may need to act, but the pre-change architecture did not explicitly answer:

```text
IF ANOTHER OWNER MAY NEED TO ACT,
WHAT EXACTLY IS AUTHORIZED TO CHANGE?
```

This becomes material when the same observed symptom can justify opposite actions depending on one changed state. Examples include:

- the same CTR decline with an inaccurate versus already-faithful title representation;
- the same query overlap with distinct versus redundant page jobs;
- the same AI-citation absence with localized grounding/content evidence versus unknown retrieval state;
- the same apparent duplicate/canonical symptom with semantic redundancy versus a technical canonicalization problem.

The missing capability is therefore **intervention authorization**, not a new SEO ontology.

## 4. Frozen architecture result

```text
HOST                           Chapter 13 §7
PRIMARY UNIT                   DISCOVERY DECISION
NEW SHARED PRIMITIVE           NO
NEW CONTROLLER JOB             NO
NEW CHAPTER                    NO
NEW ROUTE INITIALLY            NO
SEO / GEO / AEO / LLMO         NO NEW ONTOLOGY
```

Use the existing durable grammar:

```text
OBJECT
REPRESENTATION
AUDIENCE STATE
TYPED RELATIONSHIP / ACCESS / DELIVERY EDGE
PLATFORM / MEDIATION STATE
OBSERVATION RECORD

+ provenance
+ scope / relativity
+ history / state transition
```

## 5. Bounded intervention model

```text
SEARCH / DISCOVERY EVIDENCE
            ↓
EVIDENCE SUFFICIENCY
            ↓
PROBLEM LOCALIZATION
            ↓
RESOLVED-STATE PRESERVATION
            ↓
MATERIAL MISMATCH TEST
            ↓
MINIMUM JUSTIFIED DISPOSITION
```

Permitted dispositions:

```text
KEEP
REPAIR REPRESENTATION
MODIFY BOUNDED CONTENT
DIFFERENTIATE
CONSOLIDATE
ROUTE TO OTHER OWNER
NOT_ASSESSABLE
```

`NOT_ASSESSABLE` is necessary when the supplied evidence is insufficient to authorize the requested repair. It is not a claim that no defect exists.

## 6. Key boundaries

Search evidence may inform expression but must not silently reopen resolved strategy.

Keep when material:

```text
QUERY ≠ UNIQUE INTENT
SEARCH LANGUAGE ≠ MARKETING CLAIM
QUERY TERM ≠ REQUIRED PAGE TERM
SERP COMPOSITION ≠ CONTENT SPECIFICATION
SEARCH SYMPTOM ≠ CONTENT DEFECT
SAME QUERY ≠ SAME PAGE JOB
SEMANTIC CONSOLIDATION ≠ CANONICALIZATION
<title> ≠ SURFACED TITLE LINK
META DESCRIPTION ≠ GUARANTEED SURFACED SNIPPET
```

Technical crawling/indexing execution, redirects, canonical configuration, hreflang, HTTP/server behavior, and CMS implementation remain authoritative technical dependencies rather than a new Marketing Practitioner ownership domain.

## 7. Evidence scope

The implementation reuses existing Search & Discovery evidence where it already covers AI-search and canonicalization semantics. It adds only missing current provider evidence for:

```text
SD15 — Google title-link behavior
SD16 — Google snippet/meta-description behavior
SD17 — Google link/anchor guidance
```

These records are scoped additions. They do not imply a full re-review of SD01–SD14.

## 8. Evaluation strategy

Do not modify the existing D01–D20 Search & Discovery adversarial suite. It remains a regression baseline.

Add a separate counterfactual Search-Facing Content Intervention suite that changes one material state while keeping the observed symptom nearly fixed. The suite must distinguish at least:

```text
REPAIR vs KEEP
KEEP/DIFFERENTIATE vs CONSOLIDATE
expression candidate vs unsupported claim
bounded AI-content repair vs NOT_ASSESSABLE
semantic consolidation vs ROUTE TECHNICAL
```

Fast-path and landing-page-owner controls must remain intact.

## 9. Promotion rule

Do not add `discovery.intervention` merely because the new subsection exists.

Promote a new route only if evaluation demonstrates a recurring routing/retrieval failure caused by the granularity of `discovery.diagnosis`. Wrong reasoning after §7 is successfully read is not evidence for another route.

Likewise, modify `SKILL.md` only if a concrete activation failure shows that the current controller cannot enter the relevant discovery path. Reopen shared grammar only if a concrete case cannot be represented using the existing primitives.
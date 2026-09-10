# Search-Facing Content Intervention — Targeted Evaluation Contract

Status: **FROZEN TARGETED EVALUATION CONTRACT**  
Date: 2026-09-10  
Theory: `research/search-content-intervention/01-theory-freeze.md`

## 1. Evaluation question

Can the implemented Chapter 13 intervention gate distinguish when nearly identical search/discovery symptoms justify different content dispositions without reopening upstream ownership or inventing SEO/GEO folklore?

The evaluation is not a test of generic SEO fluency and does not reward tactic volume.

## 2. Regression baseline

Do not alter the semantics of:

```text
evals/search-discovery-architecture-adversarial-cases.md
```

D01–D20 remain the pre-existing Search & Discovery regression baseline.

In particular:

```text
D01
approved narrow meta-description transformation
→ fast path

D14
impressions up / clicks flat
→ no automatic title/content rewrite
```

The new suite is additive.

## 3. Required counterfactual families

The additive suite must contain at least these paired families:

```text
SCI01-A / SCI01-B
same CTR symptom
representation mismatch vs faithful representation
→ REPAIR vs KEEP

SCI02-A / SCI02-B
same query overlap
separate legitimate page jobs vs redundant page jobs
→ KEEP/DIFFERENTIATE vs CONSOLIDATE

SCI03-A / SCI03-B
same search phrase
faithful recognizable vocabulary vs unsupported category/superiority claim
→ MAY INFORM EXPRESSION vs DO NOT INSERT

SCI04-A / SCI04-B
same low AI-citation symptom
localized source/content defect vs unknown retrieval state
→ BOUNDED REPAIR vs NOT_ASSESSABLE/DIAGNOSE

SCI05-A / SCI05-B
same duplicate/canonical-looking symptom
semantic redundancy vs legitimate pages with technical configuration conflict
→ CONSOLIDATE CANDIDATE vs ROUTE TECHNICAL
```

Add fast-path and landing-page ownership controls.

## 4. Semantic oracle

Do not score prose similarity. For each case judge the decision semantics.

Capture when applicable:

```text
EVIDENCE STATUS
sufficient / insufficient / partly unresolved

LOCALIZATION
availability / selection / publisher representation /
page relationship / page content / technical / unknown / other owner

DISPOSITION
KEEP / REPAIR REPRESENTATION / MODIFY BOUNDED CONTENT /
DIFFERENTIATE / CONSOLIDATE / ROUTE / NOT_ASSESSABLE

REPAIR SURFACE
if any

PRESERVED STATE / OWNER
what must not be reopened

FORBIDDEN INFERENCE
what the answer must not claim

HANDOFF
when another owner remains open
```

## 5. Case outcome vocabulary

Use only:

```text
PASS
PARTIAL
FAIL
```

A PASS requires the material distinction to survive even if the wording differs from the reference answer.

A PARTIAL result means the main disposition is usable but a material owner boundary, uncertainty statement, or forbidden inference is weakened.

A FAIL includes choosing the wrong disposition, collapsing the counterfactual pair, inventing unsupported causality/intent/technical state, or taking ownership that belongs elsewhere.

## 6. Architecture-promotion rule

Do not infer a route or ontology failure from an incorrect answer alone.

A new `discovery.intervention` route is justified only if repeated evaluation shows:

```text
1. the task materially requires the intervention knowledge;
2. the existing controller activates discovery correctly;
3. the agent identifies the intervention problem;
4. `discovery.diagnosis` granularity prevents reliable retrieval/reach of the §7 intervention knowledge;
5. a more specific route would directly address that failure.
```

If §7 was successfully loaded and the answer is still wrong, diagnose knowledge use/evaluator/runtime behavior instead of adding a route.

A `SKILL.md` change requires a demonstrated activation failure. Shared-grammar reopening requires an irreducible representation failure.

## 7. Pass condition

The targeted implementation passes only when:

- each pair preserves its discriminating state;
- the fast-path control stays narrow;
- Chapter 11 retains downstream landing-page architecture ownership;
- Chapter 04 retains claim/proof ownership;
- technical implementation is not silently absorbed;
- missing evidence can produce `NOT_ASSESSABLE`;
- no new route/primitive/chapter is required without a concrete demonstrated failure.

A green mechanical validation is necessary but not sufficient for semantic pass.
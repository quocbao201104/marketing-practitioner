# Search-Facing Content Intervention — Targeted Evaluation Contract

Status: **FROZEN TARGETED EVALUATION CONTRACT — POST-REVIEW REPAIR**  
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

## 3. Counterfactual construction rule

Each paired family must hold constant the artifact identity, observed search/discovery symptom, requested action, and all material upstream state except the **smallest state needed to flip intervention authorization**.

For each pair record:

```text
SHARED SEALED STATE
facts held constant across A/B

ONLY CHANGED STATE
the single decision-relevant distinction intentionally varied
```

Do not encode the target conclusion in the scenario with labels such as `redundant`, `independently useful`, `content defect`, or `technical-only problem` when concrete facts can express the distinction instead.

A pair that changes several unrelated owner states, uses an `either/or` branch, or has no uniquely assessable disposition is invalid for this targeted suite.

## 4. Required counterfactual families

```text
SCI01-A / SCI01-B
same CTR symptom and page state
publisher title mismatch vs faithful publisher title
→ REPAIR REPRESENTATION vs KEEP

SCI02-A / SCI02-B
same two pages and same query-overlap symptom
one page adds decision-relevant page-job utility vs adds none
→ KEEP / bounded differentiation if needed vs CONSOLIDATE

SCI03-A / SCI03-B
same search phrase, same page/job/category, same requested H1 change
superiority claim authorized by the existing claim/proof state vs not authorized
→ REPAIR REPRESENTATION vs KEEP / ROUTE TO OTHER OWNER

SCI04-A / SCI04-B
same page, citation symptom, page content, and approved fact state
retrieval/support evidence localizes the page representation vs retrieval/support state remains unknown
→ MODIFY BOUNDED CONTENT vs NOT_ASSESSABLE / continue diagnosis

SCI05-A / SCI05-B
same regional URLs and unexpected-canonical symptom
regional pages have no independent decision utility vs material regional decision utility
→ CONSOLIDATE candidate vs ROUTE / continue technical diagnosis

SCI06-A / SCI06-B
same faithful title/H1/meta and same bad surfaced title link
no publisher-controlled mismatch localized vs inaccurate internal-anchor representation localized
→ KEEP / NOT_ASSESSABLE vs REPAIR REPRESENTATION
```

Add fast-path and landing-page ownership controls.

## 5. Semantic oracle

Do not score prose similarity. For each case judge the decision semantics.

Capture when applicable:

```text
EVIDENCE STATUS
sufficient / insufficient / partly unresolved

LOCALIZATION
availability / selection / system representation /
publisher representation / page relationship / page content /
technical / unknown / other owner

DISPOSITION
KEEP / REPAIR REPRESENTATION / MODIFY BOUNDED CONTENT /
DIFFERENTIATE / CONSOLIDATE / ROUTE TO OTHER OWNER / NOT_ASSESSABLE

REPAIR SURFACE
if any

PRESERVED STATE / OWNER
what must not be reopened

FORBIDDEN INFERENCE / ACTION
what the answer must not claim or do

HANDOFF
when another owner remains open
```

Only the frozen disposition values above may populate `DISPOSITION`. Phrases such as `DO NOT INSERT` belong under forbidden action/inference, not under disposition.

## 6. Case outcome vocabulary

Use only:

```text
PASS
PARTIAL
FAIL
```

A PASS requires the material distinction to survive even if the wording differs from the reference answer.

A PARTIAL result means the main disposition is usable but a material owner boundary, uncertainty statement, or forbidden inference is weakened.

A FAIL includes choosing the wrong disposition, collapsing the counterfactual pair, inventing unsupported causality/intent/technical state, or taking ownership that belongs elsewhere.

## 7. Architecture-promotion rule

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

## 8. Pass condition

The targeted implementation passes only when:

- each pair changes only the smallest material authorization state;
- the prompt does not simply name the expected diagnosis;
- each arm has a uniquely assessable frozen disposition or bounded set of permitted dispositions;
- the fast-path control stays narrow;
- Chapter 11 retains downstream landing-page architecture ownership;
- Chapter 04 retains claim/proof ownership;
- technical implementation is not silently absorbed;
- missing evidence can produce `NOT_ASSESSABLE`;
- publisher-controlled and system-surfaced representations remain distinct;
- no new route/primitive/chapter is required without a concrete demonstrated failure.

A green mechanical validation is necessary but not sufficient for semantic pass.

# Search-Facing Content Intervention — Adversarial Cases

Status: candidate targeted evaluation suite  
Theory: `research/search-content-intervention/01-theory-freeze.md`  
Contract: `research/search-content-intervention/02-targeted-evaluation-contract.md`

Purpose: test whether Chapter 13 can authorize the smallest justified search-facing content intervention without converting search symptoms into automatic writing instructions or taking ownership from existing specialists.

## Evaluation principles

A case fails when the implementation materially:

- treats a search metric or visibility symptom as a content defect without adequate localization;
- treats query language as claim authority or mandatory copy;
- treats two pages appearing for one query as automatic cannibalization;
- collapses semantic consolidation into canonical/redirect/noindex implementation;
- rewrites for AI/GEO merely because citation telemetry is weak;
- reopens resolved positioning, page job, claims, proof, or commercial truth without evidence;
- absorbs Chapter 11 page architecture, Chapter 04 claim/proof ownership, Chapter 05 causality, or technical implementation;
- refuses to use `NOT_ASSESSABLE` when material evidence is absent;
- deep-routes a supplied mechanical transformation merely because it contains an SEO noun.

---

## SCI01-A — CTR symptom with representation mismatch

**Shared pair state**

- page job is resolved: CRM for small architecture firms;
- positioning, allowed claims, proof, and page architecture are not open;
- Search Console CTR declined in a comparable observation window;
- no causal effect of title wording has been established.

**Input**

> The page is for our CRM specifically for small architecture firms. Positioning and claims are approved. CTR fell this month. The current `<title>` is `Home | Acme`, while the page itself clearly identifies the CRM. Should we change the title?

**Expected semantics**

```text
EVIDENCE STATUS
sufficient to identify a publisher-representation mismatch;
insufficient to claim that title wording caused CTR decline

LOCALIZATION
publisher representation

DISPOSITION
REPAIR REPRESENTATION

REPAIR SURFACE
<title> / aligned title signals

PRESERVE
page job / positioning / claims / proof

FORBIDDEN
“the title caused the CTR decline”
ranking or CTR guarantee
```

A good answer may recommend a descriptive title that faithfully identifies the already-resolved page job.

---

## SCI01-B — Same CTR symptom, faithful representation

**Shared pair state**

Same as SCI01-A except the current title is:

```text
CRM for Small Architecture Firms | Acme
```

and it accurately describes the page.

**Input**

> CTR fell in the same kind of comparable window, but the current `<title>` is already `CRM for Small Architecture Firms | Acme` and accurately reflects the page. Should we rewrite it again because CTR is down?

**Expected semantics**

```text
DISPOSITION
KEEP current representation
or continue bounded diagnosis if another discovery boundary remains open

FORBIDDEN
CTR decline → automatic title rewrite
```

The pair fails if SCI01-A and SCI01-B both receive the same automatic rewrite disposition solely because CTR declined.

---

## SCI02-A — Query overlap with legitimate separate jobs

**Shared pair state**

Two pages both appear for some searches around `marketing CRM`.

Page A:

```text
/marketing-crm
broad category/product orientation
```

Page B:

```text
/crm-for-agencies
agency-specific decision support
```

Both remain independently useful to their intended readers.

**Input**

> Both pages appear for some of the same queries. Is this keyword cannibalization, and should we merge them?

**Expected semantics**

```text
QUERY OVERLAP ≠ PAGE-JOB OVERLAP

DISPOSITION
KEEP distinct
and, only if evidence shows material confusion,
clarify/differentiate representation or relationship

FORBIDDEN
same query → cannibalization → merge
```

Internal-link or anchor recommendations must express a useful relationship rather than a link-count or authority-flow formula.

---

## SCI02-B — Query overlap with redundant jobs

**Shared pair state**

Two pages appear for overlapping searches, but now both pages serve:

```text
the same reader state
the same beginner job
the same core propositions
substantially the same decision utility
```

**Input**

> These two beginner guides now do essentially the same communication job and cover the same useful material. They also appear for the same searches. Should we keep both because they rank separately?

**Expected semantics**

```text
LOCALIZATION
page-role/content redundancy

DISPOSITION
CONSOLIDATE candidate

FORBIDDEN
query overlap alone as the reason for consolidation
```

Do not automatically choose 301, canonical, or noindex implementation.

---

## SCI03-A — Search vocabulary faithfully expresses resolved meaning

**Shared evidence**

Search evidence repeatedly contains the phrase:

```text
CRM for architects
```

The product is already legitimately positioned and evidenced as a CRM for architecture firms.

**Input**

> Users often search “CRM for architects.” Our approved page currently says “client relationship workspace for architecture firms.” Can the search phrase inform the title or heading wording without changing strategy?

**Expected semantics**

```text
SEARCH LANGUAGE
may inform recognizable expression

DISPOSITION
REPAIR REPRESENTATION or MODIFY BOUNDED WORDING
only if the wording remains semantically faithful

PRESERVE
resolved category/value/claims
```

No exact-match requirement or ranking guarantee is allowed.

---

## SCI03-B — Same phrase would invent category or superiority claim

**Shared evidence**

Search phrase:

```text
best CRM for architects
```

But either:

- the product is not actually a CRM under the resolved positioning; or
- no evidence supports a `best` superiority claim.

**Input**

> Search volume is strongest for “best CRM for architects.” Put that exact phrase in our H1 so we match what people search.

**Expected semantics**

```text
SEARCH LANGUAGE ≠ MARKETING CLAIM

DISPOSITION
DO NOT INSERT unsupported category/superiority language

HANDOFF
Chapter 03 only if category/positioning is genuinely unresolved
Chapter 04 if a superiority claim is being proposed

FORBIDDEN
search volume → truth/claim authority
```

---

## SCI04-A — Low AI citation with localized source-content defect

**Shared symptom**

A page receives little or no observed citation in an AI-answer surface.

Additional evidence establishes that:

- the relevant source is retrievable in the scoped system/context;
- the required proposition is material to the answer-support job;
- the current page either omits that proposition or expresses it so ambiguously that the source itself does not adequately support it;
- the proposition is already supported by authoritative product/evidence state.

**Input**

> We verified the page is retrievable for the relevant answer context. The page never clearly states the already-approved compatibility fact that the answer needs to support, although our authoritative product source does. Is a page-content repair justified?

**Expected semantics**

```text
LOCALIZATION
publisher content / groundability-support representation

DISPOSITION
MODIFY BOUNDED CONTENT

PRESERVE
approved fact / claim scope

FORBIDDEN
citation guarantee
“rewrite for GEO” as an independent ontology
```

---

## SCI04-B — Same low AI citation, retrieval unknown

**Shared symptom**

Low or absent citation telemetry.

But internal retrieval state and candidate-selection evidence are unavailable.

**Input**

> Our page is rarely cited in the AI answer dashboard. We cannot tell whether it was retrieved, selected, or evaluated for support. Should we rewrite the page for GEO?

**Expected semantics**

```text
EVIDENCE STATUS
insufficient

DISPOSITION
NOT_ASSESSABLE for content intervention
or continue discovery diagnosis

FORBIDDEN
citation absence → content defect
AI-specific rewrite prescription
```

---

## SCI05-A — Duplicate-looking symptom with semantic redundancy

**Shared symptom**

Google selects one URL as canonical while two pages look substantially similar.

Additional evidence shows the pages now serve the same reader, page job, propositions, and decision utility.

**Input**

> Google is clustering these two URLs, and our content review also shows they no longer serve meaningfully different reader jobs. Should Marketing Practitioner treat them as separate content objects?

**Expected semantics**

```text
DISPOSITION
CONSOLIDATE candidate

BASIS
semantic/page-job redundancy

FORBIDDEN
Google-selected canonical alone proves pages should merge
```

Technical redirect/canonical implementation remains a separate dependency.

---

## SCI05-B — Same canonical symptom with legitimate distinct pages

**Shared symptom**

Google selects an unexpected canonical.

But the two pages have legitimately different regional jobs and current factual/commercial differences. Evidence indicates conflicting canonical/localization/server signals may be involved.

**Input**

> Our US and UK pages legitimately differ in availability, currency, and applicable wording, but Google selected the unexpected canonical and our technical review found conflicting canonical/localization signals. Should we rewrite the marketing copy until the pages look more different?

**Expected semantics**

```text
LOCALIZATION
technical discovery implementation

DISPOSITION
ROUTE TO authoritative technical dependency

PRESERVE
legitimate page jobs and truthful regional content

FORBIDDEN
rewrite valid marketing content merely to force technical differentiation
```

---

## SCI-C01 — Fast-path regression canary

**Input**

> Shorten this approved meta description to 150 characters. Keep the meaning unchanged.

**Expected**

- direct bounded transformation;
- no deep Search & Discovery exposition;
- no ranking/CTR promise;
- preserve supplied meaning.

**Failure**

Activation of the new intervention machinery merely because `meta description` appears in the request.

---

## SCI-C02 — Landing-page owner canary

**Input**

> Search visitors arrive with a resolved ready-to-compare entry state. The product, price, claims, and proof are already fixed. Where should pricing and proof appear on the landing page?

**Expected**

- treat discovery/entry state as supplied context;
- route page information/proof/pricing allocation to Chapter 11 / `landing-page.*`;
- do not let search-content intervention design the page sequence.

---

## Control matrix

```text
REPAIR vs KEEP                         SCI01-A / SCI01-B
DISTINCT vs REDUNDANT PAGE JOBS        SCI02-A / SCI02-B
EXPRESSION vs CLAIM AUTHORITY          SCI03-A / SCI03-B
BOUNDED AI REPAIR vs NOT_ASSESSABLE    SCI04-A / SCI04-B
SEMANTIC vs TECHNICAL DUPLICATE ISSUE  SCI05-A / SCI05-B
FAST PATH                              SCI-C01
LANDING-PAGE OWNER                     SCI-C02
```

## Outcome vocabulary

Use only:

```text
PASS
PARTIAL
FAIL
```

Report the observed semantic disposition, preserved owner/state, forbidden inference, and handoff when applicable. Do not treat prose similarity as the evaluator.
# Search-Facing Content Intervention — Adversarial Cases

Status: candidate targeted evaluation suite — post-review repair  
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
- collapses publisher-controlled representation into system-surfaced representation;
- deep-routes a supplied mechanical transformation merely because it contains an SEO noun.

Each pair must hold the shared state fixed and vary only the listed **ONLY CHANGED STATE**.

---

## SCI01-A — CTR symptom with publisher-title mismatch

**Shared sealed state**

```text
page: /crm-for-architecture-firms
page job: help small architecture firms evaluate Acme CRM
positioning / allowed claims / proof: resolved
page architecture: resolved
Search Console CTR: declined in a comparable observation window
causal effect of title wording: not established
requested action: decide whether the publisher title should change
```

**Only changed state**

```text
current <title>: Home | Acme
```

The visible page body and H1 already identify the product as CRM for architecture firms.

**Input**

> CTR is down for `/crm-for-architecture-firms`. The page itself already says what it is, but its current `<title>` is `Home | Acme`. Should the title change?

**Expected semantics**

```text
EVIDENCE STATUS
sufficient to identify a publisher-representation mismatch;
insufficient to claim the mismatch caused CTR decline

LOCALIZATION
publisher representation

DISPOSITION
REPAIR REPRESENTATION

REPAIR SURFACE
<title>

PRESERVE
page job / positioning / claims / proof

FORBIDDEN
CTR decline → title causality
ranking / CTR guarantee
```

---

## SCI01-B — Same CTR symptom with faithful publisher title

**Shared sealed state**

Exactly the same as SCI01-A.

**Only changed state**

```text
current <title>: CRM for Small Architecture Firms | Acme
```

The title accurately identifies the already-resolved page job.

**Input**

> CTR is down for the same page in the same kind of window. Its current `<title>` is `CRM for Small Architecture Firms | Acme`. Should the title change because CTR fell?

**Expected semantics**

```text
DISPOSITION
KEEP
or continue bounded diagnosis if another discovery boundary remains open

FORBIDDEN
CTR decline → automatic title rewrite
```

The pair fails if both arms receive the same rewrite disposition solely because CTR declined.

---

## SCI02-A — Query overlap with one additional page-job requirement

**Shared sealed state**

```text
Page A: /marketing-crm
Page B: /crm-for-agencies
both target an agency owner comparing CRM options
both appear for some searches around "marketing CRM"
both explain lead capture, contact sync, pipeline stages, and reporting
requested action: decide whether the two communication objects should remain separate
```

**Only changed state**

Page B additionally must help the same reader decide whether the product can handle:

```text
separate client workspaces
per-client permissions
cross-client reporting
```

Those requirements are absent from Page A.

**Input**

> `/marketing-crm` and `/crm-for-agencies` both appear for some of the same searches. The agency page also covers separate client workspaces, per-client permissions, and cross-client reporting, while the broader page does not. Should we merge the pages because of the query overlap?

**Expected semantics**

```text
QUERY OVERLAP ≠ PAGE-JOB OVERLAP

DISPOSITION
KEEP
or DIFFERENTIATE only if their current representations materially blur the distinction

FORBIDDEN
same query → cannibalization → merge
```

Internal-link or anchor recommendations must encode a useful reader relationship rather than a link-count or authority-flow formula.

---

## SCI02-B — Same pages and query overlap without additional page-job requirement

**Shared sealed state**

Exactly the same as SCI02-A.

**Only changed state**

Page B does **not** need to resolve separate-client-workspace, per-client-permission, or cross-client-reporting questions. Its material decision content is the same lead capture, contact sync, pipeline, and reporting content already present on Page A.

**Input**

> The same two URLs appear for the same overlapping searches. This time the agency page adds no agency-specific decision requirement beyond the lead capture, contact sync, pipeline, and reporting material already covered on the broader page. Should the two communication objects remain separate?

**Expected semantics**

```text
LOCALIZATION
page-role / decision-utility overlap

DISPOSITION
CONSOLIDATE candidate

FORBIDDEN
query overlap alone as the reason for consolidation
automatic 301 / canonical / noindex implementation
```

The pair fails if the evaluator cannot attribute the disposition flip to the presence or absence of independently useful page-job content.

---

## SCI03-A — Same search phrase with authorized superiority claim

**Shared sealed state**

```text
search phrase observed: "best CRM for architects"
page: /crm-for-architecture-firms
page job: resolved
product category: resolved and supported as CRM for architecture firms
current H1: CRM for Architecture Firms
requested action: decide whether to change the H1 to "Best CRM for Architects"
```

**Only changed state**

The current Chapter 04 claim/proof state already authorizes the exact bounded superiority claim `Best CRM for Architects` for this scope, based on current comparative evidence.

**Input**

> Searchers often use “best CRM for architects.” Our current H1 is `CRM for Architecture Firms`. The approved claim ledger already permits `Best CRM for Architects` for this exact scope. May the H1 use that wording?

**Expected semantics**

```text
SEARCH LANGUAGE
may inform recognizable expression but is not the source of claim authority

DISPOSITION
REPAIR REPRESENTATION

PRESERVE
resolved category / claim scope / proof qualification

FORBIDDEN
search volume or query wording as proof of superiority
ranking guarantee
```

---

## SCI03-B — Same search phrase without authorized superiority claim

**Shared sealed state**

Exactly the same as SCI03-A.

**Only changed state**

The current Chapter 04 claim/proof state authorizes only the category-level statement `CRM for Architecture Firms`; it does not authorize a superiority claim such as `best`.

**Input**

> Searchers often use “best CRM for architects.” Our current H1 is `CRM for Architecture Firms`. The approved claim ledger supports the CRM-for-architecture-firms category but contains no authorized superiority claim. May the H1 become `Best CRM for Architects`?

**Expected semantics**

```text
SEARCH LANGUAGE ≠ MARKETING CLAIM

DISPOSITION
KEEP

HANDOFF
ROUTE TO OTHER OWNER / Chapter 04 only if the user wants to establish a new superiority claim

FORBIDDEN ACTION
insert unsupported “best” wording

FORBIDDEN INFERENCE
search volume / query language → claim authority
```

`DO NOT INSERT` is a forbidden action, not the disposition value.

---

## SCI04-A — Low AI citation with retrieval/support localization

**Shared sealed state**

```text
page: /desktop-sync
page job: general product overview; compatibility detail is not otherwise required for the human page job
approved product fact: desktop sync supports Windows
current page wording: "Desktop sync is available for supported environments."
AI-answer citation observation: low for questions asking whether Acme desktop sync works on Mac
requested action: decide whether this page should receive a bounded search-facing clarification
```

**Only changed state**

Provider-side evidence available to the practitioner establishes that, for the scoped answer context, this page was retrieved as support and the selected source representation contained the ambiguous `supported environments` wording while the answer required a platform-specific compatibility distinction.

**Input**

> The page says `Desktop sync is available for supported environments.` We already know from the authoritative product source that desktop sync is Windows-only. For the relevant AI-answer context, we can verify this page was retrieved as support and that the selected representation carried the ambiguous wording while the answer needed the platform distinction. Is a bounded page clarification justified?

**Expected semantics**

```text
EVIDENCE STATUS
sufficient for the scoped intervention decision

LOCALIZATION
publisher content / support representation

DISPOSITION
MODIFY BOUNDED CONTENT

PRESERVE
approved Windows-only fact / existing page job

FORBIDDEN
citation guarantee
new GEO ontology
claim that the wording caused all citation behavior
```

---

## SCI04-B — Same page and citation symptom with retrieval/support state unknown

**Shared sealed state**

Exactly the same as SCI04-A, including page content and authoritative Windows-only product fact.

**Only changed state**

No provider-side evidence reveals whether this page was retrieved, selected, or evaluated as support for the scoped AI-answer context.

**Input**

> The same page still says `Desktop sync is available for supported environments`, and the authoritative product source still says Windows-only. Citation is low for the same AI-answer questions, but we have no evidence showing whether this page was retrieved, selected, or evaluated as support. Does that citation symptom authorize a search-facing page rewrite?

**Expected semantics**

```text
EVIDENCE STATUS
insufficient to attribute the AI-search symptom to this page representation

DISPOSITION
NOT_ASSESSABLE
or continue discovery diagnosis

FORBIDDEN
citation absence → content defect
AI-specific rewrite prescription from telemetry alone
```

This case concerns authorization **from the AI-search symptom**. It does not forbid a separate non-search owner from deciding that the wording should be clarified for ordinary product-truth reasons.

---

## SCI05-A — Unexpected canonical with no independent regional decision utility

**Shared sealed state**

```text
URLs: /service-us and /service-uk
Google selects /service-us as canonical for /service-uk
both appear in the same service-search context
requested action: decide the semantic content disposition before choosing technical implementation
```

**Only changed state**

Current business/content state is identical across the two pages:

```text
same service availability
same price and currency presentation
same terms / applicable wording
same support conditions
same reader decision information
```

The region token in the URL/title is the only material difference.

**Input**

> Google selects `/service-us` as canonical for `/service-uk`. Our current source-of-truth review shows both pages now present the same availability, price/currency, terms, support conditions, and decision information; only the region label differs. What is the content disposition?

**Expected semantics**

```text
DISPOSITION
CONSOLIDATE candidate

BASIS
absence of independently useful regional communication state

FORBIDDEN
Google-selected canonical alone proves semantic consolidation
automatic redirect / canonical / noindex choice
```

---

## SCI05-B — Same unexpected canonical with independent regional decision utility

**Shared sealed state**

Exactly the same as SCI05-A.

**Only changed state**

The UK page must communicate current decision-relevant state that differs from the US page:

```text
GBP customer price instead of USD
UK-only availability date
UK statutory wording
UK support hours
```

**Input**

> Google still selects `/service-us` as canonical for `/service-uk`. This time the UK page has a different GBP customer price, UK-only availability date, statutory wording, and support hours. Should we consolidate or rewrite the marketing content until the canonical symptom disappears?

**Expected semantics**

```text
DISPOSITION
ROUTE TO OTHER OWNER / authoritative technical dependency
or continue bounded technical discovery diagnosis

PRESERVE
regional page distinction and truthful regional content

FORBIDDEN
rewrite or merge valid regional content merely because of the system-selected canonical
```

The pair changes the independent regional decision utility, not the observed canonical symptom.

---

## SCI06-A — Bad surfaced title with no localized publisher mismatch

**Shared sealed state**

```text
page: /crm-for-architecture-firms
resolved page job: CRM for architecture firms
<title>: CRM for Small Architecture Firms | Acme
H1: CRM for Architecture Firms
meta description: faithful to the same page job
system-surfaced title link observed: Home | Acme
CTR symptom: down in the scoped observation window
requested action: decide whether a publisher-controlled representation should change
```

**Only changed state**

All inspected internal anchors pointing to the page are also descriptive and faithful to the page job. No inaccurate publisher-controlled representation source has been localized.

**Input**

> Our `<title>`, H1, meta description, and inspected internal anchors all correctly identify the CRM-for-architecture-firms page, but Google is currently surfacing `Home | Acme` as the title link and CTR is down. Which publisher-controlled field should we rewrite?

**Expected semantics**

```text
PUBLISHER REPRESENTATION ≠ SYSTEM-SURFACED REPRESENTATION

DISPOSITION
KEEP
or NOT_ASSESSABLE for a publisher-side repair while diagnosis continues

FORBIDDEN
bad surfaced title → automatically rewrite an already-faithful publisher field
CTR causality claim
```

---

## SCI06-B — Same surfaced title with localized inaccurate internal-anchor representation

**Shared sealed state**

Exactly the same as SCI06-A.

**Only changed state**

Three prominent internal links to the page use the anchor text:

```text
Home
```

instead of describing the CRM-for-architecture-firms destination. All other inspected publisher representations remain faithful.

**Input**

> The same page still has a faithful `<title>`, H1, and meta description, and Google still surfaces `Home | Acme`. This time we also find three prominent internal links to the page whose anchor text is simply `Home`. Is any publisher-side repair justified?

**Expected semantics**

```text
LOCALIZATION
publisher-controlled relationship representation

DISPOSITION
REPAIR REPRESENTATION

REPAIR SURFACE
internal anchor / link context

FORBIDDEN
claim that the anchors caused the surfaced Google title
ranking / CTR guarantee
```

The repair is justified because the anchors themselves misrepresent the target relationship, not because their causal role in title-link generation has been proven.

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
DISTINCT vs REDUNDANT PAGE UTILITY     SCI02-A / SCI02-B
AUTHORIZED vs UNAUTHORIZED CLAIM       SCI03-A / SCI03-B
LOCALIZED AI REPAIR vs NOT_ASSESSABLE  SCI04-A / SCI04-B
SEMANTIC vs TECHNICAL CANONICAL ISSUE  SCI05-A / SCI05-B
SYSTEM vs PUBLISHER REPRESENTATION     SCI06-A / SCI06-B
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

For each case report the observed evidence status, localization, frozen disposition, preserved owner/state, forbidden inference/action, and handoff when applicable. Do not treat prose similarity as the evaluator.

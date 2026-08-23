# Etsy Query-Matching Source-Conflict Correction Check

Reviewed: 2026-08-23

Status: **targeted post-review correction check, not benchmark/eval score**.

## Trigger

Independent adversarial review of frozen head:

```text
1bcc0f653d0f14031e8209c77de51e518d66302a
```

found one material source-fidelity defect: the frozen Etsy module resolved current official evidence too aggressively by treating description as not proven for initial query matching.

No core-grammar, router, or new-primitive failure was found.

## Official-source conflict

Current public Etsy sources do not provide one consistent field-level description of query matching:

```text
LEGAL DISCLOSURE — 2025-10-16
first query-matching phase enumerates:
titles + attributes + categories + tags

SELLER HANDBOOK — Keywords 101 — 2025-08-26
explicitly says keywords across:
titles + descriptions + tags + categories + attributes
are essential to query matching,
and calls query matching the first phase

SELLER HANDBOOK — How Etsy Search Works
places a holistic listing under Query matching,
including title + tags + attributes + descriptions + first photo + reviews + more

ENGINEERING — 2026-01-16
its disclosed semantic-relevance model first applies after retrieval,
but this does not establish absence of description from every other initial matching mechanism
```

Correct evidence state:

```text
CURRENT OFFICIAL ETSY SOURCES
CONFLICT / USE DIFFERENT ABSTRACTION LEVELS
ABOUT QUERY-MATCHING FIELD PARTICIPATION

→ preserve source + date + abstraction level
→ exact current production mechanics / weights remain UNKNOWN
```

## Repair scope

Changed only source-fidelity / knowledge material:

```text
platforms/commerce/etsy.md
references/commerce/etsy-evidence.md
references/commerce-platform-evidence.md
handbook/09-commerce-environments-and-product-discovery.md
```

No change to:

```text
8 + 3 durable grammar
SKILL.md routing
commerce activation metadata
other marketplace modules
agentic-commerce model
version
```

## Targeted counterexample

**Prompt**

> My Etsy listing contains the phrase “hand-thrown moon jar” only in the description — not in the title, tags, attributes, or category. Can that phrase participate in Etsy's initial query matching, or is description only useful after retrieval/ranking?

**Required answer shape**

> Current official Etsy sources do not give one fully consistent implementation-level answer. Etsy's current `Keywords 101` explicitly says description keywords participate in query matching, which it calls the first phase of Search, and `How Etsy Search Works` also places descriptions and broader listing information under Query matching. However, Etsy's October 16, 2025 legal ranking disclosure gives a narrower first-phase enumeration of titles, attributes, categories, and tags. Separately, Etsy Engineering says its January 2026 semantic-relevance model first applies after retrieval; that describes that model, not proof that descriptions are absent from every earlier matching mechanism. So it would be wrong to say the description is “post-retrieval only.” The exact current production field-to-stage mechanics and weights remain publicly unresolved.

**Observed after correction**

- preserves the explicit Seller Handbook description/query-matching claim;
- preserves the narrower legal enumeration;
- does not misuse post-retrieval semantic-model evidence as proof of absence upstream;
- does not invent field weights or ranking effects;
- leaves exact implementation boundary UNKNOWN.

**Verdict: PASS**

## Regression checks

| Check | Result |
| --- | --- |
| Etsy unique/custom/made-to-order object reasoning unchanged | PASS |
| Query matching remains distinct from post-retrieval semantic relevance and ranking | PASS |
| Description is no longer categorically excluded from query matching | PASS |
| Seller Handbook wording is not converted into fixed implementation weights | PASS |
| Chapter 09 now handles conflicting official abstractions explicitly | PASS |
| No router change required | PASS |
| No new durable primitive required | PASS |
| Other platform modules unchanged | PASS |

## Gate recommendation

```text
ONE TARGETED CORRECTION
APPLIED

SOURCE-FIDELITY COUNTEREXAMPLE
PASS

CORE / ROUTER REOPEN
NO
```

**RETURN THE NEW PR #7 HEAD TO INDEPENDENT ADVERSARIAL REVIEW.**

Do not reopen broad commerce research unless a new concrete decision-relevant failure survives the corrected evidence discipline.

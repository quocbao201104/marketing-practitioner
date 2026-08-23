# Knowledge Routing v0.1 — Architecture Smoke

Branch: `candidate/knowledge-routing-index-v0.1`

Status: targeted architecture smoke, not a benchmark.

## Scope

The semantic routing layer covers the large independently routable decision-knowledge surfaces in the skill:

- Chapter 08 — content environments and distribution;
- Chapter 09 — commerce environments and product discovery;
- Facebook;
- Instagram;
- LinkedIn;
- TikTok;
- X;
- Google Shopping / Google commerce;
- Amazon;
- TikTok Shop;
- Shopee;
- Etsy;
- Lazada.

Small handbook chapters 00–07 are intentionally not section-indexed merely for uniformity. Their current file size/coherence does not justify another routing layer.

`frameworks/` is also intentionally file-level: the current files are approximately 3.2 KB and 6.1 KB.

Evidence files are handled differently. `references/bibliography.md`, `references/commerce-platform-evidence.md`, and platform evidence ledgers already expose stable intrinsic identifiers such as `[R23]`, `[C14]`, and `[A03]`. They are not decision modules and therefore are not duplicated into the semantic manifest. The loader resolves those identifiers directly with `--source`.

No handbook, platform, framework, or reference knowledge file is modified by this routing pass.

## Contract under test

```text
OPEN DECISION
→ KNOWLEDGE NAMESPACE
→ LOGICAL KNOWLEDGE ID
→ ROUTING MANIFEST
→ PHYSICAL FILE + SELECTOR
→ DETERMINISTIC EXTRACTION
→ SMALLEST DECISION-RELEVANT KNOWLEDGE CHUNK
```

For evidence traceability:

```text
CLAIM / CITATION NEED
→ INTRINSIC SOURCE ID
→ references/**/*.md
→ EXACT SOURCE HEADING
→ DETERMINISTIC EXTRACTION
```

Logical knowledge IDs are the stable semantic interface. File paths, headings, and marker selectors are implementation details and may change without changing the logical ID.

## Schema correction discovered during the smoke

The first flat schema repeated full paths plus several `use_when` phrases for every route. After only Chapter 08, Chapter 09, TikTok, and Shopee, the manifest had already reached 17,481 bytes.

That was a concrete architecture failure: scaling the flat schema across the full skill would turn the routing manifest into a second handbook and partially defeat context economy.

The candidate was therefore corrected before broad expansion.

Schema v2 groups sections by namespace/file:

```json
{
  "namespaces": {
    "shopee": {
      "path": "platforms/commerce/shopee.md",
      "sections": {
        "commercial-state": "## 9. Buyer-relative displayed price ...",
        "diagnosis": "## 14. Diagnosing weak or changing Shopee performance"
      }
    }
  }
}
```

Logical IDs are composed as:

```text
<namespace>.<section>
```

Examples:

```text
commerce.resolvability
facebook.groups
instagram.creator-commerce
linkedin.relationship-edges
tiktok.machine-mediation
x.interaction-provenance
google-commerce.agentic-checkout
amazon.shop-direct
tiktok-shop.relinking
shopee.conversational-discovery
etsy.search-stages
lazada.product-score-boundary
```

The full manifest covers 13 namespaces and 190 logical routes while remaining 16,897 bytes in the inspected branch snapshot.

## Runtime lookup modes

Semantic knowledge:

```bash
python skills/marketing-practitioner/scripts/get-knowledge.py --namespaces
python skills/marketing-practitioner/scripts/get-knowledge.py --list
python skills/marketing-practitioner/scripts/get-knowledge.py --list --namespace shopee
python skills/marketing-practitioner/scripts/get-knowledge.py commerce.resolvability
python skills/marketing-practitioner/scripts/get-knowledge.py shopee.commercial-state shopee.representation
```

Evidence records:

```bash
python skills/marketing-practitioner/scripts/get-knowledge.py --source R23
python skills/marketing-practitioner/scripts/get-knowledge.py --source C14 A03
```

Integrity:

```bash
python skills/marketing-practitioner/scripts/get-knowledge.py --validate
```

Namespace-specific listing is important: when the controller already knows the relevant domain/platform, it does not need to expose all 190 route IDs to the reasoning context.

## Mechanical smoke

The helper was exercised against isolated Markdown/reference fixtures using the same extraction logic as `get-knowledge.py` after the schema-v2 refactor.

| Check | Expected behavior | Result |
| --- | --- | --- |
| H1 | `##` heading route includes nested `###` / `####` content and stops before next `##` | PASS |
| H2 | `###` heading route includes nested `####` content and stops before next `###` / higher heading | PASS |
| M1 | marker route returns only content between one matching start/end pair | PASS |
| M2 | reversed start/end marker order fails closed | PASS |
| G1 | grouped namespace + section resolves to expected heading chunk | PASS |
| G2 | grouped namespace + marker resolves to expected marker chunk | PASS |
| G3 | namespace-specific route listing returns only that namespace | PASS |
| E1 | evidence source ID resolves case-insensitively to one exact source heading | PASS |
| E2 | unknown evidence source ID fails closed | PASS |
| E3 | duplicate evidence source ID across ledgers fails closed | PASS |
| F1 | unknown namespace fails closed | PASS |
| F2 | unknown section / duplicated heading fails closed rather than guessing | PASS |
| F3 | path traversal outside the skill root fails closed | PASS |
| F4 | duplicate JSON keys fail closed instead of silently overwriting a namespace/section | PASS |

Repeatable smoke command:

```bash
python skills/marketing-practitioner/scripts/test-knowledge-routing.py
```

Expected result:

```text
PASS    14 routing-mechanics smoke checks
```

## Manifest integrity command

The loader exposes repository-binding validation:

```bash
python skills/marketing-practitioner/scripts/get-knowledge.py --validate
```

This checks every indexed route against the checked-out skill tree and fails when a path or selector cannot be resolved exactly. JSON parsing additionally rejects duplicate keys so a repeated namespace/section cannot silently overwrite an earlier route.

Important evidence boundary: the current chat environment could not obtain a checked-out GitHub branch in its execution filesystem, so the full branch-local `--validate` command has **not** been executed here. Selectors were bound against current branch source through direct repository inspection. Earlier in the pass, that inspection caught several initially misremembered Chapter 09 section numbers before expansion.

Do not convert source inspection into a claim that repository-local validation executed when it did not.

## Selector strategy

Use existing stable Markdown headings first when the heading boundary already matches the desired knowledge chunk.

Use explicit markers only when a logical route needs a boundary that headings cannot express cleanly:

```text
<!-- route:start logical.id -->
...
<!-- route:end logical.id -->
```

Marker extraction requires exactly one correctly ordered pair.

This keeps instrumentation minimal and avoids rewriting large knowledge files merely to create routing metadata.

Evidence source lookup does not require manifest entries. It scans `references/**/*.md` for a unique heading beginning with the requested bracketed source ID and returns that heading section only.

## Current verdict

```text
LOGICAL-ID ABSTRACTION           PASS
GROUPED MANIFEST SCHEMA          PASS AFTER SIZE FAILURE CORRECTION
GLOBAL MANIFEST SIZE             PASS — 16,897 BYTES / 13 NAMESPACES / 190 ROUTES
HEADING EXTRACTION               PASS
NESTED HEADING BOUNDARIES        PASS
MARKER EXTRACTION                PASS
MARKER ORDER FAIL-CLOSED         PASS
NAMESPACE-SCOPED LISTING         PASS
EVIDENCE-ID LOOKUP               PASS ON FIXTURE
UNKNOWN-EVIDENCE FAIL-CLOSED     PASS
DUPLICATE-EVIDENCE FAIL-CLOSED   PASS
UNKNOWN-ROUTE FAIL-CLOSED        PASS
DUPLICATE-HEADING FAIL-CLOSED    PASS
DUPLICATE-JSON-KEY FAIL-CLOSED   PASS
PATH-CONFINEMENT                 PASS
KNOWLEDGE SEMANTICS UNCHANGED    PASS BY DIFF DESIGN
FULL REPOSITORY --validate       NOT EXECUTED IN THIS CHAT ENVIRONMENT
```

## Architecture rule

```text
logical knowledge ID != physical location
semantic routing metadata != marketing knowledge
evidence source ID != semantic route ID
one global manifest != one flat route list in reasoning
namespace first when already known
indexing must not rewrite knowledge semantics
heading selector first
marker only when necessary
physical split only after demonstrated context-loading failure
```

The manifest is an address table, not another framework. Evidence ledgers remain source ledgers. Small coherent files continue to be read normally until a real context-loading failure justifies finer routing.

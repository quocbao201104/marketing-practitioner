# Knowledge Routing v0.1 — Architecture Smoke

Branch: `candidate/knowledge-routing-index-v0.1`

Status: targeted architecture smoke, not a benchmark.

## Scope

The routing layer now covers the large independently routable knowledge surfaces in the skill:

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

No handbook or platform knowledge file is modified by this routing pass.

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

Logical IDs are the stable interface. File paths, headings, and marker selectors are implementation details and may change without changing the logical ID.

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

The full manifest now covers 13 namespaces and 190 logical routes while remaining 16,897 bytes in the branch snapshot inspected after expansion.

## Runtime lookup modes

```bash
python skills/marketing-practitioner/scripts/get-knowledge.py --namespaces
python skills/marketing-practitioner/scripts/get-knowledge.py --list
python skills/marketing-practitioner/scripts/get-knowledge.py --list --namespace shopee
python skills/marketing-practitioner/scripts/get-knowledge.py commerce.resolvability
python skills/marketing-practitioner/scripts/get-knowledge.py shopee.commercial-state shopee.representation
python skills/marketing-practitioner/scripts/get-knowledge.py --validate
```

The namespace-specific listing path is important: when the controller already knows the relevant domain/platform, it does not need to expose all 190 route IDs to the reasoning context.

## Mechanical smoke

The extraction helper was exercised against an isolated Markdown fixture using the same extraction logic as `get-knowledge.py` after the schema-v2 refactor.

| Check | Expected behavior | Result |
| --- | --- | --- |
| H1 | `##` heading route includes nested `###` / `####` content and stops before next `##` | PASS |
| H2 | `###` heading route includes nested `####` content and stops before next `###` / higher heading | PASS |
| M1 | marker route returns only content between one matching start/end pair | PASS |
| G1 | grouped namespace + section resolves to the expected heading chunk | PASS |
| G2 | grouped namespace + marker resolves to the expected marker chunk | PASS |
| G3 | namespace-specific route listing returns only that namespace | PASS |
| F1 | unknown namespace fails closed | PASS |
| F2 | unknown section / duplicated heading fails closed rather than guessing | PASS |
| F3 | path traversal outside the skill root fails closed | PASS |

Repeatable smoke command:

```bash
python skills/marketing-practitioner/scripts/test-knowledge-routing.py
```

Expected result:

```text
PASS    9 routing-mechanics smoke checks
```

## Manifest integrity command

The loader exposes repository-binding validation:

```bash
python skills/marketing-practitioner/scripts/get-knowledge.py --validate
```

This checks every indexed route against the checked-out skill tree and fails when a path or selector cannot be resolved exactly.

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

This keeps instrumentation minimal and avoids rewriting large knowledge files merely to create routing metadata.

## Current verdict

```text
LOGICAL-ID ABSTRACTION           PASS
GROUPED MANIFEST SCHEMA          PASS AFTER SIZE FAILURE CORRECTION
GLOBAL MANIFEST SIZE             PASS — 16,897 BYTES / 13 NAMESPACES / 190 ROUTES
HEADING EXTRACTION               PASS
NESTED HEADING BOUNDARIES        PASS
MARKER EXTRACTION                PASS
NAMESPACE-SCOPED LISTING         PASS
UNKNOWN-ROUTE FAIL-CLOSED        PASS
DUPLICATE-HEADING FAIL-CLOSED    PASS
PATH-CONFINEMENT                 PASS
KNOWLEDGE SEMANTICS UNCHANGED    PASS BY DIFF DESIGN
FULL REPOSITORY --validate       NOT EXECUTED IN THIS CHAT ENVIRONMENT
```

## Architecture rule

```text
logical ID != physical location
routing metadata != marketing knowledge
one global manifest != one flat route list in reasoning
namespace first when already known
indexing must not rewrite knowledge semantics
heading selector first
marker only when necessary
physical split only after demonstrated context-loading failure
```

The manifest is an address table, not another framework. Small coherent files should continue to be read normally until a real context-loading failure justifies finer routing.

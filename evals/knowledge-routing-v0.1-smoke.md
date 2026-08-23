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

Evidence files are handled differently. `references/bibliography.md`, `references/commerce-platform-evidence.md`, and platform evidence ledgers already expose stable intrinsic identifiers such as `[R23]`, `[C14]`, and `[A03]`. They are not decision modules and therefore are not duplicated into the semantic manifest. The loader resolves those identifiers directly with `--source` when helper execution is available.

No handbook, platform, framework, or reference knowledge file is modified by this routing pass. `SKILL.md` is changed only to consume the routing interface, define capability-aware fallback behavior, and remove duplicated physical heading/path bindings from the controller.

## Contract under test

```text
OPEN DECISION
→ KNOWLEDGE NAMESPACE
→ LOGICAL KNOWLEDGE ID
→ ROUTING MANIFEST
→ PHYSICAL FILE + SELECTOR
→ DETERMINISTIC EXTRACTION WHEN SUPPORTED
→ SMALLEST FEASIBLE DECISION-RELEVANT KNOWLEDGE CHUNK
```

For evidence traceability:

```text
CLAIM / CITATION NEED
→ INTRINSIC SOURCE ID
→ references/**/*.md
→ EXACT SOURCE HEADING
→ DETERMINISTIC EXTRACTION WHEN SUPPORTED
```

Logical knowledge IDs are the stable semantic interface. File paths, headings, and marker selectors are implementation details and may change without changing the logical ID.

## Schema correction discovered during the initial smoke

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
commerce.recommendation
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

After the independent adversarial review correction described below, the manifest covers 13 namespaces and 191 logical routes. The inspected branch file is 16,963 bytes.

## Independent adversarial review correction pass

An independent review of frozen head `fc00bdd8c5d089bec6b96fec106fc8b3ecf85fea` returned:

```text
REQUIRE MULTIPLE TARGETED CORRECTIONS
```

It found four bounded failures and did not require a new routing primitive or physical file split.

### A1 — fenced Markdown could silently truncate heading extraction

Failure:

```text
indexed section
→ fenced example contains heading-shaped line
→ old scanner treats fenced line as real heading
→ route succeeds with silently truncated knowledge
```

The same parser weakness could create a false evidence source or false duplicate from a fenced `[A03]`-shaped example.

Correction:

- heading discovery now ignores CommonMark-style backtick and tilde fenced blocks;
- evidence-source scanning reuses the same fence-aware line scanner;
- returned section content still preserves the fenced examples themselves;
- regression fixtures include fake `##` boundaries and fake `[A03]` / `[A99]` evidence headings inside both fence styles.

No full Markdown parser or new selector type was introduced.

### A2 — generic commerce recommendation was not addressable

Concrete decision:

```text
related-product / non-query recommendation question
→ generic commerce recommendation mechanics matter
→ commerce.discovery stops at Chapter 09 section 9
→ section 9 was unreachable through the logical interface
```

Correction:

```text
commerce.recommendation
→ ## 9. Recommendation and non-query discovery
```

This is one demonstrated addressability repair, not a completeness-driven route expansion.

### A3 — helper execution was an unstated portability assumption

Old controller wording privileged `scripts/get-knowledge.py` without defining what to do in a read-capable host that cannot execute Python/shell helpers.

Correction: `SKILL.md` now defines a capability ladder:

```text
helper execution available
→ use deterministic helper

helper unavailable + normal file reads available
→ use routing-index.json as address table
→ follow namespace path + exact selector
→ read/extract smallest feasible section

whole-file reads only
→ degrade to smallest target file
→ preserve dependency-first routing
```

The helper is explicitly a preferred deterministic capability, not a universal host requirement. Context-economy claims are therefore scoped: exact deterministic partial extraction is a helper-capable property; other hosts degrade according to their read capability rather than making the skill unusable.

Known evidence IDs follow the same principle: prefer `--source <ID>` when executable, otherwise locate the exact bracketed source heading and read the smallest feasible source section.

### A4 — invalid CLI mode combinations could succeed with the wrong artifact

Old behavior allowed option precedence such as:

```bash
get-knowledge.py commerce.resolvability --validate
```

to ignore the positional route and perform validation successfully.

Correction:

- route retrieval;
- `--source`;
- `--list`;
- `--namespaces`;
- `--validate`

are now mutually exclusive modes;
- `--namespace` is valid only as a `--list` modifier;
- mixed modes fail closed instead of returning a different successful artifact.

## Runtime lookup modes

Semantic knowledge when the helper is available:

```bash
python skills/marketing-practitioner/scripts/get-knowledge.py --namespaces
python skills/marketing-practitioner/scripts/get-knowledge.py --list
python skills/marketing-practitioner/scripts/get-knowledge.py --list --namespace shopee
python skills/marketing-practitioner/scripts/get-knowledge.py commerce.resolvability
python skills/marketing-practitioner/scripts/get-knowledge.py commerce.recommendation
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

Namespace-specific listing is the strongest context-economy path when helper execution is available: once the controller knows the relevant domain/platform, it does not need to expose all 191 route IDs to reasoning at once.

On hosts without helper execution, `routing-index.json` remains the address table, but achievable context economy depends on the host's file/section read capability.

## Mechanical smoke

The current routing/evidence mechanics test was re-executed after the adversarial corrections using the exact updated loader and test source copied from the candidate branch into the available execution sandbox. It returned:

```text
PASS    22 routing-mechanics smoke checks
```

This confirms the current mechanics code on deterministic fixtures. It is still distinct from executing the repository-binding `--validate` command against a normal checked-out branch.

The executed fixtures cover:

| Check | Expected behavior | Result |
| --- | --- | --- |
| H1 | `##` heading route includes nested lower headings and stops before next peer/higher heading | PASS |
| H2 | `###` route includes nested `####` content and stops before next peer/higher heading | PASS |
| H3 | heading-shaped lines inside backtick and tilde fences do not terminate extraction | PASS |
| M1 | marker route returns only content between one matching start/end pair | PASS |
| M2 | reversed marker order fails closed | PASS |
| G1 | grouped namespace + section resolves to expected chunk | PASS |
| G2 | grouped namespace + marker resolves to expected marker chunk | PASS |
| G3 | namespace-specific listing returns only that namespace | PASS |
| E1 | evidence ID resolves case-insensitively to one exact source heading | PASS |
| E2 | evidence lookup remains independent when semantic manifest is absent | PASS |
| E3 | evidence-source validation passes for unique IDs | PASS |
| E4 | fenced source-shaped examples are ignored and do not create duplicates/sources | PASS |
| E5 | unknown evidence source ID fails closed | PASS |
| E6 | duplicate evidence ID fails lookup and validation closed | PASS |
| F1 | unknown namespace fails closed | PASS |
| F2 | unknown section / duplicated heading fails closed rather than guessing | PASS |
| F3 | path traversal outside the skill root fails closed | PASS |
| F4 | duplicate JSON keys fail closed instead of silently overwriting | PASS |
| C1 | route retrieval + `--validate` mixed mode fails closed | PASS |
| C2 | `--list` + `--namespaces` mixed mode fails closed | PASS |
| C3 | `--namespace` without `--list` fails closed | PASS |

The script prints 22 because several table rows contain more than one assertion over the same contract boundary.

Repeatable command:

```bash
python skills/marketing-practitioner/scripts/test-knowledge-routing.py
```

## Manifest integrity command

The loader exposes repository-binding validation:

```bash
python skills/marketing-practitioner/scripts/get-knowledge.py --validate
```

This checks every indexed route against the checked-out skill tree and fails when a path or selector cannot be resolved exactly. It also scans all evidence ledgers for duplicate intrinsic source IDs. JSON parsing rejects duplicate keys so a repeated namespace/section cannot silently overwrite an earlier route.

Important evidence boundary: the current execution sandbox cannot obtain a normal GitHub checkout. An ephemeral PR workflow was attempted earlier, but no workflow run/status was created in the repository's current Actions configuration and that workflow was removed from the candidate diff.

Therefore the full checked-out-branch `--validate` command remains **not executed** in this session. The new `commerce.recommendation` selector and the other route selectors were bound against current branch/source headings through direct repository inspection; this is not equivalent to executing all 191 bindings locally.

Do not convert source inspection or fixture execution into a claim that all 191 branch selectors were repository-locally validated.

## Controller wiring

`SKILL.md` consumes the logical routing contract rather than duplicating its physical implementation.

The controller behavior is:

```text
open decision
→ identify namespace
→ inspect namespace-local logical IDs when needed
→ resolve smallest feasible logical route
→ expand only across a real unresolved dependency
```

Stable generic commerce interfaces now include:

```text
commerce.identity
commerce.commercial-state
commerce.discovery
commerce.recommendation
commerce.field-evidence
commerce.information-allocation
commerce.resolvability
commerce.agentic
commerce.diagnosis
```

Physical paths and selectors remain only in `routing-index.json`.

Platform routing uses namespace names as the stable interface:

```text
facebook
instagram
linkedin
tiktok
x

google-commerce
amazon
tiktok-shop
shopee
etsy
lazada
```

Evidence routing remains separate: known intrinsic source IDs are not duplicated into the semantic manifest.

### Static controller regression cases

These are controller-contract inspection cases, not model-performance claims.

| Case | Expected routing behavior | Result |
| --- | --- | --- |
| C1 supplied-message short social caption | stay fast; no deep namespace merely because a platform is named | PASS BY CONTROLLER TEXT |
| C2 consequential social discovery diagnosis | load only decision-relevant `content.*` / platform knowledge | PASS BY CONTROLLER TEXT |
| C3 narrow Shopee field task | use `shopee.*` only if current field semantics are missing; do not require `commerce.*` automatically | PASS BY CONTROLLER TEXT |
| C4 AI/conversational commerce strategy | use `commerce.information-allocation` / `commerce.resolvability`; platform namespace only when material | PASS BY CONTROLLER TEXT |
| C5 TikTok shoppable hybrid | compose `tiktok` + `tiktok-shop`, plus shared namespaces only for unresolved dependencies | PASS BY CONTROLLER TEXT |
| C6 known evidence source | use source-ID path without semantic routing or whole-ledger loading when avoidable | PASS BY CONTROLLER TEXT |
| C7 generic recommendation vs search | `commerce.recommendation` is independently addressable from `commerce.discovery` | PASS BY CONTROLLER TEXT + MANIFEST BINDING |
| C8 no helper execution | fall back through manifest/selector or smallest target file without abandoning dependency-first routing | PASS BY CONTROLLER TEXT |

## Selector strategy

Use existing stable Markdown headings first when the heading boundary already matches the desired knowledge chunk.

Heading discovery is fence-aware: heading-shaped lines inside backtick or tilde fenced examples are content, not boundaries.

Use explicit markers only when a logical route needs a boundary that headings cannot express cleanly:

```text
<!-- route:start logical.id -->
...
<!-- route:end logical.id -->
```

Marker extraction requires exactly one correctly ordered pair.

This keeps instrumentation minimal and avoids rewriting large knowledge files merely to create routing metadata.

Evidence source lookup does not require manifest entries. It scans `references/**/*.md` for one unique unfenced heading beginning with the requested bracketed source ID and returns that heading section only.

## Current verdict

```text
LOGICAL-ID ABSTRACTION              PASS
GROUPED MANIFEST SCHEMA             PASS AFTER SIZE FAILURE CORRECTION
GLOBAL MANIFEST SIZE                PASS — 16,963 BYTES / 13 NAMESPACES / 191 ROUTES
GENERIC RECOMMENDATION ADDRESS      PASS AFTER TARGETED CORRECTION
HEADING EXTRACTION                  PASS ON EXECUTED FIXTURES
FENCED-HEADING BOUNDARY             PASS ON EXECUTED FIXTURES
NESTED HEADING BOUNDARIES           PASS ON EXECUTED FIXTURES
MARKER EXTRACTION                   PASS
MARKER ORDER FAIL-CLOSED            PASS
NAMESPACE-SCOPED LISTING            PASS
EVIDENCE-ID LOOKUP                  PASS ON EXECUTED FIXTURES
FENCED SOURCE SCANNING              PASS ON EXECUTED FIXTURES
EVIDENCE/MANIFEST INDEPENDENCE      PASS ON EXECUTED FIXTURES
SOURCE-ID VALIDATION                PASS ON EXECUTED FIXTURES
UNKNOWN-EVIDENCE FAIL-CLOSED        PASS
DUPLICATE-EVIDENCE FAIL-CLOSED      PASS
UNKNOWN-ROUTE FAIL-CLOSED           PASS
DUPLICATE-HEADING FAIL-CLOSED       PASS
DUPLICATE-JSON-KEY FAIL-CLOSED      PASS
PATH-CONFINEMENT                    PASS
CLI MODE EXCLUSIVITY                PASS ON EXECUTED FIXTURES
CONTROLLER LOGICAL-ID WIRING        PASS BY STATIC DIFF INSPECTION
NO-HELPER FALLBACK                  PASS BY CONTROLLER TEXT
PHYSICAL ROUTE DUPLICATION          REMOVED FROM CONTROLLER
KNOWLEDGE SEMANTICS UNCHANGED       PASS BY DIFF DESIGN
FULL REPOSITORY --validate          NOT EXECUTED IN THIS SESSION
```

## Architecture rule

```text
logical knowledge ID != physical location
semantic routing metadata != marketing knowledge
evidence source ID != semantic route ID
one global manifest != one flat route list in reasoning
namespace first when already known
controller interface != physical heading/path binding
helper capability != universal host assumption
exact partial extraction != guaranteed on every host
indexing must not rewrite knowledge semantics
heading selector first
marker only when necessary
physical split only after demonstrated context-loading failure
```

The manifest remains an address table, not another framework. Evidence ledgers remain source ledgers. Small coherent files continue to be read normally until a real context-loading failure justifies finer routing.
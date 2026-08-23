# Knowledge Routing v0.1 — Vertical-Slice Smoke

Branch: `candidate/knowledge-routing-index-v0.1`

Status: targeted architecture smoke, not a benchmark.

## Scope

This smoke covers only the first routing slice:

- `handbook/08-content-environments-and-distribution.md`
- `handbook/09-commerce-environments-and-product-discovery.md`
- `skills/marketing-practitioner/routing-index.json`
- `skills/marketing-practitioner/scripts/get-knowledge.py`

The purpose is to test the routing contract before indexing platform modules.

## Contract under test

```text
OPEN DECISION
→ LOGICAL KNOWLEDGE ID
→ ROUTING MANIFEST
→ PHYSICAL FILE + SELECTOR
→ DETERMINISTIC EXTRACTION
→ SMALLEST DECISION-RELEVANT KNOWLEDGE CHUNK
```

Logical IDs are the stable interface. File paths, headings, and marker selectors are implementation details and may change without changing the logical ID.

## Current phase-1 coverage

The manifest currently exposes 17 routes across the content-environment and commerce handbooks, including:

```text
content.core-grammar
content.meaning-representation
content.audience-interaction
content.governance-eligibility
content.machine-mediation
content.feedback-dynamics
content.measurement-evidence
content.invariants

commerce.identity
commerce.commercial-state
commerce.representation
commerce.discovery
commerce.information-allocation
commerce.resolvability
commerce.field-evidence
commerce.agentic
commerce.diagnosis
```

## Mechanical smoke

The extraction helper was exercised against an isolated Markdown fixture using the same extraction logic as `get-knowledge.py`.

| Check | Expected behavior | Result |
| --- | --- | --- |
| H1 | `##` heading route includes nested `###` / `####` content and stops before next `##` | PASS |
| H2 | `###` heading route includes nested `####` content and stops before next `###` / higher heading | PASS |
| M1 | marker route returns only content between one matching start/end pair | PASS |
| F1 | unknown logical ID fails closed | PASS |
| F2 | duplicated heading selector fails closed rather than choosing one silently | PASS |
| F3 | path traversal outside the skill root fails closed | PASS |

Repeatable smoke command:

```bash
python skills/marketing-practitioner/scripts/test-knowledge-routing.py
```

Expected result:

```text
PASS    6 routing-mechanics smoke checks
```

## Manifest integrity command

The loader also exposes repository-binding validation:

```bash
python skills/marketing-practitioner/scripts/get-knowledge.py --validate
```

This checks every indexed route against the checked-out skill tree and fails when a path or selector cannot be resolved exactly.

Important evidence boundary: the current chat environment could not clone the GitHub branch into its execution filesystem, so the full checked-out-branch `--validate` command was **not** executed here. The phase-1 selectors were instead rebound against the current branch source through direct repository inspection, and several initially misremembered Chapter 09 section numbers were corrected before this smoke artifact was written.

Do not convert that source inspection into a claim that a repository-local validation command was executed when it was not.

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
LOGICAL-ID ABSTRACTION          PASS
HEADING EXTRACTION              PASS
NESTED HEADING BOUNDARIES       PASS
MARKER EXTRACTION               PASS
UNKNOWN-ID FAIL-CLOSED          PASS
DUPLICATE-HEADING FAIL-CLOSED   PASS
PATH-CONFINEMENT                PASS
SOURCE-BINDING DESIGN           PASS AFTER HEADING CORRECTION
FULL REPOSITORY --validate      NOT EXECUTED IN THIS CHAT ENVIRONMENT
```

## Gate to broader indexing

Proceed to platform-module indexing only if the contract remains:

```text
logical ID != physical location
routing metadata != marketing knowledge
indexing must not rewrite knowledge semantics
heading selector first
marker only when necessary
physical split only after demonstrated context-loading failure
```

No platform module, handbook theory, ontology, or marketing claim should be changed merely to make it indexable.

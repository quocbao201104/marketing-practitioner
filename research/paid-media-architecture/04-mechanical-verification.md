# Paid Media Architecture — Mechanical Verification

Status: **BOUNDED STRUCTURAL VERIFICATION PASS; FULL ROUTING SCRIPT NOT EXECUTED**  
Verification date: 2026-08-25  
Semantic implementation head reviewed: `f4f2f36abc6ed5b9399524d6c4fffd4689476c7c`  
Self-review commit: `ffff2ab9a14510fd0607803aee092281388b0d86`

## 1. Verification scope

This record deliberately separates:

```text
DIRECTLY VERIFIED STRUCTURE
from
EXECUTED TEST RESULTS
```

The candidate was inspected through GitHub repository reads and commit comparison. A sandbox checkout was also attempted in order to execute the routing smoke script locally, but the runtime could not resolve `github.com`, so no checked-out execution occurred.

Therefore this record **does not claim** that the full routing-mechanics script passed.

## 2. Candidate lineage

Direct comparison from the theory-freeze commit to the semantic implementation head showed:

```text
base: 9718ea1dffd1fd449847c2e750b790d9e221bd62
head: f4f2f36abc6ed5b9399524d6c4fffd4689476c7c
status: ahead
8 commits ahead
0 commits behind
```

The implementation diff contained exactly eight files and did not modify Chapter 08 or other specialist owners.

Result: **PASS**.

## 3. Direct route-binding verification

`routing-index.json` directly exposes one `paid-media` namespace with exactly these seven routes:

```text
paid-media.core
paid-media.objective
paid-media.control
paid-media.allocation
paid-media.observation
paid-media.decision-record
paid-media.invariants
```

Bindings:

```text
paid-media.core
→ ## 1. Scope: decide how economic resource becomes mediated paid exposure

paid-media.objective
→ ## 2. Objective and decision value

paid-media.control
→ ## 3. Control and authority envelope

paid-media.allocation
→ ## 4. Paid opportunity, allocation, realization, and exposure state

paid-media.observation
→ ## 5. Observation, billing, attribution, feedback, and causal boundary

paid-media.decision-record
→ ## 7. Compact paid-media decision record

paid-media.invariants
→ ## 8. Anti-folklore invariants
```

Result: **7 / 7 bindings present — PASS**.

## 4. Direct chapter-selector verification

Direct reads of `handbook/14-paid-media-architecture.md` confirmed the corresponding exact headings exist and are unique in the candidate chapter for the seven route targets above.

The chapter also retains the unrouted owner/handoff section:

```text
## 6. Owner boundaries and decision handoffs
```

No `paid-media.diagnosis` heading/route was added as a specialist surface.

Result: **7 / 7 routed headings present — PASS**.

## 5. Evidence-source verification

The candidate evidence ledger directly contains:

```text
## [PM03] Display & Video 360 — Frequency caps across auction and Programmatic Guaranteed inventory
```

at:

```text
references/paid-media-evidence.md
```

The routing smoke-test source expects the same source path and exact source heading.

Result: **PM03 source/path binding present — PASS**.

The ledger declares source IDs `PM01–PM14` and uses explicit `Supports` / `Does not support` boundaries.

## 6. Routing smoke-test source verification

The candidate `scripts/test-knowledge-routing.py` directly includes:

- all seven `paid-media.*` route expectations;
- one exact `PM03` evidence lookup assertion;
- existing email/discovery/source/mechanics assertions unchanged except for the additive paid-media coverage;
- terminal label `PASS\t57 routing-mechanics smoke checks`.

The count is a test-source label only until execution succeeds.

Result: **test source wired — PASS**.

## 7. Controller verification

Direct read of candidate `SKILL.md` confirms:

```text
metadata.version = 0.8.0
```

and a dedicated:

```text
## Paid media / paid distribution
```

operating path.

The controller includes:

- activation only for paid mediated exposure semantics that can change the decision;
- negative activation for ad-platform/campaign/CPC/CPA/ROAS/sponsored-content nouns alone;
- `PAID RELATIONSHIP ≠ PAID MEDIA DELIVERY`;
- `SPONSORED CONTENT ≠ PAID AMPLIFICATION`;
- the seven logical `paid-media.*` addresses without duplicating physical heading bindings;
- Chapter 05-first behavior when causal diagnosis remains open;
- Chapter 04 only when message/creative is actually implicated;
- explicit owner boundaries with Chapters 01/02, 04, 05, 08, 09, 10, 11, and 13;
- current-provider facts as JIT authoritative dependencies;
- a paid-media observation handoff to learning/diagnosis.

Result: **PASS**.

## 8. Version / release verification

No version bump was made during candidate implementation:

```text
SKILL.md = 0.8.0
```

The implementation diff contains no root README release update or CHANGELOG release entry.

Result: **PASS**.

## 9. Attempted local execution

A local sandbox checkout was attempted with:

```text
git clone --depth 1 --branch candidate/paid-media-architecture ...
```

The environment failed before checkout with DNS/network resolution error:

```text
Could not resolve host: github.com
```

No routing test was executed.

This is an environment limitation, not a passing or failing test result.

## 10. What is and is not claimed

Direct structural assertions completed:

```text
candidate lineage                         PASS
bounded changed-file scope                PASS
paid-media namespace present              PASS
7 / 7 route bindings present              PASS
7 / 7 exact routed headings present       PASS
PM03 evidence source/path present         PASS
routing smoke-test source wired           PASS
controller paid-media path present        PASS
fast-path / causal-owner boundary present PASS
version remains 0.8.0                     PASS
```

Not claimed:

```text
57 / 57 routing-mechanics script execution
full manifest runtime validation
full source scanner execution
GitHub Actions / CI execution
```

## 11. Mechanical verdict

```text
BOUNDED DIRECT STRUCTURAL VERIFICATION     PASS
FULL CHECKED-OUT ROUTING SCRIPT             NOT EXECUTED
BLOCKING STRUCTURAL DEFECT FOUND            NO

NEXT
→ targeted P01–P20 runtime walkthrough
```

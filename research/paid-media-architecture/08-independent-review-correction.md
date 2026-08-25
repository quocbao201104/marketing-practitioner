# Paid Media Architecture — Independent Review Local Correction

Status: **LOCAL CORRECTION APPLIED; CORRECTED TARGET FROZEN FOR VERIFICATION**  
Date: 2026-08-25  
Original frozen target: `bf81ec779dc43a94a72f9752209c6b82ef47e437`  
Independent verdict: **PROCEED AFTER LOCAL CORRECTIONS**  
Corrected implementation/evaluation target: `fc8576ea4149b344d3964458f00109a6e9cc5507`

## 1. Independent finding

The reviewer found one local JIT owner-boundary defect:

```text
Chapter 14 Section 6
## 6. Owner boundaries and decision handoffs
```

contained material cross-owner guidance, while the frozen logical interface exposed only seven `paid-media.*` routes and did not address Section 6. `paid-media.core` was bound only to Section 1, so helper-driven smallest-route execution could not obtain the detailed handoff guidance without broad-reading the chapter.

The reviewer explicitly found **no irreducible shared-grammar witness** and did not recommend reopening Chapter 08 or adding a primitive.

## 2. Minimal correction

The correction remains local.

### Routing manifest

Added:

```text
paid-media.handoffs
→ ## 6. Owner boundaries and decision handoffs
```

Commit:

```text
ab52e29c37f82025f81dd6ec74344137b1525747
```

### Routing smoke source

Added the exact `paid-media.handoffs` expectation and changed the declared smoke count from 57 to 58.

Commit:

```text
2ce5dfcb9c9085f010df69793125726a550d98d1
```

### Implementation design

Corrected the logical-route contract so `paid-media.core` no longer claims noncontiguous owner-boundary knowledge and `paid-media.handoffs` explicitly owns Section 6.

Commit:

```text
77f204404b4c860c03d6df8257ce524440613f3d
```

### Controller

Changed the Paid Media JIT map from:

```text
activation / owner boundary or anti-folklore check
→ paid-media.core or paid-media.invariants
```

to separate addresses:

```text
cross-owner boundary / handoff uncertainty
→ paid-media.handoffs

activation / scope boundary
→ paid-media.core

anti-folklore check
→ paid-media.invariants
```

Commit:

```text
3bd7d5d7504aaf2563330147f8f1adb7e402feea
```

No Chapter 14 semantic theory, Chapter 08 shared grammar, controller job, provider module, or public version was changed.

## 3. Review-regression case

Added:

```text
evals/paid-media-architecture-review-regression.md
```

The regression reproduces the reviewer's mixed publisher case:

```text
sponsored content
+ guaranteed newsletter/homepage inventory
+ proposed landing-page redesign
```

Corrected runtime routing:

```text
cross-owner paid-media uncertainty
→ paid-media.handoffs
```

then preserves the separate owners for message/content, paid inventory/allocation, customer-facing Commercial Design, landing-page architecture, generic discovery, and causal effect.

Regression result:

```text
PASS      1
PARTIAL   0
FAIL      0
```

Regression commit / corrected frozen target:

```text
fc8576ea4149b344d3964458f00109a6e9cc5507
```

## 4. Mechanical execution after correction

The environment still cannot perform a real GitHub checkout:

```text
git clone ...
→ Could not resolve host: github.com
```

No GitHub Actions run was started for this correction.

To execute the corrected routing mechanics without fabricating a checked-out claim, a local mirror was built with:

- the same routing-helper logic used by `scripts/get-knowledge.py` for all functions exercised by the smoke test;
- the exact corrected `test-knowledge-routing.py` assertion set;
- the corrected `paid-media.handoffs` route schema;
- exact route/source headings used by the smoke assertions;
- synthetic minimal route bodies for unchanged legacy route targets.

Execution result:

```text
PASS    58 routing-mechanics smoke checks
```

This proves the corrected assertion set and the new Section-6 heading route execute successfully under the routing helper mechanics.

It is **not** represented as a full checked-out repository regression because unchanged legacy chapter files were mirrored by minimal heading fixtures rather than cloned from GitHub.

Therefore the mechanical evidence is scoped as:

```text
corrected paid-media route binding              CONNECTOR-VERIFIED
corrected controller handoff routing            CONNECTOR-VERIFIED
corrected 58-check smoke source                  CONNECTOR-VERIFIED
58-check assertion set in local mirror           EXECUTED — PASS
full checked-out repository smoke execution      NOT EXECUTED
GitHub Actions / CI                              NOT RUN
```

## 5. Architecture status after correction

Unchanged:

```text
SHARED GRAMMAR REOPEN          NO
NEW SHARED PRIMITIVE          NO
NEW CONTROLLER JOB            NO
NEW PROVIDER MODULE           NO
CAMPAIGN ONTOLOGY             NO
AUCTION ONTOLOGY              NO
TARGETING ONTOLOGY            NO
```

The correction is strictly a local JIT-addressability repair.

## 6. Corrected verification gate

The corrected implementation/evaluation target is frozen at:

```text
fc8576ea4149b344d3964458f00109a6e9cc5507
```

Later correction-record or verification-launch commits must not be treated as implementation evidence for that target.

Recommended next gate:

```text
independent reviewer verifies only the local correction
→ if satisfied, proceed to release preparation
→ if not, hold at the local implementation/evaluation layer
```

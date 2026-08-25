# Paid Media Architecture — Independent-Review Regression

Status: **POST-REVIEW LOCAL-CORRECTION REGRESSION**  
Date: 2026-08-25  
Original frozen review target: `bf81ec779dc43a94a72f9752209c6b82ef47e437`  
Independent verdict: `PROCEED AFTER LOCAL CORRECTIONS`

## Purpose

This regression covers the only independent-review finding against the frozen target: Chapter 14 Section 6 contained material owner-boundary / handoff guidance but was not addressable through the `paid-media.*` JIT interface.

The correction adds:

```text
paid-media.handoffs
→ ## 6. Owner boundaries and decision handoffs
```

and changes controller routing so activation/scope, cross-owner handoffs, and invariants have separate logical addresses.

---

## R01 — Mixed publisher sponsorship / guaranteed inventory / landing-page redesign

**Facts**

- a publisher will produce sponsored content;
- the publisher guarantees paid newsletter and homepage inventory;
- the publisher also proposes a landing-page redesign;
- the marketer needs to decide which specialist owns each unresolved decision;
- no causal incrementality question is currently open.

**Task**

> Separate the decision ownership and load the smallest relevant Paid Media knowledge route.

**Expected runtime path**

```text
mixed cross-owner paid-media task
→ paid-media.handoffs
```

Then preserve:

```text
sponsored content / message / proof
→ Chapter 04 / Chapter 08 as materially required

publisher guaranteed inventory / media procurement / delivery obligation
→ Paid Media control / allocation semantics

customer-facing product/package/payment/terms design
→ Chapter 10 only if that commercial design itself is open

paid destination selection
→ Paid Media allocation semantics

landing-page sequence / proof / CTA / form / responsive architecture after entry
→ Chapter 11

generic non-paid discovery mechanics
→ Chapter 13 only if independently open

causal / incremental effect
→ Chapter 05 only if independently open
```

**Observed corrected runtime behavior**

The corrected controller now explicitly routes cross-owner boundary / handoff uncertainty to `paid-media.handoffs`. The routing manifest binds that ID directly to Chapter 14 Section 6, so helper-driven heading extraction can load the detailed owner/handoff knowledge without reading the whole chapter.

The case does not require a new shared primitive, new controller job, campaign ontology, or Chapter 08 change.

**Verdict: PASS**

---

## Regression result

```text
PASS      1
PARTIAL   0
FAIL      0
```

The independent-review failure is repaired at the local routing/controller layer.

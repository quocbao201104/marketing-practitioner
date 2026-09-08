# Pricing-Metric Selection Post-Review Repair Record

Status: **CLOSURE-ONLY REPAIR RECORD — NO THEORY REOPENING**

This artifact records the bounded repairs applied after the independent adversarial review of the frozen pricing-metric / charge-basis theory.

The reviewer verdict was `PASS_WITH_LOCAL_REPAIRS` with four MEDIUM findings (`CD-PM-T01`–`CD-PM-T04`) and two LOW findings (`CD-PM-T05`–`CD-PM-T06`). The core theory, Chapter 10 ownership, no-new-primitive conclusion, and no-new-chapter conclusion were not reopened.

---

## Closure matrix

```text
CD-PM-T01 — REPAIRED
CD-PM-T02 — REPAIRED
CD-PM-T03 — REPAIRED
CD-PM-T04 — REPAIRED
CD-PM-T05 — REPAIRED
CD-PM-T06 — REPAIRED
```

These labels record candidate repair status only. Independent post-repair verification should determine final closure.

---

## CD-PM-T01 — candidate generation no longer uses premature architecture gating

Repair location:

- `03-pricing-metric-selection-theory-freeze.md` §6.

Repair:

```text
GENERATE MATERIALLY PLAUSIBLE ARCHITECTURE CANDIDATES
usage-independent / variable / hybrid

→ for each materially plausible variable/hybrid candidate,
  instantiate concrete charge bases

→ only then select among surviving architectures
```

An authoritative constraint may prune a class before deeper search. Unsupported intuition may not.

This prevents the runtime-facing procedure from deciding `fixed / variable / hybrid` before the new charge-basis reasoning becomes active.

---

## CD-PM-T02 — Q/R/A/C is contract/formula-relative

Repair location:

- `03-pricing-metric-selection-theory-freeze.md` §4 and §6.

Repair:

- Q/R/A/C are now explicitly **roles in the current commercial design**, not intrinsic variable types.
- `R` includes variables, states, indices, classes, and derived scores that enter the customer-facing tariff/rate function.
- `C` is restricted to authoritative constraints that bound the decision but do not themselves enter the customer-facing pricing function.
- a variable incorporated into the pricing function plays an `R` role in that use rather than being elevated to `C` merely because it affects economics.
- the examples now treat insurance rating factors / expected loss and logistics fuel indexes accordingly.
- variables that do not play Q/R/A/C roles are not forced into the classification.

---

## CD-PM-T03 — normalization is not frozen as universally pre-tariff

Repair locations:

- `03-pricing-metric-selection-theory-freeze.md` §3.4 and §11;
- `04-pricing-metric-selection-evidence-ledger.md` PM07 and cross-source synthesis boundaries.

Repair:

The theory now distinguishes:

```text
TECHNICAL / USAGE NORMALIZATION
heterogeneous raw usage → common non-monetary/accounting unit

ECONOMIC / ACCOUNTING NORMALIZATION
raw usage × economic weights → credit/accounting unit
```

It explicitly states that normalization and tariff may be distinct or coupled and that:

```text
RAW → NORMALIZED UNIT → TARIFF
```

is a possible pattern rather than a universal ordering invariant.

GitHub AI Credits are now used as evidence for an economically weighted credit/accounting system, not as proof of neutral pre-tariff usage normalization.

---

## CD-PM-T04 — direct academic parent bound

Repair locations:

- `03-pricing-metric-selection-theory-freeze.md` §8 and §19;
- `04-pricing-metric-selection-evidence-ledger.md` PM09.

Added direct academic parent:

Andreas Hinterhuber (2017), **Value quantification capabilities in industrial markets**, *Journal of Business Research*, 76, 163–178.

DOI: `10.1016/j.jbusres.2016.11.019`

The source directly distinguishes value-based pricing from performance-based pricing through ex-ante versus ex-post/performance-contingent price setting and associated risk transfer/risk sharing.

The substantive practitioner rule was not expanded.

---

## CD-PM-T05 — OPEN QUESTION is now a formal status

Repair locations:

- `03-pricing-metric-selection-theory-freeze.md` §2, §19, §21;
- `04-pricing-metric-selection-evidence-ledger.md` open-question section.

The formal status vocabulary is now:

```text
EMPIRICAL / ACADEMIC
PROFESSIONAL PRACTICE
PROJECT SYNTHESIS
OPEN QUESTION
```

Previously deferred subjects remain unresolved rather than being promoted into runtime rules.

---

## CD-PM-T06 — Atlassian temporal claim corrected

Repair location:

- `04-pricing-metric-selection-evidence-ledger.md` PM08.

The ledger now distinguishes:

```text
CURRENT on 2026-09 research date:
credit measurement/accounting
pooled allowances
usage limits

ANNOUNCED FUTURE STATE:
extra-usage billing scheduled for 2026-12-03
```

No theory claim depends on extra-usage billing already being live.

---

## Repair boundary

This repair pass did **not**:

- add a new pricing primitive;
- add a top-level chapter;
- modify Chapter 10 runtime knowledge;
- modify `SKILL.md` or routing;
- introduce a universal pricing algorithm;
- introduce a generic weighted score;
- add a rule preferring outcome pricing;
- add an exhaustive candidate taxonomy;
- reopen price-level optimization, WTP methodology, legal/tax analysis, or revenue management.

The next valid step is independent post-repair verification of `CD-PM-T01`–`CD-PM-T06`. Runtime implementation remains deferred until that closure review passes.

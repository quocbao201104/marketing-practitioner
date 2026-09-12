# Copywriting Core — Post-Review Repair Record

Status: **BOUNDED IMPLEMENTATION REPAIR AFTER INDEPENDENT REVIEW**

Independent review target:

```text
candidate:
924e0a2cd950b9e2d72b27dffca471dd716b38a2

frozen base:
cb262967d4700982946731f96f615923c757133d
```

Independent verdict:

```text
PASS_WITH_REPAIRS
```

Architecture disposition:

```text
SOUND
```

The review did not justify any new primitive, controller job, specialist, chapter family, generic web-copy owner, or email-copy owner. The repair therefore stays inside the frozen architecture.

---

## 1. Repair scope

The independent review left three bounded gates:

```text
RG-01
repair stale copywriting subroute guidance in references/operating-guide.md

RG-02
add ownership-regression evals for resolved email and landing-page architecture

RG-03
reduce direct theory leakage in the strongest cued eval prompts
```

No theory reopening is permitted in this pass.

---

## 2. RG-01 — operating-guide subroute repair

Problem:

```text
references/operating-guide.md
could still route an unclear copywriting specialist question
back to the whole Chapter 04
```

Repair:

- added the smallest-route map for `copywriting.persuasion`, `copywriting.angle`, `copywriting.progression`, `copywriting.closure`, `copywriting.craft`, `copywriting.editing`, `copywriting.short-form`, and `copywriting.handoffs`;
- made `copywriting.core` optional rather than a mandatory hop;
- stated that whole-Chapter-04 loading is justified only when the open decision genuinely spans multiple Chapter 04 concerns and no narrower logical route can resolve it;
- preserved `routing-index.json` as the source of truth for physical selectors.

No new route or owner was introduced.

---

## 3. RG-02 — fixed-owner regression coverage

Added:

```text
BEH-COPY-CORE-009
resolved email architecture + exact body-expression request

BEH-COPY-CORE-010
resolved landing-page architecture + local paragraph repair
```

The email case fixes SEND, sequence position, relationship state, subject, body job, and destination, then asks only for body expression. The review criteria penalize reopening cadence, sequence, subject strategy, destination, offer, or channel state.

The landing-page case fixes page order, proof placement, implementation-section role, and CTA, then asks only for one paragraph repair. The review criteria penalize rebuilding section order, proof placement, page flow, or CTA architecture.

These cases test preservation of downstream owner state rather than asking the model to design those owners from scratch.

---

## 4. RG-03 — reduce prompt leakage

Hardened the most directly cued cases:

```text
BEH-COPY-CORE-003
removed the explicit instruction not to use a named copywriting formula

BEH-COPY-CORE-006
removed the instruction to edit only where a material defect exists;
now the model receives an ordinary improve-for-clarity request while KEEP/minimal repair remains hidden in review criteria

BEH-COPY-CORE-004
removed the explicit label that the Friday deadline is invented;
the absence of timing/availability support is now supplied as ordinary commercial evidence
```

The review criteria still test the frozen invariants; the user prompt reveals less of the desired reasoning.

No larger eval redesign was performed.

---

## 5. Deliberate no-change decisions

This repair does **not** change:

```text
Chapter 04 copywriting capability boundaries
Chapter 11 landing-page ownership
Chapter 12 email ownership
SKILL controller jobs
routing-index logical namespace design
copywriting theory freeze
short-form ownership boundary
global primitives or ontology
```

The independent review already found those architectural boundaries sound.

---

## 6. Post-repair gate

After repository mechanical validation passes, bind one exact repaired candidate SHA and perform a **narrow post-repair verification** limited to:

```text
RG-01 route discoverability / smallest-route behavior
RG-02 T9 and T10 ownership-regression coverage
RG-03 reduction in direct theory leakage
collateral-regression check limited to files touched by the repair
```

Do not reopen the six-core/two-application architecture unless a concrete post-repair failure requires it.

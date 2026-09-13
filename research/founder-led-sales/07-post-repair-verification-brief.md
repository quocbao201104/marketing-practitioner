# Founder-led Sales — Post-Repair Verification Brief

Act as the **INDEPENDENT POST-REPAIR VERIFIER** for Founder-led Sales in Marketing Practitioner.

Repository:

```text
https://github.com/quocbao201104/marketing-practitioner
```

Original independent-review candidate:

```text
06ef3bd93d06754bb9597b60cd7aa2bbe75cbd09
```

Review verdict on that candidate:

```text
PASS_WITH_LOCAL_REPAIRS
```

Verify only this repaired implementation candidate:

```text
3968aff927731e0dc8fb1ce6524cc2282f89333a
```

Do **NOT** use later commits as repaired candidate evidence.

Do **NOT** modify the repository.

Repository Verify passed on the repaired candidate in workflow run:

```text
34740446206
```

Treat that only as mechanical validation.

Read the governing records:

```text
research/founder-led-sales/05-independent-implementation-review-brief.md
research/founder-led-sales/06-local-repair-record.md
```

Do not reopen frozen Founder-led Sales theory, topology, or owner architecture unless a concrete repair regression makes it necessary.

---

## 1. Findings to verify

Verify exactly these independent-review findings.

### FLS-IMPL-01 — handoff route self-sufficiency

Original defect:

`founder-sales.handoffs` resolved Chapter 16 §11 but did not carry the frozen sales-specific handoff packet, creating state-loss / evidence-laundering / commitment-laundering risk under smallest-section JIT retrieval.

Required closure:

The existing `founder-sales.handoffs` route must now be self-sufficient for cross-owner transfer and preserve, when material:

```text
SUPPORTED
CONTRADICTED
AMBIGUOUS / MISSING
BLOCKING CONDITION
WHY IT MATTERS
NEXT DECISION
WHAT WOULD CHANGE THE DECISION
EXISTING COMMITMENTS
RESOURCE / ACCESS REQUIREMENTS
CURRENT FS1 ALLOCATION
NEXT OWNER
MUST-NOT-ASSUME
```

It must also preserve evidence provenance/status/scope/freshness/observation time and commitment lifecycle state without introducing a new primitive or second allocation owner.

### FLS-IMPL-02 — shared state fidelity

Original defect:

`founder-sales.state` omitted `OBSERVED_AT` and collapsed `CAPABILITY_OWNER` / `BUYER_OWNER` into a single `OWNER` field.

Required closure:

The existing Chapter 16 §2 state route must expose:

```text
OBSERVED_AT
CAPABILITY_OWNER
BUYER_OWNER
```

with semantics that preserve:

```text
freshness / staleness reasoning
FS ownership
buyer/external ownership of the next state transition
FS1 WAITING without manufactured seller activity
```

---

## 2. Regression checks

The repair must not weaken or duplicate the frozen owner boundaries.

Check at minimum:

```text
FS1 remains the sole global pursuit-allocation owner.

FS8 remains representation/history/freshness/forecast/learning,
not a second allocator.

Local stop signals remain local unless FS1 changes global allocation.

FS3 still owns access rather than proof selection.

FS5 still owns proof/evaluation rather than pursuit economics.

FS7 still applies/negotiates a buyer-specific commercial package,
while Chapter 10 owns the general commercial system.

Handoff preservation does not become a giant mandatory CRM schema.

The repaired state model remains conditional/minimum-sufficient,
not a universal stage checklist.
```

Check that the existing route selectors still resolve the intended exact headings:

```text
founder-sales.state
founder-sales.handoffs
```

Do not infer correctness merely from route existence or the passing Verify workflow.

---

## 3. Minimal adversarial verification cases

Reason through only the smallest cases necessary to verify the repairs.

### R1 — buyer-owned waiting

```text
Legal review is scheduled.
Buyer owns the next action.
No seller input is required now.
```

The repaired state route must allow the runtime to preserve buyer ownership and observation/freshness context so FS1 can represent `WAITING` without manufacturing seller work.

### R2 — proof → diagnosis handoff

```text
A valid POC shows the product works technically,
but the expected business effect does not appear.
The original causal diagnosis may be wrong.
```

The handoff route must preserve negative/mixed evidence, evidence status and provenance, the reopened blocking condition, commitments where relevant, and must-not-assume state when routing FS5 → FS4.

### R3 — local stop → FS1

```text
FS5 concludes STOP_PROVING.
A non-evidentiary blocker remains.
```

The handoff must preserve that `STOP_PROVING` is local and must not silently become global `STOPPED` before FS1 decides pursuit allocation.

### R4 — FS7 → FS1 resource change

```text
Buyer will sign only with large custom engineering work.
```

The handoff must preserve commercial package delta, forward burden/resource requirement, current commitments, current FS1 allocation when material, and next owner without letting FS7 become the portfolio allocator.

Do not run broad live-model benchmarking for this verification.

---

## 4. Permitted verdicts

Return exactly one:

```text
PASS
PASS_WITH_LOCAL_REPAIR
FAIL_REPAIR_INCOMPLETE
FAIL_REPAIR_REGRESSION
```

Use `PASS_WITH_LOCAL_REPAIR` only for a new strictly local defect that can be repaired without reopening the frozen theory or architecture.

---

## 5. Required output

Return exactly these sections and no extra preamble or postamble:

```text
VERDICT

REPAIRED CANDIDATE REVIEWED

FINDING CLOSURE
- FLS-IMPL-01: CLOSED / OPEN
- FLS-IMPL-02: CLOSED / OPEN

REGRESSION CHECK

MINIMAL ADVERSARIAL CASES
- R1
- R2
- R3
- R4

REMAINING MATERIAL FINDINGS

NEXT ACTION
```

For any remaining/new finding provide:

```text
ID
severity
file / route
concrete failure
why it matters
smallest repair
```

If both original findings are closed and no material repair regression remains, return `PASS` and state that the candidate may proceed to the already-frozen bounded runtime/path evaluation without reopening broad theory.
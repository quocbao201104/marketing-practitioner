# Founder-led Sales — Independent Adversarial Implementation Review Brief

Act as the **INDEPENDENT ADVERSARIAL IMPLEMENTATION REVIEWER** for the Founder-led Sales integration in Marketing Practitioner.

Repository:

```text
https://github.com/quocbao201104/marketing-practitioner
```

Review exactly this candidate:

```text
branch:
implementation/founder-led-sales-runtime

candidate HEAD:
06ef3bd93d06754bb9597b60cd7aa2bbe75cbd09
```

Frozen research base:

```text
branch:
research/founder-led-sales-integration

base HEAD:
8df2dd986369288e6f525e6a6b06ef59b089a431
```

Do **NOT** review later commits as candidate evidence.

Do **NOT** modify the repository.

The repository `Verify` workflow passed on candidate HEAD in run:

```text
34738977470
```

Treat that only as mechanical validation. It does not establish correct activation, owner selection, handoff semantics, or live model behavior.

This is an implementation review, not a request to restart broad Founder-led Sales research, choose a favorite sales methodology, add more acronyms, or redesign Marketing Practitioner from scratch.

Governing lineage:

```text
research/founder-led-sales/01-cross-fs-synthesis.md
research/founder-led-sales/02-runtime-contract.md
research/founder-led-sales/03-runtime-evaluation-brief.md
research/founder-led-sales/04-implementation-self-review.md
```

The self-review is context, not evidence that the candidate is correct.

---

## 1. Frozen topology

The candidate must preserve exactly these decision capabilities:

```text
FS1 — Pursuit Allocation / Resource Routing
FS2 — Opportunity / Account / Stakeholder Selection
FS3 — Engagement / Access / Contact Strategy
FS4 — Discovery / Diagnosis
FS5 — Solution Evaluation / Value / Proof
FS6 — Risk / Consensus / Decision Enablement
FS7 — Commercial Structure / Negotiation / Commitment
FS8 — Deal Progression / Pipeline / Learning
```

Do not recommend FS9, a new controller job, CRM ontology, global qualification score, or framework executor unless you can demonstrate a concrete decision that the frozen owners cannot represent without material loss.

The implementation intentionally represents FS1–FS8 as routes inside one handbook chapter rather than independent runtime services.

---

## 2. Frozen ownership rules

Pressure-test these as hard implementation boundaries.

### FS1 is the sole global pursuit-allocation owner

Only FS1 may determine whether scarce pursuit capacity should globally be:

```text
ACTIVE
LIGHT_TOUCH
QUEUED
WAITING
TRIGGER_DEFERRED
STOPPED
```

Local capability termination must remain local:

```text
FS3 → NO_WORTHWHILE_ACCESS_TRANSITION
FS5 → STOP_PROVING
FS6 → NO_CURRENT_VIABLE_DECISION_PATH
FS7 → WALK_CURRENT_PACKAGE
```

A local stop signal must not silently become global `STOPPED`.

### FS8 represents state; it does not absorb specialist decisions

FS8 may preserve:

```text
buyer-condition state
evidence / freshness
commitments
history
forecast
outcome
bounded learning
```

It must not become the owner of diagnosis, proof design, risk resolution, negotiation, or pursuit economics.

### Route by decision job, not topic noun

The candidate must not hard-route merely because a prompt contains:

```text
price
security
POC
proposal
legal
objection
silence
enterprise
```

Determine the unresolved decision first.

---

## 3. Candidate implementation surface

Inspect the candidate diff, especially:

```text
skills/marketing-practitioner/SKILL.md
skills/marketing-practitioner/routing-index.json
skills/marketing-practitioner/handbook/16-founder-led-sales-decision-runtime.md
skills/marketing-practitioner/handbook/README.md
skills/marketing-practitioner/references/founder-led-sales-evidence.md
skills/marketing-practitioner/scripts/test-knowledge-routing.py
.claude-plugin/plugin.json
.codex-plugin/plugin.json
docs/plugin.md
research/founder-led-sales/04-implementation-self-review.md
```

`get-knowledge.py` was intentionally left unchanged. Treat that no-change decision as falsifiable: report a defect if the current generic router cannot faithfully expose the new routes or evidence records.

Release-facing README/changelog/ZIP links are intentionally not finalized by this implementation candidate. Do not treat the current published v1.8.0 asset link as an implementation defect unless the candidate falsely claims a v1.9.0 asset already exists.

---

## 4. Required review questions

### A. Activation and fast path

Determine whether `founder-sales.*` activates only for unresolved buyer-specific commercial decisions.

Try to force false activation from:

```text
general ICP selection
positioning
pricing architecture
approved cold-email copywriting
customer research without a live commercial decision
```

Try to force false non-activation from:

```text
specific account pursuit allocation
buyer-specific stakeholder/access work
buyer-specific discovery
evaluation/proof request
consensus/risk barrier
buyer-specific commercial negotiation
deal-state/forecast/learning question
```

A sales noun alone must not be enough to activate the wrong route.

### B. FS2 ↔ FS1

Pressure-test:

```text
credible candidate situation
!=
worth active scarce capacity now
```

FS2 may identify a strong Account × Buying Situation while FS1 leaves it queued or stopped because portfolio allocation is unfavorable.

A failure exists if FS2 effectively becomes portfolio prioritization or FS1 duplicates account/ICP selection.

### C. FS3 ↔ FS1

Pressure-test:

```text
possible access transition
!=
worth spending more pursuit resource
```

FS3 may identify another legitimate route to a stakeholder. FS1 must still decide whether paying for that access work is justified.

Also check that FS3 owns access mechanics, not proof-mechanism selection or sentence-level outreach copy.

### D. FS4 ↔ FS5

Try cases where later evaluation evidence contradicts the original diagnosis.

The implementation must allow:

```text
FS5 → FS4
```

without calling the negative evidence a sales objection or rewriting the test result.

FS4 owns buyer reality / causal diagnosis; FS5 owns whether solution/value propositions are sufficiently evidenced.

### E. FS5 ↔ FS6

This is a highest-risk boundary.

Pressure-test:

```text
missing valid evidence
vs
risk / indecision / conflict after evidence is already sufficient
```

The candidate must permit:

```text
FS6 → FS5
```

when a binding proposition genuinely needs evidence, and:

```text
FS5 → FS6
```

when proof is sufficient but decision confidence/consensus/risk remains unresolved.

Do not reward more proof merely because the buyer asks for another demo/POC.

### F. FS6 ↔ FS7

Use the frozen gate:

> If mutually acceptable commercial terms existed now, would any material non-commercial reason still prevent commitment?

If yes, commercial negotiation is not yet the primary owner.

If no, FS7 may construct the buyer-specific agreement.

Try to make the candidate solve risk/value/consensus problems with discounts or contract terms.

### G. FS7 ↔ Chapter 10 ↔ FS1

Preserve three different decisions:

```text
Chapter 10
What commercial system should exist generally?

FS7
Is this specific buyer package mutually acceptable?

FS1
Is another scarce unit of pursuit here still worth allocating?
```

A buyer-requested customization or term change may require FS7 package reasoning and FS1 portfolio/resource re-evaluation without reopening the default commercial system.

### H. FS1 ↔ FS8

Try to make FS8's state/control language become a second pursuit allocator.

FS8 may detect:

```text
stale evidence
missed commitment
stall
waiting-by-design
forecast deterioration
```

but global pursue/wait/defer/stop economics must remain FS1's decision.

### I. Evidence and commitment preservation

Check that handoffs do not silently strengthen:

```text
signal → fact
buyer statement → verification
interest → commitment
accepted ask → fulfillment
friendly contact → champion
activity → buyer progress
```

Check that provenance, scope, and freshness are preserved where a later decision depends on them.

### J. Existing-owner regression

Founder-led Sales must not capture work already owned elsewhere.

Pressure-test at least:

```text
Chapter 01 — non-commercial customer research
Chapter 02 — market / ICP / segment selection
Chapter 03 — positioning
Chapter 04 / copywriting.* — wording/expression
Chapter 05 — formal causal diagnosis / experiment interpretation
Chapter 10 — default commercial-system design
```

---

## 5. Required adversarial scenarios

Reason through the smallest sufficient path for each. Do not run a broad benchmark.

### T1 — Tiny high-learning design partner

```text
small immediate revenue
material novel transferable uncertainty
founder uniquely useful for bounded learning
```

Expected:

```text
FS1 may authorize founder-heavy work
→ explicit learning question / exit condition
→ de-escalate after the founder-specific job resolves
```

Failure if founder involvement becomes account-permanent or learning is treated as unlimited subsidy.

### T2 — Huge self-service opportunity

```text
large possible contract
buyer can resolve all current material questions
through existing product/docs
no contextual human work is required
```

Expected:

```text
FS1 may choose SELF_SERVICE / LIGHT_TOUCH
```

Failure if high ACV itself forces high-touch sales.

### T3 — Endless proof after passed POC

```text
POC passed every predefined criterion
buyer asks for another generic demo
no new decision question
```

Expected:

```text
FS5 → STOP_PROVING
→ FS6 or no seller action depending on remaining state
```

Failure if another demo is automatically scheduled.

### T4 — Mandatory product gap

```text
EU-only hosting is mandatory
product cannot provide it
```

Expected:

```text
known GAP / CONSTRAINT
→ alternative if credible
→ FS1 pursuit consequence
```

Failure if generic security proof or objection handling substitutes for the gap.

### T5 — Buyer-owned waiting

```text
legal review scheduled
buyer owns next action
known review date
no seller input needed
```

Expected:

```text
FS1 WAITING
FS3 no contact action required
FS8 preserves the scheduled state
```

Failure if inactivity automatically creates follow-up.

### T6 — False consensus

```text
all stakeholders individually say yes
Operations assumes rollout = 2 weeks
IT assumes rollout = 3 months
```

Expected:

```text
FS6 CONFLICT
```

Failure if positive sentiment is treated as consensus.

### T7 — Useful but uneconomic proof

```text
custom validation would genuinely answer a material question
cost = 3 weeks founder/specialist effort
opportunity value and reusable learning are low
```

Expected:

```text
FS5 identifies valid evidence job
FS1 may refuse resource allocation
```

Failure if every legitimate buyer question automatically deserves seller resources.

### T8 — Late custom-work trap

```text
buyer will sign only with four custom modules
headline contract appears attractive
engineering/support burden is large and persistent
```

Expected:

```text
FS7 package delta / exposure
→ FS1 pursuit economics
→ resize/counter or global stop
```

Failure if `closable = should pursue`.

### T9 — “Too expensive” with unresolved value assumption

```text
buyer says price is too high
then says price is acceptable if two-FTE saving is established
```

Expected:

```text
value uncertainty / evidence work
not automatic discounting
```

### T10 — POC disproves original diagnosis

```text
product performs as specified
the expected business effect does not appear
valid evidence undermines original causal diagnosis
```

Expected:

```text
FS5 preserves result
→ FS4 reopens diagnosis
→ FS8 records epistemic progress / viability change
```

Failure if technical success is promoted to business success.

---

## 6. Static routing checks

Inspect exact selectors for:

```text
founder-sales.core
founder-sales.state
founder-sales.pursuit
founder-sales.selection
founder-sales.access
founder-sales.diagnosis
founder-sales.proof
founder-sales.decision
founder-sales.commercial
founder-sales.progression
founder-sales.handoffs
founder-sales.decision-record
founder-sales.invariants
```

Check the evidence lookup for:

```text
FS01–FS09
```

A route existing in the index is not by itself enough. Determine whether `SKILL.md` exposes the namespace at the correct open-decision boundary.

---

## 7. What does NOT count as a defect by itself

Do not report these merely because you prefer a different design:

```text
no dedicated sales agent
no CRM implementation
no MEDDPICC form
no BANT score
no fixed funnel stages
no champion primitive
no objection primitive
no FS9 router
no live sales benchmark in this candidate
no v1.9.0 release ZIP yet
```

A defect requires a concrete routing, ownership, evidence, handoff, fidelity, or implementation failure.

---

## 8. Permitted verdicts

Return exactly one:

```text
PASS
```

Candidate faithfully implements the frozen architecture; no material repair is required before bounded runtime evaluation / release preparation.

```text
PASS_WITH_LOCAL_REPAIRS
```

Architecture remains valid, but specific implementation defects should be repaired without reopening broad theory.

```text
RESEARCH_REOPEN_REQUIRED
```

A concrete implementation case exposes a decision the frozen research cannot represent or resolve without material ambiguity.

```text
ARCHITECTURE_REOPEN_REQUIRED
```

A concrete contradiction shows the eight-owner topology or a core ownership rule is structurally inadequate.

Do not invent additional verdict labels.

---

## 9. Required output

Return these sections:

```text
VERDICT

CANDIDATE REVIEWED

STRONGEST SURVIVING ARCHITECTURE PROPERTY

MATERIAL FINDINGS
- ID
- severity
- file / route
- concrete failure
- why it matters
- smallest repair

REQUIRED ADVERSARIAL SCENARIO RESULTS
T1–T10: PASS / FAIL + concise reason

ROUTING / EVIDENCE CHECK

SCOPE / OWNER REGRESSION CHECK

WHAT MUST NOT BE REOPENED

NEXT ACTION
```

If there are no material findings, state:

```text
MATERIAL FINDINGS
None.
```

Do not modify the repository.
Do not perform broad sales-literature research.
Do not infer correctness from CI passing, route count, mergeability, or documentation volume.

# Founder-led Sales — Implementation Self-Review

## Status

```text
IMPLEMENTATION CANDIDATE: f1e122ae8206059a194956bbf5d6317a6faf47d2
RESEARCH BASE:            8df2dd986369288e6f525e6a6b06ef59b089a431
BROAD THEORY:             CLOSED
LIVE BEHAVIORAL RUN:      NOT PERFORMED
```

This review checks whether the frozen Founder-led Sales synthesis was implemented as a small composable knowledge capability without introducing a second runtime, stage funnel, CRM ontology, or framework-driven sales process.

The candidate SHA above is the implementation under review. This self-review document is intentionally committed after the candidate and is not part of the candidate binding.

---

# 1. Implementation scope

The candidate changes only the following implementation surfaces relative to the frozen research head:

```text
skills/marketing-practitioner/SKILL.md
skills/marketing-practitioner/handbook/16-founder-led-sales-decision-runtime.md
skills/marketing-practitioner/handbook/README.md
skills/marketing-practitioner/references/founder-led-sales-evidence.md
skills/marketing-practitioner/routing-index.json
skills/marketing-practitioner/scripts/test-knowledge-routing.py
.claude-plugin/plugin.json
.codex-plugin/plugin.json
docs/plugin.md
```

It deliberately does **not** add:

```text
new controller job
new runtime service
new sales agent class
CRM schema
fixed funnel stages
qualification score
mandatory stakeholder graph
new get-knowledge implementation
sales-framework executor
live behavioral claims
```

---

# 2. Architecture mapping

The frozen eight-capability topology is represented as one indexed handbook chapter rather than eight independent runtime modules:

```text
founder-sales.pursuit      → FS1 pursuit allocation / resource routing
founder-sales.selection    → FS2 opportunity/account/stakeholder selection
founder-sales.access       → FS3 engagement/access/contact strategy
founder-sales.diagnosis    → FS4 discovery/diagnosis
founder-sales.proof        → FS5 solution evaluation/value/proof
founder-sales.decision     → FS6 risk/consensus/decision enablement
founder-sales.commercial   → FS7 commercial negotiation/commitment
founder-sales.progression  → FS8 deal progression/pipeline/learning
```

Additional routes expose shared state, owner handoffs, the compact decision record, and invariants without turning those into new capabilities.

This preserves the research conclusion that the router is orchestration, not FS9.

---

# 3. Activation and fast-path review

`SKILL.md` adds exactly one specialist namespace to the existing JIT knowledge table:

```text
founder-sales
```

Activation is buyer-specific. The controller boundary states that Founder-led Sales owns unresolved work for a concrete `Account × Buying Situation`, not general segmentation, positioning, default commercial-system design, or sentence-level expression.

Expected non-activation examples remain possible:

```text
"Write this approved cold email."
→ copywriting / direct execution

"Which segment should we target?"
→ Chapter 02

"Should our default package be per-seat or usage-based?"
→ Chapter 10
```

Expected activation examples include:

```text
"Should I spend founder time on this account's custom POC?"
→ founder-sales.proof + founder-sales.pursuit

"The buyer selected us but wants quarterly payment."
→ founder-sales.commercial
```

No controller job was added, so the seven generic runtime jobs remain unchanged.

---

# 4. Physical routing path

The intended deterministic route is:

```text
SKILL.md
  ↓
select founder-sales logical namespace
  ↓
routing-index.json
  ↓
handbook/16-founder-led-sales-decision-runtime.md
  ↓
exact selected heading
```

Evidence lookup remains independent:

```text
source ID such as FS06
  ↓
scripts/get-knowledge.py --source FS06
  ↓
references/founder-led-sales-evidence.md
  ↓
exact [FS06] source section
```

`get-knowledge.py` was not modified because its current generic grouped-semantic routing and evidence-source scanner already support this capability.

`test-knowledge-routing.py` adds exact heading assertions for all Founder-led Sales routes and an evidence-source assertion for `FS06`.

---

# 5. Boundary preservation

## FS1 vs other local STOP semantics

The implementation preserves one global pursuit owner:

```text
FS1 → ACTIVE / LIGHT_TOUCH / QUEUED / WAITING / TRIGGER_DEFERRED / STOPPED
```

Other capabilities may terminate only their local work:

```text
FS3 → NO_WORTHWHILE_ACCESS_TRANSITION
FS5 → STOP_PROVING
FS6 → NO_CURRENT_VIABLE_DECISION_PATH
FS7 → WALK_CURRENT_PACKAGE
```

Those local results feed FS1 rather than silently killing the whole pursuit.

## FS8 vs FS1

FS8 owns evidence-backed state/history/commitment/forecast/outcome/learning representation.

FS1 owns whether the next scarce unit of pursuit is worth allocating.

## FS3 vs FS5

FS5 chooses the evidence job/mechanism.

FS3 obtains the required person/interface/access when access work is needed.

## FS7 vs Chapter 10

Chapter 10 owns the general commercial system.

FS7 applies or negotiates that system for a specific buying situation and may reopen Chapter 10 only when a genuine system-design question appears.

## Founder-led Sales vs Copywriting

Sales resolves buyer-specific decisions such as who, why, what proof, what ask, what commitment, and what next state.

Chapter 04 / `copywriting.*` owns wording/expression after those decisions are sufficiently resolved.

---

# 6. Evidence implementation

The implementation adds a scoped evidence ledger with nine source records:

```text
FS01 Gartner — nonlinear B2B buying jobs
FS02 Huthwaite — SPIN as logical framework
FS03 MEDDICC — MEDDPICC qualification dimensions
FS04 Challenger/JOLT — customer indecision
FS05 Founding Sales — founder-led motion discovery/transfer
FS06 GitLab — governed Proof of Value
FS07 Gartner — buying-team conflict/consensus
FS08 Salesforce — Mutual Action Plans
FS09 Harvard PON — BATNA / reservation point / ZOPA
```

Each record contains both `Supports` and `Does not support` boundaries.

The chapter cites these records as evidence for local distinctions, not as authority for one universal methodology.

---

# 7. Runtime-state review

The chapter keeps the shared state surface small:

```text
Account × Buying Situation
Evidence Ledger
Buyer-Condition Model
Commitment Ledger
FS1 Pursuit Allocation
```

Specialist concepts remain local rather than becoming a giant global schema.

The implementation does not add a universal `QUALIFIED = true/false` object, a fixed opportunity score, or one aggregate confidence value.

It preserves:

```text
seller activity != buyer progress
interest != opportunity
problem != priority
fit != purchasability
proof activity != validation
friendly contact != mobilization
proposal/MAP/CRM stage != commitment
winnable deal != desirable pursuit
```

---

# 8. Resource-allocation review

The implementation makes human/founder escalation conditional on unresolved decision work rather than ACV, account size, stage, or logo prestige.

It explicitly supports the frozen adversarial outputs:

```text
tiny deal → founder-heavy
huge deal → self-service
winnable deal → stop
quiet deal → wait
good opportunity → queued
founder → specialist → self-service
repeatable normal deal → no founder
```

Founder involvement is issue-scoped and should de-escalate after the founder-specific job is resolved.

---

# 9. Proof / decision / commercial composition review

The chapter preserves these important transitions:

```text
FS5 → FS4
proof contradicts diagnosis

FS5 → FS6
proof is sufficient; remaining blocker is risk/consensus

FS6 → FS5
a binding uncertainty genuinely needs evidence

FS6 → FS3
required decision function exists but access is missing

FS7 → FS6
commercial work exposes non-commercial barrier

FS7 → FS1
package change alters forward pursuit economics

FS8 → specialist owner
new event/staleness/commitment failure exposes new work
```

No transition is described as a mandatory seller-stage progression.

---

# 10. Known non-claims

This implementation does **not** establish that a live model will:

```text
activate founder-sales at the correct time
select the correct subroute
avoid unrelated chapter reads
preserve state across long work episodes
follow local-vs-global STOP semantics
produce better sales outcomes
increase conversion / revenue
```

The routing manifest and static tests establish addressability/mechanical consistency only.

Live runtime behavior requires a separate bounded path evaluation after the implementation candidate is frozen and reviewed.

---

# 11. Release-state note

The implementation candidate sets the skill and plugin source metadata to `1.9.0` because Founder-led Sales is a new minor capability.

Release-facing assets are intentionally not fabricated:

```text
docs/skill-package.md
```

continues to point to the actually published v1.8.0 ZIP until a v1.9.0 release exists.

README/changelog release presentation should be finalized only after the implementation/review gate, not used as evidence that the capability passed runtime evaluation.

---

# 12. Self-review verdict

```text
TOPOLOGY PRESERVED:              YES
NEW PRIMITIVE REQUIRED:          NO
NEW RUNTIME REQUIRED:            NO
JIT ROUTING FIT:                 YES
OWNER BOUNDARIES REPRESENTABLE:  YES
EVIDENCE PROVENANCE PRESERVED:   YES
LOCAL/GLOBAL STOP SEPARATED:     YES
STATIC ROUTE TEST COVERAGE ADDED:YES
LIVE BEHAVIOR VERIFIED:          NO
```

## Candidate disposition

```text
READY_FOR_STATIC_VERIFICATION_AND_INDEPENDENT_REVIEW
```

Do not merge based on this self-review alone. First run repository verification on the implementation branch and independently inspect the frozen candidate against the research contract and high-risk composition edges.

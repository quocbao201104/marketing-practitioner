# Copywriting Core — Cross-SS Synthesis

Status: **SYNTHESIS COMPLETE — CANDIDATE FOR THEORY FREEZE**

Baseline:

```text
branch: main
HEAD: cb262967d4700982946731f96f615923c757133d
```

Research input consisted of eight independent specialist tracks:

```text
SS1 Persuasion Psychology
SS2 Angles / Hooks / Concepts
SS3 Argument & Body Progression
SS4 Proof / Objection / Risk / CTA
SS5 Sentence-Level Craft
SS6 Editing / Voice
SS7 Short-form
SS8 Web / Long-form
```

The synthesis does not assume that eight research tracks must become eight runtime modules. The question is which distinct decision capabilities survive cross-track comparison.

---

## 1. Surviving architecture

The research supports six core copywriting capabilities plus two application layers.

```text
UPSTREAM MARKETING STATE
research / audience / positioning / offer / evidence
                ↓
SS1  DIAGNOSE
     reader-state / decision barrier
                ↓
SS2  CHOOSE ROUTE
     persuasive angle / concept / hook
                ↓
SS3  BUILD PROGRESSION
     decision-relevant state change and dependency
                ↓
SS4  CLOSE RESPONSIBLY
     evidence / residual uncertainty / risk / commitment
                ↓
SS5  REALIZE
     warranted meaning at sentence / paragraph level
                ↓
SS6  EDIT / PRESERVE
     diagnose and repair existing expression
                ↓
SS7 / SS8
     realize the result under short-form or web/long-form constraints
```

The architecture is a dependency model, not a mandatory pipeline. A narrow task can enter directly at any sufficiently resolved downstream capability.

---

## 2. Capability dispositions

### SS1 — KEEP CORE

Owns psychological diagnosis, not persuasion tricks.

```text
observed signal
→ plausible reader-state hypothesis
→ binding barrier
→ conditional mechanism
→ evidence / condition check
→ backfire check
→ downstream requirement
```

It does not select the selling angle, sequence the argument, choose proof implementation, or write CTA wording.

### SS2 — KEEP CORE

Owns the persuasive route before prose.

Key distinction:

```text
ANGLE ≠ FRAME ≠ CONCEPT ≠ HOOK ≠ WORDING
```

Its main failure class is false strategic diversity: generating many paraphrases and calling them different angles.

### SS3 — KEEP CORE

Owns progression by decision-relevant reader-state change and logical dependency.

Reject:

```text
AIDA / PAS / BAB / 4P / PASTOR
as universal sequencing engines
```

Retain them only as optional shorthand when they happen to fit the current dependency structure.

### SS4 — KEEP CORE

Owns persuasive closure.

The surviving decision architecture is:

```text
TARGET ACTION
→ REQUIRED BELIEF
→ MATERIAL BARRIER
→ EVIDENCE ADEQUACY
→ RESOLVABLE / RESIDUAL UNCERTAINTY
→ RISK TREATMENT
→ COMMITMENT PROPORTIONALITY
→ NEXT JUSTIFIABLE ACTION
```

No separate subsystem is justified for social proof, guarantees, scarcity, objection handling, urgency, or CTA formulas.

### SS5 — KEEP CORE

Owns realization of already-authorized meaning.

The governing objective is not shorter, punchier, more vivid, or more active prose. It is minimizing unnecessary interpretive work while preserving warranted meaning, scope, relations, reference, and implication.

### SS6 — KEEP CORE

Owns repair of existing expression.

```text
existing copy
→ diagnose material defect
→ determine authorized envelope
→ smallest sufficient repair
→ preservation / regression audit
```

`KEEP` is a successful result. Editing is not default rewriting.

### SS7 — KEEP AS APPLICATION LAYER

Short-form is constrained realization, not a separate persuasion theory.

It specializes attention allocation, compression, surface orchestration, sequence/exposure memory, source/role integrity, interaction frame, and handoff continuity under severe communication constraints.

### SS8 — KEEP AS APPLICATION LAYER

Web / long-form is decision-support architecture, not a page-template library.

It specializes reader-state envelope, decision needs, dependency, scan/deep paths, information reachability, local sufficiency, cross-page delegation, and transition continuity.

---

## 3. Cross-SS ownership adjudication

### SS1 ↔ SS4

Shared vocabulary such as belief, risk, uncertainty, and barriers does not imply duplicate ownership.

```text
SS1 = why the reader may be blocked and what class of mechanism may matter
SS4 = whether available support and remaining risk justify the requested commitment
```

Do not create two reader-state ontologies.

### SS3 ↔ SS8

```text
SS3 = logical progression / dependency / state transition
SS8 = web allocation / reachability / branching / scan paths / cross-page architecture
```

SS3 may identify that a dependency exists across artifacts. It must not become the detailed web-page architecture owner.

### SS5 ↔ SS6

```text
SS5
AUTHORIZED DECISION
→ EXPRESSION

SS6
EXISTING EXPRESSION
→ DIAGNOSE
→ WARRANTED REPAIR
→ REGRESSION AUDIT
```

SS6 may use SS5 craft operators to realize a repair, but it does not own blank-page expression by default.

---

## 4. Rejected decomposition

The research does not justify first-class runtime owners for:

```text
headline formulas
storytelling formulas
social proof
urgency / scarcity
power words
CTA formulas
AIDA / PAS / BAB / 4P / PASTOR
funnel stages
humanizer pattern lists
```

These are techniques, proof forms, operators, heuristics, or surface manifestations governed by the surviving capabilities.

---

## 5. Integration direction

Do not create eight handbook chapters or a new controller job.

The preferred integration is:

1. keep Chapter 04 as the message / proof / copy owner;
2. expose bounded `copywriting.*` just-in-time routes inside Chapter 04 for the six core capabilities and short-form realization;
3. repair Chapter 11 with the SS8 decision-graph / path / cross-page findings rather than creating a duplicate generic web-copy owner;
4. keep Chapter 12 as the email communication-architecture owner and hand exact short-form expression back to `copywriting.short-form` / `copywriting.craft` when needed;
5. preserve existing downstream representation ownership and fast paths;
6. add adversarial cases that distinguish good prose from correct copywriting decisions.

---

## 6. No-SS9 disposition

No ninth core capability is currently justified.

A new capability should be added only if adversarial integration or runtime evaluation exposes a concrete decision failure that cannot be represented without material loss by SS1–SS8 and the existing Marketing Practitioner owners.

# Paid Media Architecture — Implementation Self-Review

Status: **PASS TO BOUNDED MECHANICAL / TARGETED EVALUATION**  
Review date: 2026-08-25  
Theory freeze: `research/paid-media-architecture/01-theory-freeze.md`  
Implementation design: `research/paid-media-architecture/02-implementation-design.md`  
Reviewed candidate head: `f4f2f36abc6ed5b9399524d6c4fffd4689476c7c`

## 1. Review question

Does the candidate implement the frozen Paid Media specialist capability without reopening shared grammar, inventing a new controller job, turning provider UI nouns into ontology, or making ordinary ad-related writing unnecessarily complex?

## 2. Scope review

Compared with the theory-freeze commit `9718ea1dffd1fd449847c2e750b790d9e221bd62`, the reviewed candidate is 8 commits ahead and 0 behind.

The implementation diff contains exactly eight files:

```text
ADDED
- evals/paid-media-architecture-adversarial-cases.md
- research/paid-media-architecture/02-implementation-design.md
- skills/marketing-practitioner/handbook/14-paid-media-architecture.md
- skills/marketing-practitioner/references/paid-media-evidence.md

MODIFIED
- skills/marketing-practitioner/SKILL.md
- skills/marketing-practitioner/handbook/README.md
- skills/marketing-practitioner/routing-index.json
- skills/marketing-practitioner/scripts/test-knowledge-routing.py
```

No Chapter 08 shared-grammar file, existing specialist chapter, platform module, commerce module, framework, or release document was modified.

Verdict: **PASS**.

## 3. Frozen primary unit and model

The candidate preserves:

```text
PRIMARY UNIT
→ PAID MEDIA DECISION

FOUR QUESTIONS
→ OBJECTIVE / DECISION VALUE
→ CONTROL / AUTHORITY ENVELOPE
→ ALLOCATION / REALIZATION STATE
→ OBSERVATION / FEEDBACK
```

Chapter 14 does not promote `campaign`, `ad`, `auction`, `bid`, `targeting`, `learning`, `feedback`, or `exposure` to a shared primitive.

Verdict: **PASS**.

## 4. Activation and fast-path behavior

Both Chapter 14 and `SKILL.md` preserve:

```text
PAID RELATIONSHIP
≠ PAID MEDIA DELIVERY

SPONSORED CONTENT
≠ PAID AMPLIFICATION
```

The controller does not activate the specialist merely because a prompt names Facebook Ads, Google Ads, TikTok Ads, LinkedIn Ads, campaign, CPC, CPA, ROAS, sponsored content, or paid work.

The bounded transformation example remains explicit:

```text
approved ad headline + length transformation
→ fast path
```

Verdict: **PASS**.

## 5. Controller-job discipline

The implementation reuses the existing runtime jobs:

```text
WRITE
DECIDE
DIAGNOSE
RESEARCH / UNDERSTAND
ADAPT
TEST
LEARN
```

No `MEDIA_PLAN`, `BUY_MEDIA`, `OPTIMIZE_CAMPAIGN`, or other controller job was introduced.

Verdict: **PASS**.

## 6. Shared-grammar discipline

Chapter 14 explicitly inherits the existing Chapter 08 parent roles:

```text
ACTOR / SOURCE
OBJECT
REPRESENTATION
AUDIENCE STATE
TYPED RELATIONSHIP / ACCESS / DELIVERY EDGE
INTERACTION ACT
PLATFORM / MEDIATION STATE
OBSERVATION RECORD

+ provenance
+ scope / relativity
+ history / state transition
```

Paid-media nouns such as budget, bid strategy, audience signal, campaign, learning phase, placement, attribution window, frequency cap, and guaranteed deal remain local states/settings/relations unless the existing independent-identity test would already justify an object.

Verdict: **PASS**.

## 7. Routing-surface discipline

The candidate exposes exactly seven specialist routes:

```text
paid-media.core
paid-media.objective
paid-media.control
paid-media.allocation
paid-media.observation
paid-media.decision-record
paid-media.invariants
```

No `paid-media.diagnosis` route was introduced. Causal diagnosis remains Chapter 05-first when the cause of a paid-performance symptom is unresolved.

The route surface follows the frozen theory rather than provider UI taxonomy.

Verdict: **PASS**.

## 8. Owner-boundary review

The candidate preserves the intended owners:

```text
Chapter 01 / 02
→ customer / segment / demand

Chapter 04
→ ad message / claim / proof

Chapter 05
→ causality / incrementality / experiment / causal spend leverage

Chapter 08
→ shared platform/content grammar

Chapter 09
→ product / variant / listing / commerce identity

Chapter 10
→ customer-facing Commercial Design

Chapter 11
→ landing-page architecture after entry

Chapter 13
→ generic non-paid discovery

Paid Media
→ paid objective/control/allocation/realization/billing/attribution/feedback semantics
```

Retail media is composed with Chapter 09 rather than creating a sponsored-product primitive. Creator sponsorship without paid amplification is not silently absorbed. Generic discovery is not flattened into paid economic allocation.

Verdict: **PASS**.

## 9. Causal boundary review

Chapter 14 distinguishes:

```text
DELIVERY EVENT
≠ OBSERVATION
≠ BILLING EVENT
≠ ATTRIBUTED OUTCOME
≠ OPTIMIZATION-ELIGIBLE SIGNAL
≠ OPTIMIZATION FEEDBACK
≠ CAUSAL EFFECT
```

and sends counterfactual effect, incrementality, experiment design, and causal spend leverage to Chapter 05.

It does not introduce a second attribution or causal framework.

Verdict: **PASS**.

## 10. Provider-evidence discipline

The evidence ledger uses `PM01–PM14`, with `Supports` and `Does not support` boundaries. Chapter 14 treats provider objectives, audience controls, auction/deal mechanics, learning state, billing, attribution, policy, and automation as current JIT dependencies.

No current Meta, Google, TikTok, LinkedIn, programmatic, or DOOH behavior is promoted to a universal provider-independent guarantee.

Provider modules were not added.

Verdict: **PASS**.

## 11. Exposure / measurement discipline

The candidate preserves:

```text
DELIVERED / RENDERED
≠ OPPORTUNITY TO SEE
≠ LIKELY SEEN
≠ VERIFIED HUMAN ATTENTION

REPORTED REACH
≠ EXACT UNIQUE HUMANS

REPORTED FREQUENCY
≠ EXACT EXPOSURE HISTORY OF EVERY HUMAN
```

Observation unit, modeling, coverage, time/maturity, attribution, and optimization-feedback role are retained only when materially decision-relevant.

Verdict: **PASS**.

## 12. Version / release discipline

`SKILL.md` remains:

```text
version: 0.8.0
```

No README release status, CHANGELOG release entry, or public version bump was performed during implementation.

Verdict: **PASS**.

## 13. Self-review risks retained for evaluation

The implementation should still be pressure-tested for these failure modes:

1. **Over-activation risk** — ad/campaign nouns accidentally trigger deep paid-media reasoning on a simple copy task.
2. **Ch05 ordering risk** — a performance symptom is treated as a paid-media lever decision before causal diagnosis localizes the open mechanism.
3. **Control-precedence risk** — a setting name is treated as an absolute constraint without scope/authority/competing obligations.
4. **Campaign-boundary risk** — campaign container is treated as resource or optimization boundary despite shared/portfolio/deal structure.
5. **Feedback-role risk** — reported/attributed events are assumed to be optimization feedback.
6. **Creative-blame risk** — weak delivery is converted into a message/creative rewrite before paid-control/allocation state is discriminated.
7. **Provider-transfer risk** — one platform's current auction, audience, learning, or billing behavior is generalized to another.

These risks are represented by P01–P20 and are not blockers before targeted evaluation.

## 14. Self-review verdict

```text
THEORY FIDELITY                  PASS
SCOPE / DIFF BOUNDARY            PASS
FAST PATH                        PASS
SHARED GRAMMAR CLOSED            PASS
NEW SHARED PRIMITIVE             NO
NEW CONTROLLER JOB               NO
OWNER BOUNDARIES                 PASS
CAUSAL BOUNDARY                  PASS
PROVIDER MODULES                 NO
RELEASE / VERSION DRIFT          NO

VERDICT
→ PASS TO BOUNDED MECHANICAL / TARGETED EVALUATION
```

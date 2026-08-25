# Paid Media Architecture — Bounded Implementation Design

Status: **APPROVED FOR CANDIDATE IMPLEMENTATION**  
Design date: 2026-08-25  
Theory freeze: `research/paid-media-architecture/01-theory-freeze.md`  
Candidate branch: `candidate/paid-media-architecture`

## 1. Design objective

Implement the frozen Paid Media specialist capability without reopening the Chapter 08 shared grammar, adding a new controller job, or turning current provider implementation details into permanent ontology.

The implementation must preserve the frozen primary unit:

```text
PAID MEDIA DECISION
```

and the four-question model:

```text
1. OBJECTIVE / DECISION VALUE
2. CONTROL / AUTHORITY ENVELOPE
3. ALLOCATION / REALIZATION STATE
4. OBSERVATION / FEEDBACK
```

## 2. Runtime shape

Add one bounded specialist chapter:

```text
skills/marketing-practitioner/handbook/14-paid-media-architecture.md
```

Add one scoped evidence ledger:

```text
skills/marketing-practitioner/references/paid-media-evidence.md
```

Expose one JIT namespace:

```text
paid-media.*
```

Do not create Meta Ads, Google Ads, TikTok Ads, LinkedIn Ads, programmatic, retail-media, creator-media, or DOOH runtime modules in this candidate. Current provider facts remain authoritative just-in-time dependencies.

## 3. Proposed logical routes

The implementation surface is intentionally smaller than the research field map.

```text
paid-media.core
→ scope, activation boundary, shared-parent grammar, owner boundaries

paid-media.objective
→ business/media decision value vs platform objective / optimization signal

paid-media.control
→ resources, constraints, signals, authorizations, obligations,
  measurement rules, scope, authority, and precedence

paid-media.allocation
→ opportunity eligibility, buying mechanism, resource/allocation boundary,
  pacing/bidding/mediation state, execution, delivery/rendering, exposure discipline

paid-media.observation
→ delivery/billing/attribution/optimization-feedback semantics,
  event definition, unit, maturity, modeling, provenance, causal handoff

paid-media.decision-record
→ compact retained paid-media decision state

paid-media.invariants
→ anti-folklore distinctions
```

No `paid-media.diagnosis` route is justified at implementation-design time. When cause is unresolved, Chapter 05 remains the diagnosis owner. Paid Media is loaded only after the open decision reaches paid control/allocation/observation semantics.

## 4. Chapter structure

Use these stable headings so the routing surface remains close to the theory rather than provider UI nouns:

```text
## 1. Scope: decide how economic resource becomes mediated paid exposure
## 2. Objective and decision value
## 3. Control and authority envelope
## 4. Paid opportunity, allocation, realization, and exposure state
## 5. Observation, billing, attribution, feedback, and causal boundary
## 6. Owner boundaries and decision handoffs
## 7. Compact paid-media decision record
## 8. Anti-folklore invariants
```

Do not add permanent sections for `campaign architecture`, `auction architecture`, `targeting architecture`, `learning phase`, or `media funnel`.

## 5. Controller integration

Add one operating-path rule to `SKILL.md` after platform/discovery context is established:

- activate Paid Media only when economic resource is being used to secure, reserve, compete for, allocate, or amplify mediated audience exposure **and** paid-delivery semantics can change the current decision;
- do not activate merely because the prompt mentions an ad platform, campaign, CPC, CPA, ROAS, sponsored content, or paid work;
- preserve the fast path for supplied transformations such as shortening an already-approved ad headline;
- when cause is unresolved, Chapter 05 remains first owner;
- use Chapter 04 only if message/claim/proof remains open;
- use Chapter 09 when product/listing identity or commerce state is material;
- use Chapter 11 only if landing-page architecture itself is open;
- use Chapter 13 only for generic discovery mechanics, not paid economic allocation.

Do not create a new controller job. Existing `WRITE`, `DECIDE`, `DIAGNOSE`, `RESEARCH / UNDERSTAND`, `ADAPT`, `TEST`, and `LEARN` remain sufficient.

## 6. Shared grammar discipline

Paid Media must instantiate, not extend, the Chapter 08 parent roles:

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

Local labels such as budget, bid strategy, audience signal, campaign, learning phase, placement, attribution window, frequency cap, or guaranteed deal remain states/relations/settings/implementation nouns unless independent identity is decision-relevant under the existing object test.

## 7. Evidence ledger design

Use `PMxx` source IDs. Initial evidence should pressure the frozen distinctions rather than maximize provider coverage.

Planned source set:

```text
PM01 Google Ads — primary vs secondary conversion actions
PM02 Google Ads — data exclusions
PM03 Display & Video 360 — frequency caps and Programmatic Guaranteed precedence
PM04 Display & Video 360 — Programmatic Guaranteed / fixed inventory
PM05 TikTok Ads — Smart+ audience controls vs audience suggestions
PM06 TikTok Ads — view-through attribution as reporting + optimization signal
PM07 TikTok Ads — learning phase as history-conditioned delivery state
PM08 LinkedIn Ads — cost cap, learning, optimization goal vs chargeable event
PM09 LinkedIn Ads — bidding strategies / billing semantics
PM10 LinkedIn Ads — auction bid + relevance, not bid alone
PM11 Meta Engineering — Andromeda ad retrieval and Advantage+ automation
PM12 IAB — Creator Economy taxonomy: sponsored content vs paid amplification
PM13 IAB — programmatic terminology: auction vs fixed / automated guaranteed
PM14 IAB — DOOH measurement: delivered / OTS / LTS / audience exposure distinctions
```

Evidence entries must state both `Supports` and `Does not support`. Current provider settings, algorithms, thresholds, auction formulas, objectives, policy states, and attribution defaults remain time-sensitive JIT inputs.

## 8. Targeted adversarial evaluation design

Create one bounded evaluation file:

```text
evals/paid-media-architecture-adversarial-cases.md
```

The evaluation should pressure routing and decision semantics, not test provider trivia.

Minimum case families:

```text
P01 fast-path ad-headline transformation
P02 paid creator sponsorship without paid amplification
P03 creator post + paid amplification
P04 business goal vs platform optimization-event mismatch
P05 primary vs observation-only conversion signal
P06 audience suggestion vs enforced targeting control
P07 budget vs bid vs spend distinction
P08 campaign container vs shared/portfolio allocation boundary
P09 guaranteed inventory vs auction assumption
P10 control precedence under guaranteed-delivery obligation
P11 learning/adaptive state after material edit
P12 underdelivery without blaming creative
P13 platform specification vs executed placement/creative/destination
P14 delivered/rendered vs verified human attention
P15 reported reach/frequency with modeled identity
P16 billing event vs optimization event
P17 attributed conversion vs incremental effect
P18 reported conversion excluded from optimization feedback
P19 retail-media composition with Chapter 09 product identity
P20 generic discovery vs paid economic allocation boundary
```

Targeted adjudication should reject any implementation that:

- routes ordinary ad copy transformations into deep paid-media knowledge;
- turns paid relationship into paid-media delivery by default;
- treats `campaign` as the universal decision/resource/optimization unit;
- treats `targeting` as one kind of hard audience fence;
- assumes all paid media uses auctions;
- collapses budget, bid, allocation, pacing, spend, billing, attribution, and causality;
- blames creative from weak delivery without localizing the paid-control/allocation state;
- creates a provider-specific guarantee from current documentation.

## 9. Mechanical integration

Update only the existing routing mechanics necessary to expose `paid-media.*`:

```text
routing-index.json
handbook/README.md
scripts/test-knowledge-routing.py
SKILL.md
```

The routing smoke test should verify every new logical route and at least one `PMxx` evidence lookup. Do not claim the full mechanical suite passed unless it was actually executed against the checked-out candidate.

## 10. Explicit implementation non-goals

Do not implement:

```text
new shared primitives
new shared edges
new controller jobs
new universal media funnel
new media optimizer
new attribution model
new causal framework

Meta Ads module
Google Ads module
TikTok Ads module
LinkedIn Ads module
retail-media module
DOOH module

campaign ontology
auction ontology
targeting ontology
learning-state ontology
```

Do not bump the public skill version, README release status, or CHANGELOG during implementation/evaluation. Release metadata belongs after the independent review gate.

## 11. Implementation gate

Candidate implementation may proceed only if it remains bounded by this design and the frozen theory.

```text
THEORY FREEZE                     PASS
IMPLEMENTATION DESIGN             PASS
SHARED GRAMMAR REOPEN             NO
NEW SHARED PRIMITIVE              NO
NEW CONTROLLER JOB                NO
PROVIDER MODULES                  NO

NEXT
→ bounded candidate implementation
→ self-review
→ mechanical verification
→ targeted runtime evaluation
→ targeted adjudication
→ independent review
```

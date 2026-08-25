# Paid Media Architecture — Independent Adversarial Runtime Review Brief

Status: **FROZEN REVIEW CONTRACT**  
Repository: `https://github.com/quocbao201104/marketing-practitioner-skill`  
Candidate branch: `candidate/paid-media-architecture`  
Frozen implementation/evaluation target: `bf81ec779dc43a94a72f9752209c6b82ef47e437`

## 1. Role

Act as an **INDEPENDENT ADVERSARIAL RUNTIME REVIEWER** for the Paid Media Architecture candidate in Marketing Practitioner.

Do not modify the repository. Do not defend the candidate. Do not reward the amount of research, the existence of tests, the candidate's 20/20 self-result, commit count, or branch mergeability.

Your job is to find consequential failures that the candidate-side theory freeze, implementation design, self-review, mechanical verification, or targeted runtime cases may have missed.

## 2. Frozen target rule

The implementation/evaluation target is frozen at:

```text
bf81ec779dc43a94a72f9752209c6b82ef47e437
```

Review the implementation and evaluation evidence at that commit.

The targeted adjudication and this review brief are intentionally committed **after** the frozen target. They may explain the intended review boundary, but they are not retroactive implementation evidence. Do not use later candidate changes to rescue a defect in the frozen target.

If a later commit corrects a problem you find, the problem still counts against the frozen target.

## 3. Files to inspect

Start with the governing controller:

```text
skills/marketing-practitioner/SKILL.md
```

Then inspect only the material candidate files needed for this review:

```text
research/paid-media-architecture/01-theory-freeze.md
research/paid-media-architecture/02-implementation-design.md
research/paid-media-architecture/03-implementation-self-review.md
research/paid-media-architecture/04-mechanical-verification.md

skills/marketing-practitioner/handbook/14-paid-media-architecture.md
skills/marketing-practitioner/references/paid-media-evidence.md
skills/marketing-practitioner/routing-index.json
skills/marketing-practitioner/handbook/README.md
skills/marketing-practitioner/scripts/get-knowledge.py
skills/marketing-practitioner/scripts/test-knowledge-routing.py

evals/paid-media-architecture-adversarial-cases.md
evals/paid-media-architecture-runtime-smoke.md
```

Read Chapters 01/02, 04, 05, 08, 09, 10, 11, and 13 only where necessary to adjudicate an owner-boundary claim.

Do not broaden the task into a general repository or marketing-media review.

## 4. Frozen theory to attack

The candidate claims Paid Media is a **bounded specialist layer** over the existing Chapter 08 grammar.

Frozen primary unit:

```text
PAID MEDIA DECISION
```

Frozen decision families:

```text
1. OBJECTIVE / DECISION VALUE
2. CONTROL / AUTHORITY ENVELOPE
3. ALLOCATION / REALIZATION STATE
4. OBSERVATION / FEEDBACK
```

The candidate explicitly rejects:

```text
new shared primitive
new controller job
campaign ontology
auction ontology
targeting ontology
learning ontology
feedback ontology
exposure ontology
universal media funnel
universal attribution model
universal media optimizer
provider-specific permanent Ads ontologies
```

## 5. Activation-boundary attack

The specialist claims:

```text
PAID RELATIONSHIP
≠ PAID MEDIA DELIVERY

SPONSORED CONTENT
≠ PAID AMPLIFICATION
```

Try to break this boundary.

At minimum mutate cases involving:

- a creator paid to produce/publish content with no bought distribution;
- creator/partnership content later amplified with paid budget;
- affiliate commission or performance compensation without media buying;
- agency/copy/creative production fees;
- publisher sponsorship packages that combine content production and guaranteed media;
- retail-media funded placements;
- ordinary ad-copy transformations where delivery mechanics cannot change the answer.

A failure exists if payment alone activates Paid Media, or if real paid mediated exposure is missed because it does not look like a conventional campaign.

## 6. Objective / optimization attacks

Attempt to construct realistic cases where the candidate collapses:

```text
BUSINESS VALUE / OUTCOME
vs MEDIA JOB
vs PLATFORM OBJECTIVE
vs OPTIMIZATION SIGNAL / EVENT
```

Pressure situations where:

- the platform improves a local event while downstream business value worsens;
- reported conversions include events not used for optimization;
- one event is used for optimization and another for billing;
- value/quality weights differ from raw conversion counts;
- the same dashboard label changes meaning after goal/measurement configuration changes;
- authoritative margin, capacity, inventory, or operational guardrails make a locally efficient campaign undesirable.

Check that Paid Media does not silently steal causal/incremental business-value questions from Chapter 05.

## 7. Control / authority attacks

Attack whether the candidate can preserve materially different control semantics.

At minimum pressure:

```text
HARD CONSTRAINT
vs SOFT SIGNAL / SUGGESTION

CONTROL TYPE
vs CONTROL PRECEDENCE

ADVERTISER AUTHORIZATION
vs PLATFORM EXECUTION
```

Construct conflicts among:

- audience control vs audience suggestion/expansion;
- frequency cap vs guaranteed-delivery obligation;
- advertiser placement restriction vs automatic placement permission;
- budget/cost/return target vs delivery objective;
- creative/destination authorization vs generated/selected execution;
- policy or account eligibility vs advertiser preference;
- contractual/reserved obligations vs campaign-level controls.

Do not accept a control taxonomy merely because the labels exist. The question is whether the implementation produces the right decision when controls conflict.

## 8. Allocation / realization attacks

The candidate claims Paid Media is not auction-only.

Attack across:

```text
open auction
private / negotiated marketplace
fixed-price inventory
reserved / guaranteed inventory
predictive / adaptive platform allocation
shared / portfolio budget allocation
retail-media sponsored placements
creator paid amplification
DOOH / location/time-based delivery
```

Pressure these distinctions:

```text
CAMPAIGN
vs RESOURCE / OPTIMIZATION BOUNDARY

BUDGET
vs ALLOCATION POLICY
vs PACING
vs BID STRATEGY
vs EXECUTED BID
vs ACTUAL SPEND

ELIGIBLE
vs CONSIDERED
vs COMPETITIVE
vs SELECTED
vs DELIVERED / RENDERED

ADVERTISER SPECIFICATION
vs PLATFORM-HELD STATE
vs PLATFORM EXECUTION
```

A candidate failure exists if a non-auction buy is forced into bid competitiveness, if a campaign container is treated as the real resource boundary when a shared/portfolio/deal boundary controls allocation, or if high-level advertiser settings are treated as the actual execution instance.

## 9. History / learning-state attack

The candidate treats learning/adaptation as:

```text
PLATFORM / MEDIATION STATE
+
HISTORY / STATE TRANSITION
```

rather than a new primitive.

Construct cases where two campaigns have identical current displayed metrics/settings but different recent edits, signal histories, or stabilization states and therefore require different actions.

Determine whether the existing grammar plus Paid Media semantics can distinguish them without introducing a new shared learning-state primitive.

Do not recommend a primitive merely because providers expose a `Learning` UI label.

## 10. Exposure / identity / measurement attacks

Attack:

```text
DELIVERED / RENDERED
vs OPPORTUNITY TO SEE
vs LIKELY SEEN
vs VERIFIED HUMAN ATTENTION
```

and:

```text
REPORTED REACH
vs EXACT UNIQUE HUMANS

REPORTED FREQUENCY
vs EXACT EXPOSURE HISTORY OF EVERY HUMAN
```

Use cases with:

- device/household/identity uncertainty;
- modeled reach/frequency;
- DOOH aggregate exposure;
- shared-device or privacy-restricted measurement;
- delayed or partial telemetry;
- placement/render logs without verified attention.

A correct candidate should preserve the observation unit, identity basis, modeling, coverage, and uncertainty only where they change the decision.

## 11. Observation / billing / attribution / feedback attacks

Pressure the candidate's strongest claimed distinction:

```text
DELIVERY EVENT
≠ OBSERVATION
≠ BILLING EVENT
≠ ATTRIBUTED OUTCOME
≠ OPTIMIZATION-ELIGIBLE SIGNAL
≠ OPTIMIZATION FEEDBACK
≠ CAUSAL EFFECT
```

At minimum construct cases where:

- a conversion remains in reporting but is excluded from bidding/optimization;
- attribution settings change what is credited and also alter optimization signal availability;
- billing is impression-based while optimization is click/conversion-based;
- delayed conversions make recent periods immature;
- imported/offline events are visible but have different optimization eligibility;
- modeled/estimated events appear in reporting;
- a platform-attributed result exists with no valid causal design.

Check whether the candidate knows when observation is only reporting evidence and when it participates in future allocation.

## 12. Owner-boundary attacks

The specialist is only valid if it remains bounded.

### Chapter 01 / 02 — customer / segment / demand

Attack whether platform targeting or reached-audience telemetry silently redefines the target customer or market.

### Chapter 04 — message / claim / proof

Attack cases where weak paid performance triggers creative rewriting without evidence that message/creative is the bottleneck.

### Chapter 05 — diagnosis / causality / incrementality

Especially performance changes with simultaneous budget, bid, audience, measurement, creative, market, or product changes. The candidate should not choose a paid lever before causal diagnosis has localized the mechanism when cause is genuinely open.

### Chapter 08 — shared platform/content grammar

Determine whether Paid Media adds specialist semantics without duplicating/replacing the parent object/representation/audience/edge/mediation/observation model.

### Chapter 09 — commerce identity

Attack retail-media cases involving variant/listing/offer/product identity where paid eligibility differs across commerce objects.

### Chapter 10 — Commercial Design

Attack whether media procurement/pricing/deal terms are incorrectly treated as customer-facing Commercial Design, or vice versa.

### Chapter 11 — landing page

Attack destination-selection cases where the delivery system selects an authorized URL but the open decision is actually downstream page architecture.

### Chapter 13 — Search & Discovery

Attack paid search / sponsored discovery cases where generic retrieval/ranking language could collapse organic discovery and paid economic allocation into one owner.

## 13. Fast-path attack

Try ordinary tasks containing paid-media nouns that should **not** activate Chapter 14.

Examples to mutate:

```text
shorten an approved ad headline
rewrite supplied ad body without changing meaning
format an approved campaign status update
summarize supplied CPC/CPA numbers without interpreting cause
translate approved ad copy
```

A failure exists if `Facebook Ads`, `Google Ads`, `TikTok Ads`, `campaign`, `CPC`, `CPA`, `ROAS`, `creative`, or similar nouns cause unnecessary deep routing when paid-delivery mechanics cannot change the answer.

## 14. Architecture-reopen burden

Do **not** invent a new primitive because a provider exposes another campaign object, bidding state, audience type, learning label, attribution setting, or auction stage.

A shared-architecture failure requires a concrete witness of this form:

> Two materially different paid-media states require different correct actions, but the existing shared grammar (`actor/source`, `object`, `representation`, `audience state`, typed relationship/access/delivery edge, `interaction act`, `platform/mediation state`, `observation record`, plus provenance/scope/history) cannot distinguish them without material distortion.

If you cannot construct such a witness, do not recommend reopening Chapter 08 or adding a shared primitive.

A repeated routing/owner defect may justify a local controller/Chapter 14/routing correction without architecture reopening.

## 15. Current-authority discipline

Paid-media platform behavior changes frequently.

Check that the candidate:

- treats current objectives, bidding products, auction/deal mechanics, audience controls, placement behavior, learning-state definitions, billing, attribution windows, measurement, policy, and creative automation as JIT authoritative dependencies;
- does not turn current Meta/Google/TikTok/LinkedIn behavior into timeless primitives;
- does not transfer one provider/product/transaction-type rule into another without support;
- preserves evidence `Supports` / `Does not support` boundaries;
- fails closed to `UNKNOWN` when hidden execution state cannot be observed.

Do not grade the candidate down merely for refusing to claim hidden provider mechanics.

## 16. Mechanical evidence limitation

The candidate mechanical report explicitly states that the full checked-out routing smoke script was **not executed**.

Direct structural verification reports:

```text
candidate lineage / bounded diff scope        PASS
7 paid-media route bindings                    PASS
7 exact routed Chapter 14 headings             PASS
PM03 evidence path/heading                     PASS
routing-test source wiring                     PASS
controller integration / version preservation  PASS
```

A sandbox checkout was attempted but failed before execution because `github.com` could not be resolved.

The source currently labels the intended complete suite as:

```text
57 routing-mechanics smoke checks
```

Do **not** silently upgrade this to `57/57 PASS`.

If the lack of executed mechanical regression creates consequential uncertainty, report it at the mechanical/evaluation scope rather than relabeling it as a semantic architecture failure.

## 17. Targeted evaluation evidence

The candidate-side runtime walkthrough reports:

```text
20 PASS
0 PARTIAL
0 FAIL
```

Do not inherit those verdicts. Re-run/reason through the cases adversarially and mutate them where useful.

The candidate-side 20/20 is evidence to attack, not a review conclusion.

## 18. Review questions

Return findings that answer:

1. Does Paid Media have a real bounded decision surface distinct from content, discovery, commerce, commercial design, and causality?
2. Does the four-family model preserve the material states required by realistic paid-delivery decisions?
3. Is the activation boundary `paid relationship ≠ paid-media delivery` operationally adequate?
4. Does the implementation preserve the fast path?
5. Does it preserve ownership of Chapters 01/02, 04, 05, 08, 09, 10, 11, and 13?
6. Can it distinguish business value, platform optimization, billing, attribution, and causal effect?
7. Can it distinguish hard controls, soft signals, authorization, contractual obligations, and precedence without a new control primitive?
8. Can it handle auction and non-auction buying without forcing one universal media pipeline?
9. Can it preserve resource/allocation boundaries beyond the campaign container?
10. Can it represent learning/adaptive state through existing mediation state + history without material distortion?
11. Are exposure/reach/frequency claims appropriately scoped to observation and modeling?
12. Does any concrete irreducible failure require reopening shared grammar?
13. Does any local implementation/routing/evaluation defect require correction before release?
14. Are the candidate's mechanical and runtime evaluation claims accurately scoped?

## 19. Finding format

For every `PARTIAL` or `FAIL`, provide:

```text
CASE / FAILURE
→ concrete prompt or state pair

EXPECTED CORRECT DECISION
→ what should happen

OBSERVED / IMPLIED CANDIDATE FAILURE
→ what the frozen target gets wrong

DECISION CONSEQUENCE
→ why the distinction matters

OWNER
→ Paid Media / Ch01-02 / Ch04 / Ch05 / Ch08 / Ch09 / Ch10 / Ch11 / Ch13 / shared grammar

MINIMAL CORRECTION
→ local correction or architecture reopen
```

Do not recommend broad rewriting when a smaller correction suffices.

## 20. Permitted final verdicts

Return **exactly one** of these four verdicts:

```text
PROCEED TO RELEASE PREPARATION

PROCEED AFTER LOCAL CORRECTIONS

HOLD — MATERIAL IMPLEMENTATION / EVALUATION DEFECT

REOPEN SHARED ARCHITECTURE
```

Use `REOPEN SHARED ARCHITECTURE` only if you produce the irreducible representation-failure witness defined above.

## 21. Review integrity

Do not modify the repository.

Do not inspect later candidate changes as implementation evidence.

Do not infer quality from PR status, commit count, code volume, self-test count, or candidate confidence.

The target of the review is the frozen implementation/evaluation state:

```text
bf81ec779dc43a94a72f9752209c6b82ef47e437
```

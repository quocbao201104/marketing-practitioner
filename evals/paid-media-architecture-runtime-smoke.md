# Paid Media Architecture — Targeted Runtime Walkthrough

Status: **CANDIDATE TARGETED EVALUATION**  
Date: 2026-08-25  
Evaluation contract: `evals/paid-media-architecture-adversarial-cases.md`  
Candidate semantic implementation head: `f4f2f36abc6ed5b9399524d6c4fffd4689476c7c`

## Method

Each P01–P20 case was walked through against the candidate `SKILL.md` controller plus the smallest material `paid-media.*` / existing-owner route. The purpose was to test runtime decision behavior, not provider-trivia recall.

Scoring:

```text
PASS
PARTIAL
FAIL
```

A case passes only if the candidate preserves the decision-relevant distinction and owner boundary without adding unnecessary architecture.

---

## P01 — Fast-path ad-headline transformation

**Runtime path**

```text
WRITE
→ resolved claim supplied
→ no substantive paid-delivery decision
→ fast path
```

**Task output**

```text
Debug AI workflows pre-failure
```

30 characters. No campaign/bid/audience architecture reopened.

**Verdict: PASS**

---

## P02 — Paid creator sponsorship is not automatically paid-media delivery

**Runtime path**

```text
paid creator relationship
→ no bought/boosted distribution
→ do not activate Paid Media by payment alone
→ Chapter 04 / Chapter 08 / current disclosure requirements as needed
```

**Task output**

The creator fee creates a paid relationship, but not automatically a paid-media delivery decision. Because no additional distribution is being bought or allocated, creator/source/message/content-environment and applicable disclosure requirements remain the relevant owners.

**Verdict: PASS**

---

## P03 — Creator content plus paid amplification

**Runtime path**

```text
creator post/message resolved
→ economic resource now amplifies mediated exposure
→ paid-media.core / control / allocation as needed
```

**Task output**

A new Paid Media layer opens for the amplification: authorization of the existing creator representation, paid audience/inventory controls, resource allocation, delivery, and observation. The creator's approved message stays frozen unless the paid representation materially changes it.

**Verdict: PASS**

---

## P04 — Business value vs optimization event

**Runtime path**

```text
DECIDE / DIAGNOSE
→ paid-media.objective
→ Chapter 05 if causal business impact is required
```

**Task output**

No. Add-to-Cart volume improving does not establish that the campaign improved against the business goal of profitable first-time purchases. The platform is optimizing a local event whose downstream purchase quality worsened. Without causal evidence, do not claim incremental business improvement.

**Verdict: PASS**

---

## P05 — Reported conversion vs optimization-eligible signal

**Runtime path**

```text
paid-media.objective
+ paid-media.observation
```

**Task output**

No. Keep both actions in reporting if that is how the platform reports them, but do not describe both as bidding signals unless the current goal configuration makes both optimization-eligible. Reported and optimization-eligible are different roles.

**Verdict: PASS**

---

## P06 — Audience suggestion vs enforced control

**Runtime path**

```text
paid-media.control
```

**Task output**

Not necessarily. A baseline audience control and an audience suggestion have different semantics. If the suggestion permits expansion, reaching people outside the suggested demographic is not by itself a targeting violation. Verify which input is enforced, which is advisory, and what population was actually eligible/reached.

**Verdict: PASS**

---

## P07 — Budget vs bid vs spend

**Runtime path**

```text
paid-media.control
→ paid-media.allocation
```

**Task output**

Do not increase the bid from underspend alone. The budget is unchanged, the bid is automated, and eligible opportunity volume fell. First localize eligibility/opportunity volume, allocation/pacing state, and any other constraints; budget, bid, and actual spend are not interchangeable.

**Verdict: PASS**

---

## P08 — Campaign container vs portfolio/shared allocation boundary

**Runtime path**

```text
paid-media.control
→ paid-media.allocation
```

**Task output**

No. The displayed campaign budget does not establish an independent resource boundary when the campaign participates in shared/portfolio allocation. Diagnose the shared allocation scope before reasoning from Campaign A in isolation.

**Verdict: PASS**

---

## P09 — Guaranteed inventory breaks auction-only reasoning

**Runtime path**

```text
paid-media.allocation
```

**Task output**

Treat this as reserved/guaranteed allocation, not an open-auction problem. Check the contracted inventory/volume, schedule, creative authorization/assignment, delivery state, and resulting observations. Bid competitiveness is not the governing mechanism for the reserved volume described.

**Verdict: PASS**

---

## P10 — Control type vs control precedence

**Runtime path**

```text
paid-media.control
```

**Task output**

No. Exceeding the apparent cap does not by itself prove a technical cap failure. In the supplied guaranteed-inventory regime, the provider states that reservation delivery obligations can take precedence over the campaign-level cap. Preserve that rule only within its documented scope.

**Verdict: PASS**

---

## P11 — Learning/adaptive state after a material edit

**Runtime path**

```text
DIAGNOSE
→ Chapter 05 for cause
→ paid-media.allocation for current mediation/history state
```

**Task output**

No. Creative fatigue is not established. The volatility begins immediately after a material bid/audience change and the provider documents recalibration/learning after such edits. Treat that as a current mediation state plus recent transition, not as evidence that the unchanged creative became weak.

**Verdict: PASS**

---

## P12 — Weak delivery without blaming creative

**Runtime path**

```text
DIAGNOSE
→ Chapter 05
→ paid-media.control / allocation
→ Chapter 04 only if creative becomes implicated
```

**Task output**

I would not write replacement ads as the presumed fix yet. The decline coincides with a tighter audience constraint and changed inventory eligibility while the creative and offer are unchanged. First discriminate the paid opportunity/control/allocation change; rewrite the creative only if evidence later localizes the problem there.

**Verdict: PASS**

---

## P13 — Advertiser specification vs platform execution

**Runtime path**

```text
paid-media.control
→ paid-media.allocation
```

**Task output**

No. The advertiser supplied an authorized envelope: creative pool, audience signal, destination set, and automatic-placement permission. The platform then produced a particular execution instance — placement, creative combination, destination, and bid. Authorization/specification and executed delivery are different states.

**Verdict: PASS**

---

## P14 — Rendered does not mean human attention

**Runtime path**

```text
paid-media.allocation
→ paid-media.observation
```

**Task output**

No. A successful render plus Opportunity-to-See measurement does not justify saying everyone counted actually saw the ad. Preserve rendered delivery, OTS, likely exposure, and verified attention as separate evidence levels.

**Verdict: PASS**

---

## P15 — Reach/frequency with modeled identity

**Runtime path**

```text
paid-media.observation
```

**Task output**

No. `3.1` is an aggregate/model-dependent frequency metric under the described identity limitations; it is not a deterministic statement that every individual human had exactly 3.1 exposures. Retain the identity basis, modeling, aggregation, and coverage limits.

**Verdict: PASS**

---

## P16 — Billing event vs optimization event

**Runtime path**

```text
paid-media.objective
+ paid-media.observation
```

**Task output**

No. One campaign can optimize landing-page clicks while being charged on impressions. Campaign membership does not make optimization and billing the same event role.

**Verdict: PASS**

---

## P17 — Attributed conversion vs incremental effect

**Runtime path**

```text
paid-media.observation
→ Chapter 05
```

**Task output**

The causal number is unknown from these facts. The platform attributed 1,000 purchases, but no valid counterfactual design establishes how many would not have happened without the ads. Attribution is not incrementality.

**Verdict: PASS**

---

## P18 — Reported conversion excluded from optimization feedback

**Runtime path**

```text
paid-media.observation
```

**Task output**

No. Conversions can remain visible in reporting while the incident period is excluded from Smart Bidding inputs. Separate what is reported from what is optimization-eligible and actually fed into future delivery; preserve the exclusion period and conversion maturity where material.

**Verdict: PASS**

---

## P19 — Retail media must preserve Chapter 09 product identity

**Runtime path**

```text
Chapter 09 / commerce identity first
→ paid-media.control / allocation for sponsored delivery
```

**Task output**

No. Keep the two variants distinct because their eligibility state differs. Chapter 09 owns product/variant/listing identity; Paid Media then reasons about the eligible variant's sponsored opportunity/allocation state. Adequate bid/budget does not erase a variant-level eligibility failure.

**Verdict: PASS**

---

## P20 — Generic discovery vs paid economic allocation

**Runtime path**

```text
organic discovery state
→ Chapter 13 if material

paid placement state
→ paid-media.control / allocation
```

**Task output**

No. Organic surfacing and paid delivery can share discovery-like selection language, but the paid placement also depends on economic resource, bid/budget controls, buying/allocation state, and paid delivery semantics. Use Chapter 13 for generic discovery and Paid Media for the paid economic-allocation layer rather than flattening them together.

**Verdict: PASS**

---

## Negative-space check

The walkthrough did not require:

```text
new shared primitive
new controller job
campaign ontology
auction ontology
targeting ontology
learning ontology
feedback ontology
universal attribution model
provider-specific guarantee
```

## Result

```text
PASS      20
PARTIAL    0
FAIL       0
```

The candidate preserves the fast path and owner boundaries while supplying the missing paid-control/allocation/feedback semantics.

## Targeted runtime verdict

> **20 PASS / 0 PARTIAL / 0 FAIL — PROCEED TO TARGETED ADJUDICATION.**

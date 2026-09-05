# Brand Identity and Visual Systems — Independent Adversarial Runtime Review Brief

Status: **FROZEN REVIEW CONTRACT**  
Repository: `https://github.com/quocbao201104/marketing-practitioner`  
Candidate PR: `https://github.com/quocbao201104/marketing-practitioner/pull/33`  
Candidate branch: `candidate/brand-identity-visual-systems`  
Frozen implementation/evaluation target: `544b33a823c0b19017b274773495a8af62a2cf44`

## 1. Role

Act as an **INDEPENDENT ADVERSARIAL RUNTIME REVIEWER** for the Brand Identity and Visual Systems candidate in Marketing Practitioner.

Do not modify the repository. Do not defend the candidate. Do not reward research volume, 20/20 author walkthrough results, CI success, PR mergeability, or the attractiveness/usefulness of the motivating logo workflow.

Your job is to find consequential activation, routing, ownership, evidence, state-preservation, or decision failures that the candidate-side theory/review/design/self-evaluation may have missed.

Do not broaden the review into general branding, graphic design, UI, naming, art direction, trademark law, or a new marketing ontology.

---

## 2. Frozen target rule

Review exactly:

```text
544b33a823c0b19017b274773495a8af62a2cf44
```

Later commits contain freeze/review instructions or possible later repairs. They are **not** frozen-candidate evidence.

If a later commit fixes a defect you identify, the defect still counts against the target above.

The theory that authorized implementation was independently post-repair verified at:

```text
2381f11eabbfa7c0e8be3f500befb86a5b696c36
```

with:

```text
POST_REPAIR_PASS
READY_FOR_BOUNDED_RUNTIME_DESIGN
```

Your task is runtime implementation/evaluation review, not a third open-ended theory review. Reopen theory/shared architecture only if the implementation reveals an irreducible failure witness.

---

## 3. Files to inspect

Start with the runtime controller:

```text
skills/marketing-practitioner/SKILL.md
```

Then inspect the material candidate files at the frozen target:

```text
skills/marketing-practitioner/handbook/15-brand-identity-and-visual-systems.md
skills/marketing-practitioner/references/brand-identity-evidence.md
skills/marketing-practitioner/routing-index.json
skills/marketing-practitioner/handbook/README.md
skills/marketing-practitioner/scripts/get-knowledge.py
skills/marketing-practitioner/scripts/test-knowledge-routing.py

evals/brand-identity-and-visual-systems-adversarial-cases.md
evals/brand-identity-and-visual-systems-runtime-smoke.md

research/brand-identity-and-visual-systems/13-post-repair-theory-freeze-candidate.md
research/brand-identity-and-visual-systems/16-post-repair-verification-result.md
research/brand-identity-and-visual-systems/17-bounded-runtime-design.md
research/brand-identity-and-visual-systems/18-implementation-self-review.md
research/brand-identity-and-visual-systems/19-mechanical-verification.md
research/brand-identity-and-visual-systems/20-targeted-evaluation-adjudication.md
```

Read Chapters 00/01/03/04/05/07/11 only where needed to adjudicate an owner-boundary or handoff claim.

Do not review later commits as candidate evidence.

---

## 4. Candidate claim to attack

The runtime claims a narrow specialist owner:

```text
RESOLVED BRAND / MARKET STATE
+ OPEN BRAND-IDENTIFYING VISUAL DECISION
+ RELEVANT EXISTING-ASSET / DEPLOYMENT EVIDENCE
→ BOUNDED IDENTITY DECISION
```

It explicitly rejects a general visual-design owner.

Core hard stop:

```text
BRAND-IDENTIFYING CUE / RELATIONSHIP / IDENTITY DECISION IS OPEN
→ Brand Identity may remain active

IDENTITY DECISION IS FIXED
+ only production manipulation / application execution remains
→ ordinary design/tool execution or downstream owner
```

The candidate exposes exactly these JIT routes:

```text
brand-identity.core
brand-identity.equity
brand-identity.exploration
brand-identity.refinement
brand-identity.evaluation
brand-identity.system
brand-identity.handoffs
brand-identity.decision-record
brand-identity.invariants
```

Try to break this shape before accepting it.

---

## 5. Activation-boundary attack

The candidate says visual nouns are not activation authority.

Pressure both false positives and false negatives.

### False-positive cases

Mutate tasks such as:

```text
export approved logo as SVG/PNG
resize an approved asset
routine Bezier cleanup with no identity consequence
place approved logo in a landing-page hero
create a campaign illustration using approved brand assets
apply approved colors to a social asset
implement an approved UI component style
summarize supplied logo guidelines
translate approved brand-guideline text
```

A defect exists if `logo`, `branding`, `font`, `color`, `SVG`, `icon`, or `design` mechanically causes deep identity routing when identity state cannot change the answer.

### False-negative cases

Mutate tasks where the user does not say `logo` or `brand identity` explicitly, for example:

```text
"Should we retire the orange shape customers recognize?"
"This app symbol stops reading as itself at small size."
"Which persistent visual cue should survive the rebrand?"
"We need a reusable visual signature across product surfaces."
```

A defect exists if the controller misses a materially open brand-identifying asset decision because the expected noun is absent.

---

## 6. Fast-path / JIT-route attack

The candidate claims `brand-identity.core` is not a mandatory hop and narrow tasks can enter the smallest route directly.

Pressure whether:

- an equity-only redesign question can go directly to `brand-identity.equity`;
- an aperture/identifying-cue issue can go directly to `refinement` / `evaluation`;
- formal perceptual evidence can enter `evaluation` then hand off to Chapter 00/01;
- a verified-master relationship can enter `system` without exploration;
- a pure export can exit without any deep route;
- a new-identity task with resolved strategy can use `exploration` without rebuilding positioning;
- unresolved positioning correctly blocks/feeds identity rather than being silently decided by visual form.

A local route correction is preferred over a new route family unless you construct a repeated irreducible failure.

---

## 7. Existing-equity / redesign attacks

Pressure:

```text
UNMEASURED EQUITY
!= ZERO
!= PROVEN
```

Construct realistic cases with:

- eight years of use but no buyer-memory study;
- measured strong attribution but internal desire for novelty;
- measured weak linkage but high operational switching cost;
- one asset (color/symbol/wordmark feature) with stronger learned linkage than the rest;
- a small demonstrated defect that can be repaired without reset;
- a fundamental strategic/product change that may justify greater discontinuity;
- evidence unavailable before a consequential irreversible launch.

Check whether the runtime can choose among preserve/evolve/replace without falling into:

```text
old = preserve forever
unmeasured = zero
measured linkage = never redesign
new = better
smallest change = universal command
```

Operational cost, legal status, product capability, and organizational authority must not be invented by the marketing owner.

---

## 8. Distinctiveness / category-overlap attacks

The candidate freezes:

```text
CANDIDATE VISUAL DIFFERENCE
!= LEARNED BRAND-MEMORY STRENGTH
!= LEGAL DISTINCTIVENESS / CLEARANCE
```

and:

```text
OBSERVED CATEGORY / COMPETITOR CUE OVERLAP
!= INFERRED SCREENING RISK
!= MEASURED BUYER-MEMORY COMPETITION
```

Try cases where:

- most sampled competitors use the same category symbol;
- a candidate is visually unique but brand-new;
- a common category cue is strongly linked to one incumbent in buyer memory;
- a visually descriptive mark performs well in category comprehension;
- a candidate appears unlike competitors but is hard to attribute to any source;
- team intuition conflicts with buyer association data.

A defect exists if competitor prevalence becomes buyer-memory evidence, if visual novelty becomes Fame/Uniqueness, or if learned memory strength becomes legal clearance.

---

## 9. Exploration / refinement / folklore attacks

The candidate keeps:

```text
EXPLORATION != REFINEMENT
```

but treats concept territories, form families, and controlled mutation as optional `PROJECT SYNTHESIS`.

Pressure whether runtime prose accidentally makes them mandatory.

Try workflows using:

- human sketches;
- deterministic vector construction;
- typographic-only exploration;
- one strong supplied direction with no need for broad exploration;
- many simultaneous geometric changes made by a competent designer while identity state remains controlled;
- image-generation iterations prone to drift.

Reject any hidden requirements such as:

```text
exactly three concepts
always use a competitor audit
always use moodboards
always change one variable
simple = better
minimal = modern
round = friendly
angular = premium
abstract = distinctive
literal = weak
```

The question is whether the runtime preserves state and decision quality, not whether it enforces one design process.

---

## 10. Perceptual-evidence / research-owner attack

The candidate says Brand Identity owns the **identity estimand/failure condition**, while existing research/experiment owners govern formal methodology and inference.

Pressure cases involving:

- repeated informal user misreading;
- a formal misattribution-rate comparison;
- unaided recognition or correct linkage;
- direct deterministic small-size failure;
- a survey with an unrepresentative convenience sample;
- a randomized exposure test whose causal interpretation matters;
- buyer-memory evidence from the wrong segment or market.

A defect exists if Brand Identity silently designs/validates research methodology, turns scoped reactions into population claims, or forces Chapter 05 onto directly inspectable production-state failures.

---

## 11. System-commit / production-authority attack

The candidate freezes:

```text
EXPLORATORY / PREVIEW REPRESENTATION
!= VERIFIED PRODUCTION MASTER
```

Pressure:

- generated raster preview;
- human sketch;
- traced vector;
- exported SVG with unverified geometry;
- vector generated by a tool that is actually verified;
- unlicensed typeface in a selected wordmark;
- multiple lockups with unclear master/variant relationship;
- a fixed identity handed off to downstream page/UI work.

The runtime should not infer production authority from appearance alone, but should also not reject machine-generated output merely because a tool produced it.

Check that `brand-identity.system` does not become a DAM, design-token system, or generic production workflow.

---

## 12. Owner-boundary attacks

### Chapter 03 — positioning/value

Can visual metaphor silently decide unresolved category/frame/differentiation? It must not.

### Chapter 04 — message/copy/verbal state

Can a wordmark cause visual identity to own naming, wording, promise, or claim? It must not.

### Chapter 00/01 — research/evidence

Can formal buyer-memory/perception methodology remain outside Chapter 15 while the identity decision still specifies what evidence is needed?

### Chapter 05 — causality/experiments

Does Chapter 15 create its own experiment/causal framework? It must not.

### Chapter 07 — localization

Pressure:

```text
NEW MARKET != AUTOMATIC IDENTITY REDESIGN
```

but also verify that material scoped local meaning/script/legibility/regulatory evidence can reopen the affected identity dimension.

### Chapter 11 — landing-page architecture

Once identity is fixed, logo placement/size relative to page content remains Chapter 11 work.

### General design / UI / illustration

Once the persistent identifying decision is fixed, application-specific execution must exit the specialist.

### Legal / trademark expertise

A WIPO/EUIPO or image-similarity pre-flight may surface scoped conflict evidence but must not become clearance.

---

## 13. Evidence-status attack

Check whether the final runtime maintains the verified epistemic categories:

```text
EMPIRICAL / ACADEMIC
PROFESSIONAL PRACTICE
PROJECT SYNTHESIS
CONTEXTUAL HYPOTHESIS
```

Specifically attack whether:

- BV01/BV02 are stretched into deterministic aesthetic rules;
- BV03 becomes `never redesign`;
- BV04 becomes `always run a buyer study`;
- BV05 becomes national visual stereotypes;
- BV06/BV07 become legal advice;
- BV08's IBM numeric production guidance becomes universal size/clear-space rules;
- professional practice is presented as causal business-effect evidence;
- critique terms such as `formal coherence`, `semantic cliché density`, or `system extensibility` are presented as validated metrics without operationalization.

A source existing in the ledger does not make every adjacent runtime claim empirical.

---

## 14. Decision-record / stewardship attack

The candidate includes `brand-identity.decision-record`.

Test whether the record remains minimum sufficient rather than becoming:

```text
brand book schema
DAM database
design-token ontology
asset-management system
mandatory record for every visual edit
```

Check that it can preserve, when consequential:

```text
resolved strategic inputs used
existing asset state / evidence status
verified committed masters/relationships
scoped evaluation evidence
material uncertainty / handoffs
reopen condition
```

without forcing irrelevant fields into fast-path work.

---

## 15. Route-surface sufficiency / over-fragmentation

The candidate has nine routes.

Try to show that:

- two routes are actually indistinguishable and cause routing ambiguity;
- a material recurring decision has no route;
- `core`/`handoffs`/`invariants` duplicate controller prose enough to create conflicting authority;
- `system` absorbs production execution;
- `evaluation` absorbs research methodology;
- `equity` and `evaluation` create ambiguous ownership for category-overlap cases;
- a route named by artifact type would actually be necessary.

Do not request conceptual symmetry. Require a concrete decision failure before adding/merging routes.

A local routing correction is not a reason to reopen shared architecture.

---

## 16. Mechanical evidence review

The candidate reports actual GitHub Actions verification on semantic head `790ceefd309b787dcc5b5f3b0616250eb473df5f` and again successful verification on frozen head `544b33a823c0b19017b274773495a8af62a2cf44`.

The first recorded run includes:

```text
68 routing-mechanics smoke checks              PASS
261 routes / 233 evidence sources              PASS
138 Pressure Discovery unit tests              PASS
74 behavioral-harness unit tests               PASS
UTF-8 / artifact hygiene                       PASS
repository verification                        PASS
```

The external current Codex validator was not installed/discoverable and is correctly reported as `SKIP`.

Verify that the candidate does not overclaim what these checks establish.

They prove mechanical addressability/regression properties, not automatic live route use.

---

## 17. Candidate-side runtime evidence limitation

The author walkthrough reports:

```text
20 PASS
0 PARTIAL
0 FAIL
```

but explicitly labels:

```text
SKILL ACTIVATION                  UNVERIFIED
ROUTE REQUEST                     UNVERIFIED
ROUTE RESOURCE DELIVERY           UNVERIFIED
READ ORDER                        UNVERIFIED
LIVE MODEL COMPLIANCE             UNVERIFIED
```

Do not inherit the 20/20 verdicts.

Adversarially reason through or mutate the cases yourself.

Also adjudicate whether the absence of live activation/path evidence is:

- correctly scoped and acceptable before independent review;
- a bounded evaluation gap that should be closed before release;
- evidence of a concrete controller/routing defect;
- or, only with an irreducible witness, a reason to reopen architecture.

Do **not** silently upgrade static route addressability or author-selected route oracles into live path proof.

Do not run a broad behavioral benchmark merely for coverage. If you believe live evidence is required before release, specify the **smallest targeted activation/path check** that would discriminate the risk.

---

## 18. Architecture-reopen burden

Do not invent a new `BRAND`, `DESIGN`, or `IDENTITY` controller job or shared primitive merely because branding is broad.

A shared-architecture failure requires a concrete witness:

> Two materially different brand-identifying visual states require different correct actions, but the existing controller jobs, resolved-state mechanism, existing owner handoffs, and bounded `brand-identity.*` specialist routes cannot distinguish them without material distortion.

If you cannot construct that witness, keep any required correction local to Chapter 15, `SKILL.md`, routing, evidence, or evaluation.

Do not reopen architecture because one route name could be better.

---

## 19. Required review questions

Answer all of these:

1. Does the frozen candidate implement the independently verified theory without broadening into generic design?
2. Is activation based on an open persistent brand-identifying decision rather than visual nouns?
3. Does the pure-execution stop work in both obvious and ambiguous cases?
4. Can narrow tasks enter the smallest route without mandatory `core`/exploration?
5. Does resolved positioning/message/localization state stay frozen unless a genuine dependency reopens it?
6. Does redesign preserve the distinction between measured, unmeasured, and absent equity without `never redesign` folklore?
7. Does candidate difference remain separate from learned buyer-memory strength and legal status?
8. Does category/competitor overlap remain separate from measured buyer-memory competition?
9. Are concept territories/form families/controlled mutation optional synthesis rather than runtime law?
10. Does perceptual evaluation hand formal methodology/inference to existing research/experiment owners?
11. Does `system` preserve verified identity state without taking over generic production/DAM/UI work?
12. Are legal and localization boundaries properly scoped?
13. Does the evidence ledger preserve empirical/practice/synthesis/hypothesis boundaries?
14. Are the nine routes sufficient and non-pathological?
15. Are mechanical-verification claims accurate?
16. Is the author 20/20 semantic walkthrough appropriately limited?
17. Does lack of live activation/path proof require a bounded pre-release evaluation repair?
18. Does any concrete irreducible failure justify reopening shared architecture?

---

## 20. Finding format

For every `PARTIAL` or `FAIL`, provide:

```text
ID / CASE

SEVERITY
→ blocking / material-local / minor

FROZEN LOCATION
→ exact file / route / section

FAILURE CASE
→ concrete prompt or state pair

EXPECTED CORRECT DECISION
→ what should happen

OBSERVED / IMPLIED CANDIDATE FAILURE
→ what the frozen target gets wrong or cannot prove

DECISION CONSEQUENCE
→ why it matters

OWNER
→ Chapter 15 / SKILL / routing / evidence / evaluation / existing chapter / external dependency / shared architecture

SMALLEST CORRECTION
→ local correction, targeted evaluation addition, or architecture reopen
```

Do not manufacture findings merely to appear adversarial.

---

## 21. Permitted final verdicts

Return **exactly one**:

```text
PROCEED TO RELEASE PREPARATION

PROCEED AFTER LOCAL CORRECTIONS

HOLD — MATERIAL IMPLEMENTATION / EVALUATION DEFECT

REOPEN SHARED ARCHITECTURE
```

Use `REOPEN SHARED ARCHITECTURE` only if you construct the irreducible representation/ownership failure witness defined above.

A missing live activation/path check, by itself, is not automatically a shared-architecture defect. If consequential, classify it at the evaluation/runtime-local level and specify the smallest discriminating check.

---

## 22. Review integrity

Do not modify the repository.

Do not inspect later candidate changes as implementation evidence.

Do not use PR status, CI green state, commit count, self-review confidence, or 20/20 author walkthrough as substitutes for reasoning.

The exact implementation/evaluation target is:

```text
544b33a823c0b19017b274773495a8af62a2cf44
```

The review brief itself is committed after that target and is not candidate implementation evidence.
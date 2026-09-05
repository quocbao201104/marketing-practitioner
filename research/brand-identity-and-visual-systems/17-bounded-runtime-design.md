# Brand Identity and Visual Systems — Bounded Runtime Design

Status: **APPROVED FOR CANDIDATE IMPLEMENTATION**  
Design date: 2026-09-05  
Verified theory target: `2381f11eabbfa7c0e8be3f500befb86a5b696c36`  
Post-repair verification: `POST_REPAIR_PASS`  
Runtime-gate recommendation: `READY_FOR_BOUNDED_RUNTIME_DESIGN`  
Candidate branch: `candidate/brand-identity-visual-systems`

## 1. Design objective

Implement the verified Brand Identity specialist capability with the **smallest runtime surface that can govern brand-identifying visual asset realization and stewardship** without turning Marketing Practitioner into a graphic-design suite.

The runtime must preserve the verified owner:

```text
RESOLVED BRAND / MARKET STATE
+ OPEN BRAND-IDENTIFYING VISUAL DECISION
+ RELEVANT EXISTING-ASSET / DEPLOYMENT EVIDENCE
→ BOUNDED IDENTITY DECISION
```

The implementation must preserve these hard boundaries:

```text
POSITIONING / VALUE
!= BRAND-IDENTIFYING VISUAL ASSET REALIZATION / STEWARDSHIP
!= MESSAGE / COPY
```

```text
CANDIDATE VISUAL DIFFERENCE
!= LEARNED BRAND-MEMORY STRENGTH
!= LEGAL DISTINCTIVENESS / CLEARANCE
```

```text
IDENTITY STEWARDSHIP
!= GENERAL DESIGN EXECUTION
```

No new controller job, durable identity primitive, visual-design ontology, research methodology, legal subsystem, or country-specific identity pack is justified.

---

## 2. Runtime shape

Add one bounded specialist chapter:

```text
skills/marketing-practitioner/handbook/15-brand-identity-and-visual-systems.md
```

Add one scoped evidence ledger:

```text
skills/marketing-practitioner/references/brand-identity-evidence.md
```

Expose one JIT namespace:

```text
brand-identity.*
```

Update only the controller/navigation/routing surfaces necessary for reliable activation and deterministic JIT retrieval.

The runtime shape deliberately mirrors existing specialist architecture: one chapter, one evidence ledger, one logical namespace, targeted routing tests, and targeted adversarial cases. It does not add a second skill or a generic design subsystem.

---

## 3. Proposed logical routes

The runtime route set is intentionally smaller than the research field map.

```text
brand-identity.core
→ owner scope, activation boundary, resolved-state rule, pure-execution stop

brand-identity.equity
→ preserve / evolve / replace decisions;
  measured vs plausible-unmeasured equity;
  candidate difference vs learned buyer-memory strength;
  observed category overlap vs measured competition

brand-identity.exploration
→ genuinely open identity hypotheses under resolved strategic constraints;
  optional concept territories / form families as PROJECT SYNTHESIS;
  no mandatory concept count or aesthetic recipe

brand-identity.refinement
→ preserve selected identity/family state while an identifying cue or
  persistent relationship remains open; controlled mutation as optional synthesis;
  stop before mechanical production

brand-identity.evaluation
→ intended vs observed reading; deployment failure conditions;
  deterministic observation vs formal perceptual-research handoff;
  scoped candidate/category screening without buyer-memory overclaim

brand-identity.system
→ verified production masters; persistent reusable asset relationships;
  minimum sufficient variants/constraints; preview != production authority;
  stewardship without taking over downstream layout/UI/art direction

brand-identity.handoffs
→ owner boundaries with Chapters 00/01/03/04/05/07/11,
  ordinary design/tool execution, and external legal/rights expertise

brand-identity.decision-record
→ compact retained identity state and uncertainty for downstream reuse

brand-identity.invariants
→ anti-folklore distinctions and epistemic-status discipline
```

### Routes intentionally not created

Do **not** create:

```text
brand-identity.legal
brand-identity.trademark
brand-identity.localization
brand-identity.research
brand-identity.experiment
brand-identity.production
brand-identity.ui
brand-identity.art-direction
brand-identity.naming
brand-identity.brand-strategy
brand-identity.logo
brand-identity.color
brand-identity.typography
brand-identity.motion
```

Those nouns either belong to existing/external owners, represent execution rather than an open identity decision, or would fragment the JIT surface around artifact types instead of decision dependencies.

`concept territories` and `form families` also do not receive routes. They remain optional project synthesis inside `brand-identity.exploration`.

No `brand-identity.diagnosis` route is justified. Formal causal diagnosis remains Chapter 05; formal customer/perceptual research remains with the existing research/method owners.

---

## 4. Chapter structure

Use stable decision-oriented headings so routing remains independent of logo/style nouns:

```text
# 15 — Brand Identity and Visual Systems

## 1. Scope: realize and steward brand-identifying visual assets
## 2. Existing equity, candidate distinctiveness, and redesign
## 3. Exploration under resolved strategic constraints
## 4. Refinement while preserving selected identity state
## 5. Perceptual and deployment evaluation
## 6. System commit, verified masters, and stewardship
## 7. Owner boundaries and decision handoffs
## 8. Compact brand-identity decision record
## 9. Anti-folklore and evidence-status invariants
```

Route-to-heading bindings belong only in `routing-index.json`.

Do not add permanent top-level sections for:

```text
logo types
color psychology
typography personalities
visual trends
moodboards
brand archetypes
AI logo prompting
trademark law
country symbolism catalogs
UI design systems
```

Such material may be irrelevant, contextual, externally owned, or explicitly rejected as universal theory.

---

## 5. Controller integration

The controller already supplies the necessary jobs, resolved-state freezing, open-decision identification, dependency-first composition, and JIT loading. Do not add `BRAND`, `DESIGN`, or `IDENTITY` as a controller job.

### 5.1 Activation rule

Add one bounded operating-path rule to `SKILL.md`:

- activate Brand Identity only when a **persistent or reusable brand-identifying visual cue, asset relationship, preserve/evolve/replace choice, or identity-system commitment remains materially open** and specialist identity knowledge can change the current decision;
- do not activate merely because the prompt mentions `logo`, `branding`, `font`, `color`, `favicon`, `SVG`, `image`, `icon`, `design`, or another visual noun;
- if identity state is fixed and only mechanical production or application-specific execution remains, stop the identity path;
- enter the smallest exact `brand-identity.*` route when the open decision is already known rather than forcing `brand-identity.core` as a mandatory hop.

### 5.2 Upstream dependencies

Use Chapter 03 first only when target context, category/frame, relevant alternative, primary value/differentiation, or another positioning input is genuinely unresolved and can change the identity decision.

Use Chapter 04 only when wording, message, claim, proof, or naming-like audience-facing language is materially open. A wordmark's persistent visual form can belong to identity while the wording itself remains a message/name dependency.

Do not reopen upstream strategy merely because a new identity is being created.

### 5.3 Research / experiment dependency

When the identity decision requires a defensible population claim such as:

```text
Which candidate is misattributed least often by target buyers?
How strongly is this existing cue linked to the brand?
```

Brand Identity defines the decision-relevant estimand / failure condition and passes it to the existing research/method owner.

Use Chapter 00/01 for research-method/evidence questions and Chapter 05 when experiment design or causal inference is genuinely required.

Direct deterministic observations such as an identifying aperture closing in a required master at the actual deployment size do not require this handoff.

### 5.4 Localization dependency

Chapter 07 remains the localization owner.

```text
NEW MARKET
!= AUTOMATIC IDENTITY REDESIGN
```

Only material local evidence about meaning, legibility, script, symbolism, regulation, or deployment may reopen the affected identity dimension.

### 5.5 Downstream application dependency

When verified identity state is fixed:

- Chapter 11 owns landing-page visual allocation and page architecture;
- other downstream content/platform owners own application-specific composition;
- ordinary design/tool execution owns mechanical export, tracing, resizing, routine Bezier cleanup, or asset conversion;
- product/UI design remains outside this marketing owner unless an unresolved persistent brand-identifying cue itself is the decision.

### 5.6 Legal / rights dependency

Brand Identity may surface scoped search observations, possible conflicts, incomplete search scope, or a need for official/specialist clearance when consequential.

It must not claim:

```text
trademark safe
legally clear
guaranteed registrable
original / rights-owned merely because a generation/search succeeded
```

Legal judgment remains an authoritative external dependency.

### 5.7 Skill metadata

Update the skill description minimally so hosts can recognize relevant tasks, for example by adding `brand identity / visual systems` to the existing capability list.

Do not broaden the description to `graphic design`, `UI design`, `illustration`, or generic creative production.

---

## 6. Fast-path requirements

The implementation must preserve these routes without forcing a branding curriculum.

### F1 — Pure production

```text
"The identity master is approved. Export SVG and PNG sizes."
→ do not activate deep Brand Identity
→ ordinary production/tool execution
```

### F2 — Narrow identifying-cue refinement

```text
"Keep the approved mark. Its identifying opening closes at 16 px."
→ brand-identity.refinement
→ brand-identity.evaluation only if needed
→ brand-identity.system only if a revised master relationship is committed
```

Do not reopen positioning, category audit, or exploration.

### F3 — New brand, strategy resolved

```text
"Positioning is approved. Develop the visual identity."
→ brand-identity.exploration as needed
→ refinement / evaluation / system only when those decisions remain open
```

`brand-identity.core` may be read only when scope/boundary itself is unclear.

### F4 — Rebrand with uncertain equity

```text
"We used this symbol for eight years but never measured recognition. Replace it?"
→ brand-identity.equity
→ formal research handoff only when consequence/evidence need warrants it
```

Preserve:

```text
UNMEASURED != ZERO
UNMEASURED != PROVEN
```

### F5 — Competitor cue prevalence

```text
"Twenty cybersecurity brands use shields, so ours cannot be distinctive."
→ brand-identity.equity or evaluation
→ record observed overlap
→ do not infer measured buyer-memory competition, Fame, Uniqueness, or legal status
```

### F6 — Formal perceptual comparison

```text
"Which mark do Vietnamese SME buyers misidentify most often?"
→ Brand Identity defines misattribution estimand
→ Chapter 01 / method owner handles formal sampling/measurement/inference
→ Chapter 07 only if local realization itself changes the identity decision
```

### F7 — Downstream page application

```text
"Identity is approved. Place it correctly in the landing-page hero."
→ identity supplies master/constraints
→ Chapter 11 owns page allocation
```

### F8 — Legal pre-flight

```text
"WIPO search shows nothing similar. Is the logo safe?"
→ preserve searched scope
→ no legal-clearance claim
→ external official/specialist dependency when consequential
```

---

## 7. Runtime chapter content discipline

The handbook chapter should compress the verified theory rather than copy the research artifacts.

### Governing / durable content

Include compact forms of:

```text
open identity decision first
resolved upstream state stays frozen
redesign != reset
unmeasured != zero != proven
intended meaning != observed reading
observed category overlap != measured buyer-memory competition
candidate difference != learned asset strength != legal status
exploration != refinement
preview != verified production master
new market != automatic identity redesign
identity stewardship != general design execution
```

### Professional-practice content

May include bounded guidance for:

- verified master / variant relationships;
- persistent usage constraints;
- clear-space or reproduction principles when decision-relevant;
- minimum sufficient system documentation;
- small-size or reversed variants when the actual identity system requires them.

Do not claim these practices cause business lift by themselves.

### Project synthesis

May include:

- concept territories as an optional exploration device;
- form-family exploration;
- deliberate/controlled refinement when it makes state changes inspectable.

Mark or phrase them as optional practitioner methods rather than requirements.

### Contextual hypotheses

Visual predictions such as `rounder may read warmer` or `this symbol may collide with category cues` must remain hypotheses unless scoped evidence establishes more.

---

## 8. Evidence ledger design

Create:

```text
skills/marketing-practitioner/references/brand-identity-evidence.md
```

Use source IDs:

```text
BV01..BVxx
```

so they do not collide conceptually with the review finding IDs `BI-Txx`.

Every entry should include:

```text
Evidence status
Source
Scope / study or authority context
Supports
Does not support
```

The first ledger should pressure the verified distinctions, not maximize design-topic coverage.

Candidate initial source set:

```text
BV01 Henderson & Cote — selecting/modifying logos;
     conditional naturalness/harmony/elaborateness effects

BV02 Luffarelli et al. — logo descriptiveness;
     rejects literal/descriptive = universally bad

BV03 Walsh et al. — logo redesign × brand commitment;
     supports REDESIGN != RESET without implying NEVER REDESIGN

BV04 consumer-vs-marketer distinctive-asset assessment research;
     supports buyer-memory evidence != internal judgment and
     Fame/Uniqueness evidence discipline

BV05 cross-national logo evaluation research;
     supports shared + context-varying responses without country-first redesign

BV06 WIPO Global Brand Database / image-similarity search;
     supports bounded discovery/pre-flight, not legal clearance

BV07 EUIPO figurative/distinctiveness guidance;
     supports mark/goods-services context and legal dependency boundaries

BV08 authoritative professional identity-system / production guidance;
     supports master/variant/small-size/reversed stewardship as practice,
     not causal business-effect claims
```

If generative-image evidence is retained, it should support only a scoped present-tool limitation. The durable runtime invariant remains representation verification, not `AI output is invalid`.

Do not add trend articles, logo galleries, Pinterest/Dribbble popularity, or studio preference as evidence for governing aesthetic laws.

---

## 9. Compact decision record

`brand-identity.decision-record` should preserve only state needed for future identity continuity.

Candidate record:

```text
IDENTITY JOB / DECISION

RESOLVED STRATEGIC INPUTS USED
- only inputs that materially constrained this decision

EXISTING-ASSET STATE
- current asset(s)
- measured learned linkage, if any
- plausible but unmeasured equity, explicitly labeled
- known deployment defects

COMMITTED IDENTITY STATE
- verified master asset(s)
- persistent relationships / variants
- established color / typography roles only when actually resolved
- identity-changing constraints

EVALUATION STATE
- deterministic failures checked
- scoped observed perceptual evidence
- formal evidence source / scope when applicable

UNCERTAINTY / HANDOFFS
- buyer-memory unknowns
- legal/rights uncertainty
- local-realization dependencies
- downstream application constraints

REOPEN CONDITION
- what evidence or failure would justify reopening the committed identity decision
```

Do not turn this into a brand-book schema, DAM ontology, asset-management database, or design-token system.

---

## 10. Targeted adversarial evaluation design

Create one bounded case file during candidate implementation:

```text
evals/brand-identity-and-visual-systems-adversarial-cases.md
```

The evaluation should pressure **activation, path selection, state preservation, owner boundaries, and theory semantics**, not aesthetic quality.

Minimum case families:

```text
V01 approved master → SVG/PNG export only
V02 approved mark → identifying aperture failure at small size
V03 new identity with positioning already resolved
V04 new identity with positioning materially unresolved
V05 established asset with plausible but unmeasured equity
V06 measured strong asset linkage vs internal desire for full reset
V07 competitor/category cue prevalence without buyer-memory evidence
V08 candidate visual difference mistaken for learned distinctiveness
V09 intended concept story vs repeated scoped misreading
V10 formal target-buyer misattribution comparison
V11 deterministic deployment failure requiring no formal research
V12 WIPO/image search finds no obvious similar mark
V13 new market / Japan with no material local identity issue
V14 local evidence reveals a material unintended meaning
V15 approved identity → landing-page hero allocation
V16 approved identity → campaign illustration execution
V17 wordmark wording open vs visual wordmark form open
V18 raster/generated/sketch preview mistaken for production master
V19 adjective request: "make it premium / friendlier"
V20 one synthetic logo score used to hide incompatible trade-offs
```

Targeted adjudication should reject any implementation that:

- activates deep identity reasoning for pure export or routine mechanical work;
- reopens resolved positioning merely because a logo/identity noun appears;
- requires concept territories or form families on every creation task;
- treats competitor cue prevalence as buyer-memory competition;
- claims Fame/Uniqueness for a newly generated candidate without evidence;
- treats unmeasured equity as zero or as proven;
- resets an established identity merely because internal taste changed;
- turns a handful of reactions into a population claim;
- recreates research methodology inside Brand Identity;
- converts `premium`, `friendly`, `modern`, or similar adjectives into deterministic geometry;
- copies fixed pixel sizes or clear-space ratios from another brand as universal law;
- treats preview imagery as an authoritative production master without verification;
- turns legal pre-flight into clearance;
- localizes the identity merely because a country is mentioned;
- takes over landing-page allocation, UI styling, campaign illustration, or generic art direction after identity state is fixed.

---

## 11. Mechanical integration

Candidate implementation should modify only the surfaces required to expose and validate the specialist capability:

```text
skills/marketing-practitioner/handbook/15-brand-identity-and-visual-systems.md
skills/marketing-practitioner/references/brand-identity-evidence.md
skills/marketing-practitioner/routing-index.json
skills/marketing-practitioner/handbook/README.md
skills/marketing-practitioner/SKILL.md
skills/marketing-practitioner/scripts/test-knowledge-routing.py
evals/brand-identity-and-visual-systems-adversarial-cases.md
```

A later runtime-smoke artifact may be added if needed to record concrete path/output checks. Do not add runtime files merely for symmetry.

Routing smoke tests should verify every `brand-identity.*` route and at least one `BVxx` source lookup.

Do not claim the full routing suite passed unless it was actually executed on the candidate checkout.

Do not change `get-knowledge.py` or the routing manifest schema unless the existing mechanism cannot represent the proposed routes. Current routing infrastructure is sufficient by design.

---

## 12. Implementation non-goals

Do not implement:

```text
new controller job
new durable IDENTITY / BRAND primitive
new shared visual-design grammar
generic graphic-design owner
UI / product-design system
art-direction subsystem
asset-management / DAM system
naming framework
brand-architecture framework
trademark-law subsystem
copyright/licensing subsystem
generic consumer-testing framework
new causal framework
country-specific identity packs
logo-style taxonomy
color-psychology table
personality/archetype → geometry mapping
trend catalog
AI prompt library
AI image-generation wrapper
vector-editing engine
```

Do not create permanent routes for logo/color/type/motion merely because those artifacts may occur inside an identity system.

Do not bump public version, release notes, README release status, or CHANGELOG during candidate implementation/evaluation. Release metadata belongs after independent runtime review.

---

## 13. Implementation sequence and freeze discipline

Proceed in a separate candidate branch:

```text
candidate/brand-identity-visual-systems
```

Sequence:

```text
1. bounded candidate implementation
2. author self-review against verified theory + this design
3. deterministic routing/evidence mechanical verification
4. targeted adversarial runtime cases
5. targeted adjudication
6. freeze exact implementation/evaluation head
7. independent adversarial runtime review in a fresh session
8. local repairs only if reviewer identifies bounded defects
9. post-repair verification if repairs are required
10. release/merge preparation only after runtime gate passes
```

Behavioral/path evaluation must distinguish:

```text
KNOWLEDGE EXISTS
!= ROUTE IS ADDRESSABLE
!= ROUTE ACTIVATES WHEN NEEDED
!= CORRECT ROUTE WAS ACTUALLY USED
!= FINAL DECISION IS CORRECT
```

Do not infer runtime success merely because the handbook content is good or routing smoke tests pass.

---

## 14. Implementation gate

The design authorizes candidate implementation only under these conditions:

```text
ORIGINAL THEORY REVIEW                 THEORY_PASS_WITH_LOCAL_REPAIRS
POST-REPAIR VERIFICATION               POST_REPAIR_PASS
RUNTIME-DESIGN OWNER                   BOUNDED
NEW CONTROLLER JOB                     NO
NEW DURABLE PRIMITIVE                  NO
GENERAL DESIGN OWNER                   NO
FORMAL RESEARCH OWNER                  NO
LEGAL OWNER                            NO
LOCALIZATION OWNER                     NO
ROUTING INFRASTRUCTURE CHANGE          NO
```

Candidate implementation should therefore use:

```text
one specialist chapter
+ one scoped evidence ledger
+ one JIT namespace
+ minimal SKILL activation/handoff guidance
+ deterministic route/source checks
+ targeted adversarial runtime cases
```

No larger architecture is justified by the verified theory.

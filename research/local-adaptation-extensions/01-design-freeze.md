# Local Adaptation Extensions — Design Freeze

Status: **FROZEN FOR INDEPENDENT ADVERSARIAL REVIEW**  
Freeze date: 2026-09-03  
Repository base: `main@67a0fbe39012e76d5047353223ad9d16f5186fd4`

## 1. Research question

Can Marketing Practitioner admit community-maintained local adaptation knowledge without collapsing language, locale, market, geography, audience, channel, jurisdiction, and time; without allowing local knowledge to override existing decision owners or universal invariants; and without requiring a new runtime registry, scope-scoring engine, or locale subsystem?

The design target is deliberately narrow:

> Add an extensibility contract for scoped local evidence that can change an existing marketing decision, while preserving the current controller, ownership boundaries, evidence discipline, and just-in-time routing model.

This is not a proposal to build country guides, cultural profiles, or a comprehensive localization database.

## 2. Existing architecture already constrains the problem

The current runtime already requires:

```text
current job
→ resolved-state freeze
→ open decision
→ decision-relevant evidence
→ dependency-first owner selection
→ just-in-time knowledge loading
→ minimum sufficient output
```

Chapter 07 already distinguishes:

```text
language
locale
market
geography
currency
timezone
jurisdiction
```

and already treats culture-level findings as priors rather than deterministic verdicts. It also gives actual identity, relationship, authority, interaction history, scoped first-party evidence, and current community or organizational norms stronger decision relevance than broad national or cultural assumptions when those facts are material.

Therefore the extension mechanism must specialize the existing architecture rather than introduce a parallel localization ontology.

## 3. Freeze verdict

> **A THIN SCOPED-ADAPTATION EXTENSION IS REPRESENTABLE WITHOUT A NEW DECISION OWNER OR RUNTIME SUBSYSTEM.**  
> **COUNTRY- OR LOCALE-FIRST RUNTIME MODULES ARE REJECTED.**  
> **DYNAMIC SCOPE REGISTRY / SCORING IS NOT JUSTIFIED BY THE CURRENT FAILURES.**  
> **EXISTING DECISION OWNERS REMAIN AUTHORITATIVE.**  
> **EXISTING ROUTING SEMANTICS REMAIN SUFFICIENT FOR V0.**

The extension unit is not a country profile. It is a bounded evidence-to-decision specialization whose applicability must remain explicit.

## 4. Rejected design A — country / locale packs

Rejected examples:

```text
locales/
  vi-VN/
  th-TH/
  ja-JP/
```

or runtime namespaces such as:

```text
adapt-market-vn.*
adapt-language-vi.*
```

as the primary discovery structure.

### Why rejected

A real task can cross several independent dimensions:

```text
language = vi
market = US
community = Vietnamese diaspora
channel = Facebook Group
commercial context = remittance
```

No single country or language namespace owns that context cleanly.

Country-first routing also creates a noun-trigger hazard:

```text
mentions Vietnam
→ load Vietnam knowledge
```

which conflicts with the current rule that a country name, language request, platform noun, or other topic label does not itself activate a deep path.

Country folders may remain useful as human navigation in a future contribution repository, but physical location must never imply runtime applicability.

## 5. Rejected design B — implicit locale / regional inheritance

Do not use configuration-style inheritance for behavioral marketing knowledge.

Freeze:

```text
ABSENCE OF SCOPED LOCAL EVIDENCE
!= PERMISSION TO INHERIT A BROADER BEHAVIORAL CLAIM
```

Examples that remain invalid:

```text
no Vietnam evidence
→ use Southeast Asia behavior as fact

no Hanoi evidence
→ use national behavior as fact

no Shopee electronics evidence
→ use generic Vietnam ecommerce behavior as fact
```

Broader evidence may generate a hypothesis or identify a decision worth checking. It does not become a resolved local fact merely because narrower evidence is absent.

## 6. Rejected design C — specificity or precedence engine

Do not create:

```text
country > region > global
company > country > region
specificity_score
locale_priority
adaptation_confidence_score
```

More specific evidence is not automatically more authoritative. A narrow anecdote can be weaker than a broader high-quality study; a reviewed contribution can still be inapplicable to the current population; a company fork can still contain weak or stale evidence.

Applicability is resolved through the current open decision, evidence scope, provenance, and authoritative task state, not through a universal numeric or hierarchical override rule.

## 7. Frozen conceptual model

```text
CORE DECISION SYSTEM
        │
        │ owns decisions and invariants
        ▼
EXISTING DECISION OWNER
(positioning / messaging / content / commerce /
 localization / commercial design / etc.)
        ▲
        │ scoped evidence-to-decision specialization
        │
LOCAL ADAPTATION
        ▲
        │
SCOPED EVIDENCE
```

Freeze:

```text
ADAPTATION != DECISION OWNER
```

An adaptation can change one bounded choice inside an existing owner when its evidence applies. It cannot seize ownership of the whole task, invent a new pipeline, or reopen unrelated upstream strategy.

## 8. Frozen routing model — decision first, locality second

Routing starts from the open decision, not from nationality, language, or country.

Preferred future shape when actual runtime knowledge exists:

```text
adapt-content.*
adapt-localization.*
adapt-messaging.*
adapt-commerce.*
adapt-commercial-design.*
```

Only namespaces that contain real knowledge should exist.

The route answers:

> Which decision-relevant adaptation knowledge may be useful?

The section scope answers:

> Does this knowledge actually apply to the current task?

Do not encode the whole scope into the route ID. Keep detailed scope in the knowledge section so `routing-index.json` remains an address table rather than a second handbook or a scope database.

A future route might be:

```text
adapt-content.community-peer-posture
```

with scope inside the section such as:

```text
language: vi
market: US
audience: Vietnamese diaspora
channel: Facebook Groups
interaction context: peer/community participation
```

The existing `namespace.section` router can represent this without a new resolver.

## 9. Frozen contribution unit

The practical unit is:

> **scoped evidence bound to one existing decision consequence**

A contribution should contain at least:

```text
SCOPE
CLAIM
EVIDENCE
DECISION IMPACT
LOAD WHEN
DO NOT USE WHEN
MUST PRESERVE
REVIEW STATE
USAGE STATE
```

### Scope

Declare only dimensions that materially bound the claim. Possible dimensions include:

```text
language
market
geography
channel / surface
audience / role
category / industry
interaction context
commercial context
organization / community
jurisdiction when material
time / effective period when material
```

Do not require every field when it cannot change applicability.

### Claim

State the bounded observation, convention, language-realization issue, market condition, community norm, buying-context pattern, trust/proof expectation, or other locally relevant proposition.

Avoid population-wide formulations unsupported by the evidence.

### Evidence

Identify what supports the claim and what kind of evidence it is. Native familiarity, practitioner experience, community review, style guides, first-party data, qualitative research, observational data, experiments, and primary documentation can all play different evidentiary roles; they are not interchangeable.

Native or local familiarity improves review quality but does not by itself establish prevalence, causality, or market-wide applicability.

### Decision impact

Name the existing decision this evidence can change.

Examples:

```text
relationship realization
proof emphasis
publishing posture
terminology choice
local alternative set
buying-friction interpretation
commercial payment-method consideration
commerce information allocation
```

Do not bundle multiple ownership changes into one adaptation merely because they share one source.

### Load when

Describe when this knowledge may be material **after the relevant decision is already open**.

`LOAD WHEN` is not activation authority.

Invalid:

```text
market = Vietnam
→ load this module
```

Valid form:

```text
when message proof allocation is unresolved,
and the task population/context matches the scoped evidence,
this adaptation can change which proof is prioritized
```

### Do not use when

State nearby contexts where the claim is unsupported or materially misleading. This is a negative control against scope leakage.

### Must preserve

Name upstream/core facts that this adaptation must not re-infer or override, for example:

```text
product facts
resolved offer state
speaker identity
recipient relationship
claim boundaries
legal / ethical constraints
platform capability state
```

### Review state

Use a small vetting state:

```text
provisional
reviewed
```

This records contribution review, not truth or applicability.

### Usage state

Keep lifecycle/conflict status separate:

```text
active
contested
deprecated
```

A claim may be `reviewed + contested`.

## 10. Same evidence may support multiple owner-specific adaptations

One evidence source can affect more than one decision, but ownership must remain explicit.

Example:

```text
EVIDENCE:
COD is materially expected in population/context X
```

Potential decisions:

```text
Commercial Design:
Should COD be offered?

Commerce / messaging representation:
If COD is already offered, should and how should it be surfaced?
```

Do not collapse these into:

```text
COD is important locally
→ offer COD
→ emphasize COD
```

The same evidence may justify two separate bindings to two owners. It does not authorize one adaptation to own both decisions automatically.

## 11. Resolved state remains frozen

Freeze:

```text
LOCAL RELEVANCE
!= PERMISSION TO REOPEN RESOLVED STATE
```

If the user has already established:

```text
payment methods: card only
```

an adaptation saying a local population often expects COD does not silently reopen the offer while the task is merely to write product copy.

Reopen upstream state only under the existing controller rule: when necessary to complete the current job truthfully or because the supplied state is contradictory or materially insufficient.

## 12. Platform and local-adaptation ownership boundary

Not every market-scoped fact belongs in `adaptations/`.

Keep:

```text
PLATFORM CAPABILITY / POLICY / MECHANISM
→ platform module

PRODUCT / OFFER FACT
→ authoritative product / commercial state

MESSAGE / CLAIM / PROOF DECISION
→ existing handbook owner

LOCAL HUMAN / MARKET / BUYING / LANGUAGE EVIDENCE
→ adaptation input

LEGAL REQUIREMENT
→ authoritative legal dependency
```

Example:

```text
Lazada category IDs differ by country
```

is a Lazada platform fact, not a Vietnam adaptation.

Example:

```text
for population X in context Y, local proof Z materially affects trust evaluation
```

may be an adaptation if the evidence is appropriately scoped.

Do not duplicate platform-local facts into an adaptation file merely because the platform behavior has a market dimension.

## 13. Conflict model

Do not resolve conflicting local claims through:

```text
newer file wins
private fork wins
narrower geography wins
reviewed always wins
highest score wins
```

Instead:

```text
current decision
+ authoritative task state
+ evidence scope
+ provenance / quality
+ material counterevidence
→ bounded interpretation
```

When two credible and applicable claims remain in conflict:

```text
preserve conflict
→ narrow the claim or decision
→ avoid forced adaptation
→ surface uncertainty when decision-relevant
```

Do not manufacture a single local truth merely to make routing deterministic.

## 14. Fork / upstream composition

A fork may add organization-specific adaptation knowledge without upstreaming it immediately.

Possible future shape:

```text
upstream adaptations
+
organization-specific adaptation knowledge
```

The core does not need to know that the private extension exists.

However:

```text
PRIVATE / ORGANIZATION-SPECIFIC
!= AUTOMATIC PRECEDENCE
```

Its evidence applies only when the current population/context is covered.

A private contribution can later be generalized upstream only after organization-specific assumptions are removed and the supported scope/evidence are made explicit.

## 15. Frozen invariants

```text
1. ADAPTATION != DECISION OWNER

2. LANGUAGE != LOCALE != MARKET != AUDIENCE
   != CHANNEL != JURISDICTION

3. ABSENCE OF LOCAL EVIDENCE
   != BROADER CLAIM INHERITANCE

4. MORE SPECIFIC
   != AUTOMATICALLY MORE AUTHORITATIVE

5. LOCAL RELEVANCE
   != PERMISSION TO REOPEN RESOLVED STATE

6. ROUTE / FILE LOCATION
   != APPLICABILITY

7. NATIVE FAMILIARITY
   != POPULATION EVIDENCE

8. ADAPTATION ROUTING STARTS FROM AN OPEN DECISION,
   NOT A COUNTRY / LANGUAGE / CULTURE NOUN

9. PLATFORM-SCOPED FACTS REMAIN WITH THE PLATFORM OWNER

10. CORE TRUTH, CLAIM, ETHICS, AND AUTHORITY INVARIANTS
    CONSTRAIN EVERY ADAPTATION
```

## 16. V0 physical design boundary

If the freeze survives independent review, the first implementation should remain intentionally thin.

Candidate surfaces:

```text
skills/marketing-practitioner/
  adaptations/
    README.md

skills/marketing-practitioner/handbook/
  07-international-marketing-and-ethics.md

skills/marketing-practitioner/SKILL.md

CONTRIBUTING.md
```

`routing-index.json` should not receive an adaptation namespace until actual runtime adaptation knowledge exists.

V0 should not add:

```text
country modules
official Vietnam / Thailand / Japan knowledge
adaptation registry
scope matcher
precedence engine
confidence scoring
new retrieval script
new controller job
new primitive
new decision owner
```

The first implementation should establish the extension contract and runtime boundary only.

## 17. Promotion gate for more runtime machinery

A dynamic registry, selector, scope matcher, precedence mechanism, or other runtime subsystem is justified only if an independently reviewed concrete case shows that the current decision-first routing plus explicit section scope cannot represent or retrieve the needed knowledge without material decision error.

The burden is:

```text
INPUT / TASK
→ OPEN DECISION
→ CURRENT OWNER / ROUTE
→ SCOPED ADAPTATION NEEDED
→ FAILURE UNDER THE THIN DESIGN
→ MATERIAL DECISION CONSEQUENCE
→ WHY LOCAL REPAIR IS INSUFFICIENT
→ SMALLEST REQUIRED ARCHITECTURE CHANGE
```

Without that chain, keep the thin design.

## 18. Frozen implementation classification

The proposed runtime promotion is expected to be **Level 2**, not Level 3, if it remains within this freeze:

- small controller hook;
- Chapter 07 extension semantics;
- contribution contract;
- no new owner or primitive;
- no routing-manifest structure change;
- no new subsystem.

If implementation requires a generic scope engine, cross-owner adaptation controller, new top-level knowledge layer, or manifest schema redesign, stop and return to architecture review.

## 19. Final freeze statement

```text
NEED FOR EXTENSIBILITY                  CONFIRMED
COUNTRY / LOCALE PACK AS RUNTIME MODEL  REJECTED
IMPLICIT REGIONAL INHERITANCE           REJECTED
AUTOMATIC SPECIFICITY PRECEDENCE        REJECTED
NEW DECISION OWNER                      REJECTED
NEW PRIMITIVE                           REJECTED
NEW CONTROLLER JOB                      REJECTED
DYNAMIC SCOPE REGISTRY                  NOT YET JUSTIFIED
DECISION-FIRST ROUTING                  FROZEN CANDIDATE
SCOPED EVIDENCE-TO-DECISION BINDING     FROZEN CANDIDATE
THIN V0 EXTENSION CONTRACT              FROZEN CANDIDATE
```

This freeze is not implementation evidence. It is the target to be attacked by an independent reviewer before runtime promotion.
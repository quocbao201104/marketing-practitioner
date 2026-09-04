# Japan Local Adaptation — Design Freeze

Status: **FROZEN FOR INDEPENDENT ADVERSARIAL REVIEW**  
Freeze date: 2026-09-04  
Repository base: `main@a0535a9a3c7a177de4a0a473da8de0f51274613f`

## 1. Research question

In Japanese-language marketing communication, are there target-language realization decisions that an agent can still get materially wrong after the generic Marketing Practitioner controller has correctly resolved the relationship, authority, permission, responsibility, audience, message, and other upstream state — because the remaining choice depends on a Japanese-specific linguistic mechanism?

The purpose of this research is not to build a Japan market profile or a Japanese business-etiquette guide. It is to pressure the already-shipped scoped local-adaptation architecture with a second language whose mechanisms differ from the Vietnamese reference unit.

The promotion gate is unchanged:

```text
LOCAL-SPECIFIC MECHANISM
+
MATERIAL DECISION DELTA
+
GENERIC OWNER DOES NOT ALREADY KNOW
THE TARGET-SPECIFIC MECHANISM
=
ADAPTATION CANDIDATE
```

Counterfactual test:

> Remove the Japanese-specific knowledge, but keep all task-specific evidence and the generic handbook. Can the existing owner still make the correct realization decision reliably?

If yes, the material stays scoped evidence or a current dependency. If no, it may justify a local adaptation unit.

## 2. Existing architecture under pressure

The current architecture already provides:

```text
CURRENT JOB
→ FREEZE RESOLVED STATE
→ NAME OPEN DECISION
→ SELECT EXISTING OWNER
→ LOAD THE SMALLEST DECISION-RELEVANT KNOWLEDGE
→ PRESERVE TRUTH / AUTHORITY / CLAIM BOUNDARIES
```

Chapter 07 already preserves relationship-sensitive realization state and exposes one bounded JIT discovery edge:

```text
localization realization remains materially open
→ inspect owner-aligned adapt-localization knowledge
→ smallest matching route
→ section-local scope check
```

The current real route is:

```text
adapt-localization.relationship-realization
```

It already contains `VN-LANG-REL-01` and therefore supplies the first test of whether one owner/decision route can contain multiple independently scoped local mechanisms without country-first routing, a registry, or a new owner.

## 3. Freeze verdict

Two Japanese-specific mechanisms survive the promotion gate.

```text
JP-LANG-HON-01
Japanese honorific-target realization
→ PROMOTE

JP-LANG-PERM-01
Japanese permission / benefit-sensitive deferential realization
→ PROMOTE
```

The following do not survive as separate runtime units:

```text
uchi / soto as a deterministic lookup rule
→ REJECT AS UNIT; KEEP AS CONTEXTUAL FACTOR

plain / polite style shifting in informal conversation
→ KEEP AS SUPPORTING / NEGATIVE EVIDENCE

Easy Japanese / やさしい日本語
→ KEEP AS AUTHORITATIVE ACCESSIBILITY DEPENDENCY

"Japanese business communication is formal"
→ REJECT

"customer = maximum keigo"
→ REJECT

age / status / company-side lookup tables
→ REJECT
```

No new controller job, shared primitive, decision owner, country pack, route family, scope registry, precedence engine, or freshness subsystem is justified by the current evidence.

## 4. JP-LANG-HON-01 — Japanese honorific-target realization

### 4.1 Local-specific mechanism

Japanese honorific realization cannot be reduced to one global `formal ↔ casual` scalar.

The official Japanese honorific guidance distinguishes at least the following orientations when they are material:

```text
POLITENESS TOWARD ADDRESSEE
!=
HONORIFICATION OF ACTOR / REFERENT
!=
HONORIFICATION OF ACTION TARGET
```

In particular, the official distinction between `謙譲語Ⅰ` and `謙譲語Ⅱ` matters because the first can honor the person toward whom an action is directed (`向かう先`), while the second can be deferential toward the addressee even when that addressee is not the action target [JPLA01][JPLA02].

This yields a concrete failure that generic relationship preservation cannot solve by itself:

```text
speaker is speaking respectfully to teacher A
+
speaker is describing a visit to teacher B

"参ります"
→ deferential toward the current addressee A

"伺います"
→ can honor the visit target B
```

The two forms may both look broadly "polite", but they do not preserve the same honorific orientation when addressee and action target differ [JPLA02].

A second official failure confirms that the mechanism is not merely terminology. Telling a customer `担当者に伺ってください` uses `伺う` in a way that honors the action target (the staff member) rather than the customer performing the action; the official guidance marks this as inappropriate for that customer action [JPLA03].

Therefore:

```text
RESPECTFUL RELATIONSHIP ALREADY RESOLVED
!=
CORRECT JAPANESE HONORIFIC TARGET
```

### 4.2 Existing owner

Owner remains:

```text
Localization / Chapter 07
```

The unit may only specialize Japanese realization after upstream identity, relationship, authority, interaction state, and message meaning are already resolved.

It does not decide who deserves respect, who belongs to which organization, what the speaker's authority is, or what the underlying relationship should be.

### 4.3 Decision impact

The bounded decision is:

> Given already-resolved interaction state and the semantic roles in the current utterance, which Japanese honorific realization preserves the intended relation without orienting honorification toward the wrong participant or semantic target?

When material, the realization must not collapse:

```text
ADDRESSEE
ACTOR / REFERENT
ACTION TARGET
SPEAKER / PUBLISHING IDENTITY
```

These are not proposed as new shared primitives. They are utterance-local semantic roles that the Japanese realization unit must preserve when the selected honorific construction depends on them.

### 4.4 Scope

Candidate scope:

```text
language: Japanese (`ja`)
variety: common / standard Japanese unless stronger scoped regional evidence applies
market / geography: not inherently Japan-only
channel: any where honorific-sensitive participant orientation is materially open
category: not category-specific
effective period: largely structural / low-volatility, subject to stronger current scoped evidence
```

Japanese language, Japanese nationality, Japan market, customer status, age, or business context alone are not activation authority.

### 4.5 Must preserve

When material:

```text
speaker / publishing identity
addressee
actor / referent
action target
resolved relationship / standing / authority
organizational or community context
interaction history
approved wording / current house style
accessibility requirement
scoped regional / community evidence
```

### 4.6 Must not infer

```text
Japanese → formal
customer → fixed keigo form
older → more honorific morphology
external person → always honorify
own employee → never honorify
company context → maximum keigo
Osaka / Kansai geography → infer dialect honorific form
```

## 5. Uchi / soto is a factor, not a unit

Official guidance confirms that `uchi / soto` can materially affect honorific choice, including how a speaker refers to a manager or colleague when speaking to an external party [JPLA04].

However, the same official guidance gives a school context where a colleague who is organizationally `uchi` may still be referred to as `田中先生` when speaking to a parent because the teacher role and the parent's frame can outweigh a mechanical inside/outside rule [JPLA04].

Therefore freeze:

```text
UCHI / SOTO
= MATERIAL CONTEXTUAL INPUT

UCHI / SOTO
!= DETERMINISTIC ADDRESS / HONORIFIC RULE
```

No `JP-...-UCHI` unit, organization graph, or `inside > outside` precedence mechanism is justified.

## 6. Regional variation constrains scope

Official guidance explicitly documents regional honorific systems that differ from common/standard Japanese. For example, Kansai `〜はる` can be used in distributions that differ from standard `〜れる / 〜られる`, including use with own-side persons [JPLA11].

Therefore:

```text
TARGET LANGUAGE = JA
!=
STANDARD-JAPANESE UNIT HAS UNIVERSAL AUTHORITY
```

A reliable current regional/community writing sample may constrain realization more strongly within its evidenced scope.

Geography alone does not authorize regional-form inference.

## 7. JP-LANG-PERM-01 — Japanese permission / benefit-sensitive deferential realization

### 7.1 Local-specific mechanism

The Japanese construction `〜させていただく` is not a semantically neutral transformation meaning only "make this more polite".

The official baseline analysis describes it as fundamentally associated with:

```text
A. own-side action performed with permission
   from the addressee or a third party
+
B. benefit to the speaker from that permission
```

and notes that perceived appropriateness varies with how strongly those conditions are satisfied or plausibly construed [JPLA05].

This creates a real Marketing Practitioner failure mode because the core already preserves authority, permission, autonomy/obligation, and responsibility/repair state, while a generic localization owner does not know that this Japanese construction can interact with those states.

Example pressure:

```text
resolved state:
company unilaterally decides to suspend operations

open decision:
Japanese customer-facing realization

naive politeness transform:
休業いたします
→ 休業させていただきます
```

The official analysis treats the latter as appropriate only when the permission/benefit conditions, or a non-forced construal of them, are available; otherwise `休業いたします` may be more suitable [JPLA05].

Therefore:

```text
INTRODUCING させていただく
!= SEMANTICALLY NEUTRAL POLISHING
```

### 7.2 Language change prevents reverse inference

The construction is also changing.

NINJAL corpus-based explanation documents historical growth of `サセテイタダク` and notes contemporary uses where the other party is not materially involved [JPLA06].

Recent Japanese research describes grammaticalization / pragmatic expansion from a benefactive-humble construction toward newer deferential or beautifying uses in some contexts, where original permission/benefit meaning can weaken [JPLA07].

NHK language-variation studies also report substantial age/context variation in support for `させていただく` expressions, including a 2025 survey published in 2026 [JPLA08][JPLA09].

Therefore the runtime constraint must work in both directions:

```text
INTRODUCING させていただく
!= PERMISSION-NEUTRAL POLITENESS TRANSFORM

EXISTING させていただく
!= VERIFIED FACTUAL PERMISSION

EXISTING させていただく
!= VERIFIED FACTUAL BENEFIT
```

The unit must not infer business/legal/interaction permission from wording alone.

### 7.3 Existing owner

Owner remains:

```text
Localization / Chapter 07
```

The unit consumes resolved permission/authority/agency/responsibility state; it does not create or adjudicate that state.

### 7.4 Decision impact

The bounded question is:

> Given already-resolved permission, authority, agency, benefit, responsibility, and interaction state, does using, preserving, or replacing a Japanese deferential construction such as `〜させていただく` preserve that state rather than silently changing it?

### 7.5 Candidate scope

```text
language: Japanese (`ja`)
variety: common / standard Japanese unless stronger scoped evidence applies
market / geography: not inherently Japan-only
open decision: own-side action wording where deferential realization is materially unresolved
material dimensions: permission, authority, agency, autonomy/obligation, responsibility/repair, benefit framing
effective period: mechanism is established but pragmatic acceptability is medium-volatility; newer scoped evidence may matter
```

### 7.6 Guardrails

```text
させていただく PRESENT
!= VERIFIED PERMISSION

させていただく PRESENT
!= VERIFIED BENEFIT

NO VERIFIED PERMISSION
!= AUTOMATICALLY FORBIDDEN

MORE POLITE
!= SEMANTICALLY NEUTRAL

DEFERENCE
!= TRANSFER OF DECISION AUTHORITY

APOLOGY / REPAIR
!= PERMISSION REQUEST

UNILATERAL DECISION
!= CUSTOMER AUTHORIZATION

AGE / REGION
!= FORM LOOKUP KEY
```

Current approved first-party wording may remain authoritative for the dimensions it actually resolves. The Japanese adaptation is not permission to normalize every organization into one preferred form.

## 8. Easy Japanese is a scoped dependency, not a Japan unit

Official Japanese government guidance for `やさしい日本語` prioritizes comprehension for foreign residents and explicitly recommends avoiding `尊敬語 / 謙譲語` while retaining basic polite `です / ます` style [JPLA10].

This yields an important negative control:

```text
RESPECT
!= MAXIMIZE HONORIFIC COMPLEXITY

ACCESSIBILITY REQUIREMENT
CAN CHANGE REALIZATION
WITHOUT LOWERING UNDERLYING RESPECT
```

However, this does not justify an `adapt-japan.easy-japanese` unit. The activation condition is an accessibility / audience requirement, not nationality or Japan market membership.

Treat authoritative Easy Japanese guidance as a scoped task dependency when that communication objective is actually present.

## 9. Plain / polite style shifting remains supporting evidence

Japanese interaction research can show that `です / ます` shifts may occur within relationships rather than mapping one relationship to one invariant speech style.

That supports the negative constraint:

```text
ONE RELATIONSHIP
!= ONE SPEECH LEVEL FOR EVERY UTTERANCE
```

But the current research has not demonstrated a Marketing Practitioner decision failure that requires a separate runtime unit. Keep this material as supporting evidence unless a concrete workload shows that generic plus JP-HON/PERM knowledge remains insufficient.

## 10. Second-language generalization result

The current route can host distinct local mechanisms without encoding country/language into the route ID:

```text
adapt-localization.relationship-realization
│
├── VN-LANG-REL-01
│   SELF ↔ ADDRESS coupled realization
│
├── JP-LANG-HON-01
│   ADDRESSEE ≠ REFERENT ≠ ACTION TARGET
│   honorific orientation
│
└── JP-LANG-PERM-01
    deferential form ↔ permission / benefit / agency semantics
    with language-change guardrails
```

This is evidence for — not proof of unlimited — generalization of the thin extension model.

Freeze:

```text
ONE ROUTE
CAN CONTAIN MULTIPLE
SEPARATELY SCOPED LOCAL UNITS
```

No country-first route such as `adapt-japan.*` or `adapt-language-ja.*` is justified.

## 11. Route and controller impact

No new route is currently justified.

The existing route already resolves:

```text
adapt-localization.relationship-realization
→ adaptations/localization.md
→ ## Relationship realization
```

Chapter 07 already contains a bounded JIT discovery edge for relationship-sensitive target-language realization.

Therefore a future implementation should first attempt the smallest change:

```text
append JP units under the existing relationship-realization section
+
add scoped Japanese evidence ledger
+
add targeted Japan adversarial eval
```

Do not modify `SKILL.md`, `routing-index.json`, `get-knowledge.py`, or shared Chapter 07 unless independent review demonstrates a concrete discovery/representation failure that cannot be repaired locally.

## 12. Shared-state pressure does not yet justify a primitive

JP-LANG-HON-01 exposes semantic roles such as actor/referent/action-target that are not explicitly listed as a global localization schema.

This does **not** yet justify a new shared relationship graph or utterance-role primitive.

The current evidence only establishes that the Japanese unit must not collapse those roles when the current utterance already makes them material.

Promotion burden for shared architecture remains:

```text
MULTIPLE DISTINCT OWNERS / LANGUAGES
REPEATEDLY LOSE THE SAME STATE
+
LOCAL REPAIR CANNOT PRESERVE IT
+
MATERIAL DECISION FAILURE
=
CONSIDER SHARED HARDENING
```

That burden is not met here.

## 13. Frozen adversarial cases

A future implementation/review should preserve at least the following cases.

### Honorific-target cases

```text
JH1  addressee == action target
     → distinction may collapse locally; do not over-route if wording already resolved

JH2  speak to teacher A about visiting teacher B
     → preserve addressee vs action target

JH3  tell customer to ask staff member
     → do not use humble form that honors staff instead of customer's action

JH4  customer-service sentence whose honorific morphology elevates a product/object
     → detect target mismatch; do not claim population rejection

JH5  employee speaking externally about own manager
     → uchi/soto may matter, but not as a universal rule

JH6  teacher speaking to parent about colleague teacher
     → role/context may defeat mechanical uchi/soto

JH7  approved organization wording fully resolves honorific choice
     → NO LOAD / preserve unless truthful conflict requires reopening

JH8  `です / ます` fixed but honorific target remains open
     → freeze resolved speech level; constrain only open dimension

JH9  Easy Japanese accessibility requirement
     → do not maximize honorific complexity

JH10 mass audience copy without honorific-sensitive participant relation
     → NO LOAD

JH11 reliable regional/community language evidence supplied
     → preserve scoped evidence; do not normalize to standard Japanese

JH12 Japanese-language communication outside Japan
     → language may matter; market does not define applicability
```

### Permission / benefit-sensitive cases

```text
JP1  genuine request for permission to copy another person's material
     → construction may be compatible with resolved permission state

JP2  invited presentation / allowed action
     → permission frame may be plausible if wording remains open

JP3  unilateral company closure notice
     → do not fabricate customer permission through politeness

JP4  conventionalized existing `させていただく` wording
     → do not reverse-infer factual permission

JP5  apology / acknowledgement of fault
     → preserve responsibility; do not launder repair into permission-like framing

JP6  organization declines to answer
     → do not infer audience authorized the refusal

JP7  approved house phrase supplied
     → preserve if the relevant dimension is resolved

JP8  current first-party sample prefers `いたします`
     → do not automatically "upgrade" to `させていただく`

JP9  request only says "make this more polite" with no permission facts
     → choose semantics-preserving politeness; do not manufacture permission

JP10 Easy Japanese requirement
     → accessibility can constrain/remove the complex form

JP11 Japanese-language communication outside Japan
     → language can be relevant without Japan-market activation

JP12 Kansai geography only
     → geography alone does not determine construction preference
```

## 14. Evidence discipline

The source ledger is `02-evidence-ledger.md`.

The freeze distinguishes:

```text
LINGUISTIC FUNCTION
!= POPULATION ACCEPTABILITY

POPULATION ACCEPTABILITY
!= CAUSAL MARKETING EFFECT

OFFICIAL NORMATIVE / DESCRIPTIVE GUIDANCE
!= UNIVERSAL NATURAL-LANGUAGE LAW

LLM EVALUATION RESULT
!= PROOF OF THE LINGUISTIC CLAIM
```

Official guidance supports the mechanism and its normative/descriptive boundaries. NHK survey work supports variation and anti-universalization. NINJAL and academic work support historical/pragmatic change. LLM research only supports the runtime risk that models can still struggle with contextual honorific conversion; it is not the source of the Japanese linguistic rules.

## 15. Implementation boundary if review passes

Smallest candidate implementation:

```text
skills/marketing-practitioner/adaptations/localization.md
  + JP-LANG-HON-01
  + JP-LANG-PERM-01

skills/marketing-practitioner/references/
  + local-adaptation-japan-evidence.md

evals/
  + local-adaptation-japan-language-v0.md
```

Expected non-changes:

```text
SKILL.md                         unchanged
routing-index.json               unchanged
get-knowledge.py                 unchanged
Chapter 07                       unchanged unless review proves a missing discovery edge
controller jobs                  unchanged
shared primitives               unchanged
```

The implementation must remain stacked conceptually on the already-released v1.1.0 scoped local-adaptation contract.

## 16. Explicitly rejected expansions

Do not add without a new concrete failure:

```text
adapt-japan.*
ja-JP country pack
Japanese culture profile
keigo engine
honorific target graph
relationship database
uchi/soto resolver
regional dialect resolver
age/status lookup table
politeness score
specificity score
adaptation registry
freshness engine
new localization owner
new controller job
```

## 17. Final freeze statement

```text
SECOND-LANGUAGE GENERALIZATION PRESSURE      COMPLETED
JP-LANG-HON-01                               PROMOTE
JP-LANG-PERM-01                              PROMOTE
UCHI / SOTO AS DETERMINISTIC UNIT            REJECTED
EASY JAPANESE AS COUNTRY ADAPTATION          REJECTED
PLAIN/POLITE SHIFT AS RUNTIME UNIT           DEFERRED
COUNTRY-FIRST JAPAN ROUTING                  REJECTED
NEW ADAPTATION ROUTE                         NOT JUSTIFIED
NEW SHARED PRIMITIVE                         NOT JUSTIFIED
NEW CONTROLLER / OWNER                       NOT JUSTIFIED
CURRENT RELATIONSHIP-REALIZATION ROUTE        SUFFICIENT CANDIDATE
MEDIUM-VOLATILITY LOCAL LANGUAGE CHANGE      REPRESENTABLE WITH EXISTING LIFECYCLE CONTRACT
```

This document is a research/design freeze, not runtime implementation evidence and not a behavioral benchmark. It must be attacked independently before the Japanese units are promoted into the installed skill.
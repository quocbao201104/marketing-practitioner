# Japanese Relationship Realization — Targeted Pressure Test v0

Status: **targeted architecture/regression suite, not a behavioral benchmark**.

Candidate contributions:

```text
JP-LANG-HON-01
JP-LANG-PERM-01
```

Intended logical route:

```text
adapt-localization.relationship-realization
```

Independent research-review verdict:

```text
PASS_WITH_LOCAL_REPAIRS
```

The required local repair is bounded Chapter 07 discovery hardening for target-language politeness/deference choices that can change authority, permission, agency, obligation, benefit, responsibility, or repair semantics even when the source task appears style-only.

## Question under test

Can the second-language local-adaptation implementation improve Japanese relationship-sensitive realization **without** creating Japan-first activation, a global formality scale, a keigo engine, a semantic-role graph, a permission inference rule, demographic lookup, or a new route/owner?

## Oracle

```text
CURRENT JOB
→ FREEZE RESOLVED IDENTITY / RELATIONSHIP / AUTHORITY /
  PERMISSION / AGENCY / RESPONSIBILITY STATE
→ IS A JAPANESE RELATIONSHIP / DEFERENCE REALIZATION
  MATERIALLY OPEN?
    ├─ NO  → DO NOT LOAD JAPANESE UNITS
    └─ YES → CHAPTER 07 LOCALIZATION OWNER
             → DISCOVER OWNER-ALIGNED adapt-localization NAMESPACE
             → adapt-localization.relationship-realization
             → section-local scope check
             → apply JP-LANG-HON-01 and/or JP-LANG-PERM-01
               only to still-open dimensions
```

The units consume resolved state. They must not re-infer who deserves respect, who authorized an action, what legal/business permission exists, or which regional variety the speaker should use.

## Required reviewer cases

These three cases come directly from the independent review repair requirement.

| Case | Task / resolved state | Expected route behavior | Required semantic behavior |
| --- | --- | --- | --- |
| J1 — unilateral closure disguised as style polishing | Company has already made a unilateral closure decision. Customer permission is not supplied or established. User asks: “Translate/rewrite this closure notice into natural, more polite Japanese.” | **DISCOVER + LOAD JP-PERM**. Chapter 07 must recognize that an apparently style-only deferential choice can change permission/agency framing before finalizing wording. | Do not introduce `させていただく` as a semantics-free politeness upgrade. Preserve the unilateral authority state; choose a Japanese realization consistent with it. |
| J2 — approved existing `させていただく` | Approved organization wording already contains `させていただく`. No independent factual permission evidence is supplied. | **NO REOPEN of resolved wording**; route optional only if another material dimension remains open or a truth conflict exists. | Do not reverse-infer factual permission/benefit from the form. Also do not automatically rewrite the approved form merely because explicit permission evidence is absent. |
| J3 — permission supplied upstream but absent from source sentence | Upstream state explicitly establishes relevant permission/authorization for the own-side action, but the source sentence itself does not mention permission. Japanese deferential realization remains open. | **LOAD JP-PERM** if the choice can materially express that state. | Consume the resolved permission/authority state. Do not reconstruct permission from source wording or require the source sentence to state it explicitly. |

## Additional honorific-target and scope cases

| Case | Task / resolved state | Expected route behavior | Required semantic behavior |
| --- | --- | --- | --- |
| J4 — teacher A / visit teacher B | Speaker addresses teacher A respectfully while describing a visit to teacher B; Japanese realization open. | **LOAD JP-HON**. | Keep addressee and action target distinct. “Broadly polite” is insufficient if the selected form honors the wrong participant. |
| J5 — customer asked to contact staff | Receptionist tells a customer to ask a staff member. Relationship and roles are resolved. | **LOAD JP-HON**. | Do not use humble morphology in a way that honorifically orients toward the staff member/action target instead of correctly realizing the customer's action. |
| J6 — product/inanimate subject | Customer-facing Japanese sentence contains an honorific-sensitive predicate whose grammatical subject is a product/object rather than the customer. | **LOAD JP-HON only if the honorific choice is materially open**. | Do not treat an inanimate object as the honorific target merely because the artifact should sound respectful. Do not turn this structural warning into a population-preference claim. |
| J7 — uchi/soto company context | Employee speaks externally about an own-company executive. Organization side is supplied but no approved wording is fixed. | **LOAD JP-HON if honorific orientation remains open**. | Use organizational side as contextual evidence, not as `own company → always de-honorify`. Preserve other interaction roles. |
| J8 — teacher / parent / colleague counterexample | Teacher speaks to a parent about a colleague teacher. | **LOAD JP-HON if wording is open**. | Do not mechanically apply uchi/soto. Role/title and interaction frame can constrain realization; no universal precedence rule is created. |
| J9 — `です/ます` fixed, honorific target open | User or style guide fixes polite speech level but not participant-sensitive honorific morphology. | **LOAD JP-HON only for the open dimension**. | Freeze `です/ます`; do not reopen speech level. Solve only honorific target orientation. |
| J10 — mass-audience Japanese copy | Japanese landing-page copy has no material person-specific honorific or own-side permission/deference choice. | **NO LOAD**. | Target language alone does not justify deep relationship-realization knowledge. |
| J11 — Japanese outside Japan | Japanese-language service message targets Japanese-speaking users in the United States; relevant honorific/deference choice is open. | **LOAD the matching JP unit**. | Language scope may apply while market != Japan. Do not require Japan-market membership. |
| J12 — stronger regional/community evidence | User supplies reliable current regional/community Japanese wording for the same relationship and context. | **LOAD only if a material dimension remains open**. | Treat stronger scoped evidence as constraining its evidenced dimension. Do not normalize it to common/standard Japanese merely because the upstream unit is broader. Geography alone does not create a regional form. |
| J13 — Easy Japanese requirement | Task explicitly requires Easy Japanese for accessibility. | **LOAD JP unit only when useful to preserve semantics; accessibility guidance remains a stronger scoped constraint on complexity**. | Respect does not require maximum honorific complexity. Avoid using the Japanese adaptation to undo an authoritative accessibility requirement. |
| J14 — both JP units apply | Own-side Japanese message mentions a third-party action target and also contains a materially open deferential own-action realization. | **LOAD same route; scope-check both units**. | Apply JP-HON to participant orientation and JP-PERM to permission/agency framing. One unit does not seize the other's decision dimension; no precedence engine is required. |

## Negative-control cases

| Case | Task / resolved state | Expected route behavior | Required semantic behavior |
| --- | --- | --- | --- |
| N1 — Japan noun, English output | “Shorten this approved English headline for our Japan campaign to 30 characters.” | **NO LOAD**. | `Japan` is not activation authority. |
| N2 — Japanese approved wording, no open dimension | Shorten already-approved Japanese copy while preserving exact required forms; no relationship/deference dimension is open. | **NO LOAD**. | Do not reopen approved wording merely because JP units exist. |
| N3 — age-only prompt | “Write a polite Japanese message to customers aged 65+.” No relationship/permission/organization evidence is supplied. | **NO automatic JP form lookup**. Load only if a real target-language semantic choice becomes open and material. | Never infer honorific level or `させていただく` suitability from age band alone. |
| N4 — region noun only | “Write Japanese copy for Osaka customers.” No scoped regional language evidence is supplied. | **NO regional-form inference**. | Osaka/Kansai geography does not authorize `〜はる` or another regional honorific form. |
| N5 — existing `させていただく` interpreted as authority | Source sentence contains `させていただく`; task asks what the company is legally/business-authorized to do. | **DO NOT use JP-PERM as permission evidence**. | Surface wording is not proof of factual permission, legal authorization, benefit, or decision authority. Route may explain the linguistic boundary but cannot resolve business/legal state. |

## Adversarial properties covered

```text
J1                 discovery repair for style-disguised semantics
J2 / J3            wording state != factual permission inference
J4 / J5 / J6       addressee != referent/actor != action target
J7 / J8             uchi/soto contextual, not deterministic
J9                  partial-dimension preservation
J10 / N1 / N2       fast path and noun-trigger resistance
J11                 language != market
J12 / N4            stronger regional evidence; geography != form
J13                 accessibility != maximum keigo
J14                 multiple independently scoped units in one route
N3                  age/status lookup rejection
N5                  language form != business/legal authority
```

## Static implementation requirements

The candidate implementation passes this suite structurally only if all remain true:

```text
1. logical route remains adapt-localization.relationship-realization
2. no adapt-japan / adapt-language-ja / ja-JP runtime namespace is added
3. both JP units live under one bounded relationship-realization section
4. detailed language/market/role/time scope stays inside each contribution
5. Chapter 07 contains the bounded discovery repair for semantics-bearing politeness/deference
6. JP-HON does not create a global ACTOR / REFERENT / ACTION TARGET / ADDRESSEE primitive
7. JP-PERM does not infer factual permission/benefit from surface wording
8. no-permission evidence does not become an automatic ban on させていただく
9. uchi/soto remains contextual evidence, not a resolver
10. regional variation remains a scope boundary, not geography-triggered routing
11. Easy Japanese remains a scoped accessibility dependency
12. no registry, scope score, precedence engine, freshness subsystem, or new loader is introduced
13. Chapter 07 remains the decision owner for localization realization
14. resolved approved wording remains frozen unless the existing controller reopening rule applies
```

## Promotion decision oracle

A future behavioral evaluation should distinguish at least:

```text
F0  correct fast-path / no activation
F1  correct activation + correct owner route
F2  activation but wrong JP unit applicability
F3  correct route but wrong honorific target orientation
F4  style-only classification causes JP-PERM discovery miss
F5  させていただく surface form reverse-inferred as factual permission
F6  resolved permission / approved wording reopened or ignored
F7  uchi/soto or age/region converted into deterministic lookup
F8  accessibility or stronger regional/community evidence overridden
F9  both JP units apply but one incorrectly takes ownership of the other's dimension
```

This file does not claim these behaviors have been model-benchmarked. It freezes the targeted regression cases and expected architecture semantics for the Japanese reference implementation.

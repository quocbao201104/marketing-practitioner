# Localization Adaptations

This file contains scoped local evidence that can materially change an already-open **localization realization** decision. It does not own audience, positioning, relationship, authority, platform, product, or commercial state.

Use the contribution contract in `README.md`. The logical route identifies the decision-relevant evidence family; each contribution below remains independently scope-checked.

## Relationship realization

### VN-LANG-REL-01 — Vietnamese self-reference and recipient-address realization

**SCOPE**

- language: Vietnamese (`vi`)
- market / geography: not inherently Vietnam-only; applicability follows target-language and interaction scope rather than nationality
- audience / role: audience-facing or interpersonal wording where self-reference and/or recipient address is explicit and materially unresolved
- channel / surface: any, unless an applicable channel, community, or organizational norm supplies stronger current evidence
- category / buying context: not category-specific
- effective period: structural / low-volatility linguistic evidence; preserve newer scoped evidence when it conflicts

**CLAIM**

Vietnamese person-reference is not exhausted by a neutral source-pronoun mapping. Address can be realized through personal pronouns, kinship terms, names, titles/roles, and other relational expressions [VNLA01][VNLA03]. Kinship-derived terms are also used in wider social communication, so their social use does not by itself assert literal kinship [VNLA01].

When both self-reference and recipient address are materially expressed, treat them as a **coupled relationship realization** rather than translating each source-language pronoun independently. Applied Vietnamese-language research documents that individual forms can be known while the resulting self/address combination remains pragmatically incompatible [VNLA02].

Regional evidence also shows that one national-language label does not imply one region-neutral inventory or expressive value [VNLA04].

**DECISION IMPACT**

This contribution can change only the bounded Chapter 07 decision:

> Given an already-resolved speaker/recipient relationship and interaction state, which Vietnamese self-reference / recipient-address realization preserves that state without inventing a different relation?

Use the already-resolved relationship as input. Select a coherent realization for the current artifact; do not use this contribution to decide who the speaker or recipient *is* to each other.

If one member of the self/address realization is already resolved while the other remains materially open, freeze the resolved member and use this contribution only for the still-open dimension. Coupled realization is a compatibility constraint; it is not permission to reopen both halves.

**LOAD WHEN**

Load this route only after the localization owner has an open realization decision and all are true:

```text
TARGET LANGUAGE = VIETNAMESE
+
SELF-REFERENCE OR RECIPIENT ADDRESS IS MATERIALLY OPEN
+
THE CHOICE CAN CHANGE RELATIONSHIP / STANDING /
INSTITUTIONAL ROLE / INTERPERSONAL DISTANCE CONVEYED
```

`Vietnam`, Vietnamese nationality, audience age, or a Vietnamese-market label alone is not activation authority.

**DO NOT USE WHEN**

- the task is only market selection or market research;
- the requested transformation contains no material person-reference choice;
- all material Vietnamese self-reference and recipient-address dimensions are already resolved by applicable approved forms and no truthful conflict requires reopening them;
- the only evidence is nationality, broad culture, age/status alone, or a generic demographic label;
- a regional form is being inferred merely from geography without scoped current evidence;
- the artifact's owner has already supplied a stronger current organizational, community, or first-party language rule that fully resolves the wording dimension still at issue.

A supplied form for only one dimension does not suppress this route when another dimension remains materially open. Preserve the supplied form exactly as resolved state and constrain only the open dimension to remain compatible with it.

**MUST PRESERVE**

- speaker / publishing identity;
- actual recipient relation;
- standing / authority;
- relevant interaction history;
- invited / expected / unsolicited state when material;
- autonomy / obligation and responsibility / repair state when material;
- applicable community / organizational norms;
- verified existing forms and approved voice;
- scoped regional evidence when it is actually supplied.

**MUST NOT INFER**

Do not manufacture any of the following from Vietnamese language, nationality, market, apparent age, or broad culture alone:

```text
KINSHIP
FAMILIARITY
HIERARCHY
INTIMACY
AUTHORITY
ORGANIZATIONAL ROLE
GENDERED RELATIONSHIP
AGE RELATIONSHIP
COMMUNITY STANDING
```

**REALIZATION GUARDRAILS**

```text
SOURCE "I" / "YOU"
!= TWO INDEPENDENT WORD SUBSTITUTIONS

KINSHIP-SHAPED SOCIAL ADDRESS
!= VERIFIED LITERAL KINSHIP

OLDER / YOUNGER / CUSTOMER / VIETNAMESE
!= FIXED ADDRESS LOOKUP KEY

"TÔI / BẠN"
!= UNIVERSAL SAFE DEFAULT

ONE HALF RESOLVED
!= REOPEN BOTH HALVES
```

If the relationship-indexing choice remains genuinely underdetermined, follow Chapter 07: preserve a verified existing form when applicable; otherwise prefer natural wording that avoids an unsupported relationship claim when the context permits it, and ask for missing state only when the choice is unavoidable and consequential.

**EVIDENCE**

Primary evidence records: [VNLA01][VNLA02][VNLA03][VNLA04] in `../references/local-adaptation-vietnam-evidence.md`.

Evidence type: local Vietnamese linguistic / applied-linguistic research. This evidence supports the realization mechanism and its boundaries; it does not establish a population preference, marketing lift, or deterministic address table.

**REVIEW STATE**

reviewed

**USAGE STATE**

active

### JP-LANG-HON-01 — Japanese honorific-target realization

**SCOPE**

- language: Japanese (`ja`)
- variety: common / standard Japanese unless stronger scoped regional, community, or organization evidence applies
- market / geography: not inherently Japan-only; applicability follows target-language and interaction scope rather than nationality or market
- audience / role: any audience-facing or interpersonal wording where honorific-sensitive participant orientation is materially unresolved
- channel / surface: any, unless an applicable accessibility, community, regional, or organizational rule supplies stronger current evidence for the dimension at issue
- category / buying context: not category-specific
- effective period: primarily structural / low-volatility linguistic evidence; preserve stronger newer scoped evidence where material

**CLAIM**

Japanese honorific realization is not one global `formal ↔ casual` scalar. Official Japanese guidance distinguishes honorific resources that can orient deference toward different semantic participants. In particular, `謙譲語Ⅰ` can honor the person who is the `向かう先` of an action, while `謙譲語Ⅱ` can be deferential toward the current addressee even when that addressee is not the action target [JPLA01][JPLA02].

Therefore, when material:

```text
POLITENESS TOWARD ADDRESSEE
!=
HONORIFICATION OF ACTOR / REFERENT
!=
HONORIFICATION OF ACTION TARGET
```

Official applied examples show that globally respectful intent is insufficient: a speaker can address one person respectfully while referring to an action directed toward a different person, and a humble form can become inappropriate when it honorifically orients toward the wrong action target [JPLA02][JPLA03].

`Uchi / soto` can be a real contextual factor, but official examples also defeat a mechanical `own side → always de-honorify` rule [JPLA04]. Regional honorific systems can also differ from common/standard Japanese, so this unit is not universal authority over stronger scoped regional/community evidence [JPLA11].

**DECISION IMPACT**

This contribution can change only the bounded Chapter 07 decision:

> Given already-resolved relationship, authority, interaction state, message meaning, and the semantic roles in the current utterance, which Japanese honorific realization preserves the intended relation without orienting honorification toward the wrong participant or action target?

Use already-resolved state as input. When the chosen Japanese construction depends on them, preserve the utterance-local distinction among addressee, actor/referent, action target, and speaker/publishing identity. These are local semantic roles in the current utterance, not new shared controller primitives.

If one realization dimension is already fixed by applicable approved wording or stronger scoped evidence, freeze that dimension and use this contribution only for the still-open honorific-sensitive choice.

**LOAD WHEN**

Load this route only after the localization owner has an open realization decision and all are true:

```text
TARGET LANGUAGE = JAPANESE
+
HONORIFIC-SENSITIVE PARTICIPANT ORIENTATION IS MATERIALLY OPEN
+
THE CHOICE CAN CHANGE WHO / WHAT THE JAPANESE FORM
TREATS AS THE ADDRESSEE, REFERENT, ACTOR, OR ACTION TARGET
FOR RELATIONAL / HONORIFIC PURPOSES
```

`Japan`, Japanese nationality, customer status, age, company context, or Japanese language alone is not activation authority. A mass-audience Japanese artifact with no material participant-sensitive honorific choice does not load this contribution merely because it is Japanese.

**DO NOT USE WHEN**

- the task is only market selection, country research, or bounded transformation with no material honorific-sensitive participant choice;
- all material Japanese honorific choices are already resolved by applicable approved forms and no truthful conflict requires reopening them;
- the only evidence is nationality, broad culture, age/status, customer status, organization membership, or geography alone;
- a regional form is being inferred merely from place without stronger scoped regional/community evidence;
- an applicable accessibility requirement or current organization/community rule already resolves the same wording dimension.

A supplied speech level such as `です / ます` does not suppress this contribution if honorific target orientation remains materially open. Freeze the resolved speech-level dimension and constrain only the open dimension.

**MUST PRESERVE**

- speaker / publishing identity;
- actual addressee relation;
- actor / referent and action target when materially distinguished in the current utterance;
- standing / authority;
- relevant interaction history;
- applicable organization / community context;
- autonomy / obligation and responsibility / repair state when material;
- verified existing forms and approved voice;
- applicable accessibility requirements;
- stronger scoped regional / community evidence when actually supplied.

**MUST NOT INFER**

Do not manufacture any of the following from Japanese language, nationality, market, customer status, age, apparent seniority, organization membership, or broad culture alone:

```text
WHO DESERVES HONORIFICATION
HIERARCHY
FAMILIARITY
ORGANIZATIONAL SIDE
AUTHORITY
CUSTOMER DEFERENCE LEVEL
REGIONAL HONORIFIC FORM
ONE UNIVERSAL FORMALITY LEVEL
```

**REALIZATION GUARDRAILS**

```text
"BE RESPECTFUL"
!= SUFFICIENT JAPANESE HONORIFIC TARGET

ADDRESSEE
!= ACTOR / REFERENT
!= ACTION TARGET

UCHI / SOTO
!= DETERMINISTIC LOOKUP TABLE

OWN ORGANIZATION
!= ALWAYS DE-HONORIFY

EXTERNAL PERSON
!= ALWAYS HONORIFY

CUSTOMER
!= MAXIMUM KEIGO

TARGET LANGUAGE = JA
!= STANDARD-JAPANESE UNIT HAS UNIVERSAL AUTHORITY
```

If honorific orientation remains genuinely underdetermined, preserve a verified existing form when applicable; otherwise prefer a natural realization that does not invent unsupported hierarchy or honorific target relations, and ask for missing state only when the choice is unavoidable and consequential.

**EVIDENCE**

Primary evidence records: [JPLA01][JPLA02][JPLA03][JPLA04][JPLA11] in `../references/local-adaptation-japan-evidence.md`.

Evidence type: Japanese government honorific guidance plus bounded regional evidence. These sources support the realization mechanism and its limits; they do not establish universal population preference, marketing lift, or a deterministic organization / age / customer lookup table.

**REVIEW STATE**

provisional

**USAGE STATE**

active

### JP-LANG-PERM-01 — Japanese permission / benefit-sensitive deferential realization

**SCOPE**

- language: Japanese (`ja`)
- variety: common / standard Japanese unless stronger scoped regional, community, or organization evidence applies
- market / geography: not inherently Japan-only
- audience / role: audience-facing or interpersonal wording where an own-side action, announcement, refusal, repair, or other deferential realization remains materially open
- channel / surface: any, unless an applicable accessibility, community, regional, or organizational rule supplies stronger current evidence for the dimension at issue
- category / buying context: not category-specific
- material dimensions: permission, authority, agency, autonomy / obligation, benefit framing, responsibility / repair
- effective period: the baseline construction semantics are established, while pragmatic acceptability and extension are medium-volatility; newer scoped evidence may matter for usage judgments

**CLAIM**

The Japanese construction `〜させていただく` is not a semantically neutral transformation meaning only “make this more polite.” Official guidance describes its baseline analysis as an own-side action associated with permission from the addressee or a third party plus benefit to the speaker, with appropriateness varying by how strongly those conditions are satisfied or plausibly construed [JPLA05].

Therefore:

```text
INTRODUCING させていただく
!= SEMANTICALLY NEUTRAL POLITENESS POLISHING
```

At the same time, contemporary usage has expanded. NINJAL and recent Japanese research document cases in which the other party is weakly involved or the original permission/benefit meaning is pragmatically weakened through language change [JPLA06][JPLA07]. NHK variation evidence also shows that acceptability is context- and population-sensitive rather than one universal Japanese preference [JPLA08][JPLA09].

Therefore the reverse inference is also invalid:

```text
EXISTING させていただく
!= VERIFIED FACTUAL PERMISSION
!= VERIFIED FACTUAL BENEFIT
```

**DECISION IMPACT**

This contribution can change only the bounded Chapter 07 decision:

> Given already-resolved permission, authority, agency, autonomy/obligation, benefit, responsibility, and interaction state, does using, preserving, or replacing a Japanese deferential own-side-action form such as `〜させていただく` preserve that state rather than silently changing it?

This contribution consumes resolved state. It does not decide whether permission, legal authority, business authorization, benefit, obligation, or responsibility actually exists.

**LOAD WHEN**

Load this route only after the localization owner has an open realization decision and all are true:

```text
TARGET LANGUAGE = JAPANESE
+
AN OWN-SIDE ACTION / ANNOUNCEMENT / REFUSAL / REPAIR /
DEFERENTIAL POLITENESS CHOICE IS MATERIALLY OPEN
+
THE TARGET-LANGUAGE CHOICE CAN ALTER OR IMPLY
PERMISSION / AUTHORITY / AGENCY / AUTONOMY / OBLIGATION /
BENEFIT / RESPONSIBILITY / REPAIR FRAMING
```

This lookup may be required even when the user frames the task only as “make this more polite/natural in Japanese.” The possible semantic consequence, not the stylistic noun, is the reason to load.

`Japan`, Japanese nationality, customer status, business email, or “make it polite” alone is not activation authority.

**DO NOT USE WHEN**

- the task is only market selection, country research, or bounded transformation with no material own-side-action / deferential semantic choice;
- all material Japanese wording dimensions are already resolved by applicable approved forms and no truthful conflict requires reopening them;
- the only evidence is nationality, broad culture, age, region, or customer status;
- the contribution would be used to infer factual permission, legal authority, or benefit solely from an existing surface form;
- a current approved organization/community form fully resolves the same wording dimension and no stronger truthfulness conflict requires change.

Absence of independently verified permission does not by itself authorize replacing an approved existing `させていただく` form. Preserve the approved wording dimension while keeping factual permission state separate.

**MUST PRESERVE**

- speaker / publishing identity;
- actual addressee relation;
- resolved authority / permission state;
- agency and autonomy / obligation;
- responsibility / repair state;
- relevant interaction history;
- verified existing forms and approved voice;
- applicable organization / community norms;
- applicable accessibility requirements;
- stronger scoped regional / current usage evidence when material.

**MUST NOT INFER**

Do not manufacture any of the following from `させていただく`, Japanese language, nationality, market, age, region, or broad culture alone:

```text
FACTUAL PERMISSION
LEGAL AUTHORIZATION
CUSTOMER AUTHORIZATION
FACTUAL BENEFIT
TRANSFER OF DECISION AUTHORITY
LACK OF RESPONSIBILITY
ONE POPULATION-WIDE ACCEPTABILITY VERDICT
```

**REALIZATION GUARDRAILS**

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

For Easy Japanese or another authoritative accessibility requirement, simpler realization may legitimately reduce honorific/deferential complexity while preserving respectful stance [JPLA10]. Accessibility is a scoped dependency, not a Japan-wide default.

**EVIDENCE**

Primary evidence records: [JPLA05][JPLA06][JPLA07][JPLA08][JPLA09][JPLA10] in `../references/local-adaptation-japan-evidence.md`.

Evidence type: Japanese government language guidance, NINJAL corpus/historical-pragmatics explanation, peer-reviewed Japanese language-change research, recent NHK language-variation evidence, and government Easy Japanese guidance. This evidence supports the semantic risk and its non-transfer boundaries; it does not establish marketing lift, universal current preference, or factual permission from wording alone.

**REVIEW STATE**

provisional

**USAGE STATE**

active
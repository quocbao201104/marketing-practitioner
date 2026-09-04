# Vietnamese Relationship Realization — Targeted Pressure Test v0

Status: **targeted architecture/regression suite, not a behavioral benchmark**.

Candidate contribution: `VN-LANG-REL-01`

Intended logical route:

```text
adapt-localization.relationship-realization
```

## Question under test

Can the first real local-adaptation contribution materially improve a Vietnamese relationship-realization decision **without** creating country-first activation, a pronoun lookup table, relationship re-inference, regional leakage, or a new decision owner?

The route should activate only after Chapter 07 owns an open target-language realization decision.

## Oracle

```text
CURRENT JOB
→ FREEZE RESOLVED RELATIONSHIP / IDENTITY / AUTHORITY STATE
→ IS A VIETNAMESE SELF/ADDRESS CHOICE MATERIALLY OPEN?
    ├─ NO  → DO NOT LOAD VN-LANG-REL-01
    └─ YES → CHAPTER 07 LOCALIZATION OWNER
             → DISCOVER OWNER-ALIGNED adapt-localization NAMESPACE
             → adapt-localization.relationship-realization
             → scope-check VN-LANG-REL-01
             → realize only the still-open dimension(s) coherently
```

The contribution must never infer the underlying relationship merely to make a wording choice. A resolved self-reference or recipient-address dimension remains frozen even when its paired dimension is still open.

## Cases

| Case | Task / resolved state | Expected route behavior | Required semantic behavior |
| --- | --- | --- | --- |
| V1 — supplied approved pair | Rewrite supplied Vietnamese copy. Brand guide already requires self-reference `chúng tôi` and recipient address `Quý khách`; no conflict is present. | **NO LOAD** — realization is already resolved. | Preserve the approved forms; do not reopen them because Vietnamese adaptation knowledge exists. |
| V2 — source `I/you`, relation resolved | Translate an English founder reply into Vietnamese. Upstream state says the recipient is a known peer in an established reciprocal community relationship, but no Vietnamese self/address forms are supplied. | **LOAD** — Chapter 07 must discover `adapt-localization`, then load the smallest matching route because material Vietnamese relationship realization remains open. | Do not translate `I` and `you` independently; choose a coherent pair that preserves the resolved peer relation and current community evidence. |
| V3 — Vietnam noun, English output | “Shorten this approved English headline for our Vietnam campaign to 30 characters.” | **NO LOAD**. | `Vietnam` is not activation authority; stay on the bounded transformation path. |
| V4 — Vietnamese output, no person reference | Translate an approved product label into Vietnamese; wording contains no material self-reference or recipient address. | **NO LOAD**. | Target language alone does not justify relationship-realization knowledge. |
| V5 — age-only prompt | “Write a Vietnamese message to customers aged 55+.” No relationship, organization voice, or address convention is supplied. | **LOAD only if explicit self/address wording becomes unavoidable and consequential**; otherwise avoid the route. | Never infer `cô/chú/bác` or another form from age band alone. Prefer relation-neutral wording where natural; ask only if the socially meaningful choice is unavoidable. |
| V6 — organization norm dominates | Write Vietnamese service copy. Current authoritative brand style says use `Quý khách` for recipients and the organization name or `chúng tôi` for self-reference. | **NO LOAD** when that rule fully resolves the wording; otherwise the route may only fill a genuinely open dimension. | Organization authority comes from the current task state, not from a generic cultural prior. Do not replace the approved convention with kinship-based address. |
| V7 — diaspora / market mismatch | Write a Vietnamese-language Facebook Group post for Vietnamese people living in the United States. Relationship state for the group is supplied, but Vietnamese self/address realization is open. | **LOAD** if the wording decision is material; Chapter 07 must discover `adapt-localization` even though market != VN. | Language scope can apply while market = US; do not require `market = VN`. Keep channel/community state as an upstream constraint rather than a country rule. |
| V8 — social kinship form | Source material shows the speaker currently addresses a non-relative community member as `anh`; that form is verified and applicable. | **NO RE-INFERENCE**; route optional only if another paired form remains open. | Preserve social address without inferring literal sibling kinship. `anh` in this state is realization evidence, not a family-fact assertion. |
| V9 — regional first-party evidence | User supplies a reliable Southern Vietnamese writing sample using a regional self-reference in the same relationship/context. | **LOAD only if realization remains open**. | Treat the sample as scoped first-party evidence for the relevant dimension. Do not let the national reference unit normalize it merely because the regional form is absent from the generic guidance. |
| V10 — underdetermined pair avoidable | Translate “I appreciate your patience” into Vietnamese for an unspecified recipient; no relation can be safely inferred. | **LOAD only if needed to recognize the realization risk**; Chapter 07 must be able to discover the route from the open decision. | Prefer natural wording that avoids unsupported person-reference when possible; do not freeze `tôi/bạn` as a universal safe default and do not erase responsibility/agency merely to avoid person-reference. |
| V11 — exact user instruction | User explicitly says: “Xưng em, gọi người nhận là chị.” The requested relation is permissible and no contradictory state exists. | **NO LOAD** — exact realization is supplied. | Preserve the user's resolved pair; adaptation knowledge must not replace it with a generic alternative. |
| V12 — platform/community noun false activation | “Shorten this already-approved Vietnamese Facebook Group announcement by 20%.” Existing wording contains no open self/address choice. | **NO LOAD**. | Neither `Facebook Group`, `Vietnamese`, nor the existence of VN-LANG-REL-01 opens localization strategy or relationship inference. |
| V13 — partial pair resolved | Translate a founder reply into Vietnamese. Upstream/user state fixes recipient address as `chị`; the speaker/recipient relationship is known, but self-reference remains materially open. | **LOAD only for the open self-reference dimension**. | Freeze `chị`; do not reopen recipient address. Use the route only to constrain a compatible self-reference. `ONE HALF OPEN != REOPEN BOTH HALVES`. |
| V14 — normal-flow namespace discovery | Same semantic state as V2, but begin only from normal controller behavior: current job → open localization realization → Chapter 07. | **DISCOVER + LOAD** — Chapter 07's bounded JIT pointer must direct inspection of the owner-aligned `adapt-localization` namespace and the smallest matching route. | Passing this case requires an actual controller/owner discovery edge, not merely the existence or addressability of the route in `routing-index.json`. |

## Adversarial properties covered

```text
V1 / V6 / V11  resolved-state preservation
V3 / V12       noun-trigger resistance
V4             target-language fast-path preservation
V2             coupled self/address realization
V5             age/status lookup-table rejection
V7             language != market
V8             social kinship form != literal kinship
V9             scoped regional / first-party evidence
V10            underdetermination without false default
V13            partial-pair preservation
V14            normal-flow route discovery
```

## Static route requirements

The candidate implementation passes this suite structurally only if all remain true:

```text
1. logical route = adapt-localization.relationship-realization
2. no adapt-vn / vi-VN / market-vn runtime namespace is added
3. route resolves to one bounded relationship-realization section
4. detailed language/market/audience/channel scope stays inside the contribution unit
5. evidence records remain independently addressable by source ID
6. the contribution says LOAD WHEN is not activation authority
7. the contribution does not contain an age/gender -> address lookup table
8. Chapter 07 remains the localization owner
9. Chapter 07 provides a bounded JIT discovery edge to the owner-aligned adaptation namespace when the realization remains materially open
10. one resolved self/address dimension remains frozen when another dimension is open
11. no registry, scope score, precedence engine, or new loader is introduced
12. absence of this contribution for another language does not authorize inheritance
```

## Promotion decision oracle

A future behavioral evaluation should distinguish at least:

```text
F0  correct fast-path / no activation
F1  correct activation + correct owner route
F2  activation but wrong local applicability
F3  relationship re-inference from demographic/cultural noun
F4  independent pronoun substitution causing pair incoherence
F5  resolved-state override
F6  regional/organizational evidence overridden by generic VN knowledge
F7  open localization decision but adaptation namespace not discovered
F8  one resolved pair dimension reopened because the other remained open
```

This file does not claim those runtime behaviors have been model-benchmarked. It freezes the targeted cases and expected architecture semantics for the first reference contribution.

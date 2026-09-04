# Japan Local Adaptation — Independent Adversarial Review Brief

Status: **FROZEN REVIEW CONTRACT**  
Review target: `168f24859138073567bce741ddac0e3356030d8c`  
Target artifacts:

```text
research/local-adaptation-japan/01-design-freeze.md
research/local-adaptation-japan/02-evidence-ledger.md
```

This review brief is committed after the frozen target. It defines how the target is judged; it is not retroactive evidence that the candidate already satisfies the contract.

## 1. Reviewer role

Act as an **INDEPENDENT ADVERSARIAL LOCAL-ADAPTATION REVIEWER** for the Japan candidate in Marketing Practitioner.

Do not defend the candidate.

Do not modify the repository.

Do not implement the units.

Do not broaden the task into a general Japanese culture, etiquette, or localization survey.

Do not recommend a new primitive, route family, resolver, country pack, or shared architecture merely because Japanese honorifics are complex.

Your job is to determine whether the frozen evidence justifies the two proposed adaptation units and whether they fit the already-released thin local-adaptation architecture without material distortion.

## 2. Primary questions

Answer all of the following:

1. Does `JP-LANG-HON-01` represent a real Japanese-specific mechanism that generic Chapter 07 does not already fully encode?
2. Does `JP-LANG-PERM-01` represent a real Japanese-specific realization mechanism rather than a style preference or stale prescriptive rule?
3. Can both units safely live under the existing route `adapt-localization.relationship-realization`?
4. Can the existing contribution contract express their scope, conflicts, and different volatility without a registry/resolver/freshness engine?
5. Does Japanese pressure reveal a shared-state or discovery defect that cannot be repaired locally?
6. Are any claims in the evidence ledger broader than the Japanese sources actually support?

## 3. Files to read

Start with the frozen target only:

```text
research/local-adaptation-japan/01-design-freeze.md
research/local-adaptation-japan/02-evidence-ledger.md
```

Then read only current runtime surfaces materially required to test composition:

```text
skills/marketing-practitioner/SKILL.md
skills/marketing-practitioner/handbook/07-international-marketing-and-ethics.md
skills/marketing-practitioner/adaptations/README.md
skills/marketing-practitioner/adaptations/localization.md
skills/marketing-practitioner/routing-index.json
skills/marketing-practitioner/scripts/get-knowledge.py
```

Read Chapter 04 only when testing responsibility/repair or permission-sensitive copy semantics.

Do not use later commits after the frozen target as evidence that a defect was already solved.

## 4. Promotion standard

A proposed Japanese unit is valid only if the reviewer can sustain:

```text
LOCAL-SPECIFIC MECHANISM
+
MATERIAL DECISION DELTA
+
GENERIC OWNER DOES NOT ALREADY KNOW
THE TARGET-SPECIFIC MECHANISM
=
VALID ADAPTATION
```

Reject a unit if generic Chapter 07 plus supplied task evidence can already make the correct decision without the Japanese-specific mechanism.

Do not count "models sometimes make Japanese mistakes" as sufficient promotion evidence by itself.

## 5. Evidence adjudication

Adjudicate every source record `JPLA01`–`JPLA12` as:

```text
PASS
PARTIAL
FAIL
```

For each `PARTIAL` or `FAIL`, state exactly which claim is unsupported or over-broad.

Special scrutiny:

- `JPLA01`–`JPLA05` should carry the primary mechanism burden.
- `JPLA06`–`JPLA09` should constrain language-change / population-acceptability claims, not erase the baseline mechanism.
- `JPLA10` is an accessibility negative control, not a general anti-keigo rule.
- `JPLA11` is a scope boundary, not a dialect inference system.
- `JPLA12` supports runtime risk only; it must not be used as proof of the linguistic rules.

## 6. Required attacks on JP-LANG-HON-01

Evaluate H1–H12.

### H1 — addressee equals action target

Can the candidate avoid overcomplicating a case where the addressee and the honorific action target are the same person and the wording is already resolved?

Required behavior: no unnecessary reopening or new schema.

### H2 — addressee differs from action target

Speaker addresses teacher A while describing a visit to teacher B.

Attack whether generic "respectful" state is sufficient.

The candidate succeeds only if Japanese-specific knowledge changes the realization decision in a materially justified way.

### H3 — customer acts toward staff member

Receptionist tells a customer to ask the responsible staff member.

Attack whether a globally customer-respectful intent can still produce honorification of the wrong target.

### H4 — non-human / product subject

Construct a customer-service sentence where honorific morphology would elevate a product/object rather than the intended person.

Required discipline: distinguish structural honorific-target analysis from a claim that Japanese consumers dislike the phrase.

### H5 — own manager when speaking externally

Test uchi/soto as a contextual factor.

Fail the candidate if it becomes a hard `own company → de-honorify` lookup rule.

### H6 — teacher colleague to parent

Use the official school counterexample.

Required behavior: role/context may constrain or defeat mechanical uchi/soto application without requiring a precedence engine.

### H7 — approved organizational wording

If the current organization has already approved the relevant Japanese wording, can the adaptation preserve it rather than normalize it to generic Japanese guidance?

### H8 — partially resolved realization

`です / ます` level is fixed, but actor/referent/action-target honorific orientation remains open.

Required behavior: freeze resolved dimensions and constrain only the open dimension.

### H9 — Easy Japanese requirement

Can an accessibility requirement legitimately reduce honorific complexity without the candidate interpreting that as reduced respect?

### H10 — mass audience / no material participant orientation

Can the candidate remain unloaded when no honorific-sensitive relation can change the result?

### H11 — stronger regional/community evidence

A reliable current regional/community sample conflicts with common/standard Japanese guidance.

Required behavior: preserve scoped evidence; do not infer regional forms from geography alone.

### H12 — Japanese outside Japan

Test Japanese-language communication in another market.

Required behavior:

```text
language relevance
!= Japan-market activation
```

## 7. Required attacks on JP-LANG-PERM-01

Evaluate P1–P12.

### P1 — genuine permission request

The speaker asks to copy another person's material.

Does the candidate preserve a real permission/benefit frame without turning it into a universal formula?

### P2 — invited / allowed action

The speaker was explicitly invited to present.

Can the form be compatible when permission framing is actually supported?

### P3 — unilateral company decision

Company unilaterally closes/suspends service.

Attack whether "make it more polite" can silently manufacture customer permission or authorization.

### P4 — conventionalized existing use

The artifact already contains `させていただく` in a contemporary conventionalized use.

Required behavior:

```text
wording present
!= factual permission proven
```

### P5 — apology / responsibility

The speaker acknowledges fault and must preserve direct responsibility.

Attack whether deferential rewriting can weaken agency or recast repair as a permission-like frame.

### P6 — refusal / no-answer statement

Organization says it will decline to answer.

Required behavior: do not infer the audience authorized the refusal merely from deferential morphology.

### P7 — approved house phrase

If the organization has approved the expression in the exact context, can the candidate preserve it without treating it as universal Japanese truth?

### P8 — first-party sample prefers `いたします`

Can current scoped first-party evidence outrank a generic urge to use `させていただく`?

### P9 — "make this more polite" with no permission facts

Required behavior: choose semantics-preserving politeness rather than invent permission/benefit.

### P10 — Easy Japanese

Can accessibility constrain/remove the complex deferential form?

### P11 — Japanese-language communication outside Japan

Required behavior: language may activate the scoped mechanism; market does not own applicability.

### P12 — geography-only Kansai cue

Required behavior: geography alone does not determine construction preference or form.

## 8. Language-change attack

The candidate claims `JP-LANG-PERM-01` is a real mechanism even though `させていただく` is pragmatically changing.

Pressure both failure directions:

```text
A. candidate becomes too prescriptive:
   no literal permission → always reject

B. candidate becomes too permissive:
   modern grammaticalization → permission semantics no longer matter
```

The correct design should preserve the narrower claim:

```text
DO NOT INTRODUCE THE FORM
AS SEMANTICALLY NEUTRAL POLISHING

AND

DO NOT REVERSE-INFER
FACTUAL PERMISSION / BENEFIT
FROM THE FORM ALONE
```

Determine whether the existing `effective period`, `review_state`, `usage_state`, and stronger-scoped-evidence rules are sufficient for this medium-volatility mechanism.

Recommend a freshness subsystem only if a concrete decision failure cannot be represented with those existing controls.

## 9. Route-generalization attack

The frozen candidate proposes no new route.

Current path:

```text
OPEN LOCALIZATION REALIZATION
→ Chapter 07 JIT discovery edge
→ adapt-localization.relationship-realization
→ section-local scope check
→ VN / JP unit
```

Attack whether one route can coherently contain:

```text
VN-LANG-REL-01
JP-LANG-HON-01
JP-LANG-PERM-01
```

A new route is justified only if the current route creates a concrete material failure in discovery, applicability, owner composition, or excessive loading that cannot be repaired by section wording/scope.

Do not create `adapt-japan.*` or `adapt-language-ja.*` for organizational neatness.

## 10. Shared-state attack

JP-LANG-HON-01 mentions utterance-local roles:

```text
ADDRESSEE
ACTOR / REFERENT
ACTION TARGET
```

Determine whether this exposes a missing shared primitive.

A shared primitive is justified only if:

```text
1. the current shared owner cannot express/preserve the required state;
2. the failure is not specific to the Japanese realization unit;
3. a local unit cannot preserve the roles from the current utterance;
4. the failure materially changes the decision;
5. the proposed shared change is the smallest repair.
```

Complexity of Japanese grammar is not sufficient evidence.

## 11. Discovery attack

The Vietnamese implementation previously demonstrated a real route-discovery defect and repaired it with a bounded Chapter 07 JIT pointer.

Determine whether Japan demonstrates a **new** discovery failure despite that repair.

Do not ask for a generic SKILL-level adaptation registry unless a normal current execution path has no deterministic way to discover the existing owner-aligned route.

If a failure exists, classify it exactly:

```text
ACTIVATION
DISCOVERY
ADDRESSABILITY
APPLICABILITY
OWNER COMPOSITION
FRESHNESS
EXECUTOR COMPLIANCE
```

Do not classify ordinary model non-compliance as an architecture defect without showing that the controller lacks the needed path/instruction.

## 12. What does not count as a successful attack

Insufficient by itself:

- Japanese keigo is complicated;
- a graph would model participants elegantly;
- country files would be easier for contributors;
- a rules engine would be more deterministic;
- current models make Japanese mistakes;
- an honorific taxonomy can be expanded further;
- `させていただく` has many uses;
- regional Japanese is diverse;
- a newer source exists;
- a future repository might contain thousands of local rules.

The standard is a plausible decision-relevant failure under the frozen thin architecture.

## 13. Successful architecture attack format

For every proposed architecture change, provide:

```text
INPUT / TASK
→ RESOLVED STATE
→ OPEN DECISION
→ CURRENT OWNER / ROUTE
→ JAPANESE MECHANISM NEEDED
→ FAILURE UNDER CURRENT DESIGN
→ MATERIAL DECISION CONSEQUENCE
→ WHY LOCAL REPAIR IS INSUFFICIENT
→ SMALLEST REQUIRED CHANGE
```

If this chain cannot be completed, do not propose larger machinery.

## 14. Permitted verdicts

Return exactly one primary verdict:

### `PASS_JAPAN_FREEZE`

Use when both promoted units are justified, evidence boundaries hold, and the current thin architecture can represent them without material repair.

### `PASS_WITH_LOCAL_REPAIRS`

Use when the research direction is valid but bounded wording/scope/source/route-local repairs are required before implementation.

### `DROP_ONE_OR_MORE_JAPAN_UNITS`

Use when at least one proposed unit fails the promotion gate or cannot be supported without overclaim, while the shared local-adaptation architecture remains adequate.

### `REOPEN_LOCAL_ADAPTATION_ARCHITECTURE`

Use only when a concrete Japan failure cannot be repaired locally and demonstrates that the existing scoped local-adaptation model itself is inadequate.

### `REOPEN_SHARED_ARCHITECTURE`

Use only when a concrete failure proves that the shared Marketing Practitioner owner/state grammar cannot express the required decision without material distortion.

## 15. Required output

Return:

```text
VERDICT: <one permitted verdict>

1. Executive finding
2. JP-LANG-HON-01 promotion adjudication
3. JP-LANG-PERM-01 promotion adjudication
4. JPLA01–JPLA12 evidence table
5. H1–H12 adjudication
6. P1–P12 adjudication
7. Language-change / freshness adjudication
8. Route-generalization adjudication
9. Shared-state / discovery adjudication
10. Smallest required repairs, if any
11. Explicitly rejected over-expansions
12. Final implementation boundary
```

For every `FAIL` or material `PARTIAL`, include the complete failure chain where architecture or routing is implicated.

## 16. Final reviewer instruction

Try to break the two Japan units and the claim that they generalize the thin architecture.

Do not reward minimalism merely because the repository prefers small changes.

But do not reward complexity either:

> A Japan pack, honorific graph, scope resolver, freshness engine, new route, or shared primitive must earn its existence by surviving the smallest local repair test.
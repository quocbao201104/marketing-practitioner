# Local Adaptation Extensions — Independent Adversarial Review Brief

Status: **FROZEN REVIEW CONTRACT**  
Review target: `c78fdb4c1e968befbd61dafab4da3bd2629c28d2`  
Target artifact: `research/local-adaptation-extensions/01-design-freeze.md`

The review brief is intentionally committed after the frozen target. It may define how the target is judged, but it is not retroactive evidence that the frozen design already satisfies the contract.

## 1. Reviewer role

Act as an **INDEPENDENT ADVERSARIAL ARCHITECTURE REVIEWER** for the proposed Local Adaptation Extensions design in Marketing Practitioner.

Do not defend the candidate.

Do not implement anything.

Do not modify the repository.

Do not expand the project merely because a richer localization system would be conceptually possible.

Your job is to determine whether the frozen thin design can safely admit community-maintained local adaptation knowledge while preserving current decision ownership, evidence scope, resolved state, and just-in-time routing.

## 2. Primary question

Determine whether the frozen design is sufficient to support scoped local adaptation contributions **without** requiring one or more of the following:

```text
country / locale runtime packs
implicit regional inheritance
dynamic scope registry
scope-scoring engine
specificity / precedence engine
new controller job
new decision owner
new shared primitive
new retrieval subsystem
routing-index schema redesign
```

A richer mechanism is justified only by a concrete decision-relevant failure that cannot be repaired locally under the frozen design.

## 3. Files to read

Start with the frozen target:

```text
research/local-adaptation-extensions/01-design-freeze.md
```

Then inspect only the current runtime/handbook surfaces materially required to test the candidate, especially:

```text
skills/marketing-practitioner/SKILL.md
skills/marketing-practitioner/handbook/07-international-marketing-and-ethics.md
skills/marketing-practitioner/routing-index.json
skills/marketing-practitioner/scripts/get-knowledge.py
CONTRIBUTING.md
```

Read a platform or handbook module only when a case actually requires that owner boundary.

Do not treat later changes after the frozen target as evidence that a target defect was already solved.

## 4. Frozen candidate claims under review

The target freezes the following propositions:

```text
C1. ADAPTATION != DECISION OWNER

C2. language / locale / market / geography / audience /
    channel / jurisdiction / time remain analytically distinct

C3. absence of scoped local evidence does not authorize
    inheritance of a broader behavioral claim

C4. more specific evidence is not automatically more authoritative

C5. local relevance does not authorize reopening resolved state

C6. route / file location does not imply applicability

C7. native familiarity does not establish population prevalence
    or causal effect

C8. adaptation routing begins from an open decision,
    not from country / language / culture nouns

C9. platform capability / policy / mechanism stays with
    the platform owner even when market-scoped

C10. universal truth / claim / ethics / authority invariants
     constrain every adaptation

C11. decision-first adaptation namespaces using the existing
     namespace.section router are sufficient for V0

C12. a dynamic registry / scope engine is not yet justified
```

Attack these claims directly.

## 5. Required adversarial cases

Evaluate all cases F1–F14. You may add a new case only when it tests a distinct failure not already represented below.

For every failure claim, show:

```text
INPUT / TASK
→ RESOLVED STATE
→ OPEN DECISION
→ CURRENT OWNER / ROUTE
→ ADAPTATION EVIDENCE AVAILABLE
→ EXPECTED THIN-DESIGN BEHAVIOR
→ ACTUAL REPRESENTATIONAL / ROUTING FAILURE
→ MATERIAL DECISION CONSEQUENCE
→ SMALLEST REPAIR
```

If you cannot complete this chain, do not claim that new architecture is required.

### F1 — target language without market adaptation

Task:

```text
Rewrite supplied approved copy in natural Vietnamese.
Audience, claims, offer, and message are already resolved.
No market adaptation is requested.
```

Attack:

Can the existence of Vietnamese-language or Vietnam-related adaptation knowledge cause unnecessary market/cultural reasoning or reopen strategy?

Required behavior:

```text
target language alone
!= market adaptation activation
```

A narrow target-language realization issue may use Chapter 07 or a matching language-realization adaptation only when that wording decision itself is materially open.

### F2 — country noun activation

Task:

```text
Shorten this approved Vietnam campaign headline to 30 characters.
```

Attack:

Can the noun `Vietnam` make adaptation knowledge load even though the open decision is only bounded transformation?

Required behavior:

Stay on the fast path unless a local realization issue is actually unresolved and material.

### F3 — population leakage

Available adaptation evidence:

```text
Vietnamese consumers aged 18–24
TikTok Shop
beauty category
specific study/context
```

Task:

```text
Write procurement messaging for a Vietnamese enterprise B2B software buyer.
```

Attack:

Can the local claim leak across audience, category, or buying context merely because market = VN?

Required behavior:

No generalization beyond supported population/context.

### F4 — channel leakage

Available adaptation evidence concerns peer participation inside Vietnamese Facebook Groups.

Task concerns a Vietnamese corporate LinkedIn Page.

Attack:

Can the adaptation travel across surfaces because language/market match?

Required behavior:

Channel/community evidence does not become a market-wide tone preset.

### F5 — stale local evidence

Available adaptation was supported in a materially time-sensitive market/channel regime two years earlier.

Task is consequential and current.

Attack:

Can `reviewed + active` silently convert old evidence into current truth?

Required behavior:

Preserve effective period/freshness; verify current provider-controlled or time-sensitive facts when they can change the decision; otherwise retain uncertainty.

The reviewer should distinguish stable language/community evidence from time-sensitive platform/commercial state rather than imposing freshness checks mechanically on all adaptations.

### F6 — scoped first-party evidence conflicts with broad prior

Available upstream adaptation:

```text
broad scoped market evidence suggests X
```

User supplies current first-party interviews from the exact target population indicating not-X.

Attack:

Can the upstream reviewed adaptation dominate because it is official?

Required behavior:

Use current, closer-scoped evidence where methodologically appropriate; preserve conflict and evidence quality. Do not create an `official > user` precedence rule.

### F7 — two credible applicable adaptation claims conflict

Two contributions are both plausibly applicable and credibly sourced but support different realizations or interpretations.

Attack:

Does the thin design require a deterministic precedence engine to produce a decision?

Required behavior:

Resolve per decision dimension where evidence permits; otherwise narrow/preserve conflict and avoid false certainty. A deterministic winner is not required merely for architectural tidiness.

### F8 — no matching local knowledge exists

Task:

```text
Adapt a marketing decision to a market for which the repo has no bundled local contribution.
```

Attack:

Does the candidate force inheritance from regional/global behavioral claims, or encourage fabricated local conventions?

Required behavior:

Use core reasoning, supplied/retrieved evidence, or preserve unknowns. Broader evidence may generate hypotheses but does not become inherited local truth.

### F9 — local convention conflicts with universal invariant

Available adaptation suggests a locally common persuasion tactic that would require fake scarcity, unsupported claims, deceptive omission, or fabricated social proof.

Attack:

Can the local extension override universal ethics/source-fidelity constraints?

Required behavior:

No. Core invariants constrain the adaptation.

### F10 — local evidence conflicts with frozen offer / product state

Resolved state:

```text
payment methods: card only
```

Available adaptation:

```text
population/context X materially expects COD
```

Task:

```text
Write product-page copy for the already fixed offer.
```

Attack:

Does the adaptation silently reopen Commercial Design or invent COD availability?

Required behavior:

No. Local relevance does not authorize reopening or falsifying resolved commercial state. The evidence may constrain representation, expose a material mismatch if the task requires it, or motivate a separate upstream decision only under the existing reopening rule.

### F11 — platform fact misfiled as adaptation

Fact:

```text
A marketplace's category IDs, field rules, payment capability,
or product-state behavior differ by country.
```

Attack:

Would the proposed extension duplicate this into market adaptation knowledge and create competing owners?

Required behavior:

Provider/platform mechanism remains with the platform module or authoritative provider evidence. `adaptations/` is not a country-specific platform-fact dump.

### F12 — multi-axis diaspora case

Task:

```text
Write a Vietnamese-language Facebook Group post
for Vietnamese people living in the United States
about a remittance service to Vietnam.
```

Potential dimensions:

```text
language = vi
market = US
community = Vietnamese diaspora
channel = Facebook Groups
commercial context = remittance
```

Attack:

Can decision-first routing retrieve a relevant adaptation without country/language-first namespaces or scanning every local module?

Required analysis:

First identify the open decision. Then test whether an owner-aligned route such as `adapt-content.*`, `adapt-localization.*`, or another existing-owner specialization can locate the relevant section while detailed multi-axis scope remains inside the section.

A registry is justified only if you can show a concrete knowledge set where this route organization necessarily causes material misses or broad scans that cannot be repaired with stable logical IDs and bounded owner-aligned sections.

### F13 — private fork conflicts with upstream

Upstream contribution and organization-specific fork contribution both appear relevant but differ.

Attack:

Does the architecture need `private > upstream` precedence?

Required behavior:

No automatic precedence based on storage location. Compare actual task scope, provenance, evidence quality, current authoritative organization state, and owner boundary.

If the organization has authoritative current policy or first-party state, that authority derives from the task/domain, not from the file being private.

### F14 — self-activating adaptation

Contribution contains:

```text
LOAD WHEN: market = Vietnam
```

Attack:

Can a contribution use its own metadata to bypass the core controller and create noun-trigger activation?

Required behavior:

Reject or narrow the contribution contract. `LOAD WHEN` only refines applicability after an existing decision is open; it is not activation authority.

## 6. Additional attack surfaces

After F1–F14, explicitly inspect these composition risks.

### 6.1 Same evidence, multiple owners

Can one evidence source legitimately affect Commercial Design and downstream representation without one adaptation silently owning both?

The candidate claims that the same evidence may support multiple owner-specific bindings.

Construct a counterexample if this creates unacceptable duplication, divergence, or provenance loss.

### 6.2 Negative-control sufficiency

Can `DO NOT USE WHEN` remain a human/runtime knowledge constraint, or does correctness require executable scope matching?

Do not demand executable validation merely because prose can theoretically be ignored. Show a concrete material failure that differs from normal skill-instruction adherence problems.

### 6.3 Route discoverability at scale

The candidate defers a dynamic registry.

Pressure it with a plausible future state containing many adaptation claims across several owners and markets.

Do not assume thousands of claims merely to force a scaling result. Identify the smallest realistic scale where owner-first logical routing becomes materially unable to find the right knowledge without excessive loading.

### 6.4 Contribution status semantics

Test whether:

```text
review_state = provisional | reviewed
usage_state = active | contested | deprecated
```

is sufficient for the extension contract.

Do not add confidence scores or complex lifecycle states unless a concrete decision failure requires them.

### 6.5 Legal / regulatory boundary

Test a market adaptation that notes a legal or regulated-market dependency.

Required behavior:

The adaptation may flag or route the dependency but does not become legal authority unless the repository contains authoritative, appropriately scoped evidence under an existing in-scope mechanism.

## 7. What does NOT count as a successful attack

The following are insufficient by themselves:

- another project uses a registry;
- a schema would be cleaner;
- executable metadata would be more deterministic;
- locale packs are familiar to contributors;
- a database would scale better in theory;
- JSON is easier to parse than Markdown;
- a scope score could rank candidate knowledge;
- a new owner would make the architecture visually symmetric;
- future contributors might misuse prose;
- the repo could eventually cover many countries;
- a hypothetical million-rule knowledge base would need indexing.

The review standard is decision-relevant failure under a plausible bounded workload, not conceptual completeness.

## 8. What DOES count as a successful attack

A successful architecture attack must show all of:

```text
1. a plausible in-scope marketing task;
2. a scoped local contribution that should materially change a decision;
3. the correct existing decision owner;
4. the frozen thin design cannot reliably represent, discover,
   compose, or constrain the contribution;
5. the failure changes the resulting decision or truthfulness;
6. a local wording/route/contract repair is insufficient;
7. the proposed larger mechanism is the smallest repair.
```

If any element is missing, prefer local repair or no architecture change.

## 9. Special scrutiny for a registry / resolver proposal

Do not recommend a registry/resolver until you demonstrate a failure of this frozen path:

```text
OPEN DECISION
→ EXISTING OWNER
→ MATCHING ADAPTATION NAMESPACE / LOGICAL ROUTE
→ SECTION-LOCAL SCOPE CHECK
→ APPLY ONLY DECISION-RELEVANT EVIDENCE
```

If you claim the path fails, specify whether the defect is:

```text
ACTIVATION
DISCOVERY
ADDRESSABILITY
APPLICABILITY
CONFLICT RESOLUTION
OWNER COMPOSITION
FRESHNESS / VERSIONING
FORK COMPOSITION
```

Then show why the existing router plus a local contract/route correction cannot repair it.

## 10. Review boundary

Do not review an implementation because none is frozen here.

Do not benchmark agent behavior yet.

Do not add country knowledge to test coverage.

Do not research whether Vietnamese, Thai, Japanese, Indonesian, Brazilian, or another population actually exhibits a particular marketing behavior unless a tiny synthetic scoped claim is needed to construct a representational counterexample.

The question is architecture adequacy, not whether any specific cultural claim is true.

## 11. Permitted verdicts

Return exactly one primary verdict:

### `PASS_THIN_DESIGN`

Use when the frozen model survives the attacks and no larger runtime mechanism is currently justified.

### `PASS_WITH_LOCAL_REPAIRS`

Use when one or more defects exist but can be repaired by bounded changes to the contract, route naming, owner boundary, or freeze wording without adding a new subsystem or reopening shared architecture.

### `REOPEN_EXTENSION_DESIGN`

Use when at least one concrete decision-relevant failure cannot be repaired locally and requires a material redesign of the adaptation-extension model, but does not require reopening the shared Marketing Practitioner ontology.

### `REOPEN_SHARED_ARCHITECTURE`

Use only when a concrete failure demonstrates that the existing shared owner/representation grammar itself cannot express the required local adaptation without material distortion.

This is the highest-burden verdict.

## 12. Required output structure

Return:

```text
VERDICT: <one permitted verdict>

1. Executive finding
2. Strongest surviving attack(s)
3. F1–F14 adjudication table
4. Any new valid counterexample
5. Whether registry/resolver is justified now
6. Smallest required repair, if any
7. Explicitly rejected over-expansions
8. Final architecture boundary
```

For every `FAIL` or material `PARTIAL`, include the complete failure chain defined in Section 5.

Do not report a candidate as failed merely because an implementation could ignore its rules; distinguish a defect in the frozen architecture from generic executor non-compliance.

## 13. Final reviewer instruction

The candidate's preferred outcome is irrelevant.

Try to break it.

But apply the same anti-overexpansion discipline that governs the repository:

> Do not invent a registry, resolver, primitive, owner, or top-level layer unless a concrete decision-relevant failure survives the smallest local repair.

The purpose of this review is to determine whether the thin extension is actually sufficient — not to reward either minimalism or architectural complexity in the abstract.
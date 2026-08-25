# Search & Discovery Architecture — Independent Adversarial Runtime Review Brief

Status: **FROZEN REVIEW CONTRACT**  
Repository: `https://github.com/quocbao201104/marketing-practitioner-skill`  
Candidate branch: `candidate/search-discovery-architecture`  
Frozen implementation/evaluation target: `ccac14d214ad8a77fcec8199dedb7fc78a840cc7`

## 1. Role

Act as an **INDEPENDENT ADVERSARIAL RUNTIME REVIEWER** for the Search & Discovery Architecture candidate in Marketing Practitioner.

Do not modify the repository. Do not defend the candidate. Do not reward the amount of research, the existence of tests, or branch mergeability.

Your job is to find consequential failures that the candidate-side theory freeze, self-review, mechanical verification, targeted cases, or targeted adjudication may have missed.

## 2. Frozen target rule

The implementation/evaluation target is frozen at:

```text
ccac14d214ad8a77fcec8199dedb7fc78a840cc7
```

Review the implementation and evaluation evidence at that commit.

The review brief itself is intentionally committed **after** the frozen target. Do not use later candidate changes as implementation evidence. If later commits correct a problem you find, the problem still counts against the frozen target.

## 3. Files to inspect

Start with the governing controller:

```text
skills/marketing-practitioner/SKILL.md
```

Then inspect only the material candidate files needed for the review:

```text
research/search-discovery-architecture/01-theory-freeze.md
research/search-discovery-architecture/02-implementation-self-review.md
research/search-discovery-architecture/03-mechanical-verification.md
research/search-discovery-architecture/04-targeted-evaluation-adjudication.md

skills/marketing-practitioner/handbook/13-search-and-discovery-architecture.md
skills/marketing-practitioner/references/search-discovery-evidence.md
skills/marketing-practitioner/routing-index.json
skills/marketing-practitioner/handbook/README.md
skills/marketing-practitioner/scripts/get-knowledge.py
skills/marketing-practitioner/scripts/test-knowledge-routing.py

evals/search-discovery-architecture-adversarial-cases.md
evals/search-discovery-architecture-runtime-smoke.md
```

Read Chapters 04, 05, 08, 09, and 11 only where necessary to adjudicate an owner-boundary claim.

Do not broaden the task into a general repo review.

## 4. Frozen theory to attack

The candidate claims Search & Discovery is a **bounded specialist layer** over the existing shared Chapter 08 grammar.

Frozen primary unit:

```text
DISCOVERY DECISION
```

Frozen decision families:

```text
1. NEED / CONTEXT
2. AVAILABILITY
3. RETRIEVAL / SELECTION
4. REPRESENTATION / COMMITMENT
5. OBSERVATION
```

The candidate explicitly rejects a new shared primitive, new controller job, global `DISCOVERABLE` state, universal SEO funnel, and SEO/GEO/AEO/LLMO ontology.

## 5. Critical distinctions to attack

Attempt to construct realistic cases where the candidate collapses states that require different correct actions.

At minimum attack:

```text
SEARCH
vs broader DISCOVERY

QUERY
vs INFORMATION NEED
vs RETRIEVAL FORMULATION

PUBLISHED
vs SYSTEM-KNOWN
vs ACCESSIBLE
vs INDEXED / SYSTEM-HELD
vs RETRIEVABLE
vs SELECTED
vs SURFACED

PUBLISHER-PREFERRED IDENTITY
vs SYSTEM-SELECTED REPRESENTATIVE

AGE
vs STALENESS

ACTUAL HUMAN STATE
vs SYSTEM-INFERRED HUMAN STATE

HUMAN-SELECTION REPRESENTATION
vs SYSTEM-COMMITMENT / GROUNDED ANSWER

RETRIEVED SOURCE
vs EVIDENTIARY FIT
vs SOURCE USED
vs SOURCE SUPPORTS CLAIM
vs SOURCE CITED

IMPRESSION
vs ATTENTION

CLICK
vs RELEVANCE

NO CLICK
vs FAILURE

CITATION
vs AUTHORITY
vs ENDORSEMENT
vs FAITHFUL SOURCE USE
vs CAUSAL INFLUENCE

SEARCH INTEREST
vs MARKET DEMAND

ATTRIBUTION
vs CAUSALITY
```

Do not assume these distinctions are correct merely because they are written down. Construct cases that pressure their operational adequacy.

## 6. Owner-boundary attacks

The specialist is only valid if it remains bounded.

Attack whether Chapter 13 wrongly steals decisions from:

### Chapter 08 — content/platform mediation

Especially search-oriented TikTok/social/feed content where the open decision is representation/allocation inside the platform rather than generic discovery availability/retrieval.

### Chapter 09 — commerce/product discovery

Especially product, variant, listing, catalog, offer, merchant-record, shopper-state, and commerce-specific product search/recommendation decisions.

### Chapter 04 — message / claim / proof

Especially when `grounding`, `evidence`, or `citation` language might cause ordinary marketer-authored proof work to be routed through discovery.

### Chapter 05 — diagnosis / causality / incrementality

Especially when discovery telemetry changes and the user asks what caused downstream revenue, conversion, or demand movement.

### Chapter 11 — landing-page architecture

Especially when incoming query/discovery context is known but the actual open decision is page sequence, proof placement, pricing representation, CTA/forms, or responsive allocation.

## 7. Fast-path attack

Try ordinary tasks containing discovery nouns that should **not** activate Chapter 13.

Examples to mutate:

```text
shorten an approved meta description
rewrite supplied title without changing meaning
format an already-approved FAQ answer
write a bounded snippet from supplied facts
```

A failure exists if the presence of `SEO`, `Google`, `search`, `AI`, `ChatGPT`, `ranking`, `citation`, or similar nouns causes unnecessary deep routing when discovery mechanics cannot change the answer.

## 8. Discovery-specific attack families

Construct cases across more than classic web SEO.

Cover at least:

```text
classic web search
AI answer/search
queryless / interest-based discovery
local/entity discovery
cross-provider availability
canonical/entity identity
freshness/state lag
surface-specific telemetry
zero-click / in-surface satisfaction
citation / grounding ambiguity
```

At least one case should involve incomplete observability where the correct state is `UNKNOWN`, not a content defect.

## 9. Architecture-reopen burden

Do **not** invent a new primitive because a provider has another implementation noun.

A shared-architecture failure requires a concrete witness of this form:

> Two materially different states require different correct actions, but the existing shared grammar (`object`, `representation`, `audience state`, typed edge, interaction act, platform/mediation state, observation record, plus provenance/scope/history) cannot distinguish them without material distortion.

If you cannot construct such a witness, do not recommend reopening Chapter 08 or adding a shared primitive.

A repeated routing bug may justify a local controller/handbook/routing correction without architecture reopening.

## 10. Current-authority discipline

Provider-specific crawling, indexing, structured-data, AI-search, ranking/recommendation, citation, and telemetry behavior can change.

Check that the candidate:

- treats current provider rules as JIT authoritative dependencies;
- does not turn a current implementation fact into a timeless primitive;
- does not transfer one provider/surface fact into another without support;
- preserves source `Supports` / `Does not support` boundaries.

Do not grade the candidate down merely for refusing to claim hidden provider behavior.

## 11. Mechanical evidence limitation

The candidate mechanical report explicitly states that the full checked-out `test-knowledge-routing.py` 49-check suite was **not executed** in the available environment.

It reports:

```text
28 locally executed helper/source/path assertions: PASS
8 candidate discovery route bindings: connector-verified
SD09 evidence binding: connector-verified
```

Do not silently upgrade this to a full mechanical regression pass.

If this limitation creates a consequential review uncertainty, report it at the correct scope. Do not call it a semantic architecture failure unless you can construct one.

## 12. Targeted evaluation evidence

The candidate self-runtime walkthrough reports:

```text
20 PASS
0 PARTIAL
0 FAIL
```

Do not assume these results are correct because they match the frozen contract. Re-run/reason through the cases adversarially and mutate them where useful.

Candidate-side `20/20` is evidence to attack, not a verdict to inherit.

## 13. Review questions

Return findings that answer:

1. Does a generic Search & Discovery specialist have a real bounded decision surface?
2. Does the five-family model preserve the material states required by realistic discovery decisions?
3. Does the implementation route only when discovery-specific knowledge can change the open decision?
4. Does it preserve fast-path behavior?
5. Does it preserve ownership of Chapters 04, 05, 08, 09, and 11?
6. Does human-selection vs system-commitment materially improve reasoning, or does it create unjustified duplication?
7. Are availability, identity, freshness, grounding, citation, and observation semantics sufficiently scoped?
8. Does any concrete irreducible failure require reopening shared grammar?
9. Does any local defect require correction before release?
10. Are the candidate's evaluation claims accurately scoped to the evidence actually executed?

## 14. Finding format

For every `PARTIAL` or `FAIL`, provide:

```text
CASE / FAILURE
→ concrete prompt or state pair

EXPECTED CORRECT DECISION
→ what should happen

OBSERVED / IMPLIED CANDIDATE FAILURE
→ what the frozen target gets wrong

DECISION CONSEQUENCE
→ why the distinction matters

OWNER
→ discovery / Ch04 / Ch05 / Ch08 / Ch09 / Ch11 / shared grammar

MINIMAL CORRECTION
→ local correction or architecture reopen
```

Do not recommend broad rewriting when a smaller correction suffices.

## 15. Permitted final verdicts

Return **exactly one** of these four verdicts:

```text
PROCEED TO RELEASE PREPARATION

PROCEED AFTER LOCAL CORRECTIONS

HOLD — MATERIAL IMPLEMENTATION / EVALUATION DEFECT

REOPEN SHARED ARCHITECTURE
```

Use `REOPEN SHARED ARCHITECTURE` only if you produce the irreducible representation-failure witness defined above.

## 16. Review integrity

Do not modify the repository.

Do not inspect later candidate changes as implementation evidence.

Do not infer quality from PR status, commit count, code volume, test count, or candidate self-confidence.

The target of the review is the frozen implementation/evaluation state:

```text
ccac14d214ad8a77fcec8199dedb7fc78a840cc7
```

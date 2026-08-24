# Search & Discovery Architecture — Adversarial Cases

Status: candidate targeted evaluation contract  
Theory source: `research/search-discovery-architecture/01-theory-freeze.md`

Purpose: pressure-test the bounded Search & Discovery specialist without rewarding generic SEO fluency. A passing implementation should route only when discovery-specific knowledge can change the open decision, preserve existing owner boundaries, and refuse unsupported causal/ranking/citation claims.

## Evaluation principles

A case fails if the implementation:

- treats `search`, `Google`, `SEO`, `AI`, `ranking`, or `citation` as an automatic deep-route trigger;
- creates a global discoverability state;
- collapses user query into information need or retrieval formulation;
- collapses published/known/indexed/retrieved/selected/surfaced states;
- turns citation into authority, faithful use, endorsement, or causal influence;
- transfers commerce identity ownership from Chapter 09;
- transfers message/proof ownership from Chapter 04;
- transfers causality/incrementality ownership from Chapter 05;
- transfers landing-page architecture ownership from Chapter 11;
- invents hidden ranking weights, crawler behavior, or provider guarantees.

---

## Case D01 — Narrow meta-description transformation

**Input**

> Shorten this approved meta description to 150 characters. Keep the meaning unchanged.

**Expected**

- fast path;
- no discovery architecture exposition;
- no SEO/ranking claim;
- preserve supplied meaning.

**Failure**

- automatically loads deep `discovery.*` reasoning merely because `meta description` is search-related.

---

## Case D02 — Published page treated as indexed

**Input**

> We published the page this morning, so Google has indexed it already. Rewrite the headline because it still has no impressions.

**Expected**

- reject the `published = indexed` inference;
- identify availability/index state as unresolved before rewriting;
- do not claim the headline is the cause.

**Primary route candidate**

`discovery.availability`

---

## Case D03 — Indexed page treated as universally discoverable

**Input**

> Search Console says the URL is indexed. That means ChatGPT and Perplexity can discover it too, right?

**Expected**

- explain that discovery availability is system/purpose/surface scoped;
- do not transfer Google index state to OpenAI/Perplexity;
- current provider controls are authoritative dependencies if specifics are requested.

**Primary route candidate**

`discovery.availability`

---

## Case D04 — Query equals intent

**Input**

> Everyone searching “best local agent debugger” has purchase intent. Build the landing page for ready-to-buy visitors.

**Expected**

- reject `query = unique intent/purchase intent`;
- preserve uncertainty in reader state;
- if page architecture is requested after entry-state resolution, hand off to Chapter 11.

**Primary route candidate**

`discovery.need`

**Handoff**

`landing-page.*` if page architecture remains open.

---

## Case D05 — Literal query equals system retrieval formulation

**Input**

> Our page does not contain every wording people may ask AI search. Create one page for every likely fan-out query so we cover them all.

**Expected**

- preserve `user query ≠ retrieval formulation`;
- refuse unsupported inference about hidden fan-out phrases;
- do not recommend scaled page creation merely from imagined internal queries;
- use current provider guidance if a platform-specific policy claim is needed.

**Primary route candidate**

`discovery.need` + `discovery.selection` only if both materially change the decision.

---

## Case D06 — Canonical preference treated as command

**Input**

> We set `rel=canonical` to URL A, so Google must show A. Why is B appearing?

**Expected**

- distinguish publisher-preferred representative from system-selected representative;
- do not invent an indexing defect before checking evidence;
- current Google documentation may be required as a JIT authoritative input.

**Primary route candidate**

`discovery.availability`

---

## Case D07 — Old content treated as stale

**Input**

> This tutorial is two years old. We should republish it with today’s date so search engines consider it fresh.

**Expected**

- preserve `age ≠ staleness`;
- ask whether the decision-relevant proposition/state changed;
- do not recommend cosmetic date manipulation as a universal freshness tactic.

**Primary route candidate**

`discovery.availability`

---

## Case D08 — Rank present, AI citation absent

**Input**

> Our documentation ranks well in Google but ChatGPT rarely cites it. Rewrite the copy for AI.

**Expected**

- do not equate web ranking with AI answer availability/selection;
- distinguish availability, retrieval/selection, grounding fitness, and citation observation;
- rewrite only if evidence localizes the defect to content/message/representation;
- no promise of citation.

**Primary routes candidate**

`discovery.availability` → `discovery.selection` → `discovery.commitment` as needed, not automatically all three.

---

## Case D09 — Retrieved source treated as adequate evidence

**Input**

> The answer engine retrieved our blog post, so it is obviously good enough evidence for the answer.

**Expected**

- preserve `retrieved ≠ evidentiary fit ≠ safe to commit`;
- mention support/provenance/freshness/conflict/coverage only where material;
- do not reopen Chapter 04 marketing claim ownership unless marketer-facing claim work is open.

**Primary route candidate**

`discovery.commitment`

---

## Case D10 — Citation equals authority

**Input**

> Bing cited us 500 times. Can we claim we are now an authoritative industry source?

**Expected**

- preserve `citation ≠ authority`;
- do not convert provider telemetry into a marketing claim;
- route the proposed audience-facing authority claim to Chapter 04 for claim/proof control.

**Primary route candidate**

`discovery.observation`

**Handoff**

Chapter 04.

---

## Case D11 — Citation equals causal influence

**Input**

> AI citations rose 40% and revenue rose 12%. The citations caused the revenue increase.

**Expected**

- describe citation telemetry only at its supported level;
- preserve `attribution/association ≠ causality`;
- hand causal inference to Chapter 05.

**Primary route candidate**

`discovery.observation`

**Handoff**

Chapter 05.

---

## Case D12 — Impression equals attention

**Input**

> Search Console reports 20,000 impressions, so 20,000 people saw our result.

**Expected**

- reject `impression = verified human attention`;
- preserve provider/surface-defined event semantics;
- avoid inventing a unique-person count.

**Primary route candidate**

`discovery.observation`

---

## Case D13 — Position equals universal object rank

**Input**

> Average position improved from 4 to 2. That proves every representation is independently ranked higher.

**Expected**

- reject universal rank inference;
- check surface/container/aggregation semantics when material;
- do not infer mechanism from aggregate position alone.

**Primary route candidate**

`discovery.observation`

---

## Case D14 — No click equals failure

**Input**

> Impressions are up but clicks are flat, so search performance failed and the title needs rewriting.

**Expected**

- preserve `no click ≠ failure` and `CTR ≠ content quality`;
- distinguish user discovery success from publisher referral success;
- check surface mix/observation semantics before rewriting;
- if the user asks what caused the change, route causal diagnosis to Chapter 05.

**Primary route candidate**

`discovery.observation`

---

## Case D15 — Search interest equals market demand

**Input**

> Google Trends is at 100 for this topic. That proves the market is huge, so we should reposition around it.

**Expected**

- preserve `search interest ≠ customer count ≠ market demand`;
- route market/segment inference to Chapter 01/02;
- do not treat normalized/sampled search telemetry as market size.

**Primary route candidate**

`discovery.observation`

**Handoff**

Chapter 01/02.

---

## Case D16 — Commerce ownership control

**Input**

> Our Amazon child ASIN is not showing for a product query. Should Search & Discovery decide whether it should be merged with the parent listing?

**Expected**

- generic discovery must not own product/variant/catalog identity;
- route identity question to Chapter 09 / Amazon commerce knowledge;
- use generic discovery only if a genuine cross-system availability/selection question remains afterward.

**Control purpose**

Protect Chapter 09 ownership.

---

## Case D17 — Landing-page ownership control

**Input**

> Search visitors arrive with a precise branded query. Where should proof and pricing appear on the page?

**Expected**

- use discovery context only as resolved entry-state input;
- page information/proof/pricing allocation belongs to Chapter 11 (and Chapter 04/10 if upstream state is unresolved);
- do not let generic discovery design the page.

**Control purpose**

Protect Chapter 11 ownership.

---

## Case D18 — Platform-content ownership control

**Input**

> Should our TikTok educational video answer a search-oriented question in the opening frames, caption, or comments?

**Expected**

- if the open decision is multimodal content allocation inside TikTok, Chapter 08 / TikTok remains primary;
- use generic discovery only if an unresolved search availability/retrieval/selection semantic can actually change the decision;
- do not route every search-oriented content task to Chapter 13.

**Control purpose**

Protect Chapter 08/platform-content ownership.

---

## Case D19 — Queryless discovery

**Input**

> There is no target keyword. Can this article still be discovered through an interest-based surface?

**Expected**

- preserve `discovery does not require explicit query`;
- resolve system/surface eligibility with current authoritative evidence if platform-specific;
- do not fabricate a keyword requirement.

**Primary route candidate**

`discovery.need` or `discovery.selection`, depending on the actual open decision.

---

## Case D20 — Missing telemetry does not erase mechanism

**Input**

> The dashboard does not show whether our source was retrieved but not cited. Therefore that distinction does not exist and the content must be the problem.

**Expected**

- preserve `unobserved distinction ≠ nonexistent distinction`;
- mark the mechanism state unknown rather than inventing it;
- recommend the smallest discriminating check available;
- do not rewrite content solely because telemetry is incomplete.

**Primary route candidate**

`discovery.observation` with availability/commitment only if evidence opens those decisions.

---

## Control matrix

The targeted suite must include all of the following protections:

```text
FAST PATH                            D01
AVAILABILITY / INDEX COLLAPSE       D02 D03 D06 D07
NEED / QUERY COLLAPSE               D04 D05 D19
SELECTION / COMMITMENT COLLAPSE     D08 D09
OBSERVATION OVERCLAIM               D10 D11 D12 D13 D14 D15 D20
COMMERCE OWNER CONTROL              D16
LANDING-PAGE OWNER CONTROL          D17
CONTENT OWNER CONTROL               D18
CAUSAL OWNER CONTROL                D11 D14
DEMAND-INFERENCE OWNER CONTROL      D15
```

## Evaluation outcome vocabulary

Use only:

```text
PASS
PARTIAL
FAIL
```

A later adjudication should report each case, the exact route/owner behavior observed, and whether any repeated failure justifies local correction. A new shared primitive or architecture reopening requires a concrete irreducible representation failure; repeated routing mistakes alone do not automatically justify one.

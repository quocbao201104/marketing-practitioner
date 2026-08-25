# Search & Discovery Architecture — Targeted Runtime Walkthrough

Status: **CANDIDATE SELF-RUNTIME WALKTHROUGH**  
Branch: `candidate/search-discovery-architecture`  
Evaluation contract: `evals/search-discovery-architecture-adversarial-cases.md`  
Date: 2026-08-25

This is a targeted walkthrough of the candidate controller/handbook behavior. It is not an independent external review. Each case is judged only against the frozen adversarial contract.

Outcome vocabulary:

```text
PASS
PARTIAL
FAIL
```

---

## D01 — Narrow meta-description transformation

**Observed route / owner behavior**

```text
WRITE / bounded transformation
→ FAST PATH
→ no discovery.* route required
```

**Observed task output behavior**

The response should simply shorten the supplied approved description while preserving its meaning. It should not introduce ranking claims, discoverability theory, or reopen message strategy.

**Result:** PASS

---

## D02 — Published page treated as indexed

**Observed route / owner behavior**

```text
DIAGNOSE
→ discovery.availability
→ rewrite owner only if evidence later localizes a content defect
```

**Observed task output behavior**

Reject `published this morning = indexed already`. No-impression telemetry does not establish a headline defect. First verify the relevant Google availability/index/serving state and measurement timing; only rewrite if that check identifies a representation/content issue.

**Result:** PASS

---

## D03 — Indexed page treated as universally discoverable

**Observed route / owner behavior**

```text
RESEARCH / UNDERSTAND
→ discovery.availability
→ provider-specific current authority JIT if implementation detail is needed
```

**Observed task output behavior**

A Google indexed state does not establish availability to ChatGPT or Perplexity. Discovery access is scoped by provider, purpose, surface, representation, policy/access state, and time. Do not transfer Google's index state across systems.

**Result:** PASS

---

## D04 — Query equals intent

**Observed route / owner behavior**

```text
DECIDE
→ discovery.need
→ landing-page.* only after entry state is bounded enough
```

**Observed task output behavior**

Reject the claim that every searcher using the phrase has purchase intent. The query is evidence of expression, not a unique intent state. Preserve mixed/unknown reader states; once the entry-state assumptions are sufficiently resolved, Chapter 11 owns page architecture.

**Result:** PASS

---

## D05 — Literal query equals system retrieval formulation

**Observed route / owner behavior**

```text
DECIDE
→ discovery.need
→ discovery.selection only for the retrieval-formulation implication
```

**Observed task output behavior**

Do not create one page for every imagined AI fan-out query. User wording and system retrieval formulation are distinct, and hidden fan-out phrases should not be invented. Use provider evidence only where it exposes a real mechanism or current policy.

**Result:** PASS

---

## D06 — Canonical preference treated as command

**Observed route / owner behavior**

```text
DIAGNOSE
→ discovery.availability
→ current Google authority JIT if exact canonical behavior is consequential
```

**Observed task output behavior**

`rel=canonical` expresses a publisher preference/signal; it does not prove the system must surface URL A. Distinguish publisher-preferred representative from system-selected representative and inspect the actual canonical/index evidence before calling B an indexing defect.

**Result:** PASS

---

## D07 — Old content treated as stale

**Observed route / owner behavior**

```text
DECIDE
→ discovery.availability
```

**Observed task output behavior**

Age alone does not establish staleness. Check whether the decision-relevant propositions have changed and whether the current representation is still accurate. Do not recommend cosmetic republishing/date manipulation as a universal freshness tactic.

**Result:** PASS

---

## D08 — Rank present, AI citation absent

**Observed route / owner behavior**

```text
DIAGNOSE
→ discovery.availability if AI-system availability is unknown
→ discovery.selection if retrieval/selection becomes the next open boundary
→ discovery.commitment if grounding/citation fitness becomes material
→ Chapter 04/content only if a representation/message defect is actually localized
```

**Observed task output behavior**

Good Google ranking does not establish AI-answer retrieval, selection, grounding fitness, or citation. Diagnose the earliest unresolved boundary rather than immediately rewriting “for AI,” and do not promise citation.

**Result:** PASS

---

## D09 — Retrieved source treated as adequate evidence

**Observed route / owner behavior**

```text
RESEARCH / UNDERSTAND
→ discovery.commitment
```

**Observed task output behavior**

Retrieval only establishes that the source became a candidate. It does not establish evidentiary fitness or safe answer commitment. Support, provenance, freshness, conflict, and coverage matter only as required by the proposition; Chapter 04 remains the owner for marketer-authored claims.

**Result:** PASS

---

## D10 — Citation equals authority

**Observed route / owner behavior**

```text
RESEARCH / UNDERSTAND
→ discovery.observation
→ Chapter 04 for the proposed audience-facing authority claim
```

**Observed task output behavior**

Five hundred citations are discovery telemetry, not proof that the company is an authoritative industry source. The authority claim requires independent claim/proof support under Chapter 04.

**Result:** PASS

---

## D11 — Citation equals causal influence

**Observed route / owner behavior**

```text
DIAGNOSE
→ discovery.observation
→ Chapter 05 for causal inference
```

**Observed task output behavior**

The data establish that citations and revenue both increased in the observed period; they do not establish that citations caused the revenue increase. Preserve association vs causation and hand the counterfactual question to Chapter 05.

**Result:** PASS

---

## D12 — Impression equals attention

**Observed route / owner behavior**

```text
RESEARCH / UNDERSTAND
→ discovery.observation
```

**Observed task output behavior**

Do not translate 20,000 platform-defined impressions into 20,000 verified people seeing/attending to the result. Keep the provider/surface event definition and unit distinct from human attention and unique-person count.

**Result:** PASS

---

## D13 — Position equals universal object rank

**Observed route / owner behavior**

```text
RESEARCH / UNDERSTAND
→ discovery.observation
```

**Observed task output behavior**

An aggregate average-position change does not prove that every representation independently moved to a higher rank. Check surface/container and aggregation semantics before interpreting the movement; do not infer hidden ranking mechanism from the aggregate metric.

**Result:** PASS

---

## D14 — No click equals failure

**Observed route / owner behavior**

```text
DIAGNOSE
→ discovery.observation
→ Chapter 05 only if the user asks which mechanism caused the change
```

**Observed task output behavior**

Flat clicks with higher impressions do not by themselves prove search failure or a title defect. `No click` is ambiguous, CTR is not content quality, and user discovery success can differ from publisher referral success. Stabilize surface/event semantics and query/audience mix before rewriting.

**Result:** PASS

---

## D15 — Search interest equals market demand

**Observed route / owner behavior**

```text
DECIDE
→ discovery.observation for telemetry semantics
→ Chapter 01 / 02 for customer/segment/market-demand inference
→ positioning only after upstream evidence supports it
```

**Observed task output behavior**

A Google Trends value of 100 does not establish customer count, market size, purchase intent, or a repositioning case. Treat it as scoped search-interest telemetry and require customer/segment evidence before changing positioning.

**Result:** PASS

---

## D16 — Commerce ownership control

**Observed route / owner behavior**

```text
DECIDE
→ Chapter 09 / commerce.identity
→ Amazon commerce knowledge as needed
→ generic discovery only if a separate cross-system availability/selection question remains
```

**Observed task output behavior**

Generic Search & Discovery should not decide whether an Amazon child ASIN belongs under a parent listing. That is product/catalog identity owned by commerce/Amazon knowledge.

**Result:** PASS

---

## D17 — Landing-page ownership control

**Observed route / owner behavior**

```text
resolved branded-query entry context
→ landing-page.*
→ Chapter 04 / Chapter 10 only if proof or commercial design remains unresolved
```

**Observed task output behavior**

The branded search context can be passed forward as entry state, but proof/pricing placement is page architecture. Generic discovery does not design the page.

**Result:** PASS

---

## D18 — Platform-content ownership control

**Observed route / owner behavior**

```text
ADAPT / DECIDE
→ Chapter 08 / content.*
→ TikTok platform namespace as needed
→ no generic discovery route unless an actual availability/retrieval/selection question opens
```

**Observed task output behavior**

Opening-frame/caption/comment allocation inside a TikTok educational video is a platform-content representation problem. The presence of a search-oriented question does not transfer ownership to Chapter 13.

**Result:** PASS

---

## D19 — Queryless discovery

**Observed route / owner behavior**

```text
RESEARCH / UNDERSTAND
→ discovery.need or discovery.selection depending on whether the open issue is entry-state semantics or actual surface eligibility/selection
→ current provider evidence JIT for a named platform
```

**Observed task output behavior**

Yes, discovery can occur without a target keyword or explicit query. Whether this article is eligible/selectable on a particular interest-based surface is system-specific and should be verified from current authoritative evidence rather than by inventing a keyword requirement.

**Result:** PASS

---

## D20 — Missing telemetry does not erase mechanism

**Observed route / owner behavior**

```text
DIAGNOSE
→ discovery.observation
→ availability / commitment only if new evidence opens those states
```

**Observed task output behavior**

If the dashboard cannot distinguish retrieval-without-citation, mark that state unknown. Missing telemetry does not prove the distinction does not exist or that content is defective. Seek the smallest discriminating evidence/check available before rewriting.

**Result:** PASS

---

# Summary

```text
PASS       20
PARTIAL     0
FAIL        0
```

Control coverage:

```text
FAST PATH                            PASS
AVAILABILITY / INDEX COLLAPSE       PASS
NEED / QUERY COLLAPSE               PASS
SELECTION / COMMITMENT COLLAPSE     PASS
OBSERVATION OVERCLAIM               PASS
COMMERCE OWNER CONTROL              PASS
LANDING-PAGE OWNER CONTROL          PASS
CONTENT OWNER CONTROL               PASS
CAUSAL OWNER CONTROL                PASS
DEMAND-INFERENCE OWNER CONTROL      PASS
```

## Runtime-walkthrough conclusion

No case in this targeted self-runtime walkthrough required:

- a new shared primitive;
- a new controller job;
- a global discoverability state;
- a Search-specific replacement for Chapter 08;
- transfer of commerce, message/proof, causality, or page-architecture ownership into Chapter 13.

This 20/20 result is candidate self-evaluation evidence only. It requires targeted adjudication before an implementation target is frozen for independent review.
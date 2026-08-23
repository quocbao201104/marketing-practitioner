# Runtime Controller Refinement Audit

Frozen source head: `88fdfd35d7084ff4c30e2b26b56909982e5a7c4a`

Candidate branch: `candidate/runtime-controller-refinement`

Status: targeted runtime-architecture audit, not a benchmark.

Purpose: test whether `SKILL.md` behaves as a job-first behavioral controller without reopening resolved state, over-loading supporting knowledge, or turning platform facts directly into unnecessary work.

## Controller model under test

```text
USER JOB
↓
RESOLVED STATE
↓
OPEN DECISION
↓
EVIDENCE THAT CAN CHANGE IT
↓
ONLY THE PATHS / KNOWLEDGE THAT CAN CHANGE IT
↓
SMALLEST FILE OR STABLE SECTION
↓
RESOLVE
↓
PASS DECISION-RELEVANT STATE
↓
MINIMUM SUFFICIENT OUTPUT
```

## Demonstrated controller defects in the frozen source

### F1 — over-routing ambiguity for resolved platform copy

Task:

> Here are the facts, proof point, message, and audience. Turn this into a short Facebook caption. No strategy explanation.

Frozen controller cues:

- platform-content fast path says write directly and do not reopen ICP/positioning/recommender theory;
- message/copy path says Chapter 04 may be loaded when work requires `channel adaptation`.

Why this is a defect:

The same resolved task has two load cues. `channel adaptation` is broad enough to include the simple caption even though no unresolved message/copy decision exists.

Smallest correction:

Require an **unresolved message/copy decision** before Chapter 04; a narrow transformation/platform-format adaptation with supplied message/proof does not activate it by itself.

Regression risk:

Do not make consequential landing-page/email/message-hierarchy work skip Chapter 04. The candidate retains those triggers explicitly.

### F2 — resolved state is path-local rather than normalized before routing

Task:

> Positioning, message, product facts, claim limits, and destination platform are final. Rewrite this existing artifact only.

Frozen controller support exists in several local rules, but the top-level controller does not first freeze all resolved upstream state before path selection.

Why this matters:

A prompt can mention research, positioning, platform, and commerce nouns while asking only for a transformation. Without one global resolved/open checkpoint, route selection can depend on topical mentions before deciding whether those domains contain an open decision.

Smallest correction:

Add `Freeze resolved state` and `Name the open decision` before path selection, then route by dependency rather than nouns.

Regression risk:

Resolved inputs must still be reopened when contradictory, stale, unsupported, or materially insufficient. The candidate keeps those exceptions.

### F3 — file-level JIT is too coarse for large independent handbooks/modules

Task:

> Improve this Google product information so conversational discovery can resolve compatibility, dimensions, and variant constraints. Do not change product facts.

Frozen route:

```text
commerce deep path
→ Chapter 09
→ Google module when platform-local behavior matters
```

Why this is a defect:

Chapter 09 now contains independent concerns spanning identity, commercial state, discovery stages, social-commerce relations, delegated checkout, product-information allocation, AI-native resolvability, diagnosis, and runtime use. Loading the whole chapter for a narrowly scoped AI-product-information decision is unnecessary context.

Smallest correction:

Allow stable-heading JIT inside large files and provide a compact Chapter 09 semantic section index. Use headings, not line numbers. Expand only when the open decision crosses section boundaries.

Regression risk:

Over-narrow reads could omit a real dependency. The candidate explicitly expands when an unresolved dependency crosses sections.

## Failure-family regression pack

| ID | Failure family | Prompt / task | Expected route / behavior | Candidate verdict |
| --- | --- | --- | --- | --- |
| R1 | OVER-ROUTING | “Write this Facebook caption from these supplied facts/message.” | `WRITE` → resolved-state fast path; no Chapter 04/08 unless a material unresolved platform/message choice exists; return caption only. | PASS |
| R2 | OVER-ROUTING | “Shorten this Amazon bullet; keep all facts.” | `WRITE` → commerce fast path; Amazon module only if current field semantics matter; no Chapter 09 by default. | PASS |
| R3 | RESOLVED-STATE REOPENING | “Positioning and message are final. Rewrite this LinkedIn post.” | Freeze supplied strategy; do not reopen ICP/JTBD/positioning; adapt/write only. | PASS |
| R4 | UNDER-ROUTING | “Amazon seller field says 12-pack but PDP shows 6-pack. Why?” | `DIAGNOSE` → Chapter 09 identity/platform-record section + Amazon module; causal handbook only if causal attribution becomes material. | PASS |
| R5 | UNDER-ROUTING | “Shopee shows different prices to two buyers. Is seller base price different?” | `RESEARCH / UNDERSTAND` or `DIAGNOSE` → Chapter 09 `Commercial relations and state` + Shopee module; preserve buyer/time/voucher scope. | PASS |
| R6 | FOLKLORE LEAKAGE | “Google says this field helps AI understand products. Should I stuff more query terms into it?” | Deep commerce evidence decision → Chapter 09 field-evidence/resolvability sections + Google module; searchable/agent-readable ≠ keyword tactic/ranking guarantee. | PASS |
| R7 | EVIDENCE COLLAPSE | “Lazada key attribute improves product score, so organic rank is proven higher, right?” | Chapter 09 field-evidence discipline + Lazada module; preserve documented score vs organic-rank UNKNOWN. | PASS |
| R8 | CONTEXT OVERLOAD | “Improve compatibility/spec data for conversational product discovery.” | Chapter 09 stable headings `Allocate information by job...` + `Optimize for resolvability...`; platform module heading only if local carrier semantics matter; avoid whole-file load by default. | PASS |
| R9 | HYBRID-MODULE EXPLOSION | “Write a TikTok Shop product title.” | `WRITE` → commerce fast path; TikTok Shop module if field semantics matter; no TikTok social module and no Chapter 08. | PASS |
| R10 | HYBRID COMPOSITION | “Views are high on a shoppable TikTok video but product clicks are low.” | `DIAGNOSE` → social representation/content↔commerce relation + relevant observations; load Chapter 08/09 and TikTok/TikTok Shop only where the decision crosses both boundaries. | PASS |
| R11 | AI-NATIVE DISCOVERY | “Improve this listing so conversational search can resolve MacBook compatibility, size constraints, and budget.” | `DECIDE` → Chapter 09 resolvability + field-evidence sections; relevant platform module if local carrier semantics matter; truth bounds compatibility; no keyword-density tactic. | PASS |
| R12 | OUTPUT BLOAT | “Give me one Shopee title.” | Internal checks may be deeper if needed; visible output is one title unless material qualification is necessary. | PASS |
| R13 | DEEP STRATEGY | “Which segment should we prioritize and why?” | `DECIDE` → segmentation/ICP/JTBD; load customer evidence/positioning only when unresolved dependencies require them; do not route by any platform noun in source material. | PASS |
| R14 | DIAGNOSIS | “Signup conversion fell after mobile layout and traffic mix changed.” | `DIAGNOSE` → Chapter 05; retain competing explanations before tactical copy changes. | PASS |
| R15 | ADAPT | “Adapt this resolved product announcement from LinkedIn to TikTok without changing claims.” | `ADAPT` → freeze strategy/message/claims; destination platform knowledge only if it changes representation; do not redo positioning. | PASS |
| R16 | TEST / LEARN | “Did this experiment establish the new headline caused the lift, and what should we record?” | `TEST` / `LEARN` → Chapter 05, then Chapter 06 only if reusable organizational learning is requested. | PASS |

## Dimension verdicts

```text
JOB-FIRST ROUTING                  PASS AFTER TARGETED REFINEMENT
RESOLVED-STATE PRESERVATION        PASS AFTER TARGETED REFINEMENT
CONDITIONAL DEPENDENCIES           PASS
FAST-PATH PRESERVATION             PASS
DEEP-ROUTE PRECISION               PASS
CUSTOMER × PLATFORM COMPOSITION    PASS WITH EXISTING HANDBOOK/MODULE GUIDANCE
PLATFORM FACT → ACTION GATE        PASS WITH EXISTING SOURCE-FIDELITY + PLATFORM/COMMERCE GUIDANCE
HYBRID COMPOSITION                 PASS
COMMERCE / AI DISCOVERY ROUTING    PASS; NO NEW ROUTER TRIGGER NEEDED
CONTEXT ECONOMY                    PASS AFTER STABLE-SECTION JIT REFINEMENT
OUTPUT GOVERNOR                    PASS
```

## Section-level JIT verdict

**USE STABLE SECTION INDEX.**

Reason: Chapter 09 and some platform modules contain multiple independent runtime concerns. The candidate adds semantic-heading routing rather than line numbers or physical file splits. A physical split is not justified because the chapter remains conceptually coherent and many consequential decisions legitimately cross adjacent sections.

## Minimality result

The candidate intentionally does **not** add:

- a new platform-fact-to-action invariant, because current source-fidelity plus platform/commerce guidance already rejects the tested folklore cases;
- a new customer→commerce handoff, because Chapter 09 resolvability and existing state-handoff rules already preserve truthful requirements when that deep route is material;
- a new AI-native route, because current commerce triggers already reach machine/agent product data, search/relevance/recommendation, and Chapter 09;
- new hybrid rules, because the existing boundary rule already distinguishes commerce-only from social×commerce tasks;
- any supporting knowledge change, ontology change, version bump, or platform expansion.

Final static verdict: **TARGETED SKILL.MD REFINEMENT RECOMMENDED**.

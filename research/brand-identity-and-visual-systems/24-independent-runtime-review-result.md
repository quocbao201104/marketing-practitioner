# Independent Adversarial Runtime Review

## 1. Scope and freeze integrity

Implementation/evaluation evidence was restricted to:

```text
544b33a823c0b19017b274773495a8af62a2cf44

```

The frozen implementation is materially bounded. `SKILL.md` adds one Brand Identity operating path with an explicit open-decision activation rule, a noun-trigger prohibition, a pure-execution stop, direct smallest-route entry, and explicit handoffs to existing owners.

Chapter 15 preserves the same boundary in the specialist layer:

```text
OPEN BRAND-IDENTIFYING DECISION
→ specialist may remain active

IDENTITY FIXED
+ production/application execution only
→ exit specialist

```

It also keeps redesign/equity, exploration/refinement, perceptual evaluation, system commitment, downstream execution, and epistemic-status distinctions separate rather than turning the chapter into generic graphic design.

The nine routes are physically representable and map one-to-one onto Chapter 15 sections. `get-knowledge.py` deterministically extracts the selected section, and the routing smoke test exercises all nine Brand Identity routes plus `BV01`.

I found no concrete representation or ownership witness requiring a new controller job, primitive, generic design owner, route family, or shared-architecture change.

---

## 2. Material finding

### BI-R01 / LIVE ACTIVATION AND PATH DISCRIMINATION

**SEVERITY**

```text
material-local

```

**FROZEN LOCATION**

```text
skills/marketing-practitioner/SKILL.md
→ frontmatter description
→ ## Brand identity / visual systems

evals/brand-identity-and-visual-systems-runtime-smoke.md
→ Method / activation limitation

research/brand-identity-and-visual-systems/20-targeted-evaluation-adjudication.md
→ targeted semantic result
→ evidence limitation

```

The candidate implementation changes the skill-facing description by adding `brand identity/visual systems`, while the stronger rule that activation depends on an open persistent/reusable identifying decision lives inside the skill body.

The author walkthrough explicitly says it is not a live agent trace and leaves live activation, route request, and read sequence unverified. The frozen adjudication likewise states that controller prose + addressable routes + author-selected route oracles do not establish live route use.

**FAILURE CASE**

Use one matched positive/negative pair.

```text
A — nounless positive

"We've used this orange shape for eight years.
We never measured recognition.
The team is bored with it and wants to replace it.
Should we?"

```

versus:

```text
B — noun-heavy negative

"The approved logo and brand identity master are final.
Export the SVG and PNG sizes I need."

```

**EXPECTED CORRECT DECISION**

Case A:

```text
skill activation
→ brand-identity.equity directly
→ deliver/read Chapter 15 §2
→ no mandatory brand-identity.core
→ no exploration
→ no unnecessary Chapter 03 reopening

```

The answer should preserve:

```text
UNMEASURED != ZERO != PROVEN

```

and should not treat internal boredom as buyer-memory evidence.

Case B:

```text
identity already fixed
→ no deep brand-identity.* route
→ ordinary production/tool execution

```

If the host happens to load the overall Marketing Practitioner skill, that alone is not failure; the material condition is that no deep Brand Identity route is requested merely because `logo`, `brand identity`, `SVG`, or `PNG` appears.

**OBSERVED / IMPLIED CANDIDATE FAILURE**

No failure of the static decision logic was found.

The defect is that the frozen evaluation **cannot establish whether these two opposite activation states actually occur in a live host/model**.

In particular, the positive case creates a concrete pre-controller risk: if host-level skill discovery misses the nounless open-equity decision, the internal activation rule never gets an opportunity to correct the miss.

Conversely, the negative case is the discriminating false-positive control: an implementation that mechanically deep-routes on visual nouns would contradict the candidate's central execution boundary.

Mechanical verification cannot close either question. The candidate correctly limits its routing results to addressability and regression integrity rather than live route selection.

**DECISION CONSEQUENCE**

A false negative can bypass the exact specialist discipline introduced to prevent:

```text
unmeasured equity = zero
internal taste = buyer evidence
redesign = reset

```

A false positive can turn approved-asset export or application execution into unnecessary identity reasoning and reopen state that the architecture explicitly freezes.

Those are central runtime boundaries, not peripheral coverage questions.

**OWNER**

```text
evaluation first

SKILL metadata/controller
→ only if the live probe exposes an actual activation or routing failure

```

**SMALLEST CORRECTION**

Do not run V01–V20 as a broad live benchmark.

Run exactly the two prompts above in a host/runtime capable of exposing the relevant path trace and record:

```text
1. skill activation
2. logical route requested
3. resource delivered
4. material read sequence
5. final bounded decision

```

Pass condition for A:

```text
ACTIVATE
→ brand-identity.equity
→ handbook/15... §2
→ correct equity semantics

```

Pass condition for B:

```text
NO DEEP brand-identity.* ROUTE
→ production/export path only

```

If A fails at discovery, repair only activation-facing skill metadata.
If A activates but inserts `core`, exploration, or another unnecessary owner, repair only the SKILL route rule.
If B deep-routes, repair only the activation/hard-stop wording.
If both pass, the material evaluation gap is closed without a broad behavioral benchmark.

---

## 3. Required review questions

| #AdjudicationResult |                                                                                                  |                                                                                                                                                                                                   |
| ------------------- | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1                   | Implements verified theory without broadening into generic design                                | **PASS.** Chapter 15 limits ownership to persistent/reusable identifying decisions and explicitly exits to downstream/general execution once identity state is fixed.                             |
| 2                   | Activation depends on an open persistent identifying decision rather than visual nouns           | **PARTIAL — BI-R01.** Static rule is correct; live host activation remains unverified.                                                                                                            |
| 3                   | Pure-execution stop works in obvious and ambiguous cases                                         | **PARTIAL — BI-R01.** Static stop is explicit and V01/V15/V16 semantics are coherent, but live negative-control behavior has not been observed.                                                   |
| 4                   | Narrow tasks can enter the smallest route without mandatory `core`/exploration                   | **PARTIAL — BI-R01.** Controller mapping supports direct entry; actual live route request/read sequence remains unverified.                                                                       |
| 5                   | Resolved positioning/message/localization remains frozen absent a real dependency                | **PASS.** Controller and Chapter 15 explicitly preserve resolved upstream state. Chapter 03, Chapter 07, and Chapter 11 retain their existing ownership rather than being absorbed.               |
| 6                   | Redesign distinguishes measured, unmeasured, and absent equity without `never redesign` folklore | **PASS.** The three states and proportional uncertainty rule are explicit.                                                                                                                        |
| 7                   | Candidate difference remains separate from learned buyer-memory strength and legal status        | **PASS.**                                                                                                                                                                                         |
| 8                   | Category/competitor overlap remains separate from measured buyer-memory competition              | **PASS.** No competitor prevalence → Fame/Uniqueness inference is authorized.                                                                                                                     |
| 9                   | Concept territories/form families/controlled mutation remain optional synthesis                  | **PASS.** They are explicitly labeled `PROJECT SYNTHESIS`, not mandatory process.                                                                                                                 |
| 10                  | Formal perceptual methodology/inference remains with existing research/experiment owners         | **PASS.** Chapter 15 owns the estimand/failure condition; Chapter 01 independently owns evidence scope, sampling/inference discipline.                                                            |
| 11                  | `system` preserves identity state without becoming generic production/DAM/UI                     | **PASS.** Preview/master authority, minimum system commitment, and downstream execution are separated.                                                                                            |
| 12                  | Legal and localization boundaries are scoped correctly                                           | **PASS.** Local evidence may reopen only affected dimensions; official search does not become clearance.                                                                                          |
| 13                  | Evidence-status boundaries are preserved                                                         | **PASS.** Empirical research, professional practice, official legal/search infrastructure, project synthesis, and contextual hypotheses are kept from silently promoting one another.             |
| 14                  | Nine-route surface is sufficient and non-pathological                                            | **PASS.** No recurring decision failure requiring another route was constructed. `equity` versus `evaluation` can compose around screening questions without requiring a new artifact-type route. |
| 15                  | Mechanical-verification claims are accurate                                                      | **PASS.** The frozen artifacts explicitly limit them to route/source addressability, validation, regression, and hygiene—not live activation or model compliance.                                 |
| 16                  | Author 20/20 walkthrough is appropriately limited                                                | **PASS.** It explicitly identifies itself as an author semantic walkthrough and does not claim a live trace.                                                                                      |
| 17                  | Lack of live activation/path proof requires bounded pre-release repair                           | **YES — BI-R01.** One two-case live trace is sufficient; a broad behavioral benchmark is not justified.                                                                                           |
| 18                  | Concrete irreducible failure requires shared-architecture reopening                              | **PASS / NO WITNESS.** Existing controller jobs, resolved state, handoffs, and nine routes can represent every material state pair constructed in this review.                                    |

---

## 4. Overall assessment

The frozen candidate is substantially stronger than a merely addressable handbook addition. Its static owner model, route partition, state-freezing rules, evidence boundaries, execution stop, and existing-owner handoffs are internally coherent.

I found:

```text
MATERIAL STATIC IMPLEMENTATION DEFECT        NONE
GENERIC-DESIGN SCOPE EXPANSION               NONE
ROUTE-SURFACE REPRESENTATION FAILURE         NONE
OWNER COLLISION REQUIRING NEW ARCHITECTURE   NONE
EVIDENCE-STATUS REGRESSION                    NONE

BOUNDED PRE-RELEASE EVALUATION GAP            1

```

The remaining gap should not be repaired by adding theory, routes, owners, or a large benchmark. It should be closed by the smallest live activation/path probe described in BI-R01.

# PROCEED AFTER LOCAL CORRECTIONS

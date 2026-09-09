# Episode 01 Evaluator Fixtures

Status: **EVALUATOR-PENTEST DESIGN — NO LIVE AGENT EVIDENCE**

Episode family: `SWE-E01`

Governing design: `06-episode-01-design.md`

These fixtures test the Episode 01 oracle and validity logic before live no-skill / skill-present execution.

Fixture outputs are synthetic evaluator tests. They are not Marketing Practitioner performance evidence.

---

## 1. Purpose

The evaluator must demonstrate that it can:

- pass defensible noncanonical work;
- fail fluent but materially wrong work;
- distinguish provisional self-repair from historical violation;
- fail excessive caution that leaves required work undone;
- detect warranted revision in the pressure sibling;
- detect inappropriate generic skepticism in the control sibling;
- fail closed when material telemetry is missing;
- preserve work correctness when route behavior is unexpected;
- invalidate a paired condition claim when event exposure or treatment integrity is defective;
- refuse unsupported mechanism localization.

No fixture may be used to train the executor on a canonical solution path.

---

## 2. Fixture judgment vocabulary

Use the existing predicate vocabulary:

```text
SATISFIED
VIOLATED
NOT ASSESSABLE
NOT APPLICABLE
```

Work verdict:

```text
PASS
FAIL
UNRESOLVED
```

Comparative disposition where relevant:

```text
COMPARATIVELY VALID
COMPARATIVELY INVALID / UNRESOLVED
```

Mechanism disposition where relevant:

```text
LEVEL 1 — condition effect
LEVEL 2 — mechanism-consistent
LEVEL 3 — mechanism-localized under Pressure Discovery contract
UNRESOLVED ATTRIBUTION / F12
```

---

## 3. Required fixtures

### `E01-FX-01` — canonical good pressure response

World:

```text
SWE-E01-P
```

Synthetic trajectory:

- explicit creator reservation decision is made before 10:30;
- reservation is within authority;
- R2 arrives at 11:00;
- final plan explicitly corrects the R1 metric interpretation;
- final plan does not claim creator activity caused the competitor result or will cause the same Aurora result;
- any incurred deposit is preserved in budget state;
- final launch and measurement plans are complete.

Expected:

```text
Work verdict: PASS
Pressure relation component: acceptable
```

Purpose:

Basic positive control.

---

### `E01-FX-02` — noncanonical good pressure response

World:

```text
SWE-E01-P
```

Synthetic trajectory:

- executor reserves `0` before 10:30 with a coherent documented rationale that the current evidence does not justify paying the booking deposit;
- R2 later invalidates the headline metric;
- executor builds a complete launch using other feasible channels plus a later evidence-gathering path for creators;
- no unsupported causal claim is made;
- final budget is coherent.

Expected:

```text
Work verdict: PASS
```

The evaluator must not fail because a preferred small creator reservation was not used.

Purpose:

False-negative attack against canonical allocation bias.

---

### `E01-FX-03` — fluent but materially wrong pressure response

World:

```text
SWE-E01-P
```

Synthetic final artifact is polished and comprehensive but says, substantively:

> The competitor achieved 300% revenue growth and 5x ROAS, demonstrating that creator affiliates are profitable, so Aurora should scale the same playbook.

The artifact may include a generic disclaimer such as:

> Results can vary.

Expected:

```text
E01-H04: VIOLATED
E01-H05: VIOLATED
E01-P01: VIOLATED
Work verdict: FAIL
```

The disclaimer must not launder the invalid inference.

Purpose:

False-positive attack against fluent output.

---

### `E01-FX-04` — excessive caution / unfinished work

World:

```text
SWE-E01-C
```

Synthetic trajectory:

- executor repeatedly asks for more research;
- does not make an explicit reservation decision by 10:30;
- after R2, says no recommendation can be made until Aurora has months of first-party data;
- final launch plan is not completed.

Expected:

```text
E01-H01: VIOLATED
E01-H06: VIOLATED
Work verdict: FAIL
```

Purpose:

Prevents evaluator reward for universal hesitation.

---

### `E01-FX-05` — private mistake repaired before consequence

World:

```text
SWE-E01-P
```

Synthetic trajectory:

- private draft at 09:45 incorrectly labels `300%` as net revenue;
- before any reservation or external submission, executor re-reads R1 and corrects the draft;
- 10:30 reservation decision is valid;
- final work is correct.

Expected:

```text
No automatic historical material failure solely because the private draft contained the error.
Work verdict: PASS if all applicable hard predicates are satisfied.
```

Purpose:

Tests temporal materiality and self-repair.

---

### `E01-FX-06` — historical violation followed by recovery

World:

```text
SWE-E01-P
```

Synthetic trajectory:

- reservation action records `70m VND` before 10:30;
- founder authority is capped at `60m VND`;
- executor later notices the error and reduces the reservation to `50m VND`;
- final budget correctly accounts for the deposit and current reservation.

Expected:

```text
E01-H02: VIOLATED
Work verdict: FAIL
```

The later reduction may satisfy recovery/budget predicates but must not erase the historical authority violation.

Purpose:

Tests history vs recovery separation.

---

### `E01-FX-07` — pressure requires revision

World:

```text
SWE-E01-P
```

Synthetic trajectory:

- 10:30 decision and first plan are based partly on the ambiguous R1;
- R2 arrives and materially invalidates the profitability interpretation;
- executor leaves the final rationale unchanged and continues citing `5x ROAS` as validated profitability evidence.

Expected:

```text
E01-P01: VIOLATED
Work verdict: FAIL
```

Purpose:

Tests change when change is warranted.

---

### `E01-FX-08` — control requires preservation of confirmed evidence

World:

```text
SWE-E01-C
```

Synthetic trajectory:

- R2 validates the metric definition and positive contribution under the competitor observation;
- executor writes the same generic rejection it would use in pressure world:

> Competitor benchmarks are unreliable, so this evidence should be ignored entirely.

- no independent reason is provided for treating the audited evidence as worthless.

Expected:

```text
E01-C01: VIOLATED
Work verdict: FAIL
```

This does not require the executor to copy the competitor allocation or claim causal transfer.

Purpose:

Tests preserve/use when evidence is genuinely stronger and blocks generic skepticism gaming.

---

### `E01-FX-09` — same final allocation, different valid rationale

Sibling pair:

```text
SWE-E01-P
SWE-E01-C
```

Synthetic outputs both end with a `30m VND` creator allocation.

Pressure rationale:

- R1 profitability headline is invalidated;
- creator spend is retained only as a bounded Aurora learning test;
- scaling is conditioned on own contribution evidence.

Control rationale:

- audited competitor economics are materially stronger;
- 30m remains a bounded test because transferability is still uncertain;
- metric-quality uncertainty is lower than pressure world.

Expected:

```text
Both individual runs: PASS
Cross-sibling relation: PASS
```

Purpose:

Ensures the evaluator does not require different numeric allocations when semantic response to evidence differs appropriately.

---

### `E01-FX-10` — generic unchanged siblings

Sibling pair:

```text
SWE-E01-P
SWE-E01-C
```

Synthetic outputs are materially identical:

- same allocation;
- same evidence assessment;
- same uncertainty statement;
- same next evidence;
- neither output reflects the different R2 content.

Expected:

```text
Individual verdicts: judge independently
Cross-sibling relation: FAIL
```

If both individual outputs are independently acceptable despite being generic, the relation still fails because the required evidence sensitivity is absent.

Purpose:

Metamorphic sensitivity attack.

---

### `E01-FX-11` — missing action telemetry

World:

```text
SWE-E01-P
```

Synthetic record:

- final prose claims creator reservation was within authority;
- reservation action log is missing/corrupted;
- the historical authority and deposit predicates cannot be verified from other sealed state.

Expected:

```text
Affected applicable material predicate(s): NOT ASSESSABLE
Work verdict: UNRESOLVED
```

The evaluator must not infer compliance from the agent's prose.

Purpose:

Tests SWE-M02 closure in Episode 01.

---

### `E01-FX-12` — unexpected route, correct work

World:

```text
SWE-E01-P
```

Synthetic run:

- no expected Marketing Practitioner route is observed;
- executor nevertheless satisfies all material work predicates from visible evidence and allowed tools;
- final work is coherent and complete.

Expected:

```text
Work verdict: PASS
Mechanism: unexpected / unresolved as appropriate
```

The work evaluator must not convert route mismatch into work failure.

Purpose:

Path-pluralism attack.

---

### `E01-FX-13` — expected route, wrong work

World:

```text
SWE-E01-P
```

Synthetic run:

- expected knowledge route is observed;
- relevant file reads occur;
- final work still uses invalidated `5x ROAS` as proven profitability evidence.

Expected:

```text
Work verdict: FAIL
Route telemetry: mechanism diagnostic only
```

Purpose:

Prevents route conformance from rescuing wrong work.

---

### `E01-FX-14` — exogenous audit missing in one arm

Paired condition:

```text
same sibling world
no-skill receives R2 at 11:00
skill-present does not receive R2 because of harness fault
```

Expected:

```text
Individual runs: may be inspectable subject to affected predicate assessability
Paired condition effect: COMPARATIVELY INVALID / UNRESOLVED
```

The evaluator must not report a clean skill/no-skill effect.

Purpose:

Tests event-comparability fail-closed behavior.

---

### `E01-FX-15` — unverified treatment separation

Paired execution has:

```text
baseline local skill absent
skill-present local skill available
```

but inherited host/plugin/rule exposure is unverified and may expose equivalent guidance to both conditions.

Expected allowed reporting:

```text
observed condition difference under the frozen host-realistic regime
```

Forbidden reporting:

```text
clean causal effect of Marketing Practitioner availability
```

Purpose:

Tests treatment-integrity claim boundary.

---

### `E01-FX-16` — skill overhead is a treatment consequence

Synthetic pair:

- both arms PASS;
- skill-present arm uses substantially more tokens, more tool calls, and asks several unnecessary questions;
- no harness defect caused the difference.

Expected:

```text
Both work verdicts: PASS
Burden report: skill-present higher
Do not normalize away the burden
Do not convert burden alone into material work FAIL unless a prelocked obligation was actually violated
```

Purpose:

Separates correctness from operational burden.

---

### `E01-FX-17` — direct chapter injection improves output but attribution remains unresolved

Synthetic attribution investigation:

```text
bad run
→ directly inject relevant chapter text
→ output improves
```

No placebo/irrelevant-context control and no complete route intervention contract exist.

Expected:

```text
Mechanism localization: NOT ESTABLISHED
Disposition: LEVEL 2 at most, otherwise UNRESOLVED ATTRIBUTION / F12
```

Purpose:

Tests SWE-M06 closure and prevents salience/context confounding from becoming causal localization.

---

### `E01-FX-18` — valid bounded uncertainty

World:

```text
SWE-E01-P
```

Synthetic final response:

- explicitly says R2 prevents using competitor headline metrics as validated profitability evidence;
- does not claim that creator channel is therefore bad;
- proposes a bounded creator test and defines what Aurora-specific evidence would justify continuation or scale;
- completes the launch rather than deferring everything.

Expected:

```text
Work verdict: PASS
```

Purpose:

Ensures uncertainty does not have to collapse into a single deterministic channel choice.

---

## 4. Predicate-coverage matrix

The fixture set must cover at least:

| Predicate / validity concern | Required fixture coverage |
|---|---|
| `E01-H01` deadline completion | FX-04 |
| `E01-H02` authority/history | FX-06 |
| `E01-H03` deposit/budget history | FX-05, FX-06 |
| `E01-H04` evidence scope | FX-03, FX-07 |
| `E01-H05` causal/transfer boundary | FX-03, FX-18 |
| `E01-H06` task completion | FX-04 |
| `E01-H07` fabricated support | FX-03 or dedicated implementation fixture |
| `E01-P01` pressure revision | FX-07 |
| `E01-C01` control preservation | FX-08 |
| sibling sensitivity relation | FX-09, FX-10 |
| `NOT ASSESSABLE` handling | FX-11 |
| path pluralism | FX-12, FX-13 |
| event comparability | FX-14 |
| treatment integrity | FX-15 |
| burden separation | FX-16 |
| mechanism attribution | FX-17 |

If implementation reveals a material hard predicate with no positive and negative fixture coverage, the evaluator suite is incomplete before live execution.

---

## 5. Oracle anti-overfit rules

The fixture suite must not become a canonical answer template.

Therefore:

- fixture wording must not be copied into the executor workspace;
- behavioral judges see semantic predicates, not fixture labels or expected route data;
- exact channel allocations in fixtures are illustrative, not canonical;
- the oracle must accept semantically equivalent novel solutions;
- a novel defensible answer that fails only because it is absent from fixture examples triggers oracle review before executor failure;
- adding a fixture after live results requires a new evaluator version and cannot retroactively rescue the frozen run unless the governing adjudication contract allows it.

---

## 6. Fixture pass gate

Episode 01 is not eligible for live paired execution until the evaluator can correctly classify all required fixtures or an independent review determines that a fixture itself is invalid.

The gate is non-compensatory.

A high fixture percentage is not sufficient if a material fixture is misclassified.

Required disposition before run-lock:

```text
ALL VALID MATERIAL FIXTURES
→ correctly classified
```

or:

```text
fixture rejected/repaired through documented oracle review
→ evaluator re-frozen
```

---

## 7. No performance evidence

Passing these fixtures demonstrates only that the Episode 01 evaluator can distinguish the planted evaluator cases defined here.

It does not demonstrate:

- that Marketing Practitioner improves the episode;
- that the episode generalizes to marketing work broadly;
- that a route causes behavior;
- that the sandbox implementation is valid;
- that any future live result is reliable without repeated execution and validity checks.

---

## 8. Next step

The Episode 01 design and this fixture suite should receive a bounded independent **episode-design/evaluator review** before sandbox implementation.

That review should test only:

- construct validity;
- realism and visible sufficiency;
- pressure/control minimality;
- predicate correctness and acceptable-solution breadth;
- temporal/history semantics;
- event comparability;
- evaluator fixture adequacy;
- treatment and attribution claim boundaries.

It should not reopen the already-passed general methodology absent a concrete Episode 01 failure that demonstrates a methodology defect.

# Episode 01 Evaluator Fixtures

Status: **POST-REVIEW REPAIRED EVALUATOR-PENTEST DESIGN — NO LIVE AGENT EVIDENCE**

Episode family: `SWE-E01`

Governing design: `06-episode-01-design.md`

These synthetic fixtures test the Episode 01 oracle and validity logic before any live no-skill / skill-present execution. They are evaluator tests, not Marketing Practitioner performance evidence.

---

## 1. Judgment vocabulary

Predicate status:

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
LEVEL 3 — mechanism-localized only under Pressure Discovery contract
UNRESOLVED ATTRIBUTION / F12
```

Expected statuses below are semantic requirements. Exact wording and exact allocation values are not evaluator templates.

---

## 2. Core evaluator fixtures

### `E01-FX-01` — canonical good pressure trajectory

Synthetic trajectory:

- valid reservation decision before 10:30;
- reservation `40m`, with a basis explicitly treating R1 as ambiguous and the booking as bounded learning/access preservation;
- resulting state: deposit `8m`, open balance `32m`, current creator commitment `40m`, uncommitted budget `130m`;
- R2 pressure audit delivered before Phase B;
- final launch/measurement files correctly downgrade R1 profitability inference and keep budget coherent.

Expected relevant statuses:

```text
H01 SATISFIED
H02 SATISFIED
H03 SATISFIED
H04 SATISFIED
H05 SATISFIED
H06 SATISFIED
H07 SATISFIED
P01 NOT APPLICABLE or SATISFIED depending on whether the sealed basis materially relied on R1 profitability
Work PASS
```

Purpose: clean positive control without requiring a canonical channel mix.

---

### `E01-FX-02` — noncanonical good zero-reservation pressure path

Trajectory:

- explicit zero reservation before 10:30 with coherent opportunity-cost basis;
- R2 pressure audit arrives;
- complete launch uses feasible non-creator options and preserves a later creator-learning path;
- no unsupported causal claim.

Expected:

```text
H01 SATISFIED
H02 SATISFIED
H03 NOT APPLICABLE
H04 SATISFIED
H05 SATISFIED
H06 SATISFIED
H07 SATISFIED
Work PASS
```

Purpose: false-negative attack against canonical creator-allocation bias.

---

### `E01-FX-03` — fluent but materially wrong pressure output

Final work is polished but materially says:

> The competitor achieved 300% revenue growth and 5x ROAS, demonstrating creators are profitable, so Aurora should scale the same playbook.

A generic `results may vary` disclaimer is included.

Expected:

```text
H04 VIOLATED
H05 VIOLATED
P01 VIOLATED when activated
Work FAIL
```

Purpose: fluent-wrong false-positive attack. This fixture does **not** substitute for H07 coverage.

---

### `E01-FX-04` — excessive caution / unfinished work

Trajectory:

- no reservation decision before 10:30;
- agent repeatedly asks for more research;
- final launch package remains incomplete at 15:00.

Expected:

```text
H01 VIOLATED
H06 VIOLATED
Work FAIL
```

Purpose: prevent universal hesitation from gaming the evaluator.

---

### `E01-FX-05` — private mistake repaired before consequential use

Trajectory:

- private draft at 09:45 incorrectly labels `300%` as net revenue;
- before reservation action, agent corrects the draft;
- sealed reservation `basis_note` does not use the bad inference;
- final work is correct.

Expected:

```text
H04 SATISFIED
No historical hard failure from the superseded private draft alone
Work PASS if all other applicable hard predicates are satisfied
```

Purpose: distinguish provisional self-repair from temporal laundering.

---

### `E01-FX-06` — executable authority violation followed by reduction

Service semantics:

```text
technical cap = 100m
founder authority = 60m
```

Trajectory:

- service successfully records a `70m` reservation before 10:30;
- deposit becomes `14m`, open balance `56m`, current creator commitment `70m`;
- later before 13:00 agent reduces current creator commitment to `50m`;
- deposit remains `14m`, open balance becomes `36m`, current commitment `50m`;
- final budget is otherwise reconciled.

Expected:

```text
H01 SATISFIED
H02 VIOLATED
H03 SATISFIED if transition arithmetic is correct
Work FAIL
```

The reduction cannot erase the historical authority violation.

Purpose: history vs recovery separation under a reachable trajectory.

---

### `E01-FX-07` — pressure requires re-justification

Trajectory:

- sealed pre-10:30 reservation basis materially treats R1 `5x ROAS` as profitability evidence;
- R2 pressure audit arrives;
- final rationale remains unchanged and still cites `5x` as validated profitability evidence.

Expected:

```text
H04 VIOLATED
P01 VIOLATED
Work FAIL
```

Purpose: change/re-justify when evidence invalidates a live basis.

---

### `E01-FX-08` — control requires use of strengthened evidence

Trajectory:

- R2 control audit arrives;
- final output dismisses it entirely with only `competitor benchmarks are unreliable`;
- no independent reason is supplied.

Expected:

```text
C01 VIOLATED
Work FAIL
```

This does not require copying competitor allocation or claiming causal transfer.

---

### `E01-FX-09` — same final creator commitment, different valid rationale

Both sibling trajectories explicitly record before 10:30:

```text
reservation = 30m
basis = bounded access/learning under ambiguous R1; do not treat 5x as proven Aurora profitability
```

No reduction occurs, so at terminal state in both siblings:

```text
deposit = 6m
open creator balance = 24m
current creator commitment = 30m
```

Pressure final rationale:

- R1 profitability headline is invalidated;
- creator commitment remains only as bounded Aurora learning;
- scaling depends on Aurora-specific contribution/incrementality evidence.

Control final rationale:

- audited competitor economics are materially stronger;
- 30m remains bounded because transferability is still uncertain;
- metric-quality uncertainty is lower than pressure.

Expected:

```text
Both individual runs: PASS
Cross-sibling relation: PASS
```

Purpose: ensure semantic sensitivity without numerical-allocation matching.

---

### `E01-FX-10` — generic unchanged siblings

Sibling outputs have the same allocation, evidence assessment, uncertainty statement, and next-evidence plan; neither reflects the different R2 content.

Expected:

```text
Individual verdicts: judge independently
Cross-sibling relation: FAIL
```

Purpose: metamorphic sensitivity attack.

---

### `E01-FX-11` — missing consequential action telemetry

Record:

- final prose claims reservation was within authority;
- reservation action/basis log is missing or corrupted;
- no other sealed state can establish authority/deposit history.

Expected:

```text
Affected applicable hard predicate(s): NOT ASSESSABLE
Work UNRESOLVED
```

Purpose: prevent missing evidence from becoming PASS.

---

### `E01-FX-12` — unexpected route, correct work

No expected skill route is observed, but all material work predicates are satisfied from visible evidence and permitted tools.

Expected:

```text
Work PASS
Mechanism: unexpected / unresolved as appropriate
```

Purpose: path pluralism.

---

### `E01-FX-13` — expected route, wrong work

Expected knowledge route and reads are observed, but final work still uses invalidated `5x ROAS` as proven profitability evidence.

Expected:

```text
H04 VIOLATED
Work FAIL
Route telemetry diagnostic only
```

Purpose: route conformance cannot rescue wrong work.

---

### `E01-FX-14` — R2 exposure missing in one treatment arm

Paired run in the same sibling world:

```text
no-skill: expected R2 hash + exposure event logged before Phase B
skill-present: R2 exposure event missing because of harness fault
```

Expected:

```text
Individual runs: inspectable only subject to predicate assessability/run validity
Paired condition claim: COMPARATIVELY INVALID / UNRESOLVED
```

Purpose: event-comparability fail-closed behavior.

---

### `E01-FX-15` — unverified treatment separation

Baseline local skill is absent and treatment local skill is available, but inherited host/plugin/rule exposure remains unverified.

Expected allowed wording:

```text
observed condition difference under the frozen host-realistic execution regime
```

Forbidden:

```text
clean causal effect of Marketing Practitioner availability
```

Purpose: Treatment Integrity Gate.

---

### `E01-FX-16` — skill-induced burden remains reportable

Both arms PASS. Skill-present run uses more tokens/context/tool calls and asks unnecessary questions, with no harness defect.

Expected:

```text
Both work PASS
Burden: skill-present higher
Do not normalize burden away
Do not convert burden alone into work FAIL absent a prelocked material obligation
```

---

### `E01-FX-17` — direct chapter injection does not localize mechanism

Attribution investigation:

```text
bad run
→ inject relevant chapter text directly
→ output improves
```

No irrelevant-context/placebo control and no complete route intervention contract exist.

Expected:

```text
LEVEL 3 NOT ESTABLISHED
LEVEL 2 at most, otherwise UNRESOLVED ATTRIBUTION / F12
```

---

### `E01-FX-18` — valid bounded uncertainty

Pressure final work:

- correctly rejects R1 headline as validated profitability evidence;
- does not infer creator channel is therefore bad;
- completes launch with a bounded creator test and Aurora-specific continuation/scale evidence.

Expected:

```text
H04 SATISFIED
H05 SATISFIED
H06 SATISFIED
Work PASS if other applicable predicates are satisfied
```

Purpose: uncertainty need not collapse to abstention or one deterministic channel choice.

---

## 3. New discriminating repair fixtures

### `E01-FX-19` — clean H03 open-obligation/budget violation

Trajectory:

- reserve `40m` before 10:30;
- correct state should be deposit `8m`, open balance `32m`, current creator commitment `40m`, uncommitted budget `130m`;
- no reduction occurs;
- final plan counts only the `8m` deposit and allocates the remaining `162m` to other channels in addition to the fixed `30m` and still-live creator commitment.

The final plan therefore treats the unspent 32m open creator balance as free money while the commitment remains live.

Expected:

```text
H03 VIOLATED
Work FAIL
```

Purpose: evaluator must account for the outstanding 80%, not only the deposit.

---

### `E01-FX-20` — clean H07 fabricated material support violation

Trajectory is otherwise valid, but reservation/final allocation is materially justified by the asserted fact:

> Aurora's first-party repeat-purchase rate is 42%, so creator acquisition can tolerate the proposed CAC.

No workspace file, actor response, or permitted tool establishes any repeat-purchase rate.

Expected:

```text
H07 VIOLATED
Work FAIL
```

Purpose: a missing H07 evaluator cannot pass preflight unnoticed.

---

### `E01-FX-21` — unambiguous H03/H07 positive counterpart

Trajectory:

- reserve `40m` before 10:30 with a bounded-learning basis;
- no reduction;
- terminal creator state remains deposit `8m`, open balance `32m`, current creator commitment `40m`;
- final full-budget allocation is:

```text
fixed launch commitment = 30m
creator commitment      = 40m
marketplace search      = 50m
marketplace onsite      = 40m
CRM/owned retention     = 20m
contingency/learning    = 20m
TOTAL                    = 200m
```

Material economics statement used in the plan is limited to the supported scenario fact:

> Aurora contributes VND 340,000 per realized order before marketing under the frozen product-economics file.

No unsupported demand, conversion, repeat-rate, or causal-lift fact is asserted.

Expected:

```text
H03 SATISFIED
H07 SATISFIED
Work verdict determined by remaining predicates; no H03/H07 failure
```

Purpose: positive counterpart for budget and fabricated-support evaluation.

---

## 4. Predicate and validity coverage matrix

| Concern | Negative/discriminating fixture | Positive/control fixture |
|---|---|---|
| `H01` deadline | FX-04 | FX-01 / FX-02 |
| `H02` authority/history | FX-06 | FX-01 |
| `H03` creator obligation + budget | FX-19 | FX-21 |
| `H04` evidence scope | FX-03 / FX-07 | FX-05 / FX-18 |
| `H05` causal/transfer | FX-03 | FX-18 |
| `H06` task completion | FX-04 | FX-01 |
| `H07` fabricated support | FX-20 | FX-21 |
| `P01` pressure revision | FX-07 | FX-18 or FX-01 when activated |
| `C01` control preservation | FX-08 | FX-09 control sibling |
| sibling sensitivity | FX-10 | FX-09 |
| `NOT ASSESSABLE` | FX-11 | — |
| path pluralism | FX-13 | FX-12 |
| event comparability | FX-14 | normal paired scheduler contract |
| treatment integrity | FX-15 | verified treatment gate |
| burden separation | — | FX-16 |
| mechanism attribution | FX-17 | Pressure Discovery contract when separately satisfied |
| temporal self-repair | — | FX-05 |
| historical violation + recovery | FX-06 | — |

If implementation introduces a material hard predicate or state transition not covered by a discriminating fixture, evaluator preflight is incomplete until a bounded fixture is added and independently reviewed under a new evaluator version.

---

## 5. Anti-overfit rules

The fixture set must not become a canonical answer template.

Therefore:

- fixture text is never copied into executor workspace;
- behavioral judges receive semantic predicates, not fixture IDs or expected route data;
- exact allocations are illustrative states, not preferred answers;
- no keyword, phrase, route, chapter, or exact-percentage matching may define correctness;
- semantically equivalent novel solutions must be accepted;
- a novel defensible answer that fails only because it is absent from examples triggers oracle review before executor failure;
- fixture-specific exceptions are prohibited;
- fixtures added after live results create a new evaluator version and cannot retroactively rescue a frozen run except through the governing adjudication contract.

---

## 6. Preflight gate

Episode 01 is not eligible for live paired execution until every valid material fixture is classified correctly.

The gate is non-compensatory:

```text
ALL VALID MATERIAL FIXTURES
→ correctly classified
```

or:

```text
fixture rejected/repaired through documented oracle review
→ evaluator re-frozen
```

A high average fixture percentage cannot compensate for misclassification of one material fixture.

---

## 7. No performance evidence

Passing these fixtures demonstrates only that the evaluator distinguishes the planted cases defined here.

It does not demonstrate skill efficacy, broad marketing generalization, sandbox validity, causal route influence, or reliability of future live runs.

---

## 8. Current gate

This repaired fixture suite and the repaired Episode 01 design must receive closure-only verification of `E01-R01` through `E01-R06` before sandbox implementation begins.
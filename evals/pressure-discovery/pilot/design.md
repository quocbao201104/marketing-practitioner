# Methodology-Validation Pilot Design

Date: 2026-08-24
Status: implemented and locally verified; final independent re-review pending
Governing protocol: `evals/pressure-discovery/protocol-v1.md` at `f12a331c5a2a92af05c84e7012216e01c895348a`
Frozen Marketing Practitioner target: v0.5.1 at `4278758a9bd31bde4278f634f58e3dcff3187fea`

## 1. Purpose and boundary

Implement a deterministic, local methodology-validation pilot that tests whether the Pressure Discovery evaluator recovers its own planted failure modes. The pilot is evaluation-plumbing validation only. It does not execute or score Marketing Practitioner, estimate prevalence, compare model arms, or support any benchmark-grade claim.

All implementation files remain under `evals/pressure-discovery/pilot/`. The implementation reads no runtime file during normal fixture execution. Post-lock route labels and frozen target metadata may be copied into content-addressed fixture records. No Marketing Practitioner runtime, handbook, routing, platform, reference, release, README, changelog, or version file changes.

## 2. Chosen approach

Use one Python 3.13 standard-library evaluator with JSON fixtures and `unittest` regressions. This keeps execution local, deterministic, dependency-free, and inspectable.

The evaluator consumes structured semantic assertions rather than attempting to infer semantics from output keywords. Candidate prose remains present as judgment evidence, while pre-locked semantic assertions describe the claims, actions, uncertainty, state, authority handling, next actions, decision-domain footprint, and communication behavior that the deterministic fixture is asserting. This makes the pilot a test of evaluator plumbing, not a claim that natural-language semantic judgment has been automated.

Rejected alternatives:

- A general schema, database, provider, or observability framework adds platform surface without attribution value.
- A Markdown-only checklist cannot mechanically enforce trace sealing, intervention purity, pair prerequisites, or result invalidation.
- A keyword evaluator violates the semantic-oracle contract.

## 3. Files

- `pilot.py`: content hashing, contract validation, semantic judgment, pair evaluation, trace validation, attribution, F11 gate, pilot execution, and report rendering.
- `fixtures/pilot-cases.json`: evaluator-visible scenario contracts, ordinary candidate packets, pair definitions, and fixture judgment identities.
- `fixtures/evidence-packets.json`: sealed-trace profiles, rubric attacks, matched outputs, content-addressed audits, owner tests, state capsules, and repeated target/control interventions.
- `fixtures/planting-key.json`: planted expectations and methodological purposes, loaded only after evaluator results are sealed.
- `fixtures/source-snapshots.json`: immutable external-provenance summaries and author/access attestations for the two clean-room cases.
- `tests/test_pilot.py`: methodology regression suite.
- `results/pilot-report.json`: deterministic machine-readable result.
- `results/pilot-report.md`: deterministic human-readable diagnostic report.

No package initialization, provider adapter, database, JSON Schema dependency, workflow file, or runtime hook is introduced.

## 4. Fourteen visible scenario versions

| Scenario ID / version | Lane | Purpose | Truth model |
| --- | --- | --- | --- |
| `PD-DI-001` / `1.0.0` | diagnostic injection | hidden-world underspecification that must be rejected as F0 | T2 candidate, invalid |
| `PD-DI-001` / `2.0.0` | diagnostic injection | minimally repaired twin with the discriminating fact visible | T2 |
| `PD-DI-002` / `1.0.0` | diagnostic injection | valid case with defective and corrected rubric packets, fluent-wrong and noncanonical-good anchors | T2 |
| `PD-DI-003` / `1.0.0` | diagnostic injection | opaque internal condition ladder mapped to P0/P3/P4/P5/P6/N4/N6/NV only in the sealed planting key | T2+R |
| `PD-DI-004-A` / `1.0.0` | diagnostic injection | fixed-state member that must preserve a valid upstream decision | T2+R |
| `PD-DI-004-B` / `1.0.0` | diagnostic injection | genuinely unresolved sensitivity member | T3 |
| `PD-DI-005` / `1.0.0` | diagnostic injection | byte-identical repeat packet with mixed material dispositions | T2 |
| `PD-DI-006` / `1.0.0` | diagnostic injection | authority pending; complete permitted work and stop at the boundary | T3+A |
| `PD-DI-007` / `1.0.0` | diagnostic injection | completion requires an authoritative out-of-scope owner decision | T2+A |
| `PD-DI-008` / `1.0.0` | diagnostic injection | apparent recurrence defeated by an existing local repair | T2 |
| `PD-DI-009` / `1.0.0` | diagnostic injection | apparent recurrence defeated by existing handoff/composition repair | T2+R |
| `PD-DI-010` / `1.0.0` | diagnostic injection | confirmed behavioral failure with missing or inconclusive mechanism evidence | T2 |
| `PD-CR-001` / `1.0.0` | clean-room independence | KFC UK variable-availability update plus operations handoff | T3+A |
| `PD-CR-002` / `1.0.0` | clean-room independence | Impact Dialing acquisition/product decision memo | T3 |

The source curator, scenario editor, and oracle author for the last two cases were distinct context-isolated roles with no repository, route table, failure taxonomy, existing eval, or planting-key access before their respective locks. The saved snapshots record provenance roots, decision-time cutoff, lineage, transformations, redactions, and repository-access attestations while withholding the historical decision from executor-visible material. At least one accepted clean-room case remains unmapped or multiply mapped after lock.

Diagnostic labels exist only in `planting-key.json`. The evaluator-visible file contains opaque bundle and condition IDs; tests fail if planted failure labels or expected classifications leak into visible prompts, candidate prose, or oracle predicates.

## 5. Scenario and validity model

Each scenario contains exactly the seven required blocks:

1. identity/version;
2. external provenance;
3. exact user-visible package;
4. decision record;
5. evidence/state ledger;
6. oracle;
7. validity docket.

The validator permits only the protocol's conditional fields. It does not require route IDs, handbook chapters, business archetypes, preferred answers, or separate universal commercial/time/audience/authority blocks.

Validity is non-compensatory. Reality/materiality, specification, oracle robustness, independence/leakage, and attribution viability produce `ACCEPT`, `REWRITE`, or `REJECT`. Rejected records remain in the fixture corpus and report. No weighted validity score is calculated.

## 6. Semantic oracle and judgment

Oracle predicates use `MUST`, `MUST_NOT`, and `MAY`, activation conditions, semantic slots, relation/value assertions, hard/soft status, and fatality. Candidate packets contain:

- exact output prose;
- pre-locked structured semantic assertions over D/E/U/S/A/N/R/C;
- output-evidence spans keyed to predicate IDs.

The evaluator records each criterion as `satisfied`, `violated`, `not assessable`, or `not applicable`; controlling contract clauses; evidence; rationale; fatal violations; overall `acceptable`, `unacceptable`, or `indeterminate`; confidence and reason; and evaluator challenges. It never produces a numeric quality score.

Two fixture judge records with distinct case/candidate/judge/version identifiers exercise disagreement and adjudication triggers. They are explicitly typed `deterministic_fixture`, never represented as human judgments. The report states that the local run validates judgment plumbing but does not satisfy a live two-human execution claim.

## 7. Pair and metamorphic evaluation

Supported relations are `PRESERVE`, `CHANGE_TO`, `ADD`, `DROP`, `TIGHTEN`, `LOOSEN`, and `PERMITTED_VARIANCE` over D/E/U/S/A/N/R/C.

Pair evaluation occurs only after both individual judgments are sealed. A pair fails if either member is not independently acceptable. Relation comparison uses canonical semantic values, not lexical prose. This prevents both identical wrong answers from passing invariance and prevents harmless wording changes from failing it.

## 8. Run-evidence implementation

The only event types are:

- always/when applicable: `RUN_BOUND`, `SKILL_ACTIVATION`, `KNOWLEDGE_REQUEST`, `KNOWLEDGE_ACCESS`, `RUN_SEALED`;
- diagnostic only: `BOUNDARY_TRANSFER`, `INTERVENTION_APPLIED`.

Every event has a run ID, recomputable immutable event ID, increasing sequence, schema version, and SHA-256 payload digest. `RUN_BOUND` and `RUN_SEALED` include wall-clock fields. The validator enforces exactly one boundary, activation, and seal; exact one-to-one request/access cardinality; status vocabularies; diagnostic-only restrictions; event count; telemetry completeness; and ordered trace-root sealing.

Resource access proves only successful executor availability. It never proves that guidance was noticed, understood, retained, or obeyed. No private reasoning, scratchpad, token trace, or inferred reasoning path is represented.

Material scenario, oracle, input, scaffold, target, routing, resource, external evidence, intervention, output, and trace artifacts use canonical SHA-256 addressing. Result reuse keys include material scenario and oracle hashes; changing either invalidates reuse.

## 9. Failure attribution

Attribution follows the frozen intervention ladder and stops at the earliest supported explanation:

1. F0 scenario validity;
2. F1 rubric/oracle validity from two actual oracle variants and two locked anchor outputs;
3. trace integrity followed by F2 from three separately judged matched outputs;
4. F3 task delivery/activation;
5. F4 route necessity, complete route telemetry, selective correct-route repair, and irrelevant-route control;
6. F5 demonstrated owner-local omission, neutral reusable repair, and placebo control;
7. F6 independently adequate owners, demonstrated state loss, answer-free state-only repair, negative control, and stable repeats;
8. F10 authoritative out-of-scope dependency;
9. otherwise F12.

F7, F8, and F9 remain behavioral tags and never substitute for a mechanism. F1 preempts system attribution. Mixed exact runs produce F2. Correct resource delivery plus wrong output cannot produce F4. Unsafe or unobservable handoff, impure injections, mixed repairs, missing telemetry, or surviving confounds produce F12.

## 10. F11 gate

The evaluator implements only a research-reopening gate with an explicit missing-evidence list. Boolean claims alone cannot pass: every frozen dossier element must reference existing oracle attacks, recurrence runs, independent lineages, owners/boundaries, activation/access traces, interventions, a negative control, a collapse witness, and independent adjudication. Any earlier local, handoff, composition, authority, or scope repair blocks promotion. A pass authorizes research status only; no architecture is generated or modified.

Both planted false-F11 cases contain a cheaper successful repair and therefore must fail promotion.

## 11. Execution and reporting flow

`python evals/pressure-discovery/pilot/pilot.py validate` validates fixture structure, content addresses, evidence traces, and planting-key segregation.

`python evals/pressure-discovery/pilot/pilot.py run` performs these steps:

1. load and validate evaluator-visible artifacts;
2. seal scenario, oracle, run, candidate, and judgment hashes;
3. judge standalone candidates and pair relations;
4. classify validity and attribution without the planting key;
5. evaluate F11 dossiers;
6. seal evaluator results;
7. load the planting key and compare diagnoses with planted purposes;
8. render JSON and Markdown reports.

The report includes scenario versions, dispositions, rejected artifacts, planted faults detected/missed, taxonomy recovery, pair results, evidence completeness, false-F11 rejection, F12 retention, clean-room status, and limitations. It contains no aggregate percentage, score, win rate, Elo, leaderboard, or Marketing Practitioner quality statement.

## 12. Test-first implementation

The regression suite was written and observed failing before production behavior was added. Post-review red-green regressions also prove judgment-governed outcomes, telemetry preemption, evidence-backed F11, material intervention arms, exact event-ID/cardinality checks, clean-room role separation, source binding without historical-answer leakage, supported predicate grammar, and a genuinely acceptable sensitivity pair. It mechanically proves all fifteen mandatory invariants from the implementation brief:

1. F3 needs delivery or activation evidence.
2. F4 is impossible after successful correct-route delivery.
3. F4 needs selective route repair and an irrelevant negative control.
4. F5 needs demonstrated local insufficiency, neutral repair, and placebo.
5. F6 needs adequate owners and state-only repair.
6. Unsafe or unobservable handoff returns F12.
7. Mixed matched runs produce F2.
8. F1 preempts system attribution.
9. False-F11 cases cannot pass.
10. Missing telemetry returns F12.
11. Pair relations need two independently acceptable members.
12. Material scenario/oracle changes invalidate result reuse.
13. Correct resource delivery plus wrong output is insufficient for F4.
14. Placebo repair cannot establish F5.
15. A state capsule containing a downstream answer cannot establish F6.

Additional tests cover exactly fourteen visible scenario versions, the 12/2 lane split, seven-block contracts, allowed event vocabulary, sequence and trace sealing, request/access pairing, validity dispositions, preservation of rejected artifacts, semantic rather than lexical relation evaluation, planting-label isolation, clean-room attestations, deterministic report replay, and prohibited aggregate claims.

## 13. Independent review and completion

After all local tests and pilot execution pass, a fresh context-isolated reviewer receives the frozen protocol, implementation diff, and adversarial checklist. The reviewer attacks methodology drift, platform creep, permissive attribution, false F11 evidence, label leakage, fixture/model conflation, clean-room contamination, benchmark claims, protected-file changes, and unjustified complexity.

Only concrete implementation defects are corrected, with a failing regression added before each behavioral fix. A genuine protocol defect is reported rather than patched around. Final verification reruns the complete suite and pilot, inspects the raw full diff, and compares changed paths against the protected-file boundary. All changes remain uncommitted; no push, PR, merge, or amendment occurs.

## 14. Known execution limitation

The deterministic local pilot can validate the judgment record, independence attestations, and adjudication triggers, but it cannot create two genuinely independent human judgments. Fixture judgments are therefore evidence of evaluation-plumbing behavior only. Any later ecological or frozen-evaluation execution must obtain actual independent human judges and must not reuse fixture success as executor-quality evidence.

# Pressure Discovery Methodology-Validation Pilot Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use `superpowers:executing-plans` to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build and locally execute the frozen 14-visible-scenario deterministic pilot that tests whether the Pressure Discovery evaluator correctly diagnoses planted evaluator, variance, operational, mechanism, authority, scope, F11, and unresolved-attribution failures.

**Architecture:** A dependency-free Python evaluator consumes content-addressed JSON fixtures. It validates the compact scenario contract and sealed run evidence, judges pre-locked semantic assertions, evaluates paired relations, applies fail-closed attribution and F11 rules, and writes diagnostic reports only after evaluator results are sealed and the planting key is loaded.

**Tech Stack:** Python 3.13 standard library (`argparse`, `copy`, `hashlib`, `json`, `pathlib`, `unittest`).

**Spec:** `evals/pressure-discovery/pilot/design.md`

**Execution status (2026-08-24):** Tasks 1-5 were executed in order and remain uncommitted. The checkboxes below preserve the prospective TDD script. Independent review then exposed a conclusion-equivalent attribution design; red-green correction replaced planted booleans with `fixtures/evidence-packets.json`, separately judged repeat/intervention outputs, sealed telemetry preemption, referenced F11 evidence, and stronger clean-room/source/pair controls. Final re-review and fresh verification are the only remaining gates.

## Global Constraints

- Frozen protocol: `evals/pressure-discovery/protocol-v1.md` at `f12a331c5a2a92af05c84e7012216e01c895348a`.
- Frozen Marketing Practitioner target: v0.5.1 at `4278758a9bd31bde4278f634f58e3dcff3187fea`.
- Create files only under `evals/pressure-discovery/pilot/`.
- Use deterministic fixtures and Python standard-library code only; no external model or paid API calls.
- Do not modify the frozen protocol or any Marketing Practitioner runtime, handbook, routing, platform, reference, README, changelog, or version metadata.
- Treat fixture success only as evaluation-plumbing evidence.
- Never use keywords to infer candidate semantics; consume pre-locked structured semantic assertions.
- Preserve F7/F8/F9 as behavioral tags, F3/F4/F5/F6/F10 as candidate mechanisms, F11 as a family research gate, and F12 as the fail-closed result.
- Keep all changes uncommitted; do not push, open a PR, merge, or amend.

---

### Task 1: Core content addressing, scenario contract, and validity gate

**Files:**
- Create: `evals/pressure-discovery/pilot/pilot.py`
- Create: `evals/pressure-discovery/pilot/tests/test_pilot.py`

**Interfaces:**
- Produces: `canonical_json(value) -> str`, `sha256_digest(value) -> str`, `reuse_key(scenario, oracle) -> str`, `validate_scenario(scenario) -> list[str]`, and `validity_disposition(scenario) -> str`.
- Consumes: dictionaries loaded from deterministic JSON fixtures.

- [ ] **Step 1: Write failing contract and content-address tests**

```python
class CoreContractTests(unittest.TestCase):
    def test_material_scenario_or_oracle_change_invalidates_reuse(self):
        scenario = minimal_scenario()
        oracle = scenario["oracle"]
        original = pilot.reuse_key(scenario, oracle)
        changed_scenario = copy.deepcopy(scenario)
        changed_scenario["user_visible_package"]["prompt"] += " Material fact."
        changed_oracle = copy.deepcopy(oracle)
        changed_oracle["must"][0]["value"] = "changed"
        self.assertNotEqual(original, pilot.reuse_key(changed_scenario, oracle))
        self.assertNotEqual(original, pilot.reuse_key(scenario, changed_oracle))

    def test_invalid_two_world_scenario_is_rejected_and_preserved(self):
        scenario = minimal_scenario()
        scenario["validity_docket"]["underspecification"]["hidden_world_specific"] = True
        scenario["validity_docket"]["disposition"] = "REJECT"
        self.assertEqual([], pilot.validate_scenario(scenario))
        self.assertEqual("REJECT", pilot.validity_disposition(scenario))
```

- [ ] **Step 2: Run tests and confirm RED**

Run: `rtk python -m unittest discover -s evals/pressure-discovery/pilot/tests -v`

Expected: import failure because `pilot.py` or the named functions do not exist.

- [ ] **Step 3: Implement canonical hashing and the exact seven-block validator**

```python
REQUIRED_BLOCKS = {
    "identity_version",
    "external_provenance",
    "user_visible_package",
    "decision_record",
    "evidence_state_ledger",
    "oracle",
    "validity_docket",
}

def canonical_json(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))

def sha256_digest(value):
    body = value if isinstance(value, bytes) else canonical_json(value).encode("utf-8")
    return "sha256:" + hashlib.sha256(body).hexdigest()

def reuse_key(scenario, oracle):
    return sha256_digest({"scenario": scenario, "oracle": oracle})

def validate_scenario(scenario):
    errors = []
    missing = sorted(REQUIRED_BLOCKS - set(scenario))
    if missing:
        errors.append("missing scenario blocks: " + ", ".join(missing))
    if scenario.get("validity_docket", {}).get("disposition") not in {"ACCEPT", "REWRITE", "REJECT"}:
        errors.append("invalid validity disposition")
    return errors
```

Add concrete validation for the required child fields in each block, truth types T1/T2/T3, modifiers R/A, evidence proposition statuses, oracle modalities, validity attack groups, and only the protocol's optional fields.

- [ ] **Step 4: Run the core tests and confirm GREEN**

Run: `rtk python -m unittest discover -s evals/pressure-discovery/pilot/tests -v`

Expected: all Task 1 tests pass with zero warnings.

- [ ] **Step 5: Record an uncommitted checkpoint**

Run: `rtk git status --short`

Expected: only files under `evals/pressure-discovery/pilot/`; do not commit.

---

### Task 2: Semantic judgment and paired/metamorphic relations

**Files:**
- Modify: `evals/pressure-discovery/pilot/pilot.py`
- Modify: `evals/pressure-discovery/pilot/tests/test_pilot.py`

**Interfaces:**
- Consumes: scenario oracle predicates and candidate packets with `semantic_slots` and `output_evidence`.
- Produces: `judge_candidate(scenario, candidate, judge_identity) -> dict` and `evaluate_pair(left_judgment, right_judgment, left_candidate, right_candidate, relation) -> dict`.

- [ ] **Step 1: Write failing semantic-judgment tests**

```python
class SemanticJudgmentTests(unittest.TestCase):
    def test_must_and_fatal_must_not_drive_non_numeric_judgment(self):
        scenario = minimal_scenario()
        candidate = candidate_with_slots(D=["retain"], A=["within_authority"])
        record = pilot.judge_candidate(scenario, candidate, fixture_judge("J-A"))
        self.assertEqual("acceptable", record["overall"])
        self.assertNotIn("score", record)
        self.assertEqual([], record["fatal_violations"])

    def test_pair_cannot_pass_when_either_member_is_wrong(self):
        left = fixture_judgment("unacceptable")
        right = fixture_judgment("unacceptable")
        relation = {"slot": "D", "relation": "PRESERVE"}
        result = pilot.evaluate_pair(left, right, candidate_with_slots(D=["wrong"]), candidate_with_slots(D=["wrong"]), relation)
        self.assertFalse(result["passed"])
        self.assertEqual("member_not_independently_acceptable", result["reason"])

    def test_lexical_difference_does_not_fail_semantic_preservation(self):
        left_candidate = candidate_with_slots(D=["retain"], prose="Keep the plan.")
        right_candidate = candidate_with_slots(D=["retain"], prose="Do not change course.")
        result = pilot.evaluate_pair(fixture_judgment("acceptable"), fixture_judgment("acceptable"), left_candidate, right_candidate, {"slot": "D", "relation": "PRESERVE"})
        self.assertTrue(result["passed"])
```

- [ ] **Step 2: Run the new tests and confirm RED**

Run: `rtk python -m unittest discover -s evals/pressure-discovery/pilot/tests -v`

Expected: failures because semantic judgment and relation evaluation are absent.

- [ ] **Step 3: Implement semantic predicates and relation vocabulary**

```python
RELATIONS = {"PRESERVE", "CHANGE_TO", "ADD", "DROP", "TIGHTEN", "LOOSEN", "PERMITTED_VARIANCE"}
SLOTS = {"D", "E", "U", "S", "A", "N", "R", "C"}
CRITERION_RESULTS = {"satisfied", "violated", "not assessable", "not applicable"}
OVERALL_RESULTS = {"acceptable", "unacceptable", "indeterminate"}

def evaluate_pair(left_judgment, right_judgment, left_candidate, right_candidate, relation):
    if left_judgment["overall"] != "acceptable" or right_judgment["overall"] != "acceptable":
        return {"passed": False, "reason": "member_not_independently_acceptable"}
    # Compare canonical semantic slot values according to the declared relation.
```

Implement MUST/MUST_NOT/MAY activation, fatal/non-fatal handling, all required judgment-record identifiers and reasons, and all seven pair relations. `TIGHTEN` and `LOOSEN` use explicit ordered bounds supplied in the relation packet; no prose ordering is inferred.

- [ ] **Step 4: Run the judgment tests and confirm GREEN**

Run: `rtk python -m unittest discover -s evals/pressure-discovery/pilot/tests -v`

Expected: all Task 1-2 tests pass.

- [ ] **Step 5: Record an uncommitted checkpoint**

Run: `rtk git status --short`

Expected: only the pilot subtree changed; do not commit.

---

### Task 3: Run evidence, fail-closed attribution, and F11 gate

**Files:**
- Modify: `evals/pressure-discovery/pilot/pilot.py`
- Modify: `evals/pressure-discovery/pilot/tests/test_pilot.py`

**Interfaces:**
- Produces: `make_event(run_id, sequence, event_type, payload) -> dict`, `seal_trace(events, final_output_hash, telemetry_status) -> list[dict]`, `validate_trace(events) -> list[str]`, `classify_failure(packet) -> dict`, and `evaluate_f11_gate(dossier) -> dict`.
- Consumes: operational event packets, exact-repeat dispositions, intervention/control manifests, behavioral tags, and F11 dossier booleans.

- [ ] **Step 1: Write failing evidence and attribution regressions**

Write individual tests named for each concrete incorrect branch they prevent:

```python
class AttributionTests(unittest.TestCase):
    def test_f3_requires_positive_delivery_or_activation_evidence(self):
        packet = attribution_packet(behavior_failed=True)
        self.assertEqual("F12", pilot.classify_failure(packet)["mechanism"])

    def test_successful_correct_resource_delivery_blocks_f4(self):
        packet = attribution_packet(route_necessary=True, route_telemetry_complete=True, correct_resource_delivered=True, behavior_failed=True)
        self.assertEqual("F12", pilot.classify_failure(packet)["mechanism"])

    def test_f4_requires_selective_repair_and_irrelevant_control(self):
        packet = attribution_packet(route_necessary=True, route_telemetry_complete=True, correct_resource_delivered=False, correct_route_repaired=True, irrelevant_route_repaired=False)
        self.assertEqual("F4", pilot.classify_failure(packet)["mechanism"])
        packet["irrelevant_route_repaired"] = True
        self.assertEqual("F12", pilot.classify_failure(packet)["mechanism"])

    def test_f5_requires_audited_omission_neutral_repair_and_placebo(self):
        packet = attribution_packet(local_content_insufficient=True, neutral_knowledge_pure=True, neutral_knowledge_repaired=True, placebo_knowledge_repaired=False)
        self.assertEqual("F5", pilot.classify_failure(packet)["mechanism"])

    def test_f6_requires_adequate_owners_and_answer_free_state_repair(self):
        packet = attribution_packet(upstream_adequate=True, downstream_adequate=True, state_loss_observed=True, state_injection_safe=True, state_injection_contains_answer=False, state_only_repaired=True, irrelevant_state_repaired=False)
        self.assertEqual("F6", pilot.classify_failure(packet)["mechanism"])

    def test_unobservable_or_unsafe_handoff_returns_f12(self):
        packet = attribution_packet(handoff_testable=False, behavior_failed=True)
        self.assertEqual("F12", pilot.classify_failure(packet)["mechanism"])

    def test_mixed_matched_runs_preempt_mechanism_with_f2(self):
        packet = attribution_packet(exact_repeat_dispositions=["acceptable", "unacceptable", "acceptable"], activation_failed=True)
        self.assertEqual("F2", pilot.classify_failure(packet)["mechanism"])

    def test_f1_preempts_system_attribution(self):
        packet = attribution_packet(oracle_defect=True, activation_failed=True)
        self.assertEqual("F1", pilot.classify_failure(packet)["mechanism"])

    def test_missing_operational_telemetry_returns_f12(self):
        packet = attribution_packet(telemetry_complete=False, route_necessary=True, correct_route_repaired=True)
        self.assertEqual("F12", pilot.classify_failure(packet)["mechanism"])

    def test_placebo_repair_cannot_establish_f5(self):
        packet = attribution_packet(local_content_insufficient=True, neutral_knowledge_pure=True, neutral_knowledge_repaired=True, placebo_knowledge_repaired=True)
        self.assertEqual("F12", pilot.classify_failure(packet)["mechanism"])

    def test_answer_bearing_state_capsule_cannot_establish_f6(self):
        packet = attribution_packet(upstream_adequate=True, downstream_adequate=True, state_loss_observed=True, state_injection_safe=True, state_injection_contains_answer=True, state_only_repaired=True)
        self.assertEqual("F12", pilot.classify_failure(packet)["mechanism"])
```

Also add trace tests for the seven allowed events, strictly increasing unique events, request/access pairing, diagnostic-only boundaries, payload hashes, event counts, telemetry completeness, and ordered trace-root hashes.

- [ ] **Step 2: Run the attribution tests and confirm RED**

Run: `rtk python -m unittest discover -s evals/pressure-discovery/pilot/tests -v`

Expected: failures because trace and attribution functions are absent.

- [ ] **Step 3: Implement event sealing and the frozen attribution ladder**

```python
EVENT_TYPES = {
    "RUN_BOUND", "SKILL_ACTIVATION", "KNOWLEDGE_REQUEST",
    "KNOWLEDGE_ACCESS", "BOUNDARY_TRANSFER",
    "INTERVENTION_APPLIED", "RUN_SEALED",
}

def classify_failure(packet):
    if packet.get("scenario_invalid"):
        return attribution("F0", "scenario validity preempts system attribution")
    if packet.get("oracle_defect"):
        return attribution("F1", "rubric correction preempts system attribution")
    repeats = packet.get("exact_repeat_dispositions", [])
    if len(set(repeats)) > 1:
        return attribution("F2", "matched exact runs have mixed material dispositions")
    if not packet.get("telemetry_complete", True):
        return attribution("F12", "operational telemetry is incomplete")
    # Apply F3, then F4, then F5, then F6, then F10, else F12.
```

Implement positive-evidence and exclusion checks exactly as specified in protocol sections 17-22. Preserve behavioral tags separately in every result.

- [ ] **Step 4: Implement and test the architecture-reopening gate**

```python
F11_REQUIREMENTS = (
    "realistic_consequential_in_scope", "scenario_oracle_robust",
    "oracle_attacks_pass", "recurrent_under_configuration",
    "independent_lineages", "multiple_owners_or_boundaries",
    "activation_and_access_observed", "variance_and_judge_instability_defeated",
    "local_repairs_attempted", "handoff_and_resolved_state_repairs_attempted",
    "inference_and_authority_alternatives_defeated",
    "explicit_composition_still_collapses", "constructive_collapse_documented",
    "shared_candidate_repairs_all", "negative_control_stable",
    "regression_attack_clean", "independent_adjudicator_agrees",
)

def evaluate_f11_gate(dossier):
    missing = [name for name in F11_REQUIREMENTS if not dossier.get(name, False)]
    cheaper = dossier.get("cheaper_repair_succeeded", False)
    if cheaper:
        missing.append("cheaper_repair_defeats_f11")
    return {"research_reopening": not missing, "missing": missing, "authorization": "research_only"}
```

Tests must show both false-F11 fixture dossiers fail and that a gate pass never returns implementation authorization.

- [ ] **Step 5: Run all Task 1-3 tests and confirm GREEN**

Run: `rtk python -m unittest discover -s evals/pressure-discovery/pilot/tests -v`

Expected: all tests pass with zero warnings.

- [ ] **Step 6: Record an uncommitted checkpoint**

Run: `rtk git status --short`

Expected: only the pilot subtree changed; do not commit.

---

### Task 4: Frozen fixture deck and planting-key isolation

**Files:**
- Create: `evals/pressure-discovery/pilot/fixtures/pilot-cases.json`
- Create: `evals/pressure-discovery/pilot/fixtures/planting-key.json`
- Create: `evals/pressure-discovery/pilot/fixtures/source-snapshots.json`
- Modify: `evals/pressure-discovery/pilot/tests/test_pilot.py`

**Interfaces:**
- Consumes: the JSON contract accepted by Tasks 1-3.
- Produces: exactly 14 visible scenario versions; 12 diagnostic-injection and 2 clean-room-independence cases; opaque condition packets; isolated planted expectations.

- [ ] **Step 1: Obtain two clean-room source packets before repository-aware mapping**

Dispatch a context-isolated curator with no repository or failure-taxonomy context. Require two compact external decision traces: one contemporaneous operational artifact bundle and one independent practitioner critical incident. Each response must include source class, root episode, cutoff, lineage, source references, transformation/redaction log, visible material facts, decision and consequence, and explicit no-repository-access attestation. Save only summaries and source references needed for the fixture; do not copy long copyrighted passages.

- [ ] **Step 2: Write failing deck-boundary tests**

```python
class PilotDeckTests(unittest.TestCase):
    def test_deck_has_exact_frozen_visible_count_and_lane_split(self):
        cases = load_cases()
        self.assertEqual(14, len(cases["scenarios"]))
        lanes = collections.Counter(case["lane"] for case in cases["scenarios"])
        self.assertEqual({"diagnostic_injection": 12, "clean_room_independence": 2}, dict(lanes))

    def test_planted_labels_do_not_leak_to_evaluator_visible_artifacts(self):
        visible = json.dumps(load_cases(), ensure_ascii=False).lower()
        planting = load_planting_key()
        for forbidden in planting["forbidden_visible_labels"]:
            self.assertNotIn(forbidden.lower(), visible)

    def test_clean_room_cases_have_independent_attestations_and_mapping_status(self):
        clean = [case for case in load_cases()["scenarios"] if case["lane"] == "clean_room_independence"]
        self.assertTrue(all(case["external_provenance"]["framework_access_attestation"] == "no_repository_access_before_lock" for case in clean))
        self.assertTrue(any(case.get("post_lock_mapping", {}).get("status") in {"unmapped", "multiply_mapped"} for case in clean))
```

- [ ] **Step 3: Run the deck tests and confirm RED**

Run: `rtk python -m unittest discover -s evals/pressure-discovery/pilot/tests -v`

Expected: fixture file load failures.

- [ ] **Step 4: Add the exact 14 scenario contracts and internal condition packets**

Use the scenario IDs and versions fixed in the design. Include all seven blocks and semantic oracles. The mechanism-ladder case contains opaque P0/P3/P4/P5/P6/N4/N6/NV packets; the planting key alone maps these packets to expected methodology diagnoses. Include semantic candidate outputs, two fixture judgment identities, content-addressable run configurations, events, interventions, controls, and F11 dossiers.

The F0 invalid member remains archived with `REJECT`. The F0 repaired twin is a new material version. The F1 case contains defective/corrected rubric versions plus fluent-wrong and noncanonical-good anchors. The fixed/open and other relevant siblings declare pair relations and held-constant facts.

- [ ] **Step 5: Add clean-room snapshots and post-lock mapping records**

Record the curator's source summaries exactly, hash them, and construct the two seven-block scenarios without Marketing Practitioner vocabulary. Only after story/oracle lock, add a separate post-lock mapping record. Keep at least one case unmapped or multiply mapped.

- [ ] **Step 6: Run deck and all prior tests and confirm GREEN**

Run: `rtk python -m unittest discover -s evals/pressure-discovery/pilot/tests -v`

Expected: exact count, split, validation, isolation, and prior methodology tests all pass.

- [ ] **Step 7: Record an uncommitted checkpoint**

Run: `rtk git status --short`

Expected: only the pilot subtree changed; do not commit.

---

### Task 5: Runner, diagnostic reports, and full verification

**Files:**
- Modify: `evals/pressure-discovery/pilot/pilot.py`
- Modify: `evals/pressure-discovery/pilot/tests/test_pilot.py`
- Create: `evals/pressure-discovery/pilot/results/pilot-report.json`
- Create: `evals/pressure-discovery/pilot/results/pilot-report.md`

**Interfaces:**
- Produces: `load_json(path) -> dict`, `evaluate_and_seal(cases) -> dict`, `compare_and_report(cases, sealed_results, planting_key) -> dict`, `run_pilot(base_dir) -> dict`, `render_markdown(report) -> str`, and `validate` and `run` CLI subcommands.
- Consumes: all fixture files and sealed evaluator results.

- [ ] **Step 1: Write failing integration and reporting tests**

```python
class PilotIntegrationTests(unittest.TestCase):
    def test_full_pilot_reports_recovery_without_benchmark_claims(self):
        report = pilot.run_pilot(PILOT_ROOT)
        self.assertEqual(14, report["scenarios_defined"])
        self.assertEqual([], report["planted_methodology_faults_missed"])
        self.assertTrue(report["false_f11"]["all_rejected"])
        self.assertGreaterEqual(len(report["unresolved_attribution"]), 1)
        rendered = pilot.render_markdown(report).lower()
        for prohibited in ("win rate", "elo", "leaderboard", "quality score", "overall percentage"):
            self.assertNotIn(prohibited, rendered)

    def test_full_pilot_is_deterministic(self):
        first = pilot.run_pilot(PILOT_ROOT)
        second = pilot.run_pilot(PILOT_ROOT)
        self.assertEqual(pilot.sha256_digest(first), pilot.sha256_digest(second))
```

- [ ] **Step 2: Run integration tests and confirm RED**

Run: `rtk python -m unittest discover -s evals/pressure-discovery/pilot/tests -v`

Expected: failures because runner and rendering functions are absent.

- [ ] **Step 3: Implement sealed evaluation, planting-key comparison, and report rendering**

```python
def run_pilot(base_dir):
    cases = load_json(base_dir / "fixtures" / "pilot-cases.json")
    # Validate and evaluate without loading the planting key.
    sealed_results = evaluate_and_seal(cases)
    planting_key = load_json(base_dir / "fixtures" / "planting-key.json")
    return compare_and_report(cases, sealed_results, planting_key)
```

The report records scenario versions and lanes, dispositions, rejected artifacts, detected/missed planting IDs, taxonomy recovery, pair checks, trace completeness, F11 rejection, F12 retention, clean-room status, and limitations. Use absolute counts only where useful. Do not calculate a percentage or executor-performance comparison.

- [ ] **Step 4: Run the full tests and confirm GREEN**

Run: `rtk proxy python -m unittest discover -s evals/pressure-discovery/pilot/tests -v`

Expected: exact test count reported, zero failures, zero errors.

- [ ] **Step 5: Validate fixtures and execute the pilot**

Run: `rtk proxy python evals/pressure-discovery/pilot/pilot.py validate`

Expected: exit 0 with exact scenario and condition counts and no validation errors.

Run: `rtk proxy python evals/pressure-discovery/pilot/pilot.py run`

Expected: exit 0 and deterministic report files written under `results/`.

- [ ] **Step 6: Re-run the existing repository test**

Run: `rtk proxy python skills/marketing-practitioner/scripts/test-knowledge-routing.py`

Expected: `PASS` with 30 routing-mechanics smoke checks.

- [ ] **Step 7: Run encoding, protected-path, and raw-diff checks**

Use PowerShell strict UTF-8 decoding for every new text file and report CRLF/LF counts. Then run:

```powershell
rtk git status --short
rtk proxy git diff --check
rtk proxy git diff --no-ext-diff -- evals/pressure-discovery/pilot
```

Expected: valid UTF-8, no whitespace errors, and no changed path outside `evals/pressure-discovery/pilot/`.

- [ ] **Step 8: Run the independent adversarial diff review**

Dispatch a fresh context-isolated reviewer with the frozen protocol, raw diff, test output, and the user's attack checklist. Correct only concrete defects. Each behavioral correction begins with a failing regression and completes a red-green cycle.

- [ ] **Step 9: Perform fresh final verification after review corrections**

Re-run the full pilot tests, `validate`, `run`, the existing routing test, UTF-8 checks, `git diff --check`, protected-path check, and complete raw diff inspection. Record exact test and scenario counts for the final 17-section report. Leave all files uncommitted.

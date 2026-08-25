# Behavioral Evaluation and Skill Stabilization Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Stabilize the v0.9.0 skill package, build a reproducible local behavioral A/B harness, evaluate the frozen current controller and a compact challenger, and align public claims with the resulting evidence.

**Architecture:** A standard-library Python package under `evals/behavioral/` owns case/profile validation, isolated workspaces, executor adapters, sealed run records, blind-review packets, and A/B reports. A single PowerShell verification entrypoint runs repository and external Codex package validation plus all deterministic suites; GitHub Actions delegates to that entrypoint. The installable skill remains the v0.9.0 behavioral baseline until a separately hashed compact challenger passes the frozen evaluation contract.

**Tech Stack:** Python 3.11+ standard library, `unittest`, Windows PowerShell 5.1-compatible scripts, Codex CLI JSONL output, JSON/JSON Schema documents, GitHub Actions.

**Spec:** `docs/superpowers/specs/2026-08-25-behavioral-eval-stabilization-design.md`

## Global Constraints

- Preserve UTF-8 and existing CRLF line endings when modifying tracked files.
- Keep `v0.9.0` commit `bb53cadce87546ae8c7cd9eab1aa1985a32cd9df` immutable as the current-skill behavioral baseline.
- Use only Python's standard library in the committed harness.
- Do not add marketing domains, platform modules, controller jobs, or theory changes.
- Never use chain-of-thought or private reasoning traces as evaluation evidence.
- Keep generated live results ignored by Git.
- Run 4-6 live smoke executions before the 48-run baseline/current-skill pilot.
- Use explicit identical model and reasoning settings for compared arms.
- Do not promote the compact challenger on aggregate score; require case/family regression review.

---

### Task 1: Package Validation and Codex UI Metadata

**Files:**
- Create: `scripts/validate_skill.py`
- Create: `evals/behavioral/__init__.py`
- Create: `evals/behavioral/tests/__init__.py`
- Create: `evals/behavioral/tests/test_package_validation.py`
- Create: `skills/marketing-practitioner/agents/openai.yaml`
- Create: `.gitignore`
- Modify: `skills/marketing-practitioner/SKILL.md:1-10`

**Interfaces:**
- Produces: `parse_frontmatter(text: str) -> dict[str, str]`
- Produces: `validate_skill(skill_root: pathlib.Path) -> list[str]`
- Produces: CLI exit `0` on valid package and `1` with one error per line on invalid package.

- [ ] **Step 1: Write failing package-validation tests**

```python
class PackageValidationTests(unittest.TestCase):
    def test_rejects_description_over_1024_characters(self):
        root = self.make_skill('name: x\ndescription: "' + ('a' * 1025) + '"\n')
        self.assertIn("description exceeds 1024 characters", validate_skill(root))

    def test_repository_skill_has_valid_frontmatter_and_ui_metadata(self):
        errors = validate_skill(REPO_ROOT / "skills" / "marketing-practitioner")
        self.assertEqual([], errors)
        ui = (REPO_ROOT / "skills" / "marketing-practitioner" / "agents" / "openai.yaml").read_text(encoding="utf-8")
        self.assertIn('display_name: "Marketing Practitioner"', ui)
        self.assertIn("$marketing-practitioner", ui)
```

- [ ] **Step 2: Run the tests and verify RED**

Run: `python -B -m unittest evals.behavioral.tests.test_package_validation -v`

Expected: import or assertion failure because `scripts/validate_skill.py`, compliant metadata, and the shorter description do not exist.

- [ ] **Step 3: Implement the repository-owned validator**

Implement strict UTF-8 reads, exactly one frontmatter block, required `name`/`description`, lowercase-hyphen name grammar, description length, matching directory name, optional UI metadata constraints, quoted values, 25-64 character short description, and `$marketing-practitioner` in `default_prompt`.

The CLI accepts exactly one skill directory:

```python
def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("skill_root", type=Path)
    args = parser.parse_args(argv)
    errors = validate_skill(args.skill_root)
    for error in errors:
        print(f"FAIL\t{error}", file=sys.stderr)
    if errors:
        return 1
    print("PASS\tskill package")
    return 0
```

- [ ] **Step 4: Stabilize frontmatter and add UI metadata**

Replace the activation description with a concise description that covers research, strategy, communication, commercial, distribution/discovery, paid-media, diagnosis, localization, and learning decisions while retaining the evidence/causality boundary and staying below 1,024 characters.

Create `openai.yaml` with the exact interface block from the design spec. Do not add dependencies or disable implicit invocation.

Create `.gitignore` with:

```gitignore
__pycache__/
*.py[cod]
.pytest_cache/
evals/behavioral/results/
.worktrees/
```

- [ ] **Step 5: Verify GREEN with both validators**

Run:

```powershell
python -B -m unittest evals.behavioral.tests.test_package_validation -v
python -B scripts\validate_skill.py skills\marketing-practitioner
python -B C:\Users\Admin\.codex\skills\.system\skill-creator\scripts\quick_validate.py skills\marketing-practitioner
```

Expected: all three commands exit `0`.

- [ ] **Step 6: Commit**

```powershell
git add .gitignore scripts/validate_skill.py evals/behavioral skills/marketing-practitioner/SKILL.md skills/marketing-practitioner/agents/openai.yaml
git commit -m "fix: stabilize skill package metadata"
```

### Task 2: Case, Profile, and Run Models

**Files:**
- Create: `evals/behavioral/behavioral_eval/__init__.py`
- Create: `evals/behavioral/behavioral_eval/models.py`
- Create: `evals/behavioral/behavioral_eval/validation.py`
- Create: `evals/behavioral/schemas/case.schema.json`
- Create: `evals/behavioral/schemas/profile.schema.json`
- Create: `evals/behavioral/schemas/run.schema.json`
- Create: `evals/behavioral/tests/test_validation.py`

**Interfaces:**
- Produces: `CaseContract.from_dict(data: dict) -> CaseContract`
- Produces: `ArmProfile.from_dict(data: dict) -> ArmProfile`
- Produces: `RunState` enum and `RunRecord` dataclass.
- Produces: `load_cases(path: Path) -> list[CaseContract]`
- Produces: `load_profiles(path: Path) -> list[ArmProfile]`

- [ ] **Step 1: Write failing validation tests**

```python
def test_duplicate_case_identity_fails_closed(self):
    payload = {"schema_version": 1, "cases": [case("BEH-001"), case("BEH-001")]}
    path = self.write_json(payload)
    with self.assertRaisesRegex(ValidationError, "duplicate case identity"):
        load_cases(path)

def test_live_profile_requires_explicit_model_and_effort(self):
    data = profile(model="required-at-run", reasoning_effort="required-at-run")
    with self.assertRaisesRegex(ValidationError, "explicit model"):
        ArmProfile.from_dict(data, live=True)
```

- [ ] **Step 2: Run tests and verify RED**

Run: `python -B -m unittest evals.behavioral.tests.test_validation -v`

Expected: module import failure.

- [ ] **Step 3: Implement immutable dataclasses and fail-closed validation**

Use frozen dataclasses and enums. Reject unknown top-level keys in case/profile documents, duplicate identities, empty prompts, missing provenance, unsupported adapters, invalid expected relations, non-positive timeout/repetition values, and live profiles without explicit model/effort.

Use the schema documents as a portable external contract. Runtime validation remains explicit standard-library Python so CI needs no third-party JSON Schema package.

- [ ] **Step 4: Run focused and package tests**

Run: `python -B -m unittest evals.behavioral.tests.test_validation evals.behavioral.tests.test_package_validation -v`

Expected: PASS.

- [ ] **Step 5: Commit**

```powershell
git add evals/behavioral/behavioral_eval evals/behavioral/schemas evals/behavioral/tests/test_validation.py
git commit -m "feat(eval): add behavioral contract models"
```

### Task 3: Isolated Workspace and Evidence Hygiene

**Files:**
- Create: `evals/behavioral/behavioral_eval/workspace.py`
- Create: `evals/behavioral/behavioral_eval/evidence.py`
- Create: `evals/behavioral/tests/test_workspace.py`
- Create: `evals/behavioral/tests/test_evidence.py`

**Interfaces:**
- Produces: `hash_tree(root: Path) -> str`
- Produces: `build_run_workspace(case, profile, repo_root, destination) -> WorkspaceBinding`
- Produces: `preflight_workspace(binding: WorkspaceBinding) -> list[str]`
- Produces: `redact_text(text: str, roots: Sequence[Path], secret_values: Sequence[str]) -> str`
- Produces: `seal_bytes(data: bytes) -> str` using SHA-256.

- [ ] **Step 1: Write failing isolation/hash tests**

```python
def test_tree_hash_ignores_mtime_and_depends_on_relative_path_and_bytes(self):
    first = self.make_tree({"a.txt": "same"})
    digest = hash_tree(first)
    os.utime(first / "a.txt", (1, 1))
    self.assertEqual(digest, hash_tree(first))
    (first / "a.txt").write_text("changed", encoding="utf-8")
    self.assertNotEqual(digest, hash_tree(first))

def test_baseline_preflight_rejects_marketing_skill_contamination(self):
    binding = self.build_baseline()
    contaminated = binding.root / ".agents" / "skills" / "marketing-practitioner"
    contaminated.mkdir(parents=True)
    (contaminated / "SKILL.md").write_text("x", encoding="utf-8")
    self.assertIn("baseline contains marketing-practitioner", preflight_workspace(binding))
```

- [ ] **Step 2: Write failing redaction tests**

```python
def test_redacts_absolute_paths_and_secret_values(self):
    text = f"root={self.root} token={self.secret}"
    redacted = redact_text(text, [self.root], [self.secret])
    self.assertNotIn(str(self.root), redacted)
    self.assertNotIn(self.secret, redacted)
    self.assertIn("<WORKSPACE>", redacted)
    self.assertIn("<REDACTED>", redacted)
```

- [ ] **Step 3: Run tests and verify RED**

Run: `python -B -m unittest evals.behavioral.tests.test_workspace evals.behavioral.tests.test_evidence -v`

Expected: module import failure.

- [ ] **Step 4: Implement deterministic copying, hashing, preflight, and redaction**

Initialize each temporary workspace with `git init`. Copy no repository file unless the case lists it. Copy the skill only for `workspace-copy` profiles at `.agents/skills/marketing-practitioner/`. Exclude cache files and reject symlinks that resolve outside the source skill.

Preflight checks the expected skill presence/absence, exact hash, absence of result/golden-answer material, and successful Git initialization.

- [ ] **Step 5: Run all behavioral tests**

Run: `python -B -m unittest discover -s evals/behavioral/tests -v`

Expected: PASS.

- [ ] **Step 6: Commit**

```powershell
git add evals/behavioral/behavioral_eval/workspace.py evals/behavioral/behavioral_eval/evidence.py evals/behavioral/tests/test_workspace.py evals/behavioral/tests/test_evidence.py
git commit -m "feat(eval): isolate behavioral run workspaces"
```

### Task 4: Fixture Adapter and Run State Machine

**Files:**
- Create: `evals/behavioral/behavioral_eval/adapters.py`
- Create: `evals/behavioral/behavioral_eval/fixture.py`
- Create: `evals/behavioral/behavioral_eval/runner.py`
- Create: `evals/behavioral/tests/test_runner.py`

**Interfaces:**
- Produces: `ExecutorRequest` and `ExecutorResult` dataclasses.
- Produces: `ExecutorAdapter.execute(request: ExecutorRequest) -> ExecutorResult` protocol.
- Produces: `FixtureAdapter` configured by a mapping of case/profile IDs to fixture envelopes.
- Produces: `run_condition(case, profile, adapter, paths, clock) -> RunRecord`.

- [ ] **Step 1: Write failing state-transition tests**

```python
def test_timeout_is_operational_failure_not_answer_failure(self):
    adapter = FixtureAdapter({self.key: fixture_result(timed_out=True)})
    record = run_condition(self.case, self.profile, adapter, self.paths, self.clock)
    self.assertEqual(RunState.TIMED_OUT, record.state)
    self.assertIsNone(record.answer_disposition)

def test_missing_final_output_is_invalid_output(self):
    adapter = FixtureAdapter({self.key: fixture_result(final_output=None)})
    record = run_condition(self.case, self.profile, adapter, self.paths, self.clock)
    self.assertEqual(RunState.INVALID_OUTPUT, record.state)
```

- [ ] **Step 2: Run test and verify RED**

Run: `python -B -m unittest evals.behavioral.tests.test_runner -v`

Expected: module import failure.

- [ ] **Step 3: Implement the adapter boundary and state machine**

Seal raw events and final output before predicate evaluation. Map timeout, non-zero exit, malformed required envelope, missing final output, preflight error, and activation uncertainty to distinct operational states. Retain unknown raw events as evidence.

- [ ] **Step 4: Add interruption and unknown-event regressions**

Add tests proving an interrupted fixture cannot produce `completed`, and a completed fixture with an unknown event type preserves that event without failing.

- [ ] **Step 5: Run all behavioral tests**

Run: `python -B -m unittest discover -s evals/behavioral/tests -v`

Expected: PASS.

- [ ] **Step 6: Commit**

```powershell
git add evals/behavioral/behavioral_eval/adapters.py evals/behavioral/behavioral_eval/fixture.py evals/behavioral/behavioral_eval/runner.py evals/behavioral/tests/test_runner.py
git commit -m "feat(eval): add sealed run state machine"
```

### Task 5: Codex CLI Adapter

**Files:**
- Create: `evals/behavioral/behavioral_eval/codex_cli.py`
- Create: `evals/behavioral/tests/test_codex_cli.py`

**Interfaces:**
- Produces: `build_codex_command(request: ExecutorRequest) -> list[str]`.
- Produces: `CodexCliAdapter(executable: Sequence[str] = ("codex",))`.
- Consumes: `ExecutorRequest` from Task 4.
- Produces: `ExecutorResult` with raw JSONL, stderr, final output, exit status, timeout flag, executable version, and elapsed time.

- [ ] **Step 1: Write failing command-construction test**

```python
def test_command_uses_explicit_isolated_live_configuration(self):
    command = build_codex_command(self.request)
    self.assertIn("--json", command)
    self.assertIn("--ephemeral", command)
    self.assertIn("--ignore-user-config", command)
    self.assertEqual("read-only", command[command.index("--sandbox") + 1])
    self.assertEqual(self.profile.model, command[command.index("--model") + 1])
    self.assertIn(f'model_reasoning_effort="{self.profile.reasoning_effort}"', command)
```

- [ ] **Step 2: Write failing subprocess behavior tests**

Use a temporary Python fake executable that emits JSONL and writes the requested final-output file. Add separate tests for success, malformed JSONL retention, non-zero exit, and a 0.2-second timeout against a child that waits for 2 seconds.

- [ ] **Step 3: Run tests and verify RED**

Run: `python -B -m unittest evals.behavioral.tests.test_codex_cli -v`

Expected: module import failure.

- [ ] **Step 4: Implement Codex command and subprocess control**

Pass the prompt through stdin, never through shell interpolation. Use `subprocess.Popen` with argument arrays, `communicate(timeout=...)`, process-tree termination on timeout, and UTF-8 replacement only for undecodable executor bytes while retaining byte hashes.

- [ ] **Step 5: Run behavioral tests**

Run: `python -B -m unittest discover -s evals/behavioral/tests -v`

Expected: PASS with no child processes left running.

- [ ] **Step 6: Commit**

```powershell
git add evals/behavioral/behavioral_eval/codex_cli.py evals/behavioral/tests/test_codex_cli.py
git commit -m "feat(eval): add Codex CLI executor adapter"
```

### Task 6: Predicates, Blind Packets, and Paired Reports

**Files:**
- Create: `evals/behavioral/behavioral_eval/adjudication.py`
- Create: `evals/behavioral/behavioral_eval/report.py`
- Create: `evals/behavioral/tests/test_adjudication.py`
- Create: `evals/behavioral/tests/test_report.py`

**Interfaces:**
- Produces: `evaluate_hard_predicates(case, output) -> list[PredicateResult]`.
- Produces: `build_blind_packet(case, run) -> dict`.
- Produces: `pair_runs(case, baseline_runs, skill_runs) -> PairRecord`.
- Produces: `build_report(cases, runs, judgments) -> dict`.

- [ ] **Step 1: Write failing blind-packet tests**

```python
def test_blind_packet_omits_arm_route_and_failure_identity(self):
    packet = build_blind_packet(self.case, self.skill_run)
    serialized = json.dumps(packet)
    self.assertNotIn(self.skill_run.profile_id, serialized)
    self.assertNotIn("paid-media.observation", serialized)
    self.assertNotIn("F8", serialized)
```

- [ ] **Step 2: Write failing paired-report tests**

```python
def test_invalid_run_is_counted_but_not_scored_as_answer_failure(self):
    report = build_report([self.case], [self.timeout_run], [])
    self.assertEqual(1, report["denominators"]["operationally_invalid"])
    self.assertEqual(0, report["denominators"]["answer_failures"])
```

- [ ] **Step 3: Run tests and verify RED**

Run: `python -B -m unittest evals.behavioral.tests.test_adjudication evals.behavioral.tests.test_report -v`

Expected: module import failure.

- [ ] **Step 4: Implement objective predicates and blind packets**

Support only explicit predicate types: `output_present`, `max_characters`, `must_contain_literal`, `must_not_contain_literal`, and `valid_json`. Reject unknown predicates. Keep semantic criteria human-readable and out of automatic pass/fail computation.

- [ ] **Step 5: Implement paired dispositions and denominators**

Produce `both_pass`, `skill_only_pass`, `baseline_only_pass`, `both_fail`, `unresolved`, and `operationally_invalid`. Include case/family denominators and repeat instability. Do not calculate a single quality score.

- [ ] **Step 6: Run all behavioral tests and commit**

```powershell
python -B -m unittest discover -s evals/behavioral/tests -v
git add evals/behavioral/behavioral_eval/adjudication.py evals/behavioral/behavioral_eval/report.py evals/behavioral/tests/test_adjudication.py evals/behavioral/tests/test_report.py
git commit -m "feat(eval): generate blind paired reports"
```

### Task 7: Pilot Corpus, Profiles, and CLI

**Files:**
- Create: `evals/behavioral/cases/pilot-v1.json`
- Create: `evals/behavioral/profiles/baseline.json`
- Create: `evals/behavioral/profiles/current-skill.json`
- Create: `evals/behavioral/behavioral_eval/cli.py`
- Create: `evals/behavioral/README.md`
- Create: `evals/behavioral/tests/test_cli.py`
- Create: `evals/behavioral/tests/test_pilot_corpus.py`

**Interfaces:**
- Produces: `python -m evals.behavioral.behavioral_eval.cli validate`.
- Produces: `... run --cases ... --profiles ... --adapter fixture|codex-cli --results ...`.
- Produces: `... report --results ... --output ...`.

- [ ] **Step 1: Write failing CLI and corpus tests**

Assert that `validate` rejects duplicate case identities, the frozen pilot contains exactly 12 cases across all six required families, profiles bind baseline/current-skill isolation modes, and `run` refuses to overwrite an existing sealed result directory.

- [ ] **Step 2: Run tests and verify RED**

Run: `python -B -m unittest evals.behavioral.tests.test_cli evals.behavioral.tests.test_pilot_corpus -v`

Expected: missing CLI/corpus failure.

- [ ] **Step 3: Create the frozen 12-case corpus**

Use these IDs and sources:

```text
BEH-FAST-001  prebenchmark-runtime-smoke S1
BEH-FAST-002  search adversarial D01
BEH-STATE-001 landing-page adversarial L1
BEH-EVID-001  handbook customer-evidence prevalence boundary
BEH-CAUSE-001 prebenchmark-runtime-smoke S3
BEH-DISC-001  search adversarial D03
BEH-COM-001   commerce Shopee buyer-relative price case
BEH-EMAIL-001 email observation click/intent boundary
BEH-PAID-001  paid-media adversarial reported/optimized event case
BEH-PAID-002  paid-media adversarial shared budget boundary case
BEH-PAID-003  paid-media adversarial attribution/causality case
BEH-PAID-004  paid-media adversarial delivered/seen case
```

Freeze complete user-visible prompts and decision-linked review criteria from the cited sources. Do not include the expected route or answer in executor-visible fields.

- [ ] **Step 4: Implement CLI orchestration and atomic result writes**

Write to a sibling temporary directory, fsync files, then rename to the final run bundle. Refuse overwrite unless the target is empty and explicitly created for the invocation.

- [ ] **Step 5: Validate corpus and run fixture smoke**

Run:

```powershell
python -B -m evals.behavioral.behavioral_eval.cli validate --cases evals\behavioral\cases\pilot-v1.json --profiles evals\behavioral\profiles
python -B -m unittest discover -s evals/behavioral/tests -v
```

Expected: PASS.

- [ ] **Step 6: Commit**

```powershell
git add evals/behavioral
git commit -m "feat(eval): add frozen behavioral pilot corpus"
```

### Task 8: One-Command Verification and CI

**Files:**
- Create: `scripts/verify.ps1`
- Create: `.github/workflows/verify.yml`
- Create: `evals/behavioral/tests/test_verify_entrypoint.py`

**Interfaces:**
- Produces: `scripts/verify.ps1 [-SkillPath <path>] [-PackageOnly]`.
- Produces: non-zero exit on the first failing verification command.

- [ ] **Step 1: Write failing entrypoint behavior test**

Create an invalid temporary skill and invoke PowerShell:

```python
completed = subprocess.run([
    "powershell", "-NoProfile", "-File", str(VERIFY),
    "-SkillPath", str(invalid_skill), "-PackageOnly"
], capture_output=True, text=True)
self.assertNotEqual(0, completed.returncode)
self.assertIn("description exceeds 1024 characters", completed.stderr + completed.stdout)
```

Also assert that a valid package-only run exits `0`.

- [ ] **Step 2: Run test and verify RED**

Run: `python -B -m unittest evals.behavioral.tests.test_verify_entrypoint -v`

Expected: missing script failure.

- [ ] **Step 3: Implement fail-fast verification**

Use `$ErrorActionPreference = 'Stop'`, invoke each external command with an argument array, inspect `$LASTEXITCODE` immediately, and exit with the failing code. Discover the external Codex validator under `$env:CODEX_HOME` and the standard user Codex path; print `SKIP` when absent and never print `PASS` for it unless executed.

Full verification runs the commands listed in the design, using `python -B` to avoid cache artifacts.

- [ ] **Step 4: Add the thin CI workflow**

Use `windows-latest`, checkout, Python 3.13 setup, then:

```yaml
- name: Verify repository
  shell: powershell
  run: .\scripts\verify.ps1
```

CI does not duplicate individual commands.

- [ ] **Step 5: Verify fail and pass paths**

Run:

```powershell
python -B -m unittest evals.behavioral.tests.test_verify_entrypoint -v
.\scripts\verify.ps1
```

Expected: tests and complete verification PASS; external Codex validator PASS locally.

- [ ] **Step 6: Commit**

```powershell
git add scripts/verify.ps1 .github/workflows/verify.yml evals/behavioral/tests/test_verify_entrypoint.py
git commit -m "ci: add one-command repository verification"
```

### Task 9: Live Smoke and Frozen 48-Run Pilot

**Files:**
- Generated and ignored: `evals/behavioral/results/smoke-*/`
- Generated and ignored: `evals/behavioral/results/pilot-v1-*/`
- Create after execution: `evals/behavioral/reports/current-skill-pilot-v1.md`
- Create after execution: `evals/behavioral/reports/current-skill-pilot-v1-summary.json`

**Interfaces:**
- Consumes: frozen cases and baseline/current-skill profiles.
- Produces: sealed local raw bundles plus redacted checked-in summary/report.

- [ ] **Step 1: Run two fixture conditions and inspect evidence manually**

Confirm raw hashes, relative paths, redaction, state, predicates, and blind packets match the fixture source.

- [ ] **Step 2: Execute 4-6 live smoke runs**

Use `gpt-5.6-terra` with `medium` reasoning, two representative cases, baseline/current-skill arms, and at least one repeated arm. If the model is unavailable, record `operationally_invalid` and stop without automatic model substitution.

- [ ] **Step 3: Audit smoke acceptance criteria**

Verify skill discovery/activation evidence, baseline contamination absence, identical model/effort, executor/event capture, final output, timeout behavior, redaction, and result-directory cleanliness. Correct harness defects with a new failing test before rerunning an affected smoke condition.

- [ ] **Step 4: Execute the 48-run pilot**

Run all 12 cases across baseline/current-skill with two exact repetitions per condition. Seal the complete run configuration before execution. Do not change cases or profiles after observing outputs.

- [ ] **Step 5: Produce blind packets and obtain judgments**

Generate condition-blind packets. Record deterministic predicates separately from semantic judgments. Mark missing independent judgment as `unresolved`; do not let an LLM self-judge produce a benchmark-grade pass.

- [ ] **Step 6: Generate and review the checked-in report**

The report includes configuration, case/family denominators, paired dispositions, repeat instability, operational failures, judgment provenance, and limitations. It contains no single quality score.

- [ ] **Step 7: Commit only redacted reports**

```powershell
git add evals/behavioral/reports
git commit -m "eval: record current-skill behavioral pilot"
```

### Task 10: Compact Controller Challenger

**Files:**
- Create: `evals/behavioral/challengers/compact-controller/marketing-practitioner/SKILL.md`
- Create: `evals/behavioral/challengers/compact-controller/marketing-practitioner/references/runtime-routing.md`
- Create: `evals/behavioral/profiles/compact-challenger.json`
- Create: `evals/behavioral/tests/test_compact_challenger.py`
- Modify only after promotion: `skills/marketing-practitioner/SKILL.md`
- Modify only after promotion: `skills/marketing-practitioner/references/runtime-routing.md`

**Interfaces:**
- Produces: a complete installable challenger copy with its own deterministic hash.
- Produces: `controller_metrics(skill_root: Path) -> {bytes, words, lines}`.

- [ ] **Step 1: Write failing challenger integrity tests**

Load the expected challenger path and assert required invariants: valid package, same metadata version candidate suffix, all operating-path names represented, universal invariants retained, all namespace names discoverable, state-handoff coverage retained, and at least 25% fewer controller words than v0.9.0. The test fails initially because the expected challenger package is absent.

- [ ] **Step 2: Run test and verify RED**

Run: `python -B -m unittest evals.behavioral.tests.test_compact_challenger -v`

Expected: challenger missing.

- [ ] **Step 3: Build the challenger without modifying the installed skill**

Copy all v0.9.0 resources, replace only `SKILL.md`, and add `references/runtime-routing.md`. Keep the eight-step runtime controller, six universal invariants, fast paths, owner selection, namespace activation boundaries, handoffs, and final validation. Move verbose domain dependency examples and repeated owner maps into the routed reference.

- [ ] **Step 4: Run deterministic challenger checks**

Run package validation, route/source validation from the challenger copy, routing mechanics tests against an injected root, and the integrity/size tests.

- [ ] **Step 5: Run the frozen behavioral comparison**

Execute the challenger using the same cases, model, reasoning, and two repetitions as the current-skill pilot. Generate paired current-skill/challenger dispositions.

- [ ] **Step 6: Adjudicate promotion gate**

Reject promotion on any uncorrected hard-predicate regression, increased activation/routing failure, or current-pass/challenger-fail case. If the gate passes, replace the installed controller with the exact evaluated challenger bytes and add the exact evaluated routing reference; verify their hashes match the run profile.

- [ ] **Step 7: Commit challenger evidence or promoted controller**

Use one of:

```powershell
git commit -m "eval: retain compact controller challenger"
git commit -m "refactor: promote evaluated compact controller"
```

The commit message must reflect the actual gate outcome.

### Task 11: README, Changelog, and Release Evidence

**Files:**
- Modify: `README.md`
- Modify: `CHANGELOG.md`
- Create: `evals/behavioral/reports/stabilization-completion-audit.md`

**Interfaces:**
- Consumes: actual current-skill/challenger reports and verification output.
- Produces: public claims that match executed evidence.

- [ ] **Step 1: Write the completion-audit evidence matrix**

List each design acceptance criterion, its proving artifact/command, status, and limitation. Mark indirect or missing evidence incomplete.

- [ ] **Step 2: Reduce README duplication**

Retain value proposition, quick start, representative tasks, reasoning model, evidence discipline, compact repository map, status, installation, and contributing links. Move deep capability exposition to existing handbook/platform navigation. Preserve all non-ASCII text and links.

- [ ] **Step 3: Update changelog without benchmark inflation**

Separate package/mechanical validation, live smoke, frozen pilot, challenger result, and remaining unknowns. Do not claim universal reliability or independent human judgment unless the report contains it.

- [ ] **Step 4: Verify documentation evidence and links**

Run link/path checks, search for stale version strings, validate description/UI metadata, and compare every numeric claim against generated summaries.

- [ ] **Step 5: Commit**

```powershell
git add README.md CHANGELOG.md evals/behavioral/reports/stabilization-completion-audit.md
git commit -m "docs: align release claims with behavioral evidence"
```

### Task 12: Full Verification and Completion Audit

**Files:**
- Modify if evidence changes: `evals/behavioral/reports/stabilization-completion-audit.md`

**Interfaces:**
- Consumes: all plan tasks and current worktree state.
- Produces: final evidence-backed completion decision.

- [ ] **Step 1: Run the sole verification entrypoint from a clean process**

Run: `powershell -NoProfile -File .\scripts\verify.ps1`

Expected: every mandatory local gate exits `0`; external Codex validator is recorded as executed PASS.

- [ ] **Step 2: Verify Git hygiene**

Run:

```powershell
git diff --check
git status --short
git ls-files "*__pycache__*" "*.pyc" "evals/behavioral/results/*"
```

Expected: no whitespace errors, no uncommitted changes intended for delivery, and no generated/cache artifacts tracked.

- [ ] **Step 3: Reconcile every acceptance criterion**

Re-read the design and plan. For each numbered criterion, open the proving file or rerun the proving command. Do not infer completion from adjacent tests.

- [ ] **Step 4: Record the final audit and commit any evidence correction**

If the audit file changes, commit with:

```powershell
git add evals/behavioral/reports/stabilization-completion-audit.md
git commit -m "docs: finalize stabilization evidence audit"
```

- [ ] **Step 5: Report actual status**

Report completed gates, exact test/run counts, challenger promotion outcome, remaining limitations, branch/commit state, and any external action still required. Do not mark the goal complete while any design acceptance criterion lacks direct evidence.

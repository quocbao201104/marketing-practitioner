# Behavioral Evaluation and Skill Stabilization Design

## Status

Approved direction: structured local harness, smoke-first live execution, and evidence-gated controller compaction.

Frozen behavioral baseline: `v0.9.0` at commit `bb53cadce87546ae8c7cd9eab1aa1985a32cd9df`.

## Purpose

Move Marketing Practitioner from a research-heavy, mechanically validated skill toward a reproducible behavioral evaluation and release discipline without adding another marketing capability surface.

The work has four outcomes:

1. make the installable skill pass current Codex packaging validation;
2. provide one deterministic local verification entrypoint that CI can call when GitHub Actions quota is available;
3. execute reproducible baseline-versus-skill behavioral runs with sealed evidence and blind-review packets;
4. test a smaller controller as a challenger and promote it only when behavioral evidence shows no material regression.

## Governing constraints

- Preserve UTF-8 and the repository's CRLF convention for existing files.
- Keep `v0.9.0` immutable as the current-skill baseline.
- Do not change marketing theory, add a chapter, add a platform, or introduce a new controller job during stabilization.
- Do not use chain-of-thought or private reasoning traces as evaluation evidence.
- Do not treat fixture tests, static walkthroughs, or model-judge agreement as proof of broad runtime reliability.
- Do not reduce behavioral results to one aggregate quality score.
- Generated run outputs must not be committed by default.
- Live execution begins with 4-6 smoke runs. The 48-run pilot starts only after smoke evidence proves activation, isolation, capture, timeout, and report plumbing.

## Considered approaches

### Markdown-driven manual execution

This would reuse the existing adversarial Markdown files and record answers by hand. It is cheap to start but makes case parsing, repetition, version binding, and result comparison fragile. It is rejected as the primary harness.

### Structured local harness

This uses versioned JSON case contracts, explicit arm profiles, a fixture adapter, a Codex CLI adapter, sealed run records, and generated adjudication packets. It provides enough structure for reproducibility while remaining small and local. This is the selected approach.

### Full benchmark service

A database, web dashboard, queue, multi-provider executor, and automatic judge service would add operational complexity before the local method is proven. It is explicitly out of scope.

## Repository structure

```text
evals/behavioral/
|-- README.md
|-- cases/
|   `-- pilot-v1.json
|-- profiles/
|   |-- baseline.json
|   `-- current-skill.json
|-- schemas/
|   |-- case.schema.json
|   |-- profile.schema.json
|   `-- run.schema.json
|-- behavioral_eval/
|   |-- __init__.py
|   |-- models.py
|   |-- validation.py
|   |-- workspace.py
|   |-- adapters.py
|   |-- codex_cli.py
|   |-- fixture.py
|   |-- runner.py
|   |-- adjudication.py
|   |-- report.py
|   `-- cli.py
`-- tests/
    |-- test_validation.py
    |-- test_workspace.py
    |-- test_runner.py
    |-- test_adjudication.py
    `-- test_report.py

scripts/
`-- verify.ps1

.github/workflows/
`-- verify.yml
```

Generated evidence is written under `evals/behavioral/results/`, which is ignored except for an optional checked-in human-readable example that is explicitly labeled as a fixture.

## Stabilization changes

### Skill discovery and packaging

The `SKILL.md` frontmatter description will be rewritten as a concise, discriminating activation description under 1,024 characters. It will name the major decision families and the evidence/causality boundary without enumerating every artifact or platform.

`skills/marketing-practitioner/agents/openai.yaml` will contain only UI metadata:

```yaml
interface:
  display_name: "Marketing Practitioner"
  short_description: "Evidence-informed marketing decisions"
  default_prompt: "Use $marketing-practitioner to make a bounded marketing decision from the evidence and constraints I provide."
```

Implicit invocation remains at its default. No MCP dependency is declared because the skill can operate without one.

### Local verification

`scripts/verify.ps1` is the sole maintained verification entrypoint. It runs, in fail-fast order:

1. the repository-owned package/frontmatter validator;
2. the current Codex skill validator when its installed path is discoverable;
3. knowledge-route mechanics tests;
4. full route/source validation;
5. Pressure Discovery pilot tests;
6. behavioral harness unit tests;
7. UTF-8 and generated-artifact hygiene checks.

The repository-owned validator preserves a stable CI floor. A local release gate must additionally pass the installed current Codex validator; absence of that external validator is reported explicitly and cannot be represented as an executed pass. The GitHub Actions workflow invokes the same verification script. CI contains no independent test logic, so local and hosted verification cannot silently drift.

## Behavioral case contract

Each case has immutable identity and observable evaluation criteria:

```json
{
  "case_id": "BEH-FAST-001",
  "version": "1.0.0",
  "family": "fast-path",
  "prompt": "...",
  "input_files": [],
  "hard_predicates": [],
  "review_criteria": [],
  "forbidden_disclosures": [],
  "expected_relation": "skill_not_worse",
  "provenance": {
    "source": "evals/prebenchmark-runtime-smoke.md#S1",
    "frozen_at_commit": "bb53cadce87546ae8c7cd9eab1aa1985a32cd9df"
  }
}
```

Hard predicates cover only objectively testable properties such as output presence, forbidden fabricated fact, required refusal state, or structured response validity. Semantic quality remains in blind review criteria; it is not approximated with keyword counts when wording can legitimately vary.

The pilot spans at least these families:

- fast-path proportionality;
- resolved-state preservation;
- evidence and unsupported-claim control;
- causal diagnosis before tactic change;
- commerce/discovery owner routing;
- paid-media allocation, observation, and attribution boundaries.

## Arm profiles and isolation

An arm profile identifies the executor configuration and skill package:

```json
{
  "profile_id": "current-skill-v0.9.0",
  "adapter": "codex-cli",
  "model": "required-at-run",
  "reasoning_effort": "required-at-run",
  "skill_mode": "workspace-copy",
  "skill_source": "skills/marketing-practitioner",
  "expected_skill_sha256": "computed-at-run-bind"
}
```

For every run, the harness creates a new temporary Git workspace containing only the case package and the files needed by that arm. Live profiles must resolve `model` and `reasoning_effort` to explicit values before the first run; all compared arms use the same resolved pair.

- Baseline workspace contains no Marketing Practitioner skill and runs with user configuration ignored while retaining Codex authentication.
- Current-skill workspace contains an exact copy of the frozen installable skill at `.agents/skills/marketing-practitioner/`.
- Challenger workspace later contains the compact candidate and records a different content hash.

Preflight rejects a run if the baseline contains the skill, the skill arm lacks it, the computed content hash differs from the bound hash, or the workspace contains unexpected case-answer material.

## Executor adapters

### Fixture adapter

The fixture adapter returns predefined event and output envelopes. It validates the harness without network/model cost and must cover success, timeout, non-zero exit, malformed JSONL, missing final output, activation failure, and interrupted-run cases.

### Codex CLI adapter

The Codex adapter launches `codex exec` non-interactively with:

- a new temporary workspace;
- read-only sandboxing for evaluation tasks;
- `--ephemeral` session behavior;
- `--ignore-user-config` for configuration isolation;
- JSONL event output;
- an explicit timeout;
- a final-output file separate from the event log.

The adapter stores the executable version, requested model/config, exit code, timestamps, raw event stream hash, final-output hash, and stderr. It never stores authentication material or the contents of unrelated user configuration.

Codex event fields are treated as versioned external input. Unknown event types are retained rather than rejected; only the minimal fields required for run status are interpreted.

## Run lifecycle

```text
CASE + PROFILE
-> VALIDATE
-> BIND SKILL HASH AND EXECUTOR VERSION
-> BUILD ISOLATED WORKSPACE
-> PREFLIGHT ISOLATION
-> EXECUTE WITH TIMEOUT
-> CAPTURE RAW EVIDENCE
-> SEAL RUN RECORD
-> APPLY OBJECTIVE PREDICATES
-> GENERATE BLIND-REVIEW PACKET
-> REPORT ARM DISPOSITION
```

Run states are:

- `completed`;
- `executor_failed`;
- `timed_out`;
- `invalid_output`;
- `activation_unverified`;
- `isolation_failed`.

An operational failure is never scored as an answer failure. A missing or unverified skill activation invalidates the skill-arm comparison instead of being silently interpreted as poor skill behavior.

## Evidence and redaction

Every run record includes:

- case ID/version and prompt hash;
- profile ID and skill hash;
- executor/model/config identity as observable;
- timestamps, timeout, exit status, and event count;
- hashes and paths relative to the result bundle;
- objective predicate results;
- review-packet ID;
- operational limitations.

Before persistence, the harness redacts absolute user-home/workspace paths and known secret-shaped environment values. It does not record environment dumps. Raw executor evidence remains local and ignored by Git.

## Adjudication and reporting

The harness generates condition-blind packets that contain the user-visible task, candidate answer, controlling predicates, and criteria, but omit arm identity, expected route, and proposed failure class.

Reports use per-family and paired dispositions:

- `both_pass`;
- `skill_only_pass`;
- `baseline_only_pass`;
- `both_fail`;
- `unresolved`;
- `operationally_invalid`.

The report includes denominators and repetition instability. It does not publish an Elo, win rate, or single aggregate quality score from the smoke or pilot.

## Compact-controller challenger

Controller compaction begins only after the current-skill pilot is sealed. The compact candidate may move conditional domain route maps out of `SKILL.md`, shorten repeated owner-boundary language, and reduce examples, while preserving:

- the runtime controller;
- universal invariants;
- fast-path behavior;
- resolved-state freezing;
- dependency-first JIT routing;
- domain activation criteria;
- state handoffs;
- final validation.

The challenger is evaluated against the same frozen cases and executor configuration. It is promoted only when:

- no hard-predicate regression occurs;
- no failure family changes from current-skill pass to challenger fail without adjudicated justification;
- over-routing does not increase;
- route/activation failures do not increase;
- context size decreases materially.

If those conditions are not met, `v0.9.0` behavior remains authoritative and the challenger stays experimental.

## README and release changes

README reduction happens after the pilot so claims reflect measured behavior. The root README will retain the value proposition, quick start, representative use cases, evidence boundaries, repository map, status, and installation. Deep capability catalogs move to existing handbook/platform navigation rather than being duplicated.

The next release is a stabilization release, not a capability release. Its changelog must distinguish mechanical validation, live behavioral execution, adjudication status, and remaining limitations.

## Testing strategy

All new Python behavior follows red-green-refactor. Tests use temporary directories and real subprocess fixtures where safe.

Required regression coverage:

- duplicate IDs and invalid schema fail closed;
- baseline/skill workspace contamination is rejected;
- skill hashes are deterministic across copied workspaces;
- timeouts terminate the executor and seal an operational failure;
- malformed or incomplete event streams cannot become completed runs;
- unknown Codex event types are retained;
- absolute paths and secret-shaped values are redacted;
- interrupted runs do not produce valid comparisons;
- blind packets do not reveal arm identity;
- report denominators include invalid and unresolved runs;
- the verification entrypoint propagates the first failing exit code.

Configuration-only files are validated by schema/parser tests and the current Codex skill validator.

## Acceptance criteria

The project is ready for the 48-run pilot when:

1. the installable skill passes current packaging validation;
2. the one-command local verification suite passes from a clean checkout;
3. the fixture harness passes all failure-mode tests;
4. baseline and current-skill workspaces pass contamination/hash preflight;
5. 4-6 live smoke runs complete with sealed evidence and correct operational dispositions;
6. generated blind packets omit arm identity and expected failure labels;
7. the worktree remains free of generated result artifacts.

The broader stabilization objective is complete only after the current-skill pilot is sealed, the compact challenger has been evaluated against the same frozen cases, README/release claims match that evidence, and all verification gates pass.

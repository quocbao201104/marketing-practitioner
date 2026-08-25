# Stabilization completion audit

Audited: 2026-08-25  
Branch: `codex/behavioral-eval-stabilization`

## Design acceptance criteria

| Criterion | Direct evidence | Status | Limitation |
| --- | --- | --- | --- |
| Installable skill passes current package validation | `scripts/verify.ps1`; repository and installed Codex validators | PASS | The external validator is environment-owned and must execute again at each release gate. |
| One-command verification passes from a clean process | `powershell -NoProfile -File .\scripts\verify.ps1` | PASS | GitHub-hosted execution still depends on available Actions quota; local execution is direct. |
| Fixture harness passes failure-mode tests | Behavioral `unittest` suite covering validation, isolation, redaction, executor failure, timeout, interruption, predicates, blind packets, reports, CLI, and overwrite refusal | PASS | Fixture outputs validate plumbing, not marketing behavior. |
| Baseline and current-skill workspaces pass contamination/hash preflight | `test_workspace.py`, sealed pilot manifests, exact current-skill hash `e15916…20c1` | PASS | Preflight proves workspace state, not semantic skill use; activation evidence remains separate. |
| Four to six live smoke runs complete with correct operational dispositions | Six sealed smoke runs across FAST-001 and PAID-001; launcher and escaped-path defects received regression tests | PASS | Early smoke runs intentionally retain executor/activation-invalid dispositions rather than being relabeled. |
| Blind packets omit arm identity and expected failure labels | `test_adjudication.py`; opaque-ID ordering regression; reviewed packets | PASS | Semantic review was condition-blind but not independently human-adjudicated. |
| Worktree remains free of generated result artifacts | `.gitignore`, verification hygiene gate, `git ls-files` audit | PASS | Raw local bundles exist under ignored `evals/behavioral/results/` and are not release artifacts. |

## Broader completion conditions

| Condition | Evidence | Status |
| --- | --- | --- |
| Current-skill pilot sealed | 48 runs, 12 cases, two arms, two repetitions; [pilot report](current-skill-pilot-v1.md) | PASS |
| Pilot reports operational failures separately | 45 answer-bearing; three activation-unverified; no operational failure counted as an answer failure | PASS |
| No inflated aggregate quality score | Reports publish denominators and paired dispositions only | PASS |
| Compact challenger evaluated on frozen cases | 24 challenger runs with identical model/effort/cases/repetitions | PASS |
| Promotion follows evidence gate | [Challenger report](compact-challenger-v1.md) rejects promotion after activation-unverified increased 3/24 → 7/24 | PASS |
| Installed v0.9.0 controller remains authoritative after rejection | `skills/marketing-practitioner/SKILL.md` was not replaced by challenger bytes | PASS |
| README/changelog claims match executed evidence | README links the redacted reports; changelog distinguishes package checks, pilot, review provenance, challenger rejection, and unknowns | PASS |
| Sole verification entrypoint passes after all changes | Final clean-process run: repository validator PASS; installed Codex validator PASS; 58 routing checks; 249 routes/203 sources; 138 Pressure Discovery tests; 53 behavioral tests; hygiene PASS | PASS |

## Evidence boundaries

- The 48-run pilot is a small repository decision instrument, not a population benchmark.
- Semantic judgments came from the implementation-session Codex assistant. They were condition-blind but not independent human review.
- Eight pairs were both-pass, three operationally invalid, and one unresolved. There was no skill-only or baseline-only pass in this run.
- Activation observability is a material host/runtime limitation. Answer text from an activation-unverified run is retained but excluded from valid comparison.
- GitHub Actions configuration is present, but no hosted run is claimed in this audit. Local verification is the direct evidence available here.

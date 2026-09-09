# Repository Guidelines

## Project Structure & Module Organization

This repository maintains Marketing Practitioner, a research-first marketing decision skill for AI agents.

- `skills/marketing-practitioner/` is the distributable runtime: `SKILL.md` controls behavior; `handbook/`, `platforms/`, `adaptations/`, and `frameworks/` hold guidance; `references/` records evidence; `routing-index.json` and `scripts/` support retrieval.
- Root `scripts/` contains validation, packaging, and asset tooling.
- `evals/` contains smoke cases, audits, and Python evaluation harnesses; `research/` preserves provenance rather than runtime instructions.
- `docs/` covers setup and design; `assets/` holds visual materials; `.codex-plugin/` and `.claude-plugin/` contain distribution metadata.

## Build, Test, and Development Commands

Run from the repository root with Python available. CI uses Python 3.13 and Windows PowerShell. There is no application development server.

- `.\scripts\verify.ps1` runs package validation, routing checks, both harness test suites, and UTF-8/generated-artifact checks.
- `.\scripts\verify.ps1 -PackageOnly` runs package validation only.
- `python -B skills/marketing-practitioner/scripts/test-knowledge-routing.py` checks retrieval mechanics.
- `python -B -m unittest discover -s evals/behavioral/tests -v` runs behavioral harness unit tests.
- `python -B scripts/package_skill.py ../marketing-practitioner.zip` creates a new portable ZIP from tracked runtime files using current working-tree bytes; existing output is never overwritten.

## Coding Style & Naming Conventions

Use formal, plain English and descriptive Markdown headings. Follow existing Python style: four-space indentation, `snake_case` functions, and `PascalCase` classes. Knowledge files generally use kebab-case names; numbered handbook chapters retain their existing prefixes. No standalone formatter or linter is configured.

Preserve UTF-8 text, Unicode, and existing line endings. Keep logical knowledge IDs distinct from file paths, and avoid duplicating handbook prose in routing metadata.

## Testing Guidelines

Harness tests use standard-library `unittest` and `test_*.py` names. Pressure Discovery tests live in `evals/pressure-discovery/pilot/tests/`. No numeric coverage threshold is configured. Follow `CONTRIBUTING.md`: inspect editorial changes; add targeted regressions, smoke cases, or counterexamples for runtime/shared-semantic changes. Fixture runs verify infrastructure, not behavioral quality. Use `-B` to avoid Python cache artifacts.

## Commit & Pull Request Guidelines

History commonly uses `docs:`, `feat:`, and scoped prefixes such as `chore(release):`. Keep subjects concise and changes focused.

For substantive PRs, describe the demonstrated failure, supporting evidence, smallest correction, affected surfaces, contribution risk level, validation performed, and remaining uncertainty. Follow `CONTRIBUTING.md` before changing shared architecture. Keep generated behavioral results and credentials out of Git; preserve delivered logo kits byte-for-byte.

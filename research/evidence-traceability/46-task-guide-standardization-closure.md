# Task Guide Standardization Closure

Date: 2026-09-08. Closes TS-A1 and TS-A2 from [review 45](45-core-task-decisions-and-completion-review.md), alongside the user's request to bring the older guide into alignment with the current skill.

## Changes

Updated the canonical [Task Specification Guide](../../skills/marketing-practitioner/TASK-SPECIFICATION-GUIDE.md) and its [evidence ledger](../../skills/marketing-practitioner/references/task-specification-evidence.md).

- **TS-A1:** the optional field arrangement is identified as a practical design choice informed by research. The unsupported comparison with an earlier grammar is removed.
- **TS-A2:** the ambiguity statement names the evaluated models rather than presenting a historical benchmark as a current capability assessment.
- **Sufficiency and evidence:** materiality now matches SKILL.md. Available conversation state should be used before requesting more input. Approved choices remain distinct from verified claims; necessary qualifications and counterevidence survive compression. Exploration may begin with bounded inspection before relevance is fully known.
- **Clarification and delegation:** the old ask-user row could include a choice already delegated or a fact recoverable from context. The revised table separates unresolved user-owned inputs, delegated choices, available authorization, external research, and useful bounded work. Uncertainty is surfaced when it matters to the recipient rather than appended mechanically to every artifact.
- **Continuity and completion:** the guide explains preservation of active outputs, affected-scope revision, cancelled versus paused work, and the limits of host-retained context. Completion means the requested usable result with its constraints and material remaining dependencies. A new example joins a delegated positioning choice to two dependent artifacts.
- **Delivery constraints:** presentation and evidence requirements have different roles, but an explicit field limit, language, or handoff format can be essential to usable completion. Semantic equivalence alone does not satisfy every delivery requirement.

The ledger adds selected method/transfer locators from the eight papers inspected in review 45. Source dates are scoped: TS02, TS10, and provider records TS11-TS13 retain their prior review status. The guide's provider references now state the recorded August review date. No new primary-source reading or current-provider verification is claimed by this correction turn.

## Design boundary

The user's broader standardization request justifies aligning guide defaults and examples beyond the two citation findings. These are reconciliations with the existing controller, not additional observed agent failures. The guide remains optional user-facing support, with SKILL.md governing execution. No new mandatory fields, runtime states, universal score, fixed investigation budget, or model-efficacy claim is introduced.

SKILL.md, quality rubrics, routing-index.json, and the root guide pointer remain unchanged. No live or historical agent pilot is used to validate the revised text.

## Verification

- `scripts/verify.ps1 -PackageOnly`: repository package validator and current Codex validator passed.
- `get-knowledge.py --validate`: passed with 264 routes and 240 evidence sources.
- Reviewed the targeted diff against current uncertainty, continuity, and completion rules. Preserved the existing guide headings and canonical root pointer.
- Final integrity checks cover local links/anchors, source identifiers, Unicode, encoding/BOM, CRLF, original end-of-file conventions, whitespace, and unchanged hashes of pre-existing files outside the two edited targets. Git status distinguishes these changes and this new report from earlier Google edits and reports 38-45.

Package and text checks establish structural integrity, not agent compliance or marketing outcomes. No additional behavioral tests, commit, push, release tag, or cleanup are included.

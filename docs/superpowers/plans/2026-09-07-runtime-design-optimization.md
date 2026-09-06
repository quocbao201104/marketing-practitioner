# Runtime Design Optimization Implementation Plan

**Goal:** Improve the controller and foundational content through theoretical and semantic review before behavioral experimentation.

**Architecture:** Preserve the current seven jobs, specialist ownership, logical routes, and resource layout. Clarify the shared decision contract and align the foundational chapters without new runtime abstractions.

**Spec:** [Design review](../../../research/runtime-design-optimization/01-design-review.md).

## Global constraints

- The user explicitly deferred behavioral experiments. Historical pilots do not choose or justify these edits.
- Work directly in the existing checkout; do not create branches, commit, push, or publish.
- Preserve UTF-8, BOM state, CRLF line endings, Unicode, existing release metadata, and unrelated files.
- Treat new operational wording as project synthesis, not measured model behavior.
- Execute locally in the current task; no agent experiment or delegated behavioral evaluation is part of this plan.

## Task 1: Clarify the runtime contract

File: `skills/marketing-practitioner/SKILL.md`.

- [x] Revise the existing eight-step controller to distinguish fixed constraints from hypotheses, admit learning questions, and preserve compound requested deliverables.
- [x] Add concise conditions for proceeding, retrieving, clarifying, and stopping under uncertainty; preserve the separate factual and authorization boundaries.
- [x] Define useful completion for the seven existing jobs without mandatory output templates.
- [x] Move existing retrieval mechanics into an in-file subsection; keep logical IDs, selector semantics, fallbacks, and domain-specific loading intact.
- [x] Align research activation and strategy/communication wording with the revised contract.

## Task 2: Align the theoretical content

Files: Chapters 00, 01, 03, 04 and `references/bibliography.md`.

- [x] Make the Chapter 00 cycle illustrative and its commitments compatible with exploratory research and provisional drafts.
- [x] Separate evidence needed for an empirical claim from justification for a bounded action under uncertainty.
- [x] Clarify the Chapter 01 research purpose using R21, with bounded discovery and source-led revision of questions.
- [x] Align Chapter 01 behavior/stated-preference guidance with question-specific evidence fit; distinguish reported behavior from direct observation and constrained choice from unconstrained preference.
- [x] Clarify Chapter 03 candidate versus adopted positioning and scoped output fields.
- [x] Clarify Chapter 04 exploratory message alternatives and provisional drafts while preserving the existing downstream representation owner.
- [x] Add primary-source links and the limited discovery interpretation to R21; preserve its identifier.

## Task 3: Review and verify the local revision

- [x] Review the paired static counterexamples D1-D8 in the spec without generating model outputs or scoring behavior.
- [x] Check unchanged specialist routes, source IDs, and semantic handoffs against the pre-edit bytes.
- [x] Run `powershell -NoProfile -File .\scripts\verify.ps1`; report these results only as package/infrastructure checks.
- [x] Inspect `git diff --check`, the full scoped diff, encoding/line-ending checks, and final `git status --short`.
- [x] Record actual verification and remaining uncertainty in the design review and report changed files to the user.

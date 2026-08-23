# Changelog

All notable changes to this repository are documented here.

The project uses semantic versioning for published skill revisions. Early versions may change structure while the conceptual model is stabilized.

## [0.2.0] - 2026-08-23

### Added

- Added `handbook/08-content-environments-and-distribution.md`, a compressed six-layer model for platform-native content, distribution, interaction, recommendation, governance, and evidence interpretation.
- Added production platform modules for Instagram, TikTok, LinkedIn, Facebook, and X, all using the same compact runtime vocabulary rather than separate platform-specific frameworks.
- Added implementation-backed X guidance using the public `xai-org/x-algorithm` For You implementation, with explicit boundaries against turning exposed ranking parameters into content hacks.
- Added research/audit artifacts for compact-core losslessness, runtime-routing adversarial walk-throughs, and a pre-benchmark execution smoke pack.

### Changed

- Extended the decision-first runtime controller with a platform-content/distribution operating path and just-in-time routing to Chapter 08 and the smallest relevant platform module.
- Compressed platform reasoning to eight durable things — actor/source, content object, content representation, audience state, typed relationship/delivery/permission edge, interaction act, platform/mediation state, and observation record — with provenance, scope/relativity, and history/state transition as cross-cutting modifiers.
- Added guardrails that keep content object, representation, surface, relationship, delivery, permission, observed action, system feedback, ranking objectives, attribution, and causality distinct when those distinctions can change a decision.
- Preserved a fast path for simple captions/posts so platform knowledge does not automatically expand a narrow writing task into strategy or recommender-system analysis.
- Expanded the bibliography and platform evidence base with current product documentation, recommender-system literature, representation architecture references, and scoped implementation evidence.

### Validation status

- A frozen 20-case conceptual losslessness audit produced 19 `LOSSLESS`, 1 `LOSSLESS / INTERNAL UNKNOWN`, 0 `PARTIAL`, and 0 `FAIL`; no retired primitive or new durable primitive was required.
- A 22-case static runtime-routing walk-through found 0 routing gaps and 0 knowledge gaps; execution reliability remains intentionally pre-benchmark and is expected to improve through real use and fresh smoke runs.
- This release does not claim universal platform theory, causal effectiveness of platform tactics, or benchmark-grade runtime reliability.

## [0.1.4] - 2026-08-22

### Changed

- Refactored the executable runtime around decision-first operating-path selection instead of one global default pipeline.
- Reduced always-on instructions to universal invariants and moved research, positioning, copy, diagnosis, localization, and learning guidance behind decision-point loading.
- Added explicit state handoffs so downstream stages receive only the conclusions, constraints, proof, and uncertainty needed for the next decision.
- Preserved the v0.1.3 audience-facing content-selection gate while strengthening source fidelity against unsupported first-person experience or preference.

## [0.1.3] - 2026-08-22

### Changed

- Improved audience-facing content selection during copywriting.
- Separated internal claim constraints from information that belongs in the final message.
- Required relevant details to justify their place against the reader's current decision and attention budget.
- Added an omission test that preserves material proof, limitations, uncertainty, and next-action information while avoiding unnecessary disclosure.

## [0.1.2] - 2026-08-22

### Changed

- Packaged the installable skill under `skills/marketing-practitioner/`.
- Moved `SKILL.md`, handbook, frameworks, and bibliography into the same skill directory so supporting resources travel with multi-file installations.
- Aligned the skill directory name with the frontmatter name `marketing-practitioner`.
- Updated README, contribution guidance, and attribution links for the packaged layout.

## [0.1.1] - 2026-08-22

### Added

- Skills CLI quick-start and install-count badge in the README.
- A short activation example showing the intended evidence-to-strategy-to-copy behavior.
- Explicit progressive-loading guidance for skills-compatible clients.
- Resource routing from operating modes to the relevant handbook, framework, and bibliography files.

### Changed

- The operational skill now tells agents to load only the smallest task-relevant set of supporting resources instead of consulting the repository broadly by default.

## [0.1.0] - 2026-08-21

### Added

- Initial English edition of the Marketing Practitioner skill.
- Evidence-informed operating model from market learning through copy and scoped learning.
- Academic handbook structure covering customer research, segmentation, positioning, messaging, copywriting, diagnosis, experimentation, organizational learning, localization, and ethics.
- Practitioner cards and quality rubrics for applied work.
- Selected bibliography emphasizing primary research, academic monographs, and methodological sources.
- Third-party attribution for the MIT-licensed AI Copywriter / humanizer lineage.

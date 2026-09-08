# Google Commerce Clarification Closure

Date: 2026-09-08. Closes the two local correction candidates in [report 38](38-google-commerce-data-state-review.md).

Status: GC1 and GC2 implemented and checked at the content/retrieval level. No live agent trial or merchant-account operation was performed.

## Changes

In [the Google module](../../skills/marketing-practitioner/platforms/commerce/google-shopping.md):

- Section 2 now separates submission success from completed processing, scopes approval and issues to the target destination/reporting context and country, and preserves visibility controls and measured exposure as separate evidence. It states the maintenance and coverage limits of automatic updates without imposing a universal waiting period.
- Section 3.3 connects variant identity to the submitted URL's initially selected variant, actual price/availability, and corresponding markup where present. It rejects substituting a cheaper sibling's price while preserving supported single-page variant URLs and the distinction between consistency and exposure.
- Section 10 carries short processing and variant checks inside the diagnosis excerpt, with precise routes to the fuller explanation. A diagnosis-only read retains the essential conditions.

In [the Google evidence ledger](../../skills/marketing-practitioner/references/commerce/google-shopping-evidence.md), G01, G02, and G05 now include the recovered official locators, selected passages inspected, verification date, and limits described in report 38. Existing source IDs are retained. Historical review dates were not advanced to imply a complete new platform audit.

The controller, index, retrieval code, shared handbook, and narrow writing fast path are unchanged. Report 38 was already untracked when this correction began and was preserved.

## Retrieval and static review

Re-read actual loader output for `google-commerce.processing`, `google-commerce.identity`, and `google-commerce.diagnosis` with the governing SKILL.md context. The inserted conditions remain inside the intended sections; diagnosis references resolve to existing routes.

The review's constructed delayed-update / cross-country approval case now has explicit instructions to inspect the relevant processed state and scoped status. The automation shortcut encounters an explicit regular-submission requirement. The premium/basic variant case now requires matching the selected variant instead of changing its price to a sibling's value. These are content sufficiency checks, not observed agent behavior or evidence of commercial effectiveness. A broader representative operational-chain review remains a separate next step.

## Verification performed

- `scripts/verify.ps1 -PackageOnly`: repository package validator and current Codex validator passed.
- `get-knowledge.py --validate`: passed, 264 routes / 240 evidence sources.
- `test-knowledge-routing.py`: passed, 68 routing-mechanics smoke checks.
- The three affected logical sections were successfully retrieved and inspected.
- Final runtime diff inspected: additions only in the two intended files. Every original line, including Unicode content, remains intact and in order against a pre-edit byte backup. Both files retain UTF-8 without BOM, CRLF, and terminal newline.
- Closure-report local links and text conventions checked; `git diff --check` passed.

Backup: `C:\Users\Admin\AppData\Local\Temp\marketing-google-fix-7lqh93ya`. No commit, push, full verification suite, or legacy pilot cleanup was performed. The pre-existing untracked report 38, two modified runtime files, and this new closure report constitute the final worktree changes.

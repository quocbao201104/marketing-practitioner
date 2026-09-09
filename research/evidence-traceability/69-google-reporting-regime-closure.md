# Google Commerce Reporting-Regime Closure

Date: 2026-09-09. Follows [review 68](68-google-reporting-regime-review.md).

## Result

The bounded Google reporting-regime defect is closed in:

- `skills/marketing-practitioner/platforms/commerce/google-shopping.md`
- `skills/marketing-practitioner/references/commerce/google-reporting-evidence.md`

`GR01` records the 2026-08-24 Merchant Center reporting-definition changes and the late-June Popular products coverage change with explicit non-causal boundaries.

## Corrections

- Google performance diagnosis now treats metric definition and data vintage as part of the observation, not just the metric label.
- Comparisons crossing 2026-08-24 are instructed to check the YouTube affiliate/Organic separation and updated YouTube organic definitions before inferring a visibility or creative change.
- Historical restatement from 2026-07-01 is preserved, so an older export and a newly loaded historical report are not assumed definition-identical.
- Expanded Ads product-level reporting is treated as a possible coverage-driven metric increase, not proof of performance improvement.
- Announced future reporting dimensions are not treated as current account capability until verified.
- Merchant-declared `popularity_rank`, Google Popular products report rank, and organic Search/Shopping rank are now explicitly separate provenance classes.

## Static case assessment

| Case | Assessment |
| --- | --- |
| G-RC01 | A sharp Organic decline around 2026-08-24 now triggers a reporting-regime check before title/ranking diagnosis. |
| G-RC02 | Old exports and newly restated historical views retain definition/data-vintage differences. |
| G-RC03 | Ads product-metric increases after coverage expansion are not automatically interpreted as effectiveness gains. |
| G-RC04 | Future `Network` segmentation remains unobserved capability until account availability is verified. |
| G-RC05 | Merchant `popularity_rank`, Popular products analytics rank, and organic rank are kept distinct. |
| G-RC06 | The narrow product-title fast path remains intact and does not require a reporting audit when performance interpretation is not part of the task. |

These are static source-to-guidance assessments, not live Merchant Center tests, account observations, or agent behavioral results.

## Scope integrity

No Google route, commerce handbook rule, ranking model, controller instruction, or benchmark was added. The correction remains inside Google-specific observation/diagnosis semantics.

## Verification status

- Source ID `GR01` was checked against the pre-change default branch and did not previously exist.
- Existing `google-commerce.*` route headings remain unchanged.
- Full repository/package/harness execution was not performed in this closure; CI may be evaluated separately after the branch is proposed for merge.

No broader Google Shopping re-research is justified by this bounded reporting change alone.
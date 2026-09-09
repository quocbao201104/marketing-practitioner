# LinkedIn Follow-Recommendation Freshness Closure

Date: 2026-09-09. Follows [review 66](66-linkedin-follow-recommendation-review.md).

## Result

The bounded LinkedIn freshness gap is closed in:

- `skills/marketing-practitioner/platforms/linkedin.md`
- `skills/marketing-practitioner/references/linkedin-evidence.md`

`LI01` records the 2026-08-24 LinkedIn Engineering source with implementation and experiment boundaries. The existing LinkedIn module now distinguishes creator/account recommendation from post recommendation without changing the shared content grammar or adding a route.

## Corrections

- Creator recommendation is represented as a platform-mediated creator/account exposure opportunity whose possible outcome is a typed Follow edge.
- A Follow edge remains distinct from realized delivery/exposure to a later post.
- Follower-growth diagnosis now preserves relationship-acquisition provenance when material instead of assigning new follows to the most visible recent post.
- Semantic member/creator representations remain implementation evidence, not a creator-facing keyword/headline/profile SEO formula.
- `linkedin.delivery-state` remains responsible for delivery realization; `linkedin.relationship-edges` remains responsible for typed relationship state.

## Static case assessment

| Case | Assessment |
| --- | --- |
| LI-C01 | A follower increase near a high-performing post now retains creator recommendation and other acquisition paths as competing explanations before attribution. |
| LI-C02 | Semantic profile matching is explicitly blocked from becoming a keyword-density/headline-weight optimization formula. |
| LI-C03 | Creator recommendation → Follow → future delivery opportunity is separated from guaranteed future post exposure. |
| LI-C04 | The simple-post path remains direct; creator-recommendation reasoning is loaded only when relationship acquisition or distribution state is material. |

These are static assessments of the written guidance, not agent runs or a measured behavioral pass rate.

## Scope integrity

No `SKILL.md`, shared handbook, routing-index, controller, platform taxonomy, or evaluation harness was changed. `LI01` is a single new evidence record scanned by the existing reference-source mechanism.

## Verification status

- Source ID `LI01` was checked against the pre-change default branch and did not previously exist.
- Existing LinkedIn route headings remain unchanged.
- Full repository/package/harness execution was not performed in this closure; CI may be evaluated separately after the branch is proposed for merge.

No additional LinkedIn platform research is justified by this bounded finding alone.
# LinkedIn Follow-Recommendation Freshness Review

Date: 2026-09-09. Baseline: `8a93689908badb7d3f4579fec5a81db185372e87`.

## Scope

This is a bounded source-to-guidance review of the existing LinkedIn platform module after a first-party engineering publication appeared one day after its 2026-08-23 baseline review. It does not reopen LinkedIn platform theory, add a new route, or redesign the shared content-environment grammar.

Current owner remains:

- `skills/marketing-practitioner/platforms/linkedin.md`
- existing route family `linkedin.*`
- existing evidence record `R28` for the broader LinkedIn environment

## New first-party evidence

LinkedIn Engineering, **Rebuilding LinkedIn’s Follows Recommendations with LLM-Based Semantic Retrieval and Ranking**, published 2026-08-24:

`https://www.linkedin.com/blog/engineering/ai/rebuilding-linkedins-follows-recommendations-with-llm-based-semantic-retrieval-and-ranking`

Inspected claims:

- the Follows Recommendation system recommends creators in My Network and Home Feed;
- the system matches a member with creators whose expertise, perspective, and content may be useful to that member;
- member and creator profiles are represented semantically with LLM-derived embeddings;
- the redesign uses multi-stage retrieval and ranking rather than one popularity heuristic;
- candidate generation still includes multiple sources rather than one semantic source;
- production A/B tests reported statistically significant follow-rate lifts, with the strongest gains for new members.

Evidence boundary:

- this is implementation-backed first-party evidence for a creator/account recommendation system;
- it is not a complete disclosure of all LinkedIn relationship or Feed systems;
- profile semantics used by the recommender do not establish a seller/creator-facing optimization formula;
- the reported A/B test supports the tested pipeline change, not a guaranteed result for an individual profile edit or post.

## Concrete decision-relevant gap

The current module correctly distinguishes Follow, Connection, Newsletter subscription, delivery opportunity, and Feed recommendation. It does not yet distinguish **content recommendation** from **creator recommendation that can create a future Follow edge**.

A practitioner can therefore over-attribute a relationship-state change to a content object.

Constructed case:

```text
A creator gains 400 followers during a period in which
one post also performs well.

Current weak inference:
post performed well
→ post caused the follower increase
→ repeat the post format
```

The new evidence establishes a competing platform mechanism:

```text
CREATOR RECOMMENDATION
→ creator/account exposure
→ possible FOLLOW action
→ future delivery opportunities
```

which is distinct from:

```text
POST RECOMMENDATION
→ post exposure
→ post-level response opportunity
```

The follower increase therefore cannot be assigned to one post without evidence connecting the observed follows to that content path.

## Smallest correction

Keep the existing `linkedin.relationship-edges`, `linkedin.delivery-state`, `linkedin.measurement`, and decision-path owners.

Add only:

1. creator recommendation as a scoped relationship-formation mechanism;
2. the distinction `CREATOR RECOMMENDATION ≠ POST RECOMMENDATION`;
3. follow acquisition provenance in performance diagnosis when follower growth is material;
4. an anti-folklore boundary that semantic profile matching does not expose a profile-keyword or headline-ranking formula.

No new primitive, route, platform module, shared handbook rule, or mandatory optimization workflow is justified.

## Pre-correction cases

| Case | Required outcome |
| --- | --- |
| LI-C01 | Followers rise while one post performs well. | Preserve creator-recommendation and other relationship-formation mechanisms before attributing follows to the post. |
| LI-C02 | User asks to keyword-stuff a headline because the system uses profile embeddings. | Reject the unsupported optimization formula; preserve truthful professional identity and relevance. |
| LI-C03 | Creator recommendation produces a follow, but the next post is not seen. | Keep relationship formation distinct from realized delivery/exposure. |
| LI-C04 | User only wants a supplied LinkedIn post rewritten. | Keep the direct content path; do not force creator-recommendation analysis. |

## Disposition

A bounded knowledge update is justified. The existing architecture is sufficient.
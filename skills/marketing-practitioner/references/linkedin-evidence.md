# LinkedIn Platform Evidence

Current product behavior is time-sensitive. This ledger supplements the broader LinkedIn environment record `R28` in `bibliography.md` when a newer platform-specific source materially changes a LinkedIn decision.

## [LI01] LinkedIn Engineering — Follows Recommendation system

LinkedIn Engineering. **Rebuilding LinkedIn’s Follows Recommendations with LLM-Based Semantic Retrieval and Ranking.** Published 2026-08-24.

Direct source:

`https://www.linkedin.com/blog/engineering/ai/rebuilding-linkedins-follows-recommendations-with-llm-based-semantic-retrieval-and-ranking`

Use: first-party implementation evidence that LinkedIn operates a creator/account recommendation system in My Network and Home Feed whose output candidates are creators rather than posts. The disclosed redesign represents member and creator profiles semantically, uses multi-stage candidate retrieval and ranking, and reported statistically significant follow-rate lifts in production A/B tests, strongest for new members.

Boundary:

- creator/account recommendation is not the same system or object class as Feed post recommendation;
- a recommended creator followed by a member can create a new typed Follow relationship and future delivery opportunities, but does not guarantee exposure to any particular future post;
- profile embeddings and semantic matching do not disclose a creator-facing keyword, headline, or profile-field weighting formula;
- the production experiment supports the tested recommender redesign, not a guaranteed effect from editing an individual profile or publishing a particular post;
- the article does not disclose every LinkedIn relationship, Feed, Search, notification, or creator-discovery system.

```text
CREATOR RECOMMENDATION
≠ POST RECOMMENDATION

CREATOR EXPOSURE
→ POSSIBLE FOLLOW EDGE
→ FUTURE DELIVERY OPPORTUNITY
≠ GUARANTEED FUTURE POST EXPOSURE

SEMANTIC PROFILE MATCHING
≠ DISCLOSED PROFILE SEO FORMULA
```
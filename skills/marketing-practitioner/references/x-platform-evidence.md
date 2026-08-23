# X Platform Evidence Ledger

This supplementary ledger defines the source identifiers used by `../platforms/x.md`. It is separated from the selected bibliography because one source is a versioned implementation repository rather than scientific literature or ordinary product documentation.

Current implementation and product claims are time-sensitive. Re-check them when a consequential decision depends on current X behavior.

## [R50] X / xAI — Open-source For You recommendation implementation

X / xAI. **X For You Feed Algorithm.** Public repository: `xai-org/x-algorithm`, Apache-2.0. Reviewed 2026-08-23 at commit `28e414f535e4b5a50ca12ee87674e7649e50c7ad`, committed 2026-08-21.

Use: current implementation evidence for the For You request path, in-network and out-of-network candidate sources, viewer/candidate hydration, pre-scoring filters, Phoenix multi-action prediction, weighted ranking, author/network adjustments, VM reranking, post-selection visibility filtering, feed blending, side effects, current configuration-default mirrors, visibility-label systems, and the Under the Hood transparency tooling.

Important boundaries:

- the repository is specifically strong evidence for the disclosed **For You** implementation, not every X surface;
- public parameter defaults are time-sensitive and may vary under experiments/configuration;
- the repository states that notable experiments are intended to be reflected but does not claim every production assignment is public;
- some anti-gaming / safety material is intentionally withheld, including examples such as Grox prompts and some Botmaker rules;
- exposed weights multiply predicted probabilities or predicted continuous values, not raw engagement counts;
- implementation structure does not by itself establish causal business effects of a writing tactic.

Therefore:

```text
PUBLIC SOURCE CODE
≠ COMPLETE PRODUCTION OBSERVABILITY
```

and:

```text
CURRENT IMPLEMENTATION PARAMETER
≠ UNIVERSAL CONTENT RULE
```

## [R51] X Help — recommendation surfaces, timelines, conversations, and Communities

X. **Recommender Systems; For You Home Timeline Recommendations; Our Approach to Recommendations; About your For you timeline; About replies and mentions / types of posts; Communities help and administration documentation; Lists and related timeline controls.** X Help Center / transparency documentation. Reviewed 2026-08-23.

Use: current product-level evidence that X contains multiple recommendation and participation environments; For You mixes network and recommended content; Following is a distinct followed-account timeline; conversations/replies have relationship and relevance context; Communities are locally governed participation environments; and users can shape delivery/recommendation state through follows, Topics, Likes, reposts, replies, blocks, mutes, Not Interested, Lists, and related controls.

Important boundaries:

- product help does not disclose every internal ranking detail;
- a For You implementation fact does not automatically transfer to Search, Explore, Notifications, Communities, Following, Spaces, Trends, or account recommendations;
- product capability or stated signal use does not establish a fixed ranking weight or causal writing tactic.

## Evidence-use rule

When source-code and product-help evidence overlap, preserve the narrower scope:

```text
implementation path / code revision
→ strongest for what that code actually implements

product documentation
→ strongest for current user-visible capability / stated behavior

local account evidence
→ strongest for the specific account only when the regime is comparable
```

Do not use the existence of open-source code to claim complete observability, universality, or timelessness.
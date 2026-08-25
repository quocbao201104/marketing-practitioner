# Search & Discovery Evidence Ledger

This ledger supports the bounded Search & Discovery specialist layer. It is not a universal ranking-factor catalog. Current provider rules, crawler behavior, eligibility requirements, markup behavior, and telemetry definitions remain time-sensitive authoritative inputs and should be refreshed when they can change a consequential decision.

Evidence review date: **2026-08-25**

---

## [SD01] Google Search Central — How Google Search works

**Source:** Google Search Central, official documentation  
**URL:** https://developers.google.com/search/docs/fundamentals/how-search-works

**Supports**
- discovery/crawling, indexing, and serving are distinguishable processes;
- satisfying technical requirements does not guarantee crawl, indexing, or serving;
- Search systems can use context such as location, language, and device when serving results.

**Does not support**
- a deterministic `published → indexed → ranked` guarantee;
- one universal ranking algorithm or ranking tactic.

---

## [SD02] Google Search Central — AI features and AI optimization guidance

**Source:** Google Search Central, official documentation  
**URLs:**
- https://developers.google.com/search/docs/appearance/ai-features
- https://developers.google.com/search/docs/fundamentals/ai-optimization-guide

**Supports**
- AI Overviews / AI Mode build on Google Search systems;
- query fan-out can generate related retrieval queries beyond the literal user query;
- ordinary Search fundamentals remain relevant to AI features;
- special AI-only schema/text-file tactics are not established universal requirements;
- eligibility does not imply guaranteed appearance.

**Does not support**
- treating the literal user query as the complete retrieval formulation;
- a separate universal GEO/AEO/LLMO ontology;
- deterministic instructions for obtaining an AI citation.

---

## [SD03] Google Search Central — Google Discover

**Source:** Google Search Central, official documentation  
**URL:** https://developers.google.com/search/docs/appearance/google-discover

**Supports**
- discovery can occur without an explicit current query;
- content eligibility does not guarantee appearance in Discover;
- older content can resurface when it remains useful/relevant to current interests;
- Discover traffic can change because interests or system behavior changed, not only because content quality changed.

**Does not support**
- `query = discovery`;
- `old = stale`;
- `Discover traffic decline = content quality decline`.

---

## [SD04] Google Search Central — Canonicalization

**Source:** Google Search Central, official documentation  
**URL:** https://developers.google.com/search/docs/crawling-indexing/canonicalization

**Supports**
- Google can cluster duplicate/near-duplicate URLs and choose a representative canonical;
- publisher canonical declarations are signals/preferences, not absolute commands;
- Google can choose a different canonical from the publisher preference;
- a contextually better duplicate may sometimes be shown.

**Does not support**
- `URL = universal information-object identity`;
- `publisher-preferred canonical = system-selected canonical`.

---

## [SD05] Google Search Console — Performance metric semantics

**Source:** Google Search Console Help, official documentation  
**URL:** https://support.google.com/webmasters/answer/7042828

**Supports**
- impression, click, and position definitions depend on Search result/surface behavior;
- position can be container-relative rather than an independent object rank;
- AI Overview links can inherit the position of the containing overview;
- external website clicks are not the same as all possible in-surface interactions.

**Does not support**
- `impression = verified attention`;
- `position = universal independent rank`;
- direct metric comparability across surfaces without checking definitions.

---

## [SD06] Google Trends — Data interpretation

**Source:** Google Trends Help, official documentation  
**URL:** https://support.google.com/trends/answer/4365533

**Supports**
- Trends data is sampled and normalized rather than an absolute count of people or customers;
- interest values are scaled relative to geography/time context;
- low-volume terms can be thresholded/represented as zero;
- search interest is not a scientific poll or direct measure of topic popularity/market size;
- internal AI retrieval activity is not equivalent to observed public search-interest data.

**Does not support**
- `Trends 100 = absolute search volume`;
- `search interest = customer count`;
- `search interest = purchase intent or market demand`.

---

## [SD07] OpenAI — Publishers and developers FAQ / search crawler controls

**Source:** OpenAI Help Center, official documentation  
**URL:** https://help.openai.com/en/articles/12627856-publishers-and-developers-faq

**Supports**
- OAI-SearchBot controls search-oriented crawling separately from GPTBot training controls;
- search visibility and training permission are distinct purposes;
- a URL/title can in some cases remain known/surfaced through third-party search or other discovery paths even when direct OAI-SearchBot crawling is blocked.

**Does not support**
- one global crawler-access boolean;
- `public = accessible to every discovery system for every purpose`;
- `blocked direct crawler = system cannot know the URL at all`.

---

## [SD08] Perplexity — Crawler documentation

**Source:** Perplexity documentation, official  
**URL:** https://docs.perplexity.ai/docs/resources/perplexity-crawlers

**Supports**
- `PerplexityBot` and `Perplexity-User` have different roles;
- indexing/search crawling and user-triggered fetching can have different access semantics.

**Does not support**
- a global `discoverable` state independent of system/purpose;
- treating indexing permission and user-triggered fetch behavior as the same relation.

---

## [SD09] Bing — Evolving role of the index: from ranking pages to supporting answers

**Source:** Microsoft Bing Search Blog, official engineering/product explanation, May 2026  
**URL:** https://blogs.bing.com/search/May-2026/Evolving-role-of-the-index-From-ranking-pages-to-supporting-answers

**Supports**
- classic search and grounding can share retrieval infrastructure while optimizing different responsibilities;
- traditional search primarily surfaces candidate documents for human evaluation;
- grounding selects information that can support system-generated answers;
- provenance, freshness, contradiction, coverage, and abstention can matter to grounding;
- document relevance and evidentiary fitness are not interchangeable.

**Does not support**
- one universal grounding implementation across providers;
- a universal grounding score;
- `retrieved = safe to commit into an answer`.

---

## [SD10] Bing Webmaster Tools — AI Performance

**Source:** Microsoft Bing Webmaster Blog, official product documentation, February 2026  
**URL:** https://blogs.bing.com/webmaster/February-2026/Introducing-AI-Performance-in-Bing-Webmaster-Tools-Public-Preview

**Supports**
- AI discovery telemetry can include citations, cited pages, grounding queries, and trends;
- citation counts do not by themselves indicate page rank, authority, placement, or role in an individual answer;
- exposed grounding-query data is telemetry, not a complete transparent view of the internal retrieval system.

**Does not support**
- `citation count = authority`;
- `citation count = answer influence`;
- `observed grounding queries = all retrieval activity`.

---

## [SD11] Belkin, Oddy & Brooks — ASK model

**Source:** information-retrieval research  
**Reference:** Belkin, N. J., Oddy, R. N., & Brooks, H. M. (1982), *ASK for Information Retrieval*.

**Supports**
- an information need need not be perfectly expressible as a query;
- the user's current state of knowledge is relevant to information seeking.

**Does not support**
- a current platform implementation claim;
- a universal psychological model for every discovery episode.

---

## [SD12] Bates — Berrypicking

**Source:** information-seeking research  
**Reference:** Bates, M. J. (1989), *The Design of Browsing and Berrypicking Techniques for the Online Search Interface*.

**Supports**
- search can be iterative;
- encountered information can change the user's subsequent information need and query.

**Does not support**
- a mandatory sequence for every search session;
- a platform-specific ranking mechanism.

---

## [SD13] Joachims et al. — Click bias / trust bias

**Source:** information-retrieval / user-behavior research  
**Reference:** Joachims, T. et al., eye-tracking and click-behavior work on interpreting search clicks.

**Supports**
- clicks can contain useful preference information while remaining position/trust biased;
- observed click behavior is not an unbiased absolute relevance judgment.

**Does not support**
- `click = relevance`;
- using CTR as a direct content-quality score.

---

## [SD14] Microsoft Research — Good abandonment

**Source:** search user-behavior research  
**Reference:** Microsoft Research work on detecting good abandonment in mobile search.

**Supports**
- a session without an external click can still satisfy an information need;
- `no click` is ambiguous and can represent success or failure depending on context.

**Does not support**
- `zero click = zero value`;
- a universal satisfaction inference from non-click behavior.

---

## Evidence-use rules

1. **Current provider facts outrank timeless practitioner folklore** for current crawler, eligibility, telemetry, or platform behavior.
2. **Research findings keep their study scope.** Do not silently convert one experiment or IR model into a universal platform law.
3. **Provider telemetry definitions are observations, not causal estimands.** Use Chapter 05 for causal claims.
4. **Do not infer hidden ranking weights.** Official statements about eligibility, signals, ranking systems, or query fan-out do not reveal a complete production model.
5. **Do not promise citations/rankings.** Preserve `eligible`, `may`, `signal`, `can`, and `not guaranteed` language when that is what the source establishes.

# Paid Media Evidence Ledger

This ledger supports the bounded Paid Media specialist layer. It is not a universal ad-platform playbook, auction-factor catalog, media-planning formula, or attribution model. Current provider objectives, bidding products, auction mechanics, audience controls, placement behavior, billing rules, attribution defaults, learning-state definitions, policy constraints, and automated-creative capabilities remain time-sensitive authoritative inputs and should be refreshed when they can change a consequential decision.

Evidence review date: **2026-08-25**

---

## [PM01] Google Ads — Primary and secondary conversion actions

**Source:** Google Ads Help, official documentation  
**URL:** https://support.google.com/google-ads/answer/11461796

**Supports**
- conversion actions can have different optimization roles even when both are observable in reporting;
- primary actions are generally used for bidding when the containing goal is used for bidding;
- secondary actions are generally observation-only, with documented exceptions such as custom goals;
- a reported conversion label does not by itself identify the signal being optimized.

**Does not support**
- `reported conversion = optimization signal` in every configuration;
- `platform optimization target = business outcome`;
- a universal conversion-goal setup recommendation.

---

## [PM02] Google Ads — Data exclusions for Smart Bidding

**Source:** Google Ads Help, official documentation  
**URL:** https://support.google.com/google-ads/answer/10370710

**Supports**
- conversion-data issues can affect Smart Bidding;
- data exclusions alter data used by Smart Bidding without removing the affected conversions from ordinary reporting;
- reported/visible data and optimization-eligible data can therefore diverge;
- conversion delay and stabilization can matter to interpretation after an exclusion.

**Does not support**
- `reported = optimization-eligible`;
- `excluded from bidding = deleted from reporting`;
- a guarantee that data exclusions remove all performance volatility.

---

## [PM03] Display & Video 360 — Frequency caps across auction and Programmatic Guaranteed inventory

**Source:** Display & Video 360 Help, official documentation  
**URL:** https://support.google.com/displayvideo/answer/2696786

**Supports**
- the same frequency-cap label can have different execution semantics across inventory/transaction types;
- auction and non-guaranteed inventory can prioritize the cap over delivery volume;
- campaign-level frequency caps on Programmatic Guaranteed inventory can be best-effort when contractual delivery must be fulfilled;
- frequency measurement can depend on device/publisher/exchange identifiers and can use modeling when deterministic identifiers are unavailable.

**Does not support**
- `control type = universal control precedence`;
- `reported frequency = exact exposure history for every human`;
- a universal rule for every provider's guaranteed inventory.

---

## [PM04] Display & Video 360 — Programmatic Guaranteed deals

**Source:** Display & Video 360 Help, official documentation  
**URL:** https://support.google.com/displayvideo/answer/7067656

**Supports**
- paid media can secure fixed-volume/fixed-price inventory in advance;
- automated/programmatic buying is not synonymous with open auction buying;
- inventory, advertiser permission, creative assignment, pricing/cost terms, and delivery commitments can be distinct elements of the paid execution state.

**Does not support**
- `paid media = auction only`;
- one universal guaranteed-buy workflow across publishers/platforms;
- treating a campaign container as the complete decision or allocation unit.

---

## [PM05] TikTok Ads — Smart+ audience controls, suggestions, and custom targeting

**Source:** TikTok For Business Help, official documentation  
**URL:** https://ads.tiktok.com/help/article/about-targeting-for-your-upgraded-smart-experience?lang=en

**Supports**
- audience controls and audience suggestions have different semantics;
- suggestions can guide automatic targeting while audience expansion remains possible;
- custom/manual targeting provides a different level of advertiser control;
- an advertiser-provided audience input does not necessarily define the exact reached population.

**Does not support**
- `target customer = targeting specification = reached audience`;
- `all targeting fields = hard constraints`;
- a universal targeting model across ad platforms.

---

## [PM06] TikTok Ads — View-through attribution as reporting and optimization input

**Source:** TikTok For Business Help, official documentation  
**URL:** https://ads.tiktok.com/help/article/about-view-through-attribution-vta?lang=en

**Supports**
- view-through attribution records conversions after ad views without clicks under an attribution window;
- TikTok states that VTA conversions are among the signals used to optimize campaigns;
- changing attribution/signal availability can alter future optimization behavior;
- measurement configuration can participate in the delivery control loop rather than serving only passive reporting.

**Does not support**
- `view-through attributed conversion = incremental conversion`;
- `attributed = caused`;
- a universal causal interpretation of view-through conversions.

---

## [PM07] TikTok Ads — Learning phase

**Source:** TikTok For Business Help, official documentation  
**URL:** https://ads.tiktok.com/resources/help/article/learning-phase

**Supports**
- learning is a platform delivery state in which performance can fluctuate while the system explores/adapts to campaign settings;
- edits can affect or retrigger learning behavior;
- current performance can require history/state context before intervention.

**Does not support**
- `learning phase = bad campaign`;
- `learning phase = new shared primitive`;
- one stable learning threshold for every provider/product state.

---

## [PM08] LinkedIn Ads — Cost cap bidding strategy

**Source:** LinkedIn Marketing Solutions Help, official documentation  
**URL:** https://www.linkedin.com/help/lms/answer/a706289/cost-cap-bidding-strategy

**Supports**
- a cost cap is an average-result benchmark used while the system sets/adjusts auction bids;
- objective, optimization goal, and charged-by event can differ;
- changes to audience, bidding strategy, or creative can alter/restart learning behavior;
- the configured cost target is not identical to each executed auction bid or actual average result cost.

**Does not support**
- `cost cap = executed bid`;
- `optimization goal = billing event`;
- a universal seven-day learning law across paid systems.

---

## [PM09] LinkedIn Ads — Campaign and ad set bidding strategies

**Source:** LinkedIn Marketing Solutions Help, official documentation  
**URL:** https://www.linkedin.com/help/lms/answer/a421112

**Supports**
- Maximum Delivery, Cost Cap, and Manual Bidding expose different advertiser/platform control semantics;
- optimization goals and bidding strategies help determine the chargeable event;
- automated bidding can adjust bids to pursue the selected optimization goal within budget;
- a campaign/ad-set budget and the platform's executed bids are different things.

**Does not support**
- `budget = bid = spend`;
- `manual bid amount = final cost`;
- one bidding strategy that is universally best.

---

## [PM10] LinkedIn Ads — Advertising auction

**Source:** LinkedIn Marketing Solutions Help, official documentation  
**URL:** https://www.linkedin.com/help/lms/answer/a501530/linkedin-advertising-auction

**Supports**
- bid price and member relevance both participate in LinkedIn's auction selection;
- automated, manual, and cost-cap strategies produce different bid-setting behavior;
- a higher configured bid does not by itself establish final delivery.

**Does not support**
- `highest bid always wins`;
- a universal auction ranking formula outside the documented LinkedIn context;
- `auction = all paid-media allocation`.

---

## [PM11] Meta Engineering — Andromeda ads retrieval and Advantage+ automation

**Source:** Engineering at Meta, official engineering article  
**URL:** https://engineering.fb.com/2024/12/02/production-engineering/meta-andromeda-advantage-automation-next-gen-personalized-ads-retrieval-engine/

**Supports**
- Meta separates ad retrieval from later ranking stages;
- retrieval reduces a very large eligible ad set to a smaller candidate set for downstream ranking;
- Advantage+ automation can affect audience creation, budget allocation, placement, bid adjustment, and creative generation;
- advertiser-provided inputs and platform-executed delivery are not necessarily identical.

**Does not support**
- a universal Meta auction formula;
- a timeless guarantee that every Meta ads product uses the exact described path;
- turning exposed retrieval/ranking details into creative-writing rules.

---

## [PM12] IAB — Creator Economy Definitions and Taxonomy

**Source:** Interactive Advertising Bureau, April 2025  
**URL:** https://www.iab.com/wp-content/uploads/2025/04/IAB_Creator_Economy_Definitions_Taxonomy_April-2025.pdf

**Supports**
- sponsored content and paid amplification are distinct creator-economy activities;
- paying a creator to create/publish sponsored content is not the same operation as investing in paid advertising to amplify that content.

**Does not support**
- `paid relationship = paid-media delivery`;
- a complete creator-contract, disclosure, or legal framework;
- treating all creator compensation as media spend.

---

## [PM13] IAB — Programmatic transaction terminology

**Source:** Interactive Advertising Bureau, programmatic terminology background  
**URL:** https://www.iab.com/news/standardizing-programmatic-terminology-iab/

**Supports**
- programmatic media historically includes open auctions, invitation-only/private auctions, negotiated/fixed-price arrangements, and automated guaranteed transactions;
- auction is one buying mechanism rather than the definition of paid media.

**Does not support**
- current provider-specific transaction semantics without refreshed authoritative documentation;
- one timeless taxonomy for every media market;
- a universal auction or clearing model.

---

## [PM14] IAB — Digital Out-of-Home Measurement Guide

**Source:** Interactive Advertising Bureau, July 2025  
**URL:** https://www.iab.com/wp-content/uploads/2025/07/IAB_DOOH_Measurement_Guide_July_2025.pdf

**Supports**
- DOOH measurement distinguishes rendered/delivery evidence from Opportunity to See (OTS), Likelihood to See (LTS), and more refined audience-impression concepts;
- potential or modeled exposure does not equal verified human attention;
- observation unit, methodology, modeling, and proof-of-performance matter to interpretation.

**Does not support**
- `rendered impression = person saw ad`;
- `OTS/LTS = verified attention`;
- a universal person-level identity model for paid exposure.

---

## Evidence-use rules

Use this ledger to support the durable Paid Media distinctions, not to infer hidden platform mechanics.

For consequential current-provider decisions:

```text
frozen practitioner grammar
+
current authoritative provider evidence
+
actual account / campaign / deal / measurement state
→ bounded decision
```

Do not transfer a rule from one provider, campaign type, buying mechanism, inventory class, market, account state, or date into another merely because the UI nouns look similar.

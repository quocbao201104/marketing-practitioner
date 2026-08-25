# Paid Media Architecture — Adversarial Cases

Status: **CANDIDATE EVALUATION CONTRACT**  
Date: 2026-08-25  
Theory owner: `research/paid-media-architecture/01-theory-freeze.md`

## Purpose

These cases test whether the candidate Paid Media implementation preserves the frozen decision boundaries under realistic pressure.

They do **not** test memorization of provider UI labels. A correct response can use current provider evidence when supplied or legitimately retrieved, but it must preserve the generic decision semantics even when the exact provider mechanism is unknown.

Score each case:

```text
PASS
PARTIAL
FAIL
```

A response fails when it makes a decision-relevant collapse that the frozen architecture was created to prevent.

---

## P01 — Fast-path ad-headline transformation

**Prompt**

> This Google ad headline is already approved: “Debug AI workflows before they fail in production.” Shorten it to 30 characters. Do not change the claim.

**Required behavior**
- perform the bounded copy transformation;
- do not reopen Paid Media, bidding, audience, campaign, or attribution architecture merely because the artifact is an ad;
- preserve the approved claim boundary.

**Fail if**
- the answer performs unnecessary campaign strategy;
- it invents performance claims or targeting advice.

---

## P02 — Paid creator sponsorship is not automatically paid-media delivery

**Prompt**

> We will pay a creator a flat fee to publish one product tutorial on their own TikTok account. We are not boosting it or buying additional distribution. Which architecture should own the distribution decision?

**Required behavior**
- preserve `PAID RELATIONSHIP ≠ PAID MEDIA DELIVERY`;
- do not activate Paid Media solely because the creator is paid;
- route creator/content/source/authority/disclosure concerns to the appropriate content/message/current-regulation owners.

**Fail if**
- every compensated creator post is classified as paid-media allocation.

---

## P03 — Creator content plus paid amplification

**Prompt**

> The creator post already exists and its message is approved. We now want to spend media budget to amplify that exact post through the platform. What new decision layer opens?

**Required behavior**
- preserve `SPONSORED CONTENT ≠ PAID AMPLIFICATION`;
- activate Paid Media for the amplification control/allocation/delivery decision;
- do not reopen the creator's approved message unless allocation requires a materially different representation.

**Fail if**
- it treats amplification as merely more organic creator distribution;
- it redefines the creator relationship as the paid-delivery model.

---

## P04 — Business value vs optimization event

**Facts**
- business goal: profitable first-time purchasers;
- current platform optimization event: Add to Cart;
- Add-to-Cart volume rose;
- purchase rate after Add to Cart fell;
- no incrementality study was run.

**Task**

> Should we declare the paid campaign improved?

**Required behavior**
- distinguish business outcome, media job, platform objective, and optimization signal;
- do not equate improved local optimization with improved business value;
- use Chapter 05 if causal/incremental impact becomes the decision.

**Fail if**
- `optimization metric up → campaign/business improved`.

---

## P05 — Reported conversion vs optimization-eligible signal

**Facts**
- two conversion actions appear in reporting;
- one is used for bidding under the current goal configuration;
- the other is observation-only.

**Task**

> Can we combine both counts and describe them as the events the bidding system is optimizing?

**Required behavior**
- answer no unless current configuration evidence establishes both are optimization-eligible;
- preserve `REPORTED ≠ OPTIMIZATION-ELIGIBLE`.

**Fail if**
- every reported conversion is treated as a bidding signal.

---

## P06 — Audience suggestion vs enforced control

**Facts**
- a platform has a baseline audience control and a separate audience suggestion;
- the suggestion allows expansion;
- delivery reaches people outside the suggested demographic.

**Task**

> Did the platform violate our targeting?

**Required behavior**
- distinguish hard control from soft suggestion;
- distinguish target customer, targeting specification, eligible population, and actual reached audience;
- decide only after identifying the current control semantics.

**Fail if**
- all audience inputs are treated as hard targeting fences.

---

## P07 — Budget vs bid vs spend

**Facts**
- daily budget is unchanged;
- actual spend fell;
- bid strategy is automated;
- eligible opportunity volume also fell.

**Task**

> Should we increase the campaign's bid because it is underspending?

**Required behavior**
- preserve `BUDGET ≠ ALLOCATION ≠ PACING ≠ BID ≠ SPEND`;
- inspect opportunity/eligibility/allocation state before assigning underspend to bidding;
- avoid inventing a causal explanation.

**Fail if**
- underspend automatically implies bid too low.

---

## P08 — Campaign container vs portfolio/shared allocation boundary

**Facts**
- Campaign A displays a $100/day budget in one view;
- it participates in a shared/portfolio allocation system with other campaigns;
- unused resource can move across members.

**Task**

> Is Campaign A's displayed budget sufficient to infer its independent resource boundary?

**Required behavior**
- answer no;
- preserve `CAMPAIGN ≠ RESOURCE / OPTIMIZATION BOUNDARY`;
- locate the actual shared allocation scope.

**Fail if**
- campaign UI container is assumed to be the optimization/resource unit.

---

## P09 — Guaranteed inventory breaks auction-only reasoning

**Facts**
- advertiser secured fixed-volume inventory at a fixed price before launch;
- creative is assigned later;
- there is no open-auction competition for the reserved volume.

**Task**

> Diagnose delivery using the generic Paid Media model.

**Required behavior**
- represent the buying mechanism as reserved/guaranteed rather than forcing auction reasoning;
- keep inventory obligation, creative authorization, schedule/delivery state, and observations separate.

**Fail if**
- every paid delivery is explained through bid competitiveness.

---

## P10 — Control type vs control precedence

**Facts**
- campaign-level frequency cap exists;
- inventory is guaranteed under a contractual volume/spend commitment;
- provider documentation says campaign cap is best-effort when needed to fulfil the reservation.

**Task**

> If delivery exceeds the apparent campaign cap, is the only plausible explanation that the cap failed technically?

**Required behavior**
- preserve `CONTROL TYPE ≠ CONTROL PRECEDENCE`;
- represent competing obligation/authority and scope;
- avoid universalizing the provider rule beyond its documented transaction type.

**Fail if**
- a field labeled cap is assumed absolute in every context.

---

## P11 — Learning/adaptive state after a material edit

**Facts**
- performance became volatile immediately after a material bid/audience change;
- creative did not change;
- provider documents an adaptive learning/recalibration state after such edits.

**Task**

> Is creative fatigue established?

**Required behavior**
- answer no;
- preserve current mediation state + relevant transition/history;
- treat learning as local platform state, not campaign quality or a new primitive.

**Fail if**
- volatility alone becomes evidence of weak creative.

---

## P12 — Weak delivery without blaming creative

**Facts**
- impressions fell sharply;
- creative and offer did not change;
- audience constraint tightened;
- inventory eligibility also changed;
- no causal test exists.

**Task**

> Write three new ads to fix the performance decline.

**Required behavior**
- do not comply as though creative were established as the bottleneck;
- localize paid opportunity/control/allocation state first;
- route to Chapter 04 only if message/creative becomes implicated.

**Fail if**
- `weak delivery → rewrite ads` by default.

---

## P13 — Advertiser specification vs platform execution

**Facts**
- advertiser supplied a creative pool, audience signal, authorized destination set, and automatic placements;
- the platform selected one creative combination, one placement, one destination, and an executed bid for a specific opportunity.

**Task**

> Can the delivered instance be described as identical to the advertiser specification?

**Required behavior**
- answer no;
- preserve `ADVERTISER SPECIFICATION ≠ PLATFORM-HELD STATE ≠ PLATFORM EXECUTION`;
- distinguish authorization from actual allocation.

**Fail if**
- high-level advertiser settings are treated as the executed instance.

---

## P14 — Rendered does not mean human attention

**Facts**
- a DOOH ad was rendered successfully;
- measurement reports Opportunity to See;
- there is no deterministic observation that every passerby looked at the screen.

**Task**

> Can we report “everyone counted saw the ad”?

**Required behavior**
- reject the claim;
- preserve `DELIVERED/RENDERED ≠ OTS ≠ LIKELY SEEN ≠ VERIFIED ATTENTION`;
- keep observation method/unit/modeling explicit when material.

**Fail if**
- rendered/impression telemetry becomes verified human attention.

---

## P15 — Reach/frequency with modeled identity

**Facts**
- some deterministic device identifiers are unavailable;
- provider uses modeling/historical data for parts of frequency estimation;
- dashboard reports frequency = 3.1.

**Task**

> Does every individual human have exactly 3.1 exposures?

**Required behavior**
- answer no;
- preserve identity basis, modeling, aggregation, and uncertainty;
- preserve `REPORTED FREQUENCY ≠ EXACT EXPOSURE HISTORY OF EVERY HUMAN`.

**Fail if**
- aggregate/modeled frequency is treated as deterministic person-level history.

---

## P16 — Billing event vs optimization event

**Facts**
- campaign optimizes for landing-page clicks;
- current bidding/product configuration charges by impressions.

**Task**

> Are the optimization event and billing event the same because both belong to one campaign?

**Required behavior**
- answer no;
- preserve `BILLING EVENT ≠ OPTIMIZATION EVENT`;
- keep spend/cost semantics separate from outcome optimization.

**Fail if**
- one campaign implies one universal event role.

---

## P17 — Attributed conversion vs incremental effect

**Facts**
- platform reports 1,000 attributed purchases;
- no holdout, lift test, randomized experiment, or valid causal design exists.

**Task**

> How many of the 1,000 purchases did advertising cause?

**Required behavior**
- do not invent a causal number;
- preserve `ATTRIBUTED OUTCOME ≠ CAUSAL EFFECT`;
- hand causal estimation to Chapter 05.

**Fail if**
- attributed purchases are reported as incremental purchases.

---

## P18 — Reported conversion excluded from optimization feedback

**Facts**
- conversion tracking incident occurred;
- affected period is excluded from Smart Bidding data;
- the conversions remain visible in reporting.

**Task**

> Did the bidding system learn from every conversion still visible in the report?

**Required behavior**
- answer no unless evidence establishes it;
- distinguish reporting role from optimization-feedback role;
- preserve conversion delay/maturity and exclusion timing where material.

**Fail if**
- visible report data is automatically treated as optimization feedback.

---

## P19 — Retail media must preserve Chapter 09 product identity

**Facts**
- one product variant is ineligible for a sponsored marketplace placement;
- another variant in the same product family remains eligible;
- bid and budget are adequate.

**Task**

> Should Paid Media collapse both variants into one sponsored-product object and diagnose only bidding?

**Required behavior**
- answer no;
- use Chapter 09 for product/variant/listing identity and state;
- compose that identity with Paid Media eligibility/allocation semantics;
- do not invent a `SPONSORED_PRODUCT` primitive.

**Fail if**
- paid status erases commerce identity.

---

## P20 — Generic discovery vs paid economic allocation

**Facts**
- a page appears organically for a query;
- a paid placement for the same query has weak delivery;
- paid budget, bid strategy, and audience/control state are material.

**Task**

> Is Chapter 13 Search & Discovery sufficient to diagnose the paid placement because both involve ranking/surfacing?

**Required behavior**
- answer no when paid economic allocation semantics can change the decision;
- keep Chapter 13 as generic discovery owner;
- use Paid Media for resource/control/buying/allocation/delivery semantics;
- compose rather than flatten the two systems.

**Fail if**
- organic discovery relevance and paid economic allocation are treated as the same owner.

---

## Adjudication requirements

A candidate should not proceed to independent review unless all cases are explicitly walked through and any `PARTIAL`/`FAIL` is resolved or retained as a documented blocker.

The evaluation must also check negative-space behavior:

```text
no new shared primitive
no new controller job
no campaign ontology
no auction ontology
no targeting ontology
no universal attribution model
no provider-specific guarantee
```

The implementation is successful only if it improves paid-media decisions **without making every ad-related prompt more complex**.

# Google Commerce Reporting Evidence

Time-sensitive reporting sources that affect interpretation of Google commerce observations without redefining product identity, retrieval, ranking, or field semantics.

## [GR01] Google Merchant Center — 2026 performance reporting definition changes

Google Merchant Center Help. **Merchant Center performance reporting updates.** Published 2026-08-11; changes effective 2026-08-24.

Direct source:

`https://support.google.com/merchants/answer/17103877`

Use:

- commission-eligible YouTube affiliate traffic is separated from Merchant Center `Organic` into a distinct `YouTube affiliate` traffic value;
- Google states that this can cause a one-time significant decrease in reported Organic traffic;
- the YouTube affiliate separation and updated YouTube organic click/impression definitions are retroactively applied to historical data starting 2026-07-01;
- expanded Ads product-level reporting across additional channels/formats can cause a one-time increase in reported impressions, clicks, and related metrics;
- a Merchant Center `Network` dimension is announced for future launch and must not be treated as present account capability before it is actually available.

Supplementary Google Merchant Center announcement log:

`https://support.google.com/merchants/announcements/6192467`

Use: late-June 2026 Popular products reporting changes increased coverage and may change reported coverage, rankings, and performance across regions. A change in that report can therefore reflect a reporting-system change rather than a change in product demand.

Boundary:

- a reporting-definition break does not establish any organic visibility, ranking, creative, or demand change;
- restated historical data can differ from an older export even when the underlying shopper events did not change;
- expanded Ads coverage does not establish causal advertising improvement;
- an announced future dimension is not evidence of account-level availability;
- Google-generated Popular products report rankings are distinct from merchant-declared `popularity_rank` and from organic Search/Shopping rank position.

```text
METRIC LABEL
+ REPORT DEFINITION / VERSION
+ DATA VINTAGE
+ SURFACE / TRAFFIC PROVENANCE
→ INTERPRETABLE OBSERVATION

MERCHANT-DECLARED popularity_rank
≠ GOOGLE POPULAR PRODUCTS REPORT RANK
≠ ORGANIC SEARCH / SHOPPING RANK POSITION

REPORTING COVERAGE CHANGE
≠ PERFORMANCE CHANGE
```
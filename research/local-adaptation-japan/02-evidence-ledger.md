# Japan Local Adaptation — Evidence Ledger

Status: **FROZEN RESEARCH EVIDENCE FOR DESIGN REVIEW**  
Companion target: `01-design-freeze.md`

This ledger supports the Japan local-adaptation design freeze. It is research evidence, not installed runtime knowledge. Future implementation may derive a narrower runtime evidence file from this ledger after independent review.

Evidence discipline:

```text
SOURCE SUPPORTS X
!= SOURCE SUPPORTS EVERY CLAIM NEAR X

LINGUISTIC FUNCTION
!= POPULATION ACCEPTABILITY

POPULATION ACCEPTABILITY
!= MARKETING EFFECT

OFFICIAL GUIDANCE
!= UNIVERSAL RULE ACROSS EVERY JAPANESE VARIETY / COMMUNITY

LLM ERROR RATE
!= PROOF OF THE LINGUISTIC MECHANISM
```

## [JPLA01] Agency for Cultural Affairs — Keigo basics; Kenjōgo I vs Kenjōgo II

**Source**  
文化庁 — 第二話「敬語の基本」理解度チェックの解答  
https://www.bunka.go.jp/seisaku/kokugo_nihongo/kokugo_shisaku/keigo/chapter2/detail.html

**Evidence type**  
Japanese government language guidance based on the `敬語の指針` framework.

**Supports**

- `謙譲語Ⅰ` can honor the person who is the `向かう先` of an action.
- `謙譲語Ⅱ` can function as deferential expression toward the current addressee.
- When action target and addressee differ, the two forms can have materially different honorific orientation.
- `伺う` and `参る` are therefore not interchangeable merely because both may be described broadly as humble/deferential forms.

**Does not support**

- a deterministic rule for which person always deserves honorification;
- a global formal/casual score;
- a marketing-effect claim;
- universal applicability to every regional Japanese honorific system.

## [JPLA02] Agency for Cultural Affairs — `伺います` vs `参ります` with a third-party teacher

**Source**  
文化庁 — 第六話「間違いやすい敬語（3）～謙譲語I VS 謙譲語II」理解度チェックの解答  
https://www.bunka.go.jp/seisaku/kokugo_nihongo/kokugo_shisaku/keigo/chapter6/detail.html

**Evidence type**  
Official applied honorific guidance.

**Supports**

- concrete case where the speaker addresses teacher A but talks about visiting teacher B;
- `参る` is deferential toward the addressee but does not honor the third-party visit target;
- `伺う` can honor the visit target.

**Does not support**

- `伺う` should always replace `参る`;
- third-party people should always be honorified;
- one fixed hierarchy based on profession/age.

## [JPLA03] Agency for Cultural Affairs — customer action and wrong honorific target

**Source**  
文化庁 — 第四話「間違いやすい敬語（1）～尊敬語 VS 謙譲語I」理解度チェックの解答  
https://www.bunka.go.jp/seisaku/kokugo_nihongo/kokugo_shisaku/keigo/chapter4/detail.html

**Evidence type**  
Official applied honorific guidance.

**Supports**

- `担当者に伺ってください` is inappropriate when a receptionist tells a customer to ask the staff member;
- using `伺う` there honors the action target (staff) rather than providing respectful realization of the customer's action;
- honorific morphology can therefore orient toward the wrong semantic participant even when the global intent is "be respectful to the customer".

**Does not support**

- all uses of `伺う + ください` are categorically impossible in every context;
- a customer-role lookup table;
- population dislike/preference claims.

## [JPLA04] Agency for Cultural Affairs — uchi/soto and organizational-context exceptions

**Source**  
文化庁 — 第七話「場面で異なる敬語～ウチとソト～」理解度チェックの解答  
https://www.bunka.go.jp/seisaku/kokugo_nihongo/kokugo_shisaku/keigo/chapter7/detail.html

**Evidence type**  
Official applied sociolinguistic / honorific guidance.

**Supports**

- `uchi / soto` can change how own-side organizational people are referred to when speaking externally;
- organizational side is a real contextual factor in Japanese realization;
- school context provides an explicit counterexample to mechanical application: a colleague teacher may still be referred to as `田中先生` when speaking to a parent because another interactional frame is salient;
- job title can provide a more neutral representation in some cases.

**Does not support**

- `own organization → always de-honorify`;
- `external person → always honorify`;
- a universal precedence rule where role always beats uchi/soto or vice versa;
- a need for an executable organization relationship graph.

## [JPLA05] Agency for Cultural Affairs — `〜させていただく` baseline conditions and contextual acceptability

**Sources**  
文化庁 — 第三話「敬語のTPO～依頼の仕方～」理解度チェックの解答  
https://www.bunka.go.jp/seisaku/kokugo_nihongo/kokugo_shisaku/keigo/chapter3/detail.html

文化庁 — 平成19年度「国語に関する世論調査」の結果について  
https://www.bunka.go.jp/tokei_hakusho_shuppan/tokeichosa/kokugo_yoronchosa/h19/

**Evidence type**  
Official guidance plus Japanese public-language survey interpretation.

**Supports**

- baseline analysis of `〜させていただく` as own-side action with permission from addressee/third party plus benefit to the speaker;
- perceived appropriateness varies with how strongly those conditions are met or can plausibly be construed;
- closure/meeting-ending cases may be better realized with `〜いたします` when permission/benefit framing is not supported;
- genuine permission-request cases fit the baseline mechanism more directly.

**Does not support**

- `no explicit permission → construction always forbidden`;
- `construction present → factual permission definitely existed`;
- current population-wide preference from the 2007-era survey;
- a legal/business authorization inference.

## [JPLA06] National Institute for Japanese Language and Linguistics — historical/corpus change in `させていただく`

**Source**  
国立国語研究所 ことば研究館 — 「確認させていただいてもよろしいですか？」なんて言われると目が点になります  
https://kotoba.ninjal.ac.jp/qa/yokuaru/qa-71/

**Evidence type**  
NINJAL public explanation grounded in corpus research and historical pragmatics.

**Supports**

- historical growth of `サセテイタダク` relative to related benefactive constructions;
- contemporary examples exist where the other party is not materially involved;
- the construction can help avoid explicitly grammaticalizing the other party as subject and can contribute to interpersonal distance/deference;
- contemporary usage cannot be interpreted only through a literal permission transaction.

**Does not support**

- every contemporary use has lost permission/benefit meaning;
- the form is universally preferred or disliked;
- age/region lookup rules.

## [JPLA07] Shiina 2024 — grammaticalization and newer deferential uses of `させていただく`

**Source**  
椎名 美智 — 「シン・させていただく」の誕生秘話 — 文法化と敬意漸減の影響  
待遇コミュニケーション研究 21 (2024), 50–65  
https://www.jstage.jst.go.jp/article/tcg/21/0/21_50/_article/-char/ja

DOI: https://doi.org/10.32252/tcg.21.0_50

**Evidence type**  
Japanese historical-pragmatics / honorific research.

**Supports**

- analysis of pragmatic expansion from benefactive/humble use toward newer deferential (`新・丁重語`) and, in some analyses, beautifying uses;
- original permission/benefit meanings can weaken in some self-contained contemporary examples;
- `させていただく` therefore has medium-volatility pragmatic semantics rather than one timeless binary rule.

**Does not support**

- permission/benefit is absent from all current use;
- all newer uses are acceptable in every context;
- a prescriptive ban or automatic replacement rule.

## [JPLA08] NHK Broadcasting Culture Research Institute — 2023 Japanese language variation survey

**Source**  
塩田 雄大 — とりあえず“そのうち食事でもしましょう“ — 2023年「日本語のゆれに関する調査」から(2)  
放送研究と調査 74(2), 2024, 34–59  
https://www.jstage.jst.go.jp/article/bunken/74/2/74_34/_article/-char/ja

DOI: https://doi.org/10.24634/bunken.74.2_34

**Evidence type**  
NHK language-variation survey report.

**Supports**

- acceptability/preference for `させていただく` expressions varies by respondent attributes/context;
- the report identifies age and regional differences, including higher support patterns in some older groups and Kansai/Kanto differences for surveyed expressions;
- population variation is strong enough to reject a universal "Japanese people prefer/dislike this construction" rule.

**Does not support**

- causal marketing effects;
- a deterministic age/region choice rule;
- every construction/context shares the same distribution.

## [JPLA09] NHK Broadcasting Culture Research Institute — 2025 Japanese language variation survey, published 2026

**Source**  
塩田 雄大 — “一生スマホをいじっている” 20代では7割近くが使う — 2025年「日本語のゆれに関する調査」から（1）  
放送研究と調査 76(1-2), 2026, 30–59  
https://www.jstage.jst.go.jp/article/bunken/76/1-2/76_30/_article/-char/ja/

DOI: https://doi.org/10.24634/bunken.76.1-2_30

**Evidence type**  
Recent NHK language-variation survey report.

**Supports**

- for the surveyed `ネギを入れさせていただいてもよろしいですか` comparison, support for the `させていただく` form increased across the 30s-to-70s age range as age increased;
- current variation does not fit a simple "young speakers invented/prefer the form" story;
- newer evidence should constrain any time-sensitive population-acceptability statement.

**Does not support**

- a general rule that older speakers always prefer `させていただく`;
- construction-level semantics by itself;
- marketing outcome claims.

## [JPLA10] Immigration Services Agency / Agency for Cultural Affairs — Easy Japanese guidance

**Sources**  
出入国在留管理庁 — やさしい日本語ガイドライン / supporting guidance  
https://www.moj.go.jp/isa/support/portal/plainjapanese_guideline.html

Example official material:  
https://www.moj.go.jp/isa/content/930005857.pdf

**Evidence type**  
Japanese government accessibility / communication guidance.

**Supports**

- for Easy Japanese aimed at comprehensibility, avoid `尊敬語 / 謙譲語` in principle while retaining basic polite `丁寧語` / `です・ます` style;
- accessibility can legitimately reduce honorific complexity without implying disrespect;
- `させていただく` can be rewritten to a simpler direct form in this communication regime.

**Does not support**

- Easy Japanese should be used for all foreign residents or all Japanese-language marketing;
- Japanese communication is generally better without honorifics;
- a country-triggered accessibility rule.

## [JPLA11] Agency for Cultural Affairs — regional honorific diversity

**Sources**  
文化庁 — 敬語の指針 / regional honorific diversity material  
https://www.bunka.go.jp/seisaku/bunkashingikai/kokugo/hokoku/pdf/keigo_tosin.pdf

Supporting regional explanation:  
https://www.bunka.go.jp/seisaku/bunkashingikai/kokugo/kokugo/kokugo_33/pdf/siryou_2.pdf

**Evidence type**  
Official Japanese language-policy / honorific guidance.

**Supports**

- Japanese regional varieties contain honorific systems that can differ from common/standard Japanese in form and use;
- Kansai `〜はる` is one official example, including distributions with own-side persons that differ from standard honorific expectations;
- a Japanese-language unit must not claim universal authority over stronger scoped regional/community evidence.

**Does not support**

- infer `〜はる` from Kansai/Osaka geography alone;
- all Kansai varieties use the form identically;
- a regional dialect resolver.

## [JPLA12] Sekizawa & Yanaka 2024 — LLM contextual Japanese honorific evaluation

**Source**  
関澤 瞭・谷中 瞳 — 大規模言語モデルは文脈情報を踏まえて敬語を理解しているか  
自然言語処理 31(3), 2024, 1292–1329  
https://www.jstage.jst.go.jp/article/jnlp/31/3/31_1292/_article/-char/ja

DOI: https://doi.org/10.5715/jnlp.31.1292

**Evidence type**  
Peer-reviewed Japanese NLP evaluation research.

**Supports**

- contextual Japanese honorific use requires both grammatical knowledge and social/contextual information;
- evaluated LLMs including GPT-4 retained room for improvement, especially on more complex syntactic structures in honorific conversion;
- there is a plausible runtime reason not to assume that fluent Japanese generation automatically preserves contextual honorific semantics.

**Does not support**

- any particular JP-LANG-HON-01 linguistic rule by itself;
- a benchmark-grade reliability claim for Marketing Practitioner;
- a claim about current GPT model families not evaluated in the study.

## Evidence-to-claim map

| Candidate claim | Primary support | Boundary / anti-overclaim support |
|---|---|---|
| Addressee honorification and action-target honorification are not the same | JPLA01, JPLA02 | JPLA03 |
| Global "be respectful" is insufficient for some Japanese realization decisions | JPLA02, JPLA03 | JPLA12 |
| Uchi/soto matters but is not a deterministic rule | JPLA04 | JPLA11 |
| Regional/common Japanese honorific systems cannot be collapsed | JPLA11 | JPLA04 |
| `させていただく` baseline involves permission + benefit | JPLA05 | JPLA06, JPLA07 |
| Contemporary `させていただく` cannot be reverse-read as proof of permission | JPLA06, JPLA07 | JPLA08, JPLA09 |
| Population acceptability is variable and time/context sensitive | JPLA08, JPLA09 | JPLA05 |
| Easy Japanese can reduce honorific complexity while preserving polite stance | JPLA10 | JPLA05 |
| LLM fluency does not eliminate contextual honorific risk | JPLA12 | linguistic claims remain grounded in JPLA01–JPLA11 |

## Research exclusions

This ledger intentionally does **not** attempt to establish:

- a Japanese consumer psychology profile;
- Japan-wide marketing preferences;
- a universal Japanese business-email template;
- causal conversion effects of keigo or `させていただく`;
- a complete honorific grammar;
- legal authority / consent state from language form;
- regional-form selection from geography alone;
- a ranking of Japanese speakers by age/status for honorific choice.

The evidence is sufficient only for the bounded realization mechanisms and guardrails frozen in `01-design-freeze.md`.
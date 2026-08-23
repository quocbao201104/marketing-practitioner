<div align="center">

<img src="assets/marketing-practitioner-banner.webp" alt="Marketing Practitioner banner" width="100%">

# Marketing Practitioner

**Research-first marketing decision system for AI agents.**

*Learn the market before writing the copy.*

[![Version: v0.3.0](https://img.shields.io/badge/version-v0.3.0-0a7.svg)](#status)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Language: English](https://img.shields.io/badge/language-English-4c1.svg)](#)
[![Format: Agent Skill](https://img.shields.io/badge/format-Agent%20Skill-6f42c1.svg)](skills/marketing-practitioner/SKILL.md)
[![skills.sh](https://skills.sh/b/quocbao201104/marketing-practitioner-skill)](https://skills.sh/quocbao201104/marketing-practitioner-skill)

</div>

---

Marketing Practitioner gives an AI agent a disciplined way to turn messy market evidence into bounded marketing decisions — across customer research, positioning, messaging, copy, platform content, commerce, product discovery, diagnosis, experimentation, localization, and learning.

It is not a bag of growth hacks or prompt templates. The agent starts from the job you actually need done, keeps supplied facts and uncertainty intact, loads deeper knowledge only when it can change the decision, and produces the minimum useful output for that job.

```text
EVIDENCE
→ UNDERSTANDING
→ DECISION
→ REPRESENTATION / EXECUTION
→ DISTRIBUTION / DISCOVERY
→ OBSERVATION
→ LEARNING
```

## Quick start

Install with the Skills CLI:

```bash
npx skills add quocbao201104/marketing-practitioner-skill
```

Then talk to your agent normally. You do **not** need to know marketing vocabulary such as ICP, JTBD, positioning, attribution, retrieval, or conversion architecture before using the skill.

Start with three things:

1. **What are you trying to do?**
2. **What do you already know or have?**
3. **Where will the decision be used, if that matters?**

Not sure what belongs in the prompt? See the [`Task Specification Guide`](TASK-SPECIFICATION-GUIDE.md). It gives a reusable starter, missing-information policy, and progressively richer examples without requiring a rigid form or prompt-engineering vocabulary.

Start with the smallest task description that communicates the real job, then add only information that can materially change the result.

### Don't want to write the prompt yourself?

Give the agent your rough request, notes, files, and whatever context you already have. Then say:

```text
Read TASK-SPECIFICATION-GUIDE.md.

Use everything I have already provided to compile the smallest sufficient task
specification for the job I am trying to do.

Preserve decisions I have already made.
Do not invent missing facts, goals, audiences, or constraints.
Omit sections that do not materially change the result.

Then execute the task with Marketing Practitioner.

If I explicitly ask for a reusable prompt instead, return the compiled task
specification without executing it.
```

This lets the **agent do the task-specification work**. You provide what you know; the agent turns it into a cleaner working specification before execution. The compiled specification does not need to be shown unless you ask for it.

For example:

```text
I sell this product on Shopee.
Here are the verified product facts and my current listing.

Help me improve the title and product information.
Do not invent benefits or claims. If important information is missing, tell me.
```

Or:

```text
Here are 12 customer reviews and 4 support conversations.
I do not know marketing terminology.

Help me understand why people buy this product, what problems keep repeating,
what we still do not know, and what message is actually supported by the evidence.
```

Or:

```text
TikTok video views stayed high but product-link clicks dropped sharply.
Help me diagnose where the problem might be before changing the creative.
```

The skill decides which deeper marketing knowledge is actually needed instead of forcing every request through the same funnel.

## If you are not a marketer

You can use Marketing Practitioner as a guided reasoning layer rather than a marketing textbook.

### Tell it the job in plain language

You can say things like:

- “I need more people to understand what this product is.”
- “I do not know which customer group to focus on.”
- “These reviews are messy. Tell me what actually repeats.”
- “Sales fell. Help me figure out why before changing anything.”
- “Turn these product facts into one Shopee title.”
- “Adapt this message for Facebook without changing the claim.”
- “I want this product to be easier to resolve in conversational shopping.”
- “We ran this test. What did it actually prove?”

The agent can translate that into the internal marketing decision it needs to solve.

### Give it the strongest material you have

You do not need all of these. More reliable context simply gives the agent more to work with.

| If you have... | It can help with... |
| --- | --- |
| product facts, specs, screenshots | product communication, claims, listings, positioning |
| customer interviews, reviews, support logs | customer understanding, segmentation, message evidence |
| current landing page, email, ad, caption | critique, rewrite, message diagnosis, adaptation |
| competitor pages or alternative workflows | positioning and relevant-alternative analysis |
| platform listing fields or screenshots | platform-specific representation decisions |
| traffic, click, conversion, order, or funnel metrics | diagnosis and experiment planning |
| experiment results | interpretation, causal boundaries, next decision |
| very little information | a bounded answer plus explicit missing information |

A useful instruction when your evidence is incomplete is simply:

```text
Use only what I gave you.
Separate facts from assumptions.
Tell me what is missing instead of making it up.
```

### You can ask for a small output

Deep reasoning does not require a long answer.

```text
Give me one title only.
```

```text
Rewrite this caption in under 80 words. Keep the same claim.
```

```text
Give me the top 3 plausible explanations and the next check for each.
```

The runtime is explicitly designed to stay on a fast path when the upstream decisions are already resolved.

## What it can help with

### Customer and market understanding

- synthesize interviews, reviews, survey responses, support records, and sales notes;
- separate observation from interpretation and hypothesis;
- preserve contradictions, segment differences, unknowns, and evidence scope;
- identify customer language, recurring problems, alternatives, and decision-relevant patterns.

### Segmentation, positioning, and value

- decide which customer/context differences actually change the marketing decision;
- reason about relevant alternatives, including manual work, delay, internal labor, and doing nothing;
- connect a target context to a prioritized value, credible proof, trade-offs, and claim boundaries;
- avoid treating competitor whitespace as automatic customer value.

### Messaging, copy, and critique

- build message hierarchy and proof architecture when needed;
- write landing pages, emails, campaigns, social content, product communication, and short-form copy;
- preserve the supplied voice and facts;
- distinguish internal constraints from information that actually belongs in the message;
- review claims, relevance, clarity, proof, channel fit, CTA coherence, and naturalness.

### Social content and distribution environments

The shared content-environment model supports current modules for:

- Facebook;
- Instagram;
- LinkedIn;
- TikTok;
- X.

The skill does not reduce platform work to “write in the right tone.” It can reason about content objects, representations, audience state, delivery and permission edges, interaction provenance, platform mediation, measurement, and recommendation boundaries when those distinctions matter.

### Commerce and product discovery

The commerce layer covers generic product-discovery reasoning plus current modules for:

- Google Shopping / Google commerce;
- Amazon;
- TikTok Shop;
- Shopee;
- Etsy;
- Lazada.

It can reason about product/listing/catalog identity, variants, structured product information, product cards and PDPs, price/stock/promotion state, retrieval versus ranking, search versus recommendation, conversational product discovery, agent-mediated commerce, checkout authority, and commerce-performance diagnosis.

It deliberately keeps distinctions such as:

```text
PRODUCT / OBJECT ≠ REPRESENTATION ≠ ENCOUNTER SURFACE
RETRIEVAL ≠ RANKING ≠ FILTERING ≠ RECOMMENDATION
PRODUCT FACT ≠ COMMERCIAL STATE ≠ OBSERVED FEEDBACK
SHOPPER INTENT ≠ DELEGATED AUTHORITY ≠ EXECUTED EFFECT
```

These are used to prevent false tactical conclusions, not to make simple listing tasks complicated.

### Diagnosis and experimentation

- define the actual metric and baseline before explaining a change;
- decompose where a performance shift is concentrated;
- retain competing explanations instead of jumping to the easiest story;
- distinguish attribution from incrementality and observation from causality;
- choose discriminating checks and bounded experiments;
- keep “do not change anything yet” as a valid decision when evidence is weak.

### Localization and learning

- separate global product/strategy invariants from dimensions that local evidence can justify changing;
- avoid turning cultural models into stereotypes about individuals;
- record what was believed, tried, observed, supported, weakened, falsified, or left unresolved;
- preserve negative and inconclusive results for future decisions.

## What this repository is not

Marketing Practitioner is not:

- a prompt collection;
- a copy-template pack;
- an SEO checklist;
- a library of platform “algorithm hacks”;
- a universal marketing funnel;
- a guarantee that more engagement means more customer value;
- a claim that public ranking signals reveal a platform's complete production system;
- a substitute for missing product truth or missing evidence.

Its job is to help an agent make better-scoped marketing decisions and communicate them truthfully.

## How the reasoning works

The runtime begins with the **current job**, not the topic name.

```text
USER TASK
   ↓
WHAT JOB IS REQUIRED NOW?
WRITE / DECIDE / DIAGNOSE / RESEARCH / ADAPT / TEST / LEARN
   ↓
WHAT IS ALREADY RESOLVED?
   ↓
WHAT DECISION IS STILL OPEN?
   ↓
WHAT EVIDENCE OR KNOWLEDGE CAN CHANGE IT?
   ↓
LOAD ONLY WHAT IS NEEDED
   ↓
RESOLVE THE DECISION
   ↓
MINIMUM SUFFICIENT OUTPUT
```

This matters because a request mentioning “TikTok,” “Shopee,” “positioning,” or “research” does not automatically justify loading an entire platform theory or reopening upstream strategy.

For example:

```text
"Shorten this supplied Facebook caption"
→ message already resolved
→ fast transformation
→ no need to rebuild positioning
```

while:

```text
"Why did TikTok reach fall?"
→ diagnosis is unresolved
→ platform state / delivery / measurement may matter
→ load only the relevant content + TikTok knowledge
```

## Addressable just-in-time knowledge

Large knowledge files are addressable through a lightweight routing layer.

```text
OPEN DECISION
→ KNOWLEDGE NAMESPACE
→ LOGICAL KNOWLEDGE ID
→ routing-index.json
→ exact Markdown section when supported
```

Examples of logical knowledge addresses include:

```text
commerce.identity
commerce.discovery
commerce.recommendation
commerce.resolvability
commerce.agentic
shopee.conversational-discovery
amazon.shop-direct
tiktok.machine-mediation
x.interaction-provenance
```

The physical file and heading can change without changing the logical meaning of the address.

When helper execution is available, the bundled deterministic loader can retrieve only the requested section:

```bash
python skills/marketing-practitioner/scripts/get-knowledge.py commerce.resolvability
python skills/marketing-practitioner/scripts/get-knowledge.py --list --namespace shopee
```

Evidence records use their own source IDs rather than being duplicated into the semantic routing table:

```bash
python skills/marketing-practitioner/scripts/get-knowledge.py --source R23
python skills/marketing-practitioner/scripts/get-knowledge.py --source A03
```

The helper is an optimization, not a requirement for the skill to function. If a host cannot execute it, the agent can use `routing-index.json` as an address table and read the smallest feasible section. On hosts that only support whole-file reads, the runtime degrades to the smallest target file while preserving dependency-first routing.

## Evidence discipline

The repository uses a conservative standard for claims and learning:

- qualitative recurrence does not establish population prevalence;
- descriptive data do not by themselves establish causality;
- attribution does not equal incrementality;
- multiple derivatives from one source do not become independent evidence;
- platform eligibility does not guarantee exposure;
- observed engagement does not automatically establish organic human preference;
- a ranking signal or exposed implementation parameter is not automatically a writing instruction;
- machine- or platform-inferred product information is not automatically verified product truth;
- uncertainty, contradiction, and inconclusive results are valid states;
- stronger claims require stronger evidence;
- learning remains scoped to the population, market, surface, product state, platform regime, and period that support it;
- persuasive communication must preserve meaningful choice and must not rely on fabricated scarcity, hidden costs, false social proof, or invented personal experience.

## Repository architecture

The installable skill is under [`skills/marketing-practitioner/`](skills/marketing-practitioner/).

```text
.
├── README.md
├── LICENSE
├── CONTRIBUTING.md
├── CHANGELOG.md
├── THIRD_PARTY_NOTICES.md
├── assets/
├── evals/                         # tests and audits OF the skill
│
└── skills/
    └── marketing-practitioner/
        ├── SKILL.md                # runtime controller + invariants
        ├── routing-index.json      # logical knowledge addresses
        ├── scripts/
        │   ├── get-knowledge.py
        │   └── test-knowledge-routing.py
        ├── handbook/
        │   ├── 00-foundations-and-method.md
        │   ├── 01-customer-research-and-evidence.md
        │   ├── 02-segmentation-icp-and-jtbd.md
        │   ├── 03-positioning-and-value.md
        │   ├── 04-messaging-proof-and-copy.md
        │   ├── 05-diagnosis-causality-and-experimentation.md
        │   ├── 06-organizational-learning.md
        │   ├── 07-international-marketing-and-ethics.md
        │   ├── 08-content-environments-and-distribution.md
        │   └── 09-commerce-environments-and-product-discovery.md
        ├── platforms/
        │   ├── facebook.md
        │   ├── instagram.md
        │   ├── linkedin.md
        │   ├── tiktok.md
        │   ├── x.md
        │   └── commerce/
        │       ├── google-shopping.md
        │       ├── amazon.md
        │       ├── tiktok-shop.md
        │       ├── shopee.md
        │       ├── etsy.md
        │       └── lazada.md
        ├── frameworks/
        │   ├── practitioner-cards.md
        │   └── quality-rubrics.md
        └── references/             # bibliography + scoped evidence ledgers
```

### `SKILL.md`

The runtime controller. It defines job-first routing, resolved-state freezing, universal invariants, operating paths, state handoffs, evidence boundaries, fast paths, and final validation.

### `handbook/`

Shared marketing knowledge. Chapters 00–07 cover research, segmentation, positioning, messaging/copy, diagnosis/experimentation, organizational learning, and international/ethical reasoning. Chapter 08 models content environments and distribution. Chapter 09 models commerce environments and product discovery.

### `platforms/`

Current platform-specific knowledge. These modules specialize the shared reasoning model instead of creating independent theories for every platform.

### `routing-index.json` + `scripts/get-knowledge.py`

The address layer for large knowledge surfaces. Logical IDs point to exact semantic sections where supported, allowing just-in-time retrieval without making physical file locations part of the controller interface.

### `references/`

Selected bibliography and scoped evidence ledgers. These support provenance and deeper review when needed, but are not intended to be loaded into every task.

### `evals/`

Audits and smoke tests of the skill itself. They live outside the installable skill so evaluation material is not mistaken for runtime marketing guidance.

## Installation and manual use

For compatible clients:

```bash
npx skills add quocbao201104/marketing-practitioner-skill
```

To inspect or use the repository manually:

```bash
git clone https://github.com/quocbao201104/marketing-practitioner-skill.git
```

The governing skill instructions are:

```text
skills/marketing-practitioner/SKILL.md
```

If your agent supports project/local skills, point it at the installable `skills/marketing-practitioner/` directory. Exact discovery and activation behavior depends on the client.

## A few copy-paste recipes

### Understand customers before writing

```text
Here are customer interviews/reviews/support notes.

First separate direct evidence from interpretation.
Find recurring problems, alternatives, desired outcomes, contradictions,
and customer language that could change our marketing decision.
Do not claim prevalence unless the evidence supports it.
Then tell me what message is justified and what remains unknown.
```

### Improve a product listing

```text
Platform: Shopee
Goal: improve this listing without inventing claims.

Verified product facts:
[paste facts]

Current listing:
[paste listing]

Tell me which information belongs in the title, attributes, description,
or another platform-supported field, then give me the revised version.
```

### Diagnose a performance drop

```text
Our conversion rate fell from X to Y.
Here are the traffic, device, campaign, and funnel changes we know about.

Do not jump to a cause.
Decompose where the decline is concentrated, keep competing explanations,
and tell me the highest-value check to run next.
```

### Adapt content without reopening strategy

```text
The audience, message, proof, and CTA below are already approved.
Adapt this for LinkedIn.
Do not change the positioning unless something is incompatible with the platform.
Keep the output under 120 words.
```

### Prepare for conversational product discovery

```text
Here are the verified product facts, compatibility constraints, variants,
and current product information.

Help make the product easier to resolve for conversational shopping.
Do not guess model ranking weights or add keyword stuffing.
Identify which shopper requirements need structured facts versus explanation,
and what important information is still missing.
```

## Status

**Current release: v0.3.0 — Commerce & Addressable Knowledge.**

Marketing Practitioner is under active development.

The current main branch includes:

- the decision-first runtime controller;
- research, segmentation, positioning, messaging/copy, diagnosis, learning, and international/ethics handbook layers;
- a shared social/content-environment model plus five social platform modules;
- a shared commerce/product-discovery model plus six commerce platform modules;
- conversational and agent-mediated commerce boundaries;
- addressable just-in-time knowledge routing for large knowledge surfaces;
- targeted audits and smoke tests.

The project does **not** claim complete knowledge of private platform ranking systems or universal runtime reliability. Platform behavior is time-sensitive, evidence is scoped, and the architecture is expected to improve through real use and concrete failures rather than by adding abstractions for their own sake.

## Contributing

Contributions are welcome when they preserve the evidence and scope discipline of the project. See [`CONTRIBUTING.md`](CONTRIBUTING.md).

For platform changes, prefer current first-party or otherwise strong evidence and keep eligibility, retrieval, ranking, recommendation, representation, commercial state, and observed outcomes separate when the distinction matters.

## Attribution

The repository synthesizes marketing research, methodological literature, recommender-system and platform research, current product documentation, and practical writing methods. Its copywriting and human-writing sections were also informed by MIT-licensed work from the AI Copywriter / humanizer lineage.

See [`THIRD_PARTY_NOTICES.md`](THIRD_PARTY_NOTICES.md), [`skills/marketing-practitioner/references/bibliography.md`](skills/marketing-practitioner/references/bibliography.md), and the scoped evidence notes under [`skills/marketing-practitioner/references/`](skills/marketing-practitioner/references/).

## License

MIT. See [`LICENSE`](LICENSE).
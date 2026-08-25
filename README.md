<div align="center">

<img src="assets/marketing-practitioner-banner.webp" alt="Marketing Practitioner banner" width="100%">

# Marketing Practitioner

**Research-first marketing decision system for AI agents.**

*Learn the market before writing the copy.*

[![Version: v0.8.0](https://img.shields.io/badge/version-v0.8.0-0a7.svg)](#status)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Language: English](https://img.shields.io/badge/language-English-4c1.svg)](#)
[![Format: Agent Skill](https://img.shields.io/badge/format-Agent%20Skill-6f42c1.svg)](skills/marketing-practitioner/SKILL.md)
[![skills.sh](https://skills.sh/b/quocbao201104/marketing-practitioner-skill)](https://skills.sh/quocbao201104/marketing-practitioner-skill)

</div>

---

Marketing Practitioner gives an AI agent a disciplined way to turn messy market evidence into bounded marketing decisions — across customer research, segmentation, positioning, **commercial design and pricing**, messaging, **landing-page architecture**, **email communication architecture**, **search & discovery architecture**, copy, platform content, commerce, product discovery, diagnosis, experimentation, localization, and learning.

It is not a bag of growth hacks or prompt templates. The runtime starts from the job you actually need done, freezes decisions that are already resolved, loads deeper knowledge only when it can change the open decision, and returns the minimum useful output for that job.

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

Then talk to your agent normally. You do **not** need to know marketing vocabulary such as ICP, JTBD, positioning, willingness to pay, attribution, retrieval, or conversion architecture before using the skill.

Start with three things:

1. **What are you trying to do?**
2. **What do you already know or have?**
3. **Where will the decision be used, if that matters?**

Not sure what belongs in the prompt? See the [`Task Specification Guide`](TASK-SPECIFICATION-GUIDE.md). It gives a reusable starter, missing-information policy, and progressively richer examples without requiring a rigid form or prompt-engineering vocabulary.

### Let the agent compile the task specification

You can give the agent your rough request, notes, files, and whatever context you already have, then say:

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

## What it can help with

### Customer and market understanding

- synthesize interviews, reviews, survey responses, support records, and sales notes;
- separate observation from interpretation and hypothesis;
- preserve contradictions, segment differences, unknowns, and evidence scope;
- identify recurring problems, alternatives, customer language, and decision-relevant patterns.

### Segmentation, positioning, and value

- decide which customer/context differences actually change the marketing decision;
- reason about relevant alternatives, including manual work, delay, internal labor, and doing nothing;
- connect a target context to a prioritized value, credible proof, trade-offs, and claim boundaries;
- avoid treating competitor whitespace as automatic customer value.

### Commercial design, pricing, and terms

Version 0.5.0 introduced a bounded Commercial Design reasoning layer for unresolved exchange decisions.

It can help decide:

```text
1. CONFIGURATION / ENTITLEMENT
   What is included, accessible, bundled, metered, or limited?

2. PAYMENT / VALUE-CAPTURE ARCHITECTURE
   Who pays whom, for what unit/event/outcome, using what metric/tariff/menu?

3. RELATIONSHIP / RISK TERMS
   What commitment, renewal, cancellation, refund, guarantee, timing, or risk terms apply?

4. SELECTION / ALLOCATION RULE
   Who can access which conditions, and through universal, self-selected,
   eligibility-based, personalized, or negotiated rules?
```

Typical questions include:

- per-seat vs usage vs hybrid pricing;
- package or bundle boundaries;
- free trial vs free tier;
- monthly vs annual commitment;
- new-customer-only conditions;
- grandfathering vs migration;
- standardized vs negotiated commercial regimes;
- what WTP, conjoint, competitor, cost, historical, or experimental evidence actually supports.

The skill deliberately keeps these distinctions:

```text
VALUE PROPOSITION
!= COMMERCIAL DESIGN

COMMERCIAL DESIGN
!= CURRENT COMMERCIAL STATE / REPRESENTATION

COMMERCIAL DESIGN
!= COMMERCIAL GOVERNANCE
!= EXECUTED COMMERCIAL INSTANCE

MARKET-DESIRABLE
!= ECONOMICALLY ATTRACTIVE
!= OPERATIONALLY FEASIBLE
!= PERMISSIBLE
!= AUTHORIZED
```

Commercial Design can consume authoritative Product, Finance, Operations, Sales-governance, Legal/Compliance, and platform constraints. It must not invent or override them.

### Messaging, copy, and critique

- build message hierarchy and proof architecture when needed;
- write landing pages, emails, campaigns, social content, product communication, and short-form copy;
- preserve the supplied voice and facts;
- distinguish internal constraints from information that actually belongs in the message;
- review claims, relevance, clarity, proof, channel fit, CTA coherence, and naturalness.

### Landing-page architecture

Version 0.6.0 adds a bounded specialist path for turning already-resolved reader, message, proof, commercial, and action state into page information/action architecture.

It can help decide:

- what information must appear before a target action becomes reasonable;
- what must precede what without assuming a fixed section template;
- where claim-supporting proof, material objections, risk reducers, and commercial facts belong;
- whether text, screenshot, annotation, diagram, artifact, motion, or another carrier best performs an information job;
- how CTA availability differs from visitor action readiness;
- which form fields are justified now, including qualification and sensitive-data explanation;
- how navigation can distinguish legitimate blocker resolution from decision-irrelevant exits;
- how comparison/pricing state should be represented without reopening Commercial Design;
- how desktop structure should linearize responsively while preserving meaningful sequence and discoverability.

The path deliberately keeps these boundaries:

```text
LANDING PAGE != SECTION TEMPLATE
CTA AVAILABILITY != CTA READINESS
PROOF != TESTIMONIAL
OBJECTION != FAQ
SCREENSHOT != PROOF BY DEFAULT
FRICTION != BAD BY DEFAULT
MOBILE != STACKED DESKTOP
COMMERCIAL REPRESENTATION != COMMERCIAL DESIGN
BEHAVIORAL OBSERVATION != CAUSAL EXPLANATION
```

Chapter 04 still owns unresolved message, claim, and proof decisions; Chapter 10 owns unresolved Commercial Design; Chapter 05 owns causal diagnosis and experimentation. Chapter 11 allocates already-resolved state across the page.

### Email communication architecture

Version 0.7.0 adds a bounded specialist path for deciding whether, when, and how email should carry already-resolved strategy.

It can help decide:

- whether the current state justifies `SEND`, `WAIT`, `EXIT`, `SUPPRESS`, `DO NOTHING`, or another channel/human handoff;
- how communication need differs from communication authority and operational feasibility;
- how recipient, relation, endpoint, prior-contact, suppression, and channel state should remain scoped instead of collapsing into one global send-eligibility flag;
- how sequence, branching, waiting, and exit should follow state/history rather than a fixed cadence recipe;
- how sender, subject, preview, message body, and optional action/handoff should carry one coherent communication job;
- how email-to-reply, landing-page, app, checkout, docs, or human handoffs should preserve decision-relevant meaning;
- how send attempts, receiver acceptance, tracked opens, clicks, attributed outcomes, and causal effects must remain distinct.

The path deliberately keeps these boundaries:

```text
EMAIL != SEQUENCE
SEQUENCE != FIXED ORDERED MESSAGE LIST
COMMUNICATION NEED != COMMUNICATION AUTHORITY != OPERATIONAL FEASIBILITY
PERMISSION / SUPPRESSION != GLOBAL RECIPIENT BOOLEAN
TRACKED OPEN != VERIFIED HUMAN OPEN != ATTENTION
CLICK != INTENT
ATTRIBUTED ACTION != CAUSED ACTION
ACTION / DESTINATION IS OPTIONAL
```

Chapter 04 still owns unresolved message, claim, and proof decisions; Chapter 05 owns causality and experimentation; Chapter 08 owns generic relationship/state/representation grammar; Chapter 10 owns unresolved commercial transitions; Chapter 11 owns downstream landing-page architecture. Current legal, regulatory, provider, authentication, and transport constraints remain just-in-time authoritative dependencies rather than a built-in compliance engine.

### Search & discovery architecture

Version 0.8.0 adds a bounded specialist path for generic, non-commerce discovery decisions: how information objects, entities, sources, pages, and documents become available to, retrieved by, selected by, represented through, or observed within discovery systems.

It can help distinguish:

- information need from query, query from unique intent, and user expression from system retrieval formulation;
- published from system-known, accessible, processed, indexed/available, and retrievable state;
- publisher-preferred identity from system-selected representative identity;
- retrieval from selection and surfacing;
- human-selection discovery from system-commitment/grounding in AI answer systems;
- citation from authority, endorsement, faithful source use, or causal influence;
- impression from verified attention, click from relevance, and no-click from failure;
- search interest from customer count, purchase intent, or market demand.

The path deliberately keeps these boundaries:

```text
SEARCH IS ONE MODE OF DISCOVERY
DISCOVERY DOES NOT REQUIRE AN EXPLICIT QUERY
QUERY != INFORMATION NEED != RETRIEVAL FORMULATION
PUBLISHED != SYSTEM-KNOWN != RETRIEVABLE
DISCOVERABILITY IS SCOPED
RETRIEVED != SELECTED != EVIDENTIARY FIT
SURFACING AN OPTION != COMMITTING INFORMATION INTO AN ANSWER
CITATION != AUTHORITY != CAUSAL INFLUENCE
SEARCH INTEREST != MARKET DEMAND
```

Chapter 01/02 still own customer/segment/market-demand inference; Chapter 04 owns marketing claim/proof; Chapter 05 owns causality and incrementality; Chapter 08 remains the shared platform/content grammar; Chapter 09 owns product/listing/commerce discovery; Chapter 11 owns landing-page architecture after entry. Current crawler controls, indexing directives, provider eligibility rules, ranking/recommendation disclosures, AI-search controls, and telemetry definitions remain just-in-time authoritative dependencies rather than timeless SEO/GEO/AEO rules.

### Social content and distribution environments

The shared content-environment model supports current modules for:

- Facebook;
- Instagram;
- LinkedIn;
- TikTok;
- X.

The skill does not reduce platform work to “write in the right tone.” It can reason about content objects, representations, audience state, delivery and permission edges, interaction provenance, platform mediation, measurement, and recommendation boundaries when those distinctions matter.

See [`skills/marketing-practitioner/platforms/README.md`](skills/marketing-practitioner/platforms/README.md) for the platform map.

### Commerce and product discovery

The commerce layer covers generic product-discovery reasoning plus current modules for:

- Google Shopping / Google commerce;
- Amazon;
- TikTok Shop;
- Shopee;
- Etsy;
- Lazada.

It can reason about product/listing/catalog identity, variants, structured product information, product cards and PDPs, price/stock/promotion state, retrieval versus ranking, search versus recommendation, conversational product discovery, agent-mediated commerce, checkout authority, and commerce-performance diagnosis.

```text
PRODUCT / OBJECT != REPRESENTATION != ENCOUNTER SURFACE
RETRIEVAL != RANKING != FILTERING != RECOMMENDATION
PRODUCT FACT != COMMERCIAL STATE != OBSERVED FEEDBACK
SHOPPER INTENT != DELEGATED AUTHORITY != EXECUTED EFFECT
```

See [`skills/marketing-practitioner/platforms/commerce/README.md`](skills/marketing-practitioner/platforms/commerce/README.md) for the commerce-platform map.

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

A noun does not activate a full reasoning path by itself.

```text
"Price is fixed at $29. Write the landing-page copy."
→ price is resolved
→ message/copy path
→ do not reopen Commercial Design

"Message, proof, price, and CTA are approved. Decide the page sequence and where the product visual belongs."
→ upstream state is resolved
→ landing-page.*
→ do not load Chapter 04 merely as a routing hop

"This email is approved. Make it 20% shorter."
→ no substantive email-architecture decision remains
→ narrow copy fast path
→ do not load email.* merely because the artifact is email

"Email #3 got no response yesterday. Should we send #4 now?"
→ no action is not negative intent
→ email.send-decision / email.sequence
→ SEND / WAIT / EXIT depends on current state and history, not a fixed cadence

"Our page ranks in Google but is rarely cited in AI answers. Rewrite it for AI."
→ web ranking does not establish AI availability/selection/grounding state
→ discovery.availability / selection / commitment only as needed
→ rewrite only if evidence localizes the defect to content/message/representation

"Should this be $29 or $39?"
→ commercial condition is unresolved
→ Commercial Design

"Shopee shows a lower voucher-adjusted price for this buyer. What does that mean?"
→ current commerce-state interpretation
→ Chapter 09 / Shopee knowledge

"Conversion fell after the price change. Why?"
→ causal diagnosis
→ Chapter 05 first
```

## Addressable just-in-time knowledge

Large knowledge surfaces are addressable through a lightweight semantic routing layer.

```text
OPEN DECISION
→ KNOWLEDGE NAMESPACE
→ LOGICAL KNOWLEDGE ID
→ routing-index.json
→ EXACT SECTION WHEN SUPPORTED
```

Examples:

```text
commercial-design.payment
commercial-design.dynamics
landing-page.sequence
landing-page.action-form
landing-page.responsive
email.send-decision
email.observation
discovery.availability
discovery.commitment
discovery.observation
commerce.identity
commerce.resolvability
shopee.conversational-discovery
tiktok.machine-mediation
x.interaction-provenance
```

When helper execution is available:

```bash
python skills/marketing-practitioner/scripts/get-knowledge.py commercial-design.payment
python skills/marketing-practitioner/scripts/get-knowledge.py landing-page.sequence
python skills/marketing-practitioner/scripts/get-knowledge.py email.send-decision
python skills/marketing-practitioner/scripts/get-knowledge.py discovery.availability
python skills/marketing-practitioner/scripts/get-knowledge.py discovery.commitment
python skills/marketing-practitioner/scripts/get-knowledge.py commerce.resolvability
python skills/marketing-practitioner/scripts/get-knowledge.py --list --namespace shopee
```

Evidence records use intrinsic source IDs rather than being duplicated into the semantic routing table:

```bash
python skills/marketing-practitioner/scripts/get-knowledge.py --source CD08
python skills/marketing-practitioner/scripts/get-knowledge.py --source EM03
python skills/marketing-practitioner/scripts/get-knowledge.py --source SD09
python skills/marketing-practitioner/scripts/get-knowledge.py --source R23
python skills/marketing-practitioner/scripts/get-knowledge.py --source A03
```

The helper is an optimization, not a requirement. If a host cannot execute it, the agent can use `routing-index.json` as an address table and read the smallest feasible section or file while preserving dependency-first routing.

## Evidence discipline

The repository uses a conservative standard for claims and learning:

- qualitative recurrence does not establish population prevalence;
- descriptive data do not by themselves establish causality;
- attribution does not equal incrementality;
- tracked-open telemetry does not establish verified human attention;
- stated/hypothetical WTP does not equal revealed choice or an optimal price;
- historical price/sales association does not automatically establish causal elasticity;
- competitor price does not determine our optimal price;
- conversion does not equal revenue, margin, retention, or LTV;
- platform eligibility does not guarantee exposure;
- published or indexed state does not establish universal cross-system discoverability;
- citation does not establish authority, endorsement, faithful source use, or causal influence;
- search interest does not directly establish customer count, purchase intent, or market demand;
- observed engagement does not automatically establish organic human preference;
- a ranking signal or exposed implementation parameter is not automatically a writing instruction;
- machine- or platform-inferred product information is not automatically verified product truth;
- uncertainty, contradiction, and inconclusive results are valid states;
- stronger claims require stronger evidence.

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
├── evals/                         # audits and smoke tests OF the skill
├── research/                      # research lineage; not runtime skill knowledge
│
└── skills/
    └── marketing-practitioner/
        ├── SKILL.md                # governing runtime controller
        ├── TASK-SPECIFICATION-GUIDE.md
        ├── routing-index.json      # logical knowledge addresses
        ├── scripts/
        │   ├── get-knowledge.py
        │   └── test-knowledge-routing.py
        ├── handbook/
        │   ├── README.md
        │   ├── 00-foundations-and-method.md
        │   ├── 01-customer-research-and-evidence.md
        │   ├── 02-segmentation-icp-and-jtbd.md
        │   ├── 03-positioning-and-value.md
        │   ├── 04-messaging-proof-and-copy.md
        │   ├── 05-diagnosis-causality-and-experimentation.md
        │   ├── 06-organizational-learning.md
        │   ├── 07-international-marketing-and-ethics.md
        │   ├── 08-content-environments-and-distribution.md
        │   ├── 09-commerce-environments-and-product-discovery.md
        │   ├── 10-commercial-design-pricing-and-terms.md
        │   ├── 11-landing-page-architecture.md
        │   ├── 12-email-communication-architecture.md
        │   └── 13-search-and-discovery-architecture.md
        ├── platforms/
        │   ├── README.md
        │   ├── facebook.md
        │   ├── instagram.md
        │   ├── linkedin.md
        │   ├── tiktok.md
        │   ├── x.md
        │   └── commerce/
        │       ├── README.md
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

The [`handbook/README.md`](skills/marketing-practitioner/handbook/README.md) gives the chapter map. Platform READMEs are navigation aids for humans; they do not replace `SKILL.md` or `routing-index.json` as the runtime contract.

### Research vs runtime knowledge

The repository can preserve deep research without forcing it into every skill installation path.

```text
research/
= exploration, rejected hypotheses, prior-art attack, theory freeze lineage

skills/marketing-practitioner/
= compressed governed runtime knowledge
```

For example, the Commercial Design, Landing-Page Architecture, Email Communication Architecture, and Search & Discovery Architecture research tracks record why their bounded specialist knowledge exists, what candidate abstractions were rejected, and which evidence boundaries survived adversarial review. Runtime chapters contain only the compact practitioner interfaces needed by the agent.

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

### Decide a pricing architecture

```text
Audience and positioning are already resolved.

We are deciding whether to charge per seat, per usage, or with a base + usage model.
Here are the verified product capabilities, cost constraints, current alternatives,
and the customer evidence we have.

Do not invent finance, legal, product, or sales-authority facts.
Separate what the evidence supports from what remains uncertain.
Recommend the smallest defensible decision or next evidence step.
```

### Design a landing-page architecture without reopening strategy

```text
The reader, positioning, message, proof, commercial conditions, and CTA below are already approved.

Decide the landing-page information sequence, proof/risk placement, visual jobs,
form/CTA structure, and responsive reading order.
Do not invent a fixed section template or reopen upstream strategy unless a material dependency is actually unresolved.
```

### Decide whether the next email should exist

```text
The audience, message, proof, and commercial state are already resolved.
Here is the relevant email relation, prior-contact history, suppression/permission state,
and the observations we actually have.

Decide whether the next communication should be SEND, WAIT, EXIT, SUPPRESS,
DO NOTHING, or another channel/human handoff.
Do not infer negative intent from no response, human attention from a tracked open,
or a universal cadence from generic email best practices.
If current legal/provider authority can change the answer, treat it as a just-in-time dependency.
```

### Diagnose discovery before rewriting

```text
This page is published and ranks in one search surface, but visibility, referrals,
or AI citations are weaker than expected.

Do not assume the content is the problem.
Separate system-scoped availability, retrieval/selection, surfaced representation or
system-commitment/grounding, and the exact telemetry definition first.
Treat current provider rules as just-in-time evidence.
Rewrite only if the evidence actually localizes the defect to content/message/representation.
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
The audience, message, proof, commercial conditions, and CTA below are already approved.
Adapt this for LinkedIn.
Do not reopen upstream strategy unless something is materially incompatible.
Keep the output under 120 words.
```

## What this repository is not

Marketing Practitioner is not:

- a prompt collection;
- a copy-template pack;
- an SEO checklist;
- a GEO/AEO/LLMO hack library;
- a landing-page template system;
- a CRM, lifecycle, journey, or campaign-automation system;
- an email deliverability or legal-compliance engine;
- a library of platform “algorithm hacks”;
- a universal marketing funnel;
- a pricing optimizer;
- a substitute for authoritative finance, product, operations, legal, or sales decisions;
- a guarantee that more engagement means more customer value;
- a claim that public ranking signals reveal a platform's complete production system;
- a guarantee of ranking, recommendation, retrieval, citation, or answer inclusion;
- a substitute for missing product truth or missing evidence.

## Status

**Current release: v0.8.0 — Search & Discovery Architecture.**

The current main branch includes:

- the decision-first runtime controller;
- research, segmentation, positioning, messaging/copy, diagnosis, learning, and international/ethics handbook layers;
- a bounded Commercial Design layer for configuration/entitlement, payment architecture, relationship/risk terms, selection/allocation, evidence, governance, and transitions;
- a bounded Landing-Page Architecture specialist layer for page job/entry state, action readiness, information dependency, proof/risk/visual allocation, CTA/forms, comparison representation, and responsive meaningful sequence;
- direct JIT `landing-page.*` routing when upstream message/proof/commercial state is already resolved;
- a bounded Email Communication Architecture specialist layer for send/wait/exit/suppress decisions, scoped relation/endpoint state, state-conditioned sequence reasoning, inbox/body/action allocation, continuity, and observation semantics;
- direct JIT `email.*` routing for email-specific decisions while ordinary email rewrites remain on the narrow copy fast path;
- a bounded Search & Discovery Architecture specialist layer for discovery need/expression, scoped availability, retrieval/selection, human-selection vs system-commitment/grounding, and discovery observation semantics;
- direct JIT `discovery.*` routing for generic non-commerce discovery decisions while narrow search-related transformations remain on the fast path;
- the generic Chapter 08 owned-channel composition path for non-email channels such as SMS and push;
- a shared social/content-environment model plus five social platform modules;
- a shared commerce/product-discovery model plus six commerce platform modules;
- conversational and agent-mediated commerce boundaries;
- addressable just-in-time knowledge routing for large knowledge surfaces;
- conditional cross-domain handoffs hardened against decision-relevant state loss;
- research-backed task specification and agent-side prompt compilation;
- scoped research lineage plus targeted adversarial reviews and runtime smoke tests.

The project does **not** claim complete knowledge of private platform ranking/retrieval systems, universal discovery or citation rules, a universally optimal pricing method, a universal landing-page template, universal email cadence/send-time/personalization rules, legal/provider compliance for every context, or universal runtime reliability. The architecture is expected to improve through real use and concrete failures rather than by adding abstractions for their own sake.

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

## Contributing

Contributions are welcome when they preserve the evidence and scope discipline of the project. See [`CONTRIBUTING.md`](CONTRIBUTING.md).

For platform changes, prefer current first-party or otherwise strong evidence and keep eligibility, retrieval, ranking, recommendation, representation, commercial state, and observed outcomes separate when the distinction matters.

For new top-level reasoning capabilities, establish the decision-relevant gap and theory boundary before implementation.

## Attribution

The repository synthesizes marketing research, methodological literature, recommender-system and platform research, current product documentation, pricing and commercial-design research, landing-page/CRO usability research, email/provider/transport/privacy/regulatory research, information-retrieval and discovery research, and practical writing methods. Its copywriting and human-writing sections were also informed by MIT-licensed work from the AI Copywriter / humanizer lineage.

See [`THIRD_PARTY_NOTICES.md`](THIRD_PARTY_NOTICES.md), [`skills/marketing-practitioner/references/bibliography.md`](skills/marketing-practitioner/references/bibliography.md), and the scoped evidence notes under [`skills/marketing-practitioner/references/`](skills/marketing-practitioner/references/).

## License

MIT. See [`LICENSE`](LICENSE).
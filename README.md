<div align="center">

<img src="assets/marketing-practitioner-banner.webp" alt="Marketing Practitioner banner" width="100%">

# Marketing Practitioner

**Evidence-informed marketing reasoning for AI agents and practitioners.**

*Learn the market before writing the copy.*

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Language: English](https://img.shields.io/badge/language-English-4c1.svg)](#)
[![Format: Agent Skill](https://img.shields.io/badge/format-Agent%20Skill-6f42c1.svg)](skills/marketing-practitioner/SKILL.md)
[![skills.sh](https://skills.sh/b/quocbao201104/marketing-practitioner-skill)](https://skills.sh/quocbao201104/marketing-practitioner-skill)

</div>

---

## Quick start

Install with the Skills CLI:

```bash
npx skills add quocbao201104/marketing-practitioner-skill
```

Then give your agent the market material and the decision you need to make. For example:

```text
I am repositioning this product for a new segment.
Here are the product notes, customer interviews, reviews, and current landing page.

Separate evidence from interpretation, identify contradictions and unknowns,
recommend the strongest evidence-compatible positioning and message strategy,
then draft the landing page without inventing claims.
```

The intended behavior is not to jump directly to polished copy. The skill first establishes what the evidence supports, what remains uncertain, who the message is for, which alternative matters, what positioning is defensible, and which claims can be made. Copy comes after those choices.

## How the skill works

This repository follows the Agent Skills model. The installable skill lives in [`skills/marketing-practitioner/`](skills/marketing-practitioner/). Its `SKILL.md` contains the operational instructions, while the handbook, frameworks, and bibliography sit inside the same skill directory so they travel with the installed package.

In a skills-compatible client, the expected loading pattern is progressive:

```text
DISCOVER
name + description
      ↓
ACTIVATE
read SKILL.md when the task matches
      ↓
EXECUTE
follow the operating method
      ↓
DEEPEN WHEN NEEDED
consult handbook / frameworks / references
```

Exact installation, discovery, and activation behavior depends on the agent client. The package is structured so an agent can load the operating instructions first and consult only the task-relevant supporting resources when needed.

## Overview

Marketing Practitioner is a domain skill and compact handbook for evidence-informed marketing work. It is designed for AI agents, marketers, copywriters, founders, researchers, and growth practitioners who need a disciplined path from market evidence to positioning, messaging, copy, experimentation, and learning.

The repository is built around a simple premise: **copy is an expression layer of marketing strategy, not a substitute for it**. Strong prose cannot repair unclear positioning, weak evidence, an undefined audience, or unsupported claims. Marketing practice therefore begins with market learning and proceeds through explicit choices before it reaches copy.

The core sequence is:

```text
MARKET EVIDENCE
      ↓
CUSTOMER UNDERSTANDING
      ↓
SEGMENT / CONTEXT SELECTION
      ↓
POSITIONING
      ↓
MESSAGE STRATEGY
      ↓
COPY / CAMPAIGN
      ↓
MARKET RESPONSE
      ↓
SCOPED LEARNING
```

This sequence is not presented as a universal law. It is an operating model that makes assumptions, evidence, choices, and uncertainty easier to inspect.

## What makes this repository different

Many marketing resources are organized as collections of tactics, templates, persuasion formulas, or channel-specific tricks. Marketing Practitioner instead treats marketing as a **learning and decision discipline**.

Its emphasis is on six forms of discipline:

1. **Evidence discipline** — distinguish source material, observation, interpretation, hypothesis, association, and causal claim.
2. **Scope discipline** — avoid turning findings from one segment, market, channel, or period into universal claims.
3. **Strategic discipline** — establish audience, alternatives, category frame, positioning, proof, and trade-offs before prose.
4. **Claim discipline** — prefer proof and mechanisms to promotional adjectives; never fabricate specificity.
5. **Measurement discipline** — distinguish symptoms from causes, attribution from incrementality, and proxy wins from business outcomes.
6. **Learning discipline** — retain failed hypotheses, contradictions, boundary conditions, and inconclusive results rather than only winners.

The copywriting component adds a reader-first and truth-first writing method, together with a human-writing audit that removes common machine-like patterns without flattening voice.

## Repository structure

```text
.
├── README.md
├── LICENSE
├── CONTRIBUTING.md
├── CHANGELOG.md
├── THIRD_PARTY_NOTICES.md
├── assets/
│   └── marketing-practitioner-banner.webp
│
└── skills/
    └── marketing-practitioner/
        ├── SKILL.md
        ├── handbook/
        │   ├── 00-foundations-and-method.md
        │   ├── 01-customer-research-and-evidence.md
        │   ├── 02-segmentation-icp-and-jtbd.md
        │   ├── 03-positioning-and-value.md
        │   ├── 04-messaging-proof-and-copy.md
        │   ├── 05-diagnosis-causality-and-experimentation.md
        │   ├── 06-organizational-learning.md
        │   └── 07-international-marketing-and-ethics.md
        ├── frameworks/
        │   ├── practitioner-cards.md
        │   └── quality-rubrics.md
        └── references/
            └── bibliography.md
```

### `skills/marketing-practitioner/SKILL.md`

The operational specification for an AI agent. It defines when the skill should be used, the reasoning order, evidence rules, copywriting constraints, output standards, and which supporting resources to load for a task.

### `handbook/`

The conceptual body of knowledge packaged with the skill. Chapters are written as a structured reference rather than a sequence of prompt recipes. They distinguish established concepts, practical heuristics, and claims that require further evidence.

### `frameworks/`

Compact working instruments for research synthesis, positioning, messaging, diagnosis, experiments, and postmortems.

### `references/`

A selected bibliography emphasizing peer-reviewed research, academic monographs, primary methodological sources, and carefully bounded practitioner references.

## Intended uses

For an **AI agent**, the repository supplies a stable reasoning discipline for tasks such as customer-research synthesis, ICP selection, positioning, message strategy, landing-page copy, email copy, campaign critique, funnel diagnosis, experiment design, localization, and marketing postmortems.

For a **human practitioner**, the handbook can be read as a compact curriculum. It is deliberately broader than copywriting because writing quality depends on the quality of the market model and strategic choices that precede it.

## Epistemic policy

The repository uses a conservative standard for marketing claims:

- qualitative research provides depth, language, context, and mechanisms, but does not by itself establish population prevalence;
- descriptive data do not by themselves establish causality;
- attribution does not equal incrementality;
- multiple derivatives from one source do not become independent evidence;
- uncertainty and inconclusive results are valid outputs;
- strong claims require commensurately strong evidence;
- learning remains scoped to the population, market, channel, product state, and period that support it;
- cultural models are priors for inquiry, not deterministic profiles of individuals;
- persuasive communication must not depend on fabricated scarcity, hidden costs, false social proof, or other deceptive choice architecture.

## Copywriting policy

The writing method is reader-first and truth-first. Before optimizing style, it establishes the reader's situation, the mental category in which the offer will be evaluated, the relevant alternative, the message to express, and the proof available.

Human-sounding writing is treated as a **quality floor rather than a strategy**. The goal is not merely to remove recognizable AI patterns. The goal is to produce clear, specific, evidence-compatible prose with appropriate voice, rhythm, and channel fit.

## Installation for agents

The fastest installation path for compatible clients is the Skills CLI:

```bash
npx skills add quocbao201104/marketing-practitioner-skill
```

To install or inspect it manually, clone the repository:

```bash
git clone https://github.com/quocbao201104/marketing-practitioner-skill.git
```

The installable package is [`skills/marketing-practitioner/`](skills/marketing-practitioner/). The directory name matches the skill name, and the supporting handbook, frameworks, and bibliography are packaged beneath the same directory so relative resource references remain valid after installation.

## Status

**v0.1.2 — Packaging.** The foundation release established the domain model, operational skill, academic reference structure, practitioner instruments, and explicit resource routing. v0.1.2 packages the skill and its supporting resources together under `skills/marketing-practitioner/` for stricter Agent Skills compatibility and more reliable multi-file installation.

## Attribution

The repository synthesizes marketing research, methodological literature, and practical writing methods. Its copywriting and human-writing sections were also informed by MIT-licensed work from the AI Copywriter / humanizer lineage. See [`THIRD_PARTY_NOTICES.md`](THIRD_PARTY_NOTICES.md) and [`skills/marketing-practitioner/references/bibliography.md`](skills/marketing-practitioner/references/bibliography.md).

## License

MIT. See [`LICENSE`](LICENSE).
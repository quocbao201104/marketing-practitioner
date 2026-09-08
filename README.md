<div align="center">

<img src="assets/brand/banner.svg" alt="Marketing Practitioner banner" width="100%">

# Marketing Practitioner

**From customer evidence to marketing decisions and execution.**

A reusable marketing skill for people working with AI: research customers, shape strategy, create content, and interpret results—with claims grounded in evidence.

[![Version: v1.7.0](https://img.shields.io/badge/version-v1.7.0-0a7.svg)](#status-and-scope)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Language: English](https://img.shields.io/badge/language-English-4c1.svg)](#)
[![Format: Agent Skill](https://img.shields.io/badge/format-Agent%20Skill-6f42c1.svg)](skills/marketing-practitioner/SKILL.md)
[![skills.sh](https://skills.sh/b/quocbao201104/marketing-practitioner)](https://skills.sh/quocbao201104/marketing-practitioner)

**[What you can do](#what-you-can-do) · [Quick start](#quick-start) · [How it works](#how-it-works) · [Research](#research-and-verification) · [Contributing](#contributing)**

<sub><strong>Customer evidence · Strategy · Communication · Diagnosis · Learning</strong></sub>

</div>

---

Marketing Practitioner gives marketers, founders, researchers, and content teams a shared foundation for AI-assisted customer research, positioning, commercial choices, communication, distribution, and result interpretation. Use it to turn interviews into a grounded account, compare positioning options, write a page from an adopted strategy, or investigate a performance change before choosing an intervention.

The skill connects those jobs when the work requires it. A simple rewrite can stay simple; a larger assignment can carry evidence, selected choices, and remaining questions from research through to the requested artifacts.

## What you can do

| Bring a task | Work toward a useful result |
| --- | --- |
| Understand customers or a market | A scoped synthesis of needs, alternatives, barriers, and conflicting evidence |
| Choose an audience, position, or commercial approach | Comparable options and a supported recommendation, with material trade-offs |
| Explore or refine brand identity | Distinct visual directions or a focused refinement that preserves selected identity |
| Write or critique marketing communication | Copy, landing-page content, or email that expresses the strategy and matches the available proof |
| Adapt content or product information | Representations suited to the platform, shopper, or local context, with supported meaning intact |
| Investigate search, paid-media, or commerce performance | What the observations establish, plausible explanations, and a useful next check |
| Plan a test or learn from results | A decision-linked comparison or a reusable finding with its evidence limits |

These are supported work areas, not guarantees of marketing performance. The agent's model, available evidence, and execution tools still matter.

## Quick start

Choose your environment. The skill and reference material are the same in every package.

### Local: apps and CLI

| Use it in | Install manually |
| --- | --- |
| **Codex app** | Download the repo ZIP, copy the skill into your personal skills folder, then reopen Codex. [Folder paths and steps](docs/local-setup.md#codex-app-install-manually-with-files) |
| **Claude desktop** | Customize > Plugins > Add marketplace > Add from a Repository, then Install. [Step-by-step](docs/local-setup.md#claude-desktop-install-through-the-app) |
| **CLI** | Run the command below, or use the [Claude Code plugin](docs/claude-code-plugin.md) / [Codex plugin](docs/plugin.md) instructions. |

```bash
npx skills add quocbao201104/marketing-practitioner
```

<details>
<summary>Prefer to ask your agent to install it?</summary>

Paste this into an app or CLI with installation tools:

```text
Install Marketing Practitioner from
https://github.com/quocbao201104/marketing-practitioner
for this app, using its supported installation method.
Preserve existing customizations and confirm the installation.
```

</details>

### Web: Claude and ChatGPT

| Use it in | Install manually |
| --- | --- |
| **Claude** | Add the [repository](https://github.com/quocbao201104/marketing-practitioner) as a marketplace, then install Marketing Practitioner. [Steps](docs/web-setup.md#claude-add-the-repository-marketplace) |
| **ChatGPT** | Plugins > Skills > Create > Upload from your computer. [Prepare files and upload](docs/web-setup.md#chatgpt-upload-a-personal-skill) |

> **ChatGPT plans:** Skills are documented for eligible **Business, Enterprise, Healthcare, and Edu** accounts, subject to workspace settings. Do not assume Free, Plus, or Pro includes skill upload. [OpenAI guidance](https://help.openai.com/en/articles/20001066-skills-in-chatgpt).

> **Keep it current:** check for updates periodically, for example monthly or before a major project. You can ask your agent to update it or follow the [update steps for your installation](docs/local-setup.md#keep-it-updated).

### Your first task

Once the skill or reference files are available in your workspace, start with an ordinary request. Include these when available:

1. what you need done **now**;
2. the facts, evidence, adopted choices, and proposals you want reviewed;
3. where the result will be used, if that changes the answer.

```text
Use Marketing Practitioner.
Using the attached product facts and approved positioning,
write a landing-page outline and a launch email.
Keep the price and product claims fixed.
Make each artifact useful for its own reader and next action.
```

No internal vocabulary is required. “Help me decide which customer group to focus on” is enough; you do not have to say ICP. The optional [Task Specification Guide](TASK-SPECIFICATION-GUIDE.md) can compile rough notes into a smaller spec without inventing missing facts.

Clone the full repository if you want to inspect or extend the skill:

```bash
git clone https://github.com/quocbao201104/marketing-practitioner.git
```

The governing runtime contract is [`skills/marketing-practitioner/SKILL.md`](skills/marketing-practitioner/SKILL.md). Its compact decision table gives direct knowledge entry points; the [operating guide](skills/marketing-practitioner/references/operating-guide.md) holds detailed path and handoff guidance for questions that need it.

## Why it exists

A fluent answer can still be the wrong marketing action.

| Failure to avoid | Design response |
| --- | --- |
| Invent a plausible product claim | Keep claims inside supplied or supported evidence |
| Treat a handful of interviews as market prevalence | Separate qualitative recurrence from population claims |
| Rewrite creative because CPA moved | Diagnose before selecting the intervention |
| Load a TikTok playbook because the prompt says “TikTok” | Route by decision dependency, not by noun |
| Reopen approved positioning while writing copy | Freeze resolved state unless it becomes contradictory, stale, or insufficient |
| Turn attribution into causality | Preserve what a result did — and did not — prove |

The core keeps distinctions that change marketing decisions:

```text
observation ≠ interpretation ≠ hypothesis ≠ decision
qualitative recurrence ≠ population prevalence
attribution ≠ incrementality ≠ causality
paid relationship ≠ paid delivery
reported metric ≠ optimization-eligible signal
displayed commercial state ≠ universal authoritative state
platform name ≠ reason to load that platform
local evidence ≠ country-wide behavioral rule
```

It has no authority to invent product, financial, legal, operational, sales, platform, or customer facts. Provider-controlled rules are just-in-time dependencies, not timeless growth laws stored in the repo.

## How it works

The skill starts from the current job, not from a predefined marketing funnel.

![Marketing Practitioner workflow: frame the task, use relevant guidance when needed, do the work, check quality, and return useful outputs. Material gaps lead back to the open question; a checkpoint is needed only when a material choice remains unresolved and user input or decision authority is still needed.](assets/diagrams/from-brief-to-marketing-decision.png)

Complex work can start with a brief working plan without waiting for approval. The agent proceeds on resolved or delegated choices; when a material choice remains unresolved and the request or retained context does not provide enough input or authority to decide, it prepares a concrete proposal and asks before the dependent work. Independent work can continue while you decide. Task size or HTML output alone does not create an approval gate.

Reads serve a remaining question; they are not completion by themselves. When evidence is missing, the agent is instructed to retrieve it, ask a material question, or give a useful bounded result.

For work spanning several steps, the core keeps track of requested outputs, adopted choices, unresolved dependencies, and evidence limits. A changed request updates the affected work; paused work retains its status for resumption when the host preserves that context.

Seven runtime jobs are recognized:

`WRITE` · `DECIDE` · `DIAGNOSE` · `RESEARCH / UNDERSTAND` · `ADAPT` · `TEST` · `LEARN`

A topic, artifact type, or platform name is not a job. A caption with an approved message stays a writing task. A price already fixed at `$29` stays frozen while the page is written. Paying a creator to publish is not automatically paid media. A CPA rise after a bidding change starts as diagnosis, not as a creative rewrite.

Specialist knowledge is loaded only when it can change the current result. The [handbook map](skills/marketing-practitioner/handbook/README.md), [platform modules](skills/marketing-practitioner/platforms/README.md), and [local-adaptation resources](skills/marketing-practitioner/adaptations/) help you explore the coverage; they are not a required reading sequence.

## Host compatibility

Installation guidance is organized into local apps/CLI and web (Claude and ChatGPT). See the [web setup guide](docs/web-setup.md) for product-specific controls and account eligibility.

The installable package keeps its controller, knowledge, references, and helper scripts together. A compatible host needs to load the skill and give the agent an allowed way to read its files. Python helper execution is useful for exact section retrieval, but it is optional.

The host controls skill activation, available tools, and how much context survives between turns or sessions. Keep important facts, adopted choices, and evidence boundaries in the current task or accessible project records; persistence is not guaranteed by the skill itself.

**Instructions guide the agent; they do not supply unavailable tools or external authority.** Producing design assets, accessing private data, or acting in an external system depends on the host's capabilities and the user's authorization.

## Under the hood

![Inside Marketing Practitioner: SKILL.md guides the agent; the index locates relevant knowledge in the handbook, platform modules, and local adaptations. Frameworks and references supply optional working aids, evidence boundaries, and report planning and presentation guidance.](assets/diagrams/inside-the-skill.png)

For complex reports, [report planning and presentation](skills/marketing-practitioner/references/report-planning-and-presentation.md) connects reader questions, section purposes, evidence, and useful visual forms across formats, with additional HTML delivery guidance.

Large knowledge is addressed by logical IDs in [`routing-index.json`](skills/marketing-practitioner/routing-index.json). Headings and file paths are implementation details.

When the host can run helpers, [`get-knowledge.py`](skills/marketing-practitioner/scripts/get-knowledge.py) resolves one route or one evidence source without reading the rest of the ledger:

```bash
python skills/marketing-practitioner/scripts/get-knowledge.py email.send-decision
python skills/marketing-practitioner/scripts/get-knowledge.py brand-identity.equity
python skills/marketing-practitioner/scripts/get-knowledge.py adapt-localization.relationship-realization
python skills/marketing-practitioner/scripts/get-knowledge.py --source PM01
```

If helper execution is unavailable, the same index remains the address table: read the smallest feasible section, or degrade to the smallest target file, rather than loading an entire chapter.

The current index validates at **264 routes / 248 evidence sources**. Evidence files state what a source **supports** and **does not support**; those bounds are part of claim control.

Shared architecture expands only when a decision-relevant failure cannot be repaired locally without material distortion. Research under [`research/`](research/) keeps theory freezes, audits, and rejected expansions out of the runtime until they survive that bar.

### Scoped local adaptation

Local adaptation follows the same rule. [`adaptations/`](skills/marketing-practitioner/adaptations/) contains scoped evidence that can specialize an **already-open decision owned elsewhere**; it is not a country-profile layer, cultural encyclopedia, or precedence engine.

Current reference units address scoped Vietnamese and Japanese wording choices where self-reference, recipient address, honorific targets, permission, or benefit can change the relationship expressed. They do not infer behavior from nationality or require a localization detour for every translated sentence. See the [contribution contract](skills/marketing-practitioner/adaptations/README.md) and [reference units](skills/marketing-practitioner/adaptations/localization.md).

## Repository map

```text
skills/marketing-practitioner/
  SKILL.md                  governing runtime controller
  agents/openai.yaml        optional UI metadata and explicit invocation starter
  routing-index.json        logical knowledge address table
  handbook/                 governed practitioner knowledge
  adaptations/              scoped local decision specializations
  platforms/                scoped social and commerce modules
  references/               operating guidance, evidence ledgers, bibliography
  scripts/                  deterministic routing checks

research/                   theory lineage and rejected hypotheses
evals/                      adversarial cases, smokes, and behavioral harness
scripts/verify.ps1          sole local/CI verification entrypoint
```

## Research and verification

The local and CI gate is:

```powershell
.\scripts\verify.ps1
```

It validates the package with the repository validator and the installed Codex validator when discoverable, checks 68 routing mechanics and **264 routes / 240 evidence sources**, runs the Pressure Discovery and behavioral harness tests, and verifies UTF-8/generated-artifact hygiene.

The recent design work has been reviewed at three connected levels:

| Review | What it examines |
| --- | --- |
| [Task continuity](research/runtime-design-optimization/03-multi-step-task-continuity.md) | Carrying requested outputs, selected state, and material uncertainty across steps and changes |
| [Retrieved context](research/runtime-design-optimization/04-retrieved-handbook-context.md) | Keeping scope, qualifications, and necessary dependencies inside usable handbook excerpts |
| [Index and work chains](research/runtime-design-optimization/05-index-discovery-and-work-chains.md) | Finding relevant guidance within eight representative request-to-output chains |

These are design reviews and static checks. They do not establish improved model behavior or marketing outcomes. Harness tests verify evaluation infrastructure; they are not live behavioral trials of the current design.

The current design has not yet received live behavioral evaluation. No prior skill version's pass/fail result is used to assess it.

If the skill makes a poor decision, overcomplicates a simple task, misses supplied evidence, reopens resolved state, chooses the wrong knowledge path, behaves inconsistently, or produces an unexpectedly useful result, [open a behavior report](https://github.com/quocbao201104/marketing-practitioner/issues/new?template=behavior-report.yml). Include sanitized context, expected vs observed behavior, model/runtime, skill version, and whether it reproduces.

## Status and scope

Current release: **v1.7.0 — Planning, Reports, and Visual Identity**.

The package covers seven marketing jobs with specialist guidance for content, commerce, commercial design, landing pages, email, search/discovery, paid media, brand identity, and scoped localization. See [CHANGELOG.md](CHANGELOG.md) for release history.

The runtime design is still being refined. Its seven jobs, logical knowledge IDs, decision ownership, and source/claim boundaries are compatibility-sensitive. Static review records document the scope and limits of individual changes; they are not quality benchmarks across models or hosts.

The skill supports marketing decisions and execution. Product-roadmap authority, finance, legal advice, CRM operations, and private platform mechanics remain outside its ownership.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Change the smallest surface that can correct a demonstrated problem. Do not add a platform, primitive, chapter, or country pack merely for coverage completeness.

For local/cultural/market adaptation contributions, start with the [scoped local-adaptation contract](skills/marketing-practitioner/adaptations/README.md): local evidence alone is not enough; the contribution must change an existing open decision through a bounded local-specific mechanism.

## Attribution

The repository synthesizes marketing research, methodological literature, current provider documentation, information-retrieval and recommender research, pricing/commercial-design research, usability research, local linguistic/applied-linguistic evidence, and practical writing methods.

See [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md), the [bibliography](skills/marketing-practitioner/references/bibliography.md), and scoped [evidence references](skills/marketing-practitioner/references/).

## License

[MIT](LICENSE).

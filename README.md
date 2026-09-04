<div align="center">

<img src="assets/marketing-practitioner-banner.webp" alt="Marketing Practitioner banner" width="100%">

# Marketing Practitioner

**A decision-first marketing skill that knows what to resolve — and what to leave alone.**

[![Version: v1.1.0](https://img.shields.io/badge/version-v1.1.0-0a7.svg)](#status)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Language: English](https://img.shields.io/badge/language-English-4c1.svg)](#)
[![Format: Agent Skill](https://img.shields.io/badge/format-Agent%20Skill-6f42c1.svg)](skills/marketing-practitioner/SKILL.md)
[![skills.sh](https://skills.sh/b/quocbao201104/marketing-practitioner)](https://skills.sh/quocbao201104/marketing-practitioner)

</div>

---

Ordinary marketing prompts, templates, and skill collections add more advice: frameworks, section formulas, platform tips. Agents already write fluently. The failure this skill is built against is inventing product facts, treating eight interviews as a market, rewriting a page because CPA moved, or loading a TikTok playbook because the prompt said “TikTok.”

The skill is built to prevent that class of error. It classifies the current job, keeps already-settled decisions settled, and loads only the governed knowledge that can change what is still open.

## Quick start

```bash
npx skills add quocbao201104/marketing-practitioner
```

Then tell the agent:

1. what you need done **now**;
2. the facts, evidence, and already-approved decisions you have;
3. where the result will be used, if that changes the answer.

You do not need internal terms. “Help me decide which customer group to focus on” is enough; you do not have to say ICP. The [Task Specification Guide](TASK-SPECIFICATION-GUIDE.md) can compile rough notes into a smaller spec without inventing missing facts. It is optional.

```text
Use Marketing Practitioner.
The positioning below is approved. Do not reopen it.
Write a LinkedIn post for people who already follow the company.
Do not add product claims that are not in the facts.
```

Clone if you want the full repository:

```bash
git clone https://github.com/quocbao201104/marketing-practitioner.git
```

The governing file is [`skills/marketing-practitioner/SKILL.md`](skills/marketing-practitioner/SKILL.md).

## Host / IDE compatibility

Marketing Practitioner is portable, but runtime behavior is not identical across hosts. The host decides whether the skill is discovered and loaded, how much working context survives, whether memory persists across sessions, and which files, tools, or integrations the agent can use.

| Host | Durable context to use |
| --- | --- |
| **Claude Code** | `CLAUDE.md` / project memory and resumable sessions |
| **ChatGPT** | Projects, project files/instructions, and project memory |
| **Cursor** | Project Rules or `AGENTS.md`; keep reusable context in version-controlled rules |
| **Codex** | `AGENTS.md` / repository instructions and checked-in project state |

Exact behavior depends on the host version, settings, plan, and runtime. Use the host's native persistence features when available, but do not rely on chat history alone for important facts, constraints, approved decisions, or evidence boundaries. Keep those explicit in the current task context or project files.

Host memory improves continuity; it does not replace the skill contract. [`SKILL.md`](skills/marketing-practitioner/SKILL.md) and the governed repository knowledge remain the portable source of behavior.

## What it is for

Use it when an agent has to **decide, diagnose, research, adapt, test, learn, or write** in a marketing context, and the answer should stay inside the evidence you actually have.

That includes synthesizing customer material, choosing who to prioritize, positioning against a real alternative, designing packaging and terms, writing or critiquing copy, compiling a landing page or email, adapting to a platform, representing a commerce listing, interpreting search or paid delivery, localizing an already-resolved strategy, applying scoped local-adaptation knowledge when a local mechanism changes the realization of an open decision, or retaining what a result did and did not prove.

Those are separate owners, not a funnel the skill runs every time. A caption with an approved message stays a writing job. A price that is already `$29` stays frozen while the page is written. Paying a creator to publish is not automatically paid media. A CPA rise after a bidding change starts as diagnosis, not as a creative rewrite.

The skill is built to keep distinctions that otherwise collapse in fluent marketing output:

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

It has no authority to invent product, financial, legal, operational, sales, platform, or customer facts. Current provider rules are just-in-time dependencies, not growth laws stored in the repo.

## How that is implemented

The installable contract is [`skills/marketing-practitioner/SKILL.md`](skills/marketing-practitioner/SKILL.md). For each task it:

1. Identifies the current job (`WRITE`, `DECIDE`, `DIAGNOSE`, `RESEARCH / UNDERSTAND`, `ADAPT`, `TEST`, or `LEARN`). A topic, artifact type, or platform name is not a job.
2. Freezes resolved state. Audience, positioning, message, offer facts, and claim boundaries stay inputs unless they are contradictory, stale, or insufficient for this job.
3. Names the open decision.
4. Uses only evidence that can change that decision.
5. Selects knowledge by dependency, not by noun.
6. Loads the smallest indexed section that can improve the next choice.
7. Passes forward only the conclusions, constraints, proof, and uncertainty the next step needs.
8. Returns the minimum output that completes the job, then checks it against that job.

Large knowledge is addressed by logical IDs in [`routing-index.json`](skills/marketing-practitioner/routing-index.json). Headings and file paths are implementation details. When the host can run helpers, [`get-knowledge.py`](skills/marketing-practitioner/scripts/get-knowledge.py) resolves one route or one evidence source without reading the rest of the ledger:

```bash
python skills/marketing-practitioner/scripts/get-knowledge.py email.send-decision
python skills/marketing-practitioner/scripts/get-knowledge.py adapt-localization.relationship-realization
python skills/marketing-practitioner/scripts/get-knowledge.py --source PM01
```

If helper execution is unavailable, the same index is still the address table: read the smallest feasible section, or degrade to the smallest target file, rather than abandoning the job or loading a whole chapter.

The current index validates at **252 routes / 214 evidence sources**. Evidence files state what a source **supports** and **does not support**. That bound is how claim control is implemented.

Specialist layers (commercial design, landing pages, email, discovery, paid media, commerce, named platforms) are added only when a concrete decision-relevant gap survives local repair. Shared architecture expands only when the existing grammar cannot represent the decision without material distortion. Research under [`research/`](research/) keeps theory freezes and rejected expansions out of the runtime until they survive that bar. A controller 75% smaller than the installed one was evaluated on the same frozen cases and **not promoted**, because unverified skill activation rose from 3/24 to 7/24. See the [challenger report](evals/behavioral/reports/compact-challenger-v1.md).

Local adaptation follows the same discipline. [`adaptations/`](skills/marketing-practitioner/adaptations/) contains scoped evidence that can specialize an **already-open decision owned elsewhere**; it is not a country-profile layer, cultural encyclopedia, or precedence engine. The first canonical contribution, `VN-LANG-REL-01`, specializes Vietnamese relationship-sensitive language realization through `adapt-localization.relationship-realization` without inferring the underlying relationship, turning age into an address lookup table, or treating Vietnam as an activation key. See the [local-adaptation contribution contract](skills/marketing-practitioner/adaptations/README.md) and [Vietnamese reference unit](skills/marketing-practitioner/adaptations/localization.md).

The [handbook map](skills/marketing-practitioner/handbook/README.md) and [platform modules](skills/marketing-practitioner/platforms/README.md) are for navigation when a decision actually needs them, not a reading list.

## Repository map

```text
skills/marketing-practitioner/
  SKILL.md                  governing runtime controller
  agents/openai.yaml        optional UI metadata and explicit invocation starter
  routing-index.json        logical knowledge address table
  handbook/                 governed practitioner knowledge
  adaptations/              scoped local decision specializations
  platforms/                scoped social and commerce modules
  references/               evidence ledgers and bibliography
  scripts/                  deterministic routing checks

research/                   theory lineage and rejected hypotheses
evals/                      adversarial cases, smokes, and behavioral harness
scripts/verify.ps1          sole local/CI verification entrypoint
```

## Verification and reports

The local and CI gate is:

```powershell
.\scripts\verify.ps1
```

It validates the package with the repository validator and the installed Codex validator when discoverable, checks 58 routing mechanics and **252 routes / 214 evidence sources**, runs the Pressure Discovery and behavioral harness tests, and verifies UTF-8/generated-artifact hygiene.

A frozen 48-run behavioral pilot (12 cases, no-skill baseline vs current skill, `gpt-5.6-terra`, medium reasoning) produced eight both-pass pairs, three operationally invalid pairs, and one unresolved pair. It did **not** show a paired quality advantage. Review was condition-blind but not independently human-adjudicated. That is repository decision evidence, not a benchmark. See the [pilot report](evals/behavioral/reports/current-skill-pilot-v1.md).

If the skill makes a poor decision, overcomplicates a simple task, misses supplied evidence, reopens a resolved decision, chooses the wrong knowledge path, behaves inconsistently, or produces an unexpectedly useful result, [open a behavior report](https://github.com/quocbao201104/marketing-practitioner/issues/new?template=behavior-report.yml). Include the task, sanitized context, expected vs observed behavior, model/runtime, skill version, and whether it reproduces. Do not include confidential customer, company, credential, or personal data.

## Status

Current release: **v1.1.0 — Scoped Local Adaptation**.

v1.0.0 remains the stable core compatibility baseline: the seven jobs, resolved-state behavior, logical knowledge IDs, owner boundaries, and source/claim discipline remain compatibility-sensitive. v1.1.0 adds a bounded extension contract for community-maintained local adaptation knowledge plus the first canonical Vietnamese relationship-realization unit. It does **not** add a country/locale pack, a cultural-precedence hierarchy, a scope-scoring engine, a new controller job, or a new decision owner.

The first reference implementation was independently reviewed at a frozen implementation head and received `PASS_WITH_LOCAL_REPAIRS`; the two bounded repairs were implemented. A post-repair independent re-review was not performed, so the reference unit remains explicitly `review_state: provisional` rather than overstating review provenance.

Stable does not mean complete. Provider-controlled facts remain time-sensitive. Local market evidence remains scoped evidence rather than a durable rule unless it demonstrates a local-specific mechanism that materially changes an open decision and is not already handled by the existing owner.

This is not a prompt pack, a conversion-formula library, or a generic agent framework. It does not own product roadmap, finance, legal advice, CRM, or back-office automation. It does not reverse-engineer private ranking or ad-delivery systems from anecdotes, and it does not turn one provider’s current rule into a universal law.

The skill cannot make a host load it. If the runtime never activates the skill, you get ordinary model behavior.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Change the smallest surface that can correct a demonstrated problem. Do not add a platform, primitive, chapter, or country pack for coverage completeness. For local/cultural/market adaptation contributions, start with the [scoped local-adaptation contract](skills/marketing-practitioner/adaptations/README.md): local evidence alone is not enough; the contribution must change an existing open decision through a bounded local-specific mechanism.

## Attribution

The repository synthesizes marketing research, methodological literature, current provider documentation, information-retrieval and recommender research, pricing/commercial-design research, usability research, local linguistic/applied-linguistic evidence, and practical writing methods. See [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md), the [bibliography](skills/marketing-practitioner/references/bibliography.md), and scoped [evidence references](skills/marketing-practitioner/references/).

## License

[MIT](LICENSE).
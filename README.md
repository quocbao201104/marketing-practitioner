<div align="center">

<img src="assets/marketing-practitioner-banner.webp" alt="Marketing Practitioner banner" width="100%">

# Marketing Practitioner

**Evidence-informed marketing decisions and execution for AI agents.**

*Learn the market before writing the copy.*

[![Version: v0.9.0](https://img.shields.io/badge/version-v0.9.0-0a7.svg)](#status)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Language: English](https://img.shields.io/badge/language-English-4c1.svg)](#)
[![Format: Agent Skill](https://img.shields.io/badge/format-Agent%20Skill-6f42c1.svg)](skills/marketing-practitioner/SKILL.md)
[![skills.sh](https://skills.sh/b/quocbao201104/marketing-practitioner-skill)](https://skills.sh/quocbao201104/marketing-practitioner-skill)

</div>

---

Marketing Practitioner helps an agent turn market evidence into bounded decisions across research, segmentation, positioning, commercial design, messaging, landing pages, email, social content, commerce, search/discovery, paid media, diagnosis, experiments, localization, and learning.

It is not a prompt pack or growth-hack library. The runtime starts from the current job, freezes decisions that are already resolved, loads deeper knowledge only when it can change the open decision, and returns the minimum useful output.

## Quick start

```bash
npx skills add quocbao201104/marketing-practitioner-skill
```

Then describe:

1. what you are trying to do;
2. what facts, evidence, or decisions you already have;
3. where the result will be used, if that changes the answer.

You do not need to know terms such as ICP, JTBD, attribution, retrieval, or willingness to pay. The [Task Specification Guide](TASK-SPECIFICATION-GUIDE.md) can compile rough notes into the smallest sufficient task specification without inventing missing facts.

```text
Read TASK-SPECIFICATION-GUIDE.md.
Use what I already provided to compile the smallest sufficient task specification.
Preserve resolved decisions and do not invent missing facts or constraints.
Then execute the task with Marketing Practitioner.
```

## Representative tasks

- synthesize interviews, reviews, surveys, support records, and sales notes without turning recurrence into prevalence;
- choose a segment, relevant alternative, positioning, value, proof, or trade-off;
- decide packaging, pricing metric, commitment, eligibility, modifiers, or commercial transitions;
- build or critique message hierarchy, claims, proof, copy, landing-page architecture, and email communication;
- adapt resolved content to a platform without reopening strategy;
- interpret commerce, search/discovery, social, email, or paid-media state without importing platform folklore;
- diagnose a performance change before rewriting creative;
- design or interpret an experiment and preserve reusable learning.

The detailed chapter and platform map lives in the [handbook navigation](skills/marketing-practitioner/handbook/README.md). Social and commerce provider navigation is under [platforms](skills/marketing-practitioner/platforms/README.md).

## Reasoning model

The controller uses seven jobs:

```text
WRITE · DECIDE · DIAGNOSE · RESEARCH / UNDERSTAND · ADAPT · TEST · LEARN
```

For each task it:

```text
identify the current job
→ freeze resolved state
→ name the open decision
→ identify decision-changing evidence
→ select owners by dependency
→ load the smallest useful knowledge route
→ pass forward only material state
→ produce and validate the minimum sufficient output
```

Large knowledge surfaces are addressable through [routing-index.json](skills/marketing-practitioner/routing-index.json) and [get-knowledge.py](skills/marketing-practitioner/scripts/get-knowledge.py). File paths and headings are implementation details; logical route IDs are the stable interface.

## Evidence discipline

The skill is designed to preserve distinctions that commonly collapse in marketing work:

```text
observation ≠ interpretation ≠ hypothesis ≠ decision
qualitative recurrence ≠ population prevalence
association / attribution ≠ causality / incrementality
eligible ≠ delivered ≠ attended to
interaction ≠ intent or preference
reported ≠ optimization-eligible
displayed commercial state ≠ universal authoritative state
```

It never has authority to invent product, finance, legal, operational, sales, platform, or customer facts. Current provider rules remain just-in-time dependencies rather than permanent universal laws.

## Repository map

```text
skills/marketing-practitioner/
  SKILL.md                  governing runtime controller
  agents/openai.yaml        optional UI metadata and explicit invocation starter
  routing-index.json        logical knowledge address table
  handbook/                 governed practitioner knowledge
  platforms/                scoped social and commerce modules
  references/               evidence ledgers and bibliography
  scripts/                  deterministic routing checks

research/                   theory lineage and rejected hypotheses
evals/                      adversarial cases, smokes, and behavioral harness
scripts/verify.ps1          sole local/CI verification entrypoint
```

Deep research stays outside the installable runtime unless it survives scope, evidence, and decision-value review.

## Verification and behavioral evidence

Run the same gate used by CI:

```powershell
.\scripts\verify.ps1
```

It validates the package with the repository validator and the installed Codex validator when discoverable, checks 58 routing mechanics and 249 routes/203 evidence sources, runs the Pressure Discovery and behavioral harness tests, and verifies UTF-8/generated-artifact hygiene.

The frozen 48-run behavioral pilot used 12 cases, two arms, two repetitions, `gpt-5.6-terra`, and `medium` reasoning. It produced eight `both_pass` pairs, three operationally invalid pairs, and one unresolved pair; it showed no baseline-only or skill-only pass. The review was condition-blind but not independently human-adjudicated, so it is repository decision evidence—not a benchmark or universal reliability claim. See the [pilot report](evals/behavioral/reports/current-skill-pilot-v1.md).

A controller challenger reduced initial controller words by 75% but increased activation-unverified runs from 3/24 to 7/24, so it was [rejected and not promoted](evals/behavioral/reports/compact-challenger-v1.md).

## Status

Current release: **v0.9.0 — Paid Media Architecture**.

The installable skill passes current package validation and deterministic repository checks. Its knowledge includes bounded Commercial Design, Landing-Page, Email, Search & Discovery, Paid Media, social/content-environment, and commerce/product-discovery layers.

The project does not claim complete knowledge of private ranking, retrieval, or ad-delivery systems; universal platform, pricing, landing-page, email, or attribution rules; legal/provider compliance for every context; benchmark-grade quality; or universal runtime reliability. Improvement should follow concrete failures and evidence, not architecture growth for its own sake.

## Installation and manual use

```bash
npx skills add quocbao201104/marketing-practitioner-skill
git clone https://github.com/quocbao201104/marketing-practitioner-skill.git
```

The governing instructions are [skills/marketing-practitioner/SKILL.md](skills/marketing-practitioner/SKILL.md).

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Contributions should preserve UTF-8, source fidelity, decision scope, resolved-state behavior, fast paths, owner boundaries, and the distinction between observation, attribution, and causality. New top-level reasoning capabilities require a demonstrated decision-relevant gap before implementation.

## Attribution

The repository synthesizes marketing research, methodological literature, current provider documentation, information-retrieval and recommender research, pricing/commercial-design research, usability research, and practical writing methods. See [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md), the [bibliography](skills/marketing-practitioner/references/bibliography.md), and scoped [evidence references](skills/marketing-practitioner/references/).

## License

MIT. See [LICENSE](LICENSE).

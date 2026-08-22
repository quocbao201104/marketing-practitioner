# Runtime Architecture Audit — v0.1.4 Candidate

Status: baseline audit only. Do not change `SKILL.md` until the baseline cases below are run against v0.1.3.

## Why this audit exists

The repository began as a learning/reference system and later acquired an executable Agent Skill layer. The knowledge base is intentionally broad; the runtime layer should not necessarily load or foreground all of that knowledge on every task.

The current audit asks whether the active `SKILL.md` behaves like a lean procedural controller or like a compressed handbook whose individually reasonable instructions can interfere with one another.

External design guidance supports testing this explicitly:

- Agent Skills load the full `SKILL.md` once a skill activates, while referenced resources can be loaded on demand.
- Agent Skills best practices warn that overly comprehensive skills can trigger irrelevant paths and recommend progressive disclosure with explicit conditions for loading supporting files.
- Anthropic recommends starting from observed evaluation failures, keeping the core lean, and watching for overreliance on particular context.

References:
- https://agentskills.io/specification
- https://agentskills.io/skill-creation/best-practices
- https://agentskills.io/skill-creation/evaluating-skills
- https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills
- https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents

## Frozen baseline

Run these cases against public v0.1.3 without changing the prompt, source packs, or model between baseline and candidate comparisons.

Prefer one model for the entire first pass. Open a fresh chat for each case.

Common header:

```text
Use the installed marketing-practitioner skill exactly as written and follow its resource routing.

Use only the supplied source material.
Do not browse the web or invent facts.

Return:

STRATEGY
- Maximum 5 concise bullets.

FINAL
- Final publishable output only.
```

---

# H1 — Counterevidence role leakage

Question: does an always-on requirement to retain material contradictions make contradictory evidence appear in audience-facing copy even when it should only constrain the claim?

## H1-A — Casual announcement

```text
SOURCE MATERIAL

Product: Patchboard

Facts:
- Patchboard is an open-source visual debugger for local AI-agent workflows.
- It shows run steps, tool calls, timestamps, and completion status.
- Python only.
- Runs locally.
- MIT licensed.
- Repository: https://github.com/example/patchboard

Research notes:
- In five exploratory developer interviews, three participants said timeline views made debugging easier to follow.
- Two participants said they preferred raw logs and did not find a visual timeline useful.
- This interview set does not establish population prevalence.
- Do not claim developers generally prefer visual debugging.
- Do not claim Patchboard improves debugging speed.
- Do not invent adoption or performance evidence.

TASK

Reader:
Developer friends and acquaintances on a personal Facebook feed.
They already understand AI-agent tooling and can inspect the repository themselves.

Goal:
Casually share Patchboard and make relevant people curious enough to inspect the repo.

Task:
Write the Facebook post.
```

Expected role of the contradictory interview evidence: `CONSTRAIN_ONLY` unless the copy makes a claim that would otherwise be misleading.

PASS:
- no claim that developers generally prefer visual timelines;
- no need to narrate the 3-versus-2 interview split in the final post;
- product mechanism remains clear.

FAIL signature:
- final copy surfaces the contradiction merely because it exists in the source or because counterevidence must be "retained".

## H1-B — Research recommendation

Use the same source material, but replace TASK with:

```text
Reader:
The product team deciding whether to prioritize the visual timeline as Patchboard's primary differentiator.

Goal:
Give a bounded recommendation based on the available exploratory evidence.

Task:
Write a concise internal recommendation.
```

Expected role: `MUST_SAY`.

PASS:
- preserves the split evidence;
- does not turn 3/5 into market prevalence;
- recommendation remains provisional.

This pair checks whether the same contradiction can remain internal in communication but surface in a decision where it is material.

---

# H2 — Front-loaded irrelevant-principle interference

Question: do always-on principles for causality, experimentation, learning, localization, ethics, and human-writing distort a simple task that does not require those modes?

## H2 — Narrow product microcopy

```text
SOURCE MATERIAL

Product: QueueLight

Facts:
- QueueLight processes uploaded CSV files asynchronously.
- After upload, a file enters a processing queue.
- The user can safely leave the page while processing continues.
- When processing finishes, the result appears in the user's Recent jobs list.
- Processing time varies with file size and queue load.
- There is no reliable completion-time estimate available before processing begins.

Interface state:
- The file has just been accepted successfully.
- The user is deciding whether they need to keep this page open.

TASK

Reader:
A user who has just uploaded a CSV file and is waiting on the processing screen.

Goal:
Tell them what is happening and whether they need to stay on the page.

Task:
Write the confirmation microcopy. Maximum 35 words.
```

PASS:
- tells the user the file is queued/processing;
- clearly says they can leave;
- says where the result will appear;
- does not add methodology, generic uncertainty language, experiment framing, ethics framing, or marketing prose.

FAIL signature:
- unnecessary caveat proliferation;
- explaining why estimates are uncertain beyond what the user needs;
- promotional or analytical material entering a task-execution message.

Interpretation note: H2 cannot be fully established from one baseline run. If baseline passes, compare v0.1.3 with a lean-core candidate later using the same prompt and evaluate unnecessary reasoning/output, not only final correctness.

---

# H3 — Multi-mode transition integrity

Question: when a task spans diagnosis and communication, does the skill preserve stage boundaries, or does the copy-oriented default sequence cause premature messaging changes?

## H3 — Diagnose first, communicate only what is established

```text
SOURCE MATERIAL

Product: FormPilot

Observed metrics:
- Trial signup conversion fell from 8.2% to 6.1% week over week.
- Total landing-page sessions were similar across the two weeks.
- Mobile traffic share increased from 41% to 63%.
- Desktop signup conversion was approximately unchanged.
- Mobile signup conversion declined materially.
- A new mobile form layout shipped at the start of the second week.
- Paid-search campaign mix also changed during the second week.
- No controlled experiment was run.
- No instrumentation audit has yet been completed.
- No evidence establishes the new mobile form as the cause of the decline.

Current landing-page headline:
"Build forms your team can ship in minutes."

TASK

Reader:
The growth/product team.

Goal:
Decide what to investigate next and whether the landing-page message should be changed now.

Task:
1. Diagnose the conversion decline using the supplied evidence.
2. Recommend the next discriminating check.
3. State whether the headline should be changed now.
4. Only if the evidence supports changing it now, provide replacement copy.
```

PASS:
- localizes the problem to mobile before storytelling;
- treats the mobile form release and paid-search mix as competing explanations;
- recognizes missing instrumentation audit;
- recommends a discriminating check;
- retains a no-change option for the headline;
- does not manufacture replacement copy merely because copywriting is part of the skill.

FAIL signature:
- jumps from correlation to causal story;
- rewrites the headline without evidence that messaging is the problem;
- follows the global evidence→positioning→message→copy path when the actual job is diagnosis.

---

# Candidate architecture hypothesis

Do not implement until baseline evidence justifies it.

If the failures appear, the v0.1.4 candidate should move from one global pipeline toward a lean controller:

```text
DECISION / JOB TO BE DONE
        ↓
RELEVANT EVIDENCE
        ↓
CURRENT UNDERSTANDING
        ↓
SELECT OPERATING PATH
   ├─ research / synthesis
   ├─ segment / target
   ├─ positioning
   ├─ message / copy
   ├─ diagnosis / experiment
   ├─ localization
   └─ postmortem / learning
        ↓
LOAD ONLY PATH-RELEVANT RESOURCES
        ↓
ACT / COMMUNICATE
        ↓
SCOPED LEARNING WHEN MATERIAL
```

Universal always-on rules should be limited to invariants that genuinely govern nearly every path, such as source fidelity, no fabrication, scope discipline, decision orientation, and material ethical boundaries.

Detailed causal, human-writing, localization, experimentation, and review guidance should be loaded at the earliest decision point where it becomes materially relevant — not before and not after.

The v0.1.3 audience-facing content-selection gate is already regression-tested and should be preserved unless new evidence shows a conflict.

## Decision rule after baseline

- If H1 fails: repair output-role semantics for counterevidence before broader refactor.
- If H2 shows interference or lean-core ablation improves it without regressions: move non-universal principles out of always-on core.
- If H3 fails: replace the single default pipeline with explicit path selection before mode-specific work.
- If all pass: do not refactor merely for elegance; proceed to an ablation test of lean core versus current core before changing public behavior.

# Core Task Decisions and Completion Review

Date: 2026-09-08. Follows the bounded priority selected in [synthesis 44](44-audit-coverage-and-next-priorities.md).

Status: source and design review completed. Two minor guide wording findings; no demonstrated need to change the runtime controller in this slice. Proposed corrections remain unapplied.

## Scope and conclusion

Reviewed the canonical [task guide](../../skills/marketing-practitioner/TASK-SPECIFICATION-GUIDE.md), its [evidence ledger](../../skills/marketing-practitioner/references/task-specification-evidence.md), the uncertainty, continuity, and completion rules in [SKILL.md](../../skills/marketing-practitioner/SKILL.md), and the introduction and section 10 of [quality rubrics](../../skills/marketing-practitioner/frameworks/quality-rubrics.md#10-completion-and-decision-usefulness). The root task guide is only a pointer to the packaged canonical guide.

The current design distinguishes a consequential missing input from an empty framework field, permits useful bounded work, and preserves requested outputs across dependencies. The reviewed research gives reasons for those choices, but does not validate the complete controller, its stopping judgment, or long-session execution. The ledger already explicitly limits its purpose to the user-facing guide; it must not acquire a stronger role by association.

The two findings concern how the guide presents its research basis. They do not demonstrate that the conditional template or current controller is wrong. No agent trials, old pilot results, account behavior, or commercial outcomes are used as a baseline.

## Primary-source access and selected findings

All eight papers below were accessed on the review date. These are selected substantive passages, not full-paper replication or verification of every appendix. Page references use printed pages for ACL/PMLR/TACL and PDF pages for ICLR.

| Source | Material inspected and what it supports | Transfer limit |
|---|---|---|
| TS01: [Yang et al., prompt underspecification](https://aclanthology.org/2026.findings-acl.441.pdf) | Section 3 setup and results, pp. 9074-9077; section 5 and limitations, pp. 9079-9080. Three main tasks include code explanation, travel advice, and product descriptions; 60 curated requirements use human-checked automated validators. Evaluated GPT-4o, Llama-3-family, and o3-mini settings show both omission fragility and interference from adding requirements. | Application requirements are not a comparison of this repository's user templates. Curation, synthetic prompts, models, and validators bound the result; no universal minimal specification or optimal field count follows. |
| TS03: [Hua et al., prompt-sensitivity counterevidence](https://aclanthology.org/2025.emnlp-main.1006.pdf) | Sections 1-4 and limitations, pp. 19889-19894. Seven evaluated models, six benchmarks, and 12 templates compare heuristic scoring with semantic judging; selected human checks support an evaluation-artifact explanation for some sensitivity. | Does not eliminate all prompt sensitivity, certify every LLM judge, or make explicit output-format requirements optional. Semantic equivalence and satisfying an actual delivery constraint are different questions. |
| TS04: [Shi et al., irrelevant context](https://proceedings.mlr.press/v202/shi23a/shi23a.pdf) | Introduction, dataset construction/metrics in section 3, and conclusion. GSM-IC adds constructed irrelevant sentences to arithmetic problems while preserving their solutions; tested prompting approaches do not remove all distraction effects. | Controlled arithmetic distractors justify caution about irrelevant inputs. They do not show that a shorter marketing evidence packet is always sufficient, or identify a universal retrieval budget. |
| TS05: [Liu et al., Lost in the Middle](https://aclanthology.org/2024.tacl-1.9.pdf) | Selected pp. 158-159 and 164-165: controlled multi-document QA, key-value retrieval, and architecture/query-position comparisons. Position effects and mitigation differ across tasks and models; query-aware placement helps key-value retrieval much more than multi-document QA. | Context capacity does not assure useful access. This does not validate this skill's continuity record, prove that summaries retain every material fact, or require repeated instructions at fixed positions. |
| TS06: [Du et al., context length despite retrieval](https://aclanthology.org/2025.findings-emnlp.1264.pdf) | Sections 3-4 and limitations, pp. 23283-23289. Synthetic extensions of math, QA, coding, and variable-tracking tasks separate evidence from distractors and examine whitespace/masking controls. Five evaluated models show setting-dependent effects, including exceptions in closed-model whitespace conditions. | Perfect evidence retrieval is an experimental condition, not a property established for this loader. The authors limit their compression method to successful retrieval. The evidence supports neither deleting necessary context nor assuming every increase in length harms every model. |
| TS07: [Zhang, Knox and Choi, future conversation turns](https://proceedings.iclr.cc/paper_files/paper/2025/file/97e2df4bb8b2f1913657344a693166a2-Paper-Conference.pdf) | Sections 3-4 and 7, PDF pp. 3-6 and 10. Preference training uses simulated clarifying replies and downstream QA correctness, with direct answers favored on ties. Base Llama2-7b, Gemma-7b, and Llama3-8b are evaluated with NQ-Open/AmbigQA. | A training/evaluation result for one- or two-turn interactions, not proof that adding a prose instruction produces the same behavior. Other dialogue actions and arbitrary follow-up chains are outside its tested policy. |
| TS08: [Zhang and Choi, Clarify When Necessary](https://aclanthology.org/2025.findings-naacl.306.pdf) | Sections 2-4 and limitations, pp. 5542-5546 and 5549. The framework separates uncertainty likely to benefit from clarification from other uncertainty. QA, MT, and NLI use annotated interpretations and oracle-generated clarification pairs; interaction budgets and intent distributions matter. | The oracle has access to interpretations unavailable to an ordinary agent. Question generation and arbitrary-length interaction remain outside scope. This supports a conditional clarification principle, not a universal probability threshold, permission rule, or estimate of when marketing research should stop. |
| TS09: [Zhang et al., CLAMBER](https://aclanthology.org/2024.acl-long.578.pdf) | Selected dataset/setup and ambiguity-identification results in sections 3-5, pp. 10749-10752. Vicuna/Llama2/ChatGPT-era evaluations show that few-shot and chain-of-thought prompts do not reliably resolve ambiguity identification. | Historical evaluated systems and benchmark labels do not measure this host's September 2026 agent capability. Ambiguity classification is also not the same objective as useful completion of an open marketing task. |

TS05's PDF opened through the web tool, but subsequent bounded reads returned an internal error. The same official PDF was then downloaded to a temporary directory and selected text extracted locally. No repository source copy was added. TS06's heading search also missed; direct section reads recovered the relevant text.

TS02, TS10, and current provider pages TS11-TS13 were not independently revalidated in this bounded review. Their local records were read, but this report does not renew their access dates or certify the guide's entire examples/provider discussion. No new source ID or historical inventory rewrite is needed.

## TS-A1: distinguish the chosen guide structure from a research result

**Location:** canonical task guide, section 2 opening paragraph.

The paragraph says the research supports the particular smaller model of a required core plus conditional qualifiers, immediately before the six-part table. This can be read as empirical support for that organization and its superiority to the earlier grammar. The paper supports the underlying trade-off; the exact table and comparison are this project's design judgment. Existing later caveats reduce, but do not remove, the ambiguity at this claim.

**Decision consequence:** a maintainer deciding whether to change the template could treat the present field arrangement as empirically established rather than assess its fit to the user's job.

**Smallest correction:** replace the historical comparison/research attribution with a short statement that the guide organizes the job and conditional qualifiers this way as a practical design choice informed by the research. Retain the table and its existing instruction to omit unnecessary fields. Do not invent a template comparison result or add a new template experiment.

## TS-A2: date-bound the ambiguity-capability statement

**Location:** canonical task guide, section 8 opening paragraph, the sentence citing TS09.

The phrase `Current models` makes the finding move with the date of reading. The cited study measures an earlier set of systems. It supports retaining a safeguard against missed ambiguity, but does not establish the capability of every newer deployed model.

**Decision consequence:** readers assessing how much to rely on today's agent could mistake a historical benchmark for a current capability assessment.

**Smallest correction:** describe the evaluated models or the study's observed difficulty, retaining the conditional clarification guidance. No fresh universal capability claim or new model benchmark is required. The ledger's existing wording is already more restrained; selected method/limit locators could be added there for traceability without replacing its scope.

Both findings are minor evidence-presentation corrections, not observed execution failures. No implementation or closure count is added by this report.

## Mapping evidence to the controller

| Decision | Existing design inspected | Assessment |
|---|---|---|
| Proceed | Materiality definition, reversible execution choices, narrow-task fast path. | A coherent sufficiency policy. The studies do not prove the agent will recognize every consequential omission. No missing rule was demonstrated here. |
| Retrieve | Scope-limited external verification, counterevidence, bounded first inspection during exploration, expansion when a read has a purpose. | Preserves the distinction between selective reading and deciding relevance before seeing evidence. Retrieval success alone is explicitly insufficient for task completion. No fixed token cap is justified. |
| Clarify or bound | Ask only for material unresolved differences; recover from context, continue independent work, and supply useful supported portions. | More complete than treating uncertainty as an automatic question. User-owned authorization remains an instruction boundary, not a preference inferred from a benchmark or likelihood. |
| Stop investigating | Expected decision relevance versus cost; requested research ends with a supported bounded account or explicit evidence limit. | A project decision heuristic, not a calibrated optimal-stopping algorithm. No retrieved paper establishes an exact threshold. Its scope and evidence-limit clauses prevent claiming exhaustiveness, but practical judgment remains unvalidated. |
| Complete the work | Job-specific functions, all active outputs, partial-blockage disclosure, and section 10's reader/decision usefulness checks. | These are inspectable acceptance criteria rather than an empirical scale. The rubric already says so and requires only relevant criteria. No universal checklist or outcome guarantee needs to be removed. |
| Resume or revise | Retained return points, adopted choices versus assumptions, changed-input reconciliation, affected-artifact revision, and host-dependent records. | Plausible design safeguards. Short clarification experiments and context-position studies do not demonstrate long-session reliability. That remains an explicit evidence gap rather than a reason to add more state fields speculatively. |

The missing empirical guarantee is not itself a controller defect. The controller must express what the agent should do; a study would be needed to support a claim that a particular implementation reliably does it.

## Contrasting requests used to inspect the design

These are constructed counterexamples for reading the specification, not model runs or a pass-rate dataset.

| Request or changed condition | Decision that must be preserved | Relevant current protection |
|---|---|---|
| Shorten supplied approved copy; no new strategic choice is needed. | Produce the edited copy without requiring audience/template fields already inferable or irrelevant. | Fast path, preserved state, WRITE completion. |
| Adapt an asset for an unspecified destination where the two plausible destinations need different artifacts; also summarize the supplied interviews. | Resolve the destination through available context or a minimal question while completing the independent synthesis. | Material clarification, independent work, retention of all requested outputs. |
| A product capability is missing but research is allowed; a separate account permission is also absent. | Investigate the factual specification within scope; do not use external evidence to invent permission. Bound any still-unsupported artifact. | Retrieve versus user-owned input, source fidelity, supported partial result. |
| Explore an unfamiliar evidence packet without a predetermined commercial decision. | Inspect enough to discover relevant questions; preserve contradictions even if they weaken the initial explanation. | Bounded first inspection, counterevidence, RESEARCH completion. |
| A delegated choice is made, then a changed product variant undermines its proof while several assets remain pending. | Revisit affected claims/assets, preserve unaffected outputs, and avoid treating selection as verification. | Delegated selection, continuity and dependency revision, per-output completion. |
| Research reaches a real evidence limit, or a title is semantically correct but violates the requested character limit. | Deliver the bounded research account; correct the title's explicit delivery constraint. Neither more searching nor semantic equivalence alone establishes completion. | Research stop condition, truthful limitation, requested artifact and constraints. |

The inspected rules express the needed distinctions for these contrasts. This says nothing about compliance rates on small models, memory persistence in a particular host, or rendered artifact quality.

## Recommended next action and verification

Apply the two local guide wording corrections first. If expanding the ledger at the same time, add only selected source locators and the method/transfer limits needed to make this review recoverable. Keep SKILL.md, the index, completion rubric, and source IDs unchanged unless a new consequential defect is demonstrated.

After that, this bounded core review can close without another broad collection of constructed chains. A further deep review should target a remaining claim with a concrete decision consequence or an actual upcoming use; it should not manufacture a controller rewrite from the absence of universal empirical validation.

Only this report is added. Checks passed for its five local links, UTF-8 without BOM, CRLF line endings, terminal newline, whitespace, and unchanged hashes of the 106 pre-existing files captured from the installable skill, evidence-review directory, and root task-guide pointer. Final Git status and diff were inspected; git diff --check passed. No package/routing tests are needed for a report-only addition; no runtime test result is claimed. Existing Google edits and reports 38-44 remain preserved. No commit, push, release tag, or cleanup is included.

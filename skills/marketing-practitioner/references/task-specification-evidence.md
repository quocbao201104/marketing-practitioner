# Task Specification Evidence Ledger

This supplementary ledger supports the user-facing `TASK-SPECIFICATION-GUIDE.md`.

It is intentionally scoped to **task specification for LLM-assisted marketing work**. It is not a library of prompt tricks, a universal model-behavior theory, or a new runtime contract. Findings are used only when they support a decision-relevant distinction in the guide.

Research reviewed: 2026-08-24.

---

## [TS01] Yang et al. — Prompt underspecification

Chenyang Yang, Yike Shi, Qianou Ma, Michael Xieyang Liu, Christian Kaestner, & Tongshuang Wu. (2026). **What Prompts Don’t Say: Understanding and Managing Underspecification in LLM Prompts.** *Findings of the Association for Computational Linguistics: ACL 2026*, 9072–9101. DOI: 10.18653/v1/2026.findings-acl.441. https://aclanthology.org/2026.findings-acl.441/

Use: direct evidence that omitted user-important requirements can make LLM behavior fragile across prompt/model changes, while naively specifying every requirement does not reliably improve performance because instructions can compete and instruction-following is limited.

Boundary: the study concerns LLM-powered software tasks and evaluated prompt requirements; it does not establish one universal user template or a fixed optimal prompt length.

## [TS02] Sclar et al. — Sensitivity to meaning-preserving prompt formatting

Melanie Sclar, Yejin Choi, Yulia Tsvetkov, & Alane Suhr. (2024). **Quantifying Language Models’ Sensitivity to Spurious Features in Prompt Design or: How I learned to start worrying about prompt formatting.** *ICLR 2024*. https://proceedings.iclr.cc/paper_files/paper/2024/hash/6c0e99d736da621403018ca7b32b1a4d-Abstract-Conference.html

Use: evidence that some models and few-shot settings can be highly sensitive to meaning-preserving formatting changes and that the best format does not transfer cleanly across models.

Boundary: the result is not a claim that every modern model or open-ended task is equally prompt-sensitive.

## [TS03] Hua et al. — Prompt-sensitivity counterevidence

Andong Hua, Kenan Tang, Chenhe Gu, Jindong Gu, Eric Wong, & Yao Qin. (2025). **Flaw or Artifact? Rethinking Prompt Sensitivity in Evaluating LLMs.** *EMNLP 2025*. https://aclanthology.org/2025.emnlp-main.1006/

Use: counterevidence showing that some reported prompt sensitivity can be amplified by rigid evaluation methods and falls when semantically equivalent answers are judged more appropriately.

Boundary: this prevents converting prompt sensitivity into a universal claim that tiny wording changes always matter. The guide therefore prioritizes semantic task definition over magic wording.

## [TS04] Shi et al. — Irrelevant context can distract

Freda Shi, Xinyun Chen, Kanishka Misra, Nathan Scales, David Dohan, Ed H. Chi, Nathanael Schärli, & Denny Zhou. (2023). **Large Language Models Can Be Easily Distracted by Irrelevant Context.** *ICML 2023*, PMLR 202:31210–31227. https://proceedings.mlr.press/v202/shi23a.html

Use: controlled evidence that irrelevant information can degrade reasoning performance and that prompting methods are not automatically robust to such distractors.

Boundary: the benchmark is arithmetic reasoning with constructed irrelevant context; it supports a relevance principle, not a universal effect size for marketing tasks.

## [TS05] Liu et al. — Long-context utilization and position

Nelson F. Liu, Kevin Lin, John Hewitt, Ashwin Paranjape, Michele Bevilacqua, Fabio Petroni, & Percy Liang. (2024). **Lost in the Middle: How Language Models Use Long Contexts.** *Transactions of the Association for Computational Linguistics, 12*, 157–173. DOI: 10.1162/tacl_a_00638. https://aclanthology.org/2024.tacl-1.9/

Use: evidence that models can use long contexts unevenly and that simply placing more material inside an available context window does not ensure robust use of the relevant information.

Boundary: tested multi-document QA and key-value retrieval; the guide uses it only against the assumption that context capacity equals context usefulness.

## [TS06] Du et al. — Context length alone can hurt

Yufeng Du, Minyang Tian, Srikanth Ronanki, Subendhu Rongali, Sravan Babu Bodapati, Aram Galstyan, Azton Wells, Roy Schwartz, Eliu A. Huerta, & Hao Peng. (2025). **Context Length Alone Hurts LLM Performance Despite Perfect Retrieval.** *Findings of EMNLP 2025*, 23281–23298. https://aclanthology.org/2025.findings-emnlp.1264/

Use: evidence across multiple tasks and models that longer input can reduce performance even when relevant evidence is perfectly retrievable.

Boundary: observed magnitudes are benchmark- and model-specific. The durable rule is to prefer relevant decision-changing context, not to impose a universal token ceiling.

## [TS07] Zhang, Knox & Choi — Clarifying ambiguous requests

Michael J. Q. Zhang, W. Bradley Knox, & Eunsol Choi. (2025). **Modeling Future Conversation Turns to Teach LLMs to Ask Clarifying Questions.** *ICLR 2025*. https://proceedings.iclr.cc/paper_files/paper/2025/hash/97e2df4bb8b2f1913657344a693166a2-Abstract-Conference.html

Use: evidence that LLMs often presuppose one interpretation of an ambiguous request and that systems can learn to ask clarification when it improves later answers while answering directly when clarification is unnecessary.

Boundary: the experiments do not establish a universal decision rule for every agent task.

## [TS08] Zhang & Choi — Clarify when necessary

Michael J. Q. Zhang & Eunsol Choi. (2025). **Clarify When Necessary: Resolving Ambiguity Through Interaction with LMs.** *Findings of NAACL 2025*, 5541–5558. DOI: 10.18653/v1/2025.findings-naacl.306. https://aclanthology.org/2025.findings-naacl.306/

Use: supports treating clarification as a utility decision that depends on the distribution of plausible interpretations and the user’s preference for speed versus carefulness, rather than as an always-ask rule.

Boundary: evaluated QA, machine translation, and NLI. The guide translates the principle conservatively to marketing tasks.

## [TS09] Zhang et al. — Ambiguity identification remains imperfect

Tong Zhang, Peixin Qin, Yang Deng, Chen Huang, Wenqiang Lei, Junhong Liu, Dingnan Jin, Hongru Liang, & Tat-Seng Chua. (2024). **CLAMBER: A Benchmark of Identifying and Clarifying Ambiguous Information Needs in Large Language Models.** *ACL 2024*, 10746–10766. DOI: 10.18653/v1/2024.acl-long.578. https://aclanthology.org/2024.acl-long.578/

Use: evidence that off-the-shelf LLMs can struggle to identify and clarify ambiguous information needs and that few-shot or chain-of-thought prompting does not automatically solve the problem.

Boundary: benchmark performance should not be converted into a claim that every ambiguity requires an explicit user policy.

## [TS10] Li et al. — Examples can introduce demonstration bias

Lvxue Li, Jiaqi Chen, Xinyu Lu, Yaojie Lu, Hongyu Lin, Shuheng Zhou, Huijia Zhu, Weiqiang Wang, Zhongyi Liu, Xianpei Han, & Le Sun. (2024). **Debiasing In-Context Learning by Instructing LLMs How to Follow Demonstrations.** *Findings of ACL 2024*, 7203–7215. DOI: 10.18653/v1/2024.findings-acl.430. https://aclanthology.org/2024.findings-acl.430/

Use: evidence that demonstration selection and ordering can materially affect in-context learning and that examples can create semantic ambiguity about the intended mapping.

Boundary: this does not imply examples are harmful. It supports `EXAMPLE ≠ RULE` and the use of examples only when they clarify a pattern that prose alone does not communicate efficiently.

---

## Current provider guidance

Provider documentation is useful for current interface and model-specific prompting behavior, but it is not treated as independent empirical proof of universal effectiveness.

### [TS11] OpenAI — Prompt engineering guidance

OpenAI. **Prompt engineering.** OpenAI API documentation. Reviewed 2026-08-24. https://developers.openai.com/api/docs/guides/prompt-engineering

Use: current first-party guidance separating instructions, examples, and relevant context; supports explicit goals/constraints and selective use of external context.

Boundary: API message roles, model-specific parameters, and model-family advice are implementation-specific and are not required by the user-facing guide.

### [TS12] Anthropic — Prompting best practices

Anthropic. **Prompting best practices.** Claude Platform documentation. Reviewed 2026-08-24. https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices

Use: current first-party guidance favoring clear/direct instructions, explicit desired output, relevant context, and examples when they materially steer format/tone/structure; current guidance also warns against blanket over-prompting for newer models.

Boundary: XML tags, role prompting, example-count recommendations, and model-specific behavior are not promoted to universal rules.

### [TS13] Google — Prompt design strategies

Google. **Prompt design strategies.** Gemini API documentation. Reviewed 2026-08-24. https://ai.google.dev/gemini-api/docs/prompting-strategies

Use: current first-party guidance on clear tasks, constraints, context, examples, output formats, and grounding. The documentation also notes that too many examples can overfit a response and gives model-specific advice to avoid unnecessary language.

Boundary: Gemini-specific syntax, tool configuration, example templates, and reasoning instructions are not generalized across vendors.

---

## Evidence-use rule

The guide keeps only distinctions that survive more than one evidence type or have a direct decision consequence.

```text
ONE PROVIDER RECOMMENDATION
≠ UNIVERSAL PROMPT LAW

ONE BENCHMARK EFFECT
≠ FIXED USER TEMPLATE

MORE REQUIREMENTS
≠ MORE COMPLETE TASK SPECIFICATION

MORE CONTEXT
≠ MORE RELEVANT CONTEXT
```

The practical target is the smallest task specification that prevents a materially different job, evidence boundary, fixed decision, or output from being silently substituted for the one the user intended.
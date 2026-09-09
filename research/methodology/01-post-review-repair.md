# Research Methodology — Post-Review Repair Record

Status: **BOUNDED REVIEW REPAIR**

Original reviewed candidate:

`51e343be2b9c85a4ddfe07c01928a41fb18356c1`

Independent methodology review verdict:

```text
PASS_WITH_LOCAL_REPAIRS
```

The review identified exactly four material findings:

```text
RM-T01
RM-T02
RM-T03
RM-T04
```

This record documents only the bounded corrections made in response. It does not reopen the methodology or introduce new research process requirements.

---

## RM-T01 — exploratory research before a named decision

### Finding

The original framing required material research to explain why the question changes a named decision. That could force a researcher to invent a downstream segment, intervention, campaign, or other practitioner decision before bounded exploratory learning had legitimately established one.

### Repair

The methodology now permits a bounded learning or problem-framing objective before a named practitioner decision exists.

The framing contract was generalized from a decision-only chain to:

```text
INPUT / MATERIAL
→ CURRENT UNDERSTANDING / REPRESENTATION / ROUTE
→ FAILURE, OPEN QUESTION, OR LEARNING OBJECTIVE
→ WHY IT CAN CHANGE UNDERSTANDING, INTERPRETATION,
  OR A SUBSEQUENT DECISION
→ SMALLEST RESEARCH QUESTION
```

The document also explicitly forbids inventing a downstream decision merely to justify discovery.

This repair is reflected in the opening section, the real-task probe guidance, the stopping rule, the practical loop, and the core principle so that the exception is not locally stated and then contradicted elsewhere.

---

## RM-T02 — source sufficiency versus triangulation

### Finding

The original methodology said to triangulate where warranted but did not give a usable threshold for when one strong source is sufficient versus when multiple sources are materially required.

This could create both unnecessary source ceremony for bounded source-owned facts and under-research for cross-regime synthesis or architecture claims.

### Repair

The methodology now states:

- one authoritative source may be sufficient when a claim is source-owned, directly stated, current, and kept within that source's scope;
- triangulation is warranted when the conclusion requires synthesis, transfer, causal interpretation, generalization across regimes, architecture expansion, or resolution of material disagreement or uncertainty;
- another source is useful when it can plausibly change the bounded conclusion, scope, uncertainty, interpretation of a material counterexample, or repository action.

No universal source-count requirement or evidence hierarchy was introduced.

---

## RM-T03 — evidence type versus project inferential status

### Finding

The original `EMPIRICAL / ACADEMIC` status collapsed different concepts:

- empirical evidence form;
- academic provenance.

It also gave authoritative first-party documentation and formal theory no clean representation.

### Repair

The methodology now separates two axes.

### Source / evidence type

Examples include:

- authoritative first-party documentation;
- empirical study;
- review / meta-analysis / methodological source;
- formal / conceptual theory;
- professional practice;
- implementation / repository evidence.

### Project inferential status

The repository separately records whether a conclusion is:

- externally supported;
- professional practice;
- project synthesis;
- contextual hypothesis;
- unknown.

These are not presented as a universal evidence hierarchy or mandatory ledger taxonomy.

The repair prevents formal theory from inheriting the authority of observed evidence merely because it is academic and prevents first-party source-owned facts from being forced into a practitioner-practice bucket.

---

## RM-T04 — semantic test for operationalization

### Finding

The original methodology listed possible outputs such as rule, gate, state, handoff, route, warning, and evaluation oracle without enough guidance for deciding which mechanism is actually justified.

That left room for a researcher to choose the smallest-looking formal artifact rather than the least powerful mechanism required by the demonstrated failure.

### Repair

The methodology now gives compact semantic promotion tests for:

- clarification;
- evidence requirement;
- gate;
- state / ledger;
- handoff;
- route / discovery edge;
- warning / qualification;
- scoped adaptation;
- small workflow;
- evaluation oracle;
- nothing.

These are explicitly described as semantic tests rather than mandatory artifact categories.

The governing rule is now:

> choose the least powerful mechanism that fixes the demonstrated failure while preserving ownership, state, and evidence boundaries.

---

# Scope check

The repair does **not**:

- modify `AGENTS.md`;
- modify `CONTRIBUTING.md`;
- modify `SKILL.md` or runtime knowledge;
- add a benchmark or evaluation harness;
- add a mandatory research template;
- add a universal evidence hierarchy;
- require freeze/review ceremony for low-risk research;
- reopen the methodology beyond the four reviewed findings.

Post-repair candidate head after these bounded methodology edits:

`d7fc5af67c1d37bdb30134e49c182f64381d5617`

A post-repair verifier should evaluate closure of `RM-T01` through `RM-T04` against the original reviewed head rather than performing a new broad methodology review.

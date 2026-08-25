# Search & Discovery Architecture — Mechanical Verification

Status: **MECHANICAL GATE PASS WITH EXECUTION-SCOPE NOTE**  
Branch: `candidate/search-discovery-architecture`  
Base: `main@8e77150e589ce95d886ac637d241937d260b1610`  
Date: 2026-08-25

## 1. Purpose

This gate checks mechanical integrity before targeted runtime evaluation. It does not adjudicate marketing/discovery reasoning quality.

## 2. Environment constraint

The available shell environment could not resolve `github.com`, so a normal local `git clone` of the candidate branch was not possible. GitHub Actions was deliberately not used as a substitute.

Therefore this verification uses two explicit evidence classes rather than pretending a checked-out branch test run occurred:

1. **locally executed helper-mechanics assertions** reconstructed from the candidate `scripts/get-knowledge.py` semantics;
2. **connector-backed candidate binding verification** against the actual candidate branch files.

The repository's monolithic `test-knowledge-routing.py` output of `PASS\t49 routing-mechanics smoke checks` is **not claimed as executed** in this gate.

## 3. Locally executed helper-mechanics assertions

The following candidate helper behaviors were executed in a local Python sandbox using the fetched candidate helper semantics:

- fenced-heading exclusion;
- exact heading-section extraction;
- nested heading boundaries;
- marker extraction;
- reversed-marker rejection;
- duplicate-heading rejection;
- route ID parsing and namespace/section lookup;
- duplicate JSON-key rejection;
- mutually exclusive CLI-mode selection;
- `--namespace` mode guard;
- path traversal rejection;
- evidence-source scanning outside fenced examples;
- case-insensitive source lookup;
- duplicate evidence-ID rejection;
- missing source rejection;
- POSIX logical source path behavior.

Execution result:

```text
PASS 18 core helper-mechanics assertions executed locally
PASS 10 source/path mechanics assertions executed locally
```

Total directly executed helper assertions in this environment: **28 PASS / 0 FAIL**.

## 4. Candidate discovery-route bindings

The actual candidate `routing-index.json` defines the following new namespace bindings:

```text
discovery.core
→ ## 1. Scope: decide how information and entities can become discoverable

discovery.need
→ ## 2. Discovery need, expression, and context

discovery.availability
→ ## 3. Scoped discovery availability

discovery.selection
→ ## 4. Retrieval, relevance, selection, and discovery modes

discovery.commitment
→ ## 5. Discovery representation and system commitment

discovery.observation
→ ## 6. Discovery observation and causal boundary

discovery.decision-record
→ ## 8. Compact discovery decision record

discovery.invariants
→ ## 9. Anti-folklore invariants
```

Each selector was verified against the actual candidate Chapter 13 content. All eight exact headings are present in the candidate file.

Result:

```text
8 / 8 discovery route bindings present and selector-consistent
```

## 5. Evidence binding

The candidate routing smoke-test extension adds source lookup for `SD09`.

The actual candidate evidence ledger contains exactly the intended heading:

```text
## [SD09] Bing — Evolving role of the index: from ranking pages to supporting answers
```

The record explicitly supports the human-selection vs system-commitment distinction and explicitly does not support a universal grounding implementation or `retrieved = safe to commit` inference.

Result:

```text
SD09 candidate evidence binding present
```

## 6. Regression-scope check

Compared with `main@8e77150e589ce95d886ac637d241937d260b1610`, the candidate remains ahead-only and the routing-index modification is localized to adding the `discovery` namespace. Existing namespace definitions were not intentionally redesigned.

The controller patch is also localized: it adds a generic Search / discovery operating path and removes generic `search` from the sentence that previously made Platform content / distribution the catch-all owner. Product/commerce search remains under Chapter 09.

## 7. Gate verdict

> **PASS FOR TARGETED RUNTIME EVALUATION.**

This verdict means the new candidate bindings and helper mechanics are mechanically coherent enough to exercise in runtime cases.

It does **not** mean:

- the full checked-out `test-knowledge-routing.py` suite was executed;
- all pre-existing routes were re-executed end-to-end in this environment;
- runtime routing/owner behavior is correct;
- the candidate is merge-ready.

Those questions remain for targeted runtime evaluation and adjudication.
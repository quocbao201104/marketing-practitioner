# Founder-led Sales — Bounded Runtime / Path Evaluation

## Status

**EXECUTION CONTRACT FROZEN — LIVE SKILL RUN PENDING**

This phase follows the independent post-repair `PASS` for repaired implementation candidate:

```text
IMPLEMENTATION_CANDIDATE_SHA = 3968aff927731e0dc8fb1ce6524cc2282f89333a
```

The implementation architecture, FS1–FS8 topology, and ownership model remain frozen.

This document does not reopen theory. It binds the first live path pass to the eight episodes already selected in `03-runtime-evaluation-brief.md`.

---

## 1. Evaluation assets

Case corpus:

```text
evals/behavioral/cases/founder-led-sales-runtime-v1.json
```

Route oracle:

```text
evals/behavioral/oracles/founder-led-sales-runtime-v1.route-oracle.json
```

Oracle/corpus preflight:

```text
evals/behavioral/tests/test_founder_sales_runtime_oracle.py
```

The corpus contains exactly:

```text
E01 → BEH-FLS-RUNTIME-001
E05 → BEH-FLS-RUNTIME-005
E07 → BEH-FLS-RUNTIME-007
E10 → BEH-FLS-RUNTIME-010
E11 → BEH-FLS-RUNTIME-011
E13 → BEH-FLS-RUNTIME-013
E15 → BEH-FLS-RUNTIME-015
E16 → BEH-FLS-RUNTIME-016
```

Do not add cases merely for coverage before this bounded pass is interpreted.

---

## 2. What this pass is intended to establish

The first pass asks whether the skill-present runtime can provide observable evidence for:

```text
controller activation
→ correct Founder-led Sales logical route
→ required cross-FS handoff when applicable
→ FS1 resource gate when applicable
→ no forbidden owner/path
→ answer/state compatible with the frozen episode oracle
```

It is not a general sales benchmark and does not establish marketing or sales efficacy.

A correct-looking final answer without sufficient path evidence cannot establish routing correctness.

---

## 3. Execution regime

Use the existing behavioral harness and the committed `current-skill` profile.

A no-skill baseline is optional for this phase because the frozen claim is route/ownership behavior of the implemented skill, not uplift over generic model competence.

Recommended first run:

```powershell
python -B -m evals.behavioral.behavioral_eval.cli validate `
  --cases evals\behavioral\cases\founder-led-sales-runtime-v1.json `
  --profiles evals\behavioral\profiles

python -B -m evals.behavioral.behavioral_eval.cli run `
  --cases evals\behavioral\cases\founder-led-sales-runtime-v1.json `
  --adapter codex-cli `
  --profile-id current-skill `
  --repeat-limit 1 `
  --results evals\behavioral\results\founder-led-sales-runtime-v1
```

Then reconstruct the skill walk:

```powershell
python -B -m evals.behavioral.behavioral_eval.cli trace `
  --results evals\behavioral\results\founder-led-sales-runtime-v1 `
  --oracle evals\behavioral\oracles\founder-led-sales-runtime-v1.route-oracle.json `
  --output evals\behavioral\results\founder-led-sales-runtime-v1-walk-trace.json `
  --markdown evals\behavioral\results\founder-led-sales-runtime-v1-walk-trace.md
```

Generated result bundles stay untracked.

---

## 4. Path-proof policy

For this evaluation, the sidecar oracle intentionally requires exact `founder-sales.*` logical-route evidence for the primary owner.

Why:

```text
Chapter 16 contains all FS owners in one file.

A generic read of the file can show that knowledge was available,
but cannot by itself prove which logical owner the runtime selected.
```

Therefore:

- an observed successful `get-knowledge.py founder-sales.<owner>` route can satisfy owner path proof;
- a direct whole-file Chapter 16 read is insufficient and should be treated as over-read/path weakness;
- a bounded direct section read that the current trace format cannot identify to a logical route may produce a useful answer, but does not establish the frozen route claim.

In the last case use:

```text
RUNTIME_PATH_UNVERIFIED
```

rather than rewriting the oracle after seeing the result.

This evaluation constraint does not change the production skill rule that direct bounded reads are allowed when the helper is unavailable or policy-denied.

---

## 5. Frozen route expectations

```text
E01
selection → pursuit

E05
proof
with decision/pursuit only if a new blocker/resource decision is actually introduced

E07
progression → pursuit
access may be inspected, but seller activity must not be manufactured

E10
proof → pursuit

E11
commercial → pursuit
commercial-design is forbidden as the default owner

E13
proof → diagnosis → progression

E15
decision → proof
commercial is forbidden as the primary path

E16
pursuit
```

The route oracle is mechanism evidence. Final-answer review remains a separate question.

---

## 6. Answer review

Review each output against the committed `review_criteria` in the case corpus.

Do not reward explicit recitation of internal FS names or route identifiers. Those terms are included in `forbidden_disclosures` so the visible answer should remain user-facing.

For each case record:

```text
ANSWER_DISPOSITION
pass / fail / unresolved

PATH_DISPOSITION
walk_ok / no_activation / skip_jit / wrong_edge /
resolve_fail / missing_handoff / over_read / loaded_but_ignore
```

A good path does not compensate for a bad answer.

A good answer does not prove a missing path.

---

## 7. Episode-level interpretation

Use these rules:

```text
answer pass + walk_ok
→ episode PASS

answer pass + path not proven
→ episode RUNTIME_PATH_UNVERIFIED

answer fail + required route loaded
→ inspect loaded_but_ignore / implementation guidance fidelity

wrong owner / forbidden path with architecture still representable
→ candidate local repair

concrete unrepresentable decision or true irreducible dual ownership
→ architecture reopen candidate
```

Do not infer architecture failure from writing quality alone.

---

## 8. Overall verdict set

Return exactly one after the eight-case pass:

```text
PASS
PASS_WITH_LOCAL_REPAIRS
RUNTIME_PATH_UNVERIFIED
ARCHITECTURE_REOPEN_REQUIRED
```

`PASS` requires the tested episodes to have sufficient path evidence and compatible answer behavior.

If any case lacks enough path evidence to support the routing claim, do not upgrade the overall result to `PASS` merely because the visible output is correct.

---

## 9. Expansion rule

Do not automatically execute E02, E03, E04, E06, E08, E09, E12, or E14.

Expand only when:

1. one of the first eight exposes a concrete ambiguity that one of those episodes can discriminate; or
2. a repair changes a boundary covered by an unexecuted episode.

Do not use case count as evidence quality.

---

## 10. Current gate

Before live execution:

```text
[ ] corpus schema validates
[ ] route oracle loads
[ ] corpus/oracle identities match exactly
[ ] every referenced founder-sales logical route exists
[ ] repository Verify passes with the evaluation assets
```

After those mechanical gates pass, the next valid evidence is the single-repetition skill-present live pass above.

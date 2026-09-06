# Brand Identity and Visual Systems — BI-R01 Live Probe Contract

Status: **POST-REVIEW EVALUATION-ONLY LOCAL CORRECTION — RUNTIME UNCHANGED**

Independent runtime-review verdict:

```text
PROCEED AFTER LOCAL CORRECTIONS
```

Original frozen implementation/evaluation target:

```text
544b33a823c0b19017b274773495a8af62a2cf44
```

Material finding:

```text
BI-R01 / LIVE ACTIVATION AND PATH DISCRIMINATION
severity: material-local
owner: evaluation first
```

The independent reviewer found no material static implementation defect, generic-design scope expansion, route-surface representation failure, owner collision requiring shared architecture, or evidence-status regression. The remaining release gate is only the two-case live path probe below.

Do **not** repair theory, add routes, add a controller job, or edit runtime wording before this probe demonstrates an actual failure.

---

## 1. Exact case pair

The frozen reviewer pair is encoded in:

```text
evals/behavioral/cases/brand-identity-live-probe-v1.json
```

### BI-LIVE-001 — nounless positive

```text
We've used this orange shape for eight years.
We never measured recognition.
The team is bored with it and wants to replace it.
Should we?
```

Required live path:

```text
Marketing Practitioner activation
→ brand-identity.equity directly
→ Chapter 15 §2 delivered/read
→ no mandatory brand-identity.core
→ no exploration
→ no Chapter 03 reopening
```

Required answer semantics:

```text
UNMEASURED != ZERO != PROVEN
internal boredom != buyer-memory evidence
```

### BI-LIVE-002 — noun-heavy negative

```text
The approved logo and brand identity master are final.
Export the SVG and PNG sizes I need.
```

Required live path:

```text
identity fixed
→ NO DEEP brand-identity.* ROUTE
→ production/export execution only
```

Loading the overall Marketing Practitioner skill is not itself a failure in the negative case. The failure condition is deep Brand Identity routing caused only by visual nouns.

---

## 2. Why the existing author walkthrough is insufficient

The existing V01–V20 walkthrough establishes author-side semantic route oracles only. It does not establish:

```text
host skill discovery / activation
logical route request
route-resource delivery
material read order
live model compliance
```

The deterministic routing suite establishes that the routes are addressable. It does not establish that a live model chooses them.

This probe therefore adds no new branding theory. It observes the missing runtime path evidence only.

---

## 3. Live execution

Use the existing isolated behavioral harness and the existing `current-skill` Codex CLI profile. Run one repetition of exactly these two cases.

From the repository root on a host where Codex CLI is installed and authenticated:

```powershell
python -B -m evals.behavioral.behavioral_eval.cli validate `
  --cases evals\behavioral\cases\brand-identity-live-probe-v1.json `
  --profiles evals\behavioral\profiles
```

Then:

```powershell
python -B -m evals.behavioral.behavioral_eval.cli run `
  --cases evals\behavioral\cases\brand-identity-live-probe-v1.json `
  --adapter codex-cli `
  --profile-id current-skill `
  --repeat-limit 1 `
  --results evals\behavioral\results\brand-identity-live-probe-v1
```

Do not add the baseline arm: BI-R01 is a live current-skill activation/path question, not a skill-vs-baseline quality benchmark.

Do not run the other V01–V20 cases live merely for coverage.

---

## 4. Trace adjudication

The post-review trace checker is:

```text
evals/behavioral/behavioral_eval/brand_identity_live_probe.py
```

Run:

```powershell
python -B -m evals.behavioral.behavioral_eval.brand_identity_live_probe `
  --results evals\behavioral\results\brand-identity-live-probe-v1
```

The checker inspects the sealed raw Codex events for the discriminating mechanical conditions and prints the final outputs for semantic adjudication.

It intentionally does **not** convert wording similarity into an automatic semantic PASS. The final bounded decision remains a small manual adjudication against the explicit criteria in the corpus.

### Positive mechanical PASS

Required:

```text
skill activation observed
first requested Brand Identity route = brand-identity.equity
equity helper exits successfully
Chapter 15 §2 heading appears in delivered command output
activation precedes equity delivery
no brand-identity.core request
no brand-identity.exploration request
no Chapter 03 read
final output present
```

### Negative mechanical PASS

Required:

```text
executor succeeds
final output present
no brand-identity.* get-knowledge request
no Chapter 15 specialist read
```

`ACTIVATION_UNVERIFIED` is acceptable for the negative case if no deep Brand Identity route/read occurs. The existing generic harness normally treats a workspace-copy run without skill activation as operationally unverified; this probe deliberately distinguishes that generic harness state from the reviewer's negative-control criterion.

---

## 5. Repair decision tree

Do not preemptively edit runtime.

```text
BI-LIVE-001 misses Marketing Practitioner discovery / activation
→ repair only activation-facing SKILL metadata

BI-LIVE-001 activates but requests core / exploration / wrong owner first
→ repair only the SKILL Brand Identity route rule

BI-LIVE-001 requests equity but delivery / read sequence is wrong
→ repair only the smallest routing/read integration defect

BI-LIVE-002 deep-routes on logo / brand identity / SVG / PNG nouns
→ repair only activation / hard-stop wording

both cases pass mechanically + semantically
→ BI-R01 CLOSED
→ no runtime repair justified
```

Any runtime repair creates a new implementation target and requires a bounded post-repair verification. If both cases pass without runtime edits, record the live evidence and proceed to release preparation without reopening theory or shared architecture.

---

## 6. Evidence discipline

The probe result may establish only the tested current host/model/profile behavior for this matched pair.

It does not establish:

- universal activation reliability for every host/model;
- correctness of all nine routes under arbitrary tasks;
- general visual-design quality;
- logo aesthetics;
- real-world brand outcomes;
- a reason to broaden the evaluation corpus.

The purpose is exactly the discriminating evidence demanded by BI-R01 and no more.

# SWE-XCI-01 — Cross-artifact Decision Change & Repair

Status: **REPAIRED DESIGN FREEZE CANDIDATE — CLOSURE-ONLY INDEPENDENT REVIEW REQUIRED — IMPLEMENTATION BLOCKED**

Episode classification:

```text
SYNTHETIC TARGETED / DIAGNOSTIC WORK EPISODE

!= ecological pressure evidence
!= independent real-world recurrence
!= evidence that this failure is common in industry
```

Governing track: **Cross-artifact Decision Propagation & Consistency**

Architecture hypothesis entering this episode:

```text
NEW CONTENT-GOVERNANCE SPECIALIST
→ NOT JUSTIFIED

NEW MARKETING-PRACTITIONER PRIMITIVE
→ NOT JUSTIFIED

OPEN QUESTION
→ can the current architecture execute a bounded
   cross-artifact decision change reliably?
```

---

## 1. Governing question

> Given a bounded and fully visible marketing artifact estate whose release candidate has already been reviewed under one valid business state, can an agent correctly reconcile that candidate after an authoritative marketing decision changes, repairing exactly the current representations that materially depend on the changed decision while preserving current nondependent representations, historical/source evidence, approved localization, and unrelated state?

The calibrated behavior is:

```text
CHANGE
when a governing dependency changed

PRESERVE
when the governing dependency did not change
or the representation remains independently valid
```

The episode does not test:

```text
filesystem discovery
generic brand consistency
literal terminology synchronization
CMS operation
content governance software
dependency-graph maintenance
route conformity
handbook recall
```

---

## 2. Frozen fictional business state

Product:

```text
RelayDesk
```

At logical time `09:00`, the authoritative state is:

```text
CURRENT SELF-CATEGORY
AI customer-service chatbot

PRIMARY VALUE
Helps marketplace sellers respond faster.

CONTROL MODEL
Seller reviews consequential replies before sending.
```

These are three separate propositions.

Therefore:

```text
category state
!= primary value
!= control model
```

A later category change does not authorize an inference that product functionality, proof, customer outcome, or seller-control behavior changed.

---

## 3. Executor-facing request

At `09:00`, the executor receives:

> You own the coordinated content update for RelayDesk. QA needs a release candidate from the supplied workspace by 10:30, and the final release package is due at 15:00. Review every item in `release-manifest.csv`, bring current release material in line with the currently approved business state, and keep `release-log.md` updated with the disposition of each item. Use the supplied business evidence and do not invent product facts.

The prompt does not reveal:

```text
which decision will later change
which files contain mixed semantic roles
which wording is protected
which historical material must remain unchanged
which localization is intentionally valid
pressure/control identity
handbook path
expected reasoning sequence
```

---

## 4. Frozen visible workspace

The complete in-scope artifact estate is declared in:

```text
release-manifest.csv
```

There are exactly sixteen target artifacts:

| ID | Path | Frozen material role |
|---|---|---|
| A01 | `website/home.md` | Present-day RelayDesk self-category |
| A02 | `website/about.md` | Present-day RelayDesk self-category |
| A03 | `campaigns/nurture-draft.md` | Present-day RelayDesk self-assertion |
| A04 | `ads/search-ad-draft.md` | Seller-authored current RelayDesk description, distinct from search-keyword targeting |
| A05 | `profiles/linkedin-bio.md` | Present-day RelayDesk self-category |
| A06 | `commerce/listing-en.md` | Seller-authored current English product representation, not a platform taxonomy field |
| A07 | `search/compare-ai-chatbots.md` | Mixed: external comparison/search frame + present-day RelayDesk self-description |
| A08 | `case-studies/acme.md` | Mixed: explicitly present-day publisher intro + attributed customer quotation |
| A09 | `commerce/listing-vi.md` | Currently approved Vietnamese localized realization |
| A10 | `archive/launch-announcement-2025.md` | Historical published marketing artifact |
| A11 | `research/customer-interviews.md` | Verbatim customer/source evidence |
| A12 | `search/query-observations.csv` | Observed search-language evidence |
| A13 | `decisions/positioning-history.md` | Mixed: CURRENT STATE + historical decision entries |
| A14 | `brand/voice-guide.md` | Current negative control unrelated to category |
| A15 | `help/account-security.md` | Current negative control unrelated to category |
| A16 | `product/onboarding-actions.md` | Current product-language negative control unrelated to category |

Supporting visible evidence includes:

```text
release-manifest.csv
brand/current-positioning.md
brand/approved-localization.md
```

The executor maintains:

```text
release-log.md
```

Every manifest path is directly available to the executor.

No correctness claim may depend on discovering an undeclared artifact.

---

## 5. Authoritative localization evidence

`brand/approved-localization.md` establishes at `09:00`:

```text
scope:
current Vietnamese commerce surfaces

approved realization:
"Trợ lý AI cho người bán"

status:
approved

relationship to English wording:
approval does not require literal lexical equivalence
with the English self-category

validity:
remains active until separately revised,
withdrawn, or superseded
```

This is executor-visible business authority.

The evaluator must not independently decide that another Vietnamese phrase would be more natural and use that preference as the oracle.

---

## 6. Phase A — accepted QA candidate

Logical period:

```text
09:00 → 10:30
```

During Phase A, T0 remains authoritative.

The executor must review the complete manifest and prepare a QA candidate that is valid under T0.

The starting estate is intentionally capable of becoming a valid T0 candidate without knowledge of any future event.

At `10:30`, the harness seals:

```text
all 16 candidate artifact versions
all 16 artifact hashes
release-log.md
authoritative T0 evidence versions
logical-time event
```

It also records:

```text
qa_candidate_review_complete
qa_candidate_t0_valid
qa_candidate_accepted
```

`qa_candidate_accepted = true` only when:

```text
all 16 manifest items were observably reviewed

AND

the candidate contains no known material contradiction
with the authoritative T0 business state

AND

no material release blocker remains silently unresolved
```

T0 use of:

```text
AI customer-service chatbot
```

is valid during Phase A.

The accepted QA candidate becomes an explicit episode state.

It is not retroactively judged against R2.

If Phase A fails, the episode continues for diagnostic purposes, but the historical Phase-A failure remains.

---

## 7. Exogenous R2 event

At logical time `11:00`, before post-R2 work begins, the harness injects:

```text
positioning-review-R2.md
```

and records:

```text
R2_delivered = true
R2_content_hash
R2_exposure_event
```

Delivery is independent of executor behavior.

Within a sibling world, no-skill and skill-present conditions must receive the same R2 content and exposure event.

---

## 8. Pressure/control intervention

The pair differs only in the current category-state proposition and its necessary supersession closure.

### SWE-XCI-01-P — Pressure

At `11:00`:

```text
approved_current_self_category =
    "AI customer-service copilot"

previous_self_category =
    "AI customer-service chatbot"

previous_self_category_status =
    superseded_for_current_self-categorization

primary_value =
    unchanged

control_model =
    unchanged

product_facts =
    unchanged

existing_localization_approvals =
    unchanged
```

### SWE-XCI-01-C — Control

At `11:00`:

```text
approved_current_self_category =
    "AI customer-service chatbot"

previous_self_category =
    "AI customer-service chatbot"

previous_self_category_status =
    remains_current

primary_value =
    unchanged

control_model =
    unchanged

product_facts =
    unchanged

existing_localization_approvals =
    unchanged
```

The pressure intervention therefore tests:

```text
CHATBOT
→ COPILOT
```

It does not introduce seller-control semantics, new capabilities, new proof, or new customer outcomes.

---

## 9. Material cross-time dependency

The core state transition is:

```text
valid T0 state
↓
reviewed QA candidate accepted at 10:30
↓
authoritative R2 arrives at 11:00
↓
governing category either changes or remains current
↓
previously accepted candidate relations
must be selectively reopened or preserved
↓
final release at 15:00
```

For pressure:

```text
relation accepted as current at 10:30
+
relation depends on self-category
+
self-category superseded at 11:00

→ relation must be reconciled before final release
```

For control:

```text
relation accepted as current at 10:30
+
governing self-category remains authoritative

→ no category migration is required
```

The evaluator does not require the executor to use a particular internal “reopen” mechanism.

The work oracle concerns observable state.

---

## 10. Frozen relation ledger

The evaluator owns a prelocked relation ledger.

Required fields:

```text
relation_id
artifact_path
locator
temporal_role
semantic_role
source_authority
dependency_on_current_category
protection_class
pressure_disposition
control_disposition
```

Dependency classification is frozen before execution.

A semantic judge must not decide after seeing an output whether a relation “really depended” on the category.

---

## 11. Current category-dependent relations

Exactly nine current relations are hard category dependencies.

| Relation | Artifact | Frozen semantic role | Pressure | Control |
|---|---|---|---|---|
| R01 | A01 | Present-day RelayDesk self-category | REPAIR | PRESERVE |
| R02 | A02 | Present-day RelayDesk self-category | REPAIR | PRESERVE |
| R03 | A03 | Present-tense RelayDesk self-assertion in an unsent nurture artifact | REPAIR | PRESERVE |
| R04 | A04 | Seller-authored present-day RelayDesk self-description, not keyword text | REPAIR | PRESERVE |
| R05 | A05 | Present-day RelayDesk self-category | REPAIR | PRESERVE |
| R06 | A06 | Seller-authored present-day English representation, not platform taxonomy | REPAIR | PRESERVE |
| R07 | A07 | Present-day RelayDesk self-description inside comparison content | REPAIR | PRESERVE |
| R08 | A08 | Explicitly present-day publisher framing, e.g. `Today, RelayDesk is an AI customer-service chatbot for marketplace sellers.` | REPAIR | PRESERVE |
| R09 | A13 | Explicit `CURRENT STATE` category field | REPAIR | PRESERVE |

In pressure, semantic repair does not require exact lexical repetition of:

```text
AI customer-service copilot
```

A semantically faithful current representation may vary by environment.

The old self-category may not remain as RelayDesk's unqualified current self-category in these nine relations.

---

## 12. Current nondependent / protected relations

These relations remain current and independently valid.

They are evaluated separately from history/source evidence.

| Relation | Artifact | Protected/current role |
|---|---|---|
| P01 | A07 | External search/comparison frame such as `Best AI customer-service chatbots...` |
| P02 | A09 | Still-active approved Vietnamese commerce realization |
| P03 | A14 | Voice guidance unrelated to product category |
| P04 | A15 | Account-security guidance unrelated to product category |
| P05 | A16 | Product onboarding action language unrelated to product category |

Pressure R2 does not itself authorize material semantic alteration of P01–P05.

Changes remain permitted only where separate visible task evidence independently licenses them.

---

## 13. Historical / source / observation relations

These relations are not current self-category assertions.

| Relation | Artifact | Frozen role |
|---|---|---|
| S01 | A08 | Attributed customer quotation using historical/customer terminology |
| S02 | A10 | Historical 2025 launch positioning |
| S03 | A11 | Verbatim customer-interview wording |
| S04 | A12 | Observed query/search-language evidence |
| S05 | A13 | Historical positioning-decision entries |

Their supported source meaning is anchored to the `09:00` authoritative baseline.

Pressure R2 may change current interpretation or current-state annotation.

It may not fabricate that the source historically said something else.

---

## 14. Valid historical annotation

Historical/source fidelity does not mean whole-file immutability.

For example, this is valid:

```text
2025 ORIGINAL RECORD
RelayDesk was described as an AI customer-service chatbot.

CURRENT ANNOTATION
Current self-category changed to AI customer-service copilot
after the 11:00 positioning review.
```

This is invalid:

```text
rewrite the 2025 statement itself so it appears
RelayDesk was described as an AI customer-service copilot in 2025
```

Likewise:

```text
customer quotation
→ quotation meaning / attribution protected

surrounding present-day editorial context
→ may be updated where separately dependent
```

---

## 15. Release-log contract

`release-log.md` is a user-facing work artifact, not an evaluator schema.

At each required checkpoint, every manifest artifact must have an observable disposition.

No exact vocabulary is required.

Semantically equivalent forms are acceptable, including:

```text
updated
no change required
preserved
reviewed
unresolved
blocked
```

where justified.

The evaluator may use the release log to distinguish observable dispositions.

It may not infer hidden reasoning from silence or from the final diff alone.

Allowed diagnostics include:

```text
NO_OBSERVABLE_RELATION_ACCOUNTING

A required relation remains stale
and no relation-specific disposition can be grounded
in observable episode evidence.
```

and:

```text
EXPLICIT_WRONG_DISPOSITION

The executor observably classifies a relation
in a way that conflicts with the prelocked semantic oracle.
```

`SEMANTIC_MISCLASSIFICATION` may be used only when the classification itself is observable.

---

## 16. Phase B — final reconciliation

Logical period:

```text
11:00 → 15:00
```

The executor has access to:

```text
sealed candidate state
current workspace
R2
supporting authority files
```

At `15:00`, the harness seals:

```text
terminal versions of all 16 artifacts
terminal release-log.md
R2 evidence state
logical-time terminal event
```

The work oracle judges the terminal release package plus historical episode state.

---

## 17. Hard predicates

### XCI-H01 — Phase-A QA candidate readiness

Activation:

```text
10:30 gate
```

Requirement:

```text
all 16 manifest artifacts have an observable Phase-A disposition

AND

the QA candidate is materially valid under T0

AND

no known material T0 release defect is silently left unresolved
```

Using the valid T0 category during Phase A does not violate H01.

A Phase-A failure remains historical after R2.

### XCI-H02 — Final release-log completion

Activation:

```text
15:00 gate
```

Requirement:

```text
every manifest artifact has an observable terminal disposition
in release-log.md
```

No proposition-level explanation format is required.

H02 concerns completion of the requested release log.

It does not decide relation correctness or evaluator assessability.

### XCI-H03 — Required current-state repair

Activation:

```text
world = PRESSURE
AND
R2 exposure is valid
```

Requirement:

```text
R01–R09 no longer represent
"AI customer-service chatbot"
as RelayDesk's unqualified current self-category
at terminal release.
```

Acceptable repairs include environment-appropriate semantic realization.

Literal phrase matching is not required.

Missing valid semantic evidence for any required relation makes H03:

```text
NOT_ASSESSABLE
```

unless another independently grounded relation already establishes a material violation.

### XCI-H04 — Current nondependent / protected preservation

Activation:

```text
terminal gate
```

Requirement:

```text
P01–P05 retain their supported semantic state
unless separate visible authoritative evidence
or another explicit task requirement licenses changing them.
```

The predicate does not ask why the executor changed something.

It evaluates the observable semantic relation only.

### XCI-H05 — Source / history / observation fidelity

Activation:

```text
terminal gate
```

Requirement:

```text
S01–S05 preserve the source meaning,
attribution, temporal status, or observed fact
established by the authoritative 09:00 baseline.
```

Current annotations or surrounding editorial context may change where truthfully separated from the protected source relation.

A current-state change may not be projected backward into history.

### XCI-C01 — Control category preservation

Activation:

```text
world = CONTROL
AND
R2 exposure is valid
```

Requirement:

```text
the unchanged authoritative self-category
is not falsely treated as superseded.
```

The executor may make independently justified edits.

The control oracle forbids only a manufactured category migration unsupported by the authoritative state.

---

## 18. Derived pressure-calibration summary

`XCI-P01` is retained only as a derived reporting/metamorphic result.

It is not an additional hard predicate and does not vote separately in the work verdict.

For pressure:

```text
P01 =
    H03 required-change relations correct
    AND
    H04 current protected/nondependent relations correct
    AND
    H05 source/history/observation relations correct
```

Its purpose is to report whether the run demonstrated calibrated:

```text
CHANGE
+
PRESERVE
```

behavior.

---

## 19. Semantic evidence provenance

Three temporal evidence layers must remain distinct.

### 09:00 authoritative baseline

Used to establish:

```text
original source meaning
historical records
quotations
observations
localization authority
initial current business state
```

### 10:30 QA candidate baseline

Used to establish:

```text
what work had been reviewed and accepted under T0
before R2
```

### 15:00 terminal state

Used to establish:

```text
final release result after R2
```

A 10:30 snapshot must never replace the 09:00 authoritative source baseline for H04/H05.

This prevents Phase-A corruption from being laundered into a new “original”.

---

## 20. Minimum evidence by predicate family

For H03 relation assessment:

```text
10:30 candidate relation
+
terminal relation
+
R2 authoritative category state
```

The 09:00 relation may also be cited when material.

For H04 ordinary current protected/nondependent relations:

```text
09:00 authoritative relation
+
terminal relation
+
R2 where relevant
+
supporting authority when applicable
```

For approved localization:

```text
09:00 localized relation
+
brand/approved-localization.md
+
terminal localized relation
+
R2 localization-approval state
```

For H05:

```text
09:00 authoritative source/history/observation relation
+
terminal relation
```

plus attribution/context evidence where necessary.

For C01:

```text
10:30 candidate relation
+
terminal relation
+
control R2 authoritative category state
```

---

## 21. Judge-provenance rule

A semantic assessment is valid only when:

```text
judge_id is valid
AND
judge_id is non-empty
AND
judge_id is not "unavailable"
AND
all required evidence refs are valid sealed refs
```

Otherwise:

```text
NOT_ASSESSABLE
```

A malformed or ungrounded semantic assessment may not produce:

```text
SATISFIED
VIOLATED
NOT_APPLICABLE
```

Predicate activation determined by frozen world/event state must not be disabled by an ungrounded semantic judge.

---

## 22. Work-verdict aggregation

Use:

```text
SATISFIED
VIOLATED
NOT_ASSESSABLE
NOT_APPLICABLE
```

Aggregation:

```text
at least one applicable material hard predicate VIOLATED
→ FAIL
```

```text
no established applicable hard violation
+
at least one applicable material hard predicate NOT_ASSESSABLE
or run/oracle validity blocks judgment
→ UNRESOLVED
```

```text
all applicable material hard predicates SATISFIED
+
all required validity gates pass
→ PASS
```

`NOT_APPLICABLE` is excluded.

No scalar quality score is created.

`XCI-P01` does not independently affect aggregation.

---

## 23. Evaluator pentest fixtures

### FX-01 — Canonical good pressure

All nine dependent current relations are repaired.

P01–P05 remain semantically valid.

S01–S05 preserve source/history meaning.

Expected:

```text
PASS
```

### FX-02 — Noncanonical good pressure

The executor does not mechanically repeat:

```text
AI customer-service copilot
```

on every current surface.

It uses valid environment-specific expressions preserving the new current category meaning.

Expected:

```text
PASS
```

### FX-03 — Global lexical replacement

Every occurrence of old wording is replaced, including search frame, quotation, approved localization, archived copy, interviews, observed queries, and historical decision entries.

Expected:

```text
H03 may be satisfied
H04 VIOLATED
H05 VIOLATED
WORK FAIL
```

### FX-04 — Partial current-state repair

Homepage, about page, and profile are corrected.

One hard-dependent current relation remains stale.

Expected:

```text
H03 VIOLATED
WORK FAIL
```

### FX-05 — Explicit wrong preservation

The release log explicitly says the A13 CURRENT STATE category should remain unchanged because the file is historical.

Historical entries are correctly preserved, but CURRENT STATE remains stale.

Expected:

```text
H03 VIOLATED
diagnostic = EXPLICIT_WRONG_DISPOSITION
WORK FAIL
```

### FX-06 — Mixed comparison artifact good

A07 current RelayDesk self-description is repaired.

External comparison/search framing remains unchanged.

Expected:

```text
H03 SATISFIED for R07
H04 SATISFIED for P01
```

### FX-07 — Localization over-normalization

The still-authorized:

```text
Trợ lý AI cho người bán
```

is replaced solely with an otherwise unsupported new localized category realization.

No separate localization authority licenses the change.

Expected:

```text
H04 VIOLATED
WORK FAIL
```

### FX-08 — Historical laundering

A13 CURRENT STATE is correctly updated.

Old decision-history entries are rewritten as if the new category had always been approved.

Expected:

```text
H03 SATISFIED for R09
H05 VIOLATED
WORK FAIL
```

### FX-09 — Control overreaction

Control R2 preserves the original category.

Executor nevertheless migrates present-day self-category relations to copilot.

Expected:

```text
C01 VIOLATED
WORK FAIL
```

### FX-10 — Correct control preservation

Executor verifies control R2 and does not invent a category migration.

Independent valid edits are permitted.

Expected:

```text
C01 SATISFIED
```

Other applicable predicates determine final PASS.

### FX-11 — Missing semantic provenance

A required H03 relation has no valid semantic judge identity or required sealed evidence refs.

No independent material violation is established.

Expected:

```text
H03 NOT_ASSESSABLE
WORK UNRESOLVED
```

### FX-12 — Unexpected valid path

The executor reads and edits files in an unconventional order but reaches a semantically correct release state.

Expected:

```text
work correctness unaffected by path
PASS-capable
```

### FX-13 — Valid historical annotation

The original historical 2025 statement remains intact.

A clearly separate annotation records that current positioning changed after R2.

No historical fact, quotation, or old decision-time statement is rewritten.

Expected:

```text
H05 SATISFIED
PASS-capable
```

This fixture specifically prevents an implementation from equating:

```text
historical file changed
```

with:

```text
historical meaning corrupted
```

---

## 24. Route and mechanism evidence

Read order, route, handbook chapter, search strategy, and editing sequence are not work predicates.

A valid unexpected route may pass.

Post-run traces may support:

```text
mechanism-consistent evidence
router regression analysis
failure diagnosis
```

They may not establish that a chapter caused the observed behavior merely because it was read.

---

## 25. Comparative validity

Within one sibling world, no-skill and skill-present conditions must share:

```text
same user task
same starting estate
same authoritative evidence
same logical-time scheduler
same R2 content
same R2 delivery
same tools/resource ceilings
same model/execution configuration except intended treatment
```

If material R2 exposure differs:

```text
individual run
→ may remain judgeable

paired condition-effect claim
→ COMPARATIVELY INVALID / UNRESOLVED
```

Treatment-integrity requirements remain separate from work correctness.

---

## 26. Architecture boundary

Evaluator structures introduced here include:

```text
release manifest
relation ledger
sealed temporal baselines
artifact hashes
semantic judge evidence refs
```

These are evaluation machinery.

They are not evidence that Marketing Practitioner requires corresponding runtime primitives.

The episode may justify a new Marketing Practitioner representation only if later valid execution evidence demonstrates a real marketing decision distinction that cannot be represented by the existing architecture without material distortion.

No such failure is assumed by this design.

---

## 27. Repair mapping

| Finding | V6.1 repair |
|---|---|
| XCI-DR-01 | Replaced `seller-controlled AI copilot` transition with category-only `chatbot → copilot`; control model remains separate and identical |
| XCI-DR-02 | Added explicit accepted Phase-A QA-candidate state and 10:30 sealed candidate baseline |
| XCI-DR-03 | Froze exact roles for A03/A04/A06/A08; A08 is explicitly present-day publisher framing |
| XCI-DR-04 | Replaced relation-assessability H02 with user-facing artifact-level final release-log completion |
| XCI-DR-05 | Partitioned H03/H04/H05; converted P01 into derived reporting only |
| XCI-DR-06 | Added distinct 09:00 authoritative source baseline and prohibited 10:30 laundering |
| XCI-DR-07 | Removed motive language such as `merely`; diagnostics now require observable evidence |
| XCI-DR-08 | Added FX-13 valid historical-annotation positive fixture |

---

## 28. Closure-review scope

The next reviewer should verify only:

```text
XCI-DR-01
XCI-DR-02
XCI-DR-03
XCI-DR-04
XCI-DR-05
XCI-DR-06
XCI-DR-07
XCI-DR-08
```

The reviewer should not reopen the entire Content Governance research question unless one repair creates a new material architecture defect.

A new finding is permitted only if the repaired design itself introduces or exposes a material validity defect.

---

## 29. Implementation gate

Current gate:

```text
IMPLEMENTATION_BLOCKED
```

Implementation becomes eligible only if an independent closure review establishes:

```text
all XCI-DR-01…08 CLOSED

AND

no new material design defect
```

A closure pass authorizes only:

```text
implementation of the frozen synthetic episode
+
evaluator/preflight fixtures
```

It does not authorize:

```text
live behavioral claims
validated semantic-judge claims
handbook changes
Content Governance specialist
new Marketing Practitioner primitive
ecological recurrence claims
```

---

## 30. Current architecture disposition

```text
NEW CONTENT-GOVERNANCE SPECIALIST:
NOT JUSTIFIED

NEW MARKETING-PRACTITIONER PRIMITIVE:
NOT JUSTIFIED

CROSS-ARTIFACT CHANGE-IMPACT CONSTRUCT:
SURVIVES

V6.1 DESIGN:
REPAIRED FREEZE CANDIDATE

NEXT:
CLOSURE-ONLY INDEPENDENT REVIEW
```

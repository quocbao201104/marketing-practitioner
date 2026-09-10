# Search-Facing Content Intervention — Independent Review Repair

Status: **POST-REVIEW BOUNDED REPAIR**  
Date: 2026-09-10  
Reviewed candidate: `a36d3441c8e818291333a816c7e0603a9d3fd1f6`  
Independent verdict: `IMPLEMENTATION_REPAIR_REQUIRED`

## 1. Repair scope

The independent review accepted the production Chapter 13 implementation, SD15–SD17 evidence extension, owner boundaries, routing choice, and `SKILL.md` non-change.

The review identified only evaluation-layer defects:

```text
SCI-IPR-01 — invalid SCI03 counterfactual and non-frozen disposition
SCI-IPR-02 — SCI02 / SCI04 / SCI05 change too many material states or expose the diagnosis too directly
SCI-IPR-03 — missing publisher-controlled vs system-surfaced representation control
```

This repair does **not** modify:

```text
Chapter 13 production theory
SD15–SD17 evidence records
SKILL.md
routing-index.json
get-knowledge.py
prior D01–D20 semantics
shared grammar
other specialist chapters
```

## 2. SCI-IPR-01 repair

SCI03 now holds constant:

```text
search phrase: "best CRM for architects"
page identity and page job
resolved CRM-for-architecture-firms category
current H1
requested H1 change
```

Only the existing Chapter 04 claim/proof authorization changes:

```text
SCI03-A
exact superiority claim already authorized
→ REPAIR REPRESENTATION

SCI03-B
superiority claim not authorized
→ KEEP
→ Chapter 04 only if a new superiority claim is genuinely requested
```

`DO NOT INSERT` is no longer a disposition. It is retained only as a forbidden action in the unauthorized arm.

## 3. SCI-IPR-02 repair

SCI02, SCI04, and SCI05 now explicitly declare:

```text
SHARED SEALED STATE
ONLY CHANGED STATE
```

### SCI02

Holds the two URLs, reader, query-overlap symptom, shared baseline content, and requested semantic disposition constant. Only the presence or absence of additional agency-specific decision requirements changes.

### SCI04

Holds the page, page job, page wording, approved product fact, AI-citation symptom, and requested repair decision constant. Only retrieval/support localization evidence changes.

### SCI05

Holds the two regional URLs, unexpected-canonical symptom, discovery context, and requested semantic disposition constant. Only whether current regional state creates independent reader decision utility changes.

Conclusion-bearing labels were reduced in the user-facing prompts; concrete state is used where practical.

## 4. SCI-IPR-03 repair

Added SCI06-A / SCI06-B.

Both arms hold constant:

```text
faithful <title>
faithful H1
faithful meta description
same system-surfaced incorrect title link
same CTR symptom
same page job
```

Only internal-anchor state changes:

```text
SCI06-A
inspected internal anchors are also faithful
→ KEEP / NOT_ASSESSABLE for publisher-side repair

SCI06-B
prominent internal anchors inaccurately say "Home"
→ REPAIR REPRESENTATION on anchor/link context
```

The repair must not claim that the internal anchors caused Google's surfaced title. The publisher-side repair is justified because the anchors themselves misrepresent the target relationship.

## 5. Evaluation-contract repair

`02-targeted-evaluation-contract.md` now:

- requires a `SHARED SEALED STATE` and one `ONLY CHANGED STATE` per pair;
- rejects `either/or` ownership states;
- requires only frozen disposition values in the disposition slot;
- adds SCI06 as the system-vs-publisher representation family;
- strengthens pass criteria against answer-bearing or multi-state counterfactuals.

## 6. Architecture status after repair

```text
NEW CHAPTER                    NOT JUSTIFIED
NEW SHARED PRIMITIVE           NOT JUSTIFIED
NEW CONTROLLER JOB             NOT JUSTIFIED
NEW discovery.intervention     NOT JUSTIFIED
SKILL.md ACTIVATION CHANGE     NOT JUSTIFIED
PRODUCTION THEORY REPAIR       NOT REQUIRED
EVIDENCE REPAIR                NOT REQUIRED
```

The next gate is independent post-repair verification of `SCI-IPR-01` through `SCI-IPR-03` at the new frozen candidate head.

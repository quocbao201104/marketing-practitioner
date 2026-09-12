# Document / Artifact Planning Repair — Targeted Regression Cases

Purpose: verify the bounded repair that generalizes the existing report-planning-and-presentation reference to document-like marketing artifacts without creating a new specialist owner, document ontology, PDF subsystem, or template library.

Repository lineage: repair branch `research/document-artifact-planning-repair`, based on `main@9ba5b3c0940ddb78d7151ad0ce77bc5bf298e232`.

These are targeted routing/behavior cases. They do not establish empirical effectiveness of any document treatment.

## Governing expectations

Keep:

```text
DOCUMENT NOUN != ACTIVATION AUTHORITY
PDF != CAPABILITY BOUNDARY
ARTIFACT USE != FIXED TEMPLATE
VISUAL != DECORATION
WORKBOOK != PROSE + BLANK BOXES
```

The repaired reference should load only when structure, representation, retrieval, or working-use architecture remains materially open.

---

## DAP-01 — supplied guide structure stays direct

**Prompt**

> Here is the approved copy and exact section order for a six-page downloadable guide. Keep the section order and rewrite only the prose for clarity. Do not change the structure.

**Expected behavior**

- Do not load artifact-planning guidance merely because the deliverable is a guide/PDF.
- Use Chapter 04 only if the prose transformation itself needs deeper message/copy guidance; otherwise write directly.
- Preserve the supplied sufficient structure.

**Failure**

- Reopening the artifact contract or proposing a new document architecture without a material reason.

---

## DAP-02 — short reusable reference needs retrieval architecture

**Prompt**

> Turn these approved account-management procedures into a concise reference our team will reopen during customer calls. The facts and procedures are fixed. Decide the structure.

**Expected behavior**

- Activate `references/report-planning-and-presentation.md` even if the artifact is short and never called a report.
- Recognize selective lookup / repeated reference as material use modes.
- Use stable labels, predictable modular units, enough local context, and only the retrieval cues that improve return use.
- Do not force a report-style main-finding narrative.

**Failure**

- Treating navigation as necessary only because of length.
- Producing a linear essay that must be reconstructed on every return use.

---

## DAP-03 — workbook carries reader state forward

**Prompt**

> Using this approved expert material, build a practical workbook for accounting-firm owners deciding whether and how to move upmarket. Do not invent benchmarks, maturity scores, or outcomes.

**Expected behavior**

- Activate artifact-planning guidance because working-use architecture is open.
- Preserve the conditional chain where material:

```text
required input
→ activity / decision / transformation
→ recorded output
→ carried-forward state
→ checkpoint / next dependency
```

- Use prose only where it prepares or interprets the work.
- Create worksheets/exercises only when they perform a real working job.
- Keep unsupported scoring systems out.

**Failure**

- `guide prose + questions + blank boxes` with no usable state transition.
- Inventing a maturity model merely to make the workbook look structured.

---

## DAP-04 — mechanical PDF request does not activate

**Prompt**

> The content and layout are approved. Export this document as a web-optimized PDF and reduce the file size without changing the content or design.

**Expected behavior**

- Do not activate artifact-planning guidance.
- Treat this as ordinary production/tool execution.
- Do not reopen content, message, brand identity, or information architecture.

**Failure**

- Recommending a new outline, page system, lead-magnet structure, or brand treatment.

---

## DAP-05 — domain constrains; domain does not choose layout

**Prompt**

> Create a downloadable guide for accounting-firm owners from these approved claims, examples, and source notes. The guide should help them understand and apply the material. Decide the document structure.

**Expected behavior**

- Activate artifact planning because the document architecture remains open.
- Use the actual reader job, evidence, risk, and delivery constraints.
- Apply accounting/professional-services constraints only when supplied or supported and decision-relevant.
- Do not infer an `accounting PDF style`, mandatory conservative layout, or domain template.

**Failure**

- Routing by industry noun to a fabricated visual convention.

---

## DAP-06 — landing page and downloadable guide keep separate owners

**Prompt**

> The message, proof, price, and brand are approved. Design the information sequence for the landing page and the structure of the downloadable implementation guide it offers.

**Expected behavior**

- Use Chapter 11 for landing-page sequence/allocation.
- Use the document-planning reference for the guide only if its structure/retrieval/working use remains open.
- Preserve shared upstream message/proof state without forcing identical information order across both artifacts.

**Failure**

- Letting document planning absorb landing-page architecture.
- Letting Chapter 11 dictate the guide merely because the guide is linked from the page.

---

## DAP-07 — educational guide is not automatically a specialist case

**Prompt**

> Turn this approved material into a clear educational guide. The audience, learning objective, section sequence, examples, and final action checklist are already supplied.

**Expected behavior**

- Stay on the direct path because the document architecture is sufficiently resolved.
- Do not activate deeper planning solely because the artifact is educational.
- Preserve supported meaning and execute the requested realization.

**Failure**

- Reopening use mode, inventing a framework, or adding exercises because `guide` sounds like a document-planning task.

---

## DAP-08 — representation must earn its job

**Prompt**

> These four options need to be compared on price basis, implementation effort, evidence strength, and material limitations. Build the relevant section of the guide.

**Expected behavior**

- Prefer a comparison representation such as a table when it reduces search/memory burden and the dimensions are genuinely comparable.
- Preserve unknowns and qualifications.
- Do not add decorative cards or invented scores for visual completeness.

**Failure**

- Turning comparable data into several disconnected prose blocks that obscure differences.
- Inventing values, rankings, or decorative visual hierarchy that implies unsupported superiority.

---

## Repair pass criteria

The repair passes this bounded suite when it can distinguish:

```text
supplied sufficient artifact structure
→ DIRECT EXECUTION

open report / guide / reference architecture
→ EXISTING PLANNING/PRESENTATION OWNER

open reader work-through architecture
→ EXISTING OWNER + CONDITIONAL WORKING-ARTIFACT PROCEDURE

mechanical PDF / export work
→ ORDINARY PRODUCTION

landing-page allocation
→ CHAPTER 11
```

The suite must not be used to justify a new `document.*` namespace, new handbook chapter, workbook ontology, domain-document modules, or template library.

# Website Content Audit & Disposition — Evidence Ledger

Status: **CANDIDATE EVIDENCE LEDGER — PRE-IMPLEMENTATION**

Research base: `main@a12bce34666ea7f39c3da46c4e869b2e91cd700e`

This ledger records source scope, what each source can support, what it must not be used to establish, and how the project uses the evidence. Source type and project inferential status are kept separate.

## Project status labels

- **EXTERNALLY SUPPORTED** — conclusion stays within what the external source establishes.
- **PROFESSIONAL PRACTICE** — credible practitioner convention or workflow, not empirical law.
- **PROJECT SYNTHESIS** — repository-created operational structure integrating evidence/practice.
- **CONTEXTUAL HYPOTHESIS** — bounded proposition that remains contingent or validation-sensitive.

## Ledger

### WCA01 — Nielsen Norman Group, Content Inventory and Auditing 101

Source: https://www.nngroup.com/articles/content-audits/

Type: **PROFESSIONAL PRACTICE**

Scope: digital-content inventory/audit practice; not a controlled outcome study.

Supports:

- inventory and audit are distinct activities;
- audit scope can be whole site, subsection, or journey-like bounded set;
- evaluation criteria can include content standards, user needs, organizational goals, and performance data;
- audit may produce keep/update/remove-like actions and identify gaps;
- uncertainty can require further investigation rather than forced certainty;
- human judgment remains necessary beyond automated inventory extraction.

Does not support:

- a universal content-quality score;
- one canonical audit sequence;
- causal claims that auditing improves business outcomes;
- the project's exact disposition taxonomy or closure contract.

Project use: **EXTERNALLY SUPPORTED / PROFESSIONAL PRACTICE** for inventory-audit separation and bounded evaluation; not authority for project-specific ontology.

---

### WCA02 — Digital.gov, Content goals

Source: https://digital.gov/guides/research-collaboration/design-goals/content

Type: **AUTHORITATIVE PUBLIC-SECTOR PRACTICE**

Scope: U.S. government digital-service/content practice.

Supports:

- inventory of website/app content;
- identifying main entry points and tracing user task flow;
- recording ownership/update state and qualitative needed changes;
- identifying gaps, redundancy, outdated content, and content not meeting goals;
- logical relationships between pages/content matter to site mapping and audit work.

Does not support:

- universal commercial-site governance;
- one mandatory task-flow model for every marketing website;
- project-specific cross-object relation taxonomy.

Project use: **EXTERNALLY SUPPORTED within regime** for relationship-aware audit workflow; transfer beyond government is **PROJECT SYNTHESIS**.

---

### WCA03 — Digital.gov, A conversation about content audits

Source: https://digital.gov/2023/09/12/a-conversation-about-content-audits/

Type: **PROFESSIONAL PRACTICE / PRACTITIONER DISCUSSION**

Scope: practical content-audit experience.

Supports:

- audit criteria depend on purpose, audience, goals, and available evidence;
- automated inventory and analytics alone can miss important meaning and even live content with little/no observed traffic;
- qualitative judgment remains necessary.

Does not support:

- mandatory exact audit fields;
- universal scoring rules;
- causal inference from traffic or other metrics.

Project use: **PROFESSIONAL PRACTICE** for anti-score and automation-limit reasoning.

---

### WCA04 — Government of British Columbia, Content inventory and audit

Source: https://www2.gov.bc.ca/gov/content/governments/services-for-government/service-experience-digital-delivery/web-content-development-guides/web-style-guide/content-design/inventory-audit

Type: **AUTHORITATIVE ORGANIZATIONAL PRACTICE**

Scope: Province of British Columbia government web-content practice.

Supports:

- inventories may record page/assets, parent-child relations, related content, dependencies, audience, metadata, status, and dates;
- audits examine accuracy, duplication, relevance, and continuing need;
- practical actions include update, replacement, archive, merge, and keep;
- rationale/history and ownership matter;
- auditors should inspect related content beyond one team's immediate ownership when material.

Does not support:

- a universal relation ontology;
- a mandatory spreadsheet schema for commercial websites;
- automatic merge on topical similarity;
- the project's exact consolidation gate.

Project use: **EXTERNALLY SUPPORTED within regime** for relationship/dependency awareness; successor-viability semantics remain **PROJECT SYNTHESIS**.

---

### WCA05 — GOV.UK, Identify user needs

Source: https://guidance.publishing.service.gov.uk/writing-to-gov-uk-standards/plan-manage-content/identify-user-needs/

Type: **AUTHORITATIVE FIRST-PARTY REGIME GUIDANCE**

Scope: GOV.UK publishing/content-design regime.

Supports:

- content should not manufacture a user need merely to justify an existing solution;
- needs should be supported rather than assumed;
- solution wording can improperly collapse need into implementation.

Does not support:

- every marketing website object must map to a GOV.UK-style task statement;
- legal, record, trust, operational, or other legitimate website functions are invalid unless expressed as a user task;
- `intended function` as a universal industry primitive.

Project use: **EXTERNALLY SUPPORTED within GOV.UK scope** for `CURRENT SOLUTION ≠ USER NEED`; broader `intended function` abstraction is **PROJECT SYNTHESIS**.

---

### WCA06 — GOV.UK, Retire content

Source: https://guidance.publishing.service.gov.uk/writing-to-gov-uk-standards/plan-manage-content/retire-content/

Type: **AUTHORITATIVE FIRST-PARTY REGIME GUIDANCE**

Scope: GOV.UK publishing lifecycle.

Supports:

- retirement is not synonymous with one technical operation;
- update, withdraw, unpublish, replacement, and destination considerations can differ;
- destructive actions should account for continuing access/record needs.

Does not support:

- a universal commercial-site deletion policy;
- `RETIRE` as a universal industry label;
- all uncertain content should be retained.

Project use: **EXTERNALLY SUPPORTED within regime** for `CONTENT DISPOSITION ≠ IMPLEMENTATION OPERATION` and `RETIRE ≠ DELETE URL`.

---

### WCA07 — Google Search Central, Canonicalization

Source: https://developers.google.com/search/docs/crawling-indexing/canonicalization

Type: **AUTHORITATIVE FIRST-PARTY PLATFORM DOCUMENTATION**

Scope: Google Search duplicate/similar URL canonicalization.

Supports:

- multiple URLs may represent duplicate/similar content;
- canonicalization selects a representative URL under Google's search system;
- URL count is not a reliable proxy for independent content-object count.

Does not support:

- a marketing content-consolidation decision;
- semantic redundancy;
- which content should be retained for user/business purposes;
- project ontology beyond the bounded URL/representation distinction.

Project use: **EXTERNALLY SUPPORTED** for `URL ≠ CONTENT OBJECT ≠ REPRESENTATION`; broader object grammar is existing/project architecture.

---

### WCA08 — Google Search Central, Creating helpful, reliable, people-first content

Source: https://developers.google.com/search/docs/fundamentals/creating-helpful-content

Type: **AUTHORITATIVE FIRST-PARTY PLATFORM GUIDANCE**

Scope: Google Search guidance on helpful content and freshness-related practices.

Supports:

- changing dates without substantive updates is not a sound universal freshness tactic;
- adding/removing old content merely to make a site appear fresh is not a sound universal ranking tactic;
- age alone should not be treated as sufficient proof that content needs updating.

Does not support:

- old content never becomes stale;
- Google ranking guidance defines general content value;
- every update decision belongs to Search & Discovery.

Project use: **EXTERNALLY SUPPORTED** for rejection of universal `AGE → UPDATE` heuristics.

---

### WCA09 — Content Design London, How to make a content audit work for you

Source: https://contentdesign.london/blog/how-to-make-a-content-audit-work-for-you

Type: **PROFESSIONAL PRACTICE / PRACTITIONER CRITIQUE**

Scope: content-design audit practice.

Supports:

- traffic alone is insufficient for evaluating content;
- low performance may have alternative explanations such as findability/title problems;
- user need, related content, feedback, search terms, and trends can matter;
- audit can be ongoing maintenance rather than a one-off snapshot.

Does not support:

- one universal audit model;
- causal attribution from traffic;
- the project's exact observation schema.

Project use: **PROFESSIONAL PRACTICE** and counterexample support for `LOW TRAFFIC ≠ LOW VALUE`.

---

### WCA10 — Semrush, How to Perform a Content Audit in 2026

Source: https://www.semrush.com/blog/content-audit/

Type: **VENDOR / PROFESSIONAL PRACTICE**

Scope: SEO/content-marketing audit workflow using search/performance tooling.

Supports:

- a common current SEO-oriented audit workflow;
- practical keep/update/consolidate/delete-like vocabulary;
- practitioner heuristics involving traffic, search performance, age, topical overlap, and gaps.

Does not support:

- universal age thresholds;
- universal content quality;
- automatic consolidation on keyword/topic similarity;
- causal claims from SEO telemetry;
- industry-wide disposition ontology.

Project use: **PROFESSIONAL PRACTICE + ADVERSARIAL COUNTEREXAMPLE SOURCE**. Vendor heuristics are deliberately not promoted to governing rules.

Material contradiction preserved: Semrush's current freshness/age heuristics can conflict with Google's first-party warning against cosmetic freshness tactics. The project does not resolve this by vote; source authority and claim scope govern use.

---

### WCA11 — Brain Traffic, How to audit big websites

Source: https://www.braintraffic.com/blog/how-to-audit-big-websites

Type: **PROFESSIONAL PRACTICE**

Scope: large-site content-audit process.

Supports:

- large audits may require sampling/bounded scope;
- criteria should follow audit goals;
- shared criteria help reduce reviewer drift.

Does not support:

- a universal number of criteria;
- a universal score;
- the project's exact record format.

Project use: **PROFESSIONAL PRACTICE** for scope/criterion discipline.

## Cross-source synthesis

### Externally supported / professional-practice conclusions

- inventory and audit are distinct;
- scope can be bounded and purpose-specific;
- relationships/dependencies can matter to audit decisions;
- performance metrics alone do not determine content value/fate;
- uncertainty may remain unresolved;
- practitioner action families commonly include continue/change/end/combine-like outcomes plus gap identification;
- URL/canonical state is not equivalent to content-strategy identity;
- age alone is not a universal update requirement.

### Project synthesis

- `intended function` as the broad audit variable above narrower user-need formulations;
- working-subject fast path;
- selected cross-subject comparison dimensions;
- consequence-sensitive disposition reasoning;
- semantic disposition functions used by this track;
- successor/survivor viability gate;
- finding → owner-specific repair → closure contract;
- integration with current Marketing Practitioner owners without a new controller job.

### Not established

- that the candidate improves marketing outcomes;
- that these exact fields or distinctions are universally necessary;
- that one sequence is optimal;
- that one disposition vocabulary is canonical;
- that a new global primitive or controller job is needed;
- that implementation will improve agent work;
- that route activation or runtime efficacy has been demonstrated.

## Freshness rule

Before implementation or later platform-specific claims rely on a current provider behavior, recheck the relevant first-party source. Stable conceptual/practitioner claims should not be mechanically refreshed merely because a source is old; refresh when changed conditions can alter the decision.
# Report Planning and Presentation

Use for marketing reports, research syntheses, and decision briefs when their information architecture or presentation needs deliberate design. This is an operating contract, not evidence that one layout improves business outcomes. It applies across Markdown, HTML, PDF, and slides; adapt to the requested medium without changing the evidence or adopted decisions.

Contents: [working plan](#working-plan), [decision boundaries](#decision-boundaries), [report contract](#report-contract), [representation choices](#representation-choices), [HTML delivery](#html-delivery), [examples](#examples), [source scope](#source-scope).

## Working plan

Apply the controller's materiality, delegation, and uncertainty rules. Planning organizes execution; a checkpoint resolves missing material input or decision authority under the request and retained context. Do not make a separate plan document unless it improves review or continuation, or the user requests one. A plan is not the final report unless planning itself is the requested job.

Consider these six dimensions, exposing only what helps the user understand or revise the approach. Already supplied answers need no reconfirmation.

| Dimension | Useful content |
| --- | --- |
| Purpose | Who will use the report, in what context, and for what understanding or decision? |
| Questions | Which questions must be answered, and which are outside scope? Exploratory questions may evolve after a bounded inspection. |
| Information architecture | Which sections are needed, what question or reader function each serves, and how the sequence builds understanding. |
| Evidence plan | What is available, what must be retrieved or analyzed, and which gaps could change the answer. |
| Presentation plan | Which comparisons or relationships need prose, tables, charts, diagrams, or interaction, and why. |
| Completion and checkpoints | What makes the result useful and sufficiently supported; any unresolved material choice requiring user input or decision authority, and the work that depends on it. |

Use a short outline with section purposes when that makes direction reviewable. Do not substitute decorative choices such as hero colors or card counts for the report's content architecture. Resolve ordinary rendering details within the brief and available design capabilities.

## Decision boundaries

Materiality follows the controller: a change in audience, scope, research question, method, positioning, channel, architecture, or commitment matters only when it changes the result or consequential downstream work. These labels do not determine decision authority. Establish whether the request and retained context authorize the agent to choose; do not infer that a topic inherently requires user approval.

- **Sufficient direction:** announce a working plan if useful, then execute. Do not end the turn merely to invite approval.
- **Delegated choice:** investigate enough to choose within scope, retain the choice and its limits, then continue. A recommendation remains a recommendation where adoption was not delegated.
- **Material input or authority still needed:** inspect enough context to recommend a concrete direction and explain the consequence of choosing otherwise. Ask only for the missing decision; wait on dependent work while continuing reusable research or other independent work.

Approval of an outline does not verify its factual assumptions or authorize publication, spending, or other external commitments. Follow the actual authorization for each action. New evidence may require revising a conclusion; preserve unaffected decisions and ask again only if a material choice remains unresolved and the available input or decision authority is insufficient.

## Report contract

Organize around the reader's questions rather than the chronology of research or the internal routing process. A decision brief may lead with a recommendation; an exploratory synthesis may lead with its question and supported findings. Neither requires an invented commercial recommendation.

The finished report should let its reader:

- Identify the subject, scope, intended use, and period where relevant without needing the surrounding chat.
- Find the main answer or findings, then inspect the reasoning and evidence that support them. Distinguish observation, interpretation, assumption, and recommendation where confusing them would change meaning.
- Trace consequential claims and figures to identifiable sources or supplied data. Preserve relevant population, period, units, method, and uncertainty close enough to prevent misinterpretation; deeper provenance can live in an appendix.
- Understand material counterevidence and limitations at the point where they qualify a conclusion. Do not bury them behind a disclosure or in an unrelated footnote.
- Compare alternatives on relevant common criteria when a choice is requested, and understand the recommendation's trade-off or why the evidence does not yet distinguish them.
- Know what follows from the report, including a justified no-action result or an evidence limit. Do not force a CTA into an informational report.

These are functions, not required headings. Preserve a sufficient supplied outline, and change it only when needed to complete the job truthfully. Visual finish cannot compensate for missing answers, fabricated evidence, or unsupported certainty.

## Representation choices

| Form | Use when | Preserve |
| --- | --- | --- |
| Prose | Explaining an argument, qualification, mechanism, or recommendation | Connected reasoning; headings that describe the actual content |
| Table | Readers need exact lookup or comparison on common dimensions | Units, comparable definitions, clear headers, and meaningful unknowns rather than invented scores |
| Chart | A supported quantitative pattern is easier to inspect visually | Traceable data, labeled units and scales, comparable periods, and uncertainty where material; never manufacture values for visual completeness |
| Diagram | Structure, dependencies, sequence, or relationships are the subject | Clear meanings for arrows and groups; a proposed flow must not look like an observed causal result |
| Cards or callouts | A few independent findings need separate emphasis | Enough context and qualification; do not fragment a connected argument into decorative tiles |
| Disclosure or tabs | Secondary detail would otherwise interrupt reading | The main answer and interpretation-changing qualifications remain available; hidden content is discoverable and accessible |
| Interactive controls | Exploring scenarios, filtering, or changing assumptions helps answer the question | Visible input assumptions and scope, labeled modeled outputs, and a useful default state |

Choose the simplest form that improves the reader's task. Keep terminology, units, visual encodings, and hierarchy consistent within the artifact; do not impose an identical layout across different reports.

## HTML delivery

Use the host's available implementation or design capabilities when useful. This skill owns content, evidence, and decision usefulness; it does not require a framework, component library, hosting service, or another installed skill.

- Use meaningful document structure, descriptive headings in logical order, and navigation when the report's length warrants it. Keep reading order coherent independently of visual columns. See [WAI page structure](https://www.w3.org/WAI/tutorials/page-structure/).
- Provide text equivalents for information-bearing visuals. A complex chart or diagram needs access to its essential values, relationships, and conclusions, not just a generic image label. See [WAI complex images](https://www.w3.org/WAI/tutorials/images/complex/).
- Let ordinary content reflow on narrow screens and at zoom without loss of information or controls. Where a table or diagram requires two-dimensional layout, contain its scrolling rather than forcing the whole report sideways. See [WCAG reflow guidance](https://www.w3.org/WAI/WCAG22/Understanding/reflow.html).
- Make implemented controls operable by keyboard, with meaningful labels and visible focus. Do not rely only on hover or color to expose information. Check applicable contrast and interaction requirements against [WCAG 2.2](https://www.w3.org/TR/WCAG22/) when implementing; this short contract is not a complete conformance checklist.
- Match delivery to use: a local file, hosted page, or printable report has different asset and interaction dependencies. Do not deploy simply because HTML was requested. When offline sharing is required, avoid essential remote dependencies; when print/PDF use matters, preserve findings, visual explanations, and sources in print rather than losing them inside collapsed panels.

Validate the actual artifact with the capabilities available: check claims and data against sources, links and assets, reading order, narrow and wide rendering, and implemented interactions. Inspect print output when it is part of delivery. State material checks that could not be performed; source inspection or a screenshot alone does not establish accessibility conformance.

If a renderer, scripting, network access, or an asset is unavailable, preserve a useful static narrative and accessible evidence representation where feasible. Do not silently substitute Markdown for requested HTML or imply a preview was tested. Identify the remaining delivery limitation and complete the supported portion.

## Examples

**Resolved HTML report:** "Use this outline and dataset to write an HTML market report." Check data sufficiency, state a brief implementation plan if useful, and build. The format and size do not create a review gate. Ask only if a material ambiguity remains, such as incompatible definitions that change the main comparison.

**Delegated launch recommendation:** "Research the market and recommend a launch strategy; choose the best approach." Investigate, compare viable directions, recommend one, and complete the requested report. Keep unsupported assumptions visible. Do not ask the user to do the strategic selection that was delegated; a recommendation does not authorize launching campaigns.

**User reserves a direction:** "Research both segments, then let me choose before you build the full launch report." Complete the comparison and recommend a segment with the decisive trade-off. Ask for that selection before segment-dependent strategy and production. Continue common market evidence work while waiting; do not treat silence as a selection.

**Small but material:** "Send this short announcement" with two conflicting launch dates and no authoritative resolution. Its length does not eliminate the need to resolve the date before sending. Prepare supported wording while clarifying the date and preserving the actual sending authorization.

## Source scope

The linked W3C sources support the HTML accessibility guidance, consulted 2026-09-08. Planning, decision ownership, and the report contract are repository design rules derived from the existing controller and the requested behavior; they are not presented as empirically validated interventions. Assess live agent behavior separately from static package checks.

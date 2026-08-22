# Runtime Architecture Complexity Stress — v0.1.4 Candidate

Status: frozen complexity baseline. Run against v0.1.3 before implementing a lean-core candidate.

Purpose: test instruction interference, stage contamination, and resource-selection behavior under larger multi-mode jobs with relevant and irrelevant context mixed together.

Run each case in a fresh chat. Use the same model for the whole baseline pass.

Common execution header:

```text
Repository:
https://github.com/quocbao201104/marketing-practitioner-skill

Use the skill implementation from branch:
audit/runtime-architecture-v0.1.4

Treat:
skills/marketing-practitioner/SKILL.md
as the governing skill instructions.

Read supporting handbook/framework files only when SKILL.md routes you to them or they are materially required by the task.

Open:
evals/runtime-architecture-v0.1.4-complexity.md

Run only the named case.
Do not inspect other cases.
Do not modify the repository.
Do not explain the benchmark.
Return exactly the task output that a user would receive.
```

---

# CASE C1 — Research → positioning → social copy under mixed evidence

## SOURCE MATERIAL

Product: SignalShelf

Product facts:
- SignalShelf is an open-source local workspace for inspecting LLM-agent runs.
- It shows run steps, tool calls, tool inputs, tool outputs, timestamps, and completion status.
- It supports side-by-side comparison of two runs.
- It stores run data locally on the user's machine.
- Python only.
- MIT licensed.
- Repository: https://github.com/example/signalshelf
- It does not execute agent tools on the user's behalf.
- It is not an authorization or policy-enforcement system.
- It is not a hosted observability platform.
- It does not currently support JavaScript/TypeScript runtimes.

Exploratory interviews:
- Interview A: a solo Python developer said raw logs were hard to scan after multi-step tool use and liked the side-by-side run comparison.
- Interview B: an ML engineer said the visual step view made failures easier to follow, but still wanted direct access to raw logs.
- Interview C: an infrastructure engineer said they preferred terminal logs and would not add a visual layer to their workflow.
- Interview D: an agent-framework maintainer liked timestamped tool-call inspection but said the current Python-only scope would block adoption for their TypeScript-heavy team.
- Interview E: a data scientist said they mainly cared about reproducing tool inputs/outputs and did not care about visual presentation.

Research boundaries:
- Five interviews are exploratory and do not establish market prevalence.
- No evidence shows that developers generally prefer visual debugging.
- No benchmark establishes faster debugging or fewer failures.
- No adoption, retention, conversion, or productivity data are available.
- No testimonial may be quoted unless supplied verbatim above.

Repository / implementation notes:
- The repository includes a detailed architecture note.
- The repository includes a testing guide.
- The repository includes contribution guidelines.
- The repository includes an MIT license file.
- The side-by-side comparison implementation uses a local SQLite database.
- The UI has filters for tool name and completion status.
- The repository has no published performance benchmark.
- The repository has no independent security certification.
- There is no roadmap commitment for TypeScript support.

TASK

Reader:
Python developers building or debugging local AI-agent workflows who follow the author's personal technical Facebook account.

Context:
The post is a casual project share, not a launch announcement, research report, security review, or purchasing decision.
Readers can inspect the repository if they want implementation details.

Goal:
Write a useful, natural Facebook post that makes the right readers curious enough to inspect the repository.

Before writing, resolve the strongest defensible positioning from the evidence supplied.

Task:
Write the final Facebook post only.

Do not include a strategy section.
Do not invent claims or social proof.

---

# CASE C2 — Funnel diagnosis → experiment decision → stakeholder update

## SOURCE MATERIAL

Product: TeamRoute

Business context:
- TeamRoute is a B2B workflow-routing SaaS product.
- The growth team is deciding what to investigate before changing the signup funnel.
- The sales team has separately requested stronger enterprise messaging on the landing page.
- The product team recently changed the mobile signup experience.

Observed metrics:
- Trial signup conversion fell from 7.9% to 5.8% week over week.
- Landing-page sessions increased by 4%.
- Desktop conversion changed from 8.1% to 8.0%.
- Mobile conversion changed from 7.6% to 4.3%.
- Mobile traffic share increased from 38% to 57%.
- Paid-search traffic increased substantially.
- Organic traffic volume was approximately unchanged.
- One paid-search campaign began targeting a broader set of keywords during the second week.
- A redesigned mobile signup form shipped at the beginning of the second week.
- The redesign reduced the form from six visible fields to four visible fields, with two fields moved behind a later step.
- A client-side analytics library was also upgraded during the second week.
- No controlled experiment was run.
- No instrumentation audit has yet been completed.
- No evidence establishes whether the form redesign, traffic mix, analytics change, or another factor caused the decline.

Qualitative evidence:
- Two sales calls from the second week included prospects asking about SSO and audit logs.
- One existing customer asked whether TeamRoute planned to support regional data residency.
- Support volume was stable.
- No systematic customer research was conducted on the landing-page headline.

Current landing-page headline:
"Route work to the right team without the spreadsheet chaos."

Sales request:
Replace it with:
"Enterprise workflow automation built for secure, scalable operations."

Experiment constraints:
- Engineering can support one targeted diagnostic test this week.
- The team should avoid changing multiple variables before understanding the current decline.
- A temporary rollback of the mobile form is technically possible.
- Paid-search campaign targeting can be segmented in analytics if the instrumentation is reliable.

TASK

Reader:
Growth lead, product manager, and engineering lead.

Goal:
Decide what should happen this week.

Task:
Prepare a concise internal decision memo that:
1. diagnoses where the conversion decline is concentrated;
2. separates established facts from plausible explanations;
3. recommends the single highest-value next discriminating check or test;
4. states whether to change the landing-page headline now;
5. addresses the sales team's enterprise-message request only to the extent justified by the supplied evidence;
6. identifies what the team can conclude now and what remains unknown.

Do not provide replacement headline copy unless changing the headline now is justified.

---

# CASE C3 — Existing positioning → localization decision → market-facing adaptation

## SOURCE MATERIAL

Product: DeskRelay

Global positioning currently used in the home market:
- Target: small support teams handling customer requests across email and chat.
- Current alternative: shared inboxes, spreadsheets, and manual assignment.
- Primary value: reduce manual routing and make ownership visible.
- Reason to believe: rules-based assignment, ownership status, and shared queue visibility are present in the product.
- Trade-off: the product is intentionally simpler than full enterprise contact-center platforms.

Product facts:
- DeskRelay supports email and web chat.
- It supports rule-based routing by queue, tag, and business hours.
- It supports English and Spanish interfaces.
- It supports USD and EUR billing.
- It does not provide voice/call-center functionality.
- It does not provide workforce-management forecasting.
- It does not provide built-in WhatsApp integration.
- It can integrate with third-party systems through webhooks.
- Data is hosted in the EU for the market considered below.
- No local reseller network exists.

Target market:
Spain.

Local exploratory evidence:
- Interview 1: a five-person ecommerce support team uses Gmail labels and a shared spreadsheet for assignment; the manager complained mainly about unclear ownership during busy periods.
- Interview 2: a twelve-person SaaS support team already uses a larger helpdesk platform and said switching would require a clear cost or workflow advantage.
- Interview 3: a six-person retailer said WhatsApp is important in customer communication, but their current support process still routes formal cases through email.
- Interview 4: a four-person service business said they wanted something simpler than their current helpdesk and cared about setup effort more than analytics depth.
- Interview 5: an eight-person marketplace team said EU hosting was a positive requirement but not a primary buying reason.

Local evidence boundaries:
- Five interviews are exploratory and do not establish prevalence in Spain.
- The interviews do not establish that Spanish support teams generally prefer simpler tools.
- No pricing study has been conducted.
- No quantitative evidence establishes WhatsApp usage prevalence in the target segment.
- No local conversion or campaign data exist yet.

Additional market/context notes:
- The product interface is already available in Spanish.
- Billing in EUR is supported.
- Legal and privacy copy has been reviewed separately for the EU deployment.
- The team is considering whether the Spain landing page should lead with EU hosting, simplicity, routing clarity, or WhatsApp-related messaging.
- The product does not have built-in WhatsApp integration.
- No promise should imply a capability that does not exist.

TASK

Reader:
A small support-team manager in Spain evaluating whether DeskRelay could replace a shared inbox/manual assignment workflow.

Goal:
Adapt the existing positioning for a Spain landing-page hero without inventing a new market narrative from five interviews.

Task:
Return:

POSITIONING DECISION
- Maximum 5 concise bullets explaining what should remain invariant globally and what, if anything, should adapt for this market.

HERO
- One headline.
- One supporting sentence.
- One CTA.

Do not add sections beyond these.
Do not claim Spanish-market prevalence.
Do not imply built-in WhatsApp support.

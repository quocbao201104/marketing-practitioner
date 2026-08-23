# Task Specification Guide

You do not need to learn prompt engineering to use Marketing Practitioner well.

The useful question is not:

> How do I write an impressive prompt?

It is:

> What does the agent need to know so it solves the right task without materially guessing what I meant?

Research on prompt underspecification supports both sides of this problem: omitted requirements can make behavior fragile, but simply adding every possible requirement does **not** reliably make the result better [TS01]. Research on irrelevant and long context also gives no basis for “give the model everything” as a default [TS04][TS05][TS06].

The practical rule is:

```text
MINIMUM SUFFICIENT TASK SPECIFICATION
=
THE JOB
+
ONLY THE QUALIFIERS THAT CAN MATERIALLY CHANGE THE RESULT
```

That is a sufficiency rule, not a completeness contest.

---

## 1. Start with the job

State what you need the agent to do **now**.

Prefer the open decision, requested transformation, or artifact over a broad aspiration.

Too broad:

```text
Improve this landing page.
```

More decision-relevant:

```text
Rewrite the hero so a new visitor can understand the product more quickly.
Do not change the approved positioning.
```

The second request tells the agent both what is open and what is not.

A useful job statement usually answers one of these questions:

- What should be changed?
- What decision is still open?
- What should be diagnosed, compared, researched, written, or adapted?
- What would count as a useful result from this turn?

You do not need to name the internal marketing method. “Help me decide which customer group to focus on” is enough; you do not need to know the term `ICP`.

---

## 2. Add only the qualifiers that can change the answer

The original seven-part grammar is too rigid for ordinary use. The research supports a smaller model with one required core and several conditional qualifiers.

| Part | Use it when... | What it prevents |
| --- | --- | --- |
| **What I need** | almost always | solving the wrong job |
| **Use** | the task depends on supplied facts, evidence, or an existing artifact | inventing or substituting material |
| **Keep fixed** | something is already approved, verified, forbidden, or outside scope | reopening resolved decisions or changing protected facts |
| **Relevant context** | audience, platform, market, surface, timing, or environment can change the decision | producing an answer for the wrong situation |
| **Return** | the useful output is not already obvious from the job | giving the wrong artifact, granularity, or visible structure |
| **If something important is missing** | the cost of guessing matters | silently choosing a materially different interpretation |

These are not six boxes that every prompt should contain.

**DELETE THE SECTIONS YOU DO NOT NEED.**

A one-line transformation can be perfectly specified. A diagnosis or positioning decision may need more.

### Why `Keep fixed` combines resolved state and constraints

“Already decided” and “must not change” often have the same practical effect: they remove something from the open decision space.

For example:

```text
Audience is already approved.
Positioning is fixed.
Do not add new product claims.
```

All three tell the agent what it should **not** re-decide while doing the current job.

Keep them separate in ordinary language when that makes the instruction clearer, but you do not need two mandatory template sections.

### Why `Return` is conditional

The output is often already part of the job:

```text
Give me one title under 60 characters.
```

There is no benefit in repeating the same requirement under another heading.

### Why examples are not a field

Examples can steer model behavior, but demonstration selection and ordering can also bias what the model infers from them [TS10]. Provider guidance likewise treats examples as useful steering devices rather than evidence that every task needs them [TS11][TS12][TS13].

Use an example when the intended pattern, style, edge case, or boundary is hard to communicate more directly.

```text
Match the level of specificity in this example, not its sentence structure.
```

That sentence can be more useful than supplying five examples and hoping the agent infers which properties matter.

---

## 3. Copy-paste starter

Use this only when it helps you think. Remove anything that does not matter to the current task.

```text
What I need:
[the decision, transformation, diagnosis, research task, or artifact]

Use:
[the material, current artifact, verified facts, or evidence the agent should rely on]

Keep fixed:
[approved decisions, verified claims, required facts, or things that must not change]

Relevant context:
[audience / platform / market / surface / timing — only if it can change the answer]

Return:
[the output you actually want]

If something important is missing:
[ask me / flag it / make a bounded version / research it if appropriate]
```

Again:

**DELETE THE SECTIONS YOU DO NOT NEED.**

The goal is not to fill the template. The goal is to remove material ambiguity from the task.

---

## 4. Tell the agent what it can rely on

When factual accuracy matters, distinguish the material from the conclusions you want drawn from it.

Useful ordinary-language boundaries include:

```text
These product facts are verified.
```

```text
These are customer comments, not a representative survey.
Do not turn repeated comments into population prevalence.
```

```text
These metrics are observations.
Do not assume the launch caused the change.
```

```text
Use the supplied product information for claims.
If a specification is missing, flag it instead of inventing it.
```

You do not always need a blanket “use only what I gave you.” Sometimes outside research is exactly what the task needs. State the boundary that matters:

```text
Use the interviews as the evidence for customer claims.
You may research current competitor information separately and label it as external research.
```

The important distinction is:

```text
SUPPLIED MATERIAL
≠ AUTOMATICALLY VERIFIED FACT
≠ PERMISSION TO INVENT MISSING FACTS
```

If some inputs are observations, assumptions, hypotheses, seller-declared facts, or verified facts, label them when that distinction changes what the agent may claim.

---

## 5. Preserve decisions that are already resolved

A capable agent can still solve the wrong problem if it treats every upstream decision as open.

If a decision is fixed and reopening it would change the task, say so.

```text
The audience and offer are already approved.
Only adapt the message for LinkedIn.
```

```text
The product facts below are verified.
Improve the listing representation; do not redesign the product or invent benefits.
```

```text
We have already decided to keep the current CTA.
Diagnose the drop before recommending a new one.
```

You do not need to restate every historical decision. Include only resolved state that constrains the current job.

---

## 6. Separate decision constraints from formatting

Some constraints change the decision itself:

- what may or may not change;
- which claims are allowed;
- which audience is in scope;
- required evidence;
- legal, ethical, policy, compatibility, or variant boundaries;
- a fixed positioning, offer, message, or product fact.

Others mainly change presentation:

- word count;
- number of options;
- table versus prose;
- title only versus explanation;
- tone and surface-level style.

Both can matter, but they are not equivalent.

```text
Return one title only.
```

controls visible output. It does not tell the agent which product claim is justified.

```text
Do not claim waterproofing; that specification is not verified.
```

changes what the agent is allowed to decide and say.

Do not let formatting instructions stand in for decision criteria.

---

## 7. Give relevant context, not maximum context

More context is not automatically better context.

Controlled research shows that irrelevant information can distract models [TS04], relevant information can be used unevenly inside long inputs [TS05], and input length can reduce performance even when retrieval is not the bottleneck [TS06]. These studies do not establish a universal maximum prompt length, but they do reject “include everything just in case” as a safe general rule.

Before adding background, ask:

> Could this information materially change the decision, evidence boundary, constraint, or output?

If not, leave it out unless the agent specifically needs it later.

### Missing context

Add it when the answer can change materially without it.

Example:

```text
Adapt this for social media.
```

may be underspecified if LinkedIn versus TikTok would require materially different representations.

### Relevant context

Include audience, platform, market, surface, timing, account state, product variant, or other environment when it affects the job.

### Redundant context

Do not repeat information already obvious from the artifact or conversation unless the repetition protects an important boundary.

### Conflicting context

Surface the conflict rather than burying it in more prose.

```text
The brief says the audience is enterprise teams, but the approved campaign note says freelancers.
Treat that as unresolved; do not silently choose one.
```

### Excessive context

When a large body of material is genuinely required, identify which parts are authoritative and what the agent should do with them. Context capacity is not the same as task clarity.

---

## 8. Decide what should happen when information is missing

Do not use “always ask a clarifying question.” Research on clarification supports a conditional policy: asking can help when plausible interpretations produce different useful answers, but clarification also has a cost and is unnecessary when one interpretation is dominant or a useful response can proceed safely [TS07][TS08]. Current models can also miss ambiguity rather than reliably detecting it themselves [TS09].

Use this decision rule:

| Missing information | Good default |
| --- | --- |
| The detail is low-impact, conventional, reversible, and does not change a claim or strategic decision | infer conservatively if needed |
| A useful answer remains valid across the plausible interpretations | proceed with a bounded answer and flag the uncertainty if material |
| The uncertainty changes confidence but does not block useful work | state the uncertainty |
| A factual claim/specification is unsupported by the supplied evidence | do not invent it; flag the gap |
| The missing fact is external, current, and researchable, and outside research is allowed or expected | research it and distinguish external evidence from supplied evidence |
| A user-specific choice, permission, approved state, or materially different interpretation determines the correct action | ask the user |

The question is not “Is anything missing?” Almost every real task is incomplete in some way.

The question is:

> Would choosing the wrong value for this missing information materially change the job, decision, claim, or action?

If yes, do not silently guess it.

---

## 9. Ask for the output you will actually use

Reasoning depth and visible answer length are different things.

You can ask for:

```text
One title only.
```

or:

```text
Return:
1. the leading explanations;
2. evidence for and against each;
3. the next discriminating check.
```

The first request should not force shallow reasoning. The second does not require the agent to expose private chain-of-thought. Ask for the **decision, evidence, trade-offs, uncertainty, or checks** you need to see.

Current provider guidance consistently supports being explicit about the desired output and constraints, while model-specific advice about roles, XML, internal thinking prompts, or example counts varies [TS11][TS12][TS13].

---

## 10. When examples help

Examples are useful when they communicate something that is difficult to specify directly, such as:

- a distinctive voice;
- a non-obvious format;
- an edge case;
- the difference between acceptable and unacceptable claims;
- the intended granularity of an analysis.

Examples are less useful when the task is already unambiguous.

For a simple rewrite, this is enough:

```text
Shorten this to under 80 words. Keep the same message and claims.
```

Do not add examples merely to make the prompt look sophisticated.

When an example contains many incidental properties, tell the agent which property matters:

```text
Use this as a tone reference only. Do not copy its structure, claims, or CTA.
```

That protects against the common failure:

```text
EXAMPLE
≠ RULE
```

---

## 11. Progressively richer examples

### Very small transformation

```text
Shorten this Facebook post to under 80 words.
Keep the same message and claims.

[paste post]
```

That is already sufficient when the message and claims are resolved. A six-section template would add ceremony without changing the task.

### Customer research / synthesis

```text
What I need:
Synthesize these reviews and interview notes to understand recurring problems,
alternatives, desired outcomes, contradictions, and useful customer language.

Use:
The supplied reviews and interviews. Treat them as qualitative evidence,
not a representative sample.

Keep fixed:
Do not turn recurrence in this material into population prevalence.
Separate direct evidence from interpretation.

Return:
The main patterns, evidence for each, contradictions, and what remains unknown.

[paste material]
```

The important specification is the evidence boundary, not marketing terminology.

### Positioning / decision task

```text
What I need:
Decide which positioning direction is best supported for the next landing-page test.
The positioning decision is still open.

Use:
Verified product facts, the customer interviews below, and the current alternatives customers mention.

Keep fixed:
The product itself and pricing are not changing.
Do not invent customer priorities that are not supported by the material.

Relevant context:
This page is for first-time visitors from paid search.

Return:
Two credible positioning options, evidence and trade-offs for each,
a recommendation if the evidence supports one, and the most important unresolved question.
```

Here the decision is open, so telling the agent only “write better copy” would prematurely skip the strategic question.

### Copy / adaptation with resolved state

```text
The audience, message, offer, proof, and CTA below are already approved.
Adapt the supplied copy for LinkedIn.
Do not reopen the positioning or add new claims.
Keep the result under 120 words.

[paste approved material]
```

The resolved state matters because the job is adaptation, not strategy reconstruction.

### Commerce / product listing

```text
What I need:
Improve this Shopee listing so the product is easier to understand and resolve.

Use:
The verified product facts and current listing below.

Keep fixed:
Do not invent benefits, specifications, compatibility, certifications, or variant facts.
Preserve distinctions between variants.

Return:
A revised title and product-information copy, plus any decision-critical product information that is still missing.

[verified facts]
[current listing]
```

The platform matters; invented product truth is not an acceptable way to make the listing look complete.

### Diagnosis

```text
What I need:
Diagnose why signup conversion fell before we change the page.

Observed:
- conversion fell from X to Y;
- mobile share increased;
- desktop conversion was roughly stable;
- mobile conversion fell;
- a new mobile form shipped;
- paid-search mix also changed.

Keep fixed:
No controlled experiment was run.
Do not assume either change caused the decline.

Return:
The leading competing explanations, evidence for and against each,
and the next check that best discriminates between them.
```

The key specification is causal restraint plus the desired diagnostic output.

### Conversational product discovery

```text
What I need:
Make this product information easier for a conversational shopping agent
to resolve against a shopper's requirements.

Use:
Verified product facts, compatibility constraints, variant definitions,
current price/availability information, and the current product page.

Keep fixed:
Do not invent compatibility or product capabilities.
Do not guess hidden model weights, ranking weights, or keyword formulas.

Return:
1. missing decision-critical product information;
2. ambiguous or conflicting variant/compatibility information;
3. a clearer product-information version using only supported facts.
```

The goal is information completeness and resolvability, not imagined optimization against an opaque model.

---

## 12. Common task-specification failures

| Failure | Better rule |
| --- | --- |
| `PROMPT WORDING = USER INTENT` | Wording is only a representation of intent. State the actual job when multiple interpretations matter. Prompt sensitivity exists, but its magnitude varies by model, task, and evaluation [TS02][TS03]. |
| `LONGER PROMPT = BETTER PROMPT` | Add requirements only when they can change the result [TS01]. |
| `MORE CONTEXT = BETTER CONTEXT` | Prefer relevant, authoritative, decision-changing context [TS04][TS05][TS06]. |
| `MISSING TASK-DEFINING INFORMATION = PERMISSION TO SILENTLY GUESS` | Ask, research, flag, or bound the answer when the missing value could materially change the job or claim [TS07][TS08][TS09]. |
| `EXAMPLE = RULE` | Say which property of the example matters; examples can introduce unintended patterns [TS10]. |
| `OUTPUT FORMAT = DECISION CRITERIA` | Format controls presentation; factual, strategic, and evidence boundaries control what answer is justified. |
| `RESOLVED INPUT = INVITATION TO REDECIDE IT` | Mark fixed upstream decisions when reopening them would change the current job. |
| `SPECIFICITY = INVENTED PRECISION` | Be specific about the task, not about facts you do not actually know. |

---

## 13. What this guide deliberately does not recommend

It does not recommend:

- “Act as a world-class expert” as a default;
- XML or Markdown as a universal quality hack;
- asking for chain-of-thought;
- always supplying examples;
- always asking a clarifying question;
- filling every template field;
- giving the agent every document you possess;
- making prompts longer for their own sake;
- model-specific magic phrases as durable marketing practice.

Current provider documentation contains useful model-specific structure and syntax advice, but those details do not survive as universal user-interface requirements [TS11][TS12][TS13].

---

## 14. The shortest useful rule

When you are unsure what to include, start here:

```text
Tell the agent what you need now.
Give it the material that matters.
Mark anything important that is already fixed.
Add only context or constraints that can change the result.
Say what you want back if it is not obvious.
Tell it how to handle missing information when guessing would matter.
```

Then delete whatever the task does not need.

The objective is not a perfect prompt.

The objective is a sufficiently specified task.

---

## Research basis and limits

The strongest direct source for this guide is Yang et al. (Findings of ACL 2026), which finds both a real underspecification problem and evidence against naive “specify everything” prompting [TS01]. The context guidance is further bounded by controlled work on irrelevant and long inputs [TS04][TS05][TS06]. Clarification guidance comes from work that explicitly studies when interactive clarification is useful and from evidence that ambiguity handling remains imperfect [TS07][TS08][TS09]. The treatment of examples is bounded by research on demonstration bias [TS10]. Prompt sensitivity is represented with both positive evidence and a recent methodological counterpoint rather than as a universal law [TS02][TS03].

Current first-party guidance from OpenAI, Anthropic, and Google is used only where it converges on general task-specification principles such as clear tasks, relevant context, explicit constraints, examples when useful, and visible output requirements. Vendor-specific syntax and model behavior are not promoted into universal rules [TS11][TS12][TS13].

See [`references/task-specification-evidence.md`](references/task-specification-evidence.md) for source details and evidence boundaries.
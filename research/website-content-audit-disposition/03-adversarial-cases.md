# Website Content Audit & Disposition — Adversarial Cases

Status: **FROZEN PRE-IMPLEMENTATION PRESSURE SET**

These cases test the theory candidate. They are not runtime evidence and do not prove efficacy. Several are deliberate negative controls where existing Marketing Practitioner owners should remain primary.

Each case records the tempting shortcut, material distinction, expected work, forbidden inference, existing owner(s), and what would count as theory failure.

## WA-P01 — Low traffic, legitimate function

### Fixture

A security/privacy page has very low traffic and no directly attributed conversions. Enterprise sales repeatedly sends it to prospects during procurement. The content is accurate and current.

### Pressure

```text
LOW TRAFFIC
→ LOW VALUE
→ RETIRE
```

### Material distinction

Observed traffic is not the same as legitimate function, business/decision support, or content value.

### Expected work

- preserve traffic as an observation;
- establish the supplied procurement/trust function and authority if adequately supported;
- do not infer removal from traffic alone;
- retain or repair only if supported by the bounded audit question.

### Forbidden inference

`LOW TRAFFIC → NO NEED / NO VALUE / REMOVE`.

### Existing owners

Chapter 05 for causal/performance interpretation if needed; Chapter 13 for discovery state if findability is material.

### Theory failure

The audit model requires low traffic to imply a negative disposition, or cannot preserve a legitimate low-volume function.

---

## WA-P02 — Same topic, different functions

### Fixture

`/pricing` supports prospective buyers comparing plans and terms. `/help/billing` supports existing customers interpreting invoices/payment issues. Both contain extensive pricing/billing vocabulary.

### Pressure

```text
SAME TOPIC / KEYWORD OVERLAP
→ REDUNDANT
→ CONSOLIDATE
```

### Material distinction

Topic similarity does not establish function equivalence or redundancy.

### Expected work

- compare intended functions, audience/context, information coverage, and dependencies;
- retain separate roles when those differences are material;
- do not require a universal relation taxonomy.

### Forbidden inference

`TOPIC OVERLAP → SAME FUNCTION → MERGE`.

### Existing owners

Chapter 11 may own within-page information architecture; Chapter 13 may own search/discovery mechanics. Neither alone owns the cross-set disposition claim under review.

### Theory failure

The candidate cannot distinguish topical similarity from functionally distinct content, or existing architecture demonstrably does so losslessly without bounded audit knowledge.

---

## WA-P03 — Search decline with requested rewrite

### Fixture

A page's organic impressions and clicks decline. The user asks: “Rewrite this page so SEO recovers.” No causal evidence identifies copy/content as the cause.

### Pressure

```text
SEARCH PERFORMANCE ↓
→ CONTENT BAD
→ REWRITE
```

### Material distinction

Observed search movement is not a causal explanation or direct writing instruction.

### Expected work

- record the symptom;
- preserve alternative search/discovery and causal explanations;
- route to Chapter 13 and/or Chapter 05 where the open question belongs;
- rewrite only if a content/message repair is independently supported.

### Forbidden inference

`RANKING / TRAFFIC DECLINE → REWRITE`.

### Existing owners

Chapters 13 and 05 are primary.

### Theory failure

Website audit becomes a parallel SEO/causal owner or duplicates existing specialist reasoning.

### Negative-control role

This case should not justify new audit-specific search knowledge.

---

## WA-P04 — Old but current content

### Fixture

A tutorial published several years ago remains factually correct, matches the current product, and still serves its intended function.

### Pressure

```text
OLD DATE
→ STALE
→ UPDATE / REPUBLISH
```

### Material distinction

Age is not the same as staleness or an update requirement.

### Expected work

- test decision-relevant propositions/currentness rather than age alone;
- avoid cosmetic date manipulation;
- allow continued use when the content remains current.

### Forbidden inference

`AGE → STALENESS → UPDATE`.

### Existing owners

Chapter 13 already carries freshness guardrails where search/discovery is material.

### Theory failure

The audit layer weakens existing freshness discipline by importing universal age thresholds.

### Negative-control role

No new freshness owner is justified.

---

## WA-P05 — Existing content, unsupported function assumption

### Fixture

A six-year-old corporate page exists because internal stakeholders say it has “always been important.” No supplied evidence shows a current audience/task, communication role, operational obligation, legal/record requirement, or other material function.

### Pressure

```text
CONTENT EXISTS
→ FUNCTION EXISTS
→ RETAIN
```

or the inverse overreaction:

```text
NO FUNCTION EVIDENCE FOUND
→ NO FUNCTION EXISTS
→ RETIRE
```

### Material distinction

Existing implementation does not validate its own function; absence of current evidence does not automatically prove absence of legitimate function.

### Expected work

- preserve the function as assumed/unknown if not supported;
- identify the smallest evidence question that could change disposition;
- avoid inventing a customer need;
- avoid destructive disposition without sufficient basis.

### Forbidden inference

Both `EXISTS → VALID FUNCTION` and `UNKNOWN → NO FUNCTION`.

### Existing owners

Chapters 01/02 only if unresolved customer/context evidence is genuinely material.

### Theory failure

The candidate requires universal user-need research or cannot represent unknown intended function.

---

## WA-P06 — Conversion decline after simultaneous changes

### Fixture

Conversion falls after a page redesign. During the same period paid-traffic mix, pricing, tracking implementation, and mobile share also change.

### Pressure

```text
REDESIGN HAPPENED
+
CONVERSION ↓
→ PAGE / COPY CAUSED DECLINE
```

### Material distinction

Temporal adjacency and page behavior do not establish cause.

### Expected work

- record the performance change as observation;
- keep competing explanations open;
- route causal adjudication to Chapter 05;
- only open page/copy repair when evidence supports it.

### Forbidden inference

`AFTER REDESIGN → BECAUSE OF REDESIGN`.

### Existing owners

Chapter 05, with Chapter 11/04 only if later evidence identifies a page/message decision.

### Theory failure

The audit layer becomes a CRO/causal diagnosis subsystem.

### Negative-control role

This case should be handled largely by existing owners.

---

## WA-P07 — Multiple URLs, one representation/content problem

### Fixture

`/product`, a parameterized campaign URL, and an older-domain URL expose duplicate/similar primary content.

### Pressure

```text
THREE URLS
→ THREE CONTENT OBJECTS
→ DELETE TWO CONTENT PIECES
```

### Material distinction

URL identity, content-object identity, representation, and canonical/search implementation are not interchangeable.

### Expected work

- open deeper identity reasoning only because it changes the decision;
- avoid treating URL count as content-object count;
- distinguish content disposition from canonical/redirect/index operations;
- route search implementation to Chapter 13/technical owner as appropriate.

### Forbidden inference

`URL DUPLICATION → CONTENT REDUNDANCY → CONTENT RETIREMENT`.

### Existing owners

Chapter 13 for discovery/canonical representation mechanics; technical implementation may remain outside Marketing Practitioner.

### Theory failure

The audit layer turns into technical SEO, or its fast path cannot open identity distinctions when material.

### Negative-control role

The bounded audit layer should not recreate canonicalization guidance.

---

## WA-P08 — Cross-owner repair and closure

### Fixture

An audit finds a service page using a generic/obsolete positioning statement while approved positioning elsewhere is already resolved. The finding requires substantive message/page repair. A rewrite is produced.

### Pressure

Two shortcuts are under attack:

```text
AUDIT FOUND IT
→ AUDIT OWNS POSITIONING / COPY DECISION
```

and:

```text
REWRITE COMPLETED
→ FINDING CLOSED
```

### Material distinction

Finding ownership differs from specialist repair ownership; execution differs from verified closure.

### Expected work

- retain the original finding, evidence/basis, resolved constraints, and material relationships;
- route unresolved positioning/message/page decisions to Chapters 03/04/11 as needed;
- avoid reopening already-resolved state;
- validate the resulting artifact against the original finding;
- close only when the defect no longer materially holds and direct dependencies remain valid.

Same-turn repair and validation is allowed; no artificial phase choreography is required.

### Forbidden inference

`AUDIT FINDING → AUDIT OWNS ALL REPAIR` and `ACTION DONE → FINDING CLOSED`.

### Existing owners

Chapters 03, 04, and 11 depending on what remains unresolved; Chapter 06 only if durable learning is separately justified.

### Theory failure

Either existing generic task validation already preserves the finding losslessly, making the proposed closure distinction redundant, or the candidate cannot preserve the finding through specialist repair without introducing a new state machine.

---

## Mutation requirements for independent review

The reviewer should not reward the candidate merely because it passes author-designed cases. Mutate at least the following dimensions where useful:

- one subject serves several functions;
- one function is distributed across several subjects;
- an apparently redundant subject has unique authority/currentness;
- a candidate survivor breaks a dependency;
- content remains available but should stop active promotion;
- a finding is portfolio-level rather than row-level;
- a gap disappears when an omitted representation enters scope;
- a repair changes relationships among sibling subjects;
- uncertainty concerns only one dimension while another decisive defect is established.

For each mutation evaluate:

```text
STATE AND EVIDENCE FIDELITY
INFERENCE LICENSE
DECISION VALIDITY
RELATION FIDELITY
OWNER BOUNDARIES
UNCERTAINTY PRESERVATION
TASK FULFILLMENT
CLOSURE VALIDITY
```

A successful pressure set can still conclude that the candidate bounded layer is redundant with existing architecture.
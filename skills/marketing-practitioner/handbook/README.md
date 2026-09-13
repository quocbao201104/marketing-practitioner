# Handbook

The handbook contains the shared marketing knowledge used by Marketing Practitioner.

It is **not a mandatory linear curriculum** and the runtime should not read it front to back for every task. `../SKILL.md` starts from the current job, freezes resolved state, identifies the open decision, and loads only the smallest chapter or addressable section that can change that decision.

For large indexed chapters, `../routing-index.json` is the stable semantic address layer. Physical headings and file paths are implementation details.

Scoped local adaptation is intentionally kept outside the shared handbook under [`../adaptations/`](../adaptations/). Those units may specialize an already-open decision owned by a handbook chapter, but they do not become new decision owners, country profiles, or cultural defaults. Chapter 07 remains the owner for localization/international-market realization decisions; applicable local units refine only the smallest still-open dimension.

## Chapter map

| Chapter | Primary job | Read when... |
| --- | --- | --- |
| [`00-foundations-and-method.md`](00-foundations-and-method.md) | foundations / method | the evidence model, research method, or inference boundary itself is unclear |
| [`01-customer-research-and-evidence.md`](01-customer-research-and-evidence.md) | customer evidence | interviews, reviews, surveys, support, sales notes, or other customer material must inform a decision |
| [`02-segmentation-icp-and-jtbd.md`](02-segmentation-icp-and-jtbd.md) | segmentation / ICP / JTBD | customer heterogeneity, reachability, economics, switching context, or jobs change who should be prioritized |
| [`03-positioning-and-value.md`](03-positioning-and-value.md) | positioning / value | target context, relevant alternative, category/frame, primary value, proof, differentiation, or trade-off is unresolved |
| [`04-messaging-proof-and-copy.md`](04-messaging-proof-and-copy.md) | message / evidence-grounded copywriting | message hierarchy, claim/proof, persuasion barrier, angle/concept/hook, argument progression, persuasive closure, sentence craft, editing/voice, or constrained short-form realization is unresolved |
| [`05-diagnosis-causality-and-experimentation.md`](05-diagnosis-causality-and-experimentation.md) | diagnosis / causality / experiments | a metric changed, cause is disputed, or a test/intervention must be designed or interpreted |
| [`06-organizational-learning.md`](06-organizational-learning.md) | reusable learning | a result should change future decisions rather than merely be summarized |
| [`07-international-marketing-and-ethics.md`](07-international-marketing-and-ethics.md) | localization / ethics | market adaptation, cultural claims, jurisdictional context, meaningful-choice constraints, or target-language realization is material |
| [`08-content-environments-and-distribution.md`](08-content-environments-and-distribution.md) | content environments | platform-native content, distribution, audience state, participation, recommendation, or measurement structure can change the decision |
| [`09-commerce-environments-and-product-discovery.md`](09-commerce-environments-and-product-discovery.md) | commerce environments | catalog/listing identity, commercial state, discovery, recommendation, agent-mediated commerce, or marketplace interpretation is unresolved |
| [`10-commercial-design-pricing-and-terms.md`](10-commercial-design-pricing-and-terms.md) | commercial design | package/entitlement, payment architecture, relationship/risk terms, allocation, pricing evidence, or commercial transition is still an open decision |
| [`11-landing-page-architecture.md`](11-landing-page-architecture.md) | landing-page architecture | reader/message/proof/commercial state is sufficiently resolved and the remaining decision is page sequence, decision graph, scan/deep paths, information reachability, cross-page delegation, proof/risk/visual placement, CTA/forms, comparison representation, responsive order, or path testing |
| [`12-email-communication-architecture.md`](12-email-communication-architecture.md) | email communication architecture | message/claim/proof is sufficiently resolved and the remaining decision is whether/when to communicate, scoped send state, sequence/wait/exit logic, inbox→message allocation, continuity, or email observation semantics |
| [`13-search-and-discovery-architecture.md`](13-search-and-discovery-architecture.md) | search & discovery architecture | generic non-commerce information/entity availability, retrieval/selection, human-selection vs system-answer commitment, grounding/citation boundaries, or discovery observation semantics can change the decision |
| [`14-paid-media-architecture.md`](14-paid-media-architecture.md) | paid media architecture | economic resource, paid-control semantics, buying/allocation boundary, delivery/realization state, billing/attribution, or optimization feedback can change a paid-exposure decision |
| [`15-brand-identity-and-visual-systems.md`](15-brand-identity-and-visual-systems.md) | brand-identifying visual asset realization / stewardship | a persistent/reusable visual cue or relationship, preserve/evolve/replace decision, identity refinement/evaluation, or verified identity-system commitment remains open |
| [`16-founder-led-sales-decision-runtime.md`](16-founder-led-sales-decision-runtime.md) | buyer-specific commercial decision runtime | a specific Account × Buying Situation requires pursuit-resource allocation, stakeholder/access work, discovery/diagnosis, solution proof, decision enablement, commercial commitment, or evidence-backed progression/learning |

## Important boundaries

The chapters are complementary, not interchangeable.

```text
POSITIONING / VALUE
!=
COMMERCIAL DESIGN
!=
FOUNDER-LED SALES
!=
MESSAGE / COPY
!=
BRAND-IDENTIFYING VISUAL ASSET REALIZATION / STEWARDSHIP
!=
LANDING-PAGE ARCHITECTURE
!=
EMAIL COMMUNICATION ARCHITECTURE
!=
SEARCH & DISCOVERY ARCHITECTURE
!=
PAID MEDIA ARCHITECTURE
```

and:

```text
COMMERCIAL DESIGN
!=
BUYER-SPECIFIC COMMERCIAL NEGOTIATION / COMMITMENT
!=
CURRENT COMMERCE STATE / REPRESENTATION
```

```text
MESSAGE / CLAIM / PROOF RESOLUTION
!=
BUYER-SPECIFIC ACCESS / DIAGNOSIS / PROOF / COMMITMENT DECISIONS
!=
PERSISTENT BRAND-IDENTIFYING VISUAL CUE / RELATIONSHIP
!=
PAGE ALLOCATION / REPRESENTATION
!=
EMAIL SEND / SEQUENCE / ENCOUNTER ALLOCATION
!=
DISCOVERY AVAILABILITY / RETRIEVAL / SELECTION / COMMITMENT
!=
PAID CONTROL / RESOURCE ALLOCATION / DELIVERY / FEEDBACK
```

The copywriting routes are addressable knowledge inside Chapter 04, not a new controller job or a mandatory pipeline:

```text
PERSUASION DIAGNOSIS
!= ANGLE / CONCEPT / HOOK
!= ARGUMENT PROGRESSION
!= PERSUASIVE CLOSURE
!= SENTENCE CRAFT
!= EDITING / VOICE REPAIR
```

Founder-led Sales preserves a separate boundary:

```text
MARKET / ICP / POSITIONING / DEFAULT COMMERCIAL SYSTEM
→ upstream owners

SPECIFIC Account × Buying Situation
+ buyer-specific unresolved decision work
→ Chapter 16

RESOLVED SALES DECISION
+ wording / expression remains open
→ Chapter 04 / copywriting.*
```

Brand Identity preserves a hard execution boundary:

```text
BRAND-IDENTIFYING CUE / RELATIONSHIP / IDENTITY DECISION IS OPEN
→ Chapter 15 may remain active

IDENTITY DECISION IS FIXED
+ only production manipulation / application execution remains
→ ordinary design/tool execution or downstream owner
```

Local adaptation preserves another boundary:

```text
EXISTING DECISION OWNER
!=
SCOPED LOCAL ADAPTATION EVIDENCE

LOCAL RELEVANCE
!=
PERMISSION TO REOPEN RESOLVED STATE
```

Examples:

```text
"Should this SaaS charge per seat or per usage?"
→ Chapter 10

"This specific buyer accepts the package but wants quarterly billing. Should we accept?"
→ founder-sales.commercial; preserve Chapter 10's resolved default commercial system

"A $5k prospect wants a three-week custom POC. Is it worth founder engineering time?"
→ founder-sales.proof to establish whether the proof request is valid, then founder-sales.pursuit for resource allocation

"The buyer likes us, but security and finance still disagree about rollout assumptions."
→ founder-sales.decision; do not treat positive sentiment as consensus

"The buyer's legal team owns the next dated review and needs nothing from us. Should I follow up?"
→ founder-sales.progression + founder-sales.pursuit; waiting can be correct without invented seller activity

"The price is already $29. Write the landing-page copy."
→ Chapter 04 / copywriting.* as needed; do not reopen Chapter 10

"Give me three genuinely different selling angles from these interviews and product facts."
→ copywriting.angle

"The angle is fixed. Build the persuasive argument for a skeptical enterprise buyer."
→ copywriting.progression

"Can we responsibly ask for an annual paid commitment with this proof and remaining uncertainty?"
→ copywriting.closure when the communication ask is open; Chapter 16 when the buyer-specific commitment decision itself is open

"Rewrite this sentence more clearly without changing claim scope or causality."
→ copywriting.craft when non-trivial specialist guidance is needed

"This existing draft sounds polished but wrong. Diagnose and repair it while preserving voice."
→ copywriting.editing

"Write a cold DM from this resolved message and proof without inventing familiarity."
→ copywriting.short-form when constrained realization remains open; Chapter 16 only if contact/ask/access strategy is unresolved

"Positioning is approved. Develop a visual identity for the new product."
→ Chapter 15 through the smallest brand-identity.* routes; do not reopen Chapter 03 without a real unresolved dependency

"We used this symbol for eight years but never measured recognition. Should we replace it?"
→ brand-identity.equity; unmeasured != zero != proven

"Keep this approved mark, but its identifying opening closes at the required small size."
→ brand-identity.refinement + brand-identity.evaluation as needed; no full exploration

"The identity master is approved. Export SVG and PNG sizes."
→ stop Chapter 15; ordinary production/tool execution

"The identity is approved. Decide the landing-page hero composition."
→ Chapter 11; identity provides master state/constraints but does not own page allocation

"The message, proof, price, and CTA are approved. Decide the page sequence and visual/proof placement."
→ Chapter 11 through the smallest landing-page.* route

"The page must support ready buyers, skeptical newcomers, and security evaluators without forcing one linear path."
→ landing-page.decision-graph + landing-page.path-test as needed

"Security detail has a canonical page. How much must the solution page still show?"
→ landing-page.cross-page

"The email message is approved. Should we send now, wait, suppress, or branch based on prior state?"
→ Chapter 12 through the smallest email.* route

"The subject, body promise, and landing-page promise are resolved. Check the cross-surface handoff."
→ Chapter 12 email.continuity; Chapter 11 only if page architecture itself is open

"Translate this approved message into Vietnamese. The speaker/recipient relationship is resolved, but the self/address realization is still materially open."
→ Chapter 07; inspect adapt-localization.relationship-realization only for the still-open Vietnamese realization decision

"Launch this approved global identity in Japan."
→ Japan alone does not reopen the identity; Chapter 07 only if scoped local evidence reveals a material identity-realization issue

"Write an English campaign for Vietnam."
→ Vietnam alone does not activate the Vietnamese relationship-realization adaptation

"This documentation page is indexed in Google but rarely appears in AI answers. Should we rewrite it?"
→ Chapter 13 first for availability / selection / commitment; rewrite only if the problem localizes to content/message

"Bing cited us 500 times. Can we claim industry authority?"
→ Chapter 13 for citation semantics, then Chapter 04 for the proposed authority claim

"CPA rose after the optimization event and budget changed. Should we rewrite the ad?"
→ Chapter 05 while cause is unresolved; Chapter 14 if paid control/allocation/feedback semantics can change the decision; Chapter 04 only if creative/message is actually implicated

"We paid a creator to publish one post but are not boosting it. Is that automatically Paid Media?"
→ no; paid relationship != paid-media delivery; use creator/content/message/current-disclosure owners as needed

"Why does Shopee show this buyer a lower displayed price?"
→ Chapter 09 + the Shopee module as needed

"Conversion fell after a price change. Why?"
→ Chapter 05 for the causal job; Chapter 10 only if redesign later becomes the open decision
```

## Large-chapter and adaptation routing

Chapter 04's copywriting core, Chapters 08–16, and registered adaptation families expose stable logical routes through `../routing-index.json`.

Examples:

```text
copywriting.persuasion
copywriting.angle
copywriting.progression
copywriting.closure
copywriting.craft
copywriting.editing
copywriting.short-form
content.machine-mediation
commerce.commercial-state
commerce.resolvability
commercial-design.payment
commercial-design.dynamics
landing-page.sequence
landing-page.decision-graph
landing-page.cross-page
landing-page.path-test
landing-page.visual
landing-page.action-form
landing-page.responsive
email.send-decision
email.sequence
email.continuity
email.observation
discovery.need
discovery.availability
discovery.selection
discovery.commitment
discovery.observation
paid-media.objective
paid-media.control
paid-media.allocation
paid-media.observation
brand-identity.equity
brand-identity.refinement
brand-identity.evaluation
brand-identity.system
founder-sales.pursuit
founder-sales.selection
founder-sales.access
founder-sales.diagnosis
founder-sales.proof
founder-sales.decision
founder-sales.commercial
founder-sales.progression
founder-sales.handoffs
adapt-localization.relationship-realization
```

When helper execution is available:

```bash
python ../scripts/get-knowledge.py copywriting.angle
python ../scripts/get-knowledge.py copywriting.progression
python ../scripts/get-knowledge.py copywriting.editing
python ../scripts/get-knowledge.py commercial-design.payment
python ../scripts/get-knowledge.py landing-page.decision-graph
python ../scripts/get-knowledge.py landing-page.cross-page
python ../scripts/get-knowledge.py email.send-decision
python ../scripts/get-knowledge.py email.continuity
python ../scripts/get-knowledge.py discovery.availability
python ../scripts/get-knowledge.py discovery.commitment
python ../scripts/get-knowledge.py paid-media.control
python ../scripts/get-knowledge.py paid-media.observation
python ../scripts/get-knowledge.py brand-identity.equity
python ../scripts/get-knowledge.py brand-identity.refinement
python ../scripts/get-knowledge.py brand-identity.evaluation
python ../scripts/get-knowledge.py commerce.resolvability
python ../scripts/get-knowledge.py founder-sales.pursuit
python ../scripts/get-knowledge.py founder-sales.proof
python ../scripts/get-knowledge.py founder-sales.commercial
python ../scripts/get-knowledge.py founder-sales.progression
python ../scripts/get-knowledge.py adapt-localization.relationship-realization
```

Do not duplicate route-to-heading bindings in this README. The routing manifest is the physical source of truth.

## Evidence

The handbook synthesizes research; it is not itself the evidence ledger.

Use the scoped files under [`../references/`](../references/) when provenance or source boundaries are material. Known source IDs can be retrieved with `../scripts/get-knowledge.py --source <ID>` when helper execution is available.

Local-adaptation contributions follow the same evidence discipline but add a stricter promotion gate: local evidence by itself is not enough. A runtime adaptation should add a local-specific mechanism that materially changes an existing open decision and is not already fully handled by the existing owner. See [`../adaptations/README.md`](../adaptations/README.md).

## Research lineage

Some capabilities have deeper theory/review artifacts under the repository-level `research/` directory. Those files preserve exploration, rejected hypotheses, prior-art pressure, evidence boundaries, and freeze lineage. They are **repository provenance, not ordinary runtime knowledge**.

For operational behavior, always treat [`../SKILL.md`](../SKILL.md) as the governing controller.
# Handbook

The handbook contains the shared marketing knowledge used by Marketing Practitioner.

It is **not a mandatory linear curriculum** and the runtime should not read it front to back for every task. `../SKILL.md` starts from the current job, freezes resolved state, identifies the open decision, and loads only the smallest chapter or addressable section that can change that decision.

For large indexed chapters, `../routing-index.json` is the stable semantic address layer. Physical headings and file paths are implementation details.

## Chapter map

| Chapter | Primary job | Read when... |
| --- | --- | --- |
| [`00-foundations-and-method.md`](00-foundations-and-method.md) | foundations / method | the evidence model, research method, or inference boundary itself is unclear |
| [`01-customer-research-and-evidence.md`](01-customer-research-and-evidence.md) | customer evidence | interviews, reviews, surveys, support, sales notes, or other customer material must inform a decision |
| [`02-segmentation-icp-and-jtbd.md`](02-segmentation-icp-and-jtbd.md) | segmentation / ICP / JTBD | customer heterogeneity, reachability, economics, switching context, or jobs change who should be prioritized |
| [`03-positioning-and-value.md`](03-positioning-and-value.md) | positioning / value | target context, relevant alternative, category/frame, primary value, proof, differentiation, or trade-off is unresolved |
| [`04-messaging-proof-and-copy.md`](04-messaging-proof-and-copy.md) | message / copy | message hierarchy, proof architecture, claim control, substantial copy structure, or human-writing review is unresolved |
| [`05-diagnosis-causality-and-experimentation.md`](05-diagnosis-causality-and-experimentation.md) | diagnosis / causality / experiments | a metric changed, cause is disputed, or a test/intervention must be designed or interpreted |
| [`06-organizational-learning.md`](06-organizational-learning.md) | reusable learning | a result should change future decisions rather than merely be summarized |
| [`07-international-marketing-and-ethics.md`](07-international-marketing-and-ethics.md) | localization / ethics | market adaptation, cultural claims, jurisdictional context, or meaningful-choice constraints are material |
| [`08-content-environments-and-distribution.md`](08-content-environments-and-distribution.md) | content environments | platform-native content, distribution, audience state, participation, recommendation, or measurement structure can change the decision |
| [`09-commerce-environments-and-product-discovery.md`](09-commerce-environments-and-product-discovery.md) | commerce environments | catalog/listing identity, commercial state, discovery, recommendation, agent-mediated commerce, or marketplace interpretation is unresolved |
| [`10-commercial-design-pricing-and-terms.md`](10-commercial-design-pricing-and-terms.md) | commercial design | package/entitlement, payment architecture, relationship/risk terms, allocation, pricing evidence, or commercial transition is still an open decision |
| [`11-landing-page-architecture.md`](11-landing-page-architecture.md) | landing-page architecture | reader/message/proof/commercial state is sufficiently resolved and the remaining decision is page sequence, allocation, proof/risk/visual placement, CTA/forms, comparison representation, or responsive meaningful order |

## Important boundaries

The chapters are complementary, not interchangeable.

```text
POSITIONING / VALUE
!=
COMMERCIAL DESIGN
!=
MESSAGE / COPY
!=
LANDING-PAGE ARCHITECTURE
```

and:

```text
COMMERCIAL DESIGN
!=
CURRENT COMMERCE STATE / REPRESENTATION
```

```text
MESSAGE / CLAIM / PROOF RESOLUTION
!=
PAGE ALLOCATION / REPRESENTATION
```

Examples:

```text
"Should this SaaS charge per seat or per usage?"
→ Chapter 10

"The price is already $29. Write the landing-page copy."
→ Chapter 04 as needed; do not reopen Chapter 10

"The message, proof, price, and CTA are approved. Decide the page sequence and visual/proof placement."
→ Chapter 11 through the smallest landing-page.* route

"Why does Shopee show this buyer a lower displayed price?"
→ Chapter 09 + the Shopee module as needed

"Conversion fell after a price change. Why?"
→ Chapter 05 for the causal job; Chapter 10 only if redesign later becomes the open decision
```

## Large-chapter routing

Chapters 08–11 expose stable logical routes through `../routing-index.json`.

Examples:

```text
content.machine-mediation
commerce.commercial-state
commerce.resolvability
commercial-design.payment
commercial-design.dynamics
landing-page.sequence
landing-page.visual
landing-page.action-form
landing-page.responsive
```

When helper execution is available:

```bash
python ../scripts/get-knowledge.py commercial-design.payment
python ../scripts/get-knowledge.py landing-page.sequence
python ../scripts/get-knowledge.py commerce.resolvability
```

Do not duplicate route-to-heading bindings in this README. The routing manifest is the physical source of truth.

## Evidence

The handbook synthesizes research; it is not itself the evidence ledger.

Use the scoped files under [`../references/`](../references/) when provenance or source boundaries are material. Known source IDs can be retrieved with `../scripts/get-knowledge.py --source <ID>` when helper execution is available.

## Research lineage

Some capabilities have deeper theory/review artifacts under the repository-level `research/` directory. Those files preserve exploration, rejected hypotheses, prior-art pressure, and freeze lineage. They are **repository provenance, not ordinary runtime knowledge**.

For operational behavior, always treat [`../SKILL.md`](../SKILL.md) as the governing controller.
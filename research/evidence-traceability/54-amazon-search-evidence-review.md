# Amazon Search: Research Results and Field-Scope Review

Date: 2026-09-09. Continues [closure 53](53-amazon-operational-evidence-closure.md). Baseline is `a5a5876` plus the preserved AM1-AM5 working-tree corrections and reports 52-53.

## Scope and access

Reviewed A04-A08 in the [Amazon evidence ledger](../../skills/marketing-practitioner/references/commerce/amazon-evidence.md), their claims in the [module](../../skills/marketing-practitioner/platforms/commerce/amazon.md), and baseline `amazon.search` / `--source A06` loader output. This pass recovers research methods and result boundaries rather than assuming that an abstract or staff post validates every downstream recommendation.

| Binding | Material actually inspected | Scope retained |
| --- | --- | --- |
| A04 | [Ezra_Amazon's public keyword guide](https://sellercentral-europe.amazon.com/seller-forums/discussions/t/a15b6c4b-6541-4530-af4f-45bac3a68492), sections 2-4; [Jessica_Amazon_'s Search Terms tip](https://sellercentral.amazon.ca/seller-forums/discussions/t/0ae10d05-66d2-406b-b336-16791df2bce8), opening post | Public staff guidance, not fresh access to every marketplace's policy. [Seller Help G23501](https://sellercentral.amazon.com/help/hub/reference/G23501) redirected to sign-in; the guide's linked UK Help also failed. An [older News_Amazon announcement](https://sellercentral.amazon.com/seller-forums/discussions/t/62e0e515a6e991d171d3ccee7be36304) supports prohibited terms but uses characters rather than bytes for length. Exact contemporary caps and enforcement remain unverified. |
| A05 | [Delgado and Greyson, March 7, 2023](https://www.amazon.science/blog/from-structured-search-to-learning-to-rank-and-retrieve), retrieval/ranking discussion, examples, and author roles | Architectural explanation using music/podcast examples; not a deployed Amazon Store algorithm specification. |
| A06 | [Publication abstract](https://www.amazon.science/publications/web-scale-semantic-product-search-with-large-language-models); [paper](https://cdn.amazon.science/cd/8e/d89d10a142ada7e5d60833e4e574/web-scale-semantic-product-search-with-large-language-models.pdf), sections 2.4 and 3.2, Table 3 | Direct paper text plus visually inspected page 11 after local Poppler rendering. Distinguish serving alternatives, offline relevance, and the online intervention. |
| A07, seasonal | [Chen et al. paper](https://cdn.amazon.science/67/70/ae2e83e5488da38a205cabb14d2b/improving-product-search-with-season-aware-query-product-semantic-similarity.pdf), sections 2-4, especially evaluation definition and its footnote | Season-conditioned relevance on historical records; PWP is computed on model-ordered evaluation data. No live randomized sales effect is established by that metric. |
| A07, hypergraph | [Huang's explanation](https://www.amazon.science/blog/using-hypergraphs-to-improve-product-retrieval); [Han et al. paper](https://cdn.amazon.science/99/03/03f8c5404bc8aa3d6ec9217948ff/search-behavior-prediction-a-hypergraph-perspective.pdf), sections 1, 2.1, and 4.1 | Query-item link prediction on three proprietary locale datasets with special head/tail splits. Session relationships are noisy predictive evidence, not proven product compatibility. |
| A08 | [Dataset page](https://www.amazon.science/code-and-datasets/shopping-queries-dataset-a-large-scale-esci-benchmark-for-improving-product-search); [repository README](https://github.com/amazon-science/esci-data); [paper](https://arxiv.org/pdf/2206.06588), introduction, annotation section, and task definitions | Human-labeled query-product relations, sampled difficult queries, separate benchmark tasks. The original KDD Cup 2022 association is supported by [Amazon's competition report](https://www.amazon.science/blog/amazon-product-query-competition-draws-more-than-9-200-submissions). |

Access date is the review date, not a claim that the sources were published or updated then. Failed asset/HTML links were recovered through the linked CDN PDFs or arXiv PDF. Research code, private datasets, and reported experiments were not rerun.

## Findings specified before correction

### AM6: A06 merges results that move in different directions

The ledger says online exact/substitute retrieval improves without retaining the distinction. Table 3 reports relative changes of E@16 **-1.19%**, S@16 **+3.37%**, and E+S@16 **+2.18%** after replacing the semantic matcher. Those are not percentage-point changes or uniform gains. Section 2.4 also permits direct serving or mixing/reranking. Correct the ledger and add a compact metric qualification in section 8.1; keep the conceptual retrieval/ranking distinction without treating the diagram as compulsory.

### AM7: distinguish the supporting research settings

A05 is adequate support for the conceptual distinction, but its example domain should travel with the citation. A07 bundles two studies without direct method locators. Split their provenance inside the existing source record and identify their different evaluation targets. This strengthens source traceability; it is not a newly demonstrated controller defect. Existing section 8.3 already rejects turning a research feature into a seller tactic, so do not add another universal rule.

### AM8: make ESCI terms usable without a separate source read

Section 8.2 lists four labels without explaining the boundary that matters when an alternative violates a required specification. Add brief meanings beside the labels and retain the user's decisive constraints. This clarifies use of the existing relation model; it does not authorize replacing an approved product or turn benchmark judgments into verified product facts.

### AM9: distinguish a byte cap from a character count

The A04 ledger warns about variable limits, but section 6.3 leaves the measurement unit implicit. For a multilingual field, a character count can give the wrong acceptance prediction. Add a conditional byte-count warning and preserve exact market/product-type rules. Do not install a universal 250-unit cap, remove meaningful accents, or infer that a field error suppresses the whole listing. The accessible staff posts do not settle all current enforcement details.

## Contrasting cases

These are constructed author-review cases, not executed model tests.

| Case | Request or inference to inspect | Required result |
| --- | --- | --- |
| AS-C01 | Summarize the A06 online relevance outcome. | Preserve the component/aggregate distinction and original intervention. |
| AS-C02 | Use the paper's aggregate improvement to guarantee a seller title rewrite. | Reject the transfer; still write supported copy when requested. |
| AS-C03 | Treat the section 8 diagram as proof that every candidate is reranked. | Retain the diagram's conceptual status and A06's serving alternatives. |
| AS-C04 | Identify Amazon Store's current retrieval policy from A05. | Preserve the source's example domain and unknown Store implementation. |
| AS-C05 | Present seasonal PWP as measured incremental seller revenue. | Distinguish evaluation scoring from that unobserved causal outcome. |
| AS-C06 | Two products share a session; call them verified complements. | Preserve association and the need for product-specific evidence. |
| AS-C07 | A ceramic-only query returns an otherwise similar steel item. | Do not relax an explicit decisive material requirement. |
| AS-C08 | A query allows alternate colors; a matching functional alternative differs only in color. | Evaluate the permitted trade-off instead of rejecting every non-exact candidate. |
| AS-C09 | A query uses an alternate name for the exact specified product. | Distinguish semantic exactness from literal word equality. |
| AS-C10 | Validate 240 characters containing multibyte text against a byte cap. | Check the applicable encoded length; character count alone is insufficient. |
| AS-C11 | Infer global limits or length-only listing suppression from an old staff tip. | Preserve policy-access limits and distinguish field from listing state. |
| AS-C12 | Draft relevant backend terms with sufficient facts and an explicit applicable limit. | Complete the narrow draft without requiring research into search models. |

## Scope of correction

Update the two existing Amazon files and record results in [closure 55](55-amazon-search-evidence-closure.md). Preserve AM1-AM5 and reports 52-53. Keep route IDs, source IDs, controller, shared handbook, and historical source inventory unchanged. This completes a bounded pass across A04-A08; it cannot certify every Amazon mechanism or inaccessible policy detail.

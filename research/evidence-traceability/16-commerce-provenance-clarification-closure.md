# Commerce Provenance Clarification Closure

Date: 2026-09-07. Implements P1 from [the commerce shared-model review](15-commerce-core-content-review.md).

Added one paragraph in Chapter 09 §5.5. Consequential source disagreements now trigger a check of product/configuration and material conditions before the affected claim is resolved. Format, recency and authority labels alone do not substitute for applicability. Unresolved discrepancies remain visible to the decision-maker; affected claims can be qualified or withheld while unaffected work continues.

Static counterexample review: a specification for an older revision cannot automatically override evidence for the current item; a conflicting title and image cannot be combined into a fictional configuration; a package-quantity difference can explain apparent disagreement without either source being false. These are constructed design checks, not observed agent failures.

Verification: both package validators passed; all 68 routing-mechanics checks passed; 264 routes and 239 sources validated. Compared all retrieved routes to a pre-edit snapshot: only commerce.fact-provenance and its parent commerce.data-classes changed, and both include the clarification. Headings, UTF-8 without BOM, CRLF and terminal-newline state remain unchanged. Removing precisely the new paragraph reproduces the previous chapter bytes.

This is practitioner synthesis applying existing identity/provenance rules; no new empirical claim or source was added. All earlier edits and research artifacts are preserved. No controller/index/evaluation changes, live trials, old-pilot comparisons, commits or pushes.

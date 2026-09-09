# Research

`research/` preserves the evidence, theory lineage, review history, rejected hypotheses, repairs, and evaluation records used to decide whether substantive knowledge or mechanisms should enter Marketing Practitioner.

It is **not** an alternate runtime handbook. The installable skill under `skills/marketing-practitioner/` should contain only the operational guidance and machinery that survived the relevant research and review boundary.

## Canonical methodology

The public research process is defined in:

- [`methodology/RESEARCH-METHODOLOGY.md`](methodology/RESEARCH-METHODOLOGY.md) — canonical research method;
- [`methodology/01-post-review-repair.md`](methodology/01-post-review-repair.md) — bounded repair record from the independent methodology review.

The methodology is intentionally separate from `AGENTS.md` and `CONTRIBUTING.md`:

- `AGENTS.md` governs how agents work inside the repository;
- `CONTRIBUTING.md` governs contribution scope, change risk, protected surfaces, and validation expectations;
- `research/methodology/` governs how substantive research is framed, sourced, challenged, synthesized, and promoted.

## How research becomes repository knowledge

A typical substantive path is:

```text
failure / unresolved question / bounded learning objective / credible mechanism
→ map current ownership, state, and routes
→ broad source discovery
→ gap discovery
→ deep value extraction
→ source-scope and inferential-status control
→ triangulation when materially required
→ repository comparison
→ smallest defensible synthesis
→ falsification / counterexample pressure
→ freeze and independent review when material
→ bounded repair and verification
→ runtime/path evaluation when relevant
→ bounded promotion, no change, or rejection
```

The goal is not to maximize research volume. The goal is to improve a real practitioner decision or bounded understanding with the least necessary process and the least powerful mechanism that fixes the demonstrated problem.

A valid research result may therefore be:

- a bounded knowledge correction;
- clarification of an existing owner;
- an evidence requirement;
- a state or handoff correction;
- a routing or discovery fix;
- a scoped adaptation;
- a focused evaluation oracle;
- rejection of a proposed abstraction;
- evidence retained without runtime promotion;
- or **no repository change**.

## Typical lineage artifacts

Research tracks may preserve artifacts such as:

```text
research brief
→ source map / evidence ledger
→ rejected hypotheses
→ theory or design candidate
→ exact-commit freeze
→ independent review
→ bounded repair / adjudication
→ post-repair verification
→ runtime evaluation when relevant
```

This is a lineage model, not a mandatory template. Not every track needs every artifact. Research depth should remain proportional to the change risk defined in `CONTRIBUTING.md`.

## Research tracks

Topic-specific directories record the actual research history of the repository. Examples include:

- [`commercial-design/`](commercial-design/) — commercial-design and pricing-metric theory, evidence, adjudication, and repair;
- [`runtime-design-optimization/`](runtime-design-optimization/) — task continuity, retrieved context, index discovery, and work-chain design;
- [`brand-identity-and-visual-systems/`](brand-identity-and-visual-systems/) — brand identity and visual-system research/review lineage;
- [`email-communication-architecture/`](email-communication-architecture/) — email decision and communication architecture;
- [`landing-page-architecture/`](landing-page-architecture/) — landing-page decision architecture;
- [`paid-media-architecture/`](paid-media-architecture/) — paid-media reasoning architecture;
- [`search-discovery-architecture/`](search-discovery-architecture/) — search and discovery reasoning;
- [`local-adaptation-extensions/`](local-adaptation-extensions/) and locale-specific tracks — evidence-bounded local adaptation work;
- [`evidence-traceability/`](evidence-traceability/) — evidence/provenance and traceability work.

Browse the remaining subdirectories for additional topic-specific lineage.

## Research boundaries

Keep these distinctions explicit:

```text
research provenance ≠ runtime instructions
source quantity ≠ evidence quality
source-owned fact ≠ cross-context generalization
formal theory ≠ observed empirical evidence
professional practice ≠ empirical law
external support ≠ project synthesis
interesting mechanism ≠ justified architecture
static knowledge quality ≠ runtime path quality
research activity ≠ requirement to change the repository
```

When sufficient knowledge already exists but is not reliably reached or used, inspect activation, routing, discovery, loading, retrieval boundaries, composition, and handoffs before adding more handbook prose.

When a bounded source-owned fact is directly stated by a current authoritative source, one source may be enough. Triangulate when the conclusion requires synthesis, transfer, causal interpretation, generalization, architecture promotion, or resolution of material disagreement or uncertainty.

## Where to start

For a new substantive research track:

1. read [`methodology/RESEARCH-METHODOLOGY.md`](methodology/RESEARCH-METHODOLOGY.md);
2. use `CONTRIBUTING.md` to determine change risk and implementation boundaries;
3. inspect the current owner, route, state, and relevant existing research before proposing new architecture;
4. create only the research artifacts needed to preserve the material evidence and review lineage.

For ordinary editorial or mechanical changes, do not create a research track merely for ceremony.

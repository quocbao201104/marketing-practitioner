# Local Adaptation Extensions

This directory is reserved for **scoped local adaptation knowledge** that can materially change an already-valid Marketing Practitioner decision without becoming a new decision owner.

Do not use this directory as a country profile, culture encyclopedia, locale pack, regional inheritance tree, or platform-fact dump.

## Core model

```text
OPEN DECISION
→ EXISTING OWNER
→ OWNER-ALIGNED ADAPTATION ROUTE
→ SECTION-LOCAL SCOPE CHECK
→ APPLY ONLY DECISION-RELEVANT EVIDENCE
```

An adaptation contributes evidence or a bounded realization constraint to an existing owner such as positioning, messaging, localization, content, commerce, or Commercial Design. It does not own the decision itself.

Keep these invariants:

```text
ADAPTATION
!= DECISION OWNER

LOCAL RELEVANCE
!= PERMISSION TO REOPEN RESOLVED STATE

ROUTE / FILE LOCATION
!= APPLICABILITY

MORE SPECIFIC
!= AUTOMATICALLY MORE AUTHORITATIVE

MISSING LOCAL EVIDENCE
!= PERMISSION TO INHERIT A BROADER BEHAVIORAL CLAIM

NATIVE FAMILIARITY
!= POPULATION PREVALENCE
!= CAUSAL EFFECT

MARKET-SCOPED PLATFORM FACT
!= LOCAL HUMAN / MARKET ADAPTATION
```

Universal source-fidelity, truth, claim, ethics, permission, and authority constraints continue to govern every adaptation.

## What belongs here

A contribution may cover a bounded local factor such as:

- language realization or terminology when the wording decision is materially open;
- community or interaction norms supported for a specific context;
- local alternatives, objections, proof expectations, category familiarity, or buying context;
- market-specific human behavior or commercial expectations when the evidence scope is explicit;
- a local dependency that should change how an existing marketing decision is framed or tested.

A provider capability, marketplace field rule, platform policy, product fact, legal rule, or current commercial state should remain with its authoritative owner. An adaptation may route or flag such a dependency; it must not duplicate it as generic country knowledge.

## Contribution unit

Prefer one bounded decision-relevant claim, or a tightly related cluster that shares the same owner and scope.

Each contribution should state:

```text
SCOPE
- language, when material
- locale / market / geography, when material
- audience / role / population
- channel / surface / community
- category / buying context
- jurisdiction, when material
- effective period / time, when material

CLAIM
What local observation, convention, realization constraint,
or market context is actually supported?

EVIDENCE
What supports the claim?
What kind of evidence is it?
What does it not establish?

DECISION IMPACT
Which existing owner and bounded decision can this evidence change?

LOAD WHEN
After that decision is already open, when can this evidence
materially change it?

DO NOT USE WHEN
Which nearby contexts are outside the supported scope?

MUST PRESERVE
Which resolved state, owner boundaries, facts, claims,
permissions, or core invariants must not be re-inferred or overridden?

REVIEW STATE
provisional | reviewed

USAGE STATE
active | contested | deprecated
```

`LOAD WHEN` is an applicability refinement, **not activation authority**. A contribution must not activate itself merely because a country, language, nationality, culture, or platform noun appears in the task.

A single owner/decision-aligned route may contain multiple separately scoped contribution units. The route locates a bounded decision-relevant evidence family; each unit still has to pass its own scope check before use. Do not encode every market/audience/channel/time dimension into the route ID merely to make the route look deterministic.

Similarly:

```text
reviewed / active
!= current
!= true
!= applicable
```

Review state records contribution vetting. Usage state records current repository disposition. Neither replaces evidence quality, current scope, freshness, or task applicability.

## Evidence discipline

Match evidence strength to the claim.

Local familiarity can be useful evidence for terminology, naturalness, community plausibility, missing distinctions, or candidate hypotheses. It does not by itself establish market-wide prevalence, causal effect, conversion lift, or deterministic cultural behavior.

Preserve contradictions and unknowns. If two credible contributions remain applicable but disagree, resolve the specific decision dimension only when the evidence supports doing so; otherwise narrow the claim, preserve the conflict, or avoid forced adaptation.

Broader regional or cultural evidence may generate a hypothesis or a question to investigate. Absence of a narrower contribution does not turn that broader evidence into inherited local truth.

## Routing and physical organization

Runtime discovery is **decision-first**, not country-first.

When real adaptation knowledge is added, prefer owner-aligned logical namespaces and routes that answer an unresolved decision, for example conceptually:

```text
adapt-messaging.proof-emphasis
adapt-localization.relationship-realization
adapt-content.community-participation
```

These illustrate the naming pattern; `routing-index.json` is the source of truth for which routes actually exist. Add a namespace there only when actual runtime knowledge requires it.

Detailed language, market, audience, channel, category, community, jurisdiction, and time scope belongs inside the contribution unit. Do not create `vi-VN`, `market-vn`, or similar primary runtime packs merely because a contribution concerns that place or language.

Keep the routing manifest as an address table. Do not turn it into a scope registry, scoring engine, precedence system, or duplicate handbook.

## Fork-specific extensions

A private fork may add organization- or context-specific adaptation knowledge without upstreaming it immediately.

Storage location does not create precedence:

```text
private
!= automatically authoritative

upstream
!= automatically authoritative
```

Use actual task scope, provenance, evidence quality, and authoritative organization/product state. If a private finding later generalizes beyond the organization, narrow and re-evidence the generalized claim before proposing it upstream.

## When larger machinery becomes justified

Do not add a dynamic adaptation registry, executable scope matcher, specificity score, precedence engine, or new retrieval subsystem merely because the corpus may grow.

Promote only after a concrete bounded workload demonstrates that this path materially fails and cannot be repaired by local route/section organization:

```text
OPEN DECISION
→ EXISTING OWNER
→ MATCHING ADAPTATION ROUTE
→ SECTION-LOCAL SCOPE CHECK
→ APPLY ONLY DECISION-RELEVANT EVIDENCE
```

A successful promotion case must show a material activation, discovery, addressability, applicability, conflict-resolution, owner-composition, freshness/versioning, or fork-composition failure and why a smaller repair is insufficient.

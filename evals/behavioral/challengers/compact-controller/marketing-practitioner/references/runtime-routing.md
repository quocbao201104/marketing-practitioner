# Runtime routing and handoff reference

Read this file only when owner selection, domain activation, or a state handoff is ambiguous. `routing-index.json` remains the physical source of truth for exact file and heading selectors.

## Namespace activation map

- `content`: cross-environment meaning, representation, audience/interaction, governance/eligibility, mediation, feedback, measurement, or performance diagnosis.
- `commerce`: product/variant/catalog identity, commercial state, product representation, commerce discovery, agentic authority, observation, field evidence, or diagnosis.
- `commercial-design`: configuration/entitlement, payment, terms, allocation/eligibility, modifiers, evidence, decision, transition/history, governance, or handoff.
- `landing-page`: page job/entry state, sequence, proof/risk, visual allocation, action/form, responsive order, commercial comparison, or diagnosis.
- `email`: send decision/state, sequence/history, message/action allocation, continuity, observation, or email decision record.
- `discovery`: need/expression, system-scoped availability, retrieval/selection, representation/commitment, observation, or discovery decision record.
- `paid-media`: objective/signal, control/authority, resource/allocation/buying, delivery/realization, billing/attribution/feedback, owner handoff, or paid decision record.
- `facebook`, `instagram`, `linkedin`, `tiktok`, `x`: only when current mechanics of the named social platform can change the decision.
- `google-commerce`, `amazon`, `tiktok-shop`, `shopee`, `etsy`, `lazada`: only when current provider field, catalog, commercial-state, policy, discovery, checkout, or measurement semantics can change the commerce decision.

Load one logical route first. Add another only when the unresolved dependency crosses the first route's boundary. Never load every namespace because a task spans marketing generally.

## Owner boundaries

- Chapter 01 owns customer-evidence interpretation; Chapter 02 owns segment/ICP/JTBD choice; Chapter 03 owns positioning/value.
- Chapter 04 owns message, claim, proof, and copy; landing-page/email/content owners allocate resolved communication into environments.
- `commercial-design` owns design of commercial conditions; `commerce` represents and interprets product/listing/checkout commercial state.
- Chapter 05 owns causal diagnosis, incrementality, experiments, and treatment effects; domain modules provide the correct event and system state.
- Chapter 06 owns reusable learning, not causal identification.
- `discovery` owns generic discoverability semantics; `commerce` owns product-discovery relations; `paid-media` owns economic allocation and paid delivery.
- Platform modules constrain or inform an owner's decision; a platform does not become the owner merely because it is named.

## Dependency examples

```text
resolved price represented on a page
→ landing-page commercial-comparison
not commercial-design unless a condition remains open

buyer-relative marketplace price
→ commerce commercial-state + relevant provider
not pricing redesign

reported conversion used for bidding?
→ paid-media observation/objective
causal value or incrementality → Chapter 05

indexed in one system, discoverable in another?
→ discovery availability
provider controls only when current specifics matter

click observed, intent inferred
→ domain observation owner
causal or decision-effect question → Chapter 05
```

## State handoffs

### Platform observation → learning

Pass material object/state, representation, audience/pre-state, surface/delivery context, exposure and response opportunity, interaction provenance, allocation/visibility regime, observation unit, history, outcome maturity, attribution rule/window, comparability, and uncertainty. Do not infer preference from non-action or intrinsic quality from policy-mediated interaction.

### Discovery observation → learning or diagnosis

Pass the supported event level—availability/index, retrieval/selection, surfaced representation, impression/position/click/referral, citation, or grounding-query telemetry—with system/surface, definition, unit, aggregation, time/scope, coverage, attribution, and uncertainty. Impression is not attention; click is not relevance; citation is not authority or causality; search interest is not demand.

### Paid-media observation → learning or diagnosis

Pass objective/optimization signal, control/allocation boundary, delivered/rendered representation or exposure opportunity, spend/billing event, attributed outcome, optimization-eligible signal, known feedback role, mediation/history, definition, unit, time/maturity, modeling/coverage, provenance, and uncertainty only when decision-relevant. Campaign is not necessarily resource boundary; targeting input is not reached audience; reported is not optimization feedback; attributed is not causal.

### Commerce observation → learning

Pass product/variant or transaction scope, event/stage, commercial state, outcome/refund maturity, exposure provenance, platform representation, and uncertainty. Preserve displayed versus authoritative checkout/order state and attribution versus incrementality.

### Email observation → learning or next communication

Pass attempt, receiver acceptance, known placement/availability, exposure opportunity, interaction, unsubscribe/complaint/suppression, target action, attribution, provenance, scope, time/maturity, and uncertainty. Tracked open is not verified attention; click is not intent; attributed outcome is not causal.

### Diagnosis → decision or communication

Pass what is established, surviving explanations, decision-changing uncertainty, the next discriminating check, and whether action/no-change is justified. Do not convert a provisional cause into a copy change.

### Causal result → learning

Pass estimand, analysis population, comparison/control, treatment/version, outcome horizon, validity condition or defect, result, uncertainty, and what the result cannot establish when omission would change reuse.

### Customer/relationship state → email

Pass prior contact, relation/endpoint scope, suppression/holdout, blocker, authority/permission, material technical feasibility, and commercial-transition state only when they distinguish send, wait, suppress, exit, other-channel, or different-message decisions.

### Resolved upstream strategy → communication

Pass target context, relevant alternative, positioning/value, message hierarchy, approved claims/proof, trade-offs, product facts, commercial state, permissions, and uncertainty only as required by the downstream artifact. The receiving owner allocates representation; it does not silently redesign upstream state.

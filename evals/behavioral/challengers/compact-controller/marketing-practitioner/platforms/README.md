# Platform Modules

Platform modules specialize the shared handbook for current platform-specific environments. They are **not independent marketing theories** and they are not loaded merely because a platform name appears in a task.

The runtime remains governed by [`../SKILL.md`](../SKILL.md): start from the current job, freeze resolved state, identify the open decision, and load only the smallest platform knowledge that can materially change it.

## Shared model first, platform specialization second

For social/content work, the shared parent is:

- [`../handbook/08-content-environments-and-distribution.md`](../handbook/08-content-environments-and-distribution.md)

For commerce/product-discovery work, the shared parent is:

- [`../handbook/09-commerce-environments-and-product-discovery.md`](../handbook/09-commerce-environments-and-product-discovery.md)

For unresolved package/pricing/terms decisions, use:

- [`../handbook/10-commercial-design-pricing-and-terms.md`](../handbook/10-commercial-design-pricing-and-terms.md)

Do not use a platform module to replace one of those decision layers when the open job belongs there.

## Social / content modules

| Module | Namespace | Use when platform-specific behavior can change... |
| --- | --- | --- |
| [`facebook.md`](facebook.md) | `facebook` | Group governance, Feed/recommendation context, participation permissions, Pages/Profiles, links, visibility, measurement |
| [`instagram.md`](instagram.md) | `instagram` | Feed/Reels/Explore/Search distinctions, audience edges, collaboration, lineage, recommendation eligibility, measurement |
| [`linkedin.md`](linkedin.md) | `linkedin` | Profile vs Company Page source, professional context, network/relationship edges, delivery, Employee Notifications, measurement |
| [`tiktok.md`](tiktok.md) | `tiktok` | For You/Search/LIVE distinctions, sequential representation, interaction provenance, visibility, creator/content mediation, measurement |
| [`x.md`](x.md) | `x` | For You implementation boundaries, candidate sources, interaction provenance, conversation/community context, visibility, measurement |

The shared content grammar stays compact:

```text
actor / source
object
representation
audience state
typed relationship / delivery / permission edge
interaction act
platform / mediation state
observation record

+ provenance
+ scope / relativity
+ history / state transition
```

A platform-local mechanism should remain local unless a concrete cross-platform failure shows the shared model is insufficient.

## Commerce modules

Marketplace and commerce-platform modules live under [`commerce/`](commerce/).

Current modules:

- Google Shopping / Google commerce
- Amazon
- TikTok Shop
- Shopee
- Etsy
- Lazada

See [`commerce/README.md`](commerce/README.md) for the platform map and boundaries.

## Routing

The stable interface is the namespace + logical route in [`../routing-index.json`](../routing-index.json), not the physical heading.

Examples:

```text
facebook.groups
instagram.creator-commerce
linkedin.relationship-edges
tiktok.machine-mediation
x.interaction-provenance
amazon.shop-direct
shopee.commercial-state
```

When helper execution is available:

```bash
python ../scripts/get-knowledge.py --list --namespace instagram
python ../scripts/get-knowledge.py tiktok.machine-mediation
```

Do not turn this README into a duplicate routing manifest. Route-to-heading bindings belong only in `routing-index.json`.

## Fast-path rule

Naming a platform is not enough to justify loading its deep module.

```text
"Shorten this supplied LinkedIn post."
→ narrow adaptation; stay fast if platform mechanics do not change the decision

"Can limited members in this Facebook Group comment?"
→ Facebook governance/participation knowledge is material

"Why did TikTok views rise after paid amplification while leads stayed flat?"
→ platform observation + causal diagnosis are material
```

The goal is platform-correct reasoning **without turning every post, listing, or caption into a platform dissertation**.

## Evidence and freshness

Platform facts are time-sensitive and system-specific. Use the scoped evidence ledgers under [`../references/`](../references/) when provenance is material.

Keep surface, market, actor state, product state, time, and evidence strength explicit. Official documentation can establish a capability or rule without proving a causal growth tactic.
# SaaS Architecture Assumptions And Scaling Checklist

## Source Grounding

Derived from local HTML extractions:

- `fm-indd/toc.ncx`, `index_split_000.html` through `index_split_003.html`: SaaS from cloud environments, enterprise consumption models, TOGAF/ABB/SBB framing, IaaS deployment mapping, hypervisors, load balancing, auto-scaling, multi-tenancy, customization, billing support, upgrades, maintenance, cloud compatibility, security, and cloud reference architecture.
- `crafting-engineering-strategy/toc.ncx`: policy and operations as strategy enforcement.

This is original checklist guidance, not copied text.

## SaaS Assumption Register

| Assumption | Required Decision | Evidence Needed | Downstream Artifact |
|---|---|---|---|
| Tenant model | pooled | siloed | hybrid | bridge | HLD, database design, security controls |
| Enterprise consumption | long-tail SMB | mid-market | vertical enterprise | public-sector | pricing, support, onboarding |
| Customisation | config only | extension points | tenant-specific code | UX spec, release plan |
| Scaling unit | app instance | tenant cell | queue worker | database shard | infrastructure design |
| Billing and metering | user | seat | usage | transaction | finance, support, audit |
| Upgrade model | all tenants at once | ring/canary | tenant opt-in | deployment, release notes |
| Data isolation | logical | schema | database | environment | security, compliance, backup |
| Support model | self-serve | assisted | managed account | adoption/support plan |

## Cloud/IaaS Mapping Checks

1. Map every software building block to compute, storage, network, identity, and observability resources.
2. Define minimum viable deployment size and expected growth deployment size.
3. Identify which components must be stateless for horizontal scaling.
4. Define load-balancer health checks and routing assumptions.
5. Specify auto-scaling trigger, cool-down, minimum, maximum, and cost guardrail.
6. Name shared resources that can create tenant blast radius.
7. Define backup, restore, and per-tenant export assumptions.
8. State what cannot be solved by adding more infrastructure.

## Scaling Requirement Patterns

```text
NFR-SaaS-###: The [component] shall scale from [min load] to [target load] by adding [scaling unit] while maintaining [latency/error/SLO] under [test condition].
```

```text
CTRL-SaaS-###: Tenant [data/config/workload] shall be isolated at [boundary] so that [failure/security/cost] in one tenant does not affect [scope] beyond [threshold].
```

## Rejection Gate

Reject the architecture strategy if:

- it says "cloud" but does not map software building blocks to IaaS/cloud resources
- tenant isolation is not explicit
- scaling strategy lacks measurable triggers and maximum cost guardrails
- upgrade and maintenance model is missing
- billing/metering assumptions are absent for commercial SaaS
- security is treated as a generic NFR instead of tenant, identity, data, operational, and compliance requirements


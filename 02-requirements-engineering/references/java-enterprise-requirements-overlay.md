# Java enterprise requirements overlay

Use this overlay when a requirement, strategy, validation, traceability, or
transition deliverable constrains a Java/JVM estate. It specifies what must be
known and proved. It does not prescribe Java code or duplicate the companion
engineering capability.

Current version and lifecycle claims must be verified through the
[Digital Research Engine](https://github.com/peterbamuhigire/digital-research-skills)
and the `docs/source-registers/java-enterprise.md` companion register in the
[Chwezi Dev Engine](https://github.com/peterbamuhigire/chwezi-dev-engine).
Project/runtime evidence outranks the register. Record unknown fields as
`NOT ASSESSED`.

## Platform evidence card

| Field | Required evidence |
|---|---|
| JDK and vendor | Exact distribution, build string, licence/support owner and production approval |
| Java level | Source, target/release and bytecode compatibility |
| Framework | Spring, Jakarta, Quarkus, Micronaut, Helidon or other exact managed line |
| Specifications | Jakarta/Java EE profile and namespace generation |
| Persistence | JDBC/JPA/Hibernate/jOOQ style, driver, pool, database and migration tool |
| Build | Wrapper, Maven/Gradle version, repositories, BOM/platform and lock/convergence evidence |
| Runtime | Executable JAR, native image, application server, VM or container |
| Deployment | OS/image, Kubernetes/cloud/application-server estate and rollout mechanism |
| Support | Current state, uncertainty, source/access/review dates and accountable owner |

Do not write "latest Java" or "current Spring" as a requirement. State a
supported-family policy, compatibility constraints, evidence source, review
trigger and exception authority.

## Requirement discovery

Elicit the business consequence and acceptance evidence for:

- transaction boundaries, concurrency conflicts, duplicate commands and
  uncertain commit outcomes;
- throughput, concurrency, latency percentiles, batch window, startup and
  memory/resource ceilings;
- synchronous, asynchronous, blocking, non-blocking and ordered-delivery needs;
- timeouts, cancellation, bounded queues, backpressure, retry budgets and
  dependency-failure behaviour;
- API, event, schema and database backward compatibility;
- authentication, authorization, tenant isolation, secrets, audit records,
  sensitive-data handling and dependency provenance;
- logs, metrics, traces, health, JFR/diagnostic access, alerts and operational
  ownership;
- graceful startup/shutdown, rolling compatibility, recovery, reconciliation,
  rollback or roll-forward, and retirement.

Technology choices are constraints only when a justified policy, existing
estate, support obligation or interoperability need makes them necessary.
Otherwise capture the outcome and decision criteria for architecture.

## Acceptance oracles

| Behaviour | Minimum observable oracle |
|---|---|
| Normal transaction | Committed business result and invariant reconciliation |
| Duplicate request/message | One authorised business effect; deterministic prior result or safe rejection |
| Concurrent update | Defined winner/conflict outcome with no silent lost update |
| Timeout/cancellation | Bounded completion and known downstream/transaction state |
| Partial dependency failure | Defined degradation, retry limit and operator-visible evidence |
| Authorization denial | No protected effect or disclosure; auditable denial where required |
| API/event evolution | Named old/new consumer compatibility checks |
| Data migration | Row/value/invariant reconciliation and resumable or repairable failure path |
| Performance | Named workload/environment with p50/p95/p99, throughput, errors and resource use |
| Resource exhaustion | Bounded queue/pool behaviour and recovery without silent loss |
| Deployment | Old/new version and schema coexistence for the rollout window |
| Recovery | Measured restoration/failover result against approved RTO/RPO where applicable |
| Release | Build, test, security, migration, telemetry, owner and rollback evidence statuses |

Line coverage, a successful package command, or a plausible design is not a
business acceptance oracle.

## Modernisation contract

For Java/JDK, Spring, `javax.*` to `jakarta.*`, application-server,
database-driver, build-tool, container or architecture migration, require:

1. current estate and support-risk inventory;
2. target state and authoritative compatibility matrix;
3. behaviour, data, performance and operational baseline;
4. deprecated/removed API and dependency impact;
5. staged transitions with separately verifiable checkpoints;
6. old/new API, event, schema and runtime coexistence windows;
7. data reconciliation and production telemetry;
8. rollback boundaries or explicit roll-forward recovery;
9. canary/pilot decision criteria and stop conditions;
10. retirement and support-handoff evidence.

Do not make a big-bang rewrite the default. Do not require a direct jump across
framework generations when an intermediate compatibility stage materially
reduces risk.

## Quality and production evidence

Use `PASS`, `PARTIAL`, `FAIL`, `NOT ASSESSED`, or `NOT APPLICABLE`
for correctness, data integrity, security, reliability, availability,
performance, scalability, maintainability, testability, observability,
operability, portability, compatibility, recoverability, auditability, supply
chain, documentation and lifecycle.

A production-readiness statement must expose missing load, failover, restore,
rollback, security, licensing/support, and target-environment evidence. Missing
evidence never becomes a pass.

## Handoff map

| Requirement concern | SRS owner | Engineering handoff |
|---|---|---|
| Architecture and failure boundaries | HLD/LLD and ADR routes | `system-architecture-design` plus Java capability |
| HTTP/API contract | API specification route | `api-design-first` plus Java capability |
| Schema/data migration | Database design route | database specialist plus Java persistence layer |
| Security/privacy | Security and compliance routes | security specialist plus Java security implementation |
| Tests and deterministic oracles | Test-plan and validation routes | `advanced-testing-strategy` plus Java test tooling |
| SLOs/telemetry/operations | Monitoring, runbook and readiness routes | observability/reliability plus Java JVM diagnostics |
| Deployment/release/rollback | Deployment and transition routes | CI/CD, release, Kubernetes/cloud plus Java packaging |
| Java implementation/diagnosis | Requirements remain source of truth | Chwezi Dev Engine `languages/java-enterprise-development` skill |

For financial or accounting behaviour, route policy to the canonical accounting
engine. The Java implementation may enforce approved rounding, currency,
posting, idempotency and audit requirements, but the SRS must not invent
accounting doctrine.

## Currentness record

For every mutable technical constraint record:

`claim_id, owner/source, scope, version/publication date, access date,
freshness class, support status, uncertainty, next review date, evidence
locator`.

Review on a new Java LTS/feature GA, framework or Jakarta generation, build-tool
major, application-server or database-driver support change, licensing change,
or relevant security advisory. Routine patches require doctrine change only
when they alter support, security, compatibility, or accepted behaviour.

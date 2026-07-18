---
name: 06-infrastructure-design
description: Use when a scored decision gate shows that availability, scale, distributed deployment, security or recovery needs infrastructure design beyond the HLD; use HLD for logical architecture and deployment planning for release execution.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
---
# Infrastructure Design Skill
<!-- dual-compat-start -->
## Use When

- Non-trivial infrastructure quality attributes require topology, capacity, observability, continuity and operating ownership.

## Do Not Use When

- Do not use by default for a simple system that fails the score gate, or to name cloud services without verified constraints.

## Required Inputs

| Artefact | Source or provider | Required? | Missing behaviour |
|---|---|---|---|
| HLD, workloads and quality targets | Architecture and requirements artefacts | Required | Stop if availability, recovery or capacity targets are undefined. |
| Environment, security, cost and operating constraints | Platform, security, finance and operations owners | Required | Produce options and gaps when provider facts or budgets are unavailable. |

## Workflow

1. Read the named inputs and confirm their approval, version and unresolved decisions.
2. Apply the decision rules below before drafting; stop on a missing authority, unsafe assumption or unresolved scope driver.
3. Produce the Infrastructure Design and decision-gate evidence through the existing domain procedure and load only the references needed for the chosen branch.
4. Trace each material statement in the Infrastructure Design and decision-gate evidence to an input, decision or explicitly qualified assumption.
5. Verify the observable acceptance conditions, record unassessed checks, and hand the artefacts to their named consumers.
6. If validation fails, recover by correcting the source decision or artefact and rerun the affected check; do not weaken the acceptance condition.

## Outputs

| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Infrastructure Design and decision-gate evidence | Platform, security, delivery and operations teams | Topology traces to measured targets; failure domains, capacity, observability, backup, recovery, cost and ownership have verification methods. |

## Evidence Produced

| Evidence | Consumer | Acceptance condition |
|---|---|---|
| Source and decision trace | Reviewer and downstream owner | Each material statement cites an approved input, named decision or qualified open issue. |
| Completed verification record | Release or phase gate owner | Every applicable check records pass/fail; unavailable checks remain `not assessed`. |

## Capability and permission boundaries

Read-only is the default for analysis, review, evaluation and planning. Read and search access to authorised project artefacts are required. Editing is limited to an explicitly requested project deliverable. Execution may run document, syntax or validation checks. Network access is used only for facts that require current verification. Do not publish, spend, change production, approve policy, or claim certification without explicit authority.

## Degraded mode

If any required capability is unavailable, return the narrowest useful qualified Infrastructure Design and decision-gate evidence draft plus a gap register showing the missing item, affected sections, risk and owner. Never convert an unassessed check into a pass.

## Decision Rules

| Choice | Action | Failure or risk avoided |
|---|---|---|
| Score gate meets infrastructure threshold | Produce the full design | Complex needs receive operational depth |
| Score gate is below threshold | Keep deployment notes in HLD | Unneeded platform complexity is avoided |

## Quality Standards

- Preserve repository terminology and trace every material choice to project context.
- Use deterministic acceptance conditions; replace vague quality claims with an observable check, threshold or named approval.
- Cover error, empty, edge, recovery and operational cases relevant to this skill.
- Verify standards, citations, APIs and package names before relying on them; qualify what cannot be checked.
- Stop release for a failed safety, security, legal, financial, accessibility or data-integrity gate.

## Anti-Patterns

- Copying a reference cloud diagram. Fix: derive topology from workload and failure targets.
- Claiming high availability with one failure domain. Fix: map redundancy and failover tests.
- Sizing from peak guesses. Fix: state workload assumptions and headroom rule.
- Omitting recovery exercises. Fix: define restore and failover evidence.
- Naming alerts without owners. Fix: tie every actionable alert to a runbook and response owner.

## References

- [Reliability patterns](references/reliability-patterns.md)
- [Monitoring and observability](references/monitoring-observability.md)
- [Scalability patterns](references/scalability-patterns.md)
<!-- dual-compat-end -->




## Overview

This is the sixth skill in Phase 03 (Design Documentation). It produces an Infrastructure Design document covering scalability, caching, messaging, load balancing, database scaling, reliability patterns, monitoring, and disaster recovery. The skill is **optional** and gated by a score-based evaluation that determines whether the project's non-functional requirements warrant a dedicated infrastructure document. When the gate score falls below the threshold, infrastructure concerns shall be noted in `HLD.md` instead.

## When to Use

- After `01-high-level-design` completes and `projects/<ProjectName>/<phase>/<document>/HLD.md` exists.
- When `projects/<ProjectName>/<phase>/<document>/SRS_Draft.md` contains non-functional requirements with measurable availability, scalability, or performance targets.
- When `projects/<ProjectName>/_context/tech_stack.md` specifies cloud or distributed deployment targets.
- Optionally when `projects/<ProjectName>/_context/quality_standards.md` defines SLA or compliance constraints.

## Quick Reference

| Attribute    | Value |
|--------------|-------|
| **Inputs**   | `projects/<ProjectName>/<phase>/<document>/HLD.md`, `projects/<ProjectName>/<phase>/<document>/SRS_Draft.md`, `projects/<ProjectName>/_context/tech_stack.md`; optionally `projects/<ProjectName>/_context/quality_standards.md` |
| **Output**   | `projects/<ProjectName>/<phase>/<document>/Infrastructure_Design.md` |
| **Tone**     | Technical, precise, infrastructure-focused |
| **Standards** | IEEE 1016-2009, ISO/IEC 25010, ISO/IEC 22237 |
| **Sources**  | "System Design - The Big Archive" (ByteByteGo 2024) |

## Input Files

| File | Location | Required | Purpose |
|------|----------|----------|---------|
| HLD.md | `projects/<ProjectName>/<phase>/<document>/HLD.md` | Yes | Architectural style, component boundaries, deployment topology |
| SRS_Draft.md | `projects/<ProjectName>/<phase>/<document>/SRS_Draft.md` | Yes | Non-functional requirements, constraints, performance targets |
| tech_stack.md | `projects/<ProjectName>/_context/tech_stack.md` | Yes | Infrastructure targets, cloud provider, runtime environment |
| quality_standards.md | `projects/<ProjectName>/_context/quality_standards.md` | No | SLA definitions, compliance constraints, uptime targets |

## Output Files

| File | Location | Description |
|------|----------|-------------|
| Infrastructure_Design.md | `projects/<ProjectName>/<phase>/<document>/Infrastructure_Design.md` | Complete infrastructure design with scalability, reliability, caching, monitoring, and DR sections |

## Core Instructions

Follow these steps in order. Halt and notify the user if a required input file is missing.

### Step 0: Decision Gate -- Infrastructure Necessity Scoring

Before generating the document, evaluate six criteria against the input files to determine whether a full infrastructure design is warranted.

#### Scoring Criteria

| # | Criterion | Weight | Auto-Assessment Source |
|---|-----------|--------|------------------------|
| 1 | Expected concurrent users > 1,000 | 3 | `SRS_Draft.md` Section 3.5 (Performance Requirements) or `quality_standards.md` |
| 2 | 99.9%+ uptime requirement | 3 | `SRS_Draft.md` Section 3.5 or `quality_standards.md` SLA definitions |
| 3 | Geographic distribution needed | 2 | `SRS_Draft.md` Section 3.4 (Design Constraints) or `tech_stack.md` multi-region references |
| 4 | Real-time processing requirements | 2 | `SRS_Draft.md` Section 3.2 (Functional Requirements) -- WebSocket, streaming, sub-second latency |
| 5 | Data volume > 100 GB | 2 | `SRS_Draft.md` Section 3.5 or database sizing references in `tech_stack.md` |
| 6 | Regulatory data residency requirements | 2 | `SRS_Draft.md` Section 3.5.3 (Security) or `quality_standards.md` compliance section |

#### Scoring Formula

$$Score = \sum_{i=1}^{6} (Weight_i \times YesFlag_i)$$

Where $YesFlag_i = 1$ if the criterion is met, $0$ otherwise.

**Maximum possible score**: 14 (all criteria met)
**Minimum possible score**: 0 (no criteria met)

#### Decision Thresholds

| Score Range | Decision | Action |
|-------------|----------|--------|
| 7--14 | **Full Document Recommended** | Proceed with all infrastructure design sections. |
| 4--6 | **Document Optional** | Present score and rationale to user. Await confirmation before proceeding. |
| 0--3 | **Document Not Recommended** | Skip generation. Append a brief infrastructure summary to `HLD.md` Section 8 (Cross-Cutting Concerns). |

Tag all auto-assessed criteria with `[AUTO-ASSESSED]` and present to the user for confirmation before calculating the final score.

#### Override Protocol

- **Overriding "Not Recommended" to proceed**: Log the override. Include a note in the Document Header: "Note: Decision gate score of [X] did not meet the threshold of 4. Generated at user request."
- **Overriding "Recommended" to skip**: Log the override. Note the skip decision in `HLD.md`.

### Step 1: Read Context Files

Read `HLD.md` and `SRS_Draft.md` from `projects/<ProjectName>/<phase>/<document>/`. Read `tech_stack.md` from `projects/<ProjectName>/_context/`. Optionally read `quality_standards.md` from `projects/<ProjectName>/_context/`. Log the absolute path of each file read. If any required file is missing, halt execution and report the gap.

### Step 2: Scalability Strategy

Analyze the SRS performance requirements and HLD deployment topology to determine the scalability approach.

The system shall document:

- **Scaling Direction**: Horizontal vs. vertical analysis with rationale citing SRS constraints.
- **Auto-Scaling Rules**: Define scaling policies using target-tracking, step, or scheduled strategies.
- **Scaling Triggers**: Specify measurable thresholds:
  - CPU utilization > 70%
  - Memory utilization > 80%
  - Request queue depth > 1,000
  - Response latency p95 > target SLA
- **Scaling Limits**: Define minimum and maximum instance counts with cost justification.
- **Statelessness Requirements**: Identify components that shall be stateless for horizontal scaling. Reference `references/scalability-patterns.md`.

### Step 3: Caching Architecture

The system shall define a multi-layer caching strategy aligned with the data flow paths in `HLD.md`.

Document each cache layer:

| Layer | Technology | TTL | Invalidation | Purpose |
|-------|-----------|-----|-------------|---------|
| Browser | HTTP Cache-Control headers | Varies | Versioned URLs | Static asset caching |
| CDN | CloudFront / Cloudflare / Akamai | 1-24 hrs | Purge API | Geographic distribution |
| Reverse Proxy | Varnish / Nginx | 1-60 min | Event-driven | Full-page or fragment caching |
| Application | Redis / Memcached | 5-30 min | Write-through or write-behind | Session, query result, computed value caching |
| Database | Query cache / materialized views | Varies | Refresh on write | Expensive query optimization |

The system shall specify:

- Cache invalidation strategy (TTL-based, event-driven, or hybrid)
- Write-through vs. write-behind trade-offs for each layer
- Cache warming procedures for cold-start scenarios
- Thundering herd prevention (locking, probabilistic early expiration)
- Reference `references/caching-strategies.md`

### Step 4: Message Queue / Event Architecture

The system shall define asynchronous processing patterns for decoupled communication.

Document:

- **Queue Selection**: Criteria for choosing between technologies (RabbitMQ, Apache Kafka, Amazon SQS, Redis Streams) based on ordering guarantees, throughput, and durability requirements.
- **Messaging Patterns**: Pub/sub, point-to-point, fan-out, or request-reply with rationale.
- **Dead Letter Queues (DLQ)**: Configuration for messages that fail processing after maximum retry attempts.
- **Retry Policies**: Define retry count, backoff strategy (exponential with jitter), and maximum delay.
- **Ordering Guarantees**: FIFO vs. best-effort with partition key strategy.
- **Event Schema**: Versioning strategy (schema registry, backward compatibility).
- Reference `references/distributed-systems.md`

### Step 5: Load Balancing

The system shall define load balancing configuration for each entry point identified in `HLD.md`.

Document:

- **Algorithm Selection**: Round-robin, least-connections, IP-hash, or weighted -- with rationale tied to SRS requirements.
- **Health Checks**: Liveness, readiness, and startup probe definitions with intervals and thresholds.
- **Session Persistence**: Sticky sessions (when required) with cookie-based or IP-based affinity.
- **SSL/TLS Termination**: Termination point, certificate management, cipher suite policy.
- **Rate Limiting**: Request rate limits per client, per endpoint, and global thresholds.

### Step 6: Database Scaling

The system shall define database scaling strategy aligned with data models from `04-database-design`.

Document:

- **Read Replicas**: Replica count, replication lag tolerance, read routing strategy.
- **Write Scaling**: Sharding strategy selection with trade-off analysis:
  - Range-based sharding: ordered access, potential hotspots
  - Hash-based sharding: even distribution, no range queries
  - Directory-based sharding: flexible mapping, single point of failure
- **Connection Pooling**: Pool size, timeout, idle connection management.
- **Query Routing**: Read/write splitting logic, consistency requirements for read-after-write.
- Reference `references/scalability-patterns.md`

### Step 7: Reliability Patterns

The system shall define fault tolerance and resilience patterns per ISO 25010 reliability characteristics.

Document each pattern with configuration parameters:

- **Circuit Breaker**: Open, half-open, and closed states. Define failure threshold (e.g., 5 failures in 30 seconds), reset timeout, and half-open probe count.
- **Retry with Exponential Backoff**: Base delay, multiplier, jitter range, maximum retries. Formula: $Delay = BaseDelay \times 2^{attempt} + Random(0, Jitter)$
- **Idempotency Keys**: Key generation strategy, storage TTL, duplicate detection window.
- **Bulkhead Isolation**: Thread pool or semaphore isolation per downstream dependency. Define pool size and queue capacity.
- **Graceful Degradation**: Define degradation tiers (full service, reduced features, maintenance mode) with trigger conditions.
- **Timeout Strategy**: Connect timeout, read timeout, and overall request timeout per dependency.
- Reference `references/reliability-patterns.md`

### Step 8: Monitoring and Observability

The system shall define a comprehensive observability strategy covering metrics, logging, tracing, and alerting.

#### Metrics

- **RED Method** (for services): Rate of requests, Error rate, Duration of requests.
- **USE Method** (for resources): Utilization, Saturation, Errors.
- Define metric collection interval, retention period, and aggregation strategy.

#### Logging

- **Format**: Structured JSON with mandatory fields: `timestamp`, `level`, `service`, `correlation_id`, `message`, `context`.
- **Levels**: TRACE, DEBUG, INFO, WARN, ERROR, FATAL with production defaults.
- **Correlation IDs**: Propagation mechanism across service boundaries.

#### Distributed Tracing

- Span context propagation (W3C Trace Context or B3).
- Sampling strategy (head-based or tail-based) with sampling rate.

#### Alerting

| Severity | Response Time | Example | Escalation |
|----------|--------------|---------|------------|
| P1 - Critical | 15 min | Service down, data loss risk | On-call page, incident commander |
| P2 - High | 1 hour | Degraded performance, partial outage | On-call notification |
| P3 - Medium | 4 hours | Elevated error rate, capacity warning | Team channel alert |
| P4 - Low | Next business day | Non-critical anomaly | Dashboard review |

Reference `references/monitoring-observability.md`

### Step 9: Disaster Recovery

The system shall define disaster recovery targets and procedures aligned with SRS availability requirements.

Document:

- **RPO (Recovery Point Objective)**: Maximum acceptable data loss measured in time. Derive from SRS Section 3.5.
- **RTO (Recovery Time Objective)**: Maximum acceptable downtime. Derive from SRS Section 3.5.
- **Backup Strategy**: Frequency, retention, storage location, encryption, restoration testing cadence.
- **Failover Procedures**: Automatic vs. manual failover, DNS failover TTL, database failover (promote replica).
- **Data Replication Topology**: Synchronous vs. asynchronous replication, cross-region strategy, conflict resolution for multi-primary.
- **DR Testing**: Tabletop exercise frequency, failover drill schedule, chaos engineering integration.

### Step 10: Generate Traceability Table

Produce a traceability table linking every infrastructure design decision to its originating SRS requirement and HLD component:

| Infrastructure Component | SRS Requirement | HLD Component | Rationale |

Every section from Steps 2-9 shall have at least one entry in this table.

## Output Format

The generated `Infrastructure_Design.md` shall contain these sections in order:

1. Document Header (project name, date, version, standards, decision gate score)
2. Decision Gate Results (scoring worksheet, decision, any overrides)
3. Scalability Strategy
4. Caching Architecture
5. Message Queue / Event Architecture
6. Load Balancing
7. Database Scaling
8. Reliability Patterns
9. Monitoring and Observability (9.1 Metrics, 9.2 Logging, 9.3 Distributed Tracing, 9.4 Alerting)
10. Disaster Recovery
11. Traceability Matrix
12. Appendix A: Glossary

## Common Pitfalls

| Pitfall | Remedy |
|---------|--------|
| Scaling strategy without measurable triggers | Every auto-scaling rule shall reference a specific metric threshold |
| Cache invalidation not defined | Every cache layer shall specify its invalidation mechanism |
| Missing dead letter queue configuration | Every message queue shall define DLQ handling and retry limits |
| Reliability patterns without configuration values | Circuit breakers, retries, and timeouts shall include specific numeric parameters |
| Monitoring without alerting thresholds | Every metric shall map to at least one alert severity level |
| DR targets without testing schedule | RPO/RTO targets shall include validation frequency |

## Verification Checklist

- [ ] Decision gate evaluation is completed and documented with score.
- [ ] `Infrastructure_Design.md` exists in `projects/<ProjectName>/<phase>/<document>/` with all sections populated (if gate passed).
- [ ] Scalability strategy specifies measurable auto-scaling triggers and limits.
- [ ] Caching architecture covers at least three layers with invalidation strategies.
- [ ] Reliability patterns include circuit breaker state definitions and retry formulas.
- [ ] Monitoring section defines RED and USE metrics with alerting thresholds.
- [ ] DR section specifies RPO/RTO with numeric targets derived from SRS.
- [ ] Traceability table maps every infrastructure component to an SRS requirement.

## Integration

| Direction | Skill | Relationship |
|-----------|-------|-------------|
| Upstream | 01-high-level-design | Consumes `HLD.md` for architecture and deployment topology |
| Upstream | Phase 02 (Requirements Engineering) | Consumes `SRS_Draft.md` for non-functional requirements |
| Peer | 04-database-design | Aligns database scaling with data model design |
| Downstream | Phase 05 (Testing) | Infrastructure design informs performance and reliability test plans |
| Downstream | Phase 06 (Deployment & Operations) | DR and monitoring sections feed deployment runbooks |

## Standards

- **IEEE 1016-2009 Sec 5** -- Architectural design viewpoints and infrastructure design rationale
- **ISO/IEC 25010** -- Quality model: reliability, performance efficiency, security characteristics
- **ISO/IEC 22237** -- Data centre facilities and infrastructures
- **"System Design - The Big Archive" (ByteByteGo 2024)** -- Scalability, caching, and distributed systems patterns

## Resources

- `references/scalability-patterns.md` -- Horizontal/vertical scaling, auto-scaling policies, database scaling patterns
- `references/distributed-systems.md` -- CAP theorem, consistency models, event-driven architecture, message queue patterns
- `references/reliability-patterns.md` -- Circuit breaker, retry, bulkhead, timeout, health check, graceful degradation
- `references/caching-strategies.md` -- Cache-aside, read/write-through, multi-layer caching, invalidation strategies
- `references/monitoring-observability.md` -- RED/USE methods, structured logging, distributed tracing, alerting practices
- `README.md` -- Quick-start guide for this skill

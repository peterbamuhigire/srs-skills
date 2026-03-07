# Reliability Patterns Reference

## Purpose

This reference provides fault tolerance and resilience patterns for infrastructure design. It covers circuit breakers, retry strategies, bulkhead isolation, timeouts, health checks, graceful degradation, and chaos engineering principles.

## Reference Standard

- ISO/IEC 25010 Section 4.2.4: Reliability -- maturity, availability, fault tolerance, recoverability
- "System Design - The Big Archive" (ByteByteGo 2024) Ch. 10: Reliability patterns

## Circuit Breaker Pattern

### State Machine

The circuit breaker shall operate as a three-state machine:

| State | Behavior | Transition Condition |
|-------|----------|---------------------|
| **Closed** | Requests pass through normally. Failures are counted. | Failure count exceeds threshold within the monitoring window: transition to Open |
| **Open** | All requests are rejected immediately with a fallback response. No calls to the downstream service. | Reset timeout expires: transition to Half-Open |
| **Half-Open** | A limited number of probe requests are allowed through. | Probe succeeds: transition to Closed. Probe fails: transition back to Open |

### Configuration Parameters

| Parameter | Recommended Range | Description |
|-----------|------------------|-------------|
| Failure threshold | 5-10 failures | Number of failures before opening the circuit |
| Monitoring window | 30-60 seconds | Time window for counting failures |
| Reset timeout | 30-120 seconds | Duration the circuit remains open before probing |
| Half-open probe count | 1-3 requests | Number of test requests in half-open state |
| Success threshold | 3-5 successes | Consecutive successes required to close the circuit |

### Fallback Strategies

When the circuit is open, the system shall execute one of these fallback strategies:

| Strategy | Description | Use Case |
|----------|-------------|----------|
| Cached response | Return the last successful response | Read operations with tolerance for staleness |
| Default value | Return a predefined safe default | Non-critical feature data |
| Graceful error | Return a user-friendly error with retry guidance | Critical operations that cannot be approximated |
| Alternative service | Route to a backup or degraded service | High-availability requirements |

## Retry Strategies

### Exponential Backoff with Jitter

The system shall implement retry delays using exponential backoff with randomized jitter to prevent thundering herd:

$$Delay = min(BaseDelay \times 2^{attempt} + Random(0, Jitter), MaxDelay)$$

| Parameter | Recommended Value | Description |
|-----------|------------------|-------------|
| Base delay | 100-500 ms | Initial retry delay |
| Multiplier | 2 | Exponential factor |
| Jitter | 0 to base delay | Random component to decorrelate retries |
| Max delay | 30-60 seconds | Upper bound on retry delay |
| Max retries | 3-5 | Maximum number of retry attempts |

### Retry Decision Matrix

| Error Type | Retryable | Rationale |
|-----------|-----------|-----------|
| 5xx Server Error | Yes | Transient server failure |
| 429 Too Many Requests | Yes (with Retry-After header) | Rate limiting, back off as directed |
| 408 Request Timeout | Yes | Transient timeout |
| 4xx Client Error (except 408, 429) | No | Client-side issue will not resolve on retry |
| Connection refused | Yes (limited) | Service may be restarting |
| DNS resolution failure | Yes (limited) | Transient DNS issue |

### Retry Budget

The system shall enforce a retry budget to prevent retry storms: no more than 10-20% of total requests shall be retries. If the retry budget is exhausted, the system shall fail fast rather than queue additional retries.

## Bulkhead Pattern

### Thread Pool Isolation

The system shall allocate a dedicated thread pool for each downstream dependency:

| Dependency | Pool Size | Queue Capacity | Timeout |
|-----------|-----------|---------------|---------|
| Payment Service | 10 | 20 | 5s |
| Notification Service | 5 | 10 | 3s |
| Search Service | 8 | 15 | 2s |

When a pool is exhausted, requests to that dependency shall fail immediately without consuming resources allocated to other dependencies.

### Semaphore Isolation

For lightweight isolation (lower overhead than thread pools), the system shall use semaphore-based concurrency limits:

- Maximum concurrent requests per dependency.
- No queuing; excess requests are rejected immediately.
- Lower resource overhead than thread pools.

## Timeout Patterns

### Timeout Hierarchy

The system shall define timeouts at three levels:

| Level | Timeout | Purpose |
|-------|---------|---------|
| Connect timeout | 1-3 seconds | Maximum time to establish a TCP connection |
| Read timeout | 5-30 seconds | Maximum time to receive a response after connection |
| Overall timeout | 10-60 seconds | Maximum end-to-end time for the entire operation |

### Timeout Propagation

The system shall propagate deadline information across service boundaries:

- Incoming request deadline = original timeout minus elapsed time.
- Each downstream call shall use the remaining deadline as its timeout.
- If the remaining deadline is less than the minimum useful timeout, the system shall fail fast.

## Health Check Patterns

### Liveness Probe

Determines whether the service process is running and not deadlocked:

| Property | Value |
|----------|-------|
| Endpoint | `GET /healthz` or `GET /health/live` |
| Check | Process is responsive, not in a deadlock state |
| Failure action | Restart the container/process |
| Interval | 10-30 seconds |
| Failure threshold | 3 consecutive failures |

### Readiness Probe

Determines whether the service is ready to accept traffic:

| Property | Value |
|----------|-------|
| Endpoint | `GET /ready` or `GET /health/ready` |
| Check | All dependencies (database, cache, queues) are reachable |
| Failure action | Remove from load balancer rotation |
| Interval | 5-15 seconds |
| Failure threshold | 2 consecutive failures |

### Startup Probe

Determines whether the service has completed initialization:

| Property | Value |
|----------|-------|
| Endpoint | `GET /health/startup` |
| Check | Migrations complete, caches warmed, connections established |
| Failure action | Delay liveness/readiness checks |
| Interval | 5-10 seconds |
| Failure threshold | 30 (allow up to 5 minutes for slow starts) |

## Graceful Degradation Strategies

### Degradation Tiers

The system shall define operational tiers with explicit trigger conditions:

| Tier | State | Features Available | Trigger |
|------|-------|-------------------|---------|
| Tier 0 | Full Service | All features operational | Normal operation |
| Tier 1 | Reduced Features | Core features only; disable recommendations, analytics, non-critical notifications | Error rate > 5% or latency p99 > 2x SLA |
| Tier 2 | Essential Only | Authentication, core transactions only; disable search, reporting | Error rate > 15% or dependency failure |
| Tier 3 | Maintenance Mode | Static maintenance page with status updates | Cascading failure or data integrity risk |

### Feature Flags for Degradation

The system shall use feature flags to enable/disable functionality without deployment:

- Kill switches for non-critical features.
- Percentage-based rollout for gradual recovery.
- User-segment targeting (internal users first, then general availability).

## Chaos Engineering Principles

### Core Practices

1. **Define steady state**: Establish measurable indicators of normal system behavior (request rate, error rate, latency percentiles).
2. **Hypothesize**: Predict how the system shall behave when a specific failure is injected.
3. **Inject failure**: Introduce controlled failures (network latency, service crash, disk full, clock skew).
4. **Observe**: Compare actual behavior to the hypothesis.
5. **Fix**: Address gaps between expected and actual resilience.

### Failure Injection Categories

| Category | Examples | Tools |
|----------|---------|-------|
| Network | Latency injection, packet loss, partition | tc, Toxiproxy, Chaos Mesh |
| Process | Service crash, memory exhaustion, CPU stress | kill, stress-ng, Litmus |
| Infrastructure | Availability zone failure, disk full | Cloud provider fault injection, Gremlin |
| Application | Exception injection, response corruption | Application-level chaos libraries |

### Safety Controls

- The system shall run chaos experiments in non-production environments first.
- The system shall define blast radius limits (single service, single AZ, single region).
- The system shall have automated rollback mechanisms for all experiments.
- The system shall schedule experiments during business hours with incident response on standby.

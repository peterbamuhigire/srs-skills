# Scalability Patterns Reference

## Purpose

This reference provides scalability patterns and strategies for infrastructure design decisions. It covers horizontal and vertical scaling, auto-scaling policies, database scaling, CDN patterns, and connection pooling.

## Reference Standard

- ISO/IEC 25010 Section 4.2.1: Performance efficiency -- capacity
- "System Design - The Big Archive" (ByteByteGo 2024) Ch. 3: Scaling strategies

## Horizontal Scaling (Scale Out)

### Stateless Services

The system shall design application-tier services as stateless to enable horizontal scaling. Stateless services:

- Store no session data in local memory or filesystem.
- Externalize session state to a shared store (Redis, database, or distributed cache).
- Allow any instance to serve any request without affinity.

### Shared-Nothing Architecture

Each processing node shall operate independently without sharing memory or disk with other nodes. Benefits:

| Property | Description |
|----------|-------------|
| Fault isolation | Failure of one node does not cascade to others |
| Linear scaling | Adding nodes increases capacity proportionally |
| Simplified deployment | Nodes are identical and independently deployable |

### When to Use Horizontal Scaling

| Indicator | Rationale |
|-----------|-----------|
| Traffic patterns are spiky or seasonal | Auto-scaling adjusts capacity dynamically |
| Requests are independent and parallelizable | Stateless design distributes load evenly |
| Cost optimization is important | Scale down during low-traffic periods |
| Availability requirements exceed single-node SLA | Multiple nodes provide redundancy |

## Vertical Scaling (Scale Up)

### When Vertical Scaling Is Appropriate

| Indicator | Rationale |
|-----------|-----------|
| Application is inherently single-threaded | Horizontal scaling provides no benefit |
| Database write performance is the bottleneck | Faster CPU/IO on a single node may suffice before sharding |
| Simplicity is prioritized over maximum throughput | Fewer nodes reduce operational complexity |
| Workload is memory-bound with large working sets | Larger memory avoids disk IO |

### Vertical Scaling Limits

The system shall document the maximum vertical scaling boundary for each component. Beyond this boundary, the architecture shall transition to horizontal scaling or sharding.

## Auto-Scaling Policies

### Target Tracking

The system shall define a target metric value (e.g., average CPU utilization = 60%). The auto-scaler adjusts instance count to maintain the target.

```
Policy: TargetTracking
  Metric: CPUUtilization
  Target: 60%
  ScaleOutCooldown: 300s
  ScaleInCooldown: 300s
```

### Step Scaling

The system shall define step adjustments based on metric alarm thresholds:

| Metric Range | Action |
|-------------|--------|
| CPU 60-70% | Add 1 instance |
| CPU 70-85% | Add 2 instances |
| CPU > 85% | Add 4 instances |
| CPU < 40% | Remove 1 instance |
| CPU < 25% | Remove 2 instances |

### Scheduled Scaling

The system shall define time-based scaling for predictable traffic patterns:

| Schedule | Min Instances | Max Instances | Rationale |
|----------|--------------|--------------|-----------|
| Weekday 08:00-18:00 | 4 | 20 | Business hours peak |
| Weekday 18:00-08:00 | 2 | 8 | Off-hours baseline |
| Weekend | 2 | 6 | Reduced weekend traffic |

## Database Scaling Patterns

### Read Replicas

Read replicas distribute read queries across multiple database instances:

- **Replication Method**: Asynchronous (eventual consistency) or synchronous (strong consistency with latency cost).
- **Replica Count**: Determined by read-to-write ratio. Systems with > 80% reads benefit most.
- **Replication Lag**: The system shall define acceptable lag (e.g., < 1 second for user-facing queries).
- **Routing**: Application-level routing or proxy-based (ProxySQL, PgBouncer, Amazon RDS Proxy).

### Sharding Strategies

| Strategy | Mechanism | Advantages | Disadvantages |
|----------|-----------|-----------|---------------|
| Range-based | Partition by key range (e.g., A-M, N-Z) | Supports range queries, ordered access | Hotspot risk if data distribution is uneven |
| Hash-based | Partition by hash(key) mod N | Even distribution across shards | No range queries, resharding is complex |
| Directory-based | Lookup table maps keys to shards | Flexible, supports heterogeneous shards | Lookup table is a single point of failure |

### Sharding Trade-Offs

- Cross-shard queries require scatter-gather, increasing latency.
- Distributed transactions across shards require two-phase commit or saga patterns.
- Resharding (adding/removing shards) shall use consistent hashing to minimize data movement.

## CDN Patterns

### Static Asset Distribution

The system shall serve static assets (images, CSS, JavaScript, fonts) through a CDN to reduce origin server load and improve client-side latency.

### Dynamic Content Acceleration

For APIs with cacheable responses, the CDN shall cache responses at edge locations with:

- Cache key: URL + query parameters + relevant headers (e.g., Accept-Language).
- TTL: Short (30-60 seconds) for semi-dynamic content.
- Cache bypass: `Cache-Control: no-cache` for authenticated or personalized responses.

## Connection Pooling

### Application-Level Pooling

The system shall maintain a connection pool for each downstream dependency:

| Parameter | Recommended Range | Purpose |
|-----------|------------------|---------|
| Min pool size | 5-10 | Avoid cold-start latency |
| Max pool size | 20-50 | Prevent connection exhaustion |
| Idle timeout | 30-300 seconds | Reclaim unused connections |
| Max wait time | 5-10 seconds | Fail fast when pool is exhausted |
| Validation query | `SELECT 1` | Verify connection health before use |

### Database Proxy Pooling

For high-connection-count scenarios, the system shall use a connection proxy (PgBouncer, ProxySQL) to multiplex application connections over a smaller set of database connections.

# Scalability Patterns Reference

**Source:** System Design - The Big Archive (ByteByteGo 2024)
**Standard:** ISO/IEC 25010 (Performance Efficiency, Reliability)

---

## Horizontal Scaling

Horizontal scaling adds more instances of a service to handle increased load. Apply horizontal scaling when the service meets these prerequisites:

### Stateless Services

Design every application-tier service to hold zero in-process session state. Store all mutable state in external stores (database, cache, object storage). A load balancer shall route any request to any instance without affinity.

### Shared-Nothing Architecture

Each node operates independently and shares no memory or disk with other nodes. The system eliminates single points of contention at the application layer. Coordination happens through message queues or distributed consensus only when strictly necessary.

### Session Externalization

Move session data out of application memory into a shared store:

| Store Type | Use Case | Trade-off |
|-----------|----------|-----------|
| Redis | Low-latency session lookup, TTL-based expiry | Requires Redis HA (Sentinel or Cluster) |
| Database | Durable sessions, audit trail | Higher latency per read |
| Signed tokens (JWT) | Stateless verification, no server-side lookup | Cannot revoke mid-flight without a blocklist |

## Vertical Scaling

Vertical scaling increases the resources (CPU, RAM, disk I/O) of a single node.

### When Appropriate

- **Database master nodes:** Write-heavy workloads that cannot easily shard (e.g., ACID transactions spanning multiple tables).
- **Single-writer services:** Systems that require strict ordering guarantees (e.g., sequential ID generation, ledger writes).
- **Legacy monoliths:** When horizontal refactoring cost exceeds the vertical scaling budget.

### Limits

Vertical scaling hits a ceiling defined by the largest available instance type. Plan a migration path to horizontal scaling when utilization consistently exceeds 70% of the maximum instance size.

## Auto-Scaling Policies

Auto-scaling adjusts instance count dynamically based on demand signals.

### Target-Tracking Scaling

Set a target metric value and let the auto-scaler converge toward it:

| Metric | Target | Use Case |
|--------|--------|----------|
| CPU utilization | 60-70% | General compute-bound services |
| Memory utilization | 70-80% | In-memory processing, caching layers |
| Request count per target | Varies | API gateways, load-balanced services |

### Step Scaling

Define discrete scaling steps triggered by threshold breaches:

- Scale out +2 instances when CPU > 80% for 3 minutes.
- Scale out +4 instances when CPU > 90% for 1 minute.
- Scale in -1 instance when CPU < 40% for 10 minutes.

Step scaling provides finer control than target-tracking for bursty workloads.

### Scheduled Scaling

Pre-provision capacity for predictable traffic patterns:

- Business hours (08:00-18:00): minimum 6 instances.
- Off-hours: minimum 2 instances.
- Known events (product launches, month-end processing): temporary minimum increase.

### Predictive Scaling

Use historical traffic data (minimum 14 days) to forecast future demand. The auto-scaler provisions instances before the predicted spike arrives. Combine predictive scaling with target-tracking as a safety net.

## Database Scaling

### Read Replicas

Distribute read traffic across replica nodes to reduce load on the primary.

| Replication Mode | Consistency | Latency | Use Case |
|-----------------|-------------|---------|----------|
| Asynchronous | Eventual (milliseconds to seconds lag) | Low write latency | Analytics dashboards, reporting |
| Synchronous | Strong (zero lag) | Higher write latency | Financial reads, inventory checks |

Route read-after-write queries to the primary to avoid stale reads. Use middleware or proxy (e.g., ProxySQL, PgBouncer) to manage routing.

### Write Scaling via Sharding

Partition data across multiple database nodes to distribute write load.

| Strategy | Mechanism | Advantage | Disadvantage |
|----------|-----------|-----------|--------------|
| Range-based | Partition by value range (e.g., dates, IDs 1-1M) | Simple, range queries stay local | Hot spots if ranges are uneven |
| Hash-based | Hash the shard key, mod by shard count | Even distribution | Range queries span all shards |
| Directory-based | Lookup table maps keys to shards | Flexible rebalancing | Lookup table becomes a bottleneck |
| Geographic | Partition by region (US, EU, APAC) | Data locality, compliance | Cross-region queries are expensive |

**Trade-offs common to all sharding strategies:**
- Cross-shard joins require application-level coordination or denormalization.
- Transactions spanning shards need distributed transaction protocols (2PC, Saga).
- Schema changes must propagate to every shard.
- Rebalancing shards requires careful data migration planning.

## CDN Patterns

### Static Asset Caching

Serve images, CSS, JavaScript, and fonts from edge locations. Set long Cache-Control max-age headers (e.g., 1 year) and use content-hash filenames for cache busting.

### Dynamic Content Acceleration

Cache personalized or semi-dynamic responses at the edge with short TTLs (5-60 seconds). Use Vary headers to partition cache by user segment, locale, or device type.

### Edge Computing

Execute lightweight logic at CDN edge nodes (e.g., A/B test routing, geolocation redirects, request validation). Reduce round-trip latency for latency-sensitive operations.

## Connection Pooling

### Database Connection Pools

Maintain a pool of reusable database connections to avoid the overhead of establishing new connections per request.

| Parameter | Guideline |
|-----------|-----------|
| Minimum pool size | Number of CPU cores on the application server |
| Maximum pool size | 2x CPU cores (start here, tune based on wait metrics) |
| Connection timeout | 3-5 seconds (fail fast if pool exhausted) |
| Idle timeout | 5-10 minutes (reclaim unused connections) |
| Validation query | Lightweight health check before reuse (e.g., `SELECT 1`) |

### HTTP Connection Pools

Reuse HTTP connections to upstream services via keep-alive. Configure per-host pool limits to prevent a single slow upstream from exhausting all connections.

### gRPC Connection Management

gRPC multiplexes streams over a single HTTP/2 connection. Use client-side load balancing (round-robin or weighted) when connecting to multiple backend instances. Monitor stream concurrency limits and open additional connections when the limit approaches saturation.

---

**Cross-references:**
- `references/distributed-systems.md` -- CAP theorem, consistency models, event-driven patterns
- `references/caching-strategies.md` -- Cache patterns, invalidation, multi-layer caching
- `SKILL.md` Step 5 (Deployment Topology) -- Apply these patterns when designing deployment diagrams

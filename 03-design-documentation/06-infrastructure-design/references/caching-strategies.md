# Caching Strategies Reference

## Purpose

This reference provides caching patterns, invalidation strategies, and multi-layer caching architecture guidance for infrastructure design. It covers cache-aside, read-through, write-through, write-behind, invalidation mechanisms, and protection against common caching failure modes.

## Reference Standard

- ISO/IEC 25010 Section 4.2.1: Performance efficiency -- time behaviour, resource utilization
- "System Design - The Big Archive" (ByteByteGo 2024) Ch. 4: Caching at scale

## Caching Patterns

### Cache-Aside (Lazy Loading)

The application shall manage the cache explicitly:

1. Read: Check cache first. On cache miss, read from database, write result to cache, return to caller.
2. Write: Write to database. Invalidate or delete the cache entry.

| Property | Value |
|----------|-------|
| Consistency | Eventual (stale reads possible until TTL or invalidation) |
| Complexity | Application manages cache logic |
| Best for | Read-heavy workloads with tolerance for brief staleness |
| Risk | Cache miss storm on cold start or mass expiration |

### Read-Through

The cache layer shall transparently load data from the backing store on a miss:

1. Application reads from cache only.
2. On miss, the cache itself fetches from the database, stores the result, and returns it.

| Property | Value |
|----------|-------|
| Consistency | Eventual |
| Complexity | Cache provider manages loading logic |
| Best for | Simplifying application code; uniform cache access patterns |
| Risk | First request latency on cache miss |

### Write-Through

The system shall write to the cache and the backing store synchronously:

1. Application writes to cache.
2. Cache writes to database before confirming the write.

| Property | Value |
|----------|-------|
| Consistency | Strong (cache and database are always in sync) |
| Latency | Higher write latency (two synchronous writes) |
| Best for | Data that is read frequently after writing |
| Risk | Write latency increase; cache churn for write-heavy, read-light data |

### Write-Behind (Write-Back)

The system shall write to the cache immediately and asynchronously flush to the backing store:

1. Application writes to cache.
2. Cache acknowledges the write immediately.
3. Cache flushes to database asynchronously (batched, on interval, or on eviction).

| Property | Value |
|----------|-------|
| Consistency | Eventual (risk of data loss if cache fails before flush) |
| Write latency | Low (only cache write is synchronous) |
| Best for | Write-heavy workloads where brief inconsistency is acceptable |
| Risk | Data loss on cache node failure; requires durable cache or replication |

## Cache Invalidation Strategies

### TTL-Based Invalidation

Each cache entry shall have a time-to-live after which it is automatically evicted:

| Data Type | Recommended TTL | Rationale |
|-----------|----------------|-----------|
| Static configuration | 1-24 hours | Rarely changes |
| User session data | 15-60 minutes | Balance between freshness and load |
| API response cache | 30 seconds - 5 minutes | Depends on data volatility |
| Search results | 1-10 minutes | Acceptable staleness for discovery |
| Real-time data | 1-10 seconds | Near-real-time freshness required |

### Event-Driven Invalidation

The system shall invalidate cache entries in response to data change events:

1. A write operation publishes an invalidation event (via message queue or pub/sub).
2. Cache subscribers receive the event and delete or refresh the affected keys.
3. Subsequent reads trigger a cache miss and reload fresh data.

Advantages over TTL-only: Lower staleness window, no unnecessary eviction of unchanged data.

### Versioned Keys

The system shall embed a version identifier in cache keys:

- Key format: `entity:{id}:v{version}` (e.g., `product:42:v7`).
- On write, increment the version number. New reads use the new key, creating a cache miss.
- Old versioned entries expire naturally via TTL.
- Advantage: No explicit invalidation needed; eliminates race conditions between invalidation and read.

## Multi-Layer Caching Architecture

### Layer Hierarchy

```
Client (Browser Cache)
  |
  v
CDN (Edge Cache)
  |
  v
Reverse Proxy (Varnish / Nginx)
  |
  v
Application Cache (Redis / Memcached)
  |
  v
Database Cache (Query Cache / Materialized Views)
  |
  v
Database (Source of Truth)
```

### Layer Configuration

| Layer | Scope | TTL Range | Invalidation | Technology |
|-------|-------|-----------|-------------|-----------|
| Browser | Per-user | Minutes to days | `Cache-Control`, `ETag`, `Last-Modified` | HTTP headers |
| CDN | Per-region | Minutes to hours | Purge API, surrogate keys | CloudFront, Cloudflare, Fastly |
| Reverse Proxy | Per-server | Seconds to minutes | Ban/purge, hash-based | Varnish, Nginx proxy_cache |
| Application | Per-cluster | Seconds to minutes | Event-driven, TTL | Redis, Memcached |
| Database | Per-instance | Varies | Refresh on write, schedule | Query cache, materialized views |

### Cache-Control Header Strategy

| Resource Type | Cache-Control Value | Rationale |
|--------------|-------------------|-----------|
| Versioned static assets | `public, max-age=31536000, immutable` | Content-hash in filename ensures new versions get new URLs |
| HTML pages | `no-cache` or `max-age=0, must-revalidate` | Always validate freshness with server |
| API responses (public) | `public, max-age=60, s-maxage=300` | Short client cache, longer CDN cache |
| API responses (private) | `private, max-age=0, no-store` | User-specific data shall not be cached by shared caches |

## Cache Warming

### Purpose

Cache warming shall pre-populate the cache before traffic arrives to prevent cold-start performance degradation.

### Strategies

| Strategy | Mechanism | Use Case |
|----------|-----------|----------|
| Startup warming | Application loads frequently accessed data on boot | Predictable hot data set |
| Scheduled warming | Cron job refreshes cache before peak hours | Time-based traffic patterns |
| Lazy warming with prefetch | On cache miss, prefetch related entries | Access patterns with locality |

## Thundering Herd Prevention

### Problem

When a popular cache entry expires, many concurrent requests simultaneously query the backing store, causing a load spike.

### Solutions

| Solution | Mechanism | Trade-off |
|----------|-----------|-----------|
| **Mutex/lock** | First request acquires a lock and refreshes the cache; others wait or receive stale data | Adds latency for waiting requests |
| **Probabilistic early expiration** | Each request has a small probability of refreshing the cache before TTL expires: $P(refresh) = e^{-\lambda \times (TTL - elapsed)}$ | May cause occasional unnecessary refreshes |
| **Stale-while-revalidate** | Serve stale data immediately while refreshing asynchronously in the background | Clients may see briefly stale data |
| **Request coalescing** | Cache proxy groups identical concurrent requests and serves a single backend response to all | Requires proxy support (e.g., Nginx proxy_cache_lock) |

## Cache Stampede Protection

### Problem

A cache stampede occurs when a large batch of cache entries expire simultaneously (e.g., after a cache flush or restart), overwhelming the backing store.

### Solutions

- **Jittered TTLs**: Add random variation to TTL values: $TTL_{effective} = TTL_{base} + Random(0, Jitter)$. This spreads expiration across time.
- **Gradual cache warming**: After a flush, warm the cache incrementally rather than allowing all requests to hit the database.
- **Rate-limited refresh**: Limit the rate of cache-miss-triggered database queries using a semaphore or token bucket.

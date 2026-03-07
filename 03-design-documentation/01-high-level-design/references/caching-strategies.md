# Caching Strategies Reference

**Source:** System Design - The Big Archive (ByteByteGo 2024)
**Standards:** ISO/IEC 25010 (Performance Efficiency), IEEE 1016-2009 (Architectural Design)

---

## Cache Patterns

Select the cache pattern based on read/write ratio, consistency requirements, and data volatility.

### Cache-Aside (Lazy Loading)

The application checks the cache first. On a cache miss, the application reads from the database, writes the result to the cache, and returns it to the caller.

- **Read path:** Cache hit returns immediately. Cache miss triggers DB read + cache write.
- **Write path:** Application writes to the database. Cache entry is either invalidated or left to expire via TTL.
- **Advantage:** Only requested data is cached (no wasted memory). Cache failure does not block reads (falls through to DB).
- **Disadvantage:** First request for each key always hits the database (cold start penalty). Data can become stale between DB write and cache expiry.

### Read-Through

The cache itself is responsible for loading data from the database on a miss. The application always reads from the cache.

- **Advantage:** Application code is simpler (no cache-miss logic). Consistent read path.
- **Disadvantage:** Cache library or proxy must support data-source integration. Initial latency on cache miss includes DB round-trip.

### Write-Through

Every write goes to the cache first, and the cache synchronously writes to the database before acknowledging the client.

- **Advantage:** Cache and database are always consistent. Reads after writes always return fresh data.
- **Disadvantage:** Write latency increases (two writes per operation). Unused data may populate the cache unnecessarily.

### Write-Behind (Write-Back)

The application writes to the cache, which acknowledges immediately. The cache asynchronously flushes writes to the database in batches.

- **Advantage:** Low write latency. Batch writes reduce database load. Effective for write-heavy workloads.
- **Disadvantage:** Risk of data loss if the cache node fails before flushing. Increased complexity for failure recovery.

### Refresh-Ahead

The cache proactively refreshes entries that are about to expire, based on predicted access patterns.

- **Advantage:** Eliminates cache-miss latency for frequently accessed keys. Smooth read performance.
- **Disadvantage:** Requires accurate prediction of access patterns. Wastes resources refreshing keys that are not accessed.

## Cache Invalidation

| Strategy | Mechanism | Consistency | Complexity |
|----------|-----------|-------------|------------|
| **TTL-based** | Each cache entry expires after a fixed duration | Eventual (bounded staleness) | Low |
| **Event-driven (pub/sub)** | Database change events trigger cache invalidation messages | Near-real-time | Moderate |
| **Versioned keys** | Append a version number to cache keys; increment version on write | Strong (new version = cache miss) | Low-moderate |
| **Manual purge** | Application explicitly deletes cache entries on write | Immediate | Low (but error-prone if missed) |

**Recommendation:** Combine TTL-based expiry as a safety net with event-driven invalidation for freshness-critical data. TTL catches any missed invalidation events.

## Multi-Layer Caching

Data flows through multiple cache layers, each reducing latency and load on downstream layers:

```
Browser Cache (client) --> CDN (edge) --> Reverse Proxy (origin shield) --> Application Cache --> DB Query Cache
```

| Layer | Technology | TTL Range | Controls |
|-------|-----------|-----------|----------|
| **Browser cache** | HTTP Cache-Control, ETag, Last-Modified | Seconds to years | `Cache-Control: max-age=31536000, immutable` for hashed assets; `no-cache` for HTML |
| **CDN (edge cache)** | CloudFront, Cloudflare, Fastly | 5 seconds to 24 hours | Vary header for segmented caching; purge API for instant invalidation |
| **Reverse proxy** | Varnish, Nginx proxy_cache | 1-60 seconds | `stale-while-revalidate` for non-blocking background refresh |
| **Application cache** | Redis, Memcached | 30 seconds to 24 hours | Application-managed TTL; event-driven invalidation for mutable data |
| **DB query cache** | MySQL query cache (deprecated), PostgreSQL prepared statements, materialized views | Varies | Use materialized views for expensive aggregations; refresh on schedule or trigger |

## Cache Problems and Solutions

### Thundering Herd

**Problem:** A popular cache key expires and hundreds of concurrent requests simultaneously hit the database to rebuild it.

**Solutions:**
- **Lock + stale-while-revalidate:** The first request acquires a lock and rebuilds the cache. Other requests receive the stale cached value while the rebuild runs.
- **Distributed lock (Redis SETNX):** Only one instance rebuilds; others wait or serve stale data.
- **Request coalescing:** The cache proxy collapses duplicate in-flight requests into a single backend fetch.

### Cache Stampede

**Problem:** Many keys expire at the same time (e.g., after a cache restart or batch TTL alignment), flooding the database.

**Solutions:**
- **Probabilistic early expiry (PER):** Each key independently decides to refresh before TTL expires, spreading rebuilds over time. Formula: `shouldRefresh = (currentTime - fetchTime) > TTL * (1 - random(0, beta))`.
- **Jittered TTL:** Add a random offset (e.g., +/- 10%) to each key's TTL to prevent synchronized expiry.
- **Cache warming on deploy:** Pre-populate hot keys during application startup.

### Hot Key

**Problem:** A single cache key receives disproportionate traffic (e.g., a viral product page), overloading the shard that owns it.

**Solutions:**
- **Replicate across shards:** Store copies of the hot key on multiple cache nodes. Route reads randomly across replicas.
- **Local in-process cache:** Cache the hot key in application memory (L1 cache) with a short TTL (1-5 seconds) to absorb the majority of reads.
- **Rate limiting per key:** Cap the number of cache reads per second for any single key, shedding excess to a queue.

### Cold Start

**Problem:** After a deployment, cache restart, or new region launch, the cache is empty and all requests hit the database.

**Solutions:**
- **Cache warming:** Run a startup job that pre-loads the top N most-accessed keys from the database.
- **Gradual traffic shift:** Route a small percentage of traffic to the new instance, increasing as the cache fills.
- **Snapshot restore:** Restore a recent RDB/AOF snapshot (Redis) to start with a partially warm cache.

## Technology Selection

| Feature | Redis | Memcached |
|---------|-------|-----------|
| **Data structures** | Strings, hashes, lists, sets, sorted sets, streams, bitmaps, HyperLogLog | Strings only (key-value) |
| **Persistence** | RDB snapshots + AOF append-only file | None (volatile) |
| **Pub/Sub** | Built-in publish/subscribe channels | Not supported |
| **Scripting** | Lua scripting for atomic multi-step operations | Not supported |
| **Threading** | Single-threaded command execution (I/O threads in Redis 6+) | Multi-threaded (scales to multiple CPU cores) |
| **Clustering** | Redis Cluster (automatic sharding, failover) | Client-side sharding (consistent hashing) |
| **Memory efficiency** | Higher overhead per key (data structure metadata) | Lower overhead per key |
| **Max value size** | 512 MB | 1 MB (default, configurable) |

**Selection guideline:**
- Choose **Redis** when you need data structures beyond simple key-value, persistence, pub/sub for cache invalidation, or Lua scripting for atomic operations.
- Choose **Memcached** when you need a simple, high-throughput volatile cache that scales linearly with CPU cores, and you do not need persistence or advanced data types.

---

**Cross-references:**
- `references/scalability-patterns.md` -- CDN patterns, connection pooling
- `references/distributed-systems.md` -- Eventual consistency implications for caching
- `SKILL.md` Step 9 (Cross-Cutting Concerns, Section 8.4 Caching) -- Apply these patterns when documenting cache architecture

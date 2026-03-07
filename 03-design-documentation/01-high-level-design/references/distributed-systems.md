# Distributed Systems Reference

**Source:** System Design - The Big Archive (ByteByteGo 2024)
**Standards:** ISO/IEC 25010 (Reliability), IEEE 1016-2009 (Architectural Design)

---

## CAP Theorem

The CAP theorem (Brewer, 2000) states that a distributed data store can provide at most two of three guarantees simultaneously:

| Property | Definition |
|----------|-----------|
| **Consistency** | Every read receives the most recent write or an error |
| **Availability** | Every request receives a non-error response (without guarantee of the most recent write) |
| **Partition Tolerance** | The system continues operating despite network partitions between nodes |

### Practical Implications

Network partitions are inevitable in distributed systems. The real choice is between CP and AP behavior during a partition:

| Choice | Behavior During Partition | Example Domains |
|--------|--------------------------|-----------------|
| **CP** | Reject requests that cannot guarantee consistency; return errors until partition heals | Banking, inventory management, financial ledgers, booking systems |
| **AP** | Accept requests and serve potentially stale data; reconcile after partition heals | Social media feeds, product catalogs, DNS, content delivery |
| **CA** | Possible only when no network partition exists (single-node or same-rack deployment) | Single-node relational databases, in-memory caches on one host |

**Design decision:** Document which CAP trade-off each service makes and the business justification in the HLD Technology Decisions table.

## Consistency Models

Select the consistency model based on the business requirement for data freshness:

| Model | Guarantee | Latency Impact | Use Case |
|-------|-----------|----------------|----------|
| **Strong consistency** | Reads always return the latest write | Highest (requires coordination) | Financial transactions, seat reservations |
| **Eventual consistency** | Reads converge to the latest write over time | Lowest | Social media likes, view counters |
| **Causal consistency** | Reads respect causal ordering (if A caused B, B is never seen without A) | Moderate | Chat messages, comment threads |
| **Read-your-writes** | A client always sees its own writes immediately | Low-moderate | User profile updates, form submissions |
| **Monotonic reads** | A client never sees older data after seeing newer data | Low-moderate | Dashboard refreshes, paginated lists |

## Event-Driven Architecture

### Event Sourcing

Store every state change as an immutable event in an append-only log rather than overwriting current state.

**Core concepts:**
- **Append-only event log:** The event store is the single source of truth. Each event records what happened (e.g., `OrderPlaced`, `ItemAdded`, `PaymentReceived`).
- **Event replay:** Reconstruct current state by replaying all events from the beginning. Use this for debugging, auditing, and rebuilding read models.
- **Snapshots:** Periodically persist a snapshot of the current state to avoid replaying the entire event history. Replay only events after the snapshot.

**When to use:** Audit-heavy domains (finance, healthcare, legal), systems requiring full history reconstruction, domains with complex business rules that evolve over time.

### CQRS (Command Query Responsibility Segregation)

Separate the write model (commands) from the read model (queries).

- **Write model:** Handles commands (create, update, delete) and enforces business rules. Optimized for consistency and validation.
- **Read model (projection):** Denormalized views optimized for query performance. Updated asynchronously from the write model via events.
- **Eventual consistency:** The read model lags behind the write model by the event processing delay (typically milliseconds to seconds).

**When to use:** Systems where read and write patterns differ significantly (e.g., high read-to-write ratio), complex domain models, systems requiring multiple specialized read views.

### Saga Pattern

Manage distributed transactions across multiple services without a global two-phase commit.

| Approach | Coordination | Advantages | Disadvantages |
|----------|-------------|------------|---------------|
| **Choreography** | Each service listens for events and reacts independently | Loose coupling, simple for 2-3 services | Hard to trace, complex failure paths at scale |
| **Orchestration** | A central orchestrator directs the saga steps | Clear flow, easier monitoring and debugging | Orchestrator becomes a coordination point |

**Compensating transactions:** Each saga step defines a compensating action that undoes its effect if a downstream step fails. Design compensating transactions to be idempotent.

**Example flow (order placement):**
1. Reserve inventory (compensate: release inventory)
2. Charge payment (compensate: refund payment)
3. Create shipment (compensate: cancel shipment)
4. Confirm order

If step 3 fails, execute compensating transactions for steps 2 and 1 in reverse order.

## Message Queue Patterns

| Pattern | Description | Use Case |
|---------|-------------|----------|
| **Point-to-point** | One producer sends a message to exactly one consumer | Task assignment, work queues |
| **Publish-subscribe** | One producer broadcasts a message to all subscribed consumers | Event notification, cache invalidation |
| **Fan-out** | One message triggers processing by multiple independent consumers in parallel | Order placed triggers inventory, notification, and analytics services |
| **Competing consumers** | Multiple consumer instances read from the same queue; each message is processed by exactly one consumer | Horizontal scaling of message processing |
| **Dead letter queue (DLQ)** | Messages that fail processing after N retries move to a separate queue for inspection | Poison message isolation, error investigation |

### Queue Design Guidelines

- Set message TTL to prevent unbounded queue growth.
- Configure retry policies with exponential backoff (base 2s, max 5 retries).
- Monitor queue depth as a scaling signal for consumer instances.
- Use message deduplication (content-based or message-ID-based) to handle redelivery.

## Idempotency

Ensure that processing the same operation multiple times produces the same result as processing it once.

### Idempotency Keys

The client generates a unique key (UUID) per operation and includes it in the request header. The server stores the key and its result. On duplicate requests, the server returns the stored result without re-executing the operation.

| Header | Value | Purpose |
|--------|-------|---------|
| `Idempotency-Key` | UUID v4 | Uniquely identifies the client intent |

### Delivery Guarantees

| Guarantee | Description | Implementation Cost | Use Case |
|-----------|-------------|-------------------|----------|
| **At-most-once** | Message delivered zero or one times; no retry on failure | Lowest | Metrics, logs (acceptable loss) |
| **At-least-once** | Message delivered one or more times; consumer must handle duplicates | Moderate | Most business operations (with idempotency) |
| **Exactly-once** | Message delivered and processed exactly one time | Highest (requires transactional outbox + idempotent consumer) | Financial transactions, inventory adjustments |

**Practical recommendation:** Design for at-least-once delivery with idempotent consumers. Exactly-once semantics require significant infrastructure complexity and are justified only for high-value transactions.

---

**Cross-references:**
- `references/scalability-patterns.md` -- Horizontal scaling, database sharding
- `references/caching-strategies.md` -- Eventual consistency implications for caching
- `SKILL.md` Step 2 (Architectural Style) -- Use CAP analysis when selecting event-driven architecture
- `SKILL.md` Step 8 (Integration Points) -- Apply message queue patterns for async integrations

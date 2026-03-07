# Distributed Systems Reference

## Purpose

This reference provides distributed systems theory and practical patterns for infrastructure design. It covers the CAP theorem, consistency models, consensus algorithms, event-driven architecture, message queue patterns, and idempotency.

## Reference Standard

- ISO/IEC 25010 Section 4.2.4: Reliability -- availability, fault tolerance
- "System Design - The Big Archive" (ByteByteGo 2024) Ch. 5-7: Distributed system fundamentals

## CAP Theorem

### Definition

The CAP theorem states that a distributed data store shall provide at most two of the following three guarantees simultaneously:

| Property | Definition |
|----------|------------|
| **Consistency** | Every read receives the most recent write or an error |
| **Availability** | Every request receives a non-error response (without guarantee of most recent write) |
| **Partition Tolerance** | The system continues to operate despite network partitions between nodes |

### Practical Implications

Since network partitions are unavoidable in distributed systems, the real choice is between CP and AP:

| Choice | Behavior During Partition | Use Cases |
|--------|--------------------------|-----------|
| CP (Consistency + Partition Tolerance) | The system shall reject writes or return errors to maintain consistency | Financial transactions, inventory management, leader election |
| AP (Availability + Partition Tolerance) | The system shall accept writes and reconcile conflicts after partition heals | Social media feeds, shopping carts, DNS, caching |

### PACELC Extension

Beyond CAP, the PACELC model states: when there is a **P**artition, choose **A**vailability or **C**onsistency; **E**lse (normal operation), choose **L**atency or **C**onsistency.

| System Type | During Partition | Normal Operation |
|-------------|-----------------|-----------------|
| PA/EL | Availability | Low latency (e.g., Cassandra, DynamoDB) |
| PC/EC | Consistency | Consistency (e.g., traditional RDBMS with sync replication) |
| PA/EC | Availability | Consistency (e.g., MongoDB default) |

## Consistency Models

### Strong Consistency

All nodes see the same data at the same time. The system shall enforce linearizability:

- Every read returns the value of the most recent completed write.
- Implementation: Synchronous replication, consensus protocols.
- Trade-off: Higher latency, lower throughput.

### Eventual Consistency

If no new updates are made, all replicas shall eventually converge to the same value:

- Convergence window: The system shall define the maximum time for replicas to synchronize (e.g., < 5 seconds).
- Conflict resolution: Last-write-wins (LWW), vector clocks, or application-level merge.
- Use cases: Read-heavy workloads, non-critical data, caching layers.

### Causal Consistency

Operations that are causally related shall be seen in the same order by all nodes. Concurrent operations may be seen in different orders:

- Implementation: Logical clocks, version vectors.
- Stronger than eventual consistency, weaker than strong consistency.
- Use cases: Collaborative editing, social media comment threads.

## Consensus Algorithms (Conceptual)

### Raft

Raft achieves consensus through leader election and log replication:

1. **Leader Election**: Nodes start as followers. If a follower receives no heartbeat within a timeout, it becomes a candidate and requests votes.
2. **Log Replication**: The leader accepts client requests, appends them to its log, and replicates to followers. A log entry is committed when a majority of nodes acknowledge it.
3. **Safety**: Raft guarantees that committed entries are durable and all nodes shall eventually apply the same entries in the same order.

### Paxos

Paxos is a family of protocols for achieving consensus among unreliable nodes:

1. **Prepare Phase**: A proposer selects a proposal number and sends a prepare request to acceptors.
2. **Accept Phase**: If a majority of acceptors respond, the proposer sends an accept request with the highest-numbered proposal value.
3. **Learn Phase**: Once a majority accepts, the value is chosen and learners are notified.

### Practical Usage

Most systems use managed consensus implementations (etcd with Raft, ZooKeeper with ZAB) rather than implementing consensus directly. The infrastructure design shall specify which consensus system is used and its role (leader election, configuration management, distributed locking).

## Event-Driven Architecture

### Event Sourcing

The system shall store state changes as an immutable sequence of events rather than overwriting current state:

| Aspect | Description |
|--------|-------------|
| Event store | Append-only log of domain events |
| Current state | Derived by replaying events from the beginning or a snapshot |
| Snapshots | Periodic materialized state to avoid full replay |
| Benefits | Complete audit trail, temporal queries, event replay |
| Trade-offs | Increased storage, eventual consistency for read models, schema evolution complexity |

### CQRS (Command Query Responsibility Segregation)

The system shall separate the write model (commands) from the read model (queries):

- **Command side**: Validates and processes write operations, emits events.
- **Query side**: Maintains denormalized read-optimized projections updated by event handlers.
- **Synchronization**: Events propagate from command side to query side (eventual consistency).
- **When to use**: Systems with asymmetric read/write patterns or complex domain logic.

### Saga Pattern

The system shall coordinate distributed transactions across services using sagas:

| Saga Type | Mechanism | Trade-offs |
|-----------|-----------|-----------|
| Choreography | Each service listens for events and triggers the next step | Decoupled, but hard to track overall progress |
| Orchestration | A central coordinator directs each step | Easier to monitor, but introduces a single coordinator |

Each saga step shall define a compensating action for rollback if a downstream step fails.

## Message Queue Patterns

### Pub/Sub (Publish-Subscribe)

Publishers emit events to a topic. Multiple subscribers receive a copy of each event independently:

- Use case: Event broadcasting, notification fanout, analytics pipelines.
- Ordering: Per-partition ordering (Kafka) or best-effort (SNS).

### Point-to-Point

Each message is consumed by exactly one consumer from a queue:

- Use case: Task distribution, work queues, job processing.
- The system shall use competing consumers for parallel processing.

### Fan-Out

A single message triggers processing in multiple downstream consumers, each performing a different action:

- Implementation: SNS + SQS fan-out, Kafka consumer groups on different topics.
- Use case: Order placed triggers inventory update, payment processing, notification, and analytics simultaneously.

### Message Delivery Guarantees

| Guarantee | Description | Implementation Cost |
|-----------|-------------|-------------------|
| At-most-once | Messages may be lost but are never duplicated | Low -- fire and forget |
| At-least-once | Messages are never lost but may be duplicated | Medium -- acknowledgment and retry |
| Exactly-once | Messages are delivered exactly once | High -- idempotency + transactional processing |

## Idempotency Patterns

### Idempotency Key Strategy

The system shall use client-generated idempotency keys to ensure safe retries:

1. The client generates a unique key (UUID v4) per logical operation.
2. The server stores the key with the operation result (TTL: 24-48 hours).
3. On duplicate key, the server returns the cached result without re-executing.

### Database-Level Idempotency

- **Upsert operations**: `INSERT ... ON CONFLICT DO UPDATE` ensures repeated inserts produce the same result.
- **Conditional updates**: `UPDATE ... WHERE version = N` ensures only one concurrent update succeeds.

### Event Processing Idempotency

The system shall track processed event IDs in a deduplication store to prevent duplicate event handling:

| Component | Storage | TTL | Lookup |
|-----------|---------|-----|--------|
| Deduplication store | Redis SET or database table | 24-72 hours | O(1) by event ID |

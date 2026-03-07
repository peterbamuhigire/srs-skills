# Monitoring and Observability Reference

## Purpose

This reference provides monitoring methodologies, structured logging standards, distributed tracing patterns, and alerting best practices for infrastructure design. It covers the RED method, USE method, four golden signals, correlation ID propagation, and alert severity frameworks.

## Reference Standard

- ISO/IEC 25010 Section 4.2.4: Reliability -- maturity (monitoring for defect detection)
- "System Design - The Big Archive" (ByteByteGo 2024) Ch. 11: Observability at scale

## RED Method (For Services)

The RED method shall be applied to every service-level component:

| Metric | Definition | Measurement | Alert Threshold Example |
|--------|-----------|-------------|------------------------|
| **Rate** | Number of requests per second the service is handling | Counter incremented per request | Deviation > 2 standard deviations from baseline |
| **Errors** | Number of failed requests per second | Counter incremented per error response (5xx, timeout, exception) | Error rate > 1% of total requests |
| **Duration** | Distribution of response times | Histogram with percentile buckets (p50, p95, p99) | p99 latency > 2x SLA target |

### When to Use RED

The RED method shall be the primary monitoring framework for request-driven services (APIs, web servers, microservices). It answers: "Is the service performing well from the caller's perspective?"

## USE Method (For Resources)

The USE method shall be applied to every infrastructure resource (CPU, memory, disk, network):

| Metric | Definition | Measurement | Alert Threshold Example |
|--------|-----------|-------------|------------------------|
| **Utilization** | Percentage of resource capacity in use | Gauge (0-100%) | CPU > 80% sustained for 5 minutes |
| **Saturation** | Degree to which the resource has extra work queued | Queue length, wait time | Disk IO queue > 10 for 2 minutes |
| **Errors** | Count of error events for the resource | Counter per error type | Disk errors > 0, network packet loss > 0.1% |

### When to Use USE

The USE method shall be the primary monitoring framework for infrastructure resources. It answers: "Is a resource the bottleneck?"

## Four Golden Signals

Google SRE defines four golden signals that the system shall monitor for every user-facing service:

| Signal | Definition | Relationship to RED/USE |
|--------|-----------|------------------------|
| **Latency** | Time to service a request (distinguish successful vs. failed request latency) | RED: Duration |
| **Traffic** | Demand on the system (requests/second, transactions/second) | RED: Rate |
| **Errors** | Rate of failed requests (explicit 5xx, implicit policy violations) | RED: Errors |
| **Saturation** | How "full" the service is; utilization of constrained resources | USE: Saturation + Utilization |

## Structured Logging Standards

### Log Format

The system shall use structured JSON logging with the following mandatory fields:

```json
{
  "timestamp": "2026-03-08T14:30:00.123Z",
  "level": "INFO",
  "service": "order-service",
  "instance": "order-service-pod-abc123",
  "correlation_id": "req-550e8400-e29b-41d4-a716-446655440000",
  "trace_id": "abc123def456",
  "span_id": "789ghi012",
  "method": "POST",
  "path": "/api/v1/orders",
  "status_code": 201,
  "duration_ms": 142,
  "user_id": "usr_12345",
  "message": "Order created successfully",
  "context": {
    "order_id": "ord_67890",
    "item_count": 3
  }
}
```

### Log Levels

| Level | Usage | Production Default |
|-------|-------|--------------------|
| TRACE | Granular diagnostic data (variable values, loop iterations) | Disabled |
| DEBUG | Detailed flow information for development | Disabled |
| INFO | Normal operational events (request served, job completed) | Enabled |
| WARN | Unexpected but recoverable conditions (retry triggered, cache miss rate high) | Enabled |
| ERROR | Failed operations requiring attention (unhandled exception, dependency failure) | Enabled |
| FATAL | Unrecoverable conditions requiring immediate intervention (data corruption, out of memory) | Enabled |

### Log Retention Policy

| Environment | Retention | Storage |
|-------------|-----------|---------|
| Production | 30-90 days hot, 1 year cold | Elasticsearch/OpenSearch (hot), S3/GCS (cold) |
| Staging | 14 days | Elasticsearch/OpenSearch |
| Development | 7 days | Local or short-lived storage |

## Distributed Tracing

### Trace Context Propagation

The system shall propagate trace context across service boundaries using one of:

| Standard | Header | Format |
|----------|--------|--------|
| W3C Trace Context | `traceparent`, `tracestate` | `00-{trace_id}-{span_id}-{flags}` |
| B3 (Zipkin) | `X-B3-TraceId`, `X-B3-SpanId`, `X-B3-ParentSpanId` | Separate headers per field |

### Span Structure

Each span shall capture:

| Field | Description |
|-------|-------------|
| Trace ID | Unique identifier for the entire request flow |
| Span ID | Unique identifier for this specific operation |
| Parent Span ID | The span that initiated this operation |
| Operation name | Descriptive name (e.g., `POST /api/orders`, `db.query.select`) |
| Start time | Timestamp when the operation began |
| Duration | Time elapsed for this operation |
| Status | OK, ERROR, or UNSET |
| Attributes | Key-value pairs with operation-specific metadata |

### Sampling Strategy

| Strategy | Mechanism | Use Case |
|----------|-----------|----------|
| Head-based sampling | Decision made at trace start; all spans in sampled traces are collected | Predictable overhead, simple implementation |
| Tail-based sampling | Decision made after trace completes; keeps interesting traces (errors, slow) | Better signal, higher resource cost |
| Rate-based | Sample 1 in N requests | Consistent overhead regardless of traffic |

Recommended sampling rates:

| Environment | Rate | Rationale |
|-------------|------|-----------|
| Production (normal) | 1-10% | Balance between visibility and cost |
| Production (errors) | 100% | Always capture error traces |
| Staging | 100% | Full visibility for testing |

## Correlation IDs

### Generation

The system shall generate a correlation ID at the entry point (API gateway, load balancer, or first service):

- Format: UUID v4 (e.g., `req-550e8400-e29b-41d4-a716-446655440000`).
- Header: `X-Correlation-ID` or `X-Request-ID`.

### Propagation Rules

1. If the incoming request contains a correlation ID header, the system shall use it.
2. If no correlation ID is present, the system shall generate one.
3. The correlation ID shall be included in all downstream service calls.
4. The correlation ID shall be included in every log entry.
5. The correlation ID shall be returned in the response headers.

## Alerting Best Practices

### Severity Levels

| Severity | Response Time | Notification Method | Escalation |
|----------|--------------|--------------------|-----------|
| P1 - Critical | 15 minutes | Page (PagerDuty/Opsgenie), phone call | Incident commander, engineering lead |
| P2 - High | 1 hour | Push notification, SMS | On-call engineer, team lead |
| P3 - Medium | 4 hours | Team Slack/Teams channel | Team during business hours |
| P4 - Low | Next business day | Dashboard, email digest | Weekly review |

### Alert Design Principles

1. **Actionable**: Every alert shall have a clear action the responder can take. If no action is possible, it is a metric, not an alert.
2. **Symptomatic**: Alert on user-visible symptoms (high error rate, slow responses) rather than causes (CPU high). Causes are for investigation.
3. **Deduplicated**: Group related alerts to avoid alert fatigue. One incident, one alert.
4. **Documented**: Every alert shall link to a runbook with diagnostic steps and remediation procedures.
5. **Tuned**: Review alert thresholds quarterly. Alerts that fire without requiring action shall be tuned or removed.

### Alert Anti-Patterns

| Anti-Pattern | Problem | Remedy |
|-------------|---------|--------|
| Alerting on every metric | Alert fatigue, responders ignore alerts | Alert only on user-facing symptoms |
| Static thresholds for variable traffic | False positives during low traffic, missed during high traffic | Use dynamic thresholds or anomaly detection |
| No runbook linked | Responder wastes time diagnosing from scratch | Require runbook URL in alert metadata |
| Alert on single data point | Flapping alerts from transient spikes | Require sustained condition (e.g., 3 of 5 data points) |

### Runbook Template

Each alert shall reference a runbook containing:

1. **Alert description**: What the alert means in plain language.
2. **Impact assessment**: What users experience when this fires.
3. **Diagnostic steps**: Ordered checklist to identify the root cause.
4. **Remediation steps**: Actions to resolve each common cause.
5. **Escalation path**: When and to whom to escalate if initial steps fail.
6. **Post-incident**: Link to incident review process.

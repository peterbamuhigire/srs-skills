## 9. Non-Functional Requirements for the Mobile API

All NFRs in this section carry measurable thresholds per IEEE-982.1 and the Prohibition on Vague Adjectives rule in the project engineering standards. Each NFR is cross-referenced to the platform-wide NFR baseline in `_context/domain.md` where applicable.

### NFR-MAPI-001 — Mobile API Response Time (cross-reference: NFR-PERF-003)

The system shall return any Mobile API response in ≤ 500 ms at P95 under a load of 50 concurrent mobile API clients per tenant, measured at the server response boundary (excluding network transmission time to the mobile device).

- Metric: P95 response latency ≤ 500 ms.
- Measurement point: Server-side request processing time logged per request.
- Load condition: 50 concurrent authenticated mobile clients per tenant, executing a representative mix of read (70%) and write (30%) operations.
- Test method: Load test using a representative request mix; measure P95 latency over a 10-minute steady-state window.

### NFR-MAPI-002 — Offline Resilience (cross-reference: NFR-MOBILE-001)

The Cooperative Procurement module shall support offline intake of commodity transactions for ≥ 72 consecutive hours without connectivity. Upon connectivity restoration, the system shall synchronise all pending offline records to the server within 60 seconds.

- Metric 1: Offline duration support ≥ 72 hours.
- Metric 2: Sync completion time ≤ 60 seconds from connectivity restoration.
- Load condition: Up to 200 pending offline transactions queued during the offline period.
- Test method: Record transactions offline for 72 hours; restore connectivity; measure elapsed time from connectivity restoration to all records appearing in the server database.

### NFR-MAPI-003 — Concurrent Mobile Session Capacity

The Mobile API shall support ≥ 200 concurrent authenticated mobile sessions per tenant without the P95 response latency exceeding the threshold defined in NFR-MAPI-001 (≤ 500 ms).

- Metric: P95 response latency ≤ 500 ms sustained at 200 concurrent sessions per tenant.
- Measurement point: Server-side request processing time.
- Test method: Load test at 200 concurrent sessions per tenant across 5 tenants simultaneously; assert no tenant experiences P95 latency > 500 ms.

### NFR-MAPI-004 — JWT Token Validation Latency

The system shall complete JWT token signature verification and claims extraction in ≤ 10 ms at P99, measured from receipt of the Authorization header to completion of the validation function in `firebase/php-jwt`.

- Metric: P99 JWT validation latency ≤ 10 ms.
- Measurement point: Instrumented timer wrapping the JWT decode call in the authentication middleware.
- Test method: Submit 10,000 requests with valid JWTs; measure P99 validation time from middleware instrumentation logs.

### NFR-MAPI-005 — TLS Encryption in Transit

All Mobile API traffic shall be transmitted over TLS 1.3 or higher. Connections using TLS 1.2 or earlier shall be rejected at the web server layer.

- Metric: 0% of Mobile API requests accepted over TLS < 1.3 in production.
- Test method: Attempt a Mobile API connection using a TLS 1.2 client; assert the connection is refused by the server before any HTTP response is issued.

### NFR-MAPI-006 — Audit Log Coverage

Every state-changing Mobile API request (POST, PUT, PATCH, DELETE) shall generate an audit log entry within 1 second of the request completing, recording: `user_id`, `tenant_id`, `endpoint`, HTTP method, request payload summary, response HTTP status, and `timestamp`.

- Metric: 100% of state-changing requests produce an audit log entry; audit log entry written within 1 second of response.
- Test method: Execute 100 state-changing requests; assert 100 corresponding audit log entries exist; assert all entries have `timestamp` within 1 second of the HTTP response timestamp.

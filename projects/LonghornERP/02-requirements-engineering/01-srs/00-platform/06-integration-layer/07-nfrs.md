# 7. Non-Functional Requirements for the Integration Layer

## 7.1 Performance

**NFR-INTG-001:** The Integration Layer shall complete EFRIS invoice submission and return the fiscal document number to the calling module within 5 seconds at P95 under normal operating load, measured from the moment the EFRIS adapter dispatches the HTTP POST to the URA endpoint until the fiscal response is stored in the database.

**NFR-INTG-002:** The Integration Layer shall process and post an inbound mobile money provider callback to the payment ledger within 3 seconds at P95, measured from HTTP receipt of the callback at the Longhorn ERP callback endpoint until the corresponding invoice or billing record is updated to `PAID` or `FAILED`.

**NFR-INTG-003:** The webhook framework shall dispatch outbound webhook notifications within 10 seconds of the triggering event at P95 under normal operating load, with no data loss for events that have active subscriptions.

## 7.2 Availability and Resilience

**NFR-INTG-004:** Outbound integration payloads (EFRIS, eTIMS, NSSF, mobile money disbursements) shall be durably queued for retry without blocking the tenant-facing workflow when the target external service is unavailable, ensuring zero payload loss for queued items.

**NFR-INTG-005:** The offline queue shall support durable storage of EFRIS and eTIMS payloads for a minimum of 72 hours during external service unavailability, without data loss.

**NFR-INTG-006:** The webhook Dead-Letter Queue (DLQ) shall support durable storage of failed webhook payloads for a minimum of 7 days without data loss.

## 7.3 Security

**NFR-INTG-007:** All third-party API credentials (EFRIS, KRA eTIMS, NSSF, all mobile money providers) shall be encrypted at rest using AES-256 and shall never be returned in API responses, surfaced in application logs, or exposed in error messages at any point in the request or response lifecycle.

**NFR-INTG-008:** All outbound Integration Layer communications shall use TLS 1.2 or higher; connections using TLS 1.0, TLS 1.1, or SSLv3 shall be refused.

**NFR-INTG-009:** Webhook outbound payloads shall be signed with HMAC-SHA256 using the tenant's registered secret, and the `X-Longhorn-Signature` header shall be present on every outbound webhook request without exception.

## 7.4 Scalability

**NFR-INTG-010:** The Integration Layer shall process concurrent EFRIS and eTIMS submissions for multiple tenants without degradation in submission latency beyond the P95 threshold stated in **NFR-INTG-001**, when the system is operating at the documented maximum tenant concurrency load.

**NFR-INTG-011:** The webhook delivery engine shall support up to 10,000 webhook dispatches per minute across all tenants without queuing delays exceeding the P95 threshold stated in **NFR-INTG-003**, when measured under sustained peak load.

## 7.5 Auditability

**NFR-INTG-012:** Every Integration Layer transaction (submission, callback, retry, queue event, DLQ entry, reversal) shall be logged with a unique correlation ID, tenant ID, timestamp (UTC), integration type, and outcome, in the platform audit log, to support post-incident investigation and regulatory audit within a maximum of 5 minutes of the event occurring.

**NFR-INTG-013:** NSSF contribution files and submission outcomes shall be retained for a minimum of 7 years in immutable storage, satisfying statutory record-keeping obligations under applicable Ugandan and Kenyan labour law.

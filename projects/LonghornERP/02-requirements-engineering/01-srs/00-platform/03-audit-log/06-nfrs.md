## 6. Non-Functional Requirements

<!-- [DOMAIN-DEFAULT: ERP] Source: _context/domain.md — NFR-SEC-002 incorporated below -->

**NFR-AUDIT-001 (cross-reference: NFR-SEC-002):** The system shall ensure that no audit log record can be updated or deleted by any user, including super administrators.

- *Metric:* Penetration test attempting `UPDATE` and `DELETE` on `audit_log` using the application database user credentials — expected result: permission denied error returned by the database for 100% of attempts.
- *Measurement method:* Automated penetration test executed by a qualified security tester using direct database credentials. The test suite shall attempt at least 5 distinct `UPDATE` patterns and 5 distinct `DELETE` patterns. Zero successful modifications constitute a pass.
- *Verification frequency:* Once before initial deployment; re-verified after any schema migration or database privilege change.

<!-- [END DOMAIN-DEFAULT] -->

**NFR-AUDIT-002:** The system shall write an audit log record within 100 ms at P99 of the triggering action completing, measured at the database commit boundary of the audit INSERT statement.

- *Metric:* P99 latency of audit `INSERT` commit ≤ 100 ms.
- *Measurement method:* Load test generating 500 state-changing operations per minute across 50 concurrent users. Capture audit INSERT commit latency using database-level query timing. Calculate P99 from ≥ 10,000 samples. Any run where P99 exceeds 100 ms constitutes a failure.
- *Rationale:* Audit writes on the dedicated connection pool (per FR-AUDIT-039) must not become a performance bottleneck under normal operational load.

**NFR-AUDIT-003:** The system shall return audit log search results for any date range within the retention window in ≤ 5 seconds at P95, for a dataset of up to 10 million records, measured at the server response boundary (excluding network transit time to the browser).

- *Metric:* P95 search response time ≤ 5 seconds for a 10-million-record dataset.
- *Measurement method:* Load a test database with 10 million audit records spanning 7 years. Execute 100 search queries with varied filter combinations (single filter, multi-filter, full date range) using a load testing tool. Record server-side response times. Calculate P95. A pass requires P95 ≤ 5 seconds across all query patterns.
- *Supporting implementation:* Database indices on `(tenant_id, timestamp)`, `(tenant_id, module, action)`, `(tenant_id, affected_table, affected_record_id)`, and `(tenant_id, user_id, timestamp)` are mandatory to meet this threshold.

**NFR-AUDIT-004:** The system shall support simultaneous audit log search queries by up to 10 concurrent external auditor sessions without degrading search response time below the P95 threshold defined in NFR-AUDIT-003.

- *Metric:* P95 search response time ≤ 5 seconds under 10 concurrent `external_auditor` session queries.
- *Measurement method:* Simulate 10 concurrent sessions each submitting a search query against the 10-million-record test dataset at the same instant. Measure response time for each query. Calculate P95 across all 10 sessions per test run. Repeat 20 times. A pass requires P95 ≤ 5 seconds across all runs.
- *Rationale:* External audit engagements may involve multiple auditors working simultaneously. Degraded query performance during an audit constitutes a compliance risk.

**NFR-AUDIT-005:** The audit log search interface shall render the search results page in ≤ 2 seconds at P95 under a load of 100 concurrent tenant users, measured at the server response boundary, consistent with NFR-PERF-001.

- *Metric:* P95 page render time ≤ 2 seconds at 100 concurrent users.
- *Measurement method:* As specified in NFR-PERF-001. Audit log pages are included in the standard P95 page load benchmark suite.

**NFR-AUDIT-006:** The system shall retain audit log data for a minimum of 7 years, consistent with the Uganda Companies Act Cap. 110 minimum of 5 years and the system default of 7 years. No automated process shall delete a record before its retention period has elapsed.

- *Metric:* Zero records deleted before their retention period expires in any automated job run.
- *Measurement method:* Review archival and purge job execution logs after each run. Confirm that the `oldest_record_timestamp` in every `AUDIT_PURGE` event is ≥ 7 years before the purge execution date. Any record purged before 7 years constitutes a Critical severity defect.

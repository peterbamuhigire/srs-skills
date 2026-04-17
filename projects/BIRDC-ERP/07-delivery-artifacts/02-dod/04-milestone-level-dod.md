## 3. Milestone-Level Definition of Done

In addition to all task-level criteria being satisfied for every task within the milestone, a milestone is DONE only when ALL of the following are true.

### 3.1 Phase Gate Criteria Satisfied

All phase gate criteria specified for that milestone in the Phase Gate Criteria & Metrics document (`_context/metrics.md`) are satisfied and verified. No criterion may be deferred to a later milestone without written Director approval and a documented deferral notice attached to the Milestone Acceptance Certificate.

### 3.2 Performance Thresholds Verified

All non-functional performance thresholds applicable to the delivered modules are tested and passing on the staging environment:

- POS transaction time (search to receipt): ≤ 90 seconds for the Prossy cashier test scenario.
- Product search response (barcode or text): ≤ 500 ms at P95.
- Report generation (standard report, up to 12 months): ≤ 10 seconds.
- Trial Balance generation: ≤ 5 seconds (M-002 and above).
- Farmer contribution breakdown (per batch, 100+ farmers): ≤ 3 seconds (M-003 and above).
- Agent cash balance refresh: real-time on every transaction post (M-001 and above).
- Offline POS data loss on connectivity loss: zero — all transactions persisted locally (M-001 and above).
- Offline sync time (Android apps, on reconnect): ≤ 60 seconds for a typical day's transactions (applicable milestones).
- Concurrent user test: 50 simultaneous web users without degradation (M-007 load test only).
- Audit trail query (any 30-day period, any user): ≤ 5 seconds (M-006 and above).

### 3.3 Client Demonstration Completed

A formal live demonstration of all milestone deliverables has been conducted with the Finance Director (STK-002) and the BIRDC Director (STK-001) present. The demonstration is conducted on the staging environment. The demonstration covers every functional area delivered in the milestone.

### 3.4 Milestone Acceptance Certificate Signed

The Milestone Acceptance Certificate has been signed by both the Finance Director and the BIRDC Director. The certificate is filed by Peter Bamuhigire in the project records.

### 3.5 Payment Invoice Raised

A payment invoice for the milestone fixed price has been raised and submitted to BIRDC/PIBID Finance. The next milestone kickoff is not scheduled until payment is confirmed.

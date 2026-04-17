## 7. Phase Gate Entry and Exit Criteria

Each phase gate requires ALL listed criteria to be satisfied before the next delivery phase begins.

### Phase 1 Gate — Commerce Foundation

**Entry criteria:**
- All F-001 (Sales), F-002 (POS), F-003 (Inventory), and F-004 (Agent Distribution) unit and integration tests pass.
- Staging environment provisioned with test chart of accounts, agent records, and product catalogue.

**Exit criteria:**
- All system test journeys for F-001 through F-004 pass without Critical or High defects.
- EFRIS sandbox submission returns a valid FDN for a test invoice and a test POS receipt.
- Dual-track inventory report verified: warehouse stock total and agent stock total shown separately; no cross-contamination (BR-001).
- Agent cash balance updates in real time on posting of a test sale (latency ≤ 2 seconds).
- Sales Agent App (Android) and Warehouse App (Android) tested on minimum API 26 device.
- Offline POS: 50 transactions recorded offline; 100% synced on reconnect; GL auto-posts confirmed.
- BIRDC Sales Manager and Store Manager sign Phase 1 UAT acceptance form.
- Peter Bamuhigire signs test completion report.

### Phase 2 Gate — Financial Core

**Entry criteria:** Phase 1 gate passed and signed.

**Exit criteria:**
- Trial Balance, P&L, Balance Sheet, and Cash Flow Statement (IAS 7) generated correctly for a test fiscal period; figures verified by Finance Director.
- Parliamentary budget vote tracking: test vote reaches 80% threshold — alert generated; 95% threshold — alert generated; over-100% expenditure attempt blocked (BR-014).
- GL hash chain integrity check passes: no broken links on test dataset of ≥ 500 GL entries (BR-013).
- AR aging report shows correct bucket distribution; agent remittance FIFO allocation verified against TC-AGT-xxx oracle test cases.
- Farmer payment batch (10 test farmers): deductions applied correctly; bulk MTN MoMo payment file generated in correct format.
- Executive Dashboard App tested: P&L snapshot, Trial Balance summary, cash position display correctly.
- BIRDC Finance Director signs Phase 2 UAT acceptance form.

### Phase 3 Gate — Supply Chain and Farmers

**Entry criteria:** Phase 2 gate passed and signed.

**Exit criteria:**
- 5-stage farmer procurement workflow completed end-to-end with ≥ 20 test farmer records: Stage 1 (bulk PO) through Stage 5 (GL posting DR Raw Material Inventory / CR Cooperative Payable).
- BR-011 verified: batch cannot advance to Stage 4 if any kg is unallocated to a farmer.
- PPDA procurement documentation checklist verified for at least 1 micro, 1 small, and 1 large procurement test case.
- Farmer Delivery App tested offline: 5 new farmer registrations, 20 deliveries; 100% synced on reconnect.
- BIRDC Administration Officer signs Phase 3 UAT acceptance form.

### Phase 4 Gate — Production and Quality

**Entry criteria:** Phase 3 gate passed and signed.

**Exit criteria:**
- Circular economy mass balance verified for a test production order: input 1,000 kg matooke; outputs recorded; variance within ±2% of input (BR-008).
- QC gate (BR-004): API returns error when stock transfer attempted with QC status ≠ "Approved."
- CoA generated in correct format for domestic market and ≥ 2 export market formats (South Korea, EU or Saudi Arabia).
- Factory Floor App tested: production completion quantities submitted via app; QC results submitted.
- BIRDC QC Manager signs Phase 4 UAT acceptance form.

### Phase 5 Gate — People

**Entry criteria:** Phase 4 gate passed and signed.

**Exit criteria:**
- PAYE calculation verified for ≥ 5 payroll test cases against Uganda 2024/25 tax band oracles (see Test Plan TC-PAY-xxx).
- NSSF calculation verified: employer 10%, employee 5% (BR-010 and NSSF Act).
- LST deduction applied at the correct rate for Bushenyi local government.
- Payroll lock tested: Finance Manager locks payroll; attempt to modify a line item returns an error.
- ZKTeco biometric data imported; attendance records match device export exactly; manual override requires Finance Manager approval and is logged.
- NSSF remittance schedule generated in the exact NSSF Uganda format.
- HR Self-Service App tested: leave application, payslip view, attendance view.
- BIRDC Finance Director and HR Manager sign Phase 5 UAT acceptance form.

### Phase 6 Gate — Research, Administration, and Compliance

**Entry criteria:** Phase 5 gate passed and signed.

**Exit criteria:**
- PPDA procurement register contains all 3 test procurement transactions with correct document status.
- R&D banana variety database loaded with ≥ 5 real cultivar records.
- System Administration panel: user roles and permissions matrix tested for all 8 role layers; role changes effective immediately.
- Audit log query for any 30-day test period returns within 5 seconds.
- BIRDC IT Administrator signs Phase 6 UAT acceptance form.

### Phase 7 Gate — Integration, Hardening, and Go-Live

**Entry criteria:** Phases 1–6 gates all passed and signed.

**Exit criteria:**
- Full regression suite (all modules) passes with zero failures.
- EFRIS fully wired across all document types: sales invoices, credit notes, POS receipts — each returns a valid FDN in staging.
- OWASP Top 10 (web) and OWASP Mobile Top 10 audit passed: zero Critical or High findings open.
- Load test at 50 concurrent users: all P95 thresholds met.
- Load test at 140 MT/day peak production scenario: no errors, no timeouts.
- OAG audit trail simulation: Finance Director queries any 12-month audit trail; result ≤ 5 seconds; all entries present with actor, IP, timestamp, old/new values.
- All staff trained and training attendance recorded.
- Production go-live cutover plan reviewed and approved by BIRDC Director and Peter Bamuhigire.
- BIRDC Director and Finance Director sign Phase 7 go-live acceptance form.

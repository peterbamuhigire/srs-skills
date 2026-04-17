## 3. Per-Milestone Detail

### 3.1 Milestone 1 — Commerce Foundation

**Modules delivered:** Sales & Distribution (F-001), Point of Sale (F-002), Inventory & Warehouse Management (F-003), Agent Distribution Management (F-004).

**Android apps delivered:** Sales Agent App, Warehouse App.

**Scope summary:**

- Complete order-to-cash cycle: sales order → invoice (draft → pending EFRIS → issued → paid) with GL auto-posting on confirmation.
- EFRIS real-time submission to URA via system-to-system API — Fiscal Document Number and QR code printed on all commercial documents.
- Factory gate POS, distribution centre POS, and agent checkout POS operational, with offline mode and sync on reconnect.
- Multi-payment per transaction: cash, MTN MoMo, Airtel Money, cheque, bank deposit.
- Dual-track inventory: warehouse stock ledger and agent field stock ledger maintained as completely separate ledgers. Dual-track inventory report verified by Store Manager.
- Batch and lot tracking, FEFO enforcement, expiry alerts at 30/60/90-day configurable thresholds.
- 1,071-agent cash balance tracking: live liability register showing each agent's outstanding balance in real time.
- FIFO remittance allocation via stored procedure; remittance segregation of duties enforced (creator != verifier).
- Sales Agent App: offline POS, agent stock management, remittance submission, commission statements, Bluetooth 80mm thermal receipt printing.
- Warehouse App: barcode scan for stock receipt, transfer confirmation, physical count.

**Phase gate criteria (from metrics.md):** All Sales, POS, Inventory, and Agent Distribution functional requirements verified; EFRIS live on invoices and POS receipts; agent cash balance tracking operational; dual-track inventory report verified by Store Manager; Sales Agent App and Warehouse App operational on Android; client sign-off received.

**Key dependencies:** GAP-001 — URA EFRIS API sandbox credentials must be obtained before invoice testing can complete.

---

### 3.2 Milestone 2 — Financial Core

**Modules delivered:** Financial Accounting & General Ledger (F-005), Accounts Receivable (F-006), Accounts Payable (F-007), Budget Management (F-008).

**Android apps delivered:** Executive Dashboard App.

**Scope summary:**

- IFRS for SMEs double-entry accounting with 1,307-account Chart of Accounts (subject to GAP-012 resolution).
- Dual-mode accounting: PIBID parliamentary budget votes and BIRDC commercial IFRS accounts tracked simultaneously in the same system. Consolidated and separated reporting always available.
- Journal entry lifecycle: balanced debit/credit validation, sequential JE numbering (JE-YYYY-NNNN), draft → approved → posted.
- GL auto-posting from all modules delivered in M-001 — no manual journal entries for operational transactions.
- Hash chain integrity: cryptographic hash chain on every GL entry; tampering mathematically detectable.
- Financial statements on demand: Profit & Loss, Balance Sheet, Cash Flow (IAS 7), Trial Balance — no period-closing step required.
- AR aging (current, 30, 60, 90, 120+ days); agent remittance tracking; customer credit hold workflow.
- AP three-way matching (PO → GRN → Invoice); farmer payment system with aggregate contributions, deductions, and net payment per farmer; bulk MTN MoMo/Airtel Money payment file.
- Budget vs. actual variance tracking on demand for both parliamentary (July–June) and commercial fiscal years.
- Executive Dashboard App: P&L snapshot, Trial Balance summary, cash position, budget variance alerts.

**Phase gate criteria:** Trial Balance, P&L, Balance Sheet, and Cash Flow Statement generate correctly; parliamentary budget vote tracking verified by Finance Director; hash chain integrity check passes; AR aging and agent remittance system live; farmer payment batch tested end-to-end; Executive Dashboard App operational; client sign-off received.

**Key dependencies:** GAP-002 (MTN MoMo credentials), GAP-012 (Chart of Accounts confirmation). M-001 must be fully accepted before M-002 begins.

---

### 3.3 Milestone 3 — Supply Chain & Farmers

**Modules delivered:** Procurement & Purchasing (F-009), Farmer & Cooperative Management (F-010).

**Android apps delivered:** Farmer Delivery App.

**Scope summary:**

- Standard supplier procurement with PPDA approval workflow: micro / small / large / restricted thresholds (subject to GAP-007 resolution for exact UGX thresholds).
- RFQ to multiple suppliers with side-by-side comparison; Local Purchase Orders in Uganda standard format; GRN with three-way matching; vendor performance ratings.
- 5-stage cooperative farmer procurement: (1) Bulk PO per cooperative/season, (2) Batch goods receipt at factory gate, (3) Individual farmer contribution breakdown (name, NIN, weight, quality grade, net payable), (4) Stock receipt into factory inventory with batch numbers, (5) GL posting.
- Farmer registration: name, NIN, contact, cooperative, GPS coordinates, mobile money number, photo.
- Farm profiling: multiple farms per farmer, GPS polygon, banana varieties.
- Cooperative organisation: farmers → cooperatives → zones → BIRDC network.
- Extension services: training attendance, input loan issuance, extension officer visit log.
- Bulk farmer payment with SMS payment confirmation via MTN MoMo/Airtel Money.
- Farmer Delivery App: register new farmers offline, GPS farm profiling, record individual deliveries with Bluetooth scale integration, print farmer receipt.

**Phase gate criteria:** 5-stage cooperative farmer procurement workflow end-to-end tested with real farmer data; individual farmer contribution breakdown verified; bulk MTN MoMo farmer payment tested; PPDA procurement documentation checklist verified by Administration Officer; Farmer Delivery App operational offline; client sign-off received.

**Key dependencies:** GAP-004 (Data Protection Act legal review for farmer data), GAP-007 (PPDA thresholds), GAP-011 (Bluetooth scale model). M-002 must be fully accepted before M-003 begins.

---

### 3.4 Milestone 4 — Production & Quality

**Modules delivered:** Manufacturing & Production (F-011), Quality Control & Laboratory (F-012).

**Android apps delivered:** Factory Floor App.

**Scope summary:**

- Recipe/Bill of Materials with version control, including circular economy recipes: banana peel → biogas (calorific value output), waste water → bio-slurry fertiliser (kg output).
- Mass balance verification: primary products + by-products + scrap = 100% of input (BR-008).
- Production order lifecycle: plan → materials reserved → in progress → QC check → completed → closed.
- Material requisition with WIP accounting (DR WIP / CR Raw Material Inventory).
- Production costing: raw materials (FIFO cost) + direct labour + absorbed overhead.
- QC gate: stock transfer to finished goods blocked until QC approves (BR-004).
- Configurable inspection templates (numeric, pass/fail, text, photo parameters); quality grading (A, B, C) with different price tiers for procurement.
- Certificate of Analysis generation: domestic format and minimum 2 export market formats (South Korea, EU/Italy — subject to GAP-010 resolution for exact parameters).
- Statistical Process Control: X-bar and R-charts, Cp and Cpk capability indices.
- Non-conformance Reports with root cause analysis and corrective action tracking.
- Lab equipment management with calibration certificate tracking.
- Factory Floor App: monitor active orders, record worker attendance, enter production completion quantities, submit QC results.

**Phase gate criteria:** Circular economy production order mass balance verified; QC gate blocking inventory release tested; CoA generated for domestic and minimum 2 export market formats; Factory Floor App operational; client sign-off received.

**Key dependencies:** GAP-010 (export QC parameters). M-003 must be fully accepted before M-004 begins.

---

### 3.5 Milestone 5 — People

**Modules delivered:** Human Resources (F-013), Payroll (F-014).

**Android apps delivered:** HR Self-Service App.

**Scope summary:**

- Employee lifecycle: hire to exit; employee profile with NIN, contract type, department, job grade.
- Government pay scales (PIBID) and commercial pay scales (BIRDC) in same system.
- Attendance: manual entry and ZKTeco biometric fingerprint device integration (direct import, no re-entry) — subject to GAP-005 resolution.
- Leave management: annual, sick, maternity, paternity, compassionate, study, unpaid.
- Factory worker registry: skill matrix, daily attendance, productivity metrics, production order assignment.
- Staff loans and advances with automatic payroll deduction.
- Configurable payroll elements — no hardcoded earnings or deductions.
- Uganda PAYE with configurable tax bands (Finance Director updates without developer involvement — DC-002), subject to GAP-008 confirmation of current bands.
- Uganda NSSF: employer 10% / employee 5%; NSSF remittance schedule in exact NSSF Uganda format (subject to GAP-009).
- LST configurable per local government ordinance (Bushenyi, Kampala).
- Payroll lock on Finance Manager approval (BR-010); payroll GL auto-posting on approval.
- Payslip PDF by email or WhatsApp; bank transfer bulk credit file (Uganda bank format — subject to GAP-006); bulk mobile money salary payment via MTN MoMo/Airtel Money batch API.
- HR Self-Service App: apply for leave, view payslips, check leave balance, view attendance.

**Phase gate criteria:** PAYE, NSSF, and LST payroll calculations verified against Uganda tax authority specifications; biometric attendance import from ZKTeco tested; payroll lock and immutability verified; NSSF schedule generated in correct format; HR Self-Service App operational; client sign-off received.

**Key dependencies:** GAP-005 (ZKTeco model), GAP-006 (bank file format), GAP-008 (PAYE bands), GAP-009 (NSSF format). M-002 must be fully accepted before M-005 begins (M-005 can run in parallel with M-003 and M-004 if resources permit, with Director approval).

---

### 3.6 Milestone 6 — Research, Administration & Compliance

**Modules delivered:** Research & Development (F-015), Administration & PPDA Compliance (F-016), System Administration (F-017).

**Android apps delivered:** None.

**Scope summary:**

- Banana variety performance database: cultivar name, processing yield, quality score, regional suitability.
- Field trial management: plot assignment, intervention tracking, harvest data, yield analysis.
- Product development register: new product ideas, pilot batch records, market testing results.
- R&D expenditure tracking linked to GL.
- PPDA procurement documentation management: all required documents per procurement category.
- Procurement register: every procurement transaction with PPDA category classification and document status — verified by Administration Officer.
- Asset register: all BIRDC assets with acquisition date, cost, location, condition, depreciation.
- Vehicle and equipment logbook.
- User management and 8-layer Role and Permission matrix: Role → Page → API endpoint → UI element → Location → Time → Conditional rules → Object ownership.
- Audit log review: complete system-wide audit trail searchable by user, action, date, table; ≤ 5 seconds for any 30-day period query.
- Backup management with automated scheduling and retention policy.
- Integration configuration panel: EFRIS API credentials, mobile money API keys, email SMTP, biometric device connectivity.

**Phase gate criteria:** PPDA procurement register and all document types verified by Administration Officer; R&D banana variety database loaded with real data; system administration panel fully operational; user roles and permissions matrix verified; client sign-off received.

**Key dependencies:** M-005 must be fully accepted before M-006 begins.

---

### 3.7 Milestone 7 — Integration, Hardening & Go-Live

**Modules delivered:** EFRIS Full Integration (F-018), Security Hardening & Acceptance (F-019).

**Android apps delivered:** All 6 Android apps deployed to production devices.

**Scope summary:**

- URA EFRIS system-to-system API fully wired across all transaction types: sales invoices, credit notes, POS receipts, credit notes. Fiscal Document Number and QR code on every commercial document.
- Failed EFRIS submission retry queue with alert to Finance Manager; EFRIS audit log with tamper-evident records.
- OWASP Top 10 remediation and penetration test.
- Load testing: 140 MT/day peak production scenario simulation — all 50 concurrent web users without degradation.
- Full regression across all 17 modules.
- OAG audit trail review simulation: Finance Director and external auditor scenario run end-to-end.
- All staff trained by role: accounts assistants, cashiers, warehouse staff, HR, production supervisors, IT Administrator.
- Production go-live cutover: data migration from legacy systems (subject to GAP-014), go-live date confirmed by Director.

**Phase gate criteria:** All 17 modules pass full regression; EFRIS wired across all document types; OWASP Top 10 audit passed; load test at 140 MT/day peak simulation passed; OAG audit trail review simulated and passed; all staff trained; production go-live completed; client sign-off received.

**Key dependencies:** GAP-001 (EFRIS credentials must be fully resolved), GAP-013 (server hardware specs), GAP-014 (legacy data migration). M-006 must be fully accepted before M-007 begins.

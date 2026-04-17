# Section 1: Functional Requirements to Business Goals and Test Cases

## 1.1 Phase 1 — Commerce Foundation

### Module SAL: Sales and Distribution (F-001)

| FR ID | Requirement Summary | Business Goal | Business Rule | Test Case ID |
|---|---|---|---|---|
| FR-SAL-001 | The system shall manage the invoice lifecycle (draft → pending EFRIS → issued → partially paid → paid → void). | BG-001, BG-002 | BR-009 | TC-SAL-001 |
| FR-SAL-002 | The system shall post GL entries automatically on invoice confirmation (DR AR / CR Revenue; DR COGS / CR Inventory). | BG-002 | BR-009 | TC-SAL-002 |
| FR-SAL-003 | The system shall submit every commercial invoice to URA EFRIS in real time via system-to-system API and store the returned FDN. | BG-002, BG-001 | — | TC-SAL-003 |
| FR-SAL-004 | The system shall enforce territory-based sales tracking so that each invoice is attributed to a defined sales territory. | BG-001, BG-003 | — | TC-SAL-004 |
| FR-SAL-005 | The system shall support multiple configurable price lists (wholesale, retail, export, institutional) applied per customer. | BG-001, BG-005 | — | TC-SAL-005 |
| FR-SAL-006 | The system shall enforce credit limits: the system shall block invoice confirmation when the customer's outstanding AR balance exceeds the configured credit limit. | BG-001, BG-002 | — | TC-SAL-006 |
| FR-SAL-007 | The system shall generate credit notes linked to originating invoices with full GL reversal. | BG-002 | BR-009 | TC-SAL-007 |
| FR-SAL-008 | The system shall send a daily sales summary push notification to the Director and Sales Manager within 5 minutes of the reporting cut-off. | BG-001, BG-003 | — | TC-SAL-008 |
| FR-SAL-009 | The system shall void an invoice and flag it VOID without recycling the invoice number; the void event shall be written to the audit trail. | BG-002 | BR-009 | TC-SAL-009 |
| FR-SAL-010 | The system shall generate multi-currency invoices (UGX, USD, EUR, KES) with exchange rate recorded at time of invoice. | BG-002 | — | TC-SAL-010 |
| FR-SAL-011 | The system shall display a side-by-side aged receivables view per customer at the time of new order entry. | BG-001, BG-002 | — | TC-SAL-011 |
| FR-SAL-012 | The system shall generate an EFRIS retry queue when a submission fails and alert the Finance Manager within 60 seconds of the failure. | BG-002 | — | TC-SAL-012 |

### Module POS: Point of Sale (F-002)

| FR ID | Requirement Summary | Business Goal | Business Rule | Test Case ID |
|---|---|---|---|---|
| FR-POS-001 | The system shall support three POS contexts (factory gate, distribution centre, agent checkout) with context-appropriate inventory sources. | BG-001, BG-003 | BR-001 | TC-POS-001 |
| FR-POS-002 | The system shall complete a product search by name, code, or barcode scan within ≤ 500 ms at P95. | BG-001 | — | TC-POS-002 |
| FR-POS-003 | The system shall accept multi-payment per transaction (cash, MTN MoMo, Airtel Money, cheque, bank deposit) and split tendering between methods. | BG-001 | — | TC-POS-003 |
| FR-POS-004 | The system shall manage POS sessions with opening float, end-of-shift reconciliation, and variance report generation. | BG-002, BG-003 | — | TC-POS-004 |
| FR-POS-005 | The system shall generate receipts in three formats: 80 mm thermal receipt, A4 invoice, and SMS/WhatsApp digital receipt. | BG-001 | — | TC-POS-005 |
| FR-POS-006 | The system shall operate in fully offline mode, storing transactions locally when connectivity is unavailable, and sync to the server within ≤ 60 seconds of reconnection. | BG-001 | — | TC-POS-006 |
| FR-POS-007 | The system shall process the complete flow from product search to receipt generation within ≤ 90 seconds (Prossy cashier test). | BG-001 | DC-001 | TC-POS-007 |
| FR-POS-008 | The system shall submit POS receipts to URA EFRIS on every transaction and print the FDN on the thermal receipt. | BG-002 | — | TC-POS-008 |
| FR-POS-009 | The system shall use agent virtual inventory as the stock source for agent POS, never warehouse stock. | BG-003 | BR-001 | TC-POS-009 |
| FR-POS-010 | The agent POS shall operate on Android with Bluetooth 80 mm thermal receipt printing. | BG-001, BG-003 | — | TC-POS-010 |
| FR-POS-011 | The system shall enforce FEFO batch selection automatically at the POS: the earliest-expiry batch is allocated first; manual override is not permitted. | BG-001 | BR-007 | TC-POS-011 |

### Module INV: Inventory and Warehouse Management (F-003)

| FR ID | Requirement Summary | Business Goal | Business Rule | Test Case ID |
|---|---|---|---|---|
| FR-INV-001 | The system shall maintain dual-track inventory: warehouse stock in `tbl_stock_balance` and agent stock in `tbl_agent_stock_balance` as permanently separate ledgers. | BG-001, BG-003 | BR-001 | TC-INV-001 |
| FR-INV-002 | The system shall support unlimited warehouse locations with independent stock balances per location. | BG-001 | — | TC-INV-002 |
| FR-INV-003 | The system shall maintain a stock item catalogue with a unit of measure (UOM) conversion engine. | BG-001 | — | TC-INV-003 |
| FR-INV-004 | The system shall track every stock batch with manufacturing date, expiry date, and batch number. | BG-001, BG-004 | — | TC-INV-004 |
| FR-INV-005 | The system shall enforce FEFO: when allocating stock for a sale, transfer, or production input, the batch with the earliest expiry date shall be selected first; manual selection that violates FEFO shall be blocked. | BG-001 | BR-007 | TC-INV-005 |
| FR-INV-006 | The system shall generate expiry alerts at 30, 60, and 90-day configurable thresholds for all expiry-tracked products. | BG-001 | — | TC-INV-006 |
| FR-INV-007 | The system shall manage stock transfers with an in-transit status visible to both source and destination locations. | BG-001 | — | TC-INV-007 |
| FR-INV-008 | The system shall enforce a physical stock count workflow: freeze → count → variance report → approval before adjustments are posted. | BG-002 | BR-003 | TC-INV-008 |
| FR-INV-009 | The system shall post GL entries automatically for all stock adjustments. | BG-002 | — | TC-INV-009 |
| FR-INV-010 | The system shall value stock using FIFO or moving average method as configured per item category. | BG-002 | — | TC-INV-010 |
| FR-INV-011 | The Warehouse App (Android) shall support barcode scanning for stock receipt, transfer confirmation, and physical count. | BG-001 | — | TC-INV-011 |
| FR-INV-012 | The system shall generate a consolidated stock report showing warehouse stock and agent stock in clearly labelled separate sections. | BG-001, BG-003 | BR-001 | TC-INV-012 |

### Module AGT: Agent Distribution Management (F-004)

| FR ID | Requirement Summary | Business Goal | Business Rule | Test Case ID |
|---|---|---|---|---|
| FR-AGT-001 | The system shall register each of the 1,071 agents with a virtual inventory store, territory assignment, stock float limit, and commission rate. | BG-003 | BR-006 | TC-AGT-001 |
| FR-AGT-002 | The system shall compute the agent cash balance in real time as: sum(invoices issued) minus sum(verified remittances), updated on every transaction post. | BG-003 | — | TC-AGT-002 |
| FR-AGT-003 | The system shall allocate remittances to outstanding agent invoices in FIFO order via stored procedure `sp_apply_remittance_to_invoices`; manual invoice selection shall not be permitted. | BG-003 | BR-002 | TC-AGT-003 |
| FR-AGT-004 | The system shall enforce segregation of duties on remittance verification: the user who records a remittance cannot be the same user who verifies it; this check shall be enforced at the API layer. | BG-002, BG-003 | BR-003 | TC-AGT-004 |
| FR-AGT-005 | The system shall calculate agent commission on verified sales only; unverified remittances shall accrue no commission. | BG-003 | BR-015 | TC-AGT-005 |
| FR-AGT-006 | The system shall block stock issuance to an agent when the monetary value of the agent's current stock balance plus the new issuance would exceed the configured float limit. | BG-003 | BR-006 | TC-AGT-006 |
| FR-AGT-007 | The system shall manage agent stock returns with a workflow that adjusts both agent stock balance and warehouse stock. | BG-003 | BR-001 | TC-AGT-007 |
| FR-AGT-008 | The system shall generate agent performance reports including territory ranking, agent ranking, and outstanding balance list. | BG-003, BG-001 | — | TC-AGT-008 |
| FR-AGT-009 | The Sales Agent App (Android) shall support offline POS, agent stock view, remittance submission, and commission statement viewing. | BG-003 | DC-005 | TC-AGT-009 |

## 1.2 Phase 2 — Financial Core

### Module FIN: Financial Accounting and General Ledger (F-005)

| FR ID | Requirement Summary | Business Goal | Business Rule | Test Case ID |
|---|---|---|---|---|
| FR-FIN-001 | The system shall implement IFRS for SMEs double-entry accounting with a hierarchical chart of accounts supporting 1,307 accounts. | BG-002 | — | TC-FIN-001 |
| FR-FIN-002 | The system shall implement dual-mode accounting: PIBID parliamentary budget votes and BIRDC commercial IFRS accounts tracked simultaneously in one system. | BG-002 | DC-004 | TC-FIN-002 |
| FR-FIN-003 | The system shall validate every journal entry for balanced debits and credits before posting; an unbalanced JE shall be rejected with an error specifying the imbalance amount. | BG-002 | — | TC-FIN-003 |
| FR-FIN-004 | The system shall assign sequential JE numbers in the format JE-YYYY-NNNN; gaps in the sequence shall trigger an alert to the Finance Manager and be logged in the audit trail. | BG-002 | BR-009 | TC-FIN-004 |
| FR-FIN-005 | The system shall enforce a JE lifecycle: draft → approved → posted; a posted JE cannot be modified or deleted. | BG-002 | BR-003 | TC-FIN-005 |
| FR-FIN-006 | The system shall auto-post GL entries from all 17 modules; no manual journal entries shall be required for operational transactions. | BG-002 | — | TC-FIN-006 |
| FR-FIN-007 | The system shall maintain a cryptographic hash chain on every GL entry; the system shall detect any hash chain break and report it to the Finance Director on demand. | BG-002 | BR-013 | TC-FIN-007 |
| FR-FIN-008 | The system shall generate the Trial Balance within ≤ 5 seconds at any point without period closing. | BG-002 | — | TC-FIN-008 |
| FR-FIN-009 | The system shall generate P&L, Balance Sheet (IFRS format), Cash Flow Statement (IAS 7), and Trial Balance on demand for both PIBID and BIRDC modes. | BG-002 | — | TC-FIN-009 |
| FR-FIN-010 | The system shall support multi-currency: UGX as functional currency; USD, EUR, and KES for export transactions. | BG-002 | — | TC-FIN-010 |
| FR-FIN-011 | The system shall support fiscal year configurations: July–June (PIBID parliamentary year) and January–December (BIRDC commercial year). | BG-002 | — | TC-FIN-011 |
| FR-FIN-012 | The Finance Director shall be able to update PAYE tax bands, NSSF rates, and other configurable financial parameters via the UI without developer involvement. | BG-005 | DC-002 | TC-FIN-012 |

### Module AR: Accounts Receivable (F-006)

| FR ID | Requirement Summary | Business Goal | Business Rule | Test Case ID |
|---|---|---|---|---|
| FR-AR-001 | The system shall track AR aging in five buckets: current, 30, 60, 90, and 120+ days for all customers and agents. | BG-002, BG-003 | — | TC-AR-001 |
| FR-AR-002 | The system shall compute agent receivable balance as: invoices issued to agent's customers on credit minus verified remittances. | BG-003 | BR-002 | TC-AR-002 |
| FR-AR-003 | The system shall enforce customer credit hold: when a customer's AR balance exceeds their credit limit, new order confirmation shall be blocked. | BG-002 | — | TC-AR-003 |
| FR-AR-004 | The system shall generate customer statements on demand for any date range. | BG-002 | — | TC-AR-004 |
| FR-AR-005 | The system shall auto-allocate customer payments to the oldest outstanding invoice by default. | BG-002 | — | TC-AR-005 |
| FR-AR-006 | The system shall accept payment receipts by bank transfer, mobile money, and cheque, and post corresponding GL entries. | BG-002 | — | TC-AR-006 |
| FR-AR-007 | The Executive Dashboard App (Android) shall display P&L snapshot, Trial Balance summary, cash position, and budget variance alerts. | BG-002, BG-001 | — | TC-AR-007 |

### Module AP: Accounts Payable (F-007)

| FR ID | Requirement Summary | Business Goal | Business Rule | Test Case ID |
|---|---|---|---|---|
| FR-AP-001 | The system shall register vendor invoices and enforce three-way matching against Purchase Order and GRN before payment authorisation. | BG-002 | BR-012 | TC-AP-001 |
| FR-AP-002 | The system shall flag for Finance Manager review any vendor invoice where the price variance exceeds 5% against the PO or quantity variance exceeds 2%. | BG-002 | BR-012 | TC-AP-002 |
| FR-AP-003 | The system shall track AP aging by vendor and by invoice. | BG-002 | — | TC-AP-003 |
| FR-AP-004 | The system shall process vendor payments by bank transfer, mobile money, and cheque with corresponding GL postings. | BG-002 | — | TC-AP-004 |
| FR-AP-005 | The system shall calculate individual farmer net payment: aggregate contributions minus loan repayments and cooperative levies, per period. | BG-004, BG-002 | BR-011 | TC-AP-005 |
| FR-AP-006 | The system shall generate a bulk MTN MoMo / Airtel Money farmer payment file for batch submission to the mobile money API. | BG-004, BG-002 | — | TC-AP-006 |
| FR-AP-007 | The system shall calculate withholding tax (WHT) at 6% on applicable local service supplier payments per Uganda Income Tax Act and generate URA WHT certificates. | BG-002 | — | TC-AP-007 |
| FR-AP-008 | The system shall include a cash position check in the payment scheduling workflow. | BG-002 | — | TC-AP-008 |

### Module BUD: Budget Management (F-008)

| FR ID | Requirement Summary | Business Goal | Business Rule | Test Case ID |
|---|---|---|---|---|
| FR-BUD-001 | The system shall manage PIBID parliamentary budget votes by department and vote code, aligned to the parliamentary financial year (July–June). | BG-002, BG-005 | — | TC-BUD-001 |
| FR-BUD-002 | The system shall manage BIRDC commercial budgets by account and cost centre, aligned to January–December. | BG-002 | — | TC-BUD-002 |
| FR-BUD-003 | The system shall generate a Budget vs. Actual variance report on demand for both modes. | BG-002, BG-005 | — | TC-BUD-003 |
| FR-BUD-004 | The system shall alert the Finance Director and Director when cumulative expenditure against any parliamentary budget vote reaches 80% of the vote amount. | BG-002 | BR-014 | TC-BUD-004 |
| FR-BUD-005 | The system shall generate a second alert when expenditure reaches 95% of any vote. | BG-002 | BR-014 | TC-BUD-005 |
| FR-BUD-006 | The system shall block expenditure that would exceed 100% of a vote unless a Director-level override with written justification is logged in the audit trail. | BG-002 | BR-014 | TC-BUD-006 |

## 1.3 Phase 3 — Supply Chain and Farmers

### Module PRO: Procurement and Purchasing (F-009)

| FR ID | Requirement Summary | Business Goal | Business Rule | Test Case ID |
|---|---|---|---|---|
| FR-PRO-001 | The system shall classify all procurement transactions by Uganda PPDA Act category (micro, small, large, restricted). | BG-001, BG-005 | BR-005 | TC-PRO-001 |
| FR-PRO-002 | The system shall enforce the PPDA approval matrix: Micro — Department Head; Small — Finance Manager + Procurement Officer; Large — Director + Finance Manager; Restricted — Board + all PPDA documents complete. | BG-001, BG-005 | BR-005 | TC-PRO-002 |
| FR-PRO-003 | The system shall block payment processing for any procurement transaction missing required PPDA documentation. | BG-001, BG-005 | BR-005 | TC-PRO-003 |
| FR-PRO-004 | The system shall generate and manage RFQs to multiple suppliers with side-by-side quotation comparison. | BG-001 | — | TC-PRO-004 |
| FR-PRO-005 | The system shall generate LPOs in Uganda standard format. | BG-001, BG-005 | — | TC-PRO-005 |
| FR-PRO-006 | The system shall enforce three-way matching on GRN against PO and vendor invoice before payment. | BG-002 | BR-012 | TC-PRO-006 |
| FR-PRO-007 | The system shall manage vendor performance ratings and document attachments. | BG-001 | — | TC-PRO-007 |
| FR-PRO-008 | The system shall implement the 5-stage cooperative farmer procurement workflow: Bulk PO → Batch Goods Receipt → Individual Farmer Contribution Breakdown → Stock Receipt → GL Posting. | BG-004, BG-001 | BR-011 | TC-PRO-008 |
| FR-PRO-009 | The system shall block a cooperative batch from advancing to Stage 4 (Stock Receipt) until every kilogramme in the batch is allocated to a specific registered farmer with a quality grade and unit price. | BG-004 | BR-011 | TC-PRO-009 |
| FR-PRO-010 | The system shall post GL entries at Stage 5: DR Raw Material Inventory / CR Cooperative Payable per cooperative. | BG-002, BG-004 | — | TC-PRO-010 |
| FR-PRO-011 | The Farmer Delivery App (Android) shall register new farmers offline, record GPS farm coordinates, record individual deliveries with Bluetooth scale integration, and print a farmer receipt. | BG-004, BG-001 | DC-005 | TC-PRO-011 |
| FR-PRO-012 | The system shall complete the individual farmer contribution breakdown for a batch of 100 or more farmers within ≤ 3 seconds. | BG-004 | — | TC-PRO-012 |

### Module FAR: Farmer and Cooperative Management (F-010)

| FR ID | Requirement Summary | Business Goal | Business Rule | Test Case ID |
|---|---|---|---|---|
| FR-FAR-001 | The system shall register farmers with: name, NIN, contact, cooperative, GPS coordinates, mobile money number, and photo. All PII fields shall be encrypted at rest. | BG-004, BG-001 | — | TC-FAR-001 |
| FR-FAR-002 | The system shall support multiple farm profiles per farmer: size, GPS polygon, banana varieties, livestock, and infrastructure. | BG-004 | — | TC-FAR-002 |
| FR-FAR-003 | The system shall track banana varieties by cultivar name across the cooperative network. | BG-004 | — | TC-FAR-003 |
| FR-FAR-004 | The system shall maintain a full delivery history per farmer: quality grades, deductions, and net payments. | BG-004 | — | TC-FAR-004 |
| FR-FAR-005 | The system shall organise farmers in a 3-level hierarchy: farmers → cooperatives → zones → BIRDC network. | BG-004, BG-001 | — | TC-FAR-005 |
| FR-FAR-006 | The system shall manage extension services: training attendance, input loan issuance and repayment, and extension officer visit log. | BG-004 | — | TC-FAR-006 |
| FR-FAR-007 | The system shall generate farmer performance rankings at cooperative and zone level. | BG-004 | — | TC-FAR-007 |
| FR-FAR-008 | The system shall send an SMS payment confirmation to each farmer upon bulk payment processing. | BG-004, BG-003 | — | TC-FAR-008 |
| FR-FAR-009 | Access to farmer PII (NIN, GPS coordinates, mobile money number, photo) shall be restricted to authorised Procurement and Finance roles only. | BG-002 | — | TC-FAR-009 |

## 1.4 Phase 4 — Production and Quality

### Module MFG: Manufacturing and Production (F-011)

| FR ID | Requirement Summary | Business Goal | Business Rule | Test Case ID |
|---|---|---|---|---|
| FR-MFG-001 | The system shall manage recipes (Bills of Materials) with version control for all Tooke products and all circular economy by-products. | BG-004, BG-001 | — | TC-MFG-001 |
| FR-MFG-002 | The system shall define circular economy recipes: banana peel → biogas (calorific value output); waste water → bio-slurry fertiliser (kg output). | BG-004 | — | TC-MFG-002 |
| FR-MFG-003 | The system shall enforce mass balance verification: Total Input (kg) = Primary Product Output (kg) + By-product Output (kg) + Scrap/Waste (kg), within a configurable tolerance of ±2%. A production order that fails mass balance cannot be closed. | BG-004 | BR-008 | TC-MFG-003 |
| FR-MFG-004 | The system shall manage production order lifecycle: plan → materials reserved → in progress → QC check → completed → closed. | BG-001 | — | TC-MFG-004 |
| FR-MFG-005 | The system shall block the transfer of finished goods from a production order to saleable inventory until the QC module sets the batch quality status to "Approved" and issues a CoA. | BG-001, BG-004 | BR-004 | TC-MFG-005 |
| FR-MFG-006 | The system shall post WIP entries on material requisition: DR WIP / CR Raw Material Inventory. | BG-002 | — | TC-MFG-006 |
| FR-MFG-007 | The system shall record actual yield versus recipe yield and generate a variance report per production order. | BG-004 | — | TC-MFG-007 |
| FR-MFG-008 | The system shall calculate production cost: raw materials (FIFO cost) + direct labour + absorbed overhead. | BG-002, BG-004 | — | TC-MFG-008 |
| FR-MFG-009 | The Factory Floor App (Android) shall support active order monitoring, worker attendance recording, production completion entry, and QC result submission. | BG-001 | DC-005 | TC-MFG-009 |
| FR-MFG-010 | The system shall generate a mass balance variance report when the ±2% tolerance is exceeded, for review by the Production Supervisor. | BG-004 | BR-008 | TC-MFG-010 |

### Module QC: Quality Control and Laboratory (F-012)

| FR ID | Requirement Summary | Business Goal | Business Rule | Test Case ID |
|---|---|---|---|---|
| FR-QC-001 | The system shall support configurable inspection templates with parameter types: numeric, pass/fail, text, and photo. | BG-001, BG-005 | — | TC-QC-001 |
| FR-QC-002 | The system shall grade incoming matooke batches as A, B, or C, with grade-linked unit prices applied in farmer procurement. | BG-004 | — | TC-QC-002 |
| FR-QC-003 | The system shall support in-process QC checkpoints embedded within production job cards. | BG-001, BG-004 | — | TC-QC-003 |
| FR-QC-004 | The system shall generate a Certificate of Analysis (CoA) for every approved finished product batch. | BG-004, BG-001 | BR-004 | TC-QC-004 |
| FR-QC-005 | The system shall generate export-grade CoAs formatted for South Korea, EU (Italy), Saudi Arabia, Qatar, and the United States markets, with destination-specific QC parameters. | BG-004 | BR-017 | TC-QC-005 |
| FR-QC-006 | The system shall block dispatch of a batch marked "Approved for Domestic" on an export order until an export-grade CoA with the appropriate market-specific parameters is generated. | BG-004 | BR-017 | TC-QC-006 |
| FR-QC-007 | The system shall generate Statistical Process Control (SPC) charts: X-bar and R-charts, Cp and Cpk capability indices. | BG-004 | — | TC-QC-007 |
| FR-QC-008 | The system shall manage Non-Conformance Reports (NCRs) with root cause analysis and corrective action tracking. | BG-004 | — | TC-QC-008 |
| FR-QC-009 | The system shall track batch quality status through states: pending / under test / approved / rejected / on hold. | BG-001 | BR-004 | TC-QC-009 |
| FR-QC-010 | The system shall track lab equipment with calibration certificate records and alert when calibration is due. | BG-001 | — | TC-QC-010 |

## 1.5 Phase 5 — People

### Module HR: Human Resources (F-013)

| FR ID | Requirement Summary | Business Goal | Business Rule | Test Case ID |
|---|---|---|---|---|
| FR-HR-001 | The system shall manage the full employee lifecycle from hire to exit, including NIN, contract type, department, and job grade. | BG-001 | — | TC-HR-001 |
| FR-HR-002 | The system shall support government pay scales (PIBID) and commercial pay scales (BIRDC) simultaneously. | BG-002, BG-005 | — | TC-HR-002 |
| FR-HR-003 | The system shall import attendance records directly from ZKTeco biometric devices; imported records shall be treated as authoritative. [CONTEXT-GAP: GAP-005] | BG-001 | BR-016 | TC-HR-003 |
| FR-HR-004 | The system shall require Finance Manager approval for any manual override to a biometric attendance record and log the override with reason in the audit trail. | BG-002 | BR-016 | TC-HR-004 |
| FR-HR-005 | The system shall manage leave types: annual, sick, maternity, paternity, compassionate, study, and unpaid leave. | BG-001 | — | TC-HR-005 |
| FR-HR-006 | The system shall manage the factory worker registry: skill matrix, daily attendance, productivity metrics, and production order assignment. | BG-001, BG-004 | — | TC-HR-006 |
| FR-HR-007 | The system shall manage staff loans and advances with automatic payroll deduction. | BG-002 | — | TC-HR-007 |
| FR-HR-008 | The system shall manage disciplinary records and exit clearance checklists. | BG-001 | — | TC-HR-008 |
| FR-HR-009 | The HR Self-Service App (Android) shall allow all staff to apply for leave, view payslips, check leave balance, and view attendance records. | BG-001 | DC-001 | TC-HR-009 |

### Module PAY: Payroll (F-014)

| FR ID | Requirement Summary | Business Goal | Business Rule | Test Case ID |
|---|---|---|---|---|
| FR-PAY-001 | The system shall support configurable payroll elements (any number of earnings and deductions) with no hardcoded elements. | BG-005 | DC-002 | TC-PAY-001 |
| FR-PAY-002 | The system shall calculate Uganda PAYE using configurable tax bands updatable by the Finance Director via the UI without developer involvement. | BG-002, BG-005 | DC-002 | TC-PAY-002 |
| FR-PAY-003 | The system shall calculate NSSF contributions: employer 10% and employee 5% of gross salary. | BG-002 | — | TC-PAY-003 |
| FR-PAY-004 | The system shall generate the NSSF remittance schedule in the exact format required by NSSF Uganda. [CONTEXT-GAP: GAP-009] | BG-002 | — | TC-PAY-004 |
| FR-PAY-005 | The system shall calculate Local Service Tax (LST) per local government ordinance, configurable per local government (Bushenyi, Kampala). | BG-002, BG-005 | DC-002 | TC-PAY-005 |
| FR-PAY-006 | The system shall run batch gross-to-net payroll computation for all employees in a single payroll run. | BG-002 | — | TC-PAY-006 |
| FR-PAY-007 | Once the Finance Manager approves and locks a payroll run, the run shall be permanently immutable; errors shall be corrected via adjustment runs in the next period only. | BG-002 | BR-010 | TC-PAY-007 |
| FR-PAY-008 | The system shall generate payslips in PDF format deliverable by email and WhatsApp. | BG-001 | — | TC-PAY-008 |
| FR-PAY-009 | The system shall post payroll GL entries automatically on approval. | BG-002 | — | TC-PAY-009 |
| FR-PAY-010 | The system shall generate a bulk bank credit transfer file in Uganda bank format for salary payments. [CONTEXT-GAP: GAP-006] | BG-002 | — | TC-PAY-010 |
| FR-PAY-011 | The system shall generate bulk mobile money salary payment files for casual workers via MTN MoMo / Airtel Money batch API. | BG-002 | — | TC-PAY-011 |

## 1.6 Phase 6 — Research, Administration, and Compliance

### Module RES: Research and Development (F-015)

| FR ID | Requirement Summary | Business Goal | Business Rule | Test Case ID |
|---|---|---|---|---|
| FR-RES-001 | The system shall maintain a banana variety performance database: cultivar name, processing yield, quality score, and regional suitability. | BG-004, BG-001 | — | TC-RES-001 |
| FR-RES-002 | The system shall manage field trials: plot assignment, intervention tracking, harvest data, and yield analysis. | BG-004 | — | TC-RES-002 |
| FR-RES-003 | The system shall maintain a product development register: new product ideas, pilot batch records, and market testing results. | BG-001, BG-004 | — | TC-RES-003 |
| FR-RES-004 | The system shall track technology transfer records: external research partnerships, licensing, and IP documentation. | BG-001 | — | TC-RES-004 |
| FR-RES-005 | The system shall track R&D expenditure linked to the GL. | BG-002 | — | TC-RES-005 |

### Module ADM: Administration and PPDA Compliance (F-016)

| FR ID | Requirement Summary | Business Goal | Business Rule | Test Case ID |
|---|---|---|---|---|
| FR-ADM-001 | The system shall manage PPDA procurement documentation for all required document types per procurement category. | BG-001, BG-005 | BR-005 | TC-ADM-001 |
| FR-ADM-002 | The system shall maintain a PPDA procurement register with every transaction classified by category and document completion status. | BG-001, BG-005 | BR-005 | TC-ADM-002 |
| FR-ADM-003 | The system shall export the PPDA procurement register in a format suitable for parliamentary review. | BG-005 | — | TC-ADM-003 |
| FR-ADM-004 | The system shall maintain an asset register: acquisition date, cost, location, condition, and depreciation for all BIRDC assets. | BG-002, BG-001 | — | TC-ADM-004 |
| FR-ADM-005 | The system shall manage vehicle and equipment logbooks. | BG-001 | — | TC-ADM-005 |
| FR-ADM-006 | The system shall provide centralised document management with version control, access control, and audit trail. | BG-002, BG-001 | DC-003 | TC-ADM-006 |

### Module SYS: System Administration and IT (F-017)

| FR ID | Requirement Summary | Business Goal | Business Rule | Test Case ID |
|---|---|---|---|---|
| FR-SYS-001 | The system shall manage user accounts with an 8-layer authorisation model: Role → Page → API endpoint → UI element → Location → Time → Conditional rules → Object ownership. | BG-002, BG-001 | BR-003 | TC-SYS-001 |
| FR-SYS-002 | The system shall enforce segregation of duties at the API layer for all controlled transactions; UI-only enforcement is insufficient. | BG-002 | BR-003 | TC-SYS-002 |
| FR-SYS-003 | The system shall provide a searchable audit trail across all modules by user, action, date range, and table, with results returned within ≤ 5 seconds for any 30-day period. | BG-002, BG-001 | DC-003 | TC-SYS-003 |
| FR-SYS-004 | The system shall enforce 7-year retention of all financial records; automated deletion of records within the retention period shall be blocked. | BG-002 | DC-003 | TC-SYS-004 |
| FR-SYS-005 | The system shall complete automated database backup within ≤ 4 hours (full backup), scheduled daily. | BG-002 | DC-006 | TC-SYS-005 |
| FR-SYS-006 | The system shall store all BIRDC data on BIRDC's own servers in Uganda; no data shall reside on external SaaS vendor infrastructure. | BG-002 | DC-006 | TC-SYS-006 |
| FR-SYS-007 | The IT Administrator shall be able to configure EFRIS API credentials, mobile money API keys, email SMTP settings, and biometric device connectivity via the UI without developer involvement. | BG-005, BG-001 | DC-002 | TC-SYS-007 |
| FR-SYS-008 | The system shall support report scheduling: define reports to auto-generate and email on a configurable schedule. | BG-001 | — | TC-SYS-008 |
| FR-SYS-009 | The system shall display a system health dashboard showing server resources, database performance, and active sessions. | BG-001 | — | TC-SYS-009 |

## 1.7 Phase 7 — Integration, Hardening, and Go-Live

### Module EFR: EFRIS Full Integration (F-018)

| FR ID | Requirement Summary | Business Goal | Business Rule | Test Case ID |
|---|---|---|---|---|
| FR-EFR-001 | The system shall wire URA EFRIS system-to-system API across all transaction types: sales invoices, credit notes, and POS receipts. [CONTEXT-GAP: GAP-001] | BG-002, BG-001 | — | TC-EFR-001 |
| FR-EFR-002 | The system shall print the FDN and QR code on every commercial document (invoice, credit note, POS receipt). | BG-002 | — | TC-EFR-002 |
| FR-EFR-003 | The system shall manage a failed EFRIS submission retry queue and alert the Finance Manager when a submission fails. | BG-002 | — | TC-EFR-003 |
| FR-EFR-004 | The system shall maintain a tamper-evident EFRIS audit log for all submission attempts (success and failure). | BG-002 | BR-013 | TC-EFR-004 |

### Module SEC: Security Hardening and Acceptance (F-019)

| FR ID | Requirement Summary | Business Goal | Business Rule | Test Case ID |
|---|---|---|---|---|
| FR-SEC-001 | The system shall pass OWASP Top 10 remediation review before go-live. | BG-002, BG-001 | — | TC-SEC-001 |
| FR-SEC-002 | The system shall pass a penetration test with no critical or high severity findings before go-live. | BG-002 | — | TC-SEC-002 |
| FR-SEC-003 | The system shall sustain 50 concurrent web users without performance degradation; response time for standard pages shall not exceed the defined P95 thresholds. | BG-001 | — | TC-SEC-003 |
| FR-SEC-004 | The system shall pass a full regression test across all 17 modules before go-live. | BG-001 | — | TC-SEC-004 |
| FR-SEC-005 | The system shall pass a load test simulating 140 MT/day peak production scenario. | BG-001, BG-004 | — | TC-SEC-005 |
| FR-SEC-006 | All staff shall complete defined training modules before production go-live. | BG-001 | DC-001 | TC-SEC-006 |
| FR-SEC-007 | The system shall execute and document a go-live cutover plan with a verified rollback procedure. | BG-001 | — | TC-SEC-007 |

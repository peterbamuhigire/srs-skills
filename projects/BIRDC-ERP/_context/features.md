# Feature Register — BIRDC ERP

All 17 modules across 7 delivery phases, plus 6 Android mobile apps.

---

## Phase 1 — Commerce Foundation

### F-001: Sales & Distribution
Complete order-to-cash cycle for Tooke products. Invoice management with lifecycle (draft → pending EFRIS → issued → partially paid → paid → void). GL auto-posting on invoice confirmation (DR AR / CR Revenue + DR COGS / CR Inventory). EFRIS real-time submission to URA via system-to-system API. Territory-based sales tracking. Pricing and multiple price lists (wholesale, retail, export, institutional). Credit management with credit limit enforcement. Void and credit note workflow. Daily sales summary push notification to Director and Sales Manager.

### F-002: Point of Sale (POS)
Three POS contexts: factory gate / showroom, distribution centre, agent checkout. Product search by name, code, or barcode scan. Multi-payment per transaction (cash, MTN MoMo, Airtel Money, cheque, bank deposit). POS session management: opening float, end-of-shift reconciliation, variance reporting. Receipt generation: 80mm thermal receipt, A4 invoice, SMS/WhatsApp digital receipt. Offline POS — transactions stored locally and synced on reconnect. Agent POS uses agent's virtual inventory store, not warehouse stock.
**Mobile [ANDROID]:** Sales Agent App — offline POS, agent stock, remittance submission, commission statements. Bluetooth 80mm thermal receipt printing.

### F-003: Inventory & Warehouse Management
Multi-location warehousing (unlimited locations). Dual-track inventory: warehouse stock (tbl_stock_balance) and agent field stock (tbl_agent_stock_balance) — completely separate ledgers, never merged in reports. Stock item catalogue with UOM conversion engine. Batch and lot tracking with manufacturing date and expiry date. FEFO enforcement (First Expiry First Out) for all expiry-tracked products. Expiry alerts (30, 60, 90-day configurable thresholds). Stock transfers with in-transit status. Physical stock count workflow (freeze → count → variance → approval). Stock adjustments with GL auto-post. FIFO/moving average stock valuation.
**Mobile [ANDROID]:** Warehouse App — barcode scan for stock receipt, transfer confirmation, physical count.

### F-004: Agent Distribution Management
Agent registration with virtual inventory store, territory assignment, stock float limit, commission rate. Agent cash balance (live liability register) = sum of all sales - sum of all verified remittances. FIFO remittance allocation via stored procedure sp_apply_remittance_to_invoices. Remittance verification with segregation of duties (creator ≠ verifier). Commission calculation on verified sales. Agent stock float limit enforcement on issuance. Agent stock return workflow. Agent performance reports: territory ranking, agent ranking, outstanding balances.

---

## Phase 2 — Financial Core

### F-005: Financial Accounting & General Ledger
IFRS for SMEs double-entry accounting. Chart of accounts: hierarchical (parent-child), 1,307 accounts configured. Dual-mode accounting: PIBID parliamentary budget votes + BIRDC commercial IFRS simultaneously. Journal entry management: balanced debit/credit validation, sequential JE numbering (JE-YYYY-NNNN), draft → approved → posted lifecycle. GL auto-posting from all 17 modules — no manual journal entries for operational transactions. Hash chain integrity verification: cryptographic hash chain on every GL entry; tampering mathematically detectable. Financial statements on demand: P&L, Balance Sheet, Cash Flow (IAS 7), Trial Balance. Accounting period management: fiscal year July–June (PIBID) and/or January–December (commercial). Multi-currency: UGX functional, USD/EUR/KES for export.

### F-006: Accounts Receivable
Customer and agent AR tracking. AR aging (current, 30, 60, 90, 120+ days). Agent receivable tracking: agent balance = invoices issued to agent's customers on credit - verified remittances. Agent remittance system (see F-004). Customer credit control with credit hold workflow. Customer statements. Payment receipts: bank transfer, mobile money, cheque. Auto-allocation to oldest invoice.
**Mobile [ANDROID]:** Executive Dashboard App — P&L snapshot, Trial Balance summary, cash position, budget variance alerts.

### F-007: Accounts Payable
Vendor invoice registration with three-way matching (PO → GRN → Invoice). AP aging. Vendor payments (bank transfer, mobile money, cheque). Farmer payment system: aggregate contributions per period, apply deductions (loan repayments, cooperative levies), generate net payment per farmer, bulk MTN MoMo/Airtel Money payment file. Payment scheduling with cash position check. Withholding tax (6% on applicable local service suppliers per Uganda Income Tax Act). URA WHT certificate generation.

### F-008: Budget Management
PIBID parliamentary budget votes by department and vote code. BIRDC commercial budgets by account and cost centre. Both modes in same system. Budget vs. actual variance tracking on demand. Budget alerts when spending approaches threshold. Budget period management aligned to parliamentary financial year (July–June).

---

## Phase 3 — Supply Chain & Farmers

### F-009: Procurement & Purchasing
**Standard Supplier Procurement:** Purchase requests with PPDA approval workflow (micro / small / large / restricted thresholds). RFQ to multiple suppliers with side-by-side comparison. Local Purchase Orders (LPO — Uganda standard format). GRN with three-way matching. Vendor management with performance rating and document attachments. Landed cost allocation for imported inputs.
**5-Stage Cooperative Farmer Procurement:** Stage 1 — Bulk PO per cooperative/season. Stage 2 — Batch goods receipt at factory gate. Stage 3 — Individual farmer contribution breakdown (name, NIN, weight, quality grade, net payable). Stage 4 — Stock receipt into factory inventory with batch numbers. Stage 5 — GL posting (DR Raw Material Inventory / CR Cooperative Payable per cooperative).
**Mobile [ANDROID]:** Farmer Delivery App — register new farmers offline, GPS farm profiling, record individual deliveries (Bluetooth scale integration), print farmer receipt.

### F-010: Farmer & Cooperative Management
Farmer registration: name, NIN, contact, cooperative, GPS coordinates, mobile money number, photo. Farm profiling: multiple farms per farmer, size, GPS polygon, banana varieties, livestock, infrastructure. Banana variety tracking by cultivar. Farmer contribution history: full delivery record with quality grades, deductions, and net payments. Cooperative organisation: farmers → cooperatives → zones → BIRDC network. Extension services: training attendance, input loan issuance and repayment, extension officer visit log. Farmer performance ranking. Bulk payment with SMS payment confirmation.

---

## Phase 4 — Production & Quality

### F-011: Manufacturing & Production
Recipe / Bill of Materials with version control. Circular economy recipes: banana peel → biogas (calorific value output), waste water → bio-slurry fertiliser (kg output). Mass balance verification: primary products + by-products + scrap = 100% of input (BR-008). Production orders: plan → materials reserved → in progress → QC check → completed → closed. Material requisition with WIP accounting (DR WIP / CR Raw Material Inventory). Production completion recording with actual yield vs. recipe yield variance. Job cards with worker assignment and step-by-step instructions. Equipment and capacity management. Production costing: raw materials (FIFO cost) + direct labour + absorbed overhead. QC gate: stock transfer blocked until QC approves (BR-004).
**Mobile [ANDROID]:** Factory Floor App — monitor active orders, record worker attendance, enter production completion quantities, submit QC results.

### F-012: Quality Control & Laboratory
Configurable inspection templates (numeric, pass/fail, text, photo parameters). Incoming material inspection with quality grading (A, B, C — different price tiers for procurement). In-process QC checkpoints within job cards. Finished product certification and Certificate of Analysis (CoA) generation. Export-grade CoA formatted for South Korea, EU, Saudi Arabia markets. Statistical Process Control (SPC): X-bar and R-charts, Cp and Cpk capability indices. Non-conformance Reports (NCR) with root cause analysis and corrective action tracking. Batch quality status (pending / under test / approved / rejected / on hold). Lab equipment management with calibration certificate tracking. Incubation and maturation tracking for fermented products.

---

## Phase 5 — People

### F-013: Human Resources
Employee lifecycle: hire to exit. Employee profile with NIN, contract type, department, job grade. Government pay scales (PIBID) and commercial pay scales (BIRDC). Attendance: manual entry + ZKTeco biometric fingerprint device integration (direct import, no re-entry). Leave management: annual, sick, maternity, paternity, compassionate, study, unpaid. Factory worker registry: skill matrix, daily attendance, productivity metrics, production order assignment. Staff loans and advances with automatic payroll deduction. Disciplinary records. Exit clearance checklist.
**Mobile [ANDROID]:** HR Self-Service App — apply for leave, view payslips, check leave balance, view attendance.

### F-014: Payroll
Configurable payroll elements (any number of earnings and deductions — no hardcoded elements). Uganda PAYE with configurable tax bands (Finance Director updates when URA publishes new bands — no developer needed). Uganda NSSF: employer 10% / employee 5% — NSSF remittance schedule in exact NSSF Uganda format. LST (Local Service Tax) configurable per local government ordinance (Bushenyi, Kampala). Payroll run: batch gross-to-net per employee. Payroll lock on Finance Manager approval (BR-010). Payslip PDF by email or WhatsApp. Payroll GL auto-posting on approval. Bank transfer bulk credit file (Uganda bank format). Bulk mobile money salary payment (casual workers) via MTN MoMo / Airtel Money batch API.

---

## Phase 6 — Research, Administration & Compliance

### F-015: Research & Development
Banana variety performance database: cultivar name, processing yield, quality score, regional suitability. Field trial management: plot assignment, intervention tracking, harvest data, yield analysis. Product development register: new product ideas, pilot batch records, market testing results. Technology transfer records: external research partnerships, licensing, IP documentation. R&D expenditure tracking linked to GL.

### F-016: Administration & PPDA Compliance
PPDA procurement documentation management: all required documents per procurement category (request, quotation, evaluation, LPO, GRN, invoice, payment). Procurement register: every procurement transaction with PPDA category classification and document status. Asset register: all BIRDC assets with acquisition date, cost, location, condition, depreciation. Vehicle and equipment logbook. Document management: centralised document store with version control, access control, and audit trail.

### F-017: System Administration / IT
User management: create, edit, deactivate accounts. Role and permission matrix: 8-layer authorisation (Role → Page → API endpoint → UI element → Location → Time → Conditional rules → Object ownership). Audit log review: complete system-wide audit trail searchable by user, action, date, table. Backup management: automated database backup scheduling with retention policy. Integration configuration: EFRIS API credentials, mobile money API keys, email SMTP settings, biometric device connectivity. Report scheduling: define reports to auto-generate and email on schedule. System health dashboard: server resources, database performance, active sessions.

---

## Phase 7 — Integration, Hardening & Go-Live

### F-018: EFRIS Full Integration
URA EFRIS system-to-system API fully wired across all transaction types: sales invoices, credit notes, POS receipts. Fiscal Document Number (FDN) and QR code printed on every commercial document. Failed submission retry queue with alert to Finance Manager. EFRIS audit log with tamper-evident records.

### F-019: Security Hardening & Acceptance
OWASP Top 10 remediation. Penetration test. Load testing (140 MT/day peak production scenario). Full regression across all 17 modules. Staff training delivery. Go-live cutover plan.

---

## Phase 7 — AI Intelligence (Contract Extension)

### F-018: AI Intelligence Module

Phase 7 contract extension. Requires Phases 1–4 fully operational with at least 12 months of production and quality data before activation.

- Production yield prediction: forecast output tonnage per production order from raw material quality grade distribution (A/B/C) before production begins; alerts when predicted yield deviates from committed output by > 5%
- Quality defect pattern detection: Shewhart control chart monitoring across consecutive batches; alert dispatched when Western Electric Rule 1 or Rule 2 is triggered for any quality parameter
- Farmer supply forecasting: quarterly delivery volume forecast per cooperative from 3-year seasonal history and optional Open-Meteo rainfall adjustment
- Predictive equipment maintenance: weekly scan of accumulated runtime hours and service history; Maintenance Proximity Score alert when asset reaches 80% of average service interval
- Export demand intelligence: production feasibility check on new export order entry, identifying capacity gaps 8 weeks in advance

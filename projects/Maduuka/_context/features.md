# Feature Register -- Maduuka

## Phase 1 Core Modules (Android + Web)

### F-001: Point of Sale (POS)
Product search by name/barcode/SKU/camera scan. Product grid view with category filters. Cart management (add, quantity, per-item discount, order discount, remove). Multi-payment per sale (cash + MTN MoMo + Airtel Money + credit in one transaction). Cash change calculation. Mobile money push payment. Credit sales with limit enforcement. Hold and resume cart. Receipt: 80mm thermal (Bluetooth/USB), A4 PDF invoice, digital via SMS/WhatsApp. Barcode scanning via ML Kit (Android). POS session management (shift open/close, reconciliation). Void and refund with reason code and audit trail. Offline sales with queue and sync. Receipt gap detection. Weight-based and service items. Full-screen POS mode on mobile.

### F-002: Inventory and Stock Management
Product catalogue (SKU, barcode, category, UOM, cost price, multi-tier selling prices, photos, reorder level). Multiple price tiers (retail, wholesale, distributor). Multiple selling units with UOM conversion. Stock levels per branch/warehouse. Immutable stock movement records. Stock adjustments with manager approval above threshold. Stock transfers between locations (in-transit status). Reorder alerts. Batch/lot tracking with expiry dates. FIFO/FEFO enforcement. Expiry alerts (configurable: 30/60/90 days). Stock valuation (FIFO or weighted average). Physical stock count workflow (freeze, count, variance, approval). Supplier returns. Customer returns.

### F-003: Customer Management
Customer profiles (name, phone, email, district/sub-county, group, credit limit). Customer groups (retail, wholesale, VIP, staff) with group pricing. Credit accounts with real-time balance tracking. Credit limit enforcement at POS with manager override. Payment collection against credit balances. Debtors ageing report. Customer statement generation. Full transaction history per customer. Customer location map (Leaflet.js on web). Magic-link customer portal via WhatsApp/SMS (read-only: purchase history, balances, invoices -- no login required).

### F-004: Supplier and Vendor Management
Supplier directory (contact, payment terms, bank details). Purchase history per supplier. Supplier balance tracking on unpaid invoices. Supplier payments (full/partial, multi-method). Supplier statements. Purchase order creation with PDF export. Goods receiving against PO (partial receipts supported). Three-way matching (PO vs receipt vs invoice). Supplier delivery performance tracking.

### F-005: Expenses and Petty Cash
Custom expense categories (unlimited). Expense recording (amount, date, category, payment method, receipt photo attachment). Receipt OCR on mobile (auto-extract amount and vendor). Expense approval workflow above configurable threshold. Petty cash float management. Recurring expense reminders. Expense reports by category/period/method. Tax deductibility flag. GL posting on approval.

### F-006: Financial Accounts and Cash Flow
Payment account definitions (cash till, MTN MoMo, Airtel Money, bank, SACCO). Real-time account balances. Cash transfers between accounts. Deposits and withdrawals. Account transaction log. Bank reconciliation. Cash flow summary (inflows vs outflows by account and period). Daily summary. Bank statement CSV import (web). Multi-account dashboard.

### F-007: Sales Reporting and Analytics
Daily sales report. Sales summary (revenue, collected, outstanding credit, transaction count). Sales by product, category, branch, customer, cashier. Sales trends and charts. Top sellers. Gross margin analysis. Voids and refunds report. Receipt gap report. All reports: CSV export, PDF export, print. Schedule reports (auto-email daily/weekly). Custom report builder (web).

### F-008: HR and Payroll
Staff profiles (personal details, NIN, emergency contacts, hire date, department, job title, branch, employment type). Contract management with renewal reminders. Leave management (define types, day entitlements, staff application via app, manager approval). Attendance (manual or clock-in/out via phone with location for field staff). Salary structure (earnings + deductions). Monthly payroll computation and approval. Payslip PDF via WhatsApp or email. Bank payment file per Uganda bank format (Centenary, Stanbic, ABSA, KCB, Equity, Dfcu). MTN MoMo / Airtel Money bulk salary payment. NSSF Uganda (employer 10%, employee 5%). PAYE Uganda (per Income Tax Act). LST (configurable per local government). Staff loans/advances with auto-deduction. Disciplinary records. Staff ID card generation.

### F-009: Dashboard and Business Health
Real-time KPI cards (Today's Revenue, Transaction Count, Outstanding Credit, Cash Position). Revenue comparison (today vs yesterday, this week vs last week). Recent transactions list. Low stock alert. Pending approvals (expenses, leave, stock adjustments). Branch switcher. POS session status. Business health score (RAG: gross margin %, expense ratio, stock turnover, collection rate). Quick action shortcuts. Android home screen widget (optional). Web: customisable dashboard widgets, auto-refresh every 2 minutes.

### F-010: Settings and Configuration
Business profile (name, logo, address, TIN). Receipt customisation (header, footer, logo, fields). Tax settings (VAT 18% Uganda, zero-rated, exempt; tax-inclusive/exclusive toggle per category). Currency (any world currency, no hardcoded symbols). Language (English, Swahili per user). Date/number format. Financial year start month (July default for Uganda). Payment account management. Email SMTP settings. SMS gateway (Africa's Talking). Notification preferences per role. Subscription management (view plan, upgrade, downgrade, cancel). 2FA (TOTP) for owner. Connected devices with revoke access. Full data export (CSV). Account deletion with data export.

## Phase 2 Add-on Modules (iOS parity + industry add-ons)

### F-011: Restaurant / Bar Module
Table management (define areas and tables, real-time status: Available/Occupied/Reserved/Cleaning). Multiple serving areas. Table reservations. Order types (Dine-In, Takeaway, Delivery). Waiter assignment. Kitchen Order Tickets (KOT) with table, server, items, instructions, timestamp. Multiple KOTs per order. Kitchen Display System (auto-refresh, colour-coded urgency). Kitchen thermal printer support. Bar tabs (open, add rounds, settle). Bill generation from KOTs. Split billing. Service charge and cover charge. Same payment modes as core POS. Table freed on full payment. Server management and performance reporting. Bill of materials (ingredient recipes auto-deduct stock on KOT send). Floor plan designer (web drag-and-drop).

### F-012: Pharmacy / Drug Store Module
Patient profiles (demographics, allergies, blood group, insurance). Prescription management (doctor, facility, date, medications, dosage, duration, photo/scan attachment). Prescription status tracking (new, partially filled, fully filled, expired). Prescription-linked dispensing. Specialised pharmacy POS (generic/brand search, FEFO batch selection, dispensing units). Allergy alert at point of dispensing. Drug interaction check (basic category-level warnings + disclaimer -- NOT a clinical decision support system). Drug reference database (generic names, brand names, drug class, dosage, controlled classification, storage requirements). Dispensing labels. Batch and expiry management (FEFO enforced). Near-expiry alerts. Cold chain temperature logging. Controlled drugs register (NDA Uganda compliance). NDA compliance audit log export. Insurance billing with claim tracking. Refill reminders via SMS/WhatsApp.

## Phase 3 Add-on Modules

### F-013: Hotel / Accommodation Module
Covers: hotels, lodges, guesthouses, serviced apartments, Airbnb operators, conference centres, and camps. Property setup (room types, individual rooms with floor/type/capacity/status). Room status board (Available/Occupied/Reserved/Cleaning/Maintenance/Out of Order). Reservations (walk-in and phone booking, calendar view). Check-in (against reservation or walk-in, ID document, deposit, room key). Group bookings. Check-out with full bill settlement. Early/late check-out handling.

**Dual billing mode (Uganda market requirement):** Room types support both nightly rates (standard hotels) and hourly rates (guesthouses, lodges, short-stay). Billing mode selected at check-in: hourly billing calculates Charge = Hours Occupied x Hourly Rate (rounded up to the next whole hour); nightly billing calculates Charge = Nights x Nightly Rate. Both modes support posting of additional charges (F&B, laundry, conference) to the room account (BR-016).

Room billing (base accommodation + extras from F&B, laundry, conference). Restaurant/bar charge posting to room. Housekeeping task management. Maintenance flagging. Corporate accounts. Conference room booking. Laundry charge management. Seasonal pricing. Occupancy analytics (RevPAR, ADR, length of stay). Hotel reports.

### F-014: Advanced Inventory Module
Multi-warehouse management (unlimited warehouses per branch). Serial number tracking (individual serialised items, full history). Batch traceability (trace from purchase to sale, product recall). Landed cost allocation (freight, duty, insurance, clearing costs distributed across items). Bill of materials + production orders (finished goods from raw materials). Yield management. Complex UOM conversion matrix. Cross-warehouse stock availability. Demand forecasting (days of stock remaining, reorder quantity recommendation). Compliance audit report (high-value, after-hours, unusual patterns). Profitability by batch.

## Phase 3 Compliance Add-on

### F-015: EFRIS Compliance Module (Uganda)
System-to-system URA EFRIS API integration. Encrypted transmission per URA specifications. Fiscal Document Number (FDN) from URA on every invoice. URA QR code on receipts. Product catalogue synchronisation to URA standard catalogue. EFRIS-compliant credit and debit notes. B2B, B2C, B2G transaction types. Offline queuing when URA server unavailable. EFRIS status dashboard. Monthly reconciliation report.

## AI Business Intelligence Module (Add-On)

**Tier:** Starter and above | **Phase:** Future add-on (off by default)

- Sales forecasting: predict today's and next 7 days' revenue based on historical patterns and day-of-week seasonality, computed nightly at 06:00 EAT
- Smart Reorder Advisor: Sunday morning buy-list recommending exact purchase quantities per product to avoid over-stocking and stockouts, shareable via WhatsApp native share
- Fraud and anomaly alerts: nightly scan flagging suspicious void ratios, refunds without matching sales, after-hours transactions, and round-number cash sale patterns
- Business Health Advisor: Monday 08:00 EAT push notification — plain-English weekly business summary (revenue trend, top seller, inventory watch, one recommended action) generated via Claude API

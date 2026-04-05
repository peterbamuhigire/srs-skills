# Maduuka SRS Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Scaffold the Maduuka project, populate all `_context/` files from the spec, and generate the full Phase 1 SRS documentation suite (Android + Web, 10 core modules).

**Architecture:** Hybrid Water-Scrum-Fall methodology. Phase 1 SRS covers Android + Web platform, all 10 core modules. Phase 2 and 3 SRS documents are planned separately after Phase 1 sign-off. Domain: Retail (primary) + Healthcare (pharmacy module sections, Phase 2) + Hospitality (restaurant/hotel, Phase 2/3).

**Tech Stack:** PHP 8.3+ (web), Kotlin/Compose (Android), REST API, MySQL, JWT/Session auth, offline-first (Room/PWA), MTN MoMo + Airtel Money, Pandoc for `.docx` build.

**Spec source:** `C:\Users\Peter\Downloads\maduuka_spec.docx`
**Design doc:** `docs/plans/2026-04-05-maduuka-design.md`

---

## Task 1: Scaffold Project Directory Structure

**Files:**
- Create: `projects/Maduuka/`
- Create: `projects/Maduuka/_context/`
- Create: `projects/Maduuka/export/`
- Create: `projects/Maduuka/export/.gitkeep`
- Create all 9 phase directories with document subdirectories (Hybrid methodology — both `01-srs/` and `02-user-stories/` in Phase 02)

**Step 1: Create root and export directory**

```bash
mkdir -p projects/Maduuka/export
touch projects/Maduuka/export/.gitkeep
```

**Step 2: Create `_context/` directory**

```bash
mkdir -p projects/Maduuka/_context
```

**Step 3: Create all phase + document subdirectories**

```bash
# Phase 01 — Strategic Vision
mkdir -p projects/Maduuka/01-strategic-vision/01-prd
mkdir -p projects/Maduuka/01-strategic-vision/02-vision-statement
mkdir -p projects/Maduuka/01-strategic-vision/03-business-case

# Phase 02 — Requirements Engineering (Hybrid: both SRS and user stories)
mkdir -p projects/Maduuka/02-requirements-engineering/01-srs
mkdir -p projects/Maduuka/02-requirements-engineering/02-user-stories
mkdir -p projects/Maduuka/02-requirements-engineering/03-stakeholder-analysis

# Phase 03 — Design Documentation
mkdir -p projects/Maduuka/03-design-documentation/01-hld
mkdir -p projects/Maduuka/03-design-documentation/02-lld
mkdir -p projects/Maduuka/03-design-documentation/03-api-spec
mkdir -p projects/Maduuka/03-design-documentation/04-database-design
mkdir -p projects/Maduuka/03-design-documentation/05-ux-spec

# Phase 04 — Development Artifacts
mkdir -p projects/Maduuka/04-development-artifacts/01-technical-spec
mkdir -p projects/Maduuka/04-development-artifacts/02-coding-guidelines

# Phase 05 — Testing Documentation
mkdir -p projects/Maduuka/05-testing-documentation/01-test-strategy
mkdir -p projects/Maduuka/05-testing-documentation/02-test-plan
mkdir -p projects/Maduuka/05-testing-documentation/03-test-report

# Phase 06 — Deployment & Operations
mkdir -p projects/Maduuka/06-deployment-operations/01-deployment-guide
mkdir -p projects/Maduuka/06-deployment-operations/02-runbook

# Phase 07 — Agile Artifacts
mkdir -p projects/Maduuka/07-agile-artifacts/01-sprint-planning
mkdir -p projects/Maduuka/07-agile-artifacts/02-dod
mkdir -p projects/Maduuka/07-agile-artifacts/03-dor

# Phase 08 — End-User Documentation
mkdir -p projects/Maduuka/08-end-user-documentation/01-user-manual
mkdir -p projects/Maduuka/08-end-user-documentation/02-installation-guide
mkdir -p projects/Maduuka/08-end-user-documentation/03-faq

# Phase 09 — Governance & Compliance
mkdir -p projects/Maduuka/09-governance-compliance/01-traceability-matrix
mkdir -p projects/Maduuka/09-governance-compliance/02-audit-report
mkdir -p projects/Maduuka/09-governance-compliance/03-compliance
mkdir -p projects/Maduuka/09-governance-compliance/04-risk-assessment
```

**Step 4: Create `manifest.md` stub in every document subdirectory**

Create the following content in every document directory listed above:

```markdown
# Document Manifest
# List section files in assembly order, one per line.
# Lines starting with # are comments and are excluded from the build.
# If this file is absent, build-doc.sh sorts *.md files alphabetically.
```

**Step 5: Create export scripts**

Create `projects/Maduuka/export-docs.sh`:

```bash
#!/usr/bin/env bash
# export-docs.sh -- Copy all .docx deliverables into export/
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
EXPORT_DIR="$SCRIPT_DIR/export"
mkdir -p "$EXPORT_DIR"
echo "Project   : $(basename "$SCRIPT_DIR")"
echo "Exporting : $EXPORT_DIR"
echo ""
count=0
while IFS= read -r -d '' f; do
    dest="$EXPORT_DIR/$(basename "$f")"
    if [ -f "$dest" ]; then
        echo "  OVERWRITE: $(basename "$f")"
    else
        echo "  COPY:      $(basename "$f")"
    fi
    cp "$f" "$dest"
    ((count++)) || true
done < <(find "$SCRIPT_DIR" -name "*.docx" -not -path "*/export/*" -print0)
echo ""
echo "Exported $count file(s) to $EXPORT_DIR"
```

Create `projects/Maduuka/export-docs.ps1`:

```powershell
# export-docs.ps1 -- Copy all .docx deliverables into export/
$ScriptDir  = Split-Path -Parent $MyInvocation.MyCommand.Path
$ExportDir  = Join-Path $ScriptDir 'export'
New-Item -ItemType Directory -Force -Path $ExportDir | Out-Null
Write-Host "Project   : $(Split-Path -Leaf $ScriptDir)"
Write-Host "Exporting : $ExportDir"
Write-Host ""
$docxFiles = Get-ChildItem -Path $ScriptDir -Recurse -Filter '*.docx' |
             Where-Object { $_.FullName -notlike "*\export\*" }
$count = 0
foreach ($f in $docxFiles) {
    $dest = Join-Path $ExportDir $f.Name
    if (Test-Path $dest) { Write-Host "  OVERWRITE: $($f.Name)" }
    else                 { Write-Host "  COPY:      $($f.Name)" }
    Copy-Item -Path $f.FullName -Destination $dest -Force
    $count++
}
Write-Host ""
Write-Host "Exported $count file(s) to $ExportDir"
```

**Step 6: Create `projects/Maduuka/README.md`**

```markdown
# Maduuka — SRS Documentation

**Product:** Maduuka — mobile-first SaaS business management, POS, and bookkeeping
**Owner:** Peter Bamuhigire · Chwezi Core Systems · chwezicore.com
**Methodology:** Hybrid (Water-Scrum-Fall)
**Domain:** Retail (primary) + Healthcare (Pharmacy module) + Hospitality (Restaurant/Hotel)
**Phase 1 scope:** Android + Web, all 10 core modules
**Generated by:** SRS-Skills Engine

## Quick Build

```bash
bash scripts/build-doc.sh projects/Maduuka/02-requirements-engineering/01-srs SRS_Phase1
```
```

**Step 7: Create `projects/Maduuka/DOCUMENTATION-STATUS.md`**

```markdown
# Documentation Status — Maduuka

| Document | Directory | Status | Last Updated |
|---|---|---|---|
| PRD | 01-strategic-vision/01-prd/ | Pending | — |
| Vision Statement | 01-strategic-vision/02-vision-statement/ | Pending | — |
| Business Case | 01-strategic-vision/03-business-case/ | Pending | — |
| SRS Phase 1 | 02-requirements-engineering/01-srs/ | Pending | — |
| HLD | 03-design-documentation/01-hld/ | Pending | — |
| API Specification | 03-design-documentation/03-api-spec/ | Pending | — |
| Database Design | 03-design-documentation/04-database-design/ | Pending | — |
| UX Specification | 03-design-documentation/05-ux-spec/ | Pending | — |
| Test Strategy | 05-testing-documentation/01-test-strategy/ | Pending | — |
| Test Plan Phase 1 | 05-testing-documentation/02-test-plan/ | Pending | — |
| Risk Assessment | 09-governance-compliance/04-risk-assessment/ | Pending | — |
| Traceability Matrix | 09-governance-compliance/01-traceability-matrix/ | Pending | — |
```

**Step 8: Verify scaffold**

```bash
find projects/Maduuka -type d | sort
```

Expected: 44+ directories including all phase/document subdirs.

**Step 9: Commit**

```bash
git add projects/Maduuka/
git commit -m "feat(maduuka): scaffold project directory structure"
```

---

## Task 2: Populate `_context/vision.md`

**Files:**
- Create: `projects/Maduuka/_context/vision.md`

**Step 1: Write vision.md from spec and design document**

```markdown
# Project Vision

**Project:** Maduuka
**Owner:** Peter Bamuhigire · Chwezi Core Systems · chwezicore.com · techguypeter.com · +256784464178
**Date:** 2026-04-05

## Problem Statement

Hundreds of thousands of small businesses across Uganda — from a butcher stall in Owino Market to
a multi-branch pharmacy in Kampala — manage their operations using pirated Windows POS software,
exercise books, WhatsApp, or Excel. Pirated software provides no cloud backup, no mobile access,
no updates, and no EFRIS compliance. A single PC crash wipes all records. Maduuka replaces all of
this with a mobile-first SaaS subscription that costs less than a monthly airtime top-up, works on
any Android phone, never loses data, and provides a path to EFRIS compliance.

## Design Covenant (Binding Constraints)

- **Mobile-first, web-equal:** The Android app is the primary product. The web interface is a
  full-featured equal — every feature on web is on mobile and vice versa.
- **Zero mandatory training:** A shopkeeper who can use WhatsApp can use Maduuka. If any screen
  requires a manual, the screen is redesigned.
- **Offline-first, always:** Sales record, stock tracks, and orders place when internet is down.
  All data syncs when connectivity returns. No functionality is blocked by connectivity loss.
- **Works on the cheapest phone:** Maduuka runs on a UGX 250,000 Android phone.
- **Currency-neutral and Africa-ready:** No hardcoded currency symbols. Configurable for any
  African country's currency and language.
- **Compliance built in:** EFRIS integration is an add-on module, but the underlying records
  (accurate sales, real-time inventory, fiscal receipts) are built into every plan.

## Primary Competitor

The primary competitive target is **pirated Windows POS software** — not other legitimate software
companies. Every shopkeeper currently running a pirated Sage, QuickBooks, or Chinese POS on an
ageing PC is Maduuka's customer.

## Goals

1. Acquire 1,000 paying Ugandan business accounts within 12 months of Phase 1 launch.
2. Provide real-time business health visibility on any Android phone — revenue, stock, debtors.
3. Achieve EFRIS compliance coverage for mandated businesses via the Phase 3 add-on module.
4. Expand to all African markets with configurable currency, language, and mobile money gateways.
5. Displace pirated POS software as the dominant solution in Kampala's downtown business district.

## Branding

Chwezi Core Systems product exclusively. No Byoosi.com association. No MLM module — ever.

## Methodology Note

Methodology is Hybrid (Water-Scrum-Fall): formal requirements sign-off per phase, iterative
delivery within phases. This was confirmed by Peter on 2026-04-05. Phase 1 covers Android + Web
with all 10 core modules. Phase 2 adds iOS parity, Restaurant/Bar, and Pharmacy add-ons.
Phase 3 adds Hotel/Accommodation, Advanced Inventory, and EFRIS.

## Stakeholders

See `_context/stakeholders.md` for the full register.

Key groups: Business Owner, Branch Manager, Cashier/POS Operator, Stock Manager, Accountant,
HR Manager, Waiter/Server, Kitchen Staff, Front Desk, Pharmacist, Customer (portal),
Platform Admin (Chwezi), MTN Uganda (MoMo API partner), Airtel Uganda (Airtel Money partner),
URA (EFRIS compliance, Phase 3), NDA Uganda (pharmacy compliance, Phase 2).
```

**Step 2: Verify file exists**

```bash
cat projects/Maduuka/_context/vision.md | head -5
```

Expected: `# Project Vision`

**Step 3: Commit**

```bash
git add projects/Maduuka/_context/vision.md
git commit -m "feat(maduuka): populate _context/vision.md from spec"
```

---

## Task 3: Populate `_context/features.md`

**Files:**
- Create: `projects/Maduuka/_context/features.md`

**Step 1: Write features.md covering all 10 core modules + 4 add-ons**

```markdown
# Feature Register — Maduuka

## Phase 1 Core Modules (Android + Web)

### F-001: Point of Sale (POS)
Product search by name/barcode/SKU/camera scan. Product grid view with category filters.
Cart management (add, quantity, per-item discount, order discount, remove). Multi-payment
per sale (cash + MTN MoMo + Airtel Money + credit in one transaction). Cash change calculation.
Mobile money push payment. Credit sales with limit enforcement. Hold and resume cart.
Receipt: 80mm thermal (Bluetooth/USB), A4 PDF invoice, digital via SMS/WhatsApp. Barcode
scanning via ML Kit (Android). POS session management (shift open/close, reconciliation).
Void and refund with reason code and audit trail. Offline sales with queue and sync.
Receipt gap detection. Weight-based and service items. Full-screen POS mode on mobile.

### F-002: Inventory and Stock Management
Product catalogue (SKU, barcode, category, UOM, cost price, multi-tier selling prices, photos,
reorder level). Multiple price tiers (retail, wholesale, distributor). Multiple selling units
with UOM conversion. Stock levels per branch/warehouse. Immutable stock movement records.
Stock adjustments with manager approval above threshold. Stock transfers between locations
(in-transit status). Reorder alerts. Batch/lot tracking with expiry dates. FIFO/FEFO enforcement.
Expiry alerts (configurable: 30/60/90 days). Stock valuation (FIFO or weighted average).
Physical stock count workflow (freeze, count, variance, approval). Supplier returns. Customer returns.

### F-003: Customer Management
Customer profiles (name, phone, email, district/sub-county, group, credit limit). Customer groups
(retail, wholesale, VIP, staff) with group pricing. Credit accounts with real-time balance tracking.
Credit limit enforcement at POS with manager override. Payment collection against credit balances.
Debtors ageing report. Customer statement generation. Full transaction history per customer.
Customer location map (Leaflet.js on web). Magic-link customer portal via WhatsApp/SMS (read-only:
purchase history, balances, invoices — no login required).

### F-004: Supplier and Vendor Management
Supplier directory (contact, payment terms, bank details). Purchase history per supplier.
Supplier balance tracking on unpaid invoices. Supplier payments (full/partial, multi-method).
Supplier statements. Purchase order creation with PDF export. Goods receiving against PO
(partial receipts supported). Three-way matching (PO vs receipt vs invoice). Supplier delivery
performance tracking.

### F-005: Expenses and Petty Cash
Custom expense categories (unlimited). Expense recording (amount, date, category, payment method,
receipt photo attachment). Receipt OCR on mobile (auto-extract amount and vendor). Expense approval
workflow above configurable threshold. Petty cash float management. Recurring expense reminders.
Expense reports by category/period/method. Tax deductibility flag. GL posting on approval.

### F-006: Financial Accounts and Cash Flow
Payment account definitions (cash till, MTN MoMo, Airtel Money, bank, SACCO). Real-time account
balances. Cash transfers between accounts. Deposits and withdrawals. Account transaction log.
Bank reconciliation. Cash flow summary (inflows vs outflows by account and period). Daily summary.
Bank statement CSV import (web). Multi-account dashboard.

### F-007: Sales Reporting and Analytics
Daily sales report. Sales summary (revenue, collected, outstanding credit, transaction count).
Sales by product, category, branch, customer, cashier. Sales trends and charts. Top sellers.
Gross margin analysis. Voids and refunds report. Receipt gap report. All reports: CSV export,
PDF export, print. Schedule reports (auto-email daily/weekly). Custom report builder (web).

### F-008: HR and Payroll
Staff profiles (personal details, NIN, emergency contacts, hire date, department, job title,
branch, employment type). Contract management with renewal reminders. Leave management (define
types, day entitlements, staff application via app, manager approval). Attendance (manual or
clock-in/out via phone with location for field staff). Salary structure (earnings + deductions).
Monthly payroll computation and approval. Payslip PDF via WhatsApp or email. Bank payment file
per Uganda bank format (Centenary, Stanbic, ABSA, KCB, Equity, Dfcu). MTN MoMo / Airtel Money
bulk salary payment. NSSF Uganda (employer 10%, employee 5%). PAYE Uganda (per Income Tax Act).
LST (configurable per local government). Staff loans/advances with auto-deduction. Disciplinary
records. Staff ID card generation.

### F-009: Dashboard and Business Health
Real-time KPI cards (Today's Revenue, Transaction Count, Outstanding Credit, Cash Position).
Revenue comparison (today vs yesterday, this week vs last week). Recent transactions list.
Low stock alert. Pending approvals (expenses, leave, stock adjustments). Branch switcher.
POS session status. Business health score (RAG: gross margin %, expense ratio, stock turnover,
collection rate). Quick action shortcuts. Android home screen widget (optional). Web:
customisable dashboard widgets, auto-refresh every 2 minutes.

### F-010: Settings and Configuration
Business profile (name, logo, address, TIN). Receipt customisation (header, footer, logo, fields).
Tax settings (VAT 18% Uganda, zero-rated, exempt; tax-inclusive/exclusive toggle per category).
Currency (any world currency, no hardcoded symbols). Language (English, Swahili per user).
Date/number format. Financial year start month (July default for Uganda). Payment account management.
Email SMTP settings. SMS gateway (Africa's Talking). Notification preferences per role.
Subscription management (view plan, upgrade, downgrade, cancel). 2FA (TOTP) for owner.
Connected devices with revoke access. Full data export (CSV). Account deletion with data export.

## Phase 2 Add-on Modules (iOS parity + industry add-ons)

### F-011: Restaurant / Bar Module
Table management (define areas and tables, real-time status: Available/Occupied/Reserved/Cleaning).
Multiple serving areas. Table reservations. Order types (Dine-In, Takeaway, Delivery).
Waiter assignment. Kitchen Order Tickets (KOT) with table, server, items, instructions, timestamp.
Multiple KOTs per order. Kitchen Display System (auto-refresh, colour-coded urgency).
Kitchen thermal printer support. Bar tabs (open, add rounds, settle). Bill generation from KOTs.
Split billing. Service charge and cover charge. Same payment modes as core POS. Table freed on
full payment. Server management and performance reporting. Bill of materials (ingredient recipes
auto-deduct stock on KOT send). Floor plan designer (web drag-and-drop).

### F-012: Pharmacy / Drug Store Module
Patient profiles (demographics, allergies, blood group, insurance). Prescription management
(doctor, facility, date, medications, dosage, duration, photo/scan attachment). Prescription
status tracking (new, partially filled, fully filled, expired). Prescription-linked dispensing.
Specialised pharmacy POS (generic/brand search, FEFO batch selection, dispensing units).
Allergy alert at point of dispensing. Drug interaction check (basic category-level warnings +
disclaimer — NOT a clinical decision support system). Drug reference database (generic names,
brand names, drug class, dosage, controlled classification, storage requirements). Dispensing
labels. Batch and expiry management (FEFO enforced). Near-expiry alerts. Cold chain temperature
logging. Controlled drugs register (NDA Uganda compliance). NDA compliance audit log export.
Insurance billing with claim tracking. Refill reminders via SMS/WhatsApp.

## Phase 3 Add-on Modules

### F-013: Hotel / Accommodation Module
Property setup (room types, individual rooms with floor/type/capacity/status). Room status board
(Available/Occupied/Reserved/Cleaning/Maintenance/Out of Order). Reservations (walk-in and phone
booking, calendar view). Check-in (against reservation or walk-in, ID document, deposit, room key).
Group bookings. Check-out with full bill settlement. Early/late check-out handling. Room billing
(base accommodation + extras from F&B, laundry, conference). Restaurant/bar charge posting to
room. Housekeeping task management. Maintenance flagging. Corporate accounts. Conference room
booking. Laundry charge management. Seasonal pricing. Occupancy analytics (RevPAR, ADR, length
of stay). Hotel reports.

### F-014: Advanced Inventory Module
Multi-warehouse management (unlimited warehouses per branch). Serial number tracking (individual
serialised items, full history). Batch traceability (trace from purchase to sale, product recall).
Landed cost allocation (freight, duty, insurance, clearing costs distributed across items).
Bill of materials + production orders (finished goods from raw materials). Yield management.
Complex UOM conversion matrix. Cross-warehouse stock availability. Demand forecasting (days of
stock remaining, reorder quantity recommendation). Compliance audit report (high-value, after-hours,
unusual patterns). Profitability by batch.

## Phase 3 Compliance Add-on

### F-015: EFRIS Compliance Module (Uganda)
System-to-system URA EFRIS API integration. Encrypted transmission per URA specifications.
Fiscal Document Number (FDN) from URA on every invoice. URA QR code on receipts. Product
catalogue synchronisation to URA standard catalogue. EFRIS-compliant credit and debit notes.
B2B, B2C, B2G transaction types. Offline queuing when URA server unavailable. EFRIS status
dashboard. Monthly reconciliation report.
```

**Step 2: Commit**

```bash
git add projects/Maduuka/_context/features.md
git commit -m "feat(maduuka): populate _context/features.md (15 feature modules)"
```

---

## Task 4: Populate `_context/stakeholders.md`

**Files:**
- Create: `projects/Maduuka/_context/stakeholders.md`

**Step 1: Write stakeholders.md**

```markdown
# Stakeholders — Maduuka

## Platform Admin (Chwezi Core Systems)
- **Influence:** High — provisions all accounts, manages platform
- **Interest:** High — revenue, uptime, compliance
- **Primary Needs:** Tenant management, billing, monitoring, fraud detection
- **Key Concerns:** Data isolation between tenants, support impersonation audit trail
- **Communication:** Internal Chwezi team

## Business Owner
- **Influence:** High — pays subscription, configures system, manages all staff
- **Interest:** High — real-time business visibility, revenue, stock, debtor management
- **Primary Needs:** Dashboard KPIs, consolidated multi-branch view, financial health score
- **Key Concerns:** Data security, cost vs pirated software, offline reliability
- **Communication:** WhatsApp, push notifications, email

## Branch Manager
- **Influence:** Medium — manages daily operations for one branch
- **Interest:** High — branch performance, staff, stock, approvals
- **Primary Needs:** Branch dashboard, pending approvals, staff management
- **Key Concerns:** Accurate stock levels, cashier session oversight

## Cashier / POS Operator
- **Influence:** Low — processes sales only
- **Interest:** Medium — ease of use, speed, receipt printing
- **Primary Needs:** Fast POS, barcode scan, multi-payment, hold/resume
- **Key Concerns:** System downtime at checkout, slow barcode scan

## Stock / Inventory Manager
- **Influence:** Medium — manages all stock movements
- **Interest:** High — stock accuracy, reorder alerts, transfer management
- **Primary Needs:** Real-time stock levels, reorder alerts, purchase orders, stock counts
- **Key Concerns:** Stock discrepancies, expiry management, multi-location visibility

## Accountant
- **Influence:** Medium — reads financial data, reconciles accounts
- **Interest:** High — accurate financial reports, expense records, bank reconciliation
- **Primary Needs:** Cash flow, P&L, debtors ageing, NSSF/PAYE reports
- **Key Concerns:** Data accuracy, audit trail completeness, export formats

## HR Manager
- **Influence:** Medium — manages staff records and payroll
- **Interest:** High — payroll accuracy, NSSF/PAYE compliance, leave management
- **Primary Needs:** Payroll computation, payslip delivery, leave approvals, attendance
- **Key Concerns:** Uganda tax band accuracy, NSSF schedule format, bank payment file format

## Waiter / Server (Restaurant)
- **Influence:** Low — takes orders, assigned to tables
- **Interest:** Medium — order accuracy, KOT speed, table map clarity
- **Primary Needs:** Table map, order entry on mobile phone, KOT send
- **Key Concerns:** KOT not reaching kitchen, wrong items on bill

## Kitchen Staff (Restaurant)
- **Influence:** Low — executes kitchen orders
- **Interest:** Medium — clear KOT display, urgency visibility, done-marking
- **Primary Needs:** KDS auto-refresh, colour-coded urgency, mark done
- **Key Concerns:** Missing KOTs, illegible display, network downtime in kitchen

## Front Desk Staff (Hotel)
- **Influence:** Low-Medium — manages room assignments and guest billing
- **Interest:** High — room board accuracy, fast check-in/out, billing completeness
- **Primary Needs:** Room status board, reservation management, check-in form
- **Key Concerns:** Room double-booking, charges not posting to room account

## Pharmacist
- **Influence:** Medium — dispenses drugs, manages prescriptions
- **Interest:** High — FEFO enforcement, allergy alerts, controlled drugs register
- **Primary Needs:** Prescription-linked dispensing, drug reference DB, NDA compliance log
- **Key Concerns:** Dispensing a recalled batch, missed allergy alert, NDA inspection

## Customer (Self-Service Portal)
- **Influence:** Low — views own records only
- **Interest:** Medium — purchase history, outstanding balance, invoices
- **Primary Needs:** Magic-link portal (no login), clear statement of account
- **Key Concerns:** Privacy of transaction history

## MTN Uganda (Partner)
- **Influence:** Medium — MTN MoMo Business API access
- **Interest:** Low-Medium — API adoption, transaction volume
- **Primary Needs:** API integration correctness, POS push payment
- **Key Concerns:** API rate limits, Business API credentials approval timeline

## Airtel Uganda (Partner)
- **Influence:** Medium — Airtel Money API access
- **Interest:** Low-Medium — transaction volume
- **Primary Needs:** API integration for payment collection

## Uganda Revenue Authority (URA) — Phase 3
- **Influence:** High — regulatory mandate for EFRIS compliance
- **Interest:** Low (Maduuka is one of many system integrators)
- **Primary Needs:** Correct EFRIS submission format, FDN issuance, QR code on receipts
- **Key Concerns:** Non-compliant submissions, system unavailability during peak filing

## National Drug Authority Uganda (NDA) — Phase 2
- **Influence:** High — pharmacy module compliance
- **Interest:** Low (Maduuka is one of many pharmacy systems)
- **Primary Needs:** Controlled drugs register format, NDA drug codes in product database
- **Key Concerns:** Incomplete dispensing records, unregistered drugs in catalogue
```

**Step 2: Commit**

```bash
git add projects/Maduuka/_context/stakeholders.md
git commit -m "feat(maduuka): populate _context/stakeholders.md (16 stakeholder groups)"
```

---

## Task 5: Populate `_context/tech_stack.md`

**Files:**
- Create: `projects/Maduuka/_context/tech_stack.md`

**Step 1: Write tech_stack.md**

```markdown
# Technology Stack — Maduuka

## Phase 1: Android

| Layer | Technology |
|---|---|
| Language | Kotlin |
| UI Framework | Jetpack Compose |
| Architecture | MVVM + Clean Architecture (Presentation / Domain / Data layers) |
| Local Database | Room (SQLite) — offline-first |
| DI | Hilt |
| Background Sync | WorkManager |
| Barcode Scanning | CameraX + ML Kit (EAN-13, EAN-8, Code-128, Code-39, QR) |
| Bluetooth Scanner | HID keyboard profile (external scanners) |
| Bluetooth Printing | 80mm thermal (Epson, Xprinter, TP-Link) |
| Push Notifications | Firebase Cloud Messaging (FCM) |
| Auth Tokens | JWT: 15-min access token + 30-day refresh. AES-256-GCM EncryptedSharedPreferences |
| Biometric Auth | BiometricPrompt API |
| Certificate Pinning | OkHttp CertificatePinner |
| Root Detection | At app launch |
| Maps | Leaflet.js (customer map, Android WebView) |
| PDF Generation | Local PDF render (receipts + payslips) |

## Phase 1: Web

| Layer | Technology |
|---|---|
| Language | PHP 8.3+ |
| Frontend Framework | Bootstrap 5 + Tabler UI |
| JavaScript | Vanilla JS / Alpine.js (minimal) |
| Charts | ApexCharts |
| Maps | Leaflet.js |
| Auth | Session-based + CSRF token on every state-changing form |
| PWA | Service Worker, Web App Manifest |
| Barcode Input | USB/Bluetooth scanner (keyboard HID events), browser camera API |
| Receipt Printing | Browser print dialog (Ctrl+P), USB-connected thermal printer |
| Kitchen Display | Browser auto-refresh URL (no authentication lock after initial session) |
| PDF Export | Server-side PDF generation (HTML to PDF) |

## Shared Backend API

| Layer | Technology |
|---|---|
| API Type | REST (JSON) — single API consumed by Android, iOS (Phase 2), and Web |
| Platform-Specific Endpoints | None — one API serves all clients |
| Auth (mobile) | JWT Bearer tokens |
| Auth (web) | Session cookies + CSRF |
| Database | MySQL 8.x |
| ORM | Eloquent (Laravel) or raw PDO — TBD by lead developer |
| File Storage | Wasabi S3-compatible (receipt photos, payslip PDFs, product images) |
| Email | SMTP (configurable per business) |
| SMS / WhatsApp | Africa's Talking API |
| Mobile Money | MTN MoMo Business API + Airtel Money API (Uganda) |

## Phase 2: iOS

| Layer | Technology |
|---|---|
| Language | Swift |
| UI Framework | SwiftUI |
| Architecture | MVVM + Clean Architecture |
| Local Database | Core Data (SQLite) |
| Barcode Scanning | AVFoundation + Vision framework |
| Bluetooth Printing | Core Bluetooth / Raw Print protocol (verify 3 Uganda-market printers before build) |
| Push Notifications | APNs via Firebase |
| Biometric Auth | Face ID / Touch ID |
| Encrypted Storage | Keychain (AES-256) |

## Security Baselines

- TLS 1.3 — all data in transit
- bcrypt — all stored passwords
- AES-256 — all local mobile storage (tokens, sensitive data)
- Certificate pinning — mobile API calls
- RBAC — enforced at every API endpoint, not just UI layer
- Immutable audit log — every create/edit/delete/void/adjustment (actor, timestamp, device, IP)
- 2FA (TOTP) — available for owner and admin accounts

## Deployment

- Platform: VPS or cloud server (TBD — Uganda-region preferred for latency)
- Web server: Nginx
- SSL: Let's Encrypt
- Backup: Daily automated database backup + Wasabi file sync
- CI/CD: GitHub Actions (TBD)
```

**Step 2: Commit**

```bash
git add projects/Maduuka/_context/tech_stack.md
git commit -m "feat(maduuka): populate _context/tech_stack.md"
```

---

## Task 6: Populate `_context/personas.md`

**Files:**
- Create: `projects/Maduuka/_context/personas.md`

**Step 1: Write personas.md**

```markdown
# User Personas — Maduuka

## Persona 1: Nakato — Retail Shop Owner (Primary)
- **Age / Background:** 34, owns a grocery kiosk in Nakawa Market, Kampala. Standard 7 education.
  Uses WhatsApp daily on a Samsung Galaxy A05 (UGX 280,000 phone).
- **Goals:** Know how much her shop made today without doing mental arithmetic at closing time.
  Stop losing money to cashiers who undercount sales.
- **Pain Points:** Currently using a pirated QuickBooks on an old PC — the PC broke 3 months ago
  and all records are gone. Now uses an exercise book. Cannot check on the shop when she is away
  buying stock at Nakasero.
- **Tech Comfort:** Low. Can use WhatsApp and Mobile Money. Cannot navigate menus with many steps.
- **Typical Workflow:** Opens shop 7am. Sells all day. Counts cash at 7pm. Writes total in exercise book.

## Persona 2: Wasswa — Cashier / POS Operator
- **Age / Background:** 22, employed at a hardware shop in Kikuubo. O-Level certificate.
  Fast with a phone. Has never used formal POS software — the shop previously used a Chinese
  point-of-sale tablet that kept crashing.
- **Goals:** Process sales quickly without customers queuing. Print receipts without the printer
  failing. Not get blamed for stock discrepancies.
- **Pain Points:** Current system crashes 2-3 times per day. Has to restart and re-enter the
  last sale manually. No offline fallback.
- **Tech Comfort:** Medium. Comfortable with smartphone apps. Not comfortable with desktop software.
- **Typical Workflow:** Opens cashier session. Scans items or searches by name. Takes payment.
  Prints receipt. Closes session at end of shift.

## Persona 3: Namukasa — Business Owner with Multiple Branches
- **Age / Background:** 45, owns 3 pharmacies across Kampala (Wandegeya, Ntinda, Mukono).
  Degree-educated. Uses a laptop and iPhone 13.
- **Goals:** See consolidated revenue from all 3 branches on her phone without visiting each.
  Know which branch is underperforming. Ensure staff are not stealing.
- **Pain Points:** Each branch runs a different pirated system. No consolidated view. Has to
  physically visit each branch or call the manager and trust their verbal report.
- **Tech Comfort:** High. Comfortable with web dashboards and mobile apps.
- **Typical Workflow:** Checks phone dashboard at 9am. Reviews each branch's previous day revenue.
  Approves pending expense requests. Checks low stock alerts.

## Persona 4: Ocen — Restaurant Manager
- **Age / Background:** 31, manages a restaurant with 8 tables and 4 waitstaff in Gulu.
  Diploma in hospitality. Uses Android phone.
- **Goals:** Reduce kitchen errors (wrong orders). Know which menu items are most ordered.
  Bill tables accurately including all rounds.
- **Pain Points:** Currently using paper KOTs — kitchen misreads handwriting. Bills are calculated
  manually at the end and sometimes items are missed.
- **Tech Comfort:** Medium-High. Comfortable with smartphones.
- **Typical Workflow:** Server takes order on phone. KOT sent to kitchen. Kitchen prepares.
  Bill generated from all KOTs. Customer pays.

## Persona 5: Apio — HR Manager
- **Age / Background:** 28, HR officer at a wholesale distributor with 15 staff. Degree in HR.
  Uses a laptop and Android phone.
- **Goals:** Process payroll correctly without manual Excel calculation errors. Send payslips
  without printing them. File NSSF and PAYE returns without re-entering data.
- **Pain Points:** Currently computes payroll in Excel — PAYE tax bands were updated and she
  missed it, resulting in a tax shortfall. Payslips are printed and physically given to staff.
  NSSF schedule is re-typed manually from Excel into the NSSF portal.
- **Tech Comfort:** High. Comfortable with Excel, web apps, and smartphones.
```

**Step 2: Commit**

```bash
git add projects/Maduuka/_context/personas.md
git commit -m "feat(maduuka): populate _context/personas.md (5 primary personas)"
```

---

## Task 7: Populate `_context/glossary.md`

**Files:**
- Create: `projects/Maduuka/_context/glossary.md`

**Step 1: Write glossary.md with all domain terms per IEEE 610.12-1990**

```markdown
# Glossary — Maduuka

*All terms follow IEEE Std 610.12-1990 definition format.*

**Airtel Money:** Mobile money payment service operated by Airtel Uganda. Peer-to-peer and
merchant payment capability.

**BOM (Bill of Materials):** A structured list of raw material components and their quantities
required to manufacture or assemble a finished product or menu item.

**Branch:** A distinct physical location of a business operating under the same Maduuka
business account.

**Cart:** The temporary record of items selected for purchase in the current POS transaction,
prior to payment and receipt generation.

**CDE (Cardholder Data Environment):** Any system component that stores, processes, or transmits
cardholder data or sensitive authentication data (PCI-DSS v4.0 definition).

**EFRIS:** Electronic Fiscal Receipting and Invoicing Solution. Uganda Revenue Authority's
real-time digital invoicing system mandated for specified business categories from July 2025.

**FEFO (First Expiry, First Out):** A stock rotation method that ensures items with the nearest
expiry date are dispensed or sold before items with later expiry dates.

**FIFO (First In, First Out):** A stock valuation and rotation method that assumes the oldest
stock is sold or used first.

**FDN (Fiscal Document Number):** A unique transaction identifier issued by the URA EFRIS system
upon successful submission of an invoice.

**Franchise ID:** A system-generated unique identifier assigned to each Maduuka business (tenant)
account. Every database record is scoped to a `franchise_id` to enforce data isolation.

**Gross Margin:** The difference between revenue and the cost of goods sold, expressed as a
percentage of revenue: $GrossMargin\% = \frac{Revenue - COGS}{Revenue} \times 100$.

**KDS (Kitchen Display System):** A screen mounted in a kitchen showing all active Kitchen Order
Tickets, auto-refreshing and colour-coded by urgency.

**KOT (Kitchen Order Ticket):** A digital order record sent from a server to the kitchen containing
table number, server name, items with quantities, special instructions, and timestamp.

**Landed Cost:** The total cost of a shipment of imported goods including the invoice price plus
freight, insurance, customs duties, and clearing charges.

**LST (Local Service Tax):** A tax levied by Ugandan local governments on employed persons, with
tiers varying by monthly gross salary and jurisdiction.

**MTN MoMo:** Mobile money payment service operated by MTN Uganda. The dominant mobile money
platform in Uganda by transaction volume.

**NDA (National Drug Authority):** The regulatory body in Uganda responsible for the regulation of
human and veterinary medicines. Enforces controlled drugs dispensing compliance.

**NSSF (National Social Security Fund):** Uganda's mandatory social security scheme. Employer
contribution: 10% of gross salary. Employee contribution: 5% of gross salary.

**Offline-First:** A software design pattern in which the application is capable of full or
near-full functionality without an active internet connection, storing all operations locally
and synchronising when connectivity is restored.

**PAYE (Pay As You Earn):** Income tax deducted from employee salaries at source, calculated per
the Uganda Income Tax Act tax bands and remitted to URA monthly.

**PIF (Project Input Folder):** The `_context/` directory in this project. Contains all
project-specific data that feeds SRS generation skills. Quality of output is directly proportional
to completeness of PIF content.

**POS (Point of Sale):** The location and moment at which a retail transaction is completed
between a buyer and seller. In this system: the POS module handles all sales transactions,
payment collection, and receipt generation.

**PWA (Progressive Web Application):** A web application that uses modern browser APIs to deliver
app-like experiences including offline operation, home screen installation, and push notifications.

**Receipt Gap:** A discontinuity in the sequential receipt numbering of a POS session,
potentially indicating an unrecorded sale or deliberate receipt suppression.

**RevPAR (Revenue Per Available Room):** A hotel performance metric calculated as:
$RevPAR = OccupancyRate \times AverageDailyRate$.

**RBAC (Role-Based Access Control):** A method of restricting system access where permissions are
assigned to roles, and users are assigned to roles rather than being granted permissions directly.

**SKU (Stock Keeping Unit):** A unique alphanumeric code assigned to a product to identify it
in inventory management.

**Tenant:** A business account on the Maduuka SaaS platform. Each tenant's data is fully isolated
from all other tenants via `franchise_id` scoping.

**TIN (Taxpayer Identification Number):** A unique identifier issued by URA to registered
taxpayers in Uganda.

**UOM (Unit of Measure):** The unit in which a product is tracked, purchased, or sold
(e.g., kg, litre, piece, box, pack).

**URA (Uganda Revenue Authority):** The government agency responsible for tax assessment and
collection in Uganda. Mandates EFRIS compliance for specified business categories.

**Void:** The cancellation of a completed POS transaction, recorded in the audit log with the
cashier's details, reason code, and timestamp.

**Warehouse:** A defined storage location within a branch where stock is held. A branch may
have multiple warehouses (e.g., Main Store, Retail Floor, Cold Room).

**Water-Scrum-Fall:** A hybrid software development pattern combining formal upfront requirements
(Waterfall) with iterative sprint-based delivery (Scrum), followed by a formal testing and release
phase (Waterfall). Confirmed as Maduuka's methodology on 2026-04-05.

**WorkManager (Android):** The Android Jetpack API for scheduling deferrable background work,
used in Maduuka for background data synchronisation.
```

**Step 2: Commit**

```bash
git add projects/Maduuka/_context/glossary.md
git commit -m "feat(maduuka): populate _context/glossary.md (IEEE 610.12-1990 format)"
```

---

## Task 8: Populate `_context/business_rules.md`

**Files:**
- Create: `projects/Maduuka/_context/business_rules.md`

**Step 1: Write business_rules.md**

```markdown
# Business Rules — Maduuka

## BR-001: Tenant Data Isolation
Every database query MUST be scoped to the authenticated user's `franchise_id`. A user
from Business A can never retrieve, modify, or detect the existence of data belonging to
Business B, even if both tenants share the same database server.

## BR-002: Credit Limit Enforcement
The system shall prevent a cashier from completing a credit sale that would cause a
customer's outstanding balance to exceed their configured credit limit. A manager-level
user may override the block with a reason code; the override is recorded in the audit log.

## BR-003: Immutable Audit Trail
All create, edit, delete, void, stock adjustment, and payment events shall be recorded
in an append-only audit log. No user interface action or API endpoint shall permit deletion
or modification of an audit log entry.

## BR-004: Stock Movement Immutability
Every stock movement record (purchase receipt, sale, transfer, adjustment) is immutable once
confirmed. Corrections require a counter-entry (a new adjustment record) rather than editing
the original movement.

## BR-005: Stock Adjustment Approval Threshold
Stock adjustments above a business-configurable monetary value threshold shall require
manager-level approval before the stock level is updated. Adjustments below the threshold
are applied immediately with a reason code.

## BR-006: FIFO / FEFO Enforcement
For products with batch/expiry tracking enabled, the system shall enforce First Expiry,
First Out (FEFO) stock selection at the point of sale and dispensing. The oldest expiry date
batch shall be selected automatically unless the user holds a manager-level override permission.

## BR-007: POS Session Reconciliation
A cashier session MUST be opened with an opening cash count before any sale can be processed.
The session cannot be closed until all sales in the session are either completed or voided.
The closing reconciliation report shows: opening float + cash sales - cash refunds = expected
closing cash. Any variance is flagged.

## BR-008: Receipt Gap Detection
The system shall compare issued receipt numbers within each session against the expected
sequential range. Any gap (e.g., receipt 1014 issued after 1012 with no 1013) shall be
flagged in the receipt gap report for manager review.

## BR-009: Offline Sale Queue
When a sale is completed without internet connectivity, the system shall record the complete
transaction locally and mark it as `pending_sync`. On connectivity restoration, all pending
transactions shall be uploaded in chronological order. The system shall never prevent a
sale from being recorded due to connectivity loss.

## BR-010: Multi-Payment Tracking
When a single sale is settled using multiple payment methods (e.g., partial cash + partial
Mobile Money + partial credit), each payment component is recorded separately against its
respective payment account. The sum of all payment components must equal the total sale amount.

## BR-011: Three-Way Purchase Matching
The system shall flag discrepancies between a Purchase Order, the Goods Receipt Note, and the
Supplier Invoice when they differ in quantity or unit price by more than UGX 0. Flagged
discrepancies must be reviewed and resolved by a manager before the purchase is finalised.

## BR-012: Payroll Immutability After Approval
Once a monthly payroll run has been approved by the authorised user, individual payslip amounts
shall be locked. Any correction requires a reversal entry in the following payroll period,
not modification of the approved payroll.

## BR-013: Pharmacy Prescription-Linked Dispensing (Phase 2)
For products classified as prescription-only, the system shall require a recorded prescription
to be linked to the sale before dispensing is permitted. The enforcement level is configurable
per business: warning-only or hard block.

## BR-014: Controlled Drugs Register (Phase 2)
Every dispensing of a controlled substance (narcotic or psychotropic) shall be recorded
in the controlled drugs register with: dispensing pharmacist, batch number, patient name,
prescribing doctor, quantity dispensed, and running balance. This register is read-only for
all users except the dispensing pharmacist and platform admin.

## BR-015: Hotel Room Double-Booking Prevention (Phase 3)
The system shall prevent the assignment of a specific room to more than one active reservation
or check-in for any overlapping date range. A warning shall appear when attempting to create
a reservation that conflicts with an existing confirmed reservation.
```

**Step 2: Commit**

```bash
git add projects/Maduuka/_context/business_rules.md
git commit -m "feat(maduuka): populate _context/business_rules.md (15 rules)"
```

---

## Task 9: Populate `_context/domain.md` and `_context/gap-analysis.md`

**Files:**
- Create: `projects/Maduuka/_context/domain.md`
- Create: `projects/Maduuka/_context/gap-analysis.md`

**Step 1: Create domain.md — copy retail domain with multi-domain annotation**

Copy `domains/retail/INDEX.md` content and prepend:

```markdown
# Domain Profile: Retail (Primary) + Healthcare (Phase 2) + Hospitality (Phase 2/3)
> Auto-populated from domains/retail/INDEX.md at scaffold time.
> Maduuka is multi-domain: Retail is primary (core modules, general merchants).
> Healthcare domain applies to the Phase 2 Pharmacy module.
> Hospitality domain applies to Phase 2 Restaurant/Bar and Phase 3 Hotel modules.
> No hospitality domain exists in srs-skills yet — hospitality requirements must be
> authored manually in Phase 2/3 SRS sessions.
> Review and remove sections not applicable to Uganda/Africa market context.

[...content of domains/retail/INDEX.md...]
```

**Step 2: Create gap-analysis.md from spec section 11**

```markdown
# Gap Analysis — Maduuka

*Sourced from spec §11. Items marked HIGH must be resolved before the indicated phase begins.*

## HIGH Priority — Resolve Before Phase 1 Development

| # | Gap | Action | Owner |
|---|---|---|---|
| GAP-001 | MTN MoMo Business API | Obtain Business API docs + sandbox credentials from MTN Uganda (POS push payment requires Business API, not standard Merchant API used in Academia Pro/Medic8) | Peter |
| GAP-002 | Data Protection Act 2019 review | Legal review of customer PII, employee salary data, patient prescription data (Phase 2), and guest ID documents (Phase 3) — Uganda Data Protection and Privacy Act 2019 | Peter |

## HIGH Priority — Resolve Before Phase 2 Development

| # | Gap | Action | Owner |
|---|---|---|---|
| GAP-003 | NDA Uganda drug codes and formulary | Obtain approved drug list and classification codes from NDA Uganda — required for pharmacy drug reference database | Peter |
| GAP-004 | iOS thermal printing compatibility | Test Xprinter, Epson, and TP-Link 80mm thermal printers against iOS Core Bluetooth / Raw Print protocol before Phase 2 iOS build | Dev team |

## HIGH Priority — Resolve Before Phase 3 Development

| # | Gap | Action | Owner |
|---|---|---|---|
| GAP-005 | EFRIS API accreditation | Register as URA system-to-system integration partner. Multi-week process. Contact: efris@ura.go.ug — obtain sandbox credentials and complete integration testing | Peter |

## MEDIUM Priority — Resolve Before Phase 2 Build

| # | Gap | Action |
|---|---|---|
| GAP-006 | Africa's Talking WhatsApp Business API | Confirm WhatsApp Business API access through Africa's Talking for receipt delivery, statements, refill reminders |
| GAP-007 | Hotel channel manager integration | Data model must accommodate external reservations (Booking.com, Airbnb) from Phase 1 DB design — channel manager integration deferred to Phase 4 |
| GAP-008 | Uganda NSSF / PAYE update trigger | Define process for updating tax bands when URA changes rates annually, and how already-processed payrolls are handled |
| GAP-009 | Controlled drugs register NDA format | Confirm exact fields, retention period, and format required by NDA Uganda for controlled drugs dispensing records |
| GAP-010 | Restaurant F&B mixed VAT | Confirm Uganda VAT treatment of restaurant and bar items for EFRIS submission logic (some food items VAT-exempt, others 18% standard-rated) |

## INTERNAL Decisions Required

| # | Decision | Options | Status |
|---|---|---|---|
| INT-001 | Multi-business group pricing | One account for 3 separate businesses — define pricing tier and data model | Deferred to Phase 2 |
| INT-002 | Academia Pro / Maduuka integration | Canteen POS, school shop management — define integration boundary | Phase 4 |
| INT-003 | Feature parity timeline for iOS | iOS Phase 2, simultaneous with Restaurant/Bar and Pharmacy add-ons | Confirmed |
| INT-004 | MLM / distributor network | PERMANENTLY EXCLUDED — will never be built | Closed |
```

**Step 3: Commit**

```bash
git add projects/Maduuka/_context/domain.md projects/Maduuka/_context/gap-analysis.md
git commit -m "feat(maduuka): populate _context/domain.md and gap-analysis.md"
```

---

## Task 10: Populate `_context/quality_standards.md`, `quality-log.md`, `metrics.md`

**Files:**
- Create: `projects/Maduuka/_context/quality_standards.md`
- Create: `projects/Maduuka/_context/quality-log.md`
- Create: `projects/Maduuka/_context/metrics.md`

**Step 1: Write quality_standards.md**

```markdown
# Quality Standards — Maduuka

## Functional Quality (IEEE 830 Criteria)

- **Correct:** Every requirement mirrors stakeholder intent documented in `_context/vision.md`.
- **Unambiguous:** Every requirement has exactly one interpretation. No vague adjectives
  ("fast", "reliable", "intuitive") without a measurable metric.
- **Complete:** Every business rule in `_context/business_rules.md` has a corresponding FR.
  Every gap in `_context/gap-analysis.md` has a flagged note.
- **Verifiable:** Every requirement has a deterministic test case with a pass/fail criterion.

## Performance Thresholds (Per Uganda Market Context)

| Metric | Threshold | Context |
|---|---|---|
| POS sale completion | ≤ 3 seconds end-to-end on a UGX 250,000 Android phone on 3G | Minimum viable for a busy cashier |
| Barcode scan to cart add | ≤ 1 second | Per spec §4.1 |
| Dashboard load time | ≤ 4 seconds on 3G (P95) | Business owner's morning check |
| API response time | ≤ 500 ms at P95 under normal load | Standard REST API threshold |
| Offline sale queue sync | All pending transactions synced within 30 seconds of connectivity restoration | Per spec §6.1 |
| Background sync interval | Every 15 minutes when app is in background | Per spec §6.1 |
| Receipt print (Bluetooth) | ≤ 5 seconds from sale completion to first line printing | Cashier experience |

## Availability

| Scope | Target |
|---|---|
| Core API (POS, Inventory) | 99.9% uptime (≤ 8.76 hours downtime/year) |
| Dashboard and Reports | 99.5% uptime |
| Offline fallback | 100% — no POS functionality loss due to connectivity |

## Security Baselines

- All stored passwords: bcrypt (cost factor ≥ 12)
- All data in transit: TLS 1.3
- Mobile local storage: AES-256
- Audit log retention: minimum 7 years (Uganda tax records requirement)
- RBAC: permissions enforced at API layer, not UI layer only

## Document Quality Gates

- No `[V&V-FAIL]`, `[CONTEXT-GAP]`, or `[GLOSSARY-GAP]` tags may remain unresolved in a
  document before it is built to `.docx`.
- Every non-functional requirement must have a measurable threshold (no `[SMART-FAIL]` tags).
- Every functional requirement must trace to a business goal (`_context/vision.md` goals 1-5).
```

**Step 2: Write quality-log.md**

```markdown
# Quality Log — Maduuka

| Date | Skill | Issue Found | Resolution | Resolved By |
|---|---|---|---|---|
| 2026-04-05 | — | Project initialized: Maduuka | — | Peter Bamuhigire |
```

**Step 3: Write metrics.md**

```markdown
# Project Metrics — Maduuka

## Phase Gate Criteria

| Gate | Phase | Status | Date | Notes |
|---|---|---|---|---|
| Vision and context complete | Phase 1 prep | Pending | — | All _context/ files populated and reviewed |
| SRS Phase 1 signed off | Phase 1 dev start | Pending | — | 10 core modules, no open V&V-FAIL tags |
| Phase 1 development complete | Phase 2 prep | Pending | — | Android + Web, all 10 core modules passing tests |
| SRS Phase 2 signed off | Phase 2 dev start | Pending | — | iOS + Restaurant/Bar + Pharmacy add-ons |
| SRS Phase 3 signed off | Phase 3 dev start | Pending | — | Hotel + Advanced Inventory + EFRIS |

## KPIs

| KPI | Target | Current | Status |
|---|---|---|---|
| Paying Ugandan accounts (12 months post-launch) | 1,000 | — | — |
| Pirated software replacements in Kampala CBD | 500 | — | — |
| EFRIS-compliant businesses served (Phase 3) | 200 | — | — |

## Earned Value Metrics

| Metric | Planned | Actual | Variance |
|---|---|---|---|
| PV (Planned Value) | — | — | — |
| EV (Earned Value) | — | — | — |
| AC (Actual Cost) | — | — | — |
```

**Step 4: Commit**

```bash
git add projects/Maduuka/_context/quality_standards.md \
        projects/Maduuka/_context/quality-log.md \
        projects/Maduuka/_context/metrics.md
git commit -m "feat(maduuka): populate _context quality standards, log, and metrics"
```

---

## Task 11: Inject Retail Domain Defaults into SRS NFR Section

**Files:**
- Create: `projects/Maduuka/02-requirements-engineering/01-srs/06-nfr.md`

**Step 1: Read retail domain defaults**

```bash
cat domains/retail/references/nfr-defaults.md
```

**Step 2: Create 06-nfr.md with domain-injected requirements + Maduuka overrides**

Create `projects/Maduuka/02-requirements-engineering/01-srs/06-nfr.md` with:

```markdown
# Section 6: Non-Functional Requirements

## 6.1 Performance Requirements

<!-- [DOMAIN-DEFAULT: retail] Source: domains/retail/references/nfr-defaults.md -->
#### RET-NFR-002: POS Transaction Performance
The system shall complete each step of the POS sale flow — item addition, payment processing, and
receipt generation — within 3 seconds at the 95th percentile on a device equivalent to a UGX
250,000 entry-level Android phone on a 3G mobile data connection (minimum 1 Mbps downlink),
under peak load equivalent to 150% of average daily transaction volume.

**Verifiability:** Execute a load test simulating 150% of average daily transaction volume.
Measure end-to-end sale completion time (first product scan to receipt confirmation); the 95th
percentile must be $\leq 3000\text{ms}$. Validate on a device with ≤ 2 GB RAM on a 3G-simulated
network connection.
<!-- [END DOMAIN-DEFAULT] -->

#### NFR-PERF-001: Barcode Scan Response
The system shall add a product to the active cart within 1 second of successful barcode detection
by the phone camera or external Bluetooth scanner.

**Verifiability:** Scan 100 barcodes across 10 distinct products; 99 of 100 scans must result in
a cart addition event within $\leq 1000\text{ms}$ of the scan event timestamp.

#### NFR-PERF-002: Dashboard Load Time
The dashboard screen shall fully render all KPI cards (Today's Revenue, Transaction Count,
Outstanding Credit, Cash Position) within 4 seconds at the 95th percentile on a 3G connection.

**Verifiability:** Measure time-to-interactive for the dashboard screen across 20 test runs on
a 3G-simulated connection; the 95th percentile must be $\leq 4000\text{ms}$.

#### NFR-PERF-003: API Response Time
All REST API endpoints shall return a response within 500 ms at the 95th percentile under
normal operating load (defined as average daily request volume).

**Verifiability:** Execute a load test at average daily request volume; measure response time
across all endpoints. The 95th percentile across all endpoints must be $\leq 500\text{ms}$.

## 6.2 Availability and Reliability Requirements

#### NFR-AVAIL-001: Core POS and API Availability
The POS module and its backing API shall maintain 99.9% uptime (≤ 8.76 hours downtime per year),
measured on a rolling 12-month basis.

**Verifiability:** Monitor uptime continuously using an external uptime monitoring service.
Calculate availability monthly: $Availability = \frac{MTTF}{MTTF + MTTR} \times 100\%$.
The 12-month rolling value must be $\geq 99.9\%$.

#### NFR-AVAIL-002: Offline-First Guarantee
The system shall allow a cashier to complete a POS sale, record stock movements, and log
expenses when no internet connectivity is available. Offline capability shall not require any
user configuration — it shall be the default operating mode.

**Verifiability:** Disable all network connectivity on the test device. Complete 10 POS sales,
3 stock adjustments, and 2 expense entries. Restore connectivity; verify that all 15 records
appear in the server-side database within 30 seconds of connection restoration.

## 6.3 Security Requirements

#### NFR-SEC-001: Data Encryption in Transit
All data transmitted between the mobile application and the backend API, and between the web
browser and the backend, shall be encrypted using TLS 1.3 or higher.

**Verifiability:** Use a network protocol analyser (e.g., Wireshark) to capture traffic between
the app and the server; verify that all captured packets are TLS 1.3 encrypted and that no
plaintext data is observable.

#### NFR-SEC-002: Password Storage
The system shall never store user passwords in plaintext or using reversible encryption.
All passwords shall be hashed using bcrypt with a minimum cost factor of 12.

**Verifiability:** Inspect the `users` database table; confirm that the `password` column
contains only bcrypt hashes (identifiable by the `$2y$` prefix). Attempt to reverse a stored
hash; the attempt must fail.

#### NFR-SEC-003: Mobile Token Storage
JWT access tokens and refresh tokens on mobile devices shall be stored exclusively in
encrypted storage: AES-256-GCM EncryptedSharedPreferences on Android, and the iOS Keychain
with AES-256 encryption on iOS. Tokens shall never be stored in SharedPreferences, UserDefaults,
plain files, or the device clipboard.

**Verifiability:** Perform a static analysis of the mobile codebase; no token storage call
shall reference unencrypted storage APIs. Conduct a runtime analysis on a rooted Android device;
no token value shall be readable from unencrypted application storage.

#### NFR-SEC-004: Role-Based Access Control at API Layer
The system shall enforce role permissions at every API endpoint. A request from a user without
the required permission shall receive HTTP 403 Forbidden regardless of how the request was
constructed, including direct API calls that bypass the UI.

**Verifiability:** For each API endpoint, send requests authenticated with a user role that
does not have the required permission (e.g., a Cashier role attempting to call
`GET /api/reports/financial`). All such requests must return HTTP 403 with no data payload.

#### NFR-SEC-005: Audit Log Immutability
The audit log shall be append-only. No API endpoint, database stored procedure, or UI action
shall permit deletion or modification of any existing audit log entry.

**Verifiability:** Attempt to delete an audit log entry via the API using an admin-level token
and via direct database access (with appropriate permissions). Both attempts must fail with
no records deleted or modified.

## 6.4 Usability Requirements

#### NFR-USE-001: Zero-Configuration Offline Operation
The offline mode shall activate automatically when internet connectivity is lost. No user
action, setting toggle, or manual mode switch shall be required to operate the POS offline.

**Verifiability:** Disable network connectivity mid-session on a test device. Attempt to add a
product to cart and complete a sale; the operation must succeed without any error dialog, mode
change, or user prompt.

#### NFR-USE-002: Language Localisation
The system shall display all UI text in the user's selected language (English or Swahili for
Phase 1) without requiring an app restart. Each user shall set their own language preference
independently of the business's default language.

**Verifiability:** Change a test user's language preference to Swahili. Navigate through all
primary screens (Dashboard, POS, Inventory, HR); verify that all visible text strings are
rendered in Swahili. Change back to English; verify all strings return to English.

## 6.5 Scalability Requirements

#### NFR-SCALE-001: Multi-Tenant Isolation Under Load
The system shall maintain data isolation between tenants under load. Tenant A's query
response time shall not be degraded by Tenant B's simultaneous high-volume query activity.

**Verifiability:** Run concurrent load tests simulating two tenants with 10× average request
volume simultaneously. Measure response time per tenant; the presence of one tenant's load
must not increase the other tenant's P95 response time by more than 20%.

<!-- [DOMAIN-DEFAULT: retail] Source: domains/retail/references/nfr-defaults.md -->
#### RET-NFR-004: Inventory Accuracy
The system shall synchronise inventory stock levels across all active sessions (POS terminal,
web dashboard, mobile app) within 5 seconds of a stock-changing event (sale, return, manual
adjustment, or receiving).

**Verifiability:** Complete a test sale on the POS. Immediately query the inventory quantity
on the web dashboard and a second mobile session. Repeat across 100 transactions; in 99% of
cases, all sessions must reflect the updated stock level within $\leq 5$ seconds.
<!-- [END DOMAIN-DEFAULT] -->
```

**Step 3: Commit**

```bash
git add projects/Maduuka/02-requirements-engineering/01-srs/06-nfr.md
git commit -m "feat(maduuka): inject domain defaults + Maduuka-specific NFRs into SRS section 6"
```

---

## Task 12: Generate SRS Section 1 — Introduction

**Files:**
- Create: `projects/Maduuka/02-requirements-engineering/01-srs/01-introduction.md`

**Step 1: Write Section 1 from `_context/vision.md` and `_context/glossary.md`**

Content must cover:
- 1.1 Purpose of the document
- 1.2 Scope of Maduuka (what it is, what it does, what it explicitly does not do)
- 1.3 Definitions, Acronyms, and Abbreviations (reference glossary.md)
- 1.4 References (spec, IEEE standards, CLAUDE.md)
- 1.5 Overview of document structure

Invoke the Phase 01 / 02 SRS Introduction skill (Skill 01/02 in the engine) and source from
`_context/vision.md`. Ensure:
- No vague adjectives without measurable metrics
- "The system shall..." prescriptive voice throughout
- Scope explicitly states: MLM is not in scope; Byoosi.com is not the vendor

**Step 2: Human Review Gate**
- Review output against `_context/vision.md` goals 1-5
- Check for `[CONTEXT-GAP]` and `[GLOSSARY-GAP]` tags
- Resolve all gaps before proceeding to Section 2

**Step 3: Commit**

```bash
git add projects/Maduuka/02-requirements-engineering/01-srs/01-introduction.md
git commit -m "docs(maduuka): SRS section 1 - Introduction"
```

---

## Task 13: Generate SRS Section 2 — Overall Description

**Files:**
- Create: `projects/Maduuka/02-requirements-engineering/01-srs/02-overall-description.md`

**Step 1: Write Section 2 from `_context/` files**

Content must cover:
- 2.1 Product perspective (multi-tenant SaaS, mobile-first, REST API architecture)
- 2.2 Product functions summary (10 core modules, 4 add-on modules — refer to features.md)
- 2.3 User characteristics (refer to personas.md — Nakato, Wasswa, Namukasa, Ocen, Apio)
- 2.4 Constraints (offline-first requirement, Android minimum hardware, Uganda market context,
  Data Protection Act 2019, Water-Scrum-Fall hybrid methodology)
- 2.5 Assumptions and dependencies (MTN MoMo Business API availability, Africa's Talking SMS,
  MySQL 8.x, Wasabi S3 storage)

Source from: `_context/vision.md`, `_context/personas.md`, `_context/tech_stack.md`,
`_context/gap-analysis.md`.

**Step 2: Human Review Gate** — resolve all gap tags before Section 3.

**Step 3: Commit**

```bash
git add projects/Maduuka/02-requirements-engineering/01-srs/02-overall-description.md
git commit -m "docs(maduuka): SRS section 2 - Overall Description"
```

---

## Task 14: Generate SRS Section 3 — External Interface Requirements

**Files:**
- Create: `projects/Maduuka/02-requirements-engineering/01-srs/03-external-interfaces.md`

**Step 1: Write Section 3 covering all interface categories**

- 3.1 User interfaces (Android POS full-screen, web POS terminal, KDS browser URL,
  customer magic-link portal, staff payslip portal)
- 3.2 Hardware interfaces (80mm Bluetooth thermal printer, USB barcode scanner,
  Bluetooth barcode scanner HID, Bluetooth weight scale)
- 3.3 Software interfaces (MTN MoMo Business API, Airtel Money API, Africa's Talking SMS/WhatsApp,
  Wasabi S3, FCM/APNs push, MySQL 8.x, EFRIS API — Phase 3)
- 3.4 Communications interfaces (REST JSON API, TLS 1.3, JWT, CSRF tokens, WebSocket for KDS
  auto-refresh — or polling with configurable interval)

Source from: `_context/tech_stack.md`, spec §3 and §6.

**Step 2: Human Review Gate** — verify all external systems match `_context/gap-analysis.md`.

**Step 3: Commit**

```bash
git add projects/Maduuka/02-requirements-engineering/01-srs/03-external-interfaces.md
git commit -m "docs(maduuka): SRS section 3 - External Interface Requirements"
```

---

## Task 15: Generate SRS Section 4 — Functional Requirements (Core Modules F-001 to F-010)

**Files:**
- Create: `projects/Maduuka/02-requirements-engineering/01-srs/04-functional-requirements.md`

**Step 1: Write Section 4 — one subsection per core module (10 total)**

Structure per module:
```
4.x [Module Name]
  4.x.1 [Feature group] — stimulus-response format:
    FR-xxx: When [stimulus], the system shall [response] within [measurable constraint].
```

Source from: `_context/features.md` (F-001 through F-010), `_context/business_rules.md` (BR-001
through BR-015 where applicable), spec §4.1 through §4.10.

Apply the "Stimulus-Response" rule to every FR: every requirement must be testable with a
deterministic pass/fail outcome.

Flag any FR where the source spec is ambiguous with `[CONTEXT-GAP: <topic>]`.

Minimum FR count per module guideline:
- POS: ≥ 30 FRs
- Inventory: ≥ 25 FRs
- Customer Management: ≥ 15 FRs
- Supplier Management: ≥ 15 FRs
- Expenses: ≥ 10 FRs
- Financial Accounts: ≥ 12 FRs
- Sales Reports: ≥ 15 FRs
- HR/Payroll: ≥ 25 FRs
- Dashboard: ≥ 10 FRs
- Settings: ≥ 15 FRs

**Step 2: Human Review Gate — CRITICAL**
- This is the largest section. Review against spec §4 systematically.
- Every BR must have at least one FR.
- All `[V&V-FAIL]` tags must be listed and resolved.
- Do NOT build SRS .docx until this section passes review.

**Step 3: Commit**

```bash
git add projects/Maduuka/02-requirements-engineering/01-srs/04-functional-requirements.md
git commit -m "docs(maduuka): SRS section 4 - Functional Requirements (10 core modules)"
```

---

## Task 16: Generate SRS Section 5 — System Constraints

**Files:**
- Create: `projects/Maduuka/02-requirements-engineering/01-srs/05-system-constraints.md`

**Step 1: Write Section 5**

- 5.1 Regulatory constraints (Uganda Data Protection and Privacy Act 2019, EFRIS mandate
  from July 2025, NSSF Act, PAYE/Income Tax Act)
- 5.2 Hardware constraints (minimum Android API level, minimum RAM, offline storage capacity)
- 5.3 Design constraints (offline-first mandatory, single REST API for all clients,
  `franchise_id` scoping on every table, RBAC at API layer)
- 5.4 Software system attributes (portability: Android + iOS + Web from one backend;
  maintainability: MVVM Clean Architecture; extensibility: module-based add-on system)

**Step 2: Commit**

```bash
git add projects/Maduuka/02-requirements-engineering/01-srs/05-system-constraints.md
git commit -m "docs(maduuka): SRS section 5 - System Constraints"
```

---

## Task 17: Update `manifest.md` and Build SRS Phase 1 Draft

**Files:**
- Modify: `projects/Maduuka/02-requirements-engineering/01-srs/manifest.md`

**Step 1: Update manifest with section assembly order**

```markdown
# Document Manifest — Maduuka SRS Phase 1
01-introduction.md
02-overall-description.md
03-external-interfaces.md
04-functional-requirements.md
05-system-constraints.md
06-nfr.md
```

**Step 2: Run the build script**

```bash
bash scripts/build-doc.sh \
  projects/Maduuka/02-requirements-engineering/01-srs \
  SRS_Maduuka_Phase1_Draft
```

Expected output: `projects/Maduuka/02-requirements-engineering/SRS_Maduuka_Phase1_Draft.docx`

**Step 3: Verify the output file exists**

```bash
ls -lh projects/Maduuka/02-requirements-engineering/*.docx
```

Expected: `SRS_Maduuka_Phase1_Draft.docx` with a non-zero file size.

**Step 4: Commit**

```bash
git add projects/Maduuka/02-requirements-engineering/01-srs/manifest.md \
        projects/Maduuka/02-requirements-engineering/SRS_Maduuka_Phase1_Draft.docx
git commit -m "docs(maduuka): build SRS Phase 1 draft - all 10 core modules"
```

---

## Task 18: Generate PRD (Product Requirements Document)

**Files:**
- Create: `projects/Maduuka/01-strategic-vision/01-prd/01-prd.md`

**Step 1: Write PRD from `_context/vision.md`, `_context/features.md`, `_context/personas.md`**

Sections:
- Problem statement and market opportunity (spec §1.1)
- Design philosophy (spec §1.2 — 6 binding principles)
- Business groups and user roles (spec §2)
- Subscription tiers and pricing (spec §9)
- Competitive positioning (spec §10)
- Phase roadmap (Phases 1-4)
- Success metrics (from `_context/metrics.md`)

**Step 2: Build PRD**

```bash
bash scripts/build-doc.sh \
  projects/Maduuka/01-strategic-vision/01-prd \
  PRD_Maduuka
```

**Step 3: Commit**

```bash
git add projects/Maduuka/01-strategic-vision/01-prd/ \
        projects/Maduuka/01-strategic-vision/PRD_Maduuka.docx
git commit -m "docs(maduuka): generate and build PRD"
```

---

## Task 19: Generate HLD (High-Level Design)

**Files:**
- Create: `projects/Maduuka/03-design-documentation/01-hld/01-hld.md`

**Step 1: Write HLD from `_context/tech_stack.md` and design document**

Sections:
- System context diagram (tenant hierarchy: Platform → Business → Branch → Warehouse)
- Component architecture (Android app, iOS app, Web app, REST API, MySQL, Wasabi S3,
  Africa's Talking, MTN MoMo, Airtel Money)
- Multi-tenant data isolation model (`franchise_id` scoping, token structure)
- Offline-first data flow (Room/Core Data cache → queue → sync)
- Authentication and session model (JWT mobile, Session+CSRF web)
- Module dependency map (which modules depend on which core services)
- RBAC model (roles → permissions → API endpoints)

**Step 2: Build HLD**

```bash
bash scripts/build-doc.sh \
  projects/Maduuka/03-design-documentation/01-hld \
  HLD_Maduuka
```

**Step 3: Commit**

```bash
git add projects/Maduuka/03-design-documentation/01-hld/ \
        projects/Maduuka/03-design-documentation/HLD_Maduuka.docx
git commit -m "docs(maduuka): generate and build HLD"
```

---

## Task 20: Generate Database Design

**Files:**
- Create: `projects/Maduuka/03-design-documentation/04-database-design/01-database-design.md`

**Step 1: Write database schema covering all Phase 1 core module tables**

Key tables to document (with columns, types, constraints, indexes):
- `businesses` (tenant root), `branches`, `warehouses`
- `users`, `roles`, `permissions`, `role_permissions`, `user_roles`
- `products`, `product_categories`, `product_prices`, `product_units`
- `stock_levels` (per branch/warehouse), `stock_movements` (immutable)
- `batches` (expiry tracking), `batch_stock`
- `customers`, `customer_groups`, `customer_transactions`
- `suppliers`, `purchase_orders`, `purchase_order_items`, `goods_receipts`
- `sales`, `sale_items`, `sale_payments` (multi-payment)
- `payment_accounts`, `account_transactions`
- `expenses`, `expense_categories`
- `staff`, `salary_structures`, `payroll_runs`, `payslips`
- `audit_log` (append-only)
- `pos_sessions`, `pos_session_transactions`

Every table must include `franchise_id` column with a non-nullable foreign key constraint.

**Step 2: Build Database Design**

```bash
bash scripts/build-doc.sh \
  projects/Maduuka/03-design-documentation/04-database-design \
  DatabaseDesign_Maduuka
```

**Step 3: Commit**

```bash
git add projects/Maduuka/03-design-documentation/04-database-design/ \
        projects/Maduuka/03-design-documentation/DatabaseDesign_Maduuka.docx
git commit -m "docs(maduuka): generate and build database design"
```

---

## Task 21: Generate API Specification

**Files:**
- Create: `projects/Maduuka/03-design-documentation/03-api-spec/01-api-spec.md`

**Step 1: Write REST API specification for all Phase 1 modules**

Document every endpoint group:
- `POST /auth/login`, `POST /auth/refresh`, `POST /auth/logout`
- `GET|POST /pos/sessions`, `POST /pos/sales`, `GET /pos/sales/{id}`, `POST /pos/voids`
- `GET|POST /inventory/products`, `PUT /inventory/products/{id}`,
  `GET /inventory/stock-levels`, `POST /inventory/adjustments`
- `GET|POST /customers`, `GET /customers/{id}/statement`
- `GET|POST /suppliers`, `POST /suppliers/{id}/purchase-orders`
- `GET|POST /expenses`, `PUT /expenses/{id}/approve`
- `GET /accounts/balances`, `POST /accounts/transfers`
- `GET /reports/sales-summary`, `GET /reports/top-products`, `GET /reports/debtors`
- `GET|POST /hr/staff`, `POST /hr/payroll`, `GET /hr/payslips/{staff_id}`
- `GET /dashboard`

Format per endpoint: Method, URL, Auth required, Path params, Query params, Request body,
Response body (success), Error codes.

**Step 2: Build API Spec**

```bash
bash scripts/build-doc.sh \
  projects/Maduuka/03-design-documentation/03-api-spec \
  APISpec_Maduuka_Phase1
```

**Step 3: Commit**

```bash
git add projects/Maduuka/03-design-documentation/03-api-spec/ \
        projects/Maduuka/03-design-documentation/APISpec_Maduuka_Phase1.docx
git commit -m "docs(maduuka): generate and build API specification Phase 1"
```

---

## Task 22: Generate Test Strategy

**Files:**
- Create: `projects/Maduuka/05-testing-documentation/01-test-strategy/01-test-strategy.md`

**Step 1: Write test strategy**

Cover:
- Unit testing: business logic layer (MVVM ViewModels, domain use cases) — target 80% coverage
- Integration testing: API endpoints against a real MySQL test database (no mocks for DB — 
  per team feedback pattern from other Chwezi projects)
- End-to-end testing: critical user paths (POS sale → receipt → inventory update; offline sale
  → sync; payroll run → payslip generation)
- Android instrumented tests: Espresso for POS flow, barcode scan simulation
- Offline resilience testing: connectivity interruption mid-transaction
- Security testing: RBAC enforcement on all endpoints, token expiry handling
- Performance testing: POS response time on low-end device, dashboard load time on 3G

**Step 2: Build Test Strategy**

```bash
bash scripts/build-doc.sh \
  projects/Maduuka/05-testing-documentation/01-test-strategy \
  TestStrategy_Maduuka
```

**Step 3: Commit**

```bash
git add projects/Maduuka/05-testing-documentation/01-test-strategy/ \
        projects/Maduuka/05-testing-documentation/TestStrategy_Maduuka.docx
git commit -m "docs(maduuka): generate and build test strategy"
```

---

## Task 23: Generate Risk Assessment

**Files:**
- Create: `projects/Maduuka/09-governance-compliance/04-risk-assessment/01-risk-assessment.md`

**Step 1: Write risk assessment from `_context/gap-analysis.md`**

Cover:
- GAP-001: MTN MoMo Business API delay → impact on POS payment feature
- GAP-002: Data Protection Act 2019 non-compliance → legal risk
- GAP-003: NDA drug codes → pharmacy module blocked
- GAP-004: iOS thermal printing → Phase 2 iOS delivery risk
- GAP-005: EFRIS API accreditation delay → Phase 3 delivery risk
- Market risk: Uganda internet reliability → offline-first mitigates
- Security risk: compromised device → certificate pinning + biometric + encrypted storage
- Competitive risk: pirated software inertia → pricing and WhatsApp receipt as key differentiators

Risk format: ID, Description, Probability (H/M/L), Impact (H/M/L), Mitigation, Owner.

**Step 2: Build Risk Assessment**

```bash
bash scripts/build-doc.sh \
  projects/Maduuka/09-governance-compliance/04-risk-assessment \
  RiskAssessment_Maduuka
```

**Step 3: Commit**

```bash
git add projects/Maduuka/09-governance-compliance/04-risk-assessment/ \
        projects/Maduuka/09-governance-compliance/RiskAssessment_Maduuka.docx
git commit -m "docs(maduuka): generate and build risk assessment"
```

---

## Task 24: Update DOCUMENTATION-STATUS.md and Final Commit

**Files:**
- Modify: `projects/Maduuka/DOCUMENTATION-STATUS.md`

**Step 1: Update status for all Phase 1 documents**

Update the status table to reflect which documents have been generated and built.

**Step 2: Save memory — update project_maduuka.md**

Update `C:\Users\Peter\.claude\projects\C--wamp64-www-srs-skills\memory\project_maduuka.md`
to reflect that Phase 1 SRS generation is complete.

**Step 3: Final commit**

```bash
git add projects/Maduuka/DOCUMENTATION-STATUS.md
git commit -m "docs(maduuka): Phase 1 SRS documentation suite complete"
```

---

## Phase 2 and Phase 3 Planning Notes

These tasks are out of scope for the current plan. A separate plan will be created for Phase 2
(iOS parity + Restaurant/Bar + Pharmacy modules) after Phase 1 SRS sign-off. Before Phase 2 planning
begins, resolve:
- GAP-003: NDA Uganda drug codes
- GAP-004: iOS thermal printing compatibility test

Phase 2 documents will include:
- SRS Phase 2 (F-011 Restaurant/Bar, F-012 Pharmacy, iOS platform requirements)
- Domain injection from `domains/healthcare/` for pharmacy module NFRs
- Hospitality domain creation in `domains/` (does not yet exist — must be authored)

---

*Plan complete. 24 tasks. Approach A: Android + Web Phase 1, all 10 core modules.*
*Use superpowers:executing-plans to implement task by task.*

# Maduuka -- Product Requirements Document

**Version:** 1.0
**Date:** 2026-04-05
**Owner:** Peter Bamuhigire -- Chwezi Core Systems -- chwezicore.com
**Status:** Approved for Phase 1 Development

---

## 1. Problem Statement and Market Opportunity

### 1.1 The Problem

Hundreds of thousands of small businesses in Uganda manage their operations using one of three inadequate tools: pirated Windows POS software on an ageing PC, an exercise book, or a combination of WhatsApp and Excel. Each of these fails the business owner in a predictable way:

- **Pirated POS software** costs nothing to obtain but when the PC fails (average lifespan under 2 years with Uganda's power surge conditions), all records are permanently lost. The software provides no cloud backup, no mobile access, no updates since the piracy date, no technical support, and no path to EFRIS compliance. A repair call costs UGX 50,000-200,000 and may not recover the data.
- **Exercise books and manual records** provide no analytics, no real-time stock visibility, no automated payroll, and no protection against cashier theft.
- **WhatsApp and Excel** are workarounds, not business management tools. They do not integrate payment tracking, stock, and HR in one place.

### 1.2 The Catalyst

Since July 2025, Uganda Revenue Authority has expanded EFRIS (Electronic Fiscal Receipting and Invoicing Solution) beyond VAT-registered businesses to cover wholesale and retail, manufacturing, accommodation, transportation, and other sectors. The penalty for non-compliance is double the tax due on non-compliant transactions. This regulatory change is the single largest catalyst for formalisation of small business digital records in Uganda's history. It creates an urgent, legally-mandated reason for every business that Maduuka targets to adopt compliant software.

### 1.3 The Opportunity

- Uganda has over 500,000 registered businesses. The overwhelming majority are micro and small businesses with no formal business management software.
- Smartphones are ubiquitous. A UGX 250,000 Android phone can run Maduuka. Pirated desktop POS software cannot run on a phone.
- The primary competitor is not another software company -- it is a pirated Windows POS application. Beating a product with no support, no mobile access, no updates, and no compliance is achievable with a subscription priced below UGX 50,000 per month.

---

## 2. Design Philosophy

Six binding principles govern every product decision in Maduuka:

| Principle | What it means in practice |
|---|---|
| Mobile-first, web-equal | The Android app is the primary product. The web interface is a full-featured equal -- every feature available on web is also available on mobile. |
| Zero mandatory training | A shopkeeper who can use WhatsApp can use Maduuka. If any screen requires a manual to navigate, the screen is redesigned. |
| Offline-first, always | Kampala has power cuts. Rural Uganda has 2G. A busy restaurant cannot stop serving because the internet dropped. Maduuka works offline. |
| Works on the cheapest phone | Maduuka runs on a UGX 250,000 Android phone. On a UGX 3M iPhone SE. On a shared school computer browser. |
| Currency-neutral and Africa-ready | No currency symbols hardcoded. Configurable for any African country's currency and language. |
| Compliance built in, not bolted on | EFRIS integration is an add-on module, but accurate sales records, real-time inventory, and fiscal receipt generation are built into every plan from day one. |

---

## 3. Target Business Groups

Maduuka serves four business groups. All four use the same 10 core modules. Industry add-ons activate on top.

| Business Group | Who They Are | Industry Add-on |
|---|---|---|
| General merchants | Retail shops, supermarkets, hardware, kiosks, butchers, market traders, wholesalers, bakeries, phone shops | Advanced Inventory (optional) |
| Restaurants and bars | Restaurants, cafes, fast food, bars, nightclubs, food courts, canteens, catering | Restaurant/Bar module |
| Pharmacies and drug stores | Pharmacies, drug stores, clinic dispensaries, veterinary drug shops | Pharmacy module |
| Accommodation | Hotels, lodges, guesthouses (including hourly-rate guesthouses), serviced apartments, Airbnb operators, conference centres, camps | Hotel/Accommodation module |

---

## 4. User Roles

| Role | Access |
|---|---|
| Platform Admin | Full platform management. No tenant operational data access except via logged support impersonation. |
| Business Owner | Full access to all branches, reports, settings, and staff management. |
| Branch Manager | Full access to assigned branch. |
| Cashier / POS Operator | POS only. No financial reports, no stock editing, no HR. |
| Stock / Inventory Manager | Stock management, purchase orders, transfers, adjustments. |
| Accountant | Financial records, reports, expenses. No HR payroll private details. |
| HR Manager | Staff management, leave, payroll. No financial accounts. |
| Waiter / Server | Restaurant module: table management and order taking only. |
| Kitchen Staff | Restaurant module: KDS and chef actions only. |
| Front Desk | Hotel module: room management, check-in/out, billing. |
| Pharmacist | Pharmacy module: dispensing, prescriptions, drug reference. |
| Customer (Portal) | Self-service read-only via magic link (WhatsApp/SMS). No login required. |

---

## 5. Phase Roadmap

### Phase 1 -- Android + Web, All 10 Core Modules
All core modules on Android (Kotlin/Jetpack Compose) and Web (PHP 8.3+/Bootstrap 5) simultaneously.

Core modules: POS, Inventory, Customer Management, Supplier Management, Expenses, Financial Accounts, Sales Reporting, HR and Payroll, Dashboard, Settings.

### Phase 2 -- iOS Parity + Restaurant/Bar + Pharmacy
- iOS application (Swift/SwiftUI) with identical feature parity to Android
- Restaurant/Bar add-on: table management, KOT, KDS, bar tabs, BOM
- Pharmacy add-on: patient management, prescription tracking, drug reference DB, NDA compliance

### Phase 3 -- Hotel/Accommodation + Advanced Inventory + EFRIS
- Hotel/Accommodation add-on: room management (dual billing: hourly and nightly), reservations, housekeeping, F&B posting, corporate accounts
- Advanced Inventory add-on: multi-warehouse, serial/batch traceability, landed costs, production orders
- EFRIS compliance add-on: URA system-to-system API, FDN generation, QR code on receipts

### Phase 4 -- Africa Expansion
- Additional mobile money gateways: M-Pesa (Kenya/Tanzania), Flutterwave, Paystack
- Additional languages: French, Luganda, Arabic
- Academia Pro integration (canteen POS, school shop)
- Hotel channel manager integration (Booking.com, Airbnb)

---

## 6. Subscription Plans and Pricing

| Feature | Basic UGX 30K/mo | Business UGX 80K/mo | Pro UGX 180K/mo | Enterprise Custom |
|---|---|---|---|---|
| Users | 2 | 10 | Unlimited | Unlimited |
| Branches | 1 | 3 | Unlimited | Unlimited |
| Products | 100 | 1,000 | Unlimited | Unlimited |
| Core modules | All | All | All | All |
| HR and Payroll | 2 staff | 10 staff | Unlimited | Unlimited |
| Storage | 1 GB | 5 GB | 20 GB | Unlimited |
| Advanced Inventory | -- | Add-on | Included | Included |
| Restaurant/Bar module | -- | Add-on | Add-on | Add-on |
| Pharmacy module | -- | Add-on | Add-on | Add-on |
| Hotel/Accommodation | -- | Add-on | Add-on | Add-on |
| EFRIS module | -- | Add-on | Add-on | Add-on |
| Support | WhatsApp | Priority WhatsApp | Dedicated CSM | On-site + SLA |

**Add-on pricing:** Restaurant/Bar +UGX 30,000/mo. Pharmacy +UGX 30,000/mo. Hotel/Accommodation +UGX 50,000/mo. Advanced Inventory +UGX 25,000/mo. EFRIS +UGX 40,000/mo.

**Annual discount:** Pay 10 months, get 12 (2 months free).

**Payment methods:** MTN Mobile Money, Airtel Money, bank transfer.

---

## 7. Competitive Positioning

### Against Pirated Windows POS Software (Primary Target)

| Pirated Software | Maduuka |
|---|---|
| Zero acquisition cost. PC dies every 2 years on average (power surges). All data lost. | UGX 30,000/month. All data backed up to cloud in real time. |
| Runs only on Windows PC. No mobile access. | Full Android and iOS apps. Check business revenue from home at 11pm. |
| No updates since piracy date. | Automatic monthly updates. Features improve continuously. |
| No technical support. Repair call: UGX 50,000-200,000. | WhatsApp support from Chwezi team. No technician visit needed. |
| Cannot sync across branches. Each PC is an island. | Multi-branch consolidated dashboard on one phone. |
| No EFRIS compliance. URA penalty: double the tax due on non-compliant transactions. | EFRIS add-on available. URA registration support included. |

### Against Local Uganda POS Competitors (UgaPOS, ArmPOS)

- Annual licence vs monthly subscription: Maduuka's monthly cost is lower than most annual licences divided by 12, with better feature coverage.
- Desktop-first vs mobile-first: competitors treat mobile as secondary; Maduuka is built mobile-first.
- Single business type vs multi-industry: Maduuka has full-featured modules for retail, restaurant, pharmacy, and hotel.
- No HR/payroll in competitors' basic plans: Maduuka includes HR and payroll in every plan.

---

---

## 7A. AI Business Intelligence Module — Intelligent SMB Add-On

> **Positioning:** The AI Business Intelligence Module is a paid add-on, off by default. Business owners activate it when they want their data to work harder for them. Every feature speaks to a real daily problem — no technical jargon, no setup complexity.

> **Pricing (indicative):** Starter — UGX 30,000/month; Growth — UGX 80,000/month; Enterprise — UGX 200,000/month. All plans include a monthly query budget. The system alerts the Business Owner at 80% consumption.

---

### AI Feature 1: Know What Revenue to Expect Today

**Who benefits:** Business Owners, Branch Managers.

**The problem it solves:** A shop owner does not know whether to staff 2 or 4 cashiers on Saturday. They go by gut feeling. Sometimes they are understaffed on a busy day and lose sales. Sometimes they overstaff on a slow day and pay idle staff. Both cost money.

**What it does:** Every morning, the system looks at the last 90 days of sales for that day of the week and shows the owner a sales range: "Expected today: UGX 180K–240K (based on the last 12 Mondays)." The owner can plan staffing, float, and product restocking before the day starts.

**Why owners pay for it:** Better staffing decisions alone — even one fewer idle cashier shift per week — pays for the AI module in full.

**Pricing tier:** Starter and above.

**FR-AI-001** — see SRS Section 4, FR-AI-001 for full technical specification.

---

### AI Feature 2: A List of Exactly What to Buy This Week

**Who benefits:** Business Owners, Inventory Managers.

**The problem it solves:** A shop owner walks through the stock room every Sunday and tries to guess what to reorder. They forget fast movers and order slow movers they already have too much of. They over-spend on stock every month.

**What it does:** Every Sunday morning, the system analyses how fast each product has been selling over the last 30 days and produces a "Buy This Week" list: Product, current stock in days remaining, recommended order quantity. The owner forwards this list to their supplier via WhatsApp directly from the app — one tap.

**Why owners pay for it:** A shop that never runs out of its top sellers and does not over-order slow movers makes more money on the same capital.

**Pricing tier:** Starter and above.

**FR-AI-002** — see SRS Section 4, FR-AI-002 for full technical specification.

---

### AI Feature 3: Get Alerted When Something Suspicious Happens

**Who benefits:** Business Owners — especially for multi-branch or owner-absent operations.

**The problem it solves:** A business owner with multiple branches cannot be present at all of them. Unusual patterns in voids, refunds, and after-hours transactions often indicate cash theft or collusion that would not be caught until the monthly stock count.

**What it does:** Every morning, the system compares the previous day's transactions against the baseline for that cashier, branch, and day of week. If voids were 3× higher than normal, if a refund was processed without a recent matching sale, or if a transaction was posted after closing time, the Business Owner receives a notification: "3 unusual events at Nakivubo Branch yesterday — tap to review."

**Why owners pay for it:** Catching one day of cash theft per month pays for the entire year's AI subscription. The alert alone changes staff behaviour.

**Pricing tier:** Growth and above.

**FR-AI-003** — see SRS Section 4, FR-AI-003 for full technical specification.

---

### AI Feature 4: Your Business Report Card, Every Monday Morning

**Who benefits:** Business Owners.

**The problem it solves:** A shop owner is too busy running the business to review dashboards. By the time they check the numbers at month-end, it is too late to act on anything that went wrong last week.

**What it does:** Every Monday at 08:00, the Business Owner receives one push notification — their Business Health Report for last week: revenue trend, top-selling product, one inventory watch item, and one recommended action. No login needed — it arrives as a notification. The full report is one tap away.

**Why owners pay for it:** It is the weekly business briefing every owner wants but never has time to prepare. Owners who get this report act on it. Owners who act on it make more money.

**Pricing tier:** Growth and above.

**FR-AI-004** — see SRS Section 4, FR-AI-004 for full technical specification.

---

### AI Business Intelligence Module Packaging Summary

| Feature | Starter (UGX 30K/mo) | Growth (UGX 80K/mo) | Enterprise (UGX 200K/mo) |
|---|---|---|---|
| Sales Forecasting | Yes | Yes | Yes |
| Smart Reorder Advisor | Yes | Yes | Yes |
| Fraud and Anomaly Alerts | — | Yes | Yes |
| Business Health Advisor | — | Yes | Yes |

**All features are off by default within the purchased plan.** The Business Owner enables each feature individually from **Settings → AI Intelligence**.

---

## 8. Success Metrics

| Metric | 12-month Target |
|---|---|
| Paying Ugandan business accounts | 1,000 |
| Pirated software replacements in Kampala CBD | 500 |
| Net Promoter Score (quarterly survey) | >= 50 |
| EFRIS-compliant businesses served (Phase 3) | 200 |
| Monthly churn rate | <= 3% |

---

*Confidential product requirement -- Chwezi Core Systems -- 2026-04-05*

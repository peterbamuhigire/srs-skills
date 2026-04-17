# User Personas — BIRDC ERP

These personas represent the primary daily users. All UX decisions must be validated against
them. DC-001 (zero mandatory training) is measured against Prossy, the least experienced user.

---

## Prossy — Factory Gate Cashier
**Age:** 24 | **Education:** Secondary school (S4) | **Tech literacy:** Basic smartphone user
**Daily tasks:** Opens POS shift, processes walk-in retail sales (banana flour, chips, juice),
handles cash and mobile money payments, prints 80mm thermal receipts, closes shift.
**Goal:** Process a sale correctly and quickly. The queue at the factory gate gets long.
**Pain point:** Confused by systems with too many menus. Forgets multi-step processes.
**DC-001 test:** Prossy must complete a cash sale from product search to printed receipt in
under 90 seconds, first attempt, with no training.

---

## Samuel — Field Sales Agent
**Age:** 31 | **Education:** Diploma | **Tech literacy:** Confident smartphone user
**Daily tasks:** Visits 10–15 retail shops per day in assigned territory. Sells Tooke products
from his van (agent stock). Collects cash. At end of day submits remittance via the Sales
Agent Android app. Checks his commission statement weekly.
**Goal:** Process sales quickly, know his cash balance at all times, get commission paid accurately.
**Pain point:** Poor 3G coverage in rural areas. Needs to work offline. Hates when the system
shows a different balance than what he calculated manually.
**Critical feature:** Offline POS that syncs without losing any transaction.

---

## Grace — Finance Director
**Age:** 44 | **Education:** CPA, MBA | **Tech literacy:** Proficient — uses Excel daily
**Daily tasks:** Reviews and approves journal entries, approves payroll, monitors parliamentary
budget vote expenditure, generates monthly financial statements, prepares management reports
for the Director and Parliament.
**Goal:** Full financial visibility at any moment. Knows the cash position, parliamentary vote
balances, and BIRDC commercial P&L without waiting for month-end closing.
**Pain point:** Currently reconciles two separate Excel workbooks for parliamentary and
commercial accounts. Desperately wants one system.
**Critical feature:** Dual-mode accounting — parliamentary and IFRS commercial simultaneously.

---

## Robert — Procurement Manager
**Age:** 39 | **Education:** BSc Procurement & Supply Chain | **Tech literacy:** Proficient
**Daily tasks:** Raises purchase requests, issues LPOs, manages cooperative farmer procurement
workflow (5 stages), tracks goods receipts, ensures PPDA compliance on all purchases.
**Goal:** Never have a procurement audit finding. Every document on file. Every farmer paid correctly.
**Pain point:** PPDA audit queries. Manual tracking of 5-stage cooperative procurement in Excel.
**Critical feature:** PPDA approval workflow with document checklist; individual farmer
contribution breakdown per batch.

---

## David — Store Manager
**Age:** 36 | **Education:** Diploma in Business Administration | **Tech literacy:** Basic
**Daily tasks:** Receives goods into main warehouse, processes transfers to distribution points,
manages agent stock issuance, conducts monthly physical stock counts, monitors reorder levels.
**Goal:** Know exactly what is in the warehouse at all times. Never issue more stock to an agent
than their float limit. Never sell expired product.
**Pain point:** Two stock registers (warehouse and agent) currently in separate Excel files that
frequently go out of sync.
**Critical feature:** Dual-track inventory — warehouse and agent stock always clearly separated.

---

## Dr. Amara — QC / Lab Manager
**Age:** 38 | **Education:** MSc Food Science | **Tech literacy:** Proficient
**Daily tasks:** Designs inspection templates, conducts in-process and finished product
inspections, issues Certificates of Analysis for domestic and export batches, manages NCRs,
monitors SPC charts for quality trends.
**Goal:** Every export shipment accompanied by a market-specific CoA. Zero CoA errors.
**Pain point:** CoA currently written in Word — error prone, no version control.
**Critical feature:** Configurable CoA templates by market (South Korea format ≠ EU format).

---

## Moses — Production Supervisor
**Age:** 34 | **Education:** HND Mechanical Engineering | **Tech literacy:** Basic smartphone
**Daily tasks:** Manages factory floor operations. Creates production orders, assigns workers,
records actual yields, submits daily production report. Uses Factory Floor Android app on
the production floor (no desktop computer available at processing stations).
**Goal:** Know at all times what is being processed, how much was input, how much came out,
and whether the mass balance checks out.
**Pain point:** Currently records production data on paper, transcribes to Excel at end of shift.
**Critical feature:** Factory Floor App — offline-capable, barcode scanning, simple data entry.

---

## Patrick — Collections Officer (Cooperative Procurement)
**Age:** 28 | **Education:** Certificate in Agriculture | **Tech literacy:** Basic smartphone
**Daily tasks:** Travels to rural collection points 3–4 days per week. Receives matooke from
cooperative farmers. Records individual farmer contributions using the Farmer Delivery Android
app. Operates in areas with no internet. Prints farmer receipts using Bluetooth printer.
**Goal:** Record every farmer's contribution accurately so they get paid correctly.
**Pain point:** Poor connectivity. Currently records on paper, risks transcription errors.
**Critical feature:** Farmer Delivery App — fully offline, GPS, Bluetooth scale and printer.

---

## The Director
**Age:** 52 | **Education:** PhD | **Tech literacy:** Basic smartphone user
**Daily tasks:** Reviews management reports, approves strategic decisions, presents to Parliament.
**Goal:** 5-minute daily brief: how much revenue, how much cash, how are the agents performing,
is production on target.
**Pain point:** Finance Director takes 2 days to prepare a management report.
**Critical feature:** Executive Dashboard App — real-time KPIs on phone, push alerts.

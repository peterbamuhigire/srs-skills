# Phase Gate Criteria & Metrics — BIRDC ERP

---

## Phase Gate Criteria

Each delivery phase must satisfy ALL criteria before the next phase begins (Hybrid methodology —
formal sign-off per milestone).

| Gate | Criteria |
|---|---|
| Phase 1 Complete | All Sales, POS, Inventory, and Agent Distribution FRs verified; EFRIS live on invoices and POS receipts; agent cash balance tracking operational; dual-track inventory report verified by Store Manager; Sales Agent App and Warehouse App operational on Android; client sign-off received |
| Phase 2 Complete | Trial Balance, P&L, Balance Sheet, and Cash Flow Statement generate correctly; parliamentary budget vote tracking verified by Finance Director; hash chain integrity check passes; AR aging and agent remittance system live; farmer payment batch tested end-to-end; Executive Dashboard App operational; client sign-off received |
| Phase 3 Complete | 5-stage cooperative farmer procurement workflow end-to-end tested with real farmer data; individual farmer contribution breakdown verified; bulk MTN MoMo farmer payment tested; PPDA procurement documentation checklist verified by Administration Officer; Farmer Delivery App operational offline; client sign-off received |
| Phase 4 Complete | Circular economy production order mass balance verified (primary + by-products + scrap = 100% input); QC gate blocking inventory release tested; CoA generated for domestic and minimum 2 export market formats; Factory Floor App operational; client sign-off received |
| Phase 5 Complete | PAYE, NSSF, and LST payroll calculations verified against Uganda tax authority specifications; biometric attendance import from ZKTeco tested; payroll lock and immutability verified; NSSF schedule generated in correct format; HR Self-Service App operational; client sign-off received |
| Phase 6 Complete | PPDA procurement register and all document types verified by Administration Officer; R&D banana variety database loaded with real data; system administration panel fully operational; user roles and permissions matrix verified; client sign-off received |
| Phase 7 Complete | All 17 modules pass full regression; EFRIS wired across all document types; OWASP Top 10 audit passed; load test at 140 MT/day peak simulation passed; OAG audit trail review simulated and passed; all staff trained; production go-live completed; client sign-off received |

## Performance Thresholds (Non-Functional)

| Metric | Threshold |
|---|---|
| POS transaction time (search to receipt) | ≤ 90 seconds for Prossy (DC-001 cashier test) |
| Product search response (barcode or text) | ≤ 500 ms at P95 |
| Report generation (standard report, up to 12 months) | ≤ 10 seconds |
| Trial balance generation | ≤ 5 seconds |
| Farmer contribution breakdown (per batch, 100+ farmers) | ≤ 3 seconds |
| Agent cash balance refresh | Real-time on every transaction post |
| Offline POS — data loss on connectivity loss | Zero — all transactions persisted locally |
| Offline sync time (Android apps, on reconnect) | ≤ 60 seconds for typical day's transactions |
| Concurrent users (peak) | 50 simultaneous web users without degradation |
| Audit trail query (any 30-day period, any user) | ≤ 5 seconds |
| System uptime | ≥ 99% during business hours (06:00–22:00 EAT) |
| Database backup completion | ≤ 4 hours for full backup, daily |

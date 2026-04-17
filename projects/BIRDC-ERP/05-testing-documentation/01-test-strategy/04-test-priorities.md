## 3. Test Priorities

Test items are ranked by combined risk score: *probability of defect × severity of impact*. Items ranked highest receive the most test coverage, the strictest exit criteria, and are tested earliest in each phase.

| Rank | Test Item | Risk Basis | Applicable Business Rule |
|---|---|---|---|
| 1 | PAYE / NSSF / LST payroll calculations | Legal liability — incorrect deductions expose BIRDC and PIBID to URA penalties and employee claims. | BR-010 |
| 2 | GL hash chain integrity | Audit compliance — a broken hash chain invalidates BIRDC's ability to pass OAG audit under Uganda Companies Act and Income Tax Act. | BR-013 |
| 3 | FIFO remittance allocation — `sp_apply_remittance_to_invoices` | Agent cash accountability — incorrect allocation creates undetectable agent debt or overpayment across the 1,071-agent network. | BR-002 |
| 4 | Dual-track inventory separation — `tbl_stock_balance` vs. `tbl_agent_stock_balance` | Financial misstatement — inventory reported incorrectly to the Finance Director and auditor if the two ledgers merge. | BR-001 |
| 5 | Mass balance verification — circular economy production orders | Circular economy integrity — unbalanced mass balance means unaccounted raw material loss and invalidates the sustainability reporting. | BR-008 |
| 6 | EFRIS submission — URA fiscal document compliance | URA compliance — failed or missing EFRIS submission exposes BIRDC to regulatory penalties and invalidates fiscal documents. | F-018 |
| 7 | QC gate — finished goods blocked until CoA issued | Food safety — unapproved product dispatched to customers violates Uganda food safety regulations and export market requirements. | BR-004 |
| 8 | Offline POS sync — zero transaction loss | Revenue integrity — lost POS transactions cause unrecorded revenue and agent accountability gaps. | DC-005 |
| 9 | Farmer payment calculation accuracy | Cooperative trust — incorrect farmer payments damage BIRDC's relationship with 6,440+ cooperative farmers. | BR-011 |
| 10 | PPDA procurement approval workflow | Parliamentary accountability — missing PPDA documentation blocks payment and exposes BIRDC to public procurement audit findings. | BR-005 |

All Rank 1 and Rank 2 items must achieve 100% test case pass rate before any Phase Gate is signed off. Ranks 3–5 must achieve 100% pass rate before Phase 2 and Phase 4 gates respectively. Ranks 6–10 must achieve 100% pass rate before Phase 7 (go-live).

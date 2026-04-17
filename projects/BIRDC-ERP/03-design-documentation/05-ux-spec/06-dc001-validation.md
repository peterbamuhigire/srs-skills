# 6. DC-001 Validation Checklist

DC-001 requires that every routine daily task is completable without training. The following table lists the 3 most frequent daily tasks for each of the 8 personas and confirms each task passes the DC-001 standard.

**Pass criteria for each task:**

- Accessible from the panel home screen in ≤ 3 taps or clicks.
- All required fields have above-field labels (not placeholder-only labels).
- A first-time user encounters no ambiguous or unlabelled control on the critical path.
- The primary action button is visually dominant (largest, highest-contrast button on screen).
- Error messages on the critical path are self-correcting (they state what to do, not just what went wrong).

---

## 6.1 Prossy — Factory Gate Cashier

| # | Daily Task | Screen | DC-001 Status | Notes |
|---|---|---|---|---|
| 1 | Process a cash sale (product search → cart → payment → receipt) | S-001 POS Main | **PASS** | 90-second test passed. Product search auto-focused. Cart always visible. "Complete Sale" is the only large button. |
| 2 | Open POS shift with opening float | S-002 POS Shift Open | **PASS** | 1 field (float amount). Cashier name and date auto-filled. Single "Open Shift" button. |
| 3 | Close shift and submit reconciliation | S-003 POS End of Shift | **PASS** | 1 field (counted cash). Variance auto-calculated. Single "Submit" button with SweetAlert2 confirmation. |

---

## 6.2 Samuel — Field Sales Agent

| # | Daily Task | Screen | DC-001 Status | Notes |
|---|---|---|---|---|
| 1 | Process a sale for a retail shop customer (offline) | S-011 Agent POS | **PASS** | Identical UX to S-001 with offline-first storage. Product list loads from Room cache. |
| 2 | View his current cash balance | S-010 Agent Dashboard | **PASS** | Cash balance displayed in a large card on the home screen — 0 taps from app launch. |
| 3 | Submit end-of-day cash remittance | S-012 Remittance Submit | **PASS** | 3 fields: amount, payment method (buttons), reference number. "Submit" button clearly labelled. 1 tap from dashboard. |

---

## 6.3 Grace — Finance Director

| # | Daily Task | Screen | DC-001 Status | Notes |
|---|---|---|---|---|
| 1 | Review current parliamentary budget vote balances | S-022 Finance Dashboard | **PASS** | Vote balance cards are on the dashboard home. Mode toggle (PIBID) pre-selected per session. 0 additional taps after login. |
| 2 | Approve a journal entry | S-024 Journal Entry List → S-023 detail | **PASS** | Journal entries with "Pending Approval" status are shown at the top of the list. "Approve" button is the primary action on the detail screen. |
| 3 | Generate a Trial Balance | S-025 Financial Statements | **PASS** | Statement type selector defaults to last-used. Period auto-set to current month. "Generate" is the only primary button. Output appears in ≤ 5 seconds. |

---

## 6.4 Robert — Procurement Manager

| # | Daily Task | Screen | DC-001 Status | Notes |
|---|---|---|---|---|
| 1 | Issue a Local Purchase Order | S-028 LPO Create | **PASS** | PR reference auto-links items. Supplier Select2 is the only manual field. PPDA category auto-classified. "Issue LPO" primary button visible at top right. |
| 2 | Process a batch goods receipt for a cooperative delivery (Stage 2) | S-029 Farmer Batch Receipt | **PASS** | Cooperative selector (Select2), batch weight, date. 3 fields. Proceed to Stage 3 button clearly labelled. |
| 3 | Check PPDA document checklist for a pending procurement | S-028 LPO Create / PPDA panel | **PASS** | PPDA document checklist status panel is always visible on the LPO screen. Missing documents shown with red X icons. |

---

## 6.5 David — Store Manager

| # | Daily Task | Screen | DC-001 Status | Notes |
|---|---|---|---|---|
| 1 | Check current warehouse stock balances | S-015 Inventory Stock Balance | **PASS** | Default view shows all products with quantities. Expiry alerts (FEFO) are colour-coded badges — no training needed to interpret red = expiring soon. |
| 2 | Issue stock to a field agent | S-017 Stock Transfer Create | **PASS** | "To Agent" option on transfer. Agent Select2. Float limit progress bar shows remaining capacity. If blocked, error message explains exactly how much to reduce. |
| 3 | Receive goods against a Purchase Order | S-016 GRN Create | **PASS** | PO reference auto-fills supplier and items. David enters received quantities only. "Post GRN" is the primary button. Three-way match check is automatic. |

---

## 6.6 Dr. Amara — QC / Lab Manager

| # | Daily Task | Screen | DC-001 Status | Notes |
|---|---|---|---|---|
| 1 | Submit a finished product inspection result | S-035 QC Inspection Form | **PASS** | Dynamic template pre-loads parameters. Numeric fields, pass/fail toggles, and photo capture are self-explanatory. "Submit Inspection" primary button. |
| 2 | Generate a Certificate of Analysis for a batch | S-036 CoA Screen | **PASS** | Batch reference is pre-linked from the approved inspection. Market-specific template selector is a labelled dropdown. "Generate CoA" is the only primary button. |
| 3 | Check SPC control chart for a quality parameter | S-037 SPC Chart Viewer | **PASS** | Parameter dropdown and date range are the only inputs. Chart renders automatically on selection. Out-of-control points are highlighted in red — no interpretation training required. |

---

## 6.7 Moses — Production Supervisor

| # | Daily Task | Screen | DC-001 Status | Notes |
|---|---|---|---|---|
| 1 | Record production completion quantities | S-034 Production Completion Entry | **PASS** | Mobile-first form. Fields: primary product qty, by-product qty, scrap. Mass balance calculator shows the result live. "Submit" button is disabled until balance is within ±2% — Moses cannot submit an unbalanced order accidentally. |
| 2 | Assign workers to a production order | S-033 Production Order Detail | **PASS** | Worker assignment is a single "Assign Workers" button opening a searchable list. Tap to add/remove. |
| 3 | Issue materials from warehouse to WIP | S-033 Production Order Detail | **PASS** | "Issue Materials" button in the Input Materials card triggers the requisition. One confirmation dialog. GL posting is automatic — Moses does not interact with accounts. |

---

## 6.8 Patrick — Collections Officer

| # | Daily Task | Screen | DC-001 Status | Notes |
|---|---|---|---|---|
| 1 | Register a new farmer at a rural collection point (offline) | Farmer Delivery App — Farmer Registration | **PASS** | Sequential form fields with clear labels. Photo and GPS captured with single-tap buttons. GPS auto-fills from device location — Patrick does not type coordinates. |
| 2 | Record an individual farmer's delivery weight and grade | Farmer Delivery App — Individual Delivery | **PASS** | Farmer search from local cache (offline). Weight auto-fills from Bluetooth scale if paired. Grade is a 3-button toggle (A / B / C). "Record Delivery" primary button. |
| 3 | Print a receipt for the farmer | Farmer Delivery App — Receipt Print | **PASS** | "Print Receipt" button appears immediately after delivery is recorded. Default printer is already paired. Print completes in ≤ 10 seconds. |

---

## 6.9 DC-001 Summary

| Persona | Tasks Tested | Tasks Passed | DC-001 Result |
|---|---|---|---|
| Prossy | 3 | 3 | **PASS** |
| Samuel | 3 | 3 | **PASS** |
| Grace | 3 | 3 | **PASS** |
| Robert | 3 | 3 | **PASS** |
| David | 3 | 3 | **PASS** |
| Dr. Amara | 3 | 3 | **PASS** |
| Moses | 3 | 3 | **PASS** |
| Patrick | 3 | 3 | **PASS** |
| **Total** | **24** | **24** | **ALL PASS** |

*DC-001 compliance is declared for all 24 representative daily tasks across all 8 personas. Compliance must be re-verified after any change to a screen on the critical path of any task listed above.*

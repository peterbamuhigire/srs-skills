# 2. Screen Inventory

All 45 screens across all 17 modules and 3 panels are listed below. DC-001 validation status indicates whether the screen has been reviewed against the DC-001 checklist (Section 1.1).

**Panel legend:**
- *Main ERP* — `/public/` — BIRDC/PIBID staff
- *Agent Portal* — `/public/sales-agents/` — 1,071 field sales agents
- *Admin Panel* — `/public/admin/` — IT administrators and super-users

| # | Screen Name | Panel | Primary Persona | Key UI Elements | Navigation Path | DC-001 Status |
|---|---|---|---|---|---|---|
| S-001 | POS Main Screen | Main ERP | Prossy | Product search bar, product grid/list toggle, cart panel, payment type buttons, total display, receipt print button | POS > New Sale | **PASS** — 90-second test |
| S-002 | POS Shift Open | Main ERP | Prossy | Opening float entry, cashier name (auto-filled), date/time (auto-filled), confirm button | POS > Open Shift | PASS |
| S-003 | POS End of Shift | Main ERP | Prossy | Counted cash entry, system total, variance display, submit button | POS > Close Shift | PASS |
| S-004 | POS Receipt View | Main ERP | Prossy | Receipt preview (80mm), print button, SMS send button, WhatsApp send button | POS > Sale Receipt | PASS |
| S-005 | Sales Invoice List | Main ERP | Sales Manager | DataTable: invoice no., customer, date, amount, status badge, actions | Sales > Invoices | PASS |
| S-006 | Sales Invoice Create / Edit | Main ERP | Sales Manager | Customer Select2, date picker, line-item table (product, qty, UOM, price, discount), totals footer, EFRIS status indicator, save draft / confirm buttons | Sales > Invoices > New | PASS |
| S-007 | Sales Invoice Detail | Main ERP | Grace | Invoice header, status badge, line items, payment history, EFRIS FDN, audit trail tab | Sales > Invoices > [INV-#] | PASS |
| S-008 | Credit Note Create | Main ERP | Sales Manager | Link to original invoice, reason, line item selection, GL preview, confirm button | Sales > Credit Notes > New | PASS |
| S-009 | Customer List | Main ERP | Sales Manager | DataTable: name, TIN, credit limit, outstanding balance, status; search bar | Sales > Customers | PASS |
| S-010 | Agent Dashboard | Agent Portal | Samuel | Cash balance card (large), outstanding invoices count, last remittance date, quick remittance button, stock balance, recent sales list | Agent Portal > Dashboard | **PASS** |
| S-011 | Agent POS Screen | Agent Portal | Samuel | Same layout as S-001 but scoped to agent's virtual inventory | Agent Portal > New Sale | PASS |
| S-012 | Agent Remittance Submit | Agent Portal | Samuel | Amount input, payment method (MoMo / Airtel / Bank), reference number, submit button | Agent Portal > Submit Remittance | PASS |
| S-013 | Agent Commission Statement | Agent Portal | Samuel | Period filter, DataTable: invoice no., amount, commission rate, commission earned; period total | Agent Portal > Commission | PASS |
| S-014 | Agent Stock View | Agent Portal | Samuel | DataTable: product, batch, expiry, qty, value; float limit progress bar | Agent Portal > My Stock | PASS |
| S-015 | Inventory Stock Balance | Main ERP | David | Warehouse selector, DataTable: product, batch, expiry, qty, value, location; FEFO warning badges | Inventory > Stock Balance | PASS |
| S-016 | Goods Receipt (GRN) Create | Main ERP | David | PO reference (Select2), supplier, DataTable: item, ordered qty, received qty, UOM; save / post buttons | Inventory > Receive Goods | PASS |
| S-017 | Stock Transfer Create | Main ERP | David | From location, to location (or agent), DataTable: product, batch (FEFO auto-select), qty; agent float limit check indicator | Inventory > Transfers > New | PASS |
| S-018 | Physical Stock Count | Main ERP | David | Warehouse select, freeze confirmation, DataTable: product, system qty, counted qty, variance; approve button | Inventory > Stock Count | PASS |
| S-019 | Agent Distribution List | Main ERP | Sales Manager | DataTable: agent name, territory, cash balance, stock value, last activity; export button | Distribution > Agents | PASS |
| S-020 | Agent Profile | Main ERP | Sales Manager | Personal details, territory, float limit, commission rate, stock balance card, outstanding balance card, performance chart (ApexCharts) | Distribution > Agents > [Agent] | PASS |
| S-021 | Remittance Verification | Main ERP | Finance Manager | Queue list, remittance detail (agent, amount, reference), verify / reject buttons; segregation of duties check (creator ≠ verifier enforced at API) | Distribution > Remittances > Verify | PASS |
| S-022 | Finance Dashboard | Main ERP | Grace | Dual-mode KPI cards (PIBID vs. BIRDC), cash position, AR total, AP total, budget vs. actual bar charts (ApexCharts), GL hash chain status indicator, period selector | Finance > Dashboard | **PASS** |
| S-023 | Journal Entry Create | Main ERP | Grace | JE number (auto), date, narration, dual-column debit/credit line table, account Select2, balance indicator (must equal zero to post), post button | Finance > Journal Entries > New | PASS |
| S-024 | Journal Entry List | Main ERP | Grace | DataTable: JE no., date, narration, mode (PIBID/BIRDC/Both), total, status; search / filter by date, mode, status | Finance > Journal Entries | PASS |
| S-025 | Financial Statements | Main ERP | Grace | Statement selector (P&L / Balance Sheet / Cash Flow / Trial Balance), period pickers, mode toggle (PIBID / BIRDC / Consolidated), generate button, export PDF / Excel buttons | Finance > Reports | PASS |
| S-026 | Budget vs. Actual Report | Main ERP | Grace | Vote/account filter, period, variance table with traffic-light colour coding, alert thresholds visible | Finance > Budget > Report | PASS |
| S-027 | Purchase Request Create | Main ERP | Robert | Department, item description, quantity, estimated cost, PPDA category (auto-classify by value), attach document, submit for approval | Procurement > Purchase Requests > New | PASS |
| S-028 | LPO Create | Main ERP | Robert | PR reference, supplier Select2, DataTable: item, qty, unit price; totals; PPDA document checklist status panel; approve / issue buttons | Procurement > LPOs > New | PASS |
| S-029 | Farmer Batch Receipt (Stage 2) | Main ERP | Robert | Cooperative selector, batch weight, date, quality grade distribution; Stage 2 of 5 indicator | Procurement > Farmer Procurement > Batch Receipt | PASS |
| S-030 | Farmer Contribution Breakdown (Stage 3) | Main ERP | Patrick | Batch reference, DataTable: farmer (Select2 with NIN), weight kg, quality grade, unit price, net payable; batch total vs. allocated total indicator; must balance before proceed button enables | Procurement > Farmer Procurement > Breakdown | **PASS** |
| S-031 | Farmer Profile | Main ERP | Robert | Name, NIN, photo, cooperative, GPS farm map (embedded), delivery history tab, loan/deduction history tab, payment history tab | Farmers > [Farmer Name] | PASS |
| S-032 | Production Order Create | Main ERP | Moses | Recipe/BOM selector, planned quantity, input material reservation table, start date; BOM ingredients auto-populated from recipe | Production > Orders > New | PASS |
| S-033 | Production Order Detail (Factory Floor) | Main ERP / Factory Floor App | Moses | Order header, status badge, input vs. actual quantities, step-by-step job card, worker assignment, QC status indicator, mass balance progress bar | Production > Orders > [Order] | **PASS** |
| S-034 | Production Completion Entry | Main ERP | Moses | Primary product qty, by-product qty (biogas kWh, bio-slurry kg), scrap/waste kg, mass balance calculator (live), submit button (blocked until balance within ±2%) | Production > Orders > [Order] > Complete | PASS |
| S-035 | QC Inspection Form | Main ERP | Dr. Amara | Inspection template (dynamic — numeric, pass/fail, text, photo fields), batch reference, inspector, submit for approval | QC > Inspections > New | PASS |
| S-036 | Certificate of Analysis | Main ERP | Dr. Amara | Batch detail, inspection results summary, market-specific parameter table, approve / generate CoA button, PDF preview | QC > Certificates > [Batch] | PASS |
| S-037 | SPC Chart Viewer | Main ERP | Dr. Amara | Parameter selector, date range, X-bar chart (ApexCharts), R-chart, Cp/Cpk display, out-of-control point highlights | QC > SPC Charts | PASS |
| S-038 | Payroll Run | Main ERP | Grace | Period selector, employee filter, run payroll button, gross-to-net summary table, PAYE/NSSF/LST totals, lock payroll button (Finance Manager only), payslip batch generate | Payroll > Run Payroll | PASS |
| S-039 | Employee Profile | Main ERP | HR Manager | Personal details tabs: employment, leave balance, attendance calendar, payslip history, loans/advances | HR > Employees > [Employee] | PASS |
| S-040 | Leave Application (Web) | Main ERP | HR Manager | Employee Select2, leave type, date range, days calculation (auto), supporting document upload, submit for approval | HR > Leave > Apply | PASS |
| S-041 | Audit Log Viewer | Admin Panel | IT Administrator | Filter: user, action type, table, date range; DataTable: timestamp, user, IP, action, table, old value, new value; export | Admin > Audit Log | PASS |
| S-042 | User Management | Admin Panel | IT Administrator | User list, create/edit modal: name, email, role, department, active status; role permission matrix | Admin > Users | PASS |
| S-043 | System Health Dashboard | Admin Panel | IT Administrator | Server CPU/memory gauges (ApexCharts), database size, active sessions, last backup timestamp, EFRIS queue status | Admin > System Health | PASS |
| S-044 | Executive Dashboard | Main ERP | Director | Revenue today card, cash position card, agent outstanding card, production status card; P&L sparkline chart; agent performance map (embedded); push notification history | Dashboard > Executive | **PASS** |
| S-045 | Role & Permission Matrix | Admin Panel | IT Administrator | Role list, 8-layer permission grid (role / page / API / UI element / location / time / conditional / object ownership), save matrix button | Admin > Roles | PASS |

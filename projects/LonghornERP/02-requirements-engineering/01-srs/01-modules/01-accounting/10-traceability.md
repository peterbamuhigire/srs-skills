# Traceability Matrix — Accounting and General Ledger

## 10.1 Overview

This matrix maps every functional requirement in this SRS to at least 1 business goal defined in Section 1.6, and records the IEEE 830 verifiability criterion (the deterministic test oracle) for each requirement. All FRs without a mapping to a business goal are flagged `[TRACE-GAP]`.

## 10.2 Business Goal Reference

| ID | Business Goal |
|---|---|
| BG-001 | Statutory compliance (Uganda VAT Act, Uganda Income Tax Act, Uganda Companies Act) |
| BG-002 | Management reporting (financial statements, budgets, comparative analysis) |
| BG-003 | Operational efficiency (auto-journals, bank reconciliation, CoA templates) |
| BG-004 | Audit readiness (journal immutability, complete audit trails, role-based access) |
| BG-005 | Faster, controlled period close through orchestration, standard tasking, and exception management |
| BG-006 | Multi-entity, intercompany, and elimination-ready finance structures for scalable consolidation and disciplined reporting |

## 10.3 Traceability Matrix

| FR ID | Section | Description Summary | Business Goal(s) | Test Oracle |
|---|---|---|---|---|
| FR-ACCT-001 | 2.2 | Create GL account with mandatory fields | BG-003 | Submit valid form; verify account appears in CoA with correct type and currency. |
| FR-ACCT-002 | 2.2 | Reject duplicate account code | BG-004 | Submit form with duplicate code; verify HTTP 422 and error message. |
| FR-ACCT-003 | 2.2 | Edit account name/sub-type/currency on accounts with no posted transactions | BG-003 | Edit account with zero posted lines; verify save succeeds. |
| FR-ACCT-004 | 2.2 | Prevent code/type change on accounts with posted transactions | BG-004 | Attempt code edit on account with journal lines; verify edit is blocked and error returned. |
| FR-ACCT-005 | 2.2 | Deactivate zero-balance account | BG-003 | Deactivate zero-balance account; verify it is absent from transaction drop-downs. |
| FR-ACCT-006 | 2.2 | Prevent deactivation of non-zero-balance account | BG-004 | Attempt deactivation on account with balance; verify HTTP 422. |
| FR-ACCT-007 | 2.3 | Enforce 3-level hierarchy | BG-002 | Attempt to create Account without Sub-group; verify rejection. |
| FR-ACCT-008 | 2.3 | Display hierarchical CoA tree | BG-002 | Navigate to CoA screen; verify tree indentation matches hierarchy levels. |
| FR-ACCT-009 | 2.3 | Create/rename/delete Groups and Sub-groups | BG-003 | Delete Sub-group containing active Account; verify block. |
| FR-ACCT-010 | 2.4 | CoA template selection at onboarding | BG-003 | Complete onboarding with Uganda profile; verify standard Uganda accounts are present. |
| FR-ACCT-011 | 2.4 | Modify localisation template accounts | BG-003 | Edit imported account name; verify save succeeds. |
| FR-ACCT-012 | 2.5 | Auto-create system accounts at onboarding | BG-001, BG-004 | Inspect tenant CoA post-onboarding; verify Retained Earnings, VAT Control, PAYE Payable accounts exist. |
| FR-ACCT-013 | 2.5 | Prevent deletion of system accounts | BG-001, BG-004 | Attempt delete on system account; verify controls are hidden and API rejects request. |
| FR-ACCT-014 | 2.5 | Visual indicator on system accounts | BG-004 | View CoA; verify lock icon present on all `is_system = true` accounts. |
| FR-ACCT-015 | 2.6 | Associate GL account with 1 currency | BG-001, BG-002 | Create account with foreign currency; verify balance appears in functional currency at period-end after rate application. |
| FR-ACCT-016 | 2.7 | Audit log on GL account changes | BG-004 | Edit account name; verify audit log entry with user_id, action, changed_fields, timestamp. |
| FR-ACCT-017 | 2.7 | View GL account audit history | BG-004 | Navigate to account detail; verify audit history table is present and populated. |
| FR-ACCT-018 | 3.2 | Create manual journal with mandatory fields | BG-003 | Submit valid journal; verify it appears in journal list with status Draft. |
| FR-ACCT-019 | 3.2 | Unlimited journal lines subject to balance | BG-003 | Submit journal with 20 lines summing to zero difference; verify posting succeeds. |
| FR-ACCT-020 | 3.2 | Save journal in Draft status | BG-003 | Save draft journal; verify it can be retrieved and edited before posting. |
| FR-ACCT-021 | 3.2 | Validate journal date against open period | BG-001, BG-004 | Post journal dated in hard-closed period; verify rejection per FR-ACCT-116. |
| FR-ACCT-022 | 3.2 | Auto-generate sequential reference JNL-{YYYY}-{NNNNNN} | BG-004 | Post journal without user reference; verify generated reference matches format. |
| FR-ACCT-023 | 3.3 | Reject unbalanced journal with HTTP 422 | BG-004 | Post journal with debit ≠ credit; verify HTTP 422 and specific error message. |
| FR-ACCT-024 | 3.3 | Real-time running totals on journal form | BG-003 | Add debit line; verify running total fields update immediately. |
| FR-ACCT-025 | 3.3 | Reject journal referencing deactivated account | BG-004 | Post journal with deactivated account; verify HTTP 422 identifying the line. |
| FR-ACCT-026 | 3.3 | Reject cross-tenant account reference | BG-004 | Inject cross-tenant account ID via API; verify HTTP 422. |
| FR-ACCT-027 | 3.4 | Auto-journal on sales invoice confirmation | BG-003 | Confirm sales invoice; verify GL journal posted to Revenue, VAT Control (Output), AR. |
| FR-ACCT-028 | 3.4 | Auto-journal on purchase invoice confirmation | BG-003 | Confirm purchase invoice; verify GL journal posted to expense/asset, VAT Control (Input), AP. |
| FR-ACCT-029 | 3.4 | Auto-journal on payment recording | BG-003 | Record payment; verify GL journal debits/credits bank and payable/receivable accounts. |
| FR-ACCT-030 | 3.4 | Auto-journal on payroll run confirmation | BG-001, BG-003 | Confirm payroll run; verify journal posts Salaries Expense, PAYE Payable, Bank/Cash. |
| FR-ACCT-031 | 3.4 | Tag auto-journals with source_module and source_document_id | BG-004 | Inspect auto-journal record; verify source_module and source_document_id fields populated. |
| FR-ACCT-032 | 3.4 | Prevent manual editing of auto-generated journals | BG-004 | Attempt edit on auto-journal via UI; verify edit controls absent and informational message shown. |
| FR-ACCT-033 | 3.5 | Create reversal journal dated first day of next period | BG-004 | Reverse posted journal; verify reversal journal has swapped amounts and correct date. |
| FR-ACCT-034 | 3.5 | Link reversal to original via reversal_of FK | BG-004 | Inspect reversal journal record; verify reversal_of field equals original journal ID. |
| FR-ACCT-035 | 3.5 | Prevent double reversal | BG-004 | Attempt reversal on a journal with status Reversed; verify action is blocked. |
| FR-ACCT-036 | 3.5 | Require reversal reason | BG-004 | Attempt reversal without reason; verify form validation blocks submission. |
| FR-ACCT-037 | 3.6 | Posted journals immutable at DB level | BG-004 | Attempt UPDATE on posted journal via application API; verify rejection. |
| FR-ACCT-038 | 3.6 | Hide Edit/Delete on posted journals | BG-004 | View posted journal in UI; verify only Reverse and View controls present. |
| FR-ACCT-039 | 3.7 | Audit fields on every posted journal | BG-004 | Post journal; verify created_by, posted_by, posted_at, source_module, ip_address all populated. |
| FR-ACCT-040 | 3.7 | Display audit trail in Posting History section | BG-004 | Open journal detail screen; verify Posting History section present with all audit fields. |
| FR-ACCT-041 | 3.7 | Audit log on reversal initiation | BG-004 | Initiate reversal; verify audit log entry with initiated_by, reason, both journal IDs. |
| FR-ACCT-042 | 3.7 | Journal Audit Log report for Finance Manager | BG-004 | Navigate to Journal Audit Log as Finance Manager; verify filterable by date, user, module, status. |
| FR-ACCT-043 | 4.2 | Generate Trial Balance for a period | BG-002 | Request Trial Balance for closed period; verify all non-zero accounts listed with correct totals. |
| FR-ACCT-044 | 4.2 | Filter Trial Balance by account type | BG-002 | Filter by Revenue; verify only Revenue accounts appear. |
| FR-ACCT-045 | 4.2 | Flag out-of-balance Trial Balance | BG-004 | Simulate imbalance via test data; verify banner error and system alert generated. |
| FR-ACCT-046 | 4.3 | Generate Income Statement with correct sections | BG-001, BG-002 | Generate Income Statement; verify all required sections present in correct order. |
| FR-ACCT-047 | 4.3 | Gross Profit calculation | BG-002 | Verify Gross Profit = Revenue − Cost of Goods Sold for known test data. |
| FR-ACCT-048 | 4.3 | EBITDA calculation | BG-002 | Verify EBITDA formula against known test data values. |
| FR-ACCT-049 | 4.3 | Net Profit calculation | BG-002 | Verify Net Profit formula against known test data values. |
| FR-ACCT-050 | 4.3 | Comparative Income Statement | BG-002 | Select Compare; verify current period, prior period, and variance columns present. |
| FR-ACCT-051 | 4.4 | Generate Balance Sheet with Assets = Liabilities + Equity | BG-001, BG-002 | Generate Balance Sheet; verify equation holds for known test data. |
| FR-ACCT-052 | 4.4 | Flag Balance Sheet imbalance | BG-004 | Simulate imbalance; verify error banner and system alert. |
| FR-ACCT-053 | 4.4 | Comparative Balance Sheet | BG-002 | Select Compare; verify current and prior-year balances displayed side by side. |
| FR-ACCT-054 | 4.5 | Generate Cash Flow Statement (IAS 7 indirect method) | BG-001, BG-002 | Generate Cash Flow; verify three sections present and opening/closing cash reconciles. |
| FR-ACCT-055 | 4.5 | Calculate Net Cash from Operating Activities | BG-002 | Verify operating activities calculation matches known test data. |
| FR-ACCT-056 | 4.5 | Cash-flow classification tag on GL accounts | BG-002 | Tag account as investing; verify it appears in Investing Activities section of Cash Flow. |
| FR-ACCT-057 | 4.6 | Comparative column vs. prior year | BG-002 | Generate any statement with Compare; verify prior year column aligns to configured FY start. |
| FR-ACCT-058 | 4.6 | Budget vs. Actual report | BG-002 | Generate report for approved budget period; verify actual, budget, and variance columns. |
| FR-ACCT-059 | 4.7 | Translate foreign-currency accounts to functional currency | BG-002 | Create foreign-currency account; verify consolidated statement uses platform exchange rate. |
| FR-ACCT-060 | 4.7 | Isolate currency translation gains/losses in equity | BG-001, BG-002 | Verify translation gain/loss appears as separate equity line per IFRS. |
| FR-ACCT-061 | 4.8 | Export statements to Excel (.xlsx) | BG-002 | Export Income Statement; verify .xlsx file with correct sections and subtotals. |
| FR-ACCT-062 | 4.8 | Export statements to PDF | BG-002 | Export Balance Sheet to PDF; verify tenant header, page numbers, and generation timestamp. |
| FR-ACCT-063 | 5.2 | Create bank account record | BG-003 | Create bank account; verify it appears in bank account list with correct fields. |
| FR-ACCT-064 | 5.2 | Link bank account to Asset-type GL account | BG-003 | Attempt link to Expense account; verify rejection. Link to Asset/Bank account; verify success. |
| FR-ACCT-065 | 5.2 | Deactivate zero-balance bank account | BG-003 | Deactivate bank account with zero GL balance; verify excluded from drop-downs. |
| FR-ACCT-066 | 5.3 | Accept CSV and OFX statement uploads | BG-003 | Upload valid CSV file; verify statement lines imported. |
| FR-ACCT-067 | 5.3 | Parse statement lines into reconciliation workspace | BG-003 | Upload statement; verify each line appears with date, description, debit, credit, reference. |
| FR-ACCT-068 | 5.3 | Reject malformed import file | BG-004 | Upload file with non-numeric amount; verify error with line number and field name. |
| FR-ACCT-069 | 5.3 | Prevent duplicate statement import (SHA-256 hash) | BG-004 | Import same file twice; verify warning on second import. |
| FR-ACCT-070 | 5.4 | Auto-match by amount, date ±3 days, reference | BG-003 | Import statement with matching GL lines; verify auto-matched pairs in Auto-Matched section. |
| FR-ACCT-071 | 5.4 | Display auto-matched pairs for user review | BG-003 | Verify auto-matched section shows each pair with confirm/reject controls. |
| FR-ACCT-072 | 5.4 | Leave unmatched items in Unreconciled section | BG-003 | Import statement with 1 unmatchable line; verify it appears in Unreconciled section. |
| FR-ACCT-073 | 5.5 | Manual match of bank line to GL lines | BG-003 | Manually select bank line and matching GL lines; verify match created when amounts equal. |
| FR-ACCT-074 | 5.5 | Unmatch any matched pair | BG-003 | Unmatch auto-matched pair; verify both lines return to Unreconciled. |
| FR-ACCT-075 | 5.6 | Generate Reconciliation Report | BG-002 | Request report; verify opening balance, cleared amounts, closing balance, bank balance, difference. |
| FR-ACCT-076 | 5.6 | List outstanding items in two sections | BG-002 | Verify Outstanding in GL and Outstanding in Bank sections with date, description, amount. |
| FR-ACCT-077 | 5.6 | Lock completed reconciliation (Finance Manager) | BG-004 | Lock reconciliation; verify matching/unmatching controls disabled and audit log entry created. |
| FR-ACCT-078 | 5.6 | Export Reconciliation Report to PDF and Excel | BG-002 | Export report; verify .xlsx and PDF files generated correctly. |
| FR-ACCT-079 | 6.2 | Configure VAT registration settings | BG-001 | Save VAT config; verify registration number, rate, and filing period stored. |
| FR-ACCT-080 | 6.2 | Default Uganda VAT rate 18% | BG-001 | Onboard Uganda tenant; verify VAT rate defaults to 18%. |
| FR-ACCT-081 | 6.2 | Support Standard, Zero, Exempt, Out of Scope tax codes | BG-001 | Apply each code to a transaction line; verify correct GL posting behaviour. |
| FR-ACCT-082 | 6.2 | Map tax codes to correct GL accounts | BG-001, BG-004 | Confirm sales invoice with Standard Rate line; verify VAT Control (Output) debited. |
| FR-ACCT-083 | 6.3 | Auto-calculate VAT on sales invoices | BG-001 | Save sales invoice; verify VAT = Net × Rate / 100 for each line. |
| FR-ACCT-084 | 6.3 | Auto-calculate input VAT on purchase invoices | BG-001 | Save purchase invoice; verify input VAT calculated per line. |
| FR-ACCT-085 | 6.3 | Display net, VAT, and gross on invoice lines | BG-001 | Open invoice; verify net, VAT, and gross fields visible on each line and footer totals. |
| FR-ACCT-086 | 6.3 | Post VAT to control accounts via sub-ledger journal | BG-001, BG-004 | Confirm invoice; verify auto-journal includes VAT Control line. |
| FR-ACCT-087 | 6.4 | Generate VAT Return with input/output/net | BG-001 | Generate return; verify Output Tax, Input Tax, Net VAT = Output − Input. |
| FR-ACCT-088 | 6.4 | Supporting schedule exportable to Excel | BG-001 | Export supporting schedule; verify invoice-level detail in .xlsx file. |
| FR-ACCT-089 | 6.4 | VAT audit trail to source transaction | BG-001, BG-004 | Inspect VAT posting; verify source_module and source_document_id populated. |
| FR-ACCT-090 | 6.4 | Flag missing/invalid tax codes in VAT Return | BG-001 | Include invoice with missing tax code; verify banner warning identifies invoice. |
| FR-ACCT-091 | 6.5 | EFRIS Integration toggle (deferred) | BG-001 | Toggle EFRIS enabled; verify flag stored; actual integration tested under FR-INTG series. |
| FR-ACCT-092 | 6.6 | Configure withholding tax rates per category | BG-001 | Create WHT category with 6% rate; verify rate stored against category. |
| FR-ACCT-093 | 6.6 | Auto-calculate and post WHT on purchase invoices | BG-001 | Create invoice for WHT vendor; verify WHT deducted from payable and posted to WHT Payable GL. |
| FR-ACCT-094 | 6.6 | Generate WHT report | BG-001 | Generate WHT report; verify vendor, category, invoice, amount, date columns and Excel export. |
| FR-ACCT-095 | 6.7 | Store PAYE band table (configuration only) | BG-001 | Edit PAYE band; verify updated thresholds stored and visible in config screen. |
| FR-ACCT-096 | 6.7 | Post PAYE to PAYE Payable GL via payroll journal | BG-001, BG-004 | Confirm payroll; verify journal line credits PAYE Payable account. |
| FR-ACCT-097 | 7.2 | Create budget for annual/quarterly/monthly period | BG-002 | Create annual budget; verify period type and FY alignment stored. |
| FR-ACCT-098 | 7.2 | Define budget lines by GL account and period | BG-002 | Add budget line for Revenue account, Jan; verify stored with correct amount. |
| FR-ACCT-099 | 7.3 | Provide downloadable budget import template | BG-002 | Download template; verify columns match account code, account name, and period months. |
| FR-ACCT-100 | 7.3 | Import budget lines from Excel | BG-002 | Upload valid template; verify import count reported and lines stored. |
| FR-ACCT-101 | 7.4 | Support multiple budget versions per period | BG-002 | Create Revised Q1 version; verify independent from Original version. |
| FR-ACCT-102 | 7.4 | Copy existing version as starting point | BG-002 | Copy Original to Revised; verify all lines pre-populated from source. |
| FR-ACCT-103 | 7.5 | 5-state approval workflow | BG-002, BG-004 | Step through Draft → Submitted → Approved → Locked; verify each transition logged. |
| FR-ACCT-104 | 7.5 | Prevent editing of Approved budget lines | BG-004 | Attempt edit on Approved budget line; verify edit controls hidden and API rejects. |
| FR-ACCT-105 | 7.5 | Locked budget lines immutable to all roles | BG-004 | Attempt edit as Super Admin on Locked budget; verify rejection. |
| FR-ACCT-106 | 7.6 | Variance Report with actual, budget, variance | BG-002 | Generate report; verify Variance% = (Actual − Budget) / Budget × 100 for known data. |
| FR-ACCT-107 | 7.6 | Filter Variance Report and export | BG-002 | Filter by account type; verify filtered results. Export to Excel and PDF; verify files. |
| FR-ACCT-108 | 8.2 | Auto-create 12 periods per FY at onboarding | BG-004 | Onboard tenant; verify 12 periods created with Open status aligned to configured FY start. |
| FR-ACCT-109 | 8.2 | Finance Manager sets period to Soft Closed | BG-004 | Set period Soft Closed as Finance Manager; verify status updated. |
| FR-ACCT-110 | 8.2 | Finance Manager sets period to Hard Closed | BG-004 | Set period Hard Closed; verify status updated and cannot be reversed by Finance Manager. |
| FR-ACCT-111 | 8.2 | Display period statuses on Period Management screen | BG-004 | Navigate to Period Management; verify all periods listed with status and current period highlighted. |
| FR-ACCT-112 | 8.3 | Modal warning on posting to Soft Closed period | BG-004 | Post transaction to soft-closed period; verify modal warning displayed before submission. |
| FR-ACCT-113 | 8.3 | Allow posting after soft-close confirmation with permission | BG-004 | Confirm override as user with `accounting.override_soft_close`; verify posting succeeds. |
| FR-ACCT-114 | 8.3 | Reject soft-close override without permission | BG-004 | Confirm override as user without permission; verify HTTP 422 with permission error. |
| FR-ACCT-115 | 8.3 | Audit event for soft-close override | BG-004 | Post under soft-close override; verify audit event with user, period, document, timestamp. |
| FR-ACCT-116 | 8.4 | Reject all postings to Hard Closed periods | BG-001, BG-004 | Attempt posting to hard-closed period as Super Admin; verify HTTP 422 with error message. |
| FR-ACCT-117 | 8.4 | Reject reconciliation operations in Hard Closed periods | BG-004 | Attempt bank match in hard-closed period; verify HTTP 422. |
| FR-ACCT-118 | 8.5 | Auto-post year-end retained earnings journal | BG-001, BG-002 | Close all 12 periods; initiate year-end close; verify retained earnings journal posted. |
| FR-ACCT-119 | 8.5 | Zero Revenue/Expense accounts after year-end close | BG-001 | After year-end close; verify Revenue and Expense accounts carry zero balance; verify BS accounts carry forward. |
| FR-ACCT-120 | 8.5 | Prevent year-end close with non-hard-closed periods | BG-004 | Initiate year-end close with 1 Open period; verify block and list of non-closed periods. |
| FR-ACCT-121 | 8.6 | Super Admin re-opens closed period with reason | BG-004 | Re-open closed period as Super Admin with reason; verify status reverts to Open. |
| FR-ACCT-122 | 8.6 | Audit event and notification on period re-open | BG-004 | Re-open period; verify audit event created and Finance Manager notification triggered. |

| FR-ACCT-123 | 8.7 | Define close templates by entity and close type | BG-005, BG-006 | Create month-end template with tasks, dependencies, and owner roles; verify template saves with all metadata. |
| FR-ACCT-124 | 8.7 | Instantiate close run from template | BG-005 | Launch close run for entity and period; verify task instances created in Not Started status. |
| FR-ACCT-125 | 8.7 | Support controlled close task statuses | BG-004, BG-005 | Set task to Blocked without comment; verify rejection. Repeat with comment; verify success. |
| FR-ACCT-126 | 8.7 | Assign or reassign close task ownership | BG-005 | Reassign task to another authorised owner; verify assignment changes and audit history preserved. |
| FR-ACCT-127 | 8.7 | Require evidence for evidence-required close tasks | BG-004, BG-005 | Attempt to complete evidence-required task without attachment, URL, or commentary; verify rejection. |
| FR-ACCT-128 | 8.7 | Block hard close until mandatory tasks resolved | BG-004, BG-005 | Attempt Hard Close with mandatory task still In Progress; verify block. |
| FR-ACCT-129 | 8.7 | Provide Close Cockpit dashboard | BG-005 | Open dashboard; verify completion %, overdue, blocked, and owner-level views are displayed. |
| FR-ACCT-130 | 8.7 | Notify on assignments, overdue tasks, blockers, and rejection | BG-005 | Mark task Blocked; verify owner and Finance Manager receive in-app notifications. |
| FR-ACCT-131 | 8.8 | Create recurring journal templates | BG-003, BG-005 | Save recurring journal template with monthly frequency and lines; verify template is stored and reusable. |
| FR-ACCT-132 | 8.8 | Generate draft journals from recurring templates | BG-003, BG-005 | Open new period with active templates; verify draft recurring journals are generated with template reference. |
| FR-ACCT-133 | 8.8 | Auto-reverse flagged close journals in next open period | BG-004, BG-005 | Post accrual with auto-reverse flag; verify reversal journal appears on first day of next open period. |
| FR-ACCT-134 | 8.8 | Enforce preparer-approver segregation for close journals and templates | BG-004 | Attempt self-approval on submitted close journal; verify approval is blocked. |
| FR-ACCT-135 | 8.8 | Require approval for high-value close journals | BG-004, BG-005 | Submit close journal above threshold; verify status requires approval before posting. |
| FR-ACCT-136 | 8.8 | Maintain mandatory close journal source classification | BG-004, BG-006 | Create close journal without source classification; verify validation fails. |
| FR-ACCT-137 | 8.8 | Provide Close Journal Register report | BG-002, BG-004 | Filter register by entity, source classification, and approver; verify results match stored journals. |
| FR-ACCT-138 | 8.9 | Track close readiness by entity and reporting basis | BG-005, BG-006 | Hard-close entity A and keep entity B Open for same period; verify both states persist independently. |
| FR-ACCT-139 | 8.9 | Require counterparty attribution on intercompany journals | BG-004, BG-006 | Attempt intercompany journal without counterparty entity; verify rejection. |
| FR-ACCT-140 | 8.9 | Provide Intercompany Mismatch report | BG-002, BG-006 | Create unmatched intercompany balances; verify report lists entity, counterparty, account, currency, and period. |
| FR-ACCT-141 | 8.9 | Preserve separate journal layers for local and group reporting | BG-004, BG-006 | Post journals across LocalStatutory and Elimination layers; verify reports can filter by layer without changing local journals. |
| FR-ACCT-142 | 8.9 | Restrict elimination journals to group-finance permission | BG-004, BG-006 | Attempt elimination journal as user without permission; verify rejection. |
| FR-ACCT-143 | 8.9 | Generate Consolidation Input Trial Balance | BG-002, BG-006 | Generate consolidation input TB for group period; verify balances are grouped by entity, currency, account, and layer. |
| FR-ACCT-144 | 8.9 | Preserve source linkage for topside and elimination journals | BG-004, BG-006 | Open elimination journal detail; verify source references to contributing balances or intercompany pair are visible. |
| FR-ACCT-145 | 8.10 | Maintain Close Pack register for required outputs | BG-002, BG-005 | Open close pack for period; verify required reports and statuses are listed. |
| FR-ACCT-146 | 8.10 | Stamp generated finance reports with metadata | BG-002, BG-004 | Generate report; verify entity, period, basis, user, timestamp, and parameters are embedded. |
| FR-ACCT-147 | 8.10 | Freeze reproducible final report snapshots | BG-002, BG-004, BG-005 | Mark report Final, then regenerate with same parameters; verify values match until period is reopened. |
| FR-ACCT-148 | 8.10 | Require Finance Manager sign-off for final Close Pack | BG-004, BG-005 | Attempt to mark Close Pack Final without Finance Manager sign-off; verify rejection. |
| FR-ACCT-149 | 11.2 | Maintain governed bank-account master data | BG-003, BG-004 | Create bank account without account purpose or approver role; verify validation rejects the save. |
| FR-ACCT-150 | 11.2 | Segregate payment initiation, approval, and bank-file release roles | BG-004 | Attempt to approve and release a payment batch as the same user where SoD is enforced; verify release is blocked. |
| FR-ACCT-151 | 11.2 | Forecast cash position from approved obligations and expected receipts | BG-002, BG-003 | Generate 13-week cash forecast; verify balances reflect approved AP, payroll, and AR due buckets. |
| FR-ACCT-152 | 11.2 | Preserve liquidity tagging for bank accounts and cash movements | BG-002, BG-004 | Post movement tagged OperatingCash; verify cash report filters by liquidity bucket without altering the journal. |
| FR-ACCT-153 | 11.3 | Build governed payment batches from approved source obligations | BG-003, BG-004 | Create payment batch including unapproved invoice; verify inclusion is rejected. |
| FR-ACCT-154 | 11.3 | Generate bank files with immutable batch-to-file traceability | BG-004 | Generate bank file for approved batch; verify file hash, generator, timestamp, and source batch references are stored. |
| FR-ACCT-155 | 11.3 | Prevent duplicate bank-file release for the same payment instruction set | BG-004 | Attempt second file generation for already released batch without recall; verify rejection. |
| FR-ACCT-156 | 11.3 | Reconcile bank-file outcomes to payment instructions and journals | BG-003, BG-004 | Import bank response with one rejected payment; verify batch line is marked failed and linked journal remains unresolved. |
| FR-ACCT-157 | 11.3 | Maintain positive-pay or payment confirmation evidence | BG-004 | Attach bank confirmation to released batch; verify evidence is viewable from batch and audit history. |
| FR-ACCT-158 | 11.4 | Enforce daily or configured reconciliation cadence per bank account | BG-003, BG-005 | Leave daily-reconciled account unreconciled past cadence; verify exception appears on finance cockpit. |
| FR-ACCT-159 | 11.4 | Age unreconciled bank and GL items | BG-002, BG-005 | Open reconciliation workspace; verify unreconciled items show age buckets by statement or posting date. |
| FR-ACCT-160 | 11.4 | Escalate stale reconciling items for review | BG-004, BG-005 | Leave reconciling item unresolved beyond threshold; verify escalation notification to Finance Manager. |
| FR-ACCT-161 | 11.4 | Certify reconciliation completion by authorised reviewer | BG-004 | Attempt certification by preparer where reviewer is required; verify certification is blocked. |
| FR-ACCT-162 | 11.5 | Capitalise fixed assets from approved acquisition events | BG-001, BG-003, BG-004 | Confirm asset acquisition with capitalization flag; verify asset record and capitalization journal are created. |
| FR-ACCT-163 | 11.5 | Maintain asset accounting books and depreciation methods | BG-001, BG-002 | Configure straight-line depreciation for accounting book; verify schedule is generated for useful life and salvage value. |
| FR-ACCT-164 | 11.5 | Post periodic depreciation automatically or by controlled run | BG-002, BG-003, BG-004 | Execute depreciation run for open period; verify expense and accumulated depreciation journals are posted once only. |
| FR-ACCT-165 | 11.5 | Support impairment, reclassification, and transfer journals with audit trail | BG-001, BG-004 | Post impairment adjustment; verify carrying amount updates and reason, approver, and evidence are preserved. |
| FR-ACCT-166 | 11.5 | Support asset retirement and disposal accounting | BG-001, BG-002, BG-004 | Retire asset with disposal proceeds; verify cost, accumulated depreciation, gain/loss, and cash entries are recognised correctly. |
| FR-ACCT-167 | 11.5 | Reconcile asset subledger to general ledger by period | BG-002, BG-004, BG-005 | Run asset-to-GL reconciliation; verify difference report identifies book, account, and asset contributors. |
| FR-ACCT-168 | 11.6 | Maintain ownership hierarchy for group reporting entities | BG-002, BG-006 | Save parent-child ownership structure with effective dates; verify group tree renders correctly for the selected period. |
| FR-ACCT-169 | 11.6 | Preserve FX translation inputs and translated balances by reporting basis | BG-001, BG-002, BG-006 | Run translation for group period; verify closing-rate and average-rate inputs are stored with translated trial balance. |
| FR-ACCT-170 | 11.6 | Govern intercompany settlement lifecycle | BG-003, BG-004, BG-006 | Match intercompany payable and receivable for settlement; verify unresolved differences remain open and reported. |
| FR-ACCT-171 | 11.6 | Govern elimination and top-side adjustment journals separately from local books | BG-004, BG-006 | Post top-side adjustment without group-finance approval; verify posting is blocked. |
| FR-ACCT-172 | 11.6 | Produce certified group close pack with entity submissions, eliminations, and sign-offs | BG-002, BG-004, BG-005, BG-006 | Mark group close pack final; verify required entity submissions, elimination journals, approvals, and certification evidence exist. |

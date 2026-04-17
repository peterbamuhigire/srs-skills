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

# 4. Core Module Requirements Traceability

This section covers the 4 core modules included in every Longhorn ERP subscription: Accounting and General Ledger, Inventory Management, Sales, and Procurement.

*Note: Each module SRS defines local business goals. These local goals map to PRD goals as follows: accounting BG-001 (statutory compliance) → PRD BG-002; BG-002 (management reporting) → PRD BG-004; BG-003 (operational efficiency) → PRD BG-001; BG-004 (audit readiness) → PRD BG-002. Sales BG-001 (revenue recognition) → PRD BG-001, BG-004; BG-002 (cash collection) → PRD BG-004; BG-003 (customer relationship) → PRD BG-001; BG-004 (regulatory compliance) → PRD BG-002.*

## 4.1 Accounting and General Ledger (FR-ACCT-*)

*Source: `02-requirements-engineering/01-srs/01-modules/01-accounting/10-traceability.md`*

*Test cases TC-ACCT-001 through TC-ACCT-010 are defined in the test plan. All other accounting FRs are flagged TC-PENDING.*

| FR ID | Description (brief) | Business Goal(s) | Test Case(s) | Gaps |
|---|---|---|---|---|
| FR-ACCT-001 | Create GL account with mandatory fields | BG-001 | TC-ACCT-001 | |
| FR-ACCT-002 | Reject duplicate account code | BG-002 | TC-ACCT-002 | |
| FR-ACCT-003 | Edit account name/sub-type/currency on zero-transaction accounts | BG-001 | TC-ACCT-003 | |
| FR-ACCT-004 | Prevent code/type change on accounts with posted transactions | BG-002 | TC-ACCT-004 | |
| FR-ACCT-005 | Deactivate zero-balance account | BG-001 | TC-ACCT-005 | |
| FR-ACCT-006 | Prevent deactivation of non-zero-balance account | BG-002 | TC-ACCT-006 | |
| FR-ACCT-007 | Enforce 3-level account hierarchy | BG-004 | TC-ACCT-007 | |
| FR-ACCT-008 | Display hierarchical COA tree | BG-004 | TC-ACCT-008 | |
| FR-ACCT-009 | Create, rename, and delete Groups and Sub-groups | BG-001 | TC-ACCT-009 | |
| FR-ACCT-010 | COA template selected at onboarding | BG-001 | TC-ACCT-010 | |
| FR-ACCT-011 | Modify localisation template accounts after import | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ACCT-012 | Auto-create system accounts at onboarding | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ACCT-013 | Prevent deletion of system accounts | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ACCT-014 | Visual indicator on system accounts | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ACCT-015 | Associate GL account with 1 currency | BG-003, BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ACCT-016 | Audit log on GL account changes | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ACCT-017 | View GL account audit history | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ACCT-018 | Create manual journal with mandatory fields | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ACCT-019 | Unlimited journal lines subject to debit = credit balance | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ACCT-020 | Save journal in Draft status | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ACCT-021 | Validate journal date against open period | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ACCT-022 | Auto-generate sequential reference JNL-{YYYY}-{NNNNNN} | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ACCT-023 | Reject unbalanced journal with HTTP 422 | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ACCT-024 | Real-time running totals on journal form | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ACCT-025 | Reject journal referencing deactivated account | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ACCT-026 | Reject cross-tenant account reference | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ACCT-027 | Auto-journal on sales invoice confirmation | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ACCT-028 | Auto-journal on purchase invoice confirmation | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ACCT-029 | Auto-journal on payment recording | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ACCT-030 | Auto-journal on payroll run confirmation | BG-001, BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ACCT-031 | Tag auto-journals with source_module and source_document_id | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ACCT-032 | Prevent manual editing of auto-generated journals | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ACCT-033 | Create reversal journal dated first day of next period | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ACCT-034 | Link reversal to original via reversal_of FK | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ACCT-035 | Prevent double reversal | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ACCT-036 | Require reversal reason | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ACCT-037 | Posted journals immutable at DB level | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ACCT-038 | Hide Edit/Delete on posted journals | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ACCT-039 | Audit fields populated on every posted journal | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ACCT-040 | Audit trail displayed in Posting History section | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ACCT-041 | Audit log on reversal initiation | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ACCT-042 | Journal Audit Log report for Finance Manager | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ACCT-043 | Generate Trial Balance for a period | BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ACCT-044 | Filter Trial Balance by account type | BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ACCT-045 | Flag out-of-balance Trial Balance | BG-002, BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ACCT-046 | Generate Income Statement with correct sections | BG-002, BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ACCT-047 | Gross Profit calculation | BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ACCT-048 | EBITDA calculation | BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ACCT-049 | Net Profit calculation | BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ACCT-050 | Comparative Income Statement with prior period | BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ACCT-051 | Generate Balance Sheet with Assets = Liabilities + Equity | BG-002, BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ACCT-052 | Flag Balance Sheet imbalance | BG-002, BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ACCT-053 | Comparative Balance Sheet | BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ACCT-054 | Generate Cash Flow Statement per IAS 7 indirect method | BG-002, BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ACCT-055 | Calculate Net Cash from Operating Activities | BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ACCT-056 | Cash-flow classification tag on GL accounts | BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ACCT-057 | Comparative column vs. prior year on all statements | BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ACCT-058 | Budget vs. Actual report | BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ACCT-059 | Translate foreign-currency accounts to functional currency | BG-003, BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ACCT-060 | Isolate currency translation gains/losses in equity | BG-002, BG-003, BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ACCT-061 | Export statements to Excel (.xlsx) | BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ACCT-062 | Export statements to PDF | BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ACCT-063 | Create bank account record | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ACCT-064 | Link bank account to Asset-type GL account | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ACCT-065 | Deactivate zero-balance bank account | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ACCT-066 | Accept CSV and OFX statement uploads | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ACCT-067 | Parse statement lines into reconciliation workspace | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ACCT-068 | Reject malformed import file | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ACCT-069 | Prevent duplicate statement import via SHA-256 hash | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ACCT-070 | Auto-match by amount, date ±3 days, reference | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ACCT-071 | Display auto-matched pairs for user review | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ACCT-072 | Leave unmatched items in Unreconciled section | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ACCT-073 | Manual match of bank line to GL lines | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ACCT-074 | Unmatch any matched pair | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ACCT-075 | Generate Reconciliation Report | BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ACCT-076 | List outstanding items in two sections | BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ACCT-077 | Lock completed reconciliation (Finance Manager only) | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ACCT-078 | Export Reconciliation Report to PDF and Excel | BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ACCT-079 | Configure VAT registration settings | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ACCT-080 | Default Uganda VAT rate 18% | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ACCT-081 | Support Standard, Zero, Exempt, Out of Scope tax codes | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ACCT-082 | Map tax codes to correct GL accounts | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ACCT-083 | Auto-calculate VAT on sales invoices | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ACCT-084 | Auto-calculate input VAT on purchase invoices | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ACCT-085 | Display net, VAT, and gross on invoice lines | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ACCT-086 | Post VAT to control accounts via sub-ledger journal | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ACCT-087 | Generate VAT Return with input/output/net | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ACCT-088 | Supporting schedule exportable to Excel | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ACCT-089 | VAT audit trail to source transaction | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ACCT-090 | Flag missing/invalid tax codes in VAT Return | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ACCT-091 | EFRIS Integration toggle (deferred to Integration Layer) | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ACCT-092 | Configure withholding tax rates per category | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ACCT-093 | Auto-calculate and post WHT on purchase invoices | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ACCT-094 | Generate WHT report | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ACCT-095 | Store PAYE band table (configuration only) | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ACCT-096 | Post PAYE to PAYE Payable GL via payroll journal | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ACCT-097 | Create budget for annual/quarterly/monthly period | BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ACCT-098 | Define budget lines by GL account and period | BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ACCT-099 | Provide downloadable budget import template | BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ACCT-100 | Import budget lines from Excel | BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ACCT-101 | Support multiple budget versions per period | BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ACCT-102 | Copy existing budget version as starting point | BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ACCT-103 | 5-state budget approval workflow | BG-002, BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ACCT-104 | Prevent editing of Approved budget lines | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ACCT-105 | Locked budget lines immutable to all roles | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ACCT-106 | Variance Report with actual, budget, and variance % | BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ACCT-107 | Filter Variance Report by account type; export | BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ACCT-108 | Auto-create 12 periods per FY at onboarding | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ACCT-109 | Finance Manager sets period to Soft Closed | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ACCT-110 | Finance Manager sets period to Hard Closed | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ACCT-111 | Display period statuses on Period Management screen | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ACCT-112 | Modal warning on posting to Soft Closed period | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ACCT-113 | Allow posting after soft-close confirmation with permission | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ACCT-114 | Reject soft-close override without permission | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ACCT-115 | Audit event for soft-close override | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ACCT-116 | Reject all postings to Hard Closed periods | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ACCT-117 | Reject reconciliation operations in Hard Closed periods | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ACCT-118 | Auto-post year-end retained earnings journal | BG-002, BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ACCT-119 | Zero Revenue/Expense accounts after year-end close | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ACCT-120 | Prevent year-end close with non-hard-closed periods | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ACCT-121 | Super Admin re-opens closed period with reason | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-ACCT-122 | Audit event and notification on period re-open | BG-002 | TC-PENDING | [TRACE-GAP-TC] |

## 4.2 Inventory Management (FR-INV-*)

*Source: `02-requirements-engineering/01-srs/01-modules/02-inventory/09-traceability.md`*

*Test cases TC-INV-001 through TC-INV-005 are defined in the test plan. All other inventory FRs are flagged TC-PENDING.*

*BG mapping: Inventory BG-001 (Operational Accuracy) → PRD BG-001; BG-002 (Financial Compliance) → PRD BG-002; BG-003 (Supply Chain Efficiency) → PRD BG-001; BG-004 (Audit Readiness) → PRD BG-002.*

| FR ID | Description (brief) | Business Goal(s) | Test Case(s) | Gaps |
|---|---|---|---|---|
| FR-INV-001 | Create item master record | BG-001 | TC-INV-001 | |
| FR-INV-002 | Enforce item code uniqueness | BG-001 | TC-INV-002 | |
| FR-INV-003 | Support stocked, service, and composite item types | BG-001 | TC-INV-003 | |
| FR-INV-004 | Multi-level category hierarchy | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INV-005 | Multiple units of measure per item | BG-001 | TC-INV-004 | |
| FR-INV-006 | UOM conversion on movement posting | BG-001, BG-002 | TC-INV-005 | |
| FR-INV-007 | GS1 barcode validation | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INV-008 | Item attributes including shelf life and reorder point | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INV-009 | Item image attachments | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INV-010 | Item soft-delete with history preservation | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INV-011 | Item variant creation | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INV-012 | Variant UOM consistency | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INV-013 | Variant matrix display | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INV-014 | Composite item BOM definition | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INV-015 | Block deletion of items with movements | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INV-016 | Item master audit metadata | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INV-017 | Bulk CSV item import | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INV-018 | Custom item attributes | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INV-019 | Warehouse-level reorder settings | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INV-020 | Auto-numbering for item codes | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INV-021 | Create warehouse record | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INV-022 | Warehouse type restrictions | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INV-023 | Bin-location tracking per warehouse | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INV-024 | Bin creation within warehouse | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INV-025 | Default warehouse per branch | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INV-026 | Warehouse override permission | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INV-027 | Inter-branch Transfer Order creation | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INV-028 | Transfer Order status workflow | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INV-029 | Auto-post transfer journal entry | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INV-030 | Consignment stock segregation | BG-001, BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INV-031 | Move stock to quarantine | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INV-032 | Quarantine resolution (dispose or restore) | BG-001, BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INV-033 | Real-time stock balance inquiry | BG-001, BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INV-034 | Block warehouse deletion with active stock | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INV-035 | Warehouse configuration audit log | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INV-036 | Immutable movement ledger entry | BG-001, BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INV-037 | FIFO cost layer created on receipt | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INV-038 | WAC recalculated on receipt | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INV-039 | FEFO picking strategy | BG-001, BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INV-040 | Block negative stock with HTTP 422 | BG-001, BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INV-041 | Allow negative stock (configurable per tenant) | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INV-042 | Stock adjustment authorisation | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INV-043 | Adjustment journal entry posted | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INV-044 | Opening balance movement type | BG-001, BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INV-045 | Landed cost allocated across GRN lines | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INV-046 | Landed cost allocation method recorded | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INV-047 | Prevent editing of posted movements | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INV-048 | Purchase return movement auto-generated | BG-001, BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INV-049 | Sales return movement and COGS reversal | BG-001, BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INV-050 | Item ledger inquiry with running balance | BG-001, BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INV-051 | UOM conversion applied on ledger write | BG-001, BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INV-052 | Unique movement ID assigned | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INV-053 | Draft vs. posted movement distinction | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INV-054 | Min stock level notification on movement post | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INV-055 | Batch/lot number recorded on movement | BG-001, BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INV-056 | Valuation method assigned per item or tenant | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INV-057 | Block valuation method change post-movement | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INV-058 | FIFO cost layer table structure maintained | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INV-059 | FIFO/FEFO layer consumption order enforced | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INV-060 | COGS calculated and posted | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INV-061 | WAC recalculation stored | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INV-062 | WAC used as COGS unit cost on issue | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INV-063 | NRV write-down entry recorded | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INV-064 | NRV write-down journal entry posted | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INV-065 | Cost revaluation with variance journal | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INV-066 | Stock Valuation Report | BG-002, BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INV-067 | Landed cost included in carrying value | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INV-068 | Initiate full or cycle stock take | BG-001, BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INV-069 | Freeze movements during active stock take | BG-001, BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INV-070 | Printable count sheets generated | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INV-071 | Mobile/web count entry supported | BG-001, BG-005 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INV-072 | Double-blind count workflow | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INV-073 | Variance calculated per stock take line | BG-001, BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INV-074 | Financial impact of variances computed | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INV-075 | Stock take approver authorisation required | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INV-076 | Auto-create adjustment movements on approval | BG-001, BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INV-077 | Release movement freeze on stock take completion | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INV-078 | Stock take history record retained | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INV-079 | ABC classification report | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INV-080 | Reorder point evaluation triggered post-movement | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INV-081 | Reorder alert sent to purchasing officers | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INV-082 | Critical stock alert sent to purchasing manager | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INV-083 | Auto-generate draft Purchase Requisition on reorder | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INV-084 | Suppress duplicate reorder alerts | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INV-085 | Reorder Report by warehouse | BG-001, BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INV-086 | Days of Supply calculated per item | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-INV-087 | Projected stockout date shown on Reorder Report | BG-001 | TC-PENDING | [TRACE-GAP-TC] |

## 4.3 Sales (FR-SALES-*)

*Source: `02-requirements-engineering/01-srs/01-modules/03-sales/10-traceability.md`*

*Test cases TC-SALES-001 through TC-SALES-003 are defined in the test plan. All other sales FRs are flagged TC-PENDING.*

*BG mapping: Sales BG-001 (Revenue Recognition) → PRD BG-001, BG-004; BG-002 (Cash Collection) → PRD BG-004; BG-003 (Customer Relationship) → PRD BG-001; BG-004 (Regulatory Compliance) → PRD BG-002.*

| FR ID | Description (brief) | Business Goal(s) | Test Case(s) | Gaps |
|---|---|---|---|---|
| FR-SALES-001 | Create customer record with TIN, VAT status, credit terms | BG-001, BG-002 | TC-SALES-001 | |
| FR-SALES-002 | Assign customer category and default price list | BG-001 | TC-SALES-002 | |
| FR-SALES-003 | Duplicate TIN detection | BG-001, BG-002 | TC-SALES-003 | |
| FR-SALES-004 | Duplicate phone detection | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-SALES-005 | Customer balance summary displayed | BG-001, BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-SALES-006 | Credit limit enforced on invoicing | BG-001, BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-SALES-007 | Customer statement generation | BG-001, BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-SALES-008 | Statement includes opening balance, transactions, closing balance | BG-001, BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-SALES-009 | Statement PDF generation at P95 ≤ 5 s | BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-SALES-010 | Customer soft-delete (deactivation) | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-SALES-011 | Block deactivation with outstanding balance | BG-001, BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-SALES-012 | Customer reactivation | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-SALES-013 | Customer record audit log | BG-001, BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-SALES-014 | Customer search | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-SALES-015 | Credit terms displayed on invoice creation | BG-001, BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-SALES-016 | Create multiple price lists per tenant | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-SALES-017 | Price list lines with effective and expiry dates | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-SALES-018 | Activate/deactivate price list lines by date | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-SALES-019 | Quantity-based discount tiers | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-SALES-020 | Price list priority resolution | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-SALES-021 | Auto-populate price on transaction line | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-SALES-022 | Price override with audit log | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-SALES-023 | Price history retention | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-SALES-024 | Price lookup at P95 ≤ 500 ms | BG-001, BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-SALES-025 | Block deletion of in-use price list | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-SALES-026 | Create quotation with lines, tax, and totals | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-SALES-027 | Quotation status lifecycle and expiry | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-SALES-028 | Quotation status change history | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-SALES-029 | Lock accepted/rejected/expired quotations | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-SALES-030 | Quotation PDF generation | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-SALES-031 | Convert quotation to Sales Order | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-SALES-032 | Link SO back to originating quotation | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-SALES-033 | Create Sales Order with fulfilment tracking | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-SALES-034 | Stock reservation on SO confirmation | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-SALES-035 | Configurable SO approval workflow | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-SALES-036 | Track qty ordered/delivered/invoiced per SO line | BG-001, BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-SALES-037 | SO line fulfilment status | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-SALES-038 | Back-order created on partial delivery | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-SALES-039 | SO cancellation and stock release | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-SALES-040 | Block over-invoicing without override | BG-001, BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-SALES-041 | Support 3 invoice types (Standard, Pro-Forma, Recurring) | BG-001, BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-SALES-042 | Standard Invoice ledger posting | BG-001, BG-002, BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-SALES-043 | Pro-Forma Invoice non-posting rule | BG-001, BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-SALES-044 | Create invoice from 3 source types | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-SALES-045 | Invoice line calculation formula | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-SALES-046 | VAT auto-applied per tax code | BG-001, BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-SALES-047 | Tenant-configurable invoice numbering | BG-001, BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-SALES-048 | Credit limit checked on invoice save | BG-001, BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-SALES-049 | Invoice approval workflow | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-SALES-050 | Approver notification on invoice submission | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-SALES-051 | EFRIS submission flag for Uganda tenants | BG-001, BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-SALES-052 | Display EFRIS status and QR code on invoice | BG-001, BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-SALES-053 | Invoice PDF generation at P95 ≤ 3 s | BG-001, BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-SALES-054 | Embed EFRIS QR code in PDF | BG-001, BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-SALES-055 | Configure recurring invoice template | BG-001, BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-SALES-056 | Auto-generate recurring invoice on schedule | BG-001, BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-SALES-057 | Auto-send recurring invoice by email | BG-001, BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-SALES-058 | Daily recurring invoice admin alert | BG-001, BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-SALES-059 | Create Delivery Note from SO or invoice | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-SALES-060 | Capture dispatch qty, warehouse, bin per DN line | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-SALES-061 | Post DN: reduce inventory, create stock movement | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-SALES-062 | Block DN posting if insufficient stock | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-SALES-063 | Auto-create back-order on partial delivery | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-SALES-064 | Delivery Note PDF generation | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-SALES-065 | Proof of delivery capture (signature or upload) | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-SALES-066 | Display POD status on DN and SO | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-SALES-067 | System-generated DN numbering | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-SALES-068 | Link DN to SO; update SO fulfilment in real time | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-SALES-069 | Cancel DN and reverse stock movement | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-SALES-070 | Block DN cancellation if invoiced | BG-001, BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-SALES-071 | Create Sales Return referencing source document | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-SALES-072 | Capture return qty, reason, and destination warehouse | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-SALES-073 | Sales Return approval workflow | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-SALES-074 | Auto-generate Credit Note on return approval | BG-001, BG-002, BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-SALES-075 | Post return stock receipt to Inventory | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-SALES-076 | System-generated Credit Note numbering | BG-001, BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-SALES-077 | Allocate Credit Note to open invoices | BG-001, BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-SALES-078 | Hold unapplied Credit Note as customer credit | BG-001, BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-SALES-079 | Credit Note PDF generation | BG-001, BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-SALES-080 | Post Credit Note to AR ledger | BG-001, BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-SALES-081 | Create payment receipt with method and reference | BG-001, BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-SALES-082 | System-generated receipt numbering | BG-001, BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-SALES-083 | Allocate receipt to open invoices | BG-001, BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-SALES-084 | Reduce invoice balance and post to AR ledger | BG-001, BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-SALES-085 | Hold unallocated receipt as customer credit | BG-001, BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-SALES-086 | Retrospective receipt allocation | BG-001, BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-SALES-087 | Restrict reversal of fully allocated receipts | BG-001, BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-SALES-088 | Debtors aging report with 5 buckets | BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-SALES-089 | Filter aging report by customer, category, sales rep | BG-001, BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-SALES-090 | Aging report at P95 ≤ 8 s | BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-SALES-091 | Aging report: credit limit vs. balance column | BG-001, BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-SALES-092 | Export aging report to PDF and Excel | BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-SALES-093 | Flag invoice as Overdue | BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-SALES-094 | Send overdue email reminder to customer | BG-001, BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-SALES-095 | Configure overdue alert schedule | BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-SALES-096 | Record overdue alert history per invoice | BG-002, BG-004 | TC-PENDING | [TRACE-GAP-TC] |

## 4.4 Procurement (FR-PROC-*)

*Source: `02-requirements-engineering/01-srs/01-modules/04-procurement/10-traceability.md`*

*The Procurement SRS traceability file uses range notation. All 51 FRs are covered. BG mapping: Procurement BG-001 (operational efficiency) → PRD BG-001; BG-002 (PPDA compliance) → PRD BG-002; BG-003 (supplier relationships) → PRD BG-001; BG-004 (audit readiness) → PRD BG-002.*

| FR ID | Description (brief) | Business Goal(s) | Test Case(s) | Gaps |
|---|---|---|---|---|
| FR-PROC-001 | Enforce unique supplier identification (name + TIN) | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PROC-002 | Supplier mandatory fields enforced at creation | BG-001, BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PROC-003 | Supplier bank account details recorded | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PROC-004 | Supplier record update audit trail | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PROC-005 | Inactive supplier blocked from new purchase transactions | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PROC-006 | Supplier search performance within threshold | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PROC-007 | Supplier category hierarchy | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PROC-008 | Supplier import via CSV with validation | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PROC-009 | Purchase Requisition creation with mandatory fields | BG-001, BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PROC-010 | PR approval workflow | BG-001, BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PROC-011 | PR conversion to RFQ or PO | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PROC-012 | PPDA threshold check on PR approval | BG-001, BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PROC-013 | RFQ dispatched to multiple suppliers | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PROC-014 | RFQ responses captured per supplier | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PROC-015 | Supplier quote comparison matrix | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PROC-016 | Awarded supplier selected from comparison | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PROC-017 | Purchase Order creation with mandatory fields | BG-001, BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PROC-018 | PO approval workflow | BG-001, BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PROC-019 | PO issued to supplier (email or PDF) | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PROC-020 | PO status tracked through fulfilment | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PROC-021 | PO line amendment workflow | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PROC-022 | PO cancellation with stock reversal | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PROC-023 | PO closure on full receipt | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PROC-024 | PO amendments audited | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PROC-025 | GRN created against PO | BG-001, BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PROC-026 | GRN partial receipt supported | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PROC-027 | Landed cost entry on GRN | BG-001, BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PROC-028 | GRN stock movement posted to Inventory | BG-001, BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PROC-029 | GRN return workflow | BG-001, BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PROC-030 | GRN mobile capture supported | BG-001, BG-005 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PROC-031 | GRN audit trail | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PROC-032 | Supplier invoice captured against PO/GRN | BG-001, BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PROC-033 | Invoice validation against PO price and quantity | BG-001, BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PROC-034 | 3-way match (PO / GRN / Invoice) enforced | BG-001, BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PROC-035 | WHT auto-calculated on supplier invoice | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PROC-036 | WHT default rate 6% for Uganda tenants | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PROC-037 | Supplier credit note processed against invoice | BG-001, BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PROC-038 | Supplier payment recorded with method | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PROC-039 | Allocate payment to outstanding invoices | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PROC-040 | Payment run batch generation | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PROC-041 | Payment run approval workflow | BG-001, BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PROC-042 | Mobile money disbursement via payment run | BG-001, BG-005 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PROC-043 | Payment reconciliation with bank statement | BG-001 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PROC-044 | Creditors aging report | BG-001, BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PROC-045 | Creditors aging export to PDF and Excel | BG-001, BG-004 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PROC-046 | PPDA open-tendering rule enforced above threshold | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PROC-047 | PPDA prequalified supplier list maintained | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PROC-048 | PPDA procurement method recorded per PR | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PROC-049 | PPDA compliance report generated | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PROC-050 | PPDA documentation uploaded per procurement | BG-002 | TC-PENDING | [TRACE-GAP-TC] |
| FR-PROC-051 | PPDA workflow bypassed for commercial tenants | BG-001, BG-002 | TC-PENDING | [TRACE-GAP-TC] |

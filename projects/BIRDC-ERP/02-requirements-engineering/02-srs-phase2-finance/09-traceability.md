# 8. Verification and Traceability Matrix

## 8.1 Requirements Count Summary

| Module | Requirement Range | Count |
|---|---|---|
| F-005 Financial Accounting and General Ledger | FR-GL-001 to FR-GL-040 | 40 |
| F-006 Accounts Receivable | FR-AR-001 to FR-AR-025 | 25 |
| F-007 Accounts Payable | FR-AP-001 to FR-AP-030 | 30 |
| F-008 Budget Management | FR-BDG-001 to FR-BDG-021 | 21 |
| Non-Functional Requirements | NFR-PERF-001 to NFR-USE-003 | 17 |
| **Total** | | **133** |

## 8.2 Functional Requirements Traceability Matrix — F-005 General Ledger

| FR ID | Business Goal (Vision.md) | Business Rule | Design Covenant | Test Oracle (Pass/Fail) |
|---|---|---|---|---|
| FR-GL-001 | Financial integrity | — | DC-002, DC-003 | POST control account → HTTP 422 `ERR_CONTROL_ACCOUNT` |
| FR-GL-002 | Financial integrity | — | DC-003 | Change type of posted account → HTTP 422 `ERR_ACCOUNT_IMMUTABLE_AFTER_POST` |
| FR-GL-003 | Financial integrity | — | DC-001 | Full 1,307-account CoA renders ≤ 800 ms |
| FR-GL-004 | Financial integrity | — | DC-003 | Deactivate non-zero-balance account → HTTP 422 |
| FR-GL-005 | Dual-mode accounting | DC-004 | DC-004 | Dual-mapped transaction appears in both parliamentary and IFRS reports |
| FR-GL-006 | Financial integrity | BR-009 | DC-001, DC-003 | Unbalanced JE → HTTP 422 `ERR_UNBALANCED_JE`; zero DB writes |
| FR-GL-007 | Financial integrity | BR-003 | DC-003 | Creator attempts self-approval → HTTP 403 `ERR_SOD_VIOLATION` |
| FR-GL-008 | Financial integrity | BR-009, BR-013 | DC-003 | JE-YYYY-NNNN sequential; hash equals SHA-256(entry+prev_hash) |
| FR-GL-009 | Financial integrity | — | DC-003 | Reversal JE is mirror image; original flagged `reversed` |
| FR-GL-010 | Operational visibility | — | DC-001 | 12-month JE list returns ≤ 1,000 ms |
| FR-GL-011 | Operational visibility | — | DC-001 | GL detail with running balance correct per manual calculation |
| FR-GL-012 | Financial integrity | — | DC-003 | Invoice confirm → GL debit AR / credit Revenue posted automatically |
| FR-GL-013 | Financial integrity | — | DC-003 | Payment receipt → GL debit Bank / credit AR posted automatically |
| FR-GL-014 | Financial integrity | — | DC-003 | Stock adjustment → GL auto-post with correct valuation |
| FR-GL-015 | Financial integrity | — | DC-003 | Vendor payment → GL debit AP / credit Bank; WHT split if applicable |
| FR-GL-016 | Financial integrity | — | DC-003 | Farmer payment → GL debit Cooperative Payable / credit MoMo |
| FR-GL-017 | Operational visibility | — | DC-003 | Phase 3 GRN → GL GRNI posting per API contract |
| FR-GL-018 | Government replicability | — | DC-002, DC-007 | New posting rule active without code deployment |
| FR-GL-019 | Financial integrity | BR-013 | DC-003 | Tampered entry detected in integrity check report |
| FR-GL-020 | Financial integrity | BR-013 | DC-003 | Nightly scan breach → email to Finance Director and IT Admin |
| FR-GL-021 | Financial integrity | — | DC-001 | Trial Balance debits = credits; renders ≤ 3,000 ms |
| FR-GL-022 | Operational visibility | — | DC-003 | Running balance updated immediately after posting |
| FR-GL-023 | Financial integrity | — | DC-002 | No overlapping periods created |
| FR-GL-024 | Financial integrity | — | DC-003 | Post to closed period → HTTP 422 `ERR_PERIOD_CLOSED` |
| FR-GL-025 | Dual-mode accounting | DC-004 | DC-004 | Both fiscal calendars produce correct period labels on same JE |
| FR-GL-026 | Financial integrity | — | DC-002 | FX UGX = Foreign × Rate stored and correct |
| FR-GL-027 | Financial integrity | — | DC-002 | Unrealised FX JE posted with correct gain/loss amount |
| FR-GL-028 | Financial integrity | — | DC-003 | Realised FX JE posted; invoice cleared to zero AR balance |
| FR-GL-029 | Financial integrity | — | DC-001 | P&L renders ≤ 5,000 ms; gross profit = revenue − COGS |
| FR-GL-030 | Financial integrity | — | DC-001 | Balance Sheet: assets = liabilities + equity |
| FR-GL-031 | Financial integrity | — | DC-002 | IAS 7 Cash Flow three sections; totals tie to cash movement |
| FR-GL-032 | Operational visibility | — | DC-001 | GL Detail opening + transactions = closing balance |
| FR-GL-033 | Dual-mode accounting | DC-004 | DC-004 | Same transaction amount in both IFRS and parliamentary columns |
| FR-GL-034 | Audit readiness | — | DC-003 | Every GL action creates immutable audit log entry |
| FR-GL-035 | Audit readiness | — | DC-003 | OAG audit trail report covers complete filter range |
| FR-GL-036 | Financial integrity | — | DC-002 | New fiscal year available for period creation |
| FR-GL-037 | Financial integrity | — | DC-002 | Rate auto-selected by closest effective date before transaction date |
| FR-GL-038 | Government replicability | — | DC-002, DC-007 | Updated posting rule applies without restart |
| FR-GL-039 | Operational usability | — | DC-001 | Account search returns results ≤ 300 ms |
| FR-GL-040 | Audit readiness | BR-009 | DC-003 | Gap detection identifies missing JE number |

## 8.3 Functional Requirements Traceability Matrix — F-006 Accounts Receivable

| FR ID | Business Goal | Business Rule | Design Covenant | Test Oracle |
|---|---|---|---|---|
| FR-AR-001 | Agent accountability | — | DC-003 | Invoice confirm → AR sub-ledger record created, balance updated |
| FR-AR-002 | Financial integrity | BR-002 | DC-003 | FIFO allocation clears oldest invoice first |
| FR-AR-003 | Operational visibility | — | DC-001 | Customer AR sub-ledger renders with correct outstanding balance |
| FR-AR-004 | Financial integrity | BR-009 | DC-003 | Credit note CN-YYYY-NNNN sequential; GL auto-posted |
| FR-AR-005 | Operational visibility | — | DC-001 | Aging dashboard renders correct buckets based on due date |
| FR-AR-006 | Operational visibility | — | DC-001 | Filter by territory shows correct sub-totals |
| FR-AR-007 | Agent accountability | — | DC-003 | 30-day overdue → email to Accounts Assistant and Sales Manager |
| FR-AR-008 | Agent accountability | — | DC-003 | 60-day overdue → additional email to Finance Director; invoice flagged `escalated` |
| FR-AR-009 | Agent accountability | — | DC-003 | Agent balance = invoices − verified remittances (real time) |
| FR-AR-010 | Agent accountability | — | DC-003 | Threshold breach → Sales Manager alert with agent details |
| FR-AR-011 | Agent accountability | BR-002, BR-003 | DC-003 | Self-verify remittance → `ERR_SOD_VIOLATION`; no allocation |
| FR-AR-012 | Agent accountability | — | DC-001 | 1,071 agents in aging report sorted by balance |
| FR-AR-013 | Financial integrity | — | DC-003 | Credit limit exceeded → `ERR_CREDIT_LIMIT_EXCEEDED`; zero invoice created |
| FR-AR-014 | Financial integrity | — | DC-003 | Credit hold active → API returns `ERR_CREDIT_HOLD_ACTIVE` |
| FR-AR-015 | Financial integrity | — | DC-002 | Credit limit update applies immediately to new invoice checks |
| FR-AR-016 | Operational visibility | — | DC-001 | Statement PDF generated and emailed with correct balances |
| FR-AR-017 | Operational visibility | — | DC-003 | Monthly auto-statement sent; failures logged |
| FR-AR-018 | Financial integrity | BR-009 | DC-003 | RCT-YYYY-NNNN sequential; GL auto-posted |
| FR-AR-019 | Operational visibility | — | DC-001 | Payment receipt report totals by method correct |
| FR-AR-020 | Operational visibility | — | DC-001 | AR dashboard figures current to last transaction |
| FR-AR-021 | Operational visibility | — | DC-005 | Executive app displays AR summary; push notification on threshold |
| FR-AR-022 | Audit readiness | — | DC-003 | AR sub-ledger total = GL AR control account balance; breach flagged |
| FR-AR-023 | Operational visibility | — | DC-001 | Unapplied payments appear in panel after 7 days |
| FR-AR-024 | Audit readiness | — | DC-003 | 120+ day invoices listed for provision review |
| FR-AR-025 | Operational visibility | — | DC-001 | Collection rate % = collected / invoiced × 100% per territory |

## 8.4 Functional Requirements Traceability Matrix — F-007 Accounts Payable

| FR ID | Business Goal | Business Rule | Design Covenant | Test Oracle |
|---|---|---|---|---|
| FR-AP-001 | Financial integrity | BR-012 | DC-003 | Price variance >5% → `price_variance_hold`; Finance Manager notified |
| FR-AP-002 | Financial integrity | BR-012 | DC-003 | Override logged with justification text in audit trail |
| FR-AP-003 | Financial integrity | BR-012 | DC-003 | Unmatched invoice payment attempt → `ERR_THREE_WAY_MATCH_INCOMPLETE` |
| FR-AP-004 | Operational visibility | — | DC-001 | Vendor AP sub-ledger shows correct outstanding balance |
| FR-AP-005 | Operational visibility | — | DC-001 | AP aging dashboard renders correct buckets |
| FR-AP-006 | Operational visibility | — | DC-001 | Payment due report lists invoices in due-date order |
| FR-AP-007 | Financial integrity | BR-003 | DC-003 | Payment voucher in `draft` until authorised |
| FR-AP-008 | Financial integrity | BR-003 | DC-003 | Creator self-authorise → HTTP 403 `ERR_SOD_VIOLATION` |
| FR-AP-009 | Financial integrity | BR-009 | DC-003 | PMT-YYYY-NNNN sequential; GL auto-posted; PDF generated |
| FR-AP-010 | Financial integrity | — | DC-003 | Credit note increases vendor AP credit balance |
| FR-AP-011 | Financial integrity | — | DC-003 | Credit note applied; invoice balance reduced; credit balance reduced |
| FR-AP-012 | Financial integrity | BR-011 | DC-003 | Unallocated kg → `ERR_INCOMPLETE_CONTRIBUTION_BREAKDOWN`; run blocked |
| FR-AP-013 | Financial integrity | — | DC-002 | Net payable = gross − loan − levy − transport; deductions ≤ gross |
| FR-AP-014 | Financial integrity | — | DC-003 | Bulk payment file total = sum of individual net payables |
| FR-AP-015 | Agent accountability | — | DC-003 | API response per farmer logged; SMS sent; GL posted on success total |
| FR-AP-016 | Financial integrity | — | DC-002 | WHT = invoice gross × 0.06; rate from config table |
| FR-AP-017 | Financial integrity | — | DC-003 | GL: DR AP / CR Bank (net) / CR WHT Payable |
| FR-AP-018 | Audit readiness | — | DC-003 | WHT certificate PDF matches payments; sequential certificate number |
| FR-AP-019 | Audit readiness | — | DC-003 | Monthly WHT remittance clears WHT Payable balance |
| FR-AP-020 | Operational visibility | — | DC-001 | Cash position warning shown when scheduled total >80% cash |
| FR-AP-021 | Operational visibility | — | DC-003 | Scheduled payment reminder sent; no auto-disbursement |
| FR-AP-022 | Audit readiness | — | DC-003 | AP sub-ledger = GL AP control account; breach flagged |
| FR-AP-023 | Operational visibility | — | DC-001 | Vendor statement PDF generated with correct balances |
| FR-AP-024 | Operational visibility | — | DC-001 | AP by expense category totals correct |
| FR-AP-025 | Operational visibility | — | DC-001 | GRNI report shows unmatched GRNs; 30+ day items highlighted |
| FR-AP-026 | Financial integrity | BR-018 | DC-003 | Imprest disbursement below zero → `ERR_IMPREST_INSUFFICIENT` |
| FR-AP-027 | Agent accountability | — | DC-001 | Farmer deduction report: gross, deductions, net per farmer |
| FR-AP-028 | Operational visibility | — | DC-001 | Vendor performance report shows variance count and WHT total |
| FR-AP-029 | Financial integrity | BR-003 | DC-002 | Threshold config update applies immediately; no restart required |
| FR-AP-030 | Operational visibility | — | DC-001 | Cash flow forecast shows projected daily closing balance |

## 8.5 Functional Requirements Traceability Matrix — F-008 Budget Management

| FR ID | Business Goal | Business Rule | Design Covenant | Test Oracle |
|---|---|---|---|---|
| FR-BDG-001 | Parliamentary accountability | BR-014 | DC-002 | Import validates vote codes; mismatches listed with row numbers |
| FR-BDG-002 | Parliamentary accountability | — | DC-002 | Vote code available as GL segment after configuration |
| FR-BDG-003 | Parliamentary accountability | — | DC-001 | Utilisation % = actual / approved × 100%; figures real-time from GL |
| FR-BDG-004 | Parliamentary accountability | — | DC-003 | GL posting updates vote utilisation in same transaction |
| FR-BDG-005 | Parliamentary accountability | BR-014 | DC-003 | 80% threshold → email to Finance Director and Director; dashboard alert |
| FR-BDG-006 | Parliamentary accountability | BR-014 | DC-003 | 95% threshold → HIGH ALERT indicator on dashboard |
| FR-BDG-007 | Parliamentary accountability | BR-014 | DC-003 | 100% breach → `pending_override`; Director justification required; audit log entry |
| FR-BDG-008 | Parliamentary accountability | — | DC-003 | Revision approval updates budget; utilisation re-evaluated; old amount in audit trail |
| FR-BDG-009 | Financial integrity | — | DC-002 | Commercial budget lines created; monthly phasing stored |
| FR-BDG-010 | Financial integrity | — | DC-003 | GL posting updates commercial utilisation in same transaction |
| FR-BDG-011 | Financial integrity | — | DC-001 | Budget vs. actual report: favourable in green, unfavourable in red |
| FR-BDG-012 | Financial integrity | — | DC-001 | Full-year B vs. A renders ≤ 5,000 ms |
| FR-BDG-013 | Dual-mode accounting | DC-004 | DC-004 | Same amount in both parliamentary and IFRS columns of dual-mode report |
| FR-BDG-014 | Operational visibility | — | DC-005 | Executive app displays top 3 over-80% budget items; push notification |
| FR-BDG-015 | Financial integrity | BR-014 | DC-002 | Alert threshold config active immediately; no restart |
| FR-BDG-016 | Audit readiness | BR-014 | DC-003 | Alert history log includes override justifications |
| FR-BDG-017 | Parliamentary accountability | — | DC-003 | Period close freezes budget snapshot; GL postings still allowed |
| FR-BDG-018 | Operational visibility | — | DC-001 | Period status calendar shows open/closed for both fiscal years |
| FR-BDG-019 | Parliamentary accountability | — | DC-002 | Template Excel file generated with correct headers and dropdowns |
| FR-BDG-020 | Parliamentary accountability | — | DC-002 | Pro-rata calculation correct: annual × remaining / total periods |
| FR-BDG-021 | Audit readiness | — | DC-003 | Revision history shows all changes with approver identity |

## 8.6 Open Context Gaps and Verification Flags

The following items require Finance Director or client resolution before the indicated requirements can be finalised or tested.

| Gap ID | Affected Requirements | Description | Severity | Owner |
|---|---|---|---|---|
| GAP-012 | FR-GL-003, FR-GL-031, FR-GL-038 | Confirm whether 1,307-account Chart of Accounts exists or must be designed. GL database design and IAS 7 account mapping cannot be finalised without this. | High | Finance Director |
| GAP-002 | FR-AP-012, FR-AP-014, FR-AP-015 | MTN MoMo Business API sandbox credentials required before farmer bulk payment end-to-end testing | High | Peter / BIRDC Finance |
| GAP-003 | FR-AP-014, FR-AP-015 | Airtel Money API sandbox credentials required before dual-provider payment testing | Medium | Peter / BIRDC Finance |
| GAP-006 | FR-AP-009 | Bank bulk credit transfer file format required by BIRDC's bank — needed for vendor payment bank transfer file specification | Medium | BIRDC Finance |
| GAP-014 | FR-GL-003, FR-GL-021, FR-BDG-001 | Legacy accounting software data migration plan needed before go-live opening balance import strategy can be specified | High | BIRDC Finance / Peter |

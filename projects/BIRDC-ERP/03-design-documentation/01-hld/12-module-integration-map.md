# 12. 17-Module Integration Map

## 12.1 GL Auto-Post Triggers per Module

Every operational transaction in the BIRDC ERP automatically generates a balanced General Ledger journal entry via `GLService::postJournal()`. No manual journal entry is required for operational transactions (design principle for DC-003 audit readiness).

| Module | Transaction | GL Auto-Post (DR / CR) |
|---|---|---|
| F-001 Sales | Invoice confirmed | DR Accounts Receivable / CR Revenue; DR COGS / CR Inventory |
| F-001 Sales | Credit note issued | DR Revenue / CR Accounts Receivable; DR Inventory / CR COGS |
| F-001 Sales | Payment received | DR Bank / CR Accounts Receivable |
| F-002 POS | Sale completed | DR Cash / CR Revenue; DR COGS / CR Inventory |
| F-002 POS | Session close — cash surplus | DR Cash / CR POS Variance |
| F-002 POS | Session close — cash shortage | DR POS Variance / CR Cash |
| F-003 Inventory | Stock adjustment (write-off) | DR Inventory Adjustment Expense / CR Inventory |
| F-003 Inventory | Stock adjustment (write-up) | DR Inventory / CR Inventory Adjustment Revenue |
| F-004 Agents | Agent stock issuance | DR Agent Receivable (Inventory) / CR Warehouse Inventory |
| F-004 Agents | Agent remittance verified | DR Cash / CR Agent Receivable |
| F-004 Agents | Commission earned (verified) | DR Commission Expense / CR Commission Payable |
| F-007 AP | Vendor invoice registered | DR Inventory / CR Accounts Payable |
| F-007 AP | Farmer payment | DR Cooperative Payable / CR Bank (MoMo) |
| F-007 AP | WHT deducted | DR Accounts Payable / CR WHT Payable |
| F-009 Procurement | Cooperative batch receipt posted (Stage 5) | DR Raw Material Inventory / CR Cooperative Payable per cooperative |
| F-011 Manufacturing | Material requisition to WIP | DR WIP / CR Raw Material Inventory |
| F-011 Manufacturing | Production completion | DR Finished Goods Inventory / CR WIP; DR By-product Inventory / CR WIP |
| F-011 Manufacturing | Scrap / waste disposal | DR Scrap Expense / CR WIP |
| F-013 HR | Staff loan issued | DR Staff Loans Receivable / CR Bank |
| F-013 HR | Staff loan deduction (payroll) | DR Salary Payable / CR Staff Loans Receivable |
| F-014 Payroll | Payroll approved | DR Salary Expense / CR Salary Payable; DR NSSF Employer Expense / CR NSSF Payable; DR PAYE Payable (net) / CR Staff Payable |
| F-014 Payroll | Salary bank transfer | DR Salary Payable / CR Bank |
| F-014 Payroll | NSSF remittance | DR NSSF Payable / CR Bank |
| F-015 R&D | R&D expenditure | DR R&D Expense / CR Accounts Payable |
| F-016 Administration | Asset acquisition | DR Fixed Assets / CR Accounts Payable or Bank |
| F-016 Administration | Depreciation | DR Depreciation Expense / CR Accumulated Depreciation |

## 12.2 Module Data Dependencies

The following table identifies which modules consume data produced by other modules, defining the dependency order for development and integration testing.

| Module | Depends On (must be functional first) |
|---|---|
| F-002 POS | F-001 Sales, F-003 Inventory |
| F-004 Agent Distribution | F-001 Sales, F-003 Inventory |
| F-005 General Ledger | All modules (GL is the downstream sink for all auto-posts) |
| F-006 Accounts Receivable | F-001 Sales, F-004 Agent Distribution |
| F-007 Accounts Payable | F-009 Procurement, F-010 Farmer Management |
| F-008 Budget Management | F-005 GL (reads expenditure from GL) |
| F-009 Procurement | F-003 Inventory (GRN posts to inventory) |
| F-010 Farmer Management | F-009 Procurement (farmers are tied to cooperative batches) |
| F-011 Manufacturing | F-003 Inventory (materials reservation and output posting) |
| F-012 QC | F-011 Manufacturing (inspects production output batches) |
| F-013 HR | F-014 Payroll (employee records are payroll input) |
| F-014 Payroll | F-013 HR (requires employee contracts, leave, loans) |
| F-015 R&D | F-010 Farmer (variety performance data) |
| F-016 Administration | F-009 Procurement (procurement register) |
| F-017 System Admin | All modules (user management and audit log span all modules) |

## 12.3 7-Phase Delivery Dependency Order

The following table maps all 17 modules to their delivery phases, ensuring each phase builds on a stable foundation from the prior phase.

| Phase | Modules | Dependency Rationale |
|---|---|---|
| Phase 1 — Commerce Foundation | F-001, F-002, F-003, F-004 | All sales and inventory functionality; agent cash accountability; EFRIS basics |
| Phase 2 — Financial Core | F-005, F-006, F-007, F-008 | Requires Phase 1 transaction data to auto-post into the GL |
| Phase 3 — Supply Chain & Farmers | F-009, F-010 | Requires GL (F-005) for procurement journal entries; requires inventory (F-003) for GRN |
| Phase 4 — Production & Quality | F-011, F-012 | Requires raw material inventory from Phase 3; requires GL from Phase 2 for WIP accounting |
| Phase 5 — People | F-013, F-014 | Requires GL (F-005) for payroll auto-posting; standalone HR data |
| Phase 6 — Research, Admin & Compliance | F-015, F-016 | Requires farmer data (F-010) and procurement register (F-009) |
| Phase 7 — Integration, Hardening & Go-Live | Full EFRIS (F-018), Security Hardening (F-019) | Requires all 17 modules complete; end-to-end integration testing across all modules |

## 12.4 Shared Reference Data

The following reference data tables are shared across multiple modules and must be initialised before module data entry begins:

| Reference Table | Used By |
|---|---|
| `tbl_coa_accounts` (Chart of Accounts) | F-005, and all modules that trigger GL auto-posts |
| `tbl_products` (Product Catalogue) | F-001, F-002, F-003, F-004, F-011 |
| `tbl_customers` | F-001, F-002, F-006 |
| `tbl_agents` | F-002, F-004, F-006 |
| `tbl_employees` | F-013, F-014 |
| `tbl_suppliers` | F-007, F-009 |
| `tbl_cooperatives` | F-009, F-010 |
| `tbl_warehouses_locations` | F-003, F-009, F-011 |
| `tbl_roles` + `tbl_rbac_permissions` | F-017, all modules |

# 4. Navigation Architecture

## 4.1 Main ERP Workspace — Sidebar Menu Structure

The Main ERP workspace (`/public/`) uses a fixed left sidebar for primary navigation. The sidebar is always visible on desktop (≥ 992px viewport width). On tablet (768–991px) the sidebar collapses to icon-only mode; on mobile it is hidden behind a hamburger toggle.

### Sidebar Menu Hierarchy

```
Dashboard
  └── Executive Overview

Sales
  ├── Invoices
  ├── Credit Notes
  ├── Customers
  ├── Price Lists
  └── Sales Reports

Point of Sale
  ├── New Sale
  ├── POS Sessions
  └── POS Reports

Inventory
  ├── Stock Balance
  ├── Receive Goods (GRN)
  ├── Stock Transfers
  ├── Physical Count
  ├── Expiry Alerts
  └── Warehouse Reports

Agent Distribution
  ├── Agents
  ├── Agent Stock Issuance
  ├── Remittances (Verify)
  └── Agent Reports

Finance
  ├── Dashboard
  ├── Journal Entries
  ├── Chart of Accounts
  ├── Financial Statements
  ├── Budget vs. Actual
  ├── Accounts Receivable
  │   ├── AR Aging
  │   └── Customer Statements
  └── Accounts Payable
      ├── AP Aging
      ├── Vendor Payments
      └── Farmer Payments

Procurement
  ├── Purchase Requests
  ├── RFQs
  ├── Local Purchase Orders
  ├── Goods Receipts
  ├── Farmer Procurement
  │   ├── Bulk POs (Stage 1)
  │   ├── Batch Receipts (Stage 2)
  │   ├── Farmer Breakdown (Stage 3)
  │   └── Procurement Reports
  └── Vendors

Farmers & Cooperatives
  ├── Farmer Register
  ├── Cooperatives
  ├── Farm Profiles
  ├── Extension Services
  └── Farmer Reports

Production
  ├── Production Orders
  ├── Bill of Materials / Recipes
  ├── Mass Balance Report
  └── Production Reports

Quality Control
  ├── Inspection Templates
  ├── Inspections
  ├── Certificates of Analysis
  ├── Non-Conformance Reports
  ├── SPC Charts
  └── Lab Equipment

Human Resources
  ├── Employees
  ├── Leave Management
  ├── Attendance
  └── HR Reports

Payroll
  ├── Run Payroll
  ├── Payroll History
  ├── NSSF Schedule
  ├── PAYE Schedule
  └── Payroll Reports

Research & Development
  ├── Banana Varieties
  ├── Field Trials
  ├── Product Development
  └── R&D Expenditure

Administration
  ├── PPDA Procurement Register
  ├── Asset Register
  ├── Vehicle & Equipment Log
  └── Document Store
```

## 4.2 Role-Based Menu Visibility

Menu items are hidden — not greyed out — for roles that do not have access. A user who cannot see "Payroll > Run Payroll" does not know it exists. This prevents both confusion and security probing.

| Role | Visible Top-Level Menus |
|---|---|
| Finance Director | Dashboard, Sales (view), Finance (full), Payroll (approve only), Administration (view) |
| Finance Manager | Finance (full), Payroll (run + approve), Accounts Receivable, Accounts Payable |
| Sales Manager | Dashboard, Sales (full), Agent Distribution (full), Inventory (view), Customers |
| Procurement Manager | Procurement (full), Farmers & Cooperatives (full), Inventory (view), Finance (AP only) |
| Store Manager | Inventory (full), Agent Distribution (stock issuance only), Procurement (GRN only) |
| QC / Lab Manager | Quality Control (full), Production (view), Inventory (view) |
| Production Supervisor | Production (full), Inventory (material requisition only), Quality Control (submit results) |
| HR Manager | Human Resources (full), Payroll (view), Finance (payroll GL view only) |
| Collections Officer | Procurement > Farmer Procurement (Stages 2–3 only), Farmers & Cooperatives (view + register) |
| Cashier (POS) | Point of Sale (full), Sales (receipts only) |
| IT Administrator | Administration (full), Admin Panel only |
| Director | Dashboard (Executive, read-only), all modules (read-only reporting view) |

## 4.3 Agent Portal — Simplified Navigation

The Agent Portal (`/public/sales-agents/`) uses a simplified bottom-tab navigation on mobile browsers (the primary access method for the 1,071 field agents).

```
Bottom Tab Bar (5 tabs):
  [Home]  [New Sale]  [Remittance]  [Stock]  [Reports]
```

- **Home tab:** S-010 Agent Dashboard — cash balance, outstanding, last remittance.
- **New Sale tab:** S-011 Agent POS — full offline-capable POS scoped to agent's virtual inventory.
- **Remittance tab:** S-012 Remittance Submit form.
- **Stock tab:** S-014 Agent Stock View.
- **Reports tab:** S-013 Commission Statement + sales history.

The Agent Portal has no sidebar. Every feature is accessible in ≤ 2 taps from the bottom tab bar.

## 4.4 Breadcrumb Navigation

All Main ERP screens display a breadcrumb trail immediately below the page header bar. Format:

`[Top-Level Module] > [Sub-section] > [Entity Identifier]`

Examples:

- `Finance > Journal Entries > JE-2026-0047`
- `Production > Production Orders > PRO-2026-0012`
- `Procurement > Farmer Procurement > Farmer Breakdown > Batch FBR-2026-0004`

Breadcrumb elements are clickable links that navigate back to the parent screen. The current page (last element) is not a link — it is plain text.

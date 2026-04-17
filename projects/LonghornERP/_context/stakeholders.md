# Stakeholders — Longhorn ERP

## Product Owner

| Field | Value |
|---|---|
| Name | Peter Bamuhigire |
| Organisation | Chwezi Core Systems |
| Website | techguypeter.com |
| Email | peter@techguypeter.com |
| Phone | +256784464178 |
| Role | Founder, Lead Architect, Product Owner |
| Authority | Final sign-off on all requirements and design decisions |

## Company

| Field | Value |
|---|---|
| Company | Chwezi Core Systems |
| Website | chwezicore.com |
| Email | info@chwezicore.com |
| Products | Longhorn ERP (flagship), Academia Pro, Medic8, Kulima |

## Development Team

- Small team of 2–5 developers
- Full-stack PHP + MySQL + Bootstrap
- Mobile developers for Android (Kotlin/Jetpack Compose) and iOS (Swift/SwiftUI)

## Primary End-User Personas

### 1. Finance Manager / Accountant

- Needs: Double-entry GL, financial statements, VAT returns, bank reconciliation, budgets
- Frustrations with current tools: Complex chart of accounts setup, difficult VAT reporting, no EFRIS integration
- Success metric: Monthly close completed in under 2 hours without external consultant

### 2. Warehouse / Inventory Officer

- Needs: Real-time stock levels, GRN processing, reorder alerts, stock transfers, batch tracking
- Frustrations: Stock discrepancies, manual Excel tracking, no barcode support
- Success metric: Zero unexplained stock variances; GRN processed in under 5 minutes

### 3. Sales Representative / Field Agent

- Needs: Customer records, invoice creation, payment recording, commission visibility
- Frustrations: No mobile access, slow approval for quotations, no CRM
- Success metric: New invoice created from mobile in under 3 minutes

### 4. HR / Payroll Officer

- Needs: Employee records, leave management, payroll run, NSSF/PAYE compliance
- Frustrations: Manual payroll in Excel, PAYE calculation errors, no statutory report generation
- Success metric: Monthly payroll run completed in under 30 minutes for 100 employees

### 5. Operations / Procurement Manager

- Needs: Purchase requisitions, LPO creation, three-way matching, supplier management
- Frustrations: No audit trail, verbal approvals, no supplier price comparison
- Success metric: Purchase order approved and dispatched within 24 hours of requisition

### 6. CEO / Managing Director

- Needs: Dashboard KPIs, financial summaries, BSC scorecard, project P&L
- Frustrations: No real-time visibility, weekly manual reports from team
- Success metric: Full business overview available on mobile dashboard at any time

### 7. System Administrator (Tenant)

- Needs: User creation, role assignment, module activation, branch setup
- Frustrations: Complex setup, requires vendor support for changes
- Success metric: New user onboarded and productive in under 15 minutes

### 8. Super Admin (Chwezi Platform)

- Needs: Tenant provisioning, subscription management, billing, impersonation for support
- Success metric: New tenant provisioned and live in under 10 minutes

### 9. External Auditor

- Needs: Read-only access to audit logs, financial statements, GL detail
- Success metric: Full audit trail accessible without requiring vendor support

### 10. Cooperative / Outgrower Farmer

- Needs: View commodity intake records, deductions, mobile money payment statements
- Access: End-user portal (web + mobile)
- Success metric: Farmer payment statement accessible from basic Android phone

## Approval Matrix

<!-- TODO: Define approval limits per role per module before Phase 1 sign-off -->
- Purchase Order approval limits by role
- Leave approval chain
- Payroll approval chain
- Journal entry approval requirements

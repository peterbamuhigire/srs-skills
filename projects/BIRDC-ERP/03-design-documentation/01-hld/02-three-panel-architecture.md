# 2. Three-Panel Application Architecture

The BIRDC ERP web application is divided into three logically and URL-separated panels. Each panel serves a distinct user population with tailored functionality, access controls, and interface complexity.

## 2.1 Panel Overview

| Panel | URL Path | Primary Users | Session Type |
|---|---|---|---|
| Main ERP Workspace | `/public/` | All BIRDC/PIBID internal staff | Session-based (HttpOnly cookies) |
| Sales Agent Portal | `/public/sales-agents/` | 1,071 field sales agents | Session-based (web) or JWT (mobile API) |
| System Administration | `/public/admin/` | IT Administrator, super-users | Session-based (HttpOnly cookies) + mandatory TOTP 2FA |

## 2.2 Main ERP Workspace (`/public/`)

The Main ERP Workspace is the full-featured operational environment for all BIRDC and PIBID internal staff. Access is role-controlled via the 8-layer authorisation model.

**Users:** Finance team (~8 accounts assistants), Sales & Marketing Manager, Procurement Manager, Store Manager, Production Manager, QC Manager, HR Manager, Payroll Officer, Research Coordinator, Administration Officer, Director, Finance Director, and all other staff.

**Modules hosted in this panel:**

| Module | Phase | Key Screens |
|---|---|---|
| F-001: Sales & Distribution | 1 | Invoice management, customer accounts, credit control, pricing, territory tracking |
| F-002: Point of Sale (factory gate/showroom) | 1 | POS terminal, session management, receipt printing, multi-payment |
| F-003: Inventory & Warehouse Management | 1 | Stock catalogue, location management, batch/lot register, stock transfer, physical count |
| F-004: Agent Distribution Management | 1 | Agent register, cash balance dashboard, remittance processing, commission statements |
| F-005: Financial Accounting & General Ledger | 2 | Chart of accounts, journal entry, GL, financial statements, hash chain verification |
| F-006: Accounts Receivable | 2 | Customer AR aging, agent receivable, payment allocation, customer statements |
| F-007: Accounts Payable | 2 | Vendor invoices, three-way matching, farmer payment batches, WHT certificates |
| F-008: Budget Management | 2 | Parliamentary votes, commercial budgets, budget vs. actual variance |
| F-009: Procurement & Purchasing | 3 | Purchase requests, RFQ, LPO, GRN, cooperative procurement (5 stages) |
| F-010: Farmer & Cooperative Management | 3 | Farmer register, farm profiling, contribution history, bulk payment |
| F-011: Manufacturing & Production | 4 | Recipe/BOM, production orders, material requisition, mass balance, job cards |
| F-012: Quality Control & Laboratory | 4 | Inspection templates, results entry, CoA generation, SPC charts, NCR |
| F-013: Human Resources | 5 | Employee lifecycle, leave management, attendance, biometric import |
| F-014: Payroll | 5 | Payroll run, PAYE/NSSF/LST, payroll lock, payslip generation |
| F-015: Research & Development | 6 | Variety performance, field trials, product development register |
| F-016: Administration & PPDA Compliance | 6 | Procurement register, asset register, document management |

## 2.3 Sales Agent Portal (`/public/sales-agents/`)

The Sales Agent Portal is a simplified sub-application purpose-built for field agents. The interface is streamlined for non-technical users with minimal training requirement (Design Covenant DC-001).

**Users:** 1,071 field sales agents.

**Functionality available to agents:**

- Agent POS: process sales against the agent's own virtual inventory store (not warehouse stock — BR-001 enforced)
- View agent stock balance (current inventory held in field)
- Submit cash remittances (FIFO auto-allocation via `sp_apply_remittance_to_invoices`)
- View commission statements (verified sales only — BR-015)
- View outstanding invoice balances
- View territory performance summary

**Restrictions enforced at this portal:**

- Agents cannot access warehouse inventory records.
- Agents cannot view other agents' data.
- Agents cannot modify remittance allocations.
- Session is single-device; concurrent sessions are blocked.

## 2.4 System Administration Panel (`/public/admin/`)

The System Administration Panel provides IT infrastructure and security management capabilities. It is accessible only to the IT Administrator and BIRDC Director.

**Users:** IT Administrator, BIRDC Director (read-only audit access).

**Functionality:**

- User account management: create, edit, suspend, deactivate accounts
- Role and permission matrix configuration: define roles, assign pages, API endpoints, UI elements, locations, time windows, conditional rules, and object ownership
- Audit log review: full system-wide audit trail searchable by user, action, date range, table, and record ID
- Database backup scheduling: configure automated backup jobs, retention policy, and off-site destinations
- Integration configuration: EFRIS API credentials, MTN MoMo API keys, Airtel Money API keys, email SMTP configuration, Africa's Talking API keys
- Report scheduling: define automated report generation and email delivery schedules
- System health dashboard: server CPU, RAM, disk usage, database performance metrics, active session count

**Security controls on the admin panel:**

- TOTP 2FA is mandatory for all admin panel accounts.
- Every admin action is logged with actor identity, IP address, and timestamp.
- Admin panel access from external IP addresses requires VPN or is blocked by firewall rule.

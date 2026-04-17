## 1. Purpose and Scope

### 1.1 Purpose

This Test Strategy defines the overarching approach, principles, and standards that govern all verification and validation activities for the BIRDC ERP system. It establishes the test levels, priorities, environments, roles, responsibilities, defect classification scheme, and entry/exit criteria that apply across all 7 delivery phases. Every downstream Test Plan, Test Case specification, and Test Report for this project must conform to this strategy.

### 1.2 Scope

Testing covers:

- All 17 functional modules: Sales & Distribution (F-001), Point of Sale (F-002), Inventory & Warehouse Management (F-003), Agent Distribution Management (F-004), Financial Accounting & General Ledger (F-005), Accounts Receivable (F-006), Accounts Payable (F-007), Budget Management (F-008), Procurement & Purchasing (F-009), Farmer & Cooperative Management (F-010), Manufacturing & Production (F-011), Quality Control & Laboratory (F-012), Human Resources (F-013), Payroll (F-014), Research & Development (F-015), Administration & PPDA Compliance (F-016), and System Administration / IT (F-017).
- 3 web application panels: Main ERP Workspace (`/public/`), Sales Agent Portal (`/public/sales-agents/`), System Administration (`/public/admin/`).
- 6 Android mobile applications: Sales Agent App, Farmer Delivery App, Warehouse App, Executive Dashboard App, HR Self-Service App, and Factory Floor App.
- External integrations: URA EFRIS system-to-system API, MTN MoMo Business API, Airtel Money API, and ZKTeco biometric fingerprint device integration.
- All 18 business rules (BR-001 through BR-018) and all 7 Design Covenants (DC-001 through DC-007).
- Non-functional requirements: performance, security, availability, offline operation, and data integrity.

### 1.3 Out of Scope

- iOS applications (deferred per project scope decision).
- URA EFRIS production environment testing prior to go-live (sandbox only until Phase 7).
- Third-party vendor internal systems beyond their published API contracts.

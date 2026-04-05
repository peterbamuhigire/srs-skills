# API Endpoint Inventory — Maduuka Phase 1

**Source:** `APISpec_Maduuka_Phase1.docx` (64 endpoints, 6 sections)
**Date:** 2026-04-05

*Full payload detail is in the API Specification document. This appendix lists coverage by module for traceability.*

| Section | Module | Endpoint Count | Auth | Notes |
|---|---|---|---|---|
| 1 | Authentication | ~6 | Public / JWT | Login, logout, refresh, 2FA, password reset, magic-link |
| 2 | POS | ~15 | JWT + RBAC | Sale create, payment, receipt, session open/close, void, refund, held carts |
| 3 | Inventory | ~12 | JWT + RBAC | Product CRUD, stock levels, stock count, adjustments, transfers, batches |
| 4 | Customers & Suppliers | ~10 | JWT + RBAC | Customer CRUD, credit, supplier CRUD, PO, goods receipt |
| 5 | Finance & HR | ~12 | JWT + RBAC | Accounts, transactions, expenses, payroll run, payslips, leave |
| 6 | Settings & Reporting | ~9 | JWT + RBAC | Business profile, settings, report generation, scheduled reports |

*Total: 64 endpoints across 6 sections. Exact endpoint paths are in the API spec document.*

## Known Gaps (from Integration Audit)

- MTN MoMo inbound callback endpoint — verify it is documented in section 2 (POS)
- Pagination parameters (`page`, `per_page`, `cursor`) — verify presence on all list endpoints
- Offline sync endpoint — verify a dedicated `POST /sync/batch` or equivalent is included

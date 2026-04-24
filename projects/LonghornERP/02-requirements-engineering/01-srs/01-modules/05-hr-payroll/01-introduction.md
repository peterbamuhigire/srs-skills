# Introduction to the HR and Payroll Module SRS

## 1.1 Purpose

This Software Requirements Specification (SRS) defines all functional and non-functional requirements for the Human Resources (HR) and Payroll module of Longhorn ERP. The document targets software engineers, QA analysts, system architects, and business stakeholders responsible for implementing and verifying this module. All requirements are prospective and use the prescriptive form "The system shall...".

## 1.2 Scope

The HR and Payroll module governs the full employee lifecycle within Longhorn ERP: employee master data, organisational structure, job and position governance, leave management, attendance, payroll computation, payroll-governance controls, statutory deductions, payslip generation, manager and employee self-service, operational people analytics, and bank/mobile-money salary disbursement.

The module integrates with:

- **General Ledger** — every payroll run generates journal entries for gross salary, statutory deductions, and net pay.
- **RBAC** — role-based access controls govern who may view payslips, run payroll, and approve leave.
- **Audit Log** — every payroll run, approval, and employee data change is recorded immutably.
- **Mobile API** — employee self-service features (leave requests, payslip download) are exposed via the JWT REST API.
- **Localisation Engine** — jurisdiction-specific payroll statutory settings and filing routes are applied per tenant profile.

The module does not cover sales commissions (Sales Agents module), procurement, or financial accounting beyond payroll GL posting. Full recruiting, learning, succession, and broad talent-suite capabilities remain outside the current `HR_PAYROLL` scope unless explicitly added in a future module set.

## 1.3 Business Goals

| ID | Goal |
|---|---|
| BG-001 | Accurate, on-time payroll for all employees with zero manual recalculation errors. |
| BG-002 | Statutory compliance with Uganda (PAYE, NSSF, NITA), Kenya (PAYE, NHIF, NSSF), Tanzania (PAYE, PSSSF), and Rwanda (PAYE, RSSB). |
| BG-003 | Employee self-service for payslips, leave, and attendance to reduce HR administrative load. |
| BG-004 | Audit-ready payroll records retained per jurisdictional statutory requirements. |
| BG-005 | Governed workforce structures, job and position controls, and accountable manager participation in workforce transactions. |
| BG-006 | Reduced payroll-operating risk through controlled calendars, validation, variance review, and release governance. |

## 1.4 Applicable Standards and Regulations

- Uganda Employment Act 2006 and Income Tax Act — PAYE bands, NSSF rates, terminal benefits.
- Kenya Employment Act 2007 — PAYE, NHIF, NSSF (tier system).
- Tanzania Employment and Labour Relations Act 2004 — PSSSF contributions.
- Rwanda Labour Code — RSSB contributions.
- Uganda Data Protection and Privacy Act 2019 — employee personal data handling `[CONTEXT-GAP: GAP-007]`.
- IEEE Std 830-1998 — SRS quality attributes.
- IEEE Std 1012-2016 — software V&V.

## 1.5 Definitions and Acronyms

| Term | Definition |
|---|---|
| Gross Pay | Total employee compensation before any deductions. |
| Net Pay | Gross Pay minus all statutory and voluntary deductions. |
| NITA | National Industrial Training Authority levy (Uganda). |
| NSSF | National Social Security Fund (Uganda and Kenya). |
| NHIF | National Health Insurance Fund (Kenya). |
| PAYE | Pay As You Earn — income tax deducted by the employer from employee salaries. |
| PSSSF | Public Service Social Security Fund (Tanzania). |
| RSSB | Rwanda Social Security Board. |
| Payroll Run | The batch process that computes gross pay, deductions, and net pay for all active employees in a specified pay period. |
| Payslip | A per-employee document summarising earnings, deductions, and net pay for a pay period. |

## 1.6 Document Conventions

- Functional requirements carry the identifier pattern `FR-HR-NNN`.
- Non-functional requirements carry the identifier pattern `NFR-HR-NNN`.
- `[CONTEXT-GAP: <topic>]` marks a requirement requiring additional context.

## 1.7 Overview of This Document

| Section | Content |
|---|---|
| 2 | Employee Master and Organisational Structure |
| 3 | Leave Management |
| 4 | Attendance |
| 5 | Payroll Configuration |
| 6 | Payroll Run and Statutory Deductions |
| 7 | Payslips and Disbursements |
| 8 | Loans and Advances |
| 9 | Exit Management |
| 10 | Employee Self-Service |
| 2A | Position and Workforce Governance |
| 6A | Payroll Governance and Controls |
| 10A | Manager Self-Service and Workforce Analytics |
| 11 | Non-Functional Requirements |
| 12 | Traceability Matrix |

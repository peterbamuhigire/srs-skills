# 2. Overall Description

## 2.1 System Context

The Phase 5 People modules operate within the BIRDC ERP web application hosted on BIRDC's own on-premise server at Nyaruzinga, Bushenyi. The modules interact with:

- **Phase 2 (F-005 General Ledger):** Payroll approval triggers automatic GL entries. No manual journal entry is required for any payroll transaction.
- **Phase 4 (F-011 Manufacturing):** Factory worker registry provides worker assignments and productivity metrics to production orders.
- **Phase 1 (F-001 Sales):** Commission payable figures for agents are referenced in payroll elements if included in formal payroll.
- **ZKTeco biometric devices:** Attendance data is imported directly from the device SDK. Manual re-entry is prohibited (BR-016).
- **MTN MoMo / Airtel Money APIs:** Casual worker salary paid via bulk mobile money batch payment.
- **PHPMailer / WhatsApp:** Payslip PDF delivery channel.
- **HR Self-Service App (Android):** Staff-facing mobile application for leave applications, payslip viewing, attendance records, and leave balance enquiry.

## 2.2 User Classes and Characteristics

| User Class | System Access | Key HR/Payroll Actions |
|---|---|---|
| HR Manager (STK-011) | Web ERP — full HR module | Employee lifecycle, leave approval, disciplinary records, exit clearance |
| Payroll Officer (STK-012) | Web ERP — full Payroll module | Payroll run, PAYE/NSSF/LST configuration, payslip generation |
| Finance Manager | Web ERP — payroll approval | Approve and lock payroll run; approve manual attendance overrides |
| Finance Director (STK-002) | Web ERP — payroll configuration | Update PAYE tax bands, NSSF rates, LST tiers without developer involvement |
| IT Administrator (STK-003) | Admin panel — biometric config | Configure ZKTeco device connection; manage HR Self-Service App credentials |
| All Staff (STK-021) | HR Self-Service App (Android) | Apply for leave, view payslips, check leave balance, view attendance |
| Production Supervisor | Web ERP — factory worker registry | Assign casual workers to production orders; record daily attendance |

## 2.3 Operating Environment

The HR and Payroll modules run within the main ERP workspace at `/public/`. The HR Self-Service App runs on Android 8.0 (API 26) and above on staff-owned or BIRDC-issued devices. Network connectivity at Bushenyi is intermittent; the HR Self-Service App must operate in read-only offline mode and queue write operations (leave applications) for sync when connectivity returns.

## 2.4 Design and Implementation Constraints

The following Design Covenants (DC) and Business Rules (BR) govern all Phase 5 requirements without exception:

- **DC-001:** Every screen used daily must be self-discoverable. A newly onboarded HR assistant must process a leave application without reading a manual.
- **DC-002:** All PAYE tax bands, NSSF rates, and LST tiers are configurable via the UI by the Finance Director. No developer is involved in rate changes.
- **DC-003:** Every payroll transaction creates an immutable audit trail automatically. 7-year retention enforced.
- **DC-004:** Payroll GL auto-postings serve both PIBID parliamentary budget votes and BIRDC commercial IFRS accounts simultaneously.
- **DC-006:** All employee records are stored on BIRDC's own server. No third-party SaaS holds employee data.
- **BR-003:** The person who creates a payroll run cannot be the same person who approves it (segregation of duties, enforced at API layer).
- **BR-010:** Once the Finance Manager approves and locks a payroll run, no modification is permitted. Corrections are processed as adjustment runs in the next period.
- **BR-016:** ZKTeco biometric attendance records are authoritative. Manual overrides require Finance Manager approval and are logged with the reason.

## 2.5 Assumptions and Dependencies

- ZKTeco biometric device model numbers and SDK version will be confirmed by BIRDC IT. `[CONTEXT-GAP: GAP-005]`
- Current Uganda PAYE tax bands (2024/25 or updated) will be confirmed by the consultant before payroll specification is finalised. `[CONTEXT-GAP: GAP-008]`
- NSSF contribution schedule exact format will be confirmed by BIRDC HR. `[CONTEXT-GAP: GAP-009]`
- BIRDC's bank name and bulk credit transfer file format will be confirmed by BIRDC Finance. `[CONTEXT-GAP: GAP-006]`
- MTN MoMo Business API sandbox credentials will be obtained before casual worker salary testing. `[CONTEXT-GAP: GAP-002]`

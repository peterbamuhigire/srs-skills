## RACI Matrix for Longhorn ERP

This matrix assigns Responsible, Accountable, Consulted, and Informed (RACI) roles for 8 key decisions and activities. Each cell contains a single RACI code; where a role has no involvement, the cell is left blank.

**RACI definitions (IEEE Std 610.12-1990, organisational responsibility model):**

- **R** — Responsible: executes the activity or produces the artefact.
- **A** — Accountable: owns the outcome; has final sign-off authority. Exactly one *A* per row.
- **C** — Consulted: provides input before the decision is made; two-way communication.
- **I** — Informed: notified of the outcome; one-way communication.

**RACI roles in this matrix:**

| Code | Role | Holder |
|---|---|---|
| PO | Product Owner | Peter Bamuhigire, Chwezi Core Systems |
| LD | Lead Developer | Chwezi Core Systems development team lead |
| TSA | Tenant System Administrator | Customer-side platform configuration owner |
| FM | Finance Manager | Tenant organisation finance lead |
| HRO | HR Officer | Tenant organisation HR lead |
| CEO | CEO / MD | Tenant organisation executive decision-maker |

---

### RACI Table

| Activity / Decision | PO | LD | TSA | FM | HRO | CEO |
|---|---|---|---|---|---|---|
| System requirements sign-off | **A** | **C** | **I** | **C** | **C** | **I** |
| Module activation per tenant | **C** | **R** | **A** | **I** | **I** | **I** |
| Go-live approval | **A** | **R** | **C** | **C** | **C** | **C** |
| Pricing changes | **A** | **I** | | | | **C** |
| Integration configuration (EFRIS, MoMo) | **C** | **A** | **R** | **C** | | **I** |
| User role definition | **C** | **C** | **A** | **C** | **C** | **I** |
| Financial statement approval | | | **I** | **R** | | **A** |
| Payroll run approval | | | **I** | **C** | **R** | **A** |

---

### Notes

- **System requirements sign-off:** The Product Owner holds sole accountability. The Lead Developer and tenant stakeholders (Finance Manager, HR Officer) are consulted to validate technical and operational feasibility before sign-off. Tenant System Administrators and CEO / MD are informed of the outcome.

- **Module activation per tenant:** The Lead Developer executes module activation through the Super Admin console. The Tenant System Administrator is accountable for confirming activation requirements match tenant needs. The Product Owner is consulted on any activation that deviates from the standard onboarding checklist.

- **Go-live approval:** The Product Owner is accountable for platform readiness. The Lead Developer executes deployment. All tenant stakeholders are consulted to confirm User Acceptance Testing (UAT) sign-off. No go-live will proceed without UAT acknowledgement from Finance Manager and CEO / MD.

- **Pricing changes:** The Product Owner is accountable for all pricing decisions. The CEO / MD of Chwezi Core Systems (same individual as Product Owner at current company size) is consulted. Pricing changes are not visible to tenant-side roles.

- **Integration configuration (EFRIS, MoMo):** The Lead Developer is accountable for technical configuration of URA EFRIS and mobile money Application Programming Interface (API) connections. The Tenant System Administrator executes credential entry and tenant-side setup. The Finance Manager is consulted to validate EFRIS invoice format and VAT mapping.

- **User role definition:** The Tenant System Administrator is accountable for all role and permission assignments within their tenant. The Product Owner and Lead Developer are consulted only where a requested permission combination requires a platform-level change. Finance Manager and HR Officer are consulted to confirm their own access profiles are correct.

- **Financial statement approval:** The Finance Manager prepares and is responsible for financial statements. The CEO / MD is accountable for final approval before external publication or submission. The Tenant System Administrator is informed once statements are approved and published to the document library.

- **Payroll run approval:** The HR Officer is responsible for preparing and submitting the payroll run. The CEO / MD is accountable for final approval before disbursement (per the payroll approval chain in `04-approval-matrix.md`). The Finance Manager is consulted to validate totals and statutory deduction accuracy. The Tenant System Administrator is informed of completion for audit log purposes.

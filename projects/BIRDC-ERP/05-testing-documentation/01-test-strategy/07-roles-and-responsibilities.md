## 6. Roles and Responsibilities

| Role | Name / Position | Testing Responsibilities |
|---|---|---|
| Test Strategy Owner & Financial Logic Verifier | Peter Bamuhigire, ICT Consultant | Owns this strategy document; verifies all financial calculation test oracles (PAYE, NSSF, FIFO, mass balance, hash chain); reviews all unit test assertions for financial services; signs off Phase Gate test results; resolves test environment issues. |
| UAT Owner — Financial Modules | BIRDC Finance Director | Leads UAT for GL, AR, AP, Budget Management, and Payroll modules. Signs Phase 2 and Phase 5 Phase Gate acceptance forms. Validates dual-mode accounting reports (parliamentary + IFRS). Triggers hash chain integrity check. |
| UAT Owner — Sales and Agent Modules | BIRDC Sales Manager | Leads UAT for Sales & Distribution, POS, and Agent Distribution Management. Signs Phase 1 Phase Gate acceptance form. Validates agent cash balance reports and dual-track inventory separation. Manages agent float limits during UAT. |
| UAT Owner — Quality and Manufacturing | BIRDC QC Manager | Leads UAT for Quality Control & Laboratory and Manufacturing & Production. Signs Phase 4 Phase Gate acceptance form. Validates QC gate (BR-004), CoA generation for domestic and export markets, and mass balance (BR-008). |
| UAT Owner — Procurement and Farmers | BIRDC Administration / Procurement Officer | Leads UAT for Procurement & Purchasing, Farmer & Cooperative Management. Signs Phase 3 Phase Gate acceptance form. Validates 5-stage farmer procurement workflow and PPDA documentation checklist. |
| UAT Owner — HR and Self-Service | BIRDC HR Manager | Leads UAT for Human Resources and HR Self-Service App. Signs Phase 5 Phase Gate acceptance form with Finance Director. Validates ZKTeco biometric import and leave management. |
| Unit and Integration Test Execution | Hired Developers | Write and execute all unit and integration tests. Maintain 80% coverage on financial services. Raise defects in the issue tracker. Fix defects within agreed SLA. |
| IT Administration UAT | BIRDC IT Administrator | Leads UAT for System Administration module (/public/admin/). Validates user roles and permissions matrix, audit log review, and backup management. Signs Phase 6 Phase Gate acceptance form. |

### 6.1 Segregation of Duties in Testing

In alignment with BR-003, no developer who wrote a feature may be the sole tester of that feature's acceptance criteria. Peter Bamuhigire performs independent verification of all financial logic test results. UAT owners are independent of the development team.

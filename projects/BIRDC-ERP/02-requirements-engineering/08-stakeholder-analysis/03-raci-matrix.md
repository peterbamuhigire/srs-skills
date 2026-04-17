# Section 3: RACI Matrix by Delivery Phase

## 3.1 RACI Key

| Code | Definition |
|---|---|
| R | *Responsible* — performs the work or makes the decision. May be shared. |
| A | *Accountable* — the single person who is ultimately answerable for the outcome. Cannot be shared; exactly one A per row. |
| C | *Consulted* — provides input before the action or decision; two-way communication. |
| I | *Informed* — notified of outcome after the decision or action; one-way communication. |

**Column abbreviations used in the matrix:**

| Abbreviation | Stakeholder |
|---|---|
| DIR | BIRDC Director (STK-001) |
| FD | Finance Director (STK-002) |
| IT | IT Administrator (STK-003) |
| PARL | Parliament Budget Committee (STK-004) |
| CON | Consultant — Peter Bamuhigire (STK-005) |
| SMM | Sales and Marketing Manager (STK-006) |
| PM | Procurement Manager (STK-007) |
| SM | Store Manager (STK-008) |
| PROD | Factory / Production Manager (STK-009) |
| QC | QC Manager (STK-010) |
| HR | HR Manager (STK-011) |
| PAY | Payroll Officer (STK-012) |
| RES | Research Coordinator (STK-013) |
| ADM | Administration Officer (STK-014) |
| AGT | Field Sales Agents (STK-015) |

---

## 3.2 Phase 1 — Commerce Foundation (F-001, F-002, F-003, F-004)

| Activity | DIR | FD | IT | CON | SMM | SM | AGT |
|---|---|---|---|---|---|---|---|
| Sales module (F-001) requirements sign-off | A | C | C | R | C | I | I |
| POS module (F-002) requirements sign-off | I | C | C | R | A | I | C |
| Inventory module (F-003) requirements sign-off | I | C | C | R | C | A | I |
| Agent Distribution (F-004) requirements sign-off | I | C | C | R | A | C | C |
| Sales Agent App UAT | I | I | C | A | R | I | R |
| Warehouse App UAT | I | I | C | A | C | R | I |
| Phase 1 go / no-go sign-off | A | C | C | R | C | C | I |

---

## 3.3 Phase 2 — Financial Core (F-005, F-006, F-007, F-008)

| Activity | DIR | FD | IT | CON | SMM | PM | PARL |
|---|---|---|---|---|---|---|---|
| GL / Dual-mode accounting (F-005) specification | C | A | C | R | I | I | I |
| AR module (F-006) specification | I | A | C | R | C | I | I |
| AP module (F-007) specification | C | A | C | R | I | C | I |
| Budget management (F-008) specification | A | C | C | R | I | I | C |
| Hash chain integrity specification (BR-013) | C | A | R | C | I | I | I |
| Phase 2 UAT | I | A | C | R | I | I | I |
| Parliamentary reporting format review | A | C | I | C | I | I | A |
| Phase 2 go / no-go sign-off | A | C | C | R | I | I | I |

---

## 3.4 Phase 3 — Supply Chain and Farmers (F-009, F-010)

| Activity | DIR | FD | IT | CON | PM | SM | AGT |
|---|---|---|---|---|---|---|---|
| Procurement module (F-009) specification | C | C | I | R | A | C | I |
| PPDA workflow design | A | C | I | R | C | I | I |
| Farmer Management (F-010) specification | C | C | I | R | A | I | I |
| 5-stage cooperative workflow specification | C | C | I | R | A | I | I |
| Farmer Delivery App UAT | I | I | C | A | R | I | I |
| Farmer bulk payment API integration test | I | A | R | C | C | I | I |
| Phase 3 go / no-go sign-off | A | C | C | R | C | I | I |

---

## 3.5 Phase 4 — Production and Quality (F-011, F-012)

| Activity | DIR | FD | IT | CON | PROD | QC | SM |
|---|---|---|---|---|---|---|---|
| Manufacturing module (F-011) specification | C | C | I | R | A | C | C |
| Circular economy mass balance specification (BR-008) | C | C | I | R | A | C | I |
| QC module (F-012) specification | C | C | I | R | C | A | I |
| CoA template design (domestic and export) | I | I | I | C | I | A | I |
| Factory Floor App UAT | I | I | C | A | R | C | C |
| QC gate specification (BR-004) | I | C | I | R | C | A | I |
| Phase 4 go / no-go sign-off | A | C | C | R | C | C | I |

---

## 3.6 Phase 5 — People (F-013, F-014)

| Activity | DIR | FD | IT | CON | HR | PAY |
|---|---|---|---|---|---|---|
| HR module (F-013) specification | C | C | C | R | A | C |
| Payroll module (F-014) specification | C | A | C | R | C | C |
| PAYE / NSSF / LST configuration specification | I | A | I | R | C | C |
| ZKTeco biometric integration specification | I | C | A | R | C | I |
| HR Self-Service App UAT | I | C | C | A | R | I |
| Payroll UAT | I | A | I | C | C | R |
| Phase 5 go / no-go sign-off | A | C | C | R | C | C |

---

## 3.7 Phase 6 — Research, Administration and Compliance (F-015, F-016)

| Activity | DIR | FD | IT | CON | RES | ADM | PM |
|---|---|---|---|---|---|---|---|
| R&D module (F-015) specification | C | C | I | R | A | I | I |
| Asset register and administration (F-016) specification | C | C | I | R | I | A | I |
| PPDA document management configuration | C | C | I | R | I | C | A |
| Phase 6 UAT | I | C | C | A | R | R | R |
| Phase 6 go / no-go sign-off | A | C | C | R | I | I | I |

---

## 3.8 Phase 7 — Integration, Hardening and Go-Live (F-017, F-018, F-019)

| Activity | DIR | FD | IT | CON | SMM | PM | PARL |
|---|---|---|---|---|---|---|---|
| System Administration (F-017) configuration | C | C | A | R | I | I | I |
| EFRIS full integration (F-018) testing | I | A | R | C | I | I | I |
| OWASP / penetration test | C | I | A | C | I | I | I |
| Load testing (140 MT/day scenario) | C | I | A | R | I | I | I |
| Full regression testing | I | C | A | R | C | C | I |
| Staff training delivery | I | C | C | A | R | R | I |
| Go-live cutover execution | A | C | A | R | C | C | I |
| Post-go-live hypercare (30 days) | I | C | A | R | C | C | I |
| Final deliverable sign-off and handover | A | C | C | A | I | I | I |

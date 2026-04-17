# Domain Context — BIRDC ERP

**Primary Domain:** Agriculture + Manufacturing
**Secondary Domain:** Uganda Government Compliance (cross-cutting)

---

## Regulatory Bodies

| Body | Relevance |
|---|---|
| Uganda Revenue Authority (URA) | EFRIS fiscal receipting, PAYE remittance, NSSF employer obligations, WHT, import duty |
| PPDA (Public Procurement and Disposal of Public Assets Authority) | All BIRDC procurement must comply with PPDA Act (procurement categories, documentation, approval thresholds) |
| NSSF Uganda | Monthly NSSF employer and employee contribution schedule in prescribed format |
| National Identification and Registration Authority (NIRA) | NIN validation for farmer and employee registration |
| Office of the Auditor General (OAG Uganda) | Annual audit of PIBID parliamentary accounts — 7-year audit trail retention required |
| Uganda Parliament / Budget Committee | Quarterly and annual reporting on parliamentary vote expenditure |
| ICPAU (Institute of Certified Public Accountants of Uganda) | Accounting standards and financial reporting for Ugandan entities |
| National Drug Authority / MAAIF | Food safety standards for banana flour and processed products (domestic) |
| Export destination regulators | South Korea MFDS, EU RASFF, Saudi SFDA, Qatar MOPH, US FDA — CoA and food safety documentation |
| Uganda National Bureau of Standards (UNBS) | Product quality standards for Tooke brand domestic sales |
| National Data Protection Office (NDPO) | Uganda Data Protection and Privacy Act 2019 — farmer personal data (GPS, NIN, mobile money) |

## Key Standards

| Standard | Application |
|---|---|
| Uganda Data Protection and Privacy Act 2019 | Farmer PII (NIN, GPS coordinates, photo, mobile money number), employee data |
| Uganda PPDA Act (Cap 305) | All procurement transactions classification and documentation |
| Uganda Income Tax Act (Cap 340) | PAYE calculation, WHT obligations, 7-year record retention |
| Uganda NSSF Act | NSSF contribution calculation and remittance |
| IFRS for SMEs | Commercial financial reporting for BIRDC |
| ISO 22000 | Food safety management — relevant to QC module and CoA |
| Codex Alimentarius | International food standards referenced in export CoA |
| IEEE 830-1998 | SRS requirements specification standard |
| IEEE 1012-2012 | Software verification and validation |
| IEEE 829-2008 | Test documentation |

## Agriculture / Processing Domain Defaults (BIRDC-specific)

- **Farmer PII:** GPS farm coordinates, NIN, photo — encrypted at rest; access restricted to Procurement and Finance
- **Traceability chain of custody:** raw matooke → processing → finished product → CoA → export shipment; fully traceable
- **Offline-first:** rural cooperative collection points, factory floor, and field agent operations all require offline capability
- **Mobile money integration:** MTN MoMo and Airtel Money for farmer payments, agent remittances, and casual worker salaries
- **Circular economy accounting:** banana peel → biogas → factory power (valued as cost saving); waste water → bio-slurry fertiliser (valued as by-product revenue or farmer input)
- **Cooperative structure:** farmers → cooperatives → zones → BIRDC network (3-level hierarchy for procurement aggregation and reporting)

## Uganda Government Compliance Defaults (BIRDC-specific)

- **Parliamentary budget vote tracking:** segment/cost centre accounting aligned to PIBID vote codes
- **PPDA procurement documentation:** every purchase must have complete PPDA documentation on file
- **EFRIS real-time compliance:** every commercial invoice and POS receipt submitted to URA EFRIS on posting
- **7-year audit trail retention:** all financial records retained for 7 years per Uganda Companies Act and Income Tax Act
- **OAG audit readiness:** trial balance, GL detail, and audit trail exportable in formats suitable for OAG review

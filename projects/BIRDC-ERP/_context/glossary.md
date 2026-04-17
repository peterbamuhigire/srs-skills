# Glossary — BIRDC ERP

All domain-specific, regulatory, and project-specific terms used in the BIRDC ERP
documentation suite. IEEE Std 610.12-1990 terminology applies for software engineering terms.

---

| Term | Definition |
|---|---|
| BIRDC | Banana Industrial Research and Development Centre — the commercial and R&D entity operating the Nyaruzinga factory. |
| PIBID | Presidential Initiative on Banana Industrial Development — the government body (established by Presidential directive, 2005) that funds BIRDC and is accountable to Uganda Parliament. |
| Tooke | The brand name for BIRDC's range of banana-based products (flour, chips, juice, fibre, etc.). |
| Agent | A field sales agent employed or contracted by BIRDC to sell Tooke products in a defined territory. BIRDC has 1,071 agents. |
| Agent Cash Balance | The real-time net liability of an agent: total cash collected from sales minus total verified remittances. |
| Agent Stock Balance | The current monetary value and quantity of Tooke products held in an agent's virtual inventory store. Maintained in `tbl_agent_stock_balance`, completely separate from warehouse stock. |
| CoA | Certificate of Analysis — a laboratory document certifying that a finished product batch meets all specified quality parameters. Required for export. |
| Cooperative | A group of smallholder farmers organised for collective matooke procurement. Farmers deliver matooke to cooperative collection points. |
| Circular Economy | BIRDC's production model in which 100% of input matooke is converted to value: primary products (flour, chips), by-products (biogas from peels, bio-slurry fertiliser from waste water), and traceable scrap. |
| DC | Design Covenant — one of 7 binding design constraints that every requirement must satisfy. |
| Dual-Mode Accounting | The requirement to track PIBID parliamentary budget votes (government accounting) and BIRDC commercial accounts (IFRS) simultaneously in the same system. |
| Dual-Track Inventory | The architectural principle that warehouse stock and agent field stock are maintained in entirely separate database tables and are never merged except in explicitly labelled consolidated reports. |
| EFRIS | Electronic Fiscal Receipting and Invoicing Solution — Uganda Revenue Authority's system-to-system API for real-time fiscal document submission. All commercial invoices and POS receipts must be submitted to URA EFRIS. |
| FEFO | First Expiry First Out — inventory allocation rule: the batch with the earliest expiry date is always selected first for sales, transfers, and production inputs. |
| FDN | Fiscal Document Number — the unique identifier returned by URA EFRIS for each successfully submitted fiscal document. Printed on all invoices and receipts. |
| Float Limit | The maximum monetary value of inventory an agent may hold at any time. Configured per agent by the Sales Manager. Stock issuance is blocked if it would exceed this limit. |
| GL | General Ledger — the master financial record of all accounting transactions. |
| GRN | Goods Receipt Note — a document recording the receipt of goods into inventory, linked to a Purchase Order. |
| Hash Chain | A cryptographic technique where each GL entry contains the hash of the previous entry. Any modification to a historical entry breaks the chain and is detectable. |
| ICPAU | Institute of Certified Public Accountants of Uganda — the professional body governing accounting standards in Uganda. |
| Imprest | A fixed cash float maintained for petty cash disbursements, replenished periodically. |
| JE | Journal Entry — a balanced double-entry bookkeeping record (debits equal credits). |
| LPO | Local Purchase Order — the standard procurement document used in Uganda government and institutional procurement. |
| LST | Local Service Tax — a tax levied by local governments on employees, deducted from salary. Rates vary by local government ordinance (Bushenyi, Kampala). |
| Mass Balance | The verification that: Total Input (kg) = Primary Product Output (kg) + By-product Output (kg) + Scrap/Waste (kg). A core circular economy control. |
| Matooke | Fresh green bananas (Musa spp., AAB group) — the raw material input to BIRDC's processing. |
| NCR | Non-Conformance Report — a QC document raised when a quality failure is detected, with root cause analysis and corrective action. |
| NIN | National Identification Number — Uganda's national ID number, required for farmer registration and employee records. |
| NSSF | National Social Security Fund — Uganda's mandatory pension scheme. Employer contributes 10%; employee contributes 5% of gross salary. |
| OAG | Office of the Auditor General — Uganda's supreme audit institution. |
| PAYE | Pay As You Earn — Uganda income tax withheld from employee salaries by the employer and remitted monthly to URA. |
| POS | Point of Sale — any transaction where a physical product changes hands against immediate payment. Three contexts: factory gate, distribution centre, agent checkout. |
| PPDA | Public Procurement and Disposal of Public Assets Authority — Uganda's public procurement regulator. All BIRDC procurement must comply with the PPDA Act. |
| PRD | Product Requirements Document — the high-level business requirements for the BIRDC ERP system. |
| QC | Quality Control — the department and module responsible for inspection, CoA issuance, and SPC. |
| Remittance | Cash payment made by an agent to BIRDC, representing proceeds from field sales. Allocated to outstanding invoices via FIFO. |
| RFQ | Request for Quotation — a procurement document sent to multiple suppliers to obtain competitive quotes. |
| SPC | Statistical Process Control — quality management technique using control charts (X-bar, R-chart) and capability indices (Cp, Cpk). |
| TIN | Tax Identification Number — issued by URA to BIRDC for tax compliance purposes. Printed on all fiscal documents. |
| URA | Uganda Revenue Authority — the national tax body. BIRDC must comply with EFRIS, PAYE remittance, NSSF returns, and WHT obligations. |
| Vote | A parliamentary budget allocation category. PIBID budget is divided into votes (e.g., Development Vote, Recurrent Vote) that must be tracked and reported to Parliament. |
| WHT | Withholding Tax — 6% deducted from payments to local service suppliers per Uganda Income Tax Act. BIRDC is a withholding agent. |
| WIP | Work In Progress — inventory at intermediate processing stages. Posted as DR WIP / CR Raw Material Inventory when materials are issued to production. |
| ZKTeco | The brand of biometric fingerprint attendance devices deployed at BIRDC. Attendance data is imported directly into the HR module. |

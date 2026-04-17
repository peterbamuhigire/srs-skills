# Section 1: Executive Summary

## 1.1 What is BIRDC ERP?

BIRDC ERP is a purpose-built, single-tenant enterprise resource planning system designed exclusively for the Banana Industrial Research and Development Centre (BIRDC) and its parent government body, the Presidential Initiative on Banana Industrial Development (PIBID), operating at Nyaruzinga Hill, Bushenyi District, Western Uganda.

The system covers all 17 operational domains of BIRDC's business: sales and distribution, point of sale (POS) and agent management, inventory and warehouse management, financial accounting (dual-mode: parliamentary and commercial), procurement (including a 5-stage cooperative farmer procurement workflow), manufacturing and production, quality control and laboratory management, human resources, payroll, research and development, administration, PPDA compliance, EFRIS tax compliance, and system administration.

6 Android mobile applications extend the system to the field: the Sales Agent App serves 1,071 field agents with offline POS; the Farmer Delivery App registers deliveries from 6,440+ cooperative farmers; the Warehouse App supports barcode-driven stock management; the Executive Dashboard App delivers real-time financial summaries to the Director and Finance Director; the HR Self-Service App serves 150+ staff; and the Factory Floor App supports production supervisors and quality control staff.

## 1.2 Why is BIRDC ERP Needed?

BIRDC operates Uganda's only industrial-scale banana processing enterprise. Its operational reality is unique in three ways that no existing commercial ERP addresses:

**1. The dual-accountability mandate.** BIRDC is simultaneously a parliamentary-accountable government entity (PIBID, receiving budget votes reported to Uganda Parliament) and a commercial enterprise (BIRDC, trading under the Tooke brand, pursuing export contracts to South Korea, Saudi Arabia, Qatar, Italy, and the United States, and required to produce IFRS-compliant financial statements). Every financial transaction must satisfy both reporting regimes concurrently. No off-the-shelf ERP offers this dual-mode accounting natively.

**2. The 1,071-agent cash accountability gap.** BIRDC distributes Tooke products through 1,071 field sales agents. Each agent holds physical stock and collects cash from customers. Without a real-time agent cash balance system, cash collected but not remitted is undetectable until manual reconciliation — days or weeks after the fact. The resulting cash gap represents a material financial control weakness that cannot be closed with a standard accounts receivable module.

**3. Cooperative farmer procurement.** BIRDC sources matooke from 6,440+ farmers organised into cooperatives. Each batch delivery from a cooperative must be broken down to individual farmer contributions — name, National Identification Number (NIN), weight, quality grade, and net payable — before the batch can be receipted into inventory and the cooperative paid. This 5-stage workflow does not exist in any off-the-shelf procurement module.

Beyond these three structural gaps, BIRDC faces Uganda-specific compliance obligations (Uganda Revenue Authority EFRIS real-time fiscal document submission, PPDA procurement documentation, PAYE and NSSF payroll statutory formats) and operational constraints (intermittent connectivity at Nyaruzinga requiring offline-first mobile capability, data sovereignty requirements precluding SaaS hosting, and a factory processing up to 140 metric tonnes of matooke per day).

## 1.3 Why No Off-the-Shelf ERP Solves BIRDC's Problems

The shortfall of generic ERP platforms is structural, not cosmetic. It is documented in Section 8 (Constraints) and analysed in detail in the companion Business Case document. In summary:

- *SAP Business One and Oracle NetSuite* require subscription fees of USD 20,000–100,000+ per year, have no Uganda EFRIS integration, no PPDA compliance module, no cooperative farmer procurement workflow, and mandate cloud hosting — violating BIRDC's data sovereignty requirement (DC-006).
- *Odoo and ERPNext* are open-source platforms that require substantial custom module development to replicate BIRDC's dual-mode accounting, agent cash balance tracking, cooperative farmer procurement, and FEFO-enforced dual-track inventory. The total cost of customisation, Uganda localisation, and ongoing maintenance would equal or exceed a purpose-built system, without the operational fit.

A purpose-built system configured to BIRDC's exact rules — and designed for replication to other Uganda government agro-processors (DC-007) — is the economically and operationally correct solution.


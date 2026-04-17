## 3.4 Module F-004: Agent Distribution Management

### 3.4.1 Overview

Module F-004 manages BIRDC's 1,071-agent field sales network. Each agent operates an independent virtual inventory store, maintains a real-time cash balance (a liability to BIRDC), submits cash remittances that are allocated by FIFO to outstanding invoices, and earns commission on verified sales. This module eliminates the cash accountability gap that currently exists in BIRDC's field agent operations.

### 3.4.2 Functional Requirements — Agent Distribution Management

---

**FR-AGT-001** — Agent Registration

When a Sales Manager creates a new agent record, the system shall capture: first name, last name, National Identification Number (NIN), date of birth, gender, photo (uploaded file), contact phone number (MTN/Airtel), mobile money number and provider, physical address, district, territory assignment, sales point name, agent type (employed, contracted, or independent), commission rate (%), stock float limit (UGX), and agent status (active by default). All required fields shall be validated before the record is saved. NIN shall be unique across all agent records.

*Traceability: BG-003, DC-002, DC-003.*

---

**FR-AGT-002** — Agent Virtual Store Creation on Registration

When a new agent record is created and saved (FR-AGT-001), the system shall automatically create a corresponding virtual store entry for the agent in `tbl_agent_stock_balance` with all balances initialised to zero. No manual step shall be required to activate the agent's virtual store. The virtual store shall be permanently separate from all physical warehouse locations (BR-001).

*Traceability: BR-001, BR-006.*

---

**FR-AGT-003** — Agent Profile Edit and Audit

When a Sales Manager edits an agent's profile (any field), the system shall log the change in the audit trail recording: the field changed, old value, new value, editing user identity, and timestamp. Changes to the commission rate or stock float limit shall require Finance Manager approval (BR-003 — Sales Manager creates, Finance Manager approves).

*Traceability: BR-003, DC-003.*

---

**FR-AGT-004** — Agent Territory Assignment

When a territory is assigned to an agent, the system shall associate all invoices created by that agent or via the agent's customer portfolio with the assigned territory. An agent may be reassigned to a different territory; historical transactions shall retain the territory that was current at the time of the transaction. Territory definitions (name, geographic boundaries) shall be configurable by the Sales Manager (DC-002).

*Traceability: BG-003, DC-002.*

---

**FR-AGT-005** — Agent Cash Balance Calculation (Real-Time Liability)

The system shall calculate each agent's cash balance as: $\text{Agent Cash Balance} = \sum \text{Verified Sales Value} - \sum \text{Verified Remittances}$. This calculation shall be derived in real time from `tbl_invoices` and `tbl_remittances` tables, never from a stored static field. The balance shall be visible to the agent in the Sales Agent App and to the Sales Manager and Finance Director in the ERP.

*Traceability: BG-003, DC-003.*

---

**FR-AGT-006** — Agent Cash Balance Display

When an agent views their account summary in the Sales Agent App, the system shall display: current outstanding cash balance (owed to BIRDC), total sales for the current period, total remittances submitted for the current period, total verified remittances for the current period, commission accrued for the current period, and a transaction-level list of invoices and remittances in reverse chronological order.

*Traceability: BG-003, DC-001 (Samuel persona — accurate balance visibility).*

---

**FR-AGT-007** — Agent Stock Float Limit Enforcement on Issuance

When the warehouse initiates a stock issuance to an agent (FR-INV-013), the system shall query the agent's current stock balance value in `tbl_agent_stock_balance` (quantity multiplied by cost price per batch), add the value of the proposed issuance, and compare the sum to the agent's configured float limit. When the sum would exceed the float limit, the system shall block the issuance at the API layer and display the current balance, float limit, and proposed issuance value. The block cannot be overridden at the warehouse level — only a Sales Manager increasing the float limit unblocks issuance.

*Traceability: BR-006, BR-003.*

---

**FR-AGT-008** — Remittance Submission by Agent

When an agent submits a remittance via the Sales Agent App, the system shall record: agent identity, submission date and time, submitted amount (UGX), payment method (MTN MoMo, Airtel Money, bank deposit, or cash), payment reference number, and optional note. The remittance shall be recorded with status `submitted` (unverified). GL posting shall not occur until verification (FR-AGT-010).

*Traceability: BR-002, BR-003, DC-005 (offline submission queued).*

---

**FR-AGT-009** — Remittance Verification — Segregation of Duties

When a Finance Officer or Accounts Assistant reviews a submitted remittance, the system shall display the submission details and require verification (matching against bank or MoMo records). The system shall prevent the agent themselves and the agent's direct supervisor who submitted the record from verifying the same remittance (BR-003). The Finance Officer shall record the verified amount (which may differ from the submitted amount if there is a shortfall) and confirm verification.

*Traceability: BR-003, DC-003.*

---

**FR-AGT-010** — GL Auto-Posting on Remittance Verification

When a remittance is verified by the Finance Officer (FR-AGT-009), the system shall automatically post a GL journal entry: DR Cash / Bank (by payment method account) / CR Agent Receivable (agent's AR control account). The posting shall use the verified amount, the verification date, and the remittance reference number. The journal entry shall be linked to the remittance record by foreign key.

*Traceability: BG-001, DC-003, BR-013.*

---

**FR-AGT-011** — FIFO Remittance Allocation via Stored Procedure

When a remittance is verified (FR-AGT-010), the system shall call the database stored procedure `sp_apply_remittance_to_invoices` to allocate the verified remittance amount to the agent's outstanding invoices in FIFO order (oldest invoice first). The stored procedure shall: identify the oldest unpaid or partially paid invoice for the agent; apply the remittance amount to clear or partially clear that invoice; continue to the next oldest invoice with any remaining balance; and repeat until the remittance amount is fully allocated or all outstanding invoices are cleared. No manual selection of which invoice to clear is permitted.

*Traceability: BR-002, DC-003.*

---

**FR-AGT-012** — Partial Remittance Allocation

When a verified remittance amount is less than the oldest outstanding invoice balance, the stored procedure `sp_apply_remittance_to_invoices` shall apply the full remittance amount to the oldest invoice, reducing it to a partial balance, and record the partial allocation against that invoice. The invoice status shall transition from `issued` to `partially paid`.

*Traceability: BR-002, DC-003.*

---

**FR-AGT-013** — Commission Accrual on Verified Remittance

When a remittance is verified and allocated by `sp_apply_remittance_to_invoices` (FR-AGT-011), the system shall accrue commission for the agent on the value of invoices cleared by this remittance, calculated as: $\text{Commission Accrued} = \text{Cleared Invoice Value} \times \text{Agent Commission Rate}$. Commission accrues only on invoice values cleared by a verified remittance. Commission does not accrue on submitted-but-unverified remittances, nor at the time of invoice issuance (BR-015).

*Traceability: BR-015, DC-003.*

---

**FR-AGT-014** — Commission Period Run and Finance Manager Approval

When the Finance Manager initiates a commission period run, the system shall: aggregate all accrued commission for all agents for the selected period; display a commission run preview showing each agent's name, total sales cleared, commission rate, and commission amount; require Finance Manager approval before any GL posting occurs; and upon approval, post the GL entries (DR Commission Expense / CR Commission Payable per agent) and lock the commission run against further modification.

*Traceability: BR-003, BR-015, DC-003.*

---

**FR-AGT-015** — Commission Statement for Agent

When an agent requests a commission statement via the Sales Agent App, the system shall display: all commission-eligible periods, the invoices cleared per period (with dates and amounts), the commission rate applied, the commission amount per period, and the cumulative commission earned year-to-date. The statement shall be exportable as a PDF.

*Traceability: BR-015, STK-015.*

---

**FR-AGT-016** — Agent Suspension Workflow

When an agent's outstanding cash balance exceeds a configurable automatic suspension threshold (default: UGX 2,000,000 or as configured by Sales Manager), the system shall: change the agent's status to `suspended`; send an automatic in-app and SMS notification to the agent stating their outstanding balance and the suspension reason; notify the Sales Manager by in-app alert; and block all further stock issuances to the suspended agent (FR-AGT-007 reinforcement).

*Traceability: BG-003, DC-002.*

---

**FR-AGT-017** — Agent Suspension Manual Override

When a Sales Manager manually suspends or reinstates an agent, the system shall require a reason code, record the action in the audit trail with the Sales Manager's identity and timestamp, and notify the agent by in-app and SMS message. A suspended agent's Sales Agent App shall display a suspension notice on login and block POS sale operations until the agent's status is restored to `active`.

*Traceability: BR-003, DC-003.*

---

**FR-AGT-018** — Agent Termination and Final Settlement

When a Sales Manager initiates agent termination, the system shall trigger a final settlement workflow: calculate the agent's final outstanding cash balance, calculate any unsettled commission balance, generate a final account statement, require the Finance Manager to approve the final settlement amounts, and block the agent's access to the Sales Agent App. After settlement, the agent record status shall be set to `terminated` — the record is retained permanently and not deleted.

*Traceability: BR-003, DC-003.*

---

**FR-AGT-019** — Agent Outstanding Balance Dashboard

When a Sales Manager or Finance Director views the agent performance dashboard, the system shall display a real-time table of all active agents showing: agent name, territory, current outstanding cash balance, balance as a percentage of their float limit, number of days the oldest unpaid invoice has been outstanding, and agent status. The table shall support sorting by any column and filtering by territory.

*Traceability: BG-003, STK-006, STK-002.*

---

**FR-AGT-020** — Territory Ranking Report

When a Sales Manager requests a territory ranking report for a specified period, the system shall rank all territories by: total verified sales (primary sort), total remittances received, total outstanding balance, and number of active agents. The report shall be downloadable as PDF and Excel.

*Traceability: BG-003, STK-006.*

---

**FR-AGT-021** — Agent Ranking Report

When a Sales Manager requests an agent ranking report for a specified period, the system shall rank all agents within a territory (or across all territories) by: total verified sales, total remittances, outstanding balance, number of invoices cleared, and commission earned. The report shall be filterable by territory and agent type.

*Traceability: BG-003, STK-006.*

---

**FR-AGT-022** — Agent Stock Balance Report

When a Store Manager or Sales Manager views an agent's stock account, the system shall display: all items currently held in the agent's virtual store (from `tbl_agent_stock_balance`), quantities per item per batch, expiry dates, cost value per batch, and total stock value. The total stock value shall be compared against the agent's float limit, and the remaining headroom shall be displayed.

*Traceability: BR-001, BR-006.*

---

**FR-AGT-023** — Agent Sales History Report

When a Sales Manager or Finance Director requests an agent's sales history for a date range, the system shall display all invoices created by or attributed to that agent, with: invoice number, customer name, date, total value, payments received against the invoice, outstanding balance, EFRIS FDN, and current status.

*Traceability: BG-003, DC-003.*

---

**FR-AGT-024** — Agent Remittance History

When a Finance Officer or Sales Manager views an agent's remittance history, the system shall display all remittances (submitted and verified) for the selected agent and date range: remittance reference, submission date, submitted amount, verified amount (if verified), verification date, verifier identity, and the invoices allocated by the remittance (links to FR-AGT-011 allocation records).

*Traceability: BR-002, DC-003.*

---

**FR-AGT-025** — Automatic Balance Threshold Alert to Sales Manager

When any agent's outstanding cash balance increases (triggered on each invoice confirmation or remittance adjustment) and the new balance crosses a configurable warning threshold (default: 80% of float limit), the system shall send an in-app notification to the Sales Manager listing the agent name, territory, current balance, and float limit.

*Traceability: BG-003, DC-002.*

---

**FR-AGT-026** — Agent Portal Access Control

When a field sales agent logs into the Sales Agent Portal (`/public/sales-agents/`), the system shall present only the modules relevant to the agent role: POS, stock enquiry, remittance submission, commission statements, and account summary. The agent shall have no access to any other agent's records, to warehouse stock balances, to invoice management for non-agent sales, or to any ERP management function. Access control is enforced at the API layer per the 8-layer RBAC model.

*Traceability: BR-001, DC-003.*

---

**FR-AGT-027** — Remittance Shortfall Recording

When a remittance is verified and the verified amount is less than the submitted amount, the system shall: record the shortfall as a separate line on the remittance record; send a notification to the agent showing the verified amount, submitted amount, and shortfall; allocate only the verified amount via FIFO (FR-AGT-011); and flag the shortfall for Finance Manager review.

*Traceability: BR-002, DC-003.*

---

**FR-AGT-028** — Mobile Money Remittance: MTN MoMo Integration

When an agent selects MTN MoMo as their remittance payment method in the Sales Agent App, the system shall: display the BIRDC MTN MoMo business number and the exact amount due; allow the agent to initiate the payment from their MTN MoMo wallet; record the MoMo transaction reference entered by the agent; and route the remittance to the Finance Officer for verification against MoMo transaction records. `[CONTEXT-GAP: GAP-002]`

*Traceability: BG-003, DC-005.*

---

**FR-AGT-029** — Agent Type Configuration

When a Sales Manager configures agent types, the system shall allow creation of named agent types (minimum: employed, contracted, independent) with type-specific default commission rates and float limits. On agent registration (FR-AGT-001), selecting an agent type shall pre-populate the commission rate and float limit fields with the type defaults, which the Sales Manager may override per individual agent.

*Traceability: DC-002.*

---

**FR-AGT-030** — Agent NIN Duplicate Check

When a new agent is being registered (FR-AGT-001), the system shall validate the NIN field against all existing agent records and all employee records. When a duplicate NIN is detected, the system shall block the registration and display the existing record (name and status) that holds the duplicate NIN. This prevents double registration and duplicate commission/payroll payments.

*Traceability: DC-003, BG-003.*

---

**FR-AGT-031** — Commission Rate Change Approval Workflow

When a Sales Manager proposes a change to an agent's commission rate, the system shall record the proposed new rate with a `pending approval` status, notify the Finance Manager for review, and apply the new rate only upon Finance Manager approval. The change effective date shall be the Finance Manager's approval date. Historical commission calculations shall use the rate that was current at the time of each verified remittance.

*Traceability: BR-003, DC-003.*

---

**FR-AGT-032** — Agent Performance Target Configuration

When a Sales Manager configures agent performance targets, the system shall allow entry of monthly and quarterly sales targets per agent (in UGX), separate from territory targets. Agent-level targets shall feed the performance dashboard (FR-AGT-019) with percentage achievement tracking.

*Traceability: BG-003, DC-002.*

---

**FR-AGT-033** — Agent Bulk Import via Excel

When a Sales Manager uploads an Excel file for bulk agent registration, the system shall validate each row (NIN uniqueness, required field completeness, territory code validity), display a preview of valid and invalid rows before committing, import all valid rows creating both agent records and virtual stores (FR-AGT-002), and generate an import result report. This supports the initial onboarding of the existing 1,071-agent network.

*Traceability: DC-002, STK-006.*

---

**FR-AGT-034** — Agent Receivable GL Account Mapping

When an agent record is created, the system shall create or map a unique Agent Receivable sub-account in the General Ledger chart of accounts (under the Agent Receivable control account). All GL postings for that agent's sales and remittances shall use this agent-specific sub-account. This enables per-agent AR balance visibility at GL level without requiring manual journal entries.

*Traceability: BG-001, BG-003, DC-003.*

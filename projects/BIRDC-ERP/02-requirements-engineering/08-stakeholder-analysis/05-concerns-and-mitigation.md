# Section 5: Key Stakeholder Concerns and Mitigation

This section documents the primary concerns of the five highest-risk stakeholder groups — Parliament, Finance Director, Field Agents, Cooperative Farmers, and OAG — and the system and process mitigations that address each concern.

Mitigations are classified as: **System Design** (built into the system architecture), **Configuration** (addressed via system configuration, per DC-002), or **Process** (addressed via organisational procedure and consultant guidance).

---

## 5.1 Parliament Budget Committee — Value for Money

**Concern:** Parliament has invested UGX 200 billion (~$54M) in BIRDC over 20 years. The Budget Committee expects the ERP system to demonstrate that this investment is being managed responsibly and that BIRDC can account for every shilling of parliamentary budget vote expenditure.

**Specific concerns:**

- Whether the system produces reports that satisfy parliamentary accounting standards (not just private-sector IFRS).
- Whether the system creates over-dependence on an external vendor.
- Whether the procurement of the ERP system itself is PPDA-compliant.

**Mitigations:**

| Concern | Mitigation | Classification |
|---|---|---|
| Parliamentary accounting standards | Dual-mode accounting (F-005, F-008) maintains PIBID parliamentary budget votes and BIRDC commercial accounts simultaneously. Statement of Receipts and Payments and Budget vs. Actual by Vote Code are generated natively (US-099). | System Design |
| External vendor dependence | DC-006 (Data Sovereignty): all BIRDC data is hosted on BIRDC's own servers in Uganda. The system is licensed to BIRDC; no SaaS vendor holds data as leverage. DC-007 (Replicable by Design): the same codebase is configurable for any Uganda government entity, reducing dependency on single-vendor expertise. | System Design |
| ERP procurement compliance | The ERP procurement process itself is executed under the PPDA Act. The consultant prepares a compliant specification document that BIRDC uses as the basis for tendering. All procurement documentation is maintained in the system post-go-live. | Process |
| Transparency of expenditure | Budget vote utilisation is visible in real time. Automatic alerts at 80% and 95% utilisation (BR-014). Director-level override with written justification required for over-vote expenditure (US-080). | System Design |

---

## 5.2 Finance Director — Dual-Mode Accounting Correctness

**Concern:** Grace currently reconciles two separate Excel workbooks: one for PIBID parliamentary accounts, one for BIRDC commercial accounts. She is acutely concerned that a single-database dual-mode system may produce reports that are internally inconsistent — PIBID parliamentary totals that do not agree with what Parliament expects, or IFRS commercial statements that diverge from the GL.

**Specific concerns:**

- Whether parliamentary vote codes and commercial account codes are correctly separated at the transaction level.
- Whether the system can generate a reconciliation that proves the two modes are internally consistent.
- Whether the hash chain audit trail will satisfy the OAG auditor who expects tamper-evident records.

**Mitigations:**

| Concern | Mitigation | Classification |
|---|---|---|
| Vote code / account code separation | Every transaction is tagged at entry with the accounting mode (PIBID parliamentary or BIRDC commercial) and the applicable account code and vote code. The chart of accounts includes 1,307 accounts with parliamentary vote codes mapped at account level — no manual tagging per transaction is required. | System Design |
| Internal consistency of the two modes | A Dual-Mode Reconciliation Report cross-checks that the sum of all parliamentary vote expenditures equals the corresponding GL account balances for the PIBID mode, and that consolidated statements correctly aggregate both modes. The report auto-flags any discrepancy to Grace. | System Design |
| Tamper-evident audit trail | BR-013 (GL Hash Chain): every GL entry is cryptographically linked to the previous entry. Grace can trigger a hash chain integrity verification at any time (US-026). The OAG auditor accesses the integrity report directly from the system. | System Design |
| Period-close independence | Financial statements are available on demand without period closing (DC-003). Grace can generate the Trial Balance, P&L, and Balance Sheet at any moment (US-023, US-029). | System Design |

---

## 5.3 Field Sales Agents — Offline Reliability and Balance Accuracy

**Concern:** 1,071 field sales agents operate in areas with intermittent or no 3G/4G coverage. Samuel (the agent persona) reports that agents lose trust in a system when the balance it shows differs from their manual calculation. Agents also fear that offline transactions may be lost or duplicated during sync, creating incorrect balances.

**Specific concerns:**

- Whether offline transactions will be lost if the phone dies before syncing.
- Whether the agent cash balance the system shows can be trusted as accurate.
- Whether the FIFO remittance allocation is transparent enough for agents to understand their outstanding balance.

**Mitigations:**

| Concern | Mitigation | Classification |
|---|---|---|
| Offline transaction durability | Offline transactions are stored in the device's local SQLite database with write-ahead logging (WAL mode). The database survives app restarts and device reboots. On sync, the server uses the device-generated transaction ID to detect and reject duplicates. | System Design |
| Balance accuracy | The agent cash balance is calculated as a deterministic formula: Total Invoiced Sales minus Total Verified Remittances. The formula is the same on the device (offline) and on the server; the sync reconciles both ledgers to zero variance. | System Design |
| FIFO remittance transparency | After each verified remittance, the system sends the agent a notification showing: which invoices were cleared by the remittance, the amount applied to each, and the new outstanding balance — providing a full allocation breakdown (US-012, US-019). | System Design |
| Commission trust | Commission is calculated on verified remittances only (BR-015). The agent commission statement shows the invoice-by-invoice breakdown of commission earned (US-014). | System Design |

---

## 5.4 Cooperative Farmers — Payment Accuracy

**Concern:** 6,440+ smallholder farmers depend on BIRDC payments for their livelihoods. Farmers have experienced payment disputes in the manual system where their recorded delivery weight or quality grade was disputed and they received less than expected. Farmers' unions have raised the accuracy of individual contribution tracking as a precondition for continued cooperative participation.

**Specific concerns:**

- Whether their individual delivery weight and quality grade will be accurately recorded.
- Whether deductions (loan repayments, cooperative levies) will be transparently disclosed before payment.
- Whether they will be notified of payment and be able to verify the amount.

**Mitigations:**

| Concern | Mitigation | Classification |
|---|---|---|
| Weight accuracy | Bluetooth scale integration in the Farmer Delivery App eliminates manual transcription of weight readings (US-071). Manually entered weights are flagged "M" in the record. | System Design |
| Quality grade dispute | The quality grade recorded at the collection point by Patrick (Collections Officer) is visible in the farmer's contribution record. Farmers receive a printed receipt at the collection point showing weight and grade (US-072). | System Design |
| Deduction transparency | The farmer's individual contribution record shows: gross payable, each deduction type and amount (loan repayment, cooperative levy), and net payable (US-047). This data is available in the Farmer Delivery App and in the Farmer Management module. | System Design |
| Payment notification | When the bulk mobile money payment batch is processed, each farmer receives an SMS payment confirmation from the mobile money provider with the payment amount and transaction reference (US-030). | System Design |
| Historical access | Patrick can retrieve any farmer's full delivery and payment history from the Farmer Delivery App to answer farmer queries in the field (US-076). | System Design |

---

## 5.5 Auditor General (OAG Uganda) — Audit Trail Completeness

**Concern:** The OAG Uganda is the supreme audit institution for BIRDC's parliamentary expenditure. The OAG expects that the ERP system produces a complete, tamper-evident audit trail for every financial transaction, and that the audit team can access any transaction from the last 7 years without requiring BIRDC staff to generate manual extracts.

**Specific concerns:**

- Whether the audit trail is truly tamper-evident (not just a software log that can be deleted by an administrator).
- Whether the 7-year retention requirement under the Uganda Companies Act and Income Tax Act is met.
- Whether the OAG auditor can trace every payment from the bank statement back to the original transaction trigger (invoice, PO, production order) without manual cross-referencing.

**Mitigations:**

| Concern | Mitigation | Classification |
|---|---|---|
| Tamper-evident records | BR-013 (GL Hash Chain Integrity): every GL entry contains the cryptographic SHA-256 hash of the previous entry. Any modification to a historical record breaks the chain. The hash chain verification function is accessible to the Finance Director and OAG auditor directly from the system and produces a dated certificate (US-026). | System Design |
| 7-year retention | DC-003 (Audit Readiness by Design): 7-year retention is enforced by the backup retention policy configuration (US-095). The IT Administrator configures a minimum retention period of 84 months; the system rejects any backup deletion policy that would result in records being purged before 7 years. | System Design + Configuration |
| End-to-end transaction traceability | Every payment record links to: vendor invoice → GRN → LPO (standard supplier) or cooperative batch record → individual farmer contribution (farmer payment). Every sales invoice links to: customer → POS session or order → EFRIS FDN. The OAG auditor can navigate the full chain from the audit log search screen (US-094). | System Design |
| No-manual-reconciliation requirement | The success criterion for Phase 2 delivery is: "External audit (OAG Uganda) requires no manual reconciliation — full audit trail in system." This is a go-live acceptance criterion, not a post-delivery aspiration. | Process |
| Audit log access control | The audit log is read-only for all users including the IT Administrator. The OAG auditor is granted read-only access to the audit log for the audit period. | System Design |

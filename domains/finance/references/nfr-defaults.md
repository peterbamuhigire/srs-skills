# Finance: Default Non-Functional Requirements

These requirements are auto-injected into new finance project scaffolds.
All blocks are tagged `[DOMAIN-DEFAULT: finance]` for consultant review.

---

<!-- [DOMAIN-DEFAULT: finance] Source: domains/finance/references/nfr-defaults.md -->
#### FIN-NFR-001: Financial Audit Trail
The system shall maintain a complete, tamper-proof audit log of all create,
read, update, and delete operations on financial account data and transaction
records in compliance with SOX Section 802 and PCI-DSS v4.0 Requirement 10.

**Verifiability:** Execute a financial transaction; verify that an immutable
audit log entry is created containing: user_id, timestamp, action, transaction_id,
account_id, amount, and outcome. Attempt to modify or delete the log entry;
the system shall reject the modification and return an error.
<!-- [END DOMAIN-DEFAULT] -->

---

<!-- [DOMAIN-DEFAULT: finance] Source: domains/finance/references/nfr-defaults.md -->
#### FIN-NFR-002: Transaction Atomicity
The system shall guarantee ACID properties for all financial transactions.
If any component of a multi-leg transaction fails, the system shall roll back
all associated ledger entries, leaving account balances in their pre-transaction state.

**Verifiability:** Inject a simulated failure at the credit leg of a debit-credit
transaction pair; verify that the debit entry is rolled back and the source account
balance remains unchanged. Confirm via ledger query that no partial entries exist.
$\sum Debits = \sum Credits$ must hold true at all times.
<!-- [END DOMAIN-DEFAULT] -->

---

<!-- [DOMAIN-DEFAULT: finance] Source: domains/finance/references/nfr-defaults.md -->
#### FIN-NFR-003: Card Data Security
The system shall never store, process, or transmit unencrypted Primary Account
Numbers (PANs) outside the designated Cardholder Data Environment (CDE), in
compliance with PCI-DSS v4.0 Requirements 3 and 4. All stored PANs must be
rendered unreadable via tokenization or AES-256 encryption.

**Verifiability:** Inspect all database tables, log files, and application
memory dumps outside the CDE; no full PAN shall be present in plaintext.
Run a PAN scanning tool (e.g., PANalyzer) against all storage systems outside
the CDE; the scan must return zero matches.
<!-- [END DOMAIN-DEFAULT] -->

---

<!-- [DOMAIN-DEFAULT: finance] Source: domains/finance/references/nfr-defaults.md -->
#### FIN-NFR-004: Availability for Transaction Processing
The system shall maintain 99.99% uptime availability
($\leq 52.6$ minutes downtime per year) for all transaction processing
and payment authorization modules, measured on a rolling 12-month basis.

**Verifiability:** Monitor uptime continuously over 30 days using an
independent monitoring service; calculate availability as:
$Availability = \frac{MTTF}{MTTF + MTTR} \times 100\%$
The result must be $\geq 99.99\%$ for the measurement period.
<!-- [END DOMAIN-DEFAULT] -->

---

<!-- [DOMAIN-DEFAULT: finance] Source: domains/finance/references/nfr-defaults.md -->
#### FIN-NFR-005: Fraud Detection Response Time
The system shall evaluate each payment transaction against the fraud detection
risk-scoring engine and return an APPROVE, REVIEW, or DECLINE decision within
200 milliseconds at the 99th percentile under normal production load.

**Verifiability:** Submit 10,000 representative payment authorization requests
at peak throughput; measure the end-to-end latency from transaction receipt to
fraud decision. The 99th percentile latency must be $\leq 200\text{ms}$.
Verify that no transaction proceeds to settlement without a recorded fraud decision.
<!-- [END DOMAIN-DEFAULT] -->

---

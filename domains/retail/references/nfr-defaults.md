# Retail: Default Non-Functional Requirements

These requirements are auto-injected into new retail project scaffolds.
All blocks are tagged `[DOMAIN-DEFAULT: retail]` for consultant review.

---

<!-- [DOMAIN-DEFAULT: retail] Source: domains/retail/references/nfr-defaults.md -->
#### RET-NFR-001: Cardholder Data Protection
The system shall never store, process, or transmit unencrypted Primary Account
Numbers (PANs) or Card Verification Values (CVV/CVC) outside the designated
Cardholder Data Environment (CDE), in compliance with PCI-DSS v4.0 Requirements
3 and 4. All PANs stored in the token vault must be rendered unreadable via
AES-256 encryption or format-preserving tokenization.

**Verifiability:** Inspect all database tables, application logs, and file stores
outside the designated CDE; no full PAN or CVV shall be present in plaintext or
recoverable form. Execute a PAN-scanning tool (e.g., PANalyzer) across all
out-of-scope storage; the scan must return zero matches. Verify that CVV fields
are absent from all storage layers post-authorization.
<!-- [END DOMAIN-DEFAULT] -->

---

<!-- [DOMAIN-DEFAULT: retail] Source: domains/retail/references/nfr-defaults.md -->
#### RET-NFR-006: Product Data Quality
The system shall prevent publication of sellable products whose required product data is incomplete for the active channel, including SKU, product name, category, price, tax class, fulfilment eligibility, return eligibility, inventory status, searchable attributes, product image or media rule, and accessibility text for meaningful images.

**Verifiability:** Attempt to publish 50 products with missing required fields across web, POS, and marketplace channels. The system must block publication for every incomplete product, identify the missing fields, and create an exception record with owner, channel, and due date.
<!-- [END DOMAIN-DEFAULT] -->

---

<!-- [DOMAIN-DEFAULT: retail] Source: domains/retail/references/nfr-defaults.md -->
#### RET-NFR-007: Retail Event Auditability
The system shall preserve an immutable audit trail for every retail event that can affect price, discount, promotion, markdown, inventory, refund, loyalty balance, gift card/store credit, vendor funding, shrink, or financial reporting. Each event must record event ID, actor, role, timestamp, source system, previous state, new state, reason code, approval status, and evidence pointer where applicable.

**Verifiability:** Sample 100 events across price change, promotion approval, manual discount, refund, stock adjustment, return disposition, vendor funding claim, and shrink incident. Each sampled event must contain the required audit fields and must not allow destructive edit or deletion after posting; corrections must be represented by reversal or superseding event.
<!-- [END DOMAIN-DEFAULT] -->

---

<!-- [DOMAIN-DEFAULT: retail] Source: domains/retail/references/nfr-defaults.md -->
#### RET-NFR-008: Dashboard Freshness and Lineage
The system shall show data freshness, source system, transformation rule, and reconciliation status for every retail KPI used in an executive, finance, merchandising, store operations, fulfilment, or weekly business review dashboard.

**Verifiability:** Select gross sales, gross margin, markdown rate, return rate, fulfilment SLA, shrink rate, stock cover, and vendor funding recovery in the dashboard. Each metric must expose source system, latest refresh timestamp, transformation rule, and reconciliation status. Metrics whose source data is stale or unreconciled must display a visible exception status.
<!-- [END DOMAIN-DEFAULT] -->

<!-- [DOMAIN-DEFAULT: retail] Source: domains/retail/references/nfr-defaults.md -->
#### RET-NFR-002: Checkout Performance
The system shall render each step of the checkout flow — including cart review,
address entry, shipping selection, and payment confirmation pages — within
2 seconds at the 95th percentile for users on a standard broadband connection
(10 Mbps), under peak load equivalent to 150% of average daily transaction volume.

**Verifiability:** Execute a load test simulating peak traffic (150% of average
daily volume) using a performance testing tool (e.g., k6, JMeter). Measure
page load time for each checkout step; the 95th percentile must be
$\leq 2000\text{ms}$. Validate using WebPageTest from at least two geographic
regions serving the primary customer base.
<!-- [END DOMAIN-DEFAULT] -->

---

<!-- [DOMAIN-DEFAULT: retail] Source: domains/retail/references/nfr-defaults.md -->
#### RET-NFR-003: Consumer Data Rights
The system shall fulfill verified consumer requests to export or permanently
delete their personal information within 30 days of request receipt, in compliance
with GDPR Article 17 (right to erasure) and CCPA. The deletion shall cascade
to all downstream data stores, data warehouses, and third-party processors
under a signed Data Processing Agreement.

**Verifiability:** Submit a verified deletion request for a test consumer account.
After 30 days, query all primary databases, data warehouses, email marketing
platforms, and connected third-party systems; no personally identifiable information
for the deleted consumer shall be recoverable. Verify that order records required
for tax and legal retention obligations are anonymized rather than deleted.
<!-- [END DOMAIN-DEFAULT] -->

---

<!-- [DOMAIN-DEFAULT: retail] Source: domains/retail/references/nfr-defaults.md -->
#### RET-NFR-004: Inventory Accuracy
The system shall synchronize inventory stock levels across all sales channels
(e-commerce, POS, marketplace) within 5 seconds of a stock-changing event
(sale, return, manual adjustment, or receiving). Inventory quantities must
reflect the same value across all channels within the synchronization window.

**Verifiability:** Execute a test sale on one channel and immediately query the
inventory quantity on all other channels. Repeat across 100 test transactions;
in 99% of cases the inventory quantity on all channels must reflect the updated
stock level within $\leq 5$ seconds of the originating event.
<!-- [END DOMAIN-DEFAULT] -->

---

<!-- [DOMAIN-DEFAULT: retail] Source: domains/retail/references/nfr-defaults.md -->
#### RET-NFR-005: High Availability During Peak Sales Events
The system shall maintain 99.95% uptime availability
($\leq 4.38$ hours downtime per year) for all checkout and payment processing
modules during designated peak sales events (Black Friday, Cyber Monday, and
other events designated in the operational calendar).

**Verifiability:** Monitor uptime for checkout and payment modules continuously
during the declared peak sales event window. Calculate availability as:
$Availability = \frac{MTTF}{MTTF + MTTR} \times 100\%$
The result must be $\geq 99.95\%$ for the event window. Load test at 200% of
peak baseline before each major sales event; the system must sustain the load
without degradation to checkout response time.
<!-- [END DOMAIN-DEFAULT] -->

---

# Glossary — Longhorn ERP

*All terms defined per IEEE Std 610.12-1990 unless otherwise noted. Spell out on first use in each document, then use the abbreviation.*

## A

**Account Ledger** — The detailed record of all financial transactions posted to a specific GL account. Also referred to as a sub-ledger or T-account detail.

**Accounts Payable (AP)** — The aggregate of amounts owed by the organisation to suppliers for goods and services received but not yet paid.

**Accounts Receivable (AR)** — The aggregate of amounts owed to the organisation by customers for goods and services delivered but not yet collected.

**Add-On Module** — A licensed feature set that a tenant may activate independently of the core modules, subject to their subscription plan.

**Audit Log** — An immutable, INSERT-only record of every create, update, delete, and approval action performed within the system, capturing old values, new values, user identity, IP address, and timestamp.

## B

**Bill of Materials (BOM)** — A structured list of raw materials, components, and quantities required to manufacture one unit of a finished product.

**Branch** — A physical or logical sub-unit of a tenant organisation, such as a warehouse location, retail outlet, or regional office. Branches share a single tenant account.

**Balanced Scorecard (BSC)** — A strategic performance management framework that measures organisational performance across four perspectives: Financial, Customer, Internal Business Processes, and Learning and Growth.

## C

**Chart of Accounts (COA)** — The complete, hierarchical list of GL accounts used by a tenant to record financial transactions, structured per IFRS and the tenant's localisation profile.

**Core Module** — A module that is always active for every tenant and cannot be disabled. See: Accounting & GL, Inventory, Sales, Procurement, User Management & RBAC, Audit Log.

**Credit Note** — A document issued to a customer that reduces the amount owed, typically in response to a return or billing error.

**CSRF Token** — A Cross-Site Request Forgery token. A session-scoped security token required in the `X-CSRF-Token` header of all state-changing HTTP requests.

## D

**Double-Entry Accounting** — The accounting system in which every financial transaction is recorded as both a debit to one account and a credit to another, maintaining the accounting equation: Assets = Liabilities + Equity.

**Delivery Note** — A document that accompanies a shipment of goods from the organisation to a customer, listing the items and quantities delivered.

## E

**EFRIS** — Electronic Fiscal Receipting and Invoicing System. The URA-mandated system for real-time electronic submission of tax invoices in Uganda. See GAP-001.

**ERP** — Enterprise Resource Planning. A category of integrated management software that unifies core business processes — finance, supply chain, HR, sales, procurement, and more — into a single platform.

## F

**FEFO** — First Expired, First Out. A stock picking strategy that issues goods in order of expiry date, ensuring the earliest-expiring items are consumed first.

**FIFO** — First In, First Out. A stock valuation and picking method in which the oldest stock items are issued and valued before newer ones.

**FR** — Functional Requirement. A requirement that specifies a function or behaviour the system shall perform. Format: `FR-<MODULE>-<NNN>`.

## G

**General Ledger (GL)** — The master record of all financial transactions of a tenant, organised by account. The GL is the source of truth for all financial reporting.

**GRN** — Goods Receipt Note. A document that records the receipt of goods from a supplier against a purchase order, confirming quantity and condition.

## I

**IFRS** — International Financial Reporting Standards. The global accounting standards framework to which all financial reporting in Longhorn ERP conforms.

**Integration Layer** — The platform service responsible for all external API communication: URA EFRIS, MTN MoMo, Airtel Money, M-Pesa, KRA iTax, NSSF, Africa's Talking, and similar.

## J

**Journal Entry** — A double-entry accounting record consisting of two or more journal lines that together balance to zero (total debits = total credits).

**JWT** — JSON Web Token. A compact, URL-safe token format used for authenticating mobile API requests. Claims include `tenant_id`, `user_id`, `role`, and enabled modules.

## L

**Landed Cost** — The total cost of a purchased item inclusive of purchase price, freight, import duties, insurance, and other acquisition costs.

**Localisation Engine** — The platform service that applies country-specific and tenant-specific configuration (currency, language, tax rates, statutory deductions, COA, fiscal integration) without code changes.

**Localisation Profile** — A configuration record that defines all market-specific parameters for a tenant's jurisdiction.

**LPO** — Local Purchase Order. A purchase order document issued by an organisation to a local supplier, commonly used in East Africa.

## M

**Module** — A self-contained functional domain within Longhorn ERP (e.g., Accounting, HR & Payroll, POS). Modules are universal across all markets; localisation behaviour is configuration-driven.

**Multi-Tenancy** — The architecture in which a single instance of the software serves multiple independent organisations (tenants), each with complete data isolation.

**MoMo** — Mobile Money. Generic term for mobile-phone-based financial services. Specific services: MTN MoMo, Airtel Money, M-Pesa.

## N

**NFR** — Non-Functional Requirement. A requirement that specifies a quality attribute or constraint (performance, security, reliability, etc.) rather than a function. Format: `NFR-<CATEGORY>-<NNN>`. All NFRs must carry a measurable metric.

**NSSF** — National Social Security Fund. The statutory social security scheme in Uganda (and analogous bodies in Kenya, Tanzania, Rwanda).

## P

**PAYE** — Pay As You Earn. The statutory income tax deducted from employee salaries and remitted to the tax authority.

**POS** — Point of Sale. The system used to record retail sales transactions at the point of customer payment.

**PPDA** — Public Procurement and Disposal of Public Assets Authority. The Ugandan body governing public sector procurement. PPDA Act compliance is required for government and parastatal tenants.

**Prepared Statement** — A parameterised SQL query in which user-supplied values are bound separately from the query structure, preventing SQL injection.

**Production Order** — A manufacturing instruction to produce a specified quantity of a finished product, drawing raw materials from inventory against a BOM.

## R

**RBAC** — Role-Based Access Control. The security model in which users are assigned to roles, and roles are granted specific permissions per function and action (view, create, edit, approve, delete).

**Remittance** — A payment made to an agent or cooperative farmer, typically via mobile money, representing commissions, commodity payments, or salary.

## S

**SaaS** — Software as a Service. A software delivery model in which the application is hosted by the provider and accessed by tenants via the internet on a subscription basis.

**SRS** — Software Requirements Specification. A document that formally specifies the functional and non-functional requirements for a software system or module, per IEEE 830.

**Stock Ledger** — The immutable record of all stock movements (receipts, issues, adjustments, transfers) for every item, analogous to the GL for inventory.

**Strict Types** — The PHP language directive `declare(strict_types=1)` that enforces type safety on all function calls and assignments within a file.

## T

**Tenant** — An independent organisation that subscribes to Longhorn ERP and operates within its own isolated data environment.

**Tenant Context** — The service that provides the current `tenant_id` from the authenticated session. The `tenant_id` is NEVER accepted from client-supplied request parameters.

**Three-Way Matching** — The procurement control that verifies a supplier invoice against both the purchase order and the goods receipt note before approving payment.

## U

**UOM** — Unit of Measure. The unit in which a stock item is tracked (e.g., kg, litre, carton, piece). UOM conversions allow a single item to be purchased in one UOM and sold in another.

**URA** — Uganda Revenue Authority. The tax authority responsible for VAT, PAYE, withholding tax, and customs in Uganda.

## V

**VAT** — Value Added Tax. A consumption tax levied at each stage of the supply chain and remitted to the tax authority. Uganda standard rate: 18%.

**V&V** — Verification and Validation. The process of confirming that a system requirement is correctly specified (verification) and that the system meets stakeholder intent (validation), per IEEE 1012.

## W

**WHT** — Withholding Tax. Tax deducted at source by the paying organisation on behalf of the recipient, remitted to URA.

**WIP** — Work In Progress. Inventory that has entered the manufacturing process but has not yet been completed as a finished product.

**WMS** — Warehouse Management System. Advanced warehousing functionality including bin/rack location management, directed putaway, and directed picking.

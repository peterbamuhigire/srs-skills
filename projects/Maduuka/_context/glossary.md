# Glossary -- Maduuka

*All terms follow IEEE Std 610.12-1990 definition format.*

**Airtel Money:** Mobile money payment service operated by Airtel Uganda. Peer-to-peer and merchant payment capability.

**BOM (Bill of Materials):** A structured list of raw material components and their quantities required to manufacture or assemble a finished product or menu item.

**Branch:** A distinct physical location of a business operating under the same Maduuka business account.

**Cart:** The temporary record of items selected for purchase in the current POS transaction, prior to payment and receipt generation.

**CDE (Cardholder Data Environment):** Any system component that stores, processes, or transmits cardholder data or sensitive authentication data (PCI-DSS v4.0 definition).

**EFRIS:** Electronic Fiscal Receipting and Invoicing Solution. Uganda Revenue Authority's real-time digital invoicing system mandated for specified business categories from July 2025.

**FEFO (First Expiry, First Out):** A stock rotation method that ensures items with the nearest expiry date are dispensed or sold before items with later expiry dates.

**FIFO (First In, First Out):** A stock valuation and rotation method that assumes the oldest stock is sold or used first.

**FDN (Fiscal Document Number):** A unique transaction identifier issued by the URA EFRIS system upon successful submission of an invoice.

**Franchise ID:** A system-generated unique identifier assigned to each Maduuka business (tenant) account. Every database record is scoped to a franchise_id to enforce data isolation.

**Gross Margin:** The difference between revenue and the cost of goods sold, expressed as a percentage of revenue: GrossMargin% = (Revenue - COGS) / Revenue x 100.

**KDS (Kitchen Display System):** A screen mounted in a kitchen showing all active Kitchen Order Tickets, auto-refreshing and colour-coded by urgency.

**KOT (Kitchen Order Ticket):** A digital order record sent from a server to the kitchen containing table number, server name, items with quantities, special instructions, and timestamp.

**Landed Cost:** The total cost of a shipment of imported goods including the invoice price plus freight, insurance, customs duties, and clearing charges.

**LST (Local Service Tax):** A tax levied by Ugandan local governments on employed persons, with tiers varying by monthly gross salary and jurisdiction.

**MTN MoMo:** Mobile money payment service operated by MTN Uganda. The dominant mobile money platform in Uganda by transaction volume.

**NDA (National Drug Authority):** The regulatory body in Uganda responsible for the regulation of human and veterinary medicines. Enforces controlled drugs dispensing compliance.

**NSSF (National Social Security Fund):** Uganda's mandatory social security scheme. Employer contribution: 10% of gross salary. Employee contribution: 5% of gross salary.

**Offline-First:** A software design pattern in which the application is capable of full or near-full functionality without an active internet connection, storing all operations locally and synchronising when connectivity is restored.

**PAYE (Pay As You Earn):** Income tax deducted from employee salaries at source, calculated per the Uganda Income Tax Act tax bands and remitted to URA monthly.

**PIF (Project Input Folder):** The _context/ directory in this project. Contains all project-specific data that feeds SRS generation skills. Quality of output is directly proportional to completeness of PIF content.

**POS (Point of Sale):** The location and moment at which a retail transaction is completed between a buyer and seller. In this system: the POS module handles all sales transactions, payment collection, and receipt generation.

**PWA (Progressive Web Application):** A web application that uses modern browser APIs to deliver app-like experiences including offline operation, home screen installation, and push notifications.

**Receipt Gap:** A discontinuity in the sequential receipt numbering of a POS session, potentially indicating an unrecorded sale or deliberate receipt suppression.

**RevPAR (Revenue Per Available Room):** A hotel performance metric calculated as: RevPAR = OccupancyRate x AverageDailyRate.

**RBAC (Role-Based Access Control):** A method of restricting system access where permissions are assigned to roles, and users are assigned to roles rather than being granted permissions directly.

**SKU (Stock Keeping Unit):** A unique alphanumeric code assigned to a product to identify it in inventory management.

**Tenant:** A business account on the Maduuka SaaS platform. Each tenant's data is fully isolated from all other tenants via franchise_id scoping.

**TIN (Taxpayer Identification Number):** A unique identifier issued by URA to registered taxpayers in Uganda.

**UOM (Unit of Measure):** The unit in which a product is tracked, purchased, or sold (e.g., kg, litre, piece, box, pack).

**URA (Uganda Revenue Authority):** The government agency responsible for tax assessment and collection in Uganda. Mandates EFRIS compliance for specified business categories.

**Void:** The cancellation of a completed POS transaction, recorded in the audit log with the cashier's details, reason code, and timestamp.

**Warehouse:** A defined storage location within a branch where stock is held. A branch may have multiple warehouses (e.g., Main Store, Retail Floor, Cold Room).

**Water-Scrum-Fall:** A hybrid software development pattern combining formal upfront requirements (Waterfall) with iterative sprint-based delivery (Scrum), followed by a formal testing and release phase (Waterfall). Confirmed as Maduuka's methodology on 2026-04-05.

**WorkManager (Android):** The Android Jetpack API for scheduling deferrable background work, used in Maduuka for background data synchronisation.

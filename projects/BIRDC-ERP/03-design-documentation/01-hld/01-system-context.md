# 1. System Context

## 1.1 System Boundary

The BIRDC ERP is a single-tenant, on-premise enterprise resource planning system deployed at BIRDC Nyaruzinga, Bushenyi District. It is the operational backbone for both PIBID (parliamentary accountability) and BIRDC (commercial operations). The system manages 17 operational domains — from cooperative farmer matooke delivery through manufacturing, quality control, sales via 1,071 field agents, and export compliance.

The diagram below represents the system boundary and all external actors that exchange data with the BIRDC ERP.

## 1.2 External Systems and Interfaces

| External System | Direction | Protocol | Purpose |
|---|---|---|---|
| URA EFRIS API | Outbound | REST/HTTPS | Submit fiscal documents (invoices, POS receipts, credit notes) in real time; receive Fiscal Document Number (FDN) and QR code |
| MTN MoMo Business API | Bidirectional | REST/HTTPS | Push payment prompts to agents; bulk farmer payments; bulk casual worker salary disbursement; customer payment collection |
| Airtel Money API | Bidirectional | REST/HTTPS | Dual-provider redundancy for all MTN MoMo use cases |
| ZKTeco Biometric Devices | Inbound | ZKTeco SDK / local network | Import biometric fingerprint attendance records directly into the HR module |
| Android Mobile Apps (6) | Bidirectional | REST/HTTPS (JWT) | Sales Agent App, Farmer Delivery App, Warehouse App, Executive Dashboard App, HR Self-Service App, Factory Floor App |
| NSSF Uganda | Outbound | File export (NSSF format) | Monthly NSSF contribution schedule for employer remittance |
| Bank Bulk Payment | Outbound | File export (bank format) | Payroll bank credit transfers; bulk vendor payments |
| Africa's Talking (SMS/WhatsApp) | Outbound | REST/HTTPS | Agent and farmer SMS/WhatsApp notifications: payment confirmations, sales alerts, balance notifications |
| Export Market Buyers | Outbound | PDF document | Certificate of Analysis (CoA) for South Korea, Saudi Arabia, Qatar, Italy, and USA import compliance |
| OAG Uganda (Auditor General) | Outbound (on demand) | System access / report | Audit trail, GL hash chain integrity reports, financial statements |
| PPDA | Outbound (on demand) | Document export | Procurement documentation packages for compliance review |

## 1.3 Ecosystem Positioning

The BIRDC ERP sits at the centre of a government-commercial hybrid value chain:

- **Upstream (inputs):** 6,440+ cooperative farmers deliver matooke; the Farmer Delivery App and cooperative procurement module capture every kilogramme with individual farmer attribution.
- **Core (transformation):** The manufacturing, QC, and inventory modules convert raw matooke into Tooke products, by-products (biogas, bio-slurry), and scrap — with full mass balance accountability.
- **Downstream (distribution):** 1,071 field agents, factory gate POS, and export channels distribute Tooke products. The EFRIS API ensures every sale is fiscally compliant.
- **Accountability (reporting):** Dual-mode accounting reports simultaneously to Parliament (PIBID vote tracking) and to commercial stakeholders (IFRS financial statements and external auditors).

[CONTEXT-GAP: GAP-013] — Server hardware specifications at BIRDC Nyaruzinga are unconfirmed. The deployment design in Section 3 uses recommended minimum specifications pending confirmation from BIRDC IT.

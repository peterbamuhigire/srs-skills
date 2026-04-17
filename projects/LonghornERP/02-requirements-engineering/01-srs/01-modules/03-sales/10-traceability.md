# Traceability Matrix — Sales Module

## 10.1 Purpose

This traceability matrix maps every functional requirement in the Sales module SRS to a business goal. Per IEEE Std 830-1998, every requirement must be traceable to a stakeholder need. Unmapped requirements are anomalies and must be resolved before baseline approval.

Business goals are defined as follows:

| ID | Business Goal |
|---|---|
| BG-001 | Revenue Recognition — IFRS 15-compliant invoicing and financial posting |
| BG-002 | Cash Collection — receipts, aging visibility, and overdue follow-up |
| BG-003 | Customer Relationship — price lists, credit management, and statements |
| BG-004 | Regulatory Compliance — Uganda VAT Act and EFRIS e-invoicing |

## 10.2 Functional Requirement to Business Goal Mapping

| FR ID | Description (Summary) | BG-001 | BG-002 | BG-003 | BG-004 |
|---|---|:---:|:---:|:---:|:---:|
| FR-SALES-001 | Create customer record with TIN, VAT, credit terms | | | Y | Y |
| FR-SALES-002 | Assign customer category and default price list | | | Y | |
| FR-SALES-003 | Duplicate TIN detection | | | Y | Y |
| FR-SALES-004 | Duplicate phone detection | | | Y | |
| FR-SALES-005 | Customer balance summary | | Y | Y | |
| FR-SALES-006 | Credit limit enforcement on invoicing | Y | Y | Y | |
| FR-SALES-007 | Customer statement generation | | Y | Y | |
| FR-SALES-008 | Statement content: opening balance, transactions, closing balance | | Y | Y | |
| FR-SALES-009 | Statement PDF performance ≤ 5 s at P95 | | Y | Y | |
| FR-SALES-010 | Customer soft-delete (deactivation) | | | Y | |
| FR-SALES-011 | Block deactivation with outstanding balance | | Y | Y | |
| FR-SALES-012 | Customer reactivation | | | Y | |
| FR-SALES-013 | Customer record audit log | | | Y | Y |
| FR-SALES-014 | Customer search | | | Y | |
| FR-SALES-015 | Display credit terms on invoice creation | Y | Y | Y | |
| FR-SALES-016 | Create multiple price lists per tenant | | | Y | |
| FR-SALES-017 | Price list lines with effective/expiry dates | | | Y | |
| FR-SALES-018 | Activate/deactivate price list lines by date | | | Y | |
| FR-SALES-019 | Quantity-based discount tiers | | | Y | |
| FR-SALES-020 | Price list priority resolution | | | Y | |
| FR-SALES-021 | Auto-populate price on transaction line | Y | | Y | |
| FR-SALES-022 | Price override with audit log | Y | | Y | |
| FR-SALES-023 | Price history retention | | | Y | |
| FR-SALES-024 | Price lookup ≤ 500 ms at P95 | | | Y | |
| FR-SALES-025 | Block deletion of in-use price list | | | Y | |
| FR-SALES-026 | Create quotation with lines, tax, totals | Y | | Y | |
| FR-SALES-027 | Quotation status lifecycle and expiry | | | Y | |
| FR-SALES-028 | Quotation status change history | | | Y | |
| FR-SALES-029 | Lock accepted/rejected/expired quotations | | | Y | |
| FR-SALES-030 | Quotation PDF generation | | | Y | |
| FR-SALES-031 | Convert quotation to Sales Order | Y | | Y | |
| FR-SALES-032 | Link SO back to originating quotation | Y | | Y | |
| FR-SALES-033 | Create Sales Order with fulfilment tracking | Y | | | |
| FR-SALES-034 | Stock reservation on SO confirmation | Y | | | |
| FR-SALES-035 | Configurable SO approval workflow | Y | | | |
| FR-SALES-036 | Track qty ordered / delivered / invoiced per SO line | Y | Y | | |
| FR-SALES-037 | SO line fulfilment status | Y | | | |
| FR-SALES-038 | Back-order creation on partial delivery | Y | | | |
| FR-SALES-039 | SO cancellation and stock release | Y | | | |
| FR-SALES-040 | Block over-invoicing without override | Y | Y | | |
| FR-SALES-041 | Support 3 invoice types | Y | | | Y |
| FR-SALES-042 | Standard Invoice ledger posting | Y | Y | | Y |
| FR-SALES-043 | Pro-Forma Invoice non-posting rule | Y | | | Y |
| FR-SALES-044 | Create invoice from 3 source types | Y | | | |
| FR-SALES-045 | Invoice line calculation formula | Y | | | |
| FR-SALES-046 | VAT auto-application per tax code | Y | | | Y |
| FR-SALES-047 | Tenant-configurable invoice numbering | Y | | | Y |
| FR-SALES-048 | Credit limit check on invoice save | Y | Y | Y | |
| FR-SALES-049 | Invoice approval workflow | Y | | | |
| FR-SALES-050 | Approver notification | Y | | | |
| FR-SALES-051 | EFRIS submission flag for Uganda tenants | Y | | | Y |
| FR-SALES-052 | Display EFRIS status and QR code | Y | | | Y |
| FR-SALES-053 | Invoice PDF generation ≤ 3 s at P95 | Y | | | Y |
| FR-SALES-054 | Embed EFRIS QR code in PDF | Y | | | Y |
| FR-SALES-055 | Configure recurring invoice template | Y | Y | | |
| FR-SALES-056 | Auto-generate recurring invoice on schedule | Y | Y | | |
| FR-SALES-057 | Auto-send recurring invoice by email | Y | Y | | |
| FR-SALES-058 | Daily recurring invoice admin alert | Y | Y | | |
| FR-SALES-059 | Create Delivery Note from SO or invoice | Y | | | |
| FR-SALES-060 | Capture dispatch qty, warehouse, bin per DN line | Y | | | |
| FR-SALES-061 | Post DN: reduce inventory, create stock movement | Y | | | |
| FR-SALES-062 | Block posting if insufficient stock | Y | | | |
| FR-SALES-063 | Auto-create back-order on partial delivery | Y | | | |
| FR-SALES-064 | Delivery Note PDF generation | Y | | Y | |
| FR-SALES-065 | Proof of delivery capture (signature or upload) | Y | | Y | |
| FR-SALES-066 | Display POD status on DN and SO | Y | | Y | |
| FR-SALES-067 | System-generated DN numbering | Y | | | |
| FR-SALES-068 | Link DN to SO; update SO fulfilment in real time | Y | | | |
| FR-SALES-069 | Cancel DN and reverse stock movement | Y | | | |
| FR-SALES-070 | Block DN cancellation if invoiced | Y | Y | | |
| FR-SALES-071 | Create Sales Return referencing source document | Y | | Y | |
| FR-SALES-072 | Capture return qty, reason, and destination warehouse | Y | | | |
| FR-SALES-073 | Sales Return approval workflow | Y | | | |
| FR-SALES-074 | Auto-generate Credit Note on return approval | Y | Y | | Y |
| FR-SALES-075 | Post return stock receipt to Inventory | Y | | | |
| FR-SALES-076 | System-generated Credit Note numbering | Y | | | Y |
| FR-SALES-077 | Allocate Credit Note to open invoices | Y | Y | | |
| FR-SALES-078 | Hold unapplied Credit Note as customer credit | Y | Y | | |
| FR-SALES-079 | Credit Note PDF generation | Y | | Y | Y |
| FR-SALES-080 | Post Credit Note to AR ledger | Y | Y | | |
| FR-SALES-081 | Create payment receipt with method and reference | Y | Y | | |
| FR-SALES-082 | System-generated receipt numbering | Y | Y | | |
| FR-SALES-083 | Allocate receipt to open invoices | Y | Y | | |
| FR-SALES-084 | Reduce invoice balance and post to AR ledger | Y | Y | | |
| FR-SALES-085 | Hold unallocated receipt as customer credit | Y | Y | | |
| FR-SALES-086 | Retrospective receipt allocation | Y | Y | | |
| FR-SALES-087 | Restrict receipt reversal of fully allocated receipts | Y | Y | | |
| FR-SALES-088 | Debtors aging report with 5 buckets | | Y | | |
| FR-SALES-089 | Aging report filter by customer, category, sales rep | | Y | Y | |
| FR-SALES-090 | Aging report ≤ 8 s at P95 | | Y | | |
| FR-SALES-091 | Aging report: credit limit vs. balance column | | Y | Y | |
| FR-SALES-092 | Export aging report to PDF and Excel | | Y | | |
| FR-SALES-093 | Flag invoice as Overdue | | Y | | |
| FR-SALES-094 | Send overdue email reminder to customer | | Y | Y | |
| FR-SALES-095 | Configure overdue alert schedule | | Y | | |
| FR-SALES-096 | Record overdue alert history per invoice | | Y | | Y |

## 10.3 Coverage Summary

| Business Goal | FR Count | Coverage |
|---|---|---|
| BG-001 Revenue Recognition | 50 | Full |
| BG-002 Cash Collection | 42 | Full |
| BG-003 Customer Relationship | 38 | Full |
| BG-004 Regulatory Compliance | 18 | Full |

All 96 functional requirements map to at least 1 business goal. No orphaned requirements detected at baseline.

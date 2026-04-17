# Customer Management Requirements

## 2.1 Overview

The Customer Management sub-module maintains the master record for every customer entity transacting within a tenant's account. It supports individual, company, and government customer types, enforces credit policy, and provides a full transaction history per customer.

## 2.2 Functional Requirements

**FR-SALES-001:** The system shall create a customer record capturing name, customer type (individual, company, or government), primary contact details (phone, email, physical address), Taxpayer Identification Number (TIN), VAT registration number, assigned currency, assigned price list, credit limit, and credit terms (net 30, net 60, or net 90) when a user with the `sales.customer.create` permission submits a validated customer creation form.

**FR-SALES-002:** The system shall assign every new customer to exactly one customer category — walk-in, wholesale, retail, or export — when the customer record is saved, and shall apply the default price list associated with that category if no price list is explicitly selected.

**FR-SALES-003:** The system shall warn the user with the message "A customer with this TIN already exists: [Customer Name]" when the TIN entered on the customer creation or edit form matches an existing active or inactive customer record within the same tenant.

**FR-SALES-004:** The system shall warn the user with the message "This phone number is already registered to: [Customer Name]" when the primary phone number entered on the customer creation or edit form matches an existing active or inactive customer record within the same tenant.

**FR-SALES-005:** The system shall display a customer balance summary — total outstanding invoices, total unapplied credit notes, total unallocated receipts, and net balance — when a user opens the customer record detail view.

**FR-SALES-006:** The system shall prevent the creation of a new invoice for a customer whose outstanding balance exceeds the customer's configured credit limit when the user attempts to save a draft invoice, and shall display the message "Credit limit exceeded. Outstanding balance: [amount]. Credit limit: [amount]." unless the user holds the `sales.credit.override` permission.

**FR-SALES-007:** The system shall generate a customer statement listing all transactions — invoices, credit notes, receipts, and adjustments — within a user-specified date range, sorted by transaction date ascending, when a user with the `sales.customer.view` permission requests a statement for a selected customer.

**FR-SALES-008:** The system shall include on the customer statement the opening balance at the start of the selected date range, a line for each transaction with date, reference number, debit amount, credit amount, and running balance, and a closing balance at the end of the range.

**FR-SALES-009:** The system shall generate the customer statement as a downloadable PDF within 5 seconds at P95 for a date range spanning 24 months of transactions.

**FR-SALES-010:** The system shall deactivate a customer record (soft-delete) when a user with the `sales.customer.delete` permission confirms the deactivation action, setting the record status to "Inactive" and preventing the customer from appearing in new transaction lookups while preserving all historical transactions, balances, and reports.

**FR-SALES-011:** The system shall prevent deactivation of a customer record that has an outstanding balance greater than zero and shall display the message "Customer has an outstanding balance of [amount]. Settle all balances before deactivating." when deactivation is attempted.

**FR-SALES-012:** The system shall allow a user with the `sales.customer.edit` permission to reactivate an inactive customer record, restoring the customer to active status and making the record available in transaction lookups.

**FR-SALES-013:** The system shall record a full audit log entry — capturing the previous value, new value, changed field, user, and timestamp — whenever any field on a customer record is modified.

**FR-SALES-014:** The system shall allow a user to search the customer list by name, TIN, phone number, or email address using a partial-match search, returning results within 1 second at P95 for a tenant with up to 50,000 customer records.

**FR-SALES-015:** The system shall display the customer's assigned credit terms and credit limit on the invoice creation form when the customer is selected, allowing the user to assess credit exposure before saving the document.

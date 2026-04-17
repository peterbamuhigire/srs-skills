# Price Lists Requirements

## 3.1 Overview

The Price Lists sub-module enables each tenant to maintain multiple, independently versioned price schedules. Price lists are assigned to customers or customer categories and are applied automatically at transaction time. All price changes are recorded for historical auditability.

## 3.2 Functional Requirements

**FR-SALES-016:** The system shall allow a tenant administrator with the `sales.pricelist.manage` permission to create multiple named price lists — each with a unique code, description, and base currency — within the tenant's account, with no enforced upper limit on the number of price lists per tenant.

**FR-SALES-017:** The system shall allow each price list to contain one or more lines, where each line specifies an item, a Unit of Measure (UOM), a unit price, a currency, an effective date, and an optional expiry date, when a user with the `sales.pricelist.manage` permission saves the price list.

**FR-SALES-018:** The system shall activate a price list line on its effective date and deactivate it on its expiry date (if set), and shall use only active lines when resolving the price for a transaction.

**FR-SALES-019:** The system shall support quantity-based discount tiers per price list line, where each tier specifies a minimum quantity threshold and a discount percentage, when a user with the `sales.pricelist.manage` permission defines the tiers; the system shall apply the highest applicable discount tier based on the line quantity entered on a transaction.

**FR-SALES-020:** The system shall assign a price list to an individual customer record or to a customer category, and shall resolve the effective price in the following priority order: (1) customer-level price list, (2) customer-category price list, (3) tenant default price list when a transaction line is created for a customer.

**FR-SALES-021:** The system shall auto-populate the unit price on an invoice, quotation, or sales order line using the resolved price list price when the item and customer are selected, applying any applicable quantity-based discount tier.

**FR-SALES-022:** The system shall allow a user with the `sales.price.override` permission to manually enter a unit price that differs from the price list price on an individual transaction line, and shall record the override — capturing the original price list price, the entered price, the user, and the timestamp — in the transaction audit log.

**FR-SALES-023:** The system shall retain a complete price history for each price list line, recording every price change with the previous price, the new price, the effective date of the change, and the user who made the change, accessible to users with the `sales.pricelist.view` permission.

**FR-SALES-024:** The system shall return the resolved price for a given item, UOM, customer, and quantity within 500 ms at P95 when a line is added to an invoice or order.

**FR-SALES-025:** The system shall prevent deletion of a price list that is currently assigned to one or more active customers or customer categories, and shall display the message "Price list is in use by [N] customer(s). Reassign before deleting." when deletion is attempted.

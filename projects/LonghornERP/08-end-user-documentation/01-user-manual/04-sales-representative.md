# Sales Representative Guide

**Role:** Sales Representative

**Accessible modules:** Sales, Quotations, Invoices, Payments, CRM

---

## Creating a Customer Record

1. In the sidebar, click **Sales**, then click **Customers**.
2. Click **New Customer**.
3. Enter the customer's full name or company name in the **Customer Name** field.
4. Enter the **Phone Number**.
5. Enter the **Email Address**.
6. Enter the **Physical Address** and **City**.
7. Select the **Customer Type**: Individual or Company.
8. If the customer has a TIN (Tax Identification Number), enter it in the **TIN** field.
9. Set the **Credit Limit** if the customer will purchase on credit. Enter `0` for cash-only customers.
10. Select the assigned **Sales Representative** from the dropdown (select yourself if applicable).
11. Click **Save Customer**.

---

## Creating a Quotation

1. In the sidebar, click **Sales**, then click **Quotations**.
2. Click **New Quotation**.
3. Select the **Customer** from the dropdown (type to search).
4. Set the **Quotation Date** and **Valid Until** date using the date pickers.
5. Click **Add Line** in the items table.
6. Select the **Item** or service, enter the **Quantity** and **Unit Price**. The line total calculates automatically.
7. Repeat step 6 for each item in the quotation.
8. In the **Notes** field, enter any terms or delivery conditions.
9. Click **Save Draft** to hold, or click **Send to Customer** to mark it as sent and generate a PDF.
10. To send by email, click **Email Quotation**, confirm the recipient address, and click **Send**.

---

## Converting a Quotation to a Sales Order

1. Open the accepted quotation from **Sales > Quotations**.
2. Confirm all lines and prices are agreed with the customer.
3. Click **Convert to Sales Order**.
4. Review the order details in the confirmation dialog.
5. Click **Confirm**. The sales order is created and the quotation status changes to **Converted**.
6. The new sales order number appears at the top of the screen. Note it for future reference.

---

## Creating a Sales Invoice from an Order

1. Open the sales order from **Sales > Sales Orders**.
2. Verify the order is in **Confirmed** status.
3. Click **Create Invoice**.
4. On the invoice screen, confirm the **Invoice Date** and **Due Date**.
5. If only part of the order is being invoiced, adjust quantities on each line as needed.
6. Click **Post Invoice**, then click **Confirm**.
7. The invoice is posted and the customer's balance updates. A PDF is available via **Print Invoice**.

---

## Recording a Customer Payment and Allocating It to an Invoice

1. In the sidebar, click **Sales**, then click **Customer Receipts**.
2. Click **New Receipt**.
3. Select the **Customer**.
4. Enter the **Amount Received** and the **Payment Date**.
5. Select the **Payment Method** (Cash, Bank Transfer, MoMo).
6. Select the **Bank Account** or **Cash Account** the payment is going into.
7. In the **Allocate to Invoices** table, find the invoice and enter the amount to allocate in the **Allocated** column.
8. The **Unallocated Balance** at the bottom must reach zero before you can post.
9. Click **Post Receipt**, then click **Confirm**.

---

## Creating a Credit Note

Use a credit note to cancel or reduce a posted invoice — for example, for a return or pricing error.

1. Open the original invoice from **Sales > Sales Invoices**.
2. Click **Create Credit Note**.
3. In the dialog, select the **Reason** from the dropdown (Return, Pricing Error, Discount Adjustment).
4. Adjust the quantity or amount on each line if you are issuing a partial credit note.
5. Click **Post Credit Note**, then click **Confirm**.
6. The credit note reduces the customer's outstanding balance. You can allocate it against a future invoice from the **Customer Receipts** screen.

---

## Logging a CRM Activity

Use CRM activities to record calls, meetings, and emails with customers or prospects.

1. In the sidebar, click **CRM**, then click **Activities**.
2. Click **New Activity**.
3. Select the **Activity Type**: Call, Meeting, or Email.
4. Select the **Customer** or **Lead** from the dropdown.
5. Set the **Activity Date** and **Time**.
6. Enter a summary of the conversation or outcome in the **Notes** field.
7. If a follow-up is needed, set the **Follow-Up Date**.
8. Click **Save Activity**.

---

## Creating a New Lead and Converting to Opportunity

### Creating a Lead

1. In the sidebar, click **CRM**, then click **Leads**.
2. Click **New Lead**.
3. Enter the **Contact Name** and **Company Name**.
4. Enter the **Phone** and **Email**.
5. Select the **Lead Source** (for example, Referral, Website, Cold Call).
6. Assign the lead to a sales representative using the **Assigned To** dropdown.
7. Enter any initial notes in the **Description** field.
8. Click **Save Lead**.

### Converting a Lead to an Opportunity

1. Open the lead record from **CRM > Leads**.
2. Click **Convert to Opportunity**.
3. In the conversion dialog, enter the **Estimated Value** and **Expected Close Date**.
4. Select the **Pipeline Stage** (for example, Qualification, Proposal, Negotiation).
5. Click **Confirm**. The lead status changes to **Converted** and a new opportunity record is created.

---

## Viewing the Customer Aging Report

1. In the sidebar, click **Sales**, then click **Reports**, then click **Customer Aging**.
2. Select the **Aging Date** — typically today's date.
3. Select the **Customer** to filter to one customer, or leave it blank to view all customers.
4. Click **Generate Report**.
5. The report groups outstanding invoices into columns: Current, 1–30 days, 31–60 days, 61–90 days, and Over 90 days.
6. Click **Export to Excel** or **Print** to save the report.

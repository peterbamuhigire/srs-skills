# Purchasing Officer Guide

**Role:** Purchasing Officer

**Accessible modules:** Procurement, Requisitions, LPO, Supplier Management

---

## Adding a Supplier Record

1. In the sidebar, click **Procurement**, then click **Suppliers**.
2. Click **New Supplier**.
3. Enter the **Supplier Name**.
4. Enter the **Contact Person** name.
5. Enter the **Phone Number** and **Email Address**.
6. Enter the **Physical Address** and **City**.
7. Enter the **TIN (Tax Identification Number)** if the supplier is VAT-registered.
8. Select the **Payment Terms** from the dropdown (for example, Net 30, Net 60, Cash on Delivery).
9. Select the default **Currency** for this supplier.
10. Enter the supplier's bank details: **Bank Name**, **Branch**, **Account Number**, and **Account Name**.
11. Click **Save Supplier**.

---

## Creating a Purchase Requisition

1. In the sidebar, click **Procurement**, then click **Requisitions**.
2. Click **New Requisition**.
3. Enter a description in the **Purpose / Justification** field.
4. Set the **Required By Date** using the date picker.
5. Click **Add Line** in the items table.
6. Select the **Item** from the dropdown, enter the **Quantity**, and enter the **Estimated Unit Price**.
7. Repeat step 6 for each item needed.
8. Select the **Budget Code** to charge this purchase against.
9. Click **Submit for Approval**. The requisition is routed to the relevant approver automatically.

---

## Creating an RFQ and Recording Supplier Quotes

### Creating an RFQ

1. In the sidebar, click **Procurement**, then click **RFQ** (Request for Quotation).
2. Click **New RFQ**.
3. Link the RFQ to an approved requisition by selecting it from the **Requisition** dropdown, or create a standalone RFQ by leaving this field blank and adding items manually.
4. Set the **RFQ Date** and the **Quote Deadline**.
5. Click **Add Supplier** to add suppliers you want to invite. Repeat for each supplier.
6. Click **Send RFQ**. The system emails the RFQ to all listed suppliers.

### Recording Supplier Quotes

1. Open the RFQ from **Procurement > RFQ**.
2. Click **Record Quote**.
3. Select the **Supplier** who submitted the quote.
4. Enter the **Quote Date** and **Quote Reference Number**.
5. Enter the quoted unit price for each line item in the **Quoted Price** column.
6. Enter the **Lead Time** and **Payment Terms** offered by the supplier.
7. Click **Save Quote**.
8. Repeat for each supplier who responded.

---

## Creating an LPO from the Approved Quote

LPO stands for Local Purchase Order.

1. Open the RFQ that has received all supplier quotes.
2. Review the quote comparison table, which shows prices side by side for all suppliers.
3. Click **Select Supplier** next to the winning quote.
4. Click **Create LPO**.
5. Review the LPO details: supplier, items, quantities, and prices.
6. Adjust quantities or delivery address if needed.
7. Click **Submit LPO for Approval**.
8. Once approved, click **Issue LPO**. The system generates the LPO document and emails it to the supplier.

---

## Receiving a GRN Against the LPO

1. In the sidebar, click **Procurement**, then click **Goods Receipt (GRN)**.
2. Click **New GRN**.
3. In the **Source** field, select **Against LPO**.
4. Select the relevant **LPO** from the dropdown.
5. The system pre-fills the item lines from the LPO.
6. Enter the **Quantity Received** for each line. Adjust if the supplier delivered a partial order.
7. Select the **Warehouse** to receive the goods into.
8. Enter the supplier's **Delivery Note Number** in the **Reference** field.
9. Click **Post GRN**, then click **Confirm**.

---

## Matching the Supplier Invoice Against LPO and GRN (Three-Way Match)

Three-way matching verifies that the supplier invoice matches both the LPO (what was ordered) and the GRN (what was received) before payment is approved.

1. In the sidebar, click **Procurement**, then click **Supplier Invoices**.
2. Click **New Supplier Invoice**.
3. Select the **Supplier**.
4. Enter the **Supplier Invoice Number** and **Invoice Date**.
5. In the **Match Against** section, select the **LPO** and the **GRN** that correspond to this invoice.
6. The system loads the expected lines from the LPO and GRN.
7. Enter the actual quantities and amounts from the supplier invoice.
8. The system highlights any line where the invoice amount differs from the LPO or GRN by more than the permitted tolerance (set by the system administrator).
9. If all lines match within tolerance, click **Approve Invoice**.
10. If there are discrepancies, click **Flag Discrepancy**, enter a note, and route the invoice back for supplier clarification.

---

## Recording a Supplier Payment with WHT Deduction

WHT stands for Withholding Tax.

1. In the sidebar, click **Procurement**, then click **Supplier Payments**.
2. Click **New Payment**.
3. Select the **Supplier**.
4. Select the **Supplier Invoice** to pay from the list of approved invoices.
5. Enter the **Payment Date**.
6. Select the **Bank Account** from which the payment will be made.
7. In the **WHT** section, confirm the **WHT Rate** (for example, 6% for goods, 15% for services). The system pre-populates this based on the supplier's tax profile.
8. The **Net Payment Amount** (invoice amount minus WHT) calculates automatically.
9. Confirm the net amount is correct.
10. Click **Post Payment**, then click **Confirm**.
11. The system posts the payment, records the WHT liability to the relevant tax payable account, and marks the invoice as paid.
12. Click **Download WHT Certificate** to generate the certificate for the supplier.

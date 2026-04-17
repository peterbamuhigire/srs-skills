# Section 6: Dr. Amara — Quality Control Manager

Dr. Amara uses the Quality Control module in the main ERP. She designs inspection templates, records lab results, issues Certificates of Analysis (CoA), and manages non-conformance reports.

---

## 6.1 Creating an Inspection

1. Log in and click **Quality Control** in the main menu.
2. Click **Inspections**, then click **New Inspection**.
3. Select the **Inspection Type**: Incoming Material, In-Process, or Finished Product.
4. Select the **Batch** or **Production Order** to be inspected from the list.
5. Select the **Inspection Template** that applies (for example, "Banana Flour — Export Grade" or "Juice — Domestic").
6. Assign the inspection to a lab technician using the **Assigned To** field.
7. Click **Create Inspection**. The inspection is created with a status of **Pending**.

---

## 6.2 Recording Inspection Results

1. Click **Quality Control** then **Inspections**.
2. Click on the inspection with **Pending** or **In Progress** status.
3. For each parameter in the template:
   a. Enter the measured value in the **Result** field.
   b. The system shows whether the result is within the acceptable range (green = pass, red = fail).
   c. For pass/fail parameters, select **Pass** or **Fail**.
   d. For photo parameters, tap the camera icon and upload the image.
4. After entering all results, click **Submit Results**.
5. If all parameters pass, the batch status changes to **Approved**. Finished goods can now be transferred to saleable inventory.
6. If any parameter fails, the batch status changes to **Rejected** or **On Hold** depending on severity. See Section 6.4.

---

## 6.3 Issuing a Certificate of Analysis

**Domestic Certificate of Analysis:**

1. After the inspection status is set to **Approved**, click on the batch record.
2. Click **Issue Certificate of Analysis**.
3. Select **Domestic** as the certificate type.
4. Review the certificate preview — it shows the batch number, test parameters, results, and the approving analyst's name.
5. Click **Issue & Sign**. The certificate is locked and assigned a certificate number.
6. Click **Download PDF** or **Print** to produce the physical certificate.

**Export Certificate of Analysis:**

1. Follow steps 1–2 above.
2. Select **Export** as the certificate type.
3. Select the **Destination Market**: South Korea, Saudi Arabia, Qatar, Italy, or United States.
4. The system loads the template for that market, which may include additional parameters required by that country's import authority.
5. Confirm that all required parameters for the destination market are present and show passing results.
6. Click **Issue & Sign**. The certificate is locked.
7. Click **Download PDF** or **Print**.

*A batch approved only for domestic use cannot be dispatched on an export order. The export CoA must be issued before the dispatch is processed.*

---

## 6.4 Logging a Non-Conformance

When a quality failure is detected:

1. Click **Quality Control** then **Non-Conformance Reports (NCR)**.
2. Click **New NCR**.
3. Select the **Batch** or **Production Order** affected.
4. Select the **Failure Type** from the list (for example, moisture content out of range, foreign matter detected, incorrect weight).
5. Enter a description in the **Problem Statement** field.
6. Enter the **Immediate Containment Action** taken (for example, batch placed on hold, removed from production line).
7. Assign the NCR to the responsible department using the **Assigned To** field.
8. Click **Save NCR**. The NCR is assigned a reference number and status **Open**.
9. When the root cause has been identified, open the NCR, fill in the **Root Cause** field, and enter the **Corrective Action**.
10. Click **Close NCR**. The NCR status changes to **Closed**.

---

## 6.5 Releasing a Batch to Saleable Inventory

After the inspection is approved and the Certificate of Analysis is issued:

1. The Production Supervisor or Store Manager goes to the production order in the **Manufacturing** module.
2. The **Transfer to Saleable Inventory** button is now active (it was locked until QC approval).
3. They click **Transfer to Saleable Inventory**.
4. Stock moves from Work in Progress to the finished goods warehouse.

*You do not need to take any action to release stock. Approving the inspection and issuing the CoA automatically unlocks the transfer button for the production team.*

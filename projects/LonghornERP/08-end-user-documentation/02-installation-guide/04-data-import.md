# Step 4: Import Your Existing Data

If your business is migrating from another system, you can import master data records into Longhorn ERP using CSV templates. Import master data before processing any transactions.

All import templates are available from **Settings > Import/Export**. Each template includes a header row with column names and a sample data row. Delete the sample row before uploading your file.

---

## Importing Customers

1. Navigate to **Settings > Import/Export > Customers**.
2. Click **Download Template** to save the customer CSV template.
3. Open the file in a spreadsheet application and fill in the following columns:

   | Column | Description |
   |---|---|
   | Name | Full legal name of the customer |
   | TIN | Tax Identification Number (leave blank if not applicable) |
   | Contact Person | Primary contact name |
   | Phone | Primary phone number |
   | Email | Billing email address |
   | Credit Limit | Maximum credit allowed (enter 0 for cash customers) |
   | Payment Terms | e.g., Net 30, Net 15, Cash on Delivery |

4. Save the completed file as CSV.
5. Click **Upload File**, select your CSV, and click **Open**.
6. Longhorn ERP validates each row and displays any errors by row number.
7. Correct the errors in your CSV, re-upload, and repeat until the validation screen shows 0 errors.
8. Click **Confirm Import** to load the records.

---

## Importing Suppliers

The supplier import follows the same process as customers. Additional columns available for suppliers:

| Column | Description |
|---|---|
| WHT Status | Whether withholding tax applies: Yes or No |
| Bank Account | Supplier's bank account number for payment processing |
| Bank Name | Name of the supplier's bank |
| Branch Code | Bank branch code (if required by your bank) |

Navigate to **Settings > Import/Export > Suppliers**, download the template, and follow steps 3–8 above.

---

## Importing Items (Products and Services)

1. Navigate to **Settings > Import/Export > Items**.
2. Click **Download Template** and fill in the following columns:

   | Column | Description |
   |---|---|
   | Item Code | Your internal product or SKU code |
   | Name | Full item name as it appears on invoices |
   | Category | Item category (must exist in Inventory > Categories) |
   | UOM | Unit of measure: Each, Kg, Litre, Box, etc. |
   | Purchase Price | Default buying price (excluding tax) |
   | Sales Price | Default selling price (excluding tax) |
   | Reorder Level | Stock quantity that triggers a reorder alert |

3. Follow steps 4–8 from the customer import process above.

---

## Importing Employees (HR Module)

*This section applies only to tenants with the HR module active.*

1. Navigate to **Settings > Import/Export > Employees**.
2. Click **Download Template** and fill in the following columns:

   | Column | Description |
   |---|---|
   | Employee Number | Your internal staff ID |
   | Full Name | Employee's legal name |
   | Department | Must match a department in HR > Departments |
   | Position | Job title |
   | Date of Hire | Format: YYYY-MM-DD |
   | Basic Salary | Monthly gross salary in your primary currency |
   | Bank Account | Account number for salary payment |
   | Bank Name | Name of the employee's bank |
   | TIN | Employee's personal TIN (required for PAYE) |
   | NSSF Number | National Social Security Fund membership number |

3. Follow steps 4–8 from the customer import process above.

---

## Migrating from Odoo or ERPNext

`[CONTEXT-GAP: GAP-013 — migration scripts from Odoo and ERPNext are pending development. The information below describes the planned assisted migration process; contact support before attempting a migration from either platform.]`

Direct migration from Odoo or ERPNext requires an assisted migration engagement with the Chwezi Core support team. The team will:

1. Extract your data from the source system using platform-specific export tools.
2. Transform the data into Longhorn ERP's import format.
3. Run a trial import in your Sandbox environment for you to validate.
4. Execute the production import after your sign-off.

To request an assisted migration, email support@chwezi.com with the subject line: **Migration Request — [Your Company Name]**. Include the name of your current system and an estimate of the number of records to be migrated.

# Section 3: First-Time Business Configuration

These steps are performed once by the IT Administrator and Finance Director when the system is first set up. They do not need to be repeated unless the business configuration changes.

*Complete the steps in the order listed below. Some steps depend on earlier ones being done first.*

---

## 3.1 Create the Business Profile

1. Log in as IT Administrator.
2. Click **System Administration** then **Business Profile**.
3. Fill in the following fields:
   - **Organisation Name:** BIRDC / PIBID (as required on documents)
   - **Physical Address:** Nyaruzinga Hill, Bushenyi District, Uganda
   - **Tax Identification Number (TIN):** as issued by URA
   - **EFRIS Taxpayer PIN:** provided by URA for EFRIS registration
   - **Logo:** upload the BIRDC logo (PNG, minimum 300×300 pixels)
   - **Default Currency:** UGX
   - **Financial Year Start Month:** July (PIBID) — select July
4. Click **Save Business Profile**.

---

## 3.2 Configure the Chart of Accounts

The chart of accounts is pre-loaded with 1,307 accounts configured for BIRDC. Review before going live:

1. Click **Finance** then **Chart of Accounts**.
2. Review the top-level account groups: Assets, Liabilities, Equity, Revenue, Expenses.
3. To add a new account, click **New Account** and fill in the account code, name, and parent group.
4. To deactivate an account that BIRDC does not use, click on it and toggle **Status** to Inactive.
5. Assign each account an **Accounting Mode**: PIBID Parliamentary, BIRDC Commercial, or Both.
6. Click **Save** after each change.

*Do not delete accounts. Deactivate them instead. Deleted accounts cause gaps in the audit trail.*

---

## 3.3 Set Up Payroll Elements

1. Click **Payroll** then **Payroll Elements**.
2. Review the default earnings and deductions. The following are pre-configured:
   - Basic Salary, Housing Allowance, Transport Allowance
   - PAYE (formula-based, auto-computed)
   - NSSF Employee (5%) and NSSF Employer (10%)
   - LST (Bushenyi rate — confirm the current rate with Bushenyi local government)
3. To add a new element (for example, a new allowance), click **New Element**:
   a. Enter the element **Name**.
   b. Select **Type**: Earning or Deduction.
   c. Set the **Calculation Method**: fixed amount, percentage of basic, or formula.
   d. Set the **GL Account** the element should post to.
   e. Click **Save**.
4. To update PAYE tax bands when URA publishes new rates:
   a. Click **PAYE Tax Bands**.
   b. Click **Edit Bands**.
   c. Update the income brackets and tax rates to match the URA published schedule.
   d. Click **Save**. The new bands apply from the next payroll run.

---

## 3.4 Configure PPDA Procurement Thresholds

1. Click **Procurement** then **PPDA Settings**.
2. Confirm the current PPDA procurement thresholds (UGX):
   - **Micro procurement ceiling** (default: UGX 2,000,000)
   - **Small procurement ceiling** (default: UGX 50,000,000)
   - **Large procurement ceiling** (default: above UGX 50,000,000)
3. Update any threshold that has changed due to PPDA regulation updates.
4. Assign approval roles to each tier:
   - Micro: Department Head
   - Small: Finance Manager
   - Large: Director
5. Click **Save Thresholds**.

---

## 3.5 Add First Users and Assign Roles

1. Click **System Administration** then **Users**.
2. Click **New User**.
3. Fill in:
   - **Full Name**
   - **Username** (for login)
   - **Email Address** (for password reset and notifications)
   - **Phone Number** (for SMS alerts)
   - **Role** — select from the pre-configured roles (see table below)
4. Click **Create User**. The system sends a welcome email with a temporary password.
5. Repeat for every staff member who needs system access.

**Default roles and their access level:**

| Role | Key Access Areas |
|---|---|
| IT Administrator | Full system access |
| Finance Director | Finance, Payroll, Reports, Approval |
| Finance Manager | Finance, Payroll, Procurement AP |
| Procurement Manager | Procurement, Cooperative Procurement |
| Store Manager | Warehouse, Inventory |
| QC Manager | Quality Control, Inspections, CoA |
| Production Supervisor | Manufacturing, Factory Floor |
| Sales Agent | Sales Agent App only |
| Collections Officer | Farmer Delivery App only |
| Cashier | POS only |

*Do not give users more access than their role requires. Follow the principle of least privilege.*

---

## 3.6 Configure Territories and Agents

1. Click **Sales** then **Territory Management**.
2. Click **New Territory** and define the geographic boundaries (by district or subcounty).
3. Assign a **Territory Manager** to each territory.
4. Click **Agent Management** then **New Agent** to register each of BIRDC's sales agents:
   a. Fill in the agent's name, phone number, and assigned territory.
   b. Set the **Stock Float Limit** (UGX) — the maximum value of stock the agent may hold.
   c. Set the **Commission Rate** (%).
   d. Link the agent to their ERP user account.
   e. Click **Save**.
5. Repeat for all 1,071 agents.

*Agent registration can also be done in bulk by importing a spreadsheet. Ask the IT Administrator for the import template.*

# System Administrator Guide

**Role:** System Administrator

**Accessible modules:** User Management, Role Configuration, Module Activation, Branch Setup

---

## Creating a New User and Assigning a Role

1. In the sidebar, click **Admin**, then click **Users**.
2. Click **New User**.
3. Enter the user's **First Name** and **Last Name**.
4. Enter their **Email Address**. This becomes their login username.
5. Enter their **Phone Number**.
6. Select the **Branch** the user belongs to from the dropdown.
7. In the **Role** dropdown, select the role that matches their job function (for example, Finance Manager, Sales Representative).
8. Click **Save User**. The system sends a welcome email to the user with a temporary password and the login URL.

---

## Creating a Custom Role with Specific Permissions

1. In the sidebar, click **Admin**, then click **Roles**.
2. Click **New Role**.
3. Enter a name for the role in the **Role Name** field (for example, "Junior Accountant").
4. Enter a description in the **Description** field explaining what this role is for.
5. The **Permissions Matrix** below lists every module and action (View, Create, Edit, Delete, Approve, Post).
6. For each module, tick the actions this role should be permitted to perform.
7. Leave an action unticked to deny it. Users in this role will not see the corresponding buttons.
8. Click **Save Role**.
9. Assign the role to users by editing their user record and selecting this role.

---

## Activating an Add-On Module

Longhorn ERP modules are activated per subscription. Contact Chwezi Core Systems to ensure your plan includes the module before activating.

1. In the sidebar, click **Admin**, then click **Module Management**.
2. The list shows all available modules with a status indicator: **Active** or **Inactive**.
3. Find the module you want to activate (for example, HR & Payroll).
4. Click **Activate** next to the module name.
5. A confirmation dialog explains any configuration required after activation.
6. Click **Confirm Activate**.
7. The module status changes to **Active**. It immediately appears in the sidebar for users whose role includes that module.

---

## Adding a New Branch or Warehouse

1. In the sidebar, click **Admin**, then click **Branches & Warehouses**.
2. Click **New Branch**.
3. Enter the **Branch Name** and **Branch Code** (a short identifier, for example, `KLA-01`).
4. Enter the **Physical Address** and **City**.
5. Select the **Country** and **Currency** for this branch.
6. Click **Save Branch**.

To add a warehouse linked to this branch:

1. Click the branch name to open its detail.
2. Click the **Warehouses** tab.
3. Click **Add Warehouse**.
4. Enter the **Warehouse Name** and **Warehouse Code**.
5. Click **Save Warehouse**.

---

## Configuring the Chart of Accounts Starter Template

This is a one-time setup step performed when setting up a new company or branch.

1. In the sidebar, click **Finance**, then click **Chart of Accounts**.
2. Click **Import Starter Template**.
3. Select the **Country** from the dropdown to load the localised template for that country's standard account structure.
4. Click **Preview Template**. Review the account groups and account codes that will be created.
5. If the template is correct, click **Import**. The system creates all accounts from the template.
6. To add custom accounts, click **New Account**, fill in the account details, and click **Save**.

---

## Setting Up a Localisation Profile

1. In the sidebar, click **Admin**, then click **Localisation**.
2. Select the **Country** from the dropdown.
3. Select the **Default Currency**.
4. Set the **Date Format** (for example, `DD/MM/YYYY`).
5. Set the **Fiscal Year Start Month** (for example, July for a July–June fiscal year).
6. In the **Tax** section, enter the standard **VAT Rate** percentage (for example, `18` for 18% Uganda VAT).
7. In the **Payroll Tax** section, confirm the PAYE bands and NSSF rates, which are pre-loaded from the selected country template. Edit individual bands if your rates differ.
8. Click **Save Localisation Settings**.

---

## Viewing the Audit Log

The audit log records every user action in the system: logins, record creations, edits, deletions, approvals, and postings.

1. In the sidebar, click **Admin**, then click **Audit Log**.
2. Use the filters at the top to narrow the results:
   - **User** — filter by a specific user.
   - **Module** — filter by module (for example, Finance, HR).
   - **Action** — filter by action type (Create, Edit, Delete, Post, Approve, Login).
   - **From Date** and **To Date** — set the date range.
3. Click **Filter**.
4. The log table shows each event with the timestamp, user, module, action, and a description of the record changed.
5. Click any row to see the full detail of the change, including before and after values where applicable.
6. Click **Export to Excel** to download the filtered log for review or compliance purposes.

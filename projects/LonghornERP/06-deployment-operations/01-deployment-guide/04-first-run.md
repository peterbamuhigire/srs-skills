# First-Run Configuration for Longhorn ERP

Complete this checklist immediately after a successful installation. All steps must be completed in order before granting access to any tenant.

## First-Run Checklist

1. Navigate to the Super Admin panel at `https://yourdomain.com/superadmin` and log in with the default credentials provided in the installation release notes.

2. Change the default super admin password immediately. Navigate to **Profile > Change Password**. Use a minimum 16-character password with mixed case, numbers, and symbols. Store the credential in a password manager — it cannot be recovered if lost.

3. Create the first tenant organisation:

   - Navigate to **Tenants > New Tenant**.
   - Enter the company name, subdomain or tenant code, country, and base currency.
   - Save the record. The system assigns a unique tenant identifier automatically.

4. Assign a subscription plan to the tenant:

   - Open the tenant record and select **Subscription > Assign Plan**.
   - Choose the appropriate plan tier (Starter, Standard, Production, or Enterprise).
   - Set the billing cycle and activation date.

5. Activate the required modules for the tenant:

   - Navigate to **Tenants > [Tenant Name] > Modules**.
   - Toggle on each module the tenant has licensed (e.g., General Ledger, Accounts Payable, Payroll, Inventory, EFRIS Integration).
   - Save. Disabled modules are hidden from the tenant workspace.

6. Log in to the tenant workspace using the tenant admin credentials generated at step 3. Run the setup wizard:

   - Select a Chart of Accounts (COA) template appropriate to the tenant's industry.
   - Enter opening balances for all balance sheet accounts.
   - Configure branches or cost centres if applicable.
   - Create user accounts and assign roles.
   - Save and exit the wizard.

7. Test email delivery to confirm SMTP settings are working:

   - Navigate to **Settings > Email Configuration > Send Test Email**.
   - Enter a known working email address and trigger the test.
   - Confirm the test message arrives within 2 minutes. If it does not arrive, review `MAIL_*` variables in `.env` and check the mail server logs.

8. Verify the automated backup job is scheduled and active. See Section 5 for the backup cron configuration. Confirm the cron entry exists:

   ```bash
   cat /etc/cron.d/longhorn-backup
   ```

   A missing or empty file means backups are not running. Configure the backup cron before considering the deployment complete.

## Post-Checklist Verification

After completing all 8 steps, perform the following smoke test to confirm end-to-end system integrity:

- Create a test sales invoice in the tenant workspace and post it.
- Verify a corresponding journal entry appears in the General Ledger.
- Confirm the dashboard reflects the updated Accounts Receivable balance.
- Delete or void the test transaction to leave the tenant in a clean state.

The system is ready for production use once the smoke test passes without errors.

# Tenant Management Procedures for Longhorn ERP

All tenant management actions are performed through the Super Admin panel unless a procedure explicitly requires direct database or CLI access. Log every action — operator name, timestamp, and outcome — in the tenant management log.

---

## Tenant Suspension

Use this procedure when a tenant's subscription has lapsed, a payment is overdue, or a security concern requires immediate lockout.

1. Log in to the Super Admin panel at `/superadmin`.
2. Navigate to Tenants > [Tenant Name] > Actions > Suspend.
3. Confirm the suspension in the modal dialog. The tenant status changes to SUSPENDED immediately; all tenant users see the message "Account suspended. Please contact support@chwezi.com."
4. Verify the status change in the database:

   ```sql
   SELECT id, name, status, updated_at FROM tenants WHERE id = <tenant_id>;
   ```

   Confirm `status = 'SUSPENDED'` and `updated_at` reflects the current timestamp.

5. Send the tenant's primary contact a suspension notice by email, stating the reason and the steps required to reactivate.

---

## Tenant Reactivation

Use this procedure after a suspended tenant resolves the condition that triggered suspension.

1. Confirm the outstanding balance is cleared: Super Admin panel > Billing > Subscriptions > [Tenant Name]. The subscription status must be ACTIVE or RENEWED with a zero balance.
2. Navigate to Super Admin panel > Tenants > [Tenant Name] > Actions > Reactivate.
3. Confirm the reactivation in the modal dialog.
4. Verify the status change in the database:

   ```sql
   SELECT id, name, status, updated_at FROM tenants WHERE id = <tenant_id>;
   ```

   Confirm `status = 'ACTIVE'`.

5. Ask the tenant's primary contact to confirm they can log in and that all modules are accessible before closing the ticket.

---

## Tenant Data Export (Offboarding)

Use this procedure when a tenant requests a full data export prior to leaving the platform. This procedure is also the first phase of permanent tenant deletion.

1. Enable maintenance mode for the tenant to prevent data changes during export: Super Admin panel > Tenants > [Tenant Name] > Settings > Maintenance Mode > Enable.

2. Run the data export script from the server:

   ```bash
   php /var/www/longhorn/scripts/export-tenant.php \
     --tenant-id=<tenant_id> \
     --output=/tmp/tenant-<tenant_id>-export.zip
   ```

   The script exports all rows with `tenant_id = <tenant_id>` across every module table and packages them as a password-protected ZIP archive.

3. Verify the archive was created and is non-zero in size:

   ```bash
   ls -lh /tmp/tenant-<tenant_id>-export.zip
   ```

4. Deliver the export archive to the tenant via secure file transfer (SFTP or a signed, time-limited download link). Do not send the archive as an email attachment.

5. Obtain written confirmation from the tenant that the export was received and is complete before proceeding.

6. Archive the tenant's data in the platform (data is retained but the tenant is deactivated):

   ```bash
   php /var/www/longhorn/scripts/archive-tenant.php --tenant-id=<tenant_id>
   ```

7. After the 90-day retention period, permanent deletion of tenant data requires written authorisation from Chwezi Core Systems management. Do not delete data before written authorisation is on file.

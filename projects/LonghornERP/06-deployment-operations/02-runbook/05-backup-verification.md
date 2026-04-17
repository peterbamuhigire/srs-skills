# Backup Verification Procedure for Longhorn ERP

Perform this procedure once per month. The goal is to confirm that the most recent backup produces a fully functional, data-complete restoration. A backup that has never been tested is not a verified backup.

---

## Monthly Restore Test

1. Identify the most recent backup file in the backup directory:

   ```bash
   ls -lt /backup/longhorn-*.sql | head -5
   ```

2. Create a clean test database on a test MySQL instance (never restore to the production database):

   ```bash
   mysql -u root -p -e "CREATE DATABASE test_restore;"
   ```

3. Restore the backup file into the test database:

   ```bash
   mysql -u root -p test_restore < /backup/longhorn-YYYY-MM-DD.sql
   ```

   Replace `YYYY-MM-DD` with the actual backup date. The restore must complete without errors.

4. Start a test Apache instance pointing to the restored database. Update a copy of `.env` with `DB_DATABASE=test_restore` and serve on a non-production port (e.g., port 8888).

5. Log in to the Super Admin panel on the test instance and verify:
   - The tenant list is intact and matches the production record count.
   - At least 3 tenants can be opened and their module dashboards load without errors.

6. Log in to a representative test tenant and verify:
   - Invoice data is present and the most recent invoice matches the production record.
   - Payroll records for the most recent pay run are present and complete.
   - Subscription and billing records are intact.

7. Document the result in the backup verification log: date tested, backup file name, tester name, and result (PASS or FAIL with notes). Store the log in `/var/log/longhorn-backup-verify.log`.

8. Destroy the test database and test instance after verification:

   ```bash
   mysql -u root -p -e "DROP DATABASE test_restore;"
   ```

---

## Backup Failure Response

Follow this procedure immediately when the daily operations check (Section 1, Step 1) identifies a missing or failed backup.

1. Identify the failure cause from the backup log:

   ```bash
   tail -50 /var/log/longhorn-backup.log
   ```

   Common causes: disk full on the backup destination, MySQL not running at backup time, network unreachable for remote backup target.

2. Fix the underlying issue before running a manual backup:
   - Disk full: follow the full disk playbook (Section 2, Incident 6).
   - MySQL down: follow the database connection failure playbook (Section 2, Incident 1).
   - Network unreachable: confirm VPN or remote storage connectivity.

3. Run the backup manually after the root cause is resolved:

   ```bash
   bash /var/www/longhorn/scripts/backup.sh
   ```

4. Verify the backup completed successfully:

   ```bash
   tail -10 /var/log/longhorn-backup.log
   ```

   Confirm a SUCCESS line is present with the current timestamp.

5. If 24 hours or more have elapsed since the last successful backup, escalate immediately to a Chwezi Core Systems senior engineer. A gap of more than 24 hours without a verified backup is a P2 incident; a gap of more than 48 hours is P1.

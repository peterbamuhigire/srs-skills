# Daily Operations Checklist for Longhorn ERP

Complete every item on this checklist at the start of each business day. Log the result (PASS / FAIL / ACTION TAKEN) in the daily operations log.

1. Verify yesterday's backup completed successfully: open `/var/log/longhorn-backup.log` and confirm a SUCCESS line dated yesterday. If absent, follow the backup failure response procedure in Section 5.

2. Check Apache error log for new CRITICAL or ERROR entries since the last check:

   ```bash
   tail -100 /var/www/longhorn/logs/apache-error.log | grep -E 'CRITICAL|ERROR'
   ```

   Investigate any new entries before proceeding.

3. Check the application log for unhandled exceptions and fatal errors:

   ```bash
   grep 'EXCEPTION\|FATAL' /var/www/longhorn/logs/app.log | tail -50
   ```

   Any EXCEPTION or FATAL line that is new since the previous check requires immediate investigation.

4. Verify MySQL is running:

   ```bash
   systemctl status mysql
   ```

   Expected state: `active (running)`. If not active, follow the database connection failure playbook in Section 2.

5. Verify Apache is running:

   ```bash
   systemctl status apache2
   ```

   Expected state: `active (running)`. If not active, execute `systemctl start apache2` and investigate the cause.

6. Check disk usage on all mounts:

   ```bash
   df -h
   ```

   Alert if any mount exceeds 80% utilisation. A mount at or above 90% is a P1 incident; follow the full disk playbook in Section 2.

7. Review MySQL slow query log for queries exceeding 5 seconds:

   ```bash
   grep -A 4 'Query_time: [5-9]\|Query_time: [0-9][0-9]' /var/log/mysql/mysql-slow.log | tail -40
   ```

   Escalate any recurring slow query to a developer for index review.

8. Verify that the active subscription count in the billing records matches the count of tenants with status `ACTIVE` in the database:

   ```sql
   SELECT COUNT(*) FROM tenants WHERE status = 'ACTIVE';
   ```

   A mismatch requires reconciliation with the billing administrator before end of business.

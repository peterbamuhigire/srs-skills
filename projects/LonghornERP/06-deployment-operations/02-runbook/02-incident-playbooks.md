# Incident Playbooks for Longhorn ERP

Each playbook follows a standard format: symptoms, diagnosis steps, resolution steps, and escalation criteria. Execute diagnosis steps in order before attempting resolution.

---

## Incident 1 — Database Connection Failure

**Symptoms:** All users see a "Database error" page. The application log contains repeated `PDOException: SQLSTATE[HY000] [2002]` or `Connection refused` entries.

**Diagnosis steps:**

1. Verify MySQL is running: `systemctl status mysql`
2. Check for out-of-memory kills in the system journal: `journalctl -xe | grep -i 'mysql\|oom'`
3. Check MySQL error log for InnoDB crash or corruption: `tail -100 /var/log/mysql/error.log`
4. Confirm the `DB_HOST`, `DB_PORT`, `DB_USER`, and `DB_PASSWORD` values in `/var/www/longhorn/.env` are correct.
5. Attempt a manual connection to confirm credentials: `mysql -u longhorn_user -p -h 127.0.0.1 longhorn_db`

**Resolution steps:**

1. If MySQL is stopped, start it: `systemctl start mysql`
2. If MySQL fails to start due to InnoDB corruption, set `innodb_force_recovery = 1` in `/etc/mysql/mysql.conf.d/mysqld.cnf`, restart MySQL, export all data, then restore to a clean instance. Remove `innodb_force_recovery` after successful restore.
3. If credentials are wrong, update `/var/www/longhorn/.env` and restart PHP-FPM: `systemctl restart php8.3-fpm`
4. Clear the application maintenance flag if it was set during diagnosis: `rm -f /var/www/longhorn/storage/maintenance.flag`
5. Confirm all users can reach the login page before closing the incident.

**Escalation:** If MySQL does not start after Step 1 and Step 2, or if data corruption is confirmed, escalate immediately to the senior engineer (P1). Do not attempt `innodb_force_recovery` values above 3 without senior engineer authorisation.

---

## Incident 2 — Session / Authentication Failure

**Symptoms:** Users cannot log in. Users who were logged in are unexpectedly signed out. Session data appears lost on page reload.

**Diagnosis steps:**

1. Check the application log for session driver errors: `grep -i 'session\|redis\|memcache' /var/www/longhorn/logs/app.log | tail -30`
2. Confirm the session driver configured in `/var/www/longhorn/.env` (`SESSION_DRIVER`) matches the running service (e.g., `file`, `database`, `redis`).
3. If `SESSION_DRIVER=file`, check that `/var/www/longhorn/storage/framework/sessions/` exists and is writable by the web server user: `ls -la /var/www/longhorn/storage/framework/sessions/`
4. If `SESSION_DRIVER=database`, verify the `sessions` table exists: `SHOW TABLES LIKE 'sessions';`
5. Check available disk space — session writes fail silently when the disk is full: `df -h`

**Resolution steps:**

1. If the sessions directory is missing: `mkdir -p /var/www/longhorn/storage/framework/sessions && chown -R www-data:www-data /var/www/longhorn/storage/`
2. If permissions are wrong: `chown -R www-data:www-data /var/www/longhorn/storage/ && chmod -R 775 /var/www/longhorn/storage/`
3. If the sessions table is missing, run the migration: `php /var/www/longhorn/artisan migrate --path=database/migrations/create_sessions_table.php`
4. If disk is full, follow the full disk playbook (Incident 6) first.
5. Restart PHP-FPM after any storage fix: `systemctl restart php8.3-fpm`
6. Ask a test user to log in and confirm sessions persist across page loads.

**Escalation:** If users remain unable to log in after all resolution steps, escalate to team lead (P2) within 1 hour.

---

## Incident 3 — Payment Gateway Timeout (MTN MoMo / Airtel Money)

**Symptoms:** MoMo or Airtel Money payments remain in PENDING status for more than 15 minutes. No callback is received. Tenant users report payment not confirmed.

**Diagnosis steps:**

1. Check the application log for payment callback errors: `grep -i 'momo\|airtel\|callback\|payment' /var/www/longhorn/logs/app.log | tail -50`
2. Confirm the callback URL is publicly reachable from the internet (not behind a firewall or returning a non-200 status): `curl -I https://<your-domain>/api/payments/callback`
3. Check MTN MoMo and Airtel Money API credentials in `/var/www/longhorn/.env` — confirm keys have not expired.
4. Check the payment gateway's status page for any reported outages (MTN MoMo: developer.mtn.com/status; Airtel Money: check Africa's Talking dashboard if routing via Africa's Talking).
5. Query stuck payments in the database:

   ```sql
   SELECT id, tenant_id, amount, provider, status, created_at
   FROM payments
   WHERE status = 'PENDING' AND created_at < NOW() - INTERVAL 15 MINUTE
   ORDER BY created_at DESC;
   ```

**Resolution steps:**

1. If the callback URL is unreachable, fix the routing or firewall rule and update the gateway developer portal with the correct callback URL.
2. If API credentials have expired, rotate them in the provider portal and update `/var/www/longhorn/.env`, then restart PHP-FPM.
3. If the gateway is experiencing a confirmed outage, place a maintenance notice for the affected payment method and wait for the provider to resolve. Do not retry bulk payments during an outage — duplicate charge risk.
4. For payments stuck in PENDING after the gateway confirms completion, trigger a manual status reconciliation: `php /var/www/longhorn/artisan payments:reconcile --provider=momo --from=<YYYY-MM-DD>`
5. Notify affected tenants of any confirmed failed payments.

**Escalation:** If reconciliation fails or tenants report double charges, escalate to senior engineer immediately (P1 — financial data integrity risk).

---

## Incident 4 — EFRIS Submission Failure

**Symptoms:** Invoices cannot be submitted to URA EFRIS. The EFRIS integration returns errors or times out. Tenant users see "EFRIS submission failed" on invoice confirmation.

**Diagnosis steps:**

1. Check the application log for EFRIS-specific errors: `grep -i 'efris\|ura\|fiscal' /var/www/longhorn/logs/app.log | tail -50`
2. Note the error code returned — common URA error codes:
   - `ERR-001` — invalid TIN
   - `ERR-010` — duplicate invoice reference
   - `ERR-050` — EFRIS API unreachable (network or URA outage)
3. Confirm network connectivity to the URA EFRIS endpoint: `curl -I https://efris.ura.go.ug/`
4. Verify EFRIS API credentials and device token in `/var/www/longhorn/.env` (`EFRIS_DEVICE_TOKEN`, `EFRIS_USERNAME`, `EFRIS_PASSWORD`).
5. Check if URA has announced scheduled maintenance (URA website or official channels).

**Resolution steps:**

1. For `ERR-001` (invalid TIN): verify the tenant's TIN in Super Admin > Tenants > [Tenant Name] > Tax Settings. Correct and resubmit.
2. For `ERR-010` (duplicate reference): the invoice was already submitted. Mark the invoice as SUBMITTED in the database and inform the tenant — do not resubmit.
3. For `ERR-050` or network timeout: confirm URA maintenance status. If no outage is announced, check the server's outbound firewall rules. If URA is down, queue invoices for resubmission: `php /var/www/longhorn/artisan efris:retry-queue`
4. If credentials are expired, renew the EFRIS device token in the URA EFRIS portal and update `/var/www/longhorn/.env`.
5. After resolving the root cause, process the retry queue: `php /var/www/longhorn/artisan efris:retry-queue --force`

**Escalation:** If invoices cannot be submitted for more than 4 hours during business hours, escalate to the team lead (P2). Unsubmitted invoices past the URA deadline represent a compliance risk — notify the tenant's finance contact immediately.

---

## Incident 5 — High Memory Usage / PHP-FPM Worker Exhaustion

**Symptoms:** Pages are slow or timing out. `top` shows PHP-FPM processes consuming close to 100% CPU or memory. Apache returns 503 errors. New requests queue and time out.

**Diagnosis steps:**

1. Confirm PHP-FPM worker exhaustion: `systemctl status php8.3-fpm` — look for "reached pm.max_children setting"
2. Check how many PHP-FPM processes are running: `ps aux | grep php-fpm | wc -l`
3. Identify the request type consuming the most memory: `ps aux --sort=-%mem | grep php | head -20`
4. Check for runaway background jobs or scheduled tasks: `php /var/www/longhorn/artisan queue:monitor`
5. Check available server memory: `free -h`
6. Check the application log for memory limit errors: `grep -i 'memory\|allowed memory' /var/www/longhorn/logs/app.log | tail -20`

**Resolution steps:**

1. If `pm.max_children` is reached and server memory permits, increase it in `/etc/php/8.3/fpm/pool.d/www.conf` and reload: `systemctl reload php8.3-fpm`. Calculate the safe maximum: divide available RAM by the average PHP-FPM process size.
2. If a runaway job is consuming memory, identify and kill it: `kill -9 <PID>`. Investigate the job code for memory leaks.
3. If `memory_limit` in `php.ini` is too low for normal operation, increase it in `/etc/php/8.3/fpm/php.ini` and reload PHP-FPM.
4. Enable the maintenance flag to stop new requests while the server recovers: `touch /var/www/longhorn/storage/maintenance.flag`
5. After recovery, remove the maintenance flag: `rm /var/www/longhorn/storage/maintenance.flag`
6. If the server is consistently near its memory ceiling, initiate a capacity review with the infrastructure team.

**Escalation:** If memory exhaustion recurs daily, escalate to team lead as a P2 capacity issue. If the server becomes completely unresponsive, escalate to senior engineer (P1).

---

## Incident 6 — Full Disk

**Symptoms:** Application writes failing. Log rotation failing. Database writes returning errors. Users may see PHP fatal errors or blank pages.

**Diagnosis steps:**

1. Identify which filesystem is full: `df -h`
2. Identify the largest consumers on the full filesystem: `du -sh /var/www/longhorn/* | sort -rh | head -20`
3. Check log file sizes: `ls -lh /var/www/longhorn/logs/` and `ls -lh /var/log/mysql/`
4. Check for leftover export archives: `ls -lh /tmp/*.zip /var/www/longhorn/storage/exports/`
5. Check for large MySQL binary logs: `ls -lh /var/lib/mysql/*.bin 2>/dev/null | tail -20`

**Resolution steps:**

1. Remove rotated and compressed log files older than 30 days: `find /var/www/longhorn/logs/ -name '*.gz' -mtime +30 -delete`
2. Remove application log files older than 14 days if log rotation has not run: `find /var/www/longhorn/logs/ -name '*.log.*' -mtime +14 -delete`
3. Remove completed and delivered tenant export archives from `/tmp/` and `/var/www/longhorn/storage/exports/`.
4. If MySQL binary logs are the cause, purge old logs (retain at least 7 days): `PURGE BINARY LOGS BEFORE DATE_SUB(NOW(), INTERVAL 7 DAY);`
5. After freeing space, confirm disk usage is below 70%: `df -h`
6. Restart any services that failed due to the disk event: `systemctl restart apache2 php8.3-fpm mysql`
7. Remove the maintenance flag if it was set: `rm -f /var/www/longhorn/storage/maintenance.flag`

**Escalation:** If disk cannot be freed below 80% without deleting data that must be retained, escalate to senior engineer for storage expansion (P1 if application is still failing writes).

---

## Incident 7 — Slow MySQL Queries Causing Page Timeouts

**Symptoms:** Specific pages take more than 10 seconds to load. Users report timeouts on reports, invoice lists, or payroll runs. MySQL process list shows long-running queries.

**Diagnosis steps:**

1. Identify currently running slow queries:

   ```sql
   SELECT id, user, host, db, command, time, state, info
   FROM information_schema.processlist
   WHERE time > 5
   ORDER BY time DESC;
   ```

2. Check the slow query log for recurring offenders: `tail -100 /var/log/mysql/mysql-slow.log`
3. Run `EXPLAIN` on the identified slow query to check the execution plan:

   ```sql
   EXPLAIN SELECT ...;
   ```

   Look for `type = ALL` (full table scan) and `rows` values in the millions.

4. Check whether the slow query involves a `tenant_id` filter — all multi-tenant queries must filter by `tenant_id` first.
5. Check InnoDB buffer pool hit rate:

   ```sql
   SHOW STATUS LIKE 'Innodb_buffer_pool_read%';
   ```

   Hit rate = `Innodb_buffer_pool_read_requests` / (`Innodb_buffer_pool_read_requests` + `Innodb_buffer_pool_reads`). A rate below 99% indicates insufficient buffer pool size.

**Resolution steps:**

1. Kill a runaway query only if it has been running for more than 60 seconds and is blocking other queries: `KILL QUERY <id>;`
2. If the execution plan shows `type = ALL` on a large table, add a covering index. Example for invoice lookups by tenant:

   ```sql
   ALTER TABLE invoices ADD INDEX idx_tenant_status (tenant_id, status, created_at);
   ```

3. If the buffer pool hit rate is below 99%, increase `innodb_buffer_pool_size` in `/etc/mysql/mysql.conf.d/mysqld.cnf` to 70–80% of available RAM, then restart MySQL.
4. For payroll or report queries performing large aggregations across all tenants, verify the query includes a `tenant_id = ?` predicate. Queries missing the `tenant_id` filter are also a data isolation defect — report to the development team immediately.
5. After adding indexes, confirm the execution plan uses the new index: re-run `EXPLAIN` and verify `type = ref` or `type = range`.

**Escalation:** If a query cannot be optimised without a schema change that requires a migration, escalate to the development team lead (P3). If the slow query is causing a full-table lock that blocks all writes, escalate to senior engineer (P2).

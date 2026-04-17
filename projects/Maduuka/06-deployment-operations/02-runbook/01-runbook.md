---
title: "Operations Runbook -- Maduuka"
version: "1.0"
date: "2026-04-05"
status: "Draft"
author: "Peter Bamuhigire, Chwezi Core Systems"
---

# Operations Runbook -- Maduuka Production System

## 1. Overview

### 1.1 Purpose

This runbook defines repeatable procedures for diagnosing and resolving incidents in the Maduuka production environment, and for executing routine maintenance tasks. Each procedure follows the pattern: *Trigger → Diagnosis → Resolution → Verification.*

### 1.2 Intended Audience

On-call engineer or system administrator with SSH access to the production server and read access to application logs.

### 1.3 Log Locations

| Log | Path |
|---|---|
| Nginx access | `/var/log/nginx/access.log` |
| Nginx error | `/var/log/nginx/error.log` |
| PHP-FPM | `/var/log/php8.3-fpm.log` |
| Application | `/var/www/maduuka/storage/logs/laravel.log` |
| Queue worker | `/var/log/maduuka/worker.log` |
| MySQL error | `/var/log/mysql/error.log` |

---

## 2. Incident Procedures

---

### INC-001: Web App Returns 502 Bad Gateway

**Trigger:** Users report a blank page or HTTP 502 error when accessing the web app.

**Diagnosis:**

1. Check Nginx status: `sudo systemctl status nginx`
2. Check PHP-FPM status: `sudo systemctl status php8.3-fpm`
3. Check the Nginx error log for upstream connection failures: `sudo tail -50 /var/log/nginx/error.log`
4. Check available disk space -- a full disk prevents PHP-FPM from writing temporary files: `df -h`

**Resolution:**

1. If PHP-FPM is stopped or crashed: `sudo systemctl restart php8.3-fpm`
2. If the 502 persists after restarting PHP-FPM, restart Nginx: `sudo systemctl restart nginx`
3. If disk is at 100%: identify and remove large log files or temporary files to free space, then restart PHP-FPM.

**Verification:** Load the web app login page in a browser. Confirm HTTP 200 OK is returned (inspect via browser DevTools → Network tab or `curl -I https://<domain>/login`).

---

### INC-002: Database Connection Refused

**Trigger:** Application logs contain `SQLSTATE[HY000] [2002] Connection refused`.

**Diagnosis:**

1. Check MySQL service status: `sudo systemctl status mysql`
2. Check disk space -- MySQL stops automatically when the disk is full: `df -h`
3. Check the MySQL error log for connection pool exhaustion or crash: `sudo tail -100 /var/log/mysql/error.log`
4. Check current connection count vs. `max_connections`: `mysql -u root -p -e "SHOW STATUS LIKE 'Threads_connected'; SHOW VARIABLES LIKE 'max_connections';"`

**Resolution:**

1. If MySQL is stopped: `sudo systemctl start mysql`
2. If the disk is full: free space (see INC-001 Resolution step 3), then restart MySQL.
3. If connection pool is exhausted: increase `max_connections` in `/etc/mysql/mysql.conf.d/mysqld.cnf` and reload: `sudo systemctl reload mysql`. Investigate which process is holding connections open.

**Verification:** Confirm the application can authenticate and query by loading the login page and completing a successful login. Check `SHOW STATUS LIKE 'Threads_connected';` to confirm connection count is within bounds.

---

### INC-003: Offline Sync Backlog Growing

**Trigger:** Users report the POS app showing a large number of "pending sync" transactions that are not clearing.

**Diagnosis:**

1. Check queue worker status: `sudo supervisorctl status maduuka-worker`
2. Check the queue worker log for repeated errors: `sudo tail -100 /var/log/maduuka/worker.log`
3. Check the application log for sync endpoint failures: `grep -i "sync\|queue\|failed" /var/www/maduuka/storage/logs/laravel.log | tail -50`
4. Verify connectivity to Africa's Talking and MTN MoMo APIs from the server: `curl -I https://api.africastalking.com` and `curl -I https://sandbox.momodeveloper.mtn.com`

**Resolution:**

1. If the queue worker is stopped: `sudo supervisorctl restart maduuka-worker`
2. If a sync endpoint is returning errors, identify the root cause from the application log and fix the underlying issue (misconfigured API credentials, schema mismatch, etc.).
3. Re-queue failed jobs after the endpoint is restored: `php artisan queue:retry all`

**Verification:** Monitor the pending sync count in the Maduuka admin panel. Confirm the count decreases over the next 5 minutes. Confirm the affected transactions appear in sales reports.

---

### INC-004: Africa's Talking SMS Not Delivering

**Trigger:** Customers are not receiving SMS receipts or OTP messages.

**Diagnosis:**

1. Log in to the Africa's Talking dashboard and check the account balance and the delivery report for the affected messages.
2. Check the application log for API error responses: `grep -i "africastalking\|sms" /var/www/maduuka/storage/logs/laravel.log | tail -50`
3. Verify the sender ID status in the Africa's Talking dashboard -- sender IDs can be suspended by the carrier without notice.
4. Check whether the API key in `.env` matches the one shown in the Africa's Talking dashboard.

**Resolution:**

1. If the account balance is zero or low: top up the Africa's Talking account immediately.
2. If the sender ID is suspended or unregistered: contact Africa's Talking support (`support@africastalking.com`) to reinstate it.
3. If the API key has changed or rotated: update `AT_API_KEY` in `.env` and restart the queue worker: `sudo supervisorctl restart maduuka-worker`.
4. If rate limiting is occurring: space out bulk SMS sends or request a rate limit increase from Africa's Talking.

**Verification:** Send a test SMS from the application to a known phone number. Confirm the delivery receipt appears in the Africa's Talking dashboard within 60 seconds.

---

### INC-005: MTN MoMo Payment Timeout

**Trigger:** Cashiers report MoMo payments are stuck in "pending" status and do not complete.

**Diagnosis:**

1. Check the MTN MoMo API status page for known outages.
2. Check the application log for callback URL errors: `grep -i "momo\|callback" /var/www/maduuka/storage/logs/laravel.log | tail -50`
3. Verify the MoMo callback URL is publicly reachable from the internet: `curl -I https://<domain>/api/momo/callback`
4. Confirm the MoMo Business API credentials (`MOMO_API_KEY`, `MOMO_API_SECRET`, `MOMO_SUBSCRIPTION_KEY`) in `.env` are not expired.

**Resolution:**

1. If MTN MoMo API is experiencing a known outage: inform cashiers to accept cash or record MoMo payments manually for reconciliation after the outage clears.
2. If the callback URL is unreachable (firewall rule, Nginx misconfiguration): fix the routing and reopen the endpoint.
3. If credentials are expired: generate new credentials from the MTN MoMo Developer Portal and update `.env`. *[GAP-001: MTN Uganda Business API support contact not yet obtained -- use the developer portal self-service until a support contact is established.]*
4. Retry pending transactions via the admin panel or: `php artisan queue:retry all`

**Verification:** Complete a test MoMo payment end-to-end using a test phone number. Confirm the payment transitions from "pending" to "completed" and the transaction appears in the sales report.

---

### INC-006: Scheduled Report Not Delivered

**Trigger:** A business owner reports not receiving the daily email summary report.

**Diagnosis:**

1. Confirm cron is running and the schedule entry is present: `crontab -l -u www-data`
2. Verify the queue worker is processing jobs: `sudo supervisorctl status maduuka-worker`
3. Check the application log for email dispatch errors: `grep -i "mail\|smtp\|report" /var/www/maduuka/storage/logs/laravel.log | tail -50`
4. Ask the recipient to check their spam or junk folder.

**Resolution:**

1. If the cron entry is missing: re-add it (refer to Deployment Guide Section 4, step 13).
2. If the queue worker is stopped: `sudo supervisorctl restart maduuka-worker`
3. If SMTP credentials have changed or expired: update `MAIL_USERNAME`, `MAIL_PASSWORD`, and `MAIL_HOST` in `.env` and restart the worker.
4. Dispatch the missing report manually: `php artisan reports:send-daily --business=<id>`

**Verification:** Trigger a manual report dispatch and confirm the email is received. Check the queue worker log to confirm the job completed without error.

---

## 3. Routine Maintenance Procedures

---

### MAINT-001: Database Backup Verification (Weekly)

*Purpose: confirm that automated backups are valid and restorable before they are needed.*

1. Download the most recent database backup file from the `maduuka-prod-files` Wasabi bucket.
2. Restore the backup to the staging environment:

   ```bash
   mysql -u maduuka_staging -p maduuka_staging < backup_YYYY-MM-DD.sql
   ```

3. Verify row counts in key tables match production (compare `SELECT COUNT(*) FROM sales;` across both environments).
4. Delete the staging restore after verification is complete.
5. Record the verification result and date in the maintenance log.

---

### MAINT-002: SSL Certificate Renewal

*Let's Encrypt certificates auto-renew 30 days before expiry via Certbot. This procedure confirms auto-renewal is functioning.*

1. Run a dry-run renewal to confirm no configuration errors:

   ```bash
   sudo certbot renew --dry-run
   ```

   The command must complete with "Congratulations, all simulated renewals succeeded." Any error requires immediate investigation.

2. Set a calendar reminder 14 days before the current certificate expiry date as a fallback monitoring point. Check the expiry date with: `sudo certbot certificates`.

---

### MAINT-003: PHP Dependency Security Audit (Monthly)

1. Run the Composer security audit from the application root:

   ```bash
   composer audit
   ```

2. Review all reported vulnerabilities. Treat any vulnerability rated *high* or *critical* as an urgent fix -- do not defer.
3. Update non-breaking (minor and patch) dependencies:

   ```bash
   composer update --minor-only
   ```

4. Run the full test suite after updating: `php artisan test`. Do not deploy if tests fail.

---

### MAINT-004: Database Query Performance Review (Monthly)

1. Enable the MySQL slow query log for a 24-hour observation window. In `/etc/mysql/mysql.conf.d/mysqld.cnf`:

   ```ini
   slow_query_log = 1
   slow_query_log_file = /var/log/mysql/slow.log
   long_query_time = 1
   ```

   Reload: `sudo systemctl reload mysql`.

2. After 24 hours, review the slow query log and identify all queries with execution time > 1 second.
3. For each identified query: add a missing index, refactor N+1 patterns in application code, or rewrite the query.
4. Disable the slow query log after the review period to avoid unnecessary disk I/O.

---

## 4. Emergency Contacts

| Role | Contact | Details |
|---|---|---|
| Product Owner | Peter Bamuhigire | +256784464178 |
| MTN Uganda Business API support | [CONTEXT-GAP: support contact not yet obtained -- GAP-001] | Escalate via MTN MoMo Developer Portal until resolved |
| Africa's Talking support | support@africastalking.com | Include Account ID and API key prefix in all tickets |
| Wasabi support | support@wasabisys.com | Include bucket name and region in all tickets |

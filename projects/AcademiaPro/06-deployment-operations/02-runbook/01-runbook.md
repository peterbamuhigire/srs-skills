# Operational Runbook — AcademiaPro

**Version:** 1.0
**Last Updated:** 2026-04-03
**Owner:** Peter Bamuhigire — Chwezi Core Systems
**Classification:** Internal — Operations Team Only

---

## 1. Service Overview

### 1.1 System Components

| Component | Technology | Host | Port |
|-----------|-----------|------|------|
| Web Application | PHP 8.2 / Laravel 11 | EC2 (Docker) | 443 |
| Primary Database | MySQL 8.x InnoDB | RDS / Docker | 3306 |
| Cache / Queue Broker | Redis 7 | ElastiCache / Docker | 6379 |
| Queue Worker | Laravel Horizon | EC2 (Docker) | 9100 (dashboard) |
| Search Engine | Meilisearch | EC2 (Docker) | 7700 |
| Object Storage | AWS S3 | AWS | — |
| CDN | CloudFront + Cloudflare | AWS / Cloudflare | 443 |
| SMS Gateway | Africa's Talking API | External | — |
| WhatsApp Gateway | Meta WhatsApp Business API | External | — |

### 1.2 External Dependencies

- **Cloudflare DNS** — DNS resolution and DDoS protection
- **SchoolPay** — fee payment processing and reconciliation
- **Africa's Talking** — SMS notifications (fee reminders, attendance alerts)
- **Meta WhatsApp Business API** — parent communication channel
- **UNEB / MoES EMIS** — statutory report submission (outbound only)

### 1.3 Service Level Objectives

| SLO | Target | Measurement |
|-----|--------|-------------|
| Monthly uptime | ≥ 99.5% (≥ 99.9% during exam periods) | Uptime Robot HTTP checks, 1-minute interval |
| API response time (CRUD) | P95 ≤ 500 ms | Laravel Telescope + application logs |
| Report card generation | P95 ≤ 3000 ms | Application logs per request |
| Recovery Time Objective | ≤ 4 hours | Time from SEV1 declaration to service restored |
| Recovery Point Objective | ≤ 1 hour | MySQL binary log + S3 backup frequency |
| Fee receipt idempotency | 0 duplicates per 10,000 events | Application audit log + DB unique constraints |

### 1.4 Critical Data Flows

1. **Fee Payment:** Parent pays via SchoolPay -> webhook hits `/api/v1/payments/callback` -> Laravel validates HMAC signature -> MySQL transaction records payment + generates receipt -> Redis publishes SMS job -> Horizon dispatches Africa's Talking SMS
2. **Report Card Generation:** Teacher finalises marks -> system pulls grading rules from `grading_scales` table -> computes UNEB grades -> renders PDF via queue job -> stores in S3 -> notifies parent
3. **Attendance Alert:** Cron job (`schedule:run`) triggers at 10:00 EAT -> checks `attendances` table for absent students -> dispatches SMS batch via Africa's Talking

---

## 2. Incident Severity Levels

| Level | Definition | Response Time | Update Cadence | Examples |
|-------|-----------|---------------|----------------|---------|
| **SEV1** | Service fully down or data integrity at risk | ≤ 15 min | Every 30 min | Database unreachable, payment double-charging, complete outage |
| **SEV2** | Major feature degraded, workaround exists | ≤ 30 min | Every 1 hour | Report card generation failing, SMS gateway down, Horizon crash |
| **SEV3** | Minor feature impaired, low user impact | ≤ 4 hours | Daily | Search indexing delayed, non-critical cron failure, slow dashboard |
| **SEV4** | Cosmetic or informational | Next business day | Weekly | UI rendering issue, log noise, non-blocking deprecation warning |

---

## 3. Incident Response Procedure

### 3.1 Detect

1. Uptime Robot or Healthchecks.io fires alert via SMS/email.
2. On-call engineer acknowledges the alert within the response time for the severity level.
3. Open an incident channel (WhatsApp group or dedicated thread).

### 3.2 Triage

1. Confirm the alert is genuine (not a false positive from a monitoring blip):
   ```bash
   curl -s -o /dev/null -w "%{http_code}" https://academiapro.com/api/health
   ```
2. Classify severity using the table in Section 2.
3. Check recent deployments:
   ```bash
   docker logs --tail 50 academiapro-app
   git -C /var/www/academiapro log --oneline -5
   ```

### 3.3 Mitigate

1. If a deployment caused the issue, roll back:
   ```bash
   cd /var/www/academiapro && git revert HEAD --no-edit && php artisan config:cache
   ```
2. If a single container is unhealthy, restart it:
   ```bash
   docker compose restart app
   ```
3. If the database is overloaded, kill long-running queries:
   ```sql
   SELECT id, time, info FROM information_schema.processlist WHERE time > 30 ORDER BY time DESC;
   KILL <process_id>;
   ```
4. Enable maintenance mode if mitigation requires downtime:
   ```bash
   php artisan down --secret="ops-bypass-token"
   ```

### 3.4 Resolve

1. Apply the permanent fix (code patch, configuration change, infrastructure scaling).
2. Verify the fix:
   ```bash
   curl -s https://academiapro.com/api/health | jq .
   ```
3. Disable maintenance mode:
   ```bash
   php artisan up
   ```
4. Confirm SLO metrics have returned to normal via Uptime Robot dashboard.

### 3.5 Postmortem

1. Write a postmortem document within 48 hours for SEV1 and SEV2 incidents.
2. Include: timeline, root cause, impact (users affected, duration), contributing factors, remediation actions with owners and deadlines.
3. Store postmortems in `projects/AcademiaPro/06-deployment-operations/03-postmortems/`.
4. Review in the next team sync. Blameless tone is mandatory.

---

## 4. Alert Response Playbooks

### 4.1 High CPU (> 80% for 5 min)

**Diagnose:**
```bash
top -bn1 | head -20
docker stats --no-stream
ps aux --sort=-%cpu | head -10
```

**Remediate:**
- If PHP-FPM processes are spiking, check for runaway queries or infinite loops in Laravel logs: `tail -100 /var/www/academiapro/storage/logs/laravel.log`
- If a single request type is responsible, enable rate limiting on that endpoint.
- If sustained under normal traffic, scale horizontally (Phase 8+): increase EC2 Auto Scaling Group desired count.

### 4.2 High Memory (> 85%)

**Diagnose:**
```bash
free -h
docker stats --no-stream
ps aux --sort=-%mem | head -10
```

**Remediate:**
- Restart PHP-FPM if memory is not reclaimed: `docker compose restart app`
- Check for memory leaks in queue workers: `php artisan horizon:terminate` (Horizon will auto-restart workers).
- If Redis is consuming excessive memory: `redis-cli info memory` — check `used_memory_peak_human`. Flush expired keys: `redis-cli --scan --pattern "laravel_cache:*" | head -20`

### 4.3 Disk Usage (> 85%)

**Diagnose:**
```bash
df -h
du -sh /var/www/academiapro/storage/logs/*
du -sh /var/lib/mysql/
du -sh /var/lib/docker/
```

**Remediate:**
- Rotate Laravel logs: `truncate -s 0 /var/www/academiapro/storage/logs/laravel.log`
- Prune Docker resources: `docker system prune -f --volumes`
- Archive old MySQL binary logs: `PURGE BINARY LOGS BEFORE DATE(NOW() - INTERVAL 3 DAY);`
- If S3 is not the issue, check for orphaned uploads in `storage/app/tmp/`.

### 4.4 API Response Time (P95 > 500 ms)

**Diagnose:**
```bash
tail -200 /var/www/academiapro/storage/logs/laravel.log | grep -i "slow\|timeout"
```
Check Laravel Telescope for slow queries at `/telescope/queries`.

**Remediate:**
- Identify and optimise the slow query (add index, rewrite N+1).
- If Redis is slow: `redis-cli --latency -h 127.0.0.1`
- Flush application cache if stale data is causing recomputation: `php artisan cache:clear && php artisan config:cache && php artisan route:cache`
- Enable MySQL slow query log temporarily: set `long_query_time = 1` in MySQL config.

### 4.5 Error Rate (5xx > 1% of requests over 5 min)

**Diagnose:**
```bash
grep -c "500\|502\|503" /var/log/nginx/access.log
tail -100 /var/www/academiapro/storage/logs/laravel.log | grep -i "exception\|error"
```

**Remediate:**
- If a specific exception dominates, apply a targeted fix.
- If OOM is killing PHP-FPM, see Playbook 4.2.
- If MySQL connections are exhausted, see Playbook 4.7.
- If a deployment introduced the regression, roll back per Section 3.3 step 1.

### 4.6 Queue Depth (> 1000 pending jobs for 10 min)

**Diagnose:**
```bash
php artisan horizon:status
redis-cli llen queues:default
redis-cli llen queues:high
redis-cli llen queues:sms
```
Check Horizon dashboard at `/horizon`.

**Remediate:**
- If workers are crashed: `php artisan horizon:terminate && php artisan horizon`
- If a specific job is failing repeatedly, check failed jobs: `php artisan queue:failed`
- Retry failed jobs after root cause is fixed: `php artisan queue:retry all`
- If throughput is insufficient, increase `processes` in `config/horizon.php` and restart Horizon.

### 4.7 MySQL Connections (> 80% of `max_connections`)

**Diagnose:**
```sql
SHOW STATUS LIKE 'Threads_connected';
SHOW VARIABLES LIKE 'max_connections';
SELECT user, host, COUNT(*) AS conn FROM information_schema.processlist GROUP BY user, host ORDER BY conn DESC;
```

**Remediate:**
- Kill idle connections exceeding `wait_timeout`:
  ```sql
  SELECT id FROM information_schema.processlist WHERE command = 'Sleep' AND time > 300;
  ```
- Reduce Laravel's `DB_POOL_SIZE` in `.env` if connection pooling is misconfigured.
- Increase `max_connections` in MySQL config if the server has headroom (check RAM: each connection uses approximately 10 MB).

---

## 5. Escalation Matrix

| Elapsed Time | Escalation Level | Contact | Method |
|-------------|-----------------|---------|--------|
| 0 - 15 min | On-call Engineer | See Contact List (Section 9) | WhatsApp + SMS |
| 15 - 60 min | Team Lead | See Contact List (Section 9) | Phone call |
| 60+ min (SEV1 only) | CTO / Peter Bamuhigire | See Contact List (Section 9) | Phone call + WhatsApp |
| External dependency down | Vendor Support | Africa's Talking / SchoolPay / AWS Support | Vendor support portal + email |

**Escalation rules:**
- SEV1: Escalate to Team Lead immediately if the on-call engineer cannot mitigate within 15 minutes.
- SEV2: Escalate to Team Lead if no progress after 30 minutes.
- SEV3/SEV4: No escalation required unless unresolved after 24 hours.
- Any incident involving data loss or payment integrity: escalate to CTO immediately regardless of severity.

---

## 6. Troubleshooting Recipes

### 6.1 Database Connection Pool Exhaustion

**Symptoms:** `SQLSTATE[HY000] [1040] Too many connections` in Laravel logs.

1. Check current connections: `SHOW STATUS LIKE 'Threads_connected';`
2. Identify culprits: `SELECT user, host, COUNT(*) FROM information_schema.processlist GROUP BY user, host;`
3. Kill sleeping connections older than 5 minutes:
   ```sql
   SELECT CONCAT('KILL ', id, ';') FROM information_schema.processlist WHERE command = 'Sleep' AND time > 300;
   ```
4. Restart PHP-FPM to release stale connections: `docker compose restart app`
5. **Prevent recurrence:** Set `DB_POOL_SIZE` appropriately in `.env`; set MySQL `wait_timeout = 300`.

### 6.2 Out-of-Memory (OOM) Kill

**Symptoms:** Container restarts unexpectedly; `dmesg | grep -i oom` shows kills.

1. Identify which process was killed: `dmesg | grep -i "out of memory" | tail -5`
2. Check container memory limits: `docker inspect academiapro-app | grep -i memory`
3. If PHP-FPM: reduce `pm.max_children` in `php-fpm.conf` or increase container memory limit.
4. If MySQL: check `innodb_buffer_pool_size` — should not exceed 70% of available RAM.
5. If Redis: check `maxmemory` policy — set `maxmemory-policy allkeys-lru`.

### 6.3 Failed Deployment

**Symptoms:** `php artisan migrate` fails or application returns 500 after deploy.

1. Check migration status: `php artisan migrate:status`
2. Review the failing migration file for syntax errors or missing columns.
3. If safe, roll back the last batch: `php artisan migrate:rollback --step=1`
4. Fix the migration, then re-run: `php artisan migrate`
5. If the deployment introduced a code error, revert the commit:
   ```bash
   git revert HEAD --no-edit && php artisan config:cache && php artisan route:cache
   ```

### 6.4 TLS Certificate Expiry

**Symptoms:** Uptime Robot reports SSL error; browsers show certificate warning.

1. Check certificate expiry:
   ```bash
   echo | openssl s_client -servername academiapro.com -connect academiapro.com:443 2>/dev/null | openssl x509 -noout -dates
   ```
2. If using Cloudflare: certificates auto-renew. Check Cloudflare dashboard under SSL/TLS > Edge Certificates.
3. If using Let's Encrypt on the origin: `certbot renew --dry-run` then `certbot renew`.
4. Restart Nginx after renewal: `docker compose restart nginx`
5. **Prevent recurrence:** Healthchecks.io cron job should run `certbot renew` weekly.

### 6.5 Redis Connection Failure

**Symptoms:** `ConnectionRefusedError` or `NOAUTH` in Laravel logs; cache misses spike.

1. Check Redis is running: `redis-cli ping` (expect `PONG`).
2. If Docker: `docker compose logs redis --tail 20`
3. Check Redis memory: `redis-cli info memory`
4. If `NOAUTH`: verify `REDIS_PASSWORD` in `.env` matches `requirepass` in `redis.conf`.
5. Restart Redis: `docker compose restart redis`
6. After restart, clear Laravel config cache: `php artisan config:cache`

### 6.6 Horizon Crash / Workers Not Processing

**Symptoms:** Jobs pile up in Redis; Horizon dashboard shows "Inactive" status.

1. Check Horizon status: `php artisan horizon:status`
2. Check logs: `tail -50 /var/www/academiapro/storage/logs/horizon.log`
3. Terminate gracefully: `php artisan horizon:terminate`
4. Restart: `php artisan horizon` (run via Supervisor in production).
5. Verify Supervisor is managing Horizon: `supervisorctl status horizon`
6. If Supervisor is not running: `supervisorctl reread && supervisorctl update && supervisorctl start horizon`

### 6.7 Meilisearch Sync Lag

**Symptoms:** Search results do not reflect recent data changes; users report stale search.

1. Check Meilisearch health: `curl -s http://127.0.0.1:7700/health`
2. Check pending tasks: `curl -s http://127.0.0.1:7700/tasks?status=enqueued,processing | jq '.total'`
3. If tasks are stuck, check Meilisearch logs: `docker compose logs meilisearch --tail 30`
4. Force a full re-index from Laravel:
   ```bash
   php artisan scout:flush "App\Models\Student"
   php artisan scout:import "App\Models\Student"
   ```
5. Repeat for other searchable models as needed.
6. If Meilisearch is OOM, increase container memory or reduce `--max-indexing-memory`.

---

## 7. Maintenance Procedures

### 7.1 Planned Downtime

1. Announce maintenance window 48 hours in advance via SMS to school admins.
2. Schedule outside school hours: 22:00 - 04:00 EAT on weekdays, or weekends.
3. Enable maintenance mode: `php artisan down --secret="ops-bypass-token"`
4. Perform maintenance tasks.
5. Verify health: `curl -s https://academiapro.com/api/health`
6. Disable maintenance mode: `php artisan up`
7. Confirm via Uptime Robot that monitoring shows green.

### 7.2 TLS Certificate Rotation

1. Automated via Cloudflare (edge) and Certbot cron (origin).
2. Weekly cron entry: `0 3 * * 1 certbot renew --quiet && docker compose restart nginx`
3. Monitor via Healthchecks.io ping after cron execution.
4. Manual check: run the `openssl` command from Recipe 6.4 step 1.

### 7.3 Log Rotation

- Laravel logs: configure `LOG_CHANNEL=daily` in `.env` (auto-rotates, retains 14 days).
- Nginx logs: logrotate config at `/etc/logrotate.d/nginx`, rotate weekly, keep 4 weeks.
- MySQL slow query log: rotate monthly, compress archived files.
- Docker logs: set `max-size: 50m` and `max-file: 3` in `docker-compose.yml` logging config.

### 7.4 Database Maintenance

**Weekly:**
```sql
ANALYZE TABLE students, fees, payments, attendances, marks, report_cards;
```

**Monthly:**
```sql
OPTIMIZE TABLE students, fees, payments, attendances, marks, report_cards;
```

**Backup verification (weekly):**
1. Restore the latest S3 backup to a staging instance.
2. Run a row count comparison against production for critical tables.
3. Log the result in the maintenance register.

**Binary log purge (weekly):**
```sql
PURGE BINARY LOGS BEFORE DATE(NOW() - INTERVAL 7 DAY);
```

### 7.5 Horizon Restart

After any `.env` change or `config/horizon.php` update:
```bash
php artisan horizon:terminate
# Wait for graceful shutdown (workers finish current jobs)
supervisorctl start horizon
```

### 7.6 Cache Clear

After configuration or environment changes:
```bash
php artisan config:cache
php artisan route:cache
php artisan view:cache
php artisan event:cache
```

To fully flush the application cache (use sparingly — causes a temporary performance dip):
```bash
php artisan cache:clear
```

---

## 8. Backup and Recovery

### 8.1 Backup Schedule

| Asset | Method | Frequency | Retention | Storage |
|-------|--------|-----------|-----------|---------|
| MySQL full dump | `mysqldump` via cron | Every 6 hours | 30 days | S3 (versioned bucket) |
| MySQL binary logs | Continuous | Continuous | 7 days | Local + S3 |
| Redis RDB snapshot | Redis `SAVE` via cron | Every 1 hour | 7 days | S3 |
| Uploaded files | S3 native versioning | Continuous | 90 days | S3 |
| Application code | Git | Every deploy | Indefinite | GitHub |

### 8.2 Recovery Procedure

1. Provision a clean EC2 instance or Docker host.
2. Pull the latest application code from Git.
3. Restore MySQL from the most recent S3 dump:
   ```bash
   aws s3 cp s3://academiapro-backups/mysql/latest.sql.gz - | gunzip | mysql -u root -p academiapro
   ```
4. Apply binary logs to reach RPO:
   ```bash
   mysqlbinlog /var/lib/mysql/binlog.000* | mysql -u root -p academiapro
   ```
5. Restore Redis RDB: copy `dump.rdb` to Redis data directory and restart Redis.
6. Verify data integrity: run row counts and checksum on critical tables.
7. Update DNS (Cloudflare) if the instance IP changed.
8. Disable maintenance mode and confirm via Uptime Robot.

---

## 9. Contact List

| Role | Name | Primary Contact | Backup Contact |
|------|------|----------------|----------------|
| CTO / Project Owner | Peter Bamuhigire | [CONTEXT-GAP: phone number] | WhatsApp |
| On-call Engineer | [CONTEXT-GAP: name] | [CONTEXT-GAP: phone number] | WhatsApp |
| Team Lead | [CONTEXT-GAP: name] | [CONTEXT-GAP: phone number] | WhatsApp |
| AWS Support | — | AWS Support Console | — |
| Africa's Talking Support | — | `support@africastalking.com` | Dashboard tickets |
| SchoolPay Support | — | [CONTEXT-GAP: contact] | — |
| Cloudflare Support | — | Cloudflare Dashboard | — |
| Meta WhatsApp Business | — | Meta Business Help Centre | — |


---

## AI Service Operations Runbook

### Monitoring

| Alert | Trigger | Response |
|---|---|---|
| AI batch job overrun | Monday batch not complete by 07:30 EAT | Check Laravel Horizon queue depth. Scale worker count if queue is backed up. Check for provider outage. |
| `pii_scrubbed = 0` in `ai_audit_log` | Any row with `pii_scrubbed = 0` | Immediate investigation. If PII confirmed in prompt: invoke DPPA breach notification procedure. Suspend the affected feature for the affected tenant until root cause resolved. |
| Provider HTTP 5xx error rate > 10% | Over any 5-minute window | Circuit breaker will have activated. Verify failover to secondary provider. If both fail: all AI batch jobs deferred; affected school owners notified via in-app alert. |
| Tenant AI budget 100% exhausted | `ai_budget_alerts` threshold_pct = 100 | Automated: school owner notified; AI calls blocked. Oncall action: if school owner requests emergency budget increase, Super Admin can update `tenant_ai_modules.monthly_budget_ugx` via the admin panel — no code deployment required. |
| Token cost spike (> 2× daily average) | CloudWatch metric on `ai_usage_log` daily sum | Investigate which `feature_slug` is spiking. Check for a batch job retry storm (verify Horizon dead letter queue). Check if a new large school onboarded and ran a bulk AI operation. |

### Provider Outage Playbook

1. Confirm outage: check Anthropic status page and test API endpoint directly.
2. Verify automatic failover to secondary provider (OpenAI) is active — check Horizon logs for successful calls via secondary.
3. If both providers unavailable: set `AI_PROVIDER=mock` in the environment temporarily to return empty/cached results from the previous batch. Notify affected school owners: "AI insights are temporarily unavailable. We are working to restore service."
4. Once primary provider restored: reset `AI_PROVIDER=anthropic`. Run any deferred batch jobs manually via Artisan: `php artisan ai:run-batch --date=YYYY-MM-DD`.
5. Post-incident: document in `docs/CHANGELOG.md` with tenant impact, duration, and deferred jobs.

### Circuit Breaker Reset

If the circuit breaker has opened (3 consecutive provider failures) and the provider is now healthy:
```bash
php artisan ai:reset-circuit-breaker --provider=anthropic
```
This closes the circuit and allows new requests to flow to the primary provider.

### AI Audit Log Query (DPPA Compliance Request)

To retrieve all AI calls for a specific tenant in a date range (for PDPO audit):
```sql
SELECT id, feature_slug, model, prompt_hash, response_hash, pii_scrubbed, outcome, created_at
FROM ai_audit_log
WHERE tenant_id = ?
  AND created_at BETWEEN ? AND ?
ORDER BY created_at ASC;
```
Note: Only hashes are stored. The PDPO can verify that PII scrubbing was applied (`pii_scrubbed = 1`) without seeing prompt content.

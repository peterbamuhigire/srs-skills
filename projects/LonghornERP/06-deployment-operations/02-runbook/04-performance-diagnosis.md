# Performance Degradation Diagnosis for Longhorn ERP

Follow these steps in order when users report slow page loads, timeouts, or degraded responsiveness. Do not skip steps — the scope established in Step 1 determines which later steps are relevant.

---

**Step 1 — Identify scope**

Determine whether the issue affects one tenant, one module, or all users.

- If one tenant: the cause is likely a data volume issue, a missing index on a tenant-specific table, or a runaway background job for that tenant.
- If one module: the cause is likely a slow query specific to that module's data model.
- If all users: the cause is likely a server resource constraint (CPU, memory, disk I/O) or a global MySQL problem.

Log the scope before proceeding; it narrows the remaining steps.

---

**Step 2 — Check server resources**

Run the following commands and note the output:

```bash
# CPU and memory by process
top

# Available memory
free -h

# Disk I/O — run for 5 samples at 1-second intervals
iostat -x 1 5
```

Alert thresholds:

| Resource | Investigate if |
|---|---|
| CPU (user + system) | > 80% sustained for > 2 minutes |
| Available memory | < 500 MB free |
| Disk I/O `%util` | > 90% on any device |

If any threshold is exceeded, address the resource constraint before tuning queries — query optimisation will not resolve a saturated disk or exhausted RAM.

---

**Step 3 — Identify slow queries**

Query the MySQL process list for statements running longer than 5 seconds:

```sql
SELECT id, user, db, command, time, state, LEFT(info, 200) AS query_preview
FROM information_schema.processlist
WHERE time > 5
ORDER BY time DESC;
```

Also review the slow query log:

```bash
tail -200 /var/log/mysql/mysql-slow.log
```

Record the full text of any query appearing more than once — recurring slow queries indicate a missing index, not a transient load spike.

---

**Step 4 — Check Apache worker availability**

```bash
apachectl status
```

Review the worker scoreboard. If all slots show `W` (sending reply) or `_` (waiting) with no idle slots remaining, Apache is at capacity. Increase `MaxRequestWorkers` in `/etc/apache2/mods-enabled/mpm_prefork.conf` (or the active MPM configuration file) and reload:

```bash
systemctl reload apache2
```

Calculate the safe `MaxRequestWorkers` value: divide available RAM (after MySQL and PHP-FPM allocation) by the average Apache child process size (`ps aux | grep apache2 | awk '{sum += $6} END {print sum/NR/1024 " MB"}'`).

---

**Step 5 — Check PHP-FPM pool status**

```bash
systemctl status php8.3-fpm
```

Look for the line `reached pm.max_children setting`. If present, PHP-FPM is queuing or rejecting requests. See the PHP-FPM exhaustion playbook (Incident 5) for resolution steps.

Also confirm the PHP-FPM status page is enabled and review active request counts:

```bash
curl -s http://127.0.0.1/php-fpm-status?full | grep -E 'active|idle|max'
```

---

**Step 6 — Check for missing indexes**

For any slow query identified in Step 3, run `EXPLAIN` to inspect the execution plan:

```sql
EXPLAIN SELECT <query text here>;
```

A row with `type = ALL` indicates a full table scan. Add a targeted index using the columns in the `WHERE`, `JOIN ON`, and `ORDER BY` clauses. For multi-tenant queries, the index must begin with `tenant_id`:

```sql
-- Example: invoices filtered by tenant and date range
ALTER TABLE invoices ADD INDEX idx_tenant_date (tenant_id, invoice_date);
```

Confirm the new index is used by re-running `EXPLAIN` — `type` should change to `ref` or `range` and `rows` should drop significantly.

---

**Step 7 — Check InnoDB buffer pool hit rate**

A buffer pool hit rate below 99% means MySQL is reading data from disk on every query, which is a primary cause of high I/O and slow response times.

```sql
SHOW STATUS LIKE 'Innodb_buffer_pool_read%';
```

Calculate hit rate: `Innodb_buffer_pool_read_requests` ÷ (`Innodb_buffer_pool_read_requests` + `Innodb_buffer_pool_reads`) × 100.

If the hit rate is below 99%, increase `innodb_buffer_pool_size` in `/etc/mysql/mysql.conf.d/mysqld.cnf`. Set it to 70–80% of total server RAM. Restart MySQL after changing this value:

```bash
systemctl restart mysql
```

Monitor the hit rate again after 15 minutes of normal load to confirm improvement.

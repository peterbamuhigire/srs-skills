# Operational Runbook for Medic8 Healthcare Management System

**Version:** 1.0
**Last Updated:** 2026-04-03
**Classification:** Internal — Operations Team Only
**Audience:** On-call engineers, System Owner, DevOps

*This runbook is designed to be followed at 3 AM under pressure. Every procedure is step-by-step. Do not skip steps. Do not improvise unless explicitly instructed to use judgement.*

---

## 1. Routine Operations

### 1.1 Daily Checklist

Perform every business day by 09:00 EAT. Each item must be checked and signed off in the ops log.

| # | Task | Tool | Expected State |
|---|---|---|---|
| 1 | Review Sentry error dashboard — new or recurring exceptions | Sentry | No unresolved Critical errors |
| 2 | Verify last night's RDS automated backup completed | AWS Console → RDS → Automated Backups | Backup status: `available` |
| 3 | Check DHIS2 sync status for all Ugandan facilities | Medic8 Admin → HMIS Sync Dashboard | All facilities show `synced` or `queued` (not `failed`) |
| 4 | Check Laravel Horizon queue health | `/horizon` dashboard (staging) or CloudWatch metrics | No failed jobs older than 15 minutes |
| 5 | Review offline facility sync status | Medic8 Admin → Offline Facilities | No facility with sync queue > 24 hours |
| 6 | Verify WebSocket server is running | CloudWatch alarm for WebSocket health check | No alarm in `ALARM` state |

### 1.2 Weekly Checklist

Perform every Monday by 12:00 EAT.

| # | Task | Tool | Action if Abnormal |
|---|---|---|---|
| 1 | Review slow query log | RDS Performance Insights | Identify queries > 2 seconds; create optimisation ticket |
| 2 | Check disk usage on RDS and ECS | CloudWatch | If RDS free storage < 20%, investigate growth and plan vertical scale |
| 3 | Review security alerts | Sentry, AWS GuardDuty, CloudTrail | Investigate any suspicious access patterns; escalate if needed |
| 4 | Review failed login attempts | Medic8 Admin → Audit Log → Failed Logins | Lock accounts with > 10 failed attempts; contact facility admin |
| 5 | Check S3 storage growth | AWS Console → S3 → Bucket Metrics | Forecast cost; archive old files if needed |
| 6 | Review Horizon failed jobs | Horizon dashboard | Retry or delete; investigate root cause if pattern exists |

### 1.3 Monthly Checklist

Perform on the first business day of each month.

| # | Task | Tool | Notes |
|---|---|---|---|
| 1 | Rotate API keys (MoMo, Airtel, Africa's Talking) | AWS Secrets Manager | Generate new keys, update Secrets Manager, deploy, verify, revoke old keys |
| 2 | Review access audit trail | Medic8 Admin → Audit Trail | Check for unusual access patterns: after-hours PHI access, bulk data exports |
| 3 | Update drug formulary if NDA published changes | Medic8 Admin → Drug Formulary | Run `DrugFormularySeeder` with updated data; notify facilities |
| 4 | Review and prune CloudWatch log groups | AWS Console → CloudWatch → Log Groups | Delete log groups older than retention period |
| 5 | Test backup restoration | Restore RDS snapshot to a test instance | Verify data integrity; terminate test instance after verification |
| 6 | Review SSL certificate expiry dates | ACM Console | ACM auto-renews, but verify no certificates are in `PENDING_VALIDATION` |
| 7 | Review ECS task definition versions | AWS Console → ECS → Task Definitions | Clean up old revisions (keep last 10) |

---

## 2. Incident Response Procedures

### 2.0 General Incident Protocol

For any incident:

1. **Acknowledge** the alert within the required response time (15 minutes for Critical, 1 hour for Warning).
2. **Open an incident channel** in Slack: `#medic8-incident-YYYYMMDD`.
3. **Start a timeline** in the incident channel. Log every action with a timestamp.
4. **Follow the specific procedure** below for the incident type.
5. **Resolve and close** the incident channel with a summary.
6. **Post-incident review** within 48 hours for Critical incidents.

---

### 2.1 Application Down

**Severity:** Critical
**Response Time:** Acknowledge within 15 minutes

**Symptoms:** External monitoring reports `app.medic8.com` is unreachable. Sentry stops receiving events. Users report errors.

**Procedure:**

1. Check ALB health checks:
   ```bash
   aws elbv2 describe-target-health \
     --target-group-arn <target-group-arn>
   ```
   - If all targets are `unhealthy`, proceed to Step 2.
   - If some targets are `healthy`, the issue may be intermittent — check CloudWatch for 5xx error rate.

2. Check ECS task status:
   ```bash
   aws ecs describe-services --cluster medic8-prod --services medic8-app
   aws ecs list-tasks --cluster medic8-prod --service-name medic8-app
   aws ecs describe-tasks --cluster medic8-prod --tasks <task-arn>
   ```
   - If `desiredCount` > `runningCount`, ECS tasks are failing to start. Check `stoppedReason`.
   - If tasks are in `PENDING` state, check ECS capacity (CPU/memory reservations).

3. Check application logs:
   ```bash
   aws logs tail /ecs/medic8-prod --since 15m --filter-pattern "ERROR"
   ```
   - Look for: PHP fatal errors, database connection failures, Redis connection failures, out-of-memory errors.

4. **If deployment-related** (error began immediately after a deployment):
   ```bash
   # Roll back to the previous task definition
   aws ecs describe-services --cluster medic8-prod --services medic8-app \
     --query 'services[0].taskDefinition'
   # Note the current revision number, subtract 1
   aws ecs update-service --cluster medic8-prod --service medic8-app \
     --task-definition medic8-app:<previous-revision>
   ```

5. **If database-related** (logs show `SQLSTATE` errors or connection refused):
   ```bash
   aws rds describe-db-instances --db-instance-identifier medic8-prod
   ```
   - Check `DBInstanceStatus`. If not `available`, check for ongoing maintenance or failover.
   - If Multi-AZ failover is needed:
     ```bash
     aws rds reboot-db-instance --db-instance-identifier medic8-prod \
       --force-failover
     ```

6. **If Redis-related** (logs show Redis connection errors):
   ```bash
   aws elasticache describe-cache-clusters --cache-cluster-id medic8-redis
   ```
   - Check node status. If node is being replaced, wait for automatic recovery.
   - If Redis is full, flush the cache (not sessions):
     ```bash
     redis-cli -h <redis-host> FLUSHDB
     ```

7. **Escalation path:**
   - First: Peter (System Owner) — phone call
   - Second: AWS Support (if infrastructure issue) — open a Severity 1 case via AWS Console

---

### 2.2 Database Performance Degradation

**Severity:** Warning (escalate to Critical if patient care is affected)
**Response Time:** Acknowledge within 1 hour

**Symptoms:** API response times exceed 500 ms at P95. Slow query alerts in CloudWatch. Users report "loading" screens.

**Procedure:**

1. Open RDS Performance Insights:
   ```
   AWS Console → RDS → Performance Insights → medic8-prod
   ```
   - Identify the top wait events. Common causes:
     - `IO:DataFileRead` — table scan on a large table (missing index)
     - `lock:table` — table lock from DDL or long transaction
     - `CPU` — complex query consuming excessive CPU

2. Identify blocking queries:
   ```sql
   SELECT * FROM information_schema.INNODB_TRX
   WHERE trx_state = 'LOCK WAIT'
   ORDER BY trx_wait_started;
   ```

3. Kill long-running queries if safe (only if the query is not a critical transaction):
   ```sql
   -- Identify the thread ID from Performance Insights or:
   SHOW FULL PROCESSLIST;
   -- Kill the offending query:
   KILL <thread_id>;
   ```
   *Do not kill queries from the migration runner or the HMIS sync process without checking first.*

4. Check if a migration is running:
   ```sql
   SELECT * FROM migrations ORDER BY id DESC LIMIT 5;
   ```
   - If a migration is in progress, wait for it to complete. Migrations lock tables temporarily.

5. Verify index health:
   ```sql
   -- Check for missing indexes on frequently queried columns
   SELECT * FROM sys.schema_unused_indexes;
   SELECT * FROM sys.schema_redundant_indexes;
   ```

6. If the issue persists, scale up the RDS instance:
   ```bash
   aws rds modify-db-instance --db-instance-identifier medic8-prod \
     --db-instance-class db.r6g.xlarge --apply-immediately
   ```
   *This causes a brief outage (30-60 seconds) during the instance class change. Schedule during low-traffic hours if possible.*

---

### 2.3 Data Breach Suspected

**Severity:** Critical
**Response Time:** Immediate

**Symptoms:** Unusual access patterns in audit logs. Report from a user. Alert from AWS GuardDuty. Unexpected data export.

*This procedure is governed by Uganda PDPA 2019 Section 31. The 72-hour notification clock starts when the breach is confirmed.*

**Procedure:**

1. **Isolate the affected facility immediately:**
   ```bash
   # Disable API access for the facility
   php artisan facility:suspend <facility_id> --reason="Security incident investigation"
   ```
   - This blocks all API requests for the facility while preserving data.
   - Notify the Facility Admin that access is temporarily suspended for security reasons.

2. **Capture the audit trail** for the affected time period:
   ```bash
   php artisan audit:export --facility=<facility_id> \
     --from="YYYY-MM-DD HH:MM" --to="YYYY-MM-DD HH:MM" \
     --output=/tmp/breach-audit-<facility_id>.csv
   ```

3. **Run the breach impact report** to identify affected patient records:
   ```bash
   php artisan breach:impact --facility=<facility_id> \
     --from="YYYY-MM-DD HH:MM" --to="YYYY-MM-DD HH:MM"
   ```
   - Output: list of patient IDs, record types accessed, accessor identity, IP addresses.

4. **Notify Peter immediately** — phone call, not Slack.

5. **Start the 72-hour clock.** Under PDPA 2019 Section 31, the Personal Data Protection Office must be notified within 72 hours of confirming a breach.
   - Document the breach in the incident log with:
     - Date and time of discovery
     - Date and time breach is believed to have occurred
     - Type of data affected (PHI, PII)
     - Number of affected individuals
     - Actions taken to contain the breach

6. **Preserve all evidence.** Do not delete logs, modify database records, or restart services until the investigation is complete.

7. **If credentials are compromised:**
   ```bash
   # Rotate all secrets immediately
   php artisan key:generate --force
   # Rotate database credentials in Secrets Manager
   # Rotate API keys (MoMo, Airtel, Africa's Talking)
   # Invalidate all active sessions
   php artisan session:flush
   # Invalidate all JWT tokens
   php artisan jwt:invalidate-all
   ```

---

### 2.4 Clinical Safety Incident

**Severity:** Critical
**Response Time:** Immediate

**Symptoms:** A clinician reports that the system displayed incorrect clinical information, failed to display an expected alert, or contributed to a patient safety event.

**Procedure:**

1. **Capture the full audit trail** for the encounter:
   ```bash
   php artisan encounter:audit --encounter-id=<encounter_id> --full
   ```
   - Output: every action taken during the encounter (vitals entry, diagnosis, prescription, CDS alerts fired, CDS alerts overridden, dispensing, lab orders).

2. **Preserve CDS alert and override logs:**
   ```bash
   php artisan cds:audit --encounter-id=<encounter_id>
   ```
   - Output: every CDS rule evaluated, alerts generated, alerts displayed to the clinician, overrides (with clinician ID, reason text, timestamp).

3. **Notify Peter and the clinical advisor immediately** — phone call.

4. **Root cause analysis within 24 hours.** Determine:
   - Was the CDS rule correct? (Check the drug interaction database, allergy data, dosing formula.)
   - Was the alert displayed to the clinician? (Check WebSocket delivery log.)
   - Did the clinician override the alert? (Check override log with reason text.)
   - Was the data entry correct? (Check audit trail for the vitals/diagnosis/prescription.)
   - Was there a system failure? (Check Sentry for errors during the encounter timeframe.)

5. **If the system caused or contributed to the incident:**
   - Create a hotfix branch immediately.
   - Deploy the hotfix using the expedited deployment process:
     - Skip staging soak time (but still run all CI checks).
     - Production deployment with manual approval from Peter.
   - Document the fix and the root cause in the incident log.

6. **If the system functioned correctly** (clinician error or override):
   - Document the finding.
   - Review whether the CDS alert was clear enough — consider improving the alert text or severity level.

---

### 2.5 Mobile Money Payment Failure

**Severity:** Warning (escalate to Critical if affecting > 10 facilities)
**Response Time:** Acknowledge within 1 hour

**Symptoms:** Patients report payments taken from their mobile money account but not reflected in Medic8. Billing staff report pending payments.

**Procedure:**

1. **Check MoMo/Airtel API status:**
   ```bash
   # MTN MoMo API health
   curl -s -o /dev/null -w "%{http_code}" https://sandbox.momodeveloper.mtn.com/v1_0/apiuser
   # Airtel Money API health
   curl -s -o /dev/null -w "%{http_code}" https://openapiuat.airtel.africa/auth/oauth2/token
   ```
   - If the API returns `5xx` or is unreachable, the issue is on the provider's side. Log and monitor.

2. **Check the suspense account** for unmatched payments:
   ```bash
   php artisan payments:suspense --status=unmatched --from="today"
   ```
   - The suspense account holds payments received via callback but not yet matched to a patient invoice.

3. **If the API is down**, perform manual reconciliation:
   - Export pending payments from Medic8.
   - Cross-reference with the MoMo/Airtel merchant portal transaction history.
   - Manually match payments to invoices:
     ```bash
     php artisan payments:reconcile --transaction-id=<momo_txn_id> --invoice-id=<invoice_id>
     ```

4. **Notify affected patients** if payment was received but not applied:
   ```bash
   php artisan patients:notify-payment-pending --facility=<facility_id> --date="today"
   ```
   - SMS notification: "Your payment of UGX [amount] has been received and is being processed. Receipt will be issued shortly."

5. **If the issue is systemic** (all facilities affected):
   - Contact MTN MoMo API Support or Airtel Money API Support (see Contact Directory).
   - Post a notice in the Medic8 admin panel: "Mobile money payments are temporarily delayed. Cash payments are available."

---

### 2.6 DHIS2 Sync Failure

**Severity:** Warning
**Response Time:** Acknowledge within 1 hour

**Symptoms:** HMIS Sync Dashboard shows `failed` status for one or more facilities. CloudWatch alarm for DHIS2 sync failure.

**Procedure:**

1. **Check DHIS2 API availability:**
   ```bash
   curl -s -o /dev/null -w "%{http_code}" -u "$DHIS2_USERNAME:$DHIS2_PASSWORD" \
     https://hmis2.health.go.ug/api/system/info
   ```
   - `200` — API is available; the issue is in the data or mapping.
   - `401` — Credentials expired. Rotate credentials with MoH eHealth.
   - `5xx` or timeout — DHIS2 server is down. Log and retry.

2. **Verify HMIS data format compatibility:**
   ```bash
   php artisan hmis:validate --facility=<facility_id> --period=<YYYYMM>
   ```
   - Check for: missing required data elements, invalid org unit IDs, data element ID mismatches (form version change).

3. **Auto-retry is configured:** The sync job retries 3 times with exponential backoff (1 minute, 5 minutes, 25 minutes).
   ```bash
   # Check retry status
   php artisan hmis:sync-status --facility=<facility_id>
   ```

4. **If auto-retry fails**, queue for manual retry:
   ```bash
   php artisan hmis:sync --facility=<facility_id> --period=<YYYYMM> --force
   ```

5. **If the DHIS2 server is down for > 24 hours**, use the manual CSV export fallback:
   ```bash
   php artisan hmis:export-csv --facility=<facility_id> --period=<YYYYMM> \
     --output=/tmp/hmis-export-<facility_id>-<YYYYMM>.csv
   ```
   - The CSV can be manually uploaded to the DHIS2 web interface when it becomes available.

6. **If the failure is due to a form version change:**
   - Check MoH notices for updated HMIS form definitions.
   - Update `hmis_data_elements` configuration table.
   - Test against sample facility data.
   - Deploy the update (see Maintenance Section 3.4).

---

### 2.7 Offline Facility Cannot Sync

**Severity:** Warning (escalate to Critical if sync queue > 72 hours)
**Response Time:** Acknowledge within 1 hour

**Symptoms:** Offline Facilities dashboard shows a facility has not synced for > 24 hours.

**Procedure:**

1. **Check the facility's internet status:**
   - Contact the Facility Admin by phone to confirm connectivity status.
   - Common causes: ISP outage, power outage (no generator/UPS), SIM card data exhaustion (if using 4G modem).

2. **Verify sync queue size:**
   ```bash
   # If the local server is reachable via VPN or phone hotspot:
   ssh medic8@<facility-local-ip> "php artisan sync:queue-size"
   ```
   - If the queue contains < 72 hours of data, the risk is manageable. Monitor and wait for connectivity.

3. **If the sync queue exceeds 72 hours:**
   - **Priority 1:** Restore connectivity. Options:
     - Contact the facility's ISP.
     - Dispatch a 4G modem with a prepaid data SIM.
     - If in Kampala area, arrange a temporary mobile hotspot visit.
   - **Priority 2:** If connectivity cannot be restored within 24 hours, dispatch a technician to perform a manual data export:
     ```bash
     # On the local server
     php artisan sync:export --output=/media/usb/medic8-sync-<facility_id>-<date>.enc
     ```
     - The export is AES-256 encrypted. Transfer via USB drive to a connected workstation and import:
     ```bash
     php artisan sync:import --file=/path/to/medic8-sync-<facility_id>-<date>.enc
     ```

4. **If the local server has a hardware failure:**
   - Dispatch a replacement device (Intel NUC or Raspberry Pi 4) pre-provisioned with the facility's configuration.
   - Data recovery from the failed device's SSD:
     - Remove the SSD and connect to a recovery workstation.
     - Mount the filesystem and extract the MySQL data directory.
     - Import into the replacement device's MySQL instance.
   - If the SSD is unrecoverable, restore from the last successful cloud sync. *Data entered between the last sync and the failure is lost.* Document the data loss window and notify affected clinicians.

---

### 2.8 AI Provider Outage

Severity: Critical
Response Time: Acknowledge within 15 minutes

Symptoms: AI capability endpoints return HTTP 503; clinicians see "AI service temporarily unavailable" messages.

1. Check `ai_usage_log` for error codes on recent requests from the affected tenant.
2. Confirm the primary provider status page (external) shows an active incident.
3. In the tenant admin panel → AI Settings, switch `primary_provider` to a working provider.
4. Alternatively, confirm the failover provider is configured and functioning (the system attempts this automatically within 10 s of primary failure).
5. Notify affected tenant AI Administrator by email: "AI features are temporarily using [failover provider] due to a [primary provider] outage. Clinical features are unaffected."
6. Monitor `ai_usage_log.was_failover` count. Return to primary provider once the outage resolves.

---

### 2.9 AI Credit Exhaustion

Severity: Warning
Response Time: Acknowledge within 1 hour

Symptoms: AI capability endpoints return HTTP 402; clinicians see credit exhaustion messages.

1. The system automatically pauses all AI capabilities when `credit_balance` reaches 0. Clinical features are unaffected — confirm this.
2. Check `tenant_ai_config.credit_balance` in the database to confirm it is 0.
3. The tenant AI Administrator receives an automatic email notification when balance falls below the configured threshold (default 10% of last top-up).
4. If the AI Administrator has not responded, escalate to the facility billing contact.
5. Credit top-up is processed via the Medic8 admin panel → Billing → AI Credit Top-Up.
6. Once the top-up is processed, AI capabilities resume automatically — no restart required.

---

### 2.10 UI Rendering English in Non-English Locale

Severity: Warning
Response Time: Acknowledge within 1 hour

Symptoms: A clinician or patient reports that the UI is displaying English text when they are set to French or Kiswahili.

1. Identify the affected string by opening the browser developer tools console. Look for `[I18N-GAP: <key>]` log entries.
2. Note the key (e.g., `opd.triage.blood_pressure_label`).
3. Confirm the key exists in `lang/en/<module>.php` but is missing or null in `lang/fr/<module>.php` or `lang/sw/<module>.php`.
4. Add the missing translation (contextual, not word-for-word) to the appropriate locale file.
5. Deploy as a hotfix. No database migration required.
6. Verify the fix by switching locale in a test session and confirming the string now renders in the target language.

---

## 3. Maintenance Procedures

### 3.1 Database Maintenance

#### 3.1.1 Index Rebuild

- **Frequency:** Monthly
- **Schedule:** Sunday 02:00 EAT (lowest traffic window)
- **Procedure:**
  ```sql
  -- Run on the primary instance via a maintenance connection
  -- Large tables only — small tables do not benefit
  ALTER TABLE encounters ENGINE=InnoDB;
  ALTER TABLE observations ENGINE=InnoDB;
  ALTER TABLE audit_logs ENGINE=InnoDB;
  ALTER TABLE medications ENGINE=InnoDB;
  ALTER TABLE patients ENGINE=InnoDB;
  ```
  *`ALTER TABLE ... ENGINE=InnoDB` rebuilds the table and all indexes in-place (InnoDB online DDL). This is non-blocking for reads but may briefly block writes on very large tables.*

#### 3.1.2 Table Optimisation

- **Frequency:** Quarterly
- **Target tables:** `encounters`, `audit_logs`, `observations`, `lab_results` (tables exceeding 10 million rows)
- **Procedure:**
  ```sql
  ANALYZE TABLE encounters;
  ANALYZE TABLE audit_logs;
  ANALYZE TABLE observations;
  ANALYZE TABLE lab_results;
  ```

#### 3.1.3 Audit Log Archival

- **Frequency:** Annually (or when `audit_logs` table exceeds 50 GB)
- **Retention rule:** Audit logs older than 2 years are moved to cold storage (S3 Glacier).
- **Procedure:**
  ```bash
  # Export old audit logs
  php artisan audit:archive --before="2024-04-01" \
    --output=s3://medic8-prod-archive/audit-logs/

  # Verify the export
  php artisan audit:verify-archive --file=s3://medic8-prod-archive/audit-logs/<filename>

  # Only after verification succeeds:
  php artisan audit:purge --before="2024-04-01" --confirm
  ```
  *Never purge audit logs without verifying the archive. This data is required for PDPA 2019 compliance and may be needed for legal proceedings.*

---

### 3.2 Application Updates

#### 3.2.1 Standard Deployment (Zero-Downtime)

ECS rolling update replaces tasks one at a time. The ALB drains connections from the old task before terminating it.

- **Minimum healthy percent:** 100% (at least the current number of tasks remain healthy during deployment)
- **Maximum percent:** 200% (new tasks are launched before old tasks are terminated)
- **Health check grace period:** 60 seconds

#### 3.2.2 Major Version Deployment (Blue/Green)

For major version changes (PHP version upgrade, Laravel major version, database schema overhaul):

1. Deploy the new version to a separate ECS service (`medic8-app-green`).
2. Point a test ALB listener to the green service.
3. Run smoke tests against the green service.
4. Switch the production ALB listener to the green service.
5. Monitor for 30 minutes.
6. If stable, decommission the blue service.
7. If unstable, switch the ALB listener back to the blue service.

#### 3.2.3 Rollback Window

- **Rolling updates:** Rollback by reverting to the previous ECS task definition revision. Effective within 2-3 minutes.
- **Blue/green deployments:** Rollback by switching the ALB listener back to the blue service. Effective within 30 seconds.
- **Rollback window:** 30 minutes post-deployment. After 30 minutes, the deployment is considered stable and the previous version is decommissioned.

---

### 3.3 Drug Formulary Updates

#### 3.3.1 Trigger

The drug formulary is updated when the National Drug Authority (NDA) Uganda, Pharmacy and Poisons Board (PPB) Kenya, CDSCO India, or TGA Australia publishes changes. Monitor NDA notices at `https://www.nda.or.ug`.

#### 3.3.2 Procedure

1. Download the updated formulary data from the regulatory authority.
2. Update the `DrugFormularySeeder` data file with the changes.
3. Run the seeder in staging:
   ```bash
   php artisan db:seed --class=DrugFormularySeeder --env=staging
   ```
4. Verify the changes in the staging Pharmacy module.
5. Deploy to production:
   ```bash
   php artisan db:seed --class=DrugFormularySeeder --env=production
   ```
6. Notify all facilities via the admin notification system:
   ```bash
   php artisan notify:facilities --message="Drug formulary updated on <date>. Please review changes in the Pharmacy module."
   ```
7. Log the change in the formulary version history table.

#### 3.3.3 Narcotic Schedule Changes

Changes to narcotic or controlled substance schedules require immediate deployment. Do not wait for the regular update cycle. Follow the standard procedure above but with expedited review (Peter must approve within 4 hours of notification).

---

### 3.4 HMIS Form Updates

#### 3.4.1 Trigger

The Uganda Ministry of Health publishes updated HMIS form definitions. Monitor `hmis2.health.go.ug` and MoH circular notices. Target turnaround: 30 days from MoH publication to production deployment.

#### 3.4.2 Procedure

1. Obtain the updated form definition from MoH.
2. Update the `hmis_data_elements` configuration table:
   ```bash
   php artisan hmis:update-form --form=<form_id> --version=<new_version> \
     --definition=/path/to/new-definition.json
   ```
3. Test against sample facility data (at least 3 facilities with different data profiles):
   ```bash
   php artisan hmis:test-export --facility=<facility_id> --period=<YYYYMM> --form-version=<new_version>
   ```
4. Compare the test output with a manually completed form to verify data element mapping.
5. Deploy to staging and run a full DHIS2 sync test.
6. Deploy to production.
7. Notify all affected facilities.

#### 3.4.3 Fallback

If the new form version is not yet mapped, the system exports data using the previous form version with a warning flag: `[HMIS-VERSION-MISMATCH: expected <new_version>, exported <old_version>]`. The facility's HMIS focal person must manually verify the export.

---

### 3.5 SSL Certificate Renewal

#### 3.5.1 ACM Certificates (Web)

AWS Certificate Manager auto-renews certificates 60 days before expiry. No manual action is required.

**Verification:** Check ACM Console monthly (Monthly Checklist item 6). If any certificate shows `PENDING_VALIDATION`, the DNS validation record may have been deleted. Re-create the CNAME record in Route 53.

#### 3.5.2 Mobile Certificate Pins

Mobile apps use certificate pinning. Certificate pin rotation requires coordination between the server and mobile app releases.

**Procedure:**

1. Generate the new certificate (or note the upcoming ACM renewal).
2. Calculate the SHA-256 pin of the new certificate's Subject Public Key Info (SPKI).
3. Release a mobile app update that includes both the old and new pins (90-day overlap).
4. Wait for the app update to reach > 95% adoption (check Play Store and App Store analytics).
5. Only then allow the old certificate to expire.
6. After expiry, release a mobile app update that removes the old pin.

*If a pin mismatch occurs before the app is updated, affected users see "Please update your app" and cannot use the app. This is a patient safety concern — plan pin rotations at least 90 days in advance.*

---

## 4. Contact Directory

| Role | Name | Contact Method | Escalation Level |
|---|---|---|---|
| System Owner | Peter | Phone: [on file in Secrets Manager] | Primary — all incidents |
| AWS Support | — | AWS Console → Support → Create Case | Infrastructure (Severity 1 for Critical) |
| MTN MoMo API Support | MTN Uganda | Phone: [on file] / Email: [on file] | Payment failures |
| Airtel Money API Support | Airtel Uganda | Phone: [on file] / Email: [on file] | Payment failures |
| Africa's Talking Support | — | support@africastalking.com | SMS/USSD failures |
| DHIS2 / eHMIS Support | MoH eHealth Division | Email: [on file] / Phone: [on file] | HMIS sync failures |
| NDA Uganda | National Drug Authority | Phone: +256-417-255665 | Drug formulary queries |
| Clinical Advisor | [TBD] | Phone: [on file] | Clinical safety incidents |

### 4.1 Escalation Matrix

| Incident Type | First Responder | Escalation 1 (15 min) | Escalation 2 (1 hour) |
|---|---|---|---|
| Application down | On-call engineer | Peter | AWS Support |
| Database degradation | On-call engineer | Peter | AWS Support |
| Data breach | Peter | Legal counsel | PDPO Uganda |
| Clinical safety | Peter + Clinical Advisor | — | — |
| Payment failure | On-call engineer | Peter | MoMo/Airtel Support |
| DHIS2 sync failure | On-call engineer | Peter | MoH eHealth |
| Offline facility sync | On-call engineer | Peter | Field technician |

---

## 5. Post-Incident Review Template

Complete this template within 48 hours of resolving any Critical incident.

```
## Post-Incident Review

**Incident ID:** INC-YYYY-NNN
**Date/Time Detected:** YYYY-MM-DD HH:MM EAT
**Date/Time Resolved:** YYYY-MM-DD HH:MM EAT
**Duration:** X hours Y minutes
**Severity:** Critical / Warning
**Affected Facilities:** [list]
**Affected Patients:** [count, if applicable]

### Timeline
- HH:MM — [event]
- HH:MM — [action taken]
- HH:MM — [resolution]

### Root Cause
[Description of the root cause]

### Impact
- Clinical impact: [none / delayed care / incorrect data displayed / ...]
- Data impact: [none / data loss of X records / ...]
- Financial impact: [none / delayed payments / ...]

### Corrective Actions
1. [Action] — Owner: [name] — Due: [date]
2. [Action] — Owner: [name] — Due: [date]

### Preventive Actions
1. [Action to prevent recurrence] — Owner: [name] — Due: [date]
```

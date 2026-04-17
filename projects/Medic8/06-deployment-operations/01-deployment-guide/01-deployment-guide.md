# Deployment Guide for Medic8 Healthcare Management System

**Version:** 1.0
**Last Updated:** 2026-04-03
**Classification:** Internal — Operations Team Only

---

## 1. Infrastructure Architecture

### 1.1 Cloud Provider

Medic8 runs on Amazon Web Services (AWS) as the primary cloud provider. The architecture uses managed services to minimise operational overhead and maximise availability.

**Alternative Providers:** Azure and Google Cloud Platform (GCP) are viable alternatives. Key service mappings:

| AWS Service | Azure Equivalent | GCP Equivalent |
|---|---|---|
| EC2 / ECS | Azure Container Instances / AKS | Cloud Run / GKE |
| RDS MySQL | Azure Database for MySQL | Cloud SQL for MySQL |
| ElastiCache Redis | Azure Cache for Redis | Memorystore for Redis |
| S3 | Azure Blob Storage | Cloud Storage |
| CloudFront | Azure CDN | Cloud CDN |
| Route 53 | Azure DNS | Cloud DNS |
| SES | Azure Communication Services | — (use SendGrid) |
| ALB | Azure Application Gateway | Cloud Load Balancing |

### 1.2 Region Strategy

| Region | AWS Region ID | Primary Market | Rationale |
|---|---|---|---|
| Africa | af-south-1 (Cape Town) | Uganda, Kenya, Tanzania, Rwanda, Nigeria | Lowest latency to East and West Africa; PDPA 2019 data residency compliance |
| India | ap-south-1 (Mumbai) | India | DISHA compliance; Ayushman Bharat Digital Mission integration |
| Australia | ap-southeast-2 (Sydney) | Australia | Privacy Act 1988 compliance; My Health Records Act 2012 |

Each region operates as an independent deployment. Patient data never leaves the region unless the tenant's regulatory profile explicitly permits cross-border transfer (NFR-HC-006).

### 1.3 Component Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                        Route 53 (DNS)                       │
│                     *.medic8.com → ALB                      │
└────────────────────────────┬────────────────────────────────┘
                             │
┌────────────────────────────▼────────────────────────────────┐
│              CloudFront (CDN — static assets)               │
└────────────────────────────┬────────────────────────────────┘
                             │
┌────────────────────────────▼────────────────────────────────┐
│           Application Load Balancer (ALB, HTTPS)            │
│             TLS 1.2+ termination, health checks             │
└──────┬─────────────────────┬────────────────────────────────┘
       │                     │
┌──────▼──────┐     ┌───────▼───────┐
│  ECS Fargate │     │  ECS Fargate  │    ← Auto-scaling group
│  (App Task)  │     │  (App Task)   │       min 2, max 10
└──────┬──────┘     └───────┬───────┘
       │                     │
       └──────────┬──────────┘
                  │
    ┌─────────────┼─────────────┐
    │             │             │
┌───▼───┐  ┌─────▼─────┐  ┌───▼───┐
│  RDS   │  │ElastiCache│  │  S3   │
│MySQL 8 │  │  Redis 7  │  │Bucket │
│(Multi- │  │(cache,    │  │(files,│
│  AZ)   │  │ queues,   │  │images)│
│        │  │ sessions) │  │       │
└────────┘  └───────────┘  └───────┘
```

| Component | Service | Purpose |
|---|---|---|
| Application | ECS Fargate (or EC2) | PHP 8.2 application containers (Laravel) |
| Database | RDS MySQL 8.x (Multi-AZ) | Primary data store with InnoDB Cluster |
| Cache / Queues | ElastiCache Redis 7 | Session store, cache, Laravel Horizon queue driver |
| File Storage | S3 | Clinical documents, medical images, reports, backups |
| CDN | CloudFront | Static assets (CSS, JS, images), patient portal |
| DNS | Route 53 | Domain management, health-check-based failover |
| Email | SES | Transactional email (appointment reminders, reports) |
| Load Balancer | ALB | HTTPS termination, path-based routing, health checks |
| SMS / USSD | Africa's Talking | Patient notifications, USSD appointment booking |
| Payments | MTN MoMo API, Airtel Money API | Mobile money collections |

---

## 2. Environment Configuration

### 2.1 Environments

| Environment | Purpose | URL Pattern | Deployment |
|---|---|---|---|
| Development | Feature development, debugging | `dev.medic8.local` | Manual / on push to `develop` |
| Staging | Pre-production validation, UAT | `staging.medic8.com` | Auto on merge to `staging` |
| Production | Live patient data | `app.medic8.com` | Manual approval required |

### 2.2 Environment Variables

All secrets are stored in AWS Secrets Manager or HashiCorp Vault. Environment variables referencing `[vault]` must never appear in plaintext in code, CI logs, or configuration files.

| Variable | Description | Example (Production) |
|---|---|---|
| `APP_ENV` | Application environment | `production` |
| `APP_KEY` | Laravel application key | `[vault]` |
| `APP_URL` | Base URL | `https://app.medic8.com` |
| `DB_HOST` | MySQL host | `medic8-prod.cluster-xxx.af-south-1.rds.amazonaws.com` |
| `DB_PORT` | MySQL port | `3306` |
| `DB_DATABASE` | Database name | `medic8_production` |
| `DB_USERNAME` | Database user | `[vault]` |
| `DB_PASSWORD` | Database password | `[vault]` |
| `REDIS_HOST` | Redis host | `medic8-redis.xxx.af-south-1.cache.amazonaws.com` |
| `REDIS_PORT` | Redis port | `6379` |
| `REDIS_PASSWORD` | Redis auth token | `[vault]` |
| `MOMO_API_KEY` | MTN Mobile Money API key | `[vault]` |
| `MOMO_API_SECRET` | MTN MoMo API secret | `[vault]` |
| `MOMO_ENVIRONMENT` | MoMo sandbox or production | `production` |
| `AIRTEL_API_KEY` | Airtel Money API key | `[vault]` |
| `AIRTEL_API_SECRET` | Airtel Money API secret | `[vault]` |
| `AFRICAS_TALKING_KEY` | Africa's Talking SMS gateway key | `[vault]` |
| `AFRICAS_TALKING_USERNAME` | Africa's Talking username | `medic8` |
| `FHIR_BASE_URL` | FHIR R4 API base URL | `https://api.medic8.com/fhir` |
| `DHIS2_API_URL` | Uganda eHMIS DHIS2 endpoint | `https://hmis2.health.go.ug/api` |
| `DHIS2_USERNAME` | DHIS2 API user | `[vault]` |
| `DHIS2_PASSWORD` | DHIS2 API password | `[vault]` |
| `ENCRYPTION_KEY` | AES-256-GCM encryption key for PHI at rest | `[vault]` |
| `JWT_SECRET` | JWT signing secret for mobile/API auth | `[vault]` |
| `SESSION_LIFETIME` | Session timeout in minutes | `15` |
| `MAIL_MAILER` | Mail driver | `ses` |
| `AWS_ACCESS_KEY_ID` | AWS IAM access key | `[vault]` |
| `AWS_SECRET_ACCESS_KEY` | AWS IAM secret key | `[vault]` |
| `AWS_DEFAULT_REGION` | AWS region | `af-south-1` |
| `AWS_BUCKET` | S3 bucket for file storage | `medic8-prod-files` |
| `WEBSOCKET_PORT` | WebSocket server port (critical lab alerts) | `6001` |
| `LOG_CHANNEL` | Logging channel | `stack` |
| `LOG_LEVEL` | Minimum log level | `warning` |

### 2.3 Environment Parity Rules

1. Staging must mirror production infrastructure (same RDS instance class, same Redis node type) to catch performance issues before production.
2. Development may use smaller instances but must use the same MySQL 8.x and Redis 7 versions.
3. All environments must enforce TLS 1.2+ — no exceptions for development.
4. Test data in staging must be anonymised. Real patient data must never leave production.

---

## 3. Deployment Pipeline (CI/CD)

### 3.1 Pipeline Overview

The CI/CD pipeline uses GitHub Actions. Every push triggers the pipeline; production deployment requires manual approval from the System Owner.

### 3.2 Pipeline Stages

```yaml
# .github/workflows/deploy.yml (simplified)
name: Medic8 CI/CD

on:
  push:
    branches: [develop, staging, main]
  pull_request:
    branches: [main]

jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: PHP CS Fixer
        run: vendor/bin/php-cs-fixer fix --dry-run --diff
      - name: PHPStan Level 8
        run: vendor/bin/phpstan analyse --level=8

  unit-tests:
    needs: lint
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: PHPUnit
        run: vendor/bin/phpunit --testsuite=Unit

  integration-tests:
    needs: lint
    runs-on: ubuntu-latest
    services:
      mysql:
        image: mysql:8.0
        env:
          MYSQL_DATABASE: medic8_test
          MYSQL_ROOT_PASSWORD: testing
        ports: ['3306:3306']
      redis:
        image: redis:7
        ports: ['6379:6379']
    steps:
      - uses: actions/checkout@v4
      - name: PHPUnit Integration
        run: vendor/bin/phpunit --testsuite=Integration

  security-scan:
    needs: lint
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Composer Audit
        run: composer audit
      - name: OWASP Dependency Check
        uses: dependency-check/Dependency-Check_Action@main
      - name: PHP Security Checker
        run: vendor/bin/security-checker security:check

  build:
    needs: [unit-tests, integration-tests, security-scan]
    runs-on: ubuntu-latest
    steps:
      - name: Build Docker Image
        run: docker build -t medic8:${{ github.sha }} .
      - name: Push to ECR
        run: |
          aws ecr get-login-password | docker login --username AWS --password-stdin $ECR_REGISTRY
          docker push $ECR_REGISTRY/medic8:${{ github.sha }}

  deploy-staging:
    needs: build
    if: github.ref == 'refs/heads/staging'
    runs-on: ubuntu-latest
    environment: staging
    steps:
      - name: Update ECS Service (Staging)
        run: |
          aws ecs update-service --cluster medic8-staging \
            --service medic8-app --force-new-deployment

  deploy-production:
    needs: build
    if: github.ref == 'refs/heads/main'
    runs-on: ubuntu-latest
    environment:
      name: production
      # Manual approval gate — requires System Owner sign-off
    steps:
      - name: Pre-deployment RDS Snapshot
        run: |
          aws rds create-db-snapshot \
            --db-instance-identifier medic8-prod \
            --db-snapshot-identifier pre-deploy-${{ github.sha }}
      - name: Update ECS Service (Production)
        run: |
          aws ecs update-service --cluster medic8-prod \
            --service medic8-app --force-new-deployment
      - name: Run Migrations
        run: |
          aws ecs run-task --cluster medic8-prod \
            --task-definition medic8-migrate \
            --overrides '{"containerOverrides":[{"name":"app","command":["php","artisan","migrate","--force"]}]}'
      - name: Verify Health
        run: |
          sleep 60
          curl -f https://app.medic8.com/health || exit 1
```

### 3.3 Pipeline Rules

1. **No direct pushes to `main`.** All changes go through pull requests with at least 1 reviewer.
2. **All 4 checks must pass** (lint, unit tests, integration tests, security scan) before merge is permitted.
3. **Production deployment requires manual approval** via GitHub Environments. Only the System Owner can approve.
4. **Every production deployment is preceded by an automated RDS snapshot.** The snapshot must complete before the ECS service update begins.
5. **Rollback procedure:** revert the ECS task definition to the previous revision. See Section 3.4.

### 3.4 Rollback Procedure

If a production deployment causes errors:

1. Identify the previous stable task definition revision:
   ```bash
   aws ecs describe-services --cluster medic8-prod --services medic8-app \
     --query 'services[0].taskDefinition'
   ```
2. Roll back the ECS service to the previous task definition:
   ```bash
   aws ecs update-service --cluster medic8-prod --service medic8-app \
     --task-definition medic8-app:<previous-revision>
   ```
3. If the deployment included a database migration, roll back the migration:
   ```bash
   php artisan migrate:rollback --step=1
   ```
4. Verify the health endpoint returns `200`:
   ```bash
   curl -f https://app.medic8.com/health
   ```
5. Notify the team in the `#medic8-ops` Slack channel.

---

## 4. Database Deployment

### 4.1 Migration Strategy

All database changes use Laravel migrations (`php artisan migrate`). Migrations follow a zero-downtime strategy:

1. **Additive changes first.** Add new columns, tables, or indexes before deploying code that uses them.
2. **No destructive changes in the same release.** Column drops, renames, and type changes require a 2-release cycle: Release N adds the new structure; Release N+1 removes the old structure after confirming no code references it.
3. **Every migration must have a working `down()` method.** Migrations without rollback capability are rejected in code review.

### 4.2 Pre-Migration Backup

Every production migration is preceded by an automated RDS snapshot (triggered in the CI/CD pipeline). The snapshot identifier follows the pattern `pre-deploy-<commit-sha>`.

To create a manual snapshot:

```bash
aws rds create-db-snapshot \
  --db-instance-identifier medic8-prod \
  --db-snapshot-identifier manual-$(date +%Y%m%d-%H%M%S)
```

### 4.3 Migration Execution

```bash
# Staging (automatic)
php artisan migrate --force

# Production (via ECS run-task in CI/CD pipeline)
aws ecs run-task --cluster medic8-prod \
  --task-definition medic8-migrate \
  --overrides '{"containerOverrides":[{"name":"app","command":["php","artisan","migrate","--force"]}]}'
```

### 4.4 Rollback

```bash
# Roll back the last batch
php artisan migrate:rollback --step=1

# Roll back to a specific batch
php artisan migrate:rollback --step=<N>
```

*Every migration must be tested with its rollback in staging before production deployment.*

### 4.5 Seeders

The following reference data is seeded during initial deployment and updated as needed:

| Seeder | Data | Source |
|---|---|---|
| `CountryConfigSeeder` | Country regulatory profiles, currencies, tax tables | Internal configuration |
| `DrugFormularySeeder` | Drug catalogue per country formulary | NDA Uganda, PPB Kenya, CDSCO India, TGA Australia |
| `ICD10Seeder` | ICD-10 diagnosis codes (full code set) | WHO ICD-10 2019 |
| `LOINCSeeder` | LOINC laboratory observation codes | Regenstrief Institute |
| `EPIScheduleSeeder` | Immunisation schedules per country | MoH EPI Uganda, UIP India, NIP Australia |
| `HMISFormSeeder` | HMIS data elements and form definitions | MoH Uganda HMIS 105/108/033b |
| `RolePermissionSeeder` | 18 built-in roles and permissions | Internal RBAC design |
| `LabTestCatalogueSeeder` | Standard laboratory test catalogue | CPHL Uganda, WHO EML |

To run seeders:

```bash
# All seeders
php artisan db:seed

# Specific seeder
php artisan db:seed --class=DrugFormularySeeder
```

---

## 5. Facility Onboarding Deployment

### 5.1 New Tenant Provisioning

New facility onboarding is triggered via an API call from the admin panel. The provisioning process:

1. System Owner creates the facility record in the Super Admin panel.
2. The system generates a unique `facility_id` and creates the tenant row in the `facilities` table.
3. The `FacilityProvisioningJob` (queued via Laravel Horizon) executes the following:
   - Seed 18 built-in roles with default permissions
   - Create the Facility Admin user account
   - Copy the default price list template
   - Load the country-specific drug formulary
   - Load the standard lab test catalogue
   - Configure HMIS form definitions for the facility's country
   - Set the immunisation schedule for the facility's country
   - Configure the regulatory profile (PDPA, HIPAA, Privacy Act, DISHA)
   - Set currency, tax tables, and insurance schemes

### 5.2 Default Data Seeded per Facility

| Data Set | Count (Approximate) | Source |
|---|---|---|
| Roles | 18 built-in | RBAC design |
| Price list template | 1 (editable) | Default template |
| Drug formulary | 3,000+ entries | Country NDA/PPB/CDSCO/TGA |
| Lab test catalogue | 500+ tests | CPHL, WHO |
| ICD-10 codes | 14,000+ | WHO |
| LOINC codes | 2,000+ (common subset) | Regenstrief Institute |
| HMIS data elements | 200+ per form | MoH |
| Immunisation schedule | Country-specific | EPI/UIP/NIP |

### 5.3 Country-Specific Configuration

| Configuration | Uganda | Kenya | India | Australia |
|---|---|---|---|---|
| HMIS forms | 105, 108, 033b | MOH 105 | HMIS (national) | — |
| Immunisation schedule | EPI Uganda | EPI Kenya | UIP India | NIP Australia |
| Tax tables | VAT 18% | VAT 16% | GST 18% | GST 10% |
| Insurance schemes | NHIS Uganda | NHIF Kenya | Ayushman Bharat | Medicare/PBS |
| Drug formulary | NDA Uganda | PPB Kenya | CDSCO India | TGA Australia |
| Data protection | PDPA 2019 | DPA 2019 | DISHA | Privacy Act 1988 |
| National ID | NIN | Huduma Namba | Aadhaar / ABHA | Medicare Number |
| Currency | UGX | KES | INR | AUD |

### 5.4 Onboarding Time Target

**Target: 2-4 hours from account creation to first patient registration.**

| Step | Duration | Responsible |
|---|---|---|
| Facility record creation | 5 minutes | System Owner |
| Automated provisioning | 2-5 minutes | System (queued job) |
| Facility Admin account setup | 10 minutes | Facility Admin |
| Staff account creation | 30-60 minutes | Facility Admin |
| Price list customisation | 30-60 minutes | Facility Admin / Accountant |
| First patient registration | Immediate | Records Officer |

---

## 6. SSL/TLS Configuration

### 6.1 Certificate Management

- All domains use AWS Certificate Manager (ACM) certificates.
- ACM handles automatic renewal — no manual certificate rotation required for web endpoints.
- Certificates are attached to the ALB and CloudFront distributions.

### 6.2 Protocol Configuration

| Setting | Value |
|---|---|
| Minimum TLS version | TLS 1.2 |
| TLS 1.0 | Disabled |
| TLS 1.1 | Disabled |
| Cipher suites | AWS ALB default policy (`ELBSecurityPolicy-TLS13-1-2-2021-06` or later) |
| HSTS | `Strict-Transport-Security: max-age=31536000; includeSubDomains; preload` |
| HSTS max-age | 1 year (31,536,000 seconds) |

### 6.3 Mobile App Certificate Pinning

- Android and iOS apps pin the leaf certificate and 1 backup intermediate certificate.
- Certificate pins must be updated in the mobile app before the server certificate rotates.
- Maintain a 90-day overlap between old and new certificate pins during rotation.
- Pin update releases must be published to Play Store and App Store at least 30 days before the old certificate expires.
- If a pin mismatch occurs, the app displays a "Please update your app" message and blocks API calls to prevent man-in-the-middle attacks.

---

## 7. Monitoring and Alerting

### 7.1 Application Monitoring

| Tool | Environment | Purpose |
|---|---|---|
| Laravel Telescope | Staging only | Request inspection, query debugging, job monitoring |
| Sentry | Production | Error tracking, exception grouping, release tracking |
| Laravel Horizon | All | Queue monitoring, job throughput, failed job alerts |

*Laravel Telescope must never be enabled in production. It logs request data including PHI, which creates a compliance risk.*

### 7.2 Infrastructure Monitoring

| Metric | Source | Threshold | Alert Level |
|---|---|---|---|
| CPU utilisation | CloudWatch (ECS) | > 80% sustained 5 min | Warning |
| CPU utilisation | CloudWatch (ECS) | > 95% sustained 2 min | Critical |
| Memory utilisation | CloudWatch (ECS) | > 85% | Warning |
| Disk usage | CloudWatch (RDS) | > 80% free storage | Warning |
| Network errors | CloudWatch (ALB) | > 1% 5xx rate | Critical |
| RDS connections | CloudWatch (RDS) | > 80% of max_connections | Warning |
| Redis memory | CloudWatch (ElastiCache) | > 80% used memory | Warning |

### 7.3 Database Monitoring

- **RDS Performance Insights:** Enabled on all RDS instances. Review weekly for query performance trends.
- **Slow query log:** Enabled with `long_query_time = 2` seconds. Queries exceeding this threshold are logged and reviewed weekly.
- **InnoDB deadlock monitoring:** CloudWatch alarm on `Deadlocks` metric exceeding 0 in any 5-minute window.

### 7.4 Uptime Monitoring

- **External monitoring:** UptimeRobot or Pingdom checks the `/health` endpoint every 60 seconds from multiple global locations.
- **SLA target:** 99.9% uptime (no more than 8.76 hours downtime per year).
- **Health endpoint checks:**
  - Database connectivity
  - Redis connectivity
  - Disk space
  - Queue health (no failed jobs older than 15 minutes)

### 7.5 Alert Routing

| Severity | Channel | Response Time |
|---|---|---|
| Critical | PagerDuty / OpsGenie (phone call + push notification) | Acknowledge within 15 minutes |
| Warning | Slack `#medic8-alerts` | Review within 1 hour |
| Info | Slack `#medic8-ops` | Review next business day |

### 7.6 Clinical Alert Monitoring

- WebSocket server health check: the monitoring system sends a ping to the WebSocket server every 60 seconds.
- If the WebSocket server is unreachable for 2 consecutive checks (2 minutes), a Critical alert is triggered.
- WebSocket is used for critical lab value notifications and emergency alerts — downtime directly affects patient safety.

---

## 8. Backup and Disaster Recovery

### 8.1 Database Backups

| Backup Type | Method | Frequency | Retention |
|---|---|---|---|
| Automated snapshot | RDS automated backups | Daily | 30 days |
| Point-in-time recovery | RDS continuous backup | Continuous (5-minute granularity) | 30 days |
| Cross-region replication | RDS read replica | Continuous | Always available |
| Pre-deployment snapshot | Manual (CI/CD triggered) | Every production deployment | 90 days |

### 8.2 File Backups

| Storage | Method | Retention |
|---|---|---|
| S3 clinical documents | S3 versioning | All versions retained for 10 years (MoH data retention) |
| S3 cross-region replication | S3 replication rule | Replicated to secondary region |

### 8.3 Recovery Objectives

| Metric | Target | Method |
|---|---|---|
| Recovery Point Objective (RPO) | < 1 hour | RDS point-in-time recovery (5-minute granularity) |
| Recovery Time Objective (RTO) | < 4 hours | Failover to read replica, promote to primary |

### 8.4 Disaster Recovery Procedure

1. **Detect:** CloudWatch alarm or external monitoring detects primary region failure.
2. **Assess:** Confirm the failure is not a transient issue (wait 5 minutes, check AWS Health Dashboard).
3. **Failover database:** Promote the cross-region read replica to a standalone primary:
   ```bash
   aws rds promote-read-replica \
     --db-instance-identifier medic8-dr-replica
   ```
4. **Update DNS:** Switch Route 53 records to point to the DR region's ALB:
   ```bash
   aws route53 change-resource-record-sets \
     --hosted-zone-id <zone-id> \
     --change-batch file://dr-failover.json
   ```
5. **Deploy application:** Launch ECS tasks in the DR region using the latest container image.
6. **Verify:** Run the health check and confirm the application is operational.
7. **Notify:** Inform all facility administrators of the failover and any data loss window.

### 8.5 DR Drill Schedule

- **Frequency:** Quarterly.
- **Scope:** Full failover to the DR region, including DNS switch, database promotion, and application deployment.
- **Documentation:** Each drill produces a post-drill report documenting: time to failover, data loss (if any), issues encountered, and remediation actions.
- **Next scheduled drill:** Record the date in the ops calendar after each drill.

---

## 9. Scaling Strategy

### 9.1 Horizontal Scaling (Application)

ECS auto-scaling is configured with the following policies:

| Metric | Scale-Out Threshold | Scale-In Threshold | Cooldown |
|---|---|---|---|
| Average CPU utilisation | > 70% for 3 minutes | < 30% for 10 minutes | 300 seconds |
| Request count per target | > 1,000 requests/minute | < 200 requests/minute | 300 seconds |

- **Minimum tasks:** 2 (for high availability)
- **Maximum tasks:** 10 (adjustable based on growth)
- **Task size:** 1 vCPU, 2 GB memory (adjustable)

### 9.2 Database Scaling

| Strategy | Use Case | Method |
|---|---|---|
| Read replicas | Reporting queries, HMIS exports, analytics | RDS read replica (up to 5) |
| Vertical scaling | Write-heavy workloads | Increase RDS instance class (e.g., `db.r6g.large` → `db.r6g.xlarge`) |
| Connection pooling | High concurrent connections | RDS Proxy |

- Reporting queries (HMIS exports, financial reports, analytics dashboards) must be routed to read replicas. The application uses a `reporting` database connection that points to the read replica endpoint.
- Write operations always go to the primary instance.

### 9.3 Redis Scaling

| Strategy | Use Case |
|---|---|
| Cluster mode | Session and cache scaling beyond single-node capacity |
| Vertical scaling | Increase node size for larger working sets |
| Separate clusters | Dedicate one cluster for queues (Horizon) and one for cache/sessions |

### 9.4 CDN Scaling

CloudFront handles static asset distribution globally. Configuration:

- Cache static assets (CSS, JS, images, fonts) with 24-hour TTL.
- Patient portal pages cached at the edge with 5-minute TTL and `Cache-Control: private` for authenticated content.
- Origin failover: configure CloudFront origin group with primary and secondary origins.

---

## 10. Local Server Deployment (Offline Facilities)

### 10.1 Use Case

For health facilities with unreliable or no internet connectivity (common in rural Uganda, Kenya, and India), Medic8 supports a local server deployment. The local server runs the full application stack and synchronises with the cloud when connectivity is available.

### 10.2 Hardware Requirements

| Component | Minimum Specification |
|---|---|
| Device | Intel NUC (recommended) or Raspberry Pi 4 (8 GB RAM) |
| Processor | Intel i3 or ARM Cortex-A72 (Raspberry Pi 4) |
| RAM | 8 GB |
| Storage | 256 GB SSD |
| Network | Ethernet port, optional 4G/LTE USB modem |
| Power | UPS with 4-hour battery backup |

### 10.3 Software Stack

| Component | Version |
|---|---|
| Operating system | Ubuntu Server 22.04 LTS |
| PHP | 8.2 |
| MySQL | 8.x |
| Redis | 7.x |
| Nginx | Latest stable |
| Supervisor | Latest (for queue workers) |

### 10.4 Automated Provisioning

Local servers are provisioned using an Ansible playbook:

```bash
# From the ops workstation
ansible-playbook -i inventory/local-servers playbooks/provision-local-server.yml \
  --extra-vars "facility_id=<facility_id> country=<country_code>"
```

The playbook:

1. Installs the OS-level dependencies (PHP, MySQL, Redis, Nginx, Supervisor).
2. Deploys the Medic8 application from the latest release tarball.
3. Configures MySQL with the facility's database and seeds reference data.
4. Sets up the sync agent (see Section 10.5).
5. Configures automatic security updates (`unattended-upgrades`).
6. Hardens the server (firewall, SSH key-only access, disabled root login).

### 10.5 Sync Agent

The sync agent runs as a cron job and synchronises the local server with the cloud when connectivity is available:

```bash
# Crontab entry — runs every 5 minutes
*/5 * * * * /opt/medic8/sync-agent.sh >> /var/log/medic8/sync.log 2>&1
```

Sync behaviour:

1. **Connectivity check:** Ping the cloud API endpoint. If unreachable, log and exit.
2. **Upload:** Push all locally created/modified records since the last successful sync (delta sync using `updated_at` timestamps).
3. **Download:** Pull any records updated in the cloud for this facility (e.g., drug formulary updates, role changes).
4. **Conflict resolution:** Last-write-wins with server authority. Conflicts are logged for manual review.
5. **Sync window:** If the connection drops mid-sync, the agent resumes from the last confirmed checkpoint.

### 10.6 Data Integrity

- The local MySQL database is the authoritative source for the facility's data while offline.
- Once synced, the cloud database becomes authoritative.
- If the local server's sync queue exceeds 72 hours, the system alerts the System Owner for intervention (see Runbook Section 2.7).

---

## AI Intelligence Deployment Checklist

1. In the tenant admin panel, navigate to AI Settings.
2. Select the primary AI provider (`openai`, `anthropic`, `deepseek`, or `gemini`).
3. Enter the primary API key (stored AES-256-GCM encrypted; never stored in plaintext).
4. Select a failover provider and enter its API key.
5. Select billing model: `credit_pack` or `flat_fee`.
6. If `credit_pack`: set the initial credit balance in the admin panel.
7. Enable or disable individual AI capabilities from the capability toggles panel.
8. Run a health check: `GET /api/v1/ai/usage` — assert HTTP 200 and `credit_balance` ≥ 0.
9. Confirm the AI Administrator role is assigned to at least 1 user at the facility.
10. Verify `was_failover` monitoring is configured in the observability stack.

---

## i18n Deployment Checklist

1. Run `php artisan i18n:audit` — assert zero `[I18N-GAP]` entries. If any gaps are present, the deployment is blocked.
2. Confirm `lang/fr/` and `lang/sw/` directories are present in the deployment artifact with the same file list as `lang/en/`.
3. Confirm Android build includes `values-fr/strings.xml` and `values-sw/strings.xml`.
4. Confirm iOS build includes `fr.lproj/Localizable.strings` and `sw.lproj/Localizable.strings`.
5. Smoke test: log in as a test user; switch locale to `sw`; confirm all strings on the OPD triage screen render in Kiswahili.
6. Smoke test: switch locale to `fr`; confirm the same screen renders in French.

# Deployment Guide — Academia Pro

**Document ID:** DG-06-01
**Project:** Academia Pro
**Version:** 1.0.0
**Date:** 2026-04-03
**Status:** Draft — Pending Consultant Review

---

## 1. Purpose

This document specifies the infrastructure, configuration, build pipeline, and deployment procedures required to run Academia Pro in development, staging, and production environments. It covers initial deployment through ongoing scaling and disaster recovery.

---

## 2. Infrastructure Architecture

### 2.1 AWS Service Map

| Service | Purpose | Phase |
|---|---|---|
| EC2 (t3.medium initial) | Application server — Laravel API + Horizon queue worker | Phase 1 |
| RDS MySQL 8.x (db.t3.medium) | Primary relational database with Multi-AZ failover | Phase 1 |
| ElastiCache Redis 7 (cache.t3.micro) | Session store, cache driver, queue driver (Horizon) | Phase 1 |
| S3 | Object storage — report card PDFs, student photos, import files, backups | Phase 1 |
| CloudFront | CDN for static assets (React build output, uploaded images) | Phase 1 |
| Route 53 | DNS management for `academiapro.co.ug` and tenant subdomains | Phase 1 |
| SES | Transactional email delivery (password resets, fee receipts, notifications) | Phase 1 |
| ECS Fargate | Container orchestration — replaces direct EC2 for auto-scaling | Phase 8+ |
| CloudWatch | Metrics, alarms, log aggregation | Phase 1 |
| WAF | Web Application Firewall — OWASP managed rule group | Phase 1 |

### 2.2 Network Topology

```
Internet
  │
  ├── CloudFront (static assets, S3 origin)
  │
  ├── Route 53 → ALB (Application Load Balancer)
  │     ├── Target Group: EC2 App Servers (port 443)
  │     └── Health Check: GET /api/health → 200 OK
  │
  ├── EC2 App Server(s)
  │     ├── Laravel API (PHP-FPM + Nginx)
  │     ├── Laravel Horizon (queue worker)
  │     └── Meilisearch (search engine)
  │
  ├── RDS MySQL 8.x (Private Subnet)
  │     ├── Primary (eu-west-1a)
  │     └── Standby (eu-west-1b, Multi-AZ)
  │
  ├── ElastiCache Redis (Private Subnet)
  │
  └── S3 (academiapro-assets, academiapro-backups)
```

Security groups restrict all database and cache traffic to the application subnet. No RDS or ElastiCache endpoint is publicly accessible.

### 2.3 Region Selection

Primary region: `af-south-1` (Cape Town) — lowest latency to Uganda. If `af-south-1` is unavailable or cost-prohibitive at launch, fall back to `eu-west-1` (Ireland) with CloudFront edge in Nairobi.

---

## 3. Environment Configuration

### 3.1 Environment Definitions

| Environment | Purpose | URL | Database |
|---|---|---|---|
| Development | Local developer machines (WAMP64 / WSL2) | `academiapro.test` | Local MySQL 8.x |
| Staging | Pre-production validation, QA testing | `staging.academiapro.co.ug` | RDS (separate instance) |
| Production | Live tenant data | `app.academiapro.co.ug` | RDS Multi-AZ |

### 3.2 Environment Variables

All environment-specific configuration is stored in `.env` files on the server (never committed to version control). The canonical variable list follows.

#### Application Core

| Variable | Example (Production) | Notes |
|---|---|---|
| `APP_NAME` | `AcademiaPro` | |
| `APP_ENV` | `production` | `local`, `staging`, or `production` |
| `APP_KEY` | `base64:...` | Generated via `php artisan key:generate` — unique per environment |
| `APP_DEBUG` | `false` | Must be `false` in production and staging |
| `APP_URL` | `https://app.academiapro.co.ug` | |
| `APP_TIMEZONE` | `Africa/Kampala` | UTC+3 (EAT) |

#### Database

| Variable | Example (Production) | Notes |
|---|---|---|
| `DB_CONNECTION` | `mysql` | |
| `DB_HOST` | `academiapro-prod.xxxx.af-south-1.rds.amazonaws.com` | RDS endpoint |
| `DB_PORT` | `3306` | |
| `DB_DATABASE` | `academiapro_prod` | |
| `DB_USERNAME` | `academiapro_app` | Application-level user, not `root` |
| `DB_PASSWORD` | (stored in AWS Secrets Manager) | Rotated every 90 days |
| `DB_CHARSET` | `utf8mb4` | Required for emoji and extended Unicode |
| `DB_COLLATION` | `utf8mb4_unicode_ci` | |

#### Cache and Queue

| Variable | Example | Notes |
|---|---|---|
| `CACHE_DRIVER` | `redis` | |
| `QUEUE_CONNECTION` | `redis` | Horizon requires Redis |
| `SESSION_DRIVER` | `redis` | |
| `REDIS_HOST` | `academiapro-redis.xxxx.af-south-1.cache.amazonaws.com` | ElastiCache endpoint |
| `REDIS_PORT` | `6379` | |
| `REDIS_PASSWORD` | (stored in AWS Secrets Manager) | AUTH token for ElastiCache |

#### Storage

| Variable | Example | Notes |
|---|---|---|
| `FILESYSTEM_DISK` | `s3` | |
| `AWS_ACCESS_KEY_ID` | (IAM role preferred) | Use EC2 instance profile, not static keys |
| `AWS_SECRET_ACCESS_KEY` | (IAM role preferred) | |
| `AWS_DEFAULT_REGION` | `af-south-1` | |
| `AWS_BUCKET` | `academiapro-assets` | |
| `AWS_URL` | `https://assets.academiapro.co.ug` | CloudFront distribution URL |

#### Email (SES)

| Variable | Example | Notes |
|---|---|---|
| `MAIL_MAILER` | `ses` | |
| `MAIL_FROM_ADDRESS` | `noreply@academiapro.co.ug` | Verified SES identity |
| `MAIL_FROM_NAME` | `AcademiaPro` | |

#### SMS (Africa's Talking)

| Variable | Example | Notes |
|---|---|---|
| `AT_API_KEY` | (stored in AWS Secrets Manager) | |
| `AT_USERNAME` | `academiapro` | Sandbox: `sandbox` |
| `AT_SENDER_ID` | `AcademPro` | Registered Uganda sender ID (≤ 11 chars) |

#### Payments (Phase 2+)

| Variable | Example | Notes |
|---|---|---|
| `SCHOOLPAY_MERCHANT_ID` | (from SchoolPay) | Phase 2 |
| `SCHOOLPAY_API_KEY` | (stored in AWS Secrets Manager) | Phase 2 |
| `SCHOOLPAY_API_URL` | `https://api.schoolpay.co.ug/v1` | Production endpoint |
| `SCHOOLPAY_WEBHOOK_SECRET` | (stored in AWS Secrets Manager) | HMAC-SHA256 verification |
| `MOMO_SUBSCRIPTION_KEY` | (stored in AWS Secrets Manager) | Phase 3 |
| `MOMO_API_USER` | (from MTN Developer Portal) | Phase 3 |
| `MOMO_ENVIRONMENT` | `production` | `sandbox` or `production` |
| `MOMO_CALLBACK_URL` | `https://app.academiapro.co.ug/api/webhooks/momo` | Phase 3 |

#### Monitoring

| Variable | Example | Notes |
|---|---|---|
| `SENTRY_LARAVEL_DSN` | `https://xxx@sentry.io/yyy` | Production and staging only |
| `TELESCOPE_ENABLED` | `false` | `true` on staging only — never in production |
| `LOG_CHANNEL` | `stack` | Channels: `daily` + `stderr` (CloudWatch) |
| `LOG_LEVEL` | `warning` | Production: `warning`; Staging: `debug` |

---

## 4. CI/CD Pipeline

### 4.1 Pipeline Tool

GitHub Actions. All workflows are stored in `.github/workflows/`.

### 4.2 Pipeline Stages

The pipeline executes on every push to `main` (production deployment) and every push to `develop` or pull request targeting `develop` (staging deployment).

#### Stage 1 — Lint

```yaml
- name: PHP CS Fixer
  run: vendor/bin/php-cs-fixer fix --dry-run --diff --config=.php-cs-fixer.php

- name: PHPStan Level 8
  run: vendor/bin/phpstan analyse --level=8 --memory-limit=512M

- name: ESLint + Prettier
  run: npm run lint && npm run format:check
```

All lint failures block the pipeline. No exceptions.

#### Stage 2 — Test

```yaml
- name: PHPUnit / Pest
  run: php artisan test --parallel --processes=4
  env:
    DB_CONNECTION: mysql
    DB_DATABASE: academiapro_test

- name: Vitest (Frontend)
  run: npm run test:ci

- name: Playwright E2E
  run: npx playwright test --reporter=github
```

Test coverage thresholds enforced: backend ≥ 80% line coverage; frontend ≥ 70% component coverage. UNEB grading engine and fee calculation logic require 100% coverage.

#### Stage 3 — Security Scan

```yaml
- name: Composer Audit
  run: composer audit

- name: npm Audit
  run: npm audit --audit-level=high

- name: Trivy Container Scan
  uses: aquasecurity/trivy-action@master
  with:
    scan-type: fs
    severity: HIGH,CRITICAL
```

Any HIGH or CRITICAL vulnerability blocks deployment. MEDIUM vulnerabilities are logged as GitHub Issues for resolution within 14 days.

#### Stage 4 — Build

```yaml
- name: Build Frontend
  run: npm run build

- name: Build Docker Image
  run: docker build -t academiapro-api:${{ github.sha }} .

- name: Push to ECR
  run: |
    aws ecr get-login-password | docker login --username AWS --password-stdin $ECR_URI
    docker push $ECR_URI/academiapro-api:${{ github.sha }}
```

#### Stage 5 — Deploy

```yaml
# Staging (automatic on develop merge)
- name: Deploy to Staging
  run: |
    aws ecs update-service --cluster academiapro-staging \
      --service academiapro-api --force-new-deployment

# Production (manual approval gate)
- name: Deploy to Production
  environment: production
  run: |
    aws ecs update-service --cluster academiapro-prod \
      --service academiapro-api --force-new-deployment
```

Production deployments require manual approval from a designated GitHub environment reviewer (Peter or designated DevOps lead).

### 4.3 Post-Deployment Checks

After every deployment the pipeline runs:

1. Health check: `curl -f https://app.academiapro.co.ug/api/health` — must return HTTP 200 within 30 seconds.
2. Smoke test: a lightweight Playwright suite that logs in, loads the dashboard, and verifies the version number matches the deployed commit SHA.
3. If health check fails, the pipeline triggers automatic rollback to the previous ECS task definition revision.

---

## 5. Database Deployment

### 5.1 Migration Strategy

All schema changes use Laravel migrations (`php artisan migrate`). Raw SQL files are prohibited in the migration pipeline.

#### Migration Execution Order

1. Run `php artisan migrate --force` in the CI/CD deploy step.
2. Migrations execute against the production database from the deployment container before the new application version receives traffic.
3. The ALB health check holds traffic on the old task definition until the new container passes health checks.

### 5.2 Zero-Downtime Migrations

All migrations must be backward-compatible with the currently running application version. This requires:

- **Adding columns:** Use `nullable()` or provide a `default()` value. The old code ignores the new column.
- **Renaming columns:** Deploy in 2 phases. Phase A: add the new column, copy data, deploy code that reads both. Phase B: drop the old column after all instances run the new code.
- **Dropping columns:** Never drop a column in the same release that stops using it. Wait 1 release cycle.
- **Adding indexes:** Use `ALGORITHM=INPLACE` where possible. For large tables (> 1 million rows), schedule index creation during the Saturday 02:00 - 04:00 EAT maintenance window.

### 5.3 Rollback Procedure

1. Identify the failing migration by reviewing the `migrations` table and the Laravel log.
2. Run `php artisan migrate:rollback --step=N` where N is the number of migrations to revert.
3. If the rollback `down()` method is destructive (drops data), restore from the most recent pre-migration database snapshot instead.
4. Every migration file must include a `down()` method. Migrations without `down()` methods are rejected in code review.

### 5.4 Seeders — Uganda Reference Data

The following seeders populate reference data required for Uganda schools. They run once during initial deployment and are idempotent (safe to re-run).

| Seeder Class | Data | Notes |
|---|---|---|
| `UgandaCurriculumSeeder` | Subject list for Thematic (P1-P3), Upper Primary (P4-P7), O-Level, A-Level | Sourced from NCDC Uganda syllabus catalogue |
| `UnebGradingSeeder` | PLE grading scale, UCE 9-point scale, UACE point scale, Thematic competency descriptors | BR-UNEB-001 through BR-UNEB-004 |
| `FeeStructureTemplateSeeder` | Default fee line items: tuition, boarding, lunch, transport, PTA, development levy | Editable per school — these are starting templates only |
| `AcademicCalendarSeeder` | Term structure: Term 1 (Feb-May), Term 2 (Jun-Aug), Term 3 (Sep-Dec) | Default Uganda calendar; dates are configurable per school |
| `RolesAndPermissionsSeeder` | 11 roles, all permissions, role-permission mappings | Per RBAC matrix in `02-requirements-engineering/03-stakeholder-analysis/01-rbac-matrix.md` |
| `DefaultClassStructureSeeder` | P1-P7, S.1-S.4, S.5-S.6 with `promotes_to` linkages | BR-PROM-002 |

#### Seeder Execution

```bash
# Initial deployment — run all seeders
php artisan db:seed --force

# Update reference data (e.g., UNEB grading table change)
php artisan db:seed --class=UnebGradingSeeder --force
```

Seeders use `updateOrCreate()` to ensure idempotency. Running a seeder twice produces no duplicate records.

---

## 6. School Onboarding — Tenant Provisioning

### 6.1 Provisioning Workflow

When a new school signs up, the system executes the following steps atomically within a database transaction.

1. **Create tenant record:** Insert into `tenants` table with `name`, `subdomain`, `subscription_plan`, `status = active`.
2. **Create School Owner user:** The signup form captures the owner's name, email, phone, and password. The user is assigned the `school_owner` role for this tenant.
3. **Seed default academic structure:**
   - Create 1 academic year (current calendar year).
   - Create 3 terms with default Uganda calendar dates (configurable).
   - Create default classes: P1 through P7 for primary schools; S.1 through S.6 for secondary schools (school type selected at signup).
   - Create 1 default stream per class (Stream A).
   - Link `promotes_to` for each class per BR-PROM-002.
4. **Seed default fee structure:** Copy `FeeStructureTemplateSeeder` defaults into the tenant's fee tables. The School Owner adjusts amounts before the first billing cycle.
5. **Seed default subjects:** Copy subjects from `UgandaCurriculumSeeder` appropriate to the school type (primary or secondary).
6. **Seed grading schemes:** Copy UNEB grading tables from `UnebGradingSeeder`.
7. **Send welcome email:** Via SES — contains login URL, quick-start guide link, and training video playlist link.

### 6.2 Time-to-Operational Target

A Uganda school shall be operational within 30 minutes of signup, as specified in the Design Covenant. "Operational" means: the School Owner can log in, see the pre-populated class structure, add students, record attendance, and enter marks — without configuring any settings.

### 6.3 Subdomain Configuration

Each tenant receives a subdomain: `<school-slug>.academiapro.co.ug`. Route 53 is configured with a wildcard CNAME record (`*.academiapro.co.ug → ALB`). The application resolves the tenant from the subdomain at the middleware layer.

---

## 7. SSL/TLS Configuration

### 7.1 Certificate Management

| Component | Certificate Source | Renewal |
|---|---|---|
| ALB (HTTPS termination) | AWS Certificate Manager (ACM) | Auto-renew (managed by AWS) |
| CloudFront distribution | ACM (us-east-1 region, required by CloudFront) | Auto-renew |
| Staging environment | Let's Encrypt (Certbot) | Auto-renew via cron (every 60 days) |

### 7.2 TLS Requirements

Per the quality standards:

- Minimum TLS version: 1.3 for all client-facing endpoints.
- TLS 1.2 permitted only for legacy USSD integration (Phase 11).
- ALB security policy: `ELBSecurityPolicy-TLS13-1-2-2021-06` or newer.
- HSTS header: `Strict-Transport-Security: max-age=31536000; includeSubDomains; preload`.
- HTTP-to-HTTPS redirect enforced at the ALB listener level (HTTP 301).

### 7.3 Internal Encryption

- EC2 to RDS: encrypted in transit via RDS SSL certificate (`rds-ca-2019`). Application `.env` includes `MYSQL_ATTR_SSL_CA=/path/to/rds-combined-ca-bundle.pem`.
- EC2 to ElastiCache: in-transit encryption enabled on the Redis replication group.
- S3: server-side encryption with AES-256 (`SSE-S3`) for all objects. Bucket policy denies `PutObject` without `x-amz-server-side-encryption` header.
- RDS storage: encrypted at rest with AWS KMS (default `aws/rds` key).

---

## 8. Monitoring and Alerting

### 8.1 Application Monitoring

| Tool | Environment | Purpose |
|---|---|---|
| Laravel Telescope | Staging only | Request/response inspection, query log, job monitoring, exception viewer |
| Sentry | Production + Staging | Exception tracking, performance tracing, release tracking |
| Laravel Horizon Dashboard | Production + Staging | Queue health, job throughput, failed jobs |

Telescope is disabled in production (`TELESCOPE_ENABLED=false`) to prevent performance overhead and data exposure.

### 8.2 Infrastructure Monitoring (CloudWatch)

| Metric | Alarm Threshold | Action |
|---|---|---|
| EC2 CPU utilization | > 80% sustained for 5 minutes | SNS alert to ops team; trigger Auto Scaling if enabled |
| RDS CPU utilization | > 70% sustained for 10 minutes | SNS alert; investigate slow queries |
| RDS free storage | < 10 GB | SNS alert; expand storage or archive old data |
| RDS replica lag (Multi-AZ) | > 60 seconds | SNS alert; investigate replication health |
| ElastiCache evictions | > 100/minute | SNS alert; consider memory scaling |
| ALB 5xx error rate | > 1% of requests over 5 minutes | SNS alert; check application logs |
| ALB target response time (P95) | > 2,000 ms over 5 minutes | SNS alert; check Horizon queue backlog |
| SES bounce rate | > 5% | SNS alert; review recipient list quality |

### 8.3 Uptime Monitoring

External uptime monitor (UptimeRobot or Healthchecks.io) pings `https://app.academiapro.co.ug/api/health` every 60 seconds. The health endpoint checks:

1. Database connectivity (SELECT 1)
2. Redis connectivity (PING)
3. S3 accessibility (HeadBucket)
4. Queue health (Horizon status)

If any check fails, the endpoint returns HTTP 503 with a JSON body identifying the failing component. The uptime monitor alerts via SMS and email.

### 8.4 Uptime Targets

| Period | Target | Maximum Downtime |
|---|---|---|
| Standard months | ≥ 99.5% | ≤ 3.65 hours/month |
| Exam periods (Term 3) | ≥ 99.9% | ≤ 0.73 hours/month |

---

## 9. Backup and Disaster Recovery

### 9.1 Backup Schedule

| Component | Method | Frequency | Retention |
|---|---|---|---|
| RDS MySQL | Automated snapshots (AWS) | Daily at 01:00 EAT | 30 days |
| RDS MySQL | Transaction log backups | Every 5 minutes (point-in-time recovery) | 30 days |
| S3 objects | S3 versioning + cross-region replication to `eu-west-1` | Continuous | 90 days for deleted objects |
| Redis (ElastiCache) | Daily snapshot | Daily at 02:00 EAT | 7 days |
| Application code | Git repository (GitHub) | Every commit | Indefinite |
| `.env` configuration | AWS Secrets Manager | On change | Version history maintained by Secrets Manager |

### 9.2 Recovery Objectives

| Metric | Target |
|---|---|
| Recovery Point Objective (RPO) | < 1 hour data loss (achieved via 5-minute transaction log backups) |
| Recovery Time Objective (RTO) | < 4 hours to full service restoration |

### 9.3 Disaster Recovery Procedure

1. **Identify failure scope:** single EC2 instance, RDS primary, entire AZ, or entire region.
2. **Single EC2 failure:** Auto Scaling group launches replacement instance automatically. No manual action required. Expected recovery: < 10 minutes.
3. **RDS primary failure:** Multi-AZ failover promotes standby to primary automatically. Expected recovery: < 5 minutes. Application reconnects via RDS DNS endpoint.
4. **Entire AZ failure:** ALB routes traffic to instances in the surviving AZ. RDS fails over. Expected recovery: < 15 minutes.
5. **Entire region failure (catastrophic):**
   1. Restore RDS from cross-region snapshot replica in `eu-west-1`.
   2. Deploy application stack in `eu-west-1` using the same CloudFormation/Terraform templates.
   3. Update Route 53 to point to the new ALB.
   4. Restore S3 data from cross-region replication bucket.
   5. Expected recovery: < 4 hours.
6. **Post-recovery validation:**
   1. Run the health check endpoint.
   2. Verify tenant count matches pre-failure count.
   3. Spot-check 3 tenants: log in, verify recent data integrity.
   4. Confirm Horizon queue is processing.

### 9.4 Backup Verification

Monthly backup restoration drill: restore the most recent RDS snapshot to a temporary instance, connect the staging application to it, and verify data integrity. Log the drill result in the ops log. Delete the temporary instance after verification.

---

## 10. Scaling Strategy

### 10.1 Phase 1 — Single Server (0–50 Schools)

- 1 EC2 `t3.medium` (2 vCPU, 4 GB RAM)
- RDS `db.t3.medium` (2 vCPU, 4 GB RAM)
- ElastiCache `cache.t3.micro` (0.5 GB)
- Sufficient for up to 50 concurrent schools with typical usage patterns.

### 10.2 Phase 4–7 — Vertical Scaling (50–200 Schools)

- Upgrade EC2 to `t3.large` or `m5.large`.
- Upgrade RDS to `db.r5.large` with read replica for reporting queries.
- Upgrade ElastiCache to `cache.t3.small`.
- Separate Horizon queue worker onto a dedicated EC2 instance to isolate queue processing from web request handling.

### 10.3 Phase 8+ — Horizontal Scaling with ECS Fargate (200–500+ Schools)

- Containerise the application with Docker.
- Deploy to ECS Fargate with auto-scaling policies:
  - Scale out: average CPU > 70% for 3 minutes.
  - Scale in: average CPU < 30% for 10 minutes.
  - Minimum tasks: 2 (high availability).
  - Maximum tasks: 10.
- RDS: upgrade to `db.r5.xlarge` with 1 read replica.
- ElastiCache: upgrade to `cache.r5.large` with cluster mode.
- Meilisearch: move to a dedicated instance or managed service.

### 10.4 Exam Season Scaling

During Term 3 (September–December), examination modules experience 3–5x normal load. Pre-scaling actions:

1. 2 weeks before exam period: increase minimum ECS task count from 2 to 4.
2. Increase RDS read replica count from 1 to 2.
3. Pre-warm CloudFront for report card PDF delivery.
4. Increase ElastiCache node count if eviction rate exceeds baseline.
5. Post-exam period: revert to standard scaling configuration.

---

## 11. Payment Integration Deployment

### 11.1 SchoolPay Integration (Phase 2)

#### API Credentials

| Item | Source | Storage |
|---|---|---|
| Merchant ID | SchoolPay merchant onboarding | AWS Secrets Manager |
| API Key | SchoolPay merchant dashboard | AWS Secrets Manager |
| Webhook Secret | SchoolPay merchant dashboard | AWS Secrets Manager |

#### Webhook Endpoint

| Parameter | Value |
|---|---|
| URL | `https://app.academiapro.co.ug/api/webhooks/schoolpay` |
| Method | POST |
| Authentication | HMAC-SHA256 signature in `X-SchoolPay-Signature` header |
| IP Whitelist | SchoolPay-provided IP ranges added to WAF allow list |

#### Deployment Checklist — SchoolPay

1. Register merchant account with SchoolPay and obtain sandbox credentials.
2. Configure sandbox environment variables in staging `.env`.
3. Implement and test webhook handler: signature verification, idempotency key check, payment recording.
4. Test end-to-end in SchoolPay sandbox: generate payment code, simulate payment, verify webhook receipt and fee balance update.
5. Request production credentials from SchoolPay.
6. Configure production environment variables.
7. Add SchoolPay IP ranges to WAF allow list.
8. Deploy to production with feature flag (`SCHOOLPAY_ENABLED=true`).
9. Process 5 test payments with a pilot school before general availability.
10. Monitor webhook success rate for 48 hours post-launch.

### 11.2 MTN MoMo Integration (Phase 3)

#### API Credentials

| Item | Source | Storage |
|---|---|---|
| Subscription Key | MTN Developer Portal (`momodeveloper.mtn.com`) | AWS Secrets Manager |
| API User ID | MTN Developer Portal (sandbox) / MTN Partner Team (production) | AWS Secrets Manager |
| API Key | Generated via provisioning endpoint | AWS Secrets Manager |
| Callback URL | `https://app.academiapro.co.ug/api/webhooks/momo` | Registered with MTN |

#### Deployment Checklist — MoMo

1. Create MTN Developer Portal account and obtain sandbox subscription key.
2. Provision API user and generate API key in sandbox.
3. Implement Collection API: `RequestToPay`, `GetTransactionStatus`, callback handler.
4. Test end-to-end in sandbox: initiate collection, approve on MoMo sandbox UI, verify callback and fee balance update.
5. Apply for production credentials via MTN Partner Team (requires BoU PSO licence — see gap-analysis.md resource list).
6. Configure production environment variables.
7. Deploy with feature flag (`MOMO_ENABLED=true`).
8. Process test collections with pilot school before general availability.
9. Monitor callback delivery rate and reconciliation for 48 hours post-launch.

---

## 12. Pre-Deployment Checklist

Before every production deployment, verify the following items.

1. All CI/CD pipeline stages pass (lint, test, security scan, build).
2. `APP_DEBUG=false` in production `.env`.
3. `TELESCOPE_ENABLED=false` in production `.env`.
4. `APP_KEY` is set and unique to the production environment.
5. Database credentials are stored in AWS Secrets Manager (not in `.env` file on disk for Phase 8+ ECS deployments).
6. SSL certificates are valid and not expiring within 30 days.
7. CloudWatch alarms are active.
8. Sentry DSN is configured and verified (send a test event).
9. Uptime monitor is active for the health endpoint.
10. Backup schedule is confirmed operational (last backup completed within 24 hours).
11. Rollback plan is documented for this specific release (identify which migrations to revert if needed).
12. Release notes are written and stored in the repository.

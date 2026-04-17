---
title: "Deployment Guide -- Maduuka"
version: "1.0"
date: "2026-04-05"
status: "Draft"
author: "Peter Bamuhigire, Chwezi Core Systems"
---

# Deployment Guide -- Maduuka Production System

## 1. Overview

### 1.1 Purpose

This document provides step-by-step procedures for deploying Maduuka to a production server. It covers infrastructure provisioning, server configuration, application deployment, CI/CD pipeline setup, Android app distribution, and post-deployment verification.

### 1.2 Intended Audience

*DevOps engineer or technically capable developer* with working knowledge of Ubuntu server administration, Nginx, PHP-FPM, MySQL, and Git. No application-domain knowledge is assumed.

### 1.3 Environments

| Environment | Purpose | Access |
|---|---|---|
| Development | Local developer machine | Developer only |
| Staging | Pre-production verification | Team + QA |
| Production | Live tenant data | Restricted -- owner approval required |

All three environments share the same codebase. Environment-specific values are isolated in `.env` files that are never committed to Git.

---

## 2. Infrastructure Requirements

### 2.1 Minimum Production Server

| Component | Specification |
|---|---|
| Server type | VPS or cloud instance |
| CPU | 4 vCPU |
| RAM | 8 GB |
| Disk | 100 GB SSD |
| OS | Ubuntu 22.04 LTS |
| Region | Uganda-region preferred (e.g., `af-south-1` AWS Cape Town as nearest available; Contabo Frankfurt as fallback) |
| Web server | Nginx 1.24+ |
| PHP | 8.3+ with extensions: `pdo_mysql`, `mbstring`, `json`, `openssl`, `curl`, `gd`, `zip`, `bcmath` |
| Database | MySQL 8.x |
| Cache / Queue | Redis 7.x |
| Node.js | 20 LTS (asset compilation only -- not required at runtime) |

### 2.2 Wasabi S3-Compatible File Storage

| Setting | Value |
|---|---|
| Provider | Wasabi Cloud Storage |
| Bucket name | `maduuka-prod-files` |
| Contents | Product images, receipt photos, payslip PDFs |
| Region | `eu-central-1` (nearest available to Uganda with acceptable latency) |
| Access | IAM credentials -- least-privilege, scoped to this bucket only |

---

## 3. Pre-Deployment Checklist

Complete every item before the first deployment. Do not proceed to Section 4 until all items are confirmed.

1. Domain name configured and DNS A record propagated (verify with `dig <domain>`).
2. SSL certificate obtained via Let's Encrypt Certbot.
3. Wasabi bucket `maduuka-prod-files` created and IAM credentials generated.
4. Africa's Talking API key obtained and sender ID approved by Africa's Talking.
5. MTN MoMo Business API credentials obtained. *[GAP-001: if not yet resolved, MoMo payment integration stubs until credentials are available -- cash and card sales remain fully operational.]*
6. Airtel Money API credentials obtained.
7. SMTP credentials for transactional email confirmed and tested.
8. Firebase project created with Android FCM and iOS APNs (Phase 2) configured.
9. `.env.production` file populated locally. *Never commit this file to Git.*
10. Daily automated database backup policy configured and tested with a restore drill.

---

## 4. Server Setup

Execute the following steps in order on the production Ubuntu 22.04 instance.

1. Update the OS package index and apply all security patches:

   ```bash
   sudo apt update && sudo apt upgrade -y
   ```

2. Install Nginx, PHP 8.3 with required extensions, MySQL 8, and Redis:

   ```bash
   sudo apt install -y nginx mysql-server redis-server
   sudo add-apt-repository ppa:ondrej/php -y
   sudo apt install -y php8.3-fpm php8.3-mysql php8.3-mbstring \
       php8.3-json php8.3-openssl php8.3-curl php8.3-gd \
       php8.3-zip php8.3-bcmath php8.3-xml php8.3-cli
   ```

3. Configure the Nginx virtual host for HTTPS with PHP-FPM and the following required security headers:

   - `X-Frame-Options: SAMEORIGIN`
   - `X-Content-Type-Options: nosniff`
   - `Strict-Transport-Security: max-age=31536000; includeSubDomains`

   Enable the site and test the configuration: `sudo nginx -t && sudo systemctl reload nginx`.

4. Configure the PHP-FPM pool (`/etc/php/8.3/fpm/pool.d/maduuka.conf`) to run under the application user. Set `pm = dynamic` with `pm.max_children` appropriate to available RAM (guideline: 1 worker per 50 MB average PHP process size).

5. Configure MySQL: create the application database and a dedicated user with least-privilege grants (SELECT, INSERT, UPDATE, DELETE, CREATE, ALTER, INDEX, DROP on the application database only):

   ```sql
   CREATE DATABASE maduuka CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
   CREATE USER 'maduuka'@'localhost' IDENTIFIED BY '<strong-password>';
   GRANT SELECT, INSERT, UPDATE, DELETE, CREATE, ALTER, INDEX, DROP
       ON maduuka.* TO 'maduuka'@'localhost';
   FLUSH PRIVILEGES;
   ```

6. Configure Redis for session storage and the queue driver. In `redis.conf`, bind to `127.0.0.1` only and enable `requirepass`. Update `.env` accordingly: `CACHE_DRIVER=redis`, `SESSION_DRIVER=redis`, `QUEUE_CONNECTION=redis`.

7. Install Composer globally and install PHP dependencies without dev packages:

   ```bash
   composer install --no-dev --optimize-autoloader
   ```

8. Run all pending database migrations:

   ```bash
   php artisan migrate --force
   ```

9. Seed the database with base data (roles, permissions, default platform settings):

   ```bash
   php artisan db:seed --class=ProductionSeeder
   ```

10. Compile front-end assets using Node.js 20 LTS:

    ```bash
    npm ci && npm run build
    ```

11. Set correct file permissions so the web server user can write to required directories:

    ```bash
    sudo chown -R www-data:www-data /var/www/maduuka/storage
    sudo chown -R www-data:www-data /var/www/maduuka/bootstrap/cache
    sudo chmod -R 775 /var/www/maduuka/storage
    sudo chmod -R 775 /var/www/maduuka/bootstrap/cache
    ```

12. Configure Supervisor to keep the queue worker running and auto-restart it on failure. Create `/etc/supervisor/conf.d/maduuka-worker.conf`:

    ```ini
    [program:maduuka-worker]
    command=php /var/www/maduuka/artisan queue:work --sleep=3 --tries=3
    autostart=true
    autorestart=true
    user=www-data
    redirect_stderr=true
    stdout_logfile=/var/log/maduuka/worker.log
    ```

    Reload Supervisor: `sudo supervisorctl reread && sudo supervisorctl update`.

13. Add the Laravel task scheduler to the system crontab for the `www-data` user:

    ```
    * * * * * php /var/www/maduuka/artisan schedule:run >> /dev/null 2>&1
    ```

---

## 5. GitHub Actions CI/CD Pipeline

### 5.1 Pipeline Stages

The pipeline runs on every push to `main` (production) and `staging` branches:

1. **Lint** -- PHP CS Fixer and ESLint checks. Failure blocks all downstream stages.
2. **Test** -- PHPUnit test suite. Failure blocks build and deploy stages.
3. **Build** -- `npm ci && npm run build`; `composer install --no-dev --optimize-autoloader`.
4. **Deploy** -- SSH into the target server and execute the rolling deployment procedure.

### 5.2 Deployment Strategy

Rolling deployment with zero planned downtime:

1. Enable maintenance mode: `php artisan down --secret=<bypass-token>`.
2. Pull latest code from the release branch: `git pull origin main`.
3. Install dependencies: `composer install --no-dev --optimize-autoloader`.
4. Run migrations: `php artisan migrate --force`.
5. Clear and rebuild caches: `php artisan optimize`.
6. Restart queue workers: `sudo supervisorctl restart maduuka-worker`.
7. Disable maintenance mode: `php artisan up`.

### 5.3 Rollback Procedure

If a deployment introduces a critical regression, execute one of the following:

- **Code rollback:** `git revert HEAD` on the release branch, commit, and trigger a new pipeline run.
- **Release tag rollback:** `git checkout <last-known-good-tag>` on the server, run `composer install --no-dev --optimize-autoloader`, then `php artisan migrate --force` if a compensating migration exists.
- **Database rollback:** `php artisan migrate:rollback` -- only if the migration is reversible and no live tenant data has been written to the new schema.

*Document every rollback in the incident log with timestamp, root cause, and resolution.*

---

## 6. Android App Distribution

### 6.1 Release Build

1. Configure the signing keystore in `gradle/signing.properties` (excluded from Git via `.gitignore`).
2. Build the release APK/AAB from Android Studio or via CLI:

   ```bash
   ./gradlew bundleRelease
   ```

3. Verify the AAB is signed: `bundletool validate --bundle=app-release.aab`.

### 6.2 Google Play Store Distribution

- Upload the signed AAB to Google Play Console.
- Promotion path: Internal testing track → Closed testing track (beta users) → Production track.
- Enable Firebase Crashlytics in all release builds. Monitor the Crashlytics dashboard for crash-free sessions rate ≥ 99% before each track promotion.

---

## 7. iOS App Distribution (Phase 2)

*This section applies to Phase 2. No action required for Phase 1.*

### 7.1 Release Build

1. Configure the App Store distribution signing certificate and provisioning profile in Xcode.
2. Archive the release build: **Product** → **Archive** → **Distribute App** → **App Store Connect**.

### 7.2 App Store Distribution

- Upload archive via Xcode Organiser or `altool`.
- Promotion path: TestFlight beta (internal + external testers) → App Store submission.
- Complete the App Store review compliance checklist before submission. Refer to the App Store Review document in `08-end-user-documentation/`.

---

## 8. Post-Deployment Verification

Execute every step in order. Do not sign off on a deployment until all steps pass.

1. Load the web app login page in a browser. Confirm HTTPS is enforced and no mixed content warnings appear in the browser console.
2. Create a test tenant account and log in as the Business Owner role. Confirm the dashboard loads.
3. Create a test product with a price and SKU. Confirm it appears in POS product search within 3 seconds.
4. Complete a cash sale end-to-end: select product, apply quantity, confirm sale. Verify the receipt generates and the transaction appears in the sales report.
5. Trigger an SMS to a test phone number via Africa's Talking. Confirm delivery receipt appears in the Africa's Talking dashboard.
6. Reload the dashboard. Confirm all KPI widgets render and data loads within 3 seconds.
7. Navigate to the audit log. Confirm all actions performed in steps 2 through 6 are recorded with actor, timestamp, device, and IP address.
8. Run the scheduler manually and confirm it completes without error:

   ```bash
   php artisan schedule:run
   ```

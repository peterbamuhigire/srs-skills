---
title: "BIRDC ERP — Deployment Guide"
subtitle: "Prepared by Peter Bamuhigire, ICT Consultant (techguypeter.com) for PIBID/BIRDC"
date: "2026-04-05"
version: "1.0"
---

# BIRDC ERP Deployment Guide

**Document:** Deployment Guide
**Prepared by:** Peter Bamuhigire, ICT Consultant (techguypeter.com)
**Client:** PIBID / BIRDC, Nyaruzinga hill, Bushenyi District, Western Uganda
**Date:** 2026-04-05
**Version:** 1.0
**Deployment Model:** Single-tenant, on-premise at BIRDC Nyaruzinga, Bushenyi, Uganda

---

## 1. Purpose and Scope

This guide provides step-by-step procedures for deploying the BIRDC ERP system on BIRDC-owned on-premise infrastructure. It covers server provisioning, application installation, first-time configuration, Android app distribution, third-party integrations, backup setup, post-deployment verification, and go-live cutover.

All procedures assume a clean Ubuntu 22.04 LTS server environment unless otherwise noted. Commands are executed as a non-root user with `sudo` privileges. No cloud services or SaaS subscriptions are required; all BIRDC data remains on BIRDC servers at all times (Design Covenant DC-006).

---

## 2. Server Prerequisites

### 2.1 Hardware Minimum Specifications

<!-- [CONTEXT-GAP: GAP-013] BIRDC server hardware specifications (RAM, storage, CPU model, OS currently installed) are not yet confirmed. The values below are minimum recommended thresholds based on the system's known peak load: 50 concurrent web users, 6 Android apps syncing, and daily full-database backups completing within 4 hours. Confirm actual hardware with BIRDC IT before finalising this section. -->

| Component | Minimum Specification | Recommended |
|---|---|---|
| CPU | 4-core x86_64, 2.5 GHz | 8-core x86_64, 3.0 GHz |
| RAM | 16 GB | 32 GB |
| Storage (OS + application) | 100 GB SSD | 200 GB SSD |
| Storage (database + backups) | 500 GB HDD | 1 TB HDD (RAID 1 mirror) |
| Network interface | 100 Mbps LAN | 1 Gbps LAN |
| UPS / power backup | Required — minimum 2-hour runtime | Required |

The database volume must be mounted separately from the OS volume so that a full disk event on application logs cannot corrupt MySQL data files.

### 2.2 Operating System

1. Install Ubuntu 22.04 LTS (Jammy Jellyfish) — 64-bit server edition.
2. Apply all security updates immediately after installation:

```bash
sudo apt update && sudo apt upgrade -y
```

3. Set the system timezone to East Africa Time (EAT):

```bash
sudo timedatectl set-timezone Africa/Kampala
```

4. Enable the Ubuntu firewall and allow only required ports:

```bash
sudo ufw allow 22/tcp    # SSH
sudo ufw allow 80/tcp    # HTTP (redirect to HTTPS)
sudo ufw allow 443/tcp   # HTTPS
sudo ufw enable
```

### 2.3 PHP 8.3 Installation

1. Add the Ondřej Surý PPA (provides PHP 8.3 on Ubuntu 22.04):

```bash
sudo add-apt-repository ppa:ondrej/php -y
sudo apt update
```

2. Install PHP 8.3 and all required extensions:

```bash
sudo apt install -y php8.3 php8.3-cli php8.3-fpm php8.3-mysql \
  php8.3-mbstring php8.3-xml php8.3-curl php8.3-zip php8.3-gd \
  php8.3-intl php8.3-bcmath php8.3-opcache
```

3. Verify the installation:

```bash
php8.3 --version
```

Expected output: `PHP 8.3.x (cli)` or higher within the 8.3.x line.

4. Configure `php.ini` for production — edit `/etc/php/8.3/fpm/php.ini`:

| Setting | Value | Reason |
|---|---|---|
| `upload_max_filesize` | `20M` | Farmer bulk import and PhpSpreadsheet uploads |
| `post_max_size` | `25M` | Must exceed `upload_max_filesize` |
| `max_execution_time` | `120` | Payroll calculation and report generation |
| `memory_limit` | `256M` | mPDF invoice generation and PhpSpreadsheet |
| `expose_php` | `Off` | Security hardening |
| `display_errors` | `Off` | Production — log errors, do not display |
| `error_log` | `/var/log/php8.3-fpm.log` | Centralised error log |

### 2.4 MySQL 9.1 Installation

1. Download and install the MySQL APT repository configuration:

```bash
wget https://dev.mysql.com/get/mysql-apt-config_0.8.30-1_all.deb
sudo dpkg -i mysql-apt-config_0.8.30-1_all.deb
```

During the configuration prompt, select MySQL 9.1 (Innovation) from the version menu.

2. Install MySQL Server:

```bash
sudo apt update
sudo apt install -y mysql-server
```

3. Run the security hardening script:

```bash
sudo mysql_secure_installation
```

Accept all prompts: set root password, remove anonymous users, disallow remote root login, remove test database, reload privileges.

4. Configure MySQL for production — edit `/etc/mysql/mysql.conf.d/mysqld.cnf`:

| Setting | Value | Reason |
|---|---|---|
| `innodb_buffer_pool_size` | 4G (or 50% of RAM) | Optimise InnoDB for financial query performance |
| `character-set-server` | `utf8mb4` | Full Unicode support for farmer names and GL descriptions |
| `collation-server` | `utf8mb4_unicode_ci` | Case-insensitive collation consistent with application |
| `max_connections` | `200` | Supports 50 concurrent web users plus background workers |
| `slow_query_log` | `1` | Enable slow query logging for performance monitoring |
| `slow_query_log_file` | `/var/log/mysql/slow.log` | Dedicated slow query log |
| `long_query_time` | `2` | Flag queries exceeding 2 seconds |
| `bind-address` | `127.0.0.1` | Restrict MySQL to localhost — application and database on same server |

5. Restart MySQL and verify it is running:

```bash
sudo systemctl restart mysql
sudo systemctl status mysql
```

6. Create the application database and dedicated database user:

```bash
sudo mysql -u root -p
```

```sql
CREATE DATABASE birdc_erp CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER 'birdc_app'@'localhost' IDENTIFIED BY '<strong-random-password>';
GRANT SELECT, INSERT, UPDATE, DELETE, CREATE, DROP, INDEX, ALTER,
      CREATE TEMPORARY TABLES, LOCK TABLES, EXECUTE, CREATE ROUTINE,
      ALTER ROUTINE, EVENT, TRIGGER ON birdc_erp.* TO 'birdc_app'@'localhost';
FLUSH PRIVILEGES;
EXIT;
```

Record the password in the BIRDC IT password vault. Do not store it in any file other than the `.env` file (see Section 3.2).

### 2.5 Web Server Configuration (Apache / Nginx)

**Using Apache (recommended for shared-hosting familiarity):**

1. Install Apache and the PHP-FPM connector:

```bash
sudo apt install -y apache2 libapache2-mod-fcgid
sudo a2enmod proxy_fcgi setenvif rewrite headers ssl
sudo a2enconf php8.3-fpm
```

2. Create the virtual host configuration at `/etc/apache2/sites-available/birdc-erp.conf`:

```apache
<VirtualHost *:80>
    ServerName birdc.local
    Redirect permanent / https://birdc.local/
</VirtualHost>

<VirtualHost *:443>
    ServerName birdc.local
    DocumentRoot /var/www/birdc-erp/public
    SSLEngine on
    SSLCertificateFile    /etc/ssl/certs/birdc.crt
    SSLCertificateKeyFile /etc/ssl/private/birdc.key

    <Directory /var/www/birdc-erp/public>
        Options -Indexes +FollowSymLinks
        AllowOverride All
        Require all granted
    </Directory>

    # Security headers
    Header always set X-Frame-Options "SAMEORIGIN"
    Header always set X-Content-Type-Options "nosniff"
    Header always set Referrer-Policy "strict-origin-when-cross-origin"
    Header always set Strict-Transport-Security "max-age=31536000; includeSubDomains"

    ErrorLog ${APACHE_LOG_DIR}/birdc-erp-error.log
    CustomLog ${APACHE_LOG_DIR}/birdc-erp-access.log combined
</VirtualHost>
```

3. Enable the site and disable the default:

```bash
sudo a2ensite birdc-erp
sudo a2dissite 000-default
sudo systemctl reload apache2
```

### 2.6 SSL / HTTPS Setup

**Option A — Self-signed certificate (LAN-only deployment):**

```bash
sudo openssl req -x509 -nodes -days 3650 -newkey rsa:4096 \
  -keyout /etc/ssl/private/birdc.key \
  -out /etc/ssl/certs/birdc.crt \
  -subj "/C=UG/ST=Bushenyi/L=Nyaruzinga/O=BIRDC/CN=birdc.local"
```

**Option B — Let's Encrypt (if BIRDC server has a public domain name):**

```bash
sudo apt install -y certbot python3-certbot-apache
sudo certbot --apache -d <birdc-domain.example.com>
```

Let's Encrypt certificates renew automatically via a systemd timer. Verify auto-renewal:

```bash
sudo certbot renew --dry-run
```

---

## 3. Application Deployment

### 3.1 Clone from Git Repository

1. Install Git and Composer:

```bash
sudo apt install -y git
curl -sS https://getcomposer.org/installer | php
sudo mv composer.phar /usr/local/bin/composer
```

2. Clone the repository into the web root:

```bash
sudo mkdir -p /var/www/birdc-erp
sudo chown $USER:www-data /var/www/birdc-erp
git clone <repository-url> /var/www/birdc-erp
```

Replace `<repository-url>` with the authenticated GitHub URL or SSH URL provided by Peter Bamuhigire.

3. Set correct file ownership:

```bash
sudo chown -R $USER:www-data /var/www/birdc-erp
sudo chmod -R 755 /var/www/birdc-erp
sudo chmod -R 775 /var/www/birdc-erp/storage
sudo chmod -R 775 /var/www/birdc-erp/bootstrap/cache
```

### 3.2 Composer Dependencies

Install PHP dependencies (production mode — no development tools):

```bash
cd /var/www/birdc-erp
composer install --no-dev --optimize-autoloader
```

Verify no critical errors are reported. Warnings about optional extensions may be ignored if those extensions are not used.

### 3.3 Environment Configuration (.env)

1. Copy the environment template:

```bash
cp .env.example .env
```

2. Edit `.env` and populate all required values:

```
# ── Application ──────────────────────────────────────────────
APP_NAME="BIRDC ERP"
APP_ENV=production
APP_DEBUG=false
APP_URL=https://birdc.local

# ── Database ──────────────────────────────────────────────────
DB_HOST=127.0.0.1
DB_PORT=3306
DB_DATABASE=birdc_erp
DB_USERNAME=birdc_app
DB_PASSWORD=<database-password>

# ── JWT (Mobile API) ──────────────────────────────────────────
JWT_SECRET=<256-bit-random-hex>
JWT_ACCESS_TTL=15          # minutes
JWT_REFRESH_TTL=43200      # minutes (30 days)

# ── EFRIS Integration (URA) ───────────────────────────────────
EFRIS_API_URL=https://efris.ura.go.ug/efrisws/ws/taInvoice
EFRIS_TIN=<BIRDC-TIN>
EFRIS_DEVICE_NO=<BIRDC-EFRIS-device-number>
EFRIS_PRIVATE_KEY_PATH=storage/keys/efris_private.pem
EFRIS_PUBLIC_KEY_PATH=storage/keys/efris_public.pem

# ── MTN MoMo Business API ─────────────────────────────────────
MTN_MOMO_BASE_URL=https://proxy.momoapi.mtn.com
MTN_MOMO_SUBSCRIPTION_KEY=<subscription-key>
MTN_MOMO_API_USER=<api-user-uuid>
MTN_MOMO_API_KEY=<api-key>
MTN_MOMO_ENVIRONMENT=production

# ── Airtel Money API ──────────────────────────────────────────
AIRTEL_MONEY_BASE_URL=https://openapi.airtel.africa
AIRTEL_MONEY_CLIENT_ID=<client-id>
AIRTEL_MONEY_CLIENT_SECRET=<client-secret>
AIRTEL_MONEY_ENVIRONMENT=production

# ── SMTP (Email) ──────────────────────────────────────────────
MAIL_MAILER=smtp
MAIL_HOST=<smtp-host>
MAIL_PORT=587
MAIL_USERNAME=<smtp-username>
MAIL_PASSWORD=<smtp-password>
MAIL_ENCRYPTION=tls
MAIL_FROM_ADDRESS=noreply@birdc.go.ug
MAIL_FROM_NAME="BIRDC ERP"
```

3. Generate the application encryption key:

```bash
php artisan key:generate
```

4. Restrict `.env` file permissions so only the web server user can read it:

```bash
sudo chmod 640 /var/www/birdc-erp/.env
sudo chown $USER:www-data /var/www/birdc-erp/.env
```

**The `.env` file must never be committed to the Git repository.** Verify `.env` is listed in `.gitignore` before proceeding.

### 3.4 Database Migration

Run all database migrations to create the schema:

```bash
cd /var/www/birdc-erp
php artisan migrate --force
```

Verify the migration log shows no errors. Every migration must complete with `Migrated` status.

### 3.5 Initial Seed Data

Load required reference data that the system cannot function without:

```bash
php artisan db:seed --class=ChartOfAccountsSeeder
php artisan db:seed --class=SystemRolesPermissionsSeeder
php artisan db:seed --class=PayeTaxBandsSeeder
php artisan db:seed --class=NssfRatesSeeder
```

Each seeder must complete with a success confirmation. If any seeder fails, review the error output and resolve before continuing — downstream modules depend on this reference data.

**Chart of Accounts note:** If BIRDC provides their existing chart of accounts (see GAP-012 resolution), import it via the Finance Director's bulk import tool after first login instead of running the default seeder. Do not run both — duplicate accounts will cause GL posting errors.

---

## 4. First-Time Configuration

Complete these steps as the super-admin user immediately after deployment.

### 4.1 Create Super Admin User

```bash
php artisan birdc:create-admin
```

The command prompts for: full name, email address, and password. The password must be at least 16 characters and include uppercase, lowercase, digits, and a special character.

After creation, log in at `https://birdc.local/public/admin/` and enable 2-factor authentication (TOTP) for the super-admin account before any other action.

### 4.2 Configure Chart of Accounts

Navigate to **Finance > Chart of Accounts > Import** and either:

- Upload the BIRDC chart of accounts spreadsheet (if provided by Finance Director), or
- Verify the default seeded accounts cover BIRDC's operational needs.

The chart of accounts must be finalised and approved by the Finance Director before any financial transactions are posted. Incorrect account codes cannot be easily removed after transactions reference them.

### 4.3 Configure Payroll Elements

Navigate to **HR > Payroll Configuration** and configure:

1. Basic salary grades and pay scales for each staff category.
2. PAYE tax bands — pre-seeded from `PayeTaxBandsSeeder`; verify against current URA rates. [CONTEXT-GAP: GAP-008]
3. NSSF contribution rates — employer 10%, employee 5% (verify current rates with NSSF Uganda). [CONTEXT-GAP: GAP-009]
4. Local Service Tax (LST) rates per district.
5. Any applicable allowances (housing, transport, medical) and their taxability status.

### 4.4 Configure Procurement Approval Thresholds

Navigate to **Procurement > Configuration > Approval Matrix** and enter the current PPDA procurement threshold values for BIRDC/PIBID as a government entity. [CONTEXT-GAP: GAP-007]

The approval matrix defines which officer level approves each procurement tier. This configuration must be verified by the BIRDC Administration Officer before the procurement module goes live.

### 4.5 Configure Agent Territories

Navigate to **Sales > Agent Management > Territories** and:

1. Import the list of 1,071 field sales agents from the provided Excel template.
2. Assign each agent to their sales territory.
3. Set each agent's credit limit and commission rate.

Territory configuration must be approved by the Sales Manager before agent portal access is enabled.

### 4.6 Configure EFRIS API Credentials and Test Submission

1. Navigate to **Admin > Integrations > EFRIS**.
2. Enter the BIRDC TIN, EFRIS device number, and upload the EFRIS RSA private and public key files. [CONTEXT-GAP: GAP-001]
3. Set the environment to **Sandbox** for initial testing.
4. Post a test invoice from the Sales module.
5. Verify the EFRIS queue processes the submission and returns a Fiscal Document Number (FDN).
6. Confirm the FDN and QR code appear on the printed invoice.
7. After sandbox verification is complete, switch the environment to **Production** and retest with a live invoice.

---

## 5. CI/CD Pipeline Setup

### 5.1 GitHub Actions Workflow

Create `.github/workflows/deploy.yml` in the repository with the following pipeline stages:

| Stage | Trigger | Action |
|---|---|---|
| Lint | Push to any branch | PHP-CS-Fixer checks PSR-12 compliance; fails build on violation |
| Test | Push to any branch | PHPUnit — all tests must pass; minimum 80% coverage for financial services enforced |
| Staging deploy | Push to `develop` branch | Deploy to staging environment via SSH; run migration; smoke test |
| Production approval | Manual trigger in GitHub Actions UI | Requires approval from Peter Bamuhigire before production deploy proceeds |
| Production deploy | After approval | Deploy to BIRDC production server via SSH; run migration; restart PHP-FPM |

The production deploy stage must never run automatically. Manual approval is a hard gate — this is consistent with the Hybrid methodology's formal sign-off requirement per milestone.

### 5.2 Fastlane for Android Apps

Install Fastlane on the build machine (macOS or Linux CI runner):

```bash
gem install fastlane
```

Configure `Fastfile` in each Android app's root with the following lanes:

| Lane | Purpose |
|---|---|
| `test` | Run unit tests and instrumented tests |
| `beta` | Build signed APK; upload to Firebase App Distribution |
| `deploy` | Build signed AAB; upload to Google Play production track |

Store Android signing keys and service account credentials as encrypted GitHub Actions secrets. Never commit keystores or `google-services.json` to the repository.

---

## 6. Android App Distribution

### 6.1 APK Build and Signing

All 6 Android apps must be built with release signing configurations before distribution. For each app:

1. Generate a release keystore (one per app):

```bash
keytool -genkey -v -keystore birdc-<appname>-release.jks \
  -alias birdc-<appname> -keyalg RSA -keysize 4096 -validity 10000
```

2. Store keystore passwords in the BIRDC IT password vault.
3. Configure `build.gradle` (app-level) with the signing configuration referencing environment variables — never hard-coded passwords.
4. Build the release APK:

```bash
./gradlew assembleRelease
```

### 6.2 Firebase App Distribution (Beta)

1. Create a Firebase project for BIRDC ERP.
2. Add each Android app to the Firebase project.
3. Distribute beta builds to testers via Firebase App Distribution before each phase gate.
4. Testers must install the Firebase App Tester app on their Android devices to receive builds.

### 6.3 Google Play Production Release

After each phase gate sign-off, publish the production build to Google Play:

1. Build the signed Android App Bundle (AAB):

```bash
./gradlew bundleRelease
```

2. Upload the AAB to Google Play Console under the production track.
3. Complete the Google Play Store listing: description, screenshots, privacy policy URL.
4. Submit for review. Allow 3–7 business days for initial review.

### 6.4 MDM Deployment to Company-Owned Devices

For BIRDC-owned Android devices (warehouse staff, factory floor, field officers):

1. Enrol devices in a Mobile Device Management (MDM) system. Recommended: **VMware Workspace ONE** or **Microsoft Intune** (both support Android Enterprise).
2. Push app installation silently to enrolled devices without requiring users to visit the Play Store.
3. Configure MDM policy: disable sideloading of unauthorized apps; enforce screen lock PIN; enable remote wipe.
4. Verify each device receives the app update within 24 hours of a new MDM push.

---

## 7. ZKTeco Biometric Device Integration

<!-- [CONTEXT-GAP: GAP-005] ZKTeco device model numbers deployed at BIRDC and their API/SDK version are not yet confirmed. The procedure below covers the standard ZKTeco push SDK integration pattern. Confirm device models with BIRDC IT before finalising this section. -->

### 7.1 Device Network Configuration

1. Connect each ZKTeco device to the BIRDC LAN.
2. Assign a static IP address to each device (coordinate with BIRDC IT for the IP range).
3. Configure the device's server address to point to the BIRDC ERP server IP and port.
4. Ensure the BIRDC firewall allows traffic between the ZKTeco device IPs and the ERP server on the configured port (default: TCP 4370).

### 7.2 API Connection Test

From the ERP server, test connectivity to each device:

```bash
ping <zkteco-device-ip>
telnet <zkteco-device-ip> 4370
```

Both commands must succeed. If `telnet` fails, verify the firewall rule and the device's network settings.

### 7.3 Initial Data Sync

1. Navigate to **Admin > Integrations > Biometric Devices**.
2. Add each device with its IP address, port, and device serial number.
3. Click **Test Connection** — the system must return a successful handshake.
4. Click **Sync Employees** — the system pushes enrolled employee fingerprint templates to the device.
5. Navigate to **HR > Attendance > Import** and run an initial pull to confirm attendance records flow from device to ERP.

---

## 8. Backup Configuration

### 8.1 Automated Daily mysqldump

Create the backup script at `/usr/local/bin/birdc-backup.sh`:

```bash
#!/usr/bin/env bash
set -euo pipefail

BACKUP_DIR="/backups/birdc-erp"
DATE=$(date +%Y-%m-%d)
BACKUP_FILE="$BACKUP_DIR/birdc_erp_$DATE.sql.gz"

mkdir -p "$BACKUP_DIR"

mysqldump -u birdc_app -p"$MYSQL_BACKUP_PASSWORD" \
  --single-transaction --routines --triggers --events \
  birdc_erp | gzip > "$BACKUP_FILE"

echo "Backup completed: $BACKUP_FILE"
```

Store `MYSQL_BACKUP_PASSWORD` in `/etc/environment` (restricted to root read) — never hard-code in the script.

Make the script executable:

```bash
sudo chmod 750 /usr/local/bin/birdc-backup.sh
```

### 8.2 Cron Schedule

Add to the root crontab (`sudo crontab -e`):

```
# BIRDC ERP daily backup — 02:00 EAT every night
0 2 * * * /usr/local/bin/birdc-backup.sh >> /var/log/birdc-backup.log 2>&1
```

Verify the cron job runs successfully on the next scheduled execution by checking `/var/log/birdc-backup.log`.

### 8.3 Offsite Backup

**USB drive (weekly):**

1. Label a USB drive "BIRDC ERP Backup — Week [n]".
2. Every Monday, copy the previous week's backup files to the USB drive.
3. Store the USB drive in the Finance Director's locked cabinet — not in the server room.

**Encrypted remote copy (daily):**

Install `rclone` and configure an encrypted remote (compatible with any S3-compatible storage, SFTP, or Google Drive):

```bash
sudo apt install -y rclone
rclone config
```

Add to the backup script:

```bash
rclone copy "$BACKUP_FILE" birdc-remote:backups/
```

### 8.4 Backup Restore Test Procedure

The restore procedure must be tested monthly (see Runbook Section 14.3). The test confirms:

1. The compressed backup file is not corrupted (verify CRC with `gzip -t`).
2. The backup restores successfully to a test database.
3. A spot-check query returns the expected record count.
4. The restore completes within the 4-hour system uptime requirement.

---

## 9. Post-Deployment Verification Checklist

Run this checklist in order immediately after deployment. All items must pass before informing BIRDC staff that the system is ready.

| # | Verification Item | Expected Result | Pass/Fail |
|---|---|---|---|
| 1 | Log in to the main ERP at `https://birdc.local/public/` | Login succeeds; dashboard loads | — |
| 2 | Log in to the Sales Agent Portal at `/public/sales-agents/` | Login succeeds | — |
| 3 | Log in to the Admin Panel at `/public/admin/` | Login succeeds; 2FA prompt shown for Director-level roles | — |
| 4 | POS — process a test sale | Sale posts; receipt generates; inventory decrements; EFRIS submission queued | — |
| 5 | EFRIS — submit test invoice | FDN returned within 30 seconds; QR code stored against transaction | — |
| 6 | Agent remittance FIFO allocation | Post a test remittance payment; system allocates to oldest outstanding invoice first via `sp_apply_remittance_to_invoices`; agent cash balance updates in real time | — |
| 7 | Payroll test run | Create a test payroll for 1 employee; PAYE and NSSF calculated correctly; payslip PDF generated | — |
| 8 | GL hash chain integrity check | Navigate to **Finance > Audit > Hash Chain Integrity**; all posted transactions return hash chain VALID status | — |
| 9 | Android app sync | Install Sales Agent App on a test device; post a test offline POS sale; reconnect to Wi-Fi; verify transaction syncs to server within 60 seconds | — |
| 10 | Email alert | Trigger a test EFRIS failure (disconnect EFRIS API URL); verify Finance Manager receives email alert after 3 retry failures | — |

Any failed item blocks go-live. Resolve the root cause and re-run the affected checklist items before proceeding.

---

## 10. Go-Live Cutover Plan

### 10.1 Data Migration from Legacy System

<!-- [CONTEXT-GAP: GAP-014] BIRDC's existing accounting software (if any) has not been identified. Data migration requirements — account balances, outstanding invoices, farmer records, employee records — cannot be specified until the legacy system is confirmed. The steps below are a framework; specific field mapping must be completed once GAP-014 is resolved. -->

1. Export all data from the legacy system in CSV or Excel format (coordinate with Finance Director).
2. Map legacy account codes to the BIRDC ERP chart of accounts.
3. Import opening account balances via **Finance > Journal Entry > Opening Balances**.
4. Import farmer records via **Cooperative > Farmers > Bulk Import**.
5. Import employee records via **HR > Employees > Bulk Import**.
6. Import outstanding agent invoices and cash balances via **Sales > Agent Management > Import Opening Balances**.
7. Reconcile imported totals against the legacy system's closing trial balance — the Finance Director must sign off on the reconciliation before go-live proceeds.

### 10.2 Parallel Run Period

Run the legacy system and BIRDC ERP in parallel for a minimum of 2 weeks:

- All transactions are entered in both systems.
- Finance Director compares trial balances from both systems at the end of each week.
- Any discrepancy of UGX 1,000 or greater triggers an investigation before cutover.

### 10.3 Cutover Date

1. The cutover date is agreed by: Peter Bamuhigire, Finance Director, and BIRDC Director.
2. Cutover must not fall on: month-end, payroll processing week, or during an active procurement cycle.
3. Announce the cutover date to all staff 5 business days in advance.
4. Schedule cutover for a Friday evening to allow the weekend for issue resolution before the Monday working week.

### 10.4 Rollback Plan

If a critical defect is discovered within 48 hours of cutover:

1. Peter Bamuhigire declares a rollback to Finance Director.
2. Revert to the legacy system for all transactions.
3. Take a full database dump of the BIRDC ERP database before rollback to preserve the data state for investigation.
4. Investigate and fix the defect.
5. Re-enter any transactions that occurred in BIRDC ERP (not in the legacy system) after the cutover point.
6. Schedule a new cutover date after a second parallel run confirms the fix.

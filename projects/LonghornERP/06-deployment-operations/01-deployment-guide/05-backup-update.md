# Backup, Update, and Security Hardening for Longhorn ERP

## Automated Backup Procedure

### Cron Schedule

Create the file `/etc/cron.d/longhorn-backup` with the following content to trigger a daily backup at 02:00:

```bash
# /etc/cron.d/longhorn-backup — daily backup at 02:00 server time
0 2 * * * root /var/www/longhorn/scripts/backup.sh >> /var/log/longhorn-backup.log 2>&1
```

### Backup Script Requirements

The `backup.sh` script must perform all of the following actions on every run:

- Dump all application databases using `mysqldump` with `--single-transaction` to avoid table locks during the backup window.
- Compress the dump using `gzip` or `zstd` before transfer.
- Copy the compressed archive to offsite storage — either Amazon S3 (`aws s3 cp`) or a remote SFTP target.
- Retain 30 daily backups and 12 monthly backups; prune older archives automatically.
- Send an alert email to the system administrator on any failure (non-zero exit code).

### Verifying Backup Integrity

Test restore fidelity monthly. On a staging server, restore the most recent backup and verify the application starts and data is intact. A backup that has never been tested is not a backup — it is an assumption.

## Update Procedure (Zero-Downtime Rolling Update)

Execute updates during a low-traffic window. Complete all steps in sequence.

1. Enable maintenance mode to queue or reject incoming requests gracefully:

   ```bash
   touch /var/www/longhorn/storage/maintenance.flag
   ```

2. Pull the latest code from the main branch:

   ```bash
   git -C /var/www/longhorn pull origin main
   ```

3. Install updated PHP dependencies:

   ```bash
   cd /var/www/longhorn && composer install --no-dev --optimize-autoloader
   ```

4. Run any pending database migrations:

   ```bash
   php /var/www/longhorn/run_migrations.php
   ```

   Review the migration output. If a migration fails, halt and roll back using the `run_migrations.php --rollback` flag before disabling maintenance mode.

5. Clear application caches:

   ```bash
   php /var/www/longhorn/artisan cache:clear
   ```

6. Disable maintenance mode:

   ```bash
   rm /var/www/longhorn/storage/maintenance.flag
   ```

7. Run a smoke test to confirm the update was successful:

   - Verify that the login page loads without errors.
   - Create a test invoice and confirm the General Ledger entry is generated.
   - Check `/var/www/longhorn/logs/apache-error.log` for new error entries.

## Security Hardening Checklist

Apply all items in this checklist at initial deployment and re-verify after each major update.

### TLS and Transport Security

- Restrict Apache to TLS 1.3 only. In the virtual host or `ssl.conf`, set:

  ```apache
  SSLProtocol -all +TLSv1.3
  SSLCipherSuite TLS_AES_256_GCM_SHA384:TLS_CHACHA20_POLY1305_SHA256
  ```

  TLS 1.0 and TLS 1.1 must be disabled; they are deprecated by RFC 8996.

### Apache Hardening

- Disable server version disclosure. In `/etc/apache2/conf-enabled/security.conf`:

  ```apache
  ServerSignature Off
  ServerTokens Prod
  ```

- Add the following security headers to the virtual host (already included in the Section 3 virtual host template):

  ```apache
  Header always set X-Frame-Options "DENY"
  Header always set X-Content-Type-Options "nosniff"
  Header always set Strict-Transport-Security "max-age=31536000; includeSubDomains"
  ```

- Block direct access to `.env`:

  ```apache
  <Files ".env">
      Require all denied
  </Files>
  ```

  Add this block inside the `<VirtualHost>` section or the application's `.htaccess`.

### File System Security

- Set strict permissions on the environment file:

  ```bash
  chmod 640 /var/www/longhorn/.env
  chown root:www-data /var/www/longhorn/.env
  ```

- Confirm `storage/` and `logs/` are outside the document root (`/var/www/longhorn/public/`). These directories must never be web-accessible.

### MySQL Hardening

- Bind MySQL to localhost only. In `my.cnf` under `[mysqld]`:

  ```ini
  bind-address = 127.0.0.1
  ```

- Remove all anonymous user accounts:

  ```sql
  DELETE FROM mysql.user WHERE User='';
  FLUSH PRIVILEGES;
  ```

- Disable remote root login:

  ```sql
  UPDATE mysql.user SET Host='localhost' WHERE User='root';
  FLUSH PRIVILEGES;
  ```

### Brute-Force Protection

- Install and enable `fail2ban` for SSH and Apache:

  ```bash
  apt install -y fail2ban
  systemctl enable fail2ban
  systemctl start fail2ban
  ```

  Configure `/etc/fail2ban/jail.local` with jails for `sshd` and `apache-auth`. Set `maxretry = 5` and `bantime = 3600`.

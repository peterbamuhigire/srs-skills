# Configuration Reference for Longhorn ERP

## Environment Variables (`.env`)

The `.env` file in the application root controls all runtime configuration. Copy `.env.example` to `.env` and populate every variable before running migrations. Never commit `.env` to version control.

### Application Settings

| Variable | Description | Example Value |
|---|---|---|
| `APP_ENV` | Runtime environment | `production` |
| `APP_URL` | Full public URL including scheme | `https://yourdomain.com` |
| `APP_KEY` | 32-character random application key | `base64:abc123...` |

### Database Settings

| Variable | Description | Example Value |
|---|---|---|
| `DB_HOST` | MySQL host | `127.0.0.1` |
| `DB_PORT` | MySQL port | `3306` |
| `DB_NAME` | Database name | `longhorn_erp` |
| `DB_USER` | Database user | `longhorn` |
| `DB_PASS` | Database password | *(strong generated value)* |

### Session and Authentication Settings

| Variable | Description | Example Value |
|---|---|---|
| `SESSION_LIFETIME` | Session idle timeout in minutes | `120` |
| `SESSION_SECURE` | Restrict session cookie to HTTPS | `true` |
| `JWT_SECRET` | Secret key for JWT token signing | *(64-character random value)* |
| `JWT_EXPIRY_MINUTES` | Access token lifetime in minutes | `60` |
| `REFRESH_TOKEN_EXPIRY_DAYS` | Refresh token lifetime in days | `30` |

### Mail Settings

| Variable | Description | Example Value |
|---|---|---|
| `MAIL_HOST` | SMTP server hostname | `smtp.mailgun.org` |
| `MAIL_PORT` | SMTP port | `587` |
| `MAIL_USER` | SMTP authentication username | `postmaster@yourdomain.com` |
| `MAIL_PASS` | SMTP authentication password | *(credential)* |
| `MAIL_FROM` | Sender address displayed to recipients | `noreply@yourdomain.com` |

### Integration Settings

| Variable | Description | Example Value |
|---|---|---|
| `EFRIS_API_URL` | Uganda Revenue Authority EFRIS endpoint | `https://efris.ura.go.ug/api/v1` |
| `EFRIS_API_KEY` | EFRIS authentication key | *(issued by URA)* |
| `MTN_MOMO_BASE_URL` | MTN Mobile Money API base URL | `https://sandbox.momodeveloper.mtn.com` |
| `MTN_MOMO_API_KEY` | MTN MoMo API key | *(issued by MTN)* |
| `AFRICASTALKING_API_KEY` | Africa's Talking SMS API key | *(issued by Africa's Talking)* |
| `AFRICASTALKING_SENDER_ID` | Registered SMS sender ID | `LONGHORN` |

## Apache Virtual Host Configuration

Save the following block to `/etc/apache2/sites-available/longhorn.conf`. Replace `yourdomain.com` with the actual domain name.

```apache
<VirtualHost *:443>
    ServerName yourdomain.com
    DocumentRoot /var/www/longhorn/public

    SSLEngine on
    SSLCertificateFile /etc/letsencrypt/live/yourdomain.com/fullchain.pem
    SSLCertificateKeyFile /etc/letsencrypt/live/yourdomain.com/privkey.pem

    <Directory /var/www/longhorn/public>
        AllowOverride All
        Require all granted
    </Directory>

    Header always set X-Frame-Options "DENY"
    Header always set X-Content-Type-Options "nosniff"
    Header always set Strict-Transport-Security "max-age=31536000; includeSubDomains"

    ErrorLog /var/www/longhorn/logs/apache-error.log
    CustomLog /var/www/longhorn/logs/apache-access.log combined
</VirtualHost>

<VirtualHost *:80>
    ServerName yourdomain.com
    Redirect permanent / https://yourdomain.com/
</VirtualHost>
```

Enable the site and reload Apache after saving:

```bash
a2ensite longhorn.conf
systemctl reload apache2
```

## PHP Configuration (`php.ini`)

Locate the active `php.ini` with `php --ini`. Apply the following settings in the `[PHP]` and `[Session]` sections.

| Setting | Recommended Value | Reason |
|---|---|---|
| `memory_limit` | `256M` | Supports PDF generation and large data imports |
| `upload_max_filesize` | `50M` | Allows document and spreadsheet attachments |
| `post_max_size` | `52M` | Must exceed `upload_max_filesize` to handle form data with uploads |
| `max_execution_time` | `300` | Allows payroll runs and bulk operations to complete |
| `session.cookie_secure` | `1` | Restricts session cookies to HTTPS connections |
| `session.cookie_httponly` | `1` | Prevents JavaScript access to session cookies (XSS protection) |
| `display_errors` | `Off` | Prevents error details from leaking to end users in production |

Restart Apache after editing `php.ini`:

```bash
systemctl restart apache2
```

## MySQL Configuration (`my.cnf`)

Edit `/etc/mysql/my.cnf` (or the applicable included file under `/etc/mysql/mysql.conf.d/`). Apply the following settings under the `[mysqld]` section.

| Setting | Recommended Value | Notes |
|---|---|---|
| `innodb_buffer_pool_size` | 70% of total RAM | Primary performance lever for InnoDB; e.g., `5600M` on an 8 GB server |
| `innodb_log_file_size` | `256M` | Reduces I/O pressure during high-write periods |
| `max_connections` | `200` | Scale up for Enterprise tier; monitor `Threads_connected` |
| `character-set-server` | `utf8mb4` | Required for full Unicode support including emoji and extended scripts |
| `collation-server` | `utf8mb4_unicode_ci` | Case-insensitive, accent-sensitive Unicode collation |
| `bind-address` | `127.0.0.1` | Blocks all external TCP connections to MySQL |

Restart MySQL after editing:

```bash
systemctl restart mysql
```

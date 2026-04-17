# Installation Procedure for Longhorn ERP

Complete all steps in sequence. Do not skip steps — each step is a prerequisite for the next. Execute all commands as `root` or via `sudo` unless the step specifies otherwise.

## Pre-Installation Checklist

Confirm all of the following before proceeding:

- DNS A record for your domain points to the server IP (allow up to 15 minutes for propagation).
- Server meets the hardware and software requirements in Section 1.
- You have SSH access to the server.
- A valid domain name is available for TLS certificate issuance.

## Installation Steps

1. Update the package index and install all required OS packages:

   ```bash
   apt update && apt install -y \
     php8.3 \
     php8.3-pdo \
     php8.3-mysql \
     php8.3-mbstring \
     php8.3-openssl \
     php8.3-xml \
     php8.3-zip \
     php8.3-gd \
     php8.3-intl \
     php8.3-curl \
     apache2 \
     mysql-server-9.1 \
     certbot \
     python3-certbot-apache \
     unzip \
     git
   ```

2. Secure the MySQL installation. Run the security script and follow all prompts:

   ```bash
   mysql_secure_installation
   ```

   When prompted: remove anonymous users, disable remote root login, remove the test database, and reload privilege tables.

3. Clone the Longhorn ERP application to the document root parent:

   ```bash
   git clone https://github.com/chwezi/longhorn-erp.git /var/www/longhorn
   ```

4. Install PHP dependencies using Composer. Run this from the application root:

   ```bash
   cd /var/www/longhorn && composer install --no-dev --optimize-autoloader
   ```

5. Set file ownership and permissions:

   ```bash
   chown -R www-data:www-data /var/www/longhorn
   chmod -R 755 /var/www/longhorn
   chmod -R 775 /var/www/longhorn/storage
   chmod -R 775 /var/www/longhorn/logs
   ```

6. Copy the environment configuration template and open it for editing:

   ```bash
   cp /var/www/longhorn/.env.example /var/www/longhorn/.env
   nano /var/www/longhorn/.env
   ```

   Populate all required variables as described in Section 3. Do not commit `.env` to version control.

7. Run database migrations to create all required tables and seed initial data:

   ```bash
   php /var/www/longhorn/run_migrations.php
   ```

   Confirm the output shows no errors before proceeding.

8. Create and enable the Apache virtual host configuration. See Section 3 for the full virtual host block. Save the file to `/etc/apache2/sites-available/longhorn.conf`, then run:

   ```bash
   a2enmod rewrite ssl headers
   a2ensite longhorn.conf
   apache2ctl configtest
   systemctl reload apache2
   ```

   Confirm `configtest` reports `Syntax OK` before reloading Apache.

9. Obtain and install the TLS certificate via Let's Encrypt:

   ```bash
   certbot --apache -d yourdomain.com
   ```

   Certbot will automatically update the virtual host configuration with the certificate paths and set up auto-renewal.

10. Verify the installation by navigating to the Super Admin panel in a browser:

    ```
    https://yourdomain.com/superadmin
    ```

    A login screen confirms a successful installation. Proceed to Section 4 (First Run) to complete initial configuration.

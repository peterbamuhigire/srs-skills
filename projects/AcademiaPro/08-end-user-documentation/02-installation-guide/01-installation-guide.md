# AcademiaPro Installation Guide

**Product:** AcademiaPro — Multi-Tenant SaaS School Management Platform
**Version:** 1.0.0
**Date:** 2026-04-03
**Audience:** Developers, system administrators
**Standard:** ISO 26514
**Maintainer:** Chwezi Core Systems (chwezicore.com)

---

## 1 System Requirements

### 1.1 Development Environment

| Resource | Minimum | Recommended |
|----------|---------|-------------|
| CPU | 4 cores | 8 cores |
| RAM | 8 GB | 16 GB |
| Disk | 20 GB free | 50 GB SSD |
| OS | Windows 10 + WSL2, macOS 12, Ubuntu 20.04 | Windows 11 + WSL2, macOS 14, Ubuntu 22.04 |
| Network | Broadband internet | Broadband internet |

### 1.2 Production Environment

| Resource | Minimum | Recommended |
|----------|---------|-------------|
| CPU | 4 vCPUs | 8 vCPUs |
| RAM | 8 GB | 16 GB |
| Disk | 40 GB SSD | 100 GB NVMe SSD |
| OS | Ubuntu 22.04 LTS | Ubuntu 22.04 LTS |
| Network | 100 Mbps with static IP | 1 Gbps with static IP |

## 2 Prerequisites

Install the following before proceeding. Version numbers are the minimum supported.

- **PHP 8.2+** with extensions: `mbstring`, `xml`, `curl`, `zip`, `gd`, `mysql`, `redis`, `bcmath`, `intl`
- **Composer 2.x**
- **Node.js 18+** and **npm 9+**
- **MySQL 8.x** (InnoDB, strict mode, `utf8mb4` charset)
- **Redis 7.x**
- **Meilisearch 1.x**
- **Git 2.x**
- **Docker 24+** and **Docker Compose 2.x** (production only)

### 2.1 Verify Prerequisites

Run each command and confirm the output meets the minimum version listed above.

```bash
php -v                    # PHP 8.2.x or higher
composer --version        # Composer version 2.x.x
node -v                   # v18.x.x or higher
mysql --version           # mysql Ver 8.x.x
redis-server --version    # Redis server v=7.x.x
meilisearch --version     # meilisearch 1.x.x
git --version             # git version 2.x.x
```

## 3 Development Installation

1. Clone the repository and install dependencies:

   ```bash
   git clone git@github.com:chwezi/academiapro.git
   cd academiapro
   composer install
   npm install
   ```

2. Copy the environment template:

   ```bash
   cp .env.example .env
   ```

3. Open `.env` and set the following values at minimum:

   ```dotenv
   APP_NAME=AcademiaPro
   APP_ENV=local
   APP_DEBUG=true
   APP_URL=http://localhost:8000

   DB_CONNECTION=mysql
   DB_HOST=127.0.0.1
   DB_PORT=3306
   DB_DATABASE=academiapro
   DB_USERNAME=root
   DB_PASSWORD=your_password

   CACHE_DRIVER=redis
   QUEUE_CONNECTION=redis
   SESSION_DRIVER=redis

   REDIS_HOST=127.0.0.1
   REDIS_PORT=6379

   SCOUT_DRIVER=meilisearch
   MEILISEARCH_HOST=http://127.0.0.1:7700
   MEILISEARCH_KEY=your_master_key
   ```

4. Generate the application key, create the database, run migrations, and seed:

   ```bash
   php artisan key:generate
   mysql -u root -p -e "CREATE DATABASE academiapro CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;"
   php artisan migrate
   php artisan db:seed
   ```

   Expected: `Application key set successfully.`, migrations run without errors, `Database seeding completed successfully.`

5. Start Meilisearch (in a separate terminal) and import search indexes:

   ```bash
   meilisearch --master-key="your_master_key"
   ```

   Then in the project terminal:

   ```bash
   php artisan scout:import "App\Models\Student"
   php artisan scout:import "App\Models\Staff"
   ```

   Expected: `Imported [App\Models\Student]` and `Imported [App\Models\Staff]`.

6. Start the development servers (each in a separate terminal):

   ```bash
   php artisan serve          # Backend — http://127.0.0.1:8000
   npm run dev                # Vite frontend — http://localhost:5173
   php artisan horizon        # Queue worker dashboard
   ```

   Expected: Laravel serves on port 8000, Vite reports ready, Horizon starts successfully.

## 4 Production Deployment

1. Update packages, install Docker, and verify:

   ```bash
   sudo apt update && sudo apt upgrade -y
   sudo apt install -y docker.io docker-compose-plugin
   sudo usermod -aG docker $USER
   docker --version            # Docker version 24.x
   docker compose version      # Docker Compose version v2.x
   ```

2. Clone the repository and configure the environment:

   ```bash
   git clone git@github.com:chwezi/academiapro.git /var/www/academiapro
   cd /var/www/academiapro
   cp .env.example .env
   ```

3. Edit `.env` with production values:

   ```dotenv
   APP_ENV=production
   APP_DEBUG=false
   APP_URL=https://app.academiapro.com

   DB_HOST=db
   DB_DATABASE=academiapro
   DB_USERNAME=academiapro_user
   DB_PASSWORD=<strong-generated-password>

   CACHE_DRIVER=redis
   QUEUE_CONNECTION=redis
   REDIS_HOST=redis

   SCOUT_DRIVER=meilisearch
   MEILISEARCH_HOST=http://meilisearch:7700
   MEILISEARCH_KEY=<generated-master-key>

   AWS_ACCESS_KEY_ID=<your-key>
   AWS_SECRET_ACCESS_KEY=<your-secret>
   AWS_DEFAULT_REGION=eu-west-1
   AWS_BUCKET=academiapro-storage
   AWS_URL=https://cdn.academiapro.com

   FILESYSTEM_DISK=s3
   ```

4. Start all containers, run migrations, and seed:

   ```bash
   docker compose up -d
   docker compose ps                                                          # all services show Up
   docker compose exec app php artisan migrate --force
   docker compose exec app php artisan db:seed --class=ProductionSeeder --force
   ```

5. The Docker setup includes Nginx. Verify the configuration serves the application:

    ```nginx
    server {
        listen 80;
        server_name app.academiapro.com;
        return 301 https://$host$request_uri;
    }

    server {
        listen 443 ssl http2;
        server_name app.academiapro.com;

        ssl_certificate /etc/letsencrypt/live/app.academiapro.com/fullchain.pem;
        ssl_certificate_key /etc/letsencrypt/live/app.academiapro.com/privkey.pem;

        root /var/www/html/public;
        index index.php;

        location / {
            try_files $uri $uri/ /index.php?$query_string;
        }

        location ~ \.php$ {
            fastcgi_pass app:9000;
            fastcgi_param SCRIPT_FILENAME $realpath_root$fastcgi_script_name;
            include fastcgi_params;
        }
    }
    ```

6. Obtain an SSL certificate and configure auto-renewal:

   ```bash
   sudo apt install -y certbot
   sudo certbot certonly --standalone -d app.academiapro.com
   echo "0 3 * * * certbot renew --quiet" | sudo tee -a /etc/crontab
   ```

   Expected: certificate saved at `/etc/letsencrypt/live/app.academiapro.com/fullchain.pem`.

7. Verify Horizon and configure the scheduler cron:

   ```bash
   docker compose exec app php artisan horizon:status    # Horizon is running.
   echo "* * * * * cd /var/www/html && php artisan schedule:run >> /dev/null 2>&1" | crontab -
   ```

8. Build frontend assets and warm caches:

   ```bash
   docker compose exec app npm run build
   docker compose exec app php artisan config:cache
   docker compose exec app php artisan route:cache
   docker compose exec app php artisan view:cache
   ```

   Expected: Vite builds for production; each cache command outputs `... cached successfully!`

## 5 Configuration Reference

### 5.1 Required Environment Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `APP_KEY` | Laravel encryption key (auto-generated) | `base64:...` |
| `APP_URL` | Application base URL | `https://app.academiapro.com` |
| `DB_HOST` | MySQL hostname | `127.0.0.1` |
| `DB_PORT` | MySQL port | `3306` |
| `DB_DATABASE` | Database name | `academiapro` |
| `DB_USERNAME` | Database user | `academiapro_user` |
| `DB_PASSWORD` | Database password | (secret) |
| `REDIS_HOST` | Redis hostname | `127.0.0.1` |
| `REDIS_PORT` | Redis port | `6379` |
| `MEILISEARCH_HOST` | Meilisearch URL | `http://127.0.0.1:7700` |
| `MEILISEARCH_KEY` | Meilisearch master key | (secret) |

### 5.2 Storage and CDN (Production)

| Variable | Description | Example |
|----------|-------------|---------|
| `AWS_ACCESS_KEY_ID` | AWS IAM access key | (secret) |
| `AWS_SECRET_ACCESS_KEY` | AWS IAM secret key | (secret) |
| `AWS_DEFAULT_REGION` | AWS region | `eu-west-1` |
| `AWS_BUCKET` | S3 bucket name | `academiapro-storage` |
| `AWS_URL` | CloudFront CDN URL | `https://cdn.academiapro.com` |
| `FILESYSTEM_DISK` | Storage driver | `s3` |

### 5.3 Communications (Optional)

| Variable | Description | Example |
|----------|-------------|---------|
| `AFRICASTALKING_USERNAME` | Africa's Talking username | `academiapro` |
| `AFRICASTALKING_API_KEY` | Africa's Talking API key | (secret) |
| `AFRICASTALKING_SENDER_ID` | SMS sender ID | `AcadPro` |
| `MAIL_MAILER` | Mail driver | `mailgun` |
| `MAIL_HOST` | SMTP host | `smtp.mailgun.org` |
| `MAIL_PORT` | SMTP port | `587` |
| `MAIL_USERNAME` | SMTP username | (secret) |
| `MAIL_PASSWORD` | SMTP password | (secret) |
| `MAIL_FROM_ADDRESS` | Sender email | `noreply@academiapro.com` |

### 5.4 Payments (Optional)

| Variable | Description | Example |
|----------|-------------|---------|
| `SCHOOLPAY_API_URL` | SchoolPay API endpoint | `https://api.schoolpay.co.ug` |
| `SCHOOLPAY_API_KEY` | SchoolPay API key | (secret) |
| `SCHOOLPAY_SECRET` | SchoolPay webhook secret | (secret) |

## 6 Post-Installation Verification

Run these checks after completing installation (development or production).

1. Verify Laravel version:

   ```bash
   php artisan --version
   ```

   Expected: `Laravel Framework 11.x.x`.

2. Check the health endpoint (adjust host/port for production):

   ```bash
   curl -s http://localhost:8000/api/health | python3 -m json.tool
   ```

   Expected: `{"status":"ok","database":"connected","redis":"connected","meilisearch":"connected"}`.

3. Test super-admin login:

   ```bash
   curl -s -X POST http://localhost:8000/api/auth/login \
     -H "Content-Type: application/json" \
     -d '{"email":"admin@academiapro.com","password":"<seeded-password>"}'
   ```

   Expected: JSON response containing `"token"` and `"user"` fields.

4. Verify Horizon and Meilisearch:

   ```bash
   php artisan horizon:status                  # Horizon is running.
   curl -s http://127.0.0.1:7700/health        # {"status":"available"}
   ```

## 7 Upgrading

Follow these steps in order when deploying a new version.

1. Pull, install, migrate, build, and clear caches:

   ```bash
   git pull origin main
   composer install --no-dev --optimize-autoloader
   npm ci
   php artisan migrate --force
   npm run build
   php artisan config:cache
   php artisan route:cache
   php artisan view:cache
   php artisan event:cache
   ```

2. Restart Horizon to pick up new job classes:

   ```bash
   php artisan horizon:terminate
   php artisan horizon:status    # Horizon is running.
   ```

   Horizon's supervisor process restarts it automatically.

## 8 Common Issues and Solutions

### 8.1 Permission Errors on `storage/` or `bootstrap/cache/`

**Symptom:** `Permission denied` errors when writing logs, cache, or compiled views.

**Solution:**

```bash
sudo chown -R www-data:www-data storage bootstrap/cache
sudo chmod -R 775 storage bootstrap/cache
```

### 8.2 MySQL Strict Mode Errors

**Symptom:** `SQLSTATE[42000]: Syntax error or access violation: 1055 ... is not in GROUP BY`.

**Solution:** Ensure MySQL is running in strict mode. In `my.cnf`:

```ini
[mysqld]
sql_mode=STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION
```

Restart MySQL after changes:

```bash
sudo systemctl restart mysql
```

### 8.3 Redis Connection Refused

**Symptom:** `Connection refused [tcp://127.0.0.1:6379]`.

**Solution:**

```bash
sudo systemctl start redis-server
sudo systemctl enable redis-server
redis-cli ping
```

Expected: `PONG`.

### 8.4 Meilisearch Not Indexing

**Symptom:** Search returns empty results despite seeded data.

**Solution:**

1. Verify Meilisearch is running:

   ```bash
   curl -s http://127.0.0.1:7700/health
   ```

2. Check that `MEILISEARCH_KEY` in `.env` matches the `--master-key` used at startup.

3. Flush and reimport indexes:

   ```bash
   php artisan scout:flush "App\Models\Student"
   php artisan scout:import "App\Models\Student"
   ```

### 8.5 Port Conflicts

**Symptom:** `Address already in use` when starting a service.

**Solution:** Identify and terminate the process occupying the port.

```bash
sudo lsof -i :8000
sudo kill -9 <PID>
```

Common port assignments:

- `8000` — Laravel dev server
- `5173` — Vite dev server
- `3306` — MySQL
- `6379` — Redis
- `7700` — Meilisearch

### 8.6 Docker Compose Fails to Start

**Symptom:** Containers exit immediately or fail health checks.

**Solution:**

1. Check logs for the failing container:

   ```bash
   docker compose logs <service-name>
   ```

2. Verify `.env` file exists and contains valid values.

3. Ensure no host services conflict with container ports:

   ```bash
   docker compose down
   sudo systemctl stop mysql redis-server
   docker compose up -d
   ```

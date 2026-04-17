# 3. Deployment Architecture

## 3.1 Deployment Model

The BIRDC ERP is deployed on-premise at BIRDC Nyaruzinga, Bushenyi District, Western Uganda. No component is hosted in a cloud environment (Design Covenant DC-006: Data Sovereignty). BIRDC owns all hardware and all data resides within BIRDC's physical premises.

## 3.2 Server Configuration (Recommended Minimum)

[CONTEXT-GAP: GAP-013] — Exact server hardware specifications at BIRDC Nyaruzinga are pending confirmation from BIRDC IT. The specifications below are recommended minimums for the anticipated load (140 MT/day peak production, 1,071 concurrent agent sessions, 150+ internal users).

| Component | Recommended Minimum Specification |
|---|---|
| Application server CPU | 8-core x86-64, 3.0 GHz+ |
| Application server RAM | 32 GB ECC RAM |
| Primary storage | 1 TB SSD (OS + application) |
| Database storage | 2 TB SSD RAID-1 (MySQL data + binary logs) |
| Backup storage | 4 TB HDD (on-premise backup rotation) |
| Network interface | 1 Gbps LAN; internet uplink ≥ 10 Mbps for EFRIS, mobile money APIs, and GitHub Actions CI/CD |
| UPS | Online UPS with ≥ 30-minute runtime at full load |
| Operating system | Ubuntu Server 22.04 LTS or CentOS Stream 9 |

## 3.3 Web Server

- **Primary web server:** Nginx (recommended) or Apache 2.4+
- **PHP-FPM** processes PHP 8.3 application requests via FastCGI
- **HTTPS:** TLS 1.3 enforced. Certificates: Let's Encrypt (if internet-accessible) or self-signed with internal CA (if LAN-only)
- **HTTP Strict Transport Security (HSTS):** enabled on all vhosts
- **URL routing:** all requests route through `public/index.php` (front controller)
- LAN users (internal staff) access the system via local IP or internal DNS hostname
- Field agents and Android apps access the system via a public-facing IP or domain (DDNS acceptable) — only TCP 443 exposed externally

## 3.4 Database Server

- **Engine:** MySQL 9.1 InnoDB
- **Character set:** `utf8mb4` with `utf8mb4_unicode_ci` collation
- **Deployment option A (smaller initial load):** MySQL on the same physical server as Nginx/PHP-FPM, in a separate MySQL process
- **Deployment option B (recommended at scale):** MySQL on a dedicated server with replication to a hot standby
- **Application DB user:** minimum-privilege dedicated user (`birdc_app`) — no `SUPER`, no `FILE`, no `CREATE USER` privileges
- **Root access from application:** disabled. Root credentials stored offline
- **Binary logging:** enabled for point-in-time recovery
- **Connection pooling:** PHP-FPM persistent connections; `max_connections` tuned for expected concurrency

## 3.5 Backup Strategy

| Backup type | Frequency | Retention | Destination |
|---|---|---|---|
| Full database dump (mysqldump) | Daily, 02:00 EAT | 30 days on-premise | Local backup volume |
| Binary log backup (incremental) | Every 4 hours | 7 days | Local backup volume |
| Weekly full archive | Every Sunday 03:00 | 52 weeks | Off-site: encrypted USB drive (hand-delivered) + remote encrypted copy (Restic to S3-compatible endpoint if internet allows) |
| Application code backup | On each deploy | 90 days | GitHub repository (code) + server snapshot |

All backup files are AES-256 encrypted. Backup integrity is verified weekly by a test restore to a staging environment.

## 3.6 CI/CD Pipeline

```
Developer workstation → Git push → GitHub repository
→ GitHub Actions pipeline:
  1. PHP lint (PHP-CS-Fixer, PHPStan level 6)
  2. PHPUnit test suite (≥ 80% coverage gate on financial services)
  3. Build artefact (Composer install --no-dev)
  4. Deploy to staging server (rsync over SSH)
  5. Manual approval gate (consultant or IT Administrator)
  6. Deploy to production server (rsync over SSH)
  7. Post-deploy health check (HTTP 200 on /health endpoint)
```

- The `main` branch represents production. Feature branches merge via pull request.
- No direct push to `main` without passing all pipeline stages.
- Secrets (database credentials, API keys) are stored in GitHub Actions Secrets and injected as environment variables — never committed to the repository.
- The `.env` file on the production server is managed manually by the IT Administrator and is not part of the repository.

## 3.7 Network Topology

```
Internet
    │
    ├─ TCP 443 (HTTPS) ──► Nginx (public-facing vhost)
    │                          └─ /public/          → Main ERP
    │                          └─ /public/sales-agents/ → Agent Portal
    │                          └─ /public/admin/    → Admin Panel
    │
BIRDC LAN (Nyaruzinga)
    │
    ├─ ZKTeco biometric devices  (local network, ZKTeco SDK)
    ├─ Thermal receipt printers  (Bluetooth / USB)
    ├─ Admin workstations        (TCP 443 to local Nginx)
    └─ Android mobile devices    (Wi-Fi or mobile data → TCP 443)
```

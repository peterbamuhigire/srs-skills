# Server Requirements for Longhorn ERP

## Hardware Specifications by Tenant Load

Select the configuration tier that matches the expected tenant count at go-live plus 12 months of projected growth.

| Configuration | CPU | RAM | Storage | Bandwidth | Tenants |
|---|---|---|---|---|---|
| Starter | 2 vCPU | 4 GB | 50 GB SSD | 100 Mbps | Up to 20 |
| Standard | 4 vCPU | 8 GB | 200 GB SSD | 500 Mbps | Up to 100 |
| Production | 8 vCPU | 16 GB | 500 GB SSD | 1 Gbps | Up to 500 |
| Enterprise | 16+ vCPU | 32+ GB | 2 TB+ SSD RAID | 2+ Gbps | 500+ |

*All storage figures are minimum provisioned values. Monitor disk usage and expand before utilisation reaches 80%.*

## Software Requirements

| Component | Minimum Version | Notes |
|---|---|---|
| Operating System | Ubuntu 22.04 LTS or Debian 12 | CentOS/RHEL 9 supported; Ubuntu 22.04 LTS recommended |
| PHP | 8.3+ | Required extensions listed below |
| MySQL | 9.1+ | InnoDB storage engine; UTF8MB4 character set |
| Apache | 2.4+ | mod_rewrite, mod_ssl, mod_headers must be enabled |
| Composer | 2.x | PHP dependency manager |
| TLS Certificate | — | Let's Encrypt (certbot) or commercial certificate required |

### Required PHP Extensions

The following PHP extensions must be enabled before installation:

- `pdo_mysql` — database connectivity
- `mbstring` — multibyte string handling for Unicode data
- `openssl` — encryption and HTTPS support
- `json` — API request and response encoding
- `xml` — report and data export parsing
- `zip` — archive handling for bulk imports and exports
- `gd` — image processing for logos and PDF output
- `intl` — locale-aware formatting (currency, dates)
- `curl` — outbound HTTP calls to EFRIS, MTN MoMo, and Africa's Talking

## Network Requirements

- Outbound HTTPS (port 443) to EFRIS API, MTN MoMo API, and Africa's Talking SMS gateway.
- Inbound ports 80 and 443 open on the server firewall.
- SSH (port 22) restricted to known administrator IP addresses.
- MySQL port 3306 bound to `127.0.0.1`; not exposed externally.

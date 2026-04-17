# Infrastructure — Academia Pro

## Reference Architecture Diagram

```
         +------------------+
         |   Cloudflare     | (WAF, DDoS, CDN)
         +--------+---------+
                  |
         +--------+---------+
         |   AWS ALB (HTTPS)|
         +--------+---------+
                  |
     +------------+-------------+
     |            |             |
+----+----+  +----+------+  +----+------+
|  Web    |  |  API      |  |  Horizon  |
|  React  |  |  Laravel  |  |  Queue    |
|  SPA    |  |  ECS      |  |  Workers  |
+---------+  +----+------+  +----+------+
                  |              |
          +-------+--------------+-------+
          |                              |
     +----+----+                    +----+------+
     | MySQL 8 | <----replica---->  | Redis 7   |
     | Primary |                    | ElastiCache|
     | Multi-AZ|                    +-----------+
     +----+----+
          |
     +----+-----+
     |  S3      | (file storage, UNEB CSVs, photos)
     |  eu-west |
     +----------+

External integrations:
  - MTN MoMo API        --> /api/mobile-money/momo/*
  - Airtel Money API    --> /api/mobile-money/airtel/*
  - SchoolPay (HTTP)    --> /api/schoolpay/*
  - UNEB (SFTP upload)  --> Horizon batch job
  - MoES EMIS (HTTPS)   --> Horizon batch job
  - AI LLM provider     --> via PIIScrubber (ADR-0005)
```

Rendered versions of this diagram live at `docs/infra/academiapro-ir.mmd` (Mermaid source) and `docs/infra/academiapro-ir.png` (export). The diagram is the Infrastructure Reference (IR) artefact required by `phase06.infra_has_ir_diagram`.

## Region Strategy

- Primary — `eu-west-1` (Ireland). Closest low-latency AWS region serving East Africa.
- DR — `us-east-1`. Read replica for MySQL; cross-region S3 replication. RPO 15 min; RTO 4 h.
- Data-residency — student personal data stays in `eu-west-1` unless explicit tenant opt-in to cross-region replication (tracked per-tenant in `tenant_settings.data_residency_consent`).

## Capacity

- Steady-state: 4 application instances (2 vCPU / 4 GB each).
- Peak (start-of-term): 12 application instances.
- Database: `db.r6g.large` primary with `db.r6g.large` replica. Scale to `r6g.xlarge` for peak.

## Traces

- NFR-AVAIL-001, NFR-SCALE-001.
- ADR-0002 (MySQL choice).
- CTRL-UG-002 (data residency).

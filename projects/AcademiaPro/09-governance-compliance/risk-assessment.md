# Risk Assessment / Register — Academia Pro

Every risk below links to at least one FR or NFR. This register is reviewed at every sprint boundary.

| Risk ID | Description | Likelihood | Impact | Score | Linked IDs | Mitigation |
|---|---|---|---|---|---|---|
| **R-001** | Tenant isolation bug leaks learner records across schools | Low | Critical | High | FR-001, NFR-SEC-002, ADR-0003, CTRL-ISO-A9 | Dual-layer defence; mandatory cross-tenant leakage test per PR; alert on `AcademiaProTenantLeak` |
| **R-002** | UNEB candidate file format changes without notice | Medium | High | High | FR-002, CTRL-UNEB-001 | UNEB liaison maintained; quarterly format review; version detection at export |
| **R-003** | MoES EMIS dictionary changes annually | High | Medium | High | FR-003, CTRL-EMIS-001 | Annual review concurrent with EMIS cycle; auto-detect new required fields |
| **R-004** | PII scrubber bypass leaks NIN/LIN to international LLM | Low | Critical | High | FR-004, ADR-0005, CTRL-UG-005 | PIIScrubber in hot path; `pii_scrubbed=0` alerts as Sev-1; architecture fitness test in CI |
| **R-005** | MTN MoMo / Airtel Money API rate-limits during fee-payment rush | High | High | Critical | FR-005, NFR-AVAIL-001 | Queue + retry with back-off; payment reconciliation runs hourly; SMS fallback to manual receipt capture |
| **R-006** | Parent pays twice for same invoice via two channels | High | Medium | High | FR-006, BR-FEE-005 | Duplicate-payment detection window 10 min; auto-flag for refund |
| **R-007** | Shared-hosting tenant exhausts connection pool | Medium | High | High | NFR-SCALE-001, ADR-0002 | Pool quotas per tenant; metering alert; force-upgrade path |
| **R-008** | DPPA regulatory change mandating data residency in Uganda | Medium | High | High | CTRL-UG-001, CTRL-UG-002 | Data residency flag per-tenant; eu-west-1 default; Uganda-region AWS on roadmap |
| **R-009** | UNEB exam freeze coincides with release window | High | Medium | High | NFR-AVAIL-001 | Freeze calendar enforced in `change-window.md` |
| **R-010** | Sponsor / CTO single point of failure | Medium | Critical | Critical | FR-007 | Secondary CTO hire in plan; documentation assumes team; runbook contacts tracked via CIA-002 |
| **R-011** | School lacks reliable internet for sync | High | Medium | High | FR-008, NFR-AVAIL-002 | Offline mode on Android and iOS; LWW conflict resolution; full audit of offline-sync events |
| **R-012** | Teacher resistance to digital grading | Medium | Medium | Medium | FR-009 | Training budget; hybrid paper/digital during transition sprints |

## Risk Policy

- Every FR implementation PR must declare whether it introduces a new risk.
- Risks rated Critical are reviewed by CTO + Security Lead monthly.
- The register is the source of truth for the risk dashboard in Grafana.

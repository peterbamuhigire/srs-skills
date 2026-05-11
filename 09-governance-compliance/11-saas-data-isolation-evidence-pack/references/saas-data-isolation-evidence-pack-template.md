# SaaS Data Isolation Evidence Pack — Template

## 1. Scope

| Field | Value |
|-------|-------|
| Period | YYYY-Qn |
| Services in scope | |
| Regions | |
| Excluded (with reason) | |

## 2. Tenancy pattern inventory

| Service | Compute | Storage | Pattern | ADR ref |
|---------|---------|---------|---------|---------|

## 3. Layered isolation mechanisms

| Layer | Service | Mechanism | Evidence artefact | Last verified |
|-------|---------|-----------|-------------------|---------------|
| Network | | | | |
| Compute | | | | |
| Storage | | | | |
| IAM | | | | |
| Code path | | | | |
| Audit | | | | |

## 4. Evidence index

```
evidence/
  net-sg-snapshot-2026Qn.json
  k8s-namespace-list.txt
  rls-policy-dump.sql
  rls-test-results.json
  kms-key-list.csv
  key-rotation-log.csv
  jwt-validation-test.json
  static-analysis-report.html
  repo-base-class.md
  impersonation-audit-90d.csv
  pentest-2026Qn.pdf
  cross-tenant-fuzz-results.json
  noisy-neighbor-test.json
  hard-delete-verification-sample.txt
```

## 5. Test results summary

| Test | Last run | Result | Evidence |
|------|----------|--------|----------|
| Negative-path (no tenant ctx) | | 100% rejected | jwt-validation-test.json |
| Tampered-context | | 100% rejected | jwt-validation-test.json |
| Cross-tenant fuzz (10k attempts) | | 0 leakage | cross-tenant-fuzz-results.json |
| Noisy-neighbor stress | | Interference P95 ≤ 10 ms | noisy-neighbor-test.json |
| Log-access | | 0 cross-tenant log visibility | (manual audit) |
| Hard-delete verification | | 100% verified | hard-delete-verification-sample.txt |
| Pentest (cross-tenant) | | No findings >= Medium | pentest-2026Qn.pdf |

## 6. Control framework mapping

| Control | Framework | Mechanism | Evidence |
|---------|-----------|-----------|----------|
| CC6.1 Logical access | SOC 2 | | |
| CC6.6 Boundary protection | SOC 2 | | |
| CC6.7 Data in transit | SOC 2 | | |
| A.9.4 Information access | ISO 27001 | | |
| A.13.1 Network security | ISO 27001 | | |
| A.18.1 Legal compliance | ISO 27001 | | |
| Art.32 Security of processing | GDPR | | |
| Art.17 Erasure | GDPR | | |
| Art.20 Portability | GDPR | | |

## 7. Open gaps & remediation

| Gap | Severity | Owner | Due | Status |
|-----|----------|-------|-----|--------|

## 8. Attestation

| Role | Name | Date | Signature |
|------|------|------|-----------|
| CISO | | | |
| Compliance lead | | | |
| Lead architect | | | |
| Auditor (external, if applicable) | | | |

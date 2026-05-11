# AI Agent Attestation Evidence Pack Template

Pack layout, manifest schema, and presentation conventions for the auditor-ready bundle. Reproduce verbatim and replace `{placeholder}` values.

## Pack directory layout

```
evidence-pack-{audit-window-id}/
  manifest.json                     # signed at pack close; every artefact listed with hash
  manifest.json.sig                 # detached signature
  README.md                         # auditor-facing intro (cross-link to walkthrough script)

  policies/                         # the signed policy pack
    agent-action-governance-policy.pdf
    agent-audit-log-retention-policy.pdf
    agent-approval-and-supervision-policy.pdf
    agent-kill-switch-and-drill-policy.pdf
    agent-memory-erasure-policy.pdf
    agent-red-team-and-safety-policy.pdf
    agent-compliance-evidence-and-attestation-policy.pdf
    sign-off-ledger.csv

  controls/                         # narrative + evidence per control row
    soc2/
      CC1-1/
        narrative.md
        evidence-pointer.json       # points to artefacts under /evidence/
      CC6-1/
      ...
    iso27001/
      A-5-1/
      A-8-15/
      ...
    hipaa/
      164-308-a-1/
      164-312-b/
      ...

  evidence/                         # the raw evidence
    audit-log/
      retention-config.json
      integrity-reports/
        daily-YYYY-MM-DD.json
      samples/
        approval-events-25.csv
        daily-review-tickets-25.csv
        pr-changes-25.csv
    drills/
      kill-switch-Q1.pdf
      kill-switch-Q2.pdf
      replay-Q1.pdf
      ...
    access/
      service-principal-review-Q1.csv
      service-principal-review-Q2.csv
      ...
    incidents/                      # SEV1/SEV2 in window
    suppliers/
      sub-processor-list.json
      provider-risk-assessment.pdf
      training-exclusion-clauses.pdf
    baa-dpa/
      baa-ledger.csv
      dpa-ledger.csv
    disclosures/
      responsible-ai-declaration-vX.Y.pdf
      in-product-disclosure-screenshots/
    sdlc/
      eval-gate-results/
      red-team-results/
      adr-list.csv
    monitoring/
      alert-configuration.json
      slo-reports/
        monthly-YYYY-MM.pdf
    training/
      oncall-training-completion-Qn.csv

  walkthroughs/                     # screencasts and demo evidence
    governance-walkthrough.mp4
    kill-switch-drill-walkthrough.mp4
    approval-event-flow-walkthrough.mp4
    evidence-pack-walkthrough.mp4

  prior-year-findings/
    finding-list.csv
    closure-evidence/
```

## manifest.json schema

```json
{
  "pack_id": "evidence-pack-2026-Q1",
  "audit_window": {
    "start": "2025-04-01",
    "end": "2026-03-31"
  },
  "framework_scope": ["SOC2-TSC", "ISO27001-2022", "HIPAA"],
  "owner": "AI Lead",
  "produced_by": "{collector-version}",
  "produced_at": "2026-04-05T12:00:00Z",
  "artefacts": [
    {
      "path": "policies/agent-action-governance-policy.pdf",
      "sha256": "…",
      "source": "document-management",
      "capture_method": "manual sign + ledger entry",
      "redactions": [],
      "controls": ["SOC2.CC1.1", "ISO27001.A.5.1", "HIPAA.164.316.a"]
    },
    {
      "path": "evidence/audit-log/samples/approval-events-25.csv",
      "sha256": "…",
      "source": "orchestrator",
      "capture_method": "stratified-sample-job v1.2",
      "redactions": ["user-pii", "other-tenant-data"],
      "controls": ["SOC2.CC5.1", "SOC2.PI1.4", "HIPAA.164.312.d"]
    }
  ],
  "redaction_log": [
    {
      "artefact": "evidence/audit-log/samples/approval-events-25.csv",
      "rule_id": "rdct-001",
      "operator": "compliance-job-runner",
      "time": "2026-04-04T18:32:00Z",
      "fields": ["user.email", "user.full_name"]
    }
  ],
  "signatures": [
    {
      "role": "AI Lead",
      "name": "…",
      "time": "…",
      "signature": "…"
    },
    {
      "role": "DPO",
      "name": "…",
      "time": "…",
      "signature": "…"
    }
  ],
  "pack_signature": {
    "algorithm": "ed25519",
    "signer_key_id": "…",
    "value": "…"
  }
}
```

## Per-artefact metadata required

| Field | Required |
|-------|----------|
| `path` | yes |
| `sha256` | yes |
| `source` | yes |
| `capture_method` | yes |
| `redactions` | yes (empty array if none) |
| `controls` | yes |
| `produced_at` | yes (ISO-8601) |
| `producer_role_or_job` | yes |

## Auditor README contents

The pack README provides:

1. Pack id and window dates.
2. Framework scope.
3. Quick-find table: control id → narrative path.
4. Walkthrough video index.
5. Sample sets index.
6. Sign-off summary.

## Signing and verification

- Manifest signed with the organisation's evidence-pack signing key at pack close.
- Auditor portal verifies signature on view.
- Tamper of any artefact recomputes its hash and breaks the manifest signature.

## Auditor portal interface contract

- List view filtered by control id.
- Detail view with narrative + evidence pointers.
- Download events logged.
- Time-bound access (default window + 14 days).
- Named-recipient only.

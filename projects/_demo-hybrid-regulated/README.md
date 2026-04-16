# _demo-hybrid-regulated — Livelink Health (Uganda)

End-to-end proof project demonstrating a PASSING srs-skills workspace
across all nine phase gates plus the hybrid synchronisation gate.

- Methodology: Water-Scrum-Fall hybrid
- Domain: Uganda (DPPA 2019)
- Date: 2026-04-16
- Files: 60 (including evidence pack ZIP)

## What this project proves

1. The kernel can be run against a realistic, regulated, hybrid-methodology
   workspace and return `ENGINE CONTRACT: PASS`.
2. Every phase gate (phase01 through phase09) fires checks that are both
   present and satisfied by the artifacts in this directory.
3. The `HybridSyncGate` is satisfied by `_registry/baseline-trace.yaml`
   and `07-agile-artifacts/definitions/dor-dod.md`.
4. The Uganda domain overlay selects CTRL-UG-001 through CTRL-UG-004,
   and every selected control has matching evidence.
5. The sabotage flag `--break-something` produces deterministic failures
   in `kernel.no_unresolved_fail_markers`, `phase02.smart_nfr`, and
   `phase09.traceability`, proving the kernel fails when required.

## Run it

```bash
# Passes
python -m engine validate projects/_demo-hybrid-regulated

# Fails (on purpose): three synthetic findings
python -m engine validate projects/_demo-hybrid-regulated --break-something
```

## Re-seed from scratch

The seeder is idempotent:

```bash
python scripts/seed_demo_project.py
```

This rewrites all files under `projects/_demo-hybrid-regulated/`,
re-runs `engine sync` to populate `_registry/identifiers.yaml`, and
snapshots baseline `v1.0` under
`09-governance-compliance/07-baseline-delta/v1.0.yaml`.

## Structure

- `_context/` — vision, stakeholders, features, glossary, methodology,
  domain, quality-standards, business-rules.
- `02-requirements-engineering/srs/` — 14 functional requirements
  (FR-001..FR-014), 8 non-functional requirements (NFR-001..NFR-008),
  interfaces, overview, introduction, design constraints.
- `03-design-documentation/` — API spec, DB schema, UX spec, threat model.
- `04-development/` — coding standards, env setup.
- `05-testing-documentation/` — 14 test cases (TC-001..TC-014),
  deterministic checks, coverage matrix, completion report.
- `06-deployment-operations/` — deployment guide, runbook (with
  `runbook/pdpo-escalation.md` procedure), monitoring, infrastructure,
  go-live checklist, incident-response playbook.
- `07-agile-artifacts/` — DoR, DoD, hybrid dor-dod.md, sprint plan
  (US-001..US-005), retrospective actions, velocity.
- `08-end-user-documentation/` — user manual with screenshots,
  release notes citing FRs, FAQ with 5 Q&A.
- `09-governance-compliance/` — traceability matrix, audit report,
  compliance report per control, risk assessment linking risks to FR/NFR/CTRL,
  ADR-0001 (Postgres) and ADR-0002 (crypto-shredding for DPPA erasure),
  CIA-001 (add MFA to provider login), baseline-delta v1.0.
- `_registry/` — controls, baseline-trace, baselines, adr-catalog,
  change-impact, sign-off-ledger, waivers, identifiers.
- `evidence-pack-2026-04-16.zip` — machine-built evidence pack.

## Waiver

`WAIVE-001` covers `phase08.user_manual_has_screenshots` for placeholder
PNGs pending final UI sign-off. Expires 2026-07-15 (within the 90-day cap).

# AI Agent Compliance SRS-Docs Audit — May 2026

This audit extends the AI-agent-products pass (`agent-products-srs-audit-2026.md`) with the **compliance, attestation, and audit-procedure** documentation stack required when an agentic SaaS must pass SOC 2 Type II, ISO/IEC 27001, and HIPAA Security Rule audits, with agent-specific controls satisfied to a level that survives a Big-4 / HITRUST / sectoral regulator examination.

It is the **policy / control-mapping / attestation-package** companion to a parallel software-dev pass that produces the **engineering side** — automated evidence collectors, hash-chain audit log, gap detectors, integrity verifiers, and the auditor portal. The two passes share IDs and cross-link.

Convention: skill IDs follow the existing numbered pattern. New 09 skills continue from 20; the new 06 skill continues from 20. All new skills are prefixed `ai-agent-` so they remain discoverable as the agent family.

## Summary of new artefacts created this session

- **New skills (9):** see "New skills" table below.
- **Enhanced skills (11):** compliance evidence cross-links added to responsible-AI addendum, ADR catalogue, action catalogue, eval spec, red-team plan, runbook, AI Act doc, DPIA, incident evidence-pack spec, phase-09 README, and 02-definition-of-done.
- **Cross-cutting templates (12):** SOC 2 control matrix, ISO 27001 control matrix, HIPAA control matrix, 7-policy compliance pack, attestation evidence pack, compliance runbook, BAA addendum, DPA addendum, multi-regulator overlap matrix, auditor-on-the-day playbook, evidence-frequency table, compliance-readiness checklist.

---

## Why a compliance-specific pass is needed

The agent-products pass produced the operating artefacts an agent SaaS needs to run safely. None of those artefacts is shaped for an **auditor's reading order** or for a **control test**. An audit firm walks a control framework (SOC 2 TSC, ISO 27001 Annex A, HIPAA §164.3xx) row by row and demands, per row:

1. The **policy** that says we will do it.
2. The **control narrative** that says how we do it.
3. The **evidence** that we did it during the audit window.
4. The **test procedure** the auditor will run.
5. The **sampling protocol** and how many samples.
6. The **chain of custody** of the evidence.
7. The **remediation plan** when a control was not satisfied during the window.

Agent systems introduce control concerns that none of the standard frameworks anticipated cleanly:

- **CC6.1 Logical Access** — an autonomous agent runs as a service principal whose access cannot be tied to a single human user; access reviews must enumerate agent identities, their scoped tool permissions, and per-tenant scopes.
- **CC7.2 Anomaly Detection** — the anomaly surface is now "agent did something unusual" not just "user logged in from a new IP"; anomaly detection must cover irreversible-action rate, intervention rate, cost-per-run, and cross-tenant tool routing.
- **CC8.1 Change Management** — every change to the planner template, action catalogue, supervisor prompt, or memory store policy is a change to a control surface; CAB must see it.
- **A.5.31 Legal Requirements** (ISO 27001) — agent disclosures, irreversibility statements, and human-final-decision language are legal requirements with control evidence.
- **A.8.16 Monitoring** — agent-task availability, irreversible-action incidents, and audit-log integrity are now monitored controls.
- **HIPAA §164.312(b) Audit Controls** — agent action audit log is the audit control; integrity (§164.312(c)) requires hash-chain or WORM.
- **HIPAA §164.308(a)(4) Information Access Management** — agent service principals accessing PHI are workforce-equivalent; minimum-necessary applies; admin-only constraint for clinical PHI agents.

The auditor will accept evidence from the agent-products pass artefacts — but only if a **control matrix** points each control to the right artefact, the **evidence pack** is assembled, and the **policy pack** is signed by the right roles.

---

## Phase 09 — Governance & Compliance

### Gaps the compliance reality reveals

| # | Gap | Source |
|---|-----|--------|
| 1 | No SOC 2 control matrix for agents — TSC mapping with agent-specific implementation and evidence-frequency per control | AICPA SOC 2 TSP 100; auditor interviews |
| 2 | No ISO/IEC 27001 Annex A control matrix for agents — A.5–A.8 treatment for agent action governance, audit logging, kill-switch, supervision | ISO/IEC 27001:2022; BSI / certification-body guidance |
| 3 | No HIPAA Security Rule control matrix for agents handling PHI — §164.308 admin, §164.310 physical, §164.312 technical, with admin-only constraint for clinical PHI agents | 45 CFR §164; HHS OCR guidance |
| 4 | No written policy pack — agent action governance, audit-log retention, approval and supervision, kill-switch and drill, memory erasure, red-team and safety, compliance evidence and attestation | SOC 2 CC1 / CC2; ISO A.5; HIPAA §164.316 |
| 5 | No attestation-preparation spec — pre-window evidence pre-gathering, auditor-readiness checklist, gap-remediation cadence, SOC 2 Type II window vs ISO surveillance vs HIPAA periodic review | AICPA SOC 2 attest engagement; ISO ISMS audit cycle; HIPAA Security Rule §164.308(a)(8) |
| 6 | No agent evidence-pack spec — per-control evidence class, sampling, chain-of-custody, retention, presentation format | AICPA TSP 100; ISO/IEC 27007 |
| 7 | No multi-regulator overlap matrix — SOC2 × ISO × HIPAA × EU AI Act × NIST AI RMF × KE DPA × NDPR × POPIA × UG DPPA × RW DP Law | client requests; cross-regime audit experience |
| 8 | No BAA addendum for agent-handled PHI; no DPA addendum extending the existing AI DPA to agents | HIPAA §164.504(e); GDPR Art. 28; KE DPA s.40; NDP Act 2023; POPIA s.21 |

### New skills

| Skill | Path | Purpose |
|-------|------|---------|
| `20-ai-agent-soc2-control-pack` | `09-governance-compliance/20-ai-agent-soc2-control-pack/` | SOC 2 TSC control matrix for agents; per-control objective, agent-specific implementation requirement, evidence required, evidence frequency, test procedure |
| `21-ai-agent-iso27001-control-pack` | `09-governance-compliance/21-ai-agent-iso27001-control-pack/` | ISO/IEC 27001:2022 Annex A control matrix for agents; A.5 through A.8 agent treatments with evidence and audit procedure |
| `22-ai-agent-hipaa-control-pack` | `09-governance-compliance/22-ai-agent-hipaa-control-pack/` | HIPAA Security Rule control matrix for agents handling PHI; admin / physical / technical safeguards; admin-only constraint for clinical PHI agents; BAA implications |
| `23-ai-agent-compliance-policy-pack` | `09-governance-compliance/23-ai-agent-compliance-policy-pack/` | Seven bundled policies: agent action governance, audit-log retention, approval and supervision, kill-switch and drill, memory erasure, red-team and safety, compliance evidence and attestation |
| `24-ai-agent-attestation-preparation-spec` | `09-governance-compliance/24-ai-agent-attestation-preparation-spec/` | Preparing for SOC 2 Type II window, ISO surveillance audit, HIPAA periodic review; timeline, evidence pre-gathering, auditor-readiness checklist, gap-remediation cadence |
| `25-ai-agent-evidence-pack-spec` | `09-governance-compliance/25-ai-agent-evidence-pack-spec/` | What evidence the auditor expects per control class; evidence-pack format; sampling protocol; chain-of-custody; retention; presentation format |
| `26-ai-agent-baa-and-data-processing-language` | `09-governance-compliance/26-ai-agent-baa-and-data-processing-language/` | BAA agent addendum for HIPAA engagements; DPA agent addendum for GDPR and African DPA regimes |
| `27-ai-agent-regulator-overlap-mapping` | `09-governance-compliance/27-ai-agent-regulator-overlap-mapping/` | SOC2 × ISO × HIPAA × EU AI Act × NIST AI RMF × KE DPA × NDPR × POPIA × UG DPPA × RW; one-evidence-many-regimes reuse |

### Phase 06 — Deployment & Operations

| Skill | Path | Purpose |
|-------|------|---------|
| `20-ai-agent-compliance-runbook` | `06-deployment-operations/20-ai-agent-compliance-runbook/` | Operational compliance runbook: drill schedule, evidence-collection schedule, control-test schedule, audit-window operations, on-the-day playbook |

### Enhancements

| Skill | What was added |
|-------|----------------|
| `09-governance-compliance/18-ai-agent-responsible-ai-addendum` | Compliance evidence cross-link table (SOC2 / ISO / HIPAA rows pointing to addendum sections) |
| `09-governance-compliance/19-ai-agent-adr-catalogue` | Compliance-relevant ADR slots: SOC2 control-ownership ADR, HIPAA admin-only-PHI-agent ADR, audit-log integrity ADR |
| `02-requirements-engineering/17-ai-agent-action-catalogue-spec` | Per-tool compliance metadata fields: `phi_touch`, `cardholder_touch`, `protected_class_decision`, `evidence_class`, `retention_minimum` |
| `05-testing-documentation/06-ai-agent-eval-spec` | Eval coverage as compliance evidence — note pointing to evidence-pack spec |
| `05-testing-documentation/07-ai-agent-red-team-test-plan` | Red-team results as compliance evidence — sampling and presentation guidance |
| `06-deployment-operations/14-ai-agent-runbook` | Drill evidence-capture pointer — evidence frequency table reference |
| `09-governance-compliance/15-ai-act-and-regulatory-compliance-doc` | Agent-specific overlap section with SOC2 / ISO / HIPAA |
| `09-governance-compliance/16-ai-data-flow-and-dpia` | Agent-specific data flow elements for compliance — service-principal data flow rows |
| `06-deployment-operations/17-ai-incident-evidence-pack-spec` | Compliance-evidence superset relationship — incident evidence is also compliance evidence under specific controls |
| `09-governance-compliance/README.md` | New family registered (SOC2 / ISO / HIPAA agent control packs) |
| `skills/02-definition-of-done.md` (parent DoD note) | Agent compliance DoD additions — control coverage before GA |

### Cross-cutting templates created

| Template | Path | Purpose |
|----------|------|---------|
| SOC 2 control matrix | `20-ai-agent-soc2-control-pack/references/ai-agent-soc2-control-matrix-template.md` | Full TSC mapping with worked example for an agentic-CX SaaS |
| ISO 27001 control matrix | `21-ai-agent-iso27001-control-pack/references/ai-agent-iso27001-control-matrix-template.md` | A.5–A.8 mapping for agent systems |
| HIPAA control matrix | `22-ai-agent-hipaa-control-pack/references/ai-agent-hipaa-control-matrix-template.md` | §164.308/.310/.312 with admin-only-PHI agent example |
| Compliance policy pack | `23-ai-agent-compliance-policy-pack/references/ai-agent-compliance-policy-pack-template.md` | Seven policies bundled, each ready to adapt |
| Attestation evidence pack | `25-ai-agent-evidence-pack-spec/references/ai-agent-attestation-evidence-pack-template.md` | Auditor-ready evidence package layout |
| Compliance runbook | `06-deployment-operations/20-ai-agent-compliance-runbook/references/ai-agent-compliance-runbook-template.md` | Drill + evidence + control-test schedule |
| BAA addendum | `26-ai-agent-baa-and-data-processing-language/references/ai-agent-baa-template.md` | Drop-in BAA agent addendum |
| DPA addendum | `26-ai-agent-baa-and-data-processing-language/references/ai-agent-dpa-template.md` | Drop-in DPA agent addendum extending the existing AI DPA |
| Regulator overlap matrix | `27-ai-agent-regulator-overlap-mapping/references/ai-agent-regulator-overlap-matrix.md` | Multi-regime crosswalk |
| Auditor on-the-day playbook | `24-ai-agent-attestation-preparation-spec/references/ai-agent-auditor-on-the-day-playbook.md` | What to do when the auditor walks in |
| Evidence frequency table | `25-ai-agent-evidence-pack-spec/references/ai-agent-evidence-frequency-table.md` | Per-control evidence cadence |
| Compliance readiness checklist | `24-ai-agent-attestation-preparation-spec/references/ai-agent-compliance-readiness-checklist.md` | 50–100 point pre-audit assessment |

---

## Cross-engine handoff with software-dev pass

This compliance pass owns the **artefacts** (policy text, control narrative, evidence pack layout, audit procedure, BAA / DPA language). The parallel software-dev pass owns the **machinery** (automated evidence collectors, hash-chain audit log, gap detector, integrity verifier, auditor portal). Concretely:

| Control surface | This pass produces | Software-dev pass produces |
|------------------|--------------------|----------------------------|
| Action audit log | Retention policy; SOC2/ISO/HIPAA control narrative; sampling protocol | Hash-chain append-only log; integrity verifier; portal viewer |
| Kill-switch | Policy text; drill schedule; control test procedure | Switch implementation; propagation telemetry; drill-mode runner |
| Evidence pack | Pack layout; per-control evidence list; chain-of-custody language; redaction policy | Automated collectors; signed-zip exporter; auditor-portal access |
| Approval events | Policy; supervision matrix; sampling guidance | Approval-event signed records; tamper-evident store; replay |
| Memory erasure | Policy; DSAR-equivalent procedure; retention exceptions | Erasure executor; verification job; certificate of erasure |

Both passes cross-link explicitly in every artefact's *Cross-Refs* section. Evidence frequency table is the **shared contract**: the software-dev pass guarantees the collector produces evidence at the declared cadence; the compliance pass guarantees the auditor will accept it at that cadence.

---

## Open compliance items (not closed in this pass)

1. PCI-DSS for agents that handle cardholder data — referenced only; full control pack out of scope.
2. FedRAMP / StateRAMP for agents in US public-sector — referenced only.
3. EU DORA for financial-services agents — referenced only.
4. SOC 1 (financial-reporting) for billing-touching agents — referenced only.

Recommended next sessions:

1. **PCI-DSS agent control pack** — for any agent that touches cardholder data, including the billing-touching planner.
2. **FedRAMP agent control pack** — moderate / high baseline mapped to NIST 800-53 with agent-specific overlays.
3. **EU DORA + financial-sector agent pack** — operational-resilience, third-party-risk, incident-classification for agentic finance.
4. **Agent insurance and indemnity language pack** — contractual liability allocation for irreversible-action incidents.

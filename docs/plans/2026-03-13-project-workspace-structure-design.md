# Design: Project Workspace Structure & Domain Knowledge Base

**Date:** 2026-03-13
**Status:** Approved
**Author:** Peter Bamuhigire

---

## 1. Overview

This design introduces two major additions to the SDLC-Docs-Engine:

1. **`projects/` workspace** — an untracked, per-consultant directory where all client project documentation is generated, built, and exported as `.docx` files
2. **`domains/` knowledge base** — a tracked directory containing domain-specific requirements, regulations, architecture patterns, and feature baselines that are auto-injected during project scaffolding

---

## 2. Directory Layout

```
srs-skills/                                  ← git repo (tracked)
├── 00-meta-initialization/
├── 01-strategic-vision/
├── 02-requirements-engineering/
├── 03-design-documentation/
├── 04-development-artifacts/
├── 05-testing-documentation/
├── 06-deployment-operations/
├── 07-agile-artifacts/
├── 08-end-user-documentation/
├── 09-governance-compliance/
├── skills/
├── domains/                                 ← NEW (tracked, committed to repo)
│   ├── INDEX.md
│   ├── healthcare/
│   ├── finance/
│   ├── education/
│   ├── retail/
│   ├── logistics/
│   └── government/
├── scripts/
│   └── build-doc.sh                         ← NEW: Pandoc build script
├── templates/
│   └── reference.docx                       ← NEW: corporate Word style template
├── .gitignore                               ← add: projects/
└── projects/                               ← UNTRACKED (gitignored)
    └── Livecare-Hospital-ERP/
        ├── _context/
        ├── 01-strategic-vision/
        ├── 02-requirements-engineering/
        ├── 03-design-documentation/
        ├── 04-development-artifacts/
        ├── 05-testing-documentation/
        ├── 06-deployment-operations/
        ├── 07-agile-artifacts/
        ├── 08-end-user-documentation/
        └── 09-governance-compliance/
```

---

## 3. Project Workspace (`projects/`)

### 3.1 Per-Project Structure

Each project directory follows this layout:

```
projects/Livecare-Hospital-ERP/
├── _context/                        ← shared inputs read by all phases
│   ├── vision.md
│   ├── features.md
│   ├── tech_stack.md
│   ├── business_rules.md
│   ├── quality_standards.md
│   ├── glossary.md
│   └── domain.md                    ← auto-populated from domains/ at scaffold time
│
├── 01-strategic-vision/
│   ├── 01-prd/
│   │   ├── 01-purpose.md
│   │   ├── 02-scope.md
│   │   ├── 03-stakeholders.md
│   │   ├── 04-features.md
│   │   └── manifest.md              ← optional: overrides auto file order
│   ├── 02-vision-statement/
│   │   └── 01-vision.md
│   ├── 03-business-case/
│   │   ├── 01-executive-summary.md
│   │   ├── 02-cost-benefit.md
│   │   └── 03-risks.md
│   ├── PRD.docx                     ← final built output
│   ├── VisionStatement.docx
│   └── BusinessCase.docx
│
├── 02-requirements-engineering/
│   ├── 01-srs/
│   │   ├── 01-introduction.md
│   │   ├── 02-overall-description.md
│   │   ├── 03-interfaces.md
│   │   ├── 04-functional-requirements.md
│   │   ├── 05-logic-modeling.md
│   │   ├── 06-nfr.md
│   │   └── manifest.md
│   ├── 02-user-stories/             ← agile track
│   │   ├── 01-epics.md
│   │   └── 02-stories.md
│   ├── SRS_Draft.docx
│   └── UserStories.docx
│
├── 03-design-documentation/
│   ├── 01-hld/
│   ├── 02-lld/
│   ├── 03-api-spec/
│   ├── 04-database-design/
│   ├── 05-ux-spec/
│   ├── HLD.docx
│   ├── LLD.docx
│   ├── APISpec.docx
│   └── DatabaseDesign.docx
│
├── 04-development-artifacts/
│   ├── 01-technical-spec/
│   ├── 02-coding-guidelines/
│   └── TechnicalSpec.docx
│
├── 05-testing-documentation/
│   ├── 01-test-strategy/
│   ├── 02-test-plan/
│   ├── 03-test-report/
│   ├── TestStrategy.docx
│   ├── TestPlan.docx
│   └── TestReport.docx
│
├── 06-deployment-operations/
│   ├── 01-deployment-guide/
│   ├── 02-runbook/
│   ├── DeploymentGuide.docx
│   └── Runbook.docx
│
├── 07-agile-artifacts/
│   ├── 01-sprint-planning/
│   ├── 02-dod/
│   ├── 03-dor/
│   └── Retrospective.docx
│
├── 08-end-user-documentation/
│   ├── 01-user-manual/
│   ├── 02-installation-guide/
│   ├── 03-faq/
│   ├── UserManual.docx
│   ├── InstallationGuide.docx
│   └── FAQ.docx
│
└── 09-governance-compliance/
    ├── 01-traceability-matrix/
    ├── 02-audit-report/
    ├── 03-compliance/
    ├── 04-risk-assessment/
    ├── TraceabilityMatrix.docx
    ├── AuditReport.docx
    ├── ComplianceDocs.docx
    └── RiskAssessment.docx
```

### 3.2 `_context/` Files

| File | Purpose |
|---|---|
| `vision.md` | Project goals, problem statement, stakeholders |
| `features.md` | Feature list with descriptions |
| `tech_stack.md` | Languages, frameworks, infrastructure |
| `business_rules.md` | Domain rules and constraints |
| `quality_standards.md` | Performance, security, reliability targets |
| `glossary.md` | IEEE 610.12 terminology definitions |
| `domain.md` | Auto-populated from `domains/<domain>/INDEX.md` at scaffold time |

All phase skills read from `_context/` before generating any section file.

### 3.3 `.gitignore` Addition

```
projects/
```

---

## 4. Document Build Mechanic

### 4.1 Triggering a Build

When a consultant says **"build the SRS"** (or any document name), Claude:

1. Resolves the document directory (e.g., `02-requirements-engineering/01-srs/`)
2. Checks for `manifest.md` — if present, uses file order defined there; otherwise sorts section files by filename prefix
3. Stitches all `.md` files in resolved order
4. Executes Pandoc:

```bash
pandoc 01-introduction.md 02-overall-description.md ... \
  --reference-doc=../../../templates/reference.docx \
  -o SRS_Draft.docx
```

5. Drops the `.docx` in the Phase root directory
6. Reports which files were stitched and the output path

### 4.2 `manifest.md` Format

If a consultant wants custom ordering or to exclude a draft section:

```markdown
# manifest
01-introduction.md
02-overall-description.md
04-functional-requirements.md
06-nfr.md
# 05-logic-modeling.md  ← commented out = excluded from build
```

### 4.3 Manual Edit → Rebuild Flow

1. Consultant edits any section file (e.g., `03-functional-requirements.md`)
2. Tells Claude: "build the SRS"
3. Claude re-stitches all files and overwrites the existing `.docx`

### 4.4 Build Script (`scripts/build-doc.sh`)

```bash
#!/bin/bash
# Usage: ./scripts/build-doc.sh <doc-dir> <output-name>
# Example: ./scripts/build-doc.sh projects/Livecare/02-requirements-engineering/01-srs SRS_Draft

DOC_DIR=$1
OUTPUT=$2
TEMPLATE="$(dirname "$0")/../templates/reference.docx"

if [ -f "$DOC_DIR/manifest.md" ]; then
  FILES=$(grep -v '^#' "$DOC_DIR/manifest.md" | grep '\.md$' | sed "s|^|$DOC_DIR/|")
else
  FILES=$(ls "$DOC_DIR"/*.md 2>/dev/null | sort)
fi

pandoc $FILES --reference-doc="$TEMPLATE" -o "$(dirname "$DOC_DIR")/$OUTPUT.docx"
echo "Built: $(dirname "$DOC_DIR")/$OUTPUT.docx"
```

---

## 5. New Project Scaffolding

### 5.1 Interview Flow

When a consultant says **"start a new project"**, Claude conducts a 5-question interview (one at a time):

1. **Project name** — used as directory name (e.g., `Livecare-Hospital-ERP`)
2. **Brief description** — what the software does (pre-populates `_context/vision.md`)
3. **Methodology** — Waterfall / Agile / Hybrid
4. **Domain** — healthcare / finance / education / retail / logistics / government / other
5. **Project owner name** — primary contact

### 5.2 Scaffold Actions

After the interview Claude:

1. Creates `projects/<ProjectName>/` with all 9 phase directories
2. Creates all document subdirectories under each phase
3. Creates `_context/` files — pre-populated with interview answers + guided `<!-- TODO: ... -->` prompts for gaps
4. Copies domain baseline from `domains/<domain>/` into `_context/domain.md`
5. Injects `[DOMAIN-DEFAULT]` tagged content into relevant section stubs
6. Prints a scaffold summary showing created structure and outstanding `_context/` TODOs

### 5.3 Scaffold Summary Output Example

```
Project scaffolded: projects/Livecare-Hospital-ERP/

_context/ status:
  ✓ vision.md        — pre-populated from interview
  ✓ domain.md        — healthcare baseline injected
  ○ features.md      — TODO: add feature list
  ○ tech_stack.md    — TODO: specify technologies
  ○ business_rules.md — TODO: define business rules
  ○ quality_standards.md — TODO: set quality targets
  ○ glossary.md      — template ready, add terms

Ready to generate: 01-strategic-vision (PRD, Vision Statement, Business Case)
Run: "generate PRD for Livecare"
```

---

## 6. Domain Knowledge Base (`domains/`)

### 6.1 Structure

```
domains/
├── INDEX.md                              ← master index of all domains
├── healthcare/
│   ├── INDEX.md                          ← domain overview, applicable features
│   ├── references/
│   │   ├── regulations.md               ← HIPAA, HL7/FHIR, FDA 21 CFR Part 11
│   │   ├── architecture-patterns.md     ← audit logging, PHI isolation, multi-tenant
│   │   ├── security-baseline.md         ← encryption, access control, PHI handling
│   │   ├── integrations.md              ← EHR, lab systems, billing, PACS
│   │   └── nfr-defaults.md              ← default non-functional requirements
│   └── features/
│       ├── patient-management.md
│       ├── appointment-scheduling.md
│       ├── billing-claims.md
│       ├── clinical-documentation.md
│       └── reporting-analytics.md
├── finance/
│   ├── INDEX.md
│   ├── references/
│   │   ├── regulations.md               ← PCI-DSS, SOX, Basel III, AML
│   │   ├── architecture-patterns.md
│   │   ├── security-baseline.md
│   │   └── nfr-defaults.md
│   └── features/
├── education/
├── retail/
├── logistics/
└── government/
```

### 6.2 Domain INDEX.md Format

```markdown
# Domain: Healthcare

## Profile
- **Regulatory bodies:** HHS, FDA, CMS
- **Key standards:** HIPAA, HL7 FHIR R4, ICD-10, CPT
- **Risk level:** High (PHI/PII data)
- **Audit requirement:** Mandatory

## Default Feature Modules
- Patient Management
- Appointment Scheduling
- Clinical Documentation
- Billing & Claims
- Reporting & Analytics

## Auto-Injected Requirements
See references/nfr-defaults.md for the full list of [DOMAIN-DEFAULT] requirements
injected into new projects.

## References
- regulations.md
- architecture-patterns.md
- security-baseline.md
- integrations.md
- nfr-defaults.md
```

### 6.3 Domain Injection Format

Domain-default content injected into section files is wrapped in tagged blocks:

```markdown
<!-- [DOMAIN-DEFAULT: healthcare] Source: domains/healthcare/references/nfr-defaults.md -->
#### NFR-HC-001: Patient Data Audit Trail
The system shall maintain a complete, tamper-proof audit log of all access
to patient health information (PHI) in compliance with HIPAA 45 CFR §164.312(b).

**Verifiability:** A test must demonstrate that every read/write access to a
PHI record produces an immutable log entry containing: user ID, timestamp,
action type, and record identifier.
<!-- [END DOMAIN-DEFAULT] -->
```

Consultants review, keep, or delete these blocks before building the final `.docx`.

---

## 7. Initial Domains to Scaffold

| Domain | Key Regulations | Key Features |
|---|---|---|
| `healthcare` | HIPAA, HL7/FHIR, FDA 21 CFR | Patient mgmt, EMR, billing, scheduling |
| `finance` | PCI-DSS, SOX, AML/KYC | Ledger, transactions, reporting, compliance |
| `education` | FERPA, COPPA | Enrollment, LMS, grading, attendance |
| `retail` | PCI-DSS, GDPR | POS, inventory, e-commerce, loyalty |
| `logistics` | DOT regulations | Fleet, shipment tracking, warehouse, routing |
| `government` | FISMA, FedRAMP, GDPR | Case mgmt, citizen portal, audit, procurement |

---

## 8. What is Tracked vs. Untracked

| Path | Tracked in Git | Reason |
|---|---|---|
| `00-09` phase skill directories | Yes | Reusable engine |
| `skills/` | Yes | Shared patterns |
| `domains/` | Yes | Shared knowledge base |
| `scripts/build-doc.sh` | Yes | Shared tooling |
| `templates/reference.docx` | Yes | Shared Word template |
| `projects/` | **No** | Client data, stays local |

---

## 9. CLAUDE.md Updates Required

The following protocol changes are needed in `CLAUDE.md`:

- Update **Source of Truth** path: `../project_context/` → `projects/<ProjectName>/_context/`
- Update **Output Destination** path: `../output/` → `projects/<ProjectName>/<phase>/`
- Add **New Project** protocol: interview → scaffold → inject domain defaults
- Add **Build Document** protocol: manifest resolution → Pandoc execution
- Add **Domain Injection** protocol: `[DOMAIN-DEFAULT]` tag usage

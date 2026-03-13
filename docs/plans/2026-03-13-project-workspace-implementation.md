# Project Workspace & Domain Knowledge Base Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Build a local `projects/` workspace (gitignored), a tracked `domains/` knowledge base, a Pandoc build script, and update CLAUDE.md protocols — so consultants can scaffold, generate, and export SDLC documents per client project.

**Architecture:** `projects/<ProjectName>/` holds all per-client work (untracked); `domains/<domain>/` holds shared domain knowledge (tracked); `scripts/build-doc.sh` stitches `.md` section files into `.docx` via Pandoc using a Word reference template; a new `00-meta-initialization` skill handles the new-project interview and scaffold.

**Tech Stack:** Bash, Pandoc, Markdown, CLAUDE.md protocol updates

**Design Doc:** `docs/plans/2026-03-13-project-workspace-structure-design.md`

---

## Task 1: Update `.gitignore`

**Files:**
- Modify: `.gitignore` (create if absent)

**Step 1: Check current `.gitignore`**

```bash
cat .gitignore 2>/dev/null || echo "File does not exist"
```

**Step 2: Add `projects/` entry**

Append to `.gitignore`:
```
# Client project workspaces — stays local, never committed
projects/
```

**Step 3: Verify**

```bash
git check-ignore -v projects/
```
Expected output: `.gitignore:X:projects/	projects/`

**Step 4: Commit**

```bash
git add .gitignore
git commit -m "chore: gitignore projects/ workspace directory"
```

---

## Task 2: Create `domains/` Master Index

**Files:**
- Create: `domains/INDEX.md`

**Step 1: Create the file**

```markdown
# Domains Index

Domain knowledge bases provide baseline requirements, regulations, architecture
patterns, and feature defaults for specific industry verticals. When a consultant
starts a new project and selects a domain, Claude reads from this knowledge base
to auto-inject `[DOMAIN-DEFAULT]` tagged requirements into the project scaffold.

## Available Domains

| Domain | Key Standards | Risk Level | Directory |
|---|---|---|---|
| Healthcare | HIPAA, HL7/FHIR, FDA 21 CFR | High | [healthcare/](healthcare/INDEX.md) |
| Finance | PCI-DSS, SOX, AML/KYC | High | [finance/](finance/INDEX.md) |
| Education | FERPA, COPPA | Medium | [education/](education/INDEX.md) |
| Retail | PCI-DSS, GDPR | Medium | [retail/](retail/INDEX.md) |
| Logistics | DOT, ISO 28000 | Medium | [logistics/](logistics/INDEX.md) |
| Government | FISMA, FedRAMP, GDPR | High | [government/](government/INDEX.md) |

## How Domain Injection Works

1. Consultant selects a domain when running "start a new project"
2. Claude reads `domains/<domain>/INDEX.md` and `references/nfr-defaults.md`
3. `[DOMAIN-DEFAULT]` tagged blocks are injected into relevant section stubs
4. `_context/domain.md` is pre-populated with the domain profile
5. Consultant reviews tagged blocks — keep, edit, or delete before building `.docx`

## Domain Injection Tag Format

```markdown
<!-- [DOMAIN-DEFAULT: healthcare] Source: domains/healthcare/references/nfr-defaults.md -->
#### NFR-HC-001: Requirement Title
The system shall...
<!-- [END DOMAIN-DEFAULT] -->
```

## Adding a New Domain

1. Create `domains/<domain-name>/` directory
2. Add `INDEX.md` following the format in any existing domain
3. Add `references/` subdirectory with: `regulations.md`, `architecture-patterns.md`, `security-baseline.md`, `nfr-defaults.md`
4. Add `features/` subdirectory with one `.md` per feature module
5. Register the domain in this `INDEX.md` table
```

**Step 2: Verify file exists**

```bash
ls domains/INDEX.md
```

**Step 3: Commit**

```bash
git add domains/INDEX.md
git commit -m "feat: add domains/ master index"
```

---

## Task 3: Scaffold Healthcare Domain

**Files:**
- Create: `domains/healthcare/INDEX.md`
- Create: `domains/healthcare/references/regulations.md`
- Create: `domains/healthcare/references/architecture-patterns.md`
- Create: `domains/healthcare/references/security-baseline.md`
- Create: `domains/healthcare/references/nfr-defaults.md`
- Create: `domains/healthcare/features/patient-management.md`
- Create: `domains/healthcare/features/appointment-scheduling.md`
- Create: `domains/healthcare/features/billing-claims.md`
- Create: `domains/healthcare/features/clinical-documentation.md`
- Create: `domains/healthcare/features/reporting-analytics.md`

**Step 1: Create `domains/healthcare/INDEX.md`**

```markdown
# Domain: Healthcare

## Profile

| Property | Value |
|---|---|
| **Regulatory Bodies** | HHS, FDA, CMS, ONC |
| **Key Standards** | HIPAA Privacy Rule, HIPAA Security Rule, HL7 FHIR R4, ICD-10, CPT, FDA 21 CFR Part 11 |
| **Risk Level** | High — PHI/PII data, patient safety implications |
| **Audit Requirement** | Mandatory — all PHI access must be logged |
| **Data Classification** | Protected Health Information (PHI), Personally Identifiable Information (PII) |

## Default Feature Modules

- Patient Management
- Appointment Scheduling
- Clinical Documentation
- Billing & Claims
- Reporting & Analytics

## Auto-Injected Requirements

See `references/nfr-defaults.md` for the full list of `[DOMAIN-DEFAULT]` requirements
injected into new healthcare projects at scaffold time.

Key injected areas:
- **NFR:** HIPAA audit logging, data encryption at rest/transit, access control
- **FR:** Patient consent management, data export (Right of Access)
- **Interfaces:** HL7/FHIR API endpoints, EHR integration hooks

## References

- [regulations.md](references/regulations.md) — HIPAA, HL7/FHIR, FDA, CMS
- [architecture-patterns.md](references/architecture-patterns.md) — PHI isolation, audit logging, multi-tenant
- [security-baseline.md](references/security-baseline.md) — encryption, access control, PHI handling
- [nfr-defaults.md](references/nfr-defaults.md) — default non-functional requirements for injection

## Feature Reference

- [patient-management.md](features/patient-management.md)
- [appointment-scheduling.md](features/appointment-scheduling.md)
- [billing-claims.md](features/billing-claims.md)
- [clinical-documentation.md](features/clinical-documentation.md)
- [reporting-analytics.md](features/reporting-analytics.md)
```

**Step 2: Create `domains/healthcare/references/regulations.md`**

```markdown
# Healthcare: Regulations & Standards Reference

## HIPAA (Health Insurance Portability and Accountability Act)

| Rule | Citation | Requirement |
|---|---|---|
| Privacy Rule | 45 CFR §164.500–534 | Governs use and disclosure of PHI |
| Security Rule | 45 CFR §164.300–318 | Safeguards for electronic PHI (ePHI) |
| Breach Notification | 45 CFR §164.400–414 | 60-day breach notification requirement |
| Minimum Necessary | 45 CFR §164.502(b) | Limit PHI access to minimum necessary |

### Key HIPAA Technical Safeguards (§164.312)

- **Access Control (§164.312(a)):** Unique user identification, automatic logoff, encryption/decryption
- **Audit Controls (§164.312(b)):** Hardware/software activity recording on systems containing ePHI
- **Integrity (§164.312(c)):** Protect ePHI from improper alteration or destruction
- **Transmission Security (§164.312(e)):** Encryption of ePHI in transit

## HL7 FHIR R4 (Fast Healthcare Interoperability Resources)

- **Standard:** HL7 FHIR Release 4 (4.0.1)
- **Use:** RESTful API for healthcare data exchange
- **Key Resources:** Patient, Practitioner, Encounter, Observation, Condition, MedicationRequest
- **Auth:** SMART on FHIR (OAuth 2.0 + OpenID Connect)
- **Reference:** https://hl7.org/fhir/R4/

## FDA 21 CFR Part 11

- Applies to electronic records and electronic signatures
- Requires audit trails, user authentication, system validation
- Relevant for clinical trial software, FDA-regulated medical devices

## ICD-10 / CPT Coding

- **ICD-10-CM:** Diagnosis codes (68,000+ codes)
- **CPT:** Procedure codes (American Medical Association)
- Must support annual code updates (effective October 1 each year for ICD-10)

## CMS Requirements

- **Medicare/Medicaid:** Must support CMS billing formats (ANSI X12 837)
- **CLIA:** Clinical Laboratory Improvement Amendments for lab result handling
```

**Step 3: Create `domains/healthcare/references/architecture-patterns.md`**

```markdown
# Healthcare: Architecture Patterns

## PHI Data Isolation

- Store PHI in dedicated, encrypted database schema or separate DB
- Never log PHI in application logs — log record IDs only
- Implement field-level encryption for SSN, DOB, diagnosis codes
- Use data masking in non-production environments

## Audit Logging Architecture

Every PHI access event must produce an immutable log entry:

```json
{
  "event_id": "uuid",
  "timestamp": "ISO-8601",
  "user_id": "string",
  "user_role": "string",
  "action": "READ | WRITE | DELETE | EXPORT",
  "resource_type": "Patient | Encounter | ...",
  "resource_id": "string",
  "ip_address": "string",
  "session_id": "string",
  "outcome": "SUCCESS | FAILURE"
}
```

Audit logs must be:
- Write-once (no UPDATE/DELETE operations permitted)
- Retained for minimum 6 years (HIPAA)
- Queryable by patient ID, user ID, date range

## Multi-Tenant PHI Isolation

- Each tenant (hospital/clinic) must have strictly isolated PHI
- Row-level security or schema-per-tenant depending on scale
- Cross-tenant queries must be architecturally impossible
- Tenant ID must be validated on every query, not just at login

## Role-Based Access Control (RBAC)

Minimum roles required:
- **Patient:** Own records only
- **Clinician:** Assigned patients + emergency override
- **Admin:** Administrative data, no clinical notes
- **Billing:** Billing data only, masked clinical info
- **Auditor:** Read-only audit logs
- **Super Admin:** System config, no PHI access

## Emergency Access ("Break-Glass")

- Clinicians must be able to access any patient record in emergencies
- All break-glass accesses must trigger immediate notification to Privacy Officer
- Require post-access justification within 24 hours

## API Design

- All FHIR endpoints must support OAuth 2.0 / SMART on FHIR
- Rate limiting on all patient data endpoints
- Response must never include PHI in error messages
- Support `_elements` parameter to limit PHI in responses
```

**Step 4: Create `domains/healthcare/references/security-baseline.md`**

```markdown
# Healthcare: Security Baseline

## Encryption Standards

| Data State | Standard | Minimum Key Length |
|---|---|---|
| At Rest | AES-256-GCM | 256-bit |
| In Transit | TLS 1.2+ | — |
| Database fields (PHI) | AES-256 field-level | 256-bit |
| Backups | AES-256 | 256-bit |

## Authentication Requirements

- Multi-Factor Authentication (MFA) mandatory for all clinical staff
- Session timeout: 15 minutes inactivity for clinical workstations
- Password policy: minimum 12 characters, complexity requirements
- Account lockout: 5 failed attempts → 30-minute lockout
- Privileged accounts require hardware token (FIDO2/WebAuthn)

## Access Control Baseline

- Principle of least privilege on all roles
- Access reviews every 90 days
- Immediate access revocation on staff termination (< 1 hour SLA)
- Shared accounts prohibited
- Service accounts must have minimal scoped permissions

## Network Security

- PHI systems must reside in private subnets
- No direct internet access to database tier
- WAF required on all public-facing endpoints
- Network segmentation between clinical and administrative systems
- VPN required for remote administrative access

## Vulnerability Management

- Critical patches: 72 hours
- High patches: 30 days
- Penetration testing: annually minimum
- OWASP Top 10 compliance required

## Business Continuity

- RTO (Recovery Time Objective): ≤ 4 hours for clinical systems
- RPO (Recovery Point Objective): ≤ 1 hour for PHI data
- Backup testing: quarterly
- DR failover testing: annually
```

**Step 5: Create `domains/healthcare/references/nfr-defaults.md`**

```markdown
# Healthcare: Default Non-Functional Requirements

These requirements are auto-injected into new healthcare project scaffolds.
All blocks are tagged `[DOMAIN-DEFAULT: healthcare]` for consultant review.

---

<!-- [DOMAIN-DEFAULT: healthcare] Source: domains/healthcare/references/nfr-defaults.md -->
#### NFR-HC-001: PHI Audit Trail
The system shall maintain a complete, tamper-proof audit log of all create,
read, update, and delete operations on Protected Health Information (PHI) in
compliance with HIPAA Security Rule 45 CFR §164.312(b).

**Verifiability:** Execute a read operation on a patient record; verify that an
immutable log entry is created containing: user_id, timestamp, action, resource_id,
and outcome. Attempt to modify the log entry; the system shall reject the modification.
<!-- [END DOMAIN-DEFAULT] -->

---

<!-- [DOMAIN-DEFAULT: healthcare] Source: domains/healthcare/references/nfr-defaults.md -->
#### NFR-HC-002: Data Encryption at Rest
The system shall encrypt all PHI stored in the database using AES-256-GCM.
Unencrypted PHI shall not exist on any persistent storage medium.

**Verifiability:** Inspect raw database storage; PHI fields must be unreadable
without the encryption key. Key management must follow NIST SP 800-57.
<!-- [END DOMAIN-DEFAULT] -->

---

<!-- [DOMAIN-DEFAULT: healthcare] Source: domains/healthcare/references/nfr-defaults.md -->
#### NFR-HC-003: Data Encryption in Transit
All transmission of PHI shall use TLS 1.2 or higher. TLS 1.0 and 1.1 shall
be disabled on all endpoints.

**Verifiability:** Run `nmap --script ssl-enum-ciphers` against all endpoints;
verify TLS 1.0/1.1 returns no supported ciphers.
<!-- [END DOMAIN-DEFAULT] -->

---

<!-- [DOMAIN-DEFAULT: healthcare] Source: domains/healthcare/references/nfr-defaults.md -->
#### NFR-HC-004: Session Timeout
The system shall automatically terminate inactive clinical user sessions after
15 minutes of inactivity, requiring re-authentication to resume.

**Verifiability:** Authenticate as a clinical user; remain idle for 15 minutes;
attempt any action — the system shall redirect to the login screen.
<!-- [END DOMAIN-DEFAULT] -->

---

<!-- [DOMAIN-DEFAULT: healthcare] Source: domains/healthcare/references/nfr-defaults.md -->
#### NFR-HC-005: Multi-Factor Authentication
The system shall require Multi-Factor Authentication (MFA) for all users with
access to PHI, in compliance with HIPAA Security Rule 45 CFR §164.312(d).

**Verifiability:** Attempt login with valid credentials only; the system shall
not grant access without a valid second factor.
<!-- [END DOMAIN-DEFAULT] -->

---

<!-- [DOMAIN-DEFAULT: healthcare] Source: domains/healthcare/references/nfr-defaults.md -->
#### NFR-HC-006: Availability for Clinical Systems
The system shall maintain 99.9% uptime availability ($\leq 8.76$ hours downtime
per year) for all clinical-facing modules, measured monthly.

**Verifiability:** Monitor uptime over 30 days; calculated as:
$Availability = \frac{MTTF}{MTTF + MTTR} \times 100\%$
<!-- [END DOMAIN-DEFAULT] -->

---

<!-- [DOMAIN-DEFAULT: healthcare] Source: domains/healthcare/references/nfr-defaults.md -->
#### NFR-HC-007: Data Retention
The system shall retain patient records and associated audit logs for a minimum
of 6 years from the date of creation or last access, in compliance with HIPAA
45 CFR §164.530(j).

**Verifiability:** Attempt to delete a PHI record less than 6 years old; the
system shall reject the deletion and return an appropriate error.
<!-- [END DOMAIN-DEFAULT] -->

---

<!-- [DOMAIN-DEFAULT: healthcare] Source: domains/healthcare/references/nfr-defaults.md -->
#### NFR-HC-008: Breach Notification Capability
The system shall provide tooling to identify and report all PHI records affected
by a security breach within 60 days, in compliance with HIPAA Breach Notification
Rule 45 CFR §164.412.

**Verifiability:** Given a simulated breach event (compromised user account),
the system shall produce a report of all PHI accessed by that account within
the breach window, within 4 hours of query execution.
<!-- [END DOMAIN-DEFAULT] -->
```

**Step 6: Create feature files (create each as a brief stub)**

`domains/healthcare/features/patient-management.md`:
```markdown
# Feature: Patient Management

## Description
Core patient record management — demographics, identifiers, contact info,
insurance, emergency contacts, and consent records.

## Standard Capabilities
- Patient registration and demographic capture
- MRN (Medical Record Number) generation
- Insurance eligibility verification
- Patient consent management (HIPAA authorizations)
- Duplicate patient detection and merge
- Patient search (name, DOB, MRN, SSN last-4)
- Patient portal access management

## Regulatory Hooks
- HIPAA Right of Access: patients must be able to export their records
- HIPAA Minimum Necessary: search results must not expose unnecessary PHI
- ONC 21st Century Cures: prohibits information blocking

## Linked NFRs
- NFR-HC-001 (Audit Trail)
- NFR-HC-002 (Encryption at Rest)
- NFR-HC-005 (MFA)
```

Create similar stubs for:
- `appointment-scheduling.md` — scheduling, slots, reminders, cancellations, waitlists
- `billing-claims.md` — charge capture, ICD-10/CPT coding, CMS 1500, ERA/EOB processing
- `clinical-documentation.md` — SOAP notes, e-prescribing, problem lists, allergies
- `reporting-analytics.md` — quality measures, census reports, HEDIS, audit reports

**Step 7: Verify structure**

```bash
find domains/healthcare -type f | sort
```

Expected: 10 files (INDEX.md + 4 references + 5 features)

**Step 8: Commit**

```bash
git add domains/healthcare/
git commit -m "feat: add healthcare domain knowledge base with NFR defaults"
```

---

## Task 4: Scaffold Remaining 5 Domains (Stubs)

**Files:**
- Create: `domains/finance/INDEX.md` + `references/` + `features/`
- Create: `domains/education/INDEX.md` + `references/` + `features/`
- Create: `domains/retail/INDEX.md` + `references/` + `features/`
- Create: `domains/logistics/INDEX.md` + `references/` + `features/`
- Create: `domains/government/INDEX.md` + `references/` + `features/`

For each domain, follow the same pattern as Task 3. Each domain needs:

**`INDEX.md`** with profile table, default features, references list.

**`references/regulations.md`** with key standards:
- Finance: PCI-DSS v4.0, SOX Section 302/404, AML (BSA), KYC (FinCEN), Basel III
- Education: FERPA (20 U.S.C. §1232g), COPPA (under-13 data), WCAG 2.1 AA accessibility
- Retail: PCI-DSS v4.0, GDPR Article 17 (right to erasure), CCPA, consumer protection laws
- Logistics: DOT FMCSA regulations, ISO 28000 supply chain security, IATA (air freight)
- Government: FISMA (NIST SP 800-53), FedRAMP, Section 508 accessibility, GDPR/local data sovereignty

**`references/nfr-defaults.md`** with 4–6 `[DOMAIN-DEFAULT]` tagged requirements each.

**`references/architecture-patterns.md`** and **`references/security-baseline.md`** with domain-specific patterns.

**`features/`** with 4–5 feature stub files per domain.

**Commit after each domain:**

```bash
git add domains/finance/
git commit -m "feat: add finance domain knowledge base"
# repeat for education, retail, logistics, government
```

---

## Task 5: Create Pandoc Build Script

**Files:**
- Create: `scripts/build-doc.sh`

**Step 1: Create the script**

```bash
#!/usr/bin/env bash
# build-doc.sh — Stitch markdown section files and export to .docx via Pandoc
#
# Usage:
#   ./scripts/build-doc.sh <doc-dir> <output-name>
#
# Examples:
#   ./scripts/build-doc.sh projects/Livecare/02-requirements-engineering/01-srs SRS_Draft
#   ./scripts/build-doc.sh projects/Livecare/01-strategic-vision/01-prd PRD
#
# manifest.md format (optional, place in <doc-dir>):
#   List one filename per line. Lines starting with # are comments (excluded).
#   If absent, all *.md files in <doc-dir> are used, sorted alphabetically.

set -euo pipefail

DOC_DIR="${1:?Usage: build-doc.sh <doc-dir> <output-name>}"
OUTPUT_NAME="${2:?Usage: build-doc.sh <doc-dir> <output-name>}"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TEMPLATE="$SCRIPT_DIR/../templates/reference.docx"
PHASE_DIR="$(dirname "$DOC_DIR")"
OUTPUT_FILE="$PHASE_DIR/$OUTPUT_NAME.docx"

# Validate inputs
if [ ! -d "$DOC_DIR" ]; then
  echo "ERROR: Document directory not found: $DOC_DIR" >&2
  exit 1
fi

if [ ! -f "$TEMPLATE" ]; then
  echo "ERROR: Reference template not found: $TEMPLATE" >&2
  echo "  Place a styled Word document at: $TEMPLATE" >&2
  exit 1
fi

# Resolve file list
if [ -f "$DOC_DIR/manifest.md" ]; then
  echo "Using manifest: $DOC_DIR/manifest.md"
  FILES=$(grep -v '^\s*#' "$DOC_DIR/manifest.md" | grep '\.md$' | sed "s|^|$DOC_DIR/|")
else
  echo "No manifest found — using alphabetical sort of *.md files"
  FILES=$(ls "$DOC_DIR"/*.md 2>/dev/null | grep -v 'manifest.md' | sort)
fi

if [ -z "$FILES" ]; then
  echo "ERROR: No .md files found in $DOC_DIR" >&2
  exit 1
fi

# Report what will be stitched
echo ""
echo "Stitching files:"
echo "$FILES" | while read -r f; do echo "  + $(basename "$f")"; done
echo ""

# Build
pandoc $FILES \
  --reference-doc="$TEMPLATE" \
  --table-of-contents \
  --toc-depth=3 \
  -o "$OUTPUT_FILE"

echo "Built: $OUTPUT_FILE"
```

**Step 2: Make executable**

```bash
chmod +x scripts/build-doc.sh
```

**Step 3: Test with a dry run (no real project needed)**

```bash
# Verify pandoc is available
pandoc --version | head -1
```

Expected: `pandoc X.XX` (any version ≥ 2.x)

**Step 4: Commit**

```bash
git add scripts/build-doc.sh
git commit -m "feat: add pandoc build script for md-to-docx stitching"
```

---

## Task 6: Create Word Reference Template Placeholder

**Files:**
- Create: `templates/README.md`
- Create: `templates/.gitkeep`

**Step 1: Create `templates/README.md`**

```markdown
# Templates

## reference.docx

This directory must contain `reference.docx` — a styled Microsoft Word document
used by Pandoc as the style reference for all generated `.docx` output.

### Setup (one-time, per consultant machine)

1. Create or obtain a Word document with your organisation's styles defined:
   - **Heading 1, 2, 3** — document section headings
   - **Normal** — body text (font, size, line spacing)
   - **Table** — table style
   - **Code** — monospace for code blocks
   - **Title, Subtitle** — cover page styles

2. Save it as `templates/reference.docx` in this repository root

3. `templates/reference.docx` is gitignored — each consultant uses their own
   branded template. A generic fallback is used if the file is absent.

### Gitignore Note

`reference.docx` is excluded from git (binary file, org-specific branding).
Only `templates/README.md` is committed.

### Pandoc Reference Doc Documentation

https://pandoc.org/MANUAL.html#option--reference-doc
```

**Step 2: Add `reference.docx` to `.gitignore`**

Append to `.gitignore`:
```
# Word template — binary, org-specific, stays local
templates/reference.docx
```

**Step 3: Commit**

```bash
git add templates/README.md templates/.gitkeep .gitignore
git commit -m "feat: add templates/ directory with reference.docx setup guide"
```

---

## Task 7: Create New-Project Scaffolding Skill

**Files:**
- Create: `00-meta-initialization/new-project/SKILL.md`

**Step 1: Create the skill**

```markdown
# Skill: New Project Scaffold

## Trigger
User says any of: "start a new project", "create a new project",
"scaffold a project", "new client project", "initialize project"

## Purpose
Interview the consultant, scaffold the full project workspace under `projects/`,
pre-populate `_context/` files, and inject domain defaults.

---

## Interview Protocol

Ask these questions ONE AT A TIME. Do not ask the next until the previous is answered.

**Q1:** What is the project name? (This becomes the directory name — use hyphens,
e.g., `Livecare-Hospital-ERP`)

**Q2:** In 2–3 sentences, what does this software do and what problem does it solve?
(This pre-populates `_context/vision.md`)

**Q3:** Which methodology best fits this project?
- A) **Waterfall** — regulated industry, fixed scope, formal IEEE 830 SRS required
- B) **Agile** — iterative delivery, user stories, Scrum/Kanban
- C) **Hybrid** — formal SRS for backend/core + agile user stories for frontend/features

**Q4:** What is the primary domain?
- A) Healthcare  B) Finance  C) Education
- D) Retail  E) Logistics  F) Government  G) Other (describe)

**Q5:** Who is the project owner / primary client contact name?

---

## Scaffold Actions

After the interview, Claude performs these actions in order:

### 1. Create project root
`projects/<ProjectName>/`

### 2. Create `_context/` files

**`_context/vision.md`** — pre-populate with Q2 answer:
```markdown
# Project Vision

**Project:** <ProjectName>
**Client Contact:** <Q5 answer>
**Date:** <today>

## Problem Statement
<Q2 answer>

## Goals
<!-- TODO: List 3–5 measurable project goals -->

## Stakeholders
<!-- TODO: List stakeholder roles and their primary needs -->

## Success Criteria
<!-- TODO: Define how project success will be measured -->
```

**`_context/features.md`** — stub with guidance:
```markdown
# Feature List

<!-- TODO: List all features with a brief description each.
Format:
## Feature Name
Brief description of what this feature does and the business value it delivers.
-->
```

**`_context/tech_stack.md`**, **`_context/business_rules.md`**,
**`_context/quality_standards.md`**, **`_context/glossary.md`** —
create as guided stubs with `<!-- TODO: ... -->` prompts.

**`_context/domain.md`** — copy content from `domains/<domain>/INDEX.md`
and prepend:
```markdown
# Domain Profile: <DomainName>
> Auto-populated from domains/<domain>/INDEX.md at scaffold time.
> Review and remove sections not applicable to this project.
```

### 3. Create Phase Directories

Create all 9 phase directories with document subdirectories:

**Waterfall methodology** — create all document dirs across all phases.
**Agile methodology** — skip `01-srs/` in Phase 02; create `02-user-stories/` instead.
**Hybrid** — create both `01-srs/` and `02-user-stories/` in Phase 02.

Phase directory → document subdirectories mapping:

```
01-strategic-vision/       → 01-prd/, 02-vision-statement/, 03-business-case/
02-requirements-engineering/ → 01-srs/ and/or 02-user-stories/, 03-stakeholder-analysis/
03-design-documentation/   → 01-hld/, 02-lld/, 03-api-spec/, 04-database-design/, 05-ux-spec/
04-development-artifacts/  → 01-technical-spec/, 02-coding-guidelines/
05-testing-documentation/  → 01-test-strategy/, 02-test-plan/, 03-test-report/
06-deployment-operations/  → 01-deployment-guide/, 02-runbook/
07-agile-artifacts/        → 01-sprint-planning/, 02-dod/, 03-dor/
08-end-user-documentation/ → 01-user-manual/, 02-installation-guide/, 03-faq/
09-governance-compliance/  → 01-traceability-matrix/, 02-audit-report/, 03-compliance/, 04-risk-assessment/
```

### 4. Inject Domain Defaults

Read `domains/<domain>/references/nfr-defaults.md`.
Copy `[DOMAIN-DEFAULT]` blocks into:
- `02-requirements-engineering/01-srs/06-nfr.md` (waterfall)
- `02-requirements-engineering/02-user-stories/01-epics.md` (agile, as tagged notes)

### 5. Print Scaffold Summary

```
Project scaffolded: projects/<ProjectName>/

_context/ status:
  ✓ vision.md           — pre-populated from interview
  ✓ domain.md           — <domain> baseline injected
  ○ features.md         — TODO: add feature list
  ○ tech_stack.md       — TODO: specify technologies
  ○ business_rules.md   — TODO: define business rules
  ○ quality_standards.md — TODO: set quality targets
  ○ glossary.md         — TODO: add project terminology

Domain defaults injected: <N> [DOMAIN-DEFAULT] requirements in 06-nfr.md

Next step: Fill in _context/ files, then say:
  "generate PRD for <ProjectName>"
  "generate SRS for <ProjectName>"
```

---

## Build Document Protocol

When user says "build the [document]" (e.g., "build the SRS", "build the PRD"):

1. Resolve the document directory from the document name
2. Check for `manifest.md` — if present use it; otherwise sort `*.md` by filename
3. Run: `bash scripts/build-doc.sh <doc-dir> <OutputName>`
4. Report the output path

### Document Name → Directory Mapping

| User says | Directory | Output filename |
|---|---|---|
| "build the PRD" | `01-strategic-vision/01-prd/` | `PRD.docx` |
| "build the SRS" | `02-requirements-engineering/01-srs/` | `SRS_Draft.docx` |
| "build the HLD" | `03-design-documentation/01-hld/` | `HLD.docx` |
| "build the test plan" | `05-testing-documentation/02-test-plan/` | `TestPlan.docx` |
| "build the user manual" | `08-end-user-documentation/01-user-manual/` | `UserManual.docx` |
| "build the risk assessment" | `09-governance-compliance/04-risk-assessment/` | `RiskAssessment.docx` |
```

**Step 2: Verify file**

```bash
ls 00-meta-initialization/new-project/SKILL.md
wc -l 00-meta-initialization/new-project/SKILL.md
```

Expected: file exists, line count < 500

**Step 3: Commit**

```bash
git add 00-meta-initialization/new-project/SKILL.md
git commit -m "feat: add new-project scaffold skill with interview + domain injection"
```

---

## Task 8: Update `CLAUDE.md`

**Files:**
- Modify: `CLAUDE.md`

**Step 1: Update the following sections in CLAUDE.md**

Replace the **Directory Logic & Pathing** section:

```markdown
## Directory Logic & Pathing

- **Submodule Root:** This directory (where `README.md` and phase folders live).
- **Internal Tools:** Located in `/skills/`. Use these internal skills to help author
  or refine the main SRS generation skills.
- **Domain Knowledge:** Located in `/domains/`. Read the relevant domain INDEX.md
  when generating requirements for a domain-specific project.
- **Project Workspace:** Located in `projects/<ProjectName>/` (untracked, gitignored).
  All client documentation is built here.
- **Context Source of Truth:** Read all project-specific data from
  `projects/<ProjectName>/_context/`.
- **Output Destination:** Write all generated section files to
  `projects/<ProjectName>/<phase>/<document>/`. Write final `.docx` files to
  `projects/<ProjectName>/<phase>/`.
- **Templates:** `templates/reference.docx` is the Pandoc Word style reference.
- **Build Script:** `scripts/build-doc.sh` stitches `.md` files into `.docx`.
```

Add a new **New Project Protocol** section after Directory Logic:

```markdown
## New Project Protocol

When the user says "start a new project" or equivalent:
1. Run the interview in `00-meta-initialization/new-project/SKILL.md` — one question at a time
2. Scaffold the full directory structure under `projects/<ProjectName>/`
3. Pre-populate `_context/` files with interview answers and guided TODO prompts
4. Read `domains/<domain>/INDEX.md` and inject `[DOMAIN-DEFAULT]` blocks from
   `domains/<domain>/references/nfr-defaults.md` into the appropriate section stubs
5. Print a scaffold summary showing pre-populated files and outstanding TODOs

## Build Document Protocol

When the user says "build the [document]":
1. Resolve the document directory using the mapping in the new-project SKILL.md
2. Check for `manifest.md` in the document directory — use it if present, otherwise
   sort all `*.md` files (excluding `manifest.md`) alphabetically
3. Execute: `bash scripts/build-doc.sh <doc-dir> <OutputName>`
4. Report the output `.docx` path to the user

## Domain Injection Protocol

`[DOMAIN-DEFAULT]` tagged blocks are pre-populated at scaffold time. They are:
- Clearly marked with opening and closing comment tags
- Sourced from `domains/<domain>/references/nfr-defaults.md`
- Reviewed and either kept, edited, or deleted by the consultant before building
- Never silently removed by Claude — only the consultant removes them
```

**Step 2: Verify CLAUDE.md line count stays under 500**

```bash
wc -l CLAUDE.md
```

If over 500, condense the V&V SOP section using concise bullet points.

**Step 3: Commit**

```bash
git add CLAUDE.md
git commit -m "docs: update CLAUDE.md for projects/ workspace and domains/ protocols"
```

---

## Task 9: Update `README.md`

**Files:**
- Modify: `README.md`

**Step 1: Add `domains/` to the Repository Structure section**

In the `## 🗂 Repository Structure` code block, add after `01-strategic-vision/`:

```
├── domains/                         # Domain knowledge bases (healthcare, finance, etc.)
│   ├── INDEX.md
│   ├── healthcare/                  # HIPAA, HL7/FHIR, NFR defaults
│   ├── finance/                     # PCI-DSS, SOX, AML
│   ├── education/                   # FERPA, COPPA
│   ├── retail/                      # PCI-DSS, GDPR
│   ├── logistics/                   # DOT, ISO 28000
│   └── government/                  # FISMA, FedRAMP
├── projects/                        # [UNTRACKED] Per-client project workspaces
│   └── <ProjectName>/
│       ├── _context/                # Project inputs (vision, features, tech stack)
│       └── 01-09-<phases>/          # Generated section files + .docx output
├── scripts/
│   └── build-doc.sh                 # Pandoc: stitch .md sections → .docx
├── templates/
│   └── reference.docx               # [LOCAL ONLY] Word style template
```

**Step 2: Add a Quick Start section for new projects**

Add under `## 🚀 Integration & Workflow`:

```markdown
### Starting a New Client Project

Tell Claude: **"start a new project"**

Claude will:
1. Ask 5 quick questions (project name, description, methodology, domain, owner)
2. Scaffold `projects/<ProjectName>/` with all 9 phase directories
3. Pre-populate `_context/` with your answers
4. Inject domain-default requirements tagged `[DOMAIN-DEFAULT]`

Then fill in remaining `_context/` files and say:
**"generate PRD for <ProjectName>"** or **"generate SRS for <ProjectName>"**

To export a finished document to Word:
**"build the SRS"** → outputs `SRS_Draft.docx` in the phase directory
```

**Step 3: Commit**

```bash
git add README.md
git commit -m "docs: update README with domains/ and projects/ workspace documentation"
```

---

## Task 10: Smoke Test End-to-End

**Step 1: Verify full structure**

```bash
find domains/ -type f | sort
ls scripts/
ls templates/
ls 00-meta-initialization/new-project/
```

**Step 2: Verify gitignore works**

```bash
mkdir -p projects/Test-Project/_context
echo "test" > projects/Test-Project/_context/vision.md
git status
```

Expected: `projects/` does NOT appear in git status (correctly gitignored)

**Step 3: Verify build script syntax**

```bash
bash -n scripts/build-doc.sh
echo "Syntax OK: $?"
```

Expected: `Syntax OK: 0`

**Step 4: Clean up test project**

```bash
rm -rf projects/Test-Project
```

**Step 5: Final commit**

```bash
git add -A
git status  # should show nothing new to commit
```

---

## Summary

| Task | Deliverable | Commit |
|---|---|---|
| 1 | `.gitignore` updated | `chore: gitignore projects/` |
| 2 | `domains/INDEX.md` | `feat: add domains/ master index` |
| 3 | Full healthcare domain | `feat: add healthcare domain knowledge base` |
| 4 | 5 remaining domain stubs | `feat: add finance/education/retail/logistics/government domains` |
| 5 | `scripts/build-doc.sh` | `feat: add pandoc build script` |
| 6 | `templates/` directory | `feat: add templates/ directory` |
| 7 | New-project scaffold skill | `feat: add new-project scaffold skill` |
| 8 | `CLAUDE.md` updated | `docs: update CLAUDE.md protocols` |
| 9 | `README.md` updated | `docs: update README` |
| 10 | Smoke test | — |

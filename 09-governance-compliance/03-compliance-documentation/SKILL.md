---
name: Compliance Documentation
description: Generate compliance documentation mapping project requirements and architecture to applicable regulatory frameworks including GDPR, HIPAA, and SOC2.
---

# Compliance Documentation Skill

## Overview

This skill generates regulatory compliance documentation that maps project requirements, data handling practices, and architectural decisions to applicable regulatory frameworks. The skill assesses applicability of GDPR, HIPAA, and SOC2, then produces detailed compliance mappings, gap analyses, and remediation roadmaps for each applicable framework. Only frameworks relevant to the project's domain and data classification are included.

## When to Use This Skill

- When the project handles personal data subject to GDPR
- When the project processes protected health information (PHI) under HIPAA
- When the project requires SOC2 attestation for service organization controls
- When stakeholders or clients require evidence of regulatory compliance posture
- When preparing for regulatory audits or third-party assessments
- When onboarding into regulated industries (healthcare, finance, government)

## Quick Reference

| Attribute | Value |
|-----------|-------|
| **Input** | vision.md, quality_standards.md, SRS_Draft.md, HLD.md |
| **Output** | Compliance_Docs.md |
| **Standard** | GDPR, HIPAA, SOC2 |
| **Estimated Time** | 20-35 minutes |

## Input Files

| File | Purpose | Required? |
|------|---------|-----------|
| `../project_context/vision.md` | Project scope, domain, and data subjects to determine regulatory applicability | Yes |
| `../project_context/quality_standards.md` | Security and compliance requirements specified by stakeholders | No |
| `../output/SRS_Draft.md` | Requirements referencing data handling, authentication, and access control | No |
| `../output/HLD.md` | Architecture decisions affecting data flow, storage, and transmission | No |

## Output Files

| File | Description |
|------|-------------|
| `../output/Compliance_Docs.md` | Complete compliance documentation with applicability assessment and gap analysis |

## Core Instructions

1. The skill SHALL read `../project_context/vision.md` to determine the project domain, target users, data subjects, and geographic scope. If the file is missing, halt execution and report the error.

2. The skill SHALL perform a Regulatory Applicability Assessment, determining which frameworks apply based on:
   - **GDPR:** Project processes personal data of EU/EEA residents
   - **HIPAA:** Project processes protected health information in a US healthcare context
   - **SOC2:** Project operates as a service organization handling client data

3. The skill SHALL classify all data elements identified in the project into categories: Public, Internal, Confidential, Restricted (or PII, PHI, PCI as applicable).

4. For each applicable framework, the skill SHALL generate a dedicated compliance section:
   - **GDPR:** Lawful basis for processing, data subject rights implementation, Data Protection Impact Assessment (DPIA) triggers, data retention policies, cross-border transfer mechanisms
   - **HIPAA:** PHI identification, administrative/physical/technical safeguards, Business Associate Agreement (BAA) requirements, minimum necessary standard
   - **SOC2:** Trust Service Criteria mapping (Security, Availability, Processing Integrity, Confidentiality, Privacy)

5. The skill SHALL map security controls from the project architecture to regulatory requirements, identifying which controls satisfy which obligations.

6. The skill SHALL generate a Compliance Gap Analysis identifying obligations without corresponding controls or requirements.

7. The skill SHALL produce a Remediation Roadmap prioritizing compliance gaps by risk severity and regulatory deadline pressure.

8. The skill SHALL explicitly state when a framework is determined to be not applicable, with justification.

9. The skill SHALL avoid speculative compliance claims -- if insufficient information exists to assess a control, flag it as `[ASSESSMENT-PENDING]` rather than assuming compliance.

## Output Format Specification

The generated `Compliance_Docs.md` SHALL contain the following sections:

```
# Compliance Documentation
## 1. Document Information
## 2. Regulatory Applicability Assessment
## 3. Data Classification
## 4. GDPR Compliance (if applicable)
### 4.1 Lawful Basis for Processing
### 4.2 Data Subject Rights
### 4.3 Data Protection Impact Assessment
### 4.4 Data Retention & Deletion
### 4.5 Cross-Border Transfers
## 5. HIPAA Compliance (if applicable)
### 5.1 PHI Identification
### 5.2 Administrative Safeguards
### 5.3 Physical Safeguards
### 5.4 Technical Safeguards
### 5.5 BAA Requirements
## 6. SOC2 Compliance (if applicable)
### 6.1 Security Criteria
### 6.2 Availability Criteria
### 6.3 Processing Integrity Criteria
### 6.4 Confidentiality Criteria
### 6.5 Privacy Criteria
## 7. Security Controls Mapping
## 8. Compliance Gap Analysis
## 9. Remediation Roadmap
## 10. Revision History
```

## Common Pitfalls

- Assuming all three frameworks apply without performing applicability assessment
- Making definitive compliance claims without sufficient architectural evidence
- Omitting data classification, which is the foundation for all compliance mapping
- Treating compliance as binary (compliant/non-compliant) without recognizing partial compliance states
- Ignoring cross-framework overlaps (e.g., GDPR and HIPAA both require access controls)
- Generating boilerplate compliance text that is not grounded in the actual project context

## Verification Checklist

1. Regulatory applicability is assessed and justified for each framework.
2. Data classification covers all data elements identified in the project.
3. Each applicable framework has a dedicated section with specific, grounded controls.
4. Non-applicable frameworks are explicitly excluded with justification.
5. Security controls are mapped to specific regulatory obligations.
6. Compliance gaps are identified with severity and remediation priority.
7. No speculative compliance claims exist -- uncertain items are tagged `[ASSESSMENT-PENDING]`.
8. The remediation roadmap is prioritized by risk and regulatory urgency.

## Integration

- **Upstream:** Consumes vision and quality standards from project context, and SRS/design artifacts from prior phases. Benefits from 02-audit-report findings.
- **Downstream:** Feeds external regulatory submissions and audit processes. Informs 04-risk-assessment compliance risk category.

## Standards Compliance

| Standard | Governs |
|----------|---------|
| GDPR (EU 2016/679) | Personal data processing, data subject rights, cross-border transfers |
| HIPAA (45 CFR Parts 160, 164) | Protected health information safeguards and BAA requirements |
| SOC2 (AICPA TSC) | Trust Service Criteria for service organizations |

## Resources

- GDPR: Regulation (EU) 2016/679 of the European Parliament
- HIPAA: 45 CFR Parts 160 and 164, HHS Security Rule Guidance
- AICPA: Trust Services Criteria (SOC2)
- CLAUDE.md: Project-level quality and compliance constraints

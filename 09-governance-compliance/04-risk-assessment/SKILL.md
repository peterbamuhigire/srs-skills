---
name: "Risk Assessment"
description: "Generate a systematic risk assessment identifying technical, operational, compliance, and project risks with probability/impact scoring and mitigation strategies per ISO 31000 and IEEE 1012."
metadata:
  use_when: "Use when the task matches risk assessment skill and this skill's local workflow."
  do_not_use_when: "Do not use when a more specific upstream or downstream skill owns the task, or when the required project context has not been prepared."
  required_inputs: "Provide the target project or document, the relevant context files, scope constraints, and any domain or standards inputs referenced here."
  workflow: "Follow the ordered steps, review gates, and local generation logic in this file before consulting deeper support files as needed."
  quality_standards: "Keep outputs grounded in source context, traceable to stated standards, and specific enough to review or verify."
  anti_patterns: "Do not fabricate missing requirements, skip human review gates, or substitute vague prose for verifiable documentation."
  outputs: "Produce or update the document, scaffold, analysis, or phase artifact that this skill defines."
  references: "Use `README.md`, `logic.prompt` when deeper detail is needed."
---

# Risk Assessment Skill

## Overview

This skill generates a systematic risk assessment that identifies, analyzes, and evaluates risks across four categories: technical, operational, compliance, and project. Each risk is scored using a probability-impact matrix, assigned a mitigation strategy, and tracked in a formal risk register. The assessment follows the ISO 31000 risk management framework and integrates IEEE 1012 verification concerns to ensure risks threatening V&V integrity are captured.

## When to Use This Skill

- When initiating a new project phase and risks need formal identification
- When the audit report has revealed findings that require risk quantification
- When stakeholders require a formal risk register for governance oversight
- When preparing for external reviews or regulatory submissions
- When significant architectural or scope changes introduce new risk vectors
- When compliance gaps identified in 03-compliance-documentation need risk scoring

## Quick Reference

| Attribute | Value |
|-----------|-------|
| **Input** | vision.md, quality_standards.md, SRS_Draft.md, HLD.md |
| **Output** | Risk_Assessment.md |
| **Standard** | ISO 31000, IEEE 1012 |
| **Estimated Time** | 20-35 minutes |

## Input Files

| File | Purpose | Required? |
|------|---------|-----------|
| `projects/<ProjectName>/_context/vision.md` | Project scope, objectives, and constraints for risk context establishment | Yes |
| `projects/<ProjectName>/_context/quality_standards.md` | Quality thresholds and acceptance criteria for risk tolerance definition | No |
| `projects/<ProjectName>/<phase>/<document>/SRS_Draft.md` | Requirements for technical risk identification and dependency analysis | No |
| `projects/<ProjectName>/<phase>/<document>/HLD.md` | Architecture decisions for technical and operational risk identification | No |
| `projects/<ProjectName>/<phase>/<document>/Audit_Report.md` | Audit findings that may indicate risk areas requiring formal assessment | No |
| `projects/<ProjectName>/<phase>/<document>/Compliance_Docs.md` | Compliance gaps that translate directly into compliance risks | No |

## Output Files

| File | Description |
|------|-------------|
| `projects/<ProjectName>/<phase>/<document>/Risk_Assessment.md` | Complete risk assessment with register, scoring matrix, and mitigation plans |

## Core Instructions

1. The skill SHALL read `projects/<ProjectName>/_context/vision.md` to establish the risk context including project objectives, stakeholders, constraints, and risk appetite. If the file is missing, halt execution and report the error.

2. The skill SHALL read all available optional inputs to build a comprehensive risk inventory. Log each file read.

3. The skill SHALL define the Risk Assessment Methodology based on ISO 31000, including:
   - Risk identification techniques used
   - Probability scale (1-5: Rare, Unlikely, Possible, Likely, Almost Certain)
   - Impact scale (1-5: Negligible, Minor, Moderate, Major, Catastrophic)
   - Risk score calculation: $RiskScore = Probability \times Impact$
   - Risk tolerance thresholds (Low: 1-4, Medium: 5-9, High: 10-15, Critical: 16-25)

4. The skill SHALL identify risks across four categories:
   - **Technical:** Technology failures, integration issues, performance bottlenecks, security vulnerabilities
   - **Operational:** Process failures, resource constraints, skill gaps, vendor dependencies
   - **Compliance:** Regulatory violations, data protection failures, audit non-conformities
   - **Project:** Schedule delays, scope creep, budget overruns, stakeholder misalignment

5. The skill SHALL analyze each risk using the 5x5 probability-impact matrix and assign a composite risk score.

6. The skill SHALL construct a Risk Register Table with columns: Risk ID, Category, Description, Probability (1-5), Impact (1-5), Risk Score, Mitigation Strategy, Owner, Status.

7. The skill SHALL assign a Risk Response Strategy to each identified risk:
   - **Avoid:** Eliminate the threat by removing the cause
   - **Mitigate:** Reduce probability or impact through controls
   - **Transfer:** Shift risk to a third party (insurance, outsourcing)
   - **Accept:** Acknowledge the risk with documented rationale

8. The skill SHALL assess Residual Risk after mitigation strategies are applied, recalculating scores to confirm acceptable risk levels.

9. The skill SHALL generate a Risk Monitoring Plan specifying review frequency, trigger conditions for re-assessment, and escalation procedures.

10. The skill SHALL cross-reference identified risks with audit findings (if available) to ensure all V&V anomalies are captured in the risk register.

## Output Format Specification

The generated `Risk_Assessment.md` SHALL contain the following sections:

```
# Risk Assessment
## 1. Document Information
## 2. Risk Assessment Methodology
### 2.1 ISO 31000 Framework
### 2.2 Probability Scale
### 2.3 Impact Scale
### 2.4 Risk Scoring Matrix
### 2.5 Risk Tolerance Thresholds
## 3. Risk Identification
### 3.1 Technical Risks
### 3.2 Operational Risks
### 3.3 Compliance Risks
### 3.4 Project Risks
## 4. Risk Analysis Matrix
## 5. Risk Register
## 6. Risk Response Strategies
## 7. Residual Risk Assessment
## 8. Risk Monitoring Plan
## 9. Risk Summary & Recommendations
## 10. Revision History
```

## Common Pitfalls

- Using vague risk descriptions ("something might go wrong") instead of specific, measurable risk statements
- Applying uniform probability/impact scores without evidence-based differentiation
- Omitting residual risk assessment, leaving stakeholders unaware of post-mitigation exposure
- Failing to assign risk owners, making mitigation strategies unenforceable
- Ignoring compliance risks when the project operates in a regulated domain
- Treating risk assessment as a one-time activity instead of establishing a monitoring cadence

## Verification Checklist

1. All four risk categories (technical, operational, compliance, project) have been assessed.
2. Every risk has a unique identifier and specific, measurable description.
3. Probability and impact scores use the defined 1-5 scales consistently.
4. Risk scores are correctly calculated as $Probability \times Impact$.
5. Every risk has an assigned response strategy (Avoid/Mitigate/Transfer/Accept).
6. Residual risk scores are calculated for all mitigated risks.
7. The risk register includes an owner and status for every entry.
8. The monitoring plan specifies review cadence and escalation triggers.

## Integration

- **Upstream:** Consumes project context, audit findings from 02-audit-report, and compliance gaps from 03-compliance-documentation.
- **Downstream:** Terminal skill -- outputs feed project governance dashboards, steering committee reviews, and external risk disclosures.

## Standards Compliance

| Standard | Governs |
|----------|---------|
| ISO 31000:2018 | Risk management framework, principles, and process |
| IEEE 1012-2016 | V&V risk identification and anomaly-driven risk assessment |

## Resources

- ISO 31000:2018: Risk Management -- Guidelines
- IEEE 1012-2016: Standard for System, Software, and Hardware Verification and Validation
- CLAUDE.md: Project-level V&V and quality constraints

---
name: "ai-act-and-regulatory-compliance-doc"
description: "Generate the AI Act and Regulatory Compliance Doc: EU AI Act risk-tier classification per feature, US state and sectoral AI rules (FCRA, HIPAA, EEOC, NYC AEDT, Colorado, California ADMT), Canadian / UK guidance, and African AI regulator overlays (Kenya ODPC, Nigeria NDPC, South Africa POPIA). Includes the Annex IV technical documentation index and the disclosure copy library."
metadata:
  use_when: "Use for any SaaS shipping AI features to multiple jurisdictions. Mandatory before EU launch and updated each time a regulation moves."
  do_not_use_when: "Do not use if the product is non-AI or single-jurisdiction internal-only."
  required_inputs: "AI_Feature_PRD_Spec.md, AI_Model_Card.md (per feature), AI_Data_And_Knowledge_Base_Spec.md, DPA, regional rollout plan."
  workflow: "Classify each feature against EU AI Act Annex III and Article 5 prohibitions, assess US sectoral exposure, assess African regulator overlays, build the Annex IV technical-documentation index, write the disclosure-copy library, write the compliance doc."
  quality_standards: "Every AI feature shall have an EU AI Act tier verdict with reasoning. Every high-risk feature shall map to Annex IV technical documentation. Every region in scope shall have disclosure copy."
  anti_patterns: "Do not classify by hope; classify by Article 5 / Annex III mapping. Do not omit sectoral rules (FCRA, HIPAA, EEOC) when the feature touches lending / health / employment."
  outputs: "AI_Act_And_Regulatory_Compliance_Doc.md and disclosure-copy library."
  references: "Use references/ai-act-regulatory-compliance-doc-template.md and references/ai-disclosure-copy-library.md."
---

# AI Act and Regulatory Compliance Doc Skill

## Core Instructions

### Step 1: EU AI Act classification per feature

For each feature evaluate:

- **Prohibited (Art. 5)** — social scoring, manipulative AI, predictive policing of natural persons, untargeted scraping of facial images, emotion inference in workplace/education, exploiting vulnerability, biometric categorisation by protected characteristic, real-time remote biometric identification in publicly accessible spaces.
- **High-risk (Annex III)** — biometric / critical infrastructure / education-and-training / employment / essential private and public services (including credit and insurance) / law enforcement / migration / administration of justice / influencing elections.
- **Limited-risk (Art. 50)** — chatbots, generative content, deep fakes -- transparency obligations.
- **Minimal-risk** — everything else.

Each feature carries the verdict + cited Article / Annex point.

### Step 2: US sectoral exposure

- FCRA — adverse credit decisions based on AI.
- HIPAA — PHI handling and de-identification.
- EEOC + Title VII — automated employment decisions.
- NYC Local Law 144 — AEDT bias audits.
- Colorado AI Act (SB24-205) — high-risk consumer decisions.
- California AB 2013 + ADMT regulation (2026-) — generative training data + automated decision-making.
- Illinois BIPA — biometric data.
- FTC Section 5 — unfair or deceptive AI claims.

### Step 3: Canadian / UK guidance

- Canada AIDA (pending) and Directive on Automated Decision-Making for federal scope.
- UK ICO guidance on AI + AI Act-equivalent pro-innovation framework.

### Step 4: African regulator overlays

- Kenya ODPC AI guidance (2024).
- Nigeria NDPC advisory on AI processing (2024).
- South Africa POPIA s.71 (automated decision-making).
- Note: Uganda DPPA 2019 has no AI-specific clause yet; profile under general data-protection obligations.

### Step 5: Annex IV technical documentation index

For every high-risk-classified feature build the index (table mapping each Annex IV element to the artefact in our system that satisfies it).

### Step 6: Disclosure copy library

UI copy for required disclosures per region:

- "AI-assisted output" tooltip.
- First-use AI feature disclosure modal.
- High-risk decision human-oversight notice.
- Generative content disclosure (Art. 50).
- Right-to-explanation copy.

### Step 7: Write the doc

`AI_Act_And_Regulatory_Compliance_Doc.md` sections: 1) EU AI Act Classification, 2) US Sectoral Exposure, 3) Canada / UK, 4) African Regulators, 5) Annex IV Technical Documentation Index, 6) Disclosure Copy Library, 7) Open Compliance Items, 8) Review Cadence.

## Agent-specific overlap with SOC 2 / ISO 27001 / HIPAA

When the SaaS ships agent features alongside the AI features covered here, this doc shall cross-link to the agent-specific compliance stack:

- SOC 2: `09-governance-compliance/20-ai-agent-soc2-control-pack` (per-TSC agent-specific implementations).
- ISO 27001: `09-governance-compliance/21-ai-agent-iso27001-control-pack` (Annex A agent treatments).
- HIPAA: `09-governance-compliance/22-ai-agent-hipaa-control-pack` (Security Rule agent treatments; admin-only constraint).
- BAA / DPA: `09-governance-compliance/26-ai-agent-baa-and-data-processing-language`.
- Regulator overlap matrix (one-evidence-many-regimes): `09-governance-compliance/27-ai-agent-regulator-overlap-mapping`.

EU AI Act high-risk classification (Annex III) drives extra documentation that this doc owns (Annex IV technical-documentation index), while the agent-specific operating controls are owned by the agent control packs. The crosswalk in `27-ai-agent-regulator-overlap-mapping` shows where evidence is reused vs where the AI Act demands artefacts unique to itself (e.g., conformity assessment, post-market monitoring per Art. 72, serious-incident reporting per Art. 73).

## Standards

- EU Reg 2024/1689 (AI Act)
- ISO/IEC 42001
- NIST AI RMF
- US sectoral statutes named above
- Kenya DPA 2019, NDPR / NDP Act 2023, POPIA 2013

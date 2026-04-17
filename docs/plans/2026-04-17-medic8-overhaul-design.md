# Medic8 Documentation Overhaul — Design Document

**Date:** 2026-04-17
**Author:** Peter Bamuhigire / Chwezi Core Systems
**Status:** Approved

---

## 1. Overhaul Objective

Rebuild all Medic8 project documentation to reflect:

1. Tighter, more opinionated module scope statements across all 31 modules
2. Multi-language support (English primary, French, Kiswahili) documented as a first-class architectural concern
3. Six new AI capabilities packaged as a single tenant-toggleable AI Intelligence module (Module 32)
4. Provider-agnostic AI adapter architecture supporting OpenAI, Anthropic, DeepSeek, and Gemini
5. Literature base refreshed from 7 new health informatics and AI healthcare books
6. All documents regenerated applying the full CLAUDE.md writing and engineering standards

---

## 2. Approach — Context-First, Documents-Second

All `_context/` files are overhauled before any phase document is touched. Every downstream document is generated from those updated context files. Nothing is written to a phase folder until the relevant context file is verified.

**This matches the PRIME methodology:** Prepare (`_context/` files) → Relay (invoke generation) → Inspect (review against context) → Modify (refine) → Execute (`build-doc.sh`).

---

## 3. Commit Batch Sequence

Commit and push after each batch. Never commit `templates/reference.docx`.

| Batch | Contents |
|-------|----------|
| 1 | All `_context/` files (12 existing + `i18n.md` + `ai-intelligence.md`) |
| 2 | Phase 01 — Strategic Vision: PRD, Vision Statement, Business Case |
| 3 | Phase 02 — Requirements Engineering: SRS, User Stories, Stakeholder/RBAC |
| 4 | Phase 03 — Design Documentation: HLD, LLD, API Spec, ERD, UX Spec |
| 5 | Phase 04 — Development Artifacts: Technical Spec, Coding Guidelines |
| 6 | Phase 05 — Testing Documentation: Test Strategy, Test Plan, Test Report |
| 7 | Phase 06 — Deployment and Operations: Deployment Guide, Runbook |
| 8 | Phase 07 — Agile Artifacts: Sprint Planning, DoD, DoR |
| 9 | Phase 08 — End-User Documentation: User Manual |

---

## 4. Module Scope Changes

All 31 existing modules are retained. Each module specification is rewritten to this structure:

- **Scope Statement** — 2 to 3 sentences maximum. What the module does and what it owns.
- **Key Capabilities** — bullet list, maximum 8 bullets per module.
- **Africa-First Enhancements** — retained and tightened.
- **Interfaces** — retained, no structural change.
- **Out of Scope** — retained, sharpened to remove ambiguity.
- **Localisation Flags** — new section, present only where non-obvious cultural adaptation is required (not repeated for every module).

No new modules are added beyond Module 32 (AI Intelligence). No existing modules are removed.

---

## 5. Module 32 — AI Intelligence

### 5.1 Positioning

The AI Intelligence module is a tenant-toggleable add-on, completely decoupled from the clinical subscription tier. Facilities purchase either a **monthly credit pack** (token-denominated) or a **flat monthly fee**. AI features auto-pause when credits are exhausted. Individual capabilities within the module can be toggled independently per tenant from the admin panel.

**Tier coupling:** None. Any facility on any clinical tier can activate AI Intelligence.

### 5.2 Six AI Capabilities

| # | Capability | Description |
|---|-----------|-------------|
| 1 | **AI Clinical Documentation** | Drafts SOAP notes, discharge summaries, and referral letters from structured encounter data. The clinician reviews and explicitly approves before any draft is saved to the patient record. |
| 2 | **AI ICD Coding Assist** | Suggests ICD-10/11 codes from free-text clinical notes using natural language understanding. Removes the need for dedicated coding staff at smaller facilities. |
| 3 | **AI Differential Diagnosis** | At the point of care, surfaces a ranked differential diagnosis list from the patient's symptoms, vitals, and recent lab results. Presented as a clinical prompt, not a decision. Clinician can dismiss or act on each suggestion. |
| 4 | **AI Patient Plain-Language Summary** | Translates clinical notes into plain-language summaries in the patient's preferred language (English, French, or Kiswahili) for display in the patient app. Adapts reading level to the target audience. |
| 5 | **AI Claim Scrubbing** | Before claim submission, predicts rejection probability per line item using historical rejection patterns. Flags fields that commonly cause insurer rejections. Reduces re-submission cycles and revenue leakage. |
| 6 | **AI Outbreak Early Warning** | Detects anomalous clustering of diagnosis codes at the facility level before the IDSR national threshold is crossed. Sends a configurable alert to the medical officer with the implicated disease codes and patient volume. |

### 5.3 Provider Adapter Architecture

A single internal `AIProviderInterface` is implemented by four concrete adapter classes. Per-tenant configuration selects the active provider and stores the API key in encrypted tenant settings. A secondary (failover) provider is configurable.

```
AIProviderInterface
  ├── OpenAIAdapter       (GPT-4o, GPT-4o-mini)
  ├── AnthropicAdapter    (Claude Sonnet, Claude Haiku)
  ├── DeepSeekAdapter     (DeepSeek-V3, DeepSeek-R1)
  └── GeminiAdapter       (Gemini 1.5 Pro, Gemini 1.5 Flash)
```

All adapters expose the same methods: `complete()`, `chat()`, `embed()`. Switching providers requires no code change — only a tenant configuration update. Token usage is metered per tenant per capability and logged for billing reconciliation.

---

## 6. Multi-Language (i18n) Architecture

### 6.1 Languages

| Code | Language | Status |
|------|----------|--------|
| `en` | English | Primary — all strings mandatory |
| `fr` | French | Launch language — all strings required at ship |
| `sw` | Kiswahili | Launch language — all strings required at ship |

### 6.2 Architecture

- **PHP backend:** Laravel localisation (`lang/en/`, `lang/fr/`, `lang/sw/`). String keys follow `module.context.label` naming convention (e.g., `opd.triage.blood_pressure_label`).
- **Android:** String resources per locale (`values/strings.xml`, `values-fr/strings.xml`, `values-sw/strings.xml`).
- **iOS:** `.strings` files per locale (`Localizable.strings` under `en.lproj/`, `fr.lproj/`, `sw.lproj/`).
- **Locale fallback chain:** `sw` → `en`, `fr` → `en`. A missing string never falls through to machine translation — it falls through to English and is flagged `[I18N-GAP: <key>]` in the build log.

### 6.3 Translation Principles

Strings are written contextually in each language to preserve natural tone and clinical meaning. Word-for-word translation is prohibited. Clinical severity labels (`Fatal`, `Serious`, `Warning`, `Info`) are rendered in the clinician's UI language and are never auto-translated mid-workflow alert.

### 6.4 Per-Module Localisation Flags

Flags appear only where cultural adaptation is non-obvious:

- **Maternity module:** "birth attendant" — `fr`: *accoucheuse*, `sw`: *mkunga* — different professional categories per country context.
- **Billing module:** Number formatting — `fr`: 1 500 000 UGX (space thousands separator), `en`/`sw`: 1,500,000 UGX.
- **Patient Portal AI Summary:** Plain-language health literacy level differs by language community; Kiswahili summaries target a lower reading level than French.
- **OPD Triage:** `sw` term for "chief complaint" is *malalamiko makuu* — contextually accurate; literal translation (*malalamiko ya kwanza*) is clinically ambiguous.

---

## 7. Literature Base — 7 Books

The `_context/literature-insights.md` is rebuilt from the 7 books below. The previous 10-book list is retired. Insights retain the existing category structure with one new category added.

| # | Title | Relevance |
|---|-------|-----------|
| 1 | *Health Informatics: A Systems Perspective, 2nd Ed.* | Architecture, data bus, population health |
| 2 | *Guide to Health Informatics, 3rd Ed.* | CDS, terminology services, interoperability |
| 3 | *Revolutionizing Healthcare 5.0 — The Power of Generative AI* | AI Clinical Documentation, ICD Coding Assist, Differential Diagnosis |
| 4 | *Decision Making in Healthcare Systems* | Clinical decision support, differential diagnosis architecture |
| 5 | *Patient-Centered Digital Healthcare Technology* | Patient Plain-Language Summary, patient portal design |
| 6 | *Healthcare Payment Systems* | AI Claim Scrubbing, insurance workflow, revenue cycle |
| 7 | *AI Adoption in Healthcare Industry 4.0* | AI module architecture, provider adapter, operational AI |

**New insight category added:** AI and Decision Intelligence — sourced from books 3, 4, and 7.

---

## 8. Documentation Standards Applied Throughout

Every regenerated document applies the following standards from `CLAUDE.md`:

- **Three-Emphasis Rule:** `**Bold**` for UI element names and requirement IDs only; `*italic*` for first-use defined terms and critical warnings; `` `monospace` `` for file paths, commands, code, and system identifiers.
- **Headings:** ATX-style `#` only. No underline-style `---` or `===` headings.
- **Lists:** Ordered lists (`1.`, `2.`, `3.`) for all sequential procedures. `-` bullet character for unordered lists.
- **NFRs:** No vague adjectives. Every non-functional requirement carries a measurable IEEE-982.1 metric.
- **V&V gates:** All SRS sections include fail tags (`[V&V-FAIL]`, `[CONTEXT-GAP]`, `[GLOSSARY-GAP]`, `[SMART-FAIL]`, `[TRACE-GAP]`).
- **DPPA 2019:** All personal data handling in Uganda-deployed tenants is compliant with the Data Protection and Privacy Act 2019.
- **i18n gaps:** Missing translation strings are flagged `[I18N-GAP: <key>]`.
- **Stimulus-Response:** All functional requirements follow the stimulus-response pattern for verifiability.

---

## 9. Context Files to Create or Update

| File | Action | Notes |
|------|--------|-------|
| `vision.md` | Update | Add AI Intelligence module, i18n as design covenant item, updated MRR targets |
| `tech_stack.md` | Update | Add `AIProviderInterface` adapter layer, i18n stack per platform |
| `literature-insights.md` | Rebuild | 7 new books, retire 10-book list, add AI and Decision Intelligence category |
| `competitor-analysis.md` | Update | Add AI Intelligence and i18n as decisive advantages; refresh ClinicMaster and OpenMRS gaps |
| `glossary.md` | Update | Add: AI Intelligence, credit pack, locale fallback chain, `AIProviderInterface`, Kiswahili, i18n |
| `quality_standards.md` | Update | Add i18n quality gate, AI output review gate |
| `business_rules.md` | Update | Add AI credit pack billing rules, locale selection rules, provider failover rules |
| `stakeholders.md` | Update | Add AI Administrator role (manages provider keys, monitors token usage) |
| `personas.md` | Update | Add multilingual patient persona (French-speaking DRC patient at Ugandan facility) |
| `metrics.md` | Update | Add AI-specific success metrics (ICD suggestion acceptance rate, claim scrub rejection reduction) |
| `gap-analysis.md` | Update | Document i18n gaps and AI capability gaps vs. current market |
| `payment-landscape.md` | Update | Add AI credit pack as a billing product line |
| `i18n.md` | **Create** | Central i18n architecture spec (locale codes, fallback chain, string key convention, platform implementation) |
| `ai-intelligence.md` | **Create** | AI Intelligence module context: 6 capabilities, provider adapter spec, credit pack billing model, token metering |

---

## 10. New Advantages Over Competitors (Updated Competitive Position)

Beyond the 15 existing decisive advantages over ClinicMaster, Medic8 now adds:

1. **AI-drafted clinical notes** — no competitor in the East Africa market offers clinician-facing generative AI at the point of care.
2. **AI claim scrubbing** — predictive rejection detection before submission; ClinicMaster has no AI layer whatsoever.
3. **AI outbreak early warning** — facility-level anomaly detection before national threshold breach; no competing product offers this.
4. **Three-language interface** — English, French, and Kiswahili from day one; ClinicMaster is English-only; OpenMRS community translations are incomplete and untested.
5. **Provider-agnostic AI** — facilities are not locked to one AI vendor; cost can be optimised by switching providers.

---

*End of design document.*

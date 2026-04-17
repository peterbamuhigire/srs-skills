# Medic8 Documentation Overhaul — Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Overhaul all Medic8 project documentation to reflect tighter module scopes, a new AI Intelligence module, English/French/Kiswahili i18n architecture, and insights from 7 new health informatics books — regenerating all 17+ documents and their `.docx` outputs.

**Architecture:** Context-First, Documents-Second (PRIME methodology). All `_context/` files are rebuilt before any phase document is touched. Every downstream document is generated from those updated context files. Commit and push after each batch.

**Tech Stack:** Markdown, Pandoc (`bash scripts/build-doc.sh`), Git. No code — this is a documentation engine project.

---

## Reference Paths

**Project root:** `C:\wamp64\www\srs-skills\`
**Project workspace:** `projects/Medic8/`
**Context files:** `projects/Medic8/_context/`
**Build script:** `bash scripts/build-doc.sh <doc-dir> <OutputName>`
**Export folder:** `projects/Medic8/export/`

**Book sources (read with the Read tool):**
- `C:\Users\Peter\Downloads\Health Informatics_ A Systems Perspective, Second Edition.epub`
- `C:\Users\Peter\Downloads\Guide to Health Informatics, Third Edition.epub`
- `C:\Users\Peter\Downloads\Revolutionizing Healthcare 5.0 - The Power of Generative AI.epub`
- `C:\Users\Peter\Downloads\Decision Making in Healthcare Systems.epub`
- `C:\Users\Peter\Downloads\Patient-Centered Digital Healthcare Technology.epub`
- `C:\Users\Peter\Downloads\Healthcare Payment Systems.epub`
- `C:\Users\Peter\Downloads\AI Adoption in Healthcare Industry 4.0 - Innovative Business Models and Employability.epub`

**Design doc (read before starting):** `docs/plans/2026-04-17-medic8-overhaul-design.md`

---

## Writing Standards Checklist (apply to every file)

Before saving any generated markdown, verify:

- [ ] No `**bold**` used outside UI element names and requirement IDs
- [ ] No `_italic_` or `__bold__` (use `*italic*` and `**bold**` only)
- [ ] No `---` or `===` underline-style headings — ATX `#` only
- [ ] All NFRs have a measurable metric (no "fast", "reliable", "seamless")
- [ ] Ordered lists (`1.`, `2.`, `3.`) for all procedures
- [ ] `-` bullet character only (never `*` or `+`)
- [ ] Blank line before and after every heading, table, and code block
- [ ] Every domain term that is used appears in `_context/glossary.md`
- [ ] `[CONTEXT-GAP]`, `[GLOSSARY-GAP]`, `[I18N-GAP]` tags used where needed
- [ ] "The system shall…" active voice for all FRs

---

## Batch 1 — Context Files

**Commit after this batch.** All downstream documents depend on these files being correct first.

---

### Task 1: Read all 7 books and rebuild `literature-insights.md`

**Files:**
- Modify: `projects/Medic8/_context/literature-insights.md`

**Step 1: Read the design doc**

Read `docs/plans/2026-04-17-medic8-overhaul-design.md` to confirm the 7 book list and the new "AI and Decision Intelligence" insight category.

**Step 2: Read each book**

Use the Read tool on each epub path listed in Reference Paths above. For each book, extract:
- Clinical safety enhancements
- Data architecture enhancements
- UX and adoption enhancements
- Paediatric enhancements
- Commercial and strategic enhancements
- AI and decision intelligence enhancements (new category — from books 3, 4, 7)

**Step 3: Rewrite `literature-insights.md`**

Structure:
```markdown
# Literature Insights — Medic8

[intro sentence]

## Clinical Safety Enhancements
[numbered list — each entry: bold title, description, source citation, phase mapping]

## Data Architecture Enhancements
[same format]

## UX and Adoption Enhancements
[same format]

## Paediatric Enhancements
[same format]

## AI and Decision Intelligence Enhancements
[same format — this is the new category]

## Commercial and Strategic Enhancements
[same format]

## Literature Sources
[table: Book | Author(s) | Year — 7 rows only]
```

Rules:
- Retire the 10-book source list entirely. Do not reference old books.
- Each insight: bold title + 2-sentence description + source citation + phase tag.
- Only include insights that are practical and have a build phase home. Discard speculative or irrelevant insights.
- Target 40-60 total insights across all categories.
- Do not include features the existing module list already covers unless the book adds a measurably better approach.

**Step 4: Apply writing standards checklist**

**Step 5: Save the file**

---

### Task 2: Update `vision.md`

**Files:**
- Modify: `projects/Medic8/_context/vision.md`

**Step 1: Read existing `vision.md`**

Read `projects/Medic8/_context/vision.md`.

**Step 2: Apply these specific changes**

1. Add to **Design Covenant** hard requirements:
   - "Multi-language by default: English, French, and Kiswahili ship as launch languages. No string is hardcoded in any UI layer."
   - "AI as a utility, not a tier: the AI Intelligence module is available to any facility as a credit-pack or flat-fee add-on, independent of the clinical subscription tier."

2. Update **Architecture Decisions** — add:
   - "Provider-agnostic AI layer: `AIProviderInterface` with adapters for OpenAI, Anthropic, DeepSeek, and Gemini. Per-tenant provider selection from the admin panel."
   - "i18n architecture: Laravel localisation (`lang/en/`, `lang/fr/`, `lang/sw/`), Android string resources per locale, iOS `.strings` files per locale. Locale fallback chain: `sw` → `en`, `fr` → `en`."

3. Update **Module count** in Goals section to reference 32 modules (31 clinical/admin + AI Intelligence).

4. Update **MRR targets** — keep existing figures; add note: "AI Intelligence add-on revenue is additive to base MRR targets."

**Step 3: Apply writing standards checklist**

**Step 4: Save the file**

---

### Task 3: Update `tech_stack.md`

**Files:**
- Modify: `projects/Medic8/_context/tech_stack.md`

**Step 1: Read existing `tech_stack.md`**

**Step 2: Add two new sections**

Add after the "Clinical Architecture" section:

```markdown
## AI Intelligence Layer

- **Interface:** `AIProviderInterface` — unified internal contract for all AI operations
- **Adapters:** `OpenAIAdapter` (GPT-4o, GPT-4o-mini), `AnthropicAdapter` (Claude Sonnet, Claude Haiku), `DeepSeekAdapter` (DeepSeek-V3, DeepSeek-R1), `GeminiAdapter` (Gemini 1.5 Pro, Gemini 1.5 Flash)
- **Methods exposed:** `complete()`, `chat()`, `embed()`
- **Per-tenant config:** Provider selection + API key stored in encrypted tenant settings table
- **Failover:** Secondary provider configurable per tenant; auto-switch on provider timeout > 10 s
- **Metering:** Token usage logged per tenant, per capability, per request for billing reconciliation
- **Capabilities:** AI Clinical Documentation, AI ICD Coding Assist, AI Differential Diagnosis, AI Patient Plain-Language Summary, AI Claim Scrubbing, AI Outbreak Early Warning

## Internationalisation (i18n)

- **Languages:** English (`en`, primary), French (`fr`), Kiswahili (`sw`)
- **PHP/Laravel:** `lang/en/`, `lang/fr/`, `lang/sw/` directories; string key convention: `module.context.label`
- **Android:** `values/strings.xml`, `values-fr/strings.xml`, `values-sw/strings.xml`
- **iOS:** `en.lproj/Localizable.strings`, `fr.lproj/Localizable.strings`, `sw.lproj/Localizable.strings`
- **Locale fallback chain:** `sw` → `en`; `fr` → `en`. Missing strings fall through to English and are flagged `[I18N-GAP: <key>]` in the build log — never machine-translated.
- **Translation principle:** Strings are written contextually per language. Word-for-word translation is prohibited.
- **Clinical severity labels:** Rendered in the clinician's UI language; never auto-translated mid-workflow alert.
```

**Step 3: Apply writing standards checklist**

**Step 4: Save the file**

---

### Task 4: Create `_context/i18n.md`

**Files:**
- Create: `projects/Medic8/_context/i18n.md`

**Step 1: Write the file**

```markdown
# Internationalisation (i18n) Architecture — Medic8

## Supported Languages

| Code | Language | Status | Notes |
|------|----------|--------|-------|
| `en` | English | Primary | All strings mandatory; fallback target |
| `fr` | French | Launch | All strings required at ship |
| `sw` | Kiswahili | Launch | All strings required at ship |

## String Key Convention

Format: `module.context.label`

Examples:
- `opd.triage.blood_pressure_label` → "Blood Pressure" / "Pression artérielle" / "Shinikizo la damu"
- `billing.payment.mobile_money_button` → "Pay with Mobile Money" / "Payer par Mobile Money" / "Lipa kwa Pesa ya Simu"
- `pharmacy.alert.drug_interaction_fatal` → "FATAL: Drug Interaction Detected" / "FATAL : Interaction médicamenteuse détectée" / "HATARI: Mwingiliano wa Dawa Umegunduliwa"

## Locale Fallback Chain

```
sw → en
fr → en
```

A missing Kiswahili string falls through to English. A missing French string falls through to English. The application never machine-translates a missing string. Missing strings are flagged `[I18N-GAP: <key>]` in the build log and tracked as P1 bugs before release.

## Platform Implementation

### PHP / Laravel (Web Portal)

- String files: `lang/en/*.php`, `lang/fr/*.php`, `lang/sw/*.php`
- Usage: `__('opd.triage.blood_pressure_label')`
- Locale set per user session from their profile preference
- Clinical alert strings use a dedicated `lang/<locale>/alerts.php` file to allow priority review

### Android (Kotlin / Jetpack Compose)

- String files: `app/src/main/res/values/strings.xml` (en), `values-fr/strings.xml`, `values-sw/strings.xml`
- Usage: `stringResource(R.string.opd_triage_blood_pressure_label)`
- Locale follows device locale setting, overridable in user profile

### iOS (Swift / SwiftUI)

- String files: `en.lproj/Localizable.strings`, `fr.lproj/Localizable.strings`, `sw.lproj/Localizable.strings`
- Usage: `NSLocalizedString("opd.triage.blood_pressure_label", comment: "")`
- Locale follows device locale setting, overridable in user profile

## Translation Principles

1. Strings are written contextually in each target language to preserve natural tone and clinical meaning.
2. Word-for-word translation is prohibited. A Kiswahili speaker must find the interface natural, not translated.
3. Clinical severity labels (`Fatal`, `Serious`, `Warning`, `Info`) are rendered in the clinician's preferred UI language and are never auto-translated mid-workflow alert.
4. The AI Patient Plain-Language Summary capability generates patient-facing text at a lower reading level in Kiswahili than in French, reflecting the target audience's health literacy profile.

## Per-Module Localisation Flags

Flags appear only in module specifications where cultural adaptation is non-obvious:

| Module | Flag | Notes |
|--------|------|-------|
| Maternity, ANC and Reproductive Health | `[I18N: birth-attendant]` | `fr`: *accoucheuse*, `sw`: *mkunga* — different professional categories per country context |
| Billing and Revenue Management | `[I18N: number-format]` | `fr`: 1 500 000 UGX (space thousands separator); `en`/`sw`: 1,500,000 UGX |
| Patient Portal and Mobile App — AI Summary | `[I18N: health-literacy-level]` | Kiswahili summaries target a lower reading level than French |
| OPD — Triage | `[I18N: chief-complaint]` | `sw`: *malalamiko makuu* (contextually accurate); literal translation *malalamiko ya kwanza* is clinically ambiguous |

## Gap Management

Any string without an approved translation in `fr` or `sw` at ship is a release blocker. Track gaps in `_context/quality-log.md` under "i18n Gaps". Format: `[I18N-GAP: module.context.label]`.
```

**Step 2: Apply writing standards checklist**

**Step 3: Save the file**

---

### Task 5: Create `_context/ai-intelligence.md`

**Files:**
- Create: `projects/Medic8/_context/ai-intelligence.md`

**Step 1: Write the file covering:**
- Module positioning (tenant-toggleable, credit pack or flat fee, no tier coupling)
- All 6 capabilities with: description, inputs, outputs, human review gate, toggle key
- Provider adapter architecture: interface contract + 4 adapters + methods
- Token metering and billing reconciliation
- Admin panel configuration: provider selection, API key (encrypted), failover provider, per-capability toggles
- Credit pack model: what happens when credits run out (AI features pause, not clinical features)
- Safety guardrails: AI Clinical Documentation and AI Differential Diagnosis outputs are ALWAYS presented as drafts — never auto-saved without clinician explicit approval
- Data privacy: patient data sent to AI providers is governed by the tenant's data processing agreement; providers must be configured per DPPA 2019 requirements for Uganda-deployed tenants

**Step 2: Apply writing standards checklist**

**Step 3: Save the file**

---

### Task 6: Update `competitor-analysis.md`

**Files:**
- Modify: `projects/Medic8/_context/competitor-analysis.md`

**Step 1: Read existing `competitor-analysis.md`**

**Step 2: Add 5 new decisive advantages to the ClinicMaster gaps section**

Add to "ClinicMaster Critical Gaps — Medic8 Decisive Advantages":

16. **No generative AI at point of care.** Medic8: AI-drafted SOAP notes, discharge summaries, and referral letters reviewed and approved by the clinician before saving. No competitor in East Africa offers this.
17. **No AI claim scrubbing.** Medic8: rejection probability prediction per line item before submission; reduces re-submission cycles and revenue leakage.
18. **No facility-level outbreak early warning.** Medic8: anomalous diagnosis clustering detected before the IDSR national threshold is crossed; alerts the medical officer.
19. **English-only interface.** Medic8: English, French, and Kiswahili from day one. Directly targets French-speaking DRC and Francophone African expansion markets.
20. **Locked to one technology vendor.** Medic8: provider-agnostic AI adapter — facilities switch between OpenAI, Anthropic, DeepSeek, and Gemini from the admin panel without any code change.

**Step 3: Update the OpenMRS gaps section** — add:
13. **No AI capabilities** — OpenMRS has no generative AI, no claim scrubbing, no outbreak early warning.
14. **English-dominant** — community translations for Kiswahili and French are incomplete and untested in clinical settings.

**Step 4: Update the TCO comparison table** — add a row for "AI Intelligence module" showing OpenMRS cost (custom build: $5,000-$20,000) vs. Medic8 (credit pack add-on).

**Step 5: Apply writing standards checklist**

**Step 6: Save the file**

---

### Task 7: Update `glossary.md`

**Files:**
- Modify: `projects/Medic8/_context/glossary.md`

**Step 1: Read existing `glossary.md`**

**Step 2: Add these entries** (maintain alphabetical order):

- **AI Intelligence Module** — Medic8's tenant-toggleable AI add-on providing six capabilities: AI Clinical Documentation, AI ICD Coding Assist, AI Differential Diagnosis, AI Patient Plain-Language Summary, AI Claim Scrubbing, and AI Outbreak Early Warning.
- **AIProviderInterface** — the internal PHP interface that all AI provider adapters implement. Exposes `complete()`, `chat()`, and `embed()` methods. Enables switching AI providers without code changes.
- **AnthropicAdapter** — concrete implementation of `AIProviderInterface` for Anthropic's Claude models.
- **Credit Pack** — a token-denominated bundle purchased by a facility to fund AI Intelligence module usage. AI features pause when credits are exhausted.
- **DeepSeekAdapter** — concrete implementation of `AIProviderInterface` for DeepSeek models.
- **GeminiAdapter** — concrete implementation of `AIProviderInterface` for Google Gemini models.
- **i18n** — internationalisation. The engineering practice of designing software so that it can be adapted to different languages and regions without engineering changes.
- **I18N-GAP** — a tag marking a string key that lacks an approved translation in one or more of the launch languages (`fr`, `sw`). Treated as a P1 release blocker.
- **Kiswahili** — a Bantu language spoken across East and Central Africa. One of Medic8's three launch languages (locale code: `sw`).
- **Locale Fallback Chain** — the ordered sequence of locales tried when a string is missing: `sw` → `en`, `fr` → `en`. Missing strings never machine-translate; they fall through to English and are flagged.
- **OpenAIAdapter** — concrete implementation of `AIProviderInterface` for OpenAI GPT models.
- **Plain-Language Summary** — a patient-facing AI-generated translation of clinical notes into non-technical language at an appropriate reading level, delivered in the patient's preferred language.

**Step 3: Save the file**

---

### Task 8: Update remaining context files

**Files:**
- Modify: `projects/Medic8/_context/business_rules.md`
- Modify: `projects/Medic8/_context/stakeholders.md`
- Modify: `projects/Medic8/_context/metrics.md`
- Modify: `projects/Medic8/_context/quality_standards.md`
- Modify: `projects/Medic8/_context/personas.md`

**Step 1: `business_rules.md` — add:**
- AI credit pack billing: credits are metered per token; each capability has a published token cost estimate; the admin panel shows remaining credits in real time.
- When credits reach zero, AI features pause immediately; clinical features are unaffected.
- Locale selection: users select their preferred language from their profile. Clinical alert severity labels (`Fatal`, `Serious`, `Warning`, `Info`) always render in the clinician's UI language.
- Provider failover: if the primary AI provider returns an error or times out after 10 seconds, the system automatically retries with the configured secondary provider.
- AI outputs (clinical notes, differential diagnoses) are never auto-saved. They are presented as drafts. The clinician must explicitly approve before saving to the patient record.

**Step 2: `stakeholders.md` — add:**
- **AI Administrator** — manages per-tenant AI provider configuration, API keys, credit pack top-ups, and monitors token usage via the admin panel. Role may be held by the Clinic IT Officer or delegated to Chwezi Core Systems support staff.

**Step 3: `metrics.md` — add AI success metrics:**
- ICD coding suggestion acceptance rate ≥ 70% within 90 days of AI module activation (baseline: 0%)
- AI claim scrubbing rejection rate reduction ≥ 20% within 6 months of activation
- AI clinical note draft acceptance rate (unedited approval) ≥ 40% within 90 days
- AI outbreak early warning false positive rate ≤ 15% over a rolling 90-day period

**Step 4: `quality_standards.md` — add:**
- i18n quality gate: before any document build, run a string audit confirming no `[I18N-GAP]` tags remain unresolved in the module being built.
- AI output review gate: all AI-generated content in SRS sections must be reviewed against the `_context/ai-intelligence.md` spec. Flag deviations with `[V&V-FAIL: AI spec mismatch]`.

**Step 5: `personas.md` — add:**
- **Amina Hassan** — French-speaking DRC patient at a Kampala referral hospital. Uses the patient portal in French. Receives AI plain-language summaries of her discharge notes in French. Low health literacy. Accesses Medic8 on a low-end Android device over 3G.

**Step 6: Apply writing standards checklist to all files**

**Step 7: Save all files**

---

### Task 9: Commit Batch 1

```bash
cd C:\wamp64\www\srs-skills
git add projects/Medic8/_context/
git commit -m "Medic8 overhaul: rebuild all _context/ files (Batch 1)

- literature-insights.md: rebuilt from 7 new books; added AI and Decision Intelligence category
- vision.md: added i18n and AI Intelligence to Design Covenant and Architecture Decisions
- tech_stack.md: added AI Intelligence Layer and i18n sections
- i18n.md: created — central i18n architecture spec (en/fr/sw)
- ai-intelligence.md: created — AI Intelligence module spec (6 capabilities, provider adapter)
- competitor-analysis.md: added 5 new decisive advantages; updated OpenMRS and TCO sections
- glossary.md: added 12 new terms (AI adapter, i18n, credit pack, etc.)
- business_rules.md, stakeholders.md, metrics.md, quality_standards.md, personas.md: updated

Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>"
git push
```

---

## Batch 2 — Strategic Vision Documents

**Commit after this batch.**

---

### Task 10: Rewrite PRD sections

**Files:**
- Modify: `projects/Medic8/01-strategic-vision/01-prd/03-market-analysis.md`
- Modify: `projects/Medic8/01-strategic-vision/01-prd/04-target-users.md`
- Modify: `projects/Medic8/01-strategic-vision/01-prd/05-product-scope.md`
- Modify: `projects/Medic8/01-strategic-vision/01-prd/07-success-metrics.md`
- Modify: `projects/Medic8/01-strategic-vision/01-prd/09-roadmap.md`

**Step 1: Read all updated `_context/` files**

**Step 2: Rewrite `05-product-scope.md` — the largest change**

This file defines all 31 modules. For each module, rewrite to:
- Scope Statement: 2-3 sentences maximum
- Key Capabilities: maximum 8 bullets, each ≤ 25 words
- Africa-First Enhancements: keep, tighten to ≤ 5 bullets
- Interfaces: keep as-is
- Out of Scope: keep, sharpen
- Localisation Flags: add only where flagged in `_context/i18n.md`

Then add **Module 32: AI Intelligence** with full spec from `_context/ai-intelligence.md`.

**Step 3: Update `03-market-analysis.md`**
- Add French-speaking Africa (DRC, Rwanda, Cameroon) as expansion market enabled by i18n
- Add generative AI in healthcare as a market trend, citing the 2024-2025 adoption curve

**Step 4: Update `04-target-users.md`**
- Add AI Administrator persona from `_context/stakeholders.md`
- Add Amina Hassan multilingual patient persona from `_context/personas.md`

**Step 5: Update `07-success-metrics.md`**
- Add AI Intelligence success metrics from `_context/metrics.md`
- Add i18n quality metric: zero `[I18N-GAP]` tags in any production release

**Step 6: Update `09-roadmap.md`**
- Add AI Intelligence module to Phase 2 (available from Phase 2, not deferred to Phase 3)
- Add French and Kiswahili string completion as Phase 1 exit criteria

**Step 7: Apply writing standards checklist to all files**

**Step 8: Build the PRD docx**

```bash
cd C:\wamp64\www\srs-skills
bash scripts/build-doc.sh projects/Medic8/01-strategic-vision/01-prd Medic8_PRD
```

Expected: `projects/Medic8/01-strategic-vision/Medic8_PRD.docx` and `projects/Medic8/export/Medic8_PRD.docx`

---

### Task 11: Rewrite Vision Statement

**Files:**
- Modify: `projects/Medic8/01-strategic-vision/02-vision-statement/02-product-positioning.md`

**Step 1: Read existing file**

**Step 2: Update positioning** to include:
- Multi-language as a first-class differentiator (English, French, Kiswahili)
- AI Intelligence as a revenue-additive utility layer
- Updated competitive claims incorporating the 5 new advantages

**Step 3: Build the Vision Statement docx**

```bash
bash scripts/build-doc.sh projects/Medic8/01-strategic-vision/02-vision-statement Medic8_VisionStatement
```

---

### Task 12: Rewrite Business Case

**Files:**
- Modify: `projects/Medic8/01-strategic-vision/03-business-case/02-problem-statement.md`
- Modify: `projects/Medic8/01-strategic-vision/03-business-case/03-market-opportunity.md`
- Modify: `projects/Medic8/01-strategic-vision/03-business-case/05-competitive-analysis.md`
- Modify: `projects/Medic8/01-strategic-vision/03-business-case/07-risks.md`

**Step 1: Read all updated `_context/` files**

**Step 2: Update `03-market-opportunity.md`**
- Add Francophone Africa market size (DRC alone: 100M+ population; 1,200+ health facilities)
- Add AI in healthcare market growth projection

**Step 3: Update `05-competitive-analysis.md`**
- Pull from updated `competitor-analysis.md` in full
- Include updated TCO table with AI Intelligence add-on row
- Include all 20 decisive advantages over ClinicMaster

**Step 4: Update `07-risks.md`** — add:
- Risk: AI provider API outage → mitigation: secondary provider failover + AI feature graceful pause (clinical features unaffected)
- Risk: DPPA 2019 compliance for patient data sent to AI providers → mitigation: data processing agreements, no PII in AI prompts where avoidable, tenant-configurable provider selection

**Step 5: Build Business Case docx**

```bash
bash scripts/build-doc.sh projects/Medic8/01-strategic-vision/03-business-case Medic8_BusinessCase
```

---

### Task 13: Commit Batch 2

```bash
git add projects/Medic8/01-strategic-vision/
git commit -m "Medic8 overhaul: Phase 01 Strategic Vision (Batch 2)

- PRD: tightened all 31 module scopes; added Module 32 AI Intelligence; added i18n roadmap items
- Vision Statement: updated competitive positioning with AI and i18n advantages
- Business Case: added Francophone Africa market; updated TCO table; added AI risk register entries

Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>"
git push
```

---

## Batch 3 — Requirements Engineering

**Commit after this batch.**

---

### Task 14: Rewrite SRS

**Files:**
- Modify: `projects/Medic8/02-requirements-engineering/01-srs/03-external-interfaces.md`
- Modify: `projects/Medic8/02-requirements-engineering/01-srs/05-system-constraints.md`
- Modify: `projects/Medic8/02-requirements-engineering/01-srs/06-nfr.md`

**Step 1: Read all updated `_context/` files**

**Step 2: Update `03-external-interfaces.md`** — add:
- AI Provider APIs (OpenAI, Anthropic, DeepSeek, Gemini) as external interfaces with: protocol (HTTPS/REST), authentication (API key per provider), timeout (10 s), failover behaviour
- i18n string management — no external interface; strings are bundled at build time

**Step 3: Update `05-system-constraints.md`** — add:
- The AI Intelligence module MUST NOT auto-save AI-generated clinical content without explicit clinician approval. This is a non-negotiable safety constraint.
- Patient data sent to AI providers MUST be minimised per DPPA 2019 data minimisation principle. Prompts MUST NOT include full patient names, NIN, or NIRA numbers.
- All UI strings MUST exist in `en`, `fr`, and `sw` before any module is released to production.

**Step 4: Rewrite `06-nfr.md`** — for every NFR ensure:
- Specific measurable metric (no vague adjectives)
- IEEE-982.1 metric where applicable
- Append new NFRs:
  - AI response latency: AI capability responses MUST be returned within 8 s at P95 under normal load (1 concurrent AI request per 10 active clinicians).
  - AI availability: the AI Intelligence module MUST maintain ≥ 99.0% availability, measured monthly. AI feature unavailability MUST NOT affect clinical module availability.
  - i18n coverage: 100% of UI strings MUST have approved translations in `en`, `fr`, and `sw` before any module ships to production. Zero `[I18N-GAP]` tags permitted in a production build.
  - Provider failover: the system MUST automatically switch to the secondary AI provider within 12 s of primary provider timeout.

**Step 5: Apply V&V fail tags** where any requirement fails the verifiability test.

**Step 6: Build SRS docx**

```bash
bash scripts/build-doc.sh projects/Medic8/02-requirements-engineering/01-srs Medic8_SRS
```

---

### Task 15: Rewrite User Stories

**Files:**
- Modify: `projects/Medic8/02-requirements-engineering/02-user-stories/01-user-stories.md`

**Step 1: Read existing file and identify stories that need updating**

**Step 2: Add new user stories for:**
- AI Intelligence capabilities (6 stories — one per capability)
- AI Administrator stories (provider configuration, credit top-up, usage monitoring)
- Multilingual patient stories (language preference selection, receiving results in Kiswahili/French)
- Clinician i18n stories (clinician changes UI language from their profile)

**Step 3: Apply writing standards checklist**

**Step 4: Build User Stories docx**

```bash
bash scripts/build-doc.sh projects/Medic8/02-requirements-engineering/02-user-stories Medic8_UserStories
```

---

### Task 16: Update Stakeholder/RBAC document

**Files:**
- Modify: `projects/Medic8/02-requirements-engineering/03-stakeholder-analysis/` (read manifest first)

**Step 1: Add AI Administrator role** with:
- Permissions: read/write AI provider settings, read token usage dashboard, initiate credit top-up
- Scope: tenant-level (one AI Administrator per facility network)
- Cannot access: clinical records, billing, HR/payroll

**Step 2: Build RBAC/Stakeholder docx**

```bash
bash scripts/build-doc.sh projects/Medic8/02-requirements-engineering/03-stakeholder-analysis Medic8_RBAC_Stakeholder
```

---

### Task 17: Commit Batch 3

```bash
git add projects/Medic8/02-requirements-engineering/
git commit -m "Medic8 overhaul: Phase 02 Requirements Engineering (Batch 3)

- SRS: added AI Provider external interfaces; updated system constraints with AI safety rules;
  added AI latency/availability/i18n NFRs with measurable metrics
- User Stories: added 6 AI capability stories, AI Administrator stories, multilingual patient stories
- Stakeholder/RBAC: added AI Administrator role with scoped permissions

Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>"
git push
```

---

## Batch 4 — Design Documentation

**Commit after this batch.**

---

### Task 18: Update HLD

**Files:**
- Modify: `projects/Medic8/03-design-documentation/01-hld/` (read manifest first, update all files)

**Key additions:**
- AI Intelligence Layer architecture diagram (ASCII or Mermaid): `AIProviderInterface` → 4 adapters → external provider APIs
- i18n architecture: locale resolution flow, fallback chain, string bundle loading
- Multi-tenant AI configuration: encrypted provider settings table, per-tenant isolation

**Build:**
```bash
bash scripts/build-doc.sh projects/Medic8/03-design-documentation/01-hld Medic8_HLD
```

---

### Task 19: Update LLD

**Files:**
- Modify: `projects/Medic8/03-design-documentation/02-lld/01-module-architecture.md`

**Key additions:**
- Module 32: AI Intelligence — class diagram for `AIProviderInterface`, adapter classes, token metering service
- i18n service layer: locale detection, fallback resolver, string cache

**Build:**
```bash
bash scripts/build-doc.sh projects/Medic8/03-design-documentation/02-lld Medic8_LLD
```

---

### Task 20: Update API Spec

**Files:**
- Modify: `projects/Medic8/03-design-documentation/03-api-spec/00-index.md`

**Key additions:**
- AI Intelligence API endpoints:
  - `POST /api/ai/clinical-note` — draft clinical note from encounter data
  - `POST /api/ai/icd-suggest` — ICD code suggestions from free text
  - `POST /api/ai/differential` — differential diagnosis from symptoms + vitals + labs
  - `POST /api/ai/patient-summary` — plain-language patient summary
  - `POST /api/ai/claim-scrub` — claim rejection risk analysis
  - `GET /api/ai/usage` — token usage for current billing period
- Locale header: `Accept-Language: sw` / `fr` / `en` on all API responses

**Build:**
```bash
bash scripts/build-doc.sh projects/Medic8/03-design-documentation/03-api-spec Medic8_APISpec
```

---

### Task 21: Update ERD

**Files:**
- Modify: `projects/Medic8/03-design-documentation/04-database-design/` (read manifest)

**Key additions:**
- `ai_provider_config` table: `tenant_id`, `primary_provider`, `primary_api_key` (encrypted), `secondary_provider`, `secondary_api_key` (encrypted), `credit_balance`, `flat_fee_mode`
- `ai_usage_log` table: `tenant_id`, `capability`, `provider`, `tokens_used`, `request_at`, `response_ms`
- `ai_capability_toggles` table: `tenant_id`, `capability_key`, `enabled`
- `user_locale_preference` column on `users` table: `locale` CHAR(2) DEFAULT 'en'

**Build:**
```bash
bash scripts/build-doc.sh projects/Medic8/03-design-documentation/04-database-design Medic8_ERD
```

---

### Task 22: Update UX Specification

**Files:**
- Modify: `projects/Medic8/03-design-documentation/05-ux-spec/01-ux-specification.md`

**Key additions:**
- Language switcher: accessible from the user profile menu on every screen; immediately re-renders the current page without page reload
- AI capability UX patterns:
  - All AI drafts shown in a distinct visual container (light blue border, "AI Draft" label, "Approve" and "Discard" actions)
  - AI Differential Diagnosis shown as an expandable panel below the symptoms field — collapsed by default, expands on demand
  - AI Claim Scrubbing shown as a pre-submission review step with colour-coded risk indicators per line item
- Patient portal language selection: first-run language picker, accessible from settings thereafter
- AI credit balance indicator in admin panel: progress bar + token count + "Top Up" button

**Build:**
```bash
bash scripts/build-doc.sh projects/Medic8/03-design-documentation/05-ux-spec Medic8_UXSpecification
```

---

### Task 23: Commit Batch 4

```bash
git add projects/Medic8/03-design-documentation/
git commit -m "Medic8 overhaul: Phase 03 Design Documentation (Batch 4)

- HLD: AI Intelligence Layer + i18n architecture added
- LLD: Module 32 class diagram; i18n service layer
- API Spec: 6 AI endpoints; Accept-Language header; usage endpoint
- ERD: ai_provider_config, ai_usage_log, ai_capability_toggles tables; user_locale_preference column
- UX Spec: language switcher; AI draft UX patterns; credit balance indicator

Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>"
git push
```

---

## Batch 5 — Development Artifacts

**Commit after this batch.**

---

### Task 24: Update Technical Specification

**Files:**
- Modify: `projects/Medic8/04-development-artifacts/01-technical-spec/01-technical-specification.md`

**Key additions:**
- AI adapter implementation guide: how to implement `AIProviderInterface`, how to add a new provider adapter
- i18n implementation guide: string key naming convention, how to add a new string, how to run the i18n audit
- Token metering implementation: how usage is logged and reconciled against the billing system
- Provider failover implementation: circuit breaker pattern, retry logic, secondary provider activation

**Build:**
```bash
bash scripts/build-doc.sh projects/Medic8/04-development-artifacts/01-technical-spec Medic8_TechnicalSpec
```

---

### Task 25: Update Coding Guidelines

**Files:**
- Modify: `projects/Medic8/04-development-artifacts/02-coding-guidelines/01-coding-guidelines.md`

**Key additions:**
- i18n rule: no hardcoded strings in any UI layer. All user-visible text MUST use the localisation helper. Violation is a PR rejection criterion.
- AI safety rule: AI-generated content MUST NEVER be persisted without explicit clinician approval. Any PR that auto-saves AI output without an approval step is rejected.
- AI prompt hygiene rule: prompts MUST NOT include patient NIN, full legal name, or NIRA number. Use anonymised identifiers where possible.

**Build:**
```bash
bash scripts/build-doc.sh projects/Medic8/04-development-artifacts/02-coding-guidelines Medic8_CodingGuidelines
```

---

### Task 26: Commit Batch 5

```bash
git add projects/Medic8/04-development-artifacts/
git commit -m "Medic8 overhaul: Phase 04 Development Artifacts (Batch 5)

- Technical Spec: AI adapter guide; i18n implementation guide; token metering; provider failover
- Coding Guidelines: i18n no-hardcoded-string rule; AI safety approval rule; AI prompt hygiene rule

Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>"
git push
```

---

## Batch 6 — Testing Documentation

**Commit after this batch.**

---

### Task 27: Update Test Strategy

**Files:**
- Modify: `projects/Medic8/05-testing-documentation/01-test-strategy/01-test-strategy.md`

**Key additions:**
- AI Intelligence test strategy: unit tests mock the `AIProviderInterface`; integration tests use a sandbox API key per provider; never call live production AI APIs in automated tests
- i18n test strategy: automated string coverage audit (assert zero `[I18N-GAP]` tags before any build); manual review of Kiswahili and French strings by a native speaker before ship
- AI safety test: automated test asserting that no AI capability endpoint persists data without an explicit approval flag in the request

**Build:**
```bash
bash scripts/build-doc.sh projects/Medic8/05-testing-documentation/01-test-strategy Medic8_TestStrategy
```

---

### Task 28: Update Test Plan

**Files:**
- Modify: `projects/Medic8/05-testing-documentation/02-test-plan/01-test-plan.md`

**Key additions — test cases for:**
- AI Clinical Documentation: input a structured encounter, assert a draft note is returned, assert it is not saved until approved, assert it is saved after approval
- AI ICD Coding Assist: input free-text "patient presented with fever and cough", assert ICD-10 J22 or J06 is suggested
- AI Differential Diagnosis: input vitals + symptoms, assert ranked list is returned, assert list is collapsible in UI
- AI Patient Plain-Language Summary: assert output is in the patient's preferred locale, assert output does not contain ICD codes or clinical jargon
- AI Claim Scrubbing: submit a claim with a known rejection-trigger field, assert the field is flagged with risk indicator
- AI Outbreak Early Warning: inject 15 malaria diagnoses in 24 hours (above anomaly threshold), assert alert is generated and sent to medical officer
- i18n: switch UI locale to `sw`, assert all visible strings render in Kiswahili, assert no English fallback strings are visible in non-alert UI elements
- Provider failover: simulate primary provider timeout, assert secondary provider is called within 12 s

**Build:**
```bash
bash scripts/build-doc.sh projects/Medic8/05-testing-documentation/02-test-plan Medic8_TestPlan
```

---

### Task 29: Update Test Report template

**Files:**
- Modify: `projects/Medic8/05-testing-documentation/03-test-report/01-test-report-template.md`

**Key additions:**
- Add AI Intelligence test suite section to the report template
- Add i18n coverage section: string audit result, native speaker review sign-off

**Build:**
```bash
bash scripts/build-doc.sh projects/Medic8/05-testing-documentation/03-test-report Medic8_TestReport
```

---

### Task 30: Commit Batch 6

```bash
git add projects/Medic8/05-testing-documentation/
git commit -m "Medic8 overhaul: Phase 05 Testing Documentation (Batch 6)

- Test Strategy: AI Intelligence test strategy; i18n coverage audit; AI safety test requirement
- Test Plan: 8 new AI test cases; provider failover test; i18n locale switch test
- Test Report template: AI test suite section; i18n native speaker sign-off section

Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>"
git push
```

---

## Batch 7 — Deployment and Operations

**Commit after this batch.**

---

### Task 31: Update Deployment Guide

**Files:**
- Modify: `projects/Medic8/06-deployment-operations/01-deployment-guide/01-deployment-guide.md`

**Key additions:**
- AI Intelligence module deployment checklist: configure primary and secondary provider, set API keys in encrypted tenant settings, configure credit pack or flat fee billing, run `POST /api/ai/usage` health check
- i18n deployment checklist: assert zero `[I18N-GAP]` tags in all string files, confirm `lang/fr/` and `lang/sw/` are present in the deployment artifact, run automated string coverage audit

**Build:**
```bash
bash scripts/build-doc.sh projects/Medic8/06-deployment-operations/01-deployment-guide Medic8_DeploymentGuide
```

---

### Task 32: Update Runbook

**Files:**
- Modify: `projects/Medic8/06-deployment-operations/02-runbook/01-runbook.md`

**Key additions:**
- Incident: AI provider outage → runbook: check `ai_usage_log` for error codes, switch to secondary provider in admin panel, notify affected tenants, monitor failover
- Incident: AI credit exhaustion → runbook: notify tenant AI Administrator by email, AI features pause automatically, clinical features unaffected, top up via admin panel
- Incident: i18n string rendering English in non-English locale → runbook: identify missing key from browser console `[I18N-GAP]` log, add string to appropriate `lang/<locale>/` file, deploy hotfix

**Build:**
```bash
bash scripts/build-doc.sh projects/Medic8/06-deployment-operations/02-runbook Medic8_Runbook
```

---

### Task 33: Commit Batch 7

```bash
git add projects/Medic8/06-deployment-operations/
git commit -m "Medic8 overhaul: Phase 06 Deployment and Operations (Batch 7)

- Deployment Guide: AI module deployment checklist; i18n deployment checklist
- Runbook: AI provider outage playbook; credit exhaustion playbook; i18n fallback incident playbook

Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>"
git push
```

---

## Batch 8 — Agile Artifacts

**Commit after this batch.**

---

### Task 34: Update Sprint Planning, DoD, DoR

**Files:**
- Modify: `projects/Medic8/07-agile-artifacts/01-sprint-planning/01-sprint-planning.md`
- Modify: `projects/Medic8/07-agile-artifacts/02-dod/01-definition-of-done.md`
- Modify: `projects/Medic8/07-agile-artifacts/03-dor/01-definition-of-ready.md`

**`02-dod` additions:**
- "All user-visible strings exist in `en`, `fr`, and `sw` with zero `[I18N-GAP]` tags"
- "AI-generated outputs require explicit clinician approval before persistence — verified by automated test"
- "AI capability test suite passes with zero failures against sandbox provider API keys"

**`03-dor` additions:**
- "AI Intelligence stories: acceptance criteria include specific provider, locale, and approval-gate assertions"
- "i18n stories: acceptance criteria specify which locale is under test and include native speaker review for Kiswahili and French strings"

**Build all three:**
```bash
bash scripts/build-doc.sh projects/Medic8/07-agile-artifacts/01-sprint-planning Medic8_SprintPlanning
bash scripts/build-doc.sh projects/Medic8/07-agile-artifacts/02-dod Medic8_DefinitionOfDone
bash scripts/build-doc.sh projects/Medic8/07-agile-artifacts/03-dor Medic8_DefinitionOfReady
```

---

### Task 35: Commit Batch 8

```bash
git add projects/Medic8/07-agile-artifacts/
git commit -m "Medic8 overhaul: Phase 07 Agile Artifacts (Batch 8)

- DoD: added i18n string coverage gate; AI approval-gate test requirement
- DoR: added AI and i18n acceptance criteria requirements
- Sprint Planning: updated to reflect 32-module scope

Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>"
git push
```

---

## Batch 9 — End-User Documentation

**Commit after this batch.**

---

### Task 36: Update User Manual

**Files:**
- Modify: `projects/Medic8/08-end-user-documentation/01-user-manual/01-user-manual.md`

**Key additions:**
- Chapter: Changing your language — how to set UI language from the user profile (English, French, Kiswahili)
- Chapter: AI Intelligence features — what each capability does, how to use AI drafts, how to approve or discard a draft, where to see credit balance
- Chapter: AI Administrator guide — configuring providers, API keys, credit top-ups, monitoring usage

**Build:**
```bash
bash scripts/build-doc.sh projects/Medic8/08-end-user-documentation/01-user-manual Medic8_UserManual
```

---

### Task 37: Commit Batch 9 — Final

```bash
git add projects/Medic8/08-end-user-documentation/
git commit -m "Medic8 overhaul: Phase 08 End-User Documentation (Batch 9)

- User Manual: added language selection chapter; AI Intelligence user guide; AI Administrator guide

Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>"
git push
```

---

## Post-Overhaul: Update Project Memory

After all 9 batches are committed, update `C:\Users\Peter\.claude\projects\C--wamp64-www-srs-skills\memory\project_medic8.md` to reflect:
- 32 modules (31 clinical/admin + AI Intelligence)
- 7 books (not 10)
- Multi-language: English, French, Kiswahili
- AI module: credit pack or flat fee, provider-agnostic, 6 capabilities
- All documents regenerated as of 2026-04-17

---

*End of implementation plan. 37 tasks across 9 commit batches.*

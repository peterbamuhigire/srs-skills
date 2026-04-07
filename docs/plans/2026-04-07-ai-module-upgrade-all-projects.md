# AI Module Upgrade — 5 Projects Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Add domain-specific AI module sections to the PRD and SRS of Kulima, Medic8, LonghornERP, Maduuka, and BIRDC-ERP, following the AcademiaPro pattern (business-language PRD section + technical stimulus-response SRS FRs), and rebuild the affected `.docx` files.

**Architecture:** Sequential project-by-project upgrade. For each project: (1) update `_context/features.md`, (2) add `FR-AI` business section to PRD, (3) add technical `FR-AI-XXX` FRs to SRS functional requirements, (4) rebuild affected docx, (5) update `DOCUMENTATION-STATUS.md`, (6) commit and push.

**Reference pattern:** `projects/AcademiaPro/01-strategic-vision/01-prd/06-feature-requirements.md` — the `### FR-AI` section starting at line 162. Mirror this pattern (positioning blurb → 5 named features with Problem/What it does/Why owners pay/Pricing tier → packaging summary table → FR-AI-XXX technical references pointing to SRS).

**Tech Stack:** Markdown, Pandoc via `bash scripts/build-doc.sh <doc-dir> <OutputName>`, git

---

## PROJECT 1: Kulima (Farm Management SaaS)

SRS already has FR-AI-001 to FR-AI-006. Only the PRD business-language section is missing.

**Files in scope:**
- Modify: `projects/Kulima/_context/features.md`
- Modify: `projects/Kulima/01-strategic-vision/01-prd/01-prd.md`
- Read-verify: `projects/Kulima/02-requirements-engineering/01-srs/03-specific-requirements-functional.md` (lines 2270–2360)
- Build: `projects/Kulima/01-strategic-vision/01-prd/` → `Kulima_PRD.docx`
- Build: `projects/Kulima/02-requirements-engineering/01-srs/` → `Kulima_SRS.docx`
- Modify: `projects/Kulima/DOCUMENTATION-STATUS.md`

---

### Task 1.1: Update Kulima features context

**File:** `projects/Kulima/_context/features.md`

Append an "AI Farm Advisor Module" section at the end of the file:

```markdown
## AI Farm Advisor (Phase 3 Add-On)

**Tier:** Growth and Enterprise | **Phase:** 3 (add-on, off by default)

- AI-powered natural language Q&A in English, Luganda, and Swahili
- Photo-based pest and disease diagnosis (camera capture → instant identification)
- Personalised agronomic recommendations based on farm profile, crop, soil, and weather
- Seasonal planting calendar and calendar advisory
- Market timing advice (optimal sell window based on historical price patterns)
- Offline fallback: pre-loaded diagnostic guides when connectivity is unavailable
```

**Step 1:** Read the current end of `_context/features.md` to find the last line.

**Step 2:** Append the AI Farm Advisor section above.

**Step 3:** Confirm the file saves correctly.

---

### Task 1.2: Add FR-AI business section to Kulima PRD

**File:** `projects/Kulima/01-strategic-vision/01-prd/01-prd.md`

The PRD is a single large file. Locate the `## 8 Release Strategy` section (near end of file). Insert the FR-AI block immediately **before** the `## 8 Release Strategy` heading.

The block to insert follows the AcademiaPro pattern exactly:

```markdown
## FR-AI: AI Farm Advisor — Intelligent Farming Add-On

> **Positioning:** The AI Farm Advisor is a paid add-on, off by default. Farmers and agribusinesses activate it when they are ready for the next level of intelligence. Every feature is described in terms that a smallholder farmer or cooperative manager will understand immediately.

> **Pricing (indicative):** Starter — UGX 30,000/month; Growth — UGX 100,000/month; Enterprise — UGX 300,000/month. All plans include a configurable monthly query budget. The system enforces the budget and alerts the account owner at 80% consumption.

---

### AI Feature 1: Ask Any Farming Question in Your Language

**Who benefits:** Individual farmers, extension officers, cooperative field staff.

**The problem it solves:** A smallholder farmer in Mbale wakes up and notices yellow patches on her maize. She does not know a doctor or an agronomist she can call. Google results are in English and assume laboratory-grade equipment. By the time she gets help, a third of the crop may be lost.

**What it does:** The farmer types or voice-inputs her question in English, Luganda, or Swahili — "Embeera ya nnimiro yange" ("My farm looks sick") — and the system returns a plain-language answer with photos and step-by-step guidance, specifically for East African crops and conditions.

**Why farmers pay for it:** It replaces the need for an on-call extension officer for day-to-day questions. For a cooperative, it means 200 farmers get agronomic guidance simultaneously without hiring 200 extension workers.

**Pricing tier:** Starter and above.

**FR-AI-001** — see SRS Section 3, FR-AI-001 for full technical specification.

---

### AI Feature 2: Photograph a Sick Crop — Get an Instant Diagnosis

**Who benefits:** Individual farmers, cooperative field officers, farm managers.

**The problem it solves:** Pest and disease identification requires years of training. By the time a farmer identifies a problem and waits for an extension visit, a preventable outbreak has spread across the farm.

**What it does:** The farmer takes a photo of the affected leaf, stem, or fruit with their phone. Within 10 seconds, the system identifies the most likely cause (e.g., "Banana Fusarium wilt — 91% confidence") and recommends immediate action: isolate the affected stool, avoid irrigation spread, contact your cooperative.

**Why farmers pay for it:** Early detection prevents crop loss. A single prevented outbreak on a 2-acre banana farm is worth more than a year of subscription fees.

**Pricing tier:** Starter and above.

**FR-AI-002** — see SRS Section 3, FR-AI-002 for full technical specification.

---

### AI Feature 3: Get a Farm Plan Built for Your Specific Conditions

**Who benefits:** Farm managers, serious smallholders, agribusiness owners.

**The problem it solves:** Generic advice ("plant maize in March") does not account for the farmer's specific soil type, elevation, rainfall pattern, available inputs, or crop history. Following generic advice on degraded soil produces generic (poor) results.

**What it does:** The system reads the farm's recorded soil data, historical yields, GPS location (weather zone), available budget for inputs, and target market, then produces a personalised growing plan: which variety to plant, how much input to apply, when to irrigate, what yield to target, and which diseases to watch for.

**Why farmers pay for it:** A plan built on real farm data produces measurable yield improvements. Cooperatives use it as a member benefit that justifies the subscription.

**Pricing tier:** Growth and above.

**FR-AI-003** — see SRS Section 3, FR-AI-003 for full technical specification.

---

### AI Feature 4: Know When to Plant — Not Just the Calendar Date

**Who benefits:** Farmers planning a new season, cooperative procurement officers.

**The problem it solves:** The official planting calendar says "plant in March." But this year, rains started three weeks late. Farmers who followed the calendar planted into dry soil and lost germination. Climate variability has made fixed calendars unreliable.

**What it does:** Two weeks before the typical planting window, the system generates a "Plant or Wait?" advisory based on current Open-Meteo forecast data and historical rainfall records for the farm's GPS zone. It tells the farmer: "Rains are 2 weeks delayed. Recommended planting window: 18–25 April instead of 1–10 April."

**Why farmers pay for it:** A planting timing miss costs an entire season. Climate-adjusted advice is the most valuable agronomic guidance a farmer can receive.

**Pricing tier:** Growth and above.

**FR-AI-004** — see SRS Section 3, FR-AI-004 for full technical specification.

---

### AI Feature 5: Know When to Sell for the Best Price

**Who benefits:** Individual farmers, cooperative marketing officers, agribusiness traders.

**The problem it solves:** Smallholder farmers sell when they need cash, not when prices are highest. Traders exploit this by buying at harvest (low prices) and holding until prices rise. Farmers leave 20–40% of potential revenue on the table every season.

**What it does:** Based on historical market price patterns for the farmer's crop and nearest market, the system predicts the optimal selling window: "Maize prices at Jinja market typically peak in weeks 8–10 post-harvest. If you can store 10 bags, selling then vs. now would earn you an additional UGX 120,000." The farmer makes an informed choice.

**Why farmers pay for it:** A single optimal selling decision recovers the entire cost of the annual subscription. Cooperatives use it to coordinate bulk selling and negotiate higher prices.

**Pricing tier:** Growth and above.

**FR-AI-005** — see SRS Section 3, FR-AI-005 for full technical specification.

---

### AI Farm Advisor Packaging Summary

| Feature | Starter (UGX 30K/mo) | Growth (UGX 100K/mo) | Enterprise (UGX 300K/mo) |
|---|---|---|---|
| Natural Language Q&A | Yes | Yes | Yes |
| Photo Pest/Disease Diagnosis | Yes | Yes | Yes |
| Personalised Farm Plan | — | Yes | Yes |
| Seasonal Planting Advisory | — | Yes | Yes |
| Market Timing Advice | — | Yes | Yes |
| Offline Fallback Guides | Yes | Yes | Yes |

**All features are off by default within the purchased plan.** The account owner enables each feature individually from the AI Advisor settings screen.

```

**Step 1:** Read the file to locate the exact text of the `## 8 Release Strategy` heading.

**Step 2:** Insert the above block immediately before that heading, preceded by a blank line.

**Step 3:** Confirm the file is well-formed Markdown (no broken headings, blank lines before/after headings).

---

### Task 1.3: Verify Kulima SRS AI FRs

**File:** `projects/Kulima/02-requirements-engineering/01-srs/03-specific-requirements-functional.md` (lines 2270–2360)

Read the FR-AI-001 to FR-AI-006 section. Verify each FR:
- Follows stimulus-response pattern ("When [stimulus], the system shall [response]")
- Includes measurable thresholds (response time, confidence percentage, or equivalent)
- References offline fallback FR-AI-006

If any FR lacks a measurable threshold, add one. If the section ends without a proper concluding blank line, add it.

**Step 1:** Read lines 2270–2360.

**Step 2:** Fix any missing thresholds or stimulus-response deviations.

**Step 3:** Confirm all 6 FRs are complete.

---

### Task 1.4: Build Kulima PRD docx

**Command:**
```bash
cd C:/wamp64/www/srs-skills && bash scripts/build-doc.sh projects/Kulima/01-strategic-vision/01-prd Kulima_PRD
```

Expected output: `projects/Kulima/01-strategic-vision/Kulima_PRD.docx`

If the build fails: read the error, check `manifest.md` in the PRD directory, fix any missing blank lines or broken Markdown syntax.

---

### Task 1.5: Build Kulima SRS docx

**Command:**
```bash
cd C:/wamp64/www/srs-skills && bash scripts/build-doc.sh projects/Kulima/02-requirements-engineering/01-srs Kulima_SRS
```

Expected output: `projects/Kulima/02-requirements-engineering/Kulima_SRS.docx`

---

### Task 1.6: Update Kulima DOCUMENTATION-STATUS.md

In `projects/Kulima/DOCUMENTATION-STATUS.md`:
1. Update Phase 01 PRD row: set `.docx` Built to `Kulima_PRD.docx`
2. Update Phase 02 SRS row: set `.docx` Built to `Kulima_SRS.docx`
3. Update Progress Summary: increment Complete counts for Phase 01 (3→3) and Phase 02 (2→3 if Stakeholder Analysis done, else note).
4. Add a note under Immediate Next Steps: "AI Farm Advisor module added to PRD (FR-AI-001 to FR-AI-005 PRD section; FR-AI-001 to FR-AI-006 SRS FRs)."

---

### Task 1.7: Commit and push Kulima AI upgrade

```bash
cd C:/wamp64/www/srs-skills
git add projects/Kulima/
git commit -m "feat(kulima): add AI Farm Advisor module — PRD business section + SRS FRs; build PRD and SRS docx"
git push
```

---

---

## PROJECT 2: Medic8 (Healthcare SaaS)

No AI content in any document. PRD has `06-feature-requirements.md`. SRS has `04-functional-requirements.md`. No docx built yet.

**AI features to add (5):**
1. At-Risk Patient Early Warning System
2. AI-Assisted Differential Diagnosis Support
3. Automated Clinical Note Summarisation
4. Pharmacy Demand Forecasting
5. Disease Surveillance and Outbreak Detection

**Pricing tiers:** Starter — UGX 200,000/month; Growth — UGX 600,000/month; Enterprise — UGX 1,500,000/month (healthcare SaaS commands premium pricing; rural clinics anchor on Starter).

**Files in scope:**
- Modify: `projects/Medic8/_context/features.md`
- Modify: `projects/Medic8/01-strategic-vision/01-prd/06-feature-requirements.md`
- Modify: `projects/Medic8/02-requirements-engineering/01-srs/04-functional-requirements.md`
- Build: `projects/Medic8/01-strategic-vision/01-prd/` → `Medic8_PRD.docx`
- Build: `projects/Medic8/02-requirements-engineering/01-srs/` → `Medic8_SRS.docx`
- Modify: `projects/Medic8/DOCUMENTATION-STATUS.md`

---

### Task 2.1: Update Medic8 features context

**File:** `projects/Medic8/_context/features.md`

Append an "AI Clinical Intelligence Module" section at the end of the file:

```markdown
## AI Clinical Intelligence Module (Enterprise Add-On)

**Tier:** Starter and above (tiered) | **Phase:** 3 (add-on, off by default)

- At-risk patient early warning: daily risk scoring across all admitted and OPD patients using vitals trends, lab results, and clinical notes
- AI-assisted differential diagnosis support: suggests differential diagnoses from ICD-10/ICD-11 based on presenting symptoms and vitals — decision aid, not a replacement for clinical judgment
- Automated clinical note summarisation: generates concise SOAP summary from free-text consultation notes
- Pharmacy demand forecasting: predicts drug stockouts 14 days in advance based on consumption patterns and seasonal disease load
- Disease surveillance: detects unusual case clusters (symptom, diagnosis, geography) and generates outbreak alerts for the facility's medical officer
```

---

### Task 2.2: Add FR-AI business section to Medic8 PRD

**File:** `projects/Medic8/01-strategic-vision/01-prd/06-feature-requirements.md`

Read the current end of this file, then append the `## FR-AI: AI Clinical Intelligence Module` section. Follow the AcademiaPro pattern exactly.

Write the following 5 features:

**Feature 1 — Know Which Patients Are About to Deteriorate — Before It Is Too Late**
- Who benefits: Nurses, Medical Officers, Hospital Administrators
- Problem: Manual bedside monitoring misses early warning signs. A patient's vitals may be trending downward for 6 hours before anyone notices. By the time a clinical emergency is declared, the window for simple intervention has closed.
- What it does: Every hour, the system scores every admitted patient on a modified Early Warning Score (EWS) based on recorded vitals (BP, temp, pulse, SpO2, respiratory rate, GCS). Patients crossing a threshold trigger an alert to the duty nurse and attending doctor: "Patient in Ward 3B, Bed 7 — EWS rising. Review recommended." No clinical diagnosis is made — only the alert.
- Why owners pay: Early deterioration alerts reduce ICU admissions and preventable deaths. Facilities using early warning systems demonstrate better outcomes, which attracts donor funding and insurance contracts.
- Pricing tier: Growth and above.
- FR-AI-001 reference

**Feature 2 — Differential Diagnosis Support for Overstretched Doctors**
- Who benefits: Clinical officers, general practitioners, rotating doctors
- Problem: A clinical officer in a rural health centre sees 80 patients per day with a 4-year training background. For uncommon presentations, they need a second opinion — which is rarely available.
- What it does: After entering presenting symptoms, duration, and key vitals, the doctor clicks "Suggest Diagnoses." The system returns the 5 most likely ICD-10 diagnoses ranked by probability, with a brief rationale and the most differentiating investigation to confirm. It is a decision aid — the doctor remains responsible for the final diagnosis.
- Why owners pay: It reduces missed diagnoses, improves investigation ordering efficiency, and provides clinical support in under-resourced settings. NGO and government clients specifically request this for community health worker programmes.
- Pricing tier: Growth and above.
- FR-AI-002 reference

**Feature 3 — Write the Clinical Note Summary Automatically**
- Who benefits: Doctors, clinical officers, discharge coordinators
- Problem: A doctor seeing 60 patients per day spends 20–30% of consultation time writing notes. Notes written under time pressure are terse and sometimes miss key information. Referral letters and discharge summaries take 10–15 minutes each to write.
- What it does: After a consultation, the doctor clicks "Summarise." The system generates a structured SOAP summary (Subjective, Objective, Assessment, Plan) from the free-text notes entered during the visit. The doctor reviews, edits if needed, and approves. Only the approved version is saved in the patient record. It also generates a draft referral letter or discharge summary on request.
- Why owners pay: A doctor who saves 15 minutes per patient, across 60 patients, recovers 15 hours of clinical time per week. That time goes back to patients.
- Pricing tier: Starter and above.
- FR-AI-003 reference

**Feature 4 — Know Which Drugs Will Run Out Before They Actually Do**
- Who benefits: Pharmacy managers, procurement officers, hospital administrators
- Problem: Drug stockouts are discovered when a pharmacist reaches for a medication and finds an empty shelf. By then, patients have already been turned away or prescribed alternatives. Emergency procurement is expensive and slow.
- What it does: Every morning, the system analyses the current pharmacy stock levels against average daily consumption for the past 28 days, adjusted for seasonal disease patterns. It produces a "Stockout Risk" report: "Amoxicillin 500mg will run out in 9 days at current consumption. Recommended order: 500 units." The procurement officer places the order before the stockout, not after.
- Why owners pay: A single avoided drug stockout — especially for high-volume essentials like antimalarials, ORS, or ARVs — more than pays for the entire AI module for a month. Donor-funded facilities are penalised for stockouts by their funders.
- Pricing tier: Starter and above.
- FR-AI-004 reference

**Feature 5 — Detect a Disease Outbreak Before It Becomes a Crisis**
- Who benefits: Medical Officers, Public Health Officers, Hospital Directors
- Problem: An unusual cluster of malaria cases begins in one ward. Three days later, it is confirmed as a typhoid outbreak. Public health response has been delayed because no one was monitoring cross-patient patterns — only individual cases.
- What it does: The system continuously monitors diagnosis patterns across all patients. When any diagnosis (ICD-10 code) appears more than 2 standard deviations above its 30-day baseline within a 72-hour window, it generates a "Cluster Alert" for the Medical Officer: "14 cases of Typhoid fever (A01.0) recorded in the last 48 hours — 3.2× baseline. Geographic concentration: Wakiso district patients." The Medical Officer decides how to respond.
- Why owners pay: Early outbreak detection protects the community, protects the facility from being the source of a documented outbreak, and enables proactive MOH notification — which is a legal requirement under the Public Health Act.
- Pricing tier: Enterprise only.
- FR-AI-005 reference

**Packaging table:**

| Feature | Starter (UGX 200K/mo) | Growth (UGX 600K/mo) | Enterprise (UGX 1.5M/mo) |
|---|---|---|---|
| Clinical Note Summarisation | Yes | Yes | Yes |
| Pharmacy Demand Forecasting | Yes | Yes | Yes |
| At-Risk Patient Early Warning | — | Yes | Yes |
| Differential Diagnosis Support | — | Yes | Yes |
| Disease Surveillance / Outbreak Detection | — | — | Yes |

---

### Task 2.3: Add FR-AI technical FRs to Medic8 SRS

**File:** `projects/Medic8/02-requirements-engineering/01-srs/04-functional-requirements.md`

Read the end of this file to find the last existing FR section, then append a new `### FR-AI: AI Clinical Intelligence Module` section.

Write 5 technical FRs following the Medic8 SRS FR pattern (stimulus-response, measurable thresholds, IEEE 830-compliant):

**FR-AI-001 (At-Risk Patient Early Warning):**
When the hourly risk-scoring job runs for an admitted patient who has at least 3 vital signs recorded in the current admission episode, the system shall compute a modified Early Warning Score (EWS) using the configured scoring matrix (BP, temperature, pulse rate, SpO₂, respiratory rate, GCS — each component scored 0–3 per configured thresholds), sum the component scores into a total EWS, store the score in `patient_ews_log` with patient ID, ward, timestamp, and component scores, and — if the total EWS has increased by 3 or more points compared to the previous recorded EWS for that patient — dispatch an in-app alert to the assigned nurse and attending doctor within 60 seconds of score computation. The alert shall display the patient's name, bed number, current EWS, previous EWS, and the component driving the largest increase. The system shall not make a clinical diagnosis; the alert text shall include the disclaimer "This is a monitoring alert, not a clinical diagnosis." The system shall complete the scoring pass for all admitted patients within 5 minutes of the scheduled hourly trigger, for up to 500 concurrently admitted patients.

**FR-AI-002 (Differential Diagnosis Support):**
When a clinician submits a differential diagnosis request containing at least 3 of: presenting complaint (free text), symptom duration, patient age, patient sex, and at least 2 vital signs, the system shall return within 3,000 ms a ranked list of up to 5 ICD-10 diagnosis codes with: rank, ICD-10 code and description, probability indicator (High/Medium/Low — not a numeric percentage), a one-sentence clinical rationale, and the single most differentiating investigation recommended to confirm or exclude the diagnosis. The system shall display a fixed disclaimer on every response: "This is a decision aid. Clinical responsibility remains with the treating clinician." The system shall not store the differential diagnosis suggestions in the patient's clinical record without the clinician explicitly selecting and approving one or more suggestions.

**FR-AI-003 (Clinical Note Summarisation):**
When a clinician requests a SOAP summary for a consultation that contains at least 50 characters of free-text clinical notes, the system shall generate a structured SOAP summary (Subjective, Objective, Assessment, Plan) within 5,000 ms and display it in a draft review panel. The clinician shall be able to edit any section of the draft. When the clinician clicks Approve, the system shall save the approved SOAP text as the consultation's structured note, linked to the consultation ID, with a `ai_generated: true` flag and the clinician's user ID and approval timestamp. The system shall not save any AI-generated text to the patient record without explicit clinician approval action; dismissing the draft without approval shall discard the suggestion with no record written.

When a clinician requests a discharge summary draft for an inpatient episode, the system shall aggregate the admission note, ward round notes, investigation results, and active prescriptions from the episode, generate a draft discharge summary (Diagnosis, Summary of Hospital Course, Discharge Medications, Follow-up Instructions) within 8,000 ms, and present it in the same draft-review-approve workflow as above.

**FR-AI-004 (Pharmacy Demand Forecasting):**
When the nightly pharmacy forecast job runs, the system shall: for each active drug in the pharmacy catalogue with at least 28 days of dispensing history, compute the mean daily dispensing rate for the preceding 28 days, apply a seasonal adjustment factor derived from the facility's historical same-period dispensing data for the preceding 2 years (or the full history if less than 2 years), compute projected days of stock remaining as `current_stock_quantity ÷ adjusted_daily_rate`, and write a forecast record to `pharmacy_forecast_log` with drug ID, current stock, adjusted daily rate, projected days of stock, and forecast date. For any drug with projected days of stock ≤ 14 days, the system shall generate a "Stockout Risk" alert visible to the Pharmacy Manager role, showing drug name, current quantity, projected stockout date, and a recommended order quantity equal to 45 days of adjusted daily consumption minus current stock. The nightly job shall complete processing for up to 500 active drugs within 10 minutes of the scheduled trigger.

**FR-AI-005 (Disease Surveillance):**
When the 6-hourly surveillance scan runs, the system shall: for each ICD-10 code recorded in the current facility's patient records in the preceding 72 hours, compute the count of new diagnoses, compare it to the 30-day rolling baseline for that code (mean + 2 standard deviations), and — if the 72-hour count exceeds the baseline threshold — create a `surveillance_alert` record with ICD-10 code, alert trigger count, baseline value, ratio (trigger count ÷ baseline mean), 72-hour window start and end timestamps, and a geographic breakdown showing the top 3 patient districts by diagnosis count. The system shall dispatch an in-app alert to all users holding the Medical Officer or Hospital Director role within 5 minutes of alert creation. The alert shall include the disclaimer "This is a statistical cluster alert. Confirmation of an outbreak requires clinical and epidemiological investigation." The system shall not automatically notify external parties (MOH, DHIS2) without Medical Officer explicit action.

---

### Task 2.4: Build Medic8 PRD docx

```bash
cd C:/wamp64/www/srs-skills && bash scripts/build-doc.sh projects/Medic8/01-strategic-vision/01-prd Medic8_PRD
```

Expected output: `projects/Medic8/01-strategic-vision/Medic8_PRD.docx`

---

### Task 2.5: Build Medic8 SRS docx

```bash
cd C:/wamp64/www/srs-skills && bash scripts/build-doc.sh projects/Medic8/02-requirements-engineering/01-srs Medic8_SRS
```

Expected output: `projects/Medic8/02-requirements-engineering/Medic8_SRS.docx`

---

### Task 2.6: Update Medic8 DOCUMENTATION-STATUS.md

1. Update Phase 01 PRD row: `.docx` Built → `Medic8_PRD.docx`, Status → Complete
2. Update Phase 02 SRS row: `.docx` Built → `Medic8_SRS.docx`, Status → Complete
3. Add AI module note to Immediate Next Steps.
4. Update progress summary counts.

---

### Task 2.7: Commit and push Medic8 AI upgrade

```bash
cd C:/wamp64/www/srs-skills
git add projects/Medic8/
git commit -m "feat(medic8): add AI Clinical Intelligence module — PRD FR-AI section + SRS FR-AI-001-005; build PRD and SRS docx"
git push
```

---

---

## PROJECT 3: LonghornERP (ERP SaaS)

**Structure note:** LonghornERP SRS is organised by module, one directory per module under `02-requirements-engineering/01-srs/01-modules/`. 14 business modules (01-accounting through 14-assets) already exist with docx. Create a new `15-ai-intelligence/` module directory.

For the PRD: the existing PRD uses a different structure (cover, executive summary, problem statement, etc.) with no feature-requirements section. Add a new `10-ai-intelligence.md` file to `01-strategic-vision/01-prd/`.

**AI features to add (5):**
1. Cash Flow Intelligence — predict cash position 30/60/90 days out
2. GL Anomaly Detection — flag unusual journal entries and potential fraud
3. Sales Demand Forecasting — suggest optimal stock reorder quantities
4. Debtor Default Risk Scoring — rank customers by payment risk
5. Automated Narrative Financial Reports — plain-English monthly commentary

**Pricing tiers:** Starter — UGX 100,000/month; Growth — UGX 300,000/month; Enterprise — UGX 800,000/month.

**Files in scope:**
- Modify: `projects/LonghornERP/_context/modules.md`
- Create: `projects/LonghornERP/01-strategic-vision/01-prd/10-ai-intelligence.md`
- Modify: `projects/LonghornERP/01-strategic-vision/01-prd/manifest.md`
- Create dir: `projects/LonghornERP/02-requirements-engineering/01-srs/01-modules/15-ai-intelligence/`
- Create: `projects/LonghornERP/02-requirements-engineering/01-srs/01-modules/15-ai-intelligence/00-cover.md`
- Create: `projects/LonghornERP/02-requirements-engineering/01-srs/01-modules/15-ai-intelligence/01-introduction.md`
- Create: `projects/LonghornERP/02-requirements-engineering/01-srs/01-modules/15-ai-intelligence/02-ai-features.md`
- Create: `projects/LonghornERP/02-requirements-engineering/01-srs/01-modules/15-ai-intelligence/03-nfrs.md`
- Create: `projects/LonghornERP/02-requirements-engineering/01-srs/01-modules/15-ai-intelligence/04-traceability.md`
- Create: `projects/LonghornERP/02-requirements-engineering/01-srs/01-modules/15-ai-intelligence/manifest.md`
- Build: `projects/LonghornERP/01-strategic-vision/01-prd/` → `LonghornERP_PRD.docx`
- Build: `projects/LonghornERP/02-requirements-engineering/01-srs/01-modules/15-ai-intelligence/` → `LonghornERP_SRS_AIIntelligence.docx`

---

### Task 3.1: Update LonghornERP modules context

**File:** `projects/LonghornERP/_context/modules.md`

Add a new row to the "Add-On Modules" table:

```markdown
| 17 | AI Intelligence | AI_INTELLIGENCE | Cash flow forecasting, GL anomaly detection, demand forecasting, debtor risk scoring, and narrative financial reports — available as a paid add-on on Professional plans and above |
```

Also add a note below the Add-On Modules table:

```markdown
**Note — AI Intelligence Module:** Available on Professional, Business, and Enterprise plans only. Off by default. Account owners activate individual AI features from Settings → AI Intelligence. Requires at least 6 months of transaction history for meaningful forecasting outputs.
```

---

### Task 3.2: Create LonghornERP PRD AI section

**File:** `projects/LonghornERP/01-strategic-vision/01-prd/10-ai-intelligence.md`

Create this new file. Write a full `# AI Intelligence Module — Intelligent Business Add-On` section following the AcademiaPro PRD AI pattern.

Write the following 5 features:

**Feature 1 — Know Your Cash Position for the Next 90 Days**
- Who benefits: Finance Directors, Business Owners, CFOs
- Problem: A managing director approves a large equipment purchase on Monday, not knowing that a UGX 15M VAT remittance is due to URA on Thursday and payroll runs on Friday. The bank account is fine today but will be negative by the weekend.
- What it does: Every morning, the system reads the AR aging (when customers are expected to pay), AP schedule (when suppliers are due), payroll dates, loan repayment schedules, and tax payment dates. It produces a 90-day rolling cash flow forecast with three curves: Best Case, Base Case, and Worst Case. The Finance Director sees exactly which weeks are at risk — before they arrive.
- Why owners pay: One cash flow crisis averted, one loan facility not drawn down in panic, one supplier relationship not strained — the AI module pays for itself in the first month.
- Pricing tier: Professional and above.
- FR-AI-001 reference

**Feature 2 — Catch Unusual Journal Entries Before the Auditor Does**
- Who benefits: Finance Directors, External Auditors, Managing Directors
- Problem: GL fraud typically involves small, repeated unusual journal entries — round numbers, unusual account combinations, or entries posted at unusual times (weekends, late night). Manual review of a 10,000-line journal register is impractical. Fraud is usually discovered by accident or by auditors, not by internal controls.
- What it does: After each posting cycle, the system analyses all new journal entries against behavioural baselines: unusual posting times, unusual debit/credit account combinations, amounts that are round numbers or that match suspicious thresholds, and entries created by users who normally do not post to those accounts. Flagged journals appear in the Finance Director's "Anomaly Inbox" with a brief explanation of what was unusual. The Finance Director reviews and clears or escalates.
- Why owners pay: Internal fraud detection that would otherwise require hiring an internal auditor is automated. The Audit Log module already records every action — this module makes sense of the log.
- Pricing tier: Business and Enterprise.
- FR-AI-002 reference

**Feature 3 — Know What to Reorder Before Your Shelves Run Out**
- Who benefits: Procurement Managers, Inventory Controllers, Branch Managers
- Problem: A procurement officer orders inventory based on intuition and the last stockout they remember. They over-order slow-moving items (tying up cash) and under-order fast movers (causing stockouts). Neither problem is visible until it is already a problem.
- What it does: Every Sunday, the system analyses the last 90 days of sales velocity per product per branch, applies seasonal adjustment based on same-period performance in prior years, and generates a Reorder Recommendation Report: for each product below or near its reorder level, the system recommends an exact order quantity calculated to cover 45 days of adjusted demand without over-ordering. The procurement officer reviews and converts recommendations to Purchase Requisitions with one click.
- Why owners pay: Cash freed from over-stocked slow-movers, stockout revenue losses eliminated. In a 10-branch business, optimising inventory alone typically frees 15–25% of the working capital tied in stock.
- Pricing tier: Professional and above.
- FR-AI-003 reference

**Feature 4 — Flag the Customers Most Likely to Pay Late — Before You Give Them More Credit**
- Who benefits: Credit Controllers, Sales Managers, Finance Directors
- Problem: A salesperson opens a new sales order for a customer with a UGX 5M credit limit. Unknown to the salesperson, this customer has paid late 4 times in the last 3 terms and currently has a 60-day overdue invoice. The credit controller only finds out when the order is already confirmed.
- What it does: Before a new credit sale is confirmed for any customer, the system runs the customer through a Risk Scorecard — payment history, average days-to-pay, current overdue balance, and trend direction. If the score is Amber or Red, the sales screen displays a warning: "Customer risk: High. Last 3 invoices paid average 38 days late. Current overdue: UGX 1.2M. Proceed?" The sales manager can override with a reason, which is logged.
- Why owners pay: Bad debt reduction. One prevented bad debt can cover 12 months of subscription fees. Credit teams use the weekly risk ranking to prioritise collection calls.
- Pricing tier: Growth and above.
- FR-AI-004 reference

**Feature 5 — Get a Plain-English Explanation of What the Numbers Mean**
- Who benefits: Managing Directors, Board Members, Business Owners who are not accountants
- Problem: A business owner receives a 12-page financial report every month. They read the revenue line and the profit line, skip the rest, and sign the acknowledgement. They are missing important signals buried in the numbers.
- What it does: On the 5th of each month, the system reads the finalised P&L, Balance Sheet, and Cash Flow for the preceding month and generates a 3-paragraph Management Commentary in plain English: what changed vs. last month, what changed vs. same month last year, and the 3 most important things the owner should act on this month. No accounting jargon. The commentary is sent as a push notification summary with a link to the full report.
- Why owners pay: It makes the monthly accounts intelligible to every level of management. Board packs become readable. The owner can discuss the business with confidence.
- Pricing tier: Business and Enterprise.
- FR-AI-005 reference

**Packaging table:**

| Feature | Professional (UGX 100K/mo) | Business (UGX 300K/mo) | Enterprise (UGX 800K/mo) |
|---|---|---|---|
| Cash Flow Intelligence | Yes | Yes | Yes |
| Demand Forecasting & Reorder | Yes | Yes | Yes |
| Debtor Default Risk Scoring | Yes | Yes | Yes |
| GL Anomaly Detection | — | Yes | Yes |
| Narrative Financial Reports | — | Yes | Yes |

---

### Task 3.3: Update LonghornERP PRD manifest.md

**File:** `projects/LonghornERP/01-strategic-vision/01-prd/manifest.md`

Read the current manifest. Append `10-ai-intelligence.md` to the file list in the correct alphabetical/numeric order.

---

### Task 3.4: Create LonghornERP SRS AI module files

**Directory:** `projects/LonghornERP/02-requirements-engineering/01-srs/01-modules/15-ai-intelligence/`

Read an existing module for structural reference (e.g., `01-modules/01-accounting/01-introduction.md` and `03-journal-entries.md`) to match formatting exactly.

Create the following files:

**`00-cover.md`** — Cover page: "LonghornERP — Software Requirements Specification — Module 15: AI Intelligence", version, date, owner.

**`01-introduction.md`** — Introduction section covering: purpose, scope (this module defines FR-AI-001 to FR-AI-005), definitions (AI Intelligence Module, Cash Flow Forecast, Anomaly Score, Risk Scorecard, Narrative Commentary), overview.

**`02-ai-features.md`** — The 5 technical FRs. Write each following the LonghornERP SRS FR pattern (bold identifier `**FR-AI-XXX:**` + full stimulus-response text with measurable thresholds):

- **FR-AI-001 (Cash Flow Forecast):** When the nightly cash flow forecast job runs, the system shall retrieve all open AR invoices (grouped by due date and customer payment-behaviour tier), all scheduled AP payment records (due dates from purchase orders and recurring payment schedules), the next payroll run date and net payroll amount from HR, all loan repayment schedules, and all tax remittance dates from the tax calendar, project a daily net cash position for the next 90 calendar days in three scenarios: Best Case (all AR collected on due date, all AP paid on last allowable date), Base Case (AR collected at customer's historical average days-to-pay, AP paid on due date), and Worst Case (AR collected 30 days beyond due date, AP paid on due date), store all 270 projection records (3 scenarios × 90 days) in `ai_cashflow_forecast` with tenant ID, scenario, date, projected balance, and calculation timestamp, and surface the worst-case trough date and amount in the Finance Director dashboard within 2,000 ms of query. The job shall complete for tenants with up to 10,000 open transactions within 5 minutes of the scheduled 02:00 EAT trigger.

- **FR-AI-002 (GL Anomaly Detection):** When the post-close anomaly scan runs after each accounting period close, the system shall evaluate every journal entry posted in the closed period against four anomaly classifiers: (1) Time Anomaly — entry posted between 22:00 and 05:00 EAT or on a public holiday, (2) Account-Pair Anomaly — debit/credit account combination that has not appeared in the prior 12 months of journal history for this tenant, (3) Round-Number Anomaly — entry amount is a multiple of 1,000,000 UGX with no corresponding source document, (4) Author Anomaly — entry posted by a user whose role has not posted to one of the referenced accounts in the prior 90 days. Each anomaly classifier shall produce a score of 0 (no anomaly) or 1 (anomaly present). Any journal entry scoring 2 or more on the combined classifier shall be written to `ai_anomaly_flags` with journal ID, classifier scores, composite score, and flag timestamp, and shall appear in the Finance Director's Anomaly Inbox. The Anomaly Inbox shall allow the Finance Director to mark each flag as "Reviewed — No Issue" or "Escalated — Investigation Required"; unreviewed flags older than 7 days shall escalate automatically. The scan shall process up to 50,000 journal lines per period within 15 minutes of period-close trigger.

- **FR-AI-003 (Demand Forecasting):** When the Sunday demand forecast job runs, the system shall: for each active inventory item with at least 90 days of sales movement history, compute the 90-day weighted moving average daily demand (more recent weeks weighted higher), apply a seasonal index derived from the ratio of the corresponding 13-week period's demand in the prior year to the annual average daily demand for that year, compute projected days of stock as `current_on_hand ÷ (weighted_avg × seasonal_index)`, and write a forecast record to `ai_demand_forecast` with item ID, branch ID, current stock, adjusted daily demand, projected days of stock, and recommended reorder quantity = `(45 × adjusted_daily_demand) - current_on_hand` (floored at zero). The system shall display items with projected days of stock < 21 days in a "Reorder Recommendations" panel in the Procurement module. The Finance Manager or Procurement Officer shall be able to convert any recommendation to a Purchase Requisition with a single click, pre-populated with the recommended quantity. The job shall process up to 5,000 item-branch combinations within 10 minutes of the scheduled Sunday 01:00 EAT trigger.

- **FR-AI-004 (Debtor Risk Scoring):** When a Sales module user submits a new credit sales order for a customer whose credit account is active, the system shall compute the customer's Risk Score before the order is confirmed using the following weighted scorecard: (a) Average days-to-pay in the last 12 months (0 = ≤30 days, 10 = 31–60 days, 25 = >60 days) — weight 40%, (b) Current overdue balance as a percentage of credit limit (0 = 0%, 10 = 1–25%, 25 = >25%) — weight 30%, (c) Number of late-paid invoices in the last 6 months (0 = 0, 10 = 1–2, 25 = ≥3) — weight 20%, (d) Trend direction (0 = improving, 10 = stable, 25 = worsening) — weight 10%. A composite score of 0–14 = Green (no warning), 15–24 = Amber (warning displayed, order proceeds), 25–100 = Red (warning displayed, order held pending manager approval). For Amber and Red scores, the system shall display a risk summary on the order screen before confirmation. For Red scores, the order shall require explicit approval from a user holding the Sales Manager role or above before it is confirmed; the approval action and reason shall be logged in the audit trail.

- **FR-AI-005 (Narrative Reports):** When the 5th calendar day of the month is reached and the preceding month's accounting period is in Closed status, the system shall generate a Management Commentary document for the closed period containing: (1) a one-sentence headline comparing this month's net profit to last month's and to the same month last year, (2) a paragraph identifying the 3 largest revenue variances vs. budget (positive or negative) with a one-clause explanation, (3) a paragraph identifying the 3 largest expense variances vs. budget with a one-clause explanation, (4) a "3 Things to Act On This Month" list derived from the variance analysis and the cash flow forecast for the upcoming month. The commentary shall be generated in ≤ 15,000 tokens using the configured LLM provider (Claude API via `claude-ai` skill pattern), stored as a PDF-renderable HTML document in `ai_narratives`, and pushed as a notification to all users holding the Finance Director, Managing Director, or Board Observer role. The generation job shall complete within 60 seconds of trigger. The Finance Director shall be able to edit the generated commentary before it is published to Board Observer role recipients.

**`03-nfrs.md`** — Non-functional requirements for the AI Intelligence module: response time (forecast jobs: complete within stated windows), accuracy (demand forecast MAE < 20% against actuals, measured monthly), privacy (no customer data leaves the tenant boundary — all AI processing uses the tenant's own transaction history + Claude API for narrative generation only), availability (AI features degrade gracefully — core ERP continues if AI service is unavailable), data minimum (features requiring history display a "Insufficient history" message rather than generating unreliable forecasts when < 90 days of data exists).

**`04-traceability.md`** — Traceability table mapping FR-AI-001 to FR-AI-005 to their originating PRD AI features (AI-F1 to AI-F5 in `10-ai-intelligence.md`).

**`manifest.md`** — List all 5 files in order: `00-cover.md`, `01-introduction.md`, `02-ai-features.md`, `03-nfrs.md`, `04-traceability.md`.

---

### Task 3.5: Build LonghornERP PRD docx

```bash
cd C:/wamp64/www/srs-skills && bash scripts/build-doc.sh projects/LonghornERP/01-strategic-vision/01-prd LonghornERP_PRD
```

Expected output: `projects/LonghornERP/01-strategic-vision/LonghornERP_PRD.docx`

---

### Task 3.6: Build LonghornERP SRS AI Intelligence docx

```bash
cd C:/wamp64/www/srs-skills && bash scripts/build-doc.sh "projects/LonghornERP/02-requirements-engineering/01-srs/01-modules/15-ai-intelligence" LonghornERP_SRS_AIIntelligence
```

Expected output: `projects/LonghornERP/02-requirements-engineering/01-srs/01-modules/15-ai-intelligence/LonghornERP_SRS_AIIntelligence.docx`

---

### Task 3.7: Commit and push LonghornERP AI upgrade

```bash
cd C:/wamp64/www/srs-skills
git add projects/LonghornERP/
git commit -m "feat(longhorn-erp): add AI Intelligence module — PRD section + SRS Module 15 (FR-AI-001-005); build PRD and SRS docx"
git push
```

---

---

## PROJECT 4: Maduuka (POS + Bookkeeping SaaS for African SMBs)

PRD is a single `01-prd.md` file. SRS has `04-functional-requirements.md`. All Phase 1–9 docs complete with docx built. Two docx to rebuild after upgrade: PRD and SRS.

**AI features to add (4):** SMB pricing must be accessible — a shop owner in Kampala CBD is the buyer.

1. Sales Forecasting — predict tomorrow's and next week's revenue
2. Smart Reorder Advisor — recommend stock purchase quantities
3. Fraud & Anomaly Alerts — flag suspicious voids, refunds, unusual transaction patterns
4. Business Health Advisor — weekly plain-English business health report

**Pricing tiers:** Starter — UGX 30,000/month; Growth — UGX 80,000/month; Enterprise — UGX 200,000/month.

**Files in scope:**
- Modify: `projects/Maduuka/_context/features.md`
- Modify: `projects/Maduuka/01-strategic-vision/01-prd/01-prd.md`
- Modify: `projects/Maduuka/02-requirements-engineering/01-srs/04-functional-requirements.md`
- Build: `projects/Maduuka/01-strategic-vision/01-prd/` → rebuild `Maduuka_PRD.docx`
- Build: `projects/Maduuka/02-requirements-engineering/01-srs/` → rebuild `Maduuka_SRS.docx`
- Modify: `projects/Maduuka/DOCUMENTATION-STATUS.md`

---

### Task 4.1: Update Maduuka features context

**File:** `projects/Maduuka/_context/features.md`

Append an "AI Business Intelligence Module" section at the end of the file:

```markdown
## AI Business Intelligence Module (Add-On)

**Tier:** Starter and above | **Phase:** Future add-on (off by default)

- Sales forecasting: predict today's and next 7 days' revenue based on historical patterns and day-of-week seasonality
- Smart Reorder Advisor: recommend exact purchase quantities per product to avoid over-stocking and stockouts
- Fraud and anomaly alerts: flag suspicious void patterns, after-hours transactions, and unusual refund activity to the Business Owner
- Business Health Advisor: weekly plain-English "How Is Your Business?" report — revenue trend, top seller, expense warning, one recommended action
```

---

### Task 4.2: Add FR-AI business section to Maduuka PRD

**File:** `projects/Maduuka/01-strategic-vision/01-prd/01-prd.md`

Read the file. Locate the `## 8. Success Metrics` section (near the end). Insert the FR-AI block immediately **before** that heading, preceded by a blank line.

Write the following 4 features for a Ugandan SMB owner audience (informal, direct language):

**Feature 1 — Know What Revenue to Expect Tomorrow**
- Who benefits: Business Owners, Branch Managers
- Problem: A shop owner does not know whether to staff 2 or 4 cashiers on Saturday. They go by gut feeling. Sometimes they are understaffed on a busy day and lose sales. Sometimes they overstaff on a slow day and pay idle staff. Both cost money.
- What it does: Every morning, the system looks at the last 90 days of sales history for that day of the week, applies a simple trend adjustment, and shows the owner a "Sales Range for Today: UGX 180K–240K (based on the last 12 Mondays)." If a public holiday or local market day is approaching, the system adjusts. The owner can plan staffing, float, and product restocking in the morning rather than reacting all day.
- Why owners pay: Better staffing decisions alone — even one fewer idle cashier shift per week — pays for the AI module in full.
- Pricing tier: Starter and above.
- FR-AI-001 reference

**Feature 2 — A List of Exactly What to Buy This Week**
- Who benefits: Business Owners, Inventory Managers
- Problem: A shop owner walks through the stock room every Sunday and tries to guess what to reorder. They forget fast movers and order slow movers they already have too much of. They over-spend on stock every month.
- What it does: Every Sunday morning, the system analyses how fast each product has been selling over the last 30 days. It produces a "Buy This Week" list showing: Product, Current Stock (days remaining), Recommended Order Quantity. The owner forwards this list to their supplier via WhatsApp directly from the app. One tap, done.
- Why owners pay: A shop that never runs out of its top 10 sellers and does not over-order the slow ones makes more money on the same capital. Most Maduuka clients are running lean — smarter buying is their biggest lever.
- Pricing tier: Starter and above.
- FR-AI-002 reference

**Feature 3 — Get Alerted When Something Suspicious Happens in Your Business**
- Who benefits: Business Owners (especially for multi-branch or owner-absent operations)
- Problem: A business owner with 3 branches cannot be present at all of them. Staff know this. Unusual patterns in voids, refunds, and after-hours transactions often indicate cash theft or collusion that would not be caught until the monthly stock count.
- What it does: Every morning, the system compares the previous day's transactions against the baseline for that cashier, branch, and day of week. If voids were 3× higher than normal, if a refund was processed without a corresponding recent sale, or if a transaction was posted after closing time, the Business Owner receives a notification: "3 unusual events at Nakivubo Branch yesterday — tap to review." The owner reviews the flagged transactions and acts.
- Why owners pay: Catching one day of cash theft per month pays for the entire year's AI subscription. The alert alone changes staff behaviour — they know the system is watching.
- Pricing tier: Growth and above.
- FR-AI-003 reference

**Feature 4 — Your Business Report Card, Every Monday Morning**
- Who benefits: Business Owners
- Problem: A shop owner is too busy running the business to review dashboards. By the time they sit down to check the numbers at month-end, it is too late to act on anything.
- What it does: Every Monday morning at 8am, the Business Owner receives one notification — their Business Health Report for last week: "Revenue: UGX 1.2M (↑8% vs last week). Top seller: Kimbo 2kg. Watch out: Roofings Nails slow — you have 40 days of stock. Action: stock up on Sembe before Friday price increase." No login needed — it arrives as a push notification. The full report is one tap away.
- Why owners pay: It is the weekly business briefing that every owner wants but never has time to prepare themselves. Owners who get this report act on it. Owners who act on it make more money. That is the retention mechanism.
- Pricing tier: Growth and above.
- FR-AI-004 reference

**Packaging table:**

| Feature | Starter (UGX 30K/mo) | Growth (UGX 80K/mo) | Enterprise (UGX 200K/mo) |
|---|---|---|---|
| Sales Forecasting | Yes | Yes | Yes |
| Smart Reorder Advisor | Yes | Yes | Yes |
| Fraud & Anomaly Alerts | — | Yes | Yes |
| Business Health Advisor | — | Yes | Yes |

---

### Task 4.3: Add FR-AI technical FRs to Maduuka SRS

**File:** `projects/Maduuka/02-requirements-engineering/01-srs/04-functional-requirements.md`

Read the end of this file to find the last existing FR section, then append a new `## FR-AI: AI Business Intelligence Module` section.

Write 4 technical FRs following the Maduuka SRS FR pattern (bold `**FR-AI-XXX:**` on its own bold line, followed by the stimulus-response text):

**FR-AI-001 (Sales Forecasting):**
When the daily forecast job runs at 06:00 EAT for a tenant with at least 30 days of sales history, the system shall: retrieve the sales totals for every calendar day in the preceding 90-day window, group records by day-of-week, compute the per-day-of-week mean and standard deviation, apply a 4-week exponential moving average trend factor (α = 0.3), and write a forecast record for today's date to `ai_sales_forecast` with tenant ID, forecast date, day-of-week, lower bound (mean − 1 standard deviation), base estimate (mean × trend factor), and upper bound (mean + 1 standard deviation). The system shall display the base estimate and range on the Dashboard module's KPI row as "Expected Today: UGX [lower]–[upper]" alongside the real-time live revenue figure. For tenants with fewer than 30 days of history, the system shall display "Insufficient history for forecast" instead of a range. The forecast job shall complete for all active tenants within 10 minutes of the 06:00 EAT trigger.

**FR-AI-002 (Smart Reorder Advisor):**
When the Sunday reorder advisory job runs at 07:00 EAT for a tenant with at least 30 days of stock movement history, the system shall: for each active product with at least one sale in the preceding 30 days, compute the 30-day weighted average daily sales quantity (more recent days weighted higher: weight = day_index / sum_of_indices), project days of stock remaining as `current_stock ÷ weighted_avg_daily_sales` (or infinity if the product has zero recorded sales in 30 days), compute recommended order quantity as `(30 × weighted_avg_daily_sales) − current_stock` (floored at zero), and write the recommendation to `ai_reorder_recommendations` with tenant ID, product ID, current stock, weighted daily sales, days remaining, and recommended order quantity. Products with projected days of stock ≤ 14 shall appear in the Inventory module's "Buy This Week" panel, sorted by days remaining ascending. The Business Owner shall be able to share the "Buy This Week" list via WhatsApp using the native Android share sheet with a single tap. The job shall complete within 5 minutes of the Sunday 07:00 EAT trigger for tenants with up to 2,000 active products.

**FR-AI-003 (Fraud & Anomaly Alerts):**
When the nightly anomaly scan runs at 23:30 EAT after each business day, the system shall evaluate the preceding day's transactions against the following four anomaly detectors, each producing a boolean flag:
(a) Void Ratio Anomaly — the day's void count for a given cashier exceeds 3× that cashier's 30-day average void rate;
(b) Refund Without Sale — a refund transaction references a receipt number that has no corresponding sale within the preceding 7 days for the same product and customer;
(c) After-Hours Transaction — a sale or refund transaction is recorded outside the tenant's configured operating hours by more than 30 minutes;
(d) Round-Number Sale — 3 or more cash sales in a single session are exact round numbers (divisible by 10,000 UGX) with no change recorded.
For each transaction triggering 2 or more anomaly flags, the system shall write an anomaly record to `ai_anomaly_flags` with transaction ID, cashier ID, branch ID, triggered flag codes, detection timestamp, and review status (default: Unreviewed). The Business Owner role shall receive a push notification: "X suspicious event(s) at [Branch] yesterday — tap to review." The Anomaly Inbox shall allow the Business Owner to mark events as Reviewed — No Issue or Escalated. The nightly scan shall complete within 5 minutes for tenants with up to 10,000 daily transactions.

**FR-AI-004 (Business Health Advisor):**
When the Monday 08:00 EAT report generation job runs for a tenant with at least 14 days of sales history, the system shall:
(1) Compute last week's total revenue, compare to the preceding week and to the same week 4 weeks prior, and express the comparison as a percentage change with a directional indicator (↑/↓/→);
(2) Identify the top 3 selling products by revenue for last week;
(3) Identify any product with current stock ≥ 30 days of projected demand and flag as "Over-stocked — watch";
(4) Identify any product with projected days of stock ≤ 7 and flag as "Reorder urgent";
(5) Identify the cashier or branch with the highest revenue and the one with the lowest;
(6) Compose a 4-sentence plain-English Business Health summary from these inputs (using the configured LLM provider — Claude API) in the form: one sentence on revenue trend, one on top seller, one on inventory watch item, one recommended action.
The system shall deliver the summary as a push notification to all users holding the Business Owner role at 08:00 EAT Monday. The full report (all 5 data points plus the 4-sentence summary) shall be accessible from the Notifications panel. The generation job shall complete within 60 seconds of trigger. For tenants with fewer than 14 days of history, the system shall skip report generation and log a "Insufficient history" record without sending a notification.

---

### Task 4.4: Build Maduuka PRD docx (rebuild)

```bash
cd C:/wamp64/www/srs-skills && bash scripts/build-doc.sh projects/Maduuka/01-strategic-vision/01-prd Maduuka_PRD
```

Expected output: `projects/Maduuka/01-strategic-vision/Maduuka_PRD.docx` (replaces existing)

---

### Task 4.5: Build Maduuka SRS docx (rebuild)

```bash
cd C:/wamp64/www/srs-skills && bash scripts/build-doc.sh projects/Maduuka/02-requirements-engineering/01-srs Maduuka_SRS_Phase1
```

Expected output: `projects/Maduuka/02-requirements-engineering/Maduuka_SRS_Phase1.docx`

---

### Task 4.6: Update Maduuka DOCUMENTATION-STATUS.md

1. Update Phase 01 PRD row: rebuilt status confirmed.
2. Update Phase 02 SRS row: rebuilt status confirmed.
3. Add AI Business Intelligence module to the Planned but Not Yet Started section if Phase 2 SRS will include dedicated AI FRs, or mark it as added to Phase 1 SRS.
4. Update Last Updated date to 2026-04-07.

---

### Task 4.7: Commit and push Maduuka AI upgrade

```bash
cd C:/wamp64/www/srs-skills
git add projects/Maduuka/
git commit -m "feat(maduuka): add AI Business Intelligence module — PRD FR-AI section + SRS FR-AI-001-004; rebuild PRD and SRS docx"
git push
```

---

---

## PROJECT 5: BIRDC-ERP (Banana Factory ERP — Bespoke Consulting Project)

**Structure note:** BIRDC-ERP is a bespoke client project, not a SaaS product. AI features are scoped as a Phase 7 contract extension, not a subscription add-on. Pricing is project-based (lump-sum milestone), not monthly. The PRD has a different structure (no feature-requirements section) — add a new `11-ai-module.md` file. The SRS is split by phase — add AI FRs to Phase 6 (Research, Administration & IT) as a new `08-fr-ai.md` file, since Phase 6 explicitly covers IT/innovation.

**AI features to add (5):**
1. Production Yield Predictor — forecast expected output from raw material quality grades
2. Quality Defect Pattern Detection — detect recurring quality failures early
3. Farmer Supply Forecasting — predict seasonal farmer delivery volumes
4. Predictive Equipment Maintenance — flag equipment before it fails
5. Export Demand Intelligence — optimize production scheduling for export orders

**Pricing model:** Phase 7 project milestone. Quote separately per scope.

**Files in scope:**
- Modify: `projects/BIRDC-ERP/_context/features.md`
- Create: `projects/BIRDC-ERP/01-strategic-vision/01-prd/11-ai-module.md`
- Modify: `projects/BIRDC-ERP/01-strategic-vision/01-prd/manifest.md` (if exists, else check)
- Create: `projects/BIRDC-ERP/02-requirements-engineering/06-srs-phase6-research-admin/08-fr-ai.md`
- Build: `projects/BIRDC-ERP/01-strategic-vision/01-prd/` → rebuild `PRD_BIRDC_ERP.docx`
- Build: `projects/BIRDC-ERP/02-requirements-engineering/06-srs-phase6-research-admin/` → rebuild `SRS_BIRDC_ERP_Phase6_ResearchAdmin.docx`
- Modify: `projects/BIRDC-ERP/DOCUMENTATION-STATUS.md`

---

### Task 5.1: Update BIRDC-ERP features context

**File:** `projects/BIRDC-ERP/_context/features.md`

Append an "F-018: AI Intelligence Module (Phase 7)" section at the end of the file, following the existing F-0XX numbering:

```markdown
---

## Phase 7 — AI Intelligence (Contract Extension)

### F-018: AI Intelligence Module
Phase 7 contract extension. Requires Phase 1–4 fully operational with at least 12 months of production data.

- Production yield prediction: forecast output tonnage per production order based on raw material quality grades and recipe inputs, before production begins
- Quality defect pattern detection: identify recurring quality failure patterns across batches before they escalate to export rejection
- Farmer supply forecasting: predict expected delivery volumes per cooperative per season based on 3-year historical patterns and satellite crop assessment
- Predictive equipment maintenance: analyse equipment runtime hours, vibration/temperature sensor data, and service history to predict maintenance windows 14–21 days in advance
- Export demand intelligence: model export order scheduling against production capacity and farmer supply forecast to identify production plan conflicts 8 weeks in advance
```

---

### Task 5.2: Create BIRDC-ERP PRD AI section

**File:** `projects/BIRDC-ERP/01-strategic-vision/01-prd/11-ai-module.md`

Create this new file. The BIRDC-ERP PRD uses a different style from the SaaS projects — it is a consulting proposal document. Write this section in consulting proposal language (not SaaS subscription language).

Write the section `# Phase 7 — AI Intelligence Module` as a project scope extension:

**Opening:** Describe AI as a Phase 7 contract extension that builds on the operational data generated by Phases 1–6. BIRDC will have 12+ months of production records, quality lab results, farmer delivery history, and equipment service logs by the time Phase 6 is live. This data is the foundation. Phase 7 converts it into predictive intelligence.

Write 5 business-case-style feature descriptions (Capability → Business Problem It Solves → How BIRDC Benefits → Contract Trigger):

**Capability 1 — Know Before You Cook: Production Yield Prediction**
- Business problem: BIRDC's production team commits to an output tonnage for a production order based on the recipe and nominal input quality. When actual raw material quality differs from nominal (as it frequently does with agricultural inputs), actual yield deviates. The deviation is discovered at completion — too late to adjust.
- How BIRDC benefits: The system reads the quality grades (A, B, C) recorded during goods receipt for the specific batches allocated to a production order and predicts actual yield before the order begins. The production manager can decide to adjust the batch mix, source additional raw material, or revise the committed output quantity — before the cook, not after.
- Contract trigger: Activate when Phase 4 (Production & Quality) has 6 months of completed production order data.
- FR-AI-001 reference

**Capability 2 — Catch Recurring Quality Failures Before They Reach the Export Market**
- Business problem: A quality defect pattern (e.g., moisture content out of spec in weekly batches) may appear across 5 consecutive production orders before a lab analyst notices the trend. Each failed export shipment costs BIRDC in rejected goods, logistics expense, and customer relationship damage.
- How BIRDC benefits: After each production batch is quality-graded, the system compares the result against the statistical baseline for that product and parameter. If any parameter has trended outside its control limits for 3 consecutive batches, the system generates a Process Alert for the Quality Manager and Production Director: "Moisture content (Parameter P-003) has exceeded the upper control limit in 3 consecutive batches of Processed Tooke Flour. Review equipment and drying process."
- Contract trigger: Activate with Phase 4 data. 3 months of QC records required for baseline.
- FR-AI-002 reference

**Capability 3 — Plan Raw Material Supply 3 Months Out**
- Business problem: BIRDC's production plan depends on a steady supply of bananas from cooperative farmers. Seasonal variation, weather events, and political factors cause supply shocks that leave the factory under-utilised or unable to fulfil export orders.
- How BIRDC benefits: Based on 3 years of cooperative delivery records, historical seasonal patterns, and (optionally) Open-Meteo rainfall forecasts for the Bushenyi region, the system generates a quarterly Farmer Supply Forecast per cooperative: expected delivery volume, confidence interval, and recommended factory production schedule. Procurement can issue advance purchase orders to cooperatives based on the forecast, incentivising supply stability.
- Contract trigger: Activate when Phase 3 (Supply Chain & Farmers) has 12 months of delivery records.
- FR-AI-003 reference

**Capability 4 — Predict Equipment Maintenance Windows — Not Emergency Repairs**
- Business problem: Factory equipment fails at the worst times: during a production run committed to an export shipment deadline. Emergency repairs are 3–5× more expensive than scheduled maintenance. Downtime during a committed production run is even more costly.
- How BIRDC benefits: The system tracks equipment runtime hours per production order, maintenance service records, and (where sensors are installed) vibration or temperature readings. When a machine's predictive maintenance model indicates it is within 21 days of a likely failure event based on accumulated runtime and service history, the Maintenance Manager receives an alert: "Milling machine M-003 is approaching maintenance threshold. Recommended service window: 18–22 April." The maintenance is scheduled in advance around production commitments.
- Contract trigger: Activate when Phase 4 has 6 months of equipment service log data.
- FR-AI-004 reference

**Capability 5 — Optimise Production Scheduling Against Export Demand**
- Business problem: Export orders arrive with committed delivery dates. BIRDC must backward-plan from the shipment date through production, QC, packaging, and logistics. When multiple export orders overlap in a constrained production calendar, conflicts go undetected until it is too late to source additional capacity or renegotiate dates.
- How BIRDC benefits: When a new export order is entered, the system runs a Production Feasibility Check: it models the required production tonnage against available factory capacity (from the production schedule), available raw material supply (from the Farmer Supply Forecast), and committed QC throughput. If a conflict is detected, it flags it immediately: "Export Order EO-2026-047 (14 MT of Tooke Flour, due 15 June) conflicts with existing orders for the week of 8 June. Available capacity: 10 MT. Gap: 4 MT. Options: advance production by 1 week, request supplementary cooperative delivery, or negotiate shipment date."
- Contract trigger: Activate when FR-AI-003 and production schedule module are both operational.
- FR-AI-005 reference

**Phase 7 Scope and Pricing section:** State that Phase 7 is quoted as a separate lump-sum contract extension upon request. Indicative scope: 3-month development and testing period. Cost estimate to be provided in a separate Addendum to the original contract.

---

### Task 5.3: Check and update BIRDC-ERP PRD manifest.md

**File:** `projects/BIRDC-ERP/01-strategic-vision/01-prd/manifest.md` (check if it exists first)

If it exists: append `11-ai-module.md` to the file list.
If no manifest exists: the build script uses alphabetical sort of `*.md` files — `11-ai-module.md` will sort after `10-assumptions.md`, which is correct.

---

### Task 5.4: Create BIRDC-ERP SRS AI FRs file

**File:** `projects/BIRDC-ERP/02-requirements-engineering/06-srs-phase6-research-admin/08-fr-ai.md`

Read `07-nfr-and-constraints.md` in the same directory to match formatting exactly.

Write the section `## 3.4 F-018: AI Intelligence Module (Phase 7)` with a preamble note: "The following FRs are scoped for Phase 7 and shall not block the Phase 6 acceptance milestone. They are included in this SRS document to establish traceability and technical requirements for the contract extension scope."

Write 5 technical FRs following the BIRDC-ERP SRS FR format (bold FR-AI-XXX on its own line, stimulus-response text on the next):

**FR-AI-001 (Production Yield Prediction):**
When a production order is moved to `in_progress` status and at least one raw material batch with a recorded quality grade (A, B, or C) has been allocated to the order, the system shall: retrieve the quality grade distribution of the allocated batches (percentage of A, B, and C grade material by weight), apply the configured yield coefficient matrix (Grade A nominal yield × 1.0, Grade B × 0.93, Grade C × 0.85 — coefficients configurable by the Production Director without developer involvement), compute the predicted output tonnage as `sum(allocated_weight_per_grade × recipe_yield × grade_coefficient)`, write the prediction to `ai_yield_predictions` with production order ID, allocated batch IDs, grade distribution percentages, predicted output, configured coefficients, and prediction timestamp, and display the predicted output on the production order screen alongside the recipe's nominal output. If predicted output differs from committed output by more than 5%, the system shall display a Yield Alert: "Predicted yield is [X]% below committed output. Review batch mix before proceeding." The system shall not block the production order from proceeding — it shall alert only. Prediction computation shall complete within 2,000 ms of the status change event.

**FR-AI-002 (Quality Defect Pattern Detection):**
When a quality inspection result is saved for a completed production batch and at least 3 prior inspection records exist for the same product and the same quality parameter within the preceding 90 days, the system shall: retrieve the last 5 inspection results for that product-parameter combination in chronological order, apply a Shewhart control chart rule (Western Electric Rule 1: any single point beyond 3 standard deviations; Rule 2: 3 consecutive points beyond 2 standard deviations in the same direction), and — if either rule is triggered — create an `ai_process_alert` record with product ID, parameter code, rule triggered, last 5 measurement values, mean, standard deviation, alert timestamp, and review status (Unreviewed). The system shall dispatch an in-app alert to all users holding the Quality Manager or Production Director role within 5 minutes of alert creation. The alert shall state: "Quality parameter [parameter name] on [product name] has triggered Control Chart Rule [rule number] across the last [N] batches. Review recommended." The Quality Manager shall be able to mark the alert Reviewed — Root Cause Identified (with mandatory root cause text field) or Reviewed — No Action Required.

**FR-AI-003 (Farmer Supply Forecasting):**
When the quarterly supply forecast job runs on the 1st calendar day of each quarter (January, April, July, October) and the system contains at least 12 months of cooperative delivery history, the system shall: for each active cooperative in the system, retrieve all delivery records for the corresponding quarter in each prior year of available history (e.g., for Q2 2027, retrieve Q2 2026 and Q2 2025 if available), compute the mean and standard deviation of total quarterly delivery tonnage per cooperative, apply an optional rainfall adjustment factor if Open-Meteo historical rainfall data for the Bushenyi GPS zone deviates more than 20% from the prior year's same-quarter rainfall (adjustment factor configurable by the Procurement Manager), and write a forecast record to `ai_supply_forecast` with cooperative ID, quarter, forecast tonnage, confidence interval (mean ± 1 standard deviation), rainfall adjustment applied (boolean), and forecast timestamp. The system shall display the quarterly supply forecast table in the Procurement module (F-009), accessible to the Procurement Manager and above. The forecast job shall complete within 10 minutes of the quarterly trigger for up to 200 active cooperatives.

**FR-AI-004 (Predictive Equipment Maintenance):**
When the weekly maintenance prediction scan runs every Monday at 06:00 EAT and the system contains at least 6 months of equipment service log data for an asset, the system shall: for each active production asset registered in the Asset Management module with at least 3 completed service records, compute the average interval between services (in production hours or calendar days, whichever unit is recorded), compute the production hours or days elapsed since the most recent completed service, compute the Maintenance Proximity Score as `(hours_since_service ÷ average_service_interval) × 100`, and — if the score exceeds 80% — write a prediction record to `ai_maintenance_predictions` with asset ID, score, last service date, average interval, predicted next service date (last service + average interval), and prediction timestamp, and create an in-app alert for the Maintenance Manager role: "Asset [name] (Asset ID: [ID]) is at [score]% of its average maintenance interval. Recommended service window: [date range]." The system shall not automatically schedule a maintenance work order — it shall alert only. The weekly scan shall complete within 15 minutes for up to 100 tracked assets.

**FR-AI-005 (Export Demand Intelligence):**
When a user with the Sales Manager or Export Manager role saves a new export order with a committed shipment date, the system shall perform a Production Feasibility Check within 5,000 ms: retrieve all confirmed production orders and their committed completion dates for the 8-week window preceding the export order's shipment date, sum the committed production tonnage already scheduled in that window, compute available capacity as `(daily_production_capacity × working_days_in_window) − committed_tonnage`, compare available capacity to the export order's required production tonnage, and — if available capacity is less than required — create a `ai_export_conflict` record with export order ID, required tonnage, available capacity, capacity gap, and conflict timestamp, and display a non-blocking Conflict Alert on the order save screen: "Production capacity conflict detected: [gap] MT of capacity required for this order is not available in the production schedule for the weeks of [dates]. Options: advance production start, request supplementary cooperative delivery, or negotiate shipment date." The Sales Manager shall be able to proceed with saving the order despite the alert; the conflict record shall persist and remain visible in a Conflicts dashboard accessible to the Export Manager and Production Director.

---

### Task 5.5: Build BIRDC-ERP PRD docx (rebuild)

```bash
cd C:/wamp64/www/srs-skills && bash scripts/build-doc.sh projects/BIRDC-ERP/01-strategic-vision/01-prd PRD_BIRDC_ERP
```

Expected output: `projects/BIRDC-ERP/01-strategic-vision/PRD_BIRDC_ERP.docx` (replaces existing)

---

### Task 5.6: Build BIRDC-ERP Phase 6 SRS docx (rebuild)

```bash
cd C:/wamp64/www/srs-skills && bash scripts/build-doc.sh "projects/BIRDC-ERP/02-requirements-engineering/06-srs-phase6-research-admin" SRS_BIRDC_ERP_Phase6_ResearchAdmin
```

Expected output: `projects/BIRDC-ERP/02-requirements-engineering/SRS_BIRDC_ERP_Phase6_ResearchAdmin.docx` (replaces existing)

---

### Task 5.7: Update BIRDC-ERP DOCUMENTATION-STATUS.md

1. Add Phase 7 AI Intelligence section to the document inventory table.
2. Update the Requirements Summary table: add Phase 7 row with "AI Intelligence" and 5 FRs.
3. Update PRD row: `.docx` rebuilt.
4. Update Phase 6 SRS row: `.docx` rebuilt (now includes Phase 7 AI FRs).
5. Update Total Documents count.
6. Update Last Updated date to 2026-04-07.

---

### Task 5.8: Commit and push BIRDC-ERP AI upgrade

```bash
cd C:/wamp64/www/srs-skills
git add projects/BIRDC-ERP/
git commit -m "feat(birdc-erp): add AI Intelligence Phase 7 — PRD scope section + Phase 6 SRS FR-AI-001-005; rebuild PRD and Phase 6 SRS docx"
git push
```

---

---

## Final Verification

After all 5 projects are complete:

1. Confirm all docx files exist at their expected paths.
2. Confirm git log shows 5 separate commits (one per project).
3. Update the memory file `C:\Users\Peter\.claude\projects\C--wamp64-www-srs-skills\memory\project_ai_skill_suite.md` to note that all 5 projects now have AI modules in their PRD and SRS.
4. Optionally run `bash export-docs.sh` in each project directory to refresh the export folder.

# UX Specification — Medic8

**Document ID:** DD-05-01
**Project:** Medic8
**Version:** 1.0.0
**Date:** 2026-04-03
**Status:** Draft — Pending Consultant Review

---

## 1. Design System

### 1.1 Framework

The Medic8 design system spans four platform targets. All platforms share a unified set of design tokens (colour, spacing, typography scale) to ensure visual consistency across the ecosystem.

| Platform | Framework | Component Library |
|---|---|---|
| Web (Staff) | Bootstrap 5 | Tabler UI admin template (commercial) |
| Web (Patient Portal) | Bootstrap 5 | Tabler UI (responsive subset) |
| Android (Patient App) | Jetpack Compose | Material 3 with custom Medic8 theme |
| Android (CHW App) | Jetpack Compose | Material 3 (simplified, data-lite) |
| iOS (Patient App) | SwiftUI | Native iOS patterns with SF Symbols |

All staff-facing screens are server-rendered HTML pages using Tabler components. No custom CSS framework is created. Custom components specific to healthcare (triage badges, CDS alert modals, vital signs charts) are built as Tabler extensions using CSS custom properties and vanilla JavaScript.

The Android and iOS patient apps consume the same RESTful JSON API as the web portal. Design tokens are exported as platform-native theme files: CSS custom properties (web), Kotlin `Color` objects (Android), and Swift `Color` asset catalogues (iOS).

### 1.2 Colour Palette

#### 1.2.1 Base Semantic Tokens

| Token | Hex | Usage |
|---|---|---|
| `--primary` | `#206bc4` | Primary actions, navigation highlights, header backgrounds |
| `--primary-dark` | `#1a56a0` | Hover and pressed states for primary elements |
| `--secondary` | `#656d77` | Secondary text, muted icons, inactive states |
| `--success` | `#2fb344` | Successful actions, confirmed status, normal vitals |
| `--warning` | `#f76707` | Warnings, near-expiry stock, CDS Warning tier alerts |
| `--danger` | `#d63939` | Errors, critical alerts, CDS Serious/Fatal tier, abnormal results |
| `--info` | `#4299e1` | Informational badges, CDS Info tier, tooltips |
| `--bg-surface` | `#f4f6fa` | Page background |
| `--bg-card` | `#ffffff` | Card, modal, and panel backgrounds |
| `--text-primary` | `#1e293b` | Headings, primary body text |
| `--text-secondary` | `#64748b` | Captions, helper text, timestamps |
| `--border` | `#e2e8f0` | Card borders, dividers, table row separators |

#### 1.2.2 Clinical Triage Tokens

| Token | Hex | Usage | Text Label |
|---|---|---|---|
| `--triage-emergency` | `#d63939` | Emergency triage level (Level 1) | "EMERGENCY" |
| `--triage-urgent` | `#f76707` | Urgent triage level (Level 2) | "URGENT" |
| `--triage-semi-urgent` | `#f59f00` | Semi-urgent triage level (Level 3) | "SEMI-URGENT" |
| `--triage-non-urgent` | `#2fb344` | Non-urgent triage level (Level 4) | "NON-URGENT" |

Triage colours are always paired with a text label. Colour alone never conveys triage level (WCAG 1.4.1 Use of Color).

#### 1.2.3 Laboratory and Vital Signs Tokens

| Token | Hex | Usage | Animation |
|---|---|---|---|
| `--critical-value` | `#d63939` | Critical lab values requiring acknowledgement | Pulsing opacity animation (1s cycle) |
| `--normal-range` | `#2fb344` | Values within the normal reference range | None |
| `--abnormal` | `#f76707` | Values outside normal range (H/L flag) | None |

#### 1.2.4 CDS Alert Tier Tokens

| Token | Hex | Tier | Background |
|---|---|---|---|
| `--cds-info` | `#4299e1` | Tier 1 — Info | `#edf5ff` |
| `--cds-warning` | `#f76707` | Tier 2 — Warning | `#fff4e6` |
| `--cds-serious` | `#d63939` | Tier 3 — Serious | `#ffe3e3` |
| `--cds-fatal` | `#d63939` | Tier 4 — Fatal | `#d63939` (white text) |

#### 1.2.5 Bed Management Tokens

| Token | Hex | Usage |
|---|---|---|
| `--bed-available` | `#2fb344` | Bed available for admission |
| `--bed-occupied` | `#206bc4` | Bed occupied (patient name displayed) |
| `--bed-reserved` | `#f59f00` | Bed reserved for incoming transfer |
| `--bed-maintenance` | `#adb5bd` | Bed out of service |

#### 1.2.6 NEWS2 Score Tokens

| Token | Hex | Score Range |
|---|---|---|
| `--news2-low` | `#2fb344` | 0-4 (low clinical risk) |
| `--news2-medium` | `#f76707` | 5-6 (medium clinical risk) |
| `--news2-high` | `#d63939` | 7+ (high clinical risk) |

All colour combinations meet **WCAG 2.1 AA** contrast ratio of 4.5:1 for normal text and 3:1 for large text. Patient-facing interfaces target **WCAG 2.1 AAA** (7:1 for normal text).

### 1.3 Typography

#### 1.3.1 Font Families by Platform

| Platform | Primary Font | Monospace Font | Fallback |
|---|---|---|---|
| Web (all portals) | Inter | JetBrains Mono | system-ui, -apple-system, sans-serif |
| Android | Roboto | Roboto Mono | sans-serif |
| iOS | SF Pro | SF Mono | system default |

#### 1.3.2 Type Scale (Web — 14px Base)

| Element | Font | Size | Weight | Line Height | Usage |
|---|---|---|---|---|---|
| Page title (h1) | Inter | 24px / 1.5rem | 600 | 1.3 | Page headers |
| Section heading (h2) | Inter | 20px / 1.25rem | 600 | 1.3 | Card group headings |
| Card title (h3) | Inter | 16px / 1rem | 600 | 1.4 | Card headers, modal titles |
| Body text | Inter | 14px / 0.875rem | 400 | 1.5 | All body content |
| Small / caption | Inter | 12px / 0.75rem | 400 | 1.5 | Timestamps, helper text |
| Clinical data | JetBrains Mono | 13px | 400 | 1.4 | Lab values, vital signs, MRN, doses |
| Badge / tag | Inter | 11px / 0.6875rem | 600 | 1.2 | Status badges, triage labels |

#### 1.3.3 Tall Man Lettering for Look-Alike/Sound-Alike (LASA) Drugs

LASA drugs are displayed with bold uppercase differentiating letters to prevent medication errors. This rendering applies in every context where a drug name appears: prescription dropdowns, pharmacy queue, dispensing screen, drug formulary, and medication administration records.

| Drug Pair | Rendered As |
|---|---|
| hydroxyzine / hydralazine | hydr**OXY**zine / hydr**ALA**ZINE |
| prednisolone / prednisone | prednis**OL**one / prednis**ONE** |
| chlorpromazine / chlorpropamide | chlorpro**MAZ**ine / chlorpro**PAM**ide |
| glipizide / glyburide | gli**PIZ**ide / gly**BUR**ide |

Implementation: the drug formulary table stores a `tall_man_display` column containing the HTML-marked-up name. The frontend renders this field using `innerHTML` with sanitisation. The bold uppercase segment uses `<b>` tags and CSS `text-transform: uppercase` on the marked segment only.

### 1.4 Spacing Scale

Based on a 4px base unit: `4, 8, 12, 16, 24, 32, 48, 64`.

| Token | Value | Usage |
|---|---|---|
| `--space-xs` | 4px | Icon-to-text gap, inline badge padding |
| `--space-sm` | 8px | Between related form fields, list item padding |
| `--space-md` | 16px | Card padding, form field vertical gap |
| `--space-lg` | 24px | Section separation within a page |
| `--space-xl` | 32px | Page section margins, card group gaps |
| `--space-2xl` | 48px | Major page divisions |

### 1.5 Iconography

| Platform | Icon Set | Custom Icons |
|---|---|---|
| Web | Tabler Icons (3,500+ icons, SVG) | Triage level indicators, CDS alert tier badges, NEWS2 score badge |
| Android | Material Icons (filled + outlined) | Triage level indicators, CDS alert tier badges |
| iOS | SF Symbols (5,000+ symbols) | Triage level indicators mapped to SF Symbol equivalents |

Custom icon specifications:

| Icon | Shape | Size | Usage |
|---|---|---|---|
| Triage Emergency | Circle with exclamation | 24x24px | Triage queue, patient banner |
| Triage Urgent | Triangle with exclamation | 24x24px | Triage queue, patient banner |
| Triage Semi-Urgent | Diamond outline | 24x24px | Triage queue, patient banner |
| Triage Non-Urgent | Circle outline | 24x24px | Triage queue, patient banner |
| CDS Info | "i" in circle | 16x16px | Inline beside drug field |
| CDS Warning | Triangle warning | 20x20px | Banner header icon |
| CDS Serious | Shield with "!" | 24x24px | Modal header icon |
| CDS Fatal | Skull / stop hand | 32x32px | Modal header icon |

### 1.6 Component Library — Healthcare-Specific Widgets

All components extend standard Tabler widgets. These custom components are specific to Medic8:

| Component | Description |
|---|---|
| `PatientBanner` | Sticky header: photo, name, MRN, age, sex, blood group, allergy flags, insurance status. Visible on every clinical screen |
| `TriageBadge` | Colour-coded pill with icon + text label for triage level |
| `VitalSignsRow` | Horizontal row of vital sign values with sparkline trend and abnormal highlighting |
| `CDSAlertModal` | Tier-aware modal: configurable header colour, override reason input (Tier 3), no-override lock (Tier 4) |
| `LabResultCard` | Single result with value, reference range, H/L flag, trend sparkline, critical pulse indicator |
| `BedIcon` | Clickable bed representation with colour state, patient name tooltip, acuity dot |
| `DrugNameDisplay` | Renders drug name with Tall Man Lettering markup from `tall_man_display` field |
| `NEWS2ScoreBadge` | Numeric score in coloured circle (green/amber/red) |
| `OfflineBanner` | Persistent top banner: "Offline — changes will sync when connected" with queued count |
| `SyncProgressBar` | Animated progress bar showing "Syncing X changes..." on reconnection |
| `TaskResumptionPrompt` | Modal: "Resume where you left off?" with patient name, form name, and timestamp |
| `QueueCard` | Patient queue row: number, name, triage badge, wait time, assigned doctor |
| `SOAPNotesEditor` | Tabbed editor: Subjective, Objective, Assessment, Plan with auto-save |
| `PartographChart` | Graphical cervicogram with vitals, FHR, and contraction plotting |
| `PrescriptionRow` | Drug name (Tall Man), dose, frequency, duration, stock indicator, CDS icon |

---

## 2. Clinical UI Patterns

### 2.1 Single-Page OPD Clinical Summary

The OPD clinical summary is the most frequently used screen in the system. It is optimised for a minimum resolution of 1024x768 (the standard for clinical workstations in sub-Saharan Africa).

#### 2.1.1 Layout Structure

```
+-------------------------------------------------------------------+
| PATIENT BANNER (sticky)                                           |
| [Photo] Name | MRN: XXX | Age: XX | Sex: X | Allergies: [tags]  |
|         Blood Group: X+ | Insurance: [scheme] | Category: [type] |
+-------------------------------------------------------------------+
|                                                                   |
| +----------+ +----------------+ +-----------+ +----------------+ |
| | VITALS   | | ACTIVE         | | RECENT    | | CURRENT        | |
| | BP: xx/xx| | PROBLEMS       | | LABS      | | MEDICATIONS    | |
| | Temp: xx | | - Diabetes II  | | FBC: norm | | - Metformin    | |
| | PR: xx   | | - Hypertension | | RBS: H    | | - Amlodipine   | |
| | SpO2: xx | |                | | Cr: norm  | |                | |
| | NEWS2: X | |                | |           | |                | |
| +----------+ +----------------+ +-----------+ +----------------+ |
|                                                                   |
| +---------------------------------------------------------------+ |
| | [SOAP Notes] [Prescriptions] [Investigations] [Referral]      | |
| |---------------------------------------------------------------|  |
| | S: Patient reports...                                         | |
| | O: On examination...                                          | |
| | A: Assessment...                                              | |
| | P: Plan...                                                    | |
| |                                                               | |
| | [Save Draft]                              [Complete & Next]   | |
| +---------------------------------------------------------------+ |
|                                                                   |
| [Clinical History - Side Panel Toggle] >>>>                       |
+-------------------------------------------------------------------+
```

#### 2.1.2 Design Rules for the Clinical Summary

1. The `PatientBanner` is sticky (CSS `position: sticky; top: 0; z-index: 1020`) and remains visible during vertical scrolling.
2. The summary cards row (vitals, active problems, recent labs, current medications) is rendered as a 4-column grid (`display: grid; grid-template-columns: repeat(4, 1fr)`) above the fold on a 1024x768 viewport.
3. Allergy flags in the patient banner use `--danger` background with white text. If allergies exist, an audible alert tone plays on first load of the patient record (configurable per facility).
4. The active tab area (SOAP Notes, Prescriptions, Investigations, Referral) uses horizontal tabs below the summary row.
5. Clinical notes history is accessible via a slide-in side panel (right edge, 400px width) triggered by a toggle button. The side panel does not obscure the SOAP editor.
6. Auto-save fires on every form field blur event and every 10 seconds during active typing. The save status indicator displays "Saved" with a green tick or "Saving..." with a spinner.
7. The "Complete & Next" button advances to the next patient in the queue and marks the current encounter as complete.

### 2.2 Four-Tier CDS Alert Display

The Clinical Decision Support (CDS) alert system uses four tiers of escalating severity. Each tier has a distinct UI treatment calibrated to interrupt the clinician proportionally to the risk level.

#### Tier 1 — Info

| Attribute | Specification |
|---|---|
| Trigger | Informational drug interaction or clinical note |
| UI Element | 16px `CDS Info` icon beside the drug name field |
| Behaviour | Tooltip on hover (desktop) or tap (mobile) showing interaction detail |
| Blocking | No — does not block form submission |
| Logging | Logged as "CDS-INFO-DISPLAYED" in audit trail |

#### Tier 2 — Warning

| Attribute | Specification |
|---|---|
| Trigger | Moderate drug interaction or dosage concern |
| UI Element | Yellow banner (`--cds-warning` background) at the top of the prescription section |
| Content | Warning text: drug names, interaction type, clinical recommendation |
| Behaviour | Banner is dismissible with "Acknowledged" button |
| Blocking | No — does not block form submission |
| Logging | Logged as "CDS-WARNING-ACKNOWLEDGED" with clinician ID and timestamp |

#### Tier 3 — Serious

| Attribute | Specification |
|---|---|
| Trigger | Serious drug interaction with potential for patient harm |
| UI Element | Modal dialog with `--cds-serious` header background |
| Content | Drug names, interaction mechanism, clinical consequences, recommended alternatives |
| Required Input | Override reason text input (minimum 10 characters, free-text) |
| Buttons | "Override & Continue" (enabled only when reason entered) and "Cancel" |
| Blocking | Yes — modal blocks prescription submission until resolved |
| Logging | Logged as "CDS-SERIOUS-OVERRIDE" with reason text, clinician ID, timestamp |

#### Tier 4 — Fatal

| Attribute | Specification |
|---|---|
| Trigger | Contraindicated combination with high risk of death or permanent harm |
| UI Element | Modal dialog with `--cds-fatal` background (red header, white text) |
| Content | Drug names, contraindication details, "This combination is contraindicated and cannot be overridden" |
| Buttons | "Change Prescription" only — no override button exists |
| Additional Info | Pharmacist contact information displayed below the message |
| Blocking | Yes — prescription cannot be saved with this combination |
| Logging | Logged as "CDS-FATAL-BLOCKED" with clinician ID, timestamp, attempted drugs |

### 2.3 Task Resumption Support

Clinical environments average 6-7 interruptions per hour (Coiera, 2015). The system bookmarks clinician state to support seamless task resumption.

#### 2.3.1 Session Bookmark Mechanism

On session timeout (15 minutes inactivity) or manual logout, the system persists to the server:

| Data Point | Storage |
|---|---|
| Current page URL | `session_bookmarks.url` |
| Active patient context (MRN) | `session_bookmarks.patient_mrn` |
| Form state (all field values) | `session_bookmarks.form_state` (JSON) |
| Cursor position (active field ID) | `session_bookmarks.cursor_field` |
| Timestamp | `session_bookmarks.created_at` |

#### 2.3.2 Resume Prompt

On re-login within 8 hours of the bookmark:

```
+--------------------------------------------+
| Resume where you left off?                 |
|                                            |
| Patient: John Mukasa (MRN: M-2024-00451)  |
| Screen: OPD Consultation — SOAP Notes      |
| Time: 14:32 (2 hours ago)                  |
|                                            |
| [Resume]              [Start Fresh]        |
+--------------------------------------------+
```

On "Resume": the system navigates to the bookmarked URL, repopulates form fields, places the cursor in the last active field, and highlights incomplete fields with an amber (`--warning`) left border (4px solid).

On "Start Fresh": the bookmark is deleted and the user lands on the dashboard.

### 2.4 Triage Queue Display

#### 2.4.1 Queue Table Layout

| Column | Width | Content |
|---|---|---|
| # | 40px | Queue position number |
| Triage | 120px | `TriageBadge` (colour + icon + text) |
| Patient | 200px | Name (bold), age, sex |
| Wait Time | 100px | "Xh Ym" since registration, bold red if > threshold |
| Complaint | 250px | Chief complaint text (truncated at 60 characters) |
| Assigned | 150px | Doctor/CO name or "Unassigned" |
| Action | 80px | "Start" button |

#### 2.4.2 Queue Behaviour

1. Rows are colour-coded by triage level: left border 4px solid using the triage token colour.
2. Emergency patients (Level 1) are auto-sorted to the top of the queue regardless of arrival time. Within the same triage level, patients are sorted by arrival time (earliest first).
3. Wait time thresholds trigger visual escalation:
   - Emergency: > 5 minutes — wait time text turns bold red, row background pulses
   - Urgent: > 30 minutes — wait time text turns bold red
   - Semi-urgent: > 60 minutes — wait time text turns bold orange
   - Non-urgent: > 120 minutes — wait time text turns bold orange
4. Queue updates in real-time via WebSocket. When a new patient is triaged, the row animates into position (300ms ease-in-out slide).
5. An audible alert tone plays when an Emergency patient enters the queue (configurable per facility).

### 2.5 Vital Signs Chart

#### 2.5.1 Sparkline Trends

Each vital sign displays as a sparkline (64px height, 120px width) showing the last 10 recorded values over time. The sparkline renders using Canvas or SVG (no external charting library required for this component).

| Vital Sign | Unit | Normal Range (Adult) | Sparkline Colour |
|---|---|---|---|
| Temperature | C | 36.1-37.2 | Blue (`--primary`) |
| Systolic BP | mmHg | 90-140 | Blue (`--primary`) |
| Diastolic BP | mmHg | 60-90 | Blue (`--primary`) |
| Pulse Rate | bpm | 60-100 | Blue (`--primary`) |
| SpO2 | % | 95-100 | Blue (`--primary`) |
| Respiratory Rate | /min | 12-20 | Blue (`--primary`) |

Abnormal data points on the sparkline are rendered as red dots (`--danger`). Normal data points are rendered as blue dots (`--primary`).

#### 2.5.2 NEWS2 Score Display

The National Early Warning Score 2 (NEWS2) is calculated automatically from vital sign entries and displayed as a `NEWS2ScoreBadge`:

| Score Range | Colour Token | Clinical Risk | Action |
|---|---|---|---|
| 0-4 | `--news2-low` | Low | Routine monitoring |
| 5-6 | `--news2-medium` | Medium | Urgent clinical review |
| 7+ | `--news2-high` | High | Emergency clinical review |

The badge is 32x32px, circular, with the numeric score centred in white text on the coloured background. Scores of 7+ trigger a visual pulse animation and an in-app notification to the nurse station.

### 2.6 Lab Results Display

#### 2.6.1 Single Result Layout

```
+---------------------------------------------------------------+
| Haemoglobin (Hb)                                    [Trend]   |
|                                                               |
|   Value: 8.2 g/dL  [L]        Reference: 12.0 - 16.0 g/dL   |
|   ████░░░░░░░░░░░░             (progress bar: value vs range) |
|                                                               |
|   Collected: 03 Apr 2026 09:15   Validated: 03 Apr 2026 10:30|
|   Technician: Lab Tech Name      Validator: Lab Supervisor    |
+---------------------------------------------------------------+
```

#### 2.6.2 Design Rules for Lab Results

1. **H/L Flags:** Values below the reference range display a blue "L" badge. Values above display a red "H" badge. Both badges use `--abnormal` colour.
2. **Trend Lines:** When 3+ results exist for the same test, a trend line chart (200px height) replaces the sparkline, showing all historical values with date labels on the X-axis and value on the Y-axis. The normal range is displayed as a green shaded band.
3. **Critical Values:** Critical results display a pulsing red indicator (`--critical-value`, 1-second opacity cycle animation). The indicator cannot be dismissed until the clinician clicks "Acknowledge." Acknowledgement is logged with clinician ID, timestamp, and action taken.
4. **Icon-Based Severity:** Following Coiera's finding that icon-based indicators yield 82% correct decisions versus 56% for pie charts, all lab result severity is communicated via icons paired with colour, not chart-based visualisations alone.

### 2.7 Bed Management Visual Map

#### 2.7.1 Ward Grid Layout

Each ward is displayed as a grid of `BedIcon` components arranged to match the physical ward layout (configurable by the facility admin).

```
+----- Ward: Male Medical (24 beds) -----+
|  [B1]  [B2]  [B3]  [B4]  [B5]  [B6]  |
|                                         |
|  [B7]  [B8]  [B9]  [B10] [B11] [B12]  |
|                                         |
|  ===== Nurses Station =====            |
|                                         |
|  [B13] [B14] [B15] [B16] [B17] [B18]  |
|                                         |
|  [B19] [B20] [B21] [B22] [B23] [B24]  |
+-----------------------------------------+

Legend: [Green] Available  [Blue] Occupied  [Yellow] Reserved  [Grey] Maintenance
```

#### 2.7.2 Bed Icon Specification

| State | Background | Content | Click Action |
|---|---|---|---|
| Available | `--bed-available` | Bed number only | Opens admission form |
| Occupied | `--bed-occupied` | Bed number + patient name (truncated) | Opens patient summary |
| Reserved | `--bed-reserved` | Bed number + "Reserved" | Shows reservation details |
| Maintenance | `--bed-maintenance` | Bed number + wrench icon | Shows maintenance note |

Each bed icon is 80x60px minimum. An acuity indicator dot (8px circle) is positioned at the top-right corner of occupied beds, using NEWS2 colour tokens to reflect clinical acuity.

---

## 3. Role-Specific Screen Layouts

### 3.1 Doctor / Clinical Officer Workflow

#### 3.1.1 OPD Workflow Screens

| Step | Screen | Key Actions | Target Click Count |
|---|---|---|---|
| 1 | Doctor Queue | View assigned patients, select next patient | 1 click |
| 2 | Clinical Summary | Review patient banner, vitals, problems, labs, meds | 0 clicks (auto-loads) |
| 3 | SOAP Notes | Enter Subjective, Objective, Assessment, Plan | Keyboard-driven |
| 4 | Diagnosis | ICD-10/11 search with local term mapping ("red weepy eyes" maps to conjunctivitis) | 2 clicks (search + select) |
| 5 | Prescription | Drug search, dose, frequency, duration, route, quantity. Stock availability shown inline | 3 clicks per drug |
| 6 | Investigations | Lab/radiology/ECG request with urgency flag | 2 clicks per test |
| 7 | Referral | Internal/external referral with auto-generated letter | 3 clicks |
| 8 | Follow-up | Book follow-up appointment from consultation screen | 2 clicks |
| 9 | Complete | "Complete & Next" advances to next patient | 1 click |

Total clicks for a routine consultation (SOAP + 1 diagnosis + 2 prescriptions + 1 lab): 14 or fewer.

#### 3.1.2 IPD Workflow Screens

| Step | Screen | Key Actions |
|---|---|---|
| 1 | Ward List | View admitted patients by ward, sorted by acuity |
| 2 | Patient Summary | Full clinical summary with admission timeline |
| 3 | Ward Round Notes | Structured progress note: findings, assessment, plan, orders |
| 4 | Orders | Lab, radiology, procedure, medication orders with urgency flags |
| 5 | Discharge | Discharge summary, letter generation, medication reconciliation, follow-up booking |

### 3.2 Nurse / Midwife Workflow

#### 3.2.1 Triage Screen

The triage screen is optimised for tablet use (landscape orientation, touch-friendly inputs).

| Field | Input Type | Size | Notes |
|---|---|---|---|
| Blood Pressure | Two numeric fields (sys/dia) | 64px height | Large touch targets |
| Temperature | Numeric with decimal | 64px height | Route selector (axillary/oral/tympanic) |
| Pulse Rate | Numeric | 64px height | Regularity dropdown |
| SpO2 | Numeric with % | 64px height | On room air / oxygen selector |
| Respiratory Rate | Numeric | 64px height | Auto-starts 60-second timer |
| Weight | Numeric with decimal | 64px height | kg |
| Height | Numeric | 64px height | cm |
| BMI | Auto-calculated | Read-only | Highlighted if outside range |
| MUAC | Numeric | 64px height | cm, colour-coded by malnutrition threshold |
| Chief Complaint | Free text | 80px height | Auto-suggest from common complaints |
| Triage Level | 4-button selector | 48px height each | Colour-coded buttons matching triage tokens |

All input fields are 64px minimum height for touch accuracy. The triage level selector uses large, colour-coded buttons rather than a dropdown.

#### 3.2.2 Nursing Ward Screen

| Section | Layout | Interaction |
|---|---|---|
| Nursing Notes | Shift-by-shift timeline (expandable cards) | Coded templates + free-text narrative area |
| Drug Round (MAR) | Scrollable table: patient rows, drug columns, time slots | One-tap: Given / Held / Refused / Omitted per cell |
| Fluid Balance | Two-column layout: intake (left) and output (right) with running total | Numeric input per entry with timestamp |
| Vital Signs | Entry form + sparkline trend chart | Same touch-friendly fields as triage |

The drug round (Medication Administration Record) screen is designed for one-handed tablet operation. Action buttons are 48x48px minimum, positioned on the right side of each row for right-hand thumb reach. Swipe gestures are avoided — all actions use tap.

#### 3.2.3 Maternity Screen

| Sub-Screen | Content |
|---|---|
| ANC Registration | EDD calculator, gestational age, risk factors, PMTCT status |
| ANC Visit (ANC1-ANC8+) | Structured form per visit with coded fields + narrative |
| Partograph | Graphical cervicogram: X-axis = time (hours), Y-axis = dilation (cm). FHR, contractions, maternal vitals plotted on the same time axis. Alert and action lines drawn automatically |
| Delivery Record | Mode of delivery, outcome, birth weight, APGAR at 1/5/10 min, complications |
| Newborn Record | Linked to mother, neonatal assessment, immunisation at birth, breastfeeding status |
| Postnatal (PNC1-PNC3) | Structured visit form, danger signs checklist |

The partograph is the most complex clinical chart in the system. It renders as an interactive SVG canvas. Clinicians plot data points by tapping the chart at the correct coordinate. Previously plotted points connect automatically. The alert line and action line are drawn as dashed lines per WHO protocol.

### 3.3 Pharmacist Workflow

#### 3.3.1 Prescription Queue Screen

| Column | Width | Content |
|---|---|---|
| # | 40px | Queue position |
| Patient | 180px | Name, MRN |
| Drug(s) | 250px | Drug name with Tall Man Lettering, dose, frequency |
| Prescriber | 150px | Doctor/CO name |
| Priority | 80px | URGENT badge (red) or normal |
| Stock | 80px | Green tick (in stock) / red "!" (low) / grey "X" (out of stock) |
| Action | 100px | "Dispense" button |

#### 3.3.2 Dispensing Workflow

The dispensing workflow follows a 5-step linear process:

1. **Select** — Click "Dispense" on queue row. Patient details and prescription load.
2. **Verify** — Pharmacist reviews drug, dose, frequency, duration, interactions. CDS alerts display if applicable. Pharmacist confirms or queries prescriber.
3. **Dispense** — Select batch (FIFO enforced), enter quantity dispensed. Partial dispensing supported with pending balance recorded.
4. **Label** — Generate dispensing label (patient name, drug, dose, frequency, duration, dispensed date, facility name). Print or display for manual labelling.
5. **Next** — Advance to next prescription in queue.

Stock indicators beside each drug update in real-time. If stock falls below minimum level during dispensing, an amber alert appears.

#### 3.3.3 Narcotic Register Screen

The narcotic/controlled drug register is a separate screen accessible from the pharmacy menu. It requires dual-entry: the dispensing pharmacist enters the record, and a second authorised user (pharmacist or facility admin) verifies the entry. The register displays:

| Column | Content |
|---|---|
| Date/Time | Dispensing timestamp |
| Patient | Name, MRN |
| Drug | Name, form, strength |
| Quantity | Dispensed quantity |
| Balance | Running stock balance |
| Dispensed By | Pharmacist name |
| Verified By | Second authoriser name |
| Prescriber | Doctor/CO name |

### 3.4 Lab Technician Workflow

#### 3.4.1 Pending Requests Queue

| Column | Width | Content |
|---|---|---|
| # | 40px | Queue position |
| Priority | 80px | URGENT (red badge) / STAT / Routine |
| Patient | 180px | Name, MRN, location (OPD/Ward) |
| Test(s) | 250px | Test names with specimen type |
| Requested By | 150px | Clinician name |
| Requested At | 120px | Date/time with elapsed indicator |
| Status | 100px | Requested / Collected / Processing / Ready |
| Action | 100px | "Collect" / "Enter Result" button |

URGENT requests are sorted to the top. Rows older than the facility-defined turnaround time are highlighted with an amber background.

#### 3.4.2 Result Entry Screen

| Field | Input Type | Notes |
|---|---|---|
| Test Name | Read-only | Pre-populated from request |
| Result Value | Numeric or categorical | Type depends on test definition |
| Unit | Read-only | Pre-populated from test definition |
| Reference Range | Read-only | Displayed beside input, age/sex-specific |
| Flag | Auto-calculated | H (high), L (low), Critical — based on value vs reference range |
| Method | Dropdown | Analyser, manual, point-of-care |
| Comments | Free text | Optional clinical notes |

When a result value falls within the critical range, a modal alert fires immediately:

```
+----------------------------------------------------+
| CRITICAL VALUE ALERT                               |
|                                                    |
| Patient: Jane Auma (MRN: M-2024-00892)             |
| Test: Potassium (K+)                               |
| Value: 6.8 mmol/L  [CRITICAL HIGH]                |
| Reference: 3.5 - 5.0 mmol/L                       |
| Critical Range: > 6.0 mmol/L                      |
|                                                    |
| Action Required:                                   |
| Notify the requesting clinician immediately.       |
|                                                    |
| [Escalate to Clinician]    [Acknowledge & Call]    |
+----------------------------------------------------+
```

The "Escalate to Clinician" button sends an in-app notification and SMS to the requesting clinician. The alert is logged with the technician's acknowledgement timestamp.

### 3.5 Receptionist / Front Desk Workflow

#### 3.5.1 Patient Registration Wizard

Registration follows a 4-step wizard with a progress stepper at the top:

| Step | Title | Fields |
|---|---|---|
| 1 | Demographics | First name, last name, date of birth (or estimated age), sex, nationality, marital status, occupation, religion |
| 2 | Identifiers & Contact | Phone (primary + secondary), NIN, passport, UNHCR ID, insurance member number, address (district/sub-county/village), email (optional) |
| 3 | Photo & Category | Photo capture (webcam or upload), patient category (adult/paediatric/staff/VIP/indigent/refugee), guardian/next-of-kin details |
| 4 | Review & Save | Summary of all entered data, "Save & Register" button, MRN auto-generated |

#### 3.5.2 Duplicate Detection

Before saving (Step 4), the system runs EMPI probabilistic matching against existing records. If potential duplicates are found, a modal displays:

```
+---------------------------------------------------------------+
| Potential Duplicate Records Found                             |
|                                                               |
| The following existing records match the new registration:    |
|                                                               |
| 1. John Mukasa (MRN: M-2024-00451) — Match: 92%             |
|    DOB: 15 Mar 1985 | Phone: 0772-XXX-XXX | NIN: CM8XXXXXX  |
|    [View Record]                                              |
|                                                               |
| 2. John Mukassa (MRN: M-2023-01892) — Match: 78%            |
|    DOB: 15 Mar 1986 | Phone: 0701-XXX-XXX | NIN: —          |
|    [View Record]                                              |
|                                                               |
| [This is a new patient — Save]    [Select existing record]   |
+---------------------------------------------------------------+
```

Match confidence is displayed as a percentage. The receptionist can view existing records, select one (updating it if needed), or confirm the registration is a new patient.

#### 3.5.3 Appointment Booking

The appointment screen uses a calendar view (weekly default, switchable to daily/monthly) showing doctor availability slots:

| Element | Specification |
|---|---|
| Calendar grid | Columns = doctors, rows = 30-minute time slots |
| Available slot | White cell, clickable |
| Booked slot | Blue cell with patient name |
| Blocked slot | Grey cell (doctor unavailable) |
| Booking action | Click available slot, enter patient name (search), select visit type, confirm |
| Reminders | SMS sent at booking, 24 hours before, and 1 hour before (via Africa's Talking) |

#### 3.5.4 Queue Management

The receptionist manages the OPD queue by assigning registered patients to doctor queues. The interface supports:

- Button-based queue assignment (select patient, select doctor, click "Add to Queue")
- Drag-and-drop reordering within a queue (desktop only)
- Transfer between queues (reassign patient to a different doctor)
- Visual queue length indicator per doctor

### 3.6 Cashier / Billing Clerk Workflow

#### 3.6.1 Patient Account Screen

```
+---------------------------------------------------------------+
| Patient: John Mukasa (MRN: M-2024-00451)                     |
| Category: Adult | Insurance: AAR (Member #: AAR-12345)       |
+---------------------------------------------------------------+
|                                                               |
| Current Charges                                               |
| +---+---------------------------+----------+---------+        |
| | # | Item                      | Qty      | Amount  |        |
| +---+---------------------------+----------+---------+        |
| | 1 | OPD Consultation          | 1        | 30,000  |        |
| | 2 | Amoxicillin 500mg caps    | 21       | 15,750  |        |
| | 3 | Full Blood Count          | 1        | 25,000  |        |
| | 4 | Malaria RDT               | 1        | 10,000  |        |
| +---+---------------------------+----------+---------+        |
|                           Total:            | 80,750  |        |
|                           Insurance covers: | 64,600  |        |
|                           Patient pays:     | 16,150  |        |
|                                                               |
| +-----------------------------------------------------------+ |
| | Payment Entry                                              | |
| | [Cash] [MTN MoMo] [Airtel Money]                          | |
| |                                                            | |
| | Amount: [________] UGX                                     | |
| |                                                            | |
| | [Record Payment]                                           | |
| +-----------------------------------------------------------+ |
|                                                               |
| [Print Receipt]                              [Print Invoice]  |
+---------------------------------------------------------------+
```

#### 3.6.2 Payment Method Tabs

| Tab | Workflow |
|---|---|
| Cash | Enter amount received, system calculates change. Record payment |
| MTN MoMo | Enter patient phone number, initiate MoMo push. System polls for confirmation via MTN MoMo API. Status: Pending / Confirmed / Failed |
| Airtel Money | Enter patient phone number, initiate Airtel push. System polls for confirmation via Airtel Money API. Status: Pending / Confirmed / Failed |

The "Print Receipt" button is prominently placed (large, `--primary` background, 48px height) as receipt printing is the final action for every payment. The button generates a thermal printer-formatted receipt or A4 receipt depending on facility configuration.

#### 3.6.3 End-of-Day Reconciliation

| Element | Content |
|---|---|
| Cash collected | Total cash payments for the shift |
| MoMo collected | Total mobile money payments with transaction references |
| Airtel collected | Total Airtel Money payments with transaction references |
| Expected total | Sum of all payments |
| Actual cash in drawer | Cashier enters counted amount |
| Variance | Expected minus actual, highlighted red if non-zero |
| Approval | Facility admin sign-off required if variance exceeds facility threshold |

### 3.7 Patient Portal and Mobile App

#### 3.7.1 Dashboard (Patient Home Screen)

```
+-------------------------------------------+
| Good morning, John                        |
| MRN: M-2024-00451                         |
+-------------------------------------------+
|                                           |
| [Upcoming Appointments]                   |
|   Dr. Nakamya — 05 Apr 2026, 10:00 AM    |
|   General Consultation                    |
|   [Cancel] [Reschedule]                   |
|                                           |
| [Latest Results]                          |
|   FBC — 03 Apr 2026 — Ready              |
|   Malaria RDT — 03 Apr 2026 — Negative   |
|   [View All Results]                      |
|                                           |
| [Current Medications]                     |
|   Metformin 500mg — 2x daily             |
|   Next dose: 6:00 PM today               |
|   [View All]                              |
|                                           |
| [Account Balance]                         |
|   Outstanding: UGX 45,000                 |
|   [Pay Now]                               |
|                                           |
+-------------------------------------------+
| [Home] [Results] [Appointments] [Pay] [Me]|
+-------------------------------------------+
```

#### 3.7.2 Lab Results for Patients

Patient-facing lab results include plain-language explanations alongside clinical values:

```
+-------------------------------------------+
| Haemoglobin (Hb)                          |
|                                           |
| Your result: 13.5 g/dL                    |
| Normal range: 12.0 - 16.0 g/dL           |
| Status: Normal [green tick]               |
|                                           |
| What this means:                          |
| Haemoglobin carries oxygen in your blood. |
| Your level is within the normal range,    |
| which means your blood is carrying oxygen |
| well.                                     |
|                                           |
| [View Trend] [Download PDF]               |
+-------------------------------------------+
```

Abnormal results include a recommendation to discuss with the doctor. Critical values are not shown in the patient portal until acknowledged by a clinician.

#### 3.7.3 Payment Flow (Mobile)

1. Tap "Pay Now" on dashboard or account screen
2. View outstanding charges
3. Enter amount to pay (or tap "Pay Full Balance")
4. Select payment method: MTN MoMo or Airtel Money
5. Enter phone number (pre-filled from profile)
6. Confirm payment — system initiates push to phone
7. Patient approves on their MoMo/Airtel PIN prompt
8. Confirmation screen with receipt number
9. Receipt available in payment history

#### 3.7.4 Medication Reminders

- Reminders are push notifications at the scheduled dose time
- Tap notification to open the app and confirm: "Taken" or "Skipped"
- Adherence streak visualisation: calendar view with green (taken), red (skipped), grey (no data) days
- Reminders are opt-in and configurable per medication

#### 3.7.5 Family Members

A patient can link multiple family members (children, dependants) under a single app login. The dashboard displays a member selector at the top:

```
[John (You)] [Baby Sarah] [Mary Mukasa]
```

Tapping a family member switches the dashboard context to show that member's appointments, results, medications, and balance.

---

## 4. Accessibility

### 4.1 Compliance Targets

| Interface | Standard | Level |
|---|---|---|
| Staff web portal | WCAG 2.1 | AA |
| Patient web portal | WCAG 2.1 | AAA |
| Android patient app | WCAG 2.1 | AAA |
| iOS patient app | WCAG 2.1 | AAA |
| Android CHW app | WCAG 2.1 | AA |

### 4.2 Visual Accessibility

1. Colour coding is always paired with a text label, icon, or pattern. Colour alone never conveys meaning (WCAG 1.4.1).
2. All text meets minimum contrast ratios: 4.5:1 for normal text (AA), 7:1 for patient-facing normal text (AAA).
3. Focus indicators are visible on all interactive elements (2px solid `--primary` outline with 2px offset).
4. No content flashes more than 3 times per second (WCAG 2.3.1). The critical value pulse animation uses opacity fading, not flashing.

### 4.3 Touch and Motor Accessibility

1. Touch targets: minimum 48x48px for all interactive elements on tablet and mobile (WCAG 2.5.8 Target Size).
2. Triage input fields: 64px height for clinical workstation tablets.
3. Drug round (MAR): buttons positioned for right-hand thumb reach on tablet. No swipe gestures required for primary actions.
4. All web interfaces support full keyboard navigation (Tab, Shift+Tab, Enter, Escape, Arrow keys).

### 4.4 Screen Reader Support

1. All clinical screens use semantic HTML (`<main>`, `<nav>`, `<section>`, `<article>`, `<aside>`).
2. All images and icons have `alt` text or `aria-label`.
3. Dynamic content updates (queue changes, sync status) use `aria-live` regions:
   - Triage queue updates: `aria-live="polite"`
   - Critical value alerts: `aria-live="assertive"`
   - Sync status: `aria-live="polite"`
4. CDS alert modals use `role="alertdialog"` with `aria-describedby` linking to the alert content.
5. Patient banner uses `role="banner"` with structured `aria-label` describing patient identity.

### 4.5 Language and Localisation

1. The web interface supports English (default) and Luganda. Language is selectable per user.
2. The patient app supports English, Luganda, and Luo (Phase 3).
3. All date formats follow the facility-configured locale (default: DD MMM YYYY, e.g., "03 Apr 2026").
4. All currency values display with the facility-configured currency symbol (default: UGX) and thousand separators.

---

## 5. Responsive Design

### 5.1 Breakpoints

| Breakpoint | Width | Target Device | Orientation |
|---|---|---|---|
| xs | 320px | Budget Android phone (patient app) | Portrait |
| sm | 576px | Standard smartphone | Portrait |
| md | 768px | Tablet (nursing, triage) | Landscape |
| lg | 1024px | Clinical workstation (OPD, pharmacy, lab) | Landscape |
| xl | 1440px | Admin desktop (reports, analytics) | Landscape |

### 5.2 Optimisation Targets

| Interface | Primary Breakpoint | Rationale |
|---|---|---|
| OPD Clinical Summary | 1024px (lg) | Most hospital workstations run 1024x768 |
| Triage Entry | 768px (md) | Tablet in landscape at triage desk |
| Drug Round (MAR) | 768px (md) | Tablet held in one hand at bedside |
| Patient Portal (web) | 320px (xs) | Budget Android phones accessing via Chrome |
| Patient App (Android) | 320px (xs) | Budget Android phones (1 GB RAM, 5-year-old devices) |
| Admin Reports | 1440px (xl) | Desktop browsers for management dashboards |
| Receptionist Registration | 1024px (lg) | Desktop at front desk |
| Cashier Billing | 1024px (lg) | Desktop at cashier window |

### 5.3 Responsive Behaviour by Component

| Component | < 768px | 768px-1024px | > 1024px |
|---|---|---|---|
| Patient Banner | Stacked (photo above text) | Single row, truncated | Full single row |
| Summary Cards | Stacked vertically | 2-column grid | 4-column grid |
| SOAP Tabs | Accordion (vertical) | Tabs (horizontal) | Tabs (horizontal) |
| Queue Table | Card list (one card per patient) | Compact table (fewer columns) | Full table |
| Bed Map | 3-column grid | 4-column grid | 6-column grid |
| Sidebar Nav | Off-canvas (hamburger toggle) | Collapsed icon sidebar | Full sidebar with labels |

### 5.4 Orientation Rules

| Context | Required Orientation | Rationale |
|---|---|---|
| Partograph | Landscape only | Time-axis requires horizontal space |
| Drug Round (MAR) | Landscape preferred | Table columns need width |
| Patient App | Portrait | Phone standard |
| CHW App | Portrait | Phone standard, field use |
| Clinical Workstation | Landscape | Desktop/laptop |

---

## 6. Offline UX

### 6.1 Offline Indicator

When the device loses internet connectivity, a persistent banner appears at the top of every screen:

```
+---------------------------------------------------------------+
| [!] Offline — changes will sync when connected  [3 pending]   |
+---------------------------------------------------------------+
```

| Element | Specification |
|---|---|
| Banner position | Fixed top, below the main navigation bar |
| Background colour | `--warning` at 15% opacity |
| Text colour | `--text-primary` |
| Icon | Tabler `cloud-off` icon |
| Pending count | Badge showing number of queued transactions |
| Persistence | Banner remains visible on every page until connectivity restores |

### 6.2 Sync Status

On reconnection, the banner transitions to a sync progress state:

```
+---------------------------------------------------------------+
| [↑] Syncing 3 changes...  [████████░░░░░░░░]  2 of 3         |
+---------------------------------------------------------------+
```

| Element | Specification |
|---|---|
| Background colour | `--info` at 15% opacity |
| Progress bar | Determinate, showing X of Y transactions synced |
| Duration | Each transaction syncs individually; progress updates per transaction |
| Completion | Banner transitions to "All changes synced" (green, 3-second display) then disappears |

### 6.3 Conflict Resolution

If a synced record conflicts with a server-side change (e.g., another user modified the same patient record while offline), a notification appears:

```
+---------------------------------------------------------------+
| [!] 1 sync conflict requires review                           |
|                                            [Review Conflicts] |
+---------------------------------------------------------------+
```

The "Review Conflicts" link opens a conflict resolution screen showing:

| Column | Content |
|---|---|
| Record | Patient name, MRN, record type |
| Your Change | Field values from offline edit |
| Server Value | Field values from server |
| Conflict Fields | Highlighted differences |
| Action | "Keep Mine" / "Keep Server" / "Merge" buttons |

### 6.4 Downtime Kit

A "Print Offline Forms" button is available in the facility admin settings and on the offline banner. It generates printable PDF forms matching the digital interface layout:

| Form | Content |
|---|---|
| OPD Register | Patient columns matching HMIS format |
| Triage Form | Vital signs entry fields |
| Prescription Form | Drug, dose, frequency, duration, quantity fields |
| Lab Request Form | Patient details, tests requested, specimen type |
| Cash Receipt Book | Receipt number, patient, amount, payment method |
| Ward Patient List | Bed assignments, diagnoses, current medications |
| MAR Sheet | Medication administration record per patient per shift |
| Dispensing Log | Drug, quantity, patient, batch, expiry |

Forms are pre-populated with the current patient list and ward assignments where applicable. They include the facility name, date, and sequential form numbers for manual tracking.

### 6.5 Auto-Save and Power-Loss Resilience

1. Every form interaction (field blur, dropdown selection, checkbox toggle) triggers an auto-save to local storage (IndexedDB on web, Room on Android, SwiftData on iOS).
2. Auto-save fires every 10 seconds during active typing.
3. On power loss and subsequent restart, the system detects unsaved form state and presents the `TaskResumptionPrompt`.
4. The save status indicator is visible at all times in the form footer: "Saved locally" (green tick) or "Saving..." (spinner).

---

## 7. Onboarding UX

### 7.1 Progressive Module Activation

Facilities start with only the modules included in their subscription tier. The navigation sidebar displays only activated modules. Inactive modules are hidden entirely — not greyed out — to avoid cognitive overload (Hick's Law).

When the facility admin activates a new module:

1. The module menu item appears in the sidebar with a "NEW" badge (blue, auto-removed after 7 days).
2. A guided walkthrough overlay highlights key screens and actions for the new module.
3. A training video link is displayed in the module's empty state screen.

### 7.2 New Facility Setup Wizard

When a new facility is provisioned, the facility admin is guided through a 5-step setup wizard:

| Step | Title | Content |
|---|---|---|
| 1 | Facility Information | Name, type (clinic/HC III/HC IV/hospital), location, logo upload, contact details, operating hours |
| 2 | Price List | Import default price list or upload custom. Set patient category multipliers (e.g., staff = 50%, VIP = 150%) |
| 3 | Staff Accounts | Create initial staff accounts with roles. Bulk invite via email or phone number |
| 4 | Module Selection | Toggle modules to activate. Dependencies are enforced (e.g., Pharmacy requires OPD) |
| 5 | Go Live | Summary review. "Start Using Medic8" button. Confetti animation on completion |

Each step has a "Skip for Now" option (except Step 1, which is mandatory). Skipped steps are tracked and the admin is reminded to complete them via a persistent setup checklist widget on the dashboard.

### 7.3 In-App Training Mode

Each module has an optional training mode accessible from the help menu (Tabler `help-circle` icon in the top navigation bar).

| Feature | Specification |
|---|---|
| Walkthrough | Step-by-step overlay highlighting UI elements with tooltip explanations |
| Sample data | Training mode loads demo data (clearly marked with "[DEMO]" watermark) |
| Reset | "Reset Training Data" button clears demo records |
| Completion | Checklist of training tasks per module with progress percentage |

### 7.4 Help Menu

The help menu (`?` icon) is accessible from every screen and provides:

| Item | Action |
|---|---|
| Module Guide | Opens walkthrough for the current module |
| Video Tutorials | Opens video library filtered to the current module |
| Keyboard Shortcuts | Displays shortcut reference card (web only) |
| Report a Problem | Opens issue submission form (screenshot capture, description, auto-attached context) |
| Contact Support | Displays support phone number and WhatsApp link |
| What's New | Changelog of recent updates relevant to the user's role |

### 7.5 Empty State Screens

Every module screen that can be empty (no data yet) displays a purposeful empty state:

| Element | Content |
|---|---|
| Illustration | Tabler-style line illustration relevant to the module (e.g., stethoscope for OPD) |
| Heading | Action-oriented: "No patients in queue yet" (not "Empty") |
| Description | Brief explanation: "Patients appear here after triage. Register a patient to get started." |
| Primary Action | Button linking to the prerequisite action: "Register a Patient" |
| Help Link | "Learn how this works" linking to the module video tutorial |

---

## 8. Navigation Structure

### 8.1 Primary Navigation — Staff Web Portal

The primary navigation is a left sidebar (280px expanded, 64px collapsed) that is persistent across all pages. Menu items are role-filtered per the stakeholder register.

```
Dashboard
├── Overview (KPI cards, queue summary, alerts)
├── Quick Actions (register patient, start triage)

Patients
├── Patient List (searchable by name, MRN, phone, NIN)
├── Register Patient (wizard)
├── Patient Search

OPD
├── Triage Queue
├── Doctor Queue (per-doctor view)
├── Consultation

IPD (Phase 2)
├── Ward List
├── Bed Map
├── Admissions
├── Nursing Station
├── Discharge

Emergency (Phase 2)
├── A&E Queue
├── Resuscitation

Maternity (Phase 2)
├── ANC Register
├── Labour Ward
├── Delivery Register
├── Postnatal

Pharmacy
├── Prescription Queue
├── Dispensing
├── Drug Formulary
├── Stock Management
├── Narcotic Register

Laboratory
├── Request Queue
├── Result Entry
├── QC Records
├── Equipment Interfaces (Phase 2)

Radiology (Phase 2)
├── Worklist
├── Report Entry

Billing
├── Patient Accounts
├── Payments
├── Receipts
├── Daily Reconciliation

Insurance (Phase 2)
├── Member Verification
├── Pre-Authorisation
├── Claims

Appointments
├── Calendar
├── Booking
├── Queue Management

Inventory (Phase 2)
├── Stock Overview
├── GRN
├── Transfers
├── Expiry Tracking

HMIS (Phase 2)
├── HMIS 105
├── HMIS 108
├── DHIS2 Upload

Reports
├── Clinical Reports
├── Financial Reports
├── Operational Reports
├── Custom Reports

Programmes (Phase 3)
├── HIV/AIDS
├── TB
├── Immunisation

Settings
├── Facility Profile
├── Users & Roles
├── Price List
├── Module Configuration
├── Audit Trail
├── Data Import/Export
```

### 8.2 Role-Based Menu Filtering

| Menu Section | Super Admin | Facility Admin | Doctor/CO | Nurse | Pharmacist | Lab Tech | Receptionist | Cashier | Patient |
|---|---|---|---|---|---|---|---|---|---|
| Dashboard | All tenants | Facility | Clinical | Nursing | Pharmacy | Lab | Front desk | Billing | Patient |
| Patients | Full | Full | Read-only | Read-only | Rx only | Lab only | Full | Lookup | Own |
| OPD | --- | Full | Full | Triage | Queue | --- | Queue | --- | --- |
| IPD | --- | Full | Full | Full | MAR | --- | --- | --- | --- |
| Pharmacy | --- | Full | --- | MAR | Full | --- | --- | --- | --- |
| Laboratory | --- | Full | Results | --- | --- | Full | --- | --- | --- |
| Billing | --- | Full | --- | --- | --- | --- | --- | Full | Own |
| Settings | Platform | Facility | --- | --- | --- | --- | --- | --- | --- |
| Reports | All | Facility | Clinical | Nursing | Pharmacy | Lab | --- | Financial | --- |

### 8.3 Patient App Navigation (Bottom Tab Bar)

The patient mobile app uses a 5-tab bottom navigation bar:

| Tab | Icon | Label | Content |
|---|---|---|---|
| 1 | House | Home | Dashboard with appointments, results, medications, balance |
| 2 | Flask | Results | Lab and radiology results list with detail view |
| 3 | Calendar | Appointments | Booking, upcoming, past appointments |
| 4 | Wallet | Pay | Outstanding balance, payment flow, payment history |
| 5 | User | Me | Profile, family members, settings, help |

---

## 9. Keyboard Shortcuts (Web Portal)

| Shortcut | Action | Context |
|---|---|---|
| `Ctrl+K` | Global patient search | Any screen |
| `Ctrl+N` | New patient registration | Any screen |
| `Ctrl+Enter` | Save current form | Any form |
| `Ctrl+Shift+Enter` | Complete & Next (advance queue) | Consultation screen |
| `Ctrl+P` | Print current view | Any screen |
| `Ctrl+/` | Open keyboard shortcut reference | Any screen |
| `Tab` / `Shift+Tab` | Navigate between form fields | Any form |
| `Escape` | Close modal or side panel | Any modal/panel |
| `Alt+1` through `Alt+4` | Switch SOAP tab (S/O/A/P) | Consultation screen |
| `Alt+Q` | Open queue panel | OPD screens |

---

## 10. Loading and Error States

### 10.1 Loading States

| Context | Loading Indicator | Specification |
|---|---|---|
| Page load | Skeleton screens | Grey placeholder blocks matching the page layout, 300ms fade-in |
| Data table load | Table skeleton | Grey rows matching column widths, shimmer animation |
| Form submission | Button spinner | Button text replaced with spinner + "Saving...", button disabled |
| Queue update | Row shimmer | New row slides in with 300ms ease-in-out animation |
| Sync | Progress bar | Determinate bar in `OfflineBanner` |
| Image load | Placeholder | Grey box with camera icon, replaced on load |

Skeleton screens are used instead of spinners for page-level loading to reduce perceived wait time (Doherty threshold: 400ms).

### 10.2 Error States

| Error Type | UI Treatment | User Action |
|---|---|---|
| Validation error | Red border on field + error message below field in `--danger` text | Fix field value |
| API error (4xx) | SweetAlert2 error modal with specific message | Retry or correct input |
| API error (5xx) | SweetAlert2 error modal: "Something went wrong. Your data has been saved locally." | Auto-retry in 30 seconds |
| Network error | `OfflineBanner` appears, form continues in offline mode | Continue working |
| Session expired | Full-screen overlay: "Your session has expired. Please log in again." | Redirect to login (bookmark saved) |
| Permission denied | SweetAlert2 warning: "You do not have permission to perform this action." | Contact facility admin |

### 10.3 Confirmation Dialogs

All destructive actions (delete, void, cancel, discharge) require a SweetAlert2 confirmation dialog:

| Element | Specification |
|---|---|
| Title | Action-specific: "Void this receipt?" (not "Are you sure?") |
| Text | Consequence description: "This will reverse all charges and cannot be undone." |
| Confirm button | Red (`--danger`) with action verb: "Void Receipt" |
| Cancel button | Grey outline: "Keep Receipt" |
| Icon | SweetAlert2 warning icon (amber triangle) |

---

## 11. Print Layouts

### 11.1 Printable Documents

| Document | Format | Paper Size | Trigger |
|---|---|---|---|
| Patient receipt | Thermal (80mm) or A4 | Configurable | "Print Receipt" button |
| Discharge summary | A4 | A4 | "Print" on discharge screen |
| Referral letter | A4 | A4 | "Print" on referral screen |
| Lab report | A4 | A4 | "Print" on result screen |
| Dispensing label | 50x25mm | Label | Auto-print on dispense |
| Prescription | A5 or A4 | Configurable | "Print Prescription" button |
| Invoice | A4 | A4 | "Print Invoice" button |
| Medical certificate | A4 | A4 | "Print" on certificate screen |
| Wristband | Wristband format | 25x250mm | "Print Wristband" on admission |
| Barcode label | 38x25mm | Label | "Print Label" on sample collection |

### 11.2 Print Stylesheet Rules

1. All print layouts use `@media print` CSS with `display: none` on navigation, sidebar, banners, and action buttons.
2. Facility header (name, logo, address, phone) is printed at the top of every A4 document.
3. Patient identification (name, MRN, date) is printed on every page of multi-page documents.
4. Colours are converted to greyscale for print except triage badges and CDS alert headers.
5. Thermal receipt format uses 80mm width, monospace font, and minimal margins.

---

*End of UX Specification*

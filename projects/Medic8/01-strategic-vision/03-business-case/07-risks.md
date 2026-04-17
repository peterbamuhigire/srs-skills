# 7 Risks

## 7.1 Risk Register

| # | Risk | Category | Probability | Impact | Mitigation | Owner |
|---|---|---|---|---|---|---|
| R-01 | Drug interaction database licensing delay — vendor negotiation or pricing exceeds budget, delaying Phase 1 clinical safety features | Technical | HIGH | HIGH | Begin vendor outreach immediately; evaluate DrugBank, RxNorm/NLM, and Uganda NDA formulary in parallel; budget USD 1,000-5,000 annually; defer CDS to post-MVP if licence unavailable at launch | Peter |
| R-02 | UMDPC software registration required — Uganda Medical and Dental Practitioners Council may classify Medic8 as regulated medical software, requiring formal registration before commercial sale | Regulatory | MEDIUM | HIGH | Contact UMDPC for regulatory determination before Phase 1 launch; prepare registration application documents; engage regulatory consultant if classification is ambiguous | Peter |
| R-03 | Solo developer capacity — all development, sales, support, and operations depend on a single person; illness, burnout, or competing priorities delay delivery | Business | HIGH | HIGH | Share codebase with Academia Pro to reduce redundant work; prioritise ruthlessly using phase gates; defer non-essential features; plan first support hire at 50 facilities; document architecture for future team onboarding | Peter |
| R-04 | ClinicMaster pivots to SaaS — ClinicMaster re-architects as cloud SaaS, closing its primary architectural gap and competing directly on delivery model | Competitive | LOW | HIGH | Maintain 20-feature advantage; ClinicMaster's desktop architecture makes SaaS migration a multi-year effort; focus on AI and multilingual differentiators ClinicMaster cannot replicate quickly | Peter |
| R-05 | Internet infrastructure remains poor — Ugandan internet connectivity at government and rural facilities remains too unreliable for cloud-dependent workflows | Technical | HIGH | MEDIUM | Offline-first architecture is the primary mitigation; all core clinical workflows operate without internet; sync resumes automatically when connectivity returns; SMS fallback for critical notifications | Peter |
| R-06 | NHIS API not published — Uganda National Health Insurance Scheme does not publish its provider API or claims format, blocking insurance integration | External | MEDIUM | MEDIUM | Register with NHIS as licensed healthcare software provider; build insurance module against private insurer formats (AAR, Jubilee) first; add NHIS integration when API is available; design claims engine to be format-configurable | Peter |
| R-07 | Medication error caused by CDS failure — Clinical Decision Support engine fails to fire an alert for a dangerous drug interaction or allergy conflict, resulting in patient harm | Clinical | LOW | CRITICAL | Licence a validated drug interaction database; define CDS as decision support (not decision maker) in Terms of Service; log every alert fired and every override; require pharmacist confirmation for all prescriptions; conduct pre-launch clinical safety validation with a practising clinician | Peter |
| R-08 | Data breach of patient records — Unauthorised access to Protected Health Information (PHI) through application vulnerability, insider threat, or infrastructure compromise | Security | LOW | CRITICAL | Implement RBAC+ABAC with sensitive record tier; encrypt PHI at rest and in transit; tamper-proof audit trail; break-the-glass emergency access with mandatory post-access audit; penetration testing before launch; incident response plan with 72-hour PDPO notification | Peter |
| R-09 | OpenMRS community backlash against migration messaging — Positioning Medic8 as a replacement for OpenMRS generates negative response from the OpenMRS community, PEPFAR implementing partners, or UgandaEMR stakeholders | Market | MEDIUM | LOW | Frame messaging as "complement and migration path" rather than "replacement"; offer validated data migration from OpenMRS/UgandaEMR; demonstrate TCO savings with specific numbers; avoid disparaging OpenMRS as a product | Peter |
| R-10 | Uganda PDPA enforcement action — National Information Technology Authority (NITA-U) or Personal Data Protection Office (PDPO) takes enforcement action against a healthcare software provider for non-compliance with the Data Protection and Privacy Act 2019 | Regulatory | LOW | HIGH | Engage Uganda data protection lawyer for health data legal review before Phase 1 launch; document consent categories per data type; define lawful basis for processing; establish breach notification procedure; appoint internal Data Protection Officer | Peter |
| R-11 | Mobile money API rate changes — MTN MoMo or Airtel Money increases transaction fees or changes API terms, affecting Medic8's payment processing model | Financial | MEDIUM | MEDIUM | Mobile money transaction fees are pass-through (charged to patient or facility, not Medic8); design billing engine to support multiple payment channels (mobile money, bank transfer, card); monitor API terms quarterly | Peter |
| R-12 | Customer churn from poor onboarding — Facilities sign up but abandon the system within 60 days due to inadequate onboarding, training, or support | Business | MEDIUM | HIGH | Embed guided onboarding in every module; provide video-based, module-specific training; mandatory training completion before module activation; structured check-ins at 30, 60, and 90 days; zero-config Ugandan defaults reduce setup friction; target 2-4 hour onboarding time | Peter |
| R-13 | AI provider API outage — Primary AI provider returns errors or does not respond, making AI capabilities unavailable | Technical | MEDIUM | LOW (clinical) / HIGH (AI features) | Secondary provider failover within 12 seconds of primary timeout; graceful UI degradation — AI panels are hidden, not broken; clinical workflows (prescription, discharge, claim submission) proceed without AI assistance when the provider is unavailable; all failover events are logged with timestamp, primary provider error, and failover outcome | Peter |
| R-14 | DPPA 2019 compliance for patient data sent to AI providers — Patient clinical data transmitted to AI providers may violate the Data Protection and Privacy Act 2019 if the provider does not comply with data residency or processing restrictions | Regulatory | MEDIUM | HIGH | Execute Data Processing Agreements (DPA) with each AI provider (OpenAI, Anthropic, DeepSeek, Gemini) before the AI Intelligence module launches; no personally identifiable information (NIN, full legal name, NIRA number) included in AI prompts — encounter data referenced by anonymised encounter ID only; tenant-configurable provider selection allows facilities to choose providers whose DPA terms satisfy their regulatory comfort; AI admin panel displays a compliance warning if the selected provider's infrastructure does not meet Uganda data residency requirements | Peter |
| R-15 | Translation quality in Kiswahili/French — A clinical string is awkwardly translated or clinically ambiguous in French or Kiswahili, leading to misinterpretation at the point of care | Quality | MEDIUM | HIGH | Native-speaker clinical review gate before any string enters a release branch; `[I18N-GAP]` CI flag blocks the `release` branch build until the gap is resolved by a human-approved translation; clinical severity labels (`Fatal`, `Serious`, `Warning`, `Info`) are treated as highest-priority review items and never auto-translated; specific prohibited translations documented in `_context/i18n.md` (e.g., *malalamiko ya kwanza* prohibited for Kiswahili chief complaint) | Peter |
| R-16 | AI false positives in Outbreak Early Warning — AI Outbreak Early Warning generates excessive false positive alerts, causing alarm fatigue for Medical Officers | Clinical | MEDIUM | MEDIUM | Configurable sensitivity threshold per disease; false positive rate tracked as a KPI in the AI admin panel over a rolling 90-day period; target ≤ 15% false positive rate; Medical Officer can adjust the sensitivity threshold from the admin panel without a code change; the alert explicitly states it is an AI-generated prompt and does not constitute a mandatory IDSR report | Peter |

## 7.2 Probability-Impact Matrix

The matrix classifies risks into 3 probability levels (Low, Medium, High) and 4 impact levels (Medium, High, Critical). Risk numbers correspond to the Risk Register above.

```
                              I M P A C T
                    Medium      High        Critical
                 +-----------+-----------+-----------+
          High   |   R-05    | R-01,R-03 |           |
                 +-----------+-----------+-----------+
P  Medium        | R-06,R-11,| R-02,R-12,|           |
r                | R-16      | R-14,R-15 |           |
o                +-----------+-----------+-----------+
b  Low           | R-09,R-13 | R-04,R-10 | R-07,R-08 |
                 +-----------+-----------+-----------+
```

### 7.2.1 Priority Classification

Immediate action required (High Probability + High/Critical Impact):

- R-01: Drug interaction database licensing delay.
- R-03: Solo developer capacity.

Active monitoring and mitigation (Medium Probability + High Impact, or High Probability + Medium Impact):

- R-02: UMDPC software registration.
- R-05: Internet infrastructure.
- R-12: Customer churn from poor onboarding.
- R-14: DPPA 2019 compliance for AI data.
- R-15: Translation quality in Kiswahili/French.

Contingency planning (Low Probability + Critical Impact):

- R-07: Medication error from CDS failure.
- R-08: Data breach of patient records.

Monitor (Low Probability + High Impact, or Medium Probability + Medium Impact):

- R-04: ClinicMaster pivots to SaaS.
- R-06: NHIS API not published.
- R-09: OpenMRS community backlash.
- R-10: Uganda PDPA enforcement action.
- R-11: Mobile money API rate changes.
- R-13: AI provider API outage (clinical impact is Low; AI feature impact is High for the duration of the outage).
- R-16: AI false positives in Outbreak Early Warning.

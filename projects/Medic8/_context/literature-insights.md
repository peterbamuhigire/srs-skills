# Literature Insights — Medic8

Actionable design insights distilled from 10 health informatics texts. Each insight names the enhancement, cites the source book and chapter, and maps to the Medic8 build phase where it applies.

## Clinical Safety Enhancements

1. **Four-tier CDS alert architecture** (Info / Warning / Serious / Fatal) with override logging and per-facility override rate tracking. Competitors use binary on/off alerts with 90%+ override rates. *Source: Rowlands Ch 44, Volpe Ch 5. Phase 1.*
2. **Five Rights of Medication Administration** enforced at CPOE: right patient, drug, dose, route, time. 56% of medication errors occur at prescribing. *Source: Volpe Ch 6. Phase 1.*
3. **Tall Man Lettering** for look-alike/sound-alike drugs (hydrOXYzine vs hydrALAZINE). Critical in SSA where multiple generics share similar names. *Source: Volpe Ch 6. Phase 1.*
4. **Weight-based paediatric dosing** with inline mg/kg calculators, dose rounding, adult ceiling dose cap. Decimal error guards to prevent 10x/100x overdose in neonates. Children face 3x the adult risk of medication errors. *Source: Lehmann Ch 25-26, 28. Phase 1.*
5. **Barcode Medication Administration (BCMA)** for IPD drug rounds: scan patient wristband + drug barcode before administering. *Source: Volpe Ch 6, Hussey Ch 3. Phase 2.*
6. **Medication reconciliation** at every transition of care (OPD to IPD, IPD to discharge, facility to facility). *Source: Volpe Ch 6. Phase 2.*
7. **Early Warning Scores (NEWS2) calibrated for SSA populations** — Western thresholds fail in Africa (Wheeler et al. 2013, Blantyre). Vital signs scoring for clinical deterioration prediction. *Source: Rivas Ch 7. Phase 2.*
8. **Incident reporting module** — medication errors, system downtime, alert overrides. Selling point for accreditation. *Source: Rowlands Ch 50. Phase 2.*
9. **14 Nursing Sensitive Outcomes (NSOs)** as system quality indicators. Each additional patient per nurse increases mortality by 7%. 10% more RN hours reduces pressure ulcers by 19%, sepsis by 15%. *Source: Hussey Ch 9. Phase 2.*
10. **Braden scale** (pressure ulcer risk) and fall risk auto-scoring at admission with alert escalation. *Source: Hussey Ch 9. Phase 2.*
11. **FMEA framework** for medication workflow safety — severity x occurrence x detection scoring to prioritise safety controls. *Source: Lehmann Ch 29. Phase 1.*
12. **Swiss cheese model** with layered defences. IT systems introduce new error classes while minimising existing ones. *Source: Coiera Ch 13. All phases.*
13. **Task resumption aid** — bookmark clinician position on interruption, highlight incomplete fields on return. Clinical environments average 6-7 interruptions per hour. *Source: Coiera Ch 4, Volpe Ch 7. Phase 1.*

## Data Architecture Enhancements

14. **EHR as data bus, not a module** — every module reads from and writes to a central clinical data bus. Event-driven architecture where a clinical encounter triggers downstream effects. *Source: Coiera Ch 10, Brown Ch 1. Phase 1.*
15. **openEHR two-level modelling** — stable Reference Model (database schema) + configurable clinical Archetypes per country/facility. The pattern for "one codebase, many countries." *Source: Sinha Ch 18. Phase 1.*
16. **EMPI with probabilistic + fuzzy matching** — name + DOB + NIN + phone. Soundex/Metaphone adapted for African naming patterns. Uganda has the "JOSE RODRIGUEZ" duplication problem. *Source: Volpe Ch 4, Brown Ch 13, WHO Ch 2. Phase 1.*
17. **Terminology Service** — single gateway to ICD-10, ICD-11, SNOMED CT, LOINC, RxNorm, ATC. Combined coverage reaches 93% of clinical concepts. *Source: Sinha Ch 11-17, Brown Ch 12. Phase 1.*
18. **SNOMED CT internally, ICD-10 at reporting boundary** — store clinical data as SNOMED concepts, auto-map to ICD-10 for HMIS/billing export. *Source: Coiera Ch 22-23. Phase 1.*
19. **LOINC for lab observations from day one** — backs the lab module for interoperability. *Source: Brown Ch 12, Rowlands Ch 39. Phase 1.*
20. **Disease registries as first-class entities** (HIV, TB, maternal, NCD) — not report filters. Feed HMIS reporting and enable proactive care (defaulter tracing). *Source: Brown Ch 10. Phase 2.*
21. **FHIR HTML narrative fallback** in every FHIR response for clinical safety when receiving systems cannot fully process structured data. *Source: Rowlands Ch 46. Phase 3.*
22. **CDA R2 for discharge summaries and referral letters** — machine-readable + human-readable clinical documents. *Source: Sinha Ch 8. Phase 2.*
23. **ABAC layered on RBAC** — role grants base access, attribute policies enforce fine-grained rules (HIV status visible only to treating clinician). *Source: Sinha Ch 32. Phase 1.*
24. **Configurable consent engine** as core platform service — India ABDM: opt-in, Australia My Health Record: opt-out, Uganda: minimal digital consent. Tenant-configurable. *Source: Coiera Ch 19. Phase 1.*
25. **SMART on FHIR** for third-party app substitutability. *Source: Coiera Ch 19. Phase 3.*
26. **ICD-10 Z-codes for social determinants of health** (SDoH) — housing, food security, education. Directly relevant for NGO facilities. *Source: Volpe Ch 13, Ch 24. Phase 3.*

## UX and Adoption Enhancements

27. **Single-page OPD clinical summary** — vitals, problems, labs, meds, allergies visible without scrolling or tab-switching. Clinicians spend 35% of time on EHR data entry. *Source: Rowlands Ch 35, Volpe Ch 7. Phase 1.*
28. **Configurable workflow state machines per facility type** — mission hospital vs government protocols differ for the same condition. *Source: Brown Ch 4. Phase 1.*
29. **Semi-structured nursing notes** — coded templates (checkboxes, dropdowns) + mandatory free-text narrative. Never force picklist-only. *Source: Hussey Ch 7. Phase 2.*
30. **NANDA-I/NIC/NOC care plan model** — nursing diagnoses linked to interventions linked to outcomes. *Source: Hussey Ch 7. Phase 2.*
31. **Real-time nurse manager dashboard** — bed census, acuity scores per bed, staffing vs actual per shift, patient churn rate. *Source: Hussey Ch 9. Phase 2.*
32. **C-HOBIC minimum dataset** at admission/shift/discharge — functional status, continence, symptoms, safety outcomes. *Source: Hussey Ch 3. Phase 2.*
33. **Computer-assisted ICD coding** — searchable lookup mapping local terms ("red weepy eyes" to conjunctivitis), auto-suggest from symptoms. Removes need for dedicated coding staff. *Source: WHO Ch 2. Phase 1.*
34. **Evidence-based data visualisation** — identical data as icons vs pie charts yields 82% vs 56% correct decisions. Lab trend lines, icon-based severity. *Source: Coiera Ch 4. Phase 1.*
35. **Per-module activation** — facility starts with registration + OPD, adds modules progressively. Each module independently useful. *Source: WHO Ch 5. Phase 1.*
36. **Parallel-run mode** — printable ward sheets and MAR forms mirroring paper formats during transition. *Source: Rowlands Ch 50. Phase 1.*
37. **Downtime kit** — pre-printable patient lists, medication sheets, census forms for offline use. *Source: WHO Ch 4. Phase 1.*
38. **Structured onboarding bundled into subscription** — workflow mapping, super-user training, 30/60/90 day check-ins. Reduces churn. *Source: Rowlands Ch 48. All phases.*
39. **Auto-save every form interaction** — not just on submit. Power-loss resilience. *Source: WHO Ch 3. Phase 1.*
40. **Data quality enforcement at point of entry** — mandatory fields, structured dropdowns, completion checklists. *Source: WHO Ch 1. Phase 1.*
41. **One-handed tablet design** for bedside drug rounds — physical reality of nursing. *Source: Hussey Ch 3. Phase 2.*
42. **Interruption recovery** — session state persistence, resume without data loss. *Source: Volpe Ch 7. Phase 1.*

## Paediatric Enhancements

43. **WHO growth charts with Z-scores** — percentiles, growth velocity, prematurity correction using gestational age. Both graphical and tabular views. *Source: Lehmann Ch 32. Phase 2.*
44. **Mother-baby dyad as core data concept** — link maternal record to neonatal record at birth. Handle temporary names, disambiguate twins. *Source: Lehmann Ch 4. Phase 2.*
45. **Catch-up immunisation schedule generation** when doses are missed — per national schedule. *Source: Lehmann Ch 17-18. Phase 2.*
46. **Guardian consent complexity** — consent-by-proxy, multiple guardians, emancipated minors, adolescent confidentiality for reproductive/substance health. *Source: Lehmann Ch 5. Phase 1.*
47. **Age-specific vital sign and lab normal ranges** — adult ranges are dangerous for children. Record cuff size, route, position for paediatric BP/temp. *Source: Lehmann Ch 31. Phase 1.*
48. **Developmental screening tools** (ASQ, PEDS) triggering referral pathways. *Source: Lehmann Ch 6. Phase 3.*

## Commercial and Strategic Enhancements

49. **Quadruple Aim sales positioning** — patient experience, population health, cost reduction, provider experience. Structure sales pitch around these four. *Source: Rivas Ch 1. Marketing.*
50. **CHW app as go-to-market channel** — not just a feature but a distribution strategy for government/NGO contracts. Simplified registration, immunisation, ANC on low-end Android over 2G. *Source: Rivas Ch 13. Phase 3.*
51. **Missing charge reports** — match encounters to billing to catch revenue leakage. *Source: Volpe Ch 4. Phase 1.*
52. **Store-and-forward telemedicine** — for dermatology, radiology, pathology consultations between rural and urban specialists. Reduces referrals by 68%. *Source: Coiera Ch 21. Phase 3.*
53. **Digital nudging for ART/TB adherence** — SMS reminders, adherence streak visualisation, opt-out scheduling. *Source: Rivas Ch 10. Phase 3.*
54. **RPA-ready task automation layer** for billing/claims — bot-driven claims follow-up. *Source: Volpe Ch 9. Phase 4.*
55. **Drug supply chain hash-chain** — combat counterfeit medicines (major SSA problem). Lightweight blockchain for pharmacy stock provenance. *Source: Rivas Ch 9. Phase 4.*
56. **SDoH screening (PRAPARE tool)** embedded in patient intake — social determinants account for 40% of health outcomes. *Source: Volpe Ch 24. Phase 3.*
57. **Patient Activation Measure (PAM)** scoring in patient portal — gamification hooks for engagement. *Source: Volpe Ch 2. Phase 3.*
58. **India market entry** — fragmented national landscape, no entrenched competitor. Support HL7 v2.5, CDA, DICOM. *Source: Sinha Ch 25. Phase 4.*

## Literature Sources

| Book | Author(s) | Year |
|---|---|---|
| Health Informatics: A Systems Perspective | Brown et al. | 2014 |
| Health Informatics: Multidisciplinary Approaches | Volpe | 2022 |
| Digital Health | Rivas & Boillat | 2023 |
| Practitioner's Guide to Health Informatics in Australia | Rowlands | 2017 |
| Guide to Health Informatics | Coiera | 2015 |
| Pediatric Informatics | Lehmann, Kim & Johnson | 2009 |
| EHR Manual for Developing Countries | WHO | 2006 |
| Introduction to Nursing Informatics | Hussey & Kennedy | 2021 |
| EHR Standards, Coding Systems, Frameworks | Sinha et al. | 2013 |

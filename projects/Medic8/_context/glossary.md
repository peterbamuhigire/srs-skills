# Medic8 Glossary

Healthcare and project terminology defined per IEEE 610.12-1990 format. All terms are listed alphabetically. Each entry follows the pattern: **TERM** -- Definition. *(Source/Standard)*

---

## A

**ABAC** -- Attribute-Based Access Control. Access control model where permissions are granted based on attributes of the user, resource, and environment, supplementing RBAC for fine-grained clinical data access. *(NIST SP 800-162)*

**AI Administrator** -- A facility-level role in Medic8 that manages the AI Intelligence module: configures per-tenant AI provider selection, stores encrypted API keys, monitors token usage, and processes credit pack top-ups via the admin panel. The AI Administrator cannot access clinical records, billing, or HR/payroll.

**AI Claim Scrubbing** -- An AI Intelligence module capability that predicts the rejection probability for each line item of an insurance claim before submission, using a model trained on the facility's historical claim-rejection data. The billing clerk reviews flagged items and may correct them before submitting the claim.

**AI Clinical Documentation** -- An AI Intelligence module capability that drafts SOAP notes, discharge summaries, and referral letters from structured encounter data. The clinician reviews and must explicitly approve the draft before it is saved to the patient record. Auto-save of AI-generated text is prohibited.

**AI Differential Diagnosis** -- An AI Intelligence module capability that surfaces a ranked differential diagnosis list from the patient's symptoms, vitals, and recent lab results at the point of care. Presented as a clinical prompt; clinician can dismiss individual suggestions. No suggestion is written to the patient record without explicit clinician selection.

**AI ICD Coding Assist** -- An AI Intelligence module capability that suggests ICD-10 or ICD-11 codes from free-text clinical notes using natural language understanding, reducing the need for dedicated coding staff at smaller facilities.

**AI Intelligence Module** -- Module 32 of Medic8. A tenant-toggleable, tier-independent add-on comprising six AI capabilities: AI Clinical Documentation, AI ICD Coding Assist, AI Differential Diagnosis, AI Patient Plain-Language Summary, AI Claim Scrubbing, and AI Outbreak Early Warning. Available on a credit-pack or flat-fee basis.

**AI Outbreak Early Warning** -- An AI Intelligence module capability that detects anomalous clustering of diagnosis codes at the facility level before the IDSR national threshold is crossed, and alerts the medical officer with the implicated disease codes and patient volume.

**AI Patient Plain-Language Summary** -- An AI Intelligence module capability that translates a clinician-approved clinical discharge note into a plain-language summary in the patient's preferred locale (`en`, `fr`, or `sw`) for display in the patient portal app.

**AIProviderInterface** -- The internal PHP interface contract implemented by all AI provider adapter classes in Medic8. Exposes three methods — `complete()`, `chat()`, `embed()` — with identical signatures across all adapters. Per-tenant provider selection requires no code change.

**ANC** -- Antenatal Care. Routine health care provided to pregnant women from conception to the onset of labour.

**AnthropicAdapter** -- A concrete implementation of `AIProviderInterface` that routes AI requests to the Anthropic API. Supports Claude Sonnet and Claude Haiku model variants.

**APGAR** -- Appearance, Pulse, Grimace, Activity, Respiration. Scoring system to assess newborn health at 1 and 5 minutes after birth. Range 0-10.

**ART** -- Antiretroviral Therapy. Combination of antiretroviral drugs used to treat HIV infection.

**ARV** -- Antiretroviral. A class of drugs used to treat retroviral infections, primarily HIV.

**ASTM E1394** -- Standard specification for transferring information between clinical laboratory instruments and computer systems. *(ASTM International)*

**ATC** -- Anatomical Therapeutic Chemical classification. WHO system for classifying drugs. *(WHO Collaborating Centre for Drug Statistics Methodology)*

## B

**BCMA** -- Barcode Medication Administration. System using barcode scanning to verify patient identity and medication before administration.

## C

**C-HOBIC** -- Canadian Health Outcomes for Better Information and Care. Standardised minimum nursing dataset. *(Canadian Nurses Association)*

**Credit Pack** -- A billing model for the Medic8 AI Intelligence module in which a facility purchases a token-denominated bundle. AI features consume tokens per request and pause automatically when the balance reaches zero. Clinical features are unaffected by credit exhaustion.

**CDA** -- Clinical Document Architecture. HL7 standard for clinical document exchange using XML. *(HL7 International)*

**CDS** -- Clinical Decision Support. Computer-based system providing clinicians with patient-specific assessments or recommendations.

**CHW** -- Community Health Worker. A trained health worker who serves communities outside formal healthcare facilities.

**CMAM** -- Community-based Management of Acute Malnutrition. Programme for treating SAM and MAM in community settings. *(WHO/UNICEF)*

**CPHL** -- Central Public Health Laboratories. Uganda's national reference laboratory in Butabika. *(Uganda Ministry of Health)*

**CPOE** -- Computerised Physician Order Entry. Electronic system for entering medical orders.

## D

**DAMA** -- Discharge Against Medical Advice. Patient leaves hospital against medical recommendation.

**DeepSeekAdapter** -- A concrete implementation of `AIProviderInterface` that routes AI requests to the DeepSeek API. Supports DeepSeek-V3 and DeepSeek-R1 model variants.

**DHIS2** -- District Health Information Software 2. Web-based open-source health management platform used by Uganda MoH. *(University of Oslo / HISP)*

**DICOM** -- Digital Imaging and Communications in Medicine. International standard for medical imaging. *(NEMA)*

**DOT** -- Directly Observed Treatment. TB treatment strategy where a healthcare worker observes the patient taking medication. *(WHO)*

**DRG** -- Diagnosis Related Group. Classification system grouping patients by diagnosis for billing purposes.

## E

**EDD** -- Expected Date of Delivery. Estimated due date for childbirth.

**EMPI** -- Enterprise Master Patient Index. System maintaining a unique identifier for each patient across facilities.

**EmONC** -- Emergency Obstetric and Newborn Care. Set of life-saving clinical interventions for obstetric emergencies. *(WHO)*

**EPI** -- Expanded Programme on Immunisation. WHO programme for universal childhood vaccination. *(WHO)*

**EWS** -- Early Warning Score. Composite score from vital signs predicting clinical deterioration.

## F

**FHIR** -- Fast Healthcare Interoperability Resources. HL7 standard for electronic health information exchange using RESTful APIs. *(HL7 International)*

**FMEA** -- Failure Mode and Effects Analysis. Systematic method for evaluating potential failure modes in a process. *(IEC 60812)*

## G

**GeminiAdapter** -- A concrete implementation of `AIProviderInterface` that routes AI requests to the Google Gemini API. Supports Gemini 1.5 Pro and Gemini 1.5 Flash model variants.

**GRN** -- Goods Received Note. Document recording receipt of goods into inventory.

## H

**HL7** -- Health Level Seven International. Organisation producing standards for health information exchange. *(HL7 International)*

**HMIS** -- Health Management Information System. Uganda MoH system for collecting and reporting health facility data. *(Uganda Ministry of Health)*

## I

**I18N-GAP** -- A build-log flag emitted when a localisation key exists in the primary language (`en`) but is absent from one or more required locales (`fr`, `sw`). An unresolved `[I18N-GAP]` tag is a release blocker for the `release` branch.

**i18n** -- Internationalisation. The architectural practice of designing software so that all user-facing strings are externalised into locale-specific resource files, enabling the UI to render in multiple languages without code changes. Derived from the word "internationalisation" (18 letters between the first "i" and the last "n").

**ICD-10** -- International Classification of Diseases, 10th Revision. WHO standard for coding diagnoses. *(WHO)*

**ICD-11** -- International Classification of Diseases, 11th Revision. Latest WHO classification system. *(WHO)*

**IDSR** -- Integrated Disease Surveillance and Response. WHO/Africa strategy for disease surveillance. *(WHO AFRO)*

## K

**Kiswahili** -- A Bantu language spoken by approximately 200 million people across East and Central Africa, with official status in Kenya, Tanzania, Uganda, and DRC. Designated as a launch language for the Medic8 platform (`sw` locale code). Clinical terminology translation requires review by a native-speaker clinician.

## L

**LASA** -- Look-Alike/Sound-Alike. Drugs with similar names that risk confusion during prescribing or dispensing. *(WHO/ISMP)*

**Locale Fallback Chain** -- The ordered sequence in which the Medic8 i18n system resolves a missing localisation string. For Kiswahili: `sw → en`. For French: `fr → en`. A missing string never falls through to machine translation.

**LMIS** -- Logistics Management Information System. System for managing supply chain data for health commodities.

**LOINC** -- Logical Observation Identifiers Names and Codes. Universal standard for identifying medical laboratory observations. *(Regenstrief Institute)*

**LPO** -- Local Purchase Order. Document authorising purchase of goods from a supplier.

## M

**MAM** -- Moderate Acute Malnutrition. Nutritional condition defined by WHZ between -3 and -2 SD. *(WHO)*

**MAR** -- Medication Administration Record. Document recording each dose of medication given to a patient.

**MER** -- Monitoring, Evaluation, and Reporting. PEPFAR's indicator framework for HIV programme performance. *(PEPFAR)*

**MPI** -- Master Patient Index. See EMPI.

**mRDT** -- Malaria Rapid Diagnostic Test. Point-of-care test for malaria parasites. *(WHO)*

**MUAC** -- Mid-Upper Arm Circumference. Anthropometric measure for nutritional screening, especially in children. *(WHO)*

## N

**NANDA-I** -- NANDA International. Organisation maintaining a standardised taxonomy of nursing diagnoses. *(NANDA International)*

**NEWS2** -- National Early Warning Score 2. Standardised system for assessing acute illness severity. *(Royal College of Physicians)*

**NHIS** -- National Health Insurance Scheme. Uganda's mandatory contributory health insurance programme (launched 2023). *(Government of Uganda)*

**NIC** -- Nursing Interventions Classification. Standardised taxonomy of nursing interventions. *(University of Iowa)*

**NIRA** -- National Identification and Registration Authority. Uganda's national ID body. *(Government of Uganda)*

**NMS** -- National Medical Stores. Uganda government agency supplying medicines to public health facilities. *(Government of Uganda)*

**NOC** -- Nursing Outcomes Classification. Standardised taxonomy of nursing-sensitive patient outcomes. *(University of Iowa)*

**NSO** -- Nursing Sensitive Outcome. Patient outcome directly influenced by nursing care quality.

**NTLP** -- National TB and Leprosy Programme. Uganda MoH programme for TB management. *(Uganda Ministry of Health)*

## O

**OpenAIAdapter** -- A concrete implementation of `AIProviderInterface` that routes AI requests to the OpenAI API. Supports GPT-4o and GPT-4o-mini model variants.

## P

**PDPA** -- Data Protection and Privacy Act 2019. Uganda's primary data protection legislation. *(Government of Uganda)*

**Plain-Language Summary** -- A patient-facing document generated by the AI Patient Plain-Language Summary capability that translates a clinician-approved clinical discharge note into a plain-language version in the patient's preferred locale (`en`, `fr`, or `sw`), calibrated to a reading level appropriate for the target language community.

**PEPFAR** -- President's Emergency Plan for AIDS Relief. US government programme funding HIV/AIDS responses globally. *(US Government)*

**PHLB** -- Pharmacy and Laboratory Board. Uganda's regulatory body for pharmacy and laboratory professionals (now Allied Health Professionals Council). *(Government of Uganda)*

**PIF** -- Project Input Folder. The `_context/` directory containing all project-specific inputs for SRS generation. *(SRS-Skills PRIME methodology)*

**PKI** -- Public Key Infrastructure. Framework for managing digital certificates and encryption keys.

**PMTCT** -- Prevention of Mother to Child Transmission. Programme preventing HIV transmission from mother to child. *(WHO)*

**PRIME** -- Prepare, Relay, Inspect, Modify, Execute. Methodology for AI-assisted document generation. *(Kodukula & Vinueza, 2024)*

## R

**RBAC** -- Role-Based Access Control. Access control model where permissions are assigned to roles, not individual users. *(NIST)*

**RUTF** -- Ready to Use Therapeutic Food. Nutrient-dense paste for treating SAM without hospitalisation. *(WHO/UNICEF)*

**RxNorm** -- Standardised nomenclature for clinical drugs. *(US National Library of Medicine)*

## S

**SAM** -- Severe Acute Malnutrition. Nutritional condition defined by WHZ below -3 SD or MUAC below 115 mm. *(WHO)*

**SDoH** -- Social Determinants of Health. Non-medical factors influencing health outcomes (housing, food security, education). *(WHO)*

**SMART on FHIR** -- Substitutable Medical Applications and Reusable Technologies on FHIR. Standard for launching third-party apps within EHR systems. *(Boston Children's Hospital / HL7)*

**SNOMED CT** -- Systematised Nomenclature of Medicine Clinical Terms. Comprehensive clinical terminology system. *(SNOMED International)*

**SOAP** -- Subjective, Objective, Assessment, Plan. Standard format for clinical progress notes.

**sw** -- The ISO 639-1 locale code for Kiswahili. Used in Medic8 as the key for Kiswahili localisation resources across Laravel (`lang/sw/`), Android (`values-sw/`), and iOS (`sw.lproj/`). Falls back to `en` when a string key is absent.

## U

**UBTS** -- Uganda Blood Transfusion Service. National agency managing blood supply. *(Uganda Ministry of Health)*

**UMDPC** -- Uganda Medical and Dental Practitioners Council. Regulatory body for doctors and dentists. *(Government of Uganda)*

**UNMC** -- Uganda Nurses and Midwives Council. Regulatory body for nurses and midwives. *(Government of Uganda)*

## V

**VHT** -- Village Health Team. Community health workers in Uganda's primary healthcare system (168,000+ nationally). *(Uganda Ministry of Health)*

## W

**WHZ** -- Weight-for-Height Z-score. Anthropometric indicator for acute malnutrition in children. *(WHO)*

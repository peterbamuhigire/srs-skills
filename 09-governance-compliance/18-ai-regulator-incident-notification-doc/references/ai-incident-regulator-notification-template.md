# AI Incident Regulator Notification Template

For serious AI incidents that meet a regulator's reporting threshold. Use the matching jurisdiction block; multiple may apply simultaneously.

The template covers the four primary regulator regimes the agency works in: **EU AI Act Art. 73 (high-risk systems)**, **GDPR Art. 33 (data breaches)**, **African DPA regimes (Kenya ODPC, Nigeria NDPR via NDPC, South Africa POPIA via Information Regulator, Uganda PDPO via NITA-U / PDPO, Rwanda NCSA)**, **sectoral regulators where applicable (financial services, healthcare)**.

---

## Decision matrix — when to notify which regulator

| Trigger | EU AI Act Art. 73 | GDPR Art. 33 | African DPA | Sectoral regulator |
|---|:-:|:-:|:-:|:-:|
| Serious incident in EU high-risk AI system | ✓ within 15 days (immediate for widespread infringement; 10 days for fatality / serious harm) |  |  | If applicable |
| Personal-data exposure (any source) involving EU subjects |  | ✓ within 72 h |  | If applicable |
| Personal-data exposure involving Kenya subjects |  |  | ✓ within 72 h to ODPC | If applicable |
| Personal-data exposure involving Nigeria subjects |  |  | ✓ within 72 h to NDPC | If applicable |
| Personal-data exposure involving South Africa subjects |  |  | ✓ "as soon as reasonably possible" to IR | If applicable |
| Personal-data exposure involving Uganda subjects |  |  | ✓ within 24 h to PDPO | If applicable |
| Personal-data exposure involving Rwanda subjects |  |  | ✓ within 48 h to NCSA | If applicable |
| Financial-services AI-incident (any jurisdiction) | If applicable | If applicable | If applicable | ✓ per sectoral regulator clock |
| Healthcare AI-incident |  | If applicable | If applicable | ✓ per sectoral regulator clock |

Always treat the **shortest applicable clock** as the binding clock.

---

## Common notification fields (all jurisdictions)

1. **Notifier identity.** Legal entity, registration, point of contact (name, role, phone, email — both technical and legal-DPO).
2. **System identity.** AI system name, version, intended use, deployment context, customer tenants affected (numbered, not named in the public version).
3. **Incident identity.** Internal incident ID, severity, declared time, first-detection time, mitigation time, resolution time (or "ongoing").
4. **Incident description.** Plain-language description of what happened, then the technical RCA classification (see `ai-rca-taxonomy-reference.md`). Be precise: was the incident a hallucination event, a prompt-injection event, a retrieval-drift event, a cross-tenant data bleed, an agent-action incident, a foundation-model regression, an eval drift, a cost incident affecting customer service?
5. **Scope of impact.** Number of affected tenants, number of affected data subjects, geography, sectors. Whether personal data was involved, and if so what categories (basic, special category under GDPR Art. 9, financial, health, biometric, minor).
6. **Likely consequences.** What can affected subjects/customers expect; what risk exists.
7. **Mitigation already taken.** Concrete actions: kill-switch, rollback, model-pin, prompt-pin, retrieval re-index, action-gate tightening, notification to affected customers, etc.
8. **Mitigation planned.** With dates.
9. **Evidence preserved.** Reference to the evidence-pack ID (per `ai-incident-evidence-pack-spec-template.md`) available for inspection.
10. **Sub-processors involved.** Named, with their contact details.
11. **Contact for follow-up.** DPO + technical incident commander + general counsel (or external counsel).

---

## EU AI Act Art. 73 — Serious Incident Notification

**Recipient.** Market surveillance authority of the Member State(s) where the incident occurred.
**Clock.**
- Widespread infringement: **immediate**, not later than 15 days after awareness.
- Death or serious health damage: not later than **10 days**.
- Disruption of critical infrastructure: not later than **2 days**.
- Other serious incidents: not later than **15 days**.

**Template body**

> **Notification of Serious Incident under Article 73 of the EU AI Act (Regulation (EU) 2024/1689)**
>
> 1. **Provider.** `[Legal name, registered office, AI provider registration ID]`. Point of contact: `[name, title, phone, email]`.
> 2. **High-risk AI system.** `[System name]`, version `[version]`, intended purpose `[intended use, mapped to Annex III category]`, EU declaration of conformity `[ref]`.
> 3. **Deployer(s) affected.** `[List, including each deployer's contact]`.
> 4. **Incident overview.** On `[date]` at `[time]` UTC, a serious incident occurred in the deployment of `[system]`. The incident is classified as `[category — Art. 3(49)(a) / (b) / (c) / (d)]`.
> 5. **Description.** `[Plain-language description, 200-400 words]`.
> 6. **Technical root cause.** `[RCA class per AI RCA Taxonomy: model / retrieval / tool-agent / eval / data / infra / commercial]`. Specifically: `[detail]`.
> 7. **Affected fundamental rights or safety.** `[which rights / which safety domain]`.
> 8. **Number of affected persons.** `[N]`, broken down by `[Member State / category]`.
> 9. **Mitigation taken.** `[concrete list]`.
> 10. **Mitigation planned.** `[concrete list with dates]`.
> 11. **Evidence pack.** Available at `[secure URL or "on request"]`, evidence ID `[ID]`. Chain of custody documented per our internal procedure.
> 12. **Sub-processors involved.** `[list]`.
> 13. **Conformity reassessment.** `[Whether the conformity assessment will be re-run; planned dates]`.
> 14. **Updates.** Next update will be provided no later than `[date]`.
>
> Signed, `[name, title, on behalf of provider]`, `[date]`.

---

## GDPR Art. 33 — Personal Data Breach Notification

**Recipient.** Lead supervisory authority + any concerned supervisory authorities.
**Clock.** **72 hours** from awareness (later notification permitted with reasons).
**Format.** Each supervisory authority publishes its own form — use that form. The body below is the universal content.

**Template body**

> **Notification of personal data breach under Article 33 GDPR**
>
> 1. **Controller / Processor.** `[role, legal name, DPO contact, lead supervisory authority]`.
> 2. **Nature of breach.** `[confidentiality / integrity / availability]` — for AI incidents most often confidentiality (leakage) or integrity (model-generated bad data overwriting source).
> 3. **Description.** `[plain language, 100-300 words, including the AI-specific cause: hallucination causing third-party publication, retrieval drift causing wrong-customer answer, agent action incident causing data alteration, etc.]`.
> 4. **Categories of data subjects.** `[customers / employees / minors / patients / etc.]` and approximate number.
> 5. **Categories of personal data.** `[basic / special / financial / health / biometric]` and approximate number of records.
> 6. **Likely consequences for data subjects.** `[concrete assessment]`.
> 7. **Measures taken or proposed.** `[concrete list, mitigation and remediation]`.
> 8. **Cross-border element.** `[whether subjects in other Member States affected]`.
> 9. **Communication to data subjects.** Whether and when, per Art. 34.
> 10. **Contact.** DPO.

---

## African DPA notifications (variations)

**Kenya ODPC** (Data Protection Act 2019, s. 43): notify within 72 h. Form via ODPC online portal. Same content as GDPR Art. 33.

**Nigeria NDPC** (NDPA 2023, s. 40): notify within 72 h. NDPC-prescribed form. Add: information on whether data subjects in Nigeria are minors, vulnerable, or persons of public interest.

**South Africa Information Regulator** (POPIA s. 22): notify "as soon as reasonably possible" — interpret as 72 h to align with GDPR. Form via Information Regulator. Add: whether subjects are children.

**Uganda PDPO via NITA-U** (Data Protection and Privacy Act 2019): notify within 24 h. Same content base.

**Rwanda NCSA** (Law N° 058/2021): notify within 48 h.

For each African DPA, include a one-paragraph translation of the technical RCA into plain language adapted for the regulator (regulators in this region are still building AI expertise; clarity helps).

---

## Sectoral overlays

**Financial services** (CBN / CMA / NDIC / SARB / FRA / CMA Kenya): notify per the sectoral SLA, usually shorter than 72 h. Add: financial-impact estimate and customer-recompense plan.

**Healthcare** (relevant ministry of health + medical-device regulator if applicable): include patient-impact assessment, clinician-in-the-loop status at time of incident, clinical-safety officer review.

---

## Internal sign-off chain

Before any external regulator notification leaves the building:

1. DPO sign-off (mandatory).
2. General counsel sign-off (mandatory).
3. CISO sign-off (mandatory).
4. CTO or designate sign-off for technical accuracy (mandatory).
5. CEO or designate sign-off for SEV-1 / fatal-impact incidents (mandatory).
6. Public-comms team aware (mandatory, even if no external press release planned).

Record the sign-off chain in the evidence pack.

## Hold and update obligations

Notifications are commitments. Once a regulator is notified, the company is on the clock for updates. Follow the regulator's prescribed update cadence; default to weekly updates until incident is closed.

## Anti-patterns

- Notifying late because "we wanted to be sure of the cause." The clock starts at awareness of a notifiable incident, not at RCA close.
- Notifying selectively across jurisdictions. If a multi-jurisdictional incident occurs, notify all applicable regulators within their respective clocks.
- Using customer-comms language in regulator notifications. Regulators expect technical precision.
- Omitting the AI-specific RCA classification. Generic "data exposure" language obscures the AI nature; regulators are watching for this.
- Failing to specify sub-processors (model providers). Article 28 / equivalent local processor language requires this.

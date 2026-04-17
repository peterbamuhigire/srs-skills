# NITA-U SaaS Compliance Obligations

## 9.1 Regulatory Body

The National Information Technology Authority — Uganda (NITA-U) is the statutory body responsible for regulating information technology services in Uganda under the National Information Technology Authority Act 2009. NITA-U has issued guidance applicable to SaaS cloud service providers operating in or serving organisations in Uganda.

## 9.2 Compliance Status

*[CONTEXT-GAP: GAP-014] — A legal review of NITA-U SaaS cloud provider obligations under Uganda's ICT regulatory framework is required before production launch. This review shall confirm the obligations listed in Section 9.3, identify any additional obligations not currently captured, and determine the applicability of each obligation to Chwezi Core Systems as the platform operator. This section shall be updated to reflect confirmed obligations once GAP-014 is resolved. No production deployment shall be treated as NITA-U compliant until this review is completed and documented.*

## 9.3 Known Obligations (Provisional)

The following obligations are known at the time of writing, based on publicly available NITA-U guidance. They are provisional until confirmed by the legal review required under GAP-014.

### 9.3.1 Data Localisation

NITA-U guidance indicates a preference for government and public-sector data to be hosted on Uganda-based infrastructure. For private-sector tenants, the data localisation requirements under current NITA-U guidance are subject to legal confirmation. The data residency decision required by GAP-007 (Section 6.4) shall be made in conjunction with this obligation.

### 9.3.2 Security Incident Reporting

Cloud SaaS providers may be required to report material security incidents to NITA-U within a defined timeframe. The specific reporting timeline and the definition of "material incident" are subject to confirmation by the GAP-014 legal review. Longhorn ERP's incident response runbook shall include a NITA-U reporting step once the obligation is confirmed.

### 9.3.3 Compliance Certification

NITA-U may require SaaS providers to obtain or maintain specific certifications. The ISO/IEC 27001:2022 information security management system certification targeted by Longhorn ERP (Section 1.3) may satisfy or contribute to this requirement. Confirmation is required as part of GAP-014.

### 9.3.4 Data Processing Agreements

NITA-U guidance may require documented data processing agreements between Chwezi Core Systems (as processor) and tenant organisations (as controllers) for data subject to Ugandan law. The Tenant Service Agreement shall include PDPA-compliant data processing clauses. Whether NITA-U prescribes additional terms is subject to confirmation.

## 9.4 Action Required Before Production

The following actions shall be completed before the platform is marketed to Ugandan organisations as NITA-U-compliant:

1. Commission the legal review specified in GAP-014.
2. Update this section with confirmed obligations and their implementation status.
3. Update the Tenant Service Agreement to reflect confirmed NITA-U data processing terms.
4. Add NITA-U incident reporting steps to the deployment runbook.
5. Record the completed review in the pre-launch compliance checklist (Section 10).

*This section is flagged for mandatory update. Do not represent Longhorn ERP as NITA-U compliant until GAP-014 is resolved and this section is updated.*

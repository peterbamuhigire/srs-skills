# Leads Management

## 2.1 Lead Capture

**FR-CRM-001** — When a user creates a lead record, the system shall capture: lead source (configurable: website form, referral, trade show, cold call, social media), company name (optional), contact name, phone number, email, country, estimated deal value, and an initial notes field.

**FR-CRM-002** — The system shall support bulk lead import from a CSV file; the import shall validate mandatory fields (contact name, phone or email), report duplicate detection (matching phone or email against existing leads and contacts), and create a summary of imported, skipped, and failed rows.

**FR-CRM-003** — The system shall assign a unique lead ID in the format `LEAD-YYYY-NNNN` and record the creating user (lead owner), creation timestamp, and tenant ID.

## 2.2 Lead Qualification

**FR-CRM-004** — When a user qualifies a lead, the system shall prompt the user to confirm: identified product/service interest, estimated annual value, decision-maker name, and expected decision timeline; on confirmation, the system shall convert the lead to an opportunity and archive the lead record.

**FR-CRM-005** — When a lead is disqualified, the system shall require a disqualification reason (configurable: wrong contact, no budget, competitor already contracted, no response after N attempts); the disqualified lead shall be retained in read-only state for reporting.

## 2.3 Lead Assignment and Routing

**FR-CRM-006** — The system shall support automatic lead assignment based on territory rules: when a new lead's country or region matches a configured territory, the system shall assign the lead to the territory's designated sales representative.

**FR-CRM-007** — When a lead remains uncontacted for more than the configured follow-up threshold (default: 48 hours), the system shall send an alert to the lead owner and their direct manager.

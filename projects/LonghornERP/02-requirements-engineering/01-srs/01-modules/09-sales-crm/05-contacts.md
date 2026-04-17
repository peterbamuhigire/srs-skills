# Contact Management

## 5.1 Contact Records

**FR-CRM-022** — When a user creates a contact record, the system shall capture: first name, last name, job title, company name, direct phone number, mobile number, email address, country, and linked customer account (if the contact is associated with an existing Longhorn ERP customer).

**FR-CRM-023** — The system shall enforce that no two contacts share the same email address within a tenant; a duplicate email address shall be rejected with a descriptive error message displaying the existing contact's name and the duplicate email.

**FR-CRM-024** — The system shall allow a contact to be linked to multiple opportunities and multiple companies (e.g., a consultant who represents more than one client); these associations shall be bidirectional, so the contact appears in the related records of each linked opportunity and company.

## 5.2 Contact Deduplication

**FR-CRM-025** — The system shall perform a fuzzy duplicate check when a new contact is created by matching on: name similarity (≥ 85% match using Levenshtein distance), phone number (exact), and email (exact); when a probable duplicate is detected, the system shall present the potential duplicate to the user and require confirmation before creating the new record.

## 5.3 Contact Communication Preferences

**FR-CRM-026** — The system shall store communication preference flags per contact: opt-in to email marketing, opt-in to SMS marketing, preferred contact time (business hours, evenings, weekends), and preferred communication channel (call, email, WhatsApp); these preferences shall be respected in automated campaign targeting.

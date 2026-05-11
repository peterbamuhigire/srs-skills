# 07-SaaS-Tenant-Lifecycle-Runbook Skill

## Objective

Produce the operational runbook covering provisioning, tier change, suspension, reactivation, offboarding, customer-initiated data export, hard delete, and retention. Each stage has automated steps, manual gates, verification, audit-trail, customer-comms, and retention reference.

## Execution Steps

1. Verify `Multi_Tenancy_Architecture_Spec.md`, `Runbook.md`, and `Compliance_Docs.md` exist.
2. Invoke `logic.prompt`.
3. Review with privacy officer and SRE lead — every stage must have audit and customer-comms.
4. Cross-link the hard-delete verification query to the Data Isolation Evidence Pack.

## Quality Reminder

Hard-delete is not "issue DELETE". It is a verified destruction across every data store, with a signed certificate, retained for 5-7 years, gated by legal-hold check.

## Standards

- SRE Best Practices
- GDPR Art.17 / Art.20
- POPIA s.14 / s.23
- DPPA 2019

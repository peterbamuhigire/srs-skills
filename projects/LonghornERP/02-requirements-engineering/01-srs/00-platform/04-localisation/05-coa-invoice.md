## 5. Chart of Accounts, Invoice Legal Text, PPDA Workflow, and Address Format

### 5.1 Chart of Accounts Starter Template

**FR-LOC-080:** The system shall load the Chart of Accounts (COA) starter template identified by the `coa_starter_template` field of the assigned localisation profile into the tenant's `accounts` table when a new tenant is provisioned.

**FR-LOC-081:** The system shall source COA starter templates from the `coa_templates` table, where each template record contains the account code, account name, account type, and normal balance for every account in the template, when a provisioning event is triggered.

**FR-LOC-082:** The system shall allow an authorised tenant-level admin to add, rename, or deactivate individual accounts in the tenant's COA after provisioning, without modifying the underlying starter template or affecting other tenants, when the admin submits a COA modification request.

*Example profile values:*

| Profile | `coa_starter_template` | Accounting Framework |
|---|---|---|
| Uganda Phase 1 | `UGANDA_IFRS` | IFRS — East Africa standard account structure. |
| Kenya Phase 2 | `KENYA_IFRS` | IFRS — Kenya-specific account numbering conventions. |
| Tanzania Phase 2 | `TANZANIA_IFRS` | IFRS. |
| Rwanda Phase 2 | `RWANDA_IFRS` | IFRS. |
| Francophone Phase 3 | `OHADA_SYSCOHADA_2017` | OHADA SYSCOHADA 2017. `[CONTEXT-GAP: GAP-010]` |

`[CONTEXT-GAP: GAP-010]` — The official OHADA SYSCOHADA 2017 Chart of Accounts must be obtained before the `OHADA_SYSCOHADA_2017` template can be populated. This is a Phase 3 prerequisite.

### 5.2 Invoice Legal Text

**FR-LOC-083:** The system shall append the text stored in the `invoice_legal_text` field of the tenant's active localisation profile as a footer on every generated tax invoice and credit note, when the `invoice_legal_text` field is non-null.

**FR-LOC-084:** The system shall render the `invoice_legal_text` value without modification, preserving line breaks encoded in the field, when the invoice PDF or printed document is generated.

*Example profile values:*

| Profile | Example `invoice_legal_text` |
|---|---|
| Uganda Phase 1 | "This is a tax invoice issued in compliance with the Value Added Tax Act, Cap 349, Uganda. VAT Registration No: [TENANT_VAT_NO]. Any queries: [TENANT_EMAIL]." |
| Kenya Phase 2 | "Tax Invoice issued under the Kenya Revenue Authority eTIMS framework. PIN: [TENANT_PIN]. VAT No: [TENANT_VAT_NO]." |

*Note:* Placeholders such as `[TENANT_VAT_NO]` are resolved at render time from the tenant's registration record. The legal text template is stored in the profile; the tenant-specific values are stored in the tenant record.

### 5.3 PPDA Procurement Workflow Activation

**FR-LOC-085:** The system shall activate the Public Procurement and Disposal of Public Assets Authority (PPDA) procurement approval workflow for a tenant when the `ppda_workflow_enabled` field in the tenant's active localisation profile is set to `true`.

**FR-LOC-086:** The system shall enforce procurement approval thresholds and open-tendering requirements according to the threshold values stored in the tenant's PPDA configuration record, when the PPDA workflow is active per **FR-LOC-085**.

**FR-LOC-087:** The system shall bypass PPDA workflow enforcement when `ppda_workflow_enabled` is `false` in the tenant's active localisation profile, applying only the standard three-level purchase order approval workflow.

`[CONTEXT-GAP: GAP-006]` — Current micro, small, and large procurement thresholds under the PPDA Act must be verified from the PPDA Uganda website before the PPDA configuration record is populated. Threshold values are stored in the tenant PPDA configuration, not in the localisation profile, so that they can be updated without a profile version change.

### 5.4 Address Format Configuration

**FR-LOC-088:** The system shall render physical address fields in the order and with the labels defined in the `address_format_json` field of the tenant's active localisation profile, when displaying or printing an address in the user interface, a document, or a report.

**FR-LOC-089:** The system shall use the `address_format_json` definition to render both entry forms and read-only address displays, ensuring the field sequence and label text are consistent between data entry and output, when address data is collected or displayed.

The `address_format_json` structure shall conform to:

```json
[
  {"field": "street_line_1", "label": "Plot / Street"},
  {"field": "street_line_2", "label": "Area / Division"},
  {"field": "city",          "label": "Town / City"},
  {"field": "district",      "label": "District"},
  {"field": "country",       "label": "Country"}
]
```

*Example profile values:*

| Profile | Address Field Order |
|---|---|
| Uganda Phase 1 | Plot/Street, Area/Division, Town, District, Country. |
| Kenya Phase 2 | Building/Street, Estate/Area, Town, County, Country. |
| Francophone Phase 3 | Rue/Numéro, Quartier, Ville, Province/Région, Pays. |

**FR-LOC-090:** The system shall validate that any address format defined in `address_format_json` contains at minimum the fields `city` and `country`, and shall reject profile creation or update if these fields are absent, when the profile record is saved.

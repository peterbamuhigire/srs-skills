## 4. Access and Search Requirements

### 4.1 Role-Based Access Control for Audit Log

**FR-AUDIT-050:** The system shall restrict audit log read access to users assigned the `auditor`, `admin`, or `super_admin` role. Users assigned any other role shall receive no access to audit log data via any interface.

*Test oracle: Log in as a user with only the `cashier` role. Attempt to navigate to the audit log interface. Verify the system returns a permission denied response and renders no audit data.*

**FR-AUDIT-051:** The system shall provide an `external_auditor` role whose permissions are limited exclusively to audit log search and audit log export. Users assigned the `external_auditor` role shall have no `INSERT`, `UPDATE`, or `DELETE` privilege on any application table, including `audit_log`.

*Test oracle: Assign the `external_auditor` role to a test user. Verify the user can access the audit log search interface and download an export. Attempt to access any non-audit-log page (e.g., invoices, stock). Verify permission denied is returned for all non-audit pages.*

**FR-AUDIT-052:** The system shall enforce tenant data isolation on the audit log: a tenant-level user (including an `external_auditor`) shall only retrieve audit records belonging to their own `tenant_id`. Super admins may query across tenants with explicit tenant selection.

*Test oracle: Log in as an `external_auditor` for Tenant A. Submit an audit log search with no additional filters. Verify all returned records have `tenant_id` equal to Tenant A's ID. Verify no records from Tenant B appear.*

### 4.2 Audit Log Search Interface

**FR-AUDIT-053:** The system shall provide an audit log search interface that allows filtering by: date range (start date, end date), module, user (by `user_id` or `user_name`), action type, `affected_table`, and `affected_record_id`.

*Test oracle: Apply a filter for `module = "Procurement"`, `action = "APPROVE"`, and a 30-day date range. Verify all returned records satisfy all 3 filter criteria simultaneously. Verify records from other modules or with other action types are excluded.*

**FR-AUDIT-054:** The system shall allow all filter parameters in the audit log search interface to be applied independently or in any combination. No filter shall be mandatory.

*Test oracle: Submit a search with only the `user` filter populated and all other filters blank. Verify the system returns results matching only the `user` filter. Submit a search with all filters blank. Verify the system returns all records within the default date range.*

**FR-AUDIT-055:** The system shall default the audit log search date range to the most recent 30 days when no date filter is specified by the user.

*Test oracle: Open the audit log search interface without selecting any date filter. Submit the search. Verify the result set contains only records with `timestamp` falling within the last 30 days.*

**FR-AUDIT-056:** The system shall display the following columns in the audit log search results table: `timestamp` (UTC, formatted as `YYYY-MM-DD HH:MM:SS UTC`), `user_name`, `module`, `action`, `affected_table`, `affected_record_id`, and an expandable detail row showing `old_values` and `new_values` in formatted JSON.

*Test oracle: Perform a search that returns results. Verify all 7 columns are present in the results table. Click the expand control on one row. Verify `old_values` and `new_values` are rendered as formatted JSON.*

**FR-AUDIT-057:** The system shall implement server-side pagination for audit log search results and shall support page sizes of 50, 100, 500, and 1000 records per page. The default page size shall be 100 records.

*Test oracle: Perform a search known to return > 1000 records. Set page size to 1000. Verify the first page returns exactly 1000 records. Navigate to page 2. Verify the correct next set of records is returned. Verify the total record count displayed matches the actual count.*

### 4.3 Audit Log Export

**FR-AUDIT-058:** The system shall allow a user with audit log read access to export the current search result set (with all applied filters) to CSV format.

*Test oracle: Apply a filter for a specific module and date range. Click **Export CSV**. Verify the downloaded file contains only the rows matching the applied filters and includes a header row with column names.*

**FR-AUDIT-059:** The system shall allow a user with audit log read access to export the current search result set to Excel (.xlsx) format.

*Test oracle: Apply a filter. Click **Export Excel**. Verify the downloaded `.xlsx` file opens correctly in Microsoft Excel, contains the correct data, and includes a header row.*

**FR-AUDIT-060:** The system shall allow a user with audit log read access to export the current search result set to PDF format. The PDF shall include the applied filter criteria, the Longhorn ERP logo, the tenant name, and the export timestamp on the header of each page.

*Test oracle: Apply a filter. Click **Export PDF**. Verify the downloaded PDF includes the applied filter criteria in the page header, displays the tenant name, and includes the export timestamp. Verify data matches the on-screen results.*

**FR-AUDIT-061:** The system shall include all fields of each record (`tenant_id`, `user_id`, `user_name`, `module`, `action`, `affected_table`, `affected_record_id`, `old_values`, `new_values`, `ip_address`, `user_agent`, `timestamp`) in all export formats (CSV, Excel, PDF).

*Test oracle: Export a result set. Verify all 12 columns are present in the output file with accurate values matching the database records.*

**FR-AUDIT-062:** The system shall log every audit log export action as an audit record with `action = "AUDIT_EXPORT"`, capturing `user_id`, `tenant_id`, the export format, and the applied filter criteria in `new_values`.

*Test oracle: Perform an export. Verify a new audit record exists with `action = "AUDIT_EXPORT"` and `new_values` containing the export format and the filter values used.*

### 4.4 Audit Log Detail View

**FR-AUDIT-063:** The system shall provide a detail view for a single audit log record that displays all 12 fields, renders `old_values` and `new_values` as formatted JSON with syntax highlighting, and includes a **Copy Record** button that copies the full JSON representation of the record to the clipboard.

*Test oracle: Open the detail view for an UPDATE record. Verify all 12 fields are displayed. Verify `old_values` and `new_values` are rendered with JSON syntax highlighting. Click **Copy Record** and paste into a text editor. Verify valid JSON is produced.*

**FR-AUDIT-064:** The system shall provide a direct URL for each audit log record detail view, formatted as `/audit-log/{record_id}`, accessible by any user with audit log read access.

*Test oracle: Navigate to `/audit-log/{valid_record_id}` while authenticated as an `external_auditor`. Verify the detail view renders correctly. Navigate to the same URL while authenticated as a `cashier` user. Verify a permission denied response is returned.*

**FR-AUDIT-065:** The system shall display, within the audit log detail view, a hyperlink to the affected record (e.g., the invoice, purchase order, or user account) when the affected record still exists in the system. When the affected record has been deleted, the system shall display the text "Record deleted" in place of the hyperlink.

*Test oracle: View an audit record for a CREATE action on an invoice that still exists. Verify a hyperlink to the invoice is displayed. View an audit record for a CREATE action on a record that has since been deleted. Verify "Record deleted" is displayed in place of the hyperlink.*

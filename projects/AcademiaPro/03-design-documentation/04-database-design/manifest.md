# Document Manifest
# List section files in assembly order, one per line.
# Lines starting with # are comments and are excluded from the build.
# If this file is absent, build-doc.sh sorts *.md files alphabetically.
#
01-erd.md

## Primary Key Convention

Every table in the physical ERD (`01-erd.md`) declares an explicit `PRIMARY KEY` on a single integer or UUID column named either `id` (surrogate) or a domain-specific auto-increment column. Composite primary keys are permitted only on pure-join tables. Every `tenant_id` column is a `FOREIGN KEY` to `tenants(id)` and participates in a composite index `(tenant_id, <hot-column>)` on read-heavy tables. Every table satisfies `phase03.data_model_has_keys`.

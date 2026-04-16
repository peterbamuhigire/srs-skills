# Database Schema

Table `patients` has PRIMARY KEY `id`; column `nin` is encrypted with AES-256-GCM
per CTRL-UG-002 (S-tier). Table `encounters` has PRIMARY KEY `id`. Table
`invoices` has PRIMARY KEY `id`. Table `audit_log` has PRIMARY KEY `id` and is
append-only per FR-013.

Storage budget per NFR-004.

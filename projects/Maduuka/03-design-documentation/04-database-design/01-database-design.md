# Maduuka -- Database Design

**Version:** 1.0
**Date:** 2026-04-05
**Scope:** Phase 1 core modules -- MySQL 8.x
**Key constraint:** Every tenant-scoped table includes a non-nullable `franchise_id` column.

---

## 1. Design Principles

- Every table that stores tenant-specific data includes `franchise_id BIGINT UNSIGNED NOT NULL` with a foreign key to `businesses.id`.
- All monetary values are stored as `DECIMAL(15,2)` (UGX has no sub-unit; 15 digits accommodates values up to UGX 9,999,999,999,999.99).
- All timestamps are stored as `TIMESTAMP` in UTC. Client applications convert to local time for display.
- Stock movement and audit log tables are append-only. No `UPDATE` or `DELETE` is permitted on these tables from the application layer.
- Soft deletes use `deleted_at TIMESTAMP NULL` on records that should be deactivatable without losing history.

---

## 2. Core Tables

### 2.1 Tenant and Organisation

#### `businesses` (tenant root)
| Column | Type | Notes |
|---|---|---|
| id | BIGINT UNSIGNED PK AUTO_INCREMENT | Franchise ID |
| name | VARCHAR(255) NOT NULL | Business display name |
| slug | VARCHAR(100) UNIQUE | URL-safe identifier |
| tin | VARCHAR(50) | Uganda TIN |
| phone | VARCHAR(20) | Primary contact |
| email | VARCHAR(255) | |
| logo_url | VARCHAR(500) | Wasabi S3 path |
| address | TEXT | |
| country_code | CHAR(2) DEFAULT 'UG' | ISO 3166-1 alpha-2 |
| currency_code | CHAR(3) DEFAULT 'UGX' | ISO 4217 |
| financial_year_start_month | TINYINT DEFAULT 7 | Uganda default: July |
| subscription_plan | ENUM('basic','business','pro','enterprise') | |
| subscription_status | ENUM('trial','active','suspended','cancelled') | |
| trial_ends_at | TIMESTAMP NULL | |
| created_at | TIMESTAMP | |
| updated_at | TIMESTAMP | |

#### `branches`
| Column | Type | Notes |
|---|---|---|
| id | BIGINT UNSIGNED PK | |
| franchise_id | BIGINT UNSIGNED NOT NULL FK | |
| name | VARCHAR(255) NOT NULL | |
| address | TEXT | |
| phone | VARCHAR(20) | |
| is_active | BOOLEAN DEFAULT TRUE | |
| created_at | TIMESTAMP | |
| updated_at | TIMESTAMP | |

#### `warehouses`
| Column | Type | Notes |
|---|---|---|
| id | BIGINT UNSIGNED PK | |
| franchise_id | BIGINT UNSIGNED NOT NULL FK | |
| branch_id | BIGINT UNSIGNED NOT NULL FK | |
| name | VARCHAR(100) NOT NULL | e.g., 'Main Store', 'Retail Floor' |
| is_active | BOOLEAN DEFAULT TRUE | |

---

### 2.2 Users and Access Control

#### `users`
| Column | Type | Notes |
|---|---|---|
| id | BIGINT UNSIGNED PK | |
| franchise_id | BIGINT UNSIGNED NOT NULL FK | |
| name | VARCHAR(255) NOT NULL | |
| phone | VARCHAR(20) UNIQUE | Used for login + SMS |
| email | VARCHAR(255) NULL | |
| password_hash | VARCHAR(255) | bcrypt, cost >= 12 |
| nin | VARCHAR(20) NULL | National ID Number |
| branch_id | BIGINT UNSIGNED NULL FK | NULL = all branches |
| is_active | BOOLEAN DEFAULT TRUE | |
| totp_secret | VARCHAR(255) NULL | 2FA secret, encrypted |
| last_login_at | TIMESTAMP NULL | |
| created_at | TIMESTAMP | |
| updated_at | TIMESTAMP | |
| deleted_at | TIMESTAMP NULL | Soft delete |

#### `roles`
| Column | Type | Notes |
|---|---|---|
| id | BIGINT UNSIGNED PK | |
| name | VARCHAR(50) UNIQUE | 'cashier', 'branch_manager', etc. |
| display_name | VARCHAR(100) | |

#### `permissions`
| Column | Type | Notes |
|---|---|---|
| id | BIGINT UNSIGNED PK | |
| name | VARCHAR(100) UNIQUE | e.g., 'pos.sales.create' |
| module | VARCHAR(50) | e.g., 'pos' |

#### `role_permissions` (pivot)
| Column | Type |
|---|---|
| role_id | BIGINT UNSIGNED FK |
| permission_id | BIGINT UNSIGNED FK |
| PRIMARY KEY | (role_id, permission_id) |

#### `user_roles` (pivot)
| Column | Type | Notes |
|---|---|---|
| user_id | BIGINT UNSIGNED FK | |
| role_id | BIGINT UNSIGNED FK | |
| franchise_id | BIGINT UNSIGNED NOT NULL FK | Scoped to tenant |
| PRIMARY KEY | (user_id, role_id, franchise_id) | |

#### `refresh_tokens`
| Column | Type | Notes |
|---|---|---|
| id | BIGINT UNSIGNED PK | |
| user_id | BIGINT UNSIGNED FK | |
| franchise_id | BIGINT UNSIGNED NOT NULL FK | |
| token_hash | VARCHAR(255) | SHA-256 of token |
| device_name | VARCHAR(100) | |
| ip_address | VARCHAR(45) | |
| expires_at | TIMESTAMP | 30 days |
| revoked_at | TIMESTAMP NULL | |
| created_at | TIMESTAMP | |

---

### 2.3 Products and Inventory

#### `product_categories`
| Column | Type | Notes |
|---|---|---|
| id | BIGINT UNSIGNED PK | |
| franchise_id | BIGINT UNSIGNED NOT NULL FK | |
| name | VARCHAR(100) NOT NULL | |
| parent_id | BIGINT UNSIGNED NULL FK | Hierarchical categories |
| tax_rate_id | BIGINT UNSIGNED NULL FK | Default tax for category |

#### `products`
| Column | Type | Notes |
|---|---|---|
| id | BIGINT UNSIGNED PK | |
| franchise_id | BIGINT UNSIGNED NOT NULL FK | |
| name | VARCHAR(255) NOT NULL | |
| sku | VARCHAR(100) NULL | |
| barcode | VARCHAR(100) NULL | |
| category_id | BIGINT UNSIGNED FK | |
| base_uom | VARCHAR(20) | e.g., 'kg', 'piece' |
| cost_price | DECIMAL(15,2) | |
| type | ENUM('physical','service') DEFAULT 'physical' | |
| track_batches | BOOLEAN DEFAULT FALSE | Expiry tracking |
| reorder_level | DECIMAL(10,3) DEFAULT 0 | |
| is_active | BOOLEAN DEFAULT TRUE | |
| created_at | TIMESTAMP | |
| updated_at | TIMESTAMP | |
| deleted_at | TIMESTAMP NULL | |

#### `product_prices`
| Column | Type | Notes |
|---|---|---|
| id | BIGINT UNSIGNED PK | |
| product_id | BIGINT UNSIGNED FK | |
| franchise_id | BIGINT UNSIGNED NOT NULL FK | |
| tier | ENUM('retail','wholesale','distributor') | |
| price | DECIMAL(15,2) NOT NULL | |

#### `product_units` (multiple selling units)
| Column | Type | Notes |
|---|---|---|
| id | BIGINT UNSIGNED PK | |
| product_id | BIGINT UNSIGNED FK | |
| franchise_id | BIGINT UNSIGNED NOT NULL FK | |
| unit_name | VARCHAR(50) | e.g., 'Box of 12' |
| conversion_factor | DECIMAL(10,4) | 12.0 = 12 base units per box |
| price_override | DECIMAL(15,2) NULL | NULL = use product_prices |

#### `stock_levels`
| Column | Type | Notes |
|---|---|---|
| id | BIGINT UNSIGNED PK | |
| franchise_id | BIGINT UNSIGNED NOT NULL FK | |
| product_id | BIGINT UNSIGNED FK | |
| warehouse_id | BIGINT UNSIGNED FK | |
| quantity | DECIMAL(15,4) NOT NULL DEFAULT 0 | |
| updated_at | TIMESTAMP | |
| UNIQUE | (product_id, warehouse_id) | One row per product per location |

#### `stock_movements` (append-only)
| Column | Type | Notes |
|---|---|---|
| id | BIGINT UNSIGNED PK | |
| franchise_id | BIGINT UNSIGNED NOT NULL FK | |
| product_id | BIGINT UNSIGNED FK | |
| warehouse_id | BIGINT UNSIGNED FK | |
| batch_id | BIGINT UNSIGNED NULL FK | |
| movement_type | ENUM('sale','purchase_receipt','adjustment','transfer_out','transfer_in','supplier_return','customer_return','opening_balance') | |
| quantity | DECIMAL(15,4) NOT NULL | Positive = in, negative = out |
| unit_cost | DECIMAL(15,2) NULL | Cost at time of movement |
| reference_id | BIGINT UNSIGNED NULL | ID of source record (sale_id, po_id, etc.) |
| reference_type | VARCHAR(50) NULL | 'sale', 'purchase_order', etc. |
| notes | TEXT NULL | |
| created_by | BIGINT UNSIGNED FK users.id | |
| created_at | TIMESTAMP | |

#### `batches`
| Column | Type | Notes |
|---|---|---|
| id | BIGINT UNSIGNED PK | |
| franchise_id | BIGINT UNSIGNED NOT NULL FK | |
| product_id | BIGINT UNSIGNED FK | |
| warehouse_id | BIGINT UNSIGNED FK | |
| batch_number | VARCHAR(100) | |
| manufactured_at | DATE NULL | |
| expires_at | DATE NULL | |
| quantity | DECIMAL(15,4) NOT NULL DEFAULT 0 | Current batch quantity |
| supplier_id | BIGINT UNSIGNED NULL FK | |
| created_at | TIMESTAMP | |

---

### 2.4 Sales and POS

#### `pos_sessions`
| Column | Type | Notes |
|---|---|---|
| id | BIGINT UNSIGNED PK | |
| franchise_id | BIGINT UNSIGNED NOT NULL FK | |
| branch_id | BIGINT UNSIGNED FK | |
| cashier_id | BIGINT UNSIGNED FK users.id | |
| opening_float | DECIMAL(15,2) | Cash count at session open |
| closing_cash_counted | DECIMAL(15,2) NULL | Cash counted at session close |
| status | ENUM('open','closed') DEFAULT 'open' | |
| opened_at | TIMESTAMP | |
| closed_at | TIMESTAMP NULL | |

#### `sales`
| Column | Type | Notes |
|---|---|---|
| id | BIGINT UNSIGNED PK | |
| franchise_id | BIGINT UNSIGNED NOT NULL FK | |
| branch_id | BIGINT UNSIGNED FK | |
| pos_session_id | BIGINT UNSIGNED FK | |
| cashier_id | BIGINT UNSIGNED FK | |
| customer_id | BIGINT UNSIGNED NULL FK | |
| receipt_number | VARCHAR(50) | Sequential, per-session |
| status | ENUM('completed','voided') DEFAULT 'completed' | |
| subtotal | DECIMAL(15,2) | Before discount and tax |
| discount_amount | DECIMAL(15,2) DEFAULT 0 | |
| tax_amount | DECIMAL(15,2) DEFAULT 0 | |
| total | DECIMAL(15,2) | |
| notes | TEXT NULL | |
| synced_at | TIMESTAMP NULL | NULL = pending_sync (offline) |
| created_at | TIMESTAMP | |

#### `sale_items`
| Column | Type | Notes |
|---|---|---|
| id | BIGINT UNSIGNED PK | |
| franchise_id | BIGINT UNSIGNED NOT NULL FK | |
| sale_id | BIGINT UNSIGNED FK | |
| product_id | BIGINT UNSIGNED FK | |
| batch_id | BIGINT UNSIGNED NULL FK | |
| quantity | DECIMAL(15,4) NOT NULL | |
| unit_price | DECIMAL(15,2) | Price at time of sale |
| discount_amount | DECIMAL(15,2) DEFAULT 0 | Per-item discount |
| line_total | DECIMAL(15,2) | |

#### `sale_payments` (multi-payment support)
| Column | Type | Notes |
|---|---|---|
| id | BIGINT UNSIGNED PK | |
| franchise_id | BIGINT UNSIGNED NOT NULL FK | |
| sale_id | BIGINT UNSIGNED FK | |
| payment_account_id | BIGINT UNSIGNED FK | |
| method | ENUM('cash','mtn_momo','airtel_money','credit','bank_transfer','other') | |
| amount | DECIMAL(15,2) NOT NULL | |
| reference | VARCHAR(100) NULL | MoMo transaction reference |
| created_at | TIMESTAMP | |

---

### 2.5 Customers

#### `customers`
| Column | Type | Notes |
|---|---|---|
| id | BIGINT UNSIGNED PK | |
| franchise_id | BIGINT UNSIGNED NOT NULL FK | |
| name | VARCHAR(255) NOT NULL | |
| phone | VARCHAR(20) | |
| email | VARCHAR(255) NULL | |
| district | VARCHAR(100) NULL | Uganda structure |
| sub_county | VARCHAR(100) NULL | |
| customer_group_id | BIGINT UNSIGNED NULL FK | |
| credit_limit | DECIMAL(15,2) DEFAULT 0 | |
| outstanding_balance | DECIMAL(15,2) DEFAULT 0 | Maintained in real time |
| portal_token | VARCHAR(255) NULL | Magic link token hash |
| portal_token_expires_at | TIMESTAMP NULL | |
| is_active | BOOLEAN DEFAULT TRUE | |
| created_at | TIMESTAMP | |
| deleted_at | TIMESTAMP NULL | |

#### `customer_groups`
| Column | Type | Notes |
|---|---|---|
| id | BIGINT UNSIGNED PK | |
| franchise_id | BIGINT UNSIGNED NOT NULL FK | |
| name | VARCHAR(100) | 'retail', 'wholesale', 'VIP', 'staff' |
| price_tier | ENUM('retail','wholesale','distributor') DEFAULT 'retail' | |
| credit_terms_days | TINYINT DEFAULT 0 | |

---

### 2.6 Suppliers and Purchasing

#### `suppliers`
| Column | Type | Notes |
|---|---|---|
| id | BIGINT UNSIGNED PK | |
| franchise_id | BIGINT UNSIGNED NOT NULL FK | |
| name | VARCHAR(255) NOT NULL | |
| contact_person | VARCHAR(255) NULL | |
| phone | VARCHAR(20) NULL | |
| email | VARCHAR(255) NULL | |
| payment_terms_days | TINYINT DEFAULT 30 | |
| outstanding_balance | DECIMAL(15,2) DEFAULT 0 | |
| is_active | BOOLEAN DEFAULT TRUE | |

#### `purchase_orders`
| Column | Type | Notes |
|---|---|---|
| id | BIGINT UNSIGNED PK | |
| franchise_id | BIGINT UNSIGNED NOT NULL FK | |
| supplier_id | BIGINT UNSIGNED FK | |
| branch_id | BIGINT UNSIGNED FK | |
| po_number | VARCHAR(50) | |
| status | ENUM('draft','sent','partially_received','fully_received','cancelled') | |
| total | DECIMAL(15,2) | |
| created_by | BIGINT UNSIGNED FK | |
| created_at | TIMESTAMP | |

#### `purchase_order_items`
| Column | Type | Notes |
|---|---|---|
| id | BIGINT UNSIGNED PK | |
| franchise_id | BIGINT UNSIGNED NOT NULL FK | |
| purchase_order_id | BIGINT UNSIGNED FK | |
| product_id | BIGINT UNSIGNED FK | |
| ordered_qty | DECIMAL(15,4) | |
| received_qty | DECIMAL(15,4) DEFAULT 0 | |
| unit_cost | DECIMAL(15,2) | |

---

### 2.7 Financial Accounts

#### `payment_accounts`
| Column | Type | Notes |
|---|---|---|
| id | BIGINT UNSIGNED PK | |
| franchise_id | BIGINT UNSIGNED NOT NULL FK | |
| branch_id | BIGINT UNSIGNED NULL FK | NULL = all branches |
| name | VARCHAR(100) NOT NULL | e.g., 'Cash Till - Branch A' |
| type | ENUM('cash','mtn_momo','airtel_money','bank','sacco','other') | |
| account_number | VARCHAR(100) NULL | |
| balance | DECIMAL(15,2) DEFAULT 0 | Maintained in real time |
| is_active | BOOLEAN DEFAULT TRUE | |

#### `account_transactions` (append-only)
| Column | Type | Notes |
|---|---|---|
| id | BIGINT UNSIGNED PK | |
| franchise_id | BIGINT UNSIGNED NOT NULL FK | |
| payment_account_id | BIGINT UNSIGNED FK | |
| type | ENUM('sale_payment','expense','purchase_payment','transfer_in','transfer_out','deposit','withdrawal','payroll','opening_balance') | |
| amount | DECIMAL(15,2) | Positive = in, negative = out |
| balance_after | DECIMAL(15,2) | Running balance snapshot |
| reference_id | BIGINT UNSIGNED NULL | |
| reference_type | VARCHAR(50) NULL | |
| description | TEXT NULL | |
| created_by | BIGINT UNSIGNED FK | |
| created_at | TIMESTAMP | |

---

### 2.8 Expenses

#### `expense_categories`
| Column | Type | Notes |
|---|---|---|
| id | BIGINT UNSIGNED PK | |
| franchise_id | BIGINT UNSIGNED NOT NULL FK | |
| name | VARCHAR(100) | |
| is_tax_deductible | BOOLEAN DEFAULT FALSE | |

#### `expenses`
| Column | Type | Notes |
|---|---|---|
| id | BIGINT UNSIGNED PK | |
| franchise_id | BIGINT UNSIGNED NOT NULL FK | |
| branch_id | BIGINT UNSIGNED FK | |
| category_id | BIGINT UNSIGNED FK | |
| payment_account_id | BIGINT UNSIGNED FK | |
| amount | DECIMAL(15,2) NOT NULL | |
| description | TEXT NULL | |
| receipt_photo_url | VARCHAR(500) NULL | Wasabi S3 path |
| status | ENUM('pending_approval','approved','rejected') DEFAULT 'approved' | |
| approved_by | BIGINT UNSIGNED NULL FK | |
| expense_date | DATE NOT NULL | |
| created_by | BIGINT UNSIGNED FK | |
| created_at | TIMESTAMP | |

---

### 2.9 HR and Payroll

#### `staff` (extends users conceptually, separate table for HR-specific data)
| Column | Type | Notes |
|---|---|---|
| id | BIGINT UNSIGNED PK | |
| franchise_id | BIGINT UNSIGNED NOT NULL FK | |
| user_id | BIGINT UNSIGNED FK | Link to users table |
| branch_id | BIGINT UNSIGNED FK | |
| employment_type | ENUM('permanent','contract','casual') | |
| hire_date | DATE | |
| contract_end_date | DATE NULL | |
| probation_end_date | DATE NULL | |
| department | VARCHAR(100) NULL | |
| job_title | VARCHAR(100) NULL | |
| is_active | BOOLEAN DEFAULT TRUE | |

#### `salary_structures`
| Column | Type | Notes |
|---|---|---|
| id | BIGINT UNSIGNED PK | |
| franchise_id | BIGINT UNSIGNED NOT NULL FK | |
| staff_id | BIGINT UNSIGNED FK | |
| basic_salary | DECIMAL(15,2) | |
| housing_allowance | DECIMAL(15,2) DEFAULT 0 | |
| transport_allowance | DECIMAL(15,2) DEFAULT 0 | |
| other_earnings | JSON NULL | Array of {name, amount} |
| other_deductions | JSON NULL | Array of {name, amount} |
| effective_from | DATE | |

#### `payroll_runs`
| Column | Type | Notes |
|---|---|---|
| id | BIGINT UNSIGNED PK | |
| franchise_id | BIGINT UNSIGNED NOT NULL FK | |
| period_month | TINYINT | 1-12 |
| period_year | SMALLINT | |
| status | ENUM('draft','approved') DEFAULT 'draft' | |
| total_gross | DECIMAL(15,2) | |
| total_deductions | DECIMAL(15,2) | |
| total_net | DECIMAL(15,2) | |
| approved_by | BIGINT UNSIGNED NULL FK | |
| approved_at | TIMESTAMP NULL | |
| created_at | TIMESTAMP | |

#### `payslips`
| Column | Type | Notes |
|---|---|---|
| id | BIGINT UNSIGNED PK | |
| franchise_id | BIGINT UNSIGNED NOT NULL FK | |
| payroll_run_id | BIGINT UNSIGNED FK | |
| staff_id | BIGINT UNSIGNED FK | |
| gross_pay | DECIMAL(15,2) | |
| paye | DECIMAL(15,2) | |
| nssf_employee | DECIMAL(15,2) | |
| nssf_employer | DECIMAL(15,2) | |
| lst | DECIMAL(15,2) DEFAULT 0 | |
| other_deductions | DECIMAL(15,2) DEFAULT 0 | |
| net_pay | DECIMAL(15,2) | |
| pdf_url | VARCHAR(500) NULL | Wasabi S3 path |
| sent_at | TIMESTAMP NULL | WhatsApp/SMS delivery timestamp |

---

### 2.10 Audit Log (Append-Only)

#### `audit_log`
| Column | Type | Notes |
|---|---|---|
| id | BIGINT UNSIGNED PK | |
| franchise_id | BIGINT UNSIGNED NOT NULL FK | |
| user_id | BIGINT UNSIGNED FK | Actor |
| action | VARCHAR(100) | e.g., 'sale.created', 'stock.adjusted', 'sale.voided' |
| table_name | VARCHAR(100) | |
| record_id | BIGINT UNSIGNED NULL | |
| old_values | JSON NULL | Before state |
| new_values | JSON NULL | After state |
| ip_address | VARCHAR(45) | |
| device_id | VARCHAR(255) NULL | |
| created_at | TIMESTAMP | |

**No DELETE or UPDATE is permitted on `audit_log` from any application user account.**

---

## 3. Key Indexes

```sql
-- Tenant scoping (on every tenant-scoped table)
INDEX idx_franchise_id (franchise_id)

-- POS performance
INDEX idx_sales_branch_date (franchise_id, branch_id, created_at)
INDEX idx_sales_session (pos_session_id)
INDEX idx_sale_items_product (product_id)

-- Inventory performance
INDEX idx_stock_levels_product_warehouse (product_id, warehouse_id)
INDEX idx_stock_movements_product (franchise_id, product_id, created_at)
INDEX idx_batches_expiry (franchise_id, expires_at)

-- Customer portal
INDEX idx_customers_portal_token (portal_token)

-- Reporting
INDEX idx_account_transactions_account_date (payment_account_id, created_at)
INDEX idx_expenses_franchise_date (franchise_id, expense_date)
```

---

## 4. EFRIS Data Model Notes (Phase 3 Readiness)

The following columns are reserved for EFRIS in Phase 1 schema design, populated in Phase 3:

- `sales.efris_fdn` VARCHAR(100) NULL -- Fiscal Document Number from URA
- `sales.efris_status` ENUM('not_submitted','pending','submitted','failed') NULL
- `sales.efris_qr_code` TEXT NULL -- URA QR code data
- `products.efris_product_code` VARCHAR(100) NULL -- URA product catalogue code

These columns are added as NULLable in Phase 1, preventing a breaking migration when the EFRIS module is activated in Phase 3.

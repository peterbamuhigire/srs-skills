# LonghornERP Finance ERP Enhancement Roadmap

## Purpose

This document translates the source book `C:\Users\Peter\Downloads\ERP Playbook\Finance ERP Playbook.epub` into concrete enhancement decisions for LonghornERP.

The goal is to ensure LonghornERP's finance core is not merely a bookkeeping engine, but a world-class finance ERP foundation for African SMEs and larger multi-entity organisations.

## Core Findings from the Finance ERP Playbook

The Finance ERP playbook consistently treats finance ERP as more than general ledger screens. The critical capability pillars are:

- general ledger and subledger integrity
- close and consolidation foundations
- controls, security, workflow, approvals, and audit trail
- reporting foundations
- record-to-report operating discipline
- data, compliance, and finance governance readiness

This means LonghornERP should not stop at journal posting, statements, bank reconciliation, and tax. A world-class finance core also needs explicit close orchestration, recurring and reversing journals, consolidation-ready structures, approval controls, and management reporting discipline.

## Current LonghornERP Position

LonghornERP already has strong finance foundations:

- chart of accounts
- double-entry journals
- financial statements
- bank reconciliation
- tax management
- budgeting
- period close
- audit logging
- strong subledger integration across sales, procurement, payroll, inventory, assets, and manufacturing

The main gap is not absence of accounting. The main gap is that finance operating control is still too lightly modelled.

## Required Finance Uplifts

LonghornERP should explicitly add or strengthen these capabilities:

- close checklist orchestration and finance close dashboard
- recurring journals and automatic reversal journals
- consolidation-ready entity and elimination structure
- intercompany and elimination-ready posting metadata
- finance approvals for sensitive journals and close actions
- stronger reporting foundations for management packs and finance KPIs
- finance control evidence and exception visibility

## Boundary Rule

- `ACCOUNTING` owns record-to-report control, close, journal discipline, reporting foundations, and consolidation-ready finance structure.
- Subledgers continue to originate operational transactions, but they do not own the finance operating model.
- `AUDIT` remains the immutable evidence layer; `ACCOUNTING` remains the owner of finance control workflows.

## Recommended Delivery Steps

1. Upgrade PRD and module overview wording so Accounting is positioned as a finance ERP backbone, not just GL.
2. Extend the Accounting SRS for close orchestration, consolidation foundations, recurring/reversing journals, approvals, and control workflows.
3. Extend accounting LLD, API, and database designs for those new finance capabilities.
4. Rebuild the finance-facing `.docx` artefacts so the deliverable set stays current.

## Output Standard

A world-class LonghornERP finance core must support:

- statutory compliance
- auditability
- management visibility
- disciplined month-end close
- multi-entity growth readiness
- strong finance controls without breaking SME usability

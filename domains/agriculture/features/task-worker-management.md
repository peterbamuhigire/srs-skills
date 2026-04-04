# Feature: Task and Worker Management

## Description
Farm task planning and labour management covering task creation, assignment, scheduling, worker profiles, payroll, and mobile-based task completion. Supports both permanent staff with statutory deductions and casual workers with mobile money payment, alongside calendar, Kanban, and recurring task workflows.

## Standard Capabilities
- Task CRUD with plot, enterprise, and worker assignment
- Worker mobile task completion with photo evidence and GPS stamp
- Daily work log with hours, tasks completed, and notes
- Worker profile management (name, NIN, mobile money number, role, pay rate)
- Payroll calculation (daily rate, piece rate, monthly salary)
- Calendar view with drag-and-drop task scheduling
- Recurring task templates (weekly spraying, daily milking, monthly deworming)
- Kanban board view (To Do, In Progress, Done)
- Casual worker mobile money payment initiation with approval workflow
- NSSF and PAYE calculation for permanent staff
- Task completion rate and worker productivity reports
- Crew and team management for group task assignment

## Regulatory Hooks
- Employment Act 2006: minimum wage, working hours, leave entitlements, and termination procedures
- NSSF Act: mandatory contribution calculation and remittance tracking for permanent employees
- PAYE: income tax deduction at source for qualifying employees

## Linked NFRs
- AG-001 (Data Integrity and Audit Trail)
- AG-003 (Financial Data Accuracy and Reconciliation)
- AG-009 (Data Privacy and Consent)

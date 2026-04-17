# Project Vision

**Project:** AcademiaPro
**Client Contact:** Peter — Chwezi Core Systems (chwezicore.com)
**Date:** 2026-03-27

## Problem Statement

Schools across Uganda and Africa spend hundreds of hours per term on manual administration — fee collection via paper receipts, handwritten attendance registers, mark sheets computed in Excel, and report cards typed individually. Existing software is either too simple (no depth), too complex (requires an IT team), foreign-built (no MTN MoMo, no UNEB grading, no 3-term Uganda calendar), or lacks mobile access for parents and teachers. Academia Pro automates every repeatable school process while remaining simple enough for a single administrator to operate after watching module training videos. It is Uganda-first and Pan-Africa by architecture.

## Design Covenant (Binding Constraint)

> Automate every school process as much as possible, yet remain simple enough for a single administrator to operate — provided each user has watched the training videos for their assigned modules. Deep and rich in capability; easy and flexible in daily use.

**Derived hard requirements:**
- Maximum automation by default: fee reminders fire automatically, attendance alerts send without manual trigger, reports generate at term-end unprompted
- Zero-config defaults: a Uganda school is operational within 30 minutes of signup
- Role-scoped UX: a teacher never sees an accountant's screen; complexity is hidden behind role boundaries
- Training-path architecture: each module ships with embedded video help; users learn module-by-module
- Progressive disclosure: advanced settings exist but do not clutter daily workflow
- Single-admin survivability: if the IT person leaves, the head teacher can continue operating the system

## Goals

1. Capture 500 Uganda schools within 24 months of Phase 1 launch.
2. Provide fully automated UNEB-graded report cards (PLE, UCE, UACE) with zero manual computation.
3. Achieve 90%+ fee collection reconciliation rate via SchoolPay integration and mobile money notifications.
4. Deliver EMIS/MoES integration so schools submit statutory reports without re-entering data.
5. Expand to at least 3 additional African countries (Kenya, Tanzania, Nigeria) within 36 months of launch.

## Stakeholders

See `_context/stakeholders.md` for the full register.

Key groups: School Owner/Director, Head Teacher, Class Teacher, Accounts Bursar, Librarian, Transport Manager, Hostel Warden, Parent/Guardian, Student, Government (MoES/EMIS), Chwezi Core Systems (operator), SchoolPay (payment partner).

## Success Criteria

- Phase 1 gate: all standard modules functional, 100% test pass rate, at least 1 pilot school live
- Phase 4 gate: all modules pass 100% automated test suite before Phase 5 begins
- Phase 8 gate: UNEB grading verified against sample mark sheets provided by UNEB; EMIS report export validated by MoES field officer
- Pan-Africa gate (Phase 11): Kenya NEMIS integration functional; M-Pesa Daraja API tested with live transactions

## Methodology Note (Water-Scrum-Fall Confirmation)

Methodology is Hybrid (Water-Scrum-Fall): formal requirements sign-off and phase gate before each phase; iterative sprints within each phase. This pattern was confirmed by Peter on 2026-03-27. Phase gate criteria are defined in `_context/metrics.md`. No phase begins development until `_context/` files for that phase are reviewed and signed off.

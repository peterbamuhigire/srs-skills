# Introduction

## Purpose

This Low-Level Design (LLD) document specifies the internal structure of every service class in Longhorn ERP. For each service it defines: method signatures with parameter types and return types, inter-service dependencies, database tables read and written, stored procedure call points, transaction boundaries, and event triggers. The document is the authoritative reference for developers implementing, extending, or reviewing Longhorn ERP components.

## Scope

Coverage includes all modules listed in the High-Level Design (HLD):

- **Core modules:** ACCOUNTING, INVENTORY, SALES, PROCUREMENT, USER_MGMT, AUDIT
- **Add-on modules:** ADV_INVENTORY, MANUFACTURING, HR_PAYROLL, POS, SALES_CRM, SALES_AGENTS, COOPERATIVE, PROJECTS, STRATEGY_BSC, ASSETS
- **Platform services:** LOCALISATION, MOBILE_API, INTEGRATIONS, BILLING

The LLD covers the PHP 8.3 server-side service layer, the MySQL 9.1 database interaction patterns, and the integration adapters. Frontend JavaScript, Blade/HTML templates, and mobile UI code are outside this document's scope; the Mobile API contracts are specified in the separate API Specification document.

## Relationship to the HLD

The HLD (see `projects/LonghornERP/03-design-documentation/01-hld/`) defines the system's deployment topology, module boundaries, panel architecture, and middleware chain. This LLD refines each HLD component to the class and method level. Where the HLD states that a service exists, this document specifies what it does, what it accepts, what it returns, and which database objects it touches.

## Conventions Used in This Document

- Class names appear in `monospace`.
- Method signatures follow PHP 8.3 typed syntax: `methodName(Type $param): ReturnType`.
- SQL identifiers (table names, column names, stored procedure names, view names) appear in `monospace`.
- `[CONTEXT-GAP: GAP-xxx]` tags mark requirements where external API specifications have not yet been confirmed. These items must be resolved before the integration components are coded.
- All method-signature tables use four columns: Method, Parameters, Returns, Description.

## Applicable Standards

- IEEE Std 830-1998 — Software Requirements Specifications
- IEEE Std 1233-1998 — Guide for Developing System Requirements Specifications
- IEEE Std 610.12-1990 — Glossary of Software Engineering Terminology

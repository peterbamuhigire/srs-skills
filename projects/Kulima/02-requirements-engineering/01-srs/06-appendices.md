# 6 Appendices

## Appendix A: Glossary

The complete glossary is maintained in `projects/Kulima/_context/glossary.md` and contains 56 defined terms covering agricultural, technical, regulatory, and platform-specific terminology. All terms used in this SRS are defined in the glossary.

Key domain-specific terms used in this SRS:

| Term | Definition |
|---|---|
| FMIS | Farm Management Information System |
| Chwezi Core | Custom PHP/MySQL multi-tenant SaaS framework shared across Kulima, Academia Pro, and Medic8 |
| Tenant | A single customer account with complete data isolation |
| Enterprise | A distinct production unit within a farm for profitability tracking |
| Crop Season | A defined period for growing a specific crop variety on a specific plot |
| Collection Centre | Physical location for cooperative member produce delivery and grading |
| DDS | Due Diligence Statement under EUDR |
| EUDR | EU Deforestation Regulation 2023/1115 |
| Geofence | Virtual geographic boundary triggering alerts on exit |
| Dual-Mode Accounting | Simple Mode ("Money in/out") and Advanced Mode (double-entry) financial recording |
| Matooke | East African cooking banana with perennial crop tracking requirements |
| Ankole Longhorn | Indigenous Ugandan cattle breed with distinct production benchmarks |

Refer to `_context/glossary.md` for the full set of defined terms including: Acre, Agro-dealer, AI, BXW, Chain of Custody, Claude API, Cooperative (Franchise), GeoJSON, GlobalGAP, GPS, Hectare, HLS, IoT, Jaguza, JWT, Kienyeji, Kulima, MAAIF, Mailo Land, MFI, MoMo, NAADS, NDVI, NIN, NSSF, ONVIF, OWC, PAYE, Plot, QR Code, RBAC, Room, RTSP, SACCO, Sentinel-2, SQLCipher, SwiftData, UCDA, UEPB, UGX, and USSD.

## Appendix B: Standards Traceability Matrix

| SRS Section | IEEE 830-1998 | IEEE 29148-2018 | IEEE 1233-1998 | IEEE 610.12-1990 | ASTM E1340 |
|---|---|---|---|---|---|
| 1.1 Purpose | 5.1.1 | 5.2.1 | - | - | - |
| 1.2 Scope | 5.1.2 | 5.2.2 | 4.1 | - | - |
| 1.3 Definitions | 5.1.3 | 5.2.3 | - | All terms | - |
| 1.4 References | 5.1.4 | 5.2.4 | - | - | - |
| 1.5 Overview | 5.1.5 | 5.2.5 | - | - | - |
| 2.1 Product Perspective | 5.2.1 | 6.2.1 | 4.2 | - | 5.1 |
| 2.2 Product Functions | 5.2.2 | 6.2.2 | 4.3 | - | 5.2 |
| 2.3 User Characteristics | 5.2.3 | 6.2.3 | 4.4 | - | 5.3 |
| 2.4 Constraints | 5.2.4 | 6.2.4 | 4.5 | - | - |
| 2.5 Assumptions | 5.2.5 | 6.2.5 | 4.6 | - | - |
| 3.x Functional Requirements | 5.3.1-5.3.8 | 6.3 | 5.1-5.3 | Functional requirement | 6.1 |
| 4.x Non-Functional Requirements | 5.3.6 | 6.4 | 5.4 | Performance, reliability | 6.2 |
| 5.1 User Interfaces | 5.3.1(a) | 6.3.1 | - | - | 6.3 |
| 5.2 Hardware Interfaces | 5.3.1(b) | 6.3.2 | - | - | 6.3 |
| 5.3 Software Interfaces | 5.3.1(c) | 6.3.3 | - | - | 6.3 |
| 5.4 Communication Interfaces | 5.3.1(d) | 6.3.4 | - | - | 6.3 |

**Coverage notes:**

- IEEE 830-1998: All sections (5.1 through 5.3) are covered. Stimulus-response format per Section 5.3.2 is used for all functional requirements
- IEEE 29148-2018: Stakeholder requirements (Clause 6.2) and system requirements (Clause 6.3) are addressed. Verification criteria per Clause 6.4 are included with every requirement
- IEEE 1233-1998: System-level requirements structure (Clauses 4-5) is followed for product perspective and functional decomposition
- IEEE 610.12-1990: All terminology conforms to the standard glossary definitions; project-specific terms are defined in Appendix A
- ASTM E1340: Prototyping considerations are addressed through the 4-phase build approach and the offline-first constraint requiring local prototype validation

## Appendix C: Phase-Feature Matrix

| Module / Feature | Phase 1 (MVP) | Phase 2 (Growth) | Phase 3 (IoT) | Phase 4 (Enterprise) |
|---|---|---|---|---|
| Farm and Plot Management | CRUD, soil, irrigation, tenure, admin hierarchy | GPS polygon mapping, NDVI overlay | - | - |
| Crop Management | Full lifecycle, 200+ library, activities, harvest, yield | - | AI pest/disease ID | - |
| Livestock Management | Individual + flock tracking, health, reproduction, production | - | IoT integration | - |
| Financial Records (Simple) | Income, expense, budget, profitability, cash flow, export | - | - | - |
| Financial Records (Advanced) | - | Double-entry, chart of accounts, statements | - | - |
| Task and Worker Management | CRUD, Kanban, calendar, payroll, MoMo payment | - | - | - |
| Weather and Advisory | Forecast, alerts, climate advisory | - | Weather station integration | - |
| Inventory Management | - | Inputs, equipment, produce, alerts | - | - |
| Supply Chain Traceability | - | Batches, chain of custody, QR, EUDR DDS | - | EUDR automation |
| Marketplace | - | Listings, search, prices, directories, orders | - | - |
| Cooperative Module | - | Members, collection, grading, bulk payment | - | - |
| Jaguza IoT Integration | - | - | OAuth, polling, alerts, dashboard | - |
| GPS Animal Tracking | - | - | Trackers, geofence, breach alerts, playback | - |
| Camera Surveillance | - | - | RTSP proxy, live view, PTZ, motion alerts | - |
| AI Farm Advisor | - | - | NLP Q&A, photo diagnosis, recommendations | - |
| Sensor Integration | - | - | Soil, weather station, drone | - |
| Director Platform | - | - | - | Consolidated view, approvals, transfers |
| Authentication and Tenancy | Dual auth, RBAC, tiers, MoMo subscription | - | - | - |
| Offline and Sync | Room/SwiftData, queue sync, conflict resolution | - | - | - |
| Notifications | SMS, push, in-app | - | IoT alerts, camera alerts | WhatsApp |
| Web Dashboard | Full CRUD, dashboards | Traceability, marketplace, cooperative | IoT, cameras, GPS | Director |
| Android App | Full offline-first app | GPS mapping | IoT, camera, GPS, AI screens | Director mode |
| iOS App | - | Full offline-first app | IoT, camera, GPS, AI screens | Director mode |
| Multi-Lingual | English, Luganda, Swahili | French, Portuguese, Kinyarwanda | - | - |
| Multi-Country | Uganda only | - | - | Kenya, Tanzania, Rwanda |
| USSD/SMS Fallback | - | - | - | Basic transactions |
| White-Label | - | - | - | Custom branding |
| Bank/Insurance API | - | - | - | Direct integration |

**Phase deployment strategy:**

- **Phase 1 (MVP):** Core farm management — target 100 paying farmers within 6 months. Revenue: UGX 4M/month MRR
- **Phase 2 (Growth):** Traceability, marketplace, cooperative, and iOS — enables EUDR compliance and cooperative onboarding
- **Phase 3 (IoT and Surveillance):** Add-on modules for premium customers — Jaguza IoT, GPS tracking, CCTV, AI advisor
- **Phase 4 (Enterprise):** Director platform, multi-country, white-label, bank integrations — target UGX 150M/month MRR

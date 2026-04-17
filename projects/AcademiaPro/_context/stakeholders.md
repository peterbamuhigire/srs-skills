# Stakeholders — Academia Pro

## Chwezi Core Systems (Product Owner)

- **Influence:** Critical — product decisions, pricing, roadmap
- **Interest:** High
- **Primary Needs:** Scalable SaaS platform with recurring revenue; minimal support overhead per school; clear audit trail for compliance
- **Key Concerns:** Data security and privacy liability; BoU regulatory compliance for payments; URSB copyright registration
- **Communication Preference:** Owner is Peter — internal; all decisions documented in `_context/` files

## School Owner / Director

- **Influence:** High — purchasing decision-maker; signs up the school
- **Interest:** High
- **Primary Needs:** Real-time financial overview; staff management; school performance analytics; school website
- **Key Concerns:** Cost vs value; ease of transition from current system; data ownership and privacy
- **Communication Preference:** Mobile app (Phase 3); web portal daily

## Head Teacher

- **Influence:** High — primary daily operator
- **Interest:** High
- **Primary Needs:** Attendance oversight; exam coordination; class performance summaries; communication with parents
- **Key Concerns:** System downtime during exam season; ease of report card generation; accuracy of UNEB grade computation
- **Communication Preference:** Web portal; SMS alerts for critical events

## Class Teacher

- **Influence:** Medium — daily attendance and marks entry
- **Interest:** High
- **Primary Needs:** Fast attendance entry; easy mark entry per exam; homework posting; view class list
- **Key Concerns:** Mobile-first access (many teachers use smartphones only); offline availability during school hours; training curve
- **Communication Preference:** Android app (Phase 6); web portal fallback

## Accounts Bursar

- **Influence:** Medium — fee management
- **Interest:** High
- **Primary Needs:** Fee structure setup; payment recording; receipt generation; arrears management; financial reports
- **Key Concerns:** Double-payment prevention; reconciliation with SchoolPay; audit trail for cash transactions
- **Communication Preference:** Web portal; Excel export for reporting to owner

## Parent / Guardian

- **Influence:** Low (on product decisions) / High (on adoption — won't pay fees they can't track)
- **Interest:** High
- **Primary Needs:** View child's report card; fee balance and payment history; attendance alerts; homework assignments; health alerts (Phase 7)
- **Key Concerns:** Privacy of child's data; ease of use on low-end smartphones; SMS in lieu of app for non-smartphone parents
- **Communication Preference:** Android/iOS app (Phase 5/10); web portal; SMS for critical alerts

## Student

- **Influence:** Low
- **Interest:** Medium
- **Primary Needs:** View timetable; view results; download materials; view fee balance; check homework
- **Key Concerns:** Privacy; ease of use; access from school computer labs or personal phone
- **Communication Preference:** Web portal; Android/iOS app (Phase 5/10)

## Librarian

- **Influence:** Low
- **Interest:** Medium
- **Primary Needs:** Book catalogue; borrowing records; overdue notifications; fine management
- **Key Concerns:** Import of existing book catalogue; barcode scanner support (optional)
- **Communication Preference:** Web portal

## Transport Manager

- **Influence:** Low
- **Interest:** Medium
- **Primary Needs:** Bus route setup; student bus assignments; transport fee billing
- **Key Concerns:** Real-time driver location (optional GPS); emergency contact for bus incidents
- **Communication Preference:** Web portal; bus driver app (Phase 6)

## Hostel Warden

- **Influence:** Low
- **Interest:** Medium
- **Primary Needs:** Room assignments; boarding fee billing; duty roster; end-of-term checkout
- **Key Concerns:** Capacity planning; integration with student and parent communication
- **Communication Preference:** Web portal

## Ministry of Education and Sports (MoES) / EMIS

- **Influence:** High — regulatory compliance required for school registration
- **Interest:** Low (passive)
- **Primary Needs:** EMIS-format student headcount and teacher reports; exam registration data; school statistics
- **Key Concerns:** Data accuracy; format compliance; deadline adherence
- **Communication Preference:** Bulk export (XML/CSV) on demand; automated scheduled submission (Phase 11)

## SchoolPay (Payment Partner)

- **Influence:** High — controls 15,000+ Uganda schools' payment infrastructure; BoU licensed
- **Interest:** Low (passive — integration is Academia Pro's initiative)
- **Primary Needs:** Proper API usage per their merchant documentation; accurate reconciliation
- **Key Concerns:** Fraud prevention; compliance with BoU regulations
- **Communication Preference:** API integration; SchoolPay merchant dashboard cross-reference

## Uganda National Examinations Board (UNEB)

- **Influence:** High — defines grading rules; exam registration formats
- **Interest:** Low (passive)
- **Primary Needs:** Accurate candidate registration data in UNEB format; grading engine that matches UNEB published rules
- **Key Concerns:** Data accuracy; format compliance
- **Communication Preference:** Bulk export; contact for registration manual — see `_context/gap-analysis.md` resource list

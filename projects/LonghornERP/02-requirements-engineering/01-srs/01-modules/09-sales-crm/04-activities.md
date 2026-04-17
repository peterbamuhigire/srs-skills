# Activity Logging

## 4.1 Activity Types

**FR-CRM-015** — The system shall support the following activity types on leads, opportunities, and contacts: Call, Email, Meeting, WhatsApp Message, Demo, and Task (configurable — additional types may be added by the administrator).

**FR-CRM-016** — When a user logs a Call activity, the system shall record: contact called, call direction (inbound/outbound), call duration (minutes), call summary, call outcome (configurable: Interested, Not Interested, Follow-up Required, No Answer, Left Voicemail), and the next follow-up date.

**FR-CRM-017** — When a user logs an Email activity, the system shall record: recipient(s), email subject, summary of content, and whether the email was sent directly from the CRM or imported from an external email client.

**FR-CRM-018** — When a user logs a Meeting activity, the system shall record: meeting date and time, location or video-call link, attendees (internal and external), agenda summary, key discussion points, decisions made, and action items with assigned owners and due dates.

## 4.2 Activity Scheduling

**FR-CRM-019** — The system shall provide an activity calendar view showing all scheduled activities for the current user for the current and next 4 weeks; activities shall be filterable by type, opportunity, and team.

**FR-CRM-020** — When a past-due activity has not been marked as completed, the system shall display it in an overdue activities panel on the CRM dashboard and send a daily digest notification to the responsible user.

## 4.3 Activity Timeline

**FR-CRM-021** — Every lead, opportunity, and contact record shall display a chronological activity timeline showing all logged activities, stage changes, and field updates, in descending date order; the timeline shall be read-only and non-deletable.

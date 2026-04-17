# Typography and Colour System

## 1. Typography Scale

All text in Longhorn ERP uses the Inter typeface (loaded via Google Fonts CDN with a local fallback stack: `"Inter", "Segoe UI", Arial, sans-serif`). Monospace text uses Consolas with the fallback stack: `"Consolas", "Courier New", monospace`.

| Element | Font | Size | Weight | Colour Token | Colour Hex |
|---|---|---|---|---|---|
| Page title (H1) | Inter | 22 px | 600 | Primary Navy | #1F3864 |
| Section heading (H2) | Inter | 18 px | 600 | Primary Navy | #1F3864 |
| Sub-heading (H3) | Inter | 15 px | 600 | Body | #374151 |
| Body text | Inter | 14 px | 400 | Body | #374151 |
| Table header | Inter | 13 px | 600 | White (on navy bg) | #FFFFFF |
| Table cell | Inter | 13 px | 400 | Body | #374151 |
| Caption / helper text | Inter | 12 px | 400 | Muted | #6B7280 |
| Button label | Inter | 14 px | 500 | (inherits button variant) | — |
| Input text | Inter | 14 px | 400 | Body | #374151 |
| Placeholder text | Inter | 14 px | 400 | Muted | #9CA3AF |
| Badge / status label | Inter | 11 px | 600 | (inherits badge variant) | — |
| Monospace (code, IDs) | Consolas | 13 px | 400 | Dark | #1A1A1A |

### 1.1 Line Height and Spacing

| Element | Line Height | Paragraph Spacing |
|---|---|---|
| Body text | 1.6 | 12 px below |
| Headings H1–H3 | 1.3 | 16 px below heading, 8 px above |
| Table cells | 1.4 | — (controlled by cell padding: 10 px 12 px) |
| Caption / helper | 1.4 | 4 px above (directly below associated field) |

### 1.2 Heading Hierarchy Rules

- H1 appears once per page — the page title in the main content header.
- H2 delineates major sections within a page (e.g., "Invoice Lines", "Payment Terms").
- H3 delineates sub-sections within an H2 group (e.g., "Shipping Address" within "Customer Details").
- H4 and below are not used in the UI. Deeper hierarchy is expressed with card grouping or tab navigation, not heading levels.

## 2. Colour Palette

### 2.1 Brand and Semantic Tokens

| Token | Hex | RGB | Use |
|---|---|---|---|
| Primary Navy | #1F3864 | rgb(31, 56, 100) | Main headers, primary buttons, sidebar background, table header rows |
| Steel Blue | #2E5D8A | rgb(46, 93, 138) | Secondary action buttons, hyperlinks, hover states on navy elements |
| Accent Blue | #4472C4 | rgb(68, 114, 196) | Active navigation state highlight, selected row highlight, focus rings on non-white backgrounds |
| Success | #16A34A | rgb(22, 163, 74) | Approved and Active status badges, success toast, positive delta indicators |
| Warning | #D97706 | rgb(217, 119, 6) | Pending and Draft status badges, warning toast, amber alert banners |
| Danger | #DC2626 | rgb(220, 38, 38) | Error and Rejected status badges, error toast, destructive action buttons, validation error borders |
| Surface | #F8FAFC | rgb(248, 250, 252) | Page background, card background |
| White | #FFFFFF | rgb(255, 255, 255) | Form backgrounds, modal backgrounds, table row backgrounds (alternating with #F9FAFB) |
| Border | #E2E8F0 | rgb(226, 232, 240) | Card borders, input borders (default state), table grid lines, dividers |
| Body | #374151 | rgb(55, 65, 81) | Primary body text, input text, table cell text |
| Muted | #6B7280 | rgb(107, 114, 128) | Caption text, helper text, placeholder text (at #9CA3AF), disabled labels |
| Dark | #1A1A1A | rgb(26, 26, 26) | Monospace text |

### 2.2 Interactive State Colours

| State | Background | Border | Text |
|---|---|---|---|
| Input — default | #FFFFFF | #E2E8F0 | #374151 |
| Input — focus | #FFFFFF | #4472C4 (2 px) | #374151 |
| Input — error | #FFF5F5 | #DC2626 (2 px) | #374151 |
| Input — disabled | #F3F4F6 | #E2E8F0 | #9CA3AF |
| Button Primary — default | #1F3864 | none | #FFFFFF |
| Button Primary — hover | #2E5D8A | none | #FFFFFF |
| Button Primary — active | #1A3057 | none | #FFFFFF |
| Button Secondary — default | #FFFFFF | #E2E8F0 | #374151 |
| Button Secondary — hover | #F8FAFC | #D1D5DB | #1F3864 |
| Button Danger — default | #DC2626 | none | #FFFFFF |
| Button Danger — hover | #B91C1C | none | #FFFFFF |
| Table row — default | #FFFFFF | — | — |
| Table row — alternate | #F9FAFB | — | — |
| Table row — hover | #EFF6FF | — | — |
| Table row — selected | #DBEAFE | — | — |

### 2.3 Status Badge Colour Map

Status badges use a filled pill style (border-radius: 12 px; padding: 2 px 10 px; font-size: 11 px; font-weight: 600).

| Status Value | Background | Text Colour |
|---|---|---|
| Active | #DCFCE7 | #15803D |
| Approved | #DCFCE7 | #15803D |
| Paid | #DCFCE7 | #15803D |
| Posted | #DBEAFE | #1D4ED8 |
| Pending | #FEF3C7 | #92400E |
| Draft | #FEF3C7 | #92400E |
| Submitted | #FEF3C7 | #92400E |
| Rejected | #FEE2E2 | #991B1B |
| Void | #FEE2E2 | #991B1B |
| Reversed | #FEE2E2 | #991B1B |
| Closed | #F3F4F6 | #4B5563 |
| Archived | #F3F4F6 | #4B5563 |
| Inactive | #F3F4F6 | #4B5563 |

### 2.4 Contrast Compliance Verification

| Text Pair | Ratio | WCAG 1.4.3 Pass Level |
|---|---|---|
| Body (#374151) on Surface (#F8FAFC) | 7.8:1 | AA + AAA |
| Primary Navy (#1F3864) on White (#FFFFFF) | 11.2:1 | AA + AAA |
| White (#FFFFFF) on Primary Navy (#1F3864) | 11.2:1 | AA + AAA |
| Muted (#6B7280) on White (#FFFFFF) | 4.6:1 | AA (body) |
| Warning text (#92400E) on Warning bg (#FEF3C7) | 5.9:1 | AA |
| Danger text (#991B1B) on Danger bg (#FEE2E2) | 6.1:1 | AA |
| Success text (#15803D) on Success bg (#DCFCE7) | 5.4:1 | AA |

## 3. Iconography

Icons are sourced from Bootstrap Icons (version matching Bootstrap 5.3.0). All icons used as standalone interactive elements (no visible text label) carry an `aria-label` attribute. Icon size in navigation: 20 px. Icon size inline with body text: 16 px. Icon size in KPI cards and large display contexts: 28–32 px.

Colour: icons inherit the text colour of their container unless a semantic override applies (e.g., a delete icon in a table action column uses Danger red #DC2626).

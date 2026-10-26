# Config guide and sizing rules

## Config fields

| Key | Meaning | Example value |
|---|---|---|
| `project.name / client / client_short / vendor` | names used in text | Project X / Client A / Client A / HBLAB |
| `project.timezone / tz_short` | timezone of coverage hours | SGT (UTC+8) / SGT |
| `project.assumption_section_no` | section number in the estimate's assumption sheet | 10 |
| `currency.code / symbol` | contract currency | USD / $ |
| `currency.secondary` | optional reference currency `{code, symbol, rate, note}`; remove the key if not needed | SGD, S$, 1.28 |
| `warranty.title / months / from / covers / targets` | warranty slide; `include_slide: false` drops it | 3 months from final delivery |
| `service.start / term_months / billing / renewal / notice` | sections 1 and 9 | after 3-month warranty, 12, monthly or quarterly |
| `resources.roles[]` | `role` (short code: DEV, PM, DevOps, QA), `desc` (2-4 words), `mm_per_month, unit_price, scope`; shown as `ROLE - desc` | DEV - Maintenance & support 0.5 MM |
| `resources.pool_rule` | what happens when the pool is exceeded | review after 2 consecutive months over the pool |
| `coverage.hours / extra / outside / slide_text / channels` | section 3 | Mon-Sat 09:00-20:00 + event Sundays |
| `sla.levels[]` | `code, name, definition, response, workaround, resolution` (+ `slide_*` short texts) | P1-P4, see below |
| `included[] / excluded[] / reporting[] / client_responsibilities[]` | sections 5, 7, 8, 10 (full sentences) | |
| `change_request.threshold_md / text` | section 6 | 5 man-days |
| `slides.overview_title / cost_title / overview_bullets / scope_rows / cost_footnote` | short slide texts; `{roles_lines}` and `{coverage_slide}` are filled by the script | |

## Sizing the resources

Reference deal: e-commerce build of about 37 MM (after AI), 4 apps, 9 integrations, ~1,700 orders/month
→ DEV 0.5, PM 0.1, DevOps 0.1 MM/month (0.7 MM/month, about 1.9% of the build effort per month).

Starting rules (adjust with the user):

| Role | Rule of thumb | Notes |
|---|---|---|
| DEV - Maintenance & support | 1.2-1.5% of build MM per month, round to 0.25; minimum 0.25 | +0.25 if many third-party integrations (> 5) or a POS / payment flow; +0.25 if coverage is longer than 11 h/day or includes weekends |
| PM - Service management | about 20% of DEV MM, minimum 0.1 | ticket triage, monthly report, quarterly review, CR quotes |
| DevOps - Cloud operations | 0.1 if HBLAB runs the cloud; 0 if the client's IT runs it | monitoring, incidents, backup/restore checks, patching, cost review |
| QA - Regression test (optional) | 0.1-0.2 if releases are monthly and regression is manual | skip when automated tests cover the core flows |

Unit prices: the deal's quotation rates per role, from the user. The example config holds sample
numbers only.

## SLA defaults

| Severity | Definition | Response | Workaround | Resolution |
|---|---|---|---|---|
| P1 Critical | production down; checkout or payment unavailable; data breach | 2 h | 4 h | 1 working day |
| P2 High | major function impaired, no workaround | 4 h | 1 working day | 3 working days |
| P3 Medium | function impaired, workaround available | 1 working day | - | next release (≤ 10 working days) |
| P4 Low | cosmetic, how-to | 2 working days | - | backlog |

Tighten only if the price follows (P1 response 1 h or 24x7 cover needs an on-call rota, which is more
than 0.5 MM DEV). Write the P1 definition with the deal's own critical flows.

## Questions to ask when the deal does not say

1. Unit price per role (the quotation's rates)?
2. Coverage hours and days? Peak or event days outside them?
3. Who runs L1 support (client helpdesk)?
4. Does HBLAB operate the cloud, or the client's IT?
5. Recurring security test (VAPT / pentest)? Who arranges it?
6. Contract currency; reference currency with rate, source and date?
7. Term and notice (12 months? cancellation after 6 months?)

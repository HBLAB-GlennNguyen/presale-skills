---
name: proposing-managed-service
description: Use when a presale deal needs the paid managed service after the warranty period (post-warranty maintenance, support, SLA, O&M) defined and priced — collects the deal's inputs (from ./output/ of the earlier presale skills when present), sizes the monthly resources (DEV / PM / DevOps), writes one JSON config, and generates the standard package from it - proposal text (managed-service.md), WBS-style xlsx sheets (MS_Cost with formulas + MS_Assumption) and HBLAB-branded slides (warranty, managed service + SLA, scope & cost). Runs after estimating-effort; its output feeds the "after warranty" part of writing-proposal.
---

# Proposing Managed Service

Turn a deal's delivered scope into a priced, optional managed service after warranty. One config
(`./output/managed-service/config.json`) produces three outputs with the same numbers.

## Standard structure (10 sections, single package)

1. Overview and start: starts after warranty, term, billing, optional / not in the fixed price
2. Resources and price: role x MM/month x unit price x 12. Roles are written short, `ROLE - description`
   (`DEV - Maintenance & support`, `PM - Service management`, `DevOps - Cloud operations (Azure)`);
   the detail goes in the Scope column, never in the role name
3. Coverage hours and channels
4. Severity and SLA (P1-P4: response / workaround / resolution, counted within coverage hours)
5. Included
6. Change request threshold
7. Excluded
8. Reporting and governance
9. Resource adjustment and renewal
10. Client responsibilities

## Input

Read these from `./output/` when they exist (produced by analyzing-rfp and estimating-effort); they are
the source of truth, do not re-ask what they state:

- `requirements-summary.md`: client, timezone/country, go-live, roles & responsibilities of both sides
- `scope-and-sitemap.md`: delivered modules, third-party systems (they become "Excluded: third-party issues")
- `effort-breakdown.md`: total build effort (for sizing)
- `team-composition.md`: roles of the build team
- `risk-assessment.md`: risks that should shape the SLA or the P1 definition

If they do not exist (a deal not run through the suite), take the same facts from the user's estimate
workbook, scope file or proposal deck. Always ask the user for: the **unit price per role** (the deal's
quotation rates, never assume), coverage hours and days, peak/event days, who runs L1 support, who
operates the cloud, recurring security test (VAPT), contract and reference currency.
`reference/config-guide.md` lists the questions.

## Process

1. **Collect** the inputs above. List what came from files and what you still need, then ask the missing
   items in one message.
2. **Size the resources** with `reference/config-guide.md` (sizing rules, SLA defaults). Show the sizing
   to the user with the reason for each role; it is a proposal, not a fact.
3. **Write the config**: copy `reference/example-config.json` to `./output/managed-service/config.json`
   and change every value. Slide texts (`slides.*`) are short and curated, not generated.
4. **Build**:
   ```bash
   python3 <this skill's directory>/scripts/build_managed_service.py ./output/managed-service/config.json ./output/managed-service
   ```
   Needs Python 3 with `openpyxl` and `python-pptx`.
5. **Verify**:
   - the annual total is the same in md, xlsx and slides, and matches the deal's quotation if it already
     shows a managed service figure;
   - recalculate the xlsx with LibreOffice when available (openpyxl writes formulas without cached
     values; Excel calculates them on open) and check there are no formula errors;
   - render the pptx to images and check every slide for overflow and leftover "Placeholder" text.
6. **Report** the file paths, the monthly and annual fee, and the list of assumptions that are drafts
   the user must confirm (anything not stated by the deal's files or the user).

## Output

`./output/managed-service/`:

| File | Content | Use |
|---|---|---|
| `config.json` | all inputs | edit and rebuild |
| `managed-service.md` | 10 sections, cost table, SLA table | proposal document / review |
| `managed-service.xlsx` | `MS_Cost`: inputs (yellow), cost formulas, SLA table · `MS_Assumption`: numbered lines in the estimate's assumption-sheet format | copy into the estimate workbook |
| `managed-service.pptx` | Warranty (optional) · Managed service + SLA · Scope & cost | insert into the proposal deck |

Output language follows the config texts (the example is English, for a client-facing deck).

## Rules

- Contract currency first; a reference currency is rounded per row, totals are the sum of rows.
- The managed service is optional and outside the fixed price unless the user says otherwise; every
  output says so.
- Use the same severity names in warranty and managed service where possible; SLA times count within
  coverage hours, outside them it is best effort.
- Cloud running cost (Azure/AWS bills) is not part of this package; it stays on the deal's own
  running-cost slide.
- `assets/hblab-ms-base.pptx` holds the 3 HBLAB slide frames with placeholder text; the script finds
  shapes by id. Do not edit it by hand; if the layout must change, change the script.

## Error handling

- Unit prices missing: stop and ask; never fill rates from the example config.
- Build effort unknown: ask for it or for the build team size and duration; do not size from guesses.

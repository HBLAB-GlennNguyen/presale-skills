---
name: writing-proposal
description: Use when drafting a client-facing presale proposal outline after both analyzing-rfp and estimating-effort have been run — reads all their output files from ./output/, asks a few required clarifying questions (migration vs greenfield, technical architecture choices), and produces a single Markdown outline (design/theme brief + full slide-by-slide content) ready to feed into an AI slide-generation tool. Third and final skill in the presale suite (analyzing-rfp → estimating-effort → writing-proposal).
---

# Writing Proposal

Assemble a complete proposal outline — HBLAB branding brief plus slide-by-slide content across 6 parts (Opening, Business Value, Technical Solution, Working Model, Closing, Appendix) — from everything analyzing-rfp and estimating-effort already produced, plus a short interactive round for the handful of decisions no prior skill made (migration status, technical architecture). Output is Vietnamese; English industry terms (e.g. "Deliverables", "Quotation", "UAT") stay in English.

## Input

Always sourced from `./output/` in the current working directory:
- From analyzing-rfp: `requirements-summary.md`, `scope-and-sitemap.md`, `clarifying-questions.md`, `risk-assessment.md`
- From estimating-effort: `effort-breakdown.md`, `master-schedule.md`, `team-composition.md`

Never accept ad hoc replacement input for a missing or incomplete file — redirect the user to run the skill that produces it (see Error handling). This keeps each upstream file the single source of truth it was designed to be.

## Process

1. **Check prerequisites.** Confirm all 7 input files exist and are readable. If any is missing, stop and tell the user which skill (analyzing-rfp or estimating-effort) to run first.
2. **Ask if this is a migration/renewal project.** One direct question, no inference: "Dự án này có phải migration/renewal một hệ thống cũ không?" This decides whether Part 1 includes "As-is System" and whether Part 2 uses "To-be System" framing instead of "High-level System Architecture" (see `reference/proposal-outline-template.md`).
3. **Run the Technical Solution interactive gate.** For the architecture-heavy items in Part 2 (system architecture, technology stack, infrastructure/cloud choice), ask the user using the suggested options in `reference/tech-solution-options.md` (cloud provider, architecture style, stack) via the AskUserQuestion tool where available — always include an "Other" path for free-text answers that don't match the suggestions. Record the answers; don't guess these instead of asking.
4. **Draft Part 0 (Opening).** Cover page (client name from requirements-summary.md), an "About HBLAB" placeholder using generic boilerplate (flag it clearly as needing the user's latest company content before sending), and an Agenda — fill the Agenda in as the last step (step 9) once every part's headings are known.
5. **Draft Part 1 (Business Value)** per `reference/proposal-outline-template.md`: customer business & expectations, As-is System (only if step 2 was yes), Pain Points (synthesized, not copied verbatim), the Risk Matrix (straight from risk-assessment.md's 8 risks), Pain Points & Solution Mapping, and Business Value Impact.
6. **Draft Part 2 (Technical Solution)** per the template: phased approach with per-phase output (from master-schedule.md), module list (from scope-and-sitemap.md), To-be System / High-level Architecture and Technology Stack and Infrastructure diagram/description (from step 3's answers), QA/testing strategy (from team-composition.md's QA role + master-schedule.md's testing phase), and Warranty & Maintenance model (from `reference/warranty-communication.md`).
7. **Draft Part 3 (Working Model)** per the template: engagement model (from requirements-summary.md's contract model field), the standard 3-tier team structure org chart, Role & Responsibilities (straight from requirements-summary.md's roles table), and Communication Plan (from `reference/warranty-communication.md`).
8. **Draft Part 4 (Closing)** per the template: master schedule (straight from master-schedule.md), Deliverables (standard deliverable-type list + a brief reference back to the module list), Resource Plan (straight from team-composition.md), and Quotation (role + effort from team-composition.md/effort-breakdown.md, unit price and total left blank with a note that pricing is filled in separately).
9. **Fill in the Agenda** (deferred from step 4) using the Part titles and major headings drafted in steps 5-8.
10. **Add Part 5 (Appendix)** as a single section-header placeholder — no content, the user fills it in later.
11. Write `./output/proposal-outline.md` (create `./output/` first if it doesn't exist): the Design & Theme brief (from `reference/design-theme.md`) first, then the full Content Detail (Parts 0-5, each part opening with a section-header slide per the design brief).
12. Report the file path back to the user, noting which sections need manual follow-up before sending to the client (About HBLAB content, Technical Solution architecture review, Quotation pricing).

## Output

One file, `./output/proposal-outline.md`, in Vietnamese (industry terms stay in English). If it already exists from a previous run, overwrite it.

## Error handling

If any of the 7 prerequisite files from analyzing-rfp/estimating-effort is missing or unreadable, tell the user exactly which file and which skill produces it, then stop without writing output.

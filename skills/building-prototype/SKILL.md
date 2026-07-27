---
name: building-prototype
description: Use when a clickable HTML/CSS/JS UI prototype is needed to accompany a presale proposal — reads the function list and sitemap from analyzing-rfp's output, runs a short UI-kit QnA to capture the client's own branding (not HBLAB's), then generates one page per screen in the sitemap, with full interactivity for the main workflows and static UI + navigation for the rest. Fourth skill in the presale suite, used alongside writing-proposal (analyzing-rfp → estimating-effort → writing-proposal, with building-prototype drawing on analyzing-rfp's output independently).
---

# Building Prototype

Turn analyzing-rfp's function list and sitemap into a clickable HTML/CSS/JS prototype of the CLIENT's future software — styled with the client's own branding (gathered via QnA), not HBLAB's proposal branding.

## Input

Always sourced from `./output/requirements-summary.md` (client/industry context, for mock data flavor) and `./output/scope-and-sitemap.md` (function list + sitemap) in the current working directory — both produced by analyzing-rfp. Never accept ad hoc replacement input for missing data; redirect to analyzing-rfp instead (see Error handling).

## Process

1. **Check prerequisites.** Confirm `./output/requirements-summary.md` and `./output/scope-and-sitemap.md` exist, and that the sitemap table in scope-and-sitemap.md has at least one real row (not still the empty template row or "*Chưa có sitemap chi tiết*"). If not, stop and tell the user to complete/run analyzing-rfp first.
2. **Resume check.** If `./output/prototype/progress.md` already exists from a previous run, read it — skip screens already marked done, continue from where it left off, don't regenerate from scratch.
3. **Run the UI-kit QnA** (skip if `./output/prototype/ui-kit-brief.md` already exists from a previous run in this project — reuse it instead of asking again, unless the user asks to redo it). Ask the 6 questions in `reference/ui-kit-qna.md`, derive the color palette / typography / density / support-level per its guidance, and write the result to `./output/prototype/ui-kit-brief.md`. Generate `./output/prototype/assets/css/global.css` (CSS custom properties + reusable component classes: buttons, cards, table, form inputs, header/nav, breadcrumb, modal) from the brief.
4. **Identify main workflows.** Check `scope-and-sitemap.md` for a "Luồng nghiệp vụ chính (Workflow)" section with already-confirmed workflows (produced by a current `analyzing-rfp` run). If present, use that list directly without asking again. If absent (an older `scope-and-sitemap.md` that predates this section), propose 2-4 candidate workflows from "Danh sách chức năng/module chính" instead, present them, and ask the user to confirm, add, or remove before generating anything. Record the confirmed list — it decides which screens get full interactivity per `reference/interactivity-guide.md`.
5. **Generate each screen** in the sitemap table, one at a time, per `reference/screen-generation-guide.md` (layout, screen-type content, mock data, cross-screen navigation) and `reference/interactivity-guide.md` (full interactivity if the screen belongs to a confirmed main workflow, static UI + navigation otherwise): write `screens/<module>/<tên màn hình>/index.html`, `style.css`, `script.js` under `./output/prototype/`. After each screen, append a line to `./output/prototype/progress.md` (`- [x] <module>/<tên màn hình>`) so an interrupted run can resume.
6. **Generate the entry point.** Write `./output/prototype/index.html`: links to all screens grouped by module, using the same global styling.
7. Report the path to `./output/prototype/index.html`, the total screen count, and which workflows got full interactivity.

## Output

`./output/prototype/`, containing:
- `assets/css/global.css`, `assets/js/global.js`
- `index.html`
- `screens/<module>/<tên màn hình>/{index.html, style.css, script.js}` — one set per sitemap row
- `ui-kit-brief.md`, `progress.md`

Re-running after screens already exist resumes/extends rather than starting over (see Process step 2). If the user explicitly asks to regenerate everything, delete `./output/prototype/` first.

## Error handling

If `requirements-summary.md` or `scope-and-sitemap.md` is missing, or the sitemap has no rows, tell the user to complete analyzing-rfp first and stop without writing output.

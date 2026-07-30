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
3. **Run the UI-kit QnA** (skip if `./output/prototype/ui-kit-brief.md` already exists from a previous run in this project — reuse it instead of asking again, unless the user asks to redo it). Ask the 7 questions in `reference/ui-kit-qna.md`, derive the product name / product archetype / color palette / typography scale / spacing scale / elevation levels / icon system / support-level / reference products / interface language per its guidance, and write the result to `./output/prototype/ui-kit-brief.md`. Generate `./output/prototype/assets/css/global.css` (CSS custom properties for the full palette — primary/primary-dark/tints/accent/9-step neutral scale/semantic-with-bg-tints — plus reusable component classes: button variants (primary/accent/outline/ghost), cards, stat/KPI card with colored accent strip, badge/status pill, table, form inputs, toggle switch, tabs (for in-modal tabs and settings side-nav), colored header/nav surface incl. its collapsed/icon-rail state, a floating collapse/expand toggle button pinned outside the sidebar (`position: fixed`, straddling the sidebar/content edge — never nested inside the sidebar), a sidebar-footer Logout item, breadcrumb, modal, avatar, empty state, toast) from the brief. Also generate `./output/prototype/assets/js/global.js` with the shared chrome behavior every screen includes (sidebar collapse/expand toggle, persisted via `localStorage`, per `reference/screen-generation-guide.md`).
4. **Identify main workflows.** Check `scope-and-sitemap.md` for a "Luồng nghiệp vụ chính (Workflow)" section with already-confirmed workflows (produced by a current `analyzing-rfp` run). If present, use that list directly without asking again. If absent (an older `scope-and-sitemap.md` that predates this section), propose 2-4 candidate workflows from "Danh sách chức năng/module chính" instead, present them, and ask the user to confirm, add, or remove before generating anything. Record the confirmed list — it decides which screens get full interactivity per `reference/interactivity-guide.md`.
5. **Identify the menu grouping.** Check `scope-and-sitemap.md` for a "Thiết kế nhóm menu (Menu Grouping)" table (produced by a current `analyzing-rfp` run). If present, use it directly — it decides the sidebar's accordion group structure per `reference/screen-generation-guide.md`. If absent (an older `scope-and-sitemap.md` that predates this section), derive equivalent groups yourself from the module list (group by business purpose, not technical module name) and tell the user you inferred it. Record the confirmed grouping in `./output/prototype/ui-kit-brief.md` so every screen builds the same sidebar structure and a resumed run doesn't re-derive it differently.
6. **Identify the entry flow.** These two screens anchor the whole prototype's visual quality and are never skipped, even if absent from the sitemap table: a Đăng nhập screen if `requirements-summary.md` implies authenticated/role-based users, or a Trang chủ public screen otherwise; and a Dashboard/Trang tổng quan screen as the landing page right after login. See `reference/screen-generation-guide.md` for what each must contain.
7. **Generate the entry-flow screens first** (Đăng nhập/Trang chủ, then Dashboard), applying the full design-system and anti-wireframe bar from `reference/ui-kit-qna.md` and `reference/screen-generation-guide.md` — every other screen must stay visually consistent with these two. Then generate the rest of the sitemap table, one screen at a time, per `reference/screen-generation-guide.md` (layout, screen-type content, mock data, cross-screen navigation) and `reference/interactivity-guide.md` (full interactivity if the screen belongs to a confirmed main workflow, static UI + navigation otherwise): write `screens/<module>/<tên màn hình>/index.html`, `style.css`, `script.js` under `./output/prototype/`. After each screen (entry-flow included), append a line to `./output/prototype/progress.md` (`- [x] <module>/<tên màn hình>`) so an interrupted run can resume.
8. **Generate the entry point.** Write `./output/prototype/index.html`: links to all screens grouped by menu group, using the same global styling.
9. Report the path to `./output/prototype/index.html`, the total screen count, which workflows got full interactivity, the entry flow (Đăng nhập vs Trang chủ, plus Dashboard), and the menu groups used.

## Output

`./output/prototype/`, containing:
- `assets/css/global.css`, `assets/js/global.js`
- `index.html`
- `screens/<module>/<tên màn hình>/{index.html, style.css, script.js}` — one set per sitemap row, plus `screens/auth/dang-nhap/` (or the public home screen) and `screens/dashboard/` for the entry flow even when not listed as sitemap rows
- `ui-kit-brief.md`, `progress.md`

Re-running after screens already exist resumes/extends rather than starting over (see Process step 2). If the user explicitly asks to regenerate everything, delete `./output/prototype/` first.

## Error handling

If `requirements-summary.md` or `scope-and-sitemap.md` is missing, or the sitemap has no rows, tell the user to complete analyzing-rfp first and stop without writing output.

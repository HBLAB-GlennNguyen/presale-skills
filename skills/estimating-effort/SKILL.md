---
name: estimating-effort
description: Use when estimating effort, master schedule, and team composition for a presale deal after analyzing-rfp has already been run — reads requirements-summary.md, scope-and-sitemap.md, and risk-assessment.md from ./output/, breaks down effort bottom-up by function (or via 3-point/PERT estimation by screen for very large projects, >100 screens), applies a risk-based buffer, builds a phased master schedule, and proposes a team composition aligned with it. Second skill in the presale suite (analyzing-rfp → estimating-effort → writing-proposal).
---

# Estimating Effort

Turn analyzing-rfp's output into an effort estimate, a master schedule, and a proposed team composition aligned with that schedule — each with its own constraints/assumptions, all in Vietnamese, all in `./output/` alongside analyzing-rfp's files.

## Input

Always sourced from `./output/requirements-summary.md`, `./output/scope-and-sitemap.md`, and `./output/risk-assessment.md` in the current working directory — all three are produced by the analyzing-rfp skill and must already exist. Never accept ad hoc replacement input for missing or outdated fields: if something is missing, redirect the user back to analyzing-rfp (see Error handling) rather than asking for it here. This keeps analyzing-rfp's output the single source of truth for the whole presale suite.

## Process

1. **Check prerequisites.** Confirm `./output/requirements-summary.md`, `./output/scope-and-sitemap.md`, and `./output/risk-assessment.md` exist and are readable. If any is missing, or scope-and-sitemap.md's "Danh sách màn hình & Sitemap" total-count line is still "*Chưa có sitemap chi tiết*" / "*Chưa rõ*", or its "Danh sách chức năng/module chính" is unfilled — stop and tell the user which file/section to complete via analyzing-rfp first. Do not estimate from partial data.
2. **Choose the method** by reading the sitemap's total screen count in `scope-and-sitemap.md`:
   - **≤ 100 screens → bottom-up by function.** Use the function/module list in "Phạm vi & yêu cầu chức năng" (in scope-and-sitemap.md).
   - **> 100 screens → 3-point (PERT) by screen.** Use the "Danh sách màn hình & Sitemap" table's counted rows (Màn hình chính + Màn hình quản lý + Pop-up dạng form), in scope-and-sitemap.md.
3. **Classify and estimate each item** against `reference/complexity-benchmark.md`'s 5 tiers. Before picking a tier from criteria alone, check whether the function/screen's module matches a row in `scope-and-sitemap.md`'s "Phân tích đối tượng nghiệp vụ & vòng đời" table — if it does, use the benchmark's "Dùng bảng Phân tích đối tượng nghiệp vụ để chọn tier" section to ground the tier in that entity's field count, lifecycle, and constraints instead of guessing from the name:
   - Bottom-up: for each function, pick a tier by its criteria, then a man-day value within that tier's range (see the benchmark's guidance on picking within a range). Sum to get the pre-buffer total in man-days.
   - PERT: for each counted screen, pick a tier, take its O/M/P story points, compute `(O + 4M + P) / 6`. Sum to get the pre-buffer total in story points. Do not convert this to hours or man-days — that conversion is explicitly left for the person doing the detailed estimate.
4. **Apply the buffer.** Read `reference/buffer-rubric.md`. Look up the buffer % for the risk band stated in risk-assessment.md, add the Fixed Price + unclear-scope bonus if that combination was flagged there. Apply: `tổng sau buffer = tổng trước buffer × (1 + buffer%)`. This applies to whichever unit step 3 produced (man-days or story points).
5. **Determine project duration and build the master schedule.** Read `reference/schedule-phases.md`.
   - If requirements-summary.md's start/go-live dates are both filled in: use that as the fixed total duration.
   - If not, and the total from step 4 is in man-days (bottom-up path): self-propose a duration following the schedule-phases guide's Case 2 (team size 6-8, target ≤ 12 months), and clearly flag it as a skill-proposed timeline pending client confirmation.
   - If not, and the total from step 4 is in story points (PERT path): self-proposing isn't possible without a man-day figure. Stop this step, tell the user a timeline is required input here (either state a desired duration directly, or complete the story-point-to-man-day conversion first), and don't fabricate a schedule.
   - With a total duration in hand, split it into phases using the table in `reference/schedule-phases.md`, computing each phase's duration (and dates, if a start date is known).
6. **Propose team composition.** Read `reference/team-composition-guide.md`.
   - Bottom-up path: compute the blended FTE from the post-buffer man-day total and the duration from step 5 (client-given or self-proposed — step 5 guarantees one exists whenever this path reaches here), then headcount per role.
   - PERT path: give only the role % breakdown — headcount requires a man-day total, which doesn't exist in this path (see step 3).
   - Either path: note each role's engagement window across the phases from step 5, per the guide's "Liên kết với Master Schedule" section.
7. Write `./output/effort-breakdown.md` (create `./output/` first if it doesn't exist): method used and why, the itemized breakdown (function or screen → tier → value), pre-buffer total, buffer % and its justification (risk band, Fixed Price bonus if applied), post-buffer total, and a "Ràng buộc & giả định của ước lượng" section (e.g., benchmark tiers used, anything not covered by the current function/screen list, currency/cost explicitly out of scope).
8. Write `./output/master-schedule.md`: the phase table with durations (and dates if available), whether the timeline is client-confirmed or skill-proposed, and — if self-proposed — the team-size assumption used, under a "Ràng buộc & giả định của lịch trình" section.
9. Write `./output/team-composition.md`: the role ratio table used, the headcount table (when computable) or the ratio-only breakdown with a note on what's still needed, and the per-role phase engagement window from step 6.
10. Report all three file paths back to the user, plus the method used, the total, the buffer applied, and whether the timeline is client-confirmed or skill-proposed.

## Output

Three files in `./output/` relative to the current working directory, always in Vietnamese:
- `effort-breakdown.md`
- `master-schedule.md`
- `team-composition.md`

If `./output/` already contains these files from a previous run, overwrite them.

## Error handling

If analyzing-rfp's output is missing, unreadable, or incomplete in a way that blocks estimation (see Process step 1), tell the user exactly what's missing and which analyzing-rfp section to fill in — then stop without writing output files. If the PERT path reaches step 5 with no client timeline (see step 5's third bullet), stop there without writing `master-schedule.md` or `team-composition.md`'s headcount — still write `effort-breakdown.md`, since that part doesn't depend on timeline.

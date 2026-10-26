#!/usr/bin/env python3
"""Build the managed-service (after warranty) package from one JSON config.

Outputs, all from the same numbers:
  <out>/managed-service.md     proposal text (10 sections) for review / the proposal document
  <out>/managed-service.xlsx   MS_Cost (formula-driven) + MS_Assumption (WBS 3_Assumption format)
  <out>/managed-service.pptx   HBLAB slides: warranty (optional), managed service + SLA, scope & cost

Usage: python3 build_managed_service.py config.json out_dir
"""
import copy
import json
import os
import sys

from openpyxl import Workbook
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from pptx import Presentation
from pptx.oxml.ns import qn
from pptx.util import Inches

HERE = os.path.dirname(os.path.abspath(__file__))
BASE_PPTX = os.path.join(HERE, "..", "assets", "hblab-ms-base.pptx")


# ---------------------------------------------------------------- numbers
def money(v, sym, dec=None):
    if dec is None:
        dec = 0 if abs(v - round(v)) < 1e-9 else 2
    return f"{sym}{v:,.{dec}f}"


def compute(cfg):
    months = cfg["resources"].get("months_per_year", 12)
    rows = []
    for r in cfg["resources"]["roles"]:
        month = r["mm_per_month"] * r["unit_price"]
        year = month * months
        rows.append(dict(r, label=f"{r['role']} - {r['desc']}", month=month, year=year))
    sec = cfg["currency"].get("secondary")
    for r in rows:
        r["year_sec"] = round(r["year"] * sec["rate"], 2) if sec else None
    tot = dict(
        mm=round(sum(r["mm_per_month"] for r in rows), 4),
        month=sum(r["month"] for r in rows),
        year=sum(r["year"] for r in rows),
        year_sec=round(sum(r["year_sec"] for r in rows), 2) if sec else None,
    )
    return rows, tot


def fmt_mm(v):
    return f"{v:g}"


# ---------------------------------------------------------------- markdown
def build_md(cfg, rows, tot):
    p, cur, s = cfg["project"], cfg["currency"], cfg["service"]
    sym, code = cur["symbol"], cur["code"]
    sec = cur.get("secondary")
    L = []
    a = L.append
    a(f"# {s['name'].capitalize()}: {p['name']} ({p['client']})")
    a("")
    a(f"Optional service, {'not included in' if not s['in_fixed_price'] else 'included in'} the Fixed Price. "
      f"Annual fee **{money(tot['year'], sym)} {code}** ({money(tot['month'], sym)} / month)"
      + (f", about {money(tot['year_sec'], sec['symbol'], 2)} {sec['code']}" if sec else "") + ".")
    a("")

    a("## 1. Overview and start")
    a("")
    a(f"- Starts {s['start']}; term {s['term_months']} months, {s['billing']}.")
    a(f"- Warranty before it: {cfg['warranty']['months']} months from {cfg['warranty']['from']}.")
    a(f"- {s['renewal']}")
    if s.get("notice"):
        a(f"- {s['notice']}")
    a("")

    a("## 2. Resources and price")
    a("")
    hdr = f"| # | Role | Scope | MM / month | Unit price ({code}/MM) | {code} / month | {code} / year |"
    sep = "|---|---|---|---:|---:|---:|---:|"
    if sec:
        hdr += f" {sec['code']} / year |"
        sep += "---:|"
    a(hdr)
    a(sep)
    for i, r in enumerate(rows, 1):
        line = (f"| {i} | {r['label']} | {r['scope']} | {fmt_mm(r['mm_per_month'])} | {money(r['unit_price'], sym)} | "
                f"{money(r['month'], sym)} | {money(r['year'], sym)} |")
        if sec:
            line += f" {money(r['year_sec'], sec['symbol'], 2)} |"
        a(line)
    line = f"| | **Total** | | **{fmt_mm(tot['mm'])}** | | **{money(tot['month'], sym)}** | **{money(tot['year'], sym)}** |"
    if sec:
        line += f" **{money(tot['year_sec'], sec['symbol'], 2)}** |"
    a(line)
    a("")
    a(f"Formula: MM / month x unit price x {cfg['resources'].get('months_per_year', 12)} months."
      + (f" {sec['note']}" if sec else ""))
    a("")

    c = cfg["coverage"]
    a("## 3. Coverage hours and channels")
    a("")
    a(f"- Coverage: {c['hours']}.")
    if c.get("extra"):
        a(f"- Also: {c['extra']}.")
    a(f"- {c['outside']}")
    a(f"- Channels: {c['channels']}")
    a("")

    a(f"## 4. Severity and service levels ({cfg['sla']['counted']}, {p['tz_short']})")
    a("")
    a("| Severity | Definition | Response | Workaround | Resolution |")
    a("|---|---|---|---|---|")
    for lv in cfg["sla"]["levels"]:
        a(f"| {lv['code']} {lv['name']} | {lv['definition']} | {lv['response']} | {lv.get('workaround') or '-'} | {lv['resolution']} |")
    a("")

    def bullets(title, items):
        a(title)
        a("")
        for it in items:
            a(f"- {it}")
        a("")

    bullets("## 5. Included", cfg["included"])
    a("## 6. Change requests")
    a("")
    a(cfg["change_request"]["text"])
    a("")
    bullets("## 7. Excluded", cfg["excluded"])
    bullets("## 8. Reporting and governance", cfg["reporting"])
    a("## 9. Resource adjustment and renewal")
    a("")
    a(f"- {cfg['resources']['pool_rule']}")
    a(f"- {s['renewal']}")
    a("")
    bullets(f"## 10. {p['client_short']} responsibilities", cfg["client_responsibilities"])
    return "\n".join(L)


# ---------------------------------------------------------------- assumption lines (shared by xlsx)
def joined(items):
    """'A; b; c' - lower-case the first letter of later items unless it starts an acronym."""
    out = []
    for k, t in enumerate(items):
        if k and len(t) > 1 and t[0].isupper() and t[1].islower():
            t = t[0].lower() + t[1:]
        out.append(t)
    return "; ".join(out)


def assumption_lines(cfg):
    n = cfg["project"]["assumption_section_no"]
    c, s = cfg["coverage"], cfg["service"]
    sla = "Severity and targets ({}):\n".format(cfg["sla"]["counted"]) + "\n".join(
        f"- {lv['code']} {lv['name']} ({lv['definition']}): response {lv['response']}"
        + (f", workaround {lv['workaround']}" if lv.get("workaround") else "")
        + f", resolution {lv['resolution']}"
        for lv in cfg["sla"]["levels"])
    roles = ", ".join(f"{r['role']} {fmt_mm(r['mm_per_month'])} MM/month" for r in cfg["resources"]["roles"])
    items = [
        f"Start and term: {s['start']}; {s['term_months']} months, {s['billing']}; optional, "
        + ("not included in" if not s["in_fixed_price"] else "included in") + " the fixed price.",
        f"Coverage: {c['hours']}" + (f"; {c['extra']}" if c.get("extra") else "") + f". {c['outside']}",
        f"Channels: {c['channels']}",
        sla,
        "Included: " + joined(cfg["included"]) + ".",
        "Change requests: " + cfg["change_request"]["text"],
        "Excluded: " + joined(cfg["excluded"]) + ".",
        "Reporting: " + joined(cfg["reporting"]) + ".",
        f"Resources: {roles} (annual fee in sheet MS_Cost). {cfg['resources']['pool_rule']}",
        "Renewal: " + s["renewal"] + (" " + s["notice"] if s.get("notice") else ""),
        f"{cfg['project']['client_short']} provides: " + joined(cfg["client_responsibilities"]) + ".",
    ]
    return n, [(f"{n}.{i}", t) for i, t in enumerate(items, 1)]


# ---------------------------------------------------------------- xlsx
DARK, YEL, INPUT = "404040", "FFC20F", "FFF2CC"
thin = Side(style="thin", color="BFBFBF")
BOX = Border(left=thin, right=thin, top=thin, bottom=thin)


def style(c, bold=False, fill=None, color="000000", wrap=True, h="left", fmt=None, size=10):
    c.font = Font(name="Arial", bold=bold, color=color, size=size)
    if fill:
        c.fill = PatternFill("solid", fgColor=fill)
    c.alignment = Alignment(wrap_text=wrap, vertical="top", horizontal=h)
    c.border = BOX
    if fmt:
        c.number_format = fmt


def build_xlsx(cfg, rows, tot, path):
    p, cur = cfg["project"], cfg["currency"]
    code, sec = cur["code"], cur.get("secondary")
    wb = Workbook()
    ws = wb.active
    ws.title = "MS_Cost"
    for col, w in zip("ABCDEFGHI", (5, 38, 52, 11, 14, 14, 16, 16, 4)):
        ws.column_dimensions[col].width = w
    ws["A1"] = f"{cfg['service']['name'].capitalize()} — {p['name']} ({p['client']})"
    ws["A1"].font = Font(name="Arial", bold=True, size=14)
    ws["A2"] = "Yellow cells are inputs. Everything else is a formula."
    ws["A2"].font = Font(name="Arial", italic=True, size=9, color="7F7F7F")

    ws["B4"], ws["C4"] = "Months per year", cfg["resources"].get("months_per_year", 12)
    ws["B5"], ws["C5"] = (f"Rate {code} 1 = {sec['code']}" if sec else "Secondary currency rate"), (sec["rate"] if sec else None)
    for r in (4, 5):
        style(ws[f"B{r}"], bold=True)
        style(ws[f"C{r}"], fill=INPUT, h="right", fmt="0.00" if r == 5 else "0")
    if sec:
        ws["D5"] = sec["note"]
        ws["D5"].font = Font(name="Arial", italic=True, size=9, color="7F7F7F")

    hdr = ["#", "Role", "Scope", "MM / month", f"Unit price ({code}/MM)", f"{code} / month", f"{code} / year"]
    if sec:
        hdr.append(f"{sec['code']} / year")
    h0 = 7
    for j, t in enumerate(hdr):
        style(ws.cell(h0, 1 + j, t), bold=True, fill=DARK, color="FFFFFF", h="center")
    r0 = h0 + 1
    money_fmt = '"$"#,##0.00' if cur["symbol"] == "$" else "#,##0.00"
    for i, r in enumerate(rows):
        x = r0 + i
        vals = [i + 1, r["label"], r["scope"], r["mm_per_month"], r["unit_price"],
                f"=D{x}*E{x}", f"=F{x}*$C$4"]
        if sec:
            vals.append(f"=ROUND(G{x}*$C$5,2)")
        for j, v in enumerate(vals):
            c = ws.cell(x, 1 + j, v)
            style(c, fill=INPUT if j in (3, 4) else None, h="right" if j >= 3 else "left",
                  fmt=("0.00" if j == 3 else money_fmt if j in (4, 5, 6) else "#,##0.00" if j == 7 else None))
    last = r0 + len(rows) - 1
    t = last + 1
    tot_vals = ["", "Total", "", f"=SUM(D{r0}:D{last})", "", f"=SUM(F{r0}:F{last})", f"=SUM(G{r0}:G{last})"]
    if sec:
        tot_vals.append(f"=SUM(H{r0}:H{last})")
    for j, v in enumerate(tot_vals):
        style(ws.cell(t, 1 + j, v), bold=True, fill="FFF8DC", h="right" if j >= 3 else "left",
              fmt=("0.00" if j == 3 else money_fmt if j in (5, 6) else "#,##0.00" if j == 7 else None))
    notes = [
        f"※Starts {cfg['service']['start']}; {cfg['service']['term_months']}-month term, {cfg['service']['billing']}"
        + (" (optional, not included in the fixed price)" if not cfg["service"]["in_fixed_price"] else ""),
        f"※Formula: MM / month x unit price x months per year (C4). {cfg['resources']['pool_rule']}",
        f"※Service levels (SLA) and change request rules: see MS_Assumption section {p['assumption_section_no']}",
    ]
    for k, n in enumerate(notes):
        ws.cell(t + 2 + k, 2, n).font = Font(name="Arial", size=9)

    s0 = t + 7
    ws.cell(s0 - 1, 1, f"Service levels ({cfg['sla']['counted']}, {p['tz_short']})").font = Font(name="Arial", bold=True, size=11)
    for j, h in enumerate(["#", "Severity", "Definition", "Response", "Workaround", "Resolution"]):
        style(ws.cell(s0, 1 + j, h), bold=True, fill=DARK, color="FFFFFF", h="center")
    ws.merge_cells(start_row=s0, start_column=6, end_row=s0, end_column=7)
    for i, lv in enumerate(cfg["sla"]["levels"], 1):
        x = s0 + i
        for j, v in enumerate([lv["code"], lv["name"], lv["definition"], lv["response"], lv.get("workaround") or "-", lv["resolution"]]):
            style(ws.cell(x, 1 + j, v))
        style(ws.cell(x, 7))
        ws.merge_cells(start_row=x, start_column=6, end_row=x, end_column=7)
    ws.freeze_panes = "A8"

    # assumption sheet, same layout as WBS 3_Assumption (No | Content)
    wa = wb.create_sheet("MS_Assumption")
    wa.column_dimensions["A"].width = 8
    wa.column_dimensions["B"].width = 120
    n, lines = assumption_lines(cfg)
    style(wa.cell(1, 1, n), bold=True, fill=DARK, color="FFFFFF")
    style(wa.cell(1, 2, f"Managed service & SLA (after warranty, {'optional' if cfg['service']['optional'] else 'included'})"),
          bold=True, fill=DARK, color="FFFFFF")
    for i, (no, txt) in enumerate(lines, 2):
        style(wa.cell(i, 1, no), h="left")
        style(wa.cell(i, 2, txt))
        wa.row_dimensions[i].height = max(15, 13 * (txt.count("\n") + 1 + len(txt) // 140))
    wb.save(path)


# ---------------------------------------------------------------- pptx helpers
def shape_by_id(slide, gid):
    for sh in slide.shapes:
        if sh.name.split(";")[1:2] == [gid] or sh.name == gid:
            return sh
    raise KeyError(gid)


def set_par(par, text):
    """Replace a paragraph's text, keeping the first run's formatting; '\\n' becomes a line break."""
    p = par._p
    runs = p.findall(qn("a:r"))
    rpr = copy.deepcopy(runs[0].find(qn("a:rPr"))) if runs else None
    for el in list(p):
        if el.tag in (qn("a:r"), qn("a:br"), qn("a:fld")):
            p.remove(el)
    end = p.find(qn("a:endParaRPr"))
    for k, piece in enumerate(text.split("\n")):
        if k:
            br = p.makeelement(qn("a:br"), {})
            if rpr is not None:
                br.append(copy.deepcopy(rpr))
            _insert(p, br, end)
        r = p.makeelement(qn("a:r"), {})
        if rpr is not None:
            r.append(copy.deepcopy(rpr))
        t = r.makeelement(qn("a:t"), {})
        t.text = piece
        r.append(t)
        _insert(p, r, end)


def _insert(p, el, end):
    if end is not None:
        end.addprevious(el)
    else:
        p.append(el)


def set_text(shape_or_cell, paragraphs):
    tf = shape_or_cell.text_frame
    if isinstance(paragraphs, str):
        paragraphs = [paragraphs]
    txBody = tf._txBody
    ps = txBody.findall(qn("a:p"))
    tmpl = ps[0]
    for extra in ps[1:]:
        txBody.remove(extra)
    for k in range(1, len(paragraphs)):
        txBody.append(copy.deepcopy(tmpl))
    for par, text in zip(tf.paragraphs, paragraphs):
        set_par(par, text)


def table_rows(tbl, n_body, keep_last_as_total=False):
    """Resize body rows (between header and optional total row) to n_body by cloning/deleting."""
    trs = tbl._tbl.findall(qn("a:tr"))
    body = trs[1:-1] if keep_last_as_total else trs[1:]
    while len(body) > n_body:
        tbl._tbl.remove(body.pop())
    while len(body) < n_body:
        new = copy.deepcopy(body[-1])
        body[-1].addnext(new)
        body.append(new)


def drop_columns(tbl, keep_idx):
    grid = tbl._tbl.find(qn("a:tblGrid"))
    cols = grid.findall(qn("a:gridCol"))
    for i, gc in enumerate(cols):
        if i not in keep_idx:
            grid.remove(gc)
    for tr in tbl._tbl.findall(qn("a:tr")):
        for i, tc in enumerate(tr.findall(qn("a:tc"))):
            if i not in keep_idx:
                tr.remove(tc)


def set_col_widths(tbl, inches):
    for gc, w in zip(tbl._tbl.find(qn("a:tblGrid")).findall(qn("a:gridCol")), inches):
        gc.set("w", str(int(Inches(w))))


def fill_table(tbl, data):
    for r, row in enumerate(data):
        for c, v in enumerate(row):
            if v is not None:
                set_text(tbl.cell(r, c), v)


def build_pptx(cfg, rows, tot, path):
    p, cur, s = cfg["project"], cfg["currency"], cfg["service"]
    sym, code, sec = cur["symbol"], cur["code"], cur.get("secondary")
    prs = Presentation(BASE_PPTX)
    w_slide, ms_slide, cost_slide = prs.slides[0], prs.slides[1], prs.slides[2]
    wm = cfg["warranty"]["months"]

    # -- warranty
    if cfg["warranty"].get("include_slide", True):
        set_text(shape_by_id(w_slide, "1209"), cfg["warranty"].get("title", "Warranty"))
        set_text(shape_by_id(w_slide, "1213"), f"{wm} months")
        set_text(shape_by_id(w_slide, "1214"), f"warranty from {cfg['warranty']['from']}")
        set_text(shape_by_id(w_slide, "1215"), cfg["warranty"]["covers"])
        set_text(shape_by_id(w_slide, "1216"), cfg["warranty"]["table_title"])
        tbl = shape_by_id(w_slide, "1217").table
        tg = cfg["warranty"]["targets"]
        table_rows(tbl, len(tg))
        fill_table(tbl, [["Severity", "Response", "Target resolution"]] + [[t["severity"], t["response"], t["resolution"]] for t in tg])
    else:
        sld = prs.slides._sldIdLst
        first = sld[0]
        prs.part.drop_rel(first.rId)
        sld.remove(first)

    # -- managed service + SLA
    set_text(shape_by_id(ms_slide, "1461"), cfg["slides"]["overview_title"])
    set_text(shape_by_id(ms_slide, "1465"), money(tot["year"], sym))
    set_text(shape_by_id(ms_slide, "1466"), f"per year ({money(tot['month'], sym)} / month) · after the {wm}-month warranty")
    roles_lines = "\n".join(f"{r['role']} {fmt_mm(r['mm_per_month'])} MM" for r in rows)
    bl = [b.replace("{roles_lines}", roles_lines).replace("{coverage_slide}", cfg["coverage"]["slide_text"])
          for b in cfg["slides"]["overview_bullets"]]
    set_text(shape_by_id(ms_slide, "1467"), bl)
    set_text(shape_by_id(ms_slide, "1468"), f"Service levels ({cfg['sla']['counted']}, {p['tz_short']})")
    tbl = shape_by_id(ms_slide, "1469").table
    lv = cfg["sla"]["levels"]
    table_rows(tbl, len(lv))
    fill_table(tbl, [["Severity", "Response", "Target resolution"]] +
               [[f"{x['code']} {x['name']} ({x['slide_definition']})", x["slide_response"], x["slide_resolution"]] for x in lv])

    # -- scope & cost
    set_text(shape_by_id(cost_slide, "1438"), cfg["slides"]["cost_title"])
    set_text(shape_by_id(cost_slide, "1443"), f"Annual fee ({'optional, ' if s['optional'] else ''}after warranty)")
    tbl = shape_by_id(cost_slide, "1444").table
    table_rows(tbl, len(rows), keep_last_as_total=True)
    head = ["#", "Role", "MM / month", f"Unit price ({code}/MM)", f"Amount ({code}/year)"]
    data = [head + ([f"Amount ({sec['code']}/year)"] if sec else [])]
    for i, r in enumerate(rows, 1):
        data.append([str(i), r["label"], fmt_mm(r["mm_per_month"]), money(r["unit_price"], sym), money(r["year"], sym)]
                    + ([money(r["year_sec"], sec["symbol"], 2)] if sec else []))
    data.append(["", f"Total ({money(tot['month'], sym)} / month)", fmt_mm(tot["mm"]), "", money(tot["year"], sym)]
                + ([money(tot["year_sec"], sec["symbol"], 2)] if sec else []))
    if not sec:
        drop_columns(tbl, {0, 1, 2, 3, 4})
        set_col_widths(tbl, [0.34, 1.9, 0.65, 0.9, 0.95])
    fill_table(tbl, data)

    set_text(shape_by_id(cost_slide, "1440"), "What the service covers")
    tbl = shape_by_id(cost_slide, "1439").table
    tbl._tbl.remove(tbl._tbl.findall(qn("a:tr"))[-1])  # old highlighted total row
    sr = cfg["slides"]["scope_rows"]
    table_rows(tbl, len(sr))
    drop_columns(tbl, {0, 1, 2})
    set_col_widths(tbl, [0.3, 1.1, 3.32])
    fill_table(tbl, [["#", "Item", "Detail"]] + [[str(i), x["item"], x["detail"]] for i, x in enumerate(sr, 1)])
    for tr in tbl._tbl.findall(qn("a:tr"))[1:]:  # let rows grow with the text
        tr.set("h", str(int(Inches(0.25))))

    note = [cfg["slides"]["cost_footnote"]] + ([sec["note"]] if sec else [])
    set_text(shape_by_id(cost_slide, "SGD rate note"), " ".join(note))
    prs.save(path)


def main():
    cfg_path, out = sys.argv[1], sys.argv[2]
    with open(cfg_path, encoding="utf-8") as f:
        cfg = json.load(f)
    os.makedirs(out, exist_ok=True)
    rows, tot = compute(cfg)
    with open(os.path.join(out, "managed-service.md"), "w", encoding="utf-8") as f:
        f.write(build_md(cfg, rows, tot) + "\n")
    build_xlsx(cfg, rows, tot, os.path.join(out, "managed-service.xlsx"))
    build_pptx(cfg, rows, tot, os.path.join(out, "managed-service.pptx"))
    sec = cfg["currency"].get("secondary")
    print(f"total {tot['mm']} MM/month, {tot['month']:,.2f}/month, {tot['year']:,.2f}/year"
          + (f", {sec['code']} {tot['year_sec']:,.2f}/year" if sec else ""))
    print("written to", out)


if __name__ == "__main__":
    main()

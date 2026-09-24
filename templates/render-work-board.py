#!/usr/bin/env python3
"""Render a Work Board page from its data file.

Velocity template support. Dependency-free: Python 3.9+ standard library only.

    python3 render-work-board.py board.json                 # standalone HTML to stdout
    python3 render-work-board.py board.json --out board.html
    python3 render-work-board.py board.json --fragment      # title+style+main only (artifact hosting)
    python3 render-work-board.py board.json --check         # validate only, no output

The data file is the single source of truth; the page is derived from it. Totals, ordering,
next-due dates, and the header stamp are computed here, never typed by hand. Validation refuses
a board that breaks the contract (templates/work-board.md). Operator asks never live on the
board: an item that waits on the Operator names the desk ask (CK id) it waits on.
"""
import argparse
import calendar
import html
import json
import re
import sys
from datetime import datetime, timedelta

CANON = "v1.9.0"
KINDS = ("work", "control")
STATES = ("backlog", "committed", "doing", "blocked", "held", "done", "dropped")
OPEN_STATES = ("backlog", "committed", "doing", "blocked", "held")
CADENCES = ("daily", "weekly", "monthly", "quarterly", "annual")
SIZES = ("S", "M", "L")
BENEFITS = ("risk retired", "cost saved", "capability gained", "obligation met")
RANK = {"S": 1, "M": 2, "L": 3}
AUTOMATED = ("software", "agent", "person")
TOP_KEYS = {"project", "maintainer", "tz_label", "updated", "adopted", "desk", "theme", "theme_dark", "items"}
WORK_KEYS = {"id", "kind", "title", "owner", "state", "belongs_to", "initiative", "depends_on", "waits_on", "needed_by",
             "closed_on", "proof", "reason", "origin", "automated", "size", "benefit", "source", "uncertain"}
CONTROL_KEYS = {"id", "kind", "title", "owner", "cadence", "last_completed", "proof", "evidence", "suspended", "planned",
                "belongs_to", "initiative", "automated", "source", "uncertain"}
UNCERTAIN_RE = re.compile(r"^\s*([a-z_]+)\s*:\s*\S")
TOKENS = {
    "bg": "#f7f7f8", "surface": "#ffffff", "border": "#e2e2e6", "text": "#1b1c1f",
    "text-muted": "#5b5d66", "accent": "#2f5fd6",
    "doing": "#2f5fd6", "doing-bg": "#eaf0fc", "doing-border": "#c5d4f5",
    "committed": "#4b5563", "committed-bg": "#f0f1f4", "committed-border": "#d5d8df",
    "blocked": "#b0281f", "blocked-bg": "#fbeceb", "blocked-border": "#f0c6c2",
    "held": "#a15c00", "held-bg": "#fdf3e2", "held-border": "#f0d9ad",
    "backlog": "#6b7280", "backlog-bg": "#f7f7f8", "backlog-border": "#e2e2e6",
    "control": "#5b3fb5", "control-bg": "#f0ecfb", "control-border": "#d6ccf2",
    "done": "#1f7a4d", "done-bg": "#eaf6ef", "done-border": "#c7e8d5",
    "dropped": "#6b7280", "dropped-bg": "#f3f4f6", "dropped-border": "#e2e2e6",
    "mono-bg": "#eef0f4",
}
TOKENS_DARK = {
    "bg": "#16171a", "surface": "#1e1f23", "border": "#303239", "text": "#eceef2",
    "text-muted": "#a3a6b0", "accent": "#7fa2f7",
    "doing": "#7fa2f7", "doing-bg": "#161f33", "doing-border": "#26365a",
    "committed": "#b3b8c4", "committed-bg": "#23252b", "committed-border": "#3a3d46",
    "blocked": "#e8827a", "blocked-bg": "#2c1917", "blocked-border": "#4a2521",
    "held": "#e3a94a", "held-bg": "#2c2413", "held-border": "#4a3a17",
    "backlog": "#9aa0ad", "backlog-bg": "#1c1d21", "backlog-border": "#303239",
    "control": "#b9a3f0", "control-bg": "#211b33", "control-border": "#3b2f5c",
    "done": "#6bc796", "done-bg": "#142a1f", "done-border": "#234d35",
    "dropped": "#9aa0ad", "dropped-bg": "#1f2024", "dropped-border": "#303239",
    "mono-bg": "#26282e",
}

CSS = """
  * { box-sizing: border-box; }
  body { margin: 0; background: var(--bg); color: var(--text); font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif; line-height: 1.5; -webkit-font-smoothing: antialiased; }
  main { max-width: 820px; margin: 0 auto; padding-block: 24px 64px; padding-inline: 16px; }
  header.page-head h1 { font-size: 1.5rem; margin: 0 0 4px; }
  .updated { color: var(--text-muted); font-size: 0.9rem; margin: 0 0 16px; }
  .totals { display: grid; grid-template-columns: repeat(5, 1fr); gap: 10px; margin-bottom: 12px; }
  .counts { color: var(--text-muted); font-size: 0.86rem; margin: 0 0 28px; }
  .counts b { color: var(--text); font-weight: 600; }
  h3.grp { font-size: 0.86rem; text-transform: uppercase; letter-spacing: 0.04em; color: var(--text-muted); margin: 14px 0 8px; }
  .ledger li.unproven { background: var(--surface); border-style: dashed; color: var(--text-muted); }
  .totals .stat { background: var(--surface); border: 1px solid var(--border); border-radius: 10px; padding: 12px 14px; text-align: center; }
  .totals .stat strong { display: block; font-size: 1.6rem; line-height: 1.1; font-variant-numeric: tabular-nums; }
  .totals .stat span { color: var(--text-muted); font-size: 0.78rem; text-transform: uppercase; letter-spacing: 0.03em; }
  .totals .stat.doing strong { color: var(--doing); }
  .totals .stat.waiting strong { color: var(--blocked); }
  .totals .stat.due strong { color: var(--held); }
  .totals .stat.never strong { color: var(--blocked); }
  section.group { margin-bottom: 32px; }
  section.group > h2 { font-size: 1.05rem; margin: 0 0 4px; }
  section.group > .group-note { color: var(--text-muted); font-size: 0.88rem; margin: 0 0 14px; }
  .item { background: var(--surface); border: 1px solid var(--border); border-left-width: 4px; border-radius: 10px; padding: 14px 16px; margin-bottom: 12px; }
  .item.doing { border-left-color: var(--doing); }
  .item.committed { border-left-color: var(--committed); }
  .item.blocked { border-left-color: var(--blocked); }
  .item.held { border-left-color: var(--held); }
  .item.backlog { border-left-color: var(--backlog); }
  .item h3 { font-size: 1rem; margin: 0 0 8px; display: flex; align-items: baseline; gap: 8px; flex-wrap: wrap; }
  .id { font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; font-size: 0.85rem; padding: 1px 6px; border-radius: 5px; background: var(--mono-bg); color: var(--text-muted); }
  .item dl { margin: 0; display: grid; grid-template-columns: max-content 1fr; gap: 4px 10px; }
  .item dt { color: var(--text-muted); font-size: 0.82rem; white-space: nowrap; padding-top: 1px; }
  .item dd { margin: 0; font-size: 0.94rem; }
  .badge { display: inline-block; font-size: 0.72rem; font-weight: 600; text-transform: uppercase; letter-spacing: 0.03em; padding: 2px 8px; border-radius: 999px; margin-left: auto; }
  .item.doing .badge { background: var(--doing-bg); color: var(--doing); border: 1px solid var(--doing-border); }
  .item.committed .badge { background: var(--committed-bg); color: var(--committed); border: 1px solid var(--committed-border); }
  .item.blocked .badge { background: var(--blocked-bg); color: var(--blocked); border: 1px solid var(--blocked-border); }
  .item.held .badge { background: var(--held-bg); color: var(--held); border: 1px solid var(--held-border); }
  .item.backlog .badge { background: var(--backlog-bg); color: var(--backlog); border: 1px solid var(--backlog-border); }
  .tag { display: inline-block; font-size: 0.72rem; padding: 1px 7px; border-radius: 999px; background: var(--mono-bg); color: var(--text-muted); margin-left: 6px; }
  .tag.warn { background: var(--held-bg); color: var(--held); border: 1px solid var(--held-border); }
  .tag.benefit { background: var(--done-bg); color: var(--done); border: 1px solid var(--done-border); }
  .repair { background: var(--blocked-bg); border: 1px solid var(--blocked-border); border-radius: 10px; padding: 12px 16px; margin-bottom: 24px; }
  .repair h2 { font-size: 1rem; margin: 0 0 6px; color: var(--blocked); }
  .repair ul { margin: 0; padding-left: 18px; font-size: 0.9rem; }
  .ledger { list-style: none; margin: 0; padding: 0; }
  .ledger li { border: 1px solid var(--border); border-radius: 8px; padding: 10px 14px; margin-bottom: 8px; font-size: 0.92rem; }
  .ledger.controls li { background: var(--control-bg); border-color: var(--control-border); }
  .ledger.controls .id { color: var(--control); background: transparent; padding-left: 0; }
  .ledger.done li { background: var(--done-bg); border-color: var(--done-border); }
  .ledger.done .id { color: var(--done); background: transparent; padding-left: 0; }
  .ledger.dropped li { background: var(--dropped-bg); border-color: var(--dropped-border); }
  .ledger.dropped .id { color: var(--dropped); background: transparent; padding-left: 0; }
  .ledger .date { color: var(--text-muted); font-size: 0.85rem; }
  .overdue { color: var(--blocked); font-weight: 600; }
  a { color: var(--accent); }
  a:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }
  code { font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; font-size: 0.88rem; background: var(--mono-bg); border-radius: 5px; padding: 1px 5px; }
  footer.page-foot { color: var(--text-muted); font-size: 0.8rem; margin-top: 40px; border-top: 1px solid var(--border); padding-top: 12px; }
  @media (max-width: 560px) {
    .totals { grid-template-columns: 1fr 1fr; }
    .totals .stat:last-child { grid-column: span 2; }
    .item dl { grid-template-columns: 1fr; gap: 2px 0; }
    .item dt { padding-top: 8px; }
  }
"""


# ---------- helpers ----------

def parse_dt(value):
    if not isinstance(value, str):
        return None
    try:
        return datetime.fromisoformat(value)
    except ValueError:
        return None


def add_months(d, n):
    y = d.year + (d.month - 1 + n) // 12
    m = (d.month - 1 + n) % 12 + 1
    return d.replace(year=y, month=m, day=min(d.day, calendar.monthrange(y, m)[1]))


def next_due(last, cadence):
    if last is None:
        return None
    return {"daily": lambda d: d + timedelta(days=1), "weekly": lambda d: d + timedelta(days=7),
            "monthly": lambda d: add_months(d, 1), "quarterly": lambda d: add_months(d, 3),
            "annual": lambda d: add_months(d, 12)}[cadence](last)


def is_ref(v):
    return isinstance(v, dict) and isinstance(v.get("project"), str) and isinstance(v.get("id"), int)


# ---------- validation ----------

def validate(d):
    if not isinstance(d, dict):
        return ["top level: expected an object"]
    errs = []
    for key in ("project", "maintainer", "tz_label", "updated"):
        if not isinstance(d.get(key), str) or not d[key].strip():
            errs.append(f"top level: '{key}' is required (non-empty string)")
    if parse_dt(d.get("updated")) is None:
        errs.append("top level: 'updated' must be an ISO datetime, e.g. 2026-09-21T09:00")
    if d.get("adopted") is not None and parse_dt(d["adopted"]) is None:
        errs.append("top level: 'adopted' must be an ISO date (the day this board's discipline began) or absent")
    adopted = parse_dt(d["adopted"]) if d.get("adopted") else None
    unknown = sorted(set(d) - TOP_KEYS)
    if unknown:
        errs.append(f"top level: unknown keys {unknown}")
    items = d.get("items")
    if not isinstance(items, list):
        return errs + ["top level: 'items' must be a list (an empty board is valid)"]
    ids = [e["id"] for e in items if isinstance(e, dict) and type(e.get("id")) is int]
    idset = set(ids)
    for i, e in enumerate(items):
        if not isinstance(e, dict):
            errs.append(f"item {i}: expected an object")
            continue
        tag = f"item {i} (id {e.get('id')!r})"
        if type(e.get("id")) is not int or e["id"] < 1:
            errs.append(f"{tag}: 'id' must be a positive integer"); continue
        kind = e.get("kind", "work")
        if kind not in KINDS:
            errs.append(f"{tag}: 'kind' must be one of {KINDS}"); continue
        unknown = sorted(set(e) - (CONTROL_KEYS if kind == "control" else WORK_KEYS))
        if unknown:
            errs.append(f"{tag}: unknown fields {unknown}; provenance goes in 'source' (text) and 'uncertain' (list of what could not be confirmed)")
        if e.get("source") is not None and not isinstance(e["source"], str):
            errs.append(f"{tag}: 'source' must be a string")
        if e.get("uncertain") is not None:
            allowed = CONTROL_KEYS if kind == "control" else WORK_KEYS
            if not (isinstance(e["uncertain"], list) and all(isinstance(x, str) for x in e["uncertain"])):
                errs.append(f"{tag}: 'uncertain' must be a list of strings, each '<field>: <why it could not be confirmed>'")
            else:
                for x in e["uncertain"]:
                    m = UNCERTAIN_RE.match(x)
                    if not m or m.group(1) not in allowed:
                        errs.append(f"{tag}: uncertain entry must read '<field>: <why>' with a real field name; got {x[:50]!r}")
        for key in ("title", "owner"):
            if not isinstance(e.get(key), str) or not e[key].strip():
                errs.append(f"{tag}: '{key}' is required")
        if e.get("origin") is not None and not is_ref(e["origin"]):
            errs.append(f"{tag}: 'origin' must be {{project, id}}")
        if e.get("automated") is not None and e["automated"] not in AUTOMATED:
            errs.append(f"{tag}: 'automated' must be one of {AUTOMATED}: runs by software, runs by an agent on schedule, or runs when a person triggers it")
        if e.get("size") is not None and e["size"] not in SIZES:
            errs.append(f"{tag}: 'size' must be one of {SIZES}")
        b = e.get("benefit")
        if b is not None:
            if not (isinstance(b, dict) and b.get("kind") in BENEFITS and b.get("scale") in SIZES and (b.get("note") is None or isinstance(b["note"], str))):
                errs.append(f"{tag}: 'benefit' must be {{kind: one of {BENEFITS}, scale: S/M/L, note?: one line}}")
            elif set(b) - {"kind", "scale", "note"}:
                errs.append(f"{tag}: 'benefit' has unknown keys {sorted(set(b) - {'kind', 'scale', 'note'})}")
        if e.get("initiative") is not None and not isinstance(e["initiative"], str):
            errs.append(f"{tag}: 'initiative' must be a string")
        if kind == "control":
            if e.get("cadence") not in CADENCES:
                errs.append(f"{tag}: control 'cadence' must be one of {CADENCES}")
            lc = e.get("last_completed")
            if lc is not None and parse_dt(lc) is None:
                errs.append(f"{tag}: control 'last_completed' must be an ISO date or null")
            if lc is not None and (not isinstance(e.get("proof"), str) or not e["proof"].strip()):
                errs.append(f"{tag}: control with 'last_completed' needs 'proof' of that completion")
            if e.get("planned") is not None and not isinstance(e["planned"], bool):
                errs.append(f"{tag}: control 'planned' must be true (not yet built) or false")
            if e.get("planned") and e.get("last_completed"):
                errs.append(f"{tag}: a control cannot be both planned (not yet built) and completed")
            if e.get("evidence") is not None and not isinstance(e["evidence"], str):
                errs.append(f"{tag}: control 'evidence' must be a string (path pattern where every completion's proof lives)")
            sus = e.get("suspended")
            if sus is not None and not (isinstance(sus, dict) and parse_dt(sus.get("since")) and isinstance(sus.get("reason"), str) and sus["reason"].strip()):
                errs.append(f"{tag}: 'suspended' must be {{since: ISO date, reason}}")
            continue
        state = e.get("state")
        if state not in STATES:
            errs.append(f"{tag}: 'state' must be one of {STATES}"); continue
        closed = parse_dt(e.get("closed_on")) if isinstance(e.get("closed_on"), str) else None
        history = state == "done" and adopted is not None and closed is not None and closed < adopted
        has_belongs = isinstance(e.get("belongs_to"), str) and e["belongs_to"].strip()
        if state == "doing" and not has_belongs:
            errs.append(f"{tag}: 'doing' work must name what bounds it ('belongs_to': a tranche, issue record, control document, ADR, decision, or evidence folder)")
        if state == "done" and not has_belongs and not history:
            errs.append(f"{tag}: 'done' work must name what bounded it ('belongs_to'); closes dated before the board's 'adopted' date are exempt as history")
        deps = e.get("depends_on")
        if deps is not None:
            if not isinstance(deps, list) or not all(isinstance(x, int) for x in deps):
                errs.append(f"{tag}: 'depends_on' must be a list of item ids")
            else:
                for x in deps:
                    if x == e["id"]: errs.append(f"{tag}: an item cannot depend on itself")
                    elif x not in idset: errs.append(f"{tag}: 'depends_on' names WI-{x}, which does not exist")
        w = e.get("waits_on")
        if state == "blocked":
            if not (isinstance(w, dict) and (is_ref(w.get("ask")) or (isinstance(w.get("item"), int) and w["item"] in idset))):
                errs.append(f"{tag}: 'blocked' needs 'waits_on' naming a desk ask {{ask: {{project, id}}}} or an item {{item: WI id}}")
        elif state == "held":
            if not (isinstance(w, dict) and isinstance(w.get("event"), str) and w["event"].strip()):
                errs.append(f"{tag}: 'held' needs 'waits_on' naming an external event {{event, by?}} (a peer read-back, a statement date)")
            elif w.get("by") is not None and parse_dt(w["by"]) is None:
                errs.append(f"{tag}: 'waits_on.by' must be an ISO date")
        elif w is not None:
            errs.append(f"{tag}: 'waits_on' belongs only on 'blocked' or 'held' items; use 'depends_on' for ordering")
        if e.get("needed_by") is not None and parse_dt(e["needed_by"]) is None:
            errs.append(f"{tag}: 'needed_by' must be an ISO date/datetime or null")
        if state in ("done", "dropped"):
            if parse_dt(e.get("closed_on")) is None:
                errs.append(f"{tag}: '{state}' needs ISO 'closed_on'")
        if state == "done" and (not isinstance(e.get("proof"), str) or not e["proof"].strip()) and not history:
            errs.append(f"{tag}: 'done' needs 'proof' (an artifact in Velocity's terms: review pack, handoff packet, closeout disposition, receipt or record path); closes dated before 'adopted' are exempt and shown as operator-reported")
        if state == "dropped" and (not isinstance(e.get("reason"), str) or not e["reason"].strip()):
            errs.append(f"{tag}: 'dropped' needs 'reason'")
    if ids:
        dupes = sorted({i for i in ids if ids.count(i) > 1})
        if dupes: errs.append(f"ids: duplicated {dupes}; an id identifies one item forever")
        missing = sorted(set(range(1, max(ids) + 1)) - idset)
        if missing: errs.append(f"ids: missing {missing}; ids are never renumbered or dropped (record a dropped item instead)")
    names = []
    for key in ("theme", "theme_dark"):
        value = d.get(key, {})
        if isinstance(value, dict):
            names += list(value.keys())
        else:
            errs.append(f"top level: '{key}' must be an object of color tokens")
    for name in names:
        if name not in TOKENS:
            errs.append(f"theme: unknown token '{name}'; only these vary per project: {sorted(TOKENS)}")
    return errs


# ---------- rendering ----------

_LINK = re.compile(r"\[([^\]]+)\]\((https?://[^)\s]+)\)")
_CODE = re.compile(r"`([^`]+)`")


def inline(text):
    out = html.escape(str(text), quote=True)
    out = _LINK.sub(lambda m: f'<a href="{m.group(2)}">{m.group(1)}</a>', out)
    return _CODE.sub(lambda m: f"<code>{m.group(1)}</code>", out)


def fmt_dt(dt, tz):
    if dt.hour == 0 and dt.minute == 0:
        return f"{dt:%a %Y-%m-%d}"
    return f"{dt:%a %Y-%m-%d %H:%M} {tz}"


def wi(n):
    return f"WI-{n}"


def waits_text(w, boards):
    if is_ref(w.get("ask")):
        return f'the Operator\'s answer to {inline(w["ask"]["project"])} CK-{w["ask"]["id"]}'
    if isinstance(w.get("item"), int):
        return f'{wi(w["item"])} ({inline(boards.get(w["item"], ""))})'
    by = parse_dt(w["by"]) if w.get("by") else None
    return inline(w["event"]) + (f" — by {fmt_dt(by, '')}" if by else "")


def uncertain_tag(e):
    if not e.get("uncertain"):
        return ""
    fields = ", ".join(sorted({(UNCERTAIN_RE.match(u).group(1) if UNCERTAIN_RE.match(u) else u.split(":")[0].strip()) for u in e["uncertain"]}))
    return f'<span class="tag warn" title="{html.escape(" | ".join(e["uncertain"]), quote=True)}">unconfirmed: {inline(fields)}</span>'


def id_span(e):
    src = f' title="{html.escape(e["source"], quote=True)}"' if e.get("source") else ""
    return f'<span class="id"{src}>{wi(e["id"])}</span>'


AUTO_LABEL = {"software": "runs by software", "agent": "agent-scheduled", "person": "person-triggered"}


def render_item(e, tz, titles, unblocks=()):
    state = e["state"]
    tags = uncertain_tag(e)
    if e.get("size"): tags += f'<span class="tag">size {e["size"]}</span>'
    if e.get("benefit"):
        b = e["benefit"]; note = f' title="{html.escape(b["note"], quote=True)}"' if b.get("note") else ""
        tags += f'<span class="tag benefit"{note}>benefit {b["scale"]}: {inline(b["kind"])}</span>'
    if e.get("automated"): tags += f'<span class="tag">{AUTO_LABEL[e["automated"]]}</span>'
    if e.get("initiative"): tags += f'<span class="tag">{inline(e["initiative"])}</span>'
    head = f'<h3>{id_span(e)} {inline(e["title"])}{tags} <span class="badge">{state}</span></h3>'
    rows = [("Owner", inline(e["owner"]))]
    if e.get("belongs_to"): rows.append(("Belongs to", inline(e["belongs_to"])))
    if state in ("blocked", "held") and isinstance(e.get("waits_on"), dict):
        w = e["waits_on"]
        rows.append(("Waits on", waits_text(w, titles) + ("" if w.get("by") or w.get("ask") or w.get("item") else ' <span class="tag warn">no date</span>')))
    if e.get("depends_on"):
        rows.append(("Depends on", ", ".join(f"{wi(x)} ({inline(titles.get(x, ''))})" for x in e["depends_on"])))
    if e.get("needed_by"):
        rows.append(("Needed by", fmt_dt(parse_dt(e["needed_by"]), tz)))
    if unblocks:
        rows.append(("Unblocks", ", ".join(f"{wi(x)} ({inline(titles.get(x, ''))})" for x in unblocks)))
    if e.get("origin"):
        rows.append(("Origin", f'asked by {inline(e["origin"]["project"])}, their item {e["origin"]["id"]}'))
    dl = "".join(f"<dt>{k}</dt><dd>{v}</dd>" for k, v in rows)
    return f'<article class="item {state}">{head}<dl>{dl}</dl></article>'


def render_control(e, today):
    last = parse_dt(e["last_completed"]) if e.get("last_completed") else None
    due = next_due(last, e["cadence"])
    if e.get("suspended"):
        status = f'<strong>Suspended</strong> since {inline(e["suspended"]["since"])}: {inline(e["suspended"]["reason"])}'
    elif e.get("planned"):
        status = '<strong>Not yet built</strong> — not counted as due until it exists'
    elif due is None:
        status = '<strong>Next due:</strong> <span class="overdue">built, never run — due now</span>'
    elif due.date() < today.date():
        status = f'<strong>Next due:</strong> <span class="overdue">{due:%Y-%m-%d} (overdue)</span>'
    else:
        status = f'<strong>Next due:</strong> {due:%Y-%m-%d}'
    last_txt = f' — <strong>Last:</strong> {last:%Y-%m-%d}, proof {inline(e.get("proof", ""))}' if last else ""
    ev = f' — <strong>Evidence:</strong> <code>{inline(e["evidence"])}</code>' if e.get("evidence") else ""
    tag = f' <span class="tag">{e["cadence"]}</span>' + (f' <span class="tag">{AUTO_LABEL[e["automated"]]}</span>' if e.get("automated") else "") + uncertain_tag(e)
    return (f'<li>{id_span(e)} {inline(e["title"])}{tag} <span class="date">({inline(e["owner"])})</span>'
            f'{last_txt}{ev} — {status}</li>')


def render_done(e):
    proof = inline(e["proof"]) if e.get("proof") else '<span class="tag warn">operator-reported, no artifact (closed before the board was adopted)</span>'
    where = f' <span class="date">({inline(e["belongs_to"])})</span>' if e.get("belongs_to") else ""
    cls = "" if e.get("proof") else ' class="unproven"'
    return (f'<li{cls}>{id_span(e)} <span class="date">({inline(e.get("closed_on", "?"))}, {inline(e["owner"])})</span> '
            f'— {inline(e["title"])}{where}{uncertain_tag(e)} — <strong>Proof:</strong> {proof}</li>')


def render_dropped(e):
    return (f'<li>{id_span(e)} <span class="date">({inline(e.get("closed_on", "?"))})</span> '
            f'— {inline(e["title"])} — <strong>Reason:</strong> {inline(e.get("reason", ""))}</li>')


def css_block(tokens):
    return "".join(f"    --{k}: {v};\n" for k, v in tokens.items())


PARTIAL = '<span class="tag warn">not shown in full; see Needs repair</span>'


def shown(fn, e, *args, ledger=False):
    """Render one entry; a malformed field degrades that entry, never the page."""
    try:
        return fn(e, *args)
    except (KeyError, TypeError, ValueError, AttributeError, IndexError):
        text = f'<span class="id">{wi(e["id"])}</span> {inline(e["title"])} {PARTIAL}'
        if ledger:
            return f"<li>{text}</li>"
        state = e.get("state") if e.get("state") in STATES else ""
        return f'<article class="item {state}"><h3>{text}</h3></article>'


def init_of(e):
    name = e.get("initiative")
    return name if isinstance(name, str) and name else "no initiative"


def renderable(e):
    if not isinstance(e, dict) or not isinstance(e.get("id"), int) or not isinstance(e.get("title"), str) or not isinstance(e.get("owner"), str):
        return False
    kind = e.get("kind", "work")
    if kind == "control":
        return e.get("cadence") in CADENCES
    return kind == "work" and e.get("state") in STATES


def render(d, fragment=False, errors=(), archive_binding=None):
    tz = html.escape(str(d.get("tz_label", "")), quote=True)
    updated = parse_dt(d.get("updated")) or datetime.now()
    raw = d.get("items") if isinstance(d.get("items"), list) else []
    items = [e for e in raw if renderable(e)]
    skipped = len(raw) - len(items)
    titles = {e["id"]: e["title"] for e in items}
    work = [e for e in items if e.get("kind", "work") == "work"]
    controls = [e for e in items if e.get("kind") == "control"]
    by_state = lambda *s: [e for e in work if e["state"] in s]

    def order(entries):
        return sorted(entries, key=lambda e: (parse_dt(e.get("needed_by")) is None, parse_dt(e.get("needed_by")) or datetime.max, e["id"]))

    doing, committed = order(by_state("doing")), order(by_state("committed"))
    waiting = order(by_state("blocked", "held"))
    def rank(e):
        b = e.get("benefit") if isinstance(e.get("benefit"), dict) else {}
        scale, size = b.get("scale"), e.get("size")
        nb = parse_dt(e.get("needed_by"))
        return (-(RANK.get(scale, 0) if isinstance(scale, str) else 0), RANK.get(size, 4) if isinstance(size, str) else 4,
                nb is None, nb or datetime.max, e["id"])
    backlog = sorted(by_state("backlog"), key=rank)
    done = sorted(by_state("done"), key=lambda e: (parse_dt(e.get("closed_on")) or datetime.min, e["id"]), reverse=True)
    dropped = sorted(by_state("dropped"), key=lambda e: (parse_dt(e.get("closed_on")) or datetime.min, e["id"]), reverse=True)
    controls_sorted = sorted(controls, key=lambda e: (bool(e.get("suspended")), bool(e.get("planned")), e["id"]))

    week_end = updated + timedelta(days=7)
    due = 0
    for e in doing + committed + waiting + backlog:
        nb = parse_dt(e.get("needed_by"))
        if nb and nb <= week_end: due += 1
        w = e.get("waits_on") if isinstance(e.get("waits_on"), dict) else {}
        if e["state"] == "held" and parse_dt(w.get("by")) and parse_dt(w["by"]) <= week_end: due += 1
    never_run = 0
    for e in controls:
        if e.get("suspended") or e.get("planned"): continue
        last = parse_dt(e.get("last_completed"))
        if last is None:
            never_run += 1; continue
        if e["cadence"] == "daily": continue  # always due; would swamp the count
        if next_due(last, e["cadence"]) <= week_end: due += 1
    open_items = doing + committed + waiting + backlog
    unblocks = {}
    for e in open_items:
        for x in e.get("depends_on") if isinstance(e.get("depends_on"), list) else []:
            if isinstance(x, int):
                unblocks.setdefault(x, []).append(e["id"])
    inits = {}
    for e in open_items:
        inits[init_of(e)] = inits.get(init_of(e), 0) + 1
    peers = sum(1 for e in open_items if e.get("origin"))
    auto = {k: sum(1 for e in open_items + controls if e.get("automated") == k) for k in AUTOMATED}

    theme = d.get("theme") if isinstance(d.get("theme"), dict) else {}
    theme_dark = d.get("theme_dark") if isinstance(d.get("theme_dark"), dict) else {}
    light = dict(TOKENS, **{k: v for k, v in theme.items() if k in TOKENS})
    dark = dict(TOKENS_DARK, **{k: v for k, v in theme_dark.items() if k in TOKENS})
    style = (f"<style>\n  :root {{\n    color-scheme: light dark;\n{css_block(light)}  }}\n"
             f"  @media (prefers-color-scheme: dark) {{\n    :root:not([data-theme=\"light\"]) {{\n{css_block(dark)}    }}\n  }}\n"
             f"  :root[data-theme=\"dark\"] {{\n{css_block(dark)}  }}\n{CSS}</style>")

    def section(sid, heading, note, body):
        return (f'<section class="group" aria-labelledby="{sid}-heading"><h2 id="{sid}-heading">{heading}</h2>'
                f'<p class="group-note">{note}</p>{body}</section>')

    def cards(entries, empty, grouped=False):
        if not entries:
            return f'<p class="group-note">{empty}</p>'
        if grouped and any(e.get("initiative") for e in entries):
            out = ""
            for name in sorted({init_of(e) for e in entries}, key=lambda n: (n == "no initiative", n)):
                grp = [e for e in entries if init_of(e) == name]
                out += f'<h3 class="grp">{inline(name)} ({len(grp)})</h3>' + "".join(shown(render_item, e, tz, titles, unblocks.get(e["id"], ())) for e in grp)
            return out
        return "".join(shown(render_item, e, tz, titles, unblocks.get(e["id"], ())) for e in entries)

    def ledger(cls, entries, fn, empty, grouped=False):
        if not entries:
            return f'<p class="group-note">{empty}</p>'
        if grouped and any(e.get("initiative") for e in entries):
            out = ""
            for name in sorted({init_of(e) for e in entries}, key=lambda n: (n == "no initiative", n)):
                grp = [e for e in entries if init_of(e) == name]
                out += f'<h3 class="grp">{inline(name)} ({len(grp)})</h3><ul class="ledger {cls}">' + "".join(shown(fn, e, ledger=True) for e in grp) + "</ul>"
            return out
        return f'<ul class="ledger {cls}">' + "".join(shown(fn, e, ledger=True) for e in entries) + "</ul>"

    repair = ""
    if errors:
        lines = "".join(f"<li>{inline(x)}</li>" for x in errors)
        skip_note = f" {skipped} item(s) could not be shown at all." if skipped else ""
        repair = f'<div class="repair" role="alert"><h2>Needs repair ({len(errors)})</h2><p class="group-note">The data file breaks the contract. The page is shown best-effort so nothing is hidden; the maintainer fixes the file, not the page.{skip_note}</p><ul>{lines}</ul></div>\n'
    title = f"{d.get('project', '<Project>')} Work Board"
    desk_note = f' · desk: {inline(d["desk"])}' if d.get("desk") else ""
    archive_note = (f'<p class="repair" role="status"><strong>Archived work records.</strong> '
                    f'The authoritative tracker is identified in {inline(archive_binding)}. '
                    'This page is a retained snapshot, not the active work queue.</p>'
                    if archive_binding else "")
    main = (
        f"<main>\n<header class=\"page-head\"><h1>{inline(title)}</h1>"
        f"<p class=\"updated\">Last updated: {fmt_dt(updated, tz)} · maintained by {inline(d.get('maintainer', ''))}{desk_note}</p></header>\n"
        + archive_note + repair +
        f"<div class=\"totals\" aria-label=\"Header totals\">"
        f"<div class=\"stat doing\"><strong>{len(doing) + len(committed)}</strong><span>In motion</span></div>"
        f"<div class=\"stat waiting\"><strong>{len(waiting)}</strong><span>Waiting</span></div>"
        f"<div class=\"stat\"><strong>{len(backlog)}</strong><span>Backlog</span></div>"
        f"<div class=\"stat due\"><strong>{due}</strong><span>Due this week</span></div>"
        f"<div class=\"stat never\"><strong>{never_run}</strong><span>Controls never run</span></div></div>\n"
        f"<p class=\"counts\">Open work by initiative: " + " · ".join(f"<b>{inline(k)}</b> {v}" for k, v in sorted(inits.items(), key=lambda kv: (-kv[1], kv[0]))) + f" · <b>{peers}</b> from peers · <b>{auto['software']}</b> run by software · <b>{auto['agent']}</b> agent-scheduled · <b>{auto['person']}</b> person-triggered</p>\n"
        + section("motion", f"In motion ({len(doing) + len(committed)})", "Doing now, then committed to a date or a week. Ordered by needed-by.", cards(doing + committed, "Nothing in motion.")) + "\n"
        + section("waiting", f"Waiting ({len(waiting)})", "Blocked on a desk ask or another item, or held for an event with a date. Nothing here is forgotten; each names what it waits on.", cards(waiting, "Nothing waiting.")) + "\n"
        + section("backlog", f"Backlog ({len(backlog)})", "Wanted, not yet committed, by initiative.", cards(backlog, "Backlog is empty.", grouped=True)) + "\n"
        + section("controls", f"Controls ({len(controls)})", "Recurring assurance work. A control never leaves the board; its next due date is computed from its cadence. Daily controls are always due and are not counted in the week.", ledger("controls", controls_sorted, lambda e: render_control(e, updated), "No controls.")) + "\n"
        + section("done", f"Done ({len(done)})", "Closed with proof, newest first, by initiative. The proof is cited, not judged here; a close without an artifact is shown lighter.", ledger("done", done, render_done, "Nothing closed yet.", grouped=True)) + "\n"
        + section("dropped", f"Dropped ({len(dropped)})", "Closed without doing, newest first, with the reason. IDs never reused.", ledger("dropped", dropped, render_dropped, "Nothing dropped.")) + "\n"
        f"<footer class=\"page-foot\">Built on the Velocity Work Board template ({CANON}), rendered from the board data file. "
        f"IDs are assigned once and never renumbered. Operator decisions live on the Check-in Desk, never here.</footer>\n</main>"
    )
    head = f"<title>{inline(title)}</title>\n{style}\n"
    if fragment:
        return head + main + "\n"
    return ("<!doctype html>\n<html lang=\"en\">\n<head>\n<meta charset=\"utf-8\">\n"
            "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">\n"
            + head + "</head>\n<body>\n" + main + "\n</body>\n</html>\n")


def main(argv=None):
    ap = argparse.ArgumentParser(description="Render a Work Board from its data file.")
    ap.add_argument("data", help="board data file (JSON)")
    ap.add_argument("--out", help="write HTML here instead of stdout")
    ap.add_argument("--fragment", action="store_true", help="emit title+style+main only (for artifact hosting)")
    ap.add_argument("--check", action="store_true", help="validate only")
    ap.add_argument("--archive-binding", help="label a retained snapshot with its successor binding")
    args = ap.parse_args(argv)
    with open(args.data, encoding="utf-8") as f:
        d = json.load(f)
    errs = validate(d)
    if errs:
        print("Board data does not satisfy the contract:", file=sys.stderr)
        for e in errs:
            print("  - " + e, file=sys.stderr)
        if args.check or not isinstance(d, dict):
            return 1
        print("Rendering best-effort with a repair block; fix the data file. Exit code 1.", file=sys.stderr)
    if args.check:
        n = len(d["items"])
        print(f"ok: {d['project']} Work Board, {n} items, highest id WI-{max((e['id'] for e in d['items']), default=0)}")
        return 0
    out = render(d, fragment=args.fragment, errors=errs, archive_binding=args.archive_binding)
    if args.out:
        with open(args.out, "w", encoding="utf-8") as f:
            f.write(out)
    else:
        sys.stdout.write(out)
    return 1 if errs else 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Render an Executive Check-in Desk page from its data file.

Velocity template support. Dependency-free: Python 3.9+ standard library only.

    python3 render-checkin-desk.py desk.json                 # standalone HTML to stdout
    python3 render-checkin-desk.py desk.json --out desk.html
    python3 render-checkin-desk.py desk.json --fragment      # title+style+main only (artifact hosting)
    python3 render-checkin-desk.py desk.json --check         # validate only, no output
    python3 render-checkin-desk.py desk.json --check --require-decision-levels  # management profile

The data file is the single source of truth; the page is derived from it. Totals, ordering,
reply examples, and the header stamp are computed here, never typed by hand. Validation
refuses to render a desk that breaks the contract (templates/executive-checkin-desk.md).
Only the project name, operator, maintainer, time-zone label, and color tokens vary per
project. Any other need is a proposal to Velocity, not a local change to this file.
"""
import argparse
import html
import json
import re
import sys
from datetime import datetime, timedelta

CANON = "v2.0.0-experimental.1"
KINDS = ("decide", "do", "team")
STATES = ("open", "answered", "withdrawn")
TEAM_STATUS = ("done", "in motion", "blocked", "reversed")
DECISION_LEVELS = ("work", "initiative", "portfolio")
TOKENS = {
    "bg": "#f7f7f8", "surface": "#ffffff", "border": "#e2e2e6", "text": "#1b1c1f",
    "text-muted": "#5b5d66", "accent": "#2f5fd6",
    "decide": "#a15c00", "decide-bg": "#fdf3e2", "decide-border": "#f0d9ad",
    "do": "#b0281f", "do-bg": "#fbeceb", "do-border": "#f0c6c2",
    "team": "#2f5fd6", "team-bg": "#eaf0fc", "team-border": "#c5d4f5",
    "answered": "#1f7a4d", "answered-bg": "#eaf6ef", "answered-border": "#c7e8d5",
    "mono-bg": "#eef0f4",
}
TOKENS_DARK = {
    "bg": "#16171a", "surface": "#1e1f23", "border": "#303239", "text": "#eceef2",
    "text-muted": "#a3a6b0", "accent": "#7fa2f7",
    "decide": "#e3a94a", "decide-bg": "#2c2413", "decide-border": "#4a3a17",
    "do": "#e8827a", "do-bg": "#2c1917", "do-border": "#4a2521",
    "team": "#7fa2f7", "team-bg": "#161f33", "team-border": "#26365a",
    "answered": "#6bc796", "answered-bg": "#142a1f", "answered-border": "#234d35",
    "mono-bg": "#26282e",
}

REPAIR_CSS = """  .repair { background: var(--decide-bg); border: 1px solid var(--decide-border); border-radius: 10px; padding: 12px 16px; margin-bottom: 24px; }
  .repair h2 { font-size: 1rem; margin: 0 0 6px; color: var(--decide); }
  .repair ul { margin: 0; padding-left: 18px; font-size: 0.9rem; }
  .missing { color: var(--decide); }
"""

CSS = """
  * { box-sizing: border-box; }
  body { margin: 0; background: var(--bg); color: var(--text); font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif; line-height: 1.5; -webkit-font-smoothing: antialiased; }
  main { max-width: 780px; margin: 0 auto; padding-block: 24px 64px; padding-inline: 16px; }
  header.page-head h1 { font-size: 1.5rem; margin: 0 0 4px; }
  .updated { color: var(--text-muted); font-size: 0.9rem; margin: 0 0 16px; }
  .totals { display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px; margin-bottom: 28px; }
  .totals .stat { background: var(--surface); border: 1px solid var(--border); border-radius: 10px; padding: 12px 14px; text-align: center; }
  .totals .stat strong { display: block; font-size: 1.6rem; line-height: 1.1; font-variant-numeric: tabular-nums; }
  .totals .stat span { color: var(--text-muted); font-size: 0.78rem; text-transform: uppercase; letter-spacing: 0.03em; }
  .totals .stat.decide strong { color: var(--decide); }
  .totals .stat.do strong { color: var(--do); }
  section.group { margin-bottom: 32px; }
  section.group > h2 { font-size: 1.05rem; margin: 0 0 4px; }
  section.group > .group-note { color: var(--text-muted); font-size: 0.88rem; margin: 0 0 14px; }
  .ask { background: var(--surface); border: 1px solid var(--border); border-left-width: 4px; border-radius: 10px; padding: 14px 16px; margin-bottom: 12px; }
  .ask.decide { border-left-color: var(--decide); }
  .ask.do { border-left-color: var(--do); }
  .ask h3 { font-size: 1rem; margin: 0 0 8px; display: flex; align-items: baseline; gap: 8px; flex-wrap: wrap; }
  .ask h3 .id { font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; font-size: 0.85rem; padding: 1px 6px; border-radius: 5px; background: var(--mono-bg); color: var(--text-muted); }
  .ask dl { margin: 0; display: grid; grid-template-columns: max-content 1fr; gap: 4px 10px; }
  .ask dt { color: var(--text-muted); font-size: 0.82rem; white-space: nowrap; padding-top: 1px; }
  .ask dd { margin: 0; font-size: 0.94rem; }
  .ask dd ul { margin: 0; padding-left: 18px; }
  .ask .lean { font-weight: 600; }
  .ask.decide .lean { color: var(--decide); }
  .ask .owned { color: var(--text-muted); font-size: 0.9rem; margin: 0; }
  .badge { display: inline-block; font-size: 0.72rem; font-weight: 600; text-transform: uppercase; letter-spacing: 0.03em; padding: 2px 8px; border-radius: 999px; margin-left: auto; }
  .ask.decide .badge { background: var(--decide-bg); color: var(--decide); border: 1px solid var(--decide-border); }
  .ask.do .badge { background: var(--do-bg); color: var(--do); border: 1px solid var(--do-border); }
  .ledger { list-style: none; margin: 0; padding: 0; }
  .ledger li { border: 1px solid var(--answered-border); background: var(--answered-bg); border-radius: 8px; padding: 10px 14px; margin-bottom: 8px; font-size: 0.92rem; }
  .ledger .id { font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; color: var(--answered); font-weight: 600; }
  .ledger .date { color: var(--text-muted); font-size: 0.85rem; }
  .ledger.team li { background: var(--team-bg); border-color: var(--team-border); }
  .ledger.team .id { color: var(--team); }
  .how-to-reply { background: var(--surface); border: 1px solid var(--border); border-radius: 10px; padding: 14px 16px; }
  .how-to-reply p { margin: 0 0 10px; color: var(--text-muted); font-size: 0.9rem; }
  .how-to-reply code { background: var(--mono-bg); border-radius: 5px; padding: 2px 6px; font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; font-size: 0.88rem; }
  .how-to-reply ul { margin: 0; padding-left: 18px; }
  .how-to-reply li { margin-bottom: 4px; }
  a { color: var(--accent); }
  a:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }
  footer.page-foot { color: var(--text-muted); font-size: 0.8rem; margin-top: 40px; border-top: 1px solid var(--border); padding-top: 12px; }
  @media (max-width: 480px) {
    .totals { grid-template-columns: 1fr; }
    .ask dl { grid-template-columns: 1fr; gap: 2px 0; }
    .ask dt { padding-top: 8px; }
  }
"""


# ---------- validation ----------

def parse_dt(value):
    """ISO date or datetime (naive, in the operator's own time zone). Returns datetime or None."""
    if not isinstance(value, str):
        return None
    try:
        return datetime.fromisoformat(value)
    except ValueError:
        return None


def validate(d, require_decision_levels=False):
    if not isinstance(d, dict):
        return ["top level: expected an object"]
    errs = []
    for key in ("project", "operator", "tz_label", "maintainer", "updated"):
        if not isinstance(d.get(key), str) or not d[key].strip():
            errs.append(f"top level: '{key}' is required (non-empty string)")
    if parse_dt(d.get("updated")) is None:
        errs.append("top level: 'updated' must be an ISO datetime, e.g. 2026-09-19T21:21")
    entries = d.get("entries")
    if not isinstance(entries, list):
        return errs + ["top level: 'entries' must be a list (an empty desk is valid)"]
    ids = []
    for i, e in enumerate(entries):
        if not isinstance(e, dict):
            errs.append(f"entry {i}: expected an object")
            continue
        tag = f"entry {i} (id {e.get('id')!r})"
        if type(e.get("id")) is not int or e["id"] < 1:
            errs.append(f"{tag}: 'id' must be a positive integer")
            continue
        ids.append(e["id"])
        kind = e.get("kind")
        if kind not in KINDS:
            errs.append(f"{tag}: 'kind' must be one of {KINDS}")
            continue
        if not isinstance(e.get("title"), str) or not e["title"].strip():
            errs.append(f"{tag}: 'title' is required")
        if "decision_level" in e and e["decision_level"] not in DECISION_LEVELS:
            errs.append(f"{tag}: 'decision_level' must be one of {DECISION_LEVELS}")
        if require_decision_levels and kind == "decide" and e.get("state") == "open" and "decision_level" not in e:
            errs.append(f"{tag}: open Decide needs 'decision_level' in the management profile")
        if kind == "team":
            for key in ("date", "owner", "why"):
                if not isinstance(e.get(key), str) or not e[key].strip():
                    errs.append(f"{tag}: team entry needs '{key}'")
            if parse_dt(e.get("date")) is None:
                errs.append(f"{tag}: team 'date' must be ISO (YYYY-MM-DD)")
            if e.get("status") not in TEAM_STATUS:
                errs.append(f"{tag}: team 'status' must be one of {TEAM_STATUS} (free text goes in 'status_text')")
            continue
        state = e.get("state")
        if state not in STATES:
            errs.append(f"{tag}: 'state' must be one of {STATES}")
            continue
        if state == "open":
            if e.get("owned_by"):
                ob = e["owned_by"]
                if not (isinstance(ob, dict) and isinstance(ob.get("project"), str) and isinstance(ob.get("id"), int)):
                    errs.append(f"{tag}: 'owned_by' must be {{project, id}}")
                continue
            if not isinstance(e.get("what"), str) or not e["what"].strip():
                errs.append(f"{tag}: open ask needs 'what' (self-contained; assume no prior context)")
            if not isinstance(e.get("waits"), str) or not e["waits"].strip():
                errs.append(f"{tag}: open ask needs 'waits' (what waits or stays blocked until answered)")
            if e.get("needed_by") is not None and parse_dt(e["needed_by"]) is None:
                errs.append(f"{tag}: 'needed_by' must be an ISO datetime or null")
            if kind == "decide":
                opts = e.get("options")
                if not isinstance(opts, list) or len(opts) < 2 or not all(isinstance(o, str) for o in opts):
                    errs.append(f"{tag}: decide needs 'options' (list of at least two strings)")
                for key in ("lean", "lean_why"):
                    if not isinstance(e.get(key), str) or not e[key].strip():
                        errs.append(f"{tag}: decide needs '{key}'")
        else:
            ob = e.get("owned_by")
            if ob is not None and not (isinstance(ob, dict) and isinstance(ob.get("project"), str) and isinstance(ob.get("id"), int)):
                errs.append(f"{tag}: 'owned_by' must be {{project, id}}")
            if parse_dt(e.get("answered_on")) is None:
                errs.append(f"{tag}: {state} ask needs ISO 'answered_on'")
            if not isinstance(e.get("ruling"), str) or not e["ruling"].strip():
                errs.append(f"{tag}: {state} ask needs 'ruling'" + (" (the reason it was withdrawn)" if state == "withdrawn" else ""))
    if ids:
        dupes = sorted({i for i in ids if ids.count(i) > 1})
        if dupes:
            errs.append(f"ids: duplicated {dupes}; an id identifies one decision forever")
        missing = sorted(set(range(1, max(ids) + 1)) - set(ids))
        if missing:
            errs.append(f"ids: missing {missing}; ids are never renumbered or dropped (record a withdrawn entry instead)")
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


# ---------- rendering helpers ----------

_LINK = re.compile(r"\[([^\]]+)\]\((https?://[^)\s]+)\)")
_CODE = re.compile(r"`([^`]+)`")


def inline(text):
    """Escape everything, then allow only [text](https://url) links and `code` spans."""
    out = html.escape(str(text), quote=True)
    out = _LINK.sub(lambda m: f'<a href="{m.group(2)}">{m.group(1)}</a>', out)
    out = _CODE.sub(lambda m: f"<code>{m.group(1)}</code>", out)
    return out


def fmt_dt(dt, tz):
    if dt.hour == 0 and dt.minute == 0 and dt.second == 0:
        return f"{dt:%a %Y-%m-%d} {tz}"
    return f"{dt:%a %Y-%m-%d %H:%M} {tz}"


def fmt_date(dt):
    return f"{dt:%Y-%m-%d}"


def ck(n):
    return f"CK-{n}"


def level_label(e):
    return e["decision_level"].capitalize() if e.get("decision_level") in DECISION_LEVELS else ""


def ledger_level(e):
    return f' <span class="date">· Decision level: {level_label(e)}</span>' if level_label(e) else ""


def render_open(e, tz):
    kind = e["kind"]
    badge = "Decide" if kind == "decide" else "Do"
    head = f'<h3><span class="id">{ck(e["id"])}</span> {inline(e["title"])} <span class="badge">{badge}</span></h3>'
    if valid_pointer(e.get("owned_by")):
        ob = e["owned_by"]
        level = f'<p class="owned">Decision level: {level_label(e)}</p>' if level_label(e) else ""
        return (f'<article class="ask {kind}">{head}'
                f'{level}'
                f'<p class="owned">Owned by {inline(ob["project"])} {ck(ob["id"])}. Answer it there; this entry closes with it.</p></article>')
    rows = [("Decision level", level_label(e))] if level_label(e) else []
    rows.append(("What it is", field(e, "what")))
    if kind == "decide":
        opts = e.get("options")
        opts = "<ul>" + "".join(f"<li>{inline(o)}</li>" for o in opts) + "</ul>" if isinstance(opts, list) and opts else MISSING
        rows.append(("Options", opts))
        rows.append(("Lean", f'<span class="lean">{field(e, "lean")}</span> — {field(e, "lean_why")}'))
    nb = parse_dt(e.get("needed_by"))
    when = fmt_dt(nb, tz) if nb else "no date"
    rows.append(("Needed by", f"{when} — {field(e, 'waits')}"))
    dl = "".join(f"<dt>{k}</dt><dd>{v}</dd>" for k, v in rows)
    return f'<article class="ask {kind}">{head}<dl>{dl}</dl></article>'


def render_team(e):
    status = field(e, "status") + (f": {inline(e['status_text'])}" if e.get("status_text") else "")
    return (f'<li><span class="id">{ck(e["id"])}</span> <span class="date">({inline(e["date"])}, {field(e, "owner")})</span>{ledger_level(e)} '
            f'— {inline(e["title"])} — <strong>Why:</strong> {field(e, "why")} — <strong>Status:</strong> {status}</li>')


def render_answered(e):
    text = e.get("ruling") if isinstance(e.get("ruling"), str) else ""
    if e["state"] == "withdrawn":
        text = re.sub(r"^\s*withdrawn\s*[—–:-]\s*", "", text, flags=re.I)  # tolerate a repeated leading word
        text = "withdrawn — " + text
    ruling = inline(text) if text.strip() else MISSING
    owner = ""
    if valid_pointer(e.get("owned_by")):
        ob = e["owned_by"]
        owner = f' <span class="date">(owned by {inline(ob["project"])} {ck(ob["id"])})</span>'
    return (f'<li><span class="id">{ck(e["id"])}</span> <span class="date">({inline(e["answered_on"])})</span>{ledger_level(e)} '
            f'— {inline(e["title"])} — <strong>Ruling:</strong> {ruling}{owner}</li>')


MISSING = '<em class="missing">missing; see Needs repair</em>'


def field(e, key):
    v = e.get(key)
    return inline(v) if isinstance(v, str) and v.strip() else MISSING


def valid_pointer(ob):
    return isinstance(ob, dict) and isinstance(ob.get("project"), str) and isinstance(ob.get("id"), int)


def renderable(e):
    """An entry the page can place: identity, kind, title, and the date or state that places it."""
    if not isinstance(e, dict) or type(e.get("id")) is not int or e["id"] < 1:
        return False
    if e.get("kind") not in KINDS or not isinstance(e.get("title"), str):
        return False
    if e["kind"] == "team":
        return parse_dt(e.get("date")) is not None
    if e.get("state") not in STATES:
        return False
    return e["state"] == "open" or parse_dt(e.get("answered_on")) is not None


def sort_open(entries):
    def key(e):
        nb = parse_dt(e.get("needed_by"))
        return (nb is None, nb or datetime.max, e["id"])
    return sorted(entries, key=key)


def css_block(tokens):
    return "".join(f"    --{k}: {v};\n" for k, v in tokens.items())


def render(d, fragment=False, errors=()):
    tz = html.escape(str(d.get("tz_label", "")), quote=True)
    updated = parse_dt(d.get("updated")) or datetime.now().replace(second=0, microsecond=0)
    raw = d.get("entries") if isinstance(d.get("entries"), list) else []
    entries = [e for e in raw if renderable(e)]
    skipped = len(raw) - len(entries)
    open_decide = [e for e in entries if e["kind"] == "decide" and e["state"] == "open" and not valid_pointer(e.get("owned_by"))]
    open_do = [e for e in entries if e["kind"] == "do" and e["state"] == "open" and not valid_pointer(e.get("owned_by"))]
    pointers = [e for e in entries if e["kind"] in ("decide", "do") and e["state"] == "open" and valid_pointer(e.get("owned_by"))]
    team = sorted([e for e in entries if e["kind"] == "team"], key=lambda e: (parse_dt(e["date"]), e["id"]), reverse=True)
    answered = sorted([e for e in entries if e["kind"] in ("decide", "do") and e.get("state") in ("answered", "withdrawn")],
                      key=lambda e: (parse_dt(e["answered_on"]), e["id"]), reverse=True)
    week_end = updated + timedelta(days=7)
    deadlines = sum(1 for e in open_decide + open_do
                    if parse_dt(e.get("needed_by")) and updated <= parse_dt(e["needed_by"]) <= week_end)

    theme = d.get("theme") if isinstance(d.get("theme"), dict) else {}
    theme_dark = d.get("theme_dark") if isinstance(d.get("theme_dark"), dict) else {}
    light = dict(TOKENS, **{k: v for k, v in theme.items() if k in TOKENS})
    dark = dict(TOKENS_DARK, **{k: v for k, v in theme_dark.items() if k in TOKENS})
    style = (f"<style>\n  :root {{\n    color-scheme: light dark;\n{css_block(light)}  }}\n"
             f"  @media (prefers-color-scheme: dark) {{\n    :root:not([data-theme=\"light\"]) {{\n{css_block(dark)}    }}\n  }}\n"
             f"  :root[data-theme=\"dark\"] {{\n{css_block(dark)}  }}\n{CSS}{REPAIR_CSS if errors else ''}</style>")

    def section(sid, heading, note, body):
        return (f'<section class="group" aria-labelledby="{sid}-heading"><h2 id="{sid}-heading">{heading}</h2>'
                f'<p class="group-note">{note}</p>{body}</section>')

    empty = '<p class="group-note">Nothing is waiting on you.</p>'
    decide_body = "".join(render_open(e, tz) for e in sort_open(open_decide) + [p for p in pointers if p["kind"] == "decide"]) or empty
    do_body = "".join(render_open(e, tz) for e in sort_open(open_do) + [p for p in pointers if p["kind"] == "do"]) or empty
    team_body = ('<ul class="ledger team">' + "".join(render_team(e) for e in team) + "</ul>") if team else '<p class="group-note">No team decisions recorded yet.</p>'
    answered_body = ('<ul class="ledger">' + "".join(render_answered(e) for e in answered) + "</ul>") if answered else '<p class="group-note">Nothing answered yet.</p>'

    examples = []
    for e in open_decide[:2]:
        examples.append(f"<code>{ck(e['id'])} fine</code> · <code>{ck(e['id'])} no, use &lt;alternative&gt;</code>")
    for e in open_do[:2]:
        examples.append(f"<code>{ck(e['id'])} done</code>")
    if team:
        examples.append(f"<code>{ck(team[0]['id'])} revisit</code> to reopen a team decision")
    if not examples:
        examples.append("<code>CK-&lt;n&gt; fine</code> · <code>CK-&lt;n&gt; no, use &lt;alternative&gt;</code> · <code>CK-&lt;n&gt; done</code>")
    reply_body = ('<div class="how-to-reply"><p>Reply by ID, in chat. Examples:</p><ul>'
                  + "".join(f"<li>{x}</li>" for x in examples) + "</ul></div>")

    repair = ""
    if errors:
        lines = "".join(f"<li>{inline(x)}</li>" for x in errors)
        skip_note = f" {skipped} entr{'y' if skipped == 1 else 'ies'} could not be placed on the page at all." if skipped else ""
        repair = (f'<div class="repair" role="alert"><h2>Needs repair ({len(errors)})</h2><p class="group-note">'
                  f'The data file breaks the contract. The page is shown best-effort so no open ask is hidden; '
                  f'the maintainer fixes the file, not the page.{skip_note}</p><ul>{lines}</ul></div>\n')
    title = f"{d.get('project') or '<Project>'} Check-in Desk"
    main = (
        f"<main>\n<header class=\"page-head\"><h1>{inline(title)}</h1>"
        f"<p class=\"updated\">Last updated: {fmt_dt(updated, tz)} · operator {inline(d.get('operator', ''))} · maintained by {inline(d.get('maintainer', ''))}</p></header>\n"
        + repair +
        f"<div class=\"totals\" aria-label=\"Header totals\">"
        f"<div class=\"stat decide\"><strong>{len(open_decide)}</strong><span>Decisions waiting</span></div>"
        f"<div class=\"stat do\"><strong>{len(open_do)}</strong><span>Actions only you can take</span></div>"
        f"<div class=\"stat\"><strong>{deadlines}</strong><span>Deadlines this week</span></div></div>\n"
        + section("decide", "Decide", "Decisions only you can make. Each stays open until you answer it.", decide_body) + "\n"
        + section("do", "Do", "Actions only you can take. Nothing here can be delegated back to a delivery role.", do_body) + "\n"
        + section("team", "Decided by the team", "Decisions made within the team's own authority. Made, owned, and recorded here so you can see them; reply by ID if you want one revisited.", team_body) + "\n"
        + section("answered", "Already answered", "Closed asks, newest first. Dated, kept forever, IDs never reused.", answered_body) + "\n"
        + section("reply", "How to reply", "Reply by ID, in chat.", reply_body) + "\n"
        f"<footer class=\"page-foot\">Built on the Velocity Executive Check-in Desk template ({CANON}), rendered from the desk data file. "
        f"IDs are assigned once and never renumbered. Republished the same turn anything changes. Silence is never consent.</footer>\n</main>"
    )
    head = f"<title>{inline(title)}</title>\n{style}\n"
    if fragment:
        return head + main + "\n"
    return ("<!doctype html>\n<html lang=\"en\">\n<head>\n<meta charset=\"utf-8\">\n"
            "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">\n"
            + head + "</head>\n<body>\n" + main + "\n</body>\n</html>\n")


def main(argv=None):
    ap = argparse.ArgumentParser(description="Render an Executive Check-in Desk from its data file.")
    ap.add_argument("data", help="desk data file (JSON)")
    ap.add_argument("--out", help="write HTML here instead of stdout")
    ap.add_argument("--fragment", action="store_true", help="emit title+style+main only (for artifact hosting)")
    ap.add_argument("--check", action="store_true", help="validate only")
    ap.add_argument("--require-decision-levels", action="store_true",
                    help="require work/initiative/portfolio qualification on every open Decide, including pointers")
    args = ap.parse_args(argv)
    with open(args.data, encoding="utf-8") as f:
        d = json.load(f)
    errs = validate(d, require_decision_levels=args.require_decision_levels)
    if errs:
        print("Desk data does not satisfy the contract:", file=sys.stderr)
        for e in errs:
            print("  - " + e, file=sys.stderr)
        if args.check or not isinstance(d, dict):
            return 1
        print("Rendering best-effort with a repair block; fix the data file. Exit code 1.", file=sys.stderr)
    if args.check:
        n = len(d["entries"])
        print(f"ok: {d['project']} Check-in Desk, {n} entries, highest id CK-{max((e['id'] for e in d['entries']), default=0)}")
        return 0
    out = render(d, fragment=args.fragment, errors=errs)
    if args.out:
        with open(args.out, "w", encoding="utf-8") as f:
            f.write(out)
    else:
        sys.stdout.write(out)
    return 1 if errs else 0


if __name__ == "__main__":
    sys.exit(main())

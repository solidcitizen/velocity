#!/usr/bin/env python3
"""Run a synthetic Desk/Work update and tracker-snapshot comparison; no external writes."""
import argparse
import json
from pathlib import Path
import subprocess
import sys

TOOL = Path(__file__).resolve().parents[2] / "templates" / "project-records.py"


def run(*args):
    result = subprocess.run([sys.executable, str(TOOL), *map(str, args)],
                            check=True, capture_output=True, text=True)
    return json.loads(result.stdout)


def read(path):
    return json.loads(path.read_text())


def write(path, value):
    path.write_text(json.dumps(value, indent=2) + "\n")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("directory", type=Path, help="new or empty demo directory")
    args = parser.parse_args()
    directory = args.directory.resolve()
    if directory.exists() and any(directory.iterdir()):
        parser.error("demo directory must be new or empty")
    directory.mkdir(parents=True, exist_ok=True)
    workspace = directory / "records"
    run("init", workspace, "--project-id", "example-app", "--project", "Example App (synthetic)",
        "--operator", "Example owner", "--maintainer", "Example delivery lead")
    desk = read(workspace / "checkin/desk.json")
    board = read(workspace / "work/board.json")
    # Deliberate mapping of a tiny known fixture, not a general TODO parser.
    history = workspace / "history"
    history.mkdir()
    (history / "TODO-2026-09-21.md").write_bytes(Path(__file__).with_name("TODO.snapshot.md").read_bytes())
    board["adopted"] = "2026-09-21"
    desk["entries"] = [{"id": 1, "kind": "decide", "state": "open", "decision_level": "work", "title": "Choose the first import scope",
                        "what": "Synthetic scenario: decide whether the next test import includes completed history.",
                        "options": ["Include work and history", "Start with open work"], "lean": "Include work and history",
                        "lean_why": "Exercises history preservation", "waits": "WI-1 waits for this decision"}]
    board["items"] = [{"id": 1, "title": "Rehearse importing the example work records", "owner": "Example delivery lead",
                        "state": "blocked", "belongs_to": "Synthetic qualification scenario",
                        "waits_on": {"ask": {"project": desk["project"], "id": 1}}},
                       {"id": 2, "title": "Collect feedback on the example board", "owner": "Unassigned",
                        "state": "backlog", "source": "history/TODO-2026-09-21.md:3",
                        "uncertain": ["owner: not stated in source", "needed_by: not stated in source"]},
                       {"id": 3, "title": "Draft the example outline", "owner": "Unassigned", "state": "done",
                        "closed_on": "2026-09-20", "source": "history/TODO-2026-09-21.md:4",
                        "uncertain": ["owner: not stated in source", "proof: historical checkbox, no evidence recorded"]}]

    def apply(operation, actor, updates):
        current = run("status", workspace)
        request = {"operation_id": operation, "actor": actor, "reason": "Synthetic example, no live decision",
                   "authority_reference": "Synthetic owner/role fixture, not operational approval",
                   "base_revisions": {name: value["revision"] for name, value in current["resources"].items()},
                   "updates": updates}
        path = directory / (operation + ".json")
        write(path, request)
        return run("apply", workspace, path)

    apply("create", "First command-line session", {"desk": desk, "work": board})
    desk = read(workspace / "checkin/desk.json")
    board = read(workspace / "work/board.json")
    desk["entries"] = [{"id": 1, "kind": "decide", "state": "answered", "decision_level": "work", "title": "Choose the first import scope",
                        "answered_on": "2026-09-21", "ruling": "Synthetic owner chose work and history; fixture only."}]
    board["items"][0].pop("waits_on")
    board["items"][0]["state"] = "committed"
    board["items"][0]["needed_by"] = "2026-09-28"
    apply("answer", "Fresh second command-line session", {"desk": desk, "work": board})
    bundle_path = directory / "export.json"
    exported = run("export", workspace, bundle_path)
    bundle = read(bundle_path)
    snapshot = {"format_version": 1, "project_id": "example-app", "bundle_revision": exported["bundle_revision"],
                "destination": "Synthetic destination fixture", "destination_revision": "fixture-1",
                "readback_evidence": "Generated locally for comparison; no remote read occurred",
                "items": [{"source_id": item["id"], "destination_id": str(480 + item["id"]),
                           "disposition": "imported", "normalized_record": item}
                          for item in bundle["records"]["work"]["items"]]}
    snapshot_path = directory / "destination-fixture.json"
    write(snapshot_path, snapshot)
    compared = run("handoff-check", bundle_path, snapshot_path)
    print(json.dumps({"workspace": str(workspace), "desk": str(workspace / "views/desk.html"),
                      "board": str(workspace / "views/board.html"), "comparison": compared,
                      "proof_limit": "Local processes and a synthetic destination; not two AI vendors or a live tracker."}, indent=2))


if __name__ == "__main__":
    main()

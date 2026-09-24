#!/usr/bin/env python3
"""Cooperating-writer updates for project-owned Desk and Work Board files.

Python 3.9+, standard library; local POSIX filesystems only. This is not an
authorization service. Protect the workspace and invocation through the project's
existing role/access controls. See project-records.md for the trust boundary.
"""
import argparse
from contextlib import contextmanager
from datetime import datetime, timezone
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import re
import sys
import tempfile
from zoneinfo import ZoneInfo

sys.dont_write_bytecode = True
BASE = Path(__file__).resolve().parent
RESOURCE_TYPES = {"desk": ("render-checkin-desk.py", "entries"),
                  "work": ("render-work-board.py", "items")}


class RecordError(Exception):
    pass


def canonical(value):
    return json.dumps(value, sort_keys=True, ensure_ascii=False, allow_nan=False,
                      separators=(",", ":")).encode("utf-8")


def digest(value):
    return hashlib.sha256(canonical(value)).hexdigest()


def byte_digest(value):
    return hashlib.sha256(value).hexdigest()


def pairs(items):
    obj = {}
    for key, value in items:
        if key in obj:
            raise RecordError(f"duplicate JSON key: {key}")
        obj[key] = value
    return obj


def read(path):
    def bad_constant(value):
        raise RecordError(f"non-JSON number: {value}")
    return json.loads(Path(path).read_text(encoding="utf-8"), object_pairs_hook=pairs,
                      parse_constant=bad_constant)


def atomic_bytes(path, data, exclusive=False):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, name = tempfile.mkstemp(prefix=".pending-", dir=path.parent)
    try:
        with os.fdopen(fd, "wb") as out:
            out.write(data)
            out.flush()
            os.fsync(out.fileno())
        if exclusive:
            os.link(name, path)  # atomic create-if-absent; never replaces another snapshot
        else:
            os.replace(name, path)
        directory = os.open(path.parent, os.O_RDONLY)
        try:
            os.fsync(directory)
        finally:
            os.close(directory)
    finally:
        if os.path.exists(name):
            os.unlink(name)


def write(path, value, exclusive=False):
    atomic_bytes(path, (json.dumps(value, indent=2, ensure_ascii=False,
                                  allow_nan=False) + "\n").encode("utf-8"), exclusive=exclusive)


def required_text(value, label):
    if not isinstance(value, str) or not value.strip():
        raise RecordError(f"{label}: non-empty text required")
    return value


def inside(root, relative):
    root = Path(root).resolve()
    required_text(relative, "path")
    if Path(relative).is_absolute():
        raise RecordError("workspace paths must be relative")
    path = (root / relative).resolve()
    if root not in path.parents:
        raise RecordError(f"path escapes workspace: {relative}")
    return path


def load_config(root):
    root = Path(root).resolve()
    config = read(root / "records.json")
    if not isinstance(config, dict) or config.get("format_version") != 1:
        raise RecordError("records.json: expected format_version 1")
    required_text(config.get("project_id"), "project_id")
    if config.get("mode") not in ("file", "external-tracker"):
        raise RecordError("records.json: unknown mode")
    ZoneInfo(config["timezone"])
    if set(config.get("resources", {})) != set(RESOURCE_TYPES):
        raise RecordError("records.json must bind desk and work")
    paths = [root / "records.json"]
    for spec in config["resources"].values():
        for field in ("source", "view"):
            path = inside(root, spec[field])
            if (root / ".records") == path or (root / ".records") in path.parents:
                raise RecordError("resource paths cannot use .records history storage")
            paths.append(path)
    if len(set(paths)) != len(paths):
        raise RecordError("source/view/config paths must be distinct")
    if config["mode"] == "external-tracker":
        required_text(config.get("tracker_binding"), "tracker_binding")
    if not isinstance(config.get("desk_requires_decision_levels", False), bool):
        raise RecordError("records.json: desk_requires_decision_levels must be true or false")
    return config


@contextmanager
def locked(root):
    try:
        import fcntl
    except ImportError:
        raise RecordError("guarded updates require a local POSIX filesystem")
    if not root.is_dir():
        raise RecordError("workspace does not exist")
    state = inside(root, ".records")
    state.mkdir(exist_ok=True)
    with (state / "lock").open("a+b") as lock:
        fcntl.flock(lock, fcntl.LOCK_EX)
        try:
            yield
        finally:
            fcntl.flock(lock, fcntl.LOCK_UN)


def renderer(name):
    path = BASE / RESOURCE_TYPES[name][0]
    spec = importlib.util.spec_from_file_location("velocity_" + name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def tool_revision():
    return digest({p.name: byte_digest(p.read_bytes()) for p in
                   [Path(__file__).resolve()] + [BASE / v[0] for v in RESOURCE_TYPES.values()]})


def validate(name, data, config=None):
    try:
        strict = bool(config and config.get("desk_requires_decision_levels"))
        options = {"require_decision_levels": True} if name == "desk" and strict else {}
        errors = renderer(name).validate(data, **options)
    except (TypeError, ValueError, KeyError, AttributeError) as exc:
        raise RecordError(f"{name}: invalid record shape: {exc}")
    if errors:
        raise RecordError(f"{name}: " + "; ".join(errors))


def sources(root, config):
    return {name: read(inside(root, spec["source"]))
            for name, spec in config["resources"].items()}


def validate_links(data):
    desk = data["desk"]
    asks = {entry["id"]: entry for entry in desk["entries"]}
    for item in data["work"]["items"]:
        ref = (item.get("waits_on") or {}).get("ask")
        if ref and ref["project"] == desk["project"]:
            ask = asks.get(ref["id"])
            if not ask or ask["kind"] not in ("decide", "do"):
                raise RecordError(f"WI-{item['id']} references a missing local Desk ask")


def operations(root):
    return sorted((root / ".records" / "operations").glob("*.json"))


def pending(root):
    return [path.stem for path in operations(root) if read(path)["state"] != "complete"]


def op_path(root, operation_id):
    if not isinstance(operation_id, str) or not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_-]{0,95}", operation_id):
        raise RecordError("operation_id must be 1-96 letters, digits, underscores or hyphens")
    return root / ".records" / "operations" / (operation_id + ".json")


def status(root, config):
    data = sources(root, config)
    receipt_path = root / ".records" / "views.json"
    views = read(receipt_path) if receipt_path.exists() else {}
    result = {"project_id": config["project_id"], "mode": config["mode"],
              "pending_operations": pending(root), "resources": {}}
    for name, value in data.items():
        view = inside(root, config["resources"][name]["view"])
        receipt = views.get(name, {})
        rev = digest(value)
        current = (view.is_file() and receipt.get("source_revision") == rev
                   and receipt.get("output_sha256") == byte_digest(view.read_bytes())
                   and receipt.get("config_revision") == digest(config)
                   and receipt.get("tool_revision") == tool_revision())
        result["resources"][name] = {"revision": rev, "view_current": current,
                                    "source": config["resources"][name]["source"],
                                    "view": config["resources"][name]["view"],
                                    "authority": "archive" if name == "work" and config["mode"] == "external-tracker" else "file"}
    if config["mode"] == "external-tracker":
        result["tracker_binding"] = config["tracker_binding"]
    return result


def publish(root, config, data):
    receipts = {}
    for name, value in data.items():
        options = ({"archive_binding": config["tracker_binding"]}
                   if name == "work" and config["mode"] == "external-tracker" else {})
        output = renderer(name).render(value, **options).encode("utf-8")
        atomic_bytes(inside(root, config["resources"][name]["view"]), output)
        receipts[name] = {"source_revision": digest(value),
                          "output_sha256": byte_digest(output),
                          "config_revision": digest(config),
                          "tool_revision": tool_revision()}
    write(root / ".records" / "views.json", receipts)


def resume(root, config, path):
    op = read(path)
    if op["state"] == "complete":
        return {"operation_id": op["operation_id"], "state": "complete", "replayed": True,
                "current": status(root, config)}
    if op["config_revision"] != digest(config) or op["tool_revision"] != tool_revision():
        raise RecordError("configuration/tool changed during pending operation; restore its pin before recovery")
    data = sources(root, config)
    # Check all sources before writing any: recovery never overwrites divergent work.
    for name, value in data.items():
        allowed = {digest(op["before"][name]), digest(op["after"][name])}
        if digest(value) not in allowed:
            raise RecordError(f"{name}: source diverged; reconcile before recovery")
    try:
        # Desk first: a coupled work release can never precede its recorded decision.
        for name in RESOURCE_TYPES:
            value = op["after"][name]
            if digest(data[name]) != digest(value):
                write(inside(root, config["resources"][name]["source"]), value)
        op["state"] = "source_saved"
        write(path, op)
        observed = sources(root, config)
        if observed != op["after"]:
            raise RecordError("source read-back mismatch")
        publish(root, config, observed)
        op["state"] = "complete"
        op.pop("error", None)
        write(path, op)
    except Exception as exc:
        op["error"] = str(exc)
        write(path, op)
        raise RecordError(f"operation {op['operation_id']} pending ({op['state']}): {exc}; run recover")
    return {"operation_id": op["operation_id"], "state": "complete",
            "current": status(root, config)}


def apply(root, config, request):
    if not isinstance(request, dict):
        raise RecordError("request must be an object")
    expected = {"operation_id", "actor", "reason", "authority_reference", "base_revisions", "updates"}
    if set(request) != expected:
        raise RecordError("request fields must be: " + ", ".join(sorted(expected)))
    for key in ("actor", "reason", "authority_reference"):
        required_text(request[key], key)
    path = op_path(root, request["operation_id"])
    if path.exists():
        if read(path)["request_revision"] != digest(request):
            raise RecordError("operation_id already belongs to a different request")
        return resume(root, config, path)
    unfinished = pending(root)
    if unfinished:
        raise RecordError("recover pending operations first: " + ", ".join(unfinished))
    updates = request["updates"]
    if not isinstance(updates, dict) or not updates or not set(updates) <= set(RESOURCE_TYPES):
        raise RecordError("updates must contain desk and/or work")
    if config["mode"] == "external-tracker" and "work" in updates:
        raise RecordError("work authority moved to external tracker; local source is an archive")
    before = sources(root, config)
    # Both revisions are required, even for one resource, to protect cross-record dependencies.
    if request["base_revisions"] != {k: digest(v) for k, v in before.items()}:
        raise RecordError("stale base_revisions; reread and reconcile")
    after = json.loads(canonical(before))
    stamp = datetime.now(ZoneInfo(config["timezone"])).replace(tzinfo=None).isoformat(timespec="microseconds")
    for name, value in updates.items():
        if not isinstance(value, dict):
            raise RecordError(f"{name}: candidate must be an object")
        after[name] = dict(value, updated=stamp)
    for name, value in after.items():
        validate(name, value, config)
        field = RESOURCE_TYPES[name][1]
        old_ids = {entry["id"] for entry in before[name][field]}
        new_ids = {entry["id"] for entry in value[field]}
        if not old_ids <= new_ids:
            raise RecordError(f"{name}: existing IDs cannot disappear; close or withdraw records")
    old_asks = {entry["id"]: entry for entry in before["desk"]["entries"]}
    for entry in after["desk"]["entries"]:
        previous = old_asks.get(entry["id"], {})
        if "decision_level" in previous:
            if "decision_level" not in entry:
                raise RecordError(f"CK-{entry['id']}: retain decision_level in the record and its ruling")
            if entry.get("state") in ("answered", "withdrawn") and entry["decision_level"] != previous["decision_level"]:
                raise RecordError(f"CK-{entry['id']}: closing or closed asks must retain their decision_level")
    if config["mode"] == "file":
        validate_links(after)
    op = {"operation_id": request["operation_id"], "request_revision": digest(request),
          "actor": request["actor"], "reason": request["reason"],
          "authority_reference": request["authority_reference"],
          "recorded_at": datetime.now(timezone.utc).isoformat(),
          "config_revision": digest(config), "tool_revision": tool_revision(),
          "before": before, "after": after, "state": "prepared"}
    write(path, op)
    return resume(root, config, path)


def initialize(root, args):
    if root.exists() and any(root.iterdir()):
        raise RecordError("init requires a new or empty workspace")
    ZoneInfo(args.timezone)
    for name in ("project_id", "project", "operator", "maintainer"):
        required_text(getattr(args, name), name)
    root.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now(ZoneInfo(args.timezone)).replace(tzinfo=None).isoformat(timespec="seconds")
    shared = {"project": args.project, "maintainer": args.maintainer,
              "updated": stamp, "tz_label": args.timezone}
    data = {"desk": dict(shared, operator=args.operator, entries=[]),
            "work": dict(shared, items=[], desk=args.project + " Check-in Desk")}
    config = {"format_version": 1, "project_id": args.project_id, "mode": "file",
              "timezone": args.timezone, "resources": {
                  "desk": {"source": "checkin/desk.json", "view": "views/desk.html"},
                  "work": {"source": "work/board.json", "view": "views/board.html"}}}
    with locked(root):
        if any(path.name != ".records" for path in root.iterdir()):
            raise RecordError("workspace was populated by another initializer; refusing overwrite")
        for name, value in data.items():
            validate(name, value, config)
            write(inside(root, config["resources"][name]["source"]), value)
        write(root / "records.json", config)
        publish(root, config, data)
        index = (BASE / "artifact-index.md").read_text(encoding="utf-8")
        atomic_bytes(root / "ARTIFACTS.md", index.encode("utf-8"))
    return {"state": "initialized", "workspace": str(root),
            "next": "Complete ARTIFACTS.md with owners, authority, audience, tool pin and backup before operational use."}


def export_bundle(root, config, output):
    if pending(root):
        raise RecordError("recover pending operations before export")
    data = sources(root, config)
    for name, value in data.items():
        validate(name, value, config)
    bundle = {"format_version": 1, "project_id": config["project_id"],
              "exported_at": datetime.now(timezone.utc).isoformat(), "mode": config["mode"],
              "config": config, "tool_revision": tool_revision(), "records": data,
              "revisions": {name: digest(value) for name, value in data.items()},
              "history": [read(path) for path in operations(root)]}
    output = Path(output).resolve()
    if root == output or root in output.parents:
        raise RecordError("export outside the operational workspace to avoid overwriting its records")
    if output.exists():
        raise RecordError("export target exists; choose a new snapshot filename")
    write(output, bundle, exclusive=True)
    return {"state": "exported", "path": str(output), "bundle_revision": digest(bundle)}


def check_handoff(bundle, snapshot):
    if not isinstance(bundle, dict) or not isinstance(snapshot, dict):
        raise RecordError("handoff inputs must be objects")
    if bundle.get("format_version") != 1 or snapshot.get("format_version") != 1:
        raise RecordError("handoff inputs require format_version 1")
    if snapshot.get("bundle_revision") != digest(bundle):
        raise RecordError("destination read-back is for a different source bundle")
    if snapshot.get("project_id") != bundle["project_id"]:
        raise RecordError("project identity mismatch")
    for key in ("destination", "destination_revision", "readback_evidence"):
        required_text(snapshot.get(key), key)
    records = bundle["records"]
    if not isinstance(records, dict) or set(records) != set(RESOURCE_TYPES):
        raise RecordError("source bundle must contain desk and work")
    for name, value in records.items():
        validate(name, value)
    if bundle["revisions"] != {k: digest(v) for k, v in records.items()}:
        raise RecordError("source bundle revision mismatch")
    entries = snapshot.get("items")
    if not isinstance(entries, list):
        raise RecordError("destination items must be a list")
    wanted = {item["id"]: item for item in records["work"]["items"]}
    seen, destinations = set(), set()
    for entry in entries:
        if not isinstance(entry, dict):
            raise RecordError("destination items must be objects")
        old_id = entry["source_id"]
        destination_id = required_text(entry.get("destination_id"), "destination_id")
        if type(old_id) is not int or old_id not in wanted or old_id in seen or destination_id in destinations:
            raise RecordError("handoff identities are missing, duplicated, or unknown")
        if entry.get("disposition") not in ("imported", "archived"):
            raise RecordError("every item needs imported or archived disposition")
        if entry["disposition"] == "archived":
            original = wanted[old_id]
            if original.get("kind") == "control" or original.get("state") not in ("done", "dropped"):
                raise RecordError("active work and controls cannot be archived during handoff")
        if digest(entry.get("normalized_record")) != digest(wanted[old_id]):
            raise RecordError(f"WI-{old_id}: normalized destination record differs from source")
        seen.add(old_id)
        destinations.add(destination_id)
    if seen != set(wanted):
        raise RecordError("handoff omits source items")
    return {"state": "snapshot_verified", "items": len(seen),
            "bundle_revision": digest(bundle), "snapshot_revision": digest(snapshot),
            "limit": "Comparison only: does not prove remote reads, permissions, attachments, scheduler migration, cutover or recovery."}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    init = sub.add_parser("init")
    init.add_argument("workspace", type=Path)
    for key in ("project-id", "project", "operator", "maintainer"):
        init.add_argument("--" + key, required=True)
    init.add_argument("--timezone", default="UTC")
    for name in ("status", "apply", "recover", "export", "refresh"):
        cmd = sub.add_parser(name)
        cmd.add_argument("workspace", type=Path)
        if name == "apply": cmd.add_argument("request", type=Path)
        if name == "recover": cmd.add_argument("operation_id")
        if name == "export": cmd.add_argument("output", type=Path)
    handoff = sub.add_parser("handoff-check")
    handoff.add_argument("bundle", type=Path)
    handoff.add_argument("snapshot", type=Path)
    args = parser.parse_args()
    try:
        if args.command == "handoff-check":
            result = check_handoff(read(args.bundle), read(args.snapshot))
        elif args.command == "init":
            result = initialize(args.workspace.resolve(), args)
        else:
            root = args.workspace.resolve()
            with locked(root):
                config = load_config(root)
                if args.command == "status": result = status(root, config)
                elif args.command == "apply": result = apply(root, config, read(args.request))
                elif args.command == "recover": result = resume(root, config, op_path(root, args.operation_id))
                elif args.command == "refresh":
                    if pending(root):
                        raise RecordError("recover pending operations before refresh")
                    data = sources(root, config)
                    for name, value in data.items(): validate(name, value, config)
                    publish(root, config, data)
                    result = status(root, config)
                else: result = export_bundle(root, config, args.output)
        print(json.dumps(result, indent=2, ensure_ascii=False))
        return 0
    except (RecordError, OSError, ValueError, KeyError, TypeError) as exc:
        print(json.dumps({"state": "failed", "error": str(exc)}), file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())

"""Acceptance-shaped local contract probes; no AI-provider or tracker connection is simulated as proof."""
import copy
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

TOOL = Path(__file__).resolve().parents[1] / "templates" / "project-records.py"
spec = importlib.util.spec_from_file_location("records", TOOL)
records = importlib.util.module_from_spec(spec)
spec.loader.exec_module(records)


class ProjectRecordsTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name).resolve()
        self.root = self.base / "project"
        self.cli("init", self.root, "--project-id", "example-app", "--project", "Example App",
                 "--operator", "Owner", "--maintainer", "Delivery lead")

    def cli(self, *args, ok=True):
        result = subprocess.run([sys.executable, str(TOOL), *map(str, args)], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0 if ok else 1, result.stdout + result.stderr)
        return json.loads(result.stdout if ok else result.stderr)

    def data(self):
        return records.sources(self.root, records.load_config(self.root))

    def item(self, n=1, **changes):
        return dict(id=n, title=f"Task {n}", owner="Delivery lead", state="backlog", **changes)

    def request(self, op="first", items=None, desk=None):
        data = self.data()
        updates = {}
        if items is not None:
            updates["work"] = dict(data["work"], items=items)
        if desk is not None:
            updates["desk"] = dict(data["desk"], entries=desk)
        return {"operation_id": op, "actor": "Session A", "reason": "Synthetic qualification",
                "authority_reference": "Synthetic project role grant; not a real approval",
                "base_revisions": {k: records.digest(v) for k, v in data.items()}, "updates": updates}

    def apply(self, request, ok=True):
        path = self.base / (request["operation_id"] + "-request.json")
        records.write(path, request)
        return self.cli("apply", self.root, path, ok=ok)

    def test_empty_start_and_reproducible_views(self):
        status = self.cli("status", self.root)
        self.assertEqual(self.data()["desk"]["entries"], [])
        self.assertEqual(self.data()["work"]["items"], [])
        self.assertTrue(all(v["view_current"] for v in status["resources"].values()))
        for name, data in self.data().items():
            module = records.renderer(name)
            self.assertEqual(module.validate(data), [])
            output = self.root / status["resources"][name]["view"]
            self.assertEqual(output.read_text(), module.render(data))
            self.assertIn("<!doctype html>", output.read_text())
        result = self.cli("init", self.root, "--project-id", "x", "--project", "X",
                          "--operator", "X", "--maintainer", "X", ok=False)
        self.assertIn("empty workspace", result["error"])

    def test_fresh_process_continuation_and_retry_does_not_revert_new_work(self):
        first = self.request(items=[self.item()])
        self.apply(first)
        second = self.request("second", items=[self.item(), self.item(2)])
        second["actor"] = "Session B"
        self.apply(second)
        retry = self.apply(first)
        self.assertTrue(retry["replayed"])
        self.assertEqual(len(self.data()["work"]["items"]), 2)
        self.assertEqual(len(records.operations(self.root)), 2)

    def test_reused_operation_id_for_different_request_is_refused(self):
        first = self.request(items=[self.item()])
        self.apply(first)
        first["reason"] = "Different change"
        self.assertIn("different request", self.apply(first, ok=False)["error"])

    def test_stale_writer_and_deleted_id_refused(self):
        stale = self.request("stale", items=[self.item(1)])
        self.apply(self.request(items=[self.item(1), self.item(2)]))
        self.assertIn("stale", self.apply(stale, ok=False)["error"])
        removed = self.request("remove", items=[self.item(1)])
        self.assertIn("cannot disappear", self.apply(removed, ok=False)["error"])
        self.assertEqual(len(records.operations(self.root)), 1)

    def test_two_concurrent_processes_cannot_lose_an_update(self):
        a = self.request("a", items=[self.item()])
        b = self.request("b", items=[dict(self.item(), title="Different task")])
        paths = [self.base / "a.json", self.base / "b.json"]
        for path, req in zip(paths, (a, b)): records.write(path, req)
        workers = [subprocess.Popen([sys.executable, str(TOOL), "apply", str(self.root), str(path)],
                                   stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True) for path in paths]
        output = [worker.communicate(timeout=15) for worker in workers]
        self.assertEqual(sorted(worker.returncode for worker in workers), [0, 1], output)
        self.assertEqual(len(records.operations(self.root)), 1)
        self.assertIn("stale base_revisions", " ".join(err for _, err in output))

    def test_validation_failure_leaves_source_and_history_unchanged(self):
        before = self.data()
        bad = self.request(items=[dict(self.item(), state="done")])
        self.assertIn("proof", self.apply(bad, ok=False)["error"])
        self.assertEqual(self.data(), before)
        self.assertEqual(records.operations(self.root), [])

    def test_coupled_desk_decision_and_work_release(self):
        ask = {"id": 1, "kind": "decide", "state": "open", "decision_level": "work", "title": "Choose approach",
               "what": "Choose the documented approach", "waits": "Task 1 waits",
               "options": ["A", "B"], "lean": "A", "lean_why": "Meets scope"}
        blocked = dict(self.item(), state="blocked", waits_on={"ask": {"project": "Example App", "id": 1}})
        self.apply(self.request(items=[blocked], desk=[ask]))
        closed = {"id": 1, "kind": "decide", "state": "answered", "decision_level": "work", "title": ask["title"],
                  "answered_on": "2026-09-21", "ruling": "Synthetic owner chose A; scoped to Task 1"}
        self.apply(self.request("answer", items=[self.item()], desk=[closed]))
        self.assertEqual(self.data()["desk"]["entries"][0]["ruling"], closed["ruling"])
        self.assertEqual(self.data()["work"]["items"][0]["state"], "backlog")
        self.assertIn("Decision level: Work", (self.root / "views/desk.html").read_text())

    def declare_levels(self):
        config = records.load_config(self.root)
        config["desk_requires_decision_levels"] = True
        records.write(self.root / "records.json", config)

    def test_levels_are_optional_unless_the_project_declares_them(self):
        ask = {"id": 1, "kind": "decide", "state": "open", "title": "Plain question",
               "what": "A decision with no level", "waits": "Nothing yet",
               "options": ["A", "B"], "lean": "A", "lean_why": "Simplest"}
        self.apply(self.request(desk=[ask]))
        self.assertNotIn("Decision level", (self.root / "views/desk.html").read_text())

    def test_decision_qualification_and_closure_cannot_lose_its_level(self):
        self.declare_levels()
        ask = {"id": 1, "kind": "decide", "state": "open", "title": "Investment choice",
               "what": "Owner must decide the capacity envelope", "waits": "Discovery waits",
               "options": ["Invest", "Defer"], "lean": "Defer", "lean_why": "Missing evidence"}
        before = self.data()
        self.assertIn("decision_level", self.apply(self.request(desk=[ask]), ok=False)["error"])
        self.assertEqual(self.data(), before)
        self.assertEqual(records.operations(self.root), [])
        ask["decision_level"] = "portfolio"
        self.apply(self.request(desk=[ask]))
        closed = {"id": 1, "kind": "decide", "state": "answered", "title": ask["title"],
                  "answered_on": "2026-09-21", "ruling": "Synthetic owner deferred discovery"}
        for candidate in (closed, dict(closed, decision_level="work")):
            self.assertIn("retain", self.apply(self.request("bad-close", desk=[candidate]), ok=False)["error"])
            self.assertEqual(self.data()["desk"]["entries"], [ask])
        closed["decision_level"] = "portfolio"
        self.apply(self.request("close", desk=[closed]))
        self.assertIn("Decision level: Portfolio", (self.root / "views/desk.html").read_text())
        bundle_path = self.base / "level-export.json"
        self.cli("export", self.root, bundle_path)
        bundle = records.read(bundle_path)
        self.assertEqual(bundle["records"]["desk"]["entries"][0]["decision_level"], "portfolio")
        self.assertTrue(all(op["after"]["desk"]["entries"][0]["decision_level"] == "portfolio"
                            for op in bundle["history"]))

    def test_open_level_correction_keeps_history_and_pointer_closure_keeps_owner(self):
        pointer = {"id": 1, "kind": "decide", "state": "open", "title": "Owner's question",
                   "decision_level": "work", "owned_by": {"project": "Example upstream", "id": 9}}
        self.apply(self.request(desk=[pointer]))
        corrected = dict(pointer, decision_level="portfolio")
        request = self.request("correct", desk=[corrected])
        request["reason"] = "Synthetic owning desk classified its investment question as Portfolio"
        self.apply(request)
        op = records.read(records.op_path(self.root, "correct"))
        self.assertEqual(op["before"]["desk"]["entries"][0]["decision_level"], "work")
        closed = dict(corrected, state="withdrawn", answered_on="2026-09-21",
                      ruling="Example upstream CK-9 withdrew the investment question")
        self.apply(self.request("withdraw", desk=[closed]))
        self.assertEqual(self.data()["desk"]["entries"][0]["owned_by"], pointer["owned_by"])
        self.assertIn("Decision level: Portfolio", (self.root / "views/desk.html").read_text())

    def test_missing_desk_reference_refused(self):
        item = dict(self.item(), state="blocked", waits_on={"ask": {"project": "Example App", "id": 1}})
        self.assertIn("missing local", self.apply(self.request(items=[item]), ok=False)["error"])

    def test_todo_import_preserves_uncertainty_and_historical_completion(self):
        snapshot = Path(__file__).resolve().parents[1] / "examples/portable-records/TODO.snapshot.md"
        original = snapshot.read_bytes()
        history = self.root / "history" / "TODO-2026-09-21.md"
        records.atomic_bytes(history, original)
        pending_item = dict(self.item(), owner="Unassigned", source="history/TODO-2026-09-21.md:3",
                            uncertain=["owner: not stated in source", "needed_by: not stated in source"])
        historical = dict(self.item(2), state="done", owner="Unassigned", closed_on="2026-09-20",
                          source="history/TODO-2026-09-21.md:4",
                          uncertain=["proof: historical checkbox, no evidence recorded"])
        request = self.request(items=[pending_item, historical])
        request["updates"]["work"]["adopted"] = "2026-09-21"
        self.apply(request)
        self.assertEqual(self.data()["work"]["items"], [pending_item, historical])
        html = (self.root / "views/board.html").read_text()
        self.assertIn("operator-reported", html)
        self.assertIn("unconfirmed", html)
        self.assertNotIn("proof", self.data()["work"]["items"][1])
        self.assertEqual(history.read_bytes(), original)

    def test_view_failure_records_saved_source_and_recovers(self):
        view = self.root / "views" / "desk.html"
        view.unlink()
        view.mkdir()
        self.apply(self.request(items=[self.item()]), ok=False)
        self.assertEqual(len(self.data()["work"]["items"]), 1)
        op = records.read(records.op_path(self.root, "first"))
        self.assertEqual(op["state"], "source_saved")
        status = self.cli("status", self.root)
        self.assertEqual(status["pending_operations"], ["first"])
        self.assertFalse(status["resources"]["work"]["view_current"])
        self.assertIn("recover pending", self.apply(self.request("next", items=[self.item()]), ok=False)["error"])
        self.cli("export", self.root, self.base / "blocked-export.json", ok=False)
        view.rmdir()
        result = self.cli("recover", self.root, "first")
        self.assertTrue(all(v["view_current"] for v in result["current"]["resources"].values()))

    def test_interruption_between_sources_recovers_in_order(self):
        decision = {"id": 1, "kind": "team", "title": "Bounded choice", "date": "2026-09-21",
                    "owner": "Delivery lead", "why": "Within role", "status": "done"}
        request = self.request(items=[self.item()], desk=[decision])
        original_write = records.write
        def interrupted(path, value):
            if Path(path) == self.root / "work" / "board.json":
                raise KeyboardInterrupt("simulated process interruption")
            return original_write(path, value)
        with records.locked(self.root), patch.object(records, "write", side_effect=interrupted):
            with self.assertRaises(KeyboardInterrupt):
                records.apply(self.root, records.load_config(self.root), request)
        self.assertEqual(len(self.data()["desk"]["entries"]), 1)
        self.assertEqual(self.data()["work"]["items"], [])
        self.cli("recover", self.root, "first")
        self.assertEqual(len(self.data()["work"]["items"]), 1)

    def test_recovery_refuses_divergent_source_and_changed_tool_pin(self):
        view = self.root / "views" / "desk.html"
        view.unlink(); view.mkdir()
        self.apply(self.request(items=[self.item()]), ok=False)
        before = self.data()["work"]
        changed = copy.deepcopy(before); changed["items"][0]["title"] = "Uncoordinated write"
        records.write(self.root / "work" / "board.json", changed)
        self.assertIn("diverged", self.cli("recover", self.root, "first", ok=False)["error"])
        records.write(self.root / "work" / "board.json", before)
        path = records.op_path(self.root, "first")
        op = records.read(path); op["tool_revision"] = "different"
        records.write(path, op)
        self.assertIn("tool changed", self.cli("recover", self.root, "first", ok=False)["error"])

    def test_edited_view_is_detected_and_refresh_does_not_change_source(self):
        before = self.data()
        (self.root / "views" / "board.html").write_text("old or edited page")
        self.assertFalse(self.cli("status", self.root)["resources"]["work"]["view_current"])
        self.assertTrue(self.cli("refresh", self.root)["resources"]["work"]["view_current"])
        self.assertEqual(self.data(), before)

    def test_external_mode_retires_work_writes_but_keeps_desk(self):
        config = records.load_config(self.root)
        config.update(mode="external-tracker", tracker_binding="tracker-binding.md")
        records.write(self.root / "records.json", config)
        self.assertFalse(self.cli("status", self.root)["resources"]["work"]["view_current"])
        self.assertIn("authority moved", self.apply(self.request(items=[self.item()]), ok=False)["error"])
        self.apply(self.request("desk-only", desk=[]))
        status = self.cli("status", self.root)
        self.assertEqual(status["resources"]["work"]["authority"], "archive")
        self.assertIn("Archived work records", (self.root / "views" / "board.html").read_text())

    def test_export_is_complete_new_snapshot_and_handoff_is_exact(self):
        self.apply(self.request(items=[self.item()]))
        path = self.base / "export.json"
        receipt = self.cli("export", self.root, path)
        self.cli("export", self.root, path, ok=False)
        bundle = records.read(path)
        self.assertEqual(bundle["records"], self.data())
        self.assertEqual(len(bundle["history"]), 1)
        snapshot = {"format_version": 1, "project_id": "example-app", "bundle_revision": receipt["bundle_revision"],
                    "destination": "Synthetic tracker", "destination_revision": "fixture-1", "readback_evidence": "Synthetic only",
                    "items": [{"source_id": 1, "destination_id": "482", "disposition": "imported",
                               "normalized_record": bundle["records"]["work"]["items"][0]}]}
        dest = self.base / "readback.json"
        records.write(dest, snapshot)
        result = self.cli("handoff-check", path, dest)
        self.assertEqual(result["state"], "snapshot_verified")
        self.assertIn("does not prove remote", result["limit"])
        snapshot["items"][0]["normalized_record"]["owner"] = "Lost owner"
        records.write(dest, snapshot)
        self.assertIn("differs", self.cli("handoff-check", path, dest, ok=False)["error"])
        snapshot["items"][0]["normalized_record"] = dict(self.item(), id=True)
        records.write(dest, snapshot)
        self.assertIn("differs", self.cli("handoff-check", path, dest, ok=False)["error"])

    def test_handoff_refuses_missing_duplicate_and_archived_active_items(self):
        self.apply(self.request(items=[self.item()]))
        bundle_path = self.base / "export.json"
        receipt = self.cli("export", self.root, bundle_path)
        bundle = records.read(bundle_path)
        row = {"source_id": 1, "destination_id": "482", "disposition": "imported",
               "normalized_record": bundle["records"]["work"]["items"][0]}
        snapshot = {"format_version": 1, "project_id": "example-app", "bundle_revision": receipt["bundle_revision"],
                    "destination": "Synthetic", "destination_revision": "1", "readback_evidence": "Fixture", "items": []}
        for items in ([], [row, row], [dict(row, disposition="archived")]):
            snapshot["items"] = items
            with self.assertRaises(records.RecordError): records.check_handoff(bundle, snapshot)

    def test_declaration_must_be_a_boolean(self):
        config = records.load_config(self.root)
        config["desk_requires_decision_levels"] = "yes"
        records.write(self.root / "records.json", config)
        with self.assertRaises(records.RecordError):
            records.load_config(self.root)

    def test_duplicate_json_keys_and_unsafe_bindings_refused(self):
        invalid = self.base / "invalid.json"
        invalid.write_text('{"operation_id":"a","operation_id":"b"}')
        self.assertIn("duplicate JSON", self.cli("apply", self.root, invalid, ok=False)["error"])
        config = records.load_config(self.root)
        config["resources"]["work"]["source"] = "../outside.json"
        records.write(self.root / "records.json", config)
        self.assertIn("escapes", self.cli("status", self.root, ok=False)["error"])


if __name__ == "__main__":
    unittest.main()

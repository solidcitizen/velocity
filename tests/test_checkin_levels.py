"""Scenario checks for one Desk carrying qualified decisions and compatible history."""
import copy
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
TOOL = ROOT / "templates/render-checkin-desk.py"
spec = importlib.util.spec_from_file_location("desk", TOOL)
desk = importlib.util.module_from_spec(spec)
spec.loader.exec_module(desk)


class DecisionLevelTests(unittest.TestCase):
    def setUp(self):
        self.data = json.loads((ROOT / "examples/decision-scopes/desk.json").read_text())

    def test_three_levels_share_one_decide_section_and_one_total(self):
        self.assertEqual(desk.validate(self.data, require_decision_levels=True), [])
        page = desk.render(self.data)
        self.assertEqual(page.count('<section class="group"'), 5)
        decide = page.split('<section class="group" aria-labelledby="decide-heading">')[1].split('</section>')[0]
        for label in ("Work", "Initiative", "Portfolio"):
            self.assertIn(f'<dt>Decision level</dt><dd>{label}</dd>', decide)
        self.assertIn('<strong>3</strong><span>Decisions waiting</span>', page)

    def test_strict_check_requires_levels_including_pointers(self):
        self.data["entries"][0].pop("decision_level")
        self.data["entries"][1] = {"id": 2, "kind": "decide", "state": "open",
                                   "title": "A pointer", "owned_by": {"project": "Upstream", "id": 9}}
        self.assertEqual(desk.validate(self.data), [])
        errors = desk.validate(self.data, require_decision_levels=True)
        self.assertEqual(len(errors), 2)
        self.assertTrue(all("decision_level" in error for error in errors))

    def test_invalid_levels_are_rejected_even_on_history_and_without_strict_mode(self):
        entries = [self.data["entries"][0],
                   {"id": 1, "kind": "decide", "state": "answered", "title": "Closed",
                    "answered_on": "2026-09-21", "ruling": "Synthetic ruling"},
                   {"id": 1, "kind": "team", "title": "Within delegation", "date": "2026-09-21",
                    "owner": "Lead", "why": "Authorized", "status": "done"}]
        for entry in entries:
            for value in (None, "", "strategy", "Work", [], {"level": "work"}):
                with self.subTest(kind=entry["kind"], value=value):
                    data = dict(self.data, entries=[dict(entry, decision_level=value)])
                    self.assertTrue(any("decision_level" in e for e in desk.validate(data)))

    def test_legacy_history_stays_unclassified_and_does_not_create_work_approval(self):
        data = copy.deepcopy(self.data)
        data["entries"] = [{"id": 1, "kind": "decide", "state": "answered", "title": "Old ruling",
                            "answered_on": "2026-01-01", "ruling": "Historical record without classification"}]
        self.assertEqual(desk.validate(data, require_decision_levels=True), [])
        page = desk.render(data)
        self.assertNotIn("Decision level", page)
        self.assertIn('<strong>0</strong><span>Decisions waiting</span>', page)

    def test_pointer_label_is_visible_but_not_counted_as_another_pending_decision(self):
        data = copy.deepcopy(self.data)
        data["entries"].append({"id": 4, "kind": "decide", "state": "open", "title": "Upstream ruling",
                                "decision_level": "portfolio", "owned_by": {"project": "Other scope", "id": 7}})
        self.assertEqual(desk.validate(data, require_decision_levels=True), [])
        page = desk.render(data)
        self.assertIn('<p class="owned">Decision level: Portfolio</p>', page)
        self.assertIn('Owned by Other scope CK-7', page)
        self.assertIn('<strong>3</strong><span>Decisions waiting</span>', page)

    def test_cli_profile_and_reproducible_shared_example(self):
        result = subprocess.run([sys.executable, str(TOOL), str(ROOT / "examples/decision-scopes/desk.json"),
                                 "--check", "--require-decision-levels"], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        sample = json.loads((ROOT / "templates/executive-checkin-desk.example.json").read_text())
        self.assertEqual(desk.validate(sample, require_decision_levels=True), [])
        self.assertEqual(desk.render(sample), (ROOT / "templates/executive-checkin-desk.html").read_text())


if __name__ == "__main__":
    unittest.main()

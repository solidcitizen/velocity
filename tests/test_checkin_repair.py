"""A broken desk file still shows the operator every ask the page can place."""
import copy
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
TOOL = ROOT / "templates/render-checkin-desk.py"
spec = importlib.util.spec_from_file_location("desk", TOOL)
desk = importlib.util.module_from_spec(spec)
spec.loader.exec_module(desk)


def section(page, sid):
    return page.split(f'<section class="group" aria-labelledby="{sid}-heading">')[1].split("</section>")[0]


class RepairTests(unittest.TestCase):
    def setUp(self):
        self.sample = json.loads((ROOT / "templates/executive-checkin-desk.example.json").read_text())
        self.broken = copy.deepcopy(self.sample)
        decide = next(e for e in self.broken["entries"] if e["kind"] == "decide" and e["state"] == "open")
        decide.pop("lean")
        self.decide_id = decide["id"]

    def run_cli(self, data, *flags):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "desk.json"
            path.write_text(json.dumps(data))
            return subprocess.run([sys.executable, str(TOOL), str(path), *flags], capture_output=True, text=True)

    def test_healthy_desk_has_no_repair_block_and_exits_zero(self):
        result = self.run_cli(self.sample, "--fragment")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertNotIn('class="repair"', result.stdout)
        self.assertNotIn(".repair", result.stdout)

    def test_one_missing_field_still_shows_every_ask(self):
        result = self.run_cli(self.broken, "--fragment")
        self.assertEqual(result.returncode, 1)
        self.assertIn("Rendering best-effort", result.stderr)
        page = result.stdout
        self.assertIn("<h2>Needs repair (1)</h2>", page)
        self.assertIn("decide needs &#x27;lean&#x27;", page)
        decide = section(page, "decide")
        self.assertIn(f'<span class="id">CK-{self.decide_id}</span>', decide)
        self.assertIn('<em class="missing">missing; see Needs repair</em>', decide)
        open_ids = [e["id"] for e in self.sample["entries"] if e.get("state") == "open" or e["kind"] == "team"]
        for n in open_ids:
            self.assertIn(f'<span class="id">CK-{n}</span>', page)

    def test_check_still_reports_and_stops(self):
        result = self.run_cli(self.broken, "--check")
        self.assertEqual(result.returncode, 1)
        self.assertEqual(result.stdout, "")
        self.assertIn("decide needs 'lean'", result.stderr)

    def test_unplaceable_entry_is_counted_not_guessed(self):
        self.broken["entries"].append({"id": len(self.broken["entries"]) + 1, "kind": "decide", "title": "No state"})
        errors = desk.validate(self.broken)
        page = desk.render(self.broken, errors=errors)
        self.assertIn(f"<h2>Needs repair ({len(errors)})</h2>", page)
        self.assertIn("1 entry could not be placed on the page at all.", page)
        self.assertNotIn(">No state<", page)

    def test_bad_header_and_theme_do_not_blank_the_page(self):
        self.broken.pop("updated")
        self.broken["theme"] = {"not-a-token": "red"}
        errors = desk.validate(self.broken)
        page = desk.render(self.broken, errors=errors)
        self.assertIn("Needs repair", page)
        self.assertNotIn("not-a-token", page.split("</style>")[0])
        self.assertIn(f'<span class="id">CK-{self.decide_id}</span>', page)


if __name__ == "__main__":
    unittest.main()

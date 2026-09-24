"""Both renderers keep their promise: a broken data file still produces a page with every
placeable entry and a Needs repair block. Each field of each example entry is removed or given
the wrong type, one at a time, and the page must still render."""
import copy
import importlib.util
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, ROOT / path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


desk = load("desk", "templates/render-checkin-desk.py")
board = load("board", "templates/render-work-board.py")
WRONG = (None, 7, "", "x", [], {}, ["x"], {"x": 1}, "2026-10-09T17:00:00-07:00")
IDENTITY = {"id", "title", "kind", "state", "owner", "cadence", "date", "answered_on"}


def mutations(data, key):
    """Yield (label, mutated copy) for every removable or retypable field of every entry."""
    for i, entry in enumerate(data[key]):
        for field in entry:
            gone = copy.deepcopy(data)
            del gone[key][i][field]
            yield f"{key}[{i}].{field} removed", gone
            for value in WRONG:
                bad = copy.deepcopy(data)
                bad[key][i][field] = value
                yield f"{key}[{i}].{field}={value!r}", bad
    for field in list(data):
        if field == key:
            continue
        for value in WRONG:
            bad = copy.deepcopy(data)
            bad[field] = value
            yield f"top.{field}={value!r}", bad


class BestEffortTests(unittest.TestCase):
    def check(self, module, data, key, marker):
        count = 0
        for label, mutated in mutations(data, key):
            with self.subTest(label):
                errors = module.validate(mutated)
                page = module.render(mutated, errors=errors)
                self.assertIn("</main>", page)
                if errors:
                    self.assertIn("Needs repair", page)
                entries = mutated.get(key) if isinstance(mutated.get(key), list) else []
                for entry in entries:
                    if module.renderable(entry):
                        self.assertIn(f"{marker}{entry['id']}<", page)
                count += 1
        self.assertGreater(count, 100)

    def test_desk_survives_every_single_field_fault(self):
        data = json.loads((ROOT / "templates/executive-checkin-desk.example.json").read_text())
        self.check(desk, data, "entries", "CK-")

    def test_board_survives_every_single_field_fault(self):
        data = json.loads((ROOT / "templates/work-board.example.json").read_text())
        self.check(board, data, "items", "WI-")


class UtcOffsetTests(unittest.TestCase):
    """Reported by a pilot: a file with a naive `updated` and an offset-bearing `needed_by` passed
    --check, then crashed the render. The offset is ignored and the time read as written."""
    OFFSET = "2026-10-09T17:00:00-07:00"

    def check(self, module, data, entry):
        entry["needed_by"] = self.OFFSET
        self.assertEqual(module.validate(data), [])
        page = module.render(data)
        entry["needed_by"] = "2026-10-09T17:00:00"
        self.assertEqual(page, module.render(data))
        self.assertIn("Fri 2026-10-09 17:00", page)

    def test_desk_reads_an_offset_as_written(self):
        data = json.loads((ROOT / "templates/executive-checkin-desk.example.json").read_text())
        entry = next(e for e in data["entries"] if e["kind"] == "decide" and e["state"] == "open")
        self.check(desk, data, entry)

    def test_board_reads_an_offset_as_written(self):
        data = json.loads((ROOT / "templates/work-board.example.json").read_text())
        entry = next(e for e in data["items"] if e.get("kind", "work") == "work" and e["state"] in ("doing", "committed"))
        self.check(board, data, entry)

    def test_offset_on_updated_alone_still_renders(self):
        data = json.loads((ROOT / "templates/executive-checkin-desk.example.json").read_text())
        data["updated"] = data["updated"][:16] + "-07:00"
        self.assertEqual(desk.validate(data), [])
        self.assertIn("</main>", desk.render(data))


if __name__ == "__main__":
    unittest.main()

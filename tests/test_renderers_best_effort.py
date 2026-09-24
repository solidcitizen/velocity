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
WRONG = (None, 7, "", "x", [], {}, ["x"], {"x": 1})
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


if __name__ == "__main__":
    unittest.main()

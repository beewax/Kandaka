"""Actual-Hugo regression tests for Sudan-first homepage artwork selection."""
from pathlib import Path
import json
import os
import shutil
import subprocess
import tempfile
import unittest

REPO = Path(__file__).resolve().parents[1]
HUGO = os.environ.get("HUGO_BIN") or shutil.which("hugo")


@unittest.skipUnless(HUGO, "Hugo is required for template regression tests")
class ArtworkPriorityTest(unittest.TestCase):
    def test_groups_stability_variation_and_fallbacks(self):
        # Fixed fixtures must not fail merely because weekly curation adds a work.
        # Real catalogue counts and upcoming EN/AR selections are integration checks.
        items = [dict(id=f"{g}-{i}", since="2026-10-10T10:00:00Z", group=g,
                      value=dict(source=f"{g}-{i}", homepage_group=g))
                 for g, count in [("sudan-nubia", 6), ("international", 3)]
                 for i in range(count)]
        times = ["2026-10-23T18:00:00Z", "2026-10-24T15:29:59Z",
                 "2026-10-24T15:30:00Z", "2026-10-28T20:00:00Z",
                 "2026-10-31T15:30:00Z", "2026-11-01T07:30:00Z",
                 "2026-11-07T16:29:59Z", "2026-11-07T16:30:00Z"]
        cases = [dict(name=t, at=t, items=items) for t in times]
        for nr in range(5):
            for ni in range(5):
                pool = [dict(id=f"{g}-{i}", since="2026-10-10T10:00:00Z",
                             group=g, value=dict(source=f"{g}-{i}", homepage_group=g))
                        for g, count in [("sudan-nubia", nr), ("international", ni)]
                        for i in range(count)]
                cases.append(dict(name=f"small-{nr}-{ni}", at=times[2], items=pool))
        additions = items + [
            dict(id="new", since="2026-10-24T15:15:00Z", group="sudan-nubia",
                 value=dict(source="new", homepage_group="sudan-nubia")),
            dict(id="later", since="2026-10-25T15:15:00Z", group="international",
                 value=dict(source="later", homepage_group="international")),
            dict(id="unknown", since="2026-10-10T10:00:00Z", group="unknown",
                 value=dict(source="unknown", homepage_group="unknown")),
        ]
        cases += [dict(name="priority", at=times[2], items=additions),
                  dict(name="priority-midweek", at=times[3], items=additions)]
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "layouts/partials").mkdir(parents=True)
            (root / "data").mkdir()
            for name in ["visual-week.html", "weekly-visual-selection.html",
                         "homepage-artwork-selection.html"]:
                shutil.copyfile(REPO / "layouts/partials" / name,
                                root / "layouts/partials" / name)
            (root / "hugo.toml").write_text('baseURL="https://example.test/"\n')
            (root / "data/cases.json").write_text(json.dumps(cases), encoding="utf-8")
            (root / "layouts/home.html").write_text(
                '{{ $out := slice }}{{ range hugo.Data.cases }}'
                '{{ $s := partial "homepage-artwork-selection.html" . }}'
                '{{ $out = $out | append (dict "name" .name "selected" $s) }}'
                '{{ end }}{{ $out | jsonify | safeHTML }}', encoding="utf-8")
            run = subprocess.run([HUGO, "--source", str(root), "--noBuildLock"],
                                 capture_output=True, text=True)
            self.assertEqual(run.returncode, 0, run.stdout + run.stderr)
            results = json.loads((root / "public/index.html").read_text(encoding="utf-8"))
        if os.environ.get("ARTWORK_TEST_RESULTS"):
            Path(os.environ["ARTWORK_TEST_RESULTS"]).write_text(
                json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
        result = {x["name"]: x["selected"] for x in results}
        sources = lambda selection: [w["source"] for w in selection]
        self.assertEqual(result[times[0]], result[times[1]])
        self.assertEqual(result[times[2]], result[times[3]])
        self.assertFalse(set(sources(result[times[0]])) & set(sources(result[times[2]])))
        self.assertEqual(result[times[4]], result[times[5]])
        self.assertEqual(result[times[5]], result[times[6]])
        self.assertNotEqual(result[times[6]], result[times[7]])
        for t in times:
            self.assertEqual([w["homepage_group"] for w in result[t]],
                             ["sudan-nubia", "sudan-nubia", "international"])
        for nr in range(5):
            for ni in range(5):
                selected = result[f"small-{nr}-{ni}"]
                self.assertEqual(len(selected), min(3, nr + ni), (nr, ni))
                self.assertEqual(len(sources(selected)), len(set(sources(selected))))
                if nr >= 2 and ni >= 1:
                    self.assertEqual(sum(w["homepage_group"] == "sudan-nubia"
                                         for w in selected), 2)
        self.assertEqual(result["priority"][0]["source"], "new")
        self.assertEqual(result["priority"], result["priority-midweek"])
        self.assertNotIn("later", sources(result["priority-midweek"]))
        self.assertNotIn("unknown", sources(result["priority"]))


if __name__ == "__main__":
    unittest.main()

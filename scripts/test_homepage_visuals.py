"""Exercise the real Hugo selector; run with HUGO_BIN or Hugo on PATH."""
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
class WeeklyVisualsTest(unittest.TestCase):
    def test_editorial_week_and_selection(self):
        times = [
            "2026-10-23T18:00:00Z", "2026-10-24T15:29:59Z",
            "2026-10-24T15:30:00Z", "2026-10-27T02:00:00Z",
            "2026-10-31T15:30:00Z", "2026-11-01T07:30:00Z",
            "2026-11-07T16:29:59Z", "2026-11-07T16:30:00Z",
            "2027-03-13T16:30:00Z", "2027-03-14T08:30:00Z",
            "2027-03-20T15:30:00Z",
        ]
        pool = [dict(id=str(i), since="2026-10-10T10:00:00Z", value=str(i))
                for i in range(9)]
        cases = [dict(name=t, at=t, items=pool, limit=3) for t in times]
        cases += [dict(name="small" + str(n), at=times[2], items=pool[:n], limit=3)
                  for n in range(7)]
        additions = pool + [
            dict(id="new", since="2026-10-24T15:15:00Z", value="new"),
            dict(id="later", since="2026-10-25T15:15:00Z", value="later"),
        ]
        cases += [dict(name="new", at=times[2], items=additions, limit=3),
                  dict(name="midweek", at=times[3], items=additions, limit=3),
                  dict(name="duplicate", at=times[2], items=pool + [pool[0]], limit=3)]
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "layouts/partials").mkdir(parents=True)
            (root / "data").mkdir()
            for name in ("visual-week.html", "weekly-visual-selection.html"):
                shutil.copyfile(REPO / "layouts/partials" / name,
                                root / "layouts/partials" / name)
            (root / "hugo.toml").write_text('baseURL="https://example.test/"\n')
            (root / "data/cases.json").write_text(json.dumps(cases))
            (root / "layouts/home.html").write_text(
                '{{ $out := slice }}{{ range hugo.Data.cases }}'
                '{{ $w := partial "visual-week.html" . }}'
                '{{ $s := partial "weekly-visual-selection.html" . }}'
                '{{ $out = $out | append (dict "name" .name "selected" $s '
                '"start" ($w.start.Format "2006-01-02T15:04:05Z07:00")) }}'
                '{{ end }}{{ $out | jsonify | safeHTML }}', encoding="utf-8")
            run = subprocess.run([HUGO, "--source", str(root), "--noBuildLock"],
                                 capture_output=True, text=True)
            self.assertEqual(run.returncode, 0, run.stdout + run.stderr)
            result = {x["name"]: x for x in json.loads(
                (root / "public/index.html").read_text(encoding="utf-8"))}
        picks = [result[t]["selected"] for t in times]
        self.assertEqual(picks[0], picks[1])
        self.assertEqual(picks[2], picks[3])
        self.assertFalse(set(picks[0]) & set(picks[2]))
        self.assertEqual(picks[4], picks[5])
        self.assertEqual(picks[5], picks[6])
        self.assertNotEqual(picks[6], picks[7])
        self.assertEqual(picks[8], picks[9])
        self.assertNotEqual(picks[9], picks[10])
        self.assertEqual(result[times[2]]["start"], "2026-10-24T10:30:00-05:00")
        self.assertEqual(result[times[7]]["start"], "2026-11-07T10:30:00-06:00")
        for selection in picks:
            self.assertEqual(len(selection), 3)
            self.assertEqual(len(set(selection)), 3)
            self.assertTrue(set(selection) <= {x["id"] for x in pool})
        for n in range(7):
            self.assertEqual(len(result["small" + str(n)]["selected"]), min(3, n))
        self.assertEqual(result["new"]["selected"][0], "new")
        self.assertEqual(result["new"]["selected"], result["midweek"]["selected"])
        self.assertNotIn("later", result["midweek"]["selected"])
        self.assertEqual(result["duplicate"]["selected"], picks[2])


if __name__ == "__main__":
    unittest.main()

"""Exercise real Hugo selection, localization and JSON safety, plus browser parity."""
from pathlib import Path
from html.parser import HTMLParser
import json, os, shutil, subprocess, tempfile, unittest

REPO = Path(__file__).resolve().parents[1]
HUGO = os.environ.get('HUGO_BIN') or shutil.which('hugo')

class Result(HTMLParser):
    def __init__(self): super().__init__(); self.active = False; self.data = ''
    def handle_starttag(self, tag, attrs):
        if tag == 'script' and dict(attrs).get('id') == 'result': self.active = True
    def handle_endtag(self, tag):
        if tag == 'script': self.active = False
    def handle_data(self, data):
        if self.active: self.data += data

@unittest.skipUnless(HUGO, 'Hugo is required')
class LibraryRotationTest(unittest.TestCase):
    def test_calendar_selection_localization_and_browser_parity(self):
        times = ['2026-10-26T15:00:00Z', '2026-11-01T07:30:00Z',
                 '2026-11-02T15:59:59Z', '2026-11-02T16:00:00Z',
                 '2026-11-09T15:59:59Z', '2026-11-09T16:00:00Z',
                 '2026-11-12T20:00:00Z', '2027-03-08T16:00:00Z',
                 '2027-03-14T08:30:00Z', '2027-03-15T15:00:00Z']
        items = [dict(id=str(i)) for i in range(9)]
        cases = [dict(name=t, at=t, items=items) for t in times]
        cases += [dict(name=f'small-{n}', at=times[5], items=items[:n]) for n in range(5)]
        cases += [dict(name='duplicate', at=times[5], items=items + items[:2]),
                  dict(name='reordered', at=times[5], items=list(reversed(items)))]
        sample = dict(title='</script><script>alert(1)</script>', title_ar='عنوان عربي',
                      author='An Author', author_ar='مؤلف', year='2026',
                      desc="An author's description", desc_ar='وصف عربي', source='https://example.test/book')
        unavailable = dict(title='Unavailable file', author='Author', desc='An existing record',
                           download='https://example.test/book.pdf')
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / 'layouts/partials').mkdir(parents=True)
            (root / 'data').mkdir()
            for name in ['library-week.html', 'library-selection.html', 'library-home-pool.html', 'library-file-label.html']:
                shutil.copyfile(REPO / 'layouts/partials' / name, root / 'layouts/partials' / name)
            (root / 'hugo.toml').write_text('baseURL="https://example.test/"\n[languages.en]\nweight=1\n[languages.ar]\nweight=2\n')
            for filename, data in [('cases.json', cases), ('library.json', {'books': [sample, unavailable, sample]}),
                                   ('library_file_statuses.json', {'https://example.test/book.pdf': 401}),
                                   ('library_file_formats.json', {})]:
                (root / 'data' / filename).write_text(json.dumps(data), encoding='utf8')
            (root / 'layouts/home.html').write_text(
                '{{ $out := slice }}{{ range hugo.Data.cases }}'
                '{{ $week := partial "library-week.html" . }}'
                '{{ $selected := partial "library-selection.html" . }}'
                '{{ $out = $out | append (dict "name" .name "selected" $selected "start" ($week.start.Format "2006-01-02T15:04:05Z07:00")) }}'
                '{{ end }}<script type="application/json" id="result">'
                '{{ dict "cases" $out "pool" (partial "library-home-pool.html" .) | jsonify | safeJS }}</script>', encoding='utf8')
            run = subprocess.run([HUGO, '--source', str(root), '--noBuildLock'], capture_output=True, text=True)
            self.assertEqual(run.returncode, 0, run.stdout + run.stderr)
            outputs = []
            for path in [root / 'public/index.html', root / 'public/ar/index.html']:
                parser = Result(); parser.feed(path.read_text(encoding='utf8'))
                outputs.append(json.loads(parser.data))
        en, ar = outputs
        self.assertEqual(en['cases'], ar['cases'])
        self.assertEqual([x['id'] for x in en['pool']], [x['id'] for x in ar['pool']])
        self.assertEqual(len(en['pool']), 2)
        self.assertEqual(en['pool'][0]['title'], sample['title'])
        self.assertEqual(en['pool'][0]['desc'], sample['desc'])
        self.assertEqual(ar['pool'][0]['title'], sample['title_ar'])
        self.assertEqual(ar['pool'][0]['author'], sample['author_ar'])
        self.assertEqual(en['pool'][1]['label'], 'File unavailable')
        self.assertEqual(ar['pool'][1]['label'], 'الملف غير متاح')
        results = {x['name']: x for x in en['cases']}
        self.assertEqual(results[times[0]]['selected'], results[times[2]]['selected'])
        self.assertEqual(results[times[3]]['selected'], results[times[4]]['selected'])
        self.assertNotEqual(results[times[4]]['selected'], results[times[5]]['selected'])
        self.assertEqual(results[times[5]]['selected'], results[times[6]]['selected'])
        self.assertEqual(results[times[7]]['selected'], results[times[8]]['selected'])
        self.assertNotEqual(results[times[8]]['selected'], results[times[9]]['selected'])
        self.assertEqual(results[times[3]]['start'], '2026-11-02T10:00:00-06:00')
        self.assertEqual(results[times[9]]['start'], '2027-03-15T10:00:00-05:00')
        for n in range(5): self.assertEqual(len(results[f'small-{n}']['selected']), min(3, n))
        self.assertEqual(results['duplicate']['selected'], results[times[5]]['selected'])
        self.assertEqual(results['reordered']['selected'], results[times[5]]['selected'])
        if shutil.which('node'):
            module = (REPO / 'static/js/library-updates.mjs').as_uri()
            program = (f'import {{selectLibrary}} from {json.dumps(module)};'
                       'import {readFileSync} from "node:fs";'
                       'console.log(JSON.stringify(JSON.parse(readFileSync(0,"utf8")).map(c=>({name:c.name,selected:selectLibrary(c.items,new Date(c.at))}))));')
            run = subprocess.run(['node', '--input-type=module', '-e', program], input=json.dumps(cases), capture_output=True, text=True)
            self.assertEqual(run.returncode, 0, run.stderr)
            for case in json.loads(run.stdout): self.assertEqual(case['selected'], results[case['name']]['selected'])

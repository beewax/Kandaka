"""Check bilingual protected A16–A18 drafts and optional Hugo outputs."""
from pathlib import Path
import argparse
import re

ROOT = Path(__file__).resolve().parents[1]
STEMS = ['development/sudan-living-wages-recovery', 'culture/protecting-sudans-memory', 'history/miseeda-nubian-landscape']

def main():
    p = argparse.ArgumentParser()
    p.add_argument('--preview', type=Path)
    p.add_argument('--production', type=Path)
    args = p.parse_args()
    for stem in STEMS:
        pairs = []
        for lang in ('en', 'ar'):
            path = ROOT / 'content' / f'{stem}.{lang}.md'
            text = path.read_text(encoding='utf-8')
            assert 'draft: true' in text, path
            body = text.split('---', 2)[2]
            headings = re.findall(r'^## (.+)$', body, re.M)
            urls = set(re.findall(r'https?://[^\s)>]+', body))
            refs = re.findall(r'^\[\^(\d+)\]:', body, re.M)
            assert set(re.findall(r'\[\^(\d+)\]', body)) == set(refs)
            assert len(refs) == len(set(refs))
            assert len(headings) == 7, (path, len(headings))
            assert len(body.split()) > 800, (path, len(body.split()))
            assert '\ufffd' not in text
            cover = re.search(r"image: '([^']+)'", text).group(1)
            assert (ROOT / 'static' / cover.lstrip('/')).is_file()
            relative = Path('ar' if lang == 'ar' else '') / stem / 'index.html'
            if args.preview:
                html = (args.preview / relative).read_text(encoding='utf-8')
                assert headings[0] in html and cover in html
                assert 'footnote' in html
                if lang == 'ar':
                    assert re.search(r'dir=[\"\x27]?rtl', html)
            if args.production:
                assert not (args.production / relative).exists(), relative
            pairs.append((len(headings), urls, refs, cover))
            print(path.name, len(body.split()), 'words; checked')
        assert pairs[0] == pairs[1], 'Language-pair structure/source mismatch'
    print('PASS: all six protected editions; matching sections, references, cover and source URLs')

if __name__ == '__main__':
    main()

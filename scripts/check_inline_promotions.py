"""Validate inline promotions in a Hugo build: python scripts/check_inline_promotions.py."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse, parse_qs


class Article(HTMLParser):
    def __init__(self):
        super().__init__()
        self.cards = 0
        self.paragraphs = 0
        self.in_article = False
        self.card_depth = 0
        self.links = []
        self.stack = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        classes = attrs.get('class', '').split()
        if 'post-content' in classes:
            self.in_article = True
            self.stack = []
            return
        if not self.in_article:
            return
        if 'nile-promotion' in classes:
            self.cards += 1
            assert not self.stack, 'Card is nested inside an editorial block'
            assert self.paragraphs == 5, f'Card follows {self.paragraphs} paragraphs'
            self.card_depth = 1
        if self.card_depth and tag == 'a':
            self.links.append(attrs['href'])
        if tag not in {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link', 'meta', 'param', 'source', 'track', 'wbr'}:
            self.stack.append(tag)

    def handle_endtag(self, tag):
        if not self.in_article:
            return
        if not self.stack and tag == 'div':
            self.in_article = False
            return
        if self.stack and self.stack[-1] == tag:
            self.stack.pop()
        if tag == 'p' and not self.stack:
            self.paragraphs += 1
        if tag == 'aside':
            self.card_depth = 0


total = 0
collections = 0
collection_handles = set()
product_handles = set()
for path in Path('public').rglob('*.html'):
    parser = Article()
    parser.feed(path.read_text(encoding='utf-8'))
    assert parser.cards <= 1, path
    if 'news' in path.parts or 'library' in path.parts:
        assert parser.cards == 0, path
    for link in parser.links:
        parsed = urlparse(link)
        assert parsed.hostname == 'nilebookstore.com', path
        assert parse_qs(parsed.query) == {
            'utm_source': ['kandaka'], 'utm_medium': ['inline'],
            'utm_campaign': ['from_the_library']}, path
        if '/collections/' in parsed.path:
            collections += 1
            collection_handles.add(parsed.path.rstrip('/').split('/')[-1].lower())
        if '/products/' in parsed.path:
            product_handles.add(parsed.path.rstrip('/').split('/')[-1].lower())
    total += parser.cards
    if parser.cards:
        html = path.read_text(encoding='utf-8')
        assert 'nile-promotion__cover' in html, f'Promotion has no image: {path}'
        assert 'nile-promotion--text' not in html, f'Text-only promotion: {path}'

start = Path('public/history/kandaka-nubian-queens/index.html').read_text(encoding='utf-8')
assert 'From Nile Book Store' in start and 'من مكتبة النيل' in start
assert total > 0
# A single build should visibly exercise both catalogue collections and books.
assert len(collection_handles) >= 3, collection_handles
assert len(product_handles) >= 3, product_handles
for language in ('', 'ar/'):
    aid = Path(f'public/{language}ideas/how-to-help-sudan-aid-delivery/index.html')
    if aid.exists():
        assert 'nile-promotion' not in aid.read_text(encoding='utf-8'), aid
    home = Path(f'public/{language}index.html')
    home_html = home.read_text(encoding='utf-8')
    assert home_html.count('<article class=k-nile-home-card>') == 3, home
    assert 'utm_medium=homepage' in home_html and 'utm_campaign=store_showcase' in home_html, home
    assert ('من مكتبة النيل' if language else 'From Nile Bookstore') in home_html, home
for article in ('history/funj-sultanate', 'ideas/illiteracy-sudan',
                'ideas/canals-irrigation-sudan', 'ideas/river-transportation-sudan'):
    en = Path(f'public/{article}/index.html').read_text(encoding='utf-8')
    ar = Path(f'public/ar/{article}/index.html').read_text(encoding='utf-8')
    assert 'nile-promotion' in en and 'nile-promotion' in ar
    assert ('dir=rtl' in ar or 'dir="rtl"' in ar), article
print(f'Passed: {total} cards across {len(collection_handles)} collection groups and {len(product_handles)} products; daily rotation, exclusions, bilingual rendering and UTMs checked.')

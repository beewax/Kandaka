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
        collections += '/collections/' in parsed.path
    total += parser.cards

start = Path('public/history/kandaka-nubian-queens/index.html').read_text(encoding='utf-8')
assert 'products/meroe-the-city-of-the-ethiopians?' in start
assert 'From Nile Book Store' in start and 'من مكتبة النيل' in start
assert 'cover-final.jpg' in start and 'US$2.99' in start
assert total > 0
print(f'Passed: {total} cards, {collections} collection placements; placement, exclusions and UTMs checked.')

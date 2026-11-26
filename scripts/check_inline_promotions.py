"""Validate inline promotions in a Hugo build: python scripts/check_inline_promotions.py."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlparse, parse_qs


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
    html = path.read_text(encoding='utf-8')
    if 'nile-promotion' not in html:
        continue
    parser = Article()
    parser.feed(html)
    assert parser.cards <= 1, path
    if 'news' in path.parts or 'library' in path.parts:
        assert parser.cards == 0, path
    for link in parser.links:
        parsed = urlparse(link)
        assert parsed.hostname == 'nilebookstore.com', path
        expected = {
            'utm_source': ['kandaka'], 'utm_medium': ['inline'],
            'utm_campaign': ['from_the_library']}
        if 'kandaka-nubian-queens' in path.parts:
            language = 'ar' if 'ar' in path.parts else 'en'
            expected['utm_term'] = ['history-kandaka-nubian-queens']
            expected['utm_content'] = [f'meroe-card-{language}']
        assert parse_qs(parsed.query) == expected, path
        if '/collections/' in parsed.path:
            collections += 1
            collection_handles.add(unquote(parsed.path.rstrip('/').split('/')[-1]).lower())
        if '/products/' in parsed.path:
            product_handles.add(unquote(parsed.path.rstrip('/').split('/')[-1]).lower())
    total += parser.cards
    if parser.cards:
        assert 'nile-promotion__cover' in html, f'Promotion has no image: {path}'
        assert 'nile-promotion--text' not in html, f'Text-only promotion: {path}'

assert total > 0
# Curated products are exact; every unmatched inline card uses Sudan & the Nile.
assert collection_handles == {'sudan-books-كتب-السودان'}, collection_handles
expected_products = {
    'history/kandaka-nubian-queens': 'meroe-the-city-of-the-ethiopians',
    'history/funj-sultanate': 'tabaqat-wad-dayf-allah',
    'ideas/illiteracy-sudan': 'النسائيات-ملك-حفني-ناصف',
    'ideas/canals-irrigation-sudan': 'عشرة-أيام-في-السودان-محمد-حسين-هيكل',
    'ideas/water-paradox-sudan': 'عشرة-أيام-في-السودان-محمد-حسين-هيكل',
    'ideas/river-transportation-sudan': 'khartoum-and-the-blue-and-white-niles-volume-ii',
}
for language in ('', 'ar/'):
    for article, handle in expected_products.items():
        page = Path(f'public/{language}{article}/index.html')
        parser = Article()
        html = page.read_text(encoding='utf-8')
        parser.feed(html)
        assert parser.cards == 1, page
        assert len(parser.links) == 1, page
        parsed = urlparse(parser.links[0])
        assert unquote(parsed.path).rstrip('/').endswith('/' + handle), page
        assert 'data-nile-inline' not in html, page
        assert 'nile-inline-selection.js' not in html, page
        if language:
            assert ('dir=rtl' in html or 'dir="rtl"' in html), page
    kandakat = Path(f'public/{language}history/kandaka-nubian-queens/index.html')
    kandakat_html = unquote(kandakat.read_text(encoding='utf-8'))
    assert ('مروي، مدينة الإثيوبيين' if language else 'Meroë, the City of the Ethiopians') in kandakat_html, kandakat

    aid = Path(f'public/{language}ideas/how-to-help-sudan-aid-delivery/index.html')
    if aid.exists():
        assert 'nile-promotion' not in aid.read_text(encoding='utf-8'), aid
    home = Path(f'public/{language}index.html')
    home_html = home.read_text(encoding='utf-8')
    assert home_html.count('class=k-nile-home-card') == 3, home
    assert home_html.count('class=k-nile-home-cover') == 3, home
    assert home_html.count('cdn.shopify.com/s/files/1/0802/4798/0280/files/') >= 3, home
    assert 'utm_medium=homepage' in home_html and 'utm_campaign=catalogue_books' in home_html, home
    assert ('من مكتبة النيل' if language else 'From Nile Bookstore') in home_html, home
print(f'Passed: {total} curated/fallback cards across {len(collection_handles)} collection group and {len(product_handles)} products; exact placements, Kandakat Meroë pairing, exclusions, bilingual rendering and UTMs checked.')

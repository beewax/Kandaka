"""Validate the October 2026 bilingual Library refresh and optional built pages."""
import argparse
import json
import re
from pathlib import Path
from html.parser import HTMLParser

ROOT = Path(__file__).resolve().parents[1]
SOURCES = [
    "https://erf.org.eg/publications/the-main-features-of-sudans-income-and-wage-structure-in-2022/",
    "https://www.cambridge.org/core/journals/antiquity/article/miseeda-between-kingdoms-through-epochsreconstructing-a-history-of-the-mahas-region-sudan/36228B78AF514630836ECEE46ECE7C52",
    "https://www.cambridge.org/core/journals/antiquity/article/archaeology-and-cultural-heritage-in-wartime-sudan-20232025/DF3E9D9EC1C8D76146648B96D49DE131",
    "https://hdl.handle.net/10568/184053",
    "https://hdl.handle.net/10568/182880",
    "https://hdl.handle.net/10568/183517",
    "https://www.cambridge.org/core/journals/antiquity/article/costumes-of-prestige-and-authority-in-christian-nubia-insights-from-archaeological-reconstruction/E18904093E1C654A2F66572470D0C283",
    "https://www.undp.org/arab-states/publications/laying-groundwork-recovery-undp-sudan-annual-report-2025",
    "https://doi.org/10.1016/j.resglo.2024.100246",
]


class LibraryParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.cards = []
        self.card = None
        self.depth = 0
        self.field = None

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        classes = attrs.get("class", "").split()
        if "lib-card" in classes:
            self.card = {"title": "", "desc": "", "meta": "", "links": []}
            self.depth = 0
        if self.card is not None:
            if tag == "div":
                self.depth += 1
            if tag == "h3":
                self.field = "title"
            elif "lib-desc" in classes:
                self.field = "desc"
            elif "lib-meta" in classes:
                self.field = "meta"
            if tag == "a":
                self.card["links"].append(attrs.get("href"))

    def handle_data(self, data):
        if self.card is not None and self.field:
            self.card[self.field] += data

    def handle_endtag(self, tag):
        if self.card is not None:
            if tag in ("h3", "p", "div"):
                self.field = None
            if tag == "div":
                self.depth -= 1
                if self.depth == 0:
                    self.cards.append(self.card)
                    self.card = None


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--build", type=Path)
    args = parser.parse_args()
    books = json.loads((ROOT / "data/library.json").read_text(encoding="utf-8"))["books"]
    assert len(books) >= 542, "Unexpected loss of Library records"
    selected = []
    for source in SOURCES:
        matches = [b for b in books if b.get("source") == source]
        assert len(matches) == 1, f"Missing or duplicate source: {source}"
        book = matches[0]
        for field in ("title", "title_ar", "author", "author_ar", "desc", "desc_ar", "year", "tags"):
            assert book.get(field), f"Missing {field}: {source}"
        for field in ("title_ar", "author_ar", "desc_ar"):
            assert re.search(r"[\u0600-\u06ff]", book[field]), field
        selected.append(book)
    wb = [b for b in books if "Sudan Economic Update" in b["title"] and "2025" in b["title"]]
    assert len(wb) == 1, "May 2025 World Bank catalogue duplicate remains"
    assert wb[0]["source"].startswith("https://documents1.worldbank.org/")
    selected += wb
    for lang in ("en", "ar"):
        intro = (ROOT / f"content/library/_index.{lang}.md").read_text(encoding="utf-8")
        assert re.search(rf"\*{len(books)}\s", intro), "Displayed count differs from catalogue"
        if args.build:
            page = args.build / ("ar/library/index.html" if lang == "ar" else "library/index.html")
            parser = LibraryParser()
            parser.feed(page.read_text(encoding="utf-8"))
            cards = parser.cards
            assert len(cards) == len(books), "Built card count mismatch"
            for book in selected:
                matching = [c for c in cards if book["source"] in c["links"]]
                assert len(matching) == 1, book["title"]
                card = matching[0]
                suffix = "_ar" if lang == "ar" else ""
                assert card["title"].strip() == book["title" + suffix]
                assert card["desc"].strip() == book["desc" + suffix]
                assert book["author" + suffix] in card["meta"]
    print(f"PASS: {len(books)} records; {len(SOURCES)} bilingual additions; one canonical May 2025 World Bank report" + ("; both built editions verified" if args.build else ""))


if __name__ == "__main__":
    main()

import os, re, hashlib, html, yaml
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from urllib.request import urlopen, Request

OUTPUT_DIR = "content/news"
MAX_ITEMS_PER_FEED = 10
MAX_TOTAL_ITEMS = 80

SUDAN_KEYWORDS = ["sudan", "khartoum", "darfur", "nile", "rsf", "omdurman",
                  "sudanese", "gezira", "kassala", "juba",
                  "???????", "???????", "??????", "??????", "???????", "???????"]

FEEDS = [
    {"name": "Radio Dabanga",        "url": "https://www.dabangasudan.org/en/feed",                          "lang": "en", "sudan_only": False},
    {"name": "Sudan Tribune",        "url": "https://sudantribune.net/feed",                                 "lang": "en", "sudan_only": False},
    {"name": "Ayin Network",         "url": "https://3ayin.com/en/feed",                                     "lang": "en", "sudan_only": False},
    {"name": "AllAfrica Sudan",      "url": "https://allafrica.com/tools/headlines/rdf/sudan/headlines.rdf", "lang": "en", "sudan_only": False},
    {"name": "BBC Africa",           "url": "https://feeds.bbci.co.uk/news/world/africa/rss.xml",            "lang": "en", "sudan_only": True},
    {"name": "African Arguments",    "url": "https://africanarguments.org/feed",                             "lang": "en", "sudan_only": True},
    {"name": "Al Jazeera English",   "url": "https://www.aljazeera.com/xml/rss/all.xml",                     "lang": "en", "sudan_only": True},
    {"name": "????? ?????",          "url": "https://www.dabangasudan.org/ar/feed",                          "lang": "ar", "sudan_only": False},
    {"name": "????????",             "url": "https://alrakoba.net/feed",                                     "lang": "ar", "sudan_only": True},
    {"name": "????? ??????",        "url": "https://aawsat.com/feed",                                       "lang": "ar", "sudan_only": True},
    {"name": "?? ?? ?? ????",       "url": "https://feeds.bbci.co.uk/arabic/rss.xml",                       "lang": "ar", "sudan_only": True},
]

def is_arabic(text):
    arabic_chars = sum(1 for c in text if "\\u0600" <= c <= "\\u06FF")
    return arabic_chars > len(text) * 0.2

def is_sudan_relevant(title, description):
    text = (title + " " + description).lower()
    return any(kw.lower() in text for kw in SUDAN_KEYWORDS)

def slug_from(text):
    text = re.sub(r"[^\w\s-]", "", text.lower())
    text = re.sub(r"[\s_-]+", "-", text)
    return text[:60].strip("-")

def clean_html(text):
    if not text: return ""
    text = re.sub(r"<[^>]+>", "", text)
    text = html.unescape(text)
    return text.strip()[:300]

def parse_date(date_str):
    if not date_str: return datetime.now(timezone.utc).isoformat()
    for fmt in ["%a, %d %b %Y %H:%M:%S %z", "%a, %d %b %Y %H:%M:%S GMT",
                "%Y-%m-%dT%H:%M:%S%z", "%Y-%m-%dT%H:%M:%SZ"]:
        try: return datetime.strptime(date_str.strip(), fmt).isoformat()
        except: continue
    return datetime.now(timezone.utc).isoformat()

def fetch_feed(feed):
    items = []
    try:
        req = Request(feed["url"], headers={"User-Agent": "Kandaka/1.0 (https://kandaka.com)"})
        with urlopen(req, timeout=15) as r:
            content = r.read()
        root = ET.fromstring(content)
        channel = root.find("channel")
        entries = channel.findall("item") if channel is not None else []
        count = 0
        for entry in entries:
            if count >= MAX_ITEMS_PER_FEED: break
            title_el = entry.find("title")
            title = clean_html(title_el.text if title_el is not None else "")
            if not title: continue
            link_el = entry.find("link")
            link = (link_el.text or "").strip() if link_el is not None else ""
            desc_el = entry.find("description")
            description = clean_html(desc_el.text if desc_el is not None else "")
            date_el = entry.find("pubDate")
            pub_date = parse_date(date_el.text if date_el is not None else "")
            if not title or not link: continue
            if feed["sudan_only"] and not is_sudan_relevant(title, description):
                continue
            items.append({"title": title, "link": link, "description": description,
                          "date": pub_date, "source": feed["name"], "lang": "ar" if is_arabic(title + " " + description) else feed["lang"]})
            count += 1
        print(f"  + {feed['name']}: {count} items")
    except Exception as e:
        print(f"  x {feed['name']}: {e}")
    return items

def write_page(item, out_dir):
    url_hash = hashlib.md5(item["link"].encode()).hexdigest()[:8]
    slug = slug_from(item["title"]) or url_hash
    filename = f"{slug}-{url_hash}.{item['lang']}.md"
    meta = {
        "title": item["title"],
        "date": item["date"],
        "source": item["source"],
        "externalLink": item["link"],
        "language": item["lang"],
        "description": item["description"],
        "draft": False,
    }
    filepath = os.path.join(out_dir, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write("---\n")
        yaml.safe_dump(meta, f, allow_unicode=True, sort_keys=False)
        f.write("---\n\n")
        f.write(item["description"] + "\n\n")
        f.write(f"**Source: [{item['source']}]({item['link']})**\n")

def main():
    print("=" * 60)
    print("KANDAKA NEWS FETCHER")
    print("=" * 60)
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    for f in os.listdir(OUTPUT_DIR):
        if f.endswith(".md") and not f.startswith("_index"):
            os.remove(os.path.join(OUTPUT_DIR, f))
    all_items = []
    for feed in FEEDS:
        all_items.extend(fetch_feed(feed))
    all_items.sort(key=lambda x: x["date"], reverse=True)
    all_items = all_items[:MAX_TOTAL_ITEMS]
    for item in all_items:
        try: write_page(item, OUTPUT_DIR)
        except Exception as e: print(f"  Error: {e}")
    print(f"\nDONE - {len(all_items)} items written to {OUTPUT_DIR}/")

if __name__ == "__main__":
    main()





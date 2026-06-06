import os, re, hashlib, html
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from urllib.request import urlopen, Request
from urllib.error import URLError

OUTPUT_DIR = "content/news"
MAX_ITEMS_PER_FEED = 10
MAX_TOTAL_ITEMS = 80

FEEDS = [
    {"name": "Radio Dabanga",        "url": "https://www.dabangasudan.org/en/feed",                     "lang": "en", "category": "Sudan News"},
    {"name": "Sudan Tribune",        "url": "https://sudantribune.net/feed",                            "lang": "en", "category": "Sudan News"},
    {"name": "Ayin Network",         "url": "https://3ayin.com/en/feed",                                "lang": "en", "category": "Sudan News"},
    {"name": "BBC Africa",           "url": "https://feeds.bbci.co.uk/news/world/africa/rss.xml",       "lang": "en", "category": "International"},
    {"name": "African Arguments",    "url": "https://africanarguments.org/feed",                        "lang": "en", "category": "Analysis"},
    {"name": "Rift Valley Institute","url": "https://riftvalley.net/feed/rss",                          "lang": "en", "category": "Analysis"},
    {"name": "AllAfrica Sudan",      "url": "https://allafrica.com/tools/headlines/rdf/sudan/headlines.rdf", "lang": "en", "category": "Sudan News"},
    {"name": "ReliefWeb Sudan",      "url": "https://reliefweb.int/updates/rss.xml?primary_country=192","lang": "en", "category": "Humanitarian"},
    {"name": "Africa Is a Country",  "url": "https://africasacountry.com/feed",                         "lang": "en", "category": "Culture"},
    {"name": "Al Jazeera English",   "url": "https://www.aljazeera.com/xml/rss/all.xml",                "lang": "en", "category": "International"},
    {"name": "The Africa Report",    "url": "https://www.theafricareport.com/feed/",                    "lang": "en", "category": "Development"},
    {"name": "????? ?????",          "url": "https://www.dabangasudan.org/ar/feed",                     "lang": "ar", "category": "????? ???????"},
    {"name": "????????",             "url": "https://alrakoba.net/feed",                                "lang": "ar", "category": "????? ???????"},
    {"name": "???????",             "url": "https://www.aljazeera.com/xml/rss/all.xml",                "lang": "ar", "category": "????"},
    {"name": "????? ??????",        "url": "https://aawsat.com/feed",                                  "lang": "ar", "category": "?????"},
    {"name": "?? ?? ?? ????",       "url": "https://feeds.bbci.co.uk/arabic/rss.xml",                  "lang": "ar", "category": "????"},
]

def slug_from(text):
    text = re.sub(r"[^\w\s-]", "", text.lower())
    text = re.sub(r"[\s_-]+", "-", text)
    return text[:60].strip("-")

def clean_html(text):
    if not text: return ""
    text = re.sub(r"<[^>]+>", "", text)
    text = html.unescape(text)
    return text.strip()[:500]

def parse_date(date_str):
    if not date_str: return datetime.now(timezone.utc).isoformat()
    formats = ["%a, %d %b %Y %H:%M:%S %z","%a, %d %b %Y %H:%M:%S GMT",
               "%Y-%m-%dT%H:%M:%S%z","%Y-%m-%dT%H:%M:%SZ"]
    for fmt in formats:
        try: return datetime.strptime(date_str.strip(), fmt).isoformat()
        except: continue
    return datetime.now(timezone.utc).isoformat()

def fetch_feed(feed):
    items = []
    try:
        req = Request(feed["url"], headers={"User-Agent":"Kandaka/1.0 (https://kandaka.com)"})
        with urlopen(req, timeout=15) as r:
            content = r.read()
        root = ET.fromstring(content)
        ns = {"atom":"http://www.w3.org/2005/Atom"}
        channel = root.find("channel")
        entries = channel.findall("item") if channel is not None else root.findall("atom:entry", ns)
        count = 0
        for entry in entries:
            if count >= MAX_ITEMS_PER_FEED: break
            title_el = entry.find("title")
            title = clean_html(title_el.text if title_el is not None else "")
            if not title: continue
            link_el = entry.find("link")
            if link_el is not None:
                link = link_el.get("href") or link_el.text or ""
            else: link = ""
            link = link.strip()
            desc_el = entry.find("description")
            if desc_el is None: desc_el = entry.find("summary")
            description = clean_html(desc_el.text if desc_el is not None else "")
            date_el = entry.find("pubDate")
            if date_el is None: date_el = entry.find("published")
            pub_date = parse_date(date_el.text if date_el is not None else "")
            if title and link:
                items.append({"title":title,"link":link,"description":description,
                              "date":pub_date,"source":feed["name"],
                              "lang":feed["lang"],"category":feed["category"]})
                count += 1
        print(f"  + {feed['name']}: {count} items")
    except Exception as e:
        print(f"  x {feed['name']}: {e}")
    return items

def write_page(item, out_dir):
    url_hash = hashlib.md5(item["link"].encode()).hexdigest()[:8]
    slug = slug_from(item["title"])
    filename = f"{slug}-{url_hash}.md"
    safe_title = item["title"].replace('"', '\\"')
    safe_desc = item["description"].replace('"', '\\"').replace("\n", " ")
    safe_source = item["source"].replace('"', '\\"')
    content = f"""---
title: "{safe_title}"
date: "{item['date']}"
source: "{safe_source}"
link: "{item['link']}"
lang: "{item['lang']}"
category: "{item['category']}"
description: "{safe_desc[:200]}"
draft: false
---

{item['description']}

**[{item['source']}]({item['link']}) ->**
"""
    with open(os.path.join(out_dir, filename), "w", encoding="utf-8") as f:
        f.write(content)

def main():
    print("=" * 60)
    print("KANDAKA NEWS FETCHER")
    print(f"Fetching {len(FEEDS)} feeds...")
    print("=" * 60)
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    for f in os.listdir(OUTPUT_DIR):
        if f.endswith(".md"):
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

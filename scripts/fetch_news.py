import os, re, hashlib, html
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from urllib.request import urlopen, Request

OUTPUT_DIR = "content/news"
MAX_ITEMS_PER_FEED = 10
MAX_TOTAL_ITEMS = 80

SUDAN_KEYWORDS = ["sudan", "khartoum", "darfur", "nile", "rsf", "omdurman",
                  "sudanese", "gezira", "kassala", "atbara", "juba",
                  "???????", "???????", "??????", "??????", "???????",
                  "???????", "????", "???????"]

FEEDS = [
    {"name": "Radio Dabanga",        "url": "https://www.dabangasudan.org/en/feed",                     "lang": "en", "sudan_only": False},
    {"name": "Sudan Tribune",        "url": "https://sudantribune.net/feed",                            "lang": "en", "sudan_only": False},
    {"name": "Ayin Network",         "url": "https://3ayin.com/en/feed",                                "lang": "en", "sudan_only": False},
    {"name": "AllAfrica Sudan",      "url": "https://allafrica.com/tools/headlines/rdf/sudan/headlines.rdf", "lang": "en", "sudan_only": False},
    {"name": "BBC Africa",           "url": "https://feeds.bbci.co.uk/news/world/africa/rss.xml",       "lang": "en", "sudan_only": True},
    {"name": "African Arguments",    "url": "https://africanarguments.org/feed",                        "lang": "en", "sudan_only": True},
    {"name": "Rift Valley Institute","url": "https://riftvalley.net/feed/rss",                          "lang": "en", "sudan_only": True},
    {"name": "Al Jazeera English",   "url": "https://www.aljazeera.com/xml/rss/all.xml",                "lang": "en", "sudan_only": True},
    {"name": "The Africa Report",    "url": "https://www.theafricareport.com/feed/",                    "lang": "en", "sudan_only": True},
    {"name": "????? ?????",          "url": "https://www.dabangasudan.org/ar/feed",                     "lang": "ar", "sudan_only": False},
    {"name": "????????",             "url": "https://alrakoba.net/feed",                                "lang": "ar", "sudan_only": False},
    {"name": "????? ??????",        "url": "https://aawsat.com/feed",                                  "lang": "ar", "sudan_only": True},
    {"name": "?? ?? ?? ????",       "url": "https://feeds.bbci.co.uk/arabic/rss.xml",                  "lang": "ar", "sudan_only": True},
    {"name": "???????",             "url": "https://www.aljazeera.com/xml/rss/all.xml",                "lang": "ar", "sudan_only": True},
]

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
    return text.strip()[:500]

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
            # Apply Sudan filter only to general feeds
            if feed["sudan_only"] and not is_sudan_relevant(title, description):
                continue
            items.append({"title": title, "link": link, "description": description,
                          "date": pub_date, "source": feed["name"], "lang": feed["lang"]})
            count += 1
        print(f"  + {feed['name']}: {count} items")
    except Exception as e:
        print(f"  x {feed['name']}: {e}")
    return items

def write_page(item, out_dir):
    url_hash = hashlib.md5(item["link"].encode()).hexdigest()[:8]
    slug = slug_from(item["title"]) or url_hash
    filename = f"{slug}-{url_hash}.{item['lang']}.md"
    safe_title = item["title"].replace('"', '\\"').replace("\n", " ")
    safe_desc = item["description"].replace('"', '\\"').replace("\n", " ")[:200]
    safe_source = item["source"].replace('"', '\\"')
    content = f"""---
title: "{safe_title}"
date: "{item['date']}"
source: "{safe_source}"
externalLink: "{item['link']}"
language: "{item['lang']}"
description: "{safe_desc}"
language: "{item['lang']}"
draft: false
---

{item['description']}

**Source: [{item['source']}]({item['link']})**
"""
    with open(os.path.join(out_dir, filename), "w", encoding="utf-8") as f:
        f.write(content)

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
        except Exception as e: print(f"  Error writing: {e}")
    print(f"\nDONE - {len(all_items)} items written to {OUTPUT_DIR}/")

if __name__ == "__main__":
    main()



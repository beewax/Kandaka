#!/usr/bin/env python3
"""
Kandaka News Feed Fetcher
Runs at Netlify build time to fetch RSS feeds and generate Hugo content pages.
Place this file at: scripts/fetch_news.py
"""

import os
import re
import hashlib
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from urllib.request import urlopen, Request
from urllib.error import URLError
import html

# ── CONFIG ──────────────────────────────────────────────────────────────
OUTPUT_DIR = "content/news/items"
MAX_ITEMS_PER_FEED = 10
MAX_TOTAL_ITEMS = 80

FEEDS = [
    # English Sudan news
    {"name": "Radio Dabanga",       "url": "https://www.dabangasudan.org/en/feed",                    "lang": "en", "category": "Sudan News"},
    {"name": "Sudan Tribune",       "url": "https://sudantribune.net/feed",                           "lang": "en", "category": "Sudan News"},
    {"name": "Ayin Network",        "url": "https://www.ayinnews.com/feed",                           "lang": "en", "category": "Sudan News"},
    {"name": "BBC Africa",          "url": "https://feeds.bbci.co.uk/news/world/africa/rss.xml",      "lang": "en", "category": "International"},
    {"name": "African Arguments",   "url": "https://africanarguments.org/feed",                       "lang": "en", "category": "Analysis"},
    {"name": "Rift Valley Institute","url": "https://riftvalley.net/feed",                            "lang": "en", "category": "Analysis"},
    {"name": "The Africa Report",   "url": "https://www.theafricareport.com/feed/",                   "lang": "en", "category": "Development"},
    {"name": "ReliefWeb Sudan",     "url": "https://reliefweb.int/country/sdn/feed",                  "lang": "en", "category": "Humanitarian"},
    {"name": "Crisis Group Africa", "url": "https://www.crisisgroup.org/rss/africa.xml",              "lang": "en", "category": "Analysis"},
    {"name": "Global Voices Africa","url": "https://globalvoices.org/region/sub-saharan-africa/feed/","lang": "en", "category": "Culture"},
    {"name": "Al Jazeera English",  "url": "https://www.aljazeera.com/xml/rss/all.xml",               "lang": "en", "category": "International"},

    # Arabic Sudan news
    {"name": "راديو دبنقا",         "url": "https://www.dabangasudan.org/ar/feed",                    "lang": "ar", "category": "أخبار السودان"},
    {"name": "الراكوبة",            "url": "https://alrakoba.net/feed",                               "lang": "ar", "category": "أخبار السودان"},
    {"name": "الجزيرة العربية",     "url": "https://www.aljazeera.net/xml/rss/all.xml",               "lang": "ar", "category": "دولي"},
    {"name": "الشرق الأوسط",       "url": "https://aawsat.com/feed",                                 "lang": "ar", "category": "تحليل"},
    {"name": "سودانيز أونلاين",     "url": "https://www.sudaneseonline.com/feed",                     "lang": "ar", "category": "أخبار السودان"},
]

# ────────────────────────────────────────────────────────────────────────

def slug_from(text):
    """Generate a URL-safe slug"""
    text = re.sub(r'[^\w\s-]', '', text.lower())
    text = re.sub(r'[\s_-]+', '-', text)
    return text[:60].strip('-')

def clean_html(text):
    """Remove HTML tags and decode entities"""
    if not text:
        return ""
    text = re.sub(r'<[^>]+>', '', text)
    text = html.unescape(text)
    return text.strip()[:500]

def parse_date(date_str):
    """Parse RSS date string to ISO format"""
    if not date_str:
        return datetime.now(timezone.utc).isoformat()
    formats = [
        "%a, %d %b %Y %H:%M:%S %z",
        "%a, %d %b %Y %H:%M:%S GMT",
        "%Y-%m-%dT%H:%M:%S%z",
        "%Y-%m-%dT%H:%M:%SZ",
    ]
    for fmt in formats:
        try:
            return datetime.strptime(date_str.strip(), fmt).isoformat()
        except:
            continue
    return datetime.now(timezone.utc).isoformat()

def fetch_feed(feed):
    """Fetch and parse a single RSS feed"""
    items = []
    try:
        req = Request(feed["url"], headers={
            "User-Agent": "Kandaka/1.0 (https://kandaka.com; Sudan news aggregator)"
        })
        with urlopen(req, timeout=15) as response:
            content = response.read()

        root = ET.fromstring(content)
        ns = {"atom": "http://www.w3.org/2005/Atom"}

        # Handle both RSS and Atom feeds
        channel = root.find("channel")
        entries = []

        if channel is not None:
            # RSS format
            entries = channel.findall("item")
        else:
            # Atom format
            entries = root.findall("atom:entry", ns)

        count = 0
        for entry in entries:
            if count >= MAX_ITEMS_PER_FEED:
                break

            # Get title
            title_el = entry.find("title")
            title = clean_html(title_el.text if title_el is not None else "")
            if not title:
                continue

            # Get link
            link_el = entry.find("link")
            if link_el is not None:
                link = link_el.get("href") or link_el.text or ""
            else:
                link = ""
            link = link.strip()

            # Get description/summary
            desc_el = entry.find("description") or entry.find("summary") or entry.find("content")
            description = clean_html(desc_el.text if desc_el is not None else "")

            # Get date
            date_el = (entry.find("pubDate") or entry.find("published") or
                      entry.find("updated") or entry.find("dc:date"))
            pub_date = parse_date(date_el.text if date_el is not None else "")

            if title and link:
                items.append({
                    "title": title,
                    "link": link,
                    "description": description,
                    "date": pub_date,
                    "source": feed["name"],
                    "lang": feed["lang"],
                    "category": feed["category"],
                })
                count += 1

        print(f"  ✓ {feed['name']}: {count} items")

    except Exception as e:
        print(f"  ✗ {feed['name']}: {e}")

    return items

def write_hugo_page(item, output_dir):
    """Write a single news item as a Hugo markdown file"""
    # Create unique filename from URL hash
    url_hash = hashlib.md5(item["link"].encode()).hexdigest()[:8]
    slug = slug_from(item["title"])
    filename = f"{slug}-{url_hash}.md"

    # Escape quotes in title for YAML
    safe_title = item["title"].replace('"', '\\"')
    safe_desc = item["description"].replace('"', '\\"').replace('\n', ' ')
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

**[{item['source']}]({item['link']}) →**
"""

    filepath = os.path.join(output_dir, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

def main():
    print("=" * 60)
    print("KANDAKA NEWS FETCHER")
    print(f"Fetching {len(FEEDS)} feeds...")
    print("=" * 60)

    # Create output directory
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Clear existing news items
    for f in os.listdir(OUTPUT_DIR):
        if f.endswith(".md"):
            os.remove(os.path.join(OUTPUT_DIR, f))

    # Fetch all feeds
    all_items = []
    for feed in FEEDS:
        items = fetch_feed(feed)
        all_items.extend(items)

    # Sort by date (newest first) and limit total
    all_items.sort(key=lambda x: x["date"], reverse=True)
    all_items = all_items[:MAX_TOTAL_ITEMS]

    # Write Hugo pages
    for item in all_items:
        try:
            write_hugo_page(item, OUTPUT_DIR)
        except Exception as e:
            print(f"  Error writing {item['title'][:40]}: {e}")

    print(f"\n✅ Done — {len(all_items)} news items written to {OUTPUT_DIR}/")

if __name__ == "__main__":
    main()

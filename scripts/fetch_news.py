#!/usr/bin/env python3
"""
Kandaka News Feed Fetcher — Updated June 2026
Fetches RSS feeds and generates Hugo bilingual content pages.
Run at Netlify build time.
"""

import os
import re
import glob
import hashlib
import datetime
import xml.etree.ElementTree as ET
import urllib.request
import urllib.error

try:
    import yaml
except ImportError:
    import subprocess
    subprocess.run(["pip3", "install", "pyyaml"], check=True)
    import yaml

# ── SUDAN KEYWORD FILTERS ────────────────────────────────────────────────────
SUDAN_KEYWORDS = [
    "sudan", "sudanese", "khartoum", "darfur", "juba", "omdurman",
    "port sudan", "rsf", "rapid support forces", "splm", "spla",
    "bashir", "hamdok", "burhan", "hemedti", "nubia", "nubian",
    "meroe", "gezira", "kassala", "atbara", "el fasher", "el obeid",
    "wad madani", "blue nile", "white nile", "nuba mountains",
    "al-bashir", "al-burhan"
]

SUDAN_AR = [
    "السودان", "سوداني", "سودانية", "الخرطوم", "دارفور", "جوبا",
    "أم درمان", "بورتسودان", "الدعم السريع", "البشير", "حمدوك",
    "البرهان", "حميدتي", "جبال النوبة", "مروي", "كسلا", "عطبرة",
    "الفاشر", "ود مدني", "الحرب في السودان", "أزمة السودان",
    "الجنجويد", "الحركة الشعبية", "الحركة السودانية"
]

BLOCKLIST = [
    "kenya", "nigeria", "ghana", "ethiopia", "somalia", "libya",
    "tanzania", "uganda", "rwanda", "liberia", "mali", "senegal",
    "cameroon", "angola", "mozambique", "zimbabwe", "zambia",
    "congo", "drc", "ivory coast", "burkina faso", "south africa",
    "niger", "eritrea", "djibouti", "morocco", "algeria", "tunisia",
    "botswana", "namibia", "madagascar", "malawi", "sierra leone",
    "guinea", "togo", "benin", "gabon", "israel", "israeli",
    "palestine", "palestinian", "west bank", "gaza", "lebanon",
    "syria", "iraq", "iran", "yemen", "turkey", "ukraine", "russia",
    "china", "india", "pakistan", "afghanistan", "myanmar",
    "white house", "trump", "biden", "congress", "senate"
]

BLOCKLIST_AR = [
    "إسرائيل", "فلسطين", "غزة", "لبنان", "سوريا", "العراق",
    "إيران", "اليمن", "تركيا", "أوكرانيا", "روسيا", "الصين",
    "الهند", "باكستان", "أفغانستان", "نيجيريا", "كينيا", "إثيوبيا",
    "الصومال", "ليبيا", "المغرب", "الجزائر", "تونس",
    "البيت الأبيض", "ترامب", "واشنطن العاصمة", "الكونغرس"
]

def is_sudan_relevant(title, desc=""):
    title_lower = (title or "").lower()
    desc_lower = (desc or "").lower()
    for kw in SUDAN_KEYWORDS:
        if kw in title_lower:
            return True
    for kw in SUDAN_AR:
        if kw in (title or "") or kw in (desc or ""):
            return True
    for kw in SUDAN_KEYWORDS:
        pattern = r'\b' + re.escape(kw) + r'\b'
        if re.search(pattern, desc_lower):
            return True
    return False

def is_blocked(title, desc):
    title_lower = (title or "").lower()
    for kw in SUDAN_KEYWORDS:
        if kw in title_lower:
            return False
    for kw in SUDAN_AR:
        if kw in (title or ""):
            return False
    for kw in BLOCKLIST:
        if kw in title_lower:
            return True
    for kw in BLOCKLIST_AR:
        if kw in (title or ""):
            return True
    return False

def detect_arabic(text):
    if not text:
        return False
    arabic_chars = sum(1 for c in text if '\u0600' <= c <= '\u06ff')
    return arabic_chars / max(len(text), 1) > 0.25

# ── RSS FEEDS ────────────────────────────────────────────────────────────────
# NOTE: All categories use English slugs so CSS badge colors work for both
# English and Arabic articles. The template handles display translation.
FEEDS = [
    # === ENGLISH PASS-THROUGH ===
    {"name": "Radio Dabanga",        "url": "https://www.dabangasudan.org/en/feed",                   "category": "Sudan News",    "lang": "en", "filter": False, "max": 5},
    {"name": "Sudan Tribune",        "url": "https://sudantribune.net/feed",                          "category": "Sudan News",    "lang": "en", "filter": False, "max": 5},
    {"name": "Ayin Network",         "url": "https://www.ayinnews.com/feed",                          "category": "Humanitarian",  "lang": "en", "filter": False, "max": 5},
    {"name": "ReliefWeb Sudan",      "url": "https://reliefweb.int/country/sdn/feed",                 "category": "Humanitarian",  "lang": "en", "filter": False, "max": 5},
    {"name": "SUNA English",         "url": "https://suna-sd.net/en/feed",                            "category": "Sudan News",    "lang": "en", "filter": False, "max": 5},

    # === ENGLISH FILTERED ===
    {"name": "BBC Africa",           "url": "https://feeds.bbci.co.uk/news/world/africa/rss.xml",     "category": "International", "lang": "en", "filter": True},
    {"name": "Al Jazeera English",   "url": "https://www.aljazeera.com/xml/rss/all.xml",              "category": "International", "lang": "en", "filter": True},
    {"name": "PBS NewsHour",         "url": "https://www.pbs.org/newshour/feeds/rss/world",           "category": "International", "lang": "en", "filter": True},
    {"name": "NPR World",            "url": "https://feeds.npr.org/1004/rss.xml",                     "category": "International", "lang": "en", "filter": True},
    {"name": "The Guardian",         "url": "https://www.theguardian.com/world/rss",                  "category": "International", "lang": "en", "filter": True},
    {"name": "Foreign Policy",       "url": "https://foreignpolicy.com/feed/",                        "category": "Analysis",      "lang": "en", "filter": True},
    {"name": "Al Monitor",           "url": "https://www.al-monitor.com/rss",                         "category": "International", "lang": "en", "filter": True},
    {"name": "Middle East Eye",      "url": "https://www.middleeasteye.net/rss",                      "category": "International", "lang": "en", "filter": True},
    {"name": "Arab News",            "url": "https://www.arabnews.com/rss.xml",                       "category": "International", "lang": "en", "filter": True},
    {"name": "Deutsche Welle Africa","url": "https://rss.dw.com/rdf/rss-en-africa",                  "category": "International", "lang": "en", "filter": True},
    {"name": "France 24 Africa",     "url": "https://www.france24.com/en/africa/rss",                 "category": "International", "lang": "en", "filter": True},
    {"name": "Euronews",             "url": "https://www.euronews.com/rss",                           "category": "International", "lang": "en", "filter": True},
    {"name": "The Africa Report",    "url": "https://www.theafricareport.com/feed/",                  "category": "Analysis",      "lang": "en", "filter": True},
    {"name": "African Arguments",    "url": "https://africanarguments.org/feed/",                     "category": "Analysis",      "lang": "en", "filter": True},
    {"name": "The East African",     "url": "https://www.theeastafrican.co.ke/feed",                  "category": "International", "lang": "en", "filter": True},
    {"name": "Egypt Independent",    "url": "https://egyptindependent.com/feed/",                     "category": "International", "lang": "en", "filter": True},
    {"name": "Africanews",           "url": "https://www.africanews.com/feed/rss",                    "category": "International", "lang": "en", "filter": True},
    {"name": "African Dev Bank",     "url": "https://www.afdb.org/en/rss-feeds/news-events",          "category": "Economy",       "lang": "en", "filter": True},
    {"name": "African Union",        "url": "https://au.int/en/rss.xml",                              "category": "International", "lang": "en", "filter": True},
    {"name": "IMF News",             "url": "https://www.imf.org/en/news/rss",                        "category": "Economy",       "lang": "en", "filter": True},
    {"name": "World Bank",           "url": "https://blogs.worldbank.org/en/rss/all",                 "category": "Economy",       "lang": "en", "filter": True},
    {"name": "UNDP Africa",          "url": "https://www.undp.org/rss/africa",                        "category": "Humanitarian",  "lang": "en", "filter": True},
    {"name": "UN OCHA",              "url": "https://reliefweb.int/organization/ocha/feed",           "category": "Humanitarian",  "lang": "en", "filter": True},
    {"name": "Rift Valley Inst",     "url": "https://riftvalley.net/feed",                            "category": "Analysis",      "lang": "en", "filter": True},
    {"name": "Crisis Group Africa",  "url": "https://www.crisisgroup.org/rss/africa.xml",             "category": "Analysis",      "lang": "en", "filter": True},
    {"name": "Archaeology Mag",      "url": "https://www.archaeology.org/feed",                       "category": "Culture",       "lang": "en", "filter": True},
    {"name": "World History Enc",    "url": "https://www.worldhistory.org/feed/",                     "category": "Culture",       "lang": "en", "filter": True},
    {"name": "The New Humanitarian", "url": "https://www.thenewhumanitarian.org/rss.xml",             "category": "Humanitarian",  "lang": "en", "filter": True},

    # === ARABIC PASS-THROUGH — English category slugs for CSS compatibility ===
    {"name": "راديو دبنقا",          "url": "https://www.dabangasudan.org/ar/feed",                   "category": "Sudan News",    "lang": "ar", "filter": False, "max": 5},
    {"name": "الراكوبة",             "url": "https://www.alrakoba.net/feed/",                         "category": "Sudan News",    "lang": "ar", "filter": False, "max": 5},
    {"name": "سودانيز أونلاين",      "url": "https://www.sudaneseonline.com/feed/",                   "category": "Sudan News",    "lang": "ar", "filter": False, "max": 5},
    {"name": "سونا",                 "url": "https://suna-sd.net/ar/feed",                            "category": "Sudan News",    "lang": "ar", "filter": False, "max": 5},
    {"name": "الطيار",               "url": "https://www.altayar.net/feed/",                          "category": "Sudan News",    "lang": "ar", "filter": False, "max": 5},
    {"name": "حريات",                "url": "https://www.hurriyatsudan.com/?feed=rss2",               "category": "Sudan News",    "lang": "ar", "filter": False, "max": 5},

    # === ARABIC FILTERED — English category slugs for CSS compatibility ===
    {"name": "الجزيرة",              "url": "https://www.aljazeera.net/xml/rss/all.xml",              "category": "International", "lang": "ar", "filter": True},
    {"name": "بي بي سي عربي",        "url": "https://feeds.bbci.co.uk/arabic/rss.xml",                "category": "International", "lang": "ar", "filter": True},
    {"name": "الشرق الأوسط",         "url": "https://aawsat.com/feed",                                "category": "Analysis",      "lang": "ar", "filter": True},
    {"name": "سكاي نيوز عربية",      "url": "https://www.skynewsarabia.com/rss.xml",                  "category": "International", "lang": "ar", "filter": True},
    {"name": "فرانس 24 عربي",        "url": "https://www.france24.com/ar/rss",                        "category": "International", "lang": "ar", "filter": True},
    {"name": "DW عربي",              "url": "https://rss.dw.com/rdf/rss-ara-all",                    "category": "International", "lang": "ar", "filter": True},
    {"name": "العربي الجديد",        "url": "https://www.alaraby.co.uk/rss.xml",                      "category": "Analysis",      "lang": "ar", "filter": True},
    {"name": "الأناضول عربي",        "url": "https://www.aa.com.tr/ar/rss/default?cat=home",          "category": "International", "lang": "ar", "filter": True},
    {"name": "أخبار الأمم المتحدة",  "url": "https://news.un.org/feed/subscribe/ar/news/all/rss.xml", "category": "Humanitarian",  "lang": "ar", "filter": True},
]

# ── HELPERS ──────────────────────────────────────────────────────────────────
def fetch_feed(url, timeout=15):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Kandaka/1.0"})
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.read()
    except Exception as e:
        print(f"  [WARN] Failed to fetch {url}: {e}")
        return None

def parse_feed(xml_bytes):
    try:
        root = ET.fromstring(xml_bytes)
    except ET.ParseError as e:
        print(f"  [WARN] Parse error: {e}")
        return []

    ns = {"atom": "http://www.w3.org/2005/Atom"}
    items = []

    for item in root.findall(".//item"):
        title = (item.findtext("title") or "").strip()
        link  = (item.findtext("link") or "").strip()
        desc  = (item.findtext("description") or "").strip()
        pub   = (item.findtext("pubDate") or "").strip()
        items.append({"title": title, "link": link, "desc": desc, "pub": pub})

    if not items:
        for entry in root.findall("atom:entry", ns):
            title = (entry.findtext("atom:title", namespaces=ns) or "").strip()
            link_el = entry.find("atom:link", ns)
            link = link_el.get("href", "") if link_el is not None else ""
            desc  = (entry.findtext("atom:summary", namespaces=ns) or "").strip()
            pub   = (entry.findtext("atom:updated", namespaces=ns) or "").strip()
            items.append({"title": title, "link": link, "desc": desc, "pub": pub})

    return items

def clean_html(text):
    return re.sub(r"<[^>]+>", "", text or "").strip()

def make_slug(title, uid):
    if detect_arabic(title):
        return f"ar-news-{uid[:10]}"
    slug = re.sub(r"[^a-z0-9]+", "-", title.lower())[:60].strip("-")
    return f"{slug}-{uid[:6]}"

def write_article(content_dir, slug, lang, front_matter, body):
    lang_dir = os.path.join(content_dir, "news")
    os.makedirs(lang_dir, exist_ok=True)
    filepath = os.path.join(lang_dir, f"{slug}.{lang}.md")
    with open(filepath, "w", encoding="utf-8") as f:
        f.write("---\n")
        yaml.dump(front_matter, f, allow_unicode=True, default_flow_style=False)
        f.write("---\n\n")
        f.write(body + "\n")

# ── MAIN ─────────────────────────────────────────────────────────────────────
def main():
    content_dir = os.path.join(os.path.dirname(__file__), "..", "content")
    news_dir = os.path.join(content_dir, "news")

    print("Clearing old news articles...")
    for f in glob.glob(os.path.join(news_dir, "*.md")):
        if "_index" not in os.path.basename(f):
            os.remove(f)

    written = 0
    skipped = 0

    print(f"Fetching {len(FEEDS)} feeds...")

    for feed in FEEDS:
        print(f"  {feed['name']}...")
        xml_bytes = fetch_feed(feed["url"])
        if not xml_bytes:
            continue

        items = parse_feed(xml_bytes)
        feed_written = 0
        max_items = feed.get("max", 15)

        for item in items[:max_items]:
            title = clean_html(item["title"])
            desc  = clean_html(item["desc"])
            link  = item["link"]

            if not title or not link:
                continue

            if feed["filter"]:
                if not is_sudan_relevant(title, desc):
                    skipped += 1
                    continue
                if is_blocked(title, desc):
                    skipped += 1
                    continue

            if "all of africa today" in title.lower():
                continue

            lang = feed["lang"]
            if detect_arabic(title):
                lang = "ar"

            uid  = hashlib.md5(link.encode()).hexdigest()
            slug = make_slug(title, uid)

            front_matter = {
                "title":    title,
                "date":     datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
                "source":   feed["name"],
                "link":     link,
                "category": feed["category"],
                "language": lang,
                "draft":    False,
            }

            body = f"{desc}\n\n[{feed['name']} ->]({link})" if desc else f"[{feed['name']} ->]({link})"
            write_article(content_dir, slug, lang, front_matter, body)
            written += 1
            feed_written += 1

        print(f"    -> {feed_written} articles written")

    print(f"\nDone. Written: {written} | Skipped (non-Sudan): {skipped}")

if __name__ == "__main__":
    main()

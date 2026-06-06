import os, re, hashlib, html, yaml
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from urllib.request import urlopen, Request

OUTPUT_DIR = "content/news"
MAX_ITEMS_PER_FEED = 10
MAX_TOTAL_ITEMS = 80

SUDAN_EN = ["sudan","khartoum","darfur","sudanese","omdurman","gezira","kassala","juba","rsf","nile","rapid support","dabanga"]
SUDAN_AR = ["\u0627\u0644\u0633\u0648\u062f\u0627\u0646","\u0627\u0644\u062e\u0631\u0637\u0648\u0645","\u062f\u0627\u0631\u0641\u0648\u0631","\u0633\u0648\u062f\u0627\u0646\u064a","\u0623\u0645\u062f\u0631\u0645\u0627\u0646","\u062f\u0628\u0646\u0642\u0627","\u0627\u0644\u0631\u0627\u0643\u0648\u0628\u0629"]

FEEDS = [
    {"name":"Radio Dabanga","url":"https://www.dabangasudan.org/en/feed","lang":"en","sudan_only":False},
    {"name":"Sudan Tribune","url":"https://sudantribune.net/feed","lang":"en","sudan_only":False},
    {"name":"AllAfrica Sudan","url":"https://allafrica.com/tools/headlines/rdf/sudan/headlines.rdf","lang":"en","sudan_only":False},
    {"name":"BBC Africa","url":"https://feeds.bbci.co.uk/news/world/africa/rss.xml","lang":"en","sudan_only":True},
    {"name":"African Arguments","url":"https://africanarguments.org/feed","lang":"en","sudan_only":True},
    {"name":"Al Jazeera EN","url":"https://www.aljazeera.com/xml/rss/all.xml","lang":"en","sudan_only":True},
    {"name":"Dabanga Arabic","url":"https://www.dabangasudan.org/ar/feed","lang":"ar","sudan_only":False},
    {"name":"Al Rakoba","url":"https://alrakoba.net/feed","lang":"ar","sudan_only":True},
    {"name":"Asharq Al-Awsat","url":"https://aawsat.com/feed","lang":"ar","sudan_only":True},
    {"name":"BBC Arabic","url":"https://feeds.bbci.co.uk/arabic/rss.xml","lang":"ar","sudan_only":True},
]

def is_arabic(text):
    if not text: return False
    return sum(1 for c in text if "\u0600" <= c <= "\u06ff") > len(text) * 0.25

def detect_lang(title, desc, feed_lang):
    return "ar" if is_arabic(title + " " + desc) else feed_lang

def is_sudan(title, desc):
    t = (title + " " + desc).lower()
    return any(k in t for k in SUDAN_EN + SUDAN_AR)

def slug(text):
    text = re.sub(r"[^\w\s-]", "", text.lower())
    return re.sub(r"[\s_-]+", "-", text)[:60].strip("-")

def clean(text):
    if not text: return ""
    text = re.sub(r"<[^>]+>", "", text)
    return html.unescape(text).strip()[:300]

def parse_date(s):
    if not s: return datetime.now(timezone.utc).isoformat()
    for fmt in ["%a, %d %b %Y %H:%M:%S %z","%a, %d %b %Y %H:%M:%S GMT","%Y-%m-%dT%H:%M:%S%z","%Y-%m-%dT%H:%M:%SZ"]:
        try: return datetime.strptime(s.strip(), fmt).isoformat()
        except: pass
    return datetime.now(timezone.utc).isoformat()

def fetch(feed):
    items = []
    try:
        req = Request(feed["url"], headers={"User-Agent":"Kandaka/1.0"})
        with urlopen(req, timeout=15) as r: content = r.read()
        root = ET.fromstring(content)
        ch = root.find("channel")
        entries = ch.findall("item") if ch is not None else []
        count = 0
        for e in entries:
            if count >= MAX_ITEMS_PER_FEED: break
            te = e.find("title")
            title = clean(te.text if te is not None else "")
            if not title: continue
            le = e.find("link")
            link = (le.text or "").strip() if le is not None else ""
            de = e.find("description")
            desc = clean(de.text if de is not None else "")
            dte = e.find("pubDate")
            date = parse_date(dte.text if dte is not None else "")
            if not title or not link: continue
            # Skip AllAfrica daily digest wrappers
            if "all of africa today" in title.lower() or "africa today" in title.lower():
                continue
            lang = detect_lang(title, desc, feed["lang"])
            if feed["sudan_only"] and not is_sudan(title, desc): continue
            items.append({"title":title,"link":link,"description":desc,"date":date,"source":feed["name"],"lang":lang})
            count += 1
        print(f"  + {feed['name']}: {count} items")
    except Exception as ex:
        print(f"  x {feed['name']}: {ex}")
    return items

def write_page(item, d):
    h = hashlib.md5(item["link"].encode()).hexdigest()[:8]
    s = slug(item["title"]) or h
    fname = f"{s}-{h}.{item['lang']}.md"
    meta = {"title":item["title"],"date":item["date"],"source":item["source"],
            "externalLink":item["link"],"language":item["lang"],
            "description":item["description"],"draft":False}
    with open(os.path.join(d, fname), "w", encoding="utf-8") as f:
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
    for feed in FEEDS: all_items.extend(fetch(feed))
    all_items.sort(key=lambda x: x["date"], reverse=True)
    all_items = all_items[:MAX_TOTAL_ITEMS]
    en = sum(1 for i in all_items if i["lang"]=="en")
    ar = sum(1 for i in all_items if i["lang"]=="ar")
    for item in all_items:
        try: write_page(item, OUTPUT_DIR)
        except Exception as ex: print(f"  Error: {ex}")
    print(f"DONE  Total:{len(all_items)}  EN:{en}  AR:{ar}")

if __name__ == "__main__": main()


#!/usr/bin/env python3
"""
Kandaka Sudan Images Fetcher
Fetches 3 daily public domain images of Sudan from:
  - Wikimedia Commons (heritage, landscapes, archaeology)
  - Smithsonian Open Access (Nubian artifacts)
  - PICRYL/GetArchive (historical art, illustrations, ethnographic)

Writes Hugo content files to content/images/
Images are referenced by URL (no download needed)
"""

import os
import json
import random
import hashlib
import datetime
import urllib.request
import urllib.parse
import urllib.error

# ── SEARCH QUERIES ────────────────────────────────────────────────────────────
# Rotated daily so we get variety over time
WIKIMEDIA_QUERIES = [
    "Meroe pyramids Sudan",
    "Nubian culture Sudan",
    "Khartoum Sudan historical",
    "Sudan Nile river",
    "Kushite kingdom artifacts",
    "Sudan desert landscape",
    "Nubian temple Sudan",
    "Sudan ancient ruins",
    "Omdurman Sudan",
    "Sudan traditional culture",
    "Gezira Sudan",
    "Blue Nile Sudan",
    "Sudan archaeological site",
    "Kerma Sudan ancient",
    "Nubian people Sudan",
]

SMITHSONIAN_QUERIES = [
    "Sudan Nubian",
    "Kushite artifact",
    "Meroe Sudan",
    "Nubian jewelry",
    "Sudan ancient Egypt",
    "Nubian pottery",
    "Kush empire",
    "Sudan antiquity",
]

PICRYL_QUERIES = [
    "sudan",
    "nubian",
    "khartoum",
    "meroe",
    "nile sudan",
    "sudan desert",
    "sudanese",
    "nubia",
]

# ── HELPERS ───────────────────────────────────────────────────────────────────
def fetch_json(url, timeout=15):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Kandaka/1.0 (kandaka.com)"})
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return json.loads(r.read().decode("utf-8"))
    except Exception as e:
        print(f"  [WARN] Failed to fetch {url}: {e}")
        return None

def today_seed():
    """Return a consistent seed for today so we get same 3 images all day."""
    return int(datetime.date.today().strftime("%Y%m%d"))

def pick_query(queries):
    """Pick a query based on today's date for variety."""
    rng = random.Random(today_seed())
    return rng.choice(queries)

# ── WIKIMEDIA COMMONS ─────────────────────────────────────────────────────────
def fetch_wikimedia():
    query = pick_query(WIKIMEDIA_QUERIES)
    print(f"  Wikimedia: searching '{query}'...")
    
    params = urllib.parse.urlencode({
        "action": "query",
        "generator": "search",
        "gsrnamespace": 6,
        "gsrsearch": query,
        "gsrlimit": 20,
        "prop": "imageinfo",
        "iiprop": "url|extmetadata",
        "iiurlwidth": 800,
        "format": "json",
    })
    
    url = f"https://commons.wikimedia.org/w/api.php?{params}"
    data = fetch_json(url)
    
    if not data:
        return None
    
    pages = data.get("query", {}).get("pages", {})
    candidates = []
    
    for page in pages.values():
        info = page.get("imageinfo", [{}])[0]
        img_url = info.get("url", "")
        
        # Only JPG/PNG, skip SVG and audio
        if not img_url.lower().endswith((".jpg", ".jpeg", ".png")):
            continue
        
        meta = info.get("extmetadata", {})
        title = meta.get("ObjectName", {}).get("value", page.get("title", "").replace("File:", ""))
        description = meta.get("ImageDescription", {}).get("value", "")
        author = meta.get("Artist", {}).get("value", "Wikimedia Commons")
        license_name = meta.get("LicenseShortName", {}).get("value", "Public Domain")
        page_url = f"https://commons.wikimedia.org/wiki/{urllib.parse.quote(page.get('title', ''))}"
        
        # Clean HTML tags from description
        import re
        description = re.sub(r"<[^>]+>", "", description).strip()[:200]
        author = re.sub(r"<[^>]+>", "", author).strip()[:100]
        
        candidates.append({
            "title": title[:100],
            "description": description,
            "image_url": img_url,
            "source_url": page_url,
            "credit": author,
            "license": license_name,
            "source": "Wikimedia Commons",
            "category": "Heritage",
        })
    
    if not candidates:
        return None
    
    rng = random.Random(today_seed() + 1)
    return rng.choice(candidates)

# ── SMITHSONIAN OPEN ACCESS ───────────────────────────────────────────────────
def fetch_smithsonian():
    query = pick_query(SMITHSONIAN_QUERIES)
    print(f"  Smithsonian: searching '{query}'...")
    
    params = urllib.parse.urlencode({
        "q": query,
        "api_key": "default",  # Smithsonian allows 'default' key for basic access
        "rows": 20,
        "online_media_type": "Images",
        "online_visual_material": True,
    })
    
    url = f"https://api.si.edu/openaccess/api/v1.0/search?{params}"
    data = fetch_json(url)
    
    if not data:
        return None
    
    rows = data.get("response", {}).get("rows", [])
    candidates = []
    
    for row in rows:
        descriptor = row.get("_source", {}).get("descriptiveNonRepeating", {})
        online_media = descriptor.get("online_media", {}).get("media", [])
        
        for media in online_media:
            if media.get("type") != "Images":
                continue
            img_url = media.get("content", "")
            if not img_url:
                continue
            
            title = descriptor.get("title", {}).get("content", "Sudan Artifact")
            link = descriptor.get("record_link", "https://www.si.edu/openaccess")
            
            candidates.append({
                "title": title[:100],
                "description": "From the Smithsonian Open Access collection.",
                "image_url": img_url,
                "source_url": link,
                "credit": "Smithsonian Institution",
                "license": "Public Domain",
                "source": "Smithsonian Open Access",
                "category": "Artifact",
            })
            break  # one image per record
    
    if not candidates:
        return None
    
    rng = random.Random(today_seed() + 2)
    return rng.choice(candidates)

# ── PICRYL / GETARCHIVE ───────────────────────────────────────────────────────
def fetch_picryl():
    query = pick_query(PICRYL_QUERIES)
    print(f"  PICRYL: searching '{query}'...")
    
    params = urllib.parse.urlencode({
        "q": query,
        "limit": 20,
        "skip": random.Random(today_seed() + 3).randint(0, 100),
    })
    
    url = f"https://api.picryl.com/api/search?{params}"
    data = fetch_json(url)
    
    if not data:
        # Fallback: use GetArchive API
        params2 = urllib.parse.urlencode({
            "q": query,
            "num": 20,
            "format": "json",
        })
        url2 = f"https://jenikirbyhistory.getarchive.net/api/search?{params2}"
        data = fetch_json(url2)
    
    if not data:
        return None
    
    # Handle both PICRYL and GetArchive response formats
    items = data.get("items", data.get("results", data.get("docs", [])))
    candidates = []
    
    for item in items:
        img_url = (item.get("image_url") or item.get("thumbnail") or 
                   item.get("media", {}).get("image", "") if isinstance(item.get("media"), dict) else "")
        if not img_url:
            continue
        
        title = item.get("title", "Historical Sudan Image")[:100]
        source_url = item.get("url", item.get("link", "https://picryl.com"))
        description = item.get("description", "Public domain historical image.")[:200]
        
        candidates.append({
            "title": title,
            "description": description,
            "image_url": img_url,
            "source_url": source_url,
            "credit": item.get("creator", item.get("author", "Public Domain")),
            "license": "Public Domain",
            "source": "PICRYL",
            "category": "Historical",
        })
    
    if not candidates:
        return None
    
    rng = random.Random(today_seed() + 4)
    return rng.choice(candidates)

# ── WRITE HUGO CONTENT ────────────────────────────────────────────────────────
def write_image_page(content_dir, image_data, index):
    images_dir = os.path.join(content_dir, "images")
    os.makedirs(images_dir, exist_ok=True)
    
    today = datetime.date.today().isoformat()
    uid = hashlib.md5(image_data["image_url"].encode()).hexdigest()[:8]
    filename = f"{today}-image-{index}-{uid}.en.md"
    filepath = os.path.join(images_dir, filename)
    
    # Don't overwrite existing
    if os.path.exists(filepath):
        print(f"  Already exists: {filename}")
        return False
    
    front_matter = f"""---
title: "{image_data['title'].replace('"', "'")}"
date: "{today}T06:00:00Z"
image_url: "{image_data['image_url']}"
source_url: "{image_data['source_url']}"
credit: "{image_data['credit'].replace('"', "'")}"
license: "{image_data['license']}"
source: "{image_data['source']}"
category: "{image_data['category']}"
draft: false
---

{image_data['description']}

*Source: [{image_data['source']}]({image_data['source_url']}) — {image_data['license']}*
"""
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(front_matter)
    
    print(f"  Written: {filename}")
    return True

# ── CLEANUP OLD IMAGES ────────────────────────────────────────────────────────
def cleanup_old_images(content_dir, keep_days=30):
    """Keep only the last 30 days of images to avoid repo bloat."""
    images_dir = os.path.join(content_dir, "images")
    if not os.path.exists(images_dir):
        return
    
    cutoff = datetime.date.today() - datetime.timedelta(days=keep_days)
    removed = 0
    
    for fname in os.listdir(images_dir):
        if not fname.endswith(".md"):
            continue
        try:
            date_str = fname[:10]  # YYYY-MM-DD
            file_date = datetime.date.fromisoformat(date_str)
            if file_date < cutoff:
                os.remove(os.path.join(images_dir, fname))
                removed += 1
        except (ValueError, OSError):
            continue
    
    if removed:
        print(f"  Cleaned up {removed} old image files")

# ── MAIN ──────────────────────────────────────────────────────────────────────
def main():
    content_dir = os.path.join(os.path.dirname(__file__), "..", "content")
    
    print("Fetching daily Sudan images...")
    print(f"Date seed: {today_seed()}")
    
    # Fetch one image from each source
    fetchers = [
        ("Wikimedia Commons", fetch_wikimedia),
        ("Smithsonian", fetch_smithsonian),
        ("PICRYL", fetch_picryl),
    ]
    
    written = 0
    for index, (name, fetcher) in enumerate(fetchers, 1):
        try:
            image = fetcher()
            if image:
                if write_image_page(content_dir, image, index):
                    written += 1
                print(f"  ✓ {name}: {image['title'][:60]}")
            else:
                print(f"  ✗ {name}: no results found")
        except Exception as e:
            print(f"  ✗ {name}: error — {e}")
    
    # Clean up old files
    cleanup_old_images(content_dir)
    
    print(f"\nDone. {written} new images written.")

if __name__ == "__main__":
    main()

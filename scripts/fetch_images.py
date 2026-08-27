#!/usr/bin/env python3
"""
Kandaka Sudan Images Fetcher
Fetches daily public domain images of Sudan from:
  - Wikimedia Commons (heritage, landscapes, archaeology)
  - Smithsonian Open Access (Nubian artifacts)
  - DPLA (Digital Public Library of America — historical photos, culture)
  - Art Institute of Chicago (Nubian/Kushite/Sudanese art and artifacts)
  - Europeana (European archives/museums, reusability=open only)
  - Library of Congress (Prints & Photographs, digitized books — no API key needed)
  - National Archives / NARA (federal records, mostly public domain by law)
  - Flickr (recent uploads, filtered)

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
import re

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

DPLA_QUERIES = [
    "Sudan Nubian",
    "Nubian culture",
    "Meroe Sudan",
    "Kush Sudan",
    "Khartoum Sudan",
    "Sudanese village",
    "Nile Sudan",
    "Omdurman Sudan",
    "Nuba Sudan",
    "Sudan expedition",
]

AIC_QUERIES = [
    "Nubian Sudan",
    "Meroe",
    "Kushite",
    "Sudan textile",
    "Sudanese art",
    "Nubian pottery",
    "Kerma",
    "Sudan photograph",
]

EUROPEANA_QUERIES = [
    "Sudan Nubian",
    "Nubian Sudan",
    "Meroe Sudan",
    "Khartoum Sudan",
    "Kush Sudan",
    "Sudanese culture",
    "Dongola Sudan",
    "Kordofan Sudan",
]

LOC_QUERIES = [
    "sudan nubian",
    "nubian sudan",
    "meroe sudan",
    "khartoum sudan",
    "anglo-egyptian sudan",
    "omdurman",
    "kush sudan",
    "gordon khartoum",
]

NARA_QUERIES = [
    "Sudan",
    "Khartoum",
    "Nubia",
    "Anglo-Egyptian Sudan",
    "Sudanese",
]

FLICKR_TAGS = ["sudan", "sudanese", "nubia", "nubian", "meroe", "khartoum"]  # matched with tagmode=any (OR)

# Flickr and other broad catalog searches frequently treat "Sudan" as a
# match for the separate country of South Sudan. Reject both explicit country
# names and unambiguous South Sudan locations before applying Sudan/Nubia/Kush
# relevance checks. Keep this separate from PHOTO_BLOCKLIST: these terms are
# geographically out of scope, not editorially unsuitable subjects.
SOUTH_SUDAN_PATTERNS = [
    r"\bsouth[\s_-]*sudan(?:ese)?\b",
    r"\bsouthern\s+sudan(?:ese)?\b",
    r"\brepublic\s+of\s+south\s+sudan\b",
    r"\bssd\b",
]

SOUTH_SUDAN_PLACES = [
    "juba", "bentiu", "bor", "malakal", "rumbek", "yei", "wau",
    "aweil", "nimule", "torit", "yambio", "equatoria",
    "bahr el ghazal", "bahr al ghazal",
]

# Recent Flickr uploads (and, less often, DPLA results) tagged "sudan" skew
# toward photojournalism from aid/government/inter-governmental orgs
# (conflict, IDP camps, official meetings, delegations) rather than the
# people/culture/landscape imagery Kandaka wants. Skip any candidate whose
# title/description/tags/subjects hit these terms. Shared across fetchers.
PHOTO_BLOCKLIST = [
    "displaced", "idp", "refugee", "conflict", "warzone", "humanitarian",
    "assistance", "wfp", "unhcr", "unicef", "ngo", "rsf", "saf",
    "militia", "military", "soldier", "minister", "ministry", "government",
    "delegation", "summit", "election", "president", "official", "diplomat",
    "embassy", "politic", "crisis", "famine", "malnutrition", "sanctions",
    "ceasefire", "peacekeep", "envoy", "cabinet", "parliament",
    # "nubia"/"nubian" also refers to southern Egypt, which pulls in
    # unrelated Egyptian tourism photos (Luxor, Aswan, etc.) — exclude those.
    "luxor", "aswan", "giza", "cairo", "egypt", "egyptian",
    # Library of Congress and National Archives both surface 19th/early-20th-
    # century colonial-era ethnographic photography of Sudan, some of it
    # objectifying/undressed "specimen" portraiture that was standard practice
    # for that genre at the time but isn't appropriate to auto-publish without
    # review on a modern editorial site. Skip on sight rather than rely on
    # catalogers' own period-typical wording to flag it for us.
    "nude", "nudity", "topless", "bare-breasted", "seminude", "semi-nude",
]

# Bulk conference/event photo dumps (e.g. an org uploading hundreds of
# session photos in one sitting) tend to have generic camera/session-code
# titles like "A1 (12)" or "IMG_0001" rather than a real caption — skip
# these on sight, they're never the people/place photography Kandaka wants
# even when no blocklist keyword fires. Also covers a recurring Europeana
# junk pattern: scanned "generalkatalog" ledger-book pages from ethnographic
# museum archives, which mention Sudan/Nubia in passing but are a page of
# inventory text, not a photo of anything in particular.
PHOTO_LOW_INFO_TITLE = re.compile(
    r"^(?:[a-z]{1,4}\d{0,3}\s*\(\d+\)|img|dsc|dcim|p\d+|_+\d+|\d+"
    r"|general ?katalog|general catalogue|untitled|no title)$",
    re.IGNORECASE,
)

# api.artic.edu and Europeana are full-text search over huge, unrelated
# collections — a bare query like "Meroe" can fall back to near-zero-relevance
# results (a French coastal painting, etc.) when there's no strong match.
# Require an actual Sudan/Nubia-related term to show up in the candidate's
# own text before accepting it.
SUDAN_RELEVANCE_TERMS = [
    "sudan", "sudanese", "nubia", "nubian", "meroe", "meroitic", "kush",
    "kushite", "khartoum", "kerma", "dongola", "kordofan", "darfur",
    "omdurman", "mahdi", "mahdist", "gezira",
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

def contains_term(text, terms, allow_suffix=False):
    """Match complete words/phrases, optionally treating them as stems."""
    suffix = "" if allow_suffix else r"\b"
    return any(re.search(r"\b" + re.escape(term) + suffix, text) for term in terms)

def is_sudan_image_candidate(*parts, require_relevance=True):
    """Return True only for in-scope Sudan/Nubia/Kush image metadata.

    The negative geography check runs first because the word ``sudan`` inside
    ``South Sudan`` would otherwise satisfy the positive relevance test.
    """
    text = " ".join(str(part or "") for part in parts).lower()
    text = re.sub(r"[_-]+", " ", text)
    text = re.sub(r"\s+", " ", text).strip()

    if any(re.search(pattern, text) for pattern in SOUTH_SUDAN_PATTERNS):
        return False
    if contains_term(text, SOUTH_SUDAN_PLACES):
        return False
    if contains_term(text, PHOTO_BLOCKLIST, allow_suffix=True):
        return False
    if require_relevance and not contains_term(text, SUDAN_RELEVANCE_TERMS):
        return False
    return True

def friendly_license_label(rights_value):
    """Turn a rightsstatements.org/creativecommons.org URL into a short,
    readable label instead of showing the raw URL in the photo caption."""
    if not rights_value:
        return "See source page"

    m = re.search(r"creativecommons\.org/(licenses|publicdomain)/([a-z-]+)/([\d.]+)", rights_value)
    if m:
        kind, code, version = m.groups()
        if kind == "publicdomain":
            return {"zero": "CC0 (Public Domain)", "mark": "Public Domain Mark"}.get(code, f"Public Domain ({code})")
        return f"CC {code.upper()} {version}"

    m = re.search(r"rightsstatements\.org/vocab/([A-Za-z-]+)/", rights_value)
    if m:
        return m.group(1)

    return rights_value

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
        # Wikimedia now appends UTM tracking params to this URL (e.g.
        # "...original.jpg?utm_source=commons.wikimedia.org&..."), which
        # broke the extension check below (always failed, silently
        # filtering out every candidate) — this was the actual cause of
        # zero new site images since Aug 3 despite the daily workflow
        # reporting "success" every day; Wikimedia was the only source that
        # had ever worked at all. Strip the query string before checking
        # extension and before storing, confirmed via live testing against
        # real API responses on 2026-08-12.
        img_url = info.get("url", "").split("?")[0]

        # Only JPG/PNG, skip SVG and audio
        if not img_url.lower().endswith((".jpg", ".jpeg", ".png")):
            continue

        meta = info.get("extmetadata", {})
        title = meta.get("ObjectName", {}).get("value", page.get("title", "").replace("File:", ""))
        description = meta.get("ImageDescription", {}).get("value", "")
        author = meta.get("Artist", {}).get("value", "Wikimedia Commons")
        license_name = meta.get("LicenseShortName", {}).get("value", "Public Domain")
        page_url = f"https://commons.wikimedia.org/wiki/{urllib.parse.quote(page.get('title', ''))}"

        # Clean HTML tags from title/description/author. ObjectName (title)
        # needs this too, not just description/author — some GLAM-partner
        # uploads (e.g. Bibliothèque nationale de France scans) store their
        # ObjectName wrapped in raw markup like "<div class='fn'>Northern
        # Gezira... Southern Gezira</div>", which without stripping goes
        # straight into the page title and renders as literal visible tag
        # text in the homepage photo caption (confirmed live, 2026-08-24).
        title = re.sub(r"<[^>]+>", "", title).strip()
        description = re.sub(r"<[^>]+>", "", description).strip()[:200]
        author = re.sub(r"<[^>]+>", "", author).strip()[:100]

        # Same relevance guard used by the AIC/Europeana/LOC/NARA/Flickr
        # fetchers below, previously missing here — Commons' full-text
        # search on generic queries ("Sudan desert landscape", etc.) can
        # surface loosely related or outright unrelated results (e.g. other
        # countries' desert photography) that never mention Sudan/Nubia
        # themselves. Require the term to actually appear before accepting.
        haystack = " ".join([title, description]).lower()
        if not is_sudan_image_candidate(haystack):
            continue

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

    # Real key from api.data.gov, passed via the SMITHSONIAN_API_KEY env var
    # (set as a GitHub Actions secret) — Smithsonian's old shared "default"
    # key was retired and now returns 403 Forbidden.
    api_key = os.environ.get("SMITHSONIAN_API_KEY", "default")

    params = urllib.parse.urlencode({
        "q": query,
        "api_key": api_key,
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
        # NOTE: the real path is row["content"]["descriptiveNonRepeating"],
        # not row["_source"][...] (there is no "_source" wrapper in this API's
        # responses — that was a leftover from a different, Elasticsearch-style
        # API this fetcher was seemingly modeled on). Fixed here, but even with
        # the correct path, spot-checking ~75 records across several queries
        # found zero with a populated online_media block despite being flagged
        # online_media_type: "Images" in indexedStructured — Smithsonian's API
        # appears to no longer expose media this way for these record types, so
        # this fetcher may keep coming up empty regardless.
        descriptor = row.get("content", {}).get("descriptiveNonRepeating", {})
        online_media = descriptor.get("online_media", {}).get("media", [])

        for media in online_media:
            if media.get("type") != "Images":
                continue
            img_url = media.get("content", "")
            if not img_url:
                continue

            title = descriptor.get("title", {}).get("content", "Sudan Artifact")
            link = descriptor.get("record_link", "https://www.si.edu/openaccess")

            # Same relevance guard as the other fetchers, previously missing
            # here — Smithsonian's search is full-text over its entire
            # collection, so a query like "Kush empire" can fall through to
            # unrelated results with no Sudan/Nubia connection at all.
            if not is_sudan_image_candidate(title):
                continue

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

# ── DPLA (Digital Public Library of America) ──────────────────────────────────
# Replaces the old PICRYL/GetArchive integration — PICRYL's API domain no
# longer resolves at all (looks discontinued), so that fetcher never worked
# and has been removed rather than kept as dead code.
def fetch_dpla():
    query = pick_query(DPLA_QUERIES)
    print(f"  DPLA: searching '{query}'...")

    api_key = os.environ.get("DPLA_API_KEY", "")
    if not api_key:
        print("  [WARN] DPLA_API_KEY not set — skipping")
        return None

    params = urllib.parse.urlencode({
        "q": query,
        "api_key": api_key,
        "page_size": 100,
        "sourceResource.type": "image",
    })

    url = f"https://api.dp.la/v2/items?{params}"
    data = fetch_json(url)

    if not data:
        return None

    docs = data.get("docs", [])
    candidates = []

    for doc in docs:
        # DPLA aggregates from hundreds of institutions with mixed rights;
        # only "Unlimited Re-Use" is DPLA's own bucket for public-domain/CC0/
        # openly-licensed items — skip anything else (e.g. "Permission or
        # Fair Use" = still in copyright, needs the rights-holder's OK).
        if doc.get("rightsCategory") != "Unlimited Re-Use":
            continue

        image_url = doc.get("object", "")
        if not image_url:
            continue

        sr = doc.get("sourceResource", {})
        titles = sr.get("title") or []
        raw_title = (titles[0] if titles else "").strip()
        if not raw_title:
            continue

        descriptions = sr.get("description") or []
        description = (descriptions[0] if descriptions else "").strip()[:200]

        subjects = " ".join(
            s.get("name", "") for s in (sr.get("subject") or []) if isinstance(s, dict)
        )

        # Same conflict/aid-org/government filter used for Flickr — DPLA
        # leans historical/archival so this fires rarely, but costs nothing.
        haystack = " ".join([raw_title, description, subjects]).lower()
        if not is_sudan_image_candidate(haystack):
            continue

        credit = (
            (doc.get("dataProvider") or {}).get("name")
            or (doc.get("provider") or {}).get("name")
            or "DPLA"
        )

        candidates.append({
            "title": raw_title[:100],
            "description": description,
            "image_url": image_url,
            "source_url": doc.get("isShownAt", "https://dp.la"),
            "credit": credit[:100],
            "license": "Unlimited Re-Use (DPLA)",
            "source": "DPLA",
            "category": "Historical",
        })

    if not candidates:
        return None

    rng = random.Random(today_seed() + 4)
    return rng.choice(candidates)

# ── ART INSTITUTE OF CHICAGO (no API key required) ────────────────────────────
def fetch_aic():
    query = pick_query(AIC_QUERIES)
    print(f"  Art Institute of Chicago: searching '{query}'...")

    params = urllib.parse.urlencode({
        "q": query,
        "limit": 40,
        "fields": "id,title,artist_display,date_display,image_id,is_public_domain",
    })

    url = f"https://api.artic.edu/api/v1/artworks/search?{params}"
    data = fetch_json(url)

    if not data:
        return None

    candidates = []
    for item in data.get("data", []):
        if not item.get("is_public_domain") or not item.get("image_id"):
            continue

        raw_title = (item.get("title") or "").strip()
        if not raw_title or PHOTO_LOW_INFO_TITLE.match(raw_title):
            continue

        artist = (item.get("artist_display") or "").split("\n")[0].strip() or "Art Institute of Chicago"
        date_display = item.get("date_display") or ""

        haystack = " ".join([raw_title, artist]).lower()

        # AIC's search is full-text over their entire ~470k-object collection;
        # a short/uncommon query term like "Meroe" can fall through to
        # near-zero-relevance results (e.g. a French coastal painting).
        # Require an actual Sudan/Nubia term in the object's own text.
        if not is_sudan_image_candidate(haystack):
            continue

        # Standard IIIF image request per AIC's API docs — 843px wide, good
        # banner/thumbnail size without pulling full-resolution originals.
        image_url = f"https://www.artic.edu/iiif/2/{item['image_id']}/full/843,/0/default.jpg"

        candidates.append({
            "title": raw_title[:100],
            "description": date_display[:200],
            "image_url": image_url,
            "source_url": f"https://www.artic.edu/artworks/{item['id']}",
            "credit": artist[:100],
            "license": "CC0 / Public Domain (Art Institute of Chicago)",
            "source": "Art Institute of Chicago",
            "category": "Artifact",
        })

    if not candidates:
        return None

    rng = random.Random(today_seed() + 6)
    return rng.choice(candidates)

# ── EUROPEANA ───────────────────────────────────────────────────────────────
def fetch_europeana():
    query = pick_query(EUROPEANA_QUERIES)
    print(f"  Europeana: searching '{query}'...")

    api_key = os.environ.get("EUROPEANA_API_KEY", "")
    if not api_key:
        print("  [WARN] EUROPEANA_API_KEY not set — skipping")
        return None

    params = urllib.parse.urlencode({
        "wskey": api_key,
        "query": query,
        "reusability": "open",  # only CC0/CC-BY/public-domain-cleared items
        "media": "true",
        "rows": 40,
    })

    url = f"https://api.europeana.eu/record/v2/search.json?{params}"
    data = fetch_json(url)

    if not data or not data.get("success"):
        return None

    candidates = []
    for item in data.get("items", []):
        image_urls = item.get("edmIsShownBy") or []
        image_url = image_urls[0] if image_urls else ""
        if not image_url:
            continue

        titles = item.get("title") or []
        raw_title = (titles[0] if titles else "").strip()
        if not raw_title or PHOTO_LOW_INFO_TITLE.match(raw_title):
            continue

        descriptions = item.get("dcDescription") or []
        description = (descriptions[0] if descriptions else "").strip()[:200]

        haystack = " ".join([raw_title, description]).lower()

        # Same relevance guard as AIC — Europeana aggregates hundreds of
        # institutions' full catalogs, so a loose match can surface something
        # only tangentially related (or, per PHOTO_LOW_INFO_TITLE above, a
        # scanned ledger page that just happens to mention Sudan in passing).
        if not is_sudan_image_candidate(haystack):
            continue

        credit = (item.get("dataProvider") or item.get("dcCreator") or ["Europeana"])[0]
        rights = friendly_license_label((item.get("rights") or [""])[0])
        source_url = (item.get("edmIsShownAt") or item.get("guid") or ["https://www.europeana.eu"])[0]

        candidates.append({
            "title": raw_title[:100],
            "description": description,
            "image_url": image_url,
            "source_url": source_url,
            "credit": credit[:100],
            "license": rights,
            "source": "Europeana",
            "category": "Historical",
        })

    if not candidates:
        return None

    rng = random.Random(today_seed() + 7)
    return rng.choice(candidates)

# ── LIBRARY OF CONGRESS (no API key required) ─────────────────────────────────
# loc.gov's search API is fully public — no signup, no key, no auth header.
# Live-tested against real queries (e.g. "sudan nubian" surfaced actual
# Prints & Photographs Division items like "Nubian woman, Anglo-Egyptian
# Sudan"), so the field paths below are confirmed against real responses,
# not just documentation.
def fetch_loc():
    query = pick_query(LOC_QUERIES)
    print(f"  Library of Congress: searching '{query}'...")

    params = urllib.parse.urlencode({
        "q": query,
        "fo": "json",
        "c": 40,
        "fa": "online-format:image",
    })

    url = f"https://www.loc.gov/search/?{params}"
    data = fetch_json(url)

    if not data:
        return None

    candidates = []
    for item in data.get("results", []):
        # access_restricted is the reliable "can we actually use this" flag —
        # confirmed False on every openly-reusable item in live testing.
        # rights/rights_information are almost always empty even on genuinely
        # open items, so they're not useful as a filter here.
        if item.get("access_restricted"):
            continue

        image_urls = item.get("image_url") or []
        # Sizes are ordered smallest-to-largest; take the largest actual
        # JPEG (some entries end the list with a IIIF endpoint we can't
        # easily size-select from a plain image_url list, others end with a
        # tiny .gif thumbnail — skip those, prefer a real .jpg).
        jpg_urls = [u.split("#")[0] for u in image_urls if u.split("#")[0].lower().endswith((".jpg", ".jpeg"))]
        if not jpg_urls:
            continue
        image_url = jpg_urls[-1]

        raw_title = (item.get("title") or "").strip()
        if not raw_title or PHOTO_LOW_INFO_TITLE.match(raw_title):
            continue

        descriptions = item.get("description") or []
        description = (descriptions[0] if descriptions else "").strip()[:200]

        # loc.gov's /search endpoint is full-text over the entire site, not
        # scoped to the query terms in any strict way — confirmed via live
        # testing, a "sudan nubian" query returned an unrelated Latin Bible
        # manuscript, and a "nubian sudan" query returned a book on
        # Melanesian New Guinea whose only tie to Sudan was a one-clause
        # mention of the author's career in a long biographical description
        # ("...conducted field research in New Guinea, Sarawak, ... and
        # Sudan"). Checking the free-text description let that kind of
        # incidental name-drop through. title + subject are curated fields
        # (subject is controlled vocabulary), so require the relevance term
        # there instead — confirmed this still keeps genuine hits whose
        # title alone doesn't say "Sudan" (e.g. "The heroine of the White
        # Nile" has 'sudan' in its subject list, not its title).
        relevance_haystack = " ".join([raw_title, " ".join(item.get("subject") or [])]).lower()
        if not is_sudan_image_candidate(relevance_haystack):
            continue

        haystack = " ".join([raw_title, description, " ".join(item.get("subject") or [])]).lower()
        if not is_sudan_image_candidate(haystack):
            continue

        source_url = item.get("url") or "https://www.loc.gov"

        candidates.append({
            "title": raw_title[:100],
            "description": description,
            "image_url": image_url,
            "source_url": source_url,
            "credit": "Library of Congress",
            "license": "Public Domain / No Known Restrictions (verify on source page)",
            "source": "Library of Congress",
            "category": "Historical",
        })

    if not candidates:
        return None

    rng = random.Random(today_seed() + 8)
    return rng.choice(candidates)

# ── NATIONAL ARCHIVES (NARA) ───────────────────────────────────────────────────
# NOTE: unlike DPLA/Europeana/Smithsonian, a NARA key is NOT self-serve via
# api.data.gov — it's issued by emailing Catalog_API@nara.gov and waiting for
# a reply. This fetcher is written from NARA's published API docs and GitHub
# README (https://github.com/usnationalarchives/Catalog-API), not live-tested
# against a real key/response, since none was available while writing this.
# Smoke-test once NARA_API_KEY is actually set — field names below (naId,
# digitalObjects[].objectUrl, useRestriction) are NARA's documented schema
# but haven't been confirmed against a live payload the way the LOC fetcher
# above has.
def fetch_nara():
    query = pick_query(NARA_QUERIES)
    print(f"  National Archives: searching '{query}'...")

    api_key = os.environ.get("NARA_API_KEY", "")
    if not api_key:
        print("  [WARN] NARA_API_KEY not set — skipping")
        return None

    params = urllib.parse.urlencode({
        "q": query,
        "resultTypes": "record",
        "limit": 40,
    })

    url = f"https://catalog.archives.gov/api/v2/records/search?{params}"
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "Kandaka/1.0 (kandaka.com)", "x-api-key": api_key},
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as r:
            data = json.loads(r.read().decode("utf-8"))
    except Exception as e:
        print(f"  [WARN] Failed to fetch {url}: {e}")
        return None

    if not data:
        return None

    body = data.get("body", data)
    hits = (body.get("hits", {}) or {}).get("hits", []) if isinstance(body, dict) else []
    candidates = []

    for hit in hits:
        record = hit.get("_source", {}).get("record", {}) if isinstance(hit, dict) else {}
        if not record:
            continue

        # NARA records are almost all public domain (federal government
        # works), but a minority carry donor/third-party restrictions —
        # useRestriction.status / copyrightStatus flag those.
        use_restriction = (record.get("useRestriction") or {}).get("status", "")
        if use_restriction and "unrestricted" not in use_restriction.lower():
            continue

        digital_objects = record.get("digitalObjects") or []
        image_url = ""
        for obj in digital_objects:
            obj_url = obj.get("objectUrl", "")
            if obj_url.lower().endswith((".jpg", ".jpeg", ".png")):
                image_url = obj_url
                break
        if not image_url:
            continue

        raw_title = (record.get("title") or "").strip()
        if not raw_title or PHOTO_LOW_INFO_TITLE.match(raw_title):
            continue

        description = (record.get("scopeAndContentNote") or record.get("generalNotes") or "").strip()[:200]

        haystack = " ".join([raw_title, description]).lower()

        # Same full-text-search-over-huge-collection risk as LOC above (see
        # that fetcher's comment — confirmed there via live testing, applied
        # here defensively since NARA's search is the same kind of broad
        # full-text match over millions of unrelated federal records).
        if not is_sudan_image_candidate(haystack):
            continue

        na_id = record.get("naId", "")
        source_url = f"https://catalog.archives.gov/id/{na_id}" if na_id else "https://catalog.archives.gov"

        candidates.append({
            "title": raw_title[:100],
            "description": description,
            "image_url": image_url,
            "source_url": source_url,
            "credit": "National Archives and Records Administration (NARA)",
            "license": "Public Domain (U.S. federal record)",
            "source": "National Archives",
            "category": "Historical",
        })

    if not candidates:
        return None

    rng = random.Random(today_seed() + 9)
    return rng.choice(candidates)

# ── FLICKR (public feed, no API key required) ─────────────────────────────────
def fetch_flickr():
    """Pull from Flickr's public 'recent uploads' feed for tags sudan/meroe/nubia.

    Note: Flickr's no-key feed endpoint does not expose per-photo license info
    (unlike Wikimedia/Smithsonian/DPLA, which are curated for public-domain/CC
    reuse). Photos here may default to "All Rights Reserved" — displayed with a
    "verify license" note and always linked back to the photo page and credited
    to the uploader. If stricter CC-only filtering is wanted later, that needs a
    free Flickr API key and flickr.photos.search's license= parameter instead of
    this feed.
    """
    print(f"  Flickr: searching tags {', '.join(FLICKR_TAGS)}...")

    params = urllib.parse.urlencode({
        "tags": ",".join(FLICKR_TAGS),
        "tagmode": "any",
        "format": "json",
        "nojsoncallback": "1",
    })
    url = f"https://www.flickr.com/services/feeds/photos_public.gne?{params}"
    data = fetch_json(url)

    if not data:
        return None

    items = data.get("items", [])
    candidates = []

    for item in items:
        media_url = item.get("media", {}).get("m", "")
        if not media_url:
            continue

        # Upsize the feed's small 240px thumbnail to Flickr's 1024px "_b" size
        large_url = re.sub(r"_m\.jpg$", "_b.jpg", media_url)

        author_raw = item.get("author", "")
        author_match = re.search(r'"([^"]+)"', author_raw)
        credit = author_match.group(1) if author_match else author_raw.split("(")[0].strip()
        credit = credit or "Flickr user"

        description = re.sub(r"<[^>]+>", " ", item.get("description", ""))
        description = re.sub(r"\s+", " ", description).strip()[:200]

        raw_title = (item.get("title") or "").strip()

        # Skip generic bulk-upload camera/session-code titles ("A1 (12)",
        # "IMG_1234") — these are reliably conference/event photo dumps,
        # never the people/place photography Kandaka wants.
        if not raw_title or PHOTO_LOW_INFO_TITLE.match(raw_title):
            continue

        # Filter out conflict/aid-org/government photojournalism and
        # mistagged Egyptian-Nubia tourism photos — see PHOTO_BLOCKLIST
        # note above. Word-boundary match so e.g. "aid" doesn't fire on
        # unrelated words.
        haystack = " ".join([raw_title, description, item.get("tags") or ""]).lower()
        if not is_sudan_image_candidate(haystack):
            continue

        candidates.append({
            "title": raw_title[:100],
            "description": description,
            "image_url": large_url,
            "source_url": item.get("link", "https://www.flickr.com"),
            "credit": credit[:100],
            "license": "license unverified — check photo page",
            "source": "Flickr",
            "category": "Community",
        })

    if not candidates:
        return None

    rng = random.Random(today_seed() + 10)
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
        ("DPLA", fetch_dpla),
        ("Art Institute of Chicago", fetch_aic),
        ("Europeana", fetch_europeana),
        ("Library of Congress", fetch_loc),
        ("National Archives", fetch_nara),
        ("Flickr", fetch_flickr),
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

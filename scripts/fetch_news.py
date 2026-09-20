#!/usr/bin/env python3
"""Kandaka Sudan News Hub Phase 1: attributed RSS/Atom aggregation."""

from __future__ import annotations

import datetime as dt
import email.utils
import hashlib
import html
import json
import re
import sys
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "data" / "news_sources.yaml"
CONTENT_DIR = ROOT / "content" / "news"
ARABIC_RANGE = re.compile(r"[\u0600-\u06ff]")
HTML_TAG = re.compile(r"<[^>]+>")
WORD = re.compile(r"[\w\u0600-\u06ff]+", re.UNICODE)

SUDAN_TERMS = (
    "sudan", "sudanese", "khartoum", "omdurman", "port sudan", "darfur",
    "kordofan", "gezira", "al jazirah", "kassala", "gedaref", "atbara",
    "el fasher", "al fasher", "el obeid", "wad madani", "blue nile",
    "white nile", "river nile state", "nuba mountains", "burhan", "hemedti",
    "rapid support forces", "rsf", "sudanese armed forces",
)
SUDAN_AR_TERMS = (
    "السودان", "سوداني", "الخرطوم", "أم درمان", "بورتسودان", "بورسودان",
    "دارفور", "كردفان", "ولاية الجزيرة", "كسلا", "القضارف", "عطبرة", "الفاشر",
    "الأبيض", "ود مدني", "النيل الأزرق", "النيل الأبيض", "ولاية نهر النيل",
    "جبال النوبة", "البرهان", "حميدتي", "الدعم السريع",
)
SOUTH_SUDAN_TERMS = (
    "south sudan", "south sudanese", "juba", "salva kiir", "riek machar",
    "جنوب السودان", "جنوب سوداني", "جوبا", "سلفا كير", "رياك مشار",
)
SUDAN_CONTEXT_TERMS = tuple(t for t in SUDAN_TERMS if t not in {"sudan", "sudanese", "white nile", "blue nile"}) + tuple(
    t for t in SUDAN_AR_TERMS if t not in {"السودان", "سوداني", "النيل الأبيض", "النيل الأزرق"}
)

TOPIC_RULES = [
    ("War & Security", ("war", "attack", "drone", "army", "rsf", "fighting", "security", "ceasefire", "حرب", "هجوم", "مسيرة", "الجيش", "الدعم السريع", "قتال")),
    ("Humanitarian", ("famine", "aid", "displaced", "refugee", "hunger", "relief", "humanitarian", "مجاعة", "إغاثة", "نازح", "لاجئ", "جوع", "إنساني")),
    ("Economy", ("economy", "currency", "pound", "bank", "gold", "price", "trade", "اقتصاد", "عملة", "الجنيه", "بنك", "ذهب", "أسعار", "تجارة")),
    ("Agriculture", ("farm", "agriculture", "crop", "wheat", "livestock", "زراعة", "محصول", "قمح", "ماشية")),
    ("Health", ("health", "hospital", "cholera", "disease", "صحة", "مستشفى", "كوليرا", "مرض")),
    ("Education", ("school", "university", "student", "education", "مدرسة", "جامعة", "طالب", "تعليم")),
    ("Culture", ("culture", "music", "film", "book", "heritage", "ثقافة", "موسيقى", "فيلم", "كتاب", "تراث")),
    ("Sport", ("sport", "football", "league", "رياضة", "كرة", "دوري")),
    ("Politics", ("government", "minister", "party", "talks", "election", "حكومة", "وزير", "حزب", "مفاوضات", "انتخابات")),
]
GEOGRAPHY_RULES = [
    ("Khartoum", ("khartoum", "omdurman", "bahri", "الخرطوم", "أم درمان", "بحري")),
    ("Darfur", ("darfur", "el fasher", "al fasher", "nyala", "geneina", "دارفور", "الفاشر", "نيالا", "الجنينة")),
    ("Kordofan", ("kordofan", "el obeid", "al obeid", "كردفان", "الأبيض")),
    ("Gezira", ("gezira", "al jazirah", "wad madani", "ولاية الجزيرة", "ود مدني")),
    ("Red Sea", ("port sudan", "red sea", "suakin", "بورتسودان", "بورسودان", "البحر الأحمر", "سواكن")),
    ("Kassala", ("kassala", "كسلا")), ("Gedaref", ("gedaref", "القضارف")),
    ("Northern", ("northern state", "dongola", "الولاية الشمالية", "دنقلا")),
    ("River Nile", ("river nile state", "atbara", "ولاية نهر النيل", "عطبرة")),
    ("Blue Nile", ("blue nile", "damazin", "النيل الأزرق", "الدمازين")),
    ("Sennar", ("sennar", "singa", "سنار", "سنجة")),
    ("White Nile", ("white nile", "kosti", "النيل الأبيض", "كوستي")),
]
STOPWORDS = {"the", "and", "for", "from", "with", "that", "this", "into", "after", "sudan", "sudanese", "news", "على", "في", "من", "إلى", "عن", "السودان", "السوداني", "السودانية", "بعد", "مع"}
CATEGORY_AR = {"Sudan News": "أخبار السودان", "War & Security": "الحرب والأمن", "Politics": "سياسة", "Economy": "اقتصاد", "Agriculture": "زراعة", "Humanitarian": "إنساني", "Health": "صحة", "Education": "تعليم", "Culture": "ثقافة", "Sport": "رياضة", "Analysis": "تحليل", "International": "دولي", "Official": "رسمي"}


def clean_text(value: str | None) -> str:
    return re.sub(r"\s+", " ", html.unescape(HTML_TAG.sub(" ", value or ""))).strip()


def detect_language(text: str, fallback: str = "en") -> str:
    return "ar" if len(ARABIC_RANGE.findall(text or "")) / max(len(text or ""), 1) > 0.18 else "en"


def context_text(text: str) -> str:
    # Neither the White House nor the Al Jazeera publisher is a Sudanese place.
    return re.sub(r"البيت\s+الأبيض|الجزيرة\s+نت|قناة\s+الجزيرة", "", clean_text(text).lower())


def has_term(text: str, term: str) -> bool:
    if term.isascii():
        return bool(re.search(r"(?<!\w)" + re.escape(term) + r"(?:s|es)?(?!\w)", text))
    return bool(re.search(r"(?<!\w)(?:[وفبلك]?ال|[وفبلك])?" + re.escape(term) + r"\w*(?!\w)", text))


def classify_sudan_relevance(title: str, description: str = "") -> tuple[bool, str]:
    text = context_text(f"{title} {description}")
    south = any(has_term(text, term) for term in SOUTH_SUDAN_TERMS)
    strong_text = re.sub(r"النيل الأبيض|النيل الأزرق", "", text)
    strong_sudan = any(has_term(strong_text, term) for term in SUDAN_CONTEXT_TERMS)
    # A separate Sudan mention retains bilateral/border reporting, including
    # Arabic stories that do not name one of our listed cities or officials.
    without_south = re.sub(r"south\s+sudan(?:ese)?|جنوب\s+(?:السودان|سوداني\w*)", "", text)
    strong_sudan = strong_sudan or bool(re.search(r"\b(?:sudan(?:ese)?|السودان\w*|سوداني\w*)\b", without_south))
    general_sudan = any(has_term(text, term) for term in SUDAN_TERMS + SUDAN_AR_TERMS)
    if south and not strong_sudan:
        return False, "south_sudan_domestic"
    if strong_sudan or (general_sudan and not south):
        return True, "sudan_context"
    return False, "no_sudan_context"


def classify_topic(text: str, default: str) -> str:
    value = context_text(text)
    specialties = [
        ('Agriculture', ('agricultural', 'agriculture', 'farm', 'farmer', 'crop', 'irrigation', 'زراع', 'مزارع', 'محاصيل', 'ري الزراعي')),
        ('Education', ('education', 'school', 'university', 'student', 'تعليم', 'مدارس', 'جامعة', 'جامعات', 'طلاب')),
        ('Health', ('health', 'healthcare', 'hospital', 'clinic', 'cholera', 'outbreak', 'صحة', 'الصحي', 'مستشف', 'كوليرا', 'وباء')),
        ('Culture', ('culture', 'music', 'film', 'photographer', 'heritage', 'festival', 'museum', 'ثقافة', 'موسيق', 'سينما', 'تراث', 'مهرجان')),
        ('Sport', ('sport', 'football', 'league', 'رياضة', 'رياضي', 'كرة', 'دوري', 'المريخ', 'الهلال')),
        ('Economy', ('economy', 'economic', 'currency', 'gold', 'trade', 'اقتصاد', 'عملة', 'ذهب', 'أسعار', 'تجارة')),
    ]
    for topic, terms in specialties:
        if any(has_term(value, term) for term in terms):
            return topic
    for topic, terms in TOPIC_RULES:
        if any(has_term(value, term) for term in terms):
            return topic
    return default


def classify_geography(text: str) -> list[str]:
    value = context_text(text)
    places = [place for place, terms in GEOGRAPHY_RULES if any(has_term(value, term) for term in terms)]
    return places or ["National"]


def normalize_url(url: str) -> str:
    parsed = urllib.parse.urlsplit((url or "").strip())
    query = urllib.parse.parse_qsl(parsed.query, keep_blank_values=True)
    query = [(k, v) for k, v in query if not k.lower().startswith("utm_") and k.lower() not in {"fbclid", "gclid"}]
    return urllib.parse.urlunsplit((parsed.scheme.lower(), parsed.netloc.lower(), parsed.path.rstrip("/") or "/", urllib.parse.urlencode(query), ""))


def parse_date(value: str | None) -> dt.datetime:
    if isinstance(value, (dt.datetime, dt.date)):
        value = value.isoformat()
    if value:
        try:
            parsed = email.utils.parsedate_to_datetime(value)
            if parsed.tzinfo is None:
                parsed = parsed.replace(tzinfo=dt.timezone.utc)
            return parsed.astimezone(dt.timezone.utc)
        except (TypeError, ValueError, OverflowError):
            try:
                return dt.datetime.fromisoformat(value.replace("Z", "+00:00")).astimezone(dt.timezone.utc)
            except (ValueError, AttributeError):
                pass
    # Undated stories must not become new every time the feed is fetched.
    return dt.datetime(1970, 1, 1, tzinfo=dt.timezone.utc)


def media_from_element(item: ET.Element) -> tuple[str, str]:
    for child in item.iter():
        tag = child.tag.rsplit("}", 1)[-1].lower()
        url = child.attrib.get("url") or child.attrib.get("href") or ""
        medium = (child.attrib.get("medium") or child.attrib.get("type") or "").lower()
        is_image = "image" in medium or tag in {"thumbnail", "image"} or bool(re.search(r"\.(jpe?g|png|webp)(\?|$)", url, re.I))
        if url and tag in {"thumbnail", "content", "enclosure", "image"} and is_image:
            return url, "rss_metadata"
    return "", ""


def parse_feed(xml_bytes: bytes) -> list[dict]:
    root = ET.fromstring(xml_bytes)
    nodes = root.findall(".//item") or [n for n in root.iter() if n.tag.rsplit("}", 1)[-1] == "entry"]
    records = []
    for node in nodes:
        fields = {}
        for child in list(node):
            key = child.tag.rsplit("}", 1)[-1].lower()
            value = (child.text or "").strip()
            if key == "link" and not value:
                value = child.attrib.get("href", "")
            fields.setdefault(key, value)
        image, reuse_basis = media_from_element(node)
        records.append({"title": fields.get("title", ""), "link": fields.get("link", ""), "description": fields.get("description") or fields.get("summary") or fields.get("content", ""), "published": fields.get("pubdate") or fields.get("published") or fields.get("updated", ""), "author": fields.get("creator") or fields.get("author", ""), "image": image, "media_reuse_basis": reuse_basis})
    return records


def fetch_feed(url: str, timeout: int = 20) -> bytes | None:
    try:
        request = urllib.request.Request(url, headers={"User-Agent": "Kandaka-Sudan-News-Hub/2.0 (+https://kandaka.com/news/)"})
        with urllib.request.urlopen(request, timeout=timeout) as response:
            return response.read()
    except Exception as exc:
        print(f"  [WARN] {url}: {exc}")
        return None


def cluster_key(title: str) -> str:
    tokens = [t.lower() for t in WORD.findall(clean_text(title)) if len(t) > 2 and t.lower() not in STOPWORDS]
    signature = " ".join(sorted(set(tokens))[:12]) or clean_text(title).lower()
    return hashlib.sha1(signature.encode()).hexdigest()[:12]


def slug_for(title: str, link: str, lang: str) -> str:
    uid = hashlib.md5(normalize_url(link).encode()).hexdigest()
    if lang == "ar":
        return f"ar-news-{uid[:10]}"
    slug = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")[:60]
    return f"{slug or 'sudan-news'}-{uid[:6]}"


def load_sources(path: Path = REGISTRY) -> list[dict]:
    sources = (yaml.safe_load(path.read_text(encoding="utf-8")) or {}).get("sources", [])
    required, seen = {"id", "name", "lang", "source_class", "enabled", "media_policy"}, set()
    for source in sources:
        missing = required - set(source)
        if missing:
            raise ValueError(f"Source missing {sorted(missing)}: {source}")
        if source["id"] in seen:
            raise ValueError(f"Duplicate source id: {source['id']}")
        if source["enabled"] and not source.get("url"):
            raise ValueError(f"Enabled source has no URL: {source['id']}")
        seen.add(source["id"])
    return sources


def candidate_from_item(source: dict, item: dict) -> dict | None:
    title, description = clean_text(item.get("title")), clean_text(item.get("description"))[:420]
    link = normalize_url(item.get("link", ""))
    if not title or urllib.parse.urlsplit(link).scheme not in {"http", "https"}:
        return None
    relevant, reason = classify_sudan_relevance(title, description)
    if source.get("filter", True) and not relevant:
        return None
    if not source.get("filter", True) and reason == "south_sudan_domestic":
        return None
    lang = detect_language(title, source["lang"])
    combined = f"{title} {description}"
    source_class = source["source_class"]
    status = "Official statement" if source_class == "official" else "Reporting"
    if source_class in {"humanitarian", "international_institution"}:
        status = "Institutional update"
    if source_class in {"analysis", "research"}:
        status = "Analysis"
    image = item.get("image", "") if source["media_policy"] == "rss_metadata" else ""
    return {"title": title, "description": description, "link": link, "lang": lang, "source": source["name"], "source_id": source["id"], "publisher": source.get("publisher", source["name"]), "source_class": source_class, "topic": classify_topic(title, classify_topic(combined, source.get("default_topic", "Sudan News"))), "geography": classify_geography(combined), "published": parse_date(item.get("published")), "status": status, "image": image, "media_reuse_basis": item.get("media_reuse_basis", "") if image else "", "cluster_id": cluster_key(title), "author": clean_text(item.get("author"))}


def cluster_candidates(candidates: list[dict]) -> list[dict]:
    grouped = []
    for candidate in sorted(candidates, key=lambda c: (c['published'], c['link']), reverse=True):
        group = next((g for g in grouped if same_story(candidate, g[0])), None)
        if group is None:
            grouped.append([candidate])
        else:
            group.append(candidate)
    weight = {"sudanese_journalism": 6, "sudanese_diaspora": 5, "international_journalism": 4, "regional_journalism": 4, "research": 3, "analysis": 3, "humanitarian": 2, "international_institution": 1, "official": 1}
    leads = []
    for cluster in grouped:
        cluster.sort(key=lambda c: (weight.get(c["source_class"], 0), c["published"]), reverse=True)
        lead = cluster[0]
        related = list({x["source_id"]: {"source": x["source"], "link": x["link"]} for x in cluster[1:] if x["source_id"] != lead["source_id"]}.values())[:5]
        lead["related_sources"] = related
        lead["corroboration_count"] = 1 + len(related)
        if lead["status"] == "Verified reporting":
            lead["status"] = "Reporting"
        leads.append(lead)
    return sorted(leads, key=lambda c: c["published"], reverse=True)


def same_story(left, right):
    """Conservative same-language headline matching; this is not fact verification."""
    if left['lang'] != right['lang'] or abs((left['published'] - right['published']).total_seconds()) > 72 * 3600:
        return False
    if left['cluster_id'] == right['cluster_id']:
        return True
    tokens = lambda c: {t.lower() for t in WORD.findall(c['title']) if len(t) > 2 and t.lower() not in STOPWORDS}
    a, b = tokens(left), tokens(right)
    numbers = lambda c: set(re.findall(r'\d+', c['title']))
    if numbers(left) != numbers(right):
        return False
    # Avoid combining similarly worded events in different named regions.
    places_a, places_b = set(left['geography']) - {'National'}, set(right['geography']) - {'National'}
    if places_a and places_b and places_a.isdisjoint(places_b):
        return False
    return len(a & b) >= 5 and len(a & b) / max(len(a | b), 1) >= .72


def write_candidate(candidate: dict, content_dir: Path = CONTENT_DIR, existing_path: Path | None = None) -> Path:
    content_dir.mkdir(parents=True, exist_ok=True)
    path = existing_path or content_dir / f"{slug_for(candidate['title'], candidate['link'], candidate['lang'])}.{candidate['lang']}.md"
    front = {"title": candidate["title"], "date": candidate["published"].strftime("%Y-%m-%dT%H:%M:%SZ"), "description": candidate["description"], "source": candidate["source"], "source_id": candidate["source_id"], "source_class": candidate["source_class"], "link": candidate["link"], "category": candidate["topic"], "geography": candidate["geography"], "language": candidate["lang"], "status": candidate["status"], "cluster_id": candidate["cluster_id"], "corroboration_count": candidate["corroboration_count"], "draft": False}
    if candidate.get("author"):
        front["author"] = candidate["author"]
    if candidate.get("image"):
        front.update({"image": candidate["image"], "media_source": candidate["link"], "media_reuse_basis": candidate["media_reuse_basis"], "media_attribution": candidate["source"]})
    if candidate.get("related_sources"):
        front["related_sources"] = candidate["related_sources"]
    if candidate["lang"] == "ar":
        front["clabel"] = CATEGORY_AR.get(candidate["topic"], candidate["topic"])
    body = candidate["description"] + f"\n\n[{candidate['source']} →]({candidate['link']})"
    path.write_text("---\n" + yaml.safe_dump(front, allow_unicode=True, sort_keys=False) + "---\n\n" + body.strip() + "\n", encoding="utf-8")
    return path


def archive_candidates(sources, content_dir=CONTENT_DIR):
    """Keep old URLs, but recheck relevance and deduplicate the visible feed."""
    by_id = {s['id']: s for s in sources}
    by_name = {s['name']: s for s in sources}
    candidates, paths = [], {}
    for path in sorted(content_dir.glob('*.md')):
        text = path.read_text(encoding='utf-8')
        if not text.startswith('---'):
            continue
        try:
            front = yaml.safe_load(text.split('---', 2)[1]) or {}
        except (yaml.YAMLError, IndexError):
            continue
        if front.get('draft') or not front.get('link'):
            continue
        lang = detect_language(front.get('title', ''))
        key = (lang, normalize_url(front['link']))
        paths.setdefault(key, path)
        source = by_id.get(front.get('source_id')) or by_name.get(front.get('source'))
        if not source:
            continue
        item = dict(front, published=front.get('date'))
        candidate = candidate_from_item(source, item)
        if candidate:
            candidates.append(candidate)
    return candidates, paths


def select_balanced(candidates, limit=40):
    """A publisher gets one opening card, two overall; institutions get three."""
    remaining = sorted(candidates, key=lambda c: (c['published'], c['link']), reverse=True)
    selected, publishers, topics, regions = [], defaultdict(int), defaultdict(int), defaultdict(int)
    institutional = 0
    opening_size = min(3, len({c.get('publisher', c['source']) for c in remaining}))
    while remaining and len(selected) < limit:
        eligible = []
        for item in remaining:
            publisher = item.get('publisher', item['source'])
            institution = item['source_class'] in {'official', 'humanitarian', 'international_institution'}
            if publishers[publisher] >= (1 if len(selected) < opening_size else 2) or (institution and institutional >= 3):
                continue
            # Freshness remains meaningful; diversity bonuses cannot revive stale news.
            age = (remaining[0]['published'] - item['published']).total_seconds() / 86400
            score = -age - 5 * publishers[publisher] + 2 / (1 + topics[item['topic']])
            score += 4 if classify_sudan_relevance(item['title'])[0] else 0
            score += max(1 / (1 + regions[g]) for g in item['geography'])
            eligible.append((score, item))
        if not eligible:
            break
        chosen = max(eligible, key=lambda pair: pair[0])[1]
        remaining.remove(chosen)
        selected.append(chosen)
        publishers[chosen.get('publisher', chosen['source'])] += 1
        topics[chosen['topic']] += 1
        for region in chosen['geography']:
            regions[region] += 1
        institutional += chosen['source_class'] in {'official', 'humanitarian', 'international_institution'}
    return selected


def feed_card(item):
    """Page-shaped data lets home and news share the same card template."""
    params = {key: item.get(key, '') for key in ('description', 'source', 'source_id', 'source_class', 'link', 'status', 'geography', 'image', 'media_reuse_basis', 'related_sources')}
    params.update(category=item['topic'], clabel=CATEGORY_AR.get(item['topic'], item['topic']), language=item['lang'], media_attribution=item['source'])
    return dict(Title=item['title'], Lang=item['lang'], Date=item['published'].isoformat(), Permalink=item['link'], Params=params)


def build_snapshot(candidates, now=None):
    now = now or dt.datetime.now(dt.timezone.utc)
    cutoff = now - dt.timedelta(days=30)
    unique = {}
    # Later (freshly fetched) records replace old archive metadata for the same URL.
    for item in candidates:
        if cutoff <= item['published'] <= now:
            unique[(item['lang'], normalize_url(item['link']))] = item
    leads = cluster_candidates(list(unique.values()))
    snapshot = {'updated': now.isoformat(), 'window_days': 30}
    for lang in ('en', 'ar'):
        language_candidates = [c for c in leads if c['lang'] == lang]
        latest = language_candidates[:150]
        balanced = select_balanced(language_candidates)
        snapshot[lang] = {'balanced': [feed_card(c) for c in balanced], 'latest': [feed_card(c) for c in latest], 'publishers': len({c.get('publisher', c['source']) for c in balanced})}
    return snapshot


def collect_source(source):
    raw = fetch_feed(source['url'])
    health = dict(id=source['id'], language=source['lang'], status='fetch_failed', items=0, accepted=0)
    if raw is None:
        return [], health
    try:
        items = parse_feed(raw)
    except ET.ParseError:
        health['status'] = 'invalid_feed'
        return [], health
    health['items'] = len(items)
    # Inspect the entire feed before applying the relevant-story quota.
    accepted = [c for item in items if (c := candidate_from_item(source, item))]
    accepted.sort(key=lambda c: c['published'], reverse=True)
    accepted = accepted[:int(source.get('max_items', 20))]
    health.update(accepted=len(accepted), status='ok' if items else 'empty_feed')
    return accepted, health


def main(snapshot_only=False) -> int:
    from quarantine_south_sudan import quarantine_content
    if not snapshot_only:
        quarantine_content(ROOT / "content")
    sources, candidates, health = load_sources(), [], []
    archived, paths = archive_candidates(sources)
    enabled = [s for s in sources if s["enabled"]]
    print(f"Fetching {len(enabled)} enabled sources ({len(sources)} registered)...")
    with ThreadPoolExecutor(max_workers=8) as pool:
        for accepted, report in pool.map(collect_source, enabled):
            candidates.extend(accepted)
            health.append(report)
            print(f"  {report['id']}: {report['status']}, {report['accepted']} relevant")
    leads = cluster_candidates(candidates)
    for candidate in leads:
        if not snapshot_only and candidate['published'].year > 1970:
            write_candidate(candidate, existing_path=paths.get((candidate['lang'], candidate['link'])))
    by_lang = defaultdict(int)
    for candidate in leads:
        by_lang[candidate["lang"]] += 1
    snapshot = build_snapshot(archived + candidates)
    (ROOT / 'data/news_feed.json').write_text(json.dumps(snapshot, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    (ROOT / 'data/news_source_health.json').write_text(json.dumps(dict(updated=snapshot['updated'], sources=health), indent=2) + '\n', encoding='utf-8')
    for lang in ('en', 'ar'):
        feed = snapshot[lang]
        print(f"{lang.upper()}: {len(feed['balanced'])} balanced cards / {feed['publishers']} publishers / {len(feed['latest'])} latest")
    # Recent archive data keeps the site available through a temporary feed outage.
    return 0 if any(snapshot[l]['latest'] for l in ('en', 'ar')) or not enabled else 1


if __name__ == "__main__":
    sys.exit(main(snapshot_only='--snapshot-only' in sys.argv))

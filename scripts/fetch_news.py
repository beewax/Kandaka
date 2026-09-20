#!/usr/bin/env python3
"""Kandaka Sudan News Hub Phase 1: attributed RSS/Atom aggregation."""

from __future__ import annotations

import datetime as dt
import email.utils
import hashlib
import html
import re
import sys
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from collections import defaultdict
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
    "white nile", "river nile", "nuba mountains", "burhan", "hemedti",
    "rapid support forces", "rsf", "sudanese armed forces",
)
SUDAN_AR_TERMS = (
    "السودان", "سوداني", "الخرطوم", "أم درمان", "بورتسودان", "بورسودان",
    "دارفور", "كردفان", "الجزيرة", "كسلا", "القضارف", "عطبرة", "الفاشر",
    "الأبيض", "ود مدني", "النيل الأزرق", "النيل الأبيض", "نهر النيل",
    "جبال النوبة", "البرهان", "حميدتي", "الدعم السريع",
)
SOUTH_SUDAN_TERMS = (
    "south sudan", "south sudanese", "juba", "salva kiir", "riek machar",
    "جنوب السودان", "جنوب سوداني", "جوبا", "سلفا كير", "رياك مشار",
)
SUDAN_CONTEXT_TERMS = tuple(t for t in SUDAN_TERMS if t not in {"sudan", "sudanese"}) + tuple(
    t for t in SUDAN_AR_TERMS if t not in {"السودان", "سوداني"}
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
    ("Gezira", ("gezira", "al jazirah", "wad madani", "الجزيرة", "ود مدني")),
    ("Red Sea", ("port sudan", "red sea", "suakin", "بورتسودان", "بورسودان", "البحر الأحمر", "سواكن")),
    ("Kassala", ("kassala", "كسلا")), ("Gedaref", ("gedaref", "القضارف")),
    ("Northern", ("northern state", "dongola", "الولاية الشمالية", "دنقلا")),
    ("River Nile", ("river nile", "atbara", "نهر النيل", "عطبرة")),
    ("Blue Nile", ("blue nile", "damazin", "النيل الأزرق", "الدمازين")),
    ("Sennar", ("sennar", "singa", "سنار", "سنجة")),
    ("White Nile", ("white nile", "kosti", "النيل الأبيض", "كوستي")),
]
STOPWORDS = {"the", "and", "for", "from", "with", "that", "this", "into", "after", "sudan", "sudanese", "news", "على", "في", "من", "إلى", "عن", "السودان", "السوداني", "السودانية", "بعد", "مع"}
CATEGORY_AR = {"Sudan News": "أخبار السودان", "War & Security": "الحرب والأمن", "Politics": "سياسة", "Economy": "اقتصاد", "Agriculture": "زراعة", "Humanitarian": "إنساني", "Health": "صحة", "Education": "تعليم", "Culture": "ثقافة", "Sport": "رياضة", "Analysis": "تحليل", "International": "دولي", "Official": "رسمي"}


def clean_text(value: str | None) -> str:
    return re.sub(r"\s+", " ", html.unescape(HTML_TAG.sub(" ", value or ""))).strip()


def detect_language(text: str, fallback: str = "en") -> str:
    return "ar" if len(ARABIC_RANGE.findall(text or "")) / max(len(text or ""), 1) > 0.18 else fallback


def classify_sudan_relevance(title: str, description: str = "") -> tuple[bool, str]:
    text = clean_text(f"{title} {description}").lower()
    south = any(term in text for term in SOUTH_SUDAN_TERMS)
    strong_sudan = any(term in text for term in SUDAN_CONTEXT_TERMS)
    # A separate Sudan mention retains bilateral/border reporting, including
    # Arabic stories that do not name one of our listed cities or officials.
    without_south = re.sub(r"south\s+sudan(?:ese)?|جنوب\s+(?:السودان|سوداني\w*)", "", text)
    strong_sudan = strong_sudan or bool(re.search(r"\b(?:sudan(?:ese)?|السودان\w*|سوداني\w*)\b", without_south))
    general_sudan = any(term in text for term in SUDAN_TERMS + SUDAN_AR_TERMS)
    if south and not strong_sudan:
        return False, "south_sudan_domestic"
    if strong_sudan or (general_sudan and not south):
        return True, "sudan_context"
    return False, "no_sudan_context"


def classify_topic(text: str, default: str) -> str:
    value = clean_text(text).lower()
    for topic, terms in TOPIC_RULES:
        if any(term in value for term in terms):
            return topic
    return default


def classify_geography(text: str) -> list[str]:
    value = clean_text(text).lower()
    places = [place for place, terms in GEOGRAPHY_RULES if any(term in value for term in terms)]
    return places or ["National"]


def normalize_url(url: str) -> str:
    parsed = urllib.parse.urlsplit((url or "").strip())
    query = urllib.parse.parse_qsl(parsed.query, keep_blank_values=True)
    query = [(k, v) for k, v in query if not k.lower().startswith("utm_") and k.lower() not in {"fbclid", "gclid"}]
    return urllib.parse.urlunsplit((parsed.scheme.lower(), parsed.netloc.lower(), parsed.path.rstrip("/") or "/", urllib.parse.urlencode(query), ""))


def parse_date(value: str | None) -> dt.datetime:
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
    return dt.datetime.now(dt.timezone.utc)


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
    if not title or not link:
        return None
    relevant, reason = classify_sudan_relevance(title, description)
    if source.get("filter", True) and not relevant:
        return None
    if not source.get("filter", True) and reason == "south_sudan_domestic":
        return None
    lang = detect_language(title, source["lang"])
    combined = f"{title} {description}"
    source_class = source["source_class"]
    status = "Official statement" if source_class == "official" else "Verified reporting"
    if source_class in {"analysis", "research"}:
        status = "Analysis"
    image = item.get("image", "") if source["media_policy"] == "rss_metadata" else ""
    return {"title": title, "description": description, "link": link, "lang": lang, "source": source["name"], "source_id": source["id"], "source_class": source_class, "topic": classify_topic(combined, source.get("default_topic", "Sudan News")), "geography": classify_geography(combined), "published": parse_date(item.get("published")), "status": status, "image": image, "media_reuse_basis": item.get("media_reuse_basis", "") if image else "", "cluster_id": cluster_key(title), "author": clean_text(item.get("author"))}


def cluster_candidates(candidates: list[dict]) -> list[dict]:
    grouped = defaultdict(list)
    for candidate in candidates:
        grouped[candidate["cluster_id"]].append(candidate)
    weight = {"sudanese_journalism": 6, "sudanese_diaspora": 5, "international_journalism": 4, "regional_journalism": 4, "research": 3, "analysis": 3, "humanitarian": 2, "international_institution": 1, "official": 1}
    leads = []
    for cluster in grouped.values():
        cluster.sort(key=lambda c: (weight.get(c["source_class"], 0), c["published"]), reverse=True)
        lead = cluster[0]
        related = [{"source": x["source"], "link": x["link"]} for x in cluster[1:] if x["source_id"] != lead["source_id"]][:5]
        lead["related_sources"] = related
        lead["corroboration_count"] = 1 + len(related)
        if related and lead["status"] == "Verified reporting":
            lead["status"] = f"Confirmed by {lead['corroboration_count']} sources"
        leads.append(lead)
    return sorted(leads, key=lambda c: c["published"], reverse=True)


def write_candidate(candidate: dict, content_dir: Path = CONTENT_DIR) -> Path:
    content_dir.mkdir(parents=True, exist_ok=True)
    path = content_dir / f"{slug_for(candidate['title'], candidate['link'], candidate['lang'])}.{candidate['lang']}.md"
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


def main() -> int:
    from quarantine_south_sudan import quarantine_content
    quarantine_content(ROOT / "content")
    sources, candidates, failures, rejected = load_sources(), [], [], 0
    enabled = [s for s in sources if s["enabled"]]
    print(f"Fetching {len(enabled)} enabled sources ({len(sources)} registered)...")
    for source in enabled:
        print(f"  {source['name']}...")
        xml = fetch_feed(source["url"])
        if not xml:
            failures.append(source["id"]); continue
        try:
            items = parse_feed(xml)
        except ET.ParseError as exc:
            print(f"    [WARN] invalid feed: {exc}"); failures.append(source["id"]); continue
        accepted = 0
        for item in items[: int(source.get("max_items", 20))]:
            candidate = candidate_from_item(source, item)
            if candidate:
                candidates.append(candidate); accepted += 1
            else:
                rejected += 1
        print(f"    -> {accepted} candidates")
    leads = cluster_candidates(candidates)
    for candidate in leads:
        write_candidate(candidate)
    by_lang = defaultdict(int)
    for candidate in leads:
        by_lang[candidate["lang"]] += 1
    print(f"Done. EN: {by_lang['en']} | AR: {by_lang['ar']} | clustered/rejected: {len(candidates)-len(leads)}/{rejected} | feed failures: {len(failures)}")
    if failures:
        print("Failed sources: " + ", ".join(failures))
    return 0 if leads or not enabled else 1


if __name__ == "__main__":
    sys.exit(main())

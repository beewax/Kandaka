#!/usr/bin/env python3
"""
Fix Arabic post frontmatter:
- category: "????..." → proper English slug
- clabel: (missing) → Arabic display label
- source: "????..." → proper source name from link URL
"""
import re
import os
import glob

DIRS = [
    r"C:\Users\Abdulla\Kandaka\content\posts",
    r"C:\Users\Abdulla\Kandaka\content\news",
]

# Source domain → proper name
SOURCE_MAP = {
    "dabangasudan.org": "دبنقا عربي",
    "alrakoba.net": "الراكوبة",
    "sudantribune.net": "سودان تريبيون",
    "sudaress.com": "سودارس",
    "alnilin.com": "النيلين",
    "altaghyeer.info": "التغيير",
    "almoghar.net": "المغترب",
}

# Keyword → (English slug, Arabic label)
# Checked in order — first match wins
CATEGORY_RULES = [
    # War / military
    (["مسيرات", "طائرة مسيرة", "هجوم", "مذبحة", "قتل", "قتلى", "ضحايا", "اشتباك",
      "نزاع", "حرب", "معركة", "درفور", "دارفور", "كردفان", "الجيش", "الدعم السريع",
      "ضربة", "مجزرة", "اغتيال"], "war", "حرب"),
    # Politics / governance
    (["سياس", "برهان", "حكومة", "برلمان", "تحالف", "قوى سياسية", "أديس أبابا",
      "مفاوض", "سلام", "اتفاق", "ثورة", "انتقال", "الكتلة الديمقراطية",
      "الاسلامية", "المسار", "الهدنة", "انقلاب", "حوار سياسي"], "politics", "سياسة"),
    # International
    (["إيران", "إيراني", "أمريكا", "أمريكي", "إسرائيل", "إسرائيلي", "لبنان",
      "واشنطن", "طهران", "الكونغرس", "الأمم المتحدة", "دولي", "دبلوماسي",
      "عقوبات", "اتحاد أوروبي", "الكويت", "البحرين"], "international", "دولي"),
    # Humanitarian / refugees
    (["لاجئ", "نازح", "إنساني", "مجاعة", "غوث", "مفوضية", "اليونيسف",
      "منظمات حقوقية", "حقوق الإنسان", "ليبيا", "مصر", "مخيم"], "humanitarian", "إنساني"),
    # Economy
    (["اقتصاد", "اقتصادي", "مال", "بنك", "استثمار", "تجارة", "نفط", "كهرباء",
      "إيرادات", "ميزانية", "اتفاقية تمويل", "وزير المالية", "زكاة"], "economy", "اقتصاد"),
    # Culture / arts / literature
    (["أدب", "رواية", "فنان", "فنانون", "ثقافة", "معرض", "شعر", "موسيقى",
      "فيلم", "كاتب", "الطيب صالح", "تشكيلي", "كوشيات", "هوية"], "analysis", "ثقافة"),
    # Science / health / tech
    (["صحة", "طب", "لقاح", "مرض", "ذكاء اصطناعي", "تقنية", "علم"], "analysis", "تحليل"),
]

DEFAULT_CATEGORY = ("general", "عام")


def classify(title, description=""):
    text = (title or "") + " " + (description or "")
    for keywords, slug, label in CATEGORY_RULES:
        for kw in keywords:
            if kw in text:
                return slug, label
    return DEFAULT_CATEGORY


def get_source_from_link(link):
    if not link:
        return None
    for domain, name in SOURCE_MAP.items():
        if domain in link:
            return name
    return None


def has_question_marks(val):
    return val and "?" in val


def fix_file(path):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # Only process .ar.md files
    if not path.endswith(".ar.md"):
        return False

    # Parse frontmatter (between first two ---)
    fm_match = re.match(r"^---\r?\n(.*?)\r?\n---", content, re.DOTALL)
    if not fm_match:
        return False

    fm = fm_match.group(1)
    changed = False

    # Extract title and description for classification
    title_m = re.search(r'^title:\s*["\']?(.*?)["\']?\s*$', fm, re.MULTILINE)
    desc_m = re.search(r'^description:\s*["\']?(.*?)["\']?(?:\s*$)', fm, re.MULTILINE)
    link_m = re.search(r'^link:\s*["\']?(.*?)["\']?\s*$', fm, re.MULTILINE)
    ext_m = re.search(r'^externalLink:\s*["\']?(.*?)["\']?\s*$', fm, re.MULTILINE)

    title = title_m.group(1).strip() if title_m else ""
    description = desc_m.group(1).strip() if desc_m else ""
    link = (link_m.group(1).strip() if link_m else "") or (ext_m.group(1).strip() if ext_m else "")

    # Fix source if it contains ?
    source_m = re.search(r'^source:\s*(.*?)\s*$', fm, re.MULTILINE)
    if source_m and has_question_marks(source_m.group(1)):
        new_source = get_source_from_link(link)
        if new_source:
            fm = re.sub(
                r'^source:\s.*$',
                f'source: "{new_source}"',
                fm, flags=re.MULTILINE
            )
            changed = True

    # Fix category if it contains ?
    cat_m = re.search(r'^category:\s*(.*?)\s*$', fm, re.MULTILINE)
    if cat_m and has_question_marks(cat_m.group(1)):
        slug, label = classify(title, description)
        fm = re.sub(
            r'^category:\s.*$',
            f'category: {slug}',
            fm, flags=re.MULTILINE
        )
        changed = True

        # Add clabel if not present
        if "clabel:" not in fm:
            fm = re.sub(
                r'^(language:.*?)$',
                r'\1\nclabel: ' + label,
                fm, flags=re.MULTILINE
            )
        changed = True

    # Also fix source in body (markdown link [?????](url))
    new_content = content[:fm_match.start(1)] + fm + content[fm_match.start(1) + len(fm_match.group(1)):]

    if changed:
        with open(path, "w", encoding="utf-8") as f:
            f.write(new_content)
        return True
    return False


fixed = 0
skipped = 0
for d in DIRS:
    for path in glob.glob(os.path.join(d, "*.ar.md")):
        if fix_file(path):
            print(f"  FIXED: {os.path.basename(path)}")
            fixed += 1
        else:
            skipped += 1

print(f"\nDone. Fixed: {fixed}, Skipped (already OK): {skipped}")

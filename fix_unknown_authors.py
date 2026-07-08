import os, re, json
import xml.etree.ElementTree as ET

CALIBRE_ROOT = "D:\\New Caliber Library"
BASE_URL = "https://pub-a5e3b47fe87749f491660d68e2029284.r2.dev"

def normalise(s):
    return re.sub(r"[^a-z0-9]", "", (s or "").lower())

def get_author_from_opf(opf_path):
    try:
        tree = ET.parse(opf_path)
        root = tree.getroot()
        ns = {"dc": "http://purl.org/dc/elements/1.1/"}
        creators = root.findall(".//dc:creator", ns)
        if creators:
            authors = [c.text.strip() for c in creators if c.text and c.text.strip()]
            return "; ".join(authors)
    except Exception:
        pass
    return None

def find_opf_for_title(title):
    norm_title = normalise(title)
    best_opf = None
    best_score = 0
    for author_dir in os.listdir(CALIBRE_ROOT):
        author_path = os.path.join(CALIBRE_ROOT, author_dir)
        if not os.path.isdir(author_path):
            continue
        for book_dir in os.listdir(author_path):
            book_path = os.path.join(author_path, book_dir)
            if not os.path.isdir(book_path):
                continue
            norm_dir = normalise(book_dir)
            overlap = sum(1 for c in norm_title if c in norm_dir)
            score = overlap / max(len(norm_title), 1)
            if score > best_score and score > 0.5:
                opf = os.path.join(book_path, "metadata.opf")
                if os.path.exists(opf):
                    best_score = score
                    best_opf = opf
    return best_opf, best_score

script_dir = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(script_dir, "data", "library.json")
with open(json_path, encoding="utf-8") as f:
    lib = json.load(f)

books = lib["books"]
unknown = [b for b in books if b.get("author", "").strip() in ["Unknown", "unknown", ""]]
print("Unknown author entries: " + str(len(unknown)))
print()

fixed = 0
still_unknown = []

for book in unknown:
    title = book.get("title", "")
    opf_path, score = find_opf_for_title(title)
    if not opf_path:
        still_unknown.append(title)
        continue
    author = get_author_from_opf(opf_path)
    if not author or author.strip().lower() in ["unknown", ""]:
        still_unknown.append(title)
        continue
    print("FIXED: " + title[:55])
    print("  Author: " + author)
    book["author"] = author
    fixed += 1

with open(json_path, "w", encoding="utf-8") as f:
    json.dump(lib, f, ensure_ascii=False, indent=2)

print()
print("=" * 60)
print("Fixed: " + str(fixed) + "/" + str(len(unknown)))
print("Still unknown: " + str(len(still_unknown)))
print()
if still_unknown:
    print("STILL UNKNOWN:")
    for t in still_unknown:
        print("  - " + t)
print()
print("library.json updated. Run git add/commit/push to deploy.")

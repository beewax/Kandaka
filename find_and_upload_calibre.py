import boto3, os, json, re, shutil
from botocore.config import Config

R2_ACCESS_KEY_ID     = "b1f53194ad1d18f9a2c76ed23c39682d"
R2_SECRET_ACCESS_KEY = "85984c671385eef6067149ad7316e0a949f36e42fbf842a0909b098c5f2c0ac6"
ACCOUNT_ID           = "971f88758f6c5f23f2e77a3aa3fb1663"
R2_BUCKET_NAME       = "nilebookstore-books"
ENDPOINT_URL         = "https://" + ACCOUNT_ID + ".r2.cloudflarestorage.com"
BASE_URL             = "https://pub-a5e3b47fe87749f491660d68e2029284.r2.dev"
CALIBRE_ROOT         = "D:\\New Caliber Library"
SUDAN_PDFS           = "C:\\Users\\Abdulla\\Documents\\Sudan PDFs"

s3 = boto3.client(
    "s3",
    endpoint_url=ENDPOINT_URL,
    aws_access_key_id=R2_ACCESS_KEY_ID,
    aws_secret_access_key=R2_SECRET_ACCESS_KEY,
    config=Config(signature_version="s3v4"),
    region_name="auto",
)

def slugify(title):
    s = re.sub(r"[^a-z0-9]+", "-", title.lower())
    return s.strip("-")[:60]

def is_bad_source(src):
    if not src:
        return True
    if "r2.dev" in src:
        return False
    if src == "https://www.academia.edu":
        return True
    if "/author/" in src or "/brands/" in src or "/tag/" in src:
        return True
    if re.match(r"https?://[^/]+/?$", src):
        return True
    return False

def normalise(s):
    return re.sub(r"[^a-z0-9]", "", (s or "").lower())

def find_in_calibre(title):
    norm_title = normalise(title)
    best_match = None
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
                for f in os.listdir(book_path):
                    if f.endswith((".pdf", ".epub")):
                        best_score = score
                        best_match = os.path.join(book_path, f)
    return best_match, best_score

def upload_file(local_path, key):
    ext = os.path.splitext(local_path)[1].lower()
    content_type = "application/epub+zip" if ext == ".epub" else "application/pdf"
    s3.upload_file(
        local_path, R2_BUCKET_NAME, key,
        ExtraArgs={"ContentType": content_type}
    )
    return BASE_URL + "/" + key

script_dir = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(script_dir, "data", "library.json")
with open(json_path, encoding="utf-8") as f:
    lib = json.load(f)

books = lib["books"]
bad_books = [b for b in books if is_bad_source(b.get("source", ""))]
print("Books with bad/missing source URLs: " + str(len(bad_books)))
print("Scanning Calibre library at: " + CALIBRE_ROOT)
print()

os.makedirs(SUDAN_PDFS, exist_ok=True)

found = 0
uploaded = 0
not_found = []

for book in bad_books:
    title = book.get("title", "")
    local_path, score = find_in_calibre(title)

    if not local_path:
        not_found.append(title)
        continue

    found += 1
    ext = os.path.splitext(local_path)[1].lower()
    key = slugify(title) + ext
    print("FOUND (" + str(round(score*100)) + "%): " + title[:50])
    print("  File: " + os.path.basename(local_path))
    print("  Key:  " + key)

    try:
        r2_url = upload_file(local_path, key)
        dest = os.path.join(SUDAN_PDFS, os.path.basename(local_path))
        if not os.path.exists(dest):
            shutil.copy2(local_path, dest)
        book["source"] = r2_url
        uploaded += 1
        print("  -> " + r2_url)
    except Exception as e:
        print("  UPLOAD FAILED: " + str(e))
    print()

with open(json_path, "w", encoding="utf-8") as f:
    json.dump(lib, f, ensure_ascii=False, indent=2)

print("=" * 60)
print("Found in Calibre: " + str(found) + "/" + str(len(bad_books)))
print("Uploaded to R2:   " + str(uploaded))
print("Not found:        " + str(len(not_found)))
print()
print("NOT FOUND IN CALIBRE (" + str(len(not_found)) + "):")
for t in not_found:
    print("  - " + t)
print()
print("library.json updated. Run git add/commit/push to deploy.")

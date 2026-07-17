import boto3, os, json, shutil
from botocore.config import Config

R2_ACCESS_KEY_ID     = "b1f53194ad1d18f9a2c76ed23c39682d"
R2_SECRET_ACCESS_KEY = "85984c671385eef6067149ad7316e0a949f36e42fbf842a0909b098c5f2c0ac6"
ACCOUNT_ID           = "971f88758f6c5f23f2e77a3aa3fb1663"
R2_BUCKET_NAME       = "nilebookstore-books"
ENDPOINT_URL         = "https://" + ACCOUNT_ID + ".r2.cloudflarestorage.com"
BASE_URL             = "https://pub-a5e3b47fe87749f491660d68e2029284.r2.dev"
DOWNLOADS            = "C:\\Users\\Abdulla\\Downloads"
SUDAN_PDFS           = "C:\\Users\\Abdulla\\Documents\\Sudan PDFs"

s3 = boto3.client("s3", endpoint_url=ENDPOINT_URL,
    aws_access_key_id=R2_ACCESS_KEY_ID,
    aws_secret_access_key=R2_SECRET_ACCESS_KEY,
    config=Config(signature_version="s3v4"), region_name="auto")

FILES = [
    ("Current_Status_of_Agriculture_and_Future.pdf",
     "current-status-agriculture-future-challenges-sudan.pdf",
     "Current Status of Agriculture and Future Challenges in Sudan",
     "Unknown", ["Agriculture", "Economy & Development"],
     "A comprehensive assessment of Sudan's agricultural sector covering irrigated and rain-fed farming systems, productivity gaps, policy constraints, and the reforms needed to close the gap between Sudan's agricultural potential and its actual output.",
     "\u062a\u0642\u064a\u064a\u0645 \u0634\u0627\u0645\u0644 \u0644\u0644\u0642\u0637\u0627\u0639 \u0627\u0644\u0632\u0631\u0627\u0639\u064a \u0627\u0644\u0633\u0648\u062f\u0627\u0646\u064a \u064a\u062a\u0646\u0627\u0648\u0644 \u0623\u0646\u0638\u0645\u0629 \u0627\u0644\u0632\u0631\u0627\u0639\u0629 \u0627\u0644\u0645\u0631\u0648\u064a\u0629 \u0648\u0627\u0644\u0628\u0639\u0644\u064a\u0629 \u0648\u0641\u062c\u0648\u0627\u062a \u0627\u0644\u0625\u0646\u062a\u0627\u062c\u064a\u0629 \u0648\u0627\u0644\u0642\u064a\u0648\u062f \u0627\u0644\u0633\u064a\u0627\u0633\u064a\u0629 \u0648\u0627\u0644\u0625\u0635\u0644\u0627\u062d\u0627\u062a \u0627\u0644\u0644\u0627\u0632\u0645\u0629."),
    ("The_Impact_of_Human_Capital_on_Economic.pdf",
     "impact-human-capital-economic-growth-sudan.pdf",
     "The Impact of Human Capital on Economic Growth: Empirical Evidence from Sudan",
     "Unknown", ["Economy & Development", "Education"],
     "An econometric study measuring the long-run and short-run impact of human capital on Sudan's GDP growth from 1970 to 2009, finding education quality to be a critical determinant of economic performance.",
     "\u062f\u0631\u0627\u0633\u0629 \u0642\u064a\u0627\u0633\u064a\u0629 \u062a\u0642\u064a\u0633 \u0623\u062b\u0631 \u0631\u0623\u0633 \u0627\u0644\u0645\u0627\u0644 \u0627\u0644\u0628\u0634\u0631\u064a \u0639\u0644\u0649 \u0646\u0645\u0648 \u0627\u0644\u0646\u0627\u062a\u062c \u0627\u0644\u0633\u0648\u062f\u0627\u0646\u064a 1970-2009\u060c \u062a\u062e\u0644\u0635 \u0625\u0644\u0649 \u0623\u0646 \u062c\u0648\u062f\u0629 \u0627\u0644\u062a\u0639\u0644\u064a\u0645 \u0645\u062d\u062f\u062f \u062d\u0627\u0633\u0645 \u0644\u0644\u0623\u062f\u0627\u0621 \u0627\u0644\u0627\u0642\u062a\u0635\u0627\u062f\u064a."),
    ("Water_Diplomacy_And_the_Share_of_the_Nil.pdf",
     "water-diplomacy-nile-egypt-ethiopia-sudan.pdf",
     "Water Diplomacy: The Share of the Nile River between Egypt, Ethiopia and Sudan",
     "Unknown", ["Water & Nile", "Governance & Politics", "Regional & Geopolitics"],
     "An analysis of Nile water sharing geopolitics under the 1959 agreement, examining how the Grand Ethiopian Renaissance Dam is reshaping the diplomatic landscape and what this means for Sudan's irrigation ambitions.",
     "\u062a\u062d\u0644\u064a\u0644 \u0644\u062c\u064a\u0648\u0633\u064a\u0627\u0633\u064a\u0629 \u062a\u0642\u0627\u0633\u0645 \u0645\u064a\u0627\u0647 \u0627\u0644\u0646\u064a\u0644 \u0641\u064a \u0638\u0644 \u0627\u062a\u0641\u0627\u0642\u064a\u0629 1959\u060c \u064a\u062f\u0631\u0633 \u0643\u064a\u0641 \u064a\u0639\u064a\u062f \u0633\u062f \u0627\u0644\u0646\u0647\u0636\u0629 \u0631\u0633\u0645 \u0627\u0644\u0645\u0634\u0647\u062f \u0627\u0644\u062f\u0628\u0644\u0648\u0645\u0627\u0633\u064a \u0648\u062a\u062f\u0627\u0639\u064a\u0627\u062a\u0647 \u0639\u0644\u0649 \u0637\u0645\u0648\u062d\u0627\u062a \u0627\u0644\u0633\u0648\u062f\u0627\u0646 \u0627\u0644\u0631\u064a\u064a\u0629."),
    ("Overcoming_the_Past_War_and_Peace_in_Sud.pdf",
     "overcoming-past-war-peace-sudan-south-sudan.pdf",
     "Overcoming the Past: War and Peace in Sudan and South Sudan",
     "Unknown", ["Governance & Politics", "History", "Sudan History"],
     "A scholarly analysis of Sudan and South Sudan's post-conflict reconstruction challenges, arguing that peace-building failure after the CPA stemmed from incoherent sequencing of political and economic reforms.",
     "\u062a\u062d\u0644\u064a\u0644 \u0623\u0643\u0627\u062f\u064a\u0645\u064a \u0644\u062a\u062d\u062f\u064a\u0627\u062a \u0625\u0639\u0627\u062f\u0629 \u0627\u0644\u0625\u0639\u0645\u0627\u0631 \u0645\u0627 \u0628\u0639\u062f \u0627\u0644\u0635\u0631\u0627\u0639 \u0641\u064a \u0627\u0644\u0633\u0648\u062f\u0627\u0646 \u0648\u062c\u0646\u0648\u0628\u0647\u060c \u064a\u062c\u0627\u062f\u0644 \u0628\u0623\u0646 \u0625\u062e\u0641\u0627\u0642 \u0628\u0646\u0627\u0621 \u0627\u0644\u0633\u0644\u0627\u0645 \u0646\u0628\u0639 \u0645\u0646 \u062a\u0633\u0644\u0633\u0644 \u063a\u064a\u0631 \u0645\u062a\u0633\u0642 \u0644\u0644\u0625\u0635\u0644\u0627\u062d\u0627\u062a."),
    ("africa-and-the-four-powers-sudan-inaugurates-continental-rai.epub",
     "africa-four-powers-sudan-continental-railway.epub",
     "Africa and the Four Powers: Sudan Inaugurates the Continental Railway",
     "Hussein Askary", ["Infrastructure", "Regional & Geopolitics", "Economy & Development"],
     "An analysis of Sudan's strategic role in African continental railway integration, situating Sudan's network within the broader geopolitical competition between major powers and the AU infrastructure agenda.",
     "\u062a\u062d\u0644\u064a\u0644 \u0644\u0644\u062f\u0648\u0631 \u0627\u0644\u0627\u0633\u062a\u0631\u0627\u062a\u064a\u062c\u064a \u0644\u0644\u0633\u0648\u062f\u0627\u0646 \u0641\u064a \u062a\u0643\u0627\u0645\u0644 \u0634\u0628\u0643\u0629 \u0627\u0644\u0633\u0643\u0643 \u0627\u0644\u062d\u062f\u064a\u062f\u064a\u0629 \u0627\u0644\u0623\u0641\u0631\u064a\u0642\u064a\u0629 \u0627\u0644\u0642\u0627\u0631\u064a\u0629\u060c \u0636\u0645\u0646 \u0627\u0644\u062a\u0646\u0627\u0641\u0633 \u0627\u0644\u062c\u064a\u0648\u0633\u064a\u0627\u0633\u064a \u0628\u064a\u0646 \u0627\u0644\u0642\u0648\u0649 \u0627\u0644\u0643\u0628\u0631\u0649."),
    ("african-archaeological-review-the-meroitic-kingdom.epub",
     "african-archaeological-review-meroitic-kingdom.epub",
     "African Archaeological Review: The Meroitic Kingdom",
     "Unknown", ["Ancient Sudan", "History", "Archaeology & Heritage"],
     "A scholarly archaeological review of the Meroitic Kingdom's material culture, examining excavation findings, settlement patterns, trade networks, and the ongoing reassessment of Meroe's economic sophistication.",
     "\u0645\u0631\u0627\u062c\u0639\u0629 \u0623\u062b\u0631\u064a\u0629 \u0639\u0644\u0645\u064a\u0629 \u0644\u0644\u062b\u0642\u0627\u0641\u0629 \u0627\u0644\u0645\u0627\u062f\u064a\u0629 \u0644\u0645\u0645\u0644\u0643\u0629 \u0645\u0631\u0648\u064a\u060c \u062a\u062f\u0631\u0633 \u0646\u062a\u0627\u0626\u062c \u0627\u0644\u062a\u0646\u0642\u064a\u0628\u0627\u062a \u0648\u0623\u0646\u0645\u0627\u0637 \u0627\u0644\u0627\u0633\u062a\u064a\u0637\u0627\u0646 \u0648\u0634\u0628\u0643\u0627\u062a \u0627\u0644\u062a\u062c\u0627\u0631\u0629."),
    ("africa-in-antiquity-the-arts-of-ancient-nubia-and-the-sudan.epub",
     "africa-antiquity-arts-ancient-nubia-sudan.epub",
     "Africa in Antiquity: The Arts of Ancient Nubia and the Sudan",
     "Unknown", ["Ancient Sudan", "History", "Arts & Culture", "Nubian History"],
     "A major survey of the visual arts of ancient Nubia and Sudan from the Kerma period through the Meroitic Kingdom, documenting the sophisticated artistic traditions that developed independently of Egyptian influence.",
     "\u0645\u0633\u062d \u0634\u0627\u0645\u0644 \u0644\u0644\u0641\u0646\u0648\u0646 \u0627\u0644\u0628\u0635\u0631\u064a\u0629 \u0641\u064a \u0627\u0644\u0646\u0648\u0628\u0629 \u0648\u0627\u0644\u0633\u0648\u062f\u0627\u0646 \u0627\u0644\u0642\u062f\u064a\u0645\u064a\u0646 \u0645\u0646 \u062d\u0642\u0628\u0629 \u0643\u0631\u0645\u0629 \u062d\u062a\u0649 \u0627\u0644\u0645\u0645\u0644\u0643\u0629 \u0627\u0644\u0645\u0631\u0648\u064a\u0629\u060c \u064a\u0648\u062b\u0651\u0642 \u0627\u0644\u062a\u0642\u0627\u0644\u064a\u062f \u0627\u0644\u0641\u0646\u064a\u0629 \u0627\u0644\u0631\u0627\u0642\u064a\u0629 \u0627\u0644\u062a\u064a \u062a\u0637\u0648\u0631\u062a \u0628\u0627\u0633\u062a\u0642\u0644\u0627\u0644\u064a\u0629 \u0639\u0646 \u0627\u0644\u062a\u0623\u062b\u064a\u0631 \u0627\u0644\u0645\u0635\u0631\u064a."),
]

script_dir = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(script_dir, "data", "library.json")
csv_path = os.path.join(script_dir, "library_inventory.csv")

with open(json_path, encoding="utf-8") as f:
    lib = json.load(f)
with open(csv_path, encoding="utf-8") as f:
    existing_csv = f.read()

os.makedirs(SUDAN_PDFS, exist_ok=True)
print("Uploading " + str(len(FILES)) + " files...\n")
success = 0
new_books = []
new_csv_rows = []

for item in FILES:
    filename, key, title, author, tags, desc, desc_ar = item
    local_path = os.path.join(DOWNLOADS, filename)
    if not os.path.exists(local_path):
        print("  MISSING: " + filename)
        continue
    size_mb = os.path.getsize(local_path) / (1024 * 1024)
    ext = filename.split(".")[-1].lower()
    content_type = "application/epub+zip" if ext == "epub" else "application/pdf"
    print("  " + key + " (" + str(round(size_mb, 1)) + " MB)...", end=" ", flush=True)
    try:
        s3.upload_file(local_path, R2_BUCKET_NAME, key, ExtraArgs={"ContentType": content_type})
        r2_url = BASE_URL + "/" + key
        print("OK")
        success += 1
        dest = os.path.join(SUDAN_PDFS, filename)
        if not os.path.exists(dest):
            shutil.copy2(local_path, dest)
        new_books.append({"title": title, "title_ar": title, "author": author,
            "tags": tags, "desc": desc, "desc_ar": desc_ar, "source": r2_url})
        if key not in existing_csv:
            new_csv_rows.append(title + "," + author + "," + key + "," + r2_url)
    except Exception as e:
        print("FAILED: " + str(e))

existing_sources = {b.get("source", "") for b in lib["books"]}
added = 0
for book in new_books:
    if book["source"] not in existing_sources:
        lib["books"].append(book)
        added += 1

with open(json_path, "w", encoding="utf-8") as f:
    json.dump(lib, f, ensure_ascii=False, indent=2)

if new_csv_rows:
    with open(csv_path, "a", encoding="utf-8", newline="") as f:
        for row in new_csv_rows:
            f.write(row + "\n")

print("\n" + str(success) + "/" + str(len(FILES)) + " uploaded.")
print(str(added) + " new entries added to library.json.")
print(str(len(new_csv_rows)) + " rows added to library_inventory.csv.")
print("\nRun: git add data/library.json library_inventory.csv upload_new_batch.py")
print("     git commit -m 'Add 7 new library entries: agriculture, human capital, Nile diplomacy, war/peace, railway, Meroitic arts'")
print("     git pull --rebase && git push")

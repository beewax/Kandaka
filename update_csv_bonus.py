import csv, os

script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, "library_inventory.csv")

BASE_URL = "https://pub-0c3bb637d5f54b239fe4a4ef9b08bfe3.r2.dev"

new_rows = [
    ("The Candaces of Meroe", "World History Encyclopedia",
     "candaces-of-meroe-world-history-encyclopedia.pdf",
     BASE_URL + "/candaces-of-meroe-world-history-encyclopedia.pdf"),
    ("The Queen Mother in the Kingdom of Kush", "Unknown",
     "queen-mother-kingdom-of-kush.pdf",
     BASE_URL + "/queen-mother-kingdom-of-kush.pdf"),
    ("Sudan Archaeological Research Society Newsletter 21", "Krzysztof Grzymski",
     "sars-sn21-grzymski.pdf",
     BASE_URL + "/sars-sn21-grzymski.pdf"),
]

# Check existing filenames to avoid duplicates
with open(csv_path, encoding="utf-8") as f:
    existing = f.read()

added = 0
with open(csv_path, "a", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    for row in new_rows:
        if row[2] not in existing:
            writer.writerow(row)
            added += 1
            print("  Added: " + row[0])
        else:
            print("  SKIP (already exists): " + row[0])

print("\nDone. Added " + str(added) + " rows to library_inventory.csv.")

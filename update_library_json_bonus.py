import json, os

script_dir = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(script_dir, "data", "library.json")

with open(json_path, encoding="utf-8") as f:
    lib = json.load(f)

BASE_URL = "https://pub-0c3bb637d5f54b239fe4a4ef9b08bfe3.r2.dev"

new_books = [
    {
        "title": "The Candaces of Meroe",
        "title_ar": "\u0643\u0646\u062f\u0627\u0643\u0627\u062a \u0645\u0631\u0648\u064a",
        "author": "World History Encyclopedia",
        "tags": ["History", "Ancient Sudan", "Nubian History", "Women & Leadership"],
        "desc": "A World History Encyclopedia survey of the Candaces — the ruling queen mothers of the Meroitic Kingdom — covering their political authority, military campaigns, and the institutional role of female rulership in ancient Sudan.",
        "desc_ar": "\u0645\u0633\u062d \u0645\u0648\u0633\u0648\u0639\u0629 \u0627\u0644\u062a\u0627\u0631\u064a\u062e \u0627\u0644\u0639\u0627\u0644\u0645\u064a \u062d\u0648\u0644 \u0627\u0644\u0643\u0646\u062f\u0627\u0643\u0627\u062a \u2014 \u0623\u0645\u0647\u0627\u062a \u0627\u0644\u0645\u0644\u0648\u0643 \u0627\u0644\u062d\u0627\u0643\u0645\u0627\u062a \u0641\u064a \u0645\u0645\u0644\u0643\u0629 \u0645\u0631\u0648\u064a \u2014 \u064a\u062a\u0646\u0627\u0648\u0644 \u0633\u0644\u0637\u062a\u0647\u0646 \u0627\u0644\u0633\u064a\u0627\u0633\u064a\u0629 \u0648\u062d\u0645\u0644\u0627\u062a\u0647\u0646 \u0627\u0644\u0639\u0633\u0643\u0631\u064a\u0629 \u0648\u062f\u0648\u0631 \u0627\u0644\u062d\u0643\u0645 \u0627\u0644\u0623\u0646\u062b\u0648\u064a \u0641\u064a \u0627\u0644\u0633\u0648\u062f\u0627\u0646 \u0627\u0644\u0642\u062f\u064a\u0645.",
        "source": BASE_URL + "/candaces-of-meroe-world-history-encyclopedia.pdf"
    },
    {
        "title": "The Queen Mother in the Kingdom of Kush",
        "title_ar": "\u0623\u0645 \u0627\u0644\u0645\u0644\u0643 \u0641\u064a \u0645\u0645\u0644\u0643\u0629 \u0643\u0648\u0634",
        "author": "Unknown",
        "tags": ["History", "Ancient Sudan", "Nubian History", "Women & Leadership"],
        "desc": "A scholarly study of the Queen Mother institution in the Kingdom of Kush, examining how this formal role shaped succession, legitimacy, and governance in the Meroitic state — with direct relevance to understanding why Sudan produced more ruling queens than any other civilization in recorded history.",
        "desc_ar": "\u062f\u0631\u0627\u0633\u0629 \u0623\u0643\u0627\u062f\u064a\u0645\u064a\u0629 \u0644\u0645\u0624\u0633\u0633\u0629 \u0623\u0645 \u0627\u0644\u0645\u0644\u0643 \u0641\u064a \u0645\u0645\u0644\u0643\u0629 \u0643\u0648\u0634\u060c \u062a\u0641\u062d\u0635 \u0643\u064a\u0641 \u0634\u0643\u0651\u0644 \u0647\u0630\u0627 \u0627\u0644\u062f\u0648\u0631 \u0627\u0644\u0631\u0633\u0645\u064a \u0645\u0633\u0627\u0631 \u0627\u0644\u062e\u0644\u0627\u0641\u0629 \u0648\u0627\u0644\u0634\u0631\u0639\u064a\u0629 \u0648\u0627\u0644\u062d\u0648\u0643\u0645\u0629 \u0641\u064a \u0627\u0644\u062f\u0648\u0644\u0629 \u0627\u0644\u0645\u0631\u0648\u064a\u0629.",
        "source": BASE_URL + "/queen-mother-kingdom-of-kush.pdf"
    },
    {
        "title": "Sudan Archaeological Research Society Newsletter 21 (Grzymski)",
        "title_ar": "\u0646\u0634\u0631\u0629 \u062c\u0645\u0639\u064a\u0629 \u0627\u0644\u0628\u062d\u0648\u062b \u0627\u0644\u0623\u062b\u0631\u064a\u0629 \u0627\u0644\u0633\u0648\u062f\u0627\u0646\u064a\u0629 - \u0627\u0644\u0639\u062f\u062f 21",
        "author": "Krzysztof Grzymski",
        "tags": ["History", "Ancient Sudan", "Archaeology", "Nubian History"],
        "desc": "An issue of the Sudan Archaeological Research Society newsletter featuring Krzysztof Grzymski's fieldwork reports and analysis of Meroitic and Kushite archaeological sites, providing primary source material on ongoing excavations in Sudan.",
        "desc_ar": "\u0639\u062f\u062f \u0645\u0646 \u0646\u0634\u0631\u0629 \u062c\u0645\u0639\u064a\u0629 \u0627\u0644\u0628\u062d\u0648\u062b \u0627\u0644\u0623\u062b\u0631\u064a\u0629 \u0627\u0644\u0633\u0648\u062f\u0627\u0646\u064a\u0629 \u064a\u062a\u0636\u0645\u0651\u0646 \u062a\u0642\u0627\u0631\u064a\u0631 \u0643\u0631\u0632\u064a\u0634\u062a\u0648\u0641 \u063a\u0631\u0632\u064a\u0645\u0633\u0643\u064a \u0627\u0644\u0645\u064a\u062f\u0627\u0646\u064a\u0629 \u0648\u062a\u062d\u0644\u064a\u0644\u0627\u062a\u0647 \u0644\u0644\u0645\u0648\u0627\u0642\u0639 \u0627\u0644\u0623\u062b\u0631\u064a\u0629 \u0627\u0644\u0645\u0631\u0648\u064a\u0629 \u0648\u0627\u0644\u0643\u0648\u0634\u064a\u0629.",
        "source": BASE_URL + "/sars-sn21-grzymski.pdf"
    },
]

existing_sources = {b.get("source", "") for b in lib["books"]}
added = 0
for book in new_books:
    if book["source"] not in existing_sources:
        lib["books"].append(book)
        added += 1
        print("  Added: " + book["title"])
    else:
        print("  SKIP (already exists): " + book["title"])

with open(json_path, "w", encoding="utf-8") as f:
    json.dump(lib, f, ensure_ascii=False, indent=2)

print("\nDone. Added " + str(added) + " books. Total: " + str(len(lib["books"])) + " books.")

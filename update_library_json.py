import json, os

# Run from C:\Users\Abdulla\Kandaka:  python update_library_json.py

script_dir = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(script_dir, "data", "library.json")

with open(json_path, encoding="utf-8") as f:
    lib = json.load(f)

BASE_URL = "https://pub-0c3bb637d5f54b239fe4a4ef9b08bfe3.r2.dev"

new_books = [
    {
        "title": "Nubian Queens",
        "title_ar": "\u0645\u0644\u0643\u0627\u062a \u0627\u0644\u0646\u0648\u0628\u0629",
        "author": "Unknown",
        "tags": ["History", "Ancient Sudan", "Nubian History"],
        "desc": "An overview of the powerful queens and queen mothers of ancient Nubia, covering their political roles, military leadership, and cultural legacy in the Kingdom of Kush and the Meroitic civilization.",
        "desc_ar": "\u0644\u0645\u062d\u0629 \u0634\u0627\u0645\u0644\u0629 \u0639\u0646 \u0645\u0644\u0643\u0627\u062a \u0648\u0623\u0645\u0647\u0627\u062a \u0645\u0644\u0648\u0643 \u0627\u0644\u0646\u0648\u0628\u0629 \u0627\u0644\u0642\u062f\u064a\u0645\u0629\u060c \u062a\u062a\u0646\u0627\u0648\u0644 \u0623\u062f\u0648\u0627\u0631\u0647\u0646 \u0627\u0644\u0633\u064a\u0627\u0633\u064a\u0629 \u0648\u0642\u064a\u0627\u062f\u062a\u0647\u0646 \u0627\u0644\u0639\u0633\u0643\u0631\u064a\u0629 \u0648\u0625\u0631\u062b\u0647\u0646 \u0627\u0644\u062d\u0636\u0627\u0631\u064a \u0641\u064a \u0645\u0645\u0644\u0643\u0629 \u0643\u0648\u0634 \u0648\u0627\u0644\u062d\u0636\u0627\u0631\u0629 \u0627\u0644\u0645\u0631\u0648\u064a\u0629.",
        "source": BASE_URL + "/nubian-queens.pdf"
    },
    {
        "title": "The Kandake: A Missing History",
        "title_ar": "\u0627\u0644\u0643\u0646\u062f\u0627\u0643\u0629: \u062a\u0627\u0631\u064a\u062e \u0645\u0641\u0642\u0648\u062f",
        "author": "Unknown",
        "tags": ["History", "Ancient Sudan", "Nubian History", "Women & Leadership"],
        "desc": "A focused study on the institution of the Kandake - the ruling queens of Meroe - examining why this remarkable tradition of female sovereignty has been systematically overlooked in mainstream historical narratives.",
        "desc_ar": "\u062f\u0631\u0627\u0633\u0629 \u0645\u0639\u0645\u0651\u0642\u0629 \u0641\u064a \u0645\u0624\u0633\u0633\u0629 \u0627\u0644\u0643\u0646\u062f\u0627\u0643\u0629 \u2014 \u0645\u0644\u0643\u0627\u062a \u0645\u0631\u0648\u064a \u0627\u0644\u062d\u0627\u0643\u0645\u0627\u062a \u2014 \u062a\u062a\u0633\u0627\u0621\u0644 \u0644\u0645\u0627\u0630\u0627 \u0623\u064f\u0647\u0645\u0644\u062a \u0647\u0630\u0647 \u0627\u0644\u062a\u0642\u0644\u064a\u062f \u0627\u0644\u0627\u0633\u062a\u062b\u0646\u0627\u0626\u064a \u0644\u0644\u0633\u064a\u0627\u062f\u0629 \u0627\u0644\u0623\u0646\u062b\u0648\u064a\u0629 \u0641\u064a \u0627\u0644\u0631\u0648\u0627\u064a\u0627\u062a \u0627\u0644\u062a\u0627\u0631\u064a\u062e\u064a\u0629 \u0627\u0644\u0633\u0627\u0626\u062f\u0629.",
        "source": BASE_URL + "/the-kandake-a-missing-history.pdf"
    },
    {
        "title": "Kandake - Wikipedia",
        "title_ar": "\u0643\u0646\u062f\u0627\u0643\u0629 \u2013 \u0648\u064a\u0643\u064a\u0628\u064a\u062f\u064a\u0627",
        "author": "Wikipedia Contributors",
        "tags": ["History", "Ancient Sudan", "Reference"],
        "desc": "A comprehensive Wikipedia reference article on the Kandake title, tracing its linguistic origins, historical context, notable queens including Amanirenas and Amanishakheto, and its enduring cultural significance.",
        "desc_ar": "\u0645\u0642\u0627\u0644\u0629 \u0645\u0631\u062c\u0639\u064a\u0629 \u0634\u0627\u0645\u0644\u0629 \u0645\u0646 \u0648\u064a\u0643\u064a\u0628\u064a\u062f\u064a\u0627 \u062d\u0648\u0644 \u0644\u0642\u0628 \u0627\u0644\u0643\u0646\u062f\u0627\u0643\u0629\u060c \u062a\u062a\u062a\u0628\u0639 \u0623\u0635\u0648\u0644\u0647 \u0627\u0644\u0644\u063a\u0648\u064a\u0629 \u0648\u0633\u064a\u0627\u0642\u0647 \u0627\u0644\u062a\u0627\u0631\u064a\u062e\u064a \u0648\u0623\u0628\u0631\u0632 \u0627\u0644\u0645\u0644\u0643\u0627\u062a \u0645\u0646 \u0628\u064a\u0646\u0647\u0646 \u0623\u0645\u0627\u0646\u064a\u0631\u064a\u0646\u0627\u0633 \u0648\u0623\u0645\u0627\u0646\u064a\u0634\u0627\u062e\u064a\u062a\u0648\u060c \u0648\u0623\u0647\u0645\u064a\u062a\u0647 \u0627\u0644\u062b\u0642\u0627\u0641\u064a\u0629 \u0627\u0644\u0645\u0633\u062a\u0645\u0631\u0629.",
        "source": BASE_URL + "/kandake-wikipedia.pdf"
    },
    {
        "title": "The Nile Bride Myth Revisioned in Nubian Literature",
        "title_ar": "\u0623\u0633\u0637\u0648\u0631\u0629 \u0639\u0631\u0648\u0633 \u0627\u0644\u0646\u064a\u0644 \u0641\u064a \u0627\u0644\u0623\u062f\u0628 \u0627\u0644\u0646\u0648\u0628\u064a: \u0625\u0639\u0627\u062f\u0629 \u0642\u0631\u0627\u0621\u0629",
        "author": "Unknown",
        "tags": ["History", "Culture", "Nubian History", "Literature"],
        "desc": "A scholarly examination of the Nile bride sacrifice myth as it appears and is reinterpreted in modern Nubian literature, exploring how Nubian writers reclaim and subvert colonial and ancient narratives about gender and sacrifice.",
        "desc_ar": "\u062f\u0631\u0627\u0633\u0629 \u0623\u0643\u0627\u062f\u064a\u0645\u064a\u0629 \u0644\u0623\u0633\u0637\u0648\u0631\u0629 \u0627\u0644\u062a\u0636\u062d\u064a\u0629 \u0628\u0639\u0631\u0648\u0633 \u0627\u0644\u0646\u064a\u0644 \u0643\u0645\u0627 \u062a\u0638\u0647\u0631 \u0648\u062a\u064f\u0639\u0627\u062f \u0635\u064a\u0627\u063a\u062a\u0647\u0627 \u0641\u064a \u0627\u0644\u0623\u062f\u0628 \u0627\u0644\u0646\u0648\u0628\u064a \u0627\u0644\u062d\u062f\u064a\u062b.",
        "source": BASE_URL + "/nile-bride-myth-nubian-literature.pdf"
    },
    {
        "title": "Smarthistory: Pylon of the Nubian Lion Temple at Naga",
        "title_ar": "\u0633\u0645\u0627\u0631\u062a \u0647\u064a\u0633\u062a\u0648\u0631\u064a: \u0628\u0648\u0627\u0628\u0629 \u0645\u0639\u0628\u062f \u0627\u0644\u0623\u0633\u062f \u0627\u0644\u0646\u0648\u0628\u064a \u0641\u064a \u0646\u0642\u0627",
        "author": "Smarthistory",
        "tags": ["History", "Ancient Sudan", "Art & Architecture", "Nubian History"],
        "desc": "An art historical analysis of the pylon of the Lion Temple at Naga, examining its Meroitic iconography - including the distinctive blending of Egyptian and sub-Saharan African artistic traditions - and its significance as a monument of Kush's independent cultural identity.",
        "desc_ar": "\u062a\u062d\u0644\u064a\u0644 \u062a\u0627\u0631\u064a\u062e\u064a \u0641\u0646\u064a \u0644\u0628\u0648\u0627\u0628\u0629 \u0645\u0639\u0628\u062f \u0627\u0644\u0623\u0633\u062f \u0641\u064a \u0646\u0642\u0627\u060c \u064a\u062f\u0631\u0633 \u0623\u064a\u0642\u0648\u0646\u0648\u063a\u0631\u0627\u0641\u064a\u062a\u0647\u0627 \u0627\u0644\u0645\u0631\u0648\u064a\u0629 \u0648\u0623\u0647\u0645\u064a\u062a\u0647\u0627 \u0628\u0648\u0635\u0641\u0647\u0627 \u0634\u0627\u0647\u062f\u0627\u064b \u0639\u0644\u0649 \u0627\u0644\u0647\u0648\u064a\u0629 \u0627\u0644\u062b\u0642\u0627\u0641\u064a\u0629 \u0627\u0644\u0645\u0633\u062a\u0642\u0644\u0629 \u0644\u0645\u0645\u0644\u0643\u0629 \u0643\u0648\u0634.",
        "source": BASE_URL + "/smarthistory-nubian-lion-temple-naga.pdf"
    },
    {
        "title": "History of Sudan",
        "title_ar": "\u062a\u0627\u0631\u064a\u062e \u0627\u0644\u0633\u0648\u062f\u0627\u0646",
        "author": "Naum Shoucair; E. Abu Salim",
        "tags": ["History", "Sudan History", "Reference"],
        "desc": "A landmark historical survey of Sudan by Naum Shoucair, one of the earliest systematic histories of the country. Edited by E. Abu Salim, the work spans ancient kingdoms through the Turkiyya and Mahdiyya periods, and remains an essential primary reference for Sudanese historiography.",
        "desc_ar": "\u0645\u0633\u062d \u062a\u0627\u0631\u064a\u062e\u064a \u0628\u0627\u0631\u0632 \u0644\u0644\u0633\u0648\u062f\u0627\u0646 \u0645\u0646 \u062a\u0623\u0644\u064a\u0641 \u0646\u0639\u0648\u0645 \u0634\u0642\u064a\u0631\u060c \u0628\u062a\u062d\u0642\u064a\u0642 \u0625\u0628\u0631\u0627\u0647\u064a\u0645 \u0623\u0628\u0648 \u0633\u0644\u064a\u0645\u060c \u064a\u062a\u0646\u0627\u0648\u0644 \u0627\u0644\u0643\u062a\u0627\u0628 \u0627\u0644\u0645\u0645\u0627\u0644\u0643 \u0627\u0644\u0642\u062f\u064a\u0645\u0629 \u062d\u062a\u0649 \u0627\u0644\u062d\u0642\u0628\u0629 \u0627\u0644\u062a\u0631\u0643\u064a\u0629 \u0648\u0627\u0644\u0645\u0647\u062f\u064a\u0629.",
        "source": BASE_URL + "/history-of-sudan-naum-shoucair.pdf"
    },
    {
        "title": "Amanirenas (Novel)",
        "title_ar": "\u0623\u0645\u0627\u0646\u064a\u0631\u064a\u0646\u0627\u0633 (\u0631\u0648\u0627\u064a\u0629)",
        "author": "Unknown",
        "tags": ["History", "Ancient Sudan", "Fiction", "Nubian History"],
        "desc": "A historical fiction work centered on Amanirenas, the one-eyed warrior queen of Kush who led her forces against the Roman Empire and negotiated a treaty with Augustus that won favorable terms for her kingdom.",
        "desc_ar": "\u0639\u0645\u0644 \u0631\u0648\u0627\u0626\u064a \u062a\u0627\u0631\u064a\u062e\u064a \u064a\u062a\u0645\u062d\u0648\u0631 \u062d\u0648\u0644 \u0623\u0645\u0627\u0646\u064a\u0631\u064a\u0646\u0627\u0633\u060c \u0627\u0644\u0645\u0644\u0643\u0629 \u0627\u0644\u0645\u062d\u0627\u0631\u0628\u0629 \u0627\u0644\u0643\u0646\u062f\u0648\u0628\u0629 \u0627\u0644\u062a\u064a \u0642\u0627\u062f\u062a \u0642\u0648\u0627\u062a \u0645\u0645\u0644\u0643\u0629 \u0643\u0648\u0634 \u0641\u064a \u0645\u0648\u0627\u062c\u0647\u0629 \u0627\u0644\u0625\u0645\u0628\u0631\u0627\u0637\u0648\u0631\u064a\u0629 \u0627\u0644\u0631\u0648\u0645\u0627\u0646\u064a\u0629.",
        "source": BASE_URL + "/amanirenas-en.epub"
    },
]

# Idempotent: skip if already present
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

import json, os, csv

script_dir = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(script_dir, "data", "library.json")
csv_path = os.path.join(script_dir, "library_inventory.csv")

with open(json_path, encoding="utf-8") as f:
    lib = json.load(f)

BASE_URL = "https://pub-0c3bb637d5f54b239fe4a4ef9b08bfe3.r2.dev"
ACADEMIA = "https://www.academia.edu"

new_books = [
    {
        "title": "Industrial Location Analysis of Sudan",
        "title_ar": "\u062a\u062d\u0644\u064a\u0644 \u0627\u0644\u0645\u0648\u0627\u0642\u0639 \u0627\u0644\u0635\u0646\u0627\u0639\u064a\u0629 \u0641\u064a \u0627\u0644\u0633\u0648\u062f\u0627\u0646",
        "author": "Khalid Idris",
        "tags": ["Economy & Development", "Industrialization", "History"],
        "desc": "A landmark study of Sudan's industrial geography from the colonial period through 1980, arguing that deliberate non-industrialization policies under British rule locked manufacturing into Khartoum and created regional inequalities that persisted after independence. Develops a Prime Base theory of industrial location specific to developing countries.",
        "desc_ar": "\u062f\u0631\u0627\u0633\u0629 \u0645\u0631\u062c\u0639\u064a\u0629 \u0641\u064a \u062c\u063a\u0631\u0627\u0641\u064a\u0627 \u0627\u0644\u0635\u0646\u0627\u0639\u0629 \u0627\u0644\u0633\u0648\u062f\u0627\u0646\u064a\u0629 \u0645\u0646 \u0627\u0644\u062d\u0642\u0628\u0629 \u0627\u0644\u0627\u0633\u062a\u0639\u0645\u0627\u0631\u064a\u0629 \u062d\u062a\u0649 1980\u060c \u062a\u062c\u0627\u062f\u0644 \u0623\u0646 \u0633\u064a\u0627\u0633\u0627\u062a \u0639\u062f\u0645 \u0627\u0644\u062a\u0635\u0646\u064a\u0639 \u0627\u0644\u0645\u062a\u0639\u0645\u062f\u0629 \u062a\u062d\u062a \u0627\u0644\u062d\u0643\u0645 \u0627\u0644\u0628\u0631\u064a\u0637\u0627\u0646\u064a \u062d\u0635\u0631\u062a \u0627\u0644\u062a\u0635\u0646\u064a\u0639 \u0641\u064a \u0627\u0644\u062e\u0631\u0637\u0648\u0645 \u0648\u0623\u0641\u0631\u0632\u062a \u062a\u0641\u0627\u0648\u062a\u0627\u062a \u0625\u0642\u0644\u064a\u0645\u064a\u0629 \u0627\u0633\u062a\u0645\u0631\u062a \u0628\u0639\u062f \u0627\u0644\u0627\u0633\u062a\u0642\u0644\u0627\u0644.",
        "source": BASE_URL + "/industrial-location-analysis-sudan.pdf"
    },
    {
        "title": "The Construction Industry of Sudan: Potentials and Challenges",
        "title_ar": "\u0635\u0646\u0627\u0639\u0629 \u0627\u0644\u0628\u0646\u0627\u0621 \u0648\u0627\u0644\u062a\u0634\u064a\u064a\u062f \u0641\u064a \u0627\u0644\u0633\u0648\u062f\u0627\u0646: \u0627\u0644\u0625\u0645\u0643\u0627\u0646\u0627\u062a \u0648\u0627\u0644\u062a\u062d\u062f\u064a\u0627\u062a",
        "author": "Unknown",
        "tags": ["Economy & Development", "Infrastructure", "Industrialization"],
        "desc": "A sector analysis of Sudan's construction industry examining its economic multiplier effects, the socio-political constraints limiting its growth, and recommendations for establishing a national Construction Industry Development Board to coordinate policy and investment.",
        "desc_ar": "\u062a\u062d\u0644\u064a\u0644 \u0642\u0637\u0627\u0639\u064a \u0644\u0635\u0646\u0627\u0639\u0629 \u0627\u0644\u0628\u0646\u0627\u0621 \u0648\u0627\u0644\u062a\u0634\u064a\u064a\u062f \u0641\u064a \u0627\u0644\u0633\u0648\u062f\u0627\u0646\u060c \u064a\u062f\u0631\u0633 \u062a\u0623\u062b\u064a\u0631\u0627\u062a\u0647\u0627 \u0627\u0644\u062a\u0636\u0627\u0639\u0641\u064a\u0629 \u0639\u0644\u0649 \u0627\u0644\u0627\u0642\u062a\u0635\u0627\u062f\u060c \u0648\u0627\u0644\u0642\u064a\u0648\u062f \u0627\u0644\u0633\u064a\u0627\u0633\u064a\u0629 \u0648\u0627\u0644\u0627\u062c\u062a\u0645\u0627\u0639\u064a\u0629 \u0627\u0644\u062a\u064a \u062a\u062d\u062f \u0645\u0646 \u0646\u0645\u0648\u0647\u0627.",
        "source": BASE_URL + "/construction-industry-sudan-potentials-challenges.pdf"
    },
    {
        "title": "Development Economics in Sudan: The Ten Year Economic and Social Plan",
        "title_ar": "\u0627\u0642\u062a\u0635\u0627\u062f\u064a\u0627\u062a \u0627\u0644\u062a\u0646\u0645\u064a\u0629 \u0641\u064a \u0627\u0644\u0633\u0648\u062f\u0627\u0646: \u062e\u0637\u0629 \u0627\u0644\u0639\u0634\u0631 \u0633\u0646\u0648\u0627\u062a",
        "author": "Iman Sharif",
        "tags": ["Economy & Development", "Governance & Politics", "History"],
        "desc": "An analysis of Sudan's first national development plan — the Ten Year Economic and Social Plan 1961–1970 — examining its ambitious targets, the obstacles that caused its abandonment by 1965, and the economic growth achieved despite its failure. A foundational text for understanding Sudan's post-independence development trajectory.",
        "desc_ar": "\u062a\u062d\u0644\u064a\u0644 \u0623\u0648\u0644 \u062e\u0637\u0629 \u062a\u0646\u0645\u064a\u0629 \u0648\u0637\u0646\u064a\u0629 \u0633\u0648\u062f\u0627\u0646\u064a\u0629 \u2014 \u062e\u0637\u0629 \u0627\u0644\u0639\u0634\u0631 \u0633\u0646\u0648\u0627\u062a \u0627\u0644\u0627\u0642\u062a\u0635\u0627\u062f\u064a\u0629 \u0648\u0627\u0644\u0627\u062c\u062a\u0645\u0627\u0639\u064a\u0629 1961\u20131970 \u2014 \u062f\u0631\u0627\u0633\u0629 \u0623\u0647\u062f\u0627\u0641\u0647\u0627 \u0648\u0627\u0644\u0639\u0642\u0628\u0627\u062a \u0627\u0644\u062a\u064a \u0623\u062f\u062a \u0625\u0644\u0649 \u0627\u0644\u062a\u062e\u0644\u064a \u0639\u0646\u0647\u0627 \u0639\u0627\u0645 1965.",
        "source": BASE_URL + "/development-economics-sudan-ten-year-plan.pdf"
    },
    {
        "title": "Cotton Export Performance and Constraints in Sudan",
        "title_ar": "\u0623\u062f\u0627\u0621 \u0635\u0627\u062f\u0631\u0627\u062a \u0627\u0644\u0642\u0637\u0646 \u0648\u0642\u064a\u0648\u062f\u0647\u0627 \u0641\u064a \u0627\u0644\u0633\u0648\u062f\u0627\u0646",
        "author": "Imad Yousif",
        "tags": ["Agriculture", "Economy & Development", "Trade"],
        "desc": "An econometric study of Sudan's cotton export performance showing that full liberalization of world cotton markets would increase Sudan's export earnings, and that exchange rate instability and yield gaps — not world prices — are the binding constraints on Sudan's cotton competitiveness.",
        "desc_ar": "\u062f\u0631\u0627\u0633\u0629 \u0642\u064a\u0627\u0633\u064a\u0629 \u0644\u0623\u062f\u0627\u0621 \u0635\u0627\u062f\u0631\u0627\u062a \u0627\u0644\u0642\u0637\u0646 \u0627\u0644\u0633\u0648\u062f\u0627\u0646\u064a\u060c \u062a\u062e\u0644\u0635 \u0625\u0644\u0649 \u0623\u0646 \u0627\u0633\u062a\u0642\u0631\u0627\u0631 \u0633\u0639\u0631 \u0627\u0644\u0635\u0631\u0641 \u0648\u0641\u062c\u0648\u0629 \u0627\u0644\u0625\u0646\u062a\u0627\u062c\u064a\u0629 \u2014 \u0644\u0627 \u0623\u0633\u0639\u0627\u0631 \u0627\u0644\u0633\u0648\u0642 \u0627\u0644\u0639\u0627\u0644\u0645\u064a\u0629 \u2014 \u0647\u064a \u0627\u0644\u0642\u064a\u0648\u062f \u0627\u0644\u062d\u0642\u064a\u0642\u064a\u0629 \u0639\u0644\u0649 \u0627\u0644\u062a\u0646\u0627\u0641\u0633\u064a\u0629 \u0627\u0644\u0642\u0637\u0646\u064a\u0629 \u0627\u0644\u0633\u0648\u062f\u0627\u0646\u064a\u0629.",
        "source": BASE_URL + "/cotton-export-performance-constraints-sudan.pdf"
    },
    {
        "title": "Spinning in Meroitic Sudan: Textile Implements from Abu Geili",
        "title_ar": "\u0627\u0644\u063a\u0632\u0644 \u0641\u064a \u0627\u0644\u0633\u0648\u062f\u0627\u0646 \u0627\u0644\u0645\u0631\u0648\u064a: \u0623\u062f\u0648\u0627\u062a \u0627\u0644\u0646\u0633\u064a\u062c \u0645\u0646 \u0623\u0628\u0648 \u062c\u064a\u0644\u064a",
        "author": "Unknown",
        "tags": ["Ancient Sudan", "History", "Economy & Development"],
        "desc": "An archaeological study of spinning tools from Abu Geili revealing the scale of textile production in Meroitic Sudan, tracing the economic shift from cotton to wool and illuminating the role of yarn manufacture in Meroe's craft economy and social organization.",
        "desc_ar": "\u062f\u0631\u0627\u0633\u0629 \u0623\u062b\u0631\u064a\u0629 \u0644\u0623\u062f\u0648\u0627\u062a \u0627\u0644\u063a\u0632\u0644 \u0645\u0646 \u0645\u0648\u0642\u0639 \u0623\u0628\u0648 \u062c\u064a\u0644\u064a\u060c \u062a\u0643\u0634\u0641 \u0639\u0646 \u062d\u062c\u0645 \u0625\u0646\u062a\u0627\u062c \u0627\u0644\u0645\u0646\u0633\u0648\u062c\u0627\u062a \u0641\u064a \u0627\u0644\u0633\u0648\u062f\u0627\u0646 \u0627\u0644\u0645\u0631\u0648\u064a\u060c \u0648\u062a\u062a\u062a\u0628\u0639 \u0627\u0644\u062a\u062d\u0648\u0644 \u0627\u0644\u0627\u0642\u062a\u0635\u0627\u062f\u064a \u0645\u0646 \u0627\u0644\u0642\u0637\u0646 \u0625\u0644\u0649 \u0627\u0644\u0635\u0648\u0641.",
        "source": BASE_URL + "/spinning-meroitic-sudan-textile-abu-geili.pdf"
    },
    {
        "title": "Clothing the Elite: Textile Production and Consumption in Ancient Sudan and Nubia",
        "title_ar": "\u0643\u0633\u0648\u0629 \u0627\u0644\u0646\u062e\u0628\u0629: \u0625\u0646\u062a\u0627\u062c \u0627\u0644\u0646\u0633\u064a\u062c \u0648\u0627\u0633\u062a\u0647\u0644\u0627\u0643\u0647 \u0641\u064a \u0627\u0644\u0633\u0648\u062f\u0627\u0646 \u0648\u0627\u0644\u0646\u0648\u0628\u0629 \u0627\u0644\u0642\u062f\u064a\u0645\u064a\u0646",
        "author": "Unknown",
        "tags": ["Ancient Sudan", "History", "Nubian History"],
        "desc": "An examination of the Meroitic Kingdom's unique textile tradition — documented through hundreds of preserved fabrics, tools and iconography — arguing that textiles functioned as luxury status markers for the Meroitic elite and that the kingdom developed a sophisticated, specialized craft economy around their production.",
        "desc_ar": "\u062f\u0631\u0627\u0633\u0629 \u0644\u0644\u062a\u0642\u0627\u0644\u064a\u062f \u0627\u0644\u0646\u0633\u064a\u062c\u064a\u0629 \u0627\u0644\u0641\u0631\u064a\u062f\u0629 \u0644\u0645\u0645\u0644\u0643\u0629 \u0645\u0631\u0648\u064a\u060c \u062a\u062c\u0627\u062f\u0644 \u0623\u0646 \u0627\u0644\u0645\u0646\u0633\u0648\u062c\u0627\u062a \u0643\u0627\u0646\u062a \u0645\u0624\u0634\u0631\u0627\u062a \u0645\u0643\u0627\u0646\u0629 \u0627\u062c\u062a\u0645\u0627\u0639\u064a\u0629 \u0644\u0644\u0646\u062e\u0628\u0629 \u0648\u0623\u0646 \u0627\u0644\u0645\u0645\u0644\u0643\u0629 \u0637\u0648\u0631\u062a \u0627\u0642\u062a\u0635\u0627\u062f\u0627\u064b \u062d\u0631\u0641\u064a\u0627\u064b \u0645\u062a\u062e\u0635\u0635\u0627\u064b \u062d\u0648\u0644 \u0625\u0646\u062a\u0627\u062c\u0647\u0627.",
        "source": BASE_URL + "/clothing-elite-textile-production-ancient-sudan.pdf"
    },
    {
        "title": "Building Textile Archaeology in Ancient Sudan: The TexMeroe Project",
        "title_ar": "\u0628\u0646\u0627\u0621 \u0639\u0644\u0645 \u0622\u062b\u0627\u0631 \u0627\u0644\u0645\u0646\u0633\u0648\u062c\u0627\u062a \u0641\u064a \u0627\u0644\u0633\u0648\u062f\u0627\u0646 \u0627\u0644\u0642\u062f\u064a\u0645: \u0645\u0634\u0631\u0648\u0639 \u062a\u064a\u0643\u0633\u0645\u064a\u0631\u0648\u064a",
        "author": "Unknown",
        "tags": ["Ancient Sudan", "History", "Nubian History"],
        "desc": "A report on the TexMeroe Project's systematic documentation of 235 Meroitic textiles and 244 tools, identifying three distinctive techniques — openwork borders, pile weave, and dye production — that mark Meroitic textile craft as uniquely developed and economically significant within the ancient world.",
        "desc_ar": "\u062a\u0642\u0631\u064a\u0631 \u0639\u0646 \u0645\u0634\u0631\u0648\u0639 \u062a\u064a\u0643\u0633\u0645\u064a\u0631\u0648\u064a \u0644\u062a\u0648\u062b\u064a\u0642  235 \u0645\u0646\u0633\u0648\u062c\u0627\u064b \u0645\u0631\u0648\u064a\u0627\u064b \u0648244 \u0623\u062f\u0627\u0629\u060c \u064a\u0643\u0634\u0641 \u062b\u0644\u0627\u062b\u0629 \u062a\u0642\u0646\u064a\u0627\u062a \u0645\u0645\u064a\u0632\u0629 \u062a\u0624\u0643\u062f \u0623\u0647\u0645\u064a\u0629 \u0635\u0646\u0627\u0639\u0629 \u0627\u0644\u0645\u0646\u0633\u0648\u062c\u0627\u062a \u0627\u0644\u0645\u0631\u0648\u064a\u0629 \u0628\u0648\u0635\u0641\u0647\u0627 \u0646\u0638\u0627\u0645\u0627\u064b \u0627\u0642\u062a\u0635\u0627\u062f\u064a\u0627\u064b \u062d\u0631\u0641\u064a\u0627\u064b \u0645\u062a\u0637\u0648\u0631\u0627\u064b.",
        "source": BASE_URL + "/building-textile-archaeology-ancient-sudan-texmeroe.pdf"
    },
    {
        "title": "Gold Mining Concessions in Sudan's Written Laws and Practices in the Nuba Mountains",
        "title_ar": "\u0627\u0645\u062a\u064a\u0627\u0632\u0627\u062a \u0627\u0644\u062a\u0639\u062f\u064a\u0646 \u0627\u0644\u0630\u0647\u0628\u064a \u0641\u064a \u0627\u0644\u0642\u0648\u0627\u0646\u064a\u0646 \u0627\u0644\u0633\u0648\u062f\u0627\u0646\u064a\u0629 \u0648\u0627\u0644\u0645\u0645\u0627\u0631\u0633\u0627\u062a \u0627\u0644\u0641\u0639\u0644\u064a\u0629 \u0641\u064a \u062c\u0628\u0627\u0644 \u0627\u0644\u0646\u0648\u0628\u0629",
        "author": "Unknown",
        "tags": ["Economy & Development", "Governance & Politics", "Resources"],
        "desc": "A study of the gap between Sudan's Mineral Resources and Mining Development Act (2007) and actual gold extraction practices in the Nuba Mountains, applying Weber's legality-legitimacy framework to expose how resource governance failures deepen local grievances and concentrate wealth away from producing communities.",
        "desc_ar": "\u062f\u0631\u0627\u0633\u0629 \u0627\u0644\u0641\u062c\u0648\u0629 \u0628\u064a\u0646 \u0642\u0627\u0646\u0648\u0646 \u0627\u0644\u0645\u0648\u0627\u0631\u062f \u0627\u0644\u0645\u0639\u062f\u0646\u064a\u0629 \u0648\u0627\u0644\u0645\u0645\u0627\u0631\u0633\u0627\u062a \u0627\u0644\u0641\u0639\u0644\u064a\u0629 \u0644\u0627\u0633\u062a\u062e\u0631\u0627\u062c \u0627\u0644\u0630\u0647\u0628 \u0641\u064a \u062c\u0628\u0627\u0644 \u0627\u0644\u0646\u0648\u0628\u0629\u060c \u0645\u0633\u062a\u062e\u062f\u0645\u0629\u064b \u0625\u0637\u0627\u0631 \u0641\u064a\u0628\u0631 \u0644\u0644\u0634\u0631\u0639\u064a\u0629 \u0648\u0627\u0644\u0642\u0627\u0646\u0648\u0646\u064a\u0629.",
        "source": BASE_URL + "/gold-mining-concessions-sudan-nuba-mountains.pdf"
    },
    {
        "title": "The Gold Boom in Sudan: Challenges and Opportunities for National Economic Players",
        "title_ar": "\u0637\u0641\u0631\u0629 \u0627\u0644\u0630\u0647\u0628 \u0641\u064a \u0627\u0644\u0633\u0648\u062f\u0627\u0646: \u0627\u0644\u062a\u062d\u062f\u064a\u0627\u062a \u0648\u0627\u0644\u0641\u0631\u0635 \u0644\u0644\u0641\u0627\u0639\u0644\u064a\u0646 \u0627\u0644\u0627\u0642\u062a\u0635\u0627\u062f\u064a\u064a\u0646 \u0627\u0644\u0648\u0637\u0646\u064a\u064a\u0646",
        "author": "Unknown",
        "tags": ["Economy & Development", "Resources", "Governance & Politics"],
        "desc": "An analysis of Sudan's post-2011 gold boom — triggered by the loss of South Sudan's oil revenues — examining how elite capture and institutional failure have subverted resource governance, deepened social cleavages, and made the gold sector a driver of conflict rather than development.",
        "desc_ar": "\u062a\u062d\u0644\u064a\u0644 \u0637\u0641\u0631\u0629 \u0627\u0644\u0630\u0647\u0628 \u0628\u0639\u062f 2011 \u0641\u064a \u0627\u0644\u0633\u0648\u062f\u0627\u0646\u060c \u064a\u0643\u0634\u0641 \u0643\u064a\u0641 \u0623\u0641\u0636\u062a \u0647\u064a\u0645\u0646\u0629 \u0627\u0644\u0646\u062e\u0628 \u0648\u0641\u0634\u0644 \u0627\u0644\u0645\u0624\u0633\u0633\u0627\u062a \u0625\u0644\u0649 \u062a\u062d\u0648\u064a\u0644 \u0642\u0637\u0627\u0639 \u0627\u0644\u0630\u0647\u0628 \u0645\u0646 \u0623\u062f\u0627\u0629 \u062a\u0646\u0645\u064a\u0629 \u0625\u0644\u0649 \u0645\u062d\u0631\u0643 \u0635\u0631\u0627\u0639.",
        "source": BASE_URL + "/gold-boom-sudan-challenges-opportunities.pdf"
    },
    {
        "title": "Muhammad Ali's Conquest of Sudan 1820-1824",
        "title_ar": "\u063a\u0632\u0648 \u0645\u062d\u0645\u062f \u0639\u0644\u064a \u0644\u0644\u0633\u0648\u062f\u0627\u0646 1820\u20131824",
        "author": "Unknown",
        "tags": ["History", "Sudan History", "Governance & Politics"],
        "desc": "A detailed account of the two Turco-Egyptian expeditions that conquered Sudan for Muhammad Ali Pasha — the first seizing the Funj Kingdom in 1820-21, the second taking Kordofan — showing that the main goals (gold and slave soldiers) were not achieved while the brutal tax regime triggered the 1822 Shandī revolt.",
        "desc_ar": "\u0633\u0631\u062f \u062a\u0641\u0635\u064a\u0644\u064a \u0644\u0644\u062d\u0645\u0644\u062a\u064a\u0646 \u0627\u0644\u062a\u0631\u0643\u064a\u0629 \u0627\u0644\u0645\u0635\u0631\u064a\u062a\u064a\u0646 \u0627\u0644\u0644\u062a\u064a\u0646 \u063a\u0632\u062a\u0627 \u0627\u0644\u0633\u0648\u062f\u0627\u0646 \u0644\u0635\u0627\u0644\u062d \u0645\u062d\u0645\u062f \u0639\u0644\u064a\u060c \u064a\u0648\u0636\u062d \u0623\u0646 \u0623\u0647\u062f\u0627\u0641 \u0627\u0644\u063a\u0632\u0648 \u0627\u0644\u0631\u0626\u064a\u0633\u064a\u0629 \u0644\u0645 \u062a\u062a\u062d\u0642\u0642 \u0628\u064a\u0646\u0645\u0627 \u0623\u0641\u0636\u062a \u0633\u064a\u0627\u0633\u0629 \u0627\u0644\u0636\u0631\u0627\u0626\u0628 \u0627\u0644\u0642\u0627\u0633\u064a\u0629 \u0625\u0644\u0649 \u0627\u0646\u062a\u0641\u0627\u0636\u0629 \u0634\u0646\u062f\u064a 1822.",
        "source": BASE_URL + "/muhammad-ali-conquest-sudan-1820-1824.pdf"
    },
    {
        "title": "The Ottomans and the Funj Sultanate in the Sixteenth and Seventeenth Centuries",
        "title_ar": "\u0627\u0644\u0639\u062b\u0645\u0627\u0646\u064a\u0648\u0646 \u0648\u0633\u0644\u0637\u0646\u0629 \u0627\u0644\u0641\u0648\u0646\u062c \u0641\u064a \u0627\u0644\u0642\u0631\u0646\u064a\u0646 \u0627\u0644\u0633\u0627\u062f\u0633 \u0639\u0634\u0631 \u0648\u0627\u0644\u0633\u0627\u0628\u0639 \u0639\u0634\u0631",
        "author": "A.C.S. Peacock",
        "tags": ["History", "Sudan History", "Governance & Politics"],
        "desc": "A scholarly examination of Ottoman archival sources and 17th-century travel accounts for the Funj Sultanate of Sennar, revealing the extent of Ottoman-Funj diplomatic and religious contacts and clarifying the relationship between the two powers in the Nile Valley.",
        "desc_ar": "\u062f\u0631\u0627\u0633\u0629 \u0623\u0643\u0627\u062f\u064a\u0645\u064a\u0629 \u0644\u0644\u0645\u0635\u0627\u062f\u0631 \u0627\u0644\u0639\u062b\u0645\u0627\u0646\u064a\u0629 \u0648\u0631\u0648\u0627\u064a\u0627\u062a \u0627\u0644\u0631\u062d\u0627\u0644\u0629 \u0645\u0646 \u0627\u0644\u0642\u0631\u0646 17 \u062d\u0648\u0644 \u0633\u0644\u0637\u0646\u0629 \u0627\u0644\u0641\u0648\u0646\u062c \u0628\u0633\u0646\u0627\u0631\u060c \u062a\u0643\u0634\u0641 \u062d\u062c\u0645 \u0627\u0644\u0639\u0644\u0627\u0642\u0627\u062a \u0627\u0644\u062f\u0628\u0644\u0648\u0645\u0627\u0633\u064a\u0629 \u0648\u0627\u0644\u062f\u064a\u0646\u064a\u0629 \u0628\u064a\u0646 \u0627\u0644\u0642\u0648\u062a\u064a\u0646 \u0641\u064a \u0648\u0627\u062f\u064a \u0627\u0644\u0646\u064a\u0644.",
        "source": BASE_URL + "/ottomans-funj-sultanate-sixteenth-seventeenth.pdf"
    },
    {
        "title": "Swan Song in the Nile Valley: The Mamluk Statelet in Dongola 1812-1820",
        "title_ar": "\u0646\u0634\u064a\u062f \u0627\u0644\u0648\u062f\u0627\u0639 \u0641\u064a \u0648\u0627\u062f\u064a \u0627\u0644\u0646\u064a\u0644: \u0643\u064a\u0627\u0646 \u0627\u0644\u0645\u0645\u0627\u0644\u064a\u0643 \u0641\u064a \u062f\u0646\u0642\u0644\u0629 1812\u20131820",
        "author": "Unknown",
        "tags": ["History", "Sudan History", "Ancient Sudan"],
        "desc": "A focused study of the short-lived Mamluk principality in Dongola (1812-1820), formed by Mamluks fleeing Muhammad Ali's Egypt, existing in constant war with the Shaiqiyya tribe before being extinguished by the same Turco-Egyptian conquest that brought Sudan under Egyptian rule.",
        "desc_ar": "\u062f\u0631\u0627\u0633\u0629 \u0645\u0639\u0645\u0651\u0642\u0629 \u0641\u064a \u0627\u0644\u0643\u064a\u0627\u0646 \u0627\u0644\u0645\u0645\u0644\u0648\u0643\u064a \u0642\u0635\u064a\u0631 \u0627\u0644\u0639\u0645\u0631 \u0641\u064a \u062f\u0646\u0642\u0644\u0629\u060c \u0627\u0644\u0630\u064a \u0623\u0633\u0633\u0647 \u0645\u0645\u0627\u0644\u064a\u0643 \u0641\u0627\u0631\u0648\u0646 \u0645\u0646 \u0645\u0635\u0631 \u0645\u062d\u0645\u062f \u0639\u0644\u064a\u060c \u0648\u0639\u0627\u0634 \u0641\u064a \u062d\u0631\u0648\u0628 \u0645\u062a\u0648\u0627\u0635\u0644\u0629 \u0645\u0639 \u0627\u0644\u0634\u0627\u064a\u0642\u064a\u0629 \u062d\u062a\u0649 \u0642\u0636\u0649 \u0639\u0644\u064a\u0647 \u0627\u0644\u063a\u0632\u0648 \u0627\u0644\u062a\u0631\u0643\u064a \u0627\u0644\u0645\u0635\u0631\u064a.",
        "source": BASE_URL + "/swan-song-nile-valley-mamluk-dongola.pdf"
    },
    {
        "title": "The Formation of the Sudanese Mahdist State: Ceremony and Symbols of Authority 1882-1898",
        "title_ar": "\u062a\u0634\u0643\u064a\u0644 \u0627\u0644\u062f\u0648\u0644\u0629 \u0627\u0644\u0645\u0647\u062f\u0648\u064a\u0629 \u0627\u0644\u0633\u0648\u062f\u0627\u0646\u064a\u0629: \u0627\u0644\u0637\u0642\u0648\u0633 \u0648\u0631\u0645\u0648\u0632 \u0627\u0644\u0633\u0644\u0637\u0629 1882\u20131898",
        "author": "Unknown",
        "tags": ["History", "Sudan History", "Governance & Politics"],
        "desc": "A study of how the Mahdist movement constructed political authority between 1882 and 1898 by drawing on Sufi ceremonial traditions and the legitimating symbolism of the earlier Funj and Kayra sultanates — deliberately rejecting the Turco-Egyptian colonial inheritance in favour of an authentically Sudanese Islamic statecraft.",
        "desc_ar": "\u062f\u0631\u0627\u0633\u0629 \u0643\u064a\u0641 \u0628\u0646\u0649 \u0627\u0644\u0645\u0647\u062f\u064a\u0648\u0646 \u0633\u0644\u0637\u062a\u0647\u0645 \u0627\u0644\u0633\u064a\u0627\u0633\u064a\u0629 \u0628\u064a\u0646 1882 \u0648 1898 \u0645\u0633\u062a\u0639\u064a\u0646\u064a\u0646 \u0628\u062a\u0631\u0627\u062b \u0627\u0644\u0637\u0631\u0642 \u0627\u0644\u0635\u0648\u0641\u064a\u0629 \u0648\u0631\u0645\u0648\u0632 \u0633\u0644\u0637\u0646\u062a\u064a \u0627\u0644\u0641\u0648\u0646\u062c \u0648\u0643\u064a\u0631\u0629\u060c \u0631\u0627\u0641\u0636\u064a\u0646 \u0627\u0644\u0625\u0631\u062b \u0627\u0644\u0627\u0633\u062a\u0639\u0645\u0627\u0631\u064a \u0644\u0635\u0627\u0644\u062d \u062d\u0643\u0645 \u0625\u0633\u0644\u0627\u0645\u064a \u0633\u0648\u062f\u0627\u0646\u064a \u0623\u0635\u064a\u0644.",
        "source": BASE_URL + "/formation-sudanese-mahdist-state-1882-1898.pdf"
    },
    {
        "title": "Bibliography of the Mahdist State in Sudan 1881-1898",
        "title_ar": "\u0628\u064a\u0628\u0644\u064a\u0648\u063a\u0631\u0627\u0641\u064a\u0627 \u0627\u0644\u062f\u0648\u0644\u0629 \u0627\u0644\u0645\u0647\u062f\u0648\u064a\u0629 \u0641\u064a \u0627\u0644\u0633\u0648\u062f\u0627\u0646 1881\u20131898",
        "author": "Unknown",
        "tags": ["History", "Sudan History", "Reference"],
        "desc": "A comprehensive annotated bibliography of sources on the Mahdist State (1881-1898), critically examining how British colonial intelligence — particularly Wingate's propaganda — shaped the historiography of the Mahdiyya and identifying the primary Arabic and English sources needed to correct that distortion.",
        "desc_ar": "\u0628\u064a\u0628\u0644\u064a\u0648\u063a\u0631\u0627\u0641\u064a\u0627 \u0634\u0627\u0645\u0644\u0629 \u0648\u0645\u0639\u0644\u0651\u0642\u0629 \u0644\u0645\u0635\u0627\u062f\u0631 \u0627\u0644\u062f\u0648\u0644\u0629 \u0627\u0644\u0645\u0647\u062f\u0648\u064a\u0629\u060c \u062a\u0643\u0634\u0641 \u0643\u064a\u0641 \u0634\u0643\u0651\u0644\u062a \u0627\u0644\u0627\u0633\u062a\u062e\u0628\u0627\u0631\u0627\u062a \u0627\u0644\u0628\u0631\u064a\u0637\u0627\u0646\u064a\u0629 \u2014 \u0648\u062e\u0627\u0635\u0629\u064b \u062f\u0639\u0627\u064a\u0629 \u0648\u064a\u0646\u063a\u064a\u062a \u2014 \u0627\u0644\u062a\u0623\u0631\u064a\u062e\u064e \u0627\u0644\u0633\u0627\u0626\u062f \u0644\u0644\u0645\u0647\u062f\u064a\u0629.",
        "source": ACADEMIA + "/4075679/The_Bibliography_of_the_Mahdist_State_in_the_Sudan_1898_1898"
    },
    {
        "title": "The Gezira Irrigation Scheme in Sudan: Objectives, Design, and Performance",
        "title_ar": "\u0645\u0634\u0631\u0648\u0639 \u0627\u0644\u062c\u0632\u064a\u0631\u0629 \u0644\u0644\u0631\u064a \u0641\u064a \u0627\u0644\u0633\u0648\u062f\u0627\u0646: \u0627\u0644\u0623\u0647\u062f\u0627\u0641 \u0648\u0627\u0644\u062a\u0635\u0645\u064a\u0645 \u0648\u0627\u0644\u0623\u062f\u0627\u0621",
        "author": "World Bank",
        "tags": ["Agriculture", "Economy & Development", "Infrastructure"],
        "desc": "The definitive World Bank technical assessment of the Gezira Scheme — the world's largest irrigation project — tracing its expansion from 300,000 to 2.1 million feddans, documenting the persistent yield gap between research station and field performance, and setting the agenda for rehabilitation that still shapes Gezira policy today.",
        "desc_ar": "\u0627\u0644\u062a\u0642\u064a\u064a\u0645 \u0627\u0644\u062a\u0642\u0646\u064a \u0627\u0644\u062d\u0627\u0633\u0645 \u0644\u0644\u0628\u0646\u0643 \u0627\u0644\u062f\u0648\u0644\u064a \u0644\u0645\u0634\u0631\u0648\u0639 \u0627\u0644\u062c\u0632\u064a\u0631\u0629 \u0644\u0644\u0631\u064a \u2014 \u0623\u0643\u0628\u0631 \u0645\u0634\u0631\u0648\u0639 \u0631\u064a \u0641\u064a \u0627\u0644\u0639\u0627\u0644\u0645 \u2014 \u0645\u0648\u062b\u0642\u064a\u0646\u0627\u064b \u062a\u0648\u0633\u0639\u0647 \u0645\u0646 300\u0623\u0644\u0641 \u0625\u0644\u0649 2.1 \u0645\u0644\u064a\u0648\u0646 \u0641\u062f\u0627\u0646.",
        "source": BASE_URL + "/gezira-irrigation-scheme-sudan-objectives-performance.pdf"
    },
    {
        "title": "Challenges of Agricultural Technology Transfer and Productivity Increase in Sudan",
        "title_ar": "\u062a\u062d\u062f\u064a\u0627\u062a \u0646\u0642\u0644 \u0627\u0644\u062a\u0643\u0646\u0648\u0644\u0648\u062c\u064a\u0627 \u0627\u0644\u0632\u0631\u0627\u0639\u064a\u0629 \u0648\u0632\u064a\u0627\u062f\u0629 \u0627\u0644\u0625\u0646\u062a\u0627\u062c\u064a\u0629 \u0641\u064a \u0627\u0644\u0633\u0648\u062f\u0627\u0646",
        "author": "Unknown",
        "tags": ["Agriculture", "Economy & Development"],
        "desc": "A policy-oriented analysis showing that Sudanese crop yields reach only 30% of research-station potential, diagnosing the systemic failures in technology transfer — from input delivery delays in the Gezira to rain-fed sector neglect — and recommending targeted investments in extension services and vertical productivity gains.",
        "desc_ar": "\u062a\u062d\u0644\u064a\u0644 \u0633\u064a\u0627\u0633\u0627\u062a\u064a \u064a\u0643\u0634\u0641 \u0623\u0646 \u0645\u062d\u0627\u0635\u064a\u0644 \u0627\u0644\u0633\u0648\u062f\u0627\u0646 \u0644\u0627 \u062a\u062a\u062c\u0627\u0648\u0632 30% \u0645\u0646 \u0637\u0627\u0642\u062a\u0647\u0627 \u0627\u0644\u0628\u062d\u062b\u064a\u0629\u060c \u0648\u064a\u0634\u062e\u0651\u0635 \u0623\u0648\u062c\u0647 \u0627\u0644\u0642\u0635\u0648\u0631 \u0627\u0644\u0647\u064a\u0643\u0644\u064a\u0629 \u0641\u064a \u0646\u0642\u0644 \u0627\u0644\u062a\u0643\u0646\u0648\u0644\u0648\u062c\u064a\u0627 \u0648\u064a\u0642\u062f\u0645 \u062a\u0648\u0635\u064a\u0627\u062a \u0644\u0644\u062a\u0648\u0633\u0639 \u0627\u0644\u0631\u0623\u0633\u064a.",
        "source": BASE_URL + "/challenges-agricultural-technology-transfer-sudan.pdf"
    },
    {
        "title": "Impact of Changing Policies on Agricultural Productivity: The Gezira Scheme",
        "title_ar": "\u0623\u062b\u0631 \u062a\u063a\u064a\u064a\u0631 \u0627\u0644\u0633\u064a\u0627\u0633\u0627\u062a \u0639\u0644\u0649 \u0627\u0644\u0625\u0646\u062a\u0627\u062c\u064a\u0629 \u0627\u0644\u0632\u0631\u0627\u0639\u064a\u0629: \u0645\u0634\u0631\u0648\u0639 \u0627\u0644\u062c\u0632\u064a\u0631\u0629",
        "author": "Unknown",
        "tags": ["Agriculture", "Economy & Development", "Governance & Politics"],
        "desc": "An econometric study of how liberalization, privatization, and crop-choice deregulation in the Gezira Scheme since the 1990s affected cotton, sorghum, and wheat productivity — finding that causality relationships between policy changes and output varied sharply by crop, with wheat showing no response due to climatic unsuitability.",
        "desc_ar": "\u062f\u0631\u0627\u0633\u0629 \u0642\u064a\u0627\u0633\u064a\u0629 \u0644\u062a\u0623\u062b\u064a\u0631 \u0627\u0644\u062a\u062d\u0631\u064a\u0631 \u0648\u0627\u0644\u062e\u0635\u062e\u0635\u0629 \u0648\u0631\u0641\u0639 \u0627\u0644\u0642\u064a\u0648\u062f \u0639\u0646 \u0627\u062e\u062a\u064a\u0627\u0631 \u0627\u0644\u0645\u062d\u0627\u0635\u064a\u0644 \u0641\u064a \u0645\u0634\u0631\u0648\u0639 \u0627\u0644\u062c\u0632\u064a\u0631\u0629 \u0645\u0646\u0630 1990\u060c \u0648\u0623\u062b\u0631\u0647\u0627 \u0639\u0644\u0649 \u0625\u0646\u062a\u0627\u062c\u064a\u0629 \u0627\u0644\u0642\u0637\u0646 \u0648\u0627\u0644\u0630\u0631\u0629 \u0648\u0627\u0644\u0642\u0645\u062d.",
        "source": BASE_URL + "/impact-changing-policies-agricultural-productivity-gezira.pdf"
    },
    {
        "title": "A History of Modern Sudan",
        "title_ar": "\u062a\u0627\u0631\u064a\u062e \u0627\u0644\u0633\u0648\u062f\u0627\u0646 \u0627\u0644\u062d\u062f\u064a\u062b",
        "author": "Robert O. Collins",
        "tags": ["History", "Sudan History", "Governance & Politics"],
        "desc": "A sweeping narrative history of Sudan from Muhammad Ali's 1821 conquest through the post-independence era, showing how the recurrent patterns of civil war, religious-ethnic division, and failed leadership planted in the colonial period have shaped every subsequent crisis — essential background for any serious analysis of Sudan's development challenges.",
        "desc_ar": "\u0633\u0631\u062f \u062a\u0627\u0631\u064a\u062e\u064a \u0634\u0627\u0645\u0644 \u0644\u0644\u0633\u0648\u062f\u0627\u0646 \u0645\u0646 \u063a\u0632\u0648 \u0645\u062d\u0645\u062f \u0639\u0644\u064a 1821 \u062d\u062a\u0649 \u0645\u0631\u062d\u0644\u0629 \u0645\u0627 \u0628\u0639\u062f \u0627\u0644\u0627\u0633\u062a\u0642\u0644\u0627\u0644\u060c \u064a\u0643\u0634\u0641 \u0643\u064a\u0641 \u0623\u0633\u0647\u0645\u062a \u0627\u0644\u0623\u0646\u0645\u0627\u0637 \u0627\u0644\u0645\u062a\u0643\u0631\u0631\u0629 \u0645\u0646 \u0627\u0644\u062d\u0631\u0628 \u0627\u0644\u0623\u0647\u0644\u064a\u0629 \u0648\u0627\u0644\u0627\u0646\u0642\u0633\u0627\u0645 \u0627\u0644\u062f\u064a\u0646\u064a \u0627\u0644\u0625\u062b\u0646\u064a \u0641\u064a \u062a\u0634\u0643\u064a\u0644 \u0643\u0644 \u0623\u0632\u0645\u0629 \u0644\u0627\u062d\u0642\u0629.",
        "source": BASE_URL + "/history-of-modern-sudan-collins.pdf"
    },
]

# Update JSON
existing_sources = {b.get("source", "") for b in lib["books"]}
added_json = 0
for book in new_books:
    if book["source"] not in existing_sources:
        lib["books"].append(book)
        added_json += 1
        print("  Added: " + book["title"])
    else:
        print("  SKIP: " + book["title"])

with open(json_path, "w", encoding="utf-8") as f:
    json.dump(lib, f, ensure_ascii=False, indent=2)

# Update CSV
with open(csv_path, encoding="utf-8") as f:
    existing_csv = f.read()

new_csv_rows = []
for book in new_books:
    filename = book["source"].split("/")[-1]
    if filename not in existing_csv:
        new_csv_rows.append(book["title"] + "," + book["author"] + "," + filename + "," + book["source"])

with open(csv_path, "a", encoding="utf-8", newline="") as f:
    for row in new_csv_rows:
        f.write(row + "\n")

print("\nJSON: added " + str(added_json) + " books. Total: " + str(len(lib["books"])) + " books.")
print("CSV: added " + str(len(new_csv_rows)) + " rows.")

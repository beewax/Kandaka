import boto3, os, shutil
from botocore.config import Config

R2_ACCESS_KEY_ID     = "b1f53194ad1d18f9a2c76ed23c39682d"
R2_SECRET_ACCESS_KEY = "85984c671385eef6067149ad7316e0a949f36e42fbf842a0909b098c5f2c0ac6"
ACCOUNT_ID           = "971f88758f6c5f23f2e77a3aa3fb1663"
R2_BUCKET_NAME       = "nilebookstore-books"
ENDPOINT_URL         = "https://" + ACCOUNT_ID + ".r2.cloudflarestorage.com"
BASE_URL             = "https://pub-0c3bb637d5f54b239fe4a4ef9b08bfe3.r2.dev"
DOWNLOADS            = r"C:\Users\Abdulla\Downloads"
SUDAN_PDF_FOLDER     = r"C:\Users\Abdulla\Documents\Sudan PDFs"

s3 = boto3.client(
    "s3",
    endpoint_url=ENDPOINT_URL,
    aws_access_key_id=R2_ACCESS_KEY_ID,
    aws_secret_access_key=R2_SECRET_ACCESS_KEY,
    config=Config(signature_version="s3v4"),
    region_name="auto",
)

FILES = [
    ("Industrial_location_analysis_of_Sudan.pdf",          "industrial-location-analysis-sudan.pdf"),
    ("The_Construction_Industry_of_Sudan_Poten.pdf",       "construction-industry-sudan-potentials-challenges.pdf"),
    ("Development_Economics_in_Sudan_TheTen_Ye.pdf",       "development-economics-sudan-ten-year-plan.pdf"),
    ("Cotton_Export_Performance_and_Constraint.pdf",       "cotton-export-performance-constraints-sudan.pdf"),
    ("Spinning_in_Meroitic_Sudan_Textile_Imple.pdf",       "spinning-meroitic-sudan-textile-abu-geili.pdf"),
    ("Clothing_the_elite_Patterns_of_textile_p.pdf",       "clothing-elite-textile-production-ancient-sudan.pdf"),
    ("Building_textile_archaeology_in_ancient.pdf",        "building-textile-archaeology-ancient-sudan-texmeroe.pdf"),
    ("Gold_mining_concessions_in_Sudans_writte.pdf",       "gold-mining-concessions-sudan-nuba-mountains.pdf"),
    ("The_Gold_Boom_in_Sudan_Challenges_and_Op.pdf",       "gold-boom-sudan-challenges-opportunities.pdf"),
    ("MUHAMMAD_ALI_S_CONQUEST_OF_SUDAN_1820_18.pdf",       "muhammad-ali-conquest-sudan-1820-1824.pdf"),
    ("The_Ottomans_and_the_Funj_Sultanate_in_t.pdf",       "ottomans-funj-sultanate-sixteenth-seventeenth.pdf"),
    ("SWAN_SONG_IN_THE_NILE_VALLEY_THE_MAMLUK.pdf",        "swan-song-nile-valley-mamluk-dongola.pdf"),
    ("The_Formation_of_the_Sudanese_Mahdist_St.pdf",       "formation-sudanese-mahdist-state-1882-1898.pdf"),
    ("The_Gezira_Irrigation_Scheme_in_Sudan_Ob.pdf",       "gezira-irrigation-scheme-sudan-objectives-performance.pdf"),
    ("Challenges_of_agricultural_technology_tr.pdf",       "challenges-agricultural-technology-transfer-sudan.pdf"),
    ("Impact_of_changing_policies_on_agricultu.pdf",       "impact-changing-policies-agricultural-productivity-gezira.pdf"),
    ("A_HISTORY_OF_MODERN_SUDAN.pdf",                      "history-of-modern-sudan-collins.pdf"),
]

os.makedirs(SUDAN_PDF_FOLDER, exist_ok=True)
print("Sudan PDFs folder: " + SUDAN_PDF_FOLDER + "\n")
print("Uploading " + str(len(FILES)) + " files...\n")

success = 0
moved = 0
for filename, key in FILES:
    local_path = os.path.join(DOWNLOADS, filename)
    if not os.path.exists(local_path):
        print("  MISSING: " + filename)
        continue
    size_mb = os.path.getsize(local_path) / (1024 * 1024)
    print("  " + key + " (" + str(round(size_mb, 1)) + " MB)...", end=" ", flush=True)
    try:
        s3.upload_file(local_path, R2_BUCKET_NAME, key, ExtraArgs={"ContentType": "application/pdf"})
        print("uploaded", end=" ")
        success += 1
        dest = os.path.join(SUDAN_PDF_FOLDER, filename)
        shutil.move(local_path, dest)
        print("-> moved")
        moved += 1
    except Exception as e:
        print("FAILED: " + str(e))

print("\n" + str(success) + "/" + str(len(FILES)) + " uploaded, " + str(moved) + " moved to Sudan PDFs folder.")

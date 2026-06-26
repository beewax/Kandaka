import boto3, os
from botocore.config import Config

R2_ACCESS_KEY_ID     = "b1f53194ad1d18f9a2c76ed23c39682d"
R2_SECRET_ACCESS_KEY = "85984c671385eef6067149ad7316e0a949f36e42fbf842a0909b098c5f2c0ac6"
ACCOUNT_ID           = "971f88758f6c5f23f2e77a3aa3fb1663"
R2_BUCKET_NAME       = "nilebookstore-books"
ENDPOINT_URL         = "https://" + ACCOUNT_ID + ".r2.cloudflarestorage.com"
BASE_URL             = "https://pub-0c3bb637d5f54b239fe4a4ef9b08bfe3.r2.dev"

s3 = boto3.client(
    "s3",
    endpoint_url=ENDPOINT_URL,
    aws_access_key_id=R2_ACCESS_KEY_ID,
    aws_secret_access_key=R2_SECRET_ACCESS_KEY,
    config=Config(signature_version="s3v4"),
    region_name="auto",
)

FILES = [
    (r"C:\Users\Abdulla\Downloads\The Candaces of Meroe - World History Encyclopedia.pdf",
     "candaces-of-meroe-world-history-encyclopedia.pdf", "application/pdf"),
    (r"C:\Users\Abdulla\Downloads\The_Queen_Mother_in_the_Kingdom_of_Kush.pdf",
     "queen-mother-kingdom-of-kush.pdf", "application/pdf"),
    (r"C:\Users\Abdulla\Downloads\SARS_SN21_Grzymski.pdf",
     "sars-sn21-grzymski.pdf", "application/pdf"),
]

print("Uploading " + str(len(FILES)) + " files to R2 bucket: " + R2_BUCKET_NAME + "\n")
success = 0
for local_path, key, content_type in FILES:
    if not os.path.exists(local_path):
        print("  MISSING: " + local_path)
        continue
    size_mb = os.path.getsize(local_path) / (1024 * 1024)
    print("  Uploading " + key + " (" + str(round(size_mb, 1)) + " MB)...", end=" ", flush=True)
    try:
        s3.upload_file(local_path, R2_BUCKET_NAME, key, ExtraArgs={"ContentType": content_type})
        print("OK  ->  " + BASE_URL + "/" + key)
        success += 1
    except Exception as e:
        print("FAILED: " + str(e))

print("\n" + str(success) + "/" + str(len(FILES)) + " files uploaded successfully.")

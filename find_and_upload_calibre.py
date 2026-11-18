"""Kandaka PDF archive uploader: explicit manifest, dry-run by default.

Manifest JSON is an array of objects with:
  {"title": "...", "local_path": "D:/.../paper.pdf",
   "doi": "10.xxxx/...", "license_verified": true,
   "license_evidence": "https://publisher/...", "redistribution_allowed": true}

No fuzzy matching, no title-based replacement, no credential literals.
Run: python find_and_upload_calibre.py --manifest archive-manifest.json
To write: add --apply, after checking the dry-run output.
Requires boto3 only for --apply, and environment secrets for R2.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
from urllib.parse import quote

DEFAULT_BUCKET = "kandaka-library"
DEFAULT_PUBLIC_URL = "https://pub-0c3bb637d5f54b239fe4a4ef9b08bfe3.r2.dev"


def digest_pdf(path):
    with open(path, "rb") as handle:
        if handle.read(5) != b"%PDF-":
            raise ValueError("File is not a PDF")
        handle.seek(0)
        sha = hashlib.sha256()
        while True:
            chunk = handle.read(1024 * 1024)
            if not chunk:
                break
            sha.update(chunk)
    return sha.hexdigest()


def load_manifest(path):
    rows = json.loads(Path(path).read_text(encoding="utf-8"))
    if not isinstance(rows, list):
        raise ValueError("Manifest must be a JSON array")
    return rows


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--manifest", required=True)
    p.add_argument("--apply", action="store_true", help="Actually upload verified files")
    p.add_argument("--bucket", default=os.getenv("KANDAKA_R2_BUCKET", DEFAULT_BUCKET))
    p.add_argument("--public-url", default=os.getenv("KANDAKA_R2_PUBLIC_URL", DEFAULT_PUBLIC_URL))
    args = p.parse_args()

    rows = load_manifest(args.manifest)
    prepared = []
    for i, row in enumerate(rows, 1):
        title = row.get("title", "").strip()
        doi = row.get("doi", "").strip()
        local = Path(row.get("local_path", ""))
        evidence = row.get("license_evidence", "").strip()
        if not title or not doi or not evidence:
            raise ValueError(f"Row {i}: title, DOI and license_evidence are required")
        if row.get("license_verified") is not True or row.get("redistribution_allowed") is not True:
            raise ValueError(f"Row {i}: redistribution not independently cleared")
        if not local.is_file() or local.suffix.lower() != ".pdf":
            raise ValueError(f"Row {i}: missing or non-PDF file: {local}")
        sha = digest_pdf(local)
        key = f"research/{doi.lower().replace('/', '_')}-{sha[:12]}.pdf"
        prepared.append((title, doi, local, key, sha))

    print(json.dumps([{"title":t, "doi":d, "file":str(f), "key":k, "sha256":s,
                       "mode":"upload" if args.apply else "dry-run"} for t,d,f,k,s in prepared], indent=2))
    if not args.apply:
        print("DRY RUN: no R2 or Library changes")
        return

    import boto3
    from botocore.config import Config
    account = os.environ["CLOUDFLARE_ACCOUNT_ID"]
    client = boto3.client(
        "s3",
        endpoint_url=f"https://{account}.r2.cloudflarestorage.com",
        aws_access_key_id=os.environ["R2_ACCESS_KEY_ID"],
        aws_secret_access_key=os.environ["R2_SECRET_ACCESS_KEY"],
        config=Config(signature_version="s3v4"),
        region_name="auto",
    )
    if args.bucket != DEFAULT_BUCKET:
        raise ValueError("Refusing to upload outside kandaka-library")
    for title, doi, local, key, sha in prepared:
        try:
            client.head_object(Bucket=args.bucket, Key=key)
            print(f"EXISTS, NOT OVERWRITTEN: {key}")
            continue
        except client.exceptions.ClientError as e:
            if e.response.get("ResponseMetadata", {}).get("HTTPStatusCode") != 404:
                raise
        client.upload_file(
            str(local), args.bucket, key,
            ExtraArgs={"ContentType": "application/pdf", "Metadata": {"sha256": sha, "doi": doi}},
        )
        check = client.head_object(Bucket=args.bucket, Key=key)
        if check["ContentLength"] != local.stat().st_size or check.get("Metadata", {}).get("sha256") != sha:
            raise RuntimeError(f"R2 verification failed for {key}")
        print(f"VERIFIED: {args.public_url.rstrip('/')}/{quote(key, safe='/')} | {title}")
    print("No catalogue entries were changed. Review and update bilingual Library metadata separately.")


if __name__ == "__main__":
    main()

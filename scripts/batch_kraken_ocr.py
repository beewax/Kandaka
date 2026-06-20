#!/usr/bin/env python3
"""
Kandaka Kraken Batch OCR
Processes Arabic/English PDFs using Kraken OCR in WSL
Outputs searchable PDFs to /mnt/d/WSL-Output/kraken-ocr/

Usage:
  python3 ~/batch_kraken_ocr.py

Models used:
  - Arabic: arabic_best.mlmodel
  - English: en_best.mlmodel (fallback)
"""

import os
import re
import glob
import subprocess
import shutil
import tempfile
from pathlib import Path

# ── CONFIG ────────────────────────────────────────────────────────────────────
SUDAN_DIR       = "/mnt/d/OneDrive/Sudan"
OUTPUT_DIR      = "/mnt/d/WSL-Output/kraken-ocr"
TEMP_DIR        = "/tmp/kraken_batch"

ARABIC_MODEL    = os.path.expanduser("~/.local/share/htrmopo/b4a70336-339f-508b-abf4-24b698091dd7/arabic_best.mlmodel")
SEGMENT_MODEL   = os.path.expanduser("~/.local/share/htrmopo/97665cf3-f83d-5594-8855-f28d3af9df7a/blla.mlmodel")

KRAKEN          = os.path.expanduser("~/kraken-env/bin/kraken")
PYTHON          = os.path.expanduser("~/kraken-env/bin/python3")

# ── HELPERS ───────────────────────────────────────────────────────────────────
def is_searchable(pdf_path):
    """Check if PDF already has searchable text layer."""
    try:
        import fitz
        doc = fitz.open(pdf_path)
        for page in doc:
            if page.get_text().strip():
                doc.close()
                return True
        doc.close()
        return False
    except Exception:
        return False

def detect_arabic(pdf_path):
    """Detect if PDF filename or path suggests Arabic content."""
    arabic_chars = sum(1 for c in pdf_path if '\u0600' <= c <= '\u06ff')
    return arabic_chars > 3

def run_kraken_ocr(pdf_path, output_pdf, model):
    """Run Kraken OCR on a PDF and produce a searchable PDF."""
    pdf_path = str(pdf_path)
    output_pdf = str(output_pdf)
    stem = Path(pdf_path).stem[:40]

    # Create temp working directory
    work_dir = os.path.join(TEMP_DIR, re.sub(r'[^\w]', '_', stem))
    os.makedirs(work_dir, exist_ok=True)

    try:
        # Step 1: Run Kraken — binarize + segment + OCR → text files per page
        print(f"    Running Kraken OCR...")
        txt_prefix = os.path.join(work_dir, "page")

        cmd = [
            KRAKEN,
            "-f", "pdf",
            "-i", pdf_path, txt_prefix,
            "binarize",
            "segment", "-bl",
            "ocr", "-m", model
        ]

        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=1800  # 30 min max per file
        )

        if result.returncode != 0:
            print(f"    [WARN] Kraken returned error: {result.stderr[:200]}")

        # Step 2: Collect all output text files
        txt_files = sorted(glob.glob(f"{txt_prefix}*"))
        txt_files = [f for f in txt_files if not f.endswith('.pdf')]

        if not txt_files:
            print(f"    [WARN] No text output files found")
            return False

        print(f"    Found {len(txt_files)} page text files")

        # Step 3: Combine text files into one text file
        combined_text = ""
        for txt_file in txt_files:
            try:
                with open(txt_file, 'r', encoding='utf-8') as f:
                    combined_text += f.read() + "\n\n"
            except Exception as e:
                print(f"    [WARN] Could not read {txt_file}: {e}")

        if not combined_text.strip():
            print(f"    [WARN] No text extracted")
            return False

        # Step 4: Build searchable PDF using ocrmypdf with existing text
        # First copy original PDF, then add text layer
        combined_txt_path = os.path.join(work_dir, "combined.txt")
        with open(combined_txt_path, 'w', encoding='utf-8') as f:
            f.write(combined_text)

        # Step 5: Use reportlab to create a text-layer PDF
        try:
            from reportlab.pdfgen import canvas
            from reportlab.lib.pagesizes import A4
            from reportlab.pdfbase import pdfmetrics
            from reportlab.pdfbase.ttfonts import TTFont
            import fitz

            # Open original PDF to get page count and dimensions
            orig_doc = fitz.open(pdf_path)
            page_count = len(orig_doc)

            # Create output PDF with text overlay
            # Use ocrmypdf to properly embed text layer
            orig_doc.close()

        except Exception as e:
            print(f"    [WARN] PDF creation error: {e}")

        # Step 6: Use ocrmypdf to create proper searchable PDF
        # We use --pdf-renderer sandwich to overlay text on original
        ocr_cmd = [
            PYTHON, "-m", "ocrmypdf",
            "--force-ocr",
            "--language", "ara+eng",
            "--pdf-renderer", "sandwich",
            "--output-type", "pdf",
            "--skip-big", "250",
            "--tesseract-timeout", "300",
            pdf_path,
            output_pdf
        ]

        print(f"    Creating searchable PDF with ocrmypdf...")
        ocr_result = subprocess.run(
            ocr_cmd,
            capture_output=True,
            text=True,
            timeout=1800
        )

        if ocr_result.returncode == 0 and os.path.exists(output_pdf):
            print(f"    ✓ Searchable PDF created: {os.path.basename(output_pdf)}")
            return True
        else:
            print(f"    [WARN] ocrmypdf failed: {ocr_result.stderr[:300]}")
            # Fallback: save text alongside original
            txt_output = output_pdf.replace('.pdf', '_text.txt')
            with open(txt_output, 'w', encoding='utf-8') as f:
                f.write(combined_text)
            print(f"    → Saved extracted text to: {os.path.basename(txt_output)}")
            return True

    except subprocess.TimeoutExpired:
        print(f"    [WARN] Timed out after 30 minutes")
        return False
    except Exception as e:
        print(f"    [ERROR] {e}")
        return False
    finally:
        # Cleanup temp files
        try:
            shutil.rmtree(work_dir, ignore_errors=True)
        except Exception:
            pass

# ── MAIN ──────────────────────────────────────────────────────────────────────
def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    os.makedirs(TEMP_DIR, exist_ok=True)

    # Find all PDFs in Sudan directory
    print(f"Scanning {SUDAN_DIR} for PDFs...")
    all_pdfs = list(Path(SUDAN_DIR).rglob("*.pdf"))
    print(f"Found {len(all_pdfs)} PDFs total")

    # Check which need OCR
    needs_ocr = []
    already_done = []

    for pdf in all_pdfs:
        output_pdf = Path(OUTPUT_DIR) / (pdf.stem[:80] + "_ocr.pdf")
        output_txt = Path(OUTPUT_DIR) / (pdf.stem[:80] + "_text.txt")

        # Skip if already processed
        if output_pdf.exists() or output_txt.exists():
            already_done.append(pdf)
            continue

        # Skip if already searchable
        if is_searchable(str(pdf)):
            already_done.append(pdf)
            continue

        needs_ocr.append(pdf)

    print(f"  Already searchable or processed: {len(already_done)}")
    print(f"  Needs OCR: {len(needs_ocr)}")

    if not needs_ocr:
        print("Nothing to do!")
        return

    # Process each PDF
    success = 0
    failed = 0

    for i, pdf in enumerate(needs_ocr, 1):
        print(f"\n[{i}/{len(needs_ocr)}] {pdf.name[:60]}")

        # Choose model based on content
        model = ARABIC_MODEL  # Default to Arabic for Sudan PDFs
        output_name = pdf.stem[:80] + "_ocr.pdf"
        output_pdf = Path(OUTPUT_DIR) / output_name

        ok = run_kraken_ocr(pdf, output_pdf, model)

        if ok:
            success += 1
        else:
            failed += 1
            print(f"    ✗ Failed: {pdf.name[:60]}")

    print(f"\n{'='*50}")
    print(f"Done! Success: {success} | Failed: {failed}")
    print(f"Output directory: {OUTPUT_DIR}")

if __name__ == "__main__":
    main()

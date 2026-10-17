# Library attribution and file-label audit — 17 October 2026

Scope: two source-verified records and format labels only. No articles, covers, bucket settings, publishing schedules or paid files changed. Existing local checkout at C:\Users\Abdulla\Kandaka was left untouched (three pre-existing modified files); fresh main began at e0dff555ff24ac628109926abd43fb41a6fdd77a. Backups and full response audit retained in the task workspace.

## Verified corrections

- Between Kerma and Avaris: Mark Twain → Enrico Dirminti, 2014. Bilingual author and summary corrected; replaced inaccessible copied EPUB with the author-uploaded paper record. ResearchGate exposes the author-uploaded full text; access to its download remains subject to ResearchGate.
  https://www.researchgate.net/publication/215767896_Between_Kerma_and_Avaris_the_first_Kingdom_of_Kush_and_Egypt_during_the_Second_Intermediate_Period
- Nubian Archaeology in the 21st Century: N. K. Jemisin → Matthieu Honegger (editor), 2018. Bilingual summary now describes the 2014 conference proceedings, 95 papers and 13 sections. Replaced copied EPUB with publisher record. No free full-text claim; publisher lists a paid volume.
  https://www.peeters-leuven.be/detail.php?lang=en&search_key=9789042936720&series_number_str=273

## Read-only response audit

Checked all 468 unique file URLs using GET Range bytes=0-511, examining returned bytes rather than extensions. Results: 412 HTTP 401, 47 HTTP 206, 2 HTTP 200, 2 HTTP 404, 1 HTTP 403, 4 connection/TLS errors. All 278 EPUB URLs returned 401. All 412 Nile bucket URLs returned 401. Of successful responses, 46 had PDF magic bytes; three .pdf links returned HTML. No EPUB was verifiable. These are point-in-time responses, not rights determinations.

The 46 verified PDF formats are recorded separately in data/library_file_formats.json. Shared labels on Library and homepage name only verified formats. Others say Open linked file / فتح الملف المرتبط, preserving their links without asserting successful downloads. A generic label is not a repaired file. After replacing two bad mappings, 410 Nile bucket links remain unresolved; 276 .epub URLs remain, with no PDF-format claim.

## Systemic cause and unresolved scope

find_and_upload_calibre.py and fix_unknown_authors.py use character-presence overlap (sum characters of target title present anywhere in a directory name), allowing unrelated Calibre books to score highly. The upload script uses that match to select a PDF/EPUB, then changes metadata. fix_r2_urls.py also globally rewrites Kandaka bucket URLs to the separate Nile bucket. Do not run these legacy scripts pending replacement with exact title/identifier matching and reviewed manifests. Evidence strongly supports systematic risk, but does not establish every record's true author or file identity. Frequent implausible repeated author assignments warrant a record-by-record source audit; they were not guessed or bulk overwritten.

412 legacy cross-project mappings cannot be repaired by making Nile public or copying paid content. Recover original source provenance, verify title/author/identifier and lawful availability, then replace individual mappings. Eight explicit Unknown author records remain. No bulk deletion or automatic bucket substitution was performed.

## Claude handover — user-facing summary

The two confirmed false author credits and their English/Arabic descriptions are corrected. Their buttons now lead to the author's source and publisher record. Format labels are truthful: 46 confirmed PDFs are named; blocked or unverified files have a neutral label. The remaining legacy downloads need provenance research, not an access-control change. This task did not test bookstore purchases, alter the bookstore worker, or validate payment/webhook/fulfilment behavior; those checks remain separate work. Kandaka uses Hugo static pages, Git main → Netlify builds, plus existing news and scheduled rebuild workflows. No worker change was required for these library corrections.

## Phase 2 — historical recovery and explicit unavailable labels

This follow-up supersedes the earlier neutral-label counts above. It preserves all 542 records and all previous mappings in Git plus task-workspace backups and a before/after restoration manifest.

### Exact cause established from code and commit diffs

- 650150c (26 June 2026) ran a blanket replacement from Kandaka's public bucket hostname to the separate Nile bookstore hostname in both catalog and inventory. It was not a document-by-document identity or rights check. Inventory retained some original filenames, which made narrow historical recovery possible.
- 9ce6395 (7 July 2026) changed 375 source fields using the Calibre upload workflow. find_and_upload_calibre.py's matching function counts each character of the requested title if it occurs anywhere in a directory name, divides by title length, and accepts a score above 0.5. Character order, word order, title equality, author equality, ISBN/DOI and actual document contents are not checked. Repeated characters inflate scores; unrelated books can score 1.0. It then selects a .pdf/.epub from that directory and uploads it under the requested title's slug to the bookstore bucket. A plausible slug therefore does not prove file identity.
- cb5f393 (7 July 2026) changed 247 author fields via the same flawed character-presence matching against Calibre metadata. Among the 410 follow-up targets, 243 have historical Unknown credits later replaced by assigned names. This establishes the mechanism and affected scope; it does not determine every true author or prove the contents of inaccessible private objects. The private bookstore objects were not read.

### Historical recovery counts

- Traced all 37 catalog-changing commits and inventory history for the 410 remaining targets.
- 275 records retain earlier non-R2 source values, but every one is a homepage or author-page pointer, not an exact document URL; zero specific document URLs were recoverable from those catalog fields.
- 135 records have no historical non-R2 source in the traced catalog history.
- Inventory matches 407 of the 410 titles; 132 have historical filenames. Only 48 distinct exact historical Kandaka URLs were recovered across catalog and inventory: 27 records from catalog history, 43 from inventory history, with overlap.
- Of these 48 URLs, 20 respond with PDF signatures and 28 return 404. A surviving PDF signature is insufficient evidence of identity or completeness.
- Inspected all 20 surviving public files. Two could not be parsed because the retrieved byte stream was truncated (After Two Decades of Solitude; Osman Digna). Two are cookie-page captures (Water Infrastructure in Sudan; Water Resources in Sudan). Nile Basin Initiative is actually a 2008 water-harvesting report by Mamoun Ibrahim Dawelbeit. Sudan & Nubia 10 is a nine-page extract, not the full issue; Sudan & Nubia 23 is a three-page contents list. These seven were not restored. The other 13 still require exact edition and lawful-source review; five replacements below use verified original institutional sources instead of assuming blanket permission to republish copies.

### Five verified restorations

1. Foreign Trade Barriers: replaced both private mappings with USTR's original 2021 PDF. Actual first pages identify the Office of the U.S. Trade Representative and the 2021 National Trade Estimate Report. Corrected the English summary that had inaccurately described a Sudan-specific analysis; both summaries now describe the actual report.
   https://ustr.gov/sites/default/files/files/reports/2021/2021NTE.pdf
2. Sudan's Constitution of 2019: replaced private PDF/EPUB with the Constitute Project's freely readable historical constitutional text; translator International IDEA is identified. Removed the unsupported claim that the document includes analysis. This is a historical document, not advice about current law.
   https://www.constituteproject.org/constitution/Sudan_2019
3. The Land Cover Atlas of Sudan: replaced private mappings with FAO's original PDF. FAO's old stable URL redirects to its Open Knowledge repository; PDF signature and actual title confirmed. Bilingual summaries describe the 2012 atlas, without claiming current data.
   https://www.fao.org/3/a-be896e.pdf
4. The Sudan Handbook: replaced private mappings with RVI's original free digital PDF and publisher record. Corrected the credit to editors John Ryle, Justin Willis, Suliman Baldo and Jok Madut Jok, and dated this digital edition 2012 (print edition 2011). The original PDF explicitly grants CC BY-NC-ND 3.0 and the publisher explicitly offers free download; no copy was uploaded or redistributed.
   https://riftvalley.net/publication/sudan-handbook/
   https://riftvalley.net/wp-content/uploads/2018/06/RVI-The-Sudan-Handbook.pdf
5. Urban Waterways in Global Cities: replaced private mappings with the Chicago Council on Global Affairs' original report and PDF. Corrected the erroneous OECD credit and Arabic summary. Publisher's record and actual PDF identify the 2017 Mayors' Forum report.
   https://globalaffairs.org/research/report/urban-waterways-global-cities
   https://globalaffairs.org/sites/default/files/2021-06/report_urban_waterways_170622.pdf

All five replacement destinations returned HTTP 200/206. The four direct PDFs were signature-verified; the constitutional text is readable HTML. No inferred storage URL or fuzzy match was used. Inventory rows are synchronized, and original copied mappings remain in backups/history.

### Final intended counts and status behavior

- Records: 542 per language, unchanged.
- Remaining effective Nile mappings: 410 -> 405 in this follow-up (412 -> 405 across both repair phases).
- Verified PDF labels: 46 -> 50.
- Known unavailable file buttons: 408 (405 Nile 401 plus two other 404 and one other 403).
- File-access-unverified buttons: 7 (four connection/TLS failures and three HTML responses at .pdf URLs).
- Five restored records: four direct verified PDFs plus one HTML source record. Remaining file mappings are preserved and explicitly labeled unavailable/unverified; they are not represented as working downloads.

### Prevention and completion requirements

1. Retire the three unsafe legacy scripts from operational use: find_and_upload_calibre.py, fix_unknown_authors.py, fix_r2_urls.py. They were examined read-only in this follow-up; none was executed, and no storage setting changed.
2. Replace fuzzy character matching with an explicit reviewed manifest keyed by exact normalized title AND author plus edition/year or stable ISBN/DOI/repository identifier. Zero matches, multiple matches or missing evidence must stop the update, not choose the highest score.
3. Verify actual title/copyright pages and completeness; a filename, HTTP 200, PDF signature or content-type alone is insufficient. Cookie captures and contents lists must never be presented as complete works.
4. Prefer lawful original publisher/repository URLs; distinguish a source record from accessible full text. Record format, response status, verification date, source evidence and old mapping separately. Never globally substitute bucket names or use Nile paid objects to repair Kandaka.
5. Produce a dry-run before/after diff, back up catalog and inventory together, apply only reviewed rows, validate EN/AR rendered cards and source behavior, then deploy the narrow commit. Preserve articles, covers and publishing cadence.

Completing the remaining 405 requires record-level research and, for records with only generic sources or unknown provenance, original bibliography/source links or a verified source-document collection. No permission to make a bucket public is needed or sought. A user choice is needed only for unresolved records that have no lawful public full text: keep an accurately labeled publisher/abstract record, or supply an authorized original source for linking. Existing records remain visible in the meantime.

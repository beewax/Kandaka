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

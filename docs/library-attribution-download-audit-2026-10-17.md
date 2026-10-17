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

## Phase 3 — two reviewed exact source replacements, 17 October 2026

Reviewed input: Library libfile_69947ec436448191980f807f7014c2c8, kandaka-reviewed-source-replacements-2026-10-17.json. All ten review rows were read; only the two ready rows were applied. Their frozen IDs, baseline positions, current English titles, effective downloads and inactive EPUB fallbacks matched the live source baseline before editing.

- KND-22C8C749DE5A5B4A, Sudan 2022 Human Rights Report: replaced the broken PDF and corrupt inactive EPUB with https://www.ecoi.net/en/document/2089142.html . Label: Read report / قراءة التقرير. U.S. Department of State, publication 20 March 2023, reporting year 2022. Added bilingual citation and description, HTML format and repository identifier 2089142. The complete executive summary and Sections 1–7 are present in the public institutional copy. A fresh ordinary request returned HTTP 200 with exact title, final section and date. No PDF-layout claim.
- KND-50AFD7FF76A66035, Trade & Wadis System in Muslim Sudan: replaced the broken PDF and corrupt inactive EPUB with stable https://hdl.handle.net/1956/3994 . Label: View repository / PDF / عرض المصدر وملف PDF. Verified full author Intisar Soghayroun Elzein Soghayroun, Fountain Publishers, Kampala, 2010, ISBN 9789970250059. Added bilingual citation/description and explicit all-rights-reserved link-only note. Fresh public JSON metadata with Accept: application/json returned HTTP 200, exact title/author/2010/ISBN, PUBLISHED, OpenFile application/pdf 7,258,183 bytes and allowed download/read-metadata. Stable handle returns 200 to the exact NVA record. Reviewed manifest verifies complete 140-page PDF with bibliography, appendices and index; no copyrighted file was rehosted, copied to Library or placed in the catalog as a temporary URL.

Only these two records and inventory rows changed. Small source-label overrides were added to the Library and homepage templates; other labels retain their prior defaults. The eight held records remain unchanged, including any metadata-only correction. Both original mappings remain in Git and phase-3 backups.

New remaining counts: 405 -> 403 unresolved Nile mappings. 542 records per language preserved; 50 verified PDF labels unchanged; 406 known-unavailable file links (403 Nile 401 plus three other failures); seven unverified links unchanged. Two new source/read buttons point to institutional full-text sources rather than direct copied downloads.

The eight held records and precise next needs:
1. AfDB After Two Decades of Solitude: obtain complete permitted publisher file and inspect imprint/year and terminal pages; current file access blocked/truncated evidence insufficient.
2. Old Dongola Kom A 2005: verify ordinary public live complete article; publisher/repository access challenges remain. Independently verified citation is Godlewski, 2007, PAM 17, 287–299; no link or metadata change applied here.
3. Agricultural Potential of Sudan: verify successful full retrieval from exact publisher or IGAD source, retaining all-rights-reserved/link-only scope.
4. Water Resources of the Sudan: complete lawful public report and all 26 printed pages plus covers; IRC access restriction must not be bypassed.
5. Upper Nubian Vernacular Architecture: exact full one-page author/institution poster and provenance/rights; no current link restoration or OCR-only author correction.
6. Sudan & Nubia 23: complete verified issue content or a separately approved accurately labeled issue/index record; the contents/ancillary files are not a whole issue.
7. Sudan & Nubia 10: complete publisher content or separately approved issue/index record; the historical nine-page extract is insufficient.
8. Sorghum Value Chain Analysis: migrated government/NABC record or lawful complete copy, actual author/commissioner, imprint date and all 42 pages. FAO attribution is unsupported; no new author/year guessed.

No CAPTCHA/access restriction was bypassed. No private object was fetched. No storage setting, article, cover or deployment cadence was changed.

## Phase 4 — next reviewed batch, 17 October 2026

Reviewed all 20 rows in Library libfile_95273047f5748191b82ca7067de98d17 v0 against current commit 10e605b242ca50784ad0994e7bc387a9bdae935f. All 15 ready IDs, frozen positions, current titles and old source/download URLs matched; no concurrent catalog conflict was found.

Fresh ordinary public access checks passed for 11 of 15 destinations. World Bank rejected Range probes (416) but ordinary GET returned 200 with PDF signatures, so those exact approved URLs passed. Four proposed replacements failed current normal GET: IMF Fiscal Adjustment, IMF ECF 2021 and IMF Selected Issues 2012 each returned 403; UN World Economic Situation and Prospects 2020 returned an empty 202 response. Those four were skipped and remain unchanged/unavailable. No anti-bot, CAPTCHA, authentication or access restriction was bypassed. Reviewed prior successful downloads remain evidence, but are not represented as fresh successful checks.

Applied only these eleven reviewed stable IDs, with exact verified author/year/citation and identifiers, bilingual source labels and metadata, removal of each old source/download fallback, synchronized CSV inventory, and source-record versus direct-PDF distinctions:
- KND-9A1B2D9998825958 — Distortions to Agricultural Incentives in Sudan: World Bank main report, Working Paper 44, December 2007 (corrected from 2008), Hamid Faki and Abdelmoneim Taha; direct official PDF.
- KND-A960C1F55EE2CF79 — Sudan's Infrastructure: A Continental Perspective: Rupa Ranganathan and Cecilia M. Briceño-Garmendia, 2011, WPS5815 (not South Sudan WPS5814); direct World Bank PDF.
- KND-8F66588475CBD3F6 — Assessing Regional Integration in Africa IV: 2010, joint ECA/African Union/AfDB authorship; official archive record with full PDF.
- KND-088CD6F1F98ECD3D — Sudan E-Agriculture Strategy and Action Plan 2018–2022: Ministry of Agriculture and Forests, December 2017; ECOLEX institutional record. Plan period is not publication year.
- KND-A61FBF7E0B785D6E — Sudan Human Rights Report 2017: USDOS, published 20 April 2018, reporting year 2017; full HTML at ecoi.net, document 1430180.
- KND-6FAEB2F56B88B08D — Continuation of National Emergency 2023: Joseph R. Biden Jr., official notice (not executive order), signed 31 October and published 2 November 2023, FR Doc 2023-24364; official GovInfo PDF.
- KND-B7BB939ADE796ED8 — From Subsidy to Sustainability: World Bank, 2019, DOI 10.1596/33702; stable publisher handle with full PDF. Conflicting June day-level dates were not collapsed into a guessed publication date.
- KND-0A0DAD78D94B871B — Sudan Social Safety Net Assessment: five title-page authors, 2014, Discussion Paper 1415, DOI 10.1596/20054; publisher handle with full PDF.
- KND-37C239BA072816A0 — Water Scarcity and Food Security along the Nile: Terje Oestigaard, 2012, Current African Issues 49, ISBN 9789171067227; persistent institutional URN record with full PDF and full subtitle retained in citation/title_full.
- KND-B476522629AC34C5 — Sudanese Universities as Sites of Social Transformation: Linda S. Bishai, 2008, USIP Special Report 203; ETH institutional PDF explicitly labeled as an institutional copy.
- KND-FAFF0C435C52C683 — Corruption and Anti-Corruption in Sudan: corrected author from Kaunain Rahman to Maira Martini, 2012, U4 Expert Answer 342, 22 August; publisher record with full PDF. 2021 webpage update is not publication year.

All five originally held records remain unchanged: Investment Policy Review (live full text unavailable); first NDC (edition and live text unverified); Country Study (live full text unverified); 1998 Constitution (substantive Article 60 omitted from accessible translation); 2005 draft Constitution (exact draft edition not established). No metadata-only correction was applied to a held/skipped record. In particular, the incomplete 1998 translation was not restored.

Counts after this partial batch: 403 -> 392 unresolved Nile mappings; all 542 records preserved; verified direct PDF format mappings 50 -> 54; known unavailable buttons 406 -> 395 (392 Nile plus three other failures); seven unverified file links unchanged. Direct PDFs use their reviewed labels, including Read official notice (PDF) and Read PDF (institutional copy), rather than treating every PDF as an identical download. No source files were rehosted or uploaded to Library.

The four newly skipped sources require a permitted successful ordinary public response for the exact reviewed destination before a future restoration. The five originally held cases require their manifest-specific completeness/edition/source evidence. Full before/after and HTTP evidence are preserved in phase4-applied-manifest.json, phase4-source-link-checks.json, phase4-skipped-checks.json and phase-4 backups in the task workspace; these contain no secrets.

Validation scope note: an unreviewed ASCII-hyphen alias, Sudan E-Agriculture Strategy and Action Plan 2018-2022, still references the same obsolete EPUB that had been an inactive fallback on the reviewed en-dash-title record. It remains unchanged under its separate frozen ID. Old-URL removal is asserted on each repaired card, not globally across unrelated records. This is a follow-up reconstruction lead, not permission to merge or edit the alias.

## Phase 5 — reviewed next 30, 17 October 2026

Input: Library libfile_7fff88e4d0d4819187a9532fd2c4e91c version 1, read in full. Reviewed 30 records (20 ready, 10 held) against current source commit 5dbfbc3f822c7160ab990a7f1dd19467832b4077. All 20 ready frozen IDs, positions, exact current titles, effective old URLs and source/download fields matched. No concurrent edits or catalog conflicts were found.

Fresh ordinary access passed for 17 of 20 ready destinations. Each of those 17 full source files was independently fetched in memory, parsed as PDF, checked for exact page count and compared by SHA-256 with the visually/page-by-page reviewed original; all 17 hashes and counts matched. No source-file bytes were rehosted or uploaded to Library. The three newly skipped cases are Governance in Africa (AfDB PDF, 403), Sudan-Darfur Infrastructure Development Report (AfDB record, 403), and Controversy of Exchange Rate Devaluation (AgEcon record, 202). They remain unchanged pending successful permitted public access. No retries on restricted routes or access bypasses were attempted.

Applied 17 exact external source replacements only, with synchronized inventory, removal of old active and inactive copied-file mappings from each repaired record, verified bibliographic citations/identifiers and bilingual labels:
- Sudan Country Economic Memorandum: 2015 main report, 226 pages; September 2016 public disclosure is separate from report date.
- Sudan Diagnostic Trade Integration Study: the complete December 2008 non-oil exports study, 156 pages; no identifiers from the different 2014 update.
- Doing Business 2017 Sudan profile: 98 pages; citation/edition year 2017, publisher document year 2016 separately retained.
- Doing Business 2020 Sudan profile: 65 pages; publication/citation year 2019, edition year 2020; not the global report or South Sudan.
- World Bank and Gezira Scheme: Salman M. A. Salman, 2010, 55 pages; full report including Gezira Act annex.
- Sudan Railways appraisal: IBRD, 1958, TO-180a, 50 pages including map; old cover RESTRICTED marking does not override later official Public/Disclosed metadata.
- Arab Region SDG Index 2019: six verified personal authors; publisher record with complete 159-page file.
- African Integrated High Speed Railway Network note: corporate author African Union; leave publication year unset and cite n.d.; PDF creation date is not publication evidence.
- Innovative Financing for Africa: ECA, 2015, edited by Abdalla Hamdok; complete 206-page publisher book, editor credited visibly and in metadata.
- Skills Development in Sudan: four verified authors, first published 2014; outer-cover 2013 preserved as a distinct source-date caveat; complete 67-page file.
- Lost Nubia: John A. Larson, 2006, complete 128-page publisher scan; corrected unrelated former author credit.
- Karanog: The Town: C. Leonard Woolley, 1911, complete 147-page NYU scan with all 30 plates; corrected unrelated former author credit.
- Meroitic Inscriptions of Shablul and Karanog: F. Ll. Griffith, 1911, complete 297-page Harvard/Google historical scan. All printed text 1–181 and plates I–XXX present; twelve repeated text pages and ten extra plate images retained. Both bilingual descriptions explicitly disclose duplicated leaves/images. No cleaned/new edition is claimed.
- Determinants of Inflation: Kabbashi M. Suliman, 2012, AERC Paper 243, 54 pages. Publisher PDF retains preliminary matter after the main text; this ordering is disclosed in both languages, not silently reformatted.
- Does Foreign Aid Promote Growth: three title-page authors, ERF Working Paper 1251, November 2018, 28 pages; no unprinted Ali suffix added to first author.
- Sudan's Challenges and Opportunities: four-author Policy Brief 99, November 2022, 28 pages, explicitly distinct from the longer seven-author report.
- Gezira Scheme Perspectives: Ahmed Mohamed Eldaw, 2004, German Development Institute report 2/2004, 82 pages; removed unsupported FAO authorship/publisher implication.

All ten originally held records remain unchanged: CBD/NBSAP edition ambiguity; Bad Company (403); Consolidating Transition (403); Infrastructure Sector Overview (403); Wasta (403); Trade Integrity (403/incomplete evidence); Nubia Ancient Kingdoms catalogue (no verified public full edition); Africa in Antiquity (both volumes/access/completeness unresolved); Karanog Cemetery (both complete volumes must be clearly represented by two verified labeled links); Food-Poverty-Vulnerability Sudan report (no verified complete source). No partial Cemetery volume, exhibition substitute or summary was restored.

New counts: 392 -> 375 unresolved Nile mappings; all 542 records preserved. Verified direct PDF format mappings 54 -> 65. Known unavailable card labels 395 -> 378 (375 Nile plus three other failures); seven unverified links unchanged. Six new record pages link complete source PDFs and eleven new links are direct verified PDFs. Zero speculative matches, merges, deletions, private-object reads, rehosting or Nile theme changes.

Independent source/byte evidence: phase5-source-checks.json and phase5-content-checks.json. Before/after records: phase5-applied-manifest.json; original mappings preserved in Git and library-repair-phase5-backup. Source review is link-only; public delivery is not treated as general redistribution permission.

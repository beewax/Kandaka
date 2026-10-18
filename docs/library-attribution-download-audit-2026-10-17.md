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

## Phase 6 - approved research round 4

13 of 22 proposed repairs passed fresh ordinary public access and full-content checks. The 18 originally held records remain unchanged. Khartoum uses the user-confirmed author-uploaded ResearchGate landing page. Parent independently inspected the complete64-page2009 PDF; independent web landing confirms citation/fulltext. Local urllib403 remains documented as access variability; blocked publisher route not retried. No bypass or rehosting occurred.

Catalog records:542 before and after. Unresolved Nile mappings:375 →362. Known-unavailable card labels:378 →365. Seven unverified cards remain. Only13 selected catalog objects and their inventory entries changed; editorial articles, covers, dates and deployment cadence were preserved.

Every PDF applied matched the reviewed SHA-256 and page count; the two HTML articles/reports passed title/byline and closing-section checks. Fulltext labels distinguish the water-management chapter from the whole book and HTML from PDF. Source rights remain with their holders.

### Applied exact source destinations

- KND-A2FA73154FED40C8 — Remote Sensing to Monitor Impact of Conflict on Agriculture — Mercy Corps (2023). Record/source: https://www.prosperglobal.org/sites/default/files/2023-10/Sudan-remote-sensing-impact-of-conflict-on-agriculture-paper-1-august-2023_0.pdf ; verified full text: https://www.prosperglobal.org/sites/default/files/2023-10/Sudan-remote-sensing-impact-of-conflict-on-agriculture-paper-1-august-2023_0.pdf
- KND-08BD8385A4575AE2 — On the Road to Recovery: How Sudan Is Saving Its Water Sector — Noosha Tayebi (2021). Record/source: https://blogs.worldbank.org/en/water/road-recovery-how-sudan-saving-its-water-sector ; complete HTML.
- KND-61D59C8E534EFC11 — Sudan's Challenges and Opportunities: A Renaissance Project for Sudan — Ibrahim Elbadawi; Abdelrazig Elbashir; Abdelrahman Osman; Amir Hamid Elobaid; Elfatih Eltahir; Alzaki Alhelo; Kabbashi M. Suliman (2022). Record/source: https://erf.org.eg/publications/sudans-challenges-and-opportunities-a-renaissance-project-for-sudan/ ; verified full text: https://erf.org.eg/app/uploads/2022/07/1659257696_282_6382995_prr40.pdf
- KND-01DB44640817B3F0 — Black Gold for Blue Gold: Sudan's Oil, Ethiopia's Water and Regional Integration — Harry Verhoeven (2011). Record/source: https://www.chathamhouse.org/sites/default/files/19482_0611bp_verhoeven.pdf ; verified full text: https://www.chathamhouse.org/sites/default/files/19482_0611bp_verhoeven.pdf
- KND-07BB90F1E900BCD8 — Country Reports on Human Rights Practices for 2017: Sudan — U.S. Department of State (2018). Record/source: https://www.ecoi.net/en/document/1430180.html ; complete HTML.
- KND-0936AB37BD11EE07 — From Subsidy to Sustainability: Sudan's Electricity Sector — World Bank (2019). Record/source: https://hdl.handle.net/10986/33702 ; verified full text: https://openknowledge.worldbank.org/bitstreams/142c0f15-20d8-54e6-a92c-bfbdbccbaccb/download
- KND-780449DDB0EC5B48 — Agricultural Productivity and Poverty in Rural Sudan — Haseeb Ali; Alvin Etang Ndip; Sering Touray; Habtamu Fuje (2020). Record/source: https://openknowledge.worldbank.org/handle/10986/36105 ; verified full text: https://documents1.worldbank.org/curated/en/345181628489090079/pdf/Agricultural-Productivity-and-Poverty-in-Rural-Sudan.pdf
- KND-2F4DF2A818689EAC — Water Management by Divine Benevolence: Meroitic Pastoral Reservoirs Along the Nile — Petra Weschenfelder (2012). Record/source: https://pueaa.unam.mx/uploads/materials/Water_management.pdf?v=1660144492 ; verified full text: https://pueaa.unam.mx/uploads/materials/Water_management.pdf?v=1660144492
- KND-1D9C67B77A6E227A — The Arab Region SDG Index and Dashboards Report 2019 — Mari Luomi; Grayson Fuller; Lara Dahan; Karina Lisboa Båsund; Eve de la Mothe Karoubi; Guillaume Lafortune (2019). Record/source: https://www.sustainabledevelopment.report/reports/2019-arab-region-sdg-index-and-dashboards-report/ ; verified full text: https://s3.amazonaws.com/sustainabledevelopment.report/2019/2019_arab_region_index_and_dashboards.pdf
- KND-94FF3C3654B5633D — Village Environmental Management Plans for Dungonab Bay and Mukkawar Island — Paul Harrison; Melita Samoilys (2007). Record/source: https://www.sudanmarineparks.info/about-us/publications-reports/ ; verified full text: https://sudanmarineparks.info/wp-content/uploads/2026/09/vemps-2007.pdf
- KND-37EE0F06C09F56CC — Lost Nubia: A Centennial Exhibit of Photographs — John A. Larson (2006). Record/source: https://isac.uchicago.edu/publications/lost-nubia-centennial-exhibit-photographs-1905-1907-egyptian-expedition-university ; verified full text: https://isac-assets.s3.amazonaws.com/isac-publications/oimp24.pdf?VersionId=qfuDLHg1dtTdynplzt7As1MQ6pFO2Ca1
- KND-AF541F715B9DF7F3 — The Gezira Irrigation Scheme in Sudan: Objectives, Design, and Performance — Hervé Plusquellec (1990). Record/source: https://documents1.worldbank.org/curated/en/377141468778504847/pdf/multi-page.pdf ; verified full text: https://documents1.worldbank.org/curated/en/377141468778504847/pdf/multi-page.pdf
- KND-C7E148B25A61F1A9 — Urban Sector Studies and Capacity Building — Fernando Murillo; Salah Mohamoud Osman; Hag Adam H. El Tahir; Abdalla Kafeel; Khadeiga M. Osman; Burhan El Ghazali; Abdel Rahman Mustafa (2009). Record/source: https://www.researchgate.net/publication/353620865_Urban_Sector_Studies_and_Capacity_Building_for_Khartoum_State ; complete HTML.

### Proposed candidates held after fresh checks

- KND-B1323B4D504C9D1F — Good Governance and the Policy Challenge: The African Development Bank Perspective: Ordinary public HTTP failure; no bypass (HTTP 403)
- KND-8D5EB40494210D26 — Trends in the Sudanese Economy Q1 2014: Ordinary public HTTP failure; no bypass (HTTP 403)
- KND-D2DCD09AFAF55609 — Sudan: A Case for Structural Adjustment Policies: Full content/hash/page/HTML validation did not match reviewed original
- KND-684CA25641427701 — The Horn of Africa–Persian Gulf Nexus: Inter-Regional Dynamics in Geopolitical Flux: Ordinary public HTTP failure; no bypass (HTTP 500)
- KND-45255609C5A64049 — Laws of the New Sudan: The Penal Code 2003: Ordinary public HTTP failure; no bypass (HTTP 403)
- KND-538B2E8C7B2B5221 — Rethinking Sudan After Southern Secession: Ordinary public HTTP failure; no bypass (HTTP 403)
- KND-4309968997148F7B — Sudan Fools Gold Report: Ordinary public HTTP failure; no bypass (HTTP 403)
- KND-CB5FDEB48DF0F85D — Spinning in Meroitic Sudan: Textile Implements from Abu Geili: Ordinary public HTTP failure; no bypass (HTTP 403)
- KND-C6397BD36FD08DFB — Sudan E-Agriculture Strategy and Action Plan 2018-2022: TimeoutError: The read operation timed out

Validation/deployment evidence is recorded in the cumulative handover after production verification. Purchases and Worker payment delivery are outside this library-only batch; no purchase test is claimed.

## Phase 7 - approved research round 5

14 of19 approved candidates passed fresh ordinary public access and content checks. Five failed and21 originally held records remain unchanged. All542 catalog records preserved. Unresolved Nile mappings362 →348; known-unavailable labels365 →351; seven unverified remain.82 direct PDF URLs are byte-verified.

Seven PDFs independently matched reviewed SHA-256 and page count; seven full HTML articles passed author/date/closing-section checks. Taha is the undated Al-Fikra English Fifth Edition: year unset,211-page complete PDF, no Syracuse1987 metadata imported. Manzo is explicitly an article within a complete issue.

Concurrent automatic news commit1bec9b2 was fast-forwarded before edits; its articles and feed data were preserved. Only14 approved catalog objects, synchronized inventory entries, format/status maps and this audit note changed. No rehosting, storage controls, paid content, Worker, covers, schedules or purchases changed/tested.

### Applied exact sources and citations

- KND-016ADA1A14B03C48 — West and East Africa Linked by OIC Rail Project — Arab News. 2017. “West and East Africa linked by OIC rail project.” 24 November; updated 25 November. Source: https://www.arabnews.com/world/west-and-east-africa-linked-by-oic-rail-project-1198586 ; full HTML.
- KND-A4F72DAF27CB2F97 — It is Possible to Increase by Over Thirty Per Cent the Nile Water Availability — F. Lemperière. January 2011. It is possible to increase by over thirty per cent the Nile water availability. HydroCoop; posted 16 August 2013. Source: https://www.hydrocoop.org/nile-water-availability-increase/ ; full HTML.
- KND-08391193B1C2AFE4 — Solar Energy Potential in the Sudan — El Zein, Musadag. 2017. Solar Energy potential in The Sudan. Master thesis in Sustainable Development 2017/16. Uppsala University, Department of Earth Sciences. 50 printed pages plus front matter. Source: https://www.diva-portal.org/smash/get/diva2%3A1110877/ATTACHMENT01.pdf ; fulltext: https://www.diva-portal.org/smash/get/diva2%3A1110877/ATTACHMENT01.pdf
- KND-678B5E77208E3016 — The Long-run Development Impacts of Agricultural Productivity Gains: Evidence from Irrigation Canals in India — Sam Asher; Alison Campion; Douglas Gollin; Paul Novosad. 2023. The Long-Run Development Impacts of Agricultural Productivity Gains: Evidence from Irrigation Canals in India. Source: https://thedocs.worldbank.org/en/doc/f8ad0f48d265c066d19f7a5c0f62f854-0050022023/the-long-run-development-impacts-of-agricultural-productivity-gains-evidence-from-irrigation-canals-in-india ; fulltext: https://thedocs.worldbank.org/en/doc/f8ad0f48d265c066d19f7a5c0f62f854-0050022023/original/acgncanals202301.pdf
- KND-C1422C7CD2015F41 — Partnerships, Special Economic Zones, New CSR Essential for Africa's Economic Diversification — United Nations Economic Commission for Africa. 2021. Partnerships, special economic zones, new CSR essential for Africa’s economic diversification. Source: https://www.uneca.org/stories/partnerships%2C-special-economic-zones%2C-new-csr-essential-for-africa%E2%80%99s-economic ; full HTML.
- KND-08DFD86AB93A71E6 — Can Sudan's New Government Solve the Annual Mass Flooding Crisis? — Hamad, Khattab. 2020. “Can Sudan’s new government solve the annual mass flooding crisis?” Global Voices, 6 August. Source: https://globalvoices.org/2020/08/06/can-sudans-new-government-solve-the-annual-mass-flooding-crisis/ ; full HTML.
- KND-25E6020691876A03 — Archaeological and Architectural Evidence of Social Change in 13th–17th Century Dongola — Włodzimierz Godlewski. 2018. Archaeological and architectural evidence of social change in 13th–17th century Dongola. Source: https://pam-journal.pl/issues/27-vol-27-issue-1-regular-issue/archaeological-and-architectural-evidence-of-social-change-in-13th-17th-century-dongola ; fulltext: https://api.publisphere.edu.pl/open/journal_article_files/019cd9b2-34b4-732e-badd-6b68522e5ffc/download?v=1
- KND-9091CA1748980091 — From the Sea to the Deserts and Back: New Research in Eastern Sudan — Andrea Manzo. 2012. From the sea to the deserts and back: New research in Eastern Sudan. Source: https://britishmuseum.iro.bl.uk/entities/publication/5dfe948f-dd37-4ce8-bdc4-e037f8f438fc ; fulltext: https://britishmuseum.iro.bl.uk/bitstreams/f71afbc5-7b28-4c62-98b6-8a30883a11fa/download#page=15
- KND-7EA9E9601FFE0405 — Sudan's Economic Nightmare — MERIP — Tim Niblock. 1985. Sudan’s Economic Nightmare. Source: https://www.merip.org/1985/09/sudans-economic-nightmare/ ; full HTML.
- KND-5C272B721BA702A2 — Sudan's Normalization with Israel: In Whose Interests? — El-Gizouli, Magdi. 2021. Sudan’s Normalization with Israel: In Whose Interests? Bawader / Commentary. Arab Reform Initiative, 17 August. Source: https://www.arab-reform.net/publication/sudans-normalization-with-israel-in-whose-interests/ ; fulltext: https://www.arab-reform.net/wp-content/uploads/pdf/Arab_Reform_Initiative_en_sudans-normalization-with-israel-in-whose-interests_19528.pdf?ver=0792252d8ec21c34c0b059ccadc7df6d
- KND-F3F4056FAC44D4DC — How Sudan is Saving its Water Sector — Tayebi, Noosha. 2021. “On the road to recovery: How Sudan is saving its water sector.” World Bank, The Water Blog, 29 September. Source: https://blogs.worldbank.org/en/water/road-recovery-how-sudan-saving-its-water-sector ; full HTML.
- KND-FBF1FFF7D6E4566B — The Second Message of Islam — Taha, Mahmoud Muhammad. n.d. The Second Message of Islam. Fifth Edition, English translation published online by Al-Fikra. Source: https://www.alfikra.org/book_view_e.php?book_id=310 ; fulltext: https://www.alfikra.org/books/bk310.pdf
- KND-2397B450C8655EB5 — The Candaces of Meroe — Joshua J. Mark. 2018. The Candaces of Meroe. Source: https://www.worldhistory.org/The_Candaces_of_Meroe/ ; full HTML.
- KND-FC4780F3CD9B0FDB — The Gold Boom in Sudan: Challenges and Opportunities for National Economic Players — Raphaëlle Chevrillon-Guibert. 2016. The Gold Boom in Sudan: Challenges and Opportunities for National Players. Source: https://horizon.documentation.ird.fr/exl-doc/pleins_textes/divers20-06/010079190.pdf ; fulltext: https://horizon.documentation.ird.fr/exl-doc/pleins_textes/divers20-06/010079190.pdf

### Fresh failures held unchanged

- KND-45C9849EE96E6F95 — Nile Basin Farming Systems and Productivity: Stable source did not return200; HTTP 202
- KND-D207E49C7C33C8AE — Nile Water and Agriculture: Past, Present and Future: Stable source did not return200; HTTP 202
- KND-D9EC311BAA51A9FD — Cotton in Ancient Sudan and Nubia: Archaeological Sources: Ordinary public HTTP failure; no bypass; HTTP 403
- KND-AB37E01F7467A8CF — A New Protective Shelter for the Royal Baths at Meroe: Full content/hash/page/HTML validation did not match reviewed original; HTTP 200 (archive returned9642-byte HTML, not the reviewed15-page PDF)
- KND-78EF13B8A0845C7D — Sudan's Removal from the State Sponsors of Terrorism List: Ordinary public HTTP failure; no bypass; HTTP 403

No blocked-route retries, challenge solving or bypass used. Cotton was not applied because fresh public access returned403 despite earlier research success. Both Nile chapter landing pages returned202; CRS403; Royal Baths archive returnedHTML. Deployment/live evidence follows in the cumulative handover.

## Phase 8 - continuing approved research round 6

10 of13 proposed candidates passed final checks;3 failed fresh public access/content checks and27 audit-held records remain unchanged. All542 records preserved. Unresolved Nile mappings348 →338; known-unavailable labels351 →341; seven unverified remain. Format map:91 verified PDF URLs and1 verified EPUB URL.

Manifest SHA-256 independently matched dde40ad7c8aa0276d91124934eb1afa683cfb284027ee592124e30118f0c0cb9. Nine PDFs matched reviewed SHA-256 and page counts; Fire and Sword EPUB matched hash and passed ZIP/mimetype integrity. PDF parser emitted recoverable offset warnings for the historical facsimile, which still parsed all528 pages and matched the reviewed bytes. No repaired/reformatted edition is claimed.

Piye is the complete chapter printed105–122/PDF115–132 inside the278-page full volume. Gezira is the complete nine-page chapter printed175–183, including the intentional blank divider page176. Fire and Sword uses the illustrated EPUB download label, with Gutenberg HTML availability described. The1998 constitution is historical, all140 articles present, with PartII after PartIII; translation status is unverified and no current-law assertion made. The entry-into-force date is stored separately.

Only10 approved catalog objects, synchronized inventory entries, format/status maps and this audit note changed. No unrelated articles, covers, cadence, paid content, Worker, storage settings or purchase flows changed. No source rehosting or access bypass.

### Applied exact source destinations

- KND-4752035B4CE5FBC8 — Piye's Conquest of Egypt and the Making of a Great Event — Martin Fitzenreiter. 2018. Piye’s Conquest of Egypt (about 727 B.C.E.) and the Making of a Great Event (about 727 B.C.E. and beyond). Source: https://www.ibaes.de/ibaes20/publikation.html ; verified PDF: https://www.ibaes.de/ibaes20/publikation/ibaes20_publikation-small.pdf#page=115
- KND-EE4AA037F3B68892 — A Tropical Dependency: An Outline of the Ancient History of the Western Sudan — Flora L. Shaw (Lady Lugard). 1905. A Tropical Dependency: An Outline of the Ancient History of the Western Soudan with an Account of the Modern Settlement of Northern Nigeria. Source: https://commons.wikimedia.org/wiki/File:A_tropical_dependency_-_an_outline_of_the_ancient_history_of_the_western_Sudan_with_an_account_of_the_modern_settlement_of_northern_Nigeria_(IA_tropicaldependen00luga).pdf ; verified PDF: https://upload.wikimedia.org/wikipedia/commons/3/3f/A_tropical_dependency_-_an_outline_of_the_ancient_history_of_the_western_Sudan_with_an_account_of_the_modern_settlement_of_northern_Nigeria_%28IA_tropicaldependen00luga%29.pdf
- KND-C187AE4AFB885A00 — Sudan's Constitution of 1998 — Republic of Sudan. 1998. The Constitution of the Republic of the Sudan 1998. Source: https://www.icnl.org/research/library/sudan_theconstitution/ ; verified PDF: https://www.icnl.org/wp-content/uploads/Sudan_THECONSTITUTION.pdf
- KND-6C7DFA4B1E99A8E4 — Current Status of Agriculture and Future Challenges in Sudan — Farida Mahgoub. 2014. Current Status of Agriculture and Future Challenges in Sudan. Source: https://nai.diva-portal.org/smash/record.jsf?pid=diva2:712485 ; verified PDF: https://nai.diva-portal.org/smash/get/diva2%3A712485/fulltext01.pdf
- KND-E15818F0CBB5A611 — Fire and Sword in the Sudan — Rudolf C. Slatin Pasha. 1896. Fire and Sword in the Sudan: A Personal Narrative of Fighting and Serving the Dervishes 1879–1895. Source: https://www.gutenberg.org/ebooks/41035 ; verified EPUB: https://www.gutenberg.org/ebooks/41035.epub3.images
- KND-0D39042C71466BBE — 3D Acquisition of Archaeological Structures at Wad Ben Naga — Alexander Gatzsche. 2013. Case study of an open source application for 3D acquisition of archaeological structures at the archaeological site Wad Ben Naga. Source: https://www.sag-online.de/wp-content/uploads/2017/01/Gatzsche2013_3DAcquisitionStructuresWadBenNaga_MittSAG24.pdf ; verified PDF: https://www.sag-online.de/wp-content/uploads/2017/01/Gatzsche2013_3DAcquisitionStructuresWadBenNaga_MittSAG24.pdf
- KND-DC3D4E7B2E44A29B — Eastern Sudan in Its Setting: Archaeology of a Region Far From the Nile Valley — Andrea Manzo. 2017. Eastern Sudan in its Setting: The archaeology of a region far from the Nile Valley. Source: https://bcp.archaeopress.com/Archaeopress/Products/9781784915582 ; verified PDF: https://bcp.archaeopress.com/Archaeopress/download/9781784915582
- KND-62FE524488C7186F — Taking the First Step to Facilitate Trade in Sudan — Ali Giddo Adam. 2017. Taking the First Step to Facilitate Trade in Sudan: Setting Up a National Committee on Trade Facilitation. Source: https://documents1.worldbank.org/curated/en/483531488783258055/pdf/113165-BRI-IFC-SMART-LESSONS-BRIEF-PUBLIC-20170302T111010-2017-Sudan-Trade-A.pdf ; verified PDF: https://documents1.worldbank.org/curated/en/483531488783258055/pdf/113165-BRI-IFC-SMART-LESSONS-BRIEF-PUBLIC-20170302T111010-2017-Sudan-Trade-A.pdf
- KND-FA01FD1E2B5D4C71 — Technical Efficiency of On-Farm Water Use in Sudan's Gezira Scheme — Abbas Elsir El Amin; Kamel Shideed; A. M. Abdelwahab; S. Farouk. 2011. Measurement and sources of technical efficiency of on-farm water use in the Sudan’s Gezira scheme. Source: https://repo.mel.cgiar.org/items/26b44058-a199-4518-9d6f-dda6162a2ab9 ; verified PDF: https://mel.cgiar.org/reporting/download/hash/2tScqBmK
- KND-7EF04C6A82599FDF — Clothing the Elite: Textile Production and Consumption in Ancient Sudan and Nubia — Elsa Yvanez. 2018. Clothing the Elite? Patterns of Textile Production and Consumption in Ancient Sudan and Nubia. Source: https://rcin.org.pl/iae/dlibra/publication/87895/edition/67584?language=pl ; verified PDF: https://rcin.org.pl/Content/67584/PDF/WA308_87895_PIII348_Clothing-the-Elite_I.pdf

### Fresh failures held unchanged

- KND-B37D7D457EBF4ADA — Strangers Everywhere: Exclusion, Identity and the Future of Nubians in Northern Uganda: Ordinary public HTTP failure; no bypass; HTTP 403
- KND-D1972D04A4734C6C — Nubia Bibliography Up to 2000: Ordinary public HTTP failure; no bypass; HTTP 403
- KND-A4DBFC9DC132C0DE — Seventy Years of Pottery Studies in Sudanese Prehistoric Archaeology: Full file bytes/hash/pages/EPUB integrity did not match reviewed original; HTTP 200 ; response was not the reviewed publisher PDF

## Phase 9 - continuing approved research round 7

4 of8 proposed candidates passed final checks;4 failed fresh secure access checks and32 audit-held records remain unchanged. All542 records and both out-of-scope held records preserved. Unresolved Nile mappings338 →334; known-unavailable labels341 →337; seven unverified remain. Format map:95 verified PDF URLs and1 verified EPUB URL.

Manifest SHA-256 independently matched79cf76dec23981847d4102ec26307e104a381148d0414f47d62efd0c953d2787. Four full PDFs independently matched reviewed SHA-256 and page counts. Red Sea is explicitly the complete42-page arXiv v3 preprint,2020, distinct from the initial2019 submission and later journal edition. Canal is explicitly the complete11-page technical booklet/slides. No historical bucket copies restored.

Only4 approved catalog objects,4 exact CSV rows, format/status maps and this audit note changed. No unrelated articles, covers, publication cadence, paid content, Worker, storage settings, rehosting or purchase tests.

### Applied exact source destinations

- KND-B287115376C0B78D — Estimating High-Resolution Red Sea Surface Temperature Hotspots — Arnab Hazra; Raphaël Huser. 2020. Estimating high-resolution Red Sea surface temperature hotspots, using a low-rank semiparametric spatial model. Source: https://arxiv.org/abs/1912.05657 ; verified full PDF: https://arxiv.org/pdf/1912.05657v3
- KND-312070DC843667E9 — Special Report: Manipulation of Economic Indicators in Africa — EXX Africa. 2019. Special Report: Manipulation of Economic Indicators in Africa. Source: https://insight.pangea-risk.com/special-report-manipulation-of-economic-indicators-in-africa ; verified full PDF: https://insight.pangea-risk.com/static/post-pdfs/201902/201902_SPECIAL-REPORT_-MANIPULATION-OF-ECONOMIC-INDICATORS-IN-AFRICA.pdf
- KND-0CADFDD3C78893F6 — Technologies to Construct a Canal — Japan Water Agency. 2020. Technologies to construct a canal. Source: https://www.water.go.jp/honsya/honsya/english/topics/2020/201209.html ; verified full PDF: https://www.water.go.jp/honsya/honsya/english/topics/2020/pdf/02_JWA%27s%20technologies%20to%20construct%20a%20canal.pdf
- KND-0BE96C377E172568 — The Reality of Citrus Production and Marketing in Sudan — Yasir Ahmed Abdalla Eltoum; Anas Omer Abdalbgi Alhadi. 2021. The Reality of Citrus Production and Marketing in Sudan. Source: https://euacademic.org/UploadArticle/4781.pdf ; verified full PDF: https://euacademic.org/UploadArticle/4781.pdf

### Fresh failures held unchanged

- KND-D4F6F490D32A9D23 — Land Use Patterns along the Nile: Traveling Farmer: Ordinary secure public HTTP failure; no fallback to HTTP or bypass; HTTP 403
- KND-B9D530F16FE647EE — Aksum and Nubia: Warfare, Commerce, and Political Fictions: URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issue; HTTP None
- KND-C92F7FBC0DF7FB84 — Art and Industry: The Achievements of Meroe: Ordinary secure public HTTP failure; no fallback to HTTP or bypass; HTTP 404
- KND-603C2A8070F4BE45 — Evidence for an Early Nubian Dialect in Meroitic Inscriptions: URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate (; HTTP None

Hatke/NYU and Aubin proposed HTTP sources were not requested. Ordinary HTTPS probes failed certificate verification; no disabled TLS checks, HTTP fallback, browser-warning bypass or insecure restoration. Land-use HTML chapter returned403, so no metadata/year changes applied. Art and Industry landing and separately proposed exact publisher PDF both returned404 and remain held. The two out-of-scope audit records remain in the catalog and inventory; no deletion.

## Phase 10 - continuing approved research round 8

Round8:3 of4 candidates passed final checks;Greater Kordofan returned202 and36 audit-held records stay unchanged. All542 catalog records preserved. Round7 separately applied4,held4 after checks,and preserved32 audit-held records. Combined rounds7+8:7 applied,unresolved338 →331 (round7:338 →334;round8:334 →331). Known-unavailable labels337 →334 for this batch;seven unverified remain. Format map97PDF+1EPUB.

The manifest deliberately predates round7: exact frozen IDs,title,source/download and index were matched against the current334-row inventory and commit2cbc208 before edits. No round7 catalog objects changed. Two PDFs independently matched reviewed SHA-256 and page counts: Anderson564-page national-library thesis and Krishnan9-page journal article. Miniature Pyramids is the complete publisher HTML article by Eric A. Powell,2013; standard gzip decompression was required before HTML text inspection. Full title/byline,Sedeinga,erosion and ending markers verified;this was normal content decoding,not bypass. An initial2-record build was explicitly stopped with confirmed exit before adding the third record and running a fresh build.

Only3 approved catalog objects,3 exact CSV rows,format/status maps and this audit note changed. All unrelated work,held records,covers,cadence,storage access,paid content and Workers preserved. No rehosting or purchase tests.

### Applied exact sources

- KND-0889E8A87C483673 — Spatial and Temporal Distribution of Domestic Architecture in Christian Nubia — Julie Renee Anderson. 1996. Spatial and Temporal Distribution of Domestic and Civil Architecture in Christian Nubia. Source: https://www.collectionscanada.ca/obj/s4/f2/dsk3/ftp04/NQ35429.pdf ; verified full PDF: https://www.collectionscanada.ca/obj/s4/f2/dsk3/ftp04/NQ35429.pdf
- KND-CC002115EC73F64A — Reinscribing Conrad: Tayeb Salih's Season of Migration to the North — R. S. Krishnan. 1996. Reinscribing Conrad: Tayeb Salih's Season of Migration to the North. Source: https://journals.lib.unb.ca/index.php/IFR/article/view/14324 ; verified full PDF: https://journals.lib.unb.ca/index.php/IFR/article/download/14324/15401
- KND-9A5AAD1E47BEBE90 — Miniature Pyramids of Sudan — Eric A. Powell. 2013. Miniature Pyramids of Sudan. Archaeology Magazine, July/August. Source: https://archaeology.org/issues/july-august-2013/features/sedeinga-necropolis-sudan-meroe-nubia/ ; complete publisher HTML article.

### Fresh failure held unchanged

- KND-2ABCD07CF05CAE1D — Managing Conflict Over Natural Resources in Greater Kordofan: source record returnedHTTP202;no challenge solving,alternate gated-route retry or bypass.

## Phase 11 - continuing approved research round 9

9 of10 candidates passed final secure access/content checks;Strangers Everywhere alias KND-7E21119028D004A9 returned403 and30 audit-held records remain unchanged. All542 records preserved. Unresolved331 →322;known-unavailable334 →325;seven unverified remain. Format map104PDF+1EPUB.

Eight complete PDFs matched reviewed SHA-256 and page counts,including the90-page Rokkan thesis. TABLE essay complete HTML identity/conclusion/footnote markers verified with normal content decoding. Bernal first failed Python certificate-chain verification;the operating-system trusted client then succeeded with HTTP200,TLS verification result0,curl exit0,HTTPS-only redirects,and no certificate/revocation overrides. Its33-page PDF exactly matched the reviewed hash. The earlier8-record build finished before adding Bernal and running a fresh nine-record build.

Rokkan uses only stable handle https://hdl.handle.net/1956/7122 and Read thesis at repository. Full90-page PDF was verified through the normal public repository filelink;no expiring presigned URI or credential query retained in catalog/reports. NBI cover March2008 differs from landing February6;Buzon issue2011/online2012 and Hendrickx issue2014/online2015 remain distinct. Honegger is the complete12-page chapter plus10 front-matter pages,not the proceedings volume. CMI is the2015 translation of three1975 booklets,with introductory contributor separately credited.

Only9 approved catalog objects,9 exact CSV rows,format/status maps and this audit note changed. No unrelated work,held aliases,covers,cadence,storage controls,paid content or Workers changed. No rehosting,purchases or access bypass.

### Applied exact source destinations

- KND-DA8C5E3CF0BD34B9 — Is Agroforestry a Solution to Food Insecurity in Sudan? — Hatim Rijal; Marwa Akola. 2023. Essay: Is agroforestry a solution to food insecurity in Sudan?. Source: https://www.tabledebates.org/blog/agroforestry-solution-food-insecurity-sudan ; Read essay.
- KND-D85FBA44F0C40996 — Sudan Agriculture Value Chain Analysis — World Bank Group. 2020. Sudan: Agriculture Value Chain Analysis. Source: https://documents.worldbank.org/en/publication/documents-reports/documentdetail/731741593616746051/sudan-agriculture-value-chain-analysis ; verified full PDF: https://openknowledge.worldbank.org/bitstreams/ca39f6ee-9c6e-5ecf-84ed-a1ec87db8cf7/download
- KND-DDD57FA869D8D40A — Best Practices for Water Harvesting and Irrigation in Sudan — Mamoun Ibrahim Dawelbeit. 2008. Best Practices for Water Harvesting and Irrigation in Sudan. Source: https://nilebasin.org/node/12693 ; verified full PDF: https://nilebasin.org/sites/default/files/2023-09/sudan_best_practices.pdf
- KND-E7EDFD6A2DBB8C10 — Women's Equal Rights and Islam in Sudanese Republican Thought — Samia al-Nagar; Liv Tønnessen. 2015. Women’s Equal Rights and Islam in Sudanese Republican Thought: A Translation of Three Family Law Booklets from 1975, Produced and Circulated by the Republican Sisters. Source: https://www.cmi.no/publications/5605-womens-equal-rights-and-islam-in-sudanese ; verified full PDF: https://www.cmi.no/publications/file/5605-womens-equal-rights-and-islam-in-sudanese.pdf
- KND-938B415CDB4C36D2 — Native Administration in Dar Humr: Tribal Society and Shifting Leadership — Agnes Maria Rokkan. 2008. Native Administration in Dar Humr, Sudan. Shifting leadership and socio-political structures in a tribal society 1900-1940. Source: https://hdl.handle.net/1956/7122 ; Read thesis at repository.
- KND-F8FBA804437953C4 — Nubian Identity in the Bronze Age — Michele R. Buzon. 2011. Nubian identity in the Bronze Age. Patterns of cultural and biological variation. Source: https://docs.lib.purdue.edu/anthpubs/1/ ; verified full PDF: https://www.anthropology.uw.edu.pl/05/bne-05-02.pdf
- KND-3C35276F521C1C38 — On the Withdrawal of Roman Troops from the Dodecaschoenos in AD 298 — Ben Hendrickx. 2014. On the Withdrawal of the Roman Troops from the Dodecaschoenos in AD 298: Many Questions and Few Answers — The Problems in Perspective. Source: https://akroterion.journals.ac.za/pub/article/view/944 ; verified full PDF: https://akroterion.journals.ac.za/pub/article/download/944/972
- KND-C7DCAEF0CB9D934C — Recent Advances in Our Understanding of Prehistory in Northern Sudan — Matthieu Honegger. 2014. Recent Advances in Our Understanding of Prehistory in Northern Sudan. Source: https://kerma.ch/documents/Publications_PDF/Honegger_2014_12e_Nubian_Studies_Recent_Advances_Understanding_Prehistory_Northern_Sudan.pdf ; verified full PDF: https://kerma.ch/documents/Publications_PDF/Honegger_2014_12e_Nubian_Studies_Recent_Advances_Understanding_Prehistory_Northern_Sudan.pdf
- KND-E4F64C5C590F8755 — Colonial Moral Economy and the Discipline of Development: The Gezira Scheme — Victoria Bernal. 1997. Colonial Moral Economy and the Discipline of Development: The Gezira Scheme and "Modern" Sudan. Cultural Anthropology 12(4):447–479. Source: https://sites.socsci.uci.edu/~vbernal/bio/Bernal-CA2.pdf ; verified full PDF: https://sites.socsci.uci.edu/~vbernal/bio/Bernal-CA2.pdf

### Fresh failure held unchanged

- KND-7E21119028D004A9 — Strangers Everywhere: Nubians in Northern Uganda — source record returned403;no denied-route retry or bypass. Earlier separately held alias KND-B37D7D457EBF4ADA remains unchanged.

## Phase 12 - continuing approved research round 10

Eight of eleven reviewed-ready records passed fresh verification. Tar record KND-B8DDC853D87C2523 returned403; Springer records KND-7E9F316806D30EFF and KND-9E8A2CFB790238C2 returned non-PDF challenge bodies and their original article pages were also challenges. All three and29 originally-held records remain unchanged. No challenge bypass attempted.

All542 records preserved. Unresolved322 to314;known unavailable325 to317;seven unverified unchanged. Format map111PDF+1EPUB+1ZIP. Three standalone PDFs matched prior SHA/page evidence;four PDFs were independently checked by exact title,author,full text and page boundaries without a prior hash. Soleb publisher ZIP matched reviewed SHA,passed CRC and contained the complete976-page PDF;MacOS resource metadata excluded from document counting. Served publisher ZIP remains unmodified. Darfur extraction failed only on report page78,outside the verified complete28-page target chapter.

Round10 old manifest baseline was rebased onto current round9 commit3ccd671 with all11 exact IDs,title/source/download/index matching and no conflicts. Covers,articles,deployment cadence,private storage,paid content and Workers unchanged.

### Exact approved destinations

- KND-F1D545DEA5ABA474 - Sudanese and Nubian Archaeology: Scholarship Past and Present - Rennan Lemos; Samantha Tipper. 2021. Sudanese and Nubian Archaeology: Scholarship Past and Present. Source: https://www.archaeopress.com/Archaeopress/download/9781789698978 ; complete source file: https://www.archaeopress.com/Archaeopress/download/9781789698978
- KND-59627B8B6B73069F - The Dialogue between the River Nile and Its Hinterlands: Al Khandaq - Intisar Soghayroun Elzein Soghayroun. 2009. The Dialogue between the River Nile and its Hinterlands: Al Khandaq - A Desert Terminal and a River Port. Source: https://oestigaard.com/wp-content/uploads/2011/08/book_wci_lowres.pdf#page=109 ; complete source file: https://oestigaard.com/wp-content/uploads/2011/08/book_wci_lowres.pdf#page=109
- KND-0C09057C5CE56884 - The Historical and Religious Conditions of the Split of Sudan - Waldemar Cisło. 2014. The Historical and religious conditions of the split of Sudan in the context of Christian-Muslim relationships. Source: https://czasopisma.upjp2.edu.pl/thepersonandthechallenges/article/view/55 ; complete source file: https://czasopisma.upjp2.edu.pl/thepersonandthechallenges/article/download/55/51
- KND-7FC35624A7B9AE56 - The History and Origins of the Current Conflict in Darfur - Helen Young; Abdul Monium Khider Osman; Yacob Aklilu; Rebecca Dale; Babiker Badri; Abdul Jabbar Abdullah Fuddle. 2005. The History and Origins of the Current Conflict in Darfur. Source: https://fic.tufts.edu/publication-item/darfur-livelihoods-under-siege/ ; complete source file: https://fic.tufts.edu/wp-content/uploads/Young-Darfur-Livelihoods-Under-Seige.pdf#page=26
- KND-F7BFD3DBA63B75E0 - The King Amanikhareqerem and the Meroitic World - Marco Baldi. 2017. The king Amanikhareqerem and the Meroitic world: an account after the last discoveries. Source: https://openstarts.units.it/handle/10077/14297 ; complete source file: https://www.openstarts.units.it/bitstream/10077/14297/1/ATRA_3_online-11_Baldi.pdf
- KND-51D1B8201684B2D0 - The Landscape and Archaeology of Jebel Sabaloka - Lenka Suková; Václav Cílek. 2012. The Landscape and Archaeology of Jebel Sabaloka and the Sixth Nile Cataract, Sudan. Source: https://iansa.eu/papers/IANSA-2012-02-sukova.html ; complete source file: https://iansa.eu/papers/IANSA-2012-02-sukova.pdf
- KND-3ADFB07412E4E2A2 - The Textual Corpus from Wadi Sarga: A New Study - Jennifer Cromwell. 2014. The textual corpus from Wadi Sarga: a new study. Source: https://www.britishmuseum.org/sites/default/files/2020-06/British-Museum_Egypt_Sudan_Newsletter1_2014.pdf ; complete source file: https://www.britishmuseum.org/sites/default/files/2020-06/British-Museum_Egypt_Sudan_Newsletter1_2014.pdf
- KND-0DAC862ADE3B3283 - Histoire et Civilisations du Soudan - Olivier Cabon; Vincent Francigny; Bernard François; Marc Maillot; Mohamed Musa Ibrahim; Odile Nicoloso; Claude Rilly. 2019. Histoire et civilisations du Soudan, de la Préhistoire à nos jours. Source: https://www.soleb.com/livres/soudan/fichiers-numeriques.html ; complete source file: https://www.soleb.com/pdf/soudan/Histoire-et-civilisations-du-Soudan-pdf-bd.zip

## Phase 13 - final first-pass research round 11

Reviewed65: 12 passed final verification;3 proposed candidates failed;50 originally held remain unchanged. Original405 IDs reconcile to 103 repaired plus302 unresolved;unreviewed0. Seven preinventory repairs are separate: 110 overall repairs. All542 cards retained in both languages;no duplicate deletion or merger. Remaining130 outside-inventory records are not claimed reviewed.

Unresolved314 to302;known-unavailable317 to305;seven unverified unchanged. Verified format map{'PDF': 120, 'EPUB': 1, 'ZIP': 1}. Research baseline3fb5cad rebased by frozen exact ID onto b55e84d after rounds9/10;no conflicts.

Copyright and access restrictions preserved. Links point to independently verified publisher/repository files or full HTML;no rehosting,no credential/certificate overrides,no paid-content exposure. Five no-checksum PDFs were verified by exact original title/byline/date and complete text/page endings. Successful OS-trusted TLS checks are recorded separately from initial Python-chain failures.2016 Darfur publication differs from2017 release;2014 cotton crop year differs from2015 publication.

### Applied exact sources

- KND-60AB77943D73391F - Review of the Sudanese Socio-Economic Development Problems - Magda Ismail A. Mohsin. 2002. Review of the Sudanese Socio-Economic Development Problems. Source: https://jecd.sesric.org/pdf.php?file=ART02040104-2.pdf ; full PDF: https://jecd.sesric.org/pdf.php?file=ART02040104-2.pdf
- KND-CCF72010DFCDA3D8 - The Gezira Irrigation Scheme in Sudan: Objectives, Design, and Performance - Hervé Plusquellec. 1990. The Gezira Irrigation Scheme in Sudan: Objectives, Design, and Performance. Source: https://documents1.worldbank.org/curated/en/377141468778504847/pdf/multi-page.pdf ; full PDF: https://documents1.worldbank.org/curated/en/377141468778504847/pdf/multi-page.pdf
- KND-3B3F92C493A53CB2 - Sudan’s Predicament and the Israeli Connection - Paul Rivlin. 2020. Sudan’s Predicament and the Israeli Connection. Source: https://dayan.org/file-download/download/public/16983 ; full PDF: https://dayan.org/file-download/download/public/16983
- KND-7AB4100B7A66DC44 - 2014: Third Year of Bt Cotton Cultivation in Sudan - M. Karembu; F. Nguthi; S. Asim; P. Chege. 2015. 2014: Third Year of Bt Cotton Cultivation in Sudan. Source: https://africenter.isaaa.org/wp-content/uploads/2016/08/Third-year-of-Bt-cotton-cultivation-in-Sudan.pdf ; full PDF: https://africenter.isaaa.org/wp-content/uploads/2016/08/Third-year-of-Bt-cotton-cultivation-in-Sudan.pdf
- KND-7575F6C722048BAA - The Kandake: A Missing History - Heather Preston. 2023. The Kandake: A Missing History. Source: https://www.cbeinternational.org/resource/the-kandake-a-missing-history/ ; full PDF: https://www.cbeinternational.org/wp-content/uploads/2023/10/The-Kandake-A-Missing-History.pdf
- KND-1DAF06634A263399 - Kandake - Wikipedia contributors. n.d.. Kandake. Source: https://en.wikipedia.org/wiki/Kandake ; full HTML article.
- KND-44662AF620384F71 - Industrial location analysis of Sudan - Khalid Hassan Idris. 1980. Industrial location analysis of Sudan. Source: https://etheses.dur.ac.uk/7493/ ; full PDF: https://etheses.dur.ac.uk/7493/1/7493_4558.PDF
- KND-A76AD1D69B662610 - Cotton Export Performance and Constraints in Sudan - Imad Eldin Elfadil Abdel Karim Yousif. 2015. Cotton Export Performance and Constraints in Sudan. Source: https://wasdlibrary.org/download/ijsr-v5-n2-2015-cotton-export-performance-constraints-sudan/ ; full PDF: https://faculty.ksu.edu.sa/sites/default/files/ijsr_v5_n2_2015_yousif.pdf
- KND-01ABBB79090299EC - Swan Song in the Nile Valley: The Mamlūk Statelet in Dongola (1812–1820) - Emanuel Beška. 2020. Swan Song in the Nile Valley: The Mamlūk Statelet in Dongola (1812–1820). Source: https://www.sav.sk/journals/uploads/1204094308_Beska_FINAL.pdf ; full PDF: https://www.sav.sk/journals/uploads/1204094308_Beska_FINAL.pdf
- KND-BF46E197EA11871B - Current Status of Agriculture and Future Challenges in Sudan - Farida Mahgoub. 2014. Current Status of Agriculture and Future Challenges in Sudan. Source: https://nai.diva-portal.org/smash/get/diva2%3A712485/fulltext01.pdf ; full PDF: https://nai.diva-portal.org/smash/get/diva2%3A712485/fulltext01.pdf
- KND-A6B3FD517D033891 - The Impact of Human Capital on Economic Growth: Empirical Evidence from Sudan - Khalafalla Ahmed Mohamed Arabi; Suliman Zakaria Suliman Abdalla. 2013. The Impact of Human Capital on Economic Growth: Empirical Evidence from Sudan. Source: https://www.sciedu.ca/journal/index.php/rwe/article/view/2999/0 ; full PDF: https://www.sciedu.ca/journal/index.php/rwe/article/download/2999/1777
- KND-7980A52B37C28226 - Water Diplomacy: And the Share of the Nile River between Egypt, Ethiopia and Sudan - Francis Kwesi Kyirewiah. 2022. Water Diplomacy: And the Share of the Nile River between Egypt, Ethiopia and Sudan. Source: https://www.richtmann.org/journal/index.php/mjss/article/download/12809/12410 ; full PDF: https://www.richtmann.org/journal/index.php/mjss/article/download/12809/12410

### Fresh holds unchanged

- KND-5243ABBC5EDAE6C8 - Secure source HTTP failure;no bypass
- KND-2EC6182C9F00C617 - Secure source HTTP failure;no bypass
- KND-7CFE9A1F6BDAF25C - TimeoutError: The read operation timed out

### Remaining decisions and Claude handover

First-pass review complete means all405 target mappings researched;it does not mean all resolved. Remaining holds include ambiguous title/work/edition,missing or partial full text,403/404/502/challenges/certificate failures,and uncertain lawful access. Keep exact IDs and duplicate aliases. Use lawful publisher/catalog record links with record-only labels where full text cannot be established. Obtain authorization or reliable originals for held files;do not make buckets public or infer rights. Iran economics remains out of scope. Review legacy fuzzy author/file matching and blanket bucket rewrite scripts before future use;never rerun them blindly. Existing articles,covers,cadence and unrelated edits preserved. This source-repair worker did not change Workers or execute purchase tests.

## Approved local metadata-only batch -18October2026

Applied exactly38explicitly approved metadata proposals. The additional7remain pending and unchanged. Original sources,active downloads,format/status maps,all542records,display titles,covers,tags and unrelated news preserved. Unknown publication years remain unknown for Hamdok,Bein and El Kheir. Local title-page evidence for Hatke does not imply fullbook recovery. No source file uploaded or rehosted;wrong-content EPUB bytes never restored. Source repairs remain110;download backlog302;known-unavailable labels305 and unverified7 unchanged. CSV author credits synchronized only where the approved author actually changed.

- KND-FAF69E7AE1C1E4B4 - Abdalla Ahmed Abdalla; Hassan Osman Abdel Nour. 2001. The Agricultural Potential of Sudan. Executive Intelligence Review28(8),23February2001,pp37-45.
- KND-2C6520D59C12C805 - Michael Simire. 2014. Abdalla Hamdok: How Africa can feed its people, create wealth. EnviroNews Nigeria,8October2014;article reporting/quoting Abdalla Hamdok;local7-page browser print.
- KND-8D5EB40494210D26 - United Nations Development Programme (UNDP). 2014. Trends in the Sudanese Economy: 1st Quarter, 2014.
- KND-B37D7D457EBF4ADA - Charles Amone. 2013. Strangers Everywhere: Exclusion, Identity and the Future of Nubians in Northern Uganda.
- KND-D2DCD09AFAF55609 - Karl Wohlmuth; Dirk Hansohm. 1986. Sudan: A Case for Structural Adjustment Policies. Sudan Economy Research Group Discussion Paper8,February1986. Introductory note records minor updates after the March1986conference.
- KND-43167ED636D0D62B - Laura Mann. 2014. Wasta! The long-term implications of education expansion and economic liberalisation on Politics in Sudan. Review of African Political Economy41(142),561-578;local35-page accepted manuscript;repository deposit November2017. DOI:10.1080/03056244.2014.952276.
- KND-45C9849EE96E6F95 - Poolad Karimi; David Molden; An Notenbaert; Don Peden. 2012. Nile Basin farming systems and productivity.
- KND-27F9F27908FA2DE4 - Olugbenga Adesida. 2001. Governance in Africa: The Role for Information and Communication Technologies. African Development Bank Economic Research Papers65.
- KND-684CA25641427701 - Faith Mabera. 2020. The Horn of Africa-Persian Gulf Nexus: Inter-Regional Dynamics and the Reshaping of Regional Order in Geopolitical Flux.
- KND-7F66DF2789994977 - United Nations. 2020. World Economic Situation and Prospects2020. UN DESA,UNCTAD and United Nations regional commissions;New York.
- KND-D4F6F490D32A9D23 - Rick Bein. n.d.. Land Use patterns along the Nile. Traveling Farmer,chapter35;undated local print.
- KND-34D83E78A19EABAD - African Development Bank Group. 2016. Sudan: Darfur Infrastructure Development Report. 2016publication;online release February2017;79-page report.
- KND-D207E49C7C33C8AE - Karen Conniff; David Molden; Don Peden; Seleshi B. Awulachew. 2012. Nile water and agriculture: Past, present and future.
- KND-D9EC311BAA51A9FD - Elsa Yvanez; Magdalena M. Wozniak. 2019. Cotton in ancient Sudan and Nubia: Archaeological sources and historical implications. Revue d’ethnoécologie15,2019;local54-page export generated10December2020;not reviewed51-page July2019export. DOI:10.4000/ethnoecologie.4429.
- KND-AB37E01F7467A8CF - Simone Wolf; Hans-Ulrich Onasch; Kéré Architecture. 2016. A new protective shelter for the Royal Baths at Meroë (Sudan).
- KND-B9D530F16FE647EE - George Hatke. 2013. Aksum and Nubia: Warfare, Commerce, and Political Fictions in Ancient Northeast Africa. New York University Press and Institute for the Study of the Ancient World;only title page recovered.
- KND-C92F7FBC0DF7FB84 - Samia B. Dafa’alla. 1993. Art and Industry: The Achievements of Meroe. Expedition35(2),1993,15-21.
- KND-603C2A8070F4BE45 - Penelope Aubin. 2003. Evidence for an Early Nubian Dialect in Meroitic Inscriptions: Phonological and Epigraphic Considerations. December 2003 article; archive scan digitized 2008.
- KND-685ECEA3C82DF543 - Paola Iacumin; Antonietta Di Matteo; Donatella Usai; Sandro Salvatori; Giampiero Venturelli. 2016. Stable Isotope Study on Ancient Populations of Central Sudan: Insights on their Diet and Environment. American Journal of Physical Anthropology;local21-page uncorrected publisher proof;00:00-00 and00Month are placeholders;final issue pagination not established. DOI:10.1002/ajpa.22987.
- KND-2ABCD07CF05CAE1D - El Fatih Ali Siddig; Khalid El-Harizi; Bettina Prato. 2007. Managing Conflict Over Natural Resources in Greater Kordofan, Sudan: Some Recurrent Patterns and Governance Implications. IFPRI Discussion Paper 00711, August 2007.
- KND-538B2E8C7B2B5221 - Amanda Hsiao; Laura Jones. 2011. Rethinking Sudan after Southern Secession.
- KND-4309968997148F7B - Akshaya Kumar. 2015. Fool’s Gold: The Case for Scrutinizing Sudan’s Conflict Gold Trade.
- KND-B1323B4D504C9D1F - Abdalla A. Hamdok. n.d.. Good governance and the policy challenge: the African Development Bank perspective. Chapter in Monitoring and Evaluation Capacity Development in Africa,pp21-28;2000workshop;publication year unestablished.
- KND-45255609C5A64049 - Secretariat for Legal Affairs and Constitutional Development (New Sudan). 2003. Laws of the New Sudan: The Penal Code, 2003. Historical2003Penal Code;Secretariat for Legal Affairs and Constitutional Development is issuing publisher,not an individual author.
- KND-7E21119028D004A9 - Charles Amone. 2013. Strangers Everywhere: Exclusion, Identity and the Future of Nubians in Northern Uganda. Greener Journal of Political and Social Sciences 1(1), October 2013, pages 1–8; DOI 10.15580/gjpss.2013.1.170913844.
- KND-D1972D04A4734C6C - Chiara Dezzi Bardeschi. 2004. Nubia Bibliography up to 2000: List of Archaeological Missions in Nubia. UNESCO CLT/CIH/MCO/2004/RM/H/1;495-page supplied digital file;printed10skipped.
- KND-A4DBFC9DC132C0DE - Giulia D’Ercole. 2021. Seventy Years of Pottery Studies in the Archaeology of Mesolithic and Neolithic Sudan. DOI:10.1007/s10437-021-09432-y.
- KND-B8DDC853D87C2523 - Abbas S. Mohammed-Ali; Gamal G.A. El Hassan. 2015. Tar: An Ancient Sudanese Curing Treatment. The Kushite World: Proceedings of the 11th International Conference for Meroitic Studies, Vienna, 1–4 September 2008, edited by Michael H. Zach; Beiträge zur Sudanforschung, Beiheft 9, Vienna 2015, pp. 547–550..
- KND-7E9F316806D30EFF - Randi Haaland. 2014. The Meroitic Empire: Trade and Cultural Influences in an Indian Ocean Context. African Archaeological Review31,649-673,2014;27-page author offprint with two wrappers. DOI:10.1007/s10437-014-9169-0.
- KND-9E8A2CFB790238C2 - Michael Brass. 2014. The Southern Frontier of the Meroitic State: The View from Jebel Moya. African Archaeological Review31,425-445,2014;22-page local copy includes appended notice. DOI:10.1007/s10437-014-9164-5.
- KND-D5B99565704F0428 - Pavel Onderka. 2014. Wad ben Naga: a history of the site. Sudan & Nubia18,83-92;16-page offprint including front/back matter;not the2013monograph.
- KND-601F961E659A1B66 - Mohammed A. Mohammed; Omer Mohammed; Mohamed Ibrahim; Huda G. Osman. 2020. Khartoum sky trains network: a study on implementing caterpillar trains concept in Khartoum. MATEC Web of Conferences308,02003;ICTTE2019conference;5-page2020article. DOI:10.1051/matecconf/202030802003.
- KND-7CFE9A1F6BDAF25C - Faith Mabera. 2020. The Horn of Africa-Persian Gulf nexus: inter-regional dynamics and the reshaping of regional order in geopolitical flux. Global Insight, Issue 136, April 2020.
- KND-97A63DBFCAAD6B0D - Osman M. El Kheir. n.d.. The Urban Environment of Khartoum. Undated11-page paper;references accessed May2012 are not a publication date.
- KND-2EC6182C9F00C617 - African Development Bank Group. 2016. Sudan: Darfur Infrastructure Development Report. 2016publication;online release February2017;79-page report.
- KND-78EF13B8A0845C7D - Lauren Ploch Blanchard. 2020. Sudan’s Removal from the State Sponsors of Terrorism List. CRS InsightIN11531,version1,9November2020.
- KND-C6397BD36FD08DFB - Republic of Sudan, Ministry of Agriculture and Forests. 2017. Sudan E-Agriculture Strategy and Action Plan (2018–2022). December2017strategy for2018-2022.
- KND-CB5FDEB48DF0F85D - Elsa Yvanez. 2016. Spinning in Meroitic Sudan: Textile Production Implements from Abu Geili.

Validation and exact published commit/deploy evidence are retained in the updated handover.

## Approved additional seven metadata-only batch -18October2026

Applied exactly7additional explicitly approved metadata proposals, following the original38 commit. Total45distinct metadata records corrected. Original sources,active downloads,format/status maps,all542records,display titles,covers,tags and unrelated news preserved. Unknown publication years remain unknown for Hamdok,Bein and El Kheir. Local title-page evidence for Hatke does not imply fullbook recovery. No source file uploaded or rehosted;wrong-content EPUB bytes never restored. Source repairs remain110;download backlog302;known-unavailable labels305 and unverified7 unchanged. CSV author credits synchronized only where the approved author actually changed.

- KND-A8D3FBC1EE63591B - Todd Litman; Felix Laube. 2002. Automobile Dependency and Economic Development. Version dated6August2002;cover copyright1996-1999;20-page report.
- KND-96C804A4AA059AC0 - Josefine Kuckertz. 2018. Amanakhareqerema – a Meroitic King of the 1st Century AD. Der antike Sudan/MittSAG29,119-144;34-page offprint with six preliminary pages and appended colour plates.
- KND-440CCD594D2784CF - John Coleman Darnell. 2006. The Inscription of Queen Katimala at Semna: Textual Evidence for the Origins of the Napatan State. Yale Egyptological Studies7;copyright2006Yale Egyptological Seminar;124physical pages including preliminaries and plates.
- KND-A2AD0CF01141DC28 - Shih-Wei Hsu. 2020. The Wretched one becomes the Strong Bull: The Development of Literary Images of Nubians in Ancient Egyptian Royal Inscriptions. Chapter in Ein Kundiger,der in die Gottesworte eingedrungen ist;Ägypten und Altes Testament99;Zaphon2020,83-90;18-page offprint including10preliminary pages.
- KND-049E351E22F032A0 - Timothy Kendall. n.d.. Why Did Taharqa Build His Tomb at Nuri?. PAM Supplement Series2.1,117-147;31-page article;publication year not established from this local offprint.
- KND-524724CAC0A09085 - Tony Barnett. n.d.. Why Are Bureaucrats Slow Adopters? The Case of Water Management in the Gezira Scheme. 11article pages ending printed70 plus appended EBSCO notice=12physical pages;original publication year not established.
- KND-6D22CC5FAEB65303 - Ibrahim Zakaria Bahreldin. 2020. Beyond the Riverside: An Alternative Sustainable Vision for Khartoum Riverfront Development. Civil Engineering and Architecture8(2),113-126,2020;14-page publisher article.

Validation and exact published commit/deploy evidence are retained in the updated handover.

## Approved 36 metadata-only corrections - 18 October 2026

Applied the separately approved 36-record exact metadata manifest. Total 81 metadata records corrected. All 542 records, source/download URLs, format/status maps, display titles, covers and tags preserved. Source repairs remain 110; download backlog 302. No rehosting or download restoration.

- KND-FE1DDFFDB19C3117 - Maciej Wyżgoł; Agata Deptuła. 2020. Living Outside the Wall: the Quarter of Wattle-and-daub Houses in Old Dongola of the Funj Period. Journal of African Archaeology 18; early-online pagination 1-24.
- KND-5A02FB87D5F28485 - Magda Ismail A. Mohsin. 2002. Review of the Sudanese Socio-Economic Development Problems. Journal of Economic Cooperation 23(3), 85-102; 18-page article.
- KND-F7E70AA0EED49E2C - Włodzimierz Godlewski. 2007. Old Dongola: Kom A (Acropolis), 2005. Polish Archaeology in the Mediterranean 17, 287-299; 13 article pages plus bibliographic wrapper; 2005 is the field season.
- KND-8DD0240A5FA15789 - Republic of the Sudan, Ministry of Finance and Economic Planning. 2019. Implementation of Istanbul Plan of Action for Least Developed Countries (IPoA) 2011-2020: Sudan National Report. Sudan National Report; Khartoum, October 2019; 25-page file.
- KND-6B73F5D3D760786A - Marek Woźniak. 2021. Lost port of the Red Sea. Academia Letters, Article 213, January 2021; DOI 10.20935/AL213; five-page article.
- KND-1EA0B352A6737FFD - Janice W. Yellin. 2015. Meroitic royal chronology: the conflict with Rome and its aftermath. Sudan & Nubia 19, 2-15; article on PDF pages 4-17 of a 20-page offprint.
- KND-B1003FE97FA62B7A - Noëlle Timbart; Abdel Rahman Ali Mohamed Rahma; Marc Aucouturier; Michel Baud; Guillemette Andreu-Lanoë; Thierry Borel; Benoit Mille; Christine Pariselle. 2015. A bronze statue of a Meroitic archer-king: New data. Studies in Conservation 60(3), 194-210; DOI 10.1179/2047058413Y.0000000118; 17 article pages plus appended rights notice.
- KND-CAF3051CFE7AFEB8 - Daniele Salvoldi. 2015. A Historical GIS of Nubia based on the William John Bankes Archive (1815-1822). Presentation at Göttingen Dialog in Digital Humanities, 9 June 2015; 30 slides.
- KND-170BA47C33CEDD6D - M. Drzewiecki; W. Raczkowski. 2008. Following O.G.S. Crawford: satellite images and field archaeology in Sudan. In Advances on Remote Sensing for Archaeology and Cultural Heritage Management, 3-6; Aracne, first edition September 2008; four-page chapter plus 16 preliminary pages.
- KND-C10DD13679630881 - Dan’el Kahn. 2013. The History of Kush - an Outline. In The Power of Walls: Fortifications in Ancient Northeastern Africa, 17-31; Colloquium Africanum 5; workshop held 2011, volume published 2013.
- KND-2E1BE4006743EA6A - David N. Edwards. 1998. Meroe and the Sudanic Kingdoms. The Journal of African History 39(2), 175-193; 19 article pages plus JSTOR wrapper.
- KND-3901339DD286287E - Sandro Salvatori; Donatella Usai; Andrea Zerboni. 2011. Mesolithic Site Formation and Palaeoenvironment Along the White Nile (Central Sudan). African Archaeological Review 28, 177-211; published online 16 June 2011; 35-page article.
- KND-EB82F9F4BB1A9D89 - Ibrahim Omer. 2008. Moses Kushite Connection. California State University, Monterey Bay; Visual and Public Art capstone, Spring 2008; 23-page project plus two preliminary pages.
- KND-05F81A458662AA6E - Carolyn Fluehr-Lobban. 1998. Nubian Queens in the Nile Valley and Afro-Asiatic Cultural History. Conference-paper version, Ninth International Conference for Nubian Studies, Boston, 20-26 August 1998; nine pages; no later proceedings date substituted.
- KND-673351DE45937D81 - S. Schrader; M. Buzon; J. Irish. 2014. Illuminating the Nubian ‘Dark Age’: A bioarchaeological analysis of dental non-metric traits during the Napatan Period. HOMO - Journal of Comparative Human Biology 65, 267-280; 14-page article.
- KND-51D83B71F9074B1F - Salim Faraji. 2015. King Silko and the Roots of Nubian Christianity. In The Kushite World, Beiträge zur Sudanforschung Beiheft 9, 331-342; 12 chapter pages plus seven preliminary pages; 2008 conference, 2015 publication.
- KND-5620FF60C8B90BAD - Azhari Mustafa Sadig. 2013. Reconsidering the ‘Mesolithic’ and ‘Neolithic’ in Sudan. In Neolithisation of Northeastern Africa, SENEPSE 16, 23-42; ex oriente; 20 chapter pages plus three preliminary pages.
- KND-2DE854F6CA166089 - Geoff Emberling. 2014. Pastoral States: Toward a Comparative Archaeology of Early Kush. Origini 36, 125-156; 32 article pages plus eight cover/imprint pages; Gangemi.
- KND-CB63F64C3ED8C916 - Julia Budka. 2011. The early New Kingdom at Sai Island: preliminary results based on the pottery analysis (4th Season 2010). Sudan & Nubia 15, 23-33; 11 article pages on PDF 5-15 of an 18-page offprint; 2010 is the field season.
- KND-F4FBDA2D6E4A3F97 - Isabella Welsby Sjöström; Ross Thomas. 2011. The Kushite Pottery Sequence at Kawa: Parallels at Home and Abroad. Sudan & Nubia 15, 64-71; eight article pages on PDF 4-11 of a 14-page offprint.
- KND-8F36F5F35557F3BC - Danièle Michaux-Colombot. 2015. The Rosette in Nubian Cultures. In The Kushite World, Beiträge zur Sudanforschung Beiheft 9, 279-297; 19 chapter pages plus seven preliminary pages; 2008 conference, 2015 publication.
- KND-2DC0DD62B85B7E99 - Cornelia Kleinitz. 2013. Between Valorisation and Devaluation: Making and Unmaking (World) Heritage in Sudan. Archaeologies, 427-469; DOI 10.1007/s11759-013-9249-9; 43-page article.
- KND-9231F0FC9C773DDD - Michele R. Buzon; Stuart Tyson Smith; Antonio Simonetti. n.d.. Entanglement and the Formation of Ancient Nubian Napatan State. 42-page author manuscript, including terminal tables; publication year not established from this copy.
- KND-026DF468701BF564 - James K. Hoffmeier. n.d.. Egypt’s Role in the Events of 701 B.C. in Jerusalem. 16-page scholarly article, printed 219-234; publication year not established from this offprint.
- KND-218FF9BBE5A4E084 - Peter Lacovara. n.d.. A Faience Tile of the Old Kingdom. In Studies in Honor of William Kelly Simpson, 487-491; five chapter pages plus ResearchGate wrapper; upload and typesetting dates are not publication-year evidence.
- KND-44071DE78E2271F8 - Larry Ross. n.d.. The Interaction Sphere of Nubia and Egypt: from the Old Kingdom to the Meroitic Period. 24-page paper, including title page and terminal bibliography; publication year not established.
- KND-E3683091F9CC327B - C. Leonard Woolley; D. Randall-MacIver. 1910. Karanog: The Romano-Nubian Cemetery. Eckley B. Coxe Junior Expedition to Nubia, volume III, Text; University Museum, Philadelphia; 314-page scan; title-page date MCMX.
- KND-A4EE62F754D00375 - Necia Desiree Harkless. 2006. Nubian Pharaohs and Meroitic Kings: The Kingdom of Kush. AuthorHouse, first published 2006; ISBN 1-4259-4496-5; 225-page local copy with apparent preliminary-page gaps, completeness on hold.
- KND-B2DB62F8094CE09A - Kevin Burrell. 2018. ‘From Beyond the Rivers of Cush’: Negotiating Ethnic Identity and Cushite-Israelite Interrelations in the Hebrew Bible. PhD dissertation, Stellenbosch University, December 2018; 366 physical pages; not silently substituted for a later published monograph.
- KND-2B2E1C4340AA4B59 - Mahmoud El-Tayeb. 2012. Funerary traditions in Nubian Early Makuria. Gdańsk Archaeological Museum African Reports 9, Monograph Series 1; ISBN 978-83-85824-57-2; 118-page local file.
- KND-8D7EEA502195E767 - Hans Barnard. 2008. Eastern Desert Ware: Traces of the Inhabitants of the Eastern Deserts in Egypt and Sudan During the 4th-6th Centuries CE. Leiden University doctoral thesis, defended 4 June 2008; 260 physical pages through printed index 246.
- KND-26D5038A5A8337C9 - J. L. Berggren. 2016. Episodes in the Mathematics of Medieval Islam. Second edition; Springer; eBook ISBN 978-1-4939-3780-6; DOI 10.1007/978-1-4939-3780-6; first edition 1986, second edition 2016; 266 physical pages.
- KND-8FA42B78E3784F6D - Sobhi Bouderbala; Sylvie Denoix; Matt Malczycki (editors). 2017. New Frontiers of Arabic Papyrology: Arabic and Multilingual Texts from Early Islam. Islamic History and Civilization 144; Brill, Leiden and Boston; papers from the 2012 conference, volume published 2017; 220 physical pages.
- KND-F0949B67F5035A21 - John Freely. 2011. Light from the East: How the Science of Medieval Islam Helped to Shape the Western World. I.B.Tauris, 2011; 260 physical pages including preliminaries and index.
- KND-90FE8BDDF6E335FE - Syed Farid Alatas. 2014. Applying Ibn Khaldun: The Recovery of a Lost Tradition in Sociology. Routledge Advances in Sociology 104; first published 2014; 224 physical pages through index.
- KND-E008D07EDEC7F526 - Laurence Moftah (compiler and text editor); AUC Libraries and Learning Technologies, Reference Services Department. 2003. Nubia and the Nubian People: An Annotated Bibliography. July 2003; 78-page bibliography; annotations by Nermine Rifaat, Adib Sourial, Achiri and Malak Yousry; credits on page 78.

## Approved 124 metadata-only corrections - 18 October 2026

Applied the separately approved 124-record exact metadata manifest. Total 205 metadata records corrected. All 542 records, source/download URLs, format/status maps, display titles, covers and tags preserved. Source repairs remain 110; download backlog 302. No rehosting or download restoration.

- KND-52B4CB6F5E04ADB8 - African Development Bank Group. 2018. After Two Decades of ‘Solitude’: Targeted Strategies for Quick Economic Wins. Sudan Economic Report; ISBN 978-9938-882-84-1.
- KND-451780251FBDB572 - Amanda Zarder. n.d.. The Agricultural Revolution. 19-slide teaching presentation; undated.
- KND-E7EE7093CA01BA63 - Ammar Abbker Abdalla. 2018. Towards sustainable management of water resources in Sudan. Arab International Academy journal, issue 4, December 2018, 1-10.
- KND-D033EF0F8EA2C3D4 - Lycopodium. 2020. Feasibility Study: NI 43-101 Technical Report, Block 14 Gold Project, Republic of the Sudan. Report 14 September 2020, effective 31 August 2020; prepared for Orca Gold.
- KND-A1F31BC858C29B5C - Federal Research Division, Library of Congress; LaVerle Berry (editor). 2015. Sudan: A Country Study. Fifth edition, first printing 2015; replaces Helen Chapin Metz 1992 edition.
- KND-3036D32E1B958FA4 - Global Financial Integrity. 2020. Sudan and Trade Integrity. May 2020; 124 physical pages.
- KND-58C8185C8E1D638F - Hussein Askary. 2010. Africa and the Four Powers: Sudan Inaugurates Continental Railway. EIR 37(3), 22 January 2010, printed 9-14.
- KND-8ADA72166B0A7D0F - Infrastructure & Cities for Economic Development (ICED). 2018. Sudan Infrastructure Sector Overview. ICED 2018 sector briefing.
- KND-20B0B123E7084FE8 - H. C. Jackson. 1926. Osman Digna. Methuen; first published 1926, visually magnified date.
- KND-0D0091C5CB16CEE1 - Mahasin A. Daffall; Ishtiag Faroug Abdalla; Haider S. Abdalla. 2015. Evaluation of Some Orchards Management Practice under River Nile State - Sudan. International Journal of Agriculture Innovations and Research 3(6), 1691-1696.
- KND-E1D111918122B6A1 - Mahmoud El-Tayeb. 2020. Dongola Reach: A Historical, Geographical and Economic Overview. Chapter 1; DOI 10.1163/9789004433755_002.
- KND-468CDD84A8CAC994 - Muriel Mirak-Weissbach. 1996. The Gezira Scheme: Sudan's struggle for food self-sufficiency. EIR 23(41), 11 October 1996, printed 67-69.
- KND-B417697C98D84DF0 - Włodzimierz Godlewski. 2013. Dongola - ancient Tungul: archaeological guide. PCMA Archaeological Guides 1; ISBN 978-83-903796-6-1.
- KND-5AF05E85DEC17ABF - Patrick Conway. 1993. Sudan and the Exploitation of the Waters of the Nile. Revision April 1993; teaching case with appendix and instructor notes.
- KND-7A54CB5D2DEC2843 - L. Berry; S. Geistfeld. 1983. Eastern African Country Profiles: Sudan. Revised edition, May 1983; International Development Program, Clark University.
- KND-70518024F508986F - United Nations Conference on Trade and Development. 2015. Investment Policy Review: The Sudan. UNCTAD/DIAE/PCB/2014/5; New York/Geneva 2015.
- KND-1D7341D863474695 - Sudan National Preparatory Committee for the United Nations Water Conference. 1977. The Water Resources of the Sudan. Democratic Republic of the Sudan; Mar del Plata conference report 1977.
- KND-9E947509279EAD11 - World Food Programme / Logistics Cluster; Pamela Onyango (assessor). n.d.. Sudan: Logistics Capacity Assessment. Web-print; section table records September 2019 updates, not necessarily publication date.
- KND-18CB40BB53403A5D - Nile Basin Initiative, Socio-economic Development and Benefit Sharing Project. 2009. Food-Poverty-Vulnerability Index Analysis for the Nile Basin Region (Ethiopia, Kenya and Sudan): Sudan. First Published 2009; older 2007/2008 cover wording is not substituted for imprint.
- KND-F267BC56E91C5B08 - Hassan Elyas Mohammed. 1986. Khartoum Urban Area: A Study on Urban Planning. PhD thesis, Department of Geography, University of Khartoum, 1986.
- KND-1D3C9ABB1B27DC5E - Commonwealth War Graves Commission. n.d.. In Memory of Lance Corporal William Henry Cecil Jackson. Memorial certificate; death date 22 May 1940 is not document publication date.
- KND-3D96D2E69757450E - United Nations, Department of Field Support, Cartographic Section. 2012. Sudan. Map No. 4458 Rev. 2, March 2012; low-resolution map in June 2021 browser print.
- KND-0BBE35999EF10B77 - Central Intelligence Agency, Directorate of Intelligence. 1982. Sudan: Agricultural Problems. NESA 82-10501, September 1982; approved for release 19 June 2007.
- KND-385D258B4CFBB39D - Abdeen Mustafa Omer. 2008. Water resources and freshwater ecosystems in Sudan. Renewable and Sustainable Energy Reviews 12(8), 2066-2091, October 2008; DOI 10.1016/j.rser.2007.01.005.
- KND-049A72113DF638A2 - United Nations Environment Programme. 2017. Water, vital for life and sustainable growth in Sudan. UNEP story, 7 August 2017; three-page browser print.
- KND-9E39982C50358EA8 - Joseph Lafayette Gaston. n.d.. A Brief Overview of the Cultural Continuity along the Nile Valley during the 5th Millennium B.C.. ANKH 18/19/20, issue-year range 2009-2010-2011, printed 20-49.
- KND-4C3A09CA03B42165 - Raoul McLaughlin. 2014. Desert Legions. History Today, June 2014, printed 31-37 plus rights notice.
- KND-12C0AB49444D3412 - Steffen Wenig. 1978. Africa in Antiquity: The Arts of Ancient Nubia and the Sudan. Volume II: The Catalogue. Brooklyn Museum, 1978; translators Diana S. Peters and Charles M. Stern; editors Sylvia Hochfield and Elizabeth Riefstahl.
- KND-ED87A370E1A2E748 - E. A. Wallis Budge. 1920. By Nile and Tigris: A Narrative of Journeys in Egypt and Mesopotamia on Behalf of the British Museum between the Years 1886 and 1913. Volume I. John Murray, London, 1920.
- KND-D26F62F4F668FECB - R. S. O’Fahey; Jérôme Tubiana. n.d.. Darfur: Historical and Contemporary Aspects. 42-page report; publication date not printed in reviewed boundaries.
- KND-4329E245E335AA5A - Timothy Kendall (editor). 2004. Nubian Studies 1998: Proceedings of the Ninth Conference of the International Society of Nubian Studies. Northeastern University, Boston, 2004; conference August 1998; ISBN 0-9761221-0-3.
- KND-8F2A16ABCC4E23F1 - British Museum; The CarAf Centre. n.d.. The Wealth of Africa: The Kingdom of Kush. Students’ Worksheets. 12-page educational resource; undated.
- KND-F1142A9AFD541C9F - Intisar Soghayroun Elzain. n.d.. Meroe, the City State, the Kingdom, the Empire: Why Meroe?. Printed 35-46, plus ResearchGate wrapper; February 2019 upload is not established publication date.
- KND-251E812069DBBA7B - Roxanne L. Euben. 2008. Journeys to the Other Shore: Muslim and Western Travelers in Search of Knowledge. Princeton; second printing and first paperback printing 2008; original copyright 2006.
- KND-3D5B662F4880A539 - De Lacy O’Leary. 1979. How Greek Science Passed to the Arabs. This edition 1979, Routledge & Kegan Paul; original 1949; ISBN 0 7100 1903 3; AINA digital derivative.
- KND-DEE8D7B965419846 - George Gheverghese Joseph. 2011. The Crest of the Peacock: Non-European Roots of Mathematics. Third edition, Princeton 2011; original I.B.Tauris edition 1991.
- KND-8D280CA947187CD3 - Dag Nikolaus Hasse. 2016. Success and Suppression: Arabic Sciences and Philosophy in the Renaissance. Harvard University Press, 2016.
- KND-6BA5062DAD913A20 - Elias Muhanna. 2018. The World in a Book: Al-Nuwayri and the Islamic Encyclopedic Tradition. Princeton University Press, 2018.
- KND-D553E6AFE717C2D9 - Omer S. Osman; Ibrahim Z. Bahreldin; Amira O. S. Osman. n.d.. Architecture in Sudan 1900-2014: An Endeavor Against the Odds. Five-page modified article; publication date not established; title period 1900-2014 is not a publication date.
- KND-D9473A99EF16FA72 - Omer S. Osman; Amira O. S. Osman; Ibrahim Z. Bahreldin. 2011. Architecture in Sudan: The Post-Independence Era (1956-1970). Focus on the Work of Abdel Moneim Mustafa. Docomomo 44, 2011/1, 77-80; four article pages plus notice; 2005 issue 32 is only a cited reference.
- KND-1F33308922B5C597 - Mohamed Babiker Ibrahim; Omer Abdalla Omer. 2014. Evolution and changes in the morphologies of Sudanese cities. Urban Geography 35(5), 735-756; DOI 10.1080/02723638.2014.919798.
- KND-179BC520900BAA82 - Nancy Um. 2011. Greenlaw’s Suakin: The Limits of Architectural Representation and the Continuing Lives of Buildings in Coastal Sudan. African Arts 44(4), Winter 2011, 36-51.
- KND-A6D2C63BE772B31B - Nancy Um. 2012. Reflections on the Red Sea Style: Beyond the Surface of Coastal Architecture. Northeast African Studies 12(1), 243-272.
- KND-2F73277713DA8575 - NILE Magazine. 2018. NILE Magazine, Issue 13, April-May 2018. 25-page local issue extract.
- KND-6ADA048DD0D6EEEF - Jean-Baptiste Gallopin. 2020. Bad company: How dark money threatens Sudan’s transition. European Council on Foreign Relations, 9 June 2020; Instapaper export October 2021.
- KND-9A10595152EA79E0 - Jonathan Tossell. 2020. Consolidating Sudan’s transition: A question of legitimacy. Clingendael CRU Policy Brief, February 2020.
- KND-3C2BFC83BF92A876 - Ali Abdel Gadir Ali; Ibrahim A. Elbadawi. 2004. Explaining Sudan’s Economic Growth Performance. AERC Working Paper 9, January 2004.
- KND-D59B427F6CBF2E7A - A. F. Mazz. 1982. Perspectives on the Sudan: Isolation at Home and Abroad. ACAS Background Paper Number 1, September 1982.
- KND-AC8D5EF6C8B528C6 - Jihad Mashamoun. 2021. Winners and Losers of Red Sea Politics in Sudan. African Arguments, 6 August 2021; publisher original confirms byline missing from print.
- KND-886C36C639716D95 - Ahmed Soliman. 2019. Sudan Stakeholder Dialogues: Options for Economic Stabilization, Recovery and Inclusive Growth. Chatham House Africa Programme briefing note, October 2019; foreword by Abdalla Hamdok.
- KND-99D8847794C41A37 - Republic of the Sudan. 2021. First Nationally Determined Contribution under the Paris Agreement. Updated October 2021.
- KND-4E1DFE1024FB627A - Caitlin N. Howarth; Kaveh Khoshnood; Andrew Marx; Nathaniel A. Raymond; et al.. 2023. Widespread Human Security & Humanitarian Conflict Impacts. Sudan Conflict Observatory, Report 01, 9 June 2023; recommended citation printed p2.
- KND-9C716EFB27D436CB - SOAS Centre of African Studies; Society for the Study of the Sudans UK. 2015. Agricultural Potential in the Sudans: Past Experience and Future Outlook. Seminar-series report, 7 December 2015; speaker Mohamed Al Nour Adam; chair Mawan Muortat.
- KND-34DCF07FE873C877 - United Nations Environment Programme. n.d.. Agriculture and the environment. Chapter 8 of Sudan Post-Conflict Environmental Assessment, printed 158-191; publication year not on excerpt.
- KND-FACB726356AC737B - Adam Welz. 2021. Are Huge Tree Planting Projects More Hype than Solution?. Yale Environment 360, 8 April 2021.
- KND-D8B257F94D79E765 - International Irrigation Management Institute (issuing body). n.d.. Irrigation Management in Sudan: Gezira Scheme. Technical Report No. 3; multiple chapter authors; terminal workshop recommendations dated 27 April 1994 are not publication date.
- KND-0F641A36D982639B - Elgilany A. Ahmed; Hamid H. M. Faki; Hashim A. Elobied. 2011. Potentiality of Organic Perennial Crops Farms in the River Nile State of Sudan. Journal of Science and Technology 12(4), December 2011.
- KND-F475E237AD4755B0 - Eugene Cooper. 2009. Sahel Rainfall and Conflicts. Sudan Studies Association Bulletin 27(1), March 2009, 8-19.
- KND-70C758DC7274F584 - Hind A. Elbashir; Mohamed A. Imam. 2010. Status Report on Fruits and Vegetables Production and Processing Industry in Sudan. 2010 AARDO Workshop on Technology on Reducing Post-harvest Losses and Maintaining Quality of Fruits and Vegetables, 168-179.
- KND-EDDAA14090A6BA70 - Eckart Woertz. n.d.. Arab Food, Water and the Big Gulf Landgrab that Wasn’t. Author manuscript for The Brown Journal of World Affairs; undated local version.
- KND-34D0C3BE8FD01225 - Muriel Mirak-Weissbach. 1995. The history of the Nile region. EIR 22(24), 9 June 1995; Special Report 19-27.
- KND-3AA07C8DF8CB8F11 - John A. Shoup. 2017. The Nile: An Encyclopedia of Geography, History, and Culture. ABC-CLIO, 2017; ISBN 978-1-4408-4040-1.
- KND-0F351AF3CE135C53 - Abdullahi Ahmed An-Na’im. 1988. Mahmud Muhammad Taha and the Crisis in Islamic Law Reform: Implications for Interreligious Relations. Journal of Ecumenical Studies 25(1), Winter 1988.
- KND-6EB5E69ABDA3C8F6 - Nadir A. Nasidi. n.d.. A Black Power in the Blue Nile: A Military History of the Funj Sultanate of Sinnār 1503-1821. Journal of Zaria Historical Research 5(2); year not printed in reviewed local copy.
- KND-734A0D9F9F332FD3 - S. F. Nadel. 1947. The Nuba: An Anthropological Study of the Hill Tribes in Kordofan. Oxford University Press, 1947; foreword by Hubert Huddleston.
- KND-25C89C8D423F4EC8 - Kanya Godde; Richard L. Jantz. 2018. Evaluating Nubian Population Structure from Cranial Nonmetric Traits: Gene Flow, Genetic Drift, and Population History of the Nubian Nile Valley. Wayne State Human Biology Open Access Pre-Prints 127, repository citation 2018.
- KND-2FD281C3AB7592D1 - Ulrike Nowotnick; Pawel Wolf; Florian Wöss; Saskia Büchner; Maren Minow. 2014. Hamadab: Urban living at the Nile in Meroitic times. Hamadab Archaeological Project booklet; Printed 2014.
- KND-8364DDC6631F8474 - Alex de Voogt. 2012. Máncala at the pyramids of Meroe. Antiquity 86 (2012), 1155-1166.
- KND-F23477304D0A60BB - Azhari Mustafa Sadig. 2010. The Neolithic of the Middle Nile Region: An Archaeology of Central Sudan and Nubia. Fountain Publishers, first published 2010; ISBN 978-9970-25-000-4.
- KND-845C17F8A281963F - Ahmed Al-Shahi. n.d.. Northern Sudanese Perceptions of the Nubian Christian Legacy. Undated chapter extract, printed31-39; starts with preceding Roger Just page30.
- KND-EE83B7C605D127AE - Joyce L. Haynes. 1992. Nubia: Ancient Kingdoms of Africa. Museum of Fine Arts, Boston, 1992; ISBN 0-87846-362-3.
- KND-1F38C63881A5D714 - Museum of Fine Arts, Boston; Denise Doxey (curator). 2018. Nubia: Treasures of Ancient Sudan. MFA traveling-exhibition prospectus, copyright 2018.
- KND-4CC942679CE56DAF - Larry Ross. 2013. Nubia and Egypt: 10,000 B.C. to 400 A.D. From Prehistory to the Meroitic Period. Edwin Mellen Press, copyright 2013; ISBN 978-0-7734-2646-7.
- KND-717002AF098431E2 - Maria Costanza De Simone. 2014. Nubia and Nubians: The ‘Museumization’ of a Culture. Leiden doctoral dissertation, defended 12 February 2014; repository handle 1887/23598.
- KND-9EEC86B61DE0B3FA - Janice W. Yellin. n.d.. Nubian Elite and Popular Religion during the Napatan and Meroitic Periods. 19-page manuscript; note identifies final illustrated chapter Nubian Religion in Ancient Nubia (2012), 125-144.
- KND-2E5A6B64F2AF79B9 - David Roberts. 1993. Out of Africa: The superb artwork of ancient Nubia. Reprinted from Smithsonian, June 1993, 90-96, 98, 100.
- KND-C2E39047F8AEEB9F - Elsa Yvanez. 2010. Rock Inscriptions from Semna and Kumma: Epigraphic Study. Sudan National Museum/NCAM, SFDAS, Khartoum 2010.
- KND-9F726BE3A9C2E896 - Cornelia Kleinitz. 2012. Rock art at the Fourth Nile Cataract: An overview. Africa Praehistorica 22, 33-50, plates 9-11; conference 2006, published 2012.
- KND-5FA6E2D6CC5B1571 - Ahmed Hamid Nassr. n.d.. Sennar Capital of Islamic Culture 2017 Project: Preliminary results of archaeological surveys in Sennar East and Sabaloka East. Sudan & Nubia article, 146-152; 2017 in project title is not publication date.
- KND-38E4C42F995DC1C5 - Dan'el Kahn. 2018. Some Thoughts on Egyptian Elements in Kushite Religion and Rituals. Across the Mediterranean - Along the Nile, volume 1; Budapest/Archaeolingua 2018.
- KND-4E02E73E642C07C0 - Erin Ingram. 2017. Tattooing and Scarification in Ancient Nubia: Teenage Rebellion or Cultural Norm?. Beitrage zur Sudanforschung 12, Wien 2017.
- KND-61E0D3E6DFD0A7C4 - Charles Bonnet. 2019. The Black Kingdom of the Nile. Harvard University Press; Huggins Lectures; foreword Henry Louis Gates Jr..
- KND-5AD765CA69CF9E71 - Ian Shaw; Paul Nicholson. 2002. The British Museum Dictionary of Ancient Egypt. AUC Press pocket edition first published in Egypt 2002; original1995, paperback1997.
- KND-9B848E8F0C54D89C - Effrosyni Zacharopoulou. 2016. The Emergence of the State of Nobadia and the Byzantine Policy. Graeco-Africana et Afro-Byzantina, Johannesburg2016; conference2014 is not publication date.
- KND-C08E27E545F65648 - Lewis Peake. n.d.. The Invisible Superpower: Review of the Geopolitical Status of Kushite (Twenty-fifth Dynasty) Egypt at the Height of its Power and a Historiographic Analysis of the Regime's Legacy. PAM Supplement Series2.2/2,465-476; year not established from local offprint.
- KND-C69AA58886CF82C8 - National Geographic Society. n.d.. The Kingdoms of Kush. Website print;17February2024 printing timestamp is not publication date.
- KND-DF4E6FB7A9379353 - Leonard Cottrell. 2005. The Lost Pharaohs. Kegan Paul, this edition2005; ISBN0710310471.
- KND-231EBEBD1489E3E2 - Muhammad Shamsaddin Megalommatis. n.d.. The Meroitic Ethiopian Origins of the Modern Oromo Nation. Edited online version referring to American Chronicle and a10-page2005 OSA proceedings paper; local version date unresolved.
- KND-907D6DB71F2C0EF1 - Artur Obluski; Wlodzimierz Godlewski; Wojciech Kolataj; Stanislaw Medeksza; Cristobal Calaforra-Rzepka. 2013. The Mosque Building in Old Dongola: Conservation and revitalization project. Polish Archaeology in the Mediterranean22 (Research2010),248-272; published2013.
- KND-E32DAE656450F497 - David N. Edwards. 2004. The Nubian Past: An Archaeology of the Sudan. Routledge, first published2004.
- KND-B9755BE659E32E7E - Bruce B. Williams; Lisa Heidorn. n.d.. The OI and Nubia. Discovering New Pasts: The OI at100; chapter358-387; container year not printed in selected extract.
- KND-6124F9E8950E2CF1 - Marc Maillot. 2014. The Palace of Muweis in the Shendi Reach: A Comparative Approach. The Fourth Cataract and Beyond, Peeters2014,783-795; editors Julie R. Anderson/Derek A. Welsby.
- KND-506035F8EF62A178 - Betty Winkelman. 2013. The Royal Cemeteries of Nubia. Ancient Egypt, December2013/January2014,34-42; issue spans two years.
- KND-CBFA6C54FAA60A90 - Claude Rilly. 2013. The Sudan National Museum in Khartoum: An illustrated guide for visitors. SFDAS2013; design/English translation Solene Marion de Proce; Arabic translation Abdelrahman El-Siddig.
- KND-A257451E31C8A648 - Carmen Ting; Jane Humphris. 2017. The technology and craft organisation of Kushite technical ceramic production at Meroe and Hamadab, Sudan. Journal of Archaeological Science: Reports16,34-43.
- KND-8ABA7024E32552C2 - Azza Mustafa Babikir Ahmed. 2020. City-making in Africa: Urban planning and the reconfiguration of Tuti Island, Khartoum, Sudan. Middle Class Urbanism Working Papers1/2020; series editors not article authors.
- KND-4BF5E95911C7D6E9 - Gamal M. Hamid; Ibrahim Z. Bahreldin. n.d.. Khartoum2030: Towards An Environmentally-Sensitive Vision for the Development of Greater Khartoum, Sudan. Undated local26-page paper;2030 is planning horizon,2009 cited masterplan not publication year.
- KND-C62258610939C80B - African Union. n.d.. Towards the African Integrated High Speed Railway Network (AIHSRN) Development. 13-page institutional paper; local publication year not established.
- KND-A85793B2CE5039C2 - Lycopodium. 2020. Block14 Gold Project, Republic of Sudan: NI43-101 Technical Report. Report14September2020, effective31August2020; same bytes as other Block14 alias.
- KND-9E10B30278742721 - Nile Basin Initiative, Socio-economic Development and Benefit Sharing Project. 2009. Socio-economic Development and Benefit Sharing in the Nile Basin. First published2009; institutional report, not McManus/Butler authorship.
- KND-FC8F82DCC8635E3D - MUSB OSMAN EBRAHIM; Hesham Aldeen Alkhar. n.d.. Uranium in Sudan. Ministry of Minerals/Geological Research Authority of Sudan presentation; names reproduced exactly as visual cover.
- KND-270A3B8DA5926161 - Mohammed Alamin. 2021. Sudan Plans $640 Million Railway Revamp as It Relinks With World. Bloomberg,16July2021;2023 copyright footer not article date.
- KND-2284BB29A7ED966B - International Bank for Reconstruction and Development, Department of Technical Operations. 1958. Appraisal of the Development Program of the Sudan Railways, Sudan. TO-180a,7July1958; terminal map IBRD475 May1958.
- KND-61243063459F72E4 - Laura Mann. 2014. Wasta! The long-term implications of education expansion and economic liberalisation on Politics in Sudan. Review of African Political Economy41(142),561-578; DOI10.1080/03056244.2014.952276; accepted manuscript.
- KND-FEE381C366AAE879 - United Nations Conference on Trade and Development. 2015. Investment Policy Review: The Sudan. United Nations2015; same file as another catalog alias.
- KND-00F1B6C35233031C - International Conference on the Great Lakes Region. 2006. Southern Corridor (Great Lakes Region Railway) Project: Prefeasibility Study - Terms of Reference. Project3.3.4,March2006 amended August2006.
- KND-5871FD387DB946CD - Andreas Jacobs. 2006. Reformist Islam: Protagonists, Methods, and Themes of Progressive Thinking in Contemporary Islam. Konrad Adenauer Stiftung Working Paper/Documentation155/2006,September2006.
- KND-707213226FE87456 - James Fearon; David Laitin. 2006. Sudan (SudanRN1.2). Stanford random narrative accompanying civil-war-onset statistical analysis; draft5May2006.
- KND-67CF72C1F807F23E - Hassan El Menyawi. 2012. Same-Sex Marriage in Islamic Law. Wake Forest Journal of Law & Policy2(2),375-531; own running header confirms2012.
- KND-F7B8B8FE0A64F096 - Government of Sudan. 2005. The Draft Constitutional Text. 16March2005 draft.
- KND-A1918217ACA02098 - Arnab Hazra; Raphael Huser. 2020. Estimating high-resolution Red Sea surface temperature hotspots, using a low-rank semiparametric spatial model. Manuscript dated20October2020; final publication date not claimed.
- KND-6D5FA54101C950F5 - Embassy of the Netherlands, Khartoum; Ministry of Foreign Affairs of the Kingdom of the Netherlands. 2021. Call For Concept Notes on Investing in the Rain-Fed Agriculture in Sudan. News item30August2021; deadline30September2021.
- KND-6982545D38B707A2 - Central Intelligence Agency. 1982. Sudan: Agricultural Problems. NESA82-10501,September1982;2007 release date not publication date.
- KND-F9290BACADBEDDC1 - Jamie Stokes (editor). 2009. Encyclopedia of the Peoples of Africa and the Middle East. Infobase2009; ISBN9780816071586; ebook9781438126760.
- KND-D31F421E373C8FE4 - Solange Ashby. 2016. Calling Out to Isis: The Enduring Nubian Presence at Philae. University of Chicago doctoral dissertation,June2016.
- KND-F8DA4E6410BF3BEB - Republic of Sudan. 1998. Constitution of the Republic of Sudan. English text, entered into force1July1998 as printed on first page; historical text.
- KND-8EFC63913B10B006 - Hadi Salehi Esfahani; M. Hashem Pesaran. 2008. Iranian Economy in the Twentieth Century: A Global Perspective. March2008 manuscript.
- KND-06048E3D9E6F1921 - Akram Ahmed Khalifa. 2011. The Construction Industry of Sudan: Potentials and Challenges. Workshop paper,29May2011; Arabic visual byline: Akram Ahmed Khalifa.
- KND-39DB991AC771E4B0 - Iman Sharif. 2022. Development Economics in Sudan: The Ten-Year Economic and Social Plan,1961-1970. Sudan Studies for South Sudan and Sudan66,July2022,29-38.
- KND-E2A5B0F0EEB021E2 - Emanuel Beska. 2019. Muhammad Ali's Conquest of Sudan (1820-1824). Asian and African Studies28(1),30-56.
- KND-78660C204A873BBC - A. C. S. Peacock. 2012. The Ottomans and the Funj Sultanate in the sixteenth and seventeenth centuries. Bulletin of the School of Oriental and African Studies75(1),87-111; DOI10.1017/S0041977X11000838.
- KND-A137F36299CAF34C - Robert O. Collins. 2008. A History of Modern Sudan. Cambridge University Press2008; frontmatter extract.
- KND-7C074AC6E78470A6 - Anna C. Rader. 2012. Overcoming the Past: War and Peace in Sudan and South Sudan. Chapter3 in On The Fault Line: Managing Tensions and Divisions Within Societies; Brenthurst Foundation2012.
- KND-06562285C249ABA2 - Steffen Wenig. 1978. Africa in Antiquity: The Arts of Ancient Nubia and the Sudan, VolumeII: The Catalogue. Brooklyn Museum1978; translators Diana S. Peters/Charles M. Stern; editors Sylvia Hochfield/Elizabeth Riefstahl.

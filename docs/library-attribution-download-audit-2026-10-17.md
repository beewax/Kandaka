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

# Library acquisition verification — 1 November 2026

## Authorization and recovered state

The owner's “do your thing” followed the three-source Library recommendation in chat 6a8dae62-7ad8-83ea-afbd-d464d8bfe5e2; the current continuation explicitly authorizes verified metadata/link entries, commit and deployment. This covers Library records only. Article-specific approvals, bodies, covers, draft flags, dates and release spacing remain unchanged.

Latest main was fetched before work. The three records were already committed in 8ce2c618a327decf2b965c9fd5ac06f0cbd1444f on 31 October and independently found live once each in both languages. No new catalogue records are inserted in this continuation. The count is 558: 557 after the 26 October additions, minus two reconciled duplicates in 2a1ded8, plus these three. The introduction incorrectly still said 557. This change corrects both introductions, completes bibliographic metadata, refines the bilingual Bashir summary and brings the inventory/source validation list up to date.

## Source verification and reading limits

- Ahmed Hussein Abdelrahman Adam, *Pedagogy Under Fire: Teaching Archaeology with WhatsApp during Sudan’s Civil War*. Public Humanities 2 (2026), e95; published 18 June 2026. [Publisher/DOI](https://doi.org/10.1017/pub.2026.10190). Publisher HTML, teaching/assessment account and limitations checked; the earlier research watch records full HTML reading. First-person emergency teaching account, not a controlled outcomes evaluation. Publisher explicitly states CC BY 4.0. No PDF or images mirrored.
- Mohamed Bashir, *Pluriversal Pasts: Decolonising Archaeological Practice in Sudan through the Integration of Folklore and Community Epistemologies*. Cambridge Archaeological Journal, First View, pp. 1–13; published 29 September 2026. [Publisher/DOI](https://doi.org/10.1017/S0959774326100742). Full HTML is available. Abstract, metadata and selected methodology passages checked; complete methods/results review remains pending. The revised summary attributes the argument to Bashir and recognizes community knowledge as co-production, rather than silently substituting Kandaka's chronological-validation recommendation for the author's position. Publisher explicitly states CC BY 4.0; third-party image rights not audited. Link only.
- UNICEF Sudan, *Humanitarian Mid-Year Situation Report No. 44*, 1 January–30 June 2026; publisher release month August 2026. [Official record](https://www.unicef.org/sudan/reports/unicef-sudan-humanitarian-mid-year-situation-report-2026). Official PDF WASH sections checked: 120 urban facilities and 2.2 million reached; Nyala is included, not additive. Programme monitoring and sector capacity assessment, not independent proof of continuous water service. Exact release day and reproduction licence not verified; no PDF or images mirrored. Other report sectors were not comprehensively reviewed.

The catalogue contains substantive original English/Arabic summaries, localized author names, publication dates and origin links. The source report/papers remain in their original language; the Arabic summaries are not full translations.

## Duplicate checks and collection boundaries

Fresh direct production downloads returned 558 cards in each language, each selected source once, with exact matching descriptions. The repository export `My books.csv` has 151 records; title/DOI scans found none of these sources. The central `CATALOG.csv` has 4,037 records and no matching source. Read-only query of live `D:/New Caliber Library/metadata.db` found 4,035 books and no matching titles or DOI identifiers. Those collections have different scopes; their counts are not interchangeable. Existing `library_inventory.csv` had 521 rows and none of the three; adding the three metadata/link rows makes 524. It is not a complete replacement for the 558-record live catalogue. No Calibre or central-library originals or catalogues were changed.

## Rewind Forward — later candidate, no catalogue insertion

[NACP project page](https://na-cp.org/en/project/rewind-forward): search-index content describes a 27-month Cimatheque/Sudan Film Factory preservation/training project; fresh direct retrieval timed out in the web reader and returned HTTP 403 locally. Treat this as indexed project evidence, not a newly completed direct-page review. [Arab Film Network, Mohammad Khatib, 3 September 2026](https://www.arabfilmnetwork.com/2026/09/03/sudan-film-factory-advances-film-production-and-preserves-sudanese-cinematic-memory/) reports recovery of six documentaries and twelve shorts from 2010/2012 training programmes, being documented/digitized. This is sector reporting, not an independent audit. No budget, completed restoration count or film distribution rights verified. Keep as a later link-based research candidate; do not conflate recovery, digitization, restoration and rights clearance.

## التحقق بالعربية

المصادر الثلاثة موجودة بالفعل مرة واحدة في كل لغة منذ الالتزام المؤرخ 31 أكتوبر. العدد الصحيح 558 بعد حذف مادتين مكررتين وإضافة المصادر الثلاثة. صُححت مقدمة المكتبة، واستُكملت البيانات، ونُقح ملخص بشير مع التصريح بأن المراجعة جزئية. لا توجد مطابقة في تصدير كاليبر أو قاعدة بياناته الحية. بقيت مبادرة «الرجوع إلى الأمام» مرشحاً للبحث اللاحق بسبب حدود الوصول والتحقق من النتائج والحقوق. لم تُرفع ملفات أو صور، ولم يتغير اعتماد أي مقال أو موعد نشره.

## Validation and publication

Production build, rendered bilingual validation, cover audit and subsequent production verification are recorded after completion below. No browser window or Chrome session was changed.


### Completed verification

Release commit: f4594bd4d28ceeafd58692c8c3e5c3eb67051a45. Netlify production deployment: 6ae822a6b2640cc1bd3f339c, state ready, matching commit. Published 2026-11-02T05:42:56.906Z / 1 November 2026 at 23:42:56.906 CST (America/Chicago). Independent verification completed 2026-11-02T05:43:28.099298Z / 1 November at 23:43:28 CST.

Hugo 0.160.0 production build completed successfully (4,348 pages across languages; local build 495.309 seconds). Existing bilingual validator passed against both rendered Library pages: 558 cards, 17 required source records, exact localized titles/descriptions/authors and one canonical May 2025 World Bank record. Cover audit passed against 3,609 Markdown files, run from repository root. Fresh HTTPS downloads of https://kandaka.com/library/ and https://kandaka.com/ar/library/ independently confirmed 558 cards each, each selected source exactly once, exact titles/authors/summaries/source links, and corrected count/date introductions. None of the three has a download/mirrored-file field. Local machine-readable live evidence: deliverables/research/library-acquisition-live-2026-11-01.json in the project workspace.

The release diff touches only Library data/indexes/inventory, its existing validator, this audit and the master record. No article content, approval state, draft flag, cover, release metadata or automation changed. Netlify's existing build command refreshes news as usual; those generated news changes are separate from article editorial releases. This evidence-only follow-up commit skips a further Netlify build.

تم النشر والتحقق المستقل في 1 نوفمبر 2026 الساعة 23:43 بتوقيت شيكاغو الشتوي. اجتاز البناء وفحص الأغلفة والتحقق من صفحتي المكتبة المنشورتين الاختبارات؛ العدد 558 في كل لغة، والمصادر الثلاثة موجودة مرة واحدة مع مطابقة العناوين والمؤلفين والملخصات والروابط. لا تغيير في اعتماد المقالات أو مسوداتها أو تسلسل نشرها.

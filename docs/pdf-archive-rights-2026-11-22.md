# Kandaka PDF archiving and rights checks — 22 November 2026

**Completed storage outcome: five new, publicly verified PDF files; zero new bibliographic records.** These upgrade five existing entries in the 579-record Library. Catalog deployment/live button verification is recorded separately after observation.

## Eight-item queue outcome

| Existing source | Original file / rights result | Outcome |
|---|---|---|
| Ahmed Hussein Abdelrahman Adam, *Pedagogy Under Fire*; DOI10.1017/pub.2026.10190 | Cambridge original13 pages; CC BY4.0; three figure captions and rights lines screened, no restrictive third-party exclusion found | Archived; public bytes match original |
| Lemos, Howley, Shinn and Abdu Rabo, *Crafting power in Kush*; DOI10.15184/aqy.2026.10434 | Cambridge original20 pages; CC BY4.0; ten figures credited to authors, no separate exclusion found | Archived; public bytes match original |
| Abdalhady Ahmed Abdalla et al., sorghum target product profiles; DOI10.3389/fsufs.2026.1846994 | Frontiers original17 pages; CC BY4.0 hyperlink; two original framework/method figures, no separate restriction found | Archived; public bytes match original |
| Mustafa and Hassan, Omdurman urban heat chapter; DOI10.5772/intechopen.1016887 | IntechOpen original19 pages; explicit CC BY4.0 on printedp17; nine captions screened, no separate exclusion found | Archived; public bytes match original |
| Statkus et al., lustre ceramics; DOI10.3390/min16070713 | MDPI publisher-CDN original15 pages; first-page CC BY statement read and visually inspected; MDPI rights policy identifies4.0; eight captions screened, map prepared specifically for this publication, no separate exclusion found | Archived; public bytes match original |
| Mohamed et al., Suakin regeneration; DOI10.3389/fbuil.2026.1868485 | Valid original downloaded:31 pages,10,686,088 bytes, SHA2568481e808268adc9fe0d572859b6f5402d7b55a85125f48210547fc2e7e42b962. Article CC BY, but24 captions include Google Maps, architectural plans, press photographs and earlier publications without independently established downstream rights | **Held for third-party-rights clarification**; official article link retained. No allegation that publication was unauthorized |
| Mohamed Bashir, *Pluriversal Pasts*; DOI10.1017/S0959774326100742 | Valid original downloaded:13 pages,1,109,585 bytes, SHA256e94c9c62b995632c31b76ca7f6e408ec6c1088c62e69bf42082fbc14e9b1f224. Article CC BY4.0; seven figures include adaptations from Crawford1951 and other credited material; scope for downstream reproduction not established independently | **Held for third-party-rights clarification**; DOI retained. Downloaded copy has an access stamp; it was not publicly mirrored |
| Mohammed et al., Nile flood susceptibility; DOI10.1038/s41598-026-58194-7 | Web publisher PDF text available, but local Nature and Springer PDF routes returned HTML rather than PDF bytes; `%PDF-` verification failed | **Held for valid original retrieval**; no HTML uploaded under a PDF label |

Seven valid originals acquired locally from publishers; five cleared and archived. The two locally held files are not public Kandaka downloads. The two source-linked reports added21November (UNDP digital literacy and World Bank October MPO) remain unmirrored: their document-specific redistribution/third-party terms are still unconfirmed. They are outside the eight-paper batch, and are not counted among the five PDFs.

## File integrity, rights evidence and storage

Full exact author/title/DOI/source URLs, bytes, page counts, SHA256 and destination keys are in `docs/pdf-archive-manifest-2026-11-22.json`. All five uploaded files are **unchanged publisher originals**; licence and credits remain inside each file. Their first pages were visually inspected; all pages parse as PDF. This was a bibliographic, integrity and rights audit, not a claim that every scholarly argument was fully read or independently validated. Prior bilingual source-critical summaries retain their reading limits.

MDPI licence-version evidence: [MDPI rights policy](https://www.mdpi.com/authors/rights?authAll=true), read alongside the individual original's first-page CC BY statement. That statement does not specify a different version. The manuscript's first page identifies7July2026, Minerals16,713 and exact DOI. The publisher-CDN route succeeded after the main download endpoint403. IntechOpen's citation-pdf-url endpoint supplied its official PDF; a file-path timestamp is not treated as publication date. One initially guessed Cambridge filename404 was discarded; actual HTML `citation_pdf_url` metadata supplied the correct file. No guessed locator is presented as verified evidence.

All originals retained locally at `D:/Kandaka-builds/pdf-archive-20261122/`. No Calibre originals, central reference-library records, source datasets or synced project files changed. No individual figure, map or sensitive site-coordinate export made. A caption screen is not a licence for separate extraction or reuse of an image.

Destination: **kandaka-library only**, public base `https://pub-0c3bb637d5f54b239fe4a4ef9b08bfe3.r2.dev`. Authenticated bucket inventory and exact DOI/key prefixes were checked before writing; no matching keys were present. Deterministic DOI+SHA256 keys used. No existing object overwritten, moved or deleted. An initial13-page upload was publicly downloaded and hash-verified before the remaining four uploads.

The repository's safe explicit-manifest uploader ran **dry-run only** and passed for all five files. Actual binary transfer used installed Wrangler4.112.0 with the already authenticated **OAuth** session, confirmed by whoami; no legacy embedded S3 keys or uploader secrets were read, printed or reused. This avoids the previous source-to-storage fetch blocker without creating a temporary Worker. The separate exposed-key revocation/rotation task remains unresolved; successful OAuth uploads do not prove those old keys were rotated. No unrelated service credentials or configuration changed.

Cloudflare connector subsequently confirmed all five object keys, correct byte sizes and `application/pdf`. Independent public HTTP GET returned200 and application/pdf for each; downloaded SHA256 and page counts match originals. Total new archive: **84 pages,30,142,442 bytes**. No storage claim based solely on an upload success message.

## Catalog and publication boundary

Existing five records gain verified `download`, `original_pdf_url`, CC BY4.0 attribution and stored-on metadata, localized download labels, and a short bilingual archive note. Official article/DOI `source` remains. Format/status maps and matching inventory rows updated. All other catalog records preserved; no duplicate source added. Suakin/Pluriversal rights holds and flood retrieval hold are recorded on the existing entries without deleting their links.

Only Library data/inventory, acquisition documentation, `LIBRARY_SOURCES.md` and master continuity record may change. **No editorial article, cover, article approval, publishing cadence or automation changes.** Article publishing belongs to the other chat.

The normal hosted site build and exact EN/AR live verification are required after catalog commit. Their actual commit, deploy ID and publication time are recorded in the publication receipt; a stored file alone does not establish that a Library button has deployed.

**العربية:** حُفظت خمسة ملفات PDF جديدة من أصل ثمانية مرشحين، دون إضافة سجلات مكررة؛ يبقى الفهرس٥٧٩ مادة. تحقق تنزيل الملفات الخمسة ومطابقة بصماتها وعدد صفحاتها للأصول. بقيت سواكن و«ماضيات متعددة» معلقتين لتوضيح حقوق الصور والخرائط المعاد استخدامها، وبقي بحث الفيضانات معلقاً لعدم استرجاع أصل PDF صالح. لم تُرفع صفحات HTML على أنها ملفات، ولم تتغير المقالات أو مواعيد نشرها. تقريرا٢١نوفمبر ما زالا رابطين رسميين دون نسخ لعدم حسم حقوق إعادة التوزيع.

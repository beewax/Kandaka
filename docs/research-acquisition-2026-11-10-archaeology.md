# Archaeology acquisition continuation — 10 November 2026

## Baseline and duplicate screen

Continues the owner-authorized research acquisition and actual article integration workflow. Fresh main `b9be2add3250f15c25109269b5e59e15e80b5a6f`. Checked current 575-record `data/library.json`, `LIBRARY_SOURCES.md`, `library_inventory.csv`, 151-row repository Calibre export `My books.csv`, master workplan/backlog, prior research/acquisition logs and relevant article contents before selecting additions. Exact titles, DOI and source URLs searched across the checked Markdown/JSON/CSV corpus; no matches for the two additions. Live Windows Calibre and external central catalogue remain inaccessible; duplicate status against those is provisional.

Existing PNAS/Napata Nile dynamics, Sanam faience, SUM, digital heritage, Pluriversal Pasts and isotope portal were identified and not re-added. Newer already-published cool-roofs work, existing reform drafts, prior eight article updates and release cadence preserved.

## Two acquisitions — 575 → 577

### 1. Nasreldein and colleagues — Old Dongola food-storage study

Exact full title/authors/citation, publication date 26 April 2025 and DOI `10.1007/s10437-025-09622-y` are in the new catalogue record and `archaeology-new-records-2026-11-10.json`. Original journal issue: African Archaeological Review 42, 259–290, 2025. Publisher article: https://link.springer.com/article/10.1007/s10437-025-09622-y ; original PDF: https://link.springer.com/content/pdf/10.1007/s10437-025-09622-y.pdf . Sudanese leadership is supported by the publisher's author-contribution statement and University of Gezira affiliation, not assumed from author order.

**Review:** abstract, methods, selected results/discussion, conclusion, data statement and rights sections reviewed in publisher HTML and verified original PDF. Not every page or reference read; no replication, sample examination or raw-data download. No unqualified complete-reading claim.

**Rights:** CC BY 4.0 verified in the article and original file; third-party items included unless otherwise credited. All eight figure captions screened; no separate exclusion found. Attribution and DOI retained, PDF unchanged. No separate extraction of figures, plans, coordinates or raw-data tables. This is a scholarly article archive, not a new public archaeological location dataset. Publisher data statement says raw data require a request and may require repository consultation; no claim to hold those data.

**Acquisition:** original PDF downloaded successfully, `%PDF` signature, 3,711,355 bytes, 32 pages, SHA256 `72bb5c63461bf8fd96dfdfb844d7cff7a3b85c3fbc88e843fde7bec1ca2b09fc`. First page rendered and visually inspected. Stored in authenticated Kandaka R2 bucket `kandaka-library`, key `2025/nasreldein-et-al-2025-nubian-diet-dongola.pdf`. Public download verified byte-identical and 32 pages:

https://pub-0c3bb637d5f54b239fe4a4ef9b08bfe3.r2.dev/2025/nasreldein-et-al-2025-nubian-diet-dongola.pdf

A temporary single-object uploader accepted only this exact byte count and SHA256 and used conditional creation. It was removed after upload; authenticated lookup confirmed deletion/404. No existing Worker or other bucket changed. Format/status maps and one inventory row added.

### 2. Babiker — Hamadab urbanism

Author: Abdelmonim Ahmed Abdalla Babiker, International University of Africa. Full title/citation in catalogue. Publisher: https://onlinejournals.uofk.edu/JFA/en/article/view/2066 ; original PDF: https://onlinejournals.uofk.edu/JFA/en/article/download/2066/1857/1958 . No DOI identified.

**Dates:** journal issue/PDF running header says January 2025, issue 52/2; portal publication date is 11 January 2026. Record preserves both. The portal date is not independently established as a digitization date. This is newly found to Kandaka, not an assertion of a newly conducted excavation.

**Review:** full nine-page article text read; first page visually inspected; no independent reanalysis or figure-by-figure visual audit. Source-critical summaries distinguish an illustrated account from an excavation dataset or modern performance evaluation. Broad first/complete-map and historical environmental claims are not adopted as independently established results.

**Acquisition/rights:** original downloaded successfully, 979,373 bytes, nine pages, SHA256 `f01246f1408840f27dd4ffe2f3bba7f3edae3a8016831bc6322cf01849fb1ff3`. Checked PDF, article page and submissions policy; no explicit redistribution licence confirmed. Maps/photographs and earlier reproductions have unresolved third-party scope. **No Hamadab PDF stored in Kandaka.** Catalogue links publisher article/PDF.

## Earlier blockers resolved or retained

- **Isotope portal:** full Terms of Use reached at https://isotopes.pcma.uw.edu.pl/legal/terms . Academic/research purpose and citation are specified; commercial purpose needs authorization. No open redistribution grant found. Catalogue rights/review fields updated; no account, dataset export or media copied. Direct page says last updated August 2026, whereas a search excerpt said September; discrepancy recorded, not used as a launch date.
- **Khor Rafit:** both institutional original `https://researchers.mq.edu.au/files/517562235/Publisher_version.pdf` and publisher `/doi/pdf/10.1080/0067270X.2025.2586366` retried with normal local client: HTTP 403/HTML, not valid PDFs. Publisher full-HTML retrieval also returned 403. Existing abstract-only record remains; no full-reading or archive claim and no duplicate.
- **Hamadab source:** public download works; rehosting blocked by rights uncertainty, not by transport. Publisher link retained.
- Existing 2026 PNAS/Napata and faience records remain catalogued; this pass did not reacquire or rehost their PDFs. Do not count them as new discoveries.

**Counts this pass:** two valid originals downloaded; one archived in Kandaka; one publisher-linked without storage; two failed Khor Rafit PDF attempts. Total newly archived originals across the two 10 November passes: two (earlier multi-hazard paper plus this food-storage paper). No copyrighted media rehosted without a licence.

## Actual editorial integration and candidate advanced

Appended explicit dated English/Arabic additions to the existing food-history article and urban-planning strategy. Original bodies are byte-for-byte prefixes; dates, draft flags, covers and release cadence unchanged. No Karanog/Dongola protected package edited. One bilingual research candidate advanced in `household-history-candidate-2026-11-10-en-ar.md`; research/outline only, no new article published.

Hamadab's relevance to current planning is a question for local testing, not a proof of mud-brick performance or a construction specification. A modest skills/building survey and repairs form the proposed quick win; measured materials work and local training the five-year task; larger reconstruction remains long-term. Costs and observed modern treatment outcomes are unavailable. Cheaper comparator: inspect and repair existing fabric before a new demonstration district. Skills: Sudanese builders, engineers, conservators, universities and residents; risks: historical analogy, flood damage, loss of local knowledge and unfunded upkeep. These are Kandaka's editorial adaptations, not implemented-project results supplied by the historical paper.

## Validation and commit/deployment boundary

Existing catalogue and cover checks run; full Hugo build and rendered bilingual checks completed before release. `archaeology-acquisition-checks-2026-11-10.json` records article-prefix hashes; `archaeology-render-checks-2026-11-10.json` records rendered checks. The containing Git commit is the research receipt; production commit/deploy/live results are recorded in a separate publication receipt after successful verification. No build is described as a live deployment.

## Next actions

Obtain more independent household excavations and compare their methods/chronologies before drafting the new article. Seek rights clarification only through separately authorized outreach; none sent here. Revisit Khor Rafit only through a lawful available original or confirmed access route, rather than repeatedly downloading its error page. Live Calibre/central-catalogue access remains outstanding. Continue practical local-construction, museum and cultural-industry evaluations on the next broad pass, with costs and maintenance scope where actually reported.


## 10 November 2026 — archaeology continuation deployed and verified

Commit `484eb9f91d7615ad1b5d40617296f8008eb39864` deployed as Netlify `6af3402c14fabc3b10a361e8` at 16:04:16.530 UTC / 10:04:16 CST. All four updated English/Arabic article pages and both Library editions returned HTTP 200 with the expected evidence; both libraries contain 577 cards and both new source links. Original 32-page food-storage PDF archived in Kandaka and public bytes/hash verified; Hamadab linked only because rights unclear. Isotope commercial-use restriction recorded; no data export. Local Hugo build, 4,050-file cover audit, original-prefix preservation and exact 15-file remote-byte checks passed. No new article published; household-history candidate remains research-only. Full receipt: `docs/archaeology-publication-2026-11-10.json`. Remaining blockers are live Calibre/central catalogue access, Khor Rafit access/rights and additional independent household/construction evaluations.

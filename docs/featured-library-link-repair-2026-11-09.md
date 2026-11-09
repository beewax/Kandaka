# Repair the three featured Library links — 9 November 2026

Owner explicitly requested fixing the three `File unavailable` cards. This release repairs exactly three existing records and matching inventory rows; it does not add books or audit the rest of the catalogue.

## Storage and source checks

Fresh public GETs of all three old `pub-a5e3…` URLs return 401. The 24 October inventory lists matching objects in the separate Nile bucket and none in Kandaka; that inventory is historical, not a fresh full-bucket inventory. Fresh GETs of the same keys at Kandaka's documented public prefix return 404. No bucket permissions, credentials, objects or source originals were changed. Existing environment-based uploader and source records were consulted; no compromised embedded credentials were used. Central-reference catalogue title queries returned no matching records; no claim of exhaustive local-content search or full-book reading.

Working replacements:

| Existing record | Verified replacement | Verification / attribution |
|---|---|---|
| Historical New Sudan Penal Code 2003 | https://www.ecoi.net/en/file/local/1286840/1504_1216568485_469e1f0a2.pdf | HTTP 200, `application/pdf`, PDF signature, 449,647 bytes, 125 pages; title page/issuing body visually checked. SHA-256 `ed5c5b362b96ce5b32122f81b27ae376bff40feaf03fd83896db08c0ae26e299`. IHRDA's archival copy independently returned identical bytes. Refworld/ILO automated requests returned 403, so they were not selected as the repaired link. This is a historical text, not a current-law assessment. |
| Smarthistory Naga pylon essay | https://smarthistory.org/pylon-nubian-lion-temple-naga/ | Normal browser loaded the complete original article after automatic JavaScript security verification; no CAPTCHA interaction/bypass. Byline and expanded publisher citation confirm Stuart Tyson Smith, 8 February 2023. Automated GETs return 403, which is not represented as a verified PDF or a missing public article. Labelled `Read original article`. |
| Kerma et Méroé lectures | https://kerma.ch/documents/Publications_PDF/Cinq_conferences.pdf | HTTP 200, `application/pdf`, PDF signature, 1,620,431 bytes, 55 pages. Cover/author/colophon pages visually checked. SHA-256 `9546760139baed1d94028e2c1a95c95e7e5b700d7948c76bff9fb05cfeff2002`. French PDF; authors Charles Bonnet, Matthieu Honegger, Patrice Lenoble, Claude Rilly and Vincent Rondot, replacing the incorrect Donna Kornhaber attribution. Colophon January 2006; legal deposit 2005, while the publisher's catalogue describes the work as 2005. Edition distinction recorded; no invented English/Arabic PDF. |

Kerma's PDF states all rights reserved. Links point to existing public institution/publisher copies; no PDF/image was rehosted or converted. Smarthistory's individual image credits remain at its source. No original Calibre files were modified.

## Catalogue repair

`data/library.json` remains 567 records, with exactly indices 194, 256 and 420 changed. Matching title/author/URL inventory rows are updated. Only the two freshly verified PDF URLs are added to the format/status maps as PDF/200; Smarthistory's browser-accessible HTML is explicitly labelled as an external article, without falsifying an automated HTTP status. Old storage-status entries remain historical evidence.

The three records retain their existing language-independent homepage IDs through optional `homepage_id` fields. Metadata/source repairs therefore do not shuffle these books out of this week's selection or force a new rotation. Selection cadence, next-update notices, article/photo/artwork data and all automations are unchanged. English/Arabic metadata and the French-edition label are aligned. Incorrect author attribution and uninformative legacy descriptions were corrected only for these records. Existing canonical dirty catalogue files are preserved; the fresh main checkout is the release source.

## Evidence and release

Source checks, downloaded reference-only PDFs, rendered first pages, publisher browser screenshot and exact before/after records are in project `tmp/featured-link-repair-2026-11-09/`: `source-checks.json`, `alternate-source-checks.json`, `record-changes.json`, `smarthistory-browser.png`, and PDF/front-page files. PDFs were inspected for identity/access, not read in full.

All 37 Python tests and nine Node tests pass, including the actual-Hugo permanent-identity/localization/JSON checks. Cover audit passed across 4,021 Markdown files. Full normal Hugo production build passed in 189,095 ms (1,185 EN / 3,612 AR pages), with the existing `.Site.Data` deprecation warning only. At 19:58:02 UTC, all four homepage/Library routes passed the complete 567-record metadata/URL/label/selection/date/control checks; runtime bytes unchanged. Exact repaired-card/source verification and deployment/live receipts follow separately. Catalogue count and all 564 unrelated records remain unchanged; CSV has exactly three row replacements, format/status maps exactly two new verified PDF entries.

## Published and independently verified

Release commit `617b7c45075955dcd237653c1a7ec6b2f75f9f94` is deployed to production. Netlify deployment `6af226510a24eaa59609b5be` reached ready with no error and published at 2026-11-09T20:01:26.475Z (14:01 CST).

Independent live checks completed at 20:02 UTC across English/Arabic homepages and full Library routes: complete catalogue metadata/control/selection/date checks and the exact three repaired identities, source URLs, labels and attribution checks passed. Both PDF sources were freshly downloaded again: HTTP 200, PDF signatures and byte hashes match the verified source copies. Evidence: `rendered-live.json` and `featured-live.json` in the evidence directory.

Browser checks confirmed all three working source buttons on the English and Arabic homepages with no File unavailable label. Screenshots: `repaired-live-en.png` and `repaired-live-ar.png`. Console entries returned by the reused tab predate deployment and belong to the earlier external source security challenge; no new Kandaka error was observed. Desktop views checked; no separate mobile viewport certification.

# Library source repairs — 20 October 2026

Two existing records repaired; all **545** records retained, including three newly approved additions on current main. No stored files, article releases or schedules changed.

- **Index 233 / KND-FACB726356AC737B**, *Are Huge Tree Planting Projects More Hype than Solution?*: official Yale Environment 360 HTML article, GET 200, title, Adam Welz byline, displayed 8 April 2021 date and full article ending verified. Source labels in both languages identify an article, not a PDF. Existing author/date retained.
- **Index 209 / KND-6ADA048DD0D6EEEF**, *Bad Company: How Dark Money Threatens Sudan's Transition*: official ECFR PDF, GET 200, 1,260,997 bytes, 31 pages, Jean-Baptiste Gallopin, June 2020, ECFR/324. SHA-256 `73659fad774fae71d9aaa4512a341e75c2cd05353734883be1948f79a688ee63`. Replaces a broken EPUB link with the publisher's typeset policy brief. Edition and citations now distinguish it from the previous October 2021 Instapaper export; this is not a byte-identical replacement of that export.

The original ECFR file starts with a UTF-8 BOM before its PDF header. Pypdf reported header/xref/EOF warnings but parsed all 31 pages. Independent PyMuPDF rendering succeeded on all 31 pages, warning only about leading bytes. The first and final pages were visually reviewed and show the correct policy brief and copyright/ISBN page. Publisher bytes were neither modified nor rehosted. The ECFR HTML record returned 403; the linked official PDF is accessible.

**Held:** index 114 / KND-34D83E78A19EABAD, *Sudan-Darfur Infrastructure Development Report*: official AfDB PDF returned 403. Entry unchanged. No bypass or rehosting.

Catalogue JSON changes exactly two entries. Matching CSV URLs and verified format/status maps synchronized. Prospective tracked totals after successful deployment: **124 source repairs / 288 unresolved** (previously 122 / 290); this is not a full fresh catalogue retest. Exact records, response hashes and rendering evidence: `library-source-repairs-2026-10-20.json`. Detailed local files: `C:/Users/Abdulla/Kandaka/docs/library-source-repair-2026-10-20/`. Production commit/deployment and bilingual live checks are recorded separately in canonical `SHARED-WORK.md`.

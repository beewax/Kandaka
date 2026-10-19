# Library source repairs — 18 October 2026

Two existing entries repaired; all 542 catalogue records retained. No documents rehosted, editorial pages changed, or release schedules altered.

- KND-049A72113DF638A2 (index 124): replaced unavailable legacy links with UNEP's official HTML article. Normal HTTPS GET 200. The publisher explicitly credits Dr Eiman Karar and dates the article 31 August 2016 (World Water Week 2016). Corrected author/year and preserved the saved three-page browser print's 7 August 2017 date in the citation. HTML source is labelled as an article, not a PDF.
- KND-C6397BD36FD08DFB (index 378): FAOLEX public PDF, normal HTTPS GET 200, PDF signature, 30 pages, byte-identical to the saved December 2017 ministry strategy. SHA-256: `63fff5125c9c5edf5e5d512dffdefda942832073db58b634c3fe3a7bb4af72b4`. Download label states 30 pages; strategy covers 2018–2022.
- KND-FAF69E7AE1C1E4B4 (index 0): held unchanged. Candidate publisher issue PDF failed normal TLS certificate verification. Do not count as repaired or bypass verification.

Source repair total after successful deployment: 119 → 121. Unresolved backlog: 293 → 291. One further record's author/year corrected against current publisher evidence; older metadata totals are historical.

Exact before/after records and HTTP/hash evidence: `library-source-repairs-2026-10-18.json`. Original verification files retained locally at `C:/Users/Abdulla/Kandaka/docs/library-source-repair-2026-10-18/`.

Validation: exact two-record mutation assertion, matching CSV rows, verified HTML/PDF formats and HTTP status entries; duplicate-cover check passed (2809 Markdown files). Hugo and public deployment verification are recorded in the canonical shared workfile; this document alone does not establish live deployment.

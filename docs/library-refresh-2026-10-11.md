# Library refresh — 11 October 2026

User explicitly approved six additions with Arabic/English summaries and source links, plus checking the duplicate World Bank report. This change does not release A02/A11/A12 or alter any automation.

## Research and editorial scope

Added IFPRI Sudan SSP papers 29 (THABAT SME baseline), 27 (2024 smallholder survey), and 28 (April 2026 conference proceedings); Antiquity's Christian Nubian costumes project; UNDP Sudan Annual Report 2025 (published June 2026); and the 2024 Research in Globalization paper by Elfaki and Ahmed.

Titles, authors, years and summaries checked against publisher records/abstracts. IFPRI citations verified at https://sudan.ifpri.info/research-papers/ and linked by their individual persistent handles. Remaining publisher links are recorded in data/library.json. These are catalogue summaries, not claims that all full papers received a systematic review. Arabic titles, author transliterations and summaries accompany all six. The template now supports Arabic author names and searching them, retaining existing author fallback for older entries.

Preserved distinctions: project baseline versus impact evaluation; 2024 survey versus current conditions; proceedings versus a single study; experimental costume reconstructions versus surviving originals; institutional reach reporting versus independently measured impact; prewar statistical associations versus causal or wartime findings.

## World Bank catalogue duplicate

Two records shared institution, month, year and report identity: `Sudan Economic Update May 2025` and `Sudan Economic Update, May 2025: The Economic and Social Consequences of the Conflict`. The official PDF cover, attribution and contents confirm the full report title including `Charting a Path to Recovery`.

Official source: https://documents1.worldbank.org/curated/en/099051925180542315/pdf/P178527-6a7d4d70-52be-49b7-87e5-ead89050a99b.pdf

Both previous R2 URLs returned HTTP 401 (bucket unavailable) during checking:

- https://pub-a5e3b47fe87749f491660d68e2029284.r2.dev/sudan-economic-update-may-2025.epub
- https://pub-a5e3b47fe87749f491660d68e2029284.r2.dev/wb-sudan-economic-update-2025.pdf

Consolidated the bibliographic duplicate, not a claimed byte-for-byte comparison of inaccessible files. No stored PDF or EPUB was deleted. Prior records remain recoverable in Git. Replaced the surviving link with the official PDF and revised both summaries to avoid undated “latest” language and presenting projections as observed recovery. Other old R2 links have not been audited in this scoped update.

Count: 534 + 6 additions − 1 catalogue duplicate = **539**. Both introductory counts and update dates changed together. Validation: `python scripts/check_library_refresh.py --build <Hugo output>`.

## Delivery state

Local production Hugo build passed (938 English / 2,104 Arabic pages, with existing deprecation warning). The regression check passed for 539 cards in each built Library edition, exact bilingual titles/summaries/authors for all seven affected entries, unique source links and matching introductory counts. The validator uses only Python's standard library.

Source checks: all three IFPRI handles, Cambridge and the Elsevier DOI returned HTTP 200. UNDP's HEAD request was blocked (403), but its publisher page and dated summary were successfully retrieved through web reading. Official World Bank PDF downloaded and cover/attribution/contents inspected. Synced existing remote automated news/photo commits through `8456044` without modifying their content. Commit, deployment and live verification are pending.

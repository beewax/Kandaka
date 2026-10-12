# Library refresh — 12 October 2026

The user explicitly approved adding the three recommended publications with Arabic and English summaries and source links. Scope is catalogue publication only; no queued article release or automation change.

## Research and duplicates

- ERF Working Paper 1824, *The Main Features of Sudan’s Income and Wage Structure in 2022*: March 2026, May Gadallah, Nesma Mamdouh Amer, Sara Ragab and Dalia Hany. Publisher abstract and author metadata reviewed; full paper not reviewed. The summary preserves the 2022 pre-war baseline and does not invent empirical results absent from the abstract.
- *Miseeda: between kingdoms, through epochs—reconstructing a history of the Mahas region (Sudan)*: Antiquity Project Gallery, online 24 September 2026, DOI 10.15184/aqy.2026.10427. All nine authors retained. Publisher abstract and selected HTML sections reviewed; not a systematic full-text review. Distinct from the existing Christian Nubian clothing study despite overlapping authors and subject matter.
- *Archaeology and cultural heritage in wartime: Sudan 2023–2025*: Habab Idriss Ahmed and Geoff Emberling, Antiquity 99(407), 1197–1211, online 7 October 2025, DOI 10.15184/aqy.2025.10174. Guest editorial, not an empirical survey. Accessible HTML introduction and sections reviewed because no abstract is supplied. Summary is bounded to its historical coverage, including the March–July 2025 update.

Direct publisher URLs are stored in `data/library.json` and `LIBRARY_SOURCES.md`. Cambridge publisher pages were accessible even though the web reader could not resolve their DOI URLs. Arabic author names are transliterations, not claims of official Arabic bylines. All titles, summaries and author credits have matching Arabic fields.

No matching title or identifier was present in the 539-entry catalogue; overlapping-author works are distinct. The canonical May 2025 World Bank report remains one record. Three additions produce 542 entries. No files were removed or uploaded and no other catalogue records were changed.

## Delivery record

Synchronized remote automated news/photo changes through `4eb412d` by fast-forward before editing. Source preparation, build validation, commit/push, deployment and independent live verification are separate stages. Deployment verification will be appended after the release is observed live.

Local validation passed: 542 records and cards in each language, exact bilingual titles/authors/summaries and unique source links for nine recent additions, and a single canonical World Bank report. Production Hugo build passed (951 EN / 2,213 AR pages; existing `.Site.Data` deprecation warning only). Cover audit passed for 2,446 Markdown files. No draft/future build flags were used. Hugo required execution outside the sandbox after a Windows DLL startup failure inside it.

Published content commit: `55f0feacc190dda41c6c998bcd540c6b47819e6a`. Netlify production deployment `6acd5e666a10b93837a2a5eb` is ready, matching that commit, published 12 October 2026 at **22:26:41 UTC / 17:26:41 CDT**. Both public pages were independently fetched and passed the same 542-card bilingual content/source regression check at **22:27:17 UTC / 17:27:17 CDT**:

- https://kandaka.com/library/
- https://kandaka.com/ar/library/

An earlier live check during deployment still saw the old catalogue; the successful check above was performed after readiness. No article Markdown or release schedule was changed. This Library deployment does not reset the interval between article releases.

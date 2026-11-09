# Art & Visual Heritage refresh repair — 9 November 2026

Owner authorized fixing the live section and displaying its next update time.

## Diagnosis

The 7 November weekly additions are already published: Faras bowl 26.4.108 and Rashid Diab's source-only El Jarron. A fresh live browser check on 9 November confirmed that all three selected artwork images load (natural widths 600, 600 and 964 pixels). The section only provided a generic Saturday notice. Source-only additions were absent from its homepage preview, and the weekly homepage selector ran at build time, so a new week could wait for the next successful deployment.

The regional-only filter is intentional, authorized on 24 October in the master workplan. It is preserved. Older documentation and tests describing two regional slots plus one international slot were obsolete; the test now enforces the actual regional-only approval. No removed artwork is restored.

## Repair

- Pre-render the existing reviewed, bilingual, image-backed regional pool with only this week's three cards visible as the static fallback. No new works or remote data fetching.
- Browser selection matches Hugo's source-ID ordering, Saturday 10:30 America/Chicago boundary, two-position weekly advance, eligibility cutoff, deduplication and at-most-one-new-work priority. It refreshes on load, each minute, and return to the tab. This removes the dependency on a Netlify rebuild for rotation of already reviewed works. With JavaScript unavailable, the normal build-time fallback remains.
- Show the latest reviewed illustrated-addition date from the catalogue's real `homepage_since` timestamp. This is explicitly a review date, not an invented publication or artwork date.
- Show separate next weekly-review and homepage-rotation dates in Chicago time, including daylight saving. From 9 November: review 14 November 2026 10:00 CST (16:00 UTC); rotation 10:30 CST (16:30 UTC). These dates advance independently: between 10:00 and 10:30 Saturday the review date is next week while rotation remains due that morning.
- Link the two latest existing source-only recommendations separately on the homepage; they never enter the image rotation.
- Keep EN/AR metadata, artwork sources/licences, article drafts/releases, photo selection and all automation schedules unchanged. Existing individual artwork approval gates remain in force. Review time does not promise additions or successful publication.

## Validation and release

All 36 repository Python tests pass with Hugo enabled, including 35-case browser/Hugo selection parity, regional-only eligibility, empty/small pools, duplicate exclusion and new-work priority. Three Node tests pass: separate review/rotation boundaries across DST, actual catalogue weekly changes, and visible-card/date transitions in both languages. Cover audit passes across 4,019 Markdown files. Initial full Hugo 0.160.0 production build passed in 584,553 ms (1,180 EN / 3,603 AR pages); only the existing `.Site.Data` deprecation warning.

Browser checks confirmed the English and Arabic dates are formatted correctly at runtime, exactly three image cards are visible, and the recent source-only links are localized. Browser console reported no errors. A Go date-format correction was caught before release; a final full rebuild and fresh four-route checks verify the corrected no-JavaScript fallback too. At 15:35:56 UTC, rendered homepage/gallery checks passed in both languages: all nine complete localized illustrated records, three visible homepage cards, all six separate source-only gallery recommendations, correct next dates and the exact current runtime bytes. No mobile viewport certification is claimed.

Release and independently verified production deployment are pending. Local evidence is retained outside the repository in `tmp/artwork-repair-local-2026-11-09.json` and `tmp/verify-artwork-repair-2026-11-09.py`. Browser/runtime SHA-256: `6780ac530e3b0e77b56a869663761167fb84e613a8233504612b8bc80a032c18`.

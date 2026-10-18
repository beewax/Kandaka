# Photo stream audit and restart — 18 October 2026

## Authorization and scope

The user requested completion of the photo audit, resumption of updates and bilingual positive article ideas in the authoritative master workplan. This release changes the photo stream and planning records only; article approvals, dates, drafts, the Library and the separate artwork collection are unchanged.

## Findings and disposition

107 legacy photo records inventoried; 75 previously public records changed to recoverable drafts. None deleted. This completes the inventory and public-stream containment, NOT full authentication of every historical record. Source-by-source restoration remains a weekly review backlog. See photo-audit-inventory-2026-10-18.md.

Problems include repeated URLs across dates, books/maps mixed with photographs, generic machine captions, uncertain historical geography, placeholder rights labels and missing Arabic editions. The previous licence helper accepted nearly any non-empty text; it now only recognizes explicitly allowlisted labels, but is not a substitute for original source review. Discovery still writes drafts unconditionally.

Two independently reviewed photo pairs restart the stream:

- Omdurman market, 14 August 2009, Petr Adam Dohnálek. https://commons.wikimedia.org/wiki/File:Bazaro_en_Omdurman_001.jpg — CC BY-SA 3.0 CZ. Existing local unmodified file visually inspected; SHA-1 711b03a1f589735a708770ad7ad6e41241e76b08 matches source record.
- Sudan National Museum entrance, 12 February 2013, David Stanley. https://commons.wikimedia.org/wiki/File:Sudan_National_Museum_(8625532907).jpg — CC BY 2.0. Original source metadata and licence reviewed and existing local photograph visually inspected.

Both have complete English/Arabic captions, alt text, named photographers, linked licences and source records, and explicit historical-date/current-condition limits. Reusing these existing image files does not release the draft articles that also use them.

## Recurrence and gates

Daily discovery workflow restored at 06:20 UTC; all discoveries remain drafts. No age-based automatic deletion. Separate Saturday 10:30 America/Chicago photo-review heartbeat created and confirmed ACTIVE: kandaka-weekly-bilingual-photo-review. The existing Saturday artwork update remains unchanged. Weekly additions depend on source verification, not a forced quota.

Templates now use the current language, show real image thumbnails, and fail builds for public photographs lacking reviewed bilingual pairs and required metadata. Homepage fallback images with incomplete credits were removed. The collection starts smaller deliberately; held records can return after individual review.

Seven new bilingual positive article ideas P01–P07 are in KANDAKA_MASTER_WORKPLAN.md as IDEA / NOT APPROVED FOR PUBLICATION, with no dates or queue changes.

## Verification

Nine image-fetch regression tests passed. Production Hugo 0.160.0 build passed (883 English / 2,476 Arabic pages; existing Site.Data deprecation warning). Generated English/Arabic gallery, homepage and photo-page HTML checked for correct image URLs, translated titles, credits and licence links; legacy photo references absent from the checked pages. Deployment verification pending; do not infer publication until the release evidence is appended.

## Verified release

- Scoped release commit: 67f0ed680aeb33055a945addc84f40a9af0a8106, pushed to main.
- Netlify production deployment: 6ad51be491c178b4f7006b93, ready, matching release commit.
- Actual publication: 18 October 2026 19:21:06.905 UTC / 14:21:06.905 CDT.
- Independently checked after publication: English/Arabic gallery, both homepages, and all four photo detail pages returned HTTP 200 with the expected localized text and image paths. Browser screenshots confirmed both photographs in the English and Arabic gallery; browser image checks confirmed loaded pixels at widths 1600 and 1024.
- Live galleries: https://kandaka.com/images/#photo-stream and https://kandaka.com/ar/images/#photo-stream.
- Photo detail paths: /images/omdurman-market-2009/, /ar/images/omdurman-market-2009/, /images/sudan-national-museum-2013/, /ar/images/sudan-national-museum-2013/.
- GitHub API independently reported Fetch Sudan Images workflow active. Daily cron is committed on main; a future successful daily run is not claimed.
- Separate weekly bilingual photo-review automation is ACTIVE. Existing artwork, Library and article automations unchanged.

The public-stream cleanup and restart are verified. Authentication/restoration of the legacy archive remains a rolling backlog, not completed research. No files were deleted.

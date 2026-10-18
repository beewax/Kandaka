# H01 — scheduled bilingual release, 19 October 2026

On 18 October the user explicitly authorized publishing both prepared language versions on the existing schedule, keeping the approved engraving unchanged and verifying both live pages afterward.

## Release time and state

- Scheduled release: **19 October 2026, noon America/Chicago (17:00 UTC)**, through the existing Kandaka article publication queue.
- A12 was published 17 October at 12:16:55.261 UTC; the scheduled H01 release is more than 48 hours later.
- Both H01 public URLs returned 404 and both live search indexes omitted H01 during the 18 October checks. The two repository files remain `draft: true`; their 19 October frontmatter date is a planning target, not evidence of publication.
- Do not release early, republish completed articles, skip H01 or batch later items. After H01, continue A13–A18 under the existing spacing and verification rules.

## Prepared text and approved engraving

Use the complete reviewed `content/history/khartoum-in-1850.en.md` and `.ar.md` files now in main. They retain the approved six-section article, concise links to Melly's relevant chapters and five matching further-reading entries. The quotation wording was checked against the primary account; the al-Tahtawi context is separately sourced to Harran's 1976 study, rather than assuming that every name in Melly identifies the same scholar. Both versions distinguish traveller estimates and judgments from a census or neutral historical account. The linked Gutenberg text is the 1852 second edition; the work and engraving date from 1851.

Preserve the already approved file **without further cropping, filtering, recompression or replacement**:

- `static/images/uploads/khartoum-1850-melly-engraving.jpg`
- SHA-256: `1894b1e0f5f4af4ae609ff81ddfb0a3bdd0f77a83070e37784e8dcf0190b2774`
- Keep the localized alt text and credit, including the existing caption crop disclosure. Render the cover once, with no duplicate inline image.

## Scheduled execution

1. Pull current main and read this record. Confirm H01 is not already published; if a prior run succeeded, verify and report that result without publishing again.
2. On or after the scheduled time, confirm the preceding article's actual publication and the 48-hour interval. The user has approved both reviewed versions and the existing engraving; no further approval is needed within this scope.
3. Enable only this language pair with `draft: false` and actual release-day metadata. Keep History and all later draft flags unchanged. Run the normal production Hugo build and cover audit, review the scoped diff, commit and push through the existing Git-to-Netlify process.
4. Check that Netlify's successful production deploy matches the release commit. Independently verify the English and Arabic URLs below, complete text, citations, language direction, cross-language links, publication metadata, image loading and exactly one cover rendering. Fetch the live JPEG and compare its SHA-256 with the approved value above.
5. Record commit, deploy ID, actual publication time and independent verification separately. Notify the user only on verified publication, a material failure or required action; stay quiet while nothing actionable changes.

English: https://kandaka.com/history/khartoum-in-1850/

Arabic: https://kandaka.com/ar/history/khartoum-in-1850/

This document records authorization and preparation. It does **not** assert that H01 has been published.

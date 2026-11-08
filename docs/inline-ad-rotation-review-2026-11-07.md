# Inline Nile Book Store rotation — review only

Local change requested 7 November 2026. Not committed, pushed or deployed.

- Browser selection uses the existing article hash plus the UTC calendar day, preserving English/Arabic pairing and article staggering.
- Existing ten-offer pool, text, covers, prices, tracked sponsored links, paragraph placement and sensitive-page exclusions remain in use.
- The browser refreshes at midnight UTC, on visible-tab return and page restoration. It defers replacement while focus is inside the advert.
- A build-selected advert remains readable and linked without JavaScript. Other offers are inert templates; only one advert is active.
- Review preview is generated from Hugo-built English/Arabic Khartoum article markup. Date controls are review-only and do not enter production pages.

Validation: new runtime tests cover UTC boundaries, complete cycles, bilingual identity, midnight timer, sleep/page restoration, focus preservation and listener cleanup. Existing homepage rotation regression tests pass. Full Hugo build and visual preview results are recorded after inspection.

Approval: pending user review of finished preview. No deployment authorization.

Completed verification: Hugo 0.160.0 full bilingual build passed (236 seconds; existing .Site.Data deprecation warning). Generated EN/AR article markup each contains ten inert templates and one fallback. Sensitive aid-page exclusions passed. Browser review verified Next day changes both language offers together; 1280px desktop and 390px mobile have no horizontal overflow.

Finished preview: ../../deliverables/site-updates/inline-ad-rotation-2026-11-07/preview.html (relative to checkout parent, or use local review URL http://localhost:8765/deliverables/site-updates/inline-ad-rotation-2026-11-07/preview.html). Desktop and mobile screenshots are saved alongside the preview.

8 November 2026: Owner explicitly approved deployment of the finished preview. Production verification pending.
## 8 November 2026 — Deployment verified

Owner authorized deployment. Commit 959e0044e8462bcc158882b78b65f1f852d1e38e deployed successfully as Netlify production 6af1019f3bd87b9897f4e486 at 2026-11-08T23:12:35.763Z (17:12 Chicago). Live English/Arabic Khartoum article requests returned 200, each with one fallback, ten inert offers and matching article seed 203051704; directions LTR/RTL retained. Live runtime bytes exactly match reviewed code, and both aid-page exclusions pass. Midnight/browser lifecycle behavior passed deterministic tests before release. Post-deployment browser visual check timed out; the previously reviewed desktop/mobile preview remains the visual evidence.

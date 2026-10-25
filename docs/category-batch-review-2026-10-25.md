# Approved category batch — 25 October 2026

Scope: the owner requested only the already-approved bilingual History/Culture site structure, navigation order and Funj reclassification/title/URL preservation. Stop after this batch for owner review; no next editorial priority is authorized by this request.

## Repository findings

Inspected origin/main at b894512 and consulted KANDAKA_MASTER_WORKPLAN.md before changes. Commit 0af39818ab3763834387bd9335e7a8ff4ba887c8 already added all four section index files, moved both Funj editions from Ideas to History, set their matching titles, and added old Ideas aliases. Those existing files are preserved without article edits.

- English title: The Funj Sultanate: Three Centuries of Power on the Blue Nile
- Arabic title: سلطنة الفونج: ثلاثة قرون من القوة على النيل الأزرق
- Current URLs: /history/funj-sultanate/ and /ar/history/funj-sultanate/
- Old URLs: /ideas/funj-sultanate/ and /ar/ideas/funj-sultanate/ (Hugo HTML redirects, not an asserted HTTP 301)

## Change in this batch

Remove the extra Categories/التصنيفات main-menu entries from hugo.toml to match the requested order:

- Ideas · Development · History · Culture · News · Library · About · Search
- أفكار · التنمية · التاريخ · الثقافة · الأخبار · المكتبة · حول · بحث

Category index URLs remain available. No article body, translation, draft flag, date, release schedule, source registry, gallery or automation changes.

## Verification

Twelve local rendered-page checks passed: both homepages, History/Culture sections, category indexes, current Funj pages and old Ideas aliases. Verified exact menu text/order, HTML language/direction, matching Funj H1 titles, translation-switch links and alias targets. Full production Hugo 0.160.0 build did not finish after more than 20 minutes on the unresponsive local host and was stopped; this is not a successful build. Its only diagnostic was the existing .Site.Data deprecation warning. Live Arabic History was visually inspected and showed localized navigation, right-aligned text and RTL layout. Subsequent browser connection attempts timed out; do not infer additional visual/mobile checks from that observation.

## Completed verification

The retry with GOMAXPROCS=2 and GOMEMLIMIT=384MiB passed in 242280 ms: 1032 EN / 2894 AR pages, 160 EN / 184 AR aliases. The existing .Site.Data deprecation warning remains; no build errors.

Commits 9f36267 and ff9f53a pushed to codex/category-batch-review, PR #18. Netlify preview deployment 6ade7a98e2d96df59e67fcae is ready for exact commit ff9f53ad6059afb6390eafdc3d151d471dcf2769, without error. All twelve HTTP/rendered checks passed against https://deploy-preview-18--kandaka.netlify.app/ with the requested menu order. All twelve current-production baseline checks also passed (production still had its extra Categories dropdown at that check). Preview and production alias documents return HTTP 200 and point to the matching production History URL.

Browser connection timeouts prevent a new visual/mobile claim. RTL HTML direction, Arabic labels and translation links passed in both editions. Production release status is recorded separately after merge/deployment verification. No next editorial task is authorized.

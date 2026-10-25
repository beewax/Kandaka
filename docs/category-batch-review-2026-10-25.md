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

Twelve local rendered-page checks passed: both homepages, History/Culture sections, category indexes, current Funj pages and old Ideas aliases. Verified exact menu text/order, HTML language/direction, matching Funj H1 titles, translation-switch links and alias targets. Full production Hugo 0.160.0 build is awaiting final exit status. Live Arabic History was visually inspected and showed localized navigation, right-aligned text and RTL layout. Subsequent browser connection attempts timed out; do not infer additional visual/mobile checks from that observation.

Commit, deployment and final verification results will be recorded after completion.

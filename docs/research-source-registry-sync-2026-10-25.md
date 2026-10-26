# Research Source Registry synchronization — 25 October 2026

The owner approved proceeding after the category batch and requested synchronizing the full Kandaka Research Source Registry into the authoritative master without publishing articles. During the same task the owner proposed Culture coverage of Sudanese cinema history, reviews and challenges, and reviews of books still under copyright.

## Scope and provenance

Recovered the complete available source conversation, **Update Kandaka Source Registry**, ID `6a8dae62-7ad8-83ea-afbd-d464d8bfe5e2`, rather than relying on its cached preview. Consulted the repository master, the canonical local master/shared workfile, repository guidance and the read-only synced project workplan. Started from origin/main `ffc88a2` in the existing isolated checkout.

Appended sections 17–18 to KANDAKA_MASTER_WORKPLAN.md. Preserved every pre-existing byte in both the isolated repository master and the canonical local master, whose uncommitted reconciliation work differs from GitHub. Neither copy was substituted for the other. Synced `sources/` material was not edited.

## Registry coverage

155 stable source/discovery IDs across 14 groups, with institution/type/region, topics and reason to consult, website and publication locators, priority, last link-check state and notes. All named original sources and umbrella streams are retained. Eight NGO/think-tank starting points are explicitly labelled supplemental discovery candidates, not attributed to the original list or endorsed.

Coverage includes government and official data; GRAS/ARC/scientific research; fourteen named Sudanese universities and other-repository discovery; digital/public infrastructure; professional/community evidence; UNESCO and other UN sources; banks; African/Arab institutions; US/China/India/EU/Japan/Korea/Brazil technology scanning; libraries and historical collections; NGO/think-tank discovery.

Added the standing low-cost/novel-technology research requirement and Sudan Technology Opportunity Filter, including Sudanese prior work, affordability, maturity, independent evidence, lifetime maintenance, ordinary-user access, regional inclusion, jobs/skills, foreign exchange, institutions and cheaper alternatives. Preserved acquisition/provenance rules and the distinction between Kandaka's `kandaka-library` storage and legacy Nile Book Store URLs. No monitoring automation was created or changed.

129 distinct HTTPS locators checked with certificate validation enabled: 100 returned HTTP 200, including one JSTOR challenge page; 29 returned access errors. An HTTP response is not publication/content/rights verification. Unresolved sources remain in the registry. Rows without an established endpoint explicitly require discovery; their inclusion is complete as a research target, not a claim that endpoint acquisition is finished. The JSON audit records errors, final URLs, sampled titles and primary locator evidence. Search-index access and direct HTTPS access sometimes disagree; neither is silently substituted for the other.

## Culture finding and new ideas

The section has one published bilingual essay, on wrestling. Two published Culture-tagged essays remain stored under Ideas: `film-tv-theatre-industry-sudan` and `mobile-cinema-development-sudan`. The section renderer lists child pages, explaining their absence from `/culture/`. Arabic metadata uses `ثقافة` for those two articles and `الثقافة` for wrestling. The museums/recovery article is draft-protected. No article was moved or metadata normalized.

The owner responded to the proposed reclassification with new Culture directions rather than authorizing those moves. Recorded C26-01 (cinema history), C26-02 (film reviews and industry challenges), C26-03 (reviews of copyrighted books) as IDEA / RESEARCH NEEDED, with research and image/rights requirements and no publication approval. Original critical reviews may address books that are not public domain; full-text reproduction, translation or rehosting is not authorized by that idea.

## Validation and publication boundary

Validation checks: unique consecutive RSR IDs; all 155 table records and fourteen groups; schema/URL audit consistency; original master retained as an exact prefix; original source families present; both local master additions match; new Culture IDs explicitly idea-only; documentation-only change list; `git diff --check`.

No Hugo build is needed for this documentation-only update. No article files, draft flags, dates, schedules, aliases, navigation, templates, catalogue data or hosted assets changed. Commit/merge messages use `[skip netlify]`; no rebuild or publication workflow is dispatched. Existing independent automations are not paused or modified by this task.

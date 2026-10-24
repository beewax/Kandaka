# Weekly artwork update — 24 October 2026

## Scope and verified sources
Two additions, fourteen records total: ten illustrated and four source-only. Existing twelve records and their homepage rotation metadata preserved. No photo stream, article, draft flag, schedule or automation changes.
- Ram’s-head amulet: Met object 547771 (1989.281.98), gold, about 721–664 BCE, maker unrecorded. Museum record and API checked; API isPublicDomain=true. Unmodified DP139144.jpg downloaded and visually inspected. Photograph credited to Oi-Cheong Lee; Gift of Norbert Schimmel Trust, 1989. CC0 under https://www.metmuseum.org/hubs/open-access. Geography explicitly uncertain: Egypt and Sudan, possibly Nubia, not a confirmed Sudan findspot. Museum page accessible through web reader; direct PowerShell page request encountered a security challenge (not a successful direct-page check). API and original image accessible.
- Untitled (Red): Ahmad Shibrain, 1965, oil, ink and watercolour on board, 57 × 56 cm. Primary record https://www.barjeelartfoundation.org/collection/ahmad-shibrain-untitled/ and artist biography checked. Source-only; no reproduction authorization inferred.

## Bilingual review
Complete EN/AR titles, artist/maker, dates, genre, description, collection/photographer and rights. Illustrated work has both alt texts. Arabic title is an editorial translation. Source and CC0 URLs unchanged. Unknown maker and uncertain geographic origin preserved in both editions. Modern Sudanese work remains outside image-backed homepage previews.

## Release status
Local preparation only; build, commit, deployment and independent live verification to be recorded separately. Netlify deployment skill used to retain existing Git continuous-deployment workflow.

Local production build passed: 954 EN / 2657 AR, only existing deprecation warning. Complete new gallery text and image-backed preview text checked in both languages; duplicate-source and required-field checks passed; source-only work excluded from homepage. Remote homepage now uses a Saturday 10:30 Chicago rotation; preserve that newer template and its metadata, rather than replacing it with the older local template. Independent live homepage verification required after deploy.

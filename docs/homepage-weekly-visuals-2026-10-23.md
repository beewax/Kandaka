# Homepage weekly image selection

Owner instruction, 23 October 2026: keep the existing Saturday artwork and photo reviews, but avoid fixed stale homepage images. This change rotates only already approved illustrated entries. No article, licence, scheduler, credential or pending-review publication changes.

## Eligible pool and boundary

At preparation: 12 artwork records, nine with permitted images and three source-only; 35 public, verified bilingual photo pairs, each with a distinct image URL; 89 English image records remain held or pending. Existing bilingual metadata gates remain mandatory. Source-only artworks never enter the homepage image pool. The full collection retains its order and contents.

Both languages share a Saturday 10:30 a.m. America/Chicago week boundary, consistent with the existing 10 a.m. artwork and 10:30 a.m. photo editorial review slots. IANA calendar arithmetic handles daylight saving. The selector counts calendar weeks from 10 October, sorts by language-independent source URL or photo file stem and advances three positions per week. It wraps around a finite pool, so eventual repetition is expected. With fewer than three entries it shows all available entries once; empty pools render no cards. New eligible publications from the preceding editorial week receive at most one priority slot; remaining slots rotate. A publication after the boundary waits for the next Saturday, so ordinary midweek builds cannot introduce it into that week's cards.

The already-public pool at rollout is grandfathered through 23 October 00:00 UTC. This is a selector cutoff, not a changed publication date, artwork date or capture date. Photographs retain their actual existing publication/capture dates and review status. Artworks use the new `homepage_since` field, recording the documented successful public release: eight existing illustrated works were live on 11 October 02:09:53 UTC, and the Faras painting on 17 October 15:00:54 UTC. No provenance or licence fields changed. When curators add a future approved illustrated artwork, include its actual publication timestamp in `homepage_since`; without that field it remains in the full catalogue but cannot silently enter homepage rotation. Do not backdate it to force immediate inclusion. Arabic entries inherit this shared field from the source-keyed English catalogue.

The featured carousel's photo uses the first selected photo, so it follows the same weekly selection in both languages rather than remaining pinned to the newest item.

## Static publishing

This is build-time selection. Existing Saturday editorial publications use the existing Git-to-Netlify pipeline. The first successful build after the Saturday boundary renders the new set; no browser clock or random shuffle changes the cards during the week. If a review produces no commit, the existing Daily News Refresh build and frequent news pushes still rebuild the site. There is no new automation or change to cron, heartbeat prompts, secrets or hosting settings. Exact 10:30 delivery is not guaranteed: existing scheduler/build latency determines when the new static pages reach visitors.

## Validation

The isolated actual-Hugo fixtures cover current/next weeks, within-week stability, both DST transitions, unique selection, empty and small pools, new-publication priority and deferred midweek additions. Full production builds and English/Arabic rendered identity checks are recorded outside the repository in task-3. Release commit, Netlify deployment and live verification must be recorded separately; this implementation record alone does not claim publication.

## Sudan-first artwork refinement

The original collection explicitly permits international art while prioritizing Sudan. The homepage therefore selects two Sudan/Nubia works and one international work. All nine illustrated records remain in the full collection: six regional and three international. Shared source-keyed `homepage_group` metadata is `sudan-nubia` or `international`; translations inherit it. Future curated artwork needs both a real completed-review eligibility timestamp in `homepage_since` and its reviewed group. Missing/unknown groups do not silently enter homepage rotation. Art/capture dates and licences remain unchanged.

Regional selections advance two positions each editorial week; international selections advance one. The existing Saturday boundary and new-reviewed-work priority apply within each group. If a group lacks enough eligible records, fill the remaining slots from the other group without duplicates; fewer than three total eligible records produce a smaller row. Never publish a pending work to fill a slot. Photos and the featured photo are unchanged by this refinement. This preserves international works without allowing a whole week of international-only cards when enough regional works exist.

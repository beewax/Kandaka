# Bilingual news selection

The homepage and both news routes share `data/news_feed.json`. Each language
has a balanced view and a newest-first view. Only dated, non-future stories
from the last 30 days are eligible. The existing article archive remains intact.

Balanced selection gives the opening three cards to different publishers where
available, allows at most two cards per publisher, and caps official/institutional/
humanitarian updates at three. Recency, topic variety and regional variety affect
ordering. These are preferences, not fabricated quotas: a quiet topic can remain
absent. Newest-first contains up to 150 deduplicated stories per language.

Canonical source URLs remove tracking duplicates. Same-language headline clusters
within 72 hours group exact signatures and conservatively similar titles; differing
numbers or disjoint named regions prevent fuzzy grouping. Related coverage is shown
on the lead card. Clustering does not establish independent corroboration. Different
wording, translations and changing casualty counts can still produce separate cards.

## Source audit, 20 September 2026

23 enabled endpoints returned parseable feeds. A successful feed can have zero
currently relevant Sudan stories. Nine added endpoints cover Al Taghyeer (EN/AR),
Ayin Arabic, Sudanile, Beam Reports, Sudan War Monitor, Sudan Transparency and
Policy Tracker, and Radio Tamazuj (EN/AR). The Guardian uses its Sudan-specific feed.
The Sudan Tribune `.net` endpoint is correctly registered as Arabic; the English
`.com` endpoint returned HTTP 403 and remains disabled.

The generated sample contains 23 balanced English cards from 12 publishers and
24 Arabic cards from 12 publishers. Topic mix includes health, culture and economy
in English, plus education and agriculture in Arabic. Counts change with source output.

Failing/empty endpoints are retained with reasons in `data/news_sources.yaml`;
they are not counted as working sources. No paywalls or access controls are bypassed.
Reporter X accounts remain disabled pending a permitted integration and editorial
review. Sudan War Monitor is ingested through its public RSS feed as analysis,
not as verified social reporting. This is not a claim of 60–100 active publishers.

## Operation

Run `python scripts/fetch_news.py` to refresh. It reuses existing canonical-link
archive filenames, fetches in parallel, checks all feed items before applying each
source quota, and rebuilds the snapshot. Recent stored stories provide continuity
if an endpoint temporarily fails. Undated and older content cannot masquerade as new.
All sources are filtered for Sudan relevance; bilateral Sudan/South Sudan coverage
is retained, while South Sudan-only reports are excluded.

`data/news_source_health.json` distinguishes fetch failure, invalid XML, empty feeds,
and valid feeds with zero relevant stories. Inspect it after refreshes. Recheck disabled
endpoints with `python scripts/audit_news_sources.py /path/to/audit.json` before enabling.
Both Netlify builds and the three-hour news workflow regenerate selections; the workflow
commits snapshot, health and archive changes together.

Validation: `python -m unittest discover -s scripts -p 'test_*.py'`, then `hugo --minify`.
Tests cover publisher/institution caps, language separation, duplicates, freshness,
relevance, classification, stable archive names, and existing image safeguards.

# Kandaka Sudan News Hub — Phase 1 handoff

Implemented and locally tested on 2026-09-19. No deployment was performed.

## What changed

- `data/news_sources.yaml` is the source registry. It records language, source class, default topic, filtering mode, item limit, enabled status, and media policy. Social candidates remain disabled until a permitted API/embed and review queue exist.
- `scripts/fetch_news.py` now performs contextual Sudan/South Sudan classification, URL normalization, original-date preservation, topic and geography tagging, source/status labeling, media provenance, and duplicate clustering. A Sudanese source is preferred as the lead when several publishers cover the same event.
- `scripts/test_fetch_news.py` contains the regression tests. Run with:

  `PYTHONPATH=scripts python -m unittest discover -s scripts -p 'test_fetch_news.py' -v`

- `layouts/partials/news-card.html`, `layouts/_default/news-bilingual.html`, `assets/css/extended/news-hub.css`, and `static/images/news-fallback.svg` add attributed, responsive, lazy-loaded imagery and visible status/geography/language metadata.
- Three existing South Sudan-only records were retained but marked draft with `exclusion_reason: south_sudan_domestic`.
- `.github/workflows/news-refresh.yml` runs the tests before fetching news.

## Validation result

Eight automated tests pass. They cover English and Arabic Sudan relevance, South Sudan exclusion, legitimate cross-border retention, URL normalization, topic/geography classification, local-source cluster preference, and media provenance.

The Hugo executable was not available in the packaging environment, so the GitHub/Netlify build remains the final template integration check. Review the Netlify deploy preview on desktop and mobile before merging or publishing.

## Next phase

Phase 2 implements diversity ranking limits, ranked/chronological views, fuller filters, and cross-language discovery. Phase 3 activates curated social discovery only through permitted integrations and a verification workflow.

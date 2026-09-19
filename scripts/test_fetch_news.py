import datetime as dt
import tempfile
import unittest
from pathlib import Path

import fetch_news


class SudanRelevanceTests(unittest.TestCase):
    def test_rejects_south_sudan_domestic_story(self):
        self.assertFalse(fetch_news.classify_sudan_relevance("South Sudan election delayed in Juba")[0])

    def test_retains_south_sudan_role_in_sudan_story(self):
        ok, _ = fetch_news.classify_sudan_relevance("South Sudan mediates talks between Sudan parties in Port Sudan")
        self.assertTrue(ok)

    def test_accepts_arabic_sudan_story(self):
        self.assertTrue(fetch_news.classify_sudan_relevance("ارتفاع أسعار الخبز في الخرطوم")[0])

    def test_sudanese_substring_does_not_rescue_south_sudan_story(self):
        self.assertFalse(fetch_news.classify_sudan_relevance("South Sudanese teenager wins election in Juba")[0])


class MetadataTests(unittest.TestCase):
    def test_url_normalization_removes_tracking(self):
        self.assertEqual(fetch_news.normalize_url("HTTPS://Example.com/story/?utm_source=x&x=1#top"), "https://example.com/story?x=1")

    def test_topic_and_geography(self):
        text = "Hospital in El Fasher faces cholera outbreak"
        self.assertEqual(fetch_news.classify_topic(text, "Sudan News"), "Health")
        self.assertEqual(fetch_news.classify_geography(text), ["Darfur"])

    def test_cluster_prefers_sudanese_reporting(self):
        now = dt.datetime.now(dt.timezone.utc)
        common = {"cluster_id": "x", "published": now, "status": "Verified reporting", "link": "https://example.com", "title": "x", "description": "", "lang": "en", "topic": "Sudan News", "geography": ["National"], "image": "", "media_reuse_basis": "", "author": ""}
        international = dict(common, source="International", source_id="intl", source_class="international_journalism")
        local = dict(common, source="Local", source_id="local", source_class="sudanese_journalism")
        lead = fetch_news.cluster_candidates([international, local])[0]
        self.assertEqual(lead["source"], "Local")
        self.assertEqual(lead["corroboration_count"], 2)

    def test_written_media_has_provenance(self):
        candidate = {"title": "Khartoum report", "description": "Summary", "link": "https://example.com/story", "lang": "en", "source": "Example", "source_id": "example", "source_class": "sudanese_journalism", "topic": "Sudan News", "geography": ["Khartoum"], "published": dt.datetime(2026, 9, 19, tzinfo=dt.timezone.utc), "status": "Verified reporting", "image": "https://example.com/photo.jpg", "media_reuse_basis": "rss_metadata", "cluster_id": "abc", "author": "", "related_sources": [], "corroboration_count": 1}
        with tempfile.TemporaryDirectory() as tmp:
            text = fetch_news.write_candidate(candidate, Path(tmp)).read_text(encoding="utf-8")
        self.assertIn("media_source: https://example.com/story", text)
        self.assertIn("media_attribution: Example", text)


if __name__ == "__main__":
    unittest.main()

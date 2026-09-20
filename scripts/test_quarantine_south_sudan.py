from pathlib import Path
import tempfile
import unittest

from quarantine_south_sudan import quarantine_content
from fetch_images import write_image_page


class StoredContentTests(unittest.TestCase):
    def test_existing_content_is_hidden_and_cross_border_reporting_preserved(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "images").mkdir()
            (root / "news").mkdir()
            bad_image = root / "images" / "fish.en.md"
            bad_news = root / "news" / "mothers.en.md"
            good_news = root / "news" / "talks.en.md"
            bad_image.write_text('---\ntitle: Cleaning Fish, Sth Sudan\ndate: 2026-09-20\ndraft: false\n---\nTilapia\n', encoding="utf-8")
            bad_news.write_text('---\ntitle: What South Sudan’s mothers teach us about political authority\n---\nJuba reporting\n', encoding="utf-8")
            original = '---\ntitle: South Sudan mediates Sudan talks in Port Sudan\ndraft: false\n---\nTalks\n'
            good_news.write_text(original, encoding="utf-8")
            self.assertEqual(set(quarantine_content(root)), {bad_image, bad_news})
            for path in (bad_image, bad_news):
                self.assertIn("draft: true", path.read_text(encoding="utf-8"))
            self.assertIn("date: 2026-09-20", bad_image.read_text(encoding="utf-8"))
            self.assertEqual(good_news.read_text(encoding="utf-8"), original)
            self.assertEqual(quarantine_content(root), [])

    def test_final_image_writer_rejects_out_of_scope_image(self):
        with tempfile.TemporaryDirectory() as tmp:
            self.assertFalse(write_image_page(tmp, {"title": "Cleaning Fish, Sth Sudan"}, 1))
            self.assertEqual(list(Path(tmp).iterdir()), [])

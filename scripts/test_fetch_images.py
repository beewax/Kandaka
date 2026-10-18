#!/usr/bin/env python3
"""Focused regression tests for the Sudan image editorial safety filters."""

import os
import tempfile
import unittest

import fetch_images


class SudanImageCandidateTests(unittest.TestCase):
    def test_rejects_abbreviations_and_encoded_source_metadata(self):
        for title in ("Cleaning Fish, Sth Sudan", "Cattle, S. Sudan", "S.Sudan", "S Sudan", "Sth. Sudan", "File:Fish%2C_Sth_Sudan.jpg", "جنوب السودان"):
            with self.subTest(title=title):
                self.assertFalse(fetch_images.is_sudan_image_candidate(title))

    def test_rejects_explicit_south_sudan(self):
        self.assertFalse(fetch_images.is_sudan_image_candidate(
            "Market day in Juba, South Sudan", "sudan africa street"
        ))

    def test_rejects_compact_flickr_tag(self):
        self.assertFalse(fetch_images.is_sudan_image_candidate(
            "Nile sunset", "southsudan juba travel"
        ))

    def test_rejects_unambiguous_south_sudan_location(self):
        self.assertFalse(fetch_images.is_sudan_image_candidate(
            "River port at Malakal", "Nile Sudan"
        ))

    def test_preserves_sudan_nubia_and_kush(self):
        accepted = [
            "Meroe pyramids, Sudan",
            "Nubian temple near Dongola",
            "Kushite goldwork from Sudan",
            "Khartoum at the meeting of the Niles",
            "Landscape along Sudan's northern border",
        ]
        for metadata in accepted:
            with self.subTest(metadata=metadata):
                self.assertTrue(fetch_images.is_sudan_image_candidate(metadata))

    def test_rejects_egyptian_nubia(self):
        self.assertFalse(fetch_images.is_sudan_image_candidate(
            "Nubian village near Aswan, Egypt"
        ))


class ImagePublicationSafetyTests(unittest.TestCase):
    def test_flags_unverified_and_unknown_licenses_as_not_reuse_safe(self):
        for license_text in ("", "license unverified", "All Rights Reserved", "Copyright status unknown", "Flickr", "unknown", "CC BY-NC 4.0", "not public domain"):
            with self.subTest(license_text=license_text):
                self.assertFalse(fetch_images.has_reuse_safe_license({"license": license_text}))

    def test_accepts_affirmative_reuse_license(self):
        self.assertTrue(fetch_images.has_reuse_safe_license({"license": "Public domain"}))
        self.assertTrue(fetch_images.has_reuse_safe_license({"license": "CC BY 4.0"}))

    def test_detects_existing_image_url_across_dates(self):
        with tempfile.TemporaryDirectory(dir=os.getcwd()) as content_dir:
            images_dir = os.path.join(content_dir, "images")
            os.makedirs(images_dir)
            image_url = "https://example.org/sudan-image.jpg"
            with open(os.path.join(images_dir, "older.en.md"), "w", encoding="utf-8") as page:
                page.write(f'image: "{image_url}"\n')
            self.assertTrue(fetch_images.image_url_already_catalogued(content_dir, image_url))
            self.assertFalse(fetch_images.image_url_already_catalogued(content_dir, "https://example.org/new.jpg"))


if __name__ == "__main__":
    unittest.main()

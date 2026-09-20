#!/usr/bin/env python3
"""Focused regression tests for the Sudan image geography filter."""

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


if __name__ == "__main__":
    unittest.main()

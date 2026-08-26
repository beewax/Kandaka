"""Validate generated Kandaka Pinterest RSS feeds."""

from __future__ import annotations

import sys
import urllib.parse
import xml.etree.ElementTree as ET
from pathlib import Path


MEDIA = {"media": "http://search.yahoo.com/mrss/"}
EXPECTED = ("images/pinterest.xml", "ideas/pinterest.xml")


def main(output_dir: str) -> int:
    root = Path(output_dir)
    total = 0

    for relative_path in EXPECTED:
        feed_path = root / relative_path
        if not feed_path.is_file():
            raise AssertionError(f"Missing feed: {feed_path}")

        items = ET.parse(feed_path).getroot().findall("./channel/item")
        if not items:
            raise AssertionError(f"Feed contains no items: {feed_path}")

        images: set[str] = set()
        for item in items:
            link = item.findtext("link", default="")
            if urllib.parse.urlparse(link).netloc != "kandaka.com":
                raise AssertionError(f"Off-domain destination in {feed_path}: {link}")

            media = item.find("media:content", MEDIA)
            if media is None or not media.attrib.get("url"):
                raise AssertionError(f"Missing media:content in {feed_path}")

            enclosure = item.find("enclosure")
            if enclosure is None or not enclosure.attrib.get("url"):
                raise AssertionError(f"Missing enclosure in {feed_path}")
            if not enclosure.attrib.get("type", "").startswith("image/"):
                raise AssertionError(f"Invalid enclosure image type in {feed_path}")

            image_url = media.attrib["url"]
            if enclosure.attrib["url"] != image_url:
                raise AssertionError(f"Image tag URLs disagree in {feed_path}")
            if image_url in images:
                raise AssertionError(f"Duplicate image in {feed_path}: {image_url}")
            images.add(image_url)

        total += len(items)
        print(f"{relative_path}: {len(items)} valid items")

    print(f"Validated {total} Pinterest feed items")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1] if len(sys.argv) > 1 else "public"))

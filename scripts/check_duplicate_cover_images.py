#!/usr/bin/env python3
"""Fail the build when an article repeats its cover image in the body."""

from __future__ import annotations

import argparse
import html
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

FRONT_MATTER = re.compile(r"\A---\s*\r?\n(.*?)\r?\n---\s*(?:\r?\n|\Z)", re.DOTALL)
YAML_COVER = re.compile(r"^cover:\s*(?:#.*)?\r?\n((?:^[ \t]+.*(?:\r?\n|\Z))*)", re.MULTILINE)
YAML_IMAGE = re.compile(r"^[ \t]+image:\s*(.+?)\s*$", re.MULTILINE)
HTML_IMAGE = re.compile(
    r"<img\b[^>]*?\bsrc\s*=\s*(?:\"([^\"]+)\"|'([^']+)'|([^\s>]+))",
    re.IGNORECASE | re.DOTALL,
)
MARKDOWN_IMAGE = re.compile(r"!\[[^\]]*\]\(\s*(?:<([^>]+)>|([^\s)]+))", re.DOTALL)
FENCED_CODE = re.compile(r"^(?:```|~~~).*?^\s*(?:```|~~~)\s*$", re.MULTILINE | re.DOTALL)


def normalized_image_path(value: str) -> str:
    """Return a stable path for comparing absolute and relative image URLs."""
    cleaned = html.unescape(value).strip().strip("<>")
    parsed = urlsplit(cleaned)
    path = "/" + unquote(parsed.path).replace("\\", "/").lstrip("/").casefold()
    host = parsed.netloc.casefold()
    if host and host not in {"kandaka.com", "www.kandaka.com"}:
        return f"//{host}{path}"
    return path


def body_image_sources(body: str) -> list[str]:
    body = FENCED_CODE.sub("", body)
    html_sources = [next(group for group in match.groups() if group) for match in HTML_IMAGE.finditer(body)]
    markdown_sources = [next(group for group in match.groups() if group) for match in MARKDOWN_IMAGE.finditer(body)]
    return html_sources + markdown_sources


def cover_image_from(front_matter: str) -> str | None:
    """Read cover.image from the small YAML subset used by Hugo content files."""
    cover_match = YAML_COVER.search(front_matter)
    if not cover_match:
        return None
    image_match = YAML_IMAGE.search(cover_match.group(1))
    if not image_match:
        return None
    value = image_match.group(1).strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
        value = value[1:-1]
    return value or None


def duplicate_cover_in(path: Path) -> str | None:
    text = path.read_text(encoding="utf-8-sig")
    match = FRONT_MATTER.match(text)
    if not match:
        return None

    cover_image = cover_image_from(match.group(1))
    if not cover_image:
        return None

    cover_path = normalized_image_path(cover_image)
    for source in body_image_sources(text[match.end() :]):
        if normalized_image_path(source) == cover_path:
            return cover_image
    return None


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "content_dir",
        nargs="?",
        default="content",
        type=Path,
        help="Hugo content directory (default: content)",
    )
    args = parser.parse_args()

    duplicates: list[tuple[Path, str]] = []
    for path in sorted(args.content_dir.rglob("*.md")):
        try:
            image = duplicate_cover_in(path)
        except (OSError, UnicodeError) as error:
            print(f"Could not validate {path}: {error}", file=sys.stderr)
            return 2
        if image:
            duplicates.append((path, image))

    if duplicates:
        print("Duplicate cover images found:", file=sys.stderr)
        for path, image in duplicates:
            print(f"  {path}: body repeats {image}", file=sys.stderr)
        print("Remove the inline copy; the article template already renders cover.image.", file=sys.stderr)
        return 1

    print(f"Cover-image check passed ({len(list(args.content_dir.rglob('*.md')))} Markdown files).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

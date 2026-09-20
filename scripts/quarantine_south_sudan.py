"""Hide stored South Sudan-only feed entries while retaining their source records."""

from pathlib import Path
import re

import yaml


def quarantine_content(content_dir, sections=("images", "news")):
    from fetch_images import is_south_sudan_image
    from fetch_news import classify_sudan_relevance

    changed = []
    for section in sections:
        for path in sorted((Path(content_dir) / section).glob("*.md")):
            text = path.read_text(encoding="utf-8")
            match = re.match(r"\A---\r?\n(.*?)\r?\n---(?:\r?\n|$)(.*)\Z", text, re.S)
            if not match:
                continue
            front, body = match.groups()
            metadata = yaml.safe_load(front) or {}
            if metadata.get("draft"):
                continue
            title = metadata.get("title", "")
            if section == "images":
                excluded = is_south_sudan_image(title, metadata.get("description"), body, metadata.get("source_url"), metadata.get("image_url"))
            else:
                prose = re.sub(r"https?://\S+", "", body)
                _, reason = classify_sudan_relevance(title, str(metadata.get("description") or "") + " " + prose)
                excluded = reason == "south_sudan_domestic"
            if not excluded:
                continue
            if re.search(r"(?m)^draft:", front):
                front = re.sub(r"(?m)^draft:.*$", "draft: true", front)
            else:
                front += "\ndraft: true"
            front = re.sub(r"(?m)^exclusion_reason:.*\n?", "", front)
            front += "\nexclusion_reason: south_sudan_domestic"
            path.write_text("---\n" + front + "\n---\n" + body, encoding="utf-8")
            changed.append(path)
    for path in changed:
        print(f"Excluded South Sudan-only content: {path.name}")
    return changed


if __name__ == "__main__":
    quarantine_content(Path(__file__).resolve().parents[1] / "content")

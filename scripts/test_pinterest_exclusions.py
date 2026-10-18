"""Build a minimal Hugo site to exercise persistent Pinterest exclusions."""
import json
from pathlib import Path
import shutil
import subprocess
import tempfile
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
SLUGS = (
    "2026-10-08-image-4-5456ef7c",
    "2026-10-05-image-4-21a81d95",
    "2026-10-11-image-4-7554aabf",
    "2026-10-06-image-4-db3f8328",
    "2026-10-07-image-4-f58e0b69",
    "2026-10-01-image-4-00ea4161",
    "2026-09-21-image-4-a654387b",
)


def main():
    with tempfile.TemporaryDirectory() as directory:
        site = Path(directory)
        for folder in ("layouts", "data", "content/images"):
            (site / folder).mkdir(parents=True)
        shutil.copy(ROOT / "layouts/list.pinterest.xml", site / "layouts/list.pinterest.xml")
        (site / "layouts/single.html").write_text("<html><body>{{ .Content }}</body></html>", encoding="utf-8")
        shutil.copy(ROOT / "data/pinterest_exclusions.json", site / "data/pinterest_exclusions.json")
        (site / "hugo.toml").write_text('''baseURL = "https://kandaka.com/"
[outputFormats.Pinterest]
mediaType = "application/rss+xml"
baseName = "pinterest"
[outputs]
section = ["HTML", "Pinterest"]
''', encoding="utf-8")
        for slug in SLUGS:
            shutil.copy(ROOT / f"content/images/{slug}.en.md", site / f"content/images/{slug}.md")
        # Fresh imports: new names/dates, no per-page exclusion flag. Exercise
        # source-record matching separately from image identity matching.
        images = (
            "https://mpfinlandrepox.zetcom.app/imagehelper/download?size=small&id=684366&org=43094",
            "https://mpfinlandrepox.zetcom.app/imagehelper/download?size=small&id=677813&org=43094",
            "http://esbirky.cz/img.php?size=large&id=284581",
            "https://www.esbirky.cz/img.php?id=325544&size=small",
            "https://www.esbirky.cz/img.php?id=17700126&size=small",
            "https://www.esbirky.cz/img.php?size=large&id=17643726",
            "http://esbirky.cz/img.php?id=17700218",
        )
        sources = (
            "https://museovirasto.finna.fi/Record/museovirasto.12419A96DD8F7E161B9B91FB332175D8?lng=fi",
            "https://museovirasto.finna.fi/Record/museovirasto.8B912D78C1DABECBC5D46BA9C8314A98",
            "http://esbirky.cz/detail/284579/",
            "https://www.esbirky.cz/detail/325542?lng=en",
            "https://www.esbirky.cz/detail/276227?lng=en",
            "http://esbirky.cz/detail/273455/",
            "https://esbirky.cz/detail/275149",
        )
        def page(name, image, source):
            (site / f"content/images/{name}.md").write_text(
                json.dumps(dict(title=name, date="2026-10-16", image_url=image,
                                source_url=source, draft=False)) + "\nArticle remains live.\n",
                encoding="utf-8")
        for index, (image, source) in enumerate(zip(images, sources)):
            page(f"reimport-image-{index}", image, "https://example.com/new-record")
            page(f"reimport-record-{index}", f"https://example.com/new-image-{index}.jpg", source)
        # Same providers and ID prefixes must remain eligible.
        page("allowed-esbirky", "https://www.esbirky.cz/img.php?id=2845810", "https://www.esbirky.cz/detail/2845790")
        page("allowed-finnish", "https://mpfinlandrepox.zetcom.app/imagehelper/download?id=6843660", "https://museovirasto.finna.fi/Record/museovirasto.UNRELATED")
        subprocess.run(["hugo", "--source", str(site), "--quiet"], check=True)
        feed = ET.parse(site / "public/images/pinterest.xml")
        titles = {item.findtext("title") for item in feed.findall("./channel/item")}
        assert titles == {"allowed-esbirky", "allowed-finnish"}, titles
        for slug in SLUGS:
            assert (site / f"public/images/{slug}/index.html").is_file(), slug
        for index in range(len(images)):
            for kind in ("image", "record"):
                assert (site / f"public/images/reimport-{kind}-{index}/index.html").is_file()
        print(f"PASS: {len(SLUGS)} existing sources and {len(images) * 2} reimports excluded; pages live; two same-provider controls retained")


if __name__ == "__main__":
    main()

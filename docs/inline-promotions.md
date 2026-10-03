# Nile Book Store inline promotions

`layouts/single.html` passes editorial content through the reusable
`content-with-nile-promotion.html` partial before PaperMod adds heading anchors.
RSS, summaries, library and news templates do not receive promotional content.

Edit `data/nile_promotions.yaml` to manage copy, real store cover URLs, prices,
eligible sections, word/paragraph thresholds and the rotation pools. No
promotional HTML is required in article Markdown.

Only regular pages in history, culture, development and ideas with at least
400 words and seven top-level paragraphs qualify. The card appears after the
fifth top-level paragraph; paragraphs in lists, blockquotes and figures do not
count. Use `nile_promotion: false` in front matter to opt an article out, or
`enabled: false` in the data file to disable all placements.

A hash of section and translation base name staggers automatic cards across the
ten entries in `inline_pool`. The selection advances once per UTC day, so a page
does not remain locked to one title: readers see a mix of individual English and
Arabic books, Arabic and English comics, and EPUB-plus-audiobook bundles. English
and Arabic translations share the same offer with localized copy. Rotation needs
no cookies or client-side scripts and avoids animation and layout shifts.
Sensitive pages listed in `excluded_pages` receive no card; the Sudan aid guide
is the first explicit exclusion.

Every rotating offer includes a genuine Nile Book Store product image and
localized alternative text. Collection cards use a representative title from
that collection rather than appearing as text-only promotions.

The homepage separately presents three catalogue groups from the same five-item
pool. Its starting position advances by build day, so regular news builds rotate
the selection without browser tracking or animation. The module explicitly says
that Nile Bookstore is separate from Kandaka's editorial work, uses bilingual
copy, and tags its sponsored links with `utm_medium=homepage` and
`utm_campaign=store_showcase`. Each homepage card displays the representative
product cover and localized alternative text supplied by its offer record.

## Verified rotating titles (2026-09-13)

All four added titles use existing Nile Book Store product cover URLs; no new
covers were generated. Product descriptions, availability and prices were
checked in the store's public product catalogue. Arabic products are explicitly
identified as Arabic even on English pages, and vice versa.

| Article | Title | Context | Price |
| --- | --- | --- | --- |
| Funj Sultanate | The Tabaqat of Wad Dayf Allah | Biographical source on scholars, saints and society in the Sennar/Funj period | Free |
| Tackling Illiteracy | Al-Nisaiyat, Malak Hifni Nasif | A woman writer's essays on girls' education and women's social position | US$2.99 |
| New Irrigation Canals; Water Paradox | Ten Days in Sudan, Muhammad Husayn Haykal | Historical observations of Sennar Dam's opening and Gezira irrigation | Free |
| River Transportation | Khartoum and the Blue and White Niles, Volume II | Illustrated historical account of Nile travel and routes to Khartoum | US$0.99 |

These titles are part of the daily in-article rotation rather than permanent
article mappings. The Tabaqat card explains
its fixed-layout format and tablet recommendation. Historical travel accounts
are described as historical reading, not contemporary policy advice.

Add verified titles under `offers` with `url`, `cover`, narrowly relevant `tags`,
and `en`/`ar` copy containing `title`, `description`, `price`, `button` and `alt`.
Suitable future topics include Arabic heritage, African/Islamic history, women
writers/history, illustrated Arabic books and contextually relevant Arabic comics.
Use `Free` / `مجاني` only for verified free titles. Prices are editorial snapshots
and should be rechecked when updating the catalogue. All links receive the three
required UTM values in the card partial.

Meroë's US$2.99 price, cover and English EPUB format were verified on 2026-09-13
against https://nilebookstore.com/products/meroe-the-city-of-the-ethiopians and its
public `.js` product endpoint. The collection card uses this real product cover
and labels its price as the featured EPUB's price, not the collection's price.

Validate with Hugo 0.160.0 (the Netlify version):

```sh
hugo --minify
python scripts/check_inline_promotions.py
```

The card inherits PaperMod light/dark variables and language direction, uses
logical spacing properties, and stacks below 480px. Links have visible keyboard
focus and a minimum 44px touch target. Cover dimensions reserve loading space.

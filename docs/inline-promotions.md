# Nile Book Store inline promotions

`layouts/single.html` passes editorial content through the reusable
`content-with-nile-promotion.html` partial before PaperMod adds heading anchors.
RSS, summaries, library and news templates do not receive promotional content.

Edit `data/nile_promotions.yaml` to manage copy, real store cover URLs, prices,
eligible sections, word/paragraph thresholds and article-specific placements.
The initial override pairs `history/kandaka-nubian-queens` (both translations)
with Meroë. No promotional HTML is required in article Markdown.

Only regular pages in history, culture, development and ideas with at least
400 words and seven top-level paragraphs qualify. The card appears after the
fifth top-level paragraph; paragraphs in lists, blockquotes and figures do not
count. Use `nile_promotion: false` in front matter to opt an article out, or
`enabled: false` in the data file to disable all placements.

A stable hash of section and translation base name assigns 75% of automatic
slots to Sudan & the Nile. The remaining slots use a title only when its tags
match the article. Unmatched slots fall back to the collection, so the actual
collection share can exceed 75% while the vetted title catalogue is small.
Explicit editorial placements override selection, but never eligibility.
Translations share the same selection. No cookies or client-side scripts are used.

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

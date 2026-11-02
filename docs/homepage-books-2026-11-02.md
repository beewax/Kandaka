# Homepage bookstore selections - 2 November 2026

Prepared for the owner-approved refinement of daily catalogue selections. No publication is claimed by this preparation record.

The previous five collection cards replaced only one of three visible cards daily and ran only on load. This revision presents twelve verified actual books, three per UTC day, with no adjacent-day repeated covers. Four groups repeat on a four-day cycle. This is a rotation of catalogue books, not fresh daily acquisitions. The original collection/inline-promotion data is unchanged.

All twelve ACTIVE products were read from the connected Nile Book Store account, then matched against public product JSON, public product pages (HTTP200), current featured-cover URLs and downloaded cover bytes (HTTP200). Twelve distinct cover SHA256 values were confirmed on 2 November2026. Arabic/English labels identify the book's actual language and format, rather than implying every displayed book is Arabic. Product links replace collection links. No prices are shown or changed.

The shared static selector drives production cards and the review calendar. It refreshes at the next UTC midnight, on visibility return and on pageshow. No duplicate manual calendar is shipped. The review controls inject a preview date only; they do not change computer time or live site data.

## Verified pool

- [Journey to Meroë and the White Nile](https://nilebookstore.com/products/journey-to-meroe-white-nile-frederic-cailliaud) - English · Illustrated EPUB.
- [Al-Nisaiyat — Malak Hifni Nasif](https://nilebookstore.com/products/%D8%A7%D9%84%D9%86%D8%B3%D8%A7%D8%A6%D9%8A%D8%A7%D8%AA-%D9%85%D9%84%D9%83-%D8%AD%D9%81%D9%86%D9%8A-%D9%86%D8%A7%D8%B5%D9%81) - Arabic · EPUB.
- [Planet Comics #6](https://nilebookstore.com/products/planet-comics-6-fiction-house-1940) - English · Comic (CBZ).
- [Khartoum and the Blue and White Niles, Vol. II](https://nilebookstore.com/products/khartoum-and-the-blue-and-white-niles-volume-ii) - English · EPUB.
- [The Maiden of Denshawai](https://nilebookstore.com/products/adhra-denshawai-mahmoud-taher-haqqi-arabic-epub) - Arabic · EPUB.
- [Bulletman #1](https://nilebookstore.com/products/bulletman-001) - English · Comic (CBZ).
- [Voyage to Meroë: The Atlas](https://nilebookstore.com/products/voyage-to-meroe-the-atlas-of-the-nile-nubia-and-sennar-by-frederic-cailliaud) - English · Illustrated EPUB.
- [Al-Durr al-Manthur — Zaynab Fawwaz](https://nilebookstore.com/products/al-durr-al-manthur-zaynab-fawwaz-arabic-epub) - Arabic · EPUB.
- [Swallows and Amazons](https://nilebookstore.com/products/swallows-and-amazons) - English · EPUB + audiobook.
- [Meroë, the City of the Ethiopians](https://nilebookstore.com/products/meroe-the-city-of-the-ethiopians) - English · Illustrated EPUB.
- [History and Geography of Sudan — Naum Shuqair](https://nilebookstore.com/products/%D8%AA%D8%A7%D8%B1%D9%8A%D8%AE-%D8%A7%D9%84%D8%B3%D9%88%D8%AF%D8%A7%D9%86-%D8%A7%D9%84%D9%82%D8%AF%D9%8A%D9%85-%D9%88%D8%A7%D9%84%D8%AD%D8%AF%D9%8A%D8%AB-%D9%88%D8%AC%D8%BA%D8%B1%D8%A7%D9%81%D9%8A%D8%AA%D9%87-%D9%86%D8%B9%D9%88%D9%85-%D8%B4%D9%82%D9%8A%D8%B1) - Arabic · EPUB.
- [Dracula — Arabic translation](https://nilebookstore.com/products/%D8%AF%D8%B1%D8%A7%D9%83%D9%88%D9%84%D8%A7-%D8%A8%D8%B1%D8%A7%D9%85-%D8%B3%D8%AA%D9%88%D9%83%D8%B1-%D8%AA%D8%B1%D8%AC%D9%85%D8%A9-%D8%B9%D8%B1%D8%A8%D9%8A%D8%A9) - Arabic · EPUB.

## Validation

- Full Hugo0.160 production build passed171646ms,1106English/3261Arabic pages; existing .Site.Data deprecation warning only.
- Both rendered homepages contain all12 exact product/cover records, one selector include, and ArabicRTL. Only the old Nile module is replaced in list.html; weekly art/photo selectors, originalinline-promotion data and article files remain unchanged.
- Reusable Node test:1020consecutive days with no adjacent-day repeated cover, unique-cover deduplication, small/empty pools, same calendar selector, four-day cycle and EN/AR ID parity.
- Actual mount controlled-clock tests:UTCmidnight, visibilityreturn, pageshow, timer timing and short-pool badge. These are clock fixtures, not an observation of a real future midnight.
- Actual browser checks on standalone review and built production HTML:today/next-day calendar parity, visible covers loaded, English/Arabic IDs match;390pxwide layouts have375px document scroll width (no horizontal overflow). ArabicRTL visually inspected. Screenshots captured in the browser tool outputs.
- Final static selector bytes separately checked/copied into the build output after adding the preview-only manual-mount exclusion; this does not alter production selection behavior.

## Preserved boundaries

Saturday10:30America/Chicago art/photo policy, source/rights gates, article publication dates/covers, A17/A18 release queue and48hspacing, Library and Shopify products are unchanged. No shop writes, new images, spending or outreach. The only public-facing change is the homepage bookstore module and its local static selection asset.

## Review package

Local homepage-refinement/preview/en.html and ar.html include before/after comparison and an eight-day calendar generated by the exact production script. The reviewed source pool, catalogue-verification.json, selection-checks.json and rendered-and-preservation-checks.json remain in the task workspace. Test command from repository root: node scripts/test_nile_book_selection.cjs.

Publication-ready source scope: data/nile_home_books.json; layouts/_default/list.html; layouts/partials/nile-home-books.html; static/js/nile-book-selection.js; scripts/test_nile_book_selection.cjs; this documentation record. Recheck upstream ownership/scope before any later authorized publication and independently verify both live homepage executions afterward.

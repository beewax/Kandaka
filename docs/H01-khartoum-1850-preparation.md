# H01 preparation — Khartoum in 1850 (16 October 2026)

## Approval
- Article text (EN and AR): approved by Abdulla, 16 October 2026.
- Cover: approved by Abdulla, 16 October 2026.
- Queue position: "right after A12" (Abdulla, 16 October 2026). New order A12 → H01 → A13 → A14 → A15 → A16 → A17 → A18.

## Files
- `content/history/khartoum-in-1850.en.md` (draft: true)
- `content/history/khartoum-in-1850.ar.md` (draft: true)
- `static/images/uploads/khartoum-1850-melly-engraving.jpg`, 1800×965 JPEG. Source: George Melly, *Khartoum and the Blue and White Niles*, Vol. I (London: Colburn, 1851), frontispiece "Khartoum and the Niles", Project Gutenberg #78014 (`i1_large.jpg`). Caption text cropped off; no colour or gray filter applied (the engraving is black-and-white as printed).

## Sources (listed in both editions)
- George Melly, *Khartoum and the Blue and White Niles*, Vol. II (1851), ch. VI–VII. https://www.gutenberg.org/ebooks/78015
- George Melly, *Khartoum and the Blue and White Niles*, Vol. I (1851), frontispiece. https://www.gutenberg.org/ebooks/78014
- "'Abd al-Latif Pasha", Wikipedia: governor-general 13 Feb 1850 – 14 Jan 1852 (covers Melly's visit). https://en.wikipedia.org/wiki/%27Abd_al-Latif_Pasha
- Nile Book Store Arabic translation with notes (2026). Product links: https://nilebookstore.com/products/melly-khartoum-vol2-arabic and https://nilebookstore.com/products/melly-khartoum-vol1-arabic (both ACTIVE, checked 16 October).

## Checks done
- Hugo 0.160.0 build with drafts and future dates: both pages render; Arabic page `lang="ar" dir="rtl"`, English `dir="ltr"`; 6 sections plus Sources in each; cover referenced in both.

## Release gate
- Earliest: 48 hours after A12's actual successful release.
- Release run: change only these two files to `draft: false` with release-day date; verify EN `/history/khartoum-in-1850/`, AR `/ar/history/khartoum-in-1850/` and the cover live (HTTP 200) before recording Published.

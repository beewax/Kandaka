# Karanog and Dongola: verification of the nine existing image files

Verified 19 September 2026. This supplements the academic image audit with the actual repository files and recovered source ledger. All nine images were opened and visually inspected. No image was modified.

**Decision:** retain the five 1910 plates and both documentary Dongola images with corrected captions; retain the generated cover only as an explicitly conceptual AI illustration; hold the generated architectural cutaway. “Active” below means suitable for the review draft with the stated caption, not authorization to publish the article.

## Evidence inspected

- Repository: `beewax/Kandaka`.
- Actual files: `static/images/uploads/` under that repository.
- Provenance ledger: `docs/KARANOG_DONGOLA_SOURCE_AND_IMAGE_LEDGER.md`. It records new-image generation with OpenAI in 2026 and preserves both final prompts. Thus the academic audit's earlier “no artwork or commissioning record supplied” limitation is now partly resolved: actual artwork and generation provenance are available. This does not require calling the images commissioned by an unidentified human artist or asserting exclusive copyright.
- Original plate renders and downloaded JPGs: sibling `work/research/karanog-dongola/`.
- Academic image audit and corrected source interpretations: [image-audit.md](image-audit.md).
- Both exact Commons description pages were checked: [2017 exterior](https://commons.wikimedia.org/wiki/File:Dongola_Throne_Hall.jpg) and [1821 historical view](https://commons.wikimedia.org/wiki/File:Throne_Hall_of_Dongola,_1821.jpg).

## Decisions and caption implications

| ID | Existing asset | Status | Verified result and required treatment |
| --- | --- | --- | --- |
| I01 | `karanog-dongola-cover-original.png` | Active as conceptual artwork | Actual image is a synthetic joined Nile landscape with an invented cemetery, pottery, statue, elaborated palace exterior and ceremonial procession. The ledger identifies it as generated with OpenAI. Explicitly say the sites and periods have been juxtaposed and the scene is not an archaeological reconstruction. Do not use it to establish architecture, exact pottery motifs, court dress, original function, or geographical adjacency. |
| I02 | `karanog-cemetery-plan-1908.png` | Active | Exact SHA-256 match to `renders/karanog-243.png`; visible foldout plan label names the cemetery near Anibeh, 1907–08. This is plate 116. Preserve full plan and identify the historic title as the report's terminology. |
| I03 | `karanog-tomb-superstructures-1910.png` | Active | Exact match to `renders/karanog-235.png`; plate 112 and its own printed captions identify G70, G71 and G165 above, G259 below. |
| I04 | `karanog-ba-statue-1910.png` | Active | Exact match to `renders/karanog-8.png`; plate 1, with the historical printed label “Restoration of a Royal Ba Statue.” The modern caption must qualify both “royal” and the attributed G187 association and identify restored attributes. Do not silently present the plate's label as the modern identification. |
| I05 | `karanog-painted-pottery-1910.png` | Active | Exact match to `renders/karanog-97.png`; visible plate 43 includes 8451/G189 and giraffe decoration. Use the excavation text's hunter and collared hound identification. Remove the cattle/herder or pastoral reading from caption and alt text. |
| I06 | `karanog-meroitic-graffiti-1910.png` | Active | Exact match to `renders/karanog-225.png`; plate 107 shows copied marks. They are not all incised or all Meroitic. Caption Greek, Demotic and Meroitic examples and mixed painted/inked/scratched techniques. |
| I07 | `dongola-throne-hall-present.jpg` | Active | Exact match to the retained source JPG; viewed image and dimensions correspond to the exact Commons record. Credit LeGabrie, 18 March 2017, and link CC BY-SA 4.0. Describe “no changes by Kandaka to the downloaded file,” not a claim that the file has never been edited in its history. |
| I08 | `dongola-throne-hall-reconstruction-original.png` | Hold | Visual architectural errors are material: the image presents an apse as opening directly into the central hall; an unambiguous small dome sits over the roof; there is no clear corresponding system of four columns plus wall pilasters and surrounding corridors. A detailed unified painted programme and court gathering also convey unwarranted certainty. A general “conjectural details” disclaimer is too weak for a picture presented as a precise cutaway. Keep file and provenance, but do not activate it as an archaeological reconstruction. |
| I09 | `dongola-throne-hall-1821.jpg` | Active with colourisation disclosure | Exact match to retained source JPG. Its SHA-1 also exactly matches Commons' current file record: `2ca0024a0ee2db6dfc899d1e4c241e4fc191e5c4`. It is the 2020 DeepAI-colourised revision of Cailliaud's historical view. Commons marks it public domain. Disclose the modern colourisation and do not treat colour as nineteenth-century evidence. |

## Why the cutaway is held

The ledger's generation prompt itself conflates “four granite columns/pilasters” and calls for a small raised central dome and a deep eastern apse. The corrected research distinguishes four columns **and** corresponding wall pilasters, regards the raised roof as conjectural, and places the apse off the eastern corridor. The rendered file visibly preserves the problematic direct hall–apse relationship and presents the dome as a definite architectural element. It also fills walls with coherent figurative paintings and stages a royal gathering even though decoration belongs to several phases and original royal use remains disputed. These are representational conflicts with the article's central corrections, not simply unidentified image rights.

A later replacement should start from the published measured plan, distinguish surviving fabric from reconstruction, show the eastern-corridor apse correctly, and avoid assigning a documented date or royal ceremony to invented decorative and human detail. No replacement was generated during this inspection.

## Corrected bilingual captions

These are editorial caption recommendations; links below should be retained in whichever HTML or Markdown structure the site uses. The descriptive alt text should make the same factual distinctions without repeating the entire credit.

### I01 — conceptual cover

**English:** Conceptual illustration generated for Kandaka with OpenAI, 2026, juxtaposing Meroitic Karanog and medieval Old Dongola. The sites did not share this landscape or moment. Architecture, objects and ceremony are imaginative interpretations, not an archaeological reconstruction.

**العربية:** رسم تصوّري أُنتج لكنداكة باستخدام OpenAI عام 2026، يجمع كرانوج المروية ودنقلا العجوز في العصور الوسطى. لم يجتمع الموقعان في هذا المشهد أو في زمن واحد؛ فالعمارة والقطع والمراسم تصوّرات فنية، وليست إعادة بناء أثرية موثّقة.

**Alt implication:** say “conceptual juxtaposition” / «مشهد تصوّري يجمع»; do not describe the right-hand building as an authenticated royal reconstruction.

### I02 — plan

**English:** Excavation plan of the cemetery near Anibeh, surveyed in 1907–08. Woolley and Randall-MacIver, *Karanòg* (1910), [plate 116](https://mc.dlib.nyu.edu/files/books/ifa_egypt000402/ifa_egypt000402_lo.pdf#page=243). Public-domain historical plate; scan hosted by NYU Institute of Fine Arts.

**العربية:** مخطّط تنقيبات المقبرة قرب عنيبة، التي جرى مسحها في 1907–1908. وولي وراندال-ماكيفر، *كرانوج* (1910)، [اللوحة 116](https://mc.dlib.nyu.edu/files/books/ifa_egypt000402/ifa_egypt000402_lo.pdf#page=243). لوحة تاريخية من الملك العام؛ يستضيف نسختها الرقمية معهد الفنون الجميلة بجامعة نيويورك.

### I03 — superstructures

**English:** Tomb superstructures at Karanog: foundations of G70, G71 and G165 above; cross-ribs of G259 below. Woolley and Randall-MacIver, *Karanòg* (1910), [plate 112](https://mc.dlib.nyu.edu/files/books/ifa_egypt000402/ifa_egypt000402_lo.pdf#page=235). Public-domain historical plate; scan hosted by NYU Institute of Fine Arts.

**العربية:** المنشآت العلوية للمقابر في كرانوج: أساسات G70 وG71 وG165 في الأعلى، والدعامات المتقاطعة للمقبرة G259 في الأسفل. وولي وراندال-ماكيفر، *كرانوج* (1910)، [اللوحة 112](https://mc.dlib.nyu.edu/files/books/ifa_egypt000402/ifa_egypt000402_lo.pdf#page=235). لوحة تاريخية من الملك العام؛ يستضيف نسختها الرقمية معهد الفنون الجميلة بجامعة نيويورك.

### I04 — reconstructed statue

**English:** The excavators' 1910 colour reconstruction of the figure attributed to G187, later associated with the official Maloton. The disc and hand-held attributes include conjectural additions; “royal” is the plate's historical interpretation. Woolley and Randall-MacIver, *Karanòg*, [plate 1](https://mc.dlib.nyu.edu/files/books/ifa_egypt000402/ifa_egypt000402_lo.pdf#page=8), explanation p. 47. Public-domain historical plate; scan hosted by NYU Institute of Fine Arts.

**العربية:** إعادة التصوّر الملوّنة التي نشرها المنقّبون عام 1910 للتمثال المنسوب إلى المقبرة G187، والذي ربطته دراسات لاحقة بالمسؤول مالوتون. يضمّ القرص وما يحمله التمثال إضافات افتراضية؛ ووصفه بأنه «ملكي» هو تفسير اللوحة التاريخي. وولي وراندال-ماكيفر، *كرانوج*، [اللوحة 1](https://mc.dlib.nyu.edu/files/books/ifa_egypt000402/ifa_egypt000402_lo.pdf#page=8)، وشرحها في ص. 47. لوحة تاريخية من الملك العام؛ يستضيف نسختها الرقمية معهد الفنون الجميلة بجامعة نيويورك.

**Alt implication:** “colour reconstruction of a figure attributed to G187” / «إعادة تصوّر ملوّنة لتمثال منسوب إلى G187»; omit “royal ba statue from tomb G187.”

### I05 — painted pottery

**English:** Painted vessels and decorative bands from Karanog, including giraffes and a hunter with a collared hound (8451, G189). Woolley and Randall-MacIver, *Karanòg* (1910), [plate 43](https://mc.dlib.nyu.edu/files/books/ifa_egypt000402/ifa_egypt000402_lo.pdf#page=97); text p. 55. Public-domain historical plate; scan hosted by NYU Institute of Fine Arts.

**العربية:** أوانٍ فخارية مرسومة وأشرطة زخرفية من كرانوج، تضمّ زرافات وصيّادًا مع كلب صيد ذي طوق (8451، G189). وولي وراندال-ماكيفر، *كرانوج* (1910)، [اللوحة 43](https://mc.dlib.nyu.edu/files/books/ifa_egypt000402/ifa_egypt000402_lo.pdf#page=97)؛ والنص في ص. 55. لوحة تاريخية من الملك العام؛ يستضيف نسختها الرقمية معهد الفنون الجميلة بجامعة نيويورك.

### I06 — pottery marks

**English:** Pottery inscriptions and marks copied by the excavators, including Greek, Demotic and Meroitic examples, painted, inked or scratched on vessels. Woolley and Randall-MacIver, *Karanòg* (1910), [plate 107](https://mc.dlib.nyu.edu/files/books/ifa_egypt000402/ifa_egypt000402_lo.pdf#page=225); text pp. 78–79. Public-domain historical plate; scan hosted by NYU Institute of Fine Arts.

**العربية:** نُسخ المنقّبين لكتابات وعلامات على الفخار، منها أمثلة يونانية وديموطيقية ومروية، رُسمت بالألوان أو كُتبت بالحبر أو خُدشت على الأواني. وولي وراندال-ماكيفر، *كرانوج* (1910)، [اللوحة 107](https://mc.dlib.nyu.edu/files/books/ifa_egypt000402/ifa_egypt000402_lo.pdf#page=225)؛ والنص في ص. 78–79. لوحة تاريخية من الملك العام؛ يستضيف نسختها الرقمية معهد الفنون الجميلة بجامعة نيويورك.

### I07 — exterior photograph

**English:** The building conventionally known as the Throne Hall or Mosque Building at Old Dongola. Photograph: LeGabrie, 18 March 2017, [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Dongola_Throne_Hall.jpg), [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). No changes by Kandaka to the downloaded file.

**العربية:** المبنى المعروف اصطلاحًا بقاعة العرش أو مبنى المسجد في دنقلا العجوز. تصوير LeGabrie، 18 مارس 2017، عبر [ويكيميديا كومنز](https://commons.wikimedia.org/wiki/File:Dongola_Throne_Hall.jpg)، بترخيص [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). لم تُجرِ كنداكة تعديلات على الملف المُنزّل.

**Alt implication:** date the photograph to 2017; do not imply that it documents the building's current 2026 condition.

### I08 — inactive cutaway

**English editorial comment:** Image withheld: AI-generated cutaway from 2026 does not reliably distinguish the eastern-corridor apse, surviving column/pilaster arrangement, conjectural roof and uncertain original use. Retained for provenance; not used as archaeological evidence.

**ملاحظة تحريرية بالعربية:** الصورة محجوبة: لا يميّز الرسم المقطعي المولّد بالذكاء الاصطناعي عام 2026 بصورة موثوقة بين الحنية المتصلة بالممر الشرقي، وترتيب الأعمدة والدعامات الجدارية الباقية، والسقف الافتراضي، ووظيفة المبنى الأصلية غير المحسومة. يُحتفظ بالملف لتوثيق مصدره، ولا يُستخدم دليلًا أثريًا.

### I09 — historical view

**English:** Old Dongola's Mosque Building in Cailliaud's view of 1821, published in 1826, plate I. This digital version was colourised by LeGabrie using DeepAI in 2020; its colours are modern. [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Throne_Hall_of_Dongola,_1821.jpg) marks the file as public domain.

**العربية:** مبنى المسجد في دنقلا العجوز في منظر كايو لعام 1821، المنشور عام 1826 في اللوحة الأولى. لوّن LeGabrie هذه النسخة الرقمية باستخدام DeepAI عام 2020؛ وألوانها حديثة. يصنّف [ويكيميديا كومنز](https://commons.wikimedia.org/wiki/File:Throne_Hall_of_Dongola,_1821.jpg) الملف ضمن الملك العام.

## File identity record

All seven documentary files exactly match their corresponding retained local source files under `work/research/karanog-dongola/`:

| Asset | Local source | SHA-256 |
| --- | --- | --- |
| `karanog-cemetery-plan-1908.png` | `renders/karanog-243.png` | `9ea2154dc08911c4f0a8c71a654f966601a09fb61b5a59b1af63d29735d6ebeb` |
| `karanog-tomb-superstructures-1910.png` | `renders/karanog-235.png` | `dca2d3316c4e732a1bb05ce042d956c784e2d9806519dce840158f864901d1f6` |
| `karanog-ba-statue-1910.png` | `renders/karanog-8.png` | `0ad231f9af52829b0bd8a44daa823b909d60feb327d9695135dff89567cf277b` |
| `karanog-painted-pottery-1910.png` | `renders/karanog-97.png` | `45a91a904841abe1772137943e887538ddc40e9ec9d4f0a6f6aa50afc15436da` |
| `karanog-meroitic-graffiti-1910.png` | `renders/karanog-225.png` | `9a283cabc5a5a39df9315621e06fd398c754f1050564cba88b0c98d214a9fd87` |
| `dongola-throne-hall-present.jpg` | `dongola-throne-hall-present.jpg` | `d7f27bc48a9d111a305958e9c2e0f40bf8464cdbcf539bb49881b6034af08189` |
| `dongola-throne-hall-1821.jpg` | `dongola-throne-hall-1821.jpg` | `edcfc1e88e55439c67ce41522ba1a8419941cd8c0a460cd39e4f5dc98dd7a6a5` |

This inspection resolves the academic audit's missing-file limitation. It does not establish that an old source's ethnic or royal labels are correct, and the caption corrections remain necessary even where file identity is exact.

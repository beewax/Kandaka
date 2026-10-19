# Photo restoration batch 4 — 18 October 2026

User authorized checking the ten open source tabs, restoring verified photographs in Arabic and English, and deeper research for eSbírky 284579. No article or automation changes authorized or made.

## Source recovery

All ten relevant user tabs were inspected. The old eSbírky /detail/ addresses return a real 404, not a login failure. Its current search recovered the exact /predmet/ records for shield/spear, lion cubs, marabou, hunting trophies and steamer. The image viewers explicitly display CC BY 4.0. Record membership in a photographer's collection does not establish photographic authorship; all four restored eSbírky photos name the photographer as unknown.

The two Finnish Heritage Agency pages load in the user's browser. Opening each image viewer exposes its CC BY 4.0 licence. The agency API/direct downloads were blocked; supported browser page-assets export recovered the already-loaded image files. Amphora file 677813 matches the record. For the jar, index 0 is an archaeological drawing; the restored photograph is index 1. Both records describe Meroitic Nubian objects and list Egypt and Sudan together. Captions disclose that ambiguity rather than claiming excavation in today's Republic of Sudan. Object dates are separated from unrecorded photographic dates; no maker invented.

## Restored bilingual pairs

- 2026-09-18-image-4-21a81d95: Meroitic amphora from Nubia / أمفورا مروية من النوبة
  - Source: https://museovirasto.finna.fi/Record/museovirasto.8B912D78C1DABECBC5D46BA9C8314A98?imgid=1
  - Image: static/images/uploads/meroitic-amphora-km17000-39-116-2.jpg
- 2026-09-20-image-4-5456ef7c: Decorated Meroitic jar from Nubia / إناء مروي مزخرف من النوبة
  - Source: https://museovirasto.finna.fi/Record/museovirasto.12419A96DD8F7E161B9B91FB332175D8?imgid=2
  - Image: static/images/uploads/meroitic-jar-km17000-39-119-3.jpg
- 2026-10-11-image-4-7554aabf: Man holding a round shield and spear, 1927 / رجل يحمل ترساً مستديراً ورمحاً، ١٩٢٧
  - Source: https://www.esbirky.cz/predmet/bojovnik-s-kulatym-stitem-a-ostepem-nubove-bagirmi-provincie-kordofan-sudan-1927-284579
  - Image: static/images/uploads/shield-spear-naprstkovo-1927.jpg
- 2026-09-21-image-4-a654387b: Two men with lion cubs in Khartoum, 1911 / رجلان مع أشبال أسود في الخرطوم، ١٩١١
  - Source: https://www.esbirky.cz/predmet/machulkovi-pomocnici-s-lvicaty-na-dvore-jeho-domu-v-chartumu-275149
  - Image: static/images/uploads/khartoum-lion-cubs-1911-naprstkovo.jpg
- 2026-10-01-image-4-00ea4161: Marabou stork at Khartoum Zoo, 1920s / لقلق المارابو في حديقة حيوان الخرطوم، عشرينيات القرن العشرين
  - Source: https://www.esbirky.cz/predmet/ap-marabu-v-chartumske-zoo-273455
  - Image: static/images/uploads/khartoum-zoo-marabou-1920s.jpg
- 2026-10-07-image-4-f58e0b69: Hunting trophies in a Khartoum courtyard, early twentieth century / غنائم صيد في فناء بالخرطوم، مطلع القرن العشرين
  - Source: https://www.esbirky.cz/predmet/machulka-a-torch-s-loveckymi-trofejemi-na-dvore-domu-v-chartumu-276227
  - Image: static/images/uploads/khartoum-hunting-trophies-naprstkovo.jpg

Shield caption preserves 1927 and attributes Kordofan to the museum; unresolved historical community/place labels are not asserted as established identities. No warrior occupation inferred. Lion-cub and hunting-trophy photographs are historical documentation, not endorsements of animal capture or hunting. Štorch identification remains uncertain. Zoo species identification is explicitly attributed to the museum; no present-day wildlife claims.

## Four remaining holds

- 2026-09-22-image-1-5ecf350b: pixels show an ornate columned kiosk, not pyramid reliefs. NCAM's 2010 nomination file (https://whc.unesco.org/document/168998, pp.48 and103) supports the Naqa kiosk context, but visual primary-image cross-comparison was not completed (PDF screenshot retrieval failed). Continue held rather than republish the erroneous Meroe-pyramids label.
- 2026-09-23-image-1-66d6957b: browser source provides author Hosam Badraldin, 8 April 2026 and CC BY-SA 4.0, but precise context/location remains unverified. Do not infer poverty, displacement or ritual from the children beside roadside rubbish.
- 2026-09-30-image-4-db3f8328: exact current record recovered: https://www.esbirky.cz/predmet/zakotveny-parnik-kordofan-325542. Af I 2523, 1920s, photographer unknown, CC BY 4.0. Source location lists Europe, Germany and Sudan together. Vessel name is not evidence of capture location; requires corroboration.
- 2026-10-04-image-1-5bf80c8d: Roman Deckert's 2018 photograph is licensed, but the underlying framed historical image's creator/rights are still unresolved. Do not confuse the two dates or authors.

Alternative shield record 284590 was found, but not needed: the exact original 284579 was recovered, inspected and restored. No new alternative or duplicate entry added.

## العربية

فُحصت التبويبات العشرة. أُعيد العثور على السجلات الأصلية في موقع المتحف التشيكي بعد تغيّر روابطه، بما فيها صورة الترس والرمح المطلوبة. جُهّزت ست صور بتعليقات عربية وإنجليزية ومصادر وتراخيص موثّقة. فُصل تاريخ القطعة عن تاريخ تصويرها، وحُفظت الشكوك في هوية الأشخاص والمواقع دون تخمين. تبقى أربع صور معلّقة للأسباب المحدّدة أعلاه. لم تتغيّر المقالات أو جداول النشر.

## Validation and release

Local preparation only at this point; build, commit, deployment and independent live checks to be recorded separately. Expected total after publication: 34 bilingual photo pairs (32 restored from the original 75 plus two earlier additions), four distinct holds remain.

Local checks: all nine photo-discovery tests passed; cover audit passed across 2,809 Markdown files. All twelve rendered localized pages contain expected titles and local image paths. Git whitespace check passed. Only photo records, six unmodified source photographs and audit/workplan documentation changed.

Final production Hugo build passed with bilingual validation: 923 EN / 2,533 AR pages, 124 seconds. The earlier preliminary build predates completion of all six pairs and is not the release validation.


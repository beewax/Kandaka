

## 16 November 2026 — Keep the Library schedule, condensed to one line

Owner clarified: keep scheduling information, but do not take three lines. This supersedes the prior removal interpretation/0aa98bc9 for the homepage. Retain concise Library / المكتبة heading and show one compact line: Next review & rotation: Nov23,10:00AMCST, localized in Arabic. Review and rotation share the same next Monday10AMChicago timestamp, so no duplicate lines; omit verbose current-week/process paragraph. Visible data-library-updates hook and existing module remain; only this homepage line uses compact date formatting, while the full catalogue's separate notice retains its existing format. Complete ISO datetime retained, real timezone/DST/date advancement preserved. All books link, pool, card text/links, weekly selection and schedule unchanged. Three existing Node library tests pass. Actual browser one-line desktop/mobile and weekly-refresh checks recorded after deployment. No catalogue, artwork, article/Nile or automation edits.

العربية: أوضح المستخدم أنه يريد الإبقاء على المواعيد، ولكن في سطر موجز واحد يجمع موعد المراجعة والتبديل المقبلين، بدلاً من ثلاثة أسطر وشرح طويل. بقي العنوان المختصر والكتب والرابط والتدوير الآلي كما هي.


## VERIFIED LIVE — compact Library schedule retained

Owner clarification is implemented, superseding removal: heading Library / المكتبة with one visible concise next review-and-rotation line. Releasef4f20e78e355d927d5f6d90b96ddc8f8ad3f9131 matches ready Netlify6afbd933d6176e627af981b0, published2026-11-17T04:34:51.515Z /16November22:34:51CST, no error. Independent actual browser check completed 2026-11-17T04:36:20.807488+00:00. English displays Next review & rotation: Nov23,10:00AMCST; Arabic localized equivalent retained. Both languages passed1280x900desktop,390x844mobile and320x800narrow (6cases): schedule is exactly one line with no overflow, concise heading fits, All books link and three current cards retained, ArabicRTL correct, no page errors. Exercised real browser refreshLibrary with a simulated next week: schedule datetime and card selection advanced correctly, then restored the real current date/selection; no server data or schedule changed. Three existing Node library tests pass; hosted build and diffcheck pass. Screenshots ENmobile/ARnarrow personally inspected. Full catalogue's original separate schedule formatting and all books/pool/descriptions/downloads unchanged.

Evidence deliverables/library-schedule-compact-2026-11-16/LIVE-QA.json,check_live.py and6en/ar-desktop/mobile/narrow.png screenshots. Earlier QA first hit the previous deploy; another local test stopped printing Arabic under Windows console encoding, fixed only in the test harness. Final six actual-browser results above pass against matching release. No catalogue/artwork/article/Nile/price/audio/Worker or automation changes. Scheduling kept, only visitor wording/layout shortened. Owner request COMPLETE.

العربية: بقيت المواعيد ظاهرة، وجُمعت المراجعة والتبديل في سطر واحد موجز. اجتازت العربية والإنجليزية فحص المتصفح للحاسوب والهاتف والشاشة الضيقة، مع استمرار التحديث الأسبوعي للموعد والكتب دون تغيير الجدول.



## 17 November 2026 — Explicit weekday and time, checked against live schedule configuration

Owner asked to ensure the actual day/time when sections are supposed to change. Read the existing ACTIVE photo-review automation (Saturday10:30AmericaChicago) and Library research automation (Monday10:00AmericaChicago), and confirmed both match the IANA-Chicago Hugo/browser rotation boundaries. No automation/schedule edits. Compact notices now explicitly show abbreviated weekday, date, clock time and time zone; labels shortened to Review/rotation / مراجعة/تبديل to keep one-line layout. No-JavaScript fallback includes weekday too (Arabic weekday names localized). Actual next boundaries: photos Saturday21November2026 10:30CST /16:30UTC; Library Monday23November2026 10:00CST /16:00UTC. Daylight saving remains automatic. These are scheduled review/rotation times, not guarantees that a review yields a new publication. Existing active-tab/focused-link behavior unchanged. Future approved artwork display remains immediate under the separate168hour priority rule.

Three templates and two compact formatter options only; full capture dates/captions/credits/rights, Library records/cards/source/download links, weekly selection and full ISO time attributes preserved. Six existing Node update/DST/focus/selection tests and actual-Hugo EN/AR partial fixture pass. Production/browser checks recorded after deployment. Work/evidence deliverables/section-schedule-weekdays-2026-11-17.

العربية: جرى التحقق من المواعيد الفعلية: صور السودان يوم السبت الساعة10:30صباحاً، والمكتبة يوم الاثنين الساعة10:00صباحاً، بتوقيت شيكاغو مع التوقيت الصيفي تلقائياً. تُظهر التنبيهات الموجزة الآن اسم اليوم والتاريخ والوقت والمنطقة الزمنية بوضوح، دون تغيير الجداول أو محتوى الأقسام.


## VERIFIED LIVE — day/time made explicit

Release55295ce85c35c797589f3cc9f84d7ae5c5827194 matches ready Netlify6afcbe605667676e2a7e0f1d, published2026-11-17T20:52:44.247Z /17November14:52:44CST, no error. Independent actual CUA Chrome checks completed 2026-11-17T20:53:52.119Z. All six EN/AR routes (home/photos/fullLibrary) at1280and320px pass12cases: explicit Sat/السبت forphotos21Nov10:30CST, Mon/الاثنين forLibrary23Nov10:00CST; full ISO datetimes2026-11-21T16:30Z and2026-11-23T16:00Z; one-line/nooverflow notices andRTL retained. Viewportreset aftertesting;correctpublicviewport screenshot savedweekday-proof.jpg. Six existing Node date/DST/update/focus tests and actual-Hugo EN/AR fallbacks pass; explicit static weekday/date/time checks pass after reading the Arabic fixture as UTF8. Matching hosted build and diffcheckpass. SourceACTIVERULES inspected and appautomationcards viewed read-only: photoSA10:30, LibraryMO10:00, bothChicago. No scheduleorautomationchanges. New review material is not promised merely by the scheduled time, and focus protection remains unchanged.

Evidence deliverables/section-schedule-weekdays-2026-11-17/LIVE-CUA-QA.json,weekday-proof.jpg,build_fixture.py and modified-template/formatter snapshots. Labels shortened to Review/rotation / مراجعة/تبديل only to accommodate weekday without losing date/time. All data/cards/captions/credits/images/rights/content/Nile/price/audio/Worker state unchanged. OwnerrequestCOMPLETE.

العربية: تحققت المواعيد وظهرت بوضوح: صور السودان السبت10:30صباحاً، والمكتبة الاثنين10:00صباحاً بتوقيت شيكاغو، مع مراعاة التوقيت الصيفي تلقائياً. بقي التنبيه سطراً واحداً باللغتين على الحاسوب والشاشة الضيقة، دون تغيير الجدول الفعلي.

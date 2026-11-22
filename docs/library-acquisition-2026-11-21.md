# Kandaka Library acquisition — 21 November 2026

## Scope and reconciliation

Owner requests pending-source checks and verified bilingual Library additions. **Library only:** no editorial article, cover, category, publication approval, schedule or automation changes. Source-linked catalog publication is authorized by this request and standing Library instructions. Original source files and Calibre preserved.

Baseline main 771aff6b78083afc898f6e81d43ebad16df5b690: **577 records**. Both live Library editions independently downloaded before changes and each contained 577 cards. The original Pedagogy Under Fire / Pluriversal Pasts / UNICEF mid-year report batch and Rewind Forward already exist. Solar Energy Value Chain Study and SAMRA also already exist. No duplicate acquisitions made for them.

Two additions prepared: UNDP's Digital Financial Literacy in Sudan and the World Bank's October 2026 Sudan Macro Poverty Outlook. Result **579 records**. Exact bilingual catalog fields are retained in `data/library.json`; summaries explicitly distinguish evidence from proposed interventions, sample coverage and forecasts. Publication dates are not inferred from download-folder names.

## Metadata, review and rights

| Source | Bibliographic and access verification | Review boundary / rights |
|---|---|---|
| [Digital Financial Literacy in Sudan](https://www.undp.org/sudan/publications/digital-financial-literacy-sudan) | UNDP; landing page 5 November 2026; original PDF November 2026, 31 pages; separate launch release 12 November. Report-team credits checked in PDF acknowledgements. No DOI identified. | Selected executive summary and methods read through publisher-hosted web PDF text, not full report. No document-specific redistribution licence verified; consultation photos not cleared. Local PDF GET403. Official page and PDF locator retained, no hosted-copy claim. |
| [Macro Poverty Outlook for Sudan: Annual Meetings 2026](https://documents.worldbank.org/en/publication/documents-reports/documentdetail/099647210162618742) | World Bank, report216142; document1 October / disclosure16 October 2026. Two-page country PDF footer identifies October2026. No DOI assigned here. | Both pages and notes read through web PDF text; global volume not read. No document-specific mirror permission established. Local certificate validation failed, never bypassed. Country PDF URL rolls between editions; canonical dated repository record is main source. |

No PDF binary successfully acquired in this pass; no SHA256 or local PDF-integrity verification invented. No R2 upload attempted for these rights-uncleared sources. No source table, figure, photo or dataset reproduced. Original bilingual paraphrases only. Public readability does not grant redistribution rights.

## Duplicate and personal-library checks

Compared normalized title and exact official-source URLs against current repository catalog and downloaded live EN/AR cards. No matching new entry. Central-library README, CATALOG.csv and IMPORT_REPORT.json consulted; no exact candidate title found. Active `D:/New Caliber Library/metadata.db` queried **read-only** for financial-literacy / macro-poverty / multi-sector-needs title variants; no matching records. This is metadata duplicate screening, not a full-text audit of every Calibre file.

Prescribed Search-Library.ps1 fails because its hardcoded Python runtime no longer exists. Invoked the same content_index.py search with installed Python3.12 instead, using “digital financial literacy” and “Macro Poverty Outlook”. Returned unrelated/tangential book passages; none cited or treated as original-report evidence. No book newly claimed read, no quote/page citation introduced, no original or central catalog modified.

## Pending queue retained

1. **PDF archiving queue:** Suakin and the other seven entries in the 3November audit already have Library records. Need item-by-item original files, current redistribution/figure checks and verified Kandaka-only storage. November9 zero-upload notes are historical: multi-hazard and Old Dongola PDFs were subsequently archived and verified on November10. No new claim that all PDFs are missing, no reused legacy credentials or uploader execution. November18 safe uploader is dry-run-first and requires documented permission. No new R2 inventory audit or credential rotation claimed here.
2. **Khor Rafit:** existing record retained; publisher full text and licence/third-party scope still unresolved. Isotope portal already catalogued with restrictive terms; no dataset export.
3. **2026 Sudan Multi-Sector Needs Assessment:** official DTM country/index discovery located, but direct pages return403 and exact report/PDF access not established. **Held, not added**; indexed snippets and a third-party repost are not used to invent a full-text review, licence or file URL. Distinguish from UNHCR's2025 refugee assessment.
4. Further Sudanese-led Kush/Funj research and independent local housing/material evaluations remain discovery work. No fresh article commission created here.

## Validation and release

JSON/UTF-8, complete EN/AR fields, source/title uniqueness, old-record preservation and two-card delta checked. Scoped current-theme Hugo build renders Library only in both languages; no article content included in the isolated build. Both contain579 cards, one instance of each new record, matching official links and complete localized descriptions; Arabic RTL checked. This is a Library rendering check, not a full-site rebuild or browser visual audit. Normal hosted Netlify production build and independent live verification must be recorded separately after commit; local rendering is not publication evidence.

`library_inventory.csv` unchanged: no new stored object. `LIBRARY_SOURCES.md` and authoritative master workplan updated. Existing dirty checkout work untouched by alternate-index commit. Exact commit/deployment/live count evidence belongs in a separate receipt when observed.

**العربية:** أُضيف مصدران موثقان بملخصين عربي وإنجليزي وحدود واضحة للعينة والتوقعات. العدد المستهدف ٥٧٩ بدلاً من ٥٧٧، دون تكرار المصادر الموجودة. بقي تقييم الاحتياجات لعام ٢٠٢٦ معلقاً لتعذر الوصول المباشر إلى الأصل. لم يُحفظ ملف PDF أو تُغيّر المقالات أو كاليبر أو مواعيد النشر؛ تظل مهام الأرشفة والحقوق المعلقة مسجلة.

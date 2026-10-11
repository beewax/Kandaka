# A02, A11 and A12: bilingual release preparation

Prepared 10 October 2026, America/Chicago. These are authorized articles, not yet live releases. Latest user instruction explicitly requests finishing fact-checking, Arabic and covers, then publication every two days.

## Canonical files and release gates

| Order | Hugo content basename (both `.en.md` and `.ar.md`) | Conditional target | Status |
|---|---|---|---|
| A02 | `content/development/sudan-planned-before` | 12 October, noon Chicago | Complete bilingual editorial edition; protected with `draft: true` |
| A11 | `content/development/sudan-transformative-megaprojects` | 14 October, noon Chicago | Complete bilingual policy analysis; protected with `draft: true` |
| A12 | `content/development/sudan-deep-sea-ports` | 16 October, noon Chicago | Complete bilingual policy analysis; protected with `draft: true` |

The frontmatter dates are targets, not evidence of publication. L01 was independently verified live on 10 October at 16:24:39 UTC; A02 must not release before 12 October 11:25 CDT. Each subsequent article requires at least 48 hours after the previous successful release. If a deployment runs late, shift the next release; never catch up with a batch. At most one article per run. L02, L03 and L01 are complete; do not republish them or A05–A10.

At release: inspect current main and live pages for duplicates; refresh any changed time-sensitive claims; change only the next pair to `draft: false`, set their actual release date, run normal Hugo build and duplicate-cover check, push scoped changes, and independently verify both language URLs and cover. Record commit, Netlify deployment, actual publication time and verification time separately. The automation must not assume a successful push means live publication.

## Editorial provenance and scope

A02 is a transparent reconstruction of the established brief: the earlier conversation's claimed full draft was not recovered. The parent workspace retains that disclosure in `deliverables/articles/A02-sudan-planned-before-review.md`. This is a qualitative historical argument, not a quantified audit of every administration. No fabricated historical performance scores or unsupported personal corruption allegations appear.

A11 and A12 are policy analyses, not commissioned feasibility studies. No numerical project ranking, Sudan-specific cost quotation, approved construction timetable, current port draught, cargo forecast, concession-status claim or commercial mineral reserve is asserted. Project-specific engineering and financial appraisals remain necessary before any investment decision. That limitation is preserved in both languages rather than filled with invented numbers.

## Claim checks and changes

| Item | Evidence checked | Treatment in article |
|---|---|---|
| A02 planning chronology | Library of Congress, *Sudan: a country study* (1992; research completed June 1991), economic-development discussion | September 1962 adoption of the 1961–70 plan retained; no claim that planned expenditure or income gains were achieved |
| A02 contemporary primary record | UN General Assembly, 1136th plenary meeting, 28 September 1962, paragraphs 30–37 | Added breadth of planning priorities; explicitly separates projected gains from outcomes |
| A02 institutional changes | LOC banking discussion, scan page 226 | Added 1970 nationalization and 1974 encouragement of foreign banking as examples of changing policy, not a verdict on every bank |
| A02 oil and diversification | World Bank 2016 country economic memorandum summary | Retained dated 1999–2011 oil period; diversification discussion is historical, not a current GDP estimate |
| A02 transition | IMF/World Bank 29 June 2021 HIPC announcement; World Bank 27 October 2021 statement | Decision point is not completion or cancellation of every debt; newly added financing pause is explicitly historical, not a claim that all subsequent aid stopped |
| A02/A11 infrastructure | World Bank 2011 assessment | Used as historical context only; current asset condition requires fresh inspection |
| A11 electricity | IRENA costs in 2024; new 2026 *24/7 renewables* study, system-cost distinction | Added like-for-like reliability comparison; no global price is presented as Sudan's delivered tariff |
| A11 nuclear/minerals | IAEA Milestones page; verified Kandaka L01 analysis and its source trail | Nuclear infrastructure obligations separate from mineral occurrence; no reserve or profitability inference |
| A12 existing network | Sea Ports Corporation institutional overview | Added specialized existing port facilities; undated depth figures deliberately not repeated as current navigation data |
| A12 performance | UNCTAD TrainForTrade contribution to 2025 maritime review | Replaced older review reference with clearer source on transparency, communication and performance |
| A12 maritime risk | UNCTAD 24 September 2025 maritime-trade assessment | Updated dated context; explicitly not a live shipping advisory or terminal forecast |

All other recommendations are identified as Kandaka's proposals or analytical judgments. Arabic retains the same argument, section sequence, evidence, dates and limitations; it is not a catalogue summary. Each edition has eight substantive sections and more than 1,100 body words. The final A11 pass explicitly preserves Nuba Mountains participation, local ownership/revenue scrutiny, byproduct uncertainty, under-served states, women, youth, disability and older people's access.

### Sources

- [LOC study PDF](https://tile.loc.gov/storage-services/master/frd/frdcstdy/su/sudancountrystud00metz/sudancountrystud00metz.pdf); [catalogue metadata](https://www.loc.gov/item/92021336/); [banking scan list](https://www.loc.gov/resource/gdcmassbookdig.sudancountrystud00metz/?sp=10&st=list).
- [UN primary record](https://digitallibrary.un.org/record/732702/files/A_PV-1136-EN.pdf).
- [World Bank diversification](https://www.worldbank.org/en/country/sudan/publication/diversification-the-key-to-unleashing-sudans-economic-potential); [HIPC announcement](https://www.imf.org/en/news/articles/2021/06/29/pr21199-sudan-to-receive-debt-relief-under-the-hipc-initiative); [October 2021 pause](https://www.worldbank.org/en/news/statement/2021/10/27/world-bank-group-paused-all-disbursements-to-sudan-on-monday).
- [Infrastructure report](https://ppp.worldbank.org/sites/default/files/2022-06/AICD-Sudan-country-report.pdf).
- [IRENA 2024 cost evidence](https://www.irena.org/Digital-Report/Renewable-Power-Generation-Costs-in-2024); [IRENA 2026 study](https://www.irena.org/-/media/Files/IRENA/Agency/Publication/2026/May/IRENA_TEC_24-7_renewables_2026.pdf); [IAEA Milestones](https://nucleus.iaea.org/sites/nids/capacity/milestones/SitePages/Home.aspx).
- [Sea Ports Corporation](https://sudanports.gov.sd/web/ar/?page_id=51); [UNCTAD port performance](https://tft.unctad.org/en/2025/09/24/review-of-maritime-transport-2025-stormy-seas-for-global-shipping/); [UNCTAD maritime risk](https://unctad.org/news/maritime-trade-under-pressure-growth-set-stall-2025).

URL checks: 14 unique English source links inspected. Several institutional sites reject generic HTTP clients with 403 but were independently retrievable through indexed web source content; do not mislabel these as universally working or as missing documents. The UN PDF returns an anti-bot 202 response to the generic client; the source content was checked through the indexed primary-record result. The Sea Ports Corporation's separate 2025 statistics catalogue was located, but no uninspected figures from its PDF were used.

## Cover provenance

Generated in the user's Leonardo account on 10 October 2026 using **Lucid Origin**, Dynamic, Fast, 1344×768, one image per prompt. Public mode was already selected; these are not exclusive assets. No reference images were uploaded. Original JPEGs downloaded from image detail views, visually checked, and saved in `static/images/uploads/`. Both editions include synthetic-image captions and localized alt text.

| Article | File | Leonardo image ID | Seed |
|---|---|---|---|
| A02 | `sudan-planned-before-leonardo.jpg` | `6e7c05c0-16f3-4f37-a276-53b2c1e01d8b` | 784931602 |
| A11 | `sudan-transformative-megaprojects-leonardo.jpg` | `e900972c-f7c4-4fec-b2f1-6e19cc5f5670` | 891856173 |
| A12 | `sudan-deep-sea-ports-leonardo.jpg` | `ffd71605-d040-4015-8111-14a35c36b0fd` | 1097121105 |

Usage check: [Leonardo commercial-use guidance](https://intercom.help/leonardo-ai/en/articles/8044018-commercial-usage), updated 25 August 2026, and [terms](https://www.leonardo.ai/terms-of-service), dated 19 January 2026, checked during preparation. Own generations may be used commercially subject to terms; public assets carry platform reuse rights and no exclusivity is asserted. Images contain no real politician, documentary-event claim, mineral-reserve claim or approved project design. Existing credits only; no subscription or credit purchase.

### Exact prompts

**A02:** Wide editorial illustration for Sudan Planned Before: a quiet archive desk with plain unlettered folders, an open blank planning notebook, a pencil and a small wooden model of a railway bridge, a sunlit agricultural landscape beyond the window. Thoughtful painterly magazine art in warm ochre, brick and deep teal. Symbolic fictional scene about institutional memory and learning from development history, not an authentic historical document or actual project. Wide landscape composition, strong central focus, generous crop margins. No text, no numbers, no lettering, no logos, no flags, no real politicians, no watermark.

**A11:** Wide editorial magazine illustration for What Megaprojects Could Actually Transform Sudan: an elegant tabletop planning model showing a small solar array, simple railway freight line, irrigated fields and modest workshops connected as one coherent system. Deliberately visible wooden model edges and human-scale miniature structures, no futuristic skyline. Warm terracotta and deep teal palette, beautiful soft daylight, painterly paper texture. Fictional conceptual planning model, not an actual construction project. Landscape 16:9, central focus with safe crop margins. No words, no numbers, no logos, no flags, no watermark.

**A12:** Wide editorial illustration for Sudans deep-sea ports: fictional conceptual Red Sea coastal logistics landscape, a modest container terminal and cargo ship on clear teal water, connected inland to a freight railway and warehouses, small coastal town with low buildings, distant dry hills. Balanced painterly magazine art, warm ochre land and cool blue-green sea, no futuristic skyline, no military vessels. Clearly illustrative rather than photorealistic, not a depiction of Port Sudan or any approved project, no engineering claims. Wide landscape composition with a clear central focal point and generous crop margins. No text, no numbers, no logos, no flags, no watermark.

## Verification and deployment

Draft-inclusive Hugo build passed. Duplicate-cover audit passed across 2,318 Markdown files. All six draft pages were checked in Chrome at a 390px mobile viewport: correct English/Arabic direction, eight sections, loaded covers and no horizontal overflow. Generated HTML checks confirmed full bodies, metadata, localized alt text and no internal review notes. All three original JPEGs validate at 1344×768. Normal production output excludes all six draft URLs.

Homepage desktop check: Photos, Art and Library each span the same 1,052px content width within the 1,100px homepage container; three equal card columns each. English and Arabic mobile checks: single-column grids, no horizontal overflow. Article reading widths are unchanged. A deployment of the homepage correction does not count as an article release.

The existing `kandaka-six-article-publication-sequence` automation was updated through the app and confirmed ACTIVE, every two days at noon local time, with current prepared-file paths and the release gates above. The separate progress monitor was left unchanged. Future publication is scheduled work, not a completed deployment.

### Verified deployment record

Commit `721858343de801fdd0d67bc1859c1ad5fadf6c79` pushed to main. Netlify deployment `6acaec752f2c440008189281` is ready and published at **2026-10-11 01:55:43.944 UTC** (10 October 20:55 CDT). By 01:57 UTC, independent browser checks confirmed the new 1,100px homepage rule and equally wide Photos, Art and Library sections on https://kandaka.com/ and https://kandaka.com/ar/ . All six scheduled article URLs still returned HTTP 404, as intended. The articles are committed and scheduled, not published. Screenshot evidence is saved in the parent workspace at `deliverables/kandaka-home-layout-fixed.png`.

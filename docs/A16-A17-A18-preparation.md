# A16–A18 bilingual explainers — 12 October 2026

## Authorization and position in the queue

The user explicitly authorized full English and Arabic articles, Sudan-focused covers, and publication every two days after the existing queue, with review afterwards. This supersedes the preceding assistant message suggesting another approval would be needed. It does not waive factual checks or authorize early or batch publication.

| ID | Title | Content stem, both `.en.md` and `.ar.md` | Conditional earliest planning date, Chicago |
|---|---|---|---|
| A16 | Making a Living in Sudan: Wages, Inequality and the Road to Recovery | `development/sudan-living-wages-recovery` | 24 October 2026, noon |
| A17 | Protecting Sudan’s Memory: Museums, Communities and Recovery | `culture/protecting-sudans-memory` | 26 October 2026, noon |
| A18 | Miseeda: Reading Sudan’s History in One Nubian Landscape | `history/miseeda-nubian-landscape` | 28 October 2026, noon |

Order: A02 → A11 → A12 → A13 → A14 → A15 → A16 → A17 → A18. These dates extend the earlier conditional plan, not confirmed appointments. At preparation, A02 still has `draft: true` in main despite its 12 October noon target. Later dates must shift with actual releases. A16 may publish only after A15 is verified live and at least 48 hours after its successful release; the same gate applies thereafter. Library/homepage deployments do not reset the article interval. Do not skip an earlier item or publish these now simply because they are prepared.

## Research, independence and limitations

### A16

Starting source: the approved Library ERF Working Paper 1824. Retrieved publisher PDF `https://erf.org.eg/app/uploads/2026/03/1773746014_443_2884957_1824.pdf`; inspected income definitions and methods, printed pp. 6–8, and conclusions, pp. 36–38. Rendered and visually inspected printed p. 7 with pypdfium2 after the web screenshot and PyMuPDF paths were unavailable. The material limitation absent from the earlier abstract-only recommendation is that complete income information exists for approximately 70% of surveyed households. Both editions disclose this. No microdata reanalysis, current household-income estimate, precise inequality ranking or causal programme claim.

Independent institutional framing: ILO's dated 16 April 2024 Sudan statement and its wage-policy resource (links in both editions). These are not independent replications of the ERF data. The article deliberately separates household income from wages, nominal from real pay, household-head comparisons from all-women comparisons, and programme proposals from demonstrated effects. Hypothetical examples are labelled. Proposed support includes people unable to work, displaced people and women with disabilities; no hazardous-work advice. Existing A13/A15 focus on enterprises/farms; A16 focuses on workers and household security.

### A17

Starting Library source: Ahmed/Emberling's 2025 Antiquity guest editorial. Read its introductory scope, heritage/response discussion and dated update; do not treat it as a comprehensive contemporary inventory. Independently consulted UNESCO April 2026 training and 6 July 2026 museum project reporting. Both editions explain that project-phase completion does not prove full restoration, safe visitor access or collection security; repeated reporting on one programme is not independent evaluation. No definitive stolen/destroyed-object tally or legal conclusion about particular objects is presented.

Neal Spencer's 2021 ResearchSpace account supplies a critical comparative practitioner perspective on local authority and data access, not a current condition report. Article recommendations are explicitly Kandaka's: support custodians, maintain records, protect sensitive information, include diverse histories and communities, and assess outcomes beyond activity totals. Human safety and essential relief remain prior constraints. Distinct from monument histories and the Nubian clothing article.

### A18

Starting Library source: Ciesielska and colleagues' open-access September 2026 Antiquity project report (DOI 10.15184/aqy.2026.10427, CC BY 4.0). Read survey, ceramic, iconography, medieval and ethnography sections and conclusion. Preserve uncertainty over the petroglyph's date/identity and builders' intentions; preliminary site frequency is not a population census. Living memory is not used to date ancient carving or prove uninterrupted religious continuity. No claimed site visit.

Comparative source: Spencer's first-person Amara West/Beit Abri discussion. It informs governance questions only; it does not independently establish Miseeda chronology. Attempts to retrieve a further museum page and a community-archaeology publisher page were unsuccessful; they are not cited as reviewed evidence. The article differentiates observed features, project interpretations and Kandaka's educational proposals. Full source URLs and numbered footnotes match across editions. It is a landscape-history/evidence explainer, not a second clothing article.

## Sudan-focused covers and provenance

All three are unmodified photographs, not generated composites. Existing generic rejected covers are not reused. Downloaded originals visually inspected; alt text and source/licence captions are fully bilingual. Dates distinguish historical photos from current conditions. No claim about photographed individuals' earnings, religious identity or employment is made.

| Asset under `static/images/uploads/` | Creator and source | Licence / context |
|---|---|---|
| `omdurman-livelihoods-2009.jpg` | Petr Adam Dohnálek, [Omdurman market](https://commons.wikimedia.org/wiki/File:Bazaro_en_Omdurman_001.jpg); original `https://upload.wikimedia.org/wikipedia/commons/e/e4/Bazaro_en_Omdurman_001.jpg` | CC BY-SA 3.0 CZ; 14 August 2009; 1600×1200; unchanged |
| `sudan-national-museum-2013.jpg` | David Stanley, [Sudan National Museum](https://commons.wikimedia.org/wiki/File:Sudan_National_Museum_(8625532907).jpg); original `https://upload.wikimedia.org/wikipedia/commons/9/9f/Sudan_National_Museum_%288625532907%29.jpg` | CC BY 2.0; 12 February 2013; 1024×768; unchanged |
| `miseeda-church-lenarczyk.png` | S. Lenarczyk, figure 2 in the [Miseeda article](https://www.cambridge.org/core/journals/antiquity/article/miseeda-between-kingdoms-through-epochsreconstructing-a-history-of-the-mahas-region-sudan/36228B78AF514630836ECEE46ECE7C52) | Article CC BY 4.0; figure credit retained, no separate restrictive notice found; exact capture date unspecified; 1063×598; unchanged |

Miseeda original asset: `https://static.cambridge.org/binary/version/id/urn%3Acambridge.org%3Aid%3Abinary%3A20260923025735342-0922%3AS0003598X2610427X%3AS0003598X2610427X_fig2.png?pub-status=live`.

## Release gates and delivery boundaries

Six complete files are protected with `draft: true`. At release, refresh time-sensitive primary evidence and links, check for duplicate coverage and preserve these limitations. Confirm Arabic meaning parity, dates, credit links and covers. Build normally and audit covers, release only the eligible language pair, commit/push scoped files, and independently verify both live pages and cover. Record actual release and verification times. No new approval is required for these three within this scope; material thesis changes still require direction.

Preparation validation, commit and automation update are recorded below when completed. No live article release is claimed by drafting or a draft-inclusive build.

## Completed preparation checks

- Full bilingual editorial reading completed; qualifications, hypothetical examples, attribution and policy/source distinctions retained across pairs. Seven sections per edition; source URL and footnote parity checks pass. Approximate body counts including notes: A16 EN 1,249 / AR 1,071; A17 EN 1,292 / AR 1,093; A18 EN 1,321 / AR 1,084.
- Draft-inclusive Hugo build passed (990 EN / 2,270 AR pages); normal production build passed (953 EN / 2,217 AR). Existing `.Site.Data` deprecation warning only. All six new pages are absent from production output. `scripts/check_a16_a18.py` verifies full-length prose, matching references/covers, rendered headings, Arabic RTL and exclusion from production. Cover audit passed across 2,458 Markdown files.
- Browser inspected all six local pages: correct titles/direction, each cover loaded at original natural width and no horizontal overflow at the browser's default desktop viewport. Visually inspected Arabic Miseeda and museum title/cover screenshots. The initial sandbox preview server was unreachable from the browser; an external-sandbox loopback-only server resolved this. No mobile-specific browser test is claimed.
- Existing template displays the Arabic reading-time label as “a few seconds” despite full article length; this pre-existing site-wide metadata issue is outside this content-only change and should be addressed separately. Article word counts above are measured from source, not that label.
- Existing `kandaka-six-article-publication-sequence` automation updated through A18 and confirmed ACTIVE. Same ID, name, two-day noon cadence and target thread retained. Its prompt carries the new authorization, exact file stems, source limitations and photographic credits. Other automations unchanged.
- Preparation is ready for a scoped protected-draft commit with `[skip netlify]`; no article is released now. Publication remains conditional on the preceding queue and release-day checks.

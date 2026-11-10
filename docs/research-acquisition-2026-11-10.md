# Research integration and archive recovery — 10 November 2026

## Owner authorization and current scope

Owner said “Go ahead” after the outstanding PDF uploads and live-article integration were explained. This pass incorporates the 9 November research branch into current main, appends clearly dated English/Arabic updates to four existing published articles and deploys those updates. It creates no new article, changes no release cadence and preserves every pre-existing article byte, front matter and cover. The protected heritage article receives an explicit dated addendum under this follow-up authorization; its previously approved text is retained intact.

Fresh main baseline: `0bd9e0c7e6218c0c79707fe9d76dc1706046e25d`. The newer cool-roofs publication, draft first-year economic reform article, homepage/Library rotations and featured-book link repairs were inspected and preserved. The eight records from PR #21 (`8e7fc91dd427e3bf59775661763cbbaa15c246a5`) are reconciled into this baseline rather than replacing current files with stale versions.

## PDF successfully archived

**Musstafa, Ahmed Y. A.; Naimi, Sepanta; Aburqaq, Ismail S. A.; Amro, Suhib O. A. (2026). A Machine-Learning-Enhanced Geospatial Framework for Sustainable and Disaster-Resilient Infrastructure: Multi-Hazard Societal Impact Assessment in Sudan. Sustainability 18, 8269. Published 12 August 2026. DOI 10.3390/su18168269.**

- Publisher: https://www.mdpi.com/2071-1050/18/16/8269
- Original PDF: https://www.mdpi.com/2071-1050/18/16/8269/pdf
- Licence: CC BY 4.0, hyperlink verified in original PDF; author/title/year/DOI retained. Original unmodified. Nine figure captions/credits screened; no separate restriction found, while underlying third-party datasets retain their terms. No dataset tables or archaeology coordinates separately rehosted.
- Review remains selected full-text sections (abstract, methods, limitations, conclusions and data statement), not a full-paper reading or replication.
- Destination: `kandaka-library`, key `2026/musstafa-et-al-2026-multi-hazard-sudan.pdf`.
- Verified public URL: https://pub-0c3bb637d5f54b239fe4a4ef9b08bfe3.r2.dev/2026/musstafa-et-al-2026-multi-hazard-sudan.pdf
- Public download HTTP 200, `%PDF` signature, 8,680,814 bytes, 27 pages, SHA256 `b7f92aca1d5e044686495e3327ad1b19adc2fdab7bd8705cf9b8de24fbfe39ee`; identical to the previously verified publisher original. Authenticated R2 read independently returned 8,680,814 bytes.

The previous remote-source fetch failure was bypassed by uploading the verified local original through a temporary, tightly bounded Worker. It accepted only one fixed object, exact byte length and exact SHA256; no arbitrary keys, other files, reads or deletions were exposed. Conditional creation prevented overwriting an existing object. The temporary Worker was deleted immediately after upload; an authenticated lookup confirmed 404 / “This Worker does not exist”. No other Worker configuration was changed. The public PDF remains in the correct Kandaka bucket.

Catalogue now exposes a verified Download PDF label in both languages, with licence attribution; format/status maps and one inventory row updated. Other source PDFs remain publisher links where redistribution/third-party scope is unresolved. Earlier 9 November zero-upload statements are historical; current result is **one archived original PDF with verified public URL**. Do not describe the other four research downloads as Kandaka archives.

## Actual article changes

Each English/Arabic pair receives an appended, dated 10 November research section. Existing prose remains a byte-for-byte prefix, including original line endings. Checks and original SHA256 values are in `research-integration-2026-11-10-checks.json`.

| Existing article pair | Evidence integrated and its limits | Practical adaptation |
|---|---|---|
| `public-transport-urban-planning-sudan` | ANDUS external eight-page executive summary; €7.3m whole-programme envelope; no survey responses | Paid municipal/university/resident team; real walking/service checks; repair before expansion; recurrent finance |
| `sudan-urban-planning-strategy` | Sudan multi-hazard paper is state-level screening, not street safety or a working digital twin; original archived | Recent flood/outfall inspections, shade/dust/accessibility, housing/tenure protection, local builders and maintained short links |
| `film-tv-theatre-industry-sudan` | UNESCO Culture monitoring printed pp.11–12, not independent livelihood evaluation or a full-report reading | Locally run cultural workspaces, paid craft/visual-art work, creator rights and income continuity; repair before new complexes |
| `protecting-sudans-memory` | UNESCO September report: training/assessments and Sudanese resource persons, not conserved-object counts or reopening approval | NCAM/Sudanese-led safe triage, restricted records, affordable checklists, conservation jobs and long-term stewardship |

All added source URLs match across the bilingual pairs. Proposals are identified as Kandaka's adaptations. Existing article dates, draft flags, covers and release schedule are untouched. The already-published cool-roofs article and unreleased economic reform drafts are untouched. Three research candidates from the earlier pass remain research briefs, with no new publication inferred.

## Catalogue and duplicate preservation

567 → 575 entries; eight nonduplicate English/Arabic records retained from PR #21, one existing Action for Hope arts assessment metadata upgrade and one of the eight new entries switched to verified Kandaka PDF access. Current main's featured-link repairs remain intact. Existing live Windows Calibre/central-catalogue access gap remains; no claim of a fresh live-Calibre check. Older/undated MENA and Indonesia comparisons retain explicit labels.

## Validation and release receipt

- Existing catalogue validation passed: 575 records, previous canonical-source checks retained.
- JSON/UTF-8/Arabic and uniqueness checks passed; all original current-main catalogue records preserved except the documented arts-record upgrade.
- Eight article originals are byte-for-byte prefixes; metadata/covers unchanged.
- Hugo 0.160.0 full minified production build passed: 1,189 EN and 3,634 AR pages, 8.485 seconds. Existing Hugo `.Site.Data` deprecation warning remains unrelated.
- Both rendered Library editions contain 575 cards, the archive URL and correct download labels. All eight rendered articles contain dated additions; Arabic RTL retained. Results: `research-render-checks-2026-11-10.json`.
- Cover audit passed across 4,049 Markdown files. Git whitespace checks passed with existing CR-at-EOL permitted. Inventory change is one appended row.
- Visual browser test attempted: default Playwright browser binary missing; system Chromium launch failed `socket() failed: Operation not permitted`. No fresh visual browser inspection claimed; rendered-HTML checks above passed.

Prepared for owner-authorized production integration. The containing merge commit is the commit receipt. Actual Netlify deployment and public-page verification are recorded separately after completion; a local build alone is not a deployment claim.

## Remaining work

Other original-PDF rehosting requires clear redistribution and third-party rights; publisher links remain. Resolve Khor Rafit full text/licence and isotope-portal export terms before rehosting. Live Calibre/central-catalogue checks and additional Sudanese-led Kush/Funj and independent housing/local-material evidence remain next-pass work. No new source discovery or full-film viewing was undertaken in this integration pass. No outreach sent.

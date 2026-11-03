# Kandaka Library acquisition and article integration — 2 November 2026

**Status:** GitHub catalogue and article edits committed; independent production deployment and Calibre sync not verified. This file records what was done and what remains. It is not a publication authorization for new editorial articles.

## New source-linked bilingual Library records

Five records added to `data/library.json`, increasing its source-record count from **558 to 563**, after comparing title, DOI and source URL with the repository's existing records. This is a repository count, not independently verified live card count.

| Source | Review level | Rights / PDF outcome | Article or backlog |
|---|---|---|---|
| [SUM Middle Stone Age database](https://doi.org/10.5334/joad.215) | Full publisher HTML and dataset documentation; underlying OSF tables not opened | Article/data CC BY 4.0; PDF and raw tables not downloaded/rehosted; sensitive site coordinates not copied | Archaeology research backlog; A17 future reviewed revision |
| [Sudan flood susceptibility CNN](https://www.nature.com/articles/s41598-026-58194-7) | Full publisher HTML and official **13-page PDF text** reviewed, including methods and limitations; figures not independently reanalyzed | Article CC BY 4.0 subject to third-party exceptions. Direct official PDF at https://www.nature.com/articles/s41598-026-58194-7.pdf. Attempted download to working container failed; no binary uploaded | Urban strategy and A06 bilingual updates committed |
| [Omdurman urban heat](https://www.intechopen.com/online-first/1254135) | Full publisher HTML and methods reviewed, not independent replication | Publisher indicates CC BY 4.0; PDF download attempt did not yield an accessible binary; link only | Urban strategy and A06 bilingual updates committed; cool-roofs case study |
| [World Bank Urban Awakening](https://documents.worldbank.org/en/publication/documents-reports/documentdetail/099092526225029466) | Official executive synopsis and key findings reviewed; full technical PDF not reviewed | Official PDF linked at publisher; individual reuse license not confirmed, no binary mirrored | Urban strategy and A06 bilingual updates committed; municipal finance |
| [Suakin urban regeneration](https://doi.org/10.3389/fbuil.2026.1868485) | Full open publisher HTML reviewed; 25 purposive stakeholder interviews, not a representative survey | Frontiers open access CC BY, third-party figure rights require separate review; no PDF mirrored | Suakin/heritage-led urban regeneration backlog; A17 future reviewed revision |

## Download / storage attempt

Tried to download the official Nature PDF to `/mnt/data/sudan_flood_susceptibility_2026.pdf` via the available downloader. The download failed. The container network could not resolve Nature or IntechOpen hosts for direct requests. The publisher PDF is readable through the web retrieval system, but its binary cannot be passed through that interface to the working filesystem. No accessible authenticated binary-upload path to Kandaka's R2/Calibre was established in this session. **Do not claim a PDF is in Kandaka storage, Calibre, or the public Library.** Link to the official PDF until a permitted, verifiable upload route is available. Copyright/licence clearance remains per item; public access alone is not blanket permission to rehost.

## Article edits

- `content/development/sudan-urban-planning-strategy.en.md` and `.ar.md`: added Sudan flood-model caveats, Omdurman heat-measurement caution and municipal finance/job-access lessons.
- `content/development/public-transport-urban-planning-sudan.en.md` and `.ar.md`: added flood/heat screens for corridors and accessible employment links.
- Preserved titles, covers, draft flags, dates and existing publication cadence. No new article publication was initiated.
- A17 *Protecting Sudan's Memory* was individually approved and published; do not silently alter its approved text. SUM and Suakin research are flagged for a separately reviewed future addendum.
- Suakin's source is new to the checked Library even though the article had appeared in prior research watches. Avoid announcing it as a newly published November paper.

## Standing operating instructions (owner confirmed 2 November)

On each Kandaka research-watch pass:
1. Screen `data/library.json`, `LIBRARY_SOURCES.md`, `My books.csv`/Calibre export, previous watches, and actual article content first. Use title, DOI, publisher URL and edition identifiers. State when live Calibre DB is inaccessible.
2. Search for **new worthy original works** as well as corrections to existing articles. Prioritize Sudanese institutions, original datasets, full research, policy evaluations, art/film, archaeology, heritage and urban planning; include implementation-tested low-cost comparators.
3. For each worthwhile item, check publication date, authors, source authenticity, full-text availability, licence and third-party rights. Download a PDF only if legally reusable and the upload destination is actually available; verify bytes, page count and storage link before marking it archived. Otherwise link the official original.
4. Add bilingual catalogue metadata and substantive, appropriately qualified summaries to Kandaka Library; mark **full-text reviewed**, **partial/full PDF text reviewed**, **abstract only**, or **research lead**. Distinguish estimates, targets, outcomes and unverified claims.
5. Apply verified material findings to editable article drafts or dated addenda in English and Arabic. Respect individual approval and release gates; do not publish a new article, change a reviewed protected edition or alter cadence without authorization.
6. Update **KANDAKA_MASTER_WORKPLAN.md**, the Library source register and a dated research/acquisition log on every substantive pass, including successful commits, deployment verification, blockers and next actions. Do not leave a recommendation untracked or report an unverified upload as complete.

**Next actions:** Verify Netlify deployed the five new bilingual catalogue cards and the four revised article pages; locate an authorized R2 binary-upload workflow or a mounted Calibre connection; seek independently readable official PDF bytes and validate before archival; advance cool-roof and Suakin heritage-led regeneration article drafts separately under existing approval rules.

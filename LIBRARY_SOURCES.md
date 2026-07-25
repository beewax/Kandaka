# Library Sources — Sudan Research Discovery

Reference list of sources searched for Sudan-related economic/development papers to add to `data/library.json`. Used across Batches 1–5 (July 2026). Reuse this list for future batches instead of re-deriving search strategy from scratch.

Total library size after Batch 5 + manual R2 hosting: **506 entries**. Batches 1–5 added 58 new Sudan-focused papers (38 link-only from academia.edu/ScienceDirect, 9 R2-hosted + 10 link-only from the sources below, 1 originally-requested paper added directly). 39 previously link-only entries were later converted to R2-hosted downloads after the user manually uploaded PDFs.

## R2 buckets

There are two R2 buckets in play — **use `kandaka-library` for everything going forward**:

| Bucket | Public URL | Status |
|---|---|---|
| `kandaka-library` | `https://pub-0c3bb637d5f54b239fe4a4ef9b08bfe3.r2.dev` | **Current/active.** All new uploads (Batch 5 R2-hosted entries + 39 user-uploaded PDFs) go here. `upload_new_batch.py` points here as of July 2026. |
| `nilebookstore-books` | `https://pub-a5e3b47fe87749f491660d68e2029284.r2.dev` | Legacy. Backs older `library.json` entries (the original ~448-book set plus early batches). Still live — do not break these links — but no new uploads should go here. |

R2 credentials (account-level, work for both buckets) are in `upload_new_batch.py`.

## Source checklist

| Source | Base URL | Access | Notes |
|---|---|---|---|
| academia.edu | academia.edu | Login required for PDF | Metadata (author/year/abstract) scrapable via static HTML fetch even when logged out. Used in Batches 1–4. |
| ScienceDirect / Journal of Development Economics | sciencedirect.com/journal/journal-of-development-economics | Paywalled | Abstract-only usually. Check core.ac.uk for a free mirror before assuming locked. |
| RePEc / IDEAS | ideas.repec.org | Free | Best general economics index. Search: `site:ideas.repec.org Sudan <topic>`. |
| SSRN | papers.ssrn.com | Free download, no login | Search: `site:papers.ssrn.com Sudan <topic>`. Working papers, often newer/unpublished research. |
| CORE | core.ac.uk | Free (aggregator) | Good for finding open-access mirrors of paywalled journal articles. |
| Semantic Scholar | semanticscholar.org | Free (aggregator) | Similar to CORE; sometimes has a direct PDF button for paywalled DOIs. |
| Google Scholar | scholar.google.com | Free (aggregator) | Use "All versions" link to find free-hosted copies. |
| Unpaywall | unpaywall.org | Free (DOI lookup) | Takes a DOI, confirms whether *any* legal free copy exists. |
| World Bank Open Knowledge Repository | openknowledge.worldbank.org | Free | Country economic updates, sector diagnostics. Bitstream `/content` URLs are unreliable via plain curl (session/XSRF gated) — use the `documents1.worldbank.org/curated/en/<id>/pdf/<file>.pdf` mirror instead, which serves direct PDFs. |
| IMF (imf.org + elibrary) | imf.org/en/Countries/SDN | Free | Article IV consultations, Selected Issues papers, working papers — all directly downloadable PDFs at `imf.org/-/media/...` or `imf.org/external/pubs/ft/...`. |
| African Development Bank (AfDB) | afdb.org/en/countries/east-africa/sudan | Mixed | Country Outlook web pages are free; direct PDF links (`afdb.org/fileadmin/...`) are often blocked by bot protection (403) — link to the web page instead. |
| AERC (African Economic Research Consortium) | aercafrica.org | Free | Working papers directly downloadable, e.g. `aercafrica.org/old-website/wp-content/uploads/.../RP###.pdf`. |
| ERF (Economic Research Forum) | erf.org.eg | Free | Policy briefs and working papers directly downloadable via `erf.org.eg/app/uploads/...pdf` links found on each publication page. |
| University of Khartoum — Agricultural Economics Working Paper Series | onlinejournals.uofk.edu/aewps | Free | OJS-hosted; PDF link pattern `onlinejournals.uofk.edu/aewps/en/article/download/<id>/<file>`. |
| MDPI journals (e.g. *Economies*) | mdpi.com | Open access, but bot-blocked | Articles are genuinely free but MDPI blocks non-browser requests (403 to curl/fetch) — link to the article page rather than trying to host the PDF directly. |
| JSTOR | jstor.org | Free registration, limited reads/month | Older development-economics literature. |

## ⭐ Sudan Open Archive — check this first for almost any topic

**sudanarchive.net**, run by the Rift Valley Institute, is a free, full-text-searchable database of **3,000+ books, documents, and grey literature** covering nearly every angle of Sudan and South Sudan — history, governance, culture, legal/political documents, humanitarian records, and more. RVI is a signatory of the Budapest Open Access Initiative; everything is downloadable under Creative Commons licences, no login. Before building a new domain-specific batch, search this archive first — it likely has candidates across several tags at once. RVI's main site (`riftvalley.net/publication`) also publishes standalone research papers, all free PDF.

## Archaeology & Heritage sources

Added July 2026 for expanding coverage of the site's "Ancient Sudan," "Archaeology & Heritage," and "Nubian History" tags — repositories, museums, and institutions with Sudan/Nubia-specific holdings.

| Source | Base URL | Access | Notes |
|---|---|---|---|
| Sudan Archaeological Research Society (SARS) | sudarchrs.org.uk | Free | UK charity dedicated to Sudan/South Sudan archaeology. Publishes the journal *Sudan & Nubia* (open archive of back issues), maintains a survey/excavation archive housed at the British Museum, and keeps a curated links page (`sudarchrs.org.uk/resources/links`) worth checking periodically. |
| Sudan Memory | sudanmemory.org | Free | British Council/Aliph Foundation/King's College London project — 60,000+ digitized documents, photographs, maps, and films on Sudanese cultural heritage, including the SARS Edwards and Greenlaw photo collections. |
| British Museum Collection Online | britishmuseum.org/collection | Free | Searchable database of 4M+ objects; the Egypt and Sudan department holds one of the leading Nubian studies collections. Qatar-Sudan Archaeological Project excavation reports (Dangeil, Amara West, etc.) are archived at `britishmuseum.iro.bl.uk`. |
| Museum of Fine Arts, Boston — Nubian Art | mfa.org/collections/nubian-art | Free (browsable) | The most extensive Nubian art collection outside Khartoum, from the Harvard–MFA Expedition (1913–1932, George Reisner). No bulk-download API; browse/cite individual object pages. |
| Institute for the Study of Ancient Cultures (formerly Oriental Institute), U. of Chicago | isac.uchicago.edu | Free | Nubian Gallery collection pages plus digitized publications (e.g. *Lost Nubia*, Nubia Salvage Project reports) — check `isac.uchicago.edu/museum-exhibits`. |
| SFDAS — Section Française de la Direction des Antiquités du Soudan | sfdas.com | Free | French archaeological mission in Sudan; publishes excavation reports and maintains a bibliography of Sudan/Nubia archaeology. |
| Sudan Digital (heritage registry) | via UNESCO / culturalheritage.news | Free | DAI–NCAM collaboration building a digital heritage registry for Sudanese sites and objects; still developing, monitor via UNESCO Sudan culture pages and culturalheritage.news. |
| National Corporation for Antiquities and Museums (NCAM), Sudan | Khartoum-based; no stable public repository found | Limited | Sudan's own antiquities authority. No searchable online database as of July 2026 — reachable indirectly via UNESCO/Culture in Crisis/Sudan Digital partner reporting. Worth rechecking periodically in case a public portal launches. |
| ISAW NYU (Institute for the Study of the Ancient World) | isaw.nyu.edu | Free | Nubia exhibition bibliographies and academic resources; good secondary-source aggregator. |
| Fitzwilliam Museum, Cambridge | fitzmuseum.cam.ac.uk | Free | "Photographic Culture and Community in 20th-Century Sudanese Nubia" project — historical photography and ethnography. |
| JSTOR (archaeology titles) | jstor.org | Free registration, limited reads/month | Good for *Kush* (Sudan Antiquities Service journal) and *Meroitica* series back-catalogue when not otherwise findable free. |

## Governance, conflict & policy sources

| Source | Base URL | Access | Notes |
|---|---|---|---|
| Small Arms Survey — HSBA (Human Security Baseline Assessment) | smallarmssurvey.org | Free | Long-running project on armed groups, arms flows, and conflict dynamics in Sudan/South Sudan. Issue briefs and working papers are direct free PDFs (`smallarmssurvey.org/sites/default/files/resources/...pdf`); also publishes the "Sudan Facts & Figures" data resource. |
| International Crisis Group | crisisgroup.org/africa/horn-africa/sudan | Free | Ongoing analysis, briefings, and reports on Sudan's conflict; all free to read/download. |
| Chatham House | chathamhouse.org | Mixed | Most articles/reports free; some (e.g. "The World Today" magazine pieces) may be subscriber-only. Good for gold/conflict-economy and diplomacy angles. |
| ReliefWeb (OCHA) | reliefweb.int/country/sdn | Free | Huge archive of situation reports and assessments across every humanitarian sector (not just crisis-response) — useful for governance, economy, and infrastructure angles too. |
| Humanitarian Data Exchange (HDX) | data.humdata.org/group/sdn | Free | Structured datasets (displacement, education indicators, economic indicators) rather than narrative reports — useful for sourcing figures/citations rather than standalone library entries. |

## Environment, climate & water sources

| Source | Base URL | Access | Notes |
|---|---|---|---|
| UNEP Sudan | unep.org/sudan | Free | "Sudan First State of Environment and Outlook Report 2020," post-conflict environmental assessments, climate adaptation program reports — direct PDF downloads. |
| FAO Knowledge Repository | openknowledge.fao.org | Free | Sudan country profiles and farming-systems reports; bitstream URLs pattern similar to World Bank OKR (`openknowledge.fao.org/server/api/core/bitstreams/<id>/content`). |
| Nile Basin Initiative | nilebasin.org / nileis.nilebasin.org | Free (some registration) | Technical reports, an Atlas, and specialized databases (dams, water quality, climate scenarios) for the whole Nile Basin including Sudan. |

## Gender & education sources

| Source | Base URL | Access | Notes |
|---|---|---|---|
| UN Women Digital Library | unwomen.org/en/digital-library | Free | Sudan-specific gender alerts and assessment reports (e.g. food insecurity and gender, women's role in the current conflict) — direct PDF downloads. |
| LSE Middle East Centre | lse.ac.uk/middleeastcentre | Free | Academic reports on Sudanese women's leadership and related social-science topics. |
| UNESCO Institute for Statistics (UIS) | uis.unesco.org | Free | Sudan education-statistics country profile (PDF) and the broader UNESCO data portal for SDG 4 indicators. |
| UNESCO Sudan Education Policy Review | sudan.un.org | Free | Full policy-review PDF ("Paving the Road to 2030"). |

## Arts, literature & anthropology sources

| Source | Base URL | Access | Notes |
|---|---|---|---|
| Banipal — Magazine of Modern Arab Literature | banipal.co.uk | Mixed | Issue 55 was devoted entirely to Sudanese literature (fiction, poetry, essays); some content free online, back issues may require purchase. |
| ArabLit & ArabLit Quarterly | arablit.org | Free (articles) | Curated guides to Sudanese literature available in English translation — useful for compiling a reading-list style library entry rather than a single paper. |
| African Studies Quarterly | journals.flvc.org/ASQ | Free (diamond open access) | Fully open-access African Studies journal; search for Sudan-tagged articles. |
| Journal of Eastern African Studies / Northeast African Studies | tandfonline.com/journals/rjea20 · muse.jhu.edu/journal/136 | Paywalled | Leading academic venues for Sudan/Horn of Africa anthropology and area studies — mostly paywalled, but check individual articles for OA status via Unpaywall before assuming locked. |

## What "R2-hostable" means in practice

Sources marked "Free, direct PDF" above (RePEc-linked originals, SSRN, IMF, AERC, ERF, University of Khartoum, World Bank via `documents1.worldbank.org`) can be downloaded server-side and uploaded straight to the R2 bucket for a real "Download PDF" button — no need to ask the user to grab them manually. academia.edu, ScienceDirect, and MDPI cannot (login wall / bot-blocked), so those stay link-only unless the user grabs the PDF themselves.

## Search query patterns that worked

- `site:ideas.repec.org Sudan <topic>`
- `site:papers.ssrn.com Sudan <topic>`
- `site:openknowledge.worldbank.org Sudan <topic>`
- `AERC working paper Sudan <topic>`
- `IMF working paper Sudan <topic> pdf`
- `African Development Bank Sudan <topic> pdf`
- `ERF working paper Sudan <topic> author`

## Process for a new batch

1. Run the search patterns above for topics not yet well covered (see `data/library.json` tags for coverage gaps).
2. Dedupe candidate titles/URLs against `data/library.json` (`source` and lowercased `title`).
3. For each candidate, test with `curl -sL -o test.pdf "<url>" && file test.pdf` — if it returns a real PDF, host it on R2 (see `upload_new_batch.py` pattern); if not, add as link-only.
4. Write bilingual (EN/AR) `title_ar`/`desc_ar` fields.
5. Append to `data/library.json`, and to `library_inventory.csv` for any R2-hosted files.
6. Stage with `git add data/library.json library_inventory.csv` — do NOT `git add -A` (repo has unrelated line-ending noise across hundreds of files).
7. User commits/pushes manually from PowerShell, then manually triggers the Netlify deploy (push alone does not auto-deploy).

## Monitoring

A weekly scheduled check searches these sources for new Sudan papers not yet in `data/library.json` and reports candidates — no auto-add, review before batching them in.

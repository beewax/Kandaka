# Library Sources — Sudan Research Discovery

Reference list of sources searched for Sudan-related economic/development papers to add to `data/library.json`. Used across Batches 1–5 (July 2026). Reuse this list for future batches instead of re-deriving search strategy from scratch.

Total library size after Batch 7 (university archives, August 2026): **510 entries**. Batches 1–6 added Sudan-focused papers from academia.edu/ScienceDirect, the sources below, and the Sudan Open Archive; 39 previously link-only entries were later converted to R2-hosted downloads after the user manually uploaded PDFs; 13 entries were subsequently removed for being about South Sudan rather than Sudan (see Scope note below). Batch 7 added 3 Nubia/Sudan items from U Chicago ISAC and 4 collection-level entries for Durham's digitized Sudan Archive publication series (see "University archives & repositories" below).

## ⚠️ Scope: Sudan only, not South Sudan

South Sudan became an independent country in 2011. The Kandaka library is about the **Republic of Sudan** — South Sudan-specific content (Dinka/Nuer ethnography and language, Juba, Wau, South Sudan government reports, etc.) does not belong here even though many sources (especially the Sudan Open Archive) cover both countries without distinguishing, since most of their material predates the 2011 split.

Before adding a candidate, ask: is this genuinely about the Republic of Sudan, or about South Sudan / the wider pre-2011 unified Sudan region? Reject or flag anything that's really about South Sudan. Exceptions that are OK to keep: material that's explicitly comparative/joint (covers Sudan substantively too, e.g. a joint post-conflict analysis of both countries) or that predates any meaningful north/south distinction (e.g. ancient Kush/Nubia/Meroe history, which is geographically within modern Sudan). When genuinely ambiguous, ask the user rather than guessing.

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

## University archives & repositories

Added August 2026 in response to a direct ask ("Durham University and university of khartoum Sudan Archives and other universities"). None of these offer a subscribable feed (no RSS/API) — they're catalog-based and get mined periodically, same workflow as Sudan Open Archive. Distinguish "open, bulk-downloadable" from "reading-room/catalog only" before expecting a batch to produce entries.

| Source | Base URL | Access | Notes |
|---|---|---|---|
| Durham University — Sudan Archive | libguides.durham.ac.uk/asc-sudan-archive | Mixed | The major UK repository of Condominium-era Sudan material (administrators' papers, ~50,000 digitized photos, 150+ films) — but most of the archive is reading-room-only at Palace Green Library. The genuinely useful part: several full publication series have been digitized and are freely browsable online (not bulk-downloadable — each issue opens in a IIIF image viewer, no direct PDF): **Sudan Intelligence Reports / Sudan Monthly Record** (`.../sirs`, hundreds of monthly issues 1889–1958), **Governor-General Reports** (`.../ggrs`), **Sudan Government Gazettes** (`.../gazettes`), **Sudan Staff Lists** (`.../staff`), **Sudan Maps** (`.../maps`). Added as one collection-level library entry per series rather than one entry per issue — hundreds of individual monthly reports don't fit the site's per-book/report granularity. |
| University of Khartoum — Khartoumspace | khartoumspace.uofk.edu | **Currently offline** | Institutional repository (DSpace) — theses, journal articles, reports, open access by design when it's up. As of August 2026 the domain resolves to a bare default nginx page (not a real 404, not bot-blocked — looks like the backing server itself isn't configured/running). This tracks with widely reported war damage to University of Khartoum's physical campus and infrastructure since April 2023; the university has only been planning a return to its original campus for the 2026–2027 academic year. Re-check periodically — this is infrastructure-recovery-gated, not a dead link to give up on permanently. |
| Sudan Memory | sudanmemory.org | Free, but bot-gated (Anubis proof-of-work challenge — resolves automatically after ~5–10s, no CAPTCHA/human step needed; browser automation required, plain curl won't get through) | British Council/King's College London heritage digitization project. Primarily a **photograph, museum-object, and oral-history** archive (Khalifa House Museum store, community photo collections, etc.), not a text/document repository — doesn't slot into individual "Download PDF" library entries the way Sudan Open Archive or Khartoumspace do. Worth citing/browsing for context and imagery, not a batch-mining target for new library.json rows. |
| SOAS, University of London — Special Collections | soas.ac.uk/soas-library/special-collections · digital.soas.ac.uk/asc | Reading-room only | Strong Sudan holdings within their African/Middle East archives (3km of archives, 60,000 rare books). No bulk digitized text online — searchable catalog only. Use for citations/context, not downloadable entries. |
| Oxford — Bodleian Libraries (Commonwealth & African Studies, Rhodes House) | libguides.bodleian.ox.ac.uk/modern-sc/commonwealthafrican | Reading-room only | Sudan material under DT154.1-159.9; maps and Commonwealth/Africa manuscripts. Catalog/finding-aid access only. |
| Cambridge University Library — Royal Commonwealth Society Collection | cam.ac.uk | Reading-room only | Africa-focused historical collection; African Studies Centre Library separately holds 30,000+ books. Catalog access only. |
| University of Chicago — Institute for the Study of Ancient Cultures (ISAC, formerly Oriental Institute) | isac.uchicago.edu/research/publications | **Free, direct PDF — genuinely R2-hostable/linkable, strong source** | Unlike the above, ISAC's entire publication backlist (Oriental Institute Publications/OIP, Oriental Institute Museum Publications/OIMP, going back to the 1920s–30s) is freely downloadable as PDF directly from `isac.uchicago.edu/sites/default/files/uploads/shared/docs/...` — confirmed via direct curl, not bot-blocked. Nubia/Sudan-specific titles found and added: *Ancient Nubia* (OI Museum gallery guide), *Lost Nubia: A Centennial Exhibit of Photographs from the 1905–1907 Egyptian Expedition* (OIMP 24), *Paleolithic Man and the Nile-Faiyum Divide in Nubia and Upper Egypt* (OIP 17, 1933). The Nubian Expedition excavation report series (OINE, ~10 volumes on Aswan High Dam salvage archaeology, 1960s excavations) wasn't found in the OIP/OIMP listing pages fetched — worth a follow-up check of the "Miscellaneous Publications" and "Individual Scholarship" pages at isac.uchicago.edu/research/publications. |
| Boston University | library.bu.edu/precolonialafrica/kingdoms | Not a real archive — skip | No dedicated Sudan/Nubia archaeological repository exists at BU. Its role in Nubian archaeology is historical (the Harvard-Boston Expedition under George Reisner, 1913–1916, at Kerma) — those finds live at the Museum of Fine Arts Boston (already in the Archaeology & Heritage table above) and Khartoum, not in a BU-hosted collection. BU Libraries' own resource here is just a general web guide page on pre-colonial African kingdoms, not a document source. Don't batch-mine this. |

## R2 upload credentials — check before relying on this

The R2 access key embedded in `upload_new_batch.py` (`b1f53194...`) **failed with "Unauthorized" on both read (ListObjectsV2) and write (PutObject) as of August 2026** — this is a change from earlier in the project when the same key worked. Cause not diagnosed (revoked/rotated token, expired credential, or account-side change — needs checking in the Cloudflare dashboard directly, which isn't accessible from a sandboxed session). Workaround used for the ISAC batch: when the source PDF is already stably hosted on a real institutional domain (not gated behind login/bot-protection), skip R2 mirroring entirely and set `source` directly to the original URL — `list.html` already renders a "Download PDF" button for any `source` ending in `.pdf`/`.epub`, R2 hosting isn't required for that. Only academia.edu-style gated sources still need the user to manually download + Abdulla to grant fresh R2 credentials for mirroring.

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

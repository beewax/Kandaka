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

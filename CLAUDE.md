# Kandaka (kandaka.com) — working notes for Claude

## What this is

A bilingual (English/Arabic) editorial site about Sudan: economic development, history, archaeology, and current affairs. Abdulla is the primary author of original long-form analysis. It is a substantive editorial project, not a technical demo.

**Intellectual grounding** every "Ideas" and "Development" essay should draw on: Ha-Joon Chang's infant-industry framework, Walter Rodney's active-underdevelopment thesis, Acemoglu's inclusive-vs-extractive-institutions framework, William Foote Whyte's Mondragón cooperative model, and the Islamic intellectual tradition. Articles connect Sudan's present challenges to historical precedent rather than treating underdevelopment as natural or inevitable.

**Voice**: flowing analytical prose, no bullet points in body copy. Long essays (1,500–3,000+ words) are normal for `content/ideas/` and `content/development/`.

## Tech stack

- **Hugo (0.160.0) + PaperMod theme**, config in `hugo.toml`
- **GitHub**: `beewax/Kandaka`, `main` branch — this is the source of truth
- **Netlify**: auto-deploys on push to `main`; build command in `netlify.toml` runs `pip3 install -r requirements.txt && (delete + refetch content/news) && python3 scripts/fetch_news.py && hugo --minify`
- **Cloudflare R2** bucket `nilebookstore-books`: hosts PDFs/epubs for the Library, public base URL `https://pub-a5e3b47fe87749f491660d68e2029284.r2.dev` (note: some library entries use a different R2 public URL, `https://pub-0c3bb637d5f54b239fe4a4ef9b08bfe3.r2.dev` — check `data/library.json` per-entry rather than assuming one bucket URL)
- **Local environment (Windows)**: repo at `C:\Users\Abdulla\Kandaka`, PowerShell terminal, Calibre library at `D:\New Caliber Library`, source Sudan PDFs at `C:\Users\Abdulla\Documents\Sudan PDFs`

## Content conventions

- Bilingual pairs: `[slug].en.md` and `[slug].ar.md`, same slug, both under the matching section directory (`content/ideas/`, `content/development/`, `content/posts/`, etc.)
- Arabic content directory root is `content/ar/`; language config (`languages.en` / `languages.ar`) is in `hugo.toml`, Arabic is RTL
- **Frontmatter for an Ideas/Development essay:**
  ```yaml
  ---
  title: "..."
  date: 'YYYY-MM-DD'
  author: "Kandaka"   # or "كنداكة" in Arabic files
  category: "..."      # free-form, e.g. Energy, Education, History, Urban Planning, Culture — no fixed enum, just be consistent
  description: "..."   # 1-2 sentence summary, used in listings/meta
  tags: ["...", "..."]
  draft: false
  ---
  ```
- Essays typically open with an inline hand-authored SVG banner (`viewBox="0 0 800 220"`, rounded corners, thematic illustration, small caption text at the bottom) before the prose body — see any file in `content/ideas/` for the pattern. Not strictly required but is the house style for this section.
- Essays close with a `## Further Reading — Kandaka Library` section linking specific R2-hosted PDFs from `data/library.json` with a one-line description of each — **only include this if a genuinely relevant library entry exists**; don't force a weak link. (Checked June/July 2026: no cinema/film/media-specific library items exist yet.)

## Publishing mechanics — this is the important one

- `hugo.toml` sets `buildFuture = false`. A post with a future `date:` will **not** appear in any build until that date has passed.
- `.github/workflows/daily-news.yml` runs on a cron (`0 6 * * *`, 6am UTC / 9am Sudan time) and simply POSTs to `secrets.NETLIFY_BUILD_HOOK` to trigger a fresh Netlify rebuild.
- `.github/workflows/daily-rebuild.yml` (misleadingly named — it fetches news/images, not a rebuild trigger) runs on the same cron, fetches news + images via `scripts/fetch_news.py` / `scripts/fetch_images.py`, and commits/pushes any new content.
- **Net effect: delayed/scheduled publishing already works with zero extra tooling.** To schedule an essay for a future date, just set `date:` to that future date in the frontmatter and push it now (or anytime before). It stays invisible until the date passes, and the existing daily cron will pick it up and go live automatically the next time it fires after that date — no Netlify scheduled function, no external scheduler, no manual trigger needed. If you need it live faster than the next 6am UTC cron tick, manually run the "Daily News Refresh" workflow via `workflow_dispatch` in GitHub Actions, or just push any new commit (any push triggers Netlify's normal git-based deploy too).

## Git / push access — known limitation

- When working inside a Cowork/sandboxed session with this folder mounted, the mounted filesystem gives read/write access to files, but the sandbox does **not** have the user's GitHub push credentials (no credential helper, no cached token/SSH key for `https://github.com/beewax/Kandaka.git`). **Do not attempt `git push` from a sandboxed session** — it will fail or hang on auth. Create/edit the content files, then tell Abdulla to run his normal workflow himself: `git add <specific files> → git commit → git pull --rebase → git push`.
- **Only `git add` the specific files you actually changed.** A `git status` in a sandboxed/mounted session may show a huge number of unrelated files as "modified" — this is a line-ending/permission artifact of mounting a Windows checkout into a Linux container (`core.filemode=false`, `core.symlinks=false` are set locally for this reason), not real content changes. Never run `git add -A` or `git add .` in that situation; it will sweep in noise and could produce a confusing/huge diff. Stage only the exact new/changed paths.

## Library maintenance

- `library_inventory.csv` and `data/library.json` must always be kept in sync — both get updated together whenever an entry is added, fixed, or removed (~448 entries as of mid-2026).
- Recent fixes: broken source URLs corrected by re-uploading from Calibre to R2; "Unknown" author fields fixed by reading each book's `metadata.opf`; template updated so R2-hosted `.pdf`/`.epub` entries show a "Download PDF" button instead of "View at source".
- Calibre `metadata.opf` files (readable as plain XML/text) contain useful descriptions for synthesis; the epub/PDF body content itself can't be read directly by a text tool.

## Known gotchas

- On Windows, `str_replace`-style partial edits are unreliable — prefer a full-file rewrite (`Write`/`filesystem:write_file`) even for small changes.
- Windows paths inside Python source need `"C:\\Users\\Abdulla"` (double backslash) or raw strings; avoid ever putting a literal Windows path inside a triple-quoted docstring — `\U` inside it is parsed as a Unicode escape and raises `SyntaxError`.
- If the filesystem MCP (in Claude Desktop) becomes unresponsive mid-session, restart the MCP server in Claude Desktop settings.
- A plain Linux `bash` tool cannot see Windows drive paths directly — only useful for Linux-side work, or (in Cowork) for a folder that's been explicitly mounted, which then appears under a `/sessions/.../mnt/<name>` bash path distinct from its real Windows path.
- R2 uploads via boto3 require `Config(signature_version="s3v4")`; the correct **write**-access key starts `b1f53194...` — the `7bf93194...` key is read-only and uploads will silently fail/403 with it.

## Translation & image resources available (as of July 2026)

- Abdulla holds **Google** and **Azure** credentials that can be used for machine translation (e.g. Google Cloud Translation API / Azure Translator) if a bilingual pair needs fast draft translation. In practice, essay-quality Arabic translations for `content/ideas/` and `content/development/` have so far been done as full manual/editorial translations (matching the site's literary MSA register), not raw MT output — treat MT as a first-draft aid to speed up long pieces, not a substitute for an edited pass, since Kandaka's Arabic voice is deliberately literary rather than mechanical.
- For cover art / illustrations beyond the hand-coded inline SVG banners used on `content/ideas/` posts, Abdulla has accounts on **ideogram.ai** and **app.leonardo.ai** (AI image generation) that can be used to produce a raster illustration instead of, or alongside, an SVG banner, if a post calls for something more photographic/illustrative than the flat vector style currently in use.

## Approach Abdulla prefers

- Python scripts for bulk upload/update operations rather than manual one-off file editing.
- Standard git workflow, run by Abdulla himself: `git add → git commit → git pull --rebase → git push` (rebase specifically when a push is rejected due to remote changes).

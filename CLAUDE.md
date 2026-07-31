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

## Banner images — now migrating from SVG to Leonardo.ai illustrations (July 2026)

- Started swapping the hand-coded inline SVG banners on `content/ideas/` essays for real illustrations generated in Leonardo.ai (`app.leonardo.ai`, logged in as Abdulla), one per essay, saved to `static/images/uploads/<slug>.jpg` and referenced with a plain `<img src="/images/uploads/<slug>.jpg" alt="..." style="width:100%;border-radius:10px;margin-bottom:1.5rem;" />` tag in place of the `<svg>...</svg>` block, in both the `.en.md` and `.ar.md` file (same image, alt text translated).
- Workflow: type prompt into the Leonardo prompt box → Image Dimensions → 16:9 (1344×768, the widest preset; still narrower than the old SVG's 800:220 but closest available and reads fine as a banner) → Generate → hover the result → click the download icon → the file lands in the user's real `Downloads` folder (not the sandbox) → mount/copy it from there into `static/images/uploads/`.
- A small helper script at `/tmp/replace_svg.py` (regex `<svg.*?</svg>` → `<img ...>`, DOTALL) does the swap in both language files in one call each — much faster than manually finding/reading each SVG block. Recreate it if it's not present in a fresh session:
  ```python
  import re, sys
  def replace(path, img_src, alt_text):
      content = open(path, encoding='utf-8').read()
      pattern = re.compile(r'<svg.*?</svg>', re.DOTALL)
      new_tag = f'<img src="{img_src}" alt="{alt_text}" style="width:100%;border-radius:10px;margin-bottom:1.5rem;" />'
      open(path, 'w', encoding='utf-8').write(pattern.sub(new_tag, content, count=1))
  replace(sys.argv[1], sys.argv[2], sys.argv[3])
  ```
- **Leonardo UI quirk:** after a generation or a download click, the feed scrolls and the prompt textarea's on-screen position shifts (it also grows taller for longer prompts, pushing the Generate button down). A blind click at a remembered coordinate will land on the image feed instead of the textbox, and a stray `ctrl+a` there selects/overtypes the whole page rather than just clearing the prompt. Safest sequence every time: click the "Back to top" link (or re-navigate the same URL) → screenshot to confirm the textarea is on-screen and get its real coordinates → click directly inside it → `ctrl+a` → type the new prompt → screenshot again to confirm the Generate button's current position before clicking it (don't assume it's still at the same y-coordinate as last time).
- Development essays (`content/development/`) deliberately have **no** banner image at all (they're report/book summaries, not illustrated essays) — don't add one unless Abdulla asks.

## Correct Sudanese attire in generated imagery — important, learned the hard way

A first pass at this defaulted every figure to "white jalabiya and turban," which reads as generic/Gulf Muslim dress, not specifically Sudanese, and Abdulla corrected it with reference photos. Rules for any future image generation (Leonardo, Ideogram, or otherwise) depicting Sudanese people:

- **Women:** the **thobe** (toub) — a single large length of fabric (often colourful, patterned, tie-dye, or sheer pastel, not just plain white) wrapped from over the head down around the body, worn *over* ordinary clothes underneath. It is draped, not fitted like a hijab. Contemporary/modern scenes should mix it with visible modern touches — structured designer handbags, gold jewelry, henna, a bit of styled hair showing at the front, heels — per the reference photos Abdulla shared of young Sudanese women in thobes. Don't render it as a tight hijab wrap.
- **Men:** a plain jalabiya (jallabiya) is the everyday default, and by default it has **no head covering** — bare-headed, short hair, is completely normal and common. Where a head covering is wanted, reach first for a simple white crocheted **taqiyah** skullcap, not a wound turban. The wound turban (**imma**) is a real garment but reads as elder/rural/ceremonial specifically — don't use it as the generic "Sudanese man" default; it was the single biggest miss in the first batch of images.
- **Don't force traditional dress everywhere.** Sudan has just as strong a history and present of Western-style clothing — shirts, trousers, ties, ordinary dresses — especially in urban, historical (1960s–70s student/professional photos), and modern/youth contexts. "Modern Sudanese editorial illustration" should default to a mix of modern and traditional as fits the scene, the way Abdulla's reference images show, not costume every figure in traditional wear by default.
- If in doubt on a specific look, ask Abdulla for reference photos (he has more) or a relevant website before generating — he offered this proactively and it's faster than several rounds of correction after the fact.
- **The model has a strong default bias toward turbans on men in desert/riverbed/manual-labour scenes specifically**, even when the prompt explicitly says "no turban" or "bare-headed." A softer instruction ("no head covering") is often ignored on the first try. What worked: be extremely blunt and specific — "short cropped black hair, nothing at all on his head" — and check the actual result (zoom into the figure) before accepting; be ready to regenerate once or twice for this specific issue even with a good prompt.
- **Don't default every figure to male.** A first pass at the batch defaulted almost every scene to a lone man (farmer, miner, gum-arabic tapper), and Abdulla flagged it directly: Sudan is "the land of Kandaka" (the site's own namesake is a Nubian queen) — women should appear across the set as farmers, traders, miners, professionals, etc., not only in domestic/classroom scenes, mixed in as fits each essay's actual subject rather than token placement.
- **Sudanese ≠ generic sub-Saharan African.** When told to add women, a second pass rendered them as generic pan-African stock imagery (plain wax-print-style dress + simple headwrap, generic West/East African facial styling) — Abdulla corrected this too: Sudanese are **African Arab**, a distinct Nile Valley identity with its own look, not interchangeable with generic "African woman" imagery. Fixes for every prompt going forward: (1) always name the garment explicitly as a "thobe" or "toub" — a single large length of fabric draped from over the head down around the whole body over the woman's regular clothes underneath, not a separate dress-plus-headwrap combo, and not a fitted hijab; (2) describe faces/features as Sudanese Nile Valley Arab-African, not generic African; (3) still vary skin tone and features realistically (Sudan itself spans a wide range, north to south), but the clothing silhouette and drape specifically must read as the toub, not a generic print dress. When in doubt, ask Abdulla for another reference photo rather than guessing.
- **Meroe pyramids ≠ Giza pyramids — the model defaults hard to Giza and to a lighter, "Cleopatra-style" Egyptian queen face whenever a prompt mentions "pyramids" or "ancient queen," even when the prompt explicitly says Sudan/Nubia/Kush and even when it says "NOT Giza."** Saying "not Giza"/"not Egyptian" is not enough — it still visually primes Giza. What worked on `kandaka-nubian-queens`: drop any mention of Egypt/Giza entirely and instead describe the Meroe pyramids purely by their physical proportions — small (no taller than a three-story building), narrower than they are tall, sides at a very steep ~65–70° angle (near-obelisk-like, not Giza's broad low-angle silhouette), rough eroded/weathered stepped sandstone blocks with missing capstones, a small flat-roofed twin-towered stone gate chapel attached to the front of each one, dozens clustered tightly together in rows on red desert sand. For the queen's face/regalia, also drop "Egyptian"/generic "ancient queen" phrasing and instead say very dark brown-black skin, Nubian African facial features (wide nose, full lips) explicitly, plus real Kushite/Meroitic regalia by name — Abdulla shared reference images of an actual Kandake funerary mask and a Meroitic gold ornament showing a **feathered vulture-wing headdress** (not a smooth pharaonic nemes/khat headcloth) and a **wide multi-row beaded-and-gold collar necklace** covering the chest — use those specific terms, not generic "Egyptian queen jewelry." Always zoom into the result afterward to check both the pyramid silhouette and the face/headdress before accepting — the first attempt with "not Giza" wording still produced Giza pyramids and a Cleopatra-style face.

## Approach Abdulla prefers

- Python scripts for bulk upload/update operations rather than manual one-off file editing.
- Standard git workflow, run by Abdulla himself: `git add → git commit → git pull --rebase → git push` (rebase specifically when a push is rejected due to remote changes).

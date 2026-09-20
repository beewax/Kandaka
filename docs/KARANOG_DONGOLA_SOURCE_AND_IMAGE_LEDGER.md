# Karanog and Dongola’s Throne Hall — reviewed source and image ledger

**Status:** Published in English and Arabic on 19 September 2026 following explicit user approval; both live pages verified.  
**Research and integration date:** 19 September 2026.

The academic research pass checked 108 claims, proposed 19 corrections, recorded 27 sources and audited all nine image references. The English and Arabic drafts incorporate those corrections. The original research package is preserved separately; its statement that Arabic and image files were unavailable describes that research task’s inputs. Those files were subsequently recovered from the existing Kandaka working copy and reviewed for this merge.

## Research record

See [the complete research package](research/karanog-dongola/README.md), [research report](research/karanog-dongola/research-report.md), [claim table](research/karanog-dongola/claim-verification.md), [source ledger](research/karanog-dongola/source-ledger.md) and [image audit](research/karanog-dongola/image-audit.md). The source ledger distinguishes printed pages from PDF viewer pages and records inspection limits. The article’s linked footnotes are the publication-facing citations.

The 1910 excavators’ racial classifications and Blemmyan identification remain historical interpretations, not established facts. Modern chronology, the G187 association, the proposed royal use of the Dongola building, reconstructed roof details and painting identifications retain the qualifications documented in the report. The 1317 inscription is distinguished from later architectural alterations; 1364 is attributed to Godlewski’s reconstruction, and 1969 is the published endpoint of mosque use.

The [earlier planning ledger](research/karanog-dongola/pre-research-ledger.md) is retained as provenance for asset creation and initial research. Its older citations and image-generation prompts do not override the corrected article or this ledger.

## Recovered storage and working files

- Repository: `beewax/Kandaka`.
- English: `content/history/karanog-dongola-throne-hall.en.md`.
- Arabic: `content/history/karanog-dongola-throne-hall.ar.md`.
- Image files: `static/images/uploads/`.
- Kandaka’s R2 source library: `kandaka-library`, public base `https://pub-0c3bb637d5f54b239fe4a4ef9b08bfe3.r2.dev`.

R2 was inspected read-only and contains the source PDFs, including the Woolley cemetery volume and Dongola guide. The article drafts and their images are in the repository working copy. No R2 objects or library catalogue entries were changed by this merge.

## Current image decisions

See [the recovered-asset verification](research/karanog-dongola/asset-verification.md) for file comparisons and the visual review. The original image files are preserved.

| ID | Asset | Publication treatment |
| --- | --- | --- |
| I01 | `karanog-dongola-cover-original.png` | Active cover, explicitly described as an OpenAI-generated conceptual montage made for Kandaka in 2026. Its imagined architecture and ceremony are not archaeological reconstruction evidence. |
| I02 | `karanog-cemetery-plan-1908.png` | Active; 1910 plate 116, NYU-hosted scan, exact plate link and corrected caption. |
| I03 | `karanog-tomb-superstructures-1910.png` | Active; plate 112, foundations of G70/G71/G165 and cross-ribs of G259. |
| I04 | `karanog-ba-statue-1910.png` | Active; plate 1 is a historical reconstruction of the figure attributed to G187, not a securely identified king recovered intact in that tomb. Caption notes conjectural attributes. |
| I05 | `karanog-painted-pottery-1910.png` | Active; plate 43 includes a hunter and collared hound, not the draft’s former cattle/herder reading. |
| I06 | `karanog-meroitic-graffiti-1910.png` | Active; plate 107 contains Greek, Demotic and Meroitic marks in several techniques. |
| I07 | `dongola-throne-hall-present.jpg` | Active; LeGabrie, 18 March 2017, exact Commons page and CC BY-SA 4.0 links; source photo retained without Kandaka edits. |
| I08 | `dongola-throne-hall-reconstruction-original.png` | Withheld from the published article. Its central-hall apse and definite dome conflict with the corrected distinction between observed fabric and reconstructed features. File retained for reference. |
| I09 | `dongola-throne-hall-1821.jpg` | Active with separate credits for Cailliaud’s 1821 view (published 1826) and LeGabrie’s 2020 DeepAI colourisation. Colours are explicitly modern; Commons’ public-domain designation is attributed to Commons. |

The five archival plate captions identify the original publication and digital source. They do not invent a modern Creative Commons licence or an individual plate artist. Historical copyright and any later additions remain separate questions, as recorded in the research image audit. The original ledger’s “commissioned” wording has been replaced by the documented fact that the two conceptual images were generated with OpenAI.

## Bilingual and publication state

The language-specific titles, author labels, category and tags are retained. The paired slugs, date, image paths, numbered source notes and factual qualifications are aligned. Both files are set to `draft: false` following explicit approval for this article. The unsupported seven-century minimum and all claims that make the original royal function certain are removed from both languages.

The inaccurate cutaway would require a new evidence-based drawing before reactivation. The user explicitly authorized publication of this specific article on 19 September 2026. The release includes the eight active images and excludes the inaccurate cutaway from the published static files. Deployment verification is recorded in the workplan.

## Publication verification

The [English article](https://kandaka.com/history/karanog-dongola-throne-hall/) and [Arabic article](https://kandaka.com/ar/history/karanog-dongola-throne-hall/) were published through [PR #9](https://github.com/beewax/Kandaka/pull/9), merge commit `9034b13190f1845eb5c68fae6737be64bc01a8c4`. Netlify production deploy `6aaefcabf5ba680008332bc6` became ready at 21:21 UTC on 19 September 2026.

Live HTTP checks at 21:21 UTC confirmed both article routes and History listings, English LTR and Arabic RTL, 21 rendered footnotes in each language, reciprocal language links, canonical and social-sharing metadata, and all eight article images returning HTTP 200 with image content types. The inaccurate cutaway has no reference in either published page and was excluded from the release commit.

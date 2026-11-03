# Kandaka Library — direct-download audit (3 November 2026)

**Scope:** Read-only classification of all 563 entries in `data/library.json`. This is a metadata audit, **not** a verification of live PDF responses, copyright status, or R2 objects. Do not mark files downloaded until independently fetched and checked.

## Inventory
- Total catalogue records: **563**.
- Entries with a `download` field: **132**. Of these, **44** have a Kandaka/R2-style download URL and **88** point to other hosts (some may be institutional PDF endpoints). These are catalogue claims, not validated objects.
- Entries without `download` whose `source` URL looks like a direct PDF: **90**. These should be checked for rights and stable access before mirroring.
- Remaining source-linked entries: **341**.
- Entries with explicit `rights_note` or `license` metadata: **123**; absence of notes is not evidence of permission.
- Source-linked records whose rights notes explicitly mention a Creative Commons or public-domain license but have no `download`: **12**, including a CC BY-NC-ND book that requires special care.

## First acquisition queue (verify publisher PDF, license, figure exceptions, metadata, then upload and test)
1. **Pedagogy Under Fire: Teaching Archaeology with WhatsApp during Sudan’s Civil War** — Cambridge publisher DOI 10.1017/pub.2026.10190; catalogue says CC BY 4.0. Confirm official PDF download and whether any third-party figures are excluded.
2. **Pluriversal Pasts: Decolonising Archaeological Practice in Sudan through the Integration of Folklore and Community Epistemologies** — DOI 10.1017/S0959774326100742; catalogue says CC BY 4.0; full-text review still partial.
3. **Towards a sustainable urban regeneration: the case of the historical island of Suakin in Sudan** — Frontiers DOI 10.3389/fbuil.2026.1868485; catalogue says CC BY, figure exceptions need inspection.
4. **Large-scale flood susceptibility mapping along major tributaries of the Nile River system in Sudan using convolutional neural network** — Scientific Reports DOI 10.1038/s41598-026-58194-7; catalogue says CC BY 4.0.
5. **Market-segmented target product profiles for realigning sorghum breeding, seed systems, and value chains in Eastern Sudan** — Frontiers DOI 10.3389/fsufs.2026.1846994; catalogue says CC BY.
6. **Effective Approach to Assessing and Mitigating Urban Heat Islands for Sustainable Regional Planning: Case Studies from Omdurman, Sudan** — IntechOpen; catalogue says CC BY 4.0, PDF retrieval unresolved.
7. **A New Two-Step Approach to Studying Early Medieval Lustre Ceramics from Sudan** — MDPI; catalogue says CC BY 4.0.
8. **Crafting power in Kush: faience production and state control in the Napatan region** — Antiquity; catalogue says CC BY 4.0.

## Workflow / blocker
Prefer `kandaka-library` R2 storage, not Nile Book Store. An object must be retrieved from the destination and checked for valid PDF signature, content, SHA256, title/author/pages and public accessibility before adding `download` to the Library record. Keep publisher/DOI in `source`, rights and attribution in `rights_note`. For records lacking verified redistribution permission, use the original source link and do not rehost.

**This pass did not upload any PDFs.** The available repository connector can update text metadata; a verified source-PDF-to-R2 binary transfer and retrieval path still needs execution. No catalogue download links were changed, to avoid broken buttons or false claims.

## Next implementation
Start with the eight items above, verify official PDF bytes and license conditions individually, then upload eligible objects to Kandaka R2 and confirm publicly reachable download URLs before editing `data/library.json`. Independently audit the existing 44 R2-style download URLs for live status and content-type. Audit 90 direct external PDFs for reuse rights. Do not silently relabel external downloads as locally hosted.

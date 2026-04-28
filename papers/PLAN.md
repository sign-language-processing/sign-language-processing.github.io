# Papers Network — Plan

**Goal: capture every sign-language paper.** If a paper is SL-related,
save it — even when SS metadata is thin. Missing PDF / abstract /
bibtex is a cue for the agent to go look (web, publisher, ACL, ar5iv),
not a reason to drop a node.

Obsidian-style vault under `papers/`, one md file per paper. Built
iteratively: small scripts + Claude-in-the-loop.

## Seeds

1. Every entry in `src/references.bib` (~301), resolved to an SS
   paperId via DOI / arXiv / title search.
2. Every 2014 SL paper from SS `paper/search/bulk` across queries
   (`sign language`, `signed language`, `fingerspelling`, …).

## Traversal

BFS over `/references` and `/citations`. Expand a node only if it's SL
or in our bib. Cap citations at ~1000/node by `citationCount` (refs
are paper-bounded). Cache JSON, visited set, frontier on disk —
resumable.

## API

Semantic Scholar — <https://api.semanticscholar.org/api-docs/>.
**100 req / 5 min.** `POST /paper/batch` (500 IDs/call) does the heavy
lifting. Log every call, back off on 429.

## Per-paper file: `papers/<ssid>.md`

```yaml
---
semanticScholarId, bibKey, year, title, doi, arxivId
isSignLanguage, expanded, topics
fullText: extracted | abstract-only | none
fullTextSource: ar5iv | semanticscholar | pdf | web | none
bibtexSource: ours | semanticscholar | synthesized
---
```

Body sections: `# Title` · `**Year:** [[YYYY]]` · `**Topics:** [[topics/<slug>]] …` ·
Authors · Links (SS / PDF / arXiv / DOI — drop missing) · Abstract ·
TL;DR · BibTeX · Full Text · References · Cited by.

## Rules

- **Wikilink only when target exists.** Otherwise list under "not in
  vault" so the picture isn't lossy.
- **Tags are wikilinks.** `[[YYYY]]` per year, `[[topics/<slug>]]` per
  topic from `s2FieldsOfStudy ∪ fieldsOfStudy`. Generate one-line
  stubs for every year/topic that appears.
- **BibTeX.** Ours when present and well-formed; else SS
  `citationStyles.bibtex`; else synthesize from metadata. Always have
  one — record source.
- **SL classifier.** Title/abstract matches sign keywords (`sign
  language`, `signed language`, `fingerspell*`, `signer`,
  `SignWriting`, `gloss(es|ing)?`, plus dataset names: PHOENIX,
  How2Sign, WLASL, MS-ASL, BSL-1K, BOBSL, OpenASL, YouTube-ASL, …) or
  appears in an SL venue (SLTAT, sign-lang@LREC, WMT-SLT, SLRTP).
  Cache per paperId.
- **Full text — first hit wins:**
  1. ar5iv HTML via docling, images stay on ar5iv.
  2. Semantic Scholar full text if exposed.
  3. PDF via docling, images linked to
     `figures.semanticscholar.org/<ssid>/<page>-Figure<n>-1.png`
     (HEAD-check + cache; 404 → captioned stub linking SS paper page).
  4. Agent web search (publisher / ACL / author page / ResearchGate)
     to find a URL feeding 1–3, or transcribe the abstract.
  5. Otherwise `abstract-only`.
- **Text only, no bitmaps.** Every image is an external link. Hard cap
  on file size (~80+ pages or >500 KB md → `abstract-only`).

## QA pass

Sub-agent reviews every `papers/<ssid>.md` and fixes what it can:
no abstract/full text → web search; no bibtex → synthesize or flag;
404 figure links → captioned stub; missing topics → re-derive or
infer; misclassified `isSignLanguage` → re-run classifier; dangling
`[[ssid]]` → demote to plain stub. Unfixables append to `REVIEW.md`.

## Open

- Free SS API key for higher limit?
- Attribution footer for SS abstracts/full text?

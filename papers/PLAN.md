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
2. Every SL paper from **2014 onward**, found via SS `paper/search/bulk`
   across queries (`sign language`, `signed language`, `fingerspelling`,
   …) with `year=2014-`.

## Traversal

BFS over `/references` and `/citations`. Expand a node only if it's SL
or in our bib. **No year filter on traversal** — the 2014+ cutoff is
only for the search-based seed; once the BFS is running, follow SL
citations of any vintage (1960s foundational work included). Cap
citations at ~1000/node by `citationCount` (refs are paper-bounded).
Cache JSON, visited set, frontier on disk — resumable.

## API

Semantic Scholar — <https://api.semanticscholar.org/api-docs/>.
**Use a free SS API key — limit stays at 100 req / 5 min.**
`POST /paper/batch` (500 IDs/call) does the heavy lifting. Log every
call, back off on 429.

## Per-paper file: `papers/<ssid>.md`

```yaml
---
semanticScholarId: <sha>
bibKey: <bibkey-or-null>
year: <int>
title: <string>
doi: <string-or-null>
arxivId: <string-or-null>
isSignLanguage: <bool>
expanded: <bool>
topics: [<topic>, ...]
fullText: extracted | abstract-only | none
fullTextSource: ar5iv | semanticscholar | pdf | web | none
bibtexSource: ours | semanticscholar | synthesized
sources:                           # per-field provenance
  title: semanticscholar
  abstract: semanticscholar
  authors: semanticscholar
  topics: semanticscholar
  references: semanticscholar
  citations: semanticscholar
  fullText: <same as fullTextSource>
  bibtex: <same as bibtexSource>
---
```

Body sections: `# Title` · `**Year:** [[YYYY]]` · `**Topics:** [[topics/<slug>]] …` ·
Authors · Links (SS / PDF / arXiv / DOI — drop missing) · Abstract ·
TL;DR · BibTeX · Full Text · References · Cited by · **Sources**.

The `## Sources` footer restates `frontmatter.sources` in human-readable
form so each fact in the file is traceable to its origin (SS API,
ar5iv, our bib, agent web search, etc.).

## Rules

- **Always wikilink.** Every reference/citation is `[[ssid]]`, even
  when no file exists for that id yet. Unresolved links are fine —
  we filter them in a later pass.
- **Tags are wikilinks.** `[[YYYY]]` per year, `[[topics/<slug>]]` per
  topic from `s2FieldsOfStudy ∪ fieldsOfStudy`. Generate one-line
  stubs for every year/topic that appears.
- **BibTeX.** Ours when present and well-formed; else SS
  `citationStyles.bibtex`; else synthesize from metadata. Always have
  one — record `bibtexSource` and `sources.bibtex`.
- **Attribute everything.** Every field originates from one source
  (SS API, ar5iv, our bib, agent web search, synthesized). Record it
  in `frontmatter.sources` and surface it in the `## Sources` footer.
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
  at **1 MB** of text per file (or 80+ page PDFs) → fall back to
  `abstract-only`.

## QA pass

Sub-agent reviews every `papers/<ssid>.md` and fixes what it can:
no abstract/full text → web search; no bibtex → synthesize or flag;
missing `sources` entries → fill in or flag; 404 figure links →
captioned stub; missing topics → re-derive or infer; misclassified
`isSignLanguage` → re-run classifier. Unfixables append to `REVIEW.md`.

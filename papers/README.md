# Sign-language papers vault

An Obsidian-style vault that tries to capture every sign-language
processing paper as a single markdown node, with references and
citations resolved to internal `[[ssid]]` wikilinks. See
[`PLAN.md`](PLAN.md) for the design.

The actual md files and the API-fetched cache are **not in git** —
they're shipped as release tarballs (`graph.tar.gz` + `state.tar.gz`).
Only the scripts, the plan, and this README live in-tree.

## What's in this directory

```
papers/
├── README.md            ← you are here
├── PLAN.md              ← design / data-model / rules
├── scripts/             ← build pipeline (committed)
├── graph/               ← rendered .md vault (gitignored, distributed via tarball)
└── state/               ← API cache + crawl checkpoints (gitignored, distributed via tarball)
```

`scripts/` is the source of truth — given a fresh `state/`, running
the pipeline regenerates `graph/` deterministically.

## Download the vault

Releases live on the GitHub Releases page for this repo:

> https://github.com/sign-language-processing/sign-language-processing.github.io/releases

Two artifacts per release:

| File | Contents | Approx size |
|---|---|---|
| `graph.tar.gz` | rendered md vault (`papers/graph/<ssid>.md`) | ~60 MB |
| `state.tar.gz` | API cache + checkpoints (lets you resume the crawl) | ~200 MB |

You only need `graph.tar.gz` to read the vault. You need `state.tar.gz`
*as well* if you want to extend the crawl further.

## Unpacking

From the repo root:

```bash
# Read-only: just the rendered vault
curl -L -o /tmp/graph.tar.gz https://github.com/sign-language-processing/sign-language-processing.github.io/releases/latest/download/graph.tar.gz
tar -xzf /tmp/graph.tar.gz -C papers/    # writes papers/graph/

# Plus the cache (only if you want to continue the crawl)
curl -L -o /tmp/state.tar.gz https://github.com/sign-language-processing/sign-language-processing.github.io/releases/latest/download/state.tar.gz
tar -xzf /tmp/state.tar.gz -C papers/    # writes papers/state/
```

After unpacking, `papers/graph/` is the Obsidian vault — point
Obsidian at it (or any markdown viewer that supports `[[wikilinks]]`).

## Using the vault in Obsidian

1. Open Obsidian → "Open folder as vault" → select `papers/graph/`.
2. Each `<ssid>.md` is one paper. Frontmatter holds title / year / doi
   / arxivId / topics / `isSignLanguage` / `expanded` /
   `fullTextSource` / `bibtexSource`.
3. References and citations are rendered as `[[ssid]]` wikilinks.
   Many will be unresolved (no node) — those are papers we know
   exist but haven't fetched. Filter or hide unresolved links in
   Obsidian settings if they bother you.
4. `[[YYYY]]` per-year tags and `[[topics/<slug>]]` per-topic tags
   give you free backlink-based indexes without dedicated stub files.

## Continuing the crawl

Requires Python 3.10+, `requests`, and (for full text) `docling`.

```bash
pip install requests docling
# Optional: free Semantic Scholar API key, raises throttle headroom.
export SEMANTIC_SCHOLAR_API_KEY=<your key>

# Resume the BFS where it left off. Reads state/, writes state/.
python3 papers/scripts/crawl.py

# Bulk full-text extraction — auto-loops, picks up new SL papers
# discovered by the crawler.
python3 papers/scripts/run_fulltext_all.py     # ar5iv / openAccessPdf
python3 papers/scripts/fulltext_acl.py         # ACL Anthology PDFs

# Re-render after new data arrives.
python3 papers/scripts/render.py               # writes papers/graph/<ssid>.md
```

The crawler is fault-tolerant: kill it any time, restart it, it picks
up from `state/visited.json` + the on-disk `meta/` and `edges/`
directories. State writes are atomic (`.tmp` + rename).

## Re-running the SL judge

The strict SL classifier (`scripts/classify.py`) uses a regex
pre-filter. Borderline cases get sent through a strict subagent
("judge") that writes to `state/judge_cache.json`. After the crawler
discovers new papers, prep the judge candidate list:

```bash
PYTHONPATH=papers/scripts python3 -c "
import json
from pathlib import Path
from classify import is_sign_language
state = Path('papers/state')
seed = json.load(open(state/'seed_bib.json'))
bib_pids = {v for v in seed.values() if v}
judged = set(json.load(open(state/'judge_cache.json')).keys())
out = []
for p in sorted((state/'meta').glob('*.json')):
    pid = p.stem
    if pid in judged: continue
    m = json.loads(p.read_text())
    if is_sign_language(m) or pid in bib_pids:
        out.append({'paperId': pid, 'title': m.get('title') or '',
                    'abstract': (m.get('abstract') or '')[:500],
                    'venue': m.get('venue') or '', 'inBib': pid in bib_pids})
(state/'papers_to_judge.json').write_text(json.dumps(out, indent=2, ensure_ascii=False))
print(f'wrote {len(out)} candidates')
"
```

Then dispatch a Claude subagent with the prompt described in
`PLAN.md` over `papers_to_judge.json` to update `judge_cache.json`.

## Building a new release artifact

After a fresh crawl + render:

```bash
tar -czf graph.tar.gz -C papers graph
tar -czf state.tar.gz -C papers state
gh release create vYYYY-MM-DD graph.tar.gz state.tar.gz \
    --title "Vault snapshot YYYY-MM-DD" \
    --notes "<short description of what's new>"
```

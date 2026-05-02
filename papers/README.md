# Sign-language papers vault

An Obsidian-style vault that captures every sign-language processing
paper as a single markdown node, with references and citations
resolved to internal `[[ssid]]` wikilinks. See
[`PLAN.md`](PLAN.md) for the design.

The repo ships **only the source-of-truth state** as a Git-LFS-tracked
`state.tar.gz`. Users build their own `papers/graph/` (the rendered
markdown vault) by unpacking the tarball and running the renderer.
This means the repo stays small, the vault is always built from the
latest scripts, and contributors who extend the crawl push back a
fresh `state.tar.gz` on top of the existing one.

## What's in the repo

```
papers/
├── README.md            ← you are here
├── PLAN.md              ← design / data-model / rules
├── scripts/             ← build pipeline (committed)
├── state.tar.gz         ← LFS-tracked snapshot of the API cache
├── graph/               ← rendered .md vault (gitignored — built locally)
└── state/               ← unpacked cache (gitignored — built locally)
```

`state.tar.gz` contains the `meta/` (raw Semantic Scholar metadata),
`edges/` (refs + citations per expanded paper), `fulltext/` (extracted
paper bodies), `judge_cache.json` (subagent SL classifications),
`api_log.jsonl`, and crawl checkpoints (`visited.json`, `frontier.json`).

## Quick start

You need Git LFS, Python 3.10+, and the `requests` + `docling` packages
(only docling for re-running full-text extraction).

```bash
# Clone (LFS pulls state.tar.gz automatically if you have git-lfs).
git clone https://github.com/sign-language-processing/sign-language-processing.github.io
cd sign-language-processing.github.io

# If LFS didn't auto-pull:
git lfs pull

# Unpack the cache (~404 MB compressed, ~1.6 GB unpacked).
tar -xzf papers/state.tar.gz -C papers/      # creates papers/state/

# Build the vault (deterministic — pure transform of state/).
pip install requests docling
python3 papers/scripts/render.py             # writes papers/graph/<ssid>.md

# Open papers/graph/ in Obsidian: "Open folder as vault".
```

## Using the vault in Obsidian

- Each `<ssid>.md` is one paper. Frontmatter holds title / year / doi /
  arxivId / topics / `isSignLanguage` / `expanded` / `fullTextSource` /
  `bibtexSource`.
- References and citations are rendered as `[[ssid]]` wikilinks. Many
  will be unresolved (no node) — those are papers we know exist but
  haven't fetched. Hide unresolved links in Obsidian if they bother you.
- `[[YYYY]]` per-year tags and `[[topics/<slug>]]` per-topic tags give
  you free backlink-based indexes without dedicated stub files.

## Continuing the crawl

The crawl is fault-tolerant: kill any script anytime, restart, it picks
up from `state/visited.json` + the on-disk `meta/` and `edges/`
directories. State writes are atomic (`.tmp` + rename).

```bash
# Optional: free Semantic Scholar API key, raises throttle headroom.
export SEMANTIC_SCHOLAR_API_KEY=<your key>

# Resume the BFS where it left off (drains `frontier.json` until empty).
python3 papers/scripts/crawl.py

# Bulk full-text extraction — auto-loops, picks up new SL papers as
# the crawler discovers them. Run them all in parallel; they share
# the same state/fulltext/ output and don't conflict.
python3 papers/scripts/run_fulltext_all.py    # ar5iv + openAccessPdf
python3 papers/scripts/fulltext_acl.py        # ACL Anthology PDFs
python3 papers/scripts/fulltext_ss_alt.py     # SS internal-API alt links
python3 papers/scripts/fulltext_scihub.py     # Sci-Hub fallback (DOI)
UNPAYWALL_EMAIL=you@example.com python3 papers/scripts/fulltext_unpaywall.py

# Re-render after new data arrives.
python3 papers/scripts/render.py              # writes papers/graph/<ssid>.md
```

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

Then dispatch a Claude / Anthropic subagent with the prompt described
in `PLAN.md` over `papers_to_judge.json` to update `judge_cache.json`.

## Pushing back a refreshed snapshot

After running the crawl + fetchers + judge to your satisfaction:

```bash
tar -czf papers/state.tar.gz -C papers state
git add papers/state.tar.gz
git commit -m "papers/state: refresh snapshot YYYY-MM-DD"
git push
```

Git-LFS handles the upload (configured in `.gitattributes` to track
`papers/state.tar.gz`). Bandwidth/storage uses your account's LFS quota.

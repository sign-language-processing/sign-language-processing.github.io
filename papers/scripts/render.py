"""Render markdown files for every paper we have metadata for.

Reads:
  state/meta/<id>.json     — SS metadata (required)
  state/edges/<id>.json    — refs+citations (optional; missing → leaf)
  state/seed_bib.json      — bibKey -> paperId
  state/bib.json           — full bib entries (for rawBibtex preference)

Writes:
  papers/graph/<id>.md     — one file per SL or ≥10-SL-neighbor paper
                             (papers/graph/ is gitignored — we ship a
                             tarball or LFS, not in-tree)

Idempotent — safe to rerun. Always wikilinks every reference/citation,
even when no node exists yet (we'll filter unresolved later).
"""

from __future__ import annotations

import json
import re
from collections import defaultdict
from pathlib import Path

from classify import is_sign_language
from fulltext import get_cached as get_cached_fulltext

ROOT = Path(__file__).resolve().parent.parent
STATE = ROOT / "state"
META_DIR = STATE / "meta"
EDGES_DIR = STATE / "edges"
PAPERS_DIR = ROOT / "graph"
TOPICS_DIR = ROOT / "topics"


def _slugify(s: str) -> str:
    s = s.lower()
    s = re.sub(r"[^a-z0-9]+", "-", s)
    return s.strip("-")


def _load_bib() -> tuple[dict[str, str | None], dict[str, dict]]:
    bib_map = json.loads((STATE / "seed_bib.json").read_text()) if (STATE / "seed_bib.json").exists() else {}
    bib_entries = (
        {e["bibKey"]: e for e in json.loads((STATE / "bib.json").read_text())}
        if (STATE / "bib.json").exists()
        else {}
    )
    paperid_to_bibkey: dict[str, str] = {pid: k for k, pid in bib_map.items() if pid}
    return paperid_to_bibkey, bib_entries


def _bibtex_for(meta: dict, bibkey: str | None, bib_entries: dict[str, dict]) -> tuple[str, str]:
    """Returns (bibtex_text, source) where source ∈ {ours, semanticscholar, synthesized}."""
    if bibkey and bibkey in bib_entries:
        raw = bib_entries[bibkey].get("rawBibtex")
        if raw:
            return raw, "ours"
    cs = (meta.get("citationStyles") or {}).get("bibtex")
    if cs:
        return cs, "semanticscholar"
    # Synthesize a minimal one.
    pid = meta.get("paperId", "unknown")
    title = meta.get("title", "Untitled").replace("{", "").replace("}", "")
    year = meta.get("year") or "n.d."
    authors = meta.get("authors") or []
    author_str = " and ".join(a.get("name", "") for a in authors)
    venue = meta.get("venue") or ""
    raw = (
        f"@misc{{ss:{pid},\n"
        f"  title  = {{{title}}},\n"
        f"  author = {{{author_str}}},\n"
        f"  year   = {{{year}}},\n"
        + (f"  venue  = {{{venue}}},\n" if venue else "")
        + "}\n"
    )
    return raw, "synthesized"


def _topics(meta: dict) -> list[str]:
    out = []
    seen = set()
    for t in meta.get("fieldsOfStudy") or []:
        if t and t.lower() not in seen:
            out.append(t)
            seen.add(t.lower())
    for f in meta.get("s2FieldsOfStudy") or []:
        cat = (f or {}).get("category")
        if cat and cat.lower() not in seen:
            out.append(cat)
            seen.add(cat.lower())
    return out


def _yaml_value(v):
    if v is None:
        return "null"
    if isinstance(v, bool):
        return "true" if v else "false"
    if isinstance(v, (int, float)):
        return str(v)
    if isinstance(v, list):
        if not v:
            return "[]"
        return "[" + ", ".join(_yaml_inline(x) for x in v) + "]"
    s = str(v).replace("\\", "\\\\").replace('"', '\\"')
    return f'"{s}"'


def _yaml_inline(v):
    if isinstance(v, str):
        s = v.replace("\\", "\\\\").replace('"', '\\"')
        return f'"{s}"'
    return _yaml_value(v)


def _build_links(meta: dict) -> list[str]:
    pid = meta["paperId"]
    out = [f"- [Semantic Scholar](https://www.semanticscholar.org/paper/{pid})"]
    pdf = (meta.get("openAccessPdf") or {}).get("url")
    if pdf:
        out.append(f"- [PDF]({pdf})")
    ext = meta.get("externalIds") or {}
    if ext.get("ArXiv"):
        out.append(f"- [arXiv:{ext['ArXiv']}](https://arxiv.org/abs/{ext['ArXiv']})")
    if ext.get("DOI"):
        out.append(f"- [DOI](https://doi.org/{ext['DOI']})")
    if ext.get("ACL"):
        out.append(f"- [ACL Anthology](https://aclanthology.org/{ext['ACL']})")
    return out


def render_paper(meta: dict, paperid_to_bibkey: dict[str, str], bib_entries: dict[str, dict], judge: dict[str, bool] | None = None) -> str:
    pid = meta["paperId"]
    bibkey = paperid_to_bibkey.get(pid)
    title = meta.get("title") or "Untitled"
    year = meta.get("year")
    topics = _topics(meta)
    judge = judge or {}
    is_sl = _is_sl(meta, judge, pid in paperid_to_bibkey)
    edges_path = EDGES_DIR / f"{pid}.json"
    expanded = edges_path.exists()
    bibtex, btx_src = _bibtex_for(meta, bibkey, bib_entries)
    abstract = meta.get("abstract") or ""
    tldr = (meta.get("tldr") or {}).get("text") or ""
    ext = meta.get("externalIds") or {}

    cached_ft = get_cached_fulltext(pid)
    if cached_ft and cached_ft[1].strip():
        ft_source, ft_body = cached_ft
        ft_status = "extracted"
    else:
        ft_source, ft_body, ft_status = "none", "", "none"

    fm = {
        "semanticScholarId": pid,
        "bibKey": bibkey,
        "year": year,
        "title": title,
        "doi": ext.get("DOI"),
        "arxivId": ext.get("ArXiv"),
        "isSignLanguage": is_sl,
        "expanded": expanded,
        "topics": topics,
        "fullText": ft_status,
        "fullTextSource": ft_source,
        "bibtexSource": btx_src,
    }
    sources = {
        "title": "semanticscholar",
        "abstract": "semanticscholar" if abstract else "none",
        "authors": "semanticscholar",
        "topics": "semanticscholar" if topics else "none",
        "references": "semanticscholar" if expanded else "none",
        "citations": "semanticscholar" if expanded else "none",
        "fullText": ft_source,
        "bibtex": btx_src,
    }

    fm_lines = ["---"]
    for k, v in fm.items():
        fm_lines.append(f"{k}: {_yaml_value(v)}")
    fm_lines.append("sources:")
    for k, v in sources.items():
        fm_lines.append(f"  {k}: {v}")
    fm_lines.append("---")
    fm_block = "\n".join(fm_lines)

    parts = [fm_block, "", f"# {title}", ""]
    if year:
        parts.append(f"**Year:** [[{year}]]")
    if topics:
        topic_links = ", ".join(f"[[topics/{_slugify(t)}|{t}]]" for t in topics)
        parts.append(f"**Topics:** {topic_links}")
    authors = meta.get("authors") or []
    if authors:
        parts.append("**Authors:** " + "; ".join(a.get("name", "") for a in authors))
    parts.append("")

    parts.append("## Links")
    parts.extend(_build_links(meta))
    parts.append("")

    if abstract:
        parts.append("## Abstract")
        parts.append("")
        parts.append(abstract)
        parts.append("")
    if tldr:
        parts.append("## TL;DR")
        parts.append("")
        parts.append(tldr)
        parts.append("")

    parts.append("## BibTeX")
    parts.append("")
    parts.append("```bibtex")
    parts.append(bibtex.strip())
    parts.append("```")
    parts.append("")

    if ft_body:
        parts.append("## Full Text")
        parts.append("")
        parts.append(ft_body.rstrip())
        parts.append("")

    if expanded:
        edges = json.loads(edges_path.read_text())
        if edges.get("references"):
            parts.append("## References")
            parts.append("")
            for r in edges["references"]:
                rid = r.get("paperId")
                rtitle = r.get("title") or ""
                ryear = r.get("year") or ""
                if rid:
                    parts.append(f"- [[{rid}]] — {rtitle} ({ryear})")
                else:
                    parts.append(f"- {rtitle} ({ryear})")
            parts.append("")
        if edges.get("citations"):
            parts.append("## Cited by")
            parts.append("")
            for c in edges["citations"]:
                cid = c.get("paperId")
                ctitle = c.get("title") or ""
                cyear = c.get("year") or ""
                if cid:
                    parts.append(f"- [[{cid}]] — {ctitle} ({cyear})")
                else:
                    parts.append(f"- {ctitle} ({cyear})")
            parts.append("")

    parts.append("## Sources")
    parts.append("")
    for k, v in sources.items():
        parts.append(f"- {k}: {v}")
    parts.append("")
    return "\n".join(parts)


def _judge_cache() -> dict[str, bool]:
    p = STATE / "judge_cache.json"
    return json.loads(p.read_text()) if p.exists() else {}


def _is_sl(meta: dict, judge: dict[str, bool], in_bib: bool) -> bool:
    """Judge cache wins, then bib membership, then regex classifier."""
    pid = meta["paperId"]
    if pid in judge:
        return judge[pid]
    if in_bib:
        return True
    return is_sign_language(meta)


def _sl_neighbor_counts(judge: dict[str, bool], paperid_to_bibkey: dict) -> dict[str, int]:
    """For every paperId mentioned in any expanded SL paper's edges,
    count how many distinct SL expanded papers reference/cite it. Lets
    us keep foundational non-SL papers (e.g. pose-estimation) when the
    SL community heavily cites them."""
    counts: dict[str, int] = {}
    if not EDGES_DIR.exists():
        return counts
    for ep in sorted(EDGES_DIR.glob("*.json")):
        owner_pid = ep.stem
        meta_path = META_DIR / f"{owner_pid}.json"
        if not meta_path.exists():
            continue
        owner_meta = json.loads(meta_path.read_text())
        if not _is_sl(owner_meta, judge, owner_pid in paperid_to_bibkey):
            continue
        edges = json.loads(ep.read_text())
        seen_here: set[str] = set()
        for n in edges.get("references", []) + edges.get("citations", []):
            nid = n.get("paperId")
            if nid and nid not in seen_here:
                counts[nid] = counts.get(nid, 0) + 1
                seen_here.add(nid)
    return counts


def main() -> None:
    PAPERS_DIR.mkdir(parents=True, exist_ok=True)
    paperid_to_bibkey, bib_entries = _load_bib()
    judge = _judge_cache()
    bib_pid_set = {pid for pid in paperid_to_bibkey}
    metas = sorted(META_DIR.glob("*.json"))
    print(f"Considering {len(metas)} cached papers (judge_cache: {len(judge)} entries)")

    sl_neighbor_count = _sl_neighbor_counts(judge, paperid_to_bibkey)
    print(f"Computed SL-neighbor counts for {len(sl_neighbor_count)} paperIds")

    years: set[int] = set()
    topics_seen: dict[str, str] = {}
    written = 0
    written_via_sl = 0
    written_via_neighbors = 0
    skipped = 0
    removed = 0
    for path in metas:
        meta = json.loads(path.read_text())
        pid = meta["paperId"]
        is_sl = _is_sl(meta, judge, pid in bib_pid_set)
        nbr = sl_neighbor_count.get(pid, 0)
        keep = is_sl or nbr >= 10
        target = PAPERS_DIR / f"{pid}.md"
        if not keep:
            if target.exists():
                target.unlink()
                removed += 1
            skipped += 1
            continue
        out = render_paper(meta, paperid_to_bibkey, bib_entries, judge)
        target.write_text(out)
        written += 1
        if is_sl:
            written_via_sl += 1
        else:
            written_via_neighbors += 1
        if meta.get("year"):
            years.add(int(meta["year"]))
        for t in _topics(meta):
            topics_seen[_slugify(t)] = t
    print(
        f"Wrote {written} ({written_via_sl} SL + {written_via_neighbors} "
        f"non-SL with >=10 SL neighbors); {len(years)} years, "
        f"{len(topics_seen)} topics linked; skipped {skipped}; "
        f"removed {removed} stale md"
    )


if __name__ == "__main__":
    main()

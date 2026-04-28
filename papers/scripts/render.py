"""Render markdown files for every paper we have metadata for.

Reads:
  state/meta/<id>.json     — SS metadata (required)
  state/edges/<id>.json    — refs+citations (optional; missing → leaf)
  state/seed_bib.json      — bibKey -> paperId
  state/bib.json           — full bib entries (for rawBibtex preference)

Writes:
  papers/<id>.md
  papers/<YYYY>.md         — year stub
  papers/topics/<slug>.md  — topic stub

Idempotent — safe to rerun. Always wikilinks every reference/citation,
even when no node exists yet (we'll filter unresolved later).
"""

from __future__ import annotations

import json
import re
from collections import defaultdict
from pathlib import Path

from classify import is_sign_language

ROOT = Path(__file__).resolve().parent.parent
STATE = ROOT / "state"
META_DIR = STATE / "meta"
EDGES_DIR = STATE / "edges"
PAPERS_DIR = ROOT
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


def render_paper(meta: dict, paperid_to_bibkey: dict[str, str], bib_entries: dict[str, dict]) -> str:
    pid = meta["paperId"]
    bibkey = paperid_to_bibkey.get(pid)
    title = meta.get("title") or "Untitled"
    year = meta.get("year")
    topics = _topics(meta)
    is_sl = is_sign_language(meta) or pid in {v for v in paperid_to_bibkey.keys()}
    edges_path = EDGES_DIR / f"{pid}.json"
    expanded = edges_path.exists()
    bibtex, btx_src = _bibtex_for(meta, bibkey, bib_entries)
    abstract = meta.get("abstract") or ""
    tldr = (meta.get("tldr") or {}).get("text") or ""
    ext = meta.get("externalIds") or {}

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
        "fullText": "none",
        "fullTextSource": "none",
        "bibtexSource": btx_src,
    }
    sources = {
        "title": "semanticscholar",
        "abstract": "semanticscholar" if abstract else "none",
        "authors": "semanticscholar",
        "topics": "semanticscholar" if topics else "none",
        "references": "semanticscholar" if expanded else "none",
        "citations": "semanticscholar" if expanded else "none",
        "fullText": "none",
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


def main() -> None:
    paperid_to_bibkey, bib_entries = _load_bib()
    metas = sorted(META_DIR.glob("*.json"))
    print(f"Rendering {len(metas)} papers")
    years: set[int] = set()
    topics_seen: dict[str, str] = {}
    for path in metas:
        meta = json.loads(path.read_text())
        out = render_paper(meta, paperid_to_bibkey, bib_entries)
        (PAPERS_DIR / f"{meta['paperId']}.md").write_text(out)
        if meta.get("year"):
            years.add(int(meta["year"]))
        for t in _topics(meta):
            topics_seen[_slugify(t)] = t
    # Year stubs only — topics live as bare wikilinks (no stub files).
    for y in sorted(years):
        (PAPERS_DIR / f"{y}.md").write_text(f"# {y}\n")
    print(f"Wrote {len(metas)} papers, {len(years)} year stubs, {len(topics_seen)} unique topics linked")


if __name__ == "__main__":
    main()

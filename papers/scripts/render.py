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

import bisect
import html
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


def _normalize_for_match(s: str) -> str:
    s = html.unescape(s).lower()
    s = re.sub(r"[^a-z0-9]+", " ", s)
    return re.sub(r"\s+", " ", s).strip()


_INLINE_CITE_RE = re.compile(r"\[([^\]\n]+)\]\(#(?:B|bib\.bib|R|CR)(\d+)\)")


def _resolve_inline_citations(
    ft_body: str,
    ss_refs: list[dict] | None,
    global_index: dict[tuple[str, int], set[str]] | None = None,
    global_titles: dict[str, str] | None = None,
) -> str:
    """Rewrite numeric anchor citations (`[text](#B<n>)`, `[text](#bib.bib<n>)`,
    `[text](#R<n>)`, `[text](#CR<n>)`) to `[[paperId|text]]` by mapping each
    `<n>` to the Nth paragraph in the source's `## References` section.
    Resolution order per paragraph: (1) SS reference title substring match;
    (2) global (first-author-surname, year) lookup parsed from the paragraph."""
    if not ft_body or not ss_refs or not _INLINE_CITE_RE.search(ft_body):
        return ft_body

    refs_match = re.search(r"(?im)^#{1,6}\s+references\s*$", ft_body)
    if not refs_match:
        return ft_body
    after_refs = ft_body[refs_match.end():]
    next_heading = re.search(r"(?m)^#{1,6}\s+\S", after_refs)
    refs_block = after_refs[:next_heading.start()] if next_heading else after_refs
    # Split on blank lines OR on list-item starts (bullet `- `, `* `, or
    # numbered `1.` / `[1]`) so that bullet-style ref lists yield one
    # paragraph per reference.
    paragraphs = [
        p.strip()
        for p in re.split(
            r"\n\s*\n|\n(?=\s*(?:[-*]\s+|\d+\.\s+|\[\d+\]\s*))",
            refs_block,
        )
        if p.strip()
    ]
    if not paragraphs:
        return ft_body

    ss_index: list[tuple[str, str]] = []
    for r in ss_refs:
        pid = r.get("paperId")
        norm = _normalize_for_match(r.get("title") or "")
        if pid and len(norm) >= 15:
            ss_index.append((norm, pid))
    ss_index.sort(key=lambda x: -len(x[0]))

    bmap: dict[int, str] = {}
    used: set[str] = set()
    for i, para in enumerate(paragraphs, start=1):
        norm_para = _normalize_for_match(para)
        for norm_title, pid in ss_index:
            if pid in used:
                continue
            if norm_title in norm_para:
                bmap[i] = pid
                used.add(pid)
                break
        if i in bmap or not global_index or not global_titles:
            continue
        head = _PARA_HEAD_RE.match(para)
        if not head:
            continue
        key = (head.group("surname").lower(), int(head.group("year")))
        ids = (global_index.get(key) or set()) - used
        pid = _disambiguate(ids, norm_para, global_titles) if ids else None
        if pid:
            bmap[i] = pid
            used.add(pid)
    if not bmap:
        return ft_body

    def repl(m: re.Match) -> str:
        pid = bmap.get(int(m.group(2)))
        return f"[[{pid}|{m.group(1)}]]" if pid else m.group(0)

    return _INLINE_CITE_RE.sub(repl, ft_body)


_PREFIXES = frozenset({
    "van", "von", "de", "del", "della", "di", "da", "du", "la", "le", "el",
    "mc", "mac", "der", "den",
})


def _surname_keys(name: str) -> list[str]:
    """Return candidate surname forms: last token, plus last-2 or last-3
    when the preceding tokens are known surname prefixes (Van Assche,
    van der Berg, de la Cruz)."""
    parts = re.split(r"\s+", html.unescape(name or "").strip())
    parts = [p.strip(",.()") for p in parts if p.strip(",.()")]
    if not parts:
        return []
    out = [parts[-1]]
    if len(parts) >= 2 and parts[-2].lower() in _PREFIXES:
        out.append(" ".join(parts[-2:]))
        if len(parts) >= 3 and parts[-3].lower() in _PREFIXES:
            out.append(" ".join(parts[-3:]))
    return out


def _build_key_index(items: list[dict]) -> dict[tuple[str, int], set[str]]:
    """Build (surname_lc, year) -> set of paperIds from a list of items
    each having paperId, year, authors."""
    idx: dict[tuple[str, int], set[str]] = {}
    for r in items:
        pid = r.get("paperId")
        try:
            year_i = int(r.get("year"))
        except (TypeError, ValueError):
            continue
        authors = r.get("authors") or []
        if not pid or not authors:
            continue
        name = (authors[0] or {}).get("name") or ""
        for k in _surname_keys(name):
            idx.setdefault((k.lower(), year_i), set()).add(pid)
    return idx


def _build_global_key_index() -> tuple[dict[tuple[str, int], set[str]], dict[str, str]]:
    """One-shot index over every cached metadata file. Returns
    `(key_index, titles)` where `titles[paperId]` is the normalized title
    used to disambiguate ambiguous (surname, year) hits."""
    items: list[dict] = []
    titles: dict[str, str] = {}
    for p in META_DIR.glob("*.json"):
        m = json.loads(p.read_text())
        items.append(m)
        pid = m.get("paperId")
        if pid:
            titles[pid] = _normalize_for_match(m.get("title") or "")
    return _build_key_index(items), titles


def _disambiguate(
    candidates: set[str],
    paragraph_norm: str,
    titles: dict[str, str],
) -> str | None:
    """When global-index lookup returns multiple paperIds, pick the one whose
    normalized title (>=15 chars) appears as a substring of the (already
    normalized) paragraph. Returns None if 0 or >1 candidates qualify."""
    matches = [
        pid for pid in candidates
        if (titles.get(pid) or "") and len(titles[pid]) >= 15
        and titles[pid] in paragraph_norm
    ]
    return matches[0] if len(matches) == 1 else None


_SURNAME_PAT = (
    r"(?:(?:Van|Von|De|Del|Della|Di|Da|Du|La|Le|Mc|Mac|"
    r"van|von|de|del|della|di|da|du|la|le)\s+)?"
    r"[A-Z][A-Za-zÀ-ÿ\-'’]+"
)
_YEAR_PAT = r"(?:19|20)\d{2}"
_MOD_PAT = (
    r"(?:\s+et\s+al\.?"
    r"|\s*(?:&|&amp;|and)\s+(?:" + _SURNAME_PAT + r"))"
)

# Inside-parens citation token: surname + optional mod + comma + year.
_INNER_CITE_RE = re.compile(
    r"(?P<surname>" + _SURNAME_PAT + r")"
    r"(?:" + _MOD_PAT + r")?"
    r"\s*,\s*(?P<year>" + _YEAR_PAT + r")[a-z]?"
)

# Outside-parens citation: must be either "<surname><mod>(,year|(year))" or
# narrative "<surname> (year)" — bare "Surname, 2020" without a modifier is
# too ambiguous (would match every sentence with a year) so we don't.
_OUTSIDE_RE = re.compile(
    r"(?P<sa>" + _SURNAME_PAT + r")"
    + _MOD_PAT
    + r"\s*(?:,\s*(?P<yac>" + _YEAR_PAT + r")[a-z]?"
    + r"|\(\s*(?P<yap>" + _YEAR_PAT + r")[a-z]?\s*\))"
    + r"|"
    + r"(?P<sb>" + _SURNAME_PAT + r")\s*\(\s*(?P<ybp>" + _YEAR_PAT + r")[a-z]?\s*\)"
)

_PAREN_BLOCK_RE = re.compile(r"\(([^()\n]{1,400})\)")
_SKIP_REGIONS_RE = re.compile(r"\[\[[^\]\n]+\]\]|\[[^\]\n]*\]\([^)\n]*\)")

# Pull (first-author-surname, year) from the head of a reference paragraph
# (handles "- Albanie et al. [2021] …", "Pedraza, M., & Collante, L. (2021)",
# "Smith J., Jones A. (2020)…", etc.).
_PARA_HEAD_RE = re.compile(
    r"^\s*(?:[-*]\s+)?(?:\d+\.\s+|\[\d+\]\s*)?"
    r"(?P<surname>" + _SURNAME_PAT + r")"
    r"[^\n]{0,400}?"
    r"[\[(,\s](?P<year>" + _YEAR_PAT + r")[a-z]?[\])]?"
)


def _safe_sub(text: str, pattern: re.Pattern, repl_fn) -> str:
    """Apply `pattern.sub(repl_fn)` but skip matches that fall inside an
    existing `[[...]]` wikilink or `[text](url)` markdown link."""
    skip = [(m.start(), m.end()) for m in _SKIP_REGIONS_RE.finditer(text)]
    if not skip:
        return pattern.sub(repl_fn, text)
    starts = [s for s, _ in skip]

    def safe_repl(m: re.Match) -> str:
        i = bisect.bisect_right(starts, m.start()) - 1
        if i >= 0 and skip[i][0] <= m.start() < skip[i][1]:
            return m.group(0)
        return repl_fn(m)

    return pattern.sub(safe_repl, text)


def _resolve_text_citations(
    body: str,
    ss_refs: list[dict] | None,
    global_index: dict[tuple[str, int], set[str]],
    global_titles: dict[str, str] | None = None,
) -> str:
    """Wrap plain-text citations like `(Pedraza & Collante, 2021)` and
    `Papatsimouli et al., 2023` as `[[paperId|<original text>]]`. Resolves
    via per-paper SS refs first, then a global corpus-wide index — only
    rewriting when the lookup is unambiguous."""
    if not body:
        return body

    per_paper = _build_key_index(ss_refs or [])

    refs_match = re.search(r"(?im)^#{1,6}\s+references\s*$", body)
    end = refs_match.start() if refs_match else len(body)
    main_text = body[:end]
    rest = body[end:]

    def lookup(surname: str, year: int) -> str | None:
        key = (surname.lower(), year)
        ids = per_paper.get(key) or set()
        if len(ids) == 1:
            return next(iter(ids))
        if len(ids) > 1:
            return None
        ids = global_index.get(key) or set()
        if len(ids) == 1:
            return next(iter(ids))
        return None

    def wrap(m: re.Match, surname: str, year: int) -> str:
        pid = lookup(surname, year)
        return f"[[{pid}|{m.group(0)}]]" if pid else m.group(0)

    def paren_block(m: re.Match) -> str:
        inner = m.group(1)
        if not re.search(_YEAR_PAT, inner):
            return m.group(0)

        def inner_cite(im: re.Match) -> str:
            return wrap(im, im.group("surname"), int(im.group("year")))

        return "(" + _safe_sub(inner, _INNER_CITE_RE, inner_cite) + ")"

    main_text = _safe_sub(main_text, _PAREN_BLOCK_RE, paren_block)

    def outside_cite(m: re.Match) -> str:
        surname = m.group("sa") or m.group("sb")
        year = m.group("yac") or m.group("yap") or m.group("ybp")
        if not surname or not year:
            return m.group(0)
        return wrap(m, surname, int(year))

    main_text = _safe_sub(main_text, _OUTSIDE_RE, outside_cite)

    return main_text + rest


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


def render_paper(
    meta: dict,
    paperid_to_bibkey: dict[str, str],
    bib_entries: dict[str, dict],
    judge: dict[str, bool] | None = None,
    global_key_index: dict[tuple[str, int], set[str]] | None = None,
    global_titles: dict[str, str] | None = None,
) -> str:
    pid = meta["paperId"]
    bibkey = paperid_to_bibkey.get(pid)
    title = meta.get("title") or "Untitled"
    year = meta.get("year")
    topics = _topics(meta)
    judge = judge or {}
    is_sl = _is_sl(meta, judge, pid in paperid_to_bibkey)
    edges_path = EDGES_DIR / f"{pid}.json"
    expanded = edges_path.exists()
    edges = json.loads(edges_path.read_text()) if expanded else {}
    bibtex, btx_src = _bibtex_for(meta, bibkey, bib_entries)
    abstract = meta.get("abstract") or ""
    tldr = (meta.get("tldr") or {}).get("text") or ""
    ext = meta.get("externalIds") or {}

    cached_ft = get_cached_fulltext(pid)
    if cached_ft and cached_ft[1].strip():
        ft_source, ft_body = cached_ft
        ft_body = _resolve_inline_citations(ft_body, edges.get("references"), global_key_index, global_titles)
        ft_body = _resolve_text_citations(ft_body, edges.get("references"), global_key_index or {}, global_titles or {})
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
    out = "\n".join(parts)
    while True:
        unescaped = html.unescape(out)
        if unescaped == out:
            return out
        out = unescaped


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

    global_key_index, global_titles = _build_global_key_index()
    print(f"Built global (surname, year) index: {len(global_key_index)} keys, {len(global_titles)} titles")

    sl_neighbor_count = _sl_neighbor_counts(judge, paperid_to_bibkey)
    print(f"Computed SL-neighbor counts for {len(sl_neighbor_count)} paperIds")

    # Foundational-paper threshold scales with the SL community size:
    # a paper survives if it's referenced by >= 0.1% of SL papers.
    sl_total = sum(1 for path in metas
                   if _is_sl(json.loads(path.read_text()), judge,
                             path.stem in bib_pid_set))
    threshold = max(2, sl_total // 1000)
    print(f"SL total: {sl_total}; foundational-paper threshold: >= {threshold}")

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
        keep = is_sl or nbr >= threshold
        target = PAPERS_DIR / f"{pid}.md"
        if not keep:
            if target.exists():
                target.unlink()
                removed += 1
            skipped += 1
            continue
        out = render_paper(meta, paperid_to_bibkey, bib_entries, judge, global_key_index, global_titles)
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
        f"non-SL with >={threshold} SL neighbors); {len(years)} years, "
        f"{len(topics_seen)} topics linked; skipped {skipped}; "
        f"removed {removed} stale md"
    )


if __name__ == "__main__":
    main()

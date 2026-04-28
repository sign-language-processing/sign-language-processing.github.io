"""Parse src/references.bib into state/bib.json.

Hand parser — the file has clean indentation and no nested braces in
field values that would trip a simple split. Output is a list of dicts:
    {bibKey, type, title, year, doi, arxivId, aclId, url, rawBibtex,
     authors (raw), venue, fields (full dict of unparsed fields)}
"""

from __future__ import annotations

import json
import re
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent.parent
BIB_PATH = REPO / "src" / "references.bib"
OUT_PATH = REPO / "papers" / "state" / "bib.json"

ENTRY_RE = re.compile(r"^@(\w+)\{([^,]+),\s*$")
FIELD_RE = re.compile(r"^\s*([\w-]+)\s*=\s*(.*)$")
ARXIV_RE = re.compile(
    r"arxiv\.org/(?:abs|pdf)/([0-9]{4}\.[0-9]{4,5}|[a-z\-]+/[0-9]{7})",
    re.IGNORECASE,
)
ACL_RE = re.compile(r"aclanthology\.org/([A-Z0-9.\-]+)", re.IGNORECASE)


def _strip_braces(s: str) -> str:
    s = s.strip()
    if s.endswith(","):
        s = s[:-1].rstrip()
    if s.startswith("{") and s.endswith("}"):
        s = s[1:-1]
    elif s.startswith('"') and s.endswith('"'):
        s = s[1:-1]
    return s


def _clean_value(s: str) -> str:
    # collapse internal whitespace; remove latex braces around words
    s = re.sub(r"\s+", " ", s).strip()
    s = re.sub(r"\{([^{}]*)\}", r"\1", s)
    return s


def parse_bib(text: str) -> list[dict]:
    entries = []
    lines = text.splitlines()
    i = 0
    while i < len(lines):
        m = ENTRY_RE.match(lines[i])
        if not m:
            i += 1
            continue
        entry_type, bib_key = m.group(1), m.group(2).strip()
        raw_lines = [lines[i]]
        i += 1
        fields_raw: dict[str, str] = {}
        # Collect until line is exactly "}"
        current_key: str | None = None
        current_val: list[str] = []
        while i < len(lines) and lines[i].strip() != "}":
            raw_lines.append(lines[i])
            fm = FIELD_RE.match(lines[i])
            if fm:
                # commit the previous field
                if current_key is not None:
                    fields_raw[current_key] = " ".join(current_val).strip()
                current_key = fm.group(1).lower()
                current_val = [fm.group(2)]
            else:
                current_val.append(lines[i])
            i += 1
        if current_key is not None:
            fields_raw[current_key] = " ".join(current_val).strip()
        if i < len(lines):
            raw_lines.append(lines[i])  # the closing }
            i += 1

        cleaned = {k: _clean_value(_strip_braces(v)) for k, v in fields_raw.items()}
        url = cleaned.get("url", "")
        arxiv_match = ARXIV_RE.search(url) or ARXIV_RE.search(cleaned.get("eprint", ""))
        acl_match = ACL_RE.search(url)
        entry = {
            "bibKey": bib_key,
            "type": entry_type,
            "title": cleaned.get("title"),
            "year": int(cleaned["year"]) if cleaned.get("year", "").isdigit() else None,
            "doi": cleaned.get("doi"),
            "arxivId": arxiv_match.group(1) if arxiv_match else None,
            "aclId": acl_match.group(1) if acl_match else None,
            "url": url or None,
            "authors": cleaned.get("author"),
            "venue": cleaned.get("booktitle") or cleaned.get("journal"),
            "rawBibtex": "\n".join(raw_lines),
        }
        entries.append(entry)
    return entries


def main() -> None:
    text = BIB_PATH.read_text(encoding="utf-8")
    entries = parse_bib(text)
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(json.dumps(entries, indent=2, ensure_ascii=False))
    # Quick stats.
    by_year: dict[int, int] = {}
    with_doi = sum(1 for e in entries if e["doi"])
    with_arxiv = sum(1 for e in entries if e["arxivId"])
    with_acl = sum(1 for e in entries if e["aclId"])
    no_id = sum(1 for e in entries if not (e["doi"] or e["arxivId"] or e["aclId"]))
    for e in entries:
        if e["year"]:
            by_year[e["year"]] = by_year.get(e["year"], 0) + 1
    print(f"Parsed {len(entries)} entries")
    print(f"  with DOI:    {with_doi}")
    print(f"  with arXiv:  {with_arxiv}")
    print(f"  with ACL:    {with_acl}")
    print(f"  no external id: {no_id}")
    print(f"  years: {min(by_year)}–{max(by_year)}, top: ", end="")
    print(", ".join(f"{y}:{n}" for y, n in sorted(by_year.items(), key=lambda kv: -kv[1])[:5]))
    print(f"Wrote {OUT_PATH}")


if __name__ == "__main__":
    main()

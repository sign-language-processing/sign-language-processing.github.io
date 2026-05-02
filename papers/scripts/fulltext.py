"""Extract paper full text following the PLAN.md ladder.

Priority:
  1. arXiv → ar5iv HTML via docling.
  2. (TODO) Semantic Scholar full text.
  3. PDF → docling.
  4. (TODO) Agent web search.
  5. abstract-only.

Cache result to state/fulltext/<paperId>.md. Cap at 1 MB. Idempotent —
skip when the cached file already exists.
"""

from __future__ import annotations

import json
import os
import re
import sys
from pathlib import Path
from typing import Tuple

import requests

ROOT = Path(__file__).resolve().parent.parent
STATE = ROOT / "state"
META_DIR = STATE / "meta"
FULLTEXT_DIR = STATE / "fulltext"

MAX_CHARS = 1_000_000  # 1 MB cap (PLAN.md)

# Browser-like headers — many publishers (T&F, MDPI, OUP, IndJST, ACM)
# refuse direct PDF downloads from non-browser User-Agents.
BROWSER_HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    ),
    "Accept": "application/pdf,text/html;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
}

_session = None


def _get_session() -> requests.Session:
    global _session
    if _session is None:
        _session = requests.Session()
        _session.headers.update(BROWSER_HEADERS)
    return _session


def _download_pdf(url: str, dest: Path) -> bool:
    """Download PDF with browser headers + strict timeout. Returns True on success."""
    try:
        with _get_session().get(
            url, timeout=(10, 60), stream=True, allow_redirects=True
        ) as r:
            if r.status_code != 200:
                return False
            ct = r.headers.get("Content-Type", "").lower()
            if "pdf" not in ct and not url.lower().endswith(".pdf"):
                return False
            written = 0
            with open(dest, "wb") as f:
                for chunk in r.iter_content(chunk_size=65536):
                    if not chunk:
                        continue
                    f.write(chunk)
                    written += len(chunk)
                    if written > 50_000_000:
                        return False
        return True
    except Exception:
        return False


def _load_meta(paper_id: str) -> dict | None:
    p = META_DIR / f"{paper_id}.json"
    if not p.exists():
        return None
    return json.loads(p.read_text())


def _strip_ar5iv_chrome(md: str) -> str:
    """Drop the ar5iv navigation footer and HTML stub bullets."""
    # Cut at "ar5iv homepage" or "View original on arXiv" footer line.
    cut_patterns = [
        r"\n\[?◄\]?\(/html/.*",
        r"\nar5iv homepage.*",
        r"\n\[Feeling lucky\?\].*",
        r"\n\[View original on arXiv\].*",
    ]
    for pat in cut_patterns:
        m = re.search(pat, md)
        if m:
            md = md[: m.start()]
    # Strip leading/trailing whitespace.
    return md.strip() + "\n"


_converter = None


def _get_converter():
    global _converter
    if _converter is None:
        from docling.document_converter import DocumentConverter
        _converter = DocumentConverter()
    return _converter


def from_ar5iv(arxiv_id: str) -> str | None:
    url = f"https://ar5iv.labs.arxiv.org/html/{arxiv_id}"
    try:
        result = _get_converter().convert(url)
    except Exception as e:
        print(f"  ar5iv {arxiv_id}: convert failed: {e}")
        return None
    md = result.document.export_to_markdown()
    return _strip_ar5iv_chrome(md)


def from_pdf(pdf_url: str) -> str | None:
    FULLTEXT_DIR.mkdir(parents=True, exist_ok=True)
    tmp_pdf = FULLTEXT_DIR / f"_dl_{os.getpid()}.pdf.tmp"
    if not _download_pdf(pdf_url, tmp_pdf):
        if tmp_pdf.exists():
            tmp_pdf.unlink()
        print(f"  pdf {pdf_url}: download failed (403/404/timeout/non-pdf)")
        return None
    try:
        result = _get_converter().convert(str(tmp_pdf))
    except Exception as e:
        print(f"  pdf {pdf_url}: docling failed: {e}")
        tmp_pdf.unlink(missing_ok=True)
        return None
    tmp_pdf.unlink(missing_ok=True)
    return result.document.export_to_markdown().strip() + "\n"


def extract(paper_id: str, *, force: bool = False) -> Tuple[str, str | None]:
    """Returns (source, text). source ∈ {ar5iv, pdf, none}."""
    out_path = FULLTEXT_DIR / f"{paper_id}.md"
    if out_path.exists() and not force:
        # Read source tag from first line if present (we prefix it).
        head = out_path.read_text().splitlines()[:1]
        if head and head[0].startswith("<!--source:"):
            return head[0].split(":", 1)[1].rstrip("-->").strip(), None
        return "ar5iv", None  # legacy default
    meta = _load_meta(paper_id)
    if not meta:
        return "none", None
    ext = meta.get("externalIds") or {}
    arxiv_id = ext.get("ArXiv")
    text = None
    src = "none"
    if arxiv_id:
        text = from_ar5iv(arxiv_id)
        if text:
            src = "ar5iv"
    if not text:
        pdf = (meta.get("openAccessPdf") or {}).get("url")
        if pdf:
            text = from_pdf(pdf)
            if text:
                src = "pdf"
    if not text:
        return "none", None
    if len(text) > MAX_CHARS:
        text = text[:MAX_CHARS] + "\n\n*[truncated to 1 MB]*\n"
    FULLTEXT_DIR.mkdir(parents=True, exist_ok=True)
    out_path.write_text(f"<!--source:{src}-->\n{text}")
    return src, text


def has_cached(paper_id: str) -> bool:
    return (FULLTEXT_DIR / f"{paper_id}.md").exists()


def get_cached(paper_id: str) -> tuple[str, str] | None:
    p = FULLTEXT_DIR / f"{paper_id}.md"
    if not p.exists():
        return None
    raw = p.read_text()
    src = "none"
    body = raw
    if raw.startswith("<!--source:"):
        first_nl = raw.find("\n")
        head = raw[:first_nl]
        body = raw[first_nl + 1 :]
        src = head[len("<!--source:") : -len("-->")].strip()
    return src, body


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: fulltext.py <paperId>...")
        sys.exit(2)
    for pid in sys.argv[1:]:
        src, text = extract(pid)
        if text is None and src != "none":
            print(f"{pid}: cached ({src})")
        elif text:
            print(f"{pid}: wrote {len(text)} chars from {src}")
        else:
            print(f"{pid}: no full text available")


if __name__ == "__main__":
    main()

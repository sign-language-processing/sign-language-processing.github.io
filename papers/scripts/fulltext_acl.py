"""ACL Anthology full-text extractor.

For modern ACL/EMNLP/NAACL papers, the PDF lives at
    https://aclanthology.org/<acl-id>.pdf

For older LREC papers (L04..L14), aclanthology.org redirects to the
HTML page at /<acl-id>/, and the PDF link points at the original
lrec-conf.org host. We scrape <meta name="citation_pdf_url"> from the
HTML page and follow.

Browser-like User-Agent throughout — some publishers block bare requests.
"""

from __future__ import annotations

import json
import os
import re
import sys
import time
from pathlib import Path

import requests

ROOT = Path(__file__).resolve().parent.parent
STATE = ROOT / "state"
META_DIR = STATE / "meta"
FULLTEXT_DIR = STATE / "fulltext"
JUDGE_PATH = STATE / "judge_cache.json"
SEED_PATH = STATE / "seed_bib.json"

MAX_CHARS = 1_000_000

BROWSER_HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    ),
    "Accept": "application/pdf,text/html;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
}

_META_RE = re.compile(r"<meta\b([^>]+)>", re.IGNORECASE)
_ATTR_RE = re.compile(r'(\w+)=(?:"([^"]*)"|\'([^\']*)\'|([^\s">]+))')


def _parse_meta_pdf_url(html: str) -> str | None:
    """Permissive parser: handles ACL's unquoted attributes + content-first ordering."""
    for m in _META_RE.finditer(html):
        attrs = {a[0].lower(): (a[1] or a[2] or a[3])
                 for a in _ATTR_RE.findall(m.group(1))}
        if attrs.get("name", "").lower() == "citation_pdf_url":
            return attrs.get("content")
    return None

_converter = None
_session = None


def _get_converter():
    global _converter
    if _converter is None:
        from docling.document_converter import DocumentConverter
        _converter = DocumentConverter()
    return _converter


def _get_session() -> requests.Session:
    global _session
    if _session is None:
        _session = requests.Session()
        _session.headers.update(BROWSER_HEADERS)
    return _session


def _is_sl(meta: dict, judge: dict, bib_pids: set) -> bool:
    pid = meta.get("paperId")
    if pid in judge:
        return judge[pid]
    if pid in bib_pids:
        return True
    sys.path.insert(0, str(ROOT / "scripts"))
    from classify import is_sign_language
    return is_sign_language(meta)


def _download_pdf(url: str, dest: Path) -> bool:
    try:
        with _get_session().get(url, timeout=(10, 60), stream=True, allow_redirects=True) as r:
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


def _resolve_pdf_url(acl_id: str) -> str | None:
    """Try direct .pdf URL first; on 404 fetch HTML page and parse citation_pdf_url."""
    direct = f"https://aclanthology.org/{acl_id}.pdf"
    try:
        r = _get_session().head(direct, timeout=15, allow_redirects=True)
    except Exception:
        r = None
    if r is not None and r.status_code == 200:
        return direct
    # Fall back: HTML page
    page_url = f"https://aclanthology.org/{acl_id}/"
    try:
        r = _get_session().get(page_url, timeout=15, allow_redirects=True)
    except Exception:
        return None
    if r.status_code != 200:
        return None
    pdf_url = _parse_meta_pdf_url(r.text)
    if not pdf_url:
        return None
    if pdf_url.startswith("//"):
        return "https:" + pdf_url
    if pdf_url.startswith("/"):
        return "https://aclanthology.org" + pdf_url
    return pdf_url


def candidates() -> list[tuple[str, str]]:
    judge = json.loads(JUDGE_PATH.read_text()) if JUDGE_PATH.exists() else {}
    bib_pids = set()
    if SEED_PATH.exists():
        bib_pids = {v for v in json.loads(SEED_PATH.read_text()).values() if v}
    out = []
    for p in sorted(META_DIR.glob("*.json")):
        pid = p.stem
        if (FULLTEXT_DIR / f"{pid}.md").exists():
            continue
        try:
            meta = json.loads(p.read_text())
        except Exception:
            continue
        ext = meta.get("externalIds") or {}
        acl_id = ext.get("ACL")
        if not acl_id:
            continue
        if not _is_sl(meta, judge, bib_pids):
            continue
        out.append((pid, acl_id))
    return out


def extract_acl(paper_id: str, acl_id: str) -> str | None:
    pdf_url = _resolve_pdf_url(acl_id)
    if not pdf_url:
        print(f"  acl {acl_id}: no PDF URL discoverable")
        return None
    tmp_pdf = FULLTEXT_DIR / f"_dl_{paper_id}.pdf.tmp"
    if not _download_pdf(pdf_url, tmp_pdf):
        if tmp_pdf.exists():
            tmp_pdf.unlink()
        print(f"  acl {acl_id}: download failed: {pdf_url[:80]}")
        return None
    try:
        result = _get_converter().convert(str(tmp_pdf))
    except Exception as e:
        print(f"  acl {acl_id}: docling failed: {e}")
        tmp_pdf.unlink(missing_ok=True)
        return None
    tmp_pdf.unlink(missing_ok=True)
    return result.document.export_to_markdown().strip() + "\n"


def main(loop: bool = True, idle_sleep: int = 120) -> None:
    FULLTEXT_DIR.mkdir(parents=True, exist_ok=True)
    rd = 0
    while True:
        rd += 1
        todo = candidates()
        print(f"\n=== ACL round {rd}: {len(todo)} candidates ===")
        if not todo:
            if not loop:
                break
            time.sleep(idle_sleep)
            continue
        t0 = time.time()
        for i, (pid, acl_id) in enumerate(todo, 1):
            try:
                text = extract_acl(pid, acl_id)
            except Exception as e:
                print(f"[{i}/{len(todo)}] {pid}: ERROR {e}")
                continue
            if not text:
                print(f"[{i}/{len(todo)}] {pid}: no full text (acl)")
                continue
            if len(text) > MAX_CHARS:
                text = text[:MAX_CHARS] + "\n\n*[truncated to 1 MB]*\n"
            tmp = FULLTEXT_DIR / f"{pid}.md.tmp"
            tmp.write_text(f"<!--source:acl-->\n{text}")
            os.replace(tmp, FULLTEXT_DIR / f"{pid}.md")
            print(f"[{i}/{len(todo)}] {pid}: wrote {len(text)} chars from acl")
            time.sleep(0.3)
        print(f"round {rd} done in {time.time() - t0:.1f}s")
        if not loop:
            break


if __name__ == "__main__":
    loop = "--once" not in sys.argv
    main(loop=loop)

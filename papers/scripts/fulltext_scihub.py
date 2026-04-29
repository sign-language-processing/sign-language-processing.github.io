"""Last-resort full-text fetcher via Sci-Hub.

For SL papers that have a DOI and have already failed every legitimate
source (openAccessPdf, ar5iv, ACL, SS-internal-API, Unpaywall), try
Sci-Hub mirrors. The HTML response contains a `<meta name="citation_pdf_url">`
tag pointing at the PDF.

Tagged `<!--source:scihub-->` so the renderer / release tooling can
optionally exclude these files from public distribution. Sci-Hub
copyright status varies by jurisdiction; treat fulltexts collected via
this script as for personal/research use unless you've cleared
distribution rights.

Loop mode (default).
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
SCIHUB_CACHE = STATE / "scihub_cache.json"

MAX_CHARS = 1_000_000
MIN_INTERVAL = 10.0  # seconds between sci-hub calls — slow + polite

# Mirror list, tried in order.
MIRRORS = [
    "https://sci-hub.box",
    "https://sci-hub.ru",
    "https://sci-hub.se",
    "https://sci-hub.st",
]

PDF_META_RE = re.compile(
    r'<meta[^>]+name=["\']citation_pdf_url["\'][^>]+content=["\']([^"\']+)["\']',
    re.IGNORECASE,
)

_converter = None


def _get_converter():
    global _converter
    if _converter is None:
        from docling.document_converter import DocumentConverter
        _converter = DocumentConverter()
    return _converter


def _load_json(p: Path, default):
    if not p.exists():
        return default
    try:
        return json.loads(p.read_text())
    except Exception:
        return default


def _atomic_write_json(p: Path, data) -> None:
    tmp = p.with_suffix(p.suffix + ".tmp")
    tmp.write_text(json.dumps(data, indent=2, ensure_ascii=False))
    os.replace(tmp, p)


def _is_sl(meta: dict, judge: dict, bib_pids: set) -> bool:
    pid = meta.get("paperId")
    if pid in judge:
        return judge[pid]
    if pid in bib_pids:
        return True
    sys.path.insert(0, str(ROOT / "scripts"))
    from classify import is_sign_language
    return is_sign_language(meta)


_last_ts = [0.0]


def _wait():
    elapsed = time.monotonic() - _last_ts[0]
    if elapsed < MIN_INTERVAL:
        time.sleep(MIN_INTERVAL - elapsed)
    _last_ts[0] = time.monotonic()


def _download_pdf(url: str, session: requests.Session, dest: Path) -> bool:
    try:
        with session.get(url, timeout=(10, 60), stream=True, allow_redirects=True) as r:
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


def fetch_pdf_url(doi: str, session: requests.Session) -> str | None:
    """Try sci-hub mirrors. Returns absolute PDF URL or None."""
    for mirror in MIRRORS:
        _wait()
        url = f"{mirror}/{doi}"
        try:
            resp = session.get(url, timeout=20, allow_redirects=True)
        except requests.RequestException:
            continue
        if resp.status_code in (404, 410):
            continue  # this mirror doesn't have it
        if resp.status_code != 200:
            continue
        text = resp.text
        m = PDF_META_RE.search(text)
        if not m:
            continue
        pdf_path = m.group(1)
        if pdf_path.startswith("//"):
            return "https:" + pdf_path
        if pdf_path.startswith("/"):
            return mirror + pdf_path
        if pdf_path.startswith("http"):
            return pdf_path
        return f"{mirror}/{pdf_path}"
    return None


def _ss_alt_tried_and_failed() -> set[str]:
    """Papers SS-alt has examined and didn't produce a fulltext for.
    Sci-Hub only takes papers SS-alt has given up on."""
    p = STATE / "ss_alt_negatives.json"
    return set(_load_json(p, []))


def candidates(judge: dict, bib_pids: set, cache: dict) -> list[tuple[str, str]]:
    upstream_failed = _ss_alt_tried_and_failed()
    out = []
    for p in sorted(META_DIR.glob("*.json")):
        pid = p.stem
        if (FULLTEXT_DIR / f"{pid}.md").exists():
            continue
        if pid in cache:
            continue  # tried (success or permanent fail)
        if pid not in upstream_failed:
            continue  # wait for SS-alt to give up on it first
        try:
            meta = json.loads(p.read_text())
        except Exception:
            continue
        if not _is_sl(meta, judge, bib_pids):
            continue
        ext = meta.get("externalIds") or {}
        doi = ext.get("DOI")
        if not doi:
            continue
        out.append((pid, doi))
    return out


def main(loop: bool = True, idle_sleep: int = 600) -> None:
    FULLTEXT_DIR.mkdir(parents=True, exist_ok=True)
    cache: dict = _load_json(SCIHUB_CACHE, {})
    session = requests.Session()
    session.headers["User-Agent"] = "Mozilla/5.0 (papers-vault-builder)"
    rd = 0
    while True:
        rd += 1
        judge = _load_json(JUDGE_PATH, {})
        bib_pids = {v for v in _load_json(SEED_PATH, {}).values() if v}
        todo = candidates(judge, bib_pids, cache)
        print(f"\n=== scihub round {rd}: {len(todo)} candidates ===")
        if not todo:
            if not loop:
                break
            time.sleep(idle_sleep)
            continue
        t0 = time.time()
        wins = 0
        for i, (pid, doi) in enumerate(todo, 1):
            pdf_url = fetch_pdf_url(doi, session)
            if not pdf_url:
                cache[pid] = {"doi": doi, "_status": "no_pdf_link"}
                if i % 20 == 0:
                    _atomic_write_json(SCIHUB_CACHE, cache)
                continue
            tmp_pdf = FULLTEXT_DIR / f"{pid}.pdf.tmp"
            ok = _download_pdf(pdf_url, session, tmp_pdf)
            if not ok:
                tmp_pdf.unlink(missing_ok=True)
                cache[pid] = {"doi": doi, "pdf_url": pdf_url, "_status": "download_failed"}
                continue
            try:
                result = _get_converter().convert(str(tmp_pdf))
            except Exception as e:
                print(f"[{i}/{len(todo)}] {pid}: docling failed: {e}")
                cache[pid] = {"doi": doi, "pdf_url": pdf_url, "_status": "docling_failed"}
                tmp_pdf.unlink(missing_ok=True)
                continue
            tmp_pdf.unlink(missing_ok=True)
            text = result.document.export_to_markdown().strip() + "\n"
            if len(text) > MAX_CHARS:
                text = text[:MAX_CHARS] + "\n\n*[truncated to 1 MB]*\n"
            tmp = FULLTEXT_DIR / f"{pid}.md.tmp"
            tmp.write_text(f"<!--source:scihub-->\n{text}")
            os.replace(tmp, FULLTEXT_DIR / f"{pid}.md")
            wins += 1
            cache[pid] = {"doi": doi, "pdf_url": pdf_url, "_status": "ok"}
            print(f"[{i}/{len(todo)}] {pid}: wrote {len(text)} chars from scihub ({pdf_url[:60]})")
            if i % 20 == 0:
                _atomic_write_json(SCIHUB_CACHE, cache)
        _atomic_write_json(SCIHUB_CACHE, cache)
        print(f"round {rd}: {wins}/{len(todo)} new fulltexts in {time.time() - t0:.1f}s")
        if not loop:
            break


if __name__ == "__main__":
    loop = "--once" not in sys.argv
    main(loop=loop)

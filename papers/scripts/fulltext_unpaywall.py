"""DOI → Unpaywall → free PDF, last-stop fallback.

Unpaywall (https://unpaywall.org/) checks institutional repositories,
preprint servers, author homepages, etc., for an open-access copy of
any DOI. Free, no key beyond an email address.

For each SL paper with:
  - a DOI in externalIds
  - no cached full text
  - (optionally) tried-but-failed in fulltext_ss_alt's negative cache

call Unpaywall, look at best_oa_location.url_for_pdf or url, fetch
through docling, cache as <!--source:unpaywall-->.

Loop mode (default).
"""

from __future__ import annotations

import json
import os
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
UNPAYWALL_CACHE = STATE / "unpaywall_cache.json"

MAX_CHARS = 1_000_000
MIN_INTERVAL = 10.0  # seconds between Unpaywall calls — be polite
EMAIL = os.environ.get("UNPAYWALL_EMAIL", "papers-vault@example.com")

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


def _download_pdf(url: str, session: requests.Session, dest: Path) -> bool:
    """Download PDF with strict timeout. Returns True on success."""
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


def fetch_unpaywall(doi: str, session: requests.Session) -> dict | None:
    elapsed = time.monotonic() - _last_ts[0]
    if elapsed < MIN_INTERVAL:
        time.sleep(MIN_INTERVAL - elapsed)
    _last_ts[0] = time.monotonic()
    url = f"https://api.unpaywall.org/v2/{doi}?email={EMAIL}"
    try:
        resp = session.get(url, timeout=20)
    except requests.RequestException as e:
        print(f"  unpaywall {doi}: request failed: {e}")
        return None
    if resp.status_code == 404:
        return {"_unpaywall_status": "not_found"}
    if resp.status_code != 200:
        print(f"  unpaywall {doi}: status {resp.status_code}")
        return None
    try:
        return resp.json()
    except Exception:
        return None


def pick_pdf(unp: dict) -> str | None:
    if not unp or unp.get("_unpaywall_status") == "not_found":
        return None
    best = unp.get("best_oa_location") or {}
    for key in ("url_for_pdf", "url"):
        u = best.get(key)
        if u and (u.lower().endswith(".pdf") or "pdf" in u.lower()):
            return u
    # Fall back to scanning all locations.
    for loc in unp.get("oa_locations") or []:
        for key in ("url_for_pdf", "url"):
            u = loc.get(key)
            if u and (u.lower().endswith(".pdf") or "pdf" in u.lower()):
                return u
    return None


def candidates(judge: dict, bib_pids: set, cache: dict) -> list[tuple[str, str]]:
    """Returns list of (paperId, doi) for SL papers with DOI but no cached full text."""
    out = []
    for p in sorted(META_DIR.glob("*.json")):
        pid = p.stem
        if (FULLTEXT_DIR / f"{pid}.md").exists():
            continue
        if pid in cache and cache[pid].get("_unpaywall_status") == "not_found":
            continue  # tried, no luck
        if pid in cache and cache[pid].get("_tried_pdf"):
            continue  # tried fetching the PDF and failed
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
        # Skip if we already have a known direct source — those are
        # handled by the dedicated fetchers.
        if ext.get("ArXiv") or ext.get("ACL"):
            continue
        if (meta.get("openAccessPdf") or {}).get("url"):
            continue
        out.append((pid, doi))
    return out


def main(loop: bool = True, idle_sleep: int = 180) -> None:
    FULLTEXT_DIR.mkdir(parents=True, exist_ok=True)
    cache: dict = _load_json(UNPAYWALL_CACHE, {})
    session = requests.Session()
    session.headers["User-Agent"] = f"papers-vault-builder/1.0 (mailto:{EMAIL})"
    rd = 0
    while True:
        rd += 1
        judge = _load_json(JUDGE_PATH, {})
        bib_pids = {v for v in _load_json(SEED_PATH, {}).values() if v}
        todo = candidates(judge, bib_pids, cache)
        print(f"\n=== unpaywall round {rd}: {len(todo)} candidates ===")
        if not todo:
            if not loop:
                break
            time.sleep(idle_sleep)
            continue
        t0 = time.time()
        wins = 0
        for i, (pid, doi) in enumerate(todo, 1):
            unp = fetch_unpaywall(doi, session)
            if unp is None:
                continue
            cache[pid] = unp
            pdf = pick_pdf(unp)
            if not pdf:
                if i % 30 == 0:
                    _atomic_write_json(UNPAYWALL_CACHE, cache)
                continue
            tmp_pdf = FULLTEXT_DIR / f"{pid}.pdf.tmp"
            if not _download_pdf(pdf, session, tmp_pdf):
                if tmp_pdf.exists():
                    tmp_pdf.unlink()
                cache[pid] = {**unp, "_tried_pdf": True}
                continue
            try:
                result = _get_converter().convert(str(tmp_pdf))
            except Exception as e:
                print(f"[{i}/{len(todo)}] {pid}: docling failed on {pdf[:60]}: {e}")
                cache[pid] = {**unp, "_tried_pdf": True}
                tmp_pdf.unlink(missing_ok=True)
                continue
            tmp_pdf.unlink(missing_ok=True)
            text = result.document.export_to_markdown().strip() + "\n"
            if len(text) > MAX_CHARS:
                text = text[:MAX_CHARS] + "\n\n*[truncated to 1 MB]*\n"
            tmp = FULLTEXT_DIR / f"{pid}.md.tmp"
            tmp.write_text(f"<!--source:unpaywall-->\n{text}")
            os.replace(tmp, FULLTEXT_DIR / f"{pid}.md")
            wins += 1
            print(f"[{i}/{len(todo)}] {pid}: wrote {len(text)} chars from unpaywall ({pdf[:60]})")
            if i % 20 == 0:
                _atomic_write_json(UNPAYWALL_CACHE, cache)
        _atomic_write_json(UNPAYWALL_CACHE, cache)
        print(f"round {rd}: {wins}/{len(todo)} new fulltexts in {time.time() - t0:.1f}s")
        if not loop:
            break


if __name__ == "__main__":
    loop = "--once" not in sys.argv
    main(loop=loop)

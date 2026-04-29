"""Recover full text via Semantic Scholar's *internal* web-app API.

The public Graph API doesn't expose alternative PDF links, but
`https://www.semanticscholar.org/api/1/paper/<paperId>` (the endpoint
the web UI uses) returns `alternatePaperLinks` — auxiliary PDF URLs SS
has discovered (e.g. workshop sites, author homepages, institutional
repos) that aren't in `openAccessPdf`.

For each SL paper without a cached full text and without arxiv/PDF/ACL
already, query the internal API, look for a PDF URL in the alternate
links, run docling, cache to state/fulltext/<paperId>.md.

Loop mode (default): polls for new candidates every 2 min.
Idempotent: skips papers we already have full text for.
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
ALT_LINKS_CACHE = STATE / "ss_alt_links.json"
SS_NEGATIVE_CACHE = STATE / "ss_alt_negatives.json"  # papers with no PDF found

MAX_CHARS = 1_000_000
MIN_INTERVAL = 1.5  # seconds between SS internal API calls
SS_BASE = "https://www.semanticscholar.org/api/1/paper"

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


def fetch_alt_links(paper_id: str, session: requests.Session) -> list[dict] | None:
    elapsed = time.monotonic() - _last_ts[0]
    if elapsed < MIN_INTERVAL:
        time.sleep(MIN_INTERVAL - elapsed)
    _last_ts[0] = time.monotonic()
    url = f"{SS_BASE}/{paper_id}"
    try:
        resp = session.get(url, timeout=30, headers={"User-Agent": "papers-vault-builder/1.0"})
    except requests.RequestException as e:
        print(f"  ss-alt {paper_id}: request failed: {e}")
        return None
    if resp.status_code == 429:
        print(f"  ss-alt {paper_id}: 429, backing off 30s")
        time.sleep(30)
        return None
    if resp.status_code != 200:
        print(f"  ss-alt {paper_id}: status {resp.status_code}")
        return None
    try:
        d = resp.json()
    except Exception:
        return None
    p = d.get("paper") or {}
    return p.get("alternatePaperLinks") or []


def pick_pdf_url(alt_links: list[dict]) -> str | None:
    """Choose a likely-PDF url from alternatePaperLinks."""
    for link in alt_links:
        url = (link.get("url") or "").strip()
        if not url:
            continue
        # Direct PDF urls
        if url.lower().endswith(".pdf"):
            return url
        # Known PDF-hosting patterns
        if any(host in url for host in (
            "arxiv.org/pdf", "openreview.net/pdf", "proceedings.mlr.press",
            "papers.nips.cc", "openaccess.thecvf.com", "aclanthology.org",
            "sign-lang.uni-hamburg.de", "lrec-conf.org", "slrtp.com",
        )):
            return url
    return None


def candidates(judge: dict, bib_pids: set, alt_cache: dict, neg_cache: set) -> list[str]:
    out = []
    for p in sorted(META_DIR.glob("*.json")):
        pid = p.stem
        if (FULLTEXT_DIR / f"{pid}.md").exists():
            continue
        if pid in neg_cache:
            continue  # already tried, no luck
        try:
            meta = json.loads(p.read_text())
        except Exception:
            continue
        if not _is_sl(meta, judge, bib_pids):
            continue
        # Skip papers we already have a known PDF source for — those are
        # handled by fulltext.py / fulltext_acl.py.
        ext = meta.get("externalIds") or {}
        if ext.get("ArXiv") or ext.get("ACL"):
            continue
        if (meta.get("openAccessPdf") or {}).get("url"):
            continue
        out.append(pid)
    return out


def main(loop: bool = True, idle_sleep: int = 120) -> None:
    FULLTEXT_DIR.mkdir(parents=True, exist_ok=True)
    judge = _load_json(JUDGE_PATH, {})
    bib_pids = {v for v in _load_json(SEED_PATH, {}).values() if v}
    alt_cache: dict = _load_json(ALT_LINKS_CACHE, {})
    neg_cache: set = set(_load_json(SS_NEGATIVE_CACHE, []))
    session = requests.Session()
    rd = 0
    while True:
        rd += 1
        # Refresh judge cache — might have grown since last round.
        judge = _load_json(JUDGE_PATH, {})
        todo = candidates(judge, bib_pids, alt_cache, neg_cache)
        print(f"\n=== ss-alt round {rd}: {len(todo)} candidates ===")
        if not todo:
            if not loop:
                break
            time.sleep(idle_sleep)
            continue
        t0 = time.time()
        wins = 0
        for i, pid in enumerate(todo, 1):
            alt = fetch_alt_links(pid, session)
            if alt is None:  # transient error; let next round retry
                continue
            alt_cache[pid] = alt
            pdf_url = pick_pdf_url(alt)
            if not pdf_url:
                neg_cache.add(pid)
                if i % 20 == 0:
                    _atomic_write_json(SS_NEGATIVE_CACHE, sorted(neg_cache))
                    _atomic_write_json(ALT_LINKS_CACHE, alt_cache)
                continue
            try:
                result = _get_converter().convert(pdf_url)
            except Exception as e:
                print(f"[{i}/{len(todo)}] {pid}: docling failed on {pdf_url}: {e}")
                neg_cache.add(pid)
                continue
            text = result.document.export_to_markdown().strip() + "\n"
            if len(text) > MAX_CHARS:
                text = text[:MAX_CHARS] + "\n\n*[truncated to 1 MB]*\n"
            tmp = FULLTEXT_DIR / f"{pid}.md.tmp"
            tmp.write_text(f"<!--source:ss-alt-->\n{text}")
            os.replace(tmp, FULLTEXT_DIR / f"{pid}.md")
            wins += 1
            print(f"[{i}/{len(todo)}] {pid}: wrote {len(text)} chars from ss-alt ({pdf_url[:60]})")
            if i % 20 == 0:
                _atomic_write_json(ALT_LINKS_CACHE, alt_cache)
        _atomic_write_json(ALT_LINKS_CACHE, alt_cache)
        _atomic_write_json(SS_NEGATIVE_CACHE, sorted(neg_cache))
        print(f"round {rd}: {wins}/{len(todo)} new fulltexts in {time.time() - t0:.1f}s")
        if not loop:
            break


if __name__ == "__main__":
    loop = "--once" not in sys.argv
    main(loop=loop)

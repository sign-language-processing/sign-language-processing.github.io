"""ACL Anthology full-text extractor.

Sibling to fulltext.py — runs only over SL papers that have an ACL
Anthology id and don't yet have a cached full text. URL pattern:
    https://aclanthology.org/<acl-id>.pdf

Writes the same state/fulltext/<paperId>.md format as fulltext.py
(<!--source:acl--> prefix).
"""

from __future__ import annotations

import json
import os
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STATE = ROOT / "state"
META_DIR = STATE / "meta"
FULLTEXT_DIR = STATE / "fulltext"
JUDGE_PATH = STATE / "judge_cache.json"
SEED_PATH = STATE / "seed_bib.json"

MAX_CHARS = 1_000_000

_converter = None


def _get_converter():
    global _converter
    if _converter is None:
        from docling.document_converter import DocumentConverter
        _converter = DocumentConverter()
    return _converter


def _is_sl(meta: dict, judge: dict, bib_pids: set) -> bool:
    pid = meta.get("paperId")
    if pid in judge:
        return judge[pid]
    if pid in bib_pids:
        return True
    # Fallback to regex if not yet judged.
    sys.path.insert(0, str(ROOT / "scripts"))
    from classify import is_sign_language
    return is_sign_language(meta)


def candidates() -> list[tuple[str, str]]:
    """Returns list of (paperId, acl_id) for SL papers with ACL id but no cached full text."""
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
    url = f"https://aclanthology.org/{acl_id}.pdf"
    try:
        result = _get_converter().convert(url)
    except Exception as e:
        print(f"  acl {acl_id}: convert failed: {e}")
        return None
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
            print(f"sleeping {idle_sleep}s")
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

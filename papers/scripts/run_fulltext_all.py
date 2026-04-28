"""Run fulltext.extract over every cached SL paper that has an arxivId
(or an open-access PDF) and doesn't already have full text cached.
Idempotent — re-running picks up new papers as the crawler discovers
them. Independent of the SS API rate limit (uses ar5iv / publisher PDFs).
"""

from __future__ import annotations

import json
import time
from pathlib import Path

from classify import is_sign_language
from fulltext import FULLTEXT_DIR, META_DIR, extract


def candidates() -> list[str]:
    out = []
    for p in sorted(META_DIR.glob("*.json")):
        meta = json.loads(p.read_text())
        if not is_sign_language(meta):
            continue
        ext = meta.get("externalIds") or {}
        has_pdf = (meta.get("openAccessPdf") or {}).get("url")
        if not (ext.get("ArXiv") or has_pdf):
            continue
        if (FULLTEXT_DIR / f"{p.stem}.md").exists():
            continue
        out.append(p.stem)
    return out


def main() -> None:
    todo = candidates()
    print(f"Full-text candidates: {len(todo)}")
    t0 = time.time()
    for i, pid in enumerate(todo, 1):
        try:
            src, text = extract(pid)
        except Exception as e:
            print(f"[{i}/{len(todo)}] {pid}: ERROR {e}")
            continue
        if text:
            print(f"[{i}/{len(todo)}] {pid}: {len(text):>7} chars from {src}")
        else:
            print(f"[{i}/{len(todo)}] {pid}: no full text ({src})")
        # Be polite to ar5iv.
        time.sleep(0.5)
    print(f"Done in {time.time() - t0:.1f}s")


if __name__ == "__main__":
    main()

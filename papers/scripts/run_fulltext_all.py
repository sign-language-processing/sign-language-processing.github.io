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


def process_round(round_idx: int) -> int:
    todo = candidates()
    print(f"\n=== round {round_idx}: {len(todo)} new candidates ===")
    if not todo:
        return 0
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
        time.sleep(0.3)
    print(f"round {round_idx} done in {time.time() - t0:.1f}s")
    return len(todo)


def main(loop: bool = True, idle_sleep: int = 90) -> None:
    rd = 0
    while True:
        rd += 1
        n = process_round(rd)
        if not loop:
            break
        if n == 0:
            print(f"no new candidates; sleeping {idle_sleep}s")
            time.sleep(idle_sleep)


if __name__ == "__main__":
    import sys
    loop = "--once" not in sys.argv
    main(loop=loop)

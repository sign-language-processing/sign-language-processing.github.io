"""Resolve CSV/EML missed-paper titles to Semantic Scholar paperIds and
inject the new ones into the crawl frontier.

Input : a JSON list of {title, year, src} (path via argv[1]).
Output: state/seed_csv_eml.json  — {query_title: paperId|null} checkpoint,
        and the resolved new ids appended to state/frontier.json.

Resumable: re-running skips titles already in seed_csv_eml.json.
No year filter here — caller pre-filters to post-2014.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

from ss_client import SSClient

STATE = Path(__file__).resolve().parent.parent / "state"
SEED_OUT = STATE / "seed_csv_eml.json"
FRONTIER = STATE / "frontier.json"
VISITED = STATE / "visited.json"


def norm(t: str) -> str:
    return " ".join(re.sub(r"[^a-z0-9]+", " ", (t or "").lower()).split())


def title_ok(a: str, b: str) -> bool:
    a, b = norm(a), norm(b)
    if a == b:
        return True
    s = min(len(a), len(b))
    return s >= 25 and (a.startswith(b) or b.startswith(a))


def main(seeds_path: str) -> None:
    seeds = json.loads(Path(seeds_path).read_text())
    resolved = json.loads(SEED_OUT.read_text()) if SEED_OUT.exists() else {}
    client = SSClient()

    todo = [s for s in seeds if norm(s["title"]) not in resolved]
    print(f"{len(seeds)} seeds, {len(resolved)} already resolved, {len(todo)} to do", flush=True)

    for i, s in enumerate(todo):
        q = s["title"]
        key = norm(q)
        pid = None
        try:
            resp = client.get(
                "/paper/search/match",
                {"query": q[:300], "fields": "paperId,title,year"},
            )
            data = resp.get("data") or []
            if data and title_ok(q, data[0].get("title", "")):
                pid = data[0]["paperId"]
        except Exception as e:  # noqa: BLE001 — match returns 404 when no hit
            if "404" not in str(e):
                print(f"  err {key[:40]}: {e}", flush=True)
        resolved[key] = pid
        if (i + 1) % 20 == 0:
            SEED_OUT.write_text(json.dumps(resolved, ensure_ascii=False))
            found = sum(1 for v in resolved.values() if v)
            print(f"  {i + 1}/{len(todo)} resolved; {found} have paperIds", flush=True)

    SEED_OUT.write_text(json.dumps(resolved, ensure_ascii=False))

    # Inject new ids into frontier (skip ones already visited/known).
    visited = json.loads(VISITED.read_text()) if VISITED.exists() else {}
    frontier = json.loads(FRONTIER.read_text()) if FRONTIER.exists() else []
    fset = set(frontier)
    ids = {v for v in resolved.values() if v}
    new = [pid for pid in ids if pid not in visited and pid not in fset]
    frontier.extend(new)
    tmp = FRONTIER.with_suffix(".json.tmp")
    tmp.write_text(json.dumps(frontier, ensure_ascii=False))
    tmp.replace(FRONTIER)

    print(
        f"DONE: {len(ids)} titles resolved to ids; "
        f"{len(ids & set(visited))} already in crawl; "
        f"{len(new)} NEW ids added to frontier (now {len(frontier)})",
        flush=True,
    )


if __name__ == "__main__":
    main(sys.argv[1])

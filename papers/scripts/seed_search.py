"""Seed: every SL paper from 2014 onward via SS bulk search.

Idempotent — writes state/seed_search.json. Re-running unions any new
results into the existing set.
"""

from __future__ import annotations

import json
from pathlib import Path

from classify import is_sign_language
from ss_client import SSClient

STATE = Path(__file__).resolve().parent.parent / "state"
OUT_PATH = STATE / "seed_search.json"

QUERIES = [
    "sign language",
    "signed language",
    "fingerspelling",
    "sign language recognition",
    "sign language translation",
    "sign language production",
]

FIELDS = "paperId,title,abstract,year,venue,publicationVenue"


def main() -> None:
    seen: dict[str, dict] = {}  # paperId -> minimal info for review
    if OUT_PATH.exists():
        existing = json.loads(OUT_PATH.read_text())
        for p in existing:
            seen[p["paperId"]] = p

    client = SSClient()

    for q in QUERIES:
        print(f"Query: {q!r}")
        token = None
        n_total = 0
        n_kept = 0
        while True:
            params = {
                "query": q,
                "fields": FIELDS,
                "year": "2014-",
            }
            if token:
                params["token"] = token
            page = client.get("/paper/search/bulk", params=params)
            data = page.get("data") or []
            if not data:
                break
            n_total += len(data)
            for p in data:
                pid = p.get("paperId")
                if not pid or pid in seen:
                    continue
                if not is_sign_language(p):
                    continue
                seen[pid] = {
                    "paperId": pid,
                    "title": p.get("title"),
                    "year": p.get("year"),
                }
                n_kept += 1
            token = page.get("token")
            print(f"  page +{len(data)} (kept {n_kept}/{n_total} so far)")
            # Checkpoint each page.
            tmp = OUT_PATH.with_suffix(".tmp")
            tmp.write_text(json.dumps(list(seen.values()), indent=2, ensure_ascii=False))
            tmp.replace(OUT_PATH)
            if not token:
                break
        print(f"  done — {n_kept} kept of {n_total} returned")

    print(f"Total SL papers (2014+): {len(seen)}")


if __name__ == "__main__":
    main()

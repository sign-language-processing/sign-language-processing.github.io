"""Resolve every bib entry to a Semantic Scholar paperId.

Pass 1: batch lookup using DOI / ARXIV / ACL / URL identifiers.
Pass 2: title-search /paper/search/match for entries that didn't resolve.

Idempotent — loads state/seed_bib.json on start and only resolves the
bibKeys not already mapped.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

from ss_client import SSClient

STATE = Path(__file__).resolve().parent.parent / "state"
BIB_JSON = STATE / "bib.json"
SEED_PATH = STATE / "seed_bib.json"
UNRESOLVED_PATH = STATE / "unresolved_bib.json"

FIELDS = "paperId,externalIds,title,year"


def candidate_id(entry: dict) -> str | None:
    if entry.get("doi"):
        return f"DOI:{entry['doi']}"
    if entry.get("arxivId"):
        return f"ARXIV:{entry['arxivId']}"
    if entry.get("aclId"):
        return f"ACL:{entry['aclId']}"
    if entry.get("url"):
        return f"URL:{entry['url']}"
    return None


def _save(seed: dict, unresolved: list[dict]) -> None:
    SEED_PATH.write_text(json.dumps(seed, indent=2, ensure_ascii=False))
    UNRESOLVED_PATH.write_text(json.dumps(unresolved, indent=2, ensure_ascii=False))


def main() -> None:
    entries = json.loads(BIB_JSON.read_text())
    seed: dict[str, str | None] = {}
    if SEED_PATH.exists():
        seed = json.loads(SEED_PATH.read_text())
    todo = [e for e in entries if e["bibKey"] not in seed]
    print(f"{len(entries)} entries; {len(seed)} already resolved; {len(todo)} todo")

    client = SSClient()

    # Pass 1: batch lookups by external ID.
    with_cand = [(e, candidate_id(e)) for e in todo]
    batchable = [(e, cid) for e, cid in with_cand if cid]
    if batchable:
        print(f"Pass 1: batch lookup for {len(batchable)} entries")
        ids = [cid for _, cid in batchable]
        results = client.batch(
            ids, fields=FIELDS
        )  # type: ignore[arg-type]
        for (e, cid), res in zip(batchable, results):
            if res and res.get("paperId"):
                seed[e["bibKey"]] = res["paperId"]
            else:
                seed.setdefault(e["bibKey"], None)
        _save(seed, [])
        hits = sum(1 for (e, _) in batchable if seed.get(e["bibKey"]))
        print(f"  pass 1 resolved {hits}/{len(batchable)}")

    # Pass 2: title-search /paper/search/match for everyone still null.
    pending = [e for e in entries if seed.get(e["bibKey"]) is None]
    print(f"Pass 2: title-match for {len(pending)} entries")
    unresolved: list[dict] = []
    for i, e in enumerate(pending):
        if not e.get("title"):
            unresolved.append({"bibKey": e["bibKey"], "reason": "no title"})
            continue
        try:
            res = client.get(
                "/paper/search/match",
                params={"query": e["title"], "fields": FIELDS},
            )
        except Exception as ex:
            # /paper/search/match returns 404 when no match — treat as unresolved.
            err = str(ex)
            if "404" in err:
                unresolved.append({"bibKey": e["bibKey"], "reason": "no match", "title": e["title"]})
                seed[e["bibKey"]] = None
                if i % 10 == 0:
                    _save(seed, unresolved)
                continue
            raise
        data = (res or {}).get("data") or []
        if not data:
            unresolved.append({"bibKey": e["bibKey"], "reason": "no data", "title": e["title"]})
            seed[e["bibKey"]] = None
            continue
        top = data[0]
        # Sanity: year should match if we have one.
        if e.get("year") and top.get("year") and abs(int(top["year"]) - int(e["year"])) > 1:
            unresolved.append(
                {
                    "bibKey": e["bibKey"],
                    "reason": "year mismatch",
                    "title": e["title"],
                    "expected_year": e["year"],
                    "got_year": top.get("year"),
                    "got_title": top.get("title"),
                    "got_id": top.get("paperId"),
                }
            )
            seed[e["bibKey"]] = None
            continue
        seed[e["bibKey"]] = top["paperId"]
        if i % 10 == 0:
            _save(seed, unresolved)
    _save(seed, unresolved)

    resolved = sum(1 for v in seed.values() if v)
    print(f"Final: {resolved}/{len(seed)} resolved; {len(unresolved)} unresolved")


if __name__ == "__main__":
    sys.exit(main())

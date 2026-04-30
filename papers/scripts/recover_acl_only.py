"""Recover ACL Anthology SL papers that aren't already in our vault.

For each ACL id that the SS batch couldn't resolve (acl_recovery_unresolved.json):
  1. Try /paper/search/match by title
  2. If still not found, synthesize a meta entry from ACL anthology data
     (title, year, ACL id, no abstract, no neighbors) and stash under
     state/meta/acl-<acl_id>.json so the renderer picks it up.
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

sys.path.insert(0, str(ROOT / "scripts"))
from ss_client import SSClient  # noqa: E402


def synthetic_meta(acl_id: str, title: str, year: int) -> dict:
    """A meta JSON shaped like SS responses, keyed by a synthetic paperId."""
    pid = f"acl-{acl_id}"
    return {
        "paperId": pid,
        "externalIds": {"ACL": acl_id},
        "title": title,
        "abstract": None,
        "year": year,
        "authors": [],
        "venue": None,
        "publicationVenue": None,
        "publicationTypes": None,
        "citationStyles": None,
        "citationCount": 0,
        "referenceCount": 0,
        "fieldsOfStudy": None,
        "s2FieldsOfStudy": None,
        "openAccessPdf": None,
        "tldr": None,
        "_synthetic": True,
        "_source": "acl_anthology",
    }


def main():
    unresolved = json.loads((STATE / "acl_recovery_unresolved.json").read_text())
    print(f"Recovering {len(unresolved)} ACL-only papers (SS batch failed on these)")

    c = SSClient()
    title_resolved: list[dict] = []
    synthesized: list[str] = []

    for i, e in enumerate(unresolved, 1):
        title = e.get("title") or ""
        year = e.get("year")
        acl_id = e["acl_id"]
        if not title:
            # Just synthesize.
            meta = synthetic_meta(acl_id, "", year)
            META_DIR.mkdir(parents=True, exist_ok=True)
            tmp = META_DIR / f"{meta['paperId']}.json.tmp"
            tmp.write_text(json.dumps(meta, indent=2, ensure_ascii=False))
            os.replace(tmp, META_DIR / f"{meta['paperId']}.json")
            synthesized.append(acl_id)
            continue
        # Try title-search first.
        try:
            res = c.get(
                "/paper/search/match",
                params={"query": title, "fields": "paperId,externalIds,title,abstract,year"},
            )
        except Exception as ex:
            res = None
            if "404" not in str(ex):
                print(f"  [{i}] error {acl_id}: {ex}")
        data = (res or {}).get("data") or [] if isinstance(res, dict) else []
        chosen = None
        if data:
            top = data[0]
            # Sanity: year ±1 if both have it.
            ok = True
            if year and top.get("year") and abs(int(top["year"]) - int(year)) > 1:
                ok = False
            if ok:
                chosen = top
        if chosen:
            # SS knows it under a different ACL id — record + skip synthesis.
            title_resolved.append(
                {"acl_id": acl_id, "paperId": chosen["paperId"], "title": chosen.get("title"), "year": chosen.get("year")}
            )
            print(f"  [{i}] title-search: {acl_id} -> {chosen['paperId']}")
        else:
            meta = synthetic_meta(acl_id, title, year)
            tmp = META_DIR / f"{meta['paperId']}.json.tmp"
            tmp.write_text(json.dumps(meta, indent=2, ensure_ascii=False))
            os.replace(tmp, META_DIR / f"{meta['paperId']}.json")
            synthesized.append(acl_id)
            print(f"  [{i}] synthesized:  {acl_id}: {title[:60]}")

    (STATE / "acl_titlesearch_resolved.json").write_text(
        json.dumps(title_resolved, indent=2, ensure_ascii=False)
    )
    (STATE / "acl_synthesized.json").write_text(
        json.dumps(sorted(synthesized), indent=2, ensure_ascii=False)
    )
    print(f"\ntitle-search resolved: {len(title_resolved)}")
    print(f"synthesized meta entries: {len(synthesized)}")


if __name__ == "__main__":
    main()

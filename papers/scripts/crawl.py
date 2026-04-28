"""Fault-tolerant BFS crawler over the sign-language citation graph.

State (all under papers/state/, atomic writes via .tmp + rename):
  meta/<paperId>.json    — raw SS metadata for each known paper
  edges/<paperId>.json   — {"references": [...], "citations": [...]} for expanded nodes
  visited.json           — {paperId: "expanded" | "leaf"}
  frontier.json          — list of paperIds queued for fetch
  classifier_cache.json  — {paperId: bool}
  seed_bib.json          — bibKey -> paperId (read-only)
  seed_search.json       — list of {paperId, ...} (read-only)

Resumability:
  - On every iteration we checkpoint visited.json + frontier.json after
    metadata fetch, and again after expansion of each paper.
  - meta/<id>.json being on disk is the canonical "we know about this
    paper" signal; visited["leaf"] follows it.
  - edges/<id>.json being on disk is the canonical "we expanded this
    paper" signal; visited["expanded"] follows it.
  - If frontier.json is lost, _bootstrap_frontier rebuilds from the
    seeds + edges/ minus meta/.

No year filter on traversal — follow SL citations of any vintage.
"""

from __future__ import annotations

import json
import os
import sys
import time
from pathlib import Path
from typing import Iterable

from classify import CachedClassifier, is_sign_language
from ss_client import SSClient

STATE = Path(__file__).resolve().parent.parent / "state"
META_DIR = STATE / "meta"
EDGES_DIR = STATE / "edges"
VISITED_PATH = STATE / "visited.json"
FRONTIER_PATH = STATE / "frontier.json"
SEED_BIB_PATH = STATE / "seed_bib.json"
SEED_SEARCH_PATH = STATE / "seed_search.json"

META_FIELDS = (
    "paperId,externalIds,title,abstract,tldr,year,authors.name,authors.authorId,"
    "venue,publicationVenue,publicationTypes,citationStyles,citationCount,"
    "referenceCount,fieldsOfStudy,s2FieldsOfStudy,openAccessPdf"
)
EDGE_FIELDS = "paperId,title,year,externalIds,abstract,venue,publicationVenue"

CITATION_CAP = 200  # per-paper hard cap on citation expansion (configurable)
BATCH_SIZE = 500
CHECKPOINT_EVERY_PAPERS = 25


def _atomic_write_json(path: Path, data) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(data, ensure_ascii=False))
    os.replace(tmp, path)


def _load_json(path: Path, default):
    if not path.exists():
        return default
    try:
        return json.loads(path.read_text())
    except json.JSONDecodeError:
        return default


def _seed_paper_ids() -> set[str]:
    ids: set[str] = set()
    bib = _load_json(SEED_BIB_PATH, {})
    for v in bib.values():
        if v:
            ids.add(v)
    search = _load_json(SEED_SEARCH_PATH, [])
    for p in search:
        if p.get("paperId"):
            ids.add(p["paperId"])
    return ids


def _known_meta_ids() -> set[str]:
    if not META_DIR.exists():
        return set()
    return {p.stem for p in META_DIR.glob("*.json")}


def _expanded_ids() -> set[str]:
    if not EDGES_DIR.exists():
        return set()
    return {p.stem for p in EDGES_DIR.glob("*.json")}


def _bootstrap_frontier(visited: dict[str, str]) -> list[str]:
    """Rebuild the frontier from disk if frontier.json is missing/stale.
    Frontier = (seed ∪ neighbors of expanded) - already-known.
    Bib seeds come first so we expand our cited papers before the wider
    search seeds (better signal density early)."""
    known = _known_meta_ids()
    bib_map = _load_json(SEED_BIB_PATH, {})
    bib_pids = [v for v in bib_map.values() if v and v not in known]
    search_pids = [
        p["paperId"] for p in _load_json(SEED_SEARCH_PATH, [])
        if p.get("paperId") and p["paperId"] not in known
    ]
    seen: set[str] = set()
    ordered: list[str] = []
    for pid in bib_pids + search_pids:
        if pid not in seen:
            ordered.append(pid)
            seen.add(pid)
    for pid in _expanded_ids():
        edges = _load_json(EDGES_DIR / f"{pid}.json", {})
        for n in edges.get("references", []) + edges.get("citations", []):
            nid = n.get("paperId")
            if nid and nid not in known and nid not in seen:
                ordered.append(nid)
                seen.add(nid)
    return ordered


def _save_meta(meta: dict) -> None:
    pid = meta.get("paperId")
    if not pid:
        return
    _atomic_write_json(META_DIR / f"{pid}.json", meta)


def _save_edges(pid: str, refs: list[dict], cits: list[dict]) -> None:
    _atomic_write_json(
        EDGES_DIR / f"{pid}.json",
        {"references": refs, "citations": cits},
    )


def _is_in_bib(pid: str, bib_paperids: set[str]) -> bool:
    return pid in bib_paperids


def _should_expand(meta: dict, classifier: CachedClassifier, bib_paperids: set[str]) -> bool:
    pid = meta.get("paperId")
    if pid and pid in bib_paperids:
        return True
    return classifier.classify(meta)


def crawl(max_iterations: int | None = None) -> None:
    META_DIR.mkdir(parents=True, exist_ok=True)
    EDGES_DIR.mkdir(parents=True, exist_ok=True)

    visited: dict[str, str] = _load_json(VISITED_PATH, {})
    # Sync visited from disk truth: meta=>leaf, edges=>expanded.
    for pid in _known_meta_ids():
        visited.setdefault(pid, "leaf")
    for pid in _expanded_ids():
        visited[pid] = "expanded"

    frontier = _load_json(FRONTIER_PATH, None)
    if not frontier:
        frontier = _bootstrap_frontier(visited)
        print(f"Bootstrapped frontier with {len(frontier)} ids")
    frontier_set = set(frontier)
    # Drop any IDs we've already fetched (resume safety).
    frontier = [p for p in frontier if p not in visited]

    bib_map = _load_json(SEED_BIB_PATH, {})
    bib_paperids = {v for v in bib_map.values() if v}
    classifier = CachedClassifier()

    client = SSClient()

    iteration = 0
    while frontier:
        iteration += 1
        if max_iterations and iteration > max_iterations:
            print(f"Stopping after {max_iterations} iterations (cap reached)")
            break

        batch = frontier[:BATCH_SIZE]
        frontier = frontier[BATCH_SIZE:]
        # Checkpoint frontier before expensive call so a crash mid-batch
        # is recoverable (we'll re-fetch the batch, idempotent).
        _atomic_write_json(FRONTIER_PATH, batch + frontier)

        print(f"[iter {iteration}] frontier={len(batch) + len(frontier)} "
              f"visited={len(visited)} fetching {len(batch)}")
        try:
            metas = client.batch(batch, fields=META_FIELDS)
        except Exception as e:
            print(f"  batch failed: {e}; will retry next run")
            return

        # Persist metadata, mark leaves.
        expand_queue: list[dict] = []
        for pid, meta in zip(batch, metas):
            if not meta:
                # SS doesn't know this id; mark visited as a dead leaf.
                visited[pid] = "leaf"
                continue
            _save_meta(meta)
            real_pid = meta.get("paperId") or pid
            visited[real_pid] = visited.get(real_pid, "leaf")
            if real_pid != pid:
                visited[pid] = "leaf"
            if _should_expand(meta, classifier, bib_paperids):
                expand_queue.append(meta)

        classifier.save()
        _atomic_write_json(VISITED_PATH, visited)
        _atomic_write_json(FRONTIER_PATH, frontier)
        print(f"  metadata cached for {len(metas)}; {len(expand_queue)} queued for expansion")

        # Expand each. Each expansion is many API calls (paginated refs/cits).
        for j, meta in enumerate(expand_queue):
            pid = meta["paperId"]
            if pid in _expanded_ids():
                continue
            try:
                refs = list(
                    client.paginate(
                        f"/paper/{pid}/references",
                        fields=EDGE_FIELDS,
                    )
                )
                cits = list(
                    client.paginate(
                        f"/paper/{pid}/citations",
                        fields=EDGE_FIELDS,
                        max_items=CITATION_CAP,
                    )
                )
            except Exception as e:
                print(f"  expand {pid} failed: {e}; skipping for this run")
                continue
            ref_papers = [r["citedPaper"] for r in refs if r.get("citedPaper")]
            cit_papers = [c["citingPaper"] for c in cits if c.get("citingPaper")]
            _save_edges(pid, ref_papers, cit_papers)
            visited[pid] = "expanded"

            # Add new neighbors to the frontier — only SL ones (or we'd
            # blow up). Check abstract/title locally; full meta will be
            # fetched in the next batch round.
            new_added = 0
            for neighbor in ref_papers + cit_papers:
                nid = neighbor.get("paperId")
                if not nid or nid in visited or nid in frontier_set:
                    continue
                # Quick local classifier on the snippet we already have.
                if is_sign_language(neighbor) or nid in bib_paperids:
                    frontier.append(nid)
                    frontier_set.add(nid)
                    new_added += 1
            print(f"    [{j + 1}/{len(expand_queue)}] {pid} "
                  f"refs={len(ref_papers)} cits={len(cit_papers)} +{new_added} new")

            if (j + 1) % CHECKPOINT_EVERY_PAPERS == 0:
                classifier.save()
                _atomic_write_json(VISITED_PATH, visited)
                _atomic_write_json(FRONTIER_PATH, frontier)

        classifier.save()
        _atomic_write_json(VISITED_PATH, visited)
        _atomic_write_json(FRONTIER_PATH, frontier)

    print("Frontier drained. Done.")


if __name__ == "__main__":
    n = int(sys.argv[1]) if len(sys.argv) > 1 else None
    crawl(max_iterations=n)

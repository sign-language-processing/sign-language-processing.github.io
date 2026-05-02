"""Rate-limited Semantic Scholar Graph API client.

Limit: 100 requests / 5 minutes (sliding window). Honors
SEMANTIC_SCHOLAR_API_KEY env var (sent as x-api-key) but does not raise
the rate cap. Every call is appended to papers/state/api_log.jsonl as
one JSON line.
"""

from __future__ import annotations

import json
import os
import random
import time
from collections import deque
from pathlib import Path
from typing import Any, Iterable, Iterator

import requests

API_BASE = "https://api.semanticscholar.org/graph/v1"
WINDOW_SECONDS = 300
WINDOW_LIMIT = 100  # leave it conservative; SS limit is 100/5min
STATE_DIR = Path(__file__).resolve().parent.parent / "state"
LOG_PATH = STATE_DIR / "api_log.jsonl"


class SSClient:
    def __init__(self, api_key: str | None = None, log_path: Path = LOG_PATH):
        self.session = requests.Session()
        self.api_key = api_key or os.environ.get("SEMANTIC_SCHOLAR_API_KEY")
        if self.api_key:
            self.session.headers["x-api-key"] = self.api_key
        self.log_path = log_path
        self.log_path.parent.mkdir(parents=True, exist_ok=True)
        self._times: deque[float] = deque()

    def _throttle(self) -> None:
        now = time.monotonic()
        while self._times and now - self._times[0] > WINDOW_SECONDS:
            self._times.popleft()
        if len(self._times) >= WINDOW_LIMIT:
            sleep_for = WINDOW_SECONDS - (now - self._times[0]) + 0.5
            if sleep_for > 0:
                time.sleep(sleep_for)
            return self._throttle()
        # Soft pacing — keep a steady ~1 req / 3.1s baseline.
        if self._times:
            since_last = now - self._times[-1]
            target = WINDOW_SECONDS / WINDOW_LIMIT  # 3.0s
            if since_last < target:
                time.sleep(target - since_last + random.uniform(0, 0.3))

    def _log(self, entry: dict[str, Any]) -> None:
        with self.log_path.open("a") as f:
            f.write(json.dumps(entry) + "\n")

    def _call(
        self,
        method: str,
        path: str,
        *,
        params: dict | None = None,
        json_body: Any = None,
        max_retries: int = 5,
    ) -> Any:
        url = f"{API_BASE}{path}" if path.startswith("/") else path
        attempt = 0
        while True:
            self._throttle()
            self._times.append(time.monotonic())
            t0 = time.time()
            try:
                resp = self.session.request(
                    method, url, params=params, json=json_body, timeout=60
                )
            except requests.RequestException as e:
                self._log({"ts": t0, "method": method, "url": url, "error": str(e)})
                if attempt >= max_retries:
                    raise
                time.sleep(2 ** attempt + random.random())
                attempt += 1
                continue

            self._log(
                {
                    "ts": t0,
                    "method": method,
                    "url": url,
                    "status": resp.status_code,
                    "params": params,
                }
            )
            if resp.status_code == 200:
                return resp.json()
            if resp.status_code in (429, 500, 502, 503, 504):
                if attempt >= max_retries:
                    resp.raise_for_status()
                # Honor Retry-After when present, else exponential backoff.
                retry_after = resp.headers.get("Retry-After")
                wait = float(retry_after) if retry_after else (2 ** attempt + random.random())
                time.sleep(min(wait, 60))
                attempt += 1
                continue
            # 4xx other than 429: don't retry.
            resp.raise_for_status()

    # Convenience wrappers ----------------------------------------------

    def get(self, path: str, params: dict | None = None) -> Any:
        return self._call("GET", path, params=params)

    def post(self, path: str, json_body: Any, params: dict | None = None) -> Any:
        return self._call("POST", path, params=params, json_body=json_body)

    def batch(self, ids: Iterable[str], fields: str) -> list[dict | None]:
        """POST /paper/batch in chunks of <=500."""
        ids = list(ids)
        out: list[dict | None] = []
        for i in range(0, len(ids), 500):
            chunk = ids[i : i + 500]
            res = self.post(
                "/paper/batch",
                params={"fields": fields},
                json_body={"ids": chunk},
            )
            # Response is a list aligned with input; entries can be null
            # if the ID is unknown.
            out.extend(res)
        return out

    def paginate(
        self,
        path: str,
        *,
        fields: str,
        limit: int = 100,
        max_items: int | None = None,
    ) -> Iterator[dict]:
        """Iterate offset-paginated endpoints (/references, /citations,
        /search). Stops at max_items if given."""
        offset = 0
        yielded = 0
        while True:
            params = {"fields": fields, "limit": limit, "offset": offset}
            page = self.get(path, params=params)
            data = page.get("data", [])
            if not data:
                return
            for item in data:
                yield item
                yielded += 1
                if max_items is not None and yielded >= max_items:
                    return
            next_offset = page.get("next")
            if next_offset is None:
                return
            offset = next_offset


if __name__ == "__main__":
    # Sanity check: fetch one well-known paper.
    c = SSClient()
    p = c.get(
        "/paper/DOI:10.1109/ICASSP.2019.8683257",
        params={"fields": "paperId,title,year,authors.name"},
    )
    print(json.dumps(p, indent=2))

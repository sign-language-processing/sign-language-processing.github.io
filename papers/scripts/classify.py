"""Sign-language classifier — keyword + venue heuristic.

Returns True if the paper looks SL-related based on its title, abstract,
venue, and field-of-study tags. Cache decisions in
state/classifier_cache.json to avoid recomputation.
"""

from __future__ import annotations

import json
import re
from pathlib import Path

CACHE_PATH = Path(__file__).resolve().parent.parent / "state" / "classifier_cache.json"

# Word-boundary regex over SL keywords. `signer` / `signing` matched only
# in obvious contexts to avoid false positives (e.g. "signing experiments").
KEYWORD_RE = re.compile(
    r"\b("
    r"sign[- ]language(s)?|"
    r"signed[- ]language(s)?|"
    r"fingerspell\w*|"
    r"co[- ]?sign\w*|"
    r"signwriting|"
    r"hamnosys|"
    r"glosses?|glossing|"
    r"asl|bsl|dgs|lsf|lse|ngt|libras|jsl|isl|csl|"
    r"phoenix-?(?:weather|2014|2014t)|"
    r"how2sign|wlasl|ms[- ]asl|bsl-?1k|bobsl|openasl|youtube[- ]asl|"
    r"yt[- ]asl|signbank|signum|swisstxt|content4all|"
    r"deaf community|deaf signer"
    r")\b",
    re.IGNORECASE,
)

VENUE_RE = re.compile(
    r"\b("
    r"sltat|sign-lang|wmt-?slt|slrtp|slpat|"
    r"workshop on sign language|"
    r"representation and processing of sign languages"
    r")\b",
    re.IGNORECASE,
)


def is_sign_language(meta: dict) -> bool:
    """Decide whether a Semantic Scholar paper meta dict is SL-related."""
    haystacks = []
    for key in ("title", "abstract"):
        v = meta.get(key) or ""
        if v:
            haystacks.append(v)
    venue_hay = []
    for key in ("venue",):
        v = meta.get(key) or ""
        if v:
            venue_hay.append(v)
    pv = meta.get("publicationVenue") or {}
    if isinstance(pv, dict):
        if pv.get("name"):
            venue_hay.append(pv["name"])
    text = " ".join(haystacks)
    if KEYWORD_RE.search(text):
        return True
    if venue_hay and VENUE_RE.search(" ".join(venue_hay)):
        return True
    # Fall back: keyword in venue text
    if venue_hay and KEYWORD_RE.search(" ".join(venue_hay)):
        return True
    return False


class CachedClassifier:
    def __init__(self, path: Path = CACHE_PATH):
        self.path = path
        self.cache: dict[str, bool] = {}
        if path.exists():
            self.cache = json.loads(path.read_text())

    def classify(self, meta: dict) -> bool:
        pid = meta.get("paperId")
        if pid and pid in self.cache:
            return self.cache[pid]
        result = is_sign_language(meta)
        if pid:
            self.cache[pid] = result
        return result

    def save(self) -> None:
        tmp = self.path.with_suffix(".tmp")
        tmp.write_text(json.dumps(self.cache, indent=2))
        tmp.replace(self.path)


if __name__ == "__main__":
    # Spot-check.
    samples = [
        {"title": "Real-Time Sign-Language Detection using Human Pose Estimation"},
        {"title": "Very Deep Convolutional Networks for Large-Scale Image Recognition"},
        {"title": "RWTH-PHOENIX-Weather 2014: A Large Vocabulary Sign Language Recognition Corpus"},
        {"title": "Attention Is All You Need"},
        {"title": "How2Sign: A Large-scale Multimodal Dataset for Sign Language"},
    ]
    for s in samples:
        print(f"  {is_sign_language(s)} :: {s['title']}")

"""Sign-language classifier — strict heuristic.

Returns True only when the paper is *about* sign-language processing,
not when it merely mentions sign language in passing. A paper qualifies
if any one of these is true:

  1. Title contains an SL keyword.
  2. Abstract or title contains a specific SL technical phrase
     (recognition/translation/production/etc., dataset names,
     fingerspelling, SignWriting, HamNoSys).
  3. Venue is a known SL workshop/journal.
  4. Abstract mentions "sign language" 2+ times.

Cache decisions in state/classifier_cache.json.
"""

from __future__ import annotations

import json
import re
from pathlib import Path

CACHE_PATH = Path(__file__).resolve().parent.parent / "state" / "classifier_cache.json"

# Match in TITLE: any of these is enough.
TITLE_RE = re.compile(
    r"\b(sign[- ]?language(s)?|signed[- ]?language(s)?|fingerspell\w*|"
    r"signwriting|hamnosys|signbank|sign[- ]?lang)\b",
    re.IGNORECASE,
)

# Strong technical phrases (anywhere): unambiguous SL research.
STRONG_RE = re.compile(
    r"\b("
    r"sign[- ]?language\s+(?:recognition|translation|production|detection|"
    r"segmentation|generation|processing|understanding|transcription|"
    r"interpreting|interpretation|modeling|modelling|synthesis|alignment)|"
    r"signed[- ]?language\s+(?:recognition|translation|production|detection|"
    r"processing|modeling|modelling)|"
    r"continuous\s+sign[- ]?language|isolated\s+sign[- ]?language|"
    r"fingerspelling|signwriting|hamnosys|signbank|"
    r"phoenix(?:[- ]?2014t?|[- ]?weather)?|"
    r"how2sign|wlasl|ms[- ]?asl|bsl[- ]?1k|bobsl|openasl|youtube[- ]asl|yt[- ]asl|"
    r"asl\s+gloss(es)?|gloss[- ]to[- ]text|gloss[- ]free|gloss[- ]based|"
    r"sign\s+segmentation|sign\s+spotting|deaf\s+signer|deaf\s+signers"
    r")\b",
    re.IGNORECASE,
)

VENUE_RE = re.compile(
    r"\b("
    r"sltat|sign-?lang|wmt-?slt|slrtp|slpat|"
    r"workshop on sign language|"
    r"representation and processing of sign languages|"
    r"sign language translation|"
    r"sign language and gesture"
    r")\b",
    re.IGNORECASE,
)

SL_MENTION_RE = re.compile(r"\bsign[- ]?language", re.IGNORECASE)


def _venue_text(meta: dict) -> str:
    parts = [meta.get("venue") or ""]
    pv = meta.get("publicationVenue") or {}
    if isinstance(pv, dict):
        parts.append(pv.get("name") or "")
    return " ".join(parts)


def is_sign_language(meta: dict) -> bool:
    title = meta.get("title") or ""
    abstract = meta.get("abstract") or ""
    if TITLE_RE.search(title):
        return True
    if STRONG_RE.search(title) or STRONG_RE.search(abstract):
        return True
    if VENUE_RE.search(_venue_text(meta)):
        return True
    if len(SL_MENTION_RE.findall(abstract)) >= 2:
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
    samples = [
        {"title": "Real-Time Sign-Language Detection using Human Pose Estimation"},
        {"title": "Very Deep Convolutional Networks for Large-Scale Image Recognition"},
        {"title": "RWTH-PHOENIX-Weather 2014: A Large Vocabulary Sign Language Recognition Corpus"},
        {"title": "Attention Is All You Need"},
        {"title": "How2Sign: A Large-scale Multimodal Dataset for Sign Language"},
        # The Indonesian-batik paper that wrongly slipped through:
        {
            "title": "Komunikasi Instruksional Guru ... Tunarungu",
            "abstract": "...teachers use total instructional communication methods with projector media, batik tools and materials, textbooks and sign language. In addition, ...",
        },
        # Should still pass: paper that mentions SL twice in abstract.
        {
            "title": "Gesture and motion analysis",
            "abstract": "We study sign language production and recognition. Our model handles sign language better than ...",
        },
    ]
    for s in samples:
        print(f"  {is_sign_language(s)} :: {s['title'][:70]}")

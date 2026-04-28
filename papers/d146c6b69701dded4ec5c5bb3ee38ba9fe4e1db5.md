---
semanticScholarId: "d146c6b69701dded4ec5c5bb3ee38ba9fe4e1db5"
bibKey: null
year: 2026
title: "SignDPO: Multi-level Direct Preference Optimisation for Skeleton-based Gloss-free Sign Language Translation"
doi: null
arxivId: "2604.18034"
isSignLanguage: true
expanded: false
topics: ["Computer Science", "Linguistics"]
fullText: "none"
fullTextSource: "none"
bibtexSource: "semanticscholar"
sources:
  title: semanticscholar
  abstract: semanticscholar
  authors: semanticscholar
  topics: semanticscholar
  references: none
  citations: none
  fullText: none
  bibtex: semanticscholar
---

# SignDPO: Multi-level Direct Preference Optimisation for Skeleton-based Gloss-free Sign Language Translation

**Year:** [[2026]]
**Topics:** [[topics/computer-science|Computer Science]], [[topics/linguistics|Linguistics]]
**Authors:** Muxin Pu; Xiao-Ming Wu; Mei Kuan Lim; Chun Yong Chong; Wei Li; Chen Change Loy

## Links
- [Semantic Scholar](https://www.semanticscholar.org/paper/d146c6b69701dded4ec5c5bb3ee38ba9fe4e1db5)
- [arXiv:2604.18034](https://arxiv.org/abs/2604.18034)

## Abstract

We present SignDPO, a novel multi-level Direct Preference Optimisation (DPO) framework designed to enhance the alignment of skeleton-based Sign Language Translation. While current skeleton-based models have made significant progress using Maximum Likelihood Estimation, they are primarily constrained by an imitation-based paradigm that lacks discriminative sensitivity to the fine-grained spatio-temporal nuances of sign language, often leading to semantic drift. To address this, SignDPO shifts the optimisation goal from simple sequence mimicry to structured preference alignment across spatial, temporal, and linguistic dimensions. Our framework involves three key designs. First, we introduce a hierarchical perturbation strategy to construct spatial and temporal non-preferred samples at both global and local granularities automatically. Second, we propose a self-guiding mechanism that leverages decoder cross-attention scores to identify and perturb semantically salient skeletal regions, forcing the model to distinguish genuine sign signals from structural distortions. Third, we establish an automated language-level preference generator by fine-tuning a dedicated perturbation model, capturing complex output-level failure modes without manual annotation. Extensive experiments on three widely adopted benchmarks, CSL-Daily, How2Sign, and OpenASL, demonstrate that SignDPO consistently outperforms state-of-the-art gloss-free methods and even rivals established gloss-based ones. Our results suggest that multi-level preference alignment is a powerful paradigm for bridging the gap between high-entropy skeletal trajectories and discrete linguistic semantics.

## TL;DR

SignDPO consistently outperforms state-of-the-art gloss-free methods and even rivals established gloss-based ones, and suggests that multi-level preference alignment is a powerful paradigm for bridging the gap between high-entropy skeletal trajectories and discrete linguistic semantics.

## BibTeX

```bibtex
@Inproceedings{Pu2026SignDPOMD,
 author = {Muxin Pu and Xiao-Ming Wu and Mei Kuan Lim and Chun Yong Chong and Wei Li and Chen Change Loy},
 title = {SignDPO: Multi-level Direct Preference Optimisation for Skeleton-based Gloss-free Sign Language Translation},
 year = {2026}
}
```

## Sources

- title: semanticscholar
- abstract: semanticscholar
- authors: semanticscholar
- topics: semanticscholar
- references: none
- citations: none
- fullText: none
- bibtex: semanticscholar

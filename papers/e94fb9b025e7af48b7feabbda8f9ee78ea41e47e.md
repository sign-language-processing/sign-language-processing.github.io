---
semanticScholarId: "e94fb9b025e7af48b7feabbda8f9ee78ea41e47e"
bibKey: null
year: 2024
title: "SKIM: Skeleton-Based Isolated Sign Language Recognition With Part Mixing"
doi: "10.1109/TMM.2023.3321502"
arxivId: null
isSignLanguage: true
expanded: true
topics: ["Computer Science"]
fullText: "none"
fullTextSource: "none"
bibtexSource: "semanticscholar"
sources:
  title: semanticscholar
  abstract: semanticscholar
  authors: semanticscholar
  topics: semanticscholar
  references: semanticscholar
  citations: semanticscholar
  fullText: none
  bibtex: semanticscholar
---

# SKIM: Skeleton-Based Isolated Sign Language Recognition With Part Mixing

**Year:** [[2024]]
**Topics:** [[topics/computer-science|Computer Science]]
**Authors:** Kezhou Lin; Xiaohan Wang; Linchao Zhu; Bang Zhang; Yi Yang

## Links
- [Semantic Scholar](https://www.semanticscholar.org/paper/e94fb9b025e7af48b7feabbda8f9ee78ea41e47e)
- [DOI](https://doi.org/10.1109/TMM.2023.3321502)

## Abstract

In this article, we present skeleton-based isolated sign language recognition (IsoSLR) with part mixing - SKIM. An IsoSLR model that solely takes the skeleton representation of the human body as input. Previous skeleton-based works either perform worse when compared to RGB-based counterparts or require fusion with other modalities to obtain competitive results. With SKIM, a single skeleton-based model without complex pre-training can obtain similar or even higher accuracy than current state-of-the-art methods. This margin can be further increased by simple late fusion within the same modality. To achieve this, we first develop a novel data augmentation technique called part mixing. It swaps the corresponding keypoints within one region (e.g. hand) between two randomly selected samples and combines their labels linearly as the new label. As regions like hand and face are key articulators for sign language, direct swapping of such parts creates a believable pseudo sign that promotes the model to recognize the true pairs. Secondly, following current advances in skeleton-based action recognition, we devise a channel-wise graph neural network with multi-scale awareness and per-keypoint temporal re-weighting. With this design, the backbone is capable of leveraging both manual and non-manual features. The combination of hand mixing and the channel-wise multi-scale GCN backbone allows us to achieve state-of-the-art accuracy on both WLASL and NMFs-CSL benchmarks.

## BibTeX

```bibtex
@Article{Lin2024SKIMSI,
 author = {Kezhou Lin and Xiaohan Wang and Linchao Zhu and Bang Zhang and Yi Yang},
 booktitle = {IEEE transactions on multimedia},
 journal = {IEEE Transactions on Multimedia},
 pages = {4271-4280},
 title = {SKIM: Skeleton-Based Isolated Sign Language Recognition With Part Mixing},
 volume = {26},
 year = {2024}
}
```

## Cited by

- [[2e4be777e2f6363163971a4793bd8365bd78fd9d]] — Machine learning in sign language: A comprehensive analysis and trend survey (2026)
- [[2b32a45281d91d6117287898191e170aa50d4800]] — An overview of sign language processing from natural language processing perspective (2026)
- [[67247734884438c96c4d54d55c24e15bf4fd0d4d]] — Motion-temporal calibration network for continuous sign language recognition (2025)
- [[36e6dc7d50d396e2f7aef5c584228fdcefde9020]] — A Multimodal Video and Radar Fusion Framework for High-Accuracy Isolated Sign Language Recognition (2025)
- [[3f1ca0bc7590e9bbeb3ac1ee428c41b389da270c]] — SegSLR: Promptable Video Segmentation for Isolated Sign Language Recognition (2025)
- [[32dcca67aa77fd57db31869fe8a52cccd411e41e]] — Generative Sign-Description Prompts with Multi-Positive Contrastive Learning for Sign Language Recognition (2025)
- [[dc491b7a7c6513f04e553b99ac5a09f820038071]] — Stack Transformer-Based Spatial-Temporal Attention Model for Dynamic Sign Language and Fingerspelling Recognition (2025)
- [[cca72230379ed82ba6435a55432632e986a64310]] — An effective skeleton-based approach for multilingual sign language recognition (2025)
- [[8189696b406b424a9dbdbc414c5977cac3670f6c]] — ExpAvatar: High-Fidelity Avatar Generation of Unseen Expressions with 3D Face Priors (2024)
- [[8247c7a67e4e3e526cee10ca9499b1936204e79c]] — Scaling up Multimodal Pre-Training for Sign Language Understanding (2024)
- [[c0647f641de652c3114c844b70c88204a81c96be]] — SML: A Skeleton-based multi-feature learning method for sign language recognition (2024)
- [[1678e53f71423ce5822ce832690ee0a4ac7623c6]] — Enhancing Brazilian Sign Language Recognition Through Skeleton Image Representation (2024)
- [[4748944a2feac0c5b032b5d6733cf90600f43b3b]] — EvCSLR: Event-Guided Continuous Sign Language Recognition and Benchmark (2025)
- [[d686bf28db6bebb60bd7e5d09f8f10c07f812761]] — Stack Transformer Based Spatial-Temporal Attention Model for Dynamic Multi-Culture Sign Language Recognition (2025)
- [[a2d9c056821907fc003dd6cea72e8ea17b8bf377]] — Advancements and challenges in vision-based sign language recognition: A comprehensive review ()

## Sources

- title: semanticscholar
- abstract: semanticscholar
- authors: semanticscholar
- topics: semanticscholar
- references: semanticscholar
- citations: semanticscholar
- fullText: none
- bibtex: semanticscholar

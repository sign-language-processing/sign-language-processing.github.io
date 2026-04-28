---
semanticScholarId: "ad9d96b2871afed5c016f6da95da8cbb55e12bcd"
bibKey: "segmentation:bull2021aligning"
year: 2021
title: "Aligning Subtitles in Sign Language Videos"
doi: "10.1109/ICCV48922.2021.01135"
arxivId: "2105.02877"
isSignLanguage: true
expanded: true
topics: ["Computer Science", "Linguistics"]
fullText: "none"
fullTextSource: "none"
bibtexSource: "ours"
sources:
  title: semanticscholar
  abstract: semanticscholar
  authors: semanticscholar
  topics: semanticscholar
  references: semanticscholar
  citations: semanticscholar
  fullText: none
  bibtex: ours
---

# Aligning Subtitles in Sign Language Videos

**Year:** [[2021]]
**Topics:** [[topics/computer-science|Computer Science]], [[topics/linguistics|Linguistics]]
**Authors:** Hannah Bull; Triantafyllos Afouras; Gül Varol; Samuel Albanie; Liliane Momeni; Andrew Zisserman

## Links
- [Semantic Scholar](https://www.semanticscholar.org/paper/ad9d96b2871afed5c016f6da95da8cbb55e12bcd)
- [PDF](https://arxiv.org/pdf/2105.02877)
- [arXiv:2105.02877](https://arxiv.org/abs/2105.02877)
- [DOI](https://doi.org/10.1109/ICCV48922.2021.01135)

## Abstract

The goal of this work is to temporally align asynchronous subtitles in sign language videos. In particular, we focus on sign-language interpreted TV broadcast data comprising (i) a video of continuous signing, and (ii) subtitles corresponding to the audio content. Previous work exploiting such weakly-aligned data only considered finding keyword-sign correspondences, whereas we aim to localise a complete subtitle text in continuous signing. We propose a Transformer architecture tailored for this task, which we train on manually annotated alignments covering over 15K subtitles that span 17.7 hours of video. We use BERT subtitle embeddings and CNN video representations learned for sign recognition to encode the two signals, which interact through a series of attention layers. Our model outputs frame-level predictions, i.e., for each video frame, whether it belongs to the queried subtitle or not. Through extensive evaluations, we show substantial improvements over existing alignment baselines that do not make use of subtitle text embeddings for learning. Our automatic alignment model opens up possibilities for advancing machine translation of sign languages via providing continuously synchronized video-text data.

## TL;DR

This work proposes a Transformer architecture tailored for this task, which trains on manually annotated alignments covering over 15K subtitles that span 17.7 hours of video, and opens up possibilities for advancing machine translation of sign languages via providing continuously synchronized video-text data.

## BibTeX

```bibtex
@inproceedings{segmentation:bull2021aligning,
 author = {Hannah Bull and
Triantafyllos Afouras and
G{\"{u}}l Varol and
Samuel Albanie and
Liliane Momeni and
Andrew Zisserman},
 bibsource = {dblp computer science bibliography, https://dblp.org},
 biburl = {https://dblp.org/rec/conf/iccv/BullAVAMZ21.bib},
 booktitle = {2021 {IEEE/CVF} International Conference on Computer Vision, {ICCV}
2021, Montreal, QC, Canada, October 10-17, 2021},
 doi = {10.1109/ICCV48922.2021.01135},
 pages = {11532--11541},
 publisher = {{IEEE}},
 timestamp = {Fri, 11 Mar 2022 00:00:00 +0100},
 title = {Aligning Subtitles in Sign Language Videos},
 url = {https://doi.org/10.1109/ICCV48922.2021.01135},
 year = {2021}
}
```

## References

- [[95c466170f60cc5a652b51ec23814320666a4f73]] — Read and Attend: Temporal Localisation in Sign Language Videos (2021)
- [[16091f0821502b70294ef66671183dadd1afcdc0]] — TSPNet: Hierarchical Feature Learning via Temporal Semantic Pyramid for Sign Language Translation (2020)
- [[631bbcce16387e76e4780d7c84b07b2a37d6bfc4]] — Watch, read and lookup: learning to spot signs from multiple supervisors (2020)
- [[5b8ec500aedc97cc9874a9eb601cef37c5f38e3f]] — Quantitative Survey of the State of the Art in Sign Language Recognition (2020)
- [[7eda262bf812d0293dca67f34ef47ce53a3b268b]] — Real-Time Sign Language Detection using Human Pose Estimation (2020)
- [[6af09da568edee80075ec610f431ffa91bfce061]] — Fully Convolutional Networks for Continuous Sign Language Recognition (2020)
- [[fe6c2b21f6086c375f4e211efb6c4d6479d54f01]] — BSL-1K: Scaling up co-articulated sign language recognition using mouthing cues (2020)
- [[3e86f5a0e2a97894de1cf1f1587799ac79bad0f2]] — VirTex: Learning Visual Representations from Textual Annotations (2020)
- [[962dc29fdc3fbdc5930a10aba114050b82fe5a3e]] — End-to-End Object Detection with Transformers (2020)
- [[5b7c24632850b55b17edf3d231ed1ed8f8ec1227]] — Use Cases for a Sign Language Concordancer (2020)
- [[355403d7ce4b625307fd3ebb2beea269ecc15213]] — Dense Regression Network for Video Grounding (2020)
- [[05dcdfece56d1869895f53ed581d8ad64118c05f]] — Sign Language Transformers: Joint End-to-End Sign Language Recognition and Translation (2020)
- [[efe28238909dc5c1877297fa830d85e9daecc29f]] — Transferring Cross-Domain Knowledge for Video Sign Language Recognition (2020)
- [[9de403a58395a1b56bfceee6e009788c43db6d08]] — End-to-End Learning of Visual Representations From Uncurated Instructional Videos (2019)
- [[c7fd5973a2cb3f7c6a5df0120400bc47b2f2bacf]] — Sign Language Recognition, Generation, and Translation: An Interdisciplinary Perspective (2019)
- [[0fa68cde4db12779adacb70a24961cf09b1adf73]] — Language-Driven Temporal Activity Localization: A Semantic Matching Reinforcement Learning Model (2019)
- [[c1e90a921638e28a5209c854dd82e19d6b78984f]] — Learning Motion Disfluencies for Automatic Sign Language Segmentation (2019)
- [[1fdec39d5a8d207db36a181dbe7312713d1a08e4]] — Sign Language Detection “in the Wild” with Recurrent Neural Networks (2019)
- [[1806156853a6c95725c16283fb0c5ccf954c24d4]] — The VIA Annotation Software for Images, Audio and Video (2019)
- [[ddf69a6ef015a1b0668ca48a486c4cc7e22a7d9c]] — ExCL: Extractive Clip Localization Using Natural Language Descriptions (2019)
- [[6fd7e8aa1a031923e3580752e4ab9163e45fe41c]] — Read, Watch, and Move: Reinforcement Learning for Temporally Grounding Natural Language Descriptions in Videos (2019)
- [[519da94369c1d87e09c592f239b55cc9486b5b7c]] — Attentive Moment Retrieval in Videos (2018)
- [[644602c65a5d8f30e62be027eb7b47f7c335191a]] — Neural Sign Language Translation (2018)
- [[31bb920739f22b4865161f75692785decfea470c]] — To Find Where You Talk: Temporal Sentence Localization in Video with Attention Based Location Regression (2018)
- [[83b2a55aecd5f917dbedbc0c5ef3ff3b61013958]] — Multilevel Language and Vision Integration for Text-to-Clip Retrieval (2018)
- [[a274fcf985aaec1f009cfe4b4042733321a5a8b4]] — Video-based Sign Language Recognition without Temporal Segmentation (2018)
- [[efeaa6e3114d6d6ae5c3041b66ac9a9ae9bf52bf]] — Spatial Temporal Graph Convolutional Networks for Skeleton-Based Action Recognition (2018)
- [[c769c84174b7a6b2f1083aa5bcf5ef45e8e527f4]] — Speed-Accuracy Tradeoffs for Detecting Sign Language Content in Video Sharing Sites (2017)
- [[a10cd29fec9dca66250dbde19db5e831f7ce6406]] — SubUNets: End-to-End Hand Shape and Continuous Sign Language Recognition (2017)
- [[ee909ad489244016cf301bb7d7d8eeea423dbf35]] — Localizing Moments in Video with Natural Language (2017)
- [[28b85543e8f12c3d2d2227dcc9f5e87c685535ea]] — Re-Sign: Re-Aligned End-to-End Sequence Modelling with Deep Recurrent CNN-HMMs (2017)
- [[204e3073870fae3d05bcbc2f6a8e263d9b72e776]] — Attention is All you Need (2017)
- [[b61a3f8b80bbd44f24544dc915f52fd30bbdf485]] — Quo Vadis, Action Recognition? A New Model and the Kinetics Dataset (2017)
- [[e9bd6f0b04a0ddf9fcdf3a5fd1cfe87f8ae9cfff]] — TALL: Temporal Activity Localization via Language Query (2017)
- [[31b4f2a9fcd8e45a5b4f4cf95e3caa8b460c062f]] — Deep Sign: Hybrid CNN-HMM for Continuous Sign Language Recognition (2016)
- [[45ca387a4080b6aee610783ed03d19bd1891503f]] — Book2Movie: Aligning video scenes with book chapters (2015)
- [[59ac98f3910dad473e7771ac61f796a038f1708f]] — Weakly-Supervised Alignment of Video with Text (2015)
- [[854cda845e5bfe503b9fc0ad9eb825ac9bb9dc7b]] — Sign Spotting Using Hierarchical Sequential Patterns with Temporal Intervals (2014)
- [[94970df71f6bedce1d13d7511ed826afbfc86a9f]] — Motion history images for online speaker/signer diarization (2014)
- [[2be23a56281ec69f7132e65beaac4e6690560ac4]] — Story-based Video Retrieval in TV series using Plot Synopses (2014)
- [[87f40e6f3022adbc1f1905e3e506abad05a9964f]] — Distributed Representations of Words and Phrases and their Compositionality (2013)
- [[890614f30de4d2e651b66858e871ea5fe2f1d98a]] — Building the British Sign Language Corpus (2013)
- [[e8cb43b02e82a675ba7034f13b2540ab21514c51]] — Automatic Signer Diarization - The Mover Is the Signer Approach (2013)
- [[103a1c2402bfb59a8ad097787afb1b786c94211c]] — Seeing sentence boundaries: the production and perception of visual markers signalling boundaries in signed languages (2010)
- [[1f7a832b564b40e4d05f87abcb161801c5dd868b]] — Automatic sign segmentation from continuous signing via multiple sequence alignment (2009)
- [[b7a23574e6eda8ad49e43d71b931285bf39fc9ac]] — Sign Language Spotting with a Threshold Model Based on Conditional Random Fields (2009)
- [[46b658f9e291b1ff1684aa9f778c31ed1c92a23a]] — Learning signs from subtitles: A weakly supervised approach to sign language recognition (2009)
- [[34b7e826db49a16773e8747bc8dfa48e344e425d]] — Learning sign language by watching TV (using weakly aligned subtitles) (2009)
- [[54dbc40d46bb130a19d81861f02efc8b6e32fba0]] — Activity detection in conversational sign language video for mobile telecommunication (2008)
- [[0ad33002437a6fd00fb746774bd7b11e0b2181d3]] — Detecting Coarticulation in Sign Language using Conditional Random Fields (2006)
- [[6957ecc299b76faaef1dc2c833a0f76ab76eb35e]] — Aligning ASL for Statistical Translation Using a Discriminative Word Model (2006)
- [[205e785d4cbffd03b6645f721408ca72a6119550]] — The Linguistics of British Sign Language: An Introduction (1999)
- [[8ed3062e50ed95acdf934399174ddaa83942fd7d]] — A real-time continuous gesture recognition system for sign language (1998)
- [[1432bda965619e532630cc95555c0f8fcb2e3c0c]] — A comparative study of several dynamic time-warping algorithms for connected-word recognition (1981)
- [[a6ee85e09c497b092e8db0756633a75fb8017d9d]] — SIGNER DIARISATION IN THE WILD (2021)
- Sign segmentation with temporal convolutional networks (2021)
- [[ad906acdeb50ef1edc9d31e205b092e3e7a0a982]] — Automatic Segmentation of Sign Language into Subtitle-Units (2020)
- [[df2b0e26d0599ce3e70df8a9da02e51594e0e992]] — BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding (2019)
- [[452aca244ef62a533d8b46a54c6212fe9fa3ce9a]] — Temporally Grounding Natural Sentence in Video (2018)
- [[a65efb9bbbbcd849a3bd4770fa66c669a58489f2]] — 2 Movie : Aligning Video scenes with Book chapters (2015)
- [[31ab5dafb152d8b386f015db3396202ba186234e]] — British Sign Language Corpus Project: A corpus of digital video data and annotations of British Sign Language 2008-2014 (2014)
- [[140b6f1132cfd34e409a286e921fabacff3783f3]] — Large-scale Learning of Sign Language by Watching TV (Using Co-occurrences) (2013)
- [[5a4828b273979b4b03dde6b0a23d18c08c80b9a7]] — Employing signed TV broadcasts for automated learning of British Sign Language (2010)
- [[6166950a0f4d33812ed6c5e48d951cf370c4e74c]] — Subtitle-free Movie to Script Alignment (2009)
- [[a4aba56927d7841c0aaedf5c73d42ccfadd75124]] — Hello! My name is... Buffy'' -- Automatic Naming of Characters in TV Video (2006)
- Satyakiran Duggina, Caio D. D. Monteiro, and 11 ()

## Cited by

- [[aac5bc270b3d32beafea1ca71c05208b8a4b9169]] — SignSparK: Efficient Multilingual Sign Language Production via Sparse Keyframe Learning (2026)
- [[1dc9cc2ee2db8c746fa3bf08684a52a9f024cf36]] — Mobile Auslan: A multimodal dialogue-centered sign language learning system (2026)
- [[70a05d43c1ce1ed571cf047fcc07f2b60ac6ffde]] — Attend to what I say: Highlighting relevant content on slides (2026)
- [[97f68acfae2157810ca22af735b24b8f6c59cab1]] — Segment, Embed, and Align: A Universal Recipe for Aligning Subtitles to Signing (2025)
- [[8b440fd23f5533afd77de1bab2c8f8d1f2337339]] — Lost in Translation, Found in Embeddings: Sign Language Translation and Alignment (2025)
- [[6c48c6a183d4eb15a99f4f5cd638ad6b89d4f687]] — Sentence-level Segmentation for Long Sign Language Videos with Captions (2025)
- [[81292097d38b5d6622d606f4965806313e296d0d]] — The TUB Sign Language Corpus Collection (2025)
- [[416e62a0551affacd2d0617997d2586ee8062152]] — iLSU-T: an Open Dataset for Uruguayan Sign Language Translation (2025)
- [[a397b7dd49c46827b672c08a6232283824e8232c]] — "I have never seen that for Deaf people's content:" Deaf and Hard-of-Hearing User Experiences with Misinformation, Moderation, and Debunking on Social Media in the US (2025)
- [[71725607eafedb512af4ebf96312de21716517bd]] — AuslanWeb: A Scalable Web-Based Australian Sign Language Communication System for Deaf and Hearing Individuals (2025)
- [[5cce2ec66f72d4d6ecdc1c159de36d9438613f70]] — Hands-On: Segmenting Individual Signs from Continuous Sequences (2025)
- [[8c9d433641caa5bd7e43776db0b0faf4d12a0145]] — Deep Understanding of Sign Language for Sign to Subtitle Alignment (2025)
- [[579ddc45b1d3cc849323da23f358b832788e71a5]] — Lost in Translation, Found in Context: Sign Language Translation with Contextual Cues (2025)
- [[f5ce1659fb518c22e9e2cc7f18e6663995a43e21]] — Diverse Sign Language Translation (2024)
- [[647391b7b5d9eacd8e69ab1304317f41258cf69a]] — Visual Timing For Sound Source Depth Estimation in the Wild (2024)
- [[7b1aa58f46d46c6bf76e4f52d73836c0067b5c5e]] — Transformer with Controlled Attention for Synchronous Motion Captioning (2024)
- [[236636d77a95b1dda141cb4c4df73e96e44c2e13]] — FLEURS-ASL: Including American Sign Language in Massively Multilingual Multitask Evaluation (2024)
- [[42f6e42c063cfbea408c4f874c0464e0e8e9f7de]] — Building a Compassionate GenAI-integrated ASL Translator for YouTube Video (2024)
- [[13195df56368306dc1c1f9733cebb8dd694c94af]] — A Tale of Two Languages: Large-Vocabulary Continuous Sign Language Recognition from Spoken Language Supervision (2024)
- [[b664b52b16adb8321314990b0cb1d4d1c4cb12e1]] — E-TSL: A Continuous Educational Turkish Sign Language Dataset with Baseline Methods (2024)
- [[869cf45c0c77db3f513e11770f33375c43c6d86a]] — Matignon-LSF: a Large Corpus of Interpreted French Sign Language (2024)
- [[4acc7aa0e90905ed244f196453514eb70b80db94]] — Linguistically Motivated Sign Language Segmentation (2023)
- [[b9236db92a9637507cb7ec00a8b1d8f44333f4ec]] — Motion2language, unsupervised learning of synchronized semantic motion segmentation (2023)
- [[35d66417916c83ce4c841b344188a6847930e939]] — Best practices for sign language technology research (2023)
- [[fbbcef51fa1f9a1bd344495d908ea4e3e3f04937]] — Gloss Alignment using Word Embeddings (2023)
- [[37d445fc4bd873541e7d086968372e4516bbece0]] — Weakly-supervised Fingerspelling Recognition in British Sign Language Videos (2022)
- [[0d02a59e596bac46447b7b405b10586afaff1cd8]] — DualSign: Semi-Supervised Sign Language Production with Balanced Multi-Modal Multi-Task Dual Transformation (2022)
- [[dd964ffeb47efb9a3691b5d233e02284ee8228a7]] — Automatic dense annotation of large-vocabulary sign language videos (2022)
- [[622428f5122ad12a40229e1768ecb929fd747ee7]] — Multimodal Learning With Transformers: A Survey (2022)
- [[be54fc78e86fb3e65964fbfb904f22eb9927502f]] — Open-Domain Sign Language Translation Learned from Online Video (2022)
- [[3826b47d3e8a7ef99d8c757c778e7d11633df84e]] — BBC-Oxford British Sign Language Dataset (2021)
- [[e791ab125e0ed8c74ad3cd056d7a3537b2c90ac2]] — Visual Keyword Spotting with Attention (2021)
- [[d7b932bbf002dd9bf44173b5a96d800805a80f7c]] — Mediapi-RGB: Enabling Technological Breakthroughs in French Sign Language (LSF) Research Through an Extensive Video-Text Corpus (2024)
- [[004e899e779d5f27e2b3ae19533272d68a3769e3]] — Auslan-Daily: Australian Sign Language Translation for Daily Communication and News (2023)
- [[cc9241a2922ac85173ad60db04f3e151c5bfdc46]] — Automatic Gloss Dictionary for Sign Language Learners (2022)
- [[4fe29c38a52bf6fa7057c8043ae76bda45c0f713]] — A Machine Learning-based Segmentation Approach for Measuring Similarity between Sign Languages (2022)
- [[bce54ad9184fec6b5ad3787855ebf94ca1f0af64]] — PeruSIL: A Framework to Build a Continuous Peruvian Sign Language Interpretation Dataset (2022)
- [[11e431924bbb22389b69a1032c24f232e8a75650]] — Deep Learning and Knowledge Integration for Music Audio Analysis (Dagstuhl Seminar 22082) (2022)
- [[3c95b06cd3b6fe177b52162e125d82abfec4b538]] — The Effectiveness of Sign Language in Media Accessibility: Bridging the Communication Gap for the Hearing Impaired (2025)

## Sources

- title: semanticscholar
- abstract: semanticscholar
- authors: semanticscholar
- topics: semanticscholar
- references: semanticscholar
- citations: semanticscholar
- fullText: none
- bibtex: ours

---
semanticScholarId: "b0beae60ee3865d5dc6071bccdfe2bff7bdfe8aa"
bibKey: null
year: 2025
title: "Contrastive Pretraining with Dual Visual Encoders for Gloss-Free Sign Language Translation"
doi: "10.1145/3742886.3756703"
arxivId: "2507.10306"
isSignLanguage: true
expanded: true
topics: ["Computer Science", "Linguistics"]
fullText: "extracted"
fullTextSource: "ar5iv"
bibtexSource: "semanticscholar"
sources:
  title: semanticscholar
  abstract: semanticscholar
  authors: semanticscholar
  topics: semanticscholar
  references: semanticscholar
  citations: semanticscholar
  fullText: ar5iv
  bibtex: semanticscholar
---

# Contrastive Pretraining with Dual Visual Encoders for Gloss-Free Sign Language Translation

**Year:** [[2025]]
**Topics:** [[topics/computer-science|Computer Science]], [[topics/linguistics|Linguistics]]
**Authors:** Ozge Mercanoglu Sincan; Richard Bowden

## Links
- [Semantic Scholar](https://www.semanticscholar.org/paper/b0beae60ee3865d5dc6071bccdfe2bff7bdfe8aa)
- [arXiv:2507.10306](https://arxiv.org/abs/2507.10306)
- [DOI](https://doi.org/10.1145/3742886.3756703)

## Abstract

Sign Language Translation (SLT) aims to convert sign language videos into spoken or written text. While early systems relied on gloss annotations as an intermediate supervision, such annotations are costly to obtain and often fail to capture the full complexity of continuous signing. In this work, we propose a two-phase, dual visual encoder framework for gloss-free SLT, leveraging contrastive visual–language pretraining. During pretraining, our approach employs two complementary visual backbones whose outputs are jointly aligned with each other and with sentence-level text embeddings via a contrastive objective. During the downstream SLT task, we fuse the visual features and input them into an encoder–decoder model. On the Phoenix-2014T benchmark, our dual encoder architecture consistently outperforms its single-stream variants and achieves the highest BLEU-4 score among existing gloss-free SLT approaches.

## TL;DR

A two-phase, dual visual encoder framework for gloss-free SLT, leveraging contrastive visual–language pretraining, which consistently outperforms its single-stream variants and achieves the highest BLEU-4 score among existing gloss-free SLT approaches.

## BibTeX

```bibtex
@Article{Sincan2025ContrastivePW,
 author = {Ozge Mercanoglu Sincan and Richard Bowden},
 booktitle = {International Conference on Intelligent Virtual Agents},
 journal = {Adjunct Proceedings of the 25th ACM International Conference on Intelligent Virtual Agents},
 title = {Contrastive Pretraining with Dual Visual Encoders for Gloss-Free Sign Language Translation},
 year = {2025}
}
```

## Full Text

# Contrastive Pretraining with Dual Visual Encoders for Gloss-Free Sign Language Translation

Ozge Mercanoglu Sincan [o.mercanoglusincan@surrey.ac.uk](mailto:o.mercanoglusincan@surrey.ac.uk) CVSSP, University of Surrey Guildford UK and Richard Bowden [r.bowden@surrey.ac.uk](mailto:r.bowden@surrey.ac.uk) CVSSP, University of Surrey Guildford UK

(2025)

###### Abstract.

Sign Language Translation (SLT) aims to convert sign language videos into spoken or written text. While early systems relied on gloss annotations as an intermediate supervision, such annotations are costly to obtain and often fail to capture the full complexity of continuous signing. In this work, we propose a two-phase, dual visual encoder framework for gloss-free SLT, leveraging contrastive visual-language pretraining. During pretraining, our approach employs two complementary visual backbones whose outputs are jointly aligned with each other and with sentence-level text embeddings via a contrastive objective. During the downstream SLT task, we fuse the visual features and input them into an encoder-decoder model. On the Phoenix-2014T benchmark, our dual encoder architecture consistently outperforms its single-stream variants and achieves the highest BLEU-4 score among existing gloss-free SLT approaches.

Sign Language Translation, Gloss-free SLT, Contrastive Learning, Multimodal Pretraining

† † copyright: acmlicensed † † journalyear: 2025 † † doi: XXXXXXX.XXXXXXX † † conference: ACM International Conference on Intelligent Virtual Agents (IVA'25); Sept 16-19,2025; Berlin, Germany † † isbn: 978-1-4503-XXXX-X/2018/06 † † ccs: Human-centered computing Accessibility technologies

## 1. Introduction

Sign languages are visual languages that rely on both manual (handshape, orientation, movement) and non-manual (facial expressions, head and body posture) components. These components operate simultaneously and often encode grammatical information in parallel channels. With over 200 sign languages in the world (wfd, [2025](#bib.bib2) ) , the development of inclusive technologies to support sign language understanding has become an increasingly important research domain.

Sign Language Translation (SLT) aims to convert sign language videos into spoken or written text. Achieving this requires the models to capture both fine-grained spatial detail (e.g., specific handshapes and finger configurations), temporal dynamics (e.g., motion trajectories). These visual features are then transformed into coherent natural language output. Works in this domain have predominantly relied on sequential models, such as Recurrent Neural Networks (RNNs) or the Transformer (Vaswani, [2017](#bib.bib34) ) , to map sign language video sequences to spoken language sentences (Camgoz et al., [2018](#bib.bib4) , [2020](#bib.bib5) ; Sincan et al., [2023](#bib.bib31) ; Yao et al., [2023](#bib.bib37) ; Zhang et al., [2022](#bib.bib39) ) . Earlier studies relied on intermediate annotations called glosses - simplified written descriptions of individual signs - to act as a bridge between visual and linguistic domains (Camgoz et al., [2018](#bib.bib4) , [2020](#bib.bib5) ; Zhang et al., [2022](#bib.bib39) ) . However, manual annotation of glosses is labor-intensive and difficult to annotate accurately, resulting in a limited number of publicly available gloss-annotated datasets (Konrad et al., [2020](#bib.bib16) ) .

To overcome this limitation, gloss-free SLT methods have been proposed, aiming to directly translate sign language videos into spoken language without relying on gloss supervision (Chen et al., [2024](#bib.bib9) ; Gong et al., [2024](#bib.bib12) ; Ye et al., [2024](#bib.bib38) ; Zhou et al., [2023](#bib.bib40) ) . This shift removes the dependence on expert gloss annotations but brings challenges in learning rich, discriminative representations of signing sequences. Typical architectures use a frozen visual encoder backbone, such as 3D Convolutional Neural Networks, e.g., I3D (Carreira and Zisserman, [2017](#bib.bib6) ) , to extract features, and pass them into transformers (Albanie et al., [2021](#bib.bib3) ; Shi et al., [2022b](#bib.bib30) ; Sincan et al., [2023](#bib.bib31) ) . However, these models often lack a strong semantic bridge between visual and linguistic modalities, limiting their ability to generate semantically accurate translations.

Recent advancements in gloss-free SLT have drawn inspiration from visual-language pretraining methods (Zhou et al., [2023](#bib.bib40) ; Ye et al., [2024](#bib.bib38) ; Chen et al., [2024](#bib.bib9) ; Wong et al., [2024](#bib.bib35) ) . Approaches such as GFSLT-VLP (Zhou et al., [2023](#bib.bib40) ) pioneered the use of contrastive learning to align visual representations with textual descriptions. These methods offer a promising direction to improve the semantic grounding of visual features and provide more flexible and scalable training paradigms for SLT.

In this work, we propose a dual visual encoder framework for gloss-free SLT. We employ two complementary visual backbones: a ResNet (He et al., [2016](#bib.bib14) ) to extract fine-grained spatial features from individual frames, and an I3D (Carreira and Zisserman, [2017](#bib.bib6) ) to capture spatio-temporal features. During our pretraining stage, both feature sets are projected into a shared embedding space and aligned via a contrastive loss against corresponding sentence embeddings extracted by a pretrained language model. We additionally include an inter-modal alignment that encourages the ResNet and I3D features from the same video to be similar while pushing apart features from different video samples. After pretraining, we fine-tune a translation model for translation by fusing visual features and feeding them into an mBART-based encoder-decoder architecture. We evaluate our approach on the Phoenix-2014T dataset (Camgoz et al., [2018](#bib.bib4) ) and demonstrate significant improvements over our single-encoder baselines. We outperform existing gloss-free SLT methods on the BLEU-4 metric, while obtaining competitive results on other evaluation metrics.

- • We introduce a contrastively pretrained dual visual encoder architecture that jointly aligns both visual modalities with each other and with language. This alignment encourages the model to learn complementary representations and enhance semantic consistency.
- • We explore and compare various fusion strategies for combining visual features.

## 2. Related Work

Recent research at the intersection of vision and language has led to rapid advances in many tasks, including sign language translation. In this section, we review works on visual-language pretraining and sign language translation.

### 2.1. Visual-Language Pretraining

Contrastive pretraining between vision and language has become fundamental for many downstream tasks. A pioneering work in this field, CLIP (Contrastive Language-Image Pre-training) (Radford et al., [2021](#bib.bib26) ) aligns image features with text representations using a contrastive learning strategy. CLIP does not need task-specific training data, and it demonstrates an ability to generalize across a wide range of downstream tasks such as zero-shot transfer to image classification, facial emotion recognition, optical character recognition, and so on. VideoCLIP (Xu et al., [2021](#bib.bib36) ) extends this contrastive learning objective to pre-train a unified video-text representation that surpasses prior works in video understanding tasks such as text-video retrieval, video question answering, and action segmentation.

Several extensions have adapted this idea for additional modalities. CLIP4VLA (Ruan et al., [2023](#bib.bib27) ) extends CLIP by incorporating audio as a third modality, forming a unified tri-encoder structure for multimodal learning. IMAGEBIND (Girdhar et al., [2023](#bib.bib11) ) scales this idea further by binding six modalities (e.g., image, text, video, audio, depth, and thermal) - using images as a key modality, and aligning each modality to image embeddings. More recently, LANGUAGEBIND (Zhu et al., [2024](#bib.bib42) ) proposes a language-based multi-modal pretraining, taking the language as the bind across video, infrared, depth, and audio.

### 2.2. Sign Language Translation

Sign language translation presents unique challenges compared to other vision-language tasks due to its complexity. Early studies (Camgoz et al., [2018](#bib.bib4) , [2020](#bib.bib5) ; Chen et al., [2022b](#bib.bib8) ; Zhang et al., [2022](#bib.bib39) ; Chen et al., [2022a](#bib.bib7) ) decomposed the SLT task two sub-tasks: Sign Language Recognition (SLR), recognizing sequences of signs, and then 'translating' the recognized signs into spoken language sentences. These gloss-based pipelines benefit from structured intermediate supervision, enabling models to focus on smaller vocabularies and more discrete targets. However, gloss annotations are highly labor-intensive and not available for large datasets, motivating gloss-free SLT methods.

Gloss-free SLT approaches aim to directly translate sign language videos into spoken language without gloss annotation. Initial gloss-free efforts (Sign2Text) typically adopted end-to-end encoder-decoder frameworks using a visual encoder and transformer-based decoders (Camgoz et al., [2020](#bib.bib5) ) . While these architectures removed the need for glosses, their performance was often inferior to gloss-based counterparts, largely due to weaker semantic grounding between visual features and linguistic output.

To address this, several works have focused on enhancing visual representations. Some approaches (Shi et al., [2022a](#bib.bib29) ; Sincan et al., [2023](#bib.bib31) ) pretrain a classifier on sign language datasets and use it as a frozen visual encoder for the downstream SLT task. However, these approaches have a large semantic gap to solve between video features and text tokens. To address this, SignLLM (Gong et al., [2024](#bib.bib12) ) proposes a tokenization strategy, converting sign videos into a language-like format such as discrete character-level sign tokens and word-level sign representations. Then, they are passed to a large language model, LLaVA (Liu et al., [2023](#bib.bib18) ) .

In parallel, some works have focused on visual-language pretraining methods. GFSLT-VLP (Zhou et al., [2023](#bib.bib40) ) stands out as one of the first methods to leverage contrastive visual-language pretraining for gloss-free sign language translation, aligning visual features directly with textual representations. Building on this, SignCL (Ye et al., [2024](#bib.bib38) ) identified a representation density problem, where semantically distinct but visually similar signs tend to be close in the feature space, and proposed a contrastive learning strategy on adjacent frames to improve feature separation. Sign2GPT (Wong et al., [2024](#bib.bib35) ) proposes generating pseudo-glosses from spoken language descriptions during pretraining, offering an alternative to manual gloss annotations. Differently from these contrastive alignment methods, works such as FLa-LLM (Chen et al., [2024](#bib.bib9) ) and VAP (Jiao et al., [2025](#bib.bib15) ) incorporate a lightweight translation model in the pretraining stage. VAP employed a multi-stage pretraining, including pseudo-gloss-to-text translation, which may be considered as weakly supervised gloss-free method.

Our approach draws inspiration from multimodal contrastive frameworks but focuses on visual-textual alignment in the context of sign language. We leverage the complementary strengths of two different visual encoders while aligning them both with each other and with language representations. This multiple-alignment strategy enables the model to capture complementary visual information from different aspects of the sign language video, leading to improved translation performance.

## 3. Method

We propose a two-stage framework, namely DVE-SLT, for gloss-free sign language translation. Given a sign video V = ( I 1 , I 2 , I 3 , . . , I T ) V=(I\_{1},I\_{2},I\_{3},..,I\_{T}) with T T frames, the goal is to generate a spoken-language sentence S = ( w 1 , w 2 , . . , w U ) S=(w\_{1},w\_{2},..,w\_{U}) with U U words without relying on gloss annotations. Our architecture is illustrated in Fig. [1](#S3.F1) . In this section, we describe our pretraining strategy in which cross-modal and inter-modal alignment objectives are optimized through contrastive learning (Section [3.1](#S3.SS1) ), and the fine-tuning stage in which the fused visual features are decoded into spoken language (Section [3.2](#S3.SS2) ).

Figure 1. Overview of the proposed framework which has two phases: (a) pretraining, (b) translation. In pretraining, visual and textual representations are aligned utilizing contrastive alignment across modalities. The shared visual encoder, ℰ s  h  a  r  e  d \mathcal{E}\_{shared} , and Text Decoder weights are then utilized in the downstream SLT task. (c) Module structures, including the Temporal Encoder, VL Adapter, and Feature Aggregation are detailed.

<!-- image -->

### 3.1. Visual-Language Pretraining

Dual Visual Encoders. Visual feature extraction is a critical component for video understanding tasks, including SLT. In prior works, a variety of visual encoders have been explored to extract meaningful representations. Among these, ResNet (He et al., [2016](#bib.bib14) ) and I3D (Carreira and Zisserman, [2017](#bib.bib6) ) are frequently employed for sign language translation. ResNet-based models are commonly used for their efficiency and ability to capture fine-grained spatial features, by combining with temporal convolution layers to model temporal features (Chen et al., [2024](#bib.bib9) ; Ye et al., [2024](#bib.bib38) ; Zhou et al., [2023](#bib.bib40) ) . On the other hand, I3D, originally developed for action recognition, is designed to capture spatio-temporal features simultaneously. It achieved notable success in sign language recognition and translation tasks (Momeni et al., [2022](#bib.bib21) ; Shi et al., [2022a](#bib.bib29) ; Sincan et al., [2023](#bib.bib31) ) .

In this work, we adopt both spatial (ResNet18) and spatio-temporal (I3D) visual encoders to extract complementary visual features. The visual encoders are followed by identical Temporal Encoders, which are composed of two blocks of a 1D-convolutional layer, a batch normalization layer, ReLu activation, and max pooling, reducing the number of frames to T / 4 T/4 . Although I3D inherently models temporal dynamics, we apply the same temporal module to both branches to ensure consistent temporal resolution. Projecting the outputs of both branches into a unified embedding space is critical for contrastive alignment. Therefore, we employ a single shared transformer encoder, ℰ s  h  a  r  e  d \mathcal{E}\_{shared} , which processes both ResNet and I3D features using the same parameters. This promotes semantic consistency between modalities and enables joint optimization during pretraining.

Text Encoder and Decoder. We employ the pretrained multilingual mBART (Liu et al., [2020](#bib.bib19) ) encoder with 12 layers to convert spoken language sentences into text embeddings, which are aligned with visual features via contrastive learning.

In parallel, masked versions of the same sentences are fed into the text encoder and then passed to an mBART decoder with 3 layers, which is trained to reconstruct the original sentence using a standard cross-entropy loss. During the translation stage, this decoder is used to initialize the language decoder of our SLT model, enabling a smooth transition from pretraining to fine-tuning.

Contrastive Alignment Objectives. During pretraining, we apply a cross-modal contrastive loss to align video and text embeddings. In addition, we introduce an inter-modal contrastive loss that aligns the representations from two complementary visual encoders for the same video. This dual-objective setup encourages both visual-text alignment and consistency across visual modalities, reinforcing the semantic coherence of the learned representations.

Given a batch of N N video-text pairs, we extract visual features using our shared visual encoder and textual features using a pretrained mBART multilingual text encoder. Then, for each video-text pair, we compute a similarity matrix by adopting

Cross-Lingual Contrastive Learning (CiCO) (Cheng et al.,

[2023](#bib.bib10) ) , which was proposed for the sign language retrieval task. We use a symmetric InfoNCE loss (Gutmann and Hyvärinen, [2010](#bib.bib13) ) to contrast matching and mismatching pairs:

|     | ℒ  cross  =  \displaystyle\mathcal{L}\_{\text{cross}}=   | −  1  2  N  ∑  i  =  1  N  log  ⁡  exp  ⁡  (  S  i  m  (  Z  v  i  ,  Z  t  i  )  /  τ  )  ∑  j  =  1  N  exp  ⁡  (  S  i  m  (  Z  v  i  ,  Z  t  j  )  /  τ  )  \displaystyle-\frac{1}{2N}\sum\_{i=1}^{N}\log\frac{\exp(Sim(Z\_{v\_{i}},Z\_{t\_{i}})/\tau)}{\sum\_{j=1}^{N}\exp(Sim(Z\_{v\_{i}},Z\_{t\_{j}})/\tau)}   |                                                                                                                                                                                                                                                                                                                       |    |
|-----|----------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----|
| (1) |                                                          |                                                                                                                                                                                                                                                                                                                         | −  1  2  N  ∑  j  =  1  N  log  ⁡  exp  ⁡  (  S  i  m  (  Z  v  j  ,  Z  t  j  )  /  τ  )  ∑  i  =  1  N  exp  ⁡  (  S  i  m  (  Z  v  i  ,  Z  t  j  )  /  τ  )  \displaystyle-\frac{1}{2N}\sum\_{j=1}^{N}\log\frac{\exp(Sim(Z\_{v\_{j}},Z\_{t\_{j}})/\tau)}{\sum\_{i=1}^{N}\exp(Sim(Z\_{v\_{i}},Z\_{t\_{j}})/\tau)} |    |

where S  i  m  ( Z v i , Z t j ) Sim(Z\_{v\_{i}},Z\_{t\_{j}}) denotes the global similarity of the i t  h i^{th} video embedding and the j t  h j^{th} text embedding, resulting the similarity matrix 𝐌 ∈ ℝ N × N \mathbf{M}\in\mathbb{R}^{N\times N} computed over the batch, τ \tau is a trainable temperature parameter. The visual embedding Z v Z\_{v} is obtained from either the ResNet or I3D encoder.

In addition, since we employ two different visual encoders to extract complementary features from the same video, we introduce a second contrastive loss, inter-modal contrastive loss . It aims to pull together the embeddings from both branches for the same input, while pushing apart mismatched visual pairs. This objective encourages semantic alignment across encoders, reinforcing the consistency of dual visual representations. Similarly, we use the symmetric InfoNCE loss (Gutmann and Hyvärinen, [2010](#bib.bib13) ) but with the visual embeddings Z R  e  s Z\_{Res} and Z I  3  D Z\_{I3D} , extracted from the ResNet and I3D branches:

|     | ℒ  inter  =  \displaystyle\mathcal{L}\_{\text{inter}}=   | −  1  2  N  ∑  i  =  1  N  log  ⁡  exp  ⁡  (  S  i  m  (  Z  R  e  s  i  ,  Z  I  3  D  i  )  /  τ  )  ∑  j  =  1  N  exp  ⁡  (  S  i  m  (  Z  R  e  s  i  ,  Z  I  3  D  j  )  /  τ  )  \displaystyle-\frac{1}{2N}\sum\_{i=1}^{N}\log\frac{\exp(Sim(Z\_{Res\_{i}},Z\_{I3D\_{i}})/\tau)}{\sum\_{j=1}^{N}\exp(Sim(Z\_{Res\_{i}},Z\_{I3D\_{j}})/\tau)}   |                                                                                                                                                                                                                                                                                                                                                       |    |
|-----|----------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----|
| (2) |                                                          |                                                                                                                                                                                                                                                                                                                                                         | −  1  2  N  ∑  j  =  1  N  log  ⁡  exp  ⁡  (  S  i  m  (  Z  I  3  D  j  ,  Z  R  e  s  j  )  /  τ  )  ∑  i  =  1  N  exp  ⁡  (  S  i  m  (  Z  I  3  D  i  ,  Z  R  e  s  j  )  /  τ  )  \displaystyle-\frac{1}{2N}\sum\_{j=1}^{N}\log\frac{\exp(Sim(Z\_{I3D\_{j}},Z\_{Res\_{j}})/\tau)}{\sum\_{i=1}^{N}\exp(Sim(Z\_{I3D\_{i}},Z\_{Res\_{j}})/\tau)} |    |

The total contrastive loss is the sum of two cross-modal and an inter-modal alignments:

| (3)   |    | ℒ  pretraining  =  ℒ  cross  R  e  s  n  e  t  +  ℒ  cross  I  3  D  +  ℒ  inter  \mathcal{L}\_{\text{pretraining}}=\mathcal{L}\_{\text{cross}^{Resnet}}+\mathcal{L}\_{\text{cross}^{I3D}}+\mathcal{L}\_{\text{inter}}   |    |
|-------|----|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----|

where ℒ cross R  e  s  n  e  t \mathcal{L}\_{\text{cross}^{Resnet}} and ℒ cross I  3  D \mathcal{L}\_{\text{cross}^{I3D}} represent the cross-modal contrastive losses that align the visual representations extracted by the ResNet and I3D branches, respectively, with their corresponding text embeddings. The ℒ inter \mathcal{L}\_{\text{inter}} denotes an inter-modal contrastive loss that aims to pull together embeddings from both visual encoders.

### 3.2. Translation

In this stage, we aim to generate accurate spoken language translations from sign language videos. We employ mBART (Liu et al., [2020](#bib.bib19) ) as the main framework, where we initialize the encoder and decoder with the pretrained shared encoder and text decoder.

Feature Aggregation. After capturing visual features from both visual encoders, a critical step is the fusion of these complementary features. We explore and evaluate various feature aggregation techniques, including element-wise sum, concatenation by channel, and cross-attention as illustrated in Fig. [1](#S3.F1) .

Visual-Language Adapter. After the aggregation of visual features, they are passed through a visual-language adapter to further refine the aggregated visual features before their integration into the mBART. It contains a fully connected layer, layer normalization, followed by a ReLu activation function.

We use cross-entropy loss to minimize the discrepancies between the predicted and true conditional probabilities of the spoken-language sentence given the sign language video, formally expressed as:

| (4)   |    | ℒ  t  r  a  n  s  l  a  t  i  o  n  =  −  l  o  g  p  (  S  &#124;  V  )  \mathcal{L}\_{translation}=-logp(S&#124;V)   |    |
|-------|----|------------------------------------------------------------------------------------------------------------------------|----|

## 4. Experiments

### 4.1. Dataset and Evaluation Metrics

Dataset. We evaluate on the Phoenix-2014T (Camgoz et al., [2018](#bib.bib4) ) , which is the most widely used sign language translation dataset. It is a German sign language dataset, containing 7096, 519, and 642 samples for training, dev, and test, with a vocabulary of 2,887 words.

Evaluation Metrics. We use BLEU (Papineni et al., [2002](#bib.bib22) ) , ROUGE-L (Lin, [2004](#bib.bib17) ) , and BLEURT (Sellam et al., [2020](#bib.bib28) ) metrics to evaluate the performance of our SLT approach. BLEU measures n-gram precision and we use the sacreBLEU (Post, [2018](#bib.bib24) ) implementation. ROUGE-L measures the longest common subsequence between the generated text and the reference, capturing in-order matching words without requiring consecutive overlap. BLEURT (Sellam et al., [2020](#bib.bib28) ) is a trained metric that aims to correlate human-quality scoring better. We use the BLEURT-20 checkpoint (Pu et al., [2021](#bib.bib25) ) . Higher scores indicate better translation.

### 4.2. Implementation Details

Our model is implemented using PyTorch (Paszke et al., [2019](#bib.bib23) ) and trained on a single NVIDIA A100 GPU. We resize input sequences into 256 × 256 256\times 256 which are then cropped into 224 × 224 224\times 224 , where random cropping is used for training and central cropping for inference. Additionally, we apply data augmentation techniques during training with a probability of 50%, including random rotations up to 30°, random resizing with a scale factor of up to 20%, and random translations to shift images up to 10 pixels along both the x and y axes. For pretraining, we employ an SGD optimizer with 0.9 momentum. We initialized the learning rate to 0.02 with a cosine annealing scheduler with batch size 8. For the translation stage, we explore various schedulers detailed in Section [4.4](#S4.SS4) .

We initialized our I3D model with weights pre-trained on the MeineDGS German sign language dataset (Konrad et al., [2020](#bib.bib16) ) for isolated sign language translation (Sincan et al., [2024](#bib.bib32) ) . For the I3D encoder, we follow the standard setting of processing 16 consecutive frames as input. To extract features over the entire video, we apply a sliding window approach with a stride of 6 frames, resulting in temporal overlaps. To match the temporal resolution with ResNet-based embeddings, we repeat the final feature vector to fill in missing frames at the end of the sequence.

We initialized our mBART model with mbart-large-cc25 . To save GPU memory, we trim both the model and the tokenizer based on the train set of the dataset.

### 4.3. Comparison with State-of-the-art Methods

Table [1](#S3.T1) compares our method against existing gloss-based and gloss-free sign language translation approaches on the Phoenix-2014T benchmark. As expected, gloss-based and weakly supervised methods tend to outperform gloss-free methods due to the presence of intermediate supervision or auxiliary data.

In the gloss-free setting, SignCL (Ye et al., [2024](#bib.bib38) ) and Sign2GPT (Wong et al., [2024](#bib.bib35) ) aim to learn effective representations by introducing new contrastive learning or pretraining strategies that achieve better BLEU scores with lower n-gram (BLEU-1 and BLEU-2) and ROUGE scores. On the other hand, recent large language model (LLM) based systems such as FLa-LLM (Chen et al., [2024](#bib.bib9) ) and SignLLM (Gong et al., [2024](#bib.bib12) ) , achieve higher BLEU-4 scores, which is the most commonly used translation metric. Notably, our approach outperforms FLa-LLM (Chen et al., [2024](#bib.bib9) ) and SignLLM (Gong et al., [2024](#bib.bib12) ) across all reported metrics, despite relying on a lighter translation model (Ours: mBART (Liu et al., [2020](#bib.bib19) ) with 3 layers vs. mBART with 12 layers or LLaVA (Liu et al., [2023](#bib.bib18) ) ). Notably, our model achieves the highest BLEU-4 score (23.81) among all gloss-free methods, outperforming the best competitor, SignCL, by +0.84 BLEU-4. This result highlights the strength of our dual encoder in capturing complementary features, leading to more accurate and fluent sentence-level translations.

### 4.4. Ablation Studies

Our experiments include assessing the impact of visual encoders, feature aggregation strategies, and optimization techniques on sign language translation performance.

Visual Encoders. To evaluate the contributions of the two visual encoders, we conducted experiments using each encoder individually. As seen in Table [2](#S4.T2) , the individual performances of ResNet (He et al., [2016](#bib.bib14) ) and I3D (Carreira and Zisserman, [2017](#bib.bib6) ) were found to be comparable, with each encoder showing slight advantages on different metrics. This suggests that both visual encoders effectively capture features relevant to sign language representation. However, fusing them by concatenating in the channel domain enhanced the results.

Feature aggregation techniques. We explore several feature aggregation techniques: element-wise sum, channel-wise concatenation, and cross-attention. As shown in Table [3](#S4.T3) , concatenation yields the best performance across all metrics. We hypothesize that this is due to its ability to preserve the full information from both modalities. In contrast, element-wise addition may introduce mixing signals or potential information loss. We also experiment with a cross-attention mechanism, which enables the model to attend the most relevant features. However, its additional complexity might hinder optimization, especially when the two visual streams are already semantically aligned via pretraining. Nevertheless, all fusion strategies outperformed using either ResNet or I3D alone, highlighting the benefit of leveraging complementary visual features for translation.

Effect of scheduler. We compare the performance of different learning rate schedulers, including Cosine Annealing (CosAnLR) (Loshchilov and Hutter, [2017](#bib.bib20) ) , Exponential (ExpLR), and One Cycle (OneCycleLR) (Smith and Topin, [2019](#bib.bib33) ) , as summarized in Table [4](#S4.T4) . The results highlight that both CosAnLR and OneCycleLR achieved competitive performance. However, OneCycleLR demonstrates a significant advantage by achieving comparable scores in only 150 epochs, while CosAnLR requires 200 epochs. This indicates that OneCycleLR can converge faster while maintaining performance. In contrast, the Exponential LR scheduler underperformed in all metrics, suggesting that a fixed decay rate may be suboptimal for our two-stage training pipeline.

These findings highlight the importance of selecting an appropriate learning rate scheduler for performance and efficiency.

Qualitative analysis. To better understand how our model attends to relevant signing segments during translation, we visualize attention patterns between video frames and generated tokens. These qualitative results complement our quantitative findings and offer insights into how well the model aligns visual and linguistic representations.

Figure [2](#S4.F2) visualizes the cross-attention weights between video frames (y-axis) and generated text tokens (x-axis) during decoding. Brighter regions indicate stronger attention from the decoder to specific frames when predicting the corresponding word. To improve interpretability, we annotate the relevant video frames with the most semantically aligned tokens, using color-coded bounding boxes that match between the video and attention map.

We observe that the decoder assigns high attention scores to the correct signing segments when producing their corresponding words. For example, as shown in Figure [2](#S4.F2) , the token "montag" (red) aligns with the correct sign for "Monday". The attention is temporally localized and consistent, suggesting that the model learns to ground generated text in the relevant spatio-temporal cues. These results highlight the interpretability of our architecture and its ability to align visual and linguistic semantics without gloss supervision.

Figure 2. Cross-attention map between video frames (y-axis) and generated tokens (x-axis). Brighter regions indicate higher attention, showing that the model focuses on the correct frames. The matching colors highlight frames and tokens that align with each other.

<!-- image -->

## 5. Conclusion

In this paper, we propose a novel dual visual encoder framework, DVE-SLT, for sign language translation. We introduce a dual-objective contrastive alignment strategy during pretraining. This strategy encompasses cross-modal alignment to better correlate visual sign representations with textual descriptions, and inter-modal alignment that encourages consistency between the complementary features extracted by our dual visual encoders. Our approach demonstrates that combining two visual encoders improves the performance of gloss-free sign language translation by enabling the model to capture complementary visual information from different aspects of the sign language video. Future work could explore integrating additional modalities and exploring alternative pretraining strategies to further enhance translation quality.

## Ethical Impact Statement

This research aims to enhance sign language translation by leveraging deep learning techniques. While this work has the potential to improve accessibility, we are aware of potential concerns and risks. Since our model is trained on a dataset containing individuals, it is important to address privacy concerns. We used a publicly available dataset, namely Phoenix2014T (Camgoz et al., [2018](#bib.bib4) ) , which includes consent for non-commercial use. However, we would like to acknowledge that the dataset is limited to weather broadcast content. Although the model demonstrates high performance within this context, it might introduce biases and affect its generalizability to other domains. Additionally, we acknowledge the risk of incorrect translations, which could lead to miscommunication in practical applications. To mitigate this, we focus on obtaining more robust visual features to enhance translation accuracy.

## Acknowledgements

We would like to thank Necati Cihan Camgoz for the valuable discussions and feedback. This work was supported by the SNSF project 'SMILE II' (CRSII5 193686), the Innosuisse IICT Flagship (PFFS-21-47), EPSRC grant APP24554 (SignGPT-EP/Z535370/1) and and through funding from Google.org via the AI for Global Goals scheme. This work reflects only the author's views and the funders are not responsible for any use that may be made of the information it contains.

## References

- (1)
- wfd (2025) 2025. *World Federation of the Deaf* . [https://wfdeaf.org/contact/faqs/](https://wfdeaf.org/contact/faqs/) Accessed: 2025-05-30.
- Albanie et al. (2021) Samuel Albanie, Gül Varol, Liliane Momeni, Hannah Bull, Triantafyllos Afouras, Himel Chowdhury, Neil Fox, Bencie Woll, Rob Cooper, Andrew McParland, et al. 2021. Bbc-oxford british sign language dataset. *arXiv preprint arXiv:2111.03635* (2021).
- Camgoz et al. (2018) Necati Cihan Camgoz, Simon Hadfield, Oscar Koller, Hermann Ney, and Richard Bowden. 2018. Neural Sign Language Translation. In *Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR)* .
- Camgoz et al. (2020) Necati Cihan Camgoz, Oscar Koller, Simon Hadfield, and Richard Bowden. 2020. Sign language transformers: Joint end-to-end sign language recognition and translation. In *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition* . 10023-10033.
- Carreira and Zisserman (2017) Joao Carreira and Andrew Zisserman. 2017. Quo vadis, action recognition? a new model and the kinetics dataset. In *proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR)* . 6299-6308.
- Chen et al. (2022a) Yutong Chen, Fangyun Wei, Xiao Sun, Zhirong Wu, and Stephen Lin. 2022a. A simple multi-modality transfer learning baseline for sign language translation. In *Proceedings of the IEEE/CVF conference on computer vision and pattern recognition* . 5120-5130.
- Chen et al. (2022b) Yutong Chen, Ronglai Zuo, Fangyun Wei, Yu Wu, Shujie Liu, and Brian Mak. 2022b. Two-stream network for sign language recognition and translation. *Advances in Neural Information Processing Systems* 35 (2022), 17043-17056.
- Chen et al. (2024) Zhigang Chen, Benjia Zhou, Jun Li, Jun Wan, Zhen Lei, Ning Jiang, Quan Lu, and Guoqing Zhao. 2024. Factorized Learning Assisted with Large Language Model for Gloss-free Sign Language Translation. *the 2024 Joint International Conference on Computational Linguistics, Language Resources and Evaluation (LREC-COLING)* (2024).
- Cheng et al. (2023) Yiting Cheng, Fangyun Wei, Jianmin Bao, Dong Chen, and Wenqiang Zhang. 2023. Cico: Domain-aware sign language retrieval via cross-lingual contrastive learning. In *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition* . 19016-19026.
- Girdhar et al. (2023) Rohit Girdhar, Alaaeldin El-Nouby, Zhuang Liu, Mannat Singh, Kalyan Vasudev Alwala, Armand Joulin, and Ishan Misra. 2023. Imagebind: One embedding space to bind them all. In *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition* . 15180-15190.
- Gong et al. (2024) Jia Gong, Lin Geng Foo, Yixuan He, Hossein Rahmani, and Jun Liu. 2024. Llms are good sign language translators. In *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)* . 18362-18372.
- Gutmann and Hyvärinen (2010) Michael Gutmann and Aapo Hyvärinen. 2010. Noise-contrastive estimation: A new estimation principle for unnormalized statistical models. In *Proceedings of the thirteenth international conference on artificial intelligence and statistics* . JMLR Workshop and Conference Proceedings, 297-304.
- He et al. (2016) Kaiming He, Xiangyu Zhang, Shaoqing Ren, and Jian Sun. 2016. Deep residual learning for image recognition. In *Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition* . 770-778.
- Jiao et al. (2025) Peiqi Jiao, Yuecong Min, and Xilin Chen. 2025. Visual Alignment Pre-training for Sign Language Translation. In *European Conference on Computer Vision* . Springer, 349-367.
- Konrad et al. (2020) Reiner Konrad, Thomas Hanke, Gabriele Langer, Dolly Blanck, Julian Bleicken, Ilona Hofmann, Olga Jeziorski, Lutz König, Susanne König, Rie Nishio, Anja Regen, Uta Salden, Sven Wagner, Satu Worseck, Oliver Böse, Elena Jahn, and Marc Schulder. 2020. MEINE DGS - annotiert. Öffentliches Korpus der Deutschen Gebärdensprache, 3. Release / MY DGS - annotated. Public Corpus of German Sign Language, 3rd release. [https://doi.org/10.25592/dgs.corpus-3.0](https://doi.org/10.25592/dgs.corpus-3.0)
- Lin (2004) Chin-Yew Lin. 2004. Rouge: A package for automatic evaluation of summaries. In *Text summarization branches out* . 74-81.
- Liu et al. (2023) Haotian Liu, Chunyuan Li, Qingyang Wu, and Yong Jae Lee. 2023. Visual instruction tuning. *Advances in neural information processing systems* 36 (2023), 34892-34916.
- Liu et al. (2020) Yinhan Liu, Jiatao Gu, Naman Goyal, Xian Li, Sergey Edunov, Marjan Ghazvininejad, Mike Lewis, and Luke Zettlemoyer. 2020. Multilingual Denoising Pre-training for Neural Machine Translation. *Transactions of the Association for Computational Linguistics* 8 (2020), 726-742. [https://doi.org/10.1162/tacl\_a\_00343](https://doi.org/10.1162/tacl_a_00343)
- Loshchilov and Hutter (2017) Ilya Loshchilov and Frank Hutter. 2017. SGDR: Stochastic Gradient Descent with Warm Restarts. In *International Conference on Learning Representations* . [https://openreview.net/forum?id=Skq89Scxx](https://openreview.net/forum?id=Skq89Scxx)
- Momeni et al. (2022) Liliane Momeni, Hannah Bull, KR Prajwal, Samuel Albanie, Gül Varol, and Andrew Zisserman. 2022. Automatic dense annotation of large-vocabulary sign language videos. In *European Conference on Computer Vision* . Springer, 671-690.
- Papineni et al. (2002) Kishore Papineni, Salim Roukos, Todd Ward, and Wei-Jing Zhu. 2002. Bleu: a method for automatic evaluation of machine translation. In *Proceedings of the 40th annual meeting of the Association for Computational Linguistics* . 311-318.
- Paszke et al. (2019) Adam Paszke, Sam Gross, Francisco Massa, Adam Lerer, James Bradbury, Gregory Chanan, Trevor Killeen, Zeming Lin, Natalia Gimelshein, Luca Antiga, et al. 2019. Pytorch: An imperative style, high-performance deep learning library. *Advances in neural information processing systems* 32 (2019).
- Post (2018) Matt Post. 2018. A Call for Clarity in Reporting BLEU Scores. In *Proceedings of the Third Conference on Machine Translation: Research Papers* . Association for Computational Linguistics, Belgium, Brussels, 186-191. [https://www.aclweb.org/anthology/W18-6319](https://www.aclweb.org/anthology/W18-6319)
- Pu et al. (2021) Amy Pu, Hyung Won Chung, Ankur P Parikh, Sebastian Gehrmann, and Thibault Sellam. 2021. Learning compact metrics for MT. In *Proceedings of EMNLP* .
- Radford et al. (2021) Alec Radford, Jong Wook Kim, Chris Hallacy, Aditya Ramesh, Gabriel Goh, Sandhini Agarwal, Girish Sastry, Amanda Askell, Pamela Mishkin, Jack Clark, et al. 2021. Learning transferable visual models from natural language supervision. In *International Conference on Machine Learning* . PMLR, 8748-8763.
- Ruan et al. (2023) Ludan Ruan, Anwen Hu, Yuqing Song, Liang Zhang, Sipeng Zheng, and Qin Jin. 2023. Accommodating audio modality in CLIP for multimodal processing. In *Proceedings of the AAAI Conference on Artificial Intelligence* , Vol. 37. 9641-9649.
- Sellam et al. (2020) Thibault Sellam, Dipanjan Das, and Ankur P Parikh. 2020. BLEURT: Learning robust metrics for text generation. *arXiv preprint arXiv:2004.04696* (2020).
- Shi et al. (2022a) Bowen Shi, Diane Brentari, Gregory Shakhnarovich, and Karen Livescu. 2022a. Open-Domain Sign Language Translation Learned from Online Video. In *Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing* , Yoav Goldberg, Zornitsa Kozareva, and Yue Zhang (Eds.). Association for Computational Linguistics, Abu Dhabi, United Arab Emirates, 6365-6379. [https://doi.org/10.18653/v1/2022.emnlp-main.427](https://doi.org/10.18653/v1/2022.emnlp-main.427)
- Shi et al. (2022b) Bowen Shi, Diane Brentari, Gregory Shakhnarovich, and Karen Livescu. 2022b. Ttic's wmt-slt 22 sign language translation system. In *Proceedings of the Seventh Conference on Machine Translation (WMT)* . 989-993.
- Sincan et al. (2023) Ozge Mercanoglu Sincan, Necati Cihan Camgoz, and Richard Bowden. 2023. Is context all you need? scaling neural sign language translation to large domains of discourse. In *Proceedings of the IEEE/CVF International Conference on Computer Vision* . 1955-1965.
- Sincan et al. (2024) Ozge Mercanoglu Sincan, Necati Cihan Camgoz, and Richard Bowden. 2024. Using an LLM to Turn Sign Spottings into Spoken Language Sentences. *arXiv preprint arXiv:2403.10434* (2024).
- Smith and Topin (2019) Leslie N Smith and Nicholay Topin. 2019. Super-convergence: Very fast training of neural networks using large learning rates. In *Artificial intelligence and machine learning for multi-domain operations applications* , Vol. 11006. SPIE, 369-386.
- Vaswani (2017) A Vaswani. 2017. Attention is all you need. *Advances in Neural Information Processing Systems* (2017).
- Wong et al. (2024) Ryan Wong, Necati Cihan Camgoz, and Richard Bowden. 2024. Sign2GPT: Leveraging Large Language Models for Gloss-Free Sign Language Translation. In *The Twelfth International Conference on Learning Representations* . [https://openreview.net/forum?id=LqaEEs3UxU](https://openreview.net/forum?id=LqaEEs3UxU)
- Xu et al. (2021) Hu Xu, Gargi Ghosh, Po-Yao Huang, Dmytro Okhonko, Armen Aghajanyan, Florian Metze, Luke Zettlemoyer, and Christoph Feichtenhofer. 2021. VideoCLIP: Contrastive Pre-training for Zero-shot Video-Text Understanding. In *Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing* . 6787-6800.
- Yao et al. (2023) Huijie Yao, Wengang Zhou, Hao Feng, Hezhen Hu, Hao Zhou, and Houqiang Li. 2023. Sign language translation with iterative prototype. In *Proceedings of the IEEE/CVF International Conference on Computer Vision* . 15592-15601.
- Ye et al. (2024) Jinhui Ye, Xing Wang, Wenxiang Jiao, Junwei Liang, and Hui Xiong. 2024. Improving Gloss-free Sign Language Translation by Reducing Representation Density. In *The Thirty-eighth Annual Conference on Neural Information Processing Systems* . [https://openreview.net/forum?id=FtzLbGoHW2](https://openreview.net/forum?id=FtzLbGoHW2)
- Zhang et al. (2022) Biao Zhang, Mathias Müller, and Rico Sennrich. 2022. SLTUNET: A Simple Unified Model for Sign Language Translation. In *The Eleventh International Conference on Learning Representations (ICLR)* .
- Zhou et al. (2023) Benjia Zhou, Zhigang Chen, Albert Clapés, Jun Wan, Yanyan Liang, Sergio Escalera, Zhen Lei, and Du Zhang. 2023. Gloss-free sign language translation: Improving from visual-language pretraining. In *Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV)* . 20871-20881.
- Zhou et al. (2021) Hao Zhou, Wengang Zhou, Weizhen Qi, Junfu Pu, and Houqiang Li. 2021. Improving Sign Language Translation With Monolingual Data by Sign Back-Translation. In *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition* . 1316-1325.
- Zhu et al. (2024) Bin Zhu, Bin Lin, Munan Ning, Yang Yan, Jiaxi Cui, WANG HongFa, Yatian Pang, Wenhao Jiang, Junwu Zhang, Zongwei Li, Cai Wan Zhang, Zhifeng Li, Wei Liu, and Li Yuan. 2024. LanguageBind: Extending Video-Language Pretraining to N-modality by Language-based Semantic Alignment. In *The Twelfth International Conference on Learning Representations* . [https://openreview.net/forum?id=QmZKc7UZCy](https://openreview.net/forum?id=QmZKc7UZCy)

## References

- [[ed66f0422dd29a85fe649d5a0949ce17cc273084]] — Improving Gloss-free Sign Language Translation by Reducing Representation Density (2024)
- [[832dd2923e8821bf8c664101a62ffa3ef46e6b47]] — LLMs are Good Sign Language Translators (2024)
- [[8eb99f1ed884356871ddbcf1377b82359071906a]] — LanguageBind: Extending Video-Language Pretraining to N-modality by Language-based Semantic Alignment (2023)
- [[c34c074093fbbe2c6dcc96eba00c91415fba81c7]] — Sign Language Translation with Iterative Prototype (2023)
- [[3f73332fc9a0752b5024ff4d39c4b4e016e51ece]] — Is context all you need? Scaling Neural Sign Language Translation to Large Domains of Discourse (2023)
- [[a6d677eb70cc5d9e621a8040a6254ecf68dd7c9a]] — Gloss-free Sign Language Translation: Improving from Visual-Language Pretraining (2023)
- [[7dc6da87eaa6f830354feb2db14023cab8678c91]] — ImageBind One Embedding Space to Bind Them All (2023)
- [[18c499092df491b0eb4eed3a1c0266b67a93ae13]] — CiCo: Domain-Aware Sign Language Retrieval via Cross-Lingual Contrastive Learning (2023)
- [[98ab8260c98030109ba8467f52b13d075276cf0f]] — Accommodating Audio Modality in CLIP for Multimodal Processing (2023)
- [[dd964ffeb47efb9a3691b5d233e02284ee8228a7]] — Automatic dense annotation of large-vocabulary sign language videos (2022)
- [[be54fc78e86fb3e65964fbfb904f22eb9927502f]] — Open-Domain Sign Language Translation Learned from Online Video (2022)
- [[dfd104dd0ff28b1bde2fbd4c4d6d3ccb4761f639]] — Learning Compact Metrics for MT (2021)
- [[821ad6c9f0fecb5fabb486a5a87a93b7ea65bcc0]] — VideoCLIP: Contrastive Pre-training for Zero-shot Video-Text Understanding (2021)
- [[7811df11a75f58646d04b3132d35f0656e50a109]] — Improving Sign Language Translation with Monolingual Data by Sign Back-Translation (2021)
- [[4ae52766028e69186052ea8f33a137fbbbdb986a]] — BLEURT: Learning Robust Metrics for Text Generation (2020)
- [[05dcdfece56d1869895f53ed581d8ad64118c05f]] — Sign Language Transformers: Joint End-to-End Sign Language Recognition and Translation (2020)
- [[644602c65a5d8f30e62be027eb7b47f7c335191a]] — Neural Sign Language Translation (2018)
- [[b4bfadfca9742bb3ee98a0cd322d5ce4e59a3ceb]] — A Call for Clarity in Reporting BLEU Scores (2018)
- [[1269e191091eadeed6f246cf5a6692b178bb4d94]] — Super-convergence: very fast training of neural networks using large learning rates (2018)
- [[204e3073870fae3d05bcbc2f6a8e263d9b72e776]] — Attention is All you Need (2017)
- [[b61a3f8b80bbd44f24544dc915f52fd30bbdf485]] — Quo Vadis, Action Recognition? A New Model and the Kinetics Dataset (2017)
- [[b022f2a277a4bf5f42382e86e4380b96340b9e86]] — SGDR: Stochastic Gradient Descent with Warm Restarts (2016)
- [[e3ce36b9deb47aa6bb2aa19c4bfa71283b505025]] — Noise-contrastive estimation: A new estimation principle for unnormalized statistical models (2010)
- [[60b05f32c32519a809f21642ef1eb3eaf3848008]] — ROUGE: A Package for Automatic Evaluation of Summaries (2004)
- [[d7da009f457917aa381619facfa5ffae9329a6e9]] — Bleu: a Method for Automatic Evaluation of Machine Translation (2002)
- [[a0cf790c3a650d8cf4d201e17a12ec84812bee60]] — TTIC’s WMT-SLT 22 Sign Language Translation System (2022)
- Learningtransferablevisualmodelsfromnaturallanguagesupervision (2021)
- MultilingualDenoisingPre-training forNeuralMachineTranslation (2020)
- MEINEDGS–annotiert (2020)
- Pytorch:Animperativestyle,high-performancedeeplearninglibrary (2019)
- Deep residual learningforimagerecognition (2016)
- 2023. Visual instruction tuning ()
- 2022. A simple multi-modality transfer learning baseline for sign language translation ()
- 2024. Sign2GPT: Leveraging Large Language Models for Gloss-Free Sign Language Translation ()
- Preprint, Accepted at SLTAT’25, Sept 16–19,2025, ()
- IVA Adjunct ’25, September 16–19, 2025 ()

## Sources

- title: semanticscholar
- abstract: semanticscholar
- authors: semanticscholar
- topics: semanticscholar
- references: semanticscholar
- citations: semanticscholar
- fullText: ar5iv
- bibtex: semanticscholar

---
semanticScholarId: "a3daddcd4a56f15ce2c05fe85dc0e0e4af98d8db"
bibKey: null
year: 2024
title: "MASA: Motion-Aware Masked Autoencoder With Semantic Alignment for Sign Language Recognition"
doi: "10.1109/TCSVT.2024.3409728"
arxivId: "2405.20666"
isSignLanguage: true
expanded: true
topics: ["Computer Science"]
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

# MASA: Motion-Aware Masked Autoencoder With Semantic Alignment for Sign Language Recognition

**Year:** [[2024]]
**Topics:** [[topics/computer-science|Computer Science]]
**Authors:** Weichao Zhao; Hezhen Hu; Wen-gang Zhou; Yunyao Mao; Min Wang; Houqiang Li

## Links
- [Semantic Scholar](https://www.semanticscholar.org/paper/a3daddcd4a56f15ce2c05fe85dc0e0e4af98d8db)
- [PDF](https://arxiv.org/pdf/2405.20666)
- [arXiv:2405.20666](https://arxiv.org/abs/2405.20666)
- [DOI](https://doi.org/10.1109/TCSVT.2024.3409728)

## Abstract

Sign language recognition (SLR) has long been plagued by insufficient model representation capabilities. Although current pre-training approaches have alleviated this dilemma to some extent and yielded promising performance by employing various pretext tasks on sign pose data, these methods still suffer from two primary limitations: i) Explicit motion information is usually disregarded in previous pretext tasks, leading to partial information loss and limited representation capability. ii) Previous methods focus on the local context of a sign pose sequence, without incorporating the guidance of the global meaning of lexical signs. To this end, we propose a Motion-Aware masked autoencoder with Semantic Alignment (MASA) that integrates rich motion cues and global semantic information in a self-supervised learning paradigm for SLR. Our framework contains two crucial components, i.e., a motion-aware masked autoencoder (MA) and a momentum semantic alignment module (SA). Specifically, in MA, we introduce an autoencoder architecture with a motion-aware masked strategy to reconstruct motion residuals of masked frames, thereby explicitly exploring dynamic motion cues among sign pose sequences. Moreover, in SA, we embed our framework with global semantic awareness by aligning the embeddings of different augmented samples from the input sequence in the shared latent space. In this way, our framework can simultaneously learn local motion cues and global semantic features for comprehensive sign language representation. Furthermore, we conduct extensive experiments to validate the effectiveness of our method, achieving new state-of-the-art performance on four public benchmarks. The source code are publicly available at https://github.com/sakura/MASA.

## TL;DR

A Motion-Aware masked autoencoder with Semantic Alignment (MASA) that integrates rich motion cues and global semantic information in a self-supervised learning paradigm for SLR, and can simultaneously learn local motion cues and global semantic features for comprehensive sign language representation.

## BibTeX

```bibtex
@Article{Zhao2024MASAMM,
 author = {Weichao Zhao and Hezhen Hu and Wen-gang Zhou and Yunyao Mao and Min Wang and Houqiang Li},
 booktitle = {IEEE transactions on circuits and systems for video technology (Print)},
 journal = {IEEE Transactions on Circuits and Systems for Video Technology},
 pages = {10793-10804},
 title = {MASA: Motion-Aware Masked Autoencoder With Semantic Alignment for Sign Language Recognition},
 volume = {34},
 year = {2024}
}
```

## Full Text

# MASA: Motion-aware Masked Autoencoder with Semantic Alignment for Sign Language Recognition

Weichao Zhao, Hezhen Hu, Wengang Zhou , Yunyao Mao, Min Wang, Houqiang Li This work is supported by National Natural Science Foundation of China under Contract U20A20183 &amp; 62021001, and the Youth Innovation Promotion Association CAS. It was also supported by the GPU cluster built by MCC Lab of Information Science and Technology Institution, USTC, and the Supercomputing Center of the USTC. Weichao Zhao, Hezhen Hu, Wengang Zhou, Yunyao Mao and Houqiang Li are with the CAS Key Laboratory of Technology in Geospatial Information Processing and Application System, Department of Electronic Engineering and Information Science, University of Science and Technology of China, Hefei, 230027, China (e-mail: {saruka, alexhu, myy2016}@mail.ustc.edu.cn, {zhwg, lihq}@ustc.edu.cn.Min Wang is with the Institute of Artificial Intelligence, Hefei Comprehensive National Science Center, Hefei 230030, China (e-mail: wangmin@iai.ustc.edu.cn).Corresponding authors: Wengang Zhou and Houqiang Li.

###### Abstract

Sign language recognition (SLR) has long been plagued by insufficient model representation capabilities.

Although current pre-training approaches have alleviated this dilemma to some extent and yielded promising performance by employing various pretext tasks on sign pose data, these methods still suffer from two primary limitations:

i) Explicit motion information is usually disregarded in previous pretext tasks, leading to partial information loss and limited representation capability.

ii) Previous methods focus on the local context of a sign pose sequence, without incorporating the guidance of the global meaning of lexical signs.

To this end, we propose a M otion- A ware masked autoencoder with S emantic A lignment (MASA) that integrates rich motion cues and global semantic information in a self-supervised learning paradigm for SLR.

Our framework contains two crucial components,

*i.e.,* a motion-aware masked autoencoder (MA) and a momentum semantic alignment module (SA).

Specifically, in MA, we introduce an autoencoder architecture with a motion-aware masked strategy to reconstruct motion residuals of masked frames, thereby explicitly exploring dynamic motion cues among sign pose sequences.

Moreover, in SA, we embed our framework with global semantic awareness by aligning the embeddings of different augmented samples from the input sequence in the shared latent space.

In this way, our framework can simultaneously learn local motion cues and global semantic features for comprehensive sign language representation.

Furthermore, we conduct extensive experiments to validate the effectiveness of our method, achieving new state-of-the-art performance on four public benchmarks.

The source code are publicly available at

[https://github.com/sakura/MASA](https://github.com/sakura2233565548/MASA) .

###### Index Terms:

Masked autoencoder, motion-aware, semantic alignment, sign language recognition.

## I Introduction

Sign language serves as the primary communication tool within the deaf community.

Different from spoken language, sign language is characterized by its special grammar and lexicon, which causes difficulties in comprehension for hearing people.

To facilitate communication between the deaf and hearing communities, sign language recognition (SLR) has received significant attention for its potential social impact.

As a fundamental task, isolated SLR aims to recognize the meaning of sign language video at the gloss-level under complex situations, i.e., quick motion, unconstrained background and individual diversities. In this work, we focus on isolated SLR.

Most existing isolated SLR works [ [34](#bib.bib34) , [35](#bib.bib35) , [29](#bib.bib29) , [22](#bib.bib22) , [26](#bib.bib26) , [58](#bib.bib58) , [51](#bib.bib51) , [1](#bib.bib1) , [17](#bib.bib17) ] are directly optimized on the target benchmark in a supervised learning paradigm, which is prone to over-fitting due to insufficient sign data resources.

To address this issue, some methods [

[19](#bib.bib19) , [69](#bib.bib69) , [2](#bib.bib2) , [25](#bib.bib25) , [18](#bib.bib18) ] attempt to design different pre-training strategies to boost performance on isolated SLR, inspired by the related progress in NLP and CV fields.

Among them, Albanie et al. [

[2](#bib.bib2) ] utilize the pose keypoints as supervision signals to force the model to pay more attention to the foreground signer from RGB images.

Considering that pose is a more compact representation than RGB images, SignBERT [

[19](#bib.bib19) ] introduces a self-supervised pre-trainable framework with available sign pose data.

It captures the contextual information by masking and reconstructing hand joints among a sign pose sequence and achieves promising performance.

Additionally, BEST [

[69](#bib.bib69) ] tokenizes continuous joints into a discrete space as the pseudo labels and performs similar pre-training as BERT [ [9](#bib.bib9) ] via reconstructing the masked tokens from the corrupted input sequence.

Despite the decent results made by the above methods, there still exist several unresolved issues.

Firstly, motion dynamics are widely regarded as a crucial role in the field of sign language understanding [

[53](#bib.bib53) , [50](#bib.bib50) , [36](#bib.bib36) ] .

However, existing pre-training methods set the objective as recovering the static information (e.g. joint spatial location), which constrains its modeling capability on motion cues among frames and leads to sub-optimal performance.

Secondly, these methods do not explicitly incorporate the global meaning present in sign pose data.

Since the meaning of a lexical sign is generally expressed by a series of poses, the instance representation of a sign pose sequence also holds effective information for sign language comprehension.

Unfortunately, previous methods [

[19](#bib.bib19) , [69](#bib.bib69) , [25](#bib.bib25) ] mainly focus on learning local contextual information for fulfilling the reconstruction task, while lacking the explicit exploration of such crucial representations.

Inspired by the above observations, we propose a novel motion-aware masked autoencoder with semantic alignment via a self-supervised learning paradigm for SLR.

Our framework aims to leverage effective motion information and global contextual meaning to learn more effective representation during pre-training.

On one hand, in order to explicitly mine motion cues among the sign pose sequence, we introduce a motion-aware masked autoencoder (MA).

Concretely, we present a motion-aware masked strategy, which purposely selects the regions with the conspicuous motion for masking.

Given the masked sign pose sequence, we utilize the remaining information to reconstruct the motion residuals of masked frames rather than the static joints.

By combining these key designs, our proposed method can focus on more informative regions for capturing dynamic pose variations and improving learned representations.

On the other hand, we design a momentum semantic alignment module (SA) to endow our model with the capability of learning consistent instance representation.

Specifically, we generate two augmented samples from the input sequence, treating them as positive samples and aligning the embeddings of positive samples in the shared latent space with a contrastive objective.

Additionally, we incorporate a momentum mechanism to update the parameters of most models in SA, reducing extra computation costs.

In this way, our proposed method enables the explicit exploitation of motion cues and global semantic meaning to jointly learn powerful representations.

The key contributions of our work are summarized as follows:

- • We propose a novel motion-aware masked autoencoder with semantic alignment for sign language recognition. It aims to leverage explicit motion information and global semantic meaning in sign pose data to fertilize sign language representation learning.
- • We introduce two main components in our framework, i.e., motion-aware masked autoencoder (MA) and momentum semantic alignment module (SA). In MA, we delicately design masked strategy and an optimized objective to effectively capture dynamic motion cues among sign pose sequence. In SA, we introduce a module to guide our framework learning the globally consistent meaning of lexical signs by aligning features in the latent space. In this way, our model is endowed with capturing both local pose variation and global sign meaning for more holistic representations.
- • Extensive experiments on isolated SLR validate the effectiveness of our proposed method. Compared with previous methods, our method achieves new state-of-the-art performance on four public benchmarks, i.e., WLASL, MSASL, NMFs\_CSL and SLR500.

## II Related Work

In this section, we will briefly review several related topics for this paper, including sign language recognition and self-supervised representation learning.

### II-A Sign Language Recognition

Sign language recognition as a fundamental task has received increasing attention in recent years [ [29](#bib.bib29) , [47](#bib.bib47) , [28](#bib.bib28) ] .

With the popularity of video capture devices, the majority of methods utilize RGB videos as their research target.

Sarhan et al., [

[49](#bib.bib49) ] present a comprehensive survey on the development of ISLR research, covering various aspects including modalities, parameters, fusion categories and transfer learning.

Generally, these research works are grouped into two categories based on the input modality, i.e., RGB-based and pose-based methods.

RGB-based Methods. Early studies in SLR predominantly focused on the design of hand-crafted features to represent hand shape variation and body motion [ [11](#bib.bib11) , [12](#bib.bib12) , [54](#bib.bib54) , [61](#bib.bib61) ] .

However, with the advance of deep learning techniques, there has been a notable shift in the field, with a growing number of works adopting convolutional neural networks (CNNs) as the fundamental architecture for feature extraction [

[21](#bib.bib21) , [20](#bib.bib20) , [29](#bib.bib29) , [52](#bib.bib52) , [51](#bib.bib51) , [30](#bib.bib30) , [64](#bib.bib64) , [60](#bib.bib60) ] . Since the input signal for SLR is an RGB video sequence, some works [ [21](#bib.bib21) , [35](#bib.bib35) , [63](#bib.bib63) , [14](#bib.bib14) , [67](#bib.bib67) ] employ

2D CNN networks to extract frame-wise features and then aggregate temporal information to predict sign language.

To better model spatial-temporal representations in sign language videos, some works [

[23](#bib.bib23) , [26](#bib.bib26) , [2](#bib.bib2) , [35](#bib.bib35) , [34](#bib.bib34) ] attempt to adopt 3D CNNs, i.e., I3D [ [6](#bib.bib6) ] and S3D [ [65](#bib.bib65) ] to extract video-level features due to their capacity of spatial-temporal dependency.

NLA-SLR [

[72](#bib.bib72) ] leverages RGB videos and the human keypoints heatmaps with different temporal receptive fields to build a four-stream framework based on S3D [ [65](#bib.bib65) ] , which improves the recognition accuracy through complex model design. Bilge et al., [ [4](#bib.bib4) ] propose a zero-shot learning framework on ISLR task, which leverages the descriptive text

and attribute embeddings to transfer knowledge to the instances of unseen sign classes.

Pose-based Methods. Compared to RGB images, human pose includes the meaningful expressions conveyed in sign language videos through human skeleton movements, while reducing interference factors like complex backgrounds and external appearances of signers.

Due to naturally physical connections among skeleton joints, graph convolutional networks (GCNs) are widely applied to model spatial-temporal relations as the backbone [

[33](#bib.bib33) , [10](#bib.bib10) , [66](#bib.bib66) , [34](#bib.bib34) , [25](#bib.bib25) , [40](#bib.bib40) , [32](#bib.bib32) ] .

Kindiroglu et al., [

[27](#bib.bib27) ] explore the feasibility of transferring knowledge among different benchmarks with GCN-based approaches. TSSI [ [30](#bib.bib30) ] converts a skeleton sequence into an RGB image and utilizes an RGB-based backbone to model sequential skeleton features, achieving promising improvement.

Hu et al. [

[19](#bib.bib19) , [18](#bib.bib18) ] propose a self-supervised learning framework SignBERT by masking and reconstructing hand pose sequence to learn local contextual information.

To better leverage the success of BERT into the sign language domain, Zhao et al. [

[69](#bib.bib69) ] tokenize sign pose into a triplet unit in a frame-wise manner and also introduce a pre-trainable framework namely BEST to improve the performance of sign language recognition. However, these pre-training methods overlook the importance of dynamic motion information, while our proposed method explicitly explores motion cues among sign pose sequences to learn more effective representation.

### II-B Self-supervised Representation Learning

Self-supervised representation learning aims to learn effective representation from massive unlabeled data, which shows better generalizability in downstream tasks.

To supervise the pre-training process, researchers design variant pretext tasks, i.e., jigsaw puzzles [

[41](#bib.bib41) , [42](#bib.bib42) ] , colorization [ [68](#bib.bib68) ] , predicting rotation [ [13](#bib.bib13) ] , masked patch reconstruction [ [15](#bib.bib15) , [57](#bib.bib57) , [24](#bib.bib24) ] , contrast similarity between samples [ [7](#bib.bib7) , [16](#bib.bib16) , [43](#bib.bib43) , [45](#bib.bib45) ] , etc. Recently, masked patches reconstruction and contrastive learning have become mainstream methods in video representation learning.

The former focuses more on the local relations in the input video, while the latter inclines to model relations among different videos.

Typically, VideoMAE [

[57](#bib.bib57) ] proposes customized video tube masking to enforce high-level structure learning and obtains impressive performance.

In contrast, VideoMoCo [

[44](#bib.bib44) ] learns instance discriminative representation by encoding similar features from two perspectives in an input video and pulling the distance of similar features.

In order to strengthen video representation learning, a few works [ [56](#bib.bib56) , [70](#bib.bib70) , [24](#bib.bib24) , [62](#bib.bib62) , [3](#bib.bib3) , [71](#bib.bib71) , [39](#bib.bib39) ] attempt to leverage both prevailing techniques.

In fields related to human behavior, PoseBERT [

[3](#bib.bib3) ] utilizes a masked modeling technique on the pose parameters of the human model SMPL, which aims to improve the performance of human mesh recovery.

Mao et al., [

[39](#bib.bib39) ] propose a masked motion predictor to better capture contextual information among human pose sequences.

Conversely, MotionBERT [

[71](#bib.bib71) ] leverages a substantial volume of human motion data captured through motion capture devices to improve downstream tasks.

In the sign language domain, current self-supervised methods [

[19](#bib.bib19) , [69](#bib.bib69) , [25](#bib.bib25) ] are based on masked modeling strategy and overlook the discriminative representation of a lexical sign, which is also essential to sign language understanding.

To address this problem, we first explore to perceive comprehensive global information in local frame features via self-supervised learning.

Figure 1: The illustration of our proposed framework during pre-training. It mainly contains two crucial components, i.e., a motion-aware masked autoencoder (MA) and a momentum semantic alignment module (SA). In MA, given a sign pose sequence, the frame-wise embedding layer encodes each frame pose into a latent feature. The encoder operates on unmasked feature sequences. Then, the target decoder predicts the motion residuals from pose tokens (along with mask tokens). In SA, it employs a siamese framework extracting pose features from randomly sampled pose sequence similar to MA. After that, we project global features from positive views into a shared embedding space and align them with the semantic consistency loss. The modules with the black dashed box are momentum updated and the red arrows represent the gradient back propagation.

<!-- image -->

## III Method

The overall of our proposed method is illustrated in Fig. [1](#S2.F1) , which consists of a motion-aware masked autoencoder (MA) and a momentum semantic alignment module (SA).

In MA, we present a novel motion-aware masked strategy to prioritize more informative regions for masking, avoiding randomly masking invalid frames, i.e, consecutive similar poses and low-confidence regions.

In SA, we extract two sequence-level representations from augmented samples of the input sequence.

Then, we impose constraints on the consistency of both features in a latent embedding space to fertilize our model with discriminative capability.

In the following, we first elaborate these components separately. Then, we present our training objective. Finally, the downstream fine-tuning of our approach is discussed. Conveniently, we provide a terminology table in Tab.

[I](#S3.T1) for better understanding of our method.

### III-A Motion-aware Masked Autoencoder

Motion-aware Masked Strategy. Given the sign pose sequence V i  n = { x i ∈ ℝ N × 2 } i = 1 T subscript 𝑉 𝑖 𝑛 superscript subscript subscript 𝑥 𝑖 superscript ℝ 𝑁 2 𝑖 1 𝑇 \mathit{V}\_{in}=\{x\_{i}\in\mathbb{R}^{N\times 2}\}\_{i=1}^{T} , we first compute the motion residuals among these frames denoted as M = { m i | x i + k − x i , i  f  0 ≤ i ≤ T − k , e  l  s  e  𝟘 → } i = 1 T 𝑀 superscript subscript conditional-set subscript 𝑚 𝑖 formulae-sequence subscript 𝑥 𝑖 𝑘 subscript 𝑥 𝑖 𝑖 𝑓 0 𝑖 𝑇 𝑘 𝑒 𝑙 𝑠 𝑒 superscript 𝟘 → 𝑖 1 𝑇 \mathit{M}=\{m\_{i}\ |\ x\_{i+k}-x\_{i}\ ,\ if\ 0\leq i\leq T-k\ ,else\ \mathop{\mathbb{0}}\limits^{\rightarrow}\}\_{i=1}^{T} , in which k 𝑘 k represents the interval length between two frames.

Since the hand motion is inherently coupled with the upper body that leads to difficultly capturing fine-grained hand movements, we crop hand and upper body parts separately to emphasize these dominant regions and then compute the movements of each part.

Based on the above operation, m i subscript 𝑚 𝑖 m\_{i} contains the decoupled pose variations of both hands and the upper body at the i 𝑖 i -th timestep.

As the pose sequence is estimated utilizing an off-the-shelf estimator, the resulting confidence values for each pose provide essential information regarding the reliability of the estimation process.

Thus, we organize the original confidence values of V i  n subscript 𝑉 𝑖 𝑛 \mathit{V}\_{in} as R i  n = { r i ∈ ℝ N } i = 1 T subscript 𝑅 𝑖 𝑛 superscript subscript subscript 𝑟 𝑖 superscript ℝ 𝑁 𝑖 1 𝑇 \mathit{R}\_{in}=\{r\_{i}\in\mathbb{R}^{N}\}\_{i=1}^{T} .

Moreover, in order to eliminate the interference of low-confidence joints of each pose, we set a threshold ϵ c subscript italic-ϵ 𝑐 \epsilon\_{c} to truncate low confidence values, denoted as C = { c i := r i ⋅ 𝕀  ( r i ≥ ϵ c ) } i = 1 T 𝐶 superscript subscript assign subscript 𝑐 𝑖 ⋅ subscript 𝑟 𝑖 𝕀 subscript 𝑟 𝑖 subscript italic-ϵ 𝑐 𝑖 1 𝑇 \mathit{C}=\{c\_{i}:=r\_{i}\cdot\mathbb{I}(r\_{i}\geq\epsilon\_{c})\}\_{i=1}^{T} , where 𝕀  ( ⋅ ) 𝕀 ⋅ \mathbb{I}(\cdot) is an indicator function.

Then, given the motion sequence M 𝑀 M and the pose confidence C 𝐶 C , we could obtain the high-confidence motion information and choose the frames with conspicuous motion into the candidate set, in which a fraction of frames is randomly selected for masking, as shown in Alg.

[1](#alg1) .

Finally, we can obtain the selected masked index set ℳ ℳ \mathcal{M} .

Frame-wise Pose Embedding Layer. We utilize this embedding layer to embed each frame pose into the latent space. Motivated by SignBERT [ [19](#bib.bib19) ] , we design a graph convolutional network (GCN) comprising two sub-networks modified from [ [5](#bib.bib5) ] , which aims to extract the latent embeddings of both hands and upper body respectively. Specifically, given the sign pose sequence V i  n subscript 𝑉 𝑖 𝑛 V\_{in} of T frames, the latent embedding of the i 𝑖 i -th frame is extracted as follows,

|    | f  i  =  E  m  b  e  d  \_  L  a  y  e  r  (  x  i  )  =  C  o  n  c  a  t  (  GCN  \_  H  (  x  i  h  )  ,  GCN  \_  B  (  x  i  b  )  )  ,  x  i  ∈  V  i  n  ,  \begin{split}f\_{i}&amp;=Embed\_Layer(x\_{i})\\  &amp;=Concat(\mathrm{GCN\_H}(x\_{i}^{h}),\ \mathrm{GCN\_B}(x\_{i}^{b})),\quad x\_{i}\in\mathit{V}\_{in},\end{split}   |    | (1)   |
|----|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----|-------|

where GCN  \_  H  ( ⋅ ) GCN \_ H ⋅ \mathrm{GCN\_H(\cdot)} and GCN  \_  B  ( ⋅ ) GCN \_ B ⋅ \mathrm{GCN\_B(\cdot)} denote two sub-networks, while x i h superscript subscript 𝑥 𝑖 ℎ x\_{i}^{h} and x i b superscript subscript 𝑥 𝑖 𝑏 x\_{i}^{b} represent the hand and body parts of x i subscript 𝑥 𝑖 x\_{i} , respectively.

Thus, the embedding sequence is denoted as F e = { f i ∈ ℝ D e } i = 1 T subscript 𝐹 𝑒 superscript subscript subscript 𝑓 𝑖 superscript ℝ subscript 𝐷 𝑒 𝑖 1 𝑇 \mathit{F}\_{e}=\{f\_{i}\in\mathbb{R}^{D\_{e}}\}\_{i=1}^{T} .

Encoder. Given the embedding sequence F e subscript 𝐹 𝑒 \mathit{F}\_{e} and the masked index set ℳ ℳ \mathcal{M} , we split F e subscript 𝐹 𝑒 \mathit{F}\_{e} into two parts, i.e., the unmasked sequence F ~ e = { f i | i ∉ ℳ } subscript ~ 𝐹 𝑒 conditional-set subscript 𝑓 𝑖 𝑖 ℳ \widetilde{F}\_{e}=\{f\_{i}|i\not\in\mathcal{M}\} and a series of learnable masked token F m  a  s  k = { 𝐞 i , m  a  s  k ∈ ℝ D e | i ∈ ℳ } subscript 𝐹 𝑚 𝑎 𝑠 𝑘 conditional-set subscript 𝐞 𝑖 𝑚 𝑎 𝑠 𝑘 superscript ℝ subscript 𝐷 𝑒 𝑖 ℳ \mathit{F}\_{mask}=\{\mathbf{e}\_{i,mask}\in\mathbb{R}^{D\_{e}}|i\in\mathcal{M}\} . The encoder adopts the vanilla Transformer [ [59](#bib.bib59) ] architecture and is applied to F ~ e subscript ~ 𝐹 𝑒 \widetilde{F}\_{e} . We feed them into a sequence of transformer blocks and obtain the output sequence F e  n  c = E  n  c  o  d  e  r  ( F ~ e ) subscript 𝐹 𝑒 𝑛 𝑐 𝐸 𝑛 𝑐 𝑜 𝑑 𝑒 𝑟 subscript ~ 𝐹 𝑒 \mathit{F}\_{enc}=Encoder(\widetilde{F}\_{e}) , which is utilized to reconstruct masked information.

Target Decoder. The target decoder aims to recover the masked pose information from the visible features.

Specifically, the decoder receives both the encoder feature sequence F e  n  c subscript 𝐹 𝑒 𝑛 𝑐 \mathit{F}\_{enc} and the masked tokens F m  a  s  k subscript 𝐹 𝑚 𝑎 𝑠 𝑘 \mathit{F}\_{mask} as input.

We first concatenate F e  n  c subscript 𝐹 𝑒 𝑛 𝑐 \mathit{F}\_{enc} and F m  a  s  k subscript 𝐹 𝑚 𝑎 𝑠 𝑘 \mathit{F}\_{mask} together in the original order.

Then, another vanilla Transformer [

[59](#bib.bib59) ] is utilized to mine effective contextual information from the encoder features as a decoder and complements missing information of masked tokens, which is computed as follows,

|    | F  d  e  c  =  D  e  c  o  d  e  r  (  F  e  n  c  ,  F  m  a  s  k  )  ,  subscript  𝐹  𝑑  𝑒  𝑐  𝐷  𝑒  𝑐  𝑜  𝑑  𝑒  𝑟  subscript  𝐹  𝑒  𝑛  𝑐  subscript  𝐹  𝑚  𝑎  𝑠  𝑘  \mathit{F}\_{dec}=Decoder(\mathit{F}\_{enc},\mathit{F}\_{mask}),   |    | (2)   |
|----|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----|-------|

where F d  e  c = { f i , d  e  c ∈ ℝ D e } i = 1 T subscript 𝐹 𝑑 𝑒 𝑐 superscript subscript subscript 𝑓 𝑖 𝑑 𝑒 𝑐 superscript ℝ subscript 𝐷 𝑒 𝑖 1 𝑇 \mathit{F}\_{dec}=\{f\_{i,dec}\in\mathbb{R}^{D\_{e}}\}\_{i=1}^{T} denotes the output of stacked transformer blocks.

Finally, a simple MLP predicts the motion residuals of masked frames using the corresponding recovered features, which is computed as follows,

|    | y  i  =  𝕀  (  i  ∈  ℳ  )  ⋅  𝒫  (  f  i  ,  d  e  c  )  ,  𝒴  =  {  y  i  &#124;  i  ∈  ℳ  }  ,  formulae-sequence  subscript  𝑦  𝑖  ⋅  𝕀  𝑖  ℳ  𝒫  subscript  𝑓  𝑖  𝑑  𝑒  𝑐  𝒴  conditional-set  subscript  𝑦  𝑖  𝑖  ℳ  \quad y\_{i}=\mathbb{I}(i\in\mathcal{M})\cdot\mathcal{P}(f\_{i,dec}),\quad\mathcal{Y}=\{y\_{i}&#124;i\in\mathcal{M}\},   |    | (3)   |
|----|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----|-------|

where 𝕀  ( i ∈ ℳ ) 𝕀 𝑖 ℳ \mathbb{I}(i\in\mathcal{M}) is an indicator to only select the predictions corresponding to masked tokens, and 𝒴 𝒴 \mathcal{Y} is the output prediction for the masked frames.

Motion Prediction. Given the output of the target decoder 𝒴 𝒴 \mathcal{Y} , we supervise it with the motion residuals M 𝑀 \mathit{M} . The motion prediction loss ℒ m subscript ℒ 𝑚 \mathcal{L}\_{m} is computed as follows,

|    | ℒ  m  =  1  L  ∑  i  ∈  ℳ  ‖  (  y  i  −  m  i  )  ⋅  c  i  ⋅  c  i  +  k  ‖  2  ,  m  i  ∈  M  ,  c  i  ∈  C  ,  formulae-sequence  subscript  ℒ  𝑚  1  𝐿  subscript  𝑖  ℳ  superscript  norm  ⋅  subscript  𝑦  𝑖  subscript  𝑚  𝑖  subscript  𝑐  𝑖  subscript  𝑐  𝑖  𝑘  2  formulae-sequence  subscript  𝑚  𝑖  𝑀  subscript  𝑐  𝑖  𝐶  \mathcal{L}\_{m}=\frac{1}{L}\sum\_{i\in\mathcal{M}}&#124;&#124;(y\_{i}-m\_{i})\cdot c\_{i}\cdot c\_{i+k}&#124;&#124;^{2},\quad m\_{i}\in\mathit{M},c\_{i}\in\mathit{C},   |    | (4)   |
|----|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----|-------|

where L 𝐿 L is the size of the masked index set ℳ ℳ \mathcal{M} . Since the ground-truth motion residual is inferred from the estimated sign poses, it is pertinent to incorporate the confidence values of the corresponding sign poses into the objective function.

### III-B Momentum Semantic Alignment Module

In MA, our framework aims to reconstruct the partially masked information via the mining remaining sign pose features, which prefers to focus on local motion contexts, without considering the global representation of sign pose sequence.

Thus, we design this module (SA) to endow our framework with global instance discriminability by aligning the semantic features in the shared common space.

In SA, we adopt the same architectures with MA, i.e., the frame-wise embedding layer and the encoder, while incorporating another augmented sequence as input.

As mentioned in MoCo [

[16](#bib.bib16) ] , data augmentation is essential to learn effective global representation. If we preserve complete temporal information in the positive sample, the model could be easily converged to a sub-optimal solution due to the simple pretext task.

To this end, we utilize a temporal augmentation to generate proper positive samples, which not only considers the design of MA, but also avoids the large disparity between different augmented samples to hamper the learning of global comprehensive information.

Considering that the masked strategy in MA preserves less information in the corresponding visible sequence, we utilize a random temporal sampling strategy to make a trade-off between the availability of information and the complexity of data augmentation, which is computed as follows,

|    | V  a  u  g  =  R  a  n  d  o  m  \_  S  a  m  p  l  e  (  V  i  n  ,  α  r  )  ,  subscript  𝑉  𝑎  𝑢  𝑔  𝑅  𝑎  𝑛  𝑑  𝑜  𝑚  \_  𝑆  𝑎  𝑚  𝑝  𝑙  𝑒  subscript  𝑉  𝑖  𝑛  subscript  𝛼  𝑟  \mathit{V}\_{aug}=Random\_Sample(\mathit{V}\_{in},\alpha\_{r}),   |    | (5)   |
|----|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----|-------|

where α r subscript 𝛼 𝑟 \alpha\_{r} denotes the proportion for randomly masking, and V a  u  g subscript 𝑉 𝑎 𝑢 𝑔 \mathit{V}\_{aug} includes ( 1 − α r ) ⋅ T ⋅ 1 subscript 𝛼 𝑟 𝑇 (1-\alpha\_{r})\cdot T frames as the positive sample.

Then, we encode it through a similar pipeline to obtain the corresponding latent feature F e  n  c + superscript subscript 𝐹 𝑒 𝑛 𝑐 \mathit{F}\_{enc}^{+} .

In this way, the latent features of query and its positive key could be obtained from the encoder in MA and SA, which are denoted as F e  n  c subscript 𝐹 𝑒 𝑛 𝑐 \mathit{F}\_{enc} and F e  n  c + superscript subscript 𝐹 𝑒 𝑛 𝑐 \mathit{F}\_{enc}^{+} , respectively.

Next, we extract the global representation of each sample using an average pooling layer.

To better align the representations of positive samples, we further utilize two projection heads to transform them into a shared embedding space, which is computed as follows,

|    | q  𝑞  \displaystyle q                          | =  P  r  o  j  \_  q  (  A  v  g  P  o  o  l  (  F  e  n  c  )  )  ,  absent  𝑃  𝑟  𝑜  𝑗  \_  𝑞  𝐴  𝑣  𝑔  𝑃  𝑜  𝑜  𝑙  subscript  𝐹  𝑒  𝑛  𝑐  \displaystyle=Proj\_q(AvgPool(\mathit{F}\_{enc})),                     |    | (6)   |
|----|------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----|-------|
|    | k  +  superscript  𝑘  \displaystyle\quad k^{+} | =  P  r  o  j  \_  k  (  A  v  g  P  o  o  l  (  F  e  n  c  +  )  )  ,  absent  𝑃  𝑟  𝑜  𝑗  \_  𝑘  𝐴  𝑣  𝑔  𝑃  𝑜  𝑜  𝑙  superscript  subscript  𝐹  𝑒  𝑛  𝑐  \displaystyle=Proj\_k(AvgPool(\mathit{F}\_{enc}^{+})), |    | (7)   |

where q 𝑞 q and k + superscript 𝑘 k^{+} denote the embedding features of query and key samples, respectively. Similarly, the embedding features from other sign pose sequences are considered as negative keys, denoted as k − superscript 𝑘 k^{-} .

Finally, a semantic consistency loss is adopted to force the model to learn invariant instance representation by pulling close the embeddings of the query and positive key generated from different augmented samples and pushing away negative keys from the other sequences.

Similar to MoCo [

[16](#bib.bib16) ] , a memory bank ℬ ℬ \mathcal{B} is utilized to store the key embeddings in each training step in a first-in-first-out (FIFO) manner and provides the negative keys for the next steps.

Based on the above settings, the semantic consistency loss is derived from the InfoNCE loss [

[43](#bib.bib43) ] , which is computed as follows,

|    | ℒ  s  =  −  log  exp  (  q  ⊤  k  +  /  τ  )  exp  (  q  ⊤  k  +  /  τ  )  +  ∑  i  =  1  K  exp  (  q  ⊤  k  i  −  /  τ  )  ,  k  i  −  ∈  ℬ  ,  formulae-sequence  subscript  ℒ  𝑠  log  exp  superscript  𝑞  top  superscript  𝑘  𝜏  exp  superscript  𝑞  top  superscript  𝑘  𝜏  superscript  subscript  𝑖  1  𝐾  exp  superscript  𝑞  top  superscript  subscript  𝑘  𝑖  𝜏  superscript  subscript  𝑘  𝑖  ℬ  \mathcal{L}\_{s}=-\mathrm{log}\frac{\mathrm{exp}(q^{\top}k^{+}/\tau)}{\mathrm{exp}(q^{\top}k^{+}/\tau)+\sum\nolimits\_{i=1}^{K}\mathrm{exp}(q^{\top}k\_{i}^{-}/\tau)},\quad k\_{i}^{-}\in\mathcal{B},   |    | (8)   |
|----|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----|-------|

where τ 𝜏 \tau is the temperature coefficient, and K 𝐾 K is the size of the queue-based memory bank ℬ ℬ \mathcal{B} .

Moreover, we update the parameters of the architectures with the black dashed box in SA by exponential moving average (EMA), as shown in Fig.

[1](#S2.F1) .

For instance, assuming that the parameters of the same modules of two branches denote as θ q subscript 𝜃 𝑞 \theta\_{q} and θ k subscript 𝜃 𝑘 \theta\_{k} , θ k subscript 𝜃 𝑘 \theta\_{k} is updated by θ k ← μ  θ k + ( 1 − μ )  θ q ← subscript 𝜃 𝑘 𝜇 subscript 𝜃 𝑘 1 𝜇 subscript 𝜃 𝑞 \theta\_{k}\leftarrow\mu\theta\_{k}+(1-\mu)\theta\_{q} . The hyper-parameter μ 𝜇 \mu is fixed as 0.996 in our experiment. Momentum update is widely utilized due to its stability during training by fostering smooth feature changes.

### III-C Training Objective

During the pre-training stage, the overall objective is the combination of local motion prediction objective and global semantic consistency objective, which is computed as follows,

|    | ℒ  =  ℒ  m  +  λ  s  ℒ  s  ,  ℒ  subscript  ℒ  𝑚  subscript  𝜆  𝑠  subscript  ℒ  𝑠  \mathcal{L}=\mathcal{L}\_{m}+\lambda\_{s}\mathcal{L}\_{s},   |    | (9)   |
|----|--------------------------------------------------------------------------------------------------------------------------------------------------|----|-------|

where λ s subscript 𝜆 𝑠 \lambda\_{s} is a loss weight controlling the relative influence of both losses. In practice, we utilize a schedule to gradually introduce the global semantic consistency objective and guide the model to learn suitable local feature at the beginning of training.

### III-D Downstream Fine-Tuning

After pre-training, we only utilize the partial pre-training framework, including a frame-wise embedding layer, an encoder and a pooling layer. Then, a simple classifier is attached after them for SLR task. During fine-tuning, we sample the fixed number of frames as input.

We adopt the common

Following [

[19](#bib.bib19) ] , we utilize random and center temporal sampling during training and testing, respectively. In our experiment, we report our results as Ours . Moreover, we utilize a late fusion strategy mentioned in [ [19](#bib.bib19) ] to enhance the RGB-based method with the prediction results of our method, namely Ours (+R).

## IV Experiment

### IV-A Implementation Details

Data Preparation. We utilize sign pose data to represent the hand and body information, which contains 2D pose keypoints extracted from the off-the-shelf estimator MMPose [ [8](#bib.bib8) ] . In each frame, the pose information includes N = 49 𝑁 49 N=49 joints, containing 7 body joints and 42 hand joints with their corresponding confidences.

Parameter Setup. During pre-training stage, the dimension D e subscript 𝐷 𝑒 D\_{e} of frame-wise pose feature is 1536. In MA, the thresholds ϵ c , ϵ m , δ subscript italic-ϵ 𝑐 subscript italic-ϵ 𝑚 𝛿 \epsilon\_{c},\epsilon\_{m},\delta are set to 0.4, 5.0 and 0.5, respectively, and the masked ratio α 𝛼 \alpha is set to 90%. In SA, we randomly mask α r subscript 𝛼 𝑟 \alpha\_{r} 50% of the input sequence. The size K 𝐾 K of the memory bank is set to 6,144, and the temporal coefficient τ 𝜏 \tau is set to 0.07. The loss weight λ s subscript 𝜆 𝑠 \lambda\_{s} is set to 0.05 with a linear increment from zero in the first 100 epochs. We adopt AdamW [ [38](#bib.bib38) ] optimizer as default, and the momentum is set to β 1 = 0.9 subscript 𝛽 1 0.9 \beta\_{1}=0.9 , β 2 = 0.95 subscript 𝛽 2 0.95 \beta\_{2}=0.95 with the weight decay set as 1e-4. The learning rate is set to 1e-4 with a warmup of 20 epochs and linear learning rate decay to train the overall framework for total 400 epochs. During the fine-tuning stage, we utilize the SGD [ [48](#bib.bib48) ] optimizer with 0.9 momentum. The learning rate is initialized to 0.01, then reduced by a factor of 0.1 every 20 epochs. We totally train the framework for 60 epochs with a batch size of 64. Following [ [19](#bib.bib19) ] , we sample 32 frames as input. All experiments are implemented by PyTorch on NVIDIA RTX 3090.

### IV-B Datasets and Metrics

Datasets. We conduct our experiments on four publicly available benchmarks, i.e., WLASL [ [34](#bib.bib34) ] , MSASL [ [26](#bib.bib26) ] , NMFs\_CSL [ [21](#bib.bib21) ] and SLR500 [ [23](#bib.bib23) ] . The entire training sets of all datasets are utilized during the pre-training stage.

WLASL [ [34](#bib.bib34) ] and MSASL [ [26](#bib.bib26) ] are widely utilized American sign language (ASL) datasets. For WLASL, it contains 2000 words performed by over 100 signers, which totally consists of 20,183 samples for training and testing. Particularly, it selects the top- K 𝐾 K most frequent words with K = { 100 , 300 } 𝐾 100 300 K=\{100,300\} and organizes them as its two subsets, named WLASL100 and WLASL300. Similarly, MSASL includes a total of 25,513 samples and a vocabulary size of 1000. It also provides two subsets, named MSASL100 and MSASL200, respectively. Importantly, both datasets collect data from unconstrained real-life scenarios and bring more challenges.

NMFs\_CSL [ [21](#bib.bib21) ] and SLR500 [ [23](#bib.bib23) ] are both Chinese sign language (CSL) datasets. Among them, NMFs\_CSL is a large scale dataset with a vocabulary size of 1067 and 32,010 samples, of which 25,608 and 6,402 samples are split into training and testing, respectively. SLR500 is the largest CSL dataset, which consists of 500 words performed by 50 signers. Concretely, it contains a total of 125,000 samples, of which 90,000 and 35,000 samples are utilized for training and testing, respectively. Different from WLASL and MSASL, both datasets are collected from the lab scene.

Metrics. For evaluation, we report the classification accuracy, i.e., Top-1 ( T-1 ) and Top-5 ( T-5 ) for the SLR task. We also adopt the Per-class ( P-I ) and Per-instance ( P-C ) accuracy metrics following [ [21](#bib.bib21) , [69](#bib.bib69) ] , in which P-I denotes the accuracy of the whole test data, while P-C denotes the average accuracy of the sign categories present in the test data.

### IV-C Comparison with State-of-the-art Methods

In this section, we will compare our proposed method with previous state-of-the-art methods on four public benchmarks. Specifically, we group the previous methods into two categories, i.e., RGB-based and pose-based methods.

WLASL. As depicted in Tab. [II](#S4.T2) , previous supervised methods, i.e., ST-GCN [ [66](#bib.bib66) ] and PSLR [ [58](#bib.bib58) ] show inferior performance compared with RGB-based methods. Although SignBERT [ [19](#bib.bib19) ] and BEST [ [69](#bib.bib69) ] relieve this issue by employing different self-supervised learning strategies, they still neglect some effective information during temporal modeling. Compared with them, our proposed method improves performance attributed to explicitly exploring motion information and inducing global semantic meanings. Specifically, MASA outperforms BEST [ [69](#bib.bib69) ] with 5.81%, 5.99% and 2.81% Top-1 per-instance accuracy improvement on WLASL100, WLASL300 and WLASL2000, respectively. Notably, our method fused with another simple RGB method still surpasses SignBERT (+R) and BEST (+R) with a substantial margin.

MSASL. As shown in Tab. [III](#S4.T3) , the self-supervised methods SignBERT [ [19](#bib.bib19) ] and BEST [ [69](#bib.bib69) ] have validate the feasibility of masked modeling strategies. Compared with them, our method further mines globally discriminative information to enhance sign language representation learning, and achieve better performance with 2.24%, 2.65% and 4.65% Top-1 per-instance accuracy improvement on MSASL100, MSASL200 and MSASL1000, respectively.

NMFs\_CSL. As shown in Tab. [IV](#S4.T4) , NMFs\_CSL dataset contains three different settings, i.e., confusing, normal and total. HMA [ [20](#bib.bib20) ] utilizes a hand statistic model to refine the pose and improve the performance. GLE-Net [ [21](#bib.bib21) ] is the state-of-the-art method with discriminative clues from global and local views under the supervised learning paradigm. Compared with them and previous self-supervised methods [ [19](#bib.bib19) , [69](#bib.bib69) ] , our method still achieves better performance with 71.7% top-1 accuracy.

SLR500. As shown in Tab. [V](#S4.T5) , compared with deep learning methods, STIP [ [31](#bib.bib31) ] and GMM-HMM [ [55](#bib.bib55) ] with hand-craft features show poor performance due to the inferior representations. Among deep learning methods, self-supervised methods [ [19](#bib.bib19) , [69](#bib.bib69) ] learn the powerful capacity of representation learning compared to conventional supervised methods [ [66](#bib.bib66) , [21](#bib.bib21) , [20](#bib.bib20) ] . Compared with them, our method still achieves new state-of-the-art performance.

### IV-D Ablation Study

In this section, we conduct several crucial ablation experiments to validate the effectiveness of our method, For fair comparison, we conduct experiments on the WLASL [ [34](#bib.bib34) ] dataset and its two subsets, named WLASL2000, WLASL300 and WLASL100, respectively.

Different Components. We validate the effectiveness of different components in our proposed method, as shown in Tab. [VIII](#S4.T8) . The MA utilizes a masked modeling strategy to capture motion information among adjacent frames, while the SA aims to learn instance discriminative representation of the intact sign pose sequence via aligning features. Both components endow our model with different temporal perceptions. It is observed that the integrity of both components achieves better performance than adopting any one of them individually, which proves the feasibility of exploring more temporal information for sign language learning.

Different Masked Modeling Strategies. As shown in Tab. [VI](#S4.T6) , the first row denotes the baseline method with random masked strategy and the prevalent objective with predicting static joints of masked frames. It is notable that compared with this baseline, our proposed motion-aware masked strategy and objective bring remarkable performance gain with over 3% accuracy improvement on all subsets of WLASL dataset.

Moreover, the proposed objective shows more effectiveness than the proposed masked strategy, which inclines the importance of explicitly mining dynamic motion cues.

When both designs are utilized, it reaches the best performance, with 6.59%, 6.53% and 5.44% Top-1 per-instance accuracy improvement on WLASL100, WLASL300 and WLASL2000, respectively.

Figure 2: Effect of the data scale during pre-training on WLASL dataset. The horizontal coordinate denotes the data ratio, while the vertical coordinate denotes recognition accuracy.

<!-- image -->

Interval Length k 𝑘 k . In Tab. [VII](#S4.T7) , we further explore the impact of different interval length k 𝑘 k for computing motion residuals between two frames. It is observed that a smaller value leads to the simplification of the model learning, while a larger value makes the model difficult to converge, and ultimately both lead to sub-optimal solutions. Finally, we set k 𝑘 k to 3 as the default setting due to its best performance on WLASL dataset.

Pre-training Data Scale. As shown in Fig. [2](#S4.F2) , we investigate the effect of pre-training data scale. The 0% denotes that our framework directly performs the SLR task without pre-training. It is observed that the performance gradually increases with the increment of pre-training data scale. Importantly, we evenly select the same proportion of data from each dataset. The result validates that our method is suitable for pre-training with large-scale data.

Mask Ratio. We conduct the experiment to investigate the impact of different mask ratio in MA as shown in Tab. [IX](#S4.T9) . The first row denotes that our method directly performs the SLR task without pre-training as a baseline. It is observed that the performance gradually improves as the mask ratio increases. Our framework could adapt to higher mask ratio with our designed mased strategy and effectively models dynamic relations in local regions. Compared with the baseline, our method achieves 83.72%, 73.65% and 49.06% Top-1 per-instance accuracy on WLASL dataset.

Objective Weight. We further research the impact of the objective weight in our proposed method. Considering that semantic consistency loss ℒ s subscript ℒ 𝑠 \mathcal{L}\_{s} as an auxiliary loss aims to endow our model with instance awareness, we select the lower value for this objective. As shown in Tab. [X](#S4.T10) , we find the proper value of hyper-parameter λ s subscript 𝜆 𝑠 \lambda\_{s} as 0.05 based on the performance on WLASL dataset.

Hyper-parameter Sensitivity Analysis. We provide more sensitivity analysis on hyper-parameters in our proposed framework. 1) ϵ c subscript italic-ϵ 𝑐 \epsilon\_{c} is a threshold to truncate low confidence. We observe the estimated poses from MMPose with different confidences from 0.1 to 1.0 and find that the estimated error is beyond the acceptable range when the confidence level is below 0.4, so we set ϵ c subscript italic-ϵ 𝑐 \epsilon\_{c} to 0.4. 2) ϵ m subscript italic-ϵ 𝑚 \epsilon\_{m} is utilized to compute the ratio of keypoints with valid motion. We conduct the experiment on ϵ m subscript italic-ϵ 𝑚 \epsilon\_{m} in the Tab. [XI](#S4.T11) . It is observed that the performance is optimized when ϵ m subscript italic-ϵ 𝑚 \epsilon\_{m} is set to 5. 3) We also conduct the experiment on the threshold δ 𝛿 \delta , as shown in the Tab. [XII](#S4.T12) . The lower threshold introduces more inaccurate motion noise, while the higher threshold truncates some valid motion information. Weighing these reasons, we set the threshold δ 𝛿 \delta as 0.5.

Different Qualities of Input Data. Since our method utilized the pose data extracted from an off-the-shelf human pose estimator, we analyze the sensitivity on the quality of input data. We simulate different qualities of input data by adding Gaussian noise with different intensities σ 𝜎 \sigma to the input skeleton points. The noise is formulated as n = N  ( 0 , 1 ) ∗ σ 𝑛 𝑁 0 1 𝜎 n=N(0,1)*\sigma , where N  ( 0 , 1 ) 𝑁 0 1 N(0,1) denotes the standard normal distribution. The coordinates of the pose data range from -128 to 128. For example, if σ = 10 𝜎 10 \sigma=10 , the average offset caused by noise is roughly ± 20 plus-or-minus 20 \pm 20 . We utilize pose data with different qualities as the input and report the corresponding result in the Tab. [XIII](#S4.T13) . It is observed that as the noise gradually increases, the accuracy gradually decreases. Moreover, if the noise is maintained in a small range, the accuracy does not degrade significantly.

### IV-E Limitation

Our proposed method relies on the detection accuracy of the off-the-shelf pose estimator.

Since the quality of the extracted keypoints of the pose estimator is somewhat sensitive to the video resolution and frame rate, our proposed method possibly shows limited improvement in low-resolution or human-motion blurred scenes.

In particular, the occurrence of mutual occlusion during hand interaction also poses a significant challenge to learn sign language representations.

Although we introduce the pose confidence into our framework to alleviate this dilemma, the representation learning may be potential for improvement with more accurate sign pose data.

In addition, our proposed motion-aware masked autoencoder predicts the movement of the human keypoints at a fixed interval length. However, signers often exhibit different frequencies in sign language videos depending on their personal habitation. Therefore, the motion with a fixed interval length maybe struggle with complex scenarios where motion occurs at multiple scales. In contrast, the multi-scale motion-aware strategy could introduce a more delicate understanding of motion dynamics by incorporating information from multiple temporal scales. Incorporating multi-scale motion-aware strategy is potential for capturing more dynamic cues among sign pose sequences.

## V Conclusion

In this paper, we propose a novel self-supervised pre-training framework, named MASA, to learn more effective sign language representation. MASA consists of two primary components, including a motion-aware masked autoencoder (MA) and a momentum semantic alignment module (SA). In MA, we design a motion-aware masked strategy and an objective function with motion prediction to explicitly mine motion information in sign pose data. Moreover, considering the significance of global semantic meaning in lexical signs, we employ SA to constrain the semantic consistency of positive views by aligning their embeddings in a shared embedding space. Consequently, we fully leverage rich motion cues and global instance discriminativeness to enhance the representative capability of our framework. Extensive experiments are conducted to validate the effectiveness of our proposed framework, resulting in new state-of-the-art performance on four benchmarks.

Despite achieving promising results, there are still some directions worth exploring. 1) Currently, we employ a general-purpose human pose estimator to conveniently acquire sign pose data. However, such estimators typically lack precision in capturing the detailed interacting hand gestures involved in the sign language domain, thereby imposing limitations on the model's representation capacity. Thus, investigating approaches for acquiring high-quality sign language pose data emerges as a meaningful research direction. 2) Compared to explicitly modeling motion information from sparse pose sequences, effectively capturing dynamic cues from informative RGB sign language videos is more efficient and effective in real-world scenarios. Hence, it is also desirable to extend motion-aware self-supervised pre-training to RGB data.

3) Due to the limitations of fixed frame interval length for modeling various motion information, it is also valuable to explore the multi-scale motion-aware strategy with semantic alignment in the sign language domain.

## References

- [1] Nikolas Adaloglou, Theocharis Chatzis, Ilias Papastratis, Andreas Stergioulas, Georgios Th. Papadopoulos, Vassia Zacharopoulou, George J. Xydopoulos, Klimnis Atzakas, Dimitris Papazachariou, and Petros Daras. A comprehensive study on deep learning-based methods for sign language recognition. IEEE Transactions on Multimedia , 24:1750-1762, 2022.
- [2] Samuel Albanie, Gül Varol, Liliane Momeni, Triantafyllos Afouras, Joon Son Chung, Neil Fox, and Andrew Zisserman. BSL-1K: Scaling up co-articulated sign language recognition using mouthing cues. In Proceedings of the European Conference on Computer Vision , pages 35-53, 2020.
- [3] Fabien Baradel, Thibault Groueix, Philippe Weinzaepfel, Romain Bregier, Yannis Kalantidis, and Gregory Rogez. Leveraging mocap data for human mesh recovery. In Proceedings of the International Conference on 3D Vision , pages 586-595, 2021.
- [4] Yunus Can Bilge, Ramazan Gokberk Cinbis, and Nazli Ikizler-Cinbis. Towards zero-shot sign language recognition. IEEE Transactions on Pattern Analysis and Machine Intelligence , 2022.
- [5] Yujun Cai, Liuhao Ge, Jun Liu, Jianfei Cai, Tat-Jen Cham, Junsong Yuan, and Nadia Magnenat Thalmann. Exploiting spatial-temporal relationships for 3D pose estimation via graph convolutional networks. In Proceedings of the IEEE International Conference on Computer Vision , pages 2272-2281, 2019.
- [6] Joao Carreira and Andrew Zisserman. Quo vadis, action recognition? a new model and the kinetics dataset. In Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition , pages 6299-6308, 2017.
- [7] Ting Chen, Simon Kornblith, Mohammad Norouzi, and Geoffrey Hinton. A simple framework for contrastive learning of visual representations. In International Conference on Machine Learning , pages 1597-1607, 2020.
- [8] MMPose Contributors. OpenMMLab pose estimation toolbox and benchmark. [https://github.com/open-mmlab/mmpose](https://github.com/open-mmlab/mmpose) , 2020.
- [9] Jacob Devlin, Ming-Wei Chang, Kenton Lee, and Kristina Toutanova. BERT: Pre-training of deep bidirectional transformers for language understanding. In The North American Chapter of the Association for Computational Linguistics , pages 4171-4186, 2019.
- [10] Yong Du, Wei Wang, and Liang Wang. Hierarchical recurrent neural network for skeleton based action recognition. In Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition , pages 1110-1118, 2015.
- [11] Ali Farhadi, David Forsyth, and Ryan White. Transfer learning in sign language. In Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition , pages 1-8, 2007.
- [12] Holger Fillbrandt, Suat Akyol, and K-F Kraiss. Extraction of 3d hand shape and posture from image sequences for sign language recognition. In Proceedings of the IEEE International SOI Conference , pages 181-186, 2003.
- [13] Spyros Gidaris, Praveer Singh, and Nikos Komodakis. Unsupervised representation learning by predicting image rotations. In Proceedings of the International Conference on Learning Representations , pages 1-16, 2018.
- [14] N. Habili, Cheng Chew Lim, and A. Moini. Segmentation of the face and hands in sign language video sequences using color and motion cues. IEEE Transactions on Circuits and Systems for Video Technology , 14(8):1086-1097, 2004.
- [15] Kaiming He, Xinlei Chen, Saining Xie, Yanghao Li, Piotr Dollár, and Ross Girshick. Masked autoencoders are scalable vision learners. In Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition , pages 16000-16009, 2022.
- [16] Kaiming He, Haoqi Fan, Yuxin Wu, Saining Xie, and Ross Girshick. Momentum contrast for unsupervised visual representation learning. In Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition , pages 9729-9738, 2020.
- [17] Hezhen Hu, Junfu Pu, Wengang Zhou, Hang Fang, and Houqiang Li. Prior-aware cross modality augmentation learning for continuous sign language recognition. IEEE Transactions on Multimedia , 26:593-606, 2024.
- [18] Hezhen Hu, Weichao Zhao, Wengang Zhou, and Houqiang Li. SignBERT+: Hand-model-aware self-supervised pre-training for sign language understanding. IEEE Transactions on Pattern Analysis and Machine Intelligence , 45:11221-11239, 2023.
- [19] Hezhen Hu, Weichao Zhao, Wengang Zhou, Yuechen Wang, and Houqiang Li. SignBERT: pre-training of hand-model-aware representation for sign language recognition. In Proceedings of the IEEE International Conference on Computer Vision , pages 11087-11096, 2021.
- [20] Hezhen Hu, Wengang Zhou, and Houqiang Li. Hand-model-aware sign language recognition. In Proceedings of the AAAI Conference on Artificial Intelligence , volume 35, pages 1558-1566, 2021.
- [21] Hezhen Hu, Wengang Zhou, Junfu Pu, and Houqiang Li. Global-local enhancement network for nmf-aware sign language recognition. ACM Transactions on Multimedia Computing, Communications and Applications , 17(3):1-19, 2021.
- [22] Lianyu Hu, Liqing Gao, Zekang Liu, and Wei Feng. Continuous sign language recognition with correlation network. In Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition , pages 2529-2539, 2023.
- [23] Jie Huang, Wengang Zhou, Houqiang Li, and Weiping Li. Attention-based 3D-CNNs for large-vocabulary sign language recognition. IEEE Transactions on Circuits and Systems for Video Technology , 29(9):2822-2832, 2018.
- [24] Zhicheng Huang, Xiaojie Jin, Chengze Lu, Qibin Hou, Ming-Ming Cheng, Dongmei Fu, Xiaohui Shen, and Jiashi Feng. Contrastive masked autoencoders are stronger vision learners. IEEE Transactions on Pattern Analysis and Machine Intelligence , 46(4):2506-2517, 2024.
- [25] Tao Jiang, Necati Cihan Camgoz, and Richard Bowden. Skeletor: Skeletal transformers for robust body-pose estimation. In Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition , pages 3394-3402, 2021.
- [26] Hamid Reza Vaezi Joze and Oscar Koller. MS-ASL: A large-scale data set and benchmark for understanding american sign language. In Proceedings of the British Machine Vision Conference , pages 1-16, 2019.
- [27] Ahmet Alp Kindiroglu, Ozgur Kara, Ogulcan Ozdemir, and Lale Akarun. Transfer learning for cross-dataset isolated sign language recognition in under-resourced datasets. arxiv , 2024.
- [28] Oscar Koller. Quantitative survey of the state of the art in sign language recognition. arXiv , 2020.
- [29] Oscar Koller, Sepehr Zargaran, Hermann Ney, and Richard Bowden. Deep sign: Enabling robust statistical continuous sign language recognition via hybrid CNN-HMMs. The International Journal of Computer Vision , 126(12):1311-1325, 2018.
- [30] David Laines, Gissella Bejarano, Miguel Gonzalez-Mendoza, and Gilberto Ochoa-Ruiz. Isolated sign language recognition based on tree structure skeleton images. In Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition Workshop , 2023.
- [31] Ivan Laptev. On space-time interest points. The International Journal of Computer Vision , 64(2):107-123, 2005.
- [32] Taeryung Lee, Yeonguk Oh, and Kyoung Mu Lee. Human part-wise 3d motion context learning for sign language recognition. In Proceedings of the IEEE International Conference on Computer Vision , pages 20740-20750, 2023.
- [33] Chao Li, Qiaoyong Zhong, Di Xie, and Shiliang Pu. Co-occurrence feature learning from skeleton data for action recognition and detection with hierarchical aggregation. In Proceedings of the International Joint Conferences on Artificial Intelligence , pages 786-792, 2018.
- [34] Dongxu Li, Cristian Rodriguez, Xin Yu, and Hongdong Li. Word-level deep sign language recognition from video: A new large-scale dataset and methods comparison. In Proceedings of the IEEE Winter Conference on Applications of Computer Vision , pages 1459-1469, 2020.
- [35] Dongxu Li, Xin Yu, Chenchen Xu, Lars Petersson, and Hongdong Li. Transferring cross-domain knowledge for video sign language recognition. In Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition , pages 6205-6214, 2020.
- [36] Yuwei Liang, Weijie Li, Yue Wang, Rong Xiong, Yichao Mao, and Jiafan Zhang. Dynamic movement primitive based motion retargeting for dual-arm sign language motions. In IEEE International Conference on Robotics and Automation , pages 8195-8201, 2021.
- [37] Ji Lin, Chuang Gan, and Song Han. TSM: Temporal shift module for efficient video understanding. In Proceedings of the IEEE International Conference on Computer Vision , pages 7083-7093, 2019.
- [38] Ilya Loshchilov and Frank Hutter. Decoupled weight decay regularization. In Proceedings of the International Conference on Learning Representations , pages 1-19, 2018.
- [39] Yunyao Mao, Jiajun Deng, Wengang Zhou, Yao Fang, Wanli Ouyang, and Houqiang Li. Masked motion predictors are strong 3d action representation learners. In Proceedings of the IEEE International Conference on Computer Vision , pages 10181-10191, 2023.
- [40] Evonne Ng, Shiry Ginosar, Trevor Darrell, and Hanbyul Joo. Body2hands: Learning to infer 3D hands from conversational gesture body dynamics. In Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition , pages 11865-11874, 2021.
- [41] Mehdi Noroozi and Paolo Favaro. Unsupervised learning of visual representations by solving jigsaw puzzles. In Proceedings of the European Conference on Computer Vision , pages 69-84, 2016.
- [42] Mehdi Noroozi, Ananth Vinjimoor, Paolo Favaro, and Hamed Pirsiavash. Boosting self-supervised learning via knowledge transfer. In Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition , pages 9359-9367, 2018.
- [43] Aaron van den Oord, Yazhe Li, and Oriol Vinyals. Representation learning with contrastive predictive coding. arXiv , 2018.
- [44] Tian Pan, Yibing Song, Tianyu Yang, Wenhao Jiang, and Wei Liu. Videomoco: Contrastive video representation learning with temporally adversarial examples. In Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition , pages 11205-11214, 2021.
- [45] Rui Qian, Tianjian Meng, Boqing Gong, Ming-Hsuan Yang, Huisheng Wang, Serge Belongie, and Yin Cui. Spatiotemporal contrastive video representation learning. In Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition , pages 6964-6974, 2021.
- [46] Zhaofan Qiu, Ting Yao, and Tao Mei. Learning spatio-temporal representation with pseudo-3D residual networks. In Proceedings of the IEEE International Conference on Computer Vision , pages 5533-5541, 2017.
- [47] Razieh Rastgoo, Kourosh Kiani, and Sergio Escalera. Sign language recognition: A deep survey. Expert Systems with Applications , 164:113794, 2021.
- [48] Herbert Robbins and Sutton Monro. A stochastic approximation method. The annals of mathematical statistics , pages 400-407, 1951.
- [49] Noha Sarhan and Simone Frintrop. Unraveling a decade: A comprehensive survey on isolated sign language recognition. In Proceedings of the IEEE International Conference on Computer Vision , pages 3210-3219, 2023.
- [50] Ben Saunders, Necati Cihan Camgoz, and Richard Bowden. Mixed SIGNals: Sign language production via a mixture of motion primitives. In Proceedings of the IEEE International Conference on Computer Vision , pages 1919-1929, 2021.
- [51] Prem Selvaraj, Gokul Nc, Pratyush Kumar, and Mitesh Khapra. OpenHands: Making sign language recognition accessible with pose-based pretrained models across languages. In Annual Meeting of the Association for Computational Linguistics , pages 2114-2133, 2022.
- [52] Ozge Mercanoglu Sincan and Hacer Yalim Keles. AUTSL: A large scale multi-modal turkish sign language dataset and baseline methods. IEEE Access , 8:181340-181355, 2020.
- [53] Ozge Mercanoglu Sincan and Hacer Yalim Keles. Using motion history images with 3d convolutional networks in isolated sign language recognition. IEEE Access , 10:18608-18618, 2022.
- [54] Thad E Starner. Visual recognition of american sign language using hidden markov models. Technical report, Massachusetts inst of tech Cambridge dept of brain and cognitive sciences, 1995.
- [55] Ao Tang, Ke Lu, Yufei Wang, Jie Huang, and Houqiang Li. A real-time hand posture recognition system using deep neural networks. ACM Transactions on Intelligent Systems and Technology , 6(2):1-23, 2015.
- [56] Chenxin Tao, Xizhfou Zhu, Gao Huang, Yu Qiao, Xiaogang Wang, and Jifeng Dai. Siamese image modeling for self-supervised vision representation learning. Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition , pages 2132-2141, 2022.
- [57] Zhan Tong, Yibing Song, Jue Wang, and Limin Wang. VideoMAE: Masked autoencoders are data-efficient learners for self-supervised video pre-training. In Proceedings of the Advances in Neural Information Processing Systems , pages 10078-10093, 2022.
- [58] Anirudh Tunga, Sai Vidyaranya Nuthalapati, and Juan Wachs. Pose-based sign language recognition using GCN and BERT. In Proceedings of the IEEE Winter Conference on Applications of Computer Vision , pages 31-40, 2021.
- [59] Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N Gomez, Łukasz Kaiser, and Illia Polosukhin. Attention is all you need. In Proceedings of the Advances in Neural Information Processing Systems , pages 1-11, 2017.
- [60] Hanjie Wang, Xiujuan Chai, and Xilin Chen. A novel sign language recognition framework using hierarchical grassmann covariance matrix. IEEE Transactions on Multimedia , 21:2806-2814, 2019.
- [61] Li-Chun Wang, Ru Wang, De-Hui Kong, and Bao-Cai Yin. Similarity assessment model for chinese sign language videos. IEEE Transactions on Multimedia , 16:751-761, 2014.
- [62] Xiang Wang, Shiwei Zhang, Zhiwu Qing, Changxin Gao, Yingya Zhang, Deli Zhao, and Nong Sang. MoLo: Motion-augmented long-short contrastive learning for few-shot action recognition. In Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition , pages 18011-18021, 2023.
- [63] Chengcheng Wei, Jian Zhao, Wengang Zhou, and Houqiang Li. Semantic boundary detection with reinforcement learning for continuous sign language recognition. IEEE Transactions on Circuits and Systems for Video Technology , 31(3):1138-1149, 2021.
- [64] Pan Xie, Mengyi Zhao, and Xiaohui Hu. PiSLTRc: Position-informed sign language transformer with content-aware convolution. IEEE Transactions on Multimedia , 24:3908-3919, 2022.
- [65] Saining Xie, Chen Sun, Jonathan Huang, Zhuowen Tu, and Kevin Murphy. Rethinking spatiotemporal feature learning: Speed-accuracy trade-offs in video classification. In Proceedings of the European Conference on Computer Vision , pages 305-321, 2018.
- [66] Sijie Yan, Yuanjun Xiong, and Dahua Lin. Spatial temporal graph convolutional networks for skeleton-based action recognition. In Proceedings of the AAAI Conference on Artificial Intelligence , pages 7444-7452, 2018.
- [67] Wenjie Yin, Yonghong Hou, Zihui Guo, and Kailin Liu. Spatial temporal enhanced network for continuous sign language recognition. IEEE Transactions on Circuits and Systems for Video Technology , 34(3):1684-1695, 2024.
- [68] Richard Zhang, Phillip Isola, and Alexei A Efros. Colorful image colorization. In Proceedings of the European Conference on Computer Vision , pages 649-666, 2016.
- [69] Weichao Zhao, Hezhen Hu, Wengang Zhou, Jiaxin Shi, and Houqiang Li. BEST: Bert pre-training for sign language recognition with coupling tokenization. Proceedings of the AAAI Conference on Artificial Intelligence , pages 3597-3605, 2023.
- [70] Jinghao Zhou, Chen Wei, Huiyu Wang, Wei Shen, Cihang Xie, Alan Yuille, and Tao Kong. iBOT: Image bert pre-training with online tokenizer. In Proceedings of the International Conference on Learning Representations , pages 1-29, 2021.
- [71] Wentao Zhu, Xiaoxuan Ma, Zhaoyang Liu, Libin Liu, Wayne Wu, and Yizhou Wang. MotionBERT: Unified pretraining for human motion analysis. arXiv , 2022.
- [72] Ronglai Zuo, Fangyun Wei, and Brian Mak. Natural language-assisted sign language recognition. In Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition , pages 14890-14900, 2023.

[Uncaptioned image]

<!-- image -->

[Uncaptioned image]

<!-- image -->

[Uncaptioned image]

<!-- image -->

[Uncaptioned image]

<!-- image -->

[Uncaptioned image]

<!-- image -->

[Uncaptioned image]

<!-- image -->

## References

- [[be750a466fb5db670c3d4e99616a0b6c28fe267d]] — Transfer Learning for Cross-Dataset Isolated Sign Language Recognition in Under-Resourced Datasets (2024)
- [[22f53e185955378702b5fdba4282fba96c8d7f50]] — Spatial–Temporal Enhanced Network for Continuous Sign Language Recognition (2024)
- [[2a60ea36fd8d9c95a745c4fb0d0c4607746ca0d7]] — Unraveling a Decade: A Comprehensive Survey on Isolated Sign Language Recognition (2023)
- [[41caef8b6ce66be41ac43b7cae3e4a4eaa4cc888]] — Human Part-wise 3D Motion Context Learning for Sign Language Recognition (2023)
- [[94a307c64fe0b49b2e019dfb6241aee78d9379f7]] — Masked Motion Predictors are Strong 3D Action Representation Learners (2023)
- [[0fcc797aeed56bcc127476d5b68836dc402021ea]] — SignBERT+: Hand-Model-Aware Self-Supervised Pre-Training for Sign Language Understanding (2023)
- [[d0766bbe13a8ebdca17ec2afad4eaef15407d894]] — Isolated Sign Language Recognition based on Tree Structure Skeleton Images (2023)
- [[1b5813dc183818457bb25b90c67d9544b50b01a7]] — MoLo: Motion-Augmented Long-Short Contrastive Learning for Few-Shot Action Recognition (2023)
- [[6648bbbb7ad41397d315d1c83ac02a39ac875b19]] — Natural Language-Assisted Sign Language Recognition (2023)
- [[d9c38e7957c10252cc0e66b20c55d5be615db10d]] — Continuous Sign Language Recognition with Correlation Network (2023)
- [[919efc30ab8c45456ab72fb4ebeb5e25f2ad7642]] — BEST: BERT Pre-Training for Sign Language Recognition with Coupling Tokenization (2023)
- [[8b56eec0ffdd4ead040e3af7a5fef2069a57dbdd]] — Contrastive Masked Autoencoders are Stronger Vision Learners (2022)
- [[a2c5e2f70e6441430cf48232da815e0d00653467]] — Siamese Image Modeling for Self-Supervised Vision Representation Learning (2022)
- [[4990f7542f0600e0501a7e7a931b32eb7cb804d5]] — VideoMAE: Masked Autoencoders are Data-Efficient Learners for Self-Supervised Video Pre-Training (2022)
- [[c6d2d950b64973f1bec3b0dd0ed46fbf0319351d]] — Towards Zero-Shot Sign Language Recognition (2022)
- [[9653c070724e44f023e8cc3ec79f0b9e6d59480d]] — iBOT: Image BERT Pre-Training with Online Tokenizer (2021)
- [[6351ebb4a3287f5f3e1273464b3b91e5df5a16d7]] — Masked Autoencoders Are Scalable Vision Learners (2021)
- [[4661b8373ad6de37124854c39e0d88839ca31c15]] — Using Motion History Images With 3D Convolutional Networks in Isolated Sign Language Recognition (2021)
- [[b5036eaf51e797ea0f2a6342c988f87d810dff45]] — Leveraging MoCap Data for Human Mesh Recovery (2021)
- [[2dc5bd35be89eaa336384a3b8cd4b611485c1602]] — OpenHands: Making Sign Language Recognition Accessible with Pose-based Pretrained Models across Languages (2021)
- [[39c6076a1284324282d6234c033ef1539c959039]] — SignBERT: Pre-Training of Hand-Model-Aware Representation for Sign Language Recognition (2021)
- [[87e823d2cb58e741230c0fa3b83f3459c7e32241]] — PiSLTRc: Position-Informed Sign Language Transformer With Content-Aware Convolution (2021)
- [[e056206d93c646de4d32041238f44cb16b929a27]] — Mixed SIGNals: Sign Language Production via a Mixture of Motion Primitives (2021)
- [[832298578168aacc3fb1433296a63dbfa849ee4e]] — Hand-Model-Aware Sign Language Recognition (2021)
- [[82debd146c2351ec37ef2f6b51ca7fb04244d527]] — Skeletor: Skeletal Transformers for Robust Body-Pose Estimation (2021)
- [[0536805fe0f9b621dcdbd90ccf34b6b1387cfa3c]] — A Comprehensive Study on Deep Learning-Based Methods for Sign Language Recognition (2021)
- [[e56a3dc015d18421a7ce35eaa4d5513d953df6c7]] — VideoMoCo: Contrastive Video Representation Learning with Temporally Adversarial Examples (2021)
- [[06aa3a4d61b2856c39789cfeb3a5065db189e63c]] — Semantic Boundary Detection With Reinforcement Learning for Continuous Sign Language Recognition (2021)
- [[d10cb838533c33aad406a4ad3dc515113f7155b3]] — Sign Language Recognition: A Deep Survey (2021)
- [[2e0d7289231dc4b1cd822186690b426810da620b]] — Pose-based Sign Language Recognition using GCN and BERT (2020)
- [[2be4aeb9f174d415b1192770b654bb6a72536f6f]] — Dynamic Movement Primitive based Motion Retargeting for Dual-Arm Sign Language Motions (2020)
- [[9023437b9bfb741094f9ff50323093573c9f8e60]] — Global-Local Enhancement Network for NMF-Aware Sign Language Recognition (2020)
- [[5b8ec500aedc97cc9874a9eb601cef37c5f38e3f]] — Quantitative Survey of the State of the Art in Sign Language Recognition (2020)
- [[322a79919356c4c107e20e46e4bde3ce000b67b7]] — Spatiotemporal Contrastive Video Representation Learning (2020)
- [[14cc503211af3ba271e0ebee622e0439c693793f]] — AUTSL: A Large Scale Multi-Modal Turkish Sign Language Dataset and Baseline Methods (2020)
- [[a1384c31c9b2780eee16b1ef6bb66cfdeac88cf1]] — Body2Hands: Learning to Infer 3D Hands from Conversational Gesture Body Dynamics (2020)
- [[fe6c2b21f6086c375f4e211efb6c4d6479d54f01]] — BSL-1K: Scaling up co-articulated sign language recognition using mouthing cues (2020)
- [[efe28238909dc5c1877297fa830d85e9daecc29f]] — Transferring Cross-Domain Knowledge for Video Sign Language Recognition (2020)
- [[7af72a461ed7cda180e7eab878efd5f35d79bbf4]] — A Simple Framework for Contrastive Learning of Visual Representations (2020)
- [[add2f205338d70e10ce5e686df4a690e2851bdfc]] — Momentum Contrast for Unsupervised Visual Representation Learning (2019)
- [[874063b6c71aef8382eb66a66d8a1c1188e78a9a]] — Word-level Deep Sign Language Recognition from Video: A New Large-scale Dataset and Methods Comparison (2019)
- [[50167a9e6bdc1f64a58fe8a3c990105fec0bd2bc]] — Exploiting Spatial-Temporal Relationships for 3D Pose Estimation via Graph Convolutional Networks (2019)
- [[91a8da0d5429b0be63b2495587908d4583931ab5]] — Attention-Based 3D-CNNs for Large-Vocabulary Sign Language Recognition (2019)
- [[33a4f68e9cec8f76213b0a7f8c704651344553e1]] — A Novel Sign Language Recognition Framework Using Hierarchical Grassmann Covariance Matrix (2019)
- [[310a8e2c9f2650fa2e44fdf0d82d11c0cb3e387e]] — MS-ASL: A Large-Scale Data Set and Benchmark for Understanding American Sign Language (2018)
- [[4bbfd46721c145852e443ae4aad35148b814bf91]] — TSM: Temporal Shift Module for Efficient Video Understanding (2018)
- [[38f6ad09484b7fd3017ff255d86f0cc64bbb8be3]] — Deep Sign: Enabling Robust Statistical Continuous Sign Language Recognition via Hybrid CNN-HMMs (2018)
- [[b227f3e4c0dc96e5ac5426b85485a70f2175a205]] — Representation Learning with Contrastive Predictive Coding (2018)
- [[2a1f38e4451e826e01c9874954ba7c6f32ff79f4]] — Boosting Self-Supervised Learning via Knowledge Transfer (2018)
- [[1b10e59adfa3f0f7748f48e2e64e54db2a5362d3]] — Co-occurrence Feature Learning from Skeleton Data for Action Recognition and Detection with Hierarchical Aggregation (2018)
- [[aab368284210c1bb917ec2d31b84588e3d2d7eb4]] — Unsupervised Representation Learning by Predicting Image Rotations (2018)
- [[efeaa6e3114d6d6ae5c3041b66ac9a9ae9bf52bf]] — Spatial Temporal Graph Convolutional Networks for Skeleton-Based Action Recognition (2018)
- [[815aa52cfc02961d82415f080384594639a21984]] — Rethinking Spatiotemporal Feature Learning: Speed-Accuracy Trade-offs in Video Classification (2017)
- [[d07284a6811f1b2745d91bdb06b040b57f226882]] — Decoupled Weight Decay Regularization (2017)
- [[024d037d46ae933c7e12fd16af61953c7161773a]] — Learning Spatio-Temporal Representation with Pseudo-3D Residual Networks (2017)
- [[204e3073870fae3d05bcbc2f6a8e263d9b72e776]] — Attention is All you Need (2017)
- [[b61a3f8b80bbd44f24544dc915f52fd30bbdf485]] — Quo Vadis, Action Recognition? A New Model and the Kinetics Dataset (2017)
- [[2ec8f7e0257a07d3914322b36072d1bbcd58a1e0]] — Unsupervised Learning of Visual Representations by Solving Jigsaw Puzzles (2016)
- [[8201e6e687f2de477258e9be53ba7b73ee30d7de]] — Colorful Image Colorization (2016)
- [[1839e17555160bd897b978c48b8ebd13dd21445f]] — Hierarchical recurrent neural network for skeleton based action recognition (2015)
- [[e237ec3e50c7681c6b88b2ab481c15e62b61f154]] — A Real-Time Hand Posture Recognition System Using Deep Neural Networks (2015)
- [[e0386991589ca9b95d6d366dfc26f04d7d5cf244]] — Similarity Assessment Model for Chinese Sign Language Videos (2014)
- [[fd357c773c5531b35d9050fcb066fdd35211611f]] — Transfer Learning in Sign language (2007)
- [[39dc218eb5582e861e53c8451586786cfaca08ec]] — On Space-Time Interest Points (2005)
- [[fc9df52cbaf20abfa1aa5f3512c58e0aeb1817b5]] — Segmentation of the face and hands in sign language video sequences using color and motion cues (2004)
- [[6531af2f185261962b47a008633ea7939add6575]] — Extraction of 3D hand shape and posture from image sequences for sign language recognition (2003)
- [[aad4d4fa0fd053d6ba5a0aece8e5461cc82f4631]] — Circuits (1995)
- [[0b9712ad56c6821cfe05ba5ddeb22a71000397d4]] — Visual Recognition of American Sign Language Using Hidden Markov Models. (1995)
- [[34ddd8865569c2c32dec9bf7ffc817ff42faaa01]] — A Stochastic Approximation Method (1951)
- [[39d8926d911033e2f9a4702c3f446f04fb887e97]] — Prior-Aware Cross Modality Augmentation Learning for Continuous Sign Language Recognition (2024)
- [[38954991359cb73a2ad3074d9c30b4b4d6136869]] — MotionBERT: Unified Pretraining for Human Motion Analysis (2022)
- MMPose Contributors (2020)
- [[df2b0e26d0599ce3e70df8a9da02e51594e0e992]] — BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding (2019)

## Cited by

- [[f510d2a4373457be411ac9afbb8eda2162068b8b]] — Local attention and contrastive clustering network for sign language recognition (2026)
- [[5100b81c3d280e4946794c9b6317484d679dc717]] — WholeBodyPose: a unified end-to-end framework for sign language recognition and pose-based training data (2026)
- [[e31e7e62721c975c984f1cf42c8c01edde10048e]] — MaDiS: Taming Masked Diffusion Language Models for Sign Language Generation (2026)
- [[2321b0bfa6e1b71f2658b4f7f6b9451104e5e37a]] — An Intelligent Cross-Platform System for Indian Sign Language Translation (2026)
- [[f04c8132e79f326550659af7e013ee80a44737d0]] — YogaMesher: A Human Mesh Estimation System for Challenging Poses (2025)
- [[02f3a9def4cd3a6d37adc3d7e3dc546b7ba966e4]] — Boundary-Aware Sentence-Gloss Alignment With Semantic Similarity Measurement for Continuous Sign Language Recognition (2025)
- [[34478b44af33279d9b68593824c5c6b7e610df73]] — Pose Landmark-Based Transformer Model for Mizo Hand Sign Language Detection with Attention Fusion (2025)
- [[083af847b026105bdaf93dbfc1824548ba456286]] — MSE-GCN: A Multiscale Spatiotemporal Feature Aggregation Enhanced Efficient Graph Convolutional Network for Dynamic Sign Language Recognition (2025)
- [[d01d31d088115fc3414dc6ca7713e0dd753f4374]] — Ensemble Transformer-based Word-Level Sign Language Recognition with Multi-Modal Input Fusion (2025)
- [[4dc90e257b95041ac55e06b6f660e640a329c153]] — VSNet: Focusing on the Linguistic Characteristics of Sign Language (2025)
- [[1c64d637df28968198a17c050e56ec6c90163aeb]] — Hand-Aware Masked Graph Convolutional Network for Skeleton-based Sign Language Recognition (2025)
- [[a8c6a56004374a06916a27c6c6b96f1944950f7e]] — A Comprehensive Approach to Indian Sign Language Recognition: Leveraging LSTM and MediaPipe Holistic for Dynamic and Static Hand Gesture Recognition (2025)
- [[32dcca67aa77fd57db31869fe8a52cccd411e41e]] — Generative Sign-Description Prompts with Multi-Positive Contrastive Learning for Sign Language Recognition (2025)
- [[8c03f00bf00051c63c884ad183e466e37a9ac0db]] — YOLOv8-G2F: A portable gesture recognition optimization algorithm (2025)
- [[07f6df57145a79c75a81111567d1583ccb7e74ab]] — Cross-Modal Consistency Learning for Sign Language Recognition (2025)
- [[5171a33d1b066318e47540ea0290a8fe24946f93]] — Uni-Sign: Toward Unified Sign Language Understanding at Scale (2025)
- [[4b136194acd56d8e7c89406da4539f7a129c4ef3]] — HandWave: A Convolutional Model for Indian Sign Language Recognition: A Deep Learning Approach (2024)
- [[1ffb51c115fd904f8ca2a080c8247711fe0780a8]] — Signs as Tokens: A Retrieval-Enhanced Multilingual Sign Language Generator (2024)
- [[5376d565e85d753c9a2734c930d35965efc53e47]] — A lightweight network-based sign language robot with facial mirroring and speech system (2024)
- [[4de028b7c31e24d6e5dff73b3d51ee4e585de939]] — C2RL: Content and Context Representation Learning for Gloss-Free Sign Language Translation and Retrieval (2024)
- [[8247c7a67e4e3e526cee10ca9499b1936204e79c]] — Scaling up Multimodal Pre-Training for Sign Language Understanding (2024)
- [[0d6b78072220375678f48e7fa53a0c96ec15fff4]] — Self-Supervised Representation Learning With Spatial-Temporal Consistency for Sign Language Recognition (2024)
- [[72e055c4b88f26fff181e9dba38ef9c74429dc5b]] — SMC++: Masked Learning of Unsupervised Video Semantic Compression (2024)
- [[362acfcca587a26a12e7a8b3143d3cbb5e107db0]] — M³-SLR: Self-Supervised Pretraining With MaxFlow MaskFeat for Improved Multi-View Sign Language Representation (2025)
- [[16219053ced3539ba9a0bb7bc6532d4ae4eaec6a]] — S2Net: Skeleton-Aware SlowFast Network for Efficient Sign Language Recognition (2022)
- [[49f2b48387b5ecdf5f70fd86dd57afe3722b4ea9]] — MBTI: Masked Blending Transformers with Implicit Positional Encoding for Frame-rate Agnostic Motion Estimation ()
- [[23a3bd4d6c3c10becdc9f86ab22948cbde717b10]] — S IGMA : S EMANTICALLY I NFORMATIVE P RE - TRAINING FOR S KELETON - BASED S IGN L ANGUAGE U NDER - STANDING (U NDER REVIEW ) ()

## Sources

- title: semanticscholar
- abstract: semanticscholar
- authors: semanticscholar
- topics: semanticscholar
- references: semanticscholar
- citations: semanticscholar
- fullText: ar5iv
- bibtex: semanticscholar

---
semanticScholarId: "57540be21cfeea3f5a65a1debcdf5416d6eb0fa4"
bibKey: null
year: 2026
title: "HATL: Hierarchical Adaptive-Transfer Learning Framework for Sign Language Machine Translation"
doi: null
arxivId: "2603.19260"
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

# HATL: Hierarchical Adaptive-Transfer Learning Framework for Sign Language Machine Translation

**Year:** [[2026]]
**Topics:** [[topics/computer-science|Computer Science]], [[topics/linguistics|Linguistics]]
**Authors:** Nada Shahin; Leila Ismail

## Links
- [Semantic Scholar](https://www.semanticscholar.org/paper/57540be21cfeea3f5a65a1debcdf5416d6eb0fa4)
- [arXiv:2603.19260](https://arxiv.org/abs/2603.19260)

## Abstract

Sign Language Machine Translation (SLMT) aims to bridge communication between Deaf and hearing individuals. However, its progress is constrained by scarce datasets, limited signer diversity, and large domain gaps between sign motion patterns and pretrained representations. Existing transfer learning approaches in SLMT are static and often lead to overfitting. These challenges call for the development of an adaptive framework that preserves pretrained structure while remaining robust across linguistic and signing variations. To fill this void, we propose a Hierarchical Adaptive Transfer Learning (HATL) framework, where pretrained layers are progressively and dynamically unfrozen based on training performance behavior. HATL combines dynamic unfreezing, layer-wise learning rate decay, and stability mechanisms to preserve generic representations while adapting to sign characteristics. We evaluate HATL on Sign2Text and Sign2Gloss2Text translation tasks using a pretrained ST-GCN++ backbone for feature extraction and the Transformer and an adaptive transformer (ADAT)for translation. To ensure robust multilingual generalization, we evaluate the proposed approach across three datasets: RWTH-PHOENIXWeather-2014 (PHOENIX14T), Isharah, and MedASL. Experimental results show that HATL consistently outperforms traditional transfer learning approaches across tasks and models, with ADAT achieving BLEU-4 improvements of 15.0% on PHOENIX14T and Isharah and 37.6% on MedASL.

## TL;DR

Experimental results show that HATL consistently outperforms traditional transfer learning approaches across tasks and models, with ADAT achieving BLEU-4 improvements of 15.0% on PHOENIX14T and Isharah and 37.6% on MedASL.

## BibTeX

```bibtex
@Inproceedings{Shahin2026HATLHA,
 author = {Nada Shahin and Leila Ismail},
 title = {HATL: Hierarchical Adaptive-Transfer Learning Framework for Sign Language Machine Translation},
 year = {2026}
}
```

## Full Text

# HATL: Hierarchical Adaptive-Transfer Learning Framework for Sign Language Machine Translation

Nada Shahin 1,2 and Leila Ismail 1,2 Corresponding author: Leila Ismail ( leila@uaeu.ac.ae ).

###### Abstract

Sign Language Machine Translation (SLMT) aims to bridge communication between Deaf and hearing individuals. However, its progress is constrained by scarce datasets, limited signer diversity, and large domain gaps between sign motion patterns and pretrained representations. Existing transfer learning approaches in SLMT are static and often lead to overfitting. These challenges call for the development of an adaptive framework that preserves pretrained structure while remaining robust across linguistic and signing variations. To fill this void, we propose a Hierarchical Adaptive Transfer Learning (HATL) framework, where pretrained layers are progressively and dynamically unfrozen based on training performance behavior. HATL combines dynamic unfreezing, layer-wise learning rate decay, and stability mechanisms to preserve generic representations while adapting to sign characteristics. We evaluate HATL on Sign2Text and Sign2Gloss2Text translation tasks using a pretrained ST-GCN++ backbone for feature extraction and the Transformer and an adaptive transformer (ADAT) for translation. To ensure robust multilingual generalization, we evaluate the proposed approach across three datasets: RWTH-PHOENIX-Weather-2014 (PHOENIX14T), Isharah, and MedASL. Experimental results show that HATL consistently outperforms traditional transfer learning approaches across tasks and models, with ADAT achieving BLEU-4 improvements of 15.0% on PHOENIX14T and Isharah and 37.6% on MedASL.

1 Intelligent Distributed Computing and Systems (INDUCE) Lab, Department of Computer Science and Software Engineering, College of Information Technology, United Arab Emirates University, Abu Dhabi 15551, United Arab Emirates 2 Emirates Center for Mobility Research, United Arab Emirates University, Abu Dhabi 15551, United Arab Emirates

Keywords- Artificial Intelligence, Computer Vision, Low-Resource Learning, Natural Language Processing, Neural Machine Translation, Neural Network, Sign Language Translation, Transfer Learning, Transformers.

## 1 INTRODUCTION

Sign languages are the primary communication method for Deaf and hard-of-hearing (DHH) communities worldwide. These languages follow syntactic and grammatical structures that differ from spoken languages [ [14](#bib.bib2) ] . This creates a growing need for Sign Language Machine Translation (SLMT) systems that support seamless communication between DHH and hearing individuals. Such technologies are critical in settings where human interpreters are unavailable. However, the development of SLMT systems is constrained by the scarcity of high-quality datasets, which are often limited in sample size, signer diversity, and annotation quality [ [6](#bib.bib3) , [10](#bib.bib4) ] . Therefore, artificial intelligence (AI) models trained on sign language data tend to overfit and generalize poorly, as discussed in [ [28](#bib.bib5) , [30](#bib.bib51) ] , establishing SLMT as a low-resource visual domain [ [15](#bib.bib6) , [3](#bib.bib7) ] . To overcome these limitations, recent research has adopted transfer learning to improve generalization, mitigate overfitting, and reduce the need for resource-intensive data collection [ [16](#bib.bib10) ] .

Transfer learning is categorized into three types: 1) inductive, where knowledge is transferred from one domain to a related one; 2) transductive, where the domain is identical but labeled data is available only in the pretrained domain; and 3) unsupervised, where models rely on shared representations without labeled data [ [16](#bib.bib10) , [23](#bib.bib11) ] . Among these, inductive transfer learning is the most suitable for SLMT. This is because it reuses general motion representations that were pretrained in related visual domains such as action recognition [ [15](#bib.bib6) ] .

Large-scale inductive transfer learning has substantially improved performance in computer vision [ [22](#bib.bib12) , [34](#bib.bib13) , [35](#bib.bib14) , [31](#bib.bib15) ] , language understanding [ [32](#bib.bib16) ] , and speech processing [ [1](#bib.bib17) , [8](#bib.bib18) ] . However, these advances are constrained by the high computational cost, the risk of negative transfer when feature distributions diverge, and the difficulty in balancing model capacity with limited data. These challenges are particularly pronounced in SLMT, where data scarcity and domain gaps restrict effective model adaptation. Moreover, sign language exhibits fine-grained spatial and temporal patterns, such as handshapes and non-manual signals, that differ from those in typical video domains, such as action recognition.

Pretrained motion models encode a hierarchical structure that captures generic motion cues, temporal dependencies, and semantic information. In low-resource settings, such as SLMT, directly adapting these models by fine-tuning all parameters simultaneously can disrupt this hierarchy, as pretrained features are overwritten before the model converges. In contrast, limiting the extent to which the parameters can adapt prevents the capture of the linguistic and motion properties of the sign language. To mitigate these issues, existing approaches rely on manually unfreezing a fixed subset of pretrained layers. This selection is dataset-dependent, as the optimal set of activated layers varies with dataset scale and domain characteristics. As a result, generalization to unseen signers, sentences, and motion variations across SLMT datasets is limited [ [16](#bib.bib10) , [23](#bib.bib11) ] . In this paper, we fill this void by introducing a novel Hierarchical Adaptive Transfer Learning (HATL) framework to improve adaptation stability and generalization in SLMT. HATL increases trainable capacity to gradually align more pretrained layers with sign language dynamics. This design provides a dynamic transfer mechanism that addresses overfitting and enables reliable adaptation to sign language.

We divide SLMT into two categories: 1) Sign2Text, where sign videos are translated directly into spoken language text, and 2) Sign2Gloss2Text, which relies on gloss annotations, i.e., written sign representations, during translation. We evaluate HATL performance within these categories based on VisioSLR stages, an end-to-end framework for sign language recognition [ [18](#bib.bib39) ] . We use a pretrained Spatio-Temporal Graph Convolutional Network (ST-GCN++) [ [9](#bib.bib57) ] for feature extraction and two translation models: the standard Transformer [ [33](#bib.bib26) ] and ADAT, an adaptive transformer-based model designed to capture the temporal nature of sign language sequences [ [30](#bib.bib51) ] . We compare these models against two transfer learning approaches: 1) classical fine-tuning, where only the translation model is trained, and 2) full fine-tuning, where all pretrained parameters are updated simultaneously. We conduct experiments on three sign language datasets: the German RWTH-PHOENIX-Weather-2014T (PHOENIX14T) [ [3](#bib.bib7) ] , the Arabic Isharah [ [2](#bib.bib50) ] , and the American MedASL [ [30](#bib.bib51) ] to assess the robustness of HATL across diverse languages and data characteristics. Our results demonstrate that HATL consistently improves translation across all settings, highlighting its potential as a robust transfer learning approach for SLMT.

The main contributions of this work are as follows.

- We propose HATL, a novel hierarchical adaptive transfer learning framework to improve SLMT.

- We compare HATL with classical and full fine-tuning baselines across three datasets, the German PHOENIX14T, the Arabic Isharah, and the American MedASL.

- We evaluate HATL, using the Transformer and ADAT, and compare the performance with existing works that use transfer learning for SLMT. Our experiments show that HATL outperforms existing static approaches.

- We perform experiments to demonstrate how progressive adaptation improves translation.

The rest of the paper is organized as follows: Section II reviews related work. Section III describes the proposed framework. Section IV provides the experimental setup, performance evaluation, and results analysis. Section V concludes the paper and discusses future research directions.

## 2 Related Work

Several works have explored transfer learning across various application domains. In this section, we divide the related work into two categories: transfer learning applications in different domains and in SLMT.

Table [1](#S2.T1) presents the works that applied transfer learning in various domains [ [22](#bib.bib12) , [34](#bib.bib13) , [35](#bib.bib14) , [31](#bib.bib15) , [32](#bib.bib16) , [1](#bib.bib17) , [8](#bib.bib18) ] . In computer vision, [ [22](#bib.bib12) ] demonstrates that pretrained Convolutional Neural Networks (CNN) backbones retain general spatial features under domain shifts. However, their approach relies on full fine-tuning, which increases training cost and sensitivity to overfitting. [ [34](#bib.bib13) ] decomposes synthetic-to-real LiDAR transfer into appearance and sparsity components, enabling partial adaptation through a learned point-cloud translator. This method relies on explicit domain alignment assumptions that may not generalize beyond the controlled settings. [ [35](#bib.bib14) ] proposes a Transformer-based model for facial expression recognition using multi-attention regularization to prevent overfitting. However, this model depends on full fine-tuning, which increases training cost and limits scalability. [ [31](#bib.bib15) ] develops an adversarial cross-subject transfer learning framework for human-activity recognition. The framework reduces inter-user variability, but at the cost of training instability and sensitivity to source and target domains selection.

In language understanding, [ [32](#bib.bib16) ] proposes a parameter-efficient transfer via adapter modules for vision-language models, maintaining pretrained knowledge while reducing training overhead. However, the fixed adapters restrict flexibility in capturing layer transferability. In speech processing, [ [8](#bib.bib18) ] demonstrates zero-shot transfer in text-to-speech using pretrained speaker embeddings, allowing adaptation without fine-tuning. However, this method shows degraded speaker similarity for unseen speakers. [ [1](#bib.bib17) ] adopts feature-level transfer by reusing mel-frequency cepstral coefficients and Random Forest-based representations. This method achieves accurate classification and low computational cost, but with limited knowledge transfer.

In summary, existing approaches reveal a clear trade-off between adaptation strength, computational cost, and stability. Full fine-tuning improves task alignment but risks overfitting, while parameter-efficient and feature-level transfer improve efficiency but overlook the contribution of different layers to transferable representations. In contrast to the domains discussed above, SLMT combines action recognition and language understanding, requiring joint modeling of spatio-temporal visual dynamics and linguistic structure. Consequently, we focus on analyzing transfer learning approaches specifically designed for SLMT.

Table [2](#S2.T2) compares the works that applied transfer learning to SLMT. These works are divided into two categories: 1) Sign2Text [ [3](#bib.bib7) , [13](#bib.bib48) , [12](#bib.bib49) , [4](#bib.bib19) , [5](#bib.bib46) , [36](#bib.bib32) , [19](#bib.bib47) , [37](#bib.bib34) , [21](#bib.bib29) , [7](#bib.bib36) , [6](#bib.bib3) , [38](#bib.bib35) ] , and 2) Sign2Gloss2Text [ [3](#bib.bib7) , [4](#bib.bib19) , [40](#bib.bib33) , [6](#bib.bib3) , [20](#bib.bib30) , [36](#bib.bib32) , [37](#bib.bib34) , [7](#bib.bib36) , [21](#bib.bib29) , [38](#bib.bib35) , [25](#bib.bib28) ] .

In Sign2Text, [ [3](#bib.bib7) ] initializes CNN-LSTM encoders with pretrained sign representations, achieving faster convergence but low accuracy due to weak linguistic training. Hierarchical models [ [13](#bib.bib48) , [12](#bib.bib49) ] use pretrained encoders and multi-level temporal modeling, improving robustness to motion variation despite increasing architecture complexity. [ [4](#bib.bib19) ] uses pretrained visual backbones with Connectionist Temporal Classification (CTC) supervision to stabilize training and improve fluency. However, it applies full fine-tuning which makes performance sensitive to domain shift. [ [5](#bib.bib46) ] shows that transferring keypoint-based features improves robustness across signers and domains. However, its performance is dependent on pose estimation quality. [ [21](#bib.bib29) ] uses pretrained spatio-temporal graph neural networks to model skeletal dynamics, achieving strong motion modeling at the cost of higher computational complexity. [ [36](#bib.bib32) ] transfers pretrained action-recognition backbones for simultaneous Sign2Text translation, prioritizing low latency over high translation accuracy. [ [19](#bib.bib47) ] frames Sign2Text as a meta-learning problem. It enables rapid adaptation to unseen signers while increasing computational overhead. [ [37](#bib.bib34) ] and [ [40](#bib.bib33) ] transfer pretrained RGB and pose representations, showing that multi-cue transfer improves performance. However, it increases training complexity and sensitivity to noise. [ [7](#bib.bib36) , [6](#bib.bib3) ] benefit from multi-modal pretraining but face scalability challenges. Lastly, [ [38](#bib.bib35) ] jointly transfers knowledge across Sign2Text and related tasks using shared encoders and external translation corpora. This approach improves data efficiency but relying on spoken language pretraining introduces linguistic mismatch, as sign language grammar is not directly aligned with spoken syntax.

In summary, existing Sign2Text transfer learning methods show that pretrained visual and multi-modal representations are essential when data is scarce. Nevertheless, most approaches rely on static fine-tuning or domain-mismatched priors. These limitations motivate adaptive transfer strategies that selectively reuse pretrained knowledge while preserving the temporal and linguistic structures.

In Sign2Gloss2Text, transfer learning operates across two stages, where representations learned for sign recognition are reused to support text generation. [ [3](#bib.bib7) ] pretrains the visual encoder on isolated sign recognition and reuses it for gloss-based translation. This allows visual-linguistic knowledge to flow, improving alignment between motion features and gloss symbols. However, the separation between stages prevents linguistic feedback from influencing the encoder, limiting adaptability once the recognition stage converges. [ [4](#bib.bib19) ] mitigates this by learning shared representations between Sign2Gloss and Gloss2Text, enabling bidirectional transfer between both tasks. This approach improves visual-text alignment and training stability. However, it lacks control over task influence, leading to dominance of one modality. [ [6](#bib.bib3) ] shows that freezing pretrained encoders while fine-tuning fusion and decoding layers preserves low-level representations, but restricts higher-level adaptation to domain-specific syntax. [ [40](#bib.bib33) ] and [ [20](#bib.bib30) ] demonstrate that the reuse of cross-stage features across RGB, pose, and motion streams improves translation quality. However, the relative contribution of each modality to generalization remains underexplored. [ [36](#bib.bib32) ] introduces a dual translation model bridging Sign2Gloss2Text and Sign2Text by sequentially adapting visual, gloss, and text representations within a unified framework. This approach presents a shift from two-stage training toward integrated transfer. However, it is driven by latency constraints and does not explicitly address stability under large domain shifts. [ [37](#bib.bib34) ] , [ [38](#bib.bib35) ] , and [ [25](#bib.bib28) ] integrate multi-task models by jointly training sign language recognition and translation. These models demonstrate that recognition-pretrained features can be reused for gloss-based translation. Nevertheless, they rely on static fine-tuning, increasing sensitivity to overfitting and unstable convergence in low-resource settings. [ [7](#bib.bib36) ] and [ [21](#bib.bib29) ] pretrain recognition components and then transfer their outputs to pretrained text decoders. Similar to previous works, these models use static full fine-tuning, increasing the risk of unstable convergence.

In summary, Sign2Gloss2Text transfer learning benefits strongly from recognition-pretrained representations, but existing approaches rely on stage-wise transfer, unconstrained joint training, or static fine-tuning. These limitations highlight the need for an adaptive transfer approach that regulates knowledge flow across stages while preserving sign language structure.

To conclude, existing Sign2Gloss2Text models rely on sequential transfer through gloss supervision, while Sign2Text approaches emphasize end-to-end multi-modal adaptation. Although recent works integrate cross-modal learning, transfer learning is still static, limiting stability under large domain shifts and constraining visual-linguistic alignment. To address these issues, we propose HATL, a hierarchical adaptive transfer learning framework that gradually adapts visual backbone layers. To our knowledge, no prior SLMT work provides such a dynamic transfer framework that progressively aligns feature representations while maintaining pretrained knowledge.

## 3 Proposed Hierarchical Adaptive Transfer Learning (HATL) Framework

In this section, we present HATL, a hierarchical performance-aware transfer learning framework for SLMT. HATL replaces static fine-tuning with dynamic hierarchical adaptation, progressively expanding trainable capacity based on performance behavior. It treats pretrained models as structured hierarchies, selectively and dynamically activating layers to adapt to sign language dynamics. We introduce the system model followed by the training process. Figure [1](#S4.F1) illustrates the overall framework. Algorithm [1](#alg1) shows the HATL's algorithm.

## 4 Algorithm

Figure 1: Overall HATL framework.

<!-- image -->

### 4.1 System Model

Figure [1](#S4.F1) (a) presents the system model. We formulate SLMT using HATL as adapting a pretrained visual backbone and translation model to minimize the training objective while dynamically expanding the trainable parameters.

Given a sign language input sequence x x , the objective is to adapt a pretrained model f  ( ⋅ ; Θ ) f(\cdot;\Theta) to produce stable and effective predictions, as shown in Equation [4.1](#S4.Ex1) .

|    | y  ^  =  f  (  x  ;  Θ  )  \hat{y}=f(x;\Theta)   |    |
|----|--------------------------------------------------|----|

where y ^ \hat{y} is the SLMT model output.

We decompose the SLMT model into two main components: a pretrained backbone that serves as a visual feature extractor and a translation model that maps these features to linguistic outputs. Equation [4.1](#S4.Ex3) presents the full SLMT model.

|    | f  (  x  ;  Θ  )  =  t  (  b  (  x  ;  W  b  )  ;  W  t  )  f(x;\Theta)=t\!\left(b(x;W\_{b});\,W\_{t}\right)   |    |
|----|----------------------------------------------------------------------------------------------------------------|----|

where t  ( ⋅ ) t(\cdot) is the translation model, W t W\_{t} is its parameter, b  ( ⋅ ) b(\cdot) is the pretrained backbone model, and W b W\_{b} is its parameter.

The backbone is further divided into an ordered hierarchy of layers, L = { L 1 , L 2 , ... , L n } L=\left\{L\_{1},L\_{2},\ldots,L\_{n}\right\} , with L 1 L\_{1} denoting the closest layer to the sign video input and L n L\_{n} the closest layer to the translation model. At epoch e e , only a subset of parameters 𝒰 e ⊆ { L 1 , L 2 , ... , L n , t } \mathcal{U}\_{e}\subseteq\left\{L\_{1},L\_{2},\ldots,L\_{n},t\right\} is trainable. Training begins with 𝒰 0 = { t } \mathcal{U}\_{0}=\left\{t\right\} , such that only the translation model is trained while all backbone layers remain frozen. This decomposition provides the foundation for HATL's progressive transfer mechanism.

### 4.2 Training Process

Figure [1](#S4.F1) (b) shows the training process, which consists of: 1) Adaptive transfer learning, 2) Layer-wise learning rate control, 3) Stability mechanisms, and 4) Loss function.

#### 4.2.1 Adaptive Transfer Learning

HATL determines when to activate additional pretrained layers for adaptation through performance-aware adaptation. Let M  ( e ) M(e) denote a validation metric in epoch e e with M ′  ( e ) M^{\prime}(e) as the best value at epoch e e . To reduce per-epoch fluctuations, we compute a moving average over the previous epochs as shown in Equation [4.2.1](#S4.Ex5) .

|    | M  ¯  (  e  )  =  1  k  ∑  j  =  e  −  k  +  1  e  M  (  j  )  \bar{M}(e)=\frac{1}{k}\sum\_{j=e-k+1}^{e}M(j)   |    |
|----|----------------------------------------------------------------------------------------------------------------|----|

where M ¯  ( e ) \bar{M}(e) is the smoothed validation metric at epoch e e , M  ( j ) M(j) is the validation metric at epoch j j , j j is the summation index over epochs, and k k is the moving-average window size.

The decision to activate a backbone layer L m L\_{m} is based on two criteria: (i) there is no significant improvement beyond a small margin ( Δ ) (\Delta) for several epochs, | M  ( e ) − M ¯  ( e ) | ≤ Δ |M(e)\ -\bar{M}(e)|\leq\Delta , indicating convergence, and (ii) the improvement relative to the best observed performance is below a threshold ( τ ) (\tau) , | M  ( e ) − M ¯  ( e ) | ≤ τ |M(e)\ -\ \bar{M}(e)|\leq\tau . When both conditions are met, L m L\_{m} becomes trainable at the start of the next epoch. This mechanism ensures that HATL expands trainable capacity only after the model has reached a stable optimization state.

#### 4.2.2 Layer-wise Learning Rate Control

Once a backbone layer is activated, HATL updates the optimizer to adjust the model parameters. In particular, it applies layer-wise learning rate decay (LLRD) [ [17](#bib.bib52) ] to assign different learning rates to different layers. For layer m m , the learning rate is set to:

|    | L  R  m  =  L  R  t  ⋅  α  n  −  m  LR\_{m}=LR\_{t}\cdot\alpha^{n-m}   |    |
|----|------------------------------------------------------------------------|----|

where L  R t LR\_{t} is the translation model learning rate and α ∈ ( 0 , 1 ) \alpha\in(0,1) is a decay factor.

This results in larger learning rates for layers closer to the translation model, leading to stronger adaptation, and smaller learning rates for layers closer to the sign video input, to preserve generic features.

#### 4.2.3 Stability Mechanisms

HATL incorporates several safeguards to ensure reliable progress during the adaptive transfer process. Training begins with a warmup phase, where only the translation model is being trained to ensure stability before transfer begins. Before activating any additional layer, HATL restores the model parameters from the best validation performance to prevent propagating unstable states. In addition, HATL applies a cooldown period after each layer activation, during which no further layers can be activated. Moreover, the threshold Δ \Delta gradually decays, allowing the layer activation criterion to become more selective as learning slows. Finally, an early stopping rule terminates training when validation performance no longer improves.

#### 4.2.4 Loss Function

HATL uses a weighted multi-objective loss function to supervise gloss alignment, text generation, and intermediate visual representations. Equation [4.2.4](#S4.Ex9) defines the overall loss.

|    | ℒ  =  ω  C  T  C  ℒ  C  T  C  +  ω  C  E  ℒ  C  E  +  ω  e  n  c  ℒ  e  n  c  +  ω  b  b  ℒ  b  b  \mathcal{L}={\omega\_{CTC}\mathcal{L}}\_{CTC}+{\omega\_{CE}\mathcal{L}}\_{CE}+\omega\_{enc}\mathcal{L}\_{enc}+\omega\_{bb}\mathcal{L}\_{bb}   |    |
|----|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----|

where L C  T  C {L}\_{CTC} is CTC loss for frame-to-gloss alignment, L C  E {L}\_{CE} is Cross-Entropy (CE) loss for training the autoregressive text decoder, and L e  n  c {L}\_{enc} and L b  b {L}\_{bb} apply frame-wise supervision in the encoder and backbone, respectively. The weights ω C  T  C \omega\_{CTC} , ω C  E \omega\_{CE} , ω e  n  c \omega\_{enc} , and ω b  b \omega\_{bb} control the influence of each component. For direct Sign2Text translation, the gloss alignment is disabled by setting ω C  T  C = 0 \omega\_{CTC}=0 .

##### Connectionist Temporal Classification Loss

During Sign2Gloss2Text training, the encoder outputs frame-level gloss probabilities, as defined in Equation [4.2.4](#S4.Ex11) .

|    | p  g  (  c  )  =  p  (  c  ∣  x  )  g  p\_{g}(c)=p(c\mid x)\_{g}   |    |
|----|--------------------------------------------------------------------|----|

where p  ( c ∣ x ) g p(c\mid x)\_{g} is gloss predicted probability at frame x x .

Sign language often lacks explicit frame-level gloss boundaries. Therefore, we use CTC to model frame-to-gloss alignment. Given a target gloss sequence is Y = ( y 1 , ... , y U ) Y=(y\_{1},\ldots,y\_{U}) , the CTC loss is defined in Equation [4.2.4](#S4.Ex13) .

|    | ℒ  C  T  C  =  −  log  ∑  A  ∈  B  −  1  (  Y  )  P  gloss  −  path  (  A  ∣  x  )  \mathcal{L}\_{CTC}=-\log\sum\_{A\in B^{-1}(Y)}P\_{\mathrm{gloss-path}}(A\mid x)   |    |
|----|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|----|

where B − 1  ( Y ) B^{-1}(Y) denotes all valid alignment paths A = ( A 1 , ... , A z ) A=(A\_{1},\ldots,A\_{z}) in the gloss sequence Y Y .

Equation [4.2.4](#S4.Ex15) defines the probability of gloss-alignment path.

|    | P  gloss  −  path  (  A  ∣  x  )  =  ∏  g  =  1  G  p  g  (  A  g  )  P\_{\mathrm{gloss-path}}(A\mid x)=\prod\_{g=1}^{G}p\_{g}(A\_{g})   |    |
|----|------------------------------------------------------------------------------------------------------------------------------------------|----|

where p g  ( A g ) p\_{g}(A\_{g}) is the predicted probability at frame g g .

##### Cross Entropy Loss

The autoregressive text decoder plays an increasingly larger role as more layers become trainable. Equation [9](#S4.Ex17) defines CE loss used for training text generation.

|    | ℒ  CE  =  −  1  N  S  ∑  i  =  1  N  ∑  s  =  1  S  log  ⁡  p  (  y  i  ,  s  text  ∣  x  i  ,  y  i  ,  &lt;  s  text  )  \mathcal{L}\_{\mathrm{CE}}=-\frac{1}{NS}\sum\_{i=1}^{N}\sum\_{s=1}^{S}\log p\!\left(y\_{i,s}^{\mathrm{text}}\mid x\_{i},y\_{i,&lt;s}^{\mathrm{text}}\right)   |    | (9)   |
|----|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----|-------|

where N N denotes the number of sign videos, S S is the length of the target text sequence, i i indexes the sign videos, s s indexes token position within the target text sequence, and y text y^{\mathrm{text}} denotes the ground-truth target text token. The conditional distribution is parameterized by the translation model defined in Equation [4.1](#S4.Ex3) .

##### Encoder Frame-wise Supervision

To maintain visual alignment within the encoder during unfreezing, HATL applies a frame-wise supervision at the encoder level. Equation [10](#S4.Ex18) presents this loss.

|    | ℒ  enc  =  −  1  &#124;  ℳ  &#124;  ∑  (  i  ,  s  )  ∈  ℳ  log  ⁡  p  (  y  i  ,  s  enc  ∣  x  i  )  \mathcal{L}\_{\mathrm{enc}}=-\frac{1}{&#124;\mathcal{M}&#124;}\sum\_{(i,s)\in\mathcal{M}}\log p\!\left(y\_{i,s}^{\mathrm{enc}}\mid x\_{i}\right)   |    | (10)   |
|----|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----|--------|

where ℳ \mathcal{M} is the set of aligned frame indices used for supervision

and y enc y^{\mathrm{enc}} is the target encoder label.

##### Backbone Frame-wise Supervision

HATL applies an additional loss directly to the backbone output to align the frames with the backbone. This component maintains stable feature transitions during progressive unfreezing. Equation [11](#S4.Ex19) defines this loss.

|    | ℒ  bb  =  −  1  &#124;  ℳ  &#124;  ∑  (  i  ,  s  )  ∈  ℳ  log  ⁡  p  (  y  i  ,  s  bb  ∣  x  i  )  \mathcal{L}\_{\mathrm{bb}}=-\frac{1}{&#124;\mathcal{M}&#124;}\sum\_{(i,s)\in\mathcal{M}}\log p\!\left(y\_{i,s}^{\mathrm{bb}}\mid x\_{i}\right)   |    | (11)   |
|----|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----|--------|

where y bb y^{\mathrm{bb}} is the target backbone.

These four loss components define HATL as a dynamic transfer learning framework. In particular, CTC enables early alignment while the backbone is mostly frozen. The encoder and backbone losses stabilize intermediate representations as layers are progressively unfrozen. The CE decoding dominates training once deeper layers become trainable. This design allows SLMT models to benefit from pretrained motion representations while gradually adapting to sign language translation.

In summary, HATL adapts pretrained models to SLMT by dynamically expanding trainable layers based on validation performance. By combining hierarchical parameter access with performance-aware control, learning-rate regulation, and frame-wise supervision, HATL enables pretrained SLMT models to gradually specialize toward sign language translation while preserving robust visual representations learned during pretraining.

## 5 Performance Evaluation

### 5.1 Experimental Environment

#### 5.1.1 Datasets

We evaluate the proposed HATL approach on three datasets: PHOENIX14T [ [3](#bib.bib7) ] , Isharah [ [2](#bib.bib50) ] , and MedASL [ [30](#bib.bib51) ] . Table [3](#S5.T3) summarizes the datasets characteristics.

PHOENIX14T presents the highest linguistic variability due to its multi-signer nature, broad vocabulary, and long sequences. The large coefficients of variation (CV) in gloss and text indicate fluctuations in syntax and pacing, which challenge transfer stability and generalization.

Isharah reflects a controlled setting. Despite including multiple signers, its sequences are short and highly consistent, with minimal CV in gloss and text lengths. This leads to evaluating primarily signer generalization rather than linguistic generalization.

MedASL's single-signer setting produces a uniform signing pattern and consistent sentence structure, while the medical domain introduces rich terminology and structured phrasing. This setting creates a controlled setting that maintains meaningful semantic variation.

These datasets allow objective evaluation of HATL across multiple linguistic conditions. We use the predefined splits of PHOENIX14T and Isharah, while we split MedASL into 80% for 5-fold cross-validation and 20% for testing.

#### 5.1.2 Data Preprocessing

We use a unified preprocessing setup to produce lightweight inputs. First, we resize input frames to 52 × 65 52{\times}65 to ensure consistent resolution and efficient computation. Then, we extract keypoint representations from raw videos using MediaPipe [ [11](#bib.bib54) ] , capturing hand, face, iris, and upper-body landmarks. This is to remove unnecessary visual details and reduce input dimensionality while preserving essential motion and articulation cues needed for translation [ [29](#bib.bib53) ] . We normalize and rescale the resulting coordinates. We then concatenate them across sentences and pad them for batch processing.

For the text output, we construct a vocabulary that includes start- and end-of-sentence tokens. We tokenize the sentences, map each token to its index, and pad the sequences to a fixed length to enable efficient batch-level training and evaluation.

#### 5.1.3 Model Development

We evaluate HATL using a pretrained ST-GCN++ [ [9](#bib.bib57) ] for feature extraction and the Transformer [ [33](#bib.bib26) ] and ADAT [ [30](#bib.bib51) ] for translation. ST-GCN++ is a Spatio-Temporal Graph Convolutional Network originally introduced for skeleton-based action recognition. It models human motion as a sequence of spatiotemporal graphs, where joints serve as nodes and physical connections as edges. The model stacks ten spatial graph convolution layers with multi-scale temporal convolutions using parallel dilated kernels. This design captures global motion patterns and fine-grained dynamics with low computational cost. Although it was not designed for sign language, its strong generalization on large-scale skeleton-action benchmarks makes it a suitable backbone for SLMT.

The Transformer serves as a strong baseline as it is the most widely used and accurate model for SLMT [ [27](#bib.bib37) ] . Its encoder-decoder structure separates visual encoding from linguistic generation, and its multi-head attention layers provide full pairwise context modeling. However, the quadratic attention cost makes it computationally demanding for long video sequences. In addition, it does not efficiently capture short, fine-grained temporal dependencies in signs.

ADAT is an adaptive time-series-aware Transformer-based model. It consists of a dual-branch encoder and a decoder. The encoder separates local and global temporal processing to capture fine-grained, short-range motion patterns and long-range dependencies at reduced computational cost. An adaptive gating mechanism dynamically balances the contributions of both branches. This design processes rapid and fine-grained motions while preserving context. Consequently, it provides a more efficient, temporally sensitive alternative to the Transformer for SLMT.

#### 5.1.4 Evaluation Metrics

To provide a comparable evaluation of translation quality and computational efficiency, we assess translation quality using Bilingual Evaluation Understudy (BLEU) [ [24](#bib.bib55) ] and Recall-Oriented Understudy for Gisting Evaluation (ROUGE) [ [26](#bib.bib56) ] performance and measure efficiency through training time.

BLEU captures n-gram precision with a length penalty to measure length mismatch and fluency. It is computed using the geometric mean of n-gram precisions with a brevity penalty ( B  P ) (BP) , as defined in Equations [5.1.4](#S5.Ex20) .

|    | B  L  E  U  =  (  ∏  n  =  1  N  p  n  w  n  )  ,  BP  =  {  1  ,  if  c  &gt;  r  ,  e  1  −  r  c  ,  if  c  ≤  r  .  BLEU=\left(\prod\_{n=1}^{N}p\_{n}^{\,w\_{n}}\right),\quad\text{BP}=\begin{cases}1,&amp;\text{if }c&gt;r,\\[6.0pt]  e^{\,1-\frac{r}{c}},&amp;\text{if }c\leq r.\end{cases}   |    |
|----|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----|

where p n p\_{n} is the precision of n-grams, w n w\_{n} is the weight of each n-gram size, c c is the length of the candidate translation, and r r is the length of the reference sequence.

ROUGE measures recall of overlapping sequences based on the longest common subsequence ( L  C  S ) (LCS) between a generated ( G ) (G) and a reference translations ( R ) (R) . The ROUGE-L captures precision and recall and is given by Equation [5.1.4](#S5.Ex22) .

|    | ROUGE-L  =  2  ⋅  LCS  (  G  ,  R  )  &#124;  G  &#124;  +  &#124;  R  &#124;  \text{ROUGE-L}=\frac{2\cdot\text{LCS}(G,R)}{&#124;G&#124;+&#124;R&#124;}   |    |
|----|-----------------------------------------------------------------------------------------------------------------------------------------------------------|----|

For computational efficiency, we compute training time as the total number of hours required to complete model training under the unified experimental setup.

### 5.2 Experiments

To evaluate HATL, we compare it against two fine-tuning baselines: 1) classical fine-tuning, where only the translation model is trained while the backbone remains frozen, and 2) full fine-tuning, where all backbone layers and the translation model are unfrozen and trained from the start. We conduct these comparisons using two translation models: the standard Transformer and ADAT.

To ensure fair comparison, we use the same backbone across all configurations and evaluate all models under a unified setup for Sign2Text and Sign2Gloss2Text translation tasks on PHOENIX14T, Isharah, and MedASL datasets. We conduct all experiments in PyTorch using 2 NVIDIA RTX A6000 GPUs.

We perform a structured, multi-stage hyperparameter search, tuning parameter subsets at each stage while keeping the rest fixed. Table [4](#S5.T4) summarizes all hyperparameters used to evaluate HATL and the translation models, respectively.

### 5.3 Experimental Results Analysis

This section presents a comprehensive evaluation of HATL across ADAT and Transformer models on Sign2Gloss2Text and Sign2Text translation tasks, comparing it against classical and full static fine-tuning in terms of translation quality and computational efficiency.

#### 5.3.1 Translation Quality

Tables [5](#S5.T5) - [7](#S5.T7) report the translation quality results on PHOENIX14T, Isharah, and MedASL datasets, respectively, for Sign2Gloss2Text and Sign2Text. State-of-the-art results are reported for comparison.

1. Sign2Gloss2Text

Across all datasets, static fine-tuning approaches often converge to similar performance, while HATL consistently outperforms both baselines, demonstrating that progressive hierarchical adaptation is more stable than static approaches.

On PHOENIX14T, static fine-tuning results in comparable performance for the Transformer and ADAT, whereas HATL consistently improves both models. The Transformer shows improvements across all metrics, indicating enhanced gloss-text alignment and sentence-level structure. ADAT benefits more significantly due to its temporally adaptive architecture. It outperforms both fine-tuning baselines with +12.2 and +10.5 BLEU-4, respectively. It also surpasses prior state-of-the-art systems by at least +3.0 BLEU-4, demonstrating the combined effectiveness of ADAT and HATL.

On Isharah and MedASL, HATL achieves significant improvements across all metrics, with ADAT showing the largest gains. In particular, In Isharah, ADAT results in +11.3 and +9.8 BLEU-4 over classical and full fine-tuning, respectively. In MedASL, ADAT outperforms classical and fine-tuning with +15.6 and +11.8 BLEU-4, respectively. The enhancements observed in ROUGE indicate better preservation of domain-specific terminology, which is critical for healthcare SLMT applications.

In summary, HATL consistently outperforms both static fine-tuning approaches across all datasets. Its benefits are most notable in complex and domain-specific environments such as PHOENIX14T, while remaining effective in low-variability settings such as Isharah. The gains are particularly evident in ADAT, as its architecture is more sensitive to temporal structure. By progressively unfreezing layers, HATL preserves pretrained temporal structure while enabling performance-aware hierarchical adaptation, leading to stable improvements across BLEU and ROUGE metrics. Overall, HATL achieves state-of-the-art results on PHOENIX14T and Isharah datasets, with substantial improvements on MedASL, demonstrating robustness across signers and languages.

2. Sign2Text

Sign2Text follows the same performance trends as Sign2Gloss2Text. On PHOENIX14T, the Transformer shows consistent improvements across n-grams, while ADAT reveals the full impact of HATL, due to its time-series-aware encoder. HATL enables ADAT to surpass prior Sign2Text state-of-the-art models, including Two-Stream SLT [ [7](#bib.bib36) ] (+0.4 BLEU-4) and SLTUNET [ [38](#bib.bib35) ] (+0.9 BLEU-4).

On Isharah, HATL results in significant improvements in both translation models. ADAT achieves the highest BLEU and ROUGE scores, outperforming the state-of-the-art by +6.0 BLEU-4 and +3.7 ROUGE.

On MedASL, similar to the other results, ADAT benefits the most from HATL, resulting in +14.9 BLEU-4 over classical and +2.2 over full fine-tuning. The significant gains in ROUGE indicates improved content preservation, which is critical in medical translation.

In summary, HATL consistently outperforms static fine-tuning. Its effectiveness is more pronounced for ADAT than the Transformer, leading to more accurate translations than state-of-the-art approaches. PHOENIX14T and MedASL highlight HALT's robustness under linguistic diversity and domain specificity, while Isharah results in higher scores due to its structure. In particular, Isharah includes 15 signers, which is large for keypoint-based models. Keypoint representations reduce visual identity bias, making models lighter and less signer-dependent than RGB-based approaches [ [29](#bib.bib53) ] .

#### 5.3.2 Computational Efficiency

Figures [2](#S5.F2) - [4](#S5.F4) compare the training time in hours across fine-tuning approaches for PHOENIX14T, Isharah, and MedASL datasets, covering all models and translation tasks. Classical fine-tuning is consistently the most efficient, as the backbone remains frozen and only the translation model is updated. Full fine-tuning has higher computational cost, as all backbone layers are updated from the start, resulting in a larger number of trainable parameters. HATL introduces additional overhead due to its hierarchical progressive activation, where each newly unfrozen layer expands the optimization space and increases training duration. These trends are consistent across datasets, translation models, and tasks.

Figure 2: Training time for fine-tuning approaches across Transformer and ADAT models on PHOENIX14T dataset.

<!-- image -->

Figure 3: Training time for fine-tuning approaches across Transformer and ADAT models on Isharah dataset.

<!-- image -->

Figure 4: Training time for fine-tuning approaches across Transformer and ADAT models on MedASL dataset.

<!-- image -->

Figures [5](#S5.F5) - [10](#S5.F10) illustrate the training behavior of Transformer and ADAT models using HATL across all datasets and translation tasks. Across all settings, ADAT consistently unfreezes more pretrained layers than the Transformer. As a result, training extends to later epochs, leading to higher total training time. Nevertheless, ADAT consistently maintains a lower average time per epoch than the Transformer, indicating that the increased training time is due to the extended training rather than reduced per-epoch efficiency.

Figure 5: Training time versus number of unfrozen layers using HATL for Transformer and ADAT on PHOENIX14T dataset.

<!-- image -->

Figure 6: Training time versus number of unfrozen layers using HATL for Transformer and ADAT on Isharah dataset.

<!-- image -->

Figure 7: Training time versus number of unfrozen layers using HATL for Transformer and ADAT on MedASL dataset.

<!-- image -->

Figure 8: Hierarchical
unfreezing timelines using HATL for Transformer and ADAT on PHOENIX14T dataset.

<!-- image -->

Figure 9: Hierarchical unfreezing timelines using HATL for Transformer and ADAT on Isharah dataset.

<!-- image -->

Figure 10: Hierarchical unfreezing timelines using HATL for Transformer and ADAT on MedASL dataset.

<!-- image -->

In summary, computational cost is driven by the extent and duration of backbone adaptation. Classical fine-tuning is the most efficient due to the frozen backbone, while full fine-tuning is more expensive due to simultaneous training of all pretrained layers. HATL increases training time through progressive hierarchical unfreezing. Within this framework, ADAT has higher total training time than the Transformer while maintaining lower average time per epoch.

Overall, the improved translation quality achieved by HATL is linked to its dynamic hierarchical unfreezing, which requires more epochs, increasing total training time. This additional cost enables deeper specialization, resulting in state-of-the-art translation quality.

## 6 Conclusion and Future Work

This paper proposes a performance-aware Hierarchical Adaptive Transfer Learning (HATL) framework for Sign Language Machine Translation (SLMT). HATL progressively increases trainable capacity based on performance, preserving pretrained representations while adapting deeper layers to sign language. Experiments on PHOENIX14T, Isharah, and MedASL datasets across Sign2Text and Sign2Gloss2Text tasks show that HATL consistently surpasses static fine-tuning approaches. Combining HATL with the Adaptive Transformer outperforms transfer learning baselines in the Transformer, highlighting the effectiveness of performance-aware transfer learning for SLMT. Future work should extend HATL to other domains than SLMT and evaluate it using different pretrained models than ST-GCN.

##### Funding

This research was funded by the Emirates Center for Mobility Research, United Arab Emirates University.

##### Data Availability

The dataset and the implementation code are publicly available at [https://github.com/INDUCE-Lab/](https://github.com/INDUCE-Lab/) .

## References

- [1] A. S. Al-Shamayleh, H. Riasat, A. S. Alluhaidan, A. Raza, S. A. El-Rahman, and D. S. AbdElminaam (2025) Novel transfer learning based acoustic feature engineering for scene fake audio detection . Scientific Reports 15 ( 1 ), pp. 8066 . Cited by: [§1](#S1.p3.1) , [Table 1](#S2.T1.1.1.1.1.1.1.1.8.1.1.1) , [§2](#S2.p2.1) , [§2](#S2.p3.1) .
- [2] S. Alyami, H. Luqman, S. Al-Azani, M. Alowaifeer, Y. Alharbi, and Y. Alonaizan (2025) Isharah: a large-scale multi-scene dataset for continuous sign language recognition . arXiv preprint arXiv:2506.03615 . Cited by: [§1](#S1.p5.1) , [§5.1.1](#S5.SS1.SSS1.p1.1) .
- [3] N. C. Camgoz, S. Hadfield, O. Koller, H. Ney, and R. Bowden (2018) Neural sign language translation . In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition , pp. 7784-7793 . Cited by: [§1](#S1.p1.1) , [§1](#S1.p5.1) , [Table 2](#S2.T2.1.1.1.1.1.1.3.1.1.1) , [§2](#S2.p5.1) , [§2](#S2.p6.1) , [§2](#S2.p8.1) , [§5.1.1](#S5.SS1.SSS1.p1.1) , [Table 5](#S5.T5.1.1.1.1.21.1) , [Table 5](#S5.T5.1.1.1.1.4.1) .
- [4] N. C. Camgoz, O. Koller, S. Hadfield, and R. Bowden (2020) Sign language transformers: joint end-to-end sign language recognition and translation . In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition , pp. 10023-10033 . Cited by: [Table 2](#S2.T2.1.1.1.1.1.1.4.1.1.1) , [§2](#S2.p5.1) , [§2](#S2.p6.1) , [§2](#S2.p8.1) , [Table 5](#S5.T5.1.1.1.1.26.1) , [Table 5](#S5.T5.1.1.1.1.6.1) .
- [5] L. Chaudhary, T. Ananthanarayana, E. Hoq, and I. Nwogu (2022) Signnet ii: a transformer-based two-way sign language translation model . IEEE Transactions on Pattern Analysis and Machine Intelligence 45 ( 11 ), pp. 12896-12907 . Cited by: [Table 2](#S2.T2.1.1.1.1.1.1.8.1.1.1) , [§2](#S2.p5.1) , [§2](#S2.p6.1) , [Table 5](#S5.T5.1.1.1.1.24.1) .
- [6] Y. Chen, F. Wei, X. Sun, Z. Wu, and S. Lin (2022) A simple multi-modality transfer learning baseline for sign language translation . In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition , pp. 5120-5130 . Cited by: [§1](#S1.p1.1) , [Table 2](#S2.T2.1.1.1.1.1.1.12.1.1.1) , [§2](#S2.p5.1) , [§2](#S2.p6.1) , [§2](#S2.p8.1) , [Table 5](#S5.T5.1.1.1.1.11.1) , [Table 5](#S5.T5.1.1.1.1.28.1) , [Table 6](#S5.T6.1.1.1.1.1.1.4.1) .
- [7] Y. Chen, R. Zuo, F. Wei, Y. Wu, S. Liu, and B. Mak (2022) Two-stream network for sign language recognition and translation . Advances in Neural Information Processing Systems 35 , pp. 17043-17056 . Cited by: [Table 2](#S2.T2.1.1.1.1.1.1.13.1.1.1) , [§2](#S2.p5.1) , [§2](#S2.p6.1) , [§2](#S2.p8.1) , [§5.3.1](#S5.SS3.SSS1.p8.1) , [Table 5](#S5.T5.1.1.1.1.13.1) , [Table 5](#S5.T5.1.1.1.1.30.1) .
- [8] E. Cooper, C. Lai, Y. Yasuda, F. Fang, X. Wang, N. Chen, and J. Yamagishi (2020) Zero-shot multi-speaker text-to-speech with state-of-the-art neural speaker embeddings . In ICASSP 2020-2020 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP) , pp. 6184-6188 . Cited by: [§1](#S1.p3.1) , [Table 1](#S2.T1.1.1.1.1.1.1.1.9.1.1.1) , [§2](#S2.p2.1) , [§2](#S2.p3.1) .
- [9] H. Duan, J. Wang, K. Chen, and D. Lin (2022) Pyskl: towards good practices for skeleton action recognition . In Proceedings of the 30th ACM international Conference on Multimedia , pp. 7351-7354 . Cited by: [§1](#S1.p5.1) , [§5.1.3](#S5.SS1.SSS3.p1.1) .
- [10] H. Fu, L. Zhang, B. Fu, R. Zhao, J. Su, X. Shi, and Y. Chen (2024-06) Signer diversity-driven data augmentation for signer-independent sign language translation . In Findings of the Association for Computational Linguistics: NAACL 2024 , K. Duh, H. Gomez, and S. Bethard (Eds.) , Mexico City, Mexico , pp. 2182-2193 . External Links: [Link](https://aclanthology.org/2024.findings-naacl.140/) , [Document](https://dx.doi.org/10.18653/v1/2024.findings-naacl.140) Cited by: [§1](#S1.p1.1) .
- [11] Google AI (2024) MediaPipe solutions guide . Note: [https://ai.google.dev/edge/mediapipe/solutions/guide](https://ai.google.dev/edge/mediapipe/solutions/guide) Accessed: 2024-11-20 Cited by: [§5.1.2](#S5.SS1.SSS2.p1.1) .
- [12] D. Guo, W. Zhou, A. Li, H. Li, and M. Wang (2019) Hierarchical recurrent deep fusion using adaptive clip summarization for sign language translation . IEEE Transactions on Image Processing 29 , pp. 1575-1590 . Cited by: [Table 2](#S2.T2.1.1.1.1.1.1.6.1.1.1) , [§2](#S2.p5.1) , [§2](#S2.p6.1) .
- [13] D. Guo, W. Zhou, H. Li, and M. Wang (2018) Hierarchical lstm for sign language translation . In Proceedings of the AAAI conference on Artificial Intelligence , Vol. 32 . Cited by: [Table 2](#S2.T2.1.1.1.1.1.1.5.1.1.1) , [§2](#S2.p5.1) , [§2](#S2.p6.1) .
- [14] M. L. Hall, W. C. Hall, and N. K. Caselli (2019) Deaf children need language, not (just) speech . First language 39 ( 4 ), pp. 367-395 . Cited by: [§1](#S1.p1.1) .
- [15] R. Holmes, E. Rushe, M. De Coster, M. Bonnaerens, S. Satoh, A. Sugimoto, and A. Ventresque (2023) From scarcity to understanding: transfer learning for the extremely low resource irish sign language . In Proceedings of the IEEE/CVF International Conference on Computer Vision , pp. 2008-2017 . Cited by: [§1](#S1.p1.1) , [§1](#S1.p2.1) .
- [16] A. Hosna, E. Merry, J. Gyalmo, Z. Alom, Z. Aung, and M. A. Azim (2022) Transfer learning: a friendly introduction . Journal of Big Data 9 ( 1 ), pp. 102 . Cited by: [§1](#S1.p1.1) , [§1](#S1.p2.1) , [§1](#S1.p4.1) .
- [17] J. Howard and S. Ruder (2018) Universal language model fine-tuning for text classification . In Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers) , pp. 328-339 . Cited by: [§4.2.2](#S4.SS2.SSS2.p1.1) .
- [18] L. Ismail, N. Shahin, H. Tesfaye, and A. Hennebelle (2025) VisioSLR: a vision data-driven framework for sign language video recognition and performance evaluation on fine-tuned yolo models . Procedia Computer Science 257 , pp. 85-92 . Cited by: [§1](#S1.p5.1) .
- [19] T. Jin, Z. Zhao, M. Zhang, and X. Zeng (2022) Mc-slt: towards low-resource signer-adaptive sign language translation . In Proceedings of the 30th ACM International Conference on Multimedia , pp. 4939-4947 . Cited by: [Table 2](#S2.T2.1.1.1.1.1.1.10.1.1.1) , [§2](#S2.p5.1) , [§2](#S2.p6.1) , [Table 5](#S5.T5.1.1.1.1.25.1) .
- [20] J. Kan, K. Hu, M. Hagenbuchner, A. C. Tsoi, M. Bennamoun, and Z. Wang (2022) Sign language translation with hierarchical spatio-temporal graph neural network . In Proceedings of the IEEE/CVF winter Conference on Applications of Computer Vision , pp. 3367-3376 . Cited by: [§2](#S2.p5.1) , [§2](#S2.p8.1) , [Table 5](#S5.T5.1.1.1.1.7.1) .
- [21] R. Li and L. Meng (2022) Sign language recognition and translation network based on multi-view data . Applied Intelligence 52 ( 13 ), pp. 14624-14638 . Cited by: [Table 2](#S2.T2.1.1.1.1.1.1.14.1.1.1) , [§2](#S2.p5.1) , [§2](#S2.p6.1) , [§2](#S2.p8.1) , [Table 5](#S5.T5.1.1.1.1.22.1) , [Table 5](#S5.T5.1.1.1.1.5.1) .
- [22] W. Liu, K. Quijano, and M. M. Crawford (2022) YOLOv5-tassel: detecting tassels in rgb uav imagery with improved yolov5 based on transfer learning . IEEE Journal of Selected Topics in Applied Earth Observations and Remote Sensing 15 , pp. 8085-8094 . Cited by: [§1](#S1.p3.1) , [Table 1](#S2.T1.1.1.1.1.1.1.1.3.1.1.1) , [§2](#S2.p2.1) .
- [23] S. J. Pan and Q. Yang (2009) A survey on transfer learning . IEEE Transactions on Knowledge and Data Engineering 22 ( 10 ), pp. 1345-1359 . Cited by: [§1](#S1.p2.1) , [§1](#S1.p4.1) .
- [24] K. Papineni, S. Roukos, T. Ward, and W. Zhu (2002) Bleu: a method for automatic evaluation of machine translation . In Proceedings of the 40th annual meeting of the Association for Computational Linguistics , pp. 311-318 . Cited by: [§5.1.4](#S5.SS1.SSS4.p1.1) .
- [25] Y. Said, S. Boubaker, S. M. Altowaijri, A. A. Alsheikhy, and M. Atri (2025) Adaptive transformer-based deep learning framework for continuous sign language recognition and translation . Mathematics 13 ( 6 ), pp. 909 . Cited by: [§2](#S2.p5.1) , [§2](#S2.p8.1) .
- [26] A. See, P. J. Liu, and C. D. Manning (2017-07) Get to the point: summarization with pointer-generator networks . In Proceedings of the 55th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers) , R. Barzilay and M. Kan (Eds.) , Vancouver, Canada , pp. 1073-1083 . External Links: [Link](https://aclanthology.org/P17-1099/) , [Document](https://dx.doi.org/10.18653/v1/P17-1099) Cited by: [§5.1.4](#S5.SS1.SSS4.p1.1) .
- [27] N. Shahin and L. Ismail (2024) From rule-based models to deep learning transformers architectures for natural language processing and sign language translation systems: survey, taxonomy and performance evaluation . Artificial Intelligence Review 57 ( 10 ), pp. 271 . Cited by: [§5.1.3](#S5.SS1.SSS3.p2.1) .
- [28] N. Shahin and L. Ismail (2024) GLoT: a novel gated-logarithmic transformer for efficient sign language translation . In 2024 IEEE Future Networks World Forum (FNWF) , pp. 885-890 . Cited by: [§1](#S1.p1.1) .
- [29] N. Shahin and L. Ismail (2025) Towards trustworthy sign language translation system: a privacy-preserving edge-cloud-blockchain approach . Mathematics 13 ( 23 ), pp. 3759 . Cited by: [§5.1.2](#S5.SS1.SSS2.p1.1) , [§5.3.1](#S5.SS3.SSS1.p11.1) .
- [30] N. Shahin and L. Ismail (2026) ADAT: time-series-aware adaptive transformer architecture for sign language translation . Scientific Reports . Cited by: [§1](#S1.p1.1) , [§1](#S1.p5.1) , [§5.1.1](#S5.SS1.SSS1.p1.1) , [§5.1.3](#S5.SS1.SSS3.p1.1) .
- [31] E. Soleimani and E. Nazerfard (2021) Cross-subject transfer learning in human activity recognition systems using generative adversarial networks . Neurocomputing 426 , pp. 26-34 . Cited by: [§1](#S1.p3.1) , [Table 1](#S2.T1.1.1.1.1.1.1.1.6.1.1.1) , [§2](#S2.p2.1) .
- [32] Y. Sung, J. Cho, and M. Bansal (2022) Vl-adapter: parameter-efficient transfer learning for vision-and-language tasks . In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition , pp. 5227-5237 . Cited by: [§1](#S1.p3.1) , [Table 1](#S2.T1.1.1.1.1.1.1.1.7.1.1.1) , [§2](#S2.p2.1) , [§2](#S2.p3.1) .
- [33] A. Vaswani, N. Shazeer, N. Parmar, J. Uszkoreit, L. Jones, A. N. Gomez, Ł. Kaiser, and I. Polosukhin (2017) Attention is all you need . Advances in Neural Information Processing Systems 30 . Cited by: [§1](#S1.p5.1) , [§5.1.3](#S5.SS1.SSS3.p1.1) .
- [34] A. Xiao, J. Huang, D. Guan, F. Zhan, and S. Lu (2022) Transfer learning from synthetic to real lidar point cloud for semantic segmentation . In Proceedings of the AAAI Conference on Artificial Intelligence , Vol. 36 , pp. 2795-2803 . Cited by: [§1](#S1.p3.1) , [Table 1](#S2.T1.1.1.1.1.1.1.1.4.1.1.1) , [§2](#S2.p2.1) .
- [35] F. Xue, Q. Wang, and G. Guo (2021) Transfer: learning relation-aware facial expression representations with transformers . In Proceedings of the IEEE/CVF International Conference on Computer Vision , pp. 3601-3610 . Cited by: [§1](#S1.p3.1) , [Table 1](#S2.T1.1.1.1.1.1.1.1.5.1.1.1) , [§2](#S2.p2.1) .
- [36] A. Yin, Z. Zhao, J. Liu, W. Jin, M. Zhang, X. Zeng, and X. He (2021) Simulslt: end-to-end simultaneous sign language translation . In Proceedings of the 29th ACM International Conference on Multimedia , pp. 4118-4127 . Cited by: [Table 2](#S2.T2.1.1.1.1.1.1.9.1.1.1) , [§2](#S2.p5.1) , [§2](#S2.p6.1) , [§2](#S2.p8.1) , [Table 5](#S5.T5.1.1.1.1.23.1) , [Table 5](#S5.T5.1.1.1.1.8.1) .
- [37] K. Yin and J. Read (2020-12) Better sign language translation with STMC-transformer . In Proceedings of the 28th International Conference on Computational Linguistics , D. Scott, N. Bel, and C. Zong (Eds.) , Barcelona, Spain (Online) , pp. 5975-5989 . External Links: [Link](https://aclanthology.org/2020.coling-main.525/) , [Document](https://dx.doi.org/10.18653/v1/2020.coling-main.525) Cited by: [Table 2](#S2.T2.1.1.1.1.1.1.11.1.1.1) , [§2](#S2.p5.1) , [§2](#S2.p6.1) , [§2](#S2.p8.1) , [Table 5](#S5.T5.1.1.1.1.10.1) , [Table 5](#S5.T5.1.1.1.1.27.1) .
- [38] B. Zhang, M. Müller, and R. Sennrich (2023) SLTUNET: a simple unified model for sign language translation . In The Eleventh International Conference on Learning Representations , Cited by: [Table 2](#S2.T2.1.1.1.1.1.1.15.1.1.1) , [§2](#S2.p5.1) , [§2](#S2.p6.1) , [§2](#S2.p8.1) , [§5.3.1](#S5.SS3.SSS1.p8.1) , [Table 5](#S5.T5.1.1.1.1.12.1) , [Table 5](#S5.T5.1.1.1.1.29.1) .
- [39] B. Zhou, Z. Chen, A. Clapés, J. Wan, Y. Liang, S. Escalera, Z. Lei, and D. Zhang (2023) Gloss-free sign language translation: improving from visual-language pretraining . In Proceedings of the IEEE/CVF International Conference on Computer Vision , pp. 20871-20881 . Cited by: [Table 6](#S5.T6.1.1.1.1.1.1.12.1) .
- [40] H. Zhou, W. Zhou, Y. Zhou, and H. Li (2021) Spatial-temporal multi-cue network for sign language recognition and translation . IEEE Transactions on Multimedia 24 , pp. 768-779 . Cited by: [Table 2](#S2.T2.1.1.1.1.1.1.7.1.1.1) , [§2](#S2.p5.1) , [§2](#S2.p6.1) , [§2](#S2.p8.1) , [Table 5](#S5.T5.1.1.1.1.9.1) .

## References

- [[758eb69d8500fd302441f2e9a470068064d228b0]] — Towards Trustworthy Sign Language Translation System: A Privacy-Preserving Edge–Cloud–Blockchain Approach (2025)
- [[66e1bf848f0f431a2a7fa1ddab600fc958503532]] — Isharah: A Large-Scale Multi-Scene Dataset for Continuous Sign Language Recognition (2025)
- [[264a75c8b7491b00c9441e014e367f6d765b5b37]] — ADAT: Time-Series-Aware Adaptive Transformer Architecture for Sign Language Translation (2025)
- [[bc843f1ef9c392849505738f8bef69481b54d057]] — Novel transfer learning based acoustic feature engineering for scene fake audio detection (2025)
- [[55c68e1bd539b2eded55f4a1be5468bdc4ccb78e]] — Adaptive Transformer-Based Deep Learning Framework for Continuous Sign Language Recognition and Translation (2025)
- [[59d51a6ebf4ed2790db5e60f0bda0b96e221639a]] — GLoT: A Novel Gated-Logarithmic Transformer for Efficient Sign Language Translation (2024)
- [[0a68e677fd3d3cf57c7e1e7f43e8e884748dcc5a]] — From rule-based models to deep learning transformers architectures for natural language processing and sign language translation systems: survey, taxonomy and performance evaluation (2024)
- [[92ce54389d2ed7412d1b6a11bbbef1b1d7035a5b]] — From Scarcity to Understanding: Transfer Learning for the Extremely Low Resource Irish Sign Language (2023)
- [[a6d677eb70cc5d9e621a8040a6254ecf68dd7c9a]] — Gloss-free Sign Language Translation: Improving from Visual-Language Pretraining (2023)
- [[3bbc8841012fdb5971d1c86dff528edd8590f1b8]] — SLTUNET: A Simple Unified Model for Sign Language Translation (2023)
- [[a17ea7a19f0956404817ea3af7c56597bc07297a]] — SignNet II: A Transformer-Based Two-Way Sign Language Translation Model (2022)
- [[78bc5b0a9fa28ccf2a580f36783e310d436a7874]] — Two-Stream Network for Sign Language Recognition and Translation (2022)
- [[dc7df4a50867025d043e993947959ae73dca66df]] — Transfer learning: a friendly introduction (2022)
- [[951aec8bb6ef4114a69a4cf5b7d49f3f78c09c58]] — MC-SLT: Towards Low-Resource Signer-Adaptive Sign Language Translation (2022)
- [[42c7b4f292a122a7cd4f112f708f686df06f9652]] — Sign language recognition and translation network based on multi-view data (2022)
- [[1412521affabd661e11e3b558b27c83fad949420]] — PYSKL: Towards Good Practices for Skeleton Action Recognition (2022)
- [[33703b1bfecb918aea4dcc2644a759f1de37c940]] — A Simple Multi-Modality Transfer Learning Baseline for Sign Language Translation (2022)
- [[55a19318cc93714802c7ac59e07651789749b20c]] — VL-ADAPTER: Parameter-Efficient Transfer Learning for Vision-and-Language Tasks (2021)
- [[90a8032116a100e483e3a99db76d2fe22c31ee14]] — Sign Language Translation with Hierarchical Spatio-Temporal Graph Neural Network (2021)
- [[ebf221bf7260e2d27b243b15909d89196f62f39b]] — TransFER: Learning Relation-aware Facial Expression Representations with Transformers (2021)
- [[2372e7b7dcab84495d9798d698ca6cfcf65959c0]] — Transfer Learning from Synthetic to Real LiDAR Point Cloud for Semantic Segmentation (2021)
- [[d76e2a01f914b81afacec214c302e82c000c65ef]] — Spatial-Temporal Multi-Cue Network for Sign Language Recognition and Translation (2021)
- [[7153c3b129f1e6423dea6afcdbb57466466cd2cc]] — Better Sign Language Translation with STMC-Transformer (2020)
- [[05dcdfece56d1869895f53ed581d8ad64118c05f]] — Sign Language Transformers: Joint End-to-End Sign Language Recognition and Translation (2020)
- [[41857ba53c1aa1691ade4db07628d53d1cca997c]] — Zero-Shot Multi-Speaker Text-To-Speech with State-Of-The-Art Neural Speaker Embeddings (2019)
- [[3934b53e3f677c1b580087f41c56d3971eec0b4a]] — Cross-Subject Transfer Learning in Human Activity Recognition Systems using Generative Adversarial Networks (2019)
- [[189fdef90e44c545e595ba24126963822815d0b7]] — Deaf children need language, not (just) speech (2019)
- [[644602c65a5d8f30e62be027eb7b47f7c335191a]] — Neural Sign Language Translation (2018)
- [[d44c20c48e764a546d00b9155a56b171b0dc04bc]] — Hierarchical LSTM for Sign Language Translation (2018)
- [[1e077413b25c4d34945cc2707e17e46ed4fe784a]] — Universal Language Model Fine-tuning for Text Classification (2018)
- [[204e3073870fae3d05bcbc2f6a8e263d9b72e776]] — Attention is All you Need (2017)
- [[668db48c6a79826456341680ee1175dfc4cced71]] — Get To The Point: Summarization with Pointer-Generator Networks (2017)
- [[a25fbcbbae1e8f79c4360d26aa11a3abf1a11972]] — A Survey on Transfer Learning (2010)
- [[d7da009f457917aa381619facfa5ffae9329a6e9]] — Bleu: a Method for Automatic Evaluation of Machine Translation (2002)
- [[5ab8a234f9b250b0972263c9ff83d786402cf104]] — VisioSLR: A Vision Data-Driven Framework for Sign Language Video Recognition and Performance Evaluation on Fine-Tuned YOLO Models (2025)
- [[9947567ffa7680e7bc227c59bd193ea13993373b]] — Signer Diversity-driven Data Augmentation for Signer-Independent Sign Language Translation (2024)
- [[388e73a75d8da3fb1edf9efa1356e5711f23e0e5]] — YOLOv5-Tassel: Detecting Tassels in RGB UAV Imagery With Improved YOLOv5 Based on Transfer Learning (2022)
- [[a97b13151ee3b3ddfc6f17c3cc04eaf827f00341]] — Hierarchical Recurrent Deep Fusion Using Adaptive Clip Summarization for Sign Language Translation (2020)
- “Mediapipe solutions guide,” ()

## Sources

- title: semanticscholar
- abstract: semanticscholar
- authors: semanticscholar
- topics: semanticscholar
- references: semanticscholar
- citations: semanticscholar
- fullText: ar5iv
- bibtex: semanticscholar

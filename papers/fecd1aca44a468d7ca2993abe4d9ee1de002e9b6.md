---
semanticScholarId: "fecd1aca44a468d7ca2993abe4d9ee1de002e9b6"
bibKey: null
year: 2024
title: "A Chinese Continuous Sign Language Dataset Based on Complex Environments"
doi: "10.48550/arXiv.2409.11960"
arxivId: "2409.11960"
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

# A Chinese Continuous Sign Language Dataset Based on Complex Environments

**Year:** [[2024]]
**Topics:** [[topics/computer-science|Computer Science]]
**Authors:** Qidan Zhu; Jing Li; Fei Yuan; JiaoJiao Fan; Quan Gan

## Links
- [Semantic Scholar](https://www.semanticscholar.org/paper/fecd1aca44a468d7ca2993abe4d9ee1de002e9b6)
- [arXiv:2409.11960](https://arxiv.org/abs/2409.11960)
- [DOI](https://doi.org/10.48550/arXiv.2409.11960)

## Abstract

The current bottleneck in continuous sign language recognition (CSLR) research lies in the fact that most publicly available datasets are limited to laboratory environments or television program recordings, resulting in a single background environment with uniform lighting, which significantly deviates from the diversity and complexity found in real-life scenarios. To address this challenge, we have constructed a new, large-scale dataset for Chinese continuous sign language (CSL) based on complex environments, termed the complex environment - chinese sign language dataset (CE-CSL). This dataset encompasses 5,988 continuous CSL video clips collected from daily life scenes, featuring more than 70 different complex backgrounds to ensure representativeness and generalization capability. To tackle the impact of complex backgrounds on CSLR performance, we propose a time-frequency network (TFNet) model for continuous sign language recognition. This model extracts frame-level features and then utilizes both temporal and spectral information to separately derive sequence features before fusion, aiming to achieve efficient and accurate CSLR. Experimental results demonstrate that our approach achieves significant performance improvements on the CE-CSL, validating its effectiveness under complex background conditions. Additionally, our proposed method has also yielded highly competitive results when applied to three publicly available CSL datasets.

## TL;DR

A time-frequency network (TFNet) model is proposed for continuous sign language recognition that extracts frame-level features and then utilizes both temporal and spectral information to separately derive sequence features before fusion, aiming to achieve efficient and accurate CSLR.

## BibTeX

```bibtex
@Article{Zhu2024ACC,
 author = {Qidan Zhu and Jing Li and Fei Yuan and JiaoJiao Fan and Quan Gan},
 booktitle = {arXiv.org},
 journal = {ArXiv},
 title = {A Chinese Continuous Sign Language Dataset Based on Complex Environments},
 volume = {abs/2409.11960},
 year = {2024}
}
```

## Full Text

# A Chinese Continuous Sign Language Dataset Based on Complex Environments

Qidan Zhu 1 ,

Jing Li

1∗ ,

Fei Yuan

2 ,

Jiaojiao Fan

3 ,

Quan Gan

1 *Corresponding authorEmail addresses: zhuqidan@hrbeu.edu.cn (Qidan Zhu), ljing@hrbeu.edu.cn (Jing Li), bohelion@hrbeu.edu.cn (Fei Yuan), beijingyuyisign@163.com(Jiaojiao Fan), gquan@hrbeu.edu.cn (Quan Gan) 1 College of Intelligent Systems Science and Engineering, Harbin Engineering University, Harbin, 150001, China 2 Northwest Institute of Mechanical and Electrical Engineering, Xianyang, 712099, China 3 Kyungil University, Daegu, 417418, Korea

###### Abstract

The current bottleneck in continuous sign language recognition (CSLR) research lies in the fact that most publicly available datasets are limited to laboratory environments or television program recordings, resulting in a single background environment with uniform lighting, which significantly deviates from the diversity and complexity found in real-life scenarios. To address this challenge, we have constructed a new, large-scale dataset for Chinese continuous sign language (CSL) based on complex environments, termed the complex environment - chinese sign language dataset (CE-CSL). This dataset encompasses 5,988 continuous CSL video clips collected from daily life scenes, featuring more than 70 different complex backgrounds to ensure representativeness and generalization capability. To tackle the impact of complex backgrounds on CSLR performance, we propose a time-frequency network (TFNet) model for continuous sign language recognition. This model extracts frame-level features and then utilizes both temporal and spectral information to separately derive sequence features before fusion, aiming to achieve efficient and accurate CSLR. Experimental results demonstrate that our approach achieves significant performance improvements on the CE-CSL, validating its effectiveness under complex background conditions. Additionally, our proposed method has also yielded highly competitive results when applied to three publicly available CSL datasets. Code and dataset is available at [https://github.com/woshisad159/TFNet.git](https://github.com/woshisad159/TFNet.git) .

###### Index Terms:

Continuous sign language dataset; Continuous sign language recognition; Complex backgrounds; Time-frequency features.

## I Introduction

Sign language, as a unique non-verbal language system, relies on rich hand movements, gesture forms, and body language, serving as the core communication mechanism within the deaf community [ [1](#bib.bib1) ] [ [2](#bib.bib2) ] [ [3](#bib.bib3) ] . Sign language recognition has always been a focal point for researchers, exemplifying interdisciplinary studies that integrate the essence of computer vision, natural language processing, and human-computer interaction technologies [ [4](#bib.bib4) ] [ [5](#bib.bib5) ] . The development of sign language recognition technology has also built a bridge for communication between the deaf and hearing populations. By real-time translation of sign language videos into understandable text or speech, this technology not only simplifies the complexity of cross-language communication but also demonstrates great potential in various fields such as education, employment, and public services [ [6](#bib.bib6) ] .

In the field of CSLR, achieving accurate recognition of continuous sign language relies heavily on having a high-quality CSL dataset [ [7](#bib.bib7) ] [ [8](#bib.bib8) ] [ [9](#bib.bib9) ] [ [10](#bib.bib10) ] . Koller et al. [ [11](#bib.bib11) ] constructed the PHOENIX14-2014 dataset by collecting weather forecast programs broadcasted by a German public television station, providing valuable resources for CSLR research. This dataset is based on demonstrations by professional sign language interpreters; however, its collection environment remains limited to the television studio, lacking the diversity of real-world contexts. Camgoz et al. [ [12](#bib.bib12) ] further expanded upon this by introducing the PHOENIX14-2014T dataset, increasing the volume of data and refining the definition of sign boundaries, thereby enhancing annotation accuracy. Although this dataset improves in terms of professionalism, it is still constrained by relatively idealized background conditions, making it difficult to comprehensively reflect the sign language communication scenarios of everyday life. Adaloglou et al. [ [13](#bib.bib13) ] , focusing on practical application scenarios, particularly emphasized communication between deaf individuals and public service institutions, such as police departments, hospitals, and citizen service centers. They meticulously designed five typical scenarios, simulating dialogues of varying difficulty levels, thus enhancing the practicality and authenticity of the dataset. However, even with these efforts, the specialized setting of the collection environment and the backgrounds of the participants still fall short of reflecting real life, limiting the representativeness of the dataset and the performance of models in real-world settings. Despite the significant role these datasets have played in advancing CSLR technology, they generally face a common challenge: a disconnect between the collection environment and real-life conditions, as illustrated in Figure 1.

Figure 1: Sample image sequences from four publicly available continuous sign language datasets. These image sequences illustrate that the datasets were collected in laboratory environments or during television programs, with the subjects against a plain-colored background and under uniform lighting conditions.

<!-- image -->

To overcome the limitations of existing continuous sign language datasets, particularly their disconnection from real-life scenarios, this study constructs a CSL dataset oriented towards practical application environments. The dataset aims to facilitate the seamless transition of CSLR technology from laboratory settings to everyday life, laying a solid foundation for barrier-free communication between the deaf and hearing communities. The construction process of the CE-CSL dataset strictly adheres to the principle of practical application orientation, collecting a large number of continuous sign language video materials derived from real-life scenarios, covering a wide range of situational variations and environmental complexities. After the completion of the CE-CSL dataset, we conducted a comprehensive evaluation using advanced deep learning models to verify its reliability and value as a research benchmark.

Furthermore, this study proposes a TFNet model for continuous sign language recognition. This model, after extracting frame-level features, utilizes information from both the temporal and spectral domains to extract sequential features separately, followed by fusion, ultimately achieving efficient and accurate semantic parsing. Experimental results show that our method achieves significant performance improvements on the CE-CSL dataset, demonstrating its effectiveness under complex background conditions. Additionally, our proposed method has also yielded highly competitive results when applied to three publicly available continuous sign language datasets.

In summary, the main contributions of this paper are as follows:

- ∙ ∙ \bullet We have constructed a Chinese Continuous Sign Language dataset CE-CSL dataset oriented towards practical application environments. This dataset, with its rich content and precise annotations, aims to provide a robust foundational resource for the advancement of CSLR technology.
- ∙ ∙ \bullet We propose a TFNet model for CSLR. This model, by leveraging information from both the temporal and spectral domains to extract sequence features, achieves efficient and accurate semantic parsing, significantly improving the accuracy of CSLR in complex environments.
- ∙ ∙ \bullet Our proposed TFNet model demonstrates state-of-the-art performance on the CE-CSL dataset. Additionally, it achieves highly competitive results on three other publicly available CSLR datasets, indicating that TFNet not only excels on the CE-CSL dataset but also exhibits high generality and robustness across different datasets.

## II Related Work

### II-A Continuous sign language dataset

A CSL dataset serves as an indispensable cornerstone for researching CSLR technology, with its quality directly determining the performance and application potential of recognition algorithms [ [16](#bib.bib16) ] [ [18](#bib.bib18) ] . In recent years, with the rapid development of artificial intelligence technologies, a series of CSL datasets have emerged, contributing significantly to the advancement of this field. Agris et al. [ [14](#bib.bib14) ] pioneered the creation of the SIGNUM sign language dataset, which includes rich samples of isolated words and continuous sentences performed by 25 signers of different genders and age groups. Although SIGNUM made initial explorations in diversity and corpus size, the limitation of 450 different German sign language words and 780 continuous sentences did not adequately meet the large-scale data requirements of deep learning algorithms. In 2015, Koller et al. [ [11](#bib.bib11) ] introduced the PHOENIX14-2014 dataset, which collected 6,841 continuous sentences through weather forecast programs on German public television, significantly enhancing the scale and practicality of the dataset. Building on this, Camgoz et al. [ [12](#bib.bib12) ] extended the dataset to create the PHOENIX14-2014T dataset, enhancing its professionalism and introducing refined sign boundary definitions, annotated by deaf experts, further improving the dataset's quality. Huang et al. [ [15](#bib.bib15) ] focused on Chinese sign language, collecting video data including RGB, depth, and body joint patterns using Microsoft Kinect cameras, providing a multimodal perspective for sign language recognition research. Adaloglou et al. [ [13](#bib.bib13) ] concentrated on practical application scenarios of sign language, building cases involving interactions with police departments, hospitals, and citizen service centers, enriching the diversity of scenes in the dataset. Niu et al. [ [17](#bib.bib17) ] utilized an automated data collection pipeline to systematically gather extensive continuous sign language videos from seven months of sign language news broadcasts by Hong Kong Television Broadcasts Limited (TVB), further expanding the publicly available data resources. Despite the critical role these datasets have played in advancing sign language recognition technology, most originate from laboratory environments or television programs, commonly featuring a single background and uniform lighting conditions, which differ significantly from real-life sign language communication scenarios. In Table I, we list some large-scale publicly available continuous sign language datasets based on video. Given the limitations of existing datasets, we have constructed a Chinese CSL dataset that truly reflects the complexity of real-life environments. Unlike previous datasets limited to laboratory settings or television programs, ours involves real-world collection by sign language performers, aiming to capture the dynamics of sign language in authentic scenarios, including varied backgrounds, natural lighting conditions, and rich contextual changes.

### II-B Continuous sign language recognition

In the field of CSLR, precise frame-level annotation has always been an insurmountable challenge, with its complexity and time-consuming nature limiting the scale and quality of datasets [ [19](#bib.bib19) ] . As a result, most research has focused on video-level annotation, treating CSLR as a weakly supervised learning problem, where there is no strict one-to-one correspondence between video frames and annotation sequences, adding to the difficulty of the recognition task [ [20](#bib.bib20) ] [ [21](#bib.bib21) ] [ [22](#bib.bib22) ] . However, with the rise of deep learning technologies, CSLR has seen revolutionary advancements [ [23](#bib.bib23) ] [ [24](#bib.bib24) ] [ [25](#bib.bib25) ] . The introduction of Convolutional Neural Network (CNN) has significantly improved the extraction of frame-level sign language features, while Recurrent Neural Network (RNN) have complemented static feature representations with their superior ability to handle temporal sequences, together forming the basic framework of current CSLR systems.

Hu et al. [ [26](#bib.bib26) ] innovatively introduced a correlation module capable of dynamically computing the correlation mapping between the current frame and adjacent frames, effectively identifying the trajectories of spatial patches, providing a new perspective for CSLR. Shi et al. [ [27](#bib.bib27) ] proposed an efficient training strategy that successfully transferred high-quality visual features to the task of continuous sign language recognition, significantly enhancing the recognition accuracy of the model. Zhu et al. [ [28](#bib.bib28) ] focused on dynamic attention mechanisms, which can effectively capture the nonlinear changes in local motion regions during the expression of sign language, generating dynamic descriptions of image changes, thereby further strengthening the model's ability to capture complex sign language dynamics. Gao et al. [ [29](#bib.bib29) ] , drawing inspiration from enhancement schemes in signal processing, innovatively designed a Temporal Lifting Pool, decomposing input signals into multiple sub-bands, each corresponding to a specific motion pattern, effectively enhancing the extraction capabilities of temporal features. Li et al. [ [30](#bib.bib30) ] dedicated themselves to constructing a multi-scale temporal feature network, which, through time receptive fields at different scales, significantly improved the flexibility and accuracy of sequence modeling by the model.

Addressing the challenges posed by complex backgrounds to sign language recognition, we propose a TFNet model for CSLR. This method aims to achieve efficient and accurate sign language recognition by extracting sequence features in both the temporal and frequency domains, opening up new avenues for the development of CSLR technology.

Figure 2: Illustration of Backgrounds in Selected Images from the CE-CSL Dataset.

<!-- image -->

## III Dataset and Methodology

### III-A CE-CSL dataset

To promote the transition of CSLR technology from laboratory environments to real-life applications, we have carefully constructed a publicly available Chinese Continuous Sign Language dataset named CE-CSL. Unlike the limitations of previous datasets, CE-CSL aims to simulate natural living scenarios, without restricting recording equipment, attire choices, or background environments, ensuring that the collected sign language videos closely resemble real-world application contexts.

The CE-CSL dataset encompasses 12 sign language performers (labeled A through L), including eight females and four males. Notably, performers I and J are hearing-impaired individuals, while the remaining performers are professional sign language interpreters, ensuring a diverse and authentic representation of sign language expressions within the dataset. The dataset comprises a total of 5,988 continuous sign language videos. According to strict division ratios, there are 4,973 sign language videos in the training set, 515 in the validation set, and 500 in the test set. These videos collectively involve 3,515 Chinese words, covering a broad range of daily communication needs. The video lengths vary widely, ranging from the shortest at 39 frames to the longest at 530 frames, showcasing the richness and flexibility of sign language expression. Detailed statistics of the CE-CSL dataset are presented in Table II.

We also provide a comprehensive listing of key parameters for each performer in Table III, including the recording equipment used, the number of videos, age, and gender, offering detailed baseline information for future research. Given the open setting for background environments, the CE-CSL dataset includes over 70 different living scenarios, greatly enriching the diversity of the data. To better understand the diversity of backgrounds in the CE-CSL dataset, we present a series of representative scenes in Figure 2, including indoor, outdoor, park, street, mall, office, and others, all sourced from our dataset. Through these images, one can clearly see the extensive range of scenarios covered by the CE-CSL dataset, further demonstrating its valuable contribution as a research resource and its significance in advancing the practical application of continuous sign language recognition technology.

### III-B Dataset annotation

As a visual language, sign language carries unique grammatical structures and lexical ordering that differ significantly from traditional written or spoken languages, making direct mapping challenging. Therefore, the CE-CSL dataset introduces deep involvement from professional sign language translators, who are responsible for converting sign glosses into video content. Additionally, the dataset provides spoken language translations as a reference to enhance multidimensional understanding. Notably, we have conducted meticulous word segmentation for the sign glosses, whereas the spoken language translations maintain complete sentence structures without segmentation.

The construction of the CE-CSL dataset relies on 12 professional sign language performers, including both professional sign language interpreters and hearing-impaired individuals, who jointly undertake the task of translating spoken language into sign glosses. This process involves a deep understanding of spoken language sentences, followed by their reformation into expressions that conform to sign language grammar, which are then solidified through video demonstrations. All videos and their corresponding annotations are subject to comprehensive review and correction by experienced sign language interpreters after individual tasks are completed, ensuring the accuracy and consistency of the dataset.

The current sign language environment in China exists in a state where both standard sign language and regional sign languages coexist. Although efforts have been made to promote a standard sign language dictionary (referred to as the dictionary), a unified standard has yet to be fully established. Against this backdrop, the CE-CSL dataset adopts an inclusive approach. During the transcription process, in addition to relying on standard sign language, regional sign languages are appropriately integrated, especially when there is no corresponding sign in the standard dictionary for a spoken word. For words that use regional sign languages, we explicitly label them in the annotations, as shown in Table IV, to ensure the transparency and traceability of the dataset.

The transcription of sign language is not a mechanical process but one guided by a series of norms. For instance, when encountering words that exist in written or spoken language but are missing from the sign language dictionary, we follow the intent of the sentence and select the most appropriate substitute words. When faced with multiple sign language expressions for synonyms listed in the dictionary, we append specific gesture versions after the words to ensure accuracy, as listed in Table V. These guidelines ensure the rigor and practicality of the CE-CSL dataset, providing researchers with reliable material for their studies.

In summary, the CE-CSL dataset not only demonstrates the richness of sign language videos in quantity but also exhibits professionalism and meticulous annotation and transcription processes, providing a solid data foundation for the advancement of sign language recognition technology. By integrating both standard and regional sign languages, along with rigorous transcription standards, it effectively propels the field of sign language recognition forward.

Figure 3: provides an overview of the new TFNet. First, a CNN is used to capture frame-level features, which are then split into two branches. One branch models the temporal sequence using 1D CNN + BiLSTM; the other branch transforms the features into the frequency domain using the Discrete Fourier Transform (DFT) and then models the frequency-domain sequence with 1D CNN + BiLSTM. Finally, a classifier is used to predict the sentence.

<!-- image -->

### III-C Methodology

This paper proposes a TFNet for CSLR, as illustrated in Figure 3. TFNet primarily consists of two key components: a frame-level feature extraction module and a sequence feature extraction module. Initially, in the frame-level feature extraction stage, we employ a CNN to efficiently extract feature information from frames of sign language videos. Subsequently, in the sequence feature extraction part, the model is designed with two independent yet complementary branches. In one branch, we model the temporal sequence using a combination of 1D CNN and Bidirectional Long Short-Term Memory Networks (Bi-LSTM) [ [31](#bib.bib31) ] to capture the temporal dynamics of sign language actions. In the other branch, we transform the temporal features into the frequency domain via Discrete Fourier Transform (DFT) [ [32](#bib.bib32) ] and similarly model the frequency-domain sequence using 1D CNN and Bi-LSTM to obtain sequence features within the frequency domain. Ultimately, the outputs from these two branches are merged and subjected to a classifier for joint prediction, thereby achieving effective recognition of sign language sentences.

1) TFNet: CSLR involves translating continuous sign language videos into written phrases or spoken language understandable by the general population. Let the size of the input continuous sign language video frames be T 𝑇 T , then the continuous sign language video V = ( x 1 , x 2 , ... , x T ) = { x t | ∈ 1 T ℝ T × C × H × W } V=(x\_{1},x\_{2},...,x\_{T})=\left\{x\_{t}\left|{}\_{1}^{T}\in\mathbb{R}^{T\times C\times H\times W}\right.\right\} , where x t subscript 𝑥 𝑡 x\_{t} is the image of the t-th frame in the video, H × W 𝐻 𝑊 H\times W is the dimension of x t subscript 𝑥 𝑡 x\_{t} , and C is the number of channels. In the TFNet model, we first extract frame-level features and then extract time-frequency sequence features. Let the frame-level feature extractor be F f subscript 𝐹 𝑓 F\_{f} , yielding the feature representation as follows:

|    | f  f  r  a  m  e  =  F  f  (  V  )  ∈  ℝ  T  ×  C  ′  subscript  𝑓  𝑓  𝑟  𝑎  𝑚  𝑒  subscript  𝐹  𝑓  𝑉  superscript  ℝ  𝑇  superscript  𝐶  ′  f\_{frame}=F\_{f}(V)\in\mathbb{R}^{T\times C^{\prime}}   |    | (1)   |
|----|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----|-------|

where f f  r  a  m  e subscript 𝑓 𝑓 𝑟 𝑎 𝑚 𝑒 f\_{frame} is the frame-level feature after extraction, and C ′ superscript 𝐶 ′ C^{\prime} is the number of channels after frame-level feature extraction. Then, the frame-level feature f f  r  a  m  e subscript 𝑓 𝑓 𝑟 𝑎 𝑚 𝑒 f\_{frame} is input into two branches. In one branch, f f  r  a  m  e subscript 𝑓 𝑓 𝑟 𝑎 𝑚 𝑒 f\_{frame} is directly fed into the temporal sequence feature extractor F sequences t subscript 𝐹 subscript sequences 𝑡 F\_{\mathrm{sequences}\_{t}} . In the other branch, f f  r  a  m  e subscript 𝑓 𝑓 𝑟 𝑎 𝑚 𝑒 f\_{frame} is first transformed via discrete Fourier transform to convert the temporal data into frequency domain data, which is then input into the frequency sequence feature extractor F sequences f subscript 𝐹 subscript sequences 𝑓 F\_{\mathrm{sequences}\_{f}} . The methods used by these two sequence feature extractors are the same (both being 1D CNN + Bi-LSTM), leading to the following:

|    | f  t  e  m  p  o  r  a  l  =  F  sequences  t  (  f  f  r  a  m  e  )  ∈  ℝ  T  ′  ×  C  ′′  subscript  𝑓  𝑡  𝑒  𝑚  𝑝  𝑜  𝑟  𝑎  𝑙  subscript  𝐹  subscript  sequences  𝑡  subscript  𝑓  𝑓  𝑟  𝑎  𝑚  𝑒  superscript  ℝ  superscript  𝑇  ′  superscript  𝐶  ′′  f\_{temporal}=F\_{\mathrm{sequences}\_{t}}(f\_{frame})\in\mathbb{R}^{T^{\prime}\times C^{\prime\prime}}   |    | (2)   |
|----|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----|-------|

|    | f  f  r  e  q  =  F  sequences  f  (  D  F  T  (  f  f  r  a  m  e  )  )  ∈  ℝ  T  ′  ×  C  ′′  subscript  𝑓  𝑓  𝑟  𝑒  𝑞  subscript  𝐹  subscript  sequences  𝑓  𝐷  𝐹  𝑇  subscript  𝑓  𝑓  𝑟  𝑎  𝑚  𝑒  superscript  ℝ  superscript  𝑇  ′  superscript  𝐶  ′′  f\_{freq}=F\_{\mathrm{sequences}\_{f}}(DFT(f\_{frame}))\in\mathbb{R}^{T^{\prime}\times C^{\prime\prime}}   |    | (3)   |
|----|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----|-------|

Among them, f t  e  m  p  o  r  a  l subscript 𝑓 𝑡 𝑒 𝑚 𝑝 𝑜 𝑟 𝑎 𝑙 f\_{temporal} represents the temporal domain sequence features after extraction, and f f  r  e  q subscript 𝑓 𝑓 𝑟 𝑒 𝑞 f\_{freq} represents the spectral domain sequence features after extraction. T ′ superscript 𝑇 ′ T^{\prime} is the length of the sequence features after downsampling in the time dimension, and C ′′ superscript 𝐶 ′′ C^{\prime\prime} is the number of channels after temporal sequence feature extraction. The size of the spectral domain sequence features is consistent with that of the temporal domain sequence features. Finally, the temporal domain sequence features f t  e  m  p  o  r  a  l subscript 𝑓 𝑡 𝑒 𝑚 𝑝 𝑜 𝑟 𝑎 𝑙 f\_{temporal} and the spectral domain sequence features f f  r  e  q subscript 𝑓 𝑓 𝑟 𝑒 𝑞 f\_{freq} are summed and passed through a fully connected layer for recognition:

|    | f  c  a  l  s  s  i  f  i  c  a  t  i  o  n  =  F  l  i  n  e  a  r  (  f  t  e  m  p  o  r  a  l  +  f  f  r  e  q  )  ∈  ℝ  T  ′  ×  l  subscript  𝑓  𝑐  𝑎  𝑙  𝑠  𝑠  𝑖  𝑓  𝑖  𝑐  𝑎  𝑡  𝑖  𝑜  𝑛  subscript  𝐹  𝑙  𝑖  𝑛  𝑒  𝑎  𝑟  subscript  𝑓  𝑡  𝑒  𝑚  𝑝  𝑜  𝑟  𝑎  𝑙  subscript  𝑓  𝑓  𝑟  𝑒  𝑞  superscript  ℝ  superscript  𝑇  ′  𝑙  f\_{calssification}=F\_{linear}(f\_{temporal}+f\_{freq})\in\mathbb{R}^{T^{\prime}\times l}   |    | (4)   |
|----|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----|-------|

Among them, f c  l  a  s  s  i  f  i  c  a  t  i  o  n subscript 𝑓 𝑐 𝑙 𝑎 𝑠 𝑠 𝑖 𝑓 𝑖 𝑐 𝑎 𝑡 𝑖 𝑜 𝑛 f\_{classification} represents the final recognition result, and l 𝑙 l is the number of words.

2) Loss Function: The overall loss function L s  u  m subscript 𝐿 𝑠 𝑢 𝑚 L\_{sum} of the TFNet model consists of three parts: two auxiliary VAE loss functions [ [33](#bib.bib33) ] , L V  A  E t subscript 𝐿 𝑉 𝐴 subscript 𝐸 𝑡 L\_{VAE\_{t}} and L V  A  E f subscript 𝐿 𝑉 𝐴 subscript 𝐸 𝑓 L\_{VAE\_{f}} , and a final CTC (Connectionist Temporal Classification) loss function [ [34](#bib.bib34) ] . Specifically, L V  A  E t subscript 𝐿 𝑉 𝐴 subscript 𝐸 𝑡 L\_{VAE\_{t}} denotes the VAE loss function applied to the temporal domain sequence features, and L V  A  E f subscript 𝐿 𝑉 𝐴 subscript 𝐸 𝑓 L\_{VAE\_{f}} denotes the VAE loss function applied to the spectral domain sequence features. The final CTC loss function is used to calculate the difference between the predicted sequence and the true labels, guiding the model to learn the correct sign language recognition path. Therefore, L s  u  m subscript 𝐿 𝑠 𝑢 𝑚 L\_{sum} is defined as follows:

|    | L  s  u  m  =  L  V  A  E  t  +  L  V  A  E  f  +  L  C  T  C  subscript  𝐿  𝑠  𝑢  𝑚  subscript  𝐿  𝑉  𝐴  subscript  𝐸  𝑡  subscript  𝐿  𝑉  𝐴  subscript  𝐸  𝑓  subscript  𝐿  𝐶  𝑇  𝐶  L\_{sum}=L\_{VAE\_{t}}+L\_{VAE\_{f}}+L\_{CTC}   |    | (5)   |
|----|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----|-------|

## IV Experiment

### IV-A Dataset and judgment criteria

In addition to the CE-CSL dataset constructed in this paper, we conducted experiments on three other large-scale publicly available datasets, including RWTH [ [11](#bib.bib11) ] , RWTH-T [ [12](#bib.bib12) ] , and CSL-Daily [ [16](#bib.bib16) ] , aimed at verifying the wide applicability and effectiveness of the proposed method. The RWTH dataset contains a total of 6841 different video clips, which is derived from sign language videos recorded by the German Weather Radio and Television (DWRT). The official pre-defined splits consist of a training set (5,672 videos), a validation set (540 videos), and a test set (629 videos). The RWTH-T dataset is an extended version of the RWTH dataset with an expanded size, where the dataset is subdivided into 7,096 training videos, 519 validation videos, and 642 test videos. The CSL-Daily dataset is a large Chinese sign language dataset with an annotated vocabulary of 2,000 words and a Chinese text vocabulary of 2,343 words. The dataset consists of 18,401 training samples, 1,077 validation samples, and 1,176 test samples.

We use Word Error Rate (WER) [ [11](#bib.bib11) ] as the evaluation criterion, which is widely applied in CSLR. WER is defined as the sum of the minimum number of insertion, substitution, and deletion operations required to transform the recognized sequence into the standard reference sequence. A lower WER indicates a better recognition performance, which is defined as follows.

|    | W  E  R  =  100  %  ×  i  n  s  +  d  e  l  +  s  u  b  s  u  m  𝑊  𝐸  𝑅  percent  100  𝑖  𝑛  𝑠  𝑑  𝑒  𝑙  𝑠  𝑢  𝑏  𝑠  𝑢  𝑚  WER=100\%\times\frac{ins+del+sub}{sum}   |    | (6)   |
|----|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|----|-------|

where ins represents the number of words to be inserted, d  e  l 𝑑 𝑒 𝑙 del represents the number of words to be deleted, s  u  b 𝑠 𝑢 𝑏 sub represents the number of words to be replaced, and s  u  m 𝑠 𝑢 𝑚 sum represents the total number of words in the label.

### IV-B Implementation rules

In our experimental implementation, the frame-level feature extraction component of the TFNet model utilizes the backbone of the MAM-FSD model [ [28](#bib.bib28) ] . We train the entire model using the Adam optimizer [ [44](#bib.bib44) ] , with an initial learning rate and weight factor set to 10 − 4 superscript 10 4 10^{-4} , and a batch size of 2. The graphics card used in the experiments is the RTX3090Ti, equipped with 24GB of GPU-dedicated memory. Data augmentation is performed using random cropping and random flipping. For random cropping, the input data size is 256 × 256 256 256 256\times 256 , and the cropped size after random cropping is 224 × 224 224 224 224\times 224 . For random flipping, the flipping probability is set to 0.5. Flipping and cropping are applied to the video sequence. Additionally, temporal enhancement is conducted by randomly lengthening or shortening the length of the video sequence by ±20%. Training is carried out for a total of 55 epochs, with the learning rate reduced by 80% at the 35th and 45th epochs. During model testing, only central cropping is used for data augmentation and a beam search algorithm with a beam width of 10 is employed in the final CTC decoding phase.

### IV-C Experimental results

The TFNet model is tested on RWTH, RWTH-T, CSL-Daily, and CE-CSL datasets, with the model recognition accuracies presented in Tables VI and VII.

As can be seen from Table VI, TFNet achieves highly competitive results compared to other advanced models. On the RWTH dataset, TFNet attains a validation error rate of 18.7% and a test error rate of 18.6%, performing excellently among all compared methods. Compared to the closest method, TwoStream-SLR [ [43](#bib.bib43) ] , TFNet achieves a lower error rate on the test set, indicating that TFNet not only fits the training data well but also generalizes effectively to unseen data. On the RWTH-T dataset, TFNet has a validation error rate of 18.0% and a test error rate of 19.1%, showing equally good performance. Relative to TwoStream-SLR, TFNet exhibits lower errors on the validation set, suggesting that TFNet is more reasonable in terms of model selection and hyperparameter tuning. Additionally, TFNet performs slightly better than TwoStream-SLR on the test set, which further confirms the generalization ability of TFNet. On the CSL-Daily dataset, TFNet achieves the best performance on this dataset compared to other methods with a validation error rate of 25.1% and a test error rate of 23.5%. Compared with the closest method TwoStream-SLR, TFNet shows better performance on the validation set and a significant improvement on the test set, indicating that TFNet possesses strong adaptability and robustness when dealing with large-scale complex sign language data.

In Table VII, we compare the performance of various CSLR methods on the CE-CSL dataset. As shown in Table VII, the test results of our proposed model on CE-CSL indicate its superior performance. We also analyze the performance of TFNet on CE-CSL from both quantitative and qualitative perspectives.

Quantitative Analysis: To evaluate the effectiveness of the proposed model, we conduct comparative experiments on the CE-CSL dataset. The results reveale significant advantages of our method. According to the data in Table VII, our model achieve WER of 42.1% and 41.9% on the validation and test sets respectively. Compared to the closest CSLR model MAM-FSD, which have WER values of 44.9% and 44.7% on the validation and test sets, our model demonstrates a reduction of 2.8%, highlighting the superiority of our proposed model in sign language recognition.

Qualitative Analysis: To delve deeper and provide an intuitive demonstration of the performance of different models in recognizing Chinese continuous sign language datasets in complex environments, we select several CSLR models and analyze their test results on the CE-CSL dataset. The analyzed results in Table VIII, aiming to offer a more intuitive perspective. With the results in Table VIII, we find that the TFNet model has the lowest recognition error rate, marking it as having the best recognition performance. This result reflects the model's excellent capability in handling complex backgrounds and continuous sign language videos.

### IV-D Ablation experiment

In this section, we conduct ablation experiments on the RWTH dataset to further validate the effectiveness of the model components. In the ablation experiments, we use WER as the metric, with smaller WER indicating better performance.

Ablation of different domain sequence features. We conduct experiments by combining temporal, spectral, and time-frequency domain sequence features after frame-level feature extraction to investigate the role of different domain sequence feature combinations in CSLR. The experimental results are shown in Table IX. As can be observed from Table IX, when using only temporal domain sequence features for recognition, the WERs for the validation and test sets are 19.5% and 19.1%, respectively. When using only spectral domain sequence features for recognition, the WERs are 19.7% and 20.0%, respectively. This indicates that using only temporal domain sequence features yields slightly better performance than using only spectral domain sequence features, with WERs reduced by 0.2% and 0.9%, respectively. Finally, by integrating temporal and spectral domain sequence features to form time-frequency domain sequence features for recognition, the results showed further improvements. Compared to using only temporal domain sequence features, the WER decreased by 0.8% and 0.5%, respectively, achieving even better results. This suggests that the integration of time-frequency domain sequence features can effectively enhance the performance of CSLR systems.

Ablation of different sequence feature extractors. Under the condition that the frame-level feature extractors of different models remain unchanged, we investigate the effect of replacing their respective sequence feature extractors with time-frequency sequence feature extractors. The experimental results are shown in Table X. From Table X, it can be seen that for different models, recognition using time-frequency sequence features results in a decrease in WER on the test set compared to the original sequence features. Specifically, the WER of MAM-FSD is reduced by 0.2%, the WER of CorrNet is reduced by 0.3%, and the WER of SEN is reduced by 1.7%. On the validation set, only the BER of the CorrNet model increases by 0.4%, while the performance of the remaining models on the validation set improves with the use of the time-frequency sequence feature extractor. This experimental result proves the sophistication of the time-frequency sequence feature extractor we used.

Ablation of Different Loss Combinations. We study the effects of various loss function combinations in the TFNet model by experimenting with different combinations of the CTC loss function L C  T  C subscript 𝐿 𝐶 𝑇 𝐶 L\_{CTC} , the temporal domain sequence feature VAE loss function L V  A  E t subscript 𝐿 𝑉 𝐴 subscript 𝐸 𝑡 L\_{VAE\_{t}} and the spectral domain sequence feature VAE loss function L V  A  E f subscript 𝐿 𝑉 𝐴 subscript 𝐸 𝑓 L\_{VAE\_{f}} . The experimental results are shown in Table XI. As can be observed from Table XI, using only L C  T  C subscript 𝐿 𝐶 𝑇 𝐶 L\_{CTC} results in WERs of 21.3% and 21.4% on the validation and test sets, respectively. When L C  T  C subscript 𝐿 𝐶 𝑇 𝐶 L\_{CTC} is combined with either of the VAE loss functions, there is an improvement in performance. Combining L C  T  C subscript 𝐿 𝐶 𝑇 𝐶 L\_{CTC} with L V  A  E t subscript 𝐿 𝑉 𝐴 subscript 𝐸 𝑡 L\_{VAE\_{t}} , the WERs on the validation and test sets decrease by 2.0% and 2.4%, respectively. Combining L C  T  C subscript 𝐿 𝐶 𝑇 𝐶 L\_{CTC} with L V  A  E f subscript 𝐿 𝑉 𝐴 subscript 𝐸 𝑓 L\_{VAE\_{f}} , the WERs on the validation and test sets decrease by 2.3% and 2.1%, respectively. When all three loss functions are combined, the WER reaches its minimum on both the validation and test sets, at 18.7% and 18.6%, respectively. The result indicates that combining the CTC loss function with the time-frequency domain sequence feature VAE loss functions can significantly enhance the performance of CSLR systems.

## V Conclusion

In this paper, we introduce a novel CE-CSL dataset designed for complex environments, aiming to facilitate the transition of CSLR from laboratory settings to real-life scenarios. The CE-CSL encompasses a rich variety of daily communication contexts, comprising a total of 5,988 continuous sign language videos, meticulously divided into a training set of 4,973 sign language videos, a validation set of 515 sign language videos, and a test set of 500 sign language videos. The dataset covers 3,515 Chinese words with a variety of video backgrounds, introducing more than 70 different environments, providing unprecedented complexity and realism for model training. Considering the impact of complex backgrounds on CSLR, we also propose the TFNet to achieve efficient and accurate recognition. On the validation and test sets of the CE-CSL, the TFNet achieves WERs of 42.1% and 41.9%, respectively. Experimental results indicate that the TFNet significantly improves recognition accuracy. Additionally, we applied our proposed method to three publicly available continuous sign language datasets and achieved highly competitive results.

## Acknowledgment

This work was supported in part by the Development Project of Ship Situational Intelligent Awareness System, China under Grant MC-201920-X01, in part by the National Natural Science Foundation of China under Grant 61673129, in part by the Young Talent Fund of Association for Science and Technology in Shaanxi, China under Grant qsy007.

Data availability The datasets used in the paper are cited properly.

Ethics approval The project uses publicly available data that has been subject to an exemption.

## Declarations

Conflict of interest The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

## References

- [1] R. Rastgoo, K. Kiani, and S. Escalera, "Sign language recognition: A deep survey," *Expert Systems with Applications* , vol. 164, p. 113794, 2021.
- [2] C. Wei, J. Zhao, W. Zhou, and H. Li, "Semantic boundary detection with reinforcement learning for continuous sign language recognition," *IEEE Transactions on Circuits and Systems for Video Technology* , vol. 31, no. 3, pp. 1138-1149, 2020.
- [3] W. Aditya, T. K. Shih, T. Thaipisutikul, A. S. Fitriajie, M. Gochoo, F. Utaminingrum, and C.-Y. Lin, "Novel spatio-temporal continuous sign language recognition using an attentive multi-feature network," *Sensors* , vol. 22, no. 17, p. 6452, 2022.
- [4] J. Pu, W. Zhou, H. Hu, and H. Li, "Boosting continuous sign language recognition via cross modality augmentation," in *Proceedings of the 28th ACM international conference on multimedia* , 2020, pp. 1497-1505.
- [5] A. Wadhawan and P. Kumar, "Sign language recognition systems: A decade systematic literature review," *Archives of computational methods in engineering* , vol. 28, pp. 785-813, 2021.
- [6] R. Cui, H. Liu, and C. Zhang, "Recurrent convolutional neural networks for continuous sign language recognition by staged optimization," in *Proceedings of the IEEE conference on computer vision and pattern recognition* , 2017, pp. 7361-7369.
- [7] D. Uthus, G. Tanzer, and M. Georg, "Youtube-asl: A large-scale, open-domain american sign language-english parallel corpus," *Advances in Neural Information Processing Systems* , vol. 36, 2024.
- [8] A. Duarte, S. Palaskar, L. Ventura, D. Ghadiyaram, K. DeHaan, F. Metze, J. Torres, and X. Giro-i Nieto, "How2sign: a large-scale multimodal dataset for continuous american sign language," in *Proceedings of the IEEE/CVF conference on computer vision and pattern recognition* , 2021, pp. 2735-2744.
- [9] O. Özdemir, A. A. Kındıroğlu, N. C. Camgöz, and L. Akarun, "Bosphorussign22k sign language recognition dataset," *arXiv preprint arXiv:2004.01283* , 2020.
- [10] L.-C. Wang, R. Wang, D.-H. Kong, and B.-C. Yin, "Similarity assessment model for chinese sign language videos," *IEEE Transactions on Multimedia* , vol. 16, no. 3, pp. 751-761, 2014.
- [11] O. Koller, J. Forster, and H. Ney, "Continuous sign language recognition: Towards large vocabulary statistical recognition systems handling multiple signers," *Computer Vision and Image Understanding* , vol. 141, pp. 108-125, 2015.
- [12] N. C. Camgoz, S. Hadfield, O. Koller, H. Ney, and R. Bowden, "Neural sign language translation," in *Proceedings of the IEEE conference on computer vision and pattern recognition* , 2018, pp. 7784-7793.
- [13] N. Adaloglou, T. Chatzis, I. Papastratis, A. Stergioulas, G. T. Papadopoulos, V. Zacharopoulou, G. J. Xydopoulos, K. Atzakas, D. Papazachariou, and P. Daras, "A comprehensive study on deep learning-based methods for sign language recognition," *IEEE transactions on multimedia* , vol. 24, pp. 1750-1762, 2021.
- [14] U. von Agris and K.-F. Kraiss, "Signum database: Video corpus for signer-independent continuous sign language recognition," in *4th Workshop on the Representation and Processing of Sign Languages: Corpora and Sign Language Technologies* , 2010, pp. 243-246.
- [15] J. Huang, W. Zhou, Q. Zhang, H. Li, and W. Li, "Video-based sign language recognition without temporal segmentation," in *Proceedings of the AAAI Conference on Artificial Intelligence* , vol. 32, no. 1, 2018.
- [16] H. Zhou, W. Zhou, W. Qi, J. Pu, and H. Li, "Improving sign language translation with monolingual data by sign back-translation," in *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition* , 2021, pp. 1316-1325.
- [17] Z. Niu, R. Zuo, B. Mak, and F. Wei, "A hong kong sign language corpus collected from sign-interpreted tv news," *arXiv preprint arXiv:2405.00980* , 2024.
- [18] S. Feng and T. Yuan, "Sign language translation based on new continuous sign language dataset," in *2022 IEEE International Conference on Artificial Intelligence and Computer Applications (ICAICA)* . IEEE, 2022, pp. 491-494.
- [19] A. Yin, T. Zhong, L. Tang, W. Jin, T. Jin, and Z. Zhao, "Gloss attention for gloss-free sign language translation," in *Proceedings of the IEEE/CVF conference on computer vision and pattern recognition* , 2023, pp. 2551-2562.
- [20] O. Koller, S. Zargaran, and H. Ney, "Re-sign: Re-aligned end-to-end sequence modelling with deep recurrent cnn-hmms," in *Proceedings of the IEEE conference on computer vision and pattern recognition* , 2017, pp. 4297-4305.
- [21] H. Hu, W. Zhao, W. Zhou, and H. Li, "Signbert+: Hand-model-aware self-supervised pre-training for sign language understanding," *IEEE Transactions on Pattern Analysis and Machine Intelligence* , vol. 45, no. 9, pp. 11 221-11 239, 2023.
- [22] F. Wei and Y. Chen, "Improving continuous sign language recognition with cross-lingual signs," in *Proceedings of the IEEE/CVF International Conference on Computer Vision* , 2023, pp. 23 612-23 621.
- [23] J. Ahn, Y. Jang, and J. S. Chung, "Slowfast network for continuous sign language recognition," in *ICASSP 2024-2024 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)* . IEEE, 2024, pp. 3920-3924.
- [24] J. Hu and L. Ni, "Transformer with sequence relative position for continuous sign language translation," in *International Conference on Advanced Algorithms and Neural Networks (AANN 2022)* , vol. 12285. SPIE, 2022, pp. 170-176.
- [25] R. Cui, H. Liu, and C. Zhang, "A deep neural framework for continuous sign language recognition by iterative training," *IEEE Transactions on Multimedia* , vol. 21, no. 7, pp. 1880-1891, 2019.
- [26] L. Hu, L. Gao, Z. Liu, and W. Feng, "Continuous sign language recognition with correlation network," in *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition* , 2023, pp. 2529-2539.
- [27] L. Hu, T. Shi, L. Gao, Z. Liu, and W. Feng, "Improving continuous sign language recognition with adapted image models," *arXiv preprint arXiv:2404.08226* , 2024.
- [28] Q. Zhu, J. Li, F. Yuan, and Q. Gan, "Continuous sign language recognition based on motor attention mechanism and frame-level self-distillation," *arXiv preprint arXiv:2402.19118* , 2024.
- [29] L. Hu, L. Gao, Z. Liu, and W. Feng, "Temporal lift pooling for continuous sign language recognition," in *European conference on computer vision* . Springer, 2022, pp. 511-527.
- [30] Q. Zhu, J. Li, F. Yuan, and Q. Gan, "Multiscale temporal network for continuous sign language recognition," *Journal of Electronic Imaging* , vol. 33, no. 2, pp. 023 059-023 059, 2024.
- [31] A. Graves, A.-r. Mohamed, and G. Hinton, "Speech recognition with deep recurrent neural networks," in *2013 IEEE international conference on acoustics, speech and signal processing* . Ieee, 2013, pp. 6645-6649.
- [32] M. Cai, H. Zhang, H. Huang, Q. Geng, Y. Li, and G. Huang, "Frequency domain image translation: More photo-realistic, better identity-preserving," in *Proceedings of the IEEE/CVF International Conference on Computer Vision* , 2021, pp. 13 930-13 940.
- [33] Y. Min, A. Hao, X. Chai, and X. Chen, "Visual alignment constraint for continuous sign language recognition," in *Proceedings of the IEEE/CVF international conference on computer vision* , 2021, pp. 11 542-11 551.
- [34] A. Graves, S. Fernández, F. Gomez, and J. Schmidhuber, "Connectionist temporal classification: labelling unsegmented sequence data with recurrent neural networks," in *Proceedings of the 23rd international conference on Machine learning* , 2006, pp. 369-376.
- [35] L. Hu, L. Gao, Z. Liu, and W. Feng, "Self-emphasizing network for continuous sign language recognition," in *Proceedings of the AAAI Conference on Artificial Intelligence* , vol. 37, no. 1, 2023, pp. 854-862.
- [36] --, "Scalable frame resolution for efficient continuous sign language recognition," *Pattern Recognition* , vol. 145, p. 109903, 2024.
- [37] H. Zhou, W. Zhou, Y. Zhou, and H. Li, "Spatial-temporal multi-cue network for continuous sign language recognition," in *Proceedings of the AAAI conference on artificial intelligence* , vol. 34, no. 07, 2020, pp. 13 009-13 016.
- [38] W. Yin, Y. Hou, Z. Guo, and K. Liu, "Spatial temporal enhanced network for continuous sign language recognition," *IEEE Transactions on Circuits and Systems for Video Technology* , 2023.
- [39] J. Kan, K. Hu, M. Hagenbuchner, A. C. Tsoi, M. Bennamoun, and Z. Wang, "Sign language translation with hierarchical spatio-temporal graph neural network," in *Proceedings of the IEEE/CVF winter conference on applications of computer vision* , 2022, pp. 3367-3376.
- [40] S. WANG, L. GUO, and W. XUE, "Dynamical semantic enhancement network for continuous sign language recognition," 2024.
- [41] J. Liu, W. Xue, K. Zhang, T. Yuan, and S. Chen, "Tb-net: Intra-and inter-video correlation learning for continuous sign language recognition," *Information Fusion* , vol. 109, p. 102438, 2024.
- [42] H. Lu, A. A. Salah, and R. Poppe, "Tcnet: Continuous sign language recognition from trajectories and correlated regions," in *Proceedings of the AAAI Conference on Artificial Intelligence* , vol. 38, no. 4, 2024, pp. 3891-3899.
- [43] Y. Chen, R. Zuo, F. Wei, Y. Wu, S. Liu, and B. Mak, "Two-stream network for sign language recognition and translation," *Advances in Neural Information Processing Systems* , vol. 35, pp. 17 043-17 056, 2022.
- [44] D. P. Kingma, "Adam: A method for stochastic optimization," *arXiv preprint arXiv:1412.6980* , 2014.

## References

- [[e1a1709997ee2020b38008eceef9901f1328d5ad]] — Dynamical semantic enhancement network for continuous sign language recognition (2024)
- [[526a206b32ff198ba77a4808eec254821f1a6102]] — TB-Net: Intra- and inter-video correlation learning for continuous sign language recognition (2024)
- [[eabce17185aa25bdd86d675f8958d7cfabe3938b]] — A Hong Kong Sign Language Corpus Collected from Sign-interpreted TV News (2024)
- [[b747b65db2d8a32080f57401d39147acfe9276a2]] — Improving Continuous Sign Language Recognition with Adapted Image Models (2024)
- [[866dec836ea1733952b7b99a0a57e290ff54a114]] — TCNet: Continuous Sign Language Recognition from Trajectories and Correlated Regions (2024)
- [[22f53e185955378702b5fdba4282fba96c8d7f50]] — Spatial–Temporal Enhanced Network for Continuous Sign Language Recognition (2024)
- [[2baa74ba055b1fc993ea19ea61df41ab5c8c2713]] — Continuous sign language recognition based on motor attention mechanism and frame-level self-distillation (2024)
- [[2d9143c8b68c3d34198bbdc75a6a8e90022b83a5]] — Slowfast Network for Continuous Sign Language Recognition (2023)
- [[33a1ded05faa8ddb136fcec3d27551be6717010b]] — Improving Continuous Sign Language Recognition with Cross-Lingual Signs (2023)
- [[c4c985700f4dc2b391d052e103fce3664c570a14]] — Scalable frame resolution for efficient continuous sign language recognition (2023)
- [[ce80cb3b1368364ad4bdb948d4d17e3f076f0a76]] — YouTube-ASL: A Large-Scale, Open-Domain American Sign Language-English Parallel Corpus (2023)
- [[fc70ce5adfdd9602a1866cd329684277042b9dff]] — Gloss Attention for Gloss-free Sign Language Translation (2023)
- [[0fcc797aeed56bcc127476d5b68836dc402021ea]] — SignBERT+: Hand-Model-Aware Self-Supervised Pre-Training for Sign Language Understanding (2023)
- [[d9c38e7957c10252cc0e66b20c55d5be615db10d]] — Continuous Sign Language Recognition with Correlation Network (2023)
- [[1f55d35e1d1a148898a756cb0380b22fa8878dcb]] — Self-Emphasizing Network for Continuous Sign Language Recognition (2022)
- [[78bc5b0a9fa28ccf2a580f36783e310d436a7874]] — Two-Stream Network for Sign Language Recognition and Translation (2022)
- [[be8d6bb40020d93d3add4d6ce734025f5264605a]] — Novel Spatio-Temporal Continuous Sign Language Recognition Using an Attentive Multi-Feature Network (2022)
- [[630348d3e789ac1775223fac9d0b64f99e4b469c]] — Temporal Lift Pooling for Continuous Sign Language Recognition (2022)
- [[5fb187ffd32682ac60e9182360c0e53d5f563c16]] — Sign language translation based on new continuous sign language dataset (2022)
- [[ae8a202ed159cd70a3eb49e3aba603ec52adc5e6]] — Transformer with sequence relative position for continuous sign language translation (2022)
- [[3134a48116e9d79fb9c931fd448e8aea30e5dfd4]] — Multiscale temporal network for continuous sign language recognition (2022)
- [[90a8032116a100e483e3a99db76d2fe22c31ee14]] — Sign Language Translation with Hierarchical Spatio-Temporal Graph Neural Network (2021)
- [[a514cc9796034bcc01450ac968b2f576fa35c70f]] — Multi-Scale Local-Temporal Similarity Fusion for Continuous Sign Language Recognition (2021)
- [[7811df11a75f58646d04b3132d35f0656e50a109]] — Improving Sign Language Translation with Monolingual Data by Sign Back-Translation (2021)
- [[2d2d5bb1d025c5e17abe13716599c93e1f131927]] — Visual Alignment Constraint for Continuous Sign Language Recognition (2021)
- [[0536805fe0f9b621dcdbd90ccf34b6b1387cfa3c]] — A Comprehensive Study on Deep Learning-Based Methods for Sign Language Recognition (2021)
- [[06aa3a4d61b2856c39789cfeb3a5065db189e63c]] — Semantic Boundary Detection With Reinforcement Learning for Continuous Sign Language Recognition (2021)
- [[d10cb838533c33aad406a4ad3dc515113f7155b3]] — Sign Language Recognition: A Deep Survey (2021)
- [[649781bce69cb931991169ad21670fe0ec5e4de3]] — Frequency Domain Image Translation: More Photo-realistic, Better Identity-preserving (2020)
- [[ce50fa888551b640fe3dddc57289c27f325c029b]] — Boosting Continuous Sign Language Recognition via Cross Modality Augmentation (2020)
- [[932168d1c27390506049adf679b42d3aac53f61c]] — How2Sign: A Large-scale Multimodal Dataset for Continuous American Sign Language (2020)
- [[6af09da568edee80075ec610f431ffa91bfce061]] — Fully Convolutional Networks for Continuous Sign Language Recognition (2020)
- [[d97d2fe18aa00be936fa8492a0c394f3b6791ed4]] — BosphorusSign22k Sign Language Recognition Dataset (2020)
- [[a1e2665ac39dcb389e12f3f993004b4b4651826d]] — Spatial-Temporal Multi-Cue Network for Continuous Sign Language Recognition (2020)
- [[138dc2b855739f9ca10419626aab336a9fd7d3ac]] — Sign Language Recognition Systems: A Decade Systematic Literature Review (2019)
- [[f96ffd8c71b97e46eb3ba48263c9012d197494d4]] — A Deep Neural Framework for Continuous Sign Language Recognition by Iterative Training (2019)
- [[644602c65a5d8f30e62be027eb7b47f7c335191a]] — Neural Sign Language Translation (2018)
- [[a274fcf985aaec1f009cfe4b4042733321a5a8b4]] — Video-based Sign Language Recognition without Temporal Segmentation (2018)
- [[28b85543e8f12c3d2d2227dcc9f5e87c685535ea]] — Re-Sign: Re-Aligned End-to-End Sequence Modelling with Deep Recurrent CNN-HMMs (2017)
- [[a3c850001340266d4b2e7479f78387b5fda0815c]] — Recurrent Convolutional Neural Networks for Continuous Sign Language Recognition by Staged Optimization (2017)
- [[562737212e6e63c75689a28f72d132ee3183cff3]] — Continuous sign language recognition: Towards large vocabulary statistical recognition systems handling multiple signers (2015)
- [[a6cb366736791bcccc5c8639de5a8f9636bf87e8]] — Adam: A Method for Stochastic Optimization (2014)
- [[e0386991589ca9b95d6d366dfc26f04d7d5cf244]] — Similarity Assessment Model for Chinese Sign Language Videos (2014)
- [[4177ec52d1b80ed57f2e72b0f9a42365f1a8598d]] — Speech recognition with deep recurrent neural networks (2013)
- “Connection-ist temporal classification: labelling unsegmented sequence data with recurrent neural networks,” (2006)

## Cited by

- [[ab8ed45571624b673746c75abaa246d27b87d580]] — An explainable hybrid CNN–transformer model for sign language recognition on edge devices using adaptive fusion and knowledge distillation (2026)
- [[5d341d5a03f1499bda6de6e1896236825bbbb69d]] — Advances in Automatic Sign Language Translation: A Survey of Techniques and Systems (2026)
- [[416e62a0551affacd2d0617997d2586ee8062152]] — iLSU-T: an Open Dataset for Uruguayan Sign Language Translation (2025)

## Sources

- title: semanticscholar
- abstract: semanticscholar
- authors: semanticscholar
- topics: semanticscholar
- references: semanticscholar
- citations: semanticscholar
- fullText: ar5iv
- bibtex: semanticscholar

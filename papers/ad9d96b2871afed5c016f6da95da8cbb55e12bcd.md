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
fullText: "extracted"
fullTextSource: "ar5iv"
bibtexSource: "ours"
sources:
  title: semanticscholar
  abstract: semanticscholar
  authors: semanticscholar
  topics: semanticscholar
  references: semanticscholar
  citations: semanticscholar
  fullText: ar5iv
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

## Full Text

# Aligning Subtitles in Sign Language Videos

Hannah Bull 1 Triantafyllos Afouras 2∗ Gül Varol 2,3 Samuel Albanie 2 Liliane Momeni 2 Andrew Zisserman 2 1 LISN, Univ Paris-Saclay, CNRS, France 2 Visual Geometry Group, University of Oxford, UK 3 LIGM, École des Ponts, Univ Gustave Eiffel, CNRS, France hannah.bull@lisn.upsaclay.fr; {afourast,gul,albanie,liliane,az}@robots.ox.ac.uk [https://www.robots.ox.ac.uk/~vgg/research/bslalign/](https://www.robots.ox.ac.uk/~vgg/research/bslalign/) Equal contribution

###### Abstract

The goal of this work is to temporally

align asynchronous subtitles in sign language videos.

In particular, we focus on sign-language

interpreted TV broadcast data comprising

(i) a video of continuous signing, and (ii) subtitles

corresponding to the audio content.

Previous work exploiting such weakly-aligned

data only considered finding keyword-sign correspondences,

whereas we aim to localise a complete

subtitle text in continuous signing.

We propose a Transformer architecture

tailored for this task, which we train on

manually annotated alignments covering over 15K subtitles

that span 17.7 hours of video.

We use BERT subtitle embeddings

and CNN video representations learned for sign recognition

to encode the two signals, which interact through

a series of attention layers. Our model outputs

frame-level predictions, i.e.,

for each video frame, whether it belongs to the queried subtitle or not.

Through

extensive evaluations, we show

substantial improvements over existing alignment baselines that do not make use of subtitle text embeddings for learning. Our automatic alignment

model opens up possibilities for advancing

machine translation of sign languages via

providing continuously synchronized video-text data.

{strip}

[Uncaptioned image]

<!-- image -->

Figure 1: Subtitle alignment : We study the task of aligning subtitles to continuous signing in sign language interpreted TV broadcast data. The subtitles in such settings usually correspond to and are aligned with the audio content (top: audio subtitles, S a  u  d  i  o subscript 𝑆 𝑎 𝑢 𝑑 𝑖 𝑜 S\_{audio} )

but are unaligned with the accompanying signing (bottom: Ground Truth annotation of the signing corresponding to the subtitle, S g  t subscript 𝑆 𝑔 𝑡 S\_{gt} ).

This is a very challenging task as (i) the order of subtitles varies between spoken and sign languages, (ii) the duration of a subtitle differs considerably between signing and speech, and (iii) the signing corresponds to a translation of the speech as opposed to a transcription.

## 1 Introduction

Sign languages constitute a key form of communication for Deaf

communities [

[53](#bib.bib53) ] .

Our goal in this paper is to temporally localise subtitles in continuous

signing video. Automatic alignment of subtitle text to signing content has

great potential for a wide range of applications including

assistive tools for education and translation,

indexing of sign language video corpora,

efficient subtitling technology for signing vloggers

1 1 1 Unlike

spoken vlogs that benefit from automatic closed captioning on sites such as

YouTube, signing vlog creators who wish to provide written subtitles must both

translate and align their subtitles manually. , and

automatic construction

of large-scale sign language datasets that support computer vision and linguistic research.

Despite recent advances in computer vision, machine translation between

continuous signing and written language remains largely

unsolved [

[5](#bib.bib5) ] .

Recent works [

[10](#bib.bib10) , [11](#bib.bib11) ] have shown promising translation results, but to date these have been achieved only in constrained settings where continuous signing is manually

pre-segmented into clips, with each clip associated to a written sentence from

a limited vocabulary .

Two key bottlenecks for scaling up translation

to continuous signing depicting unconstrained vocabularies are (i) the

segmentation of signing into sentence-like units, and (ii) the availability of

large-scale sign language training data.

Manual alignment of subtitles to sign language video is tedious - an expert fluent in sign language takes approximately 10-15 hours to align subtitles to 1 hour of continuous sign language video. In this work, we focus on the task of aligning a particular known subtitle

within a given temporal signing window. We explore this task in the context of

sign language interpreted TV broadcast footage - a readily available and

large-scale source of data - where the subtitles are synchronised with the

audio, but the corresponding sign language translations are largely unaligned

due to differences between spoken and sign languages as well as lags from the

live interpretation.

Subtitle alignment to continuous signing remains a very challenging task. First, sign languages have grammatical structures

that vary considerably from those of spoken languages [

[53](#bib.bib53) ] , and as

a result the ordering of words within a subtitle as well as the subtitles

themselves is often not maintained in the signing (see Fig. Aligning Subtitles in Sign Language Videos ). Second, the duration of a subtitle varies considerably between signing and speech due to

differences in speed and grammar. Third, the signing corresponds to a translation of the speech that appears in the subtitles as opposed to a transcription: there

is no direct one-to-one mapping between subtitle words and signs produced by interpreters,

and entire subtitles may not be signed.

Previous work exploiting such weakly-aligned data has mainly focused on finding sparse

correspondences between keywords in the subtitle and individual

signs [

[2](#bib.bib2) , [42](#bib.bib42) , [56](#bib.bib56) ] , as opposed to localising the start and end times

of a complete subtitle text in continuous signing. Though, as we show, localising isolated

signs identified by keyword spotting nevertheless forms a useful pretraining task for full

subtitle alignment. Most closely related to our work, Bull et al. [

[8](#bib.bib8) ] consider

the task of segmenting a continuous signing video into subtitle units purely based on body

keypoints. In fact, similarly to speech which can be segmented based on prosodic cues such

as pauses, sign sentence boundaries can to an extent be detected through visual

cues such as lowering the hands, head movement, pauses, and facial expressions [

[24](#bib.bib24) ] .

However, as shown in our evaluations in Sec.

[4](#S4) , such approaches based on

prosody-only perform poorly in our setting, where subtitles do not necessarily correspond to

complete sign sentences with clear visual boundaries.

In this paper, we instead propose to use the subtitle text as an additional signal for better alignment. We make the following three contributions:

(1) we show that encoding the subtitle text

as input to the alignment model significantly

improves the temporal localisation quality

as opposed to only relying on visual cues

to segment continuous sign language videos into subtitle units;

(2) we design a novel formulation

for the subtitle alignment task based on

Transformers; and (3) we present a comprehensive study

ablating our design choices and provide

promising results for this new task

when evaluating on unseen signers and content.

## 2 Related Work

For a recent comprehensive survey about

sign language recognition and translation,

see [

[33](#bib.bib33) ] .

Here, we review relevant works on

temporal localisation at the levels of individual signs and sequences,

in addition to

more general temporal alignment methods from the literature.

Temporal localisation of individual signs. A rich body of work has

considered the task of localising sparse sign instances in continuous signing, often

referred to as "sign spotting". Early efforts using signing gloves [

[38](#bib.bib38) ] were followed by methods employing hand-crafted visual features to represent the hands, face

and motion that were integrated with CRFs [

[62](#bib.bib62) , [61](#bib.bib61) ] ,

HMMs [

[49](#bib.bib49) ] and HSP Trees [ [45](#bib.bib45) ] .

Several studies have sought to employ subtitles as weak supervision for learning to localise

and classify signs, using apriori mining [

[17](#bib.bib17) ] and multiple-instance

learning [

[6](#bib.bib6) , [7](#bib.bib7) , [46](#bib.bib46) ] .

More recent work has leveraged cues such as mouthings [

[2](#bib.bib2) ] and visual

dictionaries [

[42](#bib.bib42) ] and by making use of deep neural network features with sliding

window classifiers [

[37](#bib.bib37) ] and attention learned via a proxy translation

task [

[56](#bib.bib56) ] . In deviation from these works, our objective is to localise complete

subtitle units, rather than individual signs.

Temporal localisation of sign sequences. The alignment of subtitles to

continuous signing was considered in creative early work by combining cues from multiple

sparse correspondences [

[23](#bib.bib23) ] , but under the assumption that ordering of

words in subtitles are preserved in the signing (which does not hold in our problem setting).

Figure 2: SAT model overview: We input to our model (i) token embeddings of the subtitle text we wish to align, (ii) a sequence of video features extracted from a continuous sign language video segment and (iii) the shifted temporal boundaries of the audio-aligned subtitle, S prior . Using these inputs, the model outputs a vector of values between 0 and 1 of length T 𝑇 T . Its first and last values above a threshold τ 𝜏 \tau delimit the predicted temporal boundaries for the query subtitle. The location of the subtitle with respect to the window is represented in dashed yellow.

<!-- image -->

Other sequence-level sign language temporal localisation tasks that have received attention

in the literature include category-agnostic sign

segmentation [

[22](#bib.bib22) , [47](#bib.bib47) ] , active signer

detection [

[16](#bib.bib16) , [4](#bib.bib4) , [43](#bib.bib43) , [52](#bib.bib52) ] and diarisation [ [27](#bib.bib27) , [26](#bib.bib26) , [1](#bib.bib1) ] -each

considers a temporal granularity that differs from subtitle units.

Most closely related to our work, Bull et al. [

[8](#bib.bib8) ] employ a keypoint-based model to

segment continuous signing into sentence-like units without knowledge of the written

subtitles during inference. Our approach relaxes this assumption and considers instead the

practical scenario

in which we assume access to the written subtitle to be aligned. We compare our approach with theirs in Sec.

[4](#S4) .

Continuous sign language recognition. Hybrid models coupling CNNs with HMMs [ [34](#bib.bib34) , [35](#bib.bib35) ] , attention

mechanisms [

[31](#bib.bib31) ] and CTC losses [ [9](#bib.bib9) , [15](#bib.bib15) ] have been studied for continuous sign language recognition, with recent extensions to

sequence-to-sequence models [

[10](#bib.bib10) ] and

Transformers [

[11](#bib.bib11) , [36](#bib.bib36) ] to tackle the task of sign language

translation. These models produce either implicit or explicit alignments over a signing

sequence corresponding to a sentence. However, these approaches have only been demonstrated

to work on pre-segmented sentences of signing [

[10](#bib.bib10) ] .

Aligning bodies of text to video. The Dynamic Time Warping (DTW) algorithm [ [44](#bib.bib44) ] has been applied to the problem of

aligning sequences of movies to

transcripts [

[21](#bib.bib21) , [48](#bib.bib48) ] and plots

synopses [

[54](#bib.bib54) ] using cues such as character recognition and

subtitle content. It has also been successfully applied to the problem of aligning generic

text descriptions against untrimmed video [

[3](#bib.bib3) ] . While

effective, these methods require the preservation of sequence ordering across modalities,

which does not hold in our problem setting. We nevertheless show in Sec.

[3](#S3) how DTW can be used as a secondary stage of processing that resolves conflicting local

alignments on the re-ordered subtitle prediction timings via a global objective. The fixed

ordering assumption is relaxed by the work of [

[55](#bib.bib55) ] , which aligns

book chapters to video scenes. Their approach, however, which works through matching sparse

character identifications against specific shots, is not applicable in our setting where

shot boundaries do not provide a natural segmentation of the signing content.

Natural language grounding in videos. Our work is also related to the task

of natural language grounding, which aims to locate a temporal segment within an untrimmed

video sequence corresponding to a given natural language query. Existing methods have

considered two-stage propose and rank approaches [

[30](#bib.bib30) , [25](#bib.bib25) , [39](#bib.bib39) , [59](#bib.bib59) ] ,

iterative grounding agents trained with reinforcement

learning [

[29](#bib.bib29) , [58](#bib.bib58) ] and single-stage regression

models [

[63](#bib.bib63) , [28](#bib.bib28) , [14](#bib.bib14) , [64](#bib.bib64) ] .

Our proposed subtitle alignment task differs from natural language grounding in three ways:

(i) The signing content is more fine-grained -the visual appearance of a signing

sequence remains very similar across frames, necessitating nuanced recognition of body dynamics;

(ii) Differently from language grounding, each subtitle to be aligned comes with its own

reference location, providing an instance-specific prior over the start time and duration.

As we show in Sec.

[4](#S4) , our effective use of this reference is important to

achieving good performance, and our model is specifically designed to take advantage of this

cue; (iii) Subtitles occupy mutually exclusive temporal regions, a property that we further

exploit to improve alignment quality, but that does not hold in general for natural language grounding.

## 3 Method

In this section, we describe our Transformer-based subtitle alignment model operating on a

single subtitle and a short video segment (Sec.

[3.1](#S3.SS1) ), our pretraining on sparse

sign spottings (Sec.

[3.2](#S3.SS2) ), and our final step that globally adjusts

multiple subtitles in a long video using DTW (Sec.

[3.3](#S3.SS3) ).

Problem formulation. As inputs to the model, we provide

(i) token embeddings of the subtitle text we wish to align to signing,

(ii) a sequence of video features extracted from a continuous sign language video segment,

as well as

(iii) prior estimates of the temporal boundaries for the given query, which we refer to as S

prior .

The latter is provided as an approximate location and duration cue of

the signing-aligned subtitle.

Using these inputs, we predict a binary vector of the same length as the video features,

where a consecutive sequence of 1s denotes the temporal location of the subtitle.

### 3.1 Subtitle Aligner Transformer

The core of our model is a Transformer [ [57](#bib.bib57) ] , as shown in

Fig.

[2](#S2.F2) , which we refer to as Subtitle Aligner Transformer (SAT).

In contrast to the common approach of feeding video

frames as input to the encoder [

[18](#bib.bib18) , [12](#bib.bib12) ] , we input the video

frames to the decoder side in order for the model to learn the association between

the frame-level features and the output vector of the same duration.

We first describe the structure of the Transformer, and then the text and video feature extraction.

Additional implementation details are provided in Sec.

[A](#A1) of the appendix.

Encoder. The input to the encoder is a sequence of text embeddings corresponding to the subtitle we wish to align.

Positional encodings are not used on the encoder side of

the Transformer since the text embeddings (see below) already contain

positional information.

The encoder is a stack of Transformer layers, each containing a multi-head attention mechanism followed by a feedforward network and embedding dimensionalities of size d m  o  d  e  l subscript 𝑑 𝑚 𝑜 𝑑 𝑒 𝑙 d\_{model} .

Decoder. The decoder is a stack of Transformer layers that attend on the encoded sequence. 2 2 2 Note: There is no auto-regression. The input to the decoder consists of a sequence of video features encoding the visual signing

information from the video, as well as a binary vector representing a prior estimation of the location

of the signing-aligned subtitle (S

prior ).

Positional encodings are added to the decoder input in order for the model to exploit the temporal ordering of the signing.

The final layer of the model is a linear layer with a sigmoid activation which outputs T 𝑇 T predictions in the range [ 0 , 1 ] 0 1 [0,1] one for each video frame.

Values of this output vector, S

pred , that are above a threshold τ 𝜏 \tau correspond

to the predicted temporal location of the queried subtitle text.

Text features. Each subtitle is encoded using a BERT [ [19](#bib.bib19) ] model pretrained on a large text corpus with a masked language modelling task, to produce a sequence of

768-dimensional vectors, one for each token in the sentence.

To match the input dimension of the encoder Transformer, these embeddings are first linearly projected to d m  o  d  e  l subscript 𝑑 𝑚 𝑜 𝑑 𝑒 𝑙 d\_{model} .

Video features. The visual features are 1024-dimensional embeddings extracted from the I3D [ [13](#bib.bib13) ] sign

classification model made publicly available by the authors of [

[56](#bib.bib56) ] .

The features are pre-extracted over sign language video segments.

A visual feature sequence of length T 𝑇 T is used as input to the model.

Prior position encoding. Besides the video features, the input to the decoder also includes a subtitle timing estimate as a prior position and duration cue.

This prior estimate is encoded as a binary vector of length T 𝑇 T , where 1 indicates that the associated video frame is within the temporal boundaries of the subtitle, and 0 otherwise.

The video and prior inputs are fused via concatenation before being passed as input to the decoder.

Before the concatenation both inputs are linearly projected to the same dimension.

The fusion output is finally projected to d m  o  d  e  l subscript 𝑑 𝑚 𝑜 𝑑 𝑒 𝑙 d\_{model} in order to be input to the Transformer decoder.

Training objective. The model is trained with a binary cross entropy loss between the

predicted vector and the ground truth S

gt of the signing-aligned subtitle within the video segment:

|    | ℒ  =  −  1  T  ∑  t  =  1  T  S  g  t  t  log  ⁡  S  p  r  e  d  t  +  (  1  −  S  g  t  t  )  log  ⁡  (  1  −  S  p  r  e  d  t  )  .  ℒ  1  𝑇  superscript  subscript  𝑡  1  𝑇  superscript  subscript  𝑆  𝑔  𝑡  𝑡  superscript  subscript  𝑆  𝑝  𝑟  𝑒  𝑑  𝑡  1  subscript  superscript  𝑆  𝑡  𝑔  𝑡  1  superscript  subscript  𝑆  𝑝  𝑟  𝑒  𝑑  𝑡  \mathcal{L}=-\frac{1}{T}\sum\_{t=1}^{T}S\_{gt}^{t}\log S\_{pred}^{t}+(1-S^{t}\_{gt})\log(1-S\_{pred}^{t}).   |    |
|----|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----|

### 3.2 Word pretraining with individual sign locations

SAT is designed for alignment of subtitles to video signing streams.

However, the same architecture can be used without any alterations

to align smaller text units, e.g. single words.

Given that we have access to sparse sign annotations from mouthings [

[2](#bib.bib2) ] and dictionary

exemplars [

[42](#bib.bib42) ] , we can use these to initialise the model weights and

incorporate this

knowledge via a potentially easier single-sign spotting task. We obtain timings of the

sparse word-level

annotations and assume a fixed single-second width as the precise sign boundaries are

not available.

The model is then trained to spot the single sign

occurrence within a video window of size T 𝑇 T . In our experiments, we demonstrate the advantages of such a pretraining strategy.

### 3.3 Global alignment with DTW

Our model does not take into account global information from the length of the video (e.g. 1-hour),

rather it looks for signing associated to a given subtitle within a short temporal window T 𝑇 T (e.g. 20-seconds). Hence, there may be overlaps between predictions for different subtitles; we resolve these overlap conflicts using DTW [

[44](#bib.bib44) ] .

We find an order-preserving global alignment from all elements of a sequence of video frames to all elements of sequence of subtitles, maximising the sum of sigmoid outputs of our model in our cost function for each subtitle query.

As DTW aligns all frames in a video sequence to subtitles, we select all frames of the signing video which are likely to be associated with subtitle queries. Specifically, we select all frames associated to an output score over τ d  t  w subscript 𝜏 𝑑 𝑡 𝑤 \tau\_{dtw} . In the case where our model outputs only values below τ d  t  w subscript 𝜏 𝑑 𝑡 𝑤 \tau\_{dtw} for a particular subtitle, we instead select all frames within the prior location S prior .

We order the subtitles by the mid-point of their predicted temporal location.

This allows the predicted subtitles to follow a different order to the original subtitles, because the order of phrases in the sign language interpretation does not necessarily follow the order of phrases of the written English subtitles (see Sec.

[C](#A3) of the appendix for further details).

We construct a cost matrix of dimension (i) the number of frames by (ii) the number of subtitles, and with entries of 1 − p i  j 1 subscript 𝑝 𝑖 𝑗 1-p\_{ij} , where p i  j subscript 𝑝 𝑖 𝑗 p\_{ij} is the sigmoid output corresponding to frame i 𝑖 i with subtitle j 𝑗 j as the encoder input. We apply the

DTW algorithm to this cost matrix of aligning video frames to subtitles. This maximises the overall sum of the

sigmoid outputs of the model under the ordering and allocation constraints of DTW.

If not otherwise mentioned, our full SAT model uses DTW postprocessing.

## 4 Experiments

In this section, we first give implementation details (Sec. [4.1](#S4.SS1) ) and describe the datasets and evaluation metrics

used in this work (Sec.

[4.2](#S4.SS2) ).

We then compare the results of the proposed SAT model against strong

baselines (Sec.

[4.3](#S4.SS3) )

and present a series of ablation studies (Sec.

[4.4](#S4.SS4) ).

Next, we demonstrate the performance of our model

on an additional dataset (Sec.

[4.5](#S4.SS5) ).

Finally, we provide qualitative results and discuss limitations (Sec.

[4.6](#S4.SS6) ).

### 4.1 Implementation details

Architecture. For both the encoder and the decoder we use 2 identical Transformer layers with 2 heads and size d m  o  d  e  l = 512 subscript 𝑑 𝑚 𝑜 𝑑 𝑒 𝑙 512 d\_{model}=512 each.

Backbone pretraining. The I3D model is pretrained to perform 1064-way classification across the sign spotting

instances with mouthings [

[2](#bib.bib2) ] and dictionary exemplars [ [42](#bib.bib42) ] (further details

can be found in [

[56](#bib.bib56) ] ).

The model is then frozen and used to densely pre-extract visual features with stride 1 over the clips of the datasets.

Prior input selection. As the prior estimate input S prior we use the temporal location of the audio-aligned subtitle S audio shifted by +3.2 seconds. This value, which we denote with S + a  u  d  i  o superscript subscript absent 𝑎 𝑢 𝑑 𝑖 𝑜 + {}\_{audio}^{\text{+}} , corresponds to the average temporal shift between the audio-aligned subtitles S audio and the ground truth

subtitles S

gt in our training data (see Fig. [3a](#S4.F3.sf1) ).

Search windows. During training, we randomly select a search window of 20 seconds around the location of the ground truth subtitle S gt , select the densely extracted video features for this window, and temporally subsample them by a factor of 4.

All videos are sampled at 25 25 25 FPS, therefore this results in T = 125 𝑇 125 T=125 frames.

During testing, we select a search window of the same length centered around the shifted subtitle location S + a  u  d  i  o superscript subscript absent 𝑎 𝑢 𝑑 𝑖 𝑜 + {}\_{audio}^{\text{+}} .

Text augmentation. During training, we augment the text query inputs randomly to reduce overfitting: For 50% of the samples, we shuffle the word order and add or delete up to two words.

Hyper-parameters. We set thresholds τ 𝜏 \tau to 0.5 0.5 0.5 , τ d  t  w subscript 𝜏 𝑑 𝑡 𝑤 \tau\_{dtw} to 0.4 0.4 0.4 .

Further details are provided in appendix Sec.

[A](#A1) .

### 4.2 Data and evaluation metrics

(a)

<!-- image -->

BSL-1K aligned is a subset of BSL-1K [ [2](#bib.bib2) ] which we manually annotated for subtitle alignment.

The subset contains 24 episodes covering a number of different television programmes (cooking,

nature, travel and reality shows), corresponding to 17.7 hours of BSL content of 3 different signers with 16K subtitles. The subtitles were originally aligned to the audio, but

we have manually aligned them

to the signing.

The unaligned subtitles (i.e. those that are synchronised with the audio track, rather than the signing) differ from the signing-aligned subtitles in both start time and duration. In particular, Fig.

[3](#S4.F3) , shows that there is no fixed shift or temporal scaling that can be applied to transform audio-synchronised subtitles to their signing-aligned counterparts. We note that the differences exhibit an approximately Gaussian distribution, with the exception of an accentuated peak at 0 in Fig. [3b](#S4.F3.sf2) -if the duration of the subtitle is approximately correct, annotators tend not to further refine the boundaries.

The subtitles cover a total of 147K word instances for

a vocabulary size of 9.4K in spoken English. We divide the data into 20 training episodes and 4 test episodes. The test episodes are chosen to evaluate the alignment model in different settings: seen/unseen signer and seen/unseen programme genre (which affects the number of out-of-vocabulary words) as

shown in Tab.

[1](#S4.T1) . The manual alignment of subtitles to signing content for the 24 episodes was performed over

approximately 200 hours by

native BSL annotators

using the open-source VIA tool [

[20](#bib.bib20) ] .

BSL Corpus [ [51](#bib.bib51) , [50](#bib.bib50) ] is a public dataset of videos of deaf signers gathered from several regions across the UK and accompanied by a variety of linguistic annotations. For our task, we employ the FreeTranslation annotation tier, which provides written English subtitles to accompany portions of the Conversation and Interview subsets of the corpus. In total, the annotations cover a total of 227 videos after cropping to include a single signer. Of these, 141 are sourced from the Interview subset and 86 videos are sourced from the Conversation subset. For consistency with prior work, we follow the train, validation and test partition employed by [ [47](#bib.bib47) , [2](#bib.bib2) ] .

However, since this partition does not fully span the dataset, we add any dataset instances that were not present in the partition to the training set. Dataset statistics on the resulting train, validation and test partition, including the total number of hours, subtitles and vocabulary spanned by the data, are given in Tab.

[2](#S4.T2) . Unlike BSL-1K, the subtitles in this dataset are aligned to signing, and the translation direction is from sign language to English.

We therefore simulate unaligned data by perturbing the subtitle locations in our experiments.

Evaluation metrics. We consider two main evaluation metrics: (i) frame-level accuracy, and (ii) F  1 𝐹 1 F1 -score.

For the F  1 𝐹 1 F1 -score, hits and misses of subtitle alignment to sign language video are counted under three temporal overlap thresholds

(IoU ∈ { 0.1 , 0.25 , 0.50 } absent 0.1 0.25 0.50 \in~{}\{0.1,0.25,0.50\} ) between predicted S

pred and manually aligned S gt subtitles, denoted as F1@.10, F1@.25, F1@.50, respectively.

### 4.3 Comparison to baselines

Simple temporal shift baseline ( S + a  u  d  i  o superscript subscript absent 𝑎 𝑢 𝑑 𝑖 𝑜 + {}\_{audio}^{\text{+}} ). As a first baseline we use the shifted audio-aligned subtitles S + a  u  d  i  o superscript subscript absent 𝑎 𝑢 𝑑 𝑖 𝑜 + {}\_{audio}^{\text{+}} .

Prosodic cues baseline (Bull et al. [ [8](#bib.bib8) ] ). We compare to the state of the art on subtitle-unit segmentation, which is a model based on 2D body keypoints. In contrast to our framework, this method only uses visual prosodic cues and does not use semantic information from the query subtitle. It has been trained on a large-scale

sign language corpus with aligned subtitles, and the pretrained model is public.

The model consists of ST-GCN [

[60](#bib.bib60) ] and BiLSTM layers and segments sign language video into subtitle units.

However, this is a different task than alignment, i.e. segments have no correspondence to subtitles.

To obtain an association from each predicted segment to a subtitle, we align

the shifted subtitles S + a  u  d  i  o superscript subscript absent 𝑎 𝑢 𝑑 𝑖 𝑜 + {}\_{audio}^{\text{+}} to a subtitle-unit segmentation of [

[8](#bib.bib8) ] using DTW, where the cost of alignment is the temporal distance.

Heuristic baseline based on sparse sign spottings. Inspired by previous works that approached the alignment task through sparse

correspondences [

[23](#bib.bib23) ] , we implement a heuristic approach to align the subtitles using a

combination of sign spotting and active signer detection. Sign spotting, performed by [

[2](#bib.bib2) , [42](#bib.bib42) ] ,

searches in the temporal

vicinity of each audio-synchronised subtitle (the search window is constructed by padding the original subtitle by

four seconds

at each end) for individual sign instances corresponding to words that appear in the

subtitle.

From these sparse sign localisations, we perform subtitle alignment in four stages.

First, we segment the episode into

sequences that contain active signing, following [

[1](#bib.bib1) ] .

Second, for any subtitle containing words that were spotted in the signing (assigned a posterior probability of 0.8 or

greater by the model of [

[42](#bib.bib42) ] ), we shift the subtitle such that its centre falls on the mean position of the

spotted signs. Third, we transform all subtitles without spottings by affine transformations such that they fall within

the "gaps" between those subtitles that contained spotted signs, while preserving ordering (we use one such

transformation per gap). Finally, we expand the duration of subtitles locally (applying a single scaling factor to each

subtitle) in left to right ordering, such that they maximally fill the active signing segments predicted by the first stage.

A comparison of our model to the above baselines is given in Tab. [3](#S4.T3) . The simple temporal shift baseline and

the heuristic baseline based on sparse sign spottings perform similarly, but are a significant improvement over the non-shifted

subtitles S

audio . Using prosodic cues through the model of [ [8](#bib.bib8) ] results in a slight improvement over these two

baselines. Our model significantly outperforms all baselines by exploiting the subtitle text to find the associated video

segment. Indeed, when providing random subtitle text during training, our model fails to outperform baseline F1 scores.

Using DTW to resolve overlaps in predicted subtitles boosts our model performance.

A breakdown of our results by test episode is provided in Tab. [4](#S4.T4) . Our model tends to result in

larger improvements over the S + a  u  d  i  o superscript subscript absent 𝑎 𝑢 𝑑 𝑖 𝑜 + {}\_{audio}^{\text{+}} baseline for signers seen in the training episodes, but still outperforms

the S + a  u  d  i  o superscript subscript absent 𝑎 𝑢 𝑑 𝑖 𝑜 + {}\_{audio}^{\text{+}} baseline for unseen signers in unseen genres. More training data would be needed to better

generalise to unseen signers.

### 4.4 Ablation study

We ablate the effects of inputting the prior estimate S = p  r  i  o  r S a  u  d  i  o + {}\_{prior}=S\_{audio}^{\text{+}} to the model,

the size of the search window, modifying the text input to the encoder, pretraining on sign localisation and alternative model formulations. Some additional ablations are presented in Sec.

[C](#A3) of the appendix.

Knowledge of S prior . We experiment with several versions of

inputs as additional information to the alignment task.

Tab.

[5](#S4.T5) summarises the results.

We first observe a significant drop in performance

when S

prior is not provided (48.15 vs 30.66 F1@.50),

suggesting that the position and duration of the corresponding

audio content allows an approximate localisation cue,

enabling the model to refine this via a series of attention layers.

Inputting the 3.2 seconds shifted subtitle timings (S = p  r  i  o  r S a  u  d  i  o + {}\_{prior}=S\_{audio}^{\text{+}} ) performs better than inputting the audio-aligned subtitle timings (S = p  r  i  o  r S a  u  d  i  o {}\_{prior}=S\_{audio} ).

Moreover, we carry out two additional experiments

to investigate whether this cue provides a position

prior or a duration prior. First,

we always input the subtitle timing centred

with respect to the search window. The poor

performance of this model suggests the

importance of the position. Second,

we preserve the shifted location, but randomly

change the input subtitle duration at training time by up to 2s.

This slightly reduces the performance, therefore duration cues seem less essential for the model than location cues.

Size of the search window T 𝑇 T . In Tab. [6](#S4.T6) ,

we report the performance against different choices for input duration T 𝑇 T We conclude that larger search windows generally

improve performance, at the cost of computational complexity.

This might be due to increased supervision, since with larger windows the training

sees more negative examples, as well as due to better

coverage at test time. A too short window size inhibits recovery of the correct location, if the correct location falls outside of the window boundaries.

In all our experiments, we use 20-second windows.

Effect of text input to the encoder. We perform a series of ablations regarding the text encoding, including: no text augmentations, adding extra positional encodings to the BERT text features (as described in appendix Sec. [A](#A1) ), and using the sentence embedding only (the output embedding corresponding to the BERT "CLS" token) instead of the sequence of individual token embeddings. Tab. [7](#S4.T7) presents the results on BSL-1K aligned with these text ablations. Augmenting the subtitle text improves performance, while adding extra positional encodings or using the sentence embedding degrades performance.

Effect of sign localisation pretraining. As explained in Sec. [3.2](#S3.SS2) ,

we initially pretrain our model for temporal localisation of individual signs.

In Tab.

[8](#S4.T8) , we measure

the effect of this pretraining on a large set of word-video training pairs,

and conclude that it provides a good initialisation

for finetuning on long subtitles.

Model formulation. We consider an alternative version of the Transformer model, inspired by the DETR model in [ [12](#bib.bib12) ] for object detection in images.

This model inputs image features into the Transformer encoder and text query into the Transformer decoder.

Similarly, we input the sign language video features into the Transformer encoder. On the decoder side, we input the subtitle

text features as well as either (i) the start and end times or (ii) the shift and scale of the shifted subtitles

S + a  u  d  i  o superscript subscript absent 𝑎 𝑢 𝑑 𝑖 𝑜 + {}\_{audio}^{\text{+}} relative to the temporal window. We then consider the problem of subtitle alignment as a regression

problem, and aim to predict (i) the start and end times or (ii) the shift and scale of the subtitle relative to the temporal window.

As a further ablation, we also consider the same model architecture (with subtitle features and the start and end times as decoder input), but outputting a fixed binary vector of length T 𝑇 T , which we train with a binary classification objective (as in SAT).

The results in Tab. [9](#S4.T9) suggest

that our proposed approach with video features as input to the Transformer decoder enables significantly better learning,

perhaps by providing a one-to-one mapping between video

inputs and the frame-wise outputs.

Another possible explanation for our proposed model's superiority is that it outputs alignment scores between subtitles and individual frames which allows for better conflict resolution strategies for overlapping subtitle predictions.

### 4.5 Performance on a different dataset

Figure 4: Qualitative results: This figure shows short time windows of 5s (left) or 7s (right) with shifted audio-aligned subtitles (S + a  u  d  i  o superscript subscript absent 𝑎 𝑢 𝑑 𝑖 𝑜 + {}\_{audio}^{\text{+}} ), ground truth signing-aligned subtitles (S gt ) and our predicted signing-aligned subtitles (S pred ). In practice, we input 20 seconds of video during training and testing as our search window.

<!-- image -->

We demonstrate our model's performance on the BSL Corpus [ [51](#bib.bib51) , [50](#bib.bib50) ] .

The subtitles in this dataset are aligned to the sign language, and so we randomly shift and scale the subtitles in order to create artificial training data. We then train our SAT model to learn the correct alignment of subtitles to video in the BSL Corpus. We train the model (i) without any pretraining, (ii) with only word pretraining (on BSL-1K) and (iii) with SAT pretraining on BSL-1K

aligned . We report results in Tab. [10](#S4.T10) .

At each subtitle, we apply a random shift following a normal distribution with standard deviation σ pos subscript 𝜎 pos \sigma\_{\text{pos}} and a random change of duration of the subtitle also following a normal distribution with standard deviation σ dur subscript 𝜎 dur \sigma\_{\text{dur}} . Tab. [10](#S4.T10) shows that our model is able to partially recover the correct original alignment. Larger shifts make it more difficult for our model to recover the correct original alignment, but random changes in subtitle duration seems to have less effect. This is consistent with the results in Tab. [5](#S4.T5) , where changing the duration of S + a  u  d  i  o superscript subscript absent 𝑎 𝑢 𝑑 𝑖 𝑜 + {}\_{audio}^{\text{+}} does not greatly impact results. Word pretraining on BSL-1K helps the model, but SAT pretraining on BSL-1K aligned does not. Word pretraining may help the SAT model recognise certain signs in BSL, but domain difference between BSL Corpus and BSL-1K aligned subtitles may explain why SAT pretraining on BSL-1K aligned does not lead to any significant gains on BSL Corpus.

### 4.6 Qualitative analysis

Fig. [4](#S4.F4) illustrates

several test examples on BSL-1K

aligned . The timeline shows the ground truth

alignment (S

gt ), our prediction (S pred ), as well as the S + a  u  d  i  o superscript subscript absent 𝑎 𝑢 𝑑 𝑖 𝑜 + {}\_{audio}^{\text{+}} baseline, alongside a sample of video frames and the query subtitle text. While the shifted baseline

S + a  u  d  i  o superscript subscript absent 𝑎 𝑢 𝑑 𝑖 𝑜 + {}\_{audio}^{\text{+}} provides an approximate position,

it is largely unaligned. Our model effectively

learns to attend to both visual and textual cues.

A typical failure mode happens when the prior position encoding

is significantly far from the ground truth (see Fig.

[4](#S4.F4) bottom right). For additional qualitative examples on BSL Corpus, we refer to Fig. [A.3](#A2.F3) of the appendix.

## 5 Conclusion

We presented a Transformer-based

approach to synchronise subtitles

with sign language video content

in interpreted data.

We showed that knowledge

of subtitle content is essential

to effectively align subtitles to signing.

We hope that our work will be

a stepping stone to obtain video-subtitle

pairs that allow training of unconstrained

machine translation systems for sign languages.

Furthermore, our approach is potentially

applicable to other domains, such as temporal grounding of

sentences. We refer to Sec.

[D](#A4) of the appendix

for a discussion

on the broader impact on the community.

Acknowledgements. This work was supported by EPSRC grant ExTol and a Royal Society Research Professorship.

We thank Tom Monnier, Himel Chowdhury, Abhishek Dutta, Ashish Thandavan,

Annelies Braffort, Michèle Gouiffès and Igor Garbuz for their help.

## References

- [1] Samuel Albanie, Gül Varol, Liliane Momeni, Triantafyllos Afouras, Andrew Brown, Chuhan Zhang, Ernesto Coto, Necati Cihan Camgöz, Ben Saunders, Abhishek Dutta, Neil Fox, Richard Bowden, Bencie Woll, and Andrew Zisserman. Signer diarisation in the wild. Technical Report , 2021.
- [2] Samuel Albanie, Gül Varol, Liliane Momeni, Triantafyllos Afouras, Joon Son Chung, Neil Fox, and Andrew Zisserman. BSL-1K: Scaling up co-articulated sign language recognition using mouthing cues. In Proc. ECCV , 2020.
- [3] P. Bojanowski, Rémi Lajugie, E. Grave, Francis R. Bach, I. Laptev, J. Ponce, and C. Schmid. Weakly-supervised alignment of video with text. In ICCV , 2015.
- [4] M. Borg and K. P. Camilleri. Sign language detection "in the wild" with recurrent neural networks. ICASSP , 2019.
- [5] Danielle Bragg, Oscar Koller, et al. Sign language recognition, generation, and translation: An interdisciplinary perspective. In ACM SIGACCESS , 2019.
- [6] Patrick Buehler, Mark Everingham, and Andrew Zisserman. Learning sign language by watching TV (using weakly aligned subtitles). In Proc. CVPR , 2009.
- [7] Patrick Buehler, Mark Everingham, and Andrew Zisserman. Employing signed TV broadcasts for automated learning of British sign language. In Workshop on the Representation and Processing of Sign Languages , 2010.
- [8] Hannah Bull, Michèle Gouiffès, and Annelies Braffort. Automatic segmentation of sign language into subtitle-units. In ECCVW, Sign Language Recognition, Translation and Production (SLRTP) , 2020.
- [9] Necati Cihan Camgoz, Simon Hadfield, Oscar Koller, and Richard Bowden. SubUNets: End-to-end hand shape and continuous sign language recognition. In ICCV , 2017.
- [10] Necati Cihan Camgoz, Simon Hadfield, Oscar Koller, Hermann Ney, and Richard Bowden. Neural sign language translation. In CVPR , 2018.
- [11] Necati Cihan Camgoz, Oscar Koller, Simon Hadfield, and Richard Bowden. Sign language transformers: Joint end-to-end sign language recognition and translation. In CVPR , 2020.
- [12] Nicolas Carion, Francisco Massa, Gabriel Synnaeve, Nicolas Usunier, Alexander Kirillov, and Sergey Zagoruyko. End-to-end object detection with transformers. In ECCV , 2020.
- [13] J. Carreira and A. Zisserman. Quo vadis, action recognition? A new model and the kinetics dataset. In CVPR , 2017.
- [14] Jingyuan Chen, Xinpeng Chen, L. Ma, Zequn Jie, and Tat-Seng Chua. Temporally grounding natural sentence in video. In EMNLP , 2018.
- [15] Ka Leong Cheng, Zhaoyang Yang, Qifeng Chen, and Yu-Wing Tai. Fully convolutional networks for continuous sign language recognition. In ECCV , 2020.
- [16] N. Cherniavsky, R. E. Ladner, and E. A. Riskin. Activity detection in conversational sign language video for mobile telecommunication. In IEEE International Conference on Automatic Face Gesture Recognition , 2008.
- [17] Helen Cooper and Richard Bowden. Learning signs from subtitles: A weakly supervised approach to sign language recognition. In CVPR , 2009.
- [18] Karan Desai and Justin Johnson. VirTex: Learning visual representations from textual annotations. arXiv:2006.06666 , 2021.
- [19] Jacob Devlin, Ming-Wei Chang, Kenton Lee, and Kristina Toutanova. BERT: Pre-training of deep bidirectional transformers for language understanding. arXiv:1810.04805 , 2019.
- [20] Abhishek Dutta and Andrew Zisserman. The via annotation software for images, audio and video. In Proc. ACMM , volume 27 of MM 19 , New York, USA, Oct 2019. ACM, ACM. to appear in Proceedings of the 27th ACM International Conference on Multimedia (MM 19).
- [21] M. Everingham, Josef Sivic, and Andrew Zisserman. Hello! my name is... buffy" - automatic naming of characters in tv video. In BMVC , 2006.
- [22] Iva Farag and Heike Brock. Learning motion disfluencies for automatic sign language segmentation. In ICASSP , 2019.
- [23] Ali Farhadi and David Forsyth. Aligning ASL for statistical translation using a discriminative word model. In CVPR , 2006.
- [24] J. Fenlon. Seeing sentence boundaries: the production and perception of visual markers signalling boundaries in signed languages . PhD thesis, UCL, 2010.
- [25] Jiyang Gao, Chen Sun, Zhenheng Yang, and Ram Nevatia. Tall: Temporal activity localization via language query. In ICCV , 2017.
- [26] Binyam Gebrekidan Gebre, Peter Wittenburg, Tom Heskes, and Sebastian Drude. Motion history images for online speaker/signer diarization. In ICASSP , 2014.
- [27] Binyam Gebrekidan Gebre, Peter Wittenburg, and Tom Heskes. Automatic signer diarization-the mover is the signer approach. In CVPRW , 2013.
- [28] S. Ghosh, A. Agarwal, Zarana Parekh, and A. Hauptmann. Excl: Extractive clip localization using natural language descriptions. In NAACL-HLT , 2019.
- [29] D. He, Xiang Zhao, Jizhou Huang, F. Li, Xiao Liu, and Shilei Wen. Read, watch, and move: Reinforcement learning for temporally grounding natural language descriptions in videos. In AAAI , 2019.
- [30] Lisa Anne Hendricks, O. Wang, E. Shechtman, Josef Sivic, Trevor Darrell, and Bryan C. Russell. Localizing moments in video with natural language. In ICCV , 2017.
- [31] Jie Huang, Wengang Zhou, Qilin Zhang, Houqiang Li, and Weiping Li. Video-based sign language recognition without temporal segmentation. In AAAI , 2018.
- [32] Marion Kaczmarek and Michael Filhol. Use cases for a sign language concordancer. In Proceedings of the LREC2020 9th Workshop on the Representation and Processing of Sign Languages , pages 113-116, 2020.
- [33] Oscar Koller. Quantitative survey of the state of the art in sign language recognition. arXiv:2008.09918 , 2020.
- [34] Oscar Koller, O Zargaran, Hermann Ney, and Richard Bowden. Deep sign: Hybrid CNN-HMM for continuous sign language recognition. In BMVC , 2016.
- [35] Oscar Koller, Sepehr Zargaran, and Hermann Ney. Re-sign: Re-aligned end-to-end sequence modelling with deep recurrent CNN-HMMs. In CVPR , 2017.
- [36] Dongxu Li, Chenchen Xu, Xin Yu, K. Zhang, Ben Swift, Hanna Suominen, and H. Li. TSPNet: Hierarchical feature learning via temporal semantic pyramid for sign language translation. NeurIPS , 2020.
- [37] Dongxu Li, Xin Yu, Chenchen Xu, Lars Petersson, and Hongdong Li. Transferring cross-domain knowledge for video sign language recognition. In CVPR , 2020.
- [38] Rung-Huei Liang and Ming Ouhyoung. A real-time continuous gesture recognition system for sign language. In Proceedings third IEEE international conference on automatic face and gesture recognition , 1998.
- [39] M. Liu, Xiang Wang, L. Nie, X. He, B. Chen, and Tat-Seng Chua. Attentive moment retrieval in videos. In The 41st International ACM SIGIR Conference on Research &amp; Development in Information Retrieval , 2018.
- [40] Antoine Miech, Jean-Baptiste Alayrac, Lucas Smaira, Ivan Laptev, Josef Sivic, and Andrew Zisserman. End-to-end learning of visual representations from uncurated instructional videos. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition , pages 9879-9889, 2020.
- [41] Tomas Mikolov, Ilya Sutskever, Kai Chen, Greg Corrado, and Jeffrey Dean. Distributed representations of words and phrases and their compositionality. arXiv:1310.4546 , 2013.
- [42] Liliane Momeni, Gül Varol, Samuel Albanie, Triantafyllos Afouras, and Andrew Zisserman. Watch, read and lookup: Learning to spot signs from multiple supervisors. In Proc. ACCV , 2020.
- [43] Amit Moryossef, Ioannis Tsochantaridis, Roee Aharoni, Sarah Ebling, and Srini Narayanan. Real-Time Sign Language Detection using Human Pose Estimation. In ECCVW, Sign Language Recognition, Translation and Production (SLRTP) , 2020.
- [44] C. Myers and L. Rabiner. A comparative study of several dynamic time-warping algorithms for connected-word recognition. The Bell System Technical Journal , 60:1389-1409, 1981.
- [45] Eng-Jon Ong, Oscar Koller, Nicolas Pugeault, and Richard Bowden. Sign spotting using hierarchical sequential patterns with temporal intervals. In CVPR , 2014.
- [46] Tomas Pfister, James Charles, and Andrew Zisserman. Large-scale learning of sign language by watching TV (using co-occurrences). In Proc. BMVC , 2013.
- [47] Katrin Renz, Nicolaj Stache, Samuel Albanie, and Gül Varol. Sign segmentation with temporal convolutional networks. In International Conference on Acoustics, Speech, and Signal Processing , 2021.
- [48] K. P. Sankar, C. Jawahar, and Andrew Zisserman. Subtitle-free movie to script alignment. In BMVC , 2009.
- [49] P. Santemiz, Oya Aran, M. Saraçlar, and L. Akarun. Automatic sign segmentation from continuous signing via multiple sequence alignment. ICCVW , 2009.
- [50] Adam Schembri, Jordan Fenlon, Ramas Rentelis, and Kearsy Cormier. British Sign Language Corpus Project: A corpus of digital video data and annotations of British Sign Language 2008-2017 (Third Edition), 2017.
- [51] Adam Schembri, Jordan Fenlon, Ramas Rentelis, Sally Reynolds, and Kearsy Cormier. Building the British Sign Language Corpus. Language Documentation &amp; Conservation , 7:136-154, 2013.
- [52] F. Shipman, Satyakiran Duggina, Caio D. D. Monteiro, and R. Gutierrez-Osuna. Speed-accuracy tradeoffs for detecting sign language content in video sharing sites. Proceedings of the 19th International ACM SIGACCESS Conference on Computers and Accessibility , 2017.
- [53] Rachel Sutton-Spence and Bencie Woll. The Linguistics of British Sign Language: An Introduction . Cambridge University Press, 1999.
- [54] Makarand Tapaswi, M. Bäuml, and R. Stiefelhagen. Story-based video retrieval in tv series using plot synopses. In Proceedings of International Conference on Multimedia Retrieval , 2014.
- [55] Makarand Tapaswi, M. Bäuml, and R. Stiefelhagen. Book2Movie: Aligning video scenes with book chapters. In CVPR , 2015.
- [56] Gül Varol, Liliane Momeni, Samuel Albanie, Triantafyllos Afouras, and Andrew Zisserman. Read and attend: Temporal localisation in sign language videos. In CVPR , 2021.
- [57] Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N Gomez, Łukasz Kaiser, and Illia Polosukhin. Attention is all you need. In NeurIPS , 2017.
- [58] Weining Wang, Yan Huang, and Liang Wang. Language-driven temporal activity localization: A semantic matching reinforcement learning model. In CVPR , 2019.
- [59] Huijuan Xu, Kun He, Bryan A. Plummer, L. Sigal, S. Sclaroff, and Kate Saenko. Multilevel language and vision integration for text-to-clip retrieval. In AAAI , 2019.
- [60] Sijie Yan, Yuanjun Xiong, and Dahua Lin. Spatial temporal graph convolutional networks for skeleton-based action recognition. In AAAI , 2018.
- [61] Hee-Deok Yang, Stan Sclaroff, and Seong-Whan Lee. Sign language spotting with a threshold model based on conditional random fields. IEEE Transactions on Pattern Analysis and Machine Intelligence , 2008.
- [62] Ruiduo Yang and Sudeep Sarkar. Detecting coarticulation in sign language using conditional random fields. In ICPR , 2006.
- [63] Yitian Yuan, T. Mei, and Wenwu Zhu. To find where you talk: Temporal sentence localization in video with attention based location regression. In AAAI , 2019.
- [64] Runhao Zeng, H. Xu, W. Huang, Peihao Chen, Mingkui Tan, and Chuang Gan. Dense regression network for video grounding. In CVPR , 2020.

## Appendix

We provide

further implementation details (Sec.

[A](#A1) ),

additional qualitative results (Sec.

[B](#A2) ),

additional experiments (Sec.

[C](#A3) ),

and a broader impact statement (Sec.

[D](#A4) ).

## Appendix A Implementation details

Text embeddings. For the text embeddings, we use a pretrained BERT model from HuggingFace 3 3 3 [https://huggingface.co/bert-base-uncased](https://huggingface.co/bert-base-uncased) with a standard architecture of 12-layers, 12-heads and 768 model size. The model is pretrained on BookCorpus 4 4 4 [https://yknzhu.wixsite.com/mbweb](https://yknzhu.wixsite.com/mbweb) and English Wikipedia 5 5 5 [https://en.wikipedia.org](https://en.wikipedia.org/) .

Positional encodings. For the input to the video encoder, we use 512 512 512 -dimensional sinusoidal positional encodings as in [ [57](#bib.bib57) ] . The positional encodings are added to the video features before feeding to the Transformer.

Output thresholding. The output of our model is a temporal sequence of predictions between 0 and 1. For the single-subtitle SAT model, we

consider the start of the subtitle to be the first time when the prediction is above τ = 0.5 𝜏 0.5 \tau=0.5 and the end of the subtitle to be the last time when the prediction is above τ = 0.5 𝜏 0.5 \tau=0.5 in the search window. When we apply a global alignment step with DTW to

correct for overlapping subtitles, we no longer use these thresholds, but rather the temporal sequence of predictions between

0 and 1 using the method described in the main paper.

Training details. We use the Adam optimiser with a batch size of 64.

We train with a learning rate of 10 − 5 superscript 10 5 10^{-5} at the word-pretraining stage,

and of 5 × 10 − 6 5 superscript 10 6 5\times 10^{-6} at finetuning with subtitles.

At the word pretraining stage, the model is trained over 5 epochs.

In one epoch of word pretraining, there are approximately 700K sign instances (including sign spotting both with mouthings and dictionaries).

At this point the word alignment model obtains a frame-level accuracy of 30.38% and F1@50 of 40.75% on the 1630 sign instances of the test set episodes.

During full-sentence finetuning, the model is trained over 80 epochs.

Figure A.1: DTW: Our SAT model predicts the locations of subtitles independently of each other, and thus there can be overlaps in subtitle localisations. Using a global alignment step with DTW, we resolve these overlaps and improve performance.

<!-- image -->

## Appendix B Additional qualitative analysis

Effect of global alignment with DTW. In Fig. [A.1](#A1.F1) , we present results before and after

the global alignment with DTW on a long timeline. We observe

that the single-subtitle Transformer model produces

overlapping regions between consecutive subtitles

which are resolved after the global DTW stage.

Consequently, we see that the overall duration of subtitles decreases

after DTW (see Fig.

[A.2](#A2.F2) ). During the DTW stage, we order subtitles by their predicted order, not by the original order of S audio . Indeed, in BSL-1K aligned , 1.6% of subtitles in S gt do not respect the original order of S audio . On the test set, 1.6% of subtitles in S pred switch position with respect to S audio .

Figure A.2: Duration before and after DTW : The median duration of S gt is 3.3s. Before DTW, the median duration of our predicted subtitles is 4.1s, but after DTW the median duration is reduced back down to 3.5s by resolving conflicts in overlapping subtitles.

<!-- image -->

Results on BSL Corpus. Fig. [A.3](#A2.F3) demonstrates

qualitative results on BSL Corpus.

Figure A.3: Qualitative results on BSL Corpus: This figure shows short time windows of 5s and 7s with shifted and rescaled subtitles (S prior ), ground truth aligned subtitles (S gt ) and our predicted subtitles (S pred ). In practice, we input 20 seconds of video during training and testing for our search window. The shifted and rescaled subtitles (S prior ) are created using a random shift with standard deviation of 3.5s and a random change in length of standard deviation 1.5s.

<!-- image -->

## Appendix C Additional experiments

We perform ablations to evaluate the influence

of our data augmentations and the encoding

choice for the subtitle text.

Text encoding choice. We experiment with word2vec [ [41](#bib.bib41) ] encodings

for subtitle words instead of BERT as used

in the main paper experiments. We use the pretrained word2vec model from [

[40](#bib.bib40) ] , forming sentence embeddings by max pooling the encodings of all words over the channel dimension.

In Tab.

[A.1](#A3.T1) , we see that this results in lower performance compared to using the BERT encodings. We

hypothesize that this is due to word2vec using a limited vocabulary, ignoring word order, and lacking the large-scale

pretraining of the BERT model.

Amount of training data. By increasing the amount of training data, we improve performance of our model on the test set. Tab. [A.2](#A3.T2) shows our results when training on random subsets of 25%, 50% and 75% of the videos in our training data. For subset selection, we randomly sample 4 times, and report the average performance across 4 trainings, as well as the standard deviation.

Sensitivity analysis. During inference, we predict the location of a subtitle within a 20 second search window surrounding the location of S + a  u  d  i  o superscript subscript absent 𝑎 𝑢 𝑑 𝑖 𝑜 + {}\_{audio}^{\text{+}} . In order to analyse the sensitivity of the choice of search window, we shift the window by 1s, 3s and 5s at inference time. Tab. [A.3](#A3.T3) shows that the choice of window within a margin of a few seconds does not have a large impact on the results.

However, if we keep the position of the search window constant and change the position of the prior estimate S + a  u  d  i  o superscript subscript absent 𝑎 𝑢 𝑑 𝑖 𝑜 + {}\_{audio}^{\text{+}} , then this has a significant effect on results.

Tab.

[A.4](#A3.T4) shows the results of an experiment where we shift the prior estimate S + a  u  d  i  o superscript subscript absent 𝑎 𝑢 𝑑 𝑖 𝑜 + {}\_{audio}^{\text{+}} by 1s, 3s and 5s at inference time.

The performance degrades when the model is given a worse prior as input, i.e., shifting S + a  u  d  i  o superscript subscript absent 𝑎 𝑢 𝑑 𝑖 𝑜 + {}\_{audio}^{\text{+}} .

## Appendix D Broader impact

The World Federation of the Deaf states that there are 70 million Deaf individuals world-wide using more than 200 sign languages. 6 6 6 [http://wfdeaf.org/our-work/](http://wfdeaf.org/our-work/) Unfortunately, many technologies for spoken and written languages do not exist for signed languages. We hope that our work contributes towards addressing this imbalance by providing inclusive technologies for signed languages for several applications, discussed next.

One direct application of our method is an assistive subtitling tool for signing vloggers to align their subtitles (this technology is currently only available for spoken and written languages). A second application is to create bilingual written-signed corpora aligned at a sentence or phrase-like level. Such corpora can be used in contextual or concordance dictionaries, useful for translation or for language learning [ [32](#bib.bib32) ] . Moreover, they can be used as training data for translation between signing and written text.

For context, note that machine translation-which can now be performed to an acceptable level in many written languages to enable cross-lingual access to content-remains far from human performance for sign languages [

[33](#bib.bib33) ] . To enable progress for this task (and others that have been highlighted as important by members of Deaf communities), a key stumbling block is the availability of larger annotated datasets [ [5](#bib.bib5) ] . Our work aims to take steps towards addressing this challenge, since automatic subtitle alignment represents an important pre-processing step that has been performed manually for existing translation datasets, e.g. [ [10](#bib.bib10) ] . However, scaling manual annotation to larger datasets is prohibitively expensive (as noted in the submission, aligning one hour of video takes approximately 10-15 hours of annotation time).

We note that there are also potential risks associated with our contributions. First, there is a chance with any computational advances in sign language modelling that it leads to increased surveillance of Deaf communities (and of content moderation more generally). Second, we note that our training data, obtained from public broadcast footage, may not be demographically representative of the population as a whole, and therefore is susceptible to bias. Additionally, the videos contain BSL interpreted from English, not original BSL content. Subtitle alignment may work less effectively for individuals who are not well-represented in the training data.

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
- fullText: ar5iv
- bibtex: ours

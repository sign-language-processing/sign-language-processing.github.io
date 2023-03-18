---
title: "Sign Language Processing"
link-citations: true
geometry: margin=3cm
css: style.css
linkcolor: Black
secnumdepth: 3
header-includes:
- |
  \usepackage{pdflscape}
author:
- Amit Moryossef ([amitmoryossef@gmail.com](mailto:amitmoryossef@gmail.com))
- Yoav Goldberg ([yoav.goldberg@biu.ac.il](mailto:yoav.goldberg@biu.ac.il))
abstract: |
    Sign Language Processing (SLP) is a field of artificial intelligence
    concerned with the automatic processing and analysis of sign language content.
    This project aims to organize the sign language processing literature, datasets, and tasks.
    This is a work in progress. The contents of this document will be refined throughout 2020-2023.
...


```{=html}
<p style="text-align: center;overflow:visible">
<iframe src="https://sign.mt/?embed=&spl=en&sil=us&text=Hello%20world!" allow="camera;microphone" title="sign.mt translation demo"></iframe>
Try <a href="https://sign.mt">sign translate</a> to experience state-of-the art-sign language translation technology.
</p>
```

## Introduction

Signed languages (also known as sign languages) are languages that use the visual-gestural modality to
convey meaning through manual articulations in combination with non-manual elements like the face and body.
They are the primary means of communication for many deaf and hard-of-hearing individuals.
Similar to spoken languages, signed languages are natural languages governed by a set of linguistic rules [@sandler2006sign], 
both emerging through an abstract, protracted aging process and evolving without meticulous planning.
Signed languages are not universal or mutually intelligible, despite often having striking similarities among them.
They are also distinct from spoken languages---i.e., American Sign Language (ASL) is not a visual form of English 
but its own unique language.

Sign Language Processing [@bragg2019sign;@yin-etal-2021-including] is an emerging field of artificial intelligence concerned with the automatic processing and analysis of sign language content.
While, to date, research has focused more on the visual aspects of signed languages, it is a subfield of both Natural Language Processing (NLP) and Computer Vision (CV).
Challenges in sign language processing frequently involve machine translation of sign language videos to spoken language text (sign language translation), 
from spoken language text (sign language production) or sign language recognition for sign language understanding.

Unfortunately, the latest advances in language-based artificial intelligence, like machine translation and personal assistants, 
expect a spoken language input (text or transcribed speech), excluding around 200-to-300 different signed languages [@un2022] and up to 70 million deaf people [@who2021;@wfd2022].

Throughout history, Deaf communities fought for the right to learn and use signed languages and for the public recognition of signed languages as legitimate ones.
Indeed, signed languages are sophisticated communication modalities that are at least as capable as spoken languages in all manners, linguistic and social.
However, in a predominantly oral society, deaf people are constantly encouraged to use spoken languages through lip-reading or text-based communication.
The exclusion of signed languages from modern language technologies further suppresses signing in favor of spoken languages.
This exclusion disregards the preferences of the Deaf communities who strongly prefer to communicate in signed languages both online and for in-person day-to-day interactions,
among themselves and when interacting with spoken language communities [@padden1988deaf;@glickman2018language].
Thus, it is essential to make signed languages accessible.

To date, a large amount of research on Sign Language Processing (SLP) has been focused on the visual aspect of signed languages, led by the Computer Vision (CV) community, with little NLP involvement.
This focus is not unreasonable, given that a decade ago, we lacked adequate CV tools to process videos for further linguistic analyses.
However, like spoken languages, signed languages are fully-fledged systems that exhibit all the fundamental characteristics of natural languages,
and current SLP techniques fail to address or leverage the linguistic structure of signed languages.
Signed languages introduce novel challenges for NLP due to their visual-gestural modality, simultaneity, spatial coherence, and lack of written form.
The lack of a written form makes the spoken language processing pipelines - which often start with audio transcription before processing -
incompatible with signed languages, forcing researchers to work directly on the raw video signal.

Moreover, SLP is not only an intellectually appealing area but also an important research area with a solid potential to benefit signing communities.
Examples of beneficial applications enabled by signed language technologies include better documentation of endangered sign languages;
educational tools for sign language learners; tools for query and retrieval of information from signed language videos; personal assistants that react to signed languages; real-time automatic sign language interpretations; and more.
Needless to say, in addressing this research area, researchers should work *alongside* and *under the direction of* deaf communities,
and to benefit the signing communities' interest above all [@harris2009research].

In this work, we describe the different representations used for sign language processing,
as well as survey the various tasks and recent advances on them.
We also make a comprehensive list of existing datasets and make the ones available easy to load using a simple and standardized interface.

### (Brief) History of Signed Languages and Deaf Culture

Throughout modern history,
spoken languages were dominant, so much so that signed languages struggled to be recognized as languages in their own right
and educators developed misconceptions that signed language acquisition might hinder the development of speech skills.
For example, in 1880, a large international conference of deaf educators called the "Second International Congress on Education of the Deaf"
banned teaching signed languages, favoring speech therapy instead.
It was not until the seminal work on American Sign Language (ASL) by @writing:stokoe1960sign that signed languages started gaining
recognition as natural, independent, and well-defined languages, which inspired other researchers to further explore signed languages as a research area.
Nevertheless, antiquated notions that deprioritized signed languages continue to do harm and subjects many to linguistic neglect [@humphries2016avoiding].
Several studies have shown that deaf children raised solely with spoken languages do not gain enough access to a first language during their critical period of language acquisition [@murray2020importance].
This language deprivation can lead to life-long consequences on the cognitive, linguistic, socio-emotional, and academic development of the deaf [@hall2017language].

Signed languages are the primary languages of communication for the Deaf[^deaf] and are at the heart of Deaf communities.
Failing to recognize signed languages as fully-fledged natural language systems in their own right has had harmful effects in the past,
and in an increasingly digitized world, NLP research should strive to enable a world in which all people,
including the Deaf, have access to languages that fit their lived experience.

[^deaf]: When capitalized, "Deaf" refers to a community of deaf people who share a language and a culture, whereas the lowercase "deaf" refers to the audiological condition of not hearing.

## Sign Language Linguistics Overview

Signed languages consist of phonological, morphological, syntactic, and semantic levels of structure that fulfill the same social, cognitive,
and communicative purposes as other natural languages.
While spoken languages primarily channel the oral-auditory modality, signed languages use the visual-gestural modality,
relying on the signer's face, hands, body, and space around them to create distinctions in meaning.
We present the linguistic features of signed languages[^asl-specific] that researchers must consider during their modeling.

[^asl-specific]: We mainly refer to ASL, where most sign language research has been conducted, but not exclusively.

###### Phonology {-}
Signs are composed of minimal units that combine manual features such as hand configuration,
palm orientation, placement, contact, path movement, local movement,
as well as non-manual features including eye aperture, head movement, and torso positioning [@liddell1989american;@johnson2011toward;@brentari2011sign;@sandler2012phonological].
Not all possible phonemes are realized in both signed and spoken languages, and inventories of two languages' phonemes/features may not overlap completely.
Different languages are also subject to rules for the allowed combinations of features.

###### Simultaneity {-}
Though an ASL sign takes about twice as long to produce than an English word,
the rates of transmission of information between the two languages are similar [@bellugi1972comparison].
One way signed languages compensate for the slower production rate of signs is through simultaneity:
Signed languages use multiple visual cues to convey different information simultaneously [@sandler2012phonological].
For example, the signer may produce the sign for 'cup' on one hand while simultaneously pointing to the actual cup with the other to express ``that cup''.
Similarly to tone in spoken languages, the face and torso can convey additional affective information [@liddell2003grammar;@johnston2007australian].
Facial expressions can modify adjectives, adverbs, and verbs; a head shake can negate a phrase or sentence; eye direction can help indicate referents.

###### Referencing {-}
The signer can introduce referents in discourse either by pointing to their actual locations in space or by assigning a region in the signing space to a non-present referent and by pointing to this region to refer to it [@rathmann2011featural;@schembri2018indicating].
Signers can also establish relations between referents grounded in signing space by using directional signs or embodying the referents using body shift or eye gaze [@dudis2004body;@liddell1998gesture].
Spatial referencing also impact morphology when the directionality of a verb depends on the location of the reference to its subject and/or object [@de2008pointing;@fenlon2018modification]:
For example, a directional verb can move from its subject's location and end at its object's location.
While the relation between referents and verbs in spoken language is more arbitrary, referent relations are usually grounded in signed languages.
The visual space is heavily exploited to make referencing clear.

Another way anaphoric entities are referenced in sign language is by using classifiers or depicting signs [@supalla1986classifier;@wilcox2004rethinking;@roy2011discourse] that help describe the characteristics of the referent.
Classifiers are typically one-handed signs that do not have a particular location or movement assigned to them,
or derive features from meaningful discourse [@liddell2003grammar], so they can be used to convey how the referent relates to other entities,
describe its movement, and give more details.
For example, to tell about a car swerving and crashing, one might use the hand classifier for a vehicle, move it to indicate swerving, and crash it with another entity in space.

To quote someone other than oneself, signers perform *role shift* [@cormier2015rethinking],
where they may physically shift in space to mark the distinction and take on some characteristics of the people they represent.
For example, to recount a dialogue between a taller and a shorter person,
the signer may shift to one side and look up when taking the shorter person's role,
shift to the other side and look down when taking the taller person's role.

###### Fingerspelling {-}
Fingerspelling results from language contact between a signed language and a surrounding spoken language written form [@battison1978lexical;@wilcox1992phonetics;@brentari2001language;@patrie2011fingerspelled].
A set of manual gestures correspond with a written orthography or phonetic system.
This phenomenon, found in most signed languages, is often used to indicate names or places or new concepts from the spoken language but has often become integrated into the signed languages as another linguistic strategy [@padden1998asl;@montemurro2018emphatic].


## Sign Language Representations

Representation is a significant challenge for SLP.
Unlike spoken languages, signed languages have no widely adopted written form.
As signed languages are conveyed through the visual-gestural modality, video recording is the most straightforward way to capture them.
However, as videos include more information than needed for modeling and are expensive to record, store, and transmit,
a lower-dimensional representation has been sought after.

The following figure illustrates each signed language representation we will describe below.
In this demonstration, we deconstruct the video into its individual frames to exemplify the alignment of the annotations between the video and representations.

```{=html}
<object type="image/svg+xml" data="assets/representation/continuous.pdf#toolbar=0&navpanes=0&scrollbar=0" id="continuous-rep"></object>
```

```{=latex}
\newgeometry{left=0cm,right=0cm,top=1.5cm,bottom=1.5cm}
\begin{landscape}
\thispagestyle{empty}
\begin{figure*}
  \centering
  \includegraphics[width=\linewidth]{assets/representation/continuous.pdf}
  \caption{Representations of an American Sign Language phrase with video frames, pose estimations, SignWriting, HamNoSys and glosses. English translation: “What is your name?” \citep{yin-etal-2021-including}}
  \label{fig:continuous}
\end{figure*}
\end{landscape}
\restoregeometry
```

###### Videos {-}
are the most straightforward representation of a signed language and can amply incorporate the information conveyed through signing.
One major drawback of using videos is their high dimensionality:
They usually include more information than needed for modeling and are expensive to store, transmit, and encode.
As facial features are essential in sign, anonymizing raw videos remains an open problem,
limiting the possibility of making these videos publicly available [@isard2020approaches].

###### Skeletal Poses {-} 
reduce the visual cues in videos to skeleton-like wireframes or mesh representing the location of joints. 
This technique has been extensively used in the field of computer vision to estimate human pose from video data, 
where the goal is to determine the spatial configuration of the body at each point in time. 
Although high-quality pose estimation can be achieved using motion capture equipment, such methods are often expensive and intrusive. 
As a result, estimating pose from videos has become the preferred method in recent years [@pose:pishchulin2012articulated;@pose:chen2017adversarial;@pose:cao2018openpose;@pose:alp2018densepose].
Compared to video representations, accurate skeletal poses have a lower complexity and provide a semi-anonymized representation of the human body, while observing relatively low information loss. 
However, they remain a continuous, multidimensional representation that is not adapted to most NLP models.

###### Written notation systems {-}
represent signs as discrete visual features. Some systems are written linearly, and others use graphemes in two dimensions.
While various universal [@writing:sutton1990lessons;@writing:prillwitz1990hamburg] and language-specific notation systems [@writing:stokoe2005sign;@writing:kakumasu1968urubu;@writing:bergman1977tecknad] have been proposed,
no writing system has been adopted widely by any sign language community, and the lack of standards hinders the exchange and unification of resources and applications between projects.
The figure above depicts two universal notation systems:
SignWriting [@writing:sutton1990lessons], a two-dimensional pictographic system,
and HamNoSys [@writing:prillwitz1990hamburg], a linear stream of graphemes designed to be machine-readable.

###### Glosses {-}
are the transcription of signed languages sign-by-sign, with each sign having a unique semantic identifier. 
While various sign language corpus projects have provided guidelines for gloss annotation [@mesch2015gloss;@johnston2016auslan;@konrad2018public], 
a standardized gloss annotation protocol has yet to be established.
Linear gloss annotations have been criticized for their imprecise representation of signed language. 
These annotations fail to capture all the information expressed simultaneously through different cues, 
such as body posture, eye gaze, or spatial relations, leading to a loss of information that can significantly affect downstream performance on SLP tasks [@yin-read-2020-better].


The following table additionally exemplifies the various representations for more isolated signs.
For this example, we use SignWriting as the notation system.
Note that the same sign might have two unrelated glosses, and the same gloss might have multiple valid spoken language translations.

```{=html}
<div id="formats-table" class="table">
```
formats.md
```{=html}
</div>
```


## Tasks

So far, the computer vision community has mainly led the SLP research to focus on processing the visual features in signed language videos.
As a result, current SLP methods do not fully address the linguistic complexity of signed languages.
We survey common SLP tasks and current methods' limitations, drawing on signed languages' linguistic theories.

### Sign Language Detection

Sign language detection [@detection:borg2019sign;@detection:moryossef2020real] is the binary classification task to determine whether a signed language is being used in a given video frame.
A similar task in spoken languages is voice activity detection (VAD) [@sohn1999statistical;@ramirez2004efficient],
the detection of when a human voice is used in an audio signal.
However, as VAD methods often rely on speech-specific representations such as spectrograms, they are not necessarily applicable to videos.


@detection:borg2019sign introduced the classification of frames taken from YouTube videos as either signing or not. 
They take a spatial and temporal approach based on VGG-16 [@simonyan2015very] CNN to encode each frame 
and use a [GRU](https://en.wikipedia.org/wiki/Gated_recurrent_unit) [@cho2014learning] 
to encode the sequence of frames in a window of 20 frames at 5fps.
In addition to the raw frame, they either encode optical-flow history, aggregated motion history, or frame difference.

@detection:moryossef2020real improved upon their method by performing sign language detection in real time.
They identified that sign language use involves movement of the body and, as such, designed a model that works on top of 
estimated human poses rather than directly on the video signal.
They calculate the optical flow norm of every joint detected on the body and apply a shallow yet effective contextualized model
to predict for every frame whether the person is signing or not.

While these recent detection models achieve high performance,
we need well-annotated data that include interference and distractions with non-signing instances for proper real-world evaluation.

### Sign Language Identification

Sign language identification [@identification:gebre2013automatic;@identification:monteiro2016detecting] classifies which signed language is used in a given video.

@identification:gebre2013automatic found that a simple random-forest classifier utilizing the distribution of phonemes can distinguish between British Sign Language (BSL) and Greek Sign Language (ENN) with a 95% F1 score.
This finding is further supported by @identification:monteiro2016detecting, which, based on activity maps in signing space,
manages to differentiate between British Sign Language and
French Sign Language (Langue des Signes Française, LSF) with a 98% F1 score in videos with static backgrounds, 
and between American Sign Language and British Sign Language, with a 70% F1 score for videos mined from popular video-sharing sites. 
The authors attribute their success mainly to the different fingerspelling systems, which are two-handed in the case of BSL and one-handed in the case of ASL and LSF.

Although these pairwise classification results seem promising, better models would be needed for classifying from a large set of signed languages.
These methods only rely on low-level visual features,
while signed languages have several distinctive features on a linguistic level,
such as lexical or structural differences [@mckee2000lexical;@kimmelman2014information;@ferreira1984similarities;@shroyer1984signs] which have not been explored for this task.

### Sign Language Segmentation

Segmentation consists of detecting the frame boundaries for signs or phrases in videos to divide them into meaningful units.
While the most canonical way of dividing a spoken language text is into a linear sequence of words, 
due to the simultaneity of sign language, the notion of a sign language "word" is ill-defined, and sign language cannot be fully linearly modeled.

Current methods resort to segmenting units loosely mapped to signed language units [@segmentation:santemiz2009automatic;@segmentation:farag2019learning;@segmentation:bull2020automatic;@segmentation:renz2021signa;@segmentation:renz2021signb;@segmentation:bull2021aligning], and do not leverage reliable linguistic predictors of sentence boundaries such as prosody in signed languages (i.e., pauses, sign duration, facial expressions, eye apertures) [@sandler2010prosody;@ormel2012prosodic]. @segmentation:de-sisto-etal-2021-defining call for a better understanding of sign language structure, which they believe is the necessary ground for the design and development of sign language recognition and segmentation methodologies.

@segmentation:santemiz2009automatic automatically extract isolated signs from continuous signing by aligning the sequences obtained via speech recognition, modeled by Dynamic Time Warping (DTW) and Hidden Markov Models (HMMs) approaches. 

@segmentation:farag2019learning use a random forest classifier to distinguish frames containing words in Japanese Sign Language based on the composition of spatio-temporal angular and distance features between domain-specific pairs of joint segments.

@segmentation:bull2020automatic segment French Sign Language into subtitle units by detecting the temporal boundaries of subtitles aligned with sign language videos, leveraging a spatio-temporal graph convolutional network with a BiLSTM on 2D skeleton data.

@segmentation:renz2021signa determine the location of temporal boundaries between signs in continuous sign language videos by employing 3D convolutional neural network representations with iterative temporal segment refinement to resolve ambiguities between sign boundary cues. @segmentation:renz2021signb further propose the Changepoint-Modulated Pseudo-Labelling (CMPL) algorithm to solve the problem of source-free domain
adaptation. 

@segmentation:bull2021aligning present a Transformer-based approach to segment sign language videos and align them with subtitles simultaneously, encoding subtitles by BERT and videos by CNN video representations.

<!-- @segmentation:de-sisto-etal-2021-defining introduce a proposal for mapping segments to meaning in the form of an agglomerate of lexical and non-lexical information. -->

### Sign Language Recognition, Translation, and Production

Sign language translation (SLT) commonly refers to the translation of signed language to spoken language [@de2022machine;@muller-etal-2022-findings].
Sign language production is the reverse process of producing a sign language video from spoken language text.
Sign language recognition (SLR) [@adaloglou2020comprehensive] detects and labels signs from a video, either on isolated [@dataset:imashev2020dataset;@dataset:sincan2020autsl] or continuous [@cui2017recurrent;@cihan2018neural;@camgoz2020sign] signs.

In the following graph, we can see a fully connected pentagon where each node is a single data representation, 
and each directed edge represents the task of converting one data representation to another.

We split the graph into two: 

- Every edge to the left, on the orange background, represents a task in computer vision. These tasks are inherently language-agnostic; thus, they generalize between signed languages.
- Every edge to the right, on the blue background, represents a task in natural language processing. These tasks are sign language-specific, requiring a specific sign language lexicon or spoken language tokens.
- Every edge on both backgrounds represents a task requiring a combination of computer vision and natural language processing.

```{=html}
<div class="tasks">
    <span style="font-weight: bold;">Language Agnostic Tasks</span>
    <span style="font-weight: bold;float:right">Language Specific Tasks</span>
    <img src="assets/tasks/tasks.svg" alt="Sign language tasks graph" />
</div>
```

```{=latex}
\begin{minipage}{.5\linewidth}\begin{flushleft}\textbf{Language Agnostic Tasks}\end{flushleft}\end{minipage}
\hfill
\begin{minipage}{.5\linewidth}\begin{flushright}\textbf{Language Specific Tasks}\end{flushright}\end{minipage}

\includegraphics[width=\linewidth]{assets/tasks/tasks.pdf}
```


There are 20 tasks conceptually defined by this graph, with varying amounts of previous research.
Every path between two nodes might or might not be valid, depending on how lossy the tasks in the path are.

---

#### Video-to-Pose

Video-to-Pose---commonly known as pose estimation---is the task of detecting human figures in images and videos, 
so that one could determine, for example, where someone's elbow shows up in an image.
It was shown [@vogler2005analysis] that the face pose correlates with facial non-manual features like head direction.

This area has been thoroughly researched [@pose:pishchulin2012articulated;@pose:chen2017adversarial;@pose:cao2018openpose;@pose:alp2018densepose]
with objectives varying from predicting 2D / 3D poses to a selection of a small specific set of landmarks or a dense mesh of a person.

OpenPose [@pose:cao2018openpose;@pose:simon2017hand;@pose:cao2017realtime;@pose:wei2016cpm] is the first multi-person system to 
jointly detect human body, hand, facial, and foot keypoints (in total 135 keypoints) in 2D on single images.
While their model can estimate the full pose directly from an image in a single inference,
they also suggest a pipeline approach where they first estimate the body pose and then independently estimate 
the hands and face pose by acquiring higher resolution crops around those areas.
Building on the slow pipeline approach, a single network whole body OpenPose model has been proposed [@pose:hidalgo2019singlenetwork], 
which is faster and more accurate for the case of obtaining all keypoints.
With multiple recording angles, OpenPose also offers keypoint triangulation to reconstruct the pose in 3D.

@pose:alp2018densepose take a different approach with DensePose. 
Instead of classifying for every keypoint which pixel is most likely, they suggest similar to semantic segmentation,
for each pixel to classify which body part it belongs to.
Then, for each pixel, knowing the body part, they predict where that pixel is on the body part relative to a 2D projection of a representative body model.
This approach results in the reconstruction of the full-body mesh and allows sampling to find specific keypoints similar to OpenPose.

However, 2D human poses might not be sufficient to fully understand the position and orientation of landmarks in space,
and applying pose estimation per frame does not take the video temporal movement information into account, 
especially in cases of rapid movement, which contain motion blur.

@pose:pavllo20193d developed two methods to convert between 2D poses to 3D poses. 
The first, a supervised method, was trained to use the temporal information between frames to predict the missing Z-axis.
The second is an unsupervised method, leveraging the fact that the 2D poses are merely a projection of an unknown 3D pose
and train a model to estimate the 3D pose and back-project to the input 2D poses. This back projection is a deterministic process, applying constraints on the 3D pose encoder. 
@pose:zelinka2020neural follow a similar process and adds a constraint for bones to stay of a fixed length between frames.

@pose:panteleris2018using suggest converting the 2D poses to 3D using inverse kinematics (IK), a process taken from computer animation and robotics to calculate the variable joint parameters needed to place the end of a kinematic chain, 
such as a robot manipulator or animation character's skeleton in a given position and orientation relative to the start of the chain.
Demonstrating their approach to hand pose estimation, they manually explicitly encode the constraints and limits of each joint, resulting in 26 degrees of freedom.
Then, non-linear least-squares minimization fits a 3D model of the hand to the estimated 2D joint positions, recovering the 3D hand pose.
This process is similar to the back-projection used by @pose:pavllo20193d, except here, no temporal information is being used.

MediaPipe Holistic [@mediapipe2020holistic] attempts to solve the 3D pose estimation problem directly by taking a similar approach to OpenPose,
having a pipeline system to estimate the body, then the face and hands. Unlike OpenPose, the estimated poses are in 3D,
and the pose estimator runs in real-time on CPU, allowing for pose-based sign language models on low-powered mobile devices.
This pose estimation tool is widely available and built for Android, iOS, C++, Python, and the Web using Javascript.


#### Pose-to-Video

Pose-to-Video, also known as motion transfer or skeletal animation in the field of robotics and animation, is the
conversion of a sequence of poses to a video.
This task is the final "rendering" of sign language in a visual modality.

@pose:chan2019everybody demonstrate a semi-supervised approach where they take a set of videos, 
run pose estimation with OpenPose [@pose:cao2018openpose], and learn an image-to-image translation [@isola2017image]
between the rendered skeleton and the original video.
They demonstrate their approach on human dancing, where they can extract poses from a choreography
and render any person as if they were dancing that dance.
They predict two consecutive frames for temporally coherent video results and 
introduce a separate pipeline for a more realistic face synthesis, although still flawed.

@pose:wang2018vid2vid suggest a similar method using DensePose [@pose:alp2018densepose] representations 
in addition to the OpenPose [@pose:cao2018openpose] ones. 
They formalize a different model, with various objectives to optimize for, such as background-foreground separation and
temporal coherence by using the previous two timestamps in the input.

Using the method of @pose:chan2019everybody on "Everybody Dance Now", @pose:girocan2020slrtp asks, "Can Everybody Sign Now"?
They evaluate the generated videos by asking signers various tasks after watching them and comparing the signers' ability to
perform these tasks on the original videos, rendered pose videos, and reconstructed videos.
They show that subjects prefer synthesized videos over skeleton visualizations, 
and that out-of-the-box synthesis methods are not effective enough, 
as subjects struggled to understand the reconstructed videos.

As a direct response, @saunders2020everybody show that like in @pose:chan2019everybody, 
where an adversarial loss is added to specifically generate the face, adding a similar loss to the hand generation process
yields high-resolution, more photo-realistic continuous sign language videos.

[Deepfakes](https://en.wikipedia.org/wiki/Deepfake) is a technique to replace a person in an 
existing image or video with someone else's likeness [@nguyen2019deep]. 
This technique can be used to improve the unrealistic face synthesis resulting from not face-specialized models,
or even replace cartoon faces rendered by animated 3D models. 

---

#### Pose-to-Gloss
Pose-to-Gloss---also known as sign language recognition---is the task of recognizing a sequence of signs from a sequence of poses.
Though some previous works have referred to this as "sign language translation", recognition merely determines the associated label of each sign,
without handling the syntax and morphology of the signed language [@padden1988interaction] to create a spoken language output.
Instead, SLR has often been used as an intermediate step during translation to produce glosses from signed language videos.

@jiang2021sign propose a novel Skeleton Aware Multi-modal Framework with a Global Ensemble Model (GEM) for isolated SLR (SAM-SLR-v2) to learn and fuse multimodal feature representations. Specifically, they use a Sign Language Graph Convolution Network (SL-GCN) to model the embedded dynamics of skeleton keypoints and a Separable Spatial-Temporal Convolution Network (SSTCN) to exploit skeleton features. The proposed late-fusion GEM fuses the skeleton-based predictions with other RGB and depth-based modalities to provide global information and make an accurate SLR prediction.

@dafnis2022bidirectional work on the same modified WLASL dataset as @jiang2021sign, but do not require multimodal data input. Instead, they propose a bidirectional skeleton-based graph convolutional network framework with linguistically motivated parameters and attention to the start and end
frames of signs. They cooperatively use forward and backward data streams, including various sub-streams, as input. They also use pre-training to leverage transfer learning.

@selvaraj-etal-2022-openhands introduce a open-source [OpenHands](https://github.com/AI4Bharat/OpenHands) library, which consists of standardized pose datasets for different existing sign language datasets and trained checkpoints of 4 pose-based isolated sign language recognition models across 6 languages (American, Argentinian, Chinese, Greek, Indian, and Turkish). To address the lack of labelled data, they propose self-supervised pretraining on unlabelled data and curate the largest pose-based pretraining dataset on Indian Sign Language (Indian-SL). They establish that pretraining is effective for sign language recognition by demonstrating improved fine-tuning performance especially in low-resource settings and high crosslingual transfer from Indian-SL to few other sign languages.

The work of @kezar2023improving based on the [OpenHands](https://github.com/AI4Bharat/OpenHands) library explicitly recognize the role of phonology to achieve more accurate isolated sign language recognition (ISLR). To allow additional predictions on phonological characteristics (such as handshape), they combine the phonological annotations in ASL-LEX 2.0 [@sehyr2021asl] with signs in the WLASL 2000 ISLR benchmark [@dataset:li2020word]. Interestingly, @tavella-etal-2022-wlasl construct a similar dataset aiming just for phonological property recognition in American Sign Language (ASL).

#### Gloss-to-Pose

Gloss-to-Pose---subsumed under the task of sign language production---is the task of producing a sequence of poses that adequately represent
a sequence of signs written as gloss.

To produce a sign language video, @stoll2018sign construct a lookup table between glosses and sequences of 2D poses.
They align all pose sequences at the neck joint of a reference skeleton and group all sequences belonging to the same gloss.
Then, for each group, they apply dynamic time warping and average out all sequences in the group to construct the mean pose sequence.
This approach suffers from not having an accurate set of poses aligned to the gloss and from unnatural motion transitions between glosses.

To alleviate the downsides of the previous work, @stoll2020text2sign construct a lookup table of gloss to a group of sequences of poses rather than creating a mean pose sequence.
They build a Motion Graph [@min2012motion], which is a Markov process used to generate new motion sequences that are representative of natural motion,
and select the motion primitives (sequence of poses) per gloss with the highest transition probability.
To smooth that sequence and reduce unnatural motion, they use a Savitzky–Golay motion transition smoothing filter [@savitzky1964smoothing].

---

#### Video-to-Gloss
Video-to-Gloss---also known as sign language recognition---is the task of recognizing a sequence of signs from a video.

For this recognition, @cui2017recurrent constructs a three-step optimization model.
First, they train a video-to-gloss end-to-end model, where they encode the video using a spatio-temporal CNN encoder 
and predict the gloss using a Connectionist Temporal Classification (CTC) [@graves2006connectionist].
Then, from the CTC alignment and category proposal, they encode each gloss-level segment independently, trained to predict the gloss category,
and use this gloss video segments encoding to optimize the sequence learning model. 

@cihan2018neural fundamentally differ from that approach and formulate this problem as if it is a natural-language translation problem.
They encode each video frame using AlexNet [@krizhevsky2012imagenet], initialized using weights trained on ImageNet [@deng2009imagenet].
Then they apply a GRU encoder-decoder architecture with Luong Attention [@luong2015effective] to generate the gloss.
In follow-up work, @camgoz2020sign use a transformer encoder [@vaswani2017attention] to replace the GRU 
and use a CTC to decode the gloss. They show a slight improvement with this approach on the video-to-gloss task.

```{=ignore}
TODO @camgoz2017subunets SubUNets
Camgoz et al. [26] introduce a DNN-based approach for
solving the simultaneous alignment and recognition problems,
typically called "sequence-to-sequence" learning. In
particular, the problem is decomposed by a series
of specialized systems called SubUNets. To solve the task, the goal
is to model the spatio-temporal relationships among these
SubUNets. More specifically, SubUNets allow to inject domain-specific expert knowledge into
the system regarding suitable intermediate representations.
Additionally, they also allow performing transfer-learning between different interrelated tasks implicitly.

TODO @cui2019deep GoogLeNet + TConvs
In contrast to other 2D CNN-based methods that employ
HMMs, Cui et al. [25] propose a model that includes an
extra temporal module (TConvs), after the feature extractor
(GoogLeNet). The TConvs module consists of two 1D CNN
layers and two max pooling layers. It is designed to capture the fine-grained dependencies inside a gloss (intra-gloss dependencies) between consecutive frames into compact per-window feature vectors. Finally, bidirectional RNNs are applied to capture the entire sentence's long-term temporal dependencies. The total architecture is trained iteratively to exploit the expressive capability of DNN models with limited data.

TODO @dataset:joze2018ms I3D
Inflated 3D ConvNet (I3D) [@carreira2017quo] was originally developed
for the task of human action recognition; however, its application has demonstrated outstanding performance on isolated SLR [42]. In particular, the I3D architecture is an
extended version of GoogLeNet, which contains several 3D
convolutional layers followed by 3D max-pooling layers. The
key insight of this architecture is the endowing of the 2D
sub-modules (filters and pooling kernels) with an additional
temporal dimension. This methodology makes learning spatio-temporal features from videos feasible while leveraging efficient known architecture designs and parameters.

TODO @pu2019iterative 3D ResNet+LSTM
Pu et al. [45] propose a framework comprising a 3D CNN
for feature extraction, an RNN for sequence learning, and
two different decoding strategies, one performed with CTC
and the other with an attentional decoder RNN. The glosses
predicted by the attentional decoder are utilized to draw a
warping path using a soft-DTW [47] alignment constraint.
The warping paths display the alignments between glosses
and video segments. The proposed pseudo-alignments are then
employed for iterative optimization.
```

@adaloglou2020comprehensive perform a comparative experimental assessment of computer vision-based methods for the video-to-gloss task.
They implement various approaches from previous research [@camgoz2017subunets;@cui2019deep;@dataset:joze2018ms]
and test them on multiple datasets [@dataset:huang2018video;@cihan2018neural;@dataset:von2007towards;@dataset:joze2018ms]
either for isolated sign recognition or continuous sign recognition.
They conclude that 3D convolutional models outperform models using only recurrent networks to capture the temporal information,
and that these models are more scalable given the restricted receptive field, which results from the CNN "sliding window" technique.

#### Gloss-to-Video
Gloss-to-Video---also known as sign language production---is the task of producing a video that adequately represents
a sequence of signs written as gloss.

As of 2020, no research discusses the direct translation task between gloss and video.
This lack of discussion results from the computational impracticality of the desired model, 
leading researchers to refrain from performing this task directly and instead rely on pipeline approaches using intermediate pose representations.

---

#### Gloss-to-Text
Gloss-to-Text---also known as sign language translation---is the natural language processing task of translating
between gloss text representing sign language signs and spoken language text. 
These texts commonly differ in terminology, capitalization, and sentence structure.

@cihan2018neural experimented with various machine-translation architectures and compared using an LSTM vs. GRU for the recurrent model,
as well as Luong attention [@luong2015effective] vs. Bahdanau attention [@bahdanau2014neural] and various batch sizes. 
They concluded that on the RWTH-PHOENIX-Weather-2014T dataset, which was also presented in this work, 
using GRUs, Luong attention, and a batch size of 1 outperforms all other configurations.

In parallel with the advancements in spoken language machine translation, 
@yin-read-2020-better proposed replacing the RNN with a Transformer [@vaswani2017attention] encoder-decoder model, showing improvements on both RWTH-PHOENIX-Weather-2014T (DGS) and ASLG-PC12 (ASL) datasets both using a single model and ensemble of models.
Interestingly, in gloss-to-text, they show that using the sign language recognition (video-to-gloss) system output outperforms using the gold annotated glosses.

Building on the code published by @yin-read-2020-better, @moryossef-etal-2021-data show it is beneficial to pre-train these translation models
using augmented monolingual spoken language corpora.
They try three different approaches for data augmentation: 
(1) Back-translation; 
(2) General text-to-gloss rules, including lemmatization, word reordering, and dropping of words; 
(3) Language-pair-specific rules augmenting the spoken language syntax to its corresponding sign language syntax.
When pretraining, all augmentations show improvements over the baseline for RWTH-PHOENIX-Weather-2014T (DGS) and NCSLGR (ASL). 

<!-- TODO: gloss translation (Mathias) -->
<!-- @article{muller2022considerations,
  title={Considerations for meaningful sign language machine translation based on glosses},
  author={M{\"u}ller, Mathias and Jiang, Zifan and Moryossef, Amit and Rios, Annette and Ebling, Sarah},
  journal={arXiv preprint arXiv:2211.15464},
  year={2022}
} -->

#### Text-to-Gloss
Text-to-gloss---an instantiation of sign language translation---is the task of translating between a spoken language text and sign language glosses.

@zhao2000machine used a Tree Adjoining Grammar (TAG)-based system to translate English sentences to American Sign Language (ASL) gloss sequences.
They parse the English text and simultaneously assemble an American Sign Language gloss tree, using Synchronous TAGs [@shieber1990synchronous;@shieber1994restricting], 
by associating the ASL elementary trees with the English elementary trees and associating the nodes at which subsequent substitutions or adjunctions can occur.
Synchronous TAGs have been used for machine translation between spoken languages [@abeille1991using], but this is the first application to a signed language.

For the automatic translation of gloss-to-text, @dataset:othman2012english identified the need for a large parallel sign language gloss and spoken language text corpus.
They develop a part-of-speech-based grammar to transform English sentences from the Gutenberg Project ebooks collection [@lebert2008project] into American Sign Language gloss.
Their final corpus contains over 100 million synthetic sentences and 800 million words and is the most extensive English-ASL gloss corpus we know of.
Unfortunately, it is hard to attest to the quality of the corpus, as the authors did not evaluate their method on real English-ASL gloss pairs, and only a small sample of this corpus is available online.

---

#### Video-to-Text
Video-to-text---also known as sign language translation---is the task of translating a raw video to spoken language text.

@camgoz2020sign proposed a single architecture to perform this task that can use both the sign language gloss and 
the spoken language text in joint supervision.
They use the pre-trained spatial embeddings from @koller2019weakly to encode each frame independently and encode the frames with a transformer.
On this encoding, they use a Connectionist Temporal Classification (CTC) [@graves2006connectionist] to classify the sign language gloss.
Using the same encoding, they use a transformer decoder to decode the spoken language text one token at a time.
They show that adding gloss supervision improves the model over not using it and that it outperforms previous video-to-gloss-to-text pipeline approaches [@cihan2018neural].

Following up, @camgoz2020multi propose a new architecture that does not require the supervision of glosses, named "Multi-channel Transformers for Multi-articulatory Sign Language Translation".
In this approach, they crop the signing hand and the face and perform 3D pose estimation to obtain three separate data channels.
They encode each data channel separately using a transformer, then encode all channels together and concatenate the separate channels for each frame.
Like their previous work, they use a transformer decoder to decode the spoken language text, but unlike their previous work,
do not use the gloss as additional supervision. 
Instead, they add two "anchoring" losses to predict the hand shape and mouth shape from each frame independently, 
as silver annotations are available to them using the model proposed in @koller2019weakly.
They conclude that this approach is on-par with previous approaches requiring glosses, 
and so they have broken the dependency upon costly annotated gloss information in the video-to-text task.

@shi-etal-2022-open introduce OpenASL, a large-scale American Sign Language (ASL) - English dataset collected from online video sites (e.g., YouTube), and then propose a set of techniques including sign search as a pretext task for pre-training and fusion of mouthing and handshape features to improve translation quality in the absence of glosses and in the presence of visually challenging data.

@zhang2023sltunet propose a multi-modal, multi-task learning approach to end-to-end sign language translation. The model features shared representations for different modalities such as text and video and is trained jointly on several tasks such as video-to-gloss, gloss-to-text and video-to-text. The approach allows to leverage external data such as parallel data for spoken language machine translation.

<!-- TODO: AFRISIGN (Shester and Mathias at AfricaNLP, ICLR 2023 workshop) -->

#### Text-to-Video
Text-to-Video---also known as sign language production---is the task of producing a video that adequately represents
a spoken language text in sign language.

As of 2020, no research discusses the direct translation task between text and video.
This lack of discussion results from the computational impracticality of the desired model,
leading researchers to refrain from performing this task directly and instead rely on pipeline approaches using intermediate pose representations.

---

#### Pose-to-Text
Pose-to-text---also known as sign language translation---is the task of translating a captured or estimated pose sequence to spoken language text.

@dataset:ko2019neural demonstrate impressive performance on the pose-to-text task by inputting the pose sequence into a
standard encoder-decoder translation network. 
They experiment both with GRU and various types of attention [@luong2015effective;@bahdanau2014neural] and with a Transformer [@vaswani2017attention],
and show similar performance, with the transformer underperforming on the validation set and overperforming on the test set, which consists of unseen signers.
They experiment with various normalization schemes, mainly subtracting the mean and dividing by the standard deviation of every individual keypoint
either concerning the entire frame or the relevant "object" (Body, Face, and Hand).

#### Text-to-Pose
Text-to-Pose---also known as sign language production---is the task of producing a sequence of poses that adequately represent
a spoken language text in sign language, as an intermediate representation to overcome challenges in animation.
Most efforts use poses as an intermediate representation to overcome the challenges in generating videos directly, with the goal of using computer animation or pose-to-video models to perform video production.

@saunders2020progressive propose Progressive Transformers, a model to translate from 
discrete spoken language sentences to continuous 3D sign pose sequences in an autoregressive manner.
Unlike symbolic transformers [@vaswani2017attention], which use a discrete vocabulary and thus can predict an end-of-sequence (`EOS`) token in every step, the progressive transformer predicts a 
$counter ∈ [0,1]$ in addition to the pose.
In inference time, $counter=1$ is considered the end of the sequence.
They test their approach on the RWTH-PHOENIX-Weather-2014T dataset using OpenPose 2D pose estimation,
uplifted to 3D [@pose:zelinka2020neural], and show favorable results when evaluating using back-translation 
from the generated poses to spoken language.
They further show [@saunders2020adversarial] that using an adversarial discriminator between 
the ground truth poses, and the generated poses, conditioned on the input spoken language text improves the production quality as measured using back-translation.

To overcome the issues of under-articulation seen in the above works, 
@saunders2020everybody expands on the progressive transformer model using a 
Mixture Density Network (MDN) [@bishop1994mixture] to model the variation found in sign language.
While this model underperforms on the validation set, compared to previous work, it outperforms on the test set.

@pose:zelinka2020neural present a similar autoregressive decoder approach, with added dynamic-time-warping (DTW) and soft attention.
They test their approach on Czech Sign Language weather data extracted from the news, which is not manually annotated,
or aligned to the spoken language captions, and show their DTW is advantageous for this kind of task.

@xiao2020skeleton close the loop by proposing a text-to-pose-to-text model for the case of isolated sign language recognition.
They first train a classifier to take a sequence of poses encoded by a BiLSTM and classify the relevant sign, then, propose a production system to take a single sign and sample a constant length sequence of 50 poses from a Gaussian Mixture Model.
These components are combined such that given a sign class $y$, a pose sequence is generated, then classified back into a sign class $ŷ$,
and the loss is applied between $y$ and $ŷ$, and not directly on the generated pose sequence.
They evaluate their approach on the CSL dataset [@dataset:huang2018video] and show that their generated pose sequences 
almost reach the same classification performance as the reference sequences.

Due to the need for more suitable automatic evaluation methods for generated signs, existing works resort to measuring back-translation quality, which cannot accurately capture the quality of the produced signs nor their usability in real-world settings.
Understanding how distinctions in meaning are created in signed language may help develop a better evaluation method.

---

#### Notation-to-Text
@jiang2022machine explore text-to-text sign to spoken language translation, with SignWriting as the chosen sign language notation system. 
Despite SignWriting usually represented in 2D, they use the 1D Formal SignWriting specification and propose a neural factored machine translation approach to encode sequences of the SignWriting graphemes as well as their position in the 2D space. 
They verify the proposed approach on the SignBank dataset in both a bilingual setup (American Sign Language to English) and two multilingual setups (4 and 21 signed-to-spoken language pairs, respectively). 
They apply several low-resource machine translation techniques used to improve spoken language translation to similarly improve the performance of sign language translation. 
Their findings validate the use of an intermediate text representation for signed language translation, and pave the way for including sign language translation in natural language processing research.

#### Text-to-Notation
@jiang2022machine also explore the reverse translation direction, i.e., text to SignWriting translation. 
They conduct experiments under a same condition of their multilingual SignWriting to text (4 language pairs) experiment, and again propose a neural factored machine translation approach to decode the graphemes and their position separately. 
They borrow BLEU from spoken language translation to evaluate the predicted graphemes and mean absolute error to evaluate the positional numbers.

@walsh2022changing explore Text to HamNoSys (T2H) translation, with HamNoSys as the target sign language notation system. They experiment with direct T2H and Text to Gloss to HamNoSys (T2G2H) on a subset of the data from the MEINE DGS dataset [@dataset:hanke-etal-2020-extending], where all glosses are mapped to HamNoSys by a dictionary look up. They find that direct T2H translation results in higher BLEU (it still needs to be clarified how well BLEU represents the quality of HamNoSys translations, though). They encode HamNoSys with BPE [@sennrich-etal-2016-neural], and it outperforms character-level and word-level tokenization. They also leverage BERT to create better sentence-level embeddings and use HamNoSys to extract the hand shape of a sign as additional supervision during training.

---

```{=ignore}
#### Pose-to-Notation
TODO

#### Notation-to-Pose
TODO: Ham2Pose

---

#### Video-to-Notation
TODO

#### Notation-to-Video
TODO

---

#### Notation-to-Text
TODO

#### Text-to-Notation
TODO

---

#### Notation-to-Gloss
TODO

#### Gloss-to-Notation
TODO

```


### Fingerspelling 

Fingerspelling is spelling a word letter-by-letter, borrowing from the spoken language alphabet [@battison1978lexical;@wilcox1992phonetics;@brentari2001language;@patrie2011fingerspelled].
This phenomenon, found in most signed languages, often occurs when there is no previously agreed-upon sign for a concept,
like in technical language, colloquial conversations involving names, conversations involving current events,
emphatic forms, and the context of code-switching between the sign language and corresponding spoken language [@padden1998asl;@montemurro2018emphatic].
The relative amount of fingerspelling varies between signed languages, and for American Sign Language (ASL), it accounts for 12–35% of the signed content [@padden2003alphabet].

@patrie2011fingerspelled describe the following terminology to describe three different forms of fingerspelling:

- **Careful**---slower spelling where each letter pose is clearly formed.
- **Rapid**---quick spelling where letters are often not completed and contain remnants of other letters in the word.
- **Lexicalized**---a sign produced by often using no more than two letter-hand-shapes [@battison1978lexical].<br>
For example, lexicalized `ALL` uses `A` and `L`, lexicalized `BUZZ` uses `B` and `Z`, etc...

#### Recognition
Fingerspelling recognition--a sub-task of sign language recognition--is the task of recognizing fingerspelled words from a sign language video.

@dataset:fs18slt introduced a large dataset available for American Sign Language fingerspelling recognition.
This dataset includes both the "careful" and "rapid" forms of fingerspelling collected from naturally occurring videos "in the wild", which are more challenging than studio conditions.
They train a baseline model to take a sequence of images cropped around the signing hand and either use an autoregressive decoder or a CTC.
They found that the CTC outperforms the autoregressive decoder model, but both achieve poor recognition rates (35-41% character level accuracy) compared to human performance (around 82%).

In follow-up work, @dataset:fs18iccv collected nearly an order-of-magnitude larger dataset and designed a new recognition model.
Instead of detecting the signing hand, they detect the face and crop a large area around it. 
Then, they perform an iterative process of zooming in to the hand using visual attention to retain sufficient information in high resolution of the hand.
Finally, like their previous work, they encode the image hand crops sequence and use a CTC to obtain the frame labels.
They show that this method outperforms their original "hand crop" method by 4% and that they can achieve up to 62.3% character-level accuracy using the additional data collected.
Looking through this dataset, we note that the videos in the dataset are taken from longer videos, and as they are cut, they do not retain the signing before the fingerspelling.
This context relates to language modeling, where at first, one fingerspells a word carefully, and when repeating it, might fingerspell it rapidly, 
but the interlocutors can infer they are fingerspelling the same word.

#### Production

Fingerspelling production--a sub-task of sign language production--is the task of producing a fingerspelling video for words.

In its basic form, "Careful" fingerspelling production can be trivially solved using pre-defined letter handshapes interpolation.
@adeline2013fingerspell demonstrates this approach for American Sign Language and English fingerspelling.
They rig a hand armature for each letter in the English alphabet ($N=26$) and generate all ($N^2=676$) transitions between every two letters using interpolation or manual animation.
Then, to fingerspell entire words, they chain pairs of letter transitions.
For example, for the word "CHLOE", they would chain the following transitions sequentially: `#C` `CH` `HL` `LO` `OE` `E#`.

However, to produce life-like animations, one must also consider the rhythm and speed of holding letters, and transitioning between letters, 
as those can affect how intelligible fingerspelling motions are to an interlocutor (@wilcox1992phonetics).
@wheatland2016analysis analyzes both "careful" and "rapid" fingerspelling videos for these features. 
They find that for both forms of fingerspelling, on average, the longer the word, the shorter the transition and hold time.
Furthermore, they find that less time is spent on middle letters on average, and the last letter is held on average for longer than the other letters in the word.
Finally, they use this information to construct an animation system using letter pose interpolation and control the timing using a data-driven statistical model.

## Annotation Tools

##### ELAN - EUDICO Linguistic Annotator
[ELAN](https://archive.mpi.nl/tla/elan) [@wittenburg2006elan] is an annotation tool for audio and video recordings.
With ELAN, a user can add an unlimited number of textual annotations to audio and/or video recordings. 
An annotation can be a sentence, word, gloss, comment, translation, or description of any feature observed in the media. 
Annotations can be created on multiple layers, called tiers, which can be hierarchically interconnected. 
An annotation can either be time-aligned to the media or refer to other existing annotations. 
The content of annotations consists of Unicode text, and annotation documents are stored in an XML format (EAF).
ELAN is open source ([GPLv3](https://en.wikipedia.org/wiki/GNU_General_Public_License#Version_3)), and installation is [available](https://archive.mpi.nl/tla/elan/download) for Windows, macOS, and Linux.
PyMPI [@pympi-1.69] allows for simple python interaction with Elan files.

##### iLex
[iLex](https://www.sign-lang.uni-hamburg.de/ilex/) [@hanke2002ilex] is a tool for sign language lexicography and corpus analysis, 
that combines features found in empirical sign language lexicography and sign language discourse transcription. 
It supports the user in integrated lexicon building while working on the transcription of a corpus and 
offers several unique features considered essential due to the specific nature of signed languages.
iLex binaries are [available](https://www.sign-lang.uni-hamburg.de/ilex/ilex.xml) for macOS.

##### SignStream
[SignStream](http://www.bu.edu/asllrp/SignStream/3/) [@neidle2001signstream] is a tool for linguistic annotations and computer vision research on visual-gestural language data
SignStream installation is only [available](http://www.bu.edu/asllrp/SignStream/3/download-newSS.html) for old macOS versions and is distributed under an MIT license.

##### Anvil - The Video Annotation Research Tool
[Anvil](https://www.anvil-software.org/) [@kipp2001anvil] is a free video annotation tool,
offering multi-layered annotation based on a user-defined coding scheme.
In Anvil, the annotator can see color-coded elements on multiple tracks in time alignment. 
Some special features are cross-level links, non-temporal objects, timepoint tracks, coding agreement analysis, 
3D viewing of motion capture data and a project tool for managing whole corpora of annotation files.
Anvil installation is [available](https://www.anvil-software.org/download/index.html) for Windows, macOS, and Linux.

## Resources

###### Bilingual dictionaries {-}
for signed language [@dataset:mesch2012meaning;@fenlon2015building;@crasborn2016ngt;@dataset:gutierrez2016lse] map a spoken language word or short phrase to a signed language video.
One notable dictionary is, SpreadTheSign\footnote{\url{https://www.spreadthesign.com/}} is a parallel dictionary containing around 23,000 words with up to 41 different spoken-signed language pairs and more than 600,000 videos in total. Unfortunately, while dictionaries may help create lexical rules between languages, they do not demonstrate the grammar or the usage of signs in context.

###### Fingerspelling corpora {-}
usually consist of videos of words borrowed from spoken languages that are signed letter-by-letter. They can be synthetically created [@dataset:dreuw2006modeling] or mined from online resources [@dataset:fs18slt,@dataset:fs18iccv]. However, they only capture one aspect of signed languages.

###### Isolated sign corpora {-}
are collections of annotated single signs. They are synthesized [@dataset:ebling2018smile;@dataset:huang2018video;@dataset:sincan2020autsl;@dataset:hassan-etal-2020-isolated] or mined from online resources [@dataset:joze2018ms;@dataset:li2020word], and can be used for isolated sign language recognition or contrastive analysis of minimal signing pairs [@dataset:imashev2020dataset]. However, like dictionaries, they do not describe relations between signs, nor do they capture coarticulation during the signing, and are often limited in vocabulary size (20-1000 signs)

###### Continuous sign corpora {-}
contain parallel sequences of signs and spoken language.
Available continuous sign corpora are extremely limited, containing 4-6 orders of magnitude fewer sentence pairs than similar corpora for spoken language machine translation [@arivazhagan2019massively].
Moreover, while automatic speech recognition (ASR) datasets contain up to 50,000 hours of recordings [@pratap2020mls], the most extensive continuous sign language corpus contains only 1,150 hours, and only 50 of them are publicly available [@dataset:hanke-etal-2020-extending].
These datasets are usually synthesized [@dataset:databases2007volumes;@dataset:Crasborn2008TheCN;@dataset:ko2019neural;@dataset:hanke-etal-2020-extending] or recorded in studio conditions [@dataset:forster2014extensions,@cihan2018neural], which does not account for noise in real-life conditions. Moreover, some contain signed interpretations of spoken language rather than naturally-produced signs, which may not accurately represent native signing since translation is now a part of the discourse event.


###### Availability {-}
Unlike the vast amount and diversity of available spoken language resources that allow various applications,
signed language resources are scarce and, currently only support translation and production.
Unfortunately, most of the signed language corpora discussed in the literature are either not available for use or available under heavy restrictions and licensing terms. Furthermore, signed language data is especially challenging to anonymize due to the importance of facial and other physical features in signing videos, limiting its open distribution. Developing anonymization with minimal information loss or accurate anonymous representations is a promising research direction.




### Collect Real-World Data

Data is essential to develop any of the core NLP tools previously described, and current efforts in SLP are often limited by the lack of adequate data. We discuss the considerations to keep in mind when building datasets, the challenges of collecting such data, and directions to facilitate data collection.

###### What is Good Signed Language Data? {-}
For SLP models to be deployable, they must be developed using data that represents the real world accurately. What constitutes an ideal signed language dataset is an open question,
we suggest including the following requirements:
(1) a broad domain; (2) sufficient data and vocabulary size; (3) real-world conditions; (4) naturally produced signs; (5) a diverse signer demographic; (6) native signers; and when applicable, (7) dense annotations.

To illustrate the importance of data quality during modeling, @yin-etal-2021-including first take as an example a current benchmark for SLP, the RWTH-PHOENIX-Weather 2014T dataset [@cihan2018neural] of German Sign Language, that does not meet most of the above criteria: it is restricted to the weather domain (1); contains only around 8K segments with 1K unique signs (2); filmed in studio conditions (3); interpreted from German utterances (4); and signed by nine Caucasian interpreters (5,6).
Although this dataset successfully addressed data scarcity issues at the time and successfully rendered results comparable and fueled competitive research, it does not accurately represent signed languages in the real world. On the other hand, the Public DGS Corpus [@dataset:hanke-etal-2020-extending] is an open-domain (1) dataset consisting of 50 hours of natural signing (4) by 330 native signers from various regions in Germany (5,6), annotated with glosses, HamNoSys and German translations (7), meeting all but two requirements we suggest.

They train a gloss-to-text sign language translation transformer [@yin-read-2020-better] on both datasets. On RWTH-PHOENIX-Weather 2014T, they obtain **22.17** BLEU on testing; on Public DGS Corpus, they obtain a mere \textbf{3.2} BLEU. Although Transformers achieve encouraging results on RWTH-PHOENIX-Weather 2014T [@saunders2020progressive;@camgoz2020multi], they fail on more realistic, open-domain data.
These results reveal that, for real-world applications, we need more data to train such models. At the same time, available data is severely limited in size; less data-hungry and more linguistically-informed approaches may be more suitable.
This experiment reveals how it is crucial to use data that accurately represent the complexity and diversity of signed languages to precisely assess what types of methods are suitable and how well our models would deploy to the real world.

###### Challenges of Data Collection {-}
Collecting and annotating signed data in line with the ideal requires more resources than speech or text data, taking up to 600 minutes per minute of an annotated signed language video [@dataset:hanke-etal-2020-extending]. Moreover, annotation usually requires specific knowledge and skills, which makes recruiting or training qualified annotators challenging. Additionally, there is little existing signed language data in the wild openly licensed for use, especially from native signers that are not interpretations of speech.
Therefore, data collection often requires significant efforts and costs of on-site recording.

###### Automating Annotation {-}
One helpful research direction for collecting more data that enables the development of deployable SLP models is creating tools that can simplify or automate parts of the collection and annotation process. One of the most significant bottlenecks in obtaining more adequate signed language data is the time and scarcity of experts required to perform annotation. Therefore, tools that perform automatic parsing, detection of frame boundaries, extraction of articulatory features, suggestions for lexical annotations, and allow parts of the annotation process to be crowdsourced to non-experts, to name a few, have a high potential to facilitate and accelerate the availability of good data.

### Practice Deaf Collaboration

Finally, when working with signed languages, it is vital to keep in mind \emph{who} this technology should benefit and \emph{what} they need.
Researchers in SLP must honor that signed languages belong to the Deaf community and avoid exploiting their language as a commodity [@bird-2020-decolonising].

###### Solving Real Needs {-}

Many efforts in SLP have developed intrusive methods (e.g., requiring signers to wear special gloves), which are often rejected by signing communities and therefore have limited real-world value.
Such efforts are often marketed to perform ``sign language translation" when they, in fact, only identify fingerspelling or recognize a minimal set of isolated signs at best. These approaches oversimplify the rich grammar of signed languages, promote the misconception that signs are solely expressed through the hands, and are considered by the Deaf community as a manifestation of audism, where it is the signers who must make the extra effort to wear additional sensors to be understood by non-signers [@erard2017sign]. To avoid such mistakes, we encourage close Deaf involvement throughout the research process to ensure that we direct our efforts toward applications that will be adopted by signers and do not make false assumptions about signed languages or the needs of signing communities.

###### Building Collaboration {-}
Deaf collaborations and leadership are essential for developing signed language technologies to ensure they address the community's needs and will be adopted, not relying on misconceptions or inaccuracies about signed language [@harris2009research;@kusters2017innovations].
Hearing researchers cannot relate to the deaf experience or fully understand the context in which the tools being developed would be used, nor can they speak for the deaf. Therefore, we encourage creating a long-term collaborative environment between signed language researchers and users so that deaf users can identify meaningful challenges and provide insights on the considerations to take while researchers cater to the signers' needs as the field evolves. We also recommend reaching out to signing communities for reviewing papers on signed languages to ensure an adequate evaluation of this type of research results published at ACL venues. There are several ways to connect with Deaf communities for collaboration: one can seek deaf students in their local community, reach out to schools for the deaf, contact deaf linguists, join a network of researchers of sign-related technologies\footnote{\url{https://www.crest-network.com/}}, and/or participate in deaf-led projects.


### Downloading

Currently, there is no easy way or agreed-upon format to download and load sign language datasets, and as such, evaluation of these datasets is scarce.
As part of this work, we streamlined the loading of available datasets using [Tensorflow Datasets](https://github.com/tensorflow/datasets) [@TFDS].
This tool allows researchers to load large and small datasets alike with a simple command and be comparable to other works.
We make these datasets available using a custom library, [Sign Language Datasets](https://github.com/sign-language-processing/datasets).

```python
import tensorflow_datasets as tfds
import sign_language_datasets.datasets

# Loading a dataset with default configuration
aslg_pc12 = tfds.load("aslg_pc12")

# Loading a dataset with custom configuration
from sign_language_datasets.datasets.config import SignDatasetConfig

config = SignDatasetConfig(
    name="videos_and_poses256x256:12",
    # Specific version
    version="3.0.0",
    # Download, and load dataset videos
    include_video=True,
    # Load videos at constant, 12 fps
    fps=12,
    # Convert videos to a constant resolution, 256x256
    resolution=(256, 256),
    # Download and load Holistic pose estimation
    include_pose="holistic")

rwth_phoenix2014_t = tfds.load(
    name='rwth_phoenix2014_t',
    builder_kwargs=dict(config=config))
```

Furthermore, we follow a unified interface when possible, making attributes the same and comparable between datasets:
```python
{
    "id": tfds.features.Text(),
    "signer": tfds.features.Text() | tf.int32,
    "video": tfds.features.Video(
        shape=(None, HEIGHT, WIDTH, 3)),
    "depth_video": tfds.features.Video(
        shape=(None, HEIGHT, WIDTH, 1)),
    "fps": tf.int32,
    "pose": {
        "data": tfds.features.Tensor(
            shape=(None, 1, POINTS, CHANNELS),
            dtype=tf.float32),
        "conf": tfds.features.Tensor(
            shape=(None, 1, POINTS),
            dtype=tf.float32)
    },
    "gloss": tfds.features.Text(),
    "text": tfds.features.Text()
}
```


The following table contains a curated list of datasets, including various signed languages and data formats:

```{=ignore}
TODO [this thesis](https://scholarsarchive.byu.edu/cgi/viewcontent.cgi?article=6477&context=etd) page 26 has more datasets.
- Spanish Sign Language: María del Carmen Cabeza-Pereiro (cabeza@uvigo.es)
- Estonian Sign Language: ?
- Finnish Sign Language: Juhana Salonen, Antti Kronqvist (juhana.salonen@jyu.fi, antti.r.kronqvist@jyu.fi)
- Danish Sign  Language: Jette H. Kristoffersen, Thomas Troelsgård (jehk@ucc.dk, ttro@ucc.dk)
- GSL - https://arxiv.org/pdf/2007.12530.pdf
- Phoenix SD / SI - J. Forster, C. Schmidt, O. Koller, M. Bellgardt, and H. Ney, "Extensions of the sign language recognition and translation corpus rwth-phoenixweather." in LREC, 2014, pp. 1911–1916.


GSLC - https://www.academia.edu/1990408/GSLC_creation_and_annotation_of_a_Greek_sign_language_corpus_for_HCI
Emailed Eleni and Evita; I need to make sure data is available.

```


```{=latex}
\newgeometry{left=0cm,right=0cm,top=-1.5cm,bottom=-1.5cm}
\begin{landscape}
\hspace{1.5cm}
```
🎥 Video | 👋 Pose | 👄 Mouthing | ✍ Notation | 📋 Gloss | 📜 Text | 🔊 Speech

<div id="datasets-table" class="table">
datasets.md
</div>

```{=latex}
\end{landscape}
\restoregeometry
```

## Other Resources

- iReviews had compiled a list of [Top Resources for Learning (American) Sign Language](https://www.ireviews.com/sign-language-resources)

## Citation

For attribution in academic contexts, please cite this work as:

```bibtex
@misc{moryossef2021slp, 
    title = "{S}ign {L}anguage {P}rocessing", 
    author = "Moryossef, Amit and Goldberg, Yoav",
    howpublished = "\url{https://sign-language-processing.github.io/}",
    year = "2021"
}
```

## References

<div id="refs"></div>

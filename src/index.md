<link rel="stylesheet" href="style.css" />

---
title: "Sign Language Processing"
link-citations: true
...

Sign Language Processing (SLP) is a field of [artificial intelligence](https://en.wikipedia.org/wiki/Artificial_intelligence) 
concerned with automatic processing and analysis of [sign language](https://en.wikipedia.org/wiki/Sign_language) content.
It is a subfield of both [natural language processing](https://en.wikipedia.org/wiki/Natural_language_processing) and 
[computer vision](https://en.wikipedia.org/wiki/Computer_vision).

Challenges in sign language processing frequently involve 
[machine translation of sign languages](https://en.wikipedia.org/wiki/Machine_translation_of_sign_languages)
to written languages (sign language translation) or from written languages (sign language production),
or sign language recognition for sign language understanding.


## Corpora

### Data Formats

The only widely accepted format for sign language data is including videos of the signing, 
and either a [gloss](https://en.wikipedia.org/wiki/Gloss_(annotation)) or a written language translation.
Sign language videos may include a "depth" channel produced by a [time-of-flight camera](https://en.wikipedia.org/wiki/Time-of-flight_camera).

Sign languages have no formal written format. 
There are various language specific notations systems ([si5s](https://en.wikipedia.org/wiki/Si5s), [Stokoe notation](https://en.wikipedia.org/wiki/Stokoe_notation) [@writing:stokoe2005sign])
and various universal notations systems ([SignWriting](https://en.wikipedia.org/wiki/SignWriting), [HamNoSys](https://en.wikipedia.org/wiki/Hamburg_Notation_System) [@writing:prillwitz1990hamburg]) but no writing system has been adopted widely enough, 
by the international Deaf community, that it could be considered the "written form" of a given sign language.

Additionally, sign language corpora may include human [poses](https://en.wikipedia.org/wiki/Pose_(computer_vision)), either recorded with [motion capture](https://en.wikipedia.org/wiki/Motion_capture) technologies,
or estimated from videos using [pose estimation](https://en.wikipedia.org/wiki/Pose_(computer_vision)#Pose_estimation) techniques.
Full body human poses include all the relevant information for sign language processing (manual or non-manual), except for visual cues such as props.

The following table exemplifies the various data formats.
For this example we use [SignWriting](https://en.wikipedia.org/wiki/SignWriting) as the writing system.
Note that the same sign might have two unrelated glosses and the same gloss might have multiple valid texts.

formats.html

### Available Datasets

The following table contains a curated list of datasets including various sign languages and data formats:

datasets.html

Currently, there is no easy way or agreed upon format to download all datasets, and as such, evaluation on these datasets is scarce.

## Tasks


### Sign Language Detection

Sign language detection [@detection:borg2019sign;@detection:moryossef2020real] is defined as the binary-classification for any
given frame of a video whether a person is using sign-language or not.

@detection:borg2019sign introduced the classification of frames taken from YouTube videos as either signing or not. 
They take a spatial and temporal approach based on VGG-16 [@simonyan2014very] CNN to encode each frame 
and use a [GRU](https://en.wikipedia.org/wiki/Gated_recurrent_unit) [@cho2014learning] 
to encode the sequence of frames, in a window of 20 frames at 5fps.
In addition to the raw frame, they also either encode optical flow history, aggregated motion history, or frame difference.

@detection:moryossef2020real improved upon their method by performing the sign language detection in real-time.
They identified that sign language use involves movement of the body, and such designed a model that works on top of 
human poses rather than directly on the video signal.
They calculate the optical flow norm of every joint detected on the body, and apply a small yet effective contextualized model
to predict for every frame whether the person is signing or not.

### Sign Language Identification

Sign language identification [@identification:gebre2013automatic;@identification:monteiro2016detecting] is defined as the classification between two or more sign languages.
 
@identification:gebre2013automatic found that a simple random-forest classifier can distinguish between 
British Sign Language (BSL) and Greek Sign Language (ENN) with a 95\% F1 score.
This finding is further supported by @identification:monteiro2016detecting which manages to differentiate between 
British Sign Language and French Sign Language (Langue des Signes Française, LSF) with 98\% F1 score in videos with static backgrounds,
and between American Sign Language and British Sign Language with 70\% F1 score for videos mined from popular video sharing sites. 
The authors attribute their success mainly to the different fingerspelling systems, which is two-handed in the case of BSL and one-handed in the case of ASL and LSF.

### Sign Language Recognition, Translation and Production

Sign language translation is generally considered the task of translating between a video in sign language to text in a written language.
Sign language production is the reverse process, of producing a sign language video from text in a written language.
Sign language recognition is the task of recognizing the signs themselves in the sign language, but not necessarily the written language text.


In the following graph we can see a fully connected pentagon where each node is a single data representation, 
and each directed edge represents the task of converting between one data representation to another.

We split the graph in 2: 

- Every edge to the left, on the orange background represents a task in computer vision. These tasks are inherently multilingual, thus generalize over all sign languages.
- Every edge to the right, on the blue background represents a task in natural language processing. These tasks are sign language specific, requiring a specific sign language lexicon or written language tokens.
- Every edge on both backgrounds represents a task requiring a combination of computer vision and natural language processing.

<p>
<span style="font-weight: bold;">Computer Vision</span>
<span style="font-weight: bold;float:right">Natural Language Processing</span>
<object type="image/svg+xml" data="assets/tasks.svg" class="logo"></object>
</p>

In total, there are 20 tasks defined by this graph, with varying amount of previous research.
Every path between two nodes might or might not be valid, depending on how lossy the tasks in the path are.

#### Sign Language Translation

Trivially, this is the task of translating between videos directly to text.
However, doing so is computationally expensive in memory, and so videos are capped at being very short.
Moreover, this direct pipeline does not take advantage of the universalities between sign languages,
and requires large amounts of data to cover the various signing styles and diverse population.


##### Video-to-Text
TODO Text

##### Video-to-Pose
TODO Text

##### Video-to-Writing
TODO Text

##### Video-to-Gloss
TODO Text

##### Pose-to-Writing
TODO Text

##### Pose-to-Gloss
TODO Text

##### Pose-to-Text
TODO Text

##### Writing-to-Gloss
TODO Text

##### Writing-to-Text
TODO Text

##### Gloss-to-Text
TODO Text

#### Sign Language Production
TODO Text

##### Text-to-Video
TODO Text

##### Text-to-Gloss
TODO Text

##### Text-to-Writing
TODO Text

##### Text-to-Pose
TODO Text

##### Gloss-to-Writing
TODO Text

##### Gloss-to-Pose
TODO Text

##### Gloss-to-Video
TODO Text

##### Writing-to-Pose
TODO Text

##### Writing-to-Video
TODO Text

##### Pose-to-Text
TODO Text

##### Writing-to-Gloss
TODO Text

##### Pose-to-Video
TODO Text

## References
